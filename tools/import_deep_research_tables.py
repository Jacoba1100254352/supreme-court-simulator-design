#!/usr/bin/env python3
"""Import Deep Research markdown pipe tables as normalized calibration rows.

The newer Supreme Court simulator research reports use markdown tables instead
of fenced CSV blocks. This script extracts tables whose first column is
`variableName`, preserves each row's source metadata, and writes a synthesis
schema that the Java calibration loader already understands.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


DEFAULT_OUTPUT_DIR = Path("data/calibration/supreme-court-research-2026")

OUTPUT_FIELDS = [
    "metricKey",
    "jurisdiction",
    "timePeriod",
    "lowerBound",
    "upperBound",
    "observedValue",
    "rawObservedValue",
    "numeratorSpec",
    "denominatorSpec",
    "confidenceLevel",
    "validationUse",
    "coverageScope",
    "comparabilityClass",
    "sourceName",
    "sourceUrl",
    "rawSection",
    "reportName",
    "notes",
]


@dataclass(frozen=True)
class ImportedReport:
    report: Path
    output_file: Path
    section_counts: dict[str, int]
    rows: list[dict[str, str]]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reports", nargs="+", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    imported: list[ImportedReport] = []
    for report in args.reports:
        rows, section_counts = import_report(report)
        output_file = args.output_dir / (slug(report.stem) + ".csv")
        write_rows(output_file, rows)
        imported.append(ImportedReport(report, output_file, section_counts, rows))
        print(f"Imported {len(rows)} rows -> {output_file}")

    write_source_register(args.output_dir, imported)
    write_readme(args.output_dir, imported)


def import_report(path: Path) -> tuple[list[dict[str, str]], dict[str, int]]:
    lines = path.read_text().splitlines()
    rows: list[dict[str, str]] = []
    section_counts: dict[str, int] = defaultdict(int)
    section = path.stem
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("### "):
            section = clean_inline(line[4:].strip())
        if is_table_header(line):
            table_lines = [line]
            index += 1
            while index < len(lines) and lines[index].strip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            for row in parse_table(table_lines):
                normalized = normalize_row(row, path.stem, section)
                rows.append(normalized)
                section_counts[section] += 1
            continue
        index += 1
    if not rows:
        raise ValueError(f"No ingest-ready variableName tables found in {path}")
    return rows, dict(section_counts)


def is_table_header(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("|") and "variableName" in stripped and "observedValueOrRange" in stripped


def parse_table(lines: list[str]) -> list[dict[str, str]]:
    headers = [clean_inline(cell) for cell in split_row(lines[0])]
    data_lines = lines[2:] if len(lines) > 1 and re.fullmatch(r"\s*\|?[\s:\-|\u2013]+\|?\s*", lines[1]) else lines[1:]
    rows: list[dict[str, str]] = []
    for line in data_lines:
        cells = split_row(line)
        if len(cells) < len(headers):
            cells.extend([""] * (len(headers) - len(cells)))
        values = [clean_inline(cell) for cell in cells[:len(headers)]]
        row = dict(zip(headers, values))
        if row.get("variableName"):
            rows.append(row)
    return rows


def split_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def normalize_row(row: dict[str, str], report_name: str, section: str) -> dict[str, str]:
    raw_value = row.get("observedValueOrRange", "")
    lower, upper, observed = parse_numeric_range(raw_value)
    validation_use = normalize_validation(row.get("validationUse", ""))
    return {
        "metricKey": row.get("variableName", ""),
        "jurisdiction": row.get("jurisdiction", ""),
        "timePeriod": row.get("period", ""),
        "lowerBound": format_optional(lower),
        "upperBound": format_optional(upper),
        "observedValue": format_optional(observed),
        "rawObservedValue": raw_value,
        "numeratorSpec": row.get("numeratorSpec", ""),
        "denominatorSpec": row.get("denominatorSpec", ""),
        "confidenceLevel": row.get("confidenceLevel", ""),
        "validationUse": validation_use,
        "coverageScope": row.get("coverageScope", ""),
        "comparabilityClass": row.get("comparabilityClass", ""),
        "sourceName": row.get("sourceName", ""),
        "sourceUrl": extract_url(row.get("sourceUrl", "")),
        "rawSection": section,
        "reportName": report_name,
        "notes": row.get("notes", ""),
    }


def parse_numeric_range(value: str) -> tuple[float | None, float | None, float | None]:
    if not value:
        return None, None, None
    text = value.replace("\u2013", "-").replace("\u2014", "-").replace("\u2212", "-")
    text = re.sub(r"(?<=\d)\s*-\s*(?=\d)", " to ", text)
    text = re.sub(r"(?<=%)\s*-\s*(?=\d)", " to ", text)
    percent_matches = [float(match.group(1).replace(",", "")) / 100.0 for match in re.finditer(r"([+-]?\d+(?:,\d{3})*(?:\.\d+)?)\s*%", text)]
    if percent_matches:
        return min(percent_matches), max(percent_matches), percent_matches[0]

    percentage_point_matches = [
        float(match.group(1).replace(",", "")) / 100.0
        for match in re.finditer(r"([+-]?\d+(?:,\d{3})*(?:\.\d+)?)\s*(?:to|-)\s*([+-]?\d+(?:,\d{3})*(?:\.\d+)?)\s+percentage points", text)
    ]
    if percentage_point_matches:
        first = percentage_point_matches[0]
        second_match = re.search(r"[+-]?\d+(?:,\d{3})*(?:\.\d+)?\s*(?:to|-)\s*([+-]?\d+(?:,\d{3})*(?:\.\d+)?)\s+percentage points", text)
        second = float(second_match.group(1).replace(",", "")) / 100.0 if second_match else first
        return min(first, second), max(first, second), (first + second) / 2.0

    numbers = [float(token.replace(",", "")) for token in re.findall(r"[+-]?\d+(?:,\d{3})*(?:\.\d+)?", text)]
    if not numbers:
        return None, None, None
    if "percentage point" in text.lower():
        numbers = [number / 100.0 for number in numbers]
    if len(numbers) == 1:
        return numbers[0], numbers[0], numbers[0]
    low = min(numbers[:2])
    high = max(numbers[:2])
    return low, high, numbers[0]


def normalize_validation(value: str) -> str:
    lowered = value.strip().lower()
    return (
        lowered.replace(" ", "_")
        .replace("/", "_")
        .replace("-", "_")
    )


def clean_inline(value: str) -> str:
    value = re.sub(r"cite[^]+", "", value)
    value = re.sub(r"entity\[[^\]]+\]", lambda match: entity_label(match.group(0)), value)
    value = re.sub(r"url([^]+)([^]+)", r"\1 (\2)", value)
    value = value.replace("**", "")
    return re.sub(r"\s+", " ", value).strip()


def entity_label(token: str) -> str:
    match = re.search(r'"([^"]+)"', token)
    return match.group(1) if match else ""


def extract_url(value: str) -> str:
    match = re.search(r"\((https?://[^)]+)\)", value)
    if match:
        return match.group(1)
    match = re.search(r"https?://\S+", value)
    if match:
        return match.group(0)
    if "turn" in value:
        return value
    return value


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def write_source_register(output_dir: Path, imported: list[ImportedReport]) -> None:
    register: dict[tuple[str, str], dict[str, object]] = {}
    for report in imported:
        for row in report.rows:
            source_name = row["sourceName"].strip()
            source_url = row["sourceUrl"].strip()
            if not source_name and not source_url:
                continue
            key = (source_name, source_url)
            entry = register.setdefault(key, {
                "sourceName": source_name,
                "sourceUrl": source_url,
                "files": set(),
                "reports": set(),
                "sections": set(),
                "rowCount": 0,
                "validationUses": set(),
                "confidenceLevels": set(),
                "comparabilityClasses": set(),
            })
            entry["files"].add(report.output_file.name)
            entry["reports"].add(report.report.name)
            entry["sections"].add(row["rawSection"])
            entry["rowCount"] = int(entry["rowCount"]) + 1
            if row["validationUse"]:
                entry["validationUses"].add(row["validationUse"])
            if row["confidenceLevel"]:
                entry["confidenceLevels"].add(row["confidenceLevel"])
            if row["comparabilityClass"]:
                entry["comparabilityClasses"].add(row["comparabilityClass"])

    fields = [
        "sourceName",
        "sourceUrl",
        "files",
        "reports",
        "sections",
        "rowCount",
        "validationUses",
        "confidenceLevels",
        "comparabilityClasses",
    ]
    with (output_dir / "source-register.csv").open("w", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        for (_source_name, _source_url), entry in sorted(register.items()):
            writer.writerow({
                "sourceName": entry["sourceName"],
                "sourceUrl": entry["sourceUrl"],
                "files": ";".join(sorted(entry["files"])),
                "reports": ";".join(sorted(entry["reports"])),
                "sections": ";".join(sorted(entry["sections"])),
                "rowCount": entry["rowCount"],
                "validationUses": ";".join(sorted(entry["validationUses"])),
                "confidenceLevels": ";".join(sorted(entry["confidenceLevels"])),
                "comparabilityClasses": ";".join(sorted(entry["comparabilityClasses"])),
            })


def write_readme(output_dir: Path, imported: list[ImportedReport]) -> None:
    lines = [
        "# Supreme Court Simulator Research Tables",
        "",
        "Normalized rows imported from local Deep Research markdown reports. The raw reports are not committed; this directory preserves only table rows and source-register metadata for calibration and paper transparency.",
        "",
        "Rows use the same synthesis schema as the earlier `supreme-court-synthesis/` import: `metricKey`, `observedValue`, `confidenceLevel`, `validationUse`, `denominatorSpec`, `coverageScope`, and `comparabilityClass` are retained so strict validation, loose calibration, proxy context, and design-prior rows remain separate.",
        "",
        "| Report | File | Rows | Sections |",
        "| --- | --- | ---: | --- |",
    ]
    for report in imported:
        section_summary = "; ".join(f"{name}: {count}" for name, count in sorted(report.section_counts.items()))
        lines.append(f"| {report.report.name} | `{report.output_file.name}` | {len(report.rows)} | {section_summary} |")
    lines.extend([
        "",
        "`source-register.csv` groups rows by named source and URL. The Java loader reads numeric `observedValue` rows recursively, but paper interpretation must still respect each row's `validationUse` and denominator notes.",
        "",
        "Regenerate with:",
        "",
        "```sh",
        "python3 tools/import_deep_research_tables.py --reports \\",
        "  \"/path/to/Supreme Court Simulator - Calibration Targets.md\" \\",
        "  \"/path/to/Supreme Court Simulator - Institutional Design and Empirical Anchors.md\" \\",
        "  \"/path/to/Supreme Court Simulator - Institutional Design Evidence.md\" \\",
        "  \"/path/to/Supreme Court Simulator - Litigation Pipeline Incentives.md\"",
        "```",
        "",
    ])
    (output_dir / "README.md").write_text("\n".join(lines))


def format_optional(value: float | None) -> str:
    return "" if value is None else f"{value:.6g}"


def slug(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


if __name__ == "__main__":
    main()
