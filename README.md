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

Build the starter paper:

```sh
make paper
```

Write the v0 campaign artifacts:

```sh
make campaign
```

Import a legislative simulator report as input:

```sh
make campaign ARGS="--legislative-input '/Users/jacobanderson/Documents/simulators/Congress Institutional Simulator/reports/simulation-campaign-v21-paper.csv'"
```

## Current Design Surface

The v0 catalog includes appointment method, court size, term limits, removal standards, recusal rules, emergency docket procedures, voting thresholds, concurrence/dissent behavior, panel versus en banc review, dual or cross-checking courts, constitutional councils, legislative override rules, and independence/accountability tradeoffs.

The headline metrics are legal stability, rights protection, partisan alignment, shadow-docket abuse, legitimacy, reversal rate, constitutional conflict, and democratic responsiveness.

## Paper

The initial LaTeX manuscript lives at `paper/main.tex`. It is intentionally framed as a model-and-design paper, not a claim that the v0 formulas are empirically validated.
