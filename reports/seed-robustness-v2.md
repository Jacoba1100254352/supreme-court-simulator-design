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
| No emergency relief without merits review | 0.699 | 0.699-0.700 | 0.000 | 0.578 | 0.680 | 0.011 | 0.582 | 0.414 | 0.376 |
| 60 percent invalidation threshold | 0.697 | 0.696-0.697 | 0.000 | 0.609 | 0.651 | 0.147 | 0.590 | 0.412 | 0.318 |
| 18-year staggered terms + regular appointments | 0.696 | 0.696-0.697 | 0.000 | 0.580 | 0.684 | 0.157 | 0.591 | 0.411 | 0.322 |
| Nonpartisan commission appointments | 0.691 | 0.691-0.691 | 0.000 | 0.583 | 0.681 | 0.157 | 0.590 | 0.411 | 0.352 |
| Retention-election accountability court | 0.687 | 0.687-0.687 | 0.000 | 0.584 | 0.653 | 0.156 | 0.618 | 0.396 | 0.352 |
| Three-judge panels with en banc correction | 0.686 | 0.686-0.687 | 0.000 | 0.588 | 0.677 | 0.159 | 0.589 | 0.412 | 0.369 |
| Judicial review with legislative supermajority override | 0.684 | 0.684-0.685 | 0.000 | 0.570 | 0.690 | 0.157 | 0.628 | 0.390 | 0.362 |
| Expanded 15-seat court | 0.683 | 0.683-0.684 | 0.000 | 0.581 | 0.683 | 0.158 | 0.591 | 0.411 | 0.372 |
| Peer recusal + reasoned emergency docket | 0.683 | 0.683-0.684 | 0.000 | 0.582 | 0.681 | 0.157 | 0.591 | 0.411 | 0.362 |
| Stylized current U.S.-like supreme court | 0.676 | 0.675-0.676 | 0.000 | 0.579 | 0.696 | 0.537 | 0.624 | 0.399 | 0.255 |
| Pre-enactment constitutional council | 0.656 | 0.656-0.656 | 0.000 | 0.600 | 0.669 | 0.155 | 0.619 | 0.425 | 0.470 |
| Supreme court with cross-checking constitutional court | 0.644 | 0.644-0.644 | 0.000 | 0.610 | 0.612 | 0.147 | 0.638 | 0.370 | 0.479 |
| Dual supreme courts with disagreement filter | 0.624 | 0.623-0.624 | 0.000 | 0.536 | 0.688 | 0.148 | 0.654 | 0.365 | 0.529 |
