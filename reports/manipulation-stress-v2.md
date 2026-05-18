# Adversarial Manipulation Stress Campaign v2

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

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

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.533); Constitutional remand before invalidation (0.532); Constitutional remand with override window (0.529); 18-year staggered terms + regular appointments (0.527); Comparative 16-seat constitutional senates (0.525); Public-interest litigation filter (0.524); No emergency relief without merits review (0.523). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.533.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.636.
- Lowest emergency-process irregularity: No emergency relief without merits review at 0.034.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.268.
- Lowest partisan alignment: Judicial review with legislative supermajority override at 0.033.
- Highest modeled public-legitimacy proxy: Emergency integrity package at 0.584.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, claimant success, precedent durability, lower-court compliance, elite acceptance, and administrative feasibility.
- Empirical claims, synthetic findings, and speculative design recommendations should be read separately: source ranges only smoke-test plausibility, campaign outputs are synthetic, and design recommendations are conditional on the model assumptions.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Higher direct outputs such as `rightsClaimantSuccess`, `doctrinalDepth`, `remedialBreadth`, `precedentDurability`, `lowerCourtCompliance`, `eliteAcceptance`, and `processLegitimacyProxy` are usually better, but each should be read in domain context.
- Lower `partisanAlignment`, `emergencyProcessIrregularity` (legacy CSV field `shadowDocketAbuse`), `emergencyLegitimacyRisk`, `emergencyDownstreamEffect`, `governmentNoncomplianceRate`, `reversalRate`, `constitutionalConflict`, `administrativeCost`, and `strategicPressure` are usually better.
- Petition, court-requested-response, CVSG, certiorari-admission, bar-capital, claim-strength, vehicle-quality, genuine-split, lower-court-split, lower-court-resistance, forum-shopping, settlement, strategic-plaintiff, repeat-player, enforcement-capacity, emergency-opportunism, emergency, emergency-downstream, replacement, recusal, concurrence, dissent, fragmentation, panel, en banc, council, cross-check, remand, public-interest, formal-response, practical-response, noncompliance, and override rates are diagnostic rather than automatically good or bad.

## Scenario Averages Across Cases

| Scenario | Directional | Admission | Cert admit | Lower split | Resistance | Enforcement | Rights protection | Claimant success | Precedent durability | Lower-court compliance | Gov. noncomp. | Emerg. downstream | Public-legit. proxy | Emerg. irregularity | Emergency risk | Strategic | Admin cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.533 | 0.569 | 0.210 | 0.635 | 0.393 | 0.521 | 0.603 | 0.163 | 0.623 | 0.487 | 0.205 | 0.177 | 0.453 | 0.129 | 0.303 | 0.304 | 0.204 |
| Constitutional remand before invalidation | 0.532 | 0.575 | 0.211 | 0.635 | 0.355 | 0.545 | 0.614 | 0.177 | 0.649 | 0.508 | 0.208 | 0.153 | 0.532 | 0.138 | 0.291 | 0.295 | 0.327 |
| Constitutional remand with override window | 0.529 | 0.576 | 0.213 | 0.635 | 0.357 | 0.545 | 0.608 | 0.164 | 0.672 | 0.506 | 0.212 | 0.176 | 0.529 | 0.105 | 0.303 | 0.295 | 0.360 |
| 18-year staggered terms + regular appointments | 0.527 | 0.563 | 0.200 | 0.635 | 0.392 | 0.523 | 0.612 | 0.196 | 0.557 | 0.488 | 0.211 | 0.153 | 0.471 | 0.138 | 0.290 | 0.307 | 0.207 |
| Comparative 16-seat constitutional senates | 0.525 | 0.569 | 0.209 | 0.635 | 0.394 | 0.521 | 0.605 | 0.159 | 0.641 | 0.488 | 0.208 | 0.178 | 0.521 | 0.129 | 0.304 | 0.298 | 0.279 |
| Public-interest litigation filter | 0.524 | 0.577 | 0.219 | 0.635 | 0.391 | 0.524 | 0.621 | 0.204 | 0.568 | 0.489 | 0.210 | 0.153 | 0.499 | 0.138 | 0.294 | 0.294 | 0.257 |
| No emergency relief without merits review | 0.523 | 0.570 | 0.207 | 0.635 | 0.387 | 0.531 | 0.629 | 0.260 | 0.490 | 0.495 | 0.215 | 0.118 | 0.577 | 0.034 | 0.268 | 0.296 | 0.247 |
| Jurisdiction stripping constrained by rights carveouts | 0.523 | 0.572 | 0.207 | 0.635 | 0.393 | 0.554 | 0.615 | 0.200 | 0.556 | 0.486 | 0.229 | 0.154 | 0.504 | 0.138 | 0.292 | 0.310 | 0.231 |
| Mandatory written emergency reasoning | 0.523 | 0.572 | 0.216 | 0.635 | 0.393 | 0.523 | 0.608 | 0.184 | 0.584 | 0.486 | 0.210 | 0.177 | 0.471 | 0.106 | 0.304 | 0.308 | 0.248 |
| Nonpartisan commission appointments | 0.522 | 0.572 | 0.210 | 0.635 | 0.392 | 0.524 | 0.615 | 0.202 | 0.550 | 0.486 | 0.214 | 0.154 | 0.492 | 0.138 | 0.291 | 0.302 | 0.231 |
| Three-judge panels with en banc correction | 0.522 | 0.571 | 0.208 | 0.635 | 0.392 | 0.524 | 0.615 | 0.198 | 0.564 | 0.488 | 0.212 | 0.154 | 0.527 | 0.138 | 0.290 | 0.298 | 0.247 |
| Peer recusal + reasoned emergency docket | 0.522 | 0.568 | 0.208 | 0.635 | 0.392 | 0.524 | 0.614 | 0.199 | 0.556 | 0.487 | 0.212 | 0.154 | 0.481 | 0.138 | 0.291 | 0.309 | 0.237 |
| Expanded 15-seat court | 0.522 | 0.564 | 0.200 | 0.635 | 0.392 | 0.523 | 0.612 | 0.195 | 0.554 | 0.488 | 0.209 | 0.153 | 0.489 | 0.136 | 0.293 | 0.305 | 0.243 |
| Retention-election accountability court | 0.522 | 0.570 | 0.208 | 0.635 | 0.392 | 0.524 | 0.601 | 0.198 | 0.557 | 0.486 | 0.215 | 0.152 | 0.493 | 0.136 | 0.289 | 0.303 | 0.230 |
| Randomized merits panels with en banc correction | 0.521 | 0.570 | 0.206 | 0.635 | 0.391 | 0.524 | 0.615 | 0.198 | 0.564 | 0.489 | 0.206 | 0.155 | 0.529 | 0.138 | 0.290 | 0.298 | 0.255 |
| Random panels with jurisdiction safeguards | 0.520 | 0.571 | 0.209 | 0.635 | 0.394 | 0.551 | 0.602 | 0.164 | 0.613 | 0.485 | 0.224 | 0.179 | 0.531 | 0.130 | 0.303 | 0.303 | 0.279 |
| Independent recusal enforcement with substitutes | 0.520 | 0.571 | 0.207 | 0.635 | 0.392 | 0.524 | 0.613 | 0.198 | 0.553 | 0.486 | 0.212 | 0.155 | 0.511 | 0.138 | 0.291 | 0.302 | 0.252 |
| Constitutional council with concrete-review backstop | 0.519 | 0.570 | 0.208 | 0.635 | 0.390 | 0.570 | 0.619 | 0.188 | 0.600 | 0.495 | 0.217 | 0.151 | 0.569 | 0.136 | 0.289 | 0.308 | 0.333 |
| Time-limited legislative override window | 0.519 | 0.571 | 0.209 | 0.635 | 0.393 | 0.526 | 0.616 | 0.200 | 0.552 | 0.483 | 0.225 | 0.154 | 0.498 | 0.137 | 0.291 | 0.314 | 0.238 |
| Automatic merits follow-up for emergency relief | 0.518 | 0.568 | 0.208 | 0.635 | 0.387 | 0.531 | 0.625 | 0.261 | 0.480 | 0.493 | 0.214 | 0.114 | 0.546 | 0.043 | 0.269 | 0.306 | 0.264 |
| Judicial review with legislative supermajority override | 0.518 | 0.568 | 0.205 | 0.635 | 0.394 | 0.524 | 0.615 | 0.197 | 0.551 | 0.483 | 0.224 | 0.155 | 0.496 | 0.138 | 0.292 | 0.316 | 0.238 |
| Emergency integrity package | 0.517 | 0.572 | 0.211 | 0.635 | 0.387 | 0.531 | 0.628 | 0.260 | 0.487 | 0.495 | 0.213 | 0.114 | 0.584 | 0.044 | 0.270 | 0.297 | 0.287 |
| Pre-enactment constitutional council | 0.516 | 0.570 | 0.206 | 0.635 | 0.390 | 0.570 | 0.617 | 0.196 | 0.571 | 0.492 | 0.219 | 0.152 | 0.559 | 0.136 | 0.289 | 0.309 | 0.319 |
| Stylized current U.S.-like supreme court | 0.516 | 0.571 | 0.213 | 0.635 | 0.404 | 0.513 | 0.636 | 0.239 | 0.525 | 0.463 | 0.251 | 0.247 | 0.305 | 0.377 | 0.377 | 0.340 | 0.164 |
| Supreme court with cross-checking constitutional court | 0.516 | 0.570 | 0.211 | 0.635 | 0.373 | 0.541 | 0.585 | 0.114 | 0.654 | 0.495 | 0.209 | 0.177 | 0.496 | 0.129 | 0.304 | 0.295 | 0.317 |
| Judicial electorate selection court | 0.514 | 0.574 | 0.212 | 0.635 | 0.392 | 0.524 | 0.615 | 0.200 | 0.553 | 0.487 | 0.213 | 0.155 | 0.514 | 0.138 | 0.293 | 0.296 | 0.295 |
| Dual supreme courts with disagreement filter | 0.490 | 0.572 | 0.212 | 0.635 | 0.396 | 0.521 | 0.613 | 0.201 | 0.496 | 0.475 | 0.223 | 0.180 | 0.501 | 0.131 | 0.306 | 0.308 | 0.354 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.450 | 0.163 | 0.325 | 0.392 | 0.644 | 0.223 | 0.323 | 0.191 |
| Constitutional remand before invalidation | 0.450 | 0.177 | 0.379 | 0.393 | 0.638 | 0.237 | 0.330 | 0.196 |
| Constitutional remand with override window | 0.450 | 0.164 | 0.336 | 0.380 | 0.643 | 0.221 | 0.334 | 0.190 |
| 18-year staggered terms + regular appointments | 0.450 | 0.196 | 0.407 | 0.465 | 0.742 | 0.287 | 0.380 | 0.233 |
| Comparative 16-seat constitutional senates | 0.450 | 0.159 | 0.327 | 0.356 | 0.629 | 0.202 | 0.326 | 0.167 |
| Public-interest litigation filter | 0.450 | 0.204 | 0.436 | 0.453 | 0.754 | 0.277 | 0.398 | 0.249 |
| No emergency relief without merits review | 0.450 | 0.260 | 0.537 | 0.571 | 0.979 | 0.410 | 0.532 | 0.317 |
| Jurisdiction stripping constrained by rights carveouts | 0.450 | 0.200 | 0.422 | 0.451 | 0.744 | 0.258 | 0.376 | 0.239 |
| Mandatory written emergency reasoning | 0.450 | 0.184 | 0.368 | 0.452 | 0.728 | 0.233 | 0.364 | 0.218 |
| Nonpartisan commission appointments | 0.450 | 0.202 | 0.420 | 0.478 | 0.744 | 0.287 | 0.407 | 0.244 |
| Three-judge panels with en banc correction | 0.450 | 0.198 | 0.422 | 0.453 | 0.742 | 0.266 | 0.379 | 0.233 |
| Peer recusal + reasoned emergency docket | 0.450 | 0.199 | 0.412 | 0.461 | 0.742 | 0.282 | 0.398 | 0.225 |
| Expanded 15-seat court | 0.450 | 0.195 | 0.406 | 0.446 | 0.737 | 0.268 | 0.400 | 0.239 |
| Retention-election accountability court | 0.450 | 0.198 | 0.416 | 0.446 | 0.755 | 0.240 | 0.400 | 0.228 |
| Randomized merits panels with en banc correction | 0.450 | 0.198 | 0.419 | 0.459 | 0.743 | 0.257 | 0.373 | 0.224 |
| Random panels with jurisdiction safeguards | 0.450 | 0.164 | 0.331 | 0.397 | 0.625 | 0.225 | 0.313 | 0.203 |
| Independent recusal enforcement with substitutes | 0.450 | 0.198 | 0.418 | 0.457 | 0.720 | 0.280 | 0.389 | 0.237 |
| Constitutional council with concrete-review backstop | 0.450 | 0.188 | 0.403 | 0.392 | 0.729 | 0.271 | 0.320 | 0.192 |
| Time-limited legislative override window | 0.450 | 0.200 | 0.427 | 0.463 | 0.741 | 0.252 | 0.368 | 0.225 |
| Automatic merits follow-up for emergency relief | 0.450 | 0.261 | 0.535 | 0.583 | 0.990 | 0.405 | 0.605 | 0.313 |
| Judicial review with legislative supermajority override | 0.450 | 0.197 | 0.416 | 0.460 | 0.730 | 0.278 | 0.384 | 0.228 |
| Emergency integrity package | 0.450 | 0.260 | 0.539 | 0.558 | 0.974 | 0.435 | 0.552 | 0.305 |
| Pre-enactment constitutional council | 0.450 | 0.196 | 0.412 | 0.438 | 0.730 | 0.219 | 0.363 | 0.219 |
| Stylized current U.S.-like supreme court | 0.450 | 0.239 | 0.484 | 0.485 | 0.984 | 0.396 | 0.520 | 0.269 |
| Supreme court with cross-checking constitutional court | 0.450 | 0.114 | 0.234 | 0.282 | 0.425 | 0.182 | 0.216 | 0.141 |
| Judicial electorate selection court | 0.450 | 0.200 | 0.422 | 0.477 | 0.740 | 0.268 | 0.382 | 0.235 |
| Dual supreme courts with disagreement filter | 0.450 | 0.201 | 0.412 | 0.482 | 0.772 | 0.279 | 0.416 | 0.228 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest emerg. irregularity | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Appointment Timing Manipulation | No emergency relief without merits review (0.613) | Automatic merits follow-up for emergency relief (0.645) | No emergency relief without merits review (0.009) | Judicial review with legislative supermajority override (0.020) |
| Emergency Application Flood | 60 percent invalidation threshold (0.496) | Stylized current U.S.-like supreme court (0.666) | No emergency relief without merits review (0.060) | Jurisdiction stripping constrained by rights carveouts (0.032) |
| Override Evasion Loop | Constitutional remand before invalidation (0.526) | No emergency relief without merits review (0.614) | No emergency relief without merits review (0.028) | Judicial review with legislative supermajority override (0.031) |
| Recusal Pressure Campaign | 60 percent invalidation threshold (0.522) | Stylized current U.S.-like supreme court (0.639) | No emergency relief without merits review (0.036) | Jurisdiction stripping constrained by rights carveouts (0.038) |
| Court Expansion Retaliation | Constitutional remand before invalidation (0.508) | Stylized current U.S.-like supreme court (0.626) | No emergency relief without merits review (0.037) | Jurisdiction stripping constrained by rights carveouts (0.048) |
