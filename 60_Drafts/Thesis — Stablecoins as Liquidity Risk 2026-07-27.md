---
type: draft
status: draft
created: 2026-07-27
title: Stablecoins as a Liquidity Risk to Global Financial Stability
domain:
- stablecoins
- finance
- market-structure
- monetary-policy
instrument:
- stablecoin-fiat
jurisdiction:
- US
- INTL
topic:
- topic/finance/stablecoins
tags:
- draft
- stablecoins
- liquidity-risk
- run-risk
- reserve-assets
- deposit-displacement
- genius-act
- unverified
related-sources:
- FEDS Note 2026-04 Stablecoins in 2025 Financial Stability
- BIS WP1270 Stablecoins and Safe Asset Prices
- BIS WP1355 Making Stablecoins Stable(r)
- IMF WP 2026-074 Making Stablecoins Stable
- US GENIUS Act 2025 (Comprehensive)
- Fed SVB Shadow Bank Runs and Stablecoins
- Fed Banks in the Age of Stablecoins
---

# Stablecoins as a Liquidity Risk to Global Financial Stability

> [!warning] Do not cite or link out from this note
> This draft carries 38 unresolved claims. See [[#10. Verification]].
> Claim markers `[V1]` to `[V38]` map to that table. Resolve the blocking
> items before `/wiki apply` indexes this note, or the errors will propagate
> into the MOCs and the synthesis layer.

---

## 1. Provenance and scope

**Source document**: `Stablecoins-as-a-Liquidity-Risk-to-Global-Financial-Stability-A-Short-Thesis.md`, held outside the vault. Imported 27 July 2026.

**What this note retains**: the financial-stability argument. Concentration, reserve composition, redemption mechanics, DeFi reflexivity, deposit displacement, and the regulatory calendar.

**What this note excises**: the equity short recommendation on Circle Internet Group (NYSE: CRCL). Insider-selling analysis, short-interest positioning, stock-price history, Altman Z-score, expected-value scenarios, position sizing, hedging, and stop-loss discipline. Schema §2.7 carries no domain value for equity research. Schema §2.3 carries no `source_type` for a trading recommendation. That material has no home in this vault. See [[#11. Excised material]].

**Source quality of the original**: 26 sources. Seven carry standing: three Circle press releases, Decrypt, CoinDesk, PYMNTS, Unchained, Visa VEEI, and MarketBeat. The rest are search-optimised content or vendor marketing. `plasma.to` markets a chain. `mexc.com` operates an exchange. `reap.global`, `stablecoininsider.org`, `eco.com`, `kavout`, `vaasblock`, `finsee.ai`, `news.market.us`, `cryptodaily`, and `coinledger` publish affiliate content. The original cites no central bank, no regulator, and no peer-reviewed work.

---

## 2. Thesis

Stablecoins transmit liquidity risk to the wider financial system through four channels: supply concentration in two issuers, reserve portfolios that require asset sales under redemption pressure, reflexive leverage loops in decentralised finance, and displacement of bank deposits.

The claim differs from the run-risk literature in one respect. The literature asks whether a stablecoin fails. This thesis asks what a stablecoin's failure does to Treasury bill markets, to bank funding, and to collateral chains. The transmission question matters more than the failure question.

Three catalysts fall inside 24 months: the GENIUS Act effective date, the Tether reserve compliance deadline, and the Clearing House tokenised deposit launch.

---

## 3. Channel one: supply concentration

The market stands at roughly $313 billion `[V1]`. Tether issues USDT at $189.5 billion for a 60% share. Circle issues USDC at $77.0 billion for a 25% share. Together they hold 85% of supply `[V2]`.

Two issuers carry the systemic weight. A failure at either produces a shock the remaining issuers cannot absorb, because the remaining issuers hold 15% of supply between them.

Concentration compounds at the venue layer. Roughly 72% of USDT and USDC supply sits on centralised exchanges `[V24]`. Aave holds the largest single on-chain USDC position at $6.3 billion `[V25]`. An exchange failure therefore produces stablecoin outflows before it produces anything else.

Geographic demand concentrates as well. Latin America accounts for about 31% of emerging-market stablecoin flow `[V26]`. That demand tracks currency devaluation rather than payment utility. It reverses when local rates stabilise or a domestic CBDC launches.

> Compare: [[10_Sources/Central-Banks/FEDS-Note-2026-04-Stablecoins-in-2025-Financial-Stability|FEDS Note 2026-04]] puts the sector at $317 billion after roughly 50% growth in 2025, and names three vulnerabilities the original omits: complex intermediation chains, vertical integration, and integration with traditional payment rails.

---

## 4. Channel two: reserve composition and the redemption rail

### 4.1 The revenue mechanism drives the reserve choice

Circle draws about 98% of revenue from reserve income `[V4]`. It invests USDC reserves in Treasury bills and money market instruments, held largely through a BlackRock government money market fund `[V16]`, earning about 4.16% as at Q1 2026 `[V5]`.

Coinbase holds 25% of Circle equity and takes 50% of residual reserve income after platform costs `[V6]`. Circle's net yield therefore runs at roughly half the gross bill yield `[V13]`.

This matters for stability rather than for equity value. An issuer whose entire revenue derives from reserve yield faces a standing incentive to lengthen duration or to reach for yield when rates compress. Reserve quality and issuer profitability move against each other.

> [[10_Sources/International-Agencies/IMF-WP-2026-074-Making-Stablecoins-Stable|IMF WP 2026/074]] states the trade-off directly. Safer reserves cut run risk and cut issuer profitability, which weakens the incentive to issue at all.

### 4.2 The redemption channel into bill markets

Redemption pressure forces reserve liquidation. Reserve liquidation moves Treasury bill prices. Bill price moves feed back into reserve adequacy.

The original asserts this loop without measuring it. The vault holds two measurements:

- [[10_Sources/International-Agencies/BIS-WP1270-Stablecoins-Safe-Asset-Prices|BIS WP 1270]] (Ahmed and Aldasoro): a $3.5 billion inflow lowers 3-month bill yields by about 0.71bp on impact and up to 4bp within 10 days. The effect strengthens when Treasury intermediaries are under stress.
- [[10_Sources/International-Agencies/BIS-WP1355-Making-Stablecoins-Stable-Regulation|BIS WP 1355]] (Goel, Lewrick, and Agarwal): cash and cash-like assets make up about 12% of a representative reserve portfolio. $10 billion of outflow-driven selling moves weekly 3-month bill returns by about 2.9bp; $30 billion moves them by about 6.4bp.

Gross and Senner (IMF WP/26/005) model the full loop: redemptions drain reserves, force sales, depress bond prices, erode issuer solvency, and amplify further redemptions. That paper is absent from the vault and should be added.

### 4.3 Attestation is not audit

Tether relies on BDO attestations rather than a full audit `[V14]`. An attestation gives limited assurance. An audit gives reasonable assurance. Tether engaged KPMG in late 2025, and no audit opinion had issued as at May 2026 `[V14]`.

Historical enforcement bears on whether reserve claims warrant belief. Tether settled with the CFTC and with the New York Attorney General in 2021 `[V18]`. The NYAG concluded that Tether misrepresented reserve adequacy `[V19]`.

---

## 5. Channel three: DeFi leverage reflexivity

The original states that reflexive leverage loops amplify cascade effects by a factor of 16. That figure appears three times in the source document and carries no citation anywhere `[V3]`.

The mechanism is plausible. Collateralised lending against a stablecoin, rehypothecation of the borrowed asset, and liquidation triggers keyed to price produce a cascade under a depeg. The magnitude is unevidenced.

**Do not carry the 16x figure forward.** It has the same shape as the 41.5% cost-reduction claim struck from the synthesis layer in June 2026. Either locate the model that produces it or state the mechanism without a multiplier.

Evidence that would substitute:

- [[10_Sources/Central-Banks/fed-svb-shadow-bank-runs-stablecoins-2025|Fed, SVB and shadow bank runs]] for the March 2023 USDC depeg as a worked case.
- Azar and Garofano, *Synthetic Stablecoins and Financial Stability* (Liberty Street Economics, June 2026), which documents a measured deleveraging spiral: USDe lost over 13% of market capitalisation on 10 October 2025 as funding turned negative and spot and derivatives unwound together.

---

## 6. Channel four: deposit displacement and bank-issued substitutes

### 6.1 Real-economy usage is thin

Stablecoins transacted about $33 trillion gross in 2025 `[V21]`. The original decomposes this as 88% crypto-on-crypto trading against real-economy payments of roughly $390 billion `[V22]`. Those two figures conflict. See the Verification table.

Velocity runs at about 14 times per year against 6 times for M1 demand deposits `[V29]`. Trading round-trips inflate that measure. Real-economy velocity runs at 0.6 to 1.2 times `[V29]`.

The stability reading: a float that turns over inside trading venues rather than settling goods reverses faster under stress than a payment float would. High velocity signals fragility here, not utility.

### 6.2 Banks are building substitutes

| Issuer | Product | Launch | Positioning |
|---|---|---|---|
| JPMorgan Chase | JPMD | 12 November 2025 `[V27]` | Institutional settlement, interbank liquidity |
| Citi | Citi Token Services | 2025 pilot `[V27]` | Treasury operations, custody integration |
| Bank of America | Tokenised deposits | 2027 announced `[V27]` | Interbank settlement |
| Wells Fargo | Tokenised deposits | 2027 announced `[V27]` | Interbank settlement |
| SoFi Bank | sofiUSD | 18 December 2025 `[V27]` | Consumer-facing, bank-integrated |

The Clearing House consortium announced a tokenised deposit network in June 2026 for launch in H1 2027 `[V28]`. Deposit backing carries FDIC insurance. Reserve-fund backing does not.

> [[10_Sources/Central-Banks/fed-banks-age-stablecoins-deposits-credit-2025|Fed, Banks in the Age of Stablecoins]] covers the deposit and credit channel. Huang and Keister (FRBNY Staff Report 1179, February 2026) put the narrow-banking trade-off formally: safe-asset-backed stablecoins crowd out bank credit, while tokenised deposits shift risk onto deposit insurance. Neither dominates. That paper is absent from the vault.

---

## 7. Regulatory catalyst calendar

| Date | Event | Status |
|---|---|---|
| 18 July 2026 | GENIUS Act rulemaking deadline | Missed `[V31]` |
| 18 January 2027 | GENIUS Act effective date; Tether compliance clock starts | Pending `[V31]` |
| Q4 2026 to Q1 2027 | Treasury reciprocity determination on foreign issuers | Pending `[V37]` |
| H1 2027 | Clearing House tokenised deposit network launch | Future `[V28]` |
| 18 July 2028 | Tether reserve compliance deadline | Future `[V32]` |

### 7.1 The reserve compliance squeeze

The GENIUS Act requires 1:1 backing in eligible assets: Treasury securities, deposits at insured banks, cash, and reverse repo against Treasuries `[V34]`. Gold, cryptocurrencies, secured loans, equities, and corporate bonds fall outside `[V34]`.

Tether reports Treasury bills at $141 billion, or 74.7% of reserves, against non-eligible assets of $48.5 billion, or 25.7% `[V33]`. That $48.5 billion requires liquidation inside an 18-month window `[V32]`.

The stability question is second-order and the original states it well. Forced liquidation of $48.5 billion in gold and crypto compresses the prices of those assets during the window in which Tether depends on their value. The sale programme degrades the reserve it is meant to realise.

**Note the naming error.** The original expands GENIUS as "Generating Regulations for Institutional Stablecoins" `[V30]`. Check against [[10_Sources/Law-Regulation/US-GENIUS-Act-2025-Comprehensive|US GENIUS Act 2025]] before drafting anything client-facing.

---

## 8. Counter-arguments

**"Stablecoins preserve dollar dominance."** The dollar benefit accrues to the Treasury, not to issuers or holders. Bank-issued substitutes and CBDCs deliver the same dollar-denomination benefit at lower counterparty risk. Financial inclusion does not require these two issuers.

**"Treasury demand drives a $1 trillion market by 2030."** The projection extrapolates 2020 to 2024 adoption without pricing competitive displacement. Bank alternatives now offer settlement against insured deposits.

**"Regulation reduces uncertainty."** Regulation creates enforcement. By setting reserve adequacy at 1:1 in Treasuries, the GENIUS Act legitimises bank-issued substitutes that clear the same bar with superior credit quality. Clarity accelerates displacement.

**"Network effects lock in share."** Switching costs are near zero. A holder swaps USDC for JPMD in seconds. Protocols carry no loyalty and will list bank-issued tokens on launch. An installed base of $189.5 billion in circulation is $189.5 billion in redemption liability.

**The strongest counter the original omits.** [[10_Sources/International-Agencies/IMF-WP-2026-074-Making-Stablecoins-Stable|IMF WP 2026/074]] finds stablecoins carry low credit and liquidity risk in normal conditions. The gap is the absent backstop, not the reserve. That reframes the thesis from "the reserves are bad" to "there is no lender of last resort". The second claim is harder to rebut and better supported.

---

## 9. What the vault already holds on this question

| Note | Bears on |
|---|---|
| [[10_Sources/Central-Banks/FEDS-Note-2026-04-Stablecoins-in-2025-Financial-Stability\|FEDS Note 2026-04]] | Market size, reserve quality and adoption, three named vulnerabilities |
| [[10_Sources/International-Agencies/BIS-WP1270-Stablecoins-Safe-Asset-Prices\|BIS WP 1270]] | Flow-to-bill-yield transmission, measured |
| [[10_Sources/International-Agencies/BIS-WP1355-Making-Stablecoins-Stable-Regulation\|BIS WP 1355]] | Fire-sale price impact, capital and liquidity requirements |
| [[10_Sources/International-Agencies/IMF-WP-2026-074-Making-Stablecoins-Stable\|IMF WP 2026/074]] | Backstop gap, narrow-bank versus equity-buffer designs |
| [[10_Sources/Central-Banks/fed-svb-shadow-bank-runs-stablecoins-2025\|Fed, SVB shadow bank runs]] | March 2023 USDC depeg |
| [[10_Sources/Central-Banks/fed-banks-age-stablecoins-deposits-credit-2025\|Fed, Banks in the Age of Stablecoins]] | Deposit displacement and credit supply |
| [[10_Sources/Central-Banks/fed-framework-vulnerabilities-money-like-products-2026\|Fed, Vulnerabilities in money-like products]] | Framework for the run channel |
| [[10_Sources/Central-Banks/FEDS-2026-037-Fragility-Perfectly-Safe-Digital-Money\|FEDS 2026-037]] | Fragility survives perfect reserve safety |
| [[10_Sources/International-Agencies/bis-wp1363-macroeconomics-of-stablecoins\|BIS WP 1363]] | Macroeconomic transmission |
| [[10_Sources/International-Agencies/BIS-WP1340-Stablecoin-Flows-FX-Markets\|BIS WP 1340]] | FX spillovers |
| [[10_Sources/International-Agencies/BIS-WP1359-Anatomy-Stablecoin-Transactions\|BIS WP 1359]] | Transaction composition, bears on the 88% claim |
| [[10_Sources/Law-Regulation/US-GENIUS-Act-2025-Comprehensive\|US GENIUS Act 2025]] | Statutory text, eligible assets, timetable |
| [[10_Sources/Academia/stablecoin-discount-tether-tbills-2025\|Stablecoin discount and Tether T-bills]] | Reserve composition and secondary pricing |
| [[30_Areas/Synthesis — Stablecoin Architecture Evolution\|Synthesis, Stablecoin Architecture Evolution]] | Parent synthesis this draft extends |

**Gaps to fill before this draft firms up**: Gross and Senner (IMF WP/26/005); Ma, Zeng, and Zhang (NBER 33882); Anadu and others (FRBNY SR 1073); Huang and Keister (FRBNY SR 1179); Lee and Tou (FRBNY SR 1185); Azar and Garofano (Liberty Street Economics, June 2026).

---

## 10. Verification

38 unresolved claims. Blocking items carry an internal contradiction or a checkable error. Open items need a primary source.

### 10.1 Blocking

| ID | Claim | Location in original | Problem |
|---|---|---|---|
| V3 | DeFi leverage loops amplify cascades 16x | §1 L5, §7.1 L185, §11 L354 | No source anywhere in the document. Load-bearing for the thesis. |
| V7 | $430m headwind per 100bp against $382.5m per 50bp | §1 L5, §3.1 L34 | The second implies $765m per 100bp. Cannot both hold. |
| V8 | Q1 2026 revenue +20% YoY against revenue down 59% annualised | §3.1 L29, §6.3 L158 | The table compares a TTM figure to one quarter. Invalid comparison. |
| V10 | Q1 2026 GAAP net loss $97m against annual net loss $69.5m | §3.1 L31, §6.4 L168 | Quarterly loss exceeds the stated annual loss. |
| V11 | Adjusted EBITDA $285m against $1.285bn | §3.1 L32, §6.3 L159 | Apparent inserted digit. |
| V18 | Tether CFTC penalty stated at $18.5m | §4.3 L75 | The CFTC order was $41m. $18.5m was the NYAG figure. The document assigns one number to both. |
| V22 | Real-economy volume $390bn described as 0.4% of $33tn | §5.1 L87 to L91 | $390bn of $33tn is about 1.2%. The residual after 88% trading is 12%. Three figures, no consistent reading. |
| V30 | GENIUS expanded as "Generating Regulations for Institutional Stablecoins" | §7.2 L190 | The Act is the Guiding and Establishing National Innovation for U.S. Stablecoins Act. |
| V35 | "Explicit Federal Reserve and BIS warnings" cited as support | §11 L349 | No Fed or BIS source appears among the 26 sources. |
| V38 | Fed stance "5.25 to 5.50%" against 3-month bills at 4.16% | §2.1 L13, §9.2 L255 | A 110bp to 130bp inversion at the 3-month point. One figure is stale. |

Two further items were excised with the equity sections and are recorded for completeness:

| ID | Claim | Location | Problem |
|---|---|---|---|
| V-X1 | Total insider sales $664m | §6.1 L133 to L141 | The table rows sum to about $9.3m. A 70x gap. |
| V-X2 | Altman Z-score 0.26 | §6.4 L166 | Undefined for a financial issuer. The document concedes at L167 that reserves are liabilities, which breaks the model inputs. |

### 10.2 Open

| ID | Claim | Resolve against |
|---|---|---|
| V1 | Market at $313bn | FEDS Note 2026-04 gives $317bn. BIS AER 2026 Ch III gives about $320bn at end-May 2026. |
| V2 | USDT $189.5bn / 60%; USDC $77.0bn / 25%; 85% combined | Issuer attestations and transparency reports. |
| V4 | Circle 98% of revenue from reserve income; FY2024 revenue $1.678bn, of which $1.641bn | Circle 10-K. |
| V5 | 3-month bill yield 4.16% at Q1 2026, down 66bp YoY | FRED series DTB3. |
| V6 | Coinbase holds 25% of Circle equity and takes 50% of residual reserve income | Circle S-1 and 10-K, not Decrypt. |
| V9 | Opex +76% YoY; SBC $566m FY2025; SBC $423.8m H1 2025 | H1 at $423.8m against FY at $566m implies H2 of $142m. Check both. |
| V12 | RLDC margin guidance 38 to 40%, down from 42 to 44% | Circle earnings release. |
| V13 | Take-home about 2.08% of reserves | Derivation halves the gross yield and ignores the custody fee. Restate the method. |
| V14 | BDO attestations; KPMG engaged late 2025; no opinion as at May 2026 | Tether attestation page and any KPMG announcement. |
| V15 | Circle S-1 lacked Big Four audited financials; "10 trading days registration statement" | An S-1 requires audited financials. The phrase is garbled. Pull the filing. |
| V16 | 90% of USDC backed by a BlackRock money market fund | Circle reserve report and the Circle Reserve Fund prospectus. |
| V17 | Circle failed to register as a money transmitter in multiple states, 2020 to 2021 | State regulator orders. |
| V19 | NYAG found Tether lacked adequate reserves for a 27-day period in 2019 | NYAG settlement text. Check the period and the finding. |
| V20 | No material 8-K filings by either issuer since 2022 | Tether files nothing with the SEC. The claim is meaningless as to Tether. |
| V21 | $33tn gross transaction volume in 2025 | Compare BIS WP 1359 on transaction composition. |
| V23 | 84% of illicit virtual-asset flows use stablecoins; $154bn sanctioned-entity volume 2025 | Chainalysis or TRM primary reporting. |
| V24 | 72% of USDT and USDC supply on centralised exchanges | On-chain analytics primary source. |
| V25 | Aave holds $6.3bn USDC | Aave protocol data, dated. |
| V26 | Latin America about 31% of emerging-market flow | Primary regional data. |
| V27 | Bank-issued product launch dates and chains | Issuer announcements for each of the five rows. |
| V28 | Clearing House announced June 2026 for H1 2027 launch | The Clearing House release, not the press coverage. |
| V29 | Velocity 14x against M1 at 6x; real-economy 0.6 to 1.2x | Visa VEEI holds standing. The 0.6 to 1.2x figure needs its own source. |
| V31 | Rulemaking deadline missed 18 July 2026; effective date 18 January 2027 | Statutory text and any Treasury notice. |
| V32 | Tether must liquidate $47bn to $49bn by 18 July 2028 | Statutory transition provisions. The document gives both $47 to $49bn and $48.5bn. |
| V33 | Tether reserves: bills $141bn (74.7%); non-eligible $48.5bn (25.7%) | Percentages imply a $188.7bn base against $189.5bn stated. Reconcile. |
| V34 | Eligible and non-eligible asset lists | Statutory text. |
| V36 | Aave $8.45bn outflows; rsETH exploit fallout | Primary protocol and incident reporting. |
| V37 | Treasury reciprocity determination pending Q4 2026 to Q1 2027 | Treasury notice. |

---

## 11. Excised material

The following sections of the source document remain outside this vault. They analyse an equity position, not a financial-stability question.

- §6 Insider and ownership data: insider sales, short interest, days to cover, borrow costs, stock price history, market capitalisation, Altman Z-score.
- §9 Risks to the short position: takeout risk, macro tailwind, product success, regulatory de-risking, squeeze risk.
- §10 Position sizing and risk management: expected-value table, capital allocation, entry and exit levels, hedging, position limits, execution discipline.
- §11 Recommended action: the short recommendation and price targets.

Two observations on that material, recorded once and not carried forward. The insider-sales total contradicts its own table by a factor of 70 `[V-X1]`. The Altman Z-score does not apply to a reserve-holding issuer `[V-X2]`.

---

## 12. Next steps

1. Resolve the 10 blocking items in §10.1. Each is a contradiction or a checkable error, and each is answerable without new research.
2. Strike the 16x amplification claim `[V3]` unless a model surfaces.
3. Add the six missing papers listed at the end of §9.
4. Repoint every macro claim from content-farm sources to the vault holdings in §9.
5. Reconsider the framing against IMF WP 2026/074. The backstop-gap argument carries better support than the reserve-quality argument.
6. Decide whether this stands alone or folds into [[30_Areas/Synthesis — Stablecoin Architecture Evolution|Synthesis, Stablecoin Architecture Evolution]].
