---
type: synthesis
date: 2026-06-30
tags:
- synthesis
- carbon-credits
- tokenisation
- test-bed
- market-structure
- voluntary-markets
related-sources:
- Verra Immobilisation Policy 2022
- Gold Standard Consent Framework
- Ballesteros-Rodriguez et al. KlimaDAO empirical study 2024
- Tlili et al. 2025 blockchain carbon markets efficiency study
- JPMorgan Carbon Markets Reimagined 2024
- Rocky Mountain Institute Beyond the Buzz 2022
- ICVCM Core Carbon Principles
- VCMI Claims Code of Practice
- AirCarbon Exchange (Singapore)
- Climate Impact X (CIX) exchange
topic:
- topic/carbon-credits
- topic/tokenisation
wiki_indexed: '2026-07-12T00:00:00Z'
wiki_hash: 79162da9fe05b1c4e5316146df43785e0968208273df05d817ef17b9cdc22ec1
wiki_role: wiki
---


# Synthesis — Carbon Credits as Tokenisation Test Bed

For future Claude: Tokenised carbon credits have become the **test bed for RWA tokenisation architecture**. The voluntary carbon market (USD 6–7 billion annually, growing 15–20% per annum) is smaller than securities markets but large enough to justify infrastructure investment. Unlike real estate (which requires jurisdictional land registries) or trade finance (which requires interbank consensus), carbon credits are governed by a small number of registries (Verra, Gold Standard, Article 6 registries) with aligned incentives to modernise. The market-structure inflection point was [[10_Sources/Law-Regulation/Verra-Immobilisation-Policy.md|Verra's 2022 suspension of third-party tokenisation]] and shift to *immobilisation*: registry retains custody; on-chain tokens track beneficial ownership. This model is now the industry standard and provides a replicable template for other RWA classes (real estate, trade finance, commodities).

---

## The Voluntary Carbon Market Structure

The voluntary carbon market (VCM) is smaller and more concentrated than compliance carbon markets (ETS, cap-and-trade):

**Market size and participants**:
- Annual credit issuance: USD 2–3 billion (2023–2024 estimates)
- Total credits in circulation: USD 6–7 billion AUM equivalent
- Major registries: Verra (60% market share), Gold Standard (20%), Article 6 (15–20% forward), smaller registries (<5%)
- Credit-generating projects: Conservation (REDD+, forest protection) 60%, renewable energy 20%, methane capture 10%, other 10%

**Credit lifecycle**:
1. **Issuance**: Project developer (conservation org, clean energy company) generates a credit by meeting a registry's additionality, leakage, and permanence criteria
2. **Transfer**: Registry transfers the credit to an account holder (investor, trader, corporate buyer)
3. **Retirement**: Corporate or individual retires the credit to offset emissions; credit is removed from circulation

**Traditional friction points**:
- **Transfer speed**: Verra and Gold Standard batch credit transfers; settlement takes 3–14 days
- **Fractional ownership**: Credits are typically traded whole; fractional holdings require contractual arrangements outside the registry
- **Secondary-market liquidity**: No centralised order book; price discovery happens over-the-counter via intermediaries
- **Credit quality tracking**: Buyers cannot easily verify credit quality on secondary market; fraud risk elevated

---

## The Market-Structure Inflection: Verra and Gold Standard Shift to Immobilisation

### The Crisis: Third-Party Tokenisation (2021–2022)

Early tokenisation platforms (Toucan Protocol, KlimaDAO, Flowcarbon) took a direct approach: they **withdrew credits from Verra** into custody, then issued tokens representing those credits on Ethereum. This meant:

**Advantages**:
- 24/7 token trading (Ethereum is always open)
- Fractional ownership (tokens are divisible; Toucan's BCT and NCT pools aggregate many credits)
- Lower transfer friction (token trades settle in minutes, not days)

**Risks**:
- **Custody risk**: Credits held in third-party custody outside Verra; if the custody provider defaults, credits are at risk
- **Registry divergence**: Credits held off-registry cannot be retired directly; token holders must send credits back to Verra to retire, adding friction
- **Fraud risk**: Tokens could be issued without corresponding credits; no real-time verification possible

### The Response: Verra and Gold Standard Pause and Pivot (2022–2023)

In May 2022, [[10_Sources/Law-Regulation/Verra-Immobilisation-Policy.md|Verra suspended third-party tokenisation]] of credits in its registry. The policy shift:

1. **No more bulk withdrawals**: Third-party platforms cannot withdraw large batches of credits
2. **Immobilisation model**: Credits *remain* in Verra's registry under an immobilisation account; tokens on Ethereum track beneficial ownership but do not represent custody
3. **Consent framework**: [[10_Sources/Law-Regulation/Gold-Standard-Consent-Framework.md|Gold Standard implemented a formal consent framework]]: projects and credit holders can explicitly authorise tokenisation; tokens are issued only with consent

**Implication**: Tokenisation becomes a **double-ledger system**:
- **On-chain (Ethereum, Polygon)**: Tokens trade 24/7; fractional ownership; secondary-market liquidity
- **Off-chain (Verra registry)**: Credits remain immobilised; beneficial ownership tracked via registry account transfer; retirement must go through registry

This is a **permanent fragmentation** of the carbon-credit market: you can trade the token without touching the registry, or retire the credit by going through the registry, but you cannot do both simultaneously.

---

## Tokenised Carbon Architecture and Its Evidence Base

### Architecture: Immobilised Credits with On-Chain Tracking

[[10_Sources/Commercial-Banks/JPMorgan-Carbon-Markets-Reimagined.md|JPMorgan's "Carbon Markets Reimagined" (2024)]] and [[10_Sources/Industry-Press/AirCarbon-Exchange.md|AirCarbon Exchange documentation]] outline the now-standard architecture:

1. **Project issues credit**: Developer generates credit in Verra; credit immobilised in Verra's custody
2. **Tokenisation event**: A platform (AirCarbon, Climate Impact X, JPMorgan) registers the immobilised credit with Verra and issues a corresponding token on Ethereum or Polygon
3. **Token trading**: Token trades 24/7 on secondary markets (DEXs, CEXs); price discovery happens on-chain
4. **Retirement pathway**: Token holder can:
   - **Retire on-chain**: Return token to originating platform; platform initiates retirement through Verra (slow, 3–7 day path)
   - **Hold indefinitely**: Token remains a perpetual claim on the immobilised credit (rarely used; most tokens are eventually retired)

**Key design feature**: The token and the credit are **permanently linked** but **not identical**. The token is a liquid claim; the credit is an immobilised asset.

### Empirical Evidence: Fragmentation and Efficiency Gains

#### Study 1: Ballesteros-Rodriguez et al. (2024) — KlimaDAO Empirical Evidence
[[10_Sources/Academia/Ballesteros-Rodriguez-KlimaDAO.md|This empirical study]] of KlimaDAO (Toucan Protocol's largest user) documents:

**Efficiency gains**:
- **Transfer time**: Traditional Verra transfer 3–14 days → Token trade 2 minutes
- **Counterparty friction**: Verra registry access limited to regulated intermediaries → Ethereum accessible to any account holder
- **Fractional entry**: Minimum traditional credit USD 5–25 (whole credit) → Token minimum USD 1–5 (fractional via BCT/NCT pools)

**Costs and friction**:
- **Redemption fee**: Toucan charges 2–5% fee to redemption (arbitrage opportunity for liquidity providers; cost to token holders who want to retire)
- **Bridge risk**: To retire a Polygon-based token, holder must bridge to Ethereum-based Verra interface; bridge costs 0.5–2%
- **Market fragmentation**: Toucan's BCT pool (base carbon) aggregates many projects; quality heterogeneity means pool price does not reflect individual credit quality
- **Custody concentration**: Toucan holds credits in a single Verra account; Toucan insolvency would risk all pooled credits

#### Study 2: Tlili et al. (2025) — Market Efficiency on Blockchain vs Traditional
[[10_Sources/Academia/Tlili-Carbon-Markets-Efficiency.md|This 2025 study]], using 2020–2023 data, applied a difference-in-differences approach to compare price discovery on Toucan Protocol (on-chain) vs traditional OTC markets:

**Finding**: On-chain tokenised credits have **faster price discovery** (information reflected in price 30% faster than OTC) but **higher price volatility** (standard deviation 40% higher than OTC).

**Interpretation**:
- Tokenisation reduces information asymmetry (24/7 market access means more traders have access to information)
- Tokenisation increases volatility (retail and algorithmic traders amplify price swings; no circuit breakers or position limits)

**Net effect**: Liquidity improvement for sophisticated traders (lower bid-ask spreads), but **not for unsophisticated retail traders** (higher volatility = higher losses in drawdowns).

---

## The Registry-Token Interface Problem (Still Unsolved)

The immobilisation model solves the **custody problem** (credits stay at Verra) but creates a **permanence problem**: tokens and credits can never fully merge. The reason:

**Verra is a registry, not a ledger**. It records *which accounts own which credits*, but it does not track *on-chain token transfers*. When you trade a Toucan BCT token on Uniswap (a Polygon-based DEX), Verra's registry does not update. The registry only updates when:
1. You initiate a redemption request through Toucan
2. Toucan submits the redemption to Verra
3. Verra deducts the credit from the immobilised account (3–7 days later)

This creates a **settlement risk window**: During the 3–7 days between token redemption and registry settlement, the token holder is technically not the legal owner of the credit. They are instead a creditor of Toucan, relying on Toucan's solvency.

[[10_Sources/Commercial-Banks/JPMorgan-Carbon-Markets-Reimagined.md|JPMorgan's analysis]] notes that this friction is acceptable for *trading* (most tokens are held for days, not years) but problematic for *retirement* (a corporate buying tokens to offset next year's emissions must plan 3–7 days ahead of the redemption date).

---

## Platforms Competing in the Immobilised Model

Three competing platforms have emerged with the immobilisation model:

### Platform 1: AirCarbon Exchange (Singapore and Abu Dhabi)
- **Model**: Tokenised credits issued on a permissioned (not public-blockchain) network
- **Participants**: DBS, Singapore Exchange (SGX) investors; ADGM-regulated Abu Dhabi investors
- **Regulation**: Licensed under Singapore MAS and UAE VARA frameworks
- **Custody**: AirCarbon holds credits in Verra immobilised accounts; AirCarbon is the custodian
- **Adoption**: Estimated USD 50–100 million in tokenised credits (small but growing)
- **Advantage**: Regulatory clarity (MAS and VARA oversight); disadvantage: illiquid (limited to Singapore and Abu Dhabi participants)

### Platform 2: Climate Impact X (Singapore)
- **Model**: Hybrid—Polygon-based tokens (public blockchain) with Singapore registry backing
- **Participants**: DBS, SGX, Standard Chartered, Temasek; focus on institutional/corporate buyers
- **Regulation**: MAS oversight via CIX as a designated trading venue
- **Custody**: CIX holds credits; tokens are backed 1:1 by immobilised Verra or Gold Standard credits
- **Adoption**: Estimated USD 100–200 million in tokenised credits
- **Advantage**: Scale (Polygon liquidity) + regulatory clarity (MAS backing); disadvantage: Singapore-centric

### Platform 3: Toucan Protocol and KlimaDAO (Public Ethereum and Polygon)
- **Model**: Public blockchain (Ethereum, Polygon); permissionless token trading
- **Participants**: Retail, traders, DAOs, some institutions
- **Regulation**: Minimal (self-regulated via DAO governance)
- **Custody**: Toucan holds credits; tokens are pooled (BCT, NCT) representing many projects
- **Adoption**: Estimated USD 50–100 million in tokenised credits (peaked 2021–2022; declining 2023–2024 amid market skepticism)
- **Advantage**: Permissionless (any account can trade); disadvantage: custody risk (Toucan is a single-purpose company with regulatory uncertainty)

---

## Why Carbon Credits are the Ideal Test Bed for RWA Tokenisation

### Reason 1: Aligned Incentives at Registry Level
Verra and Gold Standard **benefit** from tokenisation: it increases credit liquidity, attracts retail capital, and drives down credit acquisition costs for large buyers. Unlike real-estate registries (which benefit from opacity and local control) or trade-finance systems (which benefit from bank intermediation), carbon registries are **open-access** (any project can apply) and **transparent** (credits are public).

### Reason 2: Credible Quality Standards Exist
[[10_Sources/Law-Regulation/ICVCM-Core-Carbon-Principles.md|ICVCM Core Carbon Principles]] and [[10_Sources/Law-Regulation/VCMI-Claims-Code.md|VCMI Claims Code]] provide objective quality benchmarks. A tokenised carbon credit can be labelled "Core Carbon Principle compliant" or "VCMI Approved," and institutional buyers know what they are getting. Real estate has no equivalent global quality standard.

### Reason 3: Settlement is Simple Relative to Other RWA
A carbon credit is pure data: a registry entry + a serial number. When you transfer a credit, nothing physical moves. Contrast this with real estate (must update a land deed) or trade finance (must coordinate shipping documents, insurance, payment). Carbon credits are the **simplest RWA to tokenise** because they are already digital at the source (Verra is a database).

### Reason 4: Market Capitalization is Manageable (Not Too Big, Not Too Small)
USD 6–7 billion AUM is large enough to justify infrastructure build (Toucan, CIX, AirCarbon all had USD 20–50 million development budgets) but small enough that a single technology failure does not threaten systemic financial stability. By contrast, USD 11 billion tokenised treasuries is large enough to be systemic; USD 0.1 billion tokenised real estate is too small to justify development cost.

---

## Lessons from Carbon Tokenisation Applicable to Other RWA Classes

### Lesson 1: Registries Are Permanent; Full Merging of On-Chain and Off-Chain is Infeasible

The immobilisation model succeeded because it **accepted registry permanence**. Early platforms tried to *replace* Verra with on-chain smart contracts; this failed because Verra has regulatory authority (only Verra can issue a credit) that no blockchain can claim.

**Application to real estate**: Land registries (county recorders, UK Land Registry, Singapore Land Authority) are permanent institutions. Real-estate tokenisation *must* accept registry permanence and design for **dual-ledger settlement** (token on blockchain, deed at registry) rather than trying to replace the registry.

### Lesson 2: Custody at Platform or Registry, Not Distributed

Toucan Protocol initially explored distributed custody (users holding credits directly in Verra); this was rejected for complexity. Modern platforms use **centralised platform custody** (AirCarbon, CIX) or **registry-based custody** (Toucan immobilisation). No successful model relies on distributed custody (tokens as direct Verra account credentials).

**Application to other RWA**: Institutions will not trust distributed custody for valuable assets. Expect successful RWA tokenisation platforms to operate centralised custody desks (like traditional asset managers) backed by insurance and audit.

### Lesson 3: Regulatory Sponsorship Accelerates Adoption

AirCarbon (MAS-backed) and CIX (MAS and SGX-backed) are growing faster than permissionless Toucan (no regulatory sponsor). Institutions trust regulatory signals more than technology signals.

**Application to other RWA**: Asset classes with regulatory sponsorship (central banks, securities regulators) will tokenise faster than those without. Real estate will tokenise fastest in jurisdictions with regulatory interest (Singapore, UAE, Hong Kong), not in jurisdictions treating it as an unregulated crypto experiment.

### Lesson 4: Quality Heterogeneity Demands Pooling or Segmentation

Early carbon-credit tokenisation tried to tokenise individual credits; this fragmented liquidity and made price discovery hard (each credit has different additionality and permanence risk). Modern platforms use **pooling** (Toucan BCT aggregates many credits into a single token class) or **segmentation** (AirCarbon categorises credits by project type and vintage).

**Application to other RWA**: Tokenisation of heterogeneous asset classes (real estate with different locations/yields, private credit with different credit quality) must pool or segment to achieve liquidity. A "tokenised real-estate fund" will have more liquidity than "tokenised Denver apartment + tokenised Austin condo" as separate tokens.

---

## Open Questions and 2026–2027 Milestones

### Question 1: Will Immobilisation Permanently Fragment Liquidity?

If tokens and credits can never fully merge, token holders are permanently separated from registry-level voting and credit-issuance rights. This fragments governance: Verra controls credit quality; token traders control price. Will this lead to persistent arbitrage or regulatory consolidation?

**2026–2027 milestone**: Monitor whether token prices (Toucan BCT, AirCarbon, CIX) converge to or diverge from underlying credit prices at Verra. Large divergences (>10%) indicate liquidity fragmentation; small divergences (<2%) indicate efficient arbitrage.

### Question 2: Can Permissioned Models (AirCarbon, CIX) Scale Beyond Singapore and Abu Dhabi?

Current platforms are geographically concentrated. If they expand to Europe or North America, will they maintain regulatory sponsorship or become freestanding companies?

**2026–2027 milestone**: Track AirCarbon and CIX expansion announcements (new jurisdictions, new regulatory partnerships). If neither expands by end-2027, permissioned platforms may be capacity-constrained.

### Question 3: Will Retail Tokenised-Carbon Investment Remain Niche?

Tlili et al. (2025) documented that on-chain tokenisation increases volatility for retail. Will retail stay interested, or will volatility drive retail out and leave tokenisation to sophisticated traders?

**2026–2027 milestone**: Monitor Toucan Protocol and KlimaDAO's retail transaction volume. If it declines post-volatility, expect permissioned platforms (AirCarbon, CIX) to capture institutional demand while Toucan captures niche trader demand.

---

## Next Actions

1. **Commission a registry-integration roadmap**: What would it cost for Verra or Gold Standard to integrate on-chain tokens into their registry-settlement workflow? Model a scenario where token redemptions settle within 1 day (instead of 3–7 days) via blockchain oracle confirmation of credit quantity.

2. **Benchmark AirCarbon and CIX against Toucan**: Compare custody costs, platform fees, liquidity (bid-ask spreads), and redemption times. If permissioned platforms are >20% cheaper than permissionless, expect rapid consolidation.

3. **Analyse Article 6 (Paris Agreement) carbon credit tokenisation**: Article 6 enables internationally transferred mitigation outcomes (ITMOs) that are counted toward national climate targets. Tokenising Article 6 credits is more complex than VCM credits (requires international registry coordination). Model the legal and custodial complexity.

4. **Track institutional buyer demand**: Survey asset managers and corporates on their willingness to hold tokenised carbon vs traditional credits. Quantify the premium they will pay for fractional ownership, 24/7 trading, and lower entry cost.

5. **Design a replicability study**: For each other RWA class (real estate, trade finance, commodities, infrastructure), document which elements of the carbon-token model are replicable and which are unique to carbon. This informs the 2027–2028 tokenisation pipeline.
