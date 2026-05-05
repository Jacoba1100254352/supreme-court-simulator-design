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
| simulation-campaign-v0.csv | 0.281 | 0.593 | 0.167 | 0.200 | 0.280 | 0.144 | 0.597 | 0.228 | No emergency relief without merits review (0.610) |
| simulation-campaign-v5.csv | 0.429 | 0.554 | 0.239 | 0.200 | 0.280 | 0.262 | 0.562 | 0.285 | No emergency relief without merits review (0.604) |
| simulation-campaign-v10.csv | 0.518 | 0.582 | 0.268 | 0.200 | 0.227 | 0.326 | 0.565 | 0.307 | No emergency relief without merits review (0.604) |
| simulation-campaign-v15.csv | 0.500 | 0.594 | 0.255 | 0.110 | 0.230 | 0.323 | 0.513 | 0.293 | 18-year staggered terms + regular appointments (0.605) |
| simulation-campaign-v20.csv | 0.584 | 0.564 | 0.251 | 0.116 | 0.246 | 0.334 | 0.494 | 0.302 | No emergency relief without merits review (0.604) |
| simulation-campaign-v21-paper.csv | 0.343 | 0.610 | 0.175 | 0.104 | 0.237 | 0.120 | 0.547 | 0.213 | Jurisdiction stripping constrained by rights carveouts (0.612) |
| simulation-manipulation-stress.csv | 0.283 | 0.582 | 0.102 | 0.163 | 0.274 | 0.097 | 0.552 | 0.202 | Jurisdiction stripping constrained by rights carveouts (0.614) |

## Scenario Sensitivity By Family

| Family | Scenario | Directional | Legal | Rights | Shadow | Conflict | Strategic | Override att. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| simulation-campaign-v0.csv | No emergency relief without merits review | 0.610 | 0.689 | 0.641 | 0.001 | 0.362 | 0.150 | 0.000 |
| simulation-campaign-v0.csv | 18-year staggered terms + regular appointments | 0.609 | 0.679 | 0.648 | 0.052 | 0.363 | 0.170 | 0.000 |
| simulation-campaign-v0.csv | 60 percent invalidation threshold | 0.609 | 0.687 | 0.632 | 0.046 | 0.363 | 0.170 | 0.000 |
| simulation-campaign-v0.csv | Nonpartisan commission appointments | 0.608 | 0.683 | 0.650 | 0.056 | 0.369 | 0.158 | 0.000 |
| simulation-campaign-v0.csv | Jurisdiction stripping constrained by rights carveouts | 0.607 | 0.679 | 0.648 | 0.056 | 0.372 | 0.155 | 0.056 |
| simulation-campaign-v0.csv | Automatic merits follow-up for emergency relief | 0.607 | 0.684 | 0.645 | 0.003 | 0.359 | 0.160 | 0.000 |
| simulation-campaign-v0.csv | Mandatory written emergency reasoning | 0.605 | 0.685 | 0.641 | 0.024 | 0.360 | 0.167 | 0.000 |
| simulation-campaign-v0.csv | Peer recusal + reasoned emergency docket | 0.605 | 0.686 | 0.640 | 0.056 | 0.359 | 0.167 | 0.000 |
| simulation-campaign-v0.csv | Time-limited legislative override window | 0.605 | 0.681 | 0.647 | 0.054 | 0.375 | 0.159 | 0.048 |
| simulation-campaign-v0.csv | Judicial review with legislative supermajority override | 0.605 | 0.685 | 0.646 | 0.059 | 0.378 | 0.160 | 0.051 |
| simulation-campaign-v0.csv | Retention-election accountability court | 0.604 | 0.685 | 0.637 | 0.057 | 0.373 | 0.159 | 0.045 |
| simulation-campaign-v0.csv | Expanded 15-seat court | 0.603 | 0.683 | 0.643 | 0.053 | 0.361 | 0.167 | 0.000 |
| simulation-campaign-v0.csv | Independent recusal enforcement with substitutes | 0.603 | 0.685 | 0.643 | 0.054 | 0.365 | 0.158 | 0.000 |
| simulation-campaign-v0.csv | Three-judge panels with en banc correction | 0.603 | 0.685 | 0.639 | 0.057 | 0.367 | 0.158 | 0.000 |
| simulation-campaign-v0.csv | Randomized merits panels with en banc correction | 0.603 | 0.684 | 0.647 | 0.059 | 0.369 | 0.161 | 0.000 |
| simulation-campaign-v0.csv | Public-interest litigation filter | 0.602 | 0.680 | 0.655 | 0.057 | 0.374 | 0.163 | 0.000 |
| simulation-campaign-v0.csv | Constitutional remand before invalidation | 0.600 | 0.695 | 0.641 | 0.058 | 0.367 | 0.158 | 0.033 |
| simulation-campaign-v0.csv | Stylized current U.S.-like supreme court | 0.596 | 0.678 | 0.639 | 0.214 | 0.377 | 0.181 | 0.000 |
| simulation-campaign-v0.csv | Comparative 16-seat constitutional senates | 0.596 | 0.689 | 0.623 | 0.047 | 0.360 | 0.153 | 0.000 |
| simulation-campaign-v0.csv | Pre-enactment constitutional council | 0.596 | 0.687 | 0.638 | 0.055 | 0.373 | 0.164 | 0.045 |
| simulation-campaign-v0.csv | Supreme court with cross-checking constitutional court | 0.582 | 0.672 | 0.630 | 0.046 | 0.401 | 0.162 | 0.000 |
| simulation-campaign-v0.csv | Dual supreme courts with disagreement filter | 0.581 | 0.663 | 0.650 | 0.044 | 0.400 | 0.168 | 0.000 |
| simulation-campaign-v10.csv | No emergency relief without merits review | 0.604 | 0.682 | 0.654 | 0.001 | 0.380 | 0.157 | 0.000 |
| simulation-campaign-v10.csv | 18-year staggered terms + regular appointments | 0.601 | 0.673 | 0.664 | 0.068 | 0.388 | 0.182 | 0.000 |
| simulation-campaign-v10.csv | Jurisdiction stripping constrained by rights carveouts | 0.600 | 0.670 | 0.661 | 0.065 | 0.392 | 0.167 | 0.053 |
| simulation-campaign-v10.csv | Automatic merits follow-up for emergency relief | 0.600 | 0.677 | 0.658 | 0.004 | 0.377 | 0.168 | 0.000 |
| simulation-campaign-v10.csv | 60 percent invalidation threshold | 0.600 | 0.677 | 0.645 | 0.056 | 0.385 | 0.180 | 0.000 |
| simulation-campaign-v10.csv | Time-limited legislative override window | 0.599 | 0.675 | 0.660 | 0.064 | 0.395 | 0.172 | 0.048 |
| simulation-campaign-v10.csv | Mandatory written emergency reasoning | 0.598 | 0.675 | 0.650 | 0.028 | 0.377 | 0.173 | 0.000 |
| simulation-campaign-v10.csv | Nonpartisan commission appointments | 0.598 | 0.674 | 0.660 | 0.067 | 0.390 | 0.169 | 0.000 |
| simulation-campaign-v10.csv | Peer recusal + reasoned emergency docket | 0.597 | 0.674 | 0.652 | 0.062 | 0.376 | 0.178 | 0.000 |
| simulation-campaign-v10.csv | Judicial review with legislative supermajority override | 0.597 | 0.673 | 0.657 | 0.066 | 0.391 | 0.168 | 0.049 |
| simulation-campaign-v10.csv | Retention-election accountability court | 0.597 | 0.679 | 0.642 | 0.067 | 0.384 | 0.164 | 0.041 |
| simulation-campaign-v10.csv | Independent recusal enforcement with substitutes | 0.596 | 0.672 | 0.665 | 0.066 | 0.390 | 0.168 | 0.000 |
| simulation-campaign-v10.csv | Three-judge panels with en banc correction | 0.595 | 0.670 | 0.664 | 0.066 | 0.391 | 0.176 | 0.000 |
| simulation-campaign-v10.csv | Expanded 15-seat court | 0.595 | 0.675 | 0.654 | 0.064 | 0.379 | 0.177 | 0.000 |
| simulation-campaign-v10.csv | Public-interest litigation filter | 0.594 | 0.675 | 0.663 | 0.071 | 0.398 | 0.168 | 0.000 |
| simulation-campaign-v10.csv | Randomized merits panels with en banc correction | 0.594 | 0.679 | 0.653 | 0.067 | 0.386 | 0.166 | 0.000 |
| simulation-campaign-v10.csv | Constitutional remand before invalidation | 0.590 | 0.686 | 0.654 | 0.067 | 0.392 | 0.167 | 0.039 |
| simulation-campaign-v10.csv | Comparative 16-seat constitutional senates | 0.589 | 0.679 | 0.640 | 0.053 | 0.380 | 0.164 | 0.000 |
| simulation-campaign-v10.csv | Pre-enactment constitutional council | 0.587 | 0.676 | 0.651 | 0.067 | 0.390 | 0.173 | 0.044 |
| simulation-campaign-v10.csv | Stylized current U.S.-like supreme court | 0.584 | 0.663 | 0.653 | 0.247 | 0.400 | 0.195 | 0.000 |
| simulation-campaign-v10.csv | Supreme court with cross-checking constitutional court | 0.571 | 0.661 | 0.643 | 0.057 | 0.425 | 0.178 | 0.000 |
| simulation-campaign-v10.csv | Dual supreme courts with disagreement filter | 0.569 | 0.654 | 0.658 | 0.057 | 0.423 | 0.175 | 0.000 |
| simulation-campaign-v15.csv | 18-year staggered terms + regular appointments | 0.605 | 0.681 | 0.654 | 0.062 | 0.367 | 0.172 | 0.000 |
| simulation-campaign-v15.csv | No emergency relief without merits review | 0.602 | 0.686 | 0.651 | 0.001 | 0.372 | 0.158 | 0.000 |
| simulation-campaign-v15.csv | 60 percent invalidation threshold | 0.602 | 0.680 | 0.645 | 0.055 | 0.368 | 0.175 | 0.000 |
| simulation-campaign-v15.csv | Jurisdiction stripping constrained by rights carveouts | 0.601 | 0.680 | 0.655 | 0.067 | 0.378 | 0.160 | 0.041 |
| simulation-campaign-v15.csv | Nonpartisan commission appointments | 0.601 | 0.681 | 0.656 | 0.065 | 0.374 | 0.158 | 0.000 |
| simulation-campaign-v15.csv | Automatic merits follow-up for emergency relief | 0.601 | 0.681 | 0.664 | 0.005 | 0.379 | 0.168 | 0.000 |
| simulation-campaign-v15.csv | Retention-election accountability court | 0.600 | 0.683 | 0.648 | 0.062 | 0.375 | 0.156 | 0.034 |
| simulation-campaign-v15.csv | Mandatory written emergency reasoning | 0.599 | 0.682 | 0.653 | 0.030 | 0.373 | 0.174 | 0.000 |
| simulation-campaign-v15.csv | Peer recusal + reasoned emergency docket | 0.598 | 0.680 | 0.654 | 0.065 | 0.370 | 0.171 | 0.000 |
| simulation-campaign-v15.csv | Judicial review with legislative supermajority override | 0.598 | 0.677 | 0.662 | 0.068 | 0.386 | 0.169 | 0.046 |
| simulation-campaign-v15.csv | Time-limited legislative override window | 0.598 | 0.678 | 0.653 | 0.066 | 0.379 | 0.165 | 0.044 |
| simulation-campaign-v15.csv | Three-judge panels with en banc correction | 0.598 | 0.682 | 0.655 | 0.070 | 0.379 | 0.162 | 0.000 |
| simulation-campaign-v15.csv | Expanded 15-seat court | 0.597 | 0.684 | 0.651 | 0.063 | 0.366 | 0.167 | 0.000 |
| simulation-campaign-v15.csv | Randomized merits panels with en banc correction | 0.596 | 0.683 | 0.652 | 0.064 | 0.373 | 0.161 | 0.000 |
| simulation-campaign-v15.csv | Independent recusal enforcement with substitutes | 0.596 | 0.679 | 0.654 | 0.064 | 0.374 | 0.166 | 0.000 |
| simulation-campaign-v15.csv | Public-interest litigation filter | 0.595 | 0.679 | 0.663 | 0.066 | 0.385 | 0.168 | 0.000 |
| simulation-campaign-v15.csv | Pre-enactment constitutional council | 0.591 | 0.686 | 0.648 | 0.066 | 0.377 | 0.160 | 0.034 |
| simulation-campaign-v15.csv | Stylized current U.S.-like supreme court | 0.590 | 0.673 | 0.650 | 0.228 | 0.381 | 0.186 | 0.000 |
| simulation-campaign-v15.csv | Constitutional remand before invalidation | 0.590 | 0.689 | 0.655 | 0.072 | 0.386 | 0.167 | 0.032 |
| simulation-campaign-v15.csv | Comparative 16-seat constitutional senates | 0.590 | 0.682 | 0.640 | 0.054 | 0.367 | 0.159 | 0.000 |
| simulation-campaign-v15.csv | Supreme court with cross-checking constitutional court | 0.576 | 0.668 | 0.642 | 0.057 | 0.413 | 0.173 | 0.000 |
| simulation-campaign-v15.csv | Dual supreme courts with disagreement filter | 0.570 | 0.658 | 0.657 | 0.059 | 0.412 | 0.176 | 0.000 |
| simulation-campaign-v20.csv | No emergency relief without merits review | 0.604 | 0.682 | 0.655 | 0.002 | 0.377 | 0.159 | 0.000 |
| simulation-campaign-v20.csv | 18-year staggered terms + regular appointments | 0.603 | 0.676 | 0.652 | 0.064 | 0.375 | 0.170 | 0.000 |
| simulation-campaign-v20.csv | 60 percent invalidation threshold | 0.600 | 0.675 | 0.647 | 0.054 | 0.381 | 0.177 | 0.000 |
| simulation-campaign-v20.csv | Automatic merits follow-up for emergency relief | 0.600 | 0.677 | 0.651 | 0.005 | 0.369 | 0.166 | 0.000 |
| simulation-campaign-v20.csv | Jurisdiction stripping constrained by rights carveouts | 0.598 | 0.671 | 0.659 | 0.068 | 0.393 | 0.167 | 0.057 |
| simulation-campaign-v20.csv | Nonpartisan commission appointments | 0.598 | 0.676 | 0.661 | 0.070 | 0.391 | 0.168 | 0.000 |
| simulation-campaign-v20.csv | Judicial review with legislative supermajority override | 0.597 | 0.669 | 0.658 | 0.066 | 0.392 | 0.167 | 0.058 |
| simulation-campaign-v20.csv | Mandatory written emergency reasoning | 0.597 | 0.673 | 0.654 | 0.032 | 0.381 | 0.180 | 0.000 |
| simulation-campaign-v20.csv | Three-judge panels with en banc correction | 0.597 | 0.677 | 0.656 | 0.064 | 0.386 | 0.164 | 0.000 |
| simulation-campaign-v20.csv | Retention-election accountability court | 0.596 | 0.676 | 0.646 | 0.066 | 0.384 | 0.164 | 0.038 |
| simulation-campaign-v20.csv | Peer recusal + reasoned emergency docket | 0.596 | 0.673 | 0.655 | 0.067 | 0.380 | 0.178 | 0.000 |
| simulation-campaign-v20.csv | Time-limited legislative override window | 0.596 | 0.666 | 0.660 | 0.065 | 0.391 | 0.173 | 0.060 |
| simulation-campaign-v20.csv | Public-interest litigation filter | 0.595 | 0.669 | 0.669 | 0.069 | 0.395 | 0.171 | 0.000 |
| simulation-campaign-v20.csv | Randomized merits panels with en banc correction | 0.594 | 0.673 | 0.658 | 0.065 | 0.388 | 0.166 | 0.000 |
| simulation-campaign-v20.csv | Independent recusal enforcement with substitutes | 0.594 | 0.671 | 0.661 | 0.068 | 0.389 | 0.169 | 0.000 |
| simulation-campaign-v20.csv | Expanded 15-seat court | 0.593 | 0.672 | 0.654 | 0.064 | 0.378 | 0.176 | 0.000 |
| simulation-campaign-v20.csv | Pre-enactment constitutional council | 0.591 | 0.679 | 0.652 | 0.066 | 0.388 | 0.164 | 0.042 |
| simulation-campaign-v20.csv | Constitutional remand before invalidation | 0.590 | 0.685 | 0.657 | 0.067 | 0.394 | 0.169 | 0.038 |
| simulation-campaign-v20.csv | Comparative 16-seat constitutional senates | 0.589 | 0.676 | 0.640 | 0.054 | 0.374 | 0.167 | 0.000 |
| simulation-campaign-v20.csv | Stylized current U.S.-like supreme court | 0.583 | 0.660 | 0.657 | 0.244 | 0.404 | 0.197 | 0.000 |
| simulation-campaign-v20.csv | Supreme court with cross-checking constitutional court | 0.574 | 0.661 | 0.642 | 0.055 | 0.417 | 0.168 | 0.000 |
| simulation-campaign-v20.csv | Dual supreme courts with disagreement filter | 0.568 | 0.653 | 0.655 | 0.057 | 0.421 | 0.180 | 0.000 |
| simulation-campaign-v21-paper.csv | Jurisdiction stripping constrained by rights carveouts | 0.612 | 0.691 | 0.654 | 0.049 | 0.349 | 0.144 | 0.033 |
| simulation-campaign-v21-paper.csv | 18-year staggered terms + regular appointments | 0.612 | 0.692 | 0.650 | 0.055 | 0.343 | 0.158 | 0.000 |
| simulation-campaign-v21-paper.csv | No emergency relief without merits review | 0.612 | 0.697 | 0.651 | 0.001 | 0.343 | 0.143 | 0.000 |
| simulation-campaign-v21-paper.csv | 60 percent invalidation threshold | 0.610 | 0.691 | 0.644 | 0.044 | 0.344 | 0.162 | 0.000 |
| simulation-campaign-v21-paper.csv | Peer recusal + reasoned emergency docket | 0.609 | 0.692 | 0.654 | 0.052 | 0.341 | 0.158 | 0.000 |
| simulation-campaign-v21-paper.csv | Judicial review with legislative supermajority override | 0.609 | 0.689 | 0.657 | 0.050 | 0.353 | 0.150 | 0.039 |
| simulation-campaign-v21-paper.csv | Time-limited legislative override window | 0.608 | 0.690 | 0.655 | 0.053 | 0.353 | 0.152 | 0.033 |
| simulation-campaign-v21-paper.csv | Nonpartisan commission appointments | 0.607 | 0.690 | 0.657 | 0.056 | 0.352 | 0.155 | 0.000 |
| simulation-campaign-v21-paper.csv | Automatic merits follow-up for emergency relief | 0.607 | 0.693 | 0.652 | 0.002 | 0.346 | 0.155 | 0.000 |
| simulation-campaign-v21-paper.csv | Expanded 15-seat court | 0.607 | 0.693 | 0.651 | 0.052 | 0.338 | 0.153 | 0.000 |
| simulation-campaign-v21-paper.csv | Three-judge panels with en banc correction | 0.607 | 0.693 | 0.653 | 0.055 | 0.351 | 0.151 | 0.000 |
| simulation-campaign-v21-paper.csv | Mandatory written emergency reasoning | 0.606 | 0.693 | 0.648 | 0.025 | 0.344 | 0.159 | 0.000 |
| simulation-campaign-v21-paper.csv | Retention-election accountability court | 0.606 | 0.693 | 0.647 | 0.054 | 0.352 | 0.149 | 0.035 |
| simulation-campaign-v21-paper.csv | Independent recusal enforcement with substitutes | 0.605 | 0.692 | 0.654 | 0.056 | 0.349 | 0.151 | 0.000 |
| simulation-campaign-v21-paper.csv | Randomized merits panels with en banc correction | 0.604 | 0.695 | 0.650 | 0.055 | 0.349 | 0.148 | 0.000 |
| simulation-campaign-v21-paper.csv | Public-interest litigation filter | 0.603 | 0.691 | 0.657 | 0.059 | 0.356 | 0.155 | 0.000 |
| simulation-campaign-v21-paper.csv | Pre-enactment constitutional council | 0.603 | 0.696 | 0.653 | 0.049 | 0.353 | 0.148 | 0.028 |
| simulation-campaign-v21-paper.csv | Constitutional remand before invalidation | 0.601 | 0.703 | 0.655 | 0.054 | 0.356 | 0.150 | 0.023 |
| simulation-campaign-v21-paper.csv | Comparative 16-seat constitutional senates | 0.598 | 0.695 | 0.637 | 0.043 | 0.344 | 0.147 | 0.000 |
| simulation-campaign-v21-paper.csv | Stylized current U.S.-like supreme court | 0.597 | 0.682 | 0.650 | 0.201 | 0.360 | 0.178 | 0.000 |
| simulation-campaign-v21-paper.csv | Supreme court with cross-checking constitutional court | 0.589 | 0.682 | 0.644 | 0.041 | 0.379 | 0.150 | 0.000 |
| simulation-campaign-v21-paper.csv | Dual supreme courts with disagreement filter | 0.581 | 0.673 | 0.659 | 0.043 | 0.385 | 0.164 | 0.000 |
| simulation-campaign-v5.csv | No emergency relief without merits review | 0.604 | 0.678 | 0.651 | 0.001 | 0.377 | 0.155 | 0.000 |
| simulation-campaign-v5.csv | 18-year staggered terms + regular appointments | 0.604 | 0.674 | 0.648 | 0.060 | 0.375 | 0.176 | 0.000 |
| simulation-campaign-v5.csv | 60 percent invalidation threshold | 0.603 | 0.675 | 0.640 | 0.047 | 0.373 | 0.174 | 0.000 |
| simulation-campaign-v5.csv | Jurisdiction stripping constrained by rights carveouts | 0.603 | 0.672 | 0.653 | 0.059 | 0.386 | 0.163 | 0.058 |
| simulation-campaign-v5.csv | Nonpartisan commission appointments | 0.602 | 0.673 | 0.659 | 0.064 | 0.383 | 0.165 | 0.000 |
| simulation-campaign-v5.csv | Peer recusal + reasoned emergency docket | 0.599 | 0.675 | 0.648 | 0.060 | 0.373 | 0.173 | 0.000 |
| simulation-campaign-v5.csv | Retention-election accountability court | 0.599 | 0.676 | 0.645 | 0.062 | 0.386 | 0.162 | 0.046 |
| simulation-campaign-v5.csv | Time-limited legislative override window | 0.599 | 0.668 | 0.654 | 0.062 | 0.386 | 0.168 | 0.056 |
| simulation-campaign-v5.csv | Automatic merits follow-up for emergency relief | 0.599 | 0.673 | 0.655 | 0.004 | 0.378 | 0.172 | 0.000 |
| simulation-campaign-v5.csv | Mandatory written emergency reasoning | 0.599 | 0.675 | 0.646 | 0.028 | 0.372 | 0.173 | 0.000 |
| simulation-campaign-v5.csv | Judicial review with legislative supermajority override | 0.598 | 0.670 | 0.652 | 0.059 | 0.385 | 0.167 | 0.048 |
| simulation-campaign-v5.csv | Three-judge panels with en banc correction | 0.598 | 0.674 | 0.649 | 0.058 | 0.378 | 0.165 | 0.000 |
| simulation-campaign-v5.csv | Randomized merits panels with en banc correction | 0.598 | 0.670 | 0.656 | 0.059 | 0.379 | 0.162 | 0.000 |
| simulation-campaign-v5.csv | Independent recusal enforcement with substitutes | 0.597 | 0.676 | 0.649 | 0.064 | 0.381 | 0.164 | 0.000 |
| simulation-campaign-v5.csv | Public-interest litigation filter | 0.596 | 0.671 | 0.658 | 0.068 | 0.387 | 0.167 | 0.000 |
| simulation-campaign-v5.csv | Expanded 15-seat court | 0.594 | 0.672 | 0.646 | 0.062 | 0.374 | 0.175 | 0.000 |
| simulation-campaign-v5.csv | Pre-enactment constitutional council | 0.594 | 0.677 | 0.644 | 0.059 | 0.376 | 0.162 | 0.046 |
| simulation-campaign-v5.csv | Constitutional remand before invalidation | 0.590 | 0.682 | 0.649 | 0.063 | 0.386 | 0.170 | 0.043 |
| simulation-campaign-v5.csv | Stylized current U.S.-like supreme court | 0.588 | 0.664 | 0.647 | 0.225 | 0.391 | 0.187 | 0.000 |
| simulation-campaign-v5.csv | Comparative 16-seat constitutional senates | 0.588 | 0.675 | 0.637 | 0.055 | 0.376 | 0.164 | 0.000 |
| simulation-campaign-v5.csv | Supreme court with cross-checking constitutional court | 0.575 | 0.659 | 0.634 | 0.052 | 0.412 | 0.167 | 0.000 |
| simulation-campaign-v5.csv | Dual supreme courts with disagreement filter | 0.573 | 0.655 | 0.652 | 0.051 | 0.413 | 0.172 | 0.000 |
| simulation-manipulation-stress.csv | Jurisdiction stripping constrained by rights carveouts | 0.614 | 0.693 | 0.645 | 0.048 | 0.353 | 0.143 | 0.044 |
| simulation-manipulation-stress.csv | 18-year staggered terms + regular appointments | 0.612 | 0.692 | 0.638 | 0.050 | 0.345 | 0.160 | 0.000 |
| simulation-manipulation-stress.csv | No emergency relief without merits review | 0.611 | 0.698 | 0.638 | 0.001 | 0.346 | 0.141 | 0.000 |
| simulation-manipulation-stress.csv | 60 percent invalidation threshold | 0.611 | 0.692 | 0.635 | 0.042 | 0.352 | 0.164 | 0.000 |
| simulation-manipulation-stress.csv | Nonpartisan commission appointments | 0.611 | 0.690 | 0.644 | 0.049 | 0.351 | 0.147 | 0.000 |
| simulation-manipulation-stress.csv | Retention-election accountability court | 0.610 | 0.693 | 0.641 | 0.049 | 0.356 | 0.149 | 0.039 |
| simulation-manipulation-stress.csv | Peer recusal + reasoned emergency docket | 0.609 | 0.691 | 0.640 | 0.045 | 0.339 | 0.160 | 0.000 |
| simulation-manipulation-stress.csv | Automatic merits follow-up for emergency relief | 0.609 | 0.694 | 0.646 | 0.002 | 0.347 | 0.155 | 0.000 |
| simulation-manipulation-stress.csv | Mandatory written emergency reasoning | 0.609 | 0.694 | 0.639 | 0.022 | 0.348 | 0.157 | 0.000 |
| simulation-manipulation-stress.csv | Time-limited legislative override window | 0.609 | 0.691 | 0.646 | 0.050 | 0.360 | 0.152 | 0.040 |
| simulation-manipulation-stress.csv | Three-judge panels with en banc correction | 0.608 | 0.690 | 0.650 | 0.051 | 0.355 | 0.152 | 0.000 |
| simulation-manipulation-stress.csv | Judicial review with legislative supermajority override | 0.608 | 0.689 | 0.647 | 0.053 | 0.356 | 0.151 | 0.045 |
| simulation-manipulation-stress.csv | Independent recusal enforcement with substitutes | 0.608 | 0.691 | 0.649 | 0.051 | 0.353 | 0.148 | 0.000 |
| simulation-manipulation-stress.csv | Randomized merits panels with en banc correction | 0.606 | 0.692 | 0.645 | 0.053 | 0.352 | 0.148 | 0.000 |
| simulation-manipulation-stress.csv | Expanded 15-seat court | 0.606 | 0.693 | 0.640 | 0.051 | 0.345 | 0.159 | 0.000 |
| simulation-manipulation-stress.csv | Public-interest litigation filter | 0.605 | 0.689 | 0.650 | 0.052 | 0.358 | 0.152 | 0.000 |
| simulation-manipulation-stress.csv | Pre-enactment constitutional council | 0.602 | 0.694 | 0.640 | 0.048 | 0.350 | 0.147 | 0.038 |
| simulation-manipulation-stress.csv | Stylized current U.S.-like supreme court | 0.602 | 0.684 | 0.642 | 0.192 | 0.356 | 0.170 | 0.000 |
| simulation-manipulation-stress.csv | Constitutional remand before invalidation | 0.601 | 0.701 | 0.644 | 0.054 | 0.359 | 0.148 | 0.028 |
| simulation-manipulation-stress.csv | Comparative 16-seat constitutional senates | 0.601 | 0.695 | 0.631 | 0.039 | 0.347 | 0.148 | 0.000 |
| simulation-manipulation-stress.csv | Supreme court with cross-checking constitutional court | 0.587 | 0.680 | 0.631 | 0.039 | 0.382 | 0.158 | 0.000 |
| simulation-manipulation-stress.csv | Dual supreme courts with disagreement filter | 0.582 | 0.669 | 0.650 | 0.045 | 0.386 | 0.161 | 0.000 |
