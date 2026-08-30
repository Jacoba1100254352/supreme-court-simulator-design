#!/usr/bin/env python3
"""Extract a HUDOC-EXEC monitoring-capacity benchmark slice.

This script queries the official HUDOC-EXEC search endpoint for English
pending leading-case records under Committee of Ministers execution
supervision. The generated CSV is shaped like the implementation/compliance
schema so it can serve as the first direct monitoring-capacity source slice.
It is not a lower-court compliance or government noncompliance benchmark.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "data" / "benchmarks" / "implementation-compliance-schema.csv"
DEFAULT_OUTPUT = ROOT / "data" / "benchmarks" / "ecthr-execution-monitoring-pending-leading-cases-v1.csv"
DEFAULT_MANIFEST = ROOT / "data" / "benchmarks" / "ecthr-execution-monitoring-pending-leading-cases-v1-manifest.json"
DEFAULT_SUMMARY_CSV = ROOT / "reports" / "ecthr-execution-monitoring-summary-v1.csv"
DEFAULT_SUMMARY_MD = ROOT / "reports" / "ecthr-execution-monitoring-summary-v1.md"

SOURCE_KEY = "ecthr-hudoc-exec-pending-leading-cases"
SOURCE_NAME = "HUDOC-EXEC pending leading cases"
SOURCE_URL = "https://hudoc.exec.coe.int/"
SOURCE_HELP_URL = "https://www.coe.int/en/web/execution/hudoc-exec-help"
SOURCE_GLOSSARY_URL = "https://www.coe.int/en/web/execution/glossary"
SOURCE_ANNUAL_REPORT_URL = "https://www.coe.int/en/web/execution/annual-report-2025"
API_ENDPOINT = "https://hudoc.exec.coe.int/app/query/results"
QUERY = (
    "(contentsitename=EXEC AND execdocumenttype:CEC AND execisclosed:False "
    "AND execisprecedent:True AND execlanguage:ENG AND execgroup:MS)"
)
SELECT_FIELDS = [
    "execidentifier",
    "exectitle",
    "execappno",
    "execstate",
    "execgroup",
    "execsupervision",
    "execisclosed",
    "execisprecedent",
    "execlanguage",
    "execjudgmentdateastext",
    "execfinaljudgmentdateastext",
    "execfinalresolutiondateastext",
    "execshortstatusexecution",
    "execapstatus",
    "execmastergroupid",
]
SORT = "execfinaljudgmentdate ascending"
SUPERVISION_LABELS = {
    "ENHA": "enhanced supervision",
    "STAND": "standard supervision",
    "NEW": "awaiting classification",
}
STATUS_LABELS = {
    "": "pending status not shown in selected fields",
    "1": "pending under supervision",
    "2": "action plan or report stage",
    "3": "measures under assessment or supervision",
    "4": "payment or individual-measures follow-up",
    "5": "waiting for information",
    "6": "general measures follow-up",
    "7": "case/group under examination",
    "8": "partial or interim progress",
    "10": "complex or long-running execution issue",
}
SUMMARY_FIELDS = [
    "metricKey",
    "observedValue",
    "denominatorSpec",
    "sourceUrl",
    "validationUse",
    "manuscriptUse",
    "notes",
]


def schema_fields() -> list[str]:
    with SCHEMA.open(newline="") as handle:
        return [row["fieldName"] for row in csv.DictReader(handle)]


def parse_hudoc_date(value: str) -> str:
    clean = (value or "").strip()
    if not clean:
        return ""
    for fmt in ("%d/%m/%Y %H:%M:%S", "%d/%m/%Y"):
        try:
            return datetime.strptime(clean, fmt).date().isoformat()
        except ValueError:
            continue
    return ""


def case_url(identifier: str) -> str:
    return f"https://hudoc.exec.coe.int/?i={urllib.parse.quote(identifier)}"


def query_url(start: int, length: int) -> str:
    params = {
        "query": QUERY,
        "select": ",".join(SELECT_FIELDS),
        "sort": SORT,
        "start": start,
        "length": length,
    }
    return API_ENDPOINT + "?" + urllib.parse.urlencode(params)


def fetch_page(start: int, length: int) -> dict[str, Any]:
    request = urllib.request.Request(
        query_url(start, length),
        headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.load(response)


def fetch_results(page_size: int) -> tuple[int, list[dict[str, str]]]:
    start = 0
    rows: list[dict[str, str]] = []
    result_count: int | None = None
    while True:
        payload = fetch_page(start, page_size)
        result_count = int(payload["resultcount"])
        page_rows = [item.get("columns", {}) for item in payload.get("results", [])]
        rows.extend(page_rows)
        start += len(page_rows)
        if not page_rows or start >= result_count:
            break
    return result_count if result_count is not None else 0, rows


def source_hash(rows: list[dict[str, str]]) -> str:
    payload = json.dumps(rows, sort_keys=True, ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def unresolved_days(final_date: str, snapshot_date: date) -> str:
    if not final_date:
        return ""
    return str((snapshot_date - date.fromisoformat(final_date)).days)


def build_rows(raw_rows: list[dict[str, str]], snapshot_date: date, result_count: int) -> list[dict[str, str]]:
    fields = schema_fields()
    output: list[dict[str, str]] = []
    denominator = (
        "HUDOC-EXEC live query result count for English master/leading execution-case records "
        "with execdocumenttype=CEC, execisclosed=False, execisprecedent=True, execlanguage=ENG, "
        "and execgroup=MS"
    )
    for raw in raw_rows:
        final_date = parse_hudoc_date(raw.get("execfinaljudgmentdateastext", ""))
        judgment_date = parse_hudoc_date(raw.get("execjudgmentdateastext", ""))
        supervision = raw.get("execsupervision", "")
        status = raw.get("execshortstatusexecution", "")
        row = {field: "" for field in fields}
        row.update({
            "sourceKey": SOURCE_KEY,
            "sourceRecordId": raw.get("execidentifier", ""),
            "sourceUrl": case_url(raw.get("execidentifier", "")),
            "sourceSlice": "monitoring-capacity",
            "jurisdiction": "Council of Europe / " + raw.get("execstate", ""),
            "decisionId": raw.get("execappno", ""),
            "decisionDate": judgment_date,
            "decidingCourt": "European Court of Human Rights",
            "caseName": raw.get("exectitle", ""),
            "sourceDecisionType": "ECHR leading case under execution supervision",
            "sourceRecordDate": snapshot_date.isoformat(),
            "monitoringBody": "Committee of Ministers of the Council of Europe",
            "reportingInterval": "live HUDOC-EXEC record; annual Committee of Ministers reporting context",
            "complianceStatus": "pending under supervision",
            "unresolvedDurationDays": unresolved_days(final_date or judgment_date, snapshot_date),
            "enforcementCapacity": SUPERVISION_LABELS.get(supervision, supervision),
            "enforcementStep": STATUS_LABELS.get(status, "HUDOC-EXEC status code " + status),
            "measurementDenominator": denominator,
            "denominatorReconciled": f"yes: {len(raw_rows)} rows match API resultcount {result_count}",
            "coderNotes": (
                "Coded by tools/extract_ecthr_execution_monitoring_benchmark.py on "
                f"{snapshot_date.isoformat()}. Raw HUDOC-EXEC fields preserved in manifest; supervision="
                f"{supervision}; shortStatusExecution={status}; apStatus={raw.get('execapstatus', '')}; "
                f"execstate={raw.get('execstate', '')}; execmastergroupid={raw.get('execmastergroupid', '')}. "
                "This is a monitoring-capacity benchmark slice only, not a doctrinal uptake or practical "
                "government-noncompliance measure."
            ),
        })
        output.append(row)
    return sorted(output, key=lambda item: (
        item.get("decisionDate", ""),
        item.get("sourceRecordId", ""),
        item.get("decisionId", ""),
    ))


def summary_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    by_supervision = Counter(row["enforcementCapacity"] for row in rows)
    long_pending = sum(
        1
        for row in rows
        if row.get("unresolvedDurationDays") and int(row["unresolvedDurationDays"]) >= 365 * 5
    )
    denominator = "English HUDOC-EXEC pending leading-case rows in generated extract"
    return [
        {
            "metricKey": "ecthrHudocExecPendingLeadingRows",
            "observedValue": str(len(rows)),
            "denominatorSpec": denominator,
            "sourceUrl": SOURCE_URL,
            "validationUse": "direct_monitoring_slice",
            "manuscriptUse": "can support bounded monitoring-capacity evidence, not lower-court compliance validation",
            "notes": "Rows reconcile to the live HUDOC-EXEC API result count for the documented query.",
        },
        {
            "metricKey": "ecthrHudocExecEnhancedSupervisionRows",
            "observedValue": str(by_supervision.get("enhanced supervision", 0)),
            "denominatorSpec": denominator,
            "sourceUrl": SOURCE_URL,
            "validationUse": "direct_monitoring_slice",
            "manuscriptUse": "can support bounded enhanced-supervision monitoring-capacity evidence",
            "notes": "Rows with execsupervision=ENHA.",
        },
        {
            "metricKey": "ecthrHudocExecStandardSupervisionRows",
            "observedValue": str(by_supervision.get("standard supervision", 0)),
            "denominatorSpec": denominator,
            "sourceUrl": SOURCE_URL,
            "validationUse": "direct_monitoring_slice",
            "manuscriptUse": "can support bounded standard-supervision monitoring-capacity evidence",
            "notes": "Rows with execsupervision=STAND.",
        },
        {
            "metricKey": "ecthrHudocExecNewClassificationRows",
            "observedValue": str(by_supervision.get("awaiting classification", 0)),
            "denominatorSpec": denominator,
            "sourceUrl": SOURCE_URL,
            "validationUse": "direct_monitoring_slice",
            "manuscriptUse": "can support bounded awaiting-classification monitoring-capacity evidence",
            "notes": "Rows with execsupervision=NEW.",
        },
        {
            "metricKey": "ecthrHudocExecPendingOverFiveYearsRows",
            "observedValue": str(long_pending),
            "denominatorSpec": denominator,
            "sourceUrl": SOURCE_URL,
            "validationUse": "direct_monitoring_slice",
            "manuscriptUse": "can support bounded long-pending monitoring-capacity evidence",
            "notes": "Computed from final-judgment or judgment date to the snapshot date.",
        },
    ]


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_manifest(
    path: Path,
    raw_rows: list[dict[str, str]],
    coded_rows: list[dict[str, str]],
    result_count: int,
    snapshot_date: date,
    output_path: Path,
) -> None:
    by_supervision = Counter(row.get("execsupervision", "") for row in raw_rows)
    by_short_status = Counter(row.get("execshortstatusexecution", "") for row in raw_rows)
    payload = {
        "sourceKey": SOURCE_KEY,
        "sourceName": SOURCE_NAME,
        "sourceUrl": SOURCE_URL,
        "sourceHelpUrl": SOURCE_HELP_URL,
        "sourceGlossaryUrl": SOURCE_GLOSSARY_URL,
        "sourceAnnualReportUrl": SOURCE_ANNUAL_REPORT_URL,
        "apiEndpoint": API_ENDPOINT,
        "query": QUERY,
        "select": SELECT_FIELDS,
        "sort": SORT,
        "snapshotDate": snapshot_date.isoformat(),
        "resultCount": result_count,
        "rowCount": len(coded_rows),
        "rawResultSha256": source_hash(raw_rows),
        "output": output_path.relative_to(ROOT).as_posix(),
        "supervisionCodeCounts": dict(sorted(by_supervision.items())),
        "shortStatusExecutionCodeCounts": dict(sorted(by_short_status.items())),
        "notes": [
            "The extract reconciles to the live HUDOC-EXEC API result count for the documented query.",
            "The extract is a direct monitoring-capacity source slice, not a lower-court doctrinal-uptake or government-noncompliance benchmark.",
            "The annual report URL is included for official execution-reporting context; this live API slice is not forced to match the static 2025 annual-report aggregate.",
        ],
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def write_summary_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    lines = [
        "# ECtHR Execution Monitoring Summary v1",
        "",
        "This report summarizes the generated HUDOC-EXEC pending leading-case monitoring slice. It is direct row-level monitoring evidence for the implementation/compliance workqueue's monitoring-capacity slice, not validation evidence for lower-court compliance, implementation resistance, government noncompliance, or emergency downstream effects.",
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-date", default=date.today().isoformat())
    parser.add_argument("--page-size", type=int, default=500)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--summary-csv", type=Path, default=DEFAULT_SUMMARY_CSV)
    parser.add_argument("--summary-md", type=Path, default=DEFAULT_SUMMARY_MD)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    snapshot_date = date.fromisoformat(args.snapshot_date)
    result_count, raw_rows = fetch_results(args.page_size)
    if result_count != len(raw_rows):
        raise SystemExit(f"Expected {result_count} API rows, fetched {len(raw_rows)}")
    coded_rows = build_rows(raw_rows, snapshot_date, result_count)
    write_csv(args.output, coded_rows, schema_fields())
    write_manifest(args.manifest, raw_rows, coded_rows, result_count, snapshot_date, args.output)
    summary = summary_rows(coded_rows)
    write_csv(args.summary_csv, summary, SUMMARY_FIELDS)
    write_summary_markdown(args.summary_md, summary)
    print(f"Wrote {args.output.relative_to(ROOT)} ({len(coded_rows)} rows)")
    print(f"Wrote {args.manifest.relative_to(ROOT)}")
    print(f"Wrote {args.summary_csv.relative_to(ROOT)}")
    print(f"Wrote {args.summary_md.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
