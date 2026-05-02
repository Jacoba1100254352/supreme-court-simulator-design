# Legislative Family Import Comparison v3

Compares the constitutional-review import contract across multiple congressional-simulator report families.

## Run Configuration

- legislative family directory: /Users/jacobanderson/Documents/simulators/Congress Institutional Simulator/reports
- imported families: 7
- runs per family: 40
- cases per run: 48
- base seed: 20260501

## Imported Profiles

| Family | Volume | Quality | Weak mandate | Rights risk | Partisan skew | Volatility | Legitimacy | Override pressure | Best scenario |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| simulation-campaign-v0.csv | 0.281 | 0.593 | 0.167 | 0.200 | 0.280 | 0.144 | 0.597 | 0.228 | 18-year staggered terms + regular appointments (0.604) |
| simulation-campaign-v5.csv | 0.429 | 0.554 | 0.239 | 0.200 | 0.280 | 0.262 | 0.562 | 0.285 | 18-year staggered terms + regular appointments (0.600) |
| simulation-campaign-v10.csv | 0.518 | 0.582 | 0.268 | 0.200 | 0.227 | 0.326 | 0.565 | 0.307 | 18-year staggered terms + regular appointments (0.598) |
| simulation-campaign-v15.csv | 0.500 | 0.594 | 0.255 | 0.110 | 0.230 | 0.323 | 0.513 | 0.293 | 18-year staggered terms + regular appointments (0.597) |
| simulation-campaign-v20.csv | 0.584 | 0.564 | 0.251 | 0.116 | 0.246 | 0.334 | 0.494 | 0.302 | 18-year staggered terms + regular appointments (0.598) |
| simulation-campaign-v21-paper.csv | 0.343 | 0.610 | 0.175 | 0.104 | 0.237 | 0.120 | 0.547 | 0.213 | 18-year staggered terms + regular appointments (0.604) |
| simulation-manipulation-stress.csv | 0.283 | 0.582 | 0.102 | 0.163 | 0.274 | 0.097 | 0.552 | 0.202 | 18-year staggered terms + regular appointments (0.603) |

## Scenario Sensitivity By Family

| Family | Scenario | Directional | Legal | Rights | Shadow | Conflict | Strategic | Override att. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| simulation-campaign-v0.csv | 18-year staggered terms + regular appointments | 0.604 | 0.705 | 0.621 | 0.045 | 0.300 | 0.147 | 0.000 |
| simulation-campaign-v0.csv | Stylized current U.S.-like supreme court | 0.602 | 0.702 | 0.617 | 0.151 | 0.302 | 0.150 | 0.000 |
| simulation-campaign-v0.csv | 60 percent invalidation threshold | 0.601 | 0.706 | 0.606 | 0.033 | 0.295 | 0.150 | 0.000 |
| simulation-campaign-v0.csv | Nonpartisan commission appointments | 0.600 | 0.706 | 0.617 | 0.042 | 0.297 | 0.131 | 0.000 |
| simulation-campaign-v0.csv | Judicial review with legislative supermajority override | 0.599 | 0.708 | 0.618 | 0.040 | 0.302 | 0.133 | 0.027 |
| simulation-campaign-v0.csv | No emergency relief without merits review | 0.599 | 0.710 | 0.619 | 0.001 | 0.303 | 0.128 | 0.000 |
| simulation-campaign-v0.csv | Peer recusal + reasoned emergency docket | 0.598 | 0.707 | 0.611 | 0.043 | 0.290 | 0.143 | 0.000 |
| simulation-campaign-v0.csv | Retention-election accountability court | 0.597 | 0.708 | 0.617 | 0.039 | 0.309 | 0.136 | 0.028 |
| simulation-campaign-v0.csv | Three-judge panels with en banc correction | 0.597 | 0.707 | 0.619 | 0.042 | 0.305 | 0.135 | 0.000 |
| simulation-campaign-v0.csv | Expanded 15-seat court | 0.596 | 0.707 | 0.616 | 0.043 | 0.299 | 0.143 | 0.000 |
| simulation-campaign-v0.csv | Pre-enactment constitutional council | 0.588 | 0.713 | 0.612 | 0.043 | 0.306 | 0.135 | 0.019 |
| simulation-campaign-v0.csv | Comparative 16-seat constitutional senates | 0.587 | 0.710 | 0.602 | 0.035 | 0.295 | 0.130 | 0.000 |
| simulation-campaign-v0.csv | Supreme court with cross-checking constitutional court | 0.575 | 0.697 | 0.608 | 0.035 | 0.324 | 0.133 | 0.000 |
| simulation-campaign-v0.csv | Dual supreme courts with disagreement filter | 0.572 | 0.689 | 0.623 | 0.037 | 0.329 | 0.147 | 0.000 |
| simulation-campaign-v10.csv | 18-year staggered terms + regular appointments | 0.598 | 0.697 | 0.630 | 0.053 | 0.318 | 0.154 | 0.000 |
| simulation-campaign-v10.csv | Nonpartisan commission appointments | 0.596 | 0.698 | 0.632 | 0.054 | 0.320 | 0.142 | 0.000 |
| simulation-campaign-v10.csv | 60 percent invalidation threshold | 0.596 | 0.699 | 0.619 | 0.044 | 0.315 | 0.154 | 0.000 |
| simulation-campaign-v10.csv | No emergency relief without merits review | 0.594 | 0.704 | 0.624 | 0.001 | 0.313 | 0.136 | 0.000 |
| simulation-campaign-v10.csv | Three-judge panels with en banc correction | 0.593 | 0.697 | 0.630 | 0.054 | 0.319 | 0.144 | 0.000 |
| simulation-campaign-v10.csv | Judicial review with legislative supermajority override | 0.593 | 0.697 | 0.633 | 0.053 | 0.326 | 0.147 | 0.034 |
| simulation-campaign-v10.csv | Stylized current U.S.-like supreme court | 0.593 | 0.694 | 0.621 | 0.187 | 0.318 | 0.166 | 0.000 |
| simulation-campaign-v10.csv | Retention-election accountability court | 0.592 | 0.702 | 0.623 | 0.053 | 0.323 | 0.143 | 0.028 |
| simulation-campaign-v10.csv | Peer recusal + reasoned emergency docket | 0.592 | 0.698 | 0.625 | 0.052 | 0.315 | 0.153 | 0.000 |
| simulation-campaign-v10.csv | Expanded 15-seat court | 0.591 | 0.698 | 0.625 | 0.052 | 0.313 | 0.152 | 0.000 |
| simulation-campaign-v10.csv | Pre-enactment constitutional council | 0.584 | 0.702 | 0.620 | 0.053 | 0.316 | 0.143 | 0.026 |
| simulation-campaign-v10.csv | Comparative 16-seat constitutional senates | 0.583 | 0.700 | 0.617 | 0.047 | 0.317 | 0.136 | 0.000 |
| simulation-campaign-v10.csv | Supreme court with cross-checking constitutional court | 0.566 | 0.687 | 0.620 | 0.046 | 0.350 | 0.151 | 0.000 |
| simulation-campaign-v10.csv | Dual supreme courts with disagreement filter | 0.563 | 0.678 | 0.633 | 0.046 | 0.350 | 0.153 | 0.000 |
| simulation-campaign-v15.csv | 18-year staggered terms + regular appointments | 0.597 | 0.703 | 0.632 | 0.053 | 0.307 | 0.151 | 0.000 |
| simulation-campaign-v15.csv | 60 percent invalidation threshold | 0.597 | 0.704 | 0.621 | 0.042 | 0.302 | 0.147 | 0.000 |
| simulation-campaign-v15.csv | Retention-election accountability court | 0.595 | 0.705 | 0.629 | 0.048 | 0.310 | 0.137 | 0.023 |
| simulation-campaign-v15.csv | Nonpartisan commission appointments | 0.593 | 0.705 | 0.634 | 0.052 | 0.313 | 0.144 | 0.000 |
| simulation-campaign-v15.csv | Judicial review with legislative supermajority override | 0.593 | 0.702 | 0.638 | 0.052 | 0.318 | 0.144 | 0.028 |
| simulation-campaign-v15.csv | Stylized current U.S.-like supreme court | 0.593 | 0.698 | 0.631 | 0.191 | 0.316 | 0.164 | 0.000 |
| simulation-campaign-v15.csv | Expanded 15-seat court | 0.591 | 0.704 | 0.631 | 0.052 | 0.305 | 0.150 | 0.000 |
| simulation-campaign-v15.csv | Three-judge panels with en banc correction | 0.591 | 0.705 | 0.630 | 0.054 | 0.311 | 0.138 | 0.000 |
| simulation-campaign-v15.csv | Peer recusal + reasoned emergency docket | 0.591 | 0.706 | 0.637 | 0.055 | 0.314 | 0.154 | 0.000 |
| simulation-campaign-v15.csv | No emergency relief without merits review | 0.591 | 0.708 | 0.635 | 0.001 | 0.315 | 0.138 | 0.000 |
| simulation-campaign-v15.csv | Pre-enactment constitutional council | 0.586 | 0.707 | 0.628 | 0.048 | 0.309 | 0.137 | 0.022 |
| simulation-campaign-v15.csv | Comparative 16-seat constitutional senates | 0.585 | 0.706 | 0.626 | 0.042 | 0.308 | 0.135 | 0.000 |
| simulation-campaign-v15.csv | Supreme court with cross-checking constitutional court | 0.566 | 0.691 | 0.624 | 0.046 | 0.342 | 0.147 | 0.000 |
| simulation-campaign-v15.csv | Dual supreme courts with disagreement filter | 0.565 | 0.686 | 0.640 | 0.043 | 0.345 | 0.148 | 0.000 |
| simulation-campaign-v20.csv | 18-year staggered terms + regular appointments | 0.598 | 0.696 | 0.631 | 0.050 | 0.306 | 0.150 | 0.000 |
| simulation-campaign-v20.csv | 60 percent invalidation threshold | 0.596 | 0.698 | 0.626 | 0.042 | 0.310 | 0.151 | 0.000 |
| simulation-campaign-v20.csv | Stylized current U.S.-like supreme court | 0.594 | 0.690 | 0.631 | 0.180 | 0.315 | 0.164 | 0.000 |
| simulation-campaign-v20.csv | Nonpartisan commission appointments | 0.594 | 0.700 | 0.637 | 0.050 | 0.318 | 0.142 | 0.000 |
| simulation-campaign-v20.csv | Judicial review with legislative supermajority override | 0.593 | 0.694 | 0.637 | 0.051 | 0.318 | 0.147 | 0.038 |
| simulation-campaign-v20.csv | Three-judge panels with en banc correction | 0.593 | 0.697 | 0.634 | 0.054 | 0.317 | 0.140 | 0.000 |
| simulation-campaign-v20.csv | Retention-election accountability court | 0.592 | 0.701 | 0.626 | 0.050 | 0.314 | 0.138 | 0.026 |
| simulation-campaign-v20.csv | Expanded 15-seat court | 0.591 | 0.700 | 0.629 | 0.049 | 0.307 | 0.147 | 0.000 |
| simulation-campaign-v20.csv | No emergency relief without merits review | 0.591 | 0.705 | 0.629 | 0.001 | 0.312 | 0.134 | 0.000 |
| simulation-campaign-v20.csv | Peer recusal + reasoned emergency docket | 0.591 | 0.697 | 0.633 | 0.051 | 0.313 | 0.155 | 0.000 |
| simulation-campaign-v20.csv | Comparative 16-seat constitutional senates | 0.584 | 0.697 | 0.626 | 0.042 | 0.311 | 0.145 | 0.000 |
| simulation-campaign-v20.csv | Pre-enactment constitutional council | 0.582 | 0.702 | 0.630 | 0.055 | 0.320 | 0.144 | 0.021 |
| simulation-campaign-v20.csv | Supreme court with cross-checking constitutional court | 0.566 | 0.686 | 0.627 | 0.044 | 0.349 | 0.147 | 0.000 |
| simulation-campaign-v20.csv | Dual supreme courts with disagreement filter | 0.565 | 0.681 | 0.634 | 0.043 | 0.341 | 0.146 | 0.000 |
| simulation-campaign-v21-paper.csv | 18-year staggered terms + regular appointments | 0.604 | 0.713 | 0.625 | 0.037 | 0.283 | 0.135 | 0.000 |
| simulation-campaign-v21-paper.csv | 60 percent invalidation threshold | 0.603 | 0.713 | 0.625 | 0.037 | 0.288 | 0.141 | 0.000 |
| simulation-campaign-v21-paper.csv | Stylized current U.S.-like supreme court | 0.602 | 0.707 | 0.630 | 0.153 | 0.292 | 0.146 | 0.000 |
| simulation-campaign-v21-paper.csv | Three-judge panels with en banc correction | 0.601 | 0.713 | 0.629 | 0.040 | 0.286 | 0.125 | 0.000 |
| simulation-campaign-v21-paper.csv | Retention-election accountability court | 0.600 | 0.714 | 0.622 | 0.042 | 0.287 | 0.125 | 0.015 |
| simulation-campaign-v21-paper.csv | No emergency relief without merits review | 0.600 | 0.718 | 0.622 | 0.001 | 0.282 | 0.117 | 0.000 |
| simulation-campaign-v21-paper.csv | Nonpartisan commission appointments | 0.600 | 0.715 | 0.628 | 0.039 | 0.288 | 0.130 | 0.000 |
| simulation-campaign-v21-paper.csv | Judicial review with legislative supermajority override | 0.599 | 0.713 | 0.634 | 0.043 | 0.296 | 0.134 | 0.023 |
| simulation-campaign-v21-paper.csv | Expanded 15-seat court | 0.598 | 0.713 | 0.626 | 0.040 | 0.283 | 0.140 | 0.000 |
| simulation-campaign-v21-paper.csv | Peer recusal + reasoned emergency docket | 0.597 | 0.715 | 0.622 | 0.041 | 0.283 | 0.136 | 0.000 |
| simulation-campaign-v21-paper.csv | Pre-enactment constitutional council | 0.591 | 0.717 | 0.625 | 0.040 | 0.290 | 0.127 | 0.015 |
| simulation-campaign-v21-paper.csv | Comparative 16-seat constitutional senates | 0.589 | 0.715 | 0.621 | 0.037 | 0.290 | 0.131 | 0.000 |
| simulation-campaign-v21-paper.csv | Supreme court with cross-checking constitutional court | 0.575 | 0.704 | 0.623 | 0.033 | 0.318 | 0.131 | 0.000 |
| simulation-campaign-v21-paper.csv | Dual supreme courts with disagreement filter | 0.572 | 0.698 | 0.635 | 0.034 | 0.320 | 0.138 | 0.000 |
| simulation-campaign-v5.csv | 18-year staggered terms + regular appointments | 0.600 | 0.697 | 0.628 | 0.049 | 0.312 | 0.154 | 0.000 |
| simulation-campaign-v5.csv | 60 percent invalidation threshold | 0.597 | 0.697 | 0.623 | 0.042 | 0.316 | 0.158 | 0.000 |
| simulation-campaign-v5.csv | Stylized current U.S.-like supreme court | 0.596 | 0.691 | 0.627 | 0.183 | 0.318 | 0.171 | 0.000 |
| simulation-campaign-v5.csv | Nonpartisan commission appointments | 0.594 | 0.701 | 0.628 | 0.051 | 0.317 | 0.142 | 0.000 |
| simulation-campaign-v5.csv | No emergency relief without merits review | 0.594 | 0.704 | 0.626 | 0.001 | 0.313 | 0.133 | 0.000 |
| simulation-campaign-v5.csv | Retention-election accountability court | 0.594 | 0.699 | 0.627 | 0.051 | 0.321 | 0.142 | 0.030 |
| simulation-campaign-v5.csv | Judicial review with legislative supermajority override | 0.593 | 0.698 | 0.632 | 0.049 | 0.323 | 0.144 | 0.032 |
| simulation-campaign-v5.csv | Expanded 15-seat court | 0.592 | 0.698 | 0.622 | 0.050 | 0.308 | 0.148 | 0.000 |
| simulation-campaign-v5.csv | Peer recusal + reasoned emergency docket | 0.592 | 0.700 | 0.625 | 0.048 | 0.310 | 0.151 | 0.000 |
| simulation-campaign-v5.csv | Three-judge panels with en banc correction | 0.590 | 0.701 | 0.623 | 0.054 | 0.315 | 0.145 | 0.000 |
| simulation-campaign-v5.csv | Pre-enactment constitutional council | 0.586 | 0.700 | 0.625 | 0.051 | 0.319 | 0.141 | 0.029 |
| simulation-campaign-v5.csv | Comparative 16-seat constitutional senates | 0.584 | 0.701 | 0.615 | 0.042 | 0.312 | 0.142 | 0.000 |
| simulation-campaign-v5.csv | Supreme court with cross-checking constitutional court | 0.568 | 0.688 | 0.621 | 0.045 | 0.344 | 0.149 | 0.000 |
| simulation-campaign-v5.csv | Dual supreme courts with disagreement filter | 0.566 | 0.679 | 0.635 | 0.041 | 0.351 | 0.149 | 0.000 |
| simulation-manipulation-stress.csv | 18-year staggered terms + regular appointments | 0.603 | 0.711 | 0.610 | 0.039 | 0.290 | 0.141 | 0.000 |
| simulation-manipulation-stress.csv | Stylized current U.S.-like supreme court | 0.602 | 0.706 | 0.615 | 0.149 | 0.296 | 0.151 | 0.000 |
| simulation-manipulation-stress.csv | 60 percent invalidation threshold | 0.600 | 0.711 | 0.606 | 0.034 | 0.292 | 0.147 | 0.000 |
| simulation-manipulation-stress.csv | Expanded 15-seat court | 0.599 | 0.708 | 0.616 | 0.039 | 0.290 | 0.139 | 0.000 |
| simulation-manipulation-stress.csv | Nonpartisan commission appointments | 0.599 | 0.714 | 0.615 | 0.042 | 0.297 | 0.130 | 0.000 |
| simulation-manipulation-stress.csv | Retention-election accountability court | 0.599 | 0.712 | 0.614 | 0.041 | 0.300 | 0.131 | 0.021 |
| simulation-manipulation-stress.csv | No emergency relief without merits review | 0.599 | 0.713 | 0.610 | 0.001 | 0.290 | 0.124 | 0.000 |
| simulation-manipulation-stress.csv | Judicial review with legislative supermajority override | 0.598 | 0.709 | 0.618 | 0.041 | 0.301 | 0.132 | 0.029 |
| simulation-manipulation-stress.csv | Peer recusal + reasoned emergency docket | 0.598 | 0.710 | 0.616 | 0.041 | 0.294 | 0.143 | 0.000 |
| simulation-manipulation-stress.csv | Three-judge panels with en banc correction | 0.597 | 0.710 | 0.618 | 0.045 | 0.300 | 0.137 | 0.000 |
| simulation-manipulation-stress.csv | Comparative 16-seat constitutional senates | 0.591 | 0.711 | 0.604 | 0.033 | 0.287 | 0.126 | 0.000 |
| simulation-manipulation-stress.csv | Pre-enactment constitutional council | 0.591 | 0.715 | 0.612 | 0.041 | 0.299 | 0.130 | 0.018 |
| simulation-manipulation-stress.csv | Supreme court with cross-checking constitutional court | 0.575 | 0.701 | 0.611 | 0.034 | 0.325 | 0.137 | 0.000 |
| simulation-manipulation-stress.csv | Dual supreme courts with disagreement filter | 0.570 | 0.692 | 0.621 | 0.033 | 0.328 | 0.142 | 0.000 |
