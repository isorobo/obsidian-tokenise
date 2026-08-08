---
type: source
title: '402Pilot: An x402 Decision Layer for Autonomous Agent Micropayments'
authors:
- Yin Li
- Yanbo He
- Boo-Ho Yang
- Rav Lawana
- Ziyue Li
- Wei Zeng
- Jing Tang
- Fugee Tsung
organisation: ''
source_type: paper
venue: arXiv (cs.AI)
year: 2026
date_published: '2026-08-02'
url: https://arxiv.org/abs/2608.01341
doi: 10.48550/arXiv.2608.01341
jurisdiction:
- INTL
domain:
- agentic-ai
- blockchain-settlement
- finance
doctrine: []
instrument:
- stablecoin-fiat
register_section: ''
nlm_id: ''
nlm_skip: false
status: draft
created: 2026-08-09
tags:
- source
- agentic-ai
- x402
- machine-to-machine-payments
- blockchain-settlement
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/agentic-ai
- topic/blockchain-settlement
wiki_indexed: '2026-08-09T00:00:00Z'
wiki_hash: ce6b183a57f840c339738e64e012441e1b3d32ddfb88a0225b2a93f64633b8ae
wiki_role: wiki
---



# 402Pilot: An x402 Decision Layer for Autonomous Agent Micropayments

## Citation

Li, Yin, Yanbo He, Boo-Ho Yang, Rav Lawana, Ziyue Li, Wei Zeng, Jing Tang, and Fugee Tsung. "402Pilot: An x402 Decision Layer for Autonomous Agent Micropayments". arXiv:2608.01341 (cs.AI), 2 August 2026. https://arxiv.org/abs/2608.01341.

## One-line summary

The paper proposes 402Pilot, a buyer-side decision layer that lets an autonomous agent choose among x402-payable service providers under a finite wallet.

## Key claims

- Programmable-payment protocols such as x402 enable per-request micropayments but do not determine which payable service an agent should buy under budget constraints.
- The paper formulates buyer-side provider selection as an agent-native payment decision problem, covering contextual provider selection, chosen-only paid feedback, and changing market conditions.
- 402Pilot is a protocol-agnostic decision layer sitting between autonomous agents and payment execution.
- PA-DCT, a payment-aware discounted contextual Thompson-sampling policy, adapts purchasing decisions under wallet pressure and learns from post-payment feedback.
- The authors introduce a frozen-replay benchmark, 402Pilot-Bench, spanning 823 tasks, five heterogeneous provider pipelines, and three market regimes.
- PA-DCT maintains competitive service quality while spending only 39 to 43% of the available wallet and reallocates spending as market conditions shift.

## Excerpts

> "Programmable-payment protocols such as x402 enable per-request micropayments, but they do not determine which payable service an autonomous agent should buy under a finite wallet."
> ~ Abstract

> "x402 embeds per-request payment into HTTP, and its V2 release adds discovery and service metadata for payable APIs."
> ~ Body

> "PA-DCT... maintains competitive service quality while using only 39-43% of the available wallet."
> ~ Abstract

> "A frozen-replay benchmark spanning 823 tasks, five heterogeneous provider pipelines, and three market regimes is introduced for evaluation."
> ~ Abstract

## Significance

- Extends the wiki's x402 evidence base beyond adoption measurement to buyer-side purchasing policy, showing how an agent decides where to spend rather than only whether a settlement occurred.
- Gives the corpus a concrete decision-layer design for agentic-commerce micropayments, relevant to any regulator or bank assessing operational controls on autonomous agent spending.
- Reinforces x402 as the reference protocol for agent-to-agent stablecoin micropayments, complementing the forensic adoption study already indexed.
- Introduces a reusable benchmark, 402Pilot-Bench, for future comparison of buyer-side agent payment policies.

## Related

- [[10_Sources/Academia/arXiv-2607-12575-How-Agentic-Is-Agentic-Commerce-x402]] - population-scale forensic audit of x402 settlement volume that this paper's decision layer would transact over
- [[10_Sources/Commercial-Banks/AWS-Bedrock-AgentCore-Payments]] - industry infrastructure enabling the x402 stablecoin rail this paper builds a buyer-side policy for
