---
type: source
title: Can Agentic Trading Systems Pay for Their Own Intelligence?
authors:
- Qiqi Duan
- Changlun Li
- Chen Wang
- Fan Zhang
- Mengxiang Wang
- Dayi Miao
- Peixian Ma
- Jiangpeng Yan
- Liyuan Chen
- Shuoling Liu
- Preslav Nakov
- Yuyu Luo
- Nan Tang
organisation: ''
source_type: paper
venue: arXiv (cs.AI, cs.MA)
year: 2026
date_published: '2026-07-11'
url: https://arxiv.org/abs/2607.10286
doi: 10.48550/arXiv.2607.10286
jurisdiction:
- INTL
domain:
- agentic-ai
- llm-trading
- finance
doctrine: []
instrument: []
register_section: ''
nlm_id: ''
nlm_skip: false
status: draft
created: 2026-07-19
tags:
- source
- agentic-ai
- llm-trading
- trading-agents
- evaluation
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/agentic-ai
- topic/finance
wiki_indexed: '2026-07-19T00:00:00Z'
wiki_hash: d218443af28f5ce986e9c00f44c4094daed8aa8d0f42c9fa4203ab2c037dbb79
wiki_role: wiki
---


# Can Agentic Trading Systems Pay for Their Own Intelligence?

## Citation

Duan, Qiqi, Changlun Li, Chen Wang, Fan Zhang, Mengxiang Wang, Dayi Miao, Peixian Ma, Jiangpeng Yan, Liyuan Chen, Shuoling Liu, Preslav Nakov, Yuyu Luo, and Nan Tang. "Can Agentic Trading Systems Pay for Their Own Intelligence?". arXiv:2607.10286 (cs.AI), 11 July 2026. https://arxiv.org/abs/2607.10286.

## One-line summary

The paper introduces TradeLens, a diagnostic toolkit that tests whether large language model trading agents convert their reasoning costs into measurable profit rather than merely ranking well on performance metrics.

## Key claims

- Large language model agents increasingly run trading systems, and their reasoning, tool use, and continual decisions incur costs expected to generate trading value.
- Existing evaluations report performance metrics but rarely test agentic viability, meaning whether dynamic LLM-mediated decisions convert their induced costs into incremental profit.
- TradeLens reconstructs trading trajectories from records, runtime traces, and deployment configurations, and attributes profit and cost to interpretable evidence.
- Viability hinges on intelligence-to-profit conversion rather than on capital scale, trading frequency, or architecture alone; those factors only amplify or degrade decision-attributed timing value.
- Backbone models fail in distinct ways: DeepSeek-V3.2 shows poor asset selection and GLM-4.7 shows negative timing.
- The findings reframe evaluation of LLM-based trading agents from capability-centric performance ranking toward trace-grounded diagnosis of whether an agent's intelligence pays for itself.

## Excerpts

> "Existing evaluations typically report performance metrics, but rarely examine agentic viability: whether dynamic LLM-mediated decisions convert their induced costs into measurable incremental profit."
> ~ Abstract

> "We introduce TradeLens, a trace-grounded diagnostic toolkit for evaluating agentic trading systems from their trading records, runtime traces, and deployment configurations. It reconstructs trading trajectories, attributes profit and cost to interpretable evidence, and diagnoses whether and why an agent pays for its own intelligence."
> ~ Abstract

> "Our results show that viability hinges on intelligence-to-profit conversion: models exhibit different failure patterns, such as poor asset selection in DeepSeek-V3.2 and negative timing in GLM-4.7, while capital scale, trading frequency, and architecture matter only by amplifying or degrading decision-attributed timing value."
> ~ Abstract

> "These findings reframe the evaluation of LLM-based trading agents from capability-centric performance ranking to trace-grounded diagnosis of intelligence-to-profit conversion."
> ~ Abstract

## Significance

- Supplies a reusable diagnostic method for testing whether autonomous trading agents are economically viable, not merely accurate, a distinct question from forecasting-calibration benchmarks already in the corpus.
- Names two specific backbone-model failure modes (asset selection, trade timing), giving the wiki concrete evidence for governance discussion of which LLM trading-agent failures matter operationally.
- Reinforces, from a different empirical angle than the Raven-Agent paper, that agentic-AI trading viability depends on the decision layer rather than on raw model capability or capital deployed.
- Open-sourced code gives the corpus a citable, reproducible benchmark for future comparison of agentic trading architectures.

## Related

- [[10_Sources/Academia/arXiv-2607-03015-Raven-Agent-Prediction-Market-Trading]] - companion study finding that a deterministic trading layer, not forecasting accuracy, drives profitable agentic trading
- [[10_Sources/Academia/arXiv-2607-08652-Formal-Mechanisms-Market-Stability-Agent-Societies]] - companion study on cooperation and stability mechanisms in LLM trading-agent societies
- [[10_Sources/Academia/arXiv-2607-05141-Square-Root-Price-Impact-Manipulation-Cycles]] - theoretical companion on manipulation risk in learning-agent markets
