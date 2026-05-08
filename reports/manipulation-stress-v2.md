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

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.533); Constitutional remand before invalidation (0.532); Constitutional remand with override window (0.529); 18-year staggered terms + regular appointments (0.526); Public-interest litigation filter (0.525); Comparative 16-seat constitutional senates (0.525); Mandatory written emergency reasoning (0.523). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.533.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.638.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.034.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.271.
- Lowest partisan alignment: Jurisdiction stripping constrained by rights carveouts at 0.035.
- Highest public confidence index: Emergency integrity package at 0.595.
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
| 60 percent invalidation threshold | 0.533 | 0.589 | 0.247 | 0.635 | 0.392 | 0.522 | 0.606 | 0.168 | 0.622 | 0.486 | 0.200 | 0.179 | 0.460 | 0.131 | 0.306 | 0.304 | 0.208 |
| Constitutional remand before invalidation | 0.532 | 0.600 | 0.258 | 0.635 | 0.354 | 0.547 | 0.618 | 0.184 | 0.654 | 0.506 | 0.212 | 0.157 | 0.544 | 0.141 | 0.298 | 0.296 | 0.337 |
| Constitutional remand with override window | 0.529 | 0.598 | 0.253 | 0.635 | 0.355 | 0.547 | 0.612 | 0.167 | 0.673 | 0.506 | 0.206 | 0.178 | 0.540 | 0.107 | 0.308 | 0.295 | 0.369 |
| 18-year staggered terms + regular appointments | 0.526 | 0.587 | 0.246 | 0.635 | 0.391 | 0.524 | 0.615 | 0.202 | 0.553 | 0.486 | 0.210 | 0.156 | 0.481 | 0.140 | 0.294 | 0.308 | 0.212 |
| Public-interest litigation filter | 0.525 | 0.591 | 0.244 | 0.635 | 0.390 | 0.525 | 0.623 | 0.211 | 0.567 | 0.489 | 0.207 | 0.155 | 0.506 | 0.139 | 0.295 | 0.293 | 0.261 |
| Comparative 16-seat constitutional senates | 0.525 | 0.588 | 0.246 | 0.635 | 0.392 | 0.522 | 0.609 | 0.165 | 0.639 | 0.488 | 0.200 | 0.179 | 0.531 | 0.130 | 0.306 | 0.297 | 0.284 |
| Mandatory written emergency reasoning | 0.523 | 0.589 | 0.247 | 0.635 | 0.391 | 0.524 | 0.611 | 0.187 | 0.584 | 0.486 | 0.205 | 0.178 | 0.478 | 0.107 | 0.306 | 0.307 | 0.253 |
| No emergency relief without merits review | 0.523 | 0.589 | 0.244 | 0.635 | 0.386 | 0.532 | 0.633 | 0.267 | 0.483 | 0.494 | 0.212 | 0.120 | 0.588 | 0.034 | 0.271 | 0.296 | 0.252 |
| Nonpartisan commission appointments | 0.522 | 0.592 | 0.248 | 0.635 | 0.391 | 0.525 | 0.619 | 0.208 | 0.545 | 0.485 | 0.212 | 0.157 | 0.500 | 0.140 | 0.295 | 0.301 | 0.236 |
| Peer recusal + reasoned emergency docket | 0.521 | 0.588 | 0.246 | 0.635 | 0.391 | 0.525 | 0.617 | 0.203 | 0.552 | 0.486 | 0.210 | 0.156 | 0.490 | 0.140 | 0.294 | 0.308 | 0.242 |
| Jurisdiction stripping constrained by rights carveouts | 0.521 | 0.592 | 0.249 | 0.635 | 0.392 | 0.555 | 0.617 | 0.204 | 0.547 | 0.485 | 0.227 | 0.155 | 0.515 | 0.139 | 0.295 | 0.311 | 0.236 |
| Three-judge panels with en banc correction | 0.521 | 0.593 | 0.251 | 0.635 | 0.391 | 0.525 | 0.619 | 0.205 | 0.556 | 0.486 | 0.209 | 0.158 | 0.538 | 0.140 | 0.294 | 0.298 | 0.253 |
| Expanded 15-seat court | 0.521 | 0.587 | 0.241 | 0.635 | 0.391 | 0.525 | 0.616 | 0.202 | 0.548 | 0.488 | 0.205 | 0.154 | 0.500 | 0.138 | 0.297 | 0.306 | 0.249 |
| Retention-election accountability court | 0.520 | 0.592 | 0.249 | 0.635 | 0.391 | 0.526 | 0.604 | 0.203 | 0.551 | 0.485 | 0.213 | 0.155 | 0.503 | 0.139 | 0.294 | 0.302 | 0.236 |
| Stylized current U.S.-like supreme court | 0.520 | 0.585 | 0.240 | 0.635 | 0.400 | 0.514 | 0.638 | 0.243 | 0.525 | 0.469 | 0.217 | 0.246 | 0.316 | 0.373 | 0.374 | 0.336 | 0.166 |
| Randomized merits panels with en banc correction | 0.520 | 0.593 | 0.251 | 0.635 | 0.391 | 0.525 | 0.619 | 0.207 | 0.554 | 0.487 | 0.206 | 0.158 | 0.541 | 0.140 | 0.295 | 0.298 | 0.261 |
| Random panels with jurisdiction safeguards | 0.519 | 0.591 | 0.249 | 0.635 | 0.393 | 0.552 | 0.605 | 0.169 | 0.613 | 0.484 | 0.220 | 0.182 | 0.541 | 0.133 | 0.309 | 0.304 | 0.285 |
| Constitutional council with concrete-review backstop | 0.518 | 0.592 | 0.250 | 0.635 | 0.389 | 0.572 | 0.623 | 0.196 | 0.596 | 0.493 | 0.216 | 0.154 | 0.581 | 0.138 | 0.293 | 0.308 | 0.341 |
| Independent recusal enforcement with substitutes | 0.518 | 0.590 | 0.245 | 0.635 | 0.391 | 0.525 | 0.616 | 0.205 | 0.545 | 0.485 | 0.210 | 0.157 | 0.519 | 0.140 | 0.295 | 0.302 | 0.258 |
| Time-limited legislative override window | 0.518 | 0.592 | 0.251 | 0.635 | 0.392 | 0.527 | 0.618 | 0.205 | 0.546 | 0.482 | 0.218 | 0.157 | 0.506 | 0.140 | 0.295 | 0.313 | 0.243 |
| Automatic merits follow-up for emergency relief | 0.516 | 0.593 | 0.255 | 0.635 | 0.386 | 0.532 | 0.631 | 0.270 | 0.470 | 0.491 | 0.213 | 0.116 | 0.556 | 0.044 | 0.273 | 0.306 | 0.271 |
| Judicial review with legislative supermajority override | 0.516 | 0.592 | 0.252 | 0.635 | 0.392 | 0.525 | 0.620 | 0.206 | 0.543 | 0.481 | 0.223 | 0.157 | 0.508 | 0.139 | 0.296 | 0.316 | 0.244 |
| Emergency integrity package | 0.516 | 0.592 | 0.249 | 0.635 | 0.386 | 0.533 | 0.632 | 0.268 | 0.481 | 0.493 | 0.213 | 0.116 | 0.595 | 0.044 | 0.274 | 0.298 | 0.293 |
| Supreme court with cross-checking constitutional court | 0.516 | 0.590 | 0.247 | 0.635 | 0.371 | 0.542 | 0.586 | 0.113 | 0.659 | 0.495 | 0.201 | 0.179 | 0.504 | 0.131 | 0.308 | 0.293 | 0.324 |
| Pre-enactment constitutional council | 0.515 | 0.589 | 0.242 | 0.635 | 0.390 | 0.572 | 0.621 | 0.200 | 0.567 | 0.490 | 0.222 | 0.154 | 0.570 | 0.138 | 0.292 | 0.310 | 0.325 |
| Dual supreme courts with disagreement filter | 0.489 | 0.589 | 0.244 | 0.635 | 0.394 | 0.522 | 0.615 | 0.208 | 0.489 | 0.475 | 0.217 | 0.182 | 0.510 | 0.132 | 0.308 | 0.309 | 0.360 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.450 | 0.168 | 0.338 | 0.414 | 0.632 | 0.253 | 0.357 | 0.214 |
| Constitutional remand before invalidation | 0.450 | 0.184 | 0.399 | 0.394 | 0.649 | 0.246 | 0.336 | 0.214 |
| Constitutional remand with override window | 0.450 | 0.167 | 0.346 | 0.394 | 0.641 | 0.207 | 0.330 | 0.206 |
| 18-year staggered terms + regular appointments | 0.450 | 0.202 | 0.415 | 0.491 | 0.740 | 0.306 | 0.416 | 0.256 |
| Public-interest litigation filter | 0.450 | 0.211 | 0.447 | 0.471 | 0.761 | 0.302 | 0.400 | 0.282 |
| Comparative 16-seat constitutional senates | 0.450 | 0.165 | 0.338 | 0.374 | 0.645 | 0.201 | 0.322 | 0.190 |
| Mandatory written emergency reasoning | 0.450 | 0.187 | 0.375 | 0.465 | 0.720 | 0.257 | 0.344 | 0.247 |
| No emergency relief without merits review | 0.450 | 0.267 | 0.557 | 0.591 | 0.974 | 0.432 | 0.584 | 0.331 |
| Nonpartisan commission appointments | 0.450 | 0.208 | 0.446 | 0.476 | 0.740 | 0.294 | 0.438 | 0.250 |
| Peer recusal + reasoned emergency docket | 0.450 | 0.203 | 0.421 | 0.480 | 0.754 | 0.273 | 0.397 | 0.268 |
| Jurisdiction stripping constrained by rights carveouts | 0.450 | 0.204 | 0.430 | 0.466 | 0.749 | 0.300 | 0.430 | 0.247 |
| Three-judge panels with en banc correction | 0.450 | 0.205 | 0.433 | 0.485 | 0.732 | 0.251 | 0.373 | 0.268 |
| Expanded 15-seat court | 0.450 | 0.202 | 0.422 | 0.474 | 0.734 | 0.266 | 0.415 | 0.264 |
| Retention-election accountability court | 0.450 | 0.203 | 0.430 | 0.471 | 0.740 | 0.298 | 0.387 | 0.218 |
| Stylized current U.S.-like supreme court | 0.450 | 0.243 | 0.491 | 0.503 | 0.984 | 0.435 | 0.547 | 0.298 |
| Randomized merits panels with en banc correction | 0.450 | 0.207 | 0.434 | 0.483 | 0.754 | 0.309 | 0.424 | 0.246 |
| Random panels with jurisdiction safeguards | 0.450 | 0.169 | 0.345 | 0.406 | 0.626 | 0.249 | 0.327 | 0.215 |
| Constitutional council with concrete-review backstop | 0.450 | 0.196 | 0.422 | 0.405 | 0.722 | 0.270 | 0.357 | 0.220 |
| Independent recusal enforcement with substitutes | 0.450 | 0.205 | 0.429 | 0.478 | 0.753 | 0.305 | 0.376 | 0.262 |
| Time-limited legislative override window | 0.450 | 0.205 | 0.428 | 0.472 | 0.751 | 0.245 | 0.399 | 0.272 |
| Automatic merits follow-up for emergency relief | 0.450 | 0.270 | 0.554 | 0.599 | 0.982 | 0.445 | 0.610 | 0.349 |
| Judicial review with legislative supermajority override | 0.450 | 0.206 | 0.432 | 0.466 | 0.752 | 0.286 | 0.384 | 0.262 |
| Emergency integrity package | 0.450 | 0.268 | 0.554 | 0.583 | 0.979 | 0.435 | 0.574 | 0.339 |
| Supreme court with cross-checking constitutional court | 0.450 | 0.113 | 0.235 | 0.280 | 0.394 | 0.187 | 0.223 | 0.137 |
| Pre-enactment constitutional council | 0.450 | 0.200 | 0.429 | 0.449 | 0.727 | 0.245 | 0.397 | 0.224 |
| Dual supreme courts with disagreement filter | 0.450 | 0.208 | 0.420 | 0.506 | 0.777 | 0.310 | 0.411 | 0.293 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Appointment Timing Manipulation | No emergency relief without merits review (0.614) | No emergency relief without merits review (0.649) | No emergency relief without merits review (0.009) | Time-limited legislative override window (0.020) |
| Emergency Application Flood | 60 percent invalidation threshold (0.498) | Stylized current U.S.-like supreme court (0.666) | No emergency relief without merits review (0.061) | Jurisdiction stripping constrained by rights carveouts (0.033) |
| Override Evasion Loop | Constitutional remand before invalidation (0.525) | Automatic merits follow-up for emergency relief (0.618) | No emergency relief without merits review (0.028) | Dual supreme courts with disagreement filter (0.032) |
| Recusal Pressure Campaign | 60 percent invalidation threshold (0.521) | Stylized current U.S.-like supreme court (0.641) | No emergency relief without merits review (0.037) | Dual supreme courts with disagreement filter (0.039) |
| Court Expansion Retaliation | Constitutional remand before invalidation (0.510) | Stylized current U.S.-like supreme court (0.628) | No emergency relief without merits review (0.038) | Judicial review with legislative supermajority override (0.050) |
