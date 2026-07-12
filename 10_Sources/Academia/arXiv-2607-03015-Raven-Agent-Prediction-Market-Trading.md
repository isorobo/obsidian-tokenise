---
type: source
title: 'Beyond Forecasting: The Belief-to-Trade Layer in Prediction-Market Agents'
authors:
- Yishu Wang
- Yuxuan Wang
- Jiaqi Deng
- Hanyang Tang
organisation: ''
source_type: paper
venue: arXiv (cs.AI); ICML 2026 Workshop on AI Forecasting
year: 2026
date_published: '2026-07-03'
url: https://arxiv.org/abs/2607.03015
doi: 10.48550/arXiv.2607.03015
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
created: 2026-07-12
tags:
- source
- agentic-ai
- llm-trading
- prediction-markets
- autonomous-agents
- risk-management
watchlist_channel: arxiv-q-fin-rwa
topic:
- topic/agentic-ai
- topic/blockchain-settlement
wiki_indexed: '2026-07-12T00:00:00Z'
wiki_hash: 72e7bf8fef6d2b6f05986e254b4f0dc826b6e07ab22131c400d6d5afdc8913ba
wiki_role: wiki
---



# Beyond Forecasting: The Belief-to-Trade Layer in Prediction-Market Agents

## Citation

Wang, Yishu, Yuxuan Wang, Jiaqi Deng, and Hanyang Tang. "Beyond Forecasting: The Belief-to-Trade Layer in Prediction-Market Agents". arXiv:2607.03015 (cs.AI), 3 July 2026. https://arxiv.org/abs/2607.03015.

## One-line summary

The paper introduces Raven-Agent, described as the first autonomous trading agent for prediction markets, and shows that an explicit, deterministic trading layer of selection, sizing, and risk control drives positive returns even when the underlying forecaster is held fixed.

## Key claims

- Strong probability forecasts do not translate into profitable trades; prior work treats the trading rule as a fixed protocol rather than a designable object, leaving position sizing and risk control absent or expressed only as prompt instructions.
- Raven-Agent separates forecasting from trading into four modules: information collection, probability estimation, ranking and sizing, and execution and risk control, so any forecaster can be substituted without changing the trading layer.
- The ranking module scores candidates by a time-normalised expected return rather than raw probability edge, favouring short-resolution markets when edges are similar.
- The sizing module applies a quarter-Kelly fraction, and the execution module enforces deterministic caps on stake, exposure, stop loss, and drawdown outside the language model prompt.
- On a controlled replay of 42 to 58 archived Polymarket decisions, Raven-Agent (full) is the only tested policy with a positive return on stake (+15.9%) and the only one with a positive risk-adjusted return.
- Sizing by edge without selection is actively harmful: an edge-proportional baseline loses 55.5% of stake, far worse than flat sizing at negative 10.7%, showing that selection and risk filtering are necessary complements to informed sizing.
- In live Polymarket deployment across 20 predictions, Raven-Agent held $251.01 in open positions and accumulated $53.92 in cumulative profit.

## Excerpts

> "We propose Raven-Agent, to the best of our knowledge, the first autonomous trading agent for prediction markets. On a controlled replay over an archived decision set, our architecture achieves the only positive return and the only positive risk-adjusted return among all tested policies."
> ~ Abstract

> "A useful trading layer should be explicit and modular, with selection, sizing, and risk control as separate components. It should be deterministic, so that risk constraints remain in effect even when the model is confidently wrong."
> ~ §1, Introduction

> "The Edge-proportional policy shows that sizing alone, without selection, is harmful: concentrating capital on confidently wrong high-edge predictions amplifies losses to −55.5% ROI, far worse than flat sizing (−10.7%)."
> ~ §4.2, Result Analysis

> "Prior work shows that prompt-level risk guidance is unreliable under end-to-end LLM control, and that optimizing prediction accuracy can reduce trading return when the objective is misaligned. Keeping these checks outside the prompt avoids that failure mode."
> ~ §3.4, Execution and risk

## Significance

- Gives the wiki a concrete, code-released architecture for autonomous agentic-AI trading, directly evidencing the agentic-AI trading pillar of the wiki-tokenise corpus.
- Demonstrates empirically that deterministic, off-prompt risk control outperforms prompt-based risk guidance, a finding relevant to any governance framework for autonomous trading agents.
- Shows that forecasting accuracy and trading profitability are distinct capabilities, cautioning against treating LLM calibration benchmarks as a proxy for safe autonomous financial decision-making.
- Documents live-money deployment on Polymarket, evidencing that agentic-AI trading has moved from simulation to real capital allocation on public prediction-market infrastructure.

## Related

- [[10_Sources/Academia/arXiv-Agent-Economy-Blockchain-Foundation]] - blockchain-based foundation for autonomous AI agent finance
- [[10_Sources/Academia/arXiv-2607-08652-Formal-Mechanisms-Market-Stability-Agent-Societies]] - companion study on LLM agent behaviour and stability in simulated markets
- [[10_Sources/Academia/arXiv-2607-05141-Square-Root-Price-Impact-Manipulation-Cycles]] - learning-agent market dynamics and manipulation risk in algorithmic trading
