---
type: source
title: The Evolution of Financial Market Infrastructures in a Tokenized Economy
authors:
- Yaiza Cabedo
- Tommaso Mancini-Griffoli
- Fabian Schär
- Nicolas Zhang
organisation: International Monetary Fund
source_type: paper
venue: IMF Working Papers
year: 2026
date_published: '2026-07-01'
url: https://www.imf.org/en/publications/wp/issues/2026/07/01/financial-market-infrastructures-evolution-in-a-tokenized-economy-577325
doi: 10.5089/9798229051354.001
jurisdiction:
- INTL
domain:
- market-infrastructure
- settlement
- blockchain-settlement
- finance
doctrine:
- custody
- transfer
- intermediation
instrument:
- security-token
register_section: ''
nlm_id: ''
nlm_skip: false
status: draft
created: 2026-07-12
tags:
- tokenization
- market-infrastructure
- csd
- ccp
- smart-contracts
- imf
- working-paper
watchlist_channel: imf-fintech-notes
topic:
- topic/finance/market-infrastructure
- topic/blockchain-settlement
subject:
- subject/imf
wiki_indexed: '2026-07-12T00:00:00Z'
wiki_hash: 99376a83d252ad41e97b256a42ea4a6d123d4166e0019482325863a9b053cfe4
wiki_role: wiki
---



# The Evolution of Financial Market Infrastructures in a Tokenized Economy

## Citation

Cabedo, Yaiza, Tommaso Mancini-Griffoli, Fabian Schär, and Nicolas Zhang. "The Evolution of Financial Market Infrastructures in a Tokenized Economy." IMF Working Paper WP/26/136, International Monetary Fund, Monetary and Capital Markets Department, 2026-07-01. https://www.imf.org/en/publications/wp/issues/2026/07/01/financial-market-infrastructures-evolution-in-a-tokenized-economy-577325.

## One-line summary

This IMF working paper maps which central securities depository, central counterparty, and trade repository functions can migrate to smart contracts, concluding that tokenisation produces hybrid financial market infrastructures rather than full disintermediation.

## Key claims

- Smart contracts and distributed ledgers can perform a substantial share of central securities depository, central counterparty, and trade repository functions where processes are deterministic, rules-based, and data-driven.
- Record-keeping, settlement, collateral transfers, and reporting can migrate on-chain, but legal certainty, governance, accountability, and discretion under stress remain institutional functions.
- The paper analyses three interoperability architectures, single ledger, compatible ledger, and common ledger, and maps CSD, CCP, and trade repository functions across each.
- Blockchain consensus offers stronger immutability against record alteration than conventional IT databases, but a centralised or small validator set reintroduces a single point of failure.
- Compatible-ledger models require a legal entity or orchestrator to coordinate cross-ledger settlement, since hashed timelock contracts and bridges cannot alone guarantee accountability.
- Tokenisation reshapes the risk landscape by introducing smart contract vulnerabilities, governance concentration, oracle dependence, and cross-platform fragmentation alongside the frictions it removes.
- The most plausible outcome is a hybrid FMI model in which smart contracts absorb operational and transactional functions while legal entities retain governance, compliance, and crisis-intervention responsibilities.

## Excerpts

> "Tokenization does not imply disintermediation, but institutional redesign."
> ~ p. 3, Introduction

> "Yet code cannot by itself provide legal certainty, bear accountability, or exercise discretion under stress."
> ~ p. 3, Introduction

> "Blockchain technology can offer greater robustness against the alteration or deletion of settled transactions than existing securities settlement systems."
> ~ p. 30

> "The most plausible outcome is therefore the emergence of hybrid FMIs... The future of FMIs is thus not one of full disintermediation, but of institutional redesign."
> ~ p. 32, Conclusion

## Significance

- Supplies the wiki's most granular primary-source mapping of CSD, CCP, and trade-repository functions to smart-contract equivalents, load-bearing for the market-infrastructure domain.
- Shares and extends the single, compatible, and common ledger taxonomy used in NOTE/2026/006, letting the wiki cross-reference both sources at the architecture level.
- Names the specific institutional functions, legal certainty, governance, discretion under stress, that resist full codification, directly informing the wiki's custody and intermediation doctrine nodes.
- Frames tokenisation-specific risks, smart-contract vulnerability, governance concentration, and oracle dependence, extending the wiki's risk taxonomy beyond stablecoin run risk into market infrastructure.

## Related

- [[10_Sources/International-Agencies/IMF-Note-2026-006-Rise-of-Tokenization]] - companion Note applying the same ledger-architecture taxonomy to the asset layer
- [[10_Sources/International-Agencies/IMF-Tokenized-Finance-2026-04]] - the April 2026 Note this paper's FMI analysis extends
- [[10_Sources/International-Agencies/IMF-WP-2026-074-Making-Stablecoins-Stable]] - companion IMF paper on stablecoin-specific run risk
