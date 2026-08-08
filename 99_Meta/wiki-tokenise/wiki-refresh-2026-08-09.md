---
title: Wiki refresh report 2026-08-09
type: report
date: 2026-08-09
tags:
  - metadata
  - wiki-refresh
auto_generated: true
---

# Wiki refresh report, 9 August 2026

This refresh indexed the three sources the R7 monitor run added on 9 August
and re-stamped ten notes whose metadata that run updated. It tagged 3 notes,
re-stamped 10, quarantined nothing, and wrote nothing to user-owned files.
Working artefacts sit in `99_Meta/wiki-tokenise/`. The plan builder is
`build-apply-plan-2026-08-09.py`, adapted from the 2 August builder.

## Scan

- First scan: 235 notes; 6 fresh, 10 modified, 219 unchanged, 0 quarantined.
- 13 targets after filtering. `SOURCE-REGISTER.md`, `_CLAUDE.md`, and
  `README.md` fall outside the tagging scope by design.
- Applied via `apply_wiki.py`: 13 written, 0 failures.
- Verification re-scan: 235 notes, 232 unchanged, 0 modified; only the three
  by-design out-of-scope files stay fresh.

## Newly tagged

All three fresh sources arrived with on-vocabulary topics written by the
monitors. The plan confirmed them and stamped hashes:

- `arXiv-2608-01341-402Pilot-x402-Agent-Micropayments.md` —
  `topic/agentic-ai`, `topic/blockchain-settlement`
- `arXiv-2608-02311-AI-Governance-Institutional-Readiness-Finance.md` —
  `topic/agentic-ai`, `topic/finance`
- `IMF-Speech-2026-08-Katz-Stablecoins-Emerging-Markets.md` —
  `topic/finance/stablecoins`, `topic/finance`, plus `subject/imf`

## Changes to the builder

- `NOTE_OVERRIDES` gained a pin for the IMF Katz speech. Its
  domain values (`stablecoins`, `cross-border-payments`, `monetary-policy`,
  `finance`) would have led the mapper's parent-pruning to output
  `topic/finance/stablecoins` plus `topic/tokenisation`; the pin keeps the
  monitor's correct pair instead.
- `OVERRIDES`, the mapping tables, and `QUARANTINE` are unchanged from the
  2 August builder.

## Re-stamp only

Ten notes from the R7 metadata update already carried topics, so the builder
re-stamped hashes without changing them:

- `mas-parliamentary-reply-agentic-ai-2026.md`
- `mas-parliamentary-reply-vasp-aml-2026.md`
- `Ledger-Insights-Bank-of-Korea-Tokenization-Task-Force.md`
- `Ledger-Insights-BlackRock-European-Tokenized-MMFs.md`
- `Ledger-Insights-ECB-Project-Pontes-Go-Live.md`
- `Ledger-Insights-SBI-Nodeinfra-Project-Musubi-PvP.md`
- `Ledger-Insights-Schroders-Tokenized-MMF-Ireland.md`
- `Ledger-Insights-SEBI-Tokenization-DLT-Corporate-Bonds.md`
- `Ledger-Insights-Treasury-TBAC-DLT-Intraday-Repo.md`
- `Ledger-Insights-Wells-Fargo-Tokenized-Deposit.md`

## Pending Topic candidates

None. The off-vocabulary sweep across all 235 notes found zero values outside
the 14-topic controlled vocabulary. The nine values pending in the 2 August
report were resolved by the 6 August cleanup. The vocabulary stands at
14 topics and 31 subjects.

## MOC candidates

`50_MOCs/` is user-owned, so this refresh wrote no MOC changes. None of the
three new sources carries a wikilink from any MOC. Candidate placements by
assigned topic:

**MOC - Agentic-AI**
- [[arXiv-2608-01341-402Pilot-x402-Agent-Micropayments]]
- [[arXiv-2608-02311-AI-Governance-Institutional-Readiness-Finance]]

**MOC - Blockchain-Settlement**
- [[arXiv-2608-01341-402Pilot-x402-Agent-Micropayments]]

**MOC - Stablecoins**
- [[IMF-Speech-2026-08-Katz-Stablecoins-Emerging-Markets]]

**MOC - Finance**
- [[arXiv-2608-02311-AI-Governance-Institutional-Readiness-Finance]]
- [[IMF-Speech-2026-08-Katz-Stablecoins-Emerging-Markets]]

## Next steps

1. Add the MOC candidate links above to the hand-curated MOCs.
2. No Topic decisions are outstanding.
