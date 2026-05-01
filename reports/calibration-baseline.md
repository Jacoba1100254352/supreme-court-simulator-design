# Calibration Baseline v2

Synthetic plausibility checks for the constitutional-review simulator. These are guardrails, not empirical validation.

## Run Configuration

- runs: 80
- cases per run: 64
- seed: 20260501
- legislative profile: simulation-campaign-v21-paper.csv

## Summary

- targets passing: 16 / 16

## Targets

| Target | Scenario | Metric | Observed | Range | Pass |
| --- | --- | --- | ---: | ---: | --- |
| Facial challenges remain a material share of the synthetic docket. | Stylized current U.S.-like supreme court | `facialChallengeRate` | 0.238 | 0.080-0.450 | pass |
| As-applied challenges remain visible but not dominant. | Stylized current U.S.-like supreme court | `asAppliedChallengeRate` | 0.065 | 0.020-0.300 | pass |
| Election disputes are plausible as a stress category. | Stylized current U.S.-like supreme court | `electionDisputeRate` | 0.168 | 0.060-0.280 | pass |
| Emergency stay applications are present but not the whole docket. | Stylized current U.S.-like supreme court | `emergencyStayDocketRate` | 0.048 | 0.010-0.220 | pass |
| Executive-power disputes remain a recurring constitutional category. | Stylized current U.S.-like supreme court | `executivePowerDisputeRate` | 0.162 | 0.060-0.300 | pass |
| Administrative-law challenges remain a recurring constitutional category. | Stylized current U.S.-like supreme court | `administrativeLawRate` | 0.145 | 0.060-0.300 | pass |
| Rights claims remain a major constitutional review category. | Stylized current U.S.-like supreme court | `rightsClaimRate` | 0.174 | 0.060-0.350 | pass |
| Current-like invalidation does not dominate the whole docket. | Stylized current U.S.-like supreme court | `invalidationRate` | 0.005 | 0.000-0.450 | pass |
| Current-like recusals are rare at the justice-case level. | Stylized current U.S.-like supreme court | `recusalRate` | 0.006 | 0.000-0.120 | pass |
| Open emergency procedure creates measurable but bounded shadow-docket abuse. | Stylized current U.S.-like supreme court | `shadowDocketAbuse` | 0.163 | 0.050-0.450 | pass |
| Precedent stability stays in a plausible unit-interval band. | Stylized current U.S.-like supreme court | `precedentStability` | 0.975 | 0.550-1.000 | pass |
| Statutory stability stays in a plausible unit-interval band. | Stylized current U.S.-like supreme court | `statutoryStability` | 0.759 | 0.450-1.000 | pass |
| Interbranch compliance stays in a plausible unit-interval band. | Stylized current U.S.-like supreme court | `interbranchCompliance` | 0.648 | 0.350-1.000 | pass |
| Commission appointments should keep partisan alignment low. | Nonpartisan commission appointments | `partisanAlignment` | 0.025 | 0.000-0.120 | pass |
| No-relief-without-merits should sharply suppress shadow-docket abuse. | No emergency relief without merits review | `shadowDocketAbuse` | 0.000 | 0.000-0.080 | pass |
| Override designs should produce observable but not constant override attempts. | Judicial review with legislative supermajority override | `overrideAttemptRate` | 0.003 | 0.000-0.300 | pass |
