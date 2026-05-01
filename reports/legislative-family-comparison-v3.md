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
| simulation-campaign-v0.csv | 0.281 | 0.593 | 0.167 | 0.200 | 0.280 | 0.144 | 0.597 | 0.228 | 60 percent invalidation threshold (0.771) |
| simulation-campaign-v5.csv | 0.429 | 0.554 | 0.239 | 0.200 | 0.280 | 0.262 | 0.562 | 0.285 | 60 percent invalidation threshold (0.765) |
| simulation-campaign-v10.csv | 0.518 | 0.582 | 0.268 | 0.200 | 0.227 | 0.326 | 0.565 | 0.307 | 60 percent invalidation threshold (0.762) |
| simulation-campaign-v15.csv | 0.500 | 0.594 | 0.255 | 0.110 | 0.230 | 0.323 | 0.513 | 0.293 | 60 percent invalidation threshold (0.766) |
| simulation-campaign-v20.csv | 0.584 | 0.564 | 0.251 | 0.116 | 0.246 | 0.334 | 0.494 | 0.302 | 60 percent invalidation threshold (0.765) |
| simulation-campaign-v21-paper.csv | 0.324 | 0.617 | 0.174 | 0.106 | 0.233 | 0.121 | 0.550 | 0.213 | 60 percent invalidation threshold (0.775) |
| simulation-manipulation-stress.csv | 0.283 | 0.582 | 0.102 | 0.163 | 0.274 | 0.097 | 0.552 | 0.202 | 60 percent invalidation threshold (0.776) |

## Scenario Sensitivity By Family

| Family | Scenario | Directional | Legal | Rights | Shadow | Conflict | Strategic | Override att. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| simulation-campaign-v0.csv | 60 percent invalidation threshold | 0.771 | 0.727 | 0.682 | 0.055 | 0.405 | 0.169 | 0.000 |
| simulation-campaign-v0.csv | 18-year staggered terms + regular appointments | 0.766 | 0.725 | 0.692 | 0.084 | 0.406 | 0.166 | 0.000 |
| simulation-campaign-v0.csv | Stylized current U.S.-like supreme court | 0.761 | 0.715 | 0.697 | 0.279 | 0.417 | 0.196 | 0.000 |
| simulation-campaign-v0.csv | No emergency relief without merits review | 0.761 | 0.735 | 0.677 | 0.003 | 0.397 | 0.146 | 0.000 |
| simulation-campaign-v0.csv | Nonpartisan commission appointments | 0.761 | 0.726 | 0.695 | 0.077 | 0.406 | 0.165 | 0.000 |
| simulation-campaign-v0.csv | Three-judge panels with en banc correction | 0.760 | 0.723 | 0.698 | 0.076 | 0.406 | 0.167 | 0.000 |
| simulation-campaign-v0.csv | Retention-election accountability court | 0.759 | 0.727 | 0.683 | 0.077 | 0.410 | 0.167 | 0.052 |
| simulation-campaign-v0.csv | Judicial review with legislative supermajority override | 0.757 | 0.724 | 0.694 | 0.077 | 0.415 | 0.177 | 0.063 |
| simulation-campaign-v0.csv | Expanded 15-seat court | 0.755 | 0.724 | 0.698 | 0.076 | 0.406 | 0.166 | 0.000 |
| simulation-campaign-v0.csv | Peer recusal + reasoned emergency docket | 0.754 | 0.725 | 0.693 | 0.077 | 0.405 | 0.165 | 0.000 |
| simulation-campaign-v0.csv | Pre-enactment constitutional council | 0.740 | 0.732 | 0.683 | 0.076 | 0.410 | 0.169 | 0.046 |
| simulation-campaign-v0.csv | Supreme court with cross-checking constitutional court | 0.718 | 0.712 | 0.677 | 0.059 | 0.445 | 0.176 | 0.000 |
| simulation-campaign-v0.csv | Dual supreme courts with disagreement filter | 0.703 | 0.703 | 0.696 | 0.056 | 0.448 | 0.181 | 0.000 |
| simulation-campaign-v10.csv | 60 percent invalidation threshold | 0.762 | 0.713 | 0.693 | 0.068 | 0.417 | 0.179 | 0.000 |
| simulation-campaign-v10.csv | 18-year staggered terms + regular appointments | 0.761 | 0.712 | 0.702 | 0.088 | 0.416 | 0.173 | 0.000 |
| simulation-campaign-v10.csv | No emergency relief without merits review | 0.756 | 0.721 | 0.694 | 0.004 | 0.408 | 0.154 | 0.000 |
| simulation-campaign-v10.csv | Nonpartisan commission appointments | 0.753 | 0.715 | 0.703 | 0.087 | 0.415 | 0.169 | 0.000 |
| simulation-campaign-v10.csv | Retention-election accountability court | 0.753 | 0.715 | 0.690 | 0.085 | 0.423 | 0.174 | 0.076 |
| simulation-campaign-v10.csv | Stylized current U.S.-like supreme court | 0.753 | 0.702 | 0.705 | 0.314 | 0.429 | 0.205 | 0.000 |
| simulation-campaign-v10.csv | Three-judge panels with en banc correction | 0.752 | 0.712 | 0.703 | 0.085 | 0.416 | 0.172 | 0.000 |
| simulation-campaign-v10.csv | Judicial review with legislative supermajority override | 0.749 | 0.711 | 0.704 | 0.088 | 0.427 | 0.186 | 0.075 |
| simulation-campaign-v10.csv | Peer recusal + reasoned emergency docket | 0.749 | 0.713 | 0.704 | 0.087 | 0.416 | 0.173 | 0.000 |
| simulation-campaign-v10.csv | Expanded 15-seat court | 0.748 | 0.711 | 0.708 | 0.084 | 0.416 | 0.173 | 0.000 |
| simulation-campaign-v10.csv | Pre-enactment constitutional council | 0.733 | 0.717 | 0.699 | 0.085 | 0.425 | 0.183 | 0.072 |
| simulation-campaign-v10.csv | Supreme court with cross-checking constitutional court | 0.711 | 0.698 | 0.686 | 0.065 | 0.457 | 0.183 | 0.000 |
| simulation-campaign-v10.csv | Dual supreme courts with disagreement filter | 0.694 | 0.690 | 0.706 | 0.069 | 0.463 | 0.190 | 0.000 |
| simulation-campaign-v15.csv | 60 percent invalidation threshold | 0.766 | 0.722 | 0.694 | 0.065 | 0.402 | 0.170 | 0.000 |
| simulation-campaign-v15.csv | 18-year staggered terms + regular appointments | 0.765 | 0.723 | 0.703 | 0.087 | 0.401 | 0.164 | 0.000 |
| simulation-campaign-v15.csv | No emergency relief without merits review | 0.759 | 0.731 | 0.691 | 0.004 | 0.394 | 0.146 | 0.000 |
| simulation-campaign-v15.csv | Nonpartisan commission appointments | 0.757 | 0.724 | 0.701 | 0.084 | 0.400 | 0.162 | 0.000 |
| simulation-campaign-v15.csv | Retention-election accountability court | 0.757 | 0.724 | 0.695 | 0.082 | 0.407 | 0.167 | 0.056 |
| simulation-campaign-v15.csv | Judicial review with legislative supermajority override | 0.755 | 0.720 | 0.704 | 0.082 | 0.411 | 0.176 | 0.060 |
| simulation-campaign-v15.csv | Three-judge panels with en banc correction | 0.754 | 0.725 | 0.699 | 0.088 | 0.401 | 0.163 | 0.000 |
| simulation-campaign-v15.csv | Stylized current U.S.-like supreme court | 0.753 | 0.713 | 0.699 | 0.323 | 0.413 | 0.195 | 0.000 |
| simulation-campaign-v15.csv | Peer recusal + reasoned emergency docket | 0.752 | 0.722 | 0.703 | 0.086 | 0.401 | 0.162 | 0.000 |
| simulation-campaign-v15.csv | Expanded 15-seat court | 0.750 | 0.724 | 0.699 | 0.084 | 0.401 | 0.164 | 0.000 |
| simulation-campaign-v15.csv | Pre-enactment constitutional council | 0.737 | 0.728 | 0.696 | 0.084 | 0.407 | 0.171 | 0.048 |
| simulation-campaign-v15.csv | Supreme court with cross-checking constitutional court | 0.713 | 0.709 | 0.685 | 0.066 | 0.443 | 0.176 | 0.000 |
| simulation-campaign-v15.csv | Dual supreme courts with disagreement filter | 0.697 | 0.699 | 0.706 | 0.066 | 0.449 | 0.183 | 0.000 |
| simulation-campaign-v20.csv | 60 percent invalidation threshold | 0.765 | 0.715 | 0.696 | 0.063 | 0.411 | 0.176 | 0.000 |
| simulation-campaign-v20.csv | 18-year staggered terms + regular appointments | 0.762 | 0.714 | 0.707 | 0.084 | 0.410 | 0.171 | 0.000 |
| simulation-campaign-v20.csv | No emergency relief without merits review | 0.755 | 0.724 | 0.696 | 0.004 | 0.403 | 0.152 | 0.000 |
| simulation-campaign-v20.csv | Nonpartisan commission appointments | 0.754 | 0.715 | 0.708 | 0.085 | 0.410 | 0.168 | 0.000 |
| simulation-campaign-v20.csv | Stylized current U.S.-like supreme court | 0.754 | 0.703 | 0.706 | 0.302 | 0.422 | 0.200 | 0.000 |
| simulation-campaign-v20.csv | Retention-election accountability court | 0.753 | 0.717 | 0.699 | 0.082 | 0.417 | 0.172 | 0.066 |
| simulation-campaign-v20.csv | Three-judge panels with en banc correction | 0.753 | 0.716 | 0.704 | 0.085 | 0.410 | 0.169 | 0.000 |
| simulation-campaign-v20.csv | Judicial review with legislative supermajority override | 0.752 | 0.711 | 0.710 | 0.087 | 0.419 | 0.182 | 0.060 |
| simulation-campaign-v20.csv | Peer recusal + reasoned emergency docket | 0.750 | 0.714 | 0.712 | 0.085 | 0.411 | 0.171 | 0.000 |
| simulation-campaign-v20.csv | Expanded 15-seat court | 0.749 | 0.714 | 0.707 | 0.086 | 0.411 | 0.172 | 0.000 |
| simulation-campaign-v20.csv | Pre-enactment constitutional council | 0.734 | 0.723 | 0.694 | 0.084 | 0.414 | 0.173 | 0.048 |
| simulation-campaign-v20.csv | Supreme court with cross-checking constitutional court | 0.711 | 0.701 | 0.691 | 0.065 | 0.454 | 0.182 | 0.000 |
| simulation-campaign-v20.csv | Dual supreme courts with disagreement filter | 0.695 | 0.691 | 0.707 | 0.068 | 0.456 | 0.187 | 0.000 |
| simulation-campaign-v21-paper.csv | 60 percent invalidation threshold | 0.775 | 0.737 | 0.686 | 0.053 | 0.388 | 0.159 | 0.000 |
| simulation-campaign-v21-paper.csv | 18-year staggered terms + regular appointments | 0.774 | 0.737 | 0.694 | 0.070 | 0.388 | 0.155 | 0.000 |
| simulation-campaign-v21-paper.csv | No emergency relief without merits review | 0.766 | 0.744 | 0.681 | 0.002 | 0.380 | 0.137 | 0.000 |
| simulation-campaign-v21-paper.csv | Stylized current U.S.-like supreme court | 0.766 | 0.729 | 0.697 | 0.278 | 0.398 | 0.182 | 0.000 |
| simulation-campaign-v21-paper.csv | Nonpartisan commission appointments | 0.765 | 0.738 | 0.694 | 0.075 | 0.387 | 0.154 | 0.000 |
| simulation-campaign-v21-paper.csv | Three-judge panels with en banc correction | 0.765 | 0.738 | 0.694 | 0.071 | 0.387 | 0.153 | 0.000 |
| simulation-campaign-v21-paper.csv | Judicial review with legislative supermajority override | 0.764 | 0.736 | 0.696 | 0.072 | 0.394 | 0.163 | 0.046 |
| simulation-campaign-v21-paper.csv | Retention-election accountability court | 0.764 | 0.740 | 0.683 | 0.075 | 0.390 | 0.155 | 0.035 |
| simulation-campaign-v21-paper.csv | Peer recusal + reasoned emergency docket | 0.761 | 0.738 | 0.695 | 0.073 | 0.387 | 0.153 | 0.000 |
| simulation-campaign-v21-paper.csv | Expanded 15-seat court | 0.761 | 0.735 | 0.699 | 0.071 | 0.388 | 0.156 | 0.000 |
| simulation-campaign-v21-paper.csv | Pre-enactment constitutional council | 0.746 | 0.742 | 0.685 | 0.072 | 0.391 | 0.157 | 0.035 |
| simulation-campaign-v21-paper.csv | Supreme court with cross-checking constitutional court | 0.724 | 0.723 | 0.680 | 0.052 | 0.427 | 0.163 | 0.000 |
| simulation-campaign-v21-paper.csv | Dual supreme courts with disagreement filter | 0.707 | 0.716 | 0.697 | 0.054 | 0.429 | 0.171 | 0.000 |
| simulation-campaign-v5.csv | 60 percent invalidation threshold | 0.765 | 0.712 | 0.691 | 0.062 | 0.414 | 0.177 | 0.000 |
| simulation-campaign-v5.csv | 18-year staggered terms + regular appointments | 0.764 | 0.712 | 0.699 | 0.081 | 0.413 | 0.172 | 0.000 |
| simulation-campaign-v5.csv | Nonpartisan commission appointments | 0.757 | 0.711 | 0.700 | 0.077 | 0.413 | 0.171 | 0.000 |
| simulation-campaign-v5.csv | No emergency relief without merits review | 0.756 | 0.722 | 0.684 | 0.004 | 0.405 | 0.154 | 0.000 |
| simulation-campaign-v5.csv | Stylized current U.S.-like supreme court | 0.756 | 0.703 | 0.703 | 0.295 | 0.425 | 0.202 | 0.000 |
| simulation-campaign-v5.csv | Retention-election accountability court | 0.754 | 0.714 | 0.688 | 0.083 | 0.420 | 0.176 | 0.069 |
| simulation-campaign-v5.csv | Judicial review with legislative supermajority override | 0.752 | 0.707 | 0.702 | 0.080 | 0.425 | 0.188 | 0.079 |
| simulation-campaign-v5.csv | Three-judge panels with en banc correction | 0.752 | 0.715 | 0.694 | 0.084 | 0.412 | 0.170 | 0.000 |
| simulation-campaign-v5.csv | Expanded 15-seat court | 0.749 | 0.712 | 0.702 | 0.082 | 0.413 | 0.172 | 0.000 |
| simulation-campaign-v5.csv | Peer recusal + reasoned emergency docket | 0.749 | 0.712 | 0.697 | 0.085 | 0.413 | 0.171 | 0.000 |
| simulation-campaign-v5.csv | Pre-enactment constitutional council | 0.733 | 0.719 | 0.691 | 0.078 | 0.420 | 0.178 | 0.063 |
| simulation-campaign-v5.csv | Supreme court with cross-checking constitutional court | 0.713 | 0.700 | 0.678 | 0.063 | 0.455 | 0.180 | 0.000 |
| simulation-campaign-v5.csv | Dual supreme courts with disagreement filter | 0.695 | 0.685 | 0.700 | 0.063 | 0.461 | 0.188 | 0.000 |
| simulation-manipulation-stress.csv | 60 percent invalidation threshold | 0.776 | 0.731 | 0.688 | 0.052 | 0.395 | 0.165 | 0.000 |
| simulation-manipulation-stress.csv | 18-year staggered terms + regular appointments | 0.774 | 0.733 | 0.693 | 0.071 | 0.393 | 0.157 | 0.000 |
| simulation-manipulation-stress.csv | Nonpartisan commission appointments | 0.766 | 0.735 | 0.690 | 0.071 | 0.392 | 0.155 | 0.000 |
| simulation-manipulation-stress.csv | Stylized current U.S.-like supreme court | 0.766 | 0.724 | 0.693 | 0.279 | 0.404 | 0.185 | 0.000 |
| simulation-manipulation-stress.csv | No emergency relief without merits review | 0.765 | 0.739 | 0.680 | 0.002 | 0.387 | 0.142 | 0.000 |
| simulation-manipulation-stress.csv | Retention-election accountability court | 0.765 | 0.734 | 0.685 | 0.074 | 0.398 | 0.161 | 0.046 |
| simulation-manipulation-stress.csv | Three-judge panels with en banc correction | 0.764 | 0.734 | 0.689 | 0.073 | 0.392 | 0.155 | 0.000 |
| simulation-manipulation-stress.csv | Judicial review with legislative supermajority override | 0.763 | 0.730 | 0.698 | 0.070 | 0.403 | 0.169 | 0.059 |
| simulation-manipulation-stress.csv | Peer recusal + reasoned emergency docket | 0.762 | 0.734 | 0.694 | 0.069 | 0.393 | 0.157 | 0.000 |
| simulation-manipulation-stress.csv | Expanded 15-seat court | 0.760 | 0.734 | 0.692 | 0.071 | 0.393 | 0.157 | 0.000 |
| simulation-manipulation-stress.csv | Pre-enactment constitutional council | 0.746 | 0.739 | 0.685 | 0.070 | 0.397 | 0.160 | 0.039 |
| simulation-manipulation-stress.csv | Supreme court with cross-checking constitutional court | 0.724 | 0.719 | 0.679 | 0.052 | 0.432 | 0.168 | 0.000 |
| simulation-manipulation-stress.csv | Dual supreme courts with disagreement filter | 0.708 | 0.712 | 0.698 | 0.054 | 0.435 | 0.174 | 0.000 |
