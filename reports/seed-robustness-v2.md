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
| 60 percent invalidation threshold | 0.569 | 0.569-0.570 | 0.000 | 0.612 | 0.612 | 0.098 | 0.466 | 0.476 | 0.187 |
| No emergency relief without merits review | 0.569 | 0.568-0.569 | 0.001 | 0.581 | 0.634 | 0.022 | 0.466 | 0.476 | 0.230 |
| 18-year staggered terms + regular appointments | 0.567 | 0.566-0.568 | 0.001 | 0.597 | 0.621 | 0.106 | 0.467 | 0.475 | 0.191 |
| Constitutional remand before invalidation | 0.566 | 0.566-0.568 | 0.001 | 0.629 | 0.620 | 0.107 | 0.467 | 0.495 | 0.304 |
| Public-interest litigation filter | 0.564 | 0.564-0.565 | 0.000 | 0.600 | 0.627 | 0.106 | 0.467 | 0.474 | 0.238 |
| Jurisdiction stripping constrained by rights carveouts | 0.564 | 0.564-0.565 | 0.000 | 0.592 | 0.622 | 0.106 | 0.481 | 0.465 | 0.214 |
| Nonpartisan commission appointments | 0.563 | 0.563-0.564 | 0.000 | 0.596 | 0.622 | 0.107 | 0.469 | 0.474 | 0.214 |
| Constitutional remand with override window | 0.563 | 0.563-0.564 | 0.000 | 0.634 | 0.616 | 0.077 | 0.468 | 0.495 | 0.334 |
| Automatic merits follow-up for emergency relief | 0.563 | 0.562-0.563 | 0.001 | 0.575 | 0.632 | 0.030 | 0.467 | 0.476 | 0.245 |
| Peer recusal + reasoned emergency docket | 0.563 | 0.562-0.563 | 0.001 | 0.597 | 0.621 | 0.105 | 0.466 | 0.476 | 0.219 |
| Mandatory written emergency reasoning | 0.563 | 0.562-0.563 | 0.000 | 0.603 | 0.617 | 0.076 | 0.469 | 0.474 | 0.229 |
| Retention-election accountability court | 0.562 | 0.561-0.562 | 0.000 | 0.598 | 0.613 | 0.106 | 0.484 | 0.466 | 0.214 |
| Three-judge panels with en banc correction | 0.562 | 0.561-0.563 | 0.001 | 0.597 | 0.623 | 0.107 | 0.468 | 0.474 | 0.230 |
| Emergency integrity package | 0.562 | 0.562-0.562 | 0.000 | 0.580 | 0.634 | 0.030 | 0.467 | 0.476 | 0.268 |
| Expanded 15-seat court | 0.561 | 0.560-0.561 | 0.000 | 0.597 | 0.621 | 0.106 | 0.466 | 0.476 | 0.227 |
| Randomized merits panels with en banc correction | 0.561 | 0.560-0.561 | 0.001 | 0.597 | 0.623 | 0.107 | 0.468 | 0.474 | 0.237 |
| Independent recusal enforcement with substitutes | 0.561 | 0.560-0.562 | 0.000 | 0.596 | 0.623 | 0.106 | 0.469 | 0.474 | 0.235 |
| Time-limited legislative override window | 0.560 | 0.559-0.561 | 0.001 | 0.592 | 0.622 | 0.106 | 0.487 | 0.464 | 0.221 |
| Comparative 16-seat constitutional senates | 0.560 | 0.559-0.560 | 0.000 | 0.616 | 0.612 | 0.098 | 0.465 | 0.476 | 0.259 |
| Judicial review with legislative supermajority override | 0.559 | 0.559-0.560 | 0.000 | 0.591 | 0.623 | 0.107 | 0.488 | 0.462 | 0.221 |
| Random panels with jurisdiction safeguards | 0.558 | 0.558-0.559 | 0.000 | 0.604 | 0.613 | 0.099 | 0.479 | 0.467 | 0.261 |
| Constitutional council with concrete-review backstop | 0.557 | 0.556-0.557 | 0.000 | 0.610 | 0.624 | 0.105 | 0.481 | 0.488 | 0.308 |
| Pre-enactment constitutional council | 0.557 | 0.556-0.557 | 0.001 | 0.603 | 0.624 | 0.106 | 0.486 | 0.485 | 0.295 |
| Judicial electorate selection court | 0.556 | 0.556-0.556 | 0.000 | 0.597 | 0.624 | 0.106 | 0.469 | 0.474 | 0.276 |
| Stylized current U.S.-like supreme court | 0.553 | 0.552-0.553 | 0.000 | 0.590 | 0.634 | 0.304 | 0.506 | 0.454 | 0.152 |
| Supreme court with cross-checking constitutional court | 0.550 | 0.550-0.551 | 0.000 | 0.614 | 0.596 | 0.098 | 0.487 | 0.460 | 0.296 |
| Dual supreme courts with disagreement filter | 0.535 | 0.534-0.535 | 0.000 | 0.573 | 0.620 | 0.099 | 0.499 | 0.451 | 0.331 |
