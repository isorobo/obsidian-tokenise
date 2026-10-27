---
title: Claude Operating Manual — wiki-tokenise
type: system
date: 2026-06-30
last_verified: 2026-10-27
next_verification_due: 2027-01-27
tags:
  - system
  - vault-rules
  - ai-first
---

# Claude Operating Manual — wiki-tokenise

> Read this file before doing anything in this vault.
> This is the single source of truth for how Claude operates here.
> Last verified 27 October 2026. Re-verify quarterly (next due 27 January 2027): see "Maintenance of this file" at the end.

---

## Section 0 — AI-First Vault Rule (read first, applies to every note)

This vault is designed for **future-Claude** to read and reason over, not for human review. The owner uses Claude to retrieve, synthesize, and connect patterns across tokenisation research.

**Every note Claude writes to this vault must follow these rules:**

1. **Self-contained context** — Each note must explain itself. Future-Claude may pull this single note via search with no surrounding context. Don't rely on backlinks alone for meaning.
2. **"For future Claude" preamble** — Every note begins with a 2-3 sentence summary so Claude can decide relevance in 10 seconds before parsing structured data.
3. **Rich, consistent frontmatter** — Filterable metadata (`type`, `date`, `topic`, `tags`, `related-sources`, `jurisdiction`, `instrument`). See source schema in `99_Meta/schema.md`.
4. **Recency markers per claim** — When stating external facts: "BIS reports X (as of 2026-03, bis.org)" so future-Claude knows what to verify.
5. **Sources preserved verbatim** — Every external claim has its source URL inline and linked via `[[wikilink]]`.
6. **Cross-links are mandatory** — Every source, regulator, jurisdiction, instrument, or concept referenced uses `[[wikilinks]]` so the graph is traversable.
7. **Confidence levels** — Where applicable, mark claims as `stated | high | medium | speculation` so future-Claude knows what to trust vs verify.

This rule applies to all scheduled agents and to every note written by hand or by session.

---

## Section 0.5 — Verify Live State Before Acting

Before declaring a pattern, drafting a synthesis, or claiming a source says X: read the actual source text, not memory. Speculation burns context.

Specific cues:
- Read the source annotation before claiming what it says
- Grep for exact phrases before declaring consensus or contradiction
- Fetch current channel status from `99_Meta/wiki-tokenise/` before skipping a monitor run
- Check `last_run_at` timestamps before re-running a monitor
- Verify instrument classification against `99_Meta/schema.md` before categorising a source
- Treat counts, channel lists and dates in any prose (including this file) as possibly stale; the live values are in `99_Meta/wiki-tokenise/index.md` and `watchlist.md`

---

## Vault Identity

- **Owner:** Simon Gaines (simon@lundonslaw.com)
- **Primary purpose:** Tokenisation research vault: regulatory, legal and economic sources on real-world asset tokenisation, securities tokenisation, stablecoins, CBDC and digital finance infrastructure
- **Public vault:** this vault is published on GitHub and contains verified source notes, neutral concept notes and maps of content only. Analysis, argument and unverified drafts belong in the owner's private companion vault at `~/obsidian/wiki-embed`. Do not write thesis or interpretation here, and do not copy private notes into this vault.

---

## Folder Map

| Folder | Purpose |
|---|---|
| `10_Sources/` | One note per source, by category: Academia, Central-Banks, Commercial-Banks, Industry-Press, International-Agencies, Law-Regulation, Private-Sector, Think-Tanks. `SOURCE-REGISTER.md` is frozen (see Do Not Touch). |
| `30_Areas/` | Synthesis notes across several sources. |
| `30_Concepts/` | Atomic term notes, one per concept. Many are still stubs. |
| `50_MOCs/` | Hand-curated maps of content. `MOC - Root.md` is the front door. Do not auto-write. |
| `60_Drafts/` | Long-form drafts. Drafts marked `unverified` are not to be cited. |
| `80_Attachments/` | PDFs by channel under `PDFs/<channel>/`, and fonts. |
| `90_Templates/` | Templates for source, concept, person and MOC notes. The source template also holds the closed topic vocabulary. |
| `99_Meta/` | Schema, design notes, forecast data, and `wiki-tokenise/` (watchlist, state, queries, reports). |
| `.remember/` | Session memory (auto-managed by Claude). |
| `_archived_wiki-old-structure/` | Retired layout. Read-only reference. |

`00_Inbox/`, `20_People/`, `40_Domains/`, `40_Projects/` and `70_Research/` no longer exist.

---

## Key Files

- **Schema:** `[[99_Meta/schema.md]]`: frontmatter and enum values
- **Watchlist (live channel list):** `99_Meta/wiki-tokenise/watchlist.md`
- **Status (live counts and last runs):** `99_Meta/wiki-tokenise/index.md`
- **Channel state and query logs:** `99_Meta/wiki-tokenise/state/` and `queries/`
- **Weekly reports:** `99_Meta/wiki-tokenise/wiki-refresh-<date>.md`
- **Today's buffer:** `.remember/now.md`

---

## Active Context

The list of monitored channels, how many sources the vault holds and when each channel last ran are **not** recorded here. Read them from `watchlist.md` and `index.md`.

The weekly pipeline runs through the launchd job `com.lundons.wiki-weekly` (Sunday 06:00 New Zealand time). It runs the channel monitors, tags the new notes via the global `/wiki` skill, and commits locally. It never pushes. Engine source: `~/code/coding-tools/wiki-engine`.

---

## Auto-Save Rules

Claude should **auto-save without asking**:
- New sources ingested by monitors → `10_Sources/<Category>/` with frontmatter
- Updates to monitoring state → `99_Meta/wiki-tokenise/state/` (monitors only)

Claude should **ask before saving**:
- Anything that deletes or archives an existing source
- Anything that marks a monitor as "skip this run"
- Contradictions requiring reconciliation across sources
- New concept notes, synthesis notes and edits to MOCs (hand-curated)

---

## Naming Conventions

- **Sources:** `Author-or-Org-SourceTitle-Year.md` (e.g. `BIS-WP1335-Tokenomics-Blockchain-Fragmentation.md`)
- **Concepts:** Title-case with hyphens (e.g. `Singleness-of-Money.md`)
- **MOCs:** `MOC - Name.md`
- **Archive prefix:** `_archived_`
- **Style:** NZ English. No em dashes or en dashes in written notes.

---

## Frontmatter Requirements

The source template at `90_Templates/template - source.md` and `99_Meta/schema.md` are authoritative. In outline, every source note carries: `type: source`, `status`, `created`, `title`, `organisation`, `source_type`, `year`, `date_published`, `url`, `jurisdiction`, `domain`, `doctrine`, `instrument`, `tags`.

Do **not** hand-edit these fields: `topic`, `subject`, `wiki_indexed`, `wiki_hash`, `wiki_role`, `watchlist_channel`. The `/wiki` skill and the orchestrator set them. The `nlm_id` and `nlm_skip` fields are deprecated (the NotebookLM sync was retired on 9 August 2026); do not populate them on new notes.

Controlled values (jurisdiction, domain, instrument, topic) are closed sets. Never invent a value: use the nearest legal one and raise the gap in the run report.

---

## Monitors

Each channel in `watchlist.md` is run by one `wiki-tokenise-monitor` subagent, dispatched by `/wiki-tokenise`. Cadence minimums are enforced by the tooling (weekly and daily channels 6 days, monthly 21 days, irregular 13 days). Do not re-run a channel earlier unless the owner asks.

Out-of-loop pickups of named URLs use `/wiki-tokenise backfill <channel> <url...>`. The weekly runner never calls it.

---

## Propagation Rules

| Event | Also update |
|---|---|
| New source ingested | Channel state and query log (monitor does this). MOC placement is by hand from the weekly `wiki-moc-candidates-<date>.json`. |
| Monitor completes | `99_Meta/wiki-tokenise/state/<channel>.json` with `last_run_at` |
| Contradiction found | Flag in the source note; raise with the owner |

---

## Do Not Touch

- `99_Meta/schema.md`: read only; the owner changes enums
- `10_Sources/SOURCE-REGISTER.md`: frozen
- `99_Meta/wiki-tokenise/watchlist.md`: owner-edited; report recommended edits instead
- `_CLAUDE.md` and `README.md`: edited by hand in an interactive session only, never by a scheduled stage
- `.remember/`: session memory, auto-managed
- `state/*.json` and `queries/*.md`: written by monitors only
- `.obsidian/`: Obsidian settings

---

## Maintenance of this file

`README.md` and this file go stale because the vault changes weekly. Both carry `last_verified` in their frontmatter.

1. **Quarterly (next: 27 January 2027, then every three months):** check the folder map, the Do Not Touch list, the Key Files paths and the launchd label against what exists on disk, then update `last_verified` and `next_verification_due` here and `last_verified` in `README.md`.
2. **Automatic reminder:** the weekly digest stage in the owner's private vault reads `last_verified` from this file and raises a flag when it is more than 90 days old.
3. Keep numbers out of both files; point to `index.md` and `watchlist.md` instead.
