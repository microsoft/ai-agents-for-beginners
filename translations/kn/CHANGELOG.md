# ಬದಲಾವಣೆ ಸಂಕಲನ

**ಸುರುಳಿ ಮಾಡಬಹುದಾದ ಏಜೆಂಟ್‌ಗಳ ಕೋರ್ಸ್**ಗೆ ಸಂಬಂಧಿಸಿದ ಎಲ್ಲ ಗಮನಾರ್ಹ ಬದಲಾವಣೆಗಳನ್ನು ಈ ಕಡತದಲ್ಲಿ ದಾಖಲಿಸಲಾಗಿದೆ.

## [ವಿಡ್ದಿಳದ] — 2026-07-06

ಈ ಬಿಡುಗಡೆಯು ಕೋರ್ಸ್ ಅನ್ನು **ಅಜೂರ್ ಓಪನ್ಏಐ ಪ್ರತಿಕ್ರಿಯೆಗಳ API**ಗೆ ಸ್ಥಳಾಂತರಿಸುತ್ತದೆ, **ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ** ಮತ್ತು **ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ (MAF)** ಮೇಲೆ ಉತ್ಪನ್ನದ ಹೆಸರುಗಳನ್ನು ಒಂದೇಸರಿಗೊಳಿಸುತ್ತದೆ, ಗಿಟ್‌ಹಬ್ ಮಾದರಿಗಳನ್ನು ನಿರ್ಗಮಿಸುತ್ತದೆ, SDK ಆವೃತ್ತೆಗಳನ್ನು ನವೀಕರಿಸುತ್ತದೆ, ಮತ್ತು ಸ್ಥಳೀಯ ಮಾದರಿಗಳು ಮತ್ತು ಫೌಂಡ್ರಿಯಲ್ಲಿ ಇತರ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳ ಹೋಸ್ಟ್‌ಗಾಗಿ ಹೊಸ ವಿಷಯವನ್ನು ಸೇರಿಸುತ್ತದೆ.

### ಸೇರಿಸಲಾಗಿದೆ

- **ಸ್ಥಲಾಂತರ ಪರಿಣತಿ** — `.agents/skills/`ಕೆಳಗೆ [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) ಏಜೆಂಟ್ ಸ್ಕಿಲ್‌ನ್ನು (ನಡೆದು [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) સ્થાપಿಸಲಾಗಿದೆ, ಅದರ ಉಲ್ಲೇಖಗಳು ಮತ್ತು ಸ್ಕ್ಯಾನರ್ ಸ್ಕ್ರಿಪ್ಟ್ ಸಹಿತ.
- **ಫೌಂಡ್ರಿ ಲೋಕಲ್ (ಒಳ ਵਰ್ತನೆ ಮೇಲೆ ಮಾದರಿಗಳನ್ನು ಚಾಲನೆ ಮಾಡಿದರೆ)** — [00-course-setup/README.md](./00-course-setup/README.md) ನಲ್ಲಿ ಹೊಸ "ಪರ್ಯಾಯ ಪೂರೈಕೆದಾರ: ಫೌಂಡ್ರಿ ಸ್ಥಳೀಯ" ವಿಭಾಗ, ಸ್ಥಾಪನೆ (`winget` / `brew`), `foundry model run`, `foundry-local-sdk` ಮತ್ತು `FoundryLocalManager` ಅನ್ನು Microsoft Agent Frameworkಗೆ `OpenAIChatClient` ಮೂಲಕ ಸಂಪರ್ಕಿಸುವ ಬಗ್ಗೆ.
- **ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯಲ್ಲಿ ಲಾಂಗ್‌ಚೇನ್ / ಲಾಂಗ್‌ಗ್ರಾಫ್ ಏಜೆಂಟ್‌ಗಳ ಹೋಸ್ಟಿಂಗ್** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) ನಲ್ಲಿ ಹೊಸ ವಿಭಾಗ ಮತ್ತು `langchain-azure-ai[hosting]` ಮತ್ತು `ResponsesHostServer` ( `/responses` ಪ್ರೋಟೋಕಾಲ್) ಬಳಸಿ ರನೆಬಲ್ ಮಾದರಿ [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py), [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) ಆಧಾರಿತ.
- **ಮೈಕ್ರೋಸಾಫ್ಟ್ ಪ್ರಾಜೆಕ್ಟ್ ಓಪಲ್** — [15-browser-use/README.md](./15-browser-use/README.md) ನಲ್ಲಿ ಹೊಸ "ನಿಜಜೀವನ ಉದಾಹರಣೆ: ಮೈಕ್ರೋಸಾಫ್ಟ್ ಪ್ರಾಜೆಕ್ಟ್ ಓಪಲ್" ವಿಭಾಗ, ಓಪಲ್ ಅನ್ನು ಎಂಟರ್‌ಪ್ರೈಸ್ ಕಂಪ್ಯೂಟರ್-ಉಪಯೋಗ ಏಜೆಂಟ್ ಆಗಿ ಮತ್ತು ಕೋರ್ಸ್ ಧಾರಣೆಗಳಿಗೆ (ಮಾನವರು ಚಕ್ರವೃಂದದಲ್ಲಿ, ನಂಬಿಕೆ/ಭದ್ರತೆ, ಯೋಜನೆ, ಕೌಶಲ್ಯಗಳು) ನಕ್ಷೆಬದ್ಧ ಮಾಡುವುದಾಗಿ.
- **ಎರಡನೆಯ ಪಾಠ 02 ಪೈಥಾನ್ ಮಾದರಿ** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) ಸೇರಿಸಲಾಗಿದೆ ("ಬದಲಾವಣೆ" ನೋಡಿ — ಹಳೆಯ ಸಿಮೆಂಟಿಕ್ ಕರ್ಣಲ ನೋಟ್ಬುಕ್‌ನಿಂದ ಸ್ಥಳಾಂತರಿಸಲಾಗಿದೆ) ಮತ್ತು ಪಾಠದ READMEನಲ್ಲಿ ಲಿಂಕ್ ಮಾಡಲಾಗಿದೆ.
- [STUDY_GUIDE.md](./STUDY_GUIDE.md) ಗೆ **ಮಾದರಿಗಳು ಮತ್ತು ಪೂರೈಕೆದಾರರು** ವಿಭಾಗ ಸೇರಿಸಲಾಗಿದೆ.

### ಬದಲಾವಣೆಯಾಗಿದೆ

- **ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸು → ಪ್ರತಿಕ್ರಿಯೆಗಳ API (ಪೈಥಾನ್).** ಮಾದರಿಯನ್ನು ನೇರವಾಗಿ ಕರೆಮಾಡಿದ ಮಾದರಿಗಳು ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವುದರಿಂದ ಪ್ರತಿಕ್ರಿಯೆಗಳ APIಗೆ (`client.responses.create(input=..., store=False)`, `resp.output_text`) ಸ್ಥಳಾಂತರಗೊಂಡಿವೆ, `OpenAI` ಕ್ಲೈಂಟ್ ಬಳಸಿ ಸ್ಥಿರ ಅಜೂರ್ ಓಪನ್ಏಐ `/openai/v1/` ಎಂಡ್‌ಪಾಯಿಂಟ್‌ನ ವಿರುದ್ಧ (ಯಾವುದೂ `api_version` ಇಲ್ಲ). ಅದಕ್ಕೆ ಸಂಬಂಧಿತ ಮಾದರಿಗಳು:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — ಸಂಪೂರ್ಣ ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್ ಹಾದಿ (ಟೂಲ್ ಸ್ಕೀಮಾ ಪ್ರತಿಕ್ರಿಯೆಗಳ ವಿನ್ಯಾಸಕ್ಕೆ ಸರಳೀಕೃತ, ಟೂಲ್ ಫಲಿತಾಂಶಗಳು `function_call_output`, `max_output_tokens` ಮುಂತಾದವುಗಳಾಗಿ ಹಿಂತಿರುಗಿಸಿದ).
- **ಗಿಟ್‌ಹಬ್ ಮಾದರಿಗಳು → ಅಜೂರ್ ಓಪನ್ಏಐ.** ಗಿಟ್‌ಹಬ್ ಮಾದರಿಗಳು ನಿಷ್ಕಾಸಿತವಾಗಿವೆ(**ಜುಲೈ 2026** ನಿವೃತ್ತಿ), ಪ್ರತಿಕ್ರಿಯೆಗಳ APIಗೆ ಬೆಂಬಲವಿಲ್ಲ. ಎಲ್ಲಾ ಗಿಟ್‌ಹಬ್ ಮಾದರಿ ಕೋಡ್ ಮಾರ್ಗಗಳನ್ನು ಪೈಥಾನ್ ಮತ್ತು .ನೇಟ್ ಮಾದರಿಗಳಿಗೆ ಅಜೂರ್ ಓಪನ್ಏಐ / ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಗೆ ಪರಿವರ್ತಿಸಲಾಗಿದೆ:
  - ಪೈಥಾನ್: ಪಾಠ 08 ವರ್ಕ್ಫ್ಲೋ ನೋಟ್ಬುಕ್‌ಗಳು (`01`–`03`), ಪಾಠ 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .ನೆಟ್: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + ಸಂಗಡ `.md` ದಸ್ತಾವೇಜುಗಳು, ಮತ್ತು ಪಾಠ 08 ಡಾಟ್‌ನೆಟ್ ವರ್ಕ್ಫ್ಲೋ ನೋಟ್ಬುಕ್‌ಗಳು/`.md`ಗಳು (`01`–`03`) ಈಗ `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` ಅನ್ನು `AzureCliCredential` ಬಳಸಿ ಬಳಸುತ್ತವೆ.
- **ಸಿಮೆಂಟಿಕ್ ಕರ್ಣಲ → ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್.** ಹಳೆಯ `02-semantic-kernel.ipynb` ಅನ್ನು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್ವರ್ಕ್ ಮತ್ತು ಅಜೂರ್ ಓಪನ್ಏಐ (ಪ್ರತಿಕ್ರಿಯೆಗಳ API) ಬಳಸಿ ಮರುಬರೆದಿದ್ದು `02-python-agent-framework-azure-openai.ipynb` ಎಂದು ಮರುನಾಮಕರಿಸಲಾಗಿದೆ.
- **`FoundryChatClient` + `as_agent` ಯಲ್ಲಿ ಸ್ಟ್ಯಾಂಡರ್ಡೈಸ್ ಮಾಡಲಾಗಿದೆ.** README ಮತ್ತು ನೋಟ್ಬುಕ್ ಕೋಡ್‌ನಲ್ಲಿ `AzureAIProjectAgentProvider` ಉಲ್ಲೇಖವನ್ನು ಪಾಠ 01 ಮತ್ತು ಫ್ರೇಮ್ವರ್ಕ್ ನ ಸ್ವಂತ ಮಾದರಿಗಳಲ್ಲಿ ಬಳಸಿ ಬಂದ ಮಾನದಂಡದ ಮಾದರಿ `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` ಅನ್ನು `provider.as_agent(...)` ಮೂಲಕ ಬಳಕೆ ಮಾಡಲಾಗಿದೆ. ಪಾಠ 02–14 READMEs ಮತ್ತು ನೋಟ್ಬುಕ್‌ಗಳಲ್ಲಿ ನವೀಕರಿಸಲಾಗಿದೆ (ಉದಾ: ಪಾಠ 13 ಮೆಮರಿ, ಎಲ್ಲಾ ಪಾಠ 14 ನೋಟ್ಬುಕ್‌ಗಳು, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **ಉತ್ಪನ್ನದ ಹೆಸರು.** ಇಂಗ್ಲಿಷ್ ವಿಷಯದಲ್ಲಿ ಹೀಗಾಗಿ ಮರುನಾಮಕರಣ ಮಾಡಲಾಗಿದೆ:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (ಬದಲಾಗಿಲ್ಲ: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", ಮತ್ತು ಪರಿಸರ-ಚರ ಸುರಕ್ಷತಾ ಹೆಸರುಗಳು.)
- **ನಿರ್ಭರತೆಗಳು** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` ಪಿನ್ ಮಾಡಲಾಗಿದೆ.
  - `openai>=1.108.1` (ಪ್ರತಿಕ್ರಿಯೆಗಳ APIಗೆ ಕನಿಷ್ಠ) ಪಿನ್ ಮಾಡಲಾಗಿದೆ.
  - `azure-ai-inference` (ಹಳೆಯ ಗಿಟ್‌ಹಬ್ ಮಾದರಿ ಮಾದರಿಗಳಿಂದ ಮಾತ್ರ ಬಳಸುತ್ತಿದ್ದವು) ತೆಗೆದುಹಾಕಲಾಗಿದೆ.
- **ಪರಿಸರ ಸಂರಚನೆ** ([.env.example](../../.env.example)): ಗಿಟ್‌ಹಬ್ ಮಾದರಿ ಚರಗಳು (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) ತೆಗೆದುಹಾಕಲಾಗಿದೆ; `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, ಮತ್ತು ಐಚ್ಛಿಕ `AZURE_OPENAI_API_KEY` ಸೇರಿಸಲಾಗಿದೆ; ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಹೆಸರಿನಲ್ಲಿ ನವೀಕರಿಸಲಾಗಿದೆ.
- **ದಸ್ತಾವೇಜುಗಳು** — ಮೇಲಿನ ನವೀಕರಣೆಗಾಗಿ [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), ಮತ್ತು [STUDY_GUIDE.md](./STUDY_GUIDE.md) ನವೀಕರಿಸಲಾಗಿದೆ (ಪರಿಸರ ಚರ ಸ್ಥಾಪನೆ, ಪರಿಶೀಲನಾ ಸ್ಪ್ನೆಪೆಟ್, ಪೂರೈಕೆದಾರ ಸೂಚನೆ, ಹೆಸರು).

### ತೆಗೆದುಹಾಕಲಾಗಿದೆ

- ಗಿಟ್‌ಹಬ್ ಮಾದರಿ onboarding ಹಂತಗಳು ಮತ್ತು ಪರಿಸರ ಚರಗಳು ಸ್ಥಾಪನಾ ದಸ್ತಾವೇಜುಗಳಿಂದ ತೆಗೆದುಹಾಕಲಾಗಿದೆ (ಅಜೂರ್ ಓಪನ್ಏಐ / ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯು ಇದಕ್ಕೆ ಬದಲಿ).

### ಭದ್ರತೆ / ಗೌಪ್ಯತೆ (ಸಾರ್ವಜನಿಕ ಹಂಚಿಕೆಗೆ ಸ್ವಚ್ಛತೆ)

- ನಿಜವಾದ **ಅಜೂರ್ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್ ID**, ಸಂಪನ್ಮೂಲ ಗುಂಪು / ಸಂಪನ್ಮೂಲ ಹೆಸರುಗಳು ಮತ್ತು ಬಿಂಗ್ ಸಂಪರ್ಕ ID ಸೋರಿಕೆ ಮಾಡಿಕೊಂಡಿರುವ ಜ್ಯೂಪಿಟರ್ ನೋಟ್ಬುಕ್ ಕಾರ್ಯಾಚರಣೆ ಹೊರಬರುವಿಕೆಯನ್ನು ತೆರವುಗೊಳಿಸಲಾಗಿದೆ, ಜೊತೆಗೆ ಡೆವಲಪರ್ **ಸ್ಥಳೀಯ ಫೈಲ್ ಮಾರ್ಗಗಳು ಮತ್ತು ಬಳಕೆದಾರ ಹೆಸರುಗಳು**:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- ಪರಿಶೀಲನೆ ಮಾಡಲಾಗಿದೆ ಯಾವುದೇ API ಕೀಗಳು, ಟೋಕನ್‌ಗಳು, ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್ IDಗಳು ಅಥವಾ ವೈಯಕ್ತಿಕ ಮಾರ್ಗಗಳು ಟ್ರ್ಯಾಕ್ ಮಾಡಿದ ಇಂಗ್ಲಿಷ್ ವಿಷಯದಲ್ಲಿ ಉಳಿದಿಲ್ಲ (ಉಳಿದಿರುವ `GITHUB_TOKEN` ಉಲ್ಲೇಖಗಳು GitHub ಆಕ್ಷನ್‌ಗಳ ಟೋಕನ್ ಮತ್ತು ಪಾಠ 11 ಸ್ಥಾಪನೆಯ GitHub MCP ಸರ್ವರ್ PAT ಗಾಗಿ ಮಾತ್ರ).

### ಸೂಚನೆಗಳು ಮತ್ತು ಪರಿಚಿತ ಮಿತಿಗಳನ್ನು

- **ಅನನುಷ್ಠಿತ/ಸಂಕರಿಸಲ್ಪಟ್ಟಿಲ್ಲ.** ಯುಶಬಲವಾದ ಮಾದರಿಗಳು API/ಹೆಸರಿನ ಸರಿಯಾದತೆಗಾಗಿ ನವೀಕರಣಗೊಂಡವು; ನೇರವಾಗಿ ಲೈವ್ ಅಜೂರ್ ಸಂಪನ್ಮೂಲಗಳ ಮೇಲೆ ಓಡಿಸಲ್ಪಟ್ಟಿಲ್ಲ, ಮತ್ತು .ನೇಟ್ ಮಾದರಿಗಳನ್ನು ಇಲ್ಲಿ ಸಂಕಲನಗೊಳಿಸಲ್ಪಟ್ಟಿಲ್ಲ. ನಿಮ್ಮ ಸ್ವಂತ ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ / ಅಜೂರ್ ಓಪನ್ಏಐ ನಿಯೋಜನೆಯೊಂದಿಗೆ ಪರಿಶೀಲಿಸಿ.
- **ಮಾದರಿ ನಿಯೋಜನೆ ಪ್ರತಿಕ್ರಿಯೆಗಳ APIಗೆ ಬೆಂಬಲ ಕೊಡಬೇಕು.** `gpt-4o-mini`, `gpt-4.1`, ಅಥವಾ `gpt-5.x` ಮಾದರಿ ನಿಯೋಜನೆ ಬಳಸಿರಿ. ಹಳೆಯ ಮಾದರಿಗಳು ಮೂಲ ಪ್ರತಿಕ್ರಿಯೆಗಳ ಕಾರ್ಯಾಚರಣೆಯನ್ನು ಬೆಂಬಲಿಸುತ್ತವೆ ಆದರೆ ಪ್ರತಿಯೊಂದು ವೈಶಿಷ್ಟ್ಯವನ್ನು ಅಲ್ಲ.
- **ಏಜೆಂಟ್-ಫ್ರೇಮ್ವರ್ಕ್ ಆವೃತ್ತಿ.** ಮಾದರಿಗಳು ಇತ್ತೀಚಿನ MAF (`>=1.10.0`) ಅನ್ನು ಗುರಿಮಾಡಿವೆ. ಮಾನದಂಡದ ಏಜೆಂಟ್ ಸೃಷ್ಟಿ ಕರೆ `client.as_agent(...)` ಆಗಿದೆ; APIಗಳನ್ನು ಫ್ರೇಮ್ವರ್ಕ್‌ ಪ್ರಕಟಿತದستا ಮತ್ತು ಸ್ಥಾಪಿತ ಕಟ್ಟಡದ ವಿರುದ್ಧ ಪರಿಶೀಲಿಸಲಾಗಿದೆ. ನೀವು ವಿಭಿನ್ನ ಆವೃತ್ತಿಯನ್ನು ಇರಿಸಿದರೆ, ವಿಧಾನ ಲಭ್ಯತೆಯನ್ನು ದೃಢೀಕರಿಸಿ (`as_agent` ಮತ್ತು `create_agent`).
- **ಪಾಠ 08 ವರ್ಕ್ಫ್ಲೋ ನೋಟ್ಬುಕ್ 04** ಉದ್ದೇಶಪೂರ್ವಕವಾಗಿ `AzureAIAgentClient` (`agent-framework-azure-ai`ಯಿಂದ) ಉಳಿಸಲಾಗಿದೆ ಏಕೆಂದರೆ ಇದು ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಏಜೆಂಟ್ ಸರ್ವೀಸ್ ಹೋಸ್ಟ್ ಮಾಡಿದ ಉಪಕರಣಗಳನ್ನು ಬಳಸುತ್ತದೆ (ಬಿಂಗ್ ಗ್ರೌಂಡಿಂಗ್, ಕೋಡ್ ವಿವರಣಾ ಉಪಕರಣ); ಇದಾಗಿಯೇ ಇದು ಪ್ರತಿಕ್ರಿಯೆಗಳ ಆಧಾರಿತವಾಗಿದೆ.
- **.ನೆಟ್ ಡೀಫಾಲ್ಟ್ ನಿಯೋಜನೆ.** ಎರಡು ಪಾಠ 08 ಡಾಟ್‌ನೆಟ್ ವರ್ಕ್ಫ್ಲೋ ಮಾದರಿಗಳು ಹಳೆಯ `gpt-4o` ನ್ನು ಹಾರ್ಡ್‌ಕೋಡ್ ಮಾಡಿದ್ದವು; ಇವು ಈಗ `AZURE_OPENAI_DEPLOYMENT` (`gpt-4o-mini`) ನ್ನು ಡೀಫಾಲ್ಟ್ ಮಾಡಿಕೊಳ್ಳುತ್ತವೆ. ಮಾದರಿಯನ್ನು ಮಲ್ಟಿಮೋಡಲ್/ದೃಶ್ಯ ಇನ್ಪುಟ್ ಅವಲಂಬಿಸಿರುವಿರಾ ಎಂದು ಇರುವದಾದರೆ, ಹೊಂದುವ ಮಾದರಿ ಗಾಗಿ `AZURE_OPENAI_DEPLOYMENT` ಅನ್ನು ಸೆಟ್ ಮಾಡಿ.
- **ಫೌಂಡ್ರಿ ಸ್ಥಳೀಯ** ಒಪ್ಪಂದ ಮಾಡಿಕೊಳ್ಳುವ **ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ** ಎಂಡ್‌ಪಾಯಿಂಟ್ ಅನ್ನು ಹೊರತುಪಡಿಸುತ್ತದೆ ಮತ್ತು ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಗೆ ಉದ್ದೇಶಿಸಲಾಗಿದೆ; ಸಂಪೂರ್ಣ ಪ್ರತಿಕ್ರಿಯೆಗಳ API ವೈಶಿಷ್ಟ್ಯಗಳಿಗಾಗಿ ಅಜೂರ್ ಓಪನ್ಏಐ / ಮೈಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಬಳಸಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->