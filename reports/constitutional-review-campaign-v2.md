# Constitutional Review Campaign v2

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 26
- experiment cases: 20

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
| Appointment Timing Manipulation | 1.000 | adversarial/imported blend | Political actors time vacancies under high capture and public pressure. |
| Emergency Application Flood | 1.000 | emergency-flood synthetic legislature | Executives and litigants route controversial policies through urgent stay requests. |
| Override Evasion Loop | 1.000 | override-evasion synthetic legislature | Legislatures repeatedly revise invalidated laws to test rights carveouts and override thresholds. |
| Recusal Pressure Campaign | 0.850 | recusal-pressure synthetic legislature | High-salience litigants try to force or avoid recusals around ideologically charged cases. |
| Court Expansion Retaliation | 0.850 | expansion-retaliation synthetic legislature | A polarized political system reacts to judicial conflict with expansion threats and capture pressure. |

## Headline Findings

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.567); Constitutional remand before invalidation (0.565); No emergency relief without merits review (0.564); 18-year staggered terms + regular appointments (0.563); Constitutional remand with override window (0.562); Public-interest litigation filter (0.562); Jurisdiction stripping constrained by rights carveouts (0.561); Nonpartisan commission appointments (0.560); Mandatory written emergency reasoning (0.560); Peer recusal + reasoned emergency docket (0.560); Retention-election accountability court (0.559); Three-judge panels with en banc correction (0.559); Comparative 16-seat constitutional senates (0.558); Randomized merits panels with en banc correction (0.558); Automatic merits follow-up for emergency relief (0.558); Independent recusal enforcement with substitutes (0.558); Expanded 15-seat court (0.557). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.567.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.638.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.023.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.228.
- Lowest partisan alignment: Time-limited legislative override window at 0.023.
- Highest public confidence index: Emergency integrity package at 0.587.
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
| 60 percent invalidation threshold | 0.567 | 0.556 | 0.237 | 0.589 | 0.322 | 0.560 | 0.616 | 0.143 | 0.676 | 0.532 | 0.148 | 0.134 | 0.480 | 0.101 | 0.256 | 0.259 | 0.193 |
| Constitutional remand before invalidation | 0.565 | 0.565 | 0.243 | 0.589 | 0.285 | 0.582 | 0.624 | 0.153 | 0.701 | 0.552 | 0.148 | 0.116 | 0.551 | 0.110 | 0.247 | 0.248 | 0.312 |
| No emergency relief without merits review | 0.564 | 0.559 | 0.239 | 0.589 | 0.317 | 0.568 | 0.637 | 0.213 | 0.604 | 0.540 | 0.153 | 0.091 | 0.582 | 0.023 | 0.228 | 0.248 | 0.236 |
| 18-year staggered terms + regular appointments | 0.563 | 0.556 | 0.239 | 0.589 | 0.321 | 0.562 | 0.625 | 0.172 | 0.630 | 0.532 | 0.154 | 0.116 | 0.497 | 0.110 | 0.245 | 0.263 | 0.197 |
| Constitutional remand with override window | 0.562 | 0.564 | 0.239 | 0.589 | 0.286 | 0.581 | 0.620 | 0.144 | 0.716 | 0.550 | 0.151 | 0.132 | 0.550 | 0.079 | 0.256 | 0.248 | 0.343 |
| Public-interest litigation filter | 0.562 | 0.561 | 0.241 | 0.589 | 0.321 | 0.563 | 0.631 | 0.178 | 0.643 | 0.534 | 0.152 | 0.115 | 0.518 | 0.109 | 0.245 | 0.249 | 0.244 |
| Jurisdiction stripping constrained by rights carveouts | 0.561 | 0.559 | 0.238 | 0.589 | 0.321 | 0.592 | 0.626 | 0.173 | 0.630 | 0.533 | 0.166 | 0.117 | 0.525 | 0.110 | 0.246 | 0.261 | 0.220 |
| Nonpartisan commission appointments | 0.560 | 0.561 | 0.240 | 0.589 | 0.321 | 0.562 | 0.626 | 0.174 | 0.631 | 0.532 | 0.152 | 0.117 | 0.513 | 0.111 | 0.246 | 0.256 | 0.220 |
| Mandatory written emergency reasoning | 0.560 | 0.554 | 0.235 | 0.589 | 0.321 | 0.562 | 0.621 | 0.162 | 0.650 | 0.533 | 0.152 | 0.131 | 0.497 | 0.078 | 0.253 | 0.261 | 0.235 |
| Peer recusal + reasoned emergency docket | 0.560 | 0.554 | 0.234 | 0.589 | 0.321 | 0.562 | 0.625 | 0.172 | 0.632 | 0.534 | 0.151 | 0.116 | 0.503 | 0.109 | 0.244 | 0.262 | 0.225 |
| Retention-election accountability court | 0.559 | 0.560 | 0.240 | 0.589 | 0.321 | 0.563 | 0.616 | 0.170 | 0.636 | 0.532 | 0.157 | 0.115 | 0.516 | 0.109 | 0.245 | 0.256 | 0.220 |
| Three-judge panels with en banc correction | 0.559 | 0.561 | 0.240 | 0.589 | 0.321 | 0.562 | 0.627 | 0.173 | 0.638 | 0.533 | 0.152 | 0.117 | 0.553 | 0.110 | 0.245 | 0.253 | 0.236 |
| Comparative 16-seat constitutional senates | 0.558 | 0.555 | 0.236 | 0.589 | 0.322 | 0.560 | 0.616 | 0.138 | 0.688 | 0.534 | 0.148 | 0.134 | 0.545 | 0.101 | 0.255 | 0.253 | 0.266 |
| Randomized merits panels with en banc correction | 0.558 | 0.560 | 0.238 | 0.589 | 0.321 | 0.562 | 0.627 | 0.173 | 0.637 | 0.533 | 0.151 | 0.117 | 0.555 | 0.110 | 0.245 | 0.253 | 0.243 |
| Automatic merits follow-up for emergency relief | 0.558 | 0.556 | 0.237 | 0.589 | 0.317 | 0.568 | 0.636 | 0.218 | 0.585 | 0.539 | 0.154 | 0.091 | 0.554 | 0.031 | 0.228 | 0.259 | 0.252 |
| Independent recusal enforcement with substitutes | 0.558 | 0.557 | 0.235 | 0.589 | 0.321 | 0.562 | 0.625 | 0.172 | 0.632 | 0.533 | 0.152 | 0.116 | 0.528 | 0.110 | 0.245 | 0.255 | 0.240 |
| Expanded 15-seat court | 0.557 | 0.554 | 0.235 | 0.589 | 0.321 | 0.562 | 0.625 | 0.171 | 0.624 | 0.534 | 0.150 | 0.116 | 0.510 | 0.109 | 0.247 | 0.262 | 0.232 |
| Emergency integrity package | 0.557 | 0.561 | 0.242 | 0.589 | 0.317 | 0.568 | 0.638 | 0.215 | 0.596 | 0.540 | 0.151 | 0.092 | 0.587 | 0.031 | 0.230 | 0.250 | 0.275 |
| Time-limited legislative override window | 0.557 | 0.556 | 0.235 | 0.589 | 0.322 | 0.564 | 0.627 | 0.172 | 0.631 | 0.530 | 0.163 | 0.116 | 0.517 | 0.110 | 0.245 | 0.265 | 0.226 |
| Random panels with jurisdiction safeguards | 0.556 | 0.560 | 0.241 | 0.589 | 0.322 | 0.590 | 0.617 | 0.147 | 0.671 | 0.532 | 0.162 | 0.134 | 0.559 | 0.102 | 0.256 | 0.255 | 0.267 |
| Judicial review with legislative supermajority override | 0.556 | 0.559 | 0.237 | 0.589 | 0.322 | 0.563 | 0.628 | 0.173 | 0.630 | 0.530 | 0.163 | 0.117 | 0.518 | 0.110 | 0.246 | 0.267 | 0.227 |
| Constitutional council with concrete-review backstop | 0.554 | 0.558 | 0.236 | 0.589 | 0.319 | 0.607 | 0.627 | 0.163 | 0.659 | 0.540 | 0.157 | 0.115 | 0.585 | 0.109 | 0.244 | 0.260 | 0.315 |
| Pre-enactment constitutional council | 0.554 | 0.560 | 0.241 | 0.589 | 0.319 | 0.607 | 0.628 | 0.170 | 0.643 | 0.538 | 0.159 | 0.116 | 0.579 | 0.109 | 0.245 | 0.262 | 0.302 |
| Stylized current U.S.-like supreme court | 0.550 | 0.555 | 0.236 | 0.589 | 0.332 | 0.553 | 0.638 | 0.196 | 0.596 | 0.509 | 0.189 | 0.191 | 0.348 | 0.315 | 0.324 | 0.294 | 0.156 |
| Supreme court with cross-checking constitutional court | 0.549 | 0.559 | 0.238 | 0.589 | 0.301 | 0.580 | 0.600 | 0.101 | 0.696 | 0.540 | 0.149 | 0.134 | 0.515 | 0.102 | 0.256 | 0.250 | 0.304 |
| Dual supreme courts with disagreement filter | 0.530 | 0.557 | 0.237 | 0.589 | 0.324 | 0.560 | 0.623 | 0.172 | 0.586 | 0.524 | 0.161 | 0.135 | 0.519 | 0.102 | 0.258 | 0.262 | 0.339 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.397 | 0.143 | 0.326 | 0.361 | 0.638 | 0.186 | 0.282 | 0.178 |
| Constitutional remand before invalidation | 0.397 | 0.153 | 0.362 | 0.351 | 0.645 | 0.200 | 0.297 | 0.180 |
| No emergency relief without merits review | 0.397 | 0.213 | 0.478 | 0.472 | 0.947 | 0.359 | 0.428 | 0.263 |
| 18-year staggered terms + regular appointments | 0.397 | 0.172 | 0.403 | 0.407 | 0.734 | 0.260 | 0.344 | 0.224 |
| Constitutional remand with override window | 0.397 | 0.144 | 0.334 | 0.341 | 0.634 | 0.190 | 0.273 | 0.168 |
| Public-interest litigation filter | 0.397 | 0.178 | 0.428 | 0.419 | 0.739 | 0.254 | 0.345 | 0.224 |
| Jurisdiction stripping constrained by rights carveouts | 0.397 | 0.173 | 0.403 | 0.413 | 0.738 | 0.233 | 0.360 | 0.210 |
| Nonpartisan commission appointments | 0.397 | 0.174 | 0.404 | 0.412 | 0.741 | 0.255 | 0.349 | 0.217 |
| Mandatory written emergency reasoning | 0.397 | 0.162 | 0.371 | 0.401 | 0.727 | 0.244 | 0.316 | 0.207 |
| Peer recusal + reasoned emergency docket | 0.397 | 0.172 | 0.402 | 0.405 | 0.747 | 0.270 | 0.329 | 0.210 |
| Retention-election accountability court | 0.397 | 0.170 | 0.397 | 0.387 | 0.725 | 0.223 | 0.327 | 0.201 |
| Three-judge panels with en banc correction | 0.397 | 0.173 | 0.406 | 0.409 | 0.728 | 0.241 | 0.348 | 0.210 |
| Comparative 16-seat constitutional senates | 0.397 | 0.138 | 0.317 | 0.318 | 0.619 | 0.163 | 0.266 | 0.153 |
| Randomized merits panels with en banc correction | 0.397 | 0.173 | 0.406 | 0.412 | 0.737 | 0.232 | 0.341 | 0.223 |
| Automatic merits follow-up for emergency relief | 0.397 | 0.218 | 0.488 | 0.506 | 0.961 | 0.364 | 0.494 | 0.279 |
| Independent recusal enforcement with substitutes | 0.397 | 0.172 | 0.402 | 0.416 | 0.727 | 0.244 | 0.346 | 0.227 |
| Expanded 15-seat court | 0.397 | 0.171 | 0.396 | 0.409 | 0.742 | 0.235 | 0.327 | 0.215 |
| Emergency integrity package | 0.397 | 0.215 | 0.486 | 0.473 | 0.946 | 0.346 | 0.427 | 0.268 |
| Time-limited legislative override window | 0.397 | 0.172 | 0.402 | 0.406 | 0.745 | 0.241 | 0.342 | 0.211 |
| Random panels with jurisdiction safeguards | 0.397 | 0.147 | 0.336 | 0.383 | 0.648 | 0.195 | 0.281 | 0.187 |
| Judicial review with legislative supermajority override | 0.397 | 0.173 | 0.405 | 0.409 | 0.736 | 0.236 | 0.354 | 0.220 |
| Constitutional council with concrete-review backstop | 0.397 | 0.163 | 0.382 | 0.348 | 0.698 | 0.192 | 0.302 | 0.179 |
| Pre-enactment constitutional council | 0.397 | 0.170 | 0.400 | 0.377 | 0.725 | 0.212 | 0.336 | 0.201 |
| Stylized current U.S.-like supreme court | 0.397 | 0.196 | 0.423 | 0.434 | 0.961 | 0.363 | 0.426 | 0.237 |
| Supreme court with cross-checking constitutional court | 0.397 | 0.101 | 0.235 | 0.283 | 0.421 | 0.143 | 0.208 | 0.135 |
| Dual supreme courts with disagreement filter | 0.397 | 0.172 | 0.391 | 0.426 | 0.757 | 0.226 | 0.350 | 0.225 |

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
| Appointment Timing Manipulation | No emergency relief without merits review (0.615) | No emergency relief without merits review (0.653) | No emergency relief without merits review (0.010) | Judicial review with legislative supermajority override (0.021) |
| Emergency Application Flood | 60 percent invalidation threshold (0.494) | Stylized current U.S.-like supreme court (0.670) | No emergency relief without merits review (0.060) | Time-limited legislative override window (0.039) |
| Override Evasion Loop | Constitutional remand before invalidation (0.524) | Emergency integrity package (0.622) | No emergency relief without merits review (0.030) | Judicial review with legislative supermajority override (0.029) |
| Recusal Pressure Campaign | 60 percent invalidation threshold (0.522) | Stylized current U.S.-like supreme court (0.637) | No emergency relief without merits review (0.036) | Judicial review with legislative supermajority override (0.043) |
| Court Expansion Retaliation | Constitutional remand before invalidation (0.505) | Stylized current U.S.-like supreme court (0.630) | No emergency relief without merits review (0.039) | Judicial review with legislative supermajority override (0.045) |
