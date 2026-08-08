---
title: Wiki refresh report 2026-07-26
type: report
date: 2026-07-26
tags:
  - metadata
  - wiki-refresh
auto_generated: true
---

# Wiki refresh report, 26 July 2026

This refresh followed the weekly `run all` haul of the same morning, which added
new source notes across four channels (Ledger Insights, IMF blog, BIS Working
Papers, UNIDROIT). It tagged 10 notes, re-stamped 1, and wrote nothing to
user-owned files. Working artefacts sit in `99_Meta/wiki-tokenise/`. The plan
builder is `build-apply-plan-2026-07-26.py`, adapted from the 19 July builder.

## Scan

- 212 notes scanned; 13 fresh, 1 modified, 198 unchanged.
- 11 targets after filtering. `SOURCE-REGISTER.md`, `_CLAUDE.md`, and
  `README.md` fall outside the tagging scope by design.
- Applied via `apply_wiki.py`: 11 written, 0 failures.
- Re-scan confirms 0 untagged targets remain in `10_Sources/` and `30_Areas/`.
- No new `30_Areas/` synthesis notes this week, so the OVERRIDES table was
  unchanged.

## Changes to the builder

- The monitors wrote `topic` values directly into eight of the fresh notes.
  Five of those values sit outside the 14-topic controlled vocabulary (see
  Pending Topic candidates). `apply_wiki.py` appends and dedupes but never
  removes, so the builder supplied canonical topics alongside them.
- A `NOTE_OVERRIDES` table pins two notes where the deterministic mapper would
  misfire: `SEC-Peirce-DeFi-Vault-Curators` (pinned to `topic/law/securities`
  and `topic/blockchain-settlement`) and `xStocks-Expands-Tokenized-Stocks`
  (pinned to `topic/law/securities`).
- `QUARANTINE` remains empty.

## Re-stamp only

One modified note already carried topics, so the builder re-stamped the hash
without changing them:

- `BIS-WP1370-Dollarisation-Monetary-Control-Stablecoins.md`

## Pending Topic candidates

The off-vocabulary sweep found five topic values outside the controlled
vocabulary, all written by the monitors into this week's notes. The apply
step preserved them and appended the canonical equivalents. Each needs a
decision: approve as new vocabulary, or strip from the note.

| Off-vocabulary value | Note | Canonical topic now present | Suggested disposition |
|---|---|---|---|
| `topic/finance/tokenised-fund` | Ledger-Insights-Mubadala-Capital-KAIO | `topic/finance/market-infrastructure` | Strip; covered by canonical |
| `topic/law/securities-law` | Ledger-Insights-SEC-Peirce-DeFi-Vault-Curators | `topic/law/securities` | Strip; near-duplicate of canonical |
| `topic/finance/defi` | Ledger-Insights-SEC-Peirce-DeFi-Vault-Curators | `topic/blockchain-settlement` | Strip, or approve if DeFi deserves its own branch |
| `topic/finance/tokenised-equity` | Ledger-Insights-xStocks-Expands-Tokenized-Stocks | `topic/law/securities` | Strip; covered by canonical |
| `topic/finance/monetary-policy` | BIS-WP1370-Dollarisation-Monetary-Control-Stablecoins | `topic/finance/stablecoins` | Strip, or approve if monetary-policy sources keep arriving |

## MOC candidates

`50_MOCs/` is user-owned, so this refresh wrote no MOC changes. The 11 newly
tagged or re-stamped notes lack a wikilink from any MOC. Candidate placements
by assigned topic:

**MOC - Finance**
- [[Ledger-Insights-BNY-247-Treasury-Settlement-Tokenization]]
- [[Ledger-Insights-Hanwha-Largest-Investor-Securitize]]
- [[Ledger-Insights-Mubadala-Capital-KAIO-Tokenized-Private-Markets]]
- [[Ledger-Insights-StanChart-Shinhan-Backers-Digital-Asset-Canton]]
- [[Ledger-Insights-xStocks-Expands-Tokenized-Stocks-Outside-US]]

**MOC - Stablecoins**
- [[Ledger-Insights-ECB-Cipollone-Digital-Euro-Stablecoin-Shield]]
- [[Ledger-Insights-JPYC-Japanese-Logistics-Driver-Payments]]
- [[BIS-WP1370-Dollarisation-Monetary-Control-Stablecoins]]

**MOC - Blockchain-Settlement**
- [[Ledger-Insights-BNY-247-Treasury-Settlement-Tokenization]]
- [[Ledger-Insights-StanChart-Shinhan-Backers-Digital-Asset-Canton]]
- [[Ledger-Insights-SEC-Peirce-DeFi-Vault-Curators-Securities-Law]]

**MOC - Law**
- [[Ledger-Insights-SEC-Peirce-DeFi-Vault-Curators-Securities-Law]]
- [[Ledger-Insights-xStocks-Expands-Tokenized-Stocks-Outside-US]]
- [[Ledger-Insights-Hanwha-Largest-Investor-Securitize]]

**MOC - Agentic-AI**
- [[IMF-Adrian-AI-Financial-Stability-Blog-2026-07]]

**MOC - Carbon-Credits**
- [[UNIDROIT-VCC-ISDA-Presentation-Press-Release-2026]]

**MOC - Property-Rights**
- [[UNIDROIT-VCC-ISDA-Presentation-Press-Release-2026]]

**MOC - Private-Law-Convergence**
- [[UNIDROIT-VCC-ISDA-Presentation-Press-Release-2026]]

## Next steps

1. Decide the five pending Topic candidates above; strip or approve each.
2. Add the MOC candidate links above to the hand-curated MOCs.
