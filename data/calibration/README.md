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

Deep Research synthesis tables live under `supreme-court-synthesis/`. They use the report-oriented schema:

```csv
metricKey,jurisdiction,timePeriod,lowerBound,upperBound,observedValue,sourceName,sourceUrl,confidenceLevel,validationUse,denominatorSpec,coverageScope,comparabilityClass,rawSection
```

Regenerate those files from the local Deep Research synthesis report with:

```sh
python3 tools/import_deep_research_synthesis.py
```

The Java calibration loader reads both schemas recursively. Rows marked `strict_validation`, `loose_calibration`, and `paper_only_context` are preserved with their denominator and coverage notes so proxy/context rows are not mistaken for hard simulator validation targets.
