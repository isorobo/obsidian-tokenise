---
title: wiki-tokenise — Vault Overview
type: system
date: 2026-06-30
last_verified: 2026-10-27
tags:
  - system
  - vault-overview
---

# wiki-tokenise

An Obsidian vault collating authoritative sources on the **tokenisation of real-world assets** and on the money it settles in. It sits at the intersection of **finance**, **law**, and three worked examples: **carbon credits**, **real estate**, and **property rights**. A sub-topic strand covers **stablecoins** (reserves, regulation, run risk), **central bank digital currencies**, the **monetary hierarchy** they sit in, **agentic AI / LLM trading**, and the **blockchain settlement** layer underneath.

*Last verified against the vault on 27 October 2026. Counts are deliberately left out because they change weekly; see [`99_Meta/wiki-tokenise/index.md`](99_Meta/wiki-tokenise/index.md) for the live snapshot.*

## How the vault is organised

| Folder | Purpose |
|---|---|
| `10_Sources/` | One note per primary source, grouped by source type (Academia, Central-Banks, Commercial-Banks, Industry-Press, International-Agencies, Law-Regulation, Private-Sector, Think-Tanks). The master annotated bibliography is [SOURCE-REGISTER.md](10_Sources/SOURCE-REGISTER.md); it was frozen in mid-2026 and does not list newer notes. |
| `30_Areas/` | Synthesis notes that pull several sources together on one theme (settlement efficiency, stablecoin architecture, private-law convergence and similar). |
| `30_Concepts/` | Atomic vocabulary: one note per technical term. Some are still stubs. |
| `50_MOCs/` | Maps of Content: domain MOCs (Finance, Law, Carbon-Credits, Real-Estate, Property-Rights, Stablecoins, CBDC, Agentic-AI, Blockchain-Settlement), cross-cutting MOCs (Private-Law-Convergence, Agent-Ledger-Interface, Realised-vs-Projected, Monetary-Hierarchy, Seigniorage-and-Reserves), and [MOC - Root](50_MOCs/MOC%20-%20Root.md) as the front door. |
| `60_Drafts/` | Long-form writing in progress, including the April 2026 carbon-credit research report. Drafts marked `unverified` are not to be cited. |
| `80_Attachments/` | Raw PDFs, mirrored by source channel under `80_Attachments/PDFs/<channel>/`, and fonts. |
| `90_Templates/` | Obsidian templates for sources, concepts and MOCs. The source template also holds the controlled topic vocabulary. |
| `99_Meta/` | Vault administration: [schema](99_Meta/schema.md), design notes, the forecast and realised-AUM data behind the Realised-vs-Projected MOC, and the weekly pipeline's watchlist, channel state and reports under `99_Meta/wiki-tokenise/`. |
| `storm-reports/` | Generated briefings kept as standalone HTML. |
| `_archived_wiki-old-structure/` | The retired June 2026 layout, kept for reference. Not maintained. |
| `.workspace/` | Browser artefacts (see below). |

Folders named in earlier versions of this file (`00_Inbox/`, `20_People/`, `40_Domains/`, `70_Research/`) no longer exist; their content was folded into the folders above.

## How sources arrive

New sources are collected by a weekly job (launchd label `com.lundons.wiki-weekly`, Sunday 06:00 New Zealand time, on the owner's Mac). It runs one monitor per channel listed in [`99_Meta/wiki-tokenise/watchlist.md`](99_Meta/wiki-tokenise/watchlist.md), writes a source note for each accepted item, tags the notes with the controlled topic vocabulary, and commits locally. Channels cover central banks and standard setters (BIS, IMF, FSB, IOSCO, UNIDROIT, MAS, HKMA, ESMA, the Federal Reserve and its regional banks, the ECB, the Bank of England, the US Treasury and OCC, Banco Central do Brasil), arXiv, Verra and industry press. The channel list changes; the watchlist is authoritative.

## Design principles

1. **One artefact, one home; many references.** Each note lives in exactly one folder; MOCs and concepts link to it.
2. **Compress the vocabulary, expand the graph.** Atomic concepts in `30_Concepts/` link out; everything links in.
3. **Source notes talk about sources; source files are sources.** Source `.md` notes live in `10_Sources/<Category>/`; raw PDFs in `80_Attachments/PDFs/<channel>/`.
4. **Verify before relying.** Notes record where a claim came from, and unverified material is labelled as such.

## Browser artefacts

Five read-only browser artefacts live under [`.workspace/`](.workspace/) (compare, convergence, graph, realised, timeline, with `index.html` as the landing page) and read this vault directly via the File System Access API. From a terminal in that folder:

```
.\serve.bat        # Windows
./serve.sh         # macOS / Linux
python serve.py    # any platform
```

The server listens on `http://localhost:8766`. Open `index.html` for the landing page. Requires Chrome 86+ or Edge 86+. See [.workspace/README.md](.workspace/README.md) for the per-artefact contract.

## Provenance

Built on 2026-05-24, drawing on (i) domain knowledge, (ii) live web searches for the freshest authoritative outputs, and (iii) the existing 2 April 2026 carbon-credit research report (now at [60_Drafts/](60_Drafts/)). A NotebookLM notebook was used for early curation; that sync was retired on 9 August 2026. Since October 2026 the vault is extended weekly by the job described above.

## Licences

This repo is dual-licensed.

- **Content** (`10_Sources/`, `30_Areas/`, `30_Concepts/`, `50_MOCs/`, `60_Drafts/`, `90_Templates/`, `99_Meta/`, and all other markdown) is released under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. See [LICENSE-content.txt](LICENSE-content.txt).
- **Code** (`.workspace/`, `serve.py`, `serve.bat`, `serve.sh`, and the helper scripts under `99_Meta/wiki-tokenise/`) is released under the **MIT License**. See [LICENSE](LICENSE).

Third-party bundled assets retain their original licences: iA Writer fonts under SIL Open Font License 1.1, Obsidian Minimal theme under MIT, Claudian plugin under its upstream licence.

## Not a contribution project

This is a personal research vault that happens to be public. Pull requests adding or modifying sources will not be merged. Fork freely and run your own watchlist.
