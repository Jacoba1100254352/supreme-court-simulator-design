# Constitutional Review Campaign v1

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 26
- experiment cases: 15

- legislative input: simulation-campaign-v21-paper.csv: volume=0.343 quality=0.610 weakMandate=0.175 rightsRisk=0.104 partisanSkew=0.237 volatility=0.120 legitimacy=0.547

## Case Weights

| Case | Weight | Legislative source | Description |
| --- | ---: | --- | --- |
| Baseline | 1.000 | neutral synthetic legislature | Moderate polarization, ordinary emergency pressure, and neutral legislative output. |
| Partisan Appointment Pressure | 1.000 | neutral synthetic legislature | High appointment capture and polarized justice pool. |
| Rights-Risk Legislation | 1.000 | rights-risk synthetic legislature | Legislative output creates concentrated rights burdens and weak mandates. |
| Shadow-Docket Stress | 1.000 | emergency-pressure synthetic legislature | High emergency pressure and executive-defiance disputes. |
| High Democratic Mandate | 1.000 | high-mandate synthetic legislature | Popular, high-mandate laws create accountability pressure against invalidation. |
| Constitutional Conflict | 1.000 | conflict synthetic legislature | Polarized laws, executive defiance, and public attention raise court-legislature conflict. |
| Imported Legislative Output | 1.000 | neutral/imported blend | Docket assumptions derived from a legislative simulator campaign CSV. |
| Low Appointment Capture | 0.750 | neutral synthetic legislature | Appointment incentives are less partisan and the justice pool is less polarized. |
| Extreme Appointment Capture | 1.000 | neutral synthetic legislature | Appointment incentives are highly partisan and vacancies become ideological leverage points. |
| Low Emergency Pressure | 0.750 | neutral synthetic legislature | Few cases arrive through urgent stay requests or executive emergency disputes. |
| Extreme Emergency Pressure | 1.000 | extreme-emergency synthetic legislature | Emergency applications, executive-power disputes, and time-sensitive election conflicts are common. |
| Low Rights Risk | 0.750 | low-rights-risk synthetic legislature | Legislative output is legally careful, low-volatility, and rarely burdens protected interests. |
| Extreme Rights Risk | 1.000 | extreme-rights-risk synthetic legislature | Legislative output often creates concentrated rights burdens under contested public mandates. |
| Weak-Mandate Legislation | 1.000 | weak-mandate synthetic legislature | Many reviewed laws have low public legitimacy and high override pressure after invalidation. |
| Strong-Mandate Legislation | 0.750 | strong-mandate synthetic legislature | Popular legislation creates the hardest democratic-responsiveness pressure for review. |

## Headline Findings

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.580); No emergency relief without merits review (0.579); Constitutional remand before invalidation (0.578); 18-year staggered terms + regular appointments (0.577); Jurisdiction stripping constrained by rights carveouts (0.575); Public-interest litigation filter (0.575); Constitutional remand with override window (0.574); Nonpartisan commission appointments (0.574); Mandatory written emergency reasoning (0.574); Peer recusal + reasoned emergency docket (0.574); Retention-election accountability court (0.573); Three-judge panels with en banc correction (0.573); Automatic merits follow-up for emergency relief (0.573); Randomized merits panels with en banc correction (0.572); Emergency integrity package (0.572); Independent recusal enforcement with substitutes (0.572); Expanded 15-seat court (0.571); Time-limited legislative override window (0.571); Judicial review with legislative supermajority override (0.571); Comparative 16-seat constitutional senates (0.571); Random panels with jurisdiction safeguards (0.570). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.580.
- Highest rights protection: No emergency relief without merits review at 0.639.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.019.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.207.
- Lowest partisan alignment: Time-limited legislative override window at 0.019.
- Highest public confidence index: Constitutional council with concrete-review backstop at 0.589.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, claimant success, precedent durability, lower-court compliance, elite acceptance, and administrative feasibility.
- Empirical claims, synthetic findings, and speculative design recommendations should be read separately: source ranges only smoke-test plausibility, campaign outputs are synthetic, and design recommendations are conditional on the model assumptions.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Higher direct outputs such as `rightsClaimantSuccess`, `doctrinalDepth`, `remedialBreadth`, `precedentDurability`, `lowerCourtCompliance`, `eliteAcceptance`, and `publicConfidence` are usually better, but each should be read in domain context.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `emergencyLegitimacyRisk`, `emergencyDownstreamEffect`, `governmentNoncomplianceRate`, `reversalRate`, `constitutionalConflict`, `administrativeCost`, and `strategicPressure` are usually better.
- Petition, court-requested-response, CVSG, certiorari-admission, bar-capital, claim-strength, vehicle-quality, genuine-split, lower-court-split, lower-court-resistance, forum-shopping, settlement, strategic-plaintiff, repeat-player, enforcement-capacity, emergency-opportunism, emergency, emergency-downstream, replacement, recusal, concurrence, dissent, fragmentation, panel, en banc, council, cross-check, remand, public-interest, formal-response, practical-response, noncompliance, and override rates are diagnostic rather than automatically good or bad.

## Scenario Averages Across Cases

| Scenario | Directional | Admission | Cert admit | Lower split | Resistance | Enforcement | Rights protection | Claimant success | Precedent durability | Lower-court compliance | Gov. noncomp. | Emerg. downstream | Public confidence | Shadow abuse | Emergency risk | Strategic | Admin cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.580 | 0.545 | 0.234 | 0.574 | 0.298 | 0.573 | 0.619 | 0.138 | 0.693 | 0.549 | 0.126 | 0.116 | 0.489 | 0.089 | 0.231 | 0.243 | 0.186 |
| No emergency relief without merits review | 0.579 | 0.548 | 0.235 | 0.574 | 0.293 | 0.580 | 0.639 | 0.197 | 0.639 | 0.557 | 0.130 | 0.079 | 0.581 | 0.019 | 0.207 | 0.230 | 0.229 |
| Constitutional remand before invalidation | 0.578 | 0.556 | 0.240 | 0.574 | 0.262 | 0.594 | 0.626 | 0.145 | 0.717 | 0.567 | 0.129 | 0.101 | 0.557 | 0.097 | 0.224 | 0.232 | 0.303 |
| 18-year staggered terms + regular appointments | 0.577 | 0.545 | 0.233 | 0.574 | 0.297 | 0.575 | 0.628 | 0.165 | 0.656 | 0.550 | 0.131 | 0.101 | 0.505 | 0.097 | 0.222 | 0.245 | 0.191 |
| Jurisdiction stripping constrained by rights carveouts | 0.575 | 0.548 | 0.234 | 0.574 | 0.297 | 0.605 | 0.629 | 0.165 | 0.655 | 0.550 | 0.143 | 0.101 | 0.532 | 0.097 | 0.222 | 0.241 | 0.213 |
| Public-interest litigation filter | 0.575 | 0.551 | 0.238 | 0.574 | 0.297 | 0.575 | 0.633 | 0.170 | 0.666 | 0.551 | 0.130 | 0.100 | 0.524 | 0.096 | 0.223 | 0.231 | 0.237 |
| Constitutional remand with override window | 0.574 | 0.555 | 0.239 | 0.574 | 0.262 | 0.593 | 0.623 | 0.138 | 0.729 | 0.566 | 0.130 | 0.115 | 0.557 | 0.068 | 0.233 | 0.231 | 0.334 |
| Nonpartisan commission appointments | 0.574 | 0.551 | 0.238 | 0.574 | 0.297 | 0.575 | 0.629 | 0.165 | 0.656 | 0.549 | 0.132 | 0.101 | 0.521 | 0.098 | 0.223 | 0.238 | 0.213 |
| Mandatory written emergency reasoning | 0.574 | 0.545 | 0.234 | 0.574 | 0.297 | 0.575 | 0.625 | 0.156 | 0.671 | 0.550 | 0.132 | 0.114 | 0.505 | 0.068 | 0.230 | 0.244 | 0.228 |
| Peer recusal + reasoned emergency docket | 0.574 | 0.544 | 0.231 | 0.574 | 0.297 | 0.575 | 0.627 | 0.163 | 0.657 | 0.550 | 0.129 | 0.101 | 0.510 | 0.097 | 0.222 | 0.244 | 0.219 |
| Retention-election accountability court | 0.573 | 0.548 | 0.234 | 0.574 | 0.297 | 0.576 | 0.620 | 0.160 | 0.662 | 0.549 | 0.135 | 0.100 | 0.522 | 0.096 | 0.222 | 0.239 | 0.213 |
| Three-judge panels with en banc correction | 0.573 | 0.551 | 0.239 | 0.574 | 0.296 | 0.575 | 0.629 | 0.164 | 0.662 | 0.550 | 0.129 | 0.102 | 0.561 | 0.098 | 0.223 | 0.235 | 0.229 |
| Automatic merits follow-up for emergency relief | 0.573 | 0.543 | 0.231 | 0.574 | 0.294 | 0.580 | 0.637 | 0.201 | 0.620 | 0.556 | 0.132 | 0.081 | 0.555 | 0.026 | 0.207 | 0.241 | 0.244 |
| Randomized merits panels with en banc correction | 0.572 | 0.549 | 0.233 | 0.574 | 0.297 | 0.575 | 0.629 | 0.164 | 0.665 | 0.550 | 0.132 | 0.101 | 0.562 | 0.097 | 0.221 | 0.235 | 0.235 |
| Emergency integrity package | 0.572 | 0.550 | 0.236 | 0.574 | 0.293 | 0.580 | 0.639 | 0.198 | 0.634 | 0.557 | 0.130 | 0.082 | 0.585 | 0.026 | 0.209 | 0.231 | 0.267 |
| Independent recusal enforcement with substitutes | 0.572 | 0.548 | 0.235 | 0.574 | 0.297 | 0.575 | 0.629 | 0.166 | 0.655 | 0.550 | 0.131 | 0.101 | 0.534 | 0.097 | 0.224 | 0.237 | 0.234 |
| Expanded 15-seat court | 0.571 | 0.546 | 0.235 | 0.574 | 0.297 | 0.575 | 0.628 | 0.164 | 0.648 | 0.550 | 0.130 | 0.101 | 0.517 | 0.097 | 0.225 | 0.245 | 0.226 |
| Time-limited legislative override window | 0.571 | 0.547 | 0.233 | 0.574 | 0.298 | 0.576 | 0.629 | 0.164 | 0.657 | 0.547 | 0.138 | 0.101 | 0.524 | 0.097 | 0.223 | 0.246 | 0.220 |
| Judicial review with legislative supermajority override | 0.571 | 0.549 | 0.236 | 0.574 | 0.298 | 0.576 | 0.630 | 0.165 | 0.657 | 0.547 | 0.140 | 0.101 | 0.524 | 0.097 | 0.223 | 0.248 | 0.220 |
| Comparative 16-seat constitutional senates | 0.571 | 0.543 | 0.230 | 0.574 | 0.298 | 0.573 | 0.619 | 0.132 | 0.703 | 0.551 | 0.126 | 0.115 | 0.553 | 0.089 | 0.230 | 0.235 | 0.258 |
| Random panels with jurisdiction safeguards | 0.570 | 0.547 | 0.232 | 0.574 | 0.298 | 0.603 | 0.619 | 0.140 | 0.689 | 0.549 | 0.137 | 0.116 | 0.565 | 0.089 | 0.231 | 0.236 | 0.259 |
| Pre-enactment constitutional council | 0.568 | 0.551 | 0.239 | 0.574 | 0.295 | 0.619 | 0.630 | 0.161 | 0.668 | 0.554 | 0.138 | 0.101 | 0.585 | 0.097 | 0.223 | 0.245 | 0.293 |
| Stylized current U.S.-like supreme court | 0.567 | 0.544 | 0.232 | 0.574 | 0.305 | 0.566 | 0.637 | 0.181 | 0.624 | 0.533 | 0.143 | 0.165 | 0.370 | 0.280 | 0.290 | 0.271 | 0.151 |
| Constitutional council with concrete-review backstop | 0.567 | 0.548 | 0.233 | 0.574 | 0.295 | 0.619 | 0.629 | 0.154 | 0.677 | 0.556 | 0.136 | 0.100 | 0.589 | 0.096 | 0.221 | 0.242 | 0.305 |
| Supreme court with cross-checking constitutional court | 0.561 | 0.547 | 0.233 | 0.574 | 0.277 | 0.593 | 0.603 | 0.097 | 0.708 | 0.556 | 0.129 | 0.116 | 0.521 | 0.089 | 0.232 | 0.233 | 0.295 |
| Dual supreme courts with disagreement filter | 0.546 | 0.546 | 0.232 | 0.574 | 0.299 | 0.573 | 0.626 | 0.161 | 0.619 | 0.542 | 0.137 | 0.117 | 0.525 | 0.090 | 0.234 | 0.243 | 0.330 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.380 | 0.138 | 0.325 | 0.356 | 0.640 | 0.189 | 0.282 | 0.169 |
| No emergency relief without merits review | 0.380 | 0.197 | 0.458 | 0.451 | 0.932 | 0.302 | 0.376 | 0.235 |
| Constitutional remand before invalidation | 0.380 | 0.145 | 0.357 | 0.346 | 0.643 | 0.193 | 0.268 | 0.172 |
| 18-year staggered terms + regular appointments | 0.380 | 0.165 | 0.400 | 0.395 | 0.730 | 0.238 | 0.318 | 0.211 |
| Jurisdiction stripping constrained by rights carveouts | 0.380 | 0.165 | 0.401 | 0.401 | 0.734 | 0.223 | 0.341 | 0.197 |
| Public-interest litigation filter | 0.380 | 0.170 | 0.421 | 0.427 | 0.746 | 0.229 | 0.309 | 0.208 |
| Constitutional remand with override window | 0.380 | 0.138 | 0.333 | 0.332 | 0.634 | 0.182 | 0.280 | 0.163 |
| Nonpartisan commission appointments | 0.380 | 0.165 | 0.398 | 0.403 | 0.739 | 0.235 | 0.337 | 0.211 |
| Mandatory written emergency reasoning | 0.380 | 0.156 | 0.372 | 0.397 | 0.724 | 0.234 | 0.299 | 0.204 |
| Peer recusal + reasoned emergency docket | 0.380 | 0.163 | 0.390 | 0.397 | 0.737 | 0.259 | 0.321 | 0.210 |
| Retention-election accountability court | 0.380 | 0.160 | 0.388 | 0.374 | 0.712 | 0.224 | 0.295 | 0.193 |
| Three-judge panels with en banc correction | 0.380 | 0.164 | 0.400 | 0.402 | 0.735 | 0.231 | 0.324 | 0.205 |
| Automatic merits follow-up for emergency relief | 0.380 | 0.201 | 0.466 | 0.481 | 0.949 | 0.353 | 0.446 | 0.257 |
| Randomized merits panels with en banc correction | 0.380 | 0.164 | 0.398 | 0.413 | 0.730 | 0.214 | 0.332 | 0.200 |
| Emergency integrity package | 0.380 | 0.198 | 0.460 | 0.448 | 0.931 | 0.313 | 0.418 | 0.247 |
| Independent recusal enforcement with substitutes | 0.380 | 0.166 | 0.400 | 0.418 | 0.738 | 0.234 | 0.339 | 0.219 |
| Expanded 15-seat court | 0.380 | 0.164 | 0.396 | 0.402 | 0.739 | 0.232 | 0.334 | 0.201 |
| Time-limited legislative override window | 0.380 | 0.164 | 0.396 | 0.406 | 0.735 | 0.236 | 0.324 | 0.204 |
| Judicial review with legislative supermajority override | 0.380 | 0.165 | 0.400 | 0.401 | 0.734 | 0.236 | 0.335 | 0.204 |
| Comparative 16-seat constitutional senates | 0.380 | 0.132 | 0.313 | 0.315 | 0.617 | 0.141 | 0.221 | 0.145 |
| Random panels with jurisdiction safeguards | 0.380 | 0.140 | 0.332 | 0.365 | 0.652 | 0.205 | 0.262 | 0.188 |
| Pre-enactment constitutional council | 0.380 | 0.161 | 0.394 | 0.365 | 0.726 | 0.212 | 0.283 | 0.181 |
| Stylized current U.S.-like supreme court | 0.380 | 0.181 | 0.405 | 0.419 | 0.952 | 0.329 | 0.384 | 0.215 |
| Constitutional council with concrete-review backstop | 0.380 | 0.154 | 0.373 | 0.349 | 0.687 | 0.181 | 0.253 | 0.169 |
| Supreme court with cross-checking constitutional court | 0.380 | 0.097 | 0.235 | 0.283 | 0.417 | 0.143 | 0.179 | 0.134 |
| Dual supreme courts with disagreement filter | 0.380 | 0.161 | 0.384 | 0.406 | 0.743 | 0.208 | 0.319 | 0.209 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | No emergency relief without merits review (0.609) | Emergency integrity package (0.649) | No emergency relief without merits review (0.011) | Time-limited legislative override window (0.015) |
| Partisan Appointment Pressure | No emergency relief without merits review (0.609) | No emergency relief without merits review (0.649) | No emergency relief without merits review (0.011) | Dual supreme courts with disagreement filter (0.018) |
| Rights-Risk Legislation | Constitutional remand before invalidation (0.550) | No emergency relief without merits review (0.610) | No emergency relief without merits review (0.018) | Dual supreme courts with disagreement filter (0.020) |
| Shadow-Docket Stress | 60 percent invalidation threshold (0.550) | Stylized current U.S.-like supreme court (0.665) | No emergency relief without merits review (0.037) | Jurisdiction stripping constrained by rights carveouts (0.022) |
| High Democratic Mandate | No emergency relief without merits review (0.629) | Nonpartisan commission appointments (0.648) | No emergency relief without merits review (0.007) | Dual supreme courts with disagreement filter (0.009) |
| Constitutional Conflict | 60 percent invalidation threshold (0.520) | Stylized current U.S.-like supreme court (0.645) | No emergency relief without merits review (0.038) | Time-limited legislative override window (0.034) |
| Imported Legislative Output | No emergency relief without merits review (0.616) | Emergency integrity package (0.654) | No emergency relief without merits review (0.009) | Jurisdiction stripping constrained by rights carveouts (0.014) |
| Low Appointment Capture | No emergency relief without merits review (0.611) | No emergency relief without merits review (0.648) | No emergency relief without merits review (0.011) | Time-limited legislative override window (0.010) |
| Extreme Appointment Capture | No emergency relief without merits review (0.608) | No emergency relief without merits review (0.648) | No emergency relief without merits review (0.011) | Time-limited legislative override window (0.021) |
| Low Emergency Pressure | No emergency relief without merits review (0.615) | Public-interest litigation filter (0.646) | No emergency relief without merits review (0.008) | Dual supreme courts with disagreement filter (0.014) |
| Extreme Emergency Pressure | 60 percent invalidation threshold (0.525) | Stylized current U.S.-like supreme court (0.668) | No emergency relief without merits review (0.048) | Judicial review with legislative supermajority override (0.030) |
| Low Rights Risk | No emergency relief without merits review (0.637) | Emergency integrity package (0.649) | No emergency relief without merits review (0.006) | Time-limited legislative override window (0.009) |
| Extreme Rights Risk | No emergency relief without merits review (0.522) | Automatic merits follow-up for emergency relief (0.602) | No emergency relief without merits review (0.026) | Judicial review with legislative supermajority override (0.027) |
| Weak-Mandate Legislation | 60 percent invalidation threshold (0.539) | Stylized current U.S.-like supreme court (0.625) | No emergency relief without merits review (0.019) | Jurisdiction stripping constrained by rights carveouts (0.018) |
| Strong-Mandate Legislation | No emergency relief without merits review (0.635) | Judicial review with legislative supermajority override (0.647) | No emergency relief without merits review (0.006) | Dual supreme courts with disagreement filter (0.010) |
