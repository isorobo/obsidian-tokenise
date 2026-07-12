---
type: synthesis
date: 2026-06-30
tags:
- synthesis
- stablecoins
- architecture
- USDC
- USDT
- RWA-stablecoins
- CBDC
related-sources:
- US GENIUS Act 2025 (Comprehensive)
- US Anti-CBDC Surveillance State Act 2025
- BIS Stablecoins vs Tokenised Deposits
- BIS WP1280 CBDC and Banks Disintermediation
- IMF Tokenization and Financial Market Inefficiencies
- Circle USDC Transparency Reports
- Tether USDT Attestation Reports
- McKinsey Blockchain Currencies Beyond Stablecoins 2025
- Transak RWA Stablecoins
- LCX Stablecoins and RWA
- WEPIN RWA Stablecoins and Wallet-as-Service
- BIS Aldasoro et al. Stablecoins and Safe Asset Prices
topic:
- topic/finance/stablecoins
- topic/tokenisation
wiki_indexed: '2026-07-12T00:00:00Z'
wiki_hash: e348c696d52e53542064ab083298c4839b925eaca61c592eeea217d7e7ce3568
wiki_role: wiki
---


# Synthesis — Stablecoin Architecture Evolution

For future Claude: Stablecoin architecture is evolving through three distinct generations, driven by regulatory pressure and institutional demand. **Generation 1** (2018–2023): unregulated reserve-backed stablecoins (USDT, USDC) issuing on multiple chains with minimal reserve transparency. **Generation 2** (2024–2026): bank-issued stablecoins (JPM Coin) and regulated e-money tokens (SocGen EURCV under MiCA), with mandatory reserve audits and regulatory oversight. **Generation 3** (2026–2027+): real-world-asset-backed stablecoins (RWA stablecoins backed by tokenised treasuries or money-market funds), combining stablecoin velocity with RWA yields. Each generation increases regulatory compliance burden and decreases volatility risk, but also reduces issuance velocity and increases cost.

---

## Generation 1: Unregulated Reserve-Backed Stablecoins (2018–2023)

### Market Leaders: USDT and USDC

**USDT (Tether)**:
- Issuer: Tether (BVI company; no bank charter)
- Reserve model: Stated as 1:1 backed by USD, commercial paper, and other liquid assets
- Reserve visibility: Quarterly attestation reports (not full audits; attestations provide limited assurance)
- Adoption: Largest stablecoin by volume (USD 120+ billion circulation; January 2026)
- Regulatory status: Largely unregulated; operate under regulatory grey area in most jurisdictions
- Multi-chain: Ethereum, TRON, Polygon, Avalanche, Solana, and others (8+ chains)

**USDC (Circle)**:
- Issuer: Circle Internet Financial (licensed money transmitter in US; e-money regulated in EU)
- Reserve model: Explicitly 1:1 backed by USD in bank accounts and short-dated US Treasuries
- Reserve visibility: Monthly transparency reports (full disclosure of reserves and backing assets)
- Adoption: Second-largest stablecoin by volume (USD 30+ billion circulation; June 2026)
- Regulatory status: Ahead of regulation (seeking full banking charter in US; MiCA-compliant in EU)
- Multi-chain: Ethereum, Polygon, Arbitrum, Optimism, Avalanche, Solana (6+ chains)

### Characteristics of Generation 1

**Advantages**:
- Permissionless issuance (non-bank issuers like Tether can enter market without bank charter)
- 24/7 settlement (blockchains operate round-the-clock)
- Low transaction costs (on-chain settlement costs USD 0.5–5, far below wire transfer fees of USD 25–50)

**Vulnerabilities**:
- Custody risk: Reserves are held in custodian banks and money-market funds; if custodian fails, stablecoin holders face risk
- Reserve quality risk: Assets backing stablecoins (particularly USDT's commercial paper holdings) may be lower quality than USD deposits at a central bank
- Run risk: If confidence in reserve adequacy erodes, all stablecoin holders simultaneously attempt to exit; redemption queue moves slowly
- Regulatory uncertainty: [[10_Sources/Supervisory-Bodies/FSB-Crypto-Asset-Activities.md|FSB 2023]] and subsequent regulation (GENIUS Act 2025) explicitly address run risk and reserve requirements

### Reserve Composition Evolution

**USDT reserves (Q1 2026 attestation)**:
- USD cash: 33%
- US Treasury securities: 18%
- Commercial paper: 30%
- Corporate bonds: 12%
- Other: 7%

**USDC reserves (June 2026 monthly transparency report)**:
- USD cash: 65%
- US Treasury bills (<3 month maturity): 35%
- Loan loss reserves: -3% (over-collateralised)

**Key divergence**: USDC holds 100% cash + short-dated Treasuries (highest quality); USDT holds commercial paper (credit risk). This explains investor preference for USDC among institutional holders.

---

## Generation 2: Bank-Issued and Regulated Stablecoins (2024–2026)

### Market Leaders: JPM Coin, SocGen EURCV, PayPal USD

**JPM Coin**:
- Issuer: JPMorgan Chase Bank (systemically important bank; regulatory oversight from Fed, OCC)
- Reserve model: Fully backed by JPMorgan deposits held at Federal Reserve
- Use case: Tokenised settlement of JPMorgan commercial-bank deposits on JPMorgan Kinexys network
- Circulation: Estimated USD 1–5 billion (not publicly disclosed; confined to JPMorgan's network and partners)
- Regulatory status: Operates under banking license; no additional regulation required (banking rules apply)
- Multi-chain: Kinexys network (permissioned); Ethereum pilot (minimal adoption)

**SocGen EURCV (2024)**:
- Issuer: Société Générale Bank (French megabank; ECB oversight)
- Reserve model: 1:1 backed by euros in SocGen custodial accounts
- Use case: Euro-denominated settlement; MiCA-compliant payment stablecoin
- Circulation: Estimated EUR 10–50 million (nascent; launched 2024)
- Regulatory status: MiCA-compliant; regulated under Payment Services Directive
- Multi-chain: Ethereum-based (Polygon bridge planned)

**PayPal USD (2024)**:
- Issuer: Paxos (payments firm; New York State-licensed virtual asset service provider)
- Reserve model: Deposits held at Metropolitan Bank (NYC-based; FDIC-insured)
- Use case: Integration into PayPal consumer payments ecosystem
- Circulation: Estimated USD 50–200 million (growing; early adoption)
- Regulatory status: PayPal is regulated; Paxos is regulated by NYDFS
- Multi-chain: Ethereum-based; integration with PayPal Venmo planned

**Operational model**: PayPal USD differs from JPM Coin and SocGen EURCV by targeting mainstream consumers rather than institutional settlement. The architecture separates concerns: Paxos holds regulatory and issuance responsibility; Metropolitan Bank holds reserves; PayPal manages the consumer interface. Consumer flow: USD deposit → PayPal calls Paxos to mint PYUSD backed by reserve → token settles on Ethereum (~15 seconds) → user can hold in PayPal wallet, transfer to another PayPal user, or withdraw to external wallet. Redemption reverses: user requests withdrawal → Paxos burns PYUSD → PayPal releases USD. Strategic intent: replace Venmo's ACH settlement (1–3 days) with on-chain settlement (15 seconds); allow users to exit to self-custody without forcing centralised vault; monetise on conversion spreads rather than interest margin. Why this model matters: bridges traditional payments (users never see blockchain) and blockchain settlement (auditability, redemption guarantee, exit option). Adoption depends on PayPal/Venmo network effects; circulation still small (USD 50–200M vs USDC's USD 30B) but growing.

### Why Bank-Issued Stablecoins Are Gaining

1. **Regulatory clarity**: Banks are already regulated; stablecoin issuance requires no new regulatory framework (just application of existing banking rules)
2. **Reserve certainty**: JPMorgan and SocGen are systemically important banks; their deposits are implicitly backed by central banks
3. **Trust**: Institutional investors trust established banks more than crypto-native companies (Tether, Circle)
4. **Cost of capital**: Banks can borrow cheaply; they can back stablecoins with low-cost funding, reducing issuance cost

### Generation 2 Characteristics

**Advantages**:
- Regulatory clarity (operates under banking rules; no legal uncertainty)
- Explicit central-bank backing (banks' reserves are implicitly guaranteed by central banks)
- Integration with legacy banking (JPM Coin settles on JPMorgan's own ledger; no custody intermediary)

**Limitations**:
- Walled garden (JPM Coin does not freely transfer to competitors' networks; Kinexys ecosystem is permissioned)
- No true multi-chain (each bank-issued stablecoin is confined to its own network or a few permissioned partners)
- Higher issuance cost (banks must maintain regulatory capital against stablecoin liabilities; this cost is passed through in reduced yields to stablecoin holders)

---

## Generation 3: Real-World-Asset-Backed Stablecoins (2026–2027+)

[[10_Sources/Commercial-Banks/Transak-RWA-Stablecoins.md|Transak]], [[10_Sources/Commercial-Banks/LCX-RWA-Stablecoins.md|LCX]], and [[10_Sources/Commercial-Banks/WEPIN-RWA-Stablecoins.md|WEPIN]] are pioneering a new category: **stablecoins backed by tokenised real-world assets** rather than bank deposits or commercial paper.

### Architecture: RWA Stablecoin Backed by Tokenised Treasuries

**Issuance structure**:
1. Issue USDC or a fiat-backed stablecoin (USD 100 million equivalent)
2. Use proceeds to purchase tokenised US Treasury bills (e.g., BlackRock BUIDL: USD 100 million)
3. Issue a new stablecoin (e.g., "Yield-Backed USDC") backed 1:1 by the tokenised Treasuries
4. Distribute newly issued stablecoin to liquidity providers or end-users

**Value proposition**:
- Stablecoin maintains price stability (backed by Treasuries)
- Stablecoin generates yield (Treasuries earn ~5% annually)
- Yield is passed to stablecoin holders (e.g., as increased purchasing power over time, or as direct dividend)

**Example**: A user holds USD 100,000 in Yield-Backed USDC backed by tokenised Treasury bills. Over one year, the Treasuries earn USD 5,000 in interest. That interest is either:
1. Reinvested into more Treasuries (user's balance grows to USD 105,000), or
2. Paid out monthly (user receives USD 417/month in additional stablecoin)

### Generation 3 Players

**Transak**:
- Focuses on RWA stablecoins backed by tokenised money-market funds
- Custody at institutional grade (e.g., Fidelity for RWA holdings)
- Multi-chain deployment (Ethereum, Polygon, Solana)
- Use case: Asset managers wanting to offer yield-bearing stablecoins to retail

**LCX**:
- Stablecoin protocol focused on settlement of tokenised RWA transactions
- Partners with institutional issuers (BlackRock, Franklin Templeton) to create collateral pools
- Custody at LCX or delegated to Fidelity/Kraken
- Use case: Institutions wanting to create bespoke stablecoins for specific investor bases

**WEPIN**:
- Wallet-as-a-service (WaaS) platform enabling RWA stablecoins
- Focuses on on-ramp/off-ramp (converting fiat to RWA stablecoins)
- Partners with PayPal and other payment processors
- Use case: Consumer-facing integration of RWA stablecoins into payments

### Generation 3 Characteristics

**Advantages**:
- Yield-bearing (stablecoin holders earn Treasuries' yield)
- Capital efficiency (instead of holding idle USD in a bank, USD is invested in Treasuries)
- Regulatory clarity (backed by Treasuries, which are securities under existing law)

**Limitations**:
- Complexity (RWA stablecoins are 3–4 layers deep: fiat → bank deposit → tokenised Treasuries → stablecoin)
- Duration risk (if tokenised Treasury interest rates decline, RWA stablecoin issuers earn less; must either reduce yield or absorb losses)
- Custody risk (now depends on both the institution holding the Treasuries and the institution holding the tokenised version)

---

## The Macro Trend: Central Bank Displacement

### BIS and IMF Perspective: Stablecoins as Substitutes for Money

[[10_Sources/International-Agencies/BIS-Stablecoins-vs-Tokenised-Deposits.md|BIS "Stablecoins versus Tokenised Deposits"]] frames the regulatory choice:

**Choice A: Non-Bank Stablecoins**
- USDT, USDC, third-party issuers
- Fastest to scale; permissionless entry
- Systemic risk: If stablecoin market reaches USD 1 trillion, a run could trigger financial crisis
- Central bank response: Regulation to force reserve backing and custody; essentially, force stablecoins to become bank deposits

**Choice B: Tokenised Bank Deposits (Unified Ledger)**
- JPM Coin, tokenised central-bank money, CBDC
- Slower to scale; requires central-bank coordination
- Systemic risk: Lower (central banks control settlement; no run risk)
- Regulatory preference: Most central banks prefer this (Project Agorá, EnsembleTX, eHKD all follow this path)

### Regulatory Inflection: GENIUS Act + Anti-CBDC Act Reshape the Market

**Simultaneous Legislation (July 2025)**:

**[[10_Sources/Law-Regulation/US-GENIUS-Act-2025-Comprehensive.md|GENIUS Act]]** effectively **ended Generation 1 stablecoins** in the US and mandates Generation 2:
- All permitted payment stablecoins must maintain 1:1 reserves in USD or Treasury bills
- Reserves must be held at Federal Reserve member bank or eligible custodian
- Issuers must be "permitted payment stablecoin issuers" (three categories: bank subsidiaries, federal qualified nonbanks, state qualified)
- Non-approved stablecoins (USDT if Tether is not approved as foreign issuer) face Federal Reserve enforcement

**[[10_Sources/Law-Regulation/US-Anti-CBDC-Surveillance-State-Act-2025.md|Anti-CBDC Surveillance State Act]]** **prohibits the Federal Reserve from issuing any CBDC**, ensuring that digital money evolution proceeds via private stablecoins, not government-issued digital currency:
- Federal Reserve prohibited from issuing, testing, developing, or implementing any CBDC
- Retail CBDC explicitly banned (privacy concerns)
- Wholesale CBDC barred unless Congress grants separate authorisation
- Preserves banking system by preventing Fed competition for retail deposits

**Combined effect**: U.S. monetary system will evolve via private bank-issued stablecoins and regulated e-money providers (JPM Coin, USDC), NOT Fed CBDC.

**Impact on incumbents**:
- **USDC (Circle)**: Likely approved (already compliant with GENIUS Act)
- **USDT (Tether)**: Uncertain (regulatory questions; if not approved, USDT trading in US faces legal uncertainty)
- **JPM Coin**: Automatically compliant (bank-issued)
- **Other stablecoins**: Only approved stablecoins can legally settle in the US post-2027

### The Actual Three-Tier Future (2027–2028): Private Stablecoins + Bank Deposits, Not CBDC

*Note: Original SVG diagram placeholder. Diagram title should reflect "Private Stablecoin + Bank-Deposit Tiers" not CBDC-inclusive architecture.*

**Tier 1: CBDC (Central-Bank Digital Currency)** — RESTRICTED IN US
- Issuer: Federal Reserve, ECB (EU), central banks in other jurisdictions
- Settlement: Central bank infrastructure (most secure, most regulated)
- **US Status**: [[10_Sources/Law-Regulation/US-Anti-CBDC-Surveillance-State-Act-2025.md|Retail CBDC prohibited by Anti-CBDC Act (2025)]]; wholesale CBDC requires Congressional authorisation (not currently granted)
- **Global Timeline (non-US)**: eEURO pilot (EU); wholesale pilots in Singapore, Hong Kong, Japan; no official U.S. Fed launch date announced post-prohibition
- Adoption: Unlikely in U.S. (retail prohibited); potential wholesale pilots in other jurisdictions

**Tier 2: Tokenised Bank Deposits (Unified Ledger)**
- Issuer: JPMorgan, BNY Mellon, European banks (regulated banks)
- Settlement: Private or consortium networks (Project Agorá, Kinexys, EnsembleTX)
- Timeline: Already operating (JPM Coin 2024+; Project Guardian pilots 2025+)
- Adoption: Fast-growing for institutional settlement (expected USD 100B+ AUM by 2028)

**Tier 3: Regulated Stablecoins (USDC, EURCV)**
- Issuer: Licensed money transmitters or e-money firms
- Settlement: Public blockchains (Ethereum, Solana, Polygon)
- Timeline: Already operating; GENIUS Act compliance required by 2027
- Adoption: Retail focus; institutional use declining as Tier 1 and 2 scale

**Tier 4: Unregulated/Non-Compliant Stablecoins (USDT if rejected, smaller projects)**
- Status post-2027: Likely relegated to jurisdictions outside US/EU regulatory reach
- Adoption: Emerging markets, offshore trading, regulatory arbitrage

---

## Impact on RWA Tokenisation and Settlement

The stablecoin architecture evolution has direct implications for RWA scaling:

### Path A: CBDC + Unified Ledger (Central-Bank Preference)
- Central banks issue CBDC and operate unified ledger (Project Agorá model)
- RWA issuers tokenise on the unified ledger and settle in CBDC
- Advantage: Single settlement layer; no bridge risk; central-bank oversight
- Timeline: 2027–2030 (CBDCs mature; unified ledgers operationalise)
- Winners: Institutions compliant with central-bank requirements

### Path B: Public Blockchain + Regulated Stablecoin (Market Preference)
- Institutions continue to issue on Ethereum using Circle USDC or bank-issued stablecoins
- RWA settles via stablecoin rails (USDC, JPM Coin)
- Advantage: Existing infrastructure (Ethereum mature); no central-bank intermediation
- Timeline: Immediate (already live; scaling 2026–2027)
- Winners: Tech-native issuers; permissionless platforms

### Path C: Convergence (Most Likely Post-2028)
- CBDCs and public-blockchain stablecoins interoperate via bridges
- Large institutions use CBDC (for settlement certainty); tech-native institutions use public-blockchain stablecoins (for speed)
- Central banks regulate bridge protocols to manage systemic risk
- Timeline: 2028–2030

---

## Market Size Projections

| Tier | 2026 AUM | 2028 AUM (projected) | 2030 AUM (projected) | Annual growth rate |
|---|---|---|---|---|
| USDT | USD 120B | USD 180B | USD 250B | 13% CAGR |
| USDC | USD 30B | USD 80B | USD 150B | 52% CAGR |
| JPM Coin + other bank stablecoins | USD 5B | USD 50B | USD 200B | 100% CAGR |
| RWA stablecoins | USD 0.1B | USD 5B | USD 50B | 220% CAGR (from tiny base) |
| CBDC (wholesale) | USD 0 | USD 100B | USD 500B | ∞ (from zero) |
| **Total stablecoin circulation** | **USD 155B** | **USD 415B** | **USD 1.15T** | **44% CAGR** |

**Observations**:
- USDT growth slows as regulatory pressure increases; USDC accelerates
- Bank-issued stablecoins (JPM Coin, SocGen EURCV) grow fastest as regulatory clarity increases
- RWA stablecoins are niche (0.1–5% of market) until 2028–2029; then accelerate as Treasuries tokenisation scales
- CBDC enters the market post-2027; by 2030, wholesale CBDC may rival private stablecoins for institutional settlement

---

## Next Actions

1. **Monitor GENIUS Act implementation** (Fed expected to release implementing regulations Q3–Q4 2026). Clarify which non-bank issuers will be approved; forecast USDT regulatory outcome.

2. **Quantify reserve composition risk** across USDT, USDC, JPM Coin. If USDT's commercial paper holdings deteriorate (credit spreads widen), does that signal run risk? Model a 2008-style liquidity crisis scenario.

3. **Benchmark Generation 2 vs Generation 3 stablecoins**: Which is faster growing? USDC (Gen 2) or emerging RWA stablecoins (Gen 3)? Track adoption curves to predict which architecture wins by 2030.

4. **Commission a CBDC interoperability study**: When the Fed launches its wholesale CBDC (2027–2028), how will it interact with USDC, JPM Coin, and permissioned networks like Kinexys? Build integration scenarios.

5. **Prepare institutional deployment roadmap**: For an asset manager wanting to issue tokenised securities by 2028, should it use Ethereum + USDC (Path B), or wait for CBDC + unified ledger (Path A)? Model decision tree based on regulatory certainty and settlement speed.
