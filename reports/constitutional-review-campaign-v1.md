# Constitutional Review Campaign v1

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 22
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

- Top directional-score cluster within 0.010 of the maximum: No emergency relief without merits review (0.586); 18-year staggered terms + regular appointments (0.585); 60 percent invalidation threshold (0.584); Nonpartisan commission appointments (0.581); Jurisdiction stripping constrained by rights carveouts (0.581); Automatic merits follow-up for emergency relief (0.580); Mandatory written emergency reasoning (0.580); Peer recusal + reasoned emergency docket (0.580); Retention-election accountability court (0.579); Three-judge panels with en banc correction (0.578); Judicial review with legislative supermajority override (0.578); Time-limited legislative override window (0.578); Expanded 15-seat court (0.578); Independent recusal enforcement with substitutes (0.578); Randomized merits panels with en banc correction (0.577). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: No emergency relief without merits review at 0.586.
- Highest rights protection: Public-interest litigation filter at 0.656.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.004.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.213.
- Lowest partisan alignment: Jurisdiction stripping constrained by rights carveouts at 0.023.
- Highest public confidence index: Pre-enactment constitutional council at 0.671.
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
| No emergency relief without merits review | 0.586 | 0.684 | 0.575 | 0.574 | 0.648 | 0.145 | 0.773 | 0.518 | 0.159 | 0.059 | 0.658 | 0.004 | 0.215 | 0.186 | 0.265 |
| 18-year staggered terms + regular appointments | 0.585 | 0.662 | 0.556 | 0.574 | 0.642 | 0.138 | 0.755 | 0.511 | 0.165 | 0.071 | 0.577 | 0.078 | 0.223 | 0.203 | 0.217 |
| 60 percent invalidation threshold | 0.584 | 0.667 | 0.559 | 0.574 | 0.630 | 0.107 | 0.785 | 0.509 | 0.166 | 0.083 | 0.562 | 0.069 | 0.234 | 0.207 | 0.215 |
| Nonpartisan commission appointments | 0.581 | 0.682 | 0.572 | 0.574 | 0.646 | 0.142 | 0.759 | 0.509 | 0.166 | 0.074 | 0.601 | 0.080 | 0.228 | 0.195 | 0.246 |
| Jurisdiction stripping constrained by rights carveouts | 0.581 | 0.680 | 0.572 | 0.574 | 0.645 | 0.141 | 0.756 | 0.507 | 0.173 | 0.073 | 0.612 | 0.080 | 0.229 | 0.195 | 0.246 |
| Automatic merits follow-up for emergency relief | 0.580 | 0.666 | 0.557 | 0.574 | 0.651 | 0.162 | 0.746 | 0.516 | 0.163 | 0.073 | 0.622 | 0.009 | 0.213 | 0.201 | 0.281 |
| Mandatory written emergency reasoning | 0.580 | 0.667 | 0.557 | 0.574 | 0.640 | 0.132 | 0.770 | 0.511 | 0.164 | 0.081 | 0.582 | 0.043 | 0.231 | 0.207 | 0.262 |
| Peer recusal + reasoned emergency docket | 0.580 | 0.668 | 0.559 | 0.574 | 0.643 | 0.139 | 0.757 | 0.511 | 0.165 | 0.072 | 0.584 | 0.079 | 0.225 | 0.205 | 0.250 |
| Retention-election accountability court | 0.579 | 0.684 | 0.572 | 0.574 | 0.635 | 0.132 | 0.761 | 0.508 | 0.169 | 0.073 | 0.602 | 0.081 | 0.230 | 0.195 | 0.247 |
| Three-judge panels with en banc correction | 0.578 | 0.687 | 0.577 | 0.574 | 0.644 | 0.137 | 0.769 | 0.508 | 0.167 | 0.075 | 0.650 | 0.081 | 0.230 | 0.195 | 0.263 |
| Judicial review with legislative supermajority override | 0.578 | 0.680 | 0.568 | 0.574 | 0.648 | 0.141 | 0.759 | 0.506 | 0.175 | 0.074 | 0.604 | 0.081 | 0.230 | 0.204 | 0.254 |
| Time-limited legislative override window | 0.578 | 0.679 | 0.568 | 0.574 | 0.647 | 0.141 | 0.758 | 0.506 | 0.175 | 0.073 | 0.603 | 0.080 | 0.228 | 0.203 | 0.254 |
| Expanded 15-seat court | 0.578 | 0.667 | 0.558 | 0.574 | 0.642 | 0.138 | 0.748 | 0.511 | 0.162 | 0.073 | 0.591 | 0.079 | 0.229 | 0.204 | 0.258 |
| Independent recusal enforcement with substitutes | 0.578 | 0.684 | 0.575 | 0.574 | 0.646 | 0.142 | 0.760 | 0.508 | 0.170 | 0.074 | 0.617 | 0.081 | 0.231 | 0.196 | 0.271 |
| Randomized merits panels with en banc correction | 0.577 | 0.684 | 0.575 | 0.574 | 0.645 | 0.139 | 0.765 | 0.509 | 0.166 | 0.074 | 0.651 | 0.081 | 0.229 | 0.195 | 0.270 |
| Public-interest litigation filter | 0.575 | 0.715 | 0.608 | 0.574 | 0.656 | 0.155 | 0.763 | 0.503 | 0.177 | 0.077 | 0.612 | 0.084 | 0.241 | 0.201 | 0.285 |
| Comparative 16-seat constitutional senates | 0.574 | 0.665 | 0.553 | 0.574 | 0.625 | 0.096 | 0.795 | 0.512 | 0.159 | 0.083 | 0.639 | 0.069 | 0.234 | 0.192 | 0.293 |
| Constitutional remand before invalidation | 0.574 | 0.708 | 0.598 | 0.574 | 0.643 | 0.126 | 0.800 | 0.511 | 0.172 | 0.075 | 0.639 | 0.083 | 0.237 | 0.199 | 0.350 |
| Pre-enactment constitutional council | 0.572 | 0.683 | 0.573 | 0.574 | 0.643 | 0.128 | 0.773 | 0.508 | 0.173 | 0.073 | 0.671 | 0.080 | 0.227 | 0.200 | 0.325 |
| Stylized current U.S.-like supreme court | 0.571 | 0.665 | 0.554 | 0.574 | 0.646 | 0.146 | 0.712 | 0.490 | 0.178 | 0.134 | 0.422 | 0.279 | 0.305 | 0.226 | 0.175 |
| Supreme court with cross-checking constitutional court | 0.559 | 0.679 | 0.570 | 0.574 | 0.620 | 0.085 | 0.788 | 0.506 | 0.172 | 0.084 | 0.602 | 0.070 | 0.237 | 0.200 | 0.341 |
| Dual supreme courts with disagreement filter | 0.547 | 0.684 | 0.574 | 0.574 | 0.648 | 0.147 | 0.720 | 0.498 | 0.181 | 0.086 | 0.609 | 0.071 | 0.240 | 0.209 | 0.382 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.383 | 0.145 | 0.359 | 0.206 | 0.553 | 0.166 | 0.156 | 0.120 |
| 18-year staggered terms + regular appointments | 0.383 | 0.138 | 0.349 | 0.222 | 0.519 | 0.150 | 0.152 | 0.132 |
| 60 percent invalidation threshold | 0.383 | 0.107 | 0.278 | 0.168 | 0.388 | 0.090 | 0.089 | 0.090 |
| Nonpartisan commission appointments | 0.383 | 0.142 | 0.365 | 0.221 | 0.508 | 0.149 | 0.153 | 0.142 |
| Jurisdiction stripping constrained by rights carveouts | 0.383 | 0.141 | 0.361 | 0.225 | 0.506 | 0.146 | 0.145 | 0.127 |
| Automatic merits follow-up for emergency relief | 0.383 | 0.162 | 0.399 | 0.247 | 0.630 | 0.215 | 0.175 | 0.149 |
| Mandatory written emergency reasoning | 0.383 | 0.132 | 0.333 | 0.216 | 0.510 | 0.140 | 0.130 | 0.119 |
| Peer recusal + reasoned emergency docket | 0.383 | 0.139 | 0.352 | 0.217 | 0.518 | 0.133 | 0.155 | 0.126 |
| Retention-election accountability court | 0.383 | 0.132 | 0.341 | 0.194 | 0.478 | 0.126 | 0.129 | 0.115 |
| Three-judge panels with en banc correction | 0.383 | 0.137 | 0.347 | 0.231 | 0.508 | 0.145 | 0.139 | 0.130 |
| Judicial review with legislative supermajority override | 0.383 | 0.141 | 0.365 | 0.221 | 0.508 | 0.147 | 0.137 | 0.125 |
| Time-limited legislative override window | 0.383 | 0.141 | 0.362 | 0.216 | 0.514 | 0.136 | 0.172 | 0.129 |
| Expanded 15-seat court | 0.383 | 0.138 | 0.349 | 0.228 | 0.505 | 0.141 | 0.140 | 0.124 |
| Independent recusal enforcement with substitutes | 0.383 | 0.142 | 0.363 | 0.230 | 0.519 | 0.154 | 0.157 | 0.123 |
| Randomized merits panels with en banc correction | 0.383 | 0.139 | 0.354 | 0.231 | 0.502 | 0.138 | 0.147 | 0.124 |
| Public-interest litigation filter | 0.383 | 0.155 | 0.411 | 0.236 | 0.529 | 0.165 | 0.149 | 0.138 |
| Comparative 16-seat constitutional senates | 0.383 | 0.096 | 0.248 | 0.151 | 0.353 | 0.065 | 0.081 | 0.067 |
| Constitutional remand before invalidation | 0.383 | 0.126 | 0.326 | 0.200 | 0.447 | 0.117 | 0.143 | 0.109 |
| Pre-enactment constitutional council | 0.383 | 0.128 | 0.331 | 0.198 | 0.463 | 0.114 | 0.143 | 0.107 |
| Stylized current U.S.-like supreme court | 0.383 | 0.146 | 0.359 | 0.223 | 0.624 | 0.187 | 0.164 | 0.117 |
| Supreme court with cross-checking constitutional court | 0.383 | 0.085 | 0.221 | 0.150 | 0.296 | 0.088 | 0.085 | 0.088 |
| Dual supreme courts with disagreement filter | 0.383 | 0.147 | 0.381 | 0.238 | 0.534 | 0.137 | 0.170 | 0.143 |

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
| Low Appointment Capture | 18-year staggered terms + regular appointments (0.606) | Public-interest litigation filter (0.657) | No emergency relief without merits review (0.001) | Jurisdiction stripping constrained by rights carveouts (0.012) |
| Extreme Appointment Capture | No emergency relief without merits review (0.606) | Public-interest litigation filter (0.654) | No emergency relief without merits review (0.001) | Jurisdiction stripping constrained by rights carveouts (0.026) |
| Low Emergency Pressure | 18-year staggered terms + regular appointments (0.614) | Public-interest litigation filter (0.662) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.017) |
| Extreme Emergency Pressure | No emergency relief without merits review (0.553) | Automatic merits follow-up for emergency relief (0.677) | No emergency relief without merits review (0.012) | Dual supreme courts with disagreement filter (0.035) |
| Low Rights Risk | 18-year staggered terms + regular appointments (0.623) | Public-interest litigation filter (0.653) | No emergency relief without merits review (0.001) | Judicial review with legislative supermajority override (0.010) |
| Extreme Rights Risk | 60 percent invalidation threshold (0.530) | No emergency relief without merits review (0.645) | No emergency relief without merits review (0.005) | Time-limited legislative override window (0.034) |
| Weak-Mandate Legislation | 60 percent invalidation threshold (0.571) | Public-interest litigation filter (0.667) | No emergency relief without merits review (0.003) | Time-limited legislative override window (0.022) |
| Strong-Mandate Legislation | 18-year staggered terms + regular appointments (0.621) | Public-interest litigation filter (0.641) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.012) |
