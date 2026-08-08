---
title: Wiki refresh report 2026-08-02
type: report
date: 2026-08-02
tags:
  - metadata
  - wiki-refresh
auto_generated: true
---

# Wiki refresh report, 2 August 2026

This refresh caught up on the eight Ledger Insights notes the 26 July monitor
run wrote after that morning's wiki refresh had already completed. It tagged
3 notes, re-stamped 7, repaired one quarantined synthesis note, and wrote
nothing to user-owned files. Working artefacts sit in `99_Meta/wiki-tokenise/`.
The plan builder is `build-apply-plan-2026-08-02.py`, adapted from the 26 July
builder.

## Scan

- First scan: 221 notes; 4 fresh, 8 modified, 209 unchanged, 1 quarantined.
- Quarantine repair: `30_Areas/Synthesis — Agentic AI and Tokenised Settlement
  Infrastructure.md` carried malformed YAML (a quoted scalar with trailing
  text in `related-sources`). The offending line was re-quoted; no body text
  changed. Re-scan: 222 notes, 5 fresh, 8 modified, 0 quarantined.
- 10 targets after filtering. `SOURCE-REGISTER.md`, `_CLAUDE.md`, and
  `README.md` fall outside the tagging scope by design.
- Applied via `apply_wiki.py`: 10 written, 0 failures.
- Verification re-scan confirms 0 untagged targets remain in `10_Sources/`
  and `30_Areas/`; only the three by-design out-of-scope files stay fresh.

## Changes to the builder

- `OVERRIDES` gained the repaired synthesis note, classified by hand:
  `topic/agentic-ai`, `topic/blockchain-settlement`,
  `topic/finance/stablecoins`.
- `NOTE_OVERRIDES` pins two notes whose monitor-written topics missed the
  canonical vocabulary: `hkma-quantum-preparedness-whitepaper-2026` (gains
  canonical `topic/blockchain-settlement` alongside the off-vocabulary
  `topic/finance/blockchain-settlement`) and
  `Ledger-Insights-Circle-NY-Trust-Charter` (gains canonical `topic/law`
  alongside `topic/law/licensing`).
- The `NOTE_OVERRIDES` check now runs before the re-stamp branch, so a pinned
  modified note still gains its canonical topics. The 26 July builder checked
  the other way round.
- `QUARANTINE` remains empty.

## Re-stamp only

Seven Ledger Insights notes from the 26 July monitor run already carried
topics, so the builder re-stamped hashes without changing them:

- `Ledger-Insights-Aviva-Investors-Tokenized-MMF-XRP-Ledger.md`
- `Ledger-Insights-BIS-Project-Agora-Real-Money-Trials.md`
- `Ledger-Insights-BPI-Stablecoin-Remittances.md`
- `Ledger-Insights-Partior-OpenAssets-Tokenized-Deposit-Clearing.md`
- `Ledger-Insights-POSCO-LG-CNS-Trade-Finance-Blockchain-Pilot.md`
- `Ledger-Insights-RL1-Cecabank-Credit-Mutuel-Launch.md`
- `Ledger-Insights-Visa-Pismo-Stablecoin-Integration.md`

## Pending Topic candidates

The off-vocabulary sweep found nine values outside the 14-topic controlled
vocabulary: five carried over from the 26 July report (still undecided) and
four new this week. The apply step preserved them and appended canonical
equivalents. Each needs a decision: approve as new vocabulary, or strip.

| Off-vocabulary value | Note | Canonical topic now present | Suggested disposition |
|---|---|---|---|
| `topic/finance/blockchain-settlement` | hkma-quantum-preparedness-whitepaper-2026 | `topic/blockchain-settlement` | Strip; duplicate of canonical (new) |
| `topic/finance/cross-border-payments` | Ledger-Insights-BPI-Stablecoin-Remittances | `topic/finance/stablecoins` | Strip, or approve if payments sources keep arriving (new) |
| `topic/finance/tokenised-funds` | Ledger-Insights-Aviva-Investors-Tokenized-MMF | `topic/finance/market-infrastructure` | Strip; covered by canonical (new) |
| `topic/law/licensing` | Ledger-Insights-Circle-NY-Trust-Charter | `topic/law` | Strip; covered by canonical (new) |
| `topic/finance/tokenised-fund` | Ledger-Insights-Mubadala-Capital-KAIO | `topic/finance/market-infrastructure` | Strip; covered by canonical (carried over) |
| `topic/law/securities-law` | Ledger-Insights-SEC-Peirce-DeFi-Vault-Curators | `topic/law/securities` | Strip; near-duplicate of canonical (carried over) |
| `topic/finance/defi` | Ledger-Insights-SEC-Peirce-DeFi-Vault-Curators | `topic/blockchain-settlement` | Strip, or approve if DeFi deserves its own branch (carried over) |
| `topic/finance/tokenised-equity` | Ledger-Insights-xStocks-Expands-Tokenized-Stocks | `topic/law/securities` | Strip; covered by canonical (carried over) |
| `topic/finance/monetary-policy` | BIS-WP1370-Dollarisation-Monetary-Control-Stablecoins | `topic/finance/stablecoins` | Strip, or approve if monetary-policy sources keep arriving (carried over) |

## MOC candidates

`50_MOCs/` is user-owned, so this refresh wrote no MOC changes. None of the
10 notes in this week's plan carries a wikilink from any MOC. Candidate
placements by assigned topic:

**MOC - Stablecoins**
- [[Ledger-Insights-BPI-Stablecoin-Remittances]]
- [[Ledger-Insights-Circle-NY-Trust-Charter]]
- [[Ledger-Insights-Partior-OpenAssets-Tokenized-Deposit-Clearing]]
- [[Ledger-Insights-Visa-Pismo-Stablecoin-Integration]]

**MOC - Blockchain-Settlement**
- [[Ledger-Insights-BIS-Project-Agora-Real-Money-Trials]]
- [[Ledger-Insights-RL1-Cecabank-Credit-Mutuel-Launch]]
- [[hkma-quantum-preparedness-whitepaper-2026]]

**MOC - Finance**
- [[Ledger-Insights-Aviva-Investors-Tokenized-MMF-XRP-Ledger]]
- [[Ledger-Insights-POSCO-LG-CNS-Trade-Finance-Blockchain-Pilot]]
- [[Ledger-Insights-Partior-OpenAssets-Tokenized-Deposit-Clearing]]

**MOC - Agentic-AI**
- [[Synthesis — Agentic AI and Tokenised Settlement Infrastructure]]
- [[Ledger-Insights-POSCO-LG-CNS-Trade-Finance-Blockchain-Pilot]]

**MOC - Law**
- [[Ledger-Insights-Circle-NY-Trust-Charter]]

## Next steps

1. Decide the nine pending Topic candidates above; strip or approve each.
   Five have now waited two weeks.
2. Add the MOC candidate links above to the hand-curated MOCs.
