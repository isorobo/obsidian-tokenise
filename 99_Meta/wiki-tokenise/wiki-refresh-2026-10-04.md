---
title: Wiki refresh 2026-10-04
type: report
date: 2026-10-04
tags: [metadata, wiki-refresh]
auto_generated: true
---

# Wiki refresh 2026-10-04

## Scan

| Measure | Count |
|---|---|
| Notes scanned | 331 |
| Fresh (before apply) | 26 |
| Modified (before apply) | 0 |
| Unchanged (before apply) | 305 |
| Tag targets | 23 |
| Re-stamp targets | 0 |
| Orphans | 0 |
| Quarantined | 0 |
| Stubs | 0 |
| Topics in use / subjects in use | 14 / 31 |

The 3 fresh notes that were not targets are the `never_write` files (`10_Sources/SOURCE-REGISTER.md`, `README.md`, `_CLAUDE.md`). After apply, the verify scan shows exactly those 3 fresh, no modified notes and no unexpected paths. This report replaces an earlier file of the same name written by a previous run today (a 1 source smoke test, 308 notes scanned).

## Newly tagged

23 source notes, frontmatter only (`topic`, `subject`, `wiki_role`, `wiki_hash`, `wiki_indexed`). All topics were already on the monitors' notes and on the closed vocabulary, so the mapper confirmed them. Plan check passed with 0 errors; apply dry run and live run both reported 23 applied, 0 failed.

| Area | Notes | Publisher subject added |
|---|---|---|
| Academia | 9 | none |
| Central-Banks | 9 (ESMA 3, FEDS 2, HKMA 2, MAS 2) | `subject/esma`, `subject/federal-reserve`, `subject/hkma`, `subject/mas` |
| International-Agencies | 5 (BIS 1, IMF 3, UNIDROIT 1) | `subject/bis`, `subject/imf` (UNIDROIT note got none) |

Topic frequency across the plan: `topic/tokenisation` 12, `topic/finance/stablecoins` 12, `topic/blockchain-settlement` 7, `topic/finance/market-infrastructure` 6, `topic/agentic-ai` 5, `topic/carbon-credits` 3, `topic/finance` 2, `topic/law/digital-assets` 2, `topic/finance/tokenised-deposits` 2, `topic/law/securities` 1, `topic/finance/cbdc` 1.

## Re-stamp only

None.

## Pending Topic candidates

None. No off-vocabulary topic values; `unknown_enum_values` is empty; `pending_candidates` is empty.

## Schema issues

- Topic cap: `10_Sources/Law-Regulation/US-Anti-CBDC-Surveillance-State-Act-2025.md` carries 4 topics against a cap of 3. It is a legacy note, not in this cycle's plan, and was not changed. Apply is append-only, so the user must trim it by hand.
- Subject gap: `10_Sources/International-Agencies/UNIDROIT-Centenary-Financial-Markets-Technology-Workshop-2026.md` received no `subject/unidroit` although `org_subject` maps UNIDROIT. Its `organisation` value probably does not match a mapper key. Check the note's `organisation` field.
- Subject gap: none of the 9 Academia notes received a subject (no institutional issuer), as expected.

## MOC candidates

Suggest mode only; `50_MOCs/` was not written. 23 notes considered, 0 already linked, 40 candidate links across 7 MOCs, 0 unmapped. Full list: `wiki-moc-candidates-2026-10-04.json`.

- **MOC - Agentic-AI** (5): [[arXiv-2604-03733-SoK-Blockchain-Agent-to-Agent-Payments]], [[arXiv-2609-30940-Financial-Fragility-Societies-LLM-Agents]], [[ESMA-New-Supervisory-Priority-Digital-Innovation-2027]], [[IMF-Speech-2026-09-Katz-AI-Future-Payments-Policy]], [[MAS-Chia-Building-Financial-System-Future-GFF-2026]]
- **MOC - Blockchain-Settlement** (7): [[arXiv-2604-03733-SoK-Blockchain-Agent-to-Agent-Payments]], [[BIS-WP1377-Hidden-Complexity-Measuring-Stablecoin-DeFi-Ecosystems]], [[ESMA-TRV-2026-Geopolitical-Vulnerabilities-Crypto-Tokenisation]], [[HKMA-Fourth-Digital-Green-Bonds-Offering-Tokenised-Deposits-2026]], [[IMF-Speech-2026-08-Georgieva-Financially-More-Fluid-World]], [[JRFM-2026-Liquidity-Microstructure-Tokenized-Carbon-Assets]], [[npj-2026-CATchain-R-Blockchain-Carbon-Registry-Transportation]]
- **MOC - Carbon-Credits** (3): [[JRFM-2026-Liquidity-Microstructure-Tokenized-Carbon-Assets]], [[JRFM-2026-Tokenisation-Opportunities-Voluntary-Carbon-Markets-Sectoral-Diagnostic]], [[npj-2026-CATchain-R-Blockchain-Carbon-Registry-Transportation]]
- **MOC - Finance** (10): [[arXiv-2510-10469-Risk-Mitigation-Model-Monetary-Ecosystem-Stablecoins]], [[arXiv-2609-15797-Prelude-Theory-RWA-Tokenization]], [[ESMA-New-Supervisory-Priority-Digital-Innovation-2027]], [[ESMA-TRV-2026-Geopolitical-Vulnerabilities-Crypto-Tokenisation]], [[FEDS-Note-2026-09-New-Forms-Money-US-Monetary-Aggregates]], [[HKMA-Fourth-Digital-Green-Bonds-Offering-Tokenised-Deposits-2026]], [[HKMA-Treasury-Markets-Summit-2026-Digital-Native-Bond-Market]], [[IMF-Annual-Report-2026-New-Frontiers-Digital-Finance]], [[JRFM-2026-Liquidity-Microstructure-Tokenized-Carbon-Assets]], [[UNIDROIT-Centenary-Financial-Markets-Technology-Workshop-2026]]
- **MOC - Law** (1): [[ESMA-Calls-Changes-MiCA-Clearer-Safer-Emerging-Services-2026]]
- **MOC - Private-Law-Convergence** (2): [[ESMA-Calls-Changes-MiCA-Clearer-Safer-Emerging-Services-2026]], [[UNIDROIT-Centenary-Financial-Markets-Technology-Workshop-2026]]
- **MOC - Stablecoins** (12): [[arXiv-2507-13883-Stablecoins-Fundamentals-Emerging-Issues-Open-Challenges]], [[arXiv-2508-02403-SoK-Stablecoins-Digital-Transformation-RWA]], [[arXiv-2510-10469-Risk-Mitigation-Model-Monetary-Ecosystem-Stablecoins]], [[arXiv-2609-15797-Prelude-Theory-RWA-Tokenization]], [[BIS-WP1377-Hidden-Complexity-Measuring-Stablecoin-DeFi-Ecosystems]], [[ESMA-Calls-Changes-MiCA-Clearer-Safer-Emerging-Services-2026]], [[FEDS-Note-2026-08-Decade-US-Cross-Border-Payments-Efforts]], [[FEDS-Note-2026-09-New-Forms-Money-US-Monetary-Aggregates]], [[IMF-Annual-Report-2026-New-Frontiers-Digital-Finance]], [[IMF-Speech-2026-08-Georgieva-Financially-More-Fluid-World]], [[IMF-Speech-2026-09-Katz-AI-Future-Payments-Policy]], [[MAS-Stablecoin-Legislative-Amendments-Consultation-2026]]

## Housekeeping observations

- `_wiki/` did not exist before the run and does not exist now (not resurrected).
- Dated `build-apply-plan-*.py` copies remain in this folder as read-only evidence; `tk-plan` was used instead.
- Config has `engine`, `reports_dir`, `moc_mode: suggest` and the mapper tables, so no preconditions were missing.
- `topic/tokenisation` is the fallback topic and was added to 12 of 23 notes; none of the 9 Academia notes with only a fallback-level fit were held.

## Working tree

`verify` reports 27 uncommitted paths (23 tagged notes plus this cycle's scan, plan, verify, MOC candidate and report files). Nothing was committed.

## Pending your decision

- Watchlist cadence and surface edits recommended by monitors (none raised in this stage).
- Adding schema values such as a `ZA` jurisdiction.
- Auto-commit on or off.
- SOURCE-REGISTER stays frozen, or an opt-in register-link step.
- Trim `US-Anti-CBDC-Surveillance-State-Act-2025` to 3 topics.
- Check the UNIDROIT workshop note's `organisation` value so `subject/unidroit` can be mapped.
- Place the MOC candidates above by hand (MOCs are user-owned).

## Next steps

Review the 40 MOC candidate links and add them to the hand-curated MOCs. Suggested commit message: `chore(wiki): Oct refresh, tag 23 sources, MOC candidates`.
