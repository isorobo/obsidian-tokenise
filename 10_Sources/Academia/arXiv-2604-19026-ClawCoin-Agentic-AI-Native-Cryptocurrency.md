---
type: source
title: 'ClawCoin: An Agentic AI-Native Cryptocurrency for Decentralized Agent Economies'
authors:
- Shaoyu Li
- Chaoyu Zhang
- Hexuan Yu
- Y. Thomas Hou
- Wenjing Lou
organisation: arXiv
source_type: paper
venue: arXiv (cs.MA; cs.CR)
year: 2026
date_published: '2026-04-21'
url: https://arxiv.org/abs/2604.19026
doi: '10.48550/arXiv.2604.19026'
jurisdiction:
- INTL
domain:
- agentic-ai
- blockchain-settlement
- stablecoins
doctrine: []
instrument: []
register_section: ''
status: draft
created: 2026-10-25
tags:
- source
- agent-economy
- compute-cost-index
- x402
- tokenised-unit-of-account
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/agentic-ai
- topic/blockchain-settlement
wiki_indexed: '2026-10-24T17:18:03Z'
wiki_hash: 80fdf99c566b32847037f4f614014c672beb3bea00600d541bd142071c21f42e
wiki_role: wiki
---

# ClawCoin: An Agentic AI-Native Cryptocurrency for Decentralized Agent Economies

## Citation

Li, Shaoyu; Zhang, Chaoyu; Yu, Hexuan; Hou, Y. Thomas; Lou, Wenjing. "ClawCoin: An Agentic AI-Native Cryptocurrency for Decentralized Agent Economies". arXiv, 21 April 2026. https://arxiv.org/abs/2604.19026.

## One-line summary

ClawCoin proposes a tokenised unit of account and settlement asset indexed to AI compute cost, so autonomous agents can price and settle multi-hop work without fiat-denominated volatility.

## Key claims

- The authors argue that agent compute cost is not captured on on-chain ledgers, and that payment rails such as x402 move fiat-backed value without tracking compute consumed.
- ClawCoin has four layers: a basket index, a signed-attestation oracle, a NAV-based mint and redeem vault, and on-chain settlement for multi-hop delegations.
- A prototype on an Ethereum-compatible L2 was tested with a multi-agent simulator and the OpenClaw testbed.
- In single-agent simulations the coefficient of variation of execution capacity was 0.018 against 0.124 for fiat, with maximum drawdown of 1.9% against 24.7%.
- Multi-hop workflows had a 2.1% failure rate against 9.8% for fiat, with zero partial settlements.
- In a 500-round, eight-agent economy, six agents survived under ClawCoin and four under fiat; results come from the authors' own simulator and are not independent validation.

## Excerpts

> "Autonomous AI agents live or die by the API tokens they consume"
> ~ Abstract

> "Stablecoins solve transport. They do not solve representation"
> ~ Introduction

> "We tokenize the compute-cost surface itself by publishing an on-chain, transparent index"
> ~ Introduction

## Significance

- Extends the stablecoin-for-agents debate by proposing a non-fiat, index-linked settlement token rather than a fiat-backed stablecoin.
- Raises questions about reserve, redemption and oracle governance that mirror issues in tokenised-fund and stablecoin regulation.
- Backfill catch: submitted April 2026, before the previous run date, and found through search this run.

## Related

- [[10_Sources/Academia/arXiv-2604-03733-SoK-Blockchain-Agent-to-Agent-Payments]] - survey of blockchain agent-to-agent payments.
- [[10_Sources/Academia/arXiv-2608-01341-402Pilot-x402-Agent-Micropayments]] - x402 agent micropayments.
- [[10_Sources/Academia/arXiv-2605-00071-Compliance-Aware-Agentic-Payments-Stablecoin-Rails]] - agentic payments on stablecoin rails.
