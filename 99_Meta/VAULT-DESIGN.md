---
title: VAULT-DESIGN - wiki-tokenise
status: plan (proposal; awaiting user direction before implementation)
created: 2026-05-24
author: Claude (ULTRATHINK pass)
applies_to:
- 10_Sources structure
- 20_People + Institutions
- 30_Concepts
- 40_Domains
- 50_MOCs
- 90_Templates
- 99_Meta/wiki-tokenise (cron + protocol layer)
- .workspace (localhost browser artefacts)
- .obsidian (Minimal theme + Claudian + iA Fonts)
---

# Vault Design — wiki-tokenise

> The plan answers a single question. **What is the smallest set of mechanical commitments that lets one person, working alone, maintain an authoritative, queryable, comparable corpus on the tokenisation of real-world assets over many years, without the corpus drifting into industry boosterism or going stale?**

The answer borrows the architecture of the sibling vault `wiki-ai-thinkers` almost wholesale, extends it where the domain demands, and adds a view layer (Minimal theme + Claudian + iA Fonts) tuned to the practitioner reader.

The reasoning below is the *ULTRATHINK* pass. The deliverable is this file plus the live [schema.md](schema.md). Nothing in `.workspace/`, `.obsidian/`, or the watchlist orchestrator is implemented yet; everything is proposed and waiting.

---

## 0. Reading order

| Section | What it answers |
|---|---|
| **1. What we are porting and why** | Why `wiki-ai-thinkers` is the right template; what survives the port unchanged; what must change. |
| **2. Schema** | The controlled vocabulary that makes the rest mechanically possible. Lives in [schema.md](schema.md). |
| **3. Folder layout** | Already built (see [DIRECTORY-PROPOSAL.md](DIRECTORY-PROPOSAL.md)); diff against `wiki-ai-thinkers` noted here. |
| **4. People + Institutions** | Why we collapse both into `20_People/<slug>/` with a `kind` field instead of forking the folder. |
| **5. Weekly cron and the watchlist protocol** | The wiki-tokenise analogue of the wiki-thinkers orchestrator: channels not thinkers, regulatory feeds not biographies. |
| **6. Browser artefacts on localhost** | Five proposed artefacts: graph, convergence, timeline, realised-vs-projected, compare. |
| **7. View stack** | Obsidian Minimal theme + Claudian + iA Fonts; design tokens. |
| **8. Aesthetic commitments** | Applying the impeccable + frontend-design shared laws. |
| **9. Recommendations** | Fifteen observations and better-practice proposals. |
| **10. Implementation order** | The minimal sequence to ship Phase 1. |

---

## 1. What we are porting and why

`wiki-ai-thinkers` solves a structurally similar problem: build and maintain a queryable corpus of authoritative primary sources for a fast-moving knowledge domain, with a one-person operating budget. Five architectural commitments make it work.

> 1. **A locked schema.** Every note carries controlled YAML frontmatter. The schema is the contract between the vault content, the auto-MOC generator, and the browser artefacts.
> 2. **Decimal-prefix folders.** `00_` through `99_` and `100_`. Stable across renames, sortable everywhere, low cognitive overhead.
> 3. **Per-entity folders.** `20_People/<slug>/` for each person. `10_Sources/<Type>/<slug>/source.md` for each source. Every entity is a folder, every artefact is a file.
> 4. **A weekly cron-driven researcher subagent.** The roster file is the user-editable surface; the orchestrator dispatches per-row work; per-row state is persisted under `99_Meta/wiki-thinkers/state/`.
> 5. **Read-only browser artefacts on localhost.** A ~70-line Python stdlib server (`serve.py` + cross-platform launchers) serves hand-written HTML artefacts that read the vault directly via the File System Access API. IndexedDB persists the folder handle.

These five commitments port to `wiki-tokenise` without modification.

**What changes.** Three things.

1. **The unit of accumulation.** `wiki-ai-thinkers` accumulates *thinkers*. `wiki-tokenise` accumulates *legal, regulatory, market, and academic developments around a stable set of source channels*. The schema gains `institution` as a peer of `person`, and the watchlist replaces the roster.
2. **The matrix axis.** `wiki-ai-thinkers` projects thinkers × view-field. `wiki-tokenise` projects *jurisdiction × doctrine* (or *instrument × regime*). This produces a different second browser artefact: `convergence.html` instead of `positions.html`.
3. **The view stack.** `wiki-ai-thinkers` is text-only Source Serif 4. `wiki-tokenise` adopts Minimal theme + Claudian + iA Fonts. The aesthetic register stays *editorial-typographic*; the typography becomes iA Writer.

---

## 2. Schema

Defined in [schema.md](schema.md). Headlines:

> **`type`** — adds `institution` to the wiki-ai-thinkers enum, so BIS, BlackRock, and MAS sit in the same folder as named people without a parallel hierarchy.
>
> **`jurisdiction`** — first-class enum (`US`, `UK`, `EU`, `SG`, `HK`, `JP`, `KR`, `AE`, `CH`, `NZ`, `AU`, `CA`, `BR`, `IN`, `CN`, `INTL`, `MULTI`). Drives `convergence.html`.
>
> **`doctrine` / `instrument`** — paired enums for law sources and finance sources respectively. The convergence and realised-vs-projected artefacts read these directly.
>
> **`nlm_id`** — every source carries a NotebookLM source UUID where the source is in the notebook. The wiki round-trips to NotebookLM via this field.
>
> **`status: stub`** — added to the lifecycle enum so the 46 auto-generated NotebookLM stubs are queryable as such and surfaced for enrichment.

The schema is the *contract*. Every artefact, every protocol, every CSS snippet keys off it.

---

## 3. Folder layout

Already built per [DIRECTORY-PROPOSAL.md](DIRECTORY-PROPOSAL.md). Diff against `wiki-ai-thinkers`:

| Folder | `wiki-ai-thinkers` | `wiki-tokenise` | Note |
|---|---|---|---|
| `00_Inbox/` | present | present | identical |
| `10_Sources/` | grouped by type: `Paper/`, `Talk/`, `Article/`, `Video/` | grouped by source-provider type: `International-Agencies/`, `Central-Banks/`, `Commercial-Banks/`, `Academia/`, `Law-Regulation/`, `Think-Tanks/`, `Private-Sector/`, `Industry-Press/` | The tokenise grouping cuts by *who produced the source*, which matches how a practitioner cites it (and how the watchlist channels are named). |
| `100_HTML_Artefacts/` | present | omitted | per user direction. |
| `20_People/` | persons only | persons *and* institutions, via `kind` discriminator | See §4. |
| `30_Concepts/` | present | present | identical. |
| `40_Domains/` | thin scaffolding | populated: `Finance/`, `Law/`, `Examples/`, `Sub-Topic/` | The user's scope statement maps directly onto the spokes. |
| `50_MOCs/` | hand-curated | hand-curated, with three **cross-cutting** MOCs already written (Private-Law Convergence, Agent-Ledger Interface, Realised-vs-Projected) | The cross-cutting MOCs are the wiki's analytical spine. |
| `_wiki/` | auto-generated by `/wiki` skill | omitted; `50_MOCs/` absorbs the function | per user direction. |
| `.workspace/` | five files: `serve.{py,bat,sh}`, `vault-store.js`, `graph.html`, `positions.html` | proposed: same five files plus `convergence.html`, `timeline.html`, `realised.html`, `compare.html`, `index.html` | See §6. |
| `99_Meta/wiki-thinkers/` | orchestrator state | analogue: `99_Meta/wiki-tokenise/` with `watchlist.md`, `index.md`, `state/<channel>.json`, `queries/<channel>.md` | See §5. |

---

## 4. People and Institutions in one folder

The wiki-ai-thinkers vault has *people only*. Adapt or fork the layout?

> **Decision.** Keep `20_People/<slug>/` as the single folder. Add a `kind: person | institution` discriminator. Profile templates and the convergence artefact accept either.

The reasoning. The wiki's analytical units are *actors* — entities that issue sources, take positions, run pilots. Some are individuals (Larry Fink, Christine Lagarde, Hester Peirce). Most that matter for this domain are institutions (BIS, IMF, MAS, BlackRock, Securitize, Verra). Forking the folder splits a single class of entity by a property that doesn't change downstream behaviour. The discriminator field is enough.

Concrete consequence. The first dozen profile folders look like:

```
20_People/
  ├── BIS/
  │   └── profile.md             # kind: institution, role: standard-setter, jurisdiction: [INTL]
  ├── IMF/
  │   └── profile.md             # kind: institution, role: standard-setter, jurisdiction: [INTL]
  ├── MAS/
  │   └── profile.md             # kind: institution, role: central-bank, jurisdiction: [SG]
  ├── HKMA/
  │   └── profile.md             # kind: institution, role: central-bank, jurisdiction: [HK]
  ├── BlackRock/
  │   └── profile.md             # kind: institution, role: asset-manager, jurisdiction: [US]
  ├── Larry-Fink/
  │   └── profile.md             # kind: person, role: practitioner, jurisdiction: [US]
  ├── Agustin-Carstens/
  │   └── profile.md             # kind: person, role: policymaker, jurisdiction: [INTL]
  ├── Christine-Lagarde/
  │   └── profile.md             # kind: person, role: central-bank, jurisdiction: [EU]
  ├── UNIDROIT/
  │   └── profile.md             # kind: institution, role: standard-setter, jurisdiction: [INTL]
  ├── UK-Law-Commission/
  │   └── profile.md             # kind: institution, role: standard-setter, jurisdiction: [UK]
  └── ...
```

The graph artefact already handles both: a node is a node.

---

## 5. Weekly cron and the watchlist protocol

### 5.1 The shift from roster to watchlist

`wiki-ai-thinkers` runs a weekly job. Each iteration picks an *active* row from `roster.md`, spawns a `wiki-thinker-researcher` subagent, finds new primary-author work by that thinker, writes one `source.md` per accepted candidate, and stamps state.

`wiki-tokenise` runs an equivalent weekly job. Each iteration picks an *active* row from `watchlist.md`. The rows are not thinkers; they are **source channels** — regulatory bodies, market venues, academic feeds, registries, banks, and press outlets that emit material on tokenisation at a predictable cadence.

> **Watchlist channel ≠ entity.** An institution gets a `20_People/<slug>/profile.md`. A *channel* is a feed: a publication page, an arXiv tag, a registry policy area, a press-release stream. Some channels belong to entities (BIS Working Papers); some are cross-cutting (arXiv q-fin.GN).

### 5.2 Proposed channels for the pilot

Twelve channels are enough for a credible v1.

| Channel | Source | Cadence |
|---|---|---|
| `bis-working-papers` | bis.org/publ/work* | ~weekly |
| `imf-fintech-notes` | imf.org/en/Publications/fintech-notes | monthly |
| `fsb-publications` | fsb.org/publications | monthly |
| `iosco-publications` | iosco.org/library | monthly |
| `unidroit-news` | unidroit.org/news-and-events | irregular |
| `mas-news` | mas.gov.sg/news | weekly |
| `hkma-press` | hkma.gov.hk/eng/news-and-media | weekly |
| `fed-staff-papers` | federalreserve.gov/econres | monthly |
| `esma-news` | esma.europa.eu/news | weekly |
| `arxiv-q-fin-rwa` | arxiv `q-fin` filtered by `tokeni[sz]e` / `RWA` | weekly |
| `verra-policy` | verra.org/news | irregular |
| `ledger-insights` | ledgerinsights.com | daily-weekly |

### 5.3 Skill and subagent

Mirror the wiki-thinkers shape.

| Surface | Mirror | New name |
|---|---|---|
| Orchestrator skill | `~/.claude/skills/wiki-thinkers/SKILL.md` | `~/.claude/skills/wiki-tokenise/SKILL.md` |
| Researcher subagent | `~/.claude/agents/wiki-thinker-researcher.md` | `~/.claude/agents/wiki-tokenise-monitor.md` |
| Roster | `99_Meta/wiki-thinkers/roster.md` | `99_Meta/wiki-tokenise/watchlist.md` |
| Per-row state | `state/<slug>.json` | `state/<channel>.json` |
| Per-row queries | `queries/<slug>.md` | `queries/<channel>.md` |
| Status rollup | `index.md` | `index.md` |
| Status command | `/wiki-thinkers status` | `/wiki-tokenise status` |
| Run command | `/wiki-thinkers run <slug>` | `/wiki-tokenise run <channel>` |
| Refresh command | `/wiki-thinkers wiki-refresh` | `/wiki-tokenise wiki-refresh` |

### 5.4 The cron job

```text
# Windows Task Scheduler
Trigger:   Weekly, Sunday 02:00 NZ
Action:    PowerShell -ExecutionPolicy Bypass -File C:\Users\Simon\bin\wiki-tokenise-weekly.ps1
```

```powershell
# wiki-tokenise-weekly.ps1
$ErrorActionPreference = 'Stop'
$vault = 'C:\Users\Simon\Documents\wiki-tokenise'
$logDir = "$vault\99_Meta\wiki-tokenise\state\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$stamp = (Get-Date).ToString('yyyy-MM-ddTHH-mm-ss')
$log = "$logDir\weekly-$stamp.log"
claude -p "/wiki-tokenise weekly-refresh" --cwd $vault *>&1 | Tee-Object -FilePath $log
```

### 5.5 Pilot channel

> **BIS Working Papers.** Small enough to debug end-to-end, central enough that errors surface fast. Once the pilot is stable, promote the IMF channel, then MAS, HKMA, and the Federal Reserve.

### 5.6 Idempotence

The `wiki_hash` + `wiki_indexed` stamp on every note makes the cron safe to re-run. Hash unchanged → skip. Hash changed → reprocess. The watchlist subagent additionally writes a `nlm_last_sync` timestamp where the source has been mirrored into NotebookLM. Stamping is the difference between a maintenance budget that fits in a Sunday morning and one that doesn't.

---

## 6. Browser artefacts on localhost

### 6.1 Inheritance

Port these five files unchanged (rename `wiki-ai-thinkers` → `wiki-tokenise` where they reference the vault name; change `DB_NAME` in `vault-store.js`; change default port to **8766** so it does not clash with wiki-ai-thinkers on 8765):

- `serve.py`
- `serve.bat`
- `serve.sh`
- `vault-store.js`
- `graph.html` (the wiki-ai-thinkers graph already reads any vault that conforms to the schema)

### 6.2 Five new artefacts

Each artefact is one hand-written HTML file with CDN dependencies (D3, Alpine, js-yaml). No build step. All read the live vault via the File System Access API. All read-only.

> **`index.html`** — landing page. Five cards. One click to each artefact. The landing page is the only place users see the artefact set; the in-artefact header gives a short cross-link back.

> **`graph.html`** — force-directed graph of every wikilink. Carry over from wiki-ai-thinkers. Node colour by `type`; edge weight by link multiplicity. Hover for one-line summary; click for the side panel with frontmatter.

> **`convergence.html`** — the analytical centrepiece. Rows: jurisdictions (`US`, `UK`, `EU`, `SG`, `HK`, `JP`, ...). Columns: doctrines (`property-category`, `control`, `take-free-purchaser`, `secured-transactions`, `choice-of-law`, `insolvency`, `singleness-of-money`). Each cell: short text drawn from the matched source's body, plus a click-through to the source note. Replaces wiki-ai-thinkers `positions.html` as the second core artefact. Renders the **Private-Law Convergence** MOC as live data.

> **`timeline.html`** — events on a horizontal time axis. Lanes: `Regulation`, `Pilot`, `Academic`, `Incident`. Node size = `register_section` weight; node colour = `source_type`. Filterable by `jurisdiction`, `domain`, `year-range`. Surfaces narrative-arc questions: what came before MiCA? what came after the Verra suspension?

> **`realised.html`** — the honesty dashboard. Reads `99_Meta/forecasts.json` and `99_Meta/realised.json` (two small structured files, hand-maintained). Left side: bull-case forecasts (Standard Chartered USD 30.1T, BCG USD 16T, McKinsey USD 2-4T). Right side: realised AUM (BlackRock BUIDL USD 2.5B as at May 2026, tokenised-treasury sector USD 11B). Bottom: links to the sceptical sources (Oraclizer, Fed Financial Stability paper, Sonnenshein critique). Renders the **Realised-vs-Projected** MOC as live data.

> **`compare.html`** — generic side-by-side. Two pickers, each yielding a vault note. Renders frontmatter as aligned columns; renders body sections as parallel panels. Most useful for: MiCA vs GENIUS Act, UK Act vs UCC Article 12, BUIDL vs BENJI, BIS *Tokenisation Continuum* vs IMF *Tokenized Finance*. The generic comparison primitive turns the schema into a tool.

### 6.3 The vault-handle and IndexedDB

Adopt unchanged. Single `DB_NAME = 'wiki-tokenise'` in `vault-store.js`. First visit picks the folder; subsequent visits auto-reconnect if permission persists. Cross-vault contamination is impossible because each vault keys its own IndexedDB.

### 6.4 What the artefact set does *not* do

- **No writes.** Read-only is a constraint, not a default.
- **No Claude API calls.** All AI work goes through Claudian in Obsidian, or through Claude Desktop with the local MCP. The artefacts are pure browser code.
- **No build step.** Single hand-written HTML files. No node_modules.
- **No telemetry.**

---

## 7. View stack

### 7.1 Three layers

| Layer | Component | Source |
|---|---|---|
| Theme | **Obsidian Minimal** | https://github.com/kepano/obsidian-minimal |
| Plugin | **Claudian** (already installed on wiki-ai-thinkers as community plugin) | community plugins |
| Typography | **iA Fonts** (iA Writer Quattro, Duo, Mono) | https://github.com/iaolo/iA-Fonts |

### 7.2 Installation

1. **Minimal theme.** Install via Obsidian → Settings → Appearance → Themes → Browse → Minimal. Or `git clone` into `.obsidian/themes/minimal/`.
2. **Claudian.** Already installed on the sibling vault. Copy `.obsidian/plugins/claudian/` from `wiki-ai-thinkers` into `wiki-tokenise/.obsidian/plugins/claudian/`. Add `"claudian"` to `community-plugins.json`.
3. **iA Fonts.** `git clone https://github.com/iaolo/iA-Fonts.git`. Install the `.ttf` files at the OS level (Windows: right-click → Install for all users). Also copy `iAWriterQuattroV.ttf`, `iAWriterDuoV.ttf`, `iAWriterMonoV.ttf` into `80_Attachments/fonts/` so the browser artefacts can self-host them (no CDN dependency for typography). Obsidian Appearance → Font: set Text to *iA Writer Quattro V*, Monospace to *iA Writer Mono V*.

### 7.3 CSS snippet

A single `.obsidian/snippets/wiki-tokenise.css` snippet enforces the design tokens shared between Obsidian and the browser artefacts. Tokens:

```css
:root {
  /* Tinted-neutral palette - never #000 / #fff */
  --bg-paper:    oklch(98.5% 0.005 80);    /* warm off-white */
  --bg-page:    oklch(96%   0.008 80);    /* surface */
  --ink-strong:  oklch(20%   0.01  260);   /* near-black, tinted blue-grey */
  --ink-mid:    oklch(40%   0.01  260);
  --ink-soft:    oklch(60%   0.01  260);
  --accent:    oklch(38%   0.12  25);    /* oxblood / deep burgundy */
  --accent-soft: oklch(78%   0.06  25);
  --rule:      oklch(88%   0.01  260);

  /* Type scale - perfect-fourth (1.333) */
  --t-base: 16px; --t-2: 1.333rem; --t-3: 1.777rem; --t-4: 2.369rem;

  /* Spacing - 4px scale with rhythm variation */
  --s-1: 4px; --s-2: 8px; --s-3: 12px; --s-4: 16px;
  --s-5: 24px; --s-6: 40px; --s-7: 64px;

  /* Type stack */
  --font-body: 'iA Writer Quattro V', 'iA Writer Quattro', ui-sans-serif, system-ui;
  --font-display: 'iA Writer Duo V', 'iA Writer Duo', ui-sans-serif, system-ui;
  --font-mono:  'iA Writer Mono V',  'iA Writer Mono',  ui-monospace, SFMono-Regular;
}
```

Body line length capped at 70ch. No animations on layout properties. No bounce, no elastic.

### 7.4 What the snippet does in Obsidian

Tunes Minimal's defaults to the token set: warmer background, iA Quattro body, oxblood accent for active states (the [[wikilink]] hover, the inline tag highlight, the current-line gutter). The same tokens are inlined as `:root` at the top of every `.workspace/*.html` artefact so the visual register is identical between editor and browser.

---

## 8. Aesthetic commitments

### 8.1 The scene sentence

> **Practitioner — a New Zealand lawyer advising on a tokenised real-estate deal — at her desk during office hours, on a 27-inch monitor, between two client meetings, needs to find where the UK Property (Digital Assets etc) Act 2025 lands on *direct vs indirect tokenisation* in under 30 seconds.**

That sentence forces:

- **Light theme by default.** Office light. Quick reference. Not a 2am SRE dark cave.
- **Tinted-neutral background.** Reduce eye-strain over a long day. Refuse the SaaS-cream-on-pure-white reflex.
- **Editorial-typographic register.** iA Writer is *itself* the visual identity. No decorative chrome.

### 8.2 The category-reflex check

- **First-order reflex (finance domain → navy + gold).** Refused. The palette is warm cream + oxblood + tinted ink. No navy, no gold.
- **Second-order reflex (finance-not-navy → terminal-dark-mode).** Refused. Light + warm + serif/iA-mono pairing.

### 8.3 The absolute bans (impeccable)

Applied. The artefacts will not feature:

- Side-stripe borders on cards or list items.
- Gradient text.
- Decorative glassmorphism.
- The hero-metric template (big number, small label, supporting stats).
- Identical card grids.
- Modals as first thought (use inline disclosure).

### 8.4 Copy

Per the user's global drafting standards. NZ English. Active voice. No adverbs. Sentences under 20 words. No em dashes. Positive form. Concrete and specific.

The standards apply to every vault note, every MOC, every artefact label.

### 8.5 The AI slop test

Run on every artefact before commit. Could someone say *"AI made that"* without doubt? If yes, rework.

---

## 9. Recommendations and observations

Fifteen, in priority order.

> **1. Adopt the wiki-ai-thinkers architecture wholesale where it ports.** Five commitments (locked schema, decimal folders, per-entity folders, weekly cron, browser artefacts) survive the port intact. Re-inventing them costs days and yields nothing.

> **2. Discriminate person vs institution with a field, not a folder.** The wiki's analytical units are *actors*. Forking the folder splits the class on a property that does not change downstream behaviour.

> **3. Make jurisdiction a first-class enum.** It is the axis on which the Private-Law Convergence cross-cutting MOC operates, and it is the field that drives `convergence.html`. Without it, the most analytically distinctive artefact in the proposed set cannot be built.

> **4. Make `nlm_id` a first-class field on every source.** The NotebookLM round-trip is the cheapest way to enrich the 46 stubs. The bridge file at [NotebookLM-bridge.md](NotebookLM-bridge.md) is the operational analogue of `wiki-thinkers/state/`. Without `nlm_id`, every enrichment is a manual lookup.

> **5. Make `status: stub` a permanent lifecycle state.** Auto-generation will keep producing stubs. They must be queryable as such. Otherwise the enrichment backlog is invisible.

> **6. Build the watchlist instead of a thinker roster.** The unit of accumulation is *new developments on stable channels*, not *new work by a stable cast*. Twelve channels are enough for v1; promote the pilot from BIS first.

> **7. Adopt 2,026 commitment: a "Realised vs Projected" data layer.** A pair of small JSON files at `99_Meta/forecasts.json` and `99_Meta/realised.json`. The artefact `realised.html` reads both. The wiki stays honest without manual review-cycle upkeep. The Standard Chartered USD 30.1T forecast and the BlackRock BUIDL USD 2.5B AUM live in the same view, every week.

> **8. Choose port 8766 for serve.py, not 8765.** Avoids head-on collision with wiki-ai-thinkers when both vaults are open.

> **9. Self-host iA Fonts in `80_Attachments/fonts/`.** The browser artefacts should not depend on a CDN for typography. Bundling the `.ttf` files is one-time cost; CDN flakiness is recurring cost.

> **10. Mirror the Claudian plugin install.** Copy `.obsidian/plugins/claudian/` from `wiki-ai-thinkers` rather than re-downloading. Verify version parity before activating.

> **11. Adopt the wiki-ai-thinkers dual licence.** CC BY 4.0 for content, MIT for code. The licence headers belong in `LICENSE-content.txt` and `LICENSE` respectively. Even if `wiki-tokenise` stays private now, the licence-from-day-one discipline avoids retrofitting later.

> **12. Treat the SOURCE-REGISTER as the master annotated bibliography.** The auto-generated per-source stubs are *index entries* with frontmatter. The annotated paragraph belongs in the register. Two artefacts, two purposes; no duplication.

> **13. Add an Obsidian Bases view called "Stubs to enrich".** Bases is already enabled by default in current Obsidian. The view filters every note with `status: stub` and sorts by `nlm_id` presence. The enrichment backlog becomes a one-click query.

> **14. Pin the schema in Templater.** Every template at `90_Templates/` should refuse to render fields outside the controlled vocabulary. Drift starts where the schema stops being enforced.

> **15. Defer the public-publishing decision.** The wiki-ai-thinkers vault is public on GitHub. The wiki-tokenise vault probably should not be, at least at v1: it touches client-relevant areas of law. The licence model and architecture should remain *publish-ready* (so it could ship at v2), but the actual publication decision waits until the corpus stabilises and is auditable.

### 9.1 Cross-cutting observation

The single biggest analytical advantage of the wiki-tokenise corpus over what one person could carry in their head is **the convergence matrix**. Three jurisdictions (US, UK, EU) and the international standard-setter (UNIDROIT) have converged on functionally similar regimes for tokenised property between 2022 and 2025, by structurally different doctrines. No single source explains the convergence; the wiki *is* the explanation. `convergence.html` is the artefact that surfaces this. It is worth more than any other proposed page.

---

## 10. Implementation order

A minimal phase-one ship list. Each phase is one work session.

### Phase 1 — Foundations (already done)

- [x] Schema written ([schema.md](schema.md)).
- [x] Folder tree built ([DIRECTORY-PROPOSAL.md](DIRECTORY-PROPOSAL.md) realised).
- [x] 46 NotebookLM source stubs generated.
- [x] 12 MOCs scaffolded.
- [x] 4 templates in place.
- [x] [SOURCE-REGISTER.md](../10_Sources/SOURCE-REGISTER.md) populated.

### Phase 2 — View stack (proposed; awaiting direction)

- [ ] Install Obsidian Minimal theme.
- [ ] Copy Claudian and realclaudian plugins from sibling vault; add to `community-plugins.json`.
- [ ] Self-host iA Fonts in `80_Attachments/fonts/`; install at OS level.
- [ ] Write `.obsidian/snippets/wiki-tokenise.css` with the design tokens.
- [ ] Set Obsidian Appearance: Minimal theme + iA Writer Quattro V body + iA Writer Mono V code.

### Phase 3 — Localhost browser artefacts (proposed)

- [ ] Create `.workspace/` folder; copy `serve.py`, `serve.bat`, `serve.sh`, `vault-store.js` from `wiki-ai-thinkers`; rename `DB_NAME = 'wiki-tokenise'`; default port 8766.
- [ ] Port `graph.html` unchanged (schema parity).
- [ ] Build `index.html` (landing).
- [ ] Build `convergence.html` (the analytical centrepiece — see §6.2).
- [ ] Build `timeline.html`.
- [ ] Build `realised.html` (requires `99_Meta/forecasts.json` + `99_Meta/realised.json`).
- [ ] Build `compare.html`.
- [ ] Write `START_HERE.html` at vault root with launch instructions per OS.

### Phase 4 — Watchlist orchestrator (proposed)

- [ ] Author `~/.claude/skills/wiki-tokenise/SKILL.md` mirroring wiki-thinkers shape.
- [ ] Author `~/.claude/agents/wiki-tokenise-monitor.md` subagent.
- [ ] Create `99_Meta/wiki-tokenise/watchlist.md` populated with the twelve channels in §5.2.
- [ ] Wire BIS Working Papers as pilot channel; run once manually to validate.
- [ ] Add Windows Task Scheduler entry per §5.4.

### Phase 5 — Population (continuous)

- [ ] Enrich the 46 NotebookLM stubs via `source_describe` round-trip, populating `## Annotation` sections.
- [ ] Create the first dozen `20_People/<slug>/profile.md` records (BIS, IMF, MAS, HKMA, BlackRock, Larry Fink, Agustin Carstens, Christine Lagarde, UNIDROIT, UK Law Commission, Hester Peirce, Securitize).
- [ ] Populate `30_Concepts/` with the atomic terms named in the twelve MOCs.
- [ ] Populate `40_Domains/` spoke notes (one per instrument, statute, registry, platform).

---

## 11. Open questions for the next prompt

1. **Phase 2 — install the view stack now?** The decisions are made; only the install remains.
2. **Phase 3 — build all five artefacts in one session, or only `index.html` + `graph.html` + `convergence.html` first?**
3. **Phase 4 — author the wiki-tokenise orchestrator skill now, or wait until the artefact set is stable?**
4. **Public publication.** Stay private at v1, or set up GitHub from day one with the dual licence?
5. **NotebookLM stub enrichment.** Batch via `source_describe` (auto-summary) or hand-write each annotation?

Awaiting your direction.

---

## Provenance

Built on 2026-05-24 by deep ingestion of `wiki-ai-thinkers` (README, `99_Meta/schema.md`, `.workspace/README.md`, `serve.py`, `vault-store.js`, `90_Templates/*.md`, `99_Meta/wiki-thinkers/{README,roster}.md`, `.obsidian/community-plugins.json`, `.obsidian/core-plugins.json`). Synthesis applied the impeccable skill's shared design laws, the frontend-design skill's aesthetic guidance, the user's global drafting standards (NZ English, Hemingway, Strunk), and the scholarly skill's typographic-scaffolding principles. No external implementation work performed in this turn; the plan awaits direction.
