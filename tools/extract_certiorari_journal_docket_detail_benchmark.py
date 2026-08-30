#!/usr/bin/env python3
"""Join all OT2023 Journal certiorari disposition rows to official dockets.

This source slice improves docket-visible petition-stage detail for the
Journal disposition seed. It is still not a closed filed-petition cohort: the
denominator is the official Journal disposition extract, not all petitions
filed during the term.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError

import extract_certiorari_granted_docket_detail_benchmark as docket


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_DIR = ROOT / "data" / "benchmarks"
REPORTS = ROOT / "reports"
SCHEMA = BENCHMARK_DIR / "certiorari-cohort-schema.csv"
SOURCE_EXTRACT = BENCHMARK_DIR / "certiorari-journal-disposition-extract-ot2023.csv"
DEFAULT_OUTPUT = BENCHMARK_DIR / "certiorari-journal-docket-detail-ot2023.csv"
DEFAULT_MANIFEST = BENCHMARK_DIR / "certiorari-journal-docket-detail-ot2023-manifest.json"
DEFAULT_SUMMARY_CSV = REPORTS / "certiorari-journal-docket-detail-summary-v1.csv"
DEFAULT_SUMMARY_MD = REPORTS / "certiorari-journal-docket-detail-summary-v1.md"
SOURCE_KEY = "scotus-docket-plus-journal-disposition-ot2023"
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
BOUNDARY_NOTE = (
    "Official Supreme Court docket detail joined to the full OT2023 Journal "
    "certiorari disposition seed. This bounded slice covers Journal disposition "
    "rows, not a closed filing cohort, and does not validate denominator-wide "
    "specialist-counsel or split-quality rates."
)


def schema_fields() -> list[str]:
    with SCHEMA.open(newline="") as handle:
        return [row["fieldName"] for row in csv.DictReader(handle)]


def read_journal_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def source_hash(rows: list[dict[str, str]]) -> str:
    payload = json.dumps(rows, sort_keys=True, ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def safe_relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def first_before(
        proceedings: list[dict[str, str]],
        disposition_date: str,
        predicate,
) -> dict[str, str] | None:
    rows = docket.rows_before(proceedings, disposition_date)
    return docket.first_row(rows, predicate)


def response_requested_row(proceedings: list[dict[str, str]], disposition_date: str) -> dict[str, str] | None:
    return first_before(
        proceedings,
        disposition_date,
        lambda row: "response requested" in row["text"].lower(),
    )


def cvsg_row(proceedings: list[dict[str, str]], disposition_date: str) -> dict[str, str] | None:
    return first_before(
        proceedings,
        disposition_date,
        lambda row: (
            "solicitor general is invited to file a brief" in row["text"].lower()
            or "expressing the views of the united states" in row["text"].lower()
        ),
    )


def petition_row(proceedings: list[dict[str, str]]) -> dict[str, str] | None:
    return docket.first_row(
        proceedings,
        lambda row: row["text"].lower().startswith("petition for a writ of certiorari")
        and "filed" in row["text"].lower(),
    )


def amicus_count(proceedings: list[dict[str, str]], disposition_date: str) -> int:
    before_disposition = docket.rows_before(proceedings, disposition_date)
    return sum(
        1
        for row in before_disposition
        if row["text"].lower().startswith("brief amicus curiae")
        or row["text"].lower().startswith("brief amici curiae")
    )


def relist_count(proceedings: list[dict[str, str]], disposition_date: str) -> str:
    before_disposition = docket.rows_before(proceedings, disposition_date)
    distribution_count = sum(1 for row in before_disposition if row["text"].startswith("DISTRIBUTED for Conference"))
    return str(max(0, distribution_count - 1)) if distribution_count else "0"


def argument_set(proceedings: list[dict[str, str]], disposition_date: str) -> bool:
    return any(
        "set for argument" in row["text"].lower()
        for row in proceedings
        if row["date"] and (not disposition_date or row["date"] >= disposition_date)
    )


def build_row(journal_row: dict[str, str], page_url: str, body: str) -> dict[str, str]:
    proceedings = docket.proceeding_rows(body)
    parts = docket.text_parts(body)
    disposition_date = journal_row.get("dispositionDate", "")
    petition = petition_row(proceedings)
    response_requested = response_requested_row(proceedings, disposition_date)
    cvsg = cvsg_row(proceedings, disposition_date)
    before_disposition = docket.rows_before(proceedings, disposition_date)
    response_filed, response_source = docket.response_info(proceedings, before_disposition)
    if not response_filed:
        response_filed = "no"
    set_for_argument = argument_set(proceedings, disposition_date)
    merits_date, merits_result, reversal_or_vacatur = docket.merits_outcome(proceedings, disposition_date)
    granted = "yes" if journal_row.get("granted") == "1" else "no"
    gvr_or_summary = "yes" if journal_row.get("gvrOrSummaryDisposition") == "1" else "no"
    lower_court = docket.next_after(parts, "Lower Ct:") or journal_row.get("lowerCourt", "")
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
        "sgRecommendation": docket.sg_recommendation(proceedings, cvsg["date"] if cvsg else "", disposition_date),
        "certStageAmicusCount": str(amicus_count(proceedings, disposition_date)),
        "relistCount": relist_count(proceedings, disposition_date),
        "dispositionDate": disposition_date,
        "certDisposition": journal_row["certDisposition"],
        "granted": granted,
        "grantSetForArgument": "yes" if set_for_argument else "no",
        "gvrOrSummaryDisposition": gvr_or_summary,
        "meritsDocket": journal_row["docketNumber"] if set_for_argument else "",
        "meritsDecisionDate": merits_date,
        "meritsOutcome": merits_result,
        "reversalOrVacatur": reversal_or_vacatur,
        "coderNotes": BOUNDARY_NOTE,
    })
    return output


def fetch_and_build(index: int, journal_row: dict[str, str]) -> tuple[int, dict[str, str] | None, dict[str, str] | None]:
    docket_number = journal_row["docketNumber"]
    try:
        url, body = docket.fetch_docket(docket_number)
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        failure = {
            "index": str(index),
            "docketNumber": docket_number,
            "sourceRecordId": journal_row.get("sourceRecordId", ""),
            "sourceUrl": docket.docket_url(docket_number),
            "error": repr(exc),
        }
        return index, None, failure
    return index, build_row(journal_row, url, body), None


def build_rows(journal_rows: list[dict[str, str]], workers: int) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    coded_by_index: dict[int, dict[str, str]] = {}
    failures: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(fetch_and_build, index, row)
            for index, row in enumerate(journal_rows)
        ]
        for future in as_completed(futures):
            index, coded_row, failure = future.result()
            if coded_row is not None:
                coded_by_index[index] = coded_row
            if failure is not None:
                failures.append(failure)
    coded_rows = [coded_by_index[index] for index in sorted(coded_by_index)]
    failures.sort(key=lambda row: int(row["index"]))
    return coded_rows, failures


def summary_rows(
        rows: list[dict[str, str]],
        source_row_count: int,
        failed_fetch_count: int,
) -> list[dict[str, str]]:
    denominator = "OT2023 Journal certiorari disposition rows with reachable official Supreme Court docket pages"
    source_url = "https://www.supremecourt.gov/docket/docket.aspx"

    def metric(key: str, value: int, use: str, notes: str) -> dict[str, str]:
        return {
            "metricKey": key,
            "observedValue": str(value),
            "denominatorSpec": denominator,
            "sourceUrl": source_url,
            "validationUse": "bounded_journal_disposition_docket_detail",
            "manuscriptUse": use,
            "notes": notes,
        }

    return [
        metric(
            "certiorariJournalDocketSourceRows",
            source_row_count,
            "keeps the Journal disposition denominator visible before any closed-cohort claim",
            "Total OT2023 Journal certiorari disposition seed rows attempted.",
        ),
        metric(
            "certiorariJournalDocketFailedFetchRows",
            failed_fetch_count,
            "must remain a public-docket coverage limitation until official pages or another source covers these rows",
            "Journal seed rows whose official static docket page was not reachable by the extractor.",
        ),
        metric(
            "certiorariJournalDocketDetailRows",
            len(rows),
            "can support bounded reachable-public-docket detail evidence, not closed filed-petition validation",
            "One official docket-page row for each Journal disposition seed row successfully fetched.",
        ),
        metric(
            "certiorariJournalDocketPetitionFiledRows",
            sum(1 for row in rows if row["petitionFiledDate"]),
            "can support bounded petition-filed-date coverage for Journal disposition rows only",
            "Petition filing date parsed from official docket proceedings.",
        ),
        metric(
            "certiorariJournalDocketResponseFiledRows",
            sum(1 for row in rows if row["responseFiled"] in {"yes", "waived"}),
            "can support bounded response-stage coverage for Journal disposition rows only",
            "Rows with filed respondent briefs, memoranda, other response filings, or waiver entries.",
        ),
        metric(
            "certiorariJournalDocketCfrRows",
            sum(1 for row in rows if row["responseRequestedByCourt"] == "yes"),
            "can support bounded CFR presence among Journal disposition rows only",
            "Rows with a docket proceeding labeled Response Requested.",
        ),
        metric(
            "certiorariJournalDocketCvsgRows",
            sum(1 for row in rows if row["cvsgRequested"] == "yes"),
            "can support bounded CVSG presence among Journal disposition rows only",
            "Rows with a docket proceeding inviting the Solicitor General to file a brief.",
        ),
        metric(
            "certiorariJournalDocketAmicusRows",
            sum(1 for row in rows if int(row["certStageAmicusCount"] or "0") > 0),
            "can support bounded cert-stage amicus visibility for Journal disposition rows only",
            "Rows with at least one docket-visible cert-stage amicus brief before disposition.",
        ),
        metric(
            "certiorariJournalDocketRelistedRows",
            sum(1 for row in rows if int(row["relistCount"] or "0") > 0),
            "can support bounded relist visibility for Journal disposition rows only",
            "Rows with more than one docket-visible distribution before disposition.",
        ),
        metric(
            "certiorariJournalDocketGrantedRows",
            sum(1 for row in rows if row["granted"] == "yes"),
            "must remain bounded to Journal disposition rows only until it reconciles to the Journal granted/GVR count",
            "Rows marked granted by the Journal disposition seed.",
        ),
    ]


def write_summary_markdown(path: Path, rows: list[dict[str, str]], failures: list[dict[str, str]]) -> None:
    lines = [
        "# Certiorari Journal Docket Detail Summary v1",
        "",
        "This report summarizes the official Supreme Court docket-page join for all OT2023 Journal certiorari disposition seed rows. It is bounded Journal-disposition docket-detail evidence only, not a closed filed-petition cohort and not denominator-wide specialist-counsel or split-quality validation.",
        "",
        f"- Failed docket fetches: {len(failures)}",
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
        workers: int,
) -> None:
    disposition_counts = Counter(row["certDisposition"] for row in coded_rows)
    paid_ifp_counts = Counter(row["paidOrIfp"] for row in coded_rows)
    payload = {
        "sourceKey": SOURCE_KEY,
        "sourceName": "Official Supreme Court docket pages joined to OT2023 Journal disposition rows",
        "sourceUrl": "https://www.supremecourt.gov/docket/docket.aspx",
        "sourceJournalUrl": JOURNAL_URL,
        "snapshotDate": snapshot_date.isoformat(),
        "journalDispositionRows": len(journal_rows),
        "rowCount": len(coded_rows),
        "failedFetchCount": len(failures),
        "failedFetches": failures,
        "workers": workers,
        "output": safe_relative(output_path),
        "sourceRecordSha256": source_hash(coded_rows),
        "dispositionCounts": dict(sorted(disposition_counts.items())),
        "paidOrIfpCounts": dict(sorted(paid_ifp_counts.items())),
        "notes": [
            "The extract is shaped like the certiorari cohort schema and covers the full OT2023 Journal disposition seed.",
            "Official docket pages add petition filing date, response, CFR, CVSG, amicus, relist, and merits-detail fields where visible.",
            "The source unit remains Journal disposition rows, not all petitions filed during OT2023.",
            "This source slice is not a closed filed-petition cohort and cannot validate denominator-wide specialist-counsel or split-quality rates.",
        ],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
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
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument(
        "--allow-failures",
        action="store_true",
        help="write reachable docket rows and record failed fetches instead of aborting",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    snapshot_date = date.fromisoformat(args.snapshot_date)
    journal_rows = read_journal_rows(args.source)
    if args.limit:
        journal_rows = journal_rows[:args.limit]
    workers = max(1, args.workers)
    coded_rows, failures = build_rows(journal_rows, workers)
    if failures and not args.allow_failures:
        raise SystemExit(f"Failed to fetch {len(failures)} docket pages; first failure: {failures[0]}")
    fields = schema_fields()
    write_csv(args.output, coded_rows, fields)
    write_manifest(args.manifest, journal_rows, coded_rows, failures, snapshot_date, args.output, workers)
    summary = summary_rows(coded_rows, len(journal_rows), len(failures))
    write_csv(args.summary_csv, summary, SUMMARY_FIELDS)
    write_summary_markdown(args.summary_md, summary, failures)
    print(f"Wrote {safe_relative(args.output)} ({len(coded_rows)} rows)")
    print(f"Wrote {safe_relative(args.manifest)}")
    print(f"Wrote {safe_relative(args.summary_csv)}")
    print(f"Wrote {safe_relative(args.summary_md)}")


if __name__ == "__main__":
    main()
