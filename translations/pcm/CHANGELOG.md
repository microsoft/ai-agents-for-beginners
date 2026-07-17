# Changelog

Ol notable changes dem wey happen for **AI Agents for Beginners** course dey inside dis file.

## [Released] — 2026-07-13

Dis release add two new lessons wey complete di deployment journey — to scale agents reach Microsoft Foundry and also to shrink am down to one workstation — plus one smoke-test pipeline, refreshed course navigation, new learner skills, and updated branding.

### Added

- **Lesson 16 — Deploying Scalable Agents with Microsoft Foundry.** New lesson [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) plus one runnable notebook [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) wey dey build production customer-support agent (tools, RAG, memory, model routing, response caching, human approval, one evaluation gate, plus OpenTelemetry tracing), with development/deployment/runtime Mermaid diagrams, knowledge check, assignment, and challenge.
- **Lesson 17 — Creating Local AI Agents with Foundry Local and Qwen.** New lesson [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) plus notebook [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) wey dey build fully on-device engineering assistant (Qwen function calling via Foundry Local, sandbox file tools, local RAG with Chroma, optional local MCP), with local-only / local-RAG / tool-calling diagrams, knowledge check, assignment, and challenge.
- **Smoke-test pipeline.** New [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) workflow [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) plus per-lesson catalogs under [tests/](./tests/README.md) for deployable agents inside Lessons 01, 04, 05, and 16, with index README wey link each catalog to its lesson and hosted-agent name. Lesson 16 get "Validating a Deployed Agent with Smoke Tests" section; Lessons 01/04/05 get optional smoke-test pointer.
- **Learner skills.** New Agent Skills under `.agents/skills/`: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (wey package Lesson 16 and 17 guidance), and [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (wey teach how to validate notebook samples against live Microsoft Foundry / Azure OpenAI setup).
- **Notebook validation runner.** New [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) wey dey run every Python notebook headlessly with `nbconvert` and dey print PASS/FAIL matrix (plus `results.json`). E auto-detect repo root and Python, exclude non-course notebooks (`.venv`, `site-packages`, `translations`, skill template assets) plus `.NET` notebooks by default, and support `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, and `-Python`.
- **Course navigation.** Added Previous/Next lesson links to Lessons 11–15 (wey never get am before) so whole course go connect 00 → 18 for both directions.
- **New thumbnails.** Lesson thumbnails for Lessons 16 and 17, plus refreshed repo social image [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (now dey advertise the two new lessons and `aka.ms/ai-agents-beginners` URL).
- **Dependencies** ([requirements.txt](../../requirements.txt)): added `foundry-local-sdk` and `chromadb` for Lesson 17.

### Changed

- **Main [README.md](./README.md)** lesson table: Lessons 16 and 17 now dey link to their content (before e be "Coming Soon"); repo image updated to `repo-thumbnailv3.png`.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: added Lessons 16 and 17 to lesson-by-lesson guide and learning paths, plus "Validating Deployed Agents with Smoke Tests" section.
- **[AGENTS.md](./AGENTS.md)**: updated lesson count/description (00–18), add smoke-testing validation section, plus Lesson 16/17 sample-naming examples.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "Previous Lesson" dey point to Lesson 17 now (before e be Lesson 15), close the chain.
- **Standardized model references on non-deprecated models.** Replace all `gpt-4o` / `gpt-4o-mini` references for the course (docs, `.env.example`, Python/.NET notebooks and samples) with `gpt-4.1-mini` — `gpt-4o` (all versions) go retire for 2026. Lesson 16's model-routing example still get small/large contrast using `gpt-4.1-mini` (small) and `gpt-4.1` (large). Python notebooks now dey select model from env variables (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) instead of hard-coding model name.

### Notes and known limitations

- **No run for live Azure.** New lessons' notebooks na educational samples; make you run and validate am against your own Microsoft Foundry / Foundry Local setup. The smoke-test workflow need say you must deploy lesson agent and configure Azure OIDC secrets (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) with **Azure AI User** role for Foundry project scope.
- **Lesson 17 na local only.** E no get Foundry Responses endpoint, so the smoke-test action no work for am; validate by running the notebook for your workstation.

## [Released] — 2026-07-06

Dis release migrate di course go the **Azure OpenAI Responses API**, standardize product naming on **Microsoft Foundry** and **Microsoft Agent Framework (MAF)**, retire GitHub Models, update SDK versions, plus add new content on local models and how to host other frameworks on Foundry.

### Added

- **Migration skill** — Installed the [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (from [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) under `.agents/skills/`, plus its references and scanner script.
- **Foundry Local (run models on-device)** — New "Alternative Provider: Foundry Local" section inside [00-course-setup/README.md](./00-course-setup/README.md) wey cover install (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, plus how to wire `FoundryLocalManager` to Microsoft Agent Framework with `OpenAIChatClient`.
- **Hosting LangChain / LangGraph agents on Microsoft Foundry** — New section for [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus runnable sample [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) wey use `langchain-azure-ai[hosting]` and `ResponsesHostServer` (the `/responses` protocol), based on [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — New "Real-World Example: Microsoft Project Opal" section for [15-browser-use/README.md](./15-browser-use/README.md) wey show Opal as enterprise computer-use agent plus map am to course concepts (human-in-the-loop, trust/security, planning, Skills).
- **Second Lesson 02 Python sample** — Added [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (see "Changed" — migrate from old Semantic Kernel notebook) and link am in lesson README.
- **Models and Providers** section added inside [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Changed

- **Chat Completions → Responses API (Python).** Samples wey dey call model direct migrate from Chat Completions to Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), using `OpenAI` client against stable Azure OpenAI `/openai/v1/` endpoint (no `api_version`). Samples wey change include:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — full function-calling walkthrough (tool schema flatten comot go Responses format, tool results return as `function_call_output`, `max_output_tokens`, and others).
- **GitHub Models → Azure OpenAI.** GitHub Models don dey deprecated (go retire **July 2026**) and e no support Responses API. All GitHub Models code paths convert go Azure OpenAI / Microsoft Foundry inside Python and .NET samples:
  - Python: Lesson 08 workflow notebooks (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + companion `.md` docs, plus Lesson 08 dotNET workflow notebooks/`.md` (`01`–`03`) now use `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` with `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Old `02-semantic-kernel.ipynb` rewrite to use Microsoft Agent Framework with Azure OpenAI (Responses API) and rename to `02-python-agent-framework-azure-openai.ipynb`.
- **Standardized on `FoundryChatClient` + `as_agent`.** README and notebook code wey dey reference `AzureAIProjectAgentProvider` standardize on di canonical pattern wey Lesson 01 and framework's own samples dey use: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` with `provider.as_agent(...)`. Update inside Lesson 02–14 READMEs and notebooks (e.g., Lesson 13 memory, all Lesson 14 notebooks, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Product naming.** Rename for all English content:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (No change: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", plus environment variables names.)
- **Dependencies** ([requirements.txt](../../requirements.txt)):
  - Pin `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Pin `openai>=1.108.1` (minimum for Responses API).
  - Remove `azure-ai-inference` (only used for migrated GitHub Models samples).
- **Environment configuration** ([.env.example](../../.env.example)): remove GitHub Models variables (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); add `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, plus optional `AZURE_OPENAI_API_KEY`; update naming to Microsoft Foundry.
- **Docs** — Update [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), and [STUDY_GUIDE.md](./STUDY_GUIDE.md) for dis updates (setup env vars, verification snippet, provider guidance, naming).

### Removed

- GitHub Models onboarding steps and environment vars remove from setup docs (replace with Azure OpenAI / Microsoft Foundry).

### Security / Privacy (public-sharing cleanup)

- Clear Jupyter notebook execution outputs wey leak real **Azure subscription ID**, resource-group / resource names, and Bing connection ID, plus developer **local file paths and usernames**, for:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`

  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- We don check say no API keys, tokens, subscription IDs, or personal paths dey inside the tracked English content (di `GITHUB_TOKEN` dem wey remain na di GitHub Actions token for workflows and di GitHub MCP server PAT for Lesson 11 setup — both na correct and no relate to GitHub Models).

### Notes and known limitations

- **Dem never run/compile am.** Na educational samples wey dem update for API/naming correctness; dem no run am for live Azure resources, and di .NET samples no compile for this environment. Make you check am well with your own Microsoft Foundry / Azure OpenAI deployment.
- **Model deployment must support di Responses API.** Make you use deployment like `gpt-4.1-mini`, `gpt-4.1`, or `gpt-5.x` model. Old models dey support core Responses work but no get every feature.
- **Agent-framework version.** Di samples dem dey target di latest MAF (`>=1.10.0`). Di correct agent-creation call na `client.as_agent(...)`; APIs dem check against di framework published docs and di installed build. If you use another version, make sure di method dey like `as_agent` or `create_agent`.
- **Lesson 08 workflow notebook 04** purposely keep `AzureAIAgentClient` (from `agent-framework-azure-ai`) because e dey use Microsoft Foundry Agent Service hosted tools (Bing grounding, code interpreter); e don already base for Responses.
- **.NET default deployment.** Two Lesson 08 dotNET workflow samples wey before dem hard-code one model; now dem use `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) as default. If any sample rely on multimodal/vision input, make you set `AZURE_OPENAI_DEPLOYMENT` to the correct model.
- **Foundry Local** dey show OpenAI-compatible **Chat Completions** endpoint and e mean for local development; make you use Azure OpenAI / Microsoft Foundry if you want full Responses API feature set.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->