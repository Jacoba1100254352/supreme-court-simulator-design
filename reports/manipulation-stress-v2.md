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

- Top directional-score cluster within 0.010 of the maximum: No emergency relief without merits review (0.533); 60 percent invalidation threshold (0.533); 18-year staggered terms + regular appointments (0.529); Jurisdiction stripping constrained by rights carveouts (0.528); Nonpartisan commission appointments (0.527); Mandatory written emergency reasoning (0.526); Peer recusal + reasoned emergency docket (0.526); Retention-election accountability court (0.525); Emergency integrity package (0.524); Constitutional remand before invalidation (0.524); Automatic merits follow-up for emergency relief (0.524); Three-judge panels with en banc correction (0.523). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: No emergency relief without merits review at 0.533.
- Highest rights protection: Automatic merits follow-up for emergency relief at 0.669.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.040.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.322.
- Lowest partisan alignment: Judicial review with legislative supermajority override at 0.043.
- Highest public confidence index: Constitutional council with concrete-review backstop at 0.667.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, claimant success, precedent durability, lower-court compliance, elite acceptance, and administrative feasibility.
- Empirical claims, synthetic findings, and speculative design recommendations should be read separately: source ranges only smoke-test plausibility, campaign outputs are synthetic, and design recommendations are conditional on the model assumptions.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Higher direct outputs such as `rightsClaimantSuccess`, `doctrinalDepth`, `remedialBreadth`, `precedentDurability`, `lowerCourtCompliance`, `eliteAcceptance`, and `publicConfidence` are usually better, but each should be read in domain context.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `emergencyLegitimacyRisk`, `emergencyDownstreamEffect`, `governmentNoncomplianceRate`, `reversalRate`, `constitutionalConflict`, `administrativeCost`, and `strategicPressure` are usually better.
- Petition, certiorari-admission, lower-court-split, lower-court-resistance, forum-shopping, settlement, strategic-plaintiff, repeat-player, enforcement-capacity, emergency-opportunism, emergency, emergency-downstream, replacement, recusal, concurrence, dissent, fragmentation, panel, en banc, council, cross-check, remand, public-interest, formal-response, practical-response, noncompliance, and override rates are diagnostic rather than automatically good or bad.

## Scenario Averages Across Cases

| Scenario | Directional | Admission | Cert admit | Lower split | Resistance | Enforcement | Rights protection | Claimant success | Precedent durability | Lower-court compliance | Gov. noncomp. | Emerg. downstream | Public confidence | Shadow abuse | Emergency risk | Strategic | Admin cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.533 | 0.751 | 0.640 | 0.634 | 0.381 | 0.529 | 0.666 | 0.230 | 0.685 | 0.450 | 0.236 | 0.143 | 0.658 | 0.040 | 0.329 | 0.294 | 0.302 |
| 60 percent invalidation threshold | 0.533 | 0.730 | 0.618 | 0.634 | 0.389 | 0.518 | 0.635 | 0.157 | 0.739 | 0.439 | 0.233 | 0.185 | 0.520 | 0.141 | 0.356 | 0.313 | 0.248 |
| 18-year staggered terms + regular appointments | 0.529 | 0.733 | 0.621 | 0.634 | 0.387 | 0.521 | 0.649 | 0.197 | 0.688 | 0.439 | 0.240 | 0.167 | 0.540 | 0.155 | 0.344 | 0.316 | 0.252 |
| Jurisdiction stripping constrained by rights carveouts | 0.528 | 0.745 | 0.634 | 0.634 | 0.387 | 0.552 | 0.652 | 0.199 | 0.691 | 0.438 | 0.255 | 0.171 | 0.583 | 0.157 | 0.349 | 0.308 | 0.280 |
| Nonpartisan commission appointments | 0.527 | 0.744 | 0.632 | 0.634 | 0.386 | 0.522 | 0.654 | 0.206 | 0.686 | 0.438 | 0.236 | 0.169 | 0.569 | 0.155 | 0.345 | 0.307 | 0.280 |
| Mandatory written emergency reasoning | 0.526 | 0.735 | 0.621 | 0.634 | 0.387 | 0.521 | 0.648 | 0.193 | 0.706 | 0.439 | 0.237 | 0.183 | 0.546 | 0.107 | 0.353 | 0.315 | 0.298 |
| Peer recusal + reasoned emergency docket | 0.526 | 0.731 | 0.618 | 0.634 | 0.387 | 0.522 | 0.652 | 0.201 | 0.687 | 0.440 | 0.239 | 0.167 | 0.552 | 0.153 | 0.342 | 0.314 | 0.285 |
| Retention-election accountability court | 0.525 | 0.747 | 0.634 | 0.634 | 0.387 | 0.523 | 0.639 | 0.195 | 0.695 | 0.436 | 0.248 | 0.168 | 0.571 | 0.155 | 0.347 | 0.306 | 0.280 |
| Emergency integrity package | 0.524 | 0.753 | 0.640 | 0.634 | 0.381 | 0.529 | 0.667 | 0.231 | 0.678 | 0.449 | 0.237 | 0.158 | 0.664 | 0.053 | 0.333 | 0.299 | 0.351 |
| Constitutional remand before invalidation | 0.524 | 0.770 | 0.661 | 0.634 | 0.352 | 0.547 | 0.651 | 0.184 | 0.758 | 0.449 | 0.252 | 0.173 | 0.623 | 0.159 | 0.357 | 0.307 | 0.406 |
| Automatic merits follow-up for emergency relief | 0.524 | 0.734 | 0.624 | 0.634 | 0.382 | 0.528 | 0.669 | 0.252 | 0.635 | 0.448 | 0.236 | 0.153 | 0.611 | 0.051 | 0.322 | 0.307 | 0.318 |
| Three-judge panels with en banc correction | 0.523 | 0.749 | 0.638 | 0.634 | 0.387 | 0.522 | 0.652 | 0.196 | 0.700 | 0.437 | 0.243 | 0.172 | 0.612 | 0.158 | 0.350 | 0.306 | 0.299 |
| Expanded 15-seat court | 0.523 | 0.729 | 0.615 | 0.634 | 0.387 | 0.522 | 0.650 | 0.198 | 0.677 | 0.441 | 0.239 | 0.167 | 0.562 | 0.153 | 0.348 | 0.314 | 0.292 |
| Judicial review with legislative supermajority override | 0.523 | 0.742 | 0.628 | 0.634 | 0.388 | 0.522 | 0.657 | 0.202 | 0.688 | 0.434 | 0.253 | 0.169 | 0.574 | 0.156 | 0.347 | 0.316 | 0.288 |
| Time-limited legislative override window | 0.523 | 0.746 | 0.630 | 0.634 | 0.388 | 0.523 | 0.656 | 0.199 | 0.692 | 0.434 | 0.253 | 0.170 | 0.575 | 0.156 | 0.348 | 0.317 | 0.289 |
| Randomized merits panels with en banc correction | 0.522 | 0.750 | 0.642 | 0.634 | 0.387 | 0.522 | 0.653 | 0.197 | 0.699 | 0.437 | 0.242 | 0.171 | 0.619 | 0.157 | 0.348 | 0.304 | 0.307 |
| Comparative 16-seat constitutional senates | 0.521 | 0.732 | 0.617 | 0.634 | 0.389 | 0.519 | 0.629 | 0.139 | 0.759 | 0.440 | 0.234 | 0.186 | 0.608 | 0.141 | 0.356 | 0.305 | 0.331 |
| Public-interest litigation filter | 0.521 | 0.781 | 0.674 | 0.634 | 0.387 | 0.524 | 0.666 | 0.219 | 0.695 | 0.430 | 0.252 | 0.177 | 0.579 | 0.163 | 0.364 | 0.308 | 0.323 |
| Independent recusal enforcement with substitutes | 0.520 | 0.750 | 0.643 | 0.634 | 0.387 | 0.523 | 0.656 | 0.209 | 0.678 | 0.435 | 0.248 | 0.171 | 0.594 | 0.157 | 0.351 | 0.309 | 0.307 |
| Random panels with jurisdiction safeguards | 0.520 | 0.746 | 0.638 | 0.634 | 0.389 | 0.549 | 0.638 | 0.168 | 0.735 | 0.434 | 0.252 | 0.190 | 0.624 | 0.145 | 0.360 | 0.305 | 0.336 |
| Constitutional remand with override window | 0.520 | 0.768 | 0.657 | 0.634 | 0.353 | 0.547 | 0.648 | 0.176 | 0.768 | 0.449 | 0.252 | 0.189 | 0.626 | 0.110 | 0.366 | 0.308 | 0.444 |
| Constitutional council with concrete-review backstop | 0.519 | 0.749 | 0.642 | 0.634 | 0.384 | 0.572 | 0.647 | 0.167 | 0.740 | 0.447 | 0.244 | 0.167 | 0.667 | 0.154 | 0.347 | 0.309 | 0.398 |
| Pre-enactment constitutional council | 0.518 | 0.748 | 0.636 | 0.634 | 0.385 | 0.571 | 0.652 | 0.183 | 0.717 | 0.443 | 0.250 | 0.169 | 0.653 | 0.156 | 0.347 | 0.314 | 0.382 |
| Stylized current U.S.-like supreme court | 0.514 | 0.729 | 0.614 | 0.634 | 0.399 | 0.507 | 0.665 | 0.226 | 0.635 | 0.410 | 0.255 | 0.256 | 0.336 | 0.424 | 0.441 | 0.347 | 0.199 |
| Supreme court with cross-checking constitutional court | 0.507 | 0.738 | 0.626 | 0.634 | 0.369 | 0.539 | 0.615 | 0.116 | 0.745 | 0.441 | 0.242 | 0.187 | 0.571 | 0.143 | 0.358 | 0.306 | 0.382 |
| Dual supreme courts with disagreement filter | 0.484 | 0.746 | 0.635 | 0.634 | 0.391 | 0.519 | 0.655 | 0.206 | 0.612 | 0.423 | 0.260 | 0.191 | 0.583 | 0.144 | 0.363 | 0.319 | 0.427 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.446 | 0.230 | 0.552 | 0.360 | 0.813 | 0.330 | 0.253 | 0.201 |
| 60 percent invalidation threshold | 0.446 | 0.157 | 0.375 | 0.267 | 0.536 | 0.173 | 0.170 | 0.169 |
| 18-year staggered terms + regular appointments | 0.446 | 0.197 | 0.469 | 0.330 | 0.661 | 0.295 | 0.211 | 0.219 |
| Jurisdiction stripping constrained by rights carveouts | 0.446 | 0.199 | 0.469 | 0.352 | 0.661 | 0.300 | 0.217 | 0.207 |
| Nonpartisan commission appointments | 0.446 | 0.206 | 0.486 | 0.350 | 0.678 | 0.316 | 0.244 | 0.231 |
| Mandatory written emergency reasoning | 0.446 | 0.193 | 0.451 | 0.354 | 0.671 | 0.284 | 0.197 | 0.213 |
| Peer recusal + reasoned emergency docket | 0.446 | 0.201 | 0.481 | 0.347 | 0.678 | 0.280 | 0.212 | 0.193 |
| Retention-election accountability court | 0.446 | 0.195 | 0.472 | 0.334 | 0.642 | 0.245 | 0.203 | 0.204 |
| Emergency integrity package | 0.446 | 0.231 | 0.560 | 0.349 | 0.802 | 0.346 | 0.265 | 0.197 |
| Constitutional remand before invalidation | 0.446 | 0.184 | 0.453 | 0.300 | 0.590 | 0.259 | 0.201 | 0.186 |
| Automatic merits follow-up for emergency relief | 0.446 | 0.252 | 0.586 | 0.439 | 0.860 | 0.424 | 0.320 | 0.262 |
| Three-judge panels with en banc correction | 0.446 | 0.196 | 0.473 | 0.318 | 0.636 | 0.282 | 0.210 | 0.207 |
| Expanded 15-seat court | 0.446 | 0.198 | 0.472 | 0.335 | 0.650 | 0.285 | 0.236 | 0.205 |
| Judicial review with legislative supermajority override | 0.446 | 0.202 | 0.480 | 0.348 | 0.685 | 0.264 | 0.245 | 0.221 |
| Time-limited legislative override window | 0.446 | 0.199 | 0.473 | 0.353 | 0.665 | 0.273 | 0.216 | 0.216 |
| Randomized merits panels with en banc correction | 0.446 | 0.197 | 0.481 | 0.317 | 0.653 | 0.275 | 0.210 | 0.212 |
| Comparative 16-seat constitutional senates | 0.446 | 0.139 | 0.352 | 0.209 | 0.502 | 0.127 | 0.102 | 0.104 |
| Public-interest litigation filter | 0.446 | 0.219 | 0.538 | 0.376 | 0.673 | 0.286 | 0.253 | 0.226 |
| Independent recusal enforcement with substitutes | 0.446 | 0.209 | 0.499 | 0.363 | 0.657 | 0.295 | 0.254 | 0.239 |
| Random panels with jurisdiction safeguards | 0.446 | 0.168 | 0.396 | 0.286 | 0.559 | 0.247 | 0.178 | 0.195 |
| Constitutional remand with override window | 0.446 | 0.176 | 0.422 | 0.310 | 0.597 | 0.243 | 0.179 | 0.189 |
| Constitutional council with concrete-review backstop | 0.446 | 0.167 | 0.437 | 0.229 | 0.577 | 0.144 | 0.124 | 0.131 |
| Pre-enactment constitutional council | 0.446 | 0.183 | 0.446 | 0.286 | 0.641 | 0.217 | 0.159 | 0.200 |
| Stylized current U.S.-like supreme court | 0.446 | 0.226 | 0.536 | 0.343 | 0.847 | 0.373 | 0.243 | 0.202 |
| Supreme court with cross-checking constitutional court | 0.446 | 0.116 | 0.279 | 0.219 | 0.356 | 0.161 | 0.118 | 0.137 |
| Dual supreme courts with disagreement filter | 0.446 | 0.206 | 0.494 | 0.347 | 0.688 | 0.287 | 0.225 | 0.232 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Appointment Timing Manipulation | No emergency relief without merits review (0.607) | Public-interest litigation filter (0.660) | No emergency relief without merits review (0.010) | Jurisdiction stripping constrained by rights carveouts (0.025) |
| Emergency Application Flood | No emergency relief without merits review (0.500) | Stylized current U.S.-like supreme court (0.691) | No emergency relief without merits review (0.072) | Judicial review with legislative supermajority override (0.042) |
| Override Evasion Loop | 60 percent invalidation threshold (0.528) | Public-interest litigation filter (0.658) | No emergency relief without merits review (0.033) | Time-limited legislative override window (0.040) |
| Recusal Pressure Campaign | No emergency relief without merits review (0.526) | Automatic merits follow-up for emergency relief (0.679) | No emergency relief without merits review (0.043) | Judicial review with legislative supermajority override (0.048) |
| Court Expansion Retaliation | 60 percent invalidation threshold (0.511) | Emergency integrity package (0.675) | No emergency relief without merits review (0.045) | Judicial review with legislative supermajority override (0.063) |
