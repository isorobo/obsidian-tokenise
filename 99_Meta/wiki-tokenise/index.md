---
title: wiki-tokenise Status Index
type: metadata
date: 2026-10-25
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
| ledger-insights | active | 85 | 8 | 0 | 2026-10-25 |
| arxiv-q-fin-rwa | active | 43 | 3 | 0 | 2026-10-25 |
| imf-fintech-notes | active | 20 | 4 | 0 | 2026-10-25 |
| hkma-press | active | 19 | 0 | 1 | 2026-10-25 |
| esma-news | active | 18 | 0 | 4 | 2026-10-25 |
| mas-news | active | 15 | 0 | 2 | 2026-10-25 |
| fed-staff-papers | active | 14 | 0 | 1 | 2026-10-25 |
| unidroit-news | active | 14 | 1 | 0 | 2026-10-18 |
| bis-working-papers | active | 13 | 1 | 0 | 2026-10-25 |
| fsb-publications | active | 9 | 2 | 0 | 2026-10-25 |
| verra-policy | active | 6 | 0 | 1 | 2026-10-25 |
| iosco-publications | active | 5 | 0 | 9 | 2026-10-25 |
| ecb-publications | active | 4 | 4 | 0 | 2026-10-25 |
| occ-fedreg-genius | active | 4 | 4 | 0 | 2026-10-25 |
| boe-publications | active | 3 | 3 | 0 | 2026-10-25 |
| ust-refunding-tbac | active | 3 | 3 | 0 | 2026-10-25 |
| bcb-brazil | active | 2 | 2 | 0 | 2026-10-25 |
| nyfed-liberty-street | active | 2 | 2 | 0 | 2026-10-25 |

**Totals:** 18 active channels, 279 sources tracked, 36 added in the 25 October run.

## Last run

Latest run date: 25 October 2026 (17 of 18 active channels last ran on that date).

- 36 new sources written (Central-Banks 14, Industry-Press 8, International-Agencies 7, Law-Regulation 4, Academia 3).
- Dry channels (6): esma-news, fed-staff-papers, hkma-press, iosco-publications, mas-news, verra-policy.

## Monitor flags for the orchestrator

- **Cadence:** fsb-publications: fsb-publications -> monthly (channel dry for five rounds). Previous run: Eighth run. No new in-scope sources found. Three rounds checked the full publications listing, speeches and press-releases archives, the crypto-assets and global-stablecoins landing page, the crypto-assets policy-area page, the consolidated FSB source feed, and Ledger Insights coverage for anything after 9 August 2026. The one candidate surfaced, the 10 August 2026 announcement of Ayman M. Al-Sayari as FSB Regional Engagement Chair, was rejected: crypto-assets and stablecoins appear only as one bullet in a two-item list of priority areas needing non-member engagement, with no substantive analysis to support key claims or anchored excerpts. The AI final report remains due October 2026; iosco-publications: iosco-publications -> monthly (eight dry runs); ledger-insights: last run was 2026-08-17, a 48 day gap.
- **Fetch:** arxiv-q-fin-rwa: papers.ssrn.com 403; bcb-brazil: bcb.gov.br client-side rendered, no body text; bis-working-papers: bis.org /publ/work1372+ 404 (new URL pattern); boe-publications: bankofengland.co.uk/working-paper 404; boe-publications: bankunderground.co.uk no results; ecb-publications: ecb.europa.eu working-papers and speeches listings empty shell; esma-news: esma.europa.eu PDFs unreadable via WebFetch; hkma-press: hkma.gov.hk empty content; imf-fintech-notes: imf.org 403; iosco-publications: iosco.org 403; ledger-insights: ledgerinsights.com category page 404, RSS feed returned one item; mas-news: mas.gov.sg /news index returns shell only; occ-fedreg-genius: occ.gov news-release index 404; unidroit-news: unidroit.org/news-and-events 404; ust-refunding-tbac: home.treasury.gov PDFs unreadable via WebFetch; verra-policy: mdpi.com 403, nature.com and springer.com auth redirect.
- **Filter gap:** ecb-publications: working papers and speeches not covered this run; hkma-press: HKMA speeches (for example 20260923-1 Treasury Markets Summit keynote) sit outside the press-release path. Previous summary: Eighth run. No sources added. Enumerated the full visible HKMA press-release feed from 9 to 17 August 2026: a DFSA joint Climate Finance Conference announcement (10 August, sustainable-finance topic, no tokenisation content), a Faster Payment System maintenance notice, an Exchange Fund Notes tender announcement, three government-bond and FRN tender results, and a bank scam alert; nyfed-liberty-street: staff report listing not swept, only SR 1202 found.
- **Backfill:** arxiv-q-fin-rwa: 4 catches (2604.17167, 2605.00071, 2608.30519, 2609.18949); boe-publications: 3 catches; ecb-publications: 4 catches; ust-refunding-tbac: 3 catches (sb0122, sb0386, sb0592); verra-policy: 3 catches (JRFM x2, npj CATchain-R).
- **Watch:** arxiv-q-fin-rwa: 2026-10-18 SSRN 7172738 unverifiable, consider dropping; bcb-brazil: 2026-11 Resolutions 519/520 and Instruction 701/2026 need canonical URLs; bis-working-papers: 2026-10-11 doclist/bis_fsi_publs.rss is the best discovery surface. Previous summary: Run of 17 August 2026. Three rounds executed, zero sources added. IDEAS/RePEC, EconPapers, direct page fetches for WP 1372 through 1376, and the bis.org/wpapers/index.htm and doclist/wppubls.htm landing pages all confirm WP 1371 remains the published ceiling, unchanged since 21 July 2026. This is the fourth consecutive weekly run (26 July, 2 August, 9 August, 17 August) with no new BIS Working Paper of any kind, in-scope or otherwise. Broad searches for tokenisation, stablecoin, CBDC, unified ledger, tokenised deposits, and blockchain settlement surfaced only already-indexed items (WP 905, WP 1270, WP 1335, WP 1355) and adjacent IMF/academic commentary with no new working paper candidates. Channel dry across all three rounds. Target of 5 not met. Bottleneck unchanged: BIS Working Papers publication schedule remains paused or slowed for over four weeks; boe-publications: 2026-12-31 final Code of Practice for systemic stablecoins; esma-news: 2026-10-30 follow-up to the MiCA review. PREVIOUS: Eighth run, covering 9 to 17 August 2026. No sources added. ESMA's full news listing for the window contains a single item, a commodity derivatives weekly position reporting go-live notice (14 August, off scope). The library filtered from 9 August surfaced only routine administrative and registry updates: two stale MiCA compliance tables (11 August, tabulating pre-existing guidelines), a CSD register refresh, an ESG providers list, and various board summaries of conclusions, none on scope. The MiCA register refreshed again on 12 August with no accompanying narrative text or named entrants on the ESMA page itself, consistent with the rejection pattern established in rounds 5 to 7. Checked the second 2026 Trends Risks and Vulnerabilities report directly on the risk-monitoring page; fsb-publications: 2026-10 FSB AI sound practices final report; hkma-press: 2026-12-31 tokenised Exchange Fund Bills pilot and EnsembleTX CBDC settlement; imf-fintech-notes: 2026-10-08 GFSR tokenisation chapter; iosco-publications: 2026-12-01 CPMI-IOSCO FMI consultation comments close; ledger-insights: 2026-10-04 ZA jurisdiction schema gap still open; mas-news: 2026-10-16 MAS stablecoin consultation closes; mas-news: 2026-11-18 Singapore FinTech Festival; nyfed-liberty-street: 2026-11-01 next run should sweep newyorkfed.org staff report listing from sr1190 upward; occ-fedreg-genius: 2026-11-30 Fed GENIUS proposal comment deadline; occ-fedreg-genius: 2027-01-18 GENIUS Act effective date; occ-fedreg-genius: FDIC, NCUA and Treasury GENIUS rules not yet captured; unidroit-news: 2026-10-16 tenth VCC Working Group session documents. Previous run: Eighth run, eight days since the seventh run. No sources added. Three rounds of searching across the UNIDROIT news feed, the Verified Carbon Credits work-in-progress page, the Digital Assets and Private Law page, the general work-in-progress project list, and targeted searches on DAPL implementation, tokenised receivables and linked assets surfaced only one new news item in the window, an 8 August 2026 item on Georgian membership talks, already logged as rejected in a prior run and off scope. No new UNIDROIT-issued document has been posted since the ninth VCC Working Group session (16 June 2026). No documents have been posted for the tenth VCC Working Group session (14-16 October 2026), no consultation responses have been published, and no new DAPL adoption or implementation announcements appeared. The channel's session-driven cadence remains the binding constraint; ust-refunding-tbac: 2026-11-04 Q4 2026 quarterly refunding and TBAC minutes (published 2026-11-05); verra-policy: Verra internal end-2026 crypto-instruments policy target. PRIOR RUN SUMMARY: Eighth run on verra-policy channel, covering 9 to 17 August 2026. Zero sources added across three rounds. The sole item in the window was the 12 August ICVCM Core Carbon Principles approval for Verra's rice cultivation (VM0051) and landfill gas (VMR0016) methodologies, which carries no crypto, blockchain, or tokenisation content. Re-checked the two open threads carried forward from prior runs: the Meta Registry / transaction-ready API rollout remains a planned future phase per third-party aggregator coverage (carbonherald.com, esgtoday.com), with no primary Verra statement naming a delivery date.
- **Permission denied:** bcb-brazil: python3 (state written with Write tool); imf-fintech-notes: python3. Prior summary: Eighth run. No new sources added. Three rounds of general web-search sweeps, an IMF working-paper RePEc listing check, and an IMF Staff Discussion Notes listing check surfaced no candidate published after last_run_at of 2026-08-09. The RePEc IMF working-paper series listing now runs to WP/26/168 (up from 164 last run); mas-news: python3 state editing (state edited with Edit tool instead). PREVIOUS: Eighth run for mas-news channel. No sources added. MAS's website (mas.gov.sg) returned HTTP service-unavailable errors on every direct fetch attempt, extending the pattern to an eighth consecutive run; ust-refunding-tbac: rg.

## Next scheduled run

Sunday 1 November 2026 via launchd (`com.lundons.wiki-weekly`).
