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

- Top directional-score cluster within 0.010 of the maximum: No emergency relief without merits review (0.581); Jurisdiction stripping constrained by rights carveouts (0.578); 18-year staggered terms + regular appointments (0.578); 60 percent invalidation threshold (0.577); Automatic merits follow-up for emergency relief (0.575); Nonpartisan commission appointments (0.574); Mandatory written emergency reasoning (0.574); Peer recusal + reasoned emergency docket (0.573); Retention-election accountability court (0.573); Three-judge panels with en banc correction (0.573); Emergency integrity package (0.573); Time-limited legislative override window (0.571); Randomized merits panels with en banc correction (0.571); Judicial review with legislative supermajority override (0.571). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: No emergency relief without merits review at 0.581.
- Highest rights protection: Public-interest litigation filter at 0.662.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.021.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.246.
- Lowest partisan alignment: Judicial review with legislative supermajority override at 0.024.
- Highest public confidence index: Constitutional council with concrete-review backstop at 0.664.
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
| No emergency relief without merits review | 0.581 | 0.694 | 0.587 | 0.575 | 0.288 | 0.579 | 0.654 | 0.147 | 0.771 | 0.525 | 0.141 | 0.093 | 0.647 | 0.021 | 0.250 | 0.228 | 0.272 |
| Jurisdiction stripping constrained by rights carveouts | 0.578 | 0.689 | 0.581 | 0.575 | 0.292 | 0.605 | 0.651 | 0.142 | 0.755 | 0.516 | 0.153 | 0.109 | 0.597 | 0.110 | 0.264 | 0.236 | 0.251 |
| 18-year staggered terms + regular appointments | 0.578 | 0.677 | 0.571 | 0.575 | 0.292 | 0.574 | 0.649 | 0.143 | 0.750 | 0.516 | 0.143 | 0.107 | 0.561 | 0.108 | 0.260 | 0.248 | 0.224 |
| 60 percent invalidation threshold | 0.577 | 0.674 | 0.564 | 0.575 | 0.295 | 0.572 | 0.636 | 0.111 | 0.775 | 0.513 | 0.149 | 0.119 | 0.545 | 0.097 | 0.270 | 0.249 | 0.220 |
| Automatic merits follow-up for emergency relief | 0.575 | 0.679 | 0.571 | 0.575 | 0.289 | 0.579 | 0.659 | 0.170 | 0.739 | 0.522 | 0.144 | 0.107 | 0.612 | 0.030 | 0.246 | 0.243 | 0.288 |
| Nonpartisan commission appointments | 0.574 | 0.692 | 0.586 | 0.575 | 0.292 | 0.575 | 0.653 | 0.148 | 0.748 | 0.513 | 0.151 | 0.109 | 0.585 | 0.109 | 0.264 | 0.242 | 0.252 |
| Mandatory written emergency reasoning | 0.574 | 0.675 | 0.568 | 0.575 | 0.293 | 0.574 | 0.647 | 0.140 | 0.760 | 0.516 | 0.146 | 0.116 | 0.567 | 0.068 | 0.264 | 0.248 | 0.267 |
| Peer recusal + reasoned emergency docket | 0.573 | 0.674 | 0.562 | 0.575 | 0.293 | 0.574 | 0.648 | 0.140 | 0.752 | 0.515 | 0.147 | 0.108 | 0.566 | 0.108 | 0.260 | 0.247 | 0.256 |
| Retention-election accountability court | 0.573 | 0.691 | 0.580 | 0.575 | 0.292 | 0.575 | 0.640 | 0.131 | 0.758 | 0.515 | 0.147 | 0.109 | 0.586 | 0.110 | 0.265 | 0.239 | 0.252 |
| Three-judge panels with en banc correction | 0.573 | 0.689 | 0.575 | 0.575 | 0.292 | 0.574 | 0.648 | 0.138 | 0.764 | 0.514 | 0.146 | 0.109 | 0.631 | 0.110 | 0.262 | 0.237 | 0.267 |
| Emergency integrity package | 0.573 | 0.694 | 0.587 | 0.575 | 0.288 | 0.579 | 0.653 | 0.145 | 0.766 | 0.524 | 0.143 | 0.110 | 0.652 | 0.030 | 0.253 | 0.232 | 0.317 |
| Time-limited legislative override window | 0.571 | 0.692 | 0.585 | 0.575 | 0.293 | 0.575 | 0.654 | 0.144 | 0.753 | 0.510 | 0.157 | 0.109 | 0.588 | 0.110 | 0.264 | 0.248 | 0.260 |
| Randomized merits panels with en banc correction | 0.571 | 0.692 | 0.585 | 0.575 | 0.292 | 0.575 | 0.650 | 0.140 | 0.762 | 0.515 | 0.146 | 0.110 | 0.636 | 0.111 | 0.267 | 0.238 | 0.277 |
| Judicial review with legislative supermajority override | 0.571 | 0.684 | 0.576 | 0.575 | 0.294 | 0.575 | 0.652 | 0.140 | 0.753 | 0.511 | 0.159 | 0.110 | 0.586 | 0.110 | 0.266 | 0.247 | 0.259 |
| Expanded 15-seat court | 0.571 | 0.672 | 0.563 | 0.575 | 0.293 | 0.574 | 0.649 | 0.142 | 0.738 | 0.516 | 0.144 | 0.107 | 0.574 | 0.107 | 0.261 | 0.247 | 0.262 |
| Independent recusal enforcement with substitutes | 0.571 | 0.691 | 0.581 | 0.575 | 0.292 | 0.575 | 0.652 | 0.146 | 0.751 | 0.513 | 0.150 | 0.110 | 0.601 | 0.110 | 0.267 | 0.242 | 0.277 |
| Public-interest litigation filter | 0.570 | 0.722 | 0.619 | 0.575 | 0.292 | 0.576 | 0.662 | 0.158 | 0.757 | 0.508 | 0.156 | 0.115 | 0.593 | 0.116 | 0.280 | 0.240 | 0.291 |
| Constitutional remand before invalidation | 0.570 | 0.721 | 0.614 | 0.575 | 0.259 | 0.593 | 0.650 | 0.129 | 0.794 | 0.523 | 0.154 | 0.112 | 0.627 | 0.114 | 0.273 | 0.238 | 0.360 |
| Random panels with jurisdiction safeguards | 0.569 | 0.696 | 0.588 | 0.575 | 0.293 | 0.603 | 0.643 | 0.124 | 0.777 | 0.512 | 0.156 | 0.123 | 0.644 | 0.099 | 0.277 | 0.236 | 0.306 |
| Pre-enactment constitutional council | 0.568 | 0.692 | 0.587 | 0.575 | 0.291 | 0.617 | 0.649 | 0.130 | 0.770 | 0.519 | 0.155 | 0.108 | 0.657 | 0.109 | 0.264 | 0.244 | 0.333 |
| Constitutional remand with override window | 0.567 | 0.717 | 0.610 | 0.575 | 0.258 | 0.593 | 0.649 | 0.127 | 0.802 | 0.524 | 0.153 | 0.121 | 0.633 | 0.071 | 0.281 | 0.239 | 0.396 |
| Constitutional council with concrete-review backstop | 0.566 | 0.689 | 0.586 | 0.575 | 0.290 | 0.617 | 0.642 | 0.113 | 0.780 | 0.523 | 0.146 | 0.108 | 0.664 | 0.109 | 0.262 | 0.240 | 0.348 |
| Comparative 16-seat constitutional senates | 0.566 | 0.673 | 0.564 | 0.575 | 0.294 | 0.572 | 0.630 | 0.097 | 0.788 | 0.515 | 0.145 | 0.119 | 0.623 | 0.097 | 0.271 | 0.240 | 0.299 |
| Stylized current U.S.-like supreme court | 0.560 | 0.676 | 0.570 | 0.575 | 0.303 | 0.562 | 0.652 | 0.147 | 0.702 | 0.489 | 0.165 | 0.175 | 0.392 | 0.325 | 0.346 | 0.279 | 0.179 |
| Supreme court with cross-checking constitutional court | 0.554 | 0.692 | 0.584 | 0.575 | 0.274 | 0.593 | 0.627 | 0.090 | 0.779 | 0.515 | 0.154 | 0.121 | 0.587 | 0.098 | 0.275 | 0.242 | 0.349 |
| Dual supreme courts with disagreement filter | 0.542 | 0.690 | 0.582 | 0.575 | 0.295 | 0.572 | 0.652 | 0.146 | 0.716 | 0.503 | 0.159 | 0.122 | 0.591 | 0.100 | 0.277 | 0.249 | 0.389 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.373 | 0.147 | 0.392 | 0.222 | 0.604 | 0.159 | 0.136 | 0.113 |
| Jurisdiction stripping constrained by rights carveouts | 0.373 | 0.142 | 0.387 | 0.235 | 0.551 | 0.163 | 0.132 | 0.134 |
| 18-year staggered terms + regular appointments | 0.373 | 0.143 | 0.389 | 0.228 | 0.552 | 0.145 | 0.152 | 0.136 |
| 60 percent invalidation threshold | 0.373 | 0.111 | 0.304 | 0.179 | 0.435 | 0.095 | 0.095 | 0.101 |
| Automatic merits follow-up for emergency relief | 0.373 | 0.170 | 0.445 | 0.262 | 0.704 | 0.212 | 0.204 | 0.139 |
| Nonpartisan commission appointments | 0.373 | 0.148 | 0.404 | 0.256 | 0.570 | 0.172 | 0.130 | 0.127 |
| Mandatory written emergency reasoning | 0.373 | 0.140 | 0.374 | 0.230 | 0.548 | 0.163 | 0.175 | 0.139 |
| Peer recusal + reasoned emergency docket | 0.373 | 0.140 | 0.379 | 0.211 | 0.547 | 0.138 | 0.133 | 0.142 |
| Retention-election accountability court | 0.373 | 0.131 | 0.365 | 0.189 | 0.501 | 0.135 | 0.122 | 0.107 |
| Three-judge panels with en banc correction | 0.373 | 0.138 | 0.373 | 0.216 | 0.535 | 0.178 | 0.146 | 0.124 |
| Emergency integrity package | 0.373 | 0.145 | 0.376 | 0.203 | 0.608 | 0.163 | 0.154 | 0.123 |
| Time-limited legislative override window | 0.373 | 0.144 | 0.392 | 0.221 | 0.549 | 0.166 | 0.146 | 0.138 |
| Randomized merits panels with en banc correction | 0.373 | 0.140 | 0.381 | 0.231 | 0.534 | 0.150 | 0.149 | 0.118 |
| Judicial review with legislative supermajority override | 0.373 | 0.140 | 0.375 | 0.215 | 0.555 | 0.173 | 0.142 | 0.138 |
| Expanded 15-seat court | 0.373 | 0.142 | 0.388 | 0.212 | 0.544 | 0.153 | 0.152 | 0.133 |
| Independent recusal enforcement with substitutes | 0.373 | 0.146 | 0.392 | 0.239 | 0.561 | 0.173 | 0.136 | 0.140 |
| Public-interest litigation filter | 0.373 | 0.158 | 0.439 | 0.274 | 0.569 | 0.190 | 0.158 | 0.148 |
| Constitutional remand before invalidation | 0.373 | 0.129 | 0.351 | 0.217 | 0.474 | 0.141 | 0.112 | 0.112 |
| Random panels with jurisdiction safeguards | 0.373 | 0.124 | 0.339 | 0.212 | 0.456 | 0.138 | 0.121 | 0.126 |
| Pre-enactment constitutional council | 0.373 | 0.130 | 0.356 | 0.199 | 0.512 | 0.129 | 0.097 | 0.103 |
| Constitutional remand with override window | 0.373 | 0.127 | 0.350 | 0.200 | 0.480 | 0.127 | 0.115 | 0.110 |
| Constitutional council with concrete-review backstop | 0.373 | 0.113 | 0.314 | 0.161 | 0.436 | 0.086 | 0.081 | 0.092 |
| Comparative 16-seat constitutional senates | 0.373 | 0.097 | 0.271 | 0.133 | 0.370 | 0.080 | 0.069 | 0.076 |
| Stylized current U.S.-like supreme court | 0.373 | 0.147 | 0.379 | 0.206 | 0.692 | 0.198 | 0.153 | 0.120 |
| Supreme court with cross-checking constitutional court | 0.373 | 0.090 | 0.253 | 0.139 | 0.308 | 0.119 | 0.093 | 0.085 |
| Dual supreme courts with disagreement filter | 0.373 | 0.146 | 0.402 | 0.236 | 0.551 | 0.171 | 0.124 | 0.139 |

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
