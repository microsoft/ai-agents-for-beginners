---
name: local-ai-agents
license: MIT
description: 'Build local-first AI agents wey dey run fully for developer workstation
  wit Microsoft Foundry Local and Qwen function-calling models. E cover Small Language
  Models (SLMs), the OpenAI-compatible local endpoint, sandboxed local tools, local
  RAG wit Chroma, local MCP servers, hybrid cloud/local routing, and di privacy/cost/offline
  trade-offs. E based on Lesson 17 of AI Agents for Beginners. USE FOR: run agent
  locally, offline agent, on-device agent, Foundry Local, Qwen function calling, local
  tool calling, local RAG, Chroma vector database, local MCP server, privacy-preserving
  agent, hybrid local and cloud agent, small language model agent, engineering assistant
  for my machine. DO NOT USE FOR: deploying agents to di cloud at scale (use deploying-scalable-agents
  / Lesson 16), building your first agent concept (Lesson 01), Foundry (cloud) hosted
  agents, GPU cluster / server-side inference provisioning.'
---
# How to Create Local AI Agents wit Foundry Local and Qwen

> Skill wey go help for [Lesson 17 – Creating Local AI Agents](../../../17-creating-local-ai-agents/README.md).
> Use am to help person wey dey learn build agent wey sabi reason, dey call tools, and dey search
> documentation all na inside dem machine — no cloud inference. Make every
> recommendation stand gidigba for lesson content and the runnable notebook.

## Triggers

Activate this skill when person wey dey learn want:
- Run agent **fully inside device** for privacy, cost, or offline reasons.
- Serve model locally with **Foundry Local** and connect via the OpenAI-compatible endpoint.
- Use **Qwen function-calling** model to make local tool calls correct.
- Add **local RAG** (Chroma) or **local MCP server**.
- Design **hybrid** local/cloud routing way.

## Core mental model

Small Language Model (SLM) dey trade wide knowledge for privacy, cost, and offline work. The best
way: **make the SLM dey organize and make tools carry the heavy work.** The
model no need to *know* the codebase — e need to know wen to call
`read_file` and `search_docs`. Dis one dey play to SLM strength (small decisions
like tool choice) and avoid hin weakness (big knowledge, long multi-hop
reasoning).

## Why these specific pieces

- **Foundry Local** get **OpenAI-compatible HTTP endpoint**, so cloud agent code fit transfer by just changing `base_url` (and using local fake API key). E also dey choose best build (CPU/GPU/NPU) for machine.
- **Qwen** models get epp to call functions and always dey give correct tool calls — na dis one make local *chat* model become local *agent*.
- **Chroma** dey run inside process and dey store vectors for disk, so all RAG work (embed → store → retrieve → reason) remains local.
- **MCP** na transport, no be cloud service: MCP server fit run local with `stdio`.

## Setup essentials

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # lokal plassholder
```

About 8 GB RAM na minimum wey make sense; GPU/NPU fit help but dem no mandatory.

## Key patterns wey you fit repeat

Show the learner the notebook
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Sandboxed tools**: every file tool dey resolve paths and no allow anything wey dey outside one project root — even if na local, tool dey run wit user permissions.
- **Tool-calling loop**: register tools with OpenAI tools schema, run requested tools locally, give the results back, keep am up till final answer.
- **Local RAG**: put docs inside Chroma collection; `search_docs` go return top-k chunks.
- **Local MCP**: connect to local server thru `stdio`; scope am to project directory and check outputs well.

## Hybrid routing (local as one of the models)

| Situation | Where e dey run |
|-----------|---------------|
| Sensitive data / offline | Local SLM |
| Simple, bounded task | Local SLM (cheap, fast) |
| Hard multi-hop reasoning on non-sensitive data | Cloud model |
| Cloud outage | Local SLM (graceful degradation) |

Dis one dey mirror di model-routing idea from Lesson 16, with workstation as one
of di routes. Make you like designs wey fit fall back to local so agent go degrade in
quality, no be just fail completely.

## Guardrails for the assistant

- Keep every file/tool work confined to sandboxed project directory.
- No send code or data go cloud when the learner talk say na privacy/offline e wan — keep everything local.
- Set correct expectations for SLM quality; rely on tools and RAG, no be the model memorized knowledge.
- Note say Lesson 17 no get **Foundry Responses** endpoint, so cloud smoke-test ka no go work — make sure by running notebook local.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->