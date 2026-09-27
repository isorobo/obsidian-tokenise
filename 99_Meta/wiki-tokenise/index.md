---
title: wiki-tokenise Status Index
type: metadata
date: 2026-08-17
tags:
  - metadata
  - monitor-status
  - wiki-tokenise
auto_generated: true
---

# wiki-tokenise status rollup

Auto-maintained by `/wiki-tokenise status`. Do not edit by hand.

## Snapshot

| channel | status | total_sources | new_since_last_run | rounds_without_yield | last_run_at |
|---|---|---|---|---|---|
| ledger-insights | active | 63 | 8 | 0 | 2026-08-17 |
| arxiv-q-fin-rwa | active | 22 | 3 | 3 | 2026-08-17 |
| hkma-press | active | 15 | 0 | 3 | 2026-08-17 |
| esma-news | active | 13 | 0 | 12 | 2026-08-17 |
| imf-fintech-notes | active | 13 | 0 | 3 | 2026-08-17 |
| fed-staff-papers | active | 12 | 1 | 3 | 2026-08-17 |
| unidroit-news | active | 12 | 0 | 3 | 2026-08-17 |
| mas-news | active | 11 | 0 | 4 | 2026-08-17 |
| bis-working-papers | active | 10 | 0 | 3 | 2026-08-17 |
| fsb-publications | active | 7 | 0 | 3 | 2026-08-17 |
| iosco-publications | active | 5 | 0 | 3 | 2026-08-17 |
| verra-policy | active | 3 | 0 | 14 | 2026-08-17 |

**Totals:** 12 active channels, 186 sources tracked, 12 added in the 17 August run.

## Last run

Manual `run all` of 17 August 2026, 20:02 to 20:32 NZ. Three waves of 4.

- 12 of 12 channels dispatched; all returned.
- 12 new sources written (Industry-Press 8, Academia 3, Central-Banks 1).
- Dry channels (9): bis-working-papers, imf-fintech-notes, fsb-publications, iosco-publications, unidroit-news, mas-news, hkma-press, esma-news, verra-policy.
- fed-staff-papers yield was a backfill catch: FEDS 2025-090 (September 2025) evaded the title keyword filter for seven runs.

## Monitor flags for the orchestrator

- **Cadence:** iosco-publications (7 dry runs), imf-fintech-notes (8), fsb-publications (8), verra-policy (14 dry rounds) each recommend a monthly or longer interval. Weekly runs re-cover the same ground.
- **Fetch bottlenecks:** bis.org listing renders client-side; iosco.org back to HTTP 403; mas.gov.sg unavailable on direct fetch for eight runs; hkma.gov.hk blocked for six runs; ledgerinsights.com/category/tokenisation/ 404 for two runs (RSS and tag feeds work). RePEc IMF SDN page returned 504.
- **Schema gap:** no `ZA` jurisdiction value. A qualifying South African Reserve Bank source (11 August 2026 draft exchange-control rules for offshore crypto and stablecoin flows) was rejected rather than mis-coded.
- **Filter gap:** fed-staff-papers title keyword filter misses agentic-AI papers. Recommend a periodic full-year title-and-abstract audit against `title_index`.
- **Watch items:** MiCA 2.0 consultation closes 31 August 2026; UNIDROIT consultation closes 21 September 2026 (tenth VCC session 14 to 16 October); FSB AI final report due October 2026; MAS response to P009-2026 and Singapore stablecoin bill pending; Anchorpoint HKDAP stablecoin launched 12 August with no HKMA primary release yet.

## Next scheduled run

Sunday 23 August 2026 via Windows Task Scheduler (`WikiTokeniseWeeklyRefresh`).
