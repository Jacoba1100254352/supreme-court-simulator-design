# Constitutional Review Campaign v2

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 26
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

- Top directional-score cluster within 0.010 of the maximum: No emergency relief without merits review (0.567); 60 percent invalidation threshold (0.565); 18-year staggered terms + regular appointments (0.565); Jurisdiction stripping constrained by rights carveouts (0.564); Automatic merits follow-up for emergency relief (0.561); Nonpartisan commission appointments (0.561); Mandatory written emergency reasoning (0.561); Peer recusal + reasoned emergency docket (0.560); Retention-election accountability court (0.559); Emergency integrity package (0.559); Three-judge panels with en banc correction (0.559); Time-limited legislative override window (0.558); Constitutional remand before invalidation (0.558); Randomized merits panels with en banc correction (0.558); Judicial review with legislative supermajority override (0.558); Expanded 15-seat court (0.558); Independent recusal enforcement with substitutes (0.557). These close differences are not interpreted as rankings.
- Highest single directional score for table ordering only: No emergency relief without merits review at 0.567.
- Highest rights protection: Public-interest litigation filter at 0.662.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.026.
- Lowest emergency legitimacy risk: Automatic merits follow-up for emergency relief at 0.264.
- Lowest partisan alignment: Jurisdiction stripping constrained by rights carveouts at 0.029.
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
| No emergency relief without merits review | 0.567 | 0.708 | 0.600 | 0.589 | 0.312 | 0.565 | 0.658 | 0.175 | 0.736 | 0.504 | 0.168 | 0.106 | 0.649 | 0.026 | 0.269 | 0.246 | 0.279 |
| 60 percent invalidation threshold | 0.565 | 0.688 | 0.579 | 0.589 | 0.318 | 0.557 | 0.634 | 0.125 | 0.761 | 0.493 | 0.172 | 0.137 | 0.537 | 0.107 | 0.289 | 0.265 | 0.227 |
| 18-year staggered terms + regular appointments | 0.565 | 0.689 | 0.582 | 0.589 | 0.316 | 0.559 | 0.649 | 0.162 | 0.722 | 0.495 | 0.170 | 0.122 | 0.555 | 0.118 | 0.278 | 0.264 | 0.230 |
| Jurisdiction stripping constrained by rights carveouts | 0.564 | 0.702 | 0.594 | 0.589 | 0.316 | 0.590 | 0.651 | 0.161 | 0.729 | 0.495 | 0.183 | 0.124 | 0.593 | 0.120 | 0.283 | 0.254 | 0.258 |
| Automatic merits follow-up for emergency relief | 0.561 | 0.690 | 0.583 | 0.589 | 0.312 | 0.564 | 0.660 | 0.193 | 0.703 | 0.503 | 0.167 | 0.118 | 0.610 | 0.035 | 0.264 | 0.258 | 0.294 |
| Nonpartisan commission appointments | 0.561 | 0.705 | 0.599 | 0.589 | 0.316 | 0.560 | 0.652 | 0.165 | 0.725 | 0.493 | 0.176 | 0.125 | 0.580 | 0.121 | 0.284 | 0.258 | 0.259 |
| Mandatory written emergency reasoning | 0.561 | 0.688 | 0.581 | 0.589 | 0.316 | 0.559 | 0.645 | 0.155 | 0.739 | 0.496 | 0.171 | 0.133 | 0.560 | 0.078 | 0.285 | 0.264 | 0.274 |
| Peer recusal + reasoned emergency docket | 0.560 | 0.688 | 0.579 | 0.589 | 0.316 | 0.559 | 0.648 | 0.159 | 0.725 | 0.496 | 0.171 | 0.123 | 0.562 | 0.119 | 0.279 | 0.264 | 0.262 |
| Retention-election accountability court | 0.559 | 0.707 | 0.598 | 0.589 | 0.316 | 0.561 | 0.639 | 0.153 | 0.732 | 0.493 | 0.176 | 0.124 | 0.582 | 0.121 | 0.285 | 0.256 | 0.260 |
| Emergency integrity package | 0.559 | 0.707 | 0.598 | 0.589 | 0.312 | 0.565 | 0.656 | 0.172 | 0.734 | 0.504 | 0.169 | 0.121 | 0.654 | 0.036 | 0.271 | 0.249 | 0.325 |
| Three-judge panels with en banc correction | 0.559 | 0.705 | 0.596 | 0.589 | 0.316 | 0.560 | 0.650 | 0.159 | 0.737 | 0.493 | 0.174 | 0.126 | 0.627 | 0.122 | 0.283 | 0.255 | 0.275 |
| Time-limited legislative override window | 0.558 | 0.703 | 0.594 | 0.589 | 0.317 | 0.561 | 0.654 | 0.162 | 0.728 | 0.491 | 0.182 | 0.124 | 0.584 | 0.120 | 0.283 | 0.265 | 0.266 |
| Constitutional remand before invalidation | 0.558 | 0.732 | 0.625 | 0.589 | 0.282 | 0.580 | 0.648 | 0.145 | 0.779 | 0.504 | 0.178 | 0.128 | 0.625 | 0.124 | 0.292 | 0.255 | 0.371 |
| Randomized merits panels with en banc correction | 0.558 | 0.707 | 0.600 | 0.589 | 0.316 | 0.560 | 0.650 | 0.159 | 0.737 | 0.494 | 0.172 | 0.126 | 0.631 | 0.122 | 0.285 | 0.254 | 0.284 |
| Judicial review with legislative supermajority override | 0.558 | 0.701 | 0.594 | 0.589 | 0.317 | 0.560 | 0.653 | 0.160 | 0.727 | 0.491 | 0.182 | 0.125 | 0.583 | 0.121 | 0.284 | 0.264 | 0.266 |
| Expanded 15-seat court | 0.558 | 0.687 | 0.580 | 0.589 | 0.316 | 0.559 | 0.649 | 0.160 | 0.713 | 0.496 | 0.170 | 0.122 | 0.570 | 0.118 | 0.282 | 0.264 | 0.270 |
| Independent recusal enforcement with substitutes | 0.557 | 0.707 | 0.599 | 0.589 | 0.316 | 0.560 | 0.652 | 0.164 | 0.727 | 0.493 | 0.175 | 0.125 | 0.599 | 0.121 | 0.285 | 0.258 | 0.284 |
| Public-interest litigation filter | 0.557 | 0.736 | 0.634 | 0.589 | 0.316 | 0.562 | 0.662 | 0.178 | 0.731 | 0.487 | 0.185 | 0.131 | 0.590 | 0.126 | 0.298 | 0.258 | 0.298 |
| Random panels with jurisdiction safeguards | 0.555 | 0.709 | 0.602 | 0.589 | 0.317 | 0.588 | 0.641 | 0.139 | 0.758 | 0.491 | 0.184 | 0.140 | 0.639 | 0.110 | 0.296 | 0.254 | 0.313 |
| Constitutional remand with override window | 0.554 | 0.731 | 0.627 | 0.589 | 0.282 | 0.580 | 0.647 | 0.141 | 0.789 | 0.504 | 0.181 | 0.139 | 0.632 | 0.081 | 0.301 | 0.256 | 0.408 |
| Comparative 16-seat constitutional senates | 0.554 | 0.688 | 0.580 | 0.589 | 0.318 | 0.557 | 0.630 | 0.112 | 0.774 | 0.495 | 0.169 | 0.137 | 0.618 | 0.108 | 0.290 | 0.256 | 0.307 |
| Pre-enactment constitutional council | 0.554 | 0.706 | 0.599 | 0.589 | 0.315 | 0.604 | 0.648 | 0.146 | 0.747 | 0.499 | 0.181 | 0.124 | 0.656 | 0.120 | 0.283 | 0.261 | 0.345 |
| Constitutional council with concrete-review backstop | 0.553 | 0.703 | 0.599 | 0.589 | 0.314 | 0.604 | 0.643 | 0.131 | 0.760 | 0.502 | 0.176 | 0.123 | 0.663 | 0.120 | 0.282 | 0.258 | 0.360 |
| Stylized current U.S.-like supreme court | 0.548 | 0.691 | 0.584 | 0.589 | 0.327 | 0.547 | 0.655 | 0.172 | 0.679 | 0.468 | 0.188 | 0.196 | 0.379 | 0.349 | 0.368 | 0.296 | 0.184 |
| Supreme court with cross-checking constitutional court | 0.541 | 0.705 | 0.597 | 0.589 | 0.297 | 0.578 | 0.623 | 0.098 | 0.765 | 0.496 | 0.178 | 0.138 | 0.583 | 0.109 | 0.294 | 0.258 | 0.357 |
| Dual supreme courts with disagreement filter | 0.526 | 0.703 | 0.595 | 0.589 | 0.319 | 0.557 | 0.652 | 0.165 | 0.680 | 0.482 | 0.186 | 0.140 | 0.588 | 0.110 | 0.297 | 0.266 | 0.397 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.395 | 0.175 | 0.435 | 0.263 | 0.652 | 0.223 | 0.177 | 0.158 |
| 60 percent invalidation threshold | 0.395 | 0.125 | 0.319 | 0.200 | 0.452 | 0.134 | 0.122 | 0.122 |
| 18-year staggered terms + regular appointments | 0.395 | 0.162 | 0.406 | 0.272 | 0.579 | 0.209 | 0.189 | 0.172 |
| Jurisdiction stripping constrained by rights carveouts | 0.395 | 0.161 | 0.407 | 0.271 | 0.572 | 0.200 | 0.177 | 0.164 |
| Automatic merits follow-up for emergency relief | 0.395 | 0.193 | 0.470 | 0.315 | 0.737 | 0.283 | 0.225 | 0.185 |
| Nonpartisan commission appointments | 0.395 | 0.165 | 0.417 | 0.280 | 0.591 | 0.205 | 0.175 | 0.163 |
| Mandatory written emergency reasoning | 0.395 | 0.155 | 0.386 | 0.259 | 0.564 | 0.202 | 0.178 | 0.159 |
| Peer recusal + reasoned emergency docket | 0.395 | 0.159 | 0.402 | 0.255 | 0.580 | 0.195 | 0.172 | 0.166 |
| Retention-election accountability court | 0.395 | 0.153 | 0.393 | 0.234 | 0.544 | 0.174 | 0.158 | 0.140 |
| Emergency integrity package | 0.395 | 0.172 | 0.420 | 0.262 | 0.648 | 0.224 | 0.195 | 0.156 |
| Three-judge panels with en banc correction | 0.395 | 0.159 | 0.403 | 0.261 | 0.565 | 0.205 | 0.172 | 0.167 |
| Time-limited legislative override window | 0.395 | 0.162 | 0.410 | 0.269 | 0.574 | 0.211 | 0.176 | 0.168 |
| Constitutional remand before invalidation | 0.395 | 0.145 | 0.371 | 0.234 | 0.499 | 0.181 | 0.156 | 0.138 |
| Randomized merits panels with en banc correction | 0.395 | 0.159 | 0.405 | 0.263 | 0.559 | 0.201 | 0.171 | 0.156 |
| Judicial review with legislative supermajority override | 0.395 | 0.160 | 0.405 | 0.259 | 0.571 | 0.204 | 0.181 | 0.167 |
| Expanded 15-seat court | 0.395 | 0.160 | 0.404 | 0.267 | 0.578 | 0.204 | 0.167 | 0.162 |
| Independent recusal enforcement with substitutes | 0.395 | 0.164 | 0.414 | 0.278 | 0.580 | 0.207 | 0.180 | 0.167 |
| Public-interest litigation filter | 0.395 | 0.178 | 0.462 | 0.299 | 0.590 | 0.232 | 0.197 | 0.185 |
| Random panels with jurisdiction safeguards | 0.395 | 0.139 | 0.353 | 0.234 | 0.484 | 0.176 | 0.151 | 0.149 |
| Constitutional remand with override window | 0.395 | 0.141 | 0.359 | 0.232 | 0.491 | 0.170 | 0.147 | 0.144 |
| Comparative 16-seat constitutional senates | 0.395 | 0.112 | 0.291 | 0.162 | 0.401 | 0.103 | 0.088 | 0.097 |
| Pre-enactment constitutional council | 0.395 | 0.146 | 0.373 | 0.228 | 0.530 | 0.163 | 0.138 | 0.134 |
| Constitutional council with concrete-review backstop | 0.395 | 0.131 | 0.343 | 0.187 | 0.467 | 0.120 | 0.102 | 0.111 |
| Stylized current U.S.-like supreme court | 0.395 | 0.172 | 0.415 | 0.263 | 0.728 | 0.250 | 0.192 | 0.148 |
| Supreme court with cross-checking constitutional court | 0.395 | 0.098 | 0.254 | 0.162 | 0.321 | 0.126 | 0.116 | 0.102 |
| Dual supreme courts with disagreement filter | 0.395 | 0.165 | 0.418 | 0.283 | 0.584 | 0.209 | 0.175 | 0.176 |

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
| Appointment Timing Manipulation | No emergency relief without merits review (0.607) | Public-interest litigation filter (0.659) | No emergency relief without merits review (0.010) | Time-limited legislative override window (0.025) |
| Emergency Application Flood | No emergency relief without merits review (0.501) | Stylized current U.S.-like supreme court (0.692) | No emergency relief without merits review (0.071) | Dual supreme courts with disagreement filter (0.049) |
| Override Evasion Loop | 60 percent invalidation threshold (0.529) | No emergency relief without merits review (0.663) | No emergency relief without merits review (0.035) | Judicial review with legislative supermajority override (0.036) |
| Recusal Pressure Campaign | 60 percent invalidation threshold (0.524) | No emergency relief without merits review (0.674) | No emergency relief without merits review (0.042) | Judicial review with legislative supermajority override (0.055) |
| Court Expansion Retaliation | 60 percent invalidation threshold (0.510) | No emergency relief without merits review (0.678) | No emergency relief without merits review (0.045) | Jurisdiction stripping constrained by rights carveouts (0.059) |
