#!/usr/bin/env python3
"""Extract official docket detail for denied/NA emergency-application rows.

This script joins the generated denied/non-binary emergency linkage queue to
public Supreme Court docket pages. The output follows the emergency linkage
schema and closes docket-observable fields for the denied/NA slice, but it does
not supply external implementation or downstream policy validation.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import time
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_DIR = ROOT / "data" / "benchmarks"
REPORTS = ROOT / "reports"
SCHEMA = BENCHMARK_DIR / "emergency-application-linkage-schema.csv"
SOURCE_QUEUE = BENCHMARK_DIR / "emergency-application-denied-linkage-workqueue-v1.csv"
DEFAULT_OUTPUT = BENCHMARK_DIR / "emergency-application-denied-linkage-coded-v1.csv"
DEFAULT_MANIFEST = BENCHMARK_DIR / "emergency-application-denied-linkage-coded-v1-manifest.json"
DEFAULT_SUMMARY_CSV = REPORTS / "emergency-application-denied-linkage-coded-summary-v1.csv"
DEFAULT_SUMMARY_MD = REPORTS / "emergency-application-denied-linkage-coded-summary-v1.md"
SOURCE_KEY = "scotus-docket-plus-shadow-docket-v3-0"
OFFICIAL_DOCKET_BASE = "https://www.supremecourt.gov/docket/docketfiles/html/public"
SHADOW_DOCKET_URL = "https://www.shadowdocketdata.com/data"
SUMMARY_FIELDS = [
    "metricKey",
    "observedValue",
    "denominatorSpec",
    "sourceUrl",
    "validationUse",
    "manuscriptUse",
    "notes",
]

MANUAL_LINKED_MERITS = {
    "24A164": {
        "linkedMeritsDocket": "25-1017",
        "linkedMeritsFiledDate": "2026-02-19",
        "linkedMeritsDecisionDate": "",
        "meritsFollowThroughCategory": "cert_granted_merits_pending",
        "linkedMeritsOutcome": "pending",
        "sourceUrl": "https://www.supremecourt.gov/docket/docketfiles/html/public/25-1017.html",
        "verifiedDate": "2026-07-26",
        "note": (
            "The later official merits docket records the certiorari petition filed "
            "2026-02-19 and granted 2026-06-29; merits briefing remained pending "
            "as of 2026-07-26."
        ),
    },
}

FULL_MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def schema_fields() -> list[str]:
    with SCHEMA.open(newline="") as handle:
        return [row["fieldName"] for row in csv.DictReader(handle)]


def docket_url(docket_number: str) -> str:
    return f"{OFFICIAL_DOCKET_BASE}/{docket_number}.html"


def body_is_valid(body: str) -> bool:
    if not body:
        return False
    sample = body[:1000]
    if sample.count("\x00") > 50:
        return False
    return "<html" in body[:500].lower() and "ProceedingDate" in body


def fetch_docket(docket_number: str, attempts: int = 6, sleep_seconds: float = 0.25) -> tuple[str, str, str]:
    url = docket_url(docket_number)
    last_error = ""
    for attempt in range(1, attempts + 1):
        try:
            fetch_url = url if attempt == 1 else f"{url}?nocache={attempt}"
            request = Request(
                fetch_url,
                headers={
                    "User-Agent": "Mozilla/5.0 publication research script",
                    "Accept-Encoding": "identity",
                    "Cache-Control": "no-cache",
                },
            )
            with urlopen(request, timeout=30) as response:
                body = response.read().decode("utf-8", "replace")
            if body_is_valid(body):
                return url, body, "ok"
            last_error = f"invalid or empty proceedings response on attempt {attempt}"
        except (HTTPError, URLError, TimeoutError) as exc:
            last_error = f"{type(exc).__name__}: {exc}"
        if attempt < attempts:
            time.sleep(sleep_seconds)
    return url, "", last_error or "failed to fetch docket"


def strip_tags(fragment: str) -> str:
    text = re.sub(r"<[^>]+>", " ", fragment)
    return " ".join(html.unescape(text).split())


def parse_docket_date(value: str) -> str:
    value = " ".join(value.replace(",", "").split())
    for fmt in ("%b %d %Y", "%B %d %Y"):
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            continue
    return ""


def parse_long_date(value: str) -> str:
    value = " ".join(value.replace(",", "").split())
    for fmt in ("%B %d %Y", "%b %d %Y"):
        try:
            return datetime.strptime(value, fmt).date().isoformat()
        except ValueError:
            continue
    return ""


def proceeding_rows(body: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for table_row in re.findall(r"<tr[^>]*>(.*?)</tr>", body, flags=re.IGNORECASE | re.DOTALL):
        date_match = re.search(
            r'<td[^>]*class=["\']ProceedingDate["\'][^>]*>(.*?)</td>',
            table_row,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if not date_match:
            continue
        cells = re.findall(r"<td[^>]*>(.*?)</td>", table_row, flags=re.IGNORECASE | re.DOTALL)
        if len(cells) < 2:
            continue
        raw_date = strip_tags(date_match.group(1))
        text_cell = cells[1] if strip_tags(cells[0]) == raw_date else cells[-1]
        rows.append({
            "date": parse_docket_date(raw_date),
            "rawDate": raw_date,
            "text": strip_tags(text_cell),
        })
    return rows


def is_application_filing(text: str) -> bool:
    lower = text.lower()
    if "application (" not in lower:
        return False
    if any(word in lower for word in (" denied", " granted", " dismissed", " referred", " distributed")):
        return False
    return any(
        phrase in lower
        for phrase in (
            " for a stay",
            " for stay",
            " for an injunction",
            " for injunction",
            " to vacate",
            " for vacatur",
            " submitted to",
            "presented to",
        )
    )


def first_application_date(rows: list[dict[str, str]]) -> str:
    for row in rows:
        if is_application_filing(row["text"]):
            return row["date"]
    for row in rows:
        if "application (" in row["text"].lower() and row["date"]:
            return row["date"]
    return ""


def response_request_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    output = []
    for row in rows:
        lower = row["text"].lower()
        if "response to application" in lower and "requested" in lower:
            output.append(row)
        elif "response requested" in lower and "application" in lower:
            output.append(row)
    return output


def due_date_from_text(text: str) -> str:
    month_pattern = "|".join(FULL_MONTHS)
    match = re.search(
        rf"(?:on\s+)?(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)?,?\s*"
        rf"({month_pattern})\s+(\d{{1,2}}),\s+(\d{{4}})",
        text,
        flags=re.IGNORECASE,
    )
    if not match:
        return ""
    return parse_long_date(" ".join(match.groups()))


def briefing_window_days(request_rows: list[dict[str, str]]) -> str:
    if not request_rows:
        return ""
    request = request_rows[0]
    due = due_date_from_text(request["text"])
    if not due or not request["date"]:
        return ""
    try:
        return str((date.fromisoformat(due) - date.fromisoformat(request["date"])).days)
    except ValueError:
        return ""


def final_application_texts(rows: list[dict[str, str]], disposition_date: str) -> list[str]:
    disposition_words = re.compile(r"\b(denied|dismissed|granted|vacated|recalled|dissolved)\b", re.IGNORECASE)
    same_day = [
        row["text"]
        for row in rows
        if row["date"] == disposition_date
        and "application" in row["text"].lower()
        and disposition_words.search(row["text"])
    ]
    if same_day:
        return same_day
    same_day_any = [
        row["text"]
        for row in rows
        if row["date"] == disposition_date and disposition_words.search(row["text"])
    ]
    if same_day_any:
        return same_day_any
    fallback = [
        row["text"]
        for row in rows
        if "application" in row["text"].lower() and disposition_words.search(row["text"])
    ]
    return fallback[-2:]


def reasoning_present(final_texts: list[str]) -> str:
    text = " ".join(final_texts).lower()
    markers = (
        "statement of",
        "statement respecting",
        "detached opinion",
        "dissenting",
        "dissent from",
        "concurring",
        "opinion",
        "without prejudice",
        "as moot",
    )
    return "1" if any(marker in text for marker in markers) else "0"


def repeat_filing_flag(rows: list[dict[str, str]]) -> str:
    return "1" if any("refiled" in row["text"].lower() for row in rows) else "0"


def status_quo_effect(row: dict[str, str]) -> str:
    disposition = row.get("dispositionType", "").lower()
    relief = row.get("reliefGranted", "")
    if relief == "0":
        return "requested_emergency_relief_denied_status_quo_preserved"
    if "dismiss" in disposition:
        return "application_dismissed_no_emergency_relief"
    if "granted/denied" in disposition:
        return "mixed_or_partial_emergency_disposition_status_quo_partly_changed"
    return "nonbinary_or_na_docket_status_no_emergency_relief_granted"


def downstream_policy_status(row: dict[str, str]) -> str:
    disposition = row.get("dispositionType", "").lower()
    relief = row.get("reliefGranted", "")
    if relief == "0":
        return "requested_emergency_relief_denied_no_scotus_policy_change"
    if "dismiss" in disposition:
        return "application_dismissed_no_scotus_policy_change"
    if "granted/denied" in disposition:
        return "mixed_or_partial_emergency_disposition_no_external_implementation_coding"
    return "nonbinary_or_na_docket_status_no_external_implementation_coding"


def merits_followthrough_category(row: dict[str, str], rows: list[dict[str, str]]) -> str:
    joined = " ".join(item["text"] for item in rows).lower()
    explicit_denial = (
        "petition for a writ of certiorari is denied" in joined
        or "petition for a writ of certiorari is dismissed" in joined
    )
    if explicit_denial:
        return "cert_or_merits_petition_denied_no_scotus_merits_followthrough"
    if re.search(
            r"\bpetition(?: for a writ of certiorari)?\s+(?:is\s+)?granted\b"
            r"|\bcertiorari\s+(?:is\s+)?granted\b"
            r"|\bprobable jurisdiction noted\b"
            r"|\bset for argument\b",
            joined,
    ):
        return "possible_merits_followthrough_review_required"
    if "application (" in joined:
        return "no_scotus_merits_link_on_application_docket"
    return "official_docket_no_application_merits_link_visible"


def coded_row(source_row: dict[str, str], docket: dict[str, object]) -> dict[str, str]:
    rows = docket["proceedings"]
    assert isinstance(rows, list)
    proceeding_list: list[dict[str, str]] = rows
    request_rows = response_request_rows(proceeding_list)
    final_texts = final_application_texts(proceeding_list, source_row["dispositionDate"])
    application_date = first_application_date(proceeding_list)
    source_url = str(docket["url"])
    output = dict(source_row)
    output.update({
        "sourceKey": SOURCE_KEY,
        "sourceUrl": source_url,
        "applicationDate": application_date,
        "responseRequested": "1" if request_rows else "0",
        "briefingWindowDays": briefing_window_days(request_rows),
        "reasoningPresent": reasoning_present(final_texts),
        "statusQuoEffect": status_quo_effect(source_row),
        "linkedMeritsDocket": "",
        "linkedMeritsFiledDate": "",
        "linkedMeritsDecisionDate": "",
        "meritsFollowThroughCategory": merits_followthrough_category(source_row, proceeding_list),
        "linkedMeritsOutcome": "",
        "downstreamPolicyStatus": downstream_policy_status(source_row),
        "repeatFilingFlag": repeat_filing_flag(proceeding_list),
    })
    manual_link = MANUAL_LINKED_MERITS.get(source_row["docketNumber"])
    if manual_link:
        for field in (
            "linkedMeritsDocket",
            "linkedMeritsFiledDate",
            "linkedMeritsDecisionDate",
            "meritsFollowThroughCategory",
            "linkedMeritsOutcome",
        ):
            output[field] = manual_link[field]
    final_snippet = " ".join(final_texts)[:350] if final_texts else "no final application entry parsed"
    response_note = "response requested" if request_rows else "no court-requested response found"
    filing_note = f"application filed {application_date}" if application_date else "application filing date requires review"
    linked_merits_note = ""
    if manual_link:
        linked_merits_note = (
            f" Linked merits source {manual_link['sourceUrl']} verified "
            f"{manual_link['verifiedDate']}: {manual_link['note']} "
        )
    output["coderNotes"] = (
        f"Official docket page coded for denied/NA emergency slice: {filing_note}; "
        f"{response_note}; final application entry: {final_snippet}. "
        f"{linked_merits_note}"
        "This source row supports all-application docket-linkage fields but not external implementation validation. "
        f"Shadow source row preserved in sourceRecordId; source disposition was {source_row.get('dispositionType', '')}."
    )
    return {field: output.get(field, "") for field in schema_fields()}


def build_summary(rows: list[dict[str, str]], manifest: dict[str, object]) -> list[dict[str, str]]:
    denominator = "210 denied or non-binary/NA full-court emergency-application source-record rows from the compact Shadow Docket v3.0 extract"
    source = "official Supreme Court docket pages joined to compact Shadow Docket v3.0 source-record IDs"
    manuscript_use = "bounded all-application emergency docket-linkage evidence only; not external implementation validation"
    metrics = [
        ("emergencyDeniedNaDocketDetailRows", len(rows), "coded rows in denied/NA official-docket slice"),
        ("emergencyDeniedNaDocketApplicationDateRows", sum(1 for row in rows if row["applicationDate"]), "rows with official docket application filing dates"),
        ("emergencyDeniedNaDocketResponseRequestedRows", sum(1 for row in rows if row["responseRequested"] == "1"), "rows with court-requested response entries"),
        ("emergencyDeniedNaDocketReasoningRows", sum(1 for row in rows if row["reasoningPresent"] == "1"), "rows with docket-visible statement, opinion, mootness, or comparable reason marker"),
        ("emergencyDeniedNaDocketRepeatFilingRows", sum(1 for row in rows if row["repeatFilingFlag"] == "1"), "rows with docket-visible refiling"),
        ("emergencyDeniedNaDocketReviewNeededRows", sum(1 for row in rows if "review_required" in row["meritsFollowThroughCategory"]), "rows with possible merits follow-through requiring manual review before any merits claim"),
    ]
    return [
        {
            "metricKey": key,
            "observedValue": str(value),
            "denominatorSpec": denominator,
            "sourceUrl": source,
            "validationUse": "bounded_denied_na_emergency_docket_linkage",
            "manuscriptUse": manuscript_use,
            "notes": note,
        }
        for key, value, note in metrics
    ]


def write_summary_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=SUMMARY_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_summary_md(path: Path, rows: list[dict[str, str]], manifest: dict[str, object]) -> None:
    lines = [
        "# Emergency Application Denied/NA Linkage Coded Summary v1",
        "",
        "This generated summary describes the official Supreme Court docket-page join for denied and non-binary full-court emergency applications. It supports bounded all-application docket-linkage checks only; it is not external implementation validation.",
        "",
        f"- Snapshot date: {manifest['snapshotDate']}",
        f"- Source rows: {manifest['rowCount']}",
        f"- Unique official docket pages fetched: {manifest['uniqueDocketCount']}",
        f"- Failed fetches: {manifest['failedFetchCount']}",
        "",
        "| Metric | Observed value | Notes |",
        "| --- | ---: | --- |",
    ]
    for row in rows:
        lines.append(f"| `{row['metricKey']}` | {row['observedValue']} | {row['notes']} |")
    lines.extend([
        "",
        "Boundary note:",
        "",
        "- These rows use official docket pages to code application date, response request, reason visibility, status-quo effect, docket-visible merits follow-through category, downstream docket status, and repeat filing for the denied/NA queue. They do not observe external lower-court, agency, or policy implementation after the emergency order.",
    ])
    if manifest.get("manualLinkedMeritsRows"):
        lines.append(
            "- One mixed-disposition source row (24A164) is manually linked to later merits docket 25-1017, "
            "filed February 19, 2026 and granted June 29, 2026; the merits matter remained pending at the "
            f"{manifest.get('linkedMeritsRefreshDate', 'documented')} refresh."
        )
    path.write_text("\n".join(lines) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE_QUEUE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--summary-csv", type=Path, default=DEFAULT_SUMMARY_CSV)
    parser.add_argument("--summary-md", type=Path, default=DEFAULT_SUMMARY_MD)
    parser.add_argument("--snapshot-date", default=date.today().isoformat())
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--sleep", type=float, default=0.25)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source_rows = read_csv(args.source)
    if args.limit:
        source_rows = source_rows[:args.limit]
    dockets = sorted({row["docketNumber"] for row in source_rows})
    docket_data: dict[str, dict[str, object]] = {}
    fetch_errors: dict[str, str] = {}
    for docket_number in dockets:
        url, body, status = fetch_docket(docket_number, sleep_seconds=args.sleep)
        rows = proceeding_rows(body) if body else []
        if status != "ok" or not rows:
            fetch_errors[docket_number] = status if status != "ok" else "no proceeding rows parsed"
        docket_data[docket_number] = {
            "url": url,
            "status": status,
            "proceedings": rows,
        }

    output_rows = [coded_row(row, docket_data[row["docketNumber"]]) for row in source_rows]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=schema_fields(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(output_rows)

    disposition_counts = Counter(row["dispositionType"] for row in output_rows)
    relief_counts = Counter(row["reliefGranted"] for row in output_rows)
    manifest = {
        "generatedBy": Path(__file__).name,
        "snapshotDate": args.snapshot_date,
        "sourceQueue": str(args.source.relative_to(ROOT)),
        "sourceQueueRows": len(source_rows),
        "rowCount": len(output_rows),
        "uniqueDocketCount": len(dockets),
        "failedFetchCount": len(fetch_errors),
        "failedFetches": fetch_errors,
        "officialDocketBase": OFFICIAL_DOCKET_BASE,
        "shadowDocketSourceUrl": SHADOW_DOCKET_URL,
        "dispositionCounts": dict(sorted(disposition_counts.items())),
        "reliefGrantedCounts": dict(sorted(relief_counts.items())),
        "applicationDateRows": sum(1 for row in output_rows if row["applicationDate"]),
        "responseRequestedRows": sum(1 for row in output_rows if row["responseRequested"] == "1"),
        "reasoningPresentRows": sum(1 for row in output_rows if row["reasoningPresent"] == "1"),
        "repeatFilingRows": sum(1 for row in output_rows if row["repeatFilingFlag"] == "1"),
        "sha256": sha256(args.output),
        "linkedMeritsRefreshDate": max(
            (
                MANUAL_LINKED_MERITS[row["docketNumber"]]["verifiedDate"]
                for row in output_rows
                if row["docketNumber"] in MANUAL_LINKED_MERITS
            ),
            default="",
        ),
        "manualLinkedMeritsRows": sum(
            1 for row in output_rows if row["docketNumber"] in MANUAL_LINKED_MERITS
        ),
        "manualLinkedMeritsSources": sorted(
            {
                MANUAL_LINKED_MERITS[row["docketNumber"]]["sourceUrl"]
                for row in output_rows
                if row["docketNumber"] in MANUAL_LINKED_MERITS
            }
        ),
        "notes": (
            "Official docket-page join for the denied/non-binary emergency linkage queue. "
            "This is all-application docket-linkage evidence for docket-visible fields, not external implementation validation."
        ),
    }
    args.manifest.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    summary_rows = build_summary(output_rows, manifest)
    write_summary_csv(args.summary_csv, summary_rows)
    write_summary_md(args.summary_md, summary_rows, manifest)
    print(f"Wrote {args.output} ({len(output_rows)} rows)")
    print(f"Wrote {args.manifest}")
    print(f"Wrote {args.summary_csv}")
    print(f"Wrote {args.summary_md}")
    if fetch_errors:
        print(f"Review needed for {len(fetch_errors)} docket fetches: {', '.join(sorted(fetch_errors)[:10])}")


if __name__ == "__main__":
    main()
