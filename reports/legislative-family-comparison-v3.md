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
| simulation-campaign-v0.csv | 0.281 | 0.593 | 0.167 | 0.200 | 0.280 | 0.144 | 0.597 | 0.228 | 18-year staggered terms + regular appointments (0.608) |
| simulation-campaign-v5.csv | 0.429 | 0.554 | 0.239 | 0.200 | 0.280 | 0.262 | 0.562 | 0.285 | 18-year staggered terms + regular appointments (0.599) |
| simulation-campaign-v10.csv | 0.518 | 0.582 | 0.268 | 0.200 | 0.227 | 0.326 | 0.565 | 0.307 | 18-year staggered terms + regular appointments (0.600) |
| simulation-campaign-v15.csv | 0.500 | 0.594 | 0.255 | 0.110 | 0.230 | 0.323 | 0.513 | 0.293 | 18-year staggered terms + regular appointments (0.599) |
| simulation-campaign-v20.csv | 0.584 | 0.564 | 0.251 | 0.116 | 0.246 | 0.334 | 0.494 | 0.302 | 18-year staggered terms + regular appointments (0.603) |
| simulation-campaign-v21-paper.csv | 0.343 | 0.610 | 0.175 | 0.104 | 0.237 | 0.120 | 0.547 | 0.213 | 18-year staggered terms + regular appointments (0.609) |
| simulation-manipulation-stress.csv | 0.283 | 0.582 | 0.102 | 0.163 | 0.274 | 0.097 | 0.552 | 0.202 | 18-year staggered terms + regular appointments (0.607) |

## Scenario Sensitivity By Family

| Family | Scenario | Directional | Legal | Rights | Shadow | Conflict | Strategic | Override att. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| simulation-campaign-v0.csv | 18-year staggered terms + regular appointments | 0.608 | 0.670 | 0.582 | 0.081 | 0.421 | 0.212 | 0.000 |
| simulation-campaign-v0.csv | Expanded 15-seat court | 0.603 | 0.664 | 0.593 | 0.080 | 0.427 | 0.210 | 0.000 |
| simulation-campaign-v0.csv | Nonpartisan commission appointments | 0.601 | 0.669 | 0.584 | 0.089 | 0.426 | 0.201 | 0.000 |
| simulation-campaign-v0.csv | Peer recusal + reasoned emergency docket | 0.600 | 0.671 | 0.585 | 0.084 | 0.423 | 0.211 | 0.000 |
| simulation-campaign-v0.csv | Three-judge panels with en banc correction | 0.599 | 0.666 | 0.591 | 0.088 | 0.432 | 0.203 | 0.000 |
| simulation-campaign-v0.csv | 60 percent invalidation threshold | 0.598 | 0.679 | 0.561 | 0.076 | 0.421 | 0.214 | 0.000 |
| simulation-campaign-v0.csv | No emergency relief without merits review | 0.597 | 0.682 | 0.574 | 0.004 | 0.421 | 0.192 | 0.000 |
| simulation-campaign-v0.csv | Judicial review with legislative supermajority override | 0.596 | 0.669 | 0.582 | 0.088 | 0.438 | 0.204 | 0.079 |
| simulation-campaign-v0.csv | Retention-election accountability court | 0.595 | 0.673 | 0.575 | 0.086 | 0.440 | 0.201 | 0.068 |
| simulation-campaign-v0.csv | Stylized current U.S.-like supreme court | 0.595 | 0.657 | 0.585 | 0.322 | 0.442 | 0.241 | 0.000 |
| simulation-campaign-v0.csv | Comparative 16-seat constitutional senates | 0.583 | 0.683 | 0.552 | 0.079 | 0.418 | 0.200 | 0.000 |
| simulation-campaign-v0.csv | Pre-enactment constitutional council | 0.581 | 0.682 | 0.577 | 0.087 | 0.442 | 0.205 | 0.064 |
| simulation-campaign-v0.csv | Dual supreme courts with disagreement filter | 0.567 | 0.634 | 0.596 | 0.081 | 0.474 | 0.220 | 0.000 |
| simulation-campaign-v0.csv | Supreme court with cross-checking constitutional court | 0.562 | 0.661 | 0.561 | 0.081 | 0.462 | 0.212 | 0.000 |
| simulation-campaign-v10.csv | 18-year staggered terms + regular appointments | 0.600 | 0.661 | 0.598 | 0.097 | 0.437 | 0.217 | 0.000 |
| simulation-campaign-v10.csv | Peer recusal + reasoned emergency docket | 0.596 | 0.657 | 0.605 | 0.096 | 0.437 | 0.220 | 0.000 |
| simulation-campaign-v10.csv | No emergency relief without merits review | 0.596 | 0.668 | 0.589 | 0.005 | 0.429 | 0.191 | 0.000 |
| simulation-campaign-v10.csv | Expanded 15-seat court | 0.596 | 0.664 | 0.593 | 0.096 | 0.430 | 0.215 | 0.000 |
| simulation-campaign-v10.csv | 60 percent invalidation threshold | 0.595 | 0.670 | 0.573 | 0.093 | 0.430 | 0.218 | 0.000 |
| simulation-campaign-v10.csv | Stylized current U.S.-like supreme court | 0.592 | 0.649 | 0.596 | 0.351 | 0.450 | 0.247 | 0.000 |
| simulation-campaign-v10.csv | Three-judge panels with en banc correction | 0.591 | 0.667 | 0.593 | 0.101 | 0.440 | 0.205 | 0.000 |
| simulation-campaign-v10.csv | Nonpartisan commission appointments | 0.591 | 0.662 | 0.597 | 0.103 | 0.441 | 0.210 | 0.000 |
| simulation-campaign-v10.csv | Retention-election accountability court | 0.589 | 0.664 | 0.585 | 0.100 | 0.451 | 0.209 | 0.082 |
| simulation-campaign-v10.csv | Judicial review with legislative supermajority override | 0.589 | 0.659 | 0.602 | 0.104 | 0.455 | 0.217 | 0.088 |
| simulation-campaign-v10.csv | Pre-enactment constitutional council | 0.577 | 0.673 | 0.584 | 0.095 | 0.443 | 0.208 | 0.063 |
| simulation-campaign-v10.csv | Comparative 16-seat constitutional senates | 0.576 | 0.672 | 0.568 | 0.092 | 0.431 | 0.210 | 0.000 |
| simulation-campaign-v10.csv | Dual supreme courts with disagreement filter | 0.558 | 0.623 | 0.608 | 0.097 | 0.485 | 0.224 | 0.000 |
| simulation-campaign-v10.csv | Supreme court with cross-checking constitutional court | 0.549 | 0.656 | 0.567 | 0.097 | 0.480 | 0.216 | 0.000 |
| simulation-campaign-v15.csv | 18-year staggered terms + regular appointments | 0.599 | 0.671 | 0.600 | 0.099 | 0.429 | 0.217 | 0.000 |
| simulation-campaign-v15.csv | Expanded 15-seat court | 0.593 | 0.670 | 0.608 | 0.096 | 0.430 | 0.217 | 0.000 |
| simulation-campaign-v15.csv | 60 percent invalidation threshold | 0.592 | 0.675 | 0.592 | 0.092 | 0.433 | 0.218 | 0.000 |
| simulation-campaign-v15.csv | Nonpartisan commission appointments | 0.592 | 0.669 | 0.613 | 0.102 | 0.439 | 0.205 | 0.000 |
| simulation-campaign-v15.csv | Peer recusal + reasoned emergency docket | 0.592 | 0.670 | 0.602 | 0.097 | 0.429 | 0.218 | 0.000 |
| simulation-campaign-v15.csv | Judicial review with legislative supermajority override | 0.592 | 0.667 | 0.608 | 0.099 | 0.446 | 0.209 | 0.071 |
| simulation-campaign-v15.csv | Retention-election accountability court | 0.591 | 0.672 | 0.596 | 0.099 | 0.440 | 0.202 | 0.053 |
| simulation-campaign-v15.csv | Three-judge panels with en banc correction | 0.590 | 0.671 | 0.603 | 0.102 | 0.431 | 0.206 | 0.000 |
| simulation-campaign-v15.csv | Stylized current U.S.-like supreme court | 0.590 | 0.656 | 0.610 | 0.351 | 0.450 | 0.251 | 0.000 |
| simulation-campaign-v15.csv | No emergency relief without merits review | 0.590 | 0.679 | 0.603 | 0.005 | 0.432 | 0.194 | 0.000 |
| simulation-campaign-v15.csv | Pre-enactment constitutional council | 0.578 | 0.679 | 0.599 | 0.102 | 0.443 | 0.207 | 0.057 |
| simulation-campaign-v15.csv | Comparative 16-seat constitutional senates | 0.577 | 0.680 | 0.579 | 0.093 | 0.427 | 0.202 | 0.000 |
| simulation-campaign-v15.csv | Dual supreme courts with disagreement filter | 0.555 | 0.633 | 0.615 | 0.097 | 0.482 | 0.222 | 0.000 |
| simulation-campaign-v15.csv | Supreme court with cross-checking constitutional court | 0.555 | 0.660 | 0.584 | 0.090 | 0.474 | 0.216 | 0.000 |
| simulation-campaign-v20.csv | 18-year staggered terms + regular appointments | 0.603 | 0.657 | 0.610 | 0.098 | 0.435 | 0.219 | 0.000 |
| simulation-campaign-v20.csv | Nonpartisan commission appointments | 0.597 | 0.654 | 0.619 | 0.103 | 0.441 | 0.209 | 0.000 |
| simulation-campaign-v20.csv | Expanded 15-seat court | 0.596 | 0.660 | 0.609 | 0.099 | 0.430 | 0.222 | 0.000 |
| simulation-campaign-v20.csv | No emergency relief without merits review | 0.596 | 0.666 | 0.610 | 0.005 | 0.435 | 0.199 | 0.000 |
| simulation-campaign-v20.csv | Peer recusal + reasoned emergency docket | 0.593 | 0.659 | 0.615 | 0.104 | 0.440 | 0.225 | 0.000 |
| simulation-campaign-v20.csv | Stylized current U.S.-like supreme court | 0.593 | 0.649 | 0.613 | 0.349 | 0.455 | 0.249 | 0.000 |
| simulation-campaign-v20.csv | 60 percent invalidation threshold | 0.591 | 0.670 | 0.590 | 0.093 | 0.437 | 0.219 | 0.000 |
| simulation-campaign-v20.csv | Three-judge panels with en banc correction | 0.590 | 0.664 | 0.607 | 0.102 | 0.441 | 0.207 | 0.000 |
| simulation-campaign-v20.csv | Judicial review with legislative supermajority override | 0.589 | 0.656 | 0.607 | 0.106 | 0.454 | 0.217 | 0.086 |
| simulation-campaign-v20.csv | Retention-election accountability court | 0.588 | 0.661 | 0.601 | 0.105 | 0.455 | 0.212 | 0.073 |
| simulation-campaign-v20.csv | Pre-enactment constitutional council | 0.576 | 0.668 | 0.610 | 0.107 | 0.456 | 0.214 | 0.067 |
| simulation-campaign-v20.csv | Comparative 16-seat constitutional senates | 0.575 | 0.672 | 0.582 | 0.094 | 0.434 | 0.207 | 0.000 |
| simulation-campaign-v20.csv | Dual supreme courts with disagreement filter | 0.555 | 0.623 | 0.619 | 0.099 | 0.489 | 0.231 | 0.000 |
| simulation-campaign-v20.csv | Supreme court with cross-checking constitutional court | 0.549 | 0.655 | 0.585 | 0.097 | 0.484 | 0.220 | 0.000 |
| simulation-campaign-v21-paper.csv | 18-year staggered terms + regular appointments | 0.609 | 0.681 | 0.595 | 0.081 | 0.408 | 0.204 | 0.000 |
| simulation-campaign-v21-paper.csv | No emergency relief without merits review | 0.602 | 0.692 | 0.594 | 0.003 | 0.407 | 0.179 | 0.000 |
| simulation-campaign-v21-paper.csv | Nonpartisan commission appointments | 0.601 | 0.686 | 0.594 | 0.082 | 0.410 | 0.196 | 0.000 |
| simulation-campaign-v21-paper.csv | Stylized current U.S.-like supreme court | 0.600 | 0.672 | 0.599 | 0.305 | 0.424 | 0.225 | 0.000 |
| simulation-campaign-v21-paper.csv | Peer recusal + reasoned emergency docket | 0.600 | 0.687 | 0.591 | 0.082 | 0.406 | 0.199 | 0.000 |
| simulation-campaign-v21-paper.csv | 60 percent invalidation threshold | 0.599 | 0.689 | 0.578 | 0.074 | 0.408 | 0.210 | 0.000 |
| simulation-campaign-v21-paper.csv | Three-judge panels with en banc correction | 0.599 | 0.683 | 0.599 | 0.085 | 0.414 | 0.195 | 0.000 |
| simulation-campaign-v21-paper.csv | Expanded 15-seat court | 0.598 | 0.682 | 0.599 | 0.087 | 0.411 | 0.208 | 0.000 |
| simulation-campaign-v21-paper.csv | Judicial review with legislative supermajority override | 0.598 | 0.681 | 0.602 | 0.085 | 0.427 | 0.199 | 0.061 |
| simulation-campaign-v21-paper.csv | Retention-election accountability court | 0.597 | 0.685 | 0.585 | 0.085 | 0.417 | 0.193 | 0.046 |
| simulation-campaign-v21-paper.csv | Comparative 16-seat constitutional senates | 0.585 | 0.690 | 0.574 | 0.076 | 0.409 | 0.192 | 0.000 |
| simulation-campaign-v21-paper.csv | Pre-enactment constitutional council | 0.585 | 0.692 | 0.592 | 0.080 | 0.422 | 0.191 | 0.046 |
| simulation-campaign-v21-paper.csv | Dual supreme courts with disagreement filter | 0.566 | 0.653 | 0.608 | 0.080 | 0.457 | 0.213 | 0.000 |
| simulation-campaign-v21-paper.csv | Supreme court with cross-checking constitutional court | 0.564 | 0.675 | 0.578 | 0.078 | 0.447 | 0.206 | 0.000 |
| simulation-campaign-v5.csv | 18-year staggered terms + regular appointments | 0.599 | 0.661 | 0.601 | 0.100 | 0.441 | 0.225 | 0.000 |
| simulation-campaign-v5.csv | Peer recusal + reasoned emergency docket | 0.596 | 0.658 | 0.602 | 0.099 | 0.437 | 0.219 | 0.000 |
| simulation-campaign-v5.csv | Nonpartisan commission appointments | 0.595 | 0.663 | 0.605 | 0.100 | 0.441 | 0.213 | 0.000 |
| simulation-campaign-v5.csv | Judicial review with legislative supermajority override | 0.593 | 0.655 | 0.609 | 0.104 | 0.456 | 0.223 | 0.085 |
| simulation-campaign-v5.csv | Expanded 15-seat court | 0.593 | 0.663 | 0.601 | 0.095 | 0.438 | 0.219 | 0.000 |
| simulation-campaign-v5.csv | No emergency relief without merits review | 0.593 | 0.668 | 0.600 | 0.005 | 0.439 | 0.202 | 0.000 |
| simulation-campaign-v5.csv | Three-judge panels with en banc correction | 0.592 | 0.663 | 0.598 | 0.098 | 0.440 | 0.211 | 0.000 |
| simulation-campaign-v5.csv | Stylized current U.S.-like supreme court | 0.592 | 0.653 | 0.605 | 0.356 | 0.457 | 0.244 | 0.000 |
| simulation-campaign-v5.csv | Retention-election accountability court | 0.589 | 0.664 | 0.593 | 0.102 | 0.455 | 0.207 | 0.071 |
| simulation-campaign-v5.csv | 60 percent invalidation threshold | 0.587 | 0.669 | 0.579 | 0.092 | 0.441 | 0.226 | 0.000 |
| simulation-campaign-v5.csv | Pre-enactment constitutional council | 0.579 | 0.671 | 0.593 | 0.099 | 0.450 | 0.210 | 0.063 |
| simulation-campaign-v5.csv | Comparative 16-seat constitutional senates | 0.572 | 0.676 | 0.573 | 0.098 | 0.442 | 0.213 | 0.000 |
| simulation-campaign-v5.csv | Dual supreme courts with disagreement filter | 0.558 | 0.625 | 0.614 | 0.095 | 0.491 | 0.227 | 0.000 |
| simulation-campaign-v5.csv | Supreme court with cross-checking constitutional court | 0.557 | 0.651 | 0.580 | 0.096 | 0.479 | 0.220 | 0.000 |
| simulation-manipulation-stress.csv | 18-year staggered terms + regular appointments | 0.607 | 0.676 | 0.579 | 0.079 | 0.412 | 0.206 | 0.000 |
| simulation-manipulation-stress.csv | Nonpartisan commission appointments | 0.604 | 0.675 | 0.586 | 0.082 | 0.417 | 0.198 | 0.000 |
| simulation-manipulation-stress.csv | No emergency relief without merits review | 0.600 | 0.689 | 0.570 | 0.003 | 0.408 | 0.179 | 0.000 |
| simulation-manipulation-stress.csv | Expanded 15-seat court | 0.600 | 0.677 | 0.582 | 0.081 | 0.414 | 0.208 | 0.000 |
| simulation-manipulation-stress.csv | Peer recusal + reasoned emergency docket | 0.597 | 0.679 | 0.580 | 0.084 | 0.416 | 0.212 | 0.000 |
| simulation-manipulation-stress.csv | Retention-election accountability court | 0.597 | 0.679 | 0.577 | 0.082 | 0.429 | 0.197 | 0.061 |
| simulation-manipulation-stress.csv | Three-judge panels with en banc correction | 0.597 | 0.678 | 0.589 | 0.083 | 0.425 | 0.197 | 0.000 |
| simulation-manipulation-stress.csv | 60 percent invalidation threshold | 0.596 | 0.682 | 0.565 | 0.076 | 0.419 | 0.213 | 0.000 |
| simulation-manipulation-stress.csv | Stylized current U.S.-like supreme court | 0.595 | 0.668 | 0.582 | 0.316 | 0.433 | 0.232 | 0.000 |
| simulation-manipulation-stress.csv | Judicial review with legislative supermajority override | 0.593 | 0.676 | 0.587 | 0.086 | 0.437 | 0.206 | 0.066 |
| simulation-manipulation-stress.csv | Pre-enactment constitutional council | 0.581 | 0.690 | 0.569 | 0.085 | 0.427 | 0.195 | 0.047 |
| simulation-manipulation-stress.csv | Comparative 16-seat constitutional senates | 0.579 | 0.686 | 0.557 | 0.079 | 0.419 | 0.199 | 0.000 |
| simulation-manipulation-stress.csv | Dual supreme courts with disagreement filter | 0.565 | 0.644 | 0.597 | 0.081 | 0.466 | 0.219 | 0.000 |
| simulation-manipulation-stress.csv | Supreme court with cross-checking constitutional court | 0.563 | 0.667 | 0.562 | 0.080 | 0.456 | 0.209 | 0.000 |
