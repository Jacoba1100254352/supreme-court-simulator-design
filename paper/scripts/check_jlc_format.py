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
REQUIRED_GENERATED = [
    ROOT / "paper" / "figures" / "domain_claimant_success.tex",
    ROOT / "paper" / "figures" / "conflict_confidence_tradeoff.tex",
    ROOT / "paper" / "figures" / "emergency_profile.tex",
    ROOT / "paper" / "tables" / "calibration_guardrails.tex",
    ROOT / "paper" / "tables" / "uncertainty_bands.tex",
]


def fail(message: str) -> None:
    print(f"JLC format check failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def warn(message: str) -> None:
    print(f"JLC format warning: {message}", file=sys.stderr)


def strip_latex(source: str) -> str:
    source = re.sub(r"%.*", " ", source)
    source = re.sub(r"\\begin\{[^}]+\}|\\end\{[^}]+\}", " ", source)
    source = re.sub(r"\\[a-zA-Z*]+(?:\[[^\]]*\])?(?:\{[^{}]*\})?", " ", source)
    source = re.sub(r"[{}$^_&~]", " ", source)
    return source


def word_count(source: str) -> int:
    return len(re.findall(r"[A-Za-z][A-Za-z0-9'-]*", strip_latex(source)))


def main() -> None:
    strict_submission = "--strict-submission" in sys.argv
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
        ("hidden hyperlink borders", "\\hypersetup{hidelinks}"),
        ("theory section", "\\section{Theory and Design Space}"),
        ("calibration guardrail table", "tables/calibration_guardrails"),
        ("uncertainty band table", "tables/uncertainty_bands"),
        ("methods appendix", "\\section{Model Mechanics}"),
    ]
    for label, snippet in required_snippets:
        if snippet not in source:
            fail(f"missing {label}: {snippet}")

    if "Jacob Anderson" in source or "github.com/Jacoba" in source:
        fail("anonymous manuscript contains identifying author or repository text")

    for generated in REQUIRED_GENERATED:
        if not generated.exists():
            fail(f"missing generated manuscript fragment: {generated.relative_to(ROOT)}")

    data_index = source.find("Data Availability Statement")
    bibliography_index = min(
        index for index in (source.find("\\printbibliography"), source.find("\\bibliography{references}")) if index >= 0
    )
    if data_index < 0 or data_index > bibliography_index:
        fail("Data Availability Statement must appear before the reference list")

    generated_source = "\n".join(path.read_text() for path in REQUIRED_GENERATED if path.exists())
    combined_source = source + "\n" + generated_source
    figure_count = combined_source.count("\\begin{figure}")
    description_count = combined_source.count("\\Description{")
    table_count = combined_source.count("\\begin{table}")
    if description_count < figure_count + table_count:
        fail("each manuscript figure and table should include an accessibility description")

    labels = re.findall(r"\\label\{(fig:[^}]+)\}", source)
    for label in labels:
        if f"\\ref{{{label}}}" not in source:
            fail(f"figure label {label} is not cited in the manuscript text")

    words = word_count(source)
    if words > MAX_WORDS:
        fail(f"main manuscript has {words} words, above JLC's {MAX_WORDS}-word article limit")
    if words < 3_000:
        warn(f"main manuscript has only {words} words; JLC review will likely expect fuller theory and method exposition")

    if "Competing interests:" not in title_page:
        fail("title page must include the explicit competing interests declaration")
    if "Author Name" in title_page or "author@example.com" in title_page:
        message = "title page still contains placeholder author fields for non-anonymous submission"
        if strict_submission:
            fail(message)
        warn(message)

    print(f"JLC format check passed ({words} manuscript words, {figure_count} figures).")


if __name__ == "__main__":
    main()
