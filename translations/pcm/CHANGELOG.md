# Changelog

All big changes wey happen for **AI Agents for Beginners** course dey inside dis file.

## [Released] — 2026-07-14

Dis release move di course commot from two models wey dem don stop to use, move di remaining Lesson notebooks go di stable Microsoft Agent Framework API, plus check di Python notebooks with live Microsoft Foundry deployment.

### Changed

- **Move commot from deprecated models (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** Both `gpt-4.1` and `gpt-4.1-mini` don retire (dem go stop use am for **14 October 2026**). Change every place for di course (docs, `.env.example`, Python/.NET notebooks plus samples) to di new model `gpt-5-mini`. Lesson 16 model-routing example still dey show small and large as `gpt-5-nano` (small) and `gpt-5-mini` (large). Third-party files ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), historical GitHub Models text, and di `azure-openai-to-responses` skill's capability notes, dem no touch.
- **Lesson 14 handoff notebook move go stable API.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) now dey use `agent_framework.orchestrations.HandoffBuilder` with `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type` streaming, and `FoundryChatClient` (to replace di old pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent`).
- **Lesson 14 human-in-the-loop notebook move go stable API.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) now dey pause with `ctx.request_info(...)` + `@response_handler` (to replace di removed `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`), build with `WorkflowBuilder(start_executor=..., output_executors=[...])`, give structured output with `default_options={"response_format": ...}`, plus use scripted answer so notebook fit run without waiting for `input()`.
- **Environment config** ([.env.example](../../.env.example)): change model deployment names to `gpt-5-mini`; add `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (Lesson 16 routing) plus di one wey dem forget `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (Lesson 15 browser-use).
- **Dependencies** ([requirements.txt](../../requirements.txt)): pin `agent-framework`, `agent-framework-foundry`, and `agent-framework-openai` to `~=1.10.0` so everything go balance well (1.11.0 get experimental wahala wey fit affect dis lessons).

### Notes and known limitations

- **Check am well with live Microsoft Foundry.** Di Python notebooks run without UI (`nbconvert`) for Microsoft Foundry project using `gpt-5-mini` (and `gpt-5-nano` for Lesson 16 routing). Make sure you deploy same non-deprecated models for your own project; notebooks dey read deployment name from `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`.
- **Some lessons still need extra resources.** Lesson 05 need Azure AI Search; Lesson 08 Bing workflow (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) need Bing connection and Microsoft Foundry Agent Service tools; Lesson 13 (Cognee) and Lesson 17 (Foundry Local) need their own runtime environment.

## [Released] — 2026-07-13

Dis release add two new lessons wey complete di deployment story — making agents dey scale up to Microsoft Foundry and come down reach one single workstation — plus add smoke-test pipeline, update course navigation, new learner skills, and fresh branding.

### Added

- **Lesson 16 — Deploying Scalable Agents with Microsoft Foundry.** New lesson [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) plus runnable notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) wey build production customer-support agent (tools, RAG, memory, model routing, response caching, human approval, evaluation gate, and OpenTelemetry tracing), with development/deployment/runtime Mermaid diagrams, knowledge check, assignment, and challenge.
- **Lesson 17 — Creating Local AI Agents with Foundry Local and Qwen.** New lesson [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) and notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) wey build full engineering assistant on device (Qwen function calling with Foundry Local, sandbox file tools, local RAG with Chroma, optional local MCP), with local-only / local-RAG / tool-calling diagrams, knowledge check, assignment, and challenge.
- **Smoke-test pipeline.** New [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus per-lesson catalogs for deployable agents in Lessons 01, 04, 05, and 16, with index README weh map each catalog to im lesson and hosted-agent name. Lesson 16 get "Validating a Deployed Agent with Smoke Tests" section; Lessons 01/04/05 get optional smoke-test pointer.
- **Learner skills.** New Agent Skills under `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (include Lesson 16 and 17 guidance), and [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (how to check notebook samples against live Microsoft Foundry / Azure OpenAI).
- **Notebook validation runner.** New [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) wey run every Python notebook without UI using `nbconvert` and show PASS/FAIL matrix (plus `results.json`). It find repo root and Python by itself, avoid non-course notebooks (`.venv`, `site-packages`, `translations`, skill template assets) and `.NET` notebooks by default, plus support `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, and `-Python`.
- **Course navigation.** Add Previous/Next lesson links to Lessons 11–15 (wey before no get) so course go straight from 00 → 18 for both sides.
- **New thumbnails.** Lesson thumbnails for Lessons 16 and 17, plus fresh repository social image [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (now talk about the two new lessons and `aka.ms/ai-agents-beginners` URL).
- **Dependencies** ([requirements.txt](../../requirements.txt)): add `foundry-local-sdk` and `chromadb` for Lesson 17.

### Changed

- **Main [README.md](./README.md)** lesson table: Lessons 16 and 17 now link their content (before e be "Coming Soon"); repo image change go `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: add Lessons 16 and 17 to lesson-by-lesson guide and learning paths, plus "Validating Deployed Agents with Smoke Tests" section.
- **[AGENTS.md](./AGENTS.md)**: update lesson count/description (00–18), add smoke-testing validation section, add Lesson 16/17 sample-naming examples.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Previous Lesson" now point Lesson 17 (before e be Lesson 15), make chain complete.
- **Standardize model references on non-deprecated models.** Change all `gpt-4o` / `gpt-4o-mini` for course (docs, `.env.example`, Python/.NET notebooks plus samples) to `gpt-4.1-mini` — `gpt-4o` (all versions) dey retire for 2026. Lesson 16 model-routing example keep small/large difference as `gpt-4.1-mini` (small) and `gpt-4.1` (large). Python notebooks now dey select model from environment variables (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) instead of hard-coding model name.

### Notes and known limitations

- **No run live Azure.** New lessons notebooks na samples for learn; make you run and check dem with your own Microsoft Foundry / Foundry Local setup. Smoke-test workflow need make you deploy lesson agent and set Azure OIDC secrets (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) with **Azure AI User** role for Foundry project scope.
- **Lesson 17 na local only.** E no get Foundry Responses endpoint, so smoke-test no work; check am by running notebook for your own machine.

## [Released] — 2026-07-06

Dis release move course go **Azure OpenAI Responses API**, make product name standard for **Microsoft Foundry** and **Microsoft Agent Framework (MAF)**, retire GitHub Models, update SDK versions, and add new content on local models and hosting oda frameworks for Foundry.

### Added

- **Migration skill** — Install [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (from [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) under `.agents/skills/`, plus im references and scanner script.
- **Foundry Local (run models on-device)** — New "Alternative Provider: Foundry Local" section for [00-course-setup/README.md](./00-course-setup/README.md), cover install (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, and connect `FoundryLocalManager` to Microsoft Agent Framework with `OpenAIChatClient`.
- **Host LangChain / LangGraph agents for Microsoft Foundry** — New section for [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus runnable sample [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) using `langchain-azure-ai[hosting]` and `ResponsesHostServer` (for `/responses` protocol), based on [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — New "Real-World Example: Microsoft Project Opal" section for [15-browser-use/README.md](./15-browser-use/README.md) wey show Opal as enterprise computer-use agent plus relate am to course concepts (human-in-the-loop, trust/security, planning, Skills).
- **Second Lesson 02 Python sample** — Add [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (see "Changed" — move from previous Semantic Kernel notebook) and link am in lesson README.
- **Models and Providers** section add for [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Changed

- **Chat Completions → Responses API (Python).** Samples wey call model directly move from Chat Completions to Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), use `OpenAI` client with stable Azure OpenAI `/openai/v1/` endpoint (no `api_version`). Samples include:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — full tool-calling walkthrough (tool schema change to Responses format, tool results return as `function_call_output`, `max_output_tokens`, etc.).

- **GitHub Models → Azure OpenAI.** GitHub Models don stop to dey (retiring **July 2026**) and e no support Responses API. All GitHub Models code way dem get don turn to Azure OpenAI / Microsoft Foundry for Python and .NET samples:
  - Python: Lesson 08 workflow notebooks (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + companion `.md` docs, and the Lesson 08 dotNET workflow notebooks/`.md` (`01`–`03`) now use `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` with `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** The former `02-semantic-kernel.ipynb` don rewrite to use Microsoft Agent Framework with Azure OpenAI (Responses API) and dem rename am to `02-python-agent-framework-azure-openai.ipynb`.
- **Standardized on `FoundryChatClient` + `as_agent`.** README and notebook code wey dey reference `AzureAIProjectAgentProvider` dem don make am uniform with the main pattern wey Lesson 01 and the framework examples dey use: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` with `provider.as_agent(...)`. Dem update am for all Lesson 02–14 READMEs and notebooks (like Lesson 13 memory, all Lesson 14 notebooks, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Product naming.** Dem don change all the English content:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (No change: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", and environment-variable names.)
- **Dependencies** ([requirements.txt](../../requirements.txt)):
  - Dem pin `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Dem pin `openai>=1.108.1` (minimum for Responses API).
  - Dem remove `azure-ai-inference` (e dey only for the old GitHub Models samples).
- **Environment configuration** ([.env.example](../../.env.example)): dem commot all GitHub Models variables (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); add `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, and optional `AZURE_OPENAI_API_KEY`; dem update naming to Microsoft Foundry.
- **Docs** — Dem update [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), and [STUDY_GUIDE.md](./STUDY_GUIDE.md) for all these (setup env vars, verification snippet, provider guidance, naming).

### Removed

- Dem remove GitHub Models onboarding steps and environment variables from the setup docs (wey don replace with Azure OpenAI / Microsoft Foundry).

### Security / Privacy (public-sharing cleanup)

- Dem clear Jupyter notebook execution outputs wey leak real **Azure subscription ID**, resource-group / resource names, and Bing connection ID, plus developer **local file paths and usernames**, for these:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Dem verify say no API keys, tokens, subscription IDs, or personal paths dey among the English content wey dem track anymore (the `GITHUB_TOKEN` wey remain na GitHub Actions token wey dey in workflows and the GitHub MCP server PAT for Lesson 11 setup — both na legit and no get anything to do with GitHub Models).

### Notes and known limitations

- **Dem no run/compile am.** These samples na for learning, dem update them so dat API/naming go correct; dem never run dem with live Azure resources, and .NET samples no compile inside this environment. Abeg make you test am with your own Microsoft Foundry / Azure OpenAI deployment.
- **Model deployment suppose support Responses API.** Make you use deployment like `gpt-4.1-mini`, `gpt-4.1`, or `gpt-5.x` model. The old models fit do core Responses work but not every feature.
- **Agent-framework version.** The samples dey target the latest MAF (`>=1.10.0`). The normal way to create agent na `client.as_agent(...)`; Dem validate APIs against framework docs and installed build. If you dey use different version, make sure method dey (`as_agent` vs `create_agent`).
- **Lesson 08 workflow notebook 04** still dey use `AzureAIAgentClient` (from `agent-framework-azure-ai`) because e dey use Microsoft Foundry Agent Service hosted tools (Bing grounding, code interpreter); e already base for Responses.
- **.NET default deployment.** Two Lesson 08 dotNET workflow samples wey hard-code model before, dem don switch to use `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) as default. If sample need multimodal/vision input, put `AZURE_OPENAI_DEPLOYMENT` to better model.
- **Foundry Local** dey provide OpenAI-compatible **Chat Completions** endpoint and e dey meant for local development; make you use Azure OpenAI / Microsoft Foundry if you want full Responses API feature set.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->