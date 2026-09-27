---
title: Wiki refresh report 2026-08-23
type: report
date: 2026-08-23
tags:
  - metadata
  - wiki-refresh
auto_generated: true
---

# Wiki refresh report, 23 August 2026

This refresh found nothing to tag. No monitor has run since 17 August (every
channel state file carries `last_run_at: 2026-08-17`), no in-scope note
changed since the 17 August verify scan, and the vault holds the same 307
notes. The refresh wrote no frontmatter, built no plan, quarantined nothing,
and touched no user-owned MOC or register. The scan artefact is
`wiki-scan-2026-08-23.json`; no builder or apply plan exists for this date
because there was nothing to apply.

## Scan

- 307 notes; 3 fresh, 0 modified, 304 unchanged, 0 quarantined, 0 orphans.
- The three fresh notes are `10_Sources/SOURCE-REGISTER.md`, `_CLAUDE.md`,
  and `README.md`, which sit outside the tagging scope by design. They have
  shown as fresh in every refresh since 12 July.
- Targets after filtering: 0. `apply_wiki.py` was not run.
- Vocabulary in use: 14 topics, 31 subjects. Unchanged from 17 August.

## Newly tagged sources

None.

## Pending Topic candidates

None. The off-vocabulary sweep of `existing_topics` across all 307 notes
found zero values outside the 14-topic controlled vocabulary.

## Pending schema issue: concept `domain` values (carried forward)

39 of the 60 `30_Concepts/` stubs still carry `examples` or `sub-topic` in
`domain`. The 17 August report set out the two options: strip the two labels
and backfill from the assigned topics, or document the exception in
`schema.md`. `30_Concepts/` is user-owned, so this refresh left the field
alone. The `MOC_TOPIC` table in `build-apply-plan-2026-08-17.py` remains the
workaround for any future concept stub.

## MOC candidates (carried forward from 17 August)

None of the twelve sources tagged on 17 August has gained a wikilink from
any file in `50_MOCs/`. The candidate placements stand as listed in
`wiki-refresh-2026-08-17.md`:

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

## Housekeeping observations

- The 17 August haul (twelve source notes and five `99_Meta/wiki-tokenise/`
  artefacts) and the 17 August concept stamps (60 modified files in
  `30_Concepts/`) are uncommitted. `git status` shows 79 changed paths.
- `99_Meta/wiki-tokenise/README.md` lines 41 to 42 still describe
  `weekly-refresh` as running `notebooklm-sync all`. That step was retired on
  9 August (commit d756e30). The README is stale on that point.

## Next steps

1. Run `/wiki-tokenise run all` (or wait for the Sunday cron) so the next
   refresh has material to tag.
2. Add the carried-forward MOC candidate links to the hand-curated MOCs.
3. Decide the concept `domain` question.
4. Commit the 17 August haul and stamps.
5. Correct README lines 41 to 42 to drop `notebooklm-sync` from the
   `weekly-refresh` sequence.
