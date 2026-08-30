# Calibration Data

This directory contains normalized empirical calibration observations consumed by `CalibrationRunner`.

`provenance-manifest.csv` records the source version, source URL, raw-source requirement, transformation script, extraction mode, validation use, and denominator specification for each normalized source family. Treat that manifest as the first place to check whether a row is a strict validation target, a loose calibration row, or paper-only context.

Rows use the schema:

```csv
sourceKey,domain,metric,term,numerator,denominator,value,sourceUrl,notes
```

The normalized files are intentionally small and reproducible. For the full local refresh workflow, put raw downloads under `data/raw/calibration/` and run:

```sh
make raw-source-refresh
```

The wrapper detects the SCDB case-centered zip, an optional shadow-docket zip, an optional Deep Research synthesis report, and an optional manually prepared Harvard Law Review statistics summary. It writes `dist/calibration-source-refresh-manifest.json` with source names and hashes. Raw source files are ignored by git.

You can also refresh the SCDB and shadow-docket reductions directly with:

```sh
python3 tools/build_calibration_tables.py \
  --scdb-case-zip /path/to/SCDB_2025_01_caseCentered_Citation.csv.zip \
  --shadow-zip /path/to/shadow_docket_database_v2-0_data_files.zip \
  --output-dir data/calibration
```

Raw SCDB and shadow-docket archives are not committed because the shadow-docket archive is large. The generated tables preserve source URL, term, numerator, denominator, and transformation notes.

`scotus-certiorari-docketed-cohort-ot2023.csv` and `scotus-certiorari-docketed-cohort-ot2024.csv` are generated from the row-level official-docket extracts in `data/benchmarks/` by `tools/extract_certiorari_docketed_cohort_benchmark.py`. Together they supply two independently enumerated terms of docketed-intake shares and petition-level CFR, CVSG, amicus-presence, relist, and grant/GVR rates: 8,076 paid/IFP dockets and 7,716 docketed certiorari petitions. Three OT2024 certiorari petitions remain pending or held as of the July 26, 2026 snapshot and are excluded from the resolved-outcome grant/GVR denominator. These cohorts are closed for their published-statistics docketed-intake ranges, not for submissions that were never docketed or for constitutional-review petitions alone. The loader prefers a direct term cohort over a near-identical imported summary row for the same metric and term so an official observation is not double weighted.

`lower-court-precedent-treatment-v1.csv` contains 60 term-pooled context rows generated from the public Masood, Kassow, and Songer (2019) replication file: three denominator-specific treatment shares for each 1995--2004 source-decision term, separately for all 876 precedents and the 223 source-flagged constitutional-issue precedents. The source directly measures aggregate doctrinal uptake through 2016, but its citation/treatment-selected counts are not denominator-matched to the simulator's synthetic case-average `lowerCourtCompliance` score and do not measure practical implementation. Refresh and checksum-reconcile the benchmark with:

```sh
make lower-court-precedent-benchmark
```

Pass `ARGS="--refresh --extraction-date YYYY-MM-DD"` to force a source refresh. The downloaded Dataverse metadata, Stata file, tab export, replication code, and DDI metadata are cached only under ignored `data/raw/lower-court-precedent-treatment/`.

`environmental-implementation-cohort-v1.csv` contains decision-specific data-quality checks and descriptive case-study summaries derived from a separate environmental cohort. Its lower-court layer covers 191 deduplicated published CourtListener-linked federal citing-opinion documents in five fixed 730-day windows and 65 nationwide-applicability/published-citation-presence cells; 115 documents have retrievable full text and source-decision context, with nonrandom missingness. The six automated directional candidates remain pending expert legal review. Its practical layer preserves five published agency-response classifications from Gurganus (2025), joined to official implementation actions: four compliant and one narrowly compliant. Those fractions describe purposive case-study composition, not compliance probabilities or behavioral guardrails. Rebuild the cohort with:

```sh
make environmental-implementation-cohort
```

Pass `ARGS="--refresh --extraction-date YYYY-MM-DD"` to refresh CourtListener searches and public source documents. Raw search pages, public opinion files, and official-source documents are cached only under ignored `data/raw/environmental-implementation-cohort/`.

Deep Research synthesis tables live under `supreme-court-synthesis/` and `supreme-court-research-2026/`. They use the report-oriented schema:

```csv
metricKey,jurisdiction,timePeriod,lowerBound,upperBound,observedValue,sourceName,sourceUrl,confidenceLevel,validationUse,denominatorSpec,coverageScope,comparabilityClass,rawSection
```

Regenerate those files from the local Deep Research synthesis report with:

```sh
python3 tools/import_deep_research_synthesis.py
```

Regenerate the newer markdown-table research import with:

```sh
python3 tools/import_deep_research_tables.py --reports \
  "/path/to/Supreme Court Simulator - Calibration Targets.md" \
  "/path/to/Supreme Court Simulator - Institutional Design and Empirical Anchors.md" \
  "/path/to/Supreme Court Simulator - Institutional Design Evidence.md" \
  "/path/to/Supreme Court Simulator - Litigation Pipeline Incentives.md"
```

The Java calibration loader reads both schemas recursively. Rows marked `strict_validation`, `loose_calibration`, `proxy_context`, `design_prior`, and `paper_only_context` are preserved with their denominator and coverage notes so proxy/context rows are not mistaken for hard simulator validation targets.
