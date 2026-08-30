# Supreme Court Simulator Design Usage

## Commands

Build and run:

```sh
make build
make run
```

Run a smaller comparison:

```sh
make run ARGS="--runs 20 --cases 30 --scenarios current-us-like,term-limited-balanced,cross-checking-courts"
```

Judicial-electorate appointment variants can be run directly:

```bash
make run ARGS="--runs 20 --cases 30 --scenarios judicial-electorate-selection,judicial-electorate-all-federal,judicial-electorate-appellate-only,judicial-electorate-selected-circuits,judicial-electorate-state-high-courts"
```

The selector and nominee presets behind those variants are documented in `data/design/judicial-electorate-pools.csv`.

Write campaign artifacts:

```sh
make campaign
```

By default this uses the paper's legislative-output import contract:

```sh
PAPER_LEGISLATIVE_INPUT="data/external/legislative/simulation-campaign-v21-paper.csv"
```

The current default is the in-repository fixture `data/external/legislative/simulation-campaign-v21-paper.csv`; override `PAPER_LEGISLATIVE_INPUT` for a different congressional-simulator CSV. Set `PAPER_ARGS=` only when you intentionally want a synthetic-only run that will not match the paper manifests.

Run the preserved v0 campaign:

```sh
make campaign-v0
```

Build the LaTeX paper:

```sh
make paper
```

This regenerates manuscript figures and tables, verifies report manifests and substantive data invariants, checks claim-to-source traceability, exports standalone figure files, compiles the PDF, and checks the LaTeX log for unresolved references or citations.

Run strict paper checks and build the non-anonymous title page:

```sh
make paper-strict-check
```

Create a review/deposit replication archive:

```sh
make replication-package
```

This writes `dist/constitutional-review-replication.zip` and `dist/replication-package-manifest.json`.

Create a blinded anonymous-review archive:

```sh
make anonymous-submission-package
```

This writes `dist/constitutional-review-anonymous-submission.zip`, `dist/constitutional-review-anonymous-manuscript.zip`, `dist/constitutional-review-anonymous-supplement.zip`, and `dist/anonymous-submission-manifest.json`. The package builder sanitizes local absolute paths and repository references, excludes non-anonymous metadata, and fails if identifying strings remain.

Run the full diagnostic suite:

```sh
make diagnostics
```

Run empirical calibration against a custom normalized source table directory:

```sh
make calibrate CALIBRATION_DATA_DIR=/path/to/calibration
```

Import the local Supreme Court Deep Research synthesis CSV blocks into calibration inputs:

```sh
python3 tools/import_deep_research_synthesis.py
make calibrate
```

By default the importer looks for `data/raw/calibration/deep-research-report5.md`; pass `--report /path/to/report.md` when the report is elsewhere.

Refresh normalized source tables from raw downloads:

```sh
make raw-source-refresh
```

By default the refresh looks in `data/raw/calibration/`, which is ignored by git. Pass explicit paths through `ARGS` when raw files live elsewhere.

Refresh or resume the official OT2023 paid/IFP docketed cohort:

```sh
make certiorari-docketed-cohort
```

The extractor reuses same-snapshot rows by default, retries bounded Court-site failures, and regenerates the cohort manifest, summary, Journal reconciliation, and normalized calibration rows.

Import legislative outputs:

```sh
make campaign ARGS="--legislative-input data/external/legislative/simulation-campaign-v21-paper.csv"
```

The importer accepts the congressional simulator campaign CSV schema and also accepts direct columns such as `legalQuality`, `rightsRisk`, `weakMandateRate`, `partisanSkew`, `volatility`, `publicLegitimacy`, and `enactedVolume`.

## Outputs

Campaign runs write:

- `reports/constitutional-review-campaign-v2.csv`
- `reports/constitutional-review-campaign-v2.md`
- `reports/constitutional-review-campaign-v2-manifest.json`

Diagnostic runs also write empirical calibration, source-range appendix, seed-robustness, mechanism-ablation, parameter-prior, legislative-family, and manipulation-stress reports. `--cases` is now the filed universe per run. Admission filtering determines how many of those filings become merits transfers or emergency merits follow-through. The campaign CSV includes review-path admission rates, certiorari signals, emergency legitimacy risk, emergency grant rate, quorum failure, opinion fragmentation, formal legal responses, practical implementation responses, and direct output metrics such as overall and domain-specific rights-claimant success, doctrinal depth, remedial breadth, lower-court compliance, elite acceptance, and the modeled public-legitimacy proxy. For compatibility, the CSV retains legacy fields such as `shadowDocketAbuse` and `publicConfidence`; the paper-facing aliases are `emergencyProcessIrregularity` and `processLegitimacyProxy`.

The preserved v0 and v1 targets write the same campaign filename pattern with `v0` and `v1`.

Paper support outputs also include `paper/source-audit.csv`, generated table fragments in `paper/tables/`, standalone production figure files in `paper/figure-exports/`, and the replication package manifest under `dist/` when packaging is requested.

Validation-support outputs include the pathway dashboard, benchmark-readiness reports, emergency docket-linkage materials, the closed OT2023 paid/IFP docketed-intake cohort and its normalized calibration rows, summary, and Journal reconciliation, older Journal certiorari slices, implementation/compliance work queues, the HUDOC-EXEC monitoring extract, and generated benchmark templates under `reports/`, `data/benchmarks/`, and `data/calibration/`. The certiorari cohort supports bounded docket-visible screening evidence over 4,222 paid/IFP dockets and 4,033 certiorari petitions. It does not cover undocketed submissions or close issue, counsel, split-quality, vehicle-quality, lower-court-compliance, government-noncompliance, or external emergency implementation claims.
