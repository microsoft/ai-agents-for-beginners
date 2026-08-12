# Agent Smoke Tests

This folder holds **smoke-test catalogs** for the agents you build in the course.
A smoke test is a cheap, fast check that a **deployed Microsoft Foundry hosted
agent** is reachable, responding, and following its most basic prompt
expectations. It is a first gate — not a replacement for the full evaluation
pipeline you learn in [Lesson 10](../10-ai-agents-production/README.md) and
[Lesson 16](../16-deploying-scalable-agents/README.md).

The catalogs are consumed by the [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action via the [`.github/workflows/smoke-test.yml`](../.github/workflows/smoke-test.yml)
workflow.

## How to run

1. **Deploy the lesson's agent** to Microsoft Foundry as a hosted agent (see
   Lesson 16 for the deployment workflow). Note the **agent name** and your
   **Foundry project endpoint**.
2. Add these repository secrets (Settings → Secrets and variables → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. The federated
   identity needs the **Azure AI User** role at **Foundry project scope**.
3. From the **Actions** tab, run **Smoke-test hosted agents** and choose the
   `tests_file` for the lesson, then supply the matching `agent_name` and
   `project_endpoint`.

## Catalog → lesson → agent name

| Catalog | Lesson | Deploy agent as |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](./lesson-01-smoke-tests.json) | [01 – Intro to AI Agents](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](./lesson-04-smoke-tests.json) | [04 – Tool Use](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](./lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](./lesson-16-smoke-tests.json) | [16 – Deploying Scalable Agents](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Which lessons have smoke tests?

Smoke tests apply to lessons where you **deploy an agent** whose text replies can
be asserted against known content. Lessons that are conceptual, run only locally,
or produce non-deterministic creative output are intentionally excluded:

- **Lesson 17 (Creating Local AI Agents)** runs entirely on your workstation with
  Foundry Local and does **not** expose a Foundry Responses endpoint, so this
  action does not apply. Validate it by running the notebook locally.
- Design-pattern and theory lessons (02, 03, 06, 07, 09, 12) do not ship a single
  deployable agent to smoke-test.

## Catalog schema (quick reference)

Each catalog is a JSON document with a top-level `tests` array. Each entry POSTs
one prompt and asserts on the reply:

| Field | Meaning |
|-------|---------|
| `id` | Unique step identifier printed in the log. |
| `description` | Human-readable purpose. |
| `prompt` | The message sent to the agent. |
| `assertions.status` | Expected HTTP status (default 200). |
| `assertions.contains_any` | Pass if the reply contains any of these substrings. |
| `assertions.contains_all` | Pass if the reply contains every substring. |
| `assertions.contains_none` | Pass if the reply contains none of these substrings. |
| `save_response_id_as` | Store the reply id for a later multi-turn step. |
| `use_previous_response_id` | Send this turn chained to a saved reply id. |

Assertions are case-insensitive substring checks. See the
[action documentation](https://github.com/marketplace/actions/ai-smoke-test) for
the full schema, including Foundry-managed conversation resources.
