# Legislative Family Import Comparison v3

Compares the constitutional-review import contract across multiple congressional-simulator report families.

## Run Configuration

- legislative family directory: data/external/legislative
- imported families: 7
- runs per family: 40
- cases per run: 48
- base seed: 20260501

## Imported Profiles

| Family | Volume | Quality | Weak mandate | Rights risk | Partisan skew | Volatility | Legitimacy | Override pressure | Best scenario |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| simulation-campaign-v0.csv | 0.281 | 0.593 | 0.167 | 0.200 | 0.280 | 0.144 | 0.597 | 0.228 | 18-year staggered terms + regular appointments (0.614) |
| simulation-campaign-v5.csv | 0.429 | 0.554 | 0.239 | 0.200 | 0.280 | 0.262 | 0.562 | 0.285 | No emergency relief without merits review (0.603) |
| simulation-campaign-v10.csv | 0.518 | 0.582 | 0.268 | 0.200 | 0.227 | 0.326 | 0.565 | 0.307 | No emergency relief without merits review (0.601) |
| simulation-campaign-v15.csv | 0.500 | 0.594 | 0.255 | 0.110 | 0.230 | 0.323 | 0.513 | 0.293 | No emergency relief without merits review (0.607) |
| simulation-campaign-v20.csv | 0.584 | 0.564 | 0.251 | 0.116 | 0.246 | 0.334 | 0.494 | 0.302 | No emergency relief without merits review (0.603) |
| simulation-campaign-v21-paper.csv | 0.343 | 0.610 | 0.175 | 0.104 | 0.237 | 0.120 | 0.547 | 0.213 | No emergency relief without merits review (0.619) |
| simulation-manipulation-stress.csv | 0.283 | 0.582 | 0.102 | 0.163 | 0.274 | 0.097 | 0.552 | 0.202 | No emergency relief without merits review (0.620) |

## Scenario Sensitivity By Family

| Family | Scenario | Directional | Legal | Rights | Shadow | Conflict | Strategic | Override att. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| simulation-campaign-v0.csv | 18-year staggered terms + regular appointments | 0.614 | 0.668 | 0.646 | 0.069 | 0.375 | 0.198 | 0.000 |
| simulation-campaign-v0.csv | No emergency relief without merits review | 0.613 | 0.663 | 0.649 | 0.009 | 0.373 | 0.188 | 0.000 |
| simulation-campaign-v0.csv | Jurisdiction stripping constrained by rights carveouts | 0.613 | 0.666 | 0.645 | 0.069 | 0.380 | 0.194 | 0.093 |
| simulation-campaign-v0.csv | 60 percent invalidation threshold | 0.612 | 0.672 | 0.638 | 0.063 | 0.382 | 0.204 | 0.000 |
| simulation-campaign-v0.csv | Automatic merits follow-up for emergency relief | 0.611 | 0.664 | 0.647 | 0.014 | 0.372 | 0.195 | 0.000 |
| simulation-campaign-v0.csv | Peer recusal + reasoned emergency docket | 0.609 | 0.668 | 0.640 | 0.066 | 0.372 | 0.199 | 0.000 |
| simulation-campaign-v0.csv | Constitutional remand before invalidation | 0.608 | 0.689 | 0.644 | 0.069 | 0.377 | 0.190 | 0.065 |
| simulation-campaign-v0.csv | Nonpartisan commission appointments | 0.608 | 0.664 | 0.641 | 0.073 | 0.376 | 0.197 | 0.000 |
| simulation-campaign-v0.csv | Public-interest litigation filter | 0.608 | 0.664 | 0.655 | 0.070 | 0.382 | 0.194 | 0.000 |
| simulation-campaign-v0.csv | Emergency integrity package | 0.608 | 0.665 | 0.649 | 0.015 | 0.378 | 0.191 | 0.000 |
| simulation-campaign-v0.csv | Randomized merits panels with en banc correction | 0.608 | 0.670 | 0.641 | 0.067 | 0.370 | 0.188 | 0.000 |
| simulation-campaign-v0.csv | Retention-election accountability court | 0.607 | 0.664 | 0.642 | 0.068 | 0.390 | 0.199 | 0.082 |
| simulation-campaign-v0.csv | Mandatory written emergency reasoning | 0.607 | 0.670 | 0.644 | 0.043 | 0.384 | 0.203 | 0.000 |
| simulation-campaign-v0.csv | Independent recusal enforcement with substitutes | 0.607 | 0.666 | 0.646 | 0.068 | 0.377 | 0.195 | 0.000 |
| simulation-campaign-v0.csv | Three-judge panels with en banc correction | 0.607 | 0.663 | 0.643 | 0.070 | 0.379 | 0.191 | 0.000 |
| simulation-campaign-v0.csv | Time-limited legislative override window | 0.606 | 0.663 | 0.645 | 0.072 | 0.395 | 0.201 | 0.091 |
| simulation-campaign-v0.csv | Constitutional remand with override window | 0.605 | 0.691 | 0.635 | 0.043 | 0.372 | 0.185 | 0.055 |
| simulation-campaign-v0.csv | Judicial review with legislative supermajority override | 0.605 | 0.658 | 0.649 | 0.069 | 0.393 | 0.206 | 0.098 |
| simulation-campaign-v0.csv | Expanded 15-seat court | 0.605 | 0.664 | 0.646 | 0.071 | 0.380 | 0.206 | 0.000 |
| simulation-campaign-v0.csv | Random panels with jurisdiction safeguards | 0.604 | 0.667 | 0.644 | 0.064 | 0.388 | 0.190 | 0.088 |
| simulation-campaign-v0.csv | Pre-enactment constitutional council | 0.604 | 0.675 | 0.644 | 0.071 | 0.391 | 0.193 | 0.085 |
| simulation-campaign-v0.csv | Constitutional council with concrete-review backstop | 0.602 | 0.675 | 0.647 | 0.070 | 0.387 | 0.197 | 0.083 |
| simulation-campaign-v0.csv | Comparative 16-seat constitutional senates | 0.601 | 0.673 | 0.635 | 0.062 | 0.377 | 0.195 | 0.000 |
| simulation-campaign-v0.csv | Stylized current U.S.-like supreme court | 0.597 | 0.658 | 0.643 | 0.222 | 0.403 | 0.227 | 0.000 |
| simulation-campaign-v0.csv | Supreme court with cross-checking constitutional court | 0.594 | 0.669 | 0.625 | 0.061 | 0.395 | 0.191 | 0.000 |
| simulation-campaign-v0.csv | Dual supreme courts with disagreement filter | 0.583 | 0.644 | 0.644 | 0.061 | 0.408 | 0.203 | 0.000 |
| simulation-campaign-v10.csv | No emergency relief without merits review | 0.601 | 0.649 | 0.639 | 0.013 | 0.392 | 0.198 | 0.000 |
| simulation-campaign-v10.csv | 60 percent invalidation threshold | 0.597 | 0.654 | 0.629 | 0.076 | 0.401 | 0.216 | 0.000 |
| simulation-campaign-v10.csv | 18-year staggered terms + regular appointments | 0.597 | 0.649 | 0.637 | 0.083 | 0.400 | 0.214 | 0.000 |
| simulation-campaign-v10.csv | Jurisdiction stripping constrained by rights carveouts | 0.596 | 0.646 | 0.633 | 0.084 | 0.408 | 0.209 | 0.105 |
| simulation-campaign-v10.csv | Constitutional remand before invalidation | 0.595 | 0.676 | 0.632 | 0.084 | 0.396 | 0.199 | 0.063 |
| simulation-campaign-v10.csv | Automatic merits follow-up for emergency relief | 0.595 | 0.640 | 0.644 | 0.020 | 0.404 | 0.211 | 0.000 |
| simulation-campaign-v10.csv | Emergency integrity package | 0.594 | 0.641 | 0.647 | 0.020 | 0.402 | 0.203 | 0.000 |
| simulation-campaign-v10.csv | Three-judge panels with en banc correction | 0.594 | 0.651 | 0.639 | 0.086 | 0.401 | 0.204 | 0.000 |
| simulation-campaign-v10.csv | Retention-election accountability court | 0.594 | 0.649 | 0.637 | 0.081 | 0.414 | 0.211 | 0.088 |
| simulation-campaign-v10.csv | Public-interest litigation filter | 0.593 | 0.648 | 0.640 | 0.082 | 0.402 | 0.201 | 0.000 |
| simulation-campaign-v10.csv | Mandatory written emergency reasoning | 0.592 | 0.652 | 0.632 | 0.056 | 0.401 | 0.212 | 0.000 |
| simulation-campaign-v10.csv | Peer recusal + reasoned emergency docket | 0.592 | 0.647 | 0.635 | 0.081 | 0.401 | 0.215 | 0.000 |
| simulation-campaign-v10.csv | Independent recusal enforcement with substitutes | 0.592 | 0.646 | 0.641 | 0.082 | 0.405 | 0.206 | 0.000 |
| simulation-campaign-v10.csv | Randomized merits panels with en banc correction | 0.592 | 0.649 | 0.636 | 0.085 | 0.402 | 0.204 | 0.000 |
| simulation-campaign-v10.csv | Constitutional remand with override window | 0.591 | 0.676 | 0.635 | 0.056 | 0.406 | 0.207 | 0.071 |
| simulation-campaign-v10.csv | Judicial review with legislative supermajority override | 0.591 | 0.645 | 0.637 | 0.086 | 0.420 | 0.215 | 0.096 |
| simulation-campaign-v10.csv | Pre-enactment constitutional council | 0.590 | 0.656 | 0.639 | 0.079 | 0.410 | 0.209 | 0.093 |
| simulation-campaign-v10.csv | Nonpartisan commission appointments | 0.590 | 0.644 | 0.640 | 0.086 | 0.408 | 0.215 | 0.000 |
| simulation-campaign-v10.csv | Expanded 15-seat court | 0.590 | 0.648 | 0.639 | 0.083 | 0.403 | 0.217 | 0.000 |
| simulation-campaign-v10.csv | Time-limited legislative override window | 0.590 | 0.637 | 0.640 | 0.078 | 0.421 | 0.218 | 0.106 |
| simulation-campaign-v10.csv | Random panels with jurisdiction safeguards | 0.589 | 0.648 | 0.632 | 0.071 | 0.411 | 0.207 | 0.092 |
| simulation-campaign-v10.csv | Comparative 16-seat constitutional senates | 0.589 | 0.657 | 0.631 | 0.071 | 0.397 | 0.204 | 0.000 |
| simulation-campaign-v10.csv | Constitutional council with concrete-review backstop | 0.588 | 0.663 | 0.641 | 0.088 | 0.409 | 0.211 | 0.077 |
| simulation-campaign-v10.csv | Stylized current U.S.-like supreme court | 0.581 | 0.634 | 0.643 | 0.246 | 0.438 | 0.246 | 0.000 |
| simulation-campaign-v10.csv | Supreme court with cross-checking constitutional court | 0.579 | 0.652 | 0.618 | 0.073 | 0.425 | 0.204 | 0.000 |
| simulation-campaign-v10.csv | Dual supreme courts with disagreement filter | 0.567 | 0.624 | 0.637 | 0.073 | 0.433 | 0.213 | 0.000 |
| simulation-campaign-v15.csv | No emergency relief without merits review | 0.607 | 0.659 | 0.648 | 0.012 | 0.381 | 0.190 | 0.000 |
| simulation-campaign-v15.csv | 60 percent invalidation threshold | 0.603 | 0.665 | 0.635 | 0.069 | 0.389 | 0.207 | 0.000 |
| simulation-campaign-v15.csv | 18-year staggered terms + regular appointments | 0.602 | 0.660 | 0.644 | 0.079 | 0.388 | 0.207 | 0.000 |
| simulation-campaign-v15.csv | Retention-election accountability court | 0.602 | 0.667 | 0.638 | 0.078 | 0.391 | 0.195 | 0.070 |
| simulation-campaign-v15.csv | Emergency integrity package | 0.600 | 0.662 | 0.649 | 0.019 | 0.387 | 0.193 | 0.000 |
| simulation-campaign-v15.csv | Jurisdiction stripping constrained by rights carveouts | 0.600 | 0.657 | 0.646 | 0.081 | 0.402 | 0.205 | 0.093 |
| simulation-campaign-v15.csv | Constitutional remand before invalidation | 0.600 | 0.683 | 0.637 | 0.083 | 0.380 | 0.192 | 0.056 |
| simulation-campaign-v15.csv | Public-interest litigation filter | 0.599 | 0.662 | 0.647 | 0.079 | 0.386 | 0.195 | 0.000 |
| simulation-campaign-v15.csv | Time-limited legislative override window | 0.599 | 0.659 | 0.644 | 0.080 | 0.399 | 0.203 | 0.078 |
| simulation-campaign-v15.csv | Nonpartisan commission appointments | 0.599 | 0.658 | 0.641 | 0.078 | 0.388 | 0.199 | 0.000 |
| simulation-campaign-v15.csv | Randomized merits panels with en banc correction | 0.598 | 0.660 | 0.641 | 0.079 | 0.381 | 0.196 | 0.000 |
| simulation-campaign-v15.csv | Independent recusal enforcement with substitutes | 0.598 | 0.662 | 0.641 | 0.083 | 0.387 | 0.202 | 0.000 |
| simulation-campaign-v15.csv | Automatic merits follow-up for emergency relief | 0.597 | 0.649 | 0.651 | 0.020 | 0.395 | 0.207 | 0.000 |
| simulation-campaign-v15.csv | Expanded 15-seat court | 0.597 | 0.658 | 0.640 | 0.077 | 0.385 | 0.208 | 0.000 |
| simulation-campaign-v15.csv | Peer recusal + reasoned emergency docket | 0.597 | 0.659 | 0.645 | 0.084 | 0.392 | 0.209 | 0.000 |
| simulation-campaign-v15.csv | Mandatory written emergency reasoning | 0.596 | 0.659 | 0.641 | 0.051 | 0.388 | 0.210 | 0.000 |
| simulation-campaign-v15.csv | Three-judge panels with en banc correction | 0.596 | 0.659 | 0.645 | 0.087 | 0.391 | 0.202 | 0.000 |
| simulation-campaign-v15.csv | Judicial review with legislative supermajority override | 0.596 | 0.660 | 0.638 | 0.080 | 0.397 | 0.208 | 0.082 |
| simulation-campaign-v15.csv | Constitutional remand with override window | 0.595 | 0.683 | 0.640 | 0.052 | 0.388 | 0.194 | 0.057 |
| simulation-campaign-v15.csv | Random panels with jurisdiction safeguards | 0.594 | 0.656 | 0.642 | 0.071 | 0.398 | 0.199 | 0.087 |
| simulation-campaign-v15.csv | Constitutional council with concrete-review backstop | 0.594 | 0.669 | 0.645 | 0.078 | 0.396 | 0.201 | 0.073 |
| simulation-campaign-v15.csv | Pre-enactment constitutional council | 0.593 | 0.667 | 0.644 | 0.080 | 0.404 | 0.206 | 0.085 |
| simulation-campaign-v15.csv | Comparative 16-seat constitutional senates | 0.593 | 0.670 | 0.639 | 0.074 | 0.392 | 0.202 | 0.000 |
| simulation-campaign-v15.csv | Stylized current U.S.-like supreme court | 0.585 | 0.652 | 0.639 | 0.243 | 0.415 | 0.237 | 0.000 |
| simulation-campaign-v15.csv | Supreme court with cross-checking constitutional court | 0.582 | 0.655 | 0.627 | 0.068 | 0.411 | 0.199 | 0.000 |
| simulation-campaign-v15.csv | Dual supreme courts with disagreement filter | 0.574 | 0.638 | 0.644 | 0.070 | 0.415 | 0.204 | 0.000 |
| simulation-campaign-v20.csv | No emergency relief without merits review | 0.603 | 0.653 | 0.650 | 0.013 | 0.388 | 0.194 | 0.000 |
| simulation-campaign-v20.csv | 60 percent invalidation threshold | 0.600 | 0.659 | 0.641 | 0.072 | 0.393 | 0.212 | 0.000 |
| simulation-campaign-v20.csv | 18-year staggered terms + regular appointments | 0.597 | 0.645 | 0.645 | 0.078 | 0.395 | 0.212 | 0.000 |
| simulation-campaign-v20.csv | Constitutional remand before invalidation | 0.597 | 0.677 | 0.643 | 0.083 | 0.391 | 0.195 | 0.058 |
| simulation-campaign-v20.csv | Jurisdiction stripping constrained by rights carveouts | 0.596 | 0.645 | 0.646 | 0.081 | 0.404 | 0.208 | 0.097 |
| simulation-campaign-v20.csv | Automatic merits follow-up for emergency relief | 0.596 | 0.645 | 0.654 | 0.020 | 0.398 | 0.207 | 0.000 |
| simulation-campaign-v20.csv | Emergency integrity package | 0.596 | 0.649 | 0.655 | 0.020 | 0.394 | 0.202 | 0.000 |
| simulation-campaign-v20.csv | Public-interest litigation filter | 0.595 | 0.653 | 0.652 | 0.082 | 0.395 | 0.200 | 0.000 |
| simulation-campaign-v20.csv | Nonpartisan commission appointments | 0.595 | 0.647 | 0.650 | 0.084 | 0.401 | 0.205 | 0.000 |
| simulation-campaign-v20.csv | Expanded 15-seat court | 0.594 | 0.654 | 0.644 | 0.082 | 0.388 | 0.207 | 0.000 |
| simulation-campaign-v20.csv | Retention-election accountability court | 0.594 | 0.653 | 0.643 | 0.083 | 0.408 | 0.207 | 0.082 |
| simulation-campaign-v20.csv | Peer recusal + reasoned emergency docket | 0.593 | 0.653 | 0.642 | 0.085 | 0.392 | 0.211 | 0.000 |
| simulation-campaign-v20.csv | Independent recusal enforcement with substitutes | 0.593 | 0.653 | 0.644 | 0.084 | 0.393 | 0.200 | 0.000 |
| simulation-campaign-v20.csv | Mandatory written emergency reasoning | 0.593 | 0.650 | 0.643 | 0.052 | 0.395 | 0.212 | 0.000 |
| simulation-campaign-v20.csv | Randomized merits panels with en banc correction | 0.592 | 0.650 | 0.645 | 0.081 | 0.397 | 0.206 | 0.000 |
| simulation-campaign-v20.csv | Constitutional remand with override window | 0.592 | 0.676 | 0.643 | 0.056 | 0.400 | 0.201 | 0.066 |
| simulation-campaign-v20.csv | Judicial review with legislative supermajority override | 0.592 | 0.648 | 0.644 | 0.085 | 0.409 | 0.210 | 0.091 |
| simulation-campaign-v20.csv | Pre-enactment constitutional council | 0.591 | 0.659 | 0.645 | 0.081 | 0.402 | 0.205 | 0.082 |
| simulation-campaign-v20.csv | Comparative 16-seat constitutional senates | 0.589 | 0.655 | 0.646 | 0.067 | 0.398 | 0.208 | 0.000 |
| simulation-campaign-v20.csv | Three-judge panels with en banc correction | 0.589 | 0.645 | 0.644 | 0.084 | 0.398 | 0.210 | 0.000 |
| simulation-campaign-v20.csv | Random panels with jurisdiction safeguards | 0.589 | 0.654 | 0.641 | 0.075 | 0.407 | 0.203 | 0.077 |
| simulation-campaign-v20.csv | Time-limited legislative override window | 0.589 | 0.644 | 0.645 | 0.085 | 0.419 | 0.219 | 0.102 |
| simulation-campaign-v20.csv | Constitutional council with concrete-review backstop | 0.587 | 0.659 | 0.651 | 0.084 | 0.412 | 0.211 | 0.082 |
| simulation-campaign-v20.csv | Stylized current U.S.-like supreme court | 0.582 | 0.642 | 0.651 | 0.253 | 0.432 | 0.241 | 0.000 |
| simulation-campaign-v20.csv | Supreme court with cross-checking constitutional court | 0.579 | 0.651 | 0.624 | 0.072 | 0.414 | 0.197 | 0.000 |
| simulation-campaign-v20.csv | Dual supreme courts with disagreement filter | 0.564 | 0.622 | 0.643 | 0.073 | 0.431 | 0.213 | 0.000 |
| simulation-campaign-v21-paper.csv | No emergency relief without merits review | 0.619 | 0.678 | 0.651 | 0.008 | 0.358 | 0.176 | 0.000 |
| simulation-campaign-v21-paper.csv | 60 percent invalidation threshold | 0.617 | 0.685 | 0.636 | 0.058 | 0.359 | 0.189 | 0.000 |
| simulation-campaign-v21-paper.csv | 18-year staggered terms + regular appointments | 0.617 | 0.682 | 0.643 | 0.070 | 0.365 | 0.192 | 0.000 |
| simulation-campaign-v21-paper.csv | Jurisdiction stripping constrained by rights carveouts | 0.617 | 0.680 | 0.641 | 0.065 | 0.364 | 0.180 | 0.070 |
| simulation-campaign-v21-paper.csv | Automatic merits follow-up for emergency relief | 0.616 | 0.681 | 0.645 | 0.013 | 0.357 | 0.185 | 0.000 |
| simulation-campaign-v21-paper.csv | Peer recusal + reasoned emergency docket | 0.614 | 0.682 | 0.642 | 0.066 | 0.357 | 0.186 | 0.000 |
| simulation-campaign-v21-paper.csv | Public-interest litigation filter | 0.614 | 0.678 | 0.649 | 0.066 | 0.357 | 0.176 | 0.000 |
| simulation-campaign-v21-paper.csv | Nonpartisan commission appointments | 0.613 | 0.677 | 0.640 | 0.068 | 0.359 | 0.185 | 0.000 |
| simulation-campaign-v21-paper.csv | Emergency integrity package | 0.613 | 0.682 | 0.645 | 0.014 | 0.361 | 0.180 | 0.000 |
| simulation-campaign-v21-paper.csv | Retention-election accountability court | 0.613 | 0.684 | 0.639 | 0.071 | 0.370 | 0.185 | 0.066 |
| simulation-campaign-v21-paper.csv | Mandatory written emergency reasoning | 0.612 | 0.680 | 0.646 | 0.040 | 0.368 | 0.194 | 0.000 |
| simulation-campaign-v21-paper.csv | Constitutional remand before invalidation | 0.611 | 0.696 | 0.643 | 0.068 | 0.359 | 0.181 | 0.051 |
| simulation-campaign-v21-paper.csv | Three-judge panels with en banc correction | 0.611 | 0.681 | 0.639 | 0.067 | 0.357 | 0.185 | 0.000 |
| simulation-campaign-v21-paper.csv | Time-limited legislative override window | 0.611 | 0.678 | 0.645 | 0.069 | 0.374 | 0.188 | 0.080 |
| simulation-campaign-v21-paper.csv | Randomized merits panels with en banc correction | 0.611 | 0.677 | 0.646 | 0.066 | 0.362 | 0.182 | 0.000 |
| simulation-campaign-v21-paper.csv | Judicial review with legislative supermajority override | 0.611 | 0.676 | 0.646 | 0.069 | 0.376 | 0.191 | 0.073 |
| simulation-campaign-v21-paper.csv | Random panels with jurisdiction safeguards | 0.611 | 0.680 | 0.643 | 0.062 | 0.370 | 0.179 | 0.069 |
| simulation-campaign-v21-paper.csv | Constitutional remand with override window | 0.610 | 0.703 | 0.640 | 0.041 | 0.357 | 0.175 | 0.041 |
| simulation-campaign-v21-paper.csv | Expanded 15-seat court | 0.610 | 0.677 | 0.645 | 0.068 | 0.365 | 0.194 | 0.000 |
| simulation-campaign-v21-paper.csv | Independent recusal enforcement with substitutes | 0.608 | 0.676 | 0.644 | 0.071 | 0.366 | 0.191 | 0.000 |
| simulation-campaign-v21-paper.csv | Pre-enactment constitutional council | 0.608 | 0.682 | 0.645 | 0.065 | 0.372 | 0.187 | 0.077 |
| simulation-campaign-v21-paper.csv | Constitutional council with concrete-review backstop | 0.607 | 0.688 | 0.644 | 0.067 | 0.369 | 0.187 | 0.064 |
| simulation-campaign-v21-paper.csv | Comparative 16-seat constitutional senates | 0.607 | 0.685 | 0.636 | 0.058 | 0.358 | 0.187 | 0.000 |
| simulation-campaign-v21-paper.csv | Stylized current U.S.-like supreme court | 0.600 | 0.670 | 0.641 | 0.218 | 0.387 | 0.218 | 0.000 |
| simulation-campaign-v21-paper.csv | Supreme court with cross-checking constitutional court | 0.595 | 0.674 | 0.630 | 0.057 | 0.385 | 0.184 | 0.000 |
| simulation-campaign-v21-paper.csv | Dual supreme courts with disagreement filter | 0.587 | 0.659 | 0.645 | 0.058 | 0.394 | 0.192 | 0.000 |
| simulation-campaign-v5.csv | No emergency relief without merits review | 0.603 | 0.640 | 0.644 | 0.012 | 0.391 | 0.197 | 0.000 |
| simulation-campaign-v5.csv | Public-interest litigation filter | 0.598 | 0.650 | 0.640 | 0.075 | 0.395 | 0.199 | 0.000 |
| simulation-campaign-v5.csv | 60 percent invalidation threshold | 0.598 | 0.650 | 0.628 | 0.072 | 0.406 | 0.217 | 0.000 |
| simulation-campaign-v5.csv | Emergency integrity package | 0.597 | 0.642 | 0.646 | 0.019 | 0.399 | 0.199 | 0.000 |
| simulation-campaign-v5.csv | Jurisdiction stripping constrained by rights carveouts | 0.597 | 0.641 | 0.634 | 0.076 | 0.411 | 0.210 | 0.115 |
| simulation-campaign-v5.csv | 18-year staggered terms + regular appointments | 0.597 | 0.641 | 0.639 | 0.078 | 0.405 | 0.217 | 0.000 |
| simulation-campaign-v5.csv | Constitutional remand before invalidation | 0.596 | 0.670 | 0.635 | 0.084 | 0.403 | 0.200 | 0.079 |
| simulation-campaign-v5.csv | Nonpartisan commission appointments | 0.596 | 0.640 | 0.638 | 0.077 | 0.405 | 0.207 | 0.000 |
| simulation-campaign-v5.csv | Automatic merits follow-up for emergency relief | 0.595 | 0.634 | 0.643 | 0.018 | 0.402 | 0.208 | 0.000 |
| simulation-campaign-v5.csv | Peer recusal + reasoned emergency docket | 0.595 | 0.647 | 0.632 | 0.077 | 0.398 | 0.210 | 0.000 |
| simulation-campaign-v5.csv | Three-judge panels with en banc correction | 0.595 | 0.648 | 0.641 | 0.082 | 0.407 | 0.206 | 0.000 |
| simulation-campaign-v5.csv | Independent recusal enforcement with substitutes | 0.594 | 0.645 | 0.637 | 0.077 | 0.401 | 0.207 | 0.000 |
| simulation-campaign-v5.csv | Retention-election accountability court | 0.593 | 0.644 | 0.629 | 0.078 | 0.418 | 0.209 | 0.107 |
| simulation-campaign-v5.csv | Mandatory written emergency reasoning | 0.593 | 0.641 | 0.639 | 0.049 | 0.408 | 0.217 | 0.000 |
| simulation-campaign-v5.csv | Constitutional remand with override window | 0.593 | 0.673 | 0.628 | 0.049 | 0.396 | 0.200 | 0.072 |
| simulation-campaign-v5.csv | Randomized merits panels with en banc correction | 0.593 | 0.643 | 0.633 | 0.077 | 0.397 | 0.204 | 0.000 |
| simulation-campaign-v5.csv | Judicial review with legislative supermajority override | 0.592 | 0.638 | 0.641 | 0.078 | 0.418 | 0.216 | 0.109 |
| simulation-campaign-v5.csv | Expanded 15-seat court | 0.592 | 0.641 | 0.635 | 0.078 | 0.400 | 0.216 | 0.000 |
| simulation-campaign-v5.csv | Time-limited legislative override window | 0.591 | 0.639 | 0.636 | 0.079 | 0.420 | 0.214 | 0.113 |
| simulation-campaign-v5.csv | Constitutional council with concrete-review backstop | 0.591 | 0.656 | 0.638 | 0.076 | 0.407 | 0.207 | 0.090 |
| simulation-campaign-v5.csv | Random panels with jurisdiction safeguards | 0.591 | 0.647 | 0.630 | 0.071 | 0.410 | 0.204 | 0.099 |
| simulation-campaign-v5.csv | Comparative 16-seat constitutional senates | 0.590 | 0.653 | 0.634 | 0.068 | 0.403 | 0.210 | 0.000 |
| simulation-campaign-v5.csv | Pre-enactment constitutional council | 0.589 | 0.648 | 0.640 | 0.081 | 0.415 | 0.211 | 0.108 |
| simulation-campaign-v5.csv | Stylized current U.S.-like supreme court | 0.582 | 0.635 | 0.639 | 0.249 | 0.435 | 0.243 | 0.000 |
| simulation-campaign-v5.csv | Supreme court with cross-checking constitutional court | 0.578 | 0.645 | 0.615 | 0.068 | 0.428 | 0.204 | 0.000 |
| simulation-campaign-v5.csv | Dual supreme courts with disagreement filter | 0.567 | 0.617 | 0.636 | 0.070 | 0.433 | 0.215 | 0.000 |
| simulation-manipulation-stress.csv | No emergency relief without merits review | 0.620 | 0.674 | 0.649 | 0.007 | 0.359 | 0.174 | 0.000 |
| simulation-manipulation-stress.csv | 18-year staggered terms + regular appointments | 0.617 | 0.674 | 0.644 | 0.066 | 0.362 | 0.193 | 0.000 |
| simulation-manipulation-stress.csv | Emergency integrity package | 0.616 | 0.680 | 0.647 | 0.013 | 0.358 | 0.177 | 0.000 |
| simulation-manipulation-stress.csv | Jurisdiction stripping constrained by rights carveouts | 0.616 | 0.672 | 0.643 | 0.065 | 0.371 | 0.189 | 0.087 |
| simulation-manipulation-stress.csv | 60 percent invalidation threshold | 0.615 | 0.677 | 0.635 | 0.058 | 0.361 | 0.194 | 0.000 |
| simulation-manipulation-stress.csv | Three-judge panels with en banc correction | 0.615 | 0.682 | 0.638 | 0.066 | 0.359 | 0.181 | 0.000 |
| simulation-manipulation-stress.csv | Retention-election accountability court | 0.614 | 0.678 | 0.637 | 0.063 | 0.365 | 0.185 | 0.068 |
| simulation-manipulation-stress.csv | Mandatory written emergency reasoning | 0.614 | 0.678 | 0.642 | 0.042 | 0.363 | 0.192 | 0.000 |
| simulation-manipulation-stress.csv | Public-interest litigation filter | 0.614 | 0.679 | 0.646 | 0.069 | 0.363 | 0.179 | 0.000 |
| simulation-manipulation-stress.csv | Automatic merits follow-up for emergency relief | 0.613 | 0.673 | 0.639 | 0.013 | 0.358 | 0.192 | 0.000 |
| simulation-manipulation-stress.csv | Constitutional remand before invalidation | 0.613 | 0.696 | 0.638 | 0.066 | 0.357 | 0.179 | 0.055 |
| simulation-manipulation-stress.csv | Expanded 15-seat court | 0.613 | 0.679 | 0.641 | 0.063 | 0.361 | 0.194 | 0.000 |
| simulation-manipulation-stress.csv | Randomized merits panels with en banc correction | 0.612 | 0.677 | 0.644 | 0.064 | 0.364 | 0.183 | 0.000 |
| simulation-manipulation-stress.csv | Nonpartisan commission appointments | 0.612 | 0.673 | 0.645 | 0.068 | 0.367 | 0.188 | 0.000 |
| simulation-manipulation-stress.csv | Judicial review with legislative supermajority override | 0.611 | 0.673 | 0.645 | 0.067 | 0.377 | 0.194 | 0.084 |
| simulation-manipulation-stress.csv | Peer recusal + reasoned emergency docket | 0.611 | 0.674 | 0.642 | 0.066 | 0.367 | 0.195 | 0.000 |
| simulation-manipulation-stress.csv | Time-limited legislative override window | 0.611 | 0.671 | 0.644 | 0.065 | 0.379 | 0.197 | 0.088 |
| simulation-manipulation-stress.csv | Constitutional remand with override window | 0.611 | 0.697 | 0.639 | 0.038 | 0.359 | 0.177 | 0.056 |
| simulation-manipulation-stress.csv | Independent recusal enforcement with substitutes | 0.610 | 0.672 | 0.642 | 0.066 | 0.367 | 0.189 | 0.000 |
| simulation-manipulation-stress.csv | Random panels with jurisdiction safeguards | 0.610 | 0.677 | 0.637 | 0.058 | 0.372 | 0.183 | 0.072 |
| simulation-manipulation-stress.csv | Pre-enactment constitutional council | 0.609 | 0.687 | 0.636 | 0.066 | 0.371 | 0.188 | 0.064 |
| simulation-manipulation-stress.csv | Constitutional council with concrete-review backstop | 0.609 | 0.688 | 0.640 | 0.065 | 0.366 | 0.186 | 0.060 |
| simulation-manipulation-stress.csv | Comparative 16-seat constitutional senates | 0.605 | 0.682 | 0.635 | 0.056 | 0.366 | 0.189 | 0.000 |
| simulation-manipulation-stress.csv | Stylized current U.S.-like supreme court | 0.602 | 0.669 | 0.639 | 0.209 | 0.387 | 0.217 | 0.000 |
| simulation-manipulation-stress.csv | Supreme court with cross-checking constitutional court | 0.596 | 0.673 | 0.624 | 0.057 | 0.386 | 0.184 | 0.000 |
| simulation-manipulation-stress.csv | Dual supreme courts with disagreement filter | 0.591 | 0.659 | 0.641 | 0.058 | 0.388 | 0.189 | 0.000 |
