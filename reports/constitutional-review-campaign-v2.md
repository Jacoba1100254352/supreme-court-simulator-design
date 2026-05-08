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

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.569); Constitutional remand before invalidation (0.566); No emergency relief without merits review (0.565); 18-year staggered terms + regular appointments (0.564); Constitutional remand with override window (0.563); Public-interest litigation filter (0.563); Jurisdiction stripping constrained by rights carveouts (0.562); Nonpartisan commission appointments (0.561); Mandatory written emergency reasoning (0.561); Peer recusal + reasoned emergency docket (0.560); Retention-election accountability court (0.560); Three-judge panels with en banc correction (0.560); Comparative 16-seat constitutional senates (0.559); Randomized merits panels with en banc correction (0.559); Independent recusal enforcement with substitutes (0.559); Automatic merits follow-up for emergency relief (0.559). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.569.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.638.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.023.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.223.
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
| 60 percent invalidation threshold | 0.569 | 0.555 | 0.237 | 0.589 | 0.322 | 0.560 | 0.616 | 0.145 | 0.676 | 0.533 | 0.145 | 0.132 | 0.481 | 0.100 | 0.251 | 0.258 | 0.192 |
| Constitutional remand before invalidation | 0.566 | 0.565 | 0.242 | 0.589 | 0.285 | 0.582 | 0.623 | 0.153 | 0.700 | 0.552 | 0.148 | 0.115 | 0.553 | 0.108 | 0.242 | 0.247 | 0.311 |
| No emergency relief without merits review | 0.565 | 0.559 | 0.239 | 0.589 | 0.317 | 0.568 | 0.637 | 0.213 | 0.603 | 0.541 | 0.151 | 0.089 | 0.583 | 0.023 | 0.223 | 0.246 | 0.235 |
| 18-year staggered terms + regular appointments | 0.564 | 0.556 | 0.238 | 0.589 | 0.321 | 0.562 | 0.625 | 0.173 | 0.629 | 0.534 | 0.151 | 0.115 | 0.499 | 0.107 | 0.241 | 0.261 | 0.196 |
| Constitutional remand with override window | 0.563 | 0.565 | 0.241 | 0.589 | 0.286 | 0.582 | 0.620 | 0.144 | 0.716 | 0.551 | 0.149 | 0.131 | 0.552 | 0.078 | 0.251 | 0.247 | 0.342 |
| Public-interest litigation filter | 0.563 | 0.561 | 0.241 | 0.589 | 0.320 | 0.563 | 0.630 | 0.178 | 0.643 | 0.535 | 0.149 | 0.114 | 0.519 | 0.107 | 0.241 | 0.247 | 0.243 |
| Jurisdiction stripping constrained by rights carveouts | 0.562 | 0.558 | 0.237 | 0.589 | 0.321 | 0.592 | 0.626 | 0.174 | 0.630 | 0.534 | 0.164 | 0.115 | 0.527 | 0.108 | 0.240 | 0.259 | 0.218 |
| Nonpartisan commission appointments | 0.561 | 0.561 | 0.241 | 0.589 | 0.321 | 0.562 | 0.626 | 0.174 | 0.631 | 0.533 | 0.151 | 0.115 | 0.516 | 0.108 | 0.241 | 0.254 | 0.219 |
| Mandatory written emergency reasoning | 0.561 | 0.556 | 0.237 | 0.589 | 0.321 | 0.562 | 0.621 | 0.164 | 0.649 | 0.533 | 0.151 | 0.130 | 0.498 | 0.078 | 0.249 | 0.260 | 0.234 |
| Peer recusal + reasoned emergency docket | 0.560 | 0.555 | 0.234 | 0.589 | 0.321 | 0.562 | 0.625 | 0.172 | 0.631 | 0.534 | 0.150 | 0.115 | 0.505 | 0.107 | 0.240 | 0.260 | 0.225 |
| Retention-election accountability court | 0.560 | 0.559 | 0.238 | 0.589 | 0.321 | 0.563 | 0.616 | 0.170 | 0.636 | 0.533 | 0.155 | 0.113 | 0.517 | 0.107 | 0.241 | 0.254 | 0.218 |
| Three-judge panels with en banc correction | 0.560 | 0.561 | 0.240 | 0.589 | 0.320 | 0.563 | 0.626 | 0.173 | 0.638 | 0.535 | 0.148 | 0.116 | 0.555 | 0.108 | 0.240 | 0.251 | 0.235 |
| Comparative 16-seat constitutional senates | 0.559 | 0.554 | 0.235 | 0.589 | 0.322 | 0.560 | 0.616 | 0.139 | 0.688 | 0.535 | 0.144 | 0.132 | 0.547 | 0.099 | 0.250 | 0.250 | 0.265 |
| Randomized merits panels with en banc correction | 0.559 | 0.559 | 0.236 | 0.589 | 0.321 | 0.562 | 0.626 | 0.173 | 0.638 | 0.534 | 0.150 | 0.115 | 0.556 | 0.108 | 0.239 | 0.251 | 0.241 |
| Independent recusal enforcement with substitutes | 0.559 | 0.558 | 0.237 | 0.589 | 0.321 | 0.562 | 0.626 | 0.174 | 0.630 | 0.534 | 0.150 | 0.115 | 0.530 | 0.108 | 0.241 | 0.253 | 0.240 |
| Automatic merits follow-up for emergency relief | 0.559 | 0.554 | 0.234 | 0.589 | 0.317 | 0.568 | 0.635 | 0.216 | 0.585 | 0.540 | 0.154 | 0.090 | 0.555 | 0.030 | 0.223 | 0.257 | 0.250 |
| Expanded 15-seat court | 0.558 | 0.557 | 0.238 | 0.589 | 0.321 | 0.562 | 0.625 | 0.172 | 0.623 | 0.534 | 0.149 | 0.115 | 0.512 | 0.108 | 0.244 | 0.260 | 0.232 |
| Emergency integrity package | 0.558 | 0.560 | 0.239 | 0.589 | 0.317 | 0.568 | 0.637 | 0.214 | 0.597 | 0.541 | 0.151 | 0.091 | 0.587 | 0.031 | 0.225 | 0.248 | 0.274 |
| Time-limited legislative override window | 0.558 | 0.558 | 0.237 | 0.589 | 0.322 | 0.564 | 0.627 | 0.173 | 0.631 | 0.531 | 0.159 | 0.115 | 0.519 | 0.108 | 0.241 | 0.263 | 0.226 |
| Random panels with jurisdiction safeguards | 0.558 | 0.559 | 0.238 | 0.589 | 0.322 | 0.590 | 0.616 | 0.148 | 0.670 | 0.533 | 0.158 | 0.132 | 0.560 | 0.100 | 0.250 | 0.253 | 0.266 |
| Judicial review with legislative supermajority override | 0.557 | 0.559 | 0.238 | 0.589 | 0.322 | 0.563 | 0.627 | 0.173 | 0.630 | 0.531 | 0.161 | 0.115 | 0.520 | 0.108 | 0.241 | 0.264 | 0.226 |
| Stylized current U.S.-like supreme court | 0.555 | 0.555 | 0.235 | 0.589 | 0.329 | 0.553 | 0.638 | 0.196 | 0.599 | 0.517 | 0.162 | 0.185 | 0.356 | 0.303 | 0.311 | 0.288 | 0.155 |
| Constitutional council with concrete-review backstop | 0.555 | 0.557 | 0.235 | 0.589 | 0.319 | 0.607 | 0.627 | 0.162 | 0.659 | 0.540 | 0.156 | 0.113 | 0.586 | 0.107 | 0.239 | 0.258 | 0.314 |
| Pre-enactment constitutional council | 0.555 | 0.562 | 0.242 | 0.589 | 0.319 | 0.607 | 0.628 | 0.171 | 0.644 | 0.538 | 0.158 | 0.115 | 0.582 | 0.108 | 0.241 | 0.261 | 0.301 |
| Supreme court with cross-checking constitutional court | 0.550 | 0.559 | 0.239 | 0.589 | 0.301 | 0.580 | 0.599 | 0.101 | 0.697 | 0.540 | 0.148 | 0.132 | 0.517 | 0.100 | 0.251 | 0.248 | 0.303 |
| Dual supreme courts with disagreement filter | 0.531 | 0.558 | 0.237 | 0.589 | 0.323 | 0.560 | 0.623 | 0.172 | 0.587 | 0.525 | 0.156 | 0.134 | 0.520 | 0.101 | 0.253 | 0.259 | 0.338 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.397 | 0.145 | 0.330 | 0.364 | 0.639 | 0.194 | 0.297 | 0.174 |
| Constitutional remand before invalidation | 0.397 | 0.153 | 0.361 | 0.358 | 0.646 | 0.211 | 0.301 | 0.183 |
| No emergency relief without merits review | 0.397 | 0.213 | 0.480 | 0.473 | 0.945 | 0.335 | 0.430 | 0.260 |
| 18-year staggered terms + regular appointments | 0.397 | 0.173 | 0.405 | 0.409 | 0.737 | 0.250 | 0.346 | 0.226 |
| Constitutional remand with override window | 0.397 | 0.144 | 0.335 | 0.344 | 0.636 | 0.187 | 0.293 | 0.171 |
| Public-interest litigation filter | 0.397 | 0.178 | 0.422 | 0.435 | 0.747 | 0.247 | 0.341 | 0.221 |
| Jurisdiction stripping constrained by rights carveouts | 0.397 | 0.174 | 0.406 | 0.414 | 0.738 | 0.239 | 0.368 | 0.213 |
| Nonpartisan commission appointments | 0.397 | 0.174 | 0.402 | 0.420 | 0.742 | 0.257 | 0.364 | 0.226 |
| Mandatory written emergency reasoning | 0.397 | 0.164 | 0.374 | 0.405 | 0.722 | 0.238 | 0.328 | 0.212 |
| Peer recusal + reasoned emergency docket | 0.397 | 0.172 | 0.398 | 0.407 | 0.743 | 0.272 | 0.344 | 0.221 |
| Retention-election accountability court | 0.397 | 0.170 | 0.399 | 0.389 | 0.722 | 0.235 | 0.331 | 0.208 |
| Three-judge panels with en banc correction | 0.397 | 0.173 | 0.408 | 0.407 | 0.738 | 0.244 | 0.338 | 0.216 |
| Comparative 16-seat constitutional senates | 0.397 | 0.139 | 0.318 | 0.320 | 0.622 | 0.153 | 0.252 | 0.162 |
| Randomized merits panels with en banc correction | 0.397 | 0.173 | 0.404 | 0.419 | 0.737 | 0.230 | 0.346 | 0.220 |
| Independent recusal enforcement with substitutes | 0.397 | 0.174 | 0.406 | 0.426 | 0.739 | 0.241 | 0.358 | 0.224 |
| Automatic merits follow-up for emergency relief | 0.397 | 0.216 | 0.486 | 0.502 | 0.960 | 0.375 | 0.486 | 0.278 |
| Expanded 15-seat court | 0.397 | 0.172 | 0.400 | 0.415 | 0.741 | 0.240 | 0.356 | 0.215 |
| Emergency integrity package | 0.397 | 0.214 | 0.483 | 0.472 | 0.944 | 0.345 | 0.449 | 0.265 |
| Time-limited legislative override window | 0.397 | 0.173 | 0.404 | 0.416 | 0.743 | 0.249 | 0.340 | 0.217 |
| Random panels with jurisdiction safeguards | 0.397 | 0.148 | 0.335 | 0.379 | 0.651 | 0.210 | 0.295 | 0.199 |
| Judicial review with legislative supermajority override | 0.397 | 0.173 | 0.405 | 0.414 | 0.734 | 0.244 | 0.363 | 0.217 |
| Stylized current U.S.-like supreme court | 0.397 | 0.196 | 0.425 | 0.438 | 0.962 | 0.356 | 0.421 | 0.241 |
| Constitutional council with concrete-review backstop | 0.397 | 0.162 | 0.381 | 0.360 | 0.695 | 0.190 | 0.290 | 0.183 |
| Pre-enactment constitutional council | 0.397 | 0.171 | 0.402 | 0.387 | 0.726 | 0.232 | 0.322 | 0.194 |
| Supreme court with cross-checking constitutional court | 0.397 | 0.101 | 0.235 | 0.283 | 0.413 | 0.145 | 0.198 | 0.138 |
| Dual supreme courts with disagreement filter | 0.397 | 0.172 | 0.392 | 0.421 | 0.749 | 0.225 | 0.345 | 0.223 |

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
| Appointment Timing Manipulation | No emergency relief without merits review (0.614) | No emergency relief without merits review (0.653) | No emergency relief without merits review (0.010) | Time-limited legislative override window (0.021) |
| Emergency Application Flood | 60 percent invalidation threshold (0.499) | Stylized current U.S.-like supreme court (0.666) | No emergency relief without merits review (0.060) | Time-limited legislative override window (0.039) |
| Override Evasion Loop | Constitutional remand before invalidation (0.525) | Emergency integrity package (0.619) | No emergency relief without merits review (0.029) | Judicial review with legislative supermajority override (0.029) |
| Recusal Pressure Campaign | 60 percent invalidation threshold (0.526) | Stylized current U.S.-like supreme court (0.636) | No emergency relief without merits review (0.035) | Judicial review with legislative supermajority override (0.043) |
| Court Expansion Retaliation | Constitutional remand before invalidation (0.507) | Stylized current U.S.-like supreme court (0.627) | No emergency relief without merits review (0.038) | Time-limited legislative override window (0.045) |
