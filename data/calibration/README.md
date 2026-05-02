# Calibration Data

This directory contains normalized empirical calibration observations consumed by `CalibrationRunner`.

Rows use the schema:

```csv
sourceKey,domain,metric,term,numerator,denominator,value,sourceUrl,notes
```

The normalized files are intentionally small and reproducible. Refresh them from raw public datasets with:

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
