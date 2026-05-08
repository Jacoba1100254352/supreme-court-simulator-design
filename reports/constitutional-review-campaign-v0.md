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

- Top directional-score cluster within 0.010 of the maximum: 60 percent invalidation threshold (0.581); No emergency relief without merits review (0.579); Constitutional remand before invalidation (0.579); 18-year staggered terms + regular appointments (0.578); Jurisdiction stripping constrained by rights carveouts (0.576); Constitutional remand with override window (0.576); Public-interest litigation filter (0.575); Nonpartisan commission appointments (0.575); Mandatory written emergency reasoning (0.574); Retention-election accountability court (0.574); Peer recusal + reasoned emergency docket (0.574); Three-judge panels with en banc correction (0.574); Automatic merits follow-up for emergency relief (0.573); Randomized merits panels with en banc correction (0.573); Emergency integrity package (0.573); Time-limited legislative override window (0.572); Expanded 15-seat court (0.572); Independent recusal enforcement with substitutes (0.572); Judicial review with legislative supermajority override (0.572); Comparative 16-seat constitutional senates (0.571). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: 60 percent invalidation threshold at 0.581.
- Highest rights protection: Emergency integrity package at 0.641.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.019.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.210.
- Lowest partisan alignment: Time-limited legislative override window at 0.019.
- Highest public confidence index: Constitutional council with concrete-review backstop at 0.589.
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
| 60 percent invalidation threshold | 0.581 | 0.545 | 0.232 | 0.575 | 0.298 | 0.576 | 0.620 | 0.136 | 0.699 | 0.550 | 0.126 | 0.117 | 0.490 | 0.090 | 0.234 | 0.244 | 0.187 |
| No emergency relief without merits review | 0.579 | 0.551 | 0.237 | 0.575 | 0.293 | 0.583 | 0.641 | 0.195 | 0.643 | 0.558 | 0.129 | 0.080 | 0.583 | 0.019 | 0.211 | 0.231 | 0.231 |
| Constitutional remand before invalidation | 0.579 | 0.556 | 0.238 | 0.575 | 0.261 | 0.597 | 0.628 | 0.144 | 0.723 | 0.568 | 0.130 | 0.101 | 0.558 | 0.098 | 0.227 | 0.233 | 0.304 |
| 18-year staggered terms + regular appointments | 0.578 | 0.547 | 0.236 | 0.575 | 0.297 | 0.578 | 0.631 | 0.164 | 0.661 | 0.551 | 0.131 | 0.102 | 0.506 | 0.098 | 0.227 | 0.247 | 0.192 |
| Jurisdiction stripping constrained by rights carveouts | 0.576 | 0.549 | 0.233 | 0.575 | 0.296 | 0.608 | 0.631 | 0.163 | 0.660 | 0.551 | 0.141 | 0.102 | 0.533 | 0.098 | 0.225 | 0.241 | 0.213 |
| Constitutional remand with override window | 0.576 | 0.557 | 0.239 | 0.575 | 0.261 | 0.596 | 0.625 | 0.136 | 0.736 | 0.567 | 0.127 | 0.115 | 0.558 | 0.069 | 0.236 | 0.232 | 0.335 |
| Public-interest litigation filter | 0.575 | 0.554 | 0.240 | 0.575 | 0.297 | 0.578 | 0.636 | 0.170 | 0.668 | 0.551 | 0.133 | 0.101 | 0.526 | 0.098 | 0.227 | 0.233 | 0.239 |
| Nonpartisan commission appointments | 0.575 | 0.552 | 0.238 | 0.575 | 0.297 | 0.578 | 0.631 | 0.163 | 0.661 | 0.549 | 0.133 | 0.102 | 0.521 | 0.099 | 0.227 | 0.239 | 0.214 |
| Mandatory written emergency reasoning | 0.574 | 0.547 | 0.234 | 0.575 | 0.297 | 0.578 | 0.627 | 0.155 | 0.677 | 0.550 | 0.131 | 0.115 | 0.506 | 0.069 | 0.234 | 0.246 | 0.229 |
| Retention-election accountability court | 0.574 | 0.551 | 0.236 | 0.575 | 0.297 | 0.579 | 0.623 | 0.161 | 0.666 | 0.550 | 0.135 | 0.101 | 0.523 | 0.098 | 0.226 | 0.240 | 0.214 |
| Peer recusal + reasoned emergency docket | 0.574 | 0.545 | 0.230 | 0.575 | 0.297 | 0.578 | 0.629 | 0.161 | 0.662 | 0.551 | 0.130 | 0.101 | 0.511 | 0.098 | 0.225 | 0.245 | 0.220 |
| Three-judge panels with en banc correction | 0.574 | 0.554 | 0.240 | 0.575 | 0.296 | 0.578 | 0.630 | 0.161 | 0.669 | 0.551 | 0.128 | 0.103 | 0.562 | 0.099 | 0.225 | 0.236 | 0.230 |
| Automatic merits follow-up for emergency relief | 0.573 | 0.543 | 0.228 | 0.575 | 0.293 | 0.583 | 0.638 | 0.198 | 0.626 | 0.557 | 0.130 | 0.083 | 0.555 | 0.026 | 0.210 | 0.242 | 0.245 |
| Randomized merits panels with en banc correction | 0.573 | 0.549 | 0.230 | 0.575 | 0.297 | 0.578 | 0.630 | 0.160 | 0.671 | 0.551 | 0.130 | 0.101 | 0.562 | 0.098 | 0.224 | 0.235 | 0.236 |
| Emergency integrity package | 0.573 | 0.554 | 0.240 | 0.575 | 0.293 | 0.583 | 0.641 | 0.196 | 0.639 | 0.558 | 0.129 | 0.083 | 0.587 | 0.027 | 0.213 | 0.232 | 0.269 |
| Time-limited legislative override window | 0.572 | 0.548 | 0.233 | 0.575 | 0.298 | 0.579 | 0.631 | 0.160 | 0.665 | 0.548 | 0.139 | 0.102 | 0.524 | 0.098 | 0.225 | 0.247 | 0.220 |
| Expanded 15-seat court | 0.572 | 0.550 | 0.239 | 0.575 | 0.296 | 0.578 | 0.631 | 0.163 | 0.654 | 0.551 | 0.130 | 0.102 | 0.519 | 0.098 | 0.229 | 0.246 | 0.228 |
| Independent recusal enforcement with substitutes | 0.572 | 0.551 | 0.237 | 0.575 | 0.297 | 0.578 | 0.632 | 0.165 | 0.659 | 0.550 | 0.133 | 0.103 | 0.536 | 0.099 | 0.227 | 0.239 | 0.236 |
| Judicial review with legislative supermajority override | 0.572 | 0.551 | 0.237 | 0.575 | 0.297 | 0.579 | 0.633 | 0.163 | 0.662 | 0.548 | 0.138 | 0.102 | 0.526 | 0.098 | 0.226 | 0.248 | 0.221 |
| Comparative 16-seat constitutional senates | 0.571 | 0.544 | 0.230 | 0.575 | 0.298 | 0.576 | 0.621 | 0.131 | 0.709 | 0.552 | 0.127 | 0.116 | 0.554 | 0.090 | 0.235 | 0.237 | 0.259 |
| Random panels with jurisdiction safeguards | 0.571 | 0.550 | 0.233 | 0.575 | 0.297 | 0.606 | 0.622 | 0.140 | 0.694 | 0.550 | 0.137 | 0.117 | 0.566 | 0.090 | 0.235 | 0.238 | 0.261 |
| Pre-enactment constitutional council | 0.568 | 0.554 | 0.239 | 0.575 | 0.295 | 0.622 | 0.633 | 0.159 | 0.675 | 0.555 | 0.137 | 0.101 | 0.586 | 0.098 | 0.227 | 0.246 | 0.294 |
| Constitutional council with concrete-review backstop | 0.568 | 0.549 | 0.231 | 0.575 | 0.295 | 0.622 | 0.630 | 0.150 | 0.685 | 0.557 | 0.133 | 0.100 | 0.589 | 0.098 | 0.225 | 0.243 | 0.306 |
| Stylized current U.S.-like supreme court | 0.567 | 0.548 | 0.236 | 0.575 | 0.305 | 0.569 | 0.640 | 0.180 | 0.627 | 0.532 | 0.145 | 0.166 | 0.369 | 0.283 | 0.295 | 0.274 | 0.152 |
| Supreme court with cross-checking constitutional court | 0.562 | 0.549 | 0.234 | 0.575 | 0.277 | 0.596 | 0.606 | 0.097 | 0.711 | 0.557 | 0.129 | 0.116 | 0.523 | 0.090 | 0.235 | 0.234 | 0.297 |
| Dual supreme courts with disagreement filter | 0.545 | 0.550 | 0.236 | 0.575 | 0.299 | 0.576 | 0.628 | 0.161 | 0.622 | 0.542 | 0.139 | 0.119 | 0.527 | 0.091 | 0.239 | 0.245 | 0.333 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.374 | 0.136 | 0.324 | 0.342 | 0.640 | 0.198 | 0.274 | 0.181 |
| No emergency relief without merits review | 0.374 | 0.195 | 0.471 | 0.460 | 0.947 | 0.279 | 0.362 | 0.240 |
| Constitutional remand before invalidation | 0.374 | 0.144 | 0.363 | 0.351 | 0.644 | 0.213 | 0.260 | 0.177 |
| 18-year staggered terms + regular appointments | 0.374 | 0.164 | 0.409 | 0.402 | 0.747 | 0.235 | 0.326 | 0.220 |
| Jurisdiction stripping constrained by rights carveouts | 0.374 | 0.163 | 0.408 | 0.394 | 0.730 | 0.221 | 0.348 | 0.197 |
| Constitutional remand with override window | 0.374 | 0.136 | 0.337 | 0.331 | 0.640 | 0.179 | 0.291 | 0.159 |
| Public-interest litigation filter | 0.374 | 0.170 | 0.429 | 0.423 | 0.760 | 0.243 | 0.339 | 0.214 |
| Nonpartisan commission appointments | 0.374 | 0.163 | 0.400 | 0.412 | 0.745 | 0.236 | 0.330 | 0.220 |
| Mandatory written emergency reasoning | 0.374 | 0.155 | 0.377 | 0.408 | 0.722 | 0.242 | 0.303 | 0.205 |
| Retention-election accountability court | 0.374 | 0.161 | 0.399 | 0.384 | 0.729 | 0.221 | 0.307 | 0.201 |
| Peer recusal + reasoned emergency docket | 0.374 | 0.161 | 0.398 | 0.397 | 0.739 | 0.260 | 0.320 | 0.225 |
| Three-judge panels with en banc correction | 0.374 | 0.161 | 0.402 | 0.403 | 0.726 | 0.236 | 0.302 | 0.211 |
| Automatic merits follow-up for emergency relief | 0.374 | 0.198 | 0.472 | 0.487 | 0.960 | 0.328 | 0.450 | 0.263 |
| Randomized merits panels with en banc correction | 0.374 | 0.160 | 0.403 | 0.420 | 0.725 | 0.194 | 0.327 | 0.205 |
| Emergency integrity package | 0.374 | 0.196 | 0.473 | 0.445 | 0.943 | 0.307 | 0.406 | 0.252 |
| Time-limited legislative override window | 0.374 | 0.160 | 0.396 | 0.407 | 0.744 | 0.234 | 0.279 | 0.217 |
| Expanded 15-seat court | 0.374 | 0.163 | 0.406 | 0.406 | 0.745 | 0.239 | 0.336 | 0.203 |
| Independent recusal enforcement with substitutes | 0.374 | 0.165 | 0.408 | 0.420 | 0.742 | 0.223 | 0.347 | 0.237 |
| Judicial review with legislative supermajority override | 0.374 | 0.163 | 0.402 | 0.392 | 0.743 | 0.238 | 0.351 | 0.200 |
| Comparative 16-seat constitutional senates | 0.374 | 0.131 | 0.321 | 0.314 | 0.621 | 0.133 | 0.227 | 0.137 |
| Random panels with jurisdiction safeguards | 0.374 | 0.140 | 0.339 | 0.371 | 0.652 | 0.212 | 0.298 | 0.197 |
| Pre-enactment constitutional council | 0.374 | 0.159 | 0.402 | 0.371 | 0.723 | 0.212 | 0.272 | 0.182 |
| Constitutional council with concrete-review backstop | 0.374 | 0.150 | 0.377 | 0.342 | 0.692 | 0.180 | 0.199 | 0.168 |
| Stylized current U.S.-like supreme court | 0.374 | 0.180 | 0.411 | 0.438 | 0.964 | 0.329 | 0.384 | 0.214 |
| Supreme court with cross-checking constitutional court | 0.374 | 0.097 | 0.237 | 0.284 | 0.415 | 0.161 | 0.186 | 0.134 |
| Dual supreme courts with disagreement filter | 0.374 | 0.161 | 0.393 | 0.403 | 0.747 | 0.210 | 0.323 | 0.226 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | No emergency relief without merits review (0.609) | Emergency integrity package (0.649) | No emergency relief without merits review (0.011) | Time-limited legislative override window (0.015) |
| Partisan Appointment Pressure | No emergency relief without merits review (0.609) | No emergency relief without merits review (0.649) | No emergency relief without merits review (0.011) | Dual supreme courts with disagreement filter (0.018) |
| Rights-Risk Legislation | Constitutional remand before invalidation (0.550) | No emergency relief without merits review (0.610) | No emergency relief without merits review (0.018) | Dual supreme courts with disagreement filter (0.020) |
| Shadow-Docket Stress | 60 percent invalidation threshold (0.550) | Stylized current U.S.-like supreme court (0.665) | No emergency relief without merits review (0.037) | Jurisdiction stripping constrained by rights carveouts (0.022) |
| High Democratic Mandate | No emergency relief without merits review (0.629) | Nonpartisan commission appointments (0.648) | No emergency relief without merits review (0.007) | Dual supreme courts with disagreement filter (0.009) |
| Constitutional Conflict | 60 percent invalidation threshold (0.520) | Stylized current U.S.-like supreme court (0.645) | No emergency relief without merits review (0.038) | Time-limited legislative override window (0.034) |
| Imported Legislative Output | No emergency relief without merits review (0.616) | Emergency integrity package (0.654) | No emergency relief without merits review (0.009) | Jurisdiction stripping constrained by rights carveouts (0.014) |
