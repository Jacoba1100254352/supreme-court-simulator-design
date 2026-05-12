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
| 60 percent invalidation threshold | 0.570 | 0.569-0.570 | 0.000 | 0.612 | 0.612 | 0.097 | 0.464 | 0.477 | 0.186 |
| No emergency relief without merits review | 0.569 | 0.568-0.569 | 0.001 | 0.582 | 0.633 | 0.022 | 0.464 | 0.477 | 0.229 |
| 18-year staggered terms + regular appointments | 0.567 | 0.566-0.568 | 0.001 | 0.598 | 0.620 | 0.105 | 0.464 | 0.477 | 0.190 |
| Constitutional remand before invalidation | 0.567 | 0.566-0.568 | 0.001 | 0.629 | 0.619 | 0.106 | 0.465 | 0.496 | 0.302 |
| Public-interest litigation filter | 0.565 | 0.564-0.565 | 0.000 | 0.601 | 0.626 | 0.106 | 0.465 | 0.475 | 0.237 |
| Jurisdiction stripping constrained by rights carveouts | 0.564 | 0.564-0.565 | 0.000 | 0.593 | 0.621 | 0.105 | 0.479 | 0.466 | 0.213 |
| Nonpartisan commission appointments | 0.564 | 0.563-0.564 | 0.000 | 0.596 | 0.621 | 0.106 | 0.468 | 0.475 | 0.213 |
| Constitutional remand with override window | 0.564 | 0.563-0.564 | 0.000 | 0.635 | 0.615 | 0.076 | 0.466 | 0.496 | 0.332 |
| Automatic merits follow-up for emergency relief | 0.563 | 0.563-0.564 | 0.000 | 0.576 | 0.631 | 0.030 | 0.465 | 0.477 | 0.244 |
| Mandatory written emergency reasoning | 0.563 | 0.562-0.563 | 0.000 | 0.604 | 0.616 | 0.076 | 0.467 | 0.475 | 0.227 |
| Peer recusal + reasoned emergency docket | 0.563 | 0.562-0.563 | 0.000 | 0.597 | 0.620 | 0.105 | 0.465 | 0.476 | 0.219 |
| Three-judge panels with en banc correction | 0.562 | 0.561-0.563 | 0.001 | 0.598 | 0.622 | 0.106 | 0.466 | 0.475 | 0.229 |
| Retention-election accountability court | 0.562 | 0.562-0.563 | 0.000 | 0.598 | 0.612 | 0.105 | 0.482 | 0.467 | 0.213 |
| Emergency integrity package | 0.562 | 0.562-0.563 | 0.000 | 0.580 | 0.633 | 0.030 | 0.465 | 0.477 | 0.266 |
| Randomized merits panels with en banc correction | 0.561 | 0.560-0.562 | 0.001 | 0.598 | 0.621 | 0.106 | 0.466 | 0.475 | 0.236 |
| Expanded 15-seat court | 0.561 | 0.561-0.561 | 0.000 | 0.598 | 0.621 | 0.105 | 0.465 | 0.477 | 0.226 |
| Independent recusal enforcement with substitutes | 0.561 | 0.560-0.562 | 0.000 | 0.596 | 0.622 | 0.106 | 0.467 | 0.475 | 0.234 |
| Time-limited legislative override window | 0.560 | 0.560-0.561 | 0.001 | 0.593 | 0.621 | 0.106 | 0.485 | 0.465 | 0.220 |
| Comparative 16-seat constitutional senates | 0.560 | 0.560-0.560 | 0.000 | 0.617 | 0.611 | 0.097 | 0.463 | 0.477 | 0.258 |
| Judicial review with legislative supermajority override | 0.560 | 0.559-0.560 | 0.000 | 0.592 | 0.623 | 0.106 | 0.486 | 0.463 | 0.220 |
| Random panels with jurisdiction safeguards | 0.559 | 0.558-0.559 | 0.000 | 0.605 | 0.612 | 0.098 | 0.477 | 0.468 | 0.260 |
| Constitutional council with concrete-review backstop | 0.557 | 0.556-0.557 | 0.000 | 0.610 | 0.623 | 0.104 | 0.479 | 0.488 | 0.306 |
| Pre-enactment constitutional council | 0.557 | 0.556-0.558 | 0.001 | 0.604 | 0.623 | 0.106 | 0.484 | 0.486 | 0.293 |
| Judicial electorate selection court | 0.556 | 0.556-0.557 | 0.000 | 0.598 | 0.623 | 0.106 | 0.468 | 0.475 | 0.275 |
| Stylized current U.S.-like supreme court | 0.553 | 0.552-0.554 | 0.001 | 0.590 | 0.633 | 0.302 | 0.504 | 0.455 | 0.151 |
| Supreme court with cross-checking constitutional court | 0.550 | 0.550-0.551 | 0.000 | 0.614 | 0.595 | 0.098 | 0.486 | 0.461 | 0.294 |
| Dual supreme courts with disagreement filter | 0.535 | 0.535-0.536 | 0.000 | 0.573 | 0.619 | 0.098 | 0.497 | 0.452 | 0.330 |
