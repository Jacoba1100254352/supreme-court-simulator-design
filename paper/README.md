# Paper Workspace

This folder contains the LaTeX manuscript for the constitutional-review simulator.

The primary journal target is Journal of Law and Courts. `main.tex` is anonymous by default and is written to use the official Cambridge/Overleaf `cup-journal` template with `journal=jlc` when that class is available. The local machine currently builds through the fallback review-copy path because TeX Live Basic does not ship `cup-journal.cls` or `biber`.

Build it from the repository root:

```sh
make paper
```

The manuscript is intentionally cautious: it presents the simulator as a design-search framework and treats the v2 campaign plus v4 diagnostics as demonstrations of comparative mechanics rather than validation.

`make paper` regenerates LaTeX figure fragments from `reports/constitutional-review-campaign-v2.csv` before compiling. The current manuscript includes a domain-specific claimant-success heatmap, a public-confidence/constitutional-conflict scatter plot, and an emergency-docket profile chart.

The same command runs `paper/scripts/check_jlc_format.py`, which checks the main JLC-facing requirements that can be validated locally: anonymous review mode, JLC template options, author-date fallback, figure descriptions, data availability before the references, declaration sections, and the 10,000-word article ceiling.

Additional submission-prep files:

- `title-page.tex`: non-anonymous title-page skeleton for journal submission systems.
- `abstract-variants.md`: short abstracts/proposal variants for CELS, ICON-S, and APSA-style routes.
