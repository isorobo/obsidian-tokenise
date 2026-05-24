# wiki-tokenise infrastructure

This folder holds state and rollups for the **wiki-tokenise** orchestrator
skill (`~/.claude/skills/wiki-tokenise/SKILL.md`) and the per-channel
monitor subagent (`~/.claude/agents/wiki-tokenise-monitor.md`).

Hand-curated content stays elsewhere in the vault. This folder is owned
by the orchestrator and the monitor.

## Files

| Path | Owner | Purpose |
|---|---|---|
| `watchlist.md` | orchestrator | Single source of truth for active source channels. |
| `index.md` | orchestrator | Auto-maintained rollup printed by `/wiki-tokenise status`. |
| `state/<channel>.json` | monitor | Per-channel agent state (dedupe, cursor, counts). |
| `state/logs/weekly-*.log` | cron wrapper | Output of each `/wiki-tokenise weekly-refresh` run. |
| `queries/<channel>.md` | monitor | Per-channel query log. |

## Workflow

1. The orchestrator reads `watchlist.md`. Rows with `status: active` or
   `status: pilot` are in scope.
2. `/wiki-tokenise run <channel>` spawns a background
   `wiki-tokenise-monitor` subagent. That agent reads
   `state/<channel>.json`, plans queries against the channel surface,
   fetches new sources published since `last_run_at`, writes new files
   under `10_Sources/<Category>/`, and updates state.
3. `/wiki-tokenise status` reads every `state/*.json` and rewrites
   `index.md`.
4. `/wiki-tokenise weekly-refresh` runs `run all` → `notebooklm-sync all`
   → `wiki-refresh`. This is the cron entry point.

## Do not edit by hand

- `state/*.json` and `queries/*.md` are agent-owned.
- `index.md` is orchestrator-owned.

Hand edits will be overwritten.

`watchlist.md` is the user-editable surface. Add, remove, or flip status
on any row. The orchestrator reconciles `watchlist.md` against
`state/*.json` presence on each `init` call.

## Pilot

The pilot for this build is **bis-working-papers**. Once stable, promote
**imf-fintech-notes**, then **mas-news** and **hkma-press**.
