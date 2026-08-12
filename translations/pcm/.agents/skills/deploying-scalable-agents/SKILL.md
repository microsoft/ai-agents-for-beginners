---
name: deploying-scalable-agents
license: MIT
description: 'Take one working agent prototype go scalable, observable production
  deployment for Microsoft Foundry. E cover deployment patterns (client-hosted, hosted
  agents, agent workflows), the agent lifecycle, model routing, response caching,
  evaluation gates, human-in-the-loop approval, observability with OpenTelemetry,
  cost optimisation, and smoke-testing deployed agents with the AI Smoke Test action.
  Based on Lesson 16 of AI Agents for Beginners. USE FOR: deploy one agent go production,
  scale one agent, Microsoft Foundry hosted agent, Foundry Agent Service, model routing,
  response caching, evaluation gate, release gate, human approval workflow, agent
  observability, agent tracing, agent cost optimisation, smoke test one hosted agent,
  production customer support agent. DO NOT USE FOR: building your first agent (start
  with Lesson 01), running agents locally on-device (use local-ai-agents / Lesson
  17), Azure infrastructure provisioning we no relate to agents, non-Foundry deployment
  targets.'
---
# Deploying Scalable Agents with Microsoft Foundry

> Companion skill for [Lesson 16 – Deploying Scalable Agents](../../../16-deploying-scalable-agents/README.md).
> Use am to help learner move agent from prototype go scalable, observable
> production deployment. Ground every recommendation inside lesson content and
> the runnable notebook; no make you invent Foundry APIs.

## Triggers

Activate dis skill when learner wan:
- Deploy agent to Microsoft Foundry as **hosted agent** and make am versioned/observable.
- Choose between **client-hosted, hosted-agent, and agent-workflow** deployment patterns.
- Add **model routing**, **response caching**, or **bounded concurrency** to control latency and cost.
- Add **evaluation gate** so bad agent version no fit ship.
- Add **human-in-the-loop approval** step for high-risk actions.
- Instrument agent wit **OpenTelemetry** tracing for production observability.
- **Smoke-test** deployed agent as quick post-deploy gate.

## Core mental model

Production agent na mostly operational skeleton *around* di model (~80%),
no be di model itself. Map every recommendation to one of dis concerns:

| Concern | Prototype → Production |
|---------|------------------------|
| Hosting | notebook → versioned hosted service |
| Identity | your `az login` → managed identity + scoped RBAC |
| State | in-memory → externalised thread/memory store |
| Failure | traceback → retries, fallbacks, alerts |
| Cost | "small small cents" → tracked, routed, cached, budgeted |
| Quality | eyeballing → automated evaluation gate |
| Trust | you approve → policy + human-in-the-loop |

## Deployment patterns (pick one, or combine)

1. **Client-hosted** — di reasoning loop dey run inside your process. Max control; you dey own scaling/state.
2. **Hosted agent (Foundry Agent Service)** — Foundry dey host the loop, dey store threads, dey enforce RBAC/content safety, dey show di agent for portal. Less control, far less operational wahala.
3. **Agent workflow** — multiple agents/tools join body as graph wit branching, approval nodes, and durable checkpoints.

## Lifecycle (di loop wey dey deliver agent)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Offline evaluation na gate, no be afterthought** — version no go ship
unless e clear di threshold. Online observability dey feed real failures back
enter di offline test set.

## Scaling and cost levers (priority order)

1. **Right-size di model** — use di smallest model wey fit pass di evaluation gate.
2. **Route by complexity** — small/fast model for simple requests, big model for real reasoning (DIY classifier or Foundry Model Router).
3. **Cache** — serve near-duplicate requests without model call.
4. **Stateless design + bounded concurrency** — externalise state; retry wit backoff.

## Key patterns wey dem suppose reproduce

Point learner to these from di notebook
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Request handler**: cache → route by complexity → trace span → run → cache.
- **Evaluation gate**: score offline test set; return `pass_rate >= threshold` and only deploy if true.
- **Human approval**: `@tool(approval_mode="always_require")` for actions like large refunds.
- **Tracing**: wrap each request inside `tracer.start_as_current_span(...)` and set attributes like `routed.model`, `customer.id`.

## Smoke-testing deployed agent

After deploy, make sure say endpoint really dey answer (green deploy fit still dey
silent). Use [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
action via [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
with catalog for [`tests/`](../../../tests/README.md). Runner dey POST each
prompt to `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
and e dey check the reply text. Identity need **Azure AI User** role at
Foundry project scope; token audience must be `https://ai.azure.com/`.

Combine di gates: **smoke test** (make sure e dey respond, every deploy) → **offline
evaluation** (good enough to ship before promotion) → **online evaluation** (how
e dey perform for real life, continuous).

## Enterprise controls

- **RBAC**: give every hosted agent managed identity with least privilege.
- **MCP for production**: treat every MCP server as untrusted boundary — pin version, scope identity, validate outputs, rate-limit, no ever expose secrets.

## Guardrails for the assistant

- Prefer di canonical `FoundryChatClient(...)` + `provider.as_agent(...)` pattern wey dem dey use for di whole course.
- No promise live-Azure results wey you never comfirm; recommend di smoke-test workflow to confirm deployment.
- Keep evaluation and cost advice together: evaluation set di quality floor, routing/caching keep cost near dat floor.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->