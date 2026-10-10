---
type: source
title: Compliance-Aware Agentic Payments on Stablecoin Rails
authors:
- Kenneth See
- Xue Wen Tan
organisation: arXiv
source_type: paper
venue: arXiv (cs.CR)
year: 2026
date_published: '2026-04-30'
url: https://arxiv.org/abs/2605.00071
doi: '10.48550/arXiv.2605.00071'
jurisdiction:
- INTL
domain:
- stablecoins
- agentic-ai
- cross-border-payments
doctrine:
- aml-cft
instrument:
- stablecoin-fiat
register_section: ''
status: draft
created: 2026-10-11
tags:
- source
- agentic-payments
- stablecoin-rails
- on-chain-compliance
- x402
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/finance/stablecoins
- topic/agentic-ai
wiki_indexed: '2026-10-10T17:43:28Z'
wiki_hash: cfa069ef745040e3e85863b6d1c933e1c369fe615b229a1511b14821debe58a9
wiki_role: wiki
---

# Compliance-Aware Agentic Payments on Stablecoin Rails

## Citation

See, Kenneth; Tan, Xue Wen. "Compliance-Aware Agentic Payments on Stablecoin Rails". arXiv (cs.CR), 30 April 2026. https://arxiv.org/abs/2605.00071.

## One-line summary

A demo-track architecture enforces compliance checks on-chain so that agent-initiated stablecoin payments are verified at the moment of execution.

## Key claims

- Agentic payment systems extend delegated action to financial transfers and must operate in regulated settings without constant human oversight.
- The architecture combines x402-style signature-based payment authorisation with relayed transaction execution.
- A policy wrapper and a policy manager coordinate modular compliance checks at execution time rather than in a separate off-chain process.
- The design records transaction-linked on-chain attestations.
- It supports structured resolution when requirements are still pending.
- The paper is listed as a Demo Paper Track submission.

## Excerpts

> "Agentic payment systems extend delegated action to financial transfers,"
> ~ Abstract

> "We present a compliance-aware architecture that combines x402-style, signature-based payment authorisation"
> ~ Abstract

> "records transaction-linked on-chain attestations, and supports structured resolution when requirements are pending."
> ~ Abstract

## Significance

- Shows how compliance (for example AML/CFT-type checks) can be embedded in stablecoin payment execution for agents.
- Extends the vault's x402 and agent-payment sources with a compliance-first design.
- Read from the arXiv abstract page and API record only; the full text was not reviewed.

## Related

- [[10_Sources/Academia/arXiv-2608-01341-402Pilot-x402-Agent-Micropayments]] - x402 decision layer for agent micropayments.
- [[10_Sources/Academia/arXiv-2607-12575-How-Agentic-Is-Agentic-Commerce-x402]] - measurement of x402 adoption.
- [[10_Sources/Academia/arXiv-2604-03733-SoK-Blockchain-Agent-to-Agent-Payments]] - SoK on agent-to-agent blockchain payments.
