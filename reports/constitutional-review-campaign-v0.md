# Constitutional Review Campaign v0

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 26
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

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.580); Constitutional remand before invalidation (0.578); No emergency relief without merits review (0.578); 18-year staggered terms + regular appointments (0.577); Jurisdiction stripping constrained by rights carveouts (0.575); Nonpartisan commission appointments (0.575); Constitutional remand with override window (0.575); Public-interest litigation filter (0.575); Mandatory written emergency reasoning (0.574); Peer recusal + reasoned emergency docket (0.573); Retention-election accountability court (0.573); Automatic merits follow-up for emergency relief (0.573); Three-judge panels with en banc correction (0.573); Emergency integrity package (0.572); Randomized merits panels with en banc correction (0.572); Expanded 15-seat court (0.572); Independent recusal enforcement with substitutes (0.571); Time-limited legislative override window (0.571); Comparative 16-seat constitutional senates (0.571); Judicial review with legislative supermajority override (0.570); Random panels with jurisdiction safeguards (0.570). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.580.
- Highest rights protection: Emergency integrity package at 0.642.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.019.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.214.
- Lowest partisan alignment: Time-limited legislative override window at 0.019.
- Highest public confidence index: Constitutional council with concrete-review backstop at 0.587.
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
| 60 percent invalidation threshold | 0.580 | 0.548 | 0.236 | 0.575 | 0.297 | 0.576 | 0.621 | 0.136 | 0.699 | 0.550 | 0.124 | 0.119 | 0.489 | 0.092 | 0.241 | 0.245 | 0.189 |
| Constitutional remand before invalidation | 0.578 | 0.556 | 0.238 | 0.575 | 0.261 | 0.596 | 0.628 | 0.144 | 0.724 | 0.569 | 0.126 | 0.103 | 0.556 | 0.100 | 0.232 | 0.233 | 0.305 |
| No emergency relief without merits review | 0.578 | 0.552 | 0.238 | 0.575 | 0.292 | 0.583 | 0.641 | 0.196 | 0.644 | 0.558 | 0.128 | 0.082 | 0.583 | 0.019 | 0.216 | 0.232 | 0.232 |
| 18-year staggered terms + regular appointments | 0.577 | 0.548 | 0.238 | 0.575 | 0.297 | 0.578 | 0.631 | 0.163 | 0.661 | 0.550 | 0.132 | 0.104 | 0.504 | 0.101 | 0.232 | 0.248 | 0.193 |
| Jurisdiction stripping constrained by rights carveouts | 0.575 | 0.550 | 0.235 | 0.575 | 0.296 | 0.608 | 0.632 | 0.162 | 0.659 | 0.551 | 0.142 | 0.103 | 0.531 | 0.101 | 0.232 | 0.243 | 0.215 |
| Nonpartisan commission appointments | 0.575 | 0.550 | 0.233 | 0.575 | 0.296 | 0.578 | 0.631 | 0.162 | 0.664 | 0.550 | 0.128 | 0.104 | 0.518 | 0.101 | 0.231 | 0.240 | 0.215 |
| Constitutional remand with override window | 0.575 | 0.555 | 0.235 | 0.575 | 0.261 | 0.596 | 0.624 | 0.135 | 0.735 | 0.568 | 0.126 | 0.116 | 0.556 | 0.069 | 0.240 | 0.233 | 0.335 |
| Public-interest litigation filter | 0.575 | 0.551 | 0.235 | 0.575 | 0.297 | 0.578 | 0.636 | 0.169 | 0.669 | 0.551 | 0.132 | 0.102 | 0.523 | 0.100 | 0.231 | 0.234 | 0.239 |
| Mandatory written emergency reasoning | 0.574 | 0.544 | 0.230 | 0.575 | 0.297 | 0.577 | 0.627 | 0.154 | 0.678 | 0.550 | 0.131 | 0.116 | 0.505 | 0.069 | 0.237 | 0.247 | 0.229 |
| Peer recusal + reasoned emergency docket | 0.573 | 0.545 | 0.231 | 0.575 | 0.296 | 0.578 | 0.630 | 0.161 | 0.663 | 0.551 | 0.127 | 0.103 | 0.508 | 0.100 | 0.230 | 0.247 | 0.221 |
| Retention-election accountability court | 0.573 | 0.552 | 0.239 | 0.575 | 0.297 | 0.579 | 0.623 | 0.159 | 0.667 | 0.550 | 0.133 | 0.102 | 0.522 | 0.100 | 0.231 | 0.241 | 0.215 |
| Automatic merits follow-up for emergency relief | 0.573 | 0.545 | 0.231 | 0.575 | 0.293 | 0.583 | 0.639 | 0.199 | 0.627 | 0.557 | 0.128 | 0.084 | 0.555 | 0.027 | 0.214 | 0.242 | 0.246 |
| Three-judge panels with en banc correction | 0.573 | 0.555 | 0.240 | 0.575 | 0.296 | 0.578 | 0.632 | 0.162 | 0.668 | 0.550 | 0.129 | 0.104 | 0.561 | 0.101 | 0.230 | 0.238 | 0.231 |
| Emergency integrity package | 0.572 | 0.552 | 0.238 | 0.575 | 0.292 | 0.583 | 0.642 | 0.196 | 0.640 | 0.558 | 0.126 | 0.084 | 0.586 | 0.027 | 0.216 | 0.233 | 0.270 |
| Randomized merits panels with en banc correction | 0.572 | 0.549 | 0.231 | 0.575 | 0.296 | 0.578 | 0.630 | 0.161 | 0.670 | 0.551 | 0.128 | 0.104 | 0.560 | 0.101 | 0.230 | 0.237 | 0.237 |
| Expanded 15-seat court | 0.572 | 0.545 | 0.231 | 0.575 | 0.296 | 0.578 | 0.630 | 0.160 | 0.655 | 0.551 | 0.127 | 0.103 | 0.516 | 0.099 | 0.232 | 0.247 | 0.227 |
| Independent recusal enforcement with substitutes | 0.571 | 0.549 | 0.234 | 0.575 | 0.297 | 0.578 | 0.631 | 0.163 | 0.661 | 0.550 | 0.131 | 0.104 | 0.534 | 0.100 | 0.231 | 0.240 | 0.236 |
| Time-limited legislative override window | 0.571 | 0.546 | 0.229 | 0.575 | 0.298 | 0.579 | 0.631 | 0.159 | 0.664 | 0.547 | 0.139 | 0.103 | 0.521 | 0.101 | 0.230 | 0.249 | 0.221 |
| Comparative 16-seat constitutional senates | 0.571 | 0.545 | 0.231 | 0.575 | 0.298 | 0.576 | 0.622 | 0.131 | 0.710 | 0.551 | 0.126 | 0.118 | 0.552 | 0.091 | 0.239 | 0.238 | 0.260 |
| Judicial review with legislative supermajority override | 0.570 | 0.551 | 0.236 | 0.575 | 0.298 | 0.578 | 0.633 | 0.162 | 0.662 | 0.547 | 0.141 | 0.104 | 0.523 | 0.101 | 0.232 | 0.251 | 0.222 |
| Random panels with jurisdiction safeguards | 0.570 | 0.554 | 0.240 | 0.575 | 0.297 | 0.606 | 0.623 | 0.141 | 0.696 | 0.549 | 0.138 | 0.119 | 0.566 | 0.092 | 0.240 | 0.239 | 0.263 |
| Pre-enactment constitutional council | 0.568 | 0.551 | 0.235 | 0.575 | 0.294 | 0.622 | 0.632 | 0.157 | 0.675 | 0.556 | 0.132 | 0.102 | 0.583 | 0.100 | 0.230 | 0.246 | 0.294 |
| Constitutional council with concrete-review backstop | 0.567 | 0.549 | 0.234 | 0.575 | 0.295 | 0.622 | 0.631 | 0.150 | 0.685 | 0.557 | 0.133 | 0.102 | 0.587 | 0.100 | 0.230 | 0.245 | 0.308 |
| Stylized current U.S.-like supreme court | 0.562 | 0.547 | 0.233 | 0.575 | 0.307 | 0.569 | 0.640 | 0.179 | 0.624 | 0.526 | 0.165 | 0.171 | 0.360 | 0.297 | 0.309 | 0.279 | 0.153 |
| Supreme court with cross-checking constitutional court | 0.561 | 0.549 | 0.233 | 0.575 | 0.277 | 0.596 | 0.606 | 0.096 | 0.712 | 0.556 | 0.129 | 0.118 | 0.521 | 0.092 | 0.240 | 0.236 | 0.298 |
| Dual supreme courts with disagreement filter | 0.545 | 0.547 | 0.233 | 0.575 | 0.299 | 0.576 | 0.629 | 0.162 | 0.621 | 0.542 | 0.137 | 0.120 | 0.524 | 0.092 | 0.242 | 0.247 | 0.333 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.374 | 0.136 | 0.327 | 0.351 | 0.647 | 0.191 | 0.246 | 0.184 |
| Constitutional remand before invalidation | 0.374 | 0.144 | 0.363 | 0.348 | 0.638 | 0.194 | 0.276 | 0.164 |
| No emergency relief without merits review | 0.374 | 0.196 | 0.469 | 0.458 | 0.949 | 0.340 | 0.355 | 0.236 |
| 18-year staggered terms + regular appointments | 0.374 | 0.163 | 0.404 | 0.402 | 0.745 | 0.245 | 0.318 | 0.213 |
| Jurisdiction stripping constrained by rights carveouts | 0.374 | 0.162 | 0.404 | 0.403 | 0.737 | 0.213 | 0.323 | 0.191 |
| Nonpartisan commission appointments | 0.374 | 0.162 | 0.401 | 0.404 | 0.744 | 0.243 | 0.308 | 0.205 |
| Constitutional remand with override window | 0.374 | 0.135 | 0.332 | 0.328 | 0.642 | 0.170 | 0.275 | 0.154 |
| Public-interest litigation filter | 0.374 | 0.169 | 0.432 | 0.401 | 0.744 | 0.242 | 0.313 | 0.220 |
| Mandatory written emergency reasoning | 0.374 | 0.154 | 0.375 | 0.388 | 0.723 | 0.244 | 0.302 | 0.202 |
| Peer recusal + reasoned emergency docket | 0.374 | 0.161 | 0.397 | 0.395 | 0.744 | 0.249 | 0.295 | 0.209 |
| Retention-election accountability court | 0.374 | 0.159 | 0.398 | 0.366 | 0.722 | 0.208 | 0.297 | 0.176 |
| Automatic merits follow-up for emergency relief | 0.374 | 0.199 | 0.474 | 0.488 | 0.963 | 0.323 | 0.458 | 0.254 |
| Three-judge panels with en banc correction | 0.374 | 0.162 | 0.404 | 0.406 | 0.724 | 0.236 | 0.326 | 0.194 |
| Emergency integrity package | 0.374 | 0.196 | 0.473 | 0.448 | 0.943 | 0.314 | 0.388 | 0.253 |
| Randomized merits panels with en banc correction | 0.374 | 0.161 | 0.404 | 0.414 | 0.729 | 0.209 | 0.298 | 0.208 |
| Expanded 15-seat court | 0.374 | 0.160 | 0.397 | 0.398 | 0.745 | 0.234 | 0.295 | 0.200 |
| Independent recusal enforcement with substitutes | 0.374 | 0.163 | 0.404 | 0.401 | 0.730 | 0.238 | 0.306 | 0.237 |
| Time-limited legislative override window | 0.374 | 0.159 | 0.393 | 0.380 | 0.751 | 0.212 | 0.272 | 0.222 |
| Comparative 16-seat constitutional senates | 0.374 | 0.131 | 0.318 | 0.308 | 0.627 | 0.150 | 0.215 | 0.139 |
| Judicial review with legislative supermajority override | 0.374 | 0.162 | 0.405 | 0.387 | 0.737 | 0.203 | 0.337 | 0.203 |
| Random panels with jurisdiction safeguards | 0.374 | 0.141 | 0.344 | 0.374 | 0.649 | 0.200 | 0.302 | 0.203 |
| Pre-enactment constitutional council | 0.374 | 0.157 | 0.395 | 0.357 | 0.721 | 0.199 | 0.299 | 0.186 |
| Constitutional council with concrete-review backstop | 0.374 | 0.150 | 0.374 | 0.331 | 0.699 | 0.184 | 0.246 | 0.162 |
| Stylized current U.S.-like supreme court | 0.374 | 0.179 | 0.406 | 0.426 | 0.963 | 0.337 | 0.391 | 0.223 |
| Supreme court with cross-checking constitutional court | 0.374 | 0.096 | 0.235 | 0.283 | 0.413 | 0.175 | 0.193 | 0.133 |
| Dual supreme courts with disagreement filter | 0.374 | 0.162 | 0.392 | 0.416 | 0.749 | 0.215 | 0.330 | 0.227 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | No emergency relief without merits review (0.609) | Automatic merits follow-up for emergency relief (0.649) | No emergency relief without merits review (0.011) | Time-limited legislative override window (0.015) |
| Partisan Appointment Pressure | No emergency relief without merits review (0.610) | No emergency relief without merits review (0.648) | No emergency relief without merits review (0.011) | Dual supreme courts with disagreement filter (0.017) |
| Rights-Risk Legislation | Constitutional remand before invalidation (0.550) | No emergency relief without merits review (0.611) | No emergency relief without merits review (0.018) | Dual supreme courts with disagreement filter (0.020) |
| Shadow-Docket Stress | 60 percent invalidation threshold (0.547) | Stylized current U.S.-like supreme court (0.667) | No emergency relief without merits review (0.037) | Time-limited legislative override window (0.022) |
| High Democratic Mandate | No emergency relief without merits review (0.630) | Public-interest litigation filter (0.649) | No emergency relief without merits review (0.008) | Dual supreme courts with disagreement filter (0.009) |
| Constitutional Conflict | Constitutional remand before invalidation (0.518) | Stylized current U.S.-like supreme court (0.645) | No emergency relief without merits review (0.039) | Time-limited legislative override window (0.034) |
| Imported Legislative Output | No emergency relief without merits review (0.616) | Emergency integrity package (0.654) | No emergency relief without merits review (0.010) | Time-limited legislative override window (0.014) |
