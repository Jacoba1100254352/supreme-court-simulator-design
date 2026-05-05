# Legislative Output Fixtures

This directory contains frozen legislative-simulator CSV outputs used as external inputs for the constitutional-review paper runs.

The fixtures preserve the project boundary: the constitutional-review simulator imports legislative outputs through CSV data contracts and does not depend on Congress simulator Java source code.

## Paper Input

`simulation-campaign-v21-paper.csv` is the default paper-facing legislative profile used by:

```sh
make campaign
make diagnostics
make paper
```

The file was copied from the separate Congress Institutional Simulator report artifact named `simulation-campaign-v21-paper.csv`. Its SHA-256 hash is:

```text
554c92f6be3c1ccfc7b2635d6588b790101b6be1d50badc5b537b97c0851fcbe
```

## Family Comparison Inputs

The additional `simulation-campaign-v0.csv`, `simulation-campaign-v5.csv`, `simulation-campaign-v10.csv`, `simulation-campaign-v15.csv`, `simulation-campaign-v20.csv`, and `simulation-manipulation-stress.csv` fixtures support the legislative-family comparison diagnostic.

These files are source data for this repository's replication workflow. Refresh them only when deliberately updating the imported legislative baseline, then rerun `make diagnostics paper`.

