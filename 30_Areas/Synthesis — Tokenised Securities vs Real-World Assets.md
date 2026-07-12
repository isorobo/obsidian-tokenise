---
type: synthesis
date: 2026-06-30
tags:
- synthesis
- securities
- RWA
- tokenisation
- asset-class
- equity
- bonds
- treasury
related-sources:
- BIS Tokenisation Continuum
- IOSCO Decentralised Finance Report and Crypto Policy Recommendations
- IMF Tokenization and Financial Market Inefficiencies
- Standard Chartered / Synpulse RWA Market Report
- BlackRock BUIDL and tokenised-treasury sector
- Citi GPS Money Tokens Games
- McKinsey From Ripples to Waves
- EU MiCA and DLT Pilot Regime
- Academic — Tokenised-Bond Empirical Study
- Oraclizer Why Institutional Tokenization Stalls
topic:
- topic/law/securities
- topic/tokenisation
wiki_indexed: '2026-07-12T00:00:00Z'
wiki_hash: 1e78f0e6418f4e95846f10475bad8692e48850dbcf2d55a64faea1f1e7e8487b
wiki_role: wiki
---


# Synthesis — Tokenised Securities vs Real-World Assets

For future Claude: Tokenised securities (equities, bonds, funds) and tokenised real-world assets (real estate, trade finance, carbon credits) are reaching market at different speeds and for different reasons. Tokenised securities (especially US Treasury debt and money-market funds) are the early winner—USD 11 billion in tokenised treasuries by May 2026, with institutional adoption (BlackRock BUIDL) driving liquidity. Tokenised RWA (real estate, trade finance) remain fragmented and small (0.1% of the projected USD 30 trillion market). The divergence reflects that securities are *already digital* at the ownership layer (you own shares in a cap table; it is just a database), whereas RWA tokenisation requires solving the **legal registry interface problem** (how does a token on Ethereum relate to a land deed in Singapore?). Securities tokenisation is a UI upgrade; RWA tokenisation is a legal infrastructure rebuild.

---

## The Asset-Class Divergence

### Category 1: Tokenised Securities (Dominant, Growing Fast)

**Sub-categories and their status**:

#### Tokenised US Treasuries and Money-Market Funds
- **Market size**: USD 11 billion (BlackRock BUIDL USD 2.5B; Ondo Finance, WisdomTree, Hashnote, Backed Finance combined USD 8.5B) as of May 2026
- **Growth trajectory**: Doubling every 3–6 months
- **Key drivers**:
  - 24/7 market access (Ethereum never closes)
  - Fractional ownership (BUIDL minimum investment reduced from USD 10M to USD 1 for retail)
  - Institutional custody infrastructure (Fidelity, Kraken, Coinbase offer tokenised-treasury accounts)
- **Regulatory status**: US SEC has issued no-action letter to BlackRock/Securitize; tokenised treasuries are treated as securities under existing rules; no new statute required
- **Technology stack**: Ethereum and multi-chain (Polygon, Arbitrum, Avalanche, Optimism) deployment

#### Tokenised Corporate Bonds
- **Market size**: Estimated USD 0.5–1 billion (nascent)
- **Key issuers**: HSBC (Orion platform), Goldman Sachs (DAP), Deutsche Bank, European Investment Bank
- **Regulatory status**: EU DLT Pilot Regime exempts designated networks; public-blockchain (Ethereum) issuance requires full MiFID II compliance
- **Empirical cost evidence**: [[10_Sources/Academia/Belkhiria-ODDO-Bond-2026.md|Belkhiria et al. 2026]] documents 41.5% trading-process cost reduction on a tokenised ODDO BHF corporate bond
- **Growth constraint**: Multi-chain fragmentation (Ethereum, Polygon, DLT Pilot networks) fragments liquidity; no single centralised order book

#### Tokenised Equities and Fund Shares
- **Market size**: Estimated USD 2–5 billion (early stage)
- **Status**: Most existing funds issue on permissioned networks (Polymesh, Provenance) or private investor portals; no major public-blockchain equity tokenisation yet
- **Regulatory challenge**: Shares have embedded voting rights and dividend mechanics; tokenising them requires custody and corporate-action infrastructure (more complex than bonds)
- **Institutional interest**: High; 40+ participants in MAS Project Guardian are tokenising private-credit and private-equity fund units

#### Tokenised Funds (Mutual Funds, UCITS, Private Funds)
- **Market size**: Estimated USD 5–10 billion (growing fastest)
- **Key pilot**: MAS Project Guardian and HKMA EnsembleTX both focus on tokenised-fund settlement
- **Regulatory status**: UCITS tokenisation is permitted under EU DLT Pilot; private funds under Regulation D exemption in US
- **Operational breakthrough**: [[10_Sources/Central-Banks/MAS-Project-Guardian-Operationalising-Funds.md|MAS operational guide (November 2025)]] specifies NAV calculation, investor onboarding, and redemption mechanics—removing the last major operational uncertainty
- **Institutional adoption**: Expect USD 50–100 billion of tokenised institutional-fund issuance (pension funds, insurance companies, asset managers) within 18 months following MAS guide publication

---

### Category 2: Tokenised Real-World Assets (Emerging, Fragmented)

#### Tokenised Real Estate
- **Market size**: Estimated USD 500 million–1 billion (extremely small relative to projected USD 50+ trillion real-estate market)
- **Key barriers**:
  - Legal registry interface: A token on Ethereum cannot *be* a property deed; it must *represent* an off-ledger deed held by a jurisdiction-specific land registry
  - Jurisdictional fragmentation: Land title is registered at county, state, or national level; no global real-estate registry exists
  - Velocity mismatch: Real estate is a 10–30 year hold; tokenisation gains (fractional ownership, 24/7 trading) are irrelevant to hold-period economics
  - Fractional-secondary-market liquidity: A real-estate REIT can be tokenised and fractionated, but the underlying property remains indivisible; secondary-market trading is thin
- **Key platforms**: RealT (Detroit single-family rentals), Propy, Blocksquare, Brickken
- **Regulatory status**: Highly variable by jurisdiction; Singapore (ADGM) and UAE (VARA) have tokenised-fund sandboxes; US real-estate tokenisation largely unregulated

#### Tokenised Trade Finance
- **Market size**: Estimated USD 0–100 million (pilots only)
- **Projected size**: [[10_Sources/Commercial-Banks/Standard-Chartered-Synpulse-RWA.md|Standard Chartered/Synpulse projects USD 4.8 trillion by 2034]] (16% of USD 30.1 trillion total RWA)
- **Key innovation**: Tokenised letters of credit and payment-on-first-demand clauses compress 7–14 day settlement to 1–3 days (trade finance is slower than securities)
- **Regulatory status**: Limited regulatory clarity; pilots under MAS Project Guardian and individual central banks (HKMA, Bank of England, ECB)
- **Adoption blockers**: Requires interbank messaging protocol upgrades (SWIFT modernisation); legacy systems still dominant

#### Tokenised Carbon Credits
- **Market size**: Estimated USD 50–200 million of on-chain carbon credit circulation (2–3% of voluntary carbon-market USD 6–7 billion)
- **Key market-structure inflection**: [[10_Sources/Law-Regulation/Verra-Immobilisation-Policy.md|Verra's 2022 suspension of third-party tokenisation]] and [[10_Sources/Law-Regulation/Gold-Standard-Consent-Framework.md|Gold Standard consent framework]] mean tokens do not replace registries—they *track* registry-held credits
- **Platforms**: Toucan Protocol (Polygon), KlimaDAO (Ethereum), AirCarbon Exchange (Singapore), Climate Impact X (Singapore)
- **Regulatory status**: Nascent; ICVCM Core Carbon Principles and VCMI Claims Code set quality benchmarks, but tokenisation-specific rules do not exist
- **Economics**: Tokenisation does not change the cost of credit *generation* (offset verification is expensive); it reduces credit *transfer* friction and enables fractional ownership
- **Adoption constraint**: Registry consent requirement means carbon-credit tokenisation cannot proceed without voluntary-market registry approval—regulatory bottleneck

---

## Why Securities Tokenisation is Winning (Structural Advantages)

### Advantage 1: No Off-Ledger Registry Problem
A tokenised US Treasury bond *is* the treasury bond for settlement purposes. The bond is already defined by its CUSIP (Committee on Uniform Security Identification Procedures) and exists in a database (Treasury Department, DTC). Putting the bond on Ethereum is a **UI upgrade**—switching from one database (legacy DTCC) to another (Ethereum). No new legal framework is required; the US SEC already has jurisdiction over treasury bonds.

By contrast, a tokenised real-estate property token is **not** the deed. The token represents a claim on a property held in a Delaware trust, which holds a deed filed with the county recorder in Nashville, Tennessee. The on-chain token must *reference* the off-chain deed; they are not identical. This requires:
1. A legal opinion that the token holder's right to the asset is enforceable
2. A custody arrangement linking the token to the deed
3. A mechanism to update the off-chain deed if the on-chain token owner changes

This is three times the legal complexity.

### Advantage 2: Institutional Custody Infrastructure Already Exists
Fidelity, Kraken, and Coinbase have built Ethereum custody infrastructure for retail and institutional crypto users. They can **reuse** this infrastructure for tokenised treasuries—no new custody layer required. Institutional clients can hold BUIDL (BlackRock tokenised treasury) in the same Fidelity account they use for USDC and other crypto.

Real-estate tokenisation requires **new custody infrastructure**: a tokenised-REIT custodian must manage off-chain property deeds, coordinate with real-estate attorneys, and integrate with jurisdictional land registries. This is a 2–3 year build, not a reuse.

### Advantage 3: Settlement Rules Are Standardised Across Jurisdictions
An institutional investor buying a US Treasury bond follows the same settlement rules whether it is tokenised or traditional. The US SEC, FINRA, and DTCC have 50 years of rulings and guidance. Tokenisation changes the *technology*, not the *rules*.

Real-estate settlement rules vary by jurisdiction (US states, EU member states, Asia-Pacific countries). A property deed in Tennessee is registered differently than one in Singapore. Tokenisation creates a **legal-framework gap**: the token is on Ethereum (global), but the property is in a jurisdiction (local). Institutions must navigate both.

### Advantage 4: Liquidity Clustering on Ethereum
Tokenised treasuries have clustered on Ethereum (BUIDL's dominant chain) and a few secondary chains. This creates a **liquidity flywheel**: more assets on Ethereum → lower fees → more assets attracted. Secondary-market bid-ask spreads on BUIDL are tight (1–5 bps) because Ethereum has deep USDC liquidity and active trading.

Real-estate tokenisation has not clustered; each platform uses its own chain (RealT on Ethereum, Blocksquare on permissioned networks, others on Polygon). This **fragments liquidity**: no central order book exists. A real-estate token on Ethereum cannot instantly arb against one on Polygon without bridge risk and latency.

---

## Why RWA Tokenisation Remains Fragmented (Structural Barriers)

### Barrier 1: Legal Registry Interface Problem
A real-world asset has a legal owner or custodian recorded in an off-ledger registry:
- Real estate: county land registry
- Trade finance: bank's internal ledger and shipping documents
- Carbon credits: Verra, Gold Standard, or Article 6 registries
- Intellectual property: trademark office, copyright office

A token on Ethereum is a **different legal entity** than the registry entry. For the token to represent the asset with legal enforceability, the token holder must have a contractual or statutory right to enforce the off-ledger registry entry against the issuer or custodian. This requires:

1. **A legal opinion** that the token holder's right is enforceable in the asset's home jurisdiction
2. **Custody at the registry**: An agent (SPV, bank, or registry) must confirm that they hold the off-ledger asset on behalf of the token holder
3. **A transfer mechanism**: When the token changes hands on-chain, the off-ledger custody must update

Tokenised securities bypass this because the security *is* the database entry—the token updates the database entry in real-time. Tokenised RWA must maintain **two ledgers** (on-chain token + off-ledger registry) in sync, creating a reconciliation burden.

### Barrier 2: Velocity Mismatch
Tokenisation's primary efficiency gains are:
- **Intraday settlement**: Reduces working-capital tied up in settlement float (relevant to high-velocity assets: bonds, equities, money-market funds trading dozens of times per day)
- **24/7 trading**: Enables after-hours and weekend trading (relevant to 24/7-market-access use cases: crypto-native investors)
- **Fractional ownership**: Enables retail access to assets (relevant to high-value assets: real estate, art)

But these gains are **orthogonal to real-world asset returns**. A real-estate investor holding a property for 15 years does not benefit from T+0 settlement (whether it settles T+2 or T+0, the return depends on the property's cash flow and appreciation, not settlement speed). A carbon credit held for 3–5 years before offsetting benefits from fractional ownership, but not from intraday settlement.

So the **economic value of RWA tokenisation is 30–50% of securities tokenisation's value**. Issuers have weaker incentive to build infrastructure.

### Barrier 3: Regulatory Heterogeneity
Each RWA class is regulated differently:
- **Real estate**: County/state land-title law (US); freehold vs leasehold distinctions (UK); civil-law property regimes (France, Germany)
- **Trade finance**: UCP 600 (uniform trade finance rules) + national banking law + shipping law
- **Carbon credits**: Voluntary carbon market standards (ICVCM, VCMI, Verra, Gold Standard) + national climate policy

No single institution (like the SEC for securities) governs all RWA classes. This means **each RWA category must navigate multiple regulators**. A carbon-credit issuer must comply with Verra rules, national climate ministries, and financial regulators (if the credit is sold to institutions). This divergence slows standardisation.

### Barrier 4: Custody Concentration Risk
For tokenised RWA, the on-chain token is only as trustworthy as the **off-chain custodian** (the entity holding the asset in the registry). If the custodian is a single bank or SPV, it is a **counterparty risk**. If the custodian defaults, token holders may lose the asset (or fight in court for recovery).

Tokenised securities have the same problem, but **institutional custody has matured over decades**: Fidelity, BNY Mellon, State Street custody procedures are audited, insured, and regulated. RWA custody is nascent—no institutional-grade, insurance-backed, audited RWA custody exists yet.

---

## Market-by-Market Comparison

| Factor | Tokenised Securities | Tokenised RWA |
|---|---|---|
| **Current market size** | USD 11B (treasuries) + USD 5B (bonds/funds) = USD 16B | USD 1–2B (estimated) |
| **Time to significant scale** | 18–24 months (USD 100B+) | 5–7 years (USD 10B+) |
| **Primary beneficiary** | Retail investors (24/7 access), institutions (cost reduction) | Asset owners (fractional ownership), retail access |
| **Regulatory clarity** | High (existing securities law applies) | Low (RWA-specific rules emerging) |
| **Custody infrastructure** | Mature (Fidelity, Kraken, Coinbase) | Nascent (building 2026–2027) |
| **Liquidity clustering** | Ethereum + 2–3 secondary chains | Fragmented across 10+ chains |
| **Settlement efficiency gains** | High (T+2 → T+0 = 1–2% cost savings) | Low (velocity irrelevant; RWA gains are 0.5–1%) |
| **Legal interface complexity** | Low (database → blockchain UI) | High (on-chain token ↔ off-chain registry) |
| **Regulatory bottleneck** | None (SEC guidance sufficient) | Multiple (land registry, climate ministry, financial regulators) |

---

## Why This Divergence Matters for the RWA Market Thesis

The Standard Chartered/Synpulse projection of **USD 30.1 trillion by 2034** is anchored on:
1. USD 8.5 trillion of tokenised securities (securities are smaller AUM but grow faster)
2. USD 16 trillion of tokenised real-world assets (RWA is larger AUM but grows slowly)
3. USD 5.6 trillion of stablecoins and other crypto-assets

**But the 2026–2027 trajectory is inverting**: tokenised securities are growing at 40% CAGR (doubling every 18–24 months), while tokenised RWA (real estate, trade finance) are growing at 10–15% CAGR (doubling every 5–7 years).

This means:
- **By 2028**, tokenised securities will be USD 50–100 billion (mature market for institutional treasuries and funds)
- **By 2028**, tokenised RWA will still be USD 10–20 billion (early pilots and niche use cases)

The "RWA boom" is real, but it is a **2028–2032 story**, not a 2026 story. Institutions betting on 2026 RWA tokenisation returns will be disappointed.

---

## Next Actions

1. **Build a tokenised-securities liquidity tracker**: Monitor daily volume across BUIDL, USDC, tokenised bonds, tokenised funds on Ethereum, Polygon, Arbitrum, and EU DLT Pilot networks. Quantify bid-ask spreads and market depth per chain. This data will inform institutional deployment decisions.

2. **Commission a real-estate custody feasibility study**: What would it cost to build institutional-grade, insurance-backed custody for tokenised-REIT tokens holding property deeds in all 50 US states? Model the build cost and ongoing operational cost per property.

3. **Survey institutional appetite for tokenised RWA**: Conduct a survey of pension funds, insurance companies, and asset managers on which RWA classes they would tokenise if legal and custodial barriers were removed (real estate, trade finance, infrastructure, carbon, commodities). Prioritise by demand.

4. **Quantify the on-chain ↔ off-ledger reconciliation cost**: For each RWA class, estimate the annual cost of maintaining two ledgers (on-chain token + off-chain registry) in sync, including legal opinions, custody overhead, and registry updates. Benchmark against the cost savings from tokenisation.

5. **Model adoption curves by asset class**:
   - Tokenised treasuries: 40% CAGR, USD 500B by 2030 (mature)
   - Tokenised bonds: 25% CAGR, USD 50B by 2030 (growing)
   - Tokenised funds: 30% CAGR, USD 200B by 2030 (fast-growing)
   - Tokenised real estate: 12% CAGR, USD 10B by 2030 (early stage)
   - Tokenised trade finance: 15% CAGR, USD 5B by 2030 (pilot phase)
   - Tokenised carbon: 18% CAGR, USD 1B by 2030 (niche)
