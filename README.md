# Supreme Court Simulator Design

This is the earlier Supreme Court and constitutional-review design workspace. Its current manuscript is titled "Emergency Review and Constitutional Court Design by Simulation" and uses Supreme Court emergency-review evidence as a calibration anchor for broader constitutional-court design comparisons. It remains distinct from the separate `Constitutional Review Simulator` repository unless the two projects are explicitly consolidated.

The project follows the campaign/scenario/report style of the adjacent congressional simulator while keeping the source tree independent.

The simulator evaluates court designs across generated constitutional cases and, optionally, imports legislative campaign outputs as docket inputs. Imported legislative metrics are summarized into a `LegislativeOutputProfile`, which affects case quality, rights risk, weak-mandate disputes, emergency pressure, and constitutional conflict.

## Requirements

- Java 21 or newer
- `make`

There are no external Java dependencies.

## Common Commands

Build:

```sh
make build
```

Run the default scenario comparison:

```sh
make run
```

Run tests:

```sh
make test
```

Build the paper:

```sh
make paper
```

This also regenerates the paper's LaTeX figure and table fragments from the current v2 campaign, verifies report manifests and substantive data invariants, checks claim-to-source traceability, exports standalone figure files, runs a local JLC-format check, and checks the final LaTeX log for unresolved references or citations.

Run stricter submission checks and build the non-anonymous title page:

```sh
make paper-strict-check
```

`make paper` always refreshes `paper/emergency-review-constitutional-court-design.pdf` after regenerating paper tables
and figures, and the paper targets now fail if the checked-in PDF is older than
the LaTeX inputs that feed it.

Build a clean replication archive for review or deposit:

```sh
make replication-package
```

Build a blinded review archive for anonymous journal submission:

```sh
make anonymous-submission-package
```

This writes `dist/constitutional-review-anonymous-submission.zip`, plus separate `dist/constitutional-review-anonymous-manuscript.zip` and `dist/constitutional-review-anonymous-supplement.zip` archives for journal upload categories. The package scan checks staged files for author-identifying local paths, repository URLs, and author strings. Use the full replication package for non-anonymous deposit or acceptance-stage handoff; use the anonymous manuscript/supplement packages for initial peer review.

Write the current v2 campaign artifacts:

```sh
make campaign
```

`make campaign` now writes the v2 paper campaign using the documented legislative-output import contract and the frozen fixture at `data/external/legislative/simulation-campaign-v21-paper.csv` by default. Override `PAPER_LEGISLATIVE_INPUT=/path/to/campaign.csv` to use a different legislative source, or set `PAPER_ARGS=` for a synthetic-only diagnostic run. The initial v0 and v1 campaigns remain available as `make campaign-v0` and `make campaign-v1`.

Run the diagnostic suite:

```sh
make diagnostics
```

The suite writes source-backed historical calibration guardrails, seed-robustness bands, parameter-sweep uncertainty bands, mechanism ablations, a focused adversarial-manipulation stress campaign, and a multi-family legislative-import comparison. Paper-facing diagnostic targets use `PAPER_ARGS` by default so regenerated reports match the manuscript manifests.

Run the parameter sweep only:

```sh
make parameter-sweep
```

Compare the import contract against multiple congressional-simulator report families:

```sh
make legislative-family-comparison
```

By default this reads the frozen family fixtures in `data/external/legislative/`. Set `LEGISLATIVE_FAMILY_DIR=/path/to/reports` to compare a different directory of legislative campaign CSVs.

Use a different normalized empirical calibration-data directory:

```sh
make calibrate CALIBRATION_DATA_DIR=/path/to/calibration
```

Refresh normalized calibration inputs from local raw-source downloads:

```sh
make raw-source-refresh
```

Place uncommitted raw archives under `data/raw/calibration/`, or pass explicit paths through `ARGS`, for example `make raw-source-refresh ARGS="--scdb-case-zip /path/to/SCDB.zip --shadow-zip /path/to/shadow.zip"`. The refresh writes a local manifest under `dist/` and keeps raw third-party archives out of git.

Import a legislative simulator report as input:

```sh
make campaign PAPER_LEGISLATIVE_INPUT="/path/to/congressional-simulator-campaign.csv"
```

## Current Design Surface

The catalog includes appointment method, court size, term limits, removal standards, recusal rules, emergency docket procedures, voting thresholds, concurrence/dissent behavior, panel versus en banc review, dual or cross-checking courts, constitutional councils, legislative override rules, and independence/accountability tradeoffs. Appointment methods now include a judicial-electorate design in which a configurable pool of judges votes on nominees drawn from a configurable eligibility pool.

The v1 campaign added docket subtypes, justice replacement/vacancy dynamics, richer emergency procedure states, stronger override outcomes, stress-case slices, and sensitivity cases for appointment capture, emergency pressure, rights risk, and weak democratic mandate.

The v2 campaign adds adversarial manipulation cases for appointment timing, emergency-application flooding, override evasion, recusal pressure, and court-expansion retaliation. It also splits legal stability into precedent stability, statutory stability, and interbranch compliance while keeping the blended legal-stability metric for headline comparisons.

The current diagnostics add normalized empirical calibration source tables, source-range appendix reports, legal-domain profiles for rights, election, executive-power, administrative, structural, and economic-regulation cases, review-path/admissibility filtering before merits review, pre-review settlement, and explicit strategic actor choices for formal legal response and practical implementation. Generated worlds now carry the filed universe directly into petition/admission filtering; there is no preliminary fixed-size top-case certiorari selection before admission. Judicial-electorate selector and nominee presets live in `data/design/judicial-electorate-pools.csv`; they are coding presets for design exploration, not empirical calibration targets.

The review-path model distinguishes certiorari, IFP certiorari, constitutional complaints, amparo, QPC-style filtered referral, abstract ex ante and ex post review, concrete referral, emergency applications, electoral review, and interbranch disputes. Cert-style intake now tracks petition type, court-requested response/CFR, CVSG request, SG signal, amicus intensity, lower-court split depth, genuine split status, lower-court ideological drift, lower-court resistance, split maturity, relists, claimant type, bar capital, claim strength, vehicle quality, specialist counsel, forum shopping, settlement pressure, strategic plaintiff selection, repeat-player advantage, vehicle defects, and conditional reversal probability.

Emergency applications are first-class objects with applicant/respondent type, application class, requested relief, response request, full-court referral, status-quo effect, public disagreement risk, and merits follow-through. Reports now separate the legacy CSV field `shadowDocketAbuse` from `emergencyLegitimacyRisk` and `emergencyDownstreamEffect`; paper-facing text describes that legacy field as `emergencyProcessIrregularity` to avoid treating the constructed index as a legal conclusion. The reports also expose `emergencyOpportunism`.

The repeated-case state now includes repeat-player learning, emergency-incentive learning, and compliance learning. These synthetic channels update across decisions and then affect later emergency routing, settlement, forum shopping, noncompliance, and conflict. Reported learning metrics are derived diagnostics, not empirical validation claims.

The headline metrics are legal stability, rights protection, partisan alignment, emergency-process irregularity, legitimacy, reversal rate, constitutional-conflict index, and democratic responsiveness. Direct outputs such as rights-claimant success, domain-specific claimant success, doctrinal depth, remedial breadth, fragmentation, lower-court compliance, precedent durability, government noncompliance, recusal incentive pressure, emergency downstream effects, elite acceptance, and the modeled public-legitimacy proxy are kept separate from derived directional indices. Pipeline diagnostics including lower-court resistance, forum shopping, enforcement capacity, and emergency opportunism are reported as scenario-mediated values rather than raw filed-world constants.

## Current Reports

- `reports/constitutional-review-campaign-v2.csv` and `.md`: full v2 campaign.
- `reports/calibration-baseline.csv` and `.md`: empirical calibration guardrails computed from normalized source observations.
- `reports/calibration-source-ranges-v4.csv` and `.md`: generated appendix of source ranges by metric.
- `reports/seed-robustness-v2.csv` and `.md`: weighted v2 campaign sensitivity across deterministic seed offsets.
- `reports/mechanism-ablation-v2.csv` and `.md`: pairwise institutional mechanism comparisons.
- `reports/manipulation-stress-v2.csv` and `.md`: focused adversarial stress campaign.
- `reports/parameter-sweep-v4.csv` and `.md`: uncertainty bands from named prior profiles, not only random seeds.
- `reports/parameter-sweep-drivers-v4.csv` and `.md`: top close-score clusters by named prior, with interpretation caveats.
- `reports/prior-uncertainty-v1.csv` and `.md`: sampled-prior uncertainty bands over weak assumptions.
- `reports/pathway-validation-dashboard-v1.csv` and `.md`: pathway-specific denominator audit that keeps certiorari, emergency, complaint/referral, compliance, and override/remand denominators separate and distinguishes source-row labels from manuscript-use labels.
- `reports/metric-semantics-v1.csv` and `.md`: metric semantics audit that separates empirical source checks, synthetic outputs, and score-reading aids by denominator or scale.
- `reports/benchmark-readiness-v1.csv` and `.md`: benchmark/back-test work queue generated from the denominator audit, showing which source extractions are needed before stronger validation language would be justified.
- `reports/benchmark-extraction-protocol-v1.csv` and `.md`: emergency-application and certiorari-cohort extraction protocol generated from `data/benchmarks/`, defining the fields needed to close the top emergency and certiorari benchmark gaps.
- `reports/benchmark-extraction-workqueue-v1.csv` and `.md`: generated emergency benchmark coding queue that converts the protocol into term/source tasks and reconciliation evidence.
- `reports/certiorari-extraction-workqueue-v1.csv` and `.md`: generated certiorari coding queue for petition-denominator, response/CFR, CVSG, elite-counsel/amicus, and split-quality source slices.
- `reports/emergency-application-order-reconciliation-v1.csv` and `.md`: application-level Shadow Docket Database v3.0 OT2023-OT2024 denominator, grant, and public-disagreement reconciliation for the compact emergency extract.
- `reports/emergency-application-grant-linkage-workqueue-v1.md`: generated merits-follow-through/status-quo/downstream coding queue for the 31 granted rows in the compact emergency extract.
- `reports/emergency-application-denied-linkage-workqueue-v1.md`: generated all-application closure queue for the 200 denied rows and 10 non-binary/NA rows, now complemented by the official-docket coded denied/NA benchmark for docket-visible linkage fields.
- `reports/emergency-application-linkage-coded-v1.md`: official-docket coded benchmark for all 31 granted source-record rows from the emergency linkage queue, representing 30 unique emergency matters across OT2023 and OT2024.
- `reports/emergency-application-denied-linkage-coded-summary-v1.csv` and `.md`: official-docket coded summary for all 210 denied/non-binary source-record rows, supporting bounded all-application emergency docket-linkage evidence but not external implementation validation.
- `reports/emergency-application-field-readiness-v1.csv` and `.md`: field-level audit of the emergency linkage schema, separating 241-row all-application extract fields, all-application official-docket linkage fields, conditionally complete linked-merits fields, and the remaining external-implementation evidence boundary.
- `reports/certiorari-term-flow-reconciliation-v1.csv` and `.md`: official-source reconciliation for the compact OT2023 Journal paid/IFP term-flow and plenary-review extract used by the first certiorari queue slice.
- `reports/certiorari-docketed-cohort-summary-v1.csv` and `.md`: exact summary of the independently enumerated 4,222-docket OT2023 paid/IFP cohort and its 4,033 docketed certiorari petitions.
- `reports/certiorari-docketed-cohort-summary-ot2024-v1.csv` and `.md`: exact summary of the 3,854-docket OT2024 Journal-count snapshot cohort, its 3,683 certiorari petitions, and three still-pending outcomes.
- `reports/certiorari-multi-term-benchmark-v1.csv` and `.md`: generated OT2023–OT2024 comparison and denominator-weighted pooled rates for paid intake, CFR, CVSG, cert-stage amici, relists, and resolved grant/GVR outcomes.
- `reports/certiorari-docketed-cohort-journal-reconciliation-v1.csv` and `.md`: row-level current-docket comparison to the older Journal disposition extract, with Journal absence kept separate from outcome disagreement.
- `reports/certiorari-cohort-field-readiness-v1.csv` and `.md`: field-level audit separating complete docket-visible cohort fields, partial petitioner/respondent and merits fields, and uncoded issue, counsel, split-quality, and vehicle-quality fields.
- `reports/certiorari-cohort-closure-plan-v1.csv` and `.md`: source-slice plan marking the docketed-intake/CFR/CVSG gate met while retaining explicit boundaries for undocketed submissions and uncoded counsel, issue, split, vehicle, and partial merits fields.
- `reports/lower-court-precedent-treatment-summary-v1.csv` and `.md`: checksum-reconciled aggregate Shepard's treatment summary for 876 Supreme Court precedents, including 223 constitutional-issue precedents, bounded to doctrinal uptake rather than practical compliance.
- `reports/environmental-implementation-cohort-summary-v1.csv` and `.md`: five-decision environmental cohort summary reconciling 191 published federal citing-opinion documents, 65 nationwide-applicability/published-citation-presence cells, nonrandom public-text coverage, automated treatment candidates pending expert review, and five practical agency-response episodes.
- `reports/environmental-full-text-availability-audit-v1.csv` and `.md`: missingness audit by decision, court, year, opinion-document type, and retrieval reason.
- `reports/external-methods-review-ai-v1.md` and `reports/external-methods-review-response-v1.md`: disclosed independent AI methods review and severity-ranked response matrix; these are not human peer review.
- `reports/implementation-compliance-closure-plan-v1.csv` and `.md`: source-slice plan distinguishing bounded acquisition snapshots from remaining expert-coding, relevant-case opportunity, remedy-fidelity, broader noncompliance, and emergency downstream work.
- `reports/implementation-compliance-workqueue-v1.csv` and `.md`: generated coding queue that preserves those bounded source uses while identifying the broader post-judgment opportunity, remedy, implementation-outcome, and downstream observations still needed.
- `reports/ecthr-execution-monitoring-summary-v1.csv` and `.md`: summary of the generated HUDOC-EXEC pending leading-case monitoring extract, bounded to ECtHR execution-supervision monitoring capacity.
- `reports/certiorari-journal-disposition-summary-v1.csv` and `.md`: row-level OT2023 Journal certiorari disposition seed summary, explicitly framed as disposition evidence rather than a closed filed-petition cohort.
- `reports/certiorari-journal-docket-detail-summary-v1.csv` and `.md`: near-complete official-docket join for 3,947 of 3,951 OT2023 Journal disposition rows, with 4 remaining failed static-page fetches preserved as a coverage limitation.
- `reports/certiorari-journal-docket-retrieval-workqueue-v1.csv` and `.md`: row-level retry/manual-retrieval queue for the 4 OT2023 Journal disposition rows whose official static docket pages still failed during the refreshed docket-detail pass.
- `reports/certiorari-granted-docket-detail-summary-v1.csv` and `.md`: official-docket join for the OT2023 Journal granted/GVR certiorari rows, bounded to granted/GVR docket-detail checks rather than closed petition-cohort validation.
- `reports/primary-source-coverage-v1.csv` and `.md`: coverage summary showing which pathway rows are raw/primary-source-backed, synthesis-backed, proxy/design-prior, or missing.
- `reports/legislative-family-comparison-v3.csv` and `.md`: constitutional-review results across multiple congressional-simulator campaign families.

## Calibration Data

Normalized empirical source observations live in `data/calibration/`; row-level source handling is summarized in `data/calibration/provenance-manifest.csv`. Benchmark extracts and scaffolds live in `data/benchmarks/`. The primary certiorari evidence is now the paired OT2023 and OT2024 docketed cohorts: 8,076 paid/IFP public dockets, including 7,716 certiorari petitions. OT2023 contributes 4,222 dockets and 4,033 certiorari petitions; the OT2024 Journal-count snapshot contributes 3,854 dockets and 3,683 certiorari petitions, of which three remain pending or held as of July 26, 2026. The cohorts directly supply term-specific paid and IFP CFR rates, petition-level CVSG rates, cert-stage amicus presence, relist presence, and resolved grant/GVR outcomes. Their boundary remains explicit: docketed intake only, not undocketed submissions or constitutional-review-only petitions, with issue area, specialist/former-clerk counsel, split quality, and vehicle quality uncoded and several merits fields partial. The OT2024 manifest also records four same-cutoff-date public dockets above the Journal count-defined ranges as explicit snapshot exclusions.

The lower-court evidence now includes a checksum-reconciled public replication extract for 876 formally argued 1995--2004 Supreme Court precedents, with aggregate lower-court responses accumulated through 2016. Across all precedents, 235,256 followed treatments and 38,297 adverse or distinguished treatments imply an 86.0% followed share among directional treatments; the 223 source-flagged constitutional-issue precedents yield 47,370 followed and 17,753 adverse treatments, or 72.7%. These are direct aggregate doctrinal-uptake observations, but they are citation/treatment-selected and citation-weighted, omit exposed but non-citing or ignored cases, and do not measure remedy fidelity or practical implementation. They therefore remain proxy context for the synthetic case-average `lowerCourtCompliance` score.

The environmental cohort adds a distinct descriptive event layer: 191 deduplicated published CourtListener-linked federal citing-opinion documents filed during five decision-specific 730-day windows and 65 nationwide-applicability/published-citation-presence cells. Public full text and source-decision context are available for 115 documents, with nonrandom missingness across decisions and opinion-document types. Conservative target-linked rules produce five applied candidates and one distinguished candidate, 109 citation-only rows, and 76 unclear rows; every directional candidate remains pending expert legal review. Zero-citation cells mean no observed published citation, not empirical exposure, ignored precedent, or noncompliance. A separate five-episode practical layer preserves Gurganus's published four compliant and one narrowly compliant classifications and joins them to verified official agency or Federal Register actions. The 4/5 and 1/5 values describe purposive case-study composition, not compliance probabilities. Neither layer is a behavioral guardrail or denominator-matched validation target for general lower-court or government compliance.

The older Journal disposition, Journal public-docket, and granted/GVR joins remain in the repository as independent reconciliation slices. The Journal public-docket extract still records 4 failed static-page fetches, but those failures no longer leave the separately enumerated docketed-intake cohort open. Emergency extracts support bounded all-application docket-linkage claims, while external emergency implementation evidence remains missing. The HUDOC-EXEC extract supports monitoring-capacity language, not practical compliance or government-noncompliance claims.

Regenerate normalized calibration rows from raw SCDB and shadow-docket archives with `make raw-source-refresh` or `tools/build_calibration_tables.py`; raw archives are intentionally not committed. Refresh the official term cohorts with `make certiorari-docketed-cohorts`, or use the term-specific targets. Refresh and checksum-reconcile the Harvard Dataverse precedent-treatment release with `make lower-court-precedent-benchmark`; rebuild the environmental cohort with `make environmental-implementation-cohort`. Its ignored raw cache can be packaged separately with `make environmental-source-snapshot`; the main replication archive reproduces downstream analysis from frozen normalized outputs and does not claim to reproduce network acquisition by itself.

## External Legislative Fixtures

Frozen legislative-output fixtures live in `data/external/legislative/` with provenance in `data/external/legislative/source-provenance.csv`. These CSVs are imported as data only; this project does not depend on the Congress simulator source tree.

## Paper

The LaTeX manuscript lives at `paper/emergency-review-constitutional-court-design.tex`. It is intentionally framed as a model-and-design paper, not a claim that the specified mechanisms are empirically validated.

The current venue target is Journal of Law and Courts, with CELS 2026 as the near-term conference target. The manuscript is anonymous by default, uses the Cambridge/JLC `cup-journal` template path with `journal=jlc` when the official class is available, and otherwise builds locally as an author-date review copy. `make paper-jlc-template-check` is available for an official-template environment and intentionally fails on TeX installations that do not provide `cup-journal.cls`. Submission-prep notes live in `docs/submission-readiness.md`; reproduction notes live in `REPLICATION.md`.

The paper now centers the emergency-review claim and includes generated figures for domain-specific claimant success, process-legitimacy/conflict tradeoffs, and emergency-review profiles, plus generated selected-results, emergency-walkthrough, mechanical-versus-diagnostic, multi-objective score, litigation-pipeline diagnostics, calibration, calibration-classification, pathway denominator, metric-semantics, benchmark-readiness, sensitivity-driver, uncertainty, and mechanism-level contrast tables. `make paper-figure-files` exports standalone PDF/PNG figure files for journal production. `paper/source-audit.csv` maps material claims to source-code, report, data, manuscript, or literature anchors. Venue-fit notes also explain why JLC is preferred over the ACM route used by the adjacent Congress Institutional Simulator.

Use `make replication-check` before submission. It rebuilds tests, campaigns, diagnostics, validation dashboards, the strict paper checks, and the replication/submission packages, then verifies a clean copied source tree can run the core replication workflow.

Use `docs/jlc-submission-checklist.md` as the final pre-submission checklist.
