---
name: Singleness of Money
slug: Singleness-of-Money
type: concept
status: draft
created: 2026-08-09
domain:
- finance
synonyms: []
defined_in: ''
related_concepts:
- '[[Stablecoin]]'
- '[[Tokenised-Deposit]]'
- '[[Payment-Stablecoin]]'
- '[[E-Money-Token]]'
- '[[Unified-Ledger]]'
tags:
- concept
topic:
- topic/finance/stablecoins
wiki_indexed: '2026-08-17T00:00:00Z'
wiki_hash: b0b607fdc64cb7712b29c6e3201b23228120e19d856fbeb57d8784737408a428
wiki_role: concept
---

> **For future Claude.** Singleness of money is the idea that every form of money in one currency trades one for one, whoever issues it. In this vault the only source that models it directly is [[BoE-SWP1174-Model-of-Monetary-Singleness]]; most other notes that mention "singleness" do so in the vault's own Significance annotations or doctrine tags, not in the source text, so check the "Basis" column below before quoting a source as using the term. Par redemption and interchangeability of private money ([[FEDS-Note-2026-02-Brief-History-Bank-Notes-Stablecoins]]) are the closest substantive evidence.

# Singleness of Money

> **Definition.** Singleness of money is the property that all forms of money denominated in the same currency, whether central bank money, bank deposits or other privately issued money, exchange for one another at par (one for one), so a holder need not care who issued the money they hold [V1].

## Why it matters

The vault's sources on stablecoins, tokenised deposits and wholesale settlement keep returning to whether new private digital money will trade at par with existing money, and what keeps it there. Bank of England Deputy Governor Sarah Breeden puts the principle as "a pound is a pound, whoever issues it" (as of 2026-05, BoE) [[BoE-Breeden-Modernising-Money-and-Markets-2026]], and a Bank of England staff model treats central bank reserves and cash as the stabilisers of singleness (as of 2026-02, BoE) [[BoE-SWP1174-Model-of-Monetary-Singleness]]. A Federal Reserve historical note shows the same question in the pre-1913 US bank note era, when notes redeemed away from the issuing bank traded at discounts until redemption access was widened (as of 2026-02, Federal Reserve) [[FEDS-Note-2026-02-Brief-History-Bank-Notes-Stablecoins]]. The concept therefore links the vault's material on reserve requirements, redemption design, settlement assets and the [[MOC - Monetary-Hierarchy]]. In standard accounts, interbank settlement in central bank money is what keeps commercial bank money at par with central bank money [V2].

## How the vault's sources use the term

"Basis" records where the singleness link comes from: the source text itself, the vault note's own annotation, or a doctrine tag only.

| Source | How it uses or bears on singleness | Short quotation | Basis |
|---|---|---|---|
| [[BoE-SWP1174-Model-of-Monetary-Singleness]] (Hemingway, BoE staff working paper 1174, 2026-02-27) | Three-period banking model in which banks choose the unit of account of their debt and whether it serves as a medium of exchange. Small deviations from par (for example ATM withdrawal fees) can be efficient; inefficient equilibria are more likely when new private digital money issuers have business models distinct from incumbents. Reserves and cash stabilise singleness. Author's views, not Bank policy. | "small deviations from singleness may still be consistent with the efficient allocation"; "cash provides a backstop by enabling interoperability through central bank money." | Source text (title and abstract) |
| [[BoE-Breeden-Modernising-Money-and-Markets-2026]] (Breeden, BoE speech, 2026-05-19) | States the principle in plain terms within a UK "multi-money" retail vision of tokenised deposits, regulated stablecoins and possibly a retail CBDC; the Bank reports low risk appetite for a shift away from settlement in central bank money. | "a pound is a pound, whoever issues it" | Source text (term "singleness" not quoted in the vault note; vault note links it to SWP1174) |
| [[BoE-Sterling-Denominated-Systemic-Stablecoins-Policy-Statement-2026]] (BoE policy statement, 2026-06-22) | Requires at least 30% of systemic stablecoin backing to be held as central bank deposits, with up to 70% in short-term UK government debt, and confirms a planned Central Bank Liquidity Facility. The SWP1174 vault note says the model "Supports the policy logic of requiring central bank deposits in systemic stablecoin backing". | "A core strength of the UK regulatory approach to systemic stablecoins is its focus on high-quality backing assets." | Vault annotation (in SWP1174 note) |
| [[FEDS-Note-2026-02-Brief-History-Bank-Notes-Stablecoins]] (Carlson, Federal Reserve, 2026-02-06) | Historical case: an 1874 Treasury change allowing redemption at any sub-Treasury office made national bank notes trade uniformly at par and become interchangeable. Draws a parallel with stablecoin holders who usually cannot redeem directly with the issuer. Does not use the word "singleness". | "Bank note holders could be indifferent regarding the identity of the issuing bank. The notes were interchangeable." | Source text (par and interchangeability, not the term) |
| [[IMF-Note-2026-006-Rise-of-Tokenization]] (Adrian, Cabedo and Mancini-Griffoli, IMF Note 2026/006, 2026-07-01) | Concludes that stablecoins do not appear to be money because they move peer to peer without a contractual relationship with the issuer; names access to central bank reserves as a central policy question. Tagged `singleness-of-money`. | "Stablecoins can be transferred peer to peer between end users who do not necessarily have a direct contractual relationship with the issuer, nor are known to it. As such, stablecoins do not appear to be money." | Doctrine tag and vault annotation |
| [[IMF-WP-2026-074-Making-Stablecoins-Stable]] (Li and others, IMF WP/26/74, 2026-04-10) | Unregulated issuers hold risky assets, which raises run risk and may cause stablecoins to trade below par; run risk keeps stablecoins from meeting the "no-questions-asked" criterion for money (Holmstrom 2015). Safe-asset backing plus other issuer revenue is the proposed fix. | "The history of money can be read as a long attempt to satisfy the NQA criteria." | Vault annotation |
| [[FEDS-2026-011-Contrasting-Ledgers-Interbank-Payment-Systems]] (Leistra, Federal Reserve, 2026-02) | Describes US dollar interbank settlement and shared-ledger proposals (Regulated Liability Network, BIS unified ledger, IMF XC platform) that would put central bank, commercial bank and regulated nonbank money on one ledger. Takes no position. Tagged `singleness-of-money`. | "utilization of new technologies should not require shifting the legal underpinnings and treatment of money." (describing the RLN premise) | Doctrine tag |
| [[Ledger-Insights-EU-Parliament-Stablecoin-Multi-Issuance]] (Ledger Insights, 2026-07-09) | European Parliament endorsed regulated stablecoin multi-issuance, against the ESRB's recommendation to prohibit it; Circle's US and French USDC are fully interchangeable. The vault note frames the split as one over whether multi-issuance threatens singleness. | "with the tokens fully interchangeable" | Vault annotation |
| [[arXiv-2607-08524-Stablecoins-Under-Stress-Austrian-CASPs]] (Saggese and others, arXiv, 2026-07-09) | Transaction-level evidence that USDC par redemption is limited to institutions, so retail holders sold below par in secondary markets during the SVB episode. | "par redemption is reserved for institutional accounts" | Vault annotation |
| [[arXiv-2604-17167-Hidden-Plumbing-Stablecoins-GENIUS-Act-Era]] (Aronoff and others, arXiv, 2026-04-18) | Argues par redemption of US dollar stablecoins depends on Treasury and repo market functioning, broker-dealer capacity and blockchain rail reliability, not only backing-asset quality. Read from abstract only. | "Even conservatively backed stablecoins can face stress from redemption surges, market-intermediation bottlenecks" | Neither (bears on par, term not used) |
| [[BIS-WP1335-Tokenomics-Blockchain-Fragmentation]] (Shin, BIS WP 1335, 2026-03-10) | Model in which decentralised consensus fragments the monetary landscape; the vault note calls it the counterpoint to claims that money on public chains can achieve monetary singleness. | "Stablecoins cannot overcome this fragmentation since they inherit it from their underlying blockchain infrastructure." | Vault annotation |
| [[stablecoins-hybrid-monetary-ecosystems-2025]] (Wen and others, arXiv, 2025-05-16) | Proposes a two-layer architecture with private stablecoin issuers backed by central bank reserves; uses the 2023 SVB-USDC de-peg as a case study. | "private stablecoin issuers are backed by central bank reserves, ensuring uniformity, security, and programmability" | Doctrine tag and vault annotation |
| [[Ledger-Insights-Euroclear-SocGen-USDCV-Stablecoin-Settlement]] (Ledger Insights, 2026-06-25) | Euroclear to use SG-FORGE's MiCA-compliant USDCV as secondary settlement for dollar commercial paper, alongside wholesale CBDC for euro trades; the vault note reads this as a test of interoperability between private and public digital money. | None in the note on singleness | Doctrine tag and vault annotation |

Regulatory par requirements that bear on singleness without using the term: the GENIUS Act requires issuers to redeem at stated par value for fiat currency (enacted 2025-07-18, US) [[US-GENIUS-Act-2025-Comprehensive]]; the MAS consultation on the Single-Currency Stablecoin framework covers redemption at par (as of 2026-09, MAS) [[MAS-Stablecoin-Legislative-Amendments-Consultation-2026]].

## Open points

- **Source text versus vault annotation.** Only [[BoE-SWP1174-Model-of-Monetary-Singleness]] uses "singleness" in its own title and abstract in the vault. Most other links to the concept are the vault's own annotations or `singleness-of-money` doctrine tags, which future work should verify against the full source text before relying on them.
- **No canonical definition in the vault.** No vault note quotes a formal definition of singleness of money, so the definition above is marked [V1]. `defined_in` is left blank for that reason.
- **How much deviation from par matters.** [[BoE-SWP1174-Model-of-Monetary-Singleness]] treats small deviations as possibly efficient, while [[IMF-WP-2026-074-Making-Stablecoins-Stable]] treats run risk and trading below par as what keeps stablecoins from meeting the no-questions-asked test for money. These are different models, not a direct exchange.
- **What secures par.** The vault holds several candidate mechanisms without a settled view: central bank reserves and cash ([[BoE-SWP1174-Model-of-Monetary-Singleness]]), breadth of redemption access ([[FEDS-Note-2026-02-Brief-History-Bank-Notes-Stablecoins]]), market and rail plumbing ([[arXiv-2604-17167-Hidden-Plumbing-Stablecoins-GENIUS-Act-Era]]), and safe-asset backing ([[IMF-WP-2026-074-Making-Stablecoins-Stable]]). [[FEDS-2026-037-Fragility-Perfectly-Safe-Digital-Money]] models runs on digital money that can occur even when reserves are perfectly safe and liquid (as of 2026-06, Federal Reserve); it does not use the term singleness.
- **Multi-issuance.** The European Parliament and the ESRB differ on stablecoin multi-issuance under MiCA (as of 2026-07) [[Ledger-Insights-EU-Parliament-Stablecoin-Multi-Issuance]]; the vault does not yet hold the ESRB recommendation itself, so the ESRB's reasoning is not documented here.
- **Interoperability and fragmentation.** [[BIS-WP1301-Competing-Digital-Monies]] models "walled gardens" among competing digital monies and finds that fast payment systems and CBDCs restore interoperability (as of 2025-11, BIS); [[BIS-WP1335-Tokenomics-Blockchain-Fragmentation]] models fragmentation across blockchains. Neither vault note uses "singleness" in the source text.
- **Gaps among the requested sources.** The vault notes for [[IMF-Adrian-Tokenized-Finance-Money-Speech-2026-05]], [[bis-wp1363-macroeconomics-of-stablecoins]] and [[BIS-WP1382-Are-Stablecoins-Bank-Deposits-Substitutes]] do not mention singleness, par or the unit of account; they address safe settlement assets, macro channels and deposit substitution respectively. [[BIS-Tokenisation-Continuum]] and [[IMF-Tokenized-Finance-2026-04]] carry the `singleness-of-money` tag but their annotations do not discuss it. [[IMF-WP-2026-144-Stablecoins-Fixed-Exchange-Rate-Fragility]] concerns dollar stablecoins in fixed or managed exchange-rate economies, not domestic singleness.

## Sources

- [[BoE-SWP1174-Model-of-Monetary-Singleness]]
- [[BoE-Breeden-Modernising-Money-and-Markets-2026]]
- [[BoE-Sterling-Denominated-Systemic-Stablecoins-Policy-Statement-2026]]
- [[FEDS-Note-2026-02-Brief-History-Bank-Notes-Stablecoins]]
- [[IMF-Note-2026-006-Rise-of-Tokenization]]
- [[IMF-WP-2026-074-Making-Stablecoins-Stable]]
- [[FEDS-2026-011-Contrasting-Ledgers-Interbank-Payment-Systems]]
- [[FEDS-2026-037-Fragility-Perfectly-Safe-Digital-Money]]
- [[Ledger-Insights-EU-Parliament-Stablecoin-Multi-Issuance]]
- [[Ledger-Insights-Euroclear-SocGen-USDCV-Stablecoin-Settlement]]
- [[arXiv-2607-08524-Stablecoins-Under-Stress-Austrian-CASPs]]
- [[arXiv-2604-17167-Hidden-Plumbing-Stablecoins-GENIUS-Act-Era]]
- [[BIS-WP1335-Tokenomics-Blockchain-Fragmentation]]
- [[BIS-WP1301-Competing-Digital-Monies]]
- [[stablecoins-hybrid-monetary-ecosystems-2025]]
- [[US-GENIUS-Act-2025-Comprehensive]]
- [[MAS-Stablecoin-Legislative-Amendments-Consultation-2026]]
- Read, no singleness content: [[IMF-Adrian-Tokenized-Finance-Money-Speech-2026-05]], [[bis-wp1363-macroeconomics-of-stablecoins]], [[BIS-WP1382-Are-Stablecoins-Bank-Deposits-Substitutes]], [[BIS-Tokenisation-Continuum]], [[IMF-Tokenized-Finance-2026-04]], [[IMF-WP-2026-144-Stablecoins-Fixed-Exchange-Rate-Fragility]]

## See also

- [[MOC - Monetary-Hierarchy]]
- [[MOC - Stablecoins]]
- [[MOC - Seigniorage-and-Reserves]]
- [[MOC - CBDC]]
- [[Stablecoin]]
- [[Tokenised-Deposit]]
- [[Payment-Stablecoin]]
- [[E-Money-Token]]
- [[Unified-Ledger]]

## Verification

| Marker | Claim | What would verify it |
|---|---|---|
| [V1] | Singleness of money means all forms of money in one currency exchange at par, so holders need not care who issued them. | A primary definition from a central bank or BIS publication (for example a BIS Annual Economic Report chapter or a Bank of England discussion paper on new forms of digital money) added to the vault as a source note, then set as `defined_in`. |
| [V2] | In standard accounts, interbank settlement in central bank money keeps commercial bank money at par with central bank money. | A vault source note whose source text states this mechanism, for example a BIS or Bank of England publication on the two-tier monetary system. |
