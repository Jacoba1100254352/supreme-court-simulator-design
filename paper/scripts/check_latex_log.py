#!/usr/bin/env python3
"""Fail on LaTeX log issues that make the review PDF unreliable."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LOG = ROOT / "paper" / "build" / "main.log"

FAIL_PATTERNS = [
    r"undefined citations",
    r"undefined references",
    r"Citation\(s\) may have changed",
    r"Reference `[^']+' .* undefined",
    r"Citation `[^']+' .* undefined",
    r"Overfull \\hbox",
    r"Overfull \\vbox",
]


def main() -> None:
    if not LOG.exists():
        print(f"LaTeX log check failed: missing {LOG}", file=sys.stderr)
        raise SystemExit(1)
    text = LOG.read_text(errors="replace")
    failures = []
    for pattern in FAIL_PATTERNS:
        if re.search(pattern, text):
            failures.append(pattern)
    if failures:
        print("LaTeX log check failed:", file=sys.stderr)
        for pattern in failures:
            print(f"- matched {pattern}", file=sys.stderr)
        raise SystemExit(1)
    underfull_count = len(re.findall(r"Underfull \\hbox", text))
    if underfull_count:
        print(f"LaTeX log check passed with {underfull_count} underfull hbox warning(s).")
    else:
        print("LaTeX log check passed.")


if __name__ == "__main__":
    main()
