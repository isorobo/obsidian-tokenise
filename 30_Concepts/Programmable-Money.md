---
name: Programmable Money
slug: Programmable-Money
type: concept
status: draft
created: 2026-08-09
domain:
- finance
synonyms:
- programmable digital money
defined_in: ''
related_concepts:
- '[[Atomic-Settlement]]'
- '[[Tokenised-Deposit]]'
- '[[Stablecoin]]'
- '[[Account-Abstraction]]'
- '[[Agent-Authority]]'
- '[[Unified-Ledger]]'
tags:
- concept
topic:
- topic/finance
wiki_indexed: '2026-08-17T00:00:00Z'
wiki_hash: f094534dce2abc8ed4b7af82f36a47a6c6b79f8852da8a3cd7d8b66800d9fddd
wiki_role: concept
---

> **For future Claude.** This note records how 13 verified vault sources use "programmable money" and nearby terms (programmability, programmable payments, programmable compliance) across CBDC, tokenised deposits, stablecoins and AI-agent payments. No source read gives a canonical definition, so the definition below is a working summary of the cited usages and `defined_in` is left empty. Drafted 2026-10-27; check the source table before relying on any one sense of the term.

# Programmable Money

> **Definition.** Working summary of the vault's usage, not a quoted definition: programmable money is digital or tokenised money whose use or transfer can be governed by code, so that set conditions are applied automatically when it is paid (usages in [[mas-parliamentary-reply-genius-act-2025]], [[US-Anti-CBDC-Surveillance-State-Act-2025]], [[IMF-Speech-2026-09-Katz-AI-Future-Payments-Policy]]).

## Why it matters

The term sits where the vault's money instruments meet its settlement and agentic-AI threads. Regulators in the vault test or plan programmability across several forms of money: MAS's Future of Finance Institute runs Industry Sandboxes for testing programmable money and tokenised assets (as of 2026-06, MAS) [[mas-future-of-finance-institute-2026]]; the HKMA said it would release a standardised token framework to facilitate programmable digital money adoption after its e-HKD pilot (as of 2025-10, HKMA) [[hkma-ehkd-pilot-programme-complete-2025]]; and Singapore-based institutions have tested stablecoins for programmable rewards and conditional payments (as of 2025-09, MAS) [[mas-parliamentary-reply-genius-act-2025]]. The vault's US legislative note records a different treatment for a Federal Reserve CBDC: its summary of the Anti-CBDC Surveillance State Act lists "programmable money using CBDC infrastructure" among the things prohibited, and records House passage on 2 July 2025 with the Senate stage pending (as of mid-2026, per the vault note) [[US-Anti-CBDC-Surveillance-State-Act-2025]]. In the agent-payments thread, sources describe AI agents executing transactions under predefined conditions [[mas-bloom-initiative-2025]] and programmable-payment protocols such as x402 that embed per-request payment into HTTP [[arXiv-2608-01341-402Pilot-x402-Agent-Micropayments]].

## How the vault's sources use the term

Confidence: every row is `stated` in the cited vault note unless flagged. Quotations are copied from the vault note's Excerpts or body; "None" means the note holds no verbatim passage on this point.

| Source | Issuer and date | How it uses the term | Verbatim quotation |
|---|---|---|---|
| [[US-Anti-CBDC-Surveillance-State-Act-2025]] | US Congress, H.R. 1919 (House passed 2025-07-02, per note) | Programmable money as a property of a CBDC; the note's summary of sponsor concerns lists a CBDC that could expire after fixed periods, restrict purchasing categories, apply negative rates automatically, or be frozen. The note's "Scope" line for Prohibition 4 lists programmable money, velocity controls, expiration dates and negative rates through CBDC infrastructure. | Note's summary: "Unlike cash or current bank deposits, a CBDC could be programmed to:" |
| [[mas-future-of-finance-institute-2026]] | MAS, 2026-06-25 | Programmable money named as a subject for the FFI's Industry Sandboxes, alongside tokenised assets and AI-enabled workflows; a Programmable Compliance Toolkit for tokenised assets is a named deliverable. | None |
| [[hkma-ehkd-pilot-programme-complete-2025]] | HKMA, 2025-10-28 | Programmability was one of three Phase 2 themes across 11 industry projects; a standardised token framework is to facilitate "programmable digital money" adoption. The note's Significance section links the framework to tokenised bank deposits and Project Ensemble. | None |
| [[mas-parliamentary-reply-genius-act-2025]] | MAS written reply, 2025-09-24 | Stablecoin use cases tested by Singapore-based institutions include programmable rewards and conditional payments, alongside cross-border settlement. | None |
| [[IMF-FTN-2025-011-Central-Bank-Tokenized-Reserves]] | IMF FinTech Note 2025/011, 2025-11 | Programmability applied to central bank money: tokenised reserves could bring programmable or automated liquidity management; programmability is one trade-off dimension when comparing RTGS links, omnibus accounts and privately issued tokenised money. | "it could introduce enhancements such as programmable or automated liquidity management, which may require updates to governance, legal frameworks, and risk management." |
| [[Ledger-Insights-Wells-Fargo-Tokenized-Deposit]] | Ledger Insights, 2026-08-04 | Added programmability listed among Wells Fargo's future plans for its tokenised deposit offering (as of 2026-08). | None |
| [[GL1-Programmable-Compliance-Whitepaper-2026]] | GL1 with IMF, Banque de France, Kinexys, MAS and Standard Chartered, 2026-06-22 | Programmable compliance: a Policy Wrapper locks a base token and issues a wrapped token, applying compliance conditions at the point of transfer. | "Programmable compliance concentrates compliance decision-making at runtime, increasing the consequences of design and governance choices." |
| [[mas-bloom-initiative-2025]] | MAS, 2025-10-16 | BLOOM workstreams include programmable compliance controls to automate cross-border checks, and agentic payments using AI to execute transactions under predefined conditions. | None |
| [[IMF-Speech-2026-09-Katz-AI-Future-Payments-Policy]] | IMF First Deputy Managing Director, 2026-09-28 | Says the financial architecture needs to become more programmable and that tokenised assets are natively programmable, in a speech on AI agents and payments. Flag: the note says quotations come from a republished copy because imf.org returned HTTP 403. | "Tokenized assets are natively programmable and can settle almost instantly, at any hour." |
| [[arXiv-2608-01341-402Pilot-x402-Agent-Micropayments]] | arXiv preprint, 2026-08-02 | "Programmable-payment protocols" for agent micropayments; x402 embeds per-request payment into HTTP. The paper's contribution is a decision layer for choosing what to buy, which it treats as separate from the payment protocol. | "Programmable-payment protocols such as x402 enable per-request micropayments, but they do not determine which payable service an autonomous agent should buy under a finite wallet." |
| [[BIS-WP1359-Anatomy-Stablecoin-Transactions]] | BIS Working Paper 1359, 2026-06-11 | "Programmable blockchains" as the setting in which stablecoin transfers are bundled atomically with trading, lending and other operations; nearly 60% of transfer events occur within complex transactions (Ethereum data). | "Stablecoin transfers are often interpreted as payments. On programmable blockchains, however, they are frequently embedded in atomically executed transaction bundles that combine trading, lending, arbitrage, liquidity provision, and settlement." |
| [[IMF-Note-2026-004-Agentic-AI-Payments]] | IMF Note 2026/004, 2026-04-24 | Does not use the term in the vault note. Relevant for agent payments: a three-layer model separating intent, authorisation and settlement, with smart contract wallet execution (ERC 4337) cited for DLT environments. | "In DLT environments used by stablecoins or central bank digital currencies, ERC 4337, launched in 2023, provides smart contract wallet execution for authorized transactions." |
| [[IMF-Adrian-Tokenized-Finance-Money-Speech-2026-05]] | IMF Financial Counsellor, 2026-05-11 | Does not use the term in the vault note. Relevant for governance of automated execution: calls for audit and override mechanisms for systemically important smart contracts. | "Legal mandates for financial stability must ultimately prevail over automated execution." |

## Open points

- **No canonical definition.** None of the 13 notes read defines programmable money. The definition above summarises usage; `defined_in` stays empty until a source with a formal definition enters the vault.
- **Money versus payment logic.** No source note read draws an explicit distinction between programmable money and programmable payments. The notes do place conditions in different places: the Anti-CBDC note describes conditions applied to the CBDC itself (expiry, purchasing-category limits) [[US-Anti-CBDC-Surveillance-State-Act-2025]]; the x402 paper speaks of programmable-payment protocols that embed payment into HTTP requests [[arXiv-2608-01341-402Pilot-x402-Agent-Micropayments]]; GL1 applies compliance conditions at the point of transfer through a wrapped token [[GL1-Programmable-Compliance-Whitepaper-2026]]. Whether the vault should treat these as one concept or separate concepts is not settled by its sources.
- **Measurement.** BIS WP 1359 warns that treating stablecoin transfers on programmable blockchains as standalone payments risks misclassifying a large share of on-chain use [[BIS-WP1359-Anatomy-Stablecoin-Transactions]]. Any usage figure for "programmable money" payments needs to state how bundled transactions were counted.
- **Governance of automated conditions.** The IMF calls for override mechanisms for systemically important smart contracts [[IMF-Adrian-Tokenized-Finance-Money-Speech-2026-05]], while GL1 notes that administrative keys or override authorities may become attack targets or sources of insider abuse [[GL1-Programmable-Compliance-Whitepaper-2026]]. The vault holds no source that resolves how these interact for programmable money specifically.
- **Time-sensitive items to recheck.** Whether the HKMA standardised token framework has been released [[hkma-ehkd-pilot-programme-complete-2025]]; outputs of the MAS FFI Industry Sandboxes [[mas-future-of-finance-institute-2026]]; Wells Fargo's programmability plans [[Ledger-Insights-Wells-Fargo-Tokenized-Deposit]]; the Senate stage of H.R. 1919 / S.1124 [[US-Anti-CBDC-Surveillance-State-Act-2025]]; and the Katz speech wording against the imf.org page [[IMF-Speech-2026-09-Katz-AI-Future-Payments-Policy]].

## Sources

- [[US-Anti-CBDC-Surveillance-State-Act-2025]]
- [[mas-future-of-finance-institute-2026]]
- [[hkma-ehkd-pilot-programme-complete-2025]]
- [[mas-parliamentary-reply-genius-act-2025]]
- [[IMF-FTN-2025-011-Central-Bank-Tokenized-Reserves]]
- [[Ledger-Insights-Wells-Fargo-Tokenized-Deposit]]
- [[GL1-Programmable-Compliance-Whitepaper-2026]]
- [[mas-bloom-initiative-2025]]
- [[IMF-Speech-2026-09-Katz-AI-Future-Payments-Policy]]
- [[arXiv-2608-01341-402Pilot-x402-Agent-Micropayments]]
- [[BIS-WP1359-Anatomy-Stablecoin-Transactions]]
- [[IMF-Note-2026-004-Agentic-AI-Payments]]
- [[IMF-Adrian-Tokenized-Finance-Money-Speech-2026-05]]

## See also

- [[MOC - Blockchain-Settlement]]
- [[MOC - Agent-Ledger-Interface]]
- [[MOC - Finance]]
- [[Atomic-Settlement]]
- [[Tokenised-Deposit]]
- [[Stablecoin]]
- [[Account-Abstraction]]
- [[Agent-Authority]]
- [[Unified-Ledger]]

## Verification

No `[V#]` markers were needed: every claim above is drawn from a cited vault note. Source-level caveats are listed under Open points.

| Marker | Claim | What would verify it |
|---|---|---|
| None | None | None |
