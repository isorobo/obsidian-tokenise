---
type: meta
status: archived
created: 2026-05-24
updated: 2026-08-09
---

# NotebookLM Bridge

> [!warning] Retired from the weekly cron on 9 August 2026
> The `/wiki-tokenise notebooklm-sync all` stage no longer runs on a schedule.
> See [§Decision record](#decision-record-9-august-2026). The subcommand still
> works if invoked by hand after `notebooklm login`.

## Decision record, 9 August 2026

**Decision.** Cut the sync stage from `wiki-tokenise-weekly.ps1`. Keep the
subcommand for manual use. Keep the `nlm_*` frontmatter fields as deprecated
rather than stripping them, because 97 notes hold real IDs and the change
should stay reversible.

**Why.** The stage last wrote an ID back on 14 June 2026. The last run to
stamp `nlm_last_sync` was 24 May 2026. It then failed for eleven consecutive
weeks, for three different reasons in sequence:

| Period | Failure |
|---|---|
| 28 June | MCP server disconnected; CLI not installed |
| 12 to 26 July, 2 August | Stage never invoked the sync; output was a recommendation to run it by hand |
| 26 July onward | Session expired; requires an interactive browser login that cannot complete on a scheduled task |

Each run reported exit code 0, so the failure never surfaced. The backlog grew
from 48 unsynced sources in June to 121 by 9 August. A stage that cannot
succeed unattended does not belong in an unattended job.

**What replaces it.** Nothing external. The annotation layer NotebookLM was
meant to supply already exists inside the vault, in
[[SOURCE-REGISTER]], which holds 714 lines of curated annotation across 58
headings. That register carries no wikilinks and no note carries a
`register_section` value, so the two layers do not connect. Wiring them is the
replacement work. See `99_Meta/wiki-tokenise/concepts-layer-2026-08-09.md`
for the wider structural picture.

**To revive.** Run `notebooklm login`, confirm with `refresh_auth`, then
`/wiki-tokenise notebooklm-sync all`. Re-add the stage to the cron array only
if authentication can be made to survive unattended.

## Notebook

- **Title:** tokenise
- **UUID:** `d9fa07bb-4802-4626-8855-ba899655ab2b`
- **URL:** https://notebooklm.google.com/notebook/d9fa07bb-4802-4626-8855-ba899655ab2b
- **Account:** isorobo6@gmail.com (default profile)

## Sync log

| Date | Action | Notes |
|---|---|---|
| 2026-05-24 | Initial import | 50 sources retrieved; 4 deleted (3 duplicate copies of arXiv 2601.04583, 1 `scholarly.md`). 46 live sources auto-generated as stub notes in [[SOURCE-REGISTER]] Section 16 and across `10_Sources/<Category>/`. |
| 2026-06-07 | notebooklm-sync all | Backfilled 6 BIS Working Papers as full-text PDF sources (work1270, 1280, 1301, 1335, 1340, 1355). Source count 46 to 52. `nlm_id` written back to each note. These had empty `nlm_id` because earlier weekly runs ended after the monitor without reaching the sync step. |
| 2026-06-14 | notebooklm-sync (manual) | Re-authenticated via `nlm login` (headless cron sync had skipped). Pushed the 2 remaining sources with empty `nlm_id`: WP1359 (anatomy of stablecoin transactions, `11e1a667-1100-48c5-a0a0-f00d46562071`) and WP1311 (tokenisation of real estate, `ab0579ca-81d3-4a44-b931-02bf12867a38`). Source count 52 to 54. `nlm_id` written back to both notes. |
| 2026-07-12 | notebooklm-sync all (blocked) | Google session expired; token fetch failed and the sync pushed nothing. 71 sources across `10_Sources/` hold an empty `nlm_id` and await push. Re-run `notebooklm login` then `/wiki-tokenise notebooklm-sync all`. |
| 2026-07-19 to 2026-08-02 | not invoked | The cron stage returned a recommendation to run the sync by hand rather than running it. No push attempted on any of the four runs. |
| 2026-08-09 | retired | Stage cut from the weekly cron. 121 sources hold an empty `nlm_id`; 5 carry `nlm_skip: true`; 97 hold an ID. See the decision record above. |

## Operations

- `nlm login` (host shell): re-authenticate when tokens expire.
- `refresh_auth` (MCP): pick up new tokens after CLI login.
- `notebook_get`: list sources with UUIDs.
- `source_describe`: per-source AI summary with keyword chips (use for stub enrichment).
- `source_delete --confirm true`: irreversible.

## Next top-up

Run `source_describe` over each NLM source ID and paste the keyword chips + summary into the corresponding stub annotation under `10_Sources/`. Match by `nlm_id` in frontmatter.
