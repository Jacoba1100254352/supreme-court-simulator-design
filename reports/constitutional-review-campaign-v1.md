# Constitutional Review Campaign v1

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

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

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.581); No emergency relief without merits review (0.580); 18-year staggered terms + regular appointments (0.578); Constitutional remand before invalidation (0.578); Jurisdiction stripping constrained by rights carveouts (0.576); Public-interest litigation filter (0.576); Nonpartisan commission appointments (0.575); Constitutional remand with override window (0.575); Mandatory written emergency reasoning (0.574); Peer recusal + reasoned emergency docket (0.574); Automatic merits follow-up for emergency relief (0.574); Three-judge panels with en banc correction (0.574); Retention-election accountability court (0.574); Randomized merits panels with en banc correction (0.573); Emergency integrity package (0.573); Independent recusal enforcement with substitutes (0.573); Expanded 15-seat court (0.572); Time-limited legislative override window (0.572); Comparative 16-seat constitutional senates (0.571); Judicial review with legislative supermajority override (0.571). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.581.
- Highest rights protection: Emergency integrity package at 0.635.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.018.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.204.
- Lowest partisan alignment: Time-limited legislative override window at 0.018.
- Highest public confidence index: Constitutional council with concrete-review backstop at 0.575.
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
| 60 percent invalidation threshold | 0.581 | 0.519 | 0.189 | 0.574 | 0.298 | 0.571 | 0.615 | 0.132 | 0.692 | 0.552 | 0.123 | 0.114 | 0.479 | 0.087 | 0.228 | 0.240 | 0.181 |
| No emergency relief without merits review | 0.580 | 0.525 | 0.193 | 0.574 | 0.293 | 0.579 | 0.634 | 0.190 | 0.641 | 0.560 | 0.123 | 0.078 | 0.569 | 0.018 | 0.204 | 0.228 | 0.223 |
| 18-year staggered terms + regular appointments | 0.578 | 0.518 | 0.186 | 0.574 | 0.297 | 0.574 | 0.624 | 0.158 | 0.656 | 0.552 | 0.126 | 0.098 | 0.494 | 0.095 | 0.218 | 0.242 | 0.185 |
| Constitutional remand before invalidation | 0.578 | 0.531 | 0.198 | 0.574 | 0.262 | 0.591 | 0.621 | 0.140 | 0.713 | 0.568 | 0.124 | 0.100 | 0.544 | 0.096 | 0.221 | 0.230 | 0.294 |
| Jurisdiction stripping constrained by rights carveouts | 0.576 | 0.523 | 0.191 | 0.574 | 0.297 | 0.604 | 0.624 | 0.158 | 0.657 | 0.552 | 0.137 | 0.099 | 0.520 | 0.095 | 0.219 | 0.239 | 0.207 |
| Public-interest litigation filter | 0.576 | 0.526 | 0.195 | 0.574 | 0.297 | 0.574 | 0.629 | 0.165 | 0.665 | 0.553 | 0.125 | 0.099 | 0.513 | 0.095 | 0.220 | 0.229 | 0.230 |
| Nonpartisan commission appointments | 0.575 | 0.523 | 0.189 | 0.574 | 0.297 | 0.574 | 0.624 | 0.158 | 0.658 | 0.552 | 0.126 | 0.099 | 0.508 | 0.096 | 0.220 | 0.236 | 0.207 |
| Constitutional remand with override window | 0.575 | 0.530 | 0.194 | 0.574 | 0.263 | 0.591 | 0.618 | 0.133 | 0.723 | 0.568 | 0.125 | 0.113 | 0.544 | 0.067 | 0.229 | 0.230 | 0.323 |
| Mandatory written emergency reasoning | 0.574 | 0.522 | 0.193 | 0.574 | 0.298 | 0.573 | 0.622 | 0.152 | 0.669 | 0.551 | 0.127 | 0.113 | 0.496 | 0.067 | 0.227 | 0.242 | 0.222 |
| Peer recusal + reasoned emergency docket | 0.574 | 0.519 | 0.189 | 0.574 | 0.297 | 0.574 | 0.623 | 0.156 | 0.657 | 0.552 | 0.126 | 0.099 | 0.500 | 0.095 | 0.219 | 0.242 | 0.213 |
| Automatic merits follow-up for emergency relief | 0.574 | 0.520 | 0.189 | 0.574 | 0.294 | 0.579 | 0.633 | 0.195 | 0.624 | 0.558 | 0.127 | 0.080 | 0.544 | 0.026 | 0.205 | 0.238 | 0.238 |
| Three-judge panels with en banc correction | 0.574 | 0.524 | 0.189 | 0.574 | 0.297 | 0.574 | 0.625 | 0.159 | 0.661 | 0.552 | 0.125 | 0.100 | 0.547 | 0.096 | 0.219 | 0.234 | 0.223 |
| Retention-election accountability court | 0.574 | 0.526 | 0.194 | 0.574 | 0.298 | 0.575 | 0.616 | 0.154 | 0.661 | 0.551 | 0.131 | 0.099 | 0.511 | 0.096 | 0.221 | 0.237 | 0.208 |
| Randomized merits panels with en banc correction | 0.573 | 0.524 | 0.188 | 0.574 | 0.297 | 0.574 | 0.625 | 0.157 | 0.663 | 0.552 | 0.126 | 0.100 | 0.548 | 0.096 | 0.219 | 0.233 | 0.230 |
| Emergency integrity package | 0.573 | 0.525 | 0.192 | 0.574 | 0.293 | 0.579 | 0.635 | 0.192 | 0.633 | 0.559 | 0.125 | 0.080 | 0.573 | 0.026 | 0.206 | 0.230 | 0.260 |
| Independent recusal enforcement with substitutes | 0.573 | 0.523 | 0.190 | 0.574 | 0.297 | 0.574 | 0.624 | 0.158 | 0.657 | 0.552 | 0.126 | 0.099 | 0.522 | 0.096 | 0.220 | 0.235 | 0.228 |
| Expanded 15-seat court | 0.572 | 0.519 | 0.189 | 0.574 | 0.297 | 0.574 | 0.624 | 0.157 | 0.650 | 0.553 | 0.124 | 0.099 | 0.505 | 0.096 | 0.222 | 0.242 | 0.220 |
| Time-limited legislative override window | 0.572 | 0.522 | 0.189 | 0.574 | 0.298 | 0.575 | 0.625 | 0.158 | 0.657 | 0.549 | 0.135 | 0.099 | 0.512 | 0.096 | 0.220 | 0.244 | 0.214 |
| Comparative 16-seat constitutional senates | 0.571 | 0.520 | 0.190 | 0.574 | 0.298 | 0.571 | 0.615 | 0.127 | 0.702 | 0.552 | 0.122 | 0.114 | 0.539 | 0.087 | 0.228 | 0.234 | 0.252 |
| Judicial review with legislative supermajority override | 0.571 | 0.524 | 0.192 | 0.574 | 0.298 | 0.574 | 0.625 | 0.158 | 0.656 | 0.549 | 0.137 | 0.099 | 0.513 | 0.095 | 0.220 | 0.247 | 0.214 |
| Random panels with jurisdiction safeguards | 0.571 | 0.525 | 0.191 | 0.574 | 0.298 | 0.602 | 0.616 | 0.137 | 0.687 | 0.551 | 0.134 | 0.115 | 0.552 | 0.088 | 0.230 | 0.235 | 0.254 |
| Pre-enactment constitutional council | 0.569 | 0.525 | 0.194 | 0.574 | 0.296 | 0.617 | 0.625 | 0.154 | 0.667 | 0.556 | 0.132 | 0.099 | 0.570 | 0.096 | 0.220 | 0.242 | 0.284 |
| Constitutional council with concrete-review backstop | 0.568 | 0.523 | 0.190 | 0.574 | 0.295 | 0.617 | 0.624 | 0.148 | 0.676 | 0.558 | 0.131 | 0.098 | 0.575 | 0.094 | 0.218 | 0.240 | 0.297 |
| Judicial electorate selection court | 0.568 | 0.527 | 0.193 | 0.574 | 0.297 | 0.574 | 0.626 | 0.160 | 0.658 | 0.552 | 0.127 | 0.100 | 0.530 | 0.096 | 0.222 | 0.230 | 0.268 |
| Stylized current U.S.-like supreme court | 0.565 | 0.522 | 0.190 | 0.574 | 0.307 | 0.565 | 0.633 | 0.174 | 0.624 | 0.530 | 0.157 | 0.165 | 0.357 | 0.283 | 0.293 | 0.273 | 0.148 |
| Supreme court with cross-checking constitutional court | 0.562 | 0.523 | 0.190 | 0.574 | 0.278 | 0.592 | 0.600 | 0.094 | 0.706 | 0.558 | 0.125 | 0.113 | 0.510 | 0.087 | 0.227 | 0.231 | 0.287 |
| Dual supreme courts with disagreement filter | 0.547 | 0.523 | 0.191 | 0.574 | 0.300 | 0.572 | 0.623 | 0.157 | 0.618 | 0.543 | 0.135 | 0.115 | 0.513 | 0.088 | 0.230 | 0.242 | 0.322 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.380 | 0.132 | 0.308 | 0.351 | 0.648 | 0.185 | 0.254 | 0.145 |
| No emergency relief without merits review | 0.380 | 0.190 | 0.438 | 0.424 | 0.931 | 0.290 | 0.395 | 0.204 |
| 18-year staggered terms + regular appointments | 0.380 | 0.158 | 0.381 | 0.396 | 0.740 | 0.206 | 0.277 | 0.184 |
| Constitutional remand before invalidation | 0.380 | 0.140 | 0.341 | 0.332 | 0.637 | 0.173 | 0.251 | 0.156 |
| Jurisdiction stripping constrained by rights carveouts | 0.380 | 0.158 | 0.380 | 0.389 | 0.741 | 0.205 | 0.296 | 0.175 |
| Public-interest litigation filter | 0.380 | 0.165 | 0.405 | 0.401 | 0.746 | 0.227 | 0.292 | 0.185 |
| Nonpartisan commission appointments | 0.380 | 0.158 | 0.382 | 0.386 | 0.729 | 0.223 | 0.294 | 0.184 |
| Constitutional remand with override window | 0.380 | 0.133 | 0.320 | 0.320 | 0.629 | 0.162 | 0.234 | 0.148 |
| Mandatory written emergency reasoning | 0.380 | 0.152 | 0.358 | 0.394 | 0.731 | 0.216 | 0.261 | 0.177 |
| Peer recusal + reasoned emergency docket | 0.380 | 0.156 | 0.374 | 0.389 | 0.729 | 0.225 | 0.295 | 0.196 |
| Automatic merits follow-up for emergency relief | 0.380 | 0.195 | 0.449 | 0.469 | 0.950 | 0.310 | 0.421 | 0.221 |
| Three-judge panels with en banc correction | 0.380 | 0.159 | 0.386 | 0.394 | 0.727 | 0.187 | 0.294 | 0.182 |
| Retention-election accountability court | 0.380 | 0.154 | 0.375 | 0.368 | 0.709 | 0.207 | 0.283 | 0.166 |
| Randomized merits panels with en banc correction | 0.380 | 0.157 | 0.379 | 0.387 | 0.738 | 0.187 | 0.277 | 0.183 |
| Emergency integrity package | 0.380 | 0.192 | 0.447 | 0.435 | 0.933 | 0.295 | 0.371 | 0.219 |
| Independent recusal enforcement with substitutes | 0.380 | 0.158 | 0.379 | 0.390 | 0.727 | 0.219 | 0.320 | 0.184 |
| Expanded 15-seat court | 0.380 | 0.157 | 0.381 | 0.391 | 0.729 | 0.211 | 0.312 | 0.181 |
| Time-limited legislative override window | 0.380 | 0.158 | 0.382 | 0.367 | 0.730 | 0.196 | 0.288 | 0.194 |
| Comparative 16-seat constitutional senates | 0.380 | 0.127 | 0.300 | 0.299 | 0.620 | 0.148 | 0.202 | 0.119 |
| Judicial review with legislative supermajority override | 0.380 | 0.158 | 0.378 | 0.380 | 0.735 | 0.248 | 0.317 | 0.196 |
| Random panels with jurisdiction safeguards | 0.380 | 0.137 | 0.325 | 0.351 | 0.660 | 0.160 | 0.263 | 0.158 |
| Pre-enactment constitutional council | 0.380 | 0.154 | 0.367 | 0.363 | 0.721 | 0.204 | 0.283 | 0.166 |
| Constitutional council with concrete-review backstop | 0.380 | 0.148 | 0.356 | 0.336 | 0.689 | 0.168 | 0.242 | 0.150 |
| Judicial electorate selection court | 0.380 | 0.160 | 0.389 | 0.378 | 0.736 | 0.216 | 0.311 | 0.195 |
| Stylized current U.S.-like supreme court | 0.380 | 0.174 | 0.382 | 0.397 | 0.951 | 0.311 | 0.369 | 0.200 |
| Supreme court with cross-checking constitutional court | 0.380 | 0.094 | 0.228 | 0.247 | 0.426 | 0.118 | 0.167 | 0.126 |
| Dual supreme courts with disagreement filter | 0.380 | 0.157 | 0.370 | 0.383 | 0.760 | 0.202 | 0.323 | 0.191 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | No emergency relief without merits review (0.610) | No emergency relief without merits review (0.646) | No emergency relief without merits review (0.011) | Jurisdiction stripping constrained by rights carveouts (0.014) |
| Partisan Appointment Pressure | No emergency relief without merits review (0.608) | No emergency relief without merits review (0.640) | No emergency relief without merits review (0.011) | Dual supreme courts with disagreement filter (0.017) |
| Rights-Risk Legislation | Constitutional remand before invalidation (0.549) | Emergency integrity package (0.605) | No emergency relief without merits review (0.018) | Dual supreme courts with disagreement filter (0.020) |
| Shadow-Docket Stress | 60 percent invalidation threshold (0.548) | Stylized current U.S.-like supreme court (0.662) | No emergency relief without merits review (0.037) | Time-limited legislative override window (0.021) |
| High Democratic Mandate | No emergency relief without merits review (0.629) | Automatic merits follow-up for emergency relief (0.643) | No emergency relief without merits review (0.008) | Dual supreme courts with disagreement filter (0.009) |
| Constitutional Conflict | Constitutional remand before invalidation (0.522) | Stylized current U.S.-like supreme court (0.641) | No emergency relief without merits review (0.037) | Judicial review with legislative supermajority override (0.033) |
| Imported Legislative Output | No emergency relief without merits review (0.616) | Automatic merits follow-up for emergency relief (0.647) | No emergency relief without merits review (0.009) | Time-limited legislative override window (0.013) |
| Low Appointment Capture | No emergency relief without merits review (0.611) | Automatic merits follow-up for emergency relief (0.644) | No emergency relief without merits review (0.010) | Time-limited legislative override window (0.010) |
| Extreme Appointment Capture | No emergency relief without merits review (0.609) | Emergency integrity package (0.645) | No emergency relief without merits review (0.011) | Time-limited legislative override window (0.020) |
| Low Emergency Pressure | 60 percent invalidation threshold (0.615) | Public-interest litigation filter (0.639) | No emergency relief without merits review (0.008) | Dual supreme courts with disagreement filter (0.013) |
| Extreme Emergency Pressure | 60 percent invalidation threshold (0.523) | Stylized current U.S.-like supreme court (0.663) | No emergency relief without merits review (0.047) | Jurisdiction stripping constrained by rights carveouts (0.029) |
| Low Rights Risk | Jurisdiction stripping constrained by rights carveouts (0.637) | Jurisdiction stripping constrained by rights carveouts (0.644) | No emergency relief without merits review (0.006) | Time-limited legislative override window (0.008) |
| Extreme Rights Risk | 60 percent invalidation threshold (0.522) | Emergency integrity package (0.598) | No emergency relief without merits review (0.026) | Judicial review with legislative supermajority override (0.026) |
| Weak-Mandate Legislation | 60 percent invalidation threshold (0.544) | Stylized current U.S.-like supreme court (0.619) | No emergency relief without merits review (0.019) | Jurisdiction stripping constrained by rights carveouts (0.017) |
| Strong-Mandate Legislation | No emergency relief without merits review (0.635) | Judicial electorate selection court (0.641) | No emergency relief without merits review (0.007) | Dual supreme courts with disagreement filter (0.009) |
