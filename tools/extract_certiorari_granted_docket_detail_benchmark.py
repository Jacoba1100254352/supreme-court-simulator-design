#!/usr/bin/env python3
"""Extract official docket detail for Journal-granted certiorari rows.

This script joins the OT2023 Journal disposition seed to public Supreme Court
docket pages for rows the Journal parser classified as granted or GVR/remand.
The output follows the certiorari cohort schema, but it remains a bounded
granted/GVR docket-detail slice, not a closed filed-petition cohort.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
from collections import Counter
from datetime import date, datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_DIR = ROOT / "data" / "benchmarks"
REPORTS = ROOT / "reports"
SCHEMA = BENCHMARK_DIR / "certiorari-cohort-schema.csv"
SOURCE_EXTRACT = BENCHMARK_DIR / "certiorari-journal-disposition-extract-ot2023.csv"
DEFAULT_OUTPUT = BENCHMARK_DIR / "certiorari-granted-docket-detail-ot2023.csv"
DEFAULT_MANIFEST = BENCHMARK_DIR / "certiorari-granted-docket-detail-ot2023-manifest.json"
DEFAULT_SUMMARY_CSV = REPORTS / "certiorari-granted-docket-detail-summary-v1.csv"
DEFAULT_SUMMARY_MD = REPORTS / "certiorari-granted-docket-detail-summary-v1.md"
SOURCE_KEY = "scotus-docket-plus-journal-granted-ot2023"
OFFICIAL_DOCKET_BASE = "https://www.supremecourt.gov/docket/docketfiles/html/public"
JOURNAL_URL = "https://www.supremecourt.gov/orders/journal/jnl23.pdf"
SUMMARY_FIELDS = [
    "metricKey",
    "observedValue",
    "denominatorSpec",
    "sourceUrl",
    "validationUse",
    "manuscriptUse",
    "notes",
]


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        text = " ".join(data.split())
        if text:
            self.parts.append(text)


def schema_fields() -> list[str]:
    with SCHEMA.open(newline="") as handle:
        return [row["fieldName"] for row in csv.DictReader(handle)]


def read_journal_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return [
            row
            for row in csv.DictReader(handle)
            if row.get("certDisposition") in {"granted", "gvr_or_remand"}
        ]


def docket_url(docket_number: str) -> str:
    return f"{OFFICIAL_DOCKET_BASE}/{docket_number}.html"


def fetch_docket(docket_number: str) -> tuple[str, str]:
    url = docket_url(docket_number)
    request = Request(
        url,
        headers={
            "User-Agent": "SupremeCourtSimulatorResearch/1.0",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8", "replace")
    return url, body


def strip_tags(fragment: str) -> str:
    text = re.sub(r"<[^>]+>", " ", fragment)
    return " ".join(html.unescape(text).split())


def parse_date(value: str) -> str:
    value = " ".join(value.replace(",", "").split())
    for fmt in ("%b %d %Y", "%B %d %Y"):
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            continue
    return ""


def proceeding_rows(body: str) -> list[dict[str, str]]:
    pattern = re.compile(
        r'<td class="ProceedingDate">(?P<date>.*?)</td>\s*<td>(?P<text>.*?)<br\s*/?>',
        re.IGNORECASE | re.DOTALL,
    )
    rows = []
    for match in pattern.finditer(body):
        raw_date = strip_tags(match.group("date"))
        raw_text = strip_tags(match.group("text"))
        rows.append({
            "date": parse_date(raw_date),
            "rawDate": raw_date,
            "text": raw_text,
        })
    return rows


def text_parts(body: str) -> list[str]:
    parser = TextExtractor()
    parser.feed(body)
    return parser.parts


def next_after(parts: list[str], label: str) -> str:
    try:
        index = parts.index(label)
    except ValueError:
        return ""
    if index + 1 >= len(parts):
        return ""
    return parts[index + 1]


def first_row(rows: list[dict[str, str]], predicate) -> dict[str, str] | None:
    for row in rows:
        if predicate(row):
            return row
    return None


def rows_before(rows: list[dict[str, str]], cutoff_date: str) -> list[dict[str, str]]:
    if not cutoff_date:
        return rows
    return [row for row in rows if row["date"] and row["date"] <= cutoff_date]


def response_info(proceedings: list[dict[str, str]], before_grant: list[dict[str, str]]) -> tuple[str, str]:
    respondent_filed = first_row(
        before_grant,
        lambda row: (
            ("brief of respondent" in row["text"].lower() or "memorandum of respondent" in row["text"].lower())
            and "filed" in row["text"].lower()
        ),
    )
    if respondent_filed:
        if "memorandum of respondent" in respondent_filed["text"].lower():
            return "yes", "respondent memorandum"
        return "yes", "respondent brief"
    waiver = first_row(
        proceedings,
        lambda row: "waiver of right of respondent" in row["text"].lower()
        and "to respond filed" in row["text"].lower(),
    )
    if waiver:
        return "waived", "respondent waiver"
    other = first_row(
        before_grant,
        lambda row: "response" in row["text"].lower() and "filed" in row["text"].lower(),
    )
    if other:
        return "yes", "other filed response"
    return "", ""


def sg_recommendation(proceedings: list[dict[str, str]], cvsg_date: str, grant_date: str) -> str:
    candidates = rows_before(proceedings, grant_date)
    if cvsg_date:
        candidates = [row for row in candidates if not row["date"] or row["date"] >= cvsg_date]
    for row in candidates:
        text = row["text"].lower()
        if "brief amicus curiae of united states" not in text and "brief for the united states" not in text:
            continue
        if "supporting vacatur" in text:
            return "supporting vacatur"
        if "supporting reversal" in text:
            return "supporting reversal"
        if "supporting petitioner" in text or "supporting petitioners" in text:
            return "supporting petitioner"
        if "supporting respondent" in text or "supporting respondents" in text:
            return "supporting respondent"
        if "supporting affirmance" in text:
            return "supporting affirmance"
        return "brief filed"
    return ""


def merits_outcome(proceedings: list[dict[str, str]], grant_date: str) -> tuple[str, str, str]:
    later_rows = [row for row in proceedings if row["date"] and (not grant_date or row["date"] > grant_date)]
    for row in later_rows:
        text = row["text"].lower()
        if "dismissed as improvidently granted" in text:
            return row["date"], "dismissed as improvidently granted", ""
        if "judgment reversed" in text:
            return row["date"], "reversed", "yes"
        if "judgment vacated" in text:
            return row["date"], "vacated", "yes"
        if "judgment affirmed" in text:
            return row["date"], "affirmed", "no"
        if "judgment issued" in text:
            continue
    return "", "", ""


def build_row(journal_row: dict[str, str], page_url: str, body: str) -> dict[str, str]:
    proceedings = proceeding_rows(body)
    parts = text_parts(body)
    petition = first_row(
        proceedings,
        lambda row: row["text"].lower().startswith("petition for a writ of certiorari")
        and "filed" in row["text"].lower(),
    )
    response_requested = first_row(proceedings, lambda row: "response requested" in row["text"].lower())
    cvsg = first_row(
        proceedings,
        lambda row: "solicitor general is invited to file a brief" in row["text"].lower()
        or "expressing the views of the united states" in row["text"].lower(),
    )
    grant = first_row(
        proceedings,
        lambda row: "granted" in row["text"].lower()
        and "petition" in row["text"].lower(),
    )
    grant_date = grant["date"] if grant else journal_row.get("dispositionDate", "")
    before_grant = rows_before(proceedings, grant_date)
    response_filed, response_source = response_info(proceedings, before_grant)
    amicus_count = sum(
        1
        for row in before_grant
        if row["text"].lower().startswith("brief amicus curiae")
        or row["text"].lower().startswith("brief amici curiae")
    )
    distribution_count = sum(1 for row in before_grant if row["text"].startswith("DISTRIBUTED for Conference"))
    set_for_argument = any(
        "set for argument" in row["text"].lower()
        for row in proceedings
        if row["date"] and (not grant_date or row["date"] >= grant_date)
    )
    merits_date, merits_result, reversal_or_vacatur = merits_outcome(proceedings, grant_date)
    gvr_or_summary = "yes" if journal_row["certDisposition"] == "gvr_or_remand" else "no"
    if grant and ("vacated" in grant["text"].lower() or "remanded" in grant["text"].lower()):
        gvr_or_summary = "yes"
    lower_court = next_after(parts, "Lower Ct:") or journal_row.get("lowerCourt", "")
    output = {field: "" for field in schema_fields()}
    output.update({
        "sourceKey": SOURCE_KEY,
        "sourceRecordId": f"{journal_row['sourceRecordId']}; docket:{journal_row['docketNumber']}",
        "sourceUrl": page_url,
        "term": journal_row["term"],
        "docketNumber": journal_row["docketNumber"],
        "petitionFiledDate": petition["date"] if petition else "",
        "petitionType": journal_row.get("petitionType", ""),
        "paidOrIfp": journal_row.get("paidOrIfp", ""),
        "lowerCourt": lower_court,
        "responseFiled": response_filed,
        "responseSource": response_source,
        "responseRequestedByCourt": "yes" if response_requested else "no",
        "cfrDate": response_requested["date"] if response_requested else "",
        "cvsgRequested": "yes" if cvsg else "no",
        "cvsgDate": cvsg["date"] if cvsg else "",
        "sgRecommendation": sg_recommendation(proceedings, cvsg["date"] if cvsg else "", grant_date),
        "certStageAmicusCount": str(amicus_count),
        "relistCount": str(max(0, distribution_count - 1)) if distribution_count else "0",
        "dispositionDate": grant_date or journal_row.get("dispositionDate", ""),
        "certDisposition": journal_row["certDisposition"],
        "granted": "yes",
        "grantSetForArgument": "yes" if set_for_argument else "no",
        "gvrOrSummaryDisposition": gvr_or_summary,
        "meritsDocket": journal_row["docketNumber"] if set_for_argument else "",
        "meritsDecisionDate": merits_date,
        "meritsOutcome": merits_result,
        "reversalOrVacatur": reversal_or_vacatur,
        "coderNotes": (
            "Official Supreme Court docket detail joined to the OT2023 Journal granted/GVR disposition seed. "
            "This bounded slice covers Journal-granted and GVR/remand rows only; it is not a closed filing cohort "
            "and does not validate whole-docket CVSG, CFR, specialist-counsel, or split-quality rates."
        ),
    })
    return output


def source_hash(rows: list[dict[str, str]]) -> str:
    payload = json.dumps(rows, sort_keys=True, ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def summary_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    denominator = "OT2023 Journal certiorari rows classified as granted or GVR/remand and joined to official docket pages"
    source_url = "https://www.supremecourt.gov/docket/docket.aspx"

    def metric(key: str, value: int, use: str, notes: str) -> dict[str, str]:
        return {
            "metricKey": key,
            "observedValue": str(value),
            "denominatorSpec": denominator,
            "sourceUrl": source_url,
            "validationUse": "bounded_granted_gvr_docket_detail",
            "manuscriptUse": use,
            "notes": notes,
        }

    return [
        metric(
            "certiorariGrantedDocketDetailRows",
            len(rows),
            "can support bounded granted/GVR docket-detail evidence, not closed petition-cohort validation",
            "One official docket-page row for each Journal granted or GVR/remand source row successfully fetched.",
        ),
        metric(
            "certiorariGrantedDocketPetitionFiledRows",
            sum(1 for row in rows if row["petitionFiledDate"]),
            "can support bounded petition-filed-date completeness for granted/GVR rows only, not closed petition-cohort validation",
            "Petition filing date parsed from official docket proceedings.",
        ),
        metric(
            "certiorariGrantedDocketCfrRows",
            sum(1 for row in rows if row["responseRequestedByCourt"] == "yes"),
            "can support bounded CFR presence among granted/GVR docket-detail rows only, not closed petition-cohort validation",
            "Rows with a docket proceeding labeled Response Requested.",
        ),
        metric(
            "certiorariGrantedDocketCvsgRows",
            sum(1 for row in rows if row["cvsgRequested"] == "yes"),
            "can support bounded CVSG presence among granted/GVR docket-detail rows only, not closed petition-cohort validation",
            "Rows with a docket proceeding inviting the Solicitor General to file a brief.",
        ),
        metric(
            "certiorariGrantedDocketArgumentRows",
            sum(1 for row in rows if row["grantSetForArgument"] == "yes"),
            "can support bounded merits-follow-through evidence for granted/GVR rows only, not closed petition-cohort validation",
            "Rows with a docket proceeding setting the case for oral argument.",
        ),
        metric(
            "certiorariGrantedDocketMeritsOutcomeRows",
            sum(1 for row in rows if row["meritsOutcome"]),
            "can support bounded merits-outcome evidence for argued granted rows only, not closed petition-cohort validation",
            "Rows where a later docket judgment proceeding was classified as affirmed, reversed, vacated, or DIG.",
        ),
    ]


def write_summary_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    lines = [
        "# Certiorari Granted Docket Detail Summary v1",
        "",
        "This report summarizes the official Supreme Court docket-detail join for OT2023 Journal rows classified as granted or GVR/remand. It is bounded granted/GVR evidence only, not a closed filed-petition cohort and not whole-docket CFR, CVSG, counsel, or split-quality validation.",
        "",
        "| Metric | Value | Manuscript use | Notes |",
        "| --- | ---: | --- | --- |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['metricKey']}` | {row['observedValue']} | {row['manuscriptUse']} | {row['notes']} |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def write_manifest(
    path: Path,
    journal_rows: list[dict[str, str]],
    coded_rows: list[dict[str, str]],
    failures: list[dict[str, str]],
    snapshot_date: date,
    output_path: Path,
) -> None:
    disposition_counts = Counter(row["certDisposition"] for row in coded_rows)
    payload = {
        "sourceKey": SOURCE_KEY,
        "sourceName": "Official Supreme Court docket pages joined to OT2023 Journal granted/GVR rows",
        "sourceUrl": "https://www.supremecourt.gov/docket/docket.aspx",
        "sourceJournalUrl": JOURNAL_URL,
        "snapshotDate": snapshot_date.isoformat(),
        "journalGrantedOrGvrRows": len(journal_rows),
        "rowCount": len(coded_rows),
        "failedFetchCount": len(failures),
        "failedFetches": failures,
        "output": output_path.relative_to(ROOT).as_posix(),
        "sourceRecordSha256": source_hash(coded_rows),
        "dispositionCounts": dict(sorted(disposition_counts.items())),
        "notes": [
            "The extract is shaped like the certiorari cohort schema but covers only Journal granted and GVR/remand rows.",
            "Official docket pages add petition filing date, response-request, CVSG, argument, and merits-outcome detail where visible.",
            "This source slice is not a closed filed-petition cohort and cannot validate whole-docket CFR, CVSG, counsel, or split-quality rates.",
        ],
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-date", default=date.today().isoformat())
    parser.add_argument("--source", type=Path, default=SOURCE_EXTRACT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--summary-csv", type=Path, default=DEFAULT_SUMMARY_CSV)
    parser.add_argument("--summary-md", type=Path, default=DEFAULT_SUMMARY_MD)
    parser.add_argument("--limit", type=int, default=0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    snapshot_date = date.fromisoformat(args.snapshot_date)
    journal_rows = read_journal_rows(args.source)
    if args.limit:
        journal_rows = journal_rows[:args.limit]
    coded_rows: list[dict[str, str]] = []
    failures: list[dict[str, str]] = []
    for journal_row in journal_rows:
        docket = journal_row["docketNumber"]
        try:
            url, body = fetch_docket(docket)
        except (HTTPError, URLError, TimeoutError) as exc:
            failures.append({"docketNumber": docket, "error": repr(exc), "sourceUrl": docket_url(docket)})
            continue
        coded_rows.append(build_row(journal_row, url, body))
    if failures:
        raise SystemExit(f"Failed to fetch {len(failures)} docket pages; first failure: {failures[0]}")
    fields = schema_fields()
    write_csv(args.output, coded_rows, fields)
    write_manifest(args.manifest, journal_rows, coded_rows, failures, snapshot_date, args.output)
    summary = summary_rows(coded_rows)
    write_csv(args.summary_csv, summary, SUMMARY_FIELDS)
    write_summary_markdown(args.summary_md, summary)
    print(f"Wrote {args.output.relative_to(ROOT)} ({len(coded_rows)} rows)")
    print(f"Wrote {args.manifest.relative_to(ROOT)}")
    print(f"Wrote {args.summary_csv.relative_to(ROOT)}")
    print(f"Wrote {args.summary_md.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
