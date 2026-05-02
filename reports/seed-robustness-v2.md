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
| 18-year staggered terms + regular appointments | 0.589 | 0.588-0.589 | 0.000 | 0.667 | 0.613 | 0.068 | 0.363 | 0.535 | 0.192 |
| No emergency relief without merits review | 0.586 | 0.586-0.587 | 0.000 | 0.669 | 0.618 | 0.004 | 0.365 | 0.534 | 0.235 |
| Stylized current U.S.-like supreme court | 0.585 | 0.585-0.586 | 0.000 | 0.662 | 0.618 | 0.235 | 0.376 | 0.531 | 0.154 |
| Nonpartisan commission appointments | 0.585 | 0.584-0.585 | 0.000 | 0.666 | 0.617 | 0.071 | 0.370 | 0.532 | 0.219 |
| 60 percent invalidation threshold | 0.584 | 0.584-0.584 | 0.000 | 0.673 | 0.603 | 0.061 | 0.364 | 0.535 | 0.188 |
| Peer recusal + reasoned emergency docket | 0.583 | 0.582-0.583 | 0.000 | 0.667 | 0.613 | 0.068 | 0.364 | 0.535 | 0.221 |
| Expanded 15-seat court | 0.582 | 0.581-0.583 | 0.000 | 0.666 | 0.614 | 0.068 | 0.363 | 0.535 | 0.228 |
| Retention-election accountability court | 0.582 | 0.582-0.583 | 0.000 | 0.666 | 0.609 | 0.070 | 0.378 | 0.528 | 0.219 |
| Judicial review with legislative supermajority override | 0.582 | 0.582-0.582 | 0.000 | 0.663 | 0.618 | 0.070 | 0.379 | 0.527 | 0.225 |
| Three-judge panels with en banc correction | 0.582 | 0.581-0.582 | 0.000 | 0.668 | 0.615 | 0.071 | 0.370 | 0.532 | 0.234 |
| Pre-enactment constitutional council | 0.572 | 0.571-0.572 | 0.000 | 0.673 | 0.613 | 0.069 | 0.378 | 0.540 | 0.287 |
| Comparative 16-seat constitutional senates | 0.571 | 0.571-0.572 | 0.000 | 0.677 | 0.598 | 0.061 | 0.361 | 0.536 | 0.260 |
| Dual supreme courts with disagreement filter | 0.553 | 0.553-0.554 | 0.000 | 0.642 | 0.620 | 0.063 | 0.403 | 0.508 | 0.340 |
| Supreme court with cross-checking constitutional court | 0.552 | 0.551-0.552 | 0.000 | 0.663 | 0.596 | 0.063 | 0.399 | 0.509 | 0.304 |
