---
# --- Required on every note (schema.md §2.1) ---
type: source
status: stub                 # inbox | stub | draft | review | permanent | archived
created:                     # YYYY-MM-DD
tags: [source]

# --- Source fields (schema.md §2.3) ---
title: ""
authors: []                  # list of strings; author or issuer names
organisation: ""             # issuing body where distinct from authors, e.g. BIS
source_type: ""              # statute | regulation | guidance | report | paper |
                             # press-release | industry-note | speech | testimony |
                             # dataset | pilot-doc | book | blog | interview
venue: ""                    # conference, journal, registry, podcast, site
year:                        # integer
date_published:              # YYYY-MM-DD
url: ""                      # canonical link; TBD permitted at stub stage
doi: ""                      # optional

# --- Controlled axes (schema.md §2.6 to §2.9) ---
jurisdiction: []             # US | UK | EU | SG | HK | JP | KR | AE | CH | NZ | AU |
                             # CA | BR | IN | CN | INTL | MULTI
domain: []                   # finance | law | securities-law | private-law |
                             # international-private-law | monetary-policy |
                             # market-structure | market-infrastructure | settlement |
                             # cross-border-payments | carbon-credits |
                             # environmental-markets | real-estate | property-rights |
                             # land-registry | stablecoins | tokenised-deposits | cbdc |
                             # agentic-ai | llm-trading | blockchain-settlement | defi |
                             # ai-governance | taxation
doctrine: []                 # law sources only: property-category | control |
                             # take-free-purchaser | secured-transactions | choice-of-law |
                             # insolvency | custody | intermediation | transfer |
                             # singleness-of-money | prospectus | mifid-equivalence |
                             # licensing | aml-cft | market-abuse | consumer-protection |
                             # disclosure | reserve-requirements
instrument: []               # finance sources only: tokenised-fund | tokenised-bond |
                             # tokenised-deposit | tokenised-treasury |
                             # tokenised-money-market-fund | tokenised-private-credit |
                             # tokenised-equity | tokenised-real-estate |
                             # tokenised-carbon-credit | tokenised-commodity |
                             # stablecoin-fiat | stablecoin-rwa-backed |
                             # stablecoin-algorithmic | cbdc-wholesale | cbdc-retail |
                             # e-money-token | asset-referenced-token | nft | security-token

# --- Topic vocabulary: CLOSED SET OF 14. Copy values verbatim. ---
# Never invent a topic. If none fits, use the nearest and raise it in the run report.
#   topic/finance                        topic/law
#   topic/finance/stablecoins            topic/law/securities
#   topic/finance/tokenised-deposits     topic/law/property-rights
#   topic/finance/market-infrastructure  topic/law/digital-assets
#   topic/finance/cbdc                   topic/tokenisation
#   topic/blockchain-settlement          topic/carbon-credits
#   topic/agentic-ai                     topic/real-estate
topic: []

# --- Cross-references ---
register_section: ""         # section of 10_Sources/SOURCE-REGISTER.md, e.g. "1.1"
# nlm_id and nlm_skip are DEPRECATED (9 August 2026). The NotebookLM sync was
# retired from the weekly cron. Do not populate them on new notes.
# See 99_Meta/NotebookLM-bridge.md.

# Do NOT hand-edit wiki_indexed, wiki_hash, wiki_role, nlm_last_sync,
# or watchlist_channel. The /wiki skill and the orchestrator set them (§2.11).
---

# 

**Source:** [Publisher](URL)
**NotebookLM:** `` in [tokenise](https://notebooklm.google.com/notebook/d9fa07bb-4802-4626-8855-ba899655ab2b)
**Register entry:** [[SOURCE-REGISTER]]

## Citation

## Annotation

What does this source argue? What evidence does it bring? Why is it load-bearing for the wiki?

## Concepts

- [[]]

## See also

- [[MOC - Root]]
