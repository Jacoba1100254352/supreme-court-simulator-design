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
| No emergency relief without merits review | 0.511 / 0.608 / 0.625 | 0.457 / 0.659 / 0.695 | 0.615 / 0.647 / 0.653 | 0.007 / 0.011 / 0.043 | 0.346 / 0.384 / 0.588 | 0.170 / 0.195 / 0.316 |
| 60 percent invalidation threshold | 0.519 / 0.605 / 0.621 | 0.525 / 0.668 / 0.693 | 0.589 / 0.634 / 0.644 | 0.050 / 0.071 / 0.153 | 0.348 / 0.386 / 0.581 | 0.185 / 0.210 / 0.322 |
| 18-year staggered terms + regular appointments | 0.513 / 0.605 / 0.621 | 0.495 / 0.658 / 0.691 | 0.599 / 0.643 / 0.648 | 0.059 / 0.079 / 0.164 | 0.344 / 0.387 / 0.586 | 0.186 / 0.211 / 0.327 |
| Jurisdiction stripping constrained by rights carveouts | 0.509 / 0.605 / 0.621 | 0.481 / 0.660 / 0.688 | 0.599 / 0.641 / 0.648 | 0.057 / 0.079 / 0.168 | 0.355 / 0.395 / 0.611 | 0.176 / 0.202 / 0.334 |
| Automatic merits follow-up for emergency relief | 0.500 / 0.603 / 0.619 | 0.448 / 0.656 / 0.690 | 0.613 / 0.646 / 0.654 | 0.012 / 0.017 / 0.055 | 0.346 / 0.384 / 0.596 | 0.183 / 0.204 / 0.329 |
| Nonpartisan commission appointments | 0.507 / 0.602 / 0.618 | 0.483 / 0.660 / 0.691 | 0.600 / 0.642 / 0.650 | 0.062 / 0.078 / 0.165 | 0.351 / 0.386 / 0.592 | 0.179 / 0.201 / 0.323 |
| Public-interest litigation filter | 0.514 / 0.601 / 0.617 | 0.500 / 0.662 / 0.693 | 0.606 / 0.645 / 0.652 | 0.057 / 0.075 / 0.163 | 0.348 / 0.385 / 0.581 | 0.170 / 0.198 / 0.311 |
| Mandatory written emergency reasoning | 0.508 / 0.601 / 0.617 | 0.497 / 0.663 / 0.692 | 0.595 / 0.638 / 0.648 | 0.033 / 0.051 / 0.126 | 0.346 / 0.388 / 0.587 | 0.183 / 0.211 / 0.326 |
| Retention-election accountability court | 0.510 / 0.601 / 0.617 | 0.490 / 0.662 / 0.692 | 0.582 / 0.638 / 0.645 | 0.058 / 0.077 / 0.159 | 0.357 / 0.399 / 0.607 | 0.181 / 0.204 / 0.319 |
| Emergency integrity package | 0.504 / 0.601 / 0.617 | 0.454 / 0.660 / 0.692 | 0.617 / 0.647 / 0.659 | 0.012 / 0.018 / 0.054 | 0.352 / 0.388 / 0.586 | 0.175 / 0.198 / 0.317 |
| Peer recusal + reasoned emergency docket | 0.506 / 0.600 / 0.616 | 0.488 / 0.659 / 0.690 | 0.601 / 0.641 / 0.648 | 0.057 / 0.077 / 0.171 | 0.350 / 0.386 / 0.593 | 0.186 / 0.211 / 0.331 |
| Judicial review with legislative supermajority override | 0.503 / 0.600 / 0.616 | 0.477 / 0.657 / 0.687 | 0.606 / 0.642 / 0.652 | 0.059 / 0.077 / 0.167 | 0.361 / 0.401 / 0.620 | 0.185 / 0.210 / 0.334 |
| Time-limited legislative override window | 0.504 / 0.600 / 0.616 | 0.476 / 0.657 / 0.687 | 0.602 / 0.640 / 0.650 | 0.056 / 0.076 / 0.169 | 0.362 / 0.398 / 0.620 | 0.186 / 0.206 / 0.331 |
| Constitutional remand before invalidation | 0.514 / 0.600 / 0.618 | 0.538 / 0.685 / 0.712 | 0.600 / 0.636 / 0.645 | 0.058 / 0.079 / 0.167 | 0.343 / 0.390 / 0.591 | 0.168 / 0.198 / 0.316 |
| Three-judge panels with en banc correction | 0.509 / 0.600 / 0.617 | 0.495 / 0.660 / 0.691 | 0.599 / 0.642 / 0.650 | 0.057 / 0.077 / 0.164 | 0.349 / 0.389 / 0.585 | 0.178 / 0.202 / 0.317 |
| Independent recusal enforcement with substitutes | 0.509 / 0.598 / 0.616 | 0.491 / 0.659 / 0.692 | 0.601 / 0.642 / 0.651 | 0.058 / 0.077 / 0.166 | 0.350 / 0.388 / 0.584 | 0.179 / 0.204 / 0.319 |
| Expanded 15-seat court | 0.502 / 0.598 / 0.614 | 0.488 / 0.662 / 0.687 | 0.600 / 0.640 / 0.652 | 0.055 / 0.077 / 0.169 | 0.348 / 0.386 / 0.599 | 0.184 / 0.209 / 0.335 |
| Randomized merits panels with en banc correction | 0.507 / 0.598 / 0.615 | 0.496 / 0.662 / 0.690 | 0.599 / 0.642 / 0.649 | 0.056 / 0.078 / 0.163 | 0.352 / 0.388 / 0.584 | 0.178 / 0.201 / 0.316 |
| Constitutional remand with override window | 0.512 / 0.597 / 0.614 | 0.548 / 0.686 / 0.707 | 0.596 / 0.637 / 0.645 | 0.033 / 0.051 / 0.126 | 0.348 / 0.388 / 0.586 | 0.171 / 0.197 / 0.314 |
| Random panels with jurisdiction safeguards | 0.504 / 0.597 / 0.613 | 0.504 / 0.663 / 0.689 | 0.588 / 0.635 / 0.646 | 0.049 / 0.069 / 0.155 | 0.358 / 0.396 / 0.603 | 0.178 / 0.199 / 0.322 |
| Pre-enactment constitutional council | 0.501 / 0.597 / 0.612 | 0.491 / 0.669 / 0.696 | 0.607 / 0.640 / 0.649 | 0.062 / 0.077 / 0.166 | 0.362 / 0.396 / 0.617 | 0.183 / 0.206 / 0.330 |
| Constitutional council with concrete-review backstop | 0.501 / 0.594 / 0.611 | 0.504 / 0.672 / 0.699 | 0.606 / 0.642 / 0.650 | 0.059 / 0.078 / 0.166 | 0.356 / 0.395 / 0.610 | 0.178 / 0.206 / 0.327 |
| Comparative 16-seat constitutional senates | 0.508 / 0.594 / 0.610 | 0.520 / 0.670 / 0.697 | 0.587 / 0.636 / 0.640 | 0.053 / 0.068 / 0.155 | 0.350 / 0.385 / 0.584 | 0.181 / 0.203 / 0.318 |
| Stylized current U.S.-like supreme court | 0.502 / 0.592 / 0.610 | 0.492 / 0.656 / 0.683 | 0.617 / 0.643 / 0.656 | 0.171 / 0.236 / 0.426 | 0.358 / 0.405 / 0.630 | 0.203 / 0.235 / 0.360 |
| Supreme court with cross-checking constitutional court | 0.495 / 0.585 / 0.600 | 0.527 / 0.662 / 0.686 | 0.567 / 0.621 / 0.635 | 0.050 / 0.068 / 0.157 | 0.371 / 0.408 / 0.618 | 0.180 / 0.200 / 0.318 |
| Dual supreme courts with disagreement filter | 0.474 / 0.575 / 0.594 | 0.461 / 0.640 / 0.673 | 0.595 / 0.641 / 0.648 | 0.048 / 0.073 / 0.155 | 0.376 / 0.417 / 0.623 | 0.183 / 0.209 / 0.328 |

## What Would Change the Interpretation

The table below reports each named prior's top directional-score cluster within 0.010 of that prior's best score. A design conclusion should weaken if it appears only under one narrow prior, if its cluster membership depends on high emergency pressure or high conflict, or if its apparent advantage comes with rights-protection, compliance, or emergency-power caveats.

| Prior | Cluster scenario | Score | Rights | Shadow | Emerg. downstream | Gov. noncomp. | Lower-court resistance | Caveat |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Baseline institutional prior | No emergency relief without merits review | 0.608 | 0.646 | 0.011 | 0.055 | 0.091 | 0.247 | front-line cluster |
| Baseline institutional prior | Jurisdiction stripping constrained by rights carveouts | 0.607 | 0.646 | 0.076 | 0.070 | 0.091 | 0.247 | front-line cluster |
| Baseline institutional prior | 18-year staggered terms + regular appointments | 0.606 | 0.646 | 0.076 | 0.072 | 0.093 | 0.248 | front-line cluster |
| Baseline institutional prior | Automatic merits follow-up for emergency relief | 0.606 | 0.650 | 0.016 | 0.062 | 0.090 | 0.246 | front-line cluster |
| Baseline institutional prior | 60 percent invalidation threshold | 0.605 | 0.635 | 0.070 | 0.080 | 0.089 | 0.250 | rights-protection caveat |
| Baseline institutional prior | Nonpartisan commission appointments | 0.604 | 0.647 | 0.074 | 0.070 | 0.082 | 0.248 | front-line cluster |
| Baseline institutional prior | Time-limited legislative override window | 0.604 | 0.641 | 0.073 | 0.069 | 0.074 | 0.247 | front-line cluster |
| Baseline institutional prior | Emergency integrity package | 0.603 | 0.656 | 0.018 | 0.067 | 0.092 | 0.245 | front-line cluster |
| Baseline institutional prior | Peer recusal + reasoned emergency docket | 0.603 | 0.642 | 0.076 | 0.070 | 0.079 | 0.248 | front-line cluster |
| Baseline institutional prior | Mandatory written emergency reasoning | 0.603 | 0.647 | 0.050 | 0.080 | 0.091 | 0.248 | front-line cluster |
| Baseline institutional prior | Randomized merits panels with en banc correction | 0.602 | 0.645 | 0.069 | 0.066 | 0.086 | 0.248 | front-line cluster |
| Baseline institutional prior | Expanded 15-seat court | 0.602 | 0.646 | 0.074 | 0.071 | 0.074 | 0.246 | front-line cluster |
| Baseline institutional prior | Retention-election accountability court | 0.601 | 0.645 | 0.076 | 0.069 | 0.101 | 0.249 | front-line cluster |
| Baseline institutional prior | Three-judge panels with en banc correction | 0.601 | 0.641 | 0.074 | 0.071 | 0.083 | 0.247 | front-line cluster |
| Baseline institutional prior | Public-interest litigation filter | 0.601 | 0.651 | 0.076 | 0.071 | 0.107 | 0.250 | front-line cluster |
| Baseline institutional prior | Constitutional remand before invalidation | 0.601 | 0.637 | 0.076 | 0.072 | 0.092 | 0.215 | rights-protection caveat |
| Baseline institutional prior | Independent recusal enforcement with substitutes | 0.601 | 0.647 | 0.074 | 0.070 | 0.091 | 0.248 | front-line cluster |
| Baseline institutional prior | Judicial review with legislative supermajority override | 0.601 | 0.648 | 0.072 | 0.068 | 0.093 | 0.249 | front-line cluster |
| Baseline institutional prior | Constitutional remand with override window | 0.599 | 0.639 | 0.048 | 0.077 | 0.092 | 0.215 | rights-protection caveat |
| Baseline institutional prior | Pre-enactment constitutional council | 0.598 | 0.644 | 0.076 | 0.071 | 0.089 | 0.246 | front-line cluster |
| Low-polarization prior | No emergency relief without merits review | 0.610 | 0.649 | 0.011 | 0.053 | 0.087 | 0.242 | front-line cluster |
| Low-polarization prior | 60 percent invalidation threshold | 0.608 | 0.627 | 0.060 | 0.071 | 0.092 | 0.246 | rights-protection caveat |
| Low-polarization prior | 18-year staggered terms + regular appointments | 0.607 | 0.647 | 0.071 | 0.065 | 0.097 | 0.245 | front-line cluster |
| Low-polarization prior | Constitutional remand before invalidation | 0.606 | 0.634 | 0.070 | 0.062 | 0.082 | 0.210 | rights-protection caveat |
| Low-polarization prior | Public-interest litigation filter | 0.606 | 0.642 | 0.069 | 0.064 | 0.085 | 0.243 | front-line cluster |
| Low-polarization prior | Jurisdiction stripping constrained by rights carveouts | 0.605 | 0.639 | 0.070 | 0.065 | 0.096 | 0.244 | front-line cluster |
| Low-polarization prior | Emergency integrity package | 0.605 | 0.644 | 0.016 | 0.056 | 0.071 | 0.240 | front-line cluster |
| Low-polarization prior | Mandatory written emergency reasoning | 0.604 | 0.638 | 0.040 | 0.068 | 0.077 | 0.243 | front-line cluster |
| Low-polarization prior | Nonpartisan commission appointments | 0.604 | 0.639 | 0.072 | 0.063 | 0.086 | 0.244 | front-line cluster |
| Low-polarization prior | Three-judge panels with en banc correction | 0.604 | 0.638 | 0.070 | 0.065 | 0.084 | 0.244 | front-line cluster |
| Low-polarization prior | Automatic merits follow-up for emergency relief | 0.603 | 0.642 | 0.016 | 0.057 | 0.085 | 0.242 | front-line cluster |
| Low-polarization prior | Randomized merits panels with en banc correction | 0.603 | 0.645 | 0.073 | 0.066 | 0.070 | 0.242 | front-line cluster |
| Low-polarization prior | Constitutional remand with override window | 0.603 | 0.632 | 0.047 | 0.074 | 0.073 | 0.208 | rights-protection caveat |
| Low-polarization prior | Retention-election accountability court | 0.603 | 0.637 | 0.070 | 0.065 | 0.095 | 0.244 | front-line cluster |
| Low-polarization prior | Judicial review with legislative supermajority override | 0.602 | 0.643 | 0.072 | 0.064 | 0.089 | 0.244 | front-line cluster |
| Low-polarization prior | Independent recusal enforcement with substitutes | 0.602 | 0.639 | 0.068 | 0.063 | 0.085 | 0.244 | front-line cluster |
| Low-polarization prior | Peer recusal + reasoned emergency docket | 0.602 | 0.636 | 0.073 | 0.065 | 0.096 | 0.246 | front-line cluster |
| Low-polarization prior | Time-limited legislative override window | 0.601 | 0.637 | 0.074 | 0.066 | 0.092 | 0.245 | front-line cluster |
| Low-polarization prior | Expanded 15-seat court | 0.601 | 0.640 | 0.073 | 0.065 | 0.090 | 0.244 | front-line cluster |
| Low-polarization prior | Random panels with jurisdiction safeguards | 0.600 | 0.636 | 0.064 | 0.075 | 0.086 | 0.244 | front-line cluster |
| High-polarization prior | No emergency relief without merits review | 0.605 | 0.645 | 0.012 | 0.062 | 0.088 | 0.263 | front-line cluster |
| High-polarization prior | 60 percent invalidation threshold | 0.601 | 0.634 | 0.071 | 0.089 | 0.091 | 0.266 | rights-protection caveat |
| High-polarization prior | Automatic merits follow-up for emergency relief | 0.600 | 0.647 | 0.019 | 0.072 | 0.090 | 0.263 | front-line cluster |
| High-polarization prior | Jurisdiction stripping constrained by rights carveouts | 0.600 | 0.641 | 0.081 | 0.078 | 0.095 | 0.265 | front-line cluster |
| High-polarization prior | Emergency integrity package | 0.600 | 0.645 | 0.018 | 0.068 | 0.091 | 0.263 | front-line cluster |
| High-polarization prior | 18-year staggered terms + regular appointments | 0.599 | 0.640 | 0.081 | 0.079 | 0.104 | 0.267 | front-line cluster |
| High-polarization prior | Retention-election accountability court | 0.599 | 0.634 | 0.077 | 0.075 | 0.094 | 0.266 | front-line cluster |
| High-polarization prior | Public-interest litigation filter | 0.599 | 0.643 | 0.079 | 0.077 | 0.080 | 0.265 | front-line cluster |
| High-polarization prior | Constitutional remand before invalidation | 0.598 | 0.641 | 0.081 | 0.078 | 0.089 | 0.231 | administrative-cost caveat |
| High-polarization prior | Peer recusal + reasoned emergency docket | 0.598 | 0.640 | 0.078 | 0.077 | 0.084 | 0.265 | front-line cluster |
| High-polarization prior | Mandatory written emergency reasoning | 0.597 | 0.637 | 0.052 | 0.084 | 0.090 | 0.267 | front-line cluster |
| High-polarization prior | Nonpartisan commission appointments | 0.597 | 0.643 | 0.080 | 0.078 | 0.109 | 0.268 | front-line cluster |
| High-polarization prior | Time-limited legislative override window | 0.597 | 0.638 | 0.078 | 0.075 | 0.089 | 0.266 | front-line cluster |
| High-polarization prior | Randomized merits panels with en banc correction | 0.596 | 0.645 | 0.078 | 0.080 | 0.086 | 0.264 | front-line cluster |
| High-polarization prior | Constitutional remand with override window | 0.596 | 0.637 | 0.052 | 0.088 | 0.083 | 0.231 | rights-protection caveat |
| High-polarization prior | Expanded 15-seat court | 0.596 | 0.641 | 0.079 | 0.078 | 0.092 | 0.266 | front-line cluster |
| High-polarization prior | Three-judge panels with en banc correction | 0.596 | 0.644 | 0.082 | 0.079 | 0.102 | 0.267 | front-line cluster |
| High-polarization prior | Independent recusal enforcement with substitutes | 0.596 | 0.642 | 0.078 | 0.076 | 0.091 | 0.266 | front-line cluster |
| High-polarization prior | Judicial review with legislative supermajority override | 0.595 | 0.640 | 0.082 | 0.078 | 0.101 | 0.267 | front-line cluster |
| Low appointment-capture prior | No emergency relief without merits review | 0.612 | 0.647 | 0.010 | 0.051 | 0.089 | 0.239 | front-line cluster |
| Low appointment-capture prior | 60 percent invalidation threshold | 0.610 | 0.634 | 0.062 | 0.071 | 0.082 | 0.241 | rights-protection caveat |
| Low appointment-capture prior | Jurisdiction stripping constrained by rights carveouts | 0.609 | 0.646 | 0.070 | 0.062 | 0.094 | 0.240 | front-line cluster |
| Low appointment-capture prior | Automatic merits follow-up for emergency relief | 0.608 | 0.646 | 0.016 | 0.058 | 0.085 | 0.238 | front-line cluster |
| Low appointment-capture prior | Constitutional remand before invalidation | 0.607 | 0.633 | 0.069 | 0.062 | 0.083 | 0.207 | rights-protection caveat |
| Low appointment-capture prior | Nonpartisan commission appointments | 0.607 | 0.644 | 0.068 | 0.061 | 0.079 | 0.240 | front-line cluster |
| Low appointment-capture prior | Public-interest litigation filter | 0.607 | 0.650 | 0.071 | 0.063 | 0.083 | 0.240 | front-line cluster |
| Low appointment-capture prior | Emergency integrity package | 0.606 | 0.644 | 0.016 | 0.057 | 0.073 | 0.237 | front-line cluster |
| Low appointment-capture prior | 18-year staggered terms + regular appointments | 0.606 | 0.642 | 0.072 | 0.064 | 0.097 | 0.242 | front-line cluster |
| Low appointment-capture prior | Retention-election accountability court | 0.606 | 0.634 | 0.067 | 0.060 | 0.090 | 0.241 | front-line cluster |
| Low appointment-capture prior | Mandatory written emergency reasoning | 0.606 | 0.638 | 0.044 | 0.071 | 0.081 | 0.240 | front-line cluster |
| Low appointment-capture prior | Randomized merits panels with en banc correction | 0.605 | 0.635 | 0.070 | 0.062 | 0.072 | 0.239 | front-line cluster |
| Low appointment-capture prior | Three-judge panels with en banc correction | 0.604 | 0.634 | 0.073 | 0.064 | 0.079 | 0.241 | front-line cluster |
| Low appointment-capture prior | Judicial review with legislative supermajority override | 0.603 | 0.640 | 0.073 | 0.064 | 0.082 | 0.241 | front-line cluster |
| Low appointment-capture prior | Expanded 15-seat court | 0.603 | 0.637 | 0.070 | 0.062 | 0.082 | 0.241 | front-line cluster |
| Low appointment-capture prior | Constitutional remand with override window | 0.603 | 0.638 | 0.043 | 0.068 | 0.087 | 0.208 | administrative-cost caveat |
| Low appointment-capture prior | Time-limited legislative override window | 0.603 | 0.646 | 0.072 | 0.062 | 0.094 | 0.242 | front-line cluster |
| Low appointment-capture prior | Independent recusal enforcement with substitutes | 0.603 | 0.634 | 0.073 | 0.062 | 0.086 | 0.242 | front-line cluster |
| Low appointment-capture prior | Peer recusal + reasoned emergency docket | 0.603 | 0.636 | 0.072 | 0.064 | 0.100 | 0.243 | front-line cluster |
| High appointment-capture prior | No emergency relief without merits review | 0.606 | 0.651 | 0.012 | 0.062 | 0.095 | 0.261 | front-line cluster |
| High appointment-capture prior | 60 percent invalidation threshold | 0.606 | 0.634 | 0.073 | 0.087 | 0.075 | 0.263 | rights-protection caveat |
| High appointment-capture prior | 18-year staggered terms + regular appointments | 0.603 | 0.644 | 0.081 | 0.077 | 0.078 | 0.263 | front-line cluster |
| High appointment-capture prior | Jurisdiction stripping constrained by rights carveouts | 0.603 | 0.641 | 0.080 | 0.075 | 0.100 | 0.263 | front-line cluster |
| High appointment-capture prior | Automatic merits follow-up for emergency relief | 0.601 | 0.645 | 0.018 | 0.068 | 0.085 | 0.261 | front-line cluster |
| High appointment-capture prior | Nonpartisan commission appointments | 0.601 | 0.640 | 0.079 | 0.076 | 0.090 | 0.264 | front-line cluster |
| High appointment-capture prior | Public-interest litigation filter | 0.601 | 0.643 | 0.075 | 0.076 | 0.092 | 0.264 | front-line cluster |
| High appointment-capture prior | Retention-election accountability court | 0.601 | 0.641 | 0.080 | 0.076 | 0.085 | 0.263 | front-line cluster |
| High appointment-capture prior | Mandatory written emergency reasoning | 0.600 | 0.640 | 0.051 | 0.084 | 0.095 | 0.264 | front-line cluster |
| High appointment-capture prior | Emergency integrity package | 0.599 | 0.648 | 0.019 | 0.074 | 0.092 | 0.261 | front-line cluster |
| High appointment-capture prior | Time-limited legislative override window | 0.599 | 0.643 | 0.081 | 0.078 | 0.095 | 0.264 | front-line cluster |
| High appointment-capture prior | Three-judge panels with en banc correction | 0.599 | 0.643 | 0.079 | 0.077 | 0.096 | 0.264 | front-line cluster |
| High appointment-capture prior | Peer recusal + reasoned emergency docket | 0.598 | 0.649 | 0.079 | 0.078 | 0.098 | 0.263 | front-line cluster |
| High appointment-capture prior | Constitutional remand before invalidation | 0.597 | 0.643 | 0.082 | 0.078 | 0.098 | 0.230 | rights-protection caveat |
| High appointment-capture prior | Judicial review with legislative supermajority override | 0.597 | 0.645 | 0.080 | 0.078 | 0.101 | 0.264 | front-line cluster |
| High appointment-capture prior | Randomized merits panels with en banc correction | 0.596 | 0.638 | 0.081 | 0.077 | 0.086 | 0.264 | rights-protection caveat |
| High appointment-capture prior | Expanded 15-seat court | 0.596 | 0.638 | 0.083 | 0.078 | 0.085 | 0.264 | rights-protection caveat |
| High appointment-capture prior | Random panels with jurisdiction safeguards | 0.596 | 0.633 | 0.068 | 0.086 | 0.086 | 0.263 | rights-protection caveat |
| High appointment-capture prior | Independent recusal enforcement with substitutes | 0.596 | 0.646 | 0.084 | 0.080 | 0.094 | 0.264 | front-line cluster |
| High appointment-capture prior | Constitutional remand with override window | 0.596 | 0.639 | 0.052 | 0.086 | 0.090 | 0.228 | rights-protection caveat |
| Low public-pressure prior | No emergency relief without merits review | 0.609 | 0.650 | 0.010 | 0.056 | 0.092 | 0.249 | front-line cluster |
| Low public-pressure prior | 18-year staggered terms + regular appointments | 0.607 | 0.642 | 0.077 | 0.071 | 0.088 | 0.251 | front-line cluster |
| Low public-pressure prior | Public-interest litigation filter | 0.607 | 0.653 | 0.075 | 0.068 | 0.076 | 0.248 | front-line cluster |
| Low public-pressure prior | Jurisdiction stripping constrained by rights carveouts | 0.607 | 0.644 | 0.075 | 0.070 | 0.090 | 0.249 | front-line cluster |
| Low public-pressure prior | 60 percent invalidation threshold | 0.606 | 0.639 | 0.071 | 0.082 | 0.091 | 0.253 | rights-protection caveat |
| Low public-pressure prior | Automatic merits follow-up for emergency relief | 0.605 | 0.651 | 0.017 | 0.065 | 0.091 | 0.248 | front-line cluster |
| Low public-pressure prior | Nonpartisan commission appointments | 0.605 | 0.642 | 0.073 | 0.069 | 0.085 | 0.250 | front-line cluster |
| Low public-pressure prior | Mandatory written emergency reasoning | 0.604 | 0.643 | 0.045 | 0.077 | 0.080 | 0.250 | front-line cluster |
| Low public-pressure prior | Peer recusal + reasoned emergency docket | 0.603 | 0.644 | 0.071 | 0.068 | 0.085 | 0.251 | front-line cluster |
| Low public-pressure prior | Retention-election accountability court | 0.603 | 0.639 | 0.074 | 0.068 | 0.101 | 0.252 | rights-protection caveat |
| Low public-pressure prior | Time-limited legislative override window | 0.602 | 0.639 | 0.073 | 0.068 | 0.085 | 0.251 | rights-protection caveat |
| Low public-pressure prior | Constitutional remand before invalidation | 0.602 | 0.645 | 0.076 | 0.072 | 0.094 | 0.217 | rights-protection caveat |
| Low public-pressure prior | Emergency integrity package | 0.602 | 0.652 | 0.017 | 0.066 | 0.095 | 0.249 | front-line cluster |
| Low public-pressure prior | Three-judge panels with en banc correction | 0.601 | 0.645 | 0.074 | 0.071 | 0.089 | 0.250 | front-line cluster |
| Low public-pressure prior | Judicial review with legislative supermajority override | 0.601 | 0.644 | 0.075 | 0.069 | 0.092 | 0.251 | front-line cluster |
| High public-pressure prior | No emergency relief without merits review | 0.608 | 0.649 | 0.013 | 0.064 | 0.093 | 0.251 | front-line cluster |
| High public-pressure prior | Jurisdiction stripping constrained by rights carveouts | 0.604 | 0.646 | 0.081 | 0.079 | 0.099 | 0.253 | front-line cluster |
| High public-pressure prior | 18-year staggered terms + regular appointments | 0.604 | 0.648 | 0.080 | 0.079 | 0.098 | 0.254 | front-line cluster |
| High public-pressure prior | 60 percent invalidation threshold | 0.603 | 0.635 | 0.073 | 0.090 | 0.088 | 0.255 | rights-protection caveat |
| High public-pressure prior | Automatic merits follow-up for emergency relief | 0.602 | 0.655 | 0.020 | 0.077 | 0.092 | 0.251 | front-line cluster |
| High public-pressure prior | Public-interest litigation filter | 0.602 | 0.647 | 0.081 | 0.079 | 0.085 | 0.253 | front-line cluster |
| High public-pressure prior | Emergency integrity package | 0.600 | 0.658 | 0.020 | 0.076 | 0.088 | 0.249 | front-line cluster |
| High public-pressure prior | Judicial review with legislative supermajority override | 0.600 | 0.645 | 0.084 | 0.081 | 0.097 | 0.254 | front-line cluster |
| High public-pressure prior | Mandatory written emergency reasoning | 0.599 | 0.639 | 0.052 | 0.089 | 0.098 | 0.254 | rights-protection caveat |
| High public-pressure prior | Constitutional remand before invalidation | 0.599 | 0.636 | 0.085 | 0.082 | 0.088 | 0.219 | rights-protection caveat |
| High public-pressure prior | Peer recusal + reasoned emergency docket | 0.599 | 0.646 | 0.081 | 0.078 | 0.104 | 0.255 | front-line cluster |
| High public-pressure prior | Nonpartisan commission appointments | 0.599 | 0.643 | 0.087 | 0.082 | 0.099 | 0.255 | rights-protection caveat |
| High public-pressure prior | Retention-election accountability court | 0.598 | 0.642 | 0.085 | 0.083 | 0.100 | 0.254 | front-line cluster |
| High public-pressure prior | Independent recusal enforcement with substitutes | 0.598 | 0.644 | 0.080 | 0.079 | 0.090 | 0.254 | front-line cluster |
| Low emergency-share prior | No emergency relief without merits review | 0.616 | 0.646 | 0.009 | 0.037 | 0.063 | 0.240 | front-line cluster |
| Low emergency-share prior | 60 percent invalidation threshold | 0.611 | 0.634 | 0.053 | 0.056 | 0.085 | 0.245 | rights-protection caveat |
| Low emergency-share prior | 18-year staggered terms + regular appointments | 0.611 | 0.643 | 0.061 | 0.050 | 0.085 | 0.244 | front-line cluster |
| Low emergency-share prior | Public-interest litigation filter | 0.610 | 0.646 | 0.058 | 0.049 | 0.080 | 0.243 | front-line cluster |
| Low emergency-share prior | Nonpartisan commission appointments | 0.610 | 0.641 | 0.064 | 0.050 | 0.077 | 0.243 | front-line cluster |
| Low emergency-share prior | Jurisdiction stripping constrained by rights carveouts | 0.610 | 0.639 | 0.059 | 0.050 | 0.086 | 0.243 | front-line cluster |
| Low emergency-share prior | Automatic merits follow-up for emergency relief | 0.609 | 0.644 | 0.014 | 0.044 | 0.078 | 0.242 | front-line cluster |
| Low emergency-share prior | Mandatory written emergency reasoning | 0.609 | 0.633 | 0.034 | 0.053 | 0.068 | 0.243 | rights-protection caveat |
| Low emergency-share prior | Constitutional remand before invalidation | 0.609 | 0.636 | 0.062 | 0.050 | 0.073 | 0.209 | rights-protection caveat |
| Low emergency-share prior | Emergency integrity package | 0.608 | 0.651 | 0.014 | 0.044 | 0.078 | 0.240 | front-line cluster |
| Low emergency-share prior | Peer recusal + reasoned emergency docket | 0.608 | 0.644 | 0.060 | 0.048 | 0.085 | 0.244 | front-line cluster |
| Low emergency-share prior | Retention-election accountability court | 0.608 | 0.638 | 0.061 | 0.050 | 0.088 | 0.244 | front-line cluster |
| Low emergency-share prior | Constitutional remand with override window | 0.607 | 0.641 | 0.035 | 0.055 | 0.078 | 0.209 | rights-protection caveat |
| Low emergency-share prior | Three-judge panels with en banc correction | 0.607 | 0.644 | 0.059 | 0.050 | 0.084 | 0.244 | front-line cluster |
| Low emergency-share prior | Randomized merits panels with en banc correction | 0.607 | 0.645 | 0.056 | 0.048 | 0.074 | 0.243 | front-line cluster |
| Low emergency-share prior | Expanded 15-seat court | 0.607 | 0.641 | 0.058 | 0.049 | 0.073 | 0.243 | front-line cluster |
| High emergency-share prior | 60 percent invalidation threshold | 0.520 | 0.614 | 0.179 | 0.260 | 0.216 | 0.404 | compliance caveat |
| High emergency-share prior | Public-interest litigation filter | 0.519 | 0.629 | 0.178 | 0.219 | 0.216 | 0.401 | compliance caveat |
| High emergency-share prior | Constitutional remand before invalidation | 0.517 | 0.626 | 0.187 | 0.230 | 0.228 | 0.365 | compliance caveat |
| High emergency-share prior | 18-year staggered terms + regular appointments | 0.516 | 0.625 | 0.188 | 0.229 | 0.229 | 0.402 | compliance caveat |
| High emergency-share prior | No emergency relief without merits review | 0.516 | 0.647 | 0.049 | 0.182 | 0.222 | 0.394 | compliance caveat |
| High emergency-share prior | Constitutional remand with override window | 0.515 | 0.619 | 0.141 | 0.252 | 0.232 | 0.368 | compliance caveat |
| High emergency-share prior | Retention-election accountability court | 0.515 | 0.614 | 0.180 | 0.221 | 0.224 | 0.402 | compliance caveat |
| High emergency-share prior | Jurisdiction stripping constrained by rights carveouts | 0.515 | 0.629 | 0.189 | 0.231 | 0.241 | 0.402 | compliance caveat |
| High emergency-share prior | Independent recusal enforcement with substitutes | 0.514 | 0.625 | 0.187 | 0.226 | 0.205 | 0.400 | compliance caveat |
| High emergency-share prior | Three-judge panels with en banc correction | 0.514 | 0.628 | 0.185 | 0.230 | 0.221 | 0.401 | compliance caveat |
| High emergency-share prior | Mandatory written emergency reasoning | 0.513 | 0.611 | 0.144 | 0.253 | 0.223 | 0.404 | compliance caveat |
| High emergency-share prior | Nonpartisan commission appointments | 0.513 | 0.627 | 0.187 | 0.228 | 0.219 | 0.401 | compliance caveat |
| High emergency-share prior | Comparative 16-seat constitutional senates | 0.512 | 0.610 | 0.176 | 0.254 | 0.216 | 0.405 | rights-protection caveat |
| High emergency-share prior | Time-limited legislative override window | 0.511 | 0.625 | 0.185 | 0.226 | 0.236 | 0.403 | compliance caveat |
| High emergency-share prior | Peer recusal + reasoned emergency docket | 0.511 | 0.630 | 0.190 | 0.230 | 0.241 | 0.404 | compliance caveat |
| High emergency-share prior | Randomized merits panels with en banc correction | 0.510 | 0.623 | 0.184 | 0.227 | 0.248 | 0.405 | compliance caveat |
| Low rights-risk prior | No emergency relief without merits review | 0.637 | 0.653 | 0.005 | 0.039 | 0.051 | 0.176 | rights-protection caveat |
| Low rights-risk prior | Jurisdiction stripping constrained by rights carveouts | 0.636 | 0.647 | 0.052 | 0.042 | 0.040 | 0.176 | rights-protection caveat |
| Low rights-risk prior | 60 percent invalidation threshold | 0.636 | 0.646 | 0.044 | 0.049 | 0.036 | 0.178 | rights-protection caveat |
| Low rights-risk prior | 18-year staggered terms + regular appointments | 0.634 | 0.648 | 0.053 | 0.044 | 0.052 | 0.180 | rights-protection caveat |
| Low rights-risk prior | Automatic merits follow-up for emergency relief | 0.633 | 0.651 | 0.009 | 0.048 | 0.041 | 0.176 | rights-protection caveat |
| Low rights-risk prior | Nonpartisan commission appointments | 0.632 | 0.652 | 0.057 | 0.047 | 0.049 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Mandatory written emergency reasoning | 0.632 | 0.647 | 0.031 | 0.048 | 0.043 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Retention-election accountability court | 0.631 | 0.644 | 0.054 | 0.045 | 0.049 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Peer recusal + reasoned emergency docket | 0.631 | 0.648 | 0.052 | 0.044 | 0.046 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Three-judge panels with en banc correction | 0.631 | 0.653 | 0.054 | 0.045 | 0.049 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Emergency integrity package | 0.631 | 0.648 | 0.010 | 0.047 | 0.042 | 0.176 | rights-protection caveat |
| Low rights-risk prior | Judicial review with legislative supermajority override | 0.631 | 0.655 | 0.054 | 0.046 | 0.043 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Constitutional remand before invalidation | 0.631 | 0.642 | 0.051 | 0.043 | 0.041 | 0.146 | rights-protection caveat |
| Low rights-risk prior | Time-limited legislative override window | 0.631 | 0.649 | 0.057 | 0.047 | 0.044 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Independent recusal enforcement with substitutes | 0.630 | 0.651 | 0.052 | 0.046 | 0.044 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Public-interest litigation filter | 0.630 | 0.650 | 0.056 | 0.046 | 0.052 | 0.179 | rights-protection caveat |
| Low rights-risk prior | Randomized merits panels with en banc correction | 0.630 | 0.649 | 0.055 | 0.045 | 0.052 | 0.179 | rights-protection caveat |
| Low rights-risk prior | Expanded 15-seat court | 0.628 | 0.653 | 0.051 | 0.044 | 0.049 | 0.179 | rights-protection caveat |
| Low rights-risk prior | Random panels with jurisdiction safeguards | 0.628 | 0.646 | 0.045 | 0.050 | 0.054 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Pre-enactment constitutional council | 0.627 | 0.648 | 0.057 | 0.046 | 0.050 | 0.177 | rights-protection caveat |
| High rights-risk prior | 60 percent invalidation threshold | 0.529 | 0.559 | 0.115 | 0.161 | 0.204 | 0.402 | compliance caveat |
| High rights-risk prior | Constitutional remand before invalidation | 0.527 | 0.567 | 0.119 | 0.133 | 0.216 | 0.363 | compliance caveat |
| High rights-risk prior | No emergency relief without merits review | 0.526 | 0.603 | 0.027 | 0.098 | 0.226 | 0.397 | compliance caveat |
| High rights-risk prior | 18-year staggered terms + regular appointments | 0.524 | 0.573 | 0.122 | 0.136 | 0.219 | 0.402 | compliance caveat |
| High rights-risk prior | Automatic merits follow-up for emergency relief | 0.524 | 0.600 | 0.035 | 0.082 | 0.230 | 0.398 | compliance caveat |
| High rights-risk prior | Constitutional remand with override window | 0.522 | 0.564 | 0.093 | 0.162 | 0.222 | 0.364 | compliance caveat |
| High rights-risk prior | Peer recusal + reasoned emergency docket | 0.521 | 0.577 | 0.119 | 0.134 | 0.221 | 0.402 | compliance caveat |
| High rights-risk prior | Public-interest litigation filter | 0.521 | 0.580 | 0.120 | 0.135 | 0.207 | 0.400 | compliance caveat |
| High rights-risk prior | Randomized merits panels with en banc correction | 0.521 | 0.575 | 0.121 | 0.134 | 0.194 | 0.399 | compliance caveat |
| High rights-risk prior | Emergency integrity package | 0.520 | 0.607 | 0.035 | 0.081 | 0.245 | 0.400 | compliance caveat |
| High rights-risk prior | Expanded 15-seat court | 0.520 | 0.572 | 0.119 | 0.132 | 0.207 | 0.400 | compliance caveat |
| High rights-risk prior | Stylized current U.S.-like supreme court | 0.520 | 0.593 | 0.347 | 0.223 | 0.245 | 0.412 | compliance caveat |
| High rights-risk prior | Mandatory written emergency reasoning | 0.519 | 0.565 | 0.091 | 0.161 | 0.222 | 0.403 | compliance caveat |
| High rights-risk prior | Independent recusal enforcement with substitutes | 0.519 | 0.580 | 0.121 | 0.137 | 0.214 | 0.401 | compliance caveat |
| High rights-risk prior | Three-judge panels with en banc correction | 0.519 | 0.575 | 0.121 | 0.136 | 0.216 | 0.401 | compliance caveat |
| Weak democratic-mandate prior | 60 percent invalidation threshold | 0.543 | 0.607 | 0.097 | 0.131 | 0.183 | 0.377 | compliance caveat |
| Weak democratic-mandate prior | Constitutional remand before invalidation | 0.540 | 0.617 | 0.108 | 0.112 | 0.179 | 0.338 | compliance caveat |
| Weak democratic-mandate prior | Constitutional remand with override window | 0.537 | 0.616 | 0.075 | 0.128 | 0.198 | 0.340 | compliance caveat |
| Weak democratic-mandate prior | Public-interest litigation filter | 0.536 | 0.619 | 0.100 | 0.108 | 0.191 | 0.376 | compliance caveat |
| Weak democratic-mandate prior | No emergency relief without merits review | 0.536 | 0.622 | 0.020 | 0.084 | 0.192 | 0.373 | compliance caveat |
| Weak democratic-mandate prior | 18-year staggered terms + regular appointments | 0.536 | 0.616 | 0.110 | 0.113 | 0.193 | 0.377 | compliance caveat |
| Weak democratic-mandate prior | Mandatory written emergency reasoning | 0.535 | 0.613 | 0.078 | 0.128 | 0.172 | 0.375 | compliance caveat |
| Weak democratic-mandate prior | Comparative 16-seat constitutional senates | 0.535 | 0.611 | 0.098 | 0.130 | 0.180 | 0.377 | compliance caveat |
| Weak democratic-mandate prior | Expanded 15-seat court | 0.534 | 0.615 | 0.103 | 0.109 | 0.178 | 0.375 | compliance caveat |
| Weak democratic-mandate prior | Peer recusal + reasoned emergency docket | 0.533 | 0.615 | 0.105 | 0.111 | 0.194 | 0.377 | compliance caveat |
| High constitutional-conflict prior | 60 percent invalidation threshold | 0.517 | 0.605 | 0.139 | 0.188 | 0.213 | 0.435 | compliance caveat |
| Imported legislative-family prior | No emergency relief without merits review | 0.618 | 0.653 | 0.008 | 0.052 | 0.076 | 0.231 | front-line cluster |
| Imported legislative-family prior | 18-year staggered terms + regular appointments | 0.614 | 0.645 | 0.068 | 0.065 | 0.072 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | 60 percent invalidation threshold | 0.612 | 0.642 | 0.063 | 0.077 | 0.074 | 0.235 | rights-protection caveat |
| Imported legislative-family prior | Jurisdiction stripping constrained by rights carveouts | 0.612 | 0.650 | 0.077 | 0.071 | 0.077 | 0.232 | rights-protection caveat |
| Imported legislative-family prior | Automatic merits follow-up for emergency relief | 0.612 | 0.654 | 0.015 | 0.067 | 0.072 | 0.231 | front-line cluster |
| Imported legislative-family prior | Constitutional remand before invalidation | 0.610 | 0.645 | 0.075 | 0.067 | 0.065 | 0.198 | rights-protection caveat |
| Imported legislative-family prior | Emergency integrity package | 0.610 | 0.662 | 0.016 | 0.067 | 0.082 | 0.230 | front-line cluster |
| Imported legislative-family prior | Three-judge panels with en banc correction | 0.610 | 0.648 | 0.070 | 0.066 | 0.073 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Public-interest litigation filter | 0.610 | 0.650 | 0.072 | 0.070 | 0.079 | 0.234 | rights-protection caveat |
| Imported legislative-family prior | Retention-election accountability court | 0.610 | 0.644 | 0.073 | 0.066 | 0.076 | 0.234 | rights-protection caveat |
| Imported legislative-family prior | Mandatory written emergency reasoning | 0.610 | 0.649 | 0.044 | 0.074 | 0.080 | 0.234 | rights-protection caveat |
| Imported legislative-family prior | Judicial review with legislative supermajority override | 0.609 | 0.651 | 0.073 | 0.069 | 0.078 | 0.234 | rights-protection caveat |
| Imported legislative-family prior | Nonpartisan commission appointments | 0.609 | 0.648 | 0.077 | 0.069 | 0.091 | 0.236 | rights-protection caveat |
