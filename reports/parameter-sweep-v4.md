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
| No emergency relief without merits review | 0.512 / 0.605 / 0.619 | 0.488 / 0.694 / 0.717 | 0.645 / 0.653 / 0.675 | 0.007 / 0.011 / 0.051 | 0.371 / 0.417 / 0.636 | 0.167 / 0.193 / 0.317 |
| Jurisdiction stripping constrained by rights carveouts | 0.500 / 0.604 / 0.619 | 0.491 / 0.686 / 0.712 | 0.638 / 0.655 / 0.665 | 0.065 / 0.088 / 0.186 | 0.377 / 0.426 / 0.663 | 0.173 / 0.195 / 0.332 |
| 18-year staggered terms + regular appointments | 0.507 / 0.604 / 0.618 | 0.502 / 0.687 / 0.710 | 0.638 / 0.654 / 0.659 | 0.063 / 0.084 / 0.177 | 0.375 / 0.417 / 0.638 | 0.183 / 0.210 / 0.337 |
| Automatic merits follow-up for emergency relief | 0.503 / 0.601 / 0.614 | 0.470 / 0.686 / 0.713 | 0.650 / 0.658 / 0.674 | 0.013 / 0.020 / 0.062 | 0.373 / 0.416 / 0.636 | 0.180 / 0.206 / 0.330 |
| Nonpartisan commission appointments | 0.502 / 0.601 / 0.615 | 0.499 / 0.688 / 0.713 | 0.640 / 0.656 / 0.663 | 0.067 / 0.085 / 0.181 | 0.380 / 0.420 / 0.645 | 0.180 / 0.201 / 0.330 |
| 60 percent invalidation threshold | 0.511 / 0.601 / 0.616 | 0.537 / 0.687 / 0.711 | 0.616 / 0.644 / 0.648 | 0.055 / 0.072 / 0.167 | 0.378 / 0.421 / 0.644 | 0.188 / 0.213 / 0.340 |
| Peer recusal + reasoned emergency docket | 0.507 / 0.599 / 0.613 | 0.506 / 0.687 / 0.713 | 0.639 / 0.653 / 0.659 | 0.064 / 0.084 / 0.177 | 0.370 / 0.419 / 0.640 | 0.184 / 0.211 / 0.339 |
| Three-judge panels with en banc correction | 0.502 / 0.599 / 0.615 | 0.503 / 0.687 / 0.711 | 0.637 / 0.655 / 0.662 | 0.063 / 0.084 / 0.185 | 0.381 / 0.421 / 0.649 | 0.176 / 0.199 / 0.330 |
| Retention-election accountability court | 0.503 / 0.599 / 0.613 | 0.509 / 0.690 / 0.712 | 0.622 / 0.646 / 0.655 | 0.067 / 0.086 / 0.181 | 0.384 / 0.425 / 0.662 | 0.178 / 0.201 / 0.328 |
| Mandatory written emergency reasoning | 0.504 / 0.599 / 0.614 | 0.513 / 0.688 / 0.712 | 0.628 / 0.650 / 0.657 | 0.033 / 0.046 / 0.128 | 0.375 / 0.419 / 0.648 | 0.187 / 0.210 / 0.342 |
| Judicial review with legislative supermajority override | 0.494 / 0.598 / 0.614 | 0.492 / 0.683 / 0.710 | 0.643 / 0.657 / 0.664 | 0.062 / 0.082 / 0.190 | 0.384 / 0.429 / 0.676 | 0.180 / 0.205 / 0.340 |
| Time-limited legislative override window | 0.497 / 0.598 / 0.612 | 0.493 / 0.685 / 0.709 | 0.638 / 0.656 / 0.665 | 0.064 / 0.085 / 0.183 | 0.381 / 0.428 / 0.672 | 0.180 / 0.205 / 0.340 |
| Independent recusal enforcement with substitutes | 0.497 / 0.597 / 0.612 | 0.499 / 0.686 / 0.711 | 0.643 / 0.658 / 0.664 | 0.067 / 0.086 / 0.185 | 0.379 / 0.427 / 0.649 | 0.177 / 0.202 / 0.332 |
| Emergency integrity package | 0.501 / 0.596 / 0.609 | 0.484 / 0.693 / 0.716 | 0.644 / 0.651 / 0.672 | 0.013 / 0.020 / 0.065 | 0.376 / 0.420 / 0.640 | 0.171 / 0.196 / 0.321 |
| Randomized merits panels with en banc correction | 0.499 / 0.596 / 0.612 | 0.506 / 0.688 / 0.712 | 0.638 / 0.653 / 0.660 | 0.068 / 0.087 / 0.188 | 0.377 / 0.422 / 0.647 | 0.176 / 0.202 / 0.331 |
| Expanded 15-seat court | 0.503 / 0.596 / 0.611 | 0.513 / 0.686 / 0.710 | 0.635 / 0.653 / 0.659 | 0.063 / 0.085 / 0.180 | 0.371 / 0.418 / 0.638 | 0.184 / 0.211 / 0.337 |
| Public-interest litigation filter | 0.494 / 0.596 / 0.612 | 0.487 / 0.684 / 0.711 | 0.649 / 0.665 / 0.676 | 0.065 / 0.089 / 0.195 | 0.385 / 0.433 / 0.663 | 0.175 / 0.204 / 0.333 |
| Random panels with jurisdiction safeguards | 0.495 / 0.595 / 0.610 | 0.513 / 0.686 / 0.709 | 0.627 / 0.648 / 0.653 | 0.054 / 0.073 / 0.168 | 0.381 / 0.425 / 0.659 | 0.173 / 0.194 / 0.329 |
| Pre-enactment constitutional council | 0.497 / 0.594 / 0.609 | 0.520 / 0.692 / 0.715 | 0.638 / 0.654 / 0.659 | 0.065 / 0.086 / 0.180 | 0.376 / 0.430 / 0.663 | 0.174 / 0.204 / 0.337 |
| Constitutional remand before invalidation | 0.503 / 0.592 / 0.609 | 0.547 / 0.701 / 0.720 | 0.633 / 0.654 / 0.658 | 0.068 / 0.092 / 0.188 | 0.383 / 0.432 / 0.655 | 0.175 / 0.203 / 0.330 |
| Constitutional council with concrete-review backstop | 0.495 / 0.591 / 0.605 | 0.535 / 0.697 / 0.718 | 0.632 / 0.646 / 0.655 | 0.066 / 0.086 / 0.184 | 0.377 / 0.426 / 0.662 | 0.174 / 0.201 / 0.329 |
| Constitutional remand with override window | 0.501 / 0.590 / 0.605 | 0.556 / 0.701 / 0.723 | 0.633 / 0.653 / 0.657 | 0.039 / 0.049 / 0.132 | 0.382 / 0.433 / 0.656 | 0.175 / 0.200 / 0.332 |
| Comparative 16-seat constitutional senates | 0.501 / 0.588 / 0.605 | 0.546 / 0.689 / 0.711 | 0.615 / 0.640 / 0.645 | 0.053 / 0.072 / 0.165 | 0.377 / 0.418 / 0.641 | 0.180 / 0.203 / 0.332 |
| Stylized current U.S.-like supreme court | 0.490 / 0.584 / 0.604 | 0.511 / 0.674 / 0.699 | 0.642 / 0.651 / 0.675 | 0.205 / 0.266 / 0.489 | 0.396 / 0.433 / 0.681 | 0.211 / 0.238 / 0.379 |
| Supreme court with cross-checking constitutional court | 0.481 / 0.578 / 0.595 | 0.532 / 0.677 / 0.700 | 0.595 / 0.640 / 0.647 | 0.056 / 0.075 / 0.169 | 0.409 / 0.453 / 0.693 | 0.180 / 0.206 / 0.336 |
| Dual supreme courts with disagreement filter | 0.463 / 0.571 / 0.589 | 0.466 / 0.664 / 0.694 | 0.637 / 0.656 / 0.659 | 0.056 / 0.075 / 0.164 | 0.408 / 0.458 / 0.685 | 0.183 / 0.211 / 0.340 |

## What Would Change the Interpretation

The table below reports each named prior's top directional-score cluster within 0.010 of that prior's best score. A design conclusion should weaken if it appears only under one narrow prior, if its cluster membership depends on high emergency pressure or high conflict, or if its apparent advantage comes with rights-protection, compliance, or emergency-power caveats.

| Prior | Cluster scenario | Score | Rights | Shadow | Emerg. downstream | Gov. noncomp. | Lower-court resistance | Caveat |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Baseline institutional prior | No emergency relief without merits review | 0.606 | 0.659 | 0.011 | 0.062 | 0.096 | 0.241 | rights-protection caveat |
| Baseline institutional prior | 18-year staggered terms + regular appointments | 0.605 | 0.658 | 0.083 | 0.072 | 0.102 | 0.245 | rights-protection caveat |
| Baseline institutional prior | Jurisdiction stripping constrained by rights carveouts | 0.605 | 0.659 | 0.089 | 0.076 | 0.099 | 0.242 | rights-protection caveat |
| Baseline institutional prior | Nonpartisan commission appointments | 0.603 | 0.656 | 0.084 | 0.071 | 0.093 | 0.244 | rights-protection caveat |
| Baseline institutional prior | Automatic merits follow-up for emergency relief | 0.602 | 0.658 | 0.019 | 0.080 | 0.092 | 0.241 | rights-protection caveat |
| Baseline institutional prior | Peer recusal + reasoned emergency docket | 0.602 | 0.655 | 0.082 | 0.071 | 0.087 | 0.243 | rights-protection caveat |
| Baseline institutional prior | Three-judge panels with en banc correction | 0.601 | 0.653 | 0.083 | 0.073 | 0.083 | 0.242 | rights-protection caveat |
| Baseline institutional prior | 60 percent invalidation threshold | 0.601 | 0.648 | 0.071 | 0.079 | 0.115 | 0.247 | rights-protection caveat |
| Baseline institutional prior | Mandatory written emergency reasoning | 0.600 | 0.651 | 0.045 | 0.073 | 0.103 | 0.245 | rights-protection caveat |
| Baseline institutional prior | Retention-election accountability court | 0.599 | 0.644 | 0.087 | 0.074 | 0.090 | 0.243 | rights-protection caveat |
| Baseline institutional prior | Time-limited legislative override window | 0.599 | 0.654 | 0.083 | 0.072 | 0.098 | 0.245 | rights-protection caveat |
| Baseline institutional prior | Judicial review with legislative supermajority override | 0.599 | 0.654 | 0.082 | 0.073 | 0.094 | 0.243 | rights-protection caveat |
| Baseline institutional prior | Expanded 15-seat court | 0.599 | 0.655 | 0.081 | 0.072 | 0.082 | 0.242 | rights-protection caveat |
| Baseline institutional prior | Randomized merits panels with en banc correction | 0.598 | 0.657 | 0.086 | 0.073 | 0.095 | 0.243 | rights-protection caveat |
| Baseline institutional prior | Independent recusal enforcement with substitutes | 0.597 | 0.659 | 0.087 | 0.076 | 0.104 | 0.244 | rights-protection caveat |
| Baseline institutional prior | Public-interest litigation filter | 0.597 | 0.667 | 0.090 | 0.079 | 0.113 | 0.245 | rights-protection caveat |
| Baseline institutional prior | Emergency integrity package | 0.597 | 0.655 | 0.020 | 0.085 | 0.099 | 0.241 | rights-protection caveat |
| Baseline institutional prior | Random panels with jurisdiction safeguards | 0.596 | 0.651 | 0.072 | 0.082 | 0.106 | 0.244 | rights-protection caveat |
| Low-polarization prior | Jurisdiction stripping constrained by rights carveouts | 0.610 | 0.662 | 0.077 | 0.068 | 0.088 | 0.233 | rights-protection caveat |
| Low-polarization prior | No emergency relief without merits review | 0.609 | 0.651 | 0.011 | 0.059 | 0.091 | 0.234 | rights-protection caveat |
| Low-polarization prior | 18-year staggered terms + regular appointments | 0.606 | 0.652 | 0.080 | 0.069 | 0.088 | 0.237 | rights-protection caveat |
| Low-polarization prior | Nonpartisan commission appointments | 0.604 | 0.660 | 0.083 | 0.072 | 0.090 | 0.236 | rights-protection caveat |
| Low-polarization prior | 60 percent invalidation threshold | 0.604 | 0.645 | 0.068 | 0.073 | 0.106 | 0.239 | rights-protection caveat |
| Low-polarization prior | Time-limited legislative override window | 0.604 | 0.661 | 0.080 | 0.068 | 0.091 | 0.236 | rights-protection caveat |
| Low-polarization prior | Automatic merits follow-up for emergency relief | 0.604 | 0.662 | 0.018 | 0.077 | 0.093 | 0.235 | rights-protection caveat |
| Low-polarization prior | Peer recusal + reasoned emergency docket | 0.603 | 0.653 | 0.081 | 0.069 | 0.092 | 0.237 | rights-protection caveat |
| Low-polarization prior | Three-judge panels with en banc correction | 0.602 | 0.655 | 0.080 | 0.067 | 0.099 | 0.237 | rights-protection caveat |
| Low-polarization prior | Mandatory written emergency reasoning | 0.602 | 0.655 | 0.045 | 0.073 | 0.098 | 0.237 | rights-protection caveat |
| Low-polarization prior | Judicial review with legislative supermajority override | 0.602 | 0.662 | 0.080 | 0.069 | 0.100 | 0.237 | rights-protection caveat |
| Low-polarization prior | Retention-election accountability court | 0.602 | 0.652 | 0.079 | 0.069 | 0.102 | 0.237 | rights-protection caveat |
| Low-polarization prior | Randomized merits panels with en banc correction | 0.601 | 0.660 | 0.084 | 0.072 | 0.091 | 0.236 | rights-protection caveat |
| Low-polarization prior | Expanded 15-seat court | 0.601 | 0.656 | 0.075 | 0.067 | 0.082 | 0.236 | rights-protection caveat |
| Low-polarization prior | Public-interest litigation filter | 0.601 | 0.664 | 0.083 | 0.073 | 0.102 | 0.236 | rights-protection caveat |
| High-polarization prior | No emergency relief without merits review | 0.604 | 0.651 | 0.012 | 0.068 | 0.093 | 0.253 | rights-protection caveat |
| High-polarization prior | 18-year staggered terms + regular appointments | 0.602 | 0.654 | 0.085 | 0.077 | 0.101 | 0.257 | rights-protection caveat |
| High-polarization prior | Jurisdiction stripping constrained by rights carveouts | 0.602 | 0.649 | 0.087 | 0.078 | 0.114 | 0.257 | rights-protection caveat |
| High-polarization prior | Automatic merits follow-up for emergency relief | 0.601 | 0.665 | 0.020 | 0.087 | 0.093 | 0.252 | rights-protection caveat |
| High-polarization prior | 60 percent invalidation threshold | 0.601 | 0.644 | 0.072 | 0.084 | 0.100 | 0.257 | rights-protection caveat |
| High-polarization prior | Retention-election accountability court | 0.599 | 0.647 | 0.085 | 0.075 | 0.082 | 0.254 | rights-protection caveat |
| High-polarization prior | Nonpartisan commission appointments | 0.598 | 0.656 | 0.089 | 0.080 | 0.098 | 0.255 | rights-protection caveat |
| High-polarization prior | Peer recusal + reasoned emergency docket | 0.597 | 0.654 | 0.091 | 0.080 | 0.091 | 0.256 | rights-protection caveat |
| High-polarization prior | Mandatory written emergency reasoning | 0.597 | 0.649 | 0.046 | 0.078 | 0.103 | 0.257 | rights-protection caveat |
| High-polarization prior | Judicial review with legislative supermajority override | 0.597 | 0.654 | 0.082 | 0.074 | 0.105 | 0.257 | rights-protection caveat |
| High-polarization prior | Time-limited legislative override window | 0.596 | 0.653 | 0.087 | 0.077 | 0.113 | 0.258 | rights-protection caveat |
| High-polarization prior | Public-interest litigation filter | 0.596 | 0.664 | 0.088 | 0.081 | 0.101 | 0.255 | rights-protection caveat |
| High-polarization prior | Randomized merits panels with en banc correction | 0.595 | 0.653 | 0.087 | 0.079 | 0.100 | 0.256 | rights-protection caveat |
| High-polarization prior | Three-judge panels with en banc correction | 0.594 | 0.654 | 0.090 | 0.082 | 0.111 | 0.257 | rights-protection caveat |
| High-polarization prior | Emergency integrity package | 0.594 | 0.651 | 0.021 | 0.092 | 0.098 | 0.253 | rights-protection caveat |
| Low appointment-capture prior | No emergency relief without merits review | 0.611 | 0.655 | 0.010 | 0.057 | 0.079 | 0.232 | rights-protection caveat |
| Low appointment-capture prior | Jurisdiction stripping constrained by rights carveouts | 0.609 | 0.657 | 0.080 | 0.068 | 0.089 | 0.234 | rights-protection caveat |
| Low appointment-capture prior | 60 percent invalidation threshold | 0.607 | 0.647 | 0.067 | 0.072 | 0.081 | 0.236 | rights-protection caveat |
| Low appointment-capture prior | 18-year staggered terms + regular appointments | 0.607 | 0.654 | 0.077 | 0.065 | 0.099 | 0.237 | rights-protection caveat |
| Low appointment-capture prior | Automatic merits follow-up for emergency relief | 0.604 | 0.658 | 0.017 | 0.076 | 0.086 | 0.233 | rights-protection caveat |
| Low appointment-capture prior | Nonpartisan commission appointments | 0.604 | 0.660 | 0.082 | 0.069 | 0.093 | 0.236 | rights-protection caveat |
| Low appointment-capture prior | Retention-election accountability court | 0.604 | 0.656 | 0.079 | 0.068 | 0.092 | 0.235 | rights-protection caveat |
| Low appointment-capture prior | Three-judge panels with en banc correction | 0.603 | 0.660 | 0.082 | 0.070 | 0.091 | 0.236 | rights-protection caveat |
| Low appointment-capture prior | Mandatory written emergency reasoning | 0.603 | 0.655 | 0.044 | 0.071 | 0.101 | 0.237 | rights-protection caveat |
| Low appointment-capture prior | Time-limited legislative override window | 0.603 | 0.656 | 0.078 | 0.067 | 0.097 | 0.237 | rights-protection caveat |
| Low appointment-capture prior | Peer recusal + reasoned emergency docket | 0.603 | 0.656 | 0.079 | 0.067 | 0.093 | 0.236 | rights-protection caveat |
| Low appointment-capture prior | Judicial review with legislative supermajority override | 0.602 | 0.663 | 0.081 | 0.071 | 0.104 | 0.236 | rights-protection caveat |
| Low appointment-capture prior | Independent recusal enforcement with substitutes | 0.602 | 0.666 | 0.082 | 0.068 | 0.094 | 0.235 | rights-protection caveat |
| Low appointment-capture prior | Expanded 15-seat court | 0.602 | 0.653 | 0.074 | 0.065 | 0.080 | 0.235 | rights-protection caveat |
| Low appointment-capture prior | Randomized merits panels with en banc correction | 0.602 | 0.655 | 0.081 | 0.070 | 0.082 | 0.235 | rights-protection caveat |
| Low appointment-capture prior | Public-interest litigation filter | 0.601 | 0.666 | 0.079 | 0.070 | 0.106 | 0.237 | rights-protection caveat |
| High appointment-capture prior | No emergency relief without merits review | 0.603 | 0.645 | 0.013 | 0.073 | 0.089 | 0.256 | rights-protection caveat |
| High appointment-capture prior | Jurisdiction stripping constrained by rights carveouts | 0.601 | 0.654 | 0.090 | 0.085 | 0.106 | 0.259 | rights-protection caveat |
| High appointment-capture prior | 18-year staggered terms + regular appointments | 0.600 | 0.651 | 0.086 | 0.081 | 0.095 | 0.261 | rights-protection caveat |
| High appointment-capture prior | Automatic merits follow-up for emergency relief | 0.597 | 0.655 | 0.022 | 0.095 | 0.093 | 0.257 | rights-protection caveat |
| High appointment-capture prior | Nonpartisan commission appointments | 0.597 | 0.654 | 0.091 | 0.084 | 0.108 | 0.262 | rights-protection caveat |
| High appointment-capture prior | Time-limited legislative override window | 0.596 | 0.662 | 0.091 | 0.085 | 0.094 | 0.259 | rights-protection caveat |
| High appointment-capture prior | 60 percent invalidation threshold | 0.596 | 0.633 | 0.080 | 0.091 | 0.109 | 0.264 | rights-protection caveat |
| High appointment-capture prior | Mandatory written emergency reasoning | 0.595 | 0.648 | 0.053 | 0.090 | 0.106 | 0.261 | rights-protection caveat |
| High appointment-capture prior | Three-judge panels with en banc correction | 0.594 | 0.647 | 0.092 | 0.084 | 0.106 | 0.261 | rights-protection caveat |
| High appointment-capture prior | Judicial review with legislative supermajority override | 0.594 | 0.661 | 0.091 | 0.085 | 0.123 | 0.262 | rights-protection caveat |
| High appointment-capture prior | Peer recusal + reasoned emergency docket | 0.594 | 0.651 | 0.091 | 0.085 | 0.104 | 0.261 | rights-protection caveat |
| High appointment-capture prior | Independent recusal enforcement with substitutes | 0.594 | 0.657 | 0.094 | 0.085 | 0.103 | 0.261 | rights-protection caveat |
| Low public-pressure prior | Jurisdiction stripping constrained by rights carveouts | 0.609 | 0.656 | 0.080 | 0.070 | 0.093 | 0.238 | rights-protection caveat |
| Low public-pressure prior | No emergency relief without merits review | 0.608 | 0.654 | 0.010 | 0.063 | 0.097 | 0.237 | rights-protection caveat |
| Low public-pressure prior | 18-year staggered terms + regular appointments | 0.607 | 0.658 | 0.079 | 0.069 | 0.094 | 0.240 | rights-protection caveat |
| Low public-pressure prior | 60 percent invalidation threshold | 0.605 | 0.647 | 0.071 | 0.076 | 0.090 | 0.240 | rights-protection caveat |
| Low public-pressure prior | Nonpartisan commission appointments | 0.605 | 0.661 | 0.084 | 0.072 | 0.076 | 0.237 | rights-protection caveat |
| Low public-pressure prior | Automatic merits follow-up for emergency relief | 0.605 | 0.656 | 0.017 | 0.074 | 0.088 | 0.238 | rights-protection caveat |
| Low public-pressure prior | Time-limited legislative override window | 0.604 | 0.658 | 0.078 | 0.068 | 0.087 | 0.239 | rights-protection caveat |
| Low public-pressure prior | Retention-election accountability court | 0.604 | 0.654 | 0.081 | 0.069 | 0.085 | 0.238 | rights-protection caveat |
| Low public-pressure prior | Mandatory written emergency reasoning | 0.603 | 0.659 | 0.045 | 0.073 | 0.098 | 0.239 | rights-protection caveat |
| Low public-pressure prior | Three-judge panels with en banc correction | 0.603 | 0.656 | 0.079 | 0.069 | 0.096 | 0.240 | rights-protection caveat |
| Low public-pressure prior | Peer recusal + reasoned emergency docket | 0.603 | 0.648 | 0.076 | 0.066 | 0.092 | 0.241 | rights-protection caveat |
| Low public-pressure prior | Emergency integrity package | 0.601 | 0.649 | 0.017 | 0.076 | 0.081 | 0.236 | rights-protection caveat |
| Low public-pressure prior | Judicial review with legislative supermajority override | 0.601 | 0.656 | 0.082 | 0.072 | 0.103 | 0.241 | rights-protection caveat |
| Low public-pressure prior | Expanded 15-seat court | 0.601 | 0.652 | 0.076 | 0.067 | 0.094 | 0.241 | rights-protection caveat |
| Low public-pressure prior | Public-interest litigation filter | 0.600 | 0.665 | 0.085 | 0.073 | 0.101 | 0.240 | rights-protection caveat |
| Low public-pressure prior | Independent recusal enforcement with substitutes | 0.600 | 0.659 | 0.079 | 0.070 | 0.103 | 0.241 | rights-protection caveat |
| Low public-pressure prior | Randomized merits panels with en banc correction | 0.599 | 0.654 | 0.086 | 0.073 | 0.089 | 0.240 | rights-protection caveat |
| High public-pressure prior | No emergency relief without merits review | 0.604 | 0.653 | 0.013 | 0.070 | 0.096 | 0.247 | rights-protection caveat |
| High public-pressure prior | Jurisdiction stripping constrained by rights carveouts | 0.603 | 0.652 | 0.089 | 0.084 | 0.093 | 0.248 | rights-protection caveat |
| High public-pressure prior | 18-year staggered terms + regular appointments | 0.602 | 0.657 | 0.086 | 0.080 | 0.094 | 0.250 | rights-protection caveat |
| High public-pressure prior | Nonpartisan commission appointments | 0.599 | 0.651 | 0.085 | 0.081 | 0.097 | 0.250 | rights-protection caveat |
| High public-pressure prior | Automatic merits follow-up for emergency relief | 0.599 | 0.656 | 0.021 | 0.092 | 0.095 | 0.248 | rights-protection caveat |
| High public-pressure prior | Mandatory written emergency reasoning | 0.598 | 0.657 | 0.049 | 0.085 | 0.103 | 0.251 | rights-protection caveat |
| High public-pressure prior | Independent recusal enforcement with substitutes | 0.597 | 0.660 | 0.085 | 0.080 | 0.102 | 0.250 | rights-protection caveat |
| High public-pressure prior | Three-judge panels with en banc correction | 0.597 | 0.658 | 0.086 | 0.082 | 0.098 | 0.250 | rights-protection caveat |
| High public-pressure prior | 60 percent invalidation threshold | 0.597 | 0.647 | 0.080 | 0.093 | 0.114 | 0.253 | rights-protection caveat |
| High public-pressure prior | Emergency integrity package | 0.596 | 0.646 | 0.020 | 0.087 | 0.090 | 0.247 | rights-protection caveat |
| High public-pressure prior | Peer recusal + reasoned emergency docket | 0.596 | 0.654 | 0.086 | 0.080 | 0.101 | 0.251 | rights-protection caveat |
| High public-pressure prior | Judicial review with legislative supermajority override | 0.595 | 0.661 | 0.094 | 0.085 | 0.120 | 0.252 | rights-protection caveat |
| High public-pressure prior | Time-limited legislative override window | 0.595 | 0.656 | 0.092 | 0.084 | 0.107 | 0.251 | rights-protection caveat |
| High public-pressure prior | Public-interest litigation filter | 0.595 | 0.663 | 0.092 | 0.086 | 0.104 | 0.250 | rights-protection caveat |
| High public-pressure prior | Retention-election accountability court | 0.595 | 0.649 | 0.092 | 0.084 | 0.108 | 0.251 | rights-protection caveat |
| High public-pressure prior | Expanded 15-seat court | 0.594 | 0.656 | 0.088 | 0.081 | 0.105 | 0.252 | rights-protection caveat |
| High public-pressure prior | Randomized merits panels with en banc correction | 0.594 | 0.651 | 0.089 | 0.083 | 0.108 | 0.252 | rights-protection caveat |
| Low emergency-share prior | Jurisdiction stripping constrained by rights carveouts | 0.611 | 0.658 | 0.068 | 0.053 | 0.084 | 0.238 | rights-protection caveat |
| Low emergency-share prior | No emergency relief without merits review | 0.611 | 0.660 | 0.009 | 0.042 | 0.089 | 0.238 | rights-protection caveat |
| Low emergency-share prior | 18-year staggered terms + regular appointments | 0.610 | 0.653 | 0.066 | 0.051 | 0.089 | 0.240 | rights-protection caveat |
| Low emergency-share prior | 60 percent invalidation threshold | 0.610 | 0.644 | 0.057 | 0.056 | 0.094 | 0.241 | rights-protection caveat |
| Low emergency-share prior | Three-judge panels with en banc correction | 0.608 | 0.659 | 0.064 | 0.052 | 0.079 | 0.238 | rights-protection caveat |
| Low emergency-share prior | Nonpartisan commission appointments | 0.607 | 0.655 | 0.071 | 0.053 | 0.089 | 0.240 | rights-protection caveat |
| Low emergency-share prior | Automatic merits follow-up for emergency relief | 0.605 | 0.663 | 0.015 | 0.056 | 0.094 | 0.238 | front-line cluster |
| Low emergency-share prior | Peer recusal + reasoned emergency docket | 0.605 | 0.652 | 0.066 | 0.053 | 0.083 | 0.239 | rights-protection caveat |
| Low emergency-share prior | Independent recusal enforcement with substitutes | 0.605 | 0.662 | 0.069 | 0.053 | 0.086 | 0.239 | front-line cluster |
| Low emergency-share prior | Time-limited legislative override window | 0.605 | 0.663 | 0.065 | 0.050 | 0.090 | 0.240 | rights-protection caveat |
| Low emergency-share prior | Randomized merits panels with en banc correction | 0.605 | 0.662 | 0.071 | 0.054 | 0.078 | 0.238 | rights-protection caveat |
| Low emergency-share prior | Mandatory written emergency reasoning | 0.604 | 0.648 | 0.036 | 0.054 | 0.094 | 0.242 | rights-protection caveat |
| Low emergency-share prior | Judicial review with legislative supermajority override | 0.604 | 0.660 | 0.062 | 0.049 | 0.105 | 0.242 | rights-protection caveat |
| Low emergency-share prior | Public-interest litigation filter | 0.604 | 0.668 | 0.068 | 0.054 | 0.100 | 0.239 | front-line cluster |
| Low emergency-share prior | Retention-election accountability court | 0.604 | 0.645 | 0.069 | 0.053 | 0.094 | 0.241 | rights-protection caveat |
| Low emergency-share prior | Expanded 15-seat court | 0.603 | 0.653 | 0.066 | 0.049 | 0.080 | 0.240 | rights-protection caveat |
| Low emergency-share prior | Random panels with jurisdiction safeguards | 0.602 | 0.650 | 0.057 | 0.057 | 0.095 | 0.240 | rights-protection caveat |
| Low emergency-share prior | Constitutional remand before invalidation | 0.602 | 0.656 | 0.070 | 0.053 | 0.089 | 0.205 | rights-protection caveat |
| Low emergency-share prior | Emergency integrity package | 0.602 | 0.654 | 0.015 | 0.058 | 0.097 | 0.239 | rights-protection caveat |
| High emergency-share prior | No emergency relief without merits review | 0.526 | 0.676 | 0.057 | 0.220 | 0.248 | 0.388 | compliance caveat |
| High emergency-share prior | Automatic merits follow-up for emergency relief | 0.519 | 0.680 | 0.071 | 0.242 | 0.244 | 0.388 | compliance caveat |
| High emergency-share prior | Emergency integrity package | 0.517 | 0.674 | 0.072 | 0.245 | 0.241 | 0.387 | compliance caveat |
| High emergency-share prior | 18-year staggered terms + regular appointments | 0.517 | 0.659 | 0.200 | 0.244 | 0.232 | 0.393 | compliance caveat |
| High emergency-share prior | Jurisdiction stripping constrained by rights carveouts | 0.516 | 0.671 | 0.203 | 0.248 | 0.269 | 0.395 | compliance caveat |
| Low rights-risk prior | Jurisdiction stripping constrained by rights carveouts | 0.632 | 0.646 | 0.058 | 0.047 | 0.048 | 0.172 | rights-protection caveat |
| Low rights-risk prior | 18-year staggered terms + regular appointments | 0.632 | 0.647 | 0.057 | 0.045 | 0.047 | 0.173 | rights-protection caveat |
| Low rights-risk prior | No emergency relief without merits review | 0.631 | 0.648 | 0.006 | 0.042 | 0.045 | 0.171 | rights-protection caveat |
| Low rights-risk prior | Nonpartisan commission appointments | 0.629 | 0.649 | 0.060 | 0.047 | 0.036 | 0.172 | rights-protection caveat |
| Low rights-risk prior | 60 percent invalidation threshold | 0.628 | 0.644 | 0.052 | 0.052 | 0.061 | 0.176 | rights-protection caveat |
| Low rights-risk prior | Automatic merits follow-up for emergency relief | 0.628 | 0.651 | 0.010 | 0.058 | 0.044 | 0.171 | rights-protection caveat |
| Low rights-risk prior | Judicial review with legislative supermajority override | 0.628 | 0.652 | 0.060 | 0.048 | 0.047 | 0.173 | rights-protection caveat |
| Low rights-risk prior | Three-judge panels with en banc correction | 0.627 | 0.651 | 0.060 | 0.048 | 0.047 | 0.173 | rights-protection caveat |
| Low rights-risk prior | Retention-election accountability court | 0.626 | 0.645 | 0.063 | 0.047 | 0.051 | 0.174 | rights-protection caveat |
| Low rights-risk prior | Time-limited legislative override window | 0.626 | 0.647 | 0.063 | 0.048 | 0.047 | 0.173 | rights-protection caveat |
| Low rights-risk prior | Peer recusal + reasoned emergency docket | 0.626 | 0.646 | 0.060 | 0.047 | 0.043 | 0.174 | rights-protection caveat |
| Low rights-risk prior | Mandatory written emergency reasoning | 0.626 | 0.649 | 0.029 | 0.049 | 0.052 | 0.173 | rights-protection caveat |
| Low rights-risk prior | Independent recusal enforcement with substitutes | 0.626 | 0.652 | 0.062 | 0.048 | 0.051 | 0.173 | rights-protection caveat |
| Low rights-risk prior | Public-interest litigation filter | 0.626 | 0.654 | 0.060 | 0.049 | 0.051 | 0.173 | rights-protection caveat |
| Low rights-risk prior | Random panels with jurisdiction safeguards | 0.625 | 0.651 | 0.049 | 0.052 | 0.047 | 0.172 | rights-protection caveat |
| Low rights-risk prior | Randomized merits panels with en banc correction | 0.624 | 0.649 | 0.063 | 0.049 | 0.052 | 0.174 | rights-protection caveat |
| Low rights-risk prior | Expanded 15-seat court | 0.624 | 0.646 | 0.057 | 0.046 | 0.050 | 0.174 | rights-protection caveat |
| Low rights-risk prior | Emergency integrity package | 0.624 | 0.643 | 0.010 | 0.058 | 0.041 | 0.171 | rights-protection caveat |
| Low rights-risk prior | Pre-enactment constitutional council | 0.623 | 0.647 | 0.061 | 0.049 | 0.046 | 0.171 | rights-protection caveat |
| High rights-risk prior | 60 percent invalidation threshold | 0.515 | 0.586 | 0.128 | 0.177 | 0.251 | 0.401 | compliance caveat |
| High rights-risk prior | No emergency relief without merits review | 0.513 | 0.644 | 0.029 | 0.112 | 0.248 | 0.393 | compliance caveat |
| High rights-risk prior | 18-year staggered terms + regular appointments | 0.508 | 0.621 | 0.140 | 0.152 | 0.243 | 0.397 | compliance caveat |
| High rights-risk prior | Peer recusal + reasoned emergency docket | 0.508 | 0.627 | 0.130 | 0.147 | 0.231 | 0.395 | compliance caveat |
| High rights-risk prior | Constitutional remand with override window | 0.505 | 0.604 | 0.099 | 0.178 | 0.266 | 0.361 | compliance caveat |
| High rights-risk prior | Constitutional remand before invalidation | 0.505 | 0.613 | 0.147 | 0.159 | 0.262 | 0.360 | compliance caveat |
| Weak democratic-mandate prior | 60 percent invalidation threshold | 0.547 | 0.642 | 0.105 | 0.136 | 0.202 | 0.373 | compliance caveat |
| Weak democratic-mandate prior | No emergency relief without merits review | 0.545 | 0.664 | 0.023 | 0.098 | 0.215 | 0.369 | compliance caveat |
| Weak democratic-mandate prior | 18-year staggered terms + regular appointments | 0.544 | 0.656 | 0.119 | 0.122 | 0.211 | 0.373 | compliance caveat |
| Weak democratic-mandate prior | Mandatory written emergency reasoning | 0.542 | 0.640 | 0.072 | 0.122 | 0.208 | 0.373 | compliance caveat |
| Weak democratic-mandate prior | Jurisdiction stripping constrained by rights carveouts | 0.539 | 0.653 | 0.119 | 0.120 | 0.238 | 0.375 | compliance caveat |
| Weak democratic-mandate prior | Constitutional remand before invalidation | 0.539 | 0.654 | 0.118 | 0.123 | 0.222 | 0.337 | compliance caveat |
| Weak democratic-mandate prior | Peer recusal + reasoned emergency docket | 0.539 | 0.650 | 0.115 | 0.117 | 0.226 | 0.374 | compliance caveat |
| Weak democratic-mandate prior | Constitutional remand with override window | 0.538 | 0.651 | 0.075 | 0.133 | 0.224 | 0.337 | compliance caveat |
| Weak democratic-mandate prior | Automatic merits follow-up for emergency relief | 0.537 | 0.662 | 0.033 | 0.103 | 0.217 | 0.370 | compliance caveat |
| High constitutional-conflict prior | No emergency relief without merits review | 0.511 | 0.675 | 0.047 | 0.149 | 0.277 | 0.428 | compliance caveat |
| High constitutional-conflict prior | 60 percent invalidation threshold | 0.510 | 0.640 | 0.158 | 0.200 | 0.288 | 0.437 | compliance caveat |
| High constitutional-conflict prior | 18-year staggered terms + regular appointments | 0.506 | 0.654 | 0.164 | 0.175 | 0.284 | 0.434 | compliance caveat |
| High constitutional-conflict prior | Mandatory written emergency reasoning | 0.505 | 0.653 | 0.118 | 0.196 | 0.281 | 0.434 | compliance caveat |
| High constitutional-conflict prior | Retention-election accountability court | 0.505 | 0.641 | 0.170 | 0.178 | 0.265 | 0.431 | compliance caveat |
| High constitutional-conflict prior | Peer recusal + reasoned emergency docket | 0.505 | 0.658 | 0.164 | 0.178 | 0.261 | 0.431 | compliance caveat |
| High constitutional-conflict prior | Nonpartisan commission appointments | 0.504 | 0.661 | 0.171 | 0.182 | 0.274 | 0.433 | compliance caveat |
| High constitutional-conflict prior | Expanded 15-seat court | 0.503 | 0.649 | 0.167 | 0.175 | 0.280 | 0.435 | compliance caveat |
| High constitutional-conflict prior | Comparative 16-seat constitutional senates | 0.502 | 0.639 | 0.156 | 0.203 | 0.266 | 0.434 | compliance caveat |
| High constitutional-conflict prior | Constitutional remand before invalidation | 0.501 | 0.654 | 0.177 | 0.186 | 0.287 | 0.397 | compliance caveat |
| High constitutional-conflict prior | Constitutional remand with override window | 0.501 | 0.651 | 0.125 | 0.202 | 0.284 | 0.399 | compliance caveat |
| High constitutional-conflict prior | Emergency integrity package | 0.501 | 0.672 | 0.061 | 0.166 | 0.292 | 0.429 | compliance caveat |
| Imported legislative-family prior | No emergency relief without merits review | 0.612 | 0.649 | 0.009 | 0.059 | 0.083 | 0.228 | rights-protection caveat |
| Imported legislative-family prior | Jurisdiction stripping constrained by rights carveouts | 0.612 | 0.652 | 0.081 | 0.070 | 0.079 | 0.229 | rights-protection caveat |
| Imported legislative-family prior | 18-year staggered terms + regular appointments | 0.610 | 0.656 | 0.075 | 0.067 | 0.093 | 0.231 | rights-protection caveat |
| Imported legislative-family prior | 60 percent invalidation threshold | 0.609 | 0.643 | 0.065 | 0.074 | 0.080 | 0.231 | rights-protection caveat |
| Imported legislative-family prior | Automatic merits follow-up for emergency relief | 0.607 | 0.652 | 0.015 | 0.075 | 0.084 | 0.229 | rights-protection caveat |
| Imported legislative-family prior | Nonpartisan commission appointments | 0.607 | 0.655 | 0.079 | 0.069 | 0.084 | 0.230 | rights-protection caveat |
| Imported legislative-family prior | Mandatory written emergency reasoning | 0.607 | 0.650 | 0.042 | 0.072 | 0.070 | 0.229 | rights-protection caveat |
| Imported legislative-family prior | Judicial review with legislative supermajority override | 0.606 | 0.657 | 0.080 | 0.069 | 0.083 | 0.230 | rights-protection caveat |
| Imported legislative-family prior | Peer recusal + reasoned emergency docket | 0.606 | 0.647 | 0.076 | 0.065 | 0.076 | 0.230 | rights-protection caveat |
| Imported legislative-family prior | Retention-election accountability court | 0.605 | 0.652 | 0.077 | 0.067 | 0.092 | 0.231 | rights-protection caveat |
| Imported legislative-family prior | Time-limited legislative override window | 0.605 | 0.654 | 0.072 | 0.066 | 0.093 | 0.232 | rights-protection caveat |
| Imported legislative-family prior | Randomized merits panels with en banc correction | 0.605 | 0.653 | 0.077 | 0.069 | 0.077 | 0.230 | rights-protection caveat |
| Imported legislative-family prior | Independent recusal enforcement with substitutes | 0.604 | 0.657 | 0.076 | 0.067 | 0.083 | 0.231 | rights-protection caveat |
| Imported legislative-family prior | Three-judge panels with en banc correction | 0.604 | 0.655 | 0.079 | 0.070 | 0.096 | 0.231 | rights-protection caveat |
| Imported legislative-family prior | Expanded 15-seat court | 0.604 | 0.651 | 0.073 | 0.066 | 0.090 | 0.232 | rights-protection caveat |
| Imported legislative-family prior | Public-interest litigation filter | 0.603 | 0.662 | 0.083 | 0.073 | 0.087 | 0.229 | rights-protection caveat |
