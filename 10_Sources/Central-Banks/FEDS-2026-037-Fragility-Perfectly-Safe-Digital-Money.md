---
type: source
title: The Fragility of Perfectly Safe Digital Money
authors:
- Elizabeth C. Klee
- Arazi Lubis
- Chase P. Ross
- Sharon Y. Ross
- Alexandros P. Vardoulakis
organisation: Federal Reserve Board
source_type: paper
venue: Finance and Economics Discussion Series
year: 2026
date_published: '2026-06-02'
url: https://www.federalreserve.gov/econres/feds/the-fragility-of-perfectly-safe-digital-money.htm
doi: https://doi.org/10.17016/FEDS.2026.037
jurisdiction:
- US
domain:
- stablecoins
- blockchain-settlement
- market-structure
- finance
doctrine: []
instrument:
- stablecoin-fiat
register_section: ''
nlm_id: ''
nlm_skip: false
status: draft
created: 2026-06-28
tags:
- stablecoins
- digital-money
- financial-stability
- runs
- network-effects
- congestion
watchlist_channel: fed-staff-papers
topic:
- topic/finance/stablecoins
- topic/blockchain-settlement
subject:
- subject/federal-reserve
wiki_indexed: '2026-06-28T00:00:00Z'
wiki_hash: ab5aaf11eb69106c673123ffdc964ba141051e5590304f15c32bfc5acdabc64a
wiki_role: wiki
---


# The Fragility of Perfectly Safe Digital Money

## Citation

Klee, Elizabeth C., Arazi Lubis, Chase P. Ross, Sharon Y. Ross, and Alexandros P. Vardoulakis. "The Fragility of Perfectly Safe Digital Money". Finance and Economics Discussion Series 2026-037, Federal Reserve Board, 2 June 2026. https://doi.org/10.17016/FEDS.2026.037.

## One-line summary

Digital money backed by perfectly safe reserves can still suffer runs because network effects and congestion-based gas fees create strategic complementarities in redemption decisions.

## Key claims

- Digital money unbundles trust from institutions and prices it separately through congestion-sensitive gas fees, introducing a novel fragility absent in traditional payment systems.
- Network externalities make a stablecoin more valuable as adoption rises, but higher adoption drives blockchain congestion, which raises the cost of use.
- These two opposing forces generate strategic complementarities: each redemption erodes the network value for remaining holders, prompting further redemptions.
- Runs on digital money can occur even when reserve assets are perfectly safe and liquid, driven entirely by the interaction of network effects and congestion costs.
- Stablecoins with low network externalities experience disproportionately higher redemptions when congestion rises; the effect is concentrated in the high-congestion regime.
- The authors formalise the mechanism in a global games model and test it empirically using Ethereum-based stablecoins, finding a threshold pattern consistent with strategic complementarities.

## Excerpts

> "Digital money differs from previous forms of money in an important way: it unbundles trust. Instead of relying on a trustworthy institution to settle payments, it relies on decentralized verification, whose cost is priced separately through congestion-sensitive gas fees."
> ~ Abstract

> "We show that the unbundling of trust introduces a novel fragility — one that remains even when reserves are safe and liquid."
> ~ Section 1, Introduction

> "High congestion and low network externalities combine to produce strategic complementarities in redemption decisions: whether an individual user should redeem depends on whether other users also redeem."
> ~ Section 1, Introduction

> "Stablecoins with low network externalities experience disproportionately higher redemptions when congestion rises. This pattern is consistent with strategic complementarities."
> ~ Section 1, Introduction (p. 3)

## Significance

- Establishes a theoretical basis for stablecoin runs that is independent of reserve quality, directly challenging the assumption that full backing eliminates run risk.
- Provides empirical evidence from Ethereum stablecoins that informs regulatory design under the GENIUS Act and equivalent regimes.
- The global games framework is the first to model congestion fees as a structural fragility vector in digital payment systems.
- Connects the stablecoin stability debate to blockchain infrastructure design, making it load-bearing for the wiki's blockchain-settlement and stablecoins domains.

## Related

- [[10_Sources/Central-Banks/Fed-Tokenization-Financial-Stability]] - Fed overview of tokenisation stability implications
- [[10_Sources/Central-Banks/FEDS-Note-2026-04-Stablecoins-in-2025-Financial-Stability]] - companion note on 2025 stablecoin market developments
