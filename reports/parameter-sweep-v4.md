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
| 18-year staggered terms + regular appointments | 0.657 / 0.720 / 0.733 | 0.451 / 0.636 / 0.685 | 0.646 / 0.679 / 0.723 | 0.095 / 0.125 / 0.218 | 0.513 / 0.548 / 0.670 | 0.322 / 0.349 / 0.429 |
| No emergency relief without merits review | 0.662 / 0.719 / 0.730 | 0.384 / 0.662 / 0.700 | 0.619 / 0.652 / 0.767 | 0.003 / 0.005 / 0.022 | 0.499 / 0.534 / 0.673 | 0.277 / 0.306 / 0.413 |
| 60 percent invalidation threshold | 0.662 / 0.718 / 0.733 | 0.506 / 0.653 / 0.687 | 0.617 / 0.650 / 0.686 | 0.080 / 0.111 / 0.214 | 0.515 / 0.549 / 0.662 | 0.334 / 0.356 / 0.422 |
| Nonpartisan commission appointments | 0.652 / 0.713 / 0.725 | 0.440 / 0.638 / 0.682 | 0.648 / 0.676 / 0.723 | 0.097 / 0.124 / 0.220 | 0.512 / 0.547 / 0.670 | 0.301 / 0.326 / 0.410 |
| Retention-election accountability court | 0.644 / 0.711 / 0.724 | 0.439 / 0.646 / 0.687 | 0.623 / 0.650 / 0.683 | 0.095 / 0.121 / 0.216 | 0.519 / 0.563 / 0.723 | 0.300 / 0.323 / 0.423 |
| Three-judge panels with en banc correction | 0.647 / 0.709 / 0.723 | 0.451 / 0.641 / 0.685 | 0.646 / 0.671 / 0.717 | 0.098 / 0.126 / 0.219 | 0.512 / 0.546 / 0.668 | 0.299 / 0.322 / 0.408 |
| Judicial review with legislative supermajority override | 0.642 / 0.708 / 0.721 | 0.419 / 0.629 / 0.678 | 0.649 / 0.684 / 0.741 | 0.097 / 0.123 / 0.219 | 0.530 / 0.574 / 0.736 | 0.320 / 0.350 / 0.474 |
| Peer recusal + reasoned emergency docket | 0.645 / 0.707 / 0.720 | 0.449 / 0.640 / 0.683 | 0.644 / 0.674 / 0.726 | 0.096 / 0.124 / 0.220 | 0.513 / 0.548 / 0.670 | 0.323 / 0.347 / 0.428 |
| Expanded 15-seat court | 0.646 / 0.705 / 0.719 | 0.445 / 0.634 / 0.683 | 0.648 / 0.681 / 0.725 | 0.096 / 0.125 / 0.221 | 0.513 / 0.548 / 0.670 | 0.325 / 0.349 / 0.428 |
| Stylized current U.S.-like supreme court | 0.638 / 0.697 / 0.717 | 0.462 / 0.633 / 0.670 | 0.642 / 0.671 / 0.764 | 0.382 / 0.472 / 0.675 | 0.534 / 0.571 / 0.721 | 0.355 / 0.385 / 0.468 |
| Pre-enactment constitutional council | 0.611 / 0.681 / 0.696 | 0.453 / 0.662 / 0.700 | 0.627 / 0.653 / 0.728 | 0.094 / 0.124 / 0.214 | 0.519 / 0.564 / 0.726 | 0.304 / 0.340 / 0.456 |
| Supreme court with cross-checking constitutional court | 0.610 / 0.664 / 0.678 | 0.539 / 0.642 / 0.671 | 0.595 / 0.619 / 0.644 | 0.080 / 0.112 / 0.215 | 0.562 / 0.596 / 0.709 | 0.310 / 0.334 / 0.405 |
| Dual supreme courts with disagreement filter | 0.585 / 0.646 / 0.661 | 0.407 / 0.581 / 0.634 | 0.657 / 0.692 / 0.726 | 0.078 / 0.112 / 0.218 | 0.576 / 0.611 / 0.729 | 0.327 / 0.348 / 0.422 |
