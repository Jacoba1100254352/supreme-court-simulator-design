# Journal of Law and Courts Submission Checklist

Use this checklist before uploading the anonymous manuscript package or sending the project for external methods review.

## Required Local Checks

Run from the repository root:

```sh
make test
make paper-strict-check
make anonymous-submission-package
```

If refreshed raw datasets are available, run this before the final strict check:

```sh
make raw-source-refresh
make diagnostics
make paper-strict-check
make anonymous-submission-package
```

The anonymous package target rebuilds the manuscript, stages a blinded package, writes separate manuscript and supplement archives, sanitizes local paths and repository references, and fails if author-identifying strings remain.

## Upload Set for Anonymous Review

- Anonymous manuscript PDF from `paper/main.pdf` or manuscript archive `dist/constitutional-review-anonymous-manuscript.zip`.
- Anonymous supplemental package, if requested during review: `dist/constitutional-review-anonymous-supplement.zip`.
- Short abstract from `paper/abstract-variants.md`, edited to match the submission form.
- Non-anonymous title-page metadata entered only in the journal submission system or uploaded separately if the system requests it outside peer-review files.

Do not upload `dist/constitutional-review-replication.zip` as the anonymous supplement unless the journal explicitly permits author-identifying supplemental material during review.

## JLC Formatting Items

- Manuscript remains in anonymous mode in `paper/main.tex`.
- Cambridge/JLC path is present through the `cup-journal`/`journal=jlc` branch, with the local fallback used only for local builds.
- Official-template environments should pass `make paper-jlc-template-check`; local TeX installations without `cup-journal.cls` are expected to fail that target.
- Figures and tables appear near first reference in the manuscript.
- Figure and table accessibility descriptions are present.
- Data Availability Statement appears before the references.
- Funding, competing-interest, and AI-assistance statements are present.
- `paper/source-audit.csv` has checked anchors for material claims.
- The manuscript stays under the 10,000-word article ceiling checked by `paper/scripts/check_jlc_format.py`.

## Replication and Data Availability

- Normalized calibration inputs are under `data/calibration/`.
- Source-provenance manifests are under `data/calibration/provenance-manifest.csv` and `data/external/legislative/source-provenance.csv`.
- Frozen legislative-output fixtures are under `data/external/legislative/`.
- Raw third-party archives remain outside git under `data/raw/calibration/` or another local path.
- `dist/calibration-source-refresh-manifest.json` is regenerated when raw sources are refreshed.
- Public repository and Dataverse identifiers are withheld in anonymous review materials.
- Full non-anonymous replication materials are prepared with `make replication-package` only for acceptance-stage deposit or non-blind review.

## External Review Gate

Before adding more realism layers, send `docs/external-methods-review-request.md` and the anonymous package to one methods-oriented reviewer. Ask them to focus on calibration guardrails, model identification, claim discipline, and whether any manuscript claim sounds more validated than the evidence supports.
