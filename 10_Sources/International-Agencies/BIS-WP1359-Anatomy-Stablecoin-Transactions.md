---
type: source
title: The anatomy of stablecoin transactions
authors:
- Anneke Kosse
- Tara Rice
- Fabian Schär
- Takeshi Shirakami
- Jirapat Siridhasanakul
organisation: Bank for International Settlements
source_type: paper
venue: BIS Working Papers
year: 2026
date_published: '2026-06-11'
url: https://www.bis.org/publ/work1359.htm
doi: ''
jurisdiction:
- INTL
domain:
- stablecoins
- blockchain-settlement
- market-structure
- market-infrastructure
doctrine: []
instrument:
- stablecoin-fiat
register_section: ''
nlm_id: 11e1a667-1100-48c5-a0a0-f00d46562071
nlm_skip: false
status: draft
created: 2026-06-14
tags:
- stablecoins
- blockchain
- transaction-complexity
- ethereum
- market-monitoring
watchlist_channel: bis-working-papers
topic:
- topic/finance/stablecoins
- topic/blockchain-settlement
- topic/finance/market-infrastructure
subject:
- subject/bis
- subject/ethereum
wiki_indexed: '2026-06-13T18:11:00Z'
wiki_hash: 7c1980e06fed104fff214a13e3f4ec24e9242b17a7c91ce8f32988600619328b
wiki_role: wiki
---


# The anatomy of stablecoin transactions

## Citation
Kosse, Anneke, Tara Rice, Fabian Schär, Takeshi Shirakami, and Jirapat Siridhasanakul. "The anatomy of stablecoin transactions". BIS Working Papers, No 1359, 11 June 2026. https://www.bis.org/publ/work1359.htm.

## One-line summary
Analysing 593 million Ethereum event logs, this paper shows that nearly 60% of stablecoin transfers are embedded in complex multi-operation transaction bundles rather than simple payments, with material implications for market monitoring and policy.

## Key claims
- Stablecoin transfers on programmable blockchains are frequently embedded in atomically executed transaction bundles that combine trading, lending, arbitrage, liquidity provision, and settlement.
- Ignoring this transaction structure materially distorts the interpretation of stablecoin activity and overstates both transfer counts and transferred volumes.
- Complexity is a first-order feature: nearly 60% of stablecoin transfer events occur within complex transactions.
- USDT, USDC, and PYUSD are not interchangeable; each exhibits distinct patterns in transaction complexity, urgency, timing, and integration with financial protocols.
- The analytical framework draws on archive node data, public contract labels, and event signatures to produce replicable complexity metrics.
- Treating stablecoin transfers as standalone payments risks misclassifying a large share of on-chain activity, with consequences for empirical measurement, market monitoring, and regulatory design.

## Excerpts
> "Stablecoin transfers are often interpreted as payments. On programmable blockchains, however, they are frequently embedded in atomically executed transaction bundles that combine trading, lending, arbitrage, liquidity provision, and settlement."
> ~ Abstract

> "We show that ignoring this structure materially distorts the interpretation of stablecoin activity."
> ~ Abstract

> "Nearly 60 percent of transfer events occur within complex transactions."
> ~ Abstract

> "The three stablecoins are not used interchangeably: their use differs systematically across transaction structures, urgency, and timing, consistent with distinct institutional designs and economic functions."
> ~ Abstract

> "Analyses that treat transfers as standalone payments therefore risk misclassifying a large share of on-chain stablecoin use, with implications for empirical measurement, market monitoring, and policy."
> ~ Abstract

## Significance
- The paper establishes that stablecoin activity metrics used by regulators and researchers systematically overstate payment volumes; this finding challenges the empirical basis of current policy frameworks for stablecoins.
- The distinction between USDT, USDC, and PYUSD by transaction structure and urgency supports the wiki's instrument-level analysis of stablecoin-fiat instruments and their divergent regulatory treatment.
- The complexity framework — atomically bundled operations spanning DeFi protocols — connects the stablecoin and blockchain-settlement domains and provides a methodology for market-infrastructure analysis.
- Published by BIS economists and drawing on 141 million Ethereum transactions, this paper anchors the corpus on empirical transaction-level evidence rather than modelling assumptions.

## Related
- [[10_Sources/International-Agencies/BIS-WP1270-Stablecoins-Safe-Asset-Prices]] - stablecoin demand and safe asset pricing
- [[10_Sources/International-Agencies/BIS-WP1355-Making-Stablecoins-Stable-Regulation]] - stablecoin capital and liquidity regulation
- [[10_Sources/International-Agencies/BIS-WP1340-Stablecoin-Flows-FX-Markets]] - stablecoin flows and FX spillovers
