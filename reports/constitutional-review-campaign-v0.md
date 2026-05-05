# Constitutional Review Campaign v0

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 14
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

- Highest directional score: 18-year staggered terms + regular appointments at 0.592.
- Highest rights protection: Dual supreme courts with disagreement filter at 0.622.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.003.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.171.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.019.
- Highest public confidence index: Pre-enactment constitutional council at 0.625.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, claimant success, elite acceptance, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Higher direct outputs such as `rightsClaimantSuccess`, `doctrinalDepth`, `remedialBreadth`, `lowerCourtCompliance`, `eliteAcceptance`, and `publicConfidence` are usually better, but each should be read in domain context.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `emergencyLegitimacyRisk`, `reversalRate`, `constitutionalConflict`, `administrativeCost`, and `strategicPressure` are usually better.
- Petition, admission, emergency, replacement, recusal, concurrence, dissent, fragmentation, panel, en banc, council, cross-check, formal-response, practical-response, and override rates are diagnostic rather than automatically good or bad.

## Scenario Averages Across Cases

| Scenario | Directional | Admission | Screen out | Rights protection | Claimant success | Doctrinal depth | Remedy breadth | Lower-court compliance | Elite acceptance | Public confidence | Partisan align. | Shadow abuse | Emergency risk | Emergency grants | Fragmentation | Strategic | Court-curbing | Open noncomp. | Admin cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 18-year staggered terms + regular appointments | 0.592 | 0.552 | 0.309 | 0.615 | 0.091 | 0.101 | 0.071 | 0.582 | 0.546 | 0.543 | 0.047 | 0.062 | 0.177 | 0.257 | 0.241 | 0.173 | 0.096 | 0.000 | 0.187 |
| No emergency relief without merits review | 0.588 | 0.569 | 0.290 | 0.615 | 0.086 | 0.108 | 0.062 | 0.589 | 0.549 | 0.600 | 0.032 | 0.003 | 0.171 | 0.351 | 0.248 | 0.155 | 0.083 | 0.000 | 0.229 |
| Nonpartisan commission appointments | 0.588 | 0.568 | 0.293 | 0.618 | 0.092 | 0.103 | 0.071 | 0.582 | 0.546 | 0.561 | 0.032 | 0.064 | 0.183 | 0.266 | 0.247 | 0.163 | 0.086 | 0.000 | 0.213 |
| Stylized current U.S.-like supreme court | 0.587 | 0.551 | 0.309 | 0.616 | 0.094 | 0.080 | 0.051 | 0.567 | 0.542 | 0.420 | 0.047 | 0.218 | 0.238 | 0.033 | 0.291 | 0.189 | 0.100 | 0.000 | 0.150 |
| 60 percent invalidation threshold | 0.587 | 0.553 | 0.309 | 0.605 | 0.068 | 0.088 | 0.057 | 0.581 | 0.545 | 0.531 | 0.046 | 0.055 | 0.186 | 0.185 | 0.242 | 0.176 | 0.099 | 0.000 | 0.184 |
| Peer recusal + reasoned emergency docket | 0.586 | 0.553 | 0.308 | 0.614 | 0.089 | 0.100 | 0.069 | 0.583 | 0.546 | 0.546 | 0.047 | 0.061 | 0.177 | 0.257 | 0.242 | 0.173 | 0.098 | 0.000 | 0.216 |
| Judicial review with legislative supermajority override | 0.585 | 0.569 | 0.294 | 0.619 | 0.090 | 0.103 | 0.069 | 0.581 | 0.543 | 0.568 | 0.019 | 0.063 | 0.181 | 0.263 | 0.248 | 0.168 | 0.060 | 0.000 | 0.220 |
| Retention-election accountability court | 0.585 | 0.572 | 0.289 | 0.612 | 0.085 | 0.102 | 0.063 | 0.582 | 0.544 | 0.566 | 0.033 | 0.063 | 0.183 | 0.269 | 0.304 | 0.163 | 0.061 | 0.000 | 0.214 |
| Expanded 15-seat court | 0.585 | 0.550 | 0.310 | 0.613 | 0.087 | 0.099 | 0.068 | 0.583 | 0.547 | 0.551 | 0.029 | 0.062 | 0.180 | 0.257 | 0.330 | 0.172 | 0.095 | 0.000 | 0.222 |
| Three-judge panels with en banc correction | 0.585 | 0.574 | 0.288 | 0.617 | 0.089 | 0.103 | 0.071 | 0.581 | 0.545 | 0.609 | 0.055 | 0.065 | 0.183 | 0.265 | 0.205 | 0.164 | 0.088 | 0.000 | 0.229 |
| Pre-enactment constitutional council | 0.576 | 0.571 | 0.291 | 0.614 | 0.078 | 0.099 | 0.060 | 0.582 | 0.555 | 0.625 | 0.041 | 0.064 | 0.182 | 0.268 | 0.229 | 0.165 | 0.060 | 0.000 | 0.278 |
| Comparative 16-seat constitutional senates | 0.575 | 0.553 | 0.311 | 0.601 | 0.057 | 0.084 | 0.049 | 0.582 | 0.550 | 0.598 | 0.028 | 0.055 | 0.186 | 0.187 | 0.230 | 0.161 | 0.081 | 0.000 | 0.255 |
| Dual supreme courts with disagreement filter | 0.557 | 0.570 | 0.292 | 0.622 | 0.100 | 0.108 | 0.081 | 0.575 | 0.519 | 0.559 | 0.019 | 0.056 | 0.191 | 0.194 | 0.252 | 0.175 | 0.099 | 0.000 | 0.335 |
| Supreme court with cross-checking constitutional court | 0.556 | 0.569 | 0.295 | 0.601 | 0.056 | 0.094 | 0.049 | 0.578 | 0.522 | 0.555 | 0.020 | 0.057 | 0.193 | 0.192 | 0.247 | 0.170 | 0.095 | 0.000 | 0.299 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 18-year staggered terms + regular appointments | 0.371 | 0.091 | 0.241 | 0.143 | 0.395 | 0.078 | 0.085 | 0.075 |
| No emergency relief without merits review | 0.371 | 0.086 | 0.229 | 0.112 | 0.397 | 0.065 | 0.072 | 0.043 |
| Nonpartisan commission appointments | 0.371 | 0.092 | 0.247 | 0.144 | 0.398 | 0.074 | 0.079 | 0.064 |
| Stylized current U.S.-like supreme court | 0.371 | 0.094 | 0.238 | 0.140 | 0.481 | 0.094 | 0.072 | 0.056 |
| 60 percent invalidation threshold | 0.371 | 0.068 | 0.185 | 0.104 | 0.285 | 0.048 | 0.050 | 0.041 |
| Peer recusal + reasoned emergency docket | 0.371 | 0.089 | 0.236 | 0.149 | 0.389 | 0.066 | 0.102 | 0.061 |
| Judicial review with legislative supermajority override | 0.371 | 0.090 | 0.243 | 0.146 | 0.396 | 0.081 | 0.077 | 0.068 |
| Retention-election accountability court | 0.371 | 0.085 | 0.224 | 0.135 | 0.381 | 0.059 | 0.065 | 0.058 |
| Expanded 15-seat court | 0.371 | 0.087 | 0.226 | 0.148 | 0.388 | 0.063 | 0.070 | 0.063 |
| Three-judge panels with en banc correction | 0.371 | 0.089 | 0.240 | 0.144 | 0.387 | 0.072 | 0.080 | 0.066 |
| Pre-enactment constitutional council | 0.371 | 0.078 | 0.208 | 0.116 | 0.353 | 0.067 | 0.062 | 0.049 |
| Comparative 16-seat constitutional senates | 0.371 | 0.057 | 0.156 | 0.075 | 0.237 | 0.030 | 0.052 | 0.031 |
| Dual supreme courts with disagreement filter | 0.371 | 0.100 | 0.278 | 0.167 | 0.423 | 0.060 | 0.077 | 0.073 |
| Supreme court with cross-checking constitutional court | 0.371 | 0.056 | 0.152 | 0.104 | 0.232 | 0.062 | 0.037 | 0.041 |

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
