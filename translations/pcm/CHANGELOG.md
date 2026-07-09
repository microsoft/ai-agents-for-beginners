# Changelog

All di important changes wey happen for **AI Agents for Beginners** course dey inside dis file.

## [Unreleased] — 2026-07-06

Dis release don move di course go **Azure OpenAI Responses API**, standardize di product name for **Microsoft Foundry** and **Microsoft Agent Framework (MAF)**, retire GitHub Models, upgrade SDK versions, plus add new content on local models and how to host oda frameworks for Foundry.

### Added

- **Migration skill** — Install di [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) Agent Skill (from [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) for `.agents/skills/`, including di references and di scanner script.
- **Foundry Local (run models on-device)** — New "Alternative Provider: Foundry Local" section inside [00-course-setup/README.md](./00-course-setup/README.md) wey cover how to install (`winget` / `brew`), `foundry model run`, di `foundry-local-sdk`, and how to connect `FoundryLocalManager` to Microsoft Agent Framework through `OpenAIChatClient`.
- **Hosting LangChain / LangGraph agents on Microsoft Foundry** — New section for [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) plus runnable sample [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) wey use `langchain-azure-ai[hosting]` and `ResponsesHostServer` (di `/responses` protocol), based on [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).
- **Microsoft Project Opal** — New "Real-World Example: Microsoft Project Opal" section inside [15-browser-use/README.md](./15-browser-use/README.md) wey talk about Opal as enterprise computer-use agent and how e relate to course concepts (human-in-the-loop, trust/security, planning, Skills).
- **Second Lesson 02 Python sample** — Add [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) (check "Changed" — e migrate from di old Semantic Kernel notebook) plus e join am for di lesson README.
- **Models and Providers** section add for [STUDY_GUIDE.md](./STUDY_GUIDE.md).

### Changed

- **Chat Completions → Responses API (Python).** Di samples wey dey talk directly to di model don change from Chat Completions to Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`), using di `OpenAI` client for Azure OpenAI `/openai/v1/` endpoint (no `api_version`). Di samples wey e affect na:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — full walkthrough for function-calling (tool schema flatten go Responses format, tool results return as `function_call_output`, `max_output_tokens`, etc.).
- **GitHub Models → Azure OpenAI.** GitHub Models don old now (retiring **July 2026**) and e no support the Responses API. All GitHub Models code paths don change go Azure OpenAI / Microsoft Foundry for Python and .NET samples:
  - Python: Lesson 08 workflow notebooks (`01`–`03`), Lesson 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` plus di `.md` docs, plus di Lesson 08 dotNET workflow notebooks/`.md` (`01`–`03`) now use `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` with `AzureCliCredential`.
- **Semantic Kernel → Microsoft Agent Framework.** Di old `02-semantic-kernel.ipynb` get rewrite to use Microsoft Agent Framework with Azure OpenAI (Responses API) and di name change to `02-python-agent-framework-azure-openai.ipynb`.
- **Standardize on `FoundryChatClient` + `as_agent`.** README and notebook code wey dem dey call `AzureAIProjectAgentProvider` don standardize for di normal way wey Lesson 01 and di framework own samples use am: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` with `provider.as_agent(...)`. E don update for all README and notebooks from Lesson 02–14 (like Lesson 13 memory, all Lesson 14 notebooks, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **Product naming.** Di English content rename am like dis:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (Still the same: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", and environment-variable names.)
- **Dependencies** ([requirements.txt](../../requirements.txt)):
  - Pinned `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - Pinned `openai>=1.108.1` (minimum for Responses API).
  - Remove `azure-ai-inference` (na only di migrated GitHub Models samples dey use am before).
- **Environment configuration** ([.env.example](../../.env.example)): remove di GitHub Models environment variables (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`); add `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, plus optional `AZURE_OPENAI_API_KEY`; update di names for Microsoft Foundry.
- **Docs** — Update [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), plus [STUDY_GUIDE.md](./STUDY_GUIDE.md) for all dis (setup env vars, verification snippet, provider guidance, naming).

### Removed

- Remove GitHub Models onboarding steps plus environment variables from di setup docs (replace with Azure OpenAI / Microsoft Foundry).

### Security / Privacy (public-sharing cleanup)

- Clear Jupyter notebook execution outputs wey leak real **Azure subscription ID**, resource-group / resource names, and Bing connection ID, plus developer **local file paths and usernames**, for:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- Confirm say no API keys, tokens, subscription IDs, or personal paths dey inside di tracked English content (di `GITHUB_TOKEN` wey remain na di GitHub Actions token wey dey workflows and di GitHub MCP server PAT for Lesson 11 setup — both legit and no relate to GitHub Models).

### Notes and known limitations

- **No run/compile.** Dis na educational samples wey dem update to correct API/naming; dem no run am for live Azure resources, and .NET samples no compile for this environment. Make you test am for your own Microsoft Foundry / Azure OpenAI setup.
- **Model deployment suppose support Responses API.** Use deployment like `gpt-4o-mini`, `gpt-4.1`, or `gpt-5.x` model. Old models fit core Responses work but no get all di features.
- **Agent-framework version.** Samples target di newest MAF (`>=1.10.0`). Di normal agent-create call na `client.as_agent(...)`; APIs don check against di framework docs and installed build. If you use different version, make sure method dey (`as_agent` vs `create_agent`).
- **Lesson 08 workflow notebook 04** intentionally keep `AzureAIAgentClient` (from `agent-framework-azure-ai`) because e use Microsoft Foundry Agent Service hosted tools (Bing grounding, code interpreter); e don already dey Responses-based.
- **.NET default deployment.** Two Lesson 08 dotNET workflow samples before hard-code `gpt-4o`; now dem default to `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`). If sample need multimodal/vision input, set `AZURE_OPENAI_DEPLOYMENT` to model wey fit.
- **Foundry Local** get OpenAI-compatible **Chat Completions** endpoint and e meant for local development; for full Responses API features, use Azure OpenAI / Microsoft Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->