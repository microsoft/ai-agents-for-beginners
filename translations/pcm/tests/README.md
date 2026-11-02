# Agent Smoke Tests

Dis folder dey hold **smoke-test catalogs** for di agents wey you build for di course.
Smoke test na cheap, fast check wey dey confirm say **deployed Microsoft Foundry hosted
agent** fit reachable, dey answer, and dey follow im basic prompt
expectations dem. Na first gate — e no be like full evaluation
pipeline wey you go learn for [Lesson 10](../10-ai-agents-production/README.md) and
[Lesson 16](../16-deploying-scalable-agents/README.md).

The catalogs dey use by [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action thru di [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
workflow.

## How to run

1. **Deploy the lesson's agent** go Microsoft Foundry as hosted agent (see
   Lesson 16 for di deployment workflow). Note di **agent name** and your
   **Foundry project endpoint**.
2. Add dis repository secrets (Settings → Secrets and variables → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Di federated
   identity need di **Azure AI User** role for **Foundry project scope**.
3. From di **Actions** tab, run **Smoke-test hosted agents** and choose di
   `tests_file` for di lesson, den supply di matching `agent_name` and
   `project_endpoint`.

## Catalog → lesson → agent name

| Catalog | Lesson | Deploy agent as |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Intro to AI Agents](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Tool Use](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Deploying Scalable Agents](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Which lessons get smoke tests?

Smoke tests dey apply to lessons wey you **deploy agent** wey im text replies fit
fit be checked against known content. Lessons wey dey conceptual, dey only run local,
or wey dem produce non-deterministic creative output no dey inside dis:

- **Lesson 17 (Creating Local AI Agents)** dey run fully for your workstation with
  Foundry Local and e no dey expose Foundry Responses endpoint, so this
  action no concern am. You fit test am by running di notebook locally.
- Design-pattern and theory lessons (02, 03, 06, 07, 09, 12) no get any deployable
  agent wey dem fit do smoke-test.

## Catalog schema (quick reference)

Each catalog na JSON document wey get top-level `tests` array. Each entry POSTs
one prompt and check di reply:

| Field | Meaning |
|-------|---------|
| `id` | Unique step identifier wey dem print for di log. |
| `description` | Human-readable purpose. |
| `prompt` | Di message wey dem send go di agent. |
| `assertions.status` | Di expected HTTP status (default na 200). |
| `assertions.contains_any` | Pass if di reply get any of dis substrings. |
| `assertions.contains_all` | Pass if di reply get every substring. |
| `assertions.contains_none` | Pass if di reply no get any of dis substrings. |
| `save_response_id_as` | Store di reply id for later multi-turn step. |
| `use_previous_response_id` | Send dis turn wey join to saved reply id. |

Assertions na case-insensitive substring checks. See di
[action documentation](https://github.com/marketplace/actions/ai-smoke-test) for
di full schema, including Foundry-managed conversation resources.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->