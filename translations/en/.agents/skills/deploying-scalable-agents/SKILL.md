---
name: deploying-scalable-agents
license: MIT
description: 'Take a working agent prototype to a scalable, observable production
  deployment on Microsoft Foundry. Covers deployment patterns (client-hosted, hosted
  agents, agent workflows), the agent lifecycle, model routing, response caching,
  evaluation gates, human-in-the-loop approval, observability with OpenTelemetry,
  cost optimisation, and smoke-testing deployed agents with the AI Smoke Test action.
  Based on Lesson 16 of AI Agents for Beginners. USE FOR: deploy an agent to production,
  scale an agent, Microsoft Foundry hosted agent, Foundry Agent Service, model routing,
  response caching, evaluation gate, release gate, human approval workflow, agent
  observability, agent tracing, agent cost optimisation, smoke test a hosted agent,
  production customer support agent. DO NOT USE FOR: building your first agent (start
  with Lesson 01), running agents locally on-device (use local-ai-agents / Lesson
  17), Azure infrastructure provisioning unrelated to agents, non-Foundry deployment
  targets.'
---
# Deploying Scalable Agents with Microsoft Foundry

> Companion skill for [Lesson 16 – Deploying Scalable Agents](../../../16-deploying-scalable-agents/README.md).
> Use it to help a learner move an agent from prototype to a scalable, observable
> production deployment. Ground every recommendation in the lesson content and
> the runnable notebook; do not invent Foundry APIs.

## Triggers

Activate this skill when a learner wants to:
- Deploy an agent to Microsoft Foundry as a **hosted agent** and make it versioned/observable.
- Choose between **client-hosted, hosted-agent, and agent-workflow** deployment patterns.
- Add **model routing**, **response caching**, or **bounded concurrency** to control latency and cost.
- Add an **evaluation gate** so a bad agent version cannot ship.
- Add a **human-in-the-loop approval** step for high-risk actions.
- Instrument an agent with **OpenTelemetry** tracing for production observability.
- **Smoke-test** a deployed agent as a fast post-deploy gate.

## Core mental model

A production agent is mostly the operational skeleton *around* the model (~80%),
not the model itself. Map every recommendation to one of these concerns:

| Concern | Prototype → Production |
|---------|------------------------|
| Hosting | notebook → versioned hosted service |
| Identity | your `az login` → managed identity + scoped RBAC |
| State | in-memory → externalised thread/memory store |
| Failure | traceback → retries, fallbacks, alerts |
| Cost | "a few cents" → tracked, routed, cached, budgeted |
| Quality | eyeballing → automated evaluation gate |
| Trust | you approve → policy + human-in-the-loop |

## Deployment patterns (pick one, or combine)

1. **Client-hosted** — the reasoning loop runs in your process. Max control; you own scaling/state.
2. **Hosted agent (Foundry Agent Service)** — Foundry hosts the loop, stores threads, enforces RBAC/content safety, shows the agent in the portal. Less control, far less operational surface.
3. **Agent workflow** — multiple agents/tools composed into a graph with branching, approval nodes, and durable checkpoints.

## Lifecycle (the loop that ships an agent)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Offline evaluation is a gate, not an afterthought** — a version does not ship
unless it clears the threshold. Online observability feeds real failures back
into the offline test set.

## Scaling and cost levers (in priority order)

1. **Right-size the model** — use the smallest model that passes the evaluation gate.
2. **Route by complexity** — small/fast model for simple requests, large model for real reasoning (DIY classifier or Foundry Model Router).
3. **Cache** — serve near-duplicate requests without a model call.
4. **Stateless design + bounded concurrency** — externalise state; retry with backoff.

## Key patterns to reproduce

Point the learner at these from the notebook
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Request handler**: cache → route by complexity → trace span → run → cache.
- **Evaluation gate**: score an offline test set; return `pass_rate >= threshold` and only deploy if true.
- **Human approval**: `@tool(approval_mode="always_require")` for actions like large refunds.
- **Tracing**: wrap each request in `tracer.start_as_current_span(...)` and set attributes like `routed.model`, `customer.id`.

## Smoke-testing a deployed agent

After deploy, verify the endpoint actually answers (a green deploy can still be
silent). Use the [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
action via [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
with the catalog in [`tests/`](../../../tests/README.md). The runner POSTs each
prompt to `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
and asserts on the reply text. The identity needs the **Azure AI User** role at
Foundry project scope; the token audience must be `https://ai.azure.com/`.

Layer the gates: **smoke test** (reachable/responding, every deploy) → **offline
evaluation** (good enough to ship, before promotion) → **online evaluation** (how
is it doing in the wild, continuous).

## Enterprise controls

- **RBAC**: give each hosted agent a managed identity with least privilege.
- **MCP in production**: treat every MCP server as an untrusted boundary — pin the version, scope its identity, validate outputs, rate-limit, never expose secrets.

## Guardrails for the assistant

- Prefer the canonical `FoundryChatClient(...)` + `provider.as_agent(...)` pattern used across the course.
- Do not promise live-Azure results you have not verified; recommend the smoke-test workflow to confirm a deployment.
- Keep evaluation and cost advice tied together: evaluation sets the quality floor, routing/caching keep cost near that floor.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->