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
| No emergency relief without merits review | 0.578 | 0.578-0.579 | 0.001 | 0.626 | 0.651 | 0.005 | 0.447 | 0.434 | 0.273 |
| 18-year staggered terms + regular appointments | 0.576 | 0.575-0.577 | 0.001 | 0.625 | 0.644 | 0.087 | 0.448 | 0.434 | 0.225 |
| 60 percent invalidation threshold | 0.576 | 0.575-0.576 | 0.000 | 0.634 | 0.631 | 0.077 | 0.449 | 0.433 | 0.221 |
| Jurisdiction stripping constrained by rights carveouts | 0.572 | 0.572-0.573 | 0.001 | 0.621 | 0.647 | 0.089 | 0.464 | 0.422 | 0.253 |
| Automatic merits follow-up for emergency relief | 0.572 | 0.571-0.572 | 0.000 | 0.615 | 0.655 | 0.011 | 0.448 | 0.435 | 0.288 |
| Nonpartisan commission appointments | 0.572 | 0.571-0.572 | 0.001 | 0.622 | 0.648 | 0.089 | 0.455 | 0.430 | 0.254 |
| Peer recusal + reasoned emergency docket | 0.571 | 0.570-0.571 | 0.000 | 0.624 | 0.644 | 0.087 | 0.449 | 0.433 | 0.258 |
| Mandatory written emergency reasoning | 0.571 | 0.570-0.571 | 0.000 | 0.628 | 0.641 | 0.050 | 0.451 | 0.433 | 0.269 |
| Retention-election accountability court | 0.570 | 0.569-0.570 | 0.000 | 0.625 | 0.637 | 0.089 | 0.467 | 0.423 | 0.254 |
| Three-judge panels with en banc correction | 0.569 | 0.569-0.570 | 0.000 | 0.625 | 0.646 | 0.090 | 0.455 | 0.429 | 0.271 |
| Expanded 15-seat court | 0.569 | 0.568-0.569 | 0.000 | 0.625 | 0.644 | 0.088 | 0.448 | 0.434 | 0.265 |
| Judicial review with legislative supermajority override | 0.568 | 0.568-0.569 | 0.000 | 0.619 | 0.650 | 0.089 | 0.470 | 0.420 | 0.261 |
| Independent recusal enforcement with substitutes | 0.568 | 0.568-0.569 | 0.001 | 0.623 | 0.648 | 0.090 | 0.456 | 0.429 | 0.279 |
| Time-limited legislative override window | 0.568 | 0.568-0.569 | 0.000 | 0.618 | 0.649 | 0.089 | 0.471 | 0.420 | 0.261 |
| Randomized merits panels with en banc correction | 0.568 | 0.567-0.568 | 0.000 | 0.625 | 0.646 | 0.090 | 0.455 | 0.429 | 0.278 |
| Public-interest litigation filter | 0.566 | 0.566-0.566 | 0.000 | 0.620 | 0.658 | 0.093 | 0.468 | 0.419 | 0.293 |
| Comparative 16-seat constitutional senates | 0.565 | 0.564-0.565 | 0.000 | 0.640 | 0.626 | 0.077 | 0.447 | 0.434 | 0.301 |
| Constitutional remand before invalidation | 0.564 | 0.564-0.564 | 0.000 | 0.643 | 0.645 | 0.092 | 0.469 | 0.438 | 0.362 |
| Pre-enactment constitutional council | 0.562 | 0.562-0.563 | 0.000 | 0.631 | 0.645 | 0.088 | 0.468 | 0.438 | 0.337 |
| Stylized current U.S.-like supreme court | 0.561 | 0.560-0.561 | 0.000 | 0.618 | 0.650 | 0.301 | 0.475 | 0.422 | 0.180 |
| Supreme court with cross-checking constitutional court | 0.549 | 0.548-0.549 | 0.000 | 0.624 | 0.620 | 0.079 | 0.489 | 0.403 | 0.350 |
| Dual supreme courts with disagreement filter | 0.537 | 0.537-0.538 | 0.000 | 0.593 | 0.649 | 0.079 | 0.497 | 0.399 | 0.391 |
