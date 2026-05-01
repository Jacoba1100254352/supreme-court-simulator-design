# Constitutional Review Simulator

This is a separate Java simulation project for comparing supreme-court and constitutional-review institutional designs. It follows the campaign/scenario/report style of the adjacent congressional simulator while keeping the source tree independent.

The simulator evaluates court designs across generated constitutional cases and, optionally, imports legislative campaign outputs as docket inputs. Imported legislative metrics are summarized into a `LegislativeOutputProfile`, which affects case quality, rights risk, weak-mandate disputes, emergency pressure, and constitutional conflict.

## Requirements

- Java 21 or newer
- `make`

There are no external Java dependencies.

## Common Commands

Build:

```sh
make build
```

Run the default scenario comparison:

```sh
make run
```

Run tests:

```sh
make test
```

Build the paper:

```sh
make paper
```

Write the current v2 campaign artifacts:

```sh
make campaign
```

`make campaign` now writes the v2 campaign. The initial v0 and v1 campaigns remain available as `make campaign-v0` and `make campaign-v1`.

Run the diagnostic suite:

```sh
make diagnostics
```

The suite writes source-backed historical calibration guardrails, seed-robustness bands, parameter-sweep uncertainty bands, mechanism ablations, a focused adversarial-manipulation stress campaign, and a multi-family legislative-import comparison.

Run the parameter sweep only:

```sh
make parameter-sweep
```

Compare the import contract against multiple congressional-simulator report families:

```sh
make legislative-family-comparison
```

Set `LEGISLATIVE_FAMILY_DIR=/path/to/reports` to compare a different directory of legislative campaign CSVs.

Import a legislative simulator report as input:

```sh
make campaign ARGS="--legislative-input '/Users/jacobanderson/Documents/simulators/Congress Institutional Simulator/reports/simulation-campaign-v21-paper.csv'"
```

## Current Design Surface

The catalog includes appointment method, court size, term limits, removal standards, recusal rules, emergency docket procedures, voting thresholds, concurrence/dissent behavior, panel versus en banc review, dual or cross-checking courts, constitutional councils, legislative override rules, and independence/accountability tradeoffs.

The v1 campaign added docket subtypes, justice replacement/vacancy dynamics, richer emergency procedure states, stronger override outcomes, stress-case slices, and sensitivity cases for appointment capture, emergency pressure, rights risk, and weak democratic mandate.

The v2 campaign adds adversarial manipulation cases for appointment timing, emergency-application flooding, override evasion, recusal pressure, and court-expansion retaliation. It also splits legal stability into precedent stability, statutory stability, and interbranch compliance while keeping the blended legal-stability metric for headline comparisons.

The current diagnostics add source-backed historical calibration ranges, legal-domain profiles for rights, election, executive-power, administrative, structural, and economic-regulation cases, and explicit strategic response state for legislative defiance, executive emergency behavior, appointment manipulation pressure, and override adaptation.

The headline metrics are legal stability, rights protection, partisan alignment, shadow-docket abuse, legitimacy, reversal rate, constitutional conflict, and democratic responsiveness.

## Current Reports

- `reports/constitutional-review-campaign-v2.csv` and `.md`: full v2 campaign.
- `reports/calibration-baseline.csv` and `.md`: source-backed historical plausibility guardrails for docket mix and key rates.
- `reports/seed-robustness-v2.csv` and `.md`: weighted v2 campaign sensitivity across deterministic seed offsets.
- `reports/mechanism-ablation-v2.csv` and `.md`: pairwise institutional mechanism comparisons.
- `reports/manipulation-stress-v2.csv` and `.md`: focused adversarial stress campaign.
- `reports/parameter-sweep-v3.csv` and `.md`: uncertainty bands from changing model parameters, not only random seeds.
- `reports/legislative-family-comparison-v3.csv` and `.md`: constitutional-review results across multiple congressional-simulator campaign families.

## Paper

The LaTeX manuscript lives at `paper/main.tex`. It is intentionally framed as a model-and-design paper, not a claim that the current formulas are empirically validated.
