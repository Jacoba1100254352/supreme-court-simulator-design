# Adversarial Manipulation Stress Campaign v2

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 14
- experiment cases: 5

- legislative input: simulation-campaign-v21-paper.csv: volume=0.343 quality=0.610 weakMandate=0.175 rightsRisk=0.104 partisanSkew=0.237 volatility=0.120 legitimacy=0.547

## Case Weights

| Case | Weight | Legislative source | Description |
| --- | ---: | --- | --- |
| Appointment Timing Manipulation | 1.000 | adversarial/imported blend | Political actors time vacancies under high capture and public pressure. |
| Emergency Application Flood | 1.000 | emergency-flood synthetic legislature | Executives and litigants route controversial policies through urgent stay requests. |
| Override Evasion Loop | 1.000 | override-evasion synthetic legislature | Legislatures repeatedly revise invalidated laws to test rights carveouts and override thresholds. |
| Recusal Pressure Campaign | 0.850 | recusal-pressure synthetic legislature | High-salience litigants try to force or avoid recusals around ideologically charged cases. |
| Court Expansion Retaliation | 0.850 | expansion-retaliation synthetic legislature | A polarized political system reacts to judicial conflict with expansion threats and capture pressure. |

## Headline Findings

- Highest directional score: 18-year staggered terms + regular appointments at 0.574.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.624.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.008.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.230.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.034.
- Highest public confidence index: Pre-enactment constitutional council at 0.623.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, claimant success, elite acceptance, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Higher direct outputs such as `rightsClaimantSuccess`, `doctrinalDepth`, `remedialBreadth`, `lowerCourtCompliance`, `eliteAcceptance`, and `publicConfidence` are usually better, but each should be read in domain context.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `emergencyLegitimacyRisk`, `reversalRate`, `constitutionalConflict`, `administrativeCost`, and `strategicPressure` are usually better.
- Petition, admission, emergency, replacement, recusal, concurrence, dissent, fragmentation, panel, en banc, council, cross-check, formal-response, practical-response, and override rates are diagnostic rather than automatically good or bad.

## Scenario Averages Across Cases

| Scenario | Directional | Admission | Screen out | Rights protection | Claimant success | Doctrinal depth | Remedy breadth | Lower-court compliance | Elite acceptance | Public confidence | Partisan align. | Shadow abuse | Emergency risk | Emergency grants | Fragmentation | Strategic | Court-curbing | Open noncomp. | Admin cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 18-year staggered terms + regular appointments | 0.574 | 0.595 | 0.279 | 0.612 | 0.131 | 0.128 | 0.108 | 0.560 | 0.496 | 0.529 | 0.076 | 0.089 | 0.239 | 0.340 | 0.255 | 0.212 | 0.119 | 0.000 | 0.209 |
| No emergency relief without merits review | 0.573 | 0.612 | 0.260 | 0.618 | 0.137 | 0.141 | 0.101 | 0.569 | 0.495 | 0.605 | 0.057 | 0.008 | 0.230 | 0.452 | 0.255 | 0.195 | 0.121 | 0.000 | 0.253 |
| Stylized current U.S.-like supreme court | 0.570 | 0.601 | 0.272 | 0.624 | 0.153 | 0.102 | 0.079 | 0.541 | 0.490 | 0.375 | 0.073 | 0.295 | 0.319 | 0.066 | 0.309 | 0.232 | 0.120 | 0.000 | 0.168 |
| Nonpartisan commission appointments | 0.570 | 0.609 | 0.265 | 0.616 | 0.136 | 0.131 | 0.111 | 0.559 | 0.494 | 0.548 | 0.057 | 0.091 | 0.243 | 0.345 | 0.255 | 0.202 | 0.116 | 0.000 | 0.235 |
| 60 percent invalidation threshold | 0.568 | 0.597 | 0.279 | 0.600 | 0.101 | 0.110 | 0.091 | 0.558 | 0.497 | 0.513 | 0.075 | 0.081 | 0.248 | 0.258 | 0.254 | 0.213 | 0.120 | 0.000 | 0.205 |
| Expanded 15-seat court | 0.568 | 0.596 | 0.276 | 0.615 | 0.133 | 0.128 | 0.108 | 0.561 | 0.497 | 0.544 | 0.048 | 0.090 | 0.244 | 0.338 | 0.347 | 0.212 | 0.119 | 0.000 | 0.246 |
| Peer recusal + reasoned emergency docket | 0.568 | 0.593 | 0.281 | 0.611 | 0.130 | 0.127 | 0.106 | 0.561 | 0.496 | 0.533 | 0.076 | 0.090 | 0.238 | 0.336 | 0.252 | 0.213 | 0.122 | 0.000 | 0.238 |
| Retention-election accountability court | 0.566 | 0.615 | 0.257 | 0.607 | 0.130 | 0.130 | 0.099 | 0.558 | 0.487 | 0.555 | 0.057 | 0.091 | 0.245 | 0.347 | 0.318 | 0.202 | 0.079 | 0.000 | 0.237 |
| Judicial review with legislative supermajority override | 0.566 | 0.611 | 0.265 | 0.620 | 0.137 | 0.132 | 0.109 | 0.557 | 0.484 | 0.558 | 0.035 | 0.091 | 0.244 | 0.345 | 0.257 | 0.214 | 0.077 | 0.000 | 0.243 |
| Three-judge panels with en banc correction | 0.566 | 0.623 | 0.252 | 0.617 | 0.136 | 0.133 | 0.113 | 0.558 | 0.491 | 0.596 | 0.088 | 0.093 | 0.245 | 0.352 | 0.218 | 0.204 | 0.121 | 0.000 | 0.254 |
| Pre-enactment constitutional council | 0.555 | 0.615 | 0.259 | 0.614 | 0.121 | 0.127 | 0.095 | 0.559 | 0.504 | 0.623 | 0.065 | 0.091 | 0.243 | 0.350 | 0.239 | 0.210 | 0.078 | 0.000 | 0.316 |
| Comparative 16-seat constitutional senates | 0.555 | 0.590 | 0.281 | 0.593 | 0.086 | 0.104 | 0.079 | 0.560 | 0.500 | 0.583 | 0.047 | 0.081 | 0.244 | 0.256 | 0.239 | 0.199 | 0.114 | 0.000 | 0.278 |
| Dual supreme courts with disagreement filter | 0.535 | 0.613 | 0.261 | 0.618 | 0.138 | 0.134 | 0.120 | 0.550 | 0.465 | 0.549 | 0.034 | 0.084 | 0.255 | 0.265 | 0.260 | 0.215 | 0.120 | 0.000 | 0.365 |
| Supreme court with cross-checking constitutional court | 0.532 | 0.610 | 0.262 | 0.588 | 0.075 | 0.112 | 0.072 | 0.556 | 0.467 | 0.543 | 0.036 | 0.084 | 0.254 | 0.259 | 0.257 | 0.209 | 0.124 | 0.000 | 0.326 |

## Domain-Specific Rights Claimant Success

| Scenario | Claimant case share | Aggregate | Rights | Structural | Election | Executive | Administrative | Economic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 18-year staggered terms + regular appointments | 0.442 | 0.131 | 0.309 | 0.210 | 0.539 | 0.125 | 0.148 | 0.125 |
| No emergency relief without merits review | 0.442 | 0.137 | 0.339 | 0.204 | 0.583 | 0.113 | 0.129 | 0.091 |
| Stylized current U.S.-like supreme court | 0.442 | 0.153 | 0.369 | 0.193 | 0.672 | 0.176 | 0.161 | 0.108 |
| Nonpartisan commission appointments | 0.442 | 0.136 | 0.334 | 0.206 | 0.538 | 0.134 | 0.123 | 0.124 |
| 60 percent invalidation threshold | 0.442 | 0.101 | 0.253 | 0.143 | 0.400 | 0.065 | 0.086 | 0.085 |
| Expanded 15-seat court | 0.442 | 0.133 | 0.328 | 0.205 | 0.530 | 0.122 | 0.121 | 0.099 |
| Peer recusal + reasoned emergency docket | 0.442 | 0.130 | 0.315 | 0.203 | 0.515 | 0.114 | 0.144 | 0.124 |
| Retention-election accountability court | 0.442 | 0.130 | 0.323 | 0.183 | 0.540 | 0.109 | 0.101 | 0.106 |
| Judicial review with legislative supermajority override | 0.442 | 0.137 | 0.325 | 0.231 | 0.547 | 0.131 | 0.164 | 0.128 |
| Three-judge panels with en banc correction | 0.442 | 0.136 | 0.330 | 0.220 | 0.520 | 0.141 | 0.144 | 0.111 |
| Pre-enactment constitutional council | 0.442 | 0.121 | 0.306 | 0.189 | 0.480 | 0.095 | 0.097 | 0.082 |
| Comparative 16-seat constitutional senates | 0.442 | 0.086 | 0.219 | 0.113 | 0.358 | 0.043 | 0.056 | 0.068 |
| Dual supreme courts with disagreement filter | 0.442 | 0.138 | 0.338 | 0.223 | 0.545 | 0.121 | 0.123 | 0.110 |
| Supreme court with cross-checking constitutional court | 0.442 | 0.075 | 0.182 | 0.113 | 0.282 | 0.078 | 0.077 | 0.059 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Appointment Timing Manipulation | 18-year staggered terms + regular appointments (0.599) | Dual supreme courts with disagreement filter (0.629) | No emergency relief without merits review (0.001) | Judicial review with legislative supermajority override (0.021) |
| Emergency Application Flood | No emergency relief without merits review (0.550) | Stylized current U.S.-like supreme court (0.645) | No emergency relief without merits review (0.017) | Dual supreme courts with disagreement filter (0.032) |
| Override Evasion Loop | 18-year staggered terms + regular appointments (0.579) | Judicial review with legislative supermajority override (0.606) | No emergency relief without merits review (0.005) | Dual supreme courts with disagreement filter (0.031) |
| Recusal Pressure Campaign | 18-year staggered terms + regular appointments (0.572) | Stylized current U.S.-like supreme court (0.624) | No emergency relief without merits review (0.008) | Dual supreme courts with disagreement filter (0.036) |
| Court Expansion Retaliation | No emergency relief without merits review (0.572) | Stylized current U.S.-like supreme court (0.632) | No emergency relief without merits review (0.010) | Judicial review with legislative supermajority override (0.053) |
