# Replication Plan

This project is being prepared for a Journal of Law and Courts submission and a possible CELS working-paper submission.

## Requirements

- Java 21 or newer
- `make`
- A LaTeX installation with `latexmk` for the paper

The Java simulator has no external Java dependencies.

## Reproduce Main Artifacts

From the repository root:

```sh
make test
make campaign ARGS="--legislative-input '/Users/jacobanderson/Documents/simulators/Congress Institutional Simulator/reports/simulation-campaign-v21-paper.csv'"
make diagnostics ARGS="--legislative-input '/Users/jacobanderson/Documents/simulators/Congress Institutional Simulator/reports/simulation-campaign-v21-paper.csv'"
make paper
```

The manuscript table is based on `reports/constitutional-review-campaign-v2.csv` and `reports/constitutional-review-campaign-v2.md`.

## Observed, Coded, Assumed, Simulated

Observed inputs:

- Normalized calibration rows in `data/calibration/`.
- Imported legislative-output profiles read through the documented CSV contract.

Coded institutional rules:

- Scenario definitions in `src/main/java/constitutionalreview/simulation/ScenarioCatalog.java`.
- Court-design fields in `src/main/java/constitutionalreview/institution/CourtDesign.java`.
- Review paths and timing in `src/main/java/constitutionalreview/model/AccessPath.java` and `ReviewTiming.java`.

Model assumptions:

- Case-world generation in `src/main/java/constitutionalreview/simulation/WorldGenerator.java`.
- Admission scoring in `src/main/java/constitutionalreview/simulation/AdmissionFilter.java`.
- Strategic response and decision mechanics in `src/main/java/constitutionalreview/institution/ConstitutionalReviewProcess.java`.

Simulated outputs:

- Campaign outputs in `reports/constitutional-review-campaign-v2.*`.
- Calibration guardrails in `reports/calibration-baseline.*`.
- Sensitivity and diagnostic reports in `reports/seed-robustness-v2.*`, `reports/parameter-sweep-v4.*`, `reports/mechanism-ablation-v2.*`, `reports/legislative-family-comparison-v3.*`, and `reports/manipulation-stress-v2.*`.

## Data Availability Statement Draft

Replication materials, normalized calibration tables, deterministic seeds, scenario definitions, and generated reports will be deposited in a public repository or the Journal of Law and Courts Dataverse if the manuscript is accepted. Repository identifiers may be withheld in anonymous review materials.
