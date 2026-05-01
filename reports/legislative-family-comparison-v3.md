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
| simulation-campaign-v0.csv | 0.281 | 0.593 | 0.167 | 0.200 | 0.280 | 0.144 | 0.597 | 0.228 | 18-year staggered terms + regular appointments (0.726) |
| simulation-campaign-v5.csv | 0.429 | 0.554 | 0.239 | 0.200 | 0.280 | 0.262 | 0.562 | 0.285 | No emergency relief without merits review (0.719) |
| simulation-campaign-v10.csv | 0.518 | 0.582 | 0.268 | 0.200 | 0.227 | 0.326 | 0.565 | 0.307 | No emergency relief without merits review (0.715) |
| simulation-campaign-v15.csv | 0.500 | 0.594 | 0.255 | 0.110 | 0.230 | 0.323 | 0.513 | 0.293 | 18-year staggered terms + regular appointments (0.719) |
| simulation-campaign-v20.csv | 0.584 | 0.564 | 0.251 | 0.116 | 0.246 | 0.334 | 0.494 | 0.302 | 60 percent invalidation threshold (0.716) |
| simulation-campaign-v21-paper.csv | 0.324 | 0.617 | 0.174 | 0.106 | 0.233 | 0.121 | 0.550 | 0.213 | 18-year staggered terms + regular appointments (0.734) |
| simulation-manipulation-stress.csv | 0.283 | 0.582 | 0.102 | 0.163 | 0.274 | 0.097 | 0.552 | 0.202 | 18-year staggered terms + regular appointments (0.731) |

## Scenario Sensitivity By Family

| Family | Scenario | Directional | Legal | Rights | Shadow | Conflict | Strategic | Override att. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| simulation-campaign-v0.csv | 18-year staggered terms + regular appointments | 0.726 | 0.635 | 0.678 | 0.114 | 0.545 | 0.344 | 0.000 |
| simulation-campaign-v0.csv | No emergency relief without merits review | 0.724 | 0.659 | 0.649 | 0.004 | 0.531 | 0.302 | 0.000 |
| simulation-campaign-v0.csv | 60 percent invalidation threshold | 0.723 | 0.650 | 0.648 | 0.102 | 0.546 | 0.362 | 0.000 |
| simulation-campaign-v0.csv | Nonpartisan commission appointments | 0.719 | 0.633 | 0.678 | 0.113 | 0.545 | 0.316 | 0.000 |
| simulation-campaign-v0.csv | Retention-election accountability court | 0.716 | 0.651 | 0.639 | 0.112 | 0.560 | 0.322 | 0.146 |
| simulation-campaign-v0.csv | Three-judge panels with en banc correction | 0.716 | 0.647 | 0.661 | 0.112 | 0.542 | 0.312 | 0.000 |
| simulation-campaign-v0.csv | Judicial review with legislative supermajority override | 0.714 | 0.630 | 0.680 | 0.112 | 0.573 | 0.349 | 0.172 |
| simulation-campaign-v0.csv | Peer recusal + reasoned emergency docket | 0.714 | 0.634 | 0.677 | 0.105 | 0.544 | 0.338 | 0.000 |
| simulation-campaign-v0.csv | Expanded 15-seat court | 0.710 | 0.627 | 0.686 | 0.113 | 0.548 | 0.347 | 0.000 |
| simulation-campaign-v0.csv | Stylized current U.S.-like supreme court | 0.705 | 0.636 | 0.668 | 0.439 | 0.567 | 0.384 | 0.000 |
| simulation-campaign-v0.csv | Pre-enactment constitutional council | 0.687 | 0.661 | 0.652 | 0.111 | 0.560 | 0.332 | 0.129 |
| simulation-campaign-v0.csv | Supreme court with cross-checking constitutional court | 0.671 | 0.644 | 0.620 | 0.097 | 0.590 | 0.326 | 0.000 |
| simulation-campaign-v0.csv | Dual supreme courts with disagreement filter | 0.654 | 0.588 | 0.684 | 0.096 | 0.602 | 0.342 | 0.000 |
| simulation-campaign-v10.csv | No emergency relief without merits review | 0.715 | 0.641 | 0.671 | 0.006 | 0.541 | 0.306 | 0.000 |
| simulation-campaign-v10.csv | 60 percent invalidation threshold | 0.714 | 0.631 | 0.669 | 0.113 | 0.557 | 0.364 | 0.000 |
| simulation-campaign-v10.csv | 18-year staggered terms + regular appointments | 0.712 | 0.618 | 0.690 | 0.137 | 0.556 | 0.354 | 0.000 |
| simulation-campaign-v10.csv | Nonpartisan commission appointments | 0.707 | 0.616 | 0.687 | 0.127 | 0.554 | 0.331 | 0.000 |
| simulation-campaign-v10.csv | Retention-election accountability court | 0.705 | 0.625 | 0.665 | 0.128 | 0.576 | 0.340 | 0.165 |
| simulation-campaign-v10.csv | Three-judge panels with en banc correction | 0.704 | 0.624 | 0.682 | 0.127 | 0.552 | 0.329 | 0.000 |
| simulation-campaign-v10.csv | Peer recusal + reasoned emergency docket | 0.701 | 0.616 | 0.690 | 0.126 | 0.556 | 0.358 | 0.000 |
| simulation-campaign-v10.csv | Judicial review with legislative supermajority override | 0.701 | 0.599 | 0.700 | 0.128 | 0.591 | 0.369 | 0.201 |
| simulation-campaign-v10.csv | Expanded 15-seat court | 0.700 | 0.616 | 0.694 | 0.130 | 0.556 | 0.352 | 0.000 |
| simulation-campaign-v10.csv | Stylized current U.S.-like supreme court | 0.694 | 0.611 | 0.686 | 0.468 | 0.581 | 0.385 | 0.000 |
| simulation-campaign-v10.csv | Pre-enactment constitutional council | 0.676 | 0.638 | 0.674 | 0.127 | 0.575 | 0.346 | 0.151 |
| simulation-campaign-v10.csv | Supreme court with cross-checking constitutional court | 0.658 | 0.633 | 0.623 | 0.112 | 0.605 | 0.341 | 0.000 |
| simulation-campaign-v10.csv | Dual supreme courts with disagreement filter | 0.642 | 0.561 | 0.706 | 0.113 | 0.618 | 0.355 | 0.000 |
| simulation-campaign-v15.csv | 18-year staggered terms + regular appointments | 0.719 | 0.648 | 0.690 | 0.131 | 0.542 | 0.346 | 0.000 |
| simulation-campaign-v15.csv | No emergency relief without merits review | 0.719 | 0.670 | 0.662 | 0.005 | 0.528 | 0.302 | 0.000 |
| simulation-campaign-v15.csv | 60 percent invalidation threshold | 0.718 | 0.655 | 0.665 | 0.116 | 0.546 | 0.360 | 0.000 |
| simulation-campaign-v15.csv | Nonpartisan commission appointments | 0.714 | 0.649 | 0.686 | 0.128 | 0.540 | 0.315 | 0.000 |
| simulation-campaign-v15.csv | Three-judge panels with en banc correction | 0.709 | 0.656 | 0.682 | 0.133 | 0.541 | 0.319 | 0.000 |
| simulation-campaign-v15.csv | Retention-election accountability court | 0.709 | 0.652 | 0.662 | 0.131 | 0.557 | 0.327 | 0.132 |
| simulation-campaign-v15.csv | Judicial review with legislative supermajority override | 0.707 | 0.642 | 0.688 | 0.131 | 0.567 | 0.349 | 0.151 |
| simulation-campaign-v15.csv | Peer recusal + reasoned emergency docket | 0.706 | 0.653 | 0.683 | 0.132 | 0.541 | 0.345 | 0.000 |
| simulation-campaign-v15.csv | Expanded 15-seat court | 0.706 | 0.650 | 0.686 | 0.127 | 0.541 | 0.346 | 0.000 |
| simulation-campaign-v15.csv | Stylized current U.S.-like supreme court | 0.697 | 0.633 | 0.691 | 0.480 | 0.570 | 0.394 | 0.000 |
| simulation-campaign-v15.csv | Pre-enactment constitutional council | 0.681 | 0.670 | 0.661 | 0.133 | 0.554 | 0.331 | 0.109 |
| simulation-campaign-v15.csv | Supreme court with cross-checking constitutional court | 0.663 | 0.646 | 0.639 | 0.115 | 0.593 | 0.327 | 0.000 |
| simulation-campaign-v15.csv | Dual supreme courts with disagreement filter | 0.645 | 0.599 | 0.698 | 0.117 | 0.605 | 0.351 | 0.000 |
| simulation-campaign-v20.csv | 60 percent invalidation threshold | 0.716 | 0.645 | 0.668 | 0.118 | 0.551 | 0.355 | 0.000 |
| simulation-campaign-v20.csv | No emergency relief without merits review | 0.716 | 0.647 | 0.679 | 0.006 | 0.538 | 0.313 | 0.000 |
| simulation-campaign-v20.csv | 18-year staggered terms + regular appointments | 0.713 | 0.615 | 0.700 | 0.135 | 0.554 | 0.358 | 0.000 |
| simulation-campaign-v20.csv | Nonpartisan commission appointments | 0.708 | 0.624 | 0.698 | 0.134 | 0.551 | 0.329 | 0.000 |
| simulation-campaign-v20.csv | Retention-election accountability court | 0.706 | 0.633 | 0.676 | 0.131 | 0.568 | 0.335 | 0.157 |
| simulation-campaign-v20.csv | Three-judge panels with en banc correction | 0.704 | 0.628 | 0.692 | 0.136 | 0.551 | 0.332 | 0.000 |
| simulation-campaign-v20.csv | Judicial review with legislative supermajority override | 0.703 | 0.608 | 0.711 | 0.132 | 0.582 | 0.355 | 0.184 |
| simulation-campaign-v20.csv | Peer recusal + reasoned emergency docket | 0.702 | 0.627 | 0.695 | 0.131 | 0.551 | 0.347 | 0.000 |
| simulation-campaign-v20.csv | Expanded 15-seat court | 0.701 | 0.623 | 0.695 | 0.136 | 0.552 | 0.353 | 0.000 |
| simulation-campaign-v20.csv | Stylized current U.S.-like supreme court | 0.694 | 0.618 | 0.696 | 0.479 | 0.578 | 0.395 | 0.000 |
| simulation-campaign-v20.csv | Pre-enactment constitutional council | 0.678 | 0.652 | 0.677 | 0.132 | 0.568 | 0.347 | 0.138 |
| simulation-campaign-v20.csv | Supreme court with cross-checking constitutional court | 0.660 | 0.634 | 0.640 | 0.120 | 0.599 | 0.338 | 0.000 |
| simulation-campaign-v20.csv | Dual supreme courts with disagreement filter | 0.639 | 0.571 | 0.705 | 0.123 | 0.617 | 0.358 | 0.000 |
| simulation-campaign-v21-paper.csv | 18-year staggered terms + regular appointments | 0.734 | 0.672 | 0.672 | 0.106 | 0.524 | 0.333 | 0.000 |
| simulation-campaign-v21-paper.csv | 60 percent invalidation threshold | 0.733 | 0.678 | 0.650 | 0.089 | 0.525 | 0.339 | 0.000 |
| simulation-campaign-v21-paper.csv | No emergency relief without merits review | 0.731 | 0.687 | 0.645 | 0.003 | 0.510 | 0.280 | 0.000 |
| simulation-campaign-v21-paper.csv | Nonpartisan commission appointments | 0.726 | 0.673 | 0.666 | 0.110 | 0.523 | 0.306 | 0.000 |
| simulation-campaign-v21-paper.csv | Judicial review with legislative supermajority override | 0.724 | 0.668 | 0.672 | 0.110 | 0.541 | 0.322 | 0.110 |
| simulation-campaign-v21-paper.csv | Three-judge panels with en banc correction | 0.723 | 0.673 | 0.671 | 0.113 | 0.524 | 0.309 | 0.000 |
| simulation-campaign-v21-paper.csv | Retention-election accountability court | 0.723 | 0.674 | 0.646 | 0.109 | 0.533 | 0.310 | 0.102 |
| simulation-campaign-v21-paper.csv | Peer recusal + reasoned emergency docket | 0.720 | 0.674 | 0.671 | 0.109 | 0.523 | 0.331 | 0.000 |
| simulation-campaign-v21-paper.csv | Expanded 15-seat court | 0.719 | 0.672 | 0.673 | 0.110 | 0.524 | 0.328 | 0.000 |
| simulation-campaign-v21-paper.csv | Stylized current U.S.-like supreme court | 0.714 | 0.656 | 0.668 | 0.418 | 0.545 | 0.366 | 0.000 |
| simulation-campaign-v21-paper.csv | Pre-enactment constitutional council | 0.698 | 0.690 | 0.649 | 0.106 | 0.533 | 0.314 | 0.093 |
| simulation-campaign-v21-paper.csv | Supreme court with cross-checking constitutional court | 0.679 | 0.664 | 0.629 | 0.088 | 0.570 | 0.311 | 0.000 |
| simulation-campaign-v21-paper.csv | Dual supreme courts with disagreement filter | 0.663 | 0.614 | 0.693 | 0.088 | 0.584 | 0.326 | 0.000 |
| simulation-campaign-v5.csv | No emergency relief without merits review | 0.719 | 0.634 | 0.681 | 0.005 | 0.546 | 0.316 | 0.000 |
| simulation-campaign-v5.csv | 60 percent invalidation threshold | 0.718 | 0.636 | 0.667 | 0.104 | 0.556 | 0.355 | 0.000 |
| simulation-campaign-v5.csv | 18-year staggered terms + regular appointments | 0.717 | 0.607 | 0.699 | 0.126 | 0.558 | 0.353 | 0.000 |
| simulation-campaign-v5.csv | Nonpartisan commission appointments | 0.712 | 0.601 | 0.708 | 0.118 | 0.560 | 0.336 | 0.000 |
| simulation-campaign-v5.csv | Retention-election accountability court | 0.709 | 0.614 | 0.672 | 0.122 | 0.582 | 0.333 | 0.186 |
| simulation-campaign-v5.csv | Three-judge panels with en banc correction | 0.707 | 0.618 | 0.687 | 0.123 | 0.556 | 0.330 | 0.000 |
| simulation-campaign-v5.csv | Judicial review with legislative supermajority override | 0.706 | 0.597 | 0.709 | 0.122 | 0.591 | 0.362 | 0.189 |
| simulation-campaign-v5.csv | Peer recusal + reasoned emergency docket | 0.706 | 0.617 | 0.692 | 0.123 | 0.557 | 0.349 | 0.000 |
| simulation-campaign-v5.csv | Expanded 15-seat court | 0.706 | 0.618 | 0.696 | 0.122 | 0.557 | 0.350 | 0.000 |
| simulation-campaign-v5.csv | Stylized current U.S.-like supreme court | 0.699 | 0.612 | 0.691 | 0.457 | 0.581 | 0.392 | 0.000 |
| simulation-campaign-v5.csv | Pre-enactment constitutional council | 0.679 | 0.637 | 0.678 | 0.118 | 0.582 | 0.359 | 0.174 |
| simulation-campaign-v5.csv | Supreme court with cross-checking constitutional court | 0.664 | 0.624 | 0.634 | 0.107 | 0.606 | 0.336 | 0.000 |
| simulation-campaign-v5.csv | Dual supreme courts with disagreement filter | 0.646 | 0.556 | 0.705 | 0.109 | 0.618 | 0.356 | 0.000 |
| simulation-manipulation-stress.csv | 18-year staggered terms + regular appointments | 0.731 | 0.646 | 0.677 | 0.105 | 0.533 | 0.334 | 0.000 |
| simulation-manipulation-stress.csv | 60 percent invalidation threshold | 0.730 | 0.658 | 0.642 | 0.092 | 0.533 | 0.341 | 0.000 |
| simulation-manipulation-stress.csv | No emergency relief without merits review | 0.729 | 0.664 | 0.655 | 0.003 | 0.522 | 0.299 | 0.000 |
| simulation-manipulation-stress.csv | Nonpartisan commission appointments | 0.726 | 0.643 | 0.676 | 0.102 | 0.533 | 0.309 | 0.000 |
| simulation-manipulation-stress.csv | Three-judge panels with en banc correction | 0.723 | 0.650 | 0.669 | 0.104 | 0.532 | 0.302 | 0.000 |
| simulation-manipulation-stress.csv | Retention-election accountability court | 0.723 | 0.653 | 0.648 | 0.107 | 0.550 | 0.321 | 0.149 |
| simulation-manipulation-stress.csv | Judicial review with legislative supermajority override | 0.719 | 0.635 | 0.686 | 0.108 | 0.564 | 0.342 | 0.170 |
| simulation-manipulation-stress.csv | Expanded 15-seat court | 0.719 | 0.646 | 0.679 | 0.103 | 0.533 | 0.327 | 0.000 |
| simulation-manipulation-stress.csv | Peer recusal + reasoned emergency docket | 0.718 | 0.647 | 0.675 | 0.106 | 0.533 | 0.336 | 0.000 |
| simulation-manipulation-stress.csv | Stylized current U.S.-like supreme court | 0.712 | 0.635 | 0.667 | 0.420 | 0.554 | 0.367 | 0.000 |
| simulation-manipulation-stress.csv | Pre-enactment constitutional council | 0.693 | 0.668 | 0.652 | 0.103 | 0.546 | 0.330 | 0.118 |
| simulation-manipulation-stress.csv | Supreme court with cross-checking constitutional court | 0.678 | 0.649 | 0.625 | 0.087 | 0.577 | 0.323 | 0.000 |
| simulation-manipulation-stress.csv | Dual supreme courts with disagreement filter | 0.661 | 0.585 | 0.696 | 0.089 | 0.591 | 0.332 | 0.000 |
