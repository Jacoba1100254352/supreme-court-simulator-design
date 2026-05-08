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
| 60 percent invalidation threshold | 0.569 | 0.569-0.569 | 0.000 | 0.610 | 0.615 | 0.099 | 0.466 | 0.474 | 0.191 |
| No emergency relief without merits review | 0.568 | 0.567-0.568 | 0.001 | 0.579 | 0.637 | 0.023 | 0.466 | 0.474 | 0.235 |
| Constitutional remand before invalidation | 0.566 | 0.566-0.566 | 0.000 | 0.629 | 0.623 | 0.108 | 0.469 | 0.493 | 0.311 |
| 18-year staggered terms + regular appointments | 0.566 | 0.565-0.567 | 0.001 | 0.595 | 0.625 | 0.107 | 0.468 | 0.473 | 0.196 |
| Public-interest litigation filter | 0.564 | 0.563-0.565 | 0.000 | 0.599 | 0.631 | 0.107 | 0.467 | 0.472 | 0.243 |
| Jurisdiction stripping constrained by rights carveouts | 0.563 | 0.563-0.564 | 0.000 | 0.590 | 0.625 | 0.107 | 0.483 | 0.462 | 0.218 |
| Constitutional remand with override window | 0.563 | 0.562-0.563 | 0.000 | 0.634 | 0.619 | 0.077 | 0.469 | 0.493 | 0.341 |
| Nonpartisan commission appointments | 0.563 | 0.562-0.563 | 0.000 | 0.594 | 0.625 | 0.108 | 0.470 | 0.472 | 0.219 |
| Mandatory written emergency reasoning | 0.562 | 0.562-0.563 | 0.000 | 0.602 | 0.620 | 0.077 | 0.469 | 0.472 | 0.233 |
| Peer recusal + reasoned emergency docket | 0.562 | 0.562-0.563 | 0.000 | 0.595 | 0.624 | 0.106 | 0.467 | 0.473 | 0.224 |
| Automatic merits follow-up for emergency relief | 0.562 | 0.561-0.562 | 0.000 | 0.572 | 0.636 | 0.030 | 0.468 | 0.474 | 0.250 |
| Three-judge panels with en banc correction | 0.561 | 0.561-0.562 | 0.001 | 0.596 | 0.626 | 0.108 | 0.469 | 0.472 | 0.235 |
| Retention-election accountability court | 0.561 | 0.560-0.562 | 0.001 | 0.596 | 0.616 | 0.107 | 0.486 | 0.463 | 0.219 |
| Emergency integrity package | 0.561 | 0.561-0.562 | 0.000 | 0.578 | 0.637 | 0.031 | 0.467 | 0.474 | 0.274 |
| Randomized merits panels with en banc correction | 0.560 | 0.560-0.561 | 0.000 | 0.596 | 0.626 | 0.108 | 0.468 | 0.473 | 0.242 |
| Expanded 15-seat court | 0.560 | 0.559-0.561 | 0.000 | 0.595 | 0.625 | 0.107 | 0.467 | 0.473 | 0.232 |
| Independent recusal enforcement with substitutes | 0.560 | 0.559-0.561 | 0.001 | 0.594 | 0.626 | 0.108 | 0.470 | 0.472 | 0.240 |
| Comparative 16-seat constitutional senates | 0.559 | 0.559-0.560 | 0.000 | 0.615 | 0.616 | 0.099 | 0.466 | 0.474 | 0.264 |
| Time-limited legislative override window | 0.559 | 0.558-0.561 | 0.001 | 0.590 | 0.626 | 0.107 | 0.490 | 0.461 | 0.226 |
| Judicial review with legislative supermajority override | 0.559 | 0.558-0.559 | 0.000 | 0.589 | 0.627 | 0.107 | 0.490 | 0.459 | 0.225 |
| Random panels with jurisdiction safeguards | 0.558 | 0.557-0.558 | 0.000 | 0.603 | 0.616 | 0.100 | 0.480 | 0.465 | 0.266 |
| Constitutional council with concrete-review backstop | 0.556 | 0.555-0.556 | 0.000 | 0.608 | 0.627 | 0.106 | 0.484 | 0.485 | 0.314 |
| Pre-enactment constitutional council | 0.556 | 0.555-0.556 | 0.000 | 0.602 | 0.627 | 0.107 | 0.488 | 0.483 | 0.300 |
| Stylized current U.S.-like supreme court | 0.556 | 0.555-0.556 | 0.000 | 0.591 | 0.637 | 0.302 | 0.495 | 0.460 | 0.155 |
| Supreme court with cross-checking constitutional court | 0.549 | 0.549-0.550 | 0.000 | 0.613 | 0.600 | 0.099 | 0.490 | 0.457 | 0.303 |
| Dual supreme courts with disagreement filter | 0.533 | 0.532-0.534 | 0.001 | 0.569 | 0.624 | 0.100 | 0.501 | 0.448 | 0.338 |
