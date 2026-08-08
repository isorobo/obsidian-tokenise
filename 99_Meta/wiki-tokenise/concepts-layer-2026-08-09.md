---
title: Concepts layer build and MOC link repair
type: report
date: 2026-08-09
tags:
  - metadata
  - wiki-refresh
  - concepts
---

# Concepts layer build, 9 August 2026

The MOCs carried 75 broken wikilink targets. The cause was structural, not
clerical: `30_Concepts/` appears in `schema.md` §1 but was never created, and
`40_Domains/` holds no notes. The MOCs had been written against a layer that
did not exist.

## Fix applied, in three tiers

### Tier 1: repoint to notes that already existed (9 targets)

No new files. Each of these had a home in the corpus under a different name.

| Broken link | Repointed to |
|---|---|
| `Agent-Economy-arXiv` | `arXiv-Agent-Economy-Blockchain-Foundation` |
| `Autonomous-Agents-Blockchain-arXiv` | `arXiv-2601-04583-Autonomous-Agents-Blockchains` |
| `GENIUS-Act` | `US-GENIUS-Act-2025-Comprehensive` |
| `Project-Agora` | `Ledger-Insights-BIS-Project-Agora-Real-Money-Trials` |
| `DLT-Pilot-Regime` | `esma-dlt-pilot-regime-review-2025` |
| `HK-Stablecoins-Ordinance` | `hkma-stablecoin-ordinance-implementation-2025` |
| `Bedrock-AgentCore` | `AWS-Bedrock-AgentCore-Payments` |
| `x402` | `arXiv-2607-12575-How-Agentic-Is-Agentic-Commerce-x402` |
| `RWA-Stablecoins` | `RWA-Stablecoin` (plural collapsed into singular) |

### Tier 2: build `30_Concepts/` (60 stubs)

Each stub carries schema §2.4 frontmatter, a definition placeholder, and
auto-discovered source backlinks. 158 backlinks total, 2.6 per stub. Domain
assigned from the referencing MOC.

Stubs are not empty shells. Each one lands with the corpus evidence already
attached, so filling the definition is a reading task, not a search task.

### Tier 3: de-link folder paths (6 targets)

Obsidian cannot wikilink a folder. These now render as inline code:
`10_Sources/Academia/`, `20_People`, and the four `40_Domains/Finance/*` paths
that point into a tree that was never built.

## Result

| Measure | Before | After |
|---|---|---|
| Broken wikilinks in MOCs | 75 | 0 |
| Orphan source notes | 13 | 0 of 223 |
| Concept notes | 0 | 60 |
| Distinct topic values | 14 | 14 |

## Open item: 28 concepts with no corpus support

Twenty-eight of the 60 stubs matched no source in the corpus, by body text or
by filename. The MOCs promise coverage the vault does not hold. Each stub says
so in its Sources section.

Three readings, and each needs a decision:

1. **Source the gap.** The concept matters and the corpus should cover it.
   `Account-Abstraction`, `MPC`, `MEV`, `Prompt-Injection`, and
   `Transaction-Intent-Schema` all sit in the agentic-AI security path and
   carry real analytical weight.
2. **Cut the MOC reference.** The concept was aspirational.
   `Georgia-Bitfury`, `Ghana-Honduras-pilots`, `Sweden-Lantmateriet`, and
   `HSBC-Marketnode-pilot` are named pilots with no source behind them.
3. **Rename.** The concept exists in the corpus under other words.
   `Land-Registry` and `DvP-on-Chain` are likely cases.

Full list: ACX, Account-Abstraction, Additionality, Agent-Authority,
Avalanche-Subnets, Buffer-Pool, Climate-Impact-X, Corresponding-Adjustment,
Direct-vs-Indirect-Tokenisation, DvP-on-Chain, Georgia-Bitfury,
Ghana-Honduras-pilots, HSBC-Marketnode-pilot, Land-Registry, MEV, MPC,
Permissioned-vs-Permissionless, Prompt-Injection,
Property-Digital-Assets-Act-2025-UK, Propy, Real-Estate-Tokenisation-Model,
SPV-Token-Wrapper, Singapore-PSA, Sweden-Lantmateriet,
Transaction-Intent-Schema, UNIDROIT-Principles-2023, Verra-2022-Suspension,
Zombie-Credit.

## Schema updated

`schema.md` §1 gained a row for `30_Areas/`, which existed undocumented, and a
new §1.1 recording that `00_Inbox/`, `70_Research/`, and the `40_Domains/`
note layer are designed but unbuilt.
