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

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.579); No emergency relief without merits review (0.578); Constitutional remand before invalidation (0.577); 18-year staggered terms + regular appointments (0.576); Jurisdiction stripping constrained by rights carveouts (0.575); Public-interest litigation filter (0.574); Nonpartisan commission appointments (0.574); Constitutional remand with override window (0.573); Mandatory written emergency reasoning (0.573); Peer recusal + reasoned emergency docket (0.573); Retention-election accountability court (0.573); Automatic merits follow-up for emergency relief (0.572); Three-judge panels with en banc correction (0.572); Emergency integrity package (0.571); Randomized merits panels with en banc correction (0.571); Independent recusal enforcement with substitutes (0.571); Expanded 15-seat court (0.571); Time-limited legislative override window (0.570); Comparative 16-seat constitutional senates (0.570); Judicial review with legislative supermajority override (0.570). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.579.
- Highest rights protection: Emergency integrity package at 0.639.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.019.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.211.
- Lowest partisan alignment: Time-limited legislative override window at 0.019.
- Highest public confidence index: Constitutional council with concrete-review backstop at 0.587.
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
| 60 percent invalidation threshold | 0.579 | 0.545 | 0.235 | 0.574 | 0.298 | 0.573 | 0.619 | 0.137 | 0.693 | 0.549 | 0.126 | 0.118 | 0.488 | 0.091 | 0.237 | 0.244 | 0.188 |
| No emergency relief without merits review | 0.578 | 0.549 | 0.236 | 0.574 | 0.293 | 0.580 | 0.639 | 0.197 | 0.640 | 0.557 | 0.129 | 0.081 | 0.581 | 0.019 | 0.212 | 0.231 | 0.230 |
| Constitutional remand before invalidation | 0.577 | 0.555 | 0.238 | 0.574 | 0.261 | 0.593 | 0.626 | 0.145 | 0.717 | 0.567 | 0.127 | 0.103 | 0.554 | 0.100 | 0.229 | 0.232 | 0.304 |
| 18-year staggered terms + regular appointments | 0.576 | 0.546 | 0.236 | 0.574 | 0.297 | 0.575 | 0.629 | 0.164 | 0.656 | 0.549 | 0.132 | 0.102 | 0.503 | 0.099 | 0.227 | 0.247 | 0.192 |
| Jurisdiction stripping constrained by rights carveouts | 0.575 | 0.548 | 0.233 | 0.574 | 0.297 | 0.605 | 0.629 | 0.164 | 0.656 | 0.550 | 0.142 | 0.103 | 0.529 | 0.099 | 0.228 | 0.242 | 0.214 |
| Public-interest litigation filter | 0.574 | 0.551 | 0.237 | 0.574 | 0.297 | 0.575 | 0.634 | 0.169 | 0.666 | 0.550 | 0.131 | 0.102 | 0.523 | 0.098 | 0.227 | 0.233 | 0.238 |
| Nonpartisan commission appointments | 0.574 | 0.549 | 0.235 | 0.574 | 0.297 | 0.575 | 0.629 | 0.165 | 0.657 | 0.549 | 0.130 | 0.103 | 0.518 | 0.100 | 0.228 | 0.239 | 0.214 |
| Constitutional remand with override window | 0.573 | 0.554 | 0.236 | 0.574 | 0.262 | 0.593 | 0.623 | 0.137 | 0.727 | 0.566 | 0.130 | 0.116 | 0.555 | 0.069 | 0.237 | 0.233 | 0.334 |
| Mandatory written emergency reasoning | 0.573 | 0.543 | 0.231 | 0.574 | 0.297 | 0.574 | 0.625 | 0.155 | 0.673 | 0.550 | 0.130 | 0.115 | 0.503 | 0.069 | 0.234 | 0.245 | 0.228 |
| Peer recusal + reasoned emergency docket | 0.573 | 0.544 | 0.232 | 0.574 | 0.297 | 0.575 | 0.628 | 0.163 | 0.657 | 0.550 | 0.129 | 0.102 | 0.508 | 0.099 | 0.226 | 0.246 | 0.220 |
| Retention-election accountability court | 0.573 | 0.549 | 0.236 | 0.574 | 0.297 | 0.576 | 0.620 | 0.159 | 0.662 | 0.549 | 0.135 | 0.101 | 0.521 | 0.098 | 0.227 | 0.240 | 0.214 |
| Automatic merits follow-up for emergency relief | 0.572 | 0.545 | 0.233 | 0.574 | 0.293 | 0.580 | 0.638 | 0.202 | 0.621 | 0.556 | 0.130 | 0.082 | 0.554 | 0.026 | 0.211 | 0.241 | 0.245 |
| Three-judge panels with en banc correction | 0.572 | 0.552 | 0.238 | 0.574 | 0.297 | 0.575 | 0.630 | 0.164 | 0.662 | 0.549 | 0.130 | 0.103 | 0.559 | 0.100 | 0.227 | 0.237 | 0.230 |
| Emergency integrity package | 0.571 | 0.551 | 0.239 | 0.574 | 0.293 | 0.580 | 0.639 | 0.198 | 0.634 | 0.557 | 0.129 | 0.083 | 0.585 | 0.027 | 0.214 | 0.233 | 0.269 |
| Randomized merits panels with en banc correction | 0.571 | 0.550 | 0.234 | 0.574 | 0.297 | 0.575 | 0.630 | 0.164 | 0.664 | 0.549 | 0.130 | 0.103 | 0.560 | 0.099 | 0.227 | 0.237 | 0.237 |
| Independent recusal enforcement with substitutes | 0.571 | 0.546 | 0.233 | 0.574 | 0.297 | 0.575 | 0.628 | 0.163 | 0.657 | 0.549 | 0.130 | 0.102 | 0.532 | 0.099 | 0.227 | 0.239 | 0.234 |
| Expanded 15-seat court | 0.571 | 0.542 | 0.230 | 0.574 | 0.297 | 0.575 | 0.627 | 0.162 | 0.649 | 0.551 | 0.128 | 0.102 | 0.514 | 0.098 | 0.228 | 0.245 | 0.226 |
| Time-limited legislative override window | 0.570 | 0.545 | 0.230 | 0.574 | 0.298 | 0.576 | 0.629 | 0.163 | 0.658 | 0.546 | 0.140 | 0.102 | 0.521 | 0.099 | 0.226 | 0.247 | 0.220 |
| Comparative 16-seat constitutional senates | 0.570 | 0.544 | 0.231 | 0.574 | 0.298 | 0.573 | 0.619 | 0.132 | 0.704 | 0.550 | 0.127 | 0.117 | 0.551 | 0.091 | 0.236 | 0.236 | 0.259 |
| Judicial review with legislative supermajority override | 0.570 | 0.549 | 0.236 | 0.574 | 0.298 | 0.575 | 0.631 | 0.165 | 0.656 | 0.546 | 0.142 | 0.103 | 0.523 | 0.099 | 0.228 | 0.250 | 0.221 |
| Random panels with jurisdiction safeguards | 0.569 | 0.550 | 0.237 | 0.574 | 0.298 | 0.603 | 0.620 | 0.141 | 0.690 | 0.548 | 0.140 | 0.118 | 0.564 | 0.091 | 0.237 | 0.238 | 0.261 |
| Pre-enactment constitutional council | 0.567 | 0.549 | 0.236 | 0.574 | 0.295 | 0.619 | 0.630 | 0.160 | 0.668 | 0.554 | 0.135 | 0.102 | 0.583 | 0.099 | 0.227 | 0.245 | 0.293 |
| Constitutional council with concrete-review backstop | 0.566 | 0.548 | 0.234 | 0.574 | 0.295 | 0.619 | 0.629 | 0.154 | 0.677 | 0.555 | 0.136 | 0.101 | 0.587 | 0.098 | 0.226 | 0.244 | 0.306 |
| Stylized current U.S.-like supreme court | 0.563 | 0.544 | 0.232 | 0.574 | 0.308 | 0.566 | 0.638 | 0.180 | 0.622 | 0.527 | 0.164 | 0.170 | 0.361 | 0.292 | 0.303 | 0.277 | 0.152 |
| Supreme court with cross-checking constitutional court | 0.561 | 0.548 | 0.233 | 0.574 | 0.277 | 0.593 | 0.604 | 0.097 | 0.709 | 0.555 | 0.129 | 0.117 | 0.519 | 0.091 | 0.238 | 0.234 | 0.297 |
| Dual supreme courts with disagreement filter | 0.545 | 0.546 | 0.232 | 0.574 | 0.299 | 0.573 | 0.626 | 0.163 | 0.618 | 0.541 | 0.138 | 0.118 | 0.523 | 0.091 | 0.238 | 0.245 | 0.331 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.380 | 0.137 | 0.323 | 0.351 | 0.641 | 0.174 | 0.257 | 0.177 |
| No emergency relief without merits review | 0.380 | 0.197 | 0.458 | 0.447 | 0.933 | 0.331 | 0.373 | 0.238 |
| Constitutional remand before invalidation | 0.380 | 0.145 | 0.356 | 0.335 | 0.641 | 0.183 | 0.269 | 0.170 |
| 18-year staggered terms + regular appointments | 0.380 | 0.164 | 0.399 | 0.398 | 0.731 | 0.248 | 0.315 | 0.209 |
| Jurisdiction stripping constrained by rights carveouts | 0.380 | 0.164 | 0.395 | 0.400 | 0.740 | 0.216 | 0.337 | 0.193 |
| Public-interest litigation filter | 0.380 | 0.169 | 0.424 | 0.407 | 0.737 | 0.237 | 0.304 | 0.211 |
| Nonpartisan commission appointments | 0.380 | 0.165 | 0.398 | 0.396 | 0.740 | 0.244 | 0.321 | 0.203 |
| Constitutional remand with override window | 0.380 | 0.137 | 0.330 | 0.328 | 0.634 | 0.180 | 0.247 | 0.160 |
| Mandatory written emergency reasoning | 0.380 | 0.155 | 0.368 | 0.389 | 0.726 | 0.248 | 0.287 | 0.195 |
| Peer recusal + reasoned emergency docket | 0.380 | 0.163 | 0.394 | 0.390 | 0.747 | 0.250 | 0.306 | 0.197 |
| Retention-election accountability court | 0.380 | 0.159 | 0.387 | 0.370 | 0.713 | 0.212 | 0.295 | 0.181 |
| Automatic merits follow-up for emergency relief | 0.380 | 0.202 | 0.469 | 0.480 | 0.952 | 0.347 | 0.458 | 0.254 |
| Three-judge panels with en banc correction | 0.380 | 0.164 | 0.401 | 0.399 | 0.730 | 0.229 | 0.322 | 0.195 |
| Emergency integrity package | 0.380 | 0.198 | 0.464 | 0.448 | 0.933 | 0.319 | 0.387 | 0.246 |
| Randomized merits panels with en banc correction | 0.380 | 0.164 | 0.400 | 0.403 | 0.733 | 0.211 | 0.315 | 0.205 |
| Independent recusal enforcement with substitutes | 0.380 | 0.163 | 0.395 | 0.404 | 0.728 | 0.234 | 0.323 | 0.220 |
| Expanded 15-seat court | 0.380 | 0.162 | 0.389 | 0.395 | 0.743 | 0.226 | 0.302 | 0.198 |
| Time-limited legislative override window | 0.380 | 0.163 | 0.394 | 0.391 | 0.736 | 0.224 | 0.317 | 0.200 |
| Comparative 16-seat constitutional senates | 0.380 | 0.132 | 0.313 | 0.311 | 0.616 | 0.152 | 0.240 | 0.139 |
| Judicial review with legislative supermajority override | 0.380 | 0.165 | 0.399 | 0.399 | 0.736 | 0.227 | 0.330 | 0.204 |
| Random panels with jurisdiction safeguards | 0.380 | 0.141 | 0.335 | 0.377 | 0.650 | 0.185 | 0.257 | 0.181 |
| Pre-enactment constitutional council | 0.380 | 0.160 | 0.391 | 0.352 | 0.722 | 0.194 | 0.299 | 0.185 |
| Constitutional council with concrete-review backstop | 0.380 | 0.154 | 0.372 | 0.338 | 0.691 | 0.185 | 0.276 | 0.166 |
| Stylized current U.S.-like supreme court | 0.380 | 0.180 | 0.401 | 0.407 | 0.951 | 0.340 | 0.390 | 0.214 |
| Supreme court with cross-checking constitutional court | 0.380 | 0.097 | 0.235 | 0.280 | 0.420 | 0.141 | 0.195 | 0.134 |
| Dual supreme courts with disagreement filter | 0.380 | 0.163 | 0.382 | 0.417 | 0.753 | 0.208 | 0.329 | 0.217 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | No emergency relief without merits review (0.609) | Automatic merits follow-up for emergency relief (0.649) | No emergency relief without merits review (0.011) | Time-limited legislative override window (0.015) |
| Partisan Appointment Pressure | No emergency relief without merits review (0.610) | No emergency relief without merits review (0.648) | No emergency relief without merits review (0.011) | Dual supreme courts with disagreement filter (0.017) |
| Rights-Risk Legislation | Constitutional remand before invalidation (0.550) | No emergency relief without merits review (0.611) | No emergency relief without merits review (0.018) | Dual supreme courts with disagreement filter (0.020) |
| Shadow-Docket Stress | 60 percent invalidation threshold (0.547) | Stylized current U.S.-like supreme court (0.667) | No emergency relief without merits review (0.037) | Time-limited legislative override window (0.022) |
| High Democratic Mandate | No emergency relief without merits review (0.630) | Public-interest litigation filter (0.649) | No emergency relief without merits review (0.008) | Dual supreme courts with disagreement filter (0.009) |
| Constitutional Conflict | Constitutional remand before invalidation (0.518) | Stylized current U.S.-like supreme court (0.645) | No emergency relief without merits review (0.039) | Time-limited legislative override window (0.034) |
| Imported Legislative Output | No emergency relief without merits review (0.616) | Emergency integrity package (0.654) | No emergency relief without merits review (0.010) | Time-limited legislative override window (0.014) |
| Low Appointment Capture | No emergency relief without merits review (0.611) | Automatic merits follow-up for emergency relief (0.650) | No emergency relief without merits review (0.011) | Time-limited legislative override window (0.010) |
| Extreme Appointment Capture | No emergency relief without merits review (0.609) | Automatic merits follow-up for emergency relief (0.651) | No emergency relief without merits review (0.011) | Time-limited legislative override window (0.021) |
| Low Emergency Pressure | No emergency relief without merits review (0.615) | Public-interest litigation filter (0.649) | No emergency relief without merits review (0.009) | Dual supreme courts with disagreement filter (0.014) |
| Extreme Emergency Pressure | 60 percent invalidation threshold (0.522) | Stylized current U.S.-like supreme court (0.669) | No emergency relief without merits review (0.049) | Time-limited legislative override window (0.029) |
| Low Rights Risk | No emergency relief without merits review (0.637) | Public-interest litigation filter (0.650) | No emergency relief without merits review (0.006) | Time-limited legislative override window (0.009) |
| Extreme Rights Risk | No emergency relief without merits review (0.520) | Emergency integrity package (0.603) | No emergency relief without merits review (0.027) | Time-limited legislative override window (0.027) |
| Weak-Mandate Legislation | 60 percent invalidation threshold (0.538) | Stylized current U.S.-like supreme court (0.623) | No emergency relief without merits review (0.020) | Jurisdiction stripping constrained by rights carveouts (0.018) |
| Strong-Mandate Legislation | No emergency relief without merits review (0.636) | Judicial review with legislative supermajority override (0.647) | No emergency relief without merits review (0.007) | Dual supreme courts with disagreement filter (0.010) |
