# Evidence acquisition priorities for human review

The immediate deliverable is a reviewable synthetic design-search paper with reproducible evidence boundaries. The source snapshots remain dated in their manifests; preparing this packet does not refresh them. The numerical coverage and case lists below are generated in `reports/review-data-quality-v1.md` and the companion CSV queues.

## 1. Read the invited SG briefs and define petition coding

Start with all 30 CVSG-requested certiorari petitions across OT2023 and OT2024 (10 and 20 respectively). The 31st CVSG row in the complete docket inventory is not a certiorari petition. Existing `sgRecommendation` entries say only `brief filed`. Read the invited brief and retain recommendation (grant, deny, GVR, hold, mixed or unclear), date, supporting page, represented side and the official document URL. Preserve a separate filing-presence variable. A brief can recommend different treatment for separate questions; retain the distinction rather than forcing a binary value.

Next use the fixed 40-petition pilot: ten paid and ten IFP petitions per term, selected by a reproducible hash without using grant or denial. `reports/petition-characteristics-priority-queue-v1.csv` preserves all 7,716 petitions and marks pilot membership. Complete the pilot's issue, actor and representation fields before expanding to the remainder. Reading only grants or elite counsel would not support whole-cohort prevalence estimates. The CVSG set is a purposive work priority; it is not a representative sampling stratum by itself.

For each petition retain the question presented, constitutional/statutory/mixed issue classification, legal domain, petitioner and respondent categories, court of origin, counsel's name and represented side, dated evidence for specialist/former-clerk status, an alleged conflict, independent assessment of the conflict and circuits implicated, and any vehicle objection. Read the petition, opposition and relevant lower-court opinions before coding genuine split or vehicle quality. Ask the legal reviewer to approve the specialist definition and conflict codebook before broad coding. Unclear or unavailable is distinct from no.

Record each feature's information-availability date. Prediction or retrospective back-testing must not use a merits outcome, eventual SG position, later counsel biography or post-disposition knowledge as an earlier intake feature. Keep observed association and model mechanism comparison distinct from a causal reform effect. Prespecify a case-level training/holdout split before fitting; linked petitions and the same controversy must stay in one partition.

The merits-field queue uses granted-for-argument petitions. Resolve consolidated cases, DIGs, pending cases, partial dispositions and linked merits dockets before calculating a merits-outcome rate. A blank reversal flag is not an affirmance. Preserve the three pending OT2024 outcomes as of the July 26 snapshot until a separately documented refresh.

## 2. Acquire external emergency implementation records

`reports/emergency-implementation-priority-queue-v1.csv` groups every source order row into a term/docket matter and preserves the original events in `orderEvents`. Begin with the 30 granted matters, then cover denied and nonbinary matters under the same observation rule. Multiple orders on one matter must not be treated as independent policies. A later order can supersede an earlier order; tie observations to the specific event and effective interval.

For each matter seek an official lower-court follow-on order, agency action, executive directive or implementation notice. Record the actor, action, status, source URL, document date, page/paragraph, retrieval date and document hash. The existing Supreme Court docket description is a lead for retrieval; it cannot stand in for an external observation. Keep unavailable-source attempts and unresolved linkage decisions in a separate retrieval log.

Before coding outcomes, have a reviewer approve common follow-up horizons, proposed at 30 and 180 days after the relevant order. Preserve censoring for matters without complete follow-up and record reversals or policy changes in the interval. Distinguish formal legal permission, actual conduct, delay, expiration and replacement. The granted-only first pass supports descriptions of those matters; comparisons with denials need their own identification strategy and confounding assessment.

## 3. Complete environmental legal coding and text recovery

Distribute the two independent 16-document packets according to `docs/expert-legal-coding-protocol.md`. The existing 76-document text-recovery queue is a provider-access task, not a list of ignored precedents. Search by the preserved court, case, date and docket metadata; use source snapshots and exact document hashes. Retain the current published-only, two-year windows until the protocol is explicitly revised. Additional full text changes coverage but does not by itself supply all legally relevant cases.

Design a broader decision cohort through prespecified issue/time/actor rules before observing whether governments complied. Include constitutional cases and sufficient opportunities to observe delay, substitution, resistance and noncompliance; do not select cases because a desired outcome is known. Require a reviewer-approved opportunity rule for non-citing lower-court cases. Join legal obligation, responsible actor, remedy, observable conduct and observation horizon before estimating compliance.

The five existing practical environmental episodes preserve published case-study labels. Ask the reviewer to evaluate the Rapanos workaround classification and the adequacy of official-action support. Those judgments cannot be generalized to a government noncompliance probability.

## Local provenance closure

The four historical Journal fetch failures now have explicit cross-references to corresponding rows already present in the later complete OT2023 cohort, in `reports/legacy-docket-recovery-reconciliation-v1.csv`. Preserve both timestamps and source-record IDs. These are reconciled acquisition histories, not four missing observations in the closed cohort and not newly fetched pages.

Run `make expert-review-check` to detect stale forms or queues; `make replication-check` rebuilds the delivered archive. Returned human judgments and any newly acquired source documents remain separate from generated templates. Public distribution of restricted raw documents still requires a source-specific redistribution decision; the small reader ZIPs contain source links and retained public judicial text, not third-party raw archives.

## Human decisions required before stronger claims

The author needs actual human legal coding and adjudication, a methods assessment of construct/denominator alignment, approval of petition and opportunity coding rules, and a judgment about whether the paper is ready for journal submission. No generated status, test, AI review or archive check can supply these decisions. The local deliverable is a review-ready packet; external acceptance remains open.
