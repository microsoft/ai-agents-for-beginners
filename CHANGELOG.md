# Changelog

All notable changes to the **AI Agents for Beginners** course are documented in this file.

## [Released] — 2026-07-14

This release moves the course off two newly-deprecated models, migrates the remaining Lesson notebooks to the stable Microsoft Agent Framework API, and validates the Python notebooks against a live Microsoft Foundry deployment.

### Changed

- **Moved off deprecated models (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Both `gpt-4.1` and `gpt-4.1-mini` are now deprecated (published retirement date **14 October 2026**). Replaced every course reference (docs, `.env.example`, Python/.NET notebooks and samples) with the non-deprecated `gpt-5-mini`. Lesson 16's model-routing example keeps a small/large contrast using `gpt-5-nano` (small) and `gpt-5-mini` (large). Vendored third-party files ([15-browser-use/llms.txt](./15-browser-use/llms.txt)), historical GitHub Models text, and the `azure-openai-to-responses` skill's capability notes were intentionally left unchanged.
- **Lesson 14 handoff notebook migrated to the stable API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) now uses `agent_framework.orchestrations.HandoffBuilder` with `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type`-based streaming, and `FoundryChatClient` (replacing the removed pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` symbols).
- **Lesson 14 human-in-the-loop notebook migrated to the stable API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) now pauses via `ctx.request_info(...)` + `@response_handler` (replacing the removed `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), builds with `WorkflowBuilder(start_executor=..., output_executors=[...])`, drives structured output through `default_options={"response_format": ...}`, and uses a scripted answer so the notebook runs unattended (no blocking `input()`).
- **Environment configuration** ([.env.example](./.env.example)): switched the model deployment names to `gpt-5-mini`; added `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (Lesson 16 routing) and the previously-missing `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (Lesson 15 browser-use).
- **Dependencies** ([requirements.txt](./requirements.txt)): pinned `agent-framework`, `agent-framework-foundry`, and `agent-framework-openai` to `~=1.10.0` for a self-consistent, validated set (1.11.0 ships experimental breaking changes to the surfaces these lessons use).

### Notes and known limitations

- **Validated against live Microsoft Foundry.** The Python notebooks were executed headlessly with `nbconvert` against a Microsoft Foundry project using `gpt-5-mini` (and `gpt-5-nano` for Lesson 16 routing). Deploy equivalent non-deprecated models in your own project; the notebooks read the deployment name from `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Still requires extra resources for some lessons.** Lesson 05 needs Azure AI Search; the Lesson 08 Bing-grounding workflow (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) needs a Bing connection and Microsoft Foundry Agent Service hosted tools; Lesson 13 (Cognee) and Lesson 17 (Foundry Local) need their own runtimes.

## [Released] — 2026-07-13

This release adds two new lessons that complete the deployment arc — scaling agents up to Microsoft Foundry and down to a single workstation — plus a smoke-test pipeline, refreshed course navigation, new learner skills, and updated branding.

### Added

- **Lesson 16 — Deploying Scalable Agents with Microsoft Foundry.** New lesson [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) and runnable notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) building a production customer-support agent (tools, RAG, memory, model routing, response caching, human approval, an evaluation gate, and OpenTelemetry tracing), with development/deployment/runtime Mermaid diagrams, a knowledge check, an assignment, and a challenge.
- **Lesson 17 — Creating Local AI Agents with Foundry Local and Qwen.** New lesson [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) and notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) building a fully on-device engineering assistant (Qwen function calling via Foundry Local, sandboxed file tools, local RAG with Chroma, optional local MCP), with local-only / local-RAG / tool-calling diagrams, a knowledge check, an assignment, and a challenge.
- **Smoke-test pipeline.** New [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](./.github/workflows/smoke-test.yml) plus per-lesson catalogs under [tests/](./tests/README.md) for the deployable agents in Lessons 01, 04, 05, and 16, with an index README mapping each catalog to its lesson and hosted-agent name. Lesson 16 gains a "Validating a Deployed Agent with Smoke Tests" section; Lessons 01/04/05 gain an optional smoke-test pointer.
- **Learner skills.** New Agent Skills under `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (packaging the Lesson 16 and 17 guidance), and [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (how to validate the notebook samples against a live Microsoft Foundry / Azure OpenAI setup).
- **Notebook validation runner.** New [scripts/validate-notebooks.ps1](./scripts/validate-notebooks.ps1) that executes every Python notebook headlessly with `nbconvert` and prints a PASS/FAIL matrix (plus `results.json`). It auto-detects the repo root and Python, excludes non-course notebooks (`.venv`, `site-packages`, `translations`, skill template assets) and `.NET` notebooks by default, and supports `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, and `-Python`.
- **Course navigation.** Added Previous/Next lesson links to Lessons 11–15 (previously missing) so the whole course chains 00 → 18 in both directions.
- **New thumbnails.** Lesson thumbnails for Lessons 16 and 17, plus a refreshed repository social image [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (now advertising the two new lessons and the `aka.ms/ai-agents-beginners` URL).
- **Dependencies** ([requirements.txt](./requirements.txt)): added `foundry-local-sdk` and `chromadb` for Lesson 17.

### Changed

- **Main [README.md](./README.md)** lesson table: Lessons 16 and 17 now link to their content (previously "Coming Soon"); repository image bumped to `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: added Lessons 16 and 17 to the lesson-by-lesson guide and learning paths, and a "Validating Deployed Agents with Smoke Tests" section.
- **[AGENTS.md](./AGENTS.md)**: updated the lesson count/description (00–18), added a smoke-testing validation section, and added Lesson 16/17 sample-naming examples.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Previous Lesson" now points to Lesson 17 (was Lesson 15), closing the chain.
- **Standardized model references on non-deprecated models.** Replaced all `gpt-4o` / `gpt-4o-mini` references across the course (docs, `.env.example`, Python/.NET notebooks and samples) with `gpt-4.1-mini` — `gpt-4o` (all versions) is retiring in 2026. Lesson 16's model-routing example keeps a small/large contrast using `gpt-4.1-mini` (small) and `gpt-4.1` (large). Python notebooks now select the model from environment variables (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) instead of hard-coding a model name.

### Notes and known limitations

- **Not executed against live Azure.** The new lessons' notebooks are educational samples; run and validate them against your own Microsoft Foundry / Foundry Local setup. The smoke-test workflow requires you to deploy the lesson's agent and configure Azure OIDC secrets (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) with the **Azure AI User** role at Foundry project scope.
- **Lesson 17 is local-only.** It has no Foundry Responses endpoint, so the smoke-test action does not apply; validate it by running the notebook on your workstation.

## [Released] — 2026-07-06

This release migrates the course to the **Azure OpenAI Responses API**, standardizes product naming on **Microsoft Foundry** and the **Microsoft Agent Framework (MAF)**, retires GitHub Models, updates SDK versions, and adds new content on local models and hosting other frameworks on Foundry.

### Added

- **Migration skill** — Installed the [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (from [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) under `.agents/skills/`, including its references and scanner script.
- **Foundry Local (run models on-device)** — New "Alternative Provider: Foundry Local" section in [00-course-setup/README.md](./00-course-setup/README.md) covering install (`winget` / `brew`), `foundry model run`, the `foundry-local-sdk`, and wiring `FoundryLocalManager` to the Microsoft Agent Framework via `OpenAIChatClient`.
- **Hosting LangChain / LangGraph agents on Microsoft Foundry** — New section in [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus a runnable sample [14-langchain-hosted-agent.py](./14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) using `langchain-azure-ai[hosting]` and `ResponsesHostServer` (the `/responses` protocol), based on [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — New "Real-World Example: Microsoft Project Opal" section in [15-browser-use/README.md](./15-browser-use/README.md) framing Opal as an enterprise computer-use agent and mapping it to course concepts (human-in-the-loop, trust/security, planning, Skills).
- **Second Lesson 02 Python sample** — Added [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (see "Changed" — migrated from the former Semantic Kernel notebook) and linked it in the lesson README.
- **Models and Providers** section added to [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Changed

- **Chat Completions → Responses API (Python).** Samples that called the model directly were migrated from Chat Completions to the Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), using the `OpenAI` client against the stable Azure OpenAI `/openai/v1/` endpoint (no `api_version`). Affected samples include:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — the full function-calling walkthrough (tool schema flattened to the Responses format, tool results returned as `function_call_output`, `max_output_tokens`, etc.).
- **GitHub Models → Azure OpenAI.** GitHub Models is deprecated (retiring **July 2026**) and does not support the Responses API. All GitHub Models code paths were converted to Azure OpenAI / Microsoft Foundry across Python and .NET samples:
  - Python: Lesson 08 workflow notebooks (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + companion `.md` docs, and the Lesson 08 dotNET workflow notebooks/`.md` (`01`–`03`) now use `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` with `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** The former `02-semantic-kernel.ipynb` was rewritten to use the Microsoft Agent Framework with Azure OpenAI (Responses API) and renamed to `02-python-agent-framework-azure-openai.ipynb`.
- **Standardized on `FoundryChatClient` + `as_agent`.** README and notebook code that referenced `AzureAIProjectAgentProvider` were standardized on the canonical pattern used by Lesson 01 and the framework's own samples: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` with `provider.as_agent(...)`. Updated across the Lesson 02–14 READMEs and notebooks (e.g., Lesson 13 memory, all Lesson 14 notebooks, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Product naming.** Renamed throughout the English content:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Unchanged: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", and environment-variable names.)
- **Dependencies** ([requirements.txt](./requirements.txt)):
  - Pinned `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Pinned `openai>=1.108.1` (minimum for the Responses API).
  - Removed `azure-ai-inference` (was only used by the migrated GitHub Models samples).
- **Environment configuration** ([.env.example](./.env.example)): removed the GitHub Models variables (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); added `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, and optional `AZURE_OPENAI_API_KEY`; updated naming to Microsoft Foundry.
- **Docs** — Updated [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), and [STUDY_GUIDE.md](./STUDY_GUIDE.md) for the above (setup env vars, verification snippet, provider guidance, naming).

### Removed

- GitHub Models onboarding steps and environment variables from the setup docs (superseded by Azure OpenAI / Microsoft Foundry).

### Security / Privacy (public-sharing cleanup)

- Cleared Jupyter notebook execution outputs that leaked a real **Azure subscription ID**, resource-group / resource names, and Bing connection ID, plus developer **local file paths and usernames**, in:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Verified no API keys, tokens, subscription IDs, or personal paths remain in the tracked English content (the `GITHUB_TOKEN` references that remain are the GitHub Actions token in workflows and the GitHub MCP server PAT in Lesson 11 setup — both legitimate and unrelated to GitHub Models).

### Notes and known limitations

- **Not executed/compiled.** These are educational samples updated for API/naming correctness; they were not run against live Azure resources, and the .NET samples were not compiled in this environment. Validate against your own Microsoft Foundry / Azure OpenAI deployment.
- **Model deployment must support the Responses API.** Use a deployment such as `gpt-4.1-mini`, `gpt-4.1`, or a `gpt-5.x` model. Older models support core Responses functionality but not every feature.
- **Agent-framework version.** The samples target the latest MAF (`>=1.10.0`). The canonical agent-creation call is `client.as_agent(...)`; APIs were validated against the framework's published docs and an installed build. If you pin a different version, confirm method availability (`as_agent` vs `create_agent`).
- **Lesson 08 workflow notebook 04** intentionally keeps `AzureAIAgentClient` (from `agent-framework-azure-ai`) because it uses Microsoft Foundry Agent Service hosted tools (Bing grounding, code interpreter); it is already Responses-based.
- **.NET default deployment.** Two Lesson 08 dotNET workflow samples previously hard-coded a specific model; they now default to `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`). If a sample relies on multimodal/vision input, set `AZURE_OPENAI_DEPLOYMENT` to a suitable model.
- **Foundry Local** exposes an OpenAI-compatible **Chat Completions** endpoint and is intended for local development; use Azure OpenAI / Microsoft Foundry for the full Responses API feature set.
