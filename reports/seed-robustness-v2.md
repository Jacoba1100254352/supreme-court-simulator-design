# Seed Robustness v2

Weighted v2 campaign averages rerun across deterministic seed offsets.

## Run Configuration

- runs per case per seed: 40
- cases per run: 48
- experiment cases: 20
- seeds: [20260501, 20260502, 20260503, 20260504, 20260505]
- legislative input: simulation-campaign-v21-paper.csv

## Scenario Robustness

| Scenario | Directional mean | Directional range | Std. dev. | Legal stability | Rights | Shadow abuse | Conflict | Compliance | Admin cost |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.745 | 0.745-0.745 | 0.000 | 0.670 | 0.685 | 0.087 | 0.457 | 0.504 | 0.296 |
| 18-year staggered terms + regular appointments | 0.742 | 0.742-0.743 | 0.000 | 0.658 | 0.699 | 0.106 | 0.458 | 0.504 | 0.300 |
| No emergency relief without merits review | 0.740 | 0.739-0.740 | 0.000 | 0.672 | 0.691 | 0.009 | 0.449 | 0.506 | 0.354 |
| Nonpartisan commission appointments | 0.735 | 0.735-0.736 | 0.000 | 0.662 | 0.698 | 0.107 | 0.457 | 0.504 | 0.330 |
| Retention-election accountability court | 0.734 | 0.733-0.734 | 0.000 | 0.663 | 0.684 | 0.106 | 0.472 | 0.495 | 0.330 |
| Three-judge panels with en banc correction | 0.732 | 0.732-0.733 | 0.000 | 0.663 | 0.696 | 0.107 | 0.457 | 0.504 | 0.345 |
| Judicial review with legislative supermajority override | 0.731 | 0.731-0.731 | 0.000 | 0.654 | 0.703 | 0.106 | 0.477 | 0.492 | 0.340 |
| Stylized current U.S.-like supreme court | 0.731 | 0.730-0.731 | 0.000 | 0.654 | 0.705 | 0.368 | 0.476 | 0.497 | 0.243 |
| Peer recusal + reasoned emergency docket | 0.729 | 0.729-0.730 | 0.000 | 0.660 | 0.698 | 0.106 | 0.457 | 0.504 | 0.340 |
| Expanded 15-seat court | 0.729 | 0.729-0.730 | 0.000 | 0.660 | 0.699 | 0.107 | 0.457 | 0.504 | 0.350 |
| Pre-enactment constitutional council | 0.710 | 0.710-0.710 | 0.000 | 0.673 | 0.691 | 0.106 | 0.471 | 0.513 | 0.421 |
| Supreme court with cross-checking constitutional court | 0.693 | 0.693-0.693 | 0.000 | 0.663 | 0.666 | 0.087 | 0.498 | 0.470 | 0.450 |
| Dual supreme courts with disagreement filter | 0.675 | 0.674-0.675 | 0.000 | 0.627 | 0.702 | 0.088 | 0.506 | 0.467 | 0.500 |
