---
title: Wiki refresh report 2026-07-12
type: report
date: 2026-07-12
tags:
  - metadata
  - wiki-refresh
auto_generated: true
---

# Wiki refresh report, 12 July 2026

For future Claude: this report records the first wiki-refresh after the vault restructure that archived `_wiki/` to `_archived_wiki-old-structure/`. The refresh tagged 23 notes, re-stamped 11, and wrote nothing to user-owned files. Working artefacts now live in `99_Meta/wiki-tokenise/`.

## Scan

- 182 notes scanned; 27 fresh, 11 modified, 144 unchanged.
- Plan builder: `build-apply-plan-2026-07-12.py` (adapted from the archived `_build_plan.py`; scan and plan JSONs sit beside it).
- Applied via `apply_wiki.py`: 34 written, 0 failures. Re-scan confirms 178 of 182 unchanged.
- Excluded from tagging: `SOURCE-REGISTER.md` (user-owned), `_CLAUDE.md`, `README.md` (system files).

## Quarantine

- `10_Sources/Commercial-Banks/AWS-Bedrock-AgentCore-Payments.md` is an empty file (0 bytes). Unclassifiable. Delete it or re-fetch the source.

## Pending Topic candidates

Six notes carry topics outside the 14-topic controlled vocabulary. Upstream processes wrote these before this refresh; the refresh preserved them and added controlled topics beside them. Approve, merge, or normalise:

**Genuine candidates (new topics for the vocabulary):**

| Candidate | Notes | Alternative |
|---|---|---|
| `topic/regulation/federal-us` | US-GENIUS-Act-2025-Comprehensive, US-Anti-CBDC-Surveillance-State-Act-2025 | fold into `topic/law` |
| `topic/finance/payment-systems` | US-GENIUS-Act-2025-Comprehensive | fold into `topic/finance` |
| `topic/finance/monetary-policy` | US-Anti-CBDC-Surveillance-State-Act-2025 | fold into `topic/finance` |

**Mis-nested variants (normalise to existing vocabulary):**

| Variant | Note | Existing topic |
|---|---|---|
| `topic/finance/agentic-ai` | mas-safr-agentic-finance-safeguards-2026 | `topic/agentic-ai` |
| `topic/finance/blockchain-settlement` | IMF-WP-2026-136-FMI-Evolution-Tokenized-Economy | `topic/blockchain-settlement` |
| `topic/finance/tokenisation` | IMF-Note-2026-006-Rise-of-Tokenization | `topic/tokenisation` |

## MOC candidates

`50_MOCs/` is user-owned, so this refresh wrote no MOC changes. All 23 newly tagged notes lack a wikilink from any MOC. Candidate placements by assigned topic:

**MOC - Stablecoins**
- [[esma-casp-custody-digital-operational-resilience-csa-2026]]
- [[esma-mica-register-post-deadline-update-2026]]
- [[Ledger-Insights-Brazil-Central-Bank-Stablecoin-Changes]]
- [[Ledger-Insights-Circle-OCC-Final-Approval-Trust-Bank]]
- [[Ledger-Insights-EU-Parliament-Stablecoin-Multi-Issuance]]
- [[Ledger-Insights-FAB-UAE-DDSC-Stablecoin-Retail-Rollout]]
- [[Ledger-Insights-Sony-Bank-OCC-Conditional-Approval-Stablecoin]]
- [[US-GENIUS-Act-2025-Comprehensive]]
- [[FSB-Moloney-Cross-Border-Payments-Next-Chapter-2026]]
- [[Synthesis — Stablecoin Architecture Evolution]]

**MOC - Law**
- [[HKMA-FSTB-DLT-Fixed-Income-Market-Review-2026]]
- [[Ledger-Insights-Ondo-Tokenized-US-Stocks-Ownership-Rights]]
- [[Synthesis — Regulatory Pathways by Jurisdiction]]
- [[Synthesis — Tokenised Securities vs Real-World Assets]]

**MOC - Finance**
- [[Ledger-Insights-BlackRock-Citi-Tokenized-MMF-Collateral-GDF-ISDA]]
- [[Ledger-Insights-Swift-Blockchain-Tokenized-Deposits-Pilot]]
- [[US-Anti-CBDC-Surveillance-State-Act-2025]]

**MOC - Blockchain-Settlement**
- [[Storm Research — Automated Token and RWA Transfers]]
- [[Synthesis — Interoperability and Cross-Chain Fragmentation]]
- [[Synthesis — Settlement Efficiency and Cost Reduction]]

**MOC - Agentic-AI**
- [[FSB-Bowman-AI-Sound-Practices-Remarks-2026]]

**MOC - Carbon-Credits**
- [[Synthesis — Carbon Credits as Tokenisation Test Bed]]

**MOC - Private-Law-Convergence**
- [[Synthesis — Private Law Convergence Across Jurisdictions]]

## Next steps

1. Decide the three pending Topic candidates (approve or fold).
2. Normalise the three mis-nested variants in their six notes.
3. Add the MOC candidate links above to the hand-curated MOCs.
4. Delete or re-fetch the empty AWS Bedrock note.
