#!/usr/bin/env python3
"""Build a retrieval workqueue for Journal docket-detail failed fetches."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_DIR = ROOT / "data" / "benchmarks"
REPORTS = ROOT / "reports"
JOURNAL_EXTRACT = BENCHMARK_DIR / "certiorari-journal-disposition-extract-ot2023.csv"
JOURNAL_DOCKET_MANIFEST = BENCHMARK_DIR / "certiorari-journal-docket-detail-ot2023-manifest.json"
OUTPUT_CSV = REPORTS / "certiorari-journal-docket-retrieval-workqueue-v1.csv"
OUTPUT_MD = REPORTS / "certiorari-journal-docket-retrieval-workqueue-v1.md"
FIELDS = [
    "workQueueRank",
    "sourceRecordId",
    "docketNumber",
    "paidOrIfp",
    "certDisposition",
    "dispositionDate",
    "lowerCourt",
    "staticDocketUrl",
    "failedFetchError",
    "retrievalPriority",
    "retrievalAction",
    "denominatorRole",
    "completionEvidence",
    "manuscriptUse",
]
MANUSCRIPT_USE = (
    "not validation evidence; retrieval queue for failed official static docket pages before "
    "any closed filed-petition validation claim"
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def priority(row: dict[str, str]) -> str:
    disposition = row["certDisposition"]
    paid_or_ifp = row["paidOrIfp"]
    if disposition in {"granted", "gvr_or_remand"}:
        return "priority_1_granted_gvr_crosscheck"
    if paid_or_ifp == "paid":
        return "priority_2_paid_petition_denominator"
    if disposition == "dismissed":
        return "priority_4_dismissed_or_misc_boundary"
    return "priority_3_ifp_petition_denominator"


def retrieval_action(row: dict[str, str]) -> str:
    if row["certDisposition"] in {"granted", "gvr_or_remand"}:
        return (
            "retry official static docket page, then cross-check against the granted/GVR "
            "official-docket detail extract and manually search the official docket if still blocked"
        )
    return (
        "retry official static docket page with rate limiting, then use official docket search or "
        "manual Supreme Court docket lookup before treating the row as closed-cohort coded"
    )


def build_rows() -> list[dict[str, str]]:
    journal_rows = {row["sourceRecordId"]: row for row in read_csv(JOURNAL_EXTRACT)}
    manifest = json.loads(JOURNAL_DOCKET_MANIFEST.read_text())
    rows: list[dict[str, str]] = []
    for index, failure in enumerate(manifest.get("failedFetches", []), start=1):
        source_id = failure["sourceRecordId"]
        journal = journal_rows.get(source_id)
        if journal is None:
            raise SystemExit(f"Failed-fetch sourceRecordId is absent from Journal extract: {source_id}")
        output = {
            "workQueueRank": str(index),
            "sourceRecordId": source_id,
            "docketNumber": failure["docketNumber"],
            "paidOrIfp": journal["paidOrIfp"],
            "certDisposition": journal["certDisposition"],
            "dispositionDate": journal["dispositionDate"],
            "lowerCourt": journal["lowerCourt"],
            "staticDocketUrl": failure["sourceUrl"],
            "failedFetchError": failure["error"],
            "retrievalPriority": priority(journal),
            "retrievalAction": retrieval_action(journal),
            "denominatorRole": "OT2023 Journal disposition row lacking reachable static docket detail",
            "completionEvidence": (
                "official docket detail row is fetched or manually coded with source URL, "
                "petition filing date, response/CFR/CVSG fields where visible, and coder notes"
            ),
            "manuscriptUse": MANUSCRIPT_USE,
        }
        if output["docketNumber"] != journal["docketNumber"]:
            raise SystemExit(f"Failed-fetch docket mismatch for {source_id}")
        rows.append(output)
    return rows


def write_markdown(path: Path, rows: list[dict[str, str]]) -> None:
    by_priority = Counter(row["retrievalPriority"] for row in rows)
    by_disposition = Counter(row["certDisposition"] for row in rows)
    by_paid_ifp = Counter(row["paidOrIfp"] for row in rows)
    lines = [
        "# Certiorari Journal Docket Retrieval Workqueue v1",
        "",
        "This workqueue expands the failed-fetch portion of the OT2023 Journal public-docket detail pass into row-level retrieval tasks. It is not validation evidence. It identifies official static docket pages that returned errors during the extraction run and must be retried, manually recovered from official docket search, or otherwise documented before any closed filed-petition cohort claim is upgraded.",
        "",
        f"- Rows needing retrieval: {len(rows)}",
        "- Source slice: failed official static docket fetches from `certiorari-journal-docket-detail-ot2023-manifest.json`",
        "- Boundary: Journal disposition rows only; not all petitions filed during OT2023",
        "",
        "Priority counts:",
        "",
    ]
    for key, value in sorted(by_priority.items()):
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "Disposition counts:", ""])
    for key, value in sorted(by_disposition.items()):
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "Paid/IFP counts:", ""])
    for key, value in sorted(by_paid_ifp.items()):
        lines.append(f"- `{key}`: {value}")
    lines.extend([
        "",
        "Representative first rows:",
        "",
        "| Rank | Docket | Disposition | Paid/IFP | Priority | Retrieval action |",
        "| ---: | --- | --- | --- | --- | --- |",
    ])
    for row in rows[:20]:
        lines.append(
            f"| {row['workQueueRank']} | `{row['docketNumber']}` | {row['certDisposition']} | "
            f"{row['paidOrIfp']} | {row['retrievalPriority']} | {row['retrievalAction']} |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    rows = build_rows()
    write_csv(OUTPUT_CSV, rows)
    write_markdown(OUTPUT_MD, rows)
    print(f"Wrote {OUTPUT_CSV.relative_to(ROOT)}")
    print(f"Wrote {OUTPUT_MD.relative_to(ROOT)}")
    print(f"Queued {len(rows)} failed official docket fetches")


if __name__ == "__main__":
    main()
