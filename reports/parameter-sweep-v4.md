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
| 18-year staggered terms + regular appointments | 0.533 / 0.605 / 0.617 | 0.527 / 0.682 / 0.701 | 0.631 / 0.649 / 0.652 | 0.044 / 0.062 / 0.134 | 0.334 / 0.373 / 0.559 | 0.149 / 0.173 / 0.276 |
| No emergency relief without merits review | 0.530 / 0.604 / 0.615 | 0.498 / 0.688 / 0.706 | 0.639 / 0.645 / 0.667 | 0.001 / 0.001 / 0.013 | 0.334 / 0.373 / 0.563 | 0.136 / 0.156 / 0.264 |
| Jurisdiction stripping constrained by rights carveouts | 0.523 / 0.604 / 0.613 | 0.507 / 0.681 / 0.701 | 0.639 / 0.651 / 0.656 | 0.048 / 0.062 / 0.143 | 0.342 / 0.381 / 0.588 | 0.141 / 0.160 / 0.275 |
| 60 percent invalidation threshold | 0.534 / 0.602 / 0.616 | 0.542 / 0.683 / 0.701 | 0.617 / 0.638 / 0.643 | 0.036 / 0.052 / 0.122 | 0.332 / 0.373 / 0.565 | 0.149 / 0.176 / 0.284 |
| Nonpartisan commission appointments | 0.526 / 0.602 / 0.613 | 0.514 / 0.683 / 0.702 | 0.635 / 0.650 / 0.655 | 0.048 / 0.064 / 0.138 | 0.343 / 0.374 / 0.573 | 0.143 / 0.163 / 0.272 |
| Automatic merits follow-up for emergency relief | 0.527 / 0.601 / 0.611 | 0.496 / 0.682 / 0.702 | 0.644 / 0.653 / 0.668 | 0.003 / 0.004 / 0.026 | 0.338 / 0.373 / 0.560 | 0.150 / 0.171 / 0.274 |
| Time-limited legislative override window | 0.517 / 0.600 / 0.611 | 0.502 / 0.680 / 0.698 | 0.640 / 0.652 / 0.660 | 0.047 / 0.062 / 0.142 | 0.348 / 0.385 / 0.603 | 0.146 / 0.166 / 0.286 |
| Mandatory written emergency reasoning | 0.527 / 0.600 / 0.612 | 0.528 / 0.684 / 0.701 | 0.628 / 0.646 / 0.651 | 0.018 / 0.029 / 0.086 | 0.331 / 0.374 / 0.573 | 0.151 / 0.175 / 0.287 |
| Peer recusal + reasoned emergency docket | 0.525 / 0.600 / 0.611 | 0.516 / 0.681 / 0.702 | 0.634 / 0.649 / 0.655 | 0.045 / 0.062 / 0.138 | 0.337 / 0.374 / 0.567 | 0.155 / 0.174 / 0.284 |
| Retention-election accountability court | 0.523 / 0.600 / 0.612 | 0.518 / 0.683 / 0.703 | 0.625 / 0.643 / 0.645 | 0.044 / 0.063 / 0.136 | 0.340 / 0.382 / 0.597 | 0.139 / 0.162 / 0.274 |
| Judicial review with legislative supermajority override | 0.518 / 0.600 / 0.611 | 0.503 / 0.680 / 0.699 | 0.639 / 0.651 / 0.656 | 0.048 / 0.063 / 0.142 | 0.346 / 0.386 / 0.602 | 0.145 / 0.165 / 0.286 |
| Three-judge panels with en banc correction | 0.524 / 0.599 / 0.611 | 0.516 / 0.682 / 0.702 | 0.634 / 0.650 / 0.654 | 0.046 / 0.064 / 0.138 | 0.338 / 0.381 / 0.567 | 0.139 / 0.165 / 0.269 |
| Independent recusal enforcement with substitutes | 0.522 / 0.598 / 0.610 | 0.512 / 0.682 / 0.702 | 0.637 / 0.653 / 0.658 | 0.048 / 0.064 / 0.143 | 0.340 / 0.382 / 0.578 | 0.138 / 0.165 / 0.276 |
| Expanded 15-seat court | 0.523 / 0.598 / 0.610 | 0.515 / 0.681 / 0.701 | 0.635 / 0.648 / 0.655 | 0.047 / 0.061 / 0.140 | 0.333 / 0.373 / 0.569 | 0.148 / 0.173 / 0.280 |
| Randomized merits panels with en banc correction | 0.518 / 0.598 / 0.610 | 0.512 / 0.683 / 0.703 | 0.636 / 0.648 / 0.654 | 0.046 / 0.063 / 0.141 | 0.339 / 0.377 / 0.571 | 0.137 / 0.161 / 0.276 |
| Public-interest litigation filter | 0.514 / 0.596 / 0.609 | 0.496 / 0.679 / 0.700 | 0.651 / 0.658 / 0.669 | 0.048 / 0.068 / 0.143 | 0.351 / 0.389 / 0.587 | 0.145 / 0.170 / 0.284 |
| Pre-enactment constitutional council | 0.511 / 0.593 / 0.607 | 0.519 / 0.686 / 0.705 | 0.633 / 0.645 / 0.655 | 0.045 / 0.063 / 0.139 | 0.340 / 0.383 / 0.601 | 0.139 / 0.164 / 0.284 |
| Constitutional remand before invalidation | 0.519 / 0.592 / 0.605 | 0.544 / 0.692 / 0.709 | 0.634 / 0.649 / 0.656 | 0.047 / 0.066 / 0.141 | 0.348 / 0.387 / 0.594 | 0.142 / 0.166 / 0.284 |
| Comparative 16-seat constitutional senates | 0.522 / 0.591 / 0.604 | 0.557 / 0.686 / 0.702 | 0.614 / 0.633 / 0.639 | 0.036 / 0.053 / 0.124 | 0.332 / 0.372 / 0.570 | 0.139 / 0.162 / 0.274 |
| Stylized current U.S.-like supreme court | 0.514 / 0.590 / 0.606 | 0.517 / 0.672 / 0.693 | 0.634 / 0.645 / 0.670 | 0.171 / 0.228 / 0.432 | 0.344 / 0.388 / 0.607 | 0.162 / 0.190 / 0.317 |
| Supreme court with cross-checking constitutional court | 0.502 / 0.577 / 0.591 | 0.538 / 0.671 / 0.690 | 0.597 / 0.632 / 0.643 | 0.039 / 0.053 / 0.121 | 0.371 / 0.411 / 0.613 | 0.145 / 0.172 / 0.280 |
| Dual supreme courts with disagreement filter | 0.485 / 0.572 / 0.586 | 0.472 / 0.658 / 0.682 | 0.635 / 0.656 / 0.659 | 0.039 / 0.055 / 0.128 | 0.373 / 0.420 / 0.629 | 0.150 / 0.179 / 0.292 |
