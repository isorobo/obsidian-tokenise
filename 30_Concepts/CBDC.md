---
title: "Central bank digital currency (CBDC)"
name: Central bank digital currency
slug: CBDC
type: concept
domain: [finance]
synonyms: [central bank digital currency, retail CBDC, wholesale CBDC, digital euro (instance), e-HKD (instance)]
related_concepts: ["[[Stablecoin]]", "[[Tokenised-Deposit]]", "[[Singleness-of-Money]]", "[[Programmable-Money]]", "[[Unified-Ledger]]", "[[Atomic-Settlement]]"]
tags: [concept, cbdc]
status: draft
created: 2026-10-27
---

> **For future Claude.** This note pulls together the vault's CBDC sources (IMF FinTech Notes 2025, BIS Working Paper 1280, ECB blogs and remarks, HKMA releases, the US Anti-CBDC bill note, and reports on Project Agorá and Project Pontes) into one concept entry. It separates retail from wholesale CBDC, records each stated purpose and risk against the source that states it, and uses tables where sources differ. Every claim links to a vault source note; points not confirmed in the vault are marked [V#] and listed under Verification.

# Central bank digital currency (CBDC)

> **Definition.** A CBDC is central bank money in digital form, issued as a liability of the central bank, either for use by the general public (retail) or restricted to licensed financial institutions (wholesale) ([[IMF-FTN-2025-003-Private-Law-Token-CBDC]]; [[IMF-FTN-2025-011-Central-Bank-Tokenized-Reserves]]).

## Why it matters

CBDC is the public-sector form of digital money against which the vault's stablecoin and tokenised-deposit material is compared. The ECB presents a retail digital euro as public money that protects banks from stablecoin and mobile-payment encroachment ([[Ledger-Insights-ECB-Cipollone-Digital-Euro-Stablecoin-Shield]]). The IMF presents wholesale tokenised reserves as a way to keep risk-free settlement in central bank money within tokenised markets ([[IMF-FTN-2025-011-Central-Bank-Tokenized-Reserves]]). The HKMA moved its e-HKD work from retail to wholesale after pilot users treated e-HKD and tokenised bank deposits as interchangeable ([[hkma-ehkd-pilot-programme-complete-2025]]). A US bill would bar the Federal Reserve from issuing any CBDC ([[US-Anti-CBDC-Surveillance-State-Act-2025]]). The concept therefore links the [[MOC - CBDC]], [[MOC - Stablecoins]] and [[MOC - Monetary-Hierarchy]] threads.

## Retail and wholesale

The vault's instrument enum separates `cbdc-retail` and `cbdc-wholesale` (`99_Meta/schema.md` section 2.9). The sources split along the same line, but define the terms in different ways.

| Source | Scope | How the source defines or frames CBDC |
|---|---|---|
| [[IMF-FTN-2025-003-Private-Law-Token-CBDC]] (IMF, March 2025) | Retail, token-based | The monetary claim on the central bank is incorporated in a digital token; transfer of the token is transfer of the claim, with no current-account relationship between central bank and holder. "In contrast to account-based CBDC, token-based CBDC would legally truly represent a 'new form of money.'" The legal concept of a token is distinguished from the technological one. |
| [[IMF-FTN-2025-006-Selected-Legal-CBDC]] (IMF, November 2025) | Retail (rCBDC) | Retail CBDC must be legal tender under domestic monetary law; the central bank needs a statutory mandate both to issue it and to operate the payment platform. Distinguishes an "asset link" model (users hold a direct legal claim on the central bank) from a "technological link" model (they do not). |
| [[IMF-FTN-2025-011-Central-Bank-Tokenized-Reserves]] (IMF, November 2025) | Wholesale | Prefers "tokenised reserves" to "wholesale CBDC" because only the settlement technology changes; the instrument remains a direct central bank liability available only to licensed financial institutions. The vault tags this note `cbdc-wholesale`. |
| [[ECB-Blog-2025-Digital-Euro-for-Digital-Age]] (ECB, December 2025) | Retail (digital euro) | Framed against cash: euro cash exists only as banknotes and coins, and "the digital euro is designed to complement, not replace, cash." |
| [[Ledger-Insights-ECB-Project-Pontes-Go-Live]] (Ledger Insights, August 2026) | Wholesale (Eurosystem) | "Tokenised central bank money" for settling DLT transactions, in two models: cash tokens on the Eurosystem's DLT, and a trigger model that starts conventional TARGET payments from DLT instructions. |
| [[hkma-ehkd-pilot-programme-complete-2025]] and [[HKMA-HKEX-eHKD-Derivatives-Margin-Pilot-2026]] (HKMA, 2025 and 2026) | Both (e-HKD) | Retail e-HKD deprioritised; wholesale e-HKD described as operating 24/7 for real-time margin payments. |
| [[US-Anti-CBDC-Surveillance-State-Act-2025]] (US bill, 2025) | Both | The quoted bill text covers "a central bank digital currency or any digital asset that is substantially similar to a central bank digital currency under any name or label"; the vault note reads it as covering retail and wholesale use. |

**Token-based and account-based.** Only [[IMF-FTN-2025-003-Private-Law-Token-CBDC]] draws this distinction directly. It treats token-based CBDC as legally novel and says existing private-law categories (tangible, intangible, hybrid) do not map cleanly onto it. The Pontes "cash token" and "trigger" models ([[Ledger-Insights-ECB-Project-Pontes-Go-Live]]) are a different settlement-design choice; the source does not describe them as token-based or account-based.

**Wholesale in practice (as reported).**

- Project Pontes: ECB targeted production go-live on 21 September 2026, with testing from early August 2026; both models keep settlement in central bank money (as of 4 August 2026, [[Ledger-Insights-ECB-Project-Pontes-Go-Live]]). Go-live not confirmed in the vault [V3].
- Project Agorá: first real-money results, with 22 financial institutions and five central banks running 30 transactions worth about CHF 800,000 across six currencies, average settlement about 80 seconds; the platform was not connected to central bank settlement systems, and the project "remains experimental with no commitment to move into production" (as of 30 July 2026, [[Ledger-Insights-BIS-Project-Agora-Real-Money-Trials]]).
- HKEX and HKMA: pilot of wholesale e-HKD for advance margin payments in derivatives After-Hours Trading, removing the current 3pm cut-off; real-value trials are optional and subject to regulatory approval and market readiness (as of 18 June 2026, [[HKMA-HKEX-eHKD-Derivatives-Margin-Pilot-2026]]).
- Federal Reserve staff paper: the IMF cross-border (XC) platform concept would settle trades using tokenised, escrowed central bank reserves; the paper takes no position on any proposal and questions whether programmable shared-ledger settlement removes counterparty risk or relocates it (February 2026, [[FEDS-2026-011-Contrasting-Ledgers-Interbank-Payment-Systems]]).

## Stated purposes and risks

### Stated purposes

| Purpose stated | Source | Scope |
|---|---|---|
| Complement cash in digital form; free, simple, inclusive, accepted across the euro area, usable online and offline | [[ECB-Blog-2025-Digital-Euro-for-Digital-Age]] | Retail |
| Strategic autonomy in payments, monetary sovereignty and inclusion; in 13 of 21 euro area countries in-store payments depend entirely on international card schemes or mobile solutions | [[ECB-Blog-2026-Digital-Euro-Opportunity-for-Banks]] | Retail |
| Protect banks' deposits and fee income from stablecoins and mobile payments | [[Ledger-Insights-ECB-Cipollone-Digital-Euro-Stablecoin-Shield]] | Retail |
| Preserve the safety, liquidity and policy role of central bank money in tokenised markets; risk-free, atomic settlement | [[IMF-FTN-2025-011-Central-Bank-Tokenized-Reserves]] | Wholesale |
| Settle DLT transactions in central bank money rather than commercial bank money or stablecoins | [[Ledger-Insights-ECB-Project-Pontes-Go-Live]] | Wholesale |
| Improve wholesale cross-border payments | [[Ledger-Insights-BIS-Project-Agora-Real-Money-Trials]] | Wholesale |
| Tokenised asset settlement, programmability and offline payments (Phase 2 pilot themes); wholesale and cross-border payments | [[hkma-ehkd-pilot-programme-complete-2025]] | Both |
| Expand payment choice and act as a platform on which intermediaries can compete | [[IMF-FTN-2025-007-CBDC-Payments-Competition]] | Retail |
| Payment resilience, including offline capability, redundancy and interoperability | [[IMF-FTN-2025-009-Payment-Resilience-Fragile-States-CBDC]]; [[IMF-FTN-2025-008-CBDC-Financial-Stability]] | Retail |

### Financial stability and bank disintermediation

The sources differ on how large the risk is and whether design can contain it.

| Source | Position stated | Mitigation named |
|---|---|---|
| [[BIS-WP1280-CBDC-Banks-Disintermediation]] (July 2025) | "Introducing a retail CBDC might reduce financial stability because CBDC offers storage-at-scale." German household survey data show slow deposit substitution in normal times and faster withdrawals in stress. | Holding limits, which the paper finds reduce fragility while keeping some monetary benefits. |
| [[IMF-FTN-2025-008-CBDC-Financial-Stability]] (November 2025) | Effects through bank funding and lending, run risk and payment resilience can be negative or positive; size and direction depend on country, adoption and design. | Appropriate design and safeguards; combine existing estimates with country-specific modelling. |
| [[ECB-Blog-2026-Digital-Euro-Opportunity-for-Banks]] (March 2026) | "The digital euro clearly does not put bank liquidity positions and financial stability at risk." | No remuneration, a reverse waterfall, holding limits for individuals, and no holdings for corporates. |
| [[Ledger-Insights-ECB-Cipollone-Digital-Euro-Stablecoin-Shield]] (July 2026) | No-interest design and holding limits are intended to limit deposit flight. | Same design features. |
| [[US-Anti-CBDC-Surveillance-State-Act-2025]] | The vault note attributes to the legislative record a concern that households would move deposits into a retail CBDC in a crisis. | Statutory prohibition. |

[[IMF-FTN-2025-007-CBDC-Payments-Competition]] also lists holding limits among the issues policymakers should settle, alongside intermediary participation rules, fee structures and interoperability.

### Privacy and financial integrity

- The IMF finds that retail CBDC features can materially affect how well a jurisdiction's AML/CFT regime works, that some current designs may strain international AML/CFT standards, and that several issues should be settled before launch; it calls parts of its analysis preliminary because real-world use is limited (November 2025, [[IMF-FTN-2025-Financial-Integrity-Retail-CBDC]]).
- A two-tier model needs clear legal rules on intermediaries' obligations, including AML/CFT compliance ([[IMF-FTN-2025-006-Selected-Legal-CBDC]]).
- The vault note on the US bill records the sponsors' stated concerns: transaction-level visibility by the central bank, Fourth Amendment privacy, and programmable features such as expiry, purchase restrictions, automatic negative rates and unilateral freezing ([[US-Anti-CBDC-Surveillance-State-Act-2025]]). These are attributed to sponsor statements and committee testimony, not to the bill text.

Programmability is framed differently across sources:

| Source | Framing of programmability |
|---|---|
| [[hkma-ehkd-pilot-programme-complete-2025]] | A Phase 2 pilot theme; the HKMA said it would release a standardised token framework for programmable digital money. |
| [[IMF-FTN-2025-011-Central-Bank-Tokenized-Reserves]] | Programmable or automated liquidity management is a possible enhancement that may need updates to governance, legal frameworks and risk management. |
| [[US-Anti-CBDC-Surveillance-State-Act-2025]] | A stated concern of sponsors; the quoted bill text bars the FOMC from using a CBDC to implement monetary policy. |

### Payments competition

- CBDC's competitive effect depends on the existing payments landscape, regulation and design; gains may be larger in less competitive markets and smaller, mainly through wider access, in more competitive ones (November 2025, [[IMF-FTN-2025-007-CBDC-Payments-Competition]]).
- Mandatory intermediary participation and compulsory wallet portability raise competition-law and administrative-law questions, and the central bank's dual role as platform operator and regulator raises possible conflicts of interest ([[IMF-FTN-2025-006-Selected-Legal-CBDC]]).
- The ECB has said both that "the digital euro will not compete with private means of payment" ([[ECB-Blog-2025-Digital-Euro-for-Digital-Age]]) and that it would counter reliance on international card schemes and stablecoins ([[ECB-Blog-2026-Digital-Euro-Opportunity-for-Banks]]; [[Ledger-Insights-ECB-Cipollone-Digital-Euro-Stablecoin-Shield]]). The Eurosystem will not charge scheme or processing fees, and estimated total bank investment costs at EUR 4 billion to EUR 5.8 billion (as of March 2026, [[ECB-Blog-2026-Digital-Euro-Opportunity-for-Banks]]).

### Legal and operational

- Most jurisdictions would need law reform on property, insolvency and conflict of laws; holders must keep a direct claim on the central bank if an intermediary fails, or token-based CBDC "would not be risk-free central bank money"; the IMF proposes that the governing law follow the jurisdiction of the CBDC platform ([[IMF-FTN-2025-003-Private-Law-Token-CBDC]]).
- No single legal template suits all jurisdictions ([[IMF-FTN-2025-006-Selected-Legal-CBDC]]).
- Payment continuity needs work across connectivity, infrastructure, intermediaries, payment solutions and user access; for CBDC the IMF suggests offline capability, redundancy and interoperability with existing and private systems ([[IMF-FTN-2025-009-Payment-Resilience-Fragile-States-CBDC]]).

## Relation to stablecoins and tokenised deposits

| Source | How CBDC is placed against stablecoins or tokenised deposits |
|---|---|
| [[Ledger-Insights-ECB-Cipollone-Digital-Euro-Stablecoin-Shield]] | Digital euro as public money that "does not serve any single private interest"; "a euro is a euro wherever it is spent." Stablecoins and mobile payments are described as reducing banks' transaction visibility and fee income. (On the "a euro is a euro" point, see [[Singleness-of-Money]]; the source does not use that term.) |
| [[ECB-Blog-2025-Digital-Euro-for-Digital-Age]] | "The digital euro will not compete with private means of payment." |
| [[hkma-ehkd-pilot-programme-complete-2025]] | Pilot users regarded e-HKD and tokenised bank deposits as interchangeable; the HKMA turned near-term work to wholesale and cross-border use. |
| [[IMF-FTN-2025-011-Central-Bank-Tokenized-Reserves]] | Tokenised reserves sit alongside alternatives (RTGS links, omnibus accounts, privately issued tokenised money); each has trade-offs and no single option dominates. |
| [[Ledger-Insights-ECB-Project-Pontes-Go-Live]] | Both Pontes models keep settlement in central bank money rather than commercial bank money or stablecoins. |
| [[Ledger-Insights-BIS-Project-Agora-Real-Money-Trials]] | The real-money trials were tokenised deposit transactions within a BIS project involving five central banks. |
| [[FEDS-2026-011-Contrasting-Ledgers-Interbank-Payment-Systems]] | The Regulated Liability Network would put central bank, commercial bank and regulated nonbank money on one ledger with a partition per issuer; the BIS [[Unified-Ledger]] concept would add other financial assets on one programmable platform. |
| [[US-Anti-CBDC-Surveillance-State-Act-2025]] | The vault note sets the bill beside the GENIUS Act's regime for payment stablecoins and, in its own analysis rather than the bill text, expects US digital money to develop through private stablecoins and bank deposits. |

See also [[Stablecoin]] and [[Tokenised-Deposit]].

## Jurisdictions

- **EU.** Digital euro (retail) legislation sits in the Commission's 2023 Single Currency Package; the ECB aims to be ready by 2029 if co-legislators adopt the regulation in 2026 (as of December 2025, [[ECB-Blog-2025-Digital-Euro-for-Digital-Age]]); standards were expected by summer 2026 and a pilot in 2027 (as of March 2026, [[ECB-Blog-2026-Digital-Euro-Opportunity-for-Banks]]). Wholesale: Project Pontes ([[Ledger-Insights-ECB-Project-Pontes-Go-Live]]).
- **US.** H.R. 1919 and S.1124 would prohibit the Federal Reserve from issuing, testing or developing a CBDC; the vault note records House passage on 2 July 2025 by 219 to 210 [V1] and the Senate bill as pending (as of mid-2026) [V2] ([[US-Anti-CBDC-Surveillance-State-Act-2025]]). The Federal Reserve did not take part in the Agorá real-money phase (as of July 2026, [[Ledger-Insights-BIS-Project-Agora-Real-Money-Trials]]).
- **HK.** Retail e-HKD deprioritised in October 2025, with preparatory work for any future retail expansion targeted for mid-2026 [V4] ([[hkma-ehkd-pilot-programme-complete-2025]]); wholesale e-HKD margin pilot with HKEX (as of June 2026, [[HKMA-HKEX-eHKD-Derivatives-Margin-Pilot-2026]]).
- **Agorá central banks (UK, France, Japan, Korea, Switzerland).** Bank of England, Bank of France, Bank of Japan, Bank of Korea and Swiss National Bank took part in the real-money phase (as of July 2026, [[Ledger-Insights-BIS-Project-Agora-Real-Money-Trials]]).
- **Canada and Denmark.** Both let their central bank money settle on ledgers the central bank does not operate (as of February 2026, [[FEDS-2026-011-Contrasting-Ledgers-Interbank-Payment-Systems]]).
- **Fragile and conflict-affected states.** Payment-resilience lessons for CBDC design are drawn from Ukraine, West Bank and Gaza, Haiti, the CEMAC region, Tuvalu, Sudan and Yemen; these are payment cases, not CBDC deployments ([[IMF-FTN-2025-009-Payment-Resilience-Fragile-States-CBDC]]).

## Open points

- **Direct claim or not.** [[IMF-FTN-2025-003-Private-Law-Token-CBDC]] says the law must ensure token-based CBDC holders always have a direct claim on the central bank, while [[IMF-FTN-2025-006-Selected-Legal-CBDC]] describes a "technological link" design in which users have no direct legal claim. Whether such a design still meets the definition above is not settled in the vault.
- **Terminology.** [[IMF-FTN-2025-011-Central-Bank-Tokenized-Reserves]] prefers "tokenised reserves" to "wholesale CBDC"; the vault's enum uses `cbdc-wholesale` for both.
- **US bill note consistency.** [[US-Anti-CBDC-Surveillance-State-Act-2025]] describes the bill and the GENIUS Act as "passed simultaneously in July 2025" and the bill as a statutory ban, while also recording the Senate bill as pending. It says the bill prohibits wholesale CBDC, but also reports readings that a future, separately authorised wholesale CBDC could be permitted. Its comparative tables on China, Switzerland, Singapore and the UK carry no primary citations and are not relied on here.
- **Agorá and central bank money.** The report describes tokenised deposit transactions on a platform not connected to central bank settlement systems ([[Ledger-Insights-BIS-Project-Agora-Real-Money-Trials]]); the vault does not show what role central bank money played in these trials.
- **IMF channel count.** [[IMF-FTN-2025-008-CBDC-Financial-Stability]] refers to six transmission channels but lists five.
- **Coverage gaps.** No Bank of England digital pound material and no Federal Reserve retail CBDC position beyond the bill (as at 27 October 2026, [[MOC - CBDC]]).
- **Source types.** Pontes, Agorá and the Cipollone remarks reach the vault through Ledger Insights reporting, not primary ECB or BIS text.

## Sources

- [[IMF-FTN-2025-003-Private-Law-Token-CBDC]]: IMF FinTech Note 2025/003, 14 March 2025. https://www.imf.org/en/publications/fintech-notes/issues/2025/03/14/private-law-aspects-of-token-based-central-bank-digital-currencies-565165
- [[IMF-FTN-2025-006-Selected-Legal-CBDC]]: IMF FinTech Note 2025/006, 5 November 2025. https://www.imf.org/en/publications/fintech-notes/issues/2025/11/05/selected-legal-considerations-for-central-bank-digital-currencies
- [[IMF-FTN-2025-007-CBDC-Payments-Competition]]: IMF FinTech Note, 11 November 2025. https://www.imf.org/en/publications/fintech-notes/issues/2025/11/11/the-impact-of-central-bank-digital-currency-on-payments-competition-571638
- [[IMF-FTN-2025-008-CBDC-Financial-Stability]]: IMF FinTech Note 2025/008, 12 November 2025. https://www.imf.org/en/publications/fintech-notes/issues/2025/11/12/evaluating-the-implications-of-cbdc-for-financial-stability-571743
- [[IMF-FTN-2025-009-Payment-Resilience-Fragile-States-CBDC]]: IMF FinTech Note 2025/009, 12 November 2025. https://www.imf.org/en/publications/fintech-notes/issues/2025/11/12/payment-resilience-in-fragile-and-conflict-affected-states-lessons-for-central-bank-571748
- [[IMF-FTN-2025-011-Central-Bank-Tokenized-Reserves]]: IMF FinTech Note 2025/011, 18 November 2025. https://www.imf.org/en/publications/fintech-notes/issues/2025/11/18/central-bank-exploration-of-tokenized-reserves-571876
- [[IMF-FTN-2025-Financial-Integrity-Retail-CBDC]]: IMF FinTech Note, 14 November 2025. https://www.imf.org/en/publications/fintech-notes/issues/2025/11/14/financial-integrity-implications-of-retail-central-bank-digital-currencies-rcbdcs-571769
- [[BIS-WP1280-CBDC-Banks-Disintermediation]]: BIS Working Paper 1280, 8 July 2025. https://www.bis.org/publ/work1280.htm
- [[ECB-Blog-2025-Digital-Euro-for-Digital-Age]]: ECB Blog, 9 December 2025. https://www.ecb.europa.eu/press/blog/date/2025/html/ecb.blog20251209~9ba130ff20.en.html
- [[ECB-Blog-2026-Digital-Euro-Opportunity-for-Banks]]: ECB Blog, 27 March 2026. https://www.ecb.europa.eu/press/blog/date/2026/html/ecb.blog20260327~51b0640c39.en.html
- [[Ledger-Insights-ECB-Cipollone-Digital-Euro-Stablecoin-Shield]]: Ledger Insights, 20 July 2026 (secondary report of ECB remarks). https://www.ledgerinsights.com/ecbs-cipollone-argues-digital-euro-will-shield-banks-from-stablecoin-encroachment/
- [[Ledger-Insights-ECB-Project-Pontes-Go-Live]]: Ledger Insights, 4 August 2026 (secondary). https://www.ledgerinsights.com/ecb-targets-21-september-go-live-for-project-pontes-a-primer-on-tokenized-central-bank-money/
- [[Ledger-Insights-BIS-Project-Agora-Real-Money-Trials]]: Ledger Insights, 30 July 2026 (secondary). https://www.ledgerinsights.com/project-agora-starts-live-trials-lloyds-participates-in-3-tokenized-deposit-transactions/
- [[hkma-ehkd-pilot-programme-complete-2025]]: HKMA press release, 28 October 2025. https://www.hkma.gov.hk/eng/news-and-media/press-releases/2025/10/20251028-4/
- [[HKMA-HKEX-eHKD-Derivatives-Margin-Pilot-2026]]: HKMA and HKEX press release, 18 June 2026. https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/06/20260618-8/
- [[US-Anti-CBDC-Surveillance-State-Act-2025]]: US bill H.R. 1919 and S.1124, vault note with analysis. https://www.congress.gov/bill/119th-congress/house-bill/1919
- [[FEDS-2026-011-Contrasting-Ledgers-Interbank-Payment-Systems]]: Federal Reserve FEDS 2026-011, February 2026. https://doi.org/10.17016/FEDS.2026.011

## See also

- [[MOC - CBDC]]
- [[MOC - Stablecoins]]
- [[MOC - Monetary-Hierarchy]]
- [[Stablecoin]]
- [[Tokenised-Deposit]]
- [[Singleness-of-Money]]

## Verification

| Marker | Claim | What would verify it |
|---|---|---|
| [V1] | H.R. 1919 passed the House on 2 July 2025 by 219 to 210 (date and vote as given in the vault note only). | The congress.gov actions page for H.R. 1919 (119th Congress). |
| [V2] | S.1124 remained pending in the Senate (vault note status as of mid-2026); current status as of October 2026 unknown. | The congress.gov actions page for S.1124. |
| [V3] | Project Pontes went live in production on or about 21 September 2026. | An ECB press release or Eurosystem Pontes page dated September 2026 or later. |
| [V4] | Whether the HKMA completed retail e-HKD preparatory work by mid-2026, and what it decided. | An HKMA press release or e-HKD page dated mid-2026 or later. |
