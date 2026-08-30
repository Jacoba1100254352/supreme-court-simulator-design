# Submission Readiness

## Primary Target

Primary journal target: Journal of Law and Courts.

Reason: its scope explicitly fits judicial institutions, judicial independence, court selection, and theoretical or empirical work on law and courts. The manuscript is now framed as computational institutional design for judicial politics rather than as a software-platform overview.

Current manuscript posture:

- `paper/emergency-review-constitutional-court-design.tex` is anonymous by default.
- The paper inventory contains one primary manuscript. `paper/abstract-variants.md` and `paper/title-page.tex` are submission companions, not separate subpapers; no standalone breakoff manuscript currently requires an independent publication gate.
- The source attempts to use the official Cambridge `cup-journal` template with `journal=jlc` when `cup-journal.cls` is available.
- The local build falls back to an article review copy with author-date citations because the local TeX Live Basic installation does not ship Cambridge's class or `biber`.
- `make paper-jlc-template-check` is the official-template gate; it should pass in Overleaf or another TeX environment that provides `cup-journal.cls` and should fail locally when the class is unavailable.
- Citations are author-date in the local build and are ready for the official template's Chicago author-date pipeline when compiled in the Cambridge/Overleaf environment.
- Figures are appropriate for this target. JLC's author instructions ask authors to place tables and figures in the manuscript near first reference rather than collecting them at the end. The current manuscript follows that practice with generated campaign figures.
- `make paper-check` now verifies the local manuscript against the JLC-facing requirements that can be checked automatically: anonymous review mode, JLC template options, hidden hyperlink borders, author-date fallback, declaration sections, figure and table descriptions, figure references in text, data availability before references, generated selected-results/calibration/uncertainty/mechanism tables, source-audit coverage, source-provenance manifests, a mechanics appendix, report-manifest consistency, and the 10,000-word article ceiling.
- `make paper-strict-check` builds the manuscript and non-anonymous title page, then reruns the strict JLC and source-audit checks.
- `make replication-package` creates a clean archive under `dist/` with source code, tests, normalized data, frozen legislative-output fixtures, generated reports, paper source, generated figure/table fragments, standalone figure files, source-provenance manifests, the source audit, and a manifest.
- The calibration section now reports both a checksum-reconciled aggregate doctrinal-uptake benchmark for 876 Supreme Court precedents and a separate five-decision environmental snapshot with 191 published citing-opinion documents, 65 nationwide-applicability/published-citation-presence cells, and five practical implementation episodes. It exposes nonrandom full-text missingness, labels six directional values as automated candidates pending expert review, and withholds behavioral or general compliance validation claims.
- The manuscript includes a non-identifying AI assistance statement because the project used ChatGPT/Codex and Deep Research synthesis during research, implementation, drafting, formatting, and local verification. The statement now identifies the tool family, dates, access route, use categories, author responsibility, and treatment of AI-assisted research output.

## Why JLC Instead of ACM

The adjacent Congress Institutional Simulator uses ACM format because that paper is framed as a computational framework for collective decision-making, compromise, productivity, agenda control, and voting-system design. That framing fits an ACM-style computational social systems / collective intelligence audience and the `acmart` template's computing metadata expectations.

This paper is different. Its central claims are about judicial institutions: constitutional-review access paths, emergency orders, appointment and tenure rules, recusal, voting thresholds, constitutional conflict, legal stability, rights protection, and public legitimacy. Those claims need reviewers who can evaluate law-and-courts theory, comparative constitutional design, judicial-politics framing, and empirical/legal replication expectations.

Practical differences:

- JLC is the stronger substantive home because it is specifically a law-and-courts journal and publishes interdisciplinary work for the law-and-courts community. See the [JLC author instructions](https://www.cambridge.org/core/journals/journal-of-law-and-courts/information/author-instructions/preparing-your-materials).
- JLC's instructions support Word, PDF, or LaTeX review files, anonymous submission, author-date citation, data-availability language, and replication materials through JLC Dataverse at acceptance.
- ACM would be plausible only if the paper were reframed around the simulator as a computing contribution: model architecture, human-centered decision support, collective intelligence, simulation methodology, or software/tooling. That would risk making the constitutional-review substance look like an application case rather than the paper's core contribution.
- ACM production is also stricter about `acmart`, CCS concepts, TAPS compatibility, figure descriptions, and approved LaTeX packages. See ACM's [LaTeX preparation instructions](https://authors.acm.org/proceedings/production-information/preparing-your-article-with-latex). That is manageable, as the Congress paper shows, but it adds constraints without improving venue fit for a judicial-politics manuscript.

Bottom line: keep JLC as the primary journal target and CELS as the near-term feedback venue. Revisit ACM only if the paper is rewritten into a general computational institutional-design methods paper rather than a court-design paper.

## Conference Feedback Posture

The CELS 2026 paper deadline was June 22, 2026 and has passed. Do not delay the JLC path for that cycle. Use the external methods-review packet as the immediate feedback route, then monitor the next CELS call or another law-and-courts workshop after the manuscript has absorbed that review.

Before journal submission, prioritize:

- Tighten the main calibration/validation section.
- Use the generated benchmark-readiness display to decide the first benchmark/back-test extraction.
- Keep the framing empirical: observed inputs, coded rules, assumptions, simulated outputs.

## Files Added for Submission Preparation

- `paper/title-page.tex`: separate non-anonymous title-page skeleton.
- `paper/abstract-variants.md`: CELS, ICON-S, and APSA abstract/proposal variants.
- `REPLICATION.md`: one-command reproduction plan and observed/coded/assumed/simulated memo.
- `paper/scripts/check_jlc_format.py`: local JLC requirement checker.
- `paper/scripts/check_source_audit.py`: structural claim/source traceability checker; substantive row counts, hashes, and cohort semantics are checked by `verify_paper_artifacts.py`.
- `paper/scripts/verify_paper_artifacts.py`: manifest and hash consistency check for paper reports.
- `paper/scripts/export_figures.py`: standalone figure export builder for journal-production handoff.
- `paper/source-audit.csv`: claim-level source, code, data, and report anchor inventory.
- `reports/benchmark-readiness-v1.csv`: generated benchmark/back-test work queue derived from the pathway denominator audit.
- `reports/benchmark-extraction-protocol-v1.csv`: generated emergency-application and certiorari-cohort protocol for closing the top benchmark gaps.
- `reports/benchmark-extraction-workqueue-v1.csv`: generated emergency benchmark coding queue with term/source reconciliation tasks.
- `reports/certiorari-extraction-workqueue-v1.csv`: generated certiorari benchmark coding queue with petition-denominator, CFR/response, CVSG, elite-counsel/amicus, and split-quality tasks.
- `reports/emergency-application-order-reconciliation-v1.csv`: generated reconciliation for the compact OT2023-OT2024 Shadow Docket Database v3.0 emergency-application extract.
- `reports/emergency-application-grant-linkage-workqueue-v1.md`: generated summary of the 31 granted emergency-application rows that need merits-follow-through, status-quo, and downstream-policy coding.
- `reports/emergency-application-denied-linkage-workqueue-v1.md`: generated all-application closure queue for 200 denied and 10 non-binary/NA emergency-application rows used by the official-docket coded denied/NA benchmark.
- `reports/emergency-application-linkage-coded-v1.md`: official-docket coded benchmark for all 31 granted source-record rows from the emergency linkage queue, representing 30 unique emergency matters across OT2023 and OT2024.
- `reports/emergency-application-denied-linkage-coded-summary-v1.csv`: generated summary of the official-docket coded 210-row denied/NA emergency benchmark, bounded to all-application docket-linkage evidence and not external implementation validation.
- `reports/emergency-application-field-readiness-v1.csv`: generated field-level audit showing which emergency-linkage fields are covered by the 241-row all-application extract, which are now all-application official-docket linkage fields, which linked-merits fields are conditionally complete through a linked value or explicit no-link/pending category, and which still require external implementation evidence.
- `reports/certiorari-term-flow-reconciliation-v1.csv`: generated official-source reconciliation for the compact OT2023 Journal certiorari term-flow extract.
- `reports/certiorari-docketed-cohort-summary-v1.csv`: generated exact-count summary of the closed 4,222-docket OT2023 paid/IFP cohort and its 4,033 certiorari petitions.
- `reports/certiorari-docketed-cohort-summary-ot2024-v1.csv`: generated exact-count summary of the 3,854-docket OT2024 Journal-count snapshot cohort, its 3,683 certiorari petitions, and three retained pending outcomes.
- `reports/certiorari-multi-term-benchmark-v1.csv`: generated OT2023-OT2024 comparison with term-specific numerators and denominators, percentage-point changes, and denominator-weighted pooled descriptions.
- `reports/certiorari-docketed-cohort-journal-reconciliation-v1.csv`: row-level comparison of current official-docket outcomes to the older Journal disposition slice.
- `reports/certiorari-cohort-field-readiness-v1.csv`: generated field-level audit separating complete docket-visible cohort fields, partial petitioner/respondent and merits fields, and uncoded issue, counsel, split, and vehicle-quality fields.
- `reports/certiorari-cohort-closure-plan-v1.csv`: generated source-slice plan marking the docketed-intake/CFR/CVSG gate met while retaining the undocketed-submission, counsel, issue, split, vehicle, and partial-merits boundaries.
- `reports/implementation-compliance-closure-plan-v1.csv`: generated source-slice closure plan for lower-court uptake, implementation resistance, monitoring capacity, government noncompliance, and emergency downstream implementation evidence.
- `reports/implementation-compliance-workqueue-v1.csv`: generated schema-driven coding queue for lower-court treatment, implementation/resistance, monitoring, and emergency downstream source slices.
- `reports/lower-court-precedent-treatment-summary-v1.csv`: generated aggregate-treatment reconciliation for 876 precedents, 861 published main-model rows, and 223 source-flagged constitutional-issue precedents.
- `reports/environmental-implementation-cohort-summary-v1.csv`: generated reconciliation for 191 deduplicated published citing-opinion events, 65 nationwide-applicability/citation-presence cells, public-text/context coverage, automated treatment candidates, and five practical agency episodes.
- `reports/environmental-full-text-availability-audit-v1.csv`: missingness by decision, court, filing year, opinion-document type, and recorded retrieval reason.
- `reports/external-methods-review-ai-v1.md` and `reports/external-methods-review-response-v1.md`: independent AI review and response record, explicitly distinguished from human peer review.
- `reports/ecthr-execution-monitoring-summary-v1.csv`: generated summary of the HUDOC-EXEC pending leading-case monitoring-capacity extract.
- `reports/certiorari-journal-disposition-summary-v1.csv`: generated summary of the OT2023 Journal certiorari disposition seed and its not-closed-cohort boundary.
- `reports/certiorari-journal-docket-detail-summary-v1.csv`: generated summary of the 3,947-row official-docket join for OT2023 Journal disposition rows and its 4-row remaining static-page coverage gap.
- `reports/certiorari-journal-docket-retrieval-workqueue-v1.csv`: generated retry/manual-retrieval queue for the 4 OT2023 Journal disposition rows whose official static docket pages still failed during the refreshed docket-detail pass.
- `reports/certiorari-granted-docket-detail-summary-v1.csv`: generated summary of the official-docket granted/GVR certiorari detail slice and its not-closed-cohort boundary.
- `data/benchmarks/emergency-application-order-extract-shadow-docket-v3-0.csv`: compact row-level emergency denominator, grant, and public-disagreement source slice.
- `data/benchmarks/emergency-application-grant-linkage-workqueue-v1.csv`: prefilled granted-emergency coding sheet with source identifiers and uncoded linkage fields.
- `data/benchmarks/emergency-application-denied-linkage-workqueue-v1.csv`: prefilled denied/non-binary emergency coding sheet with source identifiers and uncoded linkage fields.
- `data/benchmarks/emergency-application-linkage-coded-v1.csv`: official-docket coded OT2023-OT2024 granted-emergency benchmark.
- `data/benchmarks/emergency-application-denied-linkage-coded-v1.csv`: official-docket coded denied/non-binary emergency benchmark covering the 210-row denied/NA closure queue.
- `data/benchmarks/implementation-compliance-schema.csv`: row-level schema for post-judgment implementation and compliance benchmark coding.
- `data/benchmarks/implementation-compliance-template.csv`: generated blank coding template whose columns come from the implementation/compliance schema.
- `data/benchmarks/lower-court-precedent-treatment-aggregate-v1.csv`: checksum-reconciled public replication extract with aggregate cited-only, followed, adverse, and distinguished lower-court treatment counts through 2016.
- `data/benchmarks/lower-court-precedent-treatment-aggregate-v1-manifest.json`: source-version, license, checksum, row-count, term-count, aggregate-count, and output-hash provenance for that extract.
- `data/benchmarks/lower-court-environmental-treatment-events-v1.csv`: five-decision published CourtListener-linked event corpus with stable provider-cluster provenance, citing-case fields, retained snippets and contexts, missingness reasons, and automated treatment candidates pending expert review.
- `data/benchmarks/lower-court-environmental-circuit-exposure-v1.csv`: 65 nationwide-applicability/published-citation-presence cells whose zeroes are not empirical exposure, ignored precedent, or noncompliance.
- `data/benchmarks/environmental-practical-implementation-events-v1.csv`: five published environmental agency-response classifications joined to verified official implementation actions.
- `data/benchmarks/environmental-directional-treatment-review-queue-v1.csv`: six directional candidates plus a deterministic ten-row citation-only sample, all explicitly pending expert review.
- `data/benchmarks/gurganus-2025-table-1-classifications-v1.csv`: structured classification transcription with article locators and record hashes.
- `data/benchmarks/environmental-implementation-cohort-v1-manifest.json`: source-query, deduplication, source-document, classification, denominator, limitation, count, and output-hash provenance for both cohort layers.
- `data/benchmarks/ecthr-execution-monitoring-pending-leading-cases-v1.csv`: schema-shaped HUDOC-EXEC snapshot of English pending leading cases under Committee of Ministers execution supervision, bounded to monitoring-capacity evidence.
- `data/benchmarks/certiorari-term-flow-extract-journal-ot2023.csv`: compact official Journal term-flow source slice for paid/IFP docketed cases, plenary-review counts, and related statistics.
- `data/benchmarks/certiorari-term-flow-extract-journal-ot2024.csv`: compact official Journal OT2024 term-flow source slice with all 22 parsed opening-statistics rows.
- `data/benchmarks/certiorari-docketed-cohort-ot2023.csv`: closed official-docket cohort containing all 4,222 OT2023 paid/IFP dockets and 4,033 docketed certiorari petitions.
- `data/benchmarks/certiorari-docketed-cohort-ot2024.csv`: closed Journal-count snapshot cohort containing 3,854 OT2024 paid/IFP dockets and 3,683 docketed certiorari petitions.
- `data/calibration/scotus-certiorari-docketed-cohort-ot2023.csv`: normalized paid/IFP, CFR, CVSG, amicus, relist, and grant/GVR observations derived from the closed cohort.
- `data/calibration/scotus-certiorari-docketed-cohort-ot2024.csv`: matching OT2024 observations, with the grant/GVR rate limited to 3,680 resolved petitions.
- `data/calibration/lower-court-precedent-treatment-v1.csv`: 60 term-pooled doctrinal-uptake context rows, explicitly scale-mismatched to the simulator's case-average compliance score.
- `data/calibration/environmental-implementation-cohort-v1.csv`: decision-level data-quality checks and descriptive case-study summaries; no environmental row is a behavioral guardrail.
- `data/benchmarks/certiorari-journal-disposition-extract-ot2023.csv`: row-level official Journal certiorari disposition seed with docket, disposition, source-record, and manual-review counts surfaced when parser classification leaves any rows unresolved.
- `data/benchmarks/certiorari-journal-docket-detail-ot2023.csv`: official Supreme Court docket-page join for 3,947 of 3,951 OT2023 Journal disposition rows, preserving 4 remaining failed static-page fetches as a coverage limitation rather than a closed filed-petition cohort.
- `data/benchmarks/certiorari-granted-docket-detail-ot2023.csv`: official Supreme Court docket-page join for 115 OT2023 Journal granted/GVR rows, bounded to petition filing, response/CFR, CVSG, argument, and merits-outcome detail for that slice.
- `data/benchmarks/emergency-application-linkage-template.csv`: generated blank row-level coding template whose columns come from the linkage schema.
- `data/benchmarks/certiorari-cohort-template.csv`: generated blank row-level coding template whose columns come from the certiorari cohort schema.
- `data/calibration/provenance-manifest.csv`: row-family provenance for normalized calibration sources.
- `data/external/legislative/source-provenance.csv`: fixture hashes and provenance for imported legislative outputs.
- `docs/external-methods-review-request.md`: critical review packet and draft reviewer email.
- `docs/jlc-submission-checklist.md`: pre-submission sequence and upload checklist for JLC/CELS.
- `tools/create_replication_package.py`: archive builder for review/deposit packages.
- `tools/create_anonymous_submission_package.py`: blinded review package builder with an identifier scan.
- `tools/refresh_calibration_sources.py`: raw-source wrapper for regenerating normalized calibration inputs from local downloads.

## Remaining No-Regrets Work

- Run `make raw-source-refresh` after downloading fresh raw SCDB and shadow-docket archives before final Dataverse deposit.
- The paired OT2023-OT2024 official-docket cohorts now close the high-priority recent-term certiorari denominator, CFR, and CVSG incidence slice. The project remains a design-search submission because other pathway and field-level validation gaps remain.
- Use `reports/benchmark-extraction-protocol-v1.md` to select the next still-open source slice; do not upgrade claims beyond the field-level completion rule. The strongest next certiorari slices are issue, counsel, split/vehicle quality, respondent/SG-response detail, and an additional mature term.
- Use `reports/benchmark-extraction-workqueue-v1.md` and the emergency readiness materials to keep the emergency denominator auditable. The docket-visible all-application fields are closed for the compact OT2023-OT2024 slice; external emergency implementation/downstream policy observations remain open. Lower-court and agency evidence now has bounded environmental source slices, but relevant-case opportunity, remedy fidelity, representative decision/agency coverage, and noncompliant outcomes remain open.
- Treat the two term summaries and `reports/certiorari-multi-term-benchmark-v1.md` as the publication sources for bounded OT2023-OT2024 docketed-intake, CFR, CVSG, amicus-presence, relist, and grant/GVR descriptions. Together the cohorts contain 8,076 paid/IFP dockets and 7,716 certiorari petitions. Keep the three OT2024 pending outcomes and four same-cutoff-date dockets above the Journal count-defined ranges explicit; the grant/GVR denominator uses 3,680 resolved OT2024 petitions.
- Use `reports/certiorari-cohort-field-readiness-v1.md` and `reports/certiorari-cohort-closure-plan-v1.md` to drive the next certiorari work toward respondent classification, issue area, specialist/former-clerk counsel, alleged and genuine split quality, vehicle quality, and partial merits follow-through. Preserve the separate limits that the cohort excludes undocketed submissions and is not constitutional-review-only. The older Journal artifacts remain reconciliation slices, not the denominator source.
- Aggregate lower-court doctrinal uptake, descriptive environmental published-citation presence, purposive environmental practical implementation, and monitoring capacity now have bounded source slices. Continue using `reports/implementation-compliance-closure-plan-v1.md`, `reports/implementation-compliance-workqueue-v1.md`, and `data/benchmarks/implementation-compliance-template.csv` to complete expert coding and acquire relevant-case opportunity, remedy fidelity, broader agency and decision coverage including noncompliant outcomes, and external emergency downstream observations before upgrading general compliance claims.
- Use `make anonymous-submission-package` for initial peer review, uploading `constitutional-review-anonymous-manuscript.zip` and `constitutional-review-anonymous-supplement.zip` separately when the portal supports separate categories; prepare a blinded repository or Dataverse placeholder only if the submission system requires a live URL before public release.
- Decide whether I-CON remains a possible future target before posting a public preprint.
- Get one external methods review using `docs/external-methods-review-request.md` before adding more realism layers.
