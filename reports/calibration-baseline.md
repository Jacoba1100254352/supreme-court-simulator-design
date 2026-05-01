# Historical Calibration Baseline v4

Empirical plausibility checks for the constitutional-review simulator. Target ranges are computed from normalized source observations and widened by metric-specific model tolerances; they remain calibration guardrails, not validation.

## Run Configuration

- runs: 80
- cases per run: 64
- seed: 20260501
- legislative profile: simulation-campaign-v21-paper.csv

- calibration data directory: `data/calibration`
- source observations: 709

## Summary

- targets passing: 17 / 17

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

| Target | Scenario | Metric | Source metric | Observed | Range | Source median | Source obs. | Source terms | Pass |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| Rights-related merits domains track SCDB rights issue areas. | Stylized current U.S.-like supreme court | `rightsClaimRate` | `rightsClaimRate` | 0.389 | 0.064-0.479 | 0.299 | 79 | 1946-2024 | pass |
| Administrative-law challenges track SCDB administrative-action observations. | Stylized current U.S.-like supreme court | `administrativeLawRate` | `administrativeLawRate` | 0.010 | 0.000-0.503 | 0.234 | 79 | 1946-2024 | pass |
| Election disputes remain a stress domain rather than the whole docket. | Stylized current U.S.-like supreme court | `electionDisputeRate` | `structuralRate` | 0.202 | 0.074-0.429 | 0.223 | 79 | 1946-2024 | pass |
| Executive-power disputes remain visible but bounded within structural public-law disputes. | Stylized current U.S.-like supreme court | `executivePowerDisputeRate` | `structuralRate` | 0.176 | 0.074-0.429 | 0.223 | 79 | 1946-2024 | pass |
| Declarations of unconstitutionality should be uncommon in the full merits docket. | Stylized current U.S.-like supreme court | `invalidationRate` | `invalidationRate` | 0.221 | 0.000-0.223 | 0.066 | 79 | 1946-2024 | pass |
| Current-like cases should usually receive merits review outside pure emergency processing. | Stylized current U.S.-like supreme court | `meritsReviewRate` | `meritsReviewRate` | 0.608 | 0.600-1.000 | 1.000 | 79 | 1946-2024 | pass |
| Emergency applications should be present but bounded in the current-like docket. | Stylized current U.S.-like supreme court | `emergencyStayDocketRate` | `emergencyStayDocketRate` | 0.203 | 0.000-0.223 | 0.006 | 32 | 1993-2024 | pass |
| Emergency orders should be observable but not universal. | Stylized current U.S.-like supreme court | `emergencyOrderRate` | `emergencyOrderRate` | 0.759 | 0.000-0.773 | 0.100 | 22 | 2003-2024 | pass |
| Justice-case recusals should be rare. | Stylized current U.S.-like supreme court | `recusalRate` | `recusalRate` | 0.008 | 0.000-0.029 | 0.009 | 1 | 1946-2003 | pass |
| Open emergency procedure creates measurable but bounded shadow-docket abuse. | Stylized current U.S.-like supreme court | `shadowDocketAbuse` | `shadowDocketAbuse` | 0.425 | 0.000-0.657 | 0.222 | 22 | 2003-2024 | pass |
| Precedent stability remains high enough for a stable merits court. | Stylized current U.S.-like supreme court | `precedentStability` | `precedentStability` | 0.870 | 0.853-1.000 | 0.983 | 79 | 1946-2024 | pass |
| Statutory stability remains in a source-derived post-review band. | Stylized current U.S.-like supreme court | `statutoryStability` | `statutoryStability` | 0.647 | 0.627-1.000 | 0.934 | 79 | 1946-2024 | pass |
| Interbranch compliance stays above a low-conflict floor. | Stylized current U.S.-like supreme court | `interbranchCompliance` | `statutoryStability` | 0.455 | 0.427-1.000 | 0.934 | 79 | 1946-2024 | pass |
| Commission appointments should keep partisan alignment low. | Nonpartisan commission appointments | `partisanAlignment` | `shadowDocketAbuse` | 0.045 | 0.000-0.657 | 0.222 | 22 | 2003-2024 | pass |
| No-relief-without-merits should sharply suppress shadow-docket abuse. | No emergency relief without merits review | `shadowDocketAbuse` | `shadowDocketAbuse` | 0.003 | 0.000-0.657 | 0.222 | 22 | 2003-2024 | pass |
| Emergency-restraint designs should convert urgent matters into merits acceleration. | No emergency relief without merits review | `meritsAccelerationRate` | `emergencyOrderRate` | 0.681 | 0.000-0.683 | 0.100 | 22 | 2003-2024 | pass |
| Override designs should produce observable but not constant override attempts. | Judicial review with legislative supermajority override | `overrideAttemptRate` | `invalidationRate` | 0.128 | 0.000-0.333 | 0.066 | 79 | 1946-2024 | pass |

See `calibration-source-ranges-v4.md` for the generated source-range appendix.
