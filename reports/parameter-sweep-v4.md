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
| No emergency relief without merits review | 0.508 / 0.608 / 0.625 | 0.452 / 0.660 / 0.696 | 0.617 / 0.648 / 0.652 | 0.007 / 0.011 / 0.044 | 0.345 / 0.384 / 0.604 | 0.169 / 0.194 / 0.318 |
| 60 percent invalidation threshold | 0.516 / 0.605 / 0.621 | 0.522 / 0.668 / 0.693 | 0.588 / 0.635 / 0.643 | 0.052 / 0.072 / 0.157 | 0.350 / 0.391 / 0.599 | 0.184 / 0.209 / 0.329 |
| Jurisdiction stripping constrained by rights carveouts | 0.505 / 0.605 / 0.621 | 0.477 / 0.659 / 0.689 | 0.602 / 0.639 / 0.648 | 0.053 / 0.080 / 0.167 | 0.352 / 0.395 / 0.622 | 0.176 / 0.203 / 0.337 |
| 18-year staggered terms + regular appointments | 0.511 / 0.605 / 0.622 | 0.490 / 0.659 / 0.695 | 0.598 / 0.643 / 0.650 | 0.060 / 0.080 / 0.164 | 0.344 / 0.390 / 0.599 | 0.184 / 0.210 / 0.329 |
| Automatic merits follow-up for emergency relief | 0.497 / 0.603 / 0.619 | 0.447 / 0.657 / 0.690 | 0.615 / 0.645 / 0.654 | 0.012 / 0.018 / 0.056 | 0.347 / 0.385 / 0.612 | 0.182 / 0.203 / 0.333 |
| Public-interest litigation filter | 0.511 / 0.602 / 0.618 | 0.495 / 0.662 / 0.693 | 0.609 / 0.647 / 0.653 | 0.059 / 0.077 / 0.166 | 0.347 / 0.385 / 0.598 | 0.171 / 0.195 / 0.317 |
| Emergency integrity package | 0.503 / 0.602 / 0.618 | 0.453 / 0.661 / 0.693 | 0.614 / 0.647 / 0.657 | 0.013 / 0.019 / 0.055 | 0.352 / 0.388 / 0.598 | 0.172 / 0.196 / 0.320 |
| Nonpartisan commission appointments | 0.505 / 0.602 / 0.618 | 0.480 / 0.662 / 0.692 | 0.601 / 0.643 / 0.650 | 0.063 / 0.080 / 0.168 | 0.352 / 0.389 / 0.605 | 0.178 / 0.202 / 0.325 |
| Peer recusal + reasoned emergency docket | 0.503 / 0.601 / 0.616 | 0.483 / 0.661 / 0.692 | 0.604 / 0.643 / 0.647 | 0.058 / 0.079 / 0.172 | 0.350 / 0.388 / 0.610 | 0.185 / 0.210 / 0.336 |
| Mandatory written emergency reasoning | 0.507 / 0.601 / 0.618 | 0.496 / 0.663 / 0.692 | 0.597 / 0.638 / 0.650 | 0.036 / 0.051 / 0.127 | 0.350 / 0.391 / 0.602 | 0.183 / 0.210 / 0.329 |
| Retention-election accountability court | 0.507 / 0.601 / 0.618 | 0.489 / 0.663 / 0.693 | 0.584 / 0.638 / 0.645 | 0.060 / 0.077 / 0.162 | 0.357 / 0.401 / 0.618 | 0.179 / 0.205 / 0.323 |
| Constitutional remand before invalidation | 0.511 / 0.600 / 0.617 | 0.535 / 0.686 / 0.712 | 0.600 / 0.637 / 0.646 | 0.058 / 0.080 / 0.169 | 0.344 / 0.390 / 0.604 | 0.167 / 0.197 / 0.319 |
| Judicial review with legislative supermajority override | 0.500 / 0.600 / 0.616 | 0.475 / 0.658 / 0.688 | 0.605 / 0.642 / 0.652 | 0.060 / 0.079 / 0.166 | 0.362 / 0.403 / 0.631 | 0.183 / 0.210 / 0.338 |
| Three-judge panels with en banc correction | 0.506 / 0.600 / 0.618 | 0.487 / 0.662 / 0.692 | 0.600 / 0.641 / 0.651 | 0.059 / 0.080 / 0.168 | 0.349 / 0.390 / 0.607 | 0.177 / 0.201 / 0.326 |
| Time-limited legislative override window | 0.501 / 0.600 / 0.616 | 0.474 / 0.658 / 0.688 | 0.602 / 0.640 / 0.649 | 0.057 / 0.079 / 0.169 | 0.362 / 0.401 / 0.633 | 0.183 / 0.205 / 0.336 |
| Expanded 15-seat court | 0.499 / 0.599 / 0.614 | 0.485 / 0.661 / 0.688 | 0.597 / 0.640 / 0.649 | 0.059 / 0.079 / 0.170 | 0.348 / 0.388 / 0.614 | 0.185 / 0.210 / 0.340 |
| Randomized merits panels with en banc correction | 0.504 / 0.598 / 0.616 | 0.491 / 0.662 / 0.692 | 0.601 / 0.642 / 0.649 | 0.057 / 0.081 / 0.164 | 0.351 / 0.390 / 0.598 | 0.176 / 0.199 / 0.322 |
| Independent recusal enforcement with substitutes | 0.507 / 0.598 / 0.616 | 0.488 / 0.660 / 0.692 | 0.601 / 0.644 / 0.650 | 0.060 / 0.080 / 0.168 | 0.352 / 0.392 / 0.597 | 0.177 / 0.204 / 0.321 |
| Constitutional remand with override window | 0.510 / 0.598 / 0.614 | 0.547 / 0.687 / 0.707 | 0.591 / 0.637 / 0.644 | 0.034 / 0.051 / 0.127 | 0.347 / 0.388 / 0.598 | 0.170 / 0.196 / 0.319 |
| Pre-enactment constitutional council | 0.499 / 0.597 / 0.612 | 0.490 / 0.668 / 0.697 | 0.607 / 0.641 / 0.650 | 0.063 / 0.078 / 0.167 | 0.362 / 0.399 / 0.627 | 0.182 / 0.207 / 0.331 |
| Random panels with jurisdiction safeguards | 0.500 / 0.597 / 0.613 | 0.495 / 0.663 / 0.692 | 0.587 / 0.632 / 0.643 | 0.052 / 0.071 / 0.159 | 0.356 / 0.396 / 0.620 | 0.175 / 0.199 / 0.327 |
| Comparative 16-seat constitutional senates | 0.507 / 0.594 / 0.610 | 0.519 / 0.670 / 0.698 | 0.586 / 0.635 / 0.638 | 0.052 / 0.070 / 0.155 | 0.349 / 0.387 / 0.598 | 0.178 / 0.202 / 0.322 |
| Constitutional council with concrete-review backstop | 0.501 / 0.593 / 0.611 | 0.501 / 0.672 / 0.699 | 0.607 / 0.641 / 0.648 | 0.060 / 0.081 / 0.166 | 0.357 / 0.400 / 0.617 | 0.178 / 0.206 / 0.329 |
| Stylized current U.S.-like supreme court | 0.495 / 0.588 / 0.609 | 0.485 / 0.653 / 0.681 | 0.613 / 0.643 / 0.656 | 0.183 / 0.245 / 0.435 | 0.368 / 0.419 / 0.657 | 0.203 / 0.239 / 0.370 |
| Supreme court with cross-checking constitutional court | 0.494 / 0.585 / 0.602 | 0.525 / 0.661 / 0.688 | 0.565 / 0.621 / 0.636 | 0.051 / 0.069 / 0.157 | 0.370 / 0.411 / 0.627 | 0.177 / 0.200 / 0.320 |
| Dual supreme courts with disagreement filter | 0.472 / 0.575 / 0.594 | 0.461 / 0.639 / 0.675 | 0.599 / 0.640 / 0.648 | 0.052 / 0.074 / 0.155 | 0.377 / 0.422 / 0.632 | 0.183 / 0.208 / 0.331 |

## What Would Change the Interpretation

The table below reports each named prior's top directional-score cluster within 0.010 of that prior's best score. A design conclusion should weaken if it appears only under one narrow prior, if its cluster membership depends on high emergency pressure or high conflict, or if its apparent advantage comes with rights-protection, compliance, or emergency-power caveats.

| Prior | Cluster scenario | Score | Rights | Shadow | Emerg. downstream | Gov. noncomp. | Lower-court resistance | Caveat |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Baseline institutional prior | No emergency relief without merits review | 0.609 | 0.648 | 0.011 | 0.057 | 0.080 | 0.245 | front-line cluster |
| Baseline institutional prior | Jurisdiction stripping constrained by rights carveouts | 0.607 | 0.646 | 0.077 | 0.071 | 0.079 | 0.246 | front-line cluster |
| Baseline institutional prior | Automatic merits follow-up for emergency relief | 0.606 | 0.651 | 0.017 | 0.064 | 0.074 | 0.244 | front-line cluster |
| Baseline institutional prior | 18-year staggered terms + regular appointments | 0.606 | 0.647 | 0.076 | 0.073 | 0.091 | 0.248 | front-line cluster |
| Baseline institutional prior | 60 percent invalidation threshold | 0.606 | 0.636 | 0.071 | 0.083 | 0.078 | 0.248 | rights-protection caveat |
| Baseline institutional prior | Time-limited legislative override window | 0.604 | 0.641 | 0.073 | 0.070 | 0.071 | 0.246 | front-line cluster |
| Baseline institutional prior | Peer recusal + reasoned emergency docket | 0.604 | 0.646 | 0.077 | 0.070 | 0.070 | 0.246 | front-line cluster |
| Baseline institutional prior | Nonpartisan commission appointments | 0.604 | 0.645 | 0.079 | 0.072 | 0.076 | 0.247 | front-line cluster |
| Baseline institutional prior | Emergency integrity package | 0.603 | 0.655 | 0.019 | 0.070 | 0.071 | 0.243 | front-line cluster |
| Baseline institutional prior | Mandatory written emergency reasoning | 0.603 | 0.645 | 0.049 | 0.080 | 0.076 | 0.247 | front-line cluster |
| Baseline institutional prior | Public-interest litigation filter | 0.603 | 0.653 | 0.076 | 0.071 | 0.081 | 0.247 | front-line cluster |
| Baseline institutional prior | Randomized merits panels with en banc correction | 0.602 | 0.647 | 0.075 | 0.070 | 0.080 | 0.247 | front-line cluster |
| Baseline institutional prior | Constitutional remand before invalidation | 0.601 | 0.638 | 0.079 | 0.072 | 0.084 | 0.214 | rights-protection caveat |
| Baseline institutional prior | Retention-election accountability court | 0.601 | 0.644 | 0.078 | 0.071 | 0.092 | 0.248 | front-line cluster |
| Baseline institutional prior | Judicial review with legislative supermajority override | 0.601 | 0.650 | 0.075 | 0.070 | 0.086 | 0.248 | front-line cluster |
| Baseline institutional prior | Three-judge panels with en banc correction | 0.601 | 0.640 | 0.076 | 0.072 | 0.078 | 0.247 | front-line cluster |
| Baseline institutional prior | Expanded 15-seat court | 0.601 | 0.647 | 0.078 | 0.074 | 0.075 | 0.247 | front-line cluster |
| Baseline institutional prior | Independent recusal enforcement with substitutes | 0.600 | 0.644 | 0.078 | 0.072 | 0.078 | 0.247 | front-line cluster |
| Baseline institutional prior | Random panels with jurisdiction safeguards | 0.600 | 0.638 | 0.067 | 0.079 | 0.082 | 0.247 | rights-protection caveat |
| Low-polarization prior | No emergency relief without merits review | 0.610 | 0.646 | 0.011 | 0.054 | 0.081 | 0.241 | front-line cluster |
| Low-polarization prior | 60 percent invalidation threshold | 0.609 | 0.631 | 0.061 | 0.073 | 0.082 | 0.245 | rights-protection caveat |
| Low-polarization prior | 18-year staggered terms + regular appointments | 0.608 | 0.650 | 0.074 | 0.066 | 0.090 | 0.244 | front-line cluster |
| Low-polarization prior | Public-interest litigation filter | 0.607 | 0.642 | 0.070 | 0.064 | 0.071 | 0.242 | front-line cluster |
| Low-polarization prior | Jurisdiction stripping constrained by rights carveouts | 0.607 | 0.638 | 0.071 | 0.065 | 0.083 | 0.242 | front-line cluster |
| Low-polarization prior | Nonpartisan commission appointments | 0.606 | 0.643 | 0.074 | 0.065 | 0.079 | 0.243 | front-line cluster |
| Low-polarization prior | Constitutional remand before invalidation | 0.605 | 0.632 | 0.074 | 0.065 | 0.075 | 0.209 | rights-protection caveat |
| Low-polarization prior | Emergency integrity package | 0.605 | 0.643 | 0.016 | 0.058 | 0.070 | 0.240 | front-line cluster |
| Low-polarization prior | Automatic merits follow-up for emergency relief | 0.604 | 0.643 | 0.017 | 0.058 | 0.077 | 0.241 | front-line cluster |
| Low-polarization prior | Retention-election accountability court | 0.604 | 0.637 | 0.070 | 0.065 | 0.078 | 0.242 | front-line cluster |
| Low-polarization prior | Three-judge panels with en banc correction | 0.603 | 0.639 | 0.074 | 0.067 | 0.082 | 0.244 | front-line cluster |
| Low-polarization prior | Peer recusal + reasoned emergency docket | 0.603 | 0.635 | 0.074 | 0.066 | 0.077 | 0.244 | front-line cluster |
| Low-polarization prior | Constitutional remand with override window | 0.602 | 0.631 | 0.046 | 0.073 | 0.071 | 0.209 | rights-protection caveat |
| Low-polarization prior | Randomized merits panels with en banc correction | 0.602 | 0.643 | 0.076 | 0.067 | 0.071 | 0.241 | front-line cluster |
| Low-polarization prior | Independent recusal enforcement with substitutes | 0.602 | 0.638 | 0.071 | 0.065 | 0.079 | 0.243 | front-line cluster |
| Low-polarization prior | Mandatory written emergency reasoning | 0.602 | 0.638 | 0.044 | 0.072 | 0.088 | 0.244 | front-line cluster |
| Low-polarization prior | Judicial review with legislative supermajority override | 0.602 | 0.640 | 0.076 | 0.067 | 0.080 | 0.244 | front-line cluster |
| Low-polarization prior | Time-limited legislative override window | 0.601 | 0.642 | 0.078 | 0.069 | 0.088 | 0.244 | front-line cluster |
| Low-polarization prior | Expanded 15-seat court | 0.601 | 0.639 | 0.074 | 0.066 | 0.082 | 0.244 | front-line cluster |
| Low-polarization prior | Random panels with jurisdiction safeguards | 0.600 | 0.633 | 0.065 | 0.075 | 0.084 | 0.244 | front-line cluster |
| High-polarization prior | No emergency relief without merits review | 0.606 | 0.646 | 0.012 | 0.062 | 0.080 | 0.262 | front-line cluster |
| High-polarization prior | Emergency integrity package | 0.600 | 0.648 | 0.019 | 0.071 | 0.078 | 0.261 | front-line cluster |
| High-polarization prior | 60 percent invalidation threshold | 0.600 | 0.635 | 0.075 | 0.090 | 0.089 | 0.267 | rights-protection caveat |
| High-polarization prior | Jurisdiction stripping constrained by rights carveouts | 0.600 | 0.636 | 0.083 | 0.081 | 0.093 | 0.265 | front-line cluster |
| High-polarization prior | Automatic merits follow-up for emergency relief | 0.600 | 0.646 | 0.019 | 0.070 | 0.085 | 0.262 | front-line cluster |
| High-polarization prior | Constitutional remand before invalidation | 0.600 | 0.637 | 0.080 | 0.078 | 0.078 | 0.230 | rights-protection caveat |
| High-polarization prior | Retention-election accountability court | 0.599 | 0.635 | 0.077 | 0.076 | 0.083 | 0.264 | front-line cluster |
| High-polarization prior | 18-year staggered terms + regular appointments | 0.599 | 0.642 | 0.082 | 0.080 | 0.102 | 0.267 | front-line cluster |
| High-polarization prior | Public-interest litigation filter | 0.598 | 0.647 | 0.084 | 0.079 | 0.083 | 0.265 | front-line cluster |
| High-polarization prior | Nonpartisan commission appointments | 0.597 | 0.642 | 0.082 | 0.079 | 0.102 | 0.267 | front-line cluster |
| High-polarization prior | Expanded 15-seat court | 0.597 | 0.643 | 0.080 | 0.078 | 0.085 | 0.265 | front-line cluster |
| High-polarization prior | Peer recusal + reasoned emergency docket | 0.597 | 0.643 | 0.080 | 0.080 | 0.078 | 0.264 | front-line cluster |
| High-polarization prior | Randomized merits panels with en banc correction | 0.597 | 0.645 | 0.082 | 0.082 | 0.078 | 0.263 | front-line cluster |
| High-polarization prior | Time-limited legislative override window | 0.597 | 0.640 | 0.079 | 0.076 | 0.092 | 0.266 | front-line cluster |
| High-polarization prior | Mandatory written emergency reasoning | 0.596 | 0.638 | 0.053 | 0.087 | 0.083 | 0.266 | front-line cluster |
| High-polarization prior | Constitutional remand with override window | 0.596 | 0.635 | 0.051 | 0.087 | 0.080 | 0.230 | rights-protection caveat |
| High-polarization prior | Three-judge panels with en banc correction | 0.596 | 0.643 | 0.084 | 0.082 | 0.094 | 0.266 | front-line cluster |
| Low appointment-capture prior | No emergency relief without merits review | 0.611 | 0.647 | 0.010 | 0.052 | 0.082 | 0.238 | front-line cluster |
| Low appointment-capture prior | Jurisdiction stripping constrained by rights carveouts | 0.610 | 0.640 | 0.075 | 0.063 | 0.081 | 0.239 | front-line cluster |
| Low appointment-capture prior | Automatic merits follow-up for emergency relief | 0.609 | 0.645 | 0.017 | 0.059 | 0.070 | 0.236 | front-line cluster |
| Low appointment-capture prior | 60 percent invalidation threshold | 0.609 | 0.634 | 0.065 | 0.072 | 0.083 | 0.242 | rights-protection caveat |
| Low appointment-capture prior | Nonpartisan commission appointments | 0.609 | 0.646 | 0.069 | 0.061 | 0.067 | 0.238 | front-line cluster |
| Low appointment-capture prior | Constitutional remand before invalidation | 0.607 | 0.633 | 0.074 | 0.065 | 0.069 | 0.206 | rights-protection caveat |
| Low appointment-capture prior | Emergency integrity package | 0.607 | 0.644 | 0.016 | 0.056 | 0.070 | 0.237 | front-line cluster |
| Low appointment-capture prior | 18-year staggered terms + regular appointments | 0.607 | 0.643 | 0.074 | 0.065 | 0.096 | 0.242 | front-line cluster |
| Low appointment-capture prior | Public-interest litigation filter | 0.607 | 0.653 | 0.074 | 0.064 | 0.076 | 0.239 | front-line cluster |
| Low appointment-capture prior | Retention-election accountability court | 0.606 | 0.634 | 0.070 | 0.062 | 0.076 | 0.240 | front-line cluster |
| Low appointment-capture prior | Randomized merits panels with en banc correction | 0.605 | 0.637 | 0.070 | 0.062 | 0.061 | 0.238 | rights-protection caveat |
| Low appointment-capture prior | Mandatory written emergency reasoning | 0.605 | 0.637 | 0.045 | 0.071 | 0.077 | 0.240 | front-line cluster |
| Low appointment-capture prior | Three-judge panels with en banc correction | 0.604 | 0.634 | 0.073 | 0.063 | 0.080 | 0.241 | front-line cluster |
| Low appointment-capture prior | Independent recusal enforcement with substitutes | 0.604 | 0.637 | 0.072 | 0.062 | 0.081 | 0.241 | front-line cluster |
| Low appointment-capture prior | Time-limited legislative override window | 0.604 | 0.644 | 0.073 | 0.063 | 0.074 | 0.240 | front-line cluster |
| Low appointment-capture prior | Peer recusal + reasoned emergency docket | 0.604 | 0.636 | 0.078 | 0.067 | 0.081 | 0.241 | rights-protection caveat |
| Low appointment-capture prior | Expanded 15-seat court | 0.603 | 0.639 | 0.072 | 0.064 | 0.074 | 0.240 | front-line cluster |
| Low appointment-capture prior | Constitutional remand with override window | 0.603 | 0.637 | 0.045 | 0.071 | 0.084 | 0.207 | rights-protection caveat |
| Low appointment-capture prior | Judicial review with legislative supermajority override | 0.602 | 0.639 | 0.076 | 0.065 | 0.080 | 0.241 | front-line cluster |
| High appointment-capture prior | No emergency relief without merits review | 0.607 | 0.651 | 0.012 | 0.063 | 0.082 | 0.260 | front-line cluster |
| High appointment-capture prior | 60 percent invalidation threshold | 0.605 | 0.638 | 0.075 | 0.090 | 0.077 | 0.263 | rights-protection caveat |
| High appointment-capture prior | 18-year staggered terms + regular appointments | 0.602 | 0.642 | 0.082 | 0.078 | 0.069 | 0.262 | front-line cluster |
| High appointment-capture prior | Automatic merits follow-up for emergency relief | 0.602 | 0.645 | 0.018 | 0.069 | 0.073 | 0.259 | front-line cluster |
| High appointment-capture prior | Jurisdiction stripping constrained by rights carveouts | 0.602 | 0.637 | 0.084 | 0.078 | 0.100 | 0.264 | rights-protection caveat |
| High appointment-capture prior | Public-interest litigation filter | 0.602 | 0.642 | 0.077 | 0.076 | 0.074 | 0.262 | front-line cluster |
| High appointment-capture prior | Retention-election accountability court | 0.600 | 0.639 | 0.082 | 0.077 | 0.076 | 0.262 | front-line cluster |
| High appointment-capture prior | Emergency integrity package | 0.600 | 0.646 | 0.019 | 0.073 | 0.076 | 0.259 | front-line cluster |
| High appointment-capture prior | Nonpartisan commission appointments | 0.600 | 0.639 | 0.082 | 0.078 | 0.089 | 0.264 | front-line cluster |
| High appointment-capture prior | Mandatory written emergency reasoning | 0.599 | 0.639 | 0.052 | 0.086 | 0.084 | 0.263 | front-line cluster |
| High appointment-capture prior | Three-judge panels with en banc correction | 0.599 | 0.642 | 0.083 | 0.079 | 0.088 | 0.263 | front-line cluster |
| High appointment-capture prior | Time-limited legislative override window | 0.598 | 0.643 | 0.081 | 0.079 | 0.086 | 0.263 | front-line cluster |
| High appointment-capture prior | Independent recusal enforcement with substitutes | 0.598 | 0.647 | 0.081 | 0.078 | 0.084 | 0.262 | front-line cluster |
| High appointment-capture prior | Peer recusal + reasoned emergency docket | 0.598 | 0.646 | 0.082 | 0.080 | 0.096 | 0.263 | front-line cluster |
| High appointment-capture prior | Constitutional remand before invalidation | 0.597 | 0.644 | 0.084 | 0.080 | 0.093 | 0.230 | rights-protection caveat |
| Low public-pressure prior | No emergency relief without merits review | 0.612 | 0.650 | 0.011 | 0.057 | 0.069 | 0.246 | front-line cluster |
| Low public-pressure prior | 60 percent invalidation threshold | 0.608 | 0.640 | 0.071 | 0.082 | 0.079 | 0.251 | rights-protection caveat |
| Low public-pressure prior | Jurisdiction stripping constrained by rights carveouts | 0.607 | 0.645 | 0.074 | 0.068 | 0.087 | 0.249 | front-line cluster |
| Low public-pressure prior | 18-year staggered terms + regular appointments | 0.607 | 0.643 | 0.077 | 0.071 | 0.086 | 0.251 | front-line cluster |
| Low public-pressure prior | Automatic merits follow-up for emergency relief | 0.606 | 0.650 | 0.017 | 0.066 | 0.075 | 0.247 | front-line cluster |
| Low public-pressure prior | Public-interest litigation filter | 0.606 | 0.651 | 0.075 | 0.069 | 0.076 | 0.249 | front-line cluster |
| Low public-pressure prior | Nonpartisan commission appointments | 0.604 | 0.643 | 0.075 | 0.071 | 0.079 | 0.250 | front-line cluster |
| Low public-pressure prior | Mandatory written emergency reasoning | 0.604 | 0.644 | 0.047 | 0.079 | 0.078 | 0.250 | front-line cluster |
| Low public-pressure prior | Peer recusal + reasoned emergency docket | 0.604 | 0.644 | 0.076 | 0.070 | 0.074 | 0.249 | front-line cluster |
| Low public-pressure prior | Retention-election accountability court | 0.603 | 0.641 | 0.075 | 0.068 | 0.086 | 0.250 | front-line cluster |
| Low public-pressure prior | Three-judge panels with en banc correction | 0.603 | 0.644 | 0.077 | 0.071 | 0.077 | 0.249 | front-line cluster |
| Low public-pressure prior | Constitutional remand before invalidation | 0.602 | 0.647 | 0.080 | 0.074 | 0.082 | 0.216 | rights-protection caveat |
| High public-pressure prior | No emergency relief without merits review | 0.608 | 0.649 | 0.012 | 0.064 | 0.084 | 0.250 | front-line cluster |
| High public-pressure prior | Jurisdiction stripping constrained by rights carveouts | 0.604 | 0.646 | 0.084 | 0.080 | 0.091 | 0.252 | front-line cluster |
| High public-pressure prior | 18-year staggered terms + regular appointments | 0.603 | 0.647 | 0.084 | 0.083 | 0.087 | 0.253 | front-line cluster |
| High public-pressure prior | 60 percent invalidation threshold | 0.603 | 0.635 | 0.073 | 0.092 | 0.086 | 0.254 | rights-protection caveat |
| High public-pressure prior | Automatic merits follow-up for emergency relief | 0.602 | 0.653 | 0.020 | 0.077 | 0.082 | 0.250 | front-line cluster |
| High public-pressure prior | Emergency integrity package | 0.602 | 0.654 | 0.020 | 0.077 | 0.070 | 0.248 | front-line cluster |
| High public-pressure prior | Public-interest litigation filter | 0.602 | 0.646 | 0.083 | 0.080 | 0.078 | 0.252 | front-line cluster |
| High public-pressure prior | Peer recusal + reasoned emergency docket | 0.600 | 0.644 | 0.082 | 0.079 | 0.091 | 0.254 | rights-protection caveat |
| High public-pressure prior | Mandatory written emergency reasoning | 0.600 | 0.641 | 0.053 | 0.091 | 0.086 | 0.253 | rights-protection caveat |
| High public-pressure prior | Judicial review with legislative supermajority override | 0.600 | 0.647 | 0.084 | 0.081 | 0.089 | 0.253 | front-line cluster |
| High public-pressure prior | Retention-election accountability court | 0.599 | 0.640 | 0.082 | 0.082 | 0.088 | 0.253 | front-line cluster |
| High public-pressure prior | Constitutional remand before invalidation | 0.599 | 0.638 | 0.089 | 0.085 | 0.076 | 0.218 | rights-protection caveat |
| High public-pressure prior | Nonpartisan commission appointments | 0.599 | 0.643 | 0.088 | 0.084 | 0.088 | 0.254 | rights-protection caveat |
| Low emergency-share prior | No emergency relief without merits review | 0.617 | 0.649 | 0.009 | 0.038 | 0.052 | 0.238 | front-line cluster |
| Low emergency-share prior | Jurisdiction stripping constrained by rights carveouts | 0.612 | 0.643 | 0.054 | 0.046 | 0.072 | 0.241 | front-line cluster |
| Low emergency-share prior | 18-year staggered terms + regular appointments | 0.612 | 0.645 | 0.063 | 0.051 | 0.073 | 0.243 | front-line cluster |
| Low emergency-share prior | 60 percent invalidation threshold | 0.611 | 0.634 | 0.054 | 0.058 | 0.073 | 0.244 | rights-protection caveat |
| Low emergency-share prior | Public-interest litigation filter | 0.610 | 0.648 | 0.061 | 0.050 | 0.072 | 0.242 | front-line cluster |
| Low emergency-share prior | Constitutional remand before invalidation | 0.610 | 0.636 | 0.060 | 0.049 | 0.062 | 0.208 | rights-protection caveat |
| Low emergency-share prior | Automatic merits follow-up for emergency relief | 0.609 | 0.645 | 0.014 | 0.045 | 0.077 | 0.242 | front-line cluster |
| Low emergency-share prior | Nonpartisan commission appointments | 0.609 | 0.642 | 0.066 | 0.052 | 0.071 | 0.243 | front-line cluster |
| Low emergency-share prior | Peer recusal + reasoned emergency docket | 0.608 | 0.642 | 0.060 | 0.050 | 0.073 | 0.243 | front-line cluster |
| Low emergency-share prior | Emergency integrity package | 0.608 | 0.650 | 0.014 | 0.045 | 0.073 | 0.240 | front-line cluster |
| Low emergency-share prior | Mandatory written emergency reasoning | 0.608 | 0.637 | 0.038 | 0.057 | 0.068 | 0.242 | front-line cluster |
| Low emergency-share prior | Retention-election accountability court | 0.608 | 0.641 | 0.063 | 0.051 | 0.081 | 0.244 | front-line cluster |
| Low emergency-share prior | Randomized merits panels with en banc correction | 0.607 | 0.643 | 0.058 | 0.050 | 0.064 | 0.242 | front-line cluster |
| Low emergency-share prior | Three-judge panels with en banc correction | 0.607 | 0.645 | 0.061 | 0.051 | 0.076 | 0.243 | front-line cluster |
| Low emergency-share prior | Constitutional remand with override window | 0.607 | 0.638 | 0.036 | 0.057 | 0.066 | 0.208 | rights-protection caveat |
| Low emergency-share prior | Judicial review with legislative supermajority override | 0.607 | 0.644 | 0.062 | 0.052 | 0.074 | 0.242 | front-line cluster |
| Low emergency-share prior | Time-limited legislative override window | 0.607 | 0.644 | 0.058 | 0.048 | 0.080 | 0.244 | front-line cluster |
| Low emergency-share prior | Expanded 15-seat court | 0.607 | 0.639 | 0.061 | 0.051 | 0.065 | 0.242 | front-line cluster |
| High emergency-share prior | 60 percent invalidation threshold | 0.517 | 0.617 | 0.179 | 0.263 | 0.230 | 0.405 | compliance caveat |
| High emergency-share prior | 18-year staggered terms + regular appointments | 0.516 | 0.623 | 0.187 | 0.230 | 0.219 | 0.401 | compliance caveat |
| High emergency-share prior | Public-interest litigation filter | 0.515 | 0.628 | 0.182 | 0.223 | 0.232 | 0.402 | compliance caveat |
| High emergency-share prior | Constitutional remand before invalidation | 0.514 | 0.625 | 0.190 | 0.233 | 0.240 | 0.367 | compliance caveat |
| High emergency-share prior | Jurisdiction stripping constrained by rights carveouts | 0.513 | 0.627 | 0.186 | 0.229 | 0.246 | 0.403 | compliance caveat |
| High emergency-share prior | Independent recusal enforcement with substitutes | 0.513 | 0.626 | 0.185 | 0.223 | 0.219 | 0.402 | compliance caveat |
| High emergency-share prior | Constitutional remand with override window | 0.513 | 0.617 | 0.142 | 0.251 | 0.235 | 0.369 | compliance caveat |
| High emergency-share prior | Mandatory written emergency reasoning | 0.512 | 0.612 | 0.145 | 0.254 | 0.227 | 0.404 | compliance caveat |
| High emergency-share prior | Three-judge panels with en banc correction | 0.512 | 0.632 | 0.188 | 0.232 | 0.232 | 0.402 | compliance caveat |
| High emergency-share prior | No emergency relief without merits review | 0.512 | 0.648 | 0.049 | 0.184 | 0.248 | 0.397 | compliance caveat |
| High emergency-share prior | Nonpartisan commission appointments | 0.511 | 0.624 | 0.185 | 0.228 | 0.225 | 0.402 | compliance caveat |
| High emergency-share prior | Retention-election accountability court | 0.511 | 0.615 | 0.182 | 0.224 | 0.243 | 0.404 | compliance caveat |
| High emergency-share prior | Comparative 16-seat constitutional senates | 0.510 | 0.615 | 0.178 | 0.258 | 0.229 | 0.406 | rights-protection caveat |
| High emergency-share prior | Constitutional council with concrete-review backstop | 0.509 | 0.630 | 0.185 | 0.223 | 0.231 | 0.400 | compliance caveat |
| High emergency-share prior | Peer recusal + reasoned emergency docket | 0.509 | 0.629 | 0.192 | 0.232 | 0.256 | 0.406 | compliance caveat |
| High emergency-share prior | Randomized merits panels with en banc correction | 0.508 | 0.620 | 0.185 | 0.227 | 0.260 | 0.407 | compliance caveat |
| High emergency-share prior | Time-limited legislative override window | 0.508 | 0.623 | 0.187 | 0.228 | 0.245 | 0.404 | compliance caveat |
| High emergency-share prior | Emergency integrity package | 0.508 | 0.642 | 0.060 | 0.185 | 0.230 | 0.395 | compliance caveat |
| Low rights-risk prior | No emergency relief without merits review | 0.637 | 0.652 | 0.005 | 0.039 | 0.039 | 0.175 | rights-protection caveat |
| Low rights-risk prior | Jurisdiction stripping constrained by rights carveouts | 0.637 | 0.644 | 0.052 | 0.042 | 0.030 | 0.175 | rights-protection caveat |
| Low rights-risk prior | 60 percent invalidation threshold | 0.636 | 0.642 | 0.047 | 0.051 | 0.027 | 0.177 | rights-protection caveat |
| Low rights-risk prior | 18-year staggered terms + regular appointments | 0.635 | 0.649 | 0.054 | 0.046 | 0.038 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Nonpartisan commission appointments | 0.634 | 0.653 | 0.059 | 0.049 | 0.031 | 0.176 | rights-protection caveat |
| Low rights-risk prior | Automatic merits follow-up for emergency relief | 0.634 | 0.649 | 0.009 | 0.047 | 0.028 | 0.175 | rights-protection caveat |
| Low rights-risk prior | Mandatory written emergency reasoning | 0.633 | 0.650 | 0.032 | 0.050 | 0.030 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Retention-election accountability court | 0.633 | 0.643 | 0.055 | 0.046 | 0.034 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Randomized merits panels with en banc correction | 0.632 | 0.648 | 0.054 | 0.045 | 0.029 | 0.176 | rights-protection caveat |
| Low rights-risk prior | Emergency integrity package | 0.632 | 0.652 | 0.010 | 0.050 | 0.031 | 0.175 | rights-protection caveat |
| Low rights-risk prior | Peer recusal + reasoned emergency docket | 0.632 | 0.646 | 0.055 | 0.045 | 0.037 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Three-judge panels with en banc correction | 0.632 | 0.656 | 0.055 | 0.044 | 0.040 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Time-limited legislative override window | 0.632 | 0.649 | 0.055 | 0.046 | 0.038 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Public-interest litigation filter | 0.631 | 0.651 | 0.054 | 0.046 | 0.042 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Constitutional remand before invalidation | 0.631 | 0.642 | 0.054 | 0.045 | 0.029 | 0.145 | rights-protection caveat |
| Low rights-risk prior | Judicial review with legislative supermajority override | 0.631 | 0.655 | 0.057 | 0.048 | 0.032 | 0.176 | rights-protection caveat |
| Low rights-risk prior | Independent recusal enforcement with substitutes | 0.631 | 0.650 | 0.053 | 0.046 | 0.036 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Random panels with jurisdiction safeguards | 0.628 | 0.647 | 0.047 | 0.051 | 0.041 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Expanded 15-seat court | 0.628 | 0.651 | 0.056 | 0.046 | 0.042 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Pre-enactment constitutional council | 0.627 | 0.647 | 0.059 | 0.047 | 0.036 | 0.175 | rights-protection caveat |
| High rights-risk prior | 60 percent invalidation threshold | 0.525 | 0.558 | 0.119 | 0.167 | 0.223 | 0.404 | compliance caveat |
| High rights-risk prior | Constitutional remand before invalidation | 0.524 | 0.570 | 0.120 | 0.135 | 0.225 | 0.363 | compliance caveat |
| High rights-risk prior | Automatic merits follow-up for emergency relief | 0.523 | 0.600 | 0.035 | 0.081 | 0.234 | 0.399 | compliance caveat |
| High rights-risk prior | 18-year staggered terms + regular appointments | 0.523 | 0.573 | 0.125 | 0.138 | 0.225 | 0.403 | compliance caveat |
| High rights-risk prior | No emergency relief without merits review | 0.521 | 0.606 | 0.028 | 0.102 | 0.249 | 0.400 | compliance caveat |
| High rights-risk prior | Emergency integrity package | 0.520 | 0.602 | 0.036 | 0.082 | 0.235 | 0.399 | compliance caveat |
| High rights-risk prior | Expanded 15-seat court | 0.520 | 0.571 | 0.118 | 0.132 | 0.217 | 0.402 | compliance caveat |
| High rights-risk prior | Constitutional remand with override window | 0.519 | 0.554 | 0.094 | 0.164 | 0.237 | 0.366 | compliance caveat |
| High rights-risk prior | Peer recusal + reasoned emergency docket | 0.519 | 0.580 | 0.121 | 0.136 | 0.235 | 0.403 | compliance caveat |
| High rights-risk prior | Three-judge panels with en banc correction | 0.517 | 0.574 | 0.124 | 0.138 | 0.217 | 0.401 | compliance caveat |
| High rights-risk prior | Nonpartisan commission appointments | 0.517 | 0.577 | 0.127 | 0.140 | 0.249 | 0.405 | compliance caveat |
| High rights-risk prior | Randomized merits panels with en banc correction | 0.517 | 0.582 | 0.122 | 0.136 | 0.237 | 0.403 | compliance caveat |
| High rights-risk prior | Mandatory written emergency reasoning | 0.516 | 0.570 | 0.094 | 0.164 | 0.232 | 0.404 | compliance caveat |
| High rights-risk prior | Independent recusal enforcement with substitutes | 0.516 | 0.575 | 0.125 | 0.140 | 0.227 | 0.403 | compliance caveat |
| High rights-risk prior | Public-interest litigation filter | 0.516 | 0.585 | 0.123 | 0.138 | 0.224 | 0.401 | compliance caveat |
| Weak democratic-mandate prior | Constitutional remand before invalidation | 0.540 | 0.617 | 0.108 | 0.111 | 0.176 | 0.337 | compliance caveat |
| Weak democratic-mandate prior | 60 percent invalidation threshold | 0.539 | 0.608 | 0.098 | 0.133 | 0.203 | 0.379 | compliance caveat |
| Weak democratic-mandate prior | 18-year staggered terms + regular appointments | 0.537 | 0.615 | 0.107 | 0.109 | 0.190 | 0.377 | compliance caveat |
| Weak democratic-mandate prior | Constitutional remand with override window | 0.535 | 0.618 | 0.075 | 0.128 | 0.196 | 0.340 | compliance caveat |
| Weak democratic-mandate prior | No emergency relief without merits review | 0.535 | 0.623 | 0.020 | 0.084 | 0.196 | 0.373 | compliance caveat |
| Weak democratic-mandate prior | Public-interest litigation filter | 0.534 | 0.621 | 0.102 | 0.109 | 0.190 | 0.376 | compliance caveat |
| Weak democratic-mandate prior | Mandatory written emergency reasoning | 0.534 | 0.611 | 0.078 | 0.129 | 0.181 | 0.376 | compliance caveat |
| Weak democratic-mandate prior | Nonpartisan commission appointments | 0.532 | 0.615 | 0.106 | 0.112 | 0.201 | 0.378 | compliance caveat |
| Weak democratic-mandate prior | Comparative 16-seat constitutional senates | 0.532 | 0.612 | 0.100 | 0.133 | 0.196 | 0.378 | compliance caveat |
| Weak democratic-mandate prior | Expanded 15-seat court | 0.532 | 0.611 | 0.108 | 0.113 | 0.176 | 0.375 | compliance caveat |
| Weak democratic-mandate prior | Jurisdiction stripping constrained by rights carveouts | 0.532 | 0.616 | 0.106 | 0.110 | 0.215 | 0.378 | compliance caveat |
| Weak democratic-mandate prior | Peer recusal + reasoned emergency docket | 0.532 | 0.616 | 0.108 | 0.114 | 0.199 | 0.377 | compliance caveat |
| Weak democratic-mandate prior | Automatic merits follow-up for emergency relief | 0.531 | 0.623 | 0.029 | 0.075 | 0.202 | 0.374 | compliance caveat |
| High constitutional-conflict prior | 60 percent invalidation threshold | 0.514 | 0.605 | 0.145 | 0.194 | 0.231 | 0.438 | compliance caveat |
| High constitutional-conflict prior | Constitutional remand before invalidation | 0.506 | 0.620 | 0.158 | 0.172 | 0.253 | 0.400 | compliance caveat |
| High constitutional-conflict prior | Constitutional remand with override window | 0.504 | 0.611 | 0.120 | 0.197 | 0.262 | 0.402 | compliance caveat |
| Imported legislative-family prior | No emergency relief without merits review | 0.618 | 0.653 | 0.008 | 0.054 | 0.070 | 0.230 | rights-protection caveat |
| Imported legislative-family prior | 18-year staggered terms + regular appointments | 0.616 | 0.643 | 0.070 | 0.067 | 0.053 | 0.231 | rights-protection caveat |
| Imported legislative-family prior | Jurisdiction stripping constrained by rights carveouts | 0.613 | 0.653 | 0.076 | 0.071 | 0.084 | 0.232 | rights-protection caveat |
| Imported legislative-family prior | 60 percent invalidation threshold | 0.613 | 0.644 | 0.062 | 0.078 | 0.069 | 0.234 | rights-protection caveat |
| Imported legislative-family prior | Automatic merits follow-up for emergency relief | 0.612 | 0.656 | 0.016 | 0.069 | 0.064 | 0.229 | front-line cluster |
| Imported legislative-family prior | Emergency integrity package | 0.611 | 0.661 | 0.016 | 0.068 | 0.078 | 0.230 | front-line cluster |
| Imported legislative-family prior | Public-interest litigation filter | 0.611 | 0.652 | 0.073 | 0.069 | 0.071 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Three-judge panels with en banc correction | 0.610 | 0.649 | 0.071 | 0.067 | 0.066 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Retention-election accountability court | 0.610 | 0.646 | 0.075 | 0.068 | 0.070 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Nonpartisan commission appointments | 0.610 | 0.649 | 0.077 | 0.069 | 0.076 | 0.234 | rights-protection caveat |
| Imported legislative-family prior | Mandatory written emergency reasoning | 0.610 | 0.651 | 0.045 | 0.075 | 0.071 | 0.232 | rights-protection caveat |
| Imported legislative-family prior | Constitutional remand before invalidation | 0.609 | 0.646 | 0.076 | 0.069 | 0.061 | 0.198 | rights-protection caveat |
| Imported legislative-family prior | Time-limited legislative override window | 0.608 | 0.651 | 0.069 | 0.066 | 0.074 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Judicial review with legislative supermajority override | 0.608 | 0.650 | 0.075 | 0.070 | 0.071 | 0.233 | rights-protection caveat |
