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

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.569); Constitutional remand before invalidation (0.566); No emergency relief without merits review (0.565); 18-year staggered terms + regular appointments (0.565); Constitutional remand with override window (0.563); Public-interest litigation filter (0.563); Jurisdiction stripping constrained by rights carveouts (0.563); Nonpartisan commission appointments (0.562); Mandatory written emergency reasoning (0.561); Peer recusal + reasoned emergency docket (0.561); Three-judge panels with en banc correction (0.561); Retention-election accountability court (0.560); Automatic merits follow-up for emergency relief (0.559); Randomized merits panels with en banc correction (0.559); Comparative 16-seat constitutional senates (0.559); Independent recusal enforcement with substitutes (0.559). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.569.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.634.
- Lowest emergency-process irregularity: No emergency relief without merits review at 0.022.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.222.
- Lowest partisan alignment: Time-limited legislative override window at 0.022.
- Highest modeled process-legitimacy index: Emergency integrity package at 0.577.
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
| 60 percent invalidation threshold | 0.569 | 0.535 | 0.200 | 0.589 | 0.322 | 0.559 | 0.612 | 0.139 | 0.677 | 0.535 | 0.144 | 0.130 | 0.474 | 0.098 | 0.248 | 0.256 | 0.188 |
| Constitutional remand before invalidation | 0.566 | 0.546 | 0.208 | 0.589 | 0.286 | 0.580 | 0.620 | 0.149 | 0.698 | 0.553 | 0.146 | 0.114 | 0.543 | 0.107 | 0.240 | 0.247 | 0.304 |
| No emergency relief without merits review | 0.565 | 0.540 | 0.204 | 0.589 | 0.317 | 0.567 | 0.633 | 0.207 | 0.604 | 0.543 | 0.148 | 0.088 | 0.573 | 0.022 | 0.222 | 0.246 | 0.230 |
| 18-year staggered terms + regular appointments | 0.565 | 0.533 | 0.197 | 0.589 | 0.321 | 0.561 | 0.621 | 0.167 | 0.632 | 0.536 | 0.147 | 0.113 | 0.490 | 0.106 | 0.237 | 0.259 | 0.191 |
| Constitutional remand with override window | 0.563 | 0.545 | 0.205 | 0.589 | 0.286 | 0.580 | 0.617 | 0.141 | 0.711 | 0.552 | 0.145 | 0.129 | 0.542 | 0.077 | 0.249 | 0.246 | 0.334 |
| Public-interest litigation filter | 0.563 | 0.542 | 0.207 | 0.589 | 0.321 | 0.562 | 0.628 | 0.175 | 0.643 | 0.536 | 0.148 | 0.113 | 0.511 | 0.106 | 0.239 | 0.247 | 0.238 |
| Jurisdiction stripping constrained by rights carveouts | 0.563 | 0.539 | 0.203 | 0.589 | 0.321 | 0.591 | 0.623 | 0.169 | 0.632 | 0.535 | 0.162 | 0.114 | 0.517 | 0.107 | 0.239 | 0.258 | 0.214 |
| Nonpartisan commission appointments | 0.562 | 0.540 | 0.203 | 0.589 | 0.321 | 0.561 | 0.622 | 0.169 | 0.633 | 0.535 | 0.148 | 0.114 | 0.506 | 0.107 | 0.239 | 0.253 | 0.214 |
| Mandatory written emergency reasoning | 0.561 | 0.536 | 0.202 | 0.589 | 0.322 | 0.561 | 0.618 | 0.157 | 0.651 | 0.535 | 0.149 | 0.129 | 0.490 | 0.077 | 0.246 | 0.259 | 0.229 |
| Peer recusal + reasoned emergency docket | 0.561 | 0.535 | 0.199 | 0.589 | 0.321 | 0.561 | 0.621 | 0.167 | 0.632 | 0.536 | 0.148 | 0.113 | 0.497 | 0.106 | 0.237 | 0.259 | 0.220 |
| Three-judge panels with en banc correction | 0.561 | 0.541 | 0.204 | 0.589 | 0.321 | 0.561 | 0.623 | 0.167 | 0.639 | 0.536 | 0.146 | 0.114 | 0.543 | 0.108 | 0.239 | 0.250 | 0.230 |
| Retention-election accountability court | 0.560 | 0.542 | 0.206 | 0.589 | 0.322 | 0.562 | 0.613 | 0.166 | 0.637 | 0.534 | 0.154 | 0.113 | 0.508 | 0.107 | 0.240 | 0.255 | 0.215 |
| Automatic merits follow-up for emergency relief | 0.559 | 0.537 | 0.202 | 0.589 | 0.317 | 0.567 | 0.632 | 0.212 | 0.587 | 0.541 | 0.150 | 0.089 | 0.547 | 0.030 | 0.222 | 0.256 | 0.246 |
| Randomized merits panels with en banc correction | 0.559 | 0.539 | 0.201 | 0.589 | 0.321 | 0.561 | 0.622 | 0.167 | 0.639 | 0.536 | 0.148 | 0.115 | 0.545 | 0.107 | 0.238 | 0.250 | 0.237 |
| Comparative 16-seat constitutional senates | 0.559 | 0.536 | 0.202 | 0.589 | 0.322 | 0.559 | 0.613 | 0.135 | 0.686 | 0.536 | 0.142 | 0.131 | 0.536 | 0.099 | 0.249 | 0.251 | 0.260 |
| Independent recusal enforcement with substitutes | 0.559 | 0.538 | 0.202 | 0.589 | 0.321 | 0.561 | 0.622 | 0.167 | 0.633 | 0.535 | 0.149 | 0.114 | 0.520 | 0.107 | 0.239 | 0.252 | 0.235 |
| Expanded 15-seat court | 0.559 | 0.535 | 0.200 | 0.589 | 0.321 | 0.561 | 0.621 | 0.166 | 0.625 | 0.536 | 0.146 | 0.114 | 0.502 | 0.107 | 0.242 | 0.259 | 0.227 |
| Emergency integrity package | 0.559 | 0.541 | 0.204 | 0.589 | 0.317 | 0.567 | 0.634 | 0.209 | 0.598 | 0.543 | 0.148 | 0.089 | 0.577 | 0.030 | 0.223 | 0.247 | 0.268 |
| Time-limited legislative override window | 0.558 | 0.538 | 0.202 | 0.589 | 0.322 | 0.563 | 0.623 | 0.168 | 0.632 | 0.532 | 0.158 | 0.114 | 0.510 | 0.107 | 0.239 | 0.262 | 0.221 |
| Random panels with jurisdiction safeguards | 0.558 | 0.539 | 0.202 | 0.589 | 0.322 | 0.589 | 0.613 | 0.145 | 0.669 | 0.534 | 0.157 | 0.132 | 0.549 | 0.099 | 0.249 | 0.252 | 0.261 |
| Judicial review with legislative supermajority override | 0.558 | 0.539 | 0.204 | 0.589 | 0.322 | 0.562 | 0.624 | 0.169 | 0.631 | 0.532 | 0.159 | 0.114 | 0.511 | 0.107 | 0.239 | 0.264 | 0.221 |
| Constitutional council with concrete-review backstop | 0.555 | 0.540 | 0.204 | 0.589 | 0.319 | 0.606 | 0.624 | 0.159 | 0.658 | 0.542 | 0.154 | 0.112 | 0.576 | 0.106 | 0.238 | 0.258 | 0.308 |
| Pre-enactment constitutional council | 0.555 | 0.541 | 0.206 | 0.589 | 0.320 | 0.606 | 0.624 | 0.165 | 0.644 | 0.540 | 0.155 | 0.113 | 0.569 | 0.107 | 0.238 | 0.259 | 0.294 |
| Judicial electorate selection court | 0.554 | 0.542 | 0.206 | 0.589 | 0.321 | 0.562 | 0.624 | 0.171 | 0.634 | 0.535 | 0.148 | 0.114 | 0.527 | 0.108 | 0.242 | 0.247 | 0.277 |
| Stylized current U.S.-like supreme court | 0.552 | 0.538 | 0.204 | 0.589 | 0.332 | 0.552 | 0.634 | 0.191 | 0.598 | 0.513 | 0.183 | 0.187 | 0.345 | 0.308 | 0.316 | 0.291 | 0.153 |
| Supreme court with cross-checking constitutional court | 0.550 | 0.539 | 0.202 | 0.589 | 0.302 | 0.579 | 0.597 | 0.098 | 0.694 | 0.542 | 0.146 | 0.130 | 0.507 | 0.099 | 0.249 | 0.247 | 0.296 |
| Dual supreme courts with disagreement filter | 0.532 | 0.539 | 0.202 | 0.589 | 0.324 | 0.559 | 0.621 | 0.168 | 0.588 | 0.526 | 0.157 | 0.132 | 0.511 | 0.099 | 0.250 | 0.259 | 0.332 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.397 | 0.139 | 0.314 | 0.365 | 0.638 | 0.182 | 0.266 | 0.158 |
| Constitutional remand before invalidation | 0.397 | 0.149 | 0.351 | 0.347 | 0.648 | 0.183 | 0.282 | 0.174 |
| No emergency relief without merits review | 0.397 | 0.207 | 0.466 | 0.453 | 0.944 | 0.313 | 0.442 | 0.238 |
| 18-year staggered terms + regular appointments | 0.397 | 0.167 | 0.387 | 0.400 | 0.734 | 0.215 | 0.316 | 0.207 |
| Constitutional remand with override window | 0.397 | 0.141 | 0.328 | 0.334 | 0.632 | 0.166 | 0.274 | 0.162 |
| Public-interest litigation filter | 0.397 | 0.175 | 0.416 | 0.416 | 0.750 | 0.244 | 0.333 | 0.196 |
| Jurisdiction stripping constrained by rights carveouts | 0.397 | 0.169 | 0.391 | 0.402 | 0.746 | 0.238 | 0.338 | 0.200 |
| Nonpartisan commission appointments | 0.397 | 0.169 | 0.392 | 0.397 | 0.743 | 0.247 | 0.336 | 0.197 |
| Mandatory written emergency reasoning | 0.397 | 0.157 | 0.355 | 0.397 | 0.731 | 0.216 | 0.284 | 0.190 |
| Peer recusal + reasoned emergency docket | 0.397 | 0.167 | 0.386 | 0.408 | 0.735 | 0.235 | 0.320 | 0.205 |
| Three-judge panels with en banc correction | 0.397 | 0.167 | 0.390 | 0.410 | 0.728 | 0.209 | 0.320 | 0.204 |
| Retention-election accountability court | 0.397 | 0.166 | 0.387 | 0.381 | 0.720 | 0.235 | 0.324 | 0.196 |
| Automatic merits follow-up for emergency relief | 0.397 | 0.212 | 0.474 | 0.491 | 0.961 | 0.364 | 0.468 | 0.257 |
| Randomized merits panels with en banc correction | 0.397 | 0.167 | 0.387 | 0.405 | 0.736 | 0.214 | 0.309 | 0.206 |
| Comparative 16-seat constitutional senates | 0.397 | 0.135 | 0.307 | 0.317 | 0.629 | 0.157 | 0.233 | 0.143 |
| Independent recusal enforcement with substitutes | 0.397 | 0.167 | 0.390 | 0.399 | 0.733 | 0.235 | 0.332 | 0.198 |
| Expanded 15-seat court | 0.397 | 0.166 | 0.386 | 0.404 | 0.731 | 0.227 | 0.322 | 0.202 |
| Emergency integrity package | 0.397 | 0.209 | 0.469 | 0.462 | 0.946 | 0.336 | 0.436 | 0.241 |
| Time-limited legislative override window | 0.397 | 0.168 | 0.389 | 0.390 | 0.745 | 0.202 | 0.315 | 0.208 |
| Random panels with jurisdiction safeguards | 0.397 | 0.145 | 0.329 | 0.374 | 0.652 | 0.179 | 0.294 | 0.177 |
| Judicial review with legislative supermajority override | 0.397 | 0.169 | 0.389 | 0.393 | 0.749 | 0.245 | 0.339 | 0.213 |
| Constitutional council with concrete-review backstop | 0.397 | 0.159 | 0.373 | 0.346 | 0.701 | 0.177 | 0.274 | 0.168 |
| Pre-enactment constitutional council | 0.397 | 0.165 | 0.381 | 0.380 | 0.726 | 0.210 | 0.307 | 0.188 |
| Judicial electorate selection court | 0.397 | 0.171 | 0.397 | 0.405 | 0.741 | 0.242 | 0.343 | 0.217 |
| Stylized current U.S.-like supreme court | 0.397 | 0.191 | 0.411 | 0.424 | 0.960 | 0.347 | 0.400 | 0.217 |
| Supreme court with cross-checking constitutional court | 0.397 | 0.098 | 0.231 | 0.254 | 0.418 | 0.139 | 0.188 | 0.131 |
| Dual supreme courts with disagreement filter | 0.397 | 0.168 | 0.381 | 0.407 | 0.767 | 0.226 | 0.353 | 0.202 |

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
| Appointment Timing Manipulation | No emergency relief without merits review (0.614) | Automatic merits follow-up for emergency relief (0.648) | No emergency relief without merits review (0.010) | Jurisdiction stripping constrained by rights carveouts (0.020) |
| Emergency Application Flood | 60 percent invalidation threshold (0.498) | Stylized current U.S.-like supreme court (0.665) | No emergency relief without merits review (0.059) | Jurisdiction stripping constrained by rights carveouts (0.038) |
| Override Evasion Loop | 60 percent invalidation threshold (0.523) | Emergency integrity package (0.616) | No emergency relief without merits review (0.029) | Time-limited legislative override window (0.028) |
| Recusal Pressure Campaign | 60 percent invalidation threshold (0.526) | Stylized current U.S.-like supreme court (0.634) | No emergency relief without merits review (0.035) | Time-limited legislative override window (0.041) |
| Court Expansion Retaliation | Constitutional remand before invalidation (0.507) | Stylized current U.S.-like supreme court (0.627) | No emergency relief without merits review (0.038) | Time-limited legislative override window (0.044) |
