# Constitutional Review Campaign v0

Deterministic simulation study for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 27
- experiment cases: 7

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

## Headline Findings

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.581); No emergency relief without merits review (0.580); Constitutional remand before invalidation (0.579); 18-year staggered terms + regular appointments (0.579); Public-interest litigation filter (0.577); Jurisdiction stripping constrained by rights carveouts (0.577); Nonpartisan commission appointments (0.576); Constitutional remand with override window (0.576); Mandatory written emergency reasoning (0.575); Peer recusal + reasoned emergency docket (0.575); Three-judge panels with en banc correction (0.574); Retention-election accountability court (0.574); Automatic merits follow-up for emergency relief (0.574); Randomized merits panels with en banc correction (0.573); Independent recusal enforcement with substitutes (0.573); Emergency integrity package (0.573); Expanded 15-seat court (0.572); Time-limited legislative override window (0.572); Comparative 16-seat constitutional senates (0.572); Judicial review with legislative supermajority override (0.571); Random panels with jurisdiction safeguards (0.571). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.581.
- Highest rights protection: No emergency relief without merits review at 0.637.
- Lowest emergency-process irregularity: No emergency relief without merits review at 0.019.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.210.
- Lowest partisan alignment: Time-limited legislative override window at 0.019.
- Highest modeled process-legitimacy index: Constitutional council with concrete-review backstop at 0.577.
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
| 60 percent invalidation threshold | 0.581 | 0.527 | 0.198 | 0.575 | 0.298 | 0.575 | 0.618 | 0.133 | 0.696 | 0.552 | 0.122 | 0.115 | 0.483 | 0.089 | 0.233 | 0.242 | 0.184 |
| No emergency relief without merits review | 0.580 | 0.533 | 0.205 | 0.575 | 0.293 | 0.582 | 0.637 | 0.190 | 0.645 | 0.560 | 0.124 | 0.080 | 0.573 | 0.019 | 0.210 | 0.230 | 0.226 |
| Constitutional remand before invalidation | 0.579 | 0.538 | 0.205 | 0.575 | 0.262 | 0.595 | 0.625 | 0.140 | 0.721 | 0.569 | 0.125 | 0.101 | 0.547 | 0.098 | 0.226 | 0.231 | 0.298 |
| 18-year staggered terms + regular appointments | 0.579 | 0.522 | 0.190 | 0.575 | 0.297 | 0.577 | 0.626 | 0.157 | 0.661 | 0.553 | 0.126 | 0.100 | 0.495 | 0.096 | 0.222 | 0.244 | 0.186 |
| Public-interest litigation filter | 0.577 | 0.533 | 0.203 | 0.575 | 0.296 | 0.577 | 0.633 | 0.167 | 0.669 | 0.553 | 0.124 | 0.100 | 0.516 | 0.097 | 0.225 | 0.231 | 0.233 |
| Jurisdiction stripping constrained by rights carveouts | 0.577 | 0.529 | 0.199 | 0.575 | 0.296 | 0.607 | 0.629 | 0.159 | 0.658 | 0.553 | 0.136 | 0.101 | 0.523 | 0.098 | 0.225 | 0.241 | 0.209 |
| Nonpartisan commission appointments | 0.576 | 0.531 | 0.200 | 0.575 | 0.297 | 0.577 | 0.628 | 0.158 | 0.662 | 0.552 | 0.126 | 0.101 | 0.511 | 0.098 | 0.225 | 0.238 | 0.210 |
| Constitutional remand with override window | 0.576 | 0.537 | 0.204 | 0.575 | 0.262 | 0.595 | 0.622 | 0.134 | 0.731 | 0.568 | 0.125 | 0.114 | 0.548 | 0.068 | 0.233 | 0.232 | 0.327 |
| Mandatory written emergency reasoning | 0.575 | 0.528 | 0.201 | 0.575 | 0.297 | 0.577 | 0.624 | 0.150 | 0.677 | 0.552 | 0.128 | 0.114 | 0.498 | 0.068 | 0.231 | 0.244 | 0.224 |
| Peer recusal + reasoned emergency docket | 0.575 | 0.526 | 0.198 | 0.575 | 0.297 | 0.577 | 0.626 | 0.158 | 0.662 | 0.553 | 0.125 | 0.100 | 0.503 | 0.097 | 0.224 | 0.244 | 0.215 |
| Three-judge panels with en banc correction | 0.574 | 0.532 | 0.201 | 0.575 | 0.296 | 0.577 | 0.628 | 0.157 | 0.667 | 0.553 | 0.121 | 0.101 | 0.550 | 0.098 | 0.224 | 0.234 | 0.225 |
| Retention-election accountability court | 0.574 | 0.534 | 0.205 | 0.575 | 0.297 | 0.578 | 0.620 | 0.155 | 0.665 | 0.551 | 0.132 | 0.101 | 0.514 | 0.098 | 0.226 | 0.240 | 0.210 |
| Automatic merits follow-up for emergency relief | 0.574 | 0.528 | 0.199 | 0.575 | 0.294 | 0.582 | 0.637 | 0.195 | 0.629 | 0.558 | 0.129 | 0.083 | 0.548 | 0.026 | 0.210 | 0.241 | 0.241 |
| Randomized merits panels with en banc correction | 0.573 | 0.529 | 0.196 | 0.575 | 0.297 | 0.577 | 0.627 | 0.156 | 0.668 | 0.553 | 0.125 | 0.101 | 0.550 | 0.098 | 0.224 | 0.235 | 0.232 |
| Independent recusal enforcement with substitutes | 0.573 | 0.529 | 0.198 | 0.575 | 0.297 | 0.577 | 0.627 | 0.158 | 0.662 | 0.552 | 0.125 | 0.101 | 0.524 | 0.098 | 0.225 | 0.237 | 0.230 |
| Emergency integrity package | 0.573 | 0.531 | 0.200 | 0.575 | 0.293 | 0.582 | 0.637 | 0.191 | 0.638 | 0.559 | 0.126 | 0.083 | 0.576 | 0.026 | 0.211 | 0.232 | 0.263 |
| Expanded 15-seat court | 0.572 | 0.524 | 0.195 | 0.575 | 0.297 | 0.577 | 0.626 | 0.155 | 0.654 | 0.553 | 0.124 | 0.101 | 0.506 | 0.098 | 0.227 | 0.245 | 0.222 |
| Time-limited legislative override window | 0.572 | 0.529 | 0.198 | 0.575 | 0.298 | 0.578 | 0.627 | 0.157 | 0.662 | 0.549 | 0.136 | 0.101 | 0.515 | 0.099 | 0.226 | 0.247 | 0.216 |
| Comparative 16-seat constitutional senates | 0.572 | 0.525 | 0.197 | 0.575 | 0.298 | 0.575 | 0.618 | 0.126 | 0.707 | 0.553 | 0.122 | 0.115 | 0.542 | 0.089 | 0.233 | 0.236 | 0.254 |
| Judicial review with legislative supermajority override | 0.571 | 0.528 | 0.198 | 0.575 | 0.298 | 0.577 | 0.628 | 0.157 | 0.660 | 0.549 | 0.137 | 0.100 | 0.516 | 0.097 | 0.223 | 0.248 | 0.216 |
| Random panels with jurisdiction safeguards | 0.571 | 0.529 | 0.195 | 0.575 | 0.298 | 0.605 | 0.618 | 0.135 | 0.694 | 0.551 | 0.134 | 0.116 | 0.554 | 0.090 | 0.233 | 0.236 | 0.255 |
| Pre-enactment constitutional council | 0.569 | 0.533 | 0.202 | 0.575 | 0.295 | 0.621 | 0.628 | 0.154 | 0.672 | 0.557 | 0.130 | 0.100 | 0.574 | 0.097 | 0.223 | 0.244 | 0.287 |
| Constitutional council with concrete-review backstop | 0.569 | 0.528 | 0.196 | 0.575 | 0.295 | 0.620 | 0.627 | 0.147 | 0.683 | 0.559 | 0.129 | 0.100 | 0.577 | 0.097 | 0.223 | 0.243 | 0.300 |
| Judicial electorate selection court | 0.568 | 0.531 | 0.200 | 0.575 | 0.297 | 0.577 | 0.629 | 0.161 | 0.661 | 0.552 | 0.126 | 0.101 | 0.532 | 0.098 | 0.226 | 0.232 | 0.270 |
| Stylized current U.S.-like supreme court | 0.564 | 0.528 | 0.199 | 0.575 | 0.307 | 0.568 | 0.635 | 0.173 | 0.626 | 0.530 | 0.157 | 0.167 | 0.356 | 0.288 | 0.300 | 0.276 | 0.149 |
| Supreme court with cross-checking constitutional court | 0.562 | 0.531 | 0.202 | 0.575 | 0.277 | 0.595 | 0.603 | 0.093 | 0.712 | 0.558 | 0.126 | 0.115 | 0.514 | 0.089 | 0.234 | 0.233 | 0.291 |
| Dual supreme courts with disagreement filter | 0.547 | 0.529 | 0.198 | 0.575 | 0.299 | 0.575 | 0.626 | 0.156 | 0.623 | 0.543 | 0.136 | 0.116 | 0.516 | 0.090 | 0.234 | 0.244 | 0.325 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.374 | 0.133 | 0.319 | 0.356 | 0.646 | 0.195 | 0.250 | 0.144 |
| No emergency relief without merits review | 0.374 | 0.190 | 0.456 | 0.431 | 0.947 | 0.284 | 0.371 | 0.211 |
| Constitutional remand before invalidation | 0.374 | 0.140 | 0.352 | 0.344 | 0.639 | 0.179 | 0.257 | 0.161 |
| 18-year staggered terms + regular appointments | 0.374 | 0.157 | 0.388 | 0.390 | 0.749 | 0.190 | 0.267 | 0.191 |
| Public-interest litigation filter | 0.374 | 0.167 | 0.418 | 0.396 | 0.758 | 0.244 | 0.316 | 0.195 |
| Jurisdiction stripping constrained by rights carveouts | 0.374 | 0.159 | 0.394 | 0.386 | 0.743 | 0.217 | 0.305 | 0.191 |
| Nonpartisan commission appointments | 0.374 | 0.158 | 0.390 | 0.385 | 0.739 | 0.229 | 0.320 | 0.195 |
| Constitutional remand with override window | 0.374 | 0.134 | 0.330 | 0.330 | 0.637 | 0.142 | 0.224 | 0.149 |
| Mandatory written emergency reasoning | 0.374 | 0.150 | 0.361 | 0.386 | 0.736 | 0.202 | 0.275 | 0.190 |
| Peer recusal + reasoned emergency docket | 0.374 | 0.158 | 0.386 | 0.403 | 0.742 | 0.226 | 0.286 | 0.209 |
| Three-judge panels with en banc correction | 0.374 | 0.157 | 0.387 | 0.406 | 0.724 | 0.204 | 0.316 | 0.203 |
| Retention-election accountability court | 0.374 | 0.155 | 0.385 | 0.382 | 0.719 | 0.205 | 0.279 | 0.181 |
| Automatic merits follow-up for emergency relief | 0.374 | 0.195 | 0.466 | 0.473 | 0.960 | 0.320 | 0.418 | 0.241 |
| Randomized merits panels with en banc correction | 0.374 | 0.156 | 0.388 | 0.403 | 0.735 | 0.194 | 0.235 | 0.199 |
| Independent recusal enforcement with substitutes | 0.374 | 0.158 | 0.389 | 0.398 | 0.729 | 0.220 | 0.321 | 0.201 |
| Emergency integrity package | 0.374 | 0.191 | 0.456 | 0.438 | 0.947 | 0.292 | 0.389 | 0.217 |
| Expanded 15-seat court | 0.374 | 0.155 | 0.381 | 0.409 | 0.730 | 0.211 | 0.292 | 0.187 |
| Time-limited legislative override window | 0.374 | 0.157 | 0.387 | 0.375 | 0.746 | 0.189 | 0.289 | 0.210 |
| Comparative 16-seat constitutional senates | 0.374 | 0.126 | 0.304 | 0.306 | 0.631 | 0.156 | 0.201 | 0.121 |
| Judicial review with legislative supermajority override | 0.374 | 0.157 | 0.382 | 0.371 | 0.747 | 0.258 | 0.329 | 0.217 |
| Random panels with jurisdiction safeguards | 0.374 | 0.135 | 0.326 | 0.359 | 0.642 | 0.187 | 0.285 | 0.166 |
| Pre-enactment constitutional council | 0.374 | 0.154 | 0.378 | 0.365 | 0.728 | 0.222 | 0.277 | 0.189 |
| Constitutional council with concrete-review backstop | 0.374 | 0.147 | 0.365 | 0.323 | 0.702 | 0.176 | 0.223 | 0.155 |
| Judicial electorate selection court | 0.374 | 0.161 | 0.395 | 0.410 | 0.749 | 0.248 | 0.315 | 0.213 |
| Stylized current U.S.-like supreme court | 0.374 | 0.173 | 0.390 | 0.397 | 0.964 | 0.304 | 0.373 | 0.208 |
| Supreme court with cross-checking constitutional court | 0.374 | 0.093 | 0.232 | 0.243 | 0.402 | 0.147 | 0.192 | 0.135 |
| Dual supreme courts with disagreement filter | 0.374 | 0.156 | 0.380 | 0.392 | 0.757 | 0.183 | 0.304 | 0.192 |

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
