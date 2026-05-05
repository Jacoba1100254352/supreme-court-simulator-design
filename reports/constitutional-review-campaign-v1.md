# Constitutional Review Campaign v1

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 14
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

- Highest directional score: 18-year staggered terms + regular appointments at 0.593.
- Highest rights protection: Dual supreme courts with disagreement filter at 0.620.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.003.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.171.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.018.
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
| 18-year staggered terms + regular appointments | 0.593 | 0.549 | 0.311 | 0.613 | 0.096 | 0.102 | 0.076 | 0.582 | 0.547 | 0.542 | 0.046 | 0.061 | 0.174 | 0.252 | 0.236 | 0.171 | 0.095 | 0.000 | 0.185 |
| No emergency relief without merits review | 0.589 | 0.571 | 0.290 | 0.617 | 0.097 | 0.112 | 0.071 | 0.587 | 0.548 | 0.600 | 0.032 | 0.003 | 0.171 | 0.351 | 0.244 | 0.157 | 0.084 | 0.000 | 0.229 |
| Stylized current U.S.-like supreme court | 0.589 | 0.549 | 0.311 | 0.616 | 0.101 | 0.082 | 0.056 | 0.567 | 0.543 | 0.423 | 0.047 | 0.215 | 0.235 | 0.035 | 0.287 | 0.187 | 0.097 | 0.000 | 0.149 |
| Nonpartisan commission appointments | 0.589 | 0.566 | 0.295 | 0.617 | 0.098 | 0.105 | 0.077 | 0.581 | 0.547 | 0.560 | 0.032 | 0.063 | 0.181 | 0.265 | 0.242 | 0.163 | 0.085 | 0.000 | 0.212 |
| 60 percent invalidation threshold | 0.589 | 0.549 | 0.313 | 0.604 | 0.074 | 0.089 | 0.063 | 0.580 | 0.547 | 0.530 | 0.045 | 0.054 | 0.182 | 0.185 | 0.236 | 0.174 | 0.097 | 0.000 | 0.182 |
| Peer recusal + reasoned emergency docket | 0.587 | 0.552 | 0.310 | 0.613 | 0.095 | 0.102 | 0.075 | 0.582 | 0.547 | 0.545 | 0.047 | 0.061 | 0.175 | 0.256 | 0.237 | 0.173 | 0.095 | 0.000 | 0.215 |
| Retention-election accountability court | 0.586 | 0.569 | 0.291 | 0.610 | 0.091 | 0.103 | 0.068 | 0.581 | 0.544 | 0.565 | 0.033 | 0.062 | 0.179 | 0.264 | 0.299 | 0.163 | 0.059 | 0.000 | 0.212 |
| Judicial review with legislative supermajority override | 0.586 | 0.566 | 0.296 | 0.618 | 0.097 | 0.105 | 0.075 | 0.580 | 0.542 | 0.567 | 0.019 | 0.062 | 0.179 | 0.263 | 0.243 | 0.168 | 0.059 | 0.000 | 0.219 |
| Expanded 15-seat court | 0.586 | 0.551 | 0.311 | 0.613 | 0.095 | 0.102 | 0.075 | 0.582 | 0.548 | 0.552 | 0.028 | 0.061 | 0.177 | 0.255 | 0.326 | 0.172 | 0.094 | 0.000 | 0.222 |
| Three-judge panels with en banc correction | 0.586 | 0.572 | 0.288 | 0.615 | 0.094 | 0.105 | 0.076 | 0.581 | 0.546 | 0.608 | 0.053 | 0.064 | 0.180 | 0.264 | 0.201 | 0.163 | 0.087 | 0.000 | 0.228 |
| Pre-enactment constitutional council | 0.576 | 0.570 | 0.291 | 0.613 | 0.084 | 0.101 | 0.065 | 0.581 | 0.554 | 0.624 | 0.039 | 0.063 | 0.180 | 0.266 | 0.225 | 0.166 | 0.060 | 0.000 | 0.278 |
| Comparative 16-seat constitutional senates | 0.576 | 0.552 | 0.311 | 0.599 | 0.062 | 0.086 | 0.054 | 0.582 | 0.550 | 0.597 | 0.027 | 0.055 | 0.183 | 0.188 | 0.227 | 0.160 | 0.081 | 0.000 | 0.254 |
| Dual supreme courts with disagreement filter | 0.558 | 0.567 | 0.294 | 0.620 | 0.105 | 0.110 | 0.087 | 0.574 | 0.520 | 0.556 | 0.018 | 0.056 | 0.188 | 0.193 | 0.247 | 0.174 | 0.097 | 0.000 | 0.333 |
| Supreme court with cross-checking constitutional court | 0.557 | 0.567 | 0.295 | 0.599 | 0.059 | 0.094 | 0.052 | 0.578 | 0.523 | 0.554 | 0.020 | 0.056 | 0.188 | 0.190 | 0.243 | 0.168 | 0.092 | 0.000 | 0.297 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 18-year staggered terms + regular appointments | 0.379 | 0.096 | 0.239 | 0.154 | 0.395 | 0.097 | 0.090 | 0.080 |
| No emergency relief without merits review | 0.379 | 0.097 | 0.237 | 0.132 | 0.416 | 0.090 | 0.092 | 0.062 |
| Stylized current U.S.-like supreme court | 0.379 | 0.101 | 0.241 | 0.148 | 0.494 | 0.112 | 0.089 | 0.070 |
| Nonpartisan commission appointments | 0.379 | 0.098 | 0.248 | 0.147 | 0.403 | 0.085 | 0.092 | 0.075 |
| 60 percent invalidation threshold | 0.379 | 0.074 | 0.188 | 0.123 | 0.300 | 0.057 | 0.070 | 0.053 |
| Peer recusal + reasoned emergency docket | 0.379 | 0.095 | 0.237 | 0.155 | 0.402 | 0.073 | 0.099 | 0.073 |
| Retention-election accountability court | 0.379 | 0.091 | 0.226 | 0.144 | 0.387 | 0.067 | 0.082 | 0.067 |
| Judicial review with legislative supermajority override | 0.379 | 0.097 | 0.244 | 0.152 | 0.401 | 0.088 | 0.086 | 0.078 |
| Expanded 15-seat court | 0.379 | 0.095 | 0.233 | 0.155 | 0.397 | 0.081 | 0.080 | 0.079 |
| Three-judge panels with en banc correction | 0.379 | 0.094 | 0.236 | 0.150 | 0.397 | 0.082 | 0.093 | 0.075 |
| Pre-enactment constitutional council | 0.379 | 0.084 | 0.211 | 0.128 | 0.346 | 0.075 | 0.073 | 0.059 |
| Comparative 16-seat constitutional senates | 0.379 | 0.062 | 0.158 | 0.088 | 0.249 | 0.040 | 0.066 | 0.040 |
| Dual supreme courts with disagreement filter | 0.379 | 0.105 | 0.275 | 0.167 | 0.421 | 0.076 | 0.090 | 0.089 |
| Supreme court with cross-checking constitutional court | 0.379 | 0.059 | 0.149 | 0.105 | 0.232 | 0.061 | 0.046 | 0.050 |

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
