# Constitutional Review Campaign v2

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 14
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

- Highest directional score: 18-year staggered terms + regular appointments at 0.588.
- Highest rights protection: Dual supreme courts with disagreement filter at 0.619.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.004.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.187.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.023.
- Highest public confidence index: Pre-enactment constitutional council at 0.624.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, claimant success, elite acceptance, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Higher direct outputs such as `rightsClaimantSuccess`, `doctrinalDepth`, `remedialBreadth`, `lowerCourtCompliance`, `eliteAcceptance`, and `publicConfidence` are usually better, but each should be read in domain context.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `emergencyLegitimacyRisk`, `reversalRate`, `constitutionalConflict`, `administrativeCost`, and `strategicPressure` are usually better.
- Petition, admission, emergency, replacement, recusal, concurrence, dissent, fragmentation, panel, en banc, council, cross-check, formal-response, practical-response, and override rates are diagnostic rather than automatically good or bad.

## Scenario Averages Across Cases

| Scenario | Directional | Admission | Screen out | Rights protection | Claimant success | Doctrinal depth | Remedy breadth | Lower-court compliance | Elite acceptance | Public confidence | Partisan align. | Shadow abuse | Emergency risk | Emergency grants | Fragmentation | Strategic | Court-curbing | Open noncomp. | Admin cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 18-year staggered terms + regular appointments | 0.588 | 0.560 | 0.303 | 0.613 | 0.106 | 0.109 | 0.085 | 0.576 | 0.534 | 0.539 | 0.054 | 0.068 | 0.190 | 0.274 | 0.241 | 0.182 | 0.101 | 0.000 | 0.191 |
| No emergency relief without merits review | 0.585 | 0.582 | 0.281 | 0.617 | 0.108 | 0.120 | 0.079 | 0.582 | 0.534 | 0.602 | 0.037 | 0.004 | 0.187 | 0.379 | 0.248 | 0.167 | 0.093 | 0.000 | 0.236 |
| Stylized current U.S.-like supreme court | 0.584 | 0.560 | 0.304 | 0.618 | 0.115 | 0.086 | 0.061 | 0.561 | 0.530 | 0.410 | 0.054 | 0.235 | 0.255 | 0.044 | 0.292 | 0.198 | 0.103 | 0.000 | 0.154 |
| Nonpartisan commission appointments | 0.584 | 0.578 | 0.286 | 0.616 | 0.108 | 0.112 | 0.086 | 0.575 | 0.533 | 0.557 | 0.037 | 0.070 | 0.197 | 0.286 | 0.246 | 0.173 | 0.093 | 0.000 | 0.218 |
| 60 percent invalidation threshold | 0.583 | 0.561 | 0.302 | 0.602 | 0.080 | 0.094 | 0.070 | 0.575 | 0.534 | 0.525 | 0.053 | 0.061 | 0.200 | 0.204 | 0.241 | 0.185 | 0.103 | 0.000 | 0.188 |
| Peer recusal + reasoned emergency docket | 0.582 | 0.563 | 0.301 | 0.613 | 0.105 | 0.109 | 0.084 | 0.577 | 0.534 | 0.543 | 0.055 | 0.068 | 0.191 | 0.276 | 0.241 | 0.183 | 0.102 | 0.000 | 0.221 |
| Expanded 15-seat court | 0.581 | 0.563 | 0.303 | 0.612 | 0.104 | 0.108 | 0.083 | 0.577 | 0.535 | 0.549 | 0.035 | 0.068 | 0.195 | 0.277 | 0.332 | 0.182 | 0.100 | 0.000 | 0.228 |
| Retention-election accountability court | 0.581 | 0.580 | 0.283 | 0.608 | 0.101 | 0.110 | 0.076 | 0.575 | 0.530 | 0.562 | 0.038 | 0.069 | 0.196 | 0.285 | 0.303 | 0.173 | 0.064 | 0.000 | 0.218 |
| Judicial review with legislative supermajority override | 0.581 | 0.578 | 0.287 | 0.618 | 0.107 | 0.112 | 0.084 | 0.574 | 0.527 | 0.565 | 0.023 | 0.070 | 0.195 | 0.285 | 0.247 | 0.180 | 0.063 | 0.000 | 0.225 |
| Three-judge panels with en banc correction | 0.581 | 0.582 | 0.281 | 0.614 | 0.104 | 0.111 | 0.084 | 0.575 | 0.533 | 0.604 | 0.062 | 0.071 | 0.196 | 0.286 | 0.204 | 0.173 | 0.095 | 0.000 | 0.234 |
| Pre-enactment constitutional council | 0.571 | 0.581 | 0.283 | 0.612 | 0.093 | 0.107 | 0.072 | 0.576 | 0.541 | 0.624 | 0.045 | 0.070 | 0.196 | 0.287 | 0.229 | 0.177 | 0.065 | 0.000 | 0.287 |
| Comparative 16-seat constitutional senates | 0.570 | 0.562 | 0.303 | 0.597 | 0.067 | 0.090 | 0.060 | 0.576 | 0.537 | 0.593 | 0.032 | 0.062 | 0.200 | 0.205 | 0.231 | 0.170 | 0.090 | 0.000 | 0.260 |
| Dual supreme courts with disagreement filter | 0.552 | 0.577 | 0.286 | 0.619 | 0.114 | 0.116 | 0.096 | 0.568 | 0.506 | 0.554 | 0.023 | 0.063 | 0.205 | 0.212 | 0.250 | 0.184 | 0.103 | 0.000 | 0.340 |
| Supreme court with cross-checking constitutional court | 0.551 | 0.577 | 0.287 | 0.595 | 0.063 | 0.099 | 0.057 | 0.573 | 0.509 | 0.551 | 0.024 | 0.063 | 0.205 | 0.209 | 0.246 | 0.178 | 0.099 | 0.000 | 0.304 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 18-year staggered terms + regular appointments | 0.396 | 0.106 | 0.259 | 0.173 | 0.427 | 0.105 | 0.101 | 0.090 |
| No emergency relief without merits review | 0.396 | 0.108 | 0.265 | 0.150 | 0.456 | 0.099 | 0.098 | 0.067 |
| Stylized current U.S.-like supreme court | 0.396 | 0.115 | 0.274 | 0.167 | 0.533 | 0.125 | 0.106 | 0.080 |
| Nonpartisan commission appointments | 0.396 | 0.108 | 0.268 | 0.168 | 0.434 | 0.094 | 0.103 | 0.083 |
| 60 percent invalidation threshold | 0.396 | 0.080 | 0.200 | 0.137 | 0.321 | 0.060 | 0.081 | 0.061 |
| Peer recusal + reasoned emergency docket | 0.396 | 0.105 | 0.259 | 0.173 | 0.432 | 0.086 | 0.111 | 0.084 |
| Expanded 15-seat court | 0.396 | 0.104 | 0.254 | 0.171 | 0.427 | 0.090 | 0.093 | 0.087 |
| Retention-election accountability court | 0.396 | 0.101 | 0.248 | 0.159 | 0.422 | 0.081 | 0.089 | 0.075 |
| Judicial review with legislative supermajority override | 0.396 | 0.107 | 0.268 | 0.169 | 0.428 | 0.099 | 0.095 | 0.088 |
| Three-judge panels with en banc correction | 0.396 | 0.104 | 0.255 | 0.168 | 0.424 | 0.098 | 0.103 | 0.089 |
| Pre-enactment constitutional council | 0.396 | 0.093 | 0.233 | 0.137 | 0.378 | 0.077 | 0.081 | 0.066 |
| Comparative 16-seat constitutional senates | 0.396 | 0.067 | 0.171 | 0.099 | 0.268 | 0.042 | 0.063 | 0.043 |
| Dual supreme courts with disagreement filter | 0.396 | 0.114 | 0.291 | 0.186 | 0.449 | 0.091 | 0.101 | 0.101 |
| Supreme court with cross-checking constitutional court | 0.396 | 0.063 | 0.158 | 0.111 | 0.243 | 0.065 | 0.052 | 0.052 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | 18-year staggered terms + regular appointments (0.600) | Dual supreme courts with disagreement filter (0.625) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.015) |
| Partisan Appointment Pressure | 18-year staggered terms + regular appointments (0.600) | Dual supreme courts with disagreement filter (0.633) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.017) |
| Rights-Risk Legislation | 18-year staggered terms + regular appointments (0.601) | No emergency relief without merits review (0.598) | No emergency relief without merits review (0.002) | Dual supreme courts with disagreement filter (0.020) |
| Shadow-Docket Stress | 18-year staggered terms + regular appointments (0.570) | Stylized current U.S.-like supreme court (0.632) | No emergency relief without merits review (0.006) | Judicial review with legislative supermajority override (0.022) |
| High Democratic Mandate | 18-year staggered terms + regular appointments (0.604) | Dual supreme courts with disagreement filter (0.618) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.009) |
| Constitutional Conflict | No emergency relief without merits review (0.571) | Stylized current U.S.-like supreme court (0.626) | No emergency relief without merits review (0.009) | Dual supreme courts with disagreement filter (0.034) |
| Imported Legislative Output | 18-year staggered terms + regular appointments (0.599) | Dual supreme courts with disagreement filter (0.632) | No emergency relief without merits review (0.001) | Judicial review with legislative supermajority override (0.014) |
| Low Appointment Capture | 18-year staggered terms + regular appointments (0.600) | Dual supreme courts with disagreement filter (0.626) | No emergency relief without merits review (0.001) | Judicial review with legislative supermajority override (0.010) |
| Extreme Appointment Capture | 18-year staggered terms + regular appointments (0.600) | Dual supreme courts with disagreement filter (0.628) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.021) |
| Low Emergency Pressure | 18-year staggered terms + regular appointments (0.606) | Dual supreme courts with disagreement filter (0.627) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.014) |
| Extreme Emergency Pressure | 18-year staggered terms + regular appointments (0.558) | Stylized current U.S.-like supreme court (0.630) | No emergency relief without merits review (0.010) | Dual supreme courts with disagreement filter (0.027) |
| Low Rights Risk | 18-year staggered terms + regular appointments (0.609) | Dual supreme courts with disagreement filter (0.631) | No emergency relief without merits review (0.000) | Dual supreme courts with disagreement filter (0.009) |
| Extreme Rights Risk | No emergency relief without merits review (0.600) | No emergency relief without merits review (0.598) | No emergency relief without merits review (0.004) | Dual supreme courts with disagreement filter (0.027) |
| Weak-Mandate Legislation | No emergency relief without merits review (0.590) | No emergency relief without merits review (0.635) | No emergency relief without merits review (0.003) | Judicial review with legislative supermajority override (0.018) |
| Strong-Mandate Legislation | 18-year staggered terms + regular appointments (0.606) | Dual supreme courts with disagreement filter (0.619) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.010) |
| Appointment Timing Manipulation | 18-year staggered terms + regular appointments (0.600) | Dual supreme courts with disagreement filter (0.623) | No emergency relief without merits review (0.001) | Judicial review with legislative supermajority override (0.021) |
| Emergency Application Flood | No emergency relief without merits review (0.548) | Stylized current U.S.-like supreme court (0.645) | No emergency relief without merits review (0.017) | Dual supreme courts with disagreement filter (0.038) |
| Override Evasion Loop | 18-year staggered terms + regular appointments (0.580) | Dual supreme courts with disagreement filter (0.598) | No emergency relief without merits review (0.005) | Dual supreme courts with disagreement filter (0.030) |
| Recusal Pressure Campaign | 18-year staggered terms + regular appointments (0.572) | Stylized current U.S.-like supreme court (0.622) | No emergency relief without merits review (0.009) | Dual supreme courts with disagreement filter (0.043) |
| Court Expansion Retaliation | No emergency relief without merits review (0.571) | No emergency relief without merits review (0.633) | No emergency relief without merits review (0.011) | Dual supreme courts with disagreement filter (0.047) |
