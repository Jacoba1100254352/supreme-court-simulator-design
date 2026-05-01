# Codex Guidance

This is the earlier supreme-court and constitutional-review design workspace. It overlaps with the separate `Constitutional Review Simulator` project, but it came from its own Codex session and should remain distinct unless the user asks to merge them.

Use these commands from this directory when code is present:

- `make build`
- `make run`
- `make test`
- `make campaign`

Project constraints:

- Keep the project independent from the Congress Institutional Simulator; import legislative outputs through documented data contracts rather than Java source dependencies.
- Preserve the focus on appointment methods, court size, terms, recusal, shadow-docket rules, voting thresholds, panels, cross-checking courts, constitutional councils, overrides, independence, and accountability.
- If consolidating work with `Constitutional Review Simulator`, compare files first and preserve the richer implementation rather than overwriting by name.
