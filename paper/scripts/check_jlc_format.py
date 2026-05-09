#!/usr/bin/env python3
"""Lightweight Journal of Law and Courts manuscript checks."""

from __future__ import annotations

import re
import subprocess
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
    ROOT / "paper" / "tables" / "calibration_classification.tex",
    ROOT / "paper" / "tables" / "v2_selected.tex",
    ROOT / "paper" / "tables" / "pipeline_diagnostics.tex",
    ROOT / "paper" / "tables" / "uncertainty_bands.tex",
    ROOT / "paper" / "tables" / "sensitivity_drivers.tex",
    ROOT / "paper" / "tables" / "mechanism_summary.tex",
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


def has_cambridge_class() -> bool:
    try:
        result = subprocess.run(
            ["kpsewhich", "cup-journal.cls"],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except FileNotFoundError:
        return False
    return result.returncode == 0


def check_domain_heatmap_layout() -> None:
    figure = ROOT / "paper" / "figures" / "domain_claimant_success.tex"
    if not figure.exists():
        return
    source = figure.read_text()
    headers = [
        (float(x), float(y), label)
        for x, y, label in re.findall(
            r"\\put\(([0-9.]+),([0-9.]+)\)\{\\makebox\(0,0\)\{\\textbf\{([^}]+)\}\}\}",
            source,
        )
    ]
    cells = [
        (float(x), float(y), float(width), float(height))
        for x, y, width, height in re.findall(
            r"\\put\(([0-9.]+),([0-9.]+)\)\{\\color\{(?:red|black)![0-9]+\}\\rule\{([0-9.]+)mm\}\{([0-9.]+)mm\}\}",
            source,
        )
    ]
    row_labels = [
        (float(x), float(y), label)
        for x, y, label in re.findall(
            r"\\put\(([0-9.]+),([0-9.]+)\)\{\\makebox\(0,0\)\[r\]\{\\color\{(?:red|black)\}([^}]+)\}\}",
            source,
        )
    ]
    if len(headers) != 6 or len(cells) != 48 or len(row_labels) != 8:
        fail("domain claimant-success heatmap has an unexpected generated shape")

    header_y = min(y for _x, y, _label in headers)
    first_row_y = max(y for _x, y, _width, _height in cells)
    cell_height = max(height for _x, y, _width, height in cells if y == first_row_y)
    header_gap = header_y - (first_row_y + cell_height)
    if header_gap < 3.0:
        fail(f"domain heatmap header is too close to first row ({header_gap:.1f}mm gap)")

    first_row_cells = sorted((x, width) for x, y, width, _height in cells if y == first_row_y)
    left_gutter = first_row_cells[0][0] - max(x for x, _y, _label in row_labels)
    if left_gutter < 7.0:
        fail(f"domain heatmap row-label gutter is too narrow ({left_gutter:.1f}mm)")

    cell_gaps = [
        next_x - (x + width)
        for (x, width), (next_x, _next_width) in zip(first_row_cells, first_row_cells[1:])
    ]
    if min(cell_gaps) < 1.2:
        fail(f"domain heatmap column padding is too narrow ({min(cell_gaps):.1f}mm)")

    right_edge = max(x + width for x, _y, width, _height in cells)
    if right_edge > 126.0:
        fail(f"domain heatmap right edge is too close to the figure boundary ({right_edge:.1f}mm)")

    row_centers = sorted({y for _x, y, _label in row_labels}, reverse=True)
    row_gaps = [upper - lower for upper, lower in zip(row_centers, row_centers[1:])]
    if min(row_gaps) < 6.6:
        fail(f"domain heatmap row padding is too narrow ({min(row_gaps):.1f}mm)")


def check_conflict_confidence_axis_labels() -> None:
    figure = ROOT / "paper" / "figures" / "conflict_confidence_tradeoff.tex"
    if not figure.exists():
        return
    source = figure.read_text()
    if "Public confidence $\\uparrow$" in source or "Constitutional conflict $\\downarrow$" in source:
        fail("conflict/confidence figure should spell out metric direction instead of rotating arrow glyphs")
    if "\\rotatebox{90}{\\makebox(0,0){Public confidence (higher is better)}}" not in source:
        fail("conflict/confidence figure should use a clear rotated y-axis label outside the tick labels")

    x_label = re.search(
        r"\\put\(([0-9.]+),([0-9.]+)\)\{\\makebox\(0,0\)\{Constitutional conflict \(lower is better\)\}\}",
        source,
    )
    if not x_label:
        fail("conflict/confidence figure is missing the x-axis label")
    x_label_x = float(x_label.group(1))
    x_label_y = float(x_label.group(2))
    if not 64.0 <= x_label_x <= 68.0:
        fail(f"conflict/confidence x-axis label is not centered under the plot ({x_label_x:.1f}mm)")
    if x_label_y > 5.0:
        fail(f"conflict/confidence x-axis label is too close to the tick labels ({x_label_y:.1f}mm)")

    y_label = re.search(
        r"\\put\(([0-9.]+),([0-9.]+)\)\{\\rotatebox\{90\}\{\\makebox\(0,0\)\{Public confidence \(higher is better\)\}\}\}",
        source,
    )
    if not y_label:
        fail("conflict/confidence figure is missing the rotated y-axis label coordinates")
    y_label_x = float(y_label.group(1))
    y_label_y = float(y_label.group(2))
    if not 9.0 <= y_label_x <= 13.0:
        fail(f"conflict/confidence y-axis label is not in the left-axis gutter ({y_label_x:.1f}mm)")
    if not 40.0 <= y_label_y <= 46.0:
        fail(f"conflict/confidence y-axis label is not vertically centered ({y_label_y:.1f}mm)")

    random_label = re.search(
        r"\\put\(([0-9.]+),([0-9.]+)\)\{\\makebox\(0,0\)\[l\]\{\\colorbox\{white\}\{\\color\{black\}Random panels\}\}\}",
        source,
    )
    if not random_label:
        fail("conflict/confidence figure is missing the Random panels label")
    random_x = float(random_label.group(1))
    random_y = float(random_label.group(2))
    if random_x < 94.0 or not 46.0 <= random_y <= 51.0:
        fail(f"Random panels label should sit close to its marker in the right-middle callout area ({random_x:.1f},{random_y:.1f}mm)")


def main() -> None:
    strict_submission = "--strict-submission" in sys.argv
    require_cambridge_class = "--require-cambridge-class" in sys.argv
    source = MAIN.read_text()
    title_page = TITLE_PAGE.read_text() if TITLE_PAGE.exists() else ""

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
        ("claim-boundary section", "\\section{Claim Boundaries and Interpretation}"),
        ("empirical claim boundary", "Empirical claims are limited"),
        ("synthetic finding boundary", "Synthetic findings are outputs"),
        ("speculative recommendation boundary", "Speculative design recommendations are conditional"),
        ("theory section", "\\section{Theory and Design Space}"),
        ("expectations section", "\\section{Expectations}"),
        ("calibration guardrail table", "tables/calibration_guardrails"),
        ("calibration classification table", "tables/calibration_classification"),
        ("generated selected results table", "tables/v2_selected"),
        ("litigation-pipeline diagnostics table", "tables/pipeline_diagnostics"),
        ("uncertainty band table", "tables/uncertainty_bands"),
        ("sensitivity drivers table", "tables/sensitivity_drivers"),
        ("mechanism summary table", "tables/mechanism_summary"),
        ("methods appendix", "\\section{Model Mechanics}"),
        ("source audit", "paper/source-audit.csv"),
    ]
    for label, snippet in required_snippets:
        if snippet not in source:
            fail(f"missing {label}: {snippet}")

    if require_cambridge_class and not has_cambridge_class():
        fail("official Cambridge cup-journal.cls is not available on this TeX installation")

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

    check_domain_heatmap_layout()
    check_conflict_confidence_axis_labels()

    words = word_count(source)
    if words > MAX_WORDS:
        fail(f"main manuscript has {words} words, above JLC's {MAX_WORDS}-word article limit")
    if words < 3_000:
        warn(f"main manuscript has only {words} words; JLC review will likely expect fuller theory and method exposition")

    if strict_submission and not TITLE_PAGE.exists():
        fail("strict submission check requires a separate non-anonymous title page")
    if TITLE_PAGE.exists():
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
