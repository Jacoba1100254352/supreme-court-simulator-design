# Paper Workspace

This folder contains the LaTeX manuscript for the constitutional-review simulator.

The primary journal target is Journal of Law and Courts. `main.tex` is anonymous by default and is written to use the official Cambridge/Overleaf `cup-journal` template with `journal=jlc` when that class is available. The local machine currently builds through the fallback review-copy path because TeX Live Basic does not ship `cup-journal.cls` or `biber`.

Build it from the repository root:

```sh
make paper
```

The manuscript is intentionally cautious: it presents the simulator as a design-search framework and treats the v2 campaign plus v4 diagnostics as demonstrations of comparative mechanics rather than validation.

`make paper` regenerates LaTeX figure fragments from `reports/constitutional-review-campaign-v2.csv` and generated table fragments from the campaign, calibration, parameter-sweep, and mechanism-ablation reports before compiling. It then copies the rebuilt PDF to `paper/main.pdf` and fails if that checked-in PDF is older than the LaTeX inputs. The current manuscript includes a domain-specific claimant-success heatmap, a public-confidence/constitutional-conflict scatter plot, an emergency-docket profile chart with numeric bar labels, a selected-results table, a calibration-guardrail table, an uncertainty-band table, and a mechanism-level contrast table.

The same command runs `paper/scripts/check_jlc_format.py` and `paper/scripts/check_source_audit.py`, which check the main JLC-facing requirements that can be validated locally: anonymous review mode, JLC template options, hidden hyperlink borders, author-date fallback, figure/table descriptions, figure references in the text, data availability before the references, declaration sections, generated table fragments, a methods appendix, source-audit coverage, source-provenance manifests, and the 10,000-word article ceiling. `make paper-jlc-template-check` adds the official-template requirement and fails if `cup-journal.cls` is unavailable.

`make paper-figure-files` exports standalone production-oriented figure files under `figure-exports/`. The PDFs are built from the same LaTeX fragments as the manuscript, and PNG files are generated when `pdftoppm` is available.

Additional submission-prep files:

- `title-page.tex`: non-anonymous title page for journal submission systems.
- `abstract-variants.md`: short abstracts/proposal variants for CELS, ICON-S, and APSA-style routes.
- `source-audit.csv`: claim-level source and artifact anchors for the manuscript.

Use `make paper-strict-check` before a non-anonymous submission package. Use `make paper-jlc-template-check` in Overleaf or another environment that provides the official Cambridge class. Use `make anonymous-submission-package` from the repository root for blinded review materials. Use `make replication-package` for a full non-anonymous archive under `dist/` when the journal requests acceptance-stage replication materials.
