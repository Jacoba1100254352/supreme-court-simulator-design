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
| No emergency relief without merits review | 0.584 | 0.584-0.585 | 0.001 | 0.616 | 0.614 | 0.010 | 0.489 | 0.464 | 0.301 |
| 18-year staggered terms + regular appointments | 0.583 | 0.582-0.585 | 0.001 | 0.627 | 0.600 | 0.125 | 0.486 | 0.467 | 0.250 |
| Stylized current U.S.-like supreme court | 0.578 | 0.577-0.579 | 0.001 | 0.619 | 0.620 | 0.423 | 0.515 | 0.457 | 0.198 |
| Nonpartisan commission appointments | 0.576 | 0.576-0.577 | 0.001 | 0.626 | 0.605 | 0.128 | 0.493 | 0.463 | 0.281 |
| Peer recusal + reasoned emergency docket | 0.576 | 0.575-0.577 | 0.000 | 0.627 | 0.601 | 0.125 | 0.487 | 0.467 | 0.284 |
| Expanded 15-seat court | 0.576 | 0.575-0.576 | 0.000 | 0.627 | 0.601 | 0.126 | 0.487 | 0.467 | 0.292 |
| Three-judge panels with en banc correction | 0.572 | 0.571-0.573 | 0.001 | 0.629 | 0.602 | 0.130 | 0.493 | 0.462 | 0.298 |
| Judicial review with legislative supermajority override | 0.572 | 0.572-0.572 | 0.000 | 0.619 | 0.608 | 0.129 | 0.514 | 0.451 | 0.289 |
| Retention-election accountability court | 0.572 | 0.572-0.572 | 0.000 | 0.626 | 0.590 | 0.127 | 0.510 | 0.454 | 0.281 |
| 60 percent invalidation threshold | 0.570 | 0.569-0.571 | 0.000 | 0.648 | 0.574 | 0.124 | 0.486 | 0.467 | 0.248 |
| Pre-enactment constitutional council | 0.558 | 0.557-0.560 | 0.001 | 0.638 | 0.597 | 0.127 | 0.509 | 0.475 | 0.375 |
| Comparative 16-seat constitutional senates | 0.554 | 0.554-0.555 | 0.001 | 0.652 | 0.566 | 0.124 | 0.485 | 0.467 | 0.330 |
| Dual supreme courts with disagreement filter | 0.537 | 0.536-0.537 | 0.000 | 0.588 | 0.609 | 0.127 | 0.542 | 0.428 | 0.426 |
| Supreme court with cross-checking constitutional court | 0.529 | 0.528-0.530 | 0.001 | 0.634 | 0.562 | 0.125 | 0.532 | 0.431 | 0.384 |
