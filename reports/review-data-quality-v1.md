# Review data quality and evidence priorities

The frozen data pass row-shape, primary-key, decision-window, source-order join, and snapshot-date checks. These checks establish integrity of the stated sources; the substantive coverage gaps below remain open.

Petition snapshots: {'OT2023': '2026-07-24', 'OT2024': '2026-07-26'}. This report does not refresh case outcomes to the preparation date.

- Petition cohort: 7,716 certiorari rows; 7,716 require characteristics coding.
- CVSG first pass: 30 petitions. Legacy 'brief filed' values contain no recommendation direction.
- Pilot: 40 petitions, ten per term/payment stratum, selected by a fixed hash without using outcomes. The CVSG priority set is purposive; use the complete cohort or a documented probability sample for prevalence estimates.
- Environmental legal packet: 16 documents; zero completed human reviews. The selected sample is enriched for automated directional candidates and is not a population accuracy estimate.
- Public-text recovery queue: 76/191 documents. Missingness is nonrandom; do not impute treatment from snippets.
- Emergency evidence: 241 source order rows map to 227 distinct term/docket matters, including 30 granted matters. All remain queued for external observations.
- Historical Journal recovery: 4/4 failed rows match the later closed cohort. Frozen historical failures are preserved as provenance.

## Substantive petition coverage

A populated value such as other_or_uncoded or brief filed does not count as a substantive code. Merits rows use granted-for-argument petitions as a review denominator; pending, consolidated, DIG and missing outcomes need separate docket adjudication. CVSG recommendations use CVSG-requested petitions. All other fields use every certiorari petition.

| Term | Field | Substantive / eligible | Placeholder | Blank |
|---|---|---:|---:|---:|
| OT2023 | petitionerType | 9 / 4033 | 738 | 3286 |
| OT2023 | respondentType | 219 / 4033 | 528 | 3286 |
| OT2023 | lowerCourt | 4033 / 4033 | 0 | 0 |
| OT2023 | lowerCourtOrigin | 3711 / 4033 | 322 | 0 |
| OT2023 | issueArea | 0 / 4033 | 0 | 4033 |
| OT2023 | specialistCounselFlag | 0 / 4033 | 0 | 4033 |
| OT2023 | formerClerkCounselFlag | 0 / 4033 | 0 | 4033 |
| OT2023 | allegedSplitFlag | 0 / 4033 | 0 | 4033 |
| OT2023 | genuineSplitFlag | 0 / 4033 | 0 | 4033 |
| OT2023 | splitDepth | 0 / 4033 | 0 | 4033 |
| OT2023 | vehicleQualityObjection | 0 / 4033 | 0 | 4033 |
| OT2023 | sgRecommendation | 0 / 10 | 10 | 0 |
| OT2023 | meritsDecisionDate | 49 / 70 | 0 | 21 |
| OT2023 | meritsOutcome | 49 / 70 | 0 | 21 |
| OT2023 | reversalOrVacatur | 46 / 70 | 0 | 24 |
| OT2024 | petitionerType | 41 / 3683 | 3642 | 0 |
| OT2024 | respondentType | 1266 / 3683 | 2416 | 1 |
| OT2024 | lowerCourt | 3683 / 3683 | 0 | 0 |
| OT2024 | lowerCourtOrigin | 3391 / 3683 | 292 | 0 |
| OT2024 | issueArea | 0 / 3683 | 0 | 3683 |
| OT2024 | specialistCounselFlag | 0 / 3683 | 0 | 3683 |
| OT2024 | formerClerkCounselFlag | 0 / 3683 | 0 | 3683 |
| OT2024 | allegedSplitFlag | 0 / 3683 | 0 | 3683 |
| OT2024 | genuineSplitFlag | 0 / 3683 | 0 | 3683 |
| OT2024 | splitDepth | 0 / 3683 | 0 | 3683 |
| OT2024 | vehicleQualityObjection | 0 / 3683 | 0 | 3683 |
| OT2024 | sgRecommendation | 0 / 20 | 20 | 0 |
| OT2024 | meritsDecisionDate | 44 / 62 | 0 | 18 |
| OT2024 | meritsOutcome | 44 / 62 | 0 | 18 |
| OT2024 | reversalOrVacatur | 42 / 62 | 0 | 20 |

## Required human decisions

See docs/expert-legal-coding-protocol.md and docs/evidence-acquisition-priorities.md. Human legal classification, opportunity-denominator design, remedy fidelity and methods acceptance remain open. The independent AI review supplies no human signoff.

Reproduce with make expert-review-packet; inspect tools/prepare_expert_review.py or notebooks/review-data-quality.ipynb. Run make expert-review-check to detect stale outputs. Return files belong in ignored data/raw/expert-reviews/, never in generated templates.
