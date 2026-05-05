# Adversarial Manipulation Stress Campaign v2

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 22
- experiment cases: 5

- legislative input: simulation-campaign-v21-paper.csv: volume=0.343 quality=0.610 weakMandate=0.175 rightsRisk=0.104 partisanSkew=0.237 volatility=0.120 legitimacy=0.547

## Case Weights

| Case | Weight | Legislative source | Description |
| --- | ---: | --- | --- |
| Appointment Timing Manipulation | 1.000 | adversarial/imported blend | Political actors time vacancies under high capture and public pressure. |
| Emergency Application Flood | 1.000 | emergency-flood synthetic legislature | Executives and litigants route controversial policies through urgent stay requests. |
| Override Evasion Loop | 1.000 | override-evasion synthetic legislature | Legislatures repeatedly revise invalidated laws to test rights carveouts and override thresholds. |
| Recusal Pressure Campaign | 0.850 | recusal-pressure synthetic legislature | High-salience litigants try to force or avoid recusals around ideologically charged cases. |
| Court Expansion Retaliation | 0.850 | expansion-retaliation synthetic legislature | A polarized political system reacts to judicial conflict with expansion threats and capture pressure. |

## Headline Findings

- Top directional-score cluster within 0.010 of the maximum: No emergency relief without merits review (0.555); 60 percent invalidation threshold (0.552); 18-year staggered terms + regular appointments (0.550); Jurisdiction stripping constrained by rights carveouts (0.547); Nonpartisan commission appointments (0.545); Mandatory written emergency reasoning (0.545); Peer recusal + reasoned emergency docket (0.545). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: No emergency relief without merits review at 0.555.
- Highest rights protection: Automatic merits follow-up for emergency relief at 0.664.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.010.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.288.
- Lowest partisan alignment: Jurisdiction stripping constrained by rights carveouts at 0.043.
- Highest public confidence index: No emergency relief without merits review at 0.670.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, claimant success, precedent durability, lower-court compliance, elite acceptance, and administrative feasibility.
- Empirical claims, synthetic findings, and speculative design recommendations should be read separately: source ranges only smoke-test plausibility, campaign outputs are synthetic, and design recommendations are conditional on the model assumptions.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Higher direct outputs such as `rightsClaimantSuccess`, `doctrinalDepth`, `remedialBreadth`, `precedentDurability`, `lowerCourtCompliance`, `eliteAcceptance`, and `publicConfidence` are usually better, but each should be read in domain context.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `emergencyLegitimacyRisk`, `emergencyDownstreamEffect`, `governmentNoncomplianceRate`, `reversalRate`, `constitutionalConflict`, `administrativeCost`, and `strategicPressure` are usually better.
- Petition, certiorari-admission, lower-court-split, strategic-plaintiff, repeat-player, emergency, emergency-downstream, replacement, recusal, concurrence, dissent, fragmentation, panel, en banc, council, cross-check, remand, public-interest, formal-response, practical-response, noncompliance, and override rates are diagnostic rather than automatically good or bad.

## Scenario Averages Across Cases

| Scenario | Directional | Admission | Cert admit | Lower split | Rights protection | Claimant success | Precedent durability | Lower-court compliance | Gov. noncomp. | Emerg. downstream | Public confidence | Shadow abuse | Emergency risk | Strategic | Admin cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.555 | 0.738 | 0.627 | 0.634 | 0.658 | 0.204 | 0.735 | 0.474 | 0.230 | 0.096 | 0.670 | 0.010 | 0.288 | 0.241 | 0.295 |
| 60 percent invalidation threshold | 0.552 | 0.721 | 0.606 | 0.634 | 0.629 | 0.141 | 0.770 | 0.463 | 0.237 | 0.134 | 0.540 | 0.103 | 0.315 | 0.264 | 0.243 |
| 18-year staggered terms + regular appointments | 0.550 | 0.724 | 0.610 | 0.634 | 0.648 | 0.189 | 0.717 | 0.464 | 0.236 | 0.117 | 0.562 | 0.115 | 0.304 | 0.261 | 0.247 |
| Jurisdiction stripping constrained by rights carveouts | 0.547 | 0.734 | 0.620 | 0.634 | 0.649 | 0.187 | 0.725 | 0.460 | 0.248 | 0.119 | 0.603 | 0.117 | 0.307 | 0.254 | 0.275 |
| Nonpartisan commission appointments | 0.545 | 0.739 | 0.625 | 0.634 | 0.650 | 0.192 | 0.719 | 0.460 | 0.245 | 0.120 | 0.588 | 0.117 | 0.306 | 0.253 | 0.275 |
| Mandatory written emergency reasoning | 0.545 | 0.722 | 0.607 | 0.634 | 0.642 | 0.177 | 0.739 | 0.463 | 0.243 | 0.132 | 0.565 | 0.071 | 0.311 | 0.266 | 0.292 |
| Peer recusal + reasoned emergency docket | 0.545 | 0.722 | 0.612 | 0.634 | 0.646 | 0.188 | 0.715 | 0.464 | 0.239 | 0.117 | 0.573 | 0.114 | 0.302 | 0.261 | 0.279 |
| Expanded 15-seat court | 0.543 | 0.724 | 0.608 | 0.634 | 0.647 | 0.186 | 0.710 | 0.465 | 0.235 | 0.118 | 0.582 | 0.114 | 0.309 | 0.260 | 0.288 |
| Automatic merits follow-up for emergency relief | 0.543 | 0.724 | 0.612 | 0.634 | 0.664 | 0.231 | 0.680 | 0.470 | 0.240 | 0.110 | 0.627 | 0.020 | 0.288 | 0.259 | 0.313 |
| Retention-election accountability court | 0.543 | 0.740 | 0.622 | 0.634 | 0.636 | 0.181 | 0.726 | 0.459 | 0.253 | 0.118 | 0.591 | 0.116 | 0.308 | 0.253 | 0.276 |
| Time-limited legislative override window | 0.543 | 0.739 | 0.626 | 0.634 | 0.651 | 0.184 | 0.731 | 0.458 | 0.252 | 0.119 | 0.595 | 0.117 | 0.307 | 0.263 | 0.284 |
| Three-judge panels with en banc correction | 0.543 | 0.734 | 0.618 | 0.634 | 0.648 | 0.185 | 0.727 | 0.461 | 0.244 | 0.120 | 0.630 | 0.117 | 0.306 | 0.253 | 0.291 |
| Independent recusal enforcement with substitutes | 0.542 | 0.739 | 0.624 | 0.634 | 0.649 | 0.188 | 0.722 | 0.461 | 0.240 | 0.120 | 0.611 | 0.118 | 0.309 | 0.252 | 0.301 |
| Judicial review with legislative supermajority override | 0.542 | 0.735 | 0.621 | 0.634 | 0.652 | 0.185 | 0.722 | 0.458 | 0.250 | 0.119 | 0.594 | 0.117 | 0.308 | 0.264 | 0.283 |
| Comparative 16-seat constitutional senates | 0.541 | 0.720 | 0.604 | 0.634 | 0.624 | 0.127 | 0.782 | 0.465 | 0.230 | 0.134 | 0.625 | 0.103 | 0.314 | 0.249 | 0.325 |
| Randomized merits panels with en banc correction | 0.541 | 0.740 | 0.630 | 0.634 | 0.647 | 0.184 | 0.732 | 0.461 | 0.242 | 0.121 | 0.635 | 0.118 | 0.307 | 0.253 | 0.301 |
| Constitutional remand before invalidation | 0.539 | 0.761 | 0.652 | 0.634 | 0.646 | 0.169 | 0.783 | 0.464 | 0.252 | 0.122 | 0.639 | 0.121 | 0.316 | 0.258 | 0.398 |
| Public-interest litigation filter | 0.539 | 0.775 | 0.675 | 0.634 | 0.662 | 0.206 | 0.727 | 0.453 | 0.254 | 0.125 | 0.600 | 0.122 | 0.320 | 0.260 | 0.318 |
| Pre-enactment constitutional council | 0.536 | 0.741 | 0.630 | 0.634 | 0.647 | 0.172 | 0.746 | 0.460 | 0.248 | 0.117 | 0.669 | 0.116 | 0.306 | 0.260 | 0.373 |
| Stylized current U.S.-like supreme court | 0.535 | 0.722 | 0.604 | 0.634 | 0.658 | 0.208 | 0.672 | 0.437 | 0.262 | 0.202 | 0.360 | 0.374 | 0.402 | 0.290 | 0.196 |
| Supreme court with cross-checking constitutional court | 0.522 | 0.735 | 0.622 | 0.634 | 0.613 | 0.106 | 0.770 | 0.458 | 0.251 | 0.136 | 0.593 | 0.105 | 0.319 | 0.258 | 0.378 |
| Dual supreme courts with disagreement filter | 0.506 | 0.735 | 0.625 | 0.634 | 0.650 | 0.189 | 0.657 | 0.450 | 0.257 | 0.137 | 0.604 | 0.105 | 0.321 | 0.266 | 0.419 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.443 | 0.204 | 0.518 | 0.262 | 0.754 | 0.238 | 0.204 | 0.164 |
| 60 percent invalidation threshold | 0.443 | 0.141 | 0.362 | 0.195 | 0.493 | 0.154 | 0.142 | 0.112 |
| 18-year staggered terms + regular appointments | 0.443 | 0.189 | 0.459 | 0.289 | 0.652 | 0.233 | 0.211 | 0.209 |
| Jurisdiction stripping constrained by rights carveouts | 0.443 | 0.187 | 0.461 | 0.292 | 0.649 | 0.201 | 0.198 | 0.185 |
| Nonpartisan commission appointments | 0.443 | 0.192 | 0.471 | 0.290 | 0.649 | 0.249 | 0.224 | 0.189 |
| Mandatory written emergency reasoning | 0.443 | 0.177 | 0.428 | 0.295 | 0.625 | 0.215 | 0.175 | 0.181 |
| Peer recusal + reasoned emergency docket | 0.443 | 0.188 | 0.462 | 0.300 | 0.635 | 0.250 | 0.214 | 0.190 |
| Expanded 15-seat court | 0.443 | 0.186 | 0.465 | 0.283 | 0.629 | 0.241 | 0.222 | 0.175 |
| Automatic merits follow-up for emergency relief | 0.443 | 0.231 | 0.553 | 0.360 | 0.826 | 0.320 | 0.298 | 0.229 |
| Retention-election accountability court | 0.443 | 0.181 | 0.461 | 0.261 | 0.632 | 0.212 | 0.169 | 0.153 |
| Time-limited legislative override window | 0.443 | 0.184 | 0.456 | 0.282 | 0.624 | 0.208 | 0.235 | 0.184 |
| Three-judge panels with en banc correction | 0.443 | 0.185 | 0.461 | 0.277 | 0.638 | 0.201 | 0.171 | 0.192 |
| Independent recusal enforcement with substitutes | 0.443 | 0.188 | 0.461 | 0.292 | 0.637 | 0.246 | 0.242 | 0.191 |
| Judicial review with legislative supermajority override | 0.443 | 0.185 | 0.464 | 0.289 | 0.629 | 0.218 | 0.180 | 0.177 |
| Comparative 16-seat constitutional senates | 0.443 | 0.127 | 0.330 | 0.182 | 0.447 | 0.093 | 0.108 | 0.103 |
| Randomized merits panels with en banc correction | 0.443 | 0.184 | 0.457 | 0.276 | 0.625 | 0.244 | 0.188 | 0.178 |
| Constitutional remand before invalidation | 0.443 | 0.169 | 0.430 | 0.260 | 0.550 | 0.203 | 0.204 | 0.155 |
| Public-interest litigation filter | 0.443 | 0.206 | 0.519 | 0.326 | 0.641 | 0.260 | 0.209 | 0.207 |
| Pre-enactment constitutional council | 0.443 | 0.172 | 0.434 | 0.244 | 0.605 | 0.188 | 0.179 | 0.136 |
| Stylized current U.S.-like supreme court | 0.443 | 0.208 | 0.507 | 0.304 | 0.809 | 0.289 | 0.207 | 0.162 |
| Supreme court with cross-checking constitutional court | 0.443 | 0.106 | 0.271 | 0.175 | 0.343 | 0.113 | 0.095 | 0.104 |
| Dual supreme courts with disagreement filter | 0.443 | 0.189 | 0.472 | 0.283 | 0.640 | 0.237 | 0.210 | 0.202 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Appointment Timing Manipulation | 18-year staggered terms + regular appointments (0.611) | Dual supreme courts with disagreement filter (0.654) | No emergency relief without merits review (0.001) | Jurisdiction stripping constrained by rights carveouts (0.024) |
| Emergency Application Flood | No emergency relief without merits review (0.532) | Stylized current U.S.-like supreme court (0.683) | No emergency relief without merits review (0.020) | Jurisdiction stripping constrained by rights carveouts (0.040) |
| Override Evasion Loop | 60 percent invalidation threshold (0.548) | Public-interest litigation filter (0.653) | No emergency relief without merits review (0.007) | Judicial review with legislative supermajority override (0.040) |
| Recusal Pressure Campaign | No emergency relief without merits review (0.552) | Automatic merits follow-up for emergency relief (0.668) | No emergency relief without merits review (0.011) | Jurisdiction stripping constrained by rights carveouts (0.048) |
| Court Expansion Retaliation | 60 percent invalidation threshold (0.537) | No emergency relief without merits review (0.670) | No emergency relief without merits review (0.013) | Judicial review with legislative supermajority override (0.063) |
