#!/usr/bin/env python3
"""Import ingest-ready Deep Research CSV blocks as calibration inputs.

The Deep Research reports preserve useful comparative rows, but they should not
be treated as one flat validation target. This importer extracts each fenced CSV
block, keeps it as a separate normalized file, and appends comparability metadata
used by the Java calibration loader and paper appendix.
"""

from __future__ import annotations

import argparse
import csv
import re
from io import StringIO
from pathlib import Path


DEFAULT_REPORT = Path(
    "/Users/jacobanderson/Downloads/Deep Research Reports/Supreme Court/deep-research-report5.md"
)
DEFAULT_OUTPUT_DIR = Path("data/calibration/supreme-court-synthesis")

EXTRA_COLUMNS = [
    "denominatorSpec",
    "coverageScope",
    "comparabilityClass",
    "rawSection",
]

SECTION_FILENAMES = {
    "Comparative court design presets": "comparative-court-design-presets.csv",
    "Lower-court and intake calibration": "lower-court-intake-calibration.csv",
    "Emergency docket calibration": "emergency-docket-calibration.csv",
    "Cross-national calibration targets": "cross-national-calibration-targets.csv",
    "Institutional budget, delay, and complexity benchmarks": "institutional-cost-delay-complexity-benchmarks.csv",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    sections = extract_csv_sections(args.report.read_text())
    written: list[tuple[str, Path, list[dict[str, str]]]] = []
    for section_name, csv_text in sections:
        filename = SECTION_FILENAMES.get(section_name)
        if filename is None:
            continue
        path = args.output_dir / filename
        rows = normalize_rows(section_name, csv_text)
        with path.open("w", newline="") as output:
            writer = csv.DictWriter(output, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        written.append((section_name, path, rows))

    write_source_register(args.output_dir, written)
    write_readme(args.output_dir, args.report, written)
    for section_name, path, rows in written:
        print(f"Imported {len(rows)} rows from {section_name} -> {path}")


def extract_csv_sections(markdown: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    pattern = re.compile(r"\*\*(?P<section>[^*]+)\*\*\s*\n\n```csv\n(?P<csv>.*?)\n```", re.DOTALL)
    for match in pattern.finditer(markdown):
        sections.append((match.group("section").strip(), match.group("csv").strip()))
    return sections


def normalize_rows(section_name: str, csv_text: str) -> list[dict[str, str]]:
    reader = csv.DictReader(StringIO(csv_text))
    rows: list[dict[str, str]] = []
    for raw in reader:
        row = {key: value for key, value in raw.items() if key is not None}
        row.update(metadata(section_name, row))
        rows.append(row)
    if not rows:
        raise ValueError(f"No rows found for {section_name}")
    return rows


def metadata(section_name: str, row: dict[str, str]) -> dict[str, str]:
    metric_key = row.get("metricKey", "")
    jurisdiction = row.get("jurisdiction", "")
    validation_use = row.get("validationUse", "")
    if section_name == "Comparative court design presets":
        denominator = "institutional design row, not a behavioral denominator"
        coverage = "stable court structure preset"
        comparability = "design_context"
    elif metric_key.endswith("_rate") or metric_key.endswith("_share"):
        denominator = "rate/share denominator defined by sourceName and sourceUrl"
        coverage = f"{jurisdiction} {row.get('timePeriod', '')}".strip()
        comparability = "behavioral_rate"
    elif "available" in metric_key or "absent" in metric_key or "common" in metric_key:
        denominator = "binary institutional/procedural indicator"
        coverage = f"{jurisdiction} {row.get('timePeriod', '')}".strip()
        comparability = "binary_procedure_indicator"
    elif validation_use == "paper_only_context":
        denominator = "context row, not a simulator validation denominator"
        coverage = f"{jurisdiction} {row.get('timePeriod', '')}".strip()
        comparability = "paper_context"
    else:
        denominator = "count, duration, or ratio denominator defined by sourceName and sourceUrl"
        coverage = f"{jurisdiction} {row.get('timePeriod', '')}".strip()
        comparability = "benchmark_or_constraint"

    return {
        "denominatorSpec": denominator,
        "coverageScope": coverage,
        "comparabilityClass": comparability,
        "rawSection": section_name,
    }


def write_source_register(output_dir: Path, written: list[tuple[str, Path, list[dict[str, str]]]]) -> None:
    register: dict[tuple[str, str], dict[str, object]] = {}
    for section_name, path, rows in written:
        for row in rows:
            source_name = row.get("sourceName", "").strip()
            source_url = row.get("sourceUrl", "").strip()
            if not source_name and not source_url:
                continue
            key = (source_name, source_url)
            entry = register.setdefault(key, {
                "sourceName": source_name,
                "sourceUrl": source_url,
                "files": set(),
                "sections": set(),
                "rowCount": 0,
                "validationUses": set(),
                "confidenceLevels": set(),
                "comparabilityClasses": set(),
            })
            entry["files"].add(path.name)
            entry["sections"].add(section_name)
            entry["rowCount"] = int(entry["rowCount"]) + 1
            if row.get("validationUse"):
                entry["validationUses"].add(row["validationUse"])
            if row.get("confidenceLevel"):
                entry["confidenceLevels"].add(row["confidenceLevel"])
            if row.get("comparabilityClass"):
                entry["comparabilityClasses"].add(row["comparabilityClass"])

    path = output_dir / "source-register.csv"
    fields = [
        "sourceName",
        "sourceUrl",
        "files",
        "sections",
        "rowCount",
        "validationUses",
        "confidenceLevels",
        "comparabilityClasses",
    ]
    with path.open("w", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        for (_source_name, _source_url), entry in sorted(register.items()):
            writer.writerow({
                "sourceName": entry["sourceName"],
                "sourceUrl": entry["sourceUrl"],
                "files": ";".join(sorted(entry["files"])),
                "sections": ";".join(sorted(entry["sections"])),
                "rowCount": entry["rowCount"],
                "validationUses": ";".join(sorted(entry["validationUses"])),
                "confidenceLevels": ";".join(sorted(entry["confidenceLevels"])),
                "comparabilityClasses": ";".join(sorted(entry["comparabilityClasses"])),
            })


def write_readme(output_dir: Path, report: Path, written: list[tuple[str, Path, list[dict[str, str]]]]) -> None:
    lines = [
        "# Supreme Court Deep Research Synthesis",
        "",
        f"Imported from local Deep Research synthesis report `{report.name}`. The raw report is not committed.",
        "",
        "These CSVs preserve the ingest-ready research rows as calibration inputs.",
        "Rows include `confidenceLevel`, `validationUse`, `denominatorSpec`, `coverageScope`, and `comparabilityClass` so strict validation, loose calibration, and paper-only context are not conflated.",
        "The synthesis itself is not cited as empirical authority in the manuscript; `source-register.csv` preserves the named sources and URLs represented in the normalized rows.",
        "",
        "| Section | File | Rows |",
        "| --- | --- | ---: |",
    ]
    for section_name, path, rows in written:
        lines.append(f"| {section_name} | `{path.name}` | {len(rows)} |")
    lines.extend([
        "",
        "See `source-register.csv` for a normalized source register grouped by source name and URL.",
        "",
        "The Java loader reads numeric `observedValue` rows from these files recursively when `data/calibration` is used as the calibration directory.",
        "Non-numeric design-preset rows remain available for documentation and scenario-design work, but are not treated as numerical validation observations.",
        "",
    ])
    output_dir.joinpath("README.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
