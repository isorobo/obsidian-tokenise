# .workspace

Browser artefacts that read the wiki-tokenise vault. Read-only. No
writes, no Claude API calls, no telemetry.

## Quick start

### Windows

1. Double-click `serve.bat` from Windows File Explorer (press `Win+E`
   and navigate to this folder).
2. A console window opens titled "wiki-tokenise server" and prints
   `http://localhost:8766/index.html`.
3. Ctrl-click the URL (or paste into Chrome / Edge).
4. From the landing page, click any of the five artefacts. Each prompts
   you to **Connect vault**; pick the wiki-tokenise folder once and grant
   read access. Subsequent visits one-click reconnect.

To stop the server, close the console window or press Ctrl+C.

### macOS / Linux

1. From a terminal in this folder: `./serve.sh` (or `python3 serve.py`).
2. Open `http://localhost:8766/index.html`.

### Any platform (manual)

```
python serve.py              # default port 8766
python serve.py --port 5500  # custom port
python serve.py --page graph.html  # open a specific artefact
```

## The five artefacts

| File | Purpose |
|---|---|
| `index.html` | Landing page. Linked from `START_HERE.html` at the vault root. |
| `graph.html` | Force-directed graph of every wikilink. Hover for one-line summary; click for the side panel. |
| `convergence.html` | Jurisdiction × doctrine matrix. The analytical centrepiece. |
| `timeline.html` | Events on a horizontal time axis. Lanes: Regulation, Pilot, Academic, Industry. |
| `realised.html` | Bull-case forecasts vs realised AUM. Reads `99_Meta/forecasts.json` + `99_Meta/realised.json`. |
| `compare.html` | Pick any two notes; frontmatter aligns; bodies side by side. |
| `serve.py`, `serve.bat`, `serve.sh` | Cross-platform launchers (stdlib only). |
| `vault-store.js` | IndexedDB persistence for the folder handle. |
| `_vault-loader.js` | Shared vault walker + YAML frontmatter parser. |
| `_shared.css` | Design tokens, iA Writer @font-face, base typography. |

## Design language

iA Writer Quattro V (body) + iA Writer Mono V (data tables and labels),
self-hosted from `../80_Attachments/fonts/`. Tinted-neutral palette
(warm cream + oxblood accent). Light theme by default; toggle in the
header. OKLCH throughout. No glassmorphism, no gradients, no hero-metric
template, no side-stripe borders.

## Schema dependency

Each artefact reads YAML frontmatter as defined in
`../99_Meta/schema.md`. The contract:

| Artefact | Required fields |
|---|---|
| graph | `type`, wikilinks in body |
| convergence | `type=source`, `jurisdiction`, `doctrine` |
| timeline | `type=source`, `year` or `date_published`, `source_type` |
| realised | reads `99_Meta/forecasts.json` and `99_Meta/realised.json` (hand-maintained) |
| compare | every frontmatter field on the two compared notes |

Renaming or removing a field in `schema.md` breaks the matching artefact.

## What this folder will NOT contain

- Anything that writes to the vault.
- Anything that calls the Claude API. AI work goes through Claudian in
  Obsidian, or Claude Desktop with the local MCP.
- Build artefacts. Every file is hand-written and CDN-free for fonts.
  D3 loads from a single jsDelivr URL; otherwise vanilla JS.
