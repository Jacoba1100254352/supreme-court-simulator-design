#!/usr/bin/env python3
"""Extract a Journal term-flow statistics benchmark slice.

The official Journal PDF is intentionally not committed. This script accepts a
locally downloaded Journal PDF, parses the opening statistics pages, and
writes a compact, source-record-addressable extract under data/benchmarks/.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class TermConfig:
    term: str
    source_key: str
    source_name: str
    source_url: str
    statistics_as_of: str
    source_file: str
    statistics_coverage_note: str
    expected_counts: Mapping[str, int]

    @property
    def slug(self) -> str:
        return self.term.lower()

    @property
    def default_output(self) -> Path:
        return (
            ROOT
            / "data"
            / "benchmarks"
            / f"certiorari-term-flow-extract-journal-{self.slug}.csv"
        )

    @property
    def default_manifest(self) -> Path:
        return (
            ROOT
            / "data"
            / "benchmarks"
            / f"certiorari-term-flow-extract-journal-{self.slug}-manifest.json"
        )


TERM_CONFIGS = {
    "OT2023": TermConfig(
        term="OT2023",
        source_key="journal-ot2023",
        source_name="Journal of the Supreme Court OT2023",
        source_url="https://www.supremecourt.gov/orders/journal/jnl23.pdf",
        statistics_as_of="2024-07-02",
        source_file="jnl23.pdf",
        statistics_coverage_note=(
            "Statistics cover activity between the docketing of the first case "
            "with a 23- prefix on June 30, 2023 and July 2, 2024."
        ),
        expected_counts={
            "cases_docketed_paid": 1375,
            "cases_docketed_ifp": 2847,
            "cases_docketed_original": 1,
            "cases_docketed_total": 4223,
            "cases_disposed": 4175,
            "certiorari_granted_paid": 66,
            "certiorari_granted_ifp": 3,
            "total_cases_granted_plenary_review": 69,
        },
    ),
    "OT2024": TermConfig(
        term="OT2024",
        source_key="journal-ot2024",
        source_name="Journal of the Supreme Court OT2024",
        source_url="https://www.supremecourt.gov/orders/journal/Jnl24.pdf",
        statistics_as_of="2025-06-30",
        source_file="Jnl24.pdf",
        statistics_coverage_note=(
            "Statistics cover activity between the docketing of the first case "
            "with a 24- prefix on July 3, 2024 and June 30, 2025."
        ),
        expected_counts={
            "cases_docketed_paid": 1327,
            "cases_docketed_ifp": 2527,
            "cases_docketed_original": 2,
            "cases_docketed_total": 3856,
            "cases_remaining_from_last_term": 742,
            "total_cases_on_docket": 4598,
            "cases_disposed": 4024,
            "number_remaining_on_docket": 574,
            "certiorari_granted_paid": 64,
            "certiorari_granted_ifp": 4,
            "appeals_granted_paid": 2,
            "total_cases_granted_plenary_review": 70,
            "cases_argued_during_term": 73,
            "argued_full_opinions": 64,
            "argued_per_curiam_opinions": 7,
            "argued_set_for_reargument_next_term": 2,
            "cases_available_for_argument_start": 28,
            "disposed_summarily_after_review_granted": 0,
            "applications_set_for_argument": 3,
            "original_cases_set_for_argument": 0,
            "cases_reviewed_decided_without_oral_argument": 66,
            "cases_available_for_argument_next_term": 30,
        },
    ),
}

FIELDNAMES = [
    "sourceKey",
    "sourceName",
    "sourceUrl",
    "sourceFile",
    "sourceFileSha256",
    "sourceRecordId",
    "term",
    "statisticsAsOf",
    "statisticsCoverageNote",
    "statisticKey",
    "statisticSection",
    "statisticLabel",
    "caseCategory",
    "officialCount",
    "denominatorKey",
    "denominatorCount",
    "normalizedObservedValue",
    "benchmarkUse",
    "coderNotes",
]

STATISTICS = [
    {
        "key": "cases_docketed_paid",
        "section": "cases_docketed_during_term",
        "label": "Paid cases",
        "category": "paid",
        "pattern": r"Paid cases\s+\.{2,}\s+(\d+)",
        "use": "term-flow paid/IFP intake guardrail",
    },
    {
        "key": "cases_docketed_ifp",
        "section": "cases_docketed_during_term",
        "label": "In forma pauperis cases",
        "category": "ifp",
        "pattern": r"In forma pauperis cases\s+\.{2,}\s+(\d+)",
        "use": "term-flow paid/IFP intake guardrail",
    },
    {
        "key": "cases_docketed_original",
        "section": "cases_docketed_during_term",
        "label": "Original cases",
        "category": "original",
        "pattern": r"Original cases\s*\.{2,}\s+(\d+)",
        "use": "term-flow denominator context",
    },
    {
        "key": "cases_docketed_total",
        "section": "cases_docketed_during_term",
        "label": "Total cases docketed during term",
        "category": "total",
        "pattern": r"Total\s*\.{2,}\s+(\d+)",
        "use": "term-flow denominator context",
    },
    {
        "key": "cases_remaining_from_last_term",
        "section": "term_flow",
        "label": "Cases remaining from last term",
        "category": "total",
        "pattern": r"Cases remaining from last term\s+\.{2,}\s+(\d+)",
        "use": "term-flow denominator context",
    },
    {
        "key": "total_cases_on_docket",
        "section": "term_flow",
        "label": "Total cases on the docket",
        "category": "total",
        "pattern": r"Total cases on the docket\s*\.{2,}\s+(\d+)",
        "use": "term-flow denominator context",
    },
    {
        "key": "cases_disposed",
        "section": "term_flow",
        "label": "Cases disposed of",
        "category": "total",
        "pattern": r"Cases disposed of\s+\.{2,}\s+(\d+)",
        "occurrence": "last",
        "use": "term-flow denominator context",
    },
    {
        "key": "number_remaining_on_docket",
        "section": "term_flow",
        "label": "Number remaining on docket",
        "category": "total",
        "pattern": r"Number remaining on docket\s*\.{2,}\s+(\d+)",
        "use": "term-flow denominator context",
    },
    {
        "key": "certiorari_granted_paid",
        "section": "petitions_for_certiorari_granted",
        "label": "Paid cases",
        "category": "paid",
        "pattern": r"Petitions for certiorari granted:\s+Paid cases\s+\.{2,}\s+(\d+)",
        "use": "term-flow plenary-review context",
    },
    {
        "key": "certiorari_granted_ifp",
        "section": "petitions_for_certiorari_granted",
        "label": "In forma pauperis cases",
        "category": "ifp",
        "pattern": r"Petitions for certiorari granted:.*?In forma pauperis cases\s+\.{2,}\s+(\d+)",
        "use": "term-flow plenary-review context",
    },
    {
        "key": "appeals_granted_paid",
        "section": "appeals_granted",
        "label": "Paid cases",
        "category": "paid",
        "pattern": r"Appeals granted:\s+Paid cases\s+\.{2,}\s+(\d+)",
        "use": "term-flow plenary-review context",
    },
    {
        "key": "total_cases_granted_plenary_review",
        "section": "plenary_review",
        "label": "Total cases granted plenary review",
        "category": "total",
        "pattern": r"Total cases granted plenary review\s+\.{2,}\s+(\d+)",
        "use": "term-flow plenary-review context",
    },
    {
        "key": "cases_argued_during_term",
        "section": "plenary_review",
        "label": "Cases argued during term",
        "category": "total",
        "pattern": r"Cases argued during term\s+\.{2,}\s+(\d+)",
        "use": "term-flow argument context",
    },
    {
        "key": "argued_full_opinions",
        "section": "plenary_review",
        "label": "Number disposed of by full opinions",
        "category": "total",
        "pattern": r"Number disposed of by full opinions\s*\.{2,}\s+(\d+)",
        "use": "term-flow argument context",
    },
    {
        "key": "argued_per_curiam_opinions",
        "section": "plenary_review",
        "label": "Number disposed of by per curiam opinions",
        "category": "total",
        "pattern": r"Number disposed of by per curiam opinions\s*\.{2,}\s+(\d+)",
        "use": "term-flow argument context",
    },
    {
        "key": "argued_set_for_reargument_next_term",
        "section": "plenary_review",
        "label": "Number set for reargument for next term",
        "category": "total",
        "pattern": r"Number set for reargument for next term\s*\.{2,}\s+(\d+)",
        "use": "term-flow argument context",
    },
    {
        "key": "cases_available_for_argument_start",
        "section": "plenary_review",
        "label": "Cases available for argument at beginning of term",
        "category": "total",
        "pattern": r"Cases available for argument at beginning of term\s+\.{2,}\s+(\d+)",
        "use": "term-flow argument context",
    },
    {
        "key": "disposed_summarily_after_review_granted",
        "section": "plenary_review",
        "label": "Disposed of summarily after review was granted",
        "category": "total",
        "pattern": r"Disposed of summarily after review was granted\s+\.{2,}\s+(\d+)",
        "use": "term-flow argument context",
    },
    {
        "key": "applications_set_for_argument",
        "section": "plenary_review",
        "label": "Applications set for argument",
        "category": "applications",
        "pattern": r"Applications set for argument\s+\.{2,}\s+(\d+)",
        "use": "term-flow argument context",
    },
    {
        "key": "original_cases_set_for_argument",
        "section": "plenary_review",
        "label": "Original cases set for argument",
        "category": "original",
        "pattern": r"Original cases set for argument\s+\.{2,}\s+(\d+)",
        "use": "term-flow argument context",
    },
    {
        "key": "cases_reviewed_decided_without_oral_argument",
        "section": "plenary_review",
        "label": "Cases reviewed and decided without oral argument",
        "category": "total",
        "pattern": r"Cases reviewed and decided without oral argument\s*\.{2,}\s+(\d+)",
        "use": "term-flow no-argument context",
    },
    {
        "key": "cases_available_for_argument_next_term",
        "section": "plenary_review",
        "label": "Total cases available for argument at start of next term",
        "category": "total",
        "pattern": r"Total cases available for argument at start of next term\s+\.{2,}\s+(\d+)",
        "use": "term-flow argument context",
    },
]

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdf_text(path: Path) -> str:
    if path.suffix.lower() == ".txt":
        return path.read_text()
    try:
        result = subprocess.run(
            ["pdftotext", "-layout", "-f", "1", "-l", "2", str(path), "-"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
    except FileNotFoundError as exc:
        raise SystemExit("pdftotext is required to parse the Journal PDF.") from exc
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"pdftotext failed: {exc.stderr}") from exc
    return result.stdout


def collapsed_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def parse_counts(text: str, config: TermConfig) -> dict[str, int]:
    collapsed = collapsed_text(text)
    counts: dict[str, int] = {}
    for spec in STATISTICS:
        matches = re.findall(spec["pattern"], collapsed)
        if not matches:
            raise SystemExit(f"Could not parse Journal statistic: {spec['key']}")
        value = matches[-1] if spec.get("occurrence") == "last" else matches[0]
        counts[spec["key"]] = int(value.replace(",", ""))
    for key, expected in config.expected_counts.items():
        actual = counts.get(key)
        if actual != expected:
            raise SystemExit(f"Parsed {key}={actual}, expected {expected}")
    return counts


def denominator_for(key: str, counts: dict[str, int]) -> tuple[str, str]:
    paid_ifp_total = counts["cases_docketed_paid"] + counts["cases_docketed_ifp"]
    total_docketed = counts["cases_docketed_total"]
    plenary_review_total = counts["total_cases_granted_plenary_review"]
    if key in {"cases_docketed_paid", "cases_docketed_ifp"}:
        return "paid_plus_ifp_cases_docketed_during_term", str(paid_ifp_total)
    if key in {"cases_docketed_original", "total_cases_granted_plenary_review"}:
        return "total_cases_docketed_during_term", str(total_docketed)
    if key in {"certiorari_granted_paid", "certiorari_granted_ifp", "appeals_granted_paid"}:
        return "total_cases_granted_plenary_review", str(plenary_review_total)
    if key == "cases_argued_during_term":
        return "total_cases_granted_plenary_review", str(plenary_review_total)
    return "", ""


def normalized_value(count: int, denominator: str) -> str:
    if not denominator:
        return ""
    denominator_int = int(denominator)
    if denominator_int == 0:
        return ""
    return f"{count / denominator_int:.6f}"


def build_rows(
    path: Path,
    counts: dict[str, int],
    config: TermConfig,
) -> list[dict[str, str]]:
    source_file = (
        path.name if path.suffix.lower() != ".txt" else config.source_file
    )
    source_hash = sha256(path)
    rows: list[dict[str, str]] = []
    for spec in STATISTICS:
        count = counts[spec["key"]]
        denominator_key, denominator_count = denominator_for(spec["key"], counts)
        rows.append({
            "sourceKey": config.source_key,
            "sourceName": config.source_name,
            "sourceUrl": config.source_url,
            "sourceFile": source_file,
            "sourceFileSha256": source_hash,
            "sourceRecordId": (
                f"{config.source_file}:statistics page II:{spec['key']}"
            ),
            "term": config.term,
            "statisticsAsOf": config.statistics_as_of,
            "statisticsCoverageNote": config.statistics_coverage_note,
            "statisticKey": spec["key"],
            "statisticSection": spec["section"],
            "statisticLabel": spec["label"],
            "caseCategory": spec["category"],
            "officialCount": str(count),
            "denominatorKey": denominator_key,
            "denominatorCount": denominator_count,
            "normalizedObservedValue": normalized_value(count, denominator_count),
            "benchmarkUse": spec["use"],
            "coderNotes": (
                "Official Journal term-flow statistic; useful as source-quality "
                "and intake-denominator evidence, not as a closed petition-cohort row."
            ),
        })
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def safe_relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def write_manifest(
    path: Path,
    source: Path,
    rows: list[dict[str, str]],
    output: Path,
    config: TermConfig,
) -> None:
    counts = {row["statisticKey"]: int(row["officialCount"]) for row in rows}
    payload = {
        "sourceKey": config.source_key,
        "sourceName": config.source_name,
        "sourceUrl": config.source_url,
        "sourceFile": source.name,
        "sourceFileSha256": sha256(source),
        "term": config.term,
        "statisticsAsOf": config.statistics_as_of,
        "output": safe_relative(output),
        "rowCount": len(rows),
        "officialCounts": counts,
        "notes": [
            "Raw Journal PDF is not committed.",
            "Extract is an official term-flow statistics slice, not a closed petition-cohort dataset.",
            config.statistics_coverage_note,
        ],
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "source",
        type=Path,
        help="Path to Journal PDF, or opening-pages pdftotext output",
    )
    parser.add_argument(
        "--term",
        choices=sorted(TERM_CONFIGS),
        default="OT2023",
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument("--manifest", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = TERM_CONFIGS[args.term]
    output = args.output or config.default_output
    manifest = args.manifest or config.default_manifest
    text = pdf_text(args.source)
    rows = build_rows(args.source, parse_counts(text, config), config)
    write_csv(output, rows)
    write_manifest(manifest, args.source, rows, output, config)
    print(f"Wrote {safe_relative(output)} ({len(rows)} rows)")
    print(f"Wrote {safe_relative(manifest)}")


if __name__ == "__main__":
    main()
