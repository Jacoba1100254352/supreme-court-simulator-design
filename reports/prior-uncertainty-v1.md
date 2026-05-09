# Sampled Prior Uncertainty v1

This diagnostic replaces a purely named-scenario sensitivity story with sampled prior distributions over polarization, appointment capture, public pressure, emergency share, justice-pool size, and legislative-output profile components. It is still synthetic uncertainty, not empirical validation.

## Run Configuration

- runs per prior draw: 24
- cases per run: 48
- prior draws: 32
- base seed: 20260501
- legislative input: simulation-campaign-v21-paper.csv

## Prior Draw Ranges

| Field | Min | Median | Max |
| --- | ---: | ---: | ---: |
| polarization | 0.353 | 0.520 | 0.773 |
| appointment capture | 0.209 | 0.514 | 0.764 |
| public pressure | 0.220 | 0.517 | 0.770 |
| emergency share | 0.060 | 0.268 | 0.722 |

## Scenario Uncertainty Bands

| Scenario | Score 5/50/95 | Rights 5/50/95 | Shadow 5/50/95 | Emerg. downstream 5/50/95 | Lower-court compliance 5/50/95 | Gov. noncomp. 5/50/95 | Conflict 5/50/95 | Interpretation |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| No emergency relief without merits review | 0.597/0.615/0.630 | 0.638/0.648/0.656 | 0.005/0.009/0.016 | 0.034/0.058/0.108 | 0.585/0.606/0.624 | 0.040/0.065/0.099 | 0.313/0.358/0.414 | front-line cluster |
| 18-year staggered terms + regular appointments | 0.589/0.611/0.628 | 0.630/0.640/0.652 | 0.051/0.072/0.109 | 0.043/0.071/0.127 | 0.575/0.597/0.616 | 0.037/0.072/0.098 | 0.317/0.361/0.418 | front-line cluster |
| Jurisdiction stripping constrained by rights carveouts | 0.591/0.611/0.627 | 0.622/0.642/0.650 | 0.050/0.073/0.110 | 0.045/0.071/0.127 | 0.577/0.601/0.621 | 0.047/0.073/0.107 | 0.322/0.374/0.421 | front-line cluster |
| Automatic merits follow-up for emergency relief | 0.591/0.610/0.625 | 0.634/0.647/0.656 | 0.009/0.015/0.025 | 0.041/0.066/0.126 | 0.583/0.604/0.622 | 0.044/0.064/0.109 | 0.314/0.366/0.419 | front-line cluster |
| 60 percent invalidation threshold | 0.591/0.610/0.629 | 0.622/0.634/0.644 | 0.045/0.066/0.096 | 0.052/0.080/0.139 | 0.574/0.594/0.616 | 0.040/0.073/0.104 | 0.317/0.364/0.419 | front-line cluster |
| Emergency integrity package | 0.592/0.609/0.623 | 0.637/0.647/0.659 | 0.009/0.015/0.025 | 0.040/0.068/0.126 | 0.586/0.606/0.623 | 0.042/0.063/0.098 | 0.316/0.366/0.414 | front-line cluster |
| Nonpartisan commission appointments | 0.587/0.608/0.624 | 0.627/0.643/0.650 | 0.054/0.076/0.111 | 0.046/0.071/0.127 | 0.573/0.597/0.619 | 0.048/0.068/0.112 | 0.320/0.368/0.423 | front-line cluster |
| Public-interest litigation filter | 0.588/0.608/0.625 | 0.632/0.645/0.652 | 0.051/0.072/0.107 | 0.044/0.072/0.127 | 0.578/0.596/0.618 | 0.036/0.069/0.099 | 0.312/0.365/0.417 | front-line cluster |
| Mandatory written emergency reasoning | 0.586/0.608/0.623 | 0.626/0.639/0.649 | 0.029/0.045/0.073 | 0.049/0.075/0.139 | 0.574/0.596/0.616 | 0.047/0.070/0.102 | 0.320/0.369/0.421 | front-line cluster |
| Retention-election accountability court | 0.588/0.607/0.622 | 0.626/0.639/0.647 | 0.053/0.075/0.109 | 0.045/0.071/0.126 | 0.575/0.597/0.617 | 0.046/0.070/0.101 | 0.323/0.377/0.423 | front-line cluster |
| Constitutional remand before invalidation | 0.584/0.607/0.623 | 0.626/0.640/0.647 | 0.050/0.074/0.112 | 0.043/0.071/0.129 | 0.587/0.609/0.628 | 0.042/0.066/0.107 | 0.317/0.368/0.416 | front-line cluster |
| Three-judge panels with en banc correction | 0.585/0.606/0.624 | 0.628/0.642/0.649 | 0.050/0.075/0.107 | 0.044/0.073/0.127 | 0.573/0.598/0.619 | 0.039/0.072/0.113 | 0.318/0.361/0.418 | front-line cluster |
| Randomized merits panels with en banc correction | 0.584/0.606/0.622 | 0.631/0.641/0.650 | 0.052/0.073/0.109 | 0.044/0.070/0.126 | 0.575/0.598/0.617 | 0.042/0.066/0.105 | 0.319/0.365/0.412 | front-line cluster |
| Independent recusal enforcement with substitutes | 0.583/0.606/0.624 | 0.633/0.641/0.652 | 0.053/0.074/0.111 | 0.045/0.071/0.131 | 0.574/0.598/0.619 | 0.044/0.069/0.105 | 0.318/0.365/0.422 | front-line cluster |
| Peer recusal + reasoned emergency docket | 0.584/0.606/0.623 | 0.626/0.640/0.649 | 0.051/0.071/0.108 | 0.043/0.070/0.126 | 0.571/0.597/0.619 | 0.045/0.070/0.111 | 0.316/0.368/0.419 | front-line cluster |
| Judicial review with legislative supermajority override | 0.585/0.605/0.622 | 0.629/0.642/0.648 | 0.051/0.072/0.111 | 0.045/0.070/0.128 | 0.573/0.594/0.616 | 0.046/0.079/0.108 | 0.325/0.378/0.429 | front-line cluster |
| Time-limited legislative override window | 0.585/0.605/0.623 | 0.630/0.643/0.649 | 0.053/0.075/0.110 | 0.045/0.071/0.127 | 0.572/0.595/0.617 | 0.047/0.073/0.118 | 0.328/0.381/0.430 | front-line cluster |
| Expanded 15-seat court | 0.584/0.604/0.621 | 0.630/0.642/0.650 | 0.051/0.073/0.110 | 0.042/0.070/0.127 | 0.575/0.597/0.616 | 0.042/0.068/0.102 | 0.317/0.365/0.419 | front-line cluster |
| Pre-enactment constitutional council | 0.583/0.604/0.620 | 0.628/0.642/0.650 | 0.051/0.073/0.108 | 0.043/0.072/0.129 | 0.580/0.604/0.624 | 0.048/0.068/0.106 | 0.324/0.373/0.424 | front-line cluster |
| Constitutional remand with override window | 0.580/0.604/0.621 | 0.624/0.636/0.646 | 0.029/0.047/0.074 | 0.049/0.078/0.140 | 0.585/0.611/0.628 | 0.040/0.073/0.113 | 0.311/0.360/0.416 | front-line cluster |
| Random panels with jurisdiction safeguards | 0.582/0.602/0.621 | 0.622/0.636/0.647 | 0.043/0.065/0.099 | 0.051/0.079/0.140 | 0.571/0.597/0.619 | 0.046/0.076/0.117 | 0.321/0.373/0.424 | front-line cluster |
| Comparative 16-seat constitutional senates | 0.578/0.602/0.619 | 0.623/0.636/0.644 | 0.042/0.066/0.098 | 0.051/0.081/0.141 | 0.572/0.598/0.618 | 0.043/0.066/0.111 | 0.317/0.364/0.422 | front-line cluster |
| Constitutional council with concrete-review backstop | 0.581/0.601/0.618 | 0.627/0.639/0.646 | 0.050/0.073/0.107 | 0.042/0.071/0.125 | 0.583/0.604/0.625 | 0.047/0.072/0.102 | 0.322/0.373/0.418 | front-line cluster |
| Stylized current U.S.-like supreme court | 0.568/0.594/0.616 | 0.627/0.645/0.658 | 0.167/0.234/0.324 | 0.079/0.122/0.196 | 0.543/0.576/0.602 | 0.051/0.095/0.150 | 0.337/0.401/0.462 | overlapping uncertainty band |
| Supreme court with cross-checking constitutional court | 0.569/0.592/0.610 | 0.606/0.628/0.640 | 0.045/0.065/0.097 | 0.052/0.080/0.140 | 0.573/0.600/0.620 | 0.044/0.082/0.109 | 0.337/0.392/0.448 | overlapping uncertainty band |
| Dual supreme courts with disagreement filter | 0.559/0.581/0.600 | 0.629/0.641/0.652 | 0.044/0.065/0.101 | 0.051/0.082/0.140 | 0.563/0.589/0.612 | 0.051/0.082/0.123 | 0.342/0.396/0.458 | overlapping uncertainty band |
