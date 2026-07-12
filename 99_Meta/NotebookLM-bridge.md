---
type: meta
created: 2026-05-24
---

# NotebookLM Bridge

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

## Operations

- `nlm login` (host shell): re-authenticate when tokens expire.
- `refresh_auth` (MCP): pick up new tokens after CLI login.
- `notebook_get`: list sources with UUIDs.
- `source_describe`: per-source AI summary with keyword chips (use for stub enrichment).
- `source_delete --confirm true`: irreversible.

## Next top-up

Run `source_describe` over each NLM source ID and paste the keyword chips + summary into the corresponding stub annotation under `10_Sources/`. Match by `nlm_id` in frontmatter.
