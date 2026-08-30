# Codex Guidance

This is the earlier supreme-court and constitutional-review design workspace. It overlaps with the separate `Constitutional Review Simulator` project, but it came from its own Codex session and should remain distinct unless the user asks to merge them.

Use these commands from this directory:

- `make build`
- `make run`
- `make test`
- `make campaign`
- `make paper-strict-check`
- `make replication-check`

Project constraints:

- Keep the project independent from the Congress Institutional Simulator; import legislative outputs through documented data contracts rather than Java source dependencies.
- Preserve the focus on appointment methods, court size, terms, recusal, shadow-docket rules, voting thresholds, panels, cross-checking courts, constitutional councils, overrides, independence, and accountability.
- If consolidating work with `Constitutional Review Simulator`, compare files first and preserve the richer implementation rather than overwriting by name.

## Public Repository and Secret Handling

- Treat this repository and every committed file as public information.
- Never commit `.env`, `.env.*`, credentials, access tokens, private keys, signing material, restricted-source caches, or environment-specific private paths. Track only scrubbed templates such as `.env.example`, with blank or unmistakably fake values.
- Before staging or publishing, inspect `git status --short`, review the staged diff, and run a redacted secret scan when available. Confirm that ignored local credential files remain ignored.
- If a real secret ever enters tracked content or Git history, stop publication, remove it from the affected history, and rotate or revoke the credential before pushing or changing visibility.

## Commit, Tag, and Release Policy

- Commit coherent, validated increments frequently: normally after each focused change passes its relevant checks and before switching to a different concern. Preserve unrelated user work and do not fold it into an unclear commit.
- Push validated commits as the normal completion step so the public repository stays current.
- Create tags less frequently, only for meaningful version, citation, submission, or compatibility milestones. An ordinary commit does not need a tag.
- Publish a release only at a milestone with aligned version metadata, release notes, verified artifacts and checksums where applicable, and passing release checks. Use a draft or prerelease for genuinely provisional milestones, a source-only release when that is the intended artifact, and a stable release only when the documented stable benchmark is met.
