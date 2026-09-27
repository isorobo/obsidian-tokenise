---
type: source
title: Governing Agentic AI in FinTech
authors:
- Henry Han
organisation: ''
source_type: paper
venue: arXiv (cs.CY, cs.AI, q-fin.RM)
year: 2026
date_published: '2026-08-11'
url: https://arxiv.org/abs/2608.11344
doi: 10.48550/arXiv.2608.11344
jurisdiction:
- INTL
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
created: 2026-08-17
tags:
- source
- agentic-ai
- ai-governance
- verifiability
- reproducibility
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/agentic-ai
- topic/finance
wiki_indexed: '2026-08-17T00:00:00Z'
wiki_hash: 730e4af9c6219019661384e1983e27ef4d5a168cae92eb540d3c42387b047207
wiki_role: wiki
---


# Governing Agentic AI in FinTech

## Citation

Han, Henry. "Governing Agentic AI in FinTech". arXiv:2608.11344 (cs.CY), 11 August 2026, updated 13 August 2026. https://arxiv.org/abs/2608.11344.

## One-line summary

The paper defines the Verifiability Gap in agentic-AI governance and shows across nine model versions that provider updates and orchestration choices, not model capability, break audit reproducibility.

## Key claims

- Financial institutions are delegating consequential decisions to agentic AI systems that decompose goals, coordinate models and tools, and act with little oversight.
- The paper argues the binding governance constraint is verifiability, not capability, and defines the Verifiability Gap as the shortfall between the verification delegated authority demands and the explainability retained after a decision.
- Study 1 shows provider releases alter historical financial actions, and that replay controls belong to the provider: the frontier model tested rejects temperature, top_p, and top_k settings outright and exposes no random seed.
- Under the tightest controls each endpoint allows, a local model reproduced 320 of 320 executions, while hosted models reproduced 319 of 320 and 959 of 960.
- Study 2 shows orchestration is a latent policy layer, since architecture changes final actions and no execution record repeated in any configuration at any scale tested.
- Study 3 shows two deterministic credit-model versions each reproduce their own current action perfectly, yet the current version cannot recover a historical one.
- The paper concludes that authority is defensible only while retained evidence substantiates its exercise, and that the framework extends beyond finance to other high-stakes domains.

## Excerpts

> "Financial institutions are delegating consequential decisions to agentic AI systems that decompose goals, coordinate models and tools, and act with little oversight."
> ~ Abstract

> "We argue the binding governance constraint is not capability but verifiability. We define the Verifiability Gap as the shortfall between the verification delegated authority demands and the explainability and reproducibility retained after a decision."
> ~ Abstract

> "Capability buys a higher starting point, not auditability."
> ~ Abstract

> "We conceptualize reproducibility as a governance profile, not a scalar, yielding evidence-contingent delegation: authority is defensible only while retained evidence substantiates its exercise."
> ~ Abstract

## Significance

- Introduces the Verifiability Gap as a named construct that distinguishes model capability from governable auditability, directly relevant to any supervisory standard for agentic trading or advisory systems.
- Provides empirical reproducibility figures, from 320 of 320 down to markedly lower hosted-model parity, that quantify how provider-side model updates erode the audit trail regulators would rely on.
- Shows orchestration architecture, not just the underlying model, drives non-reproducible outcomes, a finding load-bearing for any institutional-readiness or runtime-governance framework already indexed.
- Extends the wiki's agentic-AI governance thread from disclosure gaps and runtime controls to the deeper problem of retrospective verifiability itself.

## Related

- [[10_Sources/Academia/arXiv-2608-02311-AI-Governance-Institutional-Readiness-Finance]] - companion paper documenting the disclosure-based governance gap that this paper's verifiability framework helps explain
- [[10_Sources/Academia/arXiv-2608-09025-SAGE-Fin-Runtime-Governance-Financial-Agents]] - companion paper offering a runtime-control mechanism that this paper's evidence-contingent delegation concept would evaluate
