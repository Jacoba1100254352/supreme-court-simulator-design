# Constitutional Review Campaign v0

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 22
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

- Top directional-score cluster within 0.010 of the maximum: No emergency relief without merits review (0.588); 18-year staggered terms + regular appointments (0.586); 60 percent invalidation threshold (0.585); Jurisdiction stripping constrained by rights carveouts (0.583); Nonpartisan commission appointments (0.583); Automatic merits follow-up for emergency relief (0.581); Retention-election accountability court (0.581); Peer recusal + reasoned emergency docket (0.581); Mandatory written emergency reasoning (0.581); Three-judge panels with en banc correction (0.580); Time-limited legislative override window (0.580); Judicial review with legislative supermajority override (0.579); Expanded 15-seat court (0.579); Independent recusal enforcement with substitutes (0.579); Randomized merits panels with en banc correction (0.578). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: No emergency relief without merits review at 0.588.
- Highest rights protection: Public-interest litigation filter at 0.657.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.004.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.216.
- Lowest partisan alignment: Time-limited legislative override window at 0.023.
- Highest public confidence index: Pre-enactment constitutional council at 0.672.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, claimant success, precedent durability, lower-court compliance, elite acceptance, and administrative feasibility.
- Empirical claims, synthetic findings, and speculative design recommendations should be read separately: source ranges only smoke-test plausibility, campaign outputs are synthetic, and design recommendations are conditional on the model assumptions.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Higher direct outputs such as `rightsClaimantSuccess`, `doctrinalDepth`, `remedialBreadth`, `precedentDurability`, `lowerCourtCompliance`, `eliteAcceptance`, and `publicConfidence` are usually better, but each should be read in domain context.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `emergencyLegitimacyRisk`, `emergencyDownstreamEffect`, `governmentNoncomplianceRate`, `reversalRate`, `constitutionalConflict`, `administrativeCost`, and `strategicPressure` are usually better.
- Petition, certiorari-admission, lower-court-split, strategic-plaintiff, repeat-player, emergency, emergency-downstream, replacement, recusal, concurrence, dissent, fragmentation, panel, en banc, council, cross-check, remand, public-interest, formal-response, practical-response, noncompliance, and override rates are diagnostic rather than automatically good or bad.

## Scenario Averages Across Cases

| Scenario | Directional | Admission | Cert admit | Lower split | Rights protection | Claimant success | Precedent durability | Lower-court compliance | Gov. noncomp. | Emerg. downstream | Public confidence | Shadow abuse | Emergency risk | Strategic | Admin cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.588 | 0.686 | 0.576 | 0.575 | 0.648 | 0.136 | 0.789 | 0.519 | 0.159 | 0.059 | 0.660 | 0.004 | 0.219 | 0.187 | 0.267 |
| 18-year staggered terms + regular appointments | 0.586 | 0.664 | 0.558 | 0.575 | 0.643 | 0.132 | 0.770 | 0.512 | 0.165 | 0.071 | 0.578 | 0.078 | 0.226 | 0.204 | 0.219 |
| 60 percent invalidation threshold | 0.585 | 0.669 | 0.562 | 0.575 | 0.632 | 0.103 | 0.795 | 0.509 | 0.166 | 0.083 | 0.564 | 0.070 | 0.238 | 0.209 | 0.216 |
| Jurisdiction stripping constrained by rights carveouts | 0.583 | 0.684 | 0.577 | 0.575 | 0.646 | 0.135 | 0.770 | 0.509 | 0.169 | 0.073 | 0.615 | 0.081 | 0.232 | 0.194 | 0.247 |
| Nonpartisan commission appointments | 0.583 | 0.685 | 0.576 | 0.575 | 0.646 | 0.135 | 0.774 | 0.510 | 0.166 | 0.073 | 0.602 | 0.081 | 0.231 | 0.196 | 0.247 |
| Automatic merits follow-up for emergency relief | 0.581 | 0.668 | 0.559 | 0.575 | 0.651 | 0.153 | 0.761 | 0.517 | 0.163 | 0.075 | 0.623 | 0.009 | 0.216 | 0.202 | 0.282 |
| Retention-election accountability court | 0.581 | 0.685 | 0.576 | 0.575 | 0.636 | 0.124 | 0.777 | 0.510 | 0.167 | 0.073 | 0.604 | 0.081 | 0.233 | 0.196 | 0.248 |
| Peer recusal + reasoned emergency docket | 0.581 | 0.670 | 0.561 | 0.575 | 0.643 | 0.131 | 0.770 | 0.511 | 0.164 | 0.072 | 0.585 | 0.080 | 0.229 | 0.205 | 0.252 |
| Mandatory written emergency reasoning | 0.581 | 0.669 | 0.558 | 0.575 | 0.640 | 0.126 | 0.784 | 0.511 | 0.167 | 0.080 | 0.584 | 0.043 | 0.235 | 0.208 | 0.263 |
| Three-judge panels with en banc correction | 0.580 | 0.690 | 0.584 | 0.575 | 0.645 | 0.131 | 0.783 | 0.509 | 0.165 | 0.074 | 0.651 | 0.083 | 0.235 | 0.195 | 0.265 |
| Time-limited legislative override window | 0.580 | 0.681 | 0.569 | 0.575 | 0.647 | 0.134 | 0.773 | 0.507 | 0.174 | 0.073 | 0.605 | 0.081 | 0.230 | 0.203 | 0.254 |
| Judicial review with legislative supermajority override | 0.579 | 0.687 | 0.576 | 0.575 | 0.649 | 0.134 | 0.776 | 0.506 | 0.176 | 0.074 | 0.606 | 0.083 | 0.236 | 0.204 | 0.257 |
| Expanded 15-seat court | 0.579 | 0.666 | 0.559 | 0.575 | 0.643 | 0.133 | 0.759 | 0.512 | 0.161 | 0.072 | 0.591 | 0.080 | 0.232 | 0.205 | 0.259 |
| Independent recusal enforcement with substitutes | 0.579 | 0.687 | 0.577 | 0.575 | 0.646 | 0.136 | 0.773 | 0.509 | 0.169 | 0.074 | 0.619 | 0.082 | 0.234 | 0.196 | 0.272 |
| Randomized merits panels with en banc correction | 0.578 | 0.685 | 0.578 | 0.575 | 0.644 | 0.130 | 0.778 | 0.509 | 0.168 | 0.074 | 0.652 | 0.082 | 0.233 | 0.196 | 0.272 |
| Public-interest litigation filter | 0.577 | 0.718 | 0.613 | 0.575 | 0.657 | 0.149 | 0.776 | 0.504 | 0.176 | 0.077 | 0.613 | 0.085 | 0.244 | 0.202 | 0.287 |
| Comparative 16-seat constitutional senates | 0.575 | 0.665 | 0.554 | 0.575 | 0.625 | 0.089 | 0.804 | 0.513 | 0.157 | 0.082 | 0.640 | 0.069 | 0.237 | 0.193 | 0.294 |
| Constitutional remand before invalidation | 0.575 | 0.710 | 0.601 | 0.575 | 0.643 | 0.120 | 0.811 | 0.512 | 0.172 | 0.075 | 0.640 | 0.084 | 0.240 | 0.199 | 0.351 |
| Pre-enactment constitutional council | 0.573 | 0.687 | 0.575 | 0.575 | 0.644 | 0.123 | 0.785 | 0.508 | 0.173 | 0.073 | 0.672 | 0.081 | 0.231 | 0.201 | 0.326 |
| Stylized current U.S.-like supreme court | 0.571 | 0.669 | 0.559 | 0.575 | 0.646 | 0.138 | 0.722 | 0.489 | 0.179 | 0.135 | 0.419 | 0.284 | 0.312 | 0.227 | 0.177 |
| Supreme court with cross-checking constitutional court | 0.559 | 0.681 | 0.571 | 0.575 | 0.621 | 0.082 | 0.795 | 0.507 | 0.171 | 0.083 | 0.603 | 0.071 | 0.241 | 0.201 | 0.342 |
| Dual supreme courts with disagreement filter | 0.547 | 0.689 | 0.583 | 0.575 | 0.649 | 0.141 | 0.731 | 0.498 | 0.184 | 0.085 | 0.611 | 0.072 | 0.245 | 0.211 | 0.385 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.378 | 0.136 | 0.361 | 0.187 | 0.547 | 0.140 | 0.138 | 0.109 |
| 18-year staggered terms + regular appointments | 0.378 | 0.132 | 0.354 | 0.197 | 0.516 | 0.144 | 0.121 | 0.116 |
| 60 percent invalidation threshold | 0.378 | 0.103 | 0.283 | 0.154 | 0.384 | 0.080 | 0.072 | 0.076 |
| Jurisdiction stripping constrained by rights carveouts | 0.378 | 0.135 | 0.366 | 0.216 | 0.505 | 0.135 | 0.119 | 0.108 |
| Nonpartisan commission appointments | 0.378 | 0.135 | 0.362 | 0.200 | 0.517 | 0.120 | 0.136 | 0.116 |
| Automatic merits follow-up for emergency relief | 0.378 | 0.153 | 0.397 | 0.219 | 0.627 | 0.196 | 0.140 | 0.136 |
| Retention-election accountability court | 0.378 | 0.124 | 0.337 | 0.179 | 0.485 | 0.102 | 0.108 | 0.100 |
| Peer recusal + reasoned emergency docket | 0.378 | 0.131 | 0.350 | 0.192 | 0.510 | 0.120 | 0.145 | 0.116 |
| Mandatory written emergency reasoning | 0.378 | 0.126 | 0.334 | 0.199 | 0.499 | 0.125 | 0.107 | 0.107 |
| Three-judge panels with en banc correction | 0.378 | 0.131 | 0.348 | 0.212 | 0.498 | 0.131 | 0.114 | 0.122 |
| Time-limited legislative override window | 0.378 | 0.134 | 0.362 | 0.191 | 0.513 | 0.115 | 0.155 | 0.119 |
| Judicial review with legislative supermajority override | 0.378 | 0.134 | 0.367 | 0.197 | 0.499 | 0.129 | 0.098 | 0.107 |
| Expanded 15-seat court | 0.378 | 0.133 | 0.355 | 0.210 | 0.488 | 0.138 | 0.138 | 0.115 |
| Independent recusal enforcement with substitutes | 0.378 | 0.136 | 0.363 | 0.206 | 0.527 | 0.150 | 0.126 | 0.118 |
| Randomized merits panels with en banc correction | 0.378 | 0.130 | 0.352 | 0.212 | 0.500 | 0.107 | 0.129 | 0.106 |
| Public-interest litigation filter | 0.378 | 0.149 | 0.413 | 0.227 | 0.531 | 0.155 | 0.120 | 0.118 |
| Comparative 16-seat constitutional senates | 0.378 | 0.089 | 0.244 | 0.129 | 0.347 | 0.048 | 0.066 | 0.056 |
| Constitutional remand before invalidation | 0.378 | 0.120 | 0.328 | 0.178 | 0.451 | 0.112 | 0.123 | 0.095 |
| Pre-enactment constitutional council | 0.378 | 0.123 | 0.333 | 0.183 | 0.458 | 0.097 | 0.126 | 0.103 |
| Stylized current U.S.-like supreme court | 0.378 | 0.138 | 0.360 | 0.211 | 0.607 | 0.157 | 0.158 | 0.106 |
| Supreme court with cross-checking constitutional court | 0.378 | 0.082 | 0.220 | 0.142 | 0.296 | 0.070 | 0.078 | 0.084 |
| Dual supreme courts with disagreement filter | 0.378 | 0.141 | 0.387 | 0.214 | 0.526 | 0.126 | 0.137 | 0.130 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | 18-year staggered terms + regular appointments (0.607) | Public-interest litigation filter (0.657) | No emergency relief without merits review (0.001) | Jurisdiction stripping constrained by rights carveouts (0.018) |
| Partisan Appointment Pressure | 18-year staggered terms + regular appointments (0.608) | Public-interest litigation filter (0.658) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.022) |
| Rights-Risk Legislation | 60 percent invalidation threshold (0.567) | Public-interest litigation filter (0.648) | No emergency relief without merits review (0.003) | Dual supreme courts with disagreement filter (0.025) |
| Shadow-Docket Stress | No emergency relief without merits review (0.568) | Automatic merits follow-up for emergency relief (0.666) | No emergency relief without merits review (0.007) | Time-limited legislative override window (0.027) |
| High Democratic Mandate | 18-year staggered terms + regular appointments (0.617) | Dual supreme courts with disagreement filter (0.643) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.011) |
| Constitutional Conflict | No emergency relief without merits review (0.548) | Automatic merits follow-up for emergency relief (0.674) | No emergency relief without merits review (0.012) | Jurisdiction stripping constrained by rights carveouts (0.042) |
| Imported Legislative Output | No emergency relief without merits review (0.610) | Public-interest litigation filter (0.660) | No emergency relief without merits review (0.001) | Time-limited legislative override window (0.016) |
