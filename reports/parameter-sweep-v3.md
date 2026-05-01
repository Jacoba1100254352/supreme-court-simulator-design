# Parameter Sweep Uncertainty v3

Scenario bands from varying model parameters, not only random seeds.

## Run Configuration

- runs per sweep world: 40
- cases per run: 48
- base seed: 20260501
- sweep worlds: 14
- legislative input: simulation-campaign-v21-paper.csv

## Sweep Worlds

| Key | Name | Legislative source |
| --- | --- | --- |
| `baseline` | Baseline | neutral synthetic legislature |
| `low-polarization` | Low polarization | neutral synthetic legislature |
| `high-polarization` | High polarization | neutral synthetic legislature |
| `low-appointment-capture` | Low appointment capture | neutral synthetic legislature |
| `high-appointment-capture` | High appointment capture | neutral synthetic legislature |
| `low-public-pressure` | Low public pressure | neutral synthetic legislature |
| `high-public-pressure` | High public pressure | neutral synthetic legislature |
| `low-emergency-share` | Low emergency share | neutral synthetic legislature |
| `high-emergency-share` | High emergency share | parameter emergency profile |
| `low-rights-risk` | Low rights risk | parameter low-rights profile |
| `high-rights-risk` | High rights risk | parameter high-rights profile |
| `weak-mandate` | Weak democratic mandate | parameter weak-mandate profile |
| `high-conflict` | High constitutional conflict | parameter conflict profile |
| `imported-legislative-family` | Imported legislative profile | parameter/imported blend |

## Scenario Bands

| Scenario | Directional 5/50/95 | Legal 5/50/95 | Rights 5/50/95 | Shadow 5/50/95 | Conflict 5/50/95 | Strategic 5/50/95 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.708 / 0.767 / 0.779 | 0.550 / 0.725 / 0.745 | 0.672 / 0.684 / 0.708 | 0.048 / 0.064 / 0.128 | 0.381 / 0.406 / 0.541 | 0.156 / 0.173 / 0.258 |
| 18-year staggered terms + regular appointments | 0.704 / 0.766 / 0.776 | 0.520 / 0.725 / 0.746 | 0.686 / 0.697 / 0.727 | 0.066 / 0.081 / 0.153 | 0.379 / 0.406 / 0.545 | 0.149 / 0.166 / 0.260 |
| No emergency relief without merits review | 0.706 / 0.759 / 0.768 | 0.537 / 0.734 / 0.752 | 0.677 / 0.682 / 0.733 | 0.002 / 0.004 / 0.018 | 0.372 / 0.398 / 0.537 | 0.133 / 0.149 / 0.241 |
| Nonpartisan commission appointments | 0.698 / 0.758 / 0.768 | 0.523 / 0.726 / 0.747 | 0.684 / 0.693 / 0.723 | 0.067 / 0.083 / 0.158 | 0.379 / 0.405 / 0.543 | 0.149 / 0.166 / 0.256 |
| Retention-election accountability court | 0.693 / 0.757 / 0.768 | 0.526 / 0.727 / 0.749 | 0.675 / 0.685 / 0.700 | 0.066 / 0.082 / 0.153 | 0.381 / 0.410 / 0.578 | 0.150 / 0.169 / 0.272 |
| Three-judge panels with en banc correction | 0.692 / 0.756 / 0.767 | 0.526 / 0.726 / 0.747 | 0.685 / 0.696 / 0.719 | 0.066 / 0.081 / 0.155 | 0.379 / 0.405 / 0.543 | 0.148 / 0.167 / 0.256 |
| Stylized current U.S.-like supreme court | 0.689 / 0.756 / 0.771 | 0.533 / 0.716 / 0.738 | 0.688 / 0.698 / 0.731 | 0.253 / 0.301 / 0.488 | 0.390 / 0.417 / 0.569 | 0.178 / 0.197 / 0.298 |
| Judicial review with legislative supermajority override | 0.690 / 0.755 / 0.765 | 0.512 / 0.722 / 0.745 | 0.689 / 0.700 / 0.732 | 0.066 / 0.082 / 0.153 | 0.385 / 0.415 / 0.586 | 0.156 / 0.179 / 0.305 |
| Peer recusal + reasoned emergency docket | 0.691 / 0.753 / 0.764 | 0.526 / 0.724 / 0.748 | 0.687 / 0.696 / 0.725 | 0.063 / 0.083 / 0.158 | 0.378 / 0.406 / 0.543 | 0.148 / 0.167 / 0.257 |
| Expanded 15-seat court | 0.693 / 0.752 / 0.762 | 0.518 / 0.725 / 0.747 | 0.688 / 0.700 / 0.726 | 0.068 / 0.081 / 0.152 | 0.379 / 0.406 / 0.544 | 0.150 / 0.167 / 0.258 |
| Pre-enactment constitutional council | 0.665 / 0.737 / 0.749 | 0.547 / 0.732 / 0.752 | 0.677 / 0.684 / 0.719 | 0.066 / 0.083 / 0.152 | 0.382 / 0.410 / 0.579 | 0.152 / 0.171 / 0.293 |
| Supreme court with cross-checking constitutional court | 0.658 / 0.714 / 0.726 | 0.558 / 0.711 / 0.731 | 0.649 / 0.675 / 0.690 | 0.048 / 0.064 / 0.130 | 0.418 / 0.447 / 0.581 | 0.162 / 0.177 / 0.251 |
| Dual supreme courts with disagreement filter | 0.636 / 0.699 / 0.710 | 0.479 / 0.700 / 0.723 | 0.690 / 0.701 / 0.723 | 0.048 / 0.064 / 0.130 | 0.425 / 0.451 / 0.596 | 0.167 / 0.184 / 0.272 |
