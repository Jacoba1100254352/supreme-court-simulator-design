# Constitutional Review Campaign v2

Deterministic simulation study for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 27
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
| Imported Legislative Output | 1.000 | neutral/imported blend | Docket assumptions derived from an imported legislative-output profile. |
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

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.569); Constitutional remand before invalidation (0.566); No emergency relief without merits review (0.566); 18-year staggered terms + regular appointments (0.565); Constitutional remand with override window (0.563); Public-interest litigation filter (0.563); Jurisdiction stripping constrained by rights carveouts (0.563); Nonpartisan commission appointments (0.562); Mandatory written emergency reasoning (0.561); Peer recusal + reasoned emergency docket (0.561); Three-judge panels with en banc correction (0.561); Retention-election accountability court (0.561); Automatic merits follow-up for emergency relief (0.560); Randomized merits panels with en banc correction (0.560); Comparative 16-seat constitutional senates (0.559); Independent recusal enforcement with substitutes (0.559); Expanded 15-seat court (0.559); Emergency integrity package (0.559). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.569.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.634.
- Lowest emergency-process irregularity: No emergency relief without merits review at 0.022.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.220.
- Lowest partisan alignment: Time-limited legislative override window at 0.022.
- Highest modeled process-legitimacy index: Emergency integrity package at 0.575.
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
| 60 percent invalidation threshold | 0.569 | 0.531 | 0.193 | 0.589 | 0.322 | 0.559 | 0.612 | 0.138 | 0.676 | 0.536 | 0.143 | 0.130 | 0.472 | 0.098 | 0.247 | 0.256 | 0.187 |
| Constitutional remand before invalidation | 0.566 | 0.542 | 0.201 | 0.589 | 0.286 | 0.580 | 0.619 | 0.148 | 0.698 | 0.554 | 0.145 | 0.113 | 0.541 | 0.106 | 0.238 | 0.246 | 0.302 |
| No emergency relief without merits review | 0.566 | 0.536 | 0.197 | 0.589 | 0.317 | 0.567 | 0.633 | 0.206 | 0.605 | 0.543 | 0.146 | 0.088 | 0.571 | 0.022 | 0.220 | 0.245 | 0.229 |
| 18-year staggered terms + regular appointments | 0.565 | 0.529 | 0.190 | 0.589 | 0.321 | 0.561 | 0.620 | 0.166 | 0.633 | 0.536 | 0.147 | 0.112 | 0.488 | 0.105 | 0.236 | 0.258 | 0.190 |
| Constitutional remand with override window | 0.563 | 0.540 | 0.197 | 0.589 | 0.286 | 0.580 | 0.616 | 0.140 | 0.711 | 0.553 | 0.146 | 0.129 | 0.540 | 0.077 | 0.247 | 0.246 | 0.332 |
| Public-interest litigation filter | 0.563 | 0.538 | 0.200 | 0.589 | 0.321 | 0.561 | 0.627 | 0.174 | 0.643 | 0.537 | 0.147 | 0.112 | 0.509 | 0.106 | 0.238 | 0.246 | 0.237 |
| Jurisdiction stripping constrained by rights carveouts | 0.563 | 0.534 | 0.195 | 0.589 | 0.321 | 0.591 | 0.622 | 0.167 | 0.633 | 0.536 | 0.161 | 0.113 | 0.515 | 0.106 | 0.237 | 0.257 | 0.213 |
| Nonpartisan commission appointments | 0.562 | 0.534 | 0.193 | 0.589 | 0.321 | 0.561 | 0.621 | 0.167 | 0.633 | 0.536 | 0.148 | 0.113 | 0.504 | 0.107 | 0.237 | 0.252 | 0.213 |
| Mandatory written emergency reasoning | 0.561 | 0.533 | 0.196 | 0.589 | 0.322 | 0.561 | 0.618 | 0.158 | 0.649 | 0.535 | 0.148 | 0.128 | 0.489 | 0.076 | 0.245 | 0.258 | 0.228 |
| Peer recusal + reasoned emergency docket | 0.561 | 0.530 | 0.192 | 0.589 | 0.321 | 0.561 | 0.620 | 0.165 | 0.632 | 0.536 | 0.146 | 0.112 | 0.495 | 0.106 | 0.236 | 0.258 | 0.219 |
| Three-judge panels with en banc correction | 0.561 | 0.535 | 0.193 | 0.589 | 0.321 | 0.561 | 0.622 | 0.167 | 0.638 | 0.536 | 0.146 | 0.114 | 0.541 | 0.107 | 0.237 | 0.250 | 0.229 |
| Retention-election accountability court | 0.561 | 0.536 | 0.197 | 0.589 | 0.322 | 0.562 | 0.612 | 0.164 | 0.636 | 0.535 | 0.152 | 0.113 | 0.506 | 0.106 | 0.238 | 0.253 | 0.213 |
| Automatic merits follow-up for emergency relief | 0.560 | 0.532 | 0.194 | 0.589 | 0.317 | 0.567 | 0.631 | 0.210 | 0.588 | 0.542 | 0.148 | 0.089 | 0.545 | 0.030 | 0.221 | 0.255 | 0.244 |
| Randomized merits panels with en banc correction | 0.560 | 0.535 | 0.193 | 0.589 | 0.321 | 0.561 | 0.622 | 0.166 | 0.639 | 0.536 | 0.146 | 0.114 | 0.543 | 0.107 | 0.237 | 0.249 | 0.236 |
| Comparative 16-seat constitutional senates | 0.559 | 0.533 | 0.196 | 0.589 | 0.322 | 0.559 | 0.612 | 0.135 | 0.687 | 0.536 | 0.143 | 0.130 | 0.535 | 0.098 | 0.247 | 0.250 | 0.259 |
| Independent recusal enforcement with substitutes | 0.559 | 0.534 | 0.194 | 0.589 | 0.321 | 0.561 | 0.621 | 0.167 | 0.632 | 0.536 | 0.148 | 0.113 | 0.519 | 0.106 | 0.238 | 0.252 | 0.234 |
| Expanded 15-seat court | 0.559 | 0.532 | 0.195 | 0.589 | 0.321 | 0.561 | 0.621 | 0.166 | 0.626 | 0.536 | 0.146 | 0.113 | 0.500 | 0.106 | 0.241 | 0.258 | 0.226 |
| Emergency integrity package | 0.559 | 0.536 | 0.196 | 0.589 | 0.317 | 0.567 | 0.633 | 0.208 | 0.598 | 0.543 | 0.146 | 0.089 | 0.575 | 0.030 | 0.222 | 0.246 | 0.266 |
| Time-limited legislative override window | 0.559 | 0.534 | 0.194 | 0.589 | 0.322 | 0.563 | 0.622 | 0.167 | 0.633 | 0.533 | 0.156 | 0.113 | 0.508 | 0.107 | 0.238 | 0.261 | 0.220 |
| Judicial review with legislative supermajority override | 0.558 | 0.535 | 0.196 | 0.589 | 0.322 | 0.562 | 0.623 | 0.168 | 0.631 | 0.532 | 0.158 | 0.113 | 0.509 | 0.106 | 0.238 | 0.264 | 0.220 |
| Random panels with jurisdiction safeguards | 0.558 | 0.537 | 0.197 | 0.589 | 0.322 | 0.589 | 0.613 | 0.144 | 0.669 | 0.535 | 0.156 | 0.131 | 0.547 | 0.099 | 0.248 | 0.252 | 0.260 |
| Constitutional council with concrete-review backstop | 0.556 | 0.535 | 0.196 | 0.589 | 0.319 | 0.605 | 0.623 | 0.157 | 0.658 | 0.542 | 0.152 | 0.111 | 0.574 | 0.105 | 0.236 | 0.257 | 0.306 |
| Pre-enactment constitutional council | 0.556 | 0.537 | 0.199 | 0.589 | 0.320 | 0.605 | 0.623 | 0.163 | 0.645 | 0.540 | 0.153 | 0.113 | 0.567 | 0.106 | 0.237 | 0.258 | 0.293 |
| Judicial electorate selection court | 0.554 | 0.539 | 0.199 | 0.589 | 0.321 | 0.561 | 0.623 | 0.169 | 0.634 | 0.535 | 0.148 | 0.114 | 0.526 | 0.107 | 0.240 | 0.246 | 0.275 |
| Stylized current U.S.-like supreme court | 0.552 | 0.533 | 0.195 | 0.589 | 0.332 | 0.552 | 0.634 | 0.190 | 0.599 | 0.514 | 0.181 | 0.186 | 0.345 | 0.306 | 0.314 | 0.290 | 0.152 |
| Supreme court with cross-checking constitutional court | 0.551 | 0.534 | 0.194 | 0.589 | 0.302 | 0.579 | 0.596 | 0.097 | 0.694 | 0.542 | 0.145 | 0.129 | 0.506 | 0.098 | 0.246 | 0.246 | 0.295 |
| Dual supreme courts with disagreement filter | 0.532 | 0.535 | 0.195 | 0.589 | 0.324 | 0.559 | 0.620 | 0.167 | 0.588 | 0.526 | 0.157 | 0.131 | 0.509 | 0.099 | 0.249 | 0.258 | 0.330 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.397 | 0.138 | 0.312 | 0.356 | 0.644 | 0.179 | 0.275 | 0.156 |
| Constitutional remand before invalidation | 0.397 | 0.148 | 0.348 | 0.341 | 0.643 | 0.189 | 0.280 | 0.171 |
| No emergency relief without merits review | 0.397 | 0.206 | 0.460 | 0.452 | 0.944 | 0.317 | 0.439 | 0.230 |
| 18-year staggered terms + regular appointments | 0.397 | 0.166 | 0.384 | 0.407 | 0.738 | 0.220 | 0.317 | 0.199 |
| Constitutional remand with override window | 0.397 | 0.140 | 0.324 | 0.334 | 0.633 | 0.169 | 0.267 | 0.160 |
| Public-interest litigation filter | 0.397 | 0.174 | 0.410 | 0.417 | 0.750 | 0.238 | 0.322 | 0.197 |
| Jurisdiction stripping constrained by rights carveouts | 0.397 | 0.167 | 0.386 | 0.400 | 0.742 | 0.224 | 0.331 | 0.191 |
| Nonpartisan commission appointments | 0.397 | 0.167 | 0.388 | 0.398 | 0.734 | 0.238 | 0.330 | 0.193 |
| Mandatory written emergency reasoning | 0.397 | 0.158 | 0.358 | 0.405 | 0.729 | 0.225 | 0.292 | 0.189 |
| Peer recusal + reasoned emergency docket | 0.397 | 0.165 | 0.379 | 0.402 | 0.732 | 0.236 | 0.328 | 0.203 |
| Three-judge panels with en banc correction | 0.397 | 0.167 | 0.391 | 0.409 | 0.729 | 0.200 | 0.316 | 0.196 |
| Retention-election accountability court | 0.397 | 0.164 | 0.384 | 0.379 | 0.718 | 0.220 | 0.319 | 0.188 |
| Automatic merits follow-up for emergency relief | 0.397 | 0.210 | 0.468 | 0.491 | 0.961 | 0.345 | 0.469 | 0.249 |
| Randomized merits panels with en banc correction | 0.397 | 0.166 | 0.384 | 0.397 | 0.739 | 0.208 | 0.318 | 0.194 |
| Comparative 16-seat constitutional senates | 0.397 | 0.135 | 0.306 | 0.312 | 0.625 | 0.155 | 0.229 | 0.136 |
| Independent recusal enforcement with substitutes | 0.397 | 0.167 | 0.387 | 0.402 | 0.730 | 0.233 | 0.339 | 0.198 |
| Expanded 15-seat court | 0.397 | 0.166 | 0.385 | 0.402 | 0.731 | 0.222 | 0.337 | 0.199 |
| Emergency integrity package | 0.397 | 0.208 | 0.467 | 0.462 | 0.946 | 0.330 | 0.423 | 0.239 |
| Time-limited legislative override window | 0.397 | 0.167 | 0.388 | 0.385 | 0.738 | 0.214 | 0.315 | 0.204 |
| Judicial review with legislative supermajority override | 0.397 | 0.168 | 0.386 | 0.392 | 0.742 | 0.249 | 0.337 | 0.210 |
| Random panels with jurisdiction safeguards | 0.397 | 0.144 | 0.326 | 0.364 | 0.657 | 0.168 | 0.281 | 0.169 |
| Constitutional council with concrete-review backstop | 0.397 | 0.157 | 0.367 | 0.347 | 0.699 | 0.181 | 0.278 | 0.166 |
| Pre-enactment constitutional council | 0.397 | 0.163 | 0.378 | 0.380 | 0.727 | 0.211 | 0.315 | 0.179 |
| Judicial electorate selection court | 0.397 | 0.169 | 0.395 | 0.389 | 0.739 | 0.231 | 0.335 | 0.210 |
| Stylized current U.S.-like supreme court | 0.397 | 0.190 | 0.406 | 0.422 | 0.961 | 0.341 | 0.406 | 0.218 |
| Supreme court with cross-checking constitutional court | 0.397 | 0.097 | 0.226 | 0.251 | 0.422 | 0.127 | 0.190 | 0.123 |
| Dual supreme courts with disagreement filter | 0.397 | 0.167 | 0.377 | 0.396 | 0.764 | 0.225 | 0.349 | 0.204 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest emerg. irregularity | Lowest partisan align. |
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
| Appointment Timing Manipulation | No emergency relief without merits review (0.613) | Emergency integrity package (0.647) | No emergency relief without merits review (0.010) | Jurisdiction stripping constrained by rights carveouts (0.020) |
| Emergency Application Flood | 60 percent invalidation threshold (0.499) | Stylized current U.S.-like supreme court (0.666) | No emergency relief without merits review (0.059) | Jurisdiction stripping constrained by rights carveouts (0.038) |
| Override Evasion Loop | 60 percent invalidation threshold (0.524) | Emergency integrity package (0.615) | No emergency relief without merits review (0.029) | Judicial review with legislative supermajority override (0.028) |
| Recusal Pressure Campaign | 60 percent invalidation threshold (0.526) | Stylized current U.S.-like supreme court (0.633) | No emergency relief without merits review (0.035) | Time-limited legislative override window (0.041) |
| Court Expansion Retaliation | Constitutional remand before invalidation (0.508) | Stylized current U.S.-like supreme court (0.626) | No emergency relief without merits review (0.038) | Judicial review with legislative supermajority override (0.044) |
