---
type: synthesis
date: 2026-06-30
tags:
- synthesis
- regulatory-frameworks
- jurisdictions
- pathways
- policy
related-sources:
- US GENIUS Act 2025
- EU MiCA Regulation 2023/1114
- EU DLT Pilot Regime 2022/858
- UK FCA guidance and Property Act 2025
- Singapore MAS Project Guardian and framework
- Hong Kong HKMA EnsembleTX and stablecoins ordinance
- Japan Payment Services Act amendments
- UAE VARA and ADGM frameworks
- FSB High-Level Recommendations 2023/2024
topic:
- topic/law
- topic/tokenisation
wiki_indexed: '2026-07-12T00:00:00Z'
wiki_hash: 76d2e6e54a9124d0ed4e43f1421632eb24a8bb31607f8a7e548d61ce98c18fd1
wiki_role: wiki
---


# Synthesis — Regulatory Pathways by Jurisdiction

For future Claude: Between late 2024 and mid-2026, tokenisation regulation has moved from principle-setting (FSB guidelines, OECD papers) to statutory law. The US passed the GENIUS Act (July 2025), the EU operationalised MiCA (December 2024) and the DLT Pilot Regime (21X AG and 360X AG authorised 2024–2025), and Asia-Pacific jurisdictions (Singapore, Hong Kong, Japan) enacted targeted frameworks. The regulatory pathways diverge sharply: the US is stablecoin-first (GENIUS Act); the EU is securities-and-settlement-centric (MiCA + DLT Pilot); Asia favours institutional pilot sandboxes (Project Guardian, EnsembleTX). This creates three regulatory regimes competing for institutional capital.

---

## The Jurisdictional Topology

As of June 2026, tokenisation regulation has coalesced into three clusters:

### Cluster A: Rules-Based National Statutes (US, UK)
**Governance model**: Legislate once, regulate thereafter; private sector experiments within statute
**Speed of innovation**: High; once law is in place, market can move without regulatory approval (GENIUS Act framework)
**Risk tolerance**: High for stablecoins and securities; private-sector led

**Key statutes:**
- [[10_Sources/Law-Regulation/US-GENIUS-Act-2025.md|GENIUS Act (July 2025)]] — first federal stablecoin statute; requires 1:1 backing; prohibits non-permitted issuers
- [[10_Sources/Law-Regulation/UK-Property-Digital-Assets-Act-2025.md|Property (Digital Assets etc) Act 2025]] — creates legal certainty for token ownership; no explicit stablecoin statute (existing PSR framework applies)
- [[10_Sources/Law-Regulation/US-UCC-Article-12.md|UCC Article 12]] — 26 states adopted; makes tokenised assets property across US

### Cluster B: Regulatory Harmonisation with Exemptions (European Union)
**Governance model**: Harmonise rules across member states; carve out experimental zones
**Speed of innovation**: Moderate; MiCA sets the baseline, DLT Pilot carves out exemptions for designated networks
**Risk tolerance**: Moderate; regulatory approval required for payment stablecoins; securities tokenisation permitted only on DLT Pilots

**Key frameworks:**
- [[10_Sources/Law-Regulation/EU-MiCA-Regulation.md|MiCA (in full effect 30 December 2024)]] — harmonised rules for stablecoins and crypto-asset service providers
- [[10_Sources/Law-Regulation/EU-DLT-Pilot-Regime.md|DLT Pilot Regime (Regulation 2022/858)]] — exempts designated networks (21X AG, 360X AG) from MiFID II and CSDR for tokenised securities and UCITS
- Individual member-state implementations (some stricter than EU baseline)

### Cluster C: Sandbox-Driven Public-Private Pilots (Singapore, Hong Kong, Japan)
**Governance model**: Conduct supervised pilots with specific institutional participants; regulatory approval on pilot-by-pilot basis
**Speed of innovation**: Highest at scale; institutional buy-in is demonstrated before regulation
**Risk tolerance**: Depends on pilot; stablecoins excluded from most Asia pilots (reserved for domestic CBDC); focus on securities and deposits

**Key frameworks:**
- [[10_Sources/Central-Banks/MAS-Project-Guardian.md|Singapore MAS Project Guardian]] (2022–ongoing) — 40+ participants; tokenised funds, fixed income, FX
- [[10_Sources/Central-Banks/HKMA-EnsembleTX.md|Hong Kong EnsembleTX]] (November 2025 pilot announcement) — tokenised deposits and asset tokenisation; initial participants BlackRock, Franklin Templeton, HSBC, Standard Chartered
- [[10_Sources/Law-Regulation/Japan-Payment-Services-Act.md|Japan PSA amendments (2023)]] — permits bank-issued stablecoins (tokenised deposits)
- [[10_Sources/Law-Regulation/UAE-VARA.md|UAE VARA]] and [[10_Sources/Law-Regulation/UAE-ADGM.md|ADGM]] — tokenised funds in the Gulf

---

## The GENIUS Act (US) — Stablecoin-First Approach

[[10_Sources/Law-Regulation/US-GENIUS-Act-2025.md|The GENIUS Act, signed into law 18 July 2025]], is the regulatory headline. Key provisions:

**1:1 Backing Requirement**
- A permitted payment stablecoin issuer must hold reserves equal to circulation in US dollars or low-risk liquid assets (duration <1 year, minimum AA credit rating)
- Reserves must be held in a segregated account at a Federal Reserve member bank or eligible custodian
- Quarterly attestation required

**Issuer Restrictions**
- Only authorised payment stablecoin issuers can issue
- Banks and trust companies: automatic eligibility (regulated under banking law)
- Non-bank payment app providers: must apply to Fed; application requirements not yet specified (expected in 2026 implementing regulations)
- Crypto exchanges, private equity firms, tech platforms: prohibited

**Monetary-Policy Coordination**
- Federal Reserve must approve stablecoin reserves held at regional banks
- Stablecoin circulation is monitored as a component of narrow money (M1)
- Fed can recommend to Congress that Congress limit stablecoin circulation if systemic risks emerge

**Effective Date**
- Takes effect at the earlier of 18 months from enactment (January 2027) or 120 days after implementing regulations finalised
- Implementing regulations expected Q3–Q4 2026

**Implications**:
- USDC (Circle, a licensed money transmitter) will likely seek Fed approval as a non-bank issuer
- USDT (Tether) and other non-bank issuers must either exit the US market, partner with a bank, or seek exceptional approval
- JPMorgan JPM Coin (bank-issued) qualifies automatically
- Coinbase stablecoin proposals (Coinbase USD) will require Fed approval

**Competitive impact**: The GENIUS Act creates a two-tier market: Fed-approved stablecoins (likely USDC, JPM Coin, and 2–3 others) and non-approved stablecoins (unlikely to obtain US clearing or settlement). This consolidates USD stablecoin supply onto a small number of issuers and effectively bars retail crypto projects from USD stablecoin issuance.

---

## The EU Approach: MiCA + DLT Pilot Regime

[[10_Sources/Law-Regulation/EU-MiCA-Regulation.md|MiCA (in full effect 30 December 2024)]] is the EU's harmonised framework for crypto-asset service providers. It does **not** cover tokenised securities or tokenised deposits (those remain under MiFID II and CRR/CRD). Instead, MiCA focuses on **stablecoins and other crypto-assets**.

**Stablecoin Rules (MiCA Articles 16–20)**
- Asset-referenced tokens (e.g., a multi-currency stablecoin) must hold reserves equal to circulation
- Fiat-referenced tokens (e.g., EURC, a euro stablecoin) must be issued by a credit institution or electronic-money institution
- Significant stablecoin issuers (>EUR 5 million circulation) must comply with stress tests and buffer requirements
- Stablecoin transfers for cross-border payments are prohibited in some member states (ongoing implementation variation)

**DLT Pilot Regime ([[10_Sources/Law-Regulation/EU-DLT-Pilot-Regime.md|Regulation 2022/858]])**
- Exempts designated DLT networks from MiFID II and CSDR (post-trade settlement rules) for tokenised securities
- Scope: tokenised shares, bonds, UCITS, and derivatives
- Participants: 21X AG and 360X AG (both authorised as of April 2025)
- Public-blockchain trading (e.g., tokenised bonds on Ethereum) is **not** permitted under the DLT Pilot; only permissioned networks qualify

**Implication**: The EU has created a **bifurcated market**:
- Public-blockchain tokenisation: must comply with MiCA (if stablecoins/crypto-assets) or existing securities regulation (if registered securities)
- DLT Pilot permissioned settlement: exempted from legacy post-trade rules; fast-track regulatory approval

This creates a genuine **regulatory arbitrage opportunity**: a financial institution choosing between settling a tokenised bond on Ethereum (subject to MiFID II and CSDR, plus national implementation variation) or on a DLT Pilot network (exempted from CSDR; lighter-touch MiFID II application). The DLT Pilot is **faster and cheaper** for the specific use case of institutional settlement.

**Competitive impact**: Expect EUR 50–100 billion of institutional tokenised-securities issuance to route through 21X AG and 360X AG by end-2026, with public-blockchain issuance (Ethereum, Polygon) relegated to smaller, tech-native issuers and non-bank platforms.

---

## Asia-Pacific: Sandbox-Driven Acceleration

### Singapore — MAS Project Guardian

[[10_Sources/Central-Banks/MAS-Project-Guardian.md|Project Guardian]] (2022–ongoing) is a *regulatory sandbox* involving 40+ participants (DBS, JPMorgan, UBS, Apollo, Franklin Templeton, Ant Group). The model:
1. Participants propose use cases (tokenised funds, fixed income, FX)
2. MAS grants exemptions from existing Monetary Authority Act and Securities Act provisions
3. Participants test the use case under MAS supervision
4. If successful, regulation is drafted to accommodate the use case

**Tokenised Funds** (most mature use case):
- [[10_Sources/Central-Banks/MAS-Project-Guardian-Operationalising-Funds.md|MAS Operationalising Tokenised Funds guide]] (November 2025) sets out operational requirements: governance, NAV calculation, investor onboarding, compliance
- In-scope use cases: mutual funds, private-credit funds, real-estate funds
- Settlement: Participants tested SWIFT/HVPS (traditional) and experimental tokenised settlement (on a permissioned ledger)
- Competitive impact: Institutional funds are *easier* to tokenise than retail funds (fewer unit holders, simpler redemptions); expect USD 100 billion+ of institutional-fund tokenisation via Project Guardian pathways by end-2027

### Hong Kong — EnsembleTX and Stablecoins Ordinance

[[10_Sources/Central-Banks/HKMA-EnsembleTX.md|EnsembleTX]] (pilot announced November 2025) is Hong Kong's tokenised-deposit settlement architecture. Key features:
- Connects commercial-bank tokenised deposits (on a permissioned network) to the wholesale CBDC (e-HKD) on HKMA-controlled infrastructure
- Initial participants: Standard Chartered, HSBC, Bank of China (HK), BlackRock, Franklin Templeton
- Use cases: tokenised money-market fund transactions, intraday liquidity management
- Settlement initially via HKD RTGS; planned upgrade to 24/7 tokenised central-bank-money settlement

**Stablecoins Ordinance** (2025): Licensing regime for fiat-referenced stablecoin issuers operating in Hong Kong. More restrictive than Singapore (no asset-referenced tokens permitted); stablecoins are treated as near-money instruments requiring central-bank approval.

**Competitive impact**: Hong Kong is positioning as the **institutional cash settlement hub** for Asia—competing with Singapore's broader asset-tokenisation sandbox. Expect tokenised multi-currency cash (HKD, CNY, USD) to settle via EnsembleTX pathways, with higher regulatory certainty than Singapore's experimental approach.

### Japan — Bank-Issued Stablecoins

[[10_Sources/Law-Regulation/Japan-Payment-Services-Act.md|Japan's Payment Services Act amendments (2023)]] explicitly permit banks to issue stablecoins (tokenised deposits). This is the only major economy to do so; the US (GENIUS Act) and EU (MiCA) restrict stablecoin issuance to banks and money-transmitters, but Japan treats stablecoins *as* deposits, not as separate crypto-assets.

**Implication**: Japanese megabanks (Mitsubishi UFJ, Sumitomo Mitsui, Mizuho) are expected to launch tokenised-yen stablecoins (2026–2027), creating competition for USDC and USDT in yen-denominated onshore settling.

---

## Convergences and Divergences Across Clusters

### Convergence 1: Stablecoin Backing
All three clusters require (or are moving toward) **1:1 backing** of stablecoins:
- US GENIUS Act: explicit 1:1 requirement
- EU MiCA: explicit reserve requirement for asset-referenced and fiat-referenced tokens
- Asia (Singapore, Japan): MAS guidance and Japanese banking rules assume backing; Hong Kong Ordinance requires it

**Why**: Reserve requirements are the regulatory consensus mechanism for preventing stablecoin runs and bank-like contagion.

### Convergence 2: Segregation and Custody
All frameworks require **segregation** of customer assets from issuer/service-provider assets:
- US GENIUS Act: reserves held in segregated account at Fed-member bank
- EU MiCA: asset-referenced tokens must hold segregated reserves
- Asia: MAS Project Guardian and HKMA EnsembleTX both mandate custody segregation; HKMA explicitly runs on CBDC rails (segregation enforced at central bank)

**Why**: Segregation protects token holders from issuer bankruptcy.

### Divergence 1: Permissioned vs Public Settlement
- **US**: Indifferent (GENIUS Act applies to stablecoins regardless of settlement layer)
- **EU**: Prefers permissioned settlement (DLT Pilot exemptions; public-blockchain tokenisation subject to full MiFID II)
- **Asia**: Piloting both permissioned (EnsembleTX) and mixed (Project Guardian with both permissioned and SWIFT settlement)

**Implication**: Expect institutional tokenised-securities issuance to route through EU DLT Pilots (permissioned) and Asia sandboxes (permissioned), while retail and tech-native tokenisation remains on public blockchains.

### Divergence 2: Speed of Regulatory Finalisation
- **US**: GENIUS Act is statutory; implementing regulations (Fed approval process for non-bank issuers) expected Q3–Q4 2026
- **EU**: MiCA is in effect (30 December 2024); DLT Pilot is active (21X AG, 360X AG operating); no further legislative change needed for 2026–2027
- **Asia**: Sandboxes are indefinite (no statutory endpoint); regulatory codification will come *after* successful pilot completion (2027–2028)

**Implication**: EU is fastest to operate (MiCA + DLT Pilot live now); US has statutory clarity but implementation gap (Fed rules pending); Asia has institutional buy-in but regulatory permanence uncertain.

---

## Regulatory Arbitrage Opportunities and Risks

### Opportunity 1: Dual-Jurisdiction Structuring
A financial institution wanting to issue tokenised securities can:
1. Issue on an EU DLT Pilot network (exempt from CSDR; faster settlement) with European investors
2. Simultaneously issue on Ethereum with US investors (subject to SEC oversight but technologically simpler)
3. Coordinate settlement via custodian bridges, splitting regulatory burden

**Risk**: If regulators view dual issuance as regulatory evasion (avoiding full CSDR in EU while issuing equivalent instrument on Ethereum in US), enforcement action is possible.

### Opportunity 2: Asia-First Innovation
A bank or asset manager wanting to test a novel tokenisation use case (e.g., tokenised securitised mortgages, tokenised insurance contracts) can:
1. Propose the use case to MAS or HKMA as a sandbox pilot
2. Gain regulatory exemption and supervision in Singapore or Hong Kong
3. Demonstrate success with institutional participants
4. Export the operational model to EU (DLT Pilot) or US (post-GENIUS Act) with regulatory precedent

**Risk**: Pilot success does not guarantee scalability; Singapore and Hong Kong are small markets; scaling to global capital markets requires additional regulatory approvals.

### Risk 1: Regulatory Divergence Creates Fragmentation
If the US enforces GENIUS Act strictly (Fed approval required for non-bank stablecoin issuers), the EU allows asset-referenced tokens without Fed-equivalent approval, and Asia permits experiments with lighter oversight, institutions face a **three-tier regulatory landscape**:
- Tier 1 (US): Tightest, most credible to US regulators
- Tier 2 (EU): Harmonised but fragmented by member-state implementation
- Tier 3 (Asia): Most experimental but smallest market

Institutions will likely **choose the tier offering the best risk-return trade-off for their business model**, creating regulatory arbitrage at the margin and potential supervisory gaps.

### Risk 2: Stablecoin Oversupply in Non-GENIUS Act Jurisdictions
If GENIUS Act enforcement reduces US stablecoin issuance, non-approved stablecoins (USDT, smaller projects) may migrate to EU (under MiCA, if compliant) or Asia. This could create a **shadow stablecoin market** outside US regulatory reach—the regulatory outcome that GENIUS Act was designed to prevent.

---

## Timeline and Next Regulatory Milestones

| Date | Event | Jurisdiction | Impact |
|---|---|---|---|
| Q3–Q4 2026 | Fed implementing regulations for GENIUS Act non-bank issuers | US | Clarity on which non-bank stablecoin issuers (Circle, Coinbase) can operate; USDT likely exits US retail |
| H1 2027 | GENIUS Act effective date (18 months from enactment = January 2027) | US | Approved stablecoins must migrate to Fed-approved custody; non-approved stablecoins cease US settlement |
| H1 2027 | EU MiCA member-state divergence data (first annual audit of national implementations) | EU | Clarity on whether member states diverge significantly from MiCA baseline; if so, expect regulatory harmonisation push |
| H2 2027 | MAS Project Guardian tokenised-funds report (expected maturation of pilot) | Singapore | Foundation for statutory codification; likely to inform other Asia-Pacific regulatory frameworks |
| H2 2027 | HKMA EnsembleTX operational data (first full year of tokenised-deposit settlement) | Hong Kong | Proof of concept for institutional tokenised-deposit settlement; model likely adopted by mainland China |
| 2027–2028 | Japan bank-issued stablecoin launches (post-regulatory clarification) | Japan | Introduction of yen-denominated tokenised deposits; potential competition for USDC in Asia |

---

## Next Actions

1. **Monitor Fed regulatory release schedule** (expected Q3–Q4 2026) for GENIUS Act implementing regulations. The non-bank issuer approval process will determine whether Circle (USDC) and Coinbase retain US market access.

2. **Track EU member-state MiCA implementation** (first audit expected H1 2027). Identify member states that diverge significantly from MiCA baseline; this determines whether EU institutional tokenisation remains harmonised or fragments.

3. **Commission a GENIUS Act / MiCA / Asia comparison study** for institutional clients: Which jurisdiction should an asset manager use to issue a tokenised fund? Build a decision matrix weighted by (a) regulatory clarity, (b) settlement speed, (c) custodial cost, (d) target investor base.

4. **Prepare for stablecoin migration**: If USDT exits the US market post-GENIUS Act, institutions holding USDT-based positions will need to migrate to approved alternatives (USDC, JPM Coin, etc.). Estimate costs and risks of migration for major institutional portfolios.

5. **Scout Asia-Pacific regulatory opportunities**: Institutions wanting first-mover advantage in novel tokenisation use cases should begin scoping MAS Project Guardian and HKMA EnsembleTX participation. Approval cycles are 6–12 months; applications should begin now (mid-2026) for 2027 pilot launches.
