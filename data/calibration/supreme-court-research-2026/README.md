# Supreme Court Simulator Research Tables

Normalized rows imported from local Deep Research markdown reports. The raw reports are not committed; this directory preserves only table rows and source-register metadata for calibration and paper transparency.

Rows use the same synthesis schema as the earlier `supreme-court-synthesis/` import: `metricKey`, `observedValue`, `confidenceLevel`, `validationUse`, `denominatorSpec`, `coverageScope`, and `comparabilityClass` are retained so strict validation, loose calibration, proxy context, and design-prior rows remain separate.

| Report | File | Rows | Sections |
| --- | --- | ---: | --- |
| Supreme Court Simulator - Calibration Targets.md | `supreme-court-simulator-calibration-targets.csv` | 41 | Certiorari calibration targets: 24; Comparative and institutional design priors: 3; Emergency and shadow-docket calibration targets: 14 |
| Supreme Court Simulator - Institutional Design and Empirical Anchors.md | `supreme-court-simulator-institutional-design-and-empirical-anchors.csv` | 29 | Supreme Court Simulator - Institutional Design and Empirical Anchors: 29 |
| Supreme Court Simulator - Institutional Design Evidence.md | `supreme-court-simulator-institutional-design-evidence.csv` | 20 | Proxy, context, and design-prior rows: 8; Validation and calibration rows: 12 |
| Supreme Court Simulator - Litigation Pipeline Incentives.md | `supreme-court-simulator-litigation-pipeline-incentives.csv` | 30 | Filter and docket variables: 12; Repeat-player, case-mix, and access-path variables: 13; Synthetic modeling priors derived from the empirical record: 5 |

`source-register.csv` groups rows by named source and URL. The Java loader reads numeric `observedValue` rows recursively, but paper interpretation must still respect each row's `validationUse` and denominator notes.

Regenerate with:

```sh
python3 tools/import_deep_research_tables.py --reports \
  "/path/to/Supreme Court Simulator - Calibration Targets.md" \
  "/path/to/Supreme Court Simulator - Institutional Design and Empirical Anchors.md" \
  "/path/to/Supreme Court Simulator - Institutional Design Evidence.md" \
  "/path/to/Supreme Court Simulator - Litigation Pipeline Incentives.md"
```
