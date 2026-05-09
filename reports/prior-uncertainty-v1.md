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
| No emergency relief without merits review | 0.595/0.615/0.629 | 0.641/0.651/0.660 | 0.005/0.010/0.016 | 0.034/0.060/0.113 | 0.582/0.606/0.624 | 0.043/0.065/0.113 | 0.318/0.367/0.418 | front-line cluster |
| 18-year staggered terms + regular appointments | 0.589/0.612/0.629 | 0.633/0.645/0.654 | 0.052/0.074/0.111 | 0.045/0.074/0.133 | 0.574/0.596/0.615 | 0.040/0.066/0.108 | 0.327/0.368/0.426 | front-line cluster |
| 60 percent invalidation threshold | 0.588/0.611/0.629 | 0.628/0.640/0.649 | 0.049/0.066/0.101 | 0.055/0.081/0.145 | 0.570/0.594/0.615 | 0.044/0.076/0.112 | 0.324/0.369/0.428 | front-line cluster |
| Jurisdiction stripping constrained by rights carveouts | 0.590/0.610/0.628 | 0.635/0.645/0.654 | 0.054/0.076/0.113 | 0.046/0.072/0.130 | 0.574/0.597/0.619 | 0.047/0.078/0.117 | 0.325/0.384/0.434 | front-line cluster |
| Automatic merits follow-up for emergency relief | 0.590/0.610/0.625 | 0.635/0.652/0.662 | 0.009/0.016/0.026 | 0.043/0.069/0.129 | 0.579/0.604/0.622 | 0.046/0.070/0.114 | 0.323/0.375/0.425 | front-line cluster |
| Nonpartisan commission appointments | 0.586/0.609/0.626 | 0.635/0.646/0.658 | 0.056/0.079/0.114 | 0.046/0.075/0.129 | 0.571/0.597/0.620 | 0.043/0.069/0.115 | 0.324/0.379/0.428 | front-line cluster |
| Emergency integrity package | 0.590/0.609/0.624 | 0.639/0.653/0.660 | 0.009/0.015/0.026 | 0.043/0.071/0.131 | 0.583/0.602/0.626 | 0.043/0.066/0.097 | 0.322/0.373/0.424 | front-line cluster |
| Peer recusal + reasoned emergency docket | 0.585/0.607/0.624 | 0.633/0.645/0.656 | 0.054/0.075/0.112 | 0.045/0.071/0.132 | 0.570/0.597/0.619 | 0.042/0.071/0.112 | 0.325/0.375/0.432 | front-line cluster |
| Retention-election accountability court | 0.587/0.607/0.624 | 0.628/0.642/0.652 | 0.054/0.077/0.110 | 0.045/0.075/0.129 | 0.573/0.595/0.617 | 0.047/0.076/0.114 | 0.331/0.387/0.433 | front-line cluster |
| Constitutional remand before invalidation | 0.582/0.607/0.624 | 0.629/0.642/0.654 | 0.054/0.076/0.117 | 0.046/0.072/0.133 | 0.583/0.609/0.628 | 0.045/0.071/0.115 | 0.319/0.369/0.428 | front-line cluster |
| Three-judge panels with en banc correction | 0.586/0.607/0.624 | 0.633/0.646/0.657 | 0.054/0.078/0.113 | 0.047/0.075/0.133 | 0.574/0.596/0.617 | 0.042/0.067/0.109 | 0.325/0.371/0.427 | front-line cluster |
| Public-interest litigation filter | 0.587/0.607/0.624 | 0.635/0.650/0.657 | 0.054/0.075/0.112 | 0.044/0.072/0.133 | 0.575/0.597/0.616 | 0.044/0.073/0.104 | 0.322/0.372/0.424 | front-line cluster |
| Mandatory written emergency reasoning | 0.585/0.606/0.623 | 0.628/0.643/0.654 | 0.030/0.047/0.075 | 0.050/0.079/0.144 | 0.573/0.595/0.617 | 0.051/0.076/0.118 | 0.327/0.380/0.429 | front-line cluster |
| Independent recusal enforcement with substitutes | 0.584/0.606/0.623 | 0.638/0.646/0.654 | 0.055/0.077/0.115 | 0.046/0.075/0.133 | 0.572/0.596/0.614 | 0.046/0.074/0.117 | 0.326/0.375/0.429 | front-line cluster |
| Time-limited legislative override window | 0.583/0.605/0.623 | 0.635/0.646/0.655 | 0.056/0.076/0.113 | 0.047/0.074/0.133 | 0.569/0.594/0.617 | 0.047/0.079/0.117 | 0.335/0.384/0.439 | front-line cluster |
| Randomized merits panels with en banc correction | 0.583/0.605/0.622 | 0.634/0.646/0.655 | 0.056/0.076/0.115 | 0.048/0.073/0.131 | 0.572/0.597/0.618 | 0.047/0.071/0.109 | 0.329/0.373/0.426 | front-line cluster |
| Judicial review with legislative supermajority override | 0.582/0.605/0.621 | 0.634/0.646/0.654 | 0.052/0.075/0.116 | 0.046/0.071/0.134 | 0.566/0.594/0.615 | 0.054/0.080/0.125 | 0.332/0.387/0.441 | front-line cluster |
| Expanded 15-seat court | 0.582/0.604/0.622 | 0.636/0.646/0.654 | 0.053/0.075/0.110 | 0.045/0.073/0.129 | 0.573/0.596/0.615 | 0.046/0.080/0.111 | 0.324/0.375/0.425 | front-line cluster |
| Constitutional remand with override window | 0.580/0.604/0.622 | 0.629/0.641/0.653 | 0.031/0.048/0.075 | 0.051/0.081/0.142 | 0.584/0.609/0.629 | 0.043/0.072/0.109 | 0.318/0.371/0.430 | front-line cluster |
| Random panels with jurisdiction safeguards | 0.580/0.603/0.622 | 0.624/0.639/0.650 | 0.046/0.068/0.105 | 0.052/0.083/0.146 | 0.568/0.596/0.619 | 0.045/0.079/0.118 | 0.326/0.382/0.434 | front-line cluster |
| Pre-enactment constitutional council | 0.579/0.603/0.619 | 0.634/0.645/0.655 | 0.055/0.076/0.114 | 0.045/0.075/0.134 | 0.574/0.600/0.621 | 0.051/0.077/0.114 | 0.332/0.385/0.433 | front-line cluster |
| Constitutional council with concrete-review backstop | 0.580/0.601/0.618 | 0.634/0.646/0.654 | 0.052/0.075/0.111 | 0.044/0.073/0.128 | 0.579/0.602/0.623 | 0.049/0.075/0.121 | 0.331/0.382/0.436 | front-line cluster |
| Comparative 16-seat constitutional senates | 0.577/0.600/0.619 | 0.628/0.642/0.650 | 0.044/0.069/0.102 | 0.052/0.082/0.144 | 0.569/0.595/0.616 | 0.039/0.078/0.109 | 0.323/0.380/0.431 | overlapping uncertainty band |
| Stylized current U.S.-like supreme court | 0.565/0.593/0.613 | 0.633/0.647/0.664 | 0.181/0.246/0.347 | 0.085/0.126/0.208 | 0.536/0.571/0.599 | 0.057/0.104/0.166 | 0.349/0.407/0.480 | overlapping uncertainty band |
| Supreme court with cross-checking constitutional court | 0.566/0.588/0.608 | 0.616/0.632/0.646 | 0.047/0.068/0.100 | 0.054/0.083/0.144 | 0.573/0.597/0.619 | 0.046/0.080/0.119 | 0.346/0.400/0.459 | overlapping uncertainty band |
| Dual supreme courts with disagreement filter | 0.557/0.581/0.597 | 0.636/0.646/0.654 | 0.048/0.068/0.104 | 0.054/0.082/0.145 | 0.559/0.587/0.610 | 0.052/0.084/0.133 | 0.349/0.408/0.467 | overlapping uncertainty band |
