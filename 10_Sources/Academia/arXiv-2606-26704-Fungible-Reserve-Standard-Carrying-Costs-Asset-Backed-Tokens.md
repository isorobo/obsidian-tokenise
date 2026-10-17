---
type: source
title: 'The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in Asset-Backed Tokens'
authors:
- JJ Jia Jing Tan
- Eva Meng
- Josh Ng
- Zack Zhang
- September Liu
- Teelet Wang
- Ludwig Zhang
- Seth Yan
organisation: arXiv
source_type: paper
venue: arXiv (cs.CR; cs.CE; cs.CY)
year: 2026
date_published: '2026-06-25'
url: https://arxiv.org/abs/2606.26704
doi: '10.48550/arXiv.2606.26704'
jurisdiction:
- INTL
domain:
- finance
- defi
doctrine: []
instrument:
- tokenised-commodity
register_section: ''
status: draft
created: 2026-10-18
tags:
- source
- asset-backed-tokens
- carrying-costs
- erc-20
- commodities
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/blockchain-settlement
- topic/tokenisation
wiki_indexed: '2026-10-17T17:28:39Z'
wiki_hash: 005116e5aaeefb15e03e7bf0d2ecafd70d2c59f486ee881aea71cc415dfaac18
wiki_role: wiki
---

# The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in Asset-Backed Tokens

## Citation

JJ Jia Jing Tan, Eva Meng, Josh Ng, Zack Zhang, September Liu, Teelet Wang, Ludwig Zhang and Seth Yan. "The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in Asset-Backed Tokens". arXiv, 25 June 2026. https://arxiv.org/abs/2606.26704.

## One-line summary

The Fungible Reserve Standard encodes custody, insurance and audit costs of physical-asset-backed tokens through a decaying per-token backing variable instead of rebasing.

## Key claims

- The paper proposes the Fungible Reserve Standard (FRS) for tokens backed by real-world assets such as precious metals, stored commodities and warehoused goods.
- Such assets carry ongoing custody, insurance and audit costs that a token design must account for.
- Rebasing can undermine fungibility and DeFi composability.
- FRS instead reduces a per-token variable at a predefined annualised carrying-cost rate.
- A supply reconciliation mechanism preserves holder balances and ERC-20 compatibility.
- The authors describe the framework as asset-agnostic for any asset with positive, predictable holding costs.

## Excerpts

> "The framework is asset-agnostic and applicable to any real-world asset with positive, predictable holding costs."
> ~ Abstract

> "In traditional finance, negative carry is embedded transparently into product structures."
> ~ Section 1, Introduction

> "Deterministic: Carrying costs follow a predefined, algorithmically enforced schedule."
> ~ Section 9, Conclusion

## Significance

- Addresses a design gap for commodity tokens: who bears storage and insurance cost, and how that cost shows on-chain.
- Relevant to the legal question of what a holder is entitled to when backing decays by schedule rather than by a rebased balance.
- Complements the vault's RWA taxonomy and liquidity papers with a token-standard proposal.

## Related

- [[10_Sources/Academia/arXiv-2606-08534-Taxonomy-RWA-Tokenization]] - taxonomy of RWA tokenisation designs.
- [[10_Sources/Academia/arXiv-2609-15797-Prelude-Theory-RWA-Tokenization]] - economic models of RWA tokenisation.
