# Supreme Court Deep Research Synthesis

Imported from local Deep Research synthesis report `deep-research-report5.md`. The raw report is not committed.

These CSVs preserve the ingest-ready research rows as calibration inputs.
Rows include `confidenceLevel`, `validationUse`, `denominatorSpec`, `coverageScope`, and `comparabilityClass` so strict validation, loose calibration, and paper-only context are not conflated.
The synthesis itself is not cited as empirical authority in the manuscript; `source-register.csv` preserves the named sources and URLs represented in the normalized rows.

| Section | File | Rows |
| --- | --- | ---: |
| Comparative court design presets | `comparative-court-design-presets.csv` | 7 |
| Lower-court and intake calibration | `lower-court-intake-calibration.csv` | 17 |
| Emergency docket calibration | `emergency-docket-calibration.csv` | 9 |
| Cross-national calibration targets | `cross-national-calibration-targets.csv` | 11 |
| Institutional budget, delay, and complexity benchmarks | `institutional-cost-delay-complexity-benchmarks.csv` | 12 |

See `source-register.csv` for a normalized source register grouped by source name and URL.

The Java loader reads numeric `observedValue` rows from these files recursively when `data/calibration` is used as the calibration directory.
Non-numeric design-preset rows remain available for documentation and scenario-design work, but are not treated as numerical validation observations.
