---
type: synthesis
date: 2026-06-30
tags:
- synthesis
- legal-frameworks
- property-law
- private-law
- convergence
- UNIDROIT
- UCC
- UK
related-sources:
- UNIDROIT Principles on Digital Assets and Private Law
- UK Property (Digital Assets etc) Act 2025
- UCC Article 12 — Controllable Electronic Records
- UKJT Legal Statement on Control of Digital Assets 2023
- Academic — Tokenisation of Absolute Rights and Claims
- US Morgan Lewis Tokenization of Securities
- EU MiCA Regulation 2023/1114
topic:
- topic/law/property-rights
- topic/law/digital-assets
wiki_indexed: '2026-07-12T00:00:00Z'
wiki_hash: 20b5ab444868d7321c13ff2da7f268c1b2f05f7fe40b3da4949a6eb824539c74
wiki_role: wiki
---


# Synthesis — Private Law Convergence Across Jurisdictions

For future Claude: Three major jurisdictions (US, UK, EU) have independently converged on functionally identical property-law frameworks for tokenised assets—but through divergent doctrinal paths. The US adopted UCC Article 12 (controllable electronic records), the UK created a third category of personal property, and the EU aligned around UNIDROIT Principles and MiCA. All three treat the token as the asset-holder's property right, not as a mere representation. This convergence is significant because it solves the most fundamental legal uncertainty: can a token *be* the asset, or does it only *represent* an off-ledger asset?

---

## The Core Question: Is a Token the Asset or a Representation?

The foundational legal challenge is whether ownership of a token **is** ownership of the underlying right (direct tokenisation) or whether the token is merely **evidence** of ownership held in a traditional registry (indirect tokenisation).

This distinction matters for:
- **Priority and secured transactions**: Can a tokenised asset be pledged as collateral? If the token is just evidence, lenders must perfect security in the off-ledger asset, not the token.
- **Insolvency and bankruptcy**: If a custodian holding token-representing-bonds goes bankrupt, are token holders protected? Only if the token *is* the bond, not merely a wrapper.
- **Cross-border enforceability**: If a US court recognises the token as property but a Swiss court treats it as a mere representation, which law governs settlement disputes?

---

## The Three Converging Frameworks

### Framework 1: United States — UCC Article 12 (2022)
The [[10_Sources/Law-Regulation/UCC-Article-12-Controllable-Electronic-Records.md|2022 Amendments to the Uniform Commercial Code, Article 12]], adopted by 26 US states and pending in others, introduces a new property category: **controllable electronic records (CERs)**.

**Key architecture**:
- A CER is personal property (not a contract or a claim)
- Title passes by transfer of *control* (ability to electronically register a transaction; right to exclude others)
- Secured-transaction rules for CERs mirror those for accounts receivable (Article 9)
- A token *is* the CER; no underlying off-ledger asset is required (though one may exist)

**Legal consequence**: A token on Ethereum representing a bond *is* the bond for Article 12 purposes. A lender can perfect security by taking control of the token's private key. Insolvency law treats tokenised assets as property of the token holder, not the issuer—a custodian bankruptcy does not automatically extinguish token holders' rights.

**Scope**: Article 12 applies to any electronic record that is controllable (ability to register, ability to exclude). It is indifferent to whether the record is on-chain or in a centralised ledger.

---

### Framework 2: United Kingdom — Property (Digital Assets etc) Act 2025
The [[10_Sources/Law-Regulation/UK-Property-Digital-Assets-Act-2025.md|Property (Digital Assets etc) Act 2025]], which received Royal Assent in 2025, creates a **third category of personal property** between *things in possession* (chattels, tangible goods) and *things in action* (intangible rights like debts and copyrights).

**Key architecture**:
- Digital assets (including tokens) are personal property of a new type
- The Act does not define the new category in detail; courts will develop its contours case-by-case
- The [[10_Sources/Law-Regulation/UKJT-Control-of-Digital-Assets.md|UKJT 2023 Legal Statement on Control]] provides interpretive guidance: a party has *control* of a digital asset if they can transfer it and exclude others
- Secured transactions on digital assets follow common-law pledge and charge doctrines

**Legal consequence**: A token held in a UK-regulated custody account *is* personal property of the token holder, not a claim against the custodian. A bankruptcy of the custodian does not extinguish the token holder's property rights (contrast with cash, which a bank holds as a debtor-creditor relationship).

**Scope**: The new category accommodates crypto, tokens, NFTs, and any digital asset capable of transfer and exclusion. Like Article 12, it is indifferent to the underlying ledger (blockchain, centralised database, hybrid).

---

### Framework 3: European Union — UNIDROIT Principles and MiCA
The [[10_Sources/International-Agencies/UNIDROIT-Principles-Digital-Assets.md|UNIDROIT Principles on Digital Assets and Private Law (2023)]] and the [[10_Sources/Law-Regulation/EU-MiCA-Regulation.md|Markets in Crypto-Assets Regulation (2023)]], in full effect from 30 December 2024, take a convergent approach:

**Key architecture (UNIDROIT)**:
- Principle 2: Digital assets are **capable of being property** under private law
- Principle 3: Persons holding digital assets are **entitled to operate and dispose** of them (owner rights)
- Principles 4–19: Extended rules on transfer, custody, secured transactions, insolvency, and choice of law
- Principle 7: A custodian holding digital assets does so in *custodian capacity*, not as debtor—distinguishing tokenised assets from traditional deposits

**Key architecture (MiCA)**:
- MiCA does not harmonise the property question (left to member states), but it does mandate that **token issuers and service providers disclose asset custody arrangements**
- Tokenised securities and tokenised deposits remain under MiFID II and CRR/CRD banking rules, not MiCA
- MiCA applies to stablecoins and other crypto-assets; token-issuer transparency is required

**Legal consequence**: Under UNIDROIT and MiCA, a tokenised euro stablecoin issuer must disclose that the underlying euros are held in a custodian bank, but the token holder's property right in the token *itself* is recognised. If a MiCA-compliant stablecoin issuer's custodian fails, token holders can claim against the issuer's reserve assets before general creditors—because the token is property, not a debt.

---

## The Convergence Pattern

All three frameworks share three critical moves:

1. **Tokens are property, not contracts or claims**. This is the direct tokenisation assertion: ownership of a token = ownership of the right.

2. **Control (ability to transfer + ability to exclude) is the operative criterion**, not possession or custody. This accommodates both on-chain tokens (controlled via private key) and off-chain digital records (controlled via registered-owner mechanisms).

3. **Custodians are fiduciaries, not debtors**. A custodian holding a token acts in trust, not as a creditor. This separates the token holder's property rights from the custodian's bankruptcy estate.

**These moves are functionally identical across the US, UK, and EU**, despite using different doctrinal language (CERs, third category, UNIDROIT principles).

---

## Key Doctrinal Differences (Layered on Convergence)

### US: Secured-Transaction Focus
Article 12 is most developed on **secured transactions** (pledges, mortgages). The framework integrates tokens seamlessly into Article 9 priority rules. A bank taking a security interest in a CER can perfect that interest by taking control—no separate litigation risk.

### UK: Possession and Exclusion
The UKJT 2023 Statement emphasises **exclusion** as the legal marker of ownership. A token holder owns the asset if they can exclude others—a common-law concept familiar to English courts. This grounds tokenisation in centuries of property doctrine.

### EU: Regulatory Transparency and Reserve Requirements
MiCA layers **regulatory disclosure duties** on top of private-law property rights. A stablecoin issuer must hold reserves equal to the stablecoin circulation, disclose the custodian, and undergo regular attestations. This is supplementary to UNIDROIT private-law property rights, not a replacement.

---

## Remaining Uncertainties

### Uncertainty 1: Cross-Border Recognition
If a US court treats a token as an Article 12 CER and awards judgment, will a Swiss court enforce that judgment? MiCA provides some EU-internal consistency, but UNIDROIT Principles are *not binding* in most jurisdictions; they are persuasive guidance only. [[10_Sources/Law-Regulation/HCCH-UNIDROIT-Digital-Assets-Private-International-Law.md|HCCH and UNIDROIT ongoing work]] on private-international-law questions may eventually harmonise enforcement, but it is not yet complete.

### Uncertainty 2: Direct vs Indirect Tokenisation (Civil Law)
[[10_Sources/Law-Regulation/Tokenisation-Absolute-Rights-Claims.md|Academic analysis of direct vs indirect tokenisation]] notes that civil-law traditions (France, Germany, many EU member states) have historically required tokens to represent *absolute rights* (rights that inhere in the token itself) rather than *relative rights* (contractual claims). A tokenised bond might represent an absolute right (ownership of the bond certificate) but not a relative right (a bank's contractual obligation to pay). This distinction does not exist in common-law or UCC frameworks. The UNIDROIT Principles finesse this by not taking a civil-law vs common-law stance, but individual EU member states may diverge in implementation.

### Uncertainty 3: Bankruptcy-Code Carve-Outs
Neither Article 12, the UK Property Act, nor UNIDROIT Principles are automatically applied in bankruptcy proceedings. A custodian's bankruptcy trustee may argue that tokenised assets in the custodian's control should be *estate property* (so the trustee can liquidate them and distribute proceeds to all creditors) rather than *segregated property* (belonging to the token holder, excluded from the estate). [[10_Sources/Law-Regulation/UCC-Article-12-Bankruptcy-Implications.md|Bankruptcy-court treatment]] of Article 12 CERs is not yet fully developed; expect litigation 2026–2028.

---

## Evidence of Convergence in Practice

### Pilot 1: UK DIGIT (Digital Gilt Issuance Trial)
The UK Treasury and [[10_Sources/Commercial-Banks/HSBC-Orion.md|HSBC Orion]] are issuing tokenised gilts (UK government bonds) on HSBC's blockchain. The tokens are treated as personal property under the [[10_Sources/Law-Regulation/UK-Property-Digital-Assets-Act-2025.md|Property (Digital Assets etc) Act 2025]]. Legal opinions have confirmed that token holders own the gilt, not merely a claim against HSBC.

### Pilot 2: Tokenised JPMorgan Deposits (Kinexys)
[[10_Sources/Commercial-Banks/JPMorgan-Kinexys.md|JPMorgan Kinexys]] issues tokenised dollar deposits on-chain. US legal opinions treat these as Article 12 CERs—the token *is* the deposit, not a wrapper around it. Lenders can perfect security interests in the tokens without reference to JPMorgan's balance sheet.

### Pilot 3: Tokenised Carbon Credits (Verra / Gold Standard)
[[10_Sources/Law-Regulation/Verra-Immobilisation.md|Verra and Gold Standard]] have shifted to *immobilisation* models where the registry remains the legal source of truth, but on-chain tokens track beneficial ownership. The tokens do not *represent* the credit—they *are* the credit, held in a custodian's account at Verra. This hybrid model respects both on-chain property recognition and registry-based legal certainty.

---

## Implications for RWA Tokenisation

The convergence of US, UK, and EU property law creates a **three-jurisdiction baseline** where tokens are recognised as property across all major financial centres:

1. **Secured lending on tokenised assets** becomes friction-free. A bank can take a security interest in a tokenised real-estate fund token, a tokenised corporate bond, or a tokenised carbon credit, using the token itself as collateral (not requiring a separate pledge of the off-ledger asset).

2. **Cross-border custody** becomes legally simpler. A UK pension fund holding a US-issued tokenised asset (e.g., BlackRock BUIDL) has property rights under both UCC Article 12 (US) and the Property Act (UK); a US custodian cannot argue away the token holder's property status based on regulatory fragmentation.

3. **Insolvency protection** is materially improved. A custodian bankruptcy does not automatically seize tokenised assets held by third parties; the tokens remain property of the token holders.

4. **Secondary-market liquidity** is enabled. Because tokens are property, they can be freely pledged, mortgaged, and traded without requiring the issuer's consent or off-ledger permission.

---

## Next Actions

1. **Commission a bankruptcy-law analysis**: Article 12 CERs, UK digital assets, and UNIDROIT custodian principles have not been fully tested in bankruptcy court. Model a hypothetical tokenised-asset custodian insolvency (USD 10 billion AUM, holding 100 different tokenised instruments) and estimate token holders' recovery probability under US, UK, and EU law.

2. **Track HCCH–UNIDROIT private-international-law work** on digital assets (ongoing). When final principles are published (expected 2026–2027), assess whether they provide sufficient guidance on enforcement of cross-border tokenised-asset ownership.

3. **Audit civil-law member-state implementations** of MiCA and UNIDROIT Principles. If France or Germany issue guidance treating tokenised assets as relative (not absolute) rights, this breaks the convergence at the implementation layer.

4. **Monitor UK courts** for early cases interpreting the Property (Digital Assets etc) Act 2025. The first year (2025–2026) of case law will clarify whether courts treat the new property category narrowly (only on-chain tokens) or broadly (any controllable digital record).

5. **Prepare secured-transaction precedent library**: As more banks take security interests in tokenised assets (Kinexys collateral, BUIDL pledges), documenting Article 12 / Property Act / MiCA secured-transaction filings will become essential for institutional counsel.
