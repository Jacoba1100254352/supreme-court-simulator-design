#!/usr/bin/env python3
"""Fail when the committed manuscript PDF is older than its LaTeX inputs."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PDF = ROOT / "paper" / "main.pdf"
INPUT_PATTERNS = [
    "paper/main.tex",
    "paper/references.bib",
    "paper/figures/*.tex",
    "paper/tables/*.tex",
]


def fail(message: str) -> None:
    print(f"PDF freshness check failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def input_files() -> list[Path]:
    files: list[Path] = []
    for pattern in INPUT_PATTERNS:
        matches = sorted(ROOT.glob(pattern))
        if not matches:
            fail(f"input pattern {pattern} matched no files")
        files.extend(path for path in matches if path.is_file())
    return files


def main() -> None:
    if not PDF.exists():
        fail("paper/main.pdf is missing; run `make paper`")

    pdf_mtime = PDF.stat().st_mtime
    stale_inputs = [path for path in input_files() if path.stat().st_mtime > pdf_mtime]
    if stale_inputs:
        display = ", ".join(str(path.relative_to(ROOT)) for path in stale_inputs[:8])
        if len(stale_inputs) > 8:
            display += f", and {len(stale_inputs) - 8} more"
        fail(f"paper/main.pdf is older than {display}; run `make paper`")

    print(f"PDF freshness check passed ({PDF.relative_to(ROOT)} is current).")


if __name__ == "__main__":
    main()
