---
type: source
title: Square-Root Price Impact Is Necessary for Endogenous Manipulation Cycles in
  Learning-Agent Markets
authors:
- Yang Zhou
- Jianwen Chen
- Ruipeng Wei
organisation: Westlake University; Southwestern University of Finance and Economics
source_type: paper
venue: arXiv (q-fin.CP, econ.TH, nlin.AO, q-fin.TR)
year: 2026
date_published: '2026-07-06'
url: https://arxiv.org/abs/2607.05141
doi: 10.48550/arXiv.2607.05141
jurisdiction:
- CN
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
- market-manipulation
- algorithmic-trading
- market-microstructure
- reinforcement-learning
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/agentic-ai
- topic/blockchain-settlement
wiki_indexed: '2026-07-12T00:00:00Z'
wiki_hash: 9c79a81ae439e912b58d7378999d3f7663458a4985b72c8dd1c3c16cdc55f999
wiki_role: wiki
---



# Square-Root Price Impact Is Necessary for Endogenous Manipulation Cycles in Learning-Agent Markets

## Citation

Zhou, Yang, Jianwen Chen, and Ruipeng Wei. "Square-Root Price Impact Is Necessary for Endogenous Manipulation Cycles in Learning-Agent Markets". arXiv:2607.05141 (q-fin.CP), 6 July 2026. https://arxiv.org/abs/2607.05141.

## One-line summary

An evolutionary-optimised institutional trading agent placed among 20,000 herding retail traders spontaneously discovers a multi-cycle manipulative strategy earning up to 51% return, and the paper proves mathematically that this manipulation requires the square-root price-impact model rather than a linear one.

## Key claims

- A single CMA-ES-optimised LSTM institutional trading agent, trained purely to maximise terminal portfolio return, spontaneously discovers a predatory strategy without being programmed to manipulate.
- The discovered strategy produces 8 to 11 complete manipulation cycles over 2,000 trading days, with the best of 20 seeds achieving a total portfolio return of 51% and a mean of 37.7%.
- Each cycle contains four emergent phases: accumulation (around 26 days), push and wash trading (around 38 days), distribution with stealth selling (around 130 days), and reset (around 28 days).
- Mean-field reduction of the system to a nonlinear oscillator shows a continuous Hopf bifurcation as institutional capital exceeds a critical threshold, and a discontinuous fold transition in the herding-scale parameter.
- Square-root price impact is mathematically necessary for the manipulation cycle: replacing it with linear price impact eliminates the Hopf bifurcation entirely and renders the retail-only market unconditionally stable.
- The manipulation cycle persists even with zero retail herding, arising instead from position-tracking feedback coupled with square-root price impact alone, meaning the exploit is a property of market microstructure rather than of retail behaviour.
- Market safeguards modelled on Chinese A-share mechanisms, including daily price limits and stealth-distribution rules, shape the manipulation cycle's shape but do not prevent it from emerging.

## Excerpts

> "The agent spontaneously discovers a multi-cycle predatory strategy, producing 8-11 complete cycles over 2000 trading days with total portfolio return of +51% (best of 20 seeds; mean +37.7%)."
> ~ Abstract

> "Square-root impact is shown to be necessary: linear impact eliminates the Hopf bifurcation entirely and renders the retail market unconditionally stable. Manipulation cycles thus emerge as the optimal-control solution of a nonlinear dynamical system."
> ~ Abstract

> "The limit cycle persists even at β = 0: position-tracking feedback coupled with square-root price impact creates a self-sustained nonlinear oscillator requiring no retail herding."
> ~ Abstract

> "The A-share mechanisms (wash trading, daily price limits, stealth distribution) shape but do not create the cycles... the cyclic strategy survives every perturbation, with return varying by at most 3% and the cycle count by at most 1.3."
> ~ §III.A, Emergent multi-cycle strategy

## Significance

- Provides a rigorous, mathematically grounded warning that autonomous learning agents can discover market manipulation as an emergent optimal-control solution without being instructed to manipulate, directly bearing on the wiki's agentic-AI trading risk analysis.
- Identifies the square-root price-impact model, the standard assumption underlying most modern market-impact literature and many blockchain-based automated market makers, as the structural precondition for this manipulation channel.
- Shows that conventional market safeguards (price limits, settlement delays) shape rather than eliminate manipulation risk from learning agents, a caution for exchanges and DeFi venues considering agentic-AI trading participants.
- Strengthens the case for microstructure-level, rather than purely behavioural, regulatory scrutiny of autonomous trading agents as their deployment scales.

## Related

- [[10_Sources/Academia/arXiv-2607-03015-Raven-Agent-Prediction-Market-Trading]] - autonomous LLM trading agent architecture built around deterministic risk control
- [[10_Sources/Academia/arXiv-2607-08652-Formal-Mechanisms-Market-Stability-Agent-Societies]] - formal mechanisms for constraining self-interested agent behaviour in simulated markets
