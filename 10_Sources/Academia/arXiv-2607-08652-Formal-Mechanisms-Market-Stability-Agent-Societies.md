---
type: source
title: 'Formal Mechanisms for Market Stability in Self-Interested Agent Societies:
  A Marketplace Simulation Study'
authors:
- Eugene Ng Yi Sheng
- Bingquan Shen
organisation: DSO National Laboratories; National University of Singapore
source_type: paper
venue: arXiv (cs.AI)
year: 2026
date_published: '2026-07-09'
url: https://arxiv.org/abs/2607.08652
doi: 10.48550/arXiv.2607.08652
jurisdiction:
- SG
- INTL
domain:
- agentic-ai
- llm-trading
- market-structure
doctrine: []
instrument: []
register_section: ''
nlm_id: ''
nlm_skip: false
status: draft
created: 2026-07-12
tags:
- source
- agentic-ai
- multi-agent-systems
- market-stability
- mechanism-design
- llm-agents
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/agentic-ai
- topic/blockchain-settlement
wiki_indexed: '2026-07-12T00:00:00Z'
wiki_hash: e9b1ffc61fc12428ade88d4bf99b0d52a039dd30eadd938bd3318a8f1c348429
wiki_role: wiki
---



# Formal Mechanisms for Market Stability in Self-Interested Agent Societies: A Marketplace Simulation Study

## Citation

Ng Yi Sheng, Eugene, and Bingquan Shen. "Formal Mechanisms for Market Stability in Self-Interested Agent Societies: A Marketplace Simulation Study". arXiv:2607.08652 (cs.AI), 9 July 2026. https://arxiv.org/abs/2607.08652.

## One-line summary

Simulating 18 DeepSeek-V3 agents trading in a constrained marketplace, the paper finds that Mediation is the most resilient formal cooperation mechanism, sustaining positive honest-agent utility even under the strongest optimised adversarial attack.

## Key claims

- Self-interested LLM agents defect toward all-defection equilibria in repeated trading without formal mechanisms layered on top of unrestricted communication; natural-language promises alone are cheap and unverifiable.
- The marketplace environment forces structural interdependence: agents hold one of three complementary production specialties and must trade through bilateral barter to earn positive utility, since autarky yields a loss equal to production cost.
- Goods decay by 20% each round, creating temporal urgency that prevents agents from hoarding inventory as insurance against defection.
- Across eight mechanism conditions tested over 200 rounds under progressive troll injection (0 to 16 trolls), Mediation emerges as the top-performing mechanism for sustaining cooperative trade.
- Adversarial red-teaming with six iteratively prompt-optimised LLM-driven trolls shows the strongest attack reduces honest-agent utility by 13.3% but cannot collapse the market.
- The authors define adversarial robustness as a mechanism's ability to sustain positive honest-agent utility under optimised attack, concluding Mediation "can be bent but not broken."
- The findings extend CoopEval by testing a complex multi-good marketplace rather than abstract matrix games, adding Governance, Network Rewiring, Sanctions, and Judicial mechanisms to the comparison set.

## Excerpts

> "We conduct two experimental phases: (1) a mechanism comparison across eight conditions under progressive troll injection over 200 rounds, identifying Mediation as the top-performing mechanism; and (2) adversarial red-teaming of Mediation using iteratively prompt-optimised LLM-driven trolls, finding that the best attack (v6) reduces honest-agent utility by 13.3% but cannot collapse the market."
> ~ Abstract

> "As autonomous agents are deployed in economic settings, trading, negotiating, and allocating resources on behalf of human principals, the question of what keeps a population of self-interested agents from collapsing into mutual exploitation becomes practically urgent."
> ~ §1, Introduction

> "Communication alone is insufficient. Natural language promises are cheap and unverifiable. The question is therefore not whether communication helps, but how much formal structure is needed on top of communication to sustain societal cooperation, and how resilient that structure is when adversaries actively attempt to undermine it."
> ~ §1, Introduction

> "We define adversarial robustness as a mechanism's ability to sustain positive honest-agent utility under optimised attack, and find that Mediation is robust: it can be bent but not broken."
> ~ Abstract

## Significance

- Provides empirical evidence for which governance mechanism sustains stability when autonomous economic agents trade on behalf of human principals, directly relevant to the wiki's agentic-AI trading pillar.
- Establishes a formal, measurable definition of adversarial robustness for cooperation mechanisms, a benchmark future governance proposals for agentic markets can be tested against.
- Demonstrates that unrestricted communication between AI agents is insufficient for market stability, supporting the case for structural safeguards over reliance on agent self-reporting or negotiation alone.
- Adds a marketplace-specific test bed (multi-good barter, perishable inventory) to the wiki's evidence base on agent economies, complementing prediction-market and pure-payment agent studies.

## Related

- [[10_Sources/Academia/arXiv-2607-03015-Raven-Agent-Prediction-Market-Trading]] - autonomous LLM trading agent architecture in prediction markets
- [[10_Sources/Academia/arXiv-2607-05141-Square-Root-Price-Impact-Manipulation-Cycles]] - learning-agent manipulation dynamics in a different market structure
- [[10_Sources/Academia/arXiv-Agent-Economy-Blockchain-Foundation]] - blockchain-based governance foundation for autonomous AI agent economies
