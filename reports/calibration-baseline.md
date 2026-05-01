# Historical Calibration Baseline v3

Source-backed plausibility checks for the constitutional-review simulator. These ranges are broad guardrails, not empirical validation.

## Run Configuration

- runs: 80
- cases per run: 64
- seed: 20260501
- legislative profile: simulation-campaign-v21-paper.csv

## Summary

- targets passing: 19 / 19

## Sources

| Key | Source | Basis |
| --- | --- | --- |
| `scdb-issue-area` | [Supreme Court Database issue-area codebook](https://scdb.la.psu.edu/online-codebook/issue-area/) | Maps merits cases into broad legal issue areas such as civil rights, First Amendment, due process, privacy, economic activity, judicial power, and federalism. |
| `scdb-unconstitutionality` | [Supreme Court Database declaration-of-unconstitutionality codebook](https://scdb.la.psu.edu/online-codebook/declaration-of-unconstitutionality/) | Identifies decisions declaring federal, state, territorial, municipal, or local law unconstitutional. |
| `hlr-subject-matter` | [Harvard Law Review Supreme Court Statistics, Table III](https://harvardlawreview.org/supreme-court-statistics/) | Tracks subject matter of full opinions and constitutional holdings in recent terms. |
| `hlr-merits` | [Harvard Law Review Supreme Court Statistics, full opinions / merits cases](https://harvardlawreview.org/supreme-court-statistics/) | Distinguishes full-opinion merits cases from emergency-relief application orders. |
| `hlr-emergency` | [Harvard Law Review Supreme Court Statistics, applications for emergency relief](https://harvardlawreview.org/supreme-court-statistics/) | Tracks dispositions, writings, dissenting votes, and justice agreement in applications for emergency relief. |
| `hlr-voting-alignments` | [Harvard Law Review Supreme Court Statistics, voting alignments](https://harvardlawreview.org/supreme-court-statistics/) | Tracks justice alignment patterns in merits opinions and emergency-relief orders. |
| `shadow-docket-database` | [Kastellec and Taboni, Supreme Court Shadow Docket Database, 1993-2025](https://www.cambridge.org/core/journals/journal-of-law-and-courts/article/database-of-the-united-states-supreme-courts-shadow-docket-19932025/266C0FA883BE4120FB4F37D387EFC61E) | Parses Journal orders and separately tracks emergency applications, including stays, injunctions, and vacatur requests. |
| `epstein-recusal` | [Black and Epstein, Recusals and the Problem of an Equally Divided Supreme Court](https://epstein.wustl.edu/recusal) | Reports 599 post-1946 recusal cases and treats recusals as rare case-level events. |
| `scdb-formal-precedent` | [Supreme Court Database formal alteration of precedent variable](https://scdb.la.psu.edu/online-codebook/formal-alteration-of-precedent/) | Provides a historical anchor for rare formal precedent alteration. |
## Targets

| Target | Scenario | Metric | Observed | Range | Source | Pass |
| --- | --- | --- | ---: | ---: | --- | --- |
| Rights-related merits domains stay within a broad SCDB/HLR subject-matter band. | Stylized current U.S.-like supreme court | `rightsClaimRate` | 0.174 | 0.100-0.480 | `scdb-issue-area` | pass |
| Administrative-law challenges remain a recurring but not dominant merits domain. | Stylized current U.S.-like supreme court | `administrativeLawRate` | 0.145 | 0.050-0.320 | `scdb-issue-area` | pass |
| Election disputes remain a stress domain rather than the whole docket. | Stylized current U.S.-like supreme court | `electionDisputeRate` | 0.168 | 0.020-0.240 | `hlr-subject-matter` | pass |
| Executive-power disputes are visible but bounded. | Stylized current U.S.-like supreme court | `executivePowerDisputeRate` | 0.162 | 0.030-0.300 | `hlr-subject-matter` | pass |
| Facial challenges remain a material constitutional-review slice. | Stylized current U.S.-like supreme court | `facialChallengeRate` | 0.238 | 0.080-0.450 | `scdb-unconstitutionality` | pass |
| As-applied challenges remain visible but not dominant. | Stylized current U.S.-like supreme court | `asAppliedChallengeRate` | 0.065 | 0.020-0.300 | `scdb-unconstitutionality` | pass |
| Declarations of unconstitutionality should be uncommon in the full merits docket. | Stylized current U.S.-like supreme court | `invalidationRate` | 0.094 | 0.000-0.220 | `scdb-unconstitutionality` | pass |
| Current-like cases should usually receive merits review outside pure emergency processing. | Stylized current U.S.-like supreme court | `meritsReviewRate` | 0.789 | 0.600-1.000 | `hlr-merits` | pass |
| Emergency applications should be present but bounded in the current-like docket. | Stylized current U.S.-like supreme court | `emergencyStayDocketRate` | 0.048 | 0.010-0.220 | `shadow-docket-database` | pass |
| Emergency orders should be observable but not universal. | Stylized current U.S.-like supreme court | `emergencyOrderRate` | 0.537 | 0.050-0.600 | `hlr-emergency` | pass |
| Justice-case recusals should be rare. | Stylized current U.S.-like supreme court | `recusalRate` | 0.008 | 0.000-0.060 | `epstein-recusal` | pass |
| Open emergency procedure creates measurable but bounded shadow-docket abuse. | Stylized current U.S.-like supreme court | `shadowDocketAbuse` | 0.282 | 0.050-0.550 | `shadow-docket-database` | pass |
| Precedent stability remains high enough for a stable merits court. | Stylized current U.S.-like supreme court | `precedentStability` | 0.937 | 0.550-1.000 | `scdb-formal-precedent` | pass |
| Statutory stability remains in the middle-to-high band after review. | Stylized current U.S.-like supreme court | `statutoryStability` | 0.702 | 0.400-1.000 | `scdb-unconstitutionality` | pass |
| Interbranch compliance stays above a low-conflict floor. | Stylized current U.S.-like supreme court | `interbranchCompliance` | 0.549 | 0.300-1.000 | `hlr-emergency` | pass |
| Commission appointments should keep partisan alignment low. | Nonpartisan commission appointments | `partisanAlignment` | 0.041 | 0.000-0.140 | `hlr-voting-alignments` | pass |
| No-relief-without-merits should sharply suppress shadow-docket abuse. | No emergency relief without merits review | `shadowDocketAbuse` | 0.002 | 0.000-0.080 | `shadow-docket-database` | pass |
| Emergency-restraint designs should convert urgent matters into merits acceleration. | No emergency relief without merits review | `meritsAccelerationRate` | 0.493 | 0.100-0.750 | `hlr-emergency` | pass |
| Override designs should produce observable but not constant override attempts. | Judicial review with legislative supermajority override | `overrideAttemptRate` | 0.048 | 0.000-0.350 | `scdb-unconstitutionality` | pass |
