# wiki-tokenise

An Obsidian vault collating authoritative sources on the **tokenisation of real-world assets**, sitting at the intersection of **finance**, **law**, and three worked examples: **carbon credits**, **real estate**, and **property rights**. A sub-topic strand traces the correlation between RWA tokenisation, **stablecoins**, **agentic AI / LLM trading**, and the underlying **blockchain settlement** layer.

## How the vault is organised

| Folder | Purpose |
|---|---|
| `00_Inbox/` | Capture-first; triage weekly. |
| `10_Sources/` | One note per primary source, grouped by source type (International-Agencies, Central-Banks, Commercial-Banks, Academia, Law-Regulation, Think-Tanks, Private-Sector, Industry-Press). Raw PDFs mirror these subfolders under `10_Sources/PDFs/`. NotebookLM exports under `10_Sources/NotebookLM-Exports/`. The master annotated bibliography is [SOURCE-REGISTER.md](10_Sources/SOURCE-REGISTER.md). |
| `20_People/` | Authors and principals as first-class entities. |
| `30_Concepts/` | Atomic vocabulary: one note per technical term. |
| `40_Domains/` | The wiki's four spokes: `Finance/`, `Law/`, `Examples/` (Carbon-Credits, Real-Estate, Property-Rights), `Sub-Topic/` (Stablecoins, Agentic-AI-Trading, Blockchain-Settlement). |
| `50_MOCs/` | Maps of Content: nine domain MOCs plus three cross-cutting MOCs (Private-Law Convergence, Agent-Ledger Interface, Realised vs Projected). |
| `60_Drafts/` | Long-form writing in progress. Houses the existing carbon-credit deep-research report. |
| `70_Research/` | Active research threads, one folder each. |
| `80_Attachments/` | Images, screenshots, diagrams. |
| `90_Templates/` | Obsidian / Templater templates. |
| `99_Meta/` | Vault administration, inception note, directory proposal, NotebookLM bridge log. |

## Design principles

1. **One artefact, one home; many references.** Each note lives in exactly one folder; MOCs and concepts link to it.
2. **Compress the vocabulary, expand the graph.** Atomic concepts in `30_Concepts/` link out; everything links in.
3. **Source notes talk about sources; source files are sources.** Source `.md` notes live in `10_Sources/<Category>/`; raw PDFs in `10_Sources/PDFs/<Category>/`.

## Browser artefacts

Five read-only browser artefacts live under [`.workspace/`](.workspace/) and read this vault directly via the File System Access API. From a terminal in that folder:

```
.\serve.bat        # Windows
./serve.sh         # macOS / Linux
python serve.py    # any platform
```

The server listens on `http://localhost:8766`. Open `index.html` for the landing page. Requires Chrome 86+ or Edge 86+. See [.workspace/README.md](.workspace/README.md) for the per-artefact contract.

## Provenance

Built on 2026-05-24, drawing on (i) domain knowledge, (ii) live web searches for the freshest authoritative outputs, (iii) the existing 2 April 2026 carbon-credit research report (now at [60_Drafts/](60_Drafts/)), and (iv) the user-curated NotebookLM notebook `tokenise` (46 live sources).

## Licences

This repo is dual-licensed.

- **Content** (`10_Sources/`, `20_People/`, `30_Concepts/`, `40_Domains/`, `50_MOCs/`, `60_Drafts/`, `90_Templates/`, `99_Meta/`, and all other markdown) is released under **Creative Commons Attribution 4.0 International (CC BY 4.0)**. See [LICENSE-content.txt](LICENSE-content.txt).
- **Code** (`.workspace/`, `serve.py`, `serve.bat`, `serve.sh`, and PowerShell scripts under `99_Meta/wiki-tokenise/state/logs/`) is released under the **MIT License**. See [LICENSE](LICENSE).

Third-party bundled assets retain their original licences: iA Writer fonts under SIL Open Font License 1.1, Obsidian Minimal theme under MIT, Claudian plugin under its upstream licence.

## Not a contribution project

This is a personal research vault that happens to be public. Pull requests adding or modifying sources will not be merged. Fork freely and run your own watchlist.
