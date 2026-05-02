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

- Highest directional score: No emergency relief without merits review at 0.583.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.619.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.010.
- Lowest emergency legitimacy risk: No emergency relief without merits review at 0.359.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.036.
- Highest public confidence index: No emergency relief without merits review at 0.656.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Higher direct outputs such as `rightsClaimantSuccess`, `doctrinalDepth`, `remedialBreadth`, `lowerCourtCompliance`, `eliteAcceptance`, and `publicConfidence` are usually better, but each should be read in domain context.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `emergencyLegitimacyRisk`, `reversalRate`, `constitutionalConflict`, `administrativeCost`, and `strategicPressure` are usually better.
- Petition, admission, emergency, replacement, recusal, concurrence, dissent, fragmentation, panel, en banc, council, cross-check, formal-response, practical-response, and override rates are diagnostic rather than automatically good or bad.

## Scenario Averages Across Cases

| Scenario | Directional | Admission | Screen out | Rights protection | Claimant success | Doctrinal depth | Remedy breadth | Lower-court compliance | Elite acceptance | Public confidence | Partisan align. | Shadow abuse | Emergency risk | Emergency grants | Fragmentation | Strategic | Court-curbing | Open noncomp. | Admin cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.583 | 0.750 | 0.180 | 0.612 | 0.320 | 0.188 | 0.154 | 0.548 | 0.456 | 0.656 | 0.058 | 0.010 | 0.359 | 0.626 | 0.304 | 0.228 | 0.153 | 0.000 | 0.301 |
| 18-year staggered terms + regular appointments | 0.581 | 0.735 | 0.194 | 0.601 | 0.303 | 0.165 | 0.154 | 0.535 | 0.456 | 0.547 | 0.087 | 0.127 | 0.373 | 0.491 | 0.307 | 0.249 | 0.158 | 0.000 | 0.252 |
| Stylized current U.S.-like supreme court | 0.577 | 0.733 | 0.196 | 0.619 | 0.341 | 0.124 | 0.103 | 0.506 | 0.447 | 0.317 | 0.083 | 0.424 | 0.479 | 0.120 | 0.373 | 0.275 | 0.157 | 0.000 | 0.198 |
| Nonpartisan commission appointments | 0.575 | 0.752 | 0.176 | 0.604 | 0.297 | 0.168 | 0.155 | 0.534 | 0.452 | 0.571 | 0.056 | 0.128 | 0.380 | 0.504 | 0.310 | 0.238 | 0.159 | 0.000 | 0.282 |
| Peer recusal + reasoned emergency docket | 0.575 | 0.733 | 0.196 | 0.599 | 0.302 | 0.164 | 0.152 | 0.536 | 0.457 | 0.551 | 0.088 | 0.126 | 0.371 | 0.490 | 0.305 | 0.249 | 0.157 | 0.000 | 0.284 |
| Expanded 15-seat court | 0.574 | 0.736 | 0.194 | 0.601 | 0.302 | 0.165 | 0.153 | 0.535 | 0.456 | 0.562 | 0.054 | 0.127 | 0.383 | 0.491 | 0.422 | 0.249 | 0.158 | 0.000 | 0.294 |
| Three-judge panels with en banc correction | 0.571 | 0.755 | 0.175 | 0.601 | 0.291 | 0.166 | 0.153 | 0.534 | 0.453 | 0.620 | 0.092 | 0.131 | 0.378 | 0.504 | 0.260 | 0.238 | 0.157 | 0.000 | 0.299 |
| Judicial review with legislative supermajority override | 0.571 | 0.750 | 0.181 | 0.608 | 0.300 | 0.168 | 0.153 | 0.532 | 0.441 | 0.580 | 0.036 | 0.129 | 0.378 | 0.500 | 0.309 | 0.250 | 0.103 | 0.000 | 0.289 |
| Retention-election accountability court | 0.570 | 0.754 | 0.175 | 0.589 | 0.288 | 0.166 | 0.139 | 0.533 | 0.446 | 0.577 | 0.060 | 0.129 | 0.381 | 0.502 | 0.383 | 0.238 | 0.108 | 0.000 | 0.282 |
| 60 percent invalidation threshold | 0.569 | 0.733 | 0.196 | 0.572 | 0.240 | 0.132 | 0.118 | 0.530 | 0.457 | 0.509 | 0.083 | 0.125 | 0.387 | 0.366 | 0.309 | 0.251 | 0.156 | 0.000 | 0.248 |
| Pre-enactment constitutional council | 0.557 | 0.754 | 0.176 | 0.596 | 0.270 | 0.160 | 0.131 | 0.535 | 0.467 | 0.655 | 0.068 | 0.128 | 0.376 | 0.500 | 0.293 | 0.244 | 0.105 | 0.000 | 0.376 |
| Comparative 16-seat constitutional senates | 0.553 | 0.735 | 0.196 | 0.564 | 0.222 | 0.127 | 0.107 | 0.532 | 0.460 | 0.593 | 0.049 | 0.125 | 0.387 | 0.372 | 0.297 | 0.235 | 0.148 | 0.000 | 0.331 |
| Dual supreme courts with disagreement filter | 0.535 | 0.751 | 0.180 | 0.609 | 0.308 | 0.171 | 0.176 | 0.517 | 0.416 | 0.547 | 0.036 | 0.128 | 0.399 | 0.383 | 0.314 | 0.254 | 0.163 | 0.000 | 0.427 |
| Supreme court with cross-checking constitutional court | 0.527 | 0.749 | 0.180 | 0.561 | 0.209 | 0.138 | 0.101 | 0.527 | 0.423 | 0.545 | 0.037 | 0.126 | 0.393 | 0.372 | 0.313 | 0.244 | 0.157 | 0.000 | 0.384 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | 18-year staggered terms + regular appointments (0.598) | Dual supreme courts with disagreement filter (0.600) | No emergency relief without merits review (0.005) | Dual supreme courts with disagreement filter (0.025) |
| Partisan Appointment Pressure | 18-year staggered terms + regular appointments (0.599) | Dual supreme courts with disagreement filter (0.606) | No emergency relief without merits review (0.004) | Dual supreme courts with disagreement filter (0.029) |
| Rights-Risk Legislation | No emergency relief without merits review (0.615) | No emergency relief without merits review (0.638) | No emergency relief without merits review (0.007) | Dual supreme courts with disagreement filter (0.030) |
| Shadow-Docket Stress | 18-year staggered terms + regular appointments (0.551) | Stylized current U.S.-like supreme court (0.646) | No emergency relief without merits review (0.013) | Judicial review with legislative supermajority override (0.034) |
| High Democratic Mandate | 18-year staggered terms + regular appointments (0.600) | Dual supreme courts with disagreement filter (0.575) | No emergency relief without merits review (0.003) | Dual supreme courts with disagreement filter (0.016) |
| Constitutional Conflict | No emergency relief without merits review (0.567) | Stylized current U.S.-like supreme court (0.667) | No emergency relief without merits review (0.019) | Judicial review with legislative supermajority override (0.051) |
| Imported Legislative Output | 18-year staggered terms + regular appointments (0.595) | Dual supreme courts with disagreement filter (0.604) | No emergency relief without merits review (0.004) | Judicial review with legislative supermajority override (0.024) |
| Low Appointment Capture | 18-year staggered terms + regular appointments (0.604) | Dual supreme courts with disagreement filter (0.605) | No emergency relief without merits review (0.004) | Dual supreme courts with disagreement filter (0.017) |
| Extreme Appointment Capture | 18-year staggered terms + regular appointments (0.597) | Dual supreme courts with disagreement filter (0.605) | No emergency relief without merits review (0.004) | Dual supreme courts with disagreement filter (0.035) |
| Low Emergency Pressure | 18-year staggered terms + regular appointments (0.615) | Dual supreme courts with disagreement filter (0.595) | No emergency relief without merits review (0.004) | Dual supreme courts with disagreement filter (0.022) |
| Extreme Emergency Pressure | No emergency relief without merits review (0.540) | Stylized current U.S.-like supreme court (0.659) | No emergency relief without merits review (0.018) | Dual supreme courts with disagreement filter (0.040) |
| Low Rights Risk | 18-year staggered terms + regular appointments (0.611) | Dual supreme courts with disagreement filter (0.586) | No emergency relief without merits review (0.002) | Judicial review with legislative supermajority override (0.015) |
| Extreme Rights Risk | No emergency relief without merits review (0.608) | No emergency relief without merits review (0.661) | No emergency relief without merits review (0.011) | Dual supreme courts with disagreement filter (0.043) |
| Weak-Mandate Legislation | No emergency relief without merits review (0.600) | No emergency relief without merits review (0.658) | No emergency relief without merits review (0.008) | Judicial review with legislative supermajority override (0.028) |
| Strong-Mandate Legislation | 18-year staggered terms + regular appointments (0.605) | Dual supreme courts with disagreement filter (0.574) | No emergency relief without merits review (0.002) | Dual supreme courts with disagreement filter (0.016) |
| Appointment Timing Manipulation | 18-year staggered terms + regular appointments (0.600) | Dual supreme courts with disagreement filter (0.607) | No emergency relief without merits review (0.004) | Judicial review with legislative supermajority override (0.036) |
| Emergency Application Flood | No emergency relief without merits review (0.535) | Stylized current U.S.-like supreme court (0.674) | No emergency relief without merits review (0.026) | Dual supreme courts with disagreement filter (0.054) |
| Override Evasion Loop | No emergency relief without merits review (0.577) | Stylized current U.S.-like supreme court (0.637) | No emergency relief without merits review (0.013) | Judicial review with legislative supermajority override (0.045) |
| Recusal Pressure Campaign | No emergency relief without merits review (0.566) | Stylized current U.S.-like supreme court (0.658) | No emergency relief without merits review (0.018) | Judicial review with legislative supermajority override (0.064) |
| Court Expansion Retaliation | No emergency relief without merits review (0.571) | No emergency relief without merits review (0.666) | No emergency relief without merits review (0.021) | Dual supreme courts with disagreement filter (0.067) |
