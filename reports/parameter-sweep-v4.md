# Parameter Sweep Priors v4

Scenario bands from named uncertainty priors, not only random seeds. Prior weights are descriptive modeling weights used to document relative plausibility; the percentile bands below still summarize one observation per prior profile.

## Run Configuration

- runs per sweep world: 40
- cases per run: 48
- base seed: 20260501
- named priors: 14
- legislative input: simulation-campaign-v21-paper.csv

## Named Prior Profiles

| Key | Name | Weight | Legislative source | Rationale |
| --- | --- | ---: | --- | --- |
| `baseline` | Baseline institutional prior | 1.000 | neutral synthetic legislature | Central case for ordinary constitutional review. |
| `low-polarization` | Low-polarization prior | 0.600 | neutral synthetic legislature | Political branches and candidate pool are less polarized. |
| `high-polarization` | High-polarization prior | 0.850 | neutral synthetic legislature | Polarization and appointment capture both rise. |
| `low-appointment-capture` | Low appointment-capture prior | 0.550 | neutral synthetic legislature | Appointment incentives are less partisan. |
| `high-appointment-capture` | High appointment-capture prior | 0.800 | neutral synthetic legislature | Vacancies become unusually strategic. |
| `low-public-pressure` | Low public-pressure prior | 0.450 | neutral synthetic legislature | Cases receive less public attention. |
| `high-public-pressure` | High public-pressure prior | 0.700 | neutral synthetic legislature | Public attention and accountability pressures rise. |
| `low-emergency-share` | Low emergency-share prior | 0.500 | neutral synthetic legislature | Few cases arrive as urgent applications. |
| `high-emergency-share` | High emergency-share prior | 0.850 | parameter emergency profile | Emergency routing becomes institutionally important. |
| `low-rights-risk` | Low rights-risk prior | 0.450 | parameter low-rights profile | Legislative outputs rarely burden protected interests. |
| `high-rights-risk` | High rights-risk prior | 0.850 | parameter high-rights profile | Rights burdens and legal defects are common. |
| `weak-mandate` | Weak democratic-mandate prior | 0.750 | parameter weak-mandate profile | Reviewed laws have low public legitimacy. |
| `high-conflict` | High constitutional-conflict prior | 0.900 | parameter conflict profile | Interbranch conflict and defiance risk rise together. |
| `imported-legislative-family` | Imported legislative-family prior | 0.700 | parameter/imported blend | A congressional simulator output is blended into the docket assumptions. |

## Scenario Bands

| Scenario | Directional 5/50/95 | Legal 5/50/95 | Rights 5/50/95 | Shadow 5/50/95 | Conflict 5/50/95 | Strategic 5/50/95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 18-year staggered terms + regular appointments | 0.564 / 0.599 / 0.608 | 0.589 / 0.705 / 0.718 | 0.600 / 0.619 / 0.628 | 0.033 / 0.049 / 0.109 | 0.277 / 0.308 / 0.448 | 0.134 / 0.150 / 0.229 |
| 60 percent invalidation threshold | 0.557 / 0.596 / 0.605 | 0.613 / 0.706 / 0.720 | 0.583 / 0.612 / 0.621 | 0.030 / 0.041 / 0.101 | 0.277 / 0.309 / 0.446 | 0.138 / 0.153 / 0.230 |
| Stylized current U.S.-like supreme court | 0.560 / 0.596 / 0.605 | 0.590 / 0.699 / 0.715 | 0.603 / 0.623 / 0.635 | 0.133 / 0.184 / 0.343 | 0.284 / 0.315 / 0.467 | 0.141 / 0.166 / 0.253 |
| Nonpartisan commission appointments | 0.559 / 0.596 / 0.603 | 0.593 / 0.706 / 0.721 | 0.601 / 0.624 / 0.631 | 0.037 / 0.049 / 0.112 | 0.283 / 0.310 / 0.453 | 0.127 / 0.140 / 0.217 |
| No emergency relief without merits review | 0.565 / 0.595 / 0.602 | 0.589 / 0.710 / 0.725 | 0.603 / 0.617 / 0.635 | 0.001 / 0.001 / 0.011 | 0.283 / 0.309 / 0.452 | 0.119 / 0.133 / 0.209 |
| Retention-election accountability court | 0.558 / 0.594 / 0.602 | 0.595 / 0.706 / 0.722 | 0.590 / 0.619 / 0.627 | 0.038 / 0.048 / 0.110 | 0.289 / 0.314 / 0.471 | 0.125 / 0.138 / 0.218 |
| Judicial review with legislative supermajority override | 0.556 / 0.594 / 0.603 | 0.588 / 0.704 / 0.720 | 0.601 / 0.626 / 0.632 | 0.035 / 0.050 / 0.115 | 0.287 / 0.316 / 0.471 | 0.127 / 0.141 / 0.228 |
| Three-judge panels with en banc correction | 0.554 / 0.593 / 0.602 | 0.596 / 0.704 / 0.723 | 0.599 / 0.622 / 0.628 | 0.037 / 0.050 / 0.114 | 0.286 / 0.315 / 0.454 | 0.126 / 0.142 / 0.216 |
| Peer recusal + reasoned emergency docket | 0.557 / 0.593 / 0.603 | 0.593 / 0.705 / 0.719 | 0.597 / 0.620 / 0.627 | 0.033 / 0.049 / 0.112 | 0.278 / 0.308 / 0.447 | 0.135 / 0.152 / 0.228 |
| Expanded 15-seat court | 0.556 / 0.591 / 0.599 | 0.595 / 0.706 / 0.719 | 0.598 / 0.620 / 0.625 | 0.033 / 0.048 / 0.111 | 0.277 / 0.308 / 0.448 | 0.133 / 0.151 / 0.231 |
| Comparative 16-seat constitutional senates | 0.542 / 0.584 / 0.593 | 0.624 / 0.707 / 0.720 | 0.575 / 0.607 / 0.620 | 0.030 / 0.043 / 0.099 | 0.278 / 0.308 / 0.442 | 0.123 / 0.138 / 0.213 |
| Pre-enactment constitutional council | 0.543 / 0.584 / 0.594 | 0.606 / 0.710 / 0.725 | 0.597 / 0.621 / 0.627 | 0.034 / 0.051 / 0.112 | 0.286 / 0.317 / 0.474 | 0.121 / 0.140 / 0.226 |
| Supreme court with cross-checking constitutional court | 0.522 / 0.567 / 0.579 | 0.605 / 0.695 / 0.709 | 0.567 / 0.611 / 0.624 | 0.031 / 0.041 / 0.100 | 0.309 / 0.343 / 0.490 | 0.130 / 0.149 / 0.226 |
| Dual supreme courts with disagreement filter | 0.523 / 0.566 / 0.579 | 0.555 / 0.685 / 0.705 | 0.601 / 0.626 / 0.633 | 0.029 / 0.043 / 0.102 | 0.309 / 0.343 / 0.499 | 0.130 / 0.152 / 0.231 |
