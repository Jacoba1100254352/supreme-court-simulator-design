# Constitutional Review Simulator Usage

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

Write campaign artifacts:

```sh
make campaign
```

Run the preserved v0 campaign:

```sh
make campaign-v0
```

Build the LaTeX paper:

```sh
make paper
```

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

Import legislative outputs:

```sh
make campaign ARGS="--legislative-input '/Users/jacobanderson/Documents/simulators/Congress Institutional Simulator/reports/simulation-campaign-v21-paper.csv'"
```

The importer accepts the congressional simulator campaign CSV schema and also accepts direct columns such as `legalQuality`, `rightsRisk`, `weakMandateRate`, `partisanSkew`, `volatility`, `publicLegitimacy`, and `enactedVolume`.

## Outputs

Campaign runs write:

- `reports/constitutional-review-campaign-v2.csv`
- `reports/constitutional-review-campaign-v2.md`
- `reports/constitutional-review-campaign-v2-manifest.json`

Diagnostic runs also write empirical calibration, source-range appendix, seed-robustness, mechanism-ablation, parameter-prior, legislative-family, and manipulation-stress reports. `--cases` is now the filed universe per run. Admission filtering determines how many of those filings become merits transfers or emergency merits follow-through. The campaign CSV includes review-path admission rates, certiorari signals, emergency legitimacy risk, emergency grant rate, quorum failure, opinion fragmentation, formal legal responses, practical implementation responses, and direct output metrics such as overall and domain-specific rights-claimant success, doctrinal depth, remedial breadth, lower-court compliance, elite acceptance, and public confidence.

The preserved v0 and v1 targets write the same campaign filename pattern with `v0` and `v1`.
