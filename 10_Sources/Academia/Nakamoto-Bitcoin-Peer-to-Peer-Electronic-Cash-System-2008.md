---
type: source
title: 'Bitcoin: A Peer-to-Peer Electronic Cash System'
authors:
- Satoshi Nakamoto
organisation: Independent (pseudonymous author)
source_type: paper
venue: Self-published white paper (bitcoin.org)
year: 2008
date_published: '2008-10-31'
url: https://bitcoin.org/bitcoin.pdf
doi: ''
jurisdiction:
- INTL
domain:
- blockchain-settlement
- finance
doctrine: []
instrument: []
register_section: ''
status: draft
created: 2026-10-27
tags:
- source
- bitcoin
- proof-of-work
- white-paper
- backfill
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/blockchain-settlement
- topic/finance
---

# Bitcoin: A Peer-to-Peer Electronic Cash System

## Citation

Nakamoto, Satoshi. "Bitcoin: A Peer-to-Peer Electronic Cash System". Self-published white paper, 31 October 2008 (date supplied by the vault owner; the PDF text carries no date). https://bitcoin.org/bitcoin.pdf.

## One-line summary

Nakamoto proposes electronic cash that moves directly between parties without a trusted third party, using a proof-of-work chain of timestamped blocks to prevent double-spending.

## Key claims

- Electronic payments depend on trusted third parties, which raises costs and allows reversals and fraud (Section 1).
- A coin can be modelled as a chain of digital signatures, but a public history is needed to prevent double-spending (Section 2).
- Hashing transactions into a chain of timestamped blocks makes past records costly to alter (Section 3).
- Proof-of-work makes voting power proportional to CPU power, and the longest chain represents the majority decision (Section 4).
- Block rewards and transaction fees reward honest participation and introduce new coins without a central issuer (Section 6).
- Merkle trees let old transactions be pruned, and simplified payment verification lets users check payments without running a full node (Sections 7 and 8).
- If honest nodes control a majority of CPU power, the probability of an attacker overtaking the chain falls exponentially with each added block (Section 11).

## Excerpts

> "A purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another"
> ~ Abstract

> "What is needed is an electronic payment system based on cryptographic proof instead of trust"
> ~ Section 1

> "Proof-of-work is essentially one-CPU-one-vote."
> ~ Section 4

> "Nodes always consider the longest chain to be the correct one and will keep working on extending it."
> ~ Section 5

Reading note: a direct PDF fetch returned compressed binary only. The text was read through the r.jina.ai text proxy, and excerpts come from that text.

## Significance

- Primary source for the escape thesis, a payment and money system that avoids issuer and intermediary trust, against which the hierarchy-of-money and monetary sovereignty sources can be read.
- Origin of the ledger and consensus design that later tokenisation and stablecoin sources rely on for settlement.
- Not a legal or regulatory document, so it supports concept notes rather than any jurisdiction-specific analysis.

## Related

- [[10_Sources/Academia/Gorton-Zhang-Taming-Wildcat-Stablecoins-2023]] - stablecoins as private money on blockchain rails.
- [[10_Sources/Think-Tanks/Eichengreen-NBER-WP25426-Commodity-Fiat-Crypto-2019]] - history-of-money view of crypto-assets.
- [[10_Sources/Academia/Murau-Van-Klooster-Rethinking-Monetary-Sovereignty-2022]] - state governance of private money.
