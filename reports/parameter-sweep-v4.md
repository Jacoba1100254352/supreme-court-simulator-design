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
| 18-year staggered terms + regular appointments | 0.545 / 0.600 / 0.611 | 0.545 / 0.672 / 0.695 | 0.572 / 0.596 / 0.624 | 0.070 / 0.097 / 0.183 | 0.399 / 0.433 / 0.573 | 0.197 / 0.218 / 0.292 |
| No emergency relief without merits review | 0.556 / 0.595 / 0.610 | 0.489 / 0.679 / 0.704 | 0.569 / 0.591 / 0.664 | 0.003 / 0.005 / 0.019 | 0.395 / 0.429 / 0.581 | 0.172 / 0.193 / 0.281 |
| Peer recusal + reasoned emergency docket | 0.536 / 0.592 / 0.605 | 0.539 / 0.671 / 0.695 | 0.575 / 0.595 / 0.626 | 0.068 / 0.094 / 0.182 | 0.401 / 0.433 / 0.566 | 0.202 / 0.220 / 0.289 |
| Nonpartisan commission appointments | 0.540 / 0.591 / 0.603 | 0.537 / 0.672 / 0.698 | 0.575 / 0.599 / 0.632 | 0.074 / 0.098 / 0.187 | 0.406 / 0.437 / 0.580 | 0.189 / 0.206 / 0.279 |
| Stylized current U.S.-like supreme court | 0.546 / 0.590 / 0.605 | 0.547 / 0.660 / 0.683 | 0.573 / 0.599 / 0.663 | 0.272 / 0.352 / 0.559 | 0.414 / 0.452 / 0.611 | 0.220 / 0.245 / 0.323 |
| Expanded 15-seat court | 0.537 / 0.590 / 0.604 | 0.543 / 0.673 / 0.696 | 0.573 / 0.595 / 0.631 | 0.072 / 0.098 / 0.183 | 0.398 / 0.433 / 0.570 | 0.197 / 0.219 / 0.289 |
| Retention-election accountability court | 0.536 / 0.589 / 0.601 | 0.547 / 0.671 / 0.697 | 0.563 / 0.589 / 0.612 | 0.075 / 0.096 / 0.182 | 0.416 / 0.444 / 0.607 | 0.188 / 0.207 / 0.277 |
| Judicial review with legislative supermajority override | 0.534 / 0.589 / 0.604 | 0.533 / 0.667 / 0.694 | 0.583 / 0.602 / 0.630 | 0.070 / 0.100 / 0.186 | 0.411 / 0.450 / 0.615 | 0.192 / 0.216 / 0.299 |
| Three-judge panels with en banc correction | 0.533 / 0.588 / 0.601 | 0.544 / 0.671 / 0.697 | 0.576 / 0.599 / 0.627 | 0.074 / 0.098 / 0.189 | 0.406 / 0.441 / 0.576 | 0.188 / 0.209 / 0.278 |
| 60 percent invalidation threshold | 0.529 / 0.587 / 0.604 | 0.596 / 0.677 / 0.696 | 0.544 / 0.576 / 0.592 | 0.063 / 0.095 / 0.181 | 0.400 / 0.436 / 0.561 | 0.205 / 0.223 / 0.290 |
| Pre-enactment constitutional council | 0.516 / 0.575 / 0.591 | 0.555 / 0.682 / 0.704 | 0.572 / 0.587 / 0.618 | 0.071 / 0.099 / 0.186 | 0.411 / 0.446 / 0.609 | 0.191 / 0.209 / 0.293 |
| Comparative 16-seat constitutional senates | 0.510 / 0.574 / 0.589 | 0.602 / 0.683 / 0.699 | 0.542 / 0.571 / 0.588 | 0.068 / 0.091 / 0.189 | 0.401 / 0.436 / 0.566 | 0.189 / 0.208 / 0.274 |
| Dual supreme courts with disagreement filter | 0.492 / 0.560 / 0.574 | 0.503 / 0.634 / 0.667 | 0.590 / 0.609 / 0.631 | 0.072 / 0.091 / 0.191 | 0.450 / 0.481 / 0.636 | 0.204 / 0.224 / 0.297 |
| Supreme court with cross-checking constitutional court | 0.482 / 0.552 / 0.571 | 0.585 / 0.660 / 0.681 | 0.536 / 0.571 / 0.588 | 0.069 / 0.091 / 0.191 | 0.441 / 0.480 / 0.623 | 0.198 / 0.218 / 0.284 |
