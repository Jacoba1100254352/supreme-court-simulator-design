# Historical Calibration Baseline v4

Empirical plausibility checks for the constitutional-review simulator. Target ranges are computed from normalized source observations and widened by metric-specific model tolerances; they remain calibration guardrails, not validation.

## Run Configuration

- runs: 80
- cases per run: 64
- seed: 20260501
- legislative profile: simulation-campaign-v21-paper.csv

- calibration data directory: `data/calibration`
- source observations: 758

## Summary

- targets within assigned ranges: 17 / 17
- guardrail-use counts: strict_validation=5, model_prior_check=2, loose_calibration=5, proxy_sanity_check=3, mechanism_sanity_check=2

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
| `deep-research-intake-synthesis` | [Normalized comparative intake source-register rows](data/calibration/supreme-court-synthesis/source-register.csv) | Preserves named-source intake-denominator rows with validation-use and coverage metadata; used here as a structural guardrail rather than a one-to-one empirical target. |
| `model-docket-mix-prior` | [Simulator docket-mix prior](src/main/java/constitutionalreview/simulation/WorldGenerator.java) | Defines stress-domain bounds for generated docket categories that do not map cleanly to a single empirical source denominator. |
## Targets

| Target | Scenario | Use | Metric | Source metric | Observed | Range | Source median | Source obs. | Source terms | Status |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| Rights-related merits domains track SCDB rights issue areas. | Stylized current U.S.-like supreme court | `strict_validation` | `rightsClaimRate` | `rightsClaimRate` | 0.225 | 0.064-0.479 | 0.299 | 79 | 1946-2024 | within range |
| Administrative-law challenges track SCDB administrative-action observations. | Stylized current U.S.-like supreme court | `strict_validation` | `administrativeLawRate` | `administrativeLawRate` | 0.167 | 0.000-0.503 | 0.234 | 79 | 1946-2024 | within range |
| Election disputes remain a stress domain rather than the whole docket. | Stylized current U.S.-like supreme court | `model_prior_check` | `electionDisputeRate` | `electionDocketShare` | 0.055 | 0.020-0.240 | 0.130 | 0 |  | within range |
| Executive-power disputes remain visible but bounded within structural public-law disputes. | Stylized current U.S.-like supreme court | `loose_calibration` | `executivePowerDisputeRate` | `structuralRate` | 0.088 | 0.074-0.429 | 0.223 | 79 | 1946-2024 | within range |
| Declarations of unconstitutionality should be uncommon in the full merits docket. | Stylized current U.S.-like supreme court | `strict_validation` | `invalidationRate` | `invalidationRate` | 0.038 | 0.000-0.223 | 0.066 | 79 | 1946-2024 | within range |
| Admissibility-aware current-like designs should transfer a substantial but not universal share of filed matters to merits. | Stylized current U.S.-like supreme court | `model_prior_check` | `meritsTransferRate` | `admissibilityModelShare` | 0.406 | 0.250-0.850 | 0.550 | 0 |  | within range |
| Emergency applications should be present but bounded in the current-like docket. | Stylized current U.S.-like supreme court | `strict_validation` | `emergencyStayDocketRate` | `emergencyStayDocketRate` | 0.054 | 0.000-0.223 | 0.006 | 32 | 1993-2024 | within range |
| Emergency orders should be observable but not universal. | Stylized current U.S.-like supreme court | `loose_calibration` | `emergencyOrderRate` | `emergencyOrderRate` | 0.285 | 0.000-0.773 | 0.100 | 22 | 2003-2024 | within range |
| Justice-case recusals should be rare. | Stylized current U.S.-like supreme court | `strict_validation` | `recusalRate` | `recusalRate` | 0.008 | 0.000-0.029 | 0.009 | 1 | 1946-2003 | within range |
| Open emergency procedure creates measurable but bounded shadow-docket abuse. | Stylized current U.S.-like supreme court | `loose_calibration` | `shadowDocketAbuse` | `shadowDocketAbuse` | 0.156 | 0.000-0.657 | 0.222 | 22 | 2003-2024 | within range |
| Precedent stability remains high enough for a stress-inclusive docket with screened and emergency matters. | Stylized current U.S.-like supreme court | `loose_calibration` | `precedentStability` | `precedentStability` | 0.810 | 0.773-1.000 | 0.983 | 79 | 1946-2024 | within range |
| Statutory stability remains in a source-derived post-review band. | Stylized current U.S.-like supreme court | `loose_calibration` | `statutoryStability` | `statutoryStability` | 0.706 | 0.627-1.000 | 0.934 | 79 | 1946-2024 | within range |
| Interbranch compliance stays above a low-conflict floor. | Stylized current U.S.-like supreme court | `proxy_sanity_check` | `interbranchCompliance` | `statutoryStability` | 0.576 | 0.427-1.000 | 0.934 | 79 | 1946-2024 | within range |
| Commission appointments should keep partisan alignment low. | Nonpartisan commission appointments | `proxy_sanity_check` | `partisanAlignment` | `shadowDocketAbuse` | 0.020 | 0.000-0.657 | 0.222 | 22 | 2003-2024 | within range |
| No-relief-without-merits should sharply suppress shadow-docket abuse. | No emergency relief without merits review | `mechanism_sanity_check` | `shadowDocketAbuse` | `shadowDocketAbuse` | 0.001 | 0.000-0.657 | 0.222 | 22 | 2003-2024 | within range |
| Emergency-restraint designs should convert urgent matters into merits acceleration. | No emergency relief without merits review | `mechanism_sanity_check` | `meritsAccelerationRate` | `emergencyOrderRate` | 0.277 | 0.000-0.683 | 0.100 | 22 | 2003-2024 | within range |
| Override designs should produce observable but not constant override attempts. | Judicial review with legislative supermajority override | `proxy_sanity_check` | `overrideAttemptRate` | `invalidationRate` | 0.022 | 0.000-0.333 | 0.066 | 79 | 1946-2024 | within range |

See `calibration-source-ranges-v4.md` for the generated source-range appendix.
