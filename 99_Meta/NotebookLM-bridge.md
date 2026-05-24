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

## Operations

- `nlm login` (host shell): re-authenticate when tokens expire.
- `refresh_auth` (MCP): pick up new tokens after CLI login.
- `notebook_get`: list sources with UUIDs.
- `source_describe`: per-source AI summary with keyword chips (use for stub enrichment).
- `source_delete --confirm true`: irreversible.

## Next top-up

Run `source_describe` over each NLM source ID and paste the keyword chips + summary into the corresponding stub annotation under `10_Sources/`. Match by `nlm_id` in frontmatter.
