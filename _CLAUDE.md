---
title: Claude Operating Manual — wiki-tokenise
type: system
date: 2026-06-30
tags:
  - system
  - vault-rules
  - ai-first
---

# Claude Operating Manual — wiki-tokenise

> Read this file before doing anything in this vault.
> This is the single source of truth for how Claude operates here.

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

This rule applies to all `/obsidian-*` and `/research*` commands and all scheduled agents.

---

## Section 0.5 — Verify Live State Before Acting

Before declaring a pattern, drafting a synthesis, or claiming a source says X: read the actual source text, not memory. Speculation burns context.

Specific cues:
- Read the source annotation before claiming what it says
- Grep for exact phrases before declaring consensus or contradiction
- Fetch current channel status from `99_Meta/wiki-tokenise/` before skipping a monitor run
- Check last_run_at timestamps before re-running a monitor
- Verify instrument classification against `99_Meta/schema.md` before categorising a source

---

## Vault Identity

- **Owner:** Simon Gaines (simon@lundonslaw.com)
- **Primary purpose:** Tokenisation research vault — regulatory, legal, and economic sources on real-world asset tokenisation, securities tokenisation, and digital finance infrastructure
- **Last updated:** 2026-06-30

---

## Folder Map

| Folder | Purpose |
|---|---|
| `10_Sources/` | Ingested sources, one .md per source. Organized by category (Academia, Central-Banks, Commercial-Banks, Industry-Press, International-Agencies, Law-Regulation, Private-Sector, Think-Tanks). See `10_Sources/SOURCE-REGISTER.md` for index. |
| `20_People/` | Researchers, regulators, authors. One note per person. |
| `30_Areas/` | Topic maps and concept notes (tokenisation economics, settlement, liquidity, securities frameworks, etc.). |
| `40_Projects/` | Active research initiatives. |
| `99_Meta/` | Vault metadata, schema, monitors, state. |
| `.remember/` | Session memory (auto-managed by Claude). |

---

## Key Files

- **Source Register:** `[[10_Sources/SOURCE-REGISTER.md]]` — index of all ingested sources
- **Vault Schema:** `[[99_Meta/schema.md]]` — frontmatter schema for sources, people, concepts
- **Monitor Status:** `[[99_Meta/wiki-tokenise/]]` — channel states, last_run_at timestamps
- **Today's buffer:** `.remember/now.md` — current session context

---

## Active Context

**Current focus:** Tokenisation economics and securities tokenisation frameworks
**Monitor status:** 12 channels live (FSB, IOSCO, BIS, IMF, HKMA, ESMA, MAS, Fed, UNIDROIT, Wharton, Invesco, private-sector)
**Sources indexed:** ~37 (6 UNIDROIT, 6 HKMA, 5 ESMA, 4 Fed, 4 IMF, others)

---

## Auto-Save Rules

Claude should **auto-save without asking**:
- New sources ingested by monitors → `10_Sources/` with frontmatter + annotation
- Synthesis findings → `30_Areas/Synthesis — [topic].md` with source links and confidence
- People mentioned in sources → `20_People/` (stub if new)
- Updates to monitoring state → `99_Meta/wiki-tokenise/channel-name.md`

Claude should **ask before saving**:
- Anything that deletes or archives an existing source
- Anything that marks a monitor as "skip this run"
- Contradictions requiring reconciliation across sources

---

## Naming Conventions

- **Sources:** `Author-or-Org-SourceTitle-Year.md` (e.g. `BIS-WP1335-Tokenomics-Blockchain-Fragmentation.md`)
- **People:** Full name (e.g. `Hyun Song Shin.md`)
- **Concepts:** Title case, no date prefix (e.g. `Settlement economics.md`)
- **Archive prefix:** `_archived_`

---

## Frontmatter Requirements (Per Source)

Every source note must have:
```yaml
---
title: [Source Title]
type: source
nlm_id: [UUID from NotebookLM]
url: [Source URL]
organisation: [Author/Regulator/Publisher]
source_type: [report | paper | guidance | industry-note | etc]
year: [YYYY]
jurisdiction: [INTL | US | EU | UK | SG | etc]
domain: [array of domains — see schema.md]
doctrine: [array of doctrines — see schema.md]
instrument: [array of instruments — see schema.md]
created: [YYYY-MM-DD]
tags:
  - source
  - [topic tags]
wiki_indexed: [YYYY-MM-DDTHH:MM:SSZ]
status: [draft | indexed | verified]
---
```

See `99_Meta/schema.md` for complete schema.

---

## Monitor Channels

12 channels monitored automatically. State tracked in `99_Meta/wiki-tokenise/`:

1. **FSB** (Financial Stability Board) — crypto, digital assets, tokenisation policy
2. **IOSCO** (International Organization of Securities Commissions) — securities tokenisation
3. **BIS** (Bank for International Settlements) — working papers on settlement, stablecoins, tokenisation
4. **IMF** (International Monetary Fund) — tokenisation, CBDCs, financial stability
5. **HKMA** (Hong Kong Monetary Authority) — Asian tokenisation pilots
6. **ESMA** (European Securities and Markets Authority) — DLT pilot regime, MiCA
7. **MAS** (Monetary Authority of Singapore) — tokenisation projects (Project Guardian, Bloom)
8. **Fed** (US Federal Reserve) — tokenisation, settlement finality, financial stability
9. **UNIDROIT** (International Institute for Unification of Private Law) — DAPL, VCC Principles
10. **Wharton** (Wharton School) — fintech research, RWA tokenisation
11. **Invesco** — institutional tokenisation filings and announcements
12. **Private-sector press** — fintech, blockchain, RWA news outlets

Each channel has a `last_run_at` timestamp. Do not re-run a channel until 7 days have passed.

---

## Propagation Rules

| Event | Also update |
|---|---|
| New source ingested | Source Register + relevant topic area in 30_Areas/ + person note if author is new |
| Synthesis created | Daily log in `.remember/now.md` + relevant topic area links |
| Monitor completes | `99_Meta/wiki-tokenise/channel-name.md` with `last_run_at` and source count |
| Contradiction found | Flag in source note + note in 30_Areas/Synthesis — Contradictions.md |

---

## Key Regulators & Organisations to Know

| Org | Abbreviation | Focus | Notes |
|---|---|---|---|
| Financial Stability Board | FSB | Crypto/DLT policy | Reports to G20 |
| IOSCO | IOSCO | Securities regulation | 190 member jurisdictions |
| Bank for International Settlements | BIS | Central bank coordination, settlement | Hosts IOSCO, FSB secretariat |
| International Monetary Fund | IMF | Monetary policy, financial stability | Article IV tokenisation analysis |
| European Securities and Markets Authority | ESMA | EU securities law | DLT Pilot Regime administrator |
| Monetary Authority of Singapore | MAS | Asian fintech hub | Project Guardian, Bloom |
| US Federal Reserve | Fed | US monetary/banking policy | Settlement, interoperability concerns |
| UNIDROIT | UNIDROIT | Private law harmonisation | DAPL Principles, VCC Principles |
| Hong Kong Monetary Authority | HKMA | Asian tokenisation | Digital bond pilots, eHKD |

---

## Topics to Explore

Current synthesis gaps (potential next research areas):
- [ ] Tokenisation economics — cost-benefit across asset classes (settlement, intermediation, liquidity)
- [ ] Securities tokenisation — equity vs bonds vs funds; regulatory pathways
- [ ] Interoperability — cross-chain, cross-ledger settlement finality risks
- [ ] Legal frameworks — UNIDROIT DAPL vs ESMA DLT Pilot vs MAS approach comparison
- [ ] Stablecoin economics — validator costs, fragmentation, monetary singleness

---

## Do Not Touch

- `99_Meta/schema.md` — Vault schema (read only, update only if source types change)
- `.remember/` — Session memory (auto-managed)
- Monitor state files — Update only via `/obsidian-health` or monitor completion

---

## Synthesis Commands Available

Now that obsidian-second-brain is installed:

- `/obsidian-synthesize` — Scan sources for cross-source concepts and create synthesis notes
- `/obsidian-distill` — Extract core claims from a dense source
- `/obsidian-reconcile` — Find contradictions between sources
- `/obsidian-connect` — Link sources by regulator, author, jurisdiction
- `/obsidian-health` — Audit vault structure and orphaned notes
- `/research` — Fetch new sources and ingest automatically
- `/obsidian-board` — Create a kanban for a research project

See `~/.claude/obsidian-second-brain/SKILL.md` for full command reference.

---

*This file was generated by the obsidian-second-brain skill.*
*Regenerate with: "Claude, update my _CLAUDE.md"*
