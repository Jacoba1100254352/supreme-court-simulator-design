# Constitutional Review Campaign v2

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 22
- experiment cases: 20

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
| Appointment Timing Manipulation | 1.000 | adversarial/imported blend | Political actors time vacancies under high capture and public pressure. |
| Emergency Application Flood | 1.000 | emergency-flood synthetic legislature | Executives and litigants route controversial policies through urgent stay requests. |
| Override Evasion Loop | 1.000 | override-evasion synthetic legislature | Legislatures repeatedly revise invalidated laws to test rights carveouts and override thresholds. |
| Recusal Pressure Campaign | 0.850 | recusal-pressure synthetic legislature | High-salience litigants try to force or avoid recusals around ideologically charged cases. |
| Court Expansion Retaliation | 0.850 | expansion-retaliation synthetic legislature | A polarized political system reacts to judicial conflict with expansion threats and capture pressure. |

## Headline Findings

- Top directional-score cluster within 0.010 of the maximum: No emergency relief without merits review (0.579); 60 percent invalidation threshold (0.577); 18-year staggered terms + regular appointments (0.576); Jurisdiction stripping constrained by rights carveouts (0.573); Nonpartisan commission appointments (0.573); Mandatory written emergency reasoning (0.571); Peer recusal + reasoned emergency docket (0.571); Automatic merits follow-up for emergency relief (0.571); Retention-election accountability court (0.571); Three-judge panels with en banc correction (0.570); Time-limited legislative override window (0.569); Judicial review with legislative supermajority override (0.569); Expanded 15-seat court (0.569); Independent recusal enforcement with substitutes (0.569); Randomized merits panels with en banc correction (0.569). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: No emergency relief without merits review at 0.579.
- Highest rights protection: Public-interest litigation filter at 0.658.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.005.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.230.
- Lowest partisan alignment: Jurisdiction stripping constrained by rights carveouts at 0.028.
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
| No emergency relief without merits review | 0.579 | 0.698 | 0.587 | 0.589 | 0.651 | 0.161 | 0.764 | 0.507 | 0.178 | 0.068 | 0.661 | 0.005 | 0.233 | 0.200 | 0.273 |
| 60 percent invalidation threshold | 0.577 | 0.680 | 0.570 | 0.589 | 0.630 | 0.116 | 0.781 | 0.498 | 0.184 | 0.095 | 0.557 | 0.077 | 0.254 | 0.221 | 0.222 |
| 18-year staggered terms + regular appointments | 0.576 | 0.676 | 0.568 | 0.589 | 0.643 | 0.150 | 0.747 | 0.500 | 0.182 | 0.082 | 0.573 | 0.086 | 0.242 | 0.217 | 0.224 |
| Jurisdiction stripping constrained by rights carveouts | 0.573 | 0.694 | 0.585 | 0.589 | 0.646 | 0.153 | 0.750 | 0.495 | 0.193 | 0.084 | 0.610 | 0.089 | 0.247 | 0.210 | 0.253 |
| Nonpartisan commission appointments | 0.573 | 0.695 | 0.585 | 0.589 | 0.647 | 0.154 | 0.750 | 0.497 | 0.185 | 0.085 | 0.598 | 0.089 | 0.247 | 0.209 | 0.253 |
| Mandatory written emergency reasoning | 0.571 | 0.681 | 0.570 | 0.589 | 0.640 | 0.143 | 0.764 | 0.499 | 0.183 | 0.093 | 0.578 | 0.050 | 0.250 | 0.222 | 0.269 |
| Peer recusal + reasoned emergency docket | 0.571 | 0.681 | 0.569 | 0.589 | 0.644 | 0.150 | 0.749 | 0.499 | 0.184 | 0.083 | 0.580 | 0.088 | 0.244 | 0.219 | 0.258 |
| Automatic merits follow-up for emergency relief | 0.571 | 0.680 | 0.569 | 0.589 | 0.654 | 0.179 | 0.731 | 0.505 | 0.182 | 0.082 | 0.623 | 0.011 | 0.230 | 0.215 | 0.288 |
| Retention-election accountability court | 0.571 | 0.697 | 0.585 | 0.589 | 0.635 | 0.143 | 0.755 | 0.497 | 0.188 | 0.084 | 0.599 | 0.089 | 0.249 | 0.209 | 0.254 |
| Three-judge panels with en banc correction | 0.570 | 0.699 | 0.589 | 0.589 | 0.645 | 0.149 | 0.761 | 0.497 | 0.185 | 0.086 | 0.645 | 0.090 | 0.248 | 0.209 | 0.270 |
| Time-limited legislative override window | 0.569 | 0.693 | 0.581 | 0.589 | 0.648 | 0.152 | 0.751 | 0.494 | 0.194 | 0.084 | 0.601 | 0.089 | 0.247 | 0.218 | 0.261 |
| Judicial review with legislative supermajority override | 0.569 | 0.694 | 0.581 | 0.589 | 0.649 | 0.153 | 0.751 | 0.494 | 0.194 | 0.085 | 0.602 | 0.090 | 0.249 | 0.219 | 0.262 |
| Expanded 15-seat court | 0.569 | 0.679 | 0.568 | 0.589 | 0.643 | 0.149 | 0.739 | 0.500 | 0.181 | 0.083 | 0.588 | 0.088 | 0.248 | 0.218 | 0.265 |
| Independent recusal enforcement with substitutes | 0.569 | 0.697 | 0.587 | 0.589 | 0.647 | 0.154 | 0.753 | 0.496 | 0.188 | 0.085 | 0.616 | 0.090 | 0.250 | 0.210 | 0.278 |
| Randomized merits panels with en banc correction | 0.569 | 0.697 | 0.586 | 0.589 | 0.645 | 0.149 | 0.759 | 0.497 | 0.184 | 0.085 | 0.647 | 0.089 | 0.247 | 0.209 | 0.278 |
| Public-interest litigation filter | 0.567 | 0.728 | 0.621 | 0.589 | 0.658 | 0.168 | 0.756 | 0.491 | 0.195 | 0.089 | 0.609 | 0.093 | 0.260 | 0.216 | 0.293 |
| Comparative 16-seat constitutional senates | 0.566 | 0.679 | 0.565 | 0.589 | 0.625 | 0.103 | 0.793 | 0.500 | 0.178 | 0.096 | 0.635 | 0.077 | 0.253 | 0.206 | 0.301 |
| Constitutional remand before invalidation | 0.566 | 0.721 | 0.611 | 0.589 | 0.643 | 0.136 | 0.797 | 0.500 | 0.191 | 0.087 | 0.640 | 0.092 | 0.256 | 0.213 | 0.361 |
| Pre-enactment constitutional council | 0.563 | 0.696 | 0.586 | 0.589 | 0.644 | 0.138 | 0.768 | 0.496 | 0.192 | 0.084 | 0.671 | 0.088 | 0.246 | 0.215 | 0.336 |
| Stylized current U.S.-like supreme court | 0.562 | 0.679 | 0.566 | 0.589 | 0.649 | 0.161 | 0.702 | 0.477 | 0.198 | 0.151 | 0.406 | 0.302 | 0.329 | 0.241 | 0.180 |
| Supreme court with cross-checking constitutional court | 0.550 | 0.693 | 0.583 | 0.589 | 0.619 | 0.091 | 0.784 | 0.494 | 0.192 | 0.096 | 0.600 | 0.079 | 0.257 | 0.214 | 0.350 |
| Dual supreme courts with disagreement filter | 0.537 | 0.696 | 0.586 | 0.589 | 0.648 | 0.158 | 0.705 | 0.486 | 0.199 | 0.098 | 0.607 | 0.079 | 0.260 | 0.223 | 0.391 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.398 | 0.161 | 0.400 | 0.235 | 0.602 | 0.184 | 0.170 | 0.131 |
| 60 percent invalidation threshold | 0.398 | 0.116 | 0.296 | 0.187 | 0.414 | 0.103 | 0.096 | 0.105 |
| 18-year staggered terms + regular appointments | 0.398 | 0.150 | 0.374 | 0.249 | 0.546 | 0.176 | 0.165 | 0.151 |
| Jurisdiction stripping constrained by rights carveouts | 0.398 | 0.153 | 0.388 | 0.249 | 0.530 | 0.163 | 0.157 | 0.143 |
| Nonpartisan commission appointments | 0.398 | 0.154 | 0.389 | 0.247 | 0.543 | 0.171 | 0.166 | 0.160 |
| Mandatory written emergency reasoning | 0.398 | 0.143 | 0.356 | 0.239 | 0.531 | 0.159 | 0.144 | 0.136 |
| Peer recusal + reasoned emergency docket | 0.398 | 0.150 | 0.378 | 0.241 | 0.546 | 0.159 | 0.166 | 0.142 |
| Automatic merits follow-up for emergency relief | 0.398 | 0.179 | 0.436 | 0.278 | 0.675 | 0.243 | 0.200 | 0.169 |
| Retention-election accountability court | 0.398 | 0.143 | 0.368 | 0.219 | 0.506 | 0.139 | 0.140 | 0.129 |
| Three-judge panels with en banc correction | 0.398 | 0.149 | 0.374 | 0.251 | 0.534 | 0.168 | 0.152 | 0.142 |
| Time-limited legislative override window | 0.398 | 0.152 | 0.385 | 0.241 | 0.542 | 0.158 | 0.175 | 0.143 |
| Judicial review with legislative supermajority override | 0.398 | 0.153 | 0.390 | 0.249 | 0.533 | 0.168 | 0.147 | 0.142 |
| Expanded 15-seat court | 0.398 | 0.149 | 0.375 | 0.250 | 0.532 | 0.159 | 0.155 | 0.141 |
| Independent recusal enforcement with substitutes | 0.398 | 0.154 | 0.388 | 0.252 | 0.548 | 0.176 | 0.175 | 0.137 |
| Randomized merits panels with en banc correction | 0.398 | 0.149 | 0.376 | 0.253 | 0.525 | 0.158 | 0.165 | 0.140 |
| Public-interest litigation filter | 0.398 | 0.168 | 0.438 | 0.262 | 0.558 | 0.188 | 0.167 | 0.156 |
| Comparative 16-seat constitutional senates | 0.398 | 0.103 | 0.268 | 0.156 | 0.376 | 0.072 | 0.081 | 0.076 |
| Constitutional remand before invalidation | 0.398 | 0.136 | 0.350 | 0.220 | 0.472 | 0.137 | 0.151 | 0.121 |
| Pre-enactment constitutional council | 0.398 | 0.138 | 0.357 | 0.214 | 0.494 | 0.125 | 0.144 | 0.117 |
| Stylized current U.S.-like supreme court | 0.398 | 0.161 | 0.395 | 0.244 | 0.665 | 0.208 | 0.175 | 0.133 |
| Supreme court with cross-checking constitutional court | 0.398 | 0.091 | 0.233 | 0.162 | 0.312 | 0.097 | 0.090 | 0.097 |
| Dual supreme courts with disagreement filter | 0.398 | 0.158 | 0.402 | 0.258 | 0.561 | 0.159 | 0.180 | 0.161 |

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
| Appointment Timing Manipulation | 18-year staggered terms + regular appointments (0.609) | Public-interest litigation filter (0.655) | No emergency relief without merits review (0.001) | Jurisdiction stripping constrained by rights carveouts (0.025) |
| Emergency Application Flood | No emergency relief without merits review (0.534) | Stylized current U.S.-like supreme court (0.685) | No emergency relief without merits review (0.020) | Judicial review with legislative supermajority override (0.047) |
| Override Evasion Loop | 60 percent invalidation threshold (0.549) | Public-interest litigation filter (0.653) | No emergency relief without merits review (0.007) | Time-limited legislative override window (0.036) |
| Recusal Pressure Campaign | No emergency relief without merits review (0.552) | Automatic merits follow-up for emergency relief (0.668) | No emergency relief without merits review (0.011) | Judicial review with legislative supermajority override (0.054) |
| Court Expansion Retaliation | 60 percent invalidation threshold (0.536) | Automatic merits follow-up for emergency relief (0.670) | No emergency relief without merits review (0.013) | Jurisdiction stripping constrained by rights carveouts (0.056) |
