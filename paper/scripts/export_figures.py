#!/usr/bin/env python3
"""Build standalone figure files for journal submission packages."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXPORT_DIR = ROOT / "paper" / "figure-exports"
BUILD_DIR = EXPORT_DIR / "build"

FIGURES = [
    (
        "model_flow",
        "Simulation state-transition flowchart",
        "Flowchart showing filed universe, access path, admission screen, screen-out, settlement, emergency route, merits route, decision, post-decision response, and output diagnostics.",
    ),
    (
        "domain_claimant_success",
        "Domain-specific claimant-success delta heatmap",
        "Heatmap comparing claimant-success changes from the current-like baseline by legal domain across selected court designs.",
    ),
    (
        "conflict_confidence_tradeoff",
        "Process-legitimacy and constitutional-conflict tradeoff",
        "Scatter plot of process legitimacy against the constitutional-conflict index for selected court designs.",
    ),
    (
        "emergency_profile",
        "Emergency-review and process-legitimacy profile",
        "Horizontal bar chart comparing emergency irregularity, emergency legitimacy risk, and process legitimacy.",
    ),
]


def wrapper(stem: str, title: str, description: str) -> str:
    return rf"""\documentclass[11pt]{{article}}
\usepackage[margin=0.25in,paperwidth=7.6in,paperheight=5.6in]{{geometry}}
\usepackage{{xcolor}}
\usepackage{{graphicx}}
\ifdefined\pdfinfoomitdate\pdfinfoomitdate=1\fi
\ifdefined\pdfsuppressptexinfo\pdfsuppressptexinfo=-1\fi
\ifdefined\pdftrailerid\pdftrailerid{{}}\fi
\pagestyle{{empty}}
\begin{{document}}
\noindent\textbf{{{title}}}\par
\smallskip
\noindent\input{{../figures/{stem}}}
\par\smallskip
\noindent\footnotesize Accessibility description: {description}
\end{{document}}
"""


def run(command: list[str], cwd: Path) -> None:
    subprocess.run(command, cwd=cwd, check=True)


def main() -> None:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    has_latexmk = shutil.which("latexmk") is not None
    has_pdftoppm = shutil.which("pdftoppm") is not None
    if not has_latexmk:
        raise SystemExit("latexmk is required to export standalone figure PDFs")

    for stem, title, description in FIGURES:
        tex_path = EXPORT_DIR / f"{stem}.tex"
        tex_path.write_text(wrapper(stem, title, description))
        run(
            [
                "latexmk",
                "-pdf",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-outdir=build",
                tex_path.name,
            ],
            EXPORT_DIR,
        )
        pdf_path = BUILD_DIR / f"{stem}.pdf"
        final_pdf = EXPORT_DIR / f"{stem}.pdf"
        shutil.copyfile(pdf_path, final_pdf)
        if has_pdftoppm:
            run(
                [
                    "pdftoppm",
                    "-png",
                    "-r",
                    "300",
                    "-singlefile",
                    final_pdf.name,
                    stem,
                ],
                EXPORT_DIR,
            )


if __name__ == "__main__":
    main()
