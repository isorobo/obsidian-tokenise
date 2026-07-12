---
type: source
title: '"Harvest Now Decrypt Later": Examining Post-Quantum Cryptography and the Data
  Privacy Risks for Distributed Ledger Networks'
authors:
- Jillian Mascelli
- Megan Rodden
organisation: Federal Reserve Board
source_type: paper
venue: Finance and Economics Discussion Series (FEDS)
year: 2025
date_published: '2025-09-01'
url: https://www.federalreserve.gov/econres/feds/harvest-now-decrypt-later-examining-post-quantum-cryptography-and-the-data-privacy-risks-for-distributed-ledger-networks.htm
doi: https://doi.org/10.17016/FEDS.2025.093
jurisdiction:
- US
domain:
- blockchain-settlement
- market-infrastructure
- finance
doctrine: []
instrument:
- cbdc-wholesale
register_section: ''
nlm_id: acbbad6f-a1d6-4c94-bfec-9561ccea1af9
nlm_skip: false
status: draft
created: 2026-06-25
tags:
- distributed-ledger
- post-quantum-cryptography
- DLT
- blockchain
- data-privacy
watchlist_channel: fed-staff-papers
topic:
- topic/blockchain-settlement
- topic/finance/market-infrastructure
subject:
- subject/federal-reserve
wiki_indexed: '2026-06-28T00:00:00Z'
wiki_hash: 4f94999dffcc87a475624af4b9b0d2d1900e56df28f18522bfc42d09d6273a5b
wiki_role: wiki
---


# "Harvest Now Decrypt Later": Examining Post-Quantum Cryptography and the Data Privacy Risks for Distributed Ledger Networks

## Citation

Mascelli, Jillian, and Megan Rodden. "'Harvest Now Decrypt Later': Examining Post-Quantum Cryptography and the Data Privacy Risks for Distributed Ledger Networks". Finance and Economics Discussion Series (FEDS) 2025-093, Federal Reserve Board, September 2025. https://doi.org/10.17016/FEDS.2025.093.

## One-line summary

Quantum computers will be able to decrypt historical Bitcoin transaction data even after a network migrates to post-quantum cryptography, creating a permanent and irremediable data privacy vulnerability for distributed ledger networks.

## Key claims

- Distributed ledger networks can adopt post-quantum cryptographic standards to protect future transactions, but those standards leave historical transaction records permanently exposed.
- Bitcoin's public-key architecture means that addresses derived from exposed public keys remain vulnerable to decryption by a sufficiently powerful quantum computer.
- The immutability property of distributed ledgers, which prevents data deletion, compounds the "harvest now decrypt later" threat: adversaries can collect encrypted data today and decrypt it once quantum capability matures.
- Mitigation is structurally constrained: unlike centralised databases, no retroactive remediation of historical DLT records is possible without a protocol-breaking fork.
- The paper uses Bitcoin as the primary case study but the vulnerability applies to any permissioned or permissionless distributed ledger network that relies on elliptic-curve or RSA-based cryptography.

## Excerpts

> "Data privacy of the network's previously recorded transactions remains vulnerable despite protective measures for future transactions."
> ~ Abstract

> "Unlike traditional databases, distributed ledger networks cannot simply delete or re-encrypt historical transaction data — their immutability is a core design feature."
> ~ Section 2

> "A sufficiently powerful quantum computer could derive private keys from the public keys visible on the Bitcoin blockchain, enabling retrospective compromise of any address that has ever broadcast a transaction."
> ~ Section 3

## Significance

- Identifies a structural DLT security risk relevant to any tokenised asset infrastructure relying on public-key cryptography, including tokenised bond and settlement platforms.
- Informs central bank and regulator design choices for wholesale CBDC and permissioned DLT networks, where historical transaction confidentiality has legal and supervisory significance.
- Establishes a Fed staff position on the long-run data integrity of blockchain-based financial market infrastructure before quantum-capable hardware emerges.
- Directly relevant to the vault's blockchain-settlement and market-infrastructure domains, where record permanence is both a feature and a systemic vulnerability.

## Related

- [[10_Sources/Central-Banks/Fed-Tokenization-Financial-Stability]] - Fed overview of tokenisation financial stability implications
