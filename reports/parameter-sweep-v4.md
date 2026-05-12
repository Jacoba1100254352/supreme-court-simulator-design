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
| No emergency relief without merits review | 0.512 / 0.609 / 0.625 | 0.457 / 0.661 / 0.693 | 0.613 / 0.643 / 0.650 | 0.007 / 0.011 / 0.043 | 0.339 / 0.373 / 0.593 | 0.168 / 0.189 / 0.316 |
| 18-year staggered terms + regular appointments | 0.515 / 0.606 / 0.621 | 0.499 / 0.661 / 0.691 | 0.595 / 0.638 / 0.645 | 0.059 / 0.078 / 0.160 | 0.338 / 0.380 / 0.590 | 0.183 / 0.207 / 0.327 |
| 60 percent invalidation threshold | 0.516 / 0.605 / 0.622 | 0.524 / 0.667 / 0.694 | 0.583 / 0.630 / 0.638 | 0.048 / 0.069 / 0.154 | 0.340 / 0.381 / 0.593 | 0.180 / 0.206 / 0.326 |
| Automatic merits follow-up for emergency relief | 0.503 / 0.605 / 0.620 | 0.458 / 0.656 / 0.690 | 0.610 / 0.641 / 0.650 | 0.012 / 0.017 / 0.053 | 0.338 / 0.375 / 0.596 | 0.177 / 0.201 / 0.327 |
| Jurisdiction stripping constrained by rights carveouts | 0.511 / 0.604 / 0.622 | 0.485 / 0.659 / 0.689 | 0.599 / 0.638 / 0.644 | 0.055 / 0.075 / 0.163 | 0.344 / 0.388 / 0.607 | 0.169 / 0.201 / 0.329 |
| Emergency integrity package | 0.507 / 0.603 / 0.618 | 0.461 / 0.662 / 0.693 | 0.612 / 0.644 / 0.649 | 0.012 / 0.018 / 0.053 | 0.340 / 0.379 / 0.587 | 0.168 / 0.194 / 0.316 |
| Public-interest litigation filter | 0.514 / 0.603 / 0.618 | 0.501 / 0.664 / 0.693 | 0.603 / 0.642 / 0.648 | 0.057 / 0.077 / 0.161 | 0.340 / 0.382 / 0.586 | 0.169 / 0.195 / 0.311 |
| Nonpartisan commission appointments | 0.508 / 0.603 / 0.619 | 0.489 / 0.660 / 0.691 | 0.597 / 0.638 / 0.645 | 0.058 / 0.075 / 0.164 | 0.342 / 0.382 / 0.594 | 0.173 / 0.199 / 0.323 |
| Peer recusal + reasoned emergency docket | 0.510 / 0.603 / 0.618 | 0.492 / 0.662 / 0.693 | 0.595 / 0.637 / 0.645 | 0.058 / 0.077 / 0.161 | 0.342 / 0.380 / 0.590 | 0.183 / 0.205 / 0.327 |
| Mandatory written emergency reasoning | 0.509 / 0.602 / 0.618 | 0.501 / 0.664 / 0.692 | 0.594 / 0.634 / 0.645 | 0.032 / 0.049 / 0.123 | 0.336 / 0.381 / 0.591 | 0.178 / 0.206 / 0.325 |
| Three-judge panels with en banc correction | 0.508 / 0.602 / 0.617 | 0.499 / 0.663 / 0.691 | 0.595 / 0.636 / 0.646 | 0.057 / 0.078 / 0.164 | 0.340 / 0.380 / 0.594 | 0.172 / 0.197 / 0.320 |
| Constitutional remand before invalidation | 0.514 / 0.601 / 0.617 | 0.541 / 0.682 / 0.708 | 0.597 / 0.635 / 0.641 | 0.056 / 0.077 / 0.164 | 0.337 / 0.380 / 0.591 | 0.169 / 0.194 / 0.312 |
| Time-limited legislative override window | 0.506 / 0.601 / 0.616 | 0.487 / 0.658 / 0.688 | 0.597 / 0.637 / 0.643 | 0.057 / 0.078 / 0.161 | 0.352 / 0.393 / 0.615 | 0.179 / 0.204 / 0.331 |
| Retention-election accountability court | 0.510 / 0.600 / 0.618 | 0.497 / 0.662 / 0.692 | 0.580 / 0.634 / 0.638 | 0.057 / 0.077 / 0.156 | 0.346 / 0.391 / 0.604 | 0.176 / 0.203 / 0.320 |
| Expanded 15-seat court | 0.505 / 0.600 / 0.615 | 0.495 / 0.661 / 0.690 | 0.595 / 0.636 / 0.644 | 0.056 / 0.076 / 0.162 | 0.341 / 0.379 / 0.596 | 0.181 / 0.206 / 0.330 |
| Independent recusal enforcement with substitutes | 0.509 / 0.599 / 0.616 | 0.493 / 0.661 / 0.692 | 0.594 / 0.638 / 0.643 | 0.057 / 0.077 / 0.163 | 0.341 / 0.381 / 0.590 | 0.176 / 0.201 / 0.320 |
| Randomized merits panels with en banc correction | 0.507 / 0.599 / 0.617 | 0.500 / 0.662 / 0.693 | 0.595 / 0.635 / 0.646 | 0.056 / 0.078 / 0.159 | 0.342 / 0.380 / 0.588 | 0.175 / 0.198 / 0.315 |
| Judicial review with legislative supermajority override | 0.504 / 0.599 / 0.616 | 0.478 / 0.656 / 0.686 | 0.600 / 0.637 / 0.646 | 0.054 / 0.077 / 0.164 | 0.351 / 0.395 / 0.623 | 0.181 / 0.209 / 0.337 |
| Constitutional remand with override window | 0.511 / 0.599 / 0.613 | 0.549 / 0.686 / 0.705 | 0.591 / 0.634 / 0.639 | 0.034 / 0.050 / 0.125 | 0.340 / 0.381 / 0.591 | 0.170 / 0.194 / 0.315 |
| Random panels with jurisdiction safeguards | 0.504 / 0.599 / 0.613 | 0.510 / 0.664 / 0.690 | 0.583 / 0.631 / 0.639 | 0.051 / 0.069 / 0.152 | 0.347 / 0.388 / 0.604 | 0.173 / 0.196 / 0.324 |
| Pre-enactment constitutional council | 0.504 / 0.598 / 0.614 | 0.495 / 0.669 / 0.697 | 0.606 / 0.638 / 0.643 | 0.056 / 0.075 / 0.162 | 0.350 / 0.390 / 0.617 | 0.178 / 0.204 / 0.326 |
| Constitutional council with concrete-review backstop | 0.500 / 0.595 / 0.611 | 0.500 / 0.671 / 0.698 | 0.604 / 0.637 / 0.640 | 0.056 / 0.075 / 0.163 | 0.347 / 0.387 / 0.615 | 0.176 / 0.203 / 0.329 |
| Judicial electorate selection court | 0.499 / 0.595 / 0.612 | 0.489 / 0.662 / 0.694 | 0.599 / 0.639 / 0.646 | 0.056 / 0.077 / 0.163 | 0.341 / 0.384 / 0.595 | 0.170 / 0.195 / 0.320 |
| Comparative 16-seat constitutional senates | 0.509 / 0.595 / 0.611 | 0.523 / 0.672 / 0.698 | 0.583 / 0.627 / 0.635 | 0.052 / 0.068 / 0.150 | 0.339 / 0.378 / 0.589 | 0.174 / 0.199 / 0.320 |
| Stylized current U.S.-like supreme court | 0.499 / 0.590 / 0.608 | 0.495 / 0.655 / 0.680 | 0.611 / 0.640 / 0.650 | 0.181 / 0.239 / 0.420 | 0.362 / 0.408 / 0.640 | 0.204 / 0.234 / 0.365 |
| Supreme court with cross-checking constitutional court | 0.496 / 0.586 / 0.603 | 0.529 / 0.662 / 0.689 | 0.564 / 0.619 / 0.630 | 0.051 / 0.068 / 0.154 | 0.360 / 0.401 / 0.619 | 0.175 / 0.197 / 0.317 |
| Dual supreme courts with disagreement filter | 0.475 / 0.575 / 0.595 | 0.468 / 0.639 / 0.675 | 0.594 / 0.634 / 0.644 | 0.049 / 0.068 / 0.152 | 0.369 / 0.413 / 0.624 | 0.180 / 0.207 / 0.327 |

## What Would Change the Interpretation

The table below reports each named prior's top directional-score cluster within 0.010 of that prior's best score. A design conclusion should weaken if it appears only under one narrow prior, if its cluster membership depends on high emergency pressure or high conflict, or if its apparent advantage comes with rights-protection, compliance, or emergency-power caveats.

| Prior | Cluster scenario | Score | Rights | Shadow | Emerg. downstream | Gov. noncomp. | Lower-court resistance | Caveat |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Baseline institutional prior | No emergency relief without merits review | 0.610 | 0.646 | 0.011 | 0.055 | 0.071 | 0.244 | front-line cluster |
| Baseline institutional prior | 60 percent invalidation threshold | 0.608 | 0.633 | 0.064 | 0.079 | 0.070 | 0.248 | rights-protection caveat |
| Baseline institutional prior | Automatic merits follow-up for emergency relief | 0.607 | 0.647 | 0.016 | 0.060 | 0.072 | 0.245 | front-line cluster |
| Baseline institutional prior | 18-year staggered terms + regular appointments | 0.607 | 0.645 | 0.078 | 0.070 | 0.081 | 0.248 | front-line cluster |
| Baseline institutional prior | Jurisdiction stripping constrained by rights carveouts | 0.606 | 0.639 | 0.072 | 0.069 | 0.084 | 0.247 | front-line cluster |
| Baseline institutional prior | Public-interest litigation filter | 0.605 | 0.647 | 0.074 | 0.070 | 0.071 | 0.247 | front-line cluster |
| Baseline institutional prior | Mandatory written emergency reasoning | 0.604 | 0.645 | 0.048 | 0.078 | 0.078 | 0.247 | front-line cluster |
| Baseline institutional prior | Peer recusal + reasoned emergency docket | 0.604 | 0.644 | 0.074 | 0.070 | 0.069 | 0.246 | front-line cluster |
| Baseline institutional prior | Nonpartisan commission appointments | 0.604 | 0.637 | 0.072 | 0.068 | 0.076 | 0.248 | front-line cluster |
| Baseline institutional prior | Emergency integrity package | 0.604 | 0.646 | 0.018 | 0.065 | 0.069 | 0.244 | front-line cluster |
| Baseline institutional prior | Constitutional remand before invalidation | 0.603 | 0.637 | 0.074 | 0.068 | 0.072 | 0.214 | rights-protection caveat |
| Baseline institutional prior | Three-judge panels with en banc correction | 0.603 | 0.643 | 0.077 | 0.072 | 0.069 | 0.246 | front-line cluster |
| Baseline institutional prior | Time-limited legislative override window | 0.602 | 0.641 | 0.074 | 0.069 | 0.084 | 0.249 | front-line cluster |
| Baseline institutional prior | Independent recusal enforcement with substitutes | 0.602 | 0.641 | 0.072 | 0.070 | 0.072 | 0.247 | front-line cluster |
| Baseline institutional prior | Randomized merits panels with en banc correction | 0.601 | 0.645 | 0.076 | 0.071 | 0.079 | 0.248 | front-line cluster |
| Baseline institutional prior | Constitutional remand with override window | 0.601 | 0.634 | 0.048 | 0.077 | 0.078 | 0.214 | rights-protection caveat |
| Baseline institutional prior | Retention-election accountability court | 0.600 | 0.637 | 0.076 | 0.073 | 0.093 | 0.249 | front-line cluster |
| Low-polarization prior | No emergency relief without merits review | 0.612 | 0.639 | 0.010 | 0.052 | 0.067 | 0.240 | front-line cluster |
| Low-polarization prior | 60 percent invalidation threshold | 0.609 | 0.628 | 0.060 | 0.071 | 0.075 | 0.244 | rights-protection caveat |
| Low-polarization prior | Jurisdiction stripping constrained by rights carveouts | 0.608 | 0.633 | 0.069 | 0.063 | 0.073 | 0.242 | front-line cluster |
| Low-polarization prior | 18-year staggered terms + regular appointments | 0.608 | 0.631 | 0.071 | 0.065 | 0.074 | 0.243 | front-line cluster |
| Low-polarization prior | Public-interest litigation filter | 0.608 | 0.637 | 0.068 | 0.062 | 0.063 | 0.242 | front-line cluster |
| Low-polarization prior | Constitutional remand before invalidation | 0.606 | 0.629 | 0.068 | 0.061 | 0.060 | 0.209 | rights-protection caveat |
| Low-polarization prior | Automatic merits follow-up for emergency relief | 0.606 | 0.640 | 0.016 | 0.055 | 0.065 | 0.241 | front-line cluster |
| Low-polarization prior | Peer recusal + reasoned emergency docket | 0.605 | 0.637 | 0.071 | 0.063 | 0.078 | 0.244 | front-line cluster |
| Low-polarization prior | Nonpartisan commission appointments | 0.605 | 0.637 | 0.070 | 0.062 | 0.080 | 0.244 | front-line cluster |
| Low-polarization prior | Retention-election accountability court | 0.605 | 0.634 | 0.072 | 0.065 | 0.071 | 0.243 | front-line cluster |
| Low-polarization prior | Randomized merits panels with en banc correction | 0.604 | 0.635 | 0.074 | 0.065 | 0.066 | 0.243 | front-line cluster |
| Low-polarization prior | Three-judge panels with en banc correction | 0.603 | 0.631 | 0.073 | 0.066 | 0.076 | 0.244 | front-line cluster |
| Low-polarization prior | Mandatory written emergency reasoning | 0.603 | 0.633 | 0.043 | 0.070 | 0.068 | 0.243 | front-line cluster |
| Low-polarization prior | Emergency integrity package | 0.603 | 0.641 | 0.016 | 0.058 | 0.078 | 0.241 | front-line cluster |
| Low-polarization prior | Constitutional remand with override window | 0.603 | 0.629 | 0.047 | 0.074 | 0.066 | 0.208 | rights-protection caveat |
| Low-polarization prior | Independent recusal enforcement with substitutes | 0.603 | 0.637 | 0.070 | 0.065 | 0.074 | 0.243 | front-line cluster |
| Low-polarization prior | Time-limited legislative override window | 0.603 | 0.641 | 0.076 | 0.068 | 0.077 | 0.243 | front-line cluster |
| Low-polarization prior | Random panels with jurisdiction safeguards | 0.602 | 0.632 | 0.058 | 0.072 | 0.075 | 0.243 | front-line cluster |
| Low-polarization prior | Expanded 15-seat court | 0.602 | 0.632 | 0.068 | 0.063 | 0.074 | 0.244 | front-line cluster |
| High-polarization prior | No emergency relief without merits review | 0.608 | 0.643 | 0.011 | 0.058 | 0.077 | 0.263 | front-line cluster |
| High-polarization prior | Jurisdiction stripping constrained by rights carveouts | 0.602 | 0.638 | 0.079 | 0.077 | 0.074 | 0.263 | front-line cluster |
| High-polarization prior | Automatic merits follow-up for emergency relief | 0.602 | 0.643 | 0.018 | 0.068 | 0.079 | 0.263 | front-line cluster |
| High-polarization prior | 60 percent invalidation threshold | 0.601 | 0.626 | 0.072 | 0.086 | 0.081 | 0.268 | rights-protection caveat |
| High-polarization prior | 18-year staggered terms + regular appointments | 0.601 | 0.640 | 0.077 | 0.075 | 0.096 | 0.267 | front-line cluster |
| High-polarization prior | Emergency integrity package | 0.600 | 0.645 | 0.018 | 0.069 | 0.073 | 0.262 | front-line cluster |
| High-polarization prior | Constitutional remand before invalidation | 0.599 | 0.638 | 0.079 | 0.078 | 0.074 | 0.229 | rights-protection caveat |
| High-polarization prior | Public-interest litigation filter | 0.599 | 0.642 | 0.079 | 0.077 | 0.078 | 0.265 | front-line cluster |
| High-polarization prior | Retention-election accountability court | 0.598 | 0.630 | 0.077 | 0.077 | 0.081 | 0.265 | rights-protection caveat |
| Low appointment-capture prior | No emergency relief without merits review | 0.612 | 0.644 | 0.010 | 0.051 | 0.081 | 0.239 | front-line cluster |
| Low appointment-capture prior | 60 percent invalidation threshold | 0.611 | 0.629 | 0.064 | 0.070 | 0.063 | 0.241 | rights-protection caveat |
| Low appointment-capture prior | Jurisdiction stripping constrained by rights carveouts | 0.610 | 0.637 | 0.069 | 0.061 | 0.079 | 0.240 | front-line cluster |
| Low appointment-capture prior | Emergency integrity package | 0.609 | 0.641 | 0.016 | 0.056 | 0.059 | 0.236 | front-line cluster |
| Low appointment-capture prior | Nonpartisan commission appointments | 0.609 | 0.640 | 0.069 | 0.063 | 0.063 | 0.238 | front-line cluster |
| Low appointment-capture prior | Automatic merits follow-up for emergency relief | 0.608 | 0.639 | 0.016 | 0.057 | 0.073 | 0.238 | front-line cluster |
| Low appointment-capture prior | Constitutional remand before invalidation | 0.608 | 0.629 | 0.066 | 0.061 | 0.070 | 0.206 | rights-protection caveat |
| Low appointment-capture prior | 18-year staggered terms + regular appointments | 0.608 | 0.637 | 0.072 | 0.061 | 0.083 | 0.243 | front-line cluster |
| Low appointment-capture prior | Public-interest litigation filter | 0.607 | 0.651 | 0.073 | 0.065 | 0.070 | 0.238 | front-line cluster |
| Low appointment-capture prior | Mandatory written emergency reasoning | 0.607 | 0.634 | 0.043 | 0.069 | 0.065 | 0.239 | front-line cluster |
| Low appointment-capture prior | Constitutional remand with override window | 0.607 | 0.634 | 0.040 | 0.066 | 0.067 | 0.205 | administrative-cost caveat |
| Low appointment-capture prior | Peer recusal + reasoned emergency docket | 0.607 | 0.635 | 0.068 | 0.060 | 0.067 | 0.240 | front-line cluster |
| Low appointment-capture prior | Retention-election accountability court | 0.605 | 0.629 | 0.068 | 0.060 | 0.078 | 0.241 | front-line cluster |
| Low appointment-capture prior | Randomized merits panels with en banc correction | 0.605 | 0.630 | 0.071 | 0.062 | 0.065 | 0.240 | rights-protection caveat |
| Low appointment-capture prior | Independent recusal enforcement with substitutes | 0.604 | 0.638 | 0.069 | 0.062 | 0.074 | 0.241 | front-line cluster |
| Low appointment-capture prior | Time-limited legislative override window | 0.604 | 0.635 | 0.067 | 0.059 | 0.070 | 0.240 | front-line cluster |
| Low appointment-capture prior | Expanded 15-seat court | 0.604 | 0.634 | 0.071 | 0.063 | 0.071 | 0.240 | front-line cluster |
| Low appointment-capture prior | Judicial review with legislative supermajority override | 0.604 | 0.637 | 0.069 | 0.062 | 0.073 | 0.240 | front-line cluster |
| Low appointment-capture prior | Three-judge panels with en banc correction | 0.604 | 0.633 | 0.071 | 0.063 | 0.079 | 0.241 | front-line cluster |
| Low appointment-capture prior | Random panels with jurisdiction safeguards | 0.602 | 0.626 | 0.060 | 0.068 | 0.082 | 0.241 | rights-protection caveat |
| High appointment-capture prior | No emergency relief without merits review | 0.608 | 0.641 | 0.011 | 0.059 | 0.074 | 0.260 | front-line cluster |
| High appointment-capture prior | Automatic merits follow-up for emergency relief | 0.603 | 0.645 | 0.017 | 0.066 | 0.079 | 0.261 | front-line cluster |
| High appointment-capture prior | 18-year staggered terms + regular appointments | 0.603 | 0.635 | 0.080 | 0.075 | 0.076 | 0.263 | rights-protection caveat |
| High appointment-capture prior | 60 percent invalidation threshold | 0.602 | 0.630 | 0.076 | 0.090 | 0.082 | 0.265 | rights-protection caveat |
| High appointment-capture prior | Emergency integrity package | 0.601 | 0.646 | 0.018 | 0.071 | 0.070 | 0.259 | front-line cluster |
| High appointment-capture prior | Nonpartisan commission appointments | 0.601 | 0.641 | 0.077 | 0.076 | 0.076 | 0.262 | front-line cluster |
| High appointment-capture prior | Mandatory written emergency reasoning | 0.601 | 0.634 | 0.052 | 0.083 | 0.073 | 0.263 | rights-protection caveat |
| High appointment-capture prior | Peer recusal + reasoned emergency docket | 0.600 | 0.640 | 0.079 | 0.075 | 0.083 | 0.263 | front-line cluster |
| High appointment-capture prior | Three-judge panels with en banc correction | 0.600 | 0.635 | 0.079 | 0.075 | 0.070 | 0.262 | rights-protection caveat |
| High appointment-capture prior | Public-interest litigation filter | 0.600 | 0.641 | 0.083 | 0.079 | 0.083 | 0.264 | front-line cluster |
| High appointment-capture prior | Jurisdiction stripping constrained by rights carveouts | 0.600 | 0.638 | 0.081 | 0.078 | 0.104 | 0.264 | front-line cluster |
| High appointment-capture prior | Constitutional remand before invalidation | 0.600 | 0.632 | 0.079 | 0.075 | 0.087 | 0.230 | rights-protection caveat |
| High appointment-capture prior | Judicial review with legislative supermajority override | 0.599 | 0.642 | 0.078 | 0.075 | 0.080 | 0.263 | front-line cluster |
| High appointment-capture prior | Retention-election accountability court | 0.599 | 0.634 | 0.081 | 0.076 | 0.085 | 0.264 | front-line cluster |
| Low public-pressure prior | No emergency relief without merits review | 0.610 | 0.647 | 0.010 | 0.056 | 0.075 | 0.247 | front-line cluster |
| Low public-pressure prior | 18-year staggered terms + regular appointments | 0.608 | 0.640 | 0.078 | 0.071 | 0.073 | 0.250 | rights-protection caveat |
| Low public-pressure prior | Automatic merits follow-up for emergency relief | 0.607 | 0.646 | 0.017 | 0.064 | 0.070 | 0.247 | front-line cluster |
| Low public-pressure prior | Jurisdiction stripping constrained by rights carveouts | 0.607 | 0.639 | 0.072 | 0.068 | 0.080 | 0.249 | front-line cluster |
| Low public-pressure prior | 60 percent invalidation threshold | 0.606 | 0.636 | 0.067 | 0.080 | 0.080 | 0.252 | rights-protection caveat |
| Low public-pressure prior | Mandatory written emergency reasoning | 0.605 | 0.636 | 0.048 | 0.076 | 0.067 | 0.249 | rights-protection caveat |
| Low public-pressure prior | Public-interest litigation filter | 0.605 | 0.646 | 0.074 | 0.068 | 0.078 | 0.250 | front-line cluster |
| Low public-pressure prior | Nonpartisan commission appointments | 0.605 | 0.638 | 0.073 | 0.069 | 0.071 | 0.249 | rights-protection caveat |
| Low public-pressure prior | Emergency integrity package | 0.603 | 0.648 | 0.017 | 0.067 | 0.070 | 0.246 | front-line cluster |
| Low public-pressure prior | Peer recusal + reasoned emergency docket | 0.603 | 0.638 | 0.075 | 0.069 | 0.067 | 0.250 | front-line cluster |
| Low public-pressure prior | Three-judge panels with en banc correction | 0.603 | 0.642 | 0.074 | 0.070 | 0.080 | 0.250 | rights-protection caveat |
| Low public-pressure prior | Judicial review with legislative supermajority override | 0.602 | 0.643 | 0.074 | 0.068 | 0.073 | 0.250 | front-line cluster |
| Low public-pressure prior | Constitutional remand before invalidation | 0.602 | 0.640 | 0.076 | 0.069 | 0.073 | 0.216 | rights-protection caveat |
| Low public-pressure prior | Retention-election accountability court | 0.602 | 0.634 | 0.077 | 0.069 | 0.082 | 0.251 | rights-protection caveat |
| Low public-pressure prior | Time-limited legislative override window | 0.601 | 0.637 | 0.075 | 0.069 | 0.091 | 0.252 | rights-protection caveat |
| Low public-pressure prior | Expanded 15-seat court | 0.601 | 0.641 | 0.074 | 0.070 | 0.074 | 0.250 | front-line cluster |
| Low public-pressure prior | Randomized merits panels with en banc correction | 0.600 | 0.640 | 0.078 | 0.071 | 0.077 | 0.250 | rights-protection caveat |
| Low public-pressure prior | Random panels with jurisdiction safeguards | 0.600 | 0.633 | 0.069 | 0.080 | 0.077 | 0.250 | rights-protection caveat |
| High public-pressure prior | No emergency relief without merits review | 0.607 | 0.648 | 0.012 | 0.064 | 0.083 | 0.251 | front-line cluster |
| High public-pressure prior | 18-year staggered terms + regular appointments | 0.605 | 0.643 | 0.080 | 0.078 | 0.073 | 0.252 | front-line cluster |
| High public-pressure prior | Emergency integrity package | 0.603 | 0.644 | 0.019 | 0.074 | 0.067 | 0.249 | front-line cluster |
| High public-pressure prior | 60 percent invalidation threshold | 0.603 | 0.631 | 0.072 | 0.089 | 0.085 | 0.255 | rights-protection caveat |
| High public-pressure prior | Jurisdiction stripping constrained by rights carveouts | 0.602 | 0.644 | 0.083 | 0.080 | 0.095 | 0.254 | front-line cluster |
| High public-pressure prior | Automatic merits follow-up for emergency relief | 0.602 | 0.652 | 0.020 | 0.074 | 0.083 | 0.250 | front-line cluster |
| High public-pressure prior | Peer recusal + reasoned emergency docket | 0.602 | 0.639 | 0.080 | 0.077 | 0.076 | 0.253 | rights-protection caveat |
| High public-pressure prior | Mandatory written emergency reasoning | 0.601 | 0.637 | 0.051 | 0.087 | 0.071 | 0.252 | rights-protection caveat |
| High public-pressure prior | Public-interest litigation filter | 0.601 | 0.646 | 0.084 | 0.080 | 0.079 | 0.253 | front-line cluster |
| High public-pressure prior | Three-judge panels with en banc correction | 0.601 | 0.637 | 0.081 | 0.079 | 0.073 | 0.253 | rights-protection caveat |
| High public-pressure prior | Time-limited legislative override window | 0.601 | 0.637 | 0.080 | 0.076 | 0.083 | 0.254 | rights-protection caveat |
| High public-pressure prior | Nonpartisan commission appointments | 0.600 | 0.641 | 0.083 | 0.080 | 0.091 | 0.255 | front-line cluster |
| High public-pressure prior | Constitutional remand before invalidation | 0.600 | 0.638 | 0.081 | 0.078 | 0.078 | 0.220 | rights-protection caveat |
| High public-pressure prior | Expanded 15-seat court | 0.599 | 0.642 | 0.080 | 0.077 | 0.069 | 0.252 | front-line cluster |
| High public-pressure prior | Retention-election accountability court | 0.599 | 0.637 | 0.080 | 0.078 | 0.094 | 0.255 | front-line cluster |
| High public-pressure prior | Judicial review with legislative supermajority override | 0.598 | 0.640 | 0.081 | 0.079 | 0.095 | 0.255 | rights-protection caveat |
| High public-pressure prior | Independent recusal enforcement with substitutes | 0.598 | 0.638 | 0.083 | 0.081 | 0.078 | 0.253 | rights-protection caveat |
| High public-pressure prior | Constitutional remand with override window | 0.598 | 0.634 | 0.053 | 0.087 | 0.080 | 0.219 | rights-protection caveat |
| High public-pressure prior | Random panels with jurisdiction safeguards | 0.598 | 0.631 | 0.070 | 0.089 | 0.077 | 0.253 | rights-protection caveat |
| Low emergency-share prior | Jurisdiction stripping constrained by rights carveouts | 0.615 | 0.643 | 0.058 | 0.048 | 0.051 | 0.239 | front-line cluster |
| Low emergency-share prior | No emergency relief without merits review | 0.615 | 0.644 | 0.008 | 0.036 | 0.067 | 0.241 | front-line cluster |
| Low emergency-share prior | 60 percent invalidation threshold | 0.613 | 0.634 | 0.051 | 0.057 | 0.075 | 0.245 | rights-protection caveat |
| Low emergency-share prior | 18-year staggered terms + regular appointments | 0.612 | 0.645 | 0.063 | 0.051 | 0.066 | 0.242 | front-line cluster |
| Low emergency-share prior | Nonpartisan commission appointments | 0.611 | 0.638 | 0.061 | 0.049 | 0.058 | 0.242 | front-line cluster |
| Low emergency-share prior | Public-interest litigation filter | 0.611 | 0.643 | 0.059 | 0.050 | 0.060 | 0.242 | front-line cluster |
| Low emergency-share prior | Automatic merits follow-up for emergency relief | 0.610 | 0.641 | 0.013 | 0.041 | 0.072 | 0.242 | front-line cluster |
| Low emergency-share prior | Mandatory written emergency reasoning | 0.610 | 0.631 | 0.033 | 0.052 | 0.065 | 0.243 | rights-protection caveat |
| Low emergency-share prior | Constitutional remand before invalidation | 0.610 | 0.638 | 0.058 | 0.049 | 0.063 | 0.208 | rights-protection caveat |
| Low emergency-share prior | Emergency integrity package | 0.610 | 0.646 | 0.014 | 0.042 | 0.055 | 0.240 | front-line cluster |
| Low emergency-share prior | Three-judge panels with en banc correction | 0.609 | 0.638 | 0.058 | 0.048 | 0.069 | 0.243 | front-line cluster |
| Low emergency-share prior | Peer recusal + reasoned emergency docket | 0.608 | 0.637 | 0.061 | 0.049 | 0.069 | 0.243 | front-line cluster |
| Low emergency-share prior | Independent recusal enforcement with substitutes | 0.608 | 0.639 | 0.059 | 0.048 | 0.063 | 0.243 | front-line cluster |
| Low emergency-share prior | Expanded 15-seat court | 0.608 | 0.637 | 0.057 | 0.048 | 0.058 | 0.242 | front-line cluster |
| Low emergency-share prior | Retention-election accountability court | 0.608 | 0.634 | 0.060 | 0.049 | 0.069 | 0.243 | front-line cluster |
| Low emergency-share prior | Judicial review with legislative supermajority override | 0.606 | 0.636 | 0.054 | 0.047 | 0.073 | 0.243 | front-line cluster |
| Low emergency-share prior | Constitutional remand with override window | 0.606 | 0.635 | 0.037 | 0.055 | 0.071 | 0.209 | rights-protection caveat |
| Low emergency-share prior | Randomized merits panels with en banc correction | 0.605 | 0.635 | 0.058 | 0.049 | 0.072 | 0.243 | front-line cluster |
| Low emergency-share prior | Time-limited legislative override window | 0.605 | 0.640 | 0.060 | 0.049 | 0.086 | 0.246 | front-line cluster |
| High emergency-share prior | 18-year staggered terms + regular appointments | 0.519 | 0.620 | 0.180 | 0.222 | 0.225 | 0.403 | compliance caveat |
| High emergency-share prior | Public-interest litigation filter | 0.519 | 0.630 | 0.175 | 0.215 | 0.218 | 0.402 | compliance caveat |
| High emergency-share prior | 60 percent invalidation threshold | 0.518 | 0.610 | 0.175 | 0.257 | 0.237 | 0.407 | compliance caveat |
| High emergency-share prior | Jurisdiction stripping constrained by rights carveouts | 0.518 | 0.618 | 0.184 | 0.223 | 0.242 | 0.404 | compliance caveat |
| High emergency-share prior | No emergency relief without merits review | 0.517 | 0.643 | 0.047 | 0.177 | 0.227 | 0.395 | compliance caveat |
| High emergency-share prior | Constitutional remand before invalidation | 0.516 | 0.619 | 0.184 | 0.226 | 0.226 | 0.367 | compliance caveat |
| High emergency-share prior | Independent recusal enforcement with substitutes | 0.516 | 0.627 | 0.180 | 0.222 | 0.211 | 0.401 | compliance caveat |
| High emergency-share prior | Peer recusal + reasoned emergency docket | 0.515 | 0.621 | 0.182 | 0.221 | 0.224 | 0.403 | compliance caveat |
| High emergency-share prior | Nonpartisan commission appointments | 0.514 | 0.621 | 0.177 | 0.220 | 0.227 | 0.403 | compliance caveat |
| High emergency-share prior | Constitutional remand with override window | 0.514 | 0.614 | 0.141 | 0.248 | 0.226 | 0.369 | compliance caveat |
| High emergency-share prior | Retention-election accountability court | 0.513 | 0.615 | 0.178 | 0.219 | 0.232 | 0.403 | compliance caveat |
| High emergency-share prior | Pre-enactment constitutional council | 0.513 | 0.623 | 0.179 | 0.221 | 0.210 | 0.398 | compliance caveat |
| High emergency-share prior | Mandatory written emergency reasoning | 0.512 | 0.612 | 0.145 | 0.251 | 0.234 | 0.405 | compliance caveat |
| High emergency-share prior | Three-judge panels with en banc correction | 0.512 | 0.627 | 0.183 | 0.227 | 0.238 | 0.403 | compliance caveat |
| High emergency-share prior | Comparative 16-seat constitutional senates | 0.512 | 0.607 | 0.170 | 0.248 | 0.222 | 0.406 | rights-protection caveat |
| High emergency-share prior | Emergency integrity package | 0.511 | 0.640 | 0.059 | 0.179 | 0.234 | 0.397 | compliance caveat |
| High emergency-share prior | Time-limited legislative override window | 0.511 | 0.625 | 0.181 | 0.222 | 0.239 | 0.404 | compliance caveat |
| High emergency-share prior | Constitutional council with concrete-review backstop | 0.510 | 0.624 | 0.182 | 0.220 | 0.231 | 0.401 | compliance caveat |
| High emergency-share prior | Randomized merits panels with en banc correction | 0.510 | 0.623 | 0.181 | 0.221 | 0.247 | 0.405 | compliance caveat |
| Low rights-risk prior | Jurisdiction stripping constrained by rights carveouts | 0.636 | 0.640 | 0.051 | 0.041 | 0.030 | 0.176 | rights-protection caveat |
| Low rights-risk prior | No emergency relief without merits review | 0.636 | 0.647 | 0.005 | 0.036 | 0.033 | 0.176 | rights-protection caveat |
| Low rights-risk prior | 60 percent invalidation threshold | 0.636 | 0.635 | 0.043 | 0.047 | 0.031 | 0.179 | rights-protection caveat |
| Low rights-risk prior | 18-year staggered terms + regular appointments | 0.635 | 0.643 | 0.051 | 0.043 | 0.034 | 0.179 | rights-protection caveat |
| Low rights-risk prior | Nonpartisan commission appointments | 0.633 | 0.644 | 0.053 | 0.045 | 0.032 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Automatic merits follow-up for emergency relief | 0.632 | 0.642 | 0.009 | 0.046 | 0.033 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Retention-election accountability court | 0.632 | 0.638 | 0.051 | 0.043 | 0.040 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Mandatory written emergency reasoning | 0.632 | 0.643 | 0.029 | 0.048 | 0.034 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Emergency integrity package | 0.632 | 0.644 | 0.009 | 0.047 | 0.027 | 0.175 | rights-protection caveat |
| Low rights-risk prior | Peer recusal + reasoned emergency docket | 0.631 | 0.647 | 0.053 | 0.045 | 0.031 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Time-limited legislative override window | 0.631 | 0.641 | 0.052 | 0.043 | 0.033 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Public-interest litigation filter | 0.631 | 0.644 | 0.054 | 0.046 | 0.038 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Judicial review with legislative supermajority override | 0.630 | 0.647 | 0.054 | 0.046 | 0.034 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Constitutional remand before invalidation | 0.630 | 0.641 | 0.051 | 0.043 | 0.039 | 0.147 | rights-protection caveat |
| Low rights-risk prior | Three-judge panels with en banc correction | 0.630 | 0.645 | 0.056 | 0.045 | 0.033 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Randomized merits panels with en banc correction | 0.630 | 0.641 | 0.051 | 0.043 | 0.030 | 0.177 | rights-protection caveat |
| Low rights-risk prior | Independent recusal enforcement with substitutes | 0.629 | 0.645 | 0.054 | 0.045 | 0.040 | 0.178 | rights-protection caveat |
| Low rights-risk prior | Pre-enactment constitutional council | 0.629 | 0.642 | 0.052 | 0.043 | 0.033 | 0.176 | rights-protection caveat |
| Low rights-risk prior | Random panels with jurisdiction safeguards | 0.629 | 0.641 | 0.045 | 0.051 | 0.030 | 0.176 | rights-protection caveat |
| Low rights-risk prior | Expanded 15-seat court | 0.628 | 0.647 | 0.056 | 0.045 | 0.038 | 0.178 | rights-protection caveat |
| High rights-risk prior | 18-year staggered terms + regular appointments | 0.527 | 0.566 | 0.119 | 0.135 | 0.202 | 0.401 | compliance caveat |
| High rights-risk prior | No emergency relief without merits review | 0.527 | 0.600 | 0.026 | 0.098 | 0.226 | 0.398 | compliance caveat |
| High rights-risk prior | 60 percent invalidation threshold | 0.527 | 0.550 | 0.116 | 0.164 | 0.233 | 0.406 | compliance caveat |
| High rights-risk prior | Constitutional remand before invalidation | 0.527 | 0.566 | 0.118 | 0.132 | 0.218 | 0.364 | compliance caveat |
| High rights-risk prior | Automatic merits follow-up for emergency relief | 0.526 | 0.593 | 0.034 | 0.079 | 0.243 | 0.401 | compliance caveat |
| High rights-risk prior | Emergency integrity package | 0.525 | 0.599 | 0.035 | 0.079 | 0.224 | 0.398 | compliance caveat |
| High rights-risk prior | Constitutional remand with override window | 0.523 | 0.554 | 0.091 | 0.159 | 0.211 | 0.364 | compliance caveat |
| High rights-risk prior | Nonpartisan commission appointments | 0.522 | 0.571 | 0.122 | 0.135 | 0.231 | 0.404 | compliance caveat |
| High rights-risk prior | Randomized merits panels with en banc correction | 0.522 | 0.567 | 0.118 | 0.131 | 0.209 | 0.401 | compliance caveat |
| High rights-risk prior | Peer recusal + reasoned emergency docket | 0.520 | 0.569 | 0.120 | 0.134 | 0.227 | 0.403 | compliance caveat |
| High rights-risk prior | Three-judge panels with en banc correction | 0.519 | 0.569 | 0.120 | 0.133 | 0.231 | 0.404 | compliance caveat |
| High rights-risk prior | Public-interest litigation filter | 0.519 | 0.575 | 0.118 | 0.133 | 0.222 | 0.402 | compliance caveat |
| High rights-risk prior | Expanded 15-seat court | 0.518 | 0.571 | 0.122 | 0.134 | 0.236 | 0.405 | compliance caveat |
| High rights-risk prior | Retention-election accountability court | 0.518 | 0.549 | 0.117 | 0.129 | 0.230 | 0.403 | compliance caveat |
| Weak democratic-mandate prior | 60 percent invalidation threshold | 0.546 | 0.604 | 0.094 | 0.125 | 0.180 | 0.377 | compliance caveat |
| Weak democratic-mandate prior | Constitutional remand before invalidation | 0.542 | 0.616 | 0.110 | 0.113 | 0.176 | 0.338 | compliance caveat |
| Weak democratic-mandate prior | No emergency relief without merits review | 0.540 | 0.619 | 0.020 | 0.082 | 0.176 | 0.371 | compliance caveat |
| Weak democratic-mandate prior | Public-interest litigation filter | 0.540 | 0.617 | 0.099 | 0.106 | 0.174 | 0.375 | compliance caveat |
| Weak democratic-mandate prior | 18-year staggered terms + regular appointments | 0.539 | 0.610 | 0.105 | 0.109 | 0.183 | 0.377 | compliance caveat |
| Weak democratic-mandate prior | Constitutional remand with override window | 0.538 | 0.614 | 0.074 | 0.128 | 0.189 | 0.340 | compliance caveat |
| Weak democratic-mandate prior | Nonpartisan commission appointments | 0.538 | 0.611 | 0.106 | 0.111 | 0.170 | 0.375 | compliance caveat |
| Weak democratic-mandate prior | Peer recusal + reasoned emergency docket | 0.536 | 0.608 | 0.103 | 0.110 | 0.187 | 0.377 | compliance caveat |
| High constitutional-conflict prior | 60 percent invalidation threshold | 0.512 | 0.601 | 0.142 | 0.194 | 0.235 | 0.439 | compliance caveat |
| High constitutional-conflict prior | Constitutional remand before invalidation | 0.509 | 0.614 | 0.153 | 0.166 | 0.235 | 0.400 | compliance caveat |
| High constitutional-conflict prior | Public-interest litigation filter | 0.507 | 0.622 | 0.153 | 0.169 | 0.223 | 0.434 | compliance caveat |
| High constitutional-conflict prior | 18-year staggered terms + regular appointments | 0.506 | 0.613 | 0.149 | 0.163 | 0.246 | 0.438 | compliance caveat |
| High constitutional-conflict prior | Constitutional remand with override window | 0.506 | 0.610 | 0.117 | 0.192 | 0.244 | 0.401 | compliance caveat |
| High constitutional-conflict prior | Mandatory written emergency reasoning | 0.504 | 0.608 | 0.111 | 0.187 | 0.238 | 0.437 | compliance caveat |
| High constitutional-conflict prior | Comparative 16-seat constitutional senates | 0.503 | 0.609 | 0.140 | 0.194 | 0.238 | 0.438 | compliance caveat |
| High constitutional-conflict prior | Retention-election accountability court | 0.503 | 0.596 | 0.144 | 0.159 | 0.240 | 0.436 | compliance caveat |
| Imported legislative-family prior | No emergency relief without merits review | 0.619 | 0.652 | 0.009 | 0.054 | 0.054 | 0.229 | front-line cluster |
| Imported legislative-family prior | 60 percent invalidation threshold | 0.614 | 0.641 | 0.060 | 0.073 | 0.066 | 0.234 | rights-protection caveat |
| Imported legislative-family prior | 18-year staggered terms + regular appointments | 0.614 | 0.642 | 0.071 | 0.065 | 0.061 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Jurisdiction stripping constrained by rights carveouts | 0.613 | 0.644 | 0.070 | 0.066 | 0.069 | 0.232 | rights-protection caveat |
| Imported legislative-family prior | Automatic merits follow-up for emergency relief | 0.613 | 0.650 | 0.015 | 0.066 | 0.062 | 0.230 | front-line cluster |
| Imported legislative-family prior | Mandatory written emergency reasoning | 0.611 | 0.647 | 0.043 | 0.073 | 0.059 | 0.232 | rights-protection caveat |
| Imported legislative-family prior | Nonpartisan commission appointments | 0.611 | 0.646 | 0.072 | 0.067 | 0.065 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Retention-election accountability court | 0.611 | 0.639 | 0.069 | 0.065 | 0.062 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Peer recusal + reasoned emergency docket | 0.611 | 0.643 | 0.072 | 0.067 | 0.062 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Constitutional remand before invalidation | 0.611 | 0.643 | 0.074 | 0.067 | 0.061 | 0.199 | rights-protection caveat |
| Imported legislative-family prior | Three-judge panels with en banc correction | 0.610 | 0.647 | 0.071 | 0.067 | 0.063 | 0.233 | rights-protection caveat |
| Imported legislative-family prior | Emergency integrity package | 0.610 | 0.653 | 0.015 | 0.062 | 0.069 | 0.231 | rights-protection caveat |
| Imported legislative-family prior | Randomized merits panels with en banc correction | 0.610 | 0.649 | 0.070 | 0.067 | 0.065 | 0.232 | rights-protection caveat |
| Imported legislative-family prior | Public-interest litigation filter | 0.609 | 0.645 | 0.074 | 0.069 | 0.079 | 0.235 | rights-protection caveat |
| Imported legislative-family prior | Judicial review with legislative supermajority override | 0.609 | 0.645 | 0.072 | 0.065 | 0.075 | 0.235 | rights-protection caveat |
