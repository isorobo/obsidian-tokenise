---
title: Wiki refresh report 2026-08-17
type: report
date: 2026-08-17
tags:
  - metadata
  - wiki-refresh
auto_generated: true
---

# Wiki refresh report, 17 August 2026

This refresh indexed the twelve sources the R8 monitor run added between
10 and 17 August and brought the 60 concept stubs in `30_Concepts/` under
wiki stamps for the first time. It tagged 72 notes, re-stamped none,
quarantined nothing, and wrote nothing to user-owned MOCs or the register.
Working artefacts sit in `99_Meta/wiki-tokenise/`. The plan builder is
`build-apply-plan-2026-08-17.py`, adapted from the 9 August builder.

## Scan

- First scan: 307 notes; 75 fresh, 0 modified, 232 unchanged, 0 quarantined.
  The jump from 235 to 307 notes is the `30_Concepts/` layer built on
  9 August after that day's refresh had run.
- 72 targets after filtering. `SOURCE-REGISTER.md`, `_CLAUDE.md`, and
  `README.md` fall outside the tagging scope by design.
- Applied via `apply_wiki.py`: 72 written, 0 failures.
- Verification re-scan: 307 notes, 304 unchanged, 0 modified; only the three
  by-design out-of-scope files stay fresh.

## Newly tagged sources (12)

All twelve arrived with on-vocabulary topics written by the monitors. The
plan confirmed them and stamped hashes. `fed-2025-090` also gained
`subject/federal-reserve` and keeps the monitor-set `wiki_role: source`.

- `arXiv-2608-09025-SAGE-Fin-Runtime-Governance-Financial-Agents.md` :
  `topic/agentic-ai`, `topic/finance`
- `arXiv-2608-09378-Stablecoin-Transaction-Scaling-Laws-Ethereum.md` :
  `topic/finance/stablecoins`, `topic/blockchain-settlement`
- `arXiv-2608-11344-Governing-Agentic-AI-FinTech.md` :
  `topic/agentic-ai`, `topic/finance`
- `fed-2025-090-generative-ai-financial-stability-animal-spirits.md` :
  `topic/agentic-ai`, `topic/finance`, `subject/federal-reserve`
- `Ledger-Insights-Africa-Finance-Corporation-CHF-Digital-Bond-SIX-SDX.md` :
  `topic/finance/market-infrastructure`, `topic/tokenisation`
- `Ledger-Insights-Brazil-24-Hour-Delay-Crypto-Stablecoin-Transfers.md` :
  `topic/finance/stablecoins`, `topic/law`
- `Ledger-Insights-Marketnode-BNY-Funds-Stellar.md` :
  `topic/finance/market-infrastructure`, `topic/tokenisation`
- `Ledger-Insights-Nasdaq-LeveL-Markets-Acquisition-Tokenization.md` :
  `topic/finance/market-infrastructure`, `topic/tokenisation`
- `Ledger-Insights-SEC-Franklin-Templeton-BENJI-Cash-Sweep.md` :
  `topic/finance/market-infrastructure`, `topic/tokenisation`
- `Ledger-Insights-SEC-Postpones-Tokenized-Securities-Exemption.md` :
  `topic/law/securities`, `topic/tokenisation`
- `Ledger-Insights-StanChart-Anchorpoint-HKDAP-Stablecoin-Beta.md` :
  `topic/finance/stablecoins`, `topic/tokenisation`
- `Ledger-Insights-UK-FCA-Tokenized-Gold-Collateral.md` :
  `topic/finance/market-infrastructure`, `topic/law/property-rights`,
  `topic/tokenisation`

## Newly tagged concepts (60)

Every `30_Concepts/` stub now carries `wiki_role: concept`, a hash, an
index stamp, and one to two topics. Topic frequency across the layer:
carbon-credits 12, stablecoins 10, blockchain-settlement 9, law 8,
agentic-ai 6, property-rights 6, real-estate 6, finance 4,
digital-assets 4, tokenisation 1, tokenised-deposits 1.

Four stubs are pinned in `NOTE_OVERRIDES` where the MOC-derived topic
missed the concept's own home:

- `Tokenisation.md` : `topic/tokenisation`, `topic/finance`
- `Tokenised-Deposit.md` : `topic/finance/tokenised-deposits`
- `E-Money-Token.md` : `topic/law`, `topic/finance/stablecoins`
- `Asset-Referenced-Token.md` : `topic/law`, `topic/finance/stablecoins`

## Changes to the builder

1. **Fresh notes confirm monitor topics.** A fresh note whose existing
   topics are all in the 14-topic vocabulary is confirmed as-is. Six of
   this week's twelve sources would otherwise have drifted under the
   mapper's tie-breaks (`topic/law/securities` or `topic/law` in place of
   `topic/tokenisation`; `topic/finance/market-infrastructure` alongside
   stablecoins). Per-note pinning no longer scales at eight to twelve
   sources a week, so this replaces it for the fresh case.
2. **`30_Concepts/` enters scope.** Concept stubs get `wiki_role: concept`.
   Their `domain` field holds MOC section labels (`examples` on 24 stubs,
   `sub-topic` on 15) as well as enum values, so topics derive from the
   MOCs each stub links to (new `MOC_TOPIC` table) plus any enum domain
   value, parent-pruned and capped at three.
3. `OVERRIDES`, the mapping tables, and `QUARANTINE` are otherwise
   unchanged from the 9 August builder.

## Pending Topic candidates

None. The off-vocabulary sweep across all 307 notes found zero values
outside the 14-topic controlled vocabulary. The vocabulary stands at
14 topics and 31 subjects.

## Pending schema issue: concept `domain` values

39 of the 60 concept stubs carry `examples` or `sub-topic` in `domain`.
Those are MOC section headings that leaked in when the 9 August build
assigned domain "from the referencing MOC". Schema §2.4 requires domain
enum values (§2.7). `30_Concepts/` is user-owned, so this refresh left the
field alone and routed around it via `MOC_TOPIC`. Options: strip the two
labels and backfill from the assigned topics, or accept them as informal
labels and note the exception in `schema.md`.

## MOC candidates

`50_MOCs/` is user-owned, so this refresh wrote no MOC changes. None of the
twelve new sources carries a wikilink from any MOC. Candidate placements by
assigned topic:

**MOC - Agentic-AI**
- [[arXiv-2608-09025-SAGE-Fin-Runtime-Governance-Financial-Agents]]
- [[arXiv-2608-11344-Governing-Agentic-AI-FinTech]]
- [[fed-2025-090-generative-ai-financial-stability-animal-spirits]]

**MOC - Blockchain-Settlement**
- [[arXiv-2608-09378-Stablecoin-Transaction-Scaling-Laws-Ethereum]]

**MOC - Finance**
- [[Ledger-Insights-Africa-Finance-Corporation-CHF-Digital-Bond-SIX-SDX]]
- [[Ledger-Insights-Marketnode-BNY-Funds-Stellar]]
- [[Ledger-Insights-Nasdaq-LeveL-Markets-Acquisition-Tokenization]]
- [[Ledger-Insights-SEC-Franklin-Templeton-BENJI-Cash-Sweep]]
- [[Ledger-Insights-UK-FCA-Tokenized-Gold-Collateral]]
- [[arXiv-2608-09025-SAGE-Fin-Runtime-Governance-Financial-Agents]]
- [[arXiv-2608-11344-Governing-Agentic-AI-FinTech]]
- [[fed-2025-090-generative-ai-financial-stability-animal-spirits]]

**MOC - Law**
- [[Ledger-Insights-Brazil-24-Hour-Delay-Crypto-Stablecoin-Transfers]]
- [[Ledger-Insights-SEC-Postpones-Tokenized-Securities-Exemption]]

**MOC - Property-Rights**
- [[Ledger-Insights-UK-FCA-Tokenized-Gold-Collateral]]

**MOC - Stablecoins**
- [[Ledger-Insights-Brazil-24-Hour-Delay-Crypto-Stablecoin-Transfers]]
- [[Ledger-Insights-StanChart-Anchorpoint-HKDAP-Stablecoin-Beta]]
- [[arXiv-2608-09378-Stablecoin-Transaction-Scaling-Laws-Ethereum]]

## Next steps

1. Add the MOC candidate links above to the hand-curated MOCs.
2. Decide the concept `domain` question (strip and backfill, or document
   the exception).
3. No Topic decisions are outstanding.
