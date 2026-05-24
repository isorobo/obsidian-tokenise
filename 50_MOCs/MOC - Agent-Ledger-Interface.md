---
title: MOC - Agent-Ledger-Interface
type: moc
moc_kind: cross-cutting
tags: [moc, cross-cutting, agentic-ai]
created: 2026-05-24
---

# MOC - Agent-Ledger Interface

> **Cross-cutting MOC.** The engineering bridge between the wiki's finance/law core and the agentic-AI rim.

The core tension: **stochastic, adaptive AI reasoning** meets **deterministic, immutable ledger state**. The architectural question is where to put the policy layer that translates an LLM agent's *intent* into a verifiable on-chain *action* without losing either auditability or expressivity.

## Anchor texts

- [[arXiv-2601-04583-Autonomous-Agents-Blockchains]] - the **five-part taxonomy** of agent capability (passive read-only, co-pilot, autonomous executor, multi-agent co-ordinator, sovereign on-chain entity); the **Transaction Intent Schema**; the security-first architecture (account abstraction, MPC, programmable policy engines).
- [[arXiv-Agent-Economy-Blockchain-Foundation]] - the macroeconomic counterpart: blockchain settlement as the trust substrate for inter-agent commerce.
- [[Emergent-Mind-Agent-Blockchain-Interoperability]] - survey of the design space.

## Cumulative authority risks

| Stage | Risk |
|---|---|
| Passive analytics | None novel |
| Co-pilot | Prompt injection biasing recommendations |
| Autonomous executor | Key exfiltration; over-scope of policy |
| Multi-agent | Coordinated MEV; reflexive feedback loops |
| Sovereign on-chain | Full economic agency; alignment failure has market impact |

## Concepts to develop

- [[Transaction-Intent-Schema]]
- [[Account-Abstraction]]
- [[MPC]]
- [[MEV]]
- [[Prompt-Injection]]
- [[Agent-Authority]]

## See also

- [[MOC - Agentic-AI]]
- [[MOC - Blockchain-Settlement]]
- [[MOC - Stablecoins]]
- [[MOC - Root]]
