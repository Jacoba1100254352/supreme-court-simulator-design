# Journal of Law and Courts Submission Checklist

Use this checklist before uploading the anonymous manuscript package or sending the project for external methods review.

## Required Local Checks

Run from the repository root:

```sh
make test
make paper-strict-check
make anonymous-submission-package
make expert-review-check
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

- Anonymous manuscript PDF from `paper/emergency-review-constitutional-court-design.pdf` or manuscript archive `dist/constitutional-review-anonymous-manuscript.zip`.
- Anonymous supplemental package, if requested during review: `dist/constitutional-review-anonymous-supplement.zip`.
- Short abstract from `paper/abstract-variants.md`, edited to match the submission form.
- Non-anonymous title-page metadata entered only in the journal submission system or uploaded separately if the system requests it outside peer-review files.

Do not upload `dist/constitutional-review-replication.zip` as the anonymous supplement unless the journal explicitly permits author-identifying supplemental material during review.

## JLC Formatting Items

- Manuscript remains in anonymous mode in `paper/emergency-review-constitutional-court-design.tex`.
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
- Benchmark extraction schemas, templates, work queues, emergency docket-linkage extracts, paired certiorari cohorts, the 876-precedent aggregate lower-court treatment extract, the 191-event/65-cell environmental published-citation snapshot, its pending expert-review queue and five practical agency episodes, the HUDOC-EXEC monitoring extract, and implementation/compliance materials are included. The environmental slice supports descriptive citation presence and case-study composition only; it is not a behavioral guardrail.
- `paper/scripts/verify_paper_artifacts.py` reconciles all 876 aggregate-precedent rows and reductions plus the environmental cohort's 191 unique published events, 65 applicability/citation-presence cells, 115 public-text contexts, corrected 5-applied/1-distinguished automated-candidate counts, nonrandom missingness audit, 16-row pending review queue, five structured Gurganus classifications, official-source hashes, normalized rows, summaries, manifest hashes, and package inclusion.
- Source-provenance manifests are under `data/calibration/provenance-manifest.csv` and `data/external/legislative/source-provenance.csv`.
- Frozen legislative-output fixtures are under `data/external/legislative/`.
- Raw third-party archives remain outside git under `data/raw/calibration/` or another local path.
- `dist/calibration-source-refresh-manifest.json` is regenerated when raw sources are refreshed.
- Public repository and Dataverse identifiers are withheld in anonymous review materials.
- Full non-anonymous replication materials are prepared with `make replication-package` only for acceptance-stage deposit or non-blind review.

## External Review Gate

Before adding more realism layers, send `docs/external-methods-review-request.md` and the anonymous package to one methods-oriented reviewer. Ask them to focus on calibration guardrails, model identification, claim discipline, and whether any manuscript claim sounds more validated than the evidence supports.

Prepared materials are not evidence that they were sent or approved. Use `docs/expert-legal-coding-protocol.md` for the separate two-reader legal packet. Verify actual human returns, record disagreement and adjudication, and obtain the author's approval of declarations before journal submission. The existing AI review cannot satisfy either human gate.

The author should add any recoverable model/version identifiers to the AI-use declaration from actual session records. The package discloses that it does not retain a complete session-by-session version history; do not invent one or treat that disclosure as editorial acceptance.
