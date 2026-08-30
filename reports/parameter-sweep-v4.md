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
| No emergency relief without merits review | 0.512 / 0.609 / 0.625 | 0.459 / 0.661 / 0.693 | 0.615 / 0.645 / 0.651 | 0.007 / 0.011 / 0.043 | 0.342 / 0.376 / 0.594 | 0.168 / 0.190 / 0.315 |
| 18-year staggered terms + regular appointments | 0.514 / 0.606 / 0.621 | 0.494 / 0.660 / 0.691 | 0.596 / 0.637 / 0.645 | 0.059 / 0.078 / 0.159 | 0.339 / 0.382 / 0.588 | 0.184 / 0.208 / 0.327 |
| 60 percent invalidation threshold | 0.515 / 0.605 / 0.622 | 0.523 / 0.667 / 0.693 | 0.584 / 0.630 / 0.639 | 0.049 / 0.069 / 0.154 | 0.342 / 0.383 / 0.594 | 0.182 / 0.206 / 0.326 |
| Jurisdiction stripping constrained by rights carveouts | 0.510 / 0.605 / 0.622 | 0.481 / 0.660 / 0.688 | 0.600 / 0.639 / 0.644 | 0.055 / 0.075 / 0.164 | 0.345 / 0.390 / 0.610 | 0.170 / 0.200 / 0.332 |
| Automatic merits follow-up for emergency relief | 0.503 / 0.604 / 0.619 | 0.456 / 0.657 / 0.689 | 0.611 / 0.643 / 0.651 | 0.012 / 0.017 / 0.053 | 0.340 / 0.376 / 0.596 | 0.179 / 0.202 / 0.327 |
| Emergency integrity package | 0.507 / 0.603 / 0.618 | 0.461 / 0.662 / 0.693 | 0.613 / 0.645 / 0.651 | 0.012 / 0.018 / 0.053 | 0.341 / 0.382 / 0.588 | 0.167 / 0.193 / 0.315 |
| Nonpartisan commission appointments | 0.509 / 0.603 / 0.619 | 0.487 / 0.660 / 0.692 | 0.599 / 0.639 / 0.645 | 0.059 / 0.076 / 0.165 | 0.342 / 0.381 / 0.596 | 0.175 / 0.199 / 0.322 |
| Public-interest litigation filter | 0.513 / 0.603 / 0.618 | 0.500 / 0.663 / 0.692 | 0.604 / 0.645 / 0.648 | 0.058 / 0.077 / 0.163 | 0.342 / 0.383 / 0.590 | 0.170 / 0.195 / 0.312 |
| Peer recusal + reasoned emergency docket | 0.508 / 0.602 / 0.618 | 0.493 / 0.663 / 0.693 | 0.596 / 0.635 / 0.646 | 0.059 / 0.075 / 0.163 | 0.344 / 0.382 / 0.595 | 0.183 / 0.208 / 0.329 |
| Three-judge panels with en banc correction | 0.508 / 0.602 / 0.617 | 0.497 / 0.662 / 0.691 | 0.596 / 0.635 / 0.647 | 0.057 / 0.078 / 0.167 | 0.341 / 0.382 / 0.596 | 0.171 / 0.198 / 0.320 |
| Mandatory written emergency reasoning | 0.508 / 0.602 / 0.618 | 0.501 / 0.664 / 0.692 | 0.593 / 0.636 / 0.645 | 0.033 / 0.049 / 0.123 | 0.339 / 0.385 / 0.594 | 0.178 / 0.207 / 0.327 |
| Constitutional remand before invalidation | 0.514 / 0.601 / 0.617 | 0.541 / 0.683 / 0.707 | 0.598 / 0.635 / 0.642 | 0.057 / 0.078 / 0.166 | 0.341 / 0.380 / 0.593 | 0.170 / 0.193 / 0.314 |
| Time-limited legislative override window | 0.505 / 0.601 / 0.617 | 0.484 / 0.657 / 0.688 | 0.599 / 0.637 / 0.645 | 0.057 / 0.077 / 0.163 | 0.355 / 0.394 / 0.619 | 0.181 / 0.204 / 0.331 |
| Expanded 15-seat court | 0.505 / 0.600 / 0.616 | 0.494 / 0.661 / 0.690 | 0.597 / 0.638 / 0.649 | 0.056 / 0.075 / 0.163 | 0.340 / 0.382 / 0.597 | 0.179 / 0.207 / 0.332 |
| Retention-election accountability court | 0.509 / 0.600 / 0.617 | 0.493 / 0.663 / 0.691 | 0.582 / 0.632 / 0.638 | 0.056 / 0.078 / 0.157 | 0.348 / 0.393 / 0.609 | 0.177 / 0.203 / 0.322 |
| Constitutional remand with override window | 0.511 / 0.599 / 0.614 | 0.549 / 0.686 / 0.706 | 0.590 / 0.634 / 0.642 | 0.033 / 0.051 / 0.126 | 0.342 / 0.381 / 0.591 | 0.169 / 0.194 / 0.314 |
| Independent recusal enforcement with substitutes | 0.509 / 0.598 / 0.615 | 0.492 / 0.661 / 0.691 | 0.595 / 0.638 / 0.645 | 0.057 / 0.078 / 0.163 | 0.344 / 0.384 / 0.591 | 0.177 / 0.203 / 0.320 |
| Judicial review with legislative supermajority override | 0.504 / 0.598 / 0.616 | 0.477 / 0.656 / 0.687 | 0.601 / 0.638 / 0.647 | 0.055 / 0.076 / 0.164 | 0.352 / 0.396 / 0.624 | 0.182 / 0.211 / 0.337 |
| Randomized merits panels with en banc correction | 0.507 / 0.598 / 0.617 | 0.499 / 0.662 / 0.693 | 0.596 / 0.635 / 0.649 | 0.057 / 0.078 / 0.160 | 0.344 / 0.383 / 0.590 | 0.175 / 0.198 / 0.317 |
| Pre-enactment constitutional council | 0.504 / 0.598 / 0.613 | 0.495 / 0.670 / 0.697 | 0.604 / 0.639 / 0.644 | 0.058 / 0.077 / 0.161 | 0.352 / 0.392 / 0.615 | 0.177 / 0.203 / 0.327 |
| Random panels with jurisdiction safeguards | 0.503 / 0.598 / 0.613 | 0.506 / 0.664 / 0.691 | 0.585 / 0.631 / 0.639 | 0.050 / 0.071 / 0.155 | 0.349 / 0.390 / 0.608 | 0.175 / 0.197 / 0.323 |
| Comparative 16-seat constitutional senates | 0.509 / 0.595 / 0.611 | 0.526 / 0.671 / 0.697 | 0.582 / 0.628 / 0.638 | 0.051 / 0.067 / 0.150 | 0.342 / 0.380 / 0.587 | 0.174 / 0.199 / 0.318 |
| Constitutional council with concrete-review backstop | 0.500 / 0.595 / 0.610 | 0.501 / 0.671 / 0.697 | 0.603 / 0.638 / 0.643 | 0.057 / 0.076 / 0.164 | 0.348 / 0.391 / 0.616 | 0.176 / 0.204 / 0.329 |
| Judicial electorate selection court | 0.500 / 0.595 / 0.612 | 0.490 / 0.662 / 0.694 | 0.600 / 0.639 / 0.646 | 0.057 / 0.078 / 0.162 | 0.342 / 0.386 / 0.596 | 0.170 / 0.195 / 0.319 |
| Stylized current U.S.-like supreme court | 0.498 / 0.590 / 0.609 | 0.494 / 0.656 / 0.680 | 0.611 / 0.640 / 0.651 | 0.177 / 0.238 / 0.423 | 0.361 / 0.410 / 0.644 | 0.202 / 0.235 / 0.366 |
| Supreme court with cross-checking constitutional court | 0.495 / 0.586 / 0.602 | 0.528 / 0.661 / 0.688 | 0.564 / 0.619 / 0.630 | 0.051 / 0.069 / 0.153 | 0.364 / 0.401 / 0.621 | 0.175 / 0.199 / 0.319 |
| Dual supreme courts with disagreement filter | 0.474 / 0.576 / 0.595 | 0.467 / 0.639 / 0.676 | 0.595 / 0.637 / 0.644 | 0.051 / 0.070 / 0.154 | 0.371 / 0.413 / 0.628 | 0.180 / 0.207 / 0.329 |

## What Would Change the Interpretation

The table below reports each named prior's top directional-score cluster within 0.010 of that prior's best score. A design conclusion should weaken if it appears only under one narrow prior, if its cluster membership depends on high emergency pressure or high conflict, or if its apparent advantage comes with rights-protection, compliance, or emergency-power caveats.

| Prior | Cluster scenario | Score | Rights | Shadow | Emerg. downstream | Gov. noncomp. | Lower-court resistance | Caveat |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Baseline institutional prior | No emergency relief without merits review | 0.610 | 0.646 | 0.011 | 0.055 | 0.072 | 0.245 | front-line cluster |
| Baseline institutional prior | 60 percent invalidation threshold | 0.609 | 0.634 | 0.067 | 0.080 | 0.067 | 0.248 | rights-protection caveat |
| Baseline institutional prior | Automatic merits follow-up for emergency relief | 0.607 | 0.647 | 0.016 | 0.061 | 0.075 | 0.245 | front-line cluster |
| Baseline institutional prior | Jurisdiction stripping constrained by rights carveouts | 0.607 | 0.639 | 0.071 | 0.068 | 0.079 | 0.247 | front-line cluster |
| Baseline institutional prior | 18-year staggered terms + regular appointments | 0.607 | 0.648 | 0.077 | 0.070 | 0.082 | 0.248 | front-line cluster |
| Baseline institutional prior | Public-interest litigation filter | 0.605 | 0.647 | 0.075 | 0.069 | 0.074 | 0.247 | front-line cluster |
| Baseline institutional prior | Emergency integrity package | 0.605 | 0.646 | 0.017 | 0.064 | 0.060 | 0.243 | front-line cluster |
| Baseline institutional prior | Peer recusal + reasoned emergency docket | 0.603 | 0.644 | 0.073 | 0.069 | 0.072 | 0.246 | front-line cluster |
| Baseline institutional prior | Nonpartisan commission appointments | 0.603 | 0.639 | 0.074 | 0.069 | 0.072 | 0.248 | front-line cluster |
| Baseline institutional prior | Three-judge panels with en banc correction | 0.603 | 0.640 | 0.077 | 0.073 | 0.061 | 0.245 | front-line cluster |
| Baseline institutional prior | Mandatory written emergency reasoning | 0.603 | 0.644 | 0.049 | 0.079 | 0.081 | 0.248 | front-line cluster |
| Baseline institutional prior | Time-limited legislative override window | 0.603 | 0.642 | 0.072 | 0.068 | 0.080 | 0.248 | front-line cluster |
| Baseline institutional prior | Constitutional remand before invalidation | 0.602 | 0.638 | 0.078 | 0.071 | 0.077 | 0.214 | rights-protection caveat |
| Baseline institutional prior | Randomized merits panels with en banc correction | 0.601 | 0.647 | 0.076 | 0.071 | 0.077 | 0.247 | front-line cluster |
| Baseline institutional prior | Independent recusal enforcement with substitutes | 0.601 | 0.643 | 0.075 | 0.071 | 0.076 | 0.247 | front-line cluster |
| Baseline institutional prior | Expanded 15-seat court | 0.601 | 0.639 | 0.074 | 0.070 | 0.070 | 0.247 | front-line cluster |
| Baseline institutional prior | Constitutional remand with override window | 0.600 | 0.633 | 0.048 | 0.077 | 0.077 | 0.214 | rights-protection caveat |
| Baseline institutional prior | Pre-enactment constitutional council | 0.600 | 0.643 | 0.072 | 0.067 | 0.068 | 0.244 | front-line cluster |
| Low-polarization prior | No emergency relief without merits review | 0.612 | 0.638 | 0.010 | 0.051 | 0.067 | 0.240 | front-line cluster |
| Low-polarization prior | 60 percent invalidation threshold | 0.609 | 0.627 | 0.059 | 0.071 | 0.077 | 0.244 | rights-protection caveat |
| Low-polarization prior | Jurisdiction stripping constrained by rights carveouts | 0.608 | 0.635 | 0.069 | 0.063 | 0.076 | 0.242 | front-line cluster |
| Low-polarization prior | 18-year staggered terms + regular appointments | 0.608 | 0.636 | 0.071 | 0.065 | 0.076 | 0.243 | front-line cluster |
| Low-polarization prior | Public-interest litigation filter | 0.607 | 0.639 | 0.068 | 0.063 | 0.069 | 0.243 | front-line cluster |
| Low-polarization prior | Constitutional remand before invalidation | 0.606 | 0.631 | 0.069 | 0.062 | 0.066 | 0.209 | front-line cluster |
| Low-polarization prior | Automatic merits follow-up for emergency relief | 0.605 | 0.640 | 0.017 | 0.057 | 0.074 | 0.242 | front-line cluster |
| Low-polarization prior | Retention-election accountability court | 0.605 | 0.633 | 0.072 | 0.065 | 0.070 | 0.242 | front-line cluster |
| Low-polarization prior | Peer recusal + reasoned emergency docket | 0.605 | 0.635 | 0.073 | 0.064 | 0.070 | 0.243 | front-line cluster |
| Low-polarization prior | Nonpartisan commission appointments | 0.605 | 0.638 | 0.071 | 0.062 | 0.084 | 0.244 | front-line cluster |
| Low-polarization prior | Emergency integrity package | 0.604 | 0.641 | 0.016 | 0.057 | 0.068 | 0.240 | front-line cluster |
| Low-polarization prior | Three-judge panels with en banc correction | 0.604 | 0.633 | 0.070 | 0.064 | 0.080 | 0.245 | front-line cluster |
| Low-polarization prior | Mandatory written emergency reasoning | 0.603 | 0.632 | 0.042 | 0.068 | 0.072 | 0.243 | front-line cluster |
| Low-polarization prior | Randomized merits panels with en banc correction | 0.603 | 0.634 | 0.075 | 0.065 | 0.069 | 0.243 | front-line cluster |
| Low-polarization prior | Constitutional remand with override window | 0.602 | 0.627 | 0.047 | 0.075 | 0.068 | 0.209 | rights-protection caveat |
| Low-polarization prior | Time-limited legislative override window | 0.602 | 0.638 | 0.076 | 0.069 | 0.078 | 0.244 | front-line cluster |
| High-polarization prior | No emergency relief without merits review | 0.608 | 0.644 | 0.011 | 0.059 | 0.076 | 0.262 | front-line cluster |
| High-polarization prior | Jurisdiction stripping constrained by rights carveouts | 0.603 | 0.639 | 0.078 | 0.076 | 0.075 | 0.263 | front-line cluster |
| High-polarization prior | Automatic merits follow-up for emergency relief | 0.602 | 0.644 | 0.018 | 0.069 | 0.079 | 0.262 | front-line cluster |
| High-polarization prior | 60 percent invalidation threshold | 0.602 | 0.629 | 0.072 | 0.086 | 0.079 | 0.267 | rights-protection caveat |
| High-polarization prior | 18-year staggered terms + regular appointments | 0.601 | 0.637 | 0.076 | 0.074 | 0.095 | 0.267 | front-line cluster |
| High-polarization prior | Emergency integrity package | 0.600 | 0.647 | 0.019 | 0.069 | 0.071 | 0.261 | front-line cluster |
| High-polarization prior | Public-interest litigation filter | 0.599 | 0.647 | 0.079 | 0.078 | 0.081 | 0.265 | front-line cluster |
| High-polarization prior | Retention-election accountability court | 0.599 | 0.631 | 0.079 | 0.079 | 0.081 | 0.265 | rights-protection caveat |
| High-polarization prior | Three-judge panels with en banc correction | 0.598 | 0.639 | 0.078 | 0.076 | 0.090 | 0.266 | front-line cluster |
| Low appointment-capture prior | No emergency relief without merits review | 0.612 | 0.646 | 0.010 | 0.051 | 0.085 | 0.239 | front-line cluster |
| Low appointment-capture prior | 60 percent invalidation threshold | 0.610 | 0.629 | 0.064 | 0.071 | 0.069 | 0.241 | rights-protection caveat |
| Low appointment-capture prior | Jurisdiction stripping constrained by rights carveouts | 0.610 | 0.640 | 0.071 | 0.061 | 0.082 | 0.240 | front-line cluster |
| Low appointment-capture prior | Constitutional remand before invalidation | 0.609 | 0.630 | 0.066 | 0.060 | 0.072 | 0.206 | rights-protection caveat |
| Low appointment-capture prior | Emergency integrity package | 0.608 | 0.644 | 0.015 | 0.055 | 0.067 | 0.237 | front-line cluster |
| Low appointment-capture prior | Automatic merits follow-up for emergency relief | 0.608 | 0.641 | 0.016 | 0.056 | 0.075 | 0.238 | front-line cluster |
| Low appointment-capture prior | Nonpartisan commission appointments | 0.608 | 0.643 | 0.069 | 0.063 | 0.066 | 0.238 | front-line cluster |
| Low appointment-capture prior | 18-year staggered terms + regular appointments | 0.608 | 0.638 | 0.070 | 0.062 | 0.080 | 0.241 | front-line cluster |
| Low appointment-capture prior | Mandatory written emergency reasoning | 0.607 | 0.636 | 0.044 | 0.070 | 0.066 | 0.239 | front-line cluster |
| Low appointment-capture prior | Public-interest litigation filter | 0.607 | 0.648 | 0.071 | 0.063 | 0.071 | 0.239 | front-line cluster |
| Low appointment-capture prior | Peer recusal + reasoned emergency docket | 0.606 | 0.630 | 0.069 | 0.060 | 0.069 | 0.241 | rights-protection caveat |
| Low appointment-capture prior | Randomized merits panels with en banc correction | 0.605 | 0.630 | 0.072 | 0.062 | 0.061 | 0.240 | rights-protection caveat |
| Low appointment-capture prior | Retention-election accountability court | 0.605 | 0.629 | 0.069 | 0.060 | 0.078 | 0.241 | front-line cluster |
| Low appointment-capture prior | Constitutional remand with override window | 0.605 | 0.635 | 0.042 | 0.068 | 0.078 | 0.206 | administrative-cost caveat |
| Low appointment-capture prior | Three-judge panels with en banc correction | 0.604 | 0.634 | 0.070 | 0.063 | 0.079 | 0.241 | front-line cluster |
| Low appointment-capture prior | Judicial review with legislative supermajority override | 0.604 | 0.641 | 0.071 | 0.063 | 0.071 | 0.239 | front-line cluster |
| Low appointment-capture prior | Independent recusal enforcement with substitutes | 0.604 | 0.638 | 0.070 | 0.063 | 0.079 | 0.241 | front-line cluster |
| Low appointment-capture prior | Time-limited legislative override window | 0.604 | 0.636 | 0.068 | 0.061 | 0.073 | 0.240 | front-line cluster |
| Low appointment-capture prior | Expanded 15-seat court | 0.603 | 0.638 | 0.069 | 0.063 | 0.073 | 0.240 | front-line cluster |
| Low appointment-capture prior | Pre-enactment constitutional council | 0.602 | 0.636 | 0.069 | 0.059 | 0.075 | 0.239 | front-line cluster |
| Low appointment-capture prior | Random panels with jurisdiction safeguards | 0.602 | 0.625 | 0.060 | 0.068 | 0.082 | 0.241 | rights-protection caveat |
| Low appointment-capture prior | Comparative 16-seat constitutional senates | 0.602 | 0.629 | 0.062 | 0.071 | 0.063 | 0.240 | rights-protection caveat |
| High appointment-capture prior | No emergency relief without merits review | 0.607 | 0.643 | 0.011 | 0.060 | 0.076 | 0.260 | front-line cluster |
| High appointment-capture prior | 60 percent invalidation threshold | 0.603 | 0.632 | 0.076 | 0.089 | 0.083 | 0.265 | rights-protection caveat |
| High appointment-capture prior | Automatic merits follow-up for emergency relief | 0.602 | 0.644 | 0.018 | 0.068 | 0.080 | 0.261 | front-line cluster |
| High appointment-capture prior | Nonpartisan commission appointments | 0.602 | 0.638 | 0.077 | 0.076 | 0.070 | 0.262 | front-line cluster |
| High appointment-capture prior | 18-year staggered terms + regular appointments | 0.602 | 0.634 | 0.081 | 0.076 | 0.079 | 0.264 | rights-protection caveat |
| High appointment-capture prior | Emergency integrity package | 0.602 | 0.649 | 0.018 | 0.070 | 0.066 | 0.258 | front-line cluster |
| High appointment-capture prior | Peer recusal + reasoned emergency docket | 0.600 | 0.641 | 0.080 | 0.077 | 0.080 | 0.262 | front-line cluster |
| High appointment-capture prior | Mandatory written emergency reasoning | 0.600 | 0.636 | 0.053 | 0.085 | 0.075 | 0.263 | rights-protection caveat |
| High appointment-capture prior | Public-interest litigation filter | 0.600 | 0.643 | 0.083 | 0.079 | 0.085 | 0.264 | front-line cluster |
| High appointment-capture prior | Jurisdiction stripping constrained by rights carveouts | 0.600 | 0.639 | 0.084 | 0.079 | 0.107 | 0.265 | front-line cluster |
| High appointment-capture prior | Retention-election accountability court | 0.599 | 0.633 | 0.082 | 0.077 | 0.083 | 0.264 | rights-protection caveat |
| High appointment-capture prior | Three-judge panels with en banc correction | 0.599 | 0.636 | 0.080 | 0.076 | 0.078 | 0.263 | front-line cluster |
| High appointment-capture prior | Constitutional remand before invalidation | 0.598 | 0.633 | 0.081 | 0.076 | 0.089 | 0.231 | rights-protection caveat |
| High appointment-capture prior | Judicial review with legislative supermajority override | 0.598 | 0.642 | 0.076 | 0.076 | 0.089 | 0.264 | front-line cluster |
| High appointment-capture prior | Pre-enactment constitutional council | 0.597 | 0.638 | 0.078 | 0.074 | 0.078 | 0.261 | rights-protection caveat |
| Low public-pressure prior | No emergency relief without merits review | 0.610 | 0.648 | 0.011 | 0.057 | 0.071 | 0.247 | front-line cluster |
| Low public-pressure prior | Automatic merits follow-up for emergency relief | 0.608 | 0.644 | 0.017 | 0.064 | 0.071 | 0.247 | front-line cluster |
| Low public-pressure prior | 60 percent invalidation threshold | 0.606 | 0.635 | 0.066 | 0.079 | 0.080 | 0.252 | rights-protection caveat |
| Low public-pressure prior | 18-year staggered terms + regular appointments | 0.606 | 0.640 | 0.080 | 0.072 | 0.078 | 0.251 | rights-protection caveat |
| Low public-pressure prior | Jurisdiction stripping constrained by rights carveouts | 0.606 | 0.641 | 0.073 | 0.070 | 0.085 | 0.249 | front-line cluster |
| Low public-pressure prior | Public-interest litigation filter | 0.605 | 0.648 | 0.075 | 0.069 | 0.076 | 0.249 | front-line cluster |
| Low public-pressure prior | Nonpartisan commission appointments | 0.605 | 0.639 | 0.075 | 0.069 | 0.070 | 0.249 | rights-protection caveat |
| Low public-pressure prior | Peer recusal + reasoned emergency docket | 0.604 | 0.640 | 0.073 | 0.067 | 0.070 | 0.250 | front-line cluster |
| Low public-pressure prior | Mandatory written emergency reasoning | 0.604 | 0.638 | 0.047 | 0.077 | 0.071 | 0.249 | rights-protection caveat |
| Low public-pressure prior | Emergency integrity package | 0.603 | 0.648 | 0.018 | 0.068 | 0.070 | 0.246 | front-line cluster |
| Low public-pressure prior | Retention-election accountability court | 0.603 | 0.635 | 0.075 | 0.068 | 0.076 | 0.250 | rights-protection caveat |
| Low public-pressure prior | Constitutional remand before invalidation | 0.603 | 0.641 | 0.076 | 0.069 | 0.071 | 0.215 | rights-protection caveat |
| Low public-pressure prior | Three-judge panels with en banc correction | 0.603 | 0.644 | 0.076 | 0.070 | 0.081 | 0.250 | front-line cluster |
| Low public-pressure prior | Time-limited legislative override window | 0.602 | 0.641 | 0.076 | 0.070 | 0.085 | 0.251 | front-line cluster |
| Low public-pressure prior | Judicial review with legislative supermajority override | 0.602 | 0.646 | 0.073 | 0.067 | 0.081 | 0.250 | front-line cluster |
| Low public-pressure prior | Expanded 15-seat court | 0.600 | 0.642 | 0.073 | 0.070 | 0.077 | 0.250 | front-line cluster |
| High public-pressure prior | No emergency relief without merits review | 0.608 | 0.649 | 0.012 | 0.063 | 0.076 | 0.250 | front-line cluster |
| High public-pressure prior | 18-year staggered terms + regular appointments | 0.605 | 0.644 | 0.081 | 0.080 | 0.073 | 0.251 | front-line cluster |
| High public-pressure prior | 60 percent invalidation threshold | 0.603 | 0.634 | 0.073 | 0.090 | 0.087 | 0.255 | rights-protection caveat |
| High public-pressure prior | Emergency integrity package | 0.603 | 0.647 | 0.019 | 0.073 | 0.067 | 0.249 | front-line cluster |
| High public-pressure prior | Automatic merits follow-up for emergency relief | 0.603 | 0.651 | 0.020 | 0.074 | 0.081 | 0.250 | front-line cluster |
| High public-pressure prior | Jurisdiction stripping constrained by rights carveouts | 0.603 | 0.643 | 0.085 | 0.081 | 0.088 | 0.252 | front-line cluster |
| High public-pressure prior | Three-judge panels with en banc correction | 0.601 | 0.641 | 0.081 | 0.079 | 0.069 | 0.251 | rights-protection caveat |
| High public-pressure prior | Nonpartisan commission appointments | 0.601 | 0.642 | 0.083 | 0.080 | 0.088 | 0.254 | front-line cluster |
| High public-pressure prior | Mandatory written emergency reasoning | 0.601 | 0.637 | 0.051 | 0.087 | 0.085 | 0.254 | rights-protection caveat |
| High public-pressure prior | Peer recusal + reasoned emergency docket | 0.601 | 0.639 | 0.077 | 0.075 | 0.089 | 0.254 | rights-protection caveat |
| High public-pressure prior | Public-interest litigation filter | 0.600 | 0.648 | 0.085 | 0.081 | 0.079 | 0.253 | front-line cluster |
| High public-pressure prior | Time-limited legislative override window | 0.600 | 0.635 | 0.081 | 0.077 | 0.085 | 0.254 | rights-protection caveat |
| High public-pressure prior | Constitutional remand before invalidation | 0.600 | 0.638 | 0.081 | 0.078 | 0.074 | 0.219 | rights-protection caveat |
| High public-pressure prior | Retention-election accountability court | 0.599 | 0.637 | 0.080 | 0.078 | 0.094 | 0.255 | front-line cluster |
| High public-pressure prior | Expanded 15-seat court | 0.599 | 0.643 | 0.081 | 0.079 | 0.069 | 0.252 | front-line cluster |
| High public-pressure prior | Judicial review with legislative supermajority override | 0.598 | 0.641 | 0.083 | 0.080 | 0.092 | 0.255 | rights-protection caveat |
| High public-pressure prior | Constitutional remand with override window | 0.598 | 0.635 | 0.053 | 0.088 | 0.074 | 0.218 | rights-protection caveat |
| Low emergency-share prior | Jurisdiction stripping constrained by rights carveouts | 0.615 | 0.640 | 0.058 | 0.047 | 0.055 | 0.240 | front-line cluster |
| Low emergency-share prior | No emergency relief without merits review | 0.615 | 0.645 | 0.009 | 0.038 | 0.063 | 0.240 | front-line cluster |
| Low emergency-share prior | 60 percent invalidation threshold | 0.612 | 0.636 | 0.052 | 0.057 | 0.078 | 0.245 | rights-protection caveat |
| Low emergency-share prior | 18-year staggered terms + regular appointments | 0.612 | 0.643 | 0.062 | 0.051 | 0.069 | 0.243 | front-line cluster |
| Low emergency-share prior | Public-interest litigation filter | 0.611 | 0.644 | 0.061 | 0.050 | 0.056 | 0.241 | front-line cluster |
| Low emergency-share prior | Emergency integrity package | 0.611 | 0.645 | 0.014 | 0.044 | 0.052 | 0.239 | front-line cluster |
| Low emergency-share prior | Nonpartisan commission appointments | 0.611 | 0.640 | 0.062 | 0.049 | 0.062 | 0.242 | front-line cluster |
| Low emergency-share prior | Mandatory written emergency reasoning | 0.610 | 0.634 | 0.035 | 0.053 | 0.064 | 0.243 | front-line cluster |
| Low emergency-share prior | Constitutional remand before invalidation | 0.610 | 0.639 | 0.059 | 0.049 | 0.065 | 0.209 | front-line cluster |
| Low emergency-share prior | Automatic merits follow-up for emergency relief | 0.609 | 0.641 | 0.014 | 0.043 | 0.070 | 0.242 | front-line cluster |
| Low emergency-share prior | Expanded 15-seat court | 0.609 | 0.634 | 0.056 | 0.047 | 0.051 | 0.241 | front-line cluster |
| Low emergency-share prior | Three-judge panels with en banc correction | 0.609 | 0.634 | 0.059 | 0.048 | 0.068 | 0.243 | front-line cluster |
| Low emergency-share prior | Retention-election accountability court | 0.608 | 0.632 | 0.058 | 0.047 | 0.067 | 0.243 | rights-protection caveat |
| Low emergency-share prior | Peer recusal + reasoned emergency docket | 0.608 | 0.635 | 0.062 | 0.050 | 0.072 | 0.244 | rights-protection caveat |
| Low emergency-share prior | Independent recusal enforcement with substitutes | 0.607 | 0.638 | 0.058 | 0.048 | 0.069 | 0.243 | front-line cluster |
| Low emergency-share prior | Constitutional remand with override window | 0.607 | 0.637 | 0.036 | 0.055 | 0.066 | 0.208 | rights-protection caveat |
| Low emergency-share prior | Judicial review with legislative supermajority override | 0.606 | 0.636 | 0.054 | 0.048 | 0.076 | 0.243 | front-line cluster |
| High emergency-share prior | 18-year staggered terms + regular appointments | 0.520 | 0.618 | 0.177 | 0.219 | 0.223 | 0.402 | compliance caveat |
| High emergency-share prior | Jurisdiction stripping constrained by rights carveouts | 0.517 | 0.621 | 0.185 | 0.223 | 0.247 | 0.404 | compliance caveat |
| High emergency-share prior | Public-interest litigation filter | 0.517 | 0.630 | 0.178 | 0.218 | 0.230 | 0.403 | compliance caveat |
| High emergency-share prior | 60 percent invalidation threshold | 0.517 | 0.611 | 0.176 | 0.258 | 0.241 | 0.407 | compliance caveat |
| High emergency-share prior | No emergency relief without merits review | 0.516 | 0.644 | 0.048 | 0.179 | 0.229 | 0.395 | compliance caveat |
| High emergency-share prior | Constitutional remand before invalidation | 0.516 | 0.619 | 0.186 | 0.227 | 0.223 | 0.367 | compliance caveat |
| High emergency-share prior | Independent recusal enforcement with substitutes | 0.515 | 0.628 | 0.182 | 0.222 | 0.217 | 0.402 | compliance caveat |
| High emergency-share prior | Nonpartisan commission appointments | 0.515 | 0.620 | 0.180 | 0.222 | 0.221 | 0.402 | compliance caveat |
| High emergency-share prior | Constitutional remand with override window | 0.514 | 0.613 | 0.140 | 0.246 | 0.222 | 0.368 | compliance caveat |
| High emergency-share prior | Three-judge panels with en banc correction | 0.513 | 0.626 | 0.184 | 0.227 | 0.234 | 0.403 | compliance caveat |
| High emergency-share prior | Retention-election accountability court | 0.513 | 0.614 | 0.178 | 0.218 | 0.238 | 0.404 | compliance caveat |
| High emergency-share prior | Comparative 16-seat constitutional senates | 0.512 | 0.606 | 0.167 | 0.247 | 0.222 | 0.405 | rights-protection caveat |
| High emergency-share prior | Peer recusal + reasoned emergency docket | 0.512 | 0.623 | 0.185 | 0.225 | 0.238 | 0.404 | compliance caveat |
| High emergency-share prior | Pre-enactment constitutional council | 0.511 | 0.624 | 0.179 | 0.221 | 0.217 | 0.398 | compliance caveat |
| High emergency-share prior | Mandatory written emergency reasoning | 0.511 | 0.611 | 0.147 | 0.253 | 0.232 | 0.405 | compliance caveat |
| High emergency-share prior | Emergency integrity package | 0.511 | 0.639 | 0.059 | 0.181 | 0.226 | 0.396 | compliance caveat |
| High emergency-share prior | Randomized merits panels with en banc correction | 0.510 | 0.624 | 0.182 | 0.223 | 0.241 | 0.404 | compliance caveat |
| High emergency-share prior | Time-limited legislative override window | 0.510 | 0.624 | 0.181 | 0.225 | 0.252 | 0.405 | compliance caveat |
| Low rights-risk prior | No emergency relief without merits review | 0.637 | 0.649 | 0.005 | 0.037 | 0.032 | 0.175 | rights-protection caveat |
| Low rights-risk prior | Jurisdiction stripping constrained by rights carveouts | 0.637 | 0.644 | 0.051 | 0.042 | 0.029 | 0.176 | rights-protection caveat |
| Low rights-risk prior | 60 percent invalidation threshold | 0.636 | 0.637 | 0.044 | 0.048 | 0.030 | 0.179 | rights-protection caveat |
| Low rights-risk prior | 18-year staggered terms + regular appointments | 0.634 | 0.644 | 0.052 | 0.045 | 0.039 | 0.179 | rights-protection caveat |
| Low rights-risk prior | Nonpartisan commission appointments | 0.634 | 0.646 | 0.054 | 0.045 | 0.030 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Automatic merits follow-up for emergency relief | 0.633 | 0.644 | 0.009 | 0.046 | 0.032 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Mandatory written emergency reasoning | 0.632 | 0.645 | 0.029 | 0.049 | 0.034 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Time-limited legislative override window | 0.632 | 0.643 | 0.052 | 0.043 | 0.033 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Retention-election accountability court | 0.632 | 0.637 | 0.051 | 0.043 | 0.042 | 0.179 | rights-protection caveat |
| Low rights-risk prior | Peer recusal + reasoned emergency docket | 0.631 | 0.649 | 0.054 | 0.045 | 0.035 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Emergency integrity package | 0.631 | 0.642 | 0.009 | 0.047 | 0.031 | 0.176 | rights-protection caveat |
| Low rights-risk prior | Constitutional remand before invalidation | 0.630 | 0.641 | 0.052 | 0.043 | 0.035 | 0.146 | rights-protection caveat |
| Low rights-risk prior | Judicial review with legislative supermajority override | 0.630 | 0.649 | 0.055 | 0.046 | 0.035 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Public-interest litigation filter | 0.630 | 0.645 | 0.054 | 0.045 | 0.047 | 0.179 | rights-protection caveat |
| Low rights-risk prior | Three-judge panels with en banc correction | 0.630 | 0.646 | 0.055 | 0.045 | 0.038 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Randomized merits panels with en banc correction | 0.630 | 0.642 | 0.054 | 0.045 | 0.032 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Independent recusal enforcement with substitutes | 0.629 | 0.648 | 0.056 | 0.046 | 0.040 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Pre-enactment constitutional council | 0.628 | 0.641 | 0.054 | 0.044 | 0.031 | 0.176 | rights-protection caveat |
| Low rights-risk prior | Expanded 15-seat court | 0.628 | 0.650 | 0.055 | 0.045 | 0.041 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Constitutional remand with override window | 0.628 | 0.643 | 0.027 | 0.047 | 0.038 | 0.146 | rights-protection caveat |
| Low rights-risk prior | Random panels with jurisdiction safeguards | 0.628 | 0.643 | 0.048 | 0.052 | 0.038 | 0.177 | rights-protection caveat |
| High rights-risk prior | No emergency relief without merits review | 0.526 | 0.602 | 0.027 | 0.098 | 0.228 | 0.398 | compliance caveat |
| High rights-risk prior | Constitutional remand before invalidation | 0.526 | 0.565 | 0.118 | 0.131 | 0.215 | 0.363 | compliance caveat |
| High rights-risk prior | 60 percent invalidation threshold | 0.526 | 0.552 | 0.116 | 0.165 | 0.226 | 0.405 | compliance caveat |
| High rights-risk prior | Automatic merits follow-up for emergency relief | 0.526 | 0.594 | 0.034 | 0.079 | 0.241 | 0.401 | compliance caveat |
| High rights-risk prior | 18-year staggered terms + regular appointments | 0.526 | 0.568 | 0.121 | 0.138 | 0.215 | 0.402 | compliance caveat |
| High rights-risk prior | Emergency integrity package | 0.524 | 0.599 | 0.035 | 0.079 | 0.229 | 0.399 | compliance caveat |
| High rights-risk prior | Nonpartisan commission appointments | 0.520 | 0.574 | 0.126 | 0.137 | 0.234 | 0.404 | compliance caveat |
| High rights-risk prior | Constitutional remand with override window | 0.520 | 0.553 | 0.093 | 0.160 | 0.229 | 0.366 | compliance caveat |
| High rights-risk prior | Three-judge panels with en banc correction | 0.520 | 0.572 | 0.120 | 0.134 | 0.224 | 0.403 | compliance caveat |
| High rights-risk prior | Randomized merits panels with en banc correction | 0.520 | 0.571 | 0.120 | 0.136 | 0.215 | 0.402 | compliance caveat |
| High rights-risk prior | Peer recusal + reasoned emergency docket | 0.520 | 0.569 | 0.116 | 0.132 | 0.230 | 0.403 | compliance caveat |
| High rights-risk prior | Mandatory written emergency reasoning | 0.519 | 0.564 | 0.092 | 0.164 | 0.225 | 0.403 | compliance caveat |
| High rights-risk prior | Public-interest litigation filter | 0.519 | 0.575 | 0.117 | 0.132 | 0.221 | 0.402 | compliance caveat |
| High rights-risk prior | Expanded 15-seat court | 0.518 | 0.573 | 0.120 | 0.133 | 0.242 | 0.405 | compliance caveat |
| High rights-risk prior | Jurisdiction stripping constrained by rights carveouts | 0.517 | 0.576 | 0.121 | 0.137 | 0.242 | 0.403 | compliance caveat |
| High rights-risk prior | Retention-election accountability court | 0.517 | 0.551 | 0.119 | 0.132 | 0.237 | 0.404 | compliance caveat |
| Weak democratic-mandate prior | 60 percent invalidation threshold | 0.544 | 0.604 | 0.095 | 0.127 | 0.184 | 0.378 | compliance caveat |
| Weak democratic-mandate prior | Constitutional remand before invalidation | 0.540 | 0.616 | 0.108 | 0.111 | 0.173 | 0.338 | compliance caveat |
| Weak democratic-mandate prior | Constitutional remand with override window | 0.539 | 0.612 | 0.075 | 0.128 | 0.180 | 0.339 | compliance caveat |
| Weak democratic-mandate prior | No emergency relief without merits review | 0.539 | 0.622 | 0.021 | 0.084 | 0.183 | 0.372 | compliance caveat |
| Weak democratic-mandate prior | Public-interest litigation filter | 0.538 | 0.620 | 0.100 | 0.108 | 0.187 | 0.376 | compliance caveat |
| Weak democratic-mandate prior | 18-year staggered terms + regular appointments | 0.537 | 0.611 | 0.105 | 0.109 | 0.185 | 0.377 | compliance caveat |
| Weak democratic-mandate prior | Nonpartisan commission appointments | 0.537 | 0.612 | 0.103 | 0.109 | 0.176 | 0.376 | compliance caveat |
| Weak democratic-mandate prior | Peer recusal + reasoned emergency docket | 0.536 | 0.610 | 0.104 | 0.110 | 0.189 | 0.377 | compliance caveat |
| Weak democratic-mandate prior | Mandatory written emergency reasoning | 0.535 | 0.613 | 0.077 | 0.129 | 0.170 | 0.375 | compliance caveat |
| Weak democratic-mandate prior | Jurisdiction stripping constrained by rights carveouts | 0.535 | 0.614 | 0.101 | 0.108 | 0.215 | 0.378 | compliance caveat |
| Weak democratic-mandate prior | Automatic merits follow-up for emergency relief | 0.534 | 0.621 | 0.029 | 0.074 | 0.199 | 0.374 | compliance caveat |
| High constitutional-conflict prior | 60 percent invalidation threshold | 0.513 | 0.602 | 0.143 | 0.194 | 0.233 | 0.438 | compliance caveat |
| High constitutional-conflict prior | Constitutional remand before invalidation | 0.509 | 0.616 | 0.155 | 0.168 | 0.237 | 0.400 | compliance caveat |
| High constitutional-conflict prior | Public-interest litigation filter | 0.506 | 0.623 | 0.155 | 0.168 | 0.228 | 0.435 | compliance caveat |
| High constitutional-conflict prior | Constitutional remand with override window | 0.505 | 0.609 | 0.119 | 0.193 | 0.245 | 0.401 | compliance caveat |
| High constitutional-conflict prior | Comparative 16-seat constitutional senates | 0.504 | 0.604 | 0.140 | 0.192 | 0.229 | 0.437 | compliance caveat |
| High constitutional-conflict prior | 18-year staggered terms + regular appointments | 0.503 | 0.615 | 0.149 | 0.164 | 0.248 | 0.438 | compliance caveat |
| Imported legislative-family prior | No emergency relief without merits review | 0.618 | 0.655 | 0.008 | 0.054 | 0.057 | 0.229 | front-line cluster |
| Imported legislative-family prior | 18-year staggered terms + regular appointments | 0.615 | 0.643 | 0.069 | 0.065 | 0.064 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | 60 percent invalidation threshold | 0.614 | 0.643 | 0.060 | 0.074 | 0.069 | 0.234 | rights-protection caveat |
| Imported legislative-family prior | Jurisdiction stripping constrained by rights carveouts | 0.613 | 0.645 | 0.072 | 0.068 | 0.070 | 0.232 | rights-protection caveat |
| Imported legislative-family prior | Automatic merits follow-up for emergency relief | 0.612 | 0.651 | 0.015 | 0.067 | 0.065 | 0.230 | front-line cluster |
| Imported legislative-family prior | Nonpartisan commission appointments | 0.611 | 0.644 | 0.071 | 0.067 | 0.067 | 0.234 | rights-protection caveat |
| Imported legislative-family prior | Peer recusal + reasoned emergency docket | 0.610 | 0.645 | 0.073 | 0.067 | 0.064 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Mandatory written emergency reasoning | 0.610 | 0.645 | 0.044 | 0.073 | 0.066 | 0.232 | rights-protection caveat |
| Imported legislative-family prior | Three-judge panels with en banc correction | 0.610 | 0.648 | 0.071 | 0.068 | 0.066 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Randomized merits panels with en banc correction | 0.610 | 0.651 | 0.071 | 0.068 | 0.066 | 0.232 | rights-protection caveat |
| Imported legislative-family prior | Retention-election accountability court | 0.610 | 0.640 | 0.071 | 0.066 | 0.070 | 0.234 | rights-protection caveat |
| Imported legislative-family prior | Emergency integrity package | 0.610 | 0.653 | 0.015 | 0.063 | 0.076 | 0.232 | rights-protection caveat |
| Imported legislative-family prior | Public-interest litigation filter | 0.609 | 0.646 | 0.071 | 0.068 | 0.084 | 0.235 | rights-protection caveat |
| Imported legislative-family prior | Judicial review with legislative supermajority override | 0.609 | 0.646 | 0.073 | 0.067 | 0.074 | 0.234 | rights-protection caveat |
| Imported legislative-family prior | Time-limited legislative override window | 0.609 | 0.650 | 0.072 | 0.067 | 0.071 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Constitutional remand before invalidation | 0.608 | 0.643 | 0.077 | 0.069 | 0.074 | 0.201 | rights-protection caveat |
