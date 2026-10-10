---
type: source
title: 'StableEval Arena: A Cost-Aware Agentic Benchmark for Stablecoin Price Stability Prediction'
authors:
- Sean Wan
- Dongping Liu
- Luyao Zhang
organisation: arXiv
source_type: paper
venue: arXiv (cs.LG)
year: 2026
date_published: '2026-08-07'
url: https://arxiv.org/abs/2609.18949
doi: '10.48550/arXiv.2609.18949'
jurisdiction:
- INTL
domain:
- stablecoins
- agentic-ai
- llm-trading
doctrine: []
instrument:
- stablecoin-fiat
register_section: ''
status: draft
created: 2026-10-11
tags:
- source
- stablecoins
- depeg
- llm-agents
- benchmark
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/finance/stablecoins
- topic/agentic-ai
wiki_indexed: '2026-10-10T17:43:28Z'
wiki_hash: 504414b2cd8a314f1d8418198fac7ef557015f06ea4c29140bac47d7d08bb761
wiki_role: wiki
---

# StableEval Arena: A Cost-Aware Agentic Benchmark for Stablecoin Price Stability Prediction

## Citation

Wan, Sean; Liu, Dongping; Zhang, Luyao. "StableEval Arena: A Cost-Aware Agentic Benchmark for Stablecoin Price Stability Prediction". arXiv (cs.LG), 7 August 2026. https://arxiv.org/abs/2609.18949.

## One-line summary

A benchmark scores LLM-backed agents on diagnosing stablecoin peg stress and forecasting seven-day peg deviations, finding they produce valid outputs cheaply but miss most severe depeg cases.

## Key claims

- StableEval Arena is a cost-aware benchmark framework for evaluating agentic AI systems on stablecoin price stability.
- Agents diagnose peg stress and forecast deviations from the one-dollar peg over a hidden seven-day horizon, using leakage-safe historical replay of exchange price-volume data.
- Six agent configurations plus baselines are evaluated on a 120-case stress-enriched set and a 507-case natural-distribution set.
- The framework measures prediction quality, calibration, structured-output reliability, latency, token use and estimated cost.
- Trustworthiness is treated as a joint property, not accuracy alone.
- Agents reliably produce valid structured outputs at modest cost but still miss most rare severe-stress and sustained-depeg cases.
- The dataset is released on Hugging Face and the code on GitHub.

## Excerpts

> "We introduce StableEval Arena, a cost-aware benchmark framework for evaluating agentic AI systems"
> ~ Abstract

> "Rather than ranking agents by accuracy alone, the framework treats trustworthiness as a joint property"
> ~ Abstract

> "agents reliably produce valid structured outputs at modest measured cost"
> ~ Abstract

## Significance

- Links the vault's stablecoin and agentic-AI themes: it tests whether AI agents can supervise or anticipate peg stress.
- The finding that agents miss severe depegs cautions against relying on them for stablecoin risk monitoring.
- Read from the arXiv abstract page and API record only; the full text was not reviewed. The listing shows a 7 August 2026 submission date under a 2609 identifier.

## Related

- [[10_Sources/Academia/arXiv-2608-09378-Stablecoin-Transaction-Scaling-Laws-Ethereum]] - empirical stablecoin transaction evidence.
- [[10_Sources/Academia/arXiv-2607-10286-TradeLens-Agentic-Trading-Viability]] - agentic trading evaluation.
- [[10_Sources/Academia/arXiv-2607-08524-Stablecoins-Under-Stress-Austrian-CASPs]] - stablecoin behaviour under stress.
