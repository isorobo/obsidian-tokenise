---
title: Wiki refresh 2026-10-11
type: report
date: 2026-10-11
tags: [metadata, wiki-refresh]
auto_generated: true
---

# Wiki refresh 2026-10-11

## Scan

| Measure | Count |
|---|---|
| Notes scanned | 349 |
| Fresh | 21 (18 taggable, 3 never_write) |
| Modified | 0 |
| Unchanged | 328 |
| Quarantined | 0 |
| Orphans | 0 |
| Unique topics / subjects | 14 / 31 |

## Newly tagged

18 notes confirmed by `tk-plan` (all monitor topics on vocabulary): 6 Academia, 4 Central-Banks, 7 Industry-Press, 1 `30_Areas` synthesis note. Subjects added: `subject/esma` (2), `subject/hkma`, `subject/mas`. Apply: 18 applied, 0 unchanged, 0 failed (dry run first; frontmatter only).

Topic frequency in plan: stablecoins 8, market-infrastructure 7, tokenisation 6, agentic-ai 4, blockchain-settlement 2, tokenised-deposits 2, property-rights 2, securities 2, digital-assets 1.

## Re-stamp only

None.

## Pending Topic candidates

None. Off-vocabulary sweep: no values outside the closed 14-topic set.

## Schema issues

- `10_Sources/Law-Regulation/US-Anti-CBDC-Surveillance-State-Act-2025.md` carries 4 topics, over the cap of 3 (pre-existing; reported, not fixed).
- No unknown enum values in this cycle.

## MOC candidates

Suggest mode; nothing written under `50_MOCs/`. 28 candidate links from 18 notes, none already linked, none unmapped. Written to `wiki-moc-candidates-2026-10-11.json`.

- **MOC - Stablecoins:** [[arXiv-2604-17167-Hidden-Plumbing-Stablecoins-GENIUS-Act-Era]], [[arXiv-2605-00071-Compliance-Aware-Agentic-Payments-Stablecoin-Rails]], [[arXiv-2609-18949-StableEval-Arena-Stablecoin-Stability-Benchmark]], [[arXiv-2610-02435-SoK-Stablecoins-Quantum-Era]], [[arXiv-2610-03841-Dexy-Algorithmic-Central-Bank-Stablecoin]], [[ESMA-Opinion-Services-Non-MiCA-Compliant-Stablecoins-2026]], [[HKMA-Bank-Negara-Malaysia-Cooperation-Stablecoin-Tokenisation-2026]], [[Synthesis — Stablecoin Sources 2026]]
- **MOC - Finance:** [[arXiv-2604-17167-Hidden-Plumbing-Stablecoins-GENIUS-Act-Era]], [[ESMA-Call-Evidence-Tokenised-Collateral-Central-Clearing-2026]], [[Ledger-Insights-Ant-International-Tokenized-Deposits-HSBC-OCBC]], [[Ledger-Insights-CBMT-Sandbox-DNB-Commercial-Bank-Dubai]], [[Ledger-Insights-CFTC-FAQ-Tokenized-MMF-Treasuries-Customer-Funds]], [[Ledger-Insights-Clearstream-Tokenization-Settlement-Custody-Collateral]], [[Ledger-Insights-Korea-FSC-Draft-Tokenization-Rules]], [[Ledger-Insights-Securitize-Tokenized-US-Stocks-Entitlements]], [[Ledger-Insights-StanChart-Singapore-Digital-Asset-Custody]]
- **MOC - Agentic-AI:** [[arXiv-2605-00071-Compliance-Aware-Agentic-Payments-Stablecoin-Rails]], [[arXiv-2608-30519-Authority-Inference-Separation-Agentic-Finance]], [[arXiv-2609-18949-StableEval-Arena-Stablecoin-Stability-Benchmark]], [[MAS-Guidelines-AI-Risk-Management-Financial-Institutions-2026]]
- **MOC - Blockchain-Settlement:** [[arXiv-2608-30519-Authority-Inference-Separation-Agentic-Finance]], [[Ledger-Insights-Clearstream-Tokenization-Settlement-Custody-Collateral]]
- **MOC - Law:** [[Ledger-Insights-Korea-FSC-Draft-Tokenization-Rules]], [[Ledger-Insights-Securitize-Tokenized-US-Stocks-Entitlements]]
- **MOC - Property-Rights:** [[Ledger-Insights-CFTC-FAQ-Tokenized-MMF-Treasuries-Customer-Funds]], [[Ledger-Insights-StanChart-Singapore-Digital-Asset-Custody]]
- **MOC - Private-Law-Convergence:** [[ESMA-Opinion-Services-Non-MiCA-Compliant-Stablecoins-2026]]

## Housekeeping observations

- Verify ok: 3 notes remain fresh, all `never_write` (`SOURCE-REGISTER.md`, `README.md`, `_CLAUDE.md`). No unexpected paths, no stubs.
- `_wiki/` did not exist before this run and does not exist now.

## Working tree

28 dirty paths (uncommitted). Suggested commit message: `chore(wiki): tag 18 notes, wiki-refresh 2026-10-11`.

## Pending your decision

- Topic approvals: none open.
- Cap violation on the US Anti-CBDC note: strip a topic or accept.
- Watchlist cadence and surface edits recommended by monitors (none raised in this stage).
- Schema values such as `ZA` jurisdiction remain unadded.
- Auto-commit on or off.
- SOURCE-REGISTER stays frozen, or opt in to a register-link step.

## Next steps

Review and commit the working tree; link the MOC candidates into the hand-curated MOCs as wanted.
