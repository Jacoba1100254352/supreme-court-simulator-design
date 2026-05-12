# Constitutional Review Campaign v0

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

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
| Imported Legislative Output | 1.000 | neutral/imported blend | Docket assumptions derived from a legislative simulator campaign CSV. |

## Headline Findings

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.581); No emergency relief without merits review (0.580); Constitutional remand before invalidation (0.579); 18-year staggered terms + regular appointments (0.579); Jurisdiction stripping constrained by rights carveouts (0.577); Public-interest litigation filter (0.577); Nonpartisan commission appointments (0.576); Constitutional remand with override window (0.576); Peer recusal + reasoned emergency docket (0.575); Mandatory written emergency reasoning (0.575); Retention-election accountability court (0.574); Automatic merits follow-up for emergency relief (0.574); Three-judge panels with en banc correction (0.574); Randomized merits panels with en banc correction (0.574); Emergency integrity package (0.573); Expanded 15-seat court (0.573); Independent recusal enforcement with substitutes (0.573); Time-limited legislative override window (0.572); Comparative 16-seat constitutional senates (0.572); Judicial review with legislative supermajority override (0.572); Random panels with jurisdiction safeguards (0.571). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.581.
- Highest rights protection: No emergency relief without merits review at 0.637.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.019.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.208.
- Lowest partisan alignment: Time-limited legislative override window at 0.019.
- Highest public confidence index: Constitutional council with concrete-review backstop at 0.576.
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
| 60 percent invalidation threshold | 0.581 | 0.522 | 0.190 | 0.575 | 0.298 | 0.575 | 0.617 | 0.131 | 0.695 | 0.552 | 0.122 | 0.115 | 0.480 | 0.088 | 0.233 | 0.242 | 0.182 |
| No emergency relief without merits review | 0.580 | 0.530 | 0.197 | 0.575 | 0.293 | 0.582 | 0.637 | 0.188 | 0.646 | 0.561 | 0.121 | 0.079 | 0.571 | 0.019 | 0.209 | 0.229 | 0.225 |
| Constitutional remand before invalidation | 0.579 | 0.535 | 0.200 | 0.575 | 0.262 | 0.595 | 0.624 | 0.139 | 0.721 | 0.570 | 0.124 | 0.100 | 0.546 | 0.097 | 0.225 | 0.231 | 0.296 |
| 18-year staggered terms + regular appointments | 0.579 | 0.519 | 0.184 | 0.575 | 0.297 | 0.576 | 0.625 | 0.156 | 0.661 | 0.553 | 0.127 | 0.099 | 0.494 | 0.096 | 0.221 | 0.243 | 0.185 |
| Jurisdiction stripping constrained by rights carveouts | 0.577 | 0.526 | 0.193 | 0.575 | 0.296 | 0.607 | 0.628 | 0.158 | 0.659 | 0.554 | 0.135 | 0.100 | 0.521 | 0.097 | 0.222 | 0.240 | 0.208 |
| Public-interest litigation filter | 0.577 | 0.528 | 0.195 | 0.575 | 0.296 | 0.577 | 0.631 | 0.165 | 0.667 | 0.554 | 0.123 | 0.099 | 0.514 | 0.096 | 0.223 | 0.231 | 0.231 |
| Nonpartisan commission appointments | 0.576 | 0.525 | 0.189 | 0.575 | 0.297 | 0.577 | 0.626 | 0.156 | 0.663 | 0.552 | 0.126 | 0.100 | 0.509 | 0.097 | 0.223 | 0.237 | 0.208 |
| Constitutional remand with override window | 0.576 | 0.531 | 0.194 | 0.575 | 0.262 | 0.594 | 0.620 | 0.132 | 0.731 | 0.569 | 0.125 | 0.113 | 0.545 | 0.068 | 0.232 | 0.231 | 0.325 |
| Peer recusal + reasoned emergency docket | 0.575 | 0.521 | 0.189 | 0.575 | 0.297 | 0.577 | 0.624 | 0.155 | 0.662 | 0.554 | 0.123 | 0.100 | 0.500 | 0.097 | 0.223 | 0.243 | 0.214 |
| Mandatory written emergency reasoning | 0.575 | 0.524 | 0.193 | 0.575 | 0.297 | 0.576 | 0.624 | 0.150 | 0.674 | 0.552 | 0.128 | 0.113 | 0.497 | 0.067 | 0.230 | 0.244 | 0.223 |
| Retention-election accountability court | 0.574 | 0.529 | 0.196 | 0.575 | 0.297 | 0.578 | 0.619 | 0.155 | 0.664 | 0.552 | 0.129 | 0.100 | 0.513 | 0.098 | 0.225 | 0.239 | 0.209 |
| Automatic merits follow-up for emergency relief | 0.574 | 0.522 | 0.188 | 0.575 | 0.294 | 0.582 | 0.635 | 0.193 | 0.629 | 0.558 | 0.127 | 0.082 | 0.546 | 0.026 | 0.208 | 0.240 | 0.239 |
| Three-judge panels with en banc correction | 0.574 | 0.525 | 0.189 | 0.575 | 0.297 | 0.577 | 0.627 | 0.156 | 0.665 | 0.553 | 0.123 | 0.101 | 0.547 | 0.097 | 0.222 | 0.234 | 0.224 |
| Randomized merits panels with en banc correction | 0.574 | 0.525 | 0.187 | 0.575 | 0.297 | 0.577 | 0.626 | 0.155 | 0.669 | 0.554 | 0.123 | 0.100 | 0.549 | 0.097 | 0.222 | 0.234 | 0.230 |
| Emergency integrity package | 0.573 | 0.527 | 0.192 | 0.575 | 0.293 | 0.582 | 0.637 | 0.190 | 0.639 | 0.560 | 0.125 | 0.082 | 0.574 | 0.026 | 0.209 | 0.231 | 0.261 |
| Expanded 15-seat court | 0.573 | 0.521 | 0.189 | 0.575 | 0.297 | 0.577 | 0.626 | 0.156 | 0.655 | 0.554 | 0.124 | 0.101 | 0.506 | 0.097 | 0.226 | 0.244 | 0.221 |
| Independent recusal enforcement with substitutes | 0.573 | 0.525 | 0.190 | 0.575 | 0.297 | 0.577 | 0.627 | 0.157 | 0.661 | 0.552 | 0.126 | 0.101 | 0.523 | 0.097 | 0.224 | 0.237 | 0.229 |
| Time-limited legislative override window | 0.572 | 0.525 | 0.190 | 0.575 | 0.298 | 0.578 | 0.627 | 0.156 | 0.662 | 0.550 | 0.136 | 0.100 | 0.513 | 0.097 | 0.223 | 0.246 | 0.215 |
| Comparative 16-seat constitutional senates | 0.572 | 0.523 | 0.193 | 0.575 | 0.298 | 0.574 | 0.617 | 0.126 | 0.707 | 0.553 | 0.122 | 0.114 | 0.541 | 0.089 | 0.231 | 0.236 | 0.253 |
| Judicial review with legislative supermajority override | 0.572 | 0.526 | 0.194 | 0.575 | 0.298 | 0.577 | 0.627 | 0.156 | 0.661 | 0.550 | 0.135 | 0.100 | 0.514 | 0.097 | 0.222 | 0.248 | 0.215 |
| Random panels with jurisdiction safeguards | 0.571 | 0.527 | 0.192 | 0.575 | 0.298 | 0.605 | 0.618 | 0.135 | 0.693 | 0.552 | 0.133 | 0.116 | 0.553 | 0.090 | 0.234 | 0.236 | 0.255 |
| Constitutional council with concrete-review backstop | 0.569 | 0.523 | 0.187 | 0.575 | 0.295 | 0.620 | 0.626 | 0.146 | 0.682 | 0.560 | 0.127 | 0.098 | 0.576 | 0.095 | 0.221 | 0.241 | 0.298 |
| Pre-enactment constitutional council | 0.569 | 0.527 | 0.194 | 0.575 | 0.295 | 0.620 | 0.627 | 0.152 | 0.671 | 0.558 | 0.129 | 0.100 | 0.571 | 0.097 | 0.223 | 0.243 | 0.286 |
| Judicial electorate selection court | 0.568 | 0.528 | 0.193 | 0.575 | 0.297 | 0.577 | 0.627 | 0.159 | 0.663 | 0.553 | 0.127 | 0.101 | 0.531 | 0.097 | 0.225 | 0.231 | 0.269 |
| Stylized current U.S.-like supreme court | 0.564 | 0.525 | 0.191 | 0.575 | 0.307 | 0.568 | 0.634 | 0.171 | 0.627 | 0.530 | 0.157 | 0.167 | 0.355 | 0.287 | 0.299 | 0.275 | 0.149 |
| Supreme court with cross-checking constitutional court | 0.563 | 0.526 | 0.193 | 0.575 | 0.277 | 0.595 | 0.602 | 0.091 | 0.711 | 0.558 | 0.125 | 0.114 | 0.512 | 0.088 | 0.231 | 0.232 | 0.289 |
| Dual supreme courts with disagreement filter | 0.547 | 0.523 | 0.189 | 0.575 | 0.300 | 0.574 | 0.625 | 0.155 | 0.623 | 0.544 | 0.135 | 0.116 | 0.513 | 0.089 | 0.233 | 0.243 | 0.323 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.374 | 0.131 | 0.308 | 0.352 | 0.661 | 0.205 | 0.263 | 0.150 |
| No emergency relief without merits review | 0.374 | 0.188 | 0.451 | 0.421 | 0.946 | 0.287 | 0.367 | 0.201 |
| Constitutional remand before invalidation | 0.374 | 0.139 | 0.351 | 0.330 | 0.640 | 0.182 | 0.262 | 0.167 |
| 18-year staggered terms + regular appointments | 0.374 | 0.156 | 0.384 | 0.399 | 0.753 | 0.180 | 0.283 | 0.178 |
| Jurisdiction stripping constrained by rights carveouts | 0.374 | 0.158 | 0.390 | 0.390 | 0.736 | 0.211 | 0.298 | 0.182 |
| Public-interest litigation filter | 0.374 | 0.165 | 0.411 | 0.407 | 0.758 | 0.234 | 0.302 | 0.196 |
| Nonpartisan commission appointments | 0.374 | 0.156 | 0.387 | 0.383 | 0.734 | 0.209 | 0.301 | 0.195 |
| Constitutional remand with override window | 0.374 | 0.132 | 0.322 | 0.325 | 0.638 | 0.158 | 0.223 | 0.158 |
| Peer recusal + reasoned emergency docket | 0.374 | 0.155 | 0.376 | 0.392 | 0.730 | 0.217 | 0.297 | 0.221 |
| Mandatory written emergency reasoning | 0.374 | 0.150 | 0.364 | 0.400 | 0.727 | 0.212 | 0.283 | 0.184 |
| Retention-election accountability court | 0.374 | 0.155 | 0.386 | 0.372 | 0.723 | 0.188 | 0.291 | 0.171 |
| Automatic merits follow-up for emergency relief | 0.374 | 0.193 | 0.460 | 0.466 | 0.963 | 0.305 | 0.430 | 0.231 |
| Three-judge panels with en banc correction | 0.374 | 0.156 | 0.388 | 0.402 | 0.726 | 0.191 | 0.294 | 0.194 |
| Randomized merits panels with en banc correction | 0.374 | 0.155 | 0.384 | 0.393 | 0.737 | 0.181 | 0.250 | 0.188 |
| Emergency integrity package | 0.374 | 0.190 | 0.455 | 0.439 | 0.950 | 0.289 | 0.363 | 0.216 |
| Expanded 15-seat court | 0.374 | 0.156 | 0.382 | 0.418 | 0.741 | 0.210 | 0.315 | 0.181 |
| Independent recusal enforcement with substitutes | 0.374 | 0.157 | 0.387 | 0.404 | 0.724 | 0.219 | 0.318 | 0.200 |
| Time-limited legislative override window | 0.374 | 0.156 | 0.389 | 0.359 | 0.727 | 0.213 | 0.279 | 0.200 |
| Comparative 16-seat constitutional senates | 0.374 | 0.126 | 0.306 | 0.299 | 0.623 | 0.156 | 0.196 | 0.122 |
| Judicial review with legislative supermajority override | 0.374 | 0.156 | 0.381 | 0.371 | 0.737 | 0.249 | 0.321 | 0.201 |
| Random panels with jurisdiction safeguards | 0.374 | 0.135 | 0.327 | 0.344 | 0.658 | 0.169 | 0.287 | 0.154 |
| Constitutional council with concrete-review backstop | 0.374 | 0.146 | 0.362 | 0.325 | 0.716 | 0.168 | 0.216 | 0.149 |
| Pre-enactment constitutional council | 0.374 | 0.152 | 0.373 | 0.367 | 0.723 | 0.217 | 0.279 | 0.169 |
| Judicial electorate selection court | 0.374 | 0.159 | 0.392 | 0.375 | 0.744 | 0.238 | 0.316 | 0.196 |
| Stylized current U.S.-like supreme court | 0.374 | 0.171 | 0.382 | 0.400 | 0.962 | 0.300 | 0.390 | 0.206 |
| Supreme court with cross-checking constitutional court | 0.374 | 0.091 | 0.226 | 0.242 | 0.408 | 0.123 | 0.170 | 0.126 |
| Dual supreme courts with disagreement filter | 0.374 | 0.155 | 0.376 | 0.377 | 0.746 | 0.188 | 0.319 | 0.192 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | No emergency relief without merits review (0.610) | No emergency relief without merits review (0.646) | No emergency relief without merits review (0.011) | Jurisdiction stripping constrained by rights carveouts (0.014) |
| Partisan Appointment Pressure | No emergency relief without merits review (0.608) | No emergency relief without merits review (0.640) | No emergency relief without merits review (0.011) | Dual supreme courts with disagreement filter (0.017) |
| Rights-Risk Legislation | Constitutional remand before invalidation (0.549) | Emergency integrity package (0.605) | No emergency relief without merits review (0.018) | Dual supreme courts with disagreement filter (0.020) |
| Shadow-Docket Stress | 60 percent invalidation threshold (0.548) | Stylized current U.S.-like supreme court (0.662) | No emergency relief without merits review (0.037) | Time-limited legislative override window (0.021) |
| High Democratic Mandate | No emergency relief without merits review (0.629) | Automatic merits follow-up for emergency relief (0.643) | No emergency relief without merits review (0.008) | Dual supreme courts with disagreement filter (0.009) |
| Constitutional Conflict | Constitutional remand before invalidation (0.522) | Stylized current U.S.-like supreme court (0.641) | No emergency relief without merits review (0.037) | Judicial review with legislative supermajority override (0.033) |
| Imported Legislative Output | No emergency relief without merits review (0.616) | Automatic merits follow-up for emergency relief (0.647) | No emergency relief without merits review (0.009) | Time-limited legislative override window (0.013) |
