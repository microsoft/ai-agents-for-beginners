---
name: local-ai-agents
description: >-
  Build local-first AI agents that run entirely on a developer workstation with
  Microsoft Foundry Local and Qwen function-calling models. Covers Small Language
  Models (SLMs), the OpenAI-compatible local endpoint, sandboxed local tools,
  local RAG with Chroma, local MCP servers, hybrid cloud/local routing, and the
  privacy/cost/offline trade-offs. Based on Lesson 17 of AI Agents for Beginners.
  USE FOR: run an agent locally, offline agent, on-device agent, Foundry Local,
  Qwen function calling, local tool calling, local RAG, Chroma vector database,
  local MCP server, privacy-preserving agent, hybrid local and cloud agent,
  small language model agent, engineering assistant on my machine.
  DO NOT USE FOR: deploying agents to the cloud at scale (use deploying-scalable-agents /
  Lesson 16), building your first agent concept (Lesson 01), Foundry (cloud) hosted
  agents, GPU cluster / server-side inference provisioning.
license: MIT
---

# Creating Local AI Agents with Foundry Local and Qwen

> Companion skill for [Lesson 17 – Creating Local AI Agents](../../../17-creating-local-ai-agents/README.md).
> Use it to help a learner build an agent that reasons, calls tools, and searches
> documentation entirely on their own machine — no cloud inference. Ground every
> recommendation in the lesson content and the runnable notebook.

## Triggers

Activate this skill when a learner wants to:
- Run an agent **fully on-device** for privacy, cost, or offline reasons.
- Serve a model locally with **Foundry Local** and connect via the OpenAI-compatible endpoint.
- Use a **Qwen function-calling** model to drive reliable local tool calls.
- Add **local RAG** (Chroma) or a **local MCP server**.
- Design a **hybrid** local/cloud routing strategy.

## Core mental model

An SLM trades breadth for privacy, cost, and offline operation. The winning
strategy: **let the SLM orchestrate and let tools do the heavy lifting.** The
model does not need to *know* the codebase — it needs to know when to call
`read_file` and `search_docs`. That plays to an SLM's strength (bounded decisions
like tool selection) and away from its weakness (broad knowledge, long multi-hop
reasoning).

## Why these specific pieces

- **Foundry Local** exposes an **OpenAI-compatible HTTP endpoint**, so cloud agent code transfers by changing only `base_url` (and using a local placeholder API key). It also auto-selects the best build (CPU/GPU/NPU) for the machine.
- **Qwen** models are trained for function calling and emit well-formed tool calls consistently — this is what turns a local *chat* model into a local *agent*.
- **Chroma** runs in-process and stores vectors on disk, so the whole RAG pipeline (embed → store → retrieve → reason) stays local.
- **MCP** is a transport, not a cloud service: an MCP server can run locally over `stdio`.

## Setup essentials

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # local placeholder
```

~8 GB RAM is a realistic minimum; a GPU/NPU helps but is not required.

## Key patterns to reproduce

Point the learner at the notebook
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Sandboxed tools**: every file tool resolves paths and rejects anything outside a single project root — even locally, a tool runs with the user's permissions.
- **Tool-calling loop**: register tools with the OpenAI tools schema, execute requested tools locally, feed results back, repeat until a final answer.
- **Local RAG**: upsert docs into a Chroma collection; `search_docs` returns top-k chunks.
- **Local MCP**: connect to a local server over `stdio`; scope it to a project directory and validate its outputs.

## Hybrid routing (local as one of the models)

| Situation | Where it runs |
|-----------|---------------|
| Sensitive data / offline | Local SLM |
| Simple, bounded task | Local SLM (cheap, fast) |
| Hard multi-hop reasoning on non-sensitive data | Cloud model |
| Cloud outage | Local SLM (graceful degradation) |

This mirrors the model-routing idea from Lesson 16, with the workstation as one
of the routes. Prefer designs that fall back to local so the agent degrades in
quality rather than failing outright.

## Guardrails for the assistant

- Keep every file/tool operation scoped to a sandboxed project directory.
- Do not send code or data to the cloud when the learner's stated goal is privacy/offline — keep the whole pipeline local.
- Set realistic expectations for SLM quality; lean on tools and RAG rather than the model's memorised knowledge.
- Note that Lesson 17 has **no** Foundry Responses endpoint, so the cloud smoke-test action does not apply — validate by running the notebook locally.
