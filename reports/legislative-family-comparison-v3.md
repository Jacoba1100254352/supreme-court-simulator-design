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
| simulation-campaign-v0.csv | 0.281 | 0.593 | 0.167 | 0.200 | 0.280 | 0.144 | 0.597 | 0.228 | Jurisdiction stripping constrained by rights carveouts (0.611) |
| simulation-campaign-v5.csv | 0.429 | 0.554 | 0.239 | 0.200 | 0.280 | 0.262 | 0.562 | 0.285 | No emergency relief without merits review (0.603) |
| simulation-campaign-v10.csv | 0.518 | 0.582 | 0.268 | 0.200 | 0.227 | 0.326 | 0.565 | 0.307 | No emergency relief without merits review (0.602) |
| simulation-campaign-v15.csv | 0.500 | 0.594 | 0.255 | 0.110 | 0.230 | 0.323 | 0.513 | 0.293 | No emergency relief without merits review (0.603) |
| simulation-campaign-v20.csv | 0.584 | 0.564 | 0.251 | 0.116 | 0.246 | 0.334 | 0.494 | 0.302 | No emergency relief without merits review (0.601) |
| simulation-campaign-v21-paper.csv | 0.343 | 0.610 | 0.175 | 0.104 | 0.237 | 0.120 | 0.547 | 0.213 | Jurisdiction stripping constrained by rights carveouts (0.616) |
| simulation-manipulation-stress.csv | 0.283 | 0.582 | 0.102 | 0.163 | 0.274 | 0.097 | 0.552 | 0.202 | Jurisdiction stripping constrained by rights carveouts (0.617) |

## Scenario Sensitivity By Family

| Family | Scenario | Directional | Legal | Rights | Shadow | Conflict | Strategic | Override att. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| simulation-campaign-v0.csv | Jurisdiction stripping constrained by rights carveouts | 0.611 | 0.688 | 0.660 | 0.077 | 0.414 | 0.189 | 0.058 |
| simulation-campaign-v0.csv | No emergency relief without merits review | 0.611 | 0.695 | 0.650 | 0.009 | 0.401 | 0.184 | 0.000 |
| simulation-campaign-v0.csv | 18-year staggered terms + regular appointments | 0.609 | 0.687 | 0.653 | 0.077 | 0.405 | 0.202 | 0.000 |
| simulation-campaign-v0.csv | Automatic merits follow-up for emergency relief | 0.607 | 0.689 | 0.654 | 0.015 | 0.396 | 0.194 | 0.000 |
| simulation-campaign-v0.csv | Nonpartisan commission appointments | 0.607 | 0.691 | 0.648 | 0.074 | 0.400 | 0.189 | 0.000 |
| simulation-campaign-v0.csv | 60 percent invalidation threshold | 0.606 | 0.686 | 0.643 | 0.065 | 0.403 | 0.205 | 0.000 |
| simulation-campaign-v0.csv | Peer recusal + reasoned emergency docket | 0.606 | 0.689 | 0.653 | 0.075 | 0.401 | 0.201 | 0.000 |
| simulation-campaign-v0.csv | Judicial review with legislative supermajority override | 0.605 | 0.687 | 0.654 | 0.074 | 0.415 | 0.197 | 0.057 |
| simulation-campaign-v0.csv | Mandatory written emergency reasoning | 0.605 | 0.691 | 0.654 | 0.044 | 0.408 | 0.203 | 0.000 |
| simulation-campaign-v0.csv | Time-limited legislative override window | 0.605 | 0.686 | 0.658 | 0.077 | 0.419 | 0.198 | 0.054 |
| simulation-campaign-v0.csv | Independent recusal enforcement with substitutes | 0.604 | 0.691 | 0.656 | 0.077 | 0.412 | 0.194 | 0.000 |
| simulation-campaign-v0.csv | Three-judge panels with en banc correction | 0.604 | 0.690 | 0.653 | 0.077 | 0.409 | 0.192 | 0.000 |
| simulation-campaign-v0.csv | Retention-election accountability court | 0.604 | 0.692 | 0.643 | 0.078 | 0.412 | 0.190 | 0.051 |
| simulation-campaign-v0.csv | Emergency integrity package | 0.603 | 0.696 | 0.652 | 0.016 | 0.409 | 0.186 | 0.000 |
| simulation-campaign-v0.csv | Expanded 15-seat court | 0.603 | 0.687 | 0.651 | 0.072 | 0.402 | 0.200 | 0.000 |
| simulation-campaign-v0.csv | Randomized merits panels with en banc correction | 0.603 | 0.689 | 0.655 | 0.078 | 0.413 | 0.194 | 0.000 |
| simulation-campaign-v0.csv | Random panels with jurisdiction safeguards | 0.601 | 0.687 | 0.647 | 0.063 | 0.408 | 0.188 | 0.047 |
| simulation-campaign-v0.csv | Public-interest litigation filter | 0.601 | 0.685 | 0.661 | 0.080 | 0.418 | 0.194 | 0.000 |
| simulation-campaign-v0.csv | Constitutional remand before invalidation | 0.601 | 0.703 | 0.656 | 0.082 | 0.418 | 0.193 | 0.036 |
| simulation-campaign-v0.csv | Pre-enactment constitutional council | 0.600 | 0.696 | 0.649 | 0.079 | 0.414 | 0.193 | 0.048 |
| simulation-campaign-v0.csv | Constitutional remand with override window | 0.598 | 0.703 | 0.651 | 0.043 | 0.413 | 0.191 | 0.041 |
| simulation-campaign-v0.csv | Constitutional council with concrete-review backstop | 0.597 | 0.699 | 0.650 | 0.076 | 0.420 | 0.193 | 0.038 |
| simulation-campaign-v0.csv | Comparative 16-seat constitutional senates | 0.597 | 0.692 | 0.640 | 0.066 | 0.405 | 0.191 | 0.000 |
| simulation-campaign-v0.csv | Stylized current U.S.-like supreme court | 0.594 | 0.678 | 0.649 | 0.235 | 0.417 | 0.225 | 0.000 |
| simulation-campaign-v0.csv | Supreme court with cross-checking constitutional court | 0.585 | 0.678 | 0.637 | 0.064 | 0.436 | 0.196 | 0.000 |
| simulation-campaign-v0.csv | Dual supreme courts with disagreement filter | 0.576 | 0.662 | 0.660 | 0.067 | 0.449 | 0.206 | 0.000 |
| simulation-campaign-v10.csv | No emergency relief without merits review | 0.602 | 0.684 | 0.659 | 0.013 | 0.431 | 0.200 | 0.000 |
| simulation-campaign-v10.csv | Jurisdiction stripping constrained by rights carveouts | 0.601 | 0.678 | 0.657 | 0.090 | 0.434 | 0.200 | 0.057 |
| simulation-campaign-v10.csv | 18-year staggered terms + regular appointments | 0.601 | 0.677 | 0.655 | 0.086 | 0.422 | 0.211 | 0.000 |
| simulation-campaign-v10.csv | 60 percent invalidation threshold | 0.598 | 0.678 | 0.644 | 0.075 | 0.428 | 0.215 | 0.000 |
| simulation-campaign-v10.csv | Automatic merits follow-up for emergency relief | 0.597 | 0.676 | 0.658 | 0.020 | 0.424 | 0.210 | 0.000 |
| simulation-campaign-v10.csv | Peer recusal + reasoned emergency docket | 0.596 | 0.675 | 0.656 | 0.085 | 0.426 | 0.213 | 0.000 |
| simulation-campaign-v10.csv | Time-limited legislative override window | 0.596 | 0.674 | 0.656 | 0.083 | 0.435 | 0.209 | 0.060 |
| simulation-campaign-v10.csv | Mandatory written emergency reasoning | 0.594 | 0.676 | 0.658 | 0.051 | 0.434 | 0.217 | 0.000 |
| simulation-campaign-v10.csv | Retention-election accountability court | 0.594 | 0.677 | 0.649 | 0.090 | 0.437 | 0.203 | 0.055 |
| simulation-campaign-v10.csv | Three-judge panels with en banc correction | 0.594 | 0.677 | 0.656 | 0.086 | 0.437 | 0.208 | 0.000 |
| simulation-campaign-v10.csv | Nonpartisan commission appointments | 0.594 | 0.677 | 0.655 | 0.089 | 0.436 | 0.213 | 0.000 |
| simulation-campaign-v10.csv | Judicial review with legislative supermajority override | 0.594 | 0.672 | 0.655 | 0.085 | 0.437 | 0.211 | 0.061 |
| simulation-campaign-v10.csv | Public-interest litigation filter | 0.593 | 0.674 | 0.666 | 0.085 | 0.439 | 0.207 | 0.000 |
| simulation-campaign-v10.csv | Independent recusal enforcement with substitutes | 0.593 | 0.676 | 0.656 | 0.086 | 0.431 | 0.204 | 0.000 |
| simulation-campaign-v10.csv | Randomized merits panels with en banc correction | 0.592 | 0.675 | 0.657 | 0.089 | 0.434 | 0.205 | 0.000 |
| simulation-campaign-v10.csv | Expanded 15-seat court | 0.591 | 0.676 | 0.658 | 0.088 | 0.432 | 0.217 | 0.000 |
| simulation-campaign-v10.csv | Emergency integrity package | 0.591 | 0.682 | 0.655 | 0.021 | 0.435 | 0.207 | 0.000 |
| simulation-campaign-v10.csv | Random panels with jurisdiction safeguards | 0.591 | 0.673 | 0.649 | 0.076 | 0.434 | 0.201 | 0.063 |
| simulation-campaign-v10.csv | Constitutional remand before invalidation | 0.591 | 0.693 | 0.654 | 0.094 | 0.439 | 0.202 | 0.046 |
| simulation-campaign-v10.csv | Pre-enactment constitutional council | 0.589 | 0.685 | 0.652 | 0.090 | 0.441 | 0.208 | 0.051 |
| simulation-campaign-v10.csv | Constitutional remand with override window | 0.587 | 0.692 | 0.655 | 0.054 | 0.445 | 0.206 | 0.046 |
| simulation-campaign-v10.csv | Comparative 16-seat constitutional senates | 0.586 | 0.681 | 0.642 | 0.072 | 0.427 | 0.207 | 0.000 |
| simulation-campaign-v10.csv | Constitutional council with concrete-review backstop | 0.586 | 0.687 | 0.645 | 0.088 | 0.434 | 0.203 | 0.043 |
| simulation-campaign-v10.csv | Stylized current U.S.-like supreme court | 0.580 | 0.667 | 0.646 | 0.265 | 0.440 | 0.239 | 0.000 |
| simulation-campaign-v10.csv | Supreme court with cross-checking constitutional court | 0.573 | 0.666 | 0.635 | 0.074 | 0.465 | 0.208 | 0.000 |
| simulation-campaign-v10.csv | Dual supreme courts with disagreement filter | 0.568 | 0.653 | 0.659 | 0.073 | 0.467 | 0.213 | 0.000 |
| simulation-campaign-v15.csv | No emergency relief without merits review | 0.603 | 0.691 | 0.665 | 0.013 | 0.419 | 0.197 | 0.000 |
| simulation-campaign-v15.csv | Jurisdiction stripping constrained by rights carveouts | 0.601 | 0.682 | 0.663 | 0.088 | 0.420 | 0.198 | 0.047 |
| simulation-campaign-v15.csv | Automatic merits follow-up for emergency relief | 0.601 | 0.689 | 0.657 | 0.020 | 0.408 | 0.199 | 0.000 |
| simulation-campaign-v15.csv | 18-year staggered terms + regular appointments | 0.600 | 0.685 | 0.660 | 0.086 | 0.414 | 0.210 | 0.000 |
| simulation-campaign-v15.csv | Peer recusal + reasoned emergency docket | 0.599 | 0.684 | 0.662 | 0.081 | 0.415 | 0.209 | 0.000 |
| simulation-campaign-v15.csv | 60 percent invalidation threshold | 0.599 | 0.686 | 0.647 | 0.074 | 0.415 | 0.213 | 0.000 |
| simulation-campaign-v15.csv | Nonpartisan commission appointments | 0.598 | 0.683 | 0.668 | 0.088 | 0.424 | 0.205 | 0.000 |
| simulation-campaign-v15.csv | Mandatory written emergency reasoning | 0.598 | 0.687 | 0.653 | 0.048 | 0.410 | 0.207 | 0.000 |
| simulation-campaign-v15.csv | Time-limited legislative override window | 0.596 | 0.683 | 0.663 | 0.087 | 0.425 | 0.204 | 0.043 |
| simulation-campaign-v15.csv | Public-interest litigation filter | 0.596 | 0.684 | 0.665 | 0.088 | 0.419 | 0.199 | 0.000 |
| simulation-campaign-v15.csv | Retention-election accountability court | 0.596 | 0.687 | 0.654 | 0.087 | 0.422 | 0.203 | 0.039 |
| simulation-campaign-v15.csv | Randomized merits panels with en banc correction | 0.596 | 0.685 | 0.664 | 0.086 | 0.421 | 0.202 | 0.000 |
| simulation-campaign-v15.csv | Judicial review with legislative supermajority override | 0.596 | 0.681 | 0.663 | 0.091 | 0.424 | 0.207 | 0.043 |
| simulation-campaign-v15.csv | Independent recusal enforcement with substitutes | 0.595 | 0.685 | 0.666 | 0.089 | 0.426 | 0.206 | 0.000 |
| simulation-campaign-v15.csv | Three-judge panels with en banc correction | 0.595 | 0.680 | 0.667 | 0.091 | 0.427 | 0.207 | 0.000 |
| simulation-campaign-v15.csv | Emergency integrity package | 0.595 | 0.690 | 0.658 | 0.020 | 0.415 | 0.194 | 0.000 |
| simulation-campaign-v15.csv | Expanded 15-seat court | 0.594 | 0.685 | 0.659 | 0.084 | 0.412 | 0.212 | 0.000 |
| simulation-campaign-v15.csv | Pre-enactment constitutional council | 0.593 | 0.693 | 0.658 | 0.090 | 0.425 | 0.197 | 0.042 |
| simulation-campaign-v15.csv | Random panels with jurisdiction safeguards | 0.592 | 0.679 | 0.656 | 0.073 | 0.421 | 0.197 | 0.052 |
| simulation-campaign-v15.csv | Constitutional remand before invalidation | 0.591 | 0.698 | 0.657 | 0.089 | 0.419 | 0.201 | 0.029 |
| simulation-campaign-v15.csv | Constitutional remand with override window | 0.590 | 0.698 | 0.656 | 0.051 | 0.420 | 0.197 | 0.033 |
| simulation-campaign-v15.csv | Comparative 16-seat constitutional senates | 0.589 | 0.687 | 0.649 | 0.074 | 0.414 | 0.205 | 0.000 |
| simulation-campaign-v15.csv | Constitutional council with concrete-review backstop | 0.588 | 0.692 | 0.653 | 0.090 | 0.419 | 0.203 | 0.041 |
| simulation-campaign-v15.csv | Stylized current U.S.-like supreme court | 0.583 | 0.671 | 0.660 | 0.262 | 0.435 | 0.242 | 0.000 |
| simulation-campaign-v15.csv | Supreme court with cross-checking constitutional court | 0.577 | 0.674 | 0.653 | 0.076 | 0.456 | 0.207 | 0.000 |
| simulation-campaign-v15.csv | Dual supreme courts with disagreement filter | 0.569 | 0.661 | 0.666 | 0.081 | 0.456 | 0.210 | 0.000 |
| simulation-campaign-v20.csv | No emergency relief without merits review | 0.601 | 0.683 | 0.661 | 0.013 | 0.421 | 0.196 | 0.000 |
| simulation-campaign-v20.csv | Jurisdiction stripping constrained by rights carveouts | 0.600 | 0.676 | 0.666 | 0.093 | 0.431 | 0.200 | 0.061 |
| simulation-campaign-v20.csv | 18-year staggered terms + regular appointments | 0.598 | 0.678 | 0.656 | 0.088 | 0.416 | 0.213 | 0.000 |
| simulation-campaign-v20.csv | 60 percent invalidation threshold | 0.598 | 0.678 | 0.654 | 0.074 | 0.420 | 0.212 | 0.000 |
| simulation-campaign-v20.csv | Automatic merits follow-up for emergency relief | 0.596 | 0.673 | 0.665 | 0.021 | 0.416 | 0.210 | 0.000 |
| simulation-campaign-v20.csv | Nonpartisan commission appointments | 0.596 | 0.678 | 0.666 | 0.092 | 0.429 | 0.206 | 0.000 |
| simulation-campaign-v20.csv | Peer recusal + reasoned emergency docket | 0.595 | 0.677 | 0.661 | 0.090 | 0.419 | 0.209 | 0.000 |
| simulation-campaign-v20.csv | Mandatory written emergency reasoning | 0.595 | 0.680 | 0.657 | 0.050 | 0.419 | 0.213 | 0.000 |
| simulation-campaign-v20.csv | Time-limited legislative override window | 0.594 | 0.671 | 0.661 | 0.082 | 0.426 | 0.209 | 0.063 |
| simulation-campaign-v20.csv | Judicial review with legislative supermajority override | 0.594 | 0.674 | 0.663 | 0.089 | 0.429 | 0.207 | 0.056 |
| simulation-campaign-v20.csv | Public-interest litigation filter | 0.594 | 0.678 | 0.670 | 0.091 | 0.432 | 0.208 | 0.000 |
| simulation-campaign-v20.csv | Three-judge panels with en banc correction | 0.593 | 0.675 | 0.667 | 0.091 | 0.429 | 0.209 | 0.000 |
| simulation-campaign-v20.csv | Emergency integrity package | 0.593 | 0.682 | 0.664 | 0.021 | 0.423 | 0.200 | 0.000 |
| simulation-campaign-v20.csv | Expanded 15-seat court | 0.592 | 0.675 | 0.666 | 0.089 | 0.422 | 0.214 | 0.000 |
| simulation-campaign-v20.csv | Retention-election accountability court | 0.591 | 0.678 | 0.655 | 0.095 | 0.431 | 0.207 | 0.045 |
| simulation-campaign-v20.csv | Independent recusal enforcement with substitutes | 0.591 | 0.675 | 0.661 | 0.089 | 0.424 | 0.207 | 0.000 |
| simulation-campaign-v20.csv | Randomized merits panels with en banc correction | 0.591 | 0.676 | 0.662 | 0.091 | 0.424 | 0.208 | 0.000 |
| simulation-campaign-v20.csv | Constitutional remand before invalidation | 0.589 | 0.689 | 0.662 | 0.093 | 0.429 | 0.202 | 0.045 |
| simulation-campaign-v20.csv | Pre-enactment constitutional council | 0.589 | 0.683 | 0.657 | 0.091 | 0.426 | 0.207 | 0.042 |
| simulation-campaign-v20.csv | Random panels with jurisdiction safeguards | 0.589 | 0.675 | 0.652 | 0.078 | 0.428 | 0.200 | 0.047 |
| simulation-campaign-v20.csv | Constitutional council with concrete-review backstop | 0.587 | 0.689 | 0.652 | 0.089 | 0.427 | 0.203 | 0.035 |
| simulation-campaign-v20.csv | Constitutional remand with override window | 0.586 | 0.691 | 0.661 | 0.056 | 0.432 | 0.202 | 0.043 |
| simulation-campaign-v20.csv | Comparative 16-seat constitutional senates | 0.584 | 0.679 | 0.650 | 0.076 | 0.426 | 0.209 | 0.000 |
| simulation-campaign-v20.csv | Stylized current U.S.-like supreme court | 0.579 | 0.662 | 0.659 | 0.276 | 0.442 | 0.244 | 0.000 |
| simulation-campaign-v20.csv | Supreme court with cross-checking constitutional court | 0.572 | 0.665 | 0.647 | 0.075 | 0.459 | 0.214 | 0.000 |
| simulation-campaign-v20.csv | Dual supreme courts with disagreement filter | 0.566 | 0.652 | 0.665 | 0.077 | 0.463 | 0.213 | 0.000 |
| simulation-campaign-v21-paper.csv | Jurisdiction stripping constrained by rights carveouts | 0.616 | 0.703 | 0.659 | 0.071 | 0.388 | 0.174 | 0.035 |
| simulation-campaign-v21-paper.csv | No emergency relief without merits review | 0.616 | 0.707 | 0.657 | 0.008 | 0.381 | 0.173 | 0.000 |
| simulation-campaign-v21-paper.csv | 18-year staggered terms + regular appointments | 0.613 | 0.702 | 0.650 | 0.068 | 0.378 | 0.188 | 0.000 |
| simulation-campaign-v21-paper.csv | Mandatory written emergency reasoning | 0.612 | 0.703 | 0.657 | 0.039 | 0.378 | 0.187 | 0.000 |
| simulation-campaign-v21-paper.csv | 60 percent invalidation threshold | 0.612 | 0.701 | 0.650 | 0.063 | 0.385 | 0.191 | 0.000 |
| simulation-campaign-v21-paper.csv | Nonpartisan commission appointments | 0.611 | 0.701 | 0.661 | 0.072 | 0.386 | 0.184 | 0.000 |
| simulation-campaign-v21-paper.csv | Time-limited legislative override window | 0.611 | 0.700 | 0.657 | 0.068 | 0.387 | 0.182 | 0.040 |
| simulation-campaign-v21-paper.csv | Automatic merits follow-up for emergency relief | 0.610 | 0.702 | 0.663 | 0.014 | 0.388 | 0.190 | 0.000 |
| simulation-campaign-v21-paper.csv | Three-judge panels with en banc correction | 0.610 | 0.704 | 0.655 | 0.072 | 0.384 | 0.178 | 0.000 |
| simulation-campaign-v21-paper.csv | Peer recusal + reasoned emergency docket | 0.609 | 0.699 | 0.659 | 0.074 | 0.383 | 0.191 | 0.000 |
| simulation-campaign-v21-paper.csv | Retention-election accountability court | 0.609 | 0.701 | 0.652 | 0.072 | 0.387 | 0.183 | 0.035 |
| simulation-campaign-v21-paper.csv | Independent recusal enforcement with substitutes | 0.609 | 0.703 | 0.658 | 0.071 | 0.384 | 0.178 | 0.000 |
| simulation-campaign-v21-paper.csv | Judicial review with legislative supermajority override | 0.609 | 0.699 | 0.658 | 0.072 | 0.390 | 0.185 | 0.042 |
| simulation-campaign-v21-paper.csv | Randomized merits panels with en banc correction | 0.608 | 0.701 | 0.662 | 0.073 | 0.388 | 0.181 | 0.000 |
| simulation-campaign-v21-paper.csv | Public-interest litigation filter | 0.607 | 0.700 | 0.665 | 0.078 | 0.397 | 0.182 | 0.000 |
| simulation-campaign-v21-paper.csv | Expanded 15-seat court | 0.607 | 0.702 | 0.655 | 0.070 | 0.381 | 0.193 | 0.000 |
| simulation-campaign-v21-paper.csv | Random panels with jurisdiction safeguards | 0.607 | 0.698 | 0.660 | 0.061 | 0.392 | 0.180 | 0.042 |
| simulation-campaign-v21-paper.csv | Emergency integrity package | 0.606 | 0.709 | 0.657 | 0.014 | 0.391 | 0.180 | 0.000 |
| simulation-campaign-v21-paper.csv | Constitutional remand before invalidation | 0.606 | 0.712 | 0.661 | 0.074 | 0.393 | 0.178 | 0.028 |
| simulation-campaign-v21-paper.csv | Pre-enactment constitutional council | 0.605 | 0.706 | 0.655 | 0.071 | 0.391 | 0.183 | 0.037 |
| simulation-campaign-v21-paper.csv | Constitutional remand with override window | 0.603 | 0.711 | 0.658 | 0.039 | 0.390 | 0.179 | 0.029 |
| simulation-campaign-v21-paper.csv | Constitutional council with concrete-review backstop | 0.603 | 0.708 | 0.654 | 0.072 | 0.390 | 0.182 | 0.031 |
| simulation-campaign-v21-paper.csv | Comparative 16-seat constitutional senates | 0.598 | 0.703 | 0.641 | 0.063 | 0.386 | 0.185 | 0.000 |
| simulation-campaign-v21-paper.csv | Stylized current U.S.-like supreme court | 0.596 | 0.691 | 0.655 | 0.235 | 0.399 | 0.219 | 0.000 |
| simulation-campaign-v21-paper.csv | Supreme court with cross-checking constitutional court | 0.592 | 0.691 | 0.651 | 0.061 | 0.416 | 0.183 | 0.000 |
| simulation-campaign-v21-paper.csv | Dual supreme courts with disagreement filter | 0.584 | 0.681 | 0.660 | 0.061 | 0.419 | 0.191 | 0.000 |
| simulation-campaign-v5.csv | No emergency relief without merits review | 0.603 | 0.680 | 0.655 | 0.012 | 0.420 | 0.194 | 0.000 |
| simulation-campaign-v5.csv | Jurisdiction stripping constrained by rights carveouts | 0.600 | 0.675 | 0.661 | 0.088 | 0.435 | 0.202 | 0.064 |
| simulation-campaign-v5.csv | 18-year staggered terms + regular appointments | 0.600 | 0.674 | 0.651 | 0.080 | 0.415 | 0.213 | 0.000 |
| simulation-campaign-v5.csv | 60 percent invalidation threshold | 0.598 | 0.675 | 0.648 | 0.073 | 0.428 | 0.216 | 0.000 |
| simulation-campaign-v5.csv | Automatic merits follow-up for emergency relief | 0.597 | 0.672 | 0.658 | 0.019 | 0.420 | 0.209 | 0.000 |
| simulation-campaign-v5.csv | Time-limited legislative override window | 0.596 | 0.672 | 0.663 | 0.086 | 0.441 | 0.209 | 0.065 |
| simulation-campaign-v5.csv | Nonpartisan commission appointments | 0.596 | 0.673 | 0.661 | 0.087 | 0.435 | 0.209 | 0.000 |
| simulation-campaign-v5.csv | Peer recusal + reasoned emergency docket | 0.596 | 0.671 | 0.655 | 0.083 | 0.421 | 0.212 | 0.000 |
| simulation-campaign-v5.csv | Retention-election accountability court | 0.595 | 0.677 | 0.647 | 0.081 | 0.427 | 0.205 | 0.054 |
| simulation-campaign-v5.csv | Judicial review with legislative supermajority override | 0.595 | 0.672 | 0.659 | 0.086 | 0.439 | 0.210 | 0.064 |
| simulation-campaign-v5.csv | Three-judge panels with en banc correction | 0.595 | 0.677 | 0.650 | 0.080 | 0.427 | 0.206 | 0.000 |
| simulation-campaign-v5.csv | Emergency integrity package | 0.594 | 0.678 | 0.657 | 0.020 | 0.425 | 0.198 | 0.000 |
| simulation-campaign-v5.csv | Mandatory written emergency reasoning | 0.594 | 0.677 | 0.651 | 0.048 | 0.426 | 0.216 | 0.000 |
| simulation-campaign-v5.csv | Expanded 15-seat court | 0.593 | 0.672 | 0.660 | 0.081 | 0.424 | 0.213 | 0.000 |
| simulation-campaign-v5.csv | Randomized merits panels with en banc correction | 0.593 | 0.674 | 0.661 | 0.091 | 0.434 | 0.207 | 0.000 |
| simulation-campaign-v5.csv | Independent recusal enforcement with substitutes | 0.592 | 0.669 | 0.661 | 0.083 | 0.429 | 0.208 | 0.000 |
| simulation-campaign-v5.csv | Public-interest litigation filter | 0.592 | 0.670 | 0.667 | 0.090 | 0.440 | 0.204 | 0.000 |
| simulation-campaign-v5.csv | Pre-enactment constitutional council | 0.591 | 0.679 | 0.661 | 0.087 | 0.443 | 0.208 | 0.062 |
| simulation-campaign-v5.csv | Constitutional remand before invalidation | 0.590 | 0.688 | 0.656 | 0.087 | 0.435 | 0.201 | 0.051 |
| simulation-campaign-v5.csv | Random panels with jurisdiction safeguards | 0.589 | 0.671 | 0.652 | 0.076 | 0.438 | 0.203 | 0.056 |
| simulation-campaign-v5.csv | Comparative 16-seat constitutional senates | 0.588 | 0.679 | 0.639 | 0.071 | 0.417 | 0.201 | 0.000 |
| simulation-campaign-v5.csv | Constitutional council with concrete-review backstop | 0.587 | 0.686 | 0.642 | 0.082 | 0.427 | 0.206 | 0.037 |
| simulation-campaign-v5.csv | Constitutional remand with override window | 0.587 | 0.691 | 0.652 | 0.053 | 0.436 | 0.205 | 0.048 |
| simulation-campaign-v5.csv | Stylized current U.S.-like supreme court | 0.580 | 0.661 | 0.653 | 0.264 | 0.444 | 0.243 | 0.000 |
| simulation-campaign-v5.csv | Supreme court with cross-checking constitutional court | 0.574 | 0.664 | 0.641 | 0.077 | 0.460 | 0.209 | 0.000 |
| simulation-campaign-v5.csv | Dual supreme courts with disagreement filter | 0.564 | 0.647 | 0.657 | 0.078 | 0.469 | 0.217 | 0.000 |
| simulation-manipulation-stress.csv | Jurisdiction stripping constrained by rights carveouts | 0.617 | 0.700 | 0.653 | 0.071 | 0.391 | 0.174 | 0.046 |
| simulation-manipulation-stress.csv | No emergency relief without merits review | 0.616 | 0.704 | 0.651 | 0.008 | 0.385 | 0.177 | 0.000 |
| simulation-manipulation-stress.csv | 18-year staggered terms + regular appointments | 0.614 | 0.698 | 0.655 | 0.070 | 0.391 | 0.197 | 0.000 |
| simulation-manipulation-stress.csv | 60 percent invalidation threshold | 0.614 | 0.698 | 0.647 | 0.058 | 0.387 | 0.192 | 0.000 |
| simulation-manipulation-stress.csv | Nonpartisan commission appointments | 0.612 | 0.698 | 0.657 | 0.069 | 0.393 | 0.187 | 0.000 |
| simulation-manipulation-stress.csv | Automatic merits follow-up for emergency relief | 0.611 | 0.698 | 0.657 | 0.014 | 0.385 | 0.187 | 0.000 |
| simulation-manipulation-stress.csv | Mandatory written emergency reasoning | 0.610 | 0.700 | 0.652 | 0.039 | 0.389 | 0.192 | 0.000 |
| simulation-manipulation-stress.csv | Retention-election accountability court | 0.610 | 0.701 | 0.650 | 0.070 | 0.400 | 0.186 | 0.041 |
| simulation-manipulation-stress.csv | Peer recusal + reasoned emergency docket | 0.610 | 0.700 | 0.651 | 0.069 | 0.388 | 0.194 | 0.000 |
| simulation-manipulation-stress.csv | Judicial review with legislative supermajority override | 0.610 | 0.697 | 0.655 | 0.074 | 0.397 | 0.186 | 0.047 |
| simulation-manipulation-stress.csv | Randomized merits panels with en banc correction | 0.609 | 0.701 | 0.656 | 0.073 | 0.395 | 0.183 | 0.000 |
| simulation-manipulation-stress.csv | Time-limited legislative override window | 0.609 | 0.696 | 0.656 | 0.072 | 0.400 | 0.186 | 0.042 |
| simulation-manipulation-stress.csv | Three-judge panels with en banc correction | 0.609 | 0.701 | 0.652 | 0.070 | 0.398 | 0.186 | 0.000 |
| simulation-manipulation-stress.csv | Independent recusal enforcement with substitutes | 0.608 | 0.700 | 0.651 | 0.071 | 0.389 | 0.184 | 0.000 |
| simulation-manipulation-stress.csv | Emergency integrity package | 0.607 | 0.704 | 0.650 | 0.013 | 0.393 | 0.181 | 0.000 |
| simulation-manipulation-stress.csv | Expanded 15-seat court | 0.606 | 0.699 | 0.654 | 0.073 | 0.392 | 0.199 | 0.000 |
| simulation-manipulation-stress.csv | Random panels with jurisdiction safeguards | 0.606 | 0.697 | 0.652 | 0.062 | 0.402 | 0.180 | 0.036 |
| simulation-manipulation-stress.csv | Constitutional remand before invalidation | 0.605 | 0.711 | 0.651 | 0.076 | 0.394 | 0.181 | 0.027 |
| simulation-manipulation-stress.csv | Public-interest litigation filter | 0.605 | 0.696 | 0.661 | 0.075 | 0.406 | 0.190 | 0.000 |
| simulation-manipulation-stress.csv | Pre-enactment constitutional council | 0.603 | 0.701 | 0.648 | 0.071 | 0.397 | 0.189 | 0.034 |
| simulation-manipulation-stress.csv | Constitutional council with concrete-review backstop | 0.602 | 0.706 | 0.642 | 0.071 | 0.391 | 0.182 | 0.032 |
| simulation-manipulation-stress.csv | Constitutional remand with override window | 0.602 | 0.711 | 0.650 | 0.039 | 0.398 | 0.183 | 0.035 |
| simulation-manipulation-stress.csv | Comparative 16-seat constitutional senates | 0.600 | 0.703 | 0.638 | 0.062 | 0.392 | 0.184 | 0.000 |
| simulation-manipulation-stress.csv | Stylized current U.S.-like supreme court | 0.598 | 0.689 | 0.653 | 0.223 | 0.407 | 0.220 | 0.000 |
| simulation-manipulation-stress.csv | Supreme court with cross-checking constitutional court | 0.591 | 0.688 | 0.643 | 0.060 | 0.425 | 0.190 | 0.000 |
| simulation-manipulation-stress.csv | Dual supreme courts with disagreement filter | 0.585 | 0.678 | 0.655 | 0.060 | 0.420 | 0.192 | 0.000 |
