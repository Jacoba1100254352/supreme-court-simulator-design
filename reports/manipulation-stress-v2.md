# Adversarial Manipulation Stress Campaign v2

Deterministic simulation study for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 27
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

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.533); Constitutional remand before invalidation (0.531); Constitutional remand with override window (0.528); 18-year staggered terms + regular appointments (0.526); Comparative 16-seat constitutional senates (0.524); Public-interest litigation filter (0.524); No emergency relief without merits review (0.523). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.533.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.636.
- Lowest emergency-process irregularity: No emergency relief without merits review at 0.034.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.269.
- Lowest partisan alignment: Jurisdiction stripping constrained by rights carveouts at 0.034.
- Highest modeled process-legitimacy index: Emergency integrity package at 0.587.
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
| 60 percent invalidation threshold | 0.533 | 0.573 | 0.218 | 0.635 | 0.393 | 0.521 | 0.604 | 0.165 | 0.621 | 0.487 | 0.204 | 0.178 | 0.454 | 0.130 | 0.305 | 0.304 | 0.205 |
| Constitutional remand before invalidation | 0.531 | 0.581 | 0.221 | 0.635 | 0.355 | 0.546 | 0.616 | 0.179 | 0.649 | 0.508 | 0.210 | 0.154 | 0.536 | 0.139 | 0.294 | 0.296 | 0.330 |
| Constitutional remand with override window | 0.528 | 0.581 | 0.223 | 0.635 | 0.356 | 0.546 | 0.610 | 0.165 | 0.672 | 0.506 | 0.212 | 0.176 | 0.532 | 0.106 | 0.305 | 0.296 | 0.362 |
| 18-year staggered terms + regular appointments | 0.526 | 0.570 | 0.213 | 0.635 | 0.392 | 0.524 | 0.614 | 0.198 | 0.556 | 0.487 | 0.211 | 0.154 | 0.475 | 0.138 | 0.292 | 0.307 | 0.209 |
| Comparative 16-seat constitutional senates | 0.524 | 0.573 | 0.217 | 0.635 | 0.394 | 0.521 | 0.605 | 0.158 | 0.642 | 0.487 | 0.209 | 0.178 | 0.522 | 0.130 | 0.304 | 0.299 | 0.280 |
| Public-interest litigation filter | 0.524 | 0.583 | 0.229 | 0.635 | 0.391 | 0.525 | 0.622 | 0.208 | 0.565 | 0.487 | 0.211 | 0.155 | 0.501 | 0.139 | 0.296 | 0.295 | 0.259 |
| No emergency relief without merits review | 0.523 | 0.574 | 0.216 | 0.635 | 0.387 | 0.531 | 0.629 | 0.261 | 0.489 | 0.494 | 0.216 | 0.119 | 0.580 | 0.034 | 0.269 | 0.297 | 0.248 |
| Jurisdiction stripping constrained by rights carveouts | 0.523 | 0.573 | 0.210 | 0.635 | 0.393 | 0.554 | 0.615 | 0.199 | 0.556 | 0.485 | 0.232 | 0.155 | 0.504 | 0.139 | 0.293 | 0.311 | 0.232 |
| Nonpartisan commission appointments | 0.523 | 0.574 | 0.214 | 0.635 | 0.392 | 0.524 | 0.615 | 0.201 | 0.551 | 0.486 | 0.212 | 0.155 | 0.493 | 0.138 | 0.291 | 0.302 | 0.231 |
| Mandatory written emergency reasoning | 0.523 | 0.575 | 0.222 | 0.635 | 0.392 | 0.523 | 0.608 | 0.184 | 0.583 | 0.486 | 0.210 | 0.177 | 0.471 | 0.106 | 0.305 | 0.308 | 0.249 |
| Peer recusal + reasoned emergency docket | 0.522 | 0.570 | 0.212 | 0.635 | 0.392 | 0.524 | 0.615 | 0.200 | 0.555 | 0.487 | 0.212 | 0.154 | 0.481 | 0.138 | 0.291 | 0.308 | 0.237 |
| Three-judge panels with en banc correction | 0.522 | 0.576 | 0.218 | 0.635 | 0.392 | 0.524 | 0.617 | 0.201 | 0.562 | 0.487 | 0.212 | 0.156 | 0.530 | 0.139 | 0.292 | 0.298 | 0.249 |
| Expanded 15-seat court | 0.521 | 0.567 | 0.206 | 0.635 | 0.392 | 0.524 | 0.613 | 0.197 | 0.553 | 0.488 | 0.212 | 0.153 | 0.491 | 0.137 | 0.294 | 0.306 | 0.244 |
| Randomized merits panels with en banc correction | 0.521 | 0.575 | 0.216 | 0.635 | 0.391 | 0.524 | 0.616 | 0.201 | 0.562 | 0.488 | 0.207 | 0.156 | 0.531 | 0.139 | 0.292 | 0.299 | 0.256 |
| Retention-election accountability court | 0.521 | 0.576 | 0.218 | 0.635 | 0.392 | 0.525 | 0.602 | 0.199 | 0.555 | 0.485 | 0.216 | 0.154 | 0.494 | 0.138 | 0.293 | 0.303 | 0.232 |
| Random panels with jurisdiction safeguards | 0.520 | 0.576 | 0.218 | 0.635 | 0.394 | 0.551 | 0.604 | 0.166 | 0.613 | 0.484 | 0.223 | 0.180 | 0.533 | 0.131 | 0.305 | 0.303 | 0.281 |
| Independent recusal enforcement with substitutes | 0.519 | 0.574 | 0.215 | 0.635 | 0.392 | 0.524 | 0.614 | 0.199 | 0.551 | 0.486 | 0.214 | 0.155 | 0.512 | 0.138 | 0.293 | 0.303 | 0.253 |
| Constitutional council with concrete-review backstop | 0.519 | 0.573 | 0.214 | 0.635 | 0.390 | 0.570 | 0.619 | 0.189 | 0.601 | 0.494 | 0.218 | 0.152 | 0.570 | 0.137 | 0.290 | 0.307 | 0.334 |
| Time-limited legislative override window | 0.518 | 0.577 | 0.219 | 0.635 | 0.394 | 0.526 | 0.618 | 0.201 | 0.553 | 0.482 | 0.228 | 0.156 | 0.500 | 0.139 | 0.295 | 0.315 | 0.240 |
| Judicial review with legislative supermajority override | 0.517 | 0.572 | 0.214 | 0.635 | 0.393 | 0.524 | 0.615 | 0.198 | 0.549 | 0.483 | 0.223 | 0.156 | 0.498 | 0.139 | 0.293 | 0.316 | 0.239 |
| Automatic merits follow-up for emergency relief | 0.517 | 0.575 | 0.220 | 0.635 | 0.387 | 0.532 | 0.626 | 0.262 | 0.478 | 0.492 | 0.219 | 0.115 | 0.548 | 0.044 | 0.271 | 0.307 | 0.266 |
| Emergency integrity package | 0.516 | 0.577 | 0.223 | 0.635 | 0.387 | 0.532 | 0.629 | 0.261 | 0.484 | 0.493 | 0.216 | 0.115 | 0.587 | 0.044 | 0.272 | 0.299 | 0.288 |
| Stylized current U.S.-like supreme court | 0.515 | 0.574 | 0.219 | 0.635 | 0.404 | 0.513 | 0.636 | 0.240 | 0.524 | 0.462 | 0.251 | 0.247 | 0.306 | 0.378 | 0.379 | 0.341 | 0.165 |
| Pre-enactment constitutional council | 0.515 | 0.574 | 0.213 | 0.635 | 0.391 | 0.570 | 0.618 | 0.198 | 0.569 | 0.491 | 0.223 | 0.153 | 0.561 | 0.137 | 0.291 | 0.311 | 0.320 |
| Supreme court with cross-checking constitutional court | 0.515 | 0.575 | 0.220 | 0.635 | 0.373 | 0.541 | 0.585 | 0.113 | 0.654 | 0.494 | 0.209 | 0.178 | 0.497 | 0.131 | 0.307 | 0.295 | 0.319 |
| Judicial electorate selection court | 0.514 | 0.576 | 0.218 | 0.635 | 0.392 | 0.524 | 0.616 | 0.201 | 0.554 | 0.486 | 0.215 | 0.156 | 0.515 | 0.139 | 0.295 | 0.296 | 0.296 |
| Dual supreme courts with disagreement filter | 0.489 | 0.576 | 0.219 | 0.635 | 0.395 | 0.521 | 0.614 | 0.204 | 0.493 | 0.475 | 0.222 | 0.181 | 0.503 | 0.131 | 0.308 | 0.309 | 0.355 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.450 | 0.165 | 0.331 | 0.389 | 0.641 | 0.223 | 0.327 | 0.203 |
| Constitutional remand before invalidation | 0.450 | 0.179 | 0.390 | 0.387 | 0.635 | 0.247 | 0.330 | 0.204 |
| Constitutional remand with override window | 0.450 | 0.165 | 0.341 | 0.381 | 0.638 | 0.212 | 0.341 | 0.194 |
| 18-year staggered terms + regular appointments | 0.450 | 0.198 | 0.412 | 0.462 | 0.739 | 0.298 | 0.380 | 0.255 |
| Comparative 16-seat constitutional senates | 0.450 | 0.158 | 0.325 | 0.360 | 0.626 | 0.194 | 0.314 | 0.164 |
| Public-interest litigation filter | 0.450 | 0.208 | 0.443 | 0.452 | 0.757 | 0.285 | 0.414 | 0.254 |
| No emergency relief without merits review | 0.450 | 0.261 | 0.539 | 0.566 | 0.979 | 0.399 | 0.540 | 0.323 |
| Jurisdiction stripping constrained by rights carveouts | 0.450 | 0.199 | 0.420 | 0.433 | 0.752 | 0.256 | 0.378 | 0.238 |
| Nonpartisan commission appointments | 0.450 | 0.201 | 0.419 | 0.475 | 0.753 | 0.271 | 0.412 | 0.242 |
| Mandatory written emergency reasoning | 0.450 | 0.184 | 0.369 | 0.457 | 0.724 | 0.217 | 0.357 | 0.218 |
| Peer recusal + reasoned emergency docket | 0.450 | 0.200 | 0.415 | 0.467 | 0.748 | 0.265 | 0.399 | 0.237 |
| Three-judge panels with en banc correction | 0.450 | 0.201 | 0.427 | 0.456 | 0.745 | 0.273 | 0.389 | 0.256 |
| Expanded 15-seat court | 0.450 | 0.197 | 0.415 | 0.459 | 0.733 | 0.277 | 0.395 | 0.239 |
| Randomized merits panels with en banc correction | 0.450 | 0.201 | 0.424 | 0.466 | 0.744 | 0.270 | 0.368 | 0.235 |
| Retention-election accountability court | 0.450 | 0.199 | 0.416 | 0.442 | 0.756 | 0.260 | 0.393 | 0.227 |
| Random panels with jurisdiction safeguards | 0.450 | 0.166 | 0.334 | 0.395 | 0.631 | 0.223 | 0.315 | 0.220 |
| Independent recusal enforcement with substitutes | 0.450 | 0.199 | 0.418 | 0.453 | 0.730 | 0.286 | 0.396 | 0.250 |
| Constitutional council with concrete-review backstop | 0.450 | 0.189 | 0.401 | 0.405 | 0.733 | 0.255 | 0.322 | 0.197 |
| Time-limited legislative override window | 0.450 | 0.201 | 0.430 | 0.463 | 0.741 | 0.256 | 0.382 | 0.233 |
| Judicial review with legislative supermajority override | 0.450 | 0.198 | 0.414 | 0.459 | 0.744 | 0.288 | 0.384 | 0.230 |
| Automatic merits follow-up for emergency relief | 0.450 | 0.262 | 0.539 | 0.582 | 0.983 | 0.390 | 0.617 | 0.318 |
| Emergency integrity package | 0.450 | 0.261 | 0.540 | 0.563 | 0.977 | 0.437 | 0.554 | 0.301 |
| Stylized current U.S.-like supreme court | 0.450 | 0.240 | 0.489 | 0.491 | 0.985 | 0.385 | 0.530 | 0.265 |
| Pre-enactment constitutional council | 0.450 | 0.198 | 0.417 | 0.452 | 0.736 | 0.225 | 0.356 | 0.225 |
| Supreme court with cross-checking constitutional court | 0.450 | 0.113 | 0.231 | 0.288 | 0.419 | 0.183 | 0.213 | 0.147 |
| Judicial electorate selection court | 0.450 | 0.201 | 0.423 | 0.475 | 0.738 | 0.317 | 0.382 | 0.235 |
| Dual supreme courts with disagreement filter | 0.450 | 0.204 | 0.421 | 0.481 | 0.771 | 0.291 | 0.399 | 0.236 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest emerg. irregularity | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Appointment Timing Manipulation | No emergency relief without merits review (0.614) | Automatic merits follow-up for emergency relief (0.647) | No emergency relief without merits review (0.009) | Judicial review with legislative supermajority override (0.020) |
| Emergency Application Flood | 60 percent invalidation threshold (0.497) | Stylized current U.S.-like supreme court (0.666) | No emergency relief without merits review (0.060) | Jurisdiction stripping constrained by rights carveouts (0.032) |
| Override Evasion Loop | Constitutional remand before invalidation (0.526) | No emergency relief without merits review (0.615) | No emergency relief without merits review (0.028) | Dual supreme courts with disagreement filter (0.031) |
| Recusal Pressure Campaign | 60 percent invalidation threshold (0.522) | Stylized current U.S.-like supreme court (0.639) | No emergency relief without merits review (0.036) | Jurisdiction stripping constrained by rights carveouts (0.038) |
| Court Expansion Retaliation | Constitutional remand with override window (0.506) | Stylized current U.S.-like supreme court (0.624) | No emergency relief without merits review (0.038) | Jurisdiction stripping constrained by rights carveouts (0.048) |
