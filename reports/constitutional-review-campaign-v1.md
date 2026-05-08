# Constitutional Review Campaign v1

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 26
- experiment cases: 15

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
| Low Appointment Capture | 0.750 | neutral synthetic legislature | Appointment incentives are less partisan and the justice pool is less polarized. |
| Extreme Appointment Capture | 1.000 | neutral synthetic legislature | Appointment incentives are highly partisan and vacancies become ideological leverage points. |
| Low Emergency Pressure | 0.750 | neutral synthetic legislature | Few cases arrive through urgent stay requests or executive emergency disputes. |
| Extreme Emergency Pressure | 1.000 | extreme-emergency synthetic legislature | Emergency applications, executive-power disputes, and time-sensitive election conflicts are common. |
| Low Rights Risk | 0.750 | low-rights-risk synthetic legislature | Legislative output is legally careful, low-volatility, and rarely burdens protected interests. |
| Extreme Rights Risk | 1.000 | extreme-rights-risk synthetic legislature | Legislative output often creates concentrated rights burdens under contested public mandates. |
| Weak-Mandate Legislation | 1.000 | weak-mandate synthetic legislature | Many reviewed laws have low public legitimacy and high override pressure after invalidation. |
| Strong-Mandate Legislation | 0.750 | strong-mandate synthetic legislature | Popular legislation creates the hardest democratic-responsiveness pressure for review. |

## Headline Findings

- Top directional-score cluster within 0.010 of the maximum: No emergency relief without merits review (0.579); 18-year staggered terms + regular appointments (0.577); 60 percent invalidation threshold (0.576); Jurisdiction stripping constrained by rights carveouts (0.576); Automatic merits follow-up for emergency relief (0.574); Mandatory written emergency reasoning (0.572); Nonpartisan commission appointments (0.572); Peer recusal + reasoned emergency docket (0.572); Retention-election accountability court (0.571); Three-judge panels with en banc correction (0.571); Emergency integrity package (0.571); Time-limited legislative override window (0.570); Randomized merits panels with en banc correction (0.570); Judicial review with legislative supermajority override (0.570); Expanded 15-seat court (0.569); Independent recusal enforcement with substitutes (0.569); Constitutional remand before invalidation (0.569). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: No emergency relief without merits review at 0.579.
- Highest rights protection: Public-interest litigation filter at 0.661.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.021.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.243.
- Lowest partisan alignment: Jurisdiction stripping constrained by rights carveouts at 0.023.
- Highest public confidence index: Constitutional council with concrete-review backstop at 0.663.
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
| No emergency relief without merits review | 0.579 | 0.693 | 0.586 | 0.574 | 0.288 | 0.577 | 0.654 | 0.156 | 0.754 | 0.523 | 0.144 | 0.093 | 0.646 | 0.021 | 0.248 | 0.228 | 0.271 |
| 18-year staggered terms + regular appointments | 0.577 | 0.674 | 0.568 | 0.574 | 0.292 | 0.571 | 0.648 | 0.149 | 0.737 | 0.514 | 0.146 | 0.107 | 0.559 | 0.107 | 0.256 | 0.247 | 0.223 |
| 60 percent invalidation threshold | 0.576 | 0.672 | 0.563 | 0.574 | 0.294 | 0.569 | 0.634 | 0.116 | 0.766 | 0.512 | 0.149 | 0.120 | 0.543 | 0.096 | 0.266 | 0.248 | 0.219 |
| Jurisdiction stripping constrained by rights carveouts | 0.576 | 0.688 | 0.581 | 0.574 | 0.292 | 0.602 | 0.650 | 0.149 | 0.741 | 0.514 | 0.157 | 0.109 | 0.596 | 0.108 | 0.261 | 0.236 | 0.251 |
| Automatic merits follow-up for emergency relief | 0.574 | 0.675 | 0.568 | 0.574 | 0.289 | 0.576 | 0.658 | 0.175 | 0.728 | 0.521 | 0.144 | 0.105 | 0.609 | 0.029 | 0.243 | 0.241 | 0.286 |
| Mandatory written emergency reasoning | 0.572 | 0.673 | 0.567 | 0.574 | 0.293 | 0.572 | 0.645 | 0.144 | 0.749 | 0.514 | 0.148 | 0.116 | 0.565 | 0.068 | 0.262 | 0.247 | 0.266 |
| Nonpartisan commission appointments | 0.572 | 0.691 | 0.586 | 0.574 | 0.293 | 0.573 | 0.652 | 0.154 | 0.736 | 0.511 | 0.154 | 0.109 | 0.583 | 0.109 | 0.262 | 0.241 | 0.251 |
| Peer recusal + reasoned emergency docket | 0.572 | 0.673 | 0.564 | 0.574 | 0.293 | 0.571 | 0.647 | 0.147 | 0.738 | 0.514 | 0.148 | 0.108 | 0.565 | 0.107 | 0.257 | 0.247 | 0.255 |
| Retention-election accountability court | 0.571 | 0.692 | 0.583 | 0.574 | 0.292 | 0.573 | 0.639 | 0.139 | 0.743 | 0.512 | 0.152 | 0.109 | 0.586 | 0.109 | 0.263 | 0.239 | 0.252 |
| Three-judge panels with en banc correction | 0.571 | 0.690 | 0.581 | 0.574 | 0.292 | 0.572 | 0.649 | 0.147 | 0.748 | 0.512 | 0.150 | 0.110 | 0.632 | 0.110 | 0.261 | 0.238 | 0.267 |
| Emergency integrity package | 0.571 | 0.693 | 0.582 | 0.574 | 0.288 | 0.577 | 0.652 | 0.155 | 0.750 | 0.522 | 0.146 | 0.108 | 0.650 | 0.030 | 0.250 | 0.232 | 0.316 |
| Time-limited legislative override window | 0.570 | 0.689 | 0.581 | 0.574 | 0.293 | 0.573 | 0.652 | 0.149 | 0.740 | 0.510 | 0.158 | 0.109 | 0.587 | 0.108 | 0.261 | 0.247 | 0.259 |
| Randomized merits panels with en banc correction | 0.570 | 0.692 | 0.585 | 0.574 | 0.292 | 0.573 | 0.650 | 0.147 | 0.748 | 0.513 | 0.149 | 0.110 | 0.635 | 0.110 | 0.263 | 0.238 | 0.276 |
| Judicial review with legislative supermajority override | 0.570 | 0.687 | 0.582 | 0.574 | 0.294 | 0.572 | 0.652 | 0.148 | 0.739 | 0.510 | 0.159 | 0.110 | 0.586 | 0.109 | 0.262 | 0.247 | 0.259 |
| Expanded 15-seat court | 0.569 | 0.672 | 0.565 | 0.574 | 0.293 | 0.571 | 0.648 | 0.148 | 0.726 | 0.515 | 0.147 | 0.107 | 0.573 | 0.106 | 0.259 | 0.247 | 0.262 |
| Independent recusal enforcement with substitutes | 0.569 | 0.693 | 0.586 | 0.574 | 0.292 | 0.573 | 0.651 | 0.151 | 0.740 | 0.512 | 0.153 | 0.110 | 0.600 | 0.109 | 0.263 | 0.241 | 0.276 |
| Constitutional remand before invalidation | 0.569 | 0.718 | 0.611 | 0.574 | 0.258 | 0.591 | 0.648 | 0.134 | 0.785 | 0.522 | 0.155 | 0.112 | 0.625 | 0.112 | 0.271 | 0.238 | 0.358 |
| Public-interest litigation filter | 0.569 | 0.721 | 0.619 | 0.574 | 0.292 | 0.574 | 0.661 | 0.166 | 0.742 | 0.507 | 0.159 | 0.115 | 0.594 | 0.114 | 0.276 | 0.240 | 0.290 |
| Random panels with jurisdiction safeguards | 0.567 | 0.695 | 0.588 | 0.574 | 0.293 | 0.600 | 0.641 | 0.129 | 0.767 | 0.510 | 0.158 | 0.123 | 0.643 | 0.098 | 0.273 | 0.236 | 0.305 |
| Pre-enactment constitutional council | 0.566 | 0.692 | 0.587 | 0.574 | 0.291 | 0.615 | 0.647 | 0.135 | 0.757 | 0.517 | 0.157 | 0.108 | 0.658 | 0.109 | 0.262 | 0.243 | 0.333 |
| Constitutional remand with override window | 0.566 | 0.717 | 0.611 | 0.574 | 0.259 | 0.591 | 0.647 | 0.131 | 0.793 | 0.523 | 0.156 | 0.122 | 0.632 | 0.071 | 0.277 | 0.238 | 0.395 |
| Comparative 16-seat constitutional senates | 0.565 | 0.673 | 0.566 | 0.574 | 0.294 | 0.569 | 0.630 | 0.103 | 0.778 | 0.514 | 0.147 | 0.120 | 0.622 | 0.096 | 0.267 | 0.239 | 0.298 |
| Constitutional council with concrete-review backstop | 0.564 | 0.688 | 0.583 | 0.574 | 0.290 | 0.615 | 0.642 | 0.121 | 0.766 | 0.520 | 0.153 | 0.108 | 0.663 | 0.108 | 0.260 | 0.241 | 0.347 |
| Stylized current U.S.-like supreme court | 0.560 | 0.675 | 0.568 | 0.574 | 0.303 | 0.560 | 0.652 | 0.154 | 0.692 | 0.488 | 0.165 | 0.175 | 0.394 | 0.321 | 0.341 | 0.278 | 0.179 |
| Supreme court with cross-checking constitutional court | 0.553 | 0.691 | 0.585 | 0.574 | 0.274 | 0.590 | 0.625 | 0.093 | 0.771 | 0.514 | 0.155 | 0.122 | 0.585 | 0.097 | 0.272 | 0.241 | 0.348 |
| Dual supreme courts with disagreement filter | 0.540 | 0.688 | 0.580 | 0.574 | 0.295 | 0.570 | 0.651 | 0.153 | 0.702 | 0.502 | 0.161 | 0.123 | 0.589 | 0.099 | 0.274 | 0.249 | 0.387 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.379 | 0.156 | 0.389 | 0.235 | 0.604 | 0.190 | 0.153 | 0.135 |
| 18-year staggered terms + regular appointments | 0.379 | 0.149 | 0.383 | 0.246 | 0.548 | 0.172 | 0.171 | 0.151 |
| 60 percent invalidation threshold | 0.379 | 0.116 | 0.299 | 0.183 | 0.432 | 0.118 | 0.109 | 0.108 |
| Jurisdiction stripping constrained by rights carveouts | 0.379 | 0.149 | 0.384 | 0.254 | 0.544 | 0.175 | 0.156 | 0.146 |
| Automatic merits follow-up for emergency relief | 0.379 | 0.175 | 0.431 | 0.283 | 0.695 | 0.235 | 0.197 | 0.156 |
| Mandatory written emergency reasoning | 0.379 | 0.144 | 0.366 | 0.236 | 0.545 | 0.174 | 0.179 | 0.139 |
| Nonpartisan commission appointments | 0.379 | 0.154 | 0.396 | 0.263 | 0.566 | 0.177 | 0.161 | 0.143 |
| Peer recusal + reasoned emergency docket | 0.379 | 0.147 | 0.376 | 0.223 | 0.553 | 0.161 | 0.158 | 0.152 |
| Retention-election accountability court | 0.379 | 0.139 | 0.362 | 0.208 | 0.511 | 0.147 | 0.141 | 0.125 |
| Three-judge panels with en banc correction | 0.379 | 0.147 | 0.378 | 0.241 | 0.535 | 0.192 | 0.157 | 0.144 |
| Emergency integrity package | 0.379 | 0.155 | 0.376 | 0.231 | 0.605 | 0.185 | 0.173 | 0.141 |
| Time-limited legislative override window | 0.379 | 0.149 | 0.384 | 0.243 | 0.548 | 0.183 | 0.152 | 0.146 |
| Randomized merits panels with en banc correction | 0.379 | 0.147 | 0.381 | 0.243 | 0.526 | 0.174 | 0.161 | 0.144 |
| Judicial review with legislative supermajority override | 0.379 | 0.148 | 0.380 | 0.235 | 0.549 | 0.173 | 0.158 | 0.150 |
| Expanded 15-seat court | 0.379 | 0.148 | 0.381 | 0.240 | 0.551 | 0.172 | 0.151 | 0.144 |
| Independent recusal enforcement with substitutes | 0.379 | 0.151 | 0.391 | 0.255 | 0.553 | 0.175 | 0.160 | 0.147 |
| Constitutional remand before invalidation | 0.379 | 0.134 | 0.346 | 0.214 | 0.471 | 0.158 | 0.143 | 0.119 |
| Public-interest litigation filter | 0.379 | 0.166 | 0.437 | 0.275 | 0.564 | 0.207 | 0.172 | 0.164 |
| Random panels with jurisdiction safeguards | 0.379 | 0.129 | 0.333 | 0.217 | 0.461 | 0.156 | 0.136 | 0.136 |
| Pre-enactment constitutional council | 0.379 | 0.135 | 0.348 | 0.209 | 0.501 | 0.140 | 0.125 | 0.120 |
| Constitutional remand with override window | 0.379 | 0.131 | 0.340 | 0.213 | 0.470 | 0.142 | 0.137 | 0.129 |
| Comparative 16-seat constitutional senates | 0.379 | 0.103 | 0.271 | 0.152 | 0.375 | 0.091 | 0.087 | 0.088 |
| Constitutional council with concrete-review backstop | 0.379 | 0.121 | 0.316 | 0.170 | 0.441 | 0.103 | 0.099 | 0.105 |
| Stylized current U.S.-like supreme court | 0.379 | 0.154 | 0.372 | 0.235 | 0.690 | 0.215 | 0.167 | 0.132 |
| Supreme court with cross-checking constitutional court | 0.379 | 0.093 | 0.248 | 0.148 | 0.311 | 0.111 | 0.113 | 0.094 |
| Dual supreme courts with disagreement filter | 0.379 | 0.153 | 0.395 | 0.260 | 0.558 | 0.180 | 0.151 | 0.154 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | No emergency relief without merits review (0.607) | Public-interest litigation filter (0.664) | No emergency relief without merits review (0.011) | Dual supreme courts with disagreement filter (0.018) |
| Partisan Appointment Pressure | No emergency relief without merits review (0.604) | Public-interest litigation filter (0.666) | No emergency relief without merits review (0.012) | Dual supreme courts with disagreement filter (0.023) |
| Rights-Risk Legislation | 60 percent invalidation threshold (0.549) | Automatic merits follow-up for emergency relief (0.650) | No emergency relief without merits review (0.020) | Jurisdiction stripping constrained by rights carveouts (0.025) |
| Shadow-Docket Stress | No emergency relief without merits review (0.553) | Stylized current U.S.-like supreme court (0.677) | No emergency relief without merits review (0.043) | Time-limited legislative override window (0.027) |
| High Democratic Mandate | Jurisdiction stripping constrained by rights carveouts (0.624) | Public-interest litigation filter (0.650) | No emergency relief without merits review (0.008) | Dual supreme courts with disagreement filter (0.011) |
| Constitutional Conflict | 60 percent invalidation threshold (0.522) | Automatic merits follow-up for emergency relief (0.676) | No emergency relief without merits review (0.044) | Jurisdiction stripping constrained by rights carveouts (0.042) |
| Imported Legislative Output | No emergency relief without merits review (0.610) | Public-interest litigation filter (0.663) | No emergency relief without merits review (0.010) | Judicial review with legislative supermajority override (0.016) |
| Low Appointment Capture | No emergency relief without merits review (0.607) | Public-interest litigation filter (0.665) | No emergency relief without merits review (0.011) | Time-limited legislative override window (0.012) |
| Extreme Appointment Capture | Jurisdiction stripping constrained by rights carveouts (0.605) | Public-interest litigation filter (0.664) | No emergency relief without merits review (0.012) | Dual supreme courts with disagreement filter (0.027) |
| Low Emergency Pressure | Jurisdiction stripping constrained by rights carveouts (0.613) | Public-interest litigation filter (0.667) | No emergency relief without merits review (0.009) | Dual supreme courts with disagreement filter (0.017) |
| Extreme Emergency Pressure | No emergency relief without merits review (0.529) | Stylized current U.S.-like supreme court (0.680) | No emergency relief without merits review (0.057) | Jurisdiction stripping constrained by rights carveouts (0.036) |
| Low Rights Risk | Jurisdiction stripping constrained by rights carveouts (0.633) | Public-interest litigation filter (0.652) | No emergency relief without merits review (0.006) | Time-limited legislative override window (0.010) |
| Extreme Rights Risk | 60 percent invalidation threshold (0.511) | No emergency relief without merits review (0.656) | No emergency relief without merits review (0.030) | Jurisdiction stripping constrained by rights carveouts (0.034) |
| Weak-Mandate Legislation | 60 percent invalidation threshold (0.550) | Public-interest litigation filter (0.667) | No emergency relief without merits review (0.022) | Time-limited legislative override window (0.022) |
| Strong-Mandate Legislation | Jurisdiction stripping constrained by rights carveouts (0.629) | Dual supreme courts with disagreement filter (0.645) | No emergency relief without merits review (0.007) | Dual supreme courts with disagreement filter (0.012) |
