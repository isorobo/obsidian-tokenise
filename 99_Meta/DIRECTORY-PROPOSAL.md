---
title: Directory Proposal — wiki-tokenise
status: proposal (awaiting user decision; no implementation)
created: 2026-05-24
author: Claude (drafting)
---

# Directory Proposal — wiki-tokenise

> **Reading order.** Section 1 states the design constraints the proposal must satisfy. Section 2 is the proposed tree. Section 3 walks each top-level folder and explains *why*. Section 4 lists the **MOCs** the wiki will host. Section 5 surfaces the open decisions for the next prompt.

---

## 1. Design constraints

The structure has to absorb four things at once. State them up front so the tree below can be evaluated against them.

1. **Two readers.** A *practitioner* (lawyer, banker, asset manager) who wants the right answer in two clicks. A *researcher* (scholar, policy analyst) who wants the source corpus organised by argument. The tree must serve both without forcing a duplicate hierarchy.

2. **Source plurality.** Forty-six NotebookLM sources, a 13-source carbon report already in the vault, plus future PDFs, NotebookLM exports, and the user's own drafts. The tree must give each artefact a clean home that does **not** depend on which medium it arrived in.

3. **Cross-cutting threads.** Three patterns cut across the domain categories — *private-law convergence*, *agent–ledger interface*, *realised-vs-projected*. The tree must surface these as **MOCs**, per the user's note, rather than burying them in any single category folder.

4. **Karpathy-style wiki precedent.** The sibling vault `wiki-ai-thinkers` already uses the decimal-prefix convention (`10_Sources`, `20_People`, `50_MOCs`, `90_Templates`, `99_Meta`). Convergence with that convention reduces switching cost and lets the `/wiki` MOC-builder skill run on this vault without modification.

> **Design rule.** *One artefact, one home; many references.* Each note lives in exactly one folder. MOCs and concepts link to it. No duplication, no symlinks, no parallel hierarchies.

---

## 2. Proposed tree

```
wiki-tokenise/
│
├─ 00_Inbox/                       # capture-first; triage weekly
│   └─ README.md
│
├─ 10_Sources/                     # one note per primary source
│   ├─ SOURCE-REGISTER.md          # already exists — the master index
│   ├─ International-Agencies/     # BIS, IMF, FSB, IOSCO, OECD, World Bank, UNIDROIT
│   ├─ Central-Banks/              # MAS, HKMA, Fed, ECB, BoE, Banque de France
│   ├─ Commercial-Banks/           # Standard Chartered, JPMorgan, HSBC, Citi, BNY
│   ├─ Academia/                   # peer-reviewed papers, arXiv preprints
│   ├─ Law-Regulation/             # statutes, regulations, official guidance
│   ├─ Think-Tanks/                # Atlantic Council, Brookings, Carnegie, RMI
│   ├─ Private-Sector/             # BlackRock, Franklin Templeton, Securitize, Chainlink
│   ├─ Industry-Press/             # Ledger Insights, CoinDesk, FT, Caproasia
│   ├─ NotebookLM-Exports/         # NotebookLM artefacts (audio, video, briefs)
│   └─ PDFs/                       # raw downloads — mirror of folder names above
│
├─ 20_People/                      # one note per author / principal
│   ├─ Carstens-Agustin.md
│   ├─ Nilekani-Nandan.md
│   ├─ Larry-Fink.md
│   ├─ Catalini-Christian.md
│   ├─ Gorton-Gary.md
│   ├─ de-Soto-Hernando.md
│   └─ ... (extracted from sources as the wiki matures)
│
├─ 30_Concepts/                    # one note per atomic concept
│   ├─ Tokenisation.md
│   ├─ Unified-Ledger.md
│   ├─ Tokenised-Deposit.md
│   ├─ Stablecoin.md
│   ├─ Asset-Referenced-Token.md
│   ├─ Controllable-Electronic-Record.md   # UCC Art 12
│   ├─ Third-Category-Property.md          # UK
│   ├─ Atomic-Settlement.md
│   ├─ Programmable-Money.md
│   ├─ MEV.md
│   ├─ Transaction-Intent-Schema.md        # from arXiv 2601.04583
│   ├─ Account-Abstraction.md
│   ├─ MPC.md
│   ├─ Corresponding-Adjustment.md         # Paris Art 6
│   ├─ Buffer-Pool.md                       # carbon
│   └─ ...
│
├─ 40_Domains/                     # the four spokes of the wiki
│   ├─ Finance/
│   │   ├─ Tokenised-Funds.md
│   │   ├─ Tokenised-Bonds.md
│   │   ├─ Tokenised-Deposits.md
│   │   ├─ Tokenised-Treasuries.md          # BUIDL, BENJI
│   │   └─ ...
│   ├─ Law/
│   │   ├─ UCC-Article-12.md
│   │   ├─ Property-Digital-Assets-Act-2025-UK.md
│   │   ├─ UNIDROIT-Principles-2023.md
│   │   ├─ MiCA.md
│   │   ├─ DLT-Pilot-Regime.md
│   │   ├─ GENIUS-Act.md
│   │   ├─ Singapore-PSA.md
│   │   ├─ HK-Stablecoins-Ordinance.md
│   │   └─ ...
│   ├─ Examples/
│   │   ├─ Carbon-Credits/
│   │   │   ├─ Toucan.md
│   │   │   ├─ KlimaDAO.md
│   │   │   ├─ ACX.md
│   │   │   ├─ Climate-Impact-X.md
│   │   │   ├─ Verra-2022-Suspension.md
│   │   │   └─ ...
│   │   ├─ Real-Estate/
│   │   │   ├─ RealT.md
│   │   │   ├─ Propy.md
│   │   │   ├─ HSBC-Marketnode-pilot.md
│   │   │   └─ ...
│   │   └─ Property-Rights/
│   │       ├─ Georgia-Bitfury.md
│   │       ├─ Sweden-Lantmateriet.md
│   │       └─ Ghana-Honduras-pilots.md
│   └─ Sub-Topic/
│       ├─ Stablecoins/
│       │   ├─ USDC.md
│       │   ├─ USDT.md
│       │   ├─ PYUSD.md
│       │   ├─ EURCV.md
│       │   ├─ RWA-Stablecoins.md
│       │   └─ ...
│       ├─ Agentic-AI-Trading/
│       │   ├─ x402.md
│       │   ├─ Bedrock-AgentCore.md
│       │   ├─ Agent-Economy-arXiv.md
│       │   └─ Autonomous-Agents-Blockchain-arXiv.md
│       └─ Blockchain-Settlement/
│           ├─ Ethereum.md
│           ├─ Canton-Network.md
│           ├─ Polygon.md
│           ├─ Avalanche-Subnets.md
│           └─ Project-Agora.md
│
├─ 50_MOCs/                        # cross-cutting Maps of Content
│   ├─ MOC - Root.md
│   ├─ MOC - Finance.md
│   ├─ MOC - Law.md
│   ├─ MOC - Carbon-Credits.md
│   ├─ MOC - Real-Estate.md
│   ├─ MOC - Property-Rights.md
│   ├─ MOC - Stablecoins.md
│   ├─ MOC - Agentic-AI.md
│   ├─ MOC - Blockchain-Settlement.md
│   │
│   │   --- the three CROSS-CUTTING MOCs you flagged ---
│   ├─ MOC - Private-Law-Convergence.md   # UCC Art 12 ↔ UK Act ↔ UNIDROIT ↔ civil law
│   ├─ MOC - Agent-Ledger-Interface.md    # finance/law core ↔ agentic-AI rim
│   └─ MOC - Realised-vs-Projected.md     # bull-case sizing vs Oraclizer scepticism
│
├─ 60_Drafts/                      # work-in-progress writing
│   ├─ Carbon-Credit-Tokenisation-Report-2026-04-02.md   # the existing deep-research report
│   ├─ Carbon-Credit-Tokenisation-Report-2026-04-02.html
│   └─ ...
│
├─ 70_Research/                    # one folder per active research thread
│   └─ ...                          # e.g. "MiCA-Article-48-deep-dive"
│
├─ 80_Attachments/                 # images, screenshots, diagrams
│
├─ 90_Templates/                   # Obsidian / Templater templates
│   ├─ template - source.md
│   ├─ template - concept.md
│   ├─ template - person.md
│   └─ template - MOC.md
│
├─ 99_Meta/                        # vault administration
│   ├─ inception.md
│   ├─ DIRECTORY-PROPOSAL.md       # this file
│   ├─ wiki-config.yaml
│   └─ NotebookLM-bridge.md        # notebook UUID + sync log
│
└─ README.md
```

---

## 3. Folder-by-folder rationale

### 3.1 `10_Sources/` — source notes, not source files

> **Design choice.** Source *notes* live here. Source *files* (PDFs, audio) live in `10_Sources/PDFs/` and `10_Sources/NotebookLM-Exports/`.

Each source gets a thin note with frontmatter (citation, URL, NLM ID, date accessed, type, jurisdiction) and a 100–300 word annotation. The note *talks about* the source; the file *is* the source. This lets you:

- Link to a source from many concepts without dragging a PDF around.
- Run the `/wiki` MOC-builder over `.md` notes without it choking on binaries.
- Keep the `SOURCE-REGISTER.md` master index in sync with the per-source notes (the register is the index of contents; each per-source note is a chapter).

### 3.2 `20_People/` — authors as first-class entities

The sibling vault `wiki-ai-thinkers` uses this convention. For `wiki-tokenise` it pays the same dividend: when Carstens publishes again, his note already exists; when Catalini's UCC-Article-12 analysis lands, you link rather than reshelve.

### 3.3 `30_Concepts/` — atomic vocabulary

> **Karpathy principle.** *Compress the vocabulary, expand the graph.* Each technical term — `Unified Ledger`, `Controllable Electronic Record`, `Transaction Intent Schema` — gets one note. Every other note links to it.

This is the engine of the wiki. The number of *concepts* grows logarithmically; the number of *links* grows linearly. When the corpus doubles, the vocabulary barely moves.

### 3.4 `40_Domains/` — the wiki's four spokes mirror its scope

The user's scope statement names the spokes: **finance + law + examples (carbon / real estate / property rights) + sub-topic (stablecoins / agentic AI / blockchain)**. The folder structure mirrors that statement literally. No translation cost between the scope-as-stated and the directory-as-rendered.

> *Why nest `Sub-Topic/` rather than promoting it?* Because the user named it a *sub-topic*, not a fifth spoke. Honouring that hierarchy makes the implicit *load-bearing* relationship visible: stablecoins, agentic AI, and settlement chains *support* the four primary domains; they are not parallel to them.

### 3.5 `50_MOCs/` — Maps of Content, including the three cross-cutting ones

The MOCs are the wiki's **navigational substrate**. Each MOC is a curated index page: not a category, but a *route*. The three you flagged join the standard domain MOCs:

> **MOC — Private-Law Convergence.** Threads the US (UCC Article 12), UK (Property (Digital Assets etc) Act 2025), international (UNIDROIT Principles 2023), and civil-law (*Absolute Rights and Claims*) doctrines. The MOC's job: show that three jurisdictions converge on functionally similar regimes by structurally different routes.

> **MOC — Agent–Ledger Interface.** Bridges the *finance/law core* and the *agentic-AI rim*. Anchored by arXiv 2601.04583, *The Agent Economy*, Coinbase x402, AWS AgentCore. Its job: hold the stochastic-vs-deterministic tension and the security taxonomy in one place.

> **MOC — Realised vs Projected.** Deploys *Why Institutional Tokenization Stalls* (Oraclizer) and BlackRock BUIDL's USD 2.5B AUM against the USD 30.1T Standard Chartered forecast and USD 16T BCG forecast. Its job: keep the wiki honest.

### 3.6 `60_Drafts/` — the existing carbon report lands here

The 2 April 2026 carbon-credit tokenisation report currently lives at the vault root. It belongs in `60_Drafts/` as a finished deep-research piece. Moving it consolidates the root and lets the report cross-link cleanly into `40_Domains/Examples/Carbon-Credits/` and `MOC - Carbon-Credits.md`.

### 3.7 `70_Research/` — work in progress

Active research threads sit here as folders, not files. Each thread has its own SOURCES, QUESTIONS, FINDINGS notes. Pattern lifted from `wiki-ai-thinkers`.

### 3.8 `90_Templates/`, `99_Meta/` — administration

Standard Obsidian convention. The `wiki-config.yaml` lets the `/wiki` skill auto-tag and auto-MOC the vault. `NotebookLM-bridge.md` records the notebook UUID and sync state so future top-ups don't reinvent the wheel.

---

## 4. The MOCs the wiki will host

| # | MOC | Function |
|---|---|---|
| 1 | Root | Front door. Index of MOCs, top-tier reading path, recent additions. |
| 2 | Finance | Tokenised funds, bonds, deposits, treasuries, trade finance, repo. |
| 3 | Law | UCC, UK Act, UNIDROIT, MiCA, GENIUS, regional regimes. |
| 4 | Carbon Credits | Registries, bridges, platforms, integrity, Article 6 interface. |
| 5 | Real Estate | Models (SPV, REIT-token), jurisdictions, platforms, critique. |
| 6 | Property Rights | Land registry, de Soto, anchoring vs full tokenisation. |
| 7 | Stablecoins | Architectures (fiat, RWA, algorithmic), regimes, primary issuers. |
| 8 | Agentic AI | Agent taxonomy, payment rails, security, the agent economy. |
| 9 | Blockchain Settlement | Public, permissioned, hybrid; Ethereum, Canton, Avalanche, Stellar. |
| **10** | **Private-Law Convergence** | **Cross-cutting.** |
| **11** | **Agent–Ledger Interface** | **Cross-cutting.** |
| **12** | **Realised vs Projected** | **Cross-cutting.** |

The three bolded MOCs are the user's named cross-cutting threads. They live alongside the domain MOCs because *they are MOCs*, not categories.

---

## 5. Open decisions awaiting the next prompt

These are the points worth your attention before the proposal turns into folders on disk.

1. **Decimal-prefix vs flat folders.** Proposal uses `10_`, `20_`, `30_` ... matching `wiki-ai-thinkers`. Confirm or reject.

2. **`Sub-Topic/` nested under `40_Domains/`, vs promoted to its own top-level spoke.** Proposal nests, on the reading that the user's scope statement subordinates it. Confirm or invert.

3. **`PDFs/` mirrors the source-note subfolders, vs a single flat PDFs bucket.** Proposal mirrors. Mirroring keeps location-by-category consistent; flat is simpler.

4. **`60_Drafts/` absorbs the existing carbon report**, including the `.html`. Confirm or leave the report at the root.

5. **`100_HTML_Artefacts/` (from `wiki-ai-thinkers`) — include or omit.** Proposal omits; the carbon report's `.html` companion is the only candidate so far. Include later if and when needed.

6. **`_wiki/` (per Karpathy convention in the sibling vault) — include or omit.** Proposal omits. The `50_MOCs/` folder discharges the same function. If you want a literal `_wiki/` for the auto-MOC-builder skill to write into, say so and the structure adjusts.

7. **NotebookLM-source notes — auto-generate one-per-source `.md` files, or rely on `SOURCE-REGISTER.md` Section 16 table.** Proposal recommends auto-generating (one note per of the 46 sources, populated from NotebookLM `source_describe`), so that each source is independently linkable from concepts and people.

8. **Templates.** Proposal lists four (`source`, `concept`, `person`, `MOC`). Confirm scope; templates are cheap to add later.

Awaiting your direction.
