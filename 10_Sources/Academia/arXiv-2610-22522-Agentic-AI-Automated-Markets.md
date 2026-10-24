---
type: source
title: Agentic AI in Automated Markets
authors:
- Irene Aldridge
- Lourenco Belleau-Bhowmik
- James Chan
- Josh Chang
- Kelly Deng
- Pranav Dhingra
- Xinda Ding
- Haodong Fang
- Satya Hanumanchi
- Carter He
- Shuang He
- Yadong Hou
- Vallab Karanam
- Rithvik Kasarla
- Tishya Khanna
- Jihyun Kim
- Sarah Konety
- Abhinav Kotta
- Anderson Lo
- Jake Luther
- Omar Mian
- Ishan Patwardhan
- Matteo Perona
- Chenyue Qi
- Shashank Ramachandran
- Shubham Rateria
- Jake Swain
- David Thai
- Michael Twersky
- Susan Wu
- Dean Xu
- Helenna Yin
- Jiachun Zheng
organisation: arXiv
source_type: paper
venue: arXiv (econ.EM; cs.ET; q-fin.RM; q-fin.TR)
year: 2026
date_published: '2026-10-15'
url: https://arxiv.org/abs/2610.22522
doi: '10.48550/arXiv.2610.22522'
jurisdiction:
- INTL
domain:
- agentic-ai
- llm-trading
- market-structure
- defi
doctrine: []
instrument: []
register_section: ''
status: draft
created: 2026-10-25
tags:
- source
- agentic-trading
- automated-market-makers
- reinforcement-learning
- market-stability
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/agentic-ai
- topic/finance/market-infrastructure
wiki_indexed: '2026-10-24T17:18:03Z'
wiki_hash: 1fa4be81f0894b71568c08683a16c3ae204a1e2d2eaa7330767b098554d9cd96
wiki_role: wiki
---

# Agentic AI in Automated Markets

## Citation

Aldridge, Irene, et al. "Agentic AI in Automated Markets". arXiv, 15 October 2026. https://arxiv.org/abs/2610.22522.

## One-line summary

A pilot study of reinforcement-learning trading agents (arbitrageur, manipulator, herd-follower) in automated-market-maker venues argues that market stress is behaviour-specific, so regulation should target agent behaviour rather than apply uniform volatility or turnover limits.

## Key claims

- The paper studies automated markets that host autonomous, learning trading agents and run on formulaic automated market makers (AMMs).
- Three behavioural archetypes are modelled as agentic reinforcement-learning systems: a rational arbitrageur, a manipulator and a retail herd-follower, each trained with a Deep Q-Network and with REINFORCE.
- Herd-followers produce the most frequent but shortest stress episodes; manipulators produce the fewest but most persistent.
- Rational agents show the most stable rolling Sharpe ratios despite the highest return volatility.
- SHAP attributions tie each archetype to signals that fit its objective: drawdown and cross-asset returns, short-term volatility and position state, and momentum.
- DQN learned faster per sample than REINFORCE, which was more prone to policy collapse; the pilot used one run per configuration and hourly data for AAVE, ETC and SUI.

## Excerpts

> "The results motivate behavior-specific regulation rather than uniform limits on volatility or turnover."
> ~ Abstract

> "The framework is asset-agnostic."
> ~ Section 1 (Introduction)

> "A pilot on hourly cryptocurrency data (AAVE, ETC, SUI) motivates the hypotheses."
> ~ Abstract

## Significance

- Gives a regulatory-design argument for agentic AI in on-chain trading venues, relevant to supervision of autonomous agents in tokenised markets.
- The framework is asset-agnostic, so it could extend to tokenised real-world assets traded on AMMs, although the pilot uses only crypto tokens.
- Complements the vault's agentic-finance papers, which focus on governance and payments rather than market-stability effects.

## Related

- [[10_Sources/Academia/arXiv-2607-05141-Square-Root-Price-Impact-Manipulation-Cycles]] - learning-agent markets and manipulation cycles.
- [[10_Sources/Academia/arXiv-2609-30940-Financial-Fragility-Societies-LLM-Agents]] - fragility in societies of LLM agents.
- [[10_Sources/Academia/arXiv-2609-33058-Evolution-Market-Microstructure-Age-of-AI]] - market microstructure in the age of AI.
