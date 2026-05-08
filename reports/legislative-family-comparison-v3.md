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
| simulation-campaign-v0.csv | 0.281 | 0.593 | 0.167 | 0.200 | 0.280 | 0.144 | 0.597 | 0.228 | No emergency relief without merits review (0.613) |
| simulation-campaign-v5.csv | 0.429 | 0.554 | 0.239 | 0.200 | 0.280 | 0.262 | 0.562 | 0.285 | No emergency relief without merits review (0.603) |
| simulation-campaign-v10.csv | 0.518 | 0.582 | 0.268 | 0.200 | 0.227 | 0.326 | 0.565 | 0.307 | No emergency relief without merits review (0.602) |
| simulation-campaign-v15.csv | 0.500 | 0.594 | 0.255 | 0.110 | 0.230 | 0.323 | 0.513 | 0.293 | No emergency relief without merits review (0.605) |
| simulation-campaign-v20.csv | 0.584 | 0.564 | 0.251 | 0.116 | 0.246 | 0.334 | 0.494 | 0.302 | No emergency relief without merits review (0.602) |
| simulation-campaign-v21-paper.csv | 0.343 | 0.610 | 0.175 | 0.104 | 0.237 | 0.120 | 0.547 | 0.213 | No emergency relief without merits review (0.619) |
| simulation-manipulation-stress.csv | 0.283 | 0.582 | 0.102 | 0.163 | 0.274 | 0.097 | 0.552 | 0.202 | No emergency relief without merits review (0.618) |

## Scenario Sensitivity By Family

| Family | Scenario | Directional | Legal | Rights | Shadow | Conflict | Strategic | Override att. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| simulation-campaign-v0.csv | No emergency relief without merits review | 0.613 | 0.662 | 0.651 | 0.009 | 0.373 | 0.189 | 0.000 |
| simulation-campaign-v0.csv | 18-year staggered terms + regular appointments | 0.613 | 0.667 | 0.643 | 0.068 | 0.371 | 0.198 | 0.000 |
| simulation-campaign-v0.csv | Jurisdiction stripping constrained by rights carveouts | 0.613 | 0.664 | 0.650 | 0.067 | 0.384 | 0.197 | 0.098 |
| simulation-campaign-v0.csv | 60 percent invalidation threshold | 0.612 | 0.671 | 0.638 | 0.062 | 0.379 | 0.203 | 0.000 |
| simulation-campaign-v0.csv | Nonpartisan commission appointments | 0.610 | 0.665 | 0.642 | 0.067 | 0.372 | 0.194 | 0.000 |
| simulation-campaign-v0.csv | Automatic merits follow-up for emergency relief | 0.609 | 0.662 | 0.647 | 0.014 | 0.371 | 0.196 | 0.000 |
| simulation-campaign-v0.csv | Peer recusal + reasoned emergency docket | 0.609 | 0.668 | 0.641 | 0.063 | 0.373 | 0.200 | 0.000 |
| simulation-campaign-v0.csv | Emergency integrity package | 0.609 | 0.666 | 0.650 | 0.015 | 0.377 | 0.191 | 0.000 |
| simulation-campaign-v0.csv | Public-interest litigation filter | 0.608 | 0.664 | 0.652 | 0.064 | 0.377 | 0.193 | 0.000 |
| simulation-campaign-v0.csv | Mandatory written emergency reasoning | 0.607 | 0.669 | 0.645 | 0.041 | 0.381 | 0.205 | 0.000 |
| simulation-campaign-v0.csv | Randomized merits panels with en banc correction | 0.607 | 0.670 | 0.641 | 0.066 | 0.370 | 0.190 | 0.000 |
| simulation-campaign-v0.csv | Constitutional remand before invalidation | 0.607 | 0.686 | 0.643 | 0.070 | 0.378 | 0.192 | 0.069 |
| simulation-campaign-v0.csv | Independent recusal enforcement with substitutes | 0.607 | 0.666 | 0.647 | 0.067 | 0.376 | 0.194 | 0.000 |
| simulation-campaign-v0.csv | Three-judge panels with en banc correction | 0.606 | 0.663 | 0.644 | 0.069 | 0.379 | 0.191 | 0.000 |
| simulation-campaign-v0.csv | Retention-election accountability court | 0.606 | 0.664 | 0.644 | 0.070 | 0.391 | 0.200 | 0.086 |
| simulation-campaign-v0.csv | Time-limited legislative override window | 0.606 | 0.663 | 0.644 | 0.071 | 0.390 | 0.200 | 0.089 |
| simulation-campaign-v0.csv | Constitutional remand with override window | 0.605 | 0.689 | 0.637 | 0.040 | 0.374 | 0.189 | 0.055 |
| simulation-campaign-v0.csv | Judicial review with legislative supermajority override | 0.605 | 0.657 | 0.648 | 0.067 | 0.393 | 0.206 | 0.101 |
| simulation-campaign-v0.csv | Expanded 15-seat court | 0.604 | 0.664 | 0.646 | 0.071 | 0.381 | 0.207 | 0.000 |
| simulation-campaign-v0.csv | Pre-enactment constitutional council | 0.604 | 0.673 | 0.643 | 0.069 | 0.389 | 0.197 | 0.087 |
| simulation-campaign-v0.csv | Random panels with jurisdiction safeguards | 0.603 | 0.667 | 0.640 | 0.063 | 0.387 | 0.193 | 0.086 |
| simulation-campaign-v0.csv | Comparative 16-seat constitutional senates | 0.602 | 0.675 | 0.640 | 0.059 | 0.378 | 0.196 | 0.000 |
| simulation-campaign-v0.csv | Constitutional council with concrete-review backstop | 0.600 | 0.671 | 0.649 | 0.069 | 0.390 | 0.203 | 0.090 |
| simulation-campaign-v0.csv | Stylized current U.S.-like supreme court | 0.600 | 0.660 | 0.645 | 0.215 | 0.393 | 0.226 | 0.000 |
| simulation-campaign-v0.csv | Supreme court with cross-checking constitutional court | 0.593 | 0.667 | 0.627 | 0.060 | 0.397 | 0.195 | 0.000 |
| simulation-campaign-v0.csv | Dual supreme courts with disagreement filter | 0.582 | 0.642 | 0.643 | 0.060 | 0.405 | 0.204 | 0.000 |
| simulation-campaign-v10.csv | No emergency relief without merits review | 0.602 | 0.650 | 0.641 | 0.012 | 0.390 | 0.195 | 0.000 |
| simulation-campaign-v10.csv | 18-year staggered terms + regular appointments | 0.598 | 0.649 | 0.638 | 0.079 | 0.397 | 0.214 | 0.000 |
| simulation-campaign-v10.csv | 60 percent invalidation threshold | 0.597 | 0.654 | 0.629 | 0.074 | 0.399 | 0.215 | 0.000 |
| simulation-campaign-v10.csv | Automatic merits follow-up for emergency relief | 0.596 | 0.641 | 0.643 | 0.020 | 0.398 | 0.210 | 0.000 |
| simulation-campaign-v10.csv | Constitutional remand before invalidation | 0.595 | 0.674 | 0.633 | 0.080 | 0.394 | 0.198 | 0.059 |
| simulation-campaign-v10.csv | Jurisdiction stripping constrained by rights carveouts | 0.595 | 0.643 | 0.637 | 0.083 | 0.410 | 0.210 | 0.116 |
| simulation-campaign-v10.csv | Retention-election accountability court | 0.594 | 0.652 | 0.634 | 0.080 | 0.409 | 0.207 | 0.084 |
| simulation-campaign-v10.csv | Emergency integrity package | 0.594 | 0.643 | 0.644 | 0.020 | 0.398 | 0.202 | 0.000 |
| simulation-campaign-v10.csv | Three-judge panels with en banc correction | 0.593 | 0.649 | 0.640 | 0.084 | 0.398 | 0.205 | 0.000 |
| simulation-campaign-v10.csv | Public-interest litigation filter | 0.593 | 0.648 | 0.640 | 0.083 | 0.398 | 0.202 | 0.000 |
| simulation-campaign-v10.csv | Peer recusal + reasoned emergency docket | 0.593 | 0.646 | 0.634 | 0.080 | 0.396 | 0.215 | 0.000 |
| simulation-campaign-v10.csv | Mandatory written emergency reasoning | 0.592 | 0.650 | 0.633 | 0.057 | 0.400 | 0.214 | 0.000 |
| simulation-campaign-v10.csv | Randomized merits panels with en banc correction | 0.592 | 0.647 | 0.633 | 0.081 | 0.395 | 0.203 | 0.000 |
| simulation-campaign-v10.csv | Time-limited legislative override window | 0.591 | 0.638 | 0.644 | 0.078 | 0.418 | 0.216 | 0.114 |
| simulation-campaign-v10.csv | Judicial review with legislative supermajority override | 0.591 | 0.646 | 0.638 | 0.085 | 0.417 | 0.215 | 0.095 |
| simulation-campaign-v10.csv | Constitutional remand with override window | 0.591 | 0.675 | 0.633 | 0.054 | 0.401 | 0.208 | 0.069 |
| simulation-campaign-v10.csv | Nonpartisan commission appointments | 0.591 | 0.644 | 0.638 | 0.084 | 0.404 | 0.213 | 0.000 |
| simulation-campaign-v10.csv | Independent recusal enforcement with substitutes | 0.591 | 0.645 | 0.639 | 0.082 | 0.401 | 0.209 | 0.000 |
| simulation-campaign-v10.csv | Expanded 15-seat court | 0.590 | 0.648 | 0.638 | 0.083 | 0.399 | 0.216 | 0.000 |
| simulation-campaign-v10.csv | Random panels with jurisdiction safeguards | 0.589 | 0.648 | 0.634 | 0.073 | 0.412 | 0.204 | 0.098 |
| simulation-campaign-v10.csv | Comparative 16-seat constitutional senates | 0.588 | 0.655 | 0.633 | 0.072 | 0.396 | 0.206 | 0.000 |
| simulation-campaign-v10.csv | Pre-enactment constitutional council | 0.587 | 0.652 | 0.640 | 0.081 | 0.414 | 0.214 | 0.097 |
| simulation-campaign-v10.csv | Constitutional council with concrete-review backstop | 0.587 | 0.659 | 0.641 | 0.086 | 0.413 | 0.214 | 0.084 |
| simulation-campaign-v10.csv | Stylized current U.S.-like supreme court | 0.584 | 0.639 | 0.642 | 0.236 | 0.420 | 0.242 | 0.000 |
| simulation-campaign-v10.csv | Supreme court with cross-checking constitutional court | 0.578 | 0.651 | 0.617 | 0.073 | 0.421 | 0.202 | 0.000 |
| simulation-campaign-v10.csv | Dual supreme courts with disagreement filter | 0.567 | 0.626 | 0.633 | 0.071 | 0.427 | 0.213 | 0.000 |
| simulation-campaign-v15.csv | No emergency relief without merits review | 0.605 | 0.656 | 0.649 | 0.012 | 0.383 | 0.193 | 0.000 |
| simulation-campaign-v15.csv | 60 percent invalidation threshold | 0.603 | 0.666 | 0.636 | 0.070 | 0.387 | 0.208 | 0.000 |
| simulation-campaign-v15.csv | 18-year staggered terms + regular appointments | 0.602 | 0.658 | 0.643 | 0.077 | 0.387 | 0.208 | 0.000 |
| simulation-campaign-v15.csv | Retention-election accountability court | 0.601 | 0.666 | 0.637 | 0.076 | 0.387 | 0.197 | 0.071 |
| simulation-campaign-v15.csv | Jurisdiction stripping constrained by rights carveouts | 0.601 | 0.656 | 0.645 | 0.079 | 0.399 | 0.203 | 0.097 |
| simulation-campaign-v15.csv | Emergency integrity package | 0.599 | 0.662 | 0.648 | 0.019 | 0.386 | 0.194 | 0.000 |
| simulation-campaign-v15.csv | Constitutional remand before invalidation | 0.599 | 0.683 | 0.636 | 0.081 | 0.381 | 0.192 | 0.056 |
| simulation-campaign-v15.csv | Nonpartisan commission appointments | 0.599 | 0.657 | 0.641 | 0.076 | 0.386 | 0.200 | 0.000 |
| simulation-campaign-v15.csv | Public-interest litigation filter | 0.598 | 0.660 | 0.645 | 0.078 | 0.383 | 0.196 | 0.000 |
| simulation-campaign-v15.csv | Time-limited legislative override window | 0.598 | 0.657 | 0.643 | 0.079 | 0.397 | 0.202 | 0.082 |
| simulation-campaign-v15.csv | Automatic merits follow-up for emergency relief | 0.598 | 0.649 | 0.652 | 0.020 | 0.394 | 0.206 | 0.000 |
| simulation-campaign-v15.csv | Peer recusal + reasoned emergency docket | 0.598 | 0.658 | 0.641 | 0.077 | 0.384 | 0.208 | 0.000 |
| simulation-campaign-v15.csv | Mandatory written emergency reasoning | 0.598 | 0.660 | 0.643 | 0.051 | 0.386 | 0.208 | 0.000 |
| simulation-campaign-v15.csv | Randomized merits panels with en banc correction | 0.597 | 0.660 | 0.639 | 0.077 | 0.378 | 0.197 | 0.000 |
| simulation-campaign-v15.csv | Three-judge panels with en banc correction | 0.597 | 0.659 | 0.644 | 0.083 | 0.388 | 0.201 | 0.000 |
| simulation-campaign-v15.csv | Independent recusal enforcement with substitutes | 0.597 | 0.661 | 0.642 | 0.082 | 0.385 | 0.203 | 0.000 |
| simulation-campaign-v15.csv | Constitutional remand with override window | 0.596 | 0.683 | 0.643 | 0.050 | 0.388 | 0.196 | 0.064 |
| simulation-campaign-v15.csv | Judicial review with legislative supermajority override | 0.596 | 0.658 | 0.639 | 0.080 | 0.395 | 0.205 | 0.081 |
| simulation-campaign-v15.csv | Random panels with jurisdiction safeguards | 0.595 | 0.657 | 0.643 | 0.070 | 0.394 | 0.196 | 0.080 |
| simulation-campaign-v15.csv | Expanded 15-seat court | 0.595 | 0.656 | 0.640 | 0.077 | 0.386 | 0.210 | 0.000 |
| simulation-campaign-v15.csv | Pre-enactment constitutional council | 0.593 | 0.666 | 0.642 | 0.076 | 0.399 | 0.206 | 0.087 |
| simulation-campaign-v15.csv | Constitutional council with concrete-review backstop | 0.593 | 0.669 | 0.644 | 0.078 | 0.397 | 0.202 | 0.077 |
| simulation-campaign-v15.csv | Comparative 16-seat constitutional senates | 0.593 | 0.670 | 0.639 | 0.072 | 0.389 | 0.202 | 0.000 |
| simulation-campaign-v15.csv | Stylized current U.S.-like supreme court | 0.588 | 0.656 | 0.637 | 0.231 | 0.398 | 0.232 | 0.000 |
| simulation-campaign-v15.csv | Supreme court with cross-checking constitutional court | 0.583 | 0.656 | 0.627 | 0.068 | 0.408 | 0.199 | 0.000 |
| simulation-campaign-v15.csv | Dual supreme courts with disagreement filter | 0.573 | 0.638 | 0.643 | 0.071 | 0.416 | 0.204 | 0.000 |
| simulation-campaign-v20.csv | No emergency relief without merits review | 0.602 | 0.652 | 0.650 | 0.012 | 0.388 | 0.197 | 0.000 |
| simulation-campaign-v20.csv | 60 percent invalidation threshold | 0.599 | 0.657 | 0.640 | 0.070 | 0.390 | 0.212 | 0.000 |
| simulation-campaign-v20.csv | 18-year staggered terms + regular appointments | 0.599 | 0.649 | 0.643 | 0.079 | 0.387 | 0.211 | 0.000 |
| simulation-campaign-v20.csv | Jurisdiction stripping constrained by rights carveouts | 0.597 | 0.646 | 0.647 | 0.080 | 0.403 | 0.207 | 0.095 |
| simulation-campaign-v20.csv | Constitutional remand before invalidation | 0.597 | 0.675 | 0.643 | 0.081 | 0.389 | 0.198 | 0.061 |
| simulation-campaign-v20.csv | Automatic merits follow-up for emergency relief | 0.596 | 0.643 | 0.654 | 0.020 | 0.397 | 0.207 | 0.000 |
| simulation-campaign-v20.csv | Public-interest litigation filter | 0.595 | 0.654 | 0.655 | 0.082 | 0.395 | 0.201 | 0.000 |
| simulation-campaign-v20.csv | Emergency integrity package | 0.594 | 0.648 | 0.653 | 0.020 | 0.393 | 0.205 | 0.000 |
| simulation-campaign-v20.csv | Retention-election accountability court | 0.594 | 0.654 | 0.642 | 0.084 | 0.405 | 0.207 | 0.084 |
| simulation-campaign-v20.csv | Mandatory written emergency reasoning | 0.594 | 0.649 | 0.644 | 0.051 | 0.392 | 0.211 | 0.000 |
| simulation-campaign-v20.csv | Expanded 15-seat court | 0.594 | 0.653 | 0.644 | 0.081 | 0.386 | 0.208 | 0.000 |
| simulation-campaign-v20.csv | Nonpartisan commission appointments | 0.594 | 0.647 | 0.646 | 0.082 | 0.397 | 0.205 | 0.000 |
| simulation-campaign-v20.csv | Independent recusal enforcement with substitutes | 0.593 | 0.652 | 0.646 | 0.082 | 0.394 | 0.201 | 0.000 |
| simulation-campaign-v20.csv | Randomized merits panels with en banc correction | 0.593 | 0.651 | 0.646 | 0.079 | 0.392 | 0.202 | 0.000 |
| simulation-campaign-v20.csv | Peer recusal + reasoned emergency docket | 0.593 | 0.652 | 0.643 | 0.085 | 0.392 | 0.213 | 0.000 |
| simulation-campaign-v20.csv | Judicial review with legislative supermajority override | 0.591 | 0.646 | 0.643 | 0.083 | 0.406 | 0.209 | 0.092 |
| simulation-campaign-v20.csv | Constitutional remand with override window | 0.591 | 0.675 | 0.644 | 0.055 | 0.399 | 0.200 | 0.068 |
| simulation-campaign-v20.csv | Comparative 16-seat constitutional senates | 0.590 | 0.656 | 0.642 | 0.067 | 0.391 | 0.205 | 0.000 |
| simulation-campaign-v20.csv | Three-judge panels with en banc correction | 0.589 | 0.644 | 0.645 | 0.081 | 0.397 | 0.211 | 0.000 |
| simulation-campaign-v20.csv | Time-limited legislative override window | 0.589 | 0.645 | 0.645 | 0.083 | 0.414 | 0.218 | 0.102 |
| simulation-campaign-v20.csv | Random panels with jurisdiction safeguards | 0.589 | 0.653 | 0.637 | 0.075 | 0.403 | 0.203 | 0.077 |
| simulation-campaign-v20.csv | Pre-enactment constitutional council | 0.589 | 0.656 | 0.648 | 0.081 | 0.406 | 0.210 | 0.087 |
| simulation-campaign-v20.csv | Constitutional council with concrete-review backstop | 0.586 | 0.660 | 0.650 | 0.085 | 0.410 | 0.212 | 0.081 |
| simulation-campaign-v20.csv | Stylized current U.S.-like supreme court | 0.584 | 0.643 | 0.650 | 0.245 | 0.417 | 0.238 | 0.000 |
| simulation-campaign-v20.csv | Supreme court with cross-checking constitutional court | 0.578 | 0.651 | 0.624 | 0.069 | 0.414 | 0.198 | 0.000 |
| simulation-campaign-v20.csv | Dual supreme courts with disagreement filter | 0.564 | 0.622 | 0.643 | 0.072 | 0.425 | 0.213 | 0.000 |
| simulation-campaign-v21-paper.csv | No emergency relief without merits review | 0.619 | 0.678 | 0.649 | 0.008 | 0.356 | 0.177 | 0.000 |
| simulation-campaign-v21-paper.csv | 60 percent invalidation threshold | 0.617 | 0.683 | 0.635 | 0.055 | 0.357 | 0.190 | 0.000 |
| simulation-campaign-v21-paper.csv | Jurisdiction stripping constrained by rights carveouts | 0.616 | 0.679 | 0.643 | 0.067 | 0.368 | 0.182 | 0.073 |
| simulation-campaign-v21-paper.csv | 18-year staggered terms + regular appointments | 0.616 | 0.678 | 0.643 | 0.068 | 0.365 | 0.193 | 0.000 |
| simulation-campaign-v21-paper.csv | Automatic merits follow-up for emergency relief | 0.614 | 0.679 | 0.644 | 0.013 | 0.359 | 0.189 | 0.000 |
| simulation-campaign-v21-paper.csv | Nonpartisan commission appointments | 0.614 | 0.677 | 0.641 | 0.065 | 0.357 | 0.185 | 0.000 |
| simulation-campaign-v21-paper.csv | Peer recusal + reasoned emergency docket | 0.613 | 0.680 | 0.644 | 0.064 | 0.356 | 0.188 | 0.000 |
| simulation-campaign-v21-paper.csv | Public-interest litigation filter | 0.613 | 0.676 | 0.648 | 0.065 | 0.358 | 0.179 | 0.000 |
| simulation-campaign-v21-paper.csv | Emergency integrity package | 0.612 | 0.682 | 0.645 | 0.013 | 0.360 | 0.180 | 0.000 |
| simulation-campaign-v21-paper.csv | Three-judge panels with en banc correction | 0.612 | 0.680 | 0.641 | 0.065 | 0.357 | 0.183 | 0.000 |
| simulation-campaign-v21-paper.csv | Randomized merits panels with en banc correction | 0.612 | 0.677 | 0.646 | 0.064 | 0.360 | 0.181 | 0.000 |
| simulation-campaign-v21-paper.csv | Retention-election accountability court | 0.611 | 0.681 | 0.638 | 0.067 | 0.367 | 0.188 | 0.068 |
| simulation-campaign-v21-paper.csv | Judicial review with legislative supermajority override | 0.611 | 0.676 | 0.647 | 0.069 | 0.373 | 0.192 | 0.075 |
| simulation-campaign-v21-paper.csv | Mandatory written emergency reasoning | 0.611 | 0.679 | 0.645 | 0.040 | 0.368 | 0.197 | 0.000 |
| simulation-campaign-v21-paper.csv | Time-limited legislative override window | 0.611 | 0.679 | 0.644 | 0.068 | 0.374 | 0.188 | 0.071 |
| simulation-campaign-v21-paper.csv | Constitutional remand before invalidation | 0.610 | 0.693 | 0.642 | 0.065 | 0.358 | 0.182 | 0.053 |
| simulation-campaign-v21-paper.csv | Expanded 15-seat court | 0.609 | 0.676 | 0.645 | 0.066 | 0.366 | 0.195 | 0.000 |
| simulation-campaign-v21-paper.csv | Constitutional remand with override window | 0.609 | 0.701 | 0.641 | 0.041 | 0.360 | 0.177 | 0.051 |
| simulation-campaign-v21-paper.csv | Independent recusal enforcement with substitutes | 0.609 | 0.677 | 0.643 | 0.068 | 0.363 | 0.188 | 0.000 |
| simulation-campaign-v21-paper.csv | Random panels with jurisdiction safeguards | 0.608 | 0.679 | 0.641 | 0.061 | 0.370 | 0.181 | 0.068 |
| simulation-campaign-v21-paper.csv | Constitutional council with concrete-review backstop | 0.607 | 0.689 | 0.643 | 0.066 | 0.367 | 0.186 | 0.060 |
| simulation-campaign-v21-paper.csv | Pre-enactment constitutional council | 0.607 | 0.682 | 0.645 | 0.064 | 0.371 | 0.188 | 0.076 |
| simulation-campaign-v21-paper.csv | Comparative 16-seat constitutional senates | 0.605 | 0.684 | 0.636 | 0.058 | 0.357 | 0.186 | 0.000 |
| simulation-campaign-v21-paper.csv | Stylized current U.S.-like supreme court | 0.603 | 0.672 | 0.641 | 0.203 | 0.375 | 0.216 | 0.000 |
| simulation-campaign-v21-paper.csv | Supreme court with cross-checking constitutional court | 0.594 | 0.674 | 0.627 | 0.056 | 0.385 | 0.185 | 0.000 |
| simulation-campaign-v21-paper.csv | Dual supreme courts with disagreement filter | 0.586 | 0.654 | 0.646 | 0.059 | 0.393 | 0.194 | 0.000 |
| simulation-campaign-v5.csv | No emergency relief without merits review | 0.603 | 0.643 | 0.640 | 0.011 | 0.386 | 0.196 | 0.000 |
| simulation-campaign-v5.csv | 18-year staggered terms + regular appointments | 0.598 | 0.641 | 0.640 | 0.075 | 0.402 | 0.216 | 0.000 |
| simulation-campaign-v5.csv | Jurisdiction stripping constrained by rights carveouts | 0.598 | 0.642 | 0.636 | 0.073 | 0.408 | 0.208 | 0.112 |
| simulation-campaign-v5.csv | Public-interest litigation filter | 0.598 | 0.650 | 0.640 | 0.073 | 0.394 | 0.199 | 0.000 |
| simulation-campaign-v5.csv | 60 percent invalidation threshold | 0.598 | 0.649 | 0.628 | 0.069 | 0.399 | 0.215 | 0.000 |
| simulation-campaign-v5.csv | Emergency integrity package | 0.597 | 0.642 | 0.643 | 0.018 | 0.394 | 0.197 | 0.000 |
| simulation-campaign-v5.csv | Peer recusal + reasoned emergency docket | 0.597 | 0.646 | 0.634 | 0.074 | 0.393 | 0.209 | 0.000 |
| simulation-campaign-v5.csv | Constitutional remand before invalidation | 0.596 | 0.672 | 0.634 | 0.083 | 0.399 | 0.200 | 0.072 |
| simulation-campaign-v5.csv | Automatic merits follow-up for emergency relief | 0.596 | 0.634 | 0.642 | 0.018 | 0.395 | 0.210 | 0.000 |
| simulation-campaign-v5.csv | Three-judge panels with en banc correction | 0.594 | 0.645 | 0.641 | 0.080 | 0.405 | 0.206 | 0.000 |
| simulation-campaign-v5.csv | Independent recusal enforcement with substitutes | 0.594 | 0.646 | 0.634 | 0.078 | 0.398 | 0.208 | 0.000 |
| simulation-campaign-v5.csv | Constitutional remand with override window | 0.594 | 0.673 | 0.630 | 0.048 | 0.395 | 0.200 | 0.076 |
| simulation-campaign-v5.csv | Nonpartisan commission appointments | 0.593 | 0.636 | 0.637 | 0.075 | 0.405 | 0.211 | 0.000 |
| simulation-campaign-v5.csv | Randomized merits panels with en banc correction | 0.593 | 0.641 | 0.635 | 0.074 | 0.394 | 0.204 | 0.000 |
| simulation-campaign-v5.csv | Retention-election accountability court | 0.592 | 0.642 | 0.628 | 0.076 | 0.414 | 0.208 | 0.107 |
| simulation-campaign-v5.csv | Mandatory written emergency reasoning | 0.592 | 0.638 | 0.640 | 0.051 | 0.407 | 0.218 | 0.000 |
| simulation-campaign-v5.csv | Judicial review with legislative supermajority override | 0.592 | 0.635 | 0.644 | 0.080 | 0.418 | 0.217 | 0.111 |
| simulation-campaign-v5.csv | Time-limited legislative override window | 0.592 | 0.639 | 0.633 | 0.077 | 0.414 | 0.215 | 0.111 |
| simulation-campaign-v5.csv | Expanded 15-seat court | 0.591 | 0.640 | 0.634 | 0.076 | 0.395 | 0.215 | 0.000 |
| simulation-campaign-v5.csv | Random panels with jurisdiction safeguards | 0.590 | 0.647 | 0.630 | 0.071 | 0.411 | 0.205 | 0.096 |
| simulation-campaign-v5.csv | Comparative 16-seat constitutional senates | 0.590 | 0.653 | 0.631 | 0.067 | 0.396 | 0.209 | 0.000 |
| simulation-campaign-v5.csv | Pre-enactment constitutional council | 0.590 | 0.648 | 0.640 | 0.078 | 0.410 | 0.213 | 0.111 |
| simulation-campaign-v5.csv | Constitutional council with concrete-review backstop | 0.588 | 0.653 | 0.639 | 0.075 | 0.410 | 0.210 | 0.099 |
| simulation-campaign-v5.csv | Stylized current U.S.-like supreme court | 0.587 | 0.640 | 0.639 | 0.231 | 0.419 | 0.240 | 0.000 |
| simulation-campaign-v5.csv | Supreme court with cross-checking constitutional court | 0.579 | 0.647 | 0.614 | 0.069 | 0.423 | 0.206 | 0.000 |
| simulation-campaign-v5.csv | Dual supreme courts with disagreement filter | 0.567 | 0.616 | 0.633 | 0.067 | 0.429 | 0.215 | 0.000 |
| simulation-manipulation-stress.csv | No emergency relief without merits review | 0.618 | 0.672 | 0.647 | 0.007 | 0.358 | 0.177 | 0.000 |
| simulation-manipulation-stress.csv | 18-year staggered terms + regular appointments | 0.618 | 0.676 | 0.644 | 0.062 | 0.360 | 0.191 | 0.000 |
| simulation-manipulation-stress.csv | 60 percent invalidation threshold | 0.616 | 0.676 | 0.639 | 0.057 | 0.361 | 0.195 | 0.000 |
| simulation-manipulation-stress.csv | Jurisdiction stripping constrained by rights carveouts | 0.615 | 0.672 | 0.643 | 0.065 | 0.373 | 0.189 | 0.083 |
| simulation-manipulation-stress.csv | Emergency integrity package | 0.615 | 0.679 | 0.648 | 0.013 | 0.360 | 0.181 | 0.000 |
| simulation-manipulation-stress.csv | Three-judge panels with en banc correction | 0.614 | 0.680 | 0.640 | 0.066 | 0.364 | 0.184 | 0.000 |
| simulation-manipulation-stress.csv | Public-interest litigation filter | 0.613 | 0.678 | 0.643 | 0.065 | 0.359 | 0.179 | 0.000 |
| simulation-manipulation-stress.csv | Retention-election accountability court | 0.613 | 0.675 | 0.639 | 0.066 | 0.368 | 0.186 | 0.069 |
| simulation-manipulation-stress.csv | Automatic merits follow-up for emergency relief | 0.613 | 0.672 | 0.640 | 0.013 | 0.357 | 0.193 | 0.000 |
| simulation-manipulation-stress.csv | Mandatory written emergency reasoning | 0.613 | 0.677 | 0.639 | 0.040 | 0.361 | 0.193 | 0.000 |
| simulation-manipulation-stress.csv | Constitutional remand before invalidation | 0.613 | 0.696 | 0.638 | 0.063 | 0.359 | 0.178 | 0.055 |
| simulation-manipulation-stress.csv | Randomized merits panels with en banc correction | 0.612 | 0.679 | 0.639 | 0.060 | 0.359 | 0.184 | 0.000 |
| simulation-manipulation-stress.csv | Nonpartisan commission appointments | 0.612 | 0.674 | 0.643 | 0.068 | 0.364 | 0.188 | 0.000 |
| simulation-manipulation-stress.csv | Expanded 15-seat court | 0.611 | 0.678 | 0.639 | 0.063 | 0.361 | 0.195 | 0.000 |
| simulation-manipulation-stress.csv | Time-limited legislative override window | 0.611 | 0.671 | 0.642 | 0.062 | 0.375 | 0.197 | 0.092 |
| simulation-manipulation-stress.csv | Judicial review with legislative supermajority override | 0.611 | 0.673 | 0.645 | 0.067 | 0.376 | 0.195 | 0.077 |
| simulation-manipulation-stress.csv | Peer recusal + reasoned emergency docket | 0.611 | 0.673 | 0.639 | 0.065 | 0.362 | 0.194 | 0.000 |
| simulation-manipulation-stress.csv | Constitutional remand with override window | 0.610 | 0.696 | 0.641 | 0.038 | 0.362 | 0.179 | 0.058 |
| simulation-manipulation-stress.csv | Random panels with jurisdiction safeguards | 0.610 | 0.679 | 0.634 | 0.056 | 0.370 | 0.181 | 0.076 |
| simulation-manipulation-stress.csv | Independent recusal enforcement with substitutes | 0.609 | 0.671 | 0.641 | 0.065 | 0.364 | 0.191 | 0.000 |
| simulation-manipulation-stress.csv | Pre-enactment constitutional council | 0.608 | 0.684 | 0.639 | 0.064 | 0.373 | 0.191 | 0.072 |
| simulation-manipulation-stress.csv | Constitutional council with concrete-review backstop | 0.608 | 0.687 | 0.639 | 0.063 | 0.364 | 0.187 | 0.063 |
| simulation-manipulation-stress.csv | Comparative 16-seat constitutional senates | 0.606 | 0.681 | 0.636 | 0.052 | 0.362 | 0.186 | 0.000 |
| simulation-manipulation-stress.csv | Stylized current U.S.-like supreme court | 0.604 | 0.670 | 0.640 | 0.201 | 0.378 | 0.216 | 0.000 |
| simulation-manipulation-stress.csv | Supreme court with cross-checking constitutional court | 0.597 | 0.672 | 0.627 | 0.054 | 0.383 | 0.185 | 0.000 |
| simulation-manipulation-stress.csv | Dual supreme courts with disagreement filter | 0.590 | 0.659 | 0.641 | 0.058 | 0.387 | 0.191 | 0.000 |
