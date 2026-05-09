# Adversarial Manipulation Stress Campaign v2

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 26
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

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.532); Constitutional remand before invalidation (0.530); Constitutional remand with override window (0.527); 18-year staggered terms + regular appointments (0.524); Public-interest litigation filter (0.522); Comparative 16-seat constitutional senates (0.522). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.532.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.640.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.035.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.275.
- Lowest partisan alignment: Jurisdiction stripping constrained by rights carveouts at 0.035.
- Highest public confidence index: Emergency integrity package at 0.594.
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
| 60 percent invalidation threshold | 0.532 | 0.589 | 0.247 | 0.635 | 0.393 | 0.522 | 0.607 | 0.168 | 0.624 | 0.485 | 0.206 | 0.181 | 0.459 | 0.132 | 0.311 | 0.307 | 0.209 |
| Constitutional remand before invalidation | 0.530 | 0.598 | 0.254 | 0.635 | 0.355 | 0.547 | 0.619 | 0.184 | 0.653 | 0.506 | 0.216 | 0.157 | 0.544 | 0.141 | 0.300 | 0.299 | 0.337 |
| Constitutional remand with override window | 0.527 | 0.598 | 0.254 | 0.635 | 0.356 | 0.547 | 0.612 | 0.167 | 0.673 | 0.503 | 0.214 | 0.180 | 0.539 | 0.108 | 0.312 | 0.298 | 0.370 |
| 18-year staggered terms + regular appointments | 0.524 | 0.589 | 0.249 | 0.635 | 0.392 | 0.525 | 0.617 | 0.203 | 0.553 | 0.484 | 0.216 | 0.158 | 0.481 | 0.142 | 0.299 | 0.311 | 0.214 |
| Public-interest litigation filter | 0.522 | 0.594 | 0.249 | 0.635 | 0.392 | 0.525 | 0.625 | 0.211 | 0.567 | 0.485 | 0.220 | 0.157 | 0.505 | 0.141 | 0.300 | 0.297 | 0.263 |
| Comparative 16-seat constitutional senates | 0.522 | 0.589 | 0.248 | 0.635 | 0.394 | 0.522 | 0.609 | 0.165 | 0.639 | 0.485 | 0.213 | 0.181 | 0.529 | 0.133 | 0.311 | 0.301 | 0.285 |
| No emergency relief without merits review | 0.521 | 0.589 | 0.245 | 0.635 | 0.387 | 0.532 | 0.634 | 0.268 | 0.483 | 0.491 | 0.220 | 0.121 | 0.587 | 0.035 | 0.275 | 0.299 | 0.253 |
| Mandatory written emergency reasoning | 0.521 | 0.590 | 0.251 | 0.635 | 0.393 | 0.524 | 0.612 | 0.188 | 0.582 | 0.483 | 0.216 | 0.181 | 0.477 | 0.108 | 0.313 | 0.311 | 0.255 |
| Nonpartisan commission appointments | 0.520 | 0.593 | 0.251 | 0.635 | 0.392 | 0.525 | 0.620 | 0.209 | 0.544 | 0.482 | 0.218 | 0.159 | 0.498 | 0.142 | 0.299 | 0.305 | 0.237 |
| Three-judge panels with en banc correction | 0.519 | 0.592 | 0.248 | 0.635 | 0.392 | 0.525 | 0.618 | 0.204 | 0.559 | 0.484 | 0.215 | 0.159 | 0.536 | 0.142 | 0.297 | 0.301 | 0.254 |
| Peer recusal + reasoned emergency docket | 0.519 | 0.588 | 0.246 | 0.635 | 0.392 | 0.524 | 0.617 | 0.202 | 0.551 | 0.484 | 0.218 | 0.157 | 0.488 | 0.141 | 0.297 | 0.311 | 0.243 |
| Expanded 15-seat court | 0.519 | 0.584 | 0.237 | 0.635 | 0.392 | 0.524 | 0.615 | 0.199 | 0.551 | 0.485 | 0.215 | 0.155 | 0.497 | 0.139 | 0.300 | 0.309 | 0.249 |
| Jurisdiction stripping constrained by rights carveouts | 0.519 | 0.592 | 0.250 | 0.635 | 0.393 | 0.555 | 0.619 | 0.206 | 0.548 | 0.481 | 0.241 | 0.158 | 0.513 | 0.142 | 0.301 | 0.316 | 0.237 |
| Random panels with jurisdiction safeguards | 0.518 | 0.590 | 0.246 | 0.635 | 0.394 | 0.551 | 0.605 | 0.167 | 0.616 | 0.481 | 0.230 | 0.183 | 0.539 | 0.134 | 0.312 | 0.306 | 0.286 |
| Retention-election accountability court | 0.518 | 0.593 | 0.249 | 0.635 | 0.393 | 0.526 | 0.604 | 0.203 | 0.550 | 0.482 | 0.226 | 0.156 | 0.502 | 0.140 | 0.298 | 0.306 | 0.237 |
| Randomized merits panels with en banc correction | 0.518 | 0.594 | 0.251 | 0.635 | 0.391 | 0.525 | 0.620 | 0.207 | 0.554 | 0.484 | 0.214 | 0.159 | 0.539 | 0.142 | 0.298 | 0.301 | 0.262 |
| Constitutional council with concrete-review backstop | 0.517 | 0.592 | 0.248 | 0.635 | 0.390 | 0.572 | 0.623 | 0.196 | 0.598 | 0.491 | 0.225 | 0.155 | 0.580 | 0.140 | 0.298 | 0.312 | 0.342 |
| Independent recusal enforcement with substitutes | 0.516 | 0.591 | 0.245 | 0.635 | 0.392 | 0.525 | 0.617 | 0.205 | 0.545 | 0.482 | 0.221 | 0.158 | 0.519 | 0.141 | 0.300 | 0.305 | 0.259 |
| Time-limited legislative override window | 0.516 | 0.592 | 0.250 | 0.635 | 0.394 | 0.527 | 0.620 | 0.205 | 0.548 | 0.479 | 0.233 | 0.159 | 0.505 | 0.143 | 0.302 | 0.317 | 0.245 |
| Judicial review with legislative supermajority override | 0.515 | 0.591 | 0.249 | 0.635 | 0.393 | 0.525 | 0.621 | 0.207 | 0.543 | 0.480 | 0.230 | 0.158 | 0.507 | 0.141 | 0.301 | 0.319 | 0.245 |
| Stylized current U.S.-like supreme court | 0.514 | 0.586 | 0.239 | 0.635 | 0.404 | 0.514 | 0.640 | 0.246 | 0.521 | 0.461 | 0.254 | 0.251 | 0.308 | 0.384 | 0.385 | 0.343 | 0.167 |
| Automatic merits follow-up for emergency relief | 0.514 | 0.591 | 0.252 | 0.635 | 0.387 | 0.532 | 0.630 | 0.270 | 0.469 | 0.489 | 0.225 | 0.117 | 0.555 | 0.045 | 0.277 | 0.309 | 0.271 |
| Emergency integrity package | 0.514 | 0.592 | 0.249 | 0.635 | 0.387 | 0.533 | 0.632 | 0.267 | 0.479 | 0.491 | 0.222 | 0.117 | 0.594 | 0.045 | 0.277 | 0.301 | 0.294 |
| Supreme court with cross-checking constitutional court | 0.513 | 0.591 | 0.249 | 0.635 | 0.373 | 0.542 | 0.586 | 0.112 | 0.658 | 0.492 | 0.213 | 0.180 | 0.502 | 0.133 | 0.310 | 0.297 | 0.325 |
| Pre-enactment constitutional council | 0.513 | 0.589 | 0.242 | 0.635 | 0.391 | 0.572 | 0.621 | 0.203 | 0.565 | 0.488 | 0.229 | 0.156 | 0.569 | 0.140 | 0.297 | 0.314 | 0.326 |
| Dual supreme courts with disagreement filter | 0.486 | 0.593 | 0.252 | 0.635 | 0.396 | 0.522 | 0.617 | 0.209 | 0.486 | 0.470 | 0.232 | 0.185 | 0.508 | 0.135 | 0.316 | 0.314 | 0.363 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.450 | 0.168 | 0.336 | 0.417 | 0.642 | 0.258 | 0.350 | 0.215 |
| Constitutional remand before invalidation | 0.450 | 0.184 | 0.399 | 0.388 | 0.670 | 0.223 | 0.334 | 0.221 |
| Constitutional remand with override window | 0.450 | 0.167 | 0.347 | 0.403 | 0.628 | 0.214 | 0.325 | 0.203 |
| 18-year staggered terms + regular appointments | 0.450 | 0.203 | 0.419 | 0.480 | 0.745 | 0.317 | 0.406 | 0.264 |
| Public-interest litigation filter | 0.450 | 0.211 | 0.453 | 0.482 | 0.741 | 0.316 | 0.404 | 0.265 |
| Comparative 16-seat constitutional senates | 0.450 | 0.165 | 0.342 | 0.384 | 0.640 | 0.193 | 0.319 | 0.170 |
| No emergency relief without merits review | 0.450 | 0.268 | 0.560 | 0.585 | 0.973 | 0.423 | 0.576 | 0.328 |
| Mandatory written emergency reasoning | 0.450 | 0.188 | 0.383 | 0.461 | 0.716 | 0.238 | 0.365 | 0.247 |
| Nonpartisan commission appointments | 0.450 | 0.209 | 0.441 | 0.469 | 0.748 | 0.292 | 0.431 | 0.265 |
| Three-judge panels with en banc correction | 0.450 | 0.204 | 0.427 | 0.474 | 0.740 | 0.250 | 0.397 | 0.263 |
| Peer recusal + reasoned emergency docket | 0.450 | 0.202 | 0.423 | 0.468 | 0.742 | 0.283 | 0.401 | 0.255 |
| Expanded 15-seat court | 0.450 | 0.199 | 0.411 | 0.475 | 0.735 | 0.270 | 0.401 | 0.253 |
| Jurisdiction stripping constrained by rights carveouts | 0.450 | 0.206 | 0.442 | 0.444 | 0.749 | 0.295 | 0.444 | 0.229 |
| Random panels with jurisdiction safeguards | 0.450 | 0.167 | 0.340 | 0.398 | 0.617 | 0.234 | 0.319 | 0.223 |
| Retention-election accountability court | 0.450 | 0.203 | 0.434 | 0.450 | 0.746 | 0.316 | 0.376 | 0.232 |
| Randomized merits panels with en banc correction | 0.450 | 0.207 | 0.438 | 0.466 | 0.746 | 0.305 | 0.400 | 0.263 |
| Constitutional council with concrete-review backstop | 0.450 | 0.196 | 0.420 | 0.413 | 0.726 | 0.268 | 0.339 | 0.215 |
| Independent recusal enforcement with substitutes | 0.450 | 0.205 | 0.427 | 0.494 | 0.754 | 0.296 | 0.403 | 0.255 |
| Time-limited legislative override window | 0.450 | 0.205 | 0.436 | 0.451 | 0.750 | 0.250 | 0.366 | 0.271 |
| Judicial review with legislative supermajority override | 0.450 | 0.207 | 0.430 | 0.465 | 0.760 | 0.280 | 0.395 | 0.257 |
| Stylized current U.S.-like supreme court | 0.450 | 0.246 | 0.500 | 0.497 | 0.981 | 0.434 | 0.561 | 0.282 |
| Automatic merits follow-up for emergency relief | 0.450 | 0.270 | 0.554 | 0.603 | 0.979 | 0.452 | 0.616 | 0.348 |
| Emergency integrity package | 0.450 | 0.267 | 0.554 | 0.572 | 0.982 | 0.447 | 0.572 | 0.341 |
| Supreme court with cross-checking constitutional court | 0.450 | 0.112 | 0.234 | 0.278 | 0.400 | 0.166 | 0.209 | 0.133 |
| Pre-enactment constitutional council | 0.450 | 0.203 | 0.431 | 0.452 | 0.729 | 0.251 | 0.391 | 0.249 |
| Dual supreme courts with disagreement filter | 0.450 | 0.209 | 0.426 | 0.498 | 0.791 | 0.307 | 0.420 | 0.264 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Appointment Timing Manipulation | No emergency relief without merits review (0.614) | Public-interest litigation filter (0.650) | No emergency relief without merits review (0.009) | Time-limited legislative override window (0.020) |
| Emergency Application Flood | 60 percent invalidation threshold (0.496) | Stylized current U.S.-like supreme court (0.666) | No emergency relief without merits review (0.061) | Jurisdiction stripping constrained by rights carveouts (0.033) |
| Override Evasion Loop | Constitutional remand before invalidation (0.525) | No emergency relief without merits review (0.619) | No emergency relief without merits review (0.029) | Time-limited legislative override window (0.032) |
| Recusal Pressure Campaign | 60 percent invalidation threshold (0.519) | Stylized current U.S.-like supreme court (0.644) | No emergency relief without merits review (0.038) | Jurisdiction stripping constrained by rights carveouts (0.039) |
| Court Expansion Retaliation | Constitutional remand before invalidation (0.506) | Stylized current U.S.-like supreme court (0.628) | No emergency relief without merits review (0.039) | Judicial review with legislative supermajority override (0.050) |
