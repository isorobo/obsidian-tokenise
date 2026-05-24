---
type: meta
title: Vault Schema and Controlled Vocabulary
status: permanent
created: 2026-05-24
updated: 2026-05-24
topic:
- topic/meta
wiki_role: meta
---

# Vault Schema and Controlled Vocabulary

This file defines the controlled frontmatter vocabulary used across **wiki-tokenise**. Every note conforms to these fields. New values require an update here before use.

The schema is a deliberate extension of the sibling `wiki-ai-thinkers` schema. The extensions account for two facts that distinguish this domain: (i) institutions matter at least as much as individuals (BIS, BlackRock, MAS), and (ii) jurisdiction is a first-class analytical axis.

---

## 1. Folder Purpose

| Folder | Purpose |
|---|---|
| `00_Inbox/` | Unprocessed captures awaiting triage. |
| `10_Sources/` | One note per primary source, grouped by source-type subfolder. |
| `10_Sources/PDFs/` | Raw binary downloads, mirroring the source-type subfolders. Excluded from version control. |
| `10_Sources/NotebookLM-Exports/` | NotebookLM audio, slide, and brief artefacts. |
| `20_People/<slug>/` | One folder per person *or* institution. Holds `profile.md` and optional `positions.md`, `timeline.md`. |
| `30_Concepts/` | Atomic concept and theme pages. |
| `40_Domains/` | Domain spokes: `Finance/`, `Law/`, `Examples/{Carbon-Credits,Real-Estate,Property-Rights}/`, `Sub-Topic/{Stablecoins,Agentic-AI-Trading,Blockchain-Settlement}/`. |
| `50_MOCs/` | Maps of Content. Nine domain MOCs, three cross-cutting MOCs. |
| `60_Drafts/` | Work-in-progress essays, reports, deep-research outputs. |
| `70_Research/` | Active research threads. One folder per thread. |
| `80_Attachments/` | Images, diagrams, self-hosted fonts. |
| `90_Templates/` | Templater-compatible frontmatter and body templates. |
| `99_Meta/` | Vault infrastructure: this schema, the directory proposal, the NotebookLM bridge, the watchlist for the weekly cron, `wiki-tokenise/` orchestrator state. |
| `.workspace/` | Browser artefacts. Read-only. Local-server-only. |

---

## 2. Frontmatter Fields

### 2.1 Required on every note

| Field | Enum values | Notes |
|---|---|---|
| `type` | `source`, `person`, `institution`, `concept`, `moc`, `draft`, `question`, `timeline`, `position`, `meta` | Governs which template applied. |
| `status` | `inbox`, `stub`, `draft`, `review`, `permanent`, `archived` | Lifecycle state. `stub` exists for auto-generated source notes pending enrichment. |
| `created` | ISO date (`YYYY-MM-DD`) | Creation date. |
| `tags` | list of free strings | Folksonomy; not controlled. |

### 2.2 Person and Institution notes

The same folder layout (`20_People/<slug>/`) holds both. The `kind` field discriminates.

| Field | Enum or format | Notes |
|---|---|---|
| `name` | free string | Display name. |
| `slug` | kebab-case | Matches folder name. |
| `kind` | `person`, `institution` | Required. |
| `role` | see 2.5 | Primary role. |
| `jurisdiction` | list of jurisdiction enums (2.6) | Where the actor operates or has effect. |
| `domain` | list of domain enums (2.7) | Topical focus. |
| `affiliations` | list of strings | Current and past. |
| `position_view` | free string | One-line stated position. Optional; used for matrix views. |
| `key_sources` | list of wikilinks | Links to source notes authored by, issued by, or about this entity. |
| `nlm_id` | NotebookLM source UUID | Where an entity's primary output is itself a NotebookLM source. Optional. |

### 2.3 Source notes

| Field | Enum or format | Notes |
|---|---|---|
| `title` | free string | Work title. |
| `authors` | list of strings | Author or issuer names. |
| `organisation` | free string | Issuing body where distinct from authors (e.g. *BIS* for a Working Paper). |
| `source_type` | `statute`, `regulation`, `guidance`, `report`, `paper`, `press-release`, `industry-note`, `speech`, `testimony`, `dataset`, `pilot-doc`, `book`, `blog`, `interview` | Required. |
| `venue` | free string | Conference, journal, registry, podcast, site. |
| `year` | integer | Publication year. |
| `date_published` | ISO date | Where day-granularity matters (e.g. statute commencement). |
| `url` | URL | Canonical link. `TBD` permitted at stub stage. |
| `doi` | string | Optional. |
| `jurisdiction` | list of jurisdiction enums (2.6) | Where the source has legal or regulatory effect, or where it was issued. |
| `domain` | list of domain enums (2.7) | Topical scope. |
| `doctrine` | list of doctrine enums (2.8) | Where relevant (law sources). |
| `instrument` | list of instrument enums (2.9) | Where relevant (finance sources). |
| `register_section` | string | Cross-reference to the section of `10_Sources/SOURCE-REGISTER.md` that annotates this source. |
| `nlm_id` | NotebookLM source UUID | Round-trip handle for `notebook_query` and `source_describe`. |
| `nlm_skip` | bool | If true, the source is excluded from NotebookLM exports. Default false. |

### 2.4 Concept notes

| Field | Enum or format | Notes |
|---|---|---|
| `name` | free string | Display name. |
| `slug` | kebab-case | Matches filename. |
| `domain` | list of domain enums (2.7) | |
| `synonyms` | list of strings | Aliases the wiki should resolve to this concept. |
| `defined_in` | wikilink | Source that establishes the canonical definition. |
| `parent_concept` | wikilink | Where the concept is a sub-type. |
| `related_concepts` | list of wikilinks | |

### 2.5 Role enum

`regulator`, `central-bank`, `commercial-bank`, `investment-bank`, `asset-manager`, `infrastructure-provider`, `exchange`, `custodian`, `issuer`, `platform`, `registry`, `standard-setter`, `think-tank`, `academic`, `practitioner`, `policymaker`, `critic`, `journalist`, `lawyer`, `consultant`

### 2.6 Jurisdiction enum

`US`, `UK`, `EU`, `SG`, `HK`, `JP`, `KR`, `AE`, `CH`, `NZ`, `AU`, `CA`, `BR`, `IN`, `CN`, `INTL` (international / cross-border / standard-setter), `MULTI` (true cross-jurisdictional with no single home).

### 2.7 Domain enum

`finance`, `law`, `securities-law`, `private-law`, `international-private-law`, `monetary-policy`, `market-structure`, `market-infrastructure`, `settlement`, `cross-border-payments`, `carbon-credits`, `environmental-markets`, `real-estate`, `property-rights`, `land-registry`, `stablecoins`, `tokenised-deposits`, `cbdc`, `agentic-ai`, `llm-trading`, `blockchain-settlement`, `defi`, `ai-governance`, `taxation`.

### 2.8 Doctrine enum (law sources)

`property-category`, `control`, `take-free-purchaser`, `secured-transactions`, `choice-of-law`, `insolvency`, `custody`, `intermediation`, `transfer`, `singleness-of-money`, `prospectus`, `mifid-equivalence`, `licensing`, `aml-cft`, `market-abuse`, `consumer-protection`, `disclosure`, `reserve-requirements`.

### 2.9 Instrument enum (finance sources)

`tokenised-fund`, `tokenised-bond`, `tokenised-deposit`, `tokenised-treasury`, `tokenised-money-market-fund`, `tokenised-private-credit`, `tokenised-equity`, `tokenised-real-estate`, `tokenised-carbon-credit`, `tokenised-commodity`, `stablecoin-fiat`, `stablecoin-rwa-backed`, `stablecoin-algorithmic`, `cbdc-wholesale`, `cbdc-retail`, `e-money-token`, `asset-referenced-token`, `nft`, `security-token`.

### 2.10 Position notes (for instruments and proposed regimes)

| Field | Enum or format | Notes |
|---|---|---|
| `claim` | free string | The position itself. |
| `source` | wikilink | Source establishing the position. |
| `jurisdiction` | jurisdiction enum (2.6) | |
| `doctrinal_basis` | doctrine enum (2.8) | |
| `status` | `operative`, `proposed`, `suspended`, `rejected`, `superseded` | |
| `as_of_date` | ISO date | When the position was last verified. |

### 2.11 Auto-generated stamps

Set by the `/wiki` skill and the `/wiki-tokenise` orchestrator. Do not edit by hand.

| Field | Notes |
|---|---|
| `wiki_indexed` | ISO timestamp of last `/wiki apply` pass. |
| `wiki_hash` | SHA-256 of the normalised note body. Drives idempotent re-runs. |
| `wiki_role` | `wiki`, `meta`, `index`, `moc`, `source`, `person`, `institution`, `concept`. |
| `nlm_last_sync` | ISO timestamp of last NotebookLM round-trip. |
| `watchlist_channel` | Slug of the watchlist channel that surfaced this source (where applicable). |

---

## 3. Linking Conventions

- People and institutions: `[[20_People/<slug>/profile|Display Name]]`.
- Sources: `[[10_Sources/<Category>/<Slug>|Short Title]]`.
- Concepts: `[[<Concept-Slug>]]`.
- MOCs: `[[MOC - <Name>]]`.
- Every source note links to at least one person, institution, or concept.
- Every person and institution profile links to at least one source.
- MOCs collect wikilinks, not transcluded content.

---

## 4. Browser-artefact Contract

The browser artefacts under `.workspace/` (see [VAULT-DESIGN.md](VAULT-DESIGN.md) §6) depend on the following fields. Any rename or removal here breaks the artefacts.

| Artefact | Required fields |
|---|---|
| `graph.html` | `type`, `title` (sources), `name` (people/institutions), wikilinks in body. |
| `convergence.html` | `type=source`, `jurisdiction`, `doctrine`, `register_section`. |
| `timeline.html` | `type=source`, `year` or `date_published`, `source_type`. |
| `realised.html` | `type=position`, `claim`, `as_of_date`, `source`. |
| `compare.html` | All frontmatter fields on the two compared notes. |

---

## 5. Pilot Channel

The pilot for the watchlist-driven weekly refresh (see [VAULT-DESIGN.md](VAULT-DESIGN.md) §5) is the **Bank for International Settlements**. Its output channel is small enough to debug end-to-end and central enough that errors surface quickly. Once stable, the watchlist promotes to the IMF, then to MAS / HKMA / Federal Reserve.

End of schema.
