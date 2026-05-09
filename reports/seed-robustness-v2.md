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
| 60 percent invalidation threshold | 0.568 | 0.568-0.568 | 0.000 | 0.609 | 0.616 | 0.101 | 0.474 | 0.471 | 0.192 |
| No emergency relief without merits review | 0.567 | 0.566-0.567 | 0.000 | 0.578 | 0.637 | 0.023 | 0.473 | 0.472 | 0.236 |
| Constitutional remand before invalidation | 0.565 | 0.565-0.566 | 0.000 | 0.628 | 0.623 | 0.110 | 0.475 | 0.491 | 0.311 |
| 18-year staggered terms + regular appointments | 0.565 | 0.565-0.565 | 0.000 | 0.594 | 0.625 | 0.108 | 0.475 | 0.470 | 0.197 |
| Public-interest litigation filter | 0.563 | 0.562-0.564 | 0.000 | 0.598 | 0.631 | 0.109 | 0.474 | 0.470 | 0.244 |
| Jurisdiction stripping constrained by rights carveouts | 0.562 | 0.562-0.563 | 0.000 | 0.589 | 0.626 | 0.109 | 0.490 | 0.460 | 0.220 |
| Constitutional remand with override window | 0.562 | 0.561-0.563 | 0.000 | 0.633 | 0.619 | 0.078 | 0.476 | 0.491 | 0.342 |
| Nonpartisan commission appointments | 0.562 | 0.561-0.562 | 0.000 | 0.593 | 0.626 | 0.110 | 0.477 | 0.469 | 0.220 |
| Mandatory written emergency reasoning | 0.561 | 0.561-0.562 | 0.001 | 0.601 | 0.620 | 0.078 | 0.476 | 0.470 | 0.234 |
| Automatic merits follow-up for emergency relief | 0.561 | 0.561-0.562 | 0.000 | 0.571 | 0.636 | 0.031 | 0.475 | 0.471 | 0.251 |
| Peer recusal + reasoned emergency docket | 0.561 | 0.560-0.562 | 0.001 | 0.594 | 0.625 | 0.109 | 0.475 | 0.471 | 0.225 |
| Emergency integrity package | 0.560 | 0.560-0.561 | 0.000 | 0.577 | 0.637 | 0.031 | 0.474 | 0.472 | 0.274 |
| Retention-election accountability court | 0.560 | 0.560-0.561 | 0.000 | 0.595 | 0.616 | 0.109 | 0.492 | 0.461 | 0.220 |
| Three-judge panels with en banc correction | 0.560 | 0.560-0.561 | 0.001 | 0.595 | 0.626 | 0.110 | 0.476 | 0.470 | 0.236 |
| Randomized merits panels with en banc correction | 0.559 | 0.559-0.560 | 0.000 | 0.595 | 0.627 | 0.110 | 0.476 | 0.470 | 0.243 |
| Expanded 15-seat court | 0.559 | 0.558-0.560 | 0.001 | 0.595 | 0.625 | 0.108 | 0.475 | 0.471 | 0.232 |
| Independent recusal enforcement with substitutes | 0.559 | 0.558-0.560 | 0.001 | 0.593 | 0.626 | 0.109 | 0.477 | 0.469 | 0.241 |
| Comparative 16-seat constitutional senates | 0.558 | 0.558-0.559 | 0.000 | 0.614 | 0.616 | 0.100 | 0.474 | 0.471 | 0.266 |
| Time-limited legislative override window | 0.558 | 0.557-0.560 | 0.001 | 0.590 | 0.626 | 0.109 | 0.496 | 0.459 | 0.226 |
| Judicial review with legislative supermajority override | 0.558 | 0.558-0.559 | 0.000 | 0.588 | 0.628 | 0.109 | 0.496 | 0.457 | 0.226 |
| Random panels with jurisdiction safeguards | 0.557 | 0.556-0.557 | 0.000 | 0.603 | 0.616 | 0.101 | 0.487 | 0.462 | 0.267 |
| Pre-enactment constitutional council | 0.555 | 0.555-0.556 | 0.000 | 0.601 | 0.628 | 0.109 | 0.494 | 0.481 | 0.302 |
| Constitutional council with concrete-review backstop | 0.555 | 0.555-0.556 | 0.000 | 0.607 | 0.628 | 0.108 | 0.490 | 0.483 | 0.315 |
| Stylized current U.S.-like supreme court | 0.551 | 0.550-0.552 | 0.000 | 0.587 | 0.637 | 0.313 | 0.514 | 0.450 | 0.156 |
| Supreme court with cross-checking constitutional court | 0.549 | 0.548-0.549 | 0.000 | 0.612 | 0.599 | 0.100 | 0.496 | 0.455 | 0.303 |
| Dual supreme courts with disagreement filter | 0.532 | 0.531-0.533 | 0.001 | 0.568 | 0.624 | 0.102 | 0.509 | 0.446 | 0.340 |
