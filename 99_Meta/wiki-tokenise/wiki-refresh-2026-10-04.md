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
| Notes scanned | 308 |
| Fresh (before apply) | 4 |
| Modified (before apply) | 1 |
| Unchanged (before apply) | 303 |
| Orphans | 0 |
| Quarantined | 0 |
| Stubs | 0 |
| Topics in use / subjects in use | 14 / 31 |

After apply, the verify scan shows 3 fresh notes, all `never_write` files (`SOURCE-REGISTER.md`, `README.md`, `_CLAUDE.md`), and no unexpected paths.

## Newly tagged

- `10_Sources/Industry-Press/Ledger-Insights-Treasury-State-Stablecoin-Certification-GENIUS-Act.md`: topics confirmed as `topic/finance/stablecoins`, `topic/law`; `wiki_role` and stamps added. No subject (press, excluded from publisher subjects).

## Re-stamp only

- `10_Sources/Central-Banks/hkma-digital-green-bond-2025.md`: body changed, already tagged (`topic/finance/cbdc`, `topic/blockchain-settlement`); hash and indexed time refreshed, no topics added.

## Pending Topic candidates

None. No off-vocabulary topic values; `unknown_enum_values` empty.

## Schema issues

- The scan reports `cap_violations: 1` (a note over the 3-topic cap after merge). The note is not named in the scan summary; check `wiki-scan-2026-10-04.json`. Nothing was changed.

## MOC candidates

Suggest mode only; `50_MOCs/` was not written.

- MOC - Law: [[Ledger-Insights-Treasury-State-Stablecoin-Certification-GENIUS-Act]]
- MOC - Stablecoins: [[Ledger-Insights-Treasury-State-Stablecoin-Certification-GENIUS-Act]]

Unmapped: none. One of the two planned notes was already linked from a MOC.

## Housekeeping observations

- `_wiki/` does not exist (not resurrected).
- Dated `build-apply-plan-*.py` copies remain in this folder as read-only evidence; `tk-plan` was used instead.

## Working tree

7 uncommitted paths (includes this cycle's two frontmatter edits and the scan, plan, verify, candidate and report files). Nothing was committed.

## Pending your decision

- Watchlist cadence and surface edits recommended by monitors (none raised in this stage).
- Adding schema values such as a `ZA` jurisdiction.
- Auto-commit on or off.
- SOURCE-REGISTER stays frozen, or an opt-in register-link step.
- Identify and resolve the one topic-cap violation.

## Next steps

Review the two MOC candidates and add the links to `MOC - Law` and `MOC - Stablecoins` by hand. Suggested commit message: `chore(wiki): Oct refresh, tag 1 source, re-stamp 1`.
