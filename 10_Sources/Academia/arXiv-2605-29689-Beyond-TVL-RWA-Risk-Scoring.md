---
type: source
title: 'Beyond TVL: An Explainable Risk Scoring Framework for Tokenized Real-World
  Assets'
authors:
- Rischan Mafrur
- Khadijah
organisation: Western Sydney University; CryptoCoinHalal
source_type: paper
venue: arXiv (cs.CE; q-fin.CP)
year: 2026
date_published: '2026-05-28'
url: https://arxiv.org/abs/2605.29689
doi: ''
jurisdiction:
- INTL
domain:
- finance
- market-structure
- blockchain-settlement
- defi
doctrine: []
instrument:
- tokenised-bond
- tokenised-commodity
- tokenised-private-credit
- tokenised-treasury
register_section: ''
nlm_id: ''
nlm_skip: false
status: draft
created: 2026-06-28
tags:
- source
- rwa
- risk-scoring
- tokenisation
- tvl
- empirical
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/finance/market-infrastructure
- topic/blockchain-settlement
wiki_indexed: '2026-06-28T00:00:00Z'
wiki_hash: acf01b3fc9589769bde5529f15e5430103c10c5ce16ac0a20ce34890679586e4
wiki_role: wiki
---


# Beyond TVL: An Explainable Risk Scoring Framework for Tokenized Real-World Assets

## Citation

Mafrur, Rischan, and Khadijah. "Beyond TVL: An Explainable Risk Scoring Framework for Tokenized Real-World Assets". arXiv:2605.29689 (cs.CE; q-fin.CP), 28 May 2026. https://arxiv.org/abs/2605.29689.

## One-line summary

The paper presents the first empirical, data-driven framework for ranking RWA tokens by observable liquidity, concentration, and market-quality risk, finding that TVL conceals high risk in several tokens with large reported asset values.

## Key claims

- Total value locked is an unreliable proxy for risk in tokenised RWA markets because large asset bases can coexist with concentrated ownership, minimal transfer activity, and poor market quality.
- The framework evaluates three risk dimensions: liquidity risk (turnover and participation), concentration risk (holder breadth and Herfindahl indices), and market-quality risk (cross-chain distribution).
- Among ten pilot RWA tokens, private-credit products (STAC, HLSCOPE) rank highest risk; gold-backed tokens (PAXG) rank lowest.
- Tokenisation creates a layered claim: the token sits on a public ledger, but the asset, reserve, bankruptcy waterfall, and redemption processes remain partly or wholly off-chain.
- Observable on-chain activity metrics outperform headline valuation metrics for investor and regulatory risk assessment.

## Excerpts

> "a large tokenized fund may still be unsuitable for many investors if it has only a few dozen holders, a narrow dealing window"
> ~ Introduction

> "The key contribution is one of the first empirical, data-driven frameworks to rank tokenized RWAs by observable liquidity and activity metrics"
> ~ Introduction

> "tokenisation creates a layered claim. The token is on a public or semi-public ledger, but the asset, the reserve, the bankruptcy waterfall, and redemption processes remain partly or wholly off-chain"
> ~ Section 2.1

> "Higher composite means empirically higher risk (low liquidity, high concentration or poor market quality)"
> ~ Section 5.1

> "This pilot uses only public on-chain data. We do not capture off-chain trades or locked records"
> ~ Section 9 (Limitations)

## Significance

- Fills a gap in RWA market assessment by replacing headline TVL with observable, decomposable risk scores, giving the wiki a tool to evaluate tokenised instruments beyond issuer-reported data.
- Demonstrates empirically that private-credit tokens carry the highest composite risk, which is directly relevant to the wiki's coverage of tokenised private credit and its regulatory treatment.
- Highlights the off-chain/on-chain claim split as a structural feature of all current RWA systems, reinforcing the hybrid-architecture finding in arXiv:2606.08534.
- Provides a reproducible methodology (Herfindahl indices, turnover, active-address counts) that regulators and academics can apply to any on-chain token market.

## Related

- [[10_Sources/Academia/arXiv-2606-01131-Tokenized-Illiquid-RWA-Markets]] - companion paper by same lead author on liquidity evidence
- [[10_Sources/Academia/arXiv-2606-08534-Taxonomy-RWA-Tokenization]] - taxonomy of the protocols whose tokens are risk-scored here
- [[10_Sources/Academia/rwa-liquidity-challenges-2025]] - broader survey of RWA liquidity barriers
