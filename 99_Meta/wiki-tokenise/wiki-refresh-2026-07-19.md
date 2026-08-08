---
title: Wiki refresh report 2026-07-19
type: report
date: 2026-07-19
tags:
  - metadata
  - wiki-refresh
auto_generated: true
---

# Wiki refresh report, 19 July 2026

This refresh followed the weekly `run all` haul of the same morning, which added
19 source notes across seven channels. It tagged 20 notes, re-stamped 2, and
wrote nothing to user-owned files. Working artefacts sit in
`99_Meta/wiki-tokenise/`. The plan builder is `build-apply-plan-2026-07-19.py`,
adapted from the 12 July builder.

## Scan

- 201 notes scanned; 23 fresh, 2 modified, 176 unchanged.
- Plan builder: `build-apply-plan-2026-07-19.py`. Scan and plan JSONs sit beside it.
- Applied via `apply_wiki.py`: 22 written, 0 failures.
- Re-scan confirms 0 untagged targets remain in `10_Sources/` and `30_Areas/`.
- No new `30_Areas/` synthesis notes this week, so the OVERRIDES table was unchanged.
- Every domain, instrument, and doctrine value mapped through the existing
  classification tables. No new mapping keys were needed.

## Changes to the builder

- `QUARANTINE` is now empty. `AWS-Bedrock-AgentCore-Payments.md`, quarantined on
  12 July as a 0-byte stub, was re-fetched on 13 July. It now carries full
  content and classifies normally to `topic/blockchain-settlement` and
  `topic/finance/stablecoins`, merged with its existing `topic/agentic-ai`.

## Re-stamp only

Two modified notes already carried controlled topics, so the builder re-stamped
the hash without changing topics:

- `IMF-WP-2026-074-Making-Stablecoins-Stable.md`
- `UNIDROIT-VCC-Draft-Principles-Commentary-WG9-Doc3.md`

## Pending Topic candidates

None. The off-vocabulary sweep across the whole vault returned zero topics
outside the 14-topic controlled vocabulary. The six off-vocabulary topics from
the 12 July refresh were folded or normalised on 13 July, and this batch
introduced none.

## MOC candidates

`50_MOCs/` is user-owned, so this refresh wrote no MOC changes. All 20 newly
tagged notes lack a wikilink from any MOC. Candidate placements by assigned
topic:

**MOC - Stablecoins**
- [[esma-mica-register-second-post-deadline-update-2026]]
- [[FEDS-Note-2026-02-Brief-History-Bank-Notes-Stablecoins]]
- [[FEDS-Note-2026-07-Fifth-Conference-International-Dollar-Stablecoins]]
- [[Ledger-Insights-UK-US-Transatlantic-Taskforce-Stablecoins]]
- [[Ledger-Insights-Visa-Stablecoin-Platform-Launch]]
- [[IMF-WP-2026-144-Stablecoins-Fixed-Exchange-Rate-Fragility]]
- [[arXiv-2607-12575-How-Agentic-Is-Agentic-Commerce-x402]]

**MOC - Finance**
- [[HKMA-HKEX-eHKD-Derivatives-Margin-Pilot-2026]]
- [[Ledger-Insights-BlackRock-Digital-Asset-Strategy]]
- [[Ledger-Insights-CFTC-MMF-Collateral-Rule-Change]]
- [[Ledger-Insights-DTCC-Live-Tokenization-JPMorgan-CME-BNP]]
- [[Ledger-Insights-HK-SFC-Baillie-Gifford-Tokenized-Fund-Approval]]
- [[Ledger-Insights-HSBC-Digital-Securities-Sandbox-LSEG-Gilt]]
- [[Ledger-Insights-Tokenized-Deposits-Why-Not-Faster]]
- [[GL1-Programmable-Compliance-Whitepaper-2026]]

**MOC - Blockchain-Settlement**
- [[FEDS-2026-011-Contrasting-Ledgers-Interbank-Payment-Systems]]
- [[Ledger-Insights-HSBC-Digital-Securities-Sandbox-LSEG-Gilt]]
- [[GL1-Programmable-Compliance-Whitepaper-2026]]
- [[AWS-Bedrock-AgentCore-Payments]]

**MOC - Law**
- [[esma-mica-register-second-post-deadline-update-2026]]
- [[Ledger-Insights-DTCC-Live-Tokenization-JPMorgan-CME-BNP]]
- [[Ledger-Insights-HK-SFC-Baillie-Gifford-Tokenized-Fund-Approval]]
- [[Ledger-Insights-UK-US-Transatlantic-Taskforce-Stablecoins]]

**MOC - Agentic-AI**
- [[arXiv-2607-10286-TradeLens-Agentic-Trading-Viability]]
- [[arXiv-2607-12575-How-Agentic-Is-Agentic-Commerce-x402]]
- [[AWS-Bedrock-AgentCore-Payments]]

**MOC - Agent-Ledger-Interface**
- [[arXiv-2607-12575-How-Agentic-Is-Agentic-Commerce-x402]]
- [[AWS-Bedrock-AgentCore-Payments]]

**MOC - Carbon-Credits**
- [[UNIDROIT-VCC-Consultation-Launch-Press-Release-2026]]
- [[UNIDROIT-VCC-Draft-Principles-Consultation-Text-2026]]

**MOC - Property-Rights**
- [[UNIDROIT-VCC-Consultation-Launch-Press-Release-2026]]
- [[UNIDROIT-VCC-Draft-Principles-Consultation-Text-2026]]

**MOC - Private-Law-Convergence**
- [[UNIDROIT-VCC-Consultation-Launch-Press-Release-2026]]
- [[UNIDROIT-VCC-Draft-Principles-Consultation-Text-2026]]

## Next steps

1. Add the MOC candidate links above to the hand-curated MOCs.
2. No Topic vocabulary decisions are pending this week.
