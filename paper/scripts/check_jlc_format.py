#!/usr/bin/env python3
"""Lightweight Journal of Law and Courts manuscript checks."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MAIN = ROOT / "paper" / "main.tex"
TITLE_PAGE = ROOT / "paper" / "title-page.tex"
MAX_WORDS = 10_000


def fail(message: str) -> None:
    print(f"JLC format check failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def strip_latex(source: str) -> str:
    source = re.sub(r"%.*", " ", source)
    source = re.sub(r"\\begin\{[^}]+\}|\\end\{[^}]+\}", " ", source)
    source = re.sub(r"\\[a-zA-Z*]+(?:\[[^\]]*\])?(?:\{[^{}]*\})?", " ", source)
    source = re.sub(r"[{}$^_&~]", " ", source)
    return source


def word_count(source: str) -> int:
    return len(re.findall(r"[A-Za-z][A-Za-z0-9'-]*", strip_latex(source)))


def main() -> None:
    source = MAIN.read_text()
    title_page = TITLE_PAGE.read_text()

    required_snippets = [
        ("official JLC class option", "journal=jlc"),
        ("research article template option", "manuscript=research-article"),
        ("anonymous review mode", "\\anonymoustrue"),
        ("data availability statement", "Data Availability Statement"),
        ("funding statement", "Funding Statement"),
        ("competing interests declaration", "Competing Interests"),
        ("AI assistance statement", "AI Assistance Statement"),
        ("author-date fallback", "\\usepackage[authoryear,round]{natbib}"),
    ]
    for label, snippet in required_snippets:
        if snippet not in source:
            fail(f"missing {label}: {snippet}")

    if "Jacob Anderson" in source or "github.com/Jacoba" in source:
        fail("anonymous manuscript contains identifying author or repository text")

    data_index = source.find("Data Availability Statement")
    bibliography_index = min(
        index for index in (source.find("\\printbibliography"), source.find("\\bibliography{references}")) if index >= 0
    )
    if data_index < 0 or data_index > bibliography_index:
        fail("Data Availability Statement must appear before the reference list")

    figure_count = source.count("\\begin{figure}")
    description_count = source.count("\\Description{")
    if description_count < figure_count:
        fail("each manuscript figure should include an accessibility description")

    words = word_count(source)
    if words > MAX_WORDS:
        fail(f"main manuscript has {words} words, above JLC's {MAX_WORDS}-word article limit")

    if "Competing interests:" not in title_page:
        fail("title page must include the explicit competing interests declaration")

    print(f"JLC format check passed ({words} manuscript words, {figure_count} figures).")


if __name__ == "__main__":
    main()
