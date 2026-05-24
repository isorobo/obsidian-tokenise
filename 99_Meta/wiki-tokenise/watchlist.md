# Watchlist

Living watchlist of source channels the `/wiki-tokenise` orchestrator
runs on each weekly refresh. The orchestrator reads this table on every
`run all` and `weekly-refresh` invocation.

## Conventions

- `channel` = slug used in `state/<channel>.json` and `queries/<channel>.md`.
- `name` = display name.
- `category` = matches the destination folder under `10_Sources/`.
- `cadence` = expected publication frequency.
- `target_per_run` = ceiling on sources added per run (the monitor exits
  earlier if the channel is dry).
- `status` values:
  - `pilot` — actively being debugged end-to-end.
  - `active` — runs on every `run all` and `weekly-refresh`.
  - `paused` — held back.
  - `pending` — listed but not yet wired (no `state/*.json` yet).

## Table

| channel | name | category | cadence | target_per_run | status |
|---|---|---|---|---|---|
| bis-working-papers | BIS Working Papers | International-Agencies | weekly | 5 | pilot |
| imf-fintech-notes | IMF FinTech Notes | International-Agencies | monthly | 4 | pending |
| fsb-publications | FSB Publications | International-Agencies | monthly | 4 | pending |
| iosco-publications | IOSCO Publications | International-Agencies | monthly | 4 | pending |
| unidroit-news | UNIDROIT News and Publications | International-Agencies | irregular | 3 | pending |
| mas-news | MAS News and Initiatives | Central-Banks | weekly | 6 | pending |
| hkma-press | HKMA Press Releases | Central-Banks | weekly | 6 | pending |
| fed-staff-papers | Federal Reserve Staff Working Papers | Central-Banks | monthly | 4 | pending |
| esma-news | ESMA News and Reports | Central-Banks | weekly | 5 | pending |
| arxiv-q-fin-rwa | arXiv q-fin filtered for tokenisation / RWA | Academia | weekly | 6 | pending |
| verra-policy | Verra Crypto and Tokenisation Policy | Private-Sector | irregular | 3 | pending |
| ledger-insights | Ledger Insights (RWA + tokenisation tags) | Industry-Press | daily | 8 | pending |

## Promote to active

Flip `pending` to `active` for the channels you want the weekly
refresh to run. The pilot **bis-working-papers** runs first to validate
the end-to-end loop. Once it ships at least one full cycle without
error, promote `imf-fintech-notes` and `mas-news` together.

## Channel surface notes

- **bis-working-papers** — base URL: `https://www.bis.org/publ/work*.htm`. Filter on titles containing `token`, `unified ledger`, `stablecoin`, `CBDC`, `tokenisation`.
- **imf-fintech-notes** — base URL: `https://www.imf.org/en/Publications/fintech-notes`. Filter on titles containing `token` or `stablecoin`.
- **fsb-publications** — base URL: `https://www.fsb.org/publications/`. Filter on titles containing `token`, `stablecoin`, `crypto`, `digital`.
- **iosco-publications** — base URL: `https://www.iosco.org/library/`. Filter on titles containing `token`, `crypto`, `digital`.
- **unidroit-news** — base URL: `https://www.unidroit.org/news-and-events/`. Filter on titles containing `digital assets`, `tokenisation`, `private law`.
- **mas-news** — base URL: `https://www.mas.gov.sg/news`. Filter on `Project Guardian`, `tokenis`, `digital asset`, `stablecoin`.
- **hkma-press** — base URL: `https://www.hkma.gov.hk/eng/news-and-media/press-releases/`. Filter on `Project Ensemble`, `tokenis`, `stablecoin`, `e-HKD`.
- **fed-staff-papers** — base URL: `https://www.federalreserve.gov/econres/feds/`. Filter on titles containing `token`, `stablecoin`, `CBDC`, `DLT`.
- **esma-news** — base URL: `https://www.esma.europa.eu/news`. Filter on `MiCA`, `DLT Pilot`, `tokenis`.
- **arxiv-q-fin-rwa** — query: `cat:q-fin.GN AND (abs:"tokenisation" OR abs:"tokenization" OR abs:"real-world asset")`. Sort: submittedDate desc.
- **verra-policy** — base URL: `https://verra.org/news/`. Filter on `crypto`, `token`.
- **ledger-insights** — base URL: `https://www.ledgerinsights.com/category/tokenisation/`. Take the latest items above `last_run_at`.
