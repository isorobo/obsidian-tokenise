---
type: source
title: 'Programmable Compliance: Compliance Architecture for Regulated Tokenised Assets'
authors:
- Khai Uy Pham (Banque de France)
- Sonja Davidovic (International Monetary Fund)
- Weekee Toh (Kinexys by J.P. Morgan)
- Kenneth See (Monetary Authority of Singapore)
- Cayden Chang (Standard Chartered Bank)
- Sam Vicary (Standard Chartered Bank)
organisation: Global Layer One (GL1)
source_type: paper
venue: Global Layer One (GL1) White Paper
year: 2026
date_published: '2026-06-22'
url: https://global-layer-one.org/pdf/gl1-pc-whitepaper-22-jun-2026.pdf
doi: ''
jurisdiction:
- MULTI
- INTL
domain:
- finance
- market-infrastructure
- blockchain-settlement
- cross-border-payments
doctrine:
- aml-cft
- disclosure
- transfer
instrument:
- tokenised-bond
- tokenised-deposit
- tokenised-fund
register_section: ''
nlm_id: ''
nlm_skip: false
status: draft
created: 2026-07-13
tags:
- gl1
- global-layer-one
- programmable-compliance
- tokenisation
- aml-cft
- compliance-architecture
- imf
- banque-de-france
- kinexys
- mas
- standard-chartered
watchlist_channel: mas-news
topic:
- topic/finance/market-infrastructure
- topic/blockchain-settlement
wiki_indexed: '2026-07-19T00:00:00Z'
wiki_hash: 8ea15129a1595fd86f06c2094a26f61d47925ff0dcca5f9558a512d97321e3f8
wiki_role: wiki
---


# Programmable Compliance: Compliance Architecture for Regulated Tokenised Assets

## Citation

Global Layer One (GL1). "Programmable Compliance: Compliance Architecture for Regulated Tokenised Assets". Global Layer One (GL1) White Paper, 22 June 2026. https://global-layer-one.org/pdf/gl1-pc-whitepaper-22-jun-2026.pdf.

Retrieved directly from the canonical GL1 PDF. MAS's own site carried no independent release page and stayed unreachable throughout this run, matching the channel's known bottleneck. Ledger Insights, Bermuda's PR Newswire release, and Chainlink's official post corroborate the publication date and contributor list.

## One-line summary

GL1, with the IMF, Banque de France, Kinexys, MAS, and Standard Chartered, proposes a compliance architecture embedding regulatory checks into tokenised-asset transfers.

## Key claims

- The paper proposes a STAR framework, covering Status, Transaction, Asset, and Reporting, that separates policy definition from transaction execution.
- Four features implement the model: an Identity Management Module, a Policy Wrapper, a Policy Manager, and Administrative Control.
- The Policy Wrapper locks a base asset token and issues a wrapped token, applying compliance conditions at the point of transfer.
- Every transaction generates a Transaction Envelope that accumulates identity data and produces a Compliance Attestation recording the pass or fail outcome.
- The architecture builds on existing initiatives, including BIS Innovation Hub's Project Mandala, Chainlink's Automated Compliance Engine, and GLEIF's verifiable Legal Entity Identifiers.
- The paper identifies residual risks, such as stale sanctions data, and novel risks, such as oracle dependency and administrative-key concentration.
- Compliance Attestations are execution-time records only; they do not substitute for statutory filings such as suspicious activity reports.

## Excerpts

> "This paper proposes an architectural model that addresses these limitations by separating policy definition, identity management, compliance evaluation, and transaction execution into distinct but coordinated components."
> ~ Introduction, p.5

> "Rules fixed at deployment can only be updated by modifying the contract itself, which becomes increasingly burdensome as regulatory requirements evolve."
> ~ Introduction, pp.4-5

> "Compliance Attestations are execution-time records of compliance evaluation outcomes. They are not equivalent to regulatory filing obligations such as suspicious activity reports, transaction reports, or other regulatory returns, which remain distinct obligations governed by applicable law and reporting requirements."
> ~ Governance and Accountability, pp.28-29

> "Administrative keys or override authorities may become high-value attack targets or sources of insider abuse."
> ~ Risk and Governance Considerations, p.26

> "Programmable compliance concentrates compliance decision-making at runtime, increasing the consequences of design and governance choices."
> ~ Conclusion, p.30

## Significance

- The paper evidences convergence between MAS, the IMF, Banque de France, and Kinexys on one technical compliance standard for tokenised assets.
- The STAR framework and Policy Wrapper give the wiki a concrete technical definition of programmable compliance, separate from AML/CFT policy statements alone.
- MAS's Future of Finance Institute named a Programmable Compliance Toolkit three days after this paper, tying GL1's model to Singapore's deployment roadmap.
- The Governance and Accountability section separates on-chain Compliance Attestations from statutory filings, informing the wiki's disclosure and reporting doctrine thread.

## Related

- [[10_Sources/Central-Banks/mas-future-of-finance-institute-2026]] - FFI's Programmable Compliance Toolkit, announced three days after this paper
- [[10_Sources/Central-Banks/mas-leong-layer-one-summit-2025]] - Earlier MAS speech naming GL1's backers and mandate
- [[10_Sources/Central-Banks/mas-safr-agentic-finance-safeguards-2026]] - MAS's parallel runtime-governance framework, published eleven days later
