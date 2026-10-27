---
title: Seigniorage versus reserve carry
name: Seigniorage versus reserve carry
slug: Seigniorage-vs-Reserve-Carry
type: concept
domain: [finance]
synonyms: [reserve income, issuer carry]
related_concepts:
  - "[[Stablecoin]]"
  - "[[Payment-Stablecoin]]"
  - "[[Tokenised-Deposit]]"
  - "[[Singleness-of-Money]]"
  - "[[USDC]]"
  - "[[USDT]]"
  - "[[RWA-Stablecoin]]"
tags: [concept, stablecoins, reserves]
status: draft
created: 2026-10-27
---

> **For future Claude.** This note separates two kinds of issuer income that commentary often runs together: seigniorage (income from issuing money that pays no interest) and reserve carry (the return a stablecoin issuer earns on the assets backing its coins). As of 27 October 2026 no source note in the vault uses the word "seigniorage"; the word appears only in vault metadata, so the standard meaning is stated here as framing and flagged for verification. Use the vault evidence below for reserve composition, yield rules and scale, and the Verification table for what still needs a primary source.

# Seigniorage versus reserve carry

> **Definition.** Seigniorage is the income a money issuer earns because its money is a liability that pays no interest, while reserve carry is the return a stablecoin issuer earns on the interest-bearing assets held against its coins, less what it pays out `[V1]` `[V3]`.

## Why it matters

The vault groups its reserve sources under [[MOC - Seigniorage-and-Reserves]], whose own header already warns that "seigniorage" is used loosely and that an issuer's reserve income is carry on reserve assets, not issuance profit on a zero-interest liability (MOC note, added 24 October 2026). The distinction matters for reading three strands of the vault. First, US law confines payment stablecoin reserves to cash, short Treasury securities, insured deposits, Treasury repo, government money market funds and central bank reserves, so the issuer's income depends on short-term rates on those assets ([[US-GENIUS-Act-2025-Comprehensive]], vault summary of the Act as signed 18 July 2025). Second, the same Act, as summarised in the vault, bars payment of interest or returns to holders, which decides who receives that return ([[US-GENIUS-Act-2025-Comprehensive]]). Third, policy papers treat issuer revenue as a design variable: the IMF paper proposes "other sources of revenue for issuers" alongside safe-asset backing ([[IMF-WP-2026-074-Making-Stablecoins-Stable]], April 2026), and the Bank of England revised its backing-asset proposals "to support the viability of issuers' business models" ([[BoE-Sterling-Denominated-Systemic-Stablecoins-Policy-Statement-2026]], June 2026).

## Seigniorage (the standard meaning)

- **Framing, not from the vault.** In the standard textbook meaning, seigniorage is the revenue a currency issuer earns from issuing money, a liability that pays no interest, over and above the cost of producing and maintaining it `[V1]`. Central banks typically pass most of this income to the state after costs `[V2]`.
- **Vault evidence on central bank money that pays no interest.** The ECB states that "like cash, the digital euro will not be remunerated" ([[ECB-Blog-2026-Digital-Euro-Opportunity-for-Banks]], as of 27 March 2026). This shows a central bank liability designed to pay no interest; the note does not discuss the income the Eurosystem earns from it.
- **Central bank deposits in stablecoin backing.** The Bank of England requires at least 30% of a sterling systemic stablecoin's backing to be held as central bank deposits, with a cap of 70% on interest-bearing short-term UK government debt; the vault note describes the deposit portion as unremunerated ([[BoE-Sterling-Denominated-Systemic-Stablecoins-Policy-Statement-2026]], as of 22 June 2026, cap figures per the Bank's news release of the same date).
- **Central bank remuneration as issuer revenue.** The IMF paper lists "central bank reserves remuneration" as one possible source of issuer revenue where stablecoins are backed by central bank reserves in a narrow bank setting ([[IMF-WP-2026-074-Making-Stablecoins-Stable]], April 2026). In that setting the issuer's income would come from the central bank's interest on reserves, not from the issuer's own liability.
- **Remittances to the state.** No vault source covers central bank remittances to a treasury or government (see Open points).

## Reserve carry (what stablecoin issuers earn)

**What the reserves are.**

- Eligible US reserves are US currency, Treasury securities with maturity under 93 days, demand deposits at insured institutions, repo secured by Treasury bills, government money market funds, central bank reserves and, with regulator approval, tokenised federal government assets ([[US-GENIUS-Act-2025-Comprehensive]], vault summary, as of 2025).
- The OCC final rule cut the daily liquidity requirement from 10% to 5%, dropped the proposed 30% weekly requirement and removed the proposed 20-day weighted average maturity cap, so an issuer could hold 5% in daily liquidity and the rest in Treasuries of up to 93 days ([[Ledger-Insights-OCC-Final-GENIUS-Act-Stablecoin-Rules]], as of 21 October 2026). The rule takes effect on 18 January 2027 ([[OCC-Bulletin-2026-50-GENIUS-Act-Regulations-Final-Rule]]).
- Asset managers have launched reserve money market funds for issuers: Fidelity's fund is a conventional GENIUS Act compliant fund, at least eight institutions offer similar funds, and nearly all charge 0.17% to 0.18% after fee waivers ([[Ledger-Insights-Fidelity-Stablecoin-Reserve-MMF]], as of 18 June 2026). Invesco's tokenised reserve fund invests in cash, Treasuries of 93 days or less and overnight Treasury repo ([[Ledger-Insights-Invesco-Tokenized-Stablecoin-Reserve-Fund]], as of 28 June 2026).
- The Circle Reserve Fund held about 86% of USDC reserves as of March 2026; its repo holdings stood at 69% of net assets, and USDT reserves include corporate bonds, gold, Bitcoin and secured loans ([[NYFed-LSE-Stablecoins-NonCrypto-Shocks-2026-Update]], as of 31 July 2026).
- Circle's structure separates a New York trust that issues USDC from a national trust that manages reserves and provides custody, with reserve management described as a future capability ([[Ledger-Insights-Circle-NY-Trust-Charter]], as of 2 August 2026; [[Ledger-Insights-Circle-OCC-Final-Approval-Trust-Bank]], as of 11 July 2026).

**Scale of the reserve book.**

- Dollar-backed stablecoins held over USD 200 billion in assets as of March 2025, and issuers bought USD 40 billion of Treasury bills in 2024 ([[BIS-WP1270-Stablecoins-Safe-Asset-Prices]], May 2025).
- Tether held about USD 98.5 billion of Treasury bills in Q1 2025, 1.6% of bills outstanding ([[stablecoin-discount-tether-tbills-2025]], May 2025).
- Stablecoin market capitalisation reached about USD 317 billion by April 2026 ([[FEDS-Note-2026-04-Stablecoins-in-2025-Financial-Stability]]); the NY Fed puts US dollar stablecoins at about USD 308 billion ([[NYFed-LSE-Stablecoins-NonCrypto-Shocks-2026-Update]], as of July 2026).
- US debt managers treat stablecoin reserves as a source of bill demand: dealers in April 2025 said providers already held significant Treasury positions ([[UST-TBAC-Minutes-2025-04-29-Stablecoins-Charge]]), and the February 2026 minutes list "potential demand associated with stablecoins" among shifts in Treasury demand ([[UST-TBAC-Minutes-2026-02-03-Stablecoin-Demand-Bills]]).

**How the models treat issuer income.**

- Without regulation, issuers hold risky assets to maximise profit, which raises run risk ([[IMF-WP-2026-074-Making-Stablecoins-Stable]], April 2026).
- Without regulation, issuers choose minimal capital and bond-heavy portfolios; liquidity requirements shift portfolios toward cash and capital requirements raise both cash and capital buffers ([[BIS-WP1355-Making-Stablecoins-Stable-Regulation]], June 2026).
- Par redemption depends on Treasury and repo market functioning and broker-dealer capacity, not only on backing-asset quality ([[arXiv-2604-17167-Hidden-Plumbing-Stablecoins-GENIUS-Act-Era]], abstract only, April 2026).

**Who receives the return: yield rules.**

- The vault's GENIUS Act summary records that stablecoin holders cannot earn interest or returns ([[US-GENIUS-Act-2025-Comprehensive]], as of 2025; secondary summary, statutory text not quoted).
- The Federal Reserve Board's proposed Regulation (12 CFR Part 247) includes a ban on paying interest or yield to holders in Subpart B ([[Fed-FR-2026-19860-Board-GENIUS-Act-Proposed-Rule]], proposed 29 September 2026, comments due 30 November 2026).
- Trade press headlines the OCC final rule as relaxing "reserve and yield rules", but the free portion read for the vault covers reserves only ([[Ledger-Insights-OCC-Final-GENIUS-Act-Stablecoin-Rules]], as of 21 October 2026).
- Before the Act, the TBAC charge noted that some stablecoins were moving toward paying interest and discussed the effect of interest-bearing stablecoins on Treasury demand, the dollar and insured depository institutions ([[UST-TBAC-Minutes-2025-04-29-Stablecoins-Charge]], April 2025).
- The Bank of England statement clarifies policy on coinholder remuneration; the vault note does not record what that policy is ([[BoE-Sterling-Denominated-Systemic-Stablecoins-Policy-Statement-2026]], June 2026).
- For contrast, SoFi's tokenised deposit pays holders a variable 4.4% and converts into the bank's SoFi USD stablecoin; the article attributes the economics to double-digit personal loan yields ([[Ledger-Insights-SoFi-Retail-Tokenized-Deposits-SOFIE]], as of 22 October 2026).

**Where the two meet and differ.**

| Point | Seigniorage | Reserve carry | Basis |
|---|---|---|---|
| Liability | Money that pays no interest | Payment stablecoin; holders may not be paid interest under the GENIUS Act | `[V1]`; [[US-GENIUS-Act-2025-Comprehensive]], [[Fed-FR-2026-19860-Board-GENIUS-Act-Proposed-Rule]] |
| Assets held | Central bank's own portfolio | Cash, short Treasuries, repo, government MMFs, central bank reserves | `[V1]`; [[US-GENIUS-Act-2025-Comprehensive]], [[NYFed-LSE-Stablecoins-NonCrypto-Shocks-2026-Update]] |
| Source of income | Issuing the money itself | Return on the reserve assets, which depends on short-term rates and portfolio choice | `[V1]` `[V3]`; [[IMF-WP-2026-074-Making-Stablecoins-Stable]], [[BIS-WP1355-Making-Stablecoins-Stable-Regulation]] |
| Recipient of net income | Typically the state | The issuer, subject to costs and rules; no vault source sets out issuer net income | `[V2]` `[V3]` |
| Effect on government funding | Not covered in vault | Stablecoin inflows lower 3-month bill yields by 2.5 to 3.5 basis points; one paper estimates about USD 15 billion a year in interest savings for the US government from Tether's bill demand | [[BIS-WP1270-Stablecoins-Safe-Asset-Prices]], [[stablecoin-discount-tether-tbills-2025]] |

## How the vault's sources use the word "seigniorage"

- A search of `10_Sources`, `30_Areas` and `60_Drafts` for "seigniorage" and "seignorage" returned no matches (search run 27 October 2026). No source note, synthesis or draft in the vault uses the word.
- The word appears only in vault metadata: the MOC name [[MOC - Seigniorage-and-Reserves]], the controlled topic tag `topic/finance/seigniorage-reserves`, and a title filter added on 24 October 2026 to the fed-staff-papers monitor channel. The MOC's own caveat is the only place the vault discusses its meaning.
- The source notes describe issuer economics in other terms: "profit" and "other sources of revenue for issuers" ([[IMF-WP-2026-074-Making-Stablecoins-Stable]]), issuers' "business models" ([[BoE-Sterling-Denominated-Systemic-Stablecoins-Policy-Statement-2026]]), and "interest savings" for the US government ([[stablecoin-discount-tether-tbills-2025]]).
- The claim that the stablecoin literature calls reserve income "seigniorage" therefore rests on no vault source at present `[V4]`.

## Open points

- **Central bank remittances.** A search for "remit" finds only cross-border payment remittances (for example [[Ledger-Insights-BPI-Stablecoin-Remittances]] and [[FEDS-Note-2026-08-Decade-US-Cross-Border-Payments-Efforts]]). No vault source covers central bank remittances to a treasury, consistent with the coverage gap recorded in [[MOC - Seigniorage-and-Reserves]].
- **Issuer net income.** A search for "net interest" returned no matches in `10_Sources`, `30_Areas` or `60_Drafts`. No source note sets out a stablecoin issuer's reserve income, distribution costs or net margin; issuer annual reports or filings are absent.
- **Yield rule detail.** The OCC final rule's yield provisions were not read (paywalled press note; the bulletin note summarises structure only), and only the first part of the Federal Reserve proposal was read. The scope of the holder-yield prohibition, including whether it reaches payments by parties other than the issuer, is not set out in any vault note.
- **UK remuneration policy.** The content of the Bank of England's coinholder remuneration policy is not recorded in the vault note.
- **Statute text.** The GENIUS Act note is a secondary summary; the vault holds no quoted statutory text for the yield prohibition or the eligible reserve list.
- **Usage in the literature.** Whether, and by whom, reserve income is called "seigniorage" needs a source before the MOC caveat can be cited as evidence `[V4]`.

## Sources

- [[US-GENIUS-Act-2025-Comprehensive]]
- [[OCC-Bulletin-2026-50-GENIUS-Act-Regulations-Final-Rule]]
- [[Ledger-Insights-OCC-Final-GENIUS-Act-Stablecoin-Rules]]
- [[Fed-FR-2026-19860-Board-GENIUS-Act-Proposed-Rule]]
- [[BoE-Sterling-Denominated-Systemic-Stablecoins-Policy-Statement-2026]]
- [[IMF-WP-2026-074-Making-Stablecoins-Stable]]
- [[BIS-WP1355-Making-Stablecoins-Stable-Regulation]]
- [[BIS-WP1270-Stablecoins-Safe-Asset-Prices]]
- [[stablecoin-discount-tether-tbills-2025]]
- [[FEDS-Note-2026-04-Stablecoins-in-2025-Financial-Stability]]
- [[NYFed-LSE-Stablecoins-NonCrypto-Shocks-2026-Update]]
- [[UST-TBAC-Minutes-2025-04-29-Stablecoins-Charge]]
- [[UST-TBAC-Minutes-2026-02-03-Stablecoin-Demand-Bills]]
- [[Ledger-Insights-Fidelity-Stablecoin-Reserve-MMF]]
- [[Ledger-Insights-Invesco-Tokenized-Stablecoin-Reserve-Fund]]
- [[Ledger-Insights-Circle-OCC-Final-Approval-Trust-Bank]]
- [[Ledger-Insights-Circle-NY-Trust-Charter]]
- [[arXiv-2604-17167-Hidden-Plumbing-Stablecoins-GENIUS-Act-Era]]
- [[ECB-Blog-2026-Digital-Euro-Opportunity-for-Banks]]
- [[Ledger-Insights-SoFi-Retail-Tokenized-Deposits-SOFIE]]

## See also

- [[MOC - Seigniorage-and-Reserves]]
- [[MOC - Stablecoins]]
- [[Stablecoin]]
- [[Payment-Stablecoin]]
- [[Tokenised-Deposit]]

## Verification

| Marker | Claim | What source would verify it |
|---|---|---|
| `[V1]` | Seigniorage is the revenue a currency issuer earns from issuing money, a zero-interest liability, over and above its cost. | A central bank or IMF/BIS glossary or textbook definition of seigniorage (for example a BIS or IMF explainer, or a central bank annual report section on seigniorage income). |
| `[V2]` | Central banks typically remit most of their net income, including seigniorage, to the state. | Federal Reserve remittances to the Treasury (Federal Reserve annual financial statements) or the Bank of England or Eurosystem profit distribution rules. |
| `[V3]` | A stablecoin issuer's income is mainly the return on its reserve assets, net of what it pays out. | Issuer filings with an income breakdown (for example a Circle annual report or S-1) or an official study of issuer revenue. |
| `[V4]` | Stablecoin literature and commentary often call issuer reserve income "seigniorage". | Any paper or official report in the vault's scope that uses "seigniorage" for stablecoin issuer income. |
