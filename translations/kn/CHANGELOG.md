# ಚೇಂಜ್‌ಲೋಗ್

**ಪ್ರಾರಂಭಿಕರಿಗಾಗಿ AI ಏಜೆಂಟ್ಸ್** ಕೋರ್ಸ್‌ಗೆ ಸಂಬಂಧಿಸಿದ ಎಲ್ಲಾ ಪರಿಣಾಮಕಾರಿಯಾದ ಬದಲಾವಣೆಗಳನ್ನು ಈ ಫೈಲ್‌ನಲ್ಲಿ ದಾಖಲಿಸಲಾಗಿದೆ.

## [ಮুক্তಗೊಂಡಿದೆ] — 2026-07-14

ಈ ಬಿಡುಗಡೆ ಕೋರ್ಸನ್ನು ಎರಡು ಹೊಸದಾಗಿ ಉಪೇಕ್ಷಿಸಿದ ಮಾದರಿಗಳಿಂದ (deprecated) ತೆಗೆದುಹಾಕುತ್ತದೆ, ಉಳಿದ ಪಾಠದ ನೊಟ್ಬುಕ್‌ಗಳನ್ನು ಸ್ಥಿರ Microsoft Agent Framework API ಗೆ ಸ್ಥಳಾಂತರಿಸುತ್ತದೆ ಮತ್ತು ಪೈಥಾನ್ ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಲೈವ್ Microsoft Foundry ನಿಯೋಗದ ವಿರುದ್ದ ಮಾನ್ಯತೆ ನೀಡುತ್ತದೆ.

### ಬದಲಾಯಿಸಲಾಗಿದೆ

- **ಉಪೇಕ್ಷಿಸಲಾದ ಮಾದರಿಗಳನ್ನು ತೆಗೆದುಹಾಕಲಾಗಿದೆ (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`).** `gpt-4.1` ಮತ್ತು `gpt-4.1-mini` ಈಗ deprecated ಆಗಿ (ಪ್ರকাশಿತ ನಿವೃತ್ತಿ ದಿನಾಂಕ **14 ಅಕ್ಟೋಬರ್ 2026**). ಪ್ರತಿಯೊಂದು ಕೋರ್ಸ್ ಉಲ್ಲೇಖವನ್ನು (ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳು, `.env.example`, ಪೈಥಾನ್/.ನೆಟ್ ನೋಟ್ಬುಕ್‌ಗಳು ಮತ್ತು ಮಾದರಿ) ಉಪೇಕ್ಷಿಸಲಾಗದ `gpt-5-mini` ಮೂಲಕ ಬದಲಾಯಿಸಲಾಗಿದೆ. ಪಾಠ 16 ರ ಮಾದರಿ-ರೌಟಿಂಗ್ ಉದಾಹರಣೆಯಲ್ಲಿ `gpt-5-nano` (ಸಣ್ಣ) ಮತ್ತು `gpt-5-mini` (ದೊಡ್ಡ) ಮೂಲಕ ಸಣ್ಣ/ದೊಡ್ಡ ವಿರುದ್ಧಾಭಿಪ್ರಾಯವನ್ನು ಕಾಯ್ದುಕೊಳ್ಳಲಾಗಿದೆ. ತೃತೀಯ-ಪಕ್ಷದ ಕಡತಗಳು ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), ಇತಿಹಾಸಾತ್ಮಕ GitHub ಮಾದರಿಗಳ ಪಠ್ಯ ಮತ್ತು `azure-openai-to-responses` ಕೌಶಲ್ಯದ ಸಾಮರ್ಥ್ಯದ ಟಿಪ್ಪಣಿಗಳನ್ನು ಉದ್ದೇಶಿತವಾಗಿ ಬದಲಾಯಿಸಲಾಗಿಲ್ಲ.
- **ಪಾಠ 14 ಹ್ಯಾಂಡ್‌ಆಫ್ ನೋಟ್ಬುಕ್ ಸ್ಥಿರ API ಗೆ ವಹಿಸಿದ್ದು.** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) ಈಗ `agent_framework.orchestrations.HandoffBuilder` ನಲ್ಲಿ `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type` ಆಧಾರಿತ ಸ್ಟ್ರೀಮಿಂಗ್ ಮತ್ತು `FoundryChatClient` ಬಳಸಿ (ಹಳೇ pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` ಚಿಹ್ನೆಗಳನ್ನು ಬದಲಿಸಿ).
- **ಪಾಠ 14 ಮಾನವ-ಇನ್-ದಿ-ಲೂಪ್ ನೋಟ್ಬುಕ್ ಸ್ಥಿರ API ಗೆ ವಹಿಸಿದ್ದು.** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) ಈಗ `ctx.request_info(...)` + `@response_handler` ಮೂಲಕ ವಿರಾಮಗೊಳ್ಳುತ್ತದೆ (ಹಳೇ `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` ತೆಗೆದುಹಾಕಲಾಗಿದೆ), `WorkflowBuilder(start_executor=..., output_executors=[...])` ನೊಂದಿಗೆ ನಿರ್ಮಿಸಿದ್ದು, `default_options={"response_format": ...}` ಮೂಲಕ ರಚಿಸಿದ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಚಾಲನೆಮಾಡುತ್ತದೆ ಮತ್ತು ಸ್ಕ್ರಿಪ್ಟಡ್ ಉತ್ತರವನ್ನು ಬಳಸಿ ನೋಟ್ಬುಕ್ ನಿರ್ಬಂಧಿಸದೆ (no blocking `input()`) ಓಡುತ್ತದೆ.
- **ಪರಿಸರ ಸಂರಚನೆ** ([.env.example](../../.env.example)): ಮಾದರಿ ನಿಯೋಗದ ಹೆಸರನ್ನು `gpt-5-mini` ಗೆ ಬದಲಿಸಿಕೊಂಡಿದೆ; `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (ಪಾಠ 16 ರೌಟಿಂಗ್) ಮತ್ತು ಹಿಂದೆ ಇಲ್ಲದಿದ್ದ `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (ಪಾಠ 15 ಬ್ರೌಸರ್ ಬಳಕೆ) ಸೇರಿಸಲಾಗಿದೆ.
- **ಆಶ್ರಿತತೆಗಳು** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry`, ಮತ್ತು `agent-framework-openai` ಅನ್ನು `~=1.10.0` ಗೆ ಪಿನ್ ಮಾಡಲಾಗಿದೆ, ಸ್ವಯಂ-ಸಮನ್ವಯ ಮತ್ತು ಮಾನ್ಯತೆಗೊಳ್ಳುವ ಸೆಟ್ (1.11.0 ಈಗ ಪ್ರವೃತ್ತಿಯ ವಲಯಗಳಾಗಿ ಬಳಕೆಮಾಡುವ ಪಾಠಗಳಿಗೆ ಪ್ರದೇಶ ಬೇರೆಯಾದ ಬದಲಾವಣೆಗಳನ್ನು ಒಳಗೊಂಡಿದೆ).

### ಟಿಪ್ಪಣಿಗಳು ಮತ್ತು ಗೊತ್ತಿರುವ ಮಿತಿಗಳು

- **ಲೈವ್ Microsoft Foundry ವಿರುದ್ಧ ಮಾನ್ಯತೆಯಾಯಿತು.** ಪೈಥಾನ್ ನೋಟ್ಬುಕ್‌ಗಳನ್ನು `nbconvert` ಮೂಲಕ ಹೆಡ್‌ಲೆಸ್ ಆಗಿ ಚಾಲನೆ ಮಾಡಲಾಗಿದೆ ಮತ್ತು Microsoft Foundry ಯೋಜನೆಯೊಂದಿಗೆ `gpt-5-mini` (ಮತ್ತು ಪಾಠ 16 ರೌಟಿಂಗ್‌ಗೆ `gpt-5-nano`) ಬಳಸಲಾಗಿದೆ. ನಿಮ್ಮ ಮನೆಯ ಯೋಜನೆಯಲ್ಲಿ ಸಮನಾದDeprecated ಅಲ್ಲದ ಮಾದರಿಗಳನ್ನು ನಿಯೋಗಿಸಿ; ನೋಟ್ಬುಕ್‌ಗಳು ನಿಯೋಗ ಹೆಸರನ್ನು `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` ರಿಂದ ಓದುತ್ತವೆ.
- **ಕೆಲವು ಪಾಠಗಳಿಗೆ ಇನ್ನಷ್ಟು ವನರುಷCCION ಬೇಕು.** ಪಾಠ 05 ಕ್ಕೆ Azure AI ಸರ್ಚ್ ಅಗತ್ಯವಿದೆ; ಪಾಠ 08 ರ Bing-based ವರ್ಕ್‌ಫ್ಲೋ (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) ಗೆ Bing ಸಂಪರ್ಕ ಮತ್ತು Microsoft Foundry ಏಜೆಂಟ್ ಸರ್ವಿಸ್ ಹೋಸ್ಟ್ ಮಾಡಿದ ಉಪಕರಣಗಳ ಅಗತ್ಯವಿದೆ; ಪಾಠ 13 (Cognee) ಮತ್ತು ಪಾಠ 17 (Foundry Local) ತಮ್ಮದೇ ರನ್‌ಟೈಮ್‌ಗಳನ್ನು ಹೊಂದಿವೆ.

## [ಮುಕ್ತಗೊಂಡಿದೆ] — 2026-07-13

ಈ ಬಿಡುಗಡೆ ಎರಡು ಹೊಸ ಪಾಠಗಳನ್ನು ಸೇರಿಸಿದೆ, ಇದು ನಿಯೋಗ ಚರವನ್ನು ಪೂರ್ಣಗೊಳಿಸುತ್ತಿದೆ — ಏಜೆಂಟ್‌ಗಳನ್ನು Microsoft Foundry ಗೆ ಹೆಚ್ಚಿಸುವುದು ಮತ್ತು ಒಂದೇ ವರ್ಕ್‌ಸ್ಟೇಷನ್‌ಗೆ ಇಳಿಸುವುದು — ಜೊತೆಗೆ ಸ್ಮೋಕ್ ಟೆಸ್ಟ್ ಪೈಪ್ಲೈನ್, ನವೀಕೃತ ಕೋರ್ಸ್ ನ್ಯಾವಿಗೇಶನ್, ಹೊಸ ಕಲಿಕಾರಣ ಕೌಶಲ್ಯಗಳು ಮತ್ತು ನವೀಕರಿಸಿದ ಬ್ರಾಂಡಿಂಗ್.

### ಸೇರಿಸಲಾಗಿದೆ

- **ಪಾಠ 16 — Microsoft Foundry ಸಹಿತ ತಜ್ಞವಾಗಿ ಏಜೆಂಟ್‌ಗಳನ್ನು ನಿಯೋಗಿಸುವುದು.** ಹೊಸ ಪಾಠ [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) ಮತ್ತು ಓಡಿಸಬಹುದಾದ ಟಿಪ್ಪಣಿ ಪುಸ್ತಕ [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) ಉತ್ಪಾದನಾ ಗ್ರಾಹಕ-ಸಹಾಯ ಏಜೆಂಟ್ ನಿರ್ಮಿಸುತ್ತದೆ (ಉಪಕರಣಗಳು, RAG, ಸ್ಮೃತಿ, ಮಾದರಿ ರೌಟಿಂಗ್, ಪ್ರತಿಕ್ರಿಯೆ ಕ್ಯಾಶಿಂಗ್, ಮಾನವ ಅನುಮೋದನೆ, ಮೌಲ್ಯಮಾಪನ ಗೇಟ್ ಮತ್ತು OpenTelemetry ಟ್ರೇಸಿಂಗ್) ಚಟುವಟಿಕೆಗಳು/ನಿಯೋಗ/ರನ್‌ಟೈಮ್ ಮೆರ್ಮೇಡ್ ಗುರುತು ಪತ್ರಗಳು, ಜ್ಞಾನ ಪರಿಶೀಲನೆ, ಕಾರ್ಮಿಕ ಮತ್ತು ಸವಾಲ್ ಸಹಿತ.
- **ಪಾಠ 17 — Foundry Local ಮತ್ತು Qwen ಸಹಿತ ಸ್ಥಳೀಯ AI ಏಜೆಂಟ್‌ಗಳನ್ನು ರಚಿಸುವುದು.** ಹೊಸ ಪಾಠ [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) ಮತ್ತು ನೋಟ್ಬುಕ್ [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) ಸಂಪೂರ್ಣವಾಗಿ ಸಾಧನದಲ್ಲಿ ಆಧಾರಿತ ಎಂಜಿನಿಯರಿಂಗ್ ಸಹಾಯಕನನ್ನು ನಿರ್ಮಿಸುತ್ತಿದೆ (Qwen ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್ Foundry Local ಮೂಲಕ, ಸ್ಯಾಂಡ್‌ಬಾಕ್ಸ್ ಫೈಲ್ ಉಪಕರಣಗಳು, ಸ್ಥಳೀಯ RAG Chroma ಮೂಲಕ, ಐಚ್ಛಿಕ ಸ್ಥಳೀಯ MCP), ಸ್ಥಳೀಯ ಮಾತ್ರ / ಸ್ಥಳೀಯ RAG / ಉಪಕರಣ-ಕಾಲಿಂಗ್ ಚಿತ್ರಣಗಳು, ಜ್ಞಾನ ಪರಿಶೀಲನೆ, ಕಾರ್ಯ ಮತ್ತು ಸವಾಲ್ ಸಹಿತ.
- **ಸ್ಮೋಕ್ ಟೆಸ್ಟ್ ಪೈಪ್ಲೈನ್.** ಹೊಸ [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) ವರ್ಕ್‌ಫ್ಲೋ [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) ಜೊತೆಗೆ ಪ್ರತಿ ಪಾಠಗಳೆಡೆಗಿನ ಕ್ಯಾಂಟಲಾಗ್‌ಗಳು [tests/](./tests/README.md) ಫಲಿತಾಂಶಗಳನ್ನು ನಿಯೋಗದ ಏಜೆಂಟ್‌ಗಳಿಗೆ ಪಾಠ 01, 04, 05 ಮತ್ತು 16 ಕ್ಕೆ, ಪ್ರತಿಯೊಂದು ಕ್ಯಾಂಟಲಾಗ್ ಅನ್ನು ಅದರ ಪಾಠ ಮತ್ತು ಹೋಸ್ಟ್ ಆದ ಏಜೆಂಟ್ ಹೆಸರಿನೊಂದಿಗೆ ಸೂಚಿಸಲಾಗಿದೆ. ಪಾಠ 16 ಗೆ "ನಿಯೋಜಿತ ಏಜೆಂಟ್ ಅನ್ನು ಸ್ಮೋಕ್ ಟೆಸ್ಟ್‌ಗಳೊಂದಿಗೆ ಮಾನ್ಯಗೊಳಿಸುವುದು" ವಿಭಾಗ ಸೇರ್ಪಡೆ; ಪಾಠಗಳು 01/04/05 ಗೆ ಐಚ್ಛಿಕ ಸ್ಮೋಕ್ ಟೆಸ್ಟ್ ಸೂಚಕ.
- **ಕಲಿಕಾರಣ ಕೌಶಲ್ಯಗಳು.** ಹೊಸ ಏಜೆಂಟ್ ಕೌಶಲ್ಯಗಳು `.agents/skills/` ಒಳಗೆ: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (ಪಾಠ 16 ಮತ್ತು 17 ಮಾರ್ಗಸೂಚಿಯನ್ನು ಪ್ಯಾಕೇಜ್ ಮಾಡುವುದು), ಮತ್ತು [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (ಲೈವ್ Microsoft Foundry / Azure OpenAI ಸೆಟ್ಟಪ್ ವಿರುದ್ದ ನೋಟ್ಬುಕ್ ಮಾದರಿಗಳನ್ನು ಮಾನ್ಯಗೊಳಿಸುವ ವಿಧಾನ).
- **ನೋಟ್ಬುಕ್ ಮಾನ್ಯತೆ ಓಡಿಸುವಿಕೆ.** ಹೊಸ [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) ಇದು ಪ್ರತಿಯೊಂದು ಪೈಥಾನ್ ನೋಟ್ಬುಕ್ ಅನ್ನು ಹೆಡ್‌ಲೆಸ್ ಆಗಿ `nbconvert` ಉಪಯೋಗಿಸಿ ಚಲಿಸುತ್ತದೆ ಮತ್ತು PASS/FAIL ಮ್ಯಾಟ್ರಿಕ್ಸ್ (ಮತ್ತು `results.json`) ಮುದ್ರಿಸುತ್ತದೆ. ಇದು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ರೈಪೋ ಮೂಲ ಮತ್ತು ಪೈಥಾನ್ ಗುರುತಿಸಿ, ಶ್ರೇಣಿಯಲ್ಲಿ ಇಲ್ಲದ ನೋಟ್ಬುಕ್‌ಗಳು (`.venv`, `site-packages`, `translations`, ಕೌಶಲ್ಯ ಟೆಂಪ್ಲೇಟ್ ಆಸ್ತಿ) ಮತ್ತು `.NET` ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಬೇರ್ಪಡಿಸುತ್ತದೆ ಮತ್ತು `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet` ಮತ್ತು `-Python` ಆಯ್ಕೆಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತದೆ.
- **ಕೋರ್ಸ್ ನ್ಯಾವಿಗೇಶನ್.** ಮುಂಚಿನ / ಮುಂದಿನ ಪಾಠ ಲಿಂಕ್‌ಗಳನ್ನು ಪಾಠ 11–15 (ಹಿಂದೆ ಇರಲಿಲ್ಲ) ಸೇರಿಸಲಾಗಿದೆ, ಇದರಿಂದ ಸಂಪೂರ್ಣ ಕೋರ್ಸ್ 00 → 18 ಎರಡೂ ಬದಿಗಳಲ್ಲಿ ಜೋಡಣೆ ಹೊಂದಿದೆ.
- **ಹೊಸ ಥಂಬ್ನೇಲ್‌ಗಳು.** ಪಾಠ 16 ಮತ್ತು 17 ರ ಥಂಬ್ನೇಲ್‌ಗಳು, ಜೊತೆಗೆ ನವೀಕೃತ ಸ್ವಾಮಿ ಚಿತ್ರ [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (ಈಗ ಎರಡು ಹೊಸ ಪಾಠಗಳನ್ನು ಮತ್ತು `aka.ms/ai-agents-beginners` URL ಅನ್ನು ಪ್ರಚಾರ ಮಾಡುತ್ತಿದೆ).
- **ಆಶ್ರಿತತೆಗಳು** ([requirements.txt](../../requirements.txt)): ಪಾಠ 17 ಗಾಗಿ `foundry-local-sdk` ಮತ್ತು `chromadb` ಸೇರಿಸಲಾಗಿದೆ.

### ಬದಲಾಯಿಸಲಾಗಿದೆ

- **ಮುಖ್ಯ [README.md](./README.md)** ಪಾಠಗಳ ಪಟ್ಟಿಗೆ ಪಾಠ 16 ಮತ್ತು 17 ಈಗ ಅವರ ವಿಷಯಕ್ಕೆ ಲಿಂಕ್ ಮಾಡಲಾಗಿದೆ (ಹಿಂದೆ "ಇನ್ನಿಲ್ಲ" ಎಂದು ತೋರಿಸುತ್ತಿತ್ತು); ಸಂಗ್ರಹಣಾ ಚಿತ್ರ `repo-thumbnailv3.png` ಗೆ ಬದಲಿಸಲಾಗಿದೆ.
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: ಪಾಠ-ಬದಲಿಗೆ ಮಾರ್ಗದರ್ಶಿ ಮತ್ತು ಕಲಿಕೆಯ ಮಾರ್ಗಗಳಿಗೆ ಪಾಠ 16 ಮತ್ತು 17 ಸೇರಿಸಲಾಗಿದೆ ಮತ್ತು "ನಿಯೋಜಿತ ಏಜೆಂಟ್‌ಗಳನ್ನು ಸ್ಮೋಕ್ ಟೆಸ್ಟ್‌ಗಳೊಂದಿಗೆ ಮಾನ್ಯಗೊಳಿಸುವುದು" ವಿಭಾಗ ಸೇರಿಸಲಾಗಿದೆ.
- **[AGENTS.md](./AGENTS.md)**: ಪಾಠಗಳ ಎಣಿಕೆ/ವಿವರಣೆ (00–18) ನವೀಕರಿಸಲಾಗಿದೆ, ಸ್ಮೋಕ್ ٽೆಸ್ಟ್ ಮಾನ್ಯತೆ ವಿಭಾಗ ಸೇರಿಸಲಾಗಿದೆ ಮತ್ತು ಪಾಠ 16/17 ಮಾದರಿ ಹೆಸರಿನ ಉದಾಹರಣೆಗಳು ಸೇರಿಸಲಾಗಿದೆ.
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "ಹಿಂದಿನ ಪಾಠ" ಈಗ ಪಾಠ 17 ಗೆ ಸೂಚಿಸುತ್ತದೆ (ಹಳೆಯದು ಪಾಠ 15); ಸರಣಿಯನ್ನು ಮುಚ್ಚುತ್ತದೆ.
- **ಅಪರಿಹಾರ್ಯ ಮಾದರಿಗಳ ಮೇಲೆ ಮಾದರಿ ಉಲ್ಲೇಖಗಳನ್ನು ಪ್ರಮಾಣೀಕರಿಸಲಾಗಿದೆ.** ಕೋರ್ಸ್ ಎರಡನೆಯ ಎಲ್ಲ `gpt-4o` / `gpt-4o-mini` ಉಲ್ಲೇಖಗಳನ್ನು (ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳು, `.env.example`, ಪೈಥಾನ್/.ನೆಟ್ ನೋಟ್ಬುಕ್‌ಗಳು ಮತ್ತು ಮಾದರಿ) `gpt-4.1-mini` ಮೂಲಕ ಬದಲಿಸಲಾಗಿದೆ — `gpt-4o` (ಎಲ್ಲಾ ಆವೃತ್ತಿಗಳು) 2026 ರಲ್ಲಿ ನಿವೃತ್ತಿ ಆಗುತ್ತಿದೆ. ಪಾಠ 16 ರ ಮಾದರಿ-ರೌಟಿಂಗ್ ಉದಾಹರಣೆಯಲ್ಲಿ ಸಣ್ಣ/ದೊಡ್ಡ ವಿರುದ್ಧಾಭಿಪ್ರಾಯವನ್ನು `gpt-4.1-mini` (ಸಣ್ಣ) ಮತ್ತು `gpt-4.1` (ದೊಡ್ಡ) ಬಳಸಿ ಕಾಯ್ದುಕೊಳ್ಳಲಾಗಿದೆ. ಪೈಥಾನ್ ನೋಟ್ಬುಕ್‌ಗಳು ಈಗ ಮಾದರಿಗೆಟನ್ ಹೆಸರನ್ನು ನಿಯೋಜನೆಯದರೀಯವಾಗಿ पर्यावरण ಚರಗಳಿನಿಂದ (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) ಆಯ್ಕೆಮಾಡುತ್ತವೆ, ಮಧ್ಯಸ್ಥ ಮಾದರಿ ಹೆಸರನ್ನು ನೇರವಾಗಿ ಹಾರ್ಡ್ ಕೋಡ್ ಮಾಡುವುದು ಇಲ್ಲ.

### ಟಿಪ್ಪಣಿಗಳು ಮತ್ತು ಗೊತ್ತಿರುವ ಮಿತಿಗಳು

- **ಲೈವ್ Azure ವಿರುದ್ಧ ಕಾರ್ಯಗತಗೊಳಿಸಲ್ಪಟ್ಟಿಲ್ಲ.** ಹೊಸ ಪಾಠಗಳ ನೋಟ್ಬುಕ್‌ಗಳು ಶಿಕ್ಷಣ ಮಾದರಿಗಳಾಗಿವೆ; ನಿಮ್ಮ ತಮ್ಮ Microsoft Foundry / Foundry Local ಸೆಟ್ಟಪ್ ಬಳಸಿ ಅವುಗಳನ್ನು ಚಾಲನೆ ಮಾಡಿ ಮತ್ತು ಮಾನ್ಯತೆ ನೀಡಿ. ಸ್ಮೋಕ್ ಟೆಸ್ಟ್ ವರ್ಕ್‌ಫ್ಲೋ ನೀವು ಪಾಠದ ಏಜೆಂಟ್ ಅನ್ನು ನಿಯೋಜಿಸಿ ಮತ್ತು Foundry ಯೋಜನಾ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ **Azure AI ಬಳಕೆದಾರ** ಪಾತ್ರದೊಂದಿಗೆ Azure OIDC ರಹಸ್ಯಗಳನ್ನು (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) ಸಂರಚಿಸುವ ಅಗತ್ಯವಿದೆ.
- **ಪಾಠ 17 ಸ್ಥಳೀಯವಾಗಿದೆ ಮಾತ್ರ.** ಇದಕ್ಕೆ Foundry ಪ್ರತಿಕ್ರಿಯೆಗಳ ಅಂತಿಮಬಿಂದುವಿನಿಲ್ಲ, ಆದ್ದರಿಂದ ಸ್ಮೋಕ್ ಟೆಸ್ಟ್ ಕ್ರಿಯೆ ಅನ್ವಯಿಸುವುದಿಲ್ಲ; ನೋಟ್ಬುಕ್ ನಿಮ್ಮ ವರ್ಕ್‌ಸ್ಟೇಷನ್ ಮೇಲೆ ಚಾಲನೆ ಮಾಡಿಕೊಳ್ಲಿ.

## [ಮುಕ್ತಗೊಂಡಿದೆ] — 2026-07-06

ಈ ಬಿಡುಗಡೆ ಕೋರ್ಸನ್ನು **Azure OpenAI Responses API** ಗೆ ಸ್ಥಳಾಂತರಿಸುತ್ತದೆ, ಉತ್ಪನ್ನ ಹೆಸರನ್ನು **Microsoft Foundry** ಮತ್ತು **Microsoft Agent Framework (MAF)** ಮೇಲೆ ಪ್ರಮಾಣೀಕರಿಸುತ್ತದೆ, GitHub ಮಾದರಿಗಳನ್ನು ನಿವೃತ್ತಿ ಮಾಡುತ್ತದೆ, SDK ಆವೃತ್ತಿಗಳನ್ನು ನವೀಕರಿಸುತ್ತದೆ ಮತ್ತು ಸ್ಥಳೀಯ ಮಾದರಿಗಳು ಮತ್ತು Foundry ಮೇಲೆ ಇತರ ಫ್ರೇಮ್ವರ್ಕ್‌ಗಳು ಹೋಸ್ಟ್ ಮಾಡುವ ಬಗ್ಗೆ ಹೊಸ ವಿಷಯವನ್ನು ಸೇರಿಸುತ್ತದೆ.

### ಸೇರಿಸಲಾಗಿದೆ

- **ಸ್ಥಳಾಂತರ ಕೌಶಲ್ಯ** — `.agents/skills/` ಅಡಿಯಲ್ಲಿ [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) ಏಜೆಂಟ್ ಕೌಶಲ್ಯವನ್ನು ಸ್ಥಾಪಿಸಲಾಗಿದೆ (Azure-Samples/azure-openai-to-responses ನಿಂದ), ಅದರ ಉಲ್ಲೇಖಗಳು ಮತ್ತು ಸ್ಕ್ಯಾನರ್ ಸ್ಕ್ರಿಪ್ಟ್ ಸಹಿತ.
- **Foundry Local (ಮಾದರಿಗಳನ್ನು ಸಾಧನದಲ್ಲಿ ಓಡಿಸಿ)** — [00-course-setup/README.md](./00-course-setup/README.md) ನಲ್ಲಿ ಹೊಸ "ವೈકલ್ಪಿಕ ಪ್ರೊವೈಡರ್: Foundry Local" ವಿಭಾಗವು ಇನ್‌ಸ್ಟಾಲ್ (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, ಮತ್ತು `FoundryLocalManager` ಅನ್ನು Microsoft Agent Framework ಗೆ `OpenAIChatClient` ಮೂಲಕ ಯಶಸ್ವಿಯಾಗಿ ಸಂಪರ್ಕಿಸುವಂತೆ ದಾಖಲಿಸಿದೆ.
- **Microsoft Foundry ನಲ್ಲಿ LangChain / LangGraph ಏಜೆಂಟ್‌ಗಳು ಹೋಸ್ಟ್ ಮಾಡುವುದು** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) ನಲ್ಲಿ ಹೊಸ ವಿಭಾಗ ಮತ್ತು ಚಾಲನೆ ಮಾಡಬಹುದಾದ ಮಾದರಿ [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) `langchain-azure-ai[hosting]` ಮತ್ತು `ResponsesHostServer` (`/responses` ಪ್ರೋಟೋಕಾಲ್) ಉಪಯೋಗಿಸಿ, ಮತ್ತಷ್ಟು ವಿವರಗಳಿಗೆ [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) ನೋಡಿ.
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) ನಲ್ಲಿ ಹೊಸ "ವಾಸ್ತವಿಕ ಉದಾಹರಣೆ: Microsoft Project Opal" ವಿಭಾಗ, Opal ನನ್ನು ಉದ್ಯಮ ಕಂಪ್ಯೂಟರ್ ಬಳಕೆ ಏಜೆಂಟ್ ಆಗಿ ಫ್ರೇಮ್ ಮಾಡಿ ಕೋರ್ಸ್ ತತ್ವಗಳಿಗೆ (ಮಾನವ-ಇನ್-ದಿ-ಲೂಪ್, ಭರವಸೆ/ಸುರಕ್ಷತೆ, ಯೋಜನೆ, ಕೌಶಲ್ಯಗಳು) ಮ್ಯಾಪ್ ಮಾಡಿದೆ.
- **ಮೂರುನೇ ಪಾಠ 02 ಪೈಥಾನ್ ಮಾದರಿ** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) ಸೇರಿಸಲಾಗಿದೆ ("ಬದಲಾಯಿಸಲಾಗಿದೆ" ವಿಭಾಗ ನೋಡಿರಿ — ಹಳೆಯ Semantic Kernel ನೋಟ್ಬುಕ್‌ನಿಂದ ಸ್ಥಳಾಂತರಿಸಲಾಗಿದೆ) ಮತ್ತು ಪಾಠ README ಯಲ್ಲಿ ಲಿಂಕ್ ಮಾಡಲಾಗಿದೆ.
- **ಮಾದರಿಗಳ ಮತ್ತು ಪ್ರೊವೈಡರ್‌ಗಳ** ವಿಭಾಗ [STUDY_GUIDE.md](./STUDY_GUIDE.md) ಗೆ ಸೇರಿಸಲಾಗಿದೆ.

### ಬದಲಾಯಿಸಲಾಗಿದೆ

- **ಚಾಟ್ ಪೂರ್ಣತೆ → ಪ್ರತಿಕ್ರಿಯೆಗಳ API (ಪೈಥಾನ್).** ಮಾದರಿಯನ್ನು ನೇರವಾಗಿ ಕರೆ ಮಾಡಿದ ಮಾದರಿ `Responses API` (`client.responses.create(input=..., store=False)`, `resp.output_text`) ಗೆ ಸ್ಥಳಾಂತರಿಸಿದ್ದು, `OpenAI` ಕ್ಲಯಿಂಟ್ ಉಪಯೋಗಿಸಿ ಸ್ಥಿರ Azure OpenAI `/openai/v1/` ಅಂತಿಮ ಬಿಂದುವಿಗೆ (ಯಾವುದೇ `api_version` ಇಲ್ಲ). ಇದರಿಂದ ಪ್ರಭಾವಿತ ಮಾದರಿ:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — ಸಂಪೂರ್ಣ ಫಂಕ್ಷನ್ ಕಾಲಿಂಗ್ ಓಪನಿಂಗ್ (ಉಪಕರಣ ಪರಿಕಲ್ಪನೆಯನ್ನು ಪ್ರತಿಕ್ರಿಯೆಗಳ ಸ್ವರೂಪಕ್ಕೆ ಸರಳಗೊಳಿಸಲಾಗಿದೆ, ಉಪಕರಣ ಫಲಿತಾಂಶವನ್ನು `function_call_output`, `max_output_tokens` ಮುಂತಾದವೆಯಾಗಿರುತ್ತದೆ).

- **GitHub ಮಾದರಿಗಳು → ಅಜೂರ್ ಓಪನ್‌ಎಐ.** GitHub ಮಾದರಿಗಳು ಅನಧಿಕೃತಗೊಂಡಿವೆ (**)ಜುಲೈ 2026** ರಂದು ನಿವೃತ್ತಿಯಾಗುತ್ತದೆ** ಮತ್ತುResponses API ಅನ್ನು ಬೆಂಬಲಿಸುವುದಿಲ್ಲ. Python ಮತ್ತು .NET semplesಗಳಾದ GitHub ಮಾದರಿಗಳ ಎಲ್ಲಾ ಕೋಡ್ ಮಾರ್ಗಗಳನ್ನು ಅಜೂರ್ ಓಪನ್‌ಎಐ / ಮೈನಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಗೆ ಪರಬರ್ತಿಸಲಾಗಿದೆ:
  - Python: ಪಾಠ 08 ವರ್ಕ್‌ಫ್ಲೋ ನೋಟ್‌ಬುಕ್ ಗಳು (`01`–`03`), ಪಾಠ 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`).
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + ಸಹಾಯಕ `.md` ಡಾಕ್ಯುಮೆಂಟ್ ಗಳು, ಮತ್ತು ಪಾಠ 08 dotNET ವರ್ಕ್‌ಫ್ಲೋ ನೋಟ್‌ಬುಕ್ ಗಳು/`.md` (`01`–`03`) ಈಗ `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` ಯನ್ನು `AzureCliCredential` ಜೊತೆ ಬಳಸುತ್ತವೆ.
- **ಸಾಮ೦ತ್ಯ ಕಣ್ಣು → ಮೈನಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್.** ಹಳೆಯ `02-semantic-kernel.ipynb` ಅನ್ನು ಮೈನಕ್ರೋಸಾಫ್ಟ್ ಏಜೆಂಟ್ ಫ್ರೇಮ್‌ವರ್ಕ್ ಅಜೂರ್ ಓಪನ್‌ಎಐ (Responses API) ಜೊತೆ ಪುನಃ ಬರೆಯಲಾಗಿದೆ ಮತ್ತು `02-python-agent-framework-azure-openai.ipynb` ಎಂದು ಹೆಸರು ಬದಲಿಸಲಾಗಿದೆ.
- **`FoundryChatClient` + `as_agent` ನಲ್ಲಿ ಪ್ರಾಮಾಣೀಕರಿಸಲಾಗಿದೆ.** README ಮತ್ತು ನೋಟ್‌ಬುಕ್ ಕೋಡ್ ಗಳು `AzureAIProjectAgentProvider` ಅನ್ನು ಉಲ್ಲೇಖಿಸುವುದು ಪಾಠ 01 ಮತ್ತು ಫ್ರೇಮ್‌ವರ್ಕ್‌ನ ಸ್ವಂತ semples ಗಳು ಬಳಸುವ ಪ್ರಾಮಾಣಿಕ ಮಾದರಿಯಲ್ಲಿ ಪ್ರಾಮಾಣೀಕರಿಸಲಾಗಿದೆ: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` ಜೊತೆ `provider.as_agent(...)`. ಪಾಠ 02–14 READMEs ಮತ್ತು ನೋಟ್‌ಬುಕ್ ಗಳಲ್ಲಿ ನವೀಕರಿಸಲಾಗಿದೆ (ಉದಾಹರಣೆಗೆ, ಪಾಠ 13 ಮೆಮೊರಿ, ಎಲ್ಲಾ ಪಾಠ 14 ನೋಟ್‌ಬುಕ್ ಗಳು, `11-agentic-protocols/code_samples/github-mcp/app.py`).
- **ಉತ್ಪನ್ನ ನಾಮಕರಣ.** ಇಂಗ್ಲಿಷ್ ವಿಷಯಗಳಲ್ಲಿ ಅಲ್ಲಿದ್ದಂತೆ ಹೆಸರು ಬದಲಾಯಿಸಲಾಗಿದೆ:
  - "Azure AI Foundry" / "Azure AI Studio" → **ಮೈನಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ**
  - "Azure AI Agent Service" → **ಮೈನಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಏಜೆಂಟ್ ಸೇವೆ**
  - (ಬದಲಾವಣೆ ಇಲ್ಲ: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", ಮತ್ತು ಪರಿಸರ-ಚರಕ ಹೆಸರಿಗಳು.)
- **ಆಶ್ರಿತತೆಗಳು** ([requirements.txt](../../requirements.txt)):
  - ಪಿನ್ ಮಾಡಲಾಗಿದೆ `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0`.
  - ಪಿನ್ ಮಾಡಲಾಗಿದೆ `openai>=1.108.1` (Responses API ಗಾಗಿ ಕನಿಷ್ಠ).
  - ತೆಗೆಯಲಾಗಿದೆ `azure-ai-inference` (ಮಾತ್ರ ಮಾರ್ಪಡಿಸಿದ GitHub ಮಾದರಿ semples ಗೆ ಬಳಸಲಾಯಿತು).
- **ಪರಿಸರ ಸಂರಚನೆ** ([.env.example](../../.env.example)): GitHub ಮಾದರಿಗಳ ಚರಕ variables (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) ತೆಗೆಯಲಾಗಿದೆ; ಸೇರಿಸಲಾಗಿದೆ `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, ಮತ್ತು ಐಚ್ಛಿಕ `AZURE_OPENAI_API_KEY`; ನಾಮಕರಣವನ್ನು Microsoft Foundry ಗೆ ನವೀಕರಿಸಲಾಗಿದೆ.
- **ಡಾಕ್ಯುಮೆಂಟ್ ಗಳು** — ಮೇಲ್ಕಾಣಿಸಿದಕ್ಕಾಗಿ [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), ಮತ್ತು [STUDY_GUIDE.md](./STUDY_GUIDE.md) ನವೀಕರಿಸಲಾಗಿದೆ (ಸಂರಚನೆ ಚರಕಗಳು, ಪರಿಶೀಲನ ಸ্নಿಪೆಟ್, ಪೂರೈಕೆದಾರ ಮಾರ್ಗದರ್ಶನ, ನಾಮಕರಣ).

### ತೆಗೆಯಲಾಗಿದೆ

- GitHub ಮಾದರಿಗಳ onboarding ಹೆಜ್ಜೆಗಳು ಮತ್ತು ಪರಿಸರ ಚರಕ variables ಗಳು setup docs ನಿಂದ (ಅಜೂರ್ ಓಪನ್‌ಎಐ / ಮೈನಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಮೂಲಕ ಮೀರಿಸಲಾಗಿದೆ).

### ಭದ್ರತೆ / ಗೌಪ್ಯತೆ (ಸಾರ್ವಜನಿಕ ಹಂಚಿಕೆ ನಾಶ)

- ನಿಜವಾದ **Azure ಸಬ್‌ಸ್ಕ್ರಿಪ್ಷನ್ ಐಡಿ**, resource-group / resource ಹೆಸರಿಗಳು, Bing ಸಂಪರ್ಕ ID, ಜೊತೆಗೆ ಅಭಿವೃದ್ಧಿಪಡಿಸಿದ **ಸ್ಥಳೀಯ ಕಡತ ಮಾರ್ಗಗಳು ಮತ್ತು ಬಳಕೆದಾರ ಹೆಸರುಗಳು** ಅನಾವರಣವಾಗಿರುವ Jupyter notebook ನಿರ್ವಹಣಾ ಔಟ್‌ಪುಟ್ ಗಳೆಲ್ಲಾ ಅಳಿಸಲಾಗಿದೆ:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- API ಕೀಗಳು, ಟೋಕನ್ಗಳು, ಸಬ್‌ಸ್ಕ್ರಿಪ್ಷನ್ ಐಡಿ ಅಥವಾ ವೈಯಕ್ತಿಕ ಮಾರ್ಗಗಳು ಟ್ರ್ಯಾಕ್ ಆಗಿರುವ ಇಂಗ್ಲಿಷ್ ವಿಷಯದಲ್ಲಿ ಉಳಿದಿಲ್ಲ ಎಂಬುದನ್ನು ಪರಿಶೀಲಿಸಲಾಯಿತು (`GITHUB_TOKEN` ಉಲ್ಲೇಖಗಳು GitHub Actions ಟೋಕನ್(workflows) ಮತ್ತು GitHub MCP ಸರ್ವರ್ PAT (ಪಾಠ 11 setup) ನಲ್ಲಿ ಮಾತ್ರ ಇವೆ — ಎರಡೂ ಕಾನೂನುಬದ್ಧ ಮತ್ತು GitHub ಮಾದರಿಗಳಿಗೆ ಸಂಬಂಧವಿಲ್ಲ).

### ಟಿಪ್ಪಣಿಗಳು ಮತ್ತು ತಿಳಿದಿರುವ ಮಿತಿ

- **ನಡತ/ಕಂಪೈಲ್ ಆಗಿಲ್ಲ.** ಇವು API/ನಾಮಕರಣದ ಸರಿಯಾದತೆಗಾಗಿ ನವೀಕರಿಸಲಾಗಿರುವ ಶೈಕ್ಷಣಿಕ semples; ಅವು ಜೀವಂತ ಅಜೂರ್ ಸಂಪನ್ಮೂಲಗಳ ಮೇಲೆ ಪ್ರಯೋಗಿಸಲ್ಪಟ್ಟಿಲ್ಲ, ಮತ್ತು .NET semples ಈ ಪರಿಸರದಲ್ಲಿ ಉಪಯೋಗಿಸುವಿಕೆ ನಡೆಯಲಿಲ್ಲ. ನಿಮ್ಮ ಸ್ವಂತ ಮೈನಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ / ಅಜೂರ್ ಓಪನ್‌ಎಐ ನಿಯೋಜನೆ ವಿರುದ್ಧ ಪರಿಶೀಲಿಸಿ.
- **ಮಾದರಿ ನಿಯೋಜನವು Responses API ಅನ್ನು ಬೆಂಬಲಿಸಬೇಕು.** `gpt-4.1-mini`, `gpt-4.1`, ಅಥವಾ `gpt-5.x` ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿ. ಹಳೆಯ ಮಾದರಿಗಳು Responses ಮೂಲ ಕಾರ್ಯೆಯನ್ನು ಬೆಂಬಲಿಸುತ್ತವೆ ಆದರೆ ಪ್ರತಿಯೊಂದು ವೈಶಿಷ್ಟ್ಯವನ್ನೂ ಅಲ್ಲ.
- **Agent-framework ಆವೃತ್ತಿ.** semples ಗಳು ನವೀನ MAF (`>=1.10.0`) ಗಾಗಿ ಆಗಿದ್ದು, canonical ಏಜೆಂಟ್-ಸೃಷ್ಟಿ ಕರೆ `client.as_agent(...)`; API ಗಳು ಫ್ರೇಮ್‌ವರ್ಕ್ ಪ್ರಕಟಿತ ಡಾಕ್ಯುಮೆಂಟೇಷನ್ ಮತ್ತು ಸ್ಥಾಪಿತ ನಿರ್ಮಿತಿಯೊಂದಿಗೆ ಪರಿಶೀಲಿಸಲ್ಪಟ್ಟಿವೆ. ನೀವು ಬೇರೆ ಆವೃತ್ತಿಯನ್ನು ಪಿನ್ ಮಾಡಿದರೆ, ವಿಧಾನ ಲಭ್ಯತೆಯನ್ನು ದೃಢೀಕರಿಸಿ (`as_agent` ವಿರುದ್ಧ `create_agent`).
- **ಪಾಠ 08 ವರ್ಕ್‌ಫ್ಲೋ ನೋಟ್‌ಬುಕ್ 04** ಉದ್ದೇಶಪೂರಕವಾಗಿ `AzureAIAgentClient` ( `agent-framework-azure-ai` ಯಿಂದ) ಉಪಯೋಗಿಸುತ್ತದೆ ಏಕೆಂದರೆ ಇದು ಮೈನಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿ ಏಜೆಂಟ್ ಸೇವೆ ಅತಿಥಿ ಉಪಕರಣಗಳನ್ನು (ಬಿಂಗ್ ಗ್ರೌಂಡಿಂಗ್, ಕೋಡ್ ಇಂಟರ್ಪ್ರೀಟರ್) ಬಳಸುತ್ತದೆ; ಇದು ಈಗಾಗಲೇ Responses ಆಧಾರಿತವಾಗಿದೆ.
- **.NET ಡಿಫಾಲ್ಟ್ ನಿಯೋಜನೆ.** ಎರಡು ಪಾಠ 08 dotNET ವರ್ಕ್‌ಫ್ಲೋ semples ಹಿಂದೆ ನಿರ್ದಿಷ್ಟ ಮಾದರಿಯನ್ನು ಹಾರ್ಡ್-ಕೋಡ್ ಮಾಡಿದ್ದವು; ಈಗ ಅವು ಡಿಫಾಲ್ಟ್ ಆಗಿ `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) ಬಳಸುತ್ತವೆ. ಒಂದು semple ಬಹುಮಾಧ್ಯಮ / ದೃಶ್ಯ ಇನ್ಪುಟ್ ಮೇಲೆ ಅವಲಂಬಿತ ಇದಾದರೆ, phùರುವಷ್ಟು ಸೂಕ್ತ ಮಾದರಿಗಾಗಿ `AZURE_OPENAI_DEPLOYMENT` ಅನ್ನು ಸೆಟ್ ಮಾಡಿ.
- **ಫೌಂಡ್ರಿ ಲೋಕಲ್** ಒಬ್ಬ OpenAI-ಅನುಕೂಲ **ಚಾಟ್ ಪೂರ್ಣಗೊಳಿಸುವಿಕೆ**‌ಗಳ ಮುಕ್ತಾಯವನ್ನು ಒದಗಿಸುತ್ತದೆ ಮತ್ತು ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಗಾಗಿಯೇ ಉದ್ದೇಶಿಸಲಾಗಿದೆ; Responses API ವೈಶಿಷ್ಟ್ಯ ಸಂಪೂರ್ಣಕ್ಕಾಗಿ ಅಜೂರ್ ಓಪನ್‌ಎಐ / ಮೈನಕ್ರೋಸಾಫ್ಟ್ ಫೌಂಡ್ರಿಯನ್ನು ಬಳಸಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->