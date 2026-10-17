---
type: source
title: When Token Transfers Do Not Mean Liquidity in Tokenized Real-World Assets
authors:
- Emre Atay Tümer
- Rischan Mafrur
organisation: arXiv
source_type: paper
venue: arXiv (cs.CE; q-fin.CP)
year: 2026
date_published: '2026-10-05'
url: https://arxiv.org/abs/2610.05873
doi: '10.48550/arXiv.2610.05873'
jurisdiction:
- INTL
domain:
- finance
- market-structure
doctrine: []
instrument:
- tokenised-fund
register_section: ''
status: draft
created: 2026-10-18
tags:
- source
- rwa
- liquidity
- on-chain-measurement
- tokenised-funds
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/finance/market-infrastructure
- topic/tokenisation
wiki_indexed: '2026-10-17T17:28:39Z'
wiki_hash: 7f26b18a8688a64add02469fa888c22d5ddba84d9e4329c4b77bf76860c6d7d2
wiki_role: wiki
---

# When Token Transfers Do Not Mean Liquidity in Tokenized Real-World Assets

## Citation

Emre Atay Tümer and Rischan Mafrur. "When Token Transfers Do Not Mean Liquidity in Tokenized Real-World Assets". arXiv, 5 October 2026. https://arxiv.org/abs/2610.05873.

## One-line summary

On-chain transfer volume and address concentration for tokenised funds mix minting, burning, issuer operations and intermediary flows, so they must be classified before being read as market liquidity.

## Key claims

- On-chain transfer volume in tokenised real-world assets mixes economically different events: minting, burning, issuer operations and transfers between addresses.
- Separating these event types and recalculating transfer turnover can change the measured result.
- A large address balance may belong to a pool or intermediary serving many investors, so concentration should be compared against total supply and against supply excluding identified intermediaries.
- The sample covers Ethereum-based tokenised funds from December 2025 to August 2026.
- Removing an intermediary can lower supply-based concentration while concentration among the remaining addresses rises.
- Turnover and concentration indicate liquidity-related activity but do not directly measure market liquidity.

## Excerpts

> "They provide evidence about liquidity-related activity, but they do not directly measure market liquidity."
> ~ Abstract

> "But a token moving is not the same as a token being traded."
> ~ Section 1, Introduction

> "This paper develops a framework for making these measurement choices explicit."
> ~ Section 7, Conclusion

## Significance

- Cautions against reading raw transfer counts for tokenised funds as secondary-market depth, which matters for any source in the vault that cites on-chain activity as evidence of liquidity.
- Extends the earlier Mafrur papers on RWA liquidity and risk scoring with a measurement-validity argument.
- Gives supervisors and researchers a method point: classify event types and exclude intermediaries before computing turnover or concentration.

## Related

- [[10_Sources/Academia/arXiv-2606-01131-Tokenized-Illiquid-RWA-Markets]] - earlier liquidity study by the same corresponding author.
- [[10_Sources/Academia/arXiv-2605-29689-Beyond-TVL-RWA-Risk-Scoring]] - risk scoring for tokenised RWAs using liquidity and concentration measures.
