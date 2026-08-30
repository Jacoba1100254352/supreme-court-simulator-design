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
| simulation-campaign-v0.csv | 0.281 | 0.593 | 0.167 | 0.200 | 0.280 | 0.144 | 0.597 | 0.228 | No emergency relief without merits review (0.615) |
| simulation-campaign-v5.csv | 0.429 | 0.554 | 0.239 | 0.200 | 0.280 | 0.262 | 0.562 | 0.285 | No emergency relief without merits review (0.601) |
| simulation-campaign-v10.csv | 0.518 | 0.582 | 0.268 | 0.200 | 0.227 | 0.326 | 0.565 | 0.307 | No emergency relief without merits review (0.603) |
| simulation-campaign-v15.csv | 0.500 | 0.594 | 0.255 | 0.110 | 0.230 | 0.323 | 0.513 | 0.293 | No emergency relief without merits review (0.607) |
| simulation-campaign-v20.csv | 0.584 | 0.564 | 0.251 | 0.116 | 0.246 | 0.334 | 0.494 | 0.302 | 60 percent invalidation threshold (0.601) |
| simulation-campaign-v21-paper.csv | 0.343 | 0.610 | 0.175 | 0.104 | 0.237 | 0.120 | 0.547 | 0.213 | No emergency relief without merits review (0.619) |
| simulation-manipulation-stress.csv | 0.283 | 0.582 | 0.102 | 0.163 | 0.274 | 0.097 | 0.552 | 0.202 | No emergency relief without merits review (0.620) |

## Scenario Sensitivity By Family

| Family | Scenario | Directional | Legal | Rights | Shadow | Conflict | Strategic | Override att. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| simulation-campaign-v0.csv | No emergency relief without merits review | 0.615 | 0.665 | 0.643 | 0.008 | 0.361 | 0.182 | 0.000 |
| simulation-campaign-v0.csv | 60 percent invalidation threshold | 0.614 | 0.673 | 0.635 | 0.060 | 0.370 | 0.196 | 0.000 |
| simulation-campaign-v0.csv | 18-year staggered terms + regular appointments | 0.612 | 0.662 | 0.644 | 0.070 | 0.371 | 0.200 | 0.000 |
| simulation-campaign-v0.csv | Jurisdiction stripping constrained by rights carveouts | 0.612 | 0.662 | 0.639 | 0.064 | 0.374 | 0.193 | 0.096 |
| simulation-campaign-v0.csv | Automatic merits follow-up for emergency relief | 0.611 | 0.662 | 0.643 | 0.014 | 0.365 | 0.196 | 0.000 |
| simulation-campaign-v0.csv | Emergency integrity package | 0.609 | 0.668 | 0.643 | 0.015 | 0.367 | 0.188 | 0.000 |
| simulation-campaign-v0.csv | Public-interest litigation filter | 0.609 | 0.666 | 0.647 | 0.067 | 0.372 | 0.187 | 0.000 |
| simulation-campaign-v0.csv | Mandatory written emergency reasoning | 0.609 | 0.673 | 0.635 | 0.043 | 0.367 | 0.199 | 0.000 |
| simulation-campaign-v0.csv | Three-judge panels with en banc correction | 0.608 | 0.666 | 0.638 | 0.067 | 0.367 | 0.188 | 0.000 |
| simulation-campaign-v0.csv | Nonpartisan commission appointments | 0.607 | 0.663 | 0.639 | 0.070 | 0.373 | 0.196 | 0.000 |
| simulation-campaign-v0.csv | Peer recusal + reasoned emergency docket | 0.607 | 0.664 | 0.639 | 0.067 | 0.372 | 0.201 | 0.000 |
| simulation-campaign-v0.csv | Constitutional remand before invalidation | 0.607 | 0.686 | 0.638 | 0.068 | 0.369 | 0.187 | 0.063 |
| simulation-campaign-v0.csv | Retention-election accountability court | 0.607 | 0.664 | 0.639 | 0.069 | 0.387 | 0.200 | 0.091 |
| simulation-campaign-v0.csv | Randomized merits panels with en banc correction | 0.606 | 0.667 | 0.642 | 0.069 | 0.369 | 0.191 | 0.000 |
| simulation-campaign-v0.csv | Pre-enactment constitutional council | 0.606 | 0.673 | 0.640 | 0.066 | 0.376 | 0.190 | 0.080 |
| simulation-campaign-v0.csv | Constitutional remand with override window | 0.606 | 0.688 | 0.636 | 0.042 | 0.370 | 0.189 | 0.065 |
| simulation-campaign-v0.csv | Time-limited legislative override window | 0.605 | 0.659 | 0.642 | 0.066 | 0.389 | 0.203 | 0.092 |
| simulation-campaign-v0.csv | Expanded 15-seat court | 0.605 | 0.664 | 0.643 | 0.071 | 0.377 | 0.203 | 0.000 |
| simulation-campaign-v0.csv | Independent recusal enforcement with substitutes | 0.604 | 0.661 | 0.643 | 0.069 | 0.374 | 0.194 | 0.000 |
| simulation-campaign-v0.csv | Random panels with jurisdiction safeguards | 0.604 | 0.666 | 0.640 | 0.062 | 0.382 | 0.192 | 0.080 |
| simulation-campaign-v0.csv | Judicial review with legislative supermajority override | 0.604 | 0.658 | 0.643 | 0.066 | 0.383 | 0.204 | 0.085 |
| simulation-campaign-v0.csv | Constitutional council with concrete-review backstop | 0.603 | 0.676 | 0.640 | 0.067 | 0.375 | 0.193 | 0.077 |
| simulation-campaign-v0.csv | Comparative 16-seat constitutional senates | 0.603 | 0.676 | 0.635 | 0.058 | 0.371 | 0.193 | 0.000 |
| simulation-campaign-v0.csv | Judicial electorate selection court | 0.602 | 0.667 | 0.644 | 0.069 | 0.375 | 0.188 | 0.000 |
| simulation-campaign-v0.csv | Stylized current U.S.-like supreme court | 0.598 | 0.660 | 0.639 | 0.217 | 0.396 | 0.225 | 0.000 |
| simulation-campaign-v0.csv | Supreme court with cross-checking constitutional court | 0.595 | 0.668 | 0.626 | 0.056 | 0.393 | 0.191 | 0.000 |
| simulation-campaign-v0.csv | Dual supreme courts with disagreement filter | 0.583 | 0.644 | 0.638 | 0.059 | 0.401 | 0.200 | 0.000 |
| simulation-campaign-v10.csv | No emergency relief without merits review | 0.603 | 0.650 | 0.636 | 0.012 | 0.384 | 0.196 | 0.000 |
| simulation-campaign-v10.csv | 60 percent invalidation threshold | 0.599 | 0.655 | 0.629 | 0.072 | 0.394 | 0.211 | 0.000 |
| simulation-campaign-v10.csv | Jurisdiction stripping constrained by rights carveouts | 0.598 | 0.646 | 0.630 | 0.078 | 0.399 | 0.205 | 0.107 |
| simulation-campaign-v10.csv | Automatic merits follow-up for emergency relief | 0.598 | 0.642 | 0.639 | 0.019 | 0.391 | 0.204 | 0.000 |
| simulation-campaign-v10.csv | 18-year staggered terms + regular appointments | 0.597 | 0.647 | 0.634 | 0.084 | 0.395 | 0.213 | 0.000 |
| simulation-campaign-v10.csv | Emergency integrity package | 0.595 | 0.643 | 0.641 | 0.019 | 0.390 | 0.199 | 0.000 |
| simulation-campaign-v10.csv | Constitutional remand before invalidation | 0.594 | 0.674 | 0.628 | 0.084 | 0.390 | 0.196 | 0.063 |
| simulation-campaign-v10.csv | Mandatory written emergency reasoning | 0.593 | 0.649 | 0.630 | 0.052 | 0.394 | 0.210 | 0.000 |
| simulation-campaign-v10.csv | Three-judge panels with en banc correction | 0.593 | 0.650 | 0.636 | 0.082 | 0.396 | 0.205 | 0.000 |
| simulation-campaign-v10.csv | Peer recusal + reasoned emergency docket | 0.593 | 0.650 | 0.628 | 0.077 | 0.389 | 0.208 | 0.000 |
| simulation-campaign-v10.csv | Randomized merits panels with en banc correction | 0.593 | 0.648 | 0.635 | 0.083 | 0.395 | 0.205 | 0.000 |
| simulation-campaign-v10.csv | Public-interest litigation filter | 0.593 | 0.651 | 0.633 | 0.079 | 0.391 | 0.202 | 0.000 |
| simulation-campaign-v10.csv | Independent recusal enforcement with substitutes | 0.593 | 0.649 | 0.636 | 0.082 | 0.398 | 0.210 | 0.000 |
| simulation-campaign-v10.csv | Constitutional remand with override window | 0.592 | 0.678 | 0.629 | 0.054 | 0.395 | 0.200 | 0.065 |
| simulation-campaign-v10.csv | Time-limited legislative override window | 0.592 | 0.643 | 0.636 | 0.079 | 0.407 | 0.213 | 0.095 |
| simulation-campaign-v10.csv | Retention-election accountability court | 0.592 | 0.650 | 0.629 | 0.082 | 0.406 | 0.209 | 0.086 |
| simulation-campaign-v10.csv | Judicial review with legislative supermajority override | 0.592 | 0.642 | 0.640 | 0.085 | 0.412 | 0.215 | 0.103 |
| simulation-campaign-v10.csv | Nonpartisan commission appointments | 0.591 | 0.643 | 0.636 | 0.083 | 0.400 | 0.214 | 0.000 |
| simulation-campaign-v10.csv | Expanded 15-seat court | 0.591 | 0.649 | 0.634 | 0.082 | 0.394 | 0.211 | 0.000 |
| simulation-campaign-v10.csv | Pre-enactment constitutional council | 0.589 | 0.653 | 0.633 | 0.075 | 0.405 | 0.211 | 0.100 |
| simulation-campaign-v10.csv | Constitutional council with concrete-review backstop | 0.589 | 0.662 | 0.634 | 0.082 | 0.401 | 0.207 | 0.080 |
| simulation-campaign-v10.csv | Random panels with jurisdiction safeguards | 0.588 | 0.646 | 0.629 | 0.073 | 0.404 | 0.204 | 0.092 |
| simulation-campaign-v10.csv | Judicial electorate selection court | 0.588 | 0.645 | 0.641 | 0.080 | 0.398 | 0.202 | 0.000 |
| simulation-campaign-v10.csv | Comparative 16-seat constitutional senates | 0.587 | 0.658 | 0.625 | 0.073 | 0.392 | 0.206 | 0.000 |
| simulation-campaign-v10.csv | Stylized current U.S.-like supreme court | 0.582 | 0.633 | 0.637 | 0.239 | 0.426 | 0.242 | 0.000 |
| simulation-campaign-v10.csv | Supreme court with cross-checking constitutional court | 0.580 | 0.650 | 0.615 | 0.067 | 0.412 | 0.199 | 0.000 |
| simulation-campaign-v10.csv | Dual supreme courts with disagreement filter | 0.567 | 0.625 | 0.629 | 0.069 | 0.424 | 0.213 | 0.000 |
| simulation-campaign-v15.csv | No emergency relief without merits review | 0.607 | 0.661 | 0.644 | 0.012 | 0.375 | 0.187 | 0.000 |
| simulation-campaign-v15.csv | 60 percent invalidation threshold | 0.603 | 0.666 | 0.630 | 0.069 | 0.381 | 0.203 | 0.000 |
| simulation-campaign-v15.csv | 18-year staggered terms + regular appointments | 0.603 | 0.660 | 0.639 | 0.078 | 0.382 | 0.206 | 0.000 |
| simulation-campaign-v15.csv | Jurisdiction stripping constrained by rights carveouts | 0.602 | 0.655 | 0.644 | 0.079 | 0.393 | 0.197 | 0.099 |
| simulation-campaign-v15.csv | Public-interest litigation filter | 0.602 | 0.664 | 0.643 | 0.076 | 0.376 | 0.189 | 0.000 |
| simulation-campaign-v15.csv | Emergency integrity package | 0.600 | 0.662 | 0.642 | 0.019 | 0.378 | 0.191 | 0.000 |
| simulation-campaign-v15.csv | Constitutional remand before invalidation | 0.599 | 0.681 | 0.637 | 0.081 | 0.378 | 0.190 | 0.062 |
| simulation-campaign-v15.csv | Retention-election accountability court | 0.599 | 0.663 | 0.636 | 0.078 | 0.393 | 0.197 | 0.070 |
| simulation-campaign-v15.csv | Judicial review with legislative supermajority override | 0.599 | 0.659 | 0.637 | 0.077 | 0.387 | 0.202 | 0.086 |
| simulation-campaign-v15.csv | Nonpartisan commission appointments | 0.599 | 0.660 | 0.636 | 0.077 | 0.379 | 0.198 | 0.000 |
| simulation-campaign-v15.csv | Mandatory written emergency reasoning | 0.599 | 0.661 | 0.638 | 0.048 | 0.378 | 0.201 | 0.000 |
| simulation-campaign-v15.csv | Three-judge panels with en banc correction | 0.598 | 0.663 | 0.633 | 0.077 | 0.378 | 0.196 | 0.000 |
| simulation-campaign-v15.csv | Automatic merits follow-up for emergency relief | 0.598 | 0.650 | 0.645 | 0.019 | 0.386 | 0.204 | 0.000 |
| simulation-campaign-v15.csv | Peer recusal + reasoned emergency docket | 0.598 | 0.662 | 0.637 | 0.078 | 0.379 | 0.205 | 0.000 |
| simulation-campaign-v15.csv | Independent recusal enforcement with substitutes | 0.598 | 0.658 | 0.640 | 0.079 | 0.379 | 0.201 | 0.000 |
| simulation-campaign-v15.csv | Time-limited legislative override window | 0.598 | 0.658 | 0.635 | 0.075 | 0.388 | 0.198 | 0.079 |
| simulation-campaign-v15.csv | Constitutional remand with override window | 0.596 | 0.683 | 0.634 | 0.050 | 0.379 | 0.192 | 0.059 |
| simulation-campaign-v15.csv | Expanded 15-seat court | 0.596 | 0.657 | 0.639 | 0.076 | 0.381 | 0.205 | 0.000 |
| simulation-campaign-v15.csv | Randomized merits panels with en banc correction | 0.596 | 0.658 | 0.633 | 0.074 | 0.375 | 0.195 | 0.000 |
| simulation-campaign-v15.csv | Pre-enactment constitutional council | 0.595 | 0.665 | 0.639 | 0.075 | 0.390 | 0.200 | 0.081 |
| simulation-campaign-v15.csv | Comparative 16-seat constitutional senates | 0.594 | 0.669 | 0.635 | 0.069 | 0.382 | 0.199 | 0.000 |
| simulation-campaign-v15.csv | Constitutional council with concrete-review backstop | 0.593 | 0.668 | 0.638 | 0.074 | 0.386 | 0.199 | 0.074 |
| simulation-campaign-v15.csv | Judicial electorate selection court | 0.592 | 0.661 | 0.639 | 0.079 | 0.379 | 0.189 | 0.000 |
| simulation-campaign-v15.csv | Random panels with jurisdiction safeguards | 0.592 | 0.656 | 0.635 | 0.073 | 0.393 | 0.198 | 0.082 |
| simulation-campaign-v15.csv | Supreme court with cross-checking constitutional court | 0.585 | 0.657 | 0.628 | 0.065 | 0.399 | 0.193 | 0.000 |
| simulation-campaign-v15.csv | Stylized current U.S.-like supreme court | 0.585 | 0.650 | 0.638 | 0.239 | 0.411 | 0.236 | 0.000 |
| simulation-campaign-v15.csv | Dual supreme courts with disagreement filter | 0.572 | 0.639 | 0.633 | 0.068 | 0.410 | 0.205 | 0.000 |
| simulation-campaign-v20.csv | 60 percent invalidation threshold | 0.601 | 0.659 | 0.637 | 0.069 | 0.388 | 0.207 | 0.000 |
| simulation-campaign-v20.csv | No emergency relief without merits review | 0.600 | 0.647 | 0.652 | 0.012 | 0.387 | 0.196 | 0.000 |
| simulation-campaign-v20.csv | Automatic merits follow-up for emergency relief | 0.599 | 0.649 | 0.646 | 0.019 | 0.385 | 0.203 | 0.000 |
| simulation-campaign-v20.csv | 18-year staggered terms + regular appointments | 0.598 | 0.645 | 0.645 | 0.077 | 0.389 | 0.209 | 0.000 |
| simulation-campaign-v20.csv | Constitutional remand before invalidation | 0.598 | 0.677 | 0.639 | 0.081 | 0.382 | 0.193 | 0.055 |
| simulation-campaign-v20.csv | Public-interest litigation filter | 0.596 | 0.652 | 0.649 | 0.079 | 0.386 | 0.196 | 0.000 |
| simulation-campaign-v20.csv | Nonpartisan commission appointments | 0.596 | 0.652 | 0.644 | 0.081 | 0.392 | 0.204 | 0.000 |
| simulation-campaign-v20.csv | Jurisdiction stripping constrained by rights carveouts | 0.596 | 0.644 | 0.647 | 0.079 | 0.404 | 0.209 | 0.103 |
| simulation-campaign-v20.csv | Emergency integrity package | 0.595 | 0.648 | 0.649 | 0.019 | 0.386 | 0.199 | 0.000 |
| simulation-campaign-v20.csv | Mandatory written emergency reasoning | 0.595 | 0.653 | 0.639 | 0.051 | 0.387 | 0.207 | 0.000 |
| simulation-campaign-v20.csv | Peer recusal + reasoned emergency docket | 0.594 | 0.652 | 0.643 | 0.083 | 0.391 | 0.211 | 0.000 |
| simulation-campaign-v20.csv | Expanded 15-seat court | 0.594 | 0.652 | 0.643 | 0.080 | 0.384 | 0.211 | 0.000 |
| simulation-campaign-v20.csv | Constitutional remand with override window | 0.594 | 0.678 | 0.639 | 0.051 | 0.385 | 0.197 | 0.059 |
| simulation-campaign-v20.csv | Retention-election accountability court | 0.594 | 0.652 | 0.639 | 0.084 | 0.403 | 0.206 | 0.081 |
| simulation-campaign-v20.csv | Randomized merits panels with en banc correction | 0.593 | 0.652 | 0.642 | 0.078 | 0.387 | 0.199 | 0.000 |
| simulation-campaign-v20.csv | Independent recusal enforcement with substitutes | 0.593 | 0.650 | 0.642 | 0.082 | 0.390 | 0.202 | 0.000 |
| simulation-campaign-v20.csv | Three-judge panels with en banc correction | 0.593 | 0.648 | 0.645 | 0.081 | 0.389 | 0.206 | 0.000 |
| simulation-campaign-v20.csv | Judicial review with legislative supermajority override | 0.592 | 0.646 | 0.644 | 0.083 | 0.407 | 0.210 | 0.097 |
| simulation-campaign-v20.csv | Time-limited legislative override window | 0.592 | 0.644 | 0.644 | 0.081 | 0.407 | 0.212 | 0.095 |
| simulation-campaign-v20.csv | Random panels with jurisdiction safeguards | 0.590 | 0.653 | 0.639 | 0.074 | 0.401 | 0.202 | 0.081 |
| simulation-campaign-v20.csv | Judicial electorate selection court | 0.589 | 0.652 | 0.648 | 0.079 | 0.393 | 0.194 | 0.000 |
| simulation-campaign-v20.csv | Pre-enactment constitutional council | 0.589 | 0.658 | 0.644 | 0.085 | 0.406 | 0.208 | 0.089 |
| simulation-campaign-v20.csv | Constitutional council with concrete-review backstop | 0.589 | 0.660 | 0.645 | 0.081 | 0.402 | 0.207 | 0.080 |
| simulation-campaign-v20.csv | Comparative 16-seat constitutional senates | 0.588 | 0.656 | 0.643 | 0.067 | 0.393 | 0.211 | 0.000 |
| simulation-campaign-v20.csv | Stylized current U.S.-like supreme court | 0.583 | 0.644 | 0.645 | 0.248 | 0.423 | 0.237 | 0.000 |
| simulation-campaign-v20.csv | Supreme court with cross-checking constitutional court | 0.580 | 0.651 | 0.627 | 0.073 | 0.410 | 0.197 | 0.000 |
| simulation-campaign-v20.csv | Dual supreme courts with disagreement filter | 0.567 | 0.626 | 0.641 | 0.071 | 0.422 | 0.208 | 0.000 |
| simulation-campaign-v21-paper.csv | No emergency relief without merits review | 0.619 | 0.677 | 0.645 | 0.007 | 0.347 | 0.172 | 0.000 |
| simulation-campaign-v21-paper.csv | 60 percent invalidation threshold | 0.617 | 0.684 | 0.630 | 0.058 | 0.353 | 0.186 | 0.000 |
| simulation-campaign-v21-paper.csv | Jurisdiction stripping constrained by rights carveouts | 0.616 | 0.678 | 0.638 | 0.065 | 0.358 | 0.178 | 0.065 |
| simulation-campaign-v21-paper.csv | Automatic merits follow-up for emergency relief | 0.616 | 0.676 | 0.642 | 0.013 | 0.349 | 0.183 | 0.000 |
| simulation-campaign-v21-paper.csv | 18-year staggered terms + regular appointments | 0.615 | 0.678 | 0.635 | 0.064 | 0.352 | 0.189 | 0.000 |
| simulation-campaign-v21-paper.csv | Peer recusal + reasoned emergency docket | 0.614 | 0.682 | 0.638 | 0.065 | 0.351 | 0.186 | 0.000 |
| simulation-campaign-v21-paper.csv | Public-interest litigation filter | 0.614 | 0.680 | 0.645 | 0.065 | 0.353 | 0.174 | 0.000 |
| simulation-campaign-v21-paper.csv | Nonpartisan commission appointments | 0.614 | 0.678 | 0.637 | 0.065 | 0.350 | 0.180 | 0.000 |
| simulation-campaign-v21-paper.csv | Emergency integrity package | 0.613 | 0.681 | 0.642 | 0.013 | 0.352 | 0.176 | 0.000 |
| simulation-campaign-v21-paper.csv | Three-judge panels with en banc correction | 0.612 | 0.682 | 0.636 | 0.067 | 0.351 | 0.180 | 0.000 |
| simulation-campaign-v21-paper.csv | Retention-election accountability court | 0.612 | 0.680 | 0.638 | 0.067 | 0.367 | 0.184 | 0.073 |
| simulation-campaign-v21-paper.csv | Mandatory written emergency reasoning | 0.612 | 0.681 | 0.638 | 0.040 | 0.357 | 0.190 | 0.000 |
| simulation-campaign-v21-paper.csv | Judicial review with legislative supermajority override | 0.611 | 0.676 | 0.639 | 0.067 | 0.364 | 0.187 | 0.066 |
| simulation-campaign-v21-paper.csv | Randomized merits panels with en banc correction | 0.611 | 0.677 | 0.638 | 0.067 | 0.354 | 0.183 | 0.000 |
| simulation-campaign-v21-paper.csv | Constitutional remand before invalidation | 0.611 | 0.694 | 0.643 | 0.069 | 0.358 | 0.179 | 0.052 |
| simulation-campaign-v21-paper.csv | Expanded 15-seat court | 0.610 | 0.678 | 0.643 | 0.068 | 0.358 | 0.190 | 0.000 |
| simulation-campaign-v21-paper.csv | Random panels with jurisdiction safeguards | 0.609 | 0.680 | 0.636 | 0.058 | 0.361 | 0.179 | 0.064 |
| simulation-campaign-v21-paper.csv | Time-limited legislative override window | 0.609 | 0.675 | 0.638 | 0.069 | 0.366 | 0.192 | 0.082 |
| simulation-campaign-v21-paper.csv | Independent recusal enforcement with substitutes | 0.609 | 0.678 | 0.639 | 0.065 | 0.355 | 0.183 | 0.000 |
| simulation-campaign-v21-paper.csv | Constitutional remand with override window | 0.608 | 0.697 | 0.637 | 0.041 | 0.355 | 0.181 | 0.054 |
| simulation-campaign-v21-paper.csv | Pre-enactment constitutional council | 0.608 | 0.680 | 0.645 | 0.064 | 0.369 | 0.187 | 0.080 |
| simulation-campaign-v21-paper.csv | Judicial electorate selection court | 0.607 | 0.679 | 0.644 | 0.065 | 0.358 | 0.176 | 0.000 |
| simulation-campaign-v21-paper.csv | Constitutional council with concrete-review backstop | 0.606 | 0.688 | 0.636 | 0.067 | 0.360 | 0.186 | 0.061 |
| simulation-campaign-v21-paper.csv | Comparative 16-seat constitutional senates | 0.605 | 0.685 | 0.633 | 0.056 | 0.351 | 0.183 | 0.000 |
| simulation-campaign-v21-paper.csv | Stylized current U.S.-like supreme court | 0.600 | 0.668 | 0.644 | 0.219 | 0.387 | 0.220 | 0.000 |
| simulation-campaign-v21-paper.csv | Supreme court with cross-checking constitutional court | 0.598 | 0.677 | 0.626 | 0.054 | 0.376 | 0.181 | 0.000 |
| simulation-campaign-v21-paper.csv | Dual supreme courts with disagreement filter | 0.585 | 0.658 | 0.637 | 0.057 | 0.388 | 0.190 | 0.000 |
| simulation-campaign-v5.csv | No emergency relief without merits review | 0.601 | 0.642 | 0.636 | 0.012 | 0.387 | 0.195 | 0.000 |
| simulation-campaign-v5.csv | 60 percent invalidation threshold | 0.599 | 0.652 | 0.619 | 0.066 | 0.387 | 0.211 | 0.000 |
| simulation-campaign-v5.csv | 18-year staggered terms + regular appointments | 0.599 | 0.644 | 0.637 | 0.076 | 0.397 | 0.212 | 0.000 |
| simulation-campaign-v5.csv | Constitutional remand before invalidation | 0.598 | 0.672 | 0.633 | 0.077 | 0.392 | 0.196 | 0.073 |
| simulation-campaign-v5.csv | Public-interest litigation filter | 0.598 | 0.650 | 0.636 | 0.075 | 0.393 | 0.198 | 0.000 |
| simulation-campaign-v5.csv | Emergency integrity package | 0.597 | 0.644 | 0.640 | 0.018 | 0.393 | 0.198 | 0.000 |
| simulation-campaign-v5.csv | Nonpartisan commission appointments | 0.597 | 0.640 | 0.638 | 0.076 | 0.400 | 0.205 | 0.000 |
| simulation-campaign-v5.csv | Automatic merits follow-up for emergency relief | 0.597 | 0.634 | 0.642 | 0.018 | 0.395 | 0.208 | 0.000 |
| simulation-campaign-v5.csv | Jurisdiction stripping constrained by rights carveouts | 0.596 | 0.638 | 0.630 | 0.077 | 0.405 | 0.206 | 0.113 |
| simulation-campaign-v5.csv | Three-judge panels with en banc correction | 0.596 | 0.648 | 0.635 | 0.078 | 0.399 | 0.206 | 0.000 |
| simulation-campaign-v5.csv | Peer recusal + reasoned emergency docket | 0.595 | 0.646 | 0.631 | 0.074 | 0.390 | 0.209 | 0.000 |
| simulation-campaign-v5.csv | Mandatory written emergency reasoning | 0.595 | 0.645 | 0.629 | 0.047 | 0.394 | 0.213 | 0.000 |
| simulation-campaign-v5.csv | Retention-election accountability court | 0.595 | 0.646 | 0.624 | 0.075 | 0.405 | 0.204 | 0.098 |
| simulation-campaign-v5.csv | Constitutional remand with override window | 0.594 | 0.670 | 0.632 | 0.047 | 0.397 | 0.199 | 0.077 |
| simulation-campaign-v5.csv | Independent recusal enforcement with substitutes | 0.594 | 0.643 | 0.633 | 0.076 | 0.393 | 0.206 | 0.000 |
| simulation-campaign-v5.csv | Random panels with jurisdiction safeguards | 0.593 | 0.646 | 0.629 | 0.067 | 0.399 | 0.198 | 0.100 |
| simulation-campaign-v5.csv | Time-limited legislative override window | 0.592 | 0.640 | 0.630 | 0.075 | 0.412 | 0.213 | 0.112 |
| simulation-campaign-v5.csv | Expanded 15-seat court | 0.592 | 0.642 | 0.628 | 0.074 | 0.393 | 0.214 | 0.000 |
| simulation-campaign-v5.csv | Randomized merits panels with en banc correction | 0.591 | 0.642 | 0.632 | 0.079 | 0.396 | 0.212 | 0.000 |
| simulation-campaign-v5.csv | Judicial review with legislative supermajority override | 0.591 | 0.634 | 0.636 | 0.077 | 0.413 | 0.216 | 0.113 |
| simulation-campaign-v5.csv | Constitutional council with concrete-review backstop | 0.591 | 0.657 | 0.631 | 0.073 | 0.401 | 0.204 | 0.096 |
| simulation-campaign-v5.csv | Comparative 16-seat constitutional senates | 0.590 | 0.655 | 0.628 | 0.068 | 0.394 | 0.210 | 0.000 |
| simulation-campaign-v5.csv | Pre-enactment constitutional council | 0.589 | 0.646 | 0.637 | 0.077 | 0.407 | 0.209 | 0.102 |
| simulation-campaign-v5.csv | Judicial electorate selection court | 0.588 | 0.641 | 0.638 | 0.074 | 0.397 | 0.203 | 0.000 |
| simulation-campaign-v5.csv | Stylized current U.S.-like supreme court | 0.583 | 0.638 | 0.629 | 0.242 | 0.426 | 0.239 | 0.000 |
| simulation-campaign-v5.csv | Supreme court with cross-checking constitutional court | 0.579 | 0.648 | 0.611 | 0.068 | 0.421 | 0.202 | 0.000 |
| simulation-campaign-v5.csv | Dual supreme courts with disagreement filter | 0.570 | 0.620 | 0.632 | 0.066 | 0.421 | 0.209 | 0.000 |
| simulation-manipulation-stress.csv | No emergency relief without merits review | 0.620 | 0.674 | 0.646 | 0.007 | 0.354 | 0.175 | 0.000 |
| simulation-manipulation-stress.csv | 18-year staggered terms + regular appointments | 0.618 | 0.676 | 0.640 | 0.060 | 0.351 | 0.191 | 0.000 |
| simulation-manipulation-stress.csv | 60 percent invalidation threshold | 0.617 | 0.678 | 0.630 | 0.055 | 0.350 | 0.188 | 0.000 |
| simulation-manipulation-stress.csv | Jurisdiction stripping constrained by rights carveouts | 0.616 | 0.672 | 0.637 | 0.061 | 0.362 | 0.183 | 0.084 |
| simulation-manipulation-stress.csv | Emergency integrity package | 0.615 | 0.676 | 0.645 | 0.013 | 0.354 | 0.178 | 0.000 |
| simulation-manipulation-stress.csv | Retention-election accountability court | 0.615 | 0.675 | 0.637 | 0.063 | 0.364 | 0.184 | 0.073 |
| simulation-manipulation-stress.csv | Nonpartisan commission appointments | 0.614 | 0.674 | 0.638 | 0.062 | 0.355 | 0.183 | 0.000 |
| simulation-manipulation-stress.csv | Automatic merits follow-up for emergency relief | 0.614 | 0.669 | 0.646 | 0.013 | 0.359 | 0.189 | 0.000 |
| simulation-manipulation-stress.csv | Public-interest litigation filter | 0.613 | 0.679 | 0.642 | 0.066 | 0.356 | 0.177 | 0.000 |
| simulation-manipulation-stress.csv | Constitutional remand before invalidation | 0.613 | 0.697 | 0.636 | 0.065 | 0.355 | 0.176 | 0.053 |
| simulation-manipulation-stress.csv | Three-judge panels with en banc correction | 0.613 | 0.679 | 0.637 | 0.066 | 0.358 | 0.186 | 0.000 |
| simulation-manipulation-stress.csv | Peer recusal + reasoned emergency docket | 0.613 | 0.676 | 0.639 | 0.065 | 0.359 | 0.191 | 0.000 |
| simulation-manipulation-stress.csv | Mandatory written emergency reasoning | 0.613 | 0.675 | 0.636 | 0.040 | 0.357 | 0.193 | 0.000 |
| simulation-manipulation-stress.csv | Time-limited legislative override window | 0.612 | 0.673 | 0.639 | 0.063 | 0.368 | 0.187 | 0.078 |
| simulation-manipulation-stress.csv | Judicial review with legislative supermajority override | 0.612 | 0.675 | 0.639 | 0.065 | 0.364 | 0.187 | 0.073 |
| simulation-manipulation-stress.csv | Independent recusal enforcement with substitutes | 0.612 | 0.674 | 0.642 | 0.064 | 0.359 | 0.184 | 0.000 |
| simulation-manipulation-stress.csv | Expanded 15-seat court | 0.611 | 0.673 | 0.637 | 0.060 | 0.353 | 0.191 | 0.000 |
| simulation-manipulation-stress.csv | Randomized merits panels with en banc correction | 0.611 | 0.678 | 0.638 | 0.065 | 0.359 | 0.184 | 0.000 |
| simulation-manipulation-stress.csv | Constitutional remand with override window | 0.610 | 0.696 | 0.633 | 0.036 | 0.352 | 0.173 | 0.050 |
| simulation-manipulation-stress.csv | Pre-enactment constitutional council | 0.610 | 0.684 | 0.638 | 0.062 | 0.367 | 0.187 | 0.067 |
| simulation-manipulation-stress.csv | Random panels with jurisdiction safeguards | 0.609 | 0.676 | 0.632 | 0.056 | 0.366 | 0.182 | 0.080 |
| simulation-manipulation-stress.csv | Constitutional council with concrete-review backstop | 0.608 | 0.685 | 0.635 | 0.063 | 0.359 | 0.183 | 0.065 |
| simulation-manipulation-stress.csv | Judicial electorate selection court | 0.608 | 0.675 | 0.644 | 0.062 | 0.359 | 0.179 | 0.000 |
| simulation-manipulation-stress.csv | Comparative 16-seat constitutional senates | 0.606 | 0.681 | 0.632 | 0.056 | 0.358 | 0.185 | 0.000 |
| simulation-manipulation-stress.csv | Stylized current U.S.-like supreme court | 0.601 | 0.667 | 0.639 | 0.206 | 0.384 | 0.219 | 0.000 |
| simulation-manipulation-stress.csv | Supreme court with cross-checking constitutional court | 0.598 | 0.676 | 0.620 | 0.055 | 0.374 | 0.181 | 0.000 |
| simulation-manipulation-stress.csv | Dual supreme courts with disagreement filter | 0.590 | 0.659 | 0.635 | 0.056 | 0.382 | 0.190 | 0.000 |
