---
type: source
title: 'Scaling laws of Stablecoin Transactions: Evidence from USDT and USDC on the
  Ethereum blockchain'
authors:
- Kundan Mukhia
- Sabat Rai
- Vivek Shrivastav
- Imran Ansari
- Md. Nurujjaman
organisation: ''
source_type: paper
venue: arXiv (q-fin.ST)
year: 2026
date_published: '2026-08-10'
url: https://arxiv.org/abs/2608.09378
doi: 10.48550/arXiv.2608.09378
jurisdiction:
- INTL
domain:
- stablecoins
- market-structure
- blockchain-settlement
doctrine: []
instrument:
- stablecoin-fiat
register_section: ''
nlm_id: ''
nlm_skip: false
status: draft
created: 2026-08-17
tags:
- source
- stablecoins
- ethereum
- power-law
- transaction-scaling
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/finance/stablecoins
- topic/blockchain-settlement
wiki_indexed: '2026-08-17T00:00:00Z'
wiki_hash: de1bfb23e0c0269949ea979b25c924b227b28b1ff48e09a9cd1c3b9d95f99eef
wiki_role: wiki
---


# Scaling laws of Stablecoin Transactions: Evidence from USDT and USDC on the Ethereum blockchain

## Citation

Mukhia, Kundan, Sabat Rai, Vivek Shrivastav, Imran Ansari, and Md. Nurujjaman. "Scaling laws of Stablecoin Transactions: Evidence from USDT and USDC on the Ethereum blockchain". arXiv:2608.09378 (q-fin.ST), 10 August 2026. https://arxiv.org/abs/2608.09378.

## One-line summary

The paper finds two distinct power-law scaling regimes in USDT and USDC transaction values on Ethereum, separating account-driven transfers from smart-contract-driven transfers.

## Key claims

- The paper analyses approximately 370 million USDT and USDC transactions on Ethereum across six periods from June 2024 to February 2026.
- It classifies transactions into four categories by counterparty type: EOA-EOA, EOA-SC, SC-EOA, and SC-SC.
- Transaction value distributions show heavy-tailed power-law scaling for both stablecoins across every period and category.
- Externally Owned Account-involved categories cluster around a power-law exponent of 1.45 to 1.60, while smart-contract-to-smart-contract transactions show a higher exponent of approximately 1.72 to 1.73.
- Sensitivity analysis confirms the separation between the two regimes holds across periods, stablecoins, and sample sizes.
- Counterfactual analysis shows that shifts in category weights alone explain only 10% to 35% of the observed temporal variation in the overall exponent.
- The authors state this is the first study of scaling behaviour in stablecoin transaction data.

## Excerpts

> "To the best of our knowledge, this is the first study to investigate scaling behavior in stablecoin transaction data, focusing on USDT and USDC."
> ~ Abstract

> "We identify two distinct scaling regimes: EOA-involved categories cluster around 1.45-1.60, whereas SC-SC transactions exhibit higher exponents of approximately 1.72-1.73."
> ~ Abstract

> "Across different sample sizes, the counterfactual path accounts for only about 10%-35% of the total temporal range observed in the actual data."
> ~ Abstract

> "Power-law tail behavior is observed throughout stablecoin transaction activity, but the exponent depends on whether transactions are driven by EOAs or SCs."
> ~ Abstract

## Significance

- Supplies the corpus's first large-sample statistical study of on-chain stablecoin transaction behaviour, distinct from the existing stress-event and adoption-focused stablecoin sources.
- Shows that smart-contract-mediated stablecoin flows, the channel most relevant to DeFi and agentic-payment rails, behave statistically differently from wallet-to-wallet transfers, a load-bearing distinction for any settlement-risk analysis.
- Covers a 20-month window running through February 2026, giving the wiki a recent empirical baseline for USDT and USDC transaction-value distributions ahead of any GENIUS Act reserve-disclosure comparison.
- Complements the Austrian CASP transaction-level stablecoin study already indexed by adding an on-chain, protocol-level lens rather than a national-market lens.

## Related

- [[10_Sources/Academia/arXiv-2607-08524-Stablecoins-Under-Stress-Austrian-CASPs]] - companion transaction-level stablecoin study using national CASP data rather than on-chain Ethereum data
- [[10_Sources/Academia/arXiv-2608-01341-402Pilot-x402-Agent-Micropayments]] - agentic-payment paper whose stablecoin settlement rail this study's SC-SC transaction category would capture
