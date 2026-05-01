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
| 60 percent invalidation threshold | 0.786 | 0.786-0.787 | 0.000 | 0.748 | 0.696 | 0.050 | 0.294 | 0.600 | 0.266 |
| 18-year staggered terms + regular appointments | 0.784 | 0.783-0.784 | 0.000 | 0.745 | 0.702 | 0.066 | 0.295 | 0.599 | 0.272 |
| Stylized current U.S.-like supreme court | 0.777 | 0.776-0.777 | 0.000 | 0.741 | 0.702 | 0.240 | 0.296 | 0.599 | 0.222 |
| No emergency relief without merits review | 0.776 | 0.776-0.776 | 0.000 | 0.754 | 0.695 | 0.001 | 0.293 | 0.600 | 0.326 |
| Nonpartisan commission appointments | 0.776 | 0.775-0.776 | 0.000 | 0.747 | 0.701 | 0.066 | 0.295 | 0.600 | 0.302 |
| Retention-election accountability court | 0.776 | 0.775-0.776 | 0.000 | 0.749 | 0.697 | 0.066 | 0.298 | 0.597 | 0.302 |
| Three-judge panels with en banc correction | 0.775 | 0.775-0.775 | 0.000 | 0.747 | 0.700 | 0.066 | 0.295 | 0.599 | 0.315 |
| Judicial review with legislative supermajority override | 0.774 | 0.774-0.774 | 0.000 | 0.745 | 0.702 | 0.066 | 0.300 | 0.596 | 0.312 |
| Peer recusal + reasoned emergency docket | 0.770 | 0.770-0.771 | 0.000 | 0.747 | 0.701 | 0.066 | 0.295 | 0.599 | 0.312 |
| Expanded 15-seat court | 0.770 | 0.770-0.770 | 0.000 | 0.746 | 0.702 | 0.066 | 0.295 | 0.599 | 0.322 |
| Pre-enactment constitutional council | 0.760 | 0.760-0.761 | 0.000 | 0.753 | 0.696 | 0.066 | 0.298 | 0.604 | 0.368 |
| Supreme court with cross-checking constitutional court | 0.736 | 0.736-0.736 | 0.000 | 0.736 | 0.692 | 0.049 | 0.332 | 0.569 | 0.418 |
| Dual supreme courts with disagreement filter | 0.720 | 0.720-0.720 | 0.000 | 0.725 | 0.703 | 0.049 | 0.333 | 0.569 | 0.467 |
