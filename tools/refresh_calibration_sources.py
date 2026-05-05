#!/usr/bin/env python3
"""Refresh normalized calibration inputs from local raw-source downloads."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
MANIFEST = DIST / "calibration-source-refresh-manifest.json"

NORMALIZED_HEADER = [
    "sourceKey",
    "domain",
    "metric",
    "term",
    "numerator",
    "denominator",
    "value",
    "sourceUrl",
    "notes",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def candidate(raw_dir: Path, explicit: Path | None, patterns: list[str]) -> Path | None:
    if explicit:
        return explicit
    for pattern in patterns:
        matches = sorted(raw_dir.glob(pattern))
        if matches:
            return matches[0]
    return None


def run(command: list[str]) -> None:
    print("Running " + " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def validate_normalized_csv(path: Path) -> int:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        header = reader.fieldnames or []
        missing = [column for column in NORMALIZED_HEADER if column not in header]
        if missing:
            raise SystemExit(f"{path} is missing normalized columns: {', '.join(missing)}")
        return sum(1 for _ in reader)


def copy_hlr_manual_csv(source: Path, output_dir: Path) -> Path:
    validate_normalized_csv(source)
    destination = output_dir / "harvard-law-review-statistics-summary.csv"
    shutil.copy2(source, destination)
    return destination


def relative_or_name(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.name


def file_entry(path: Path, role: str) -> dict[str, object]:
    return {
        "role": role,
        "name": path.name,
        "path": relative_or_name(path),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def existing_outputs(output_dir: Path) -> list[Path]:
    if not output_dir.exists():
        return []
    return sorted(path for path in output_dir.rglob("*.csv") if path.is_file())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", type=Path, default=Path("data/raw/calibration"))
    parser.add_argument("--output-dir", type=Path, default=Path("data/calibration"))
    parser.add_argument("--scdb-case-zip", type=Path)
    parser.add_argument("--shadow-zip", type=Path)
    parser.add_argument("--deep-research-report", type=Path)
    parser.add_argument("--hlr-manual-csv", type=Path)
    parser.add_argument("--skip-deep-research", action="store_true")
    args = parser.parse_args()

    raw_dir = args.raw_dir
    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    DIST.mkdir(parents=True, exist_ok=True)

    scdb_zip = candidate(raw_dir, args.scdb_case_zip, ["*SCDB*case*.zip", "*caseCentered*.zip"])
    if scdb_zip is None:
        raise SystemExit(
            "No SCDB case-centered zip found. Put it under data/raw/calibration or pass --scdb-case-zip."
        )
    shadow_zip = candidate(raw_dir, args.shadow_zip, ["*shadow*docket*.zip", "*shadow*.zip"])
    deep_report = candidate(raw_dir, args.deep_research_report, ["deep-research-report5.md", "*synthesis*.md"])
    hlr_manual = candidate(raw_dir, args.hlr_manual_csv, ["harvard-law-review-statistics-summary.csv", "*hlr*.csv"])

    inputs = [file_entry(scdb_zip, "scdb_case_zip")]
    command = [
        "python3",
        "tools/build_calibration_tables.py",
        "--scdb-case-zip",
        str(scdb_zip),
        "--output-dir",
        str(output_dir),
    ]
    if shadow_zip:
        inputs.append(file_entry(shadow_zip, "shadow_docket_zip"))
        command.extend(["--shadow-zip", str(shadow_zip)])
    run(command)

    if deep_report and not args.skip_deep_research:
        inputs.append(file_entry(deep_report, "deep_research_synthesis_report"))
        run(
            [
                "python3",
                "tools/import_deep_research_synthesis.py",
                "--report",
                str(deep_report),
                "--output-dir",
                str(output_dir / "supreme-court-synthesis"),
            ]
        )
    elif not args.skip_deep_research:
        print("No Deep Research synthesis report found; skipping synthesis CSV import.")

    copied_hlr = None
    if hlr_manual:
        inputs.append(file_entry(hlr_manual, "harvard_law_review_manual_summary"))
        copied_hlr = copy_hlr_manual_csv(hlr_manual, output_dir)
    else:
        print("No Harvard Law Review manual summary CSV found; keeping coded HLR source ranges unchanged.")

    outputs = [file_entry(path, "normalized_output") for path in existing_outputs(output_dir)]
    notes = [
        "Raw-source archives are intentionally not committed.",
        "The SCDB and shadow-docket rows are generated from raw archives by tools/build_calibration_tables.py.",
        "Deep Research synthesis rows preserve validationUse, denominatorSpec, coverageScope, and comparabilityClass metadata.",
        "Harvard Law Review statistics are copied only when a manually prepared normalized CSV is supplied.",
    ]
    if copied_hlr:
        notes.append(f"Copied HLR manual summary to {relative_or_name(copied_hlr)}.")
    manifest: dict[str, object] = {
        "createdAt": datetime.now(timezone.utc).isoformat(),
        "rawDirectory": relative_or_name(raw_dir),
        "outputDirectory": relative_or_name(output_dir),
        "inputs": inputs,
        "outputs": outputs,
        "notes": notes,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(f"Wrote {relative_or_name(MANIFEST)}")


if __name__ == "__main__":
    main()
