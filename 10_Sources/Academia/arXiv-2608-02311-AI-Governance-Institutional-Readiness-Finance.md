---
type: source
title: AI Governance for Institutional Readiness in Finance
authors:
- Irene Aldridge
- Steve Krawciw
organisation: RiskAICenter
source_type: paper
venue: arXiv (econ.EM, q-fin.RM, q-fin.ST)
year: 2026
date_published: '2026-08-03'
url: https://arxiv.org/abs/2608.02311
doi: 10.48550/arXiv.2608.02311
jurisdiction:
- US
domain:
- agentic-ai
- ai-governance
- finance
doctrine: []
instrument: []
register_section: ''
nlm_id: ''
nlm_skip: false
status: draft
created: 2026-08-09
tags:
- source
- agentic-ai
- ai-governance
- asset-management
- risk-management
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/agentic-ai
- topic/finance
wiki_indexed: '2026-08-09T00:00:00Z'
wiki_hash: d100fbf11b5075e63b25132b189fa4ee78790060e755e8220ca31ebab6cdf624
wiki_role: wiki
---



# AI Governance for Institutional Readiness in Finance

## Citation

Aldridge, Irene, and Steve Krawciw. "AI Governance for Institutional Readiness in Finance". arXiv:2608.02311 (econ.EM), 3 August 2026. https://arxiv.org/abs/2608.02311.

## One-line summary

The paper documents a governance gap for agentic AI in asset management and proposes a computable four-layer framework to detect policy drift and crowding risk.

## Key claims

- 88% of surveyed finance professionals report no operational governance framework for agentic AI, despite universal awareness of its deployment.
- Only 24 of 75 large US money managers disclosing AI use in Form ADV filings report a formal governance policy.
- The governance gap is architectural, not cultural, because governance built for deterministic systems assumes static validation, while continuously retrained agentic policies violate that assumption by design.
- The paper proposes a four-layer framework, covering Policy, Engineering, Composition, and Systemic layers, with computable instantiations at each layer.
- A regret-covariance statistic detects policy drift from observed costs and decisions alone, without access to an agent's internal state.
- A calibrated crowding model shows joint drawdown probability rising from 39.2% to 79.3% as institutions converge on correlated exposures, with return correlation jumping from about 0.21 to 0.81 between calm and stress regimes.
- The framework draws on a case study of a deployed LLM-embedding trading strategy alongside a contemporaneous discretionary fund blowup.

## Excerpts

> "88% of surveyed finance professionals report no operational governance framework for agentic AI despite universal awareness of its deployment, and only 24 of 75 large U.S. money managers disclosing AI use in Form ADV filings report a formal governance policy."
> ~ Abstract

> "This gap is architectural, not cultural: governance built for deterministic systems assumes static validation. However, continuously retrained agentic policies violate static governance by design."
> ~ Abstract

> "A calibrated crowding model [shows] joint drawdown probability rising from 39.2% to 79.3% as institutions converge on correlated exposures."
> ~ Abstract

> "The framework is supported by a study of a deployed LLM-embedding trading strategy and a contemporaneous discretionary fund blowup."
> ~ Abstract

## Significance

- Supplies quantitative evidence, drawn from Form ADV disclosures, that formal agentic-AI governance remains rare among large US money managers, a load-bearing fact for the wiki's agentic-AI governance thread.
- Proposes a computable, model-free drift-detection statistic that regulators or risk teams could apply without vendor cooperation, relevant to any future supervisory approach to agentic trading systems.
- Quantifies systemic crowding risk from correlated agentic strategies, connecting the agentic-AI pillar to market-structure and systemic-risk concerns already present in the corpus.
- Complements TradeLens and other agentic-trading-viability papers already indexed by shifting the question from whether an agent is profitable to whether its governance is institutionally sound.

## Related

- [[10_Sources/Academia/arXiv-2607-10286-TradeLens-Agentic-Trading-Viability]] - companion study on whether LLM trading agents convert reasoning costs into profit, a related but distinct viability question
- [[10_Sources/Academia/arXiv-2607-08652-Formal-Mechanisms-Market-Stability-Agent-Societies]] - companion study on cooperation and stability mechanisms in LLM trading-agent societies
