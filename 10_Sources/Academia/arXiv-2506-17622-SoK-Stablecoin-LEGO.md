---
type: source
title: 'SoK: Stablecoin Designs, Risks, and the Stablecoin LEGO'
authors:
- Shengchen Ling
- Yuefeng Du
- Yajin Zhou
- Lei Wu
- Cong Wang
- Xiaohua Jia
- Houmin Yan
organisation: ''
source_type: paper
venue: arXiv (cs.CR)
year: 2025
date_published: '2025-06-21'
url: https://arxiv.org/abs/2506.17622
doi: ''
jurisdiction:
- INTL
domain:
- finance
- stablecoins
- defi
- market-infrastructure
doctrine:
- reserve-requirements
- singleness-of-money
instrument:
- stablecoin-fiat
- stablecoin-rwa-backed
- stablecoin-algorithmic
register_section: ''
nlm_id: ''
nlm_skip: false
status: draft
created: 2026-06-28
tags:
- source
- stablecoin
- sok
- risk
- lego
- systematisation
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/finance/stablecoins
- topic/blockchain-settlement
wiki_indexed: '2026-06-28T00:00:00Z'
wiki_hash: 242b431981e792f8c9ad89e1b028e06e4a563d5b268e51a0b052d6856c7f6c73
wiki_role: wiki
---


# SoK: Stablecoin Designs, Risks, and the Stablecoin LEGO

## Citation

Ling, Shengchen, Yuefeng Du, Yajin Zhou, Lei Wu, Cong Wang, Xiaohua Jia, and Houmin Yan. "SoK: Stablecoin Designs, Risks, and the Stablecoin LEGO". arXiv:2506.17622 (cs.CR), 21 June 2025. https://arxiv.org/abs/2506.17622.

## One-line summary

Synthesising 157 studies, 95 active stablecoins, and 44 security incidents, the paper finds that stablecoin stability is an emergent, fragile property rather than a guaranteed design feature, and introduces the Stablecoin LEGO framework to map historical failures to preventive controls in current implementations.

## Key claims

- Stability is an emergent, fragile state dependent on sustained market confidence and continuous liquidity, not an inherent property of any stablecoin mechanism.
- Stablecoin design choices create risk specialisation rather than risk elimination; fiat-backed and crypto-backed stablecoins each concentrate risks that the other type mitigates.
- Yield mechanisms present in 56.84% of stablecoins create systemic tension between the stability mandate and high-risk financial engineering (derivatives, external DeFi integrations).
- The stablecoin market is highly concentrated: the top five (USDT, USDC, USDS, USDe, DAI) control over 93% of total market capitalisation.
- Security incidents (44 major events) act as evolutionary pressures that redefine security standards; 38.64% stem from code vulnerabilities, 27.27% from market volatility.
- The Stablecoin LEGO framework deconstructs past failures and maps them to identifiable preventive and detective controls in current designs.

## Excerpts

> "Stability is best understood not an inherent property but an emergent, fragile state reliant on the interplay between market confidence and continuous liquidity."
> ~ Abstract

> "Design choices result in risk specialization rather than complete risk elimination...stablecoins typically manage certain key risks effectively...while implicitly concentrating others."
> ~ §III, Insight 2

> "The integration of yield mechanisms transforms stablecoins from simple payment tools into complex financial instruments...creating new vectors for contagion and systemic risk."
> ~ §III-D, Insight 3

> "The stablecoin market is highly concentrated: the top 5 (USDT, USDC, USDS, USDe, DAI) constitute over 93% of total market capitalization, and the top 20 represent 98%."
> ~ §III-A, Observation 1

> "Major security incidents act as acute 'evolutionary pressures', forging resilience by stress-testing designs and aggressively redefining the security frontier."
> ~ Abstract

## Significance

- Provides the most comprehensive systematisation of stablecoin architectures and failure modes to date, giving the wiki an authoritative evidence base for the stablecoins domain.
- Demonstrates that yield-bearing stablecoins carry systemic risk vectors absent from pure payment instruments, which has direct relevance to regulatory debates under MiCA, GENIUS Act, and other frameworks covered by the wiki.
- The Stablecoin LEGO framework operationalises the lessons from 44 incidents into actionable design controls, relevant to the wiki's coverage of reserve-requirements and singleness-of-money doctrine.
- Market concentration data (top 5 = 93% of capitalisation) grounds the wiki's systemic-risk analysis of stablecoin infrastructure.

## Related

- [[10_Sources/Academia/sok-stablecoins-retail-payments-2026]] - SoK on stablecoins in retail payment systems
- [[10_Sources/Academia/stablecoins-hybrid-monetary-ecosystems-2025]] - hybrid monetary ecosystem proposals involving stablecoins
- [[10_Sources/Academia/stablecoin-discount-tether-tbills-2025]] - empirical evidence on Tether's Treasury-bill market share
