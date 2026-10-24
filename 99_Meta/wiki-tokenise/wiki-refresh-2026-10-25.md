---
title: Wiki refresh report 2026-10-25
type: report
date: 2026-10-25
tags: [metadata, wiki-refresh]
auto_generated: true
---

# Wiki refresh report: 2026-10-25

## Scan

| Measure | Count |
|---|---|
| Notes scanned | 401 |
| Fresh (before apply) | 39 |
| Modified | 0 |
| Unchanged | 362 |
| Orphans | 0 |
| Quarantined | 0 |
| Tag targets | 36 |
| Re-stamp targets | 0 |

The 3 fresh notes left after apply are the `never_write` files: `10_Sources/SOURCE-REGISTER.md`, `README.md` and `_CLAUDE.md`.

## Newly tagged

36 notes tagged and stamped by `tk-plan` then `apply` (0 failed). All were confirmed from on-vocabulary monitor topics. Subjects added to 9 notes (`subject/bis`, `subject/fsb`, `subject/imf`, `subject/federal-reserve`).

Topic frequency in the plan: stablecoins 21, market-infrastructure 10, finance 7, law/digital-assets 6, tokenised-deposits 6, cbdc 6, tokenisation 5, agentic-ai 4, blockchain-settlement 3, law 2.

## Re-stamp only

None.

## Pending Topic candidates

None. No off-vocabulary values and no held notes.

## Schema issues

- Cap violation: `10_Sources/Law-Regulation/US-Anti-CBDC-Surveillance-State-Act-2025.md` carries 4 topics (cap is 3). Legacy note, not changed by this run.

## MOC candidates

Suggest mode only; `50_MOCs/` was not written. 62 candidate links across 36 notes, none already linked, none unmapped. Full list in `wiki-moc-candidates-2026-10-25.json`. Counts by target MOC:

| MOC | Candidates |
|---|---|
| MOC - Stablecoins | 22 |
| MOC - Finance | 21 |
| MOC - Private-Law-Convergence | 6 |
| MOC - CBDC | 6 |
| MOC - Agentic-AI | 4 |
| MOC - Blockchain-Settlement | 3 |
| MOC - Law | 2 |

## Housekeeping observations

- `_wiki/` does not exist (not resurrected).
- Verify: ok, no unexpected paths.

## Working tree

46 uncommitted paths. Nothing was committed. Suggested message: `chore(wiki): weekly refresh 2026-10-25, 36 notes tagged`.

## Pending your decision

- Add or remove a topic on `US-Anti-CBDC-Surveillance-State-Act-2025.md` to meet the cap of 3.
- Place the 62 MOC candidates by hand in `50_MOCs/`.
- Commit the working tree.
- Standing: watchlist edits recommended by monitors, schema values such as `ZA`, auto-commit on or off, SOURCE-REGISTER frozen or opt-in.

## Next steps

Review MOC candidates, then commit.
