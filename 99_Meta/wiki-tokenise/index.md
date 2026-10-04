---
title: wiki-tokenise Status Index
type: metadata
date: 2026-10-04
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
| ledger-insights | active | 64 | 1 | 0 | 2026-10-04 |
| arxiv-q-fin-rwa | active | 28 | 6 | 0 | 2026-10-04 |
| hkma-press | active | 17 | 2 | 0 | 2026-10-04 |
| esma-news | active | 16 | 3 | 0 | 2026-10-04 |
| imf-fintech-notes | active | 16 | 3 | 3 | 2026-10-04 |
| fed-staff-papers | active | 14 | 2 | 0 | 2026-10-04 |
| mas-news | active | 13 | 2 | 3 | 2026-10-04 |
| unidroit-news | active | 13 | 1 | 0 | 2026-10-04 |
| bis-working-papers | active | 11 | 1 | 0 | 2026-10-04 |
| fsb-publications | active | 7 | 0 | 5 | 2026-10-04 |
| verra-policy | active | 6 | 3 | 0 | 2026-10-04 |
| iosco-publications | active | 5 | 0 | 6 | 2026-10-04 |

**Totals:** 12 active channels, 210 sources tracked, 24 added in the 4 October run.

## Last run

Latest run date: 4 October 2026 (12 of 12 active channels last ran on that date).

- 24 new sources written (Academia 9, Central-Banks 9, International-Agencies 5, Industry-Press 1).
- Dry channels (2): fsb-publications, iosco-publications.

## Monitor flags for the orchestrator

- **Cadence:** fsb-publications: fsb-publications -> monthly (channel dry for five rounds). Previous run: Eighth run. No new in-scope sources found. Three rounds checked the full publications listing, speeches and press-releases archives, the crypto-assets and global-stablecoins landing page, the crypto-assets policy-area page, the consolidated FSB source feed, and Ledger Insights coverage for anything after 9 August 2026. The one candidate surfaced, the 10 August 2026 announcement of Ayman M. Al-Sayari as FSB Regional Engagement Chair, was rejected: crypto-assets and stablecoins appear only as one bullet in a two-item list of priority areas needing non-member engagement, with no substantive analysis to support key claims or anchored excerpts. The AI final report remains due October 2026; iosco-publications: iosco-publications -> monthly (eight dry runs); ledger-insights: last run was 2026-08-17, a 48 day gap.
- **Fetch:** arxiv-q-fin-rwa: export.arxiv.org 429; bis-working-papers: bis.org /publ/work1372+ 404 (new URL pattern); esma-news: esma.europa.eu PDFs unreadable via WebFetch; hkma-press: hkma.gov.hk empty content; imf-fintech-notes: imf.org 403; iosco-publications: iosco.org 403; ledger-insights: ledgerinsights.com category page 404, RSS feed returned one item; mas-news: mas.gov.sg /news index returns shell only; unidroit-news: unidroit.org/news-and-events 404; verra-policy: mdpi.com 403, nature.com and springer.com auth redirect.
- **Filter gap:** hkma-press: HKMA speeches (for example 20260923-1 Treasury Markets Summit keynote) sit outside the press-release path. Previous summary: Eighth run. No sources added. Enumerated the full visible HKMA press-release feed from 9 to 17 August 2026: a DFSA joint Climate Finance Conference announcement (10 August, sustainable-finance topic, no tokenisation content), a Faster Payment System maintenance notice, an Exchange Fund Notes tender announcement, three government-bond and FRN tender results, and a bank scam alert.
- **Backfill:** arxiv-q-fin-rwa: 4 catches (2508.02403, 2604.03733, 2510.10469, 2507.13883); verra-policy: 3 catches (JRFM x2, npj CATchain-R).
- **Watch:** arxiv-q-fin-rwa: 2026-10-11 re-check SSRN 7172738; bis-working-papers: 2026-10-11 doclist/bis_fsi_publs.rss is the best discovery surface. Previous summary: Run of 17 August 2026. Three rounds executed, zero sources added. IDEAS/RePEC, EconPapers, direct page fetches for WP 1372 through 1376, and the bis.org/wpapers/index.htm and doclist/wppubls.htm landing pages all confirm WP 1371 remains the published ceiling, unchanged since 21 July 2026. This is the fourth consecutive weekly run (26 July, 2 August, 9 August, 17 August) with no new BIS Working Paper of any kind, in-scope or otherwise. Broad searches for tokenisation, stablecoin, CBDC, unified ledger, tokenised deposits, and blockchain settlement surfaced only already-indexed items (WP 905, WP 1270, WP 1335, WP 1355) and adjacent IMF/academic commentary with no new working paper candidates. Channel dry across all three rounds. Target of 5 not met. Bottleneck unchanged: BIS Working Papers publication schedule remains paused or slowed for over four weeks; esma-news: 2026-10-30 follow-up to the MiCA review. PREVIOUS: Eighth run, covering 9 to 17 August 2026. No sources added. ESMA's full news listing for the window contains a single item, a commodity derivatives weekly position reporting go-live notice (14 August, off scope). The library filtered from 9 August surfaced only routine administrative and registry updates: two stale MiCA compliance tables (11 August, tabulating pre-existing guidelines), a CSD register refresh, an ESG providers list, and various board summaries of conclusions, none on scope. The MiCA register refreshed again on 12 August with no accompanying narrative text or named entrants on the ESMA page itself, consistent with the rejection pattern established in rounds 5 to 7. Checked the second 2026 Trends Risks and Vulnerabilities report directly on the risk-monitoring page; fsb-publications: 2026-10 FSB AI sound practices final report; hkma-press: 2026-12-31 tokenised Exchange Fund Bills pilot and EnsembleTX CBDC settlement; imf-fintech-notes: 2026-10-08 GFSR tokenisation chapter; iosco-publications: 2026-12-01 CPMI-IOSCO FMI consultation comments close; ledger-insights: 2026-10-04 ZA jurisdiction schema gap still open; mas-news: 2026-10-16 MAS stablecoin consultation closes; mas-news: 2026-11-18 Singapore FinTech Festival; unidroit-news: 2026-10-16 tenth VCC Working Group session documents. Previous run: Eighth run, eight days since the seventh run. No sources added. Three rounds of searching across the UNIDROIT news feed, the Verified Carbon Credits work-in-progress page, the Digital Assets and Private Law page, the general work-in-progress project list, and targeted searches on DAPL implementation, tokenised receivables and linked assets surfaced only one new news item in the window, an 8 August 2026 item on Georgian membership talks, already logged as rejected in a prior run and off scope. No new UNIDROIT-issued document has been posted since the ninth VCC Working Group session (16 June 2026). No documents have been posted for the tenth VCC Working Group session (14-16 October 2026), no consultation responses have been published, and no new DAPL adoption or implementation announcements appeared. The channel's session-driven cadence remains the binding constraint; verra-policy: Verra internal end-2026 crypto-instruments policy target. PRIOR RUN SUMMARY: Eighth run on verra-policy channel, covering 9 to 17 August 2026. Zero sources added across three rounds. The sole item in the window was the 12 August ICVCM Core Carbon Principles approval for Verra's rice cultivation (VM0051) and landfill gas (VMR0016) methodologies, which carries no crypto, blockchain, or tokenisation content. Re-checked the two open threads carried forward from prior runs: the Meta Registry / transaction-ready API rollout remains a planned future phase per third-party aggregator coverage (carbonherald.com, esgtoday.com), with no primary Verra statement naming a delivery date.
- **Permission denied:** imf-fintech-notes: python3. Prior summary: Eighth run. No new sources added. Three rounds of general web-search sweeps, an IMF working-paper RePEc listing check, and an IMF Staff Discussion Notes listing check surfaced no candidate published after last_run_at of 2026-08-09. The RePEc IMF working-paper series listing now runs to WP/26/168 (up from 164 last run); mas-news: python3 state editing (state edited with Edit tool instead). PREVIOUS: Eighth run for mas-news channel. No sources added. MAS's website (mas.gov.sg) returned HTTP service-unavailable errors on every direct fetch attempt, extending the pattern to an eighth consecutive run.

## Next scheduled run

Sunday 11 October 2026 via launchd (`com.lundons.wiki-weekly`).
