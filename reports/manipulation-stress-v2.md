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

- Highest directional score: No emergency relief without merits review at 0.567.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.642.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.016.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.424.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.051.
- Highest public confidence index: No emergency relief without merits review at 0.663.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Higher direct outputs such as `rightsClaimantSuccess`, `doctrinalDepth`, `remedialBreadth`, `lowerCourtCompliance`, `eliteAcceptance`, and `publicConfidence` are usually better, but each should be read in domain context.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `emergencyLegitimacyRisk`, `reversalRate`, `constitutionalConflict`, `administrativeCost`, and `strategicPressure` are usually better.
- Petition, admission, emergency, replacement, recusal, concurrence, dissent, fragmentation, panel, en banc, council, cross-check, formal-response, practical-response, and override rates are diagnostic rather than automatically good or bad.

## Scenario Averages Across Cases

| Scenario | Directional | Admission | Screen out | Rights protection | Claimant success | Doctrinal depth | Remedy breadth | Lower-court compliance | Elite acceptance | Public confidence | Partisan align. | Shadow abuse | Emergency risk | Emergency grants | Fragmentation | Strategic | Court-curbing | Open noncomp. | Admin cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.567 | 0.798 | 0.142 | 0.634 | 0.352 | 0.221 | 0.194 | 0.528 | 0.409 | 0.663 | 0.080 | 0.016 | 0.424 | 0.711 | 0.315 | 0.260 | 0.169 | 0.000 | 0.324 |
| 18-year staggered terms + regular appointments | 0.563 | 0.778 | 0.162 | 0.614 | 0.322 | 0.190 | 0.189 | 0.513 | 0.414 | 0.528 | 0.114 | 0.157 | 0.442 | 0.562 | 0.321 | 0.279 | 0.167 | 0.000 | 0.272 |
| Stylized current U.S.-like supreme court | 0.561 | 0.777 | 0.162 | 0.642 | 0.377 | 0.141 | 0.120 | 0.481 | 0.402 | 0.265 | 0.109 | 0.498 | 0.554 | 0.167 | 0.391 | 0.307 | 0.171 | 0.000 | 0.213 |
| Expanded 15-seat court | 0.555 | 0.781 | 0.161 | 0.614 | 0.321 | 0.190 | 0.188 | 0.513 | 0.413 | 0.548 | 0.071 | 0.158 | 0.457 | 0.563 | 0.443 | 0.279 | 0.167 | 0.000 | 0.316 |
| Nonpartisan commission appointments | 0.555 | 0.795 | 0.144 | 0.615 | 0.311 | 0.191 | 0.186 | 0.512 | 0.409 | 0.553 | 0.081 | 0.160 | 0.449 | 0.573 | 0.320 | 0.267 | 0.171 | 0.000 | 0.303 |
| Peer recusal + reasoned emergency docket | 0.554 | 0.779 | 0.163 | 0.610 | 0.313 | 0.188 | 0.184 | 0.514 | 0.412 | 0.534 | 0.120 | 0.157 | 0.441 | 0.565 | 0.320 | 0.279 | 0.171 | 0.000 | 0.307 |
| Three-judge panels with en banc correction | 0.551 | 0.798 | 0.141 | 0.613 | 0.305 | 0.190 | 0.185 | 0.511 | 0.408 | 0.601 | 0.126 | 0.162 | 0.444 | 0.576 | 0.272 | 0.268 | 0.174 | 0.000 | 0.321 |
| Judicial review with legislative supermajority override | 0.550 | 0.793 | 0.146 | 0.621 | 0.315 | 0.192 | 0.186 | 0.510 | 0.394 | 0.566 | 0.052 | 0.159 | 0.447 | 0.571 | 0.320 | 0.283 | 0.107 | 0.000 | 0.311 |
| Retention-election accountability court | 0.549 | 0.799 | 0.145 | 0.597 | 0.304 | 0.190 | 0.168 | 0.511 | 0.398 | 0.563 | 0.084 | 0.159 | 0.450 | 0.575 | 0.400 | 0.268 | 0.109 | 0.000 | 0.304 |
| 60 percent invalidation threshold | 0.546 | 0.778 | 0.162 | 0.577 | 0.239 | 0.149 | 0.143 | 0.508 | 0.415 | 0.482 | 0.111 | 0.156 | 0.460 | 0.441 | 0.325 | 0.280 | 0.169 | 0.000 | 0.269 |
| Pre-enactment constitutional council | 0.535 | 0.796 | 0.145 | 0.606 | 0.279 | 0.181 | 0.157 | 0.514 | 0.426 | 0.648 | 0.090 | 0.156 | 0.440 | 0.575 | 0.305 | 0.276 | 0.110 | 0.000 | 0.409 |
| Comparative 16-seat constitutional senates | 0.530 | 0.781 | 0.162 | 0.569 | 0.219 | 0.143 | 0.130 | 0.509 | 0.415 | 0.574 | 0.069 | 0.157 | 0.458 | 0.440 | 0.307 | 0.264 | 0.165 | 0.000 | 0.355 |
| Dual supreme courts with disagreement filter | 0.512 | 0.791 | 0.149 | 0.617 | 0.318 | 0.192 | 0.209 | 0.493 | 0.370 | 0.528 | 0.051 | 0.160 | 0.469 | 0.456 | 0.321 | 0.283 | 0.173 | 0.000 | 0.454 |
| Supreme court with cross-checking constitutional court | 0.502 | 0.790 | 0.148 | 0.560 | 0.201 | 0.152 | 0.119 | 0.505 | 0.376 | 0.526 | 0.054 | 0.158 | 0.462 | 0.442 | 0.321 | 0.271 | 0.173 | 0.000 | 0.410 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Appointment Timing Manipulation | 18-year staggered terms + regular appointments (0.601) | Dual supreme courts with disagreement filter (0.601) | No emergency relief without merits review (0.004) | Judicial review with legislative supermajority override (0.036) |
| Emergency Application Flood | No emergency relief without merits review (0.530) | Stylized current U.S.-like supreme court (0.671) | No emergency relief without merits review (0.026) | Dual supreme courts with disagreement filter (0.045) |
| Override Evasion Loop | No emergency relief without merits review (0.579) | Stylized current U.S.-like supreme court (0.635) | No emergency relief without merits review (0.013) | Dual supreme courts with disagreement filter (0.047) |
| Recusal Pressure Campaign | No emergency relief without merits review (0.568) | Stylized current U.S.-like supreme court (0.656) | No emergency relief without merits review (0.018) | Dual supreme courts with disagreement filter (0.054) |
| Court Expansion Retaliation | No emergency relief without merits review (0.572) | No emergency relief without merits review (0.663) | No emergency relief without merits review (0.020) | Judicial review with legislative supermajority override (0.073) |
