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
| simulation-campaign-v0.csv | 0.281 | 0.593 | 0.167 | 0.200 | 0.280 | 0.144 | 0.597 | 0.228 | No emergency relief without merits review (0.614) |
| simulation-campaign-v5.csv | 0.429 | 0.554 | 0.239 | 0.200 | 0.280 | 0.262 | 0.562 | 0.285 | No emergency relief without merits review (0.602) |
| simulation-campaign-v10.csv | 0.518 | 0.582 | 0.268 | 0.200 | 0.227 | 0.326 | 0.565 | 0.307 | No emergency relief without merits review (0.602) |
| simulation-campaign-v15.csv | 0.500 | 0.594 | 0.255 | 0.110 | 0.230 | 0.323 | 0.513 | 0.293 | No emergency relief without merits review (0.607) |
| simulation-campaign-v20.csv | 0.584 | 0.564 | 0.251 | 0.116 | 0.246 | 0.334 | 0.494 | 0.302 | 60 percent invalidation threshold (0.602) |
| simulation-campaign-v21-paper.csv | 0.343 | 0.610 | 0.175 | 0.104 | 0.237 | 0.120 | 0.547 | 0.213 | No emergency relief without merits review (0.619) |
| simulation-manipulation-stress.csv | 0.283 | 0.582 | 0.102 | 0.163 | 0.274 | 0.097 | 0.552 | 0.202 | No emergency relief without merits review (0.620) |

## Scenario Sensitivity By Family

| Family | Scenario | Directional | Legal | Rights | Shadow | Conflict | Strategic | Override att. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| simulation-campaign-v0.csv | No emergency relief without merits review | 0.614 | 0.664 | 0.642 | 0.008 | 0.362 | 0.184 | 0.000 |
| simulation-campaign-v0.csv | 60 percent invalidation threshold | 0.613 | 0.670 | 0.637 | 0.060 | 0.372 | 0.200 | 0.000 |
| simulation-campaign-v0.csv | 18-year staggered terms + regular appointments | 0.611 | 0.663 | 0.643 | 0.072 | 0.371 | 0.200 | 0.000 |
| simulation-campaign-v0.csv | Jurisdiction stripping constrained by rights carveouts | 0.611 | 0.659 | 0.639 | 0.063 | 0.373 | 0.194 | 0.095 |
| simulation-campaign-v0.csv | Automatic merits follow-up for emergency relief | 0.610 | 0.662 | 0.642 | 0.014 | 0.364 | 0.196 | 0.000 |
| simulation-campaign-v0.csv | Emergency integrity package | 0.610 | 0.668 | 0.643 | 0.014 | 0.366 | 0.187 | 0.000 |
| simulation-campaign-v0.csv | Peer recusal + reasoned emergency docket | 0.608 | 0.664 | 0.641 | 0.064 | 0.369 | 0.201 | 0.000 |
| simulation-campaign-v0.csv | Nonpartisan commission appointments | 0.608 | 0.664 | 0.638 | 0.070 | 0.370 | 0.194 | 0.000 |
| simulation-campaign-v0.csv | Public-interest litigation filter | 0.608 | 0.666 | 0.644 | 0.068 | 0.371 | 0.189 | 0.000 |
| simulation-campaign-v0.csv | Three-judge panels with en banc correction | 0.607 | 0.665 | 0.640 | 0.070 | 0.370 | 0.189 | 0.000 |
| simulation-campaign-v0.csv | Mandatory written emergency reasoning | 0.607 | 0.670 | 0.636 | 0.044 | 0.369 | 0.200 | 0.000 |
| simulation-campaign-v0.csv | Constitutional remand before invalidation | 0.607 | 0.685 | 0.636 | 0.068 | 0.368 | 0.186 | 0.061 |
| simulation-campaign-v0.csv | Retention-election accountability court | 0.606 | 0.663 | 0.637 | 0.070 | 0.384 | 0.200 | 0.084 |
| simulation-campaign-v0.csv | Time-limited legislative override window | 0.606 | 0.659 | 0.642 | 0.065 | 0.386 | 0.202 | 0.091 |
| simulation-campaign-v0.csv | Expanded 15-seat court | 0.606 | 0.664 | 0.641 | 0.068 | 0.372 | 0.199 | 0.000 |
| simulation-campaign-v0.csv | Randomized merits panels with en banc correction | 0.606 | 0.666 | 0.641 | 0.068 | 0.369 | 0.193 | 0.000 |
| simulation-campaign-v0.csv | Constitutional remand with override window | 0.605 | 0.688 | 0.637 | 0.042 | 0.371 | 0.190 | 0.063 |
| simulation-campaign-v0.csv | Pre-enactment constitutional council | 0.605 | 0.672 | 0.643 | 0.067 | 0.381 | 0.192 | 0.087 |
| simulation-campaign-v0.csv | Independent recusal enforcement with substitutes | 0.604 | 0.661 | 0.643 | 0.069 | 0.377 | 0.195 | 0.000 |
| simulation-campaign-v0.csv | Judicial review with legislative supermajority override | 0.604 | 0.661 | 0.638 | 0.066 | 0.377 | 0.201 | 0.081 |
| simulation-campaign-v0.csv | Constitutional council with concrete-review backstop | 0.604 | 0.677 | 0.636 | 0.065 | 0.368 | 0.191 | 0.075 |
| simulation-campaign-v0.csv | Random panels with jurisdiction safeguards | 0.603 | 0.668 | 0.633 | 0.061 | 0.377 | 0.190 | 0.077 |
| simulation-campaign-v0.csv | Comparative 16-seat constitutional senates | 0.603 | 0.677 | 0.632 | 0.060 | 0.369 | 0.192 | 0.000 |
| simulation-campaign-v0.csv | Judicial electorate selection court | 0.602 | 0.666 | 0.641 | 0.065 | 0.372 | 0.187 | 0.000 |
| simulation-campaign-v0.csv | Stylized current U.S.-like supreme court | 0.598 | 0.661 | 0.638 | 0.216 | 0.392 | 0.224 | 0.000 |
| simulation-campaign-v0.csv | Supreme court with cross-checking constitutional court | 0.595 | 0.668 | 0.627 | 0.057 | 0.392 | 0.191 | 0.000 |
| simulation-campaign-v0.csv | Dual supreme courts with disagreement filter | 0.583 | 0.644 | 0.636 | 0.059 | 0.399 | 0.200 | 0.000 |
| simulation-campaign-v10.csv | No emergency relief without merits review | 0.602 | 0.648 | 0.636 | 0.012 | 0.383 | 0.197 | 0.000 |
| simulation-campaign-v10.csv | Jurisdiction stripping constrained by rights carveouts | 0.598 | 0.646 | 0.630 | 0.077 | 0.396 | 0.204 | 0.103 |
| simulation-campaign-v10.csv | 60 percent invalidation threshold | 0.598 | 0.654 | 0.629 | 0.073 | 0.393 | 0.211 | 0.000 |
| simulation-campaign-v10.csv | Automatic merits follow-up for emergency relief | 0.598 | 0.643 | 0.636 | 0.019 | 0.388 | 0.204 | 0.000 |
| simulation-campaign-v10.csv | 18-year staggered terms + regular appointments | 0.597 | 0.646 | 0.636 | 0.083 | 0.391 | 0.214 | 0.000 |
| simulation-campaign-v10.csv | Emergency integrity package | 0.595 | 0.643 | 0.641 | 0.020 | 0.391 | 0.199 | 0.000 |
| simulation-campaign-v10.csv | Constitutional remand before invalidation | 0.595 | 0.674 | 0.626 | 0.085 | 0.386 | 0.196 | 0.058 |
| simulation-campaign-v10.csv | Public-interest litigation filter | 0.594 | 0.652 | 0.630 | 0.076 | 0.387 | 0.199 | 0.000 |
| simulation-campaign-v10.csv | Peer recusal + reasoned emergency docket | 0.594 | 0.649 | 0.628 | 0.075 | 0.387 | 0.208 | 0.000 |
| simulation-campaign-v10.csv | Constitutional remand with override window | 0.594 | 0.680 | 0.626 | 0.052 | 0.389 | 0.198 | 0.063 |
| simulation-campaign-v10.csv | Mandatory written emergency reasoning | 0.594 | 0.650 | 0.631 | 0.052 | 0.389 | 0.208 | 0.000 |
| simulation-campaign-v10.csv | Independent recusal enforcement with substitutes | 0.593 | 0.649 | 0.635 | 0.079 | 0.393 | 0.210 | 0.000 |
| simulation-campaign-v10.csv | Retention-election accountability court | 0.593 | 0.652 | 0.626 | 0.081 | 0.401 | 0.206 | 0.084 |
| simulation-campaign-v10.csv | Randomized merits panels with en banc correction | 0.593 | 0.648 | 0.637 | 0.081 | 0.395 | 0.205 | 0.000 |
| simulation-campaign-v10.csv | Three-judge panels with en banc correction | 0.592 | 0.650 | 0.632 | 0.082 | 0.394 | 0.206 | 0.000 |
| simulation-campaign-v10.csv | Judicial review with legislative supermajority override | 0.592 | 0.639 | 0.642 | 0.081 | 0.413 | 0.215 | 0.107 |
| simulation-campaign-v10.csv | Expanded 15-seat court | 0.592 | 0.653 | 0.631 | 0.082 | 0.388 | 0.208 | 0.000 |
| simulation-campaign-v10.csv | Time-limited legislative override window | 0.592 | 0.643 | 0.636 | 0.079 | 0.408 | 0.214 | 0.097 |
| simulation-campaign-v10.csv | Nonpartisan commission appointments | 0.592 | 0.643 | 0.635 | 0.083 | 0.399 | 0.213 | 0.000 |
| simulation-campaign-v10.csv | Constitutional council with concrete-review backstop | 0.590 | 0.662 | 0.630 | 0.078 | 0.394 | 0.204 | 0.077 |
| simulation-campaign-v10.csv | Pre-enactment constitutional council | 0.589 | 0.656 | 0.631 | 0.076 | 0.401 | 0.210 | 0.088 |
| simulation-campaign-v10.csv | Random panels with jurisdiction safeguards | 0.589 | 0.647 | 0.628 | 0.073 | 0.401 | 0.202 | 0.086 |
| simulation-campaign-v10.csv | Judicial electorate selection court | 0.588 | 0.645 | 0.639 | 0.079 | 0.395 | 0.201 | 0.000 |
| simulation-campaign-v10.csv | Comparative 16-seat constitutional senates | 0.587 | 0.659 | 0.622 | 0.072 | 0.389 | 0.205 | 0.000 |
| simulation-campaign-v10.csv | Stylized current U.S.-like supreme court | 0.582 | 0.634 | 0.635 | 0.236 | 0.423 | 0.240 | 0.000 |
| simulation-campaign-v10.csv | Supreme court with cross-checking constitutional court | 0.579 | 0.649 | 0.615 | 0.068 | 0.413 | 0.201 | 0.000 |
| simulation-campaign-v10.csv | Dual supreme courts with disagreement filter | 0.567 | 0.626 | 0.628 | 0.071 | 0.423 | 0.213 | 0.000 |
| simulation-campaign-v15.csv | No emergency relief without merits review | 0.607 | 0.661 | 0.643 | 0.012 | 0.375 | 0.188 | 0.000 |
| simulation-campaign-v15.csv | 18-year staggered terms + regular appointments | 0.603 | 0.665 | 0.635 | 0.077 | 0.377 | 0.204 | 0.000 |
| simulation-campaign-v15.csv | 60 percent invalidation threshold | 0.602 | 0.666 | 0.629 | 0.068 | 0.378 | 0.202 | 0.000 |
| simulation-campaign-v15.csv | Public-interest litigation filter | 0.602 | 0.663 | 0.639 | 0.074 | 0.373 | 0.190 | 0.000 |
| simulation-campaign-v15.csv | Jurisdiction stripping constrained by rights carveouts | 0.602 | 0.654 | 0.642 | 0.076 | 0.389 | 0.198 | 0.094 |
| simulation-campaign-v15.csv | Emergency integrity package | 0.602 | 0.664 | 0.642 | 0.018 | 0.371 | 0.186 | 0.000 |
| simulation-campaign-v15.csv | Nonpartisan commission appointments | 0.600 | 0.660 | 0.635 | 0.075 | 0.375 | 0.195 | 0.000 |
| simulation-campaign-v15.csv | Retention-election accountability court | 0.600 | 0.665 | 0.633 | 0.076 | 0.388 | 0.196 | 0.067 |
| simulation-campaign-v15.csv | Automatic merits follow-up for emergency relief | 0.599 | 0.652 | 0.643 | 0.019 | 0.382 | 0.203 | 0.000 |
| simulation-campaign-v15.csv | Constitutional remand before invalidation | 0.599 | 0.680 | 0.636 | 0.080 | 0.378 | 0.193 | 0.063 |
| simulation-campaign-v15.csv | Mandatory written emergency reasoning | 0.599 | 0.661 | 0.639 | 0.048 | 0.379 | 0.201 | 0.000 |
| simulation-campaign-v15.csv | Independent recusal enforcement with substitutes | 0.598 | 0.660 | 0.637 | 0.078 | 0.379 | 0.199 | 0.000 |
| simulation-campaign-v15.csv | Peer recusal + reasoned emergency docket | 0.598 | 0.661 | 0.637 | 0.077 | 0.377 | 0.204 | 0.000 |
| simulation-campaign-v15.csv | Judicial review with legislative supermajority override | 0.598 | 0.657 | 0.639 | 0.078 | 0.389 | 0.203 | 0.086 |
| simulation-campaign-v15.csv | Time-limited legislative override window | 0.597 | 0.656 | 0.635 | 0.074 | 0.390 | 0.200 | 0.084 |
| simulation-campaign-v15.csv | Three-judge panels with en banc correction | 0.597 | 0.662 | 0.632 | 0.078 | 0.380 | 0.198 | 0.000 |
| simulation-campaign-v15.csv | Expanded 15-seat court | 0.597 | 0.660 | 0.637 | 0.078 | 0.378 | 0.203 | 0.000 |
| simulation-campaign-v15.csv | Constitutional remand with override window | 0.596 | 0.682 | 0.634 | 0.049 | 0.379 | 0.194 | 0.058 |
| simulation-campaign-v15.csv | Randomized merits panels with en banc correction | 0.596 | 0.658 | 0.634 | 0.074 | 0.375 | 0.195 | 0.000 |
| simulation-campaign-v15.csv | Pre-enactment constitutional council | 0.595 | 0.666 | 0.638 | 0.075 | 0.390 | 0.198 | 0.080 |
| simulation-campaign-v15.csv | Comparative 16-seat constitutional senates | 0.594 | 0.668 | 0.634 | 0.069 | 0.379 | 0.197 | 0.000 |
| simulation-campaign-v15.csv | Constitutional council with concrete-review backstop | 0.593 | 0.667 | 0.638 | 0.074 | 0.389 | 0.202 | 0.079 |
| simulation-campaign-v15.csv | Judicial electorate selection court | 0.593 | 0.662 | 0.640 | 0.077 | 0.379 | 0.189 | 0.000 |
| simulation-campaign-v15.csv | Random panels with jurisdiction safeguards | 0.592 | 0.657 | 0.633 | 0.073 | 0.390 | 0.199 | 0.077 |
| simulation-campaign-v15.csv | Stylized current U.S.-like supreme court | 0.585 | 0.651 | 0.636 | 0.236 | 0.407 | 0.233 | 0.000 |
| simulation-campaign-v15.csv | Supreme court with cross-checking constitutional court | 0.585 | 0.659 | 0.624 | 0.065 | 0.398 | 0.192 | 0.000 |
| simulation-campaign-v15.csv | Dual supreme courts with disagreement filter | 0.573 | 0.640 | 0.633 | 0.069 | 0.405 | 0.202 | 0.000 |
| simulation-campaign-v20.csv | 60 percent invalidation threshold | 0.602 | 0.659 | 0.637 | 0.067 | 0.383 | 0.205 | 0.000 |
| simulation-campaign-v20.csv | No emergency relief without merits review | 0.601 | 0.648 | 0.651 | 0.012 | 0.384 | 0.193 | 0.000 |
| simulation-campaign-v20.csv | 18-year staggered terms + regular appointments | 0.600 | 0.650 | 0.639 | 0.073 | 0.381 | 0.207 | 0.000 |
| simulation-campaign-v20.csv | Automatic merits follow-up for emergency relief | 0.598 | 0.649 | 0.646 | 0.019 | 0.385 | 0.204 | 0.000 |
| simulation-campaign-v20.csv | Constitutional remand before invalidation | 0.598 | 0.677 | 0.641 | 0.081 | 0.383 | 0.195 | 0.056 |
| simulation-campaign-v20.csv | Jurisdiction stripping constrained by rights carveouts | 0.597 | 0.644 | 0.646 | 0.079 | 0.402 | 0.207 | 0.101 |
| simulation-campaign-v20.csv | Public-interest litigation filter | 0.596 | 0.653 | 0.646 | 0.078 | 0.383 | 0.195 | 0.000 |
| simulation-campaign-v20.csv | Mandatory written emergency reasoning | 0.596 | 0.655 | 0.637 | 0.050 | 0.384 | 0.204 | 0.000 |
| simulation-campaign-v20.csv | Emergency integrity package | 0.596 | 0.651 | 0.646 | 0.019 | 0.383 | 0.198 | 0.000 |
| simulation-campaign-v20.csv | Nonpartisan commission appointments | 0.595 | 0.651 | 0.642 | 0.079 | 0.388 | 0.204 | 0.000 |
| simulation-campaign-v20.csv | Randomized merits panels with en banc correction | 0.595 | 0.654 | 0.640 | 0.076 | 0.384 | 0.196 | 0.000 |
| simulation-campaign-v20.csv | Peer recusal + reasoned emergency docket | 0.594 | 0.654 | 0.640 | 0.084 | 0.388 | 0.210 | 0.000 |
| simulation-campaign-v20.csv | Expanded 15-seat court | 0.594 | 0.652 | 0.643 | 0.080 | 0.384 | 0.209 | 0.000 |
| simulation-campaign-v20.csv | Independent recusal enforcement with substitutes | 0.594 | 0.651 | 0.641 | 0.081 | 0.387 | 0.200 | 0.000 |
| simulation-campaign-v20.csv | Retention-election accountability court | 0.594 | 0.651 | 0.637 | 0.084 | 0.401 | 0.204 | 0.082 |
| simulation-campaign-v20.csv | Three-judge panels with en banc correction | 0.593 | 0.649 | 0.645 | 0.080 | 0.390 | 0.205 | 0.000 |
| simulation-campaign-v20.csv | Constitutional remand with override window | 0.593 | 0.676 | 0.638 | 0.051 | 0.384 | 0.196 | 0.060 |
| simulation-campaign-v20.csv | Judicial review with legislative supermajority override | 0.592 | 0.647 | 0.642 | 0.084 | 0.403 | 0.210 | 0.092 |
| simulation-campaign-v20.csv | Time-limited legislative override window | 0.592 | 0.645 | 0.643 | 0.079 | 0.404 | 0.212 | 0.087 |
| simulation-campaign-v20.csv | Judicial electorate selection court | 0.590 | 0.653 | 0.647 | 0.081 | 0.389 | 0.193 | 0.000 |
| simulation-campaign-v20.csv | Random panels with jurisdiction safeguards | 0.590 | 0.653 | 0.638 | 0.073 | 0.400 | 0.202 | 0.076 |
| simulation-campaign-v20.csv | Pre-enactment constitutional council | 0.590 | 0.659 | 0.644 | 0.084 | 0.404 | 0.208 | 0.086 |
| simulation-campaign-v20.csv | Constitutional council with concrete-review backstop | 0.588 | 0.661 | 0.643 | 0.081 | 0.399 | 0.206 | 0.082 |
| simulation-campaign-v20.csv | Comparative 16-seat constitutional senates | 0.587 | 0.656 | 0.642 | 0.070 | 0.394 | 0.211 | 0.000 |
| simulation-campaign-v20.csv | Stylized current U.S.-like supreme court | 0.583 | 0.645 | 0.644 | 0.245 | 0.420 | 0.237 | 0.000 |
| simulation-campaign-v20.csv | Supreme court with cross-checking constitutional court | 0.581 | 0.654 | 0.624 | 0.073 | 0.401 | 0.194 | 0.000 |
| simulation-campaign-v20.csv | Dual supreme courts with disagreement filter | 0.569 | 0.628 | 0.639 | 0.071 | 0.417 | 0.208 | 0.000 |
| simulation-campaign-v21-paper.csv | No emergency relief without merits review | 0.619 | 0.677 | 0.645 | 0.007 | 0.347 | 0.173 | 0.000 |
| simulation-campaign-v21-paper.csv | 60 percent invalidation threshold | 0.616 | 0.684 | 0.630 | 0.057 | 0.352 | 0.186 | 0.000 |
| simulation-campaign-v21-paper.csv | Automatic merits follow-up for emergency relief | 0.616 | 0.677 | 0.642 | 0.013 | 0.348 | 0.181 | 0.000 |
| simulation-campaign-v21-paper.csv | 18-year staggered terms + regular appointments | 0.616 | 0.677 | 0.634 | 0.064 | 0.350 | 0.187 | 0.000 |
| simulation-campaign-v21-paper.csv | Jurisdiction stripping constrained by rights carveouts | 0.616 | 0.677 | 0.639 | 0.063 | 0.359 | 0.180 | 0.069 |
| simulation-campaign-v21-paper.csv | Nonpartisan commission appointments | 0.614 | 0.679 | 0.636 | 0.063 | 0.346 | 0.180 | 0.000 |
| simulation-campaign-v21-paper.csv | Public-interest litigation filter | 0.614 | 0.681 | 0.642 | 0.064 | 0.349 | 0.172 | 0.000 |
| simulation-campaign-v21-paper.csv | Mandatory written emergency reasoning | 0.613 | 0.681 | 0.637 | 0.040 | 0.353 | 0.189 | 0.000 |
| simulation-campaign-v21-paper.csv | Peer recusal + reasoned emergency docket | 0.613 | 0.681 | 0.637 | 0.064 | 0.350 | 0.187 | 0.000 |
| simulation-campaign-v21-paper.csv | Emergency integrity package | 0.613 | 0.679 | 0.643 | 0.013 | 0.352 | 0.177 | 0.000 |
| simulation-campaign-v21-paper.csv | Judicial review with legislative supermajority override | 0.612 | 0.677 | 0.641 | 0.065 | 0.363 | 0.185 | 0.064 |
| simulation-campaign-v21-paper.csv | Three-judge panels with en banc correction | 0.612 | 0.681 | 0.635 | 0.066 | 0.350 | 0.181 | 0.000 |
| simulation-campaign-v21-paper.csv | Retention-election accountability court | 0.612 | 0.681 | 0.637 | 0.067 | 0.366 | 0.184 | 0.074 |
| simulation-campaign-v21-paper.csv | Constitutional remand before invalidation | 0.611 | 0.695 | 0.636 | 0.067 | 0.351 | 0.176 | 0.048 |
| simulation-campaign-v21-paper.csv | Time-limited legislative override window | 0.611 | 0.677 | 0.637 | 0.069 | 0.364 | 0.189 | 0.078 |
| simulation-campaign-v21-paper.csv | Randomized merits panels with en banc correction | 0.610 | 0.678 | 0.636 | 0.069 | 0.352 | 0.181 | 0.000 |
| simulation-campaign-v21-paper.csv | Random panels with jurisdiction safeguards | 0.610 | 0.680 | 0.635 | 0.058 | 0.358 | 0.178 | 0.063 |
| simulation-campaign-v21-paper.csv | Expanded 15-seat court | 0.610 | 0.678 | 0.641 | 0.068 | 0.357 | 0.190 | 0.000 |
| simulation-campaign-v21-paper.csv | Independent recusal enforcement with substitutes | 0.610 | 0.678 | 0.639 | 0.064 | 0.355 | 0.182 | 0.000 |
| simulation-campaign-v21-paper.csv | Constitutional remand with override window | 0.608 | 0.697 | 0.635 | 0.041 | 0.352 | 0.180 | 0.053 |
| simulation-campaign-v21-paper.csv | Constitutional council with concrete-review backstop | 0.607 | 0.689 | 0.636 | 0.067 | 0.356 | 0.181 | 0.058 |
| simulation-campaign-v21-paper.csv | Judicial electorate selection court | 0.607 | 0.680 | 0.641 | 0.065 | 0.356 | 0.176 | 0.000 |
| simulation-campaign-v21-paper.csv | Pre-enactment constitutional council | 0.607 | 0.679 | 0.644 | 0.063 | 0.368 | 0.188 | 0.083 |
| simulation-campaign-v21-paper.csv | Comparative 16-seat constitutional senates | 0.606 | 0.685 | 0.630 | 0.054 | 0.347 | 0.181 | 0.000 |
| simulation-campaign-v21-paper.csv | Stylized current U.S.-like supreme court | 0.599 | 0.667 | 0.642 | 0.222 | 0.387 | 0.220 | 0.000 |
| simulation-campaign-v21-paper.csv | Supreme court with cross-checking constitutional court | 0.598 | 0.677 | 0.626 | 0.054 | 0.374 | 0.182 | 0.000 |
| simulation-campaign-v21-paper.csv | Dual supreme courts with disagreement filter | 0.586 | 0.656 | 0.640 | 0.059 | 0.388 | 0.190 | 0.000 |
| simulation-campaign-v5.csv | No emergency relief without merits review | 0.602 | 0.643 | 0.638 | 0.012 | 0.387 | 0.195 | 0.000 |
| simulation-campaign-v5.csv | 18-year staggered terms + regular appointments | 0.600 | 0.646 | 0.635 | 0.076 | 0.395 | 0.211 | 0.000 |
| simulation-campaign-v5.csv | 60 percent invalidation threshold | 0.599 | 0.648 | 0.623 | 0.067 | 0.390 | 0.212 | 0.000 |
| simulation-campaign-v5.csv | Constitutional remand before invalidation | 0.599 | 0.673 | 0.631 | 0.076 | 0.390 | 0.195 | 0.071 |
| simulation-campaign-v5.csv | Public-interest litigation filter | 0.597 | 0.651 | 0.633 | 0.075 | 0.390 | 0.196 | 0.000 |
| simulation-campaign-v5.csv | Automatic merits follow-up for emergency relief | 0.597 | 0.636 | 0.638 | 0.018 | 0.390 | 0.207 | 0.000 |
| simulation-campaign-v5.csv | Jurisdiction stripping constrained by rights carveouts | 0.597 | 0.638 | 0.631 | 0.075 | 0.405 | 0.207 | 0.114 |
| simulation-campaign-v5.csv | Nonpartisan commission appointments | 0.597 | 0.641 | 0.634 | 0.074 | 0.397 | 0.204 | 0.000 |
| simulation-campaign-v5.csv | Emergency integrity package | 0.597 | 0.644 | 0.641 | 0.019 | 0.394 | 0.199 | 0.000 |
| simulation-campaign-v5.csv | Peer recusal + reasoned emergency docket | 0.596 | 0.647 | 0.629 | 0.072 | 0.386 | 0.206 | 0.000 |
| simulation-campaign-v5.csv | Retention-election accountability court | 0.596 | 0.646 | 0.624 | 0.073 | 0.400 | 0.200 | 0.099 |
| simulation-campaign-v5.csv | Three-judge panels with en banc correction | 0.596 | 0.647 | 0.634 | 0.078 | 0.397 | 0.206 | 0.000 |
| simulation-campaign-v5.csv | Mandatory written emergency reasoning | 0.595 | 0.646 | 0.629 | 0.047 | 0.390 | 0.211 | 0.000 |
| simulation-campaign-v5.csv | Independent recusal enforcement with substitutes | 0.594 | 0.644 | 0.633 | 0.076 | 0.390 | 0.203 | 0.000 |
| simulation-campaign-v5.csv | Constitutional remand with override window | 0.594 | 0.671 | 0.629 | 0.046 | 0.394 | 0.200 | 0.072 |
| simulation-campaign-v5.csv | Time-limited legislative override window | 0.593 | 0.642 | 0.628 | 0.072 | 0.406 | 0.210 | 0.109 |
| simulation-campaign-v5.csv | Random panels with jurisdiction safeguards | 0.593 | 0.646 | 0.629 | 0.068 | 0.400 | 0.198 | 0.097 |
| simulation-campaign-v5.csv | Judicial review with legislative supermajority override | 0.593 | 0.638 | 0.633 | 0.074 | 0.408 | 0.211 | 0.105 |
| simulation-campaign-v5.csv | Expanded 15-seat court | 0.592 | 0.641 | 0.629 | 0.074 | 0.391 | 0.214 | 0.000 |
| simulation-campaign-v5.csv | Constitutional council with concrete-review backstop | 0.591 | 0.658 | 0.631 | 0.072 | 0.400 | 0.204 | 0.094 |
| simulation-campaign-v5.csv | Randomized merits panels with en banc correction | 0.591 | 0.641 | 0.632 | 0.079 | 0.395 | 0.211 | 0.000 |
| simulation-campaign-v5.csv | Comparative 16-seat constitutional senates | 0.591 | 0.655 | 0.625 | 0.068 | 0.390 | 0.207 | 0.000 |
| simulation-campaign-v5.csv | Pre-enactment constitutional council | 0.590 | 0.647 | 0.634 | 0.074 | 0.404 | 0.207 | 0.102 |
| simulation-campaign-v5.csv | Judicial electorate selection court | 0.588 | 0.641 | 0.637 | 0.075 | 0.396 | 0.203 | 0.000 |
| simulation-campaign-v5.csv | Stylized current U.S.-like supreme court | 0.583 | 0.638 | 0.627 | 0.240 | 0.423 | 0.239 | 0.000 |
| simulation-campaign-v5.csv | Supreme court with cross-checking constitutional court | 0.579 | 0.647 | 0.612 | 0.067 | 0.420 | 0.204 | 0.000 |
| simulation-campaign-v5.csv | Dual supreme courts with disagreement filter | 0.571 | 0.620 | 0.632 | 0.066 | 0.418 | 0.207 | 0.000 |
| simulation-manipulation-stress.csv | No emergency relief without merits review | 0.620 | 0.677 | 0.642 | 0.007 | 0.351 | 0.174 | 0.000 |
| simulation-manipulation-stress.csv | 18-year staggered terms + regular appointments | 0.618 | 0.677 | 0.638 | 0.060 | 0.351 | 0.189 | 0.000 |
| simulation-manipulation-stress.csv | 60 percent invalidation threshold | 0.617 | 0.678 | 0.630 | 0.054 | 0.349 | 0.188 | 0.000 |
| simulation-manipulation-stress.csv | Jurisdiction stripping constrained by rights carveouts | 0.616 | 0.671 | 0.639 | 0.063 | 0.364 | 0.185 | 0.088 |
| simulation-manipulation-stress.csv | Retention-election accountability court | 0.614 | 0.675 | 0.636 | 0.062 | 0.363 | 0.183 | 0.074 |
| simulation-manipulation-stress.csv | Time-limited legislative override window | 0.614 | 0.674 | 0.640 | 0.062 | 0.366 | 0.185 | 0.078 |
| simulation-manipulation-stress.csv | Nonpartisan commission appointments | 0.614 | 0.677 | 0.634 | 0.063 | 0.352 | 0.182 | 0.000 |
| simulation-manipulation-stress.csv | Automatic merits follow-up for emergency relief | 0.614 | 0.669 | 0.646 | 0.013 | 0.359 | 0.190 | 0.000 |
| simulation-manipulation-stress.csv | Emergency integrity package | 0.614 | 0.676 | 0.644 | 0.013 | 0.354 | 0.178 | 0.000 |
| simulation-manipulation-stress.csv | Constitutional remand before invalidation | 0.614 | 0.696 | 0.637 | 0.062 | 0.354 | 0.177 | 0.054 |
| simulation-manipulation-stress.csv | Peer recusal + reasoned emergency docket | 0.614 | 0.677 | 0.639 | 0.064 | 0.354 | 0.190 | 0.000 |
| simulation-manipulation-stress.csv | Public-interest litigation filter | 0.613 | 0.678 | 0.640 | 0.067 | 0.354 | 0.176 | 0.000 |
| simulation-manipulation-stress.csv | Three-judge panels with en banc correction | 0.613 | 0.678 | 0.636 | 0.065 | 0.356 | 0.184 | 0.000 |
| simulation-manipulation-stress.csv | Judicial review with legislative supermajority override | 0.612 | 0.674 | 0.639 | 0.064 | 0.363 | 0.187 | 0.073 |
| simulation-manipulation-stress.csv | Independent recusal enforcement with substitutes | 0.612 | 0.671 | 0.643 | 0.064 | 0.358 | 0.186 | 0.000 |
| simulation-manipulation-stress.csv | Mandatory written emergency reasoning | 0.611 | 0.675 | 0.636 | 0.042 | 0.360 | 0.194 | 0.000 |
| simulation-manipulation-stress.csv | Expanded 15-seat court | 0.611 | 0.674 | 0.638 | 0.062 | 0.357 | 0.192 | 0.000 |
| simulation-manipulation-stress.csv | Pre-enactment constitutional council | 0.611 | 0.683 | 0.634 | 0.059 | 0.362 | 0.185 | 0.069 |
| simulation-manipulation-stress.csv | Randomized merits panels with en banc correction | 0.611 | 0.678 | 0.637 | 0.065 | 0.359 | 0.185 | 0.000 |
| simulation-manipulation-stress.csv | Constitutional remand with override window | 0.610 | 0.696 | 0.633 | 0.037 | 0.352 | 0.174 | 0.051 |
| simulation-manipulation-stress.csv | Random panels with jurisdiction safeguards | 0.609 | 0.676 | 0.628 | 0.055 | 0.360 | 0.179 | 0.072 |
| simulation-manipulation-stress.csv | Constitutional council with concrete-review backstop | 0.608 | 0.686 | 0.632 | 0.062 | 0.356 | 0.184 | 0.063 |
| simulation-manipulation-stress.csv | Judicial electorate selection court | 0.607 | 0.676 | 0.641 | 0.063 | 0.357 | 0.179 | 0.000 |
| simulation-manipulation-stress.csv | Comparative 16-seat constitutional senates | 0.606 | 0.681 | 0.632 | 0.057 | 0.358 | 0.182 | 0.000 |
| simulation-manipulation-stress.csv | Stylized current U.S.-like supreme court | 0.601 | 0.667 | 0.637 | 0.207 | 0.385 | 0.218 | 0.000 |
| simulation-manipulation-stress.csv | Supreme court with cross-checking constitutional court | 0.599 | 0.677 | 0.618 | 0.054 | 0.371 | 0.180 | 0.000 |
| simulation-manipulation-stress.csv | Dual supreme courts with disagreement filter | 0.591 | 0.660 | 0.634 | 0.056 | 0.381 | 0.186 | 0.000 |
