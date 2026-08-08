---
title: wiki-tokenise Status Index
type: metadata
date: 2026-07-13
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
| ledger-insights | active | 23 | 8 | 0 | 2026-07-12 |
| arxiv-q-fin-rwa | active | 15 | 4 | 0 | 2026-07-12 |
| hkma-press | active | 14 | 1 | 0 | 2026-07-12 |
| esma-news | active | 12 | 2 | 0 | 2026-07-12 |
| imf-fintech-notes | active | 10 | 2 | 0 | 2026-07-12 |
| bis-working-papers | active | 9 | 0 | 3 | 2026-07-12 |
| fed-staff-papers | active | 9 | 0 | 3 | 2026-07-12 |
| mas-news | active | 9 | 1 | 3 | 2026-07-12 |
| unidroit-news | active | 9 | 3 | 0 | 2026-07-12 |
| fsb-publications | active | 7 | 2 | 3 | 2026-07-12 |
| iosco-publications | active | 5 | 0 | 3 | 2026-07-12 |
| verra-policy | active | 3 | 0 | 3 | 2026-07-12 |

**Totals:** 12 active channels, 125 sources tracked, 23 added in the 12 July scheduled run, 3 added by the 13 July backfill.

## Last weekly refresh

Scheduled run of 12 July 2026, 06:00 NZ (`WikiTokeniseWeeklyRefresh`, exit 0).

- 12 of 12 channels dispatched; all returned.
- 23 new sources written (Industry-Press 8, International-Agencies 7, Central-Banks 4, Academia 4).
- Dry channels: bis-working-papers, iosco-publications, fed-staff-papers, verra-policy.
- NotebookLM sync blocked on expired Google authentication; 71 sources pending push.
- wiki-refresh completed; the four pending decisions were actioned on 13 July (see below).

## 13 July backfill (out-of-loop)

Manual pass for four items the forward-only date filter could not reach. The monitors left `last_run_at` and `rounds_without_yield` unchanged, so these additions sit outside the scheduled loop.

- hkma-press: [[HKMA-HKEX-eHKD-Derivatives-Margin-Pilot-2026]] (e-HKD and HKEX after-hours margin pilot, 18 June 2026). 13 to 14.
- fed-staff-papers: [[FEDS-2026-011-Contrasting-Ledgers-Interbank-Payment-Systems]] (Contrasting Ledgers, February 2026). 8 to 9.
- mas-news: [[GL1-Programmable-Compliance-Whitepaper-2026]] (GL1 Programmable Compliance white paper, 22 June 2026). 8 to 9.
- Rejected on scope review: FEDS 2026-009 "Initial Margin for Crypto Currencies". An ISDA SIMM margin-calibration paper with no tokenisation, DLT, or CBDC content.
- Re-fetched in place: [[AWS-Bedrock-AgentCore-Payments]] populated from the canonical AWS source (was a 0-byte file with two live inbound wikilinks).

## Wiki-refresh decisions actioned 13 July

- Folded three off-vocabulary topics into `topic/law` and `topic/finance`.
- Normalised three mis-nested variants to `topic/tokenisation`, `topic/blockchain-settlement`, and `topic/agentic-ai`.
- Added 23 source links across seven MOCs under a dated section.

## Next scheduled run

Sunday 19 July 2026, 06:00 NZ via Windows Task Scheduler (`WikiTokeniseWeeklyRefresh`).
