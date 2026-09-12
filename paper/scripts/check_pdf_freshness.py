#!/usr/bin/env python3
"""Fail when the committed manuscript PDF is older than its LaTeX inputs."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PDF = ROOT / "paper" / "emergency-review-constitutional-court-design.pdf"
INPUT_PATTERNS = [
    "paper/emergency-review-constitutional-court-design.tex",
    "paper/references.bib",
    "paper/figures/*.tex",
    "paper/tables/*.tex",
]


def fail(message: str) -> None:
    print(f"PDF freshness check failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def input_files(patterns: list[str]) -> list[Path]:
    files: list[Path] = []
    for pattern in patterns:
        matches = sorted(ROOT.glob(pattern))
        if not matches:
            fail(f"input pattern {pattern} matched no files")
        files.extend(path for path in matches if path.is_file())
    return files


def check_document(pdf: Path, patterns: list[str]) -> None:
    if not pdf.exists():
        fail(f"{pdf.relative_to(ROOT)} is missing; run `make paper`")

    pdf_mtime = pdf.stat().st_mtime
    stale_inputs = [path for path in input_files(patterns) if path.stat().st_mtime > pdf_mtime]
    if stale_inputs:
        display = ", ".join(str(path.relative_to(ROOT)) for path in stale_inputs[:8])
        if len(stale_inputs) > 8:
            display += f", and {len(stale_inputs) - 8} more"
        fail(f"{pdf.relative_to(ROOT)} is older than {display}; run `make paper`")

    print(f"PDF freshness check passed ({pdf.relative_to(ROOT)} is current).")


def main() -> None:
    check_document(PDF, INPUT_PATTERNS)
    check_document(ROOT / "paper/technical-supplement.pdf", [
        "paper/technical-supplement.tex",
        "paper/tables/normative_scores.tex",
        "paper/tables/pipeline_diagnostics.tex",
        "paper/tables/mechanical_emergent.tex",
        "paper/tables/model_weights.tex",
    ])


if __name__ == "__main__":
    main()
