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

Import legislative outputs:

```sh
make campaign ARGS="--legislative-input '/Users/jacobanderson/Documents/simulators/Congress Institutional Simulator/reports/simulation-campaign-v21-paper.csv'"
```

The importer accepts the congressional simulator campaign CSV schema and also accepts direct columns such as `legalQuality`, `rightsRisk`, `weakMandateRate`, `partisanSkew`, `volatility`, `publicLegitimacy`, and `enactedVolume`.

## Outputs

Campaign runs write:

- `reports/constitutional-review-campaign-v1.csv`
- `reports/constitutional-review-campaign-v1.md`
- `reports/constitutional-review-campaign-v1-manifest.json`

The preserved v0 target writes the same filenames with `v0`.
