---
type: source
title: 'Agents that transact: Introducing Amazon Bedrock AgentCore Payments, built
  with Coinbase and Stripe'
authors:
- Amazon Web Services
organisation: Amazon Web Services
source_type: press-release
venue: AWS Machine Learning Blog
year: 2026
date_published: '2026-05-07'
url: https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/
doi: ''
jurisdiction:
- US
domain:
- agentic-ai
- settlement
- blockchain-settlement
- stablecoins
instrument:
- stablecoin-fiat
register_section: ''
nlm_id: ''
nlm_skip: false
status: draft
created: 2026-07-13
tags:
- source
- agentic-ai
- x402
- stablecoins
- AWS
- USDC
watchlist_channel: manual-backfill
topic:
- topic/agentic-ai
- topic/blockchain-settlement
- topic/finance/stablecoins
wiki_indexed: '2026-07-19T00:00:00Z'
wiki_hash: c4de7917255d91ae1b771806406bcc4e9ffa224628ac6f0b27f561805c8c70b3
wiki_role: wiki
---



# Agents that transact: Introducing Amazon Bedrock AgentCore Payments, built with Coinbase and Stripe

**Source:** [Amazon Web Services](https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/)

## Citation

Amazon Web Services. "Agents that transact: Introducing Amazon Bedrock AgentCore Payments, built with Coinbase and Stripe". AWS Machine Learning Blog, 7 May 2026. https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/.

## Annotation

Amazon Web Services launched Amazon Bedrock AgentCore Payments in preview on 7 May 2026. The feature lets an AI agent built on Bedrock pay for what it uses. An agent discovers, evaluates, and pays for APIs, Model Context Protocol (MCP) servers, web content, and other agents. No human wires up each billing relationship.

The payment layer runs on the x402 protocol, an open HTTP standard for machine-to-machine micropayments. An agent requests a paid resource and receives an HTTP 402 "Payment Required" response. The payment manager then authenticates the wallet, sends a stablecoin payment, and attaches proof. It returns the content inside the agent's reasoning loop.

Each agent holds a scoped, managed wallet. The developer picks a Coinbase CDP wallet or a Stripe Privy wallet at integration time. Settlement uses USDC on Base, an Ethereum layer-2 network. The developer never handles a private key. Settlement finalises in under two seconds at a cost near USD 0.0001 per transaction.

Governance rests with the end user. The user authorises the agent to use the wallet before any spending. Per-session spending limits cap each run. The agent holds no open-ended access to funds.

The launch moves x402 stablecoin settlement from a startup protocol into managed enterprise cloud. AWS built the feature with Coinbase and Stripe. It gives autonomous agents a settlement rail on a public blockchain. The design sets USDC as the default settlement asset for agent-to-agent commerce on tokenised rails.

## Concepts

- [[x402]] - the open HTTP 402 payment protocol the feature implements
- [[Bedrock-AgentCore]] - the Amazon Bedrock agent runtime that hosts the payment manager

## See also

- [[MOC - Agentic-AI]]
