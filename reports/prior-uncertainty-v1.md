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
| No emergency relief without merits review | 0.596/0.615/0.630 | 0.638/0.649/0.657 | 0.005/0.010/0.016 | 0.033/0.058/0.110 | 0.585/0.605/0.623 | 0.043/0.066/0.101 | 0.315/0.358/0.414 | front-line cluster |
| 18-year staggered terms + regular appointments | 0.589/0.611/0.628 | 0.630/0.642/0.652 | 0.052/0.073/0.109 | 0.043/0.071/0.128 | 0.572/0.597/0.615 | 0.040/0.068/0.103 | 0.318/0.361/0.420 | front-line cluster |
| Jurisdiction stripping constrained by rights carveouts | 0.591/0.611/0.627 | 0.626/0.642/0.652 | 0.051/0.072/0.109 | 0.045/0.072/0.127 | 0.577/0.600/0.622 | 0.050/0.073/0.106 | 0.322/0.378/0.424 | front-line cluster |
| Automatic merits follow-up for emergency relief | 0.592/0.610/0.625 | 0.635/0.649/0.658 | 0.009/0.015/0.025 | 0.043/0.067/0.126 | 0.582/0.604/0.623 | 0.045/0.063/0.108 | 0.318/0.368/0.422 | front-line cluster |
| 60 percent invalidation threshold | 0.590/0.610/0.628 | 0.623/0.636/0.646 | 0.045/0.068/0.098 | 0.051/0.080/0.140 | 0.572/0.595/0.616 | 0.042/0.069/0.104 | 0.319/0.367/0.418 | front-line cluster |
| Emergency integrity package | 0.591/0.609/0.623 | 0.638/0.648/0.659 | 0.009/0.015/0.025 | 0.041/0.069/0.128 | 0.586/0.605/0.623 | 0.043/0.064/0.097 | 0.318/0.367/0.415 | front-line cluster |
| Nonpartisan commission appointments | 0.587/0.608/0.625 | 0.627/0.643/0.653 | 0.052/0.076/0.113 | 0.045/0.072/0.128 | 0.573/0.596/0.620 | 0.046/0.068/0.105 | 0.319/0.367/0.425 | front-line cluster |
| Retention-election accountability court | 0.588/0.608/0.622 | 0.626/0.639/0.648 | 0.054/0.075/0.109 | 0.045/0.071/0.128 | 0.574/0.597/0.616 | 0.046/0.072/0.107 | 0.325/0.378/0.424 | front-line cluster |
| Public-interest litigation filter | 0.588/0.608/0.625 | 0.632/0.645/0.654 | 0.052/0.072/0.110 | 0.045/0.069/0.129 | 0.577/0.596/0.617 | 0.035/0.069/0.100 | 0.314/0.367/0.420 | front-line cluster |
| Mandatory written emergency reasoning | 0.586/0.607/0.623 | 0.625/0.641/0.650 | 0.029/0.046/0.074 | 0.049/0.076/0.141 | 0.574/0.596/0.617 | 0.048/0.072/0.107 | 0.321/0.370/0.423 | front-line cluster |
| Constitutional remand before invalidation | 0.585/0.607/0.623 | 0.626/0.640/0.650 | 0.053/0.076/0.111 | 0.044/0.072/0.129 | 0.587/0.610/0.629 | 0.044/0.067/0.106 | 0.318/0.365/0.419 | front-line cluster |
| Three-judge panels with en banc correction | 0.585/0.607/0.624 | 0.630/0.643/0.650 | 0.051/0.074/0.108 | 0.045/0.073/0.128 | 0.574/0.599/0.619 | 0.041/0.065/0.113 | 0.319/0.361/0.419 | front-line cluster |
| Peer recusal + reasoned emergency docket | 0.584/0.606/0.624 | 0.629/0.641/0.650 | 0.050/0.072/0.108 | 0.043/0.069/0.127 | 0.573/0.597/0.618 | 0.045/0.070/0.111 | 0.316/0.367/0.421 | front-line cluster |
| Independent recusal enforcement with substitutes | 0.584/0.606/0.624 | 0.632/0.642/0.652 | 0.053/0.075/0.112 | 0.046/0.073/0.134 | 0.574/0.597/0.617 | 0.045/0.072/0.106 | 0.320/0.367/0.424 | front-line cluster |
| Judicial review with legislative supermajority override | 0.586/0.605/0.622 | 0.630/0.643/0.650 | 0.049/0.074/0.113 | 0.044/0.070/0.129 | 0.573/0.594/0.616 | 0.047/0.078/0.108 | 0.324/0.379/0.429 | front-line cluster |
| Time-limited legislative override window | 0.586/0.605/0.624 | 0.631/0.644/0.650 | 0.055/0.076/0.111 | 0.045/0.072/0.129 | 0.573/0.594/0.617 | 0.049/0.072/0.113 | 0.330/0.380/0.432 | front-line cluster |
| Randomized merits panels with en banc correction | 0.583/0.605/0.622 | 0.632/0.641/0.651 | 0.053/0.074/0.109 | 0.045/0.071/0.126 | 0.574/0.597/0.615 | 0.043/0.069/0.109 | 0.320/0.366/0.414 | front-line cluster |
| Expanded 15-seat court | 0.584/0.605/0.621 | 0.629/0.643/0.651 | 0.051/0.072/0.109 | 0.043/0.071/0.126 | 0.576/0.597/0.617 | 0.043/0.069/0.101 | 0.320/0.367/0.417 | front-line cluster |
| Constitutional remand with override window | 0.580/0.604/0.621 | 0.625/0.638/0.648 | 0.030/0.046/0.074 | 0.050/0.078/0.139 | 0.583/0.611/0.629 | 0.040/0.066/0.111 | 0.312/0.363/0.420 | front-line cluster |
| Random panels with jurisdiction safeguards | 0.582/0.603/0.621 | 0.622/0.638/0.647 | 0.044/0.065/0.100 | 0.051/0.079/0.141 | 0.571/0.597/0.619 | 0.050/0.073/0.114 | 0.321/0.372/0.426 | front-line cluster |
| Pre-enactment constitutional council | 0.583/0.603/0.620 | 0.629/0.642/0.654 | 0.051/0.075/0.110 | 0.044/0.072/0.130 | 0.579/0.603/0.622 | 0.050/0.066/0.109 | 0.325/0.377/0.428 | front-line cluster |
| Constitutional council with concrete-review backstop | 0.581/0.601/0.619 | 0.626/0.642/0.648 | 0.051/0.073/0.107 | 0.044/0.071/0.126 | 0.582/0.602/0.625 | 0.046/0.071/0.104 | 0.325/0.374/0.423 | front-line cluster |
| Comparative 16-seat constitutional senates | 0.578/0.600/0.618 | 0.624/0.636/0.645 | 0.044/0.067/0.099 | 0.052/0.080/0.145 | 0.572/0.596/0.618 | 0.039/0.072/0.112 | 0.322/0.367/0.422 | front-line cluster |
| Judicial electorate selection court | 0.579/0.600/0.617 | 0.629/0.645/0.651 | 0.052/0.075/0.111 | 0.045/0.073/0.130 | 0.574/0.598/0.615 | 0.046/0.071/0.112 | 0.319/0.371/0.424 | front-line cluster |
| Stylized current U.S.-like supreme court | 0.568/0.594/0.616 | 0.628/0.645/0.660 | 0.168/0.232/0.324 | 0.080/0.123/0.197 | 0.541/0.577/0.603 | 0.049/0.098/0.153 | 0.338/0.399/0.466 | overlapping uncertainty band |
| Supreme court with cross-checking constitutional court | 0.569/0.592/0.608 | 0.612/0.628/0.641 | 0.045/0.064/0.097 | 0.052/0.079/0.140 | 0.573/0.598/0.619 | 0.050/0.084/0.113 | 0.343/0.391/0.452 | overlapping uncertainty band |
| Dual supreme courts with disagreement filter | 0.558/0.581/0.599 | 0.632/0.641/0.653 | 0.046/0.065/0.101 | 0.051/0.083/0.143 | 0.560/0.588/0.612 | 0.054/0.083/0.127 | 0.344/0.396/0.461 | overlapping uncertainty band |
