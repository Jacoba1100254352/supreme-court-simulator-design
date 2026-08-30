# Constitutional Review Campaign v1

Deterministic simulation study for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 27
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
| Imported Legislative Output | 1.000 | neutral/imported blend | Docket assumptions derived from an imported legislative-output profile. |
| Low Appointment Capture | 0.750 | neutral synthetic legislature | Appointment incentives are less partisan and the justice pool is less polarized. |
| Extreme Appointment Capture | 1.000 | neutral synthetic legislature | Appointment incentives are highly partisan and vacancies become ideological leverage points. |
| Low Emergency Pressure | 0.750 | neutral synthetic legislature | Few cases arrive through urgent stay requests or executive emergency disputes. |
| Extreme Emergency Pressure | 1.000 | extreme-emergency synthetic legislature | Emergency applications, executive-power disputes, and time-sensitive election conflicts are common. |
| Low Rights Risk | 0.750 | low-rights-risk synthetic legislature | Legislative output is legally careful, low-volatility, and rarely burdens protected interests. |
| Extreme Rights Risk | 1.000 | extreme-rights-risk synthetic legislature | Legislative output often creates concentrated rights burdens under contested public mandates. |
| Weak-Mandate Legislation | 1.000 | weak-mandate synthetic legislature | Many reviewed laws have low public legitimacy and high override pressure after invalidation. |
| Strong-Mandate Legislation | 0.750 | strong-mandate synthetic legislature | Popular legislation creates the hardest democratic-responsiveness pressure for review. |

## Headline Findings

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.581); No emergency relief without merits review (0.579); 18-year staggered terms + regular appointments (0.578); Constitutional remand before invalidation (0.578); Jurisdiction stripping constrained by rights carveouts (0.576); Public-interest litigation filter (0.576); Nonpartisan commission appointments (0.575); Constitutional remand with override window (0.575); Mandatory written emergency reasoning (0.574); Peer recusal + reasoned emergency docket (0.574); Three-judge panels with en banc correction (0.574); Retention-election accountability court (0.573); Automatic merits follow-up for emergency relief (0.573); Randomized merits panels with en banc correction (0.572); Independent recusal enforcement with substitutes (0.572); Emergency integrity package (0.572); Expanded 15-seat court (0.572); Time-limited legislative override window (0.572); Comparative 16-seat constitutional senates (0.571); Judicial review with legislative supermajority override (0.571). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.581.
- Highest rights protection: Emergency integrity package at 0.635.
- Lowest emergency-process irregularity: No emergency relief without merits review at 0.018.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.206.
- Lowest partisan alignment: Time-limited legislative override window at 0.018.
- Highest modeled process-legitimacy index: Constitutional council with concrete-review backstop at 0.577.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, claimant success, precedent durability, lower-court compliance, elite acceptance, and administrative feasibility.
- Empirical claims, synthetic findings, and speculative design recommendations should be read separately: plausibility checks only screen source ranges, simulation outputs are synthetic, and design recommendations are conditional on the model assumptions.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Higher direct outputs such as `rightsClaimantSuccess`, `doctrinalDepth`, `remedialBreadth`, `precedentDurability`, `lowerCourtCompliance`, `eliteAcceptance`, and `processLegitimacyProxy` are usually better, but each should be read in domain context.
- Lower `partisanAlignment`, `emergencyProcessIrregularity`, `emergencyLegitimacyRisk`, `emergencyDownstreamEffect`, `governmentNoncomplianceRate`, `reversalRate`, `constitutionalConflict`, `administrativeCost`, and `strategicPressure` are usually better.
- Petition, court-requested-response, CVSG, certiorari-admission, bar-capital, claim-strength, vehicle-quality, genuine-split, lower-court-split, lower-court-resistance, forum-shopping, settlement, strategic-plaintiff, repeat-player, enforcement-capacity, emergency-opportunism, emergency, emergency-downstream, replacement, recusal, concurrence, dissent, fragmentation, panel, en banc, council, cross-check, remand, public-interest, formal-response, practical-response, noncompliance, and override rates are diagnostic rather than automatically good or bad.

## Scenario Averages Across Cases

| Scenario | Directional | Admission | Cert admit | Lower split | Resistance | Enforcement | Rights protection | Claimant success | Precedent durability | Lower-court compliance | Gov. noncomp. | Emerg. downstream | Public-legit. proxy | Emerg. irregularity | Emergency risk | Strategic | Admin cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.581 | 0.524 | 0.196 | 0.574 | 0.298 | 0.572 | 0.616 | 0.134 | 0.692 | 0.551 | 0.123 | 0.114 | 0.481 | 0.087 | 0.229 | 0.240 | 0.182 |
| No emergency relief without merits review | 0.579 | 0.529 | 0.201 | 0.574 | 0.293 | 0.579 | 0.635 | 0.192 | 0.640 | 0.559 | 0.125 | 0.078 | 0.571 | 0.018 | 0.206 | 0.229 | 0.225 |
| 18-year staggered terms + regular appointments | 0.578 | 0.522 | 0.193 | 0.574 | 0.297 | 0.574 | 0.624 | 0.159 | 0.656 | 0.552 | 0.126 | 0.099 | 0.495 | 0.095 | 0.219 | 0.242 | 0.186 |
| Constitutional remand before invalidation | 0.578 | 0.535 | 0.204 | 0.574 | 0.262 | 0.592 | 0.622 | 0.141 | 0.714 | 0.568 | 0.125 | 0.100 | 0.545 | 0.097 | 0.222 | 0.230 | 0.296 |
| Jurisdiction stripping constrained by rights carveouts | 0.576 | 0.527 | 0.199 | 0.574 | 0.297 | 0.604 | 0.626 | 0.160 | 0.656 | 0.552 | 0.138 | 0.100 | 0.521 | 0.096 | 0.221 | 0.240 | 0.208 |
| Public-interest litigation filter | 0.576 | 0.531 | 0.202 | 0.574 | 0.297 | 0.574 | 0.630 | 0.166 | 0.666 | 0.552 | 0.126 | 0.099 | 0.515 | 0.095 | 0.221 | 0.230 | 0.232 |
| Nonpartisan commission appointments | 0.575 | 0.528 | 0.199 | 0.574 | 0.297 | 0.574 | 0.625 | 0.160 | 0.657 | 0.551 | 0.126 | 0.100 | 0.511 | 0.096 | 0.221 | 0.236 | 0.208 |
| Constitutional remand with override window | 0.575 | 0.534 | 0.202 | 0.574 | 0.262 | 0.592 | 0.619 | 0.134 | 0.724 | 0.568 | 0.124 | 0.113 | 0.546 | 0.068 | 0.230 | 0.230 | 0.325 |
| Mandatory written emergency reasoning | 0.574 | 0.525 | 0.199 | 0.574 | 0.298 | 0.574 | 0.622 | 0.151 | 0.671 | 0.551 | 0.128 | 0.113 | 0.497 | 0.067 | 0.228 | 0.243 | 0.223 |
| Peer recusal + reasoned emergency docket | 0.574 | 0.524 | 0.198 | 0.574 | 0.297 | 0.574 | 0.624 | 0.159 | 0.656 | 0.552 | 0.127 | 0.099 | 0.502 | 0.095 | 0.220 | 0.243 | 0.214 |
| Three-judge panels with en banc correction | 0.574 | 0.530 | 0.200 | 0.574 | 0.297 | 0.574 | 0.626 | 0.159 | 0.662 | 0.552 | 0.125 | 0.101 | 0.549 | 0.097 | 0.221 | 0.234 | 0.224 |
| Retention-election accountability court | 0.573 | 0.531 | 0.204 | 0.574 | 0.298 | 0.575 | 0.617 | 0.156 | 0.661 | 0.550 | 0.132 | 0.100 | 0.513 | 0.097 | 0.222 | 0.239 | 0.209 |
| Automatic merits follow-up for emergency relief | 0.573 | 0.525 | 0.198 | 0.574 | 0.294 | 0.579 | 0.634 | 0.196 | 0.623 | 0.557 | 0.129 | 0.081 | 0.546 | 0.026 | 0.206 | 0.239 | 0.239 |
| Randomized merits panels with en banc correction | 0.572 | 0.528 | 0.197 | 0.574 | 0.297 | 0.574 | 0.625 | 0.158 | 0.663 | 0.552 | 0.126 | 0.100 | 0.550 | 0.097 | 0.221 | 0.234 | 0.231 |
| Independent recusal enforcement with substitutes | 0.572 | 0.527 | 0.198 | 0.574 | 0.297 | 0.574 | 0.625 | 0.159 | 0.658 | 0.551 | 0.127 | 0.100 | 0.524 | 0.097 | 0.222 | 0.236 | 0.229 |
| Emergency integrity package | 0.572 | 0.530 | 0.201 | 0.574 | 0.293 | 0.579 | 0.635 | 0.193 | 0.633 | 0.558 | 0.127 | 0.081 | 0.575 | 0.026 | 0.208 | 0.231 | 0.262 |
| Expanded 15-seat court | 0.572 | 0.522 | 0.195 | 0.574 | 0.297 | 0.574 | 0.624 | 0.158 | 0.649 | 0.552 | 0.125 | 0.100 | 0.506 | 0.096 | 0.223 | 0.243 | 0.221 |
| Time-limited legislative override window | 0.572 | 0.526 | 0.196 | 0.574 | 0.298 | 0.575 | 0.625 | 0.158 | 0.657 | 0.549 | 0.135 | 0.100 | 0.513 | 0.097 | 0.221 | 0.245 | 0.215 |
| Comparative 16-seat constitutional senates | 0.571 | 0.523 | 0.196 | 0.574 | 0.298 | 0.572 | 0.616 | 0.128 | 0.702 | 0.552 | 0.122 | 0.114 | 0.541 | 0.088 | 0.229 | 0.235 | 0.253 |
| Judicial review with legislative supermajority override | 0.571 | 0.528 | 0.199 | 0.574 | 0.298 | 0.575 | 0.627 | 0.160 | 0.656 | 0.548 | 0.138 | 0.100 | 0.515 | 0.096 | 0.221 | 0.247 | 0.215 |
| Random panels with jurisdiction safeguards | 0.571 | 0.527 | 0.196 | 0.574 | 0.298 | 0.602 | 0.617 | 0.138 | 0.687 | 0.551 | 0.135 | 0.115 | 0.554 | 0.089 | 0.230 | 0.235 | 0.254 |
| Pre-enactment constitutional council | 0.568 | 0.530 | 0.202 | 0.574 | 0.295 | 0.617 | 0.626 | 0.155 | 0.667 | 0.556 | 0.132 | 0.099 | 0.572 | 0.096 | 0.221 | 0.243 | 0.286 |
| Constitutional council with concrete-review backstop | 0.568 | 0.527 | 0.198 | 0.574 | 0.295 | 0.617 | 0.625 | 0.149 | 0.676 | 0.557 | 0.133 | 0.099 | 0.577 | 0.095 | 0.220 | 0.241 | 0.299 |
| Judicial electorate selection court | 0.567 | 0.531 | 0.201 | 0.574 | 0.297 | 0.574 | 0.627 | 0.162 | 0.657 | 0.551 | 0.127 | 0.100 | 0.532 | 0.097 | 0.223 | 0.231 | 0.270 |
| Stylized current U.S.-like supreme court | 0.564 | 0.526 | 0.200 | 0.574 | 0.307 | 0.565 | 0.634 | 0.175 | 0.623 | 0.529 | 0.158 | 0.166 | 0.358 | 0.284 | 0.295 | 0.274 | 0.149 |
| Supreme court with cross-checking constitutional court | 0.562 | 0.528 | 0.199 | 0.574 | 0.278 | 0.592 | 0.601 | 0.095 | 0.706 | 0.557 | 0.126 | 0.114 | 0.512 | 0.088 | 0.230 | 0.232 | 0.289 |
| Dual supreme courts with disagreement filter | 0.547 | 0.528 | 0.199 | 0.574 | 0.300 | 0.572 | 0.624 | 0.159 | 0.618 | 0.543 | 0.135 | 0.115 | 0.516 | 0.089 | 0.231 | 0.242 | 0.324 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.380 | 0.134 | 0.313 | 0.360 | 0.644 | 0.183 | 0.242 | 0.150 |
| No emergency relief without merits review | 0.380 | 0.192 | 0.445 | 0.430 | 0.931 | 0.283 | 0.397 | 0.210 |
| 18-year staggered terms + regular appointments | 0.380 | 0.159 | 0.385 | 0.392 | 0.734 | 0.200 | 0.271 | 0.193 |
| Constitutional remand before invalidation | 0.380 | 0.141 | 0.343 | 0.341 | 0.642 | 0.164 | 0.256 | 0.159 |
| Jurisdiction stripping constrained by rights carveouts | 0.380 | 0.160 | 0.385 | 0.392 | 0.745 | 0.215 | 0.306 | 0.184 |
| Public-interest litigation filter | 0.380 | 0.166 | 0.411 | 0.400 | 0.748 | 0.231 | 0.299 | 0.185 |
| Nonpartisan commission appointments | 0.380 | 0.160 | 0.386 | 0.388 | 0.739 | 0.238 | 0.305 | 0.187 |
| Constitutional remand with override window | 0.380 | 0.134 | 0.324 | 0.320 | 0.630 | 0.163 | 0.237 | 0.149 |
| Mandatory written emergency reasoning | 0.380 | 0.151 | 0.355 | 0.385 | 0.738 | 0.204 | 0.251 | 0.178 |
| Peer recusal + reasoned emergency docket | 0.380 | 0.159 | 0.381 | 0.394 | 0.735 | 0.223 | 0.284 | 0.202 |
| Three-judge panels with en banc correction | 0.380 | 0.159 | 0.386 | 0.398 | 0.725 | 0.194 | 0.296 | 0.187 |
| Retention-election accountability court | 0.380 | 0.156 | 0.377 | 0.369 | 0.709 | 0.222 | 0.289 | 0.178 |
| Automatic merits follow-up for emergency relief | 0.380 | 0.196 | 0.455 | 0.470 | 0.950 | 0.328 | 0.426 | 0.232 |
| Randomized merits panels with en banc correction | 0.380 | 0.158 | 0.381 | 0.394 | 0.735 | 0.197 | 0.272 | 0.192 |
| Independent recusal enforcement with substitutes | 0.380 | 0.159 | 0.383 | 0.387 | 0.728 | 0.225 | 0.306 | 0.187 |
| Emergency integrity package | 0.380 | 0.193 | 0.450 | 0.434 | 0.933 | 0.299 | 0.388 | 0.221 |
| Expanded 15-seat court | 0.380 | 0.158 | 0.381 | 0.393 | 0.727 | 0.215 | 0.298 | 0.184 |
| Time-limited legislative override window | 0.380 | 0.158 | 0.382 | 0.370 | 0.739 | 0.182 | 0.290 | 0.198 |
| Comparative 16-seat constitutional senates | 0.380 | 0.128 | 0.302 | 0.303 | 0.626 | 0.148 | 0.208 | 0.124 |
| Judicial review with legislative supermajority override | 0.380 | 0.160 | 0.380 | 0.384 | 0.744 | 0.242 | 0.306 | 0.203 |
| Random panels with jurisdiction safeguards | 0.380 | 0.138 | 0.326 | 0.365 | 0.653 | 0.172 | 0.279 | 0.168 |
| Pre-enactment constitutional council | 0.380 | 0.155 | 0.372 | 0.362 | 0.720 | 0.202 | 0.268 | 0.179 |
| Constitutional council with concrete-review backstop | 0.380 | 0.149 | 0.361 | 0.336 | 0.692 | 0.166 | 0.237 | 0.158 |
| Judicial electorate selection court | 0.380 | 0.162 | 0.393 | 0.396 | 0.740 | 0.224 | 0.320 | 0.205 |
| Stylized current U.S.-like supreme court | 0.380 | 0.175 | 0.387 | 0.400 | 0.951 | 0.318 | 0.359 | 0.200 |
| Supreme court with cross-checking constitutional court | 0.380 | 0.095 | 0.232 | 0.251 | 0.420 | 0.132 | 0.169 | 0.135 |
| Dual supreme courts with disagreement filter | 0.380 | 0.159 | 0.374 | 0.398 | 0.768 | 0.203 | 0.320 | 0.188 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest emerg. irregularity | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | No emergency relief without merits review (0.610) | Automatic merits follow-up for emergency relief (0.644) | No emergency relief without merits review (0.011) | Jurisdiction stripping constrained by rights carveouts (0.015) |
| Partisan Appointment Pressure | No emergency relief without merits review (0.608) | No emergency relief without merits review (0.641) | No emergency relief without merits review (0.011) | Dual supreme courts with disagreement filter (0.017) |
| Rights-Risk Legislation | Constitutional remand before invalidation (0.550) | Emergency integrity package (0.605) | No emergency relief without merits review (0.018) | Dual supreme courts with disagreement filter (0.020) |
| Shadow-Docket Stress | 60 percent invalidation threshold (0.548) | Stylized current U.S.-like supreme court (0.664) | No emergency relief without merits review (0.037) | Time-limited legislative override window (0.022) |
| High Democratic Mandate | No emergency relief without merits review (0.629) | Automatic merits follow-up for emergency relief (0.644) | No emergency relief without merits review (0.008) | Dual supreme courts with disagreement filter (0.009) |
| Constitutional Conflict | 60 percent invalidation threshold (0.521) | Stylized current U.S.-like supreme court (0.641) | No emergency relief without merits review (0.037) | Judicial review with legislative supermajority override (0.033) |
| Imported Legislative Output | No emergency relief without merits review (0.616) | No emergency relief without merits review (0.648) | No emergency relief without merits review (0.009) | Time-limited legislative override window (0.013) |
| Low Appointment Capture | No emergency relief without merits review (0.611) | Automatic merits follow-up for emergency relief (0.649) | No emergency relief without merits review (0.011) | Time-limited legislative override window (0.010) |
| Extreme Appointment Capture | No emergency relief without merits review (0.608) | Emergency integrity package (0.646) | No emergency relief without merits review (0.011) | Time-limited legislative override window (0.021) |
| Low Emergency Pressure | 60 percent invalidation threshold (0.616) | Public-interest litigation filter (0.642) | No emergency relief without merits review (0.008) | Dual supreme courts with disagreement filter (0.013) |
| Extreme Emergency Pressure | 60 percent invalidation threshold (0.522) | Stylized current U.S.-like supreme court (0.665) | No emergency relief without merits review (0.047) | Jurisdiction stripping constrained by rights carveouts (0.029) |
| Low Rights Risk | Jurisdiction stripping constrained by rights carveouts (0.638) | Three-judge panels with en banc correction (0.645) | No emergency relief without merits review (0.006) | Time-limited legislative override window (0.008) |
| Extreme Rights Risk | No emergency relief without merits review (0.522) | Emergency integrity package (0.598) | No emergency relief without merits review (0.026) | Judicial review with legislative supermajority override (0.026) |
| Weak-Mandate Legislation | 60 percent invalidation threshold (0.544) | Stylized current U.S.-like supreme court (0.622) | No emergency relief without merits review (0.019) | Time-limited legislative override window (0.017) |
| Strong-Mandate Legislation | No emergency relief without merits review (0.636) | Judicial electorate selection court (0.644) | No emergency relief without merits review (0.006) | Dual supreme courts with disagreement filter (0.009) |
