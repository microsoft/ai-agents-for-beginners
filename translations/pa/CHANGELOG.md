# ਚેન્જਲੌਗ

**ਸਰਲ ਸ਼ੁਰੂਆਤੀ ਲਈ ਏਆਈ ਏਜੰਟਸ** ਕੋਰਸ ਵਿੱਚ ਸਾਰੇ ਮਹੱਤਵਪੂਰਨ ਬਦਲਾਅ ਇਸ ਫਾਈਲ ਵਿੱਚ ਦਰਜ ਹਨ।

## [ਜਾਰੀ ਕੀਤਾ] — 2026-07-14

ਇਸ ਰਿਲੀਜ਼ ਨਾਲ ਕੋਰਸ ਦੋ ਨਵੀਂ ਡੇਪਰਕੀਟਿਡ ਮਾਡਲਾਂ ਤੋਂ ਹਟਾ ਦਿੱਤਾ ਗਿਆ ਹੈ, ਬਾਕੀ ਬਚੇ ਹੋਏ ਲੈਸਨ ਨੋਟਬੁੱਕਸ ਨੂੰ ਸਥਿਰ ਮਾਈਕ੍ਰੋਸਾਫਟ ਏਜੰਟ ਫਰੇਮਵਰਕ ਏਪੀਆਈ ਨਾਲ ਮਾਈਗ્રੇਟ ਕੀਤਾ ਗਿਆ ਹੈ, ਅਤੇ ਪਾਈਥਨ ਨੋਟਬੁੱਕਸ ਨੂੰ ਲਾਈਵ ਮਾਈਕ੍ਰੋਸਾਫਟ ਫਾਊਂਡਰੀ ਡਿਪਲੋਇਮੈਂਟ ਖ਼ਿਲਾਫ਼ ਸਤਿਆਪਿਤ ਕੀਤਾ ਗਿਆ ਹੈ।

### ਬਦਲਾਅ

- **ਡੇਪਰਕੀਟਿਡ ਮਾਡਲਾਂ (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`) ਤੋਂ ਖਸੇਲ ਗਿਆ।** ਦੋਹਾਂ `gpt-4.1` ਅਤੇ `gpt-4.1-mini` ਹੁਣ ਡੇਪਰਕੀਟਿਡ ਹਨ (ਛਾਪਨ ਦੀ ਸਮਾਪਤੀ ਦੀ ਤਾਰੀਖ **14 ਅਕਤूबर 2026**). ਹਰ ਕੋਰਸ ਸੰਦਰਭ (ਡੌਕਸ, `.env.example`, ਪਾਈਥਨ/.NET ਨੋਟਬੁੱਕਸ ਅਤੇ ਨਮੂਨੇ) ਨੂੰ ਗੈਰ-ਡੇਪਰਕੀਟਿਡ `gpt-5-mini` ਨਾਲ ਬਦਲ ਦਿੱਤਾ ਗਿਆ। ਲੈਸਨ 16 ਦਾ ਮਾਡਲ-ਰੂਟਿੰਗ ਉਦਾਹਰਣ ਛੋਟੀ/ਵੱਡੀ ਤੁਲਨਾ ਨਾਲ `gpt-5-nano` (ਛੋਟਾ) ਅਤੇ `gpt-5-mini` (ਵੱਡਾ) ਵਰਤਦਾ ਹੈ। ਵੇਂਡਰ ਕਰਕੇ ਤੀਸਰੇ ਪੱਖ ਦੇ ਫਾਈਲਾਂ ([15-browser-use/llms.txt](../../15-browser-use/llms.txt)), ਇਤਿਹਾਸਕ GitHub ਮਾਡਲ ਟੈਕਸਟ, ਅਤੇ `azure-openai-to-responses` ਸਕਿਲ ਦੀ ਸਮਰਥਾ ਨੋਟਸ ਜਾਣਬੂਝ ਕੇ ਬਦਲੇ ਬਿਨਾਂ ਰਹੇ।
- **ਲੈਸਨ 14 ਹੈਂਡਆਫ਼ ਨੋਟਬੁੱਕ ਨੂੰ ਸਥਿਰ ਏਪੀਆਈ ਤੇ ਮਾਈਗ੍ਰੇਟ ਕੀਤਾ।** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) ਹੁਣ `agent_framework.orchestrations.HandoffBuilder` ਨਾਲ `.with_start_agent(...)`, `HandoffAgentUserRequest.create_response(...)`, `event.type`-ਆਧਾਰਿਤ ਸਟ੍ਰੀਮਿੰਗ, ਅਤੇ `FoundryChatClient` ਵਰਤਦਾ ਹੈ (ਪਹਿਲੇ ਹਟਾਏ ਗਏ pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` ਚਿੰਨਾਂ ਦੀ ਥਾਂ)।
- **ਲੈਸਨ 14 ਹਿਊਮਨ-ਇਨ-ਦ-ਲੂਪ ਨੋਟਬੁੱਕ ਸਥਿਰ ਏਪੀਆਈ ਤੇ ਮਾਈਗ੍ਰੇਟ ਕੀਤਾ।** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) ਹੁਣ `ctx.request_info(...)` + `@response_handler` ਰਾਹੀਂ ਰੋਕਦਾ ਹੈ (ਪਹਿਲਾਂ ਹਟਾਏ ਗਏ `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse` ਦੀ ਥਾਂ), `WorkflowBuilder(start_executor=..., output_executors=[...])` ਨਾਲ ਬਣਾਉਂਦਾ ਹੈ, `default_options={"response_format": ...}` ਰਾਹੀਂ ਸਹੁਲਤਵਾਰ ਨਤੀਜੇ ਦਿੰਦਾ ਹੈ, ਅਤੇ ਸਕ੍ਰਿਪਟ ਕੀਤੀ ਜਵਾਬ ਨਾਲ ਨੋਟਬੁੱਕ ਬਿਨਾਂ ਬੰਦ ਹੋਏ ਚਲਦਾ ਹੈ (`input()` ਨੂੰ ਰੋਕਦਾ ਨਹੀਂ)।
- **ਵਾਤਾਵਰਨ ਸੰਰਚਨਾ** ([.env.example](../../.env.example)): ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਨਾਮਾਂ ਨੂੰ `gpt-5-mini` ਵਿੱਚ ਬਦਲਿਆ; ਸ਼ਾਮਿਲ ਕੀਤੇ `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL` (ਲੈਸਨ 16 ਰੂਟਿੰਗ) ਅਤੇ ਪਹਿਲਾਂ ਨਾ ਰਹਿਣ ਵਾਲਾ `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` (ਲੈਸਨ 15 ਬ੍ਰਾਉਜ਼ਰ-ਯੂਜ਼)।
- **ਲੋੜੀਂਦੇ ਪੈਕੇਜ** ([requirements.txt](../../requirements.txt)): `agent-framework`, `agent-framework-foundry`, ਅਤੇ `agent-framework-openai` ਨੂੰ `~=1.10.0` ਤੇ ਤੈਅ ਕੀਤਾ ਗਿਆ ਤਾਕਿ ਇੱਕ ਖੁਦ-ਮੁਤਾਬਿਕ, ਸਤਿਆਪਿਤ ਸੈੱਟ ਬਣਾਏ (1.11.0 ਵਿੱਚ ਇਹ ਲੈਸਨਾਂ ਲਈ ਸਤਹਾਂ ਨੂੰ ਬਦਲਨ ਵਾਲੇ ਤਜਰਬਾਤੀ ਤਬਦੀਲੀਆਂ ਸ਼ਾਮਿਲ ਹਨ)।

### ਨੋਟਸ ਅਤੇ ਜਾਣੀਆਂ ਸੀਮਾਵਾਂ

- **ਲਾਈਵ ਮਾਈਕ੍ਰੋਸਾਫਟ ਫਾਊਂਡਰੀ ਖ਼ਿਲਾਫ਼ ਸਤਿਆਪਿਤ ਕੀਤਾ।** ਪਾਈਥਨ ਨੋਟਬੁੱਕਸ ਨੂੰ `nbconvert` ਨਾਲ ਬਿਨਾਂ ਮੁੱਖ ਤੋਂ ਚਲਾਇਆ ਗਿਆ Microsoft Foundry ਪ੍ਰੋਜੈਕਟ ਤੇ ਜਿਸ ਵਿੱਚ `gpt-5-mini` (ਅਤੇ ਲੈਸਨ 16 ਰੂਟਿੰਗ ਲਈ `gpt-5-nano`) ਵਰਤੇ ਗਏ। ਤੁਸੀਂ ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਬਰਾਬਰ ਗੈਰ-ਡੇਪਰਕੀਟਿਡ ਮਾਡਲਾਂ ਡਿਪਲੋਇ ਕਰ ਸਕਦੇ ਹੋ; ਨੋਟਬੁੱਕ ਅਧਾਰਿਤ ਡਿਪਲੋਇਮੈਂਟ ਨਾਮ `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` ਤੋਂ ਪੜ੍ਹਦੇ ਹਨ।
- **ਕੁਝ ਲੈਸਨਾਂ ਲਈ ਵਧੀਕ ਸਰੋਤ ਲੋੜੀਂਦੇ।** ਲੈਸਨ 05 ਨੂੰ Azure AI Search ਦੀ ਲੋੜ ਹੈ; ਲੈਸਨ 08 ਬਿੰਗ-ਗ੍ਰਾਊਂਡਿੰਗ ਵਰਕਫ਼ਲੋ (`04.python-agent-framework-workflow-aifoundry-condition.ipynb`) ਨੂੰ ਬਿੰਗ ਕਨੈਕਸ਼ਨ ਅਤੇ ਮਾਈਕ੍ਰੋਸਾਫਟ ਫਾਊਂਡਰੀ ਏਜੰਟ ਸਰਵਿਸ ਹੋਸਟ ਕੀਤੀਆਂ ਟੂਲਜ਼ ਦੀ ਲੋੜ ਹੈ; ਲੈਸਨ 13 (Cognee) ਅਤੇ ਲੈਸਨ 17 (Foundry Local) ਨੂੰ ਆਪਣਾ ਦੇਸਥਾਨਕ ਰਨਟਾਈਮ ਚਾਹੀਦਾ ਹੈ।

## [ਜਾਰੀ ਕੀਤਾ] — 2026-07-13

ਇਸ ਰਿਲੀਜ਼ ਨਾਲ ਦੋ ਨਵੇਂ ਲੈਸਨ ਜੋੜੇ ਗਏ ਹਨ ਜੋ ਡਿਪਲੋਇਮੈਂਟ ਕ੍ਰਮ ਨੂੰ ਪੂਰਾ ਕਰਦੇ ਹਨ — ਏਜੰਟਸ ਨੂੰ ਮਾਈਕ੍ਰੋਸਾਫਟ ਫਾਊਂਡਰੀ ਤੇ ਵਧਾਉਣਾ ਅਤੇ ਇਕੱਲੇ ਕੰਮ ਵਾਲੇ ਕੰਪਿਊਟਰ ਤੱਕ ਘਟਾਉਣਾ — ਨਾਲ ਨਾਲ ਸ್ಮੋਕ-ਟੈਸਟ ਪਾਈਪਲਾਈਨ, ਤਾਜ਼ਾ ਕੋਰਸ ਨੈਵੀਗੇਸ਼ਨ, ਨਵੇਂ ਸਿੱਖਣ ਵਾਲੇ ਕੌਸ਼ਲ, ਅਤੇ ਅਪਡੇਟਡ ਬ੍ਰਾਂਡਿੰਗ।

### ਸ਼ਾਮਿਲ ਕੀਤਾ

- **ਲੈਸਨ 16 — ਮਾਈਕ੍ਰੋਸਾਫਟ ਫਾਊਂਡਰੀ ਨਾਲ ਸਕੇਲਬਲ ਏਜੰਟ ਦੀ ਤਿਆਰੀ।** ਨਵਾਂ ਲੈਸਨ [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) ਅਤੇ ਚਲਾਉਣਯੋਗ ਨੋਟਬੁੱਕ [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb) ਜੋ ਇੱਕ ਉਤਪਾਦਨ ਗਾਹਕ ਸਹਾਇਤਾ ਏਜੰਟ ਬਣਾਉਂਦਾ ਹੈ (ਟੂਲ, RAG, ਮੈਮੋਰੀ, ਮਾਡਲ ਰੂਟਿੰਗ, ਜਵਾਬ ਕੈਸ਼ਿੰਗ, ਮਨੁੱਖੀ ਮਨਜ਼ੂਰੀ, ਮੁਲਾਂਕਣ ਵਾਲਾ ਦਰਵਾਜ਼ਾ ਅਤੇ OpenTelemetry ਟਰੇਸਿੰਗ), ਨਾਲ ਵਿਕਾਸ/ਡਿਪਲੋਇਮੈਂਟ/ਰੰਨਟਾਈਮ Mermaid ਡਾਇਗਰਾਮ, ਗਿਆਨ ਜਾਂਚ, ਇੱਕ ਐਸਾਈਨਮੈਂਟ ਅਤੇ ਇੱਕ ਚੁਣੌਤੀ।
- **ਲੈਸਨ 17 — Foundry Local ਅਤੇ Qwen ਨਾਲ ਸਥਾਨਕ ਏਆਈ ਏਜੰਟ ਬਣਾਉਣਾ।** ਨਵਾਂ ਲੈਸਨ [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) ਅਤੇ ਨੋਟਬੁੱਕ [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb) ਜੋ ਇੱਕ ਪੂਰੀ ਤਰ੍ਹਾਂ ਡਿਵਾਈਸ ‘ਤੇ ਇੰਜੀਨੀਅਰਿੰਗ ਸਹਾਇਕ ਤਿਆਰ ਕਰਦਾ ਹੈ (Foundry Local ਰਾਹੀਂ Qwen ਫੰਕਸ਼ਨ ਕਾਲਿੰਗ, ਸੈਂਡਬਾਕਸਡ ਫਾਈਲ ਟੂਲਜ਼, ਸਥਾਨਕ RAG ਚਰੋਮਾ ਨਾਲ, ਵਿਕਲਪਿਕ ਸਥਾਨਕ MCP), ਨਾਲ ਸਥਾਨਕ / ਸਥਾਨਕ-RAG / ਟੂਲ ਕਾਲਿੰਗ ਡਾਇਗਰਾਮ, ਗਿਆਨ ਜਾਂਚ, ਐਸਾਈਨਮੈਂਟ ਅਤੇ ਚੁਣੌਤੀ।
- **ਸਮੋਕ-ਟੈਸਟ ਪਾਈਪਲਾਈਨ।** ਨਵਾਂ [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) ਵਰਕਫਲੋ [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) ਨਾਲ ਨਾਲ ਪ੍ਰਤੀ ਲੈਸਨ ਕੈਟਾਲੌਗ [tests/](./tests/README.md) ਅਧਾਰਿਤ ਡਿਪਲੋਇ ਕਰਨ ਯੋਗ ਏਜੰਟਸ ਲਈ ਜੋ ਲੈਸਨ 01, 04, 05 ਅਤੇ 16 ਵਿੱਚ ਹਨ, ਇੱਕ ਇੰਡੈਕਸ README ਹਰ ਕੈਟਾਲੌਗ ਨੂੰ ਮੂਲ ਲੈਸਨ ਅਤੇ ਹੋਸਟ ਕੀਤੇ ਏਜੰਟ ਨਾਮ ਨਾਲ ਜੋੜਦਾ ਹੈ। ਲੈਸਨ 16 ਨੂੰ "ਸਮੋਕ ਟੈਸਟ ਨਾਲ ਡਿਪਲੋਇਡ ਏਜੰਟ ਦੀ ਵੈਰੀਫਿਕੇਸ਼ਨ" ਸੈਕਸ਼ਨ ਮਿਲਦਾ ਹੈ; ਲੈਸਨ 01/04/05 ਨੂੰ ਐਕਸ਼ਨਸਮਾਜ਼ ਸਮੋਕ-ਟੈਸਟ ਪોઈਂਟਰ ਮਿਲਦਾ ਹੈ।
- **ਸਿੱਖਣ ਵਾਲੇ ਕੌਸ਼ਲ।** ਨਵੇਂ ਏਜੰਟ ਸKills `.agents/skills/` ਹੇਠ: [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md), [local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md) (ਲੈਸਨ 16 ਅਤੇ 17 ਦੇ ਨੇਤ੍ਰਤਵ ਨੂੰ ਪੈਕੇਜ ਕਰਦੇ), ਅਤੇ [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md) (ਕਿਸ ਤਰ੍ਹਾਂ ਨੋਟਬੁੱਕ ਨਮੂਨਿਆਂ ਨੂੰ ਜੀਵੰਤ Microsoft Foundry / Azure OpenAI ਸੈਟਅੱਪ ਨਾਲ ਸਤਿਆਪਿਤ ਕਰਨਾ)।
- **ਨੋਟਬੁੱਕ ਵੈਰੀਫਿਕੇਸ਼ਨ ਦੌੜਾਵਣ ਵਾਲਾ।** ਨਵਾਂ [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1) ਜੋ ਹਰ ਪਾਈਥਨ ਨੋਟਬੁੱਕ ਨੂੰ ਬਿਨਾ ਮੁੱਖ ਤੋਂ `nbconvert` ਨਾਲ ਚਲਾਉਂਦਾ ਹੈ ਅਤੇ PASS/FAIL ਮੈਟਰਿਕਸ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ (ਅਤੀਰਕ `results.json` ਨਾਲ). ਇਹ ਆਟੋਮੈਟਿਕ ਰੇਪੋ ਰੂਟ ਅਤੇ ਪਾਈਥਨ ਪਤਾ ਲਗਾਉਂਦਾ ਹੈ, ਗੈਰ-ਕੋਰਸ ਨੋਟਬੁੱਕਸ (`.venv`, `site-packages`, `translations`, ਸਕਿਲ ਟੈਂਪਲੇਟ ਐਸੈਟਸ) ਅਤੇ `.NET` ਨੋਟਬੁੱਕਸ ਨੂੰ ਡਿਫਾਲਟ ਨਾਲ ਬਾਹਰ ਕਰਦਾ ਹੈ, ਅਤੇ `-Filter`, `-Timeout`, `-List`, `-IncludeDotnet`, ਅਤੇ `-Python` ਨੂੰ ਸਹਾਰਦਾ ਹੈ।
- **ਕੋਰਸ ਨੈਵੀਗੇਸ਼ਨ।** ਲੈਸਨ 11-15 ਵਿੱਚ ਪਿਛਲਾ/ਅਗਲਾ ਲੈਸਨ ਲਿੰਕ ਸ਼ਾਮਿਲ ਕੀਤਾ ਗਿਆ ਜੋ ਪਹਿਲਾਂ ਮੌਜੂਦ ਨਹੀਂ ਸੀ, ਤਾਂ ਜੋ ਪੂਰਾ ਕੋਰਸ 00 → 18 ਦੋਹਾਂ ਦਿਸ਼ਾਵਾਂ ਵਿੱਚ ਜੁੜੇ।
- **ਨਵੇਂ ਥੰਬਨੇਲ।** ਲੈਸਨ 16 ਅਤੇ 17 ਲਈ ਲੈਸਨ ਥੰਬਨੇਲ, ਨਾਲ ਨਾਲ ਤਾਜ਼ਾ ਕੀਤਾ ਹੋਇਆ ਰਿਪੋਜਿਟਰੀ ਸੋਸ਼ਲ ਇਮੇਜ [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png) (ਹੁਣ ਦੋ ਨਵੇਂ ਲੈਸਨਾਂ ਅਤੇ `aka.ms/ai-agents-beginners` URL ਨੂੰ ਪ੍ਰਚਾਰਤਾ ਹੈ)।
- **ਲੋੜੀਂਦੇ ਪੈਕੇਜ** ([requirements.txt](../../requirements.txt)): ਲੈਸਨ 17 ਲਈ `foundry-local-sdk` ਅਤੇ `chromadb` ਜੋੜੇ ਗਏ।

### ਬਦਲਾਅ

- **ਮੁੱਖ [README.md](./README.md)** ਲੈਸਨ ਸੂਚੀ: ਲੈਸਨ 16 ਅਤੇ 17 ਹੁਣ ਆਪਣੇ ਸਮੱਗਰੀ ਨਾਲ ਜੋੜੇ ਗਏ (ਪਹਿਲਾਂ "ਜਲਦੀ ਆ ਰਹੇ ਸੀ"); ਰਿਪੋਜਿਟਰੀ ਦੀ ਤਸਵੀਰ `repo-thumbnailv3.png` ਵਿੱਚ ਬਦਲ ਗਈ।
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**: ਲੈਸਨ 16 ਅਤੇ 17 ਲੈਸਨ-ਦਰ-ਲੈਸਨ ਗਾਈਡ ਅਤੇ ਸਿੱਖਣ ਵਾਲੇ ਮਾਰਗ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕੀਤੇ, ਅਤੇ "ਸਮੋਕ ਟੈਸਟ ਨਾਲ ਡਿਪਲੋਇਡ ਏਜੰਟ ਦੀ ਵੈਰੀਫਿਕੇਸ਼ਨ" ਸੈਕਸ਼ਨ।
- **[AGENTS.md](./AGENTS.md)**: ਲੈਸਨ ਗਿਣਤੀ/ਵਰਣਨ ਵਿੱਚ ਤਬਦੀਲੀ (00–18), ਸਮੋਕ-ਟੈਸਟਿੰਗ ਵੈਰੀਫਿਕੇਸ਼ਨ ਸੈਕਸ਼ਨ ਸ਼ਾਮਿਲ ਕੀਤਾ, ਅਤੇ ਲੈਸਨ 16/17 ਦੇ ਨਮੂਨਾ-ਨਾਂ ਦੇ ਉਦਾਹਰਣ ਜੋੜੇ।
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**: "ਪਿਛਲਾ ਲੈਸਨ" ਹੁਣ ਲੈਸਨ 17 ਵੱਲ ਹਵਾਲਾ ਦਿੰਦਾ ਹੈ (ਪਹਿਲਾਂ ਲੈਸਨ 15 ਸੀ), ਚੇਨ ਬੰਦ ਕਰਦਾ ਹੈ।
- **ਗੈਰ-ਡੇਪਰਕੀਟਿਡ ਮਾਡਲਾਂ ਤੇ ਮਾਡਲ ਸੰਦਰਭਾਂ ਦਾ ਸਧਾਰਣੀਕਰਨ।** ਸਾਰੇ `gpt-4o` / `gpt-4o-mini` ਹਵਾਲੇ (ਡੌਕਸ, `.env.example`, ਪਾਈਥਨ/.NET ਨੋਟਬੁੱਕਸ ਅਤੇ ਨਮੂਨੇ) ਨੂੰ `gpt-4.1-mini` ਨਾਲ ਬਦਲਾ ਗਿਆ — `gpt-4o` (ਸਾਰੇ ਵਰਜਨ) 2026 ਵਿੱਚ ਰਿਟਾਇਰ ਹੋ ਰਿਹਾ ਹੈ। ਲੈਸਨ 16 ਦਾ ਮਾਡਲ-ਰੂਟਿੰਗ ਉਦਾਹਰਣ ਛੋਟੀ/ਵੱਡੀ ਤੁਲਨਾ `gpt-4.1-mini` (ਛੋਟਾ) ਅਤੇ `gpt-4.1` (ਵੱਡਾ) ਨਾਲ ਰੱਖਦਾ ਹੈ। ਪਾਈਥਨ ਨੋਟਬੁੱਕ ਹੁਣ ਮਾਡਲ ਨਾਮ ਹਾਰਡ-ਕੋਡ ਕਰਨ ਦੀ ਥਾਂ ਵਾਤਾਵਰਨ ਵੈਰੀਏਬਲਜ਼ (`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`) ਤੋਂ ਮਾਡਲ ਚੁਣਦੇ ਹਨ।

### ਨੋਟਸ ਅਤੇ ਜਾਣੀਆਂ ਸੀਮਾਵਾਂ

- **ਲਾਈਵ Azure ਖ਼ਿਲਾਫ਼ ਨਹੀਂ ਚਲਾਏ ਗਏ।** ਨਵੇਂ ਲੈਸਨਾਂ ਦੇ ਨੋਟਬੁੱਕ ਸਿੱਖਣ ਵਾਲੇ ਨਮੂਨੇ ਹਨ; ਆਪਣੇ Microsoft Foundry / Foundry Local ਸੈਟਅੱਪ 'ਤੇ ਚਲਾ ਕੇ ਸਤਿਆਪਿਤ ਕਰੋ। ਸਮੋਕ-ਟੈਸਟ ਵਰਕਫਲੋ ਸਮੇਂ ਤੱਕ ਤੁਹਾਨੂੰ ਲੈਸਨ ਦੇ ਏਜੰਟ ਨੂੰ ਡਿਪਲੋਇ ਕਰਨਾ ਅਤੇ Azure OIDC ਸੀਕ੍ਰੇਟਸ (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) ਨੂੰ **Azure AI User** ਭੂਮਿਕਾ ਨਾਲ Foundry ਪ੍ਰੋਜੈਕਟ ਸਥਾਨ ਤੇ ਨਿਰਧਾਰਿਤ ਕਰਨਾ ਲਾਜ਼ਮੀ ਹੈ।
- **ਲੈਸਨ 17 ਸਿਰਫ ਸਥਾਨਕ ਹੈ।** ਇਸ ਵਿੱਚ ਕੋਈ Foundry Responses ਐਂਡਪੌਇੰਟ ਨਹੀਂ ਹੈ, ਇਸ ਲਈ ਸਮੋਕ-ਟੈਸਟ ਕਾਰਜ ਅਮਲ ਨਹੀਂ ਹੁੰਦਾ; ਇਸਨੂੰ ਆਪਣੇ ਕੰਮ ਵਾਲੀ ਜਗ੍ਹਾ ਤੇ ਨੋਟਬੁੱਕ ਚਲਾ ਕੇ ਵੈਰੀਫਾਈ ਕਰੋ।

## [ਜਾਰੀ ਕੀਤਾ] — 2026-07-06

ਇਸ ਰਿਲੀਜ਼ ਨਾਲ ਕੋਰਸ ਨੂੰ **Azure OpenAI Responses API** ਤੇ ਮਾਈਗ੍ਰੇਟ ਕੀਤਾ ਗਿਆ, ਉਤਪਾਦ ਨਾਮਾਵਲੀ ਨੂੰ **Microsoft Foundry** ਅਤੇ **Microsoft Agent Framework (MAF)** 'ਤੇ ਸਧਾਰਣ ਕੀਤਾ, GitHub Models ਨੂੰ ਰਿਟਾਇਰ ਕੀਤਾ, SDK ਵਰਸਨਾਂ ਨੂੰ ਅਪਡੇਟ ਕੀਤਾ, ਅਤੇ ਨਵੇਂ ਸਮੱਗਰੀ ਜੋੜੀ ਜੋ ਸਥਾਨਕ ਮਾਡਲਾਂ ਤੇ ਹੋਰ ਫਰੇਮਵਰਕਸ ਨੂੰ Foundry ਤੇ ਹੋਸਟ ਕਰਦੀ ਹੈ।

### ਸ਼ਾਮਿਲ ਕੀਤਾ

- **ਮਾਈਗ੍ਰੇਸ਼ਨ ਸਕਿਲ** — [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) ਏਜੰਟ ਸਕਿਲ (ਤੁਲਨਾਤਮਕ [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)) `.agents/skills/` ਤਹਿਤ ਇੰਸਟਾਲ ਕੀਤਾ, ਜਿਸ ਵਿੱਚ ਇਸਦੇ ਹਵਾਲੇ ਅਤੇ ਸਕੈਨਰ ਸਕ੍ਰਿਪਟ ਹਨ।
- **Foundry Local (ਡਿਵਾਈਸ ਤੇ ਮਾਡਲ ਚਲਾਓ)** — [00-course-setup/README.md](./00-course-setup/README.md) ਵਿੱਚ ਨਵਾਂ "ਵਿਕਲਪਿਕ ਪ੍ਰਦਾਤਾ: Foundry Local" ਸੈਕਸ਼ਨ ਜੋ ਇੰਸਟਾਲ (`winget` / `brew`), `foundry model run`, `foundry-local-sdk`, ਅਤੇ Microsoft Agent Framework ਨੂੰ `OpenAIChatClient` ਰਾਹੀਂ ਜੋੜਦਾ ਹੈ।
- **Microsoft Foundry ‘ਤੇ LangChain / LangGraph ਏਜੰਟਸ ਹੋਸਟ ਕਰਨਾ** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) ਵਿੱਚ ਨਵਾਂ ਸੈਕਸ਼ਨ ਅਤੇ ਦੌੜਾਉਣਯੋਗ ਨਮੂਨਾ [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ਜੋ `langchain-azure-ai[hosting]` ਅਤੇ `ResponsesHostServer` ( `/responses` ਪ੍ਰੋਟੋਕੋਲ) ਵਰਤਦਾ ਹੈ, ਬੇਸڈ Microsoft Learn ਅਧਾਰਿਤ ਹੈ।
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) ਵਿੱਚ ਨਵਾਂ "ਅਸਲੀ ਦੁਨੀਆ ਦਾ ਉਦਾਹਰਣ: Microsoft Project Opal" ਸੈਕਸ਼ਨ ਜੋ Opal ਨੂੰ ਉਦਯੋਗਿਕ ਕੰਪਿਊਟਰ-ਯੂਜ਼ ਏਜੰਟ ਵਜੋਂ ਦਰਸਾਉਂਦਾ ਹੈ ਅਤੇ ਕੋਰਸ ਸੰਕਲਪਾਂ ਨਾਲ ਜੋੜਦਾ ਹੈ (ਮਨੁੱਖ-ਇਨ-ਦ-ਲੂਪ, ਭਰੋਸਾ/ਸੁਰੱਖਿਆ, ਯੋਜਨਾ, ਸਕਿਲ)।
- **ਦੂਜਾ ਲੈਸਨ 02 ਪਾਈਥਨ ਨਮੂਨਾ** — [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb) ਜੋੜਿਆ (ਦੇਖੋ "ਬਦਲਾਅ" — ਪੁਰਾਣੇ Semantic Kernel ਨੋਟਬੁੱਕ ਤੋਂ ਮਾਈਗ੍ਰੇਟ ਕੀਤਾ) ਅਤੇ ਲੈਸਨ README ’ਚ ਜੋੜਿਆ।
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)** ਵਿੱਚ ਮਾਡਲ ਅਤੇ ਪ੍ਰਦਾਤਾ ਭਾਗ ਜੋੜਿਆ।

### ਬਦਲਾਅ

- **ਚੈਟ ਕੰਪਲੀਟਸਨ → Responses API (ਪਾਈਥਨ).** ਮਾਡਲ ਨੂੰ ਸਿੱਧਾ ਕਾਲ ਕਰਨ ਵਾਲੇ ਨਮੂਨੇ ਚੈਟ ਕੰਪਲੀਸ਼ਨ ਤੋਂ Responses API (`client.responses.create(input=..., store=False)`, `resp.output_text`) ਤੇ ਮਾਈਗ੍ਰੇਟ ਕੀਤੇ ਗਏ, ਜੋ ਸਥਿਰ Azure OpenAI `/openai/v1/` ਐਂਡਪੌਇੰਟ (`api_version` ਬਿਨਾਂ) ਨਾਲ `OpenAI` ਕਲੀਅੰਟ ਵਰਤਦਾ ਹੈ। ਪ੍ਰਭਾਵਿਤ ਨਮੂਨੇ ਸ਼ਾਮਿਲ ਹਨ:
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04-tool-use/README.md) — ਪੂਰਾ ਫੰਕਸ਼ਨ-ਕਾਲਿੰਗ ਵਾਕਥਰੂ (ਟੂਲ ਸਕੀਮਾ Responses ਫਾਰਮੈਟ ਵਿੱਚ ਘਟਾਇਆ, ਟੂਲ ਦੇ ਨਤੀਜੇ `function_call_output`, `max_output_tokens` ਆਦਿ ਵਜੋਂ ਮੁੜ ਮਿਲਦੇ ਹਨ)।

- **GitHub ਮਾਡਲ → Azure OpenAI.** GitHub ਮਾਡਲ ਹਟਾਏ ਜਾ ਰਹੇ ਹਨ (ਜੁਲਾਈ 2026 ਨੂੰ ਰਿਟਾਇਰ ਹੋਣਗੇ) ਅਤੇ Responses API ਦਾ ਸਹਾਰਾ ਨਹੀਂ ਦਿੰਦੇ। ਸਾਰੇ GitHub ਮਾਡਲ ਕੋਡ ਪਾਥ Azure OpenAI / Microsoft Foundry ਵਿੱਚ Python ਅਤੇ .NET ਨਮੂਨਾਂ ਵਿੱਚ ਬਦਲੇ ਗਏ ਹਨ:
  - Python: ਸਬਕ 08 ਵਰਕਫਲੋ ਨੋਟਬੁੱਕਸ (`01`–`03`), ਸਬਕ 14 (`14-handoff`, `14-human-loop`, `hotel_booking_workflow_sample.py`)।
  - .NET: `01`–`04`, `07`, `08` `*-dotnet-agent-framework.cs` + ਸਾਥੀ `.md` ਡੌਕਸ, ਅਤੇ ਸਬਕ 08 dotNET ਵਰਕਫਲੋ ਨੋਟਬੁੱਕਸ/`.md` (`01`–`03`) ਹੁਣ `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` ਨਾਲ `AzureCliCredential` ਵਰਤਦੇ ਹਨ।
- **Semantic Kernel → Microsoft Agent Framework.** ਪਹਿਲਾਂ ਵਾਲਾ `02-semantic-kernel.ipynb` Microsoft Agent Framework ਨਾਲ Azure OpenAI (Responses API) ਵਰਤ ਕੇ ਮੁੜ ਲਿਖਿਆ ਗਿਆ ਅਤੇ ਨਾਮ ਬਦਲ ਕੇ `02-python-agent-framework-azure-openai.ipynb` ਕੀਤਾ ਗਿਆ।
- **`FoundryChatClient` + `as_agent` ਤੇ ਮਿਆਰੀਕਰਨ ਕੀਤਾ।** README ਅਤੇ ਨੋਟਬੁੱਕ ਕੋਡ ਜੋ `AzureAIProjectAgentProvider` ਨੂੰ ਦਰਸਾਉਂਦਾ ਸੀ, ਉਹ ਸਬਕ 01 ਅਤੇ ਫਰੇਮਵਰਕ ਦੇ ਆਪਣੇ ਨਮੂਨਿਆਂ ਵੱਲੋਂ ਵਰਤੇ ਗਏ ਮੁੱਖ ਪੈਟਰਨ ਤੇ ਮਿਆਰੀਕਰਨ ਕੀਤਾ ਗਿਆ: `FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` ਨਾਲ `provider.as_agent(...)`। ਇਹ ਸਬਕ 02–14 READMEs ਅਤੇ ਨੋਟਬੁੱਕਸ, ਜਿਵੇਂ ਕਿ ਸਬਕ 13 ਮੈਮੋਰੀ, ਸਾਰੇ ਸਬਕ 14 ਨੋਟਬੁੱਕਸ, `11-agentic-protocols/code_samples/github-mcp/app.py` ਵਿੱਚ ਅਪਡੇਟ ਕੀਤਾ ਗਿਆ।
- **ਉਤਪਾਦ ਦਾ ਨਾਮਕਰਨ।** ਅੰਗ੍ਰੇਜ਼ੀ ਸਮੱਗਰੀ ਵਿੱਚ ਪੂਰੇ ਸਿਸਟਮ ਵਿੱਚ ਨਾਮ ਬਦਲਿਆ:
  - "Azure AI Foundry" / "Azure AI Studio" → **Microsoft Foundry**
  - "Azure AI Agent Service" → **Microsoft Foundry Agent Service**
  - (ਬਦਲਾਅ ਨਹੀਂ: "Azure OpenAI", "Azure AI Search", "Azure AI Inference", ਅਤੇ ਵਾਤਾਵਰਣ-ਵੈਰੀਏਬਲ ਨਾਮ।)
- **ਡਿਪੈਂਡੈਂਸੀਜ਼** ([requirements.txt](../../requirements.txt)):
  - `agent-framework>=1.10.0`, `agent-framework-foundry>=1.10.0`, `agent-framework-openai>=1.10.0` ਨਿਸ਼ਚਿਤ ਕੀਤੀਆਂ ਗਈਆਂ।
  - `openai>=1.108.1` (Responses API ਲਈ ਘੱਟੋ-ਘੱਟ ਸੰਸਕਰਨ) ਨਿਸ਼ਚਿਤ ਕੀਤੀ।
  - `azure-ai-inference` ਨੂੰ ਹਟਾਇਆ ਗਿਆ (ਹੁਣ ਸਿਰਫ਼ GitHub ਮਾਡਲ ਨਮੂਨਿਆਂ ਵੱਲੋਂ ਵਰਤਿਆ ਜਾਂਦਾ ਸੀ ਜੋ ਮਾਈਗ੍ਰੇਟ ਹੋ ਚੁੱਕੇ ਹਨ)।
- **ਵਾਤਾਵਰਣ ਸੰਰਚਨਾ** ([.env.example](../../.env.example)): GitHub ਮਾਡਲ ਵੈਰੀਏਬਲ ਹਟਾਏ (`GITHUB_TOKEN`, `GITHUB_ENDPOINT`, `GITHUB_MODEL_ID`) ਤੇ `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, ਅਤੇ ਵਿਕਲਪਿਕ `AZURE_OPENAI_API_KEY` ਸ਼ਾਮਿਲ ਕੀਤੇ; ਨਾਮਕਰਨ Microsoft Foundry ਲਈ ਅਪਡੇਟ ਕੀਤਾ।
- **ਦਸਤਾਵੇਜ਼** — [00-course-setup/README.md](./00-course-setup/README.md), [AGENTS.md](./AGENTS.md), [README.md](./README.md), ਅਤੇ [STUDY_GUIDE.md](./STUDY_GUIDE.md) ਨੂੰ ਉਪਰੋਕਤ ਅਨੁਸਾਰ ਅਪਡੇਟ ਕੀਤਾ (ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਸੈਟ ਕਰਨਾ, ਜਾਂਚ ਸਪਲਿਟ, ਪ੍ਰਦਾਤਾ ਮਾਰਗਦਰਸ਼ਨ, ਨਾਮਕਰਨ)।

### ਹਟਾਏ ਗਏ

- GitHub ਮਾਡਲਾਂ ਦੇ ਆਨਬੋਰਡਿੰਗ ਚਰਨ ਅਤੇ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲਾਂ ਨੂੰ ਸੈੱਟਅਪ ਡੌਕਸੋਂ ਹਟਾਇਆ ਗਿਆ (Azure OpenAI / Microsoft Foundry ਨਾਲ ਬਦਲਿਆ ਗਿਆ)।

### ਸੁਰੱਖਿਆ / ਪ੍ਰਾਇਵੇਸੀ (ਜਨਤਕ-ਸ਼ੇਅਰਿੰਗ ਸਫਾਈ)

- ਅਜਿਹੇ ਜੁਪਾਈਟਰ ਨੋਟਬੁੱਕ ਐਗਜ਼ੀਕਿਊਸ਼ਨ ਆউਟਪੁਟ ਸਾਫ ਕੀਤੇ ਜੋ ਅਸਲੀ **Azure membership ID**, resource-group / resource names ਅਤੇ Bing ਕਨੈਕਸ਼ਨ ID ਨਾਲ ਫੁਟੇ, ਨਾਲ ਹੀ ਡਿਵੈਲਪਰ ਦੇ **ਲੋਕਲ ਫਾਇਲ ਪਾਥ ਅਤੇ ਯੂਜ਼ਰਨਾਂਮ** ਵੀ ਸਨ:
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- ਪੱਕਾ ਕੀਤਾ ਕਿ ਕਿਸੇ ਵੀ API ਕੀਜ਼, ਟੋਕਨ, ਸਬਸਕ੍ਰਿਪਸ਼ਨ ID ਜਾਂ ਨਿੱਜੀ ਪਾਥ ਟਰੈਕ ਕੀਤੀ ਗਈ ਅੰਗ੍ਰੇਜ਼ੀ ਸਮੱਗਰੀ ਵਿੱਚ ਨਹੀਂ ਰਹੇ (ਬਾਕੀ ਬਚੇ `GITHUB_TOKEN` ਦਾ ਹਵਾਲਾ GitHub ਐਕਸ਼ਨ ਟੋਕਨ ਵਰਕਫਲੋਜ਼ ਅਤੇ GitHub MCP ਸਰਵਰ PAT ਸਬਕ 11 ਸੈੱਟਅਪ ਵਿੱਚ ਹੀ ਹੈ — ਦੋਹਾਂ GitHub ਮਾਡਲਾਂ ਨਾਲ ਸਬੰਧਤ ਨਹੀਂ)।

### ਨੋਟਸ ਅਤੇ ਜਾਣਿਆ ਸੀਮਾਵਾਂ

- **ਨਹੀਂ ਚਲਾਇਆ/ਕੰਪਾਇਲ ਕੀਤਾ।** ਇਹ ਸਿੱਖਿਅਕ ਨਮੂਨੇ ਹਨ ਜੋ API/ਨਾਮਕਰਨ ਸਹੀ ਕਰਨ ਲਈ ਅਪਡੇਟ ਕੀਤੇ ਗਏ ਹਨ; ਇਹ ਲਾਈਵ Azure ਸਰੋਤਾਂ ਖਿਲਾਫ ਨਹੀਂ ਚਲਾਏ ਗਏ ਅਤੇ .NET ਨਮੂਨੇ ਇਸ ਮਾਹੌਲ ਵਿਚ ਕੰਪਾਇਲ ਨਹੀਂ ਕੀਤੇ ਗਏ। ਆਪਣੀ Microsoft Foundry / Azure OpenAI ਡਿਪਲੋਇਮੈਂਟ ਨਾਲ ਤਸਦੀਕ ਕਰੋ।
- **ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ Responses API ਦਾ ਸਹਾਰਾ ਦੇਣਾ ਚਾਹੀਦਾ ਹੈ।** `gpt-4.1-mini`, `gpt-4.1`, ਜਾਂ `gpt-5.x` ਵਰਗੇ ਡਿਪਲੋਇਮੈਂਟ ਵਰਤੋ। ਪੁਰਾਣੇ ਮਾਡਲ Responses ਦੇ ਮੁੱਖ ਫੰਕਸ਼ਨਲਿਟੀ ਦਾ ਸਹਾਰਾ ਦਿੰਦੇ ਹਨ ਪਰ ਹਰ ਫੀਚਰ ਨਹੀਂ।
- **Agent-framework ਵਰਜਨ।** ਨਮੂਨੇ ਨਵੀਨਤਮ MAF (`>=1.10.0`) ਉੱਤੇ ਟਾਰਗਿਟ ਕੀਤੇ ਗਏ ਹਨ। ਮੁੱਖ ਏਜੰਟ ਬਣਾਉਣ ਵਾਲਾ ਕਾਲ `client.as_agent(...)` ਹੈ; APIs ਨੂੰ ਫਰੇਮਵਰਕ ਦੀ ਪ੍ਰਕਾਸ਼ਿਤ ਡੌਕਸ ਅਤੇ ਇੱਕ ਇੰਸਟਾਲ ਕੀਤੇ ਗਏ ਬਿਲਡ ਨਾਲ ਵੈਧਤਾ ਦਿੱਤੀ ਗਈ। ਜੇ ਤੁਸੀਂ ਵੱਖਰਾ ਵਰਜਨ ਨਿਸ਼ਚਿਤ ਕਰੋ, ਤਾਂ ਵਿਧੀ ਉਪਲਬਧਤਾ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ (`as_agent` ਵਿਰੁੱਧ `create_agent`)।
- **ਸਬਕ 08 ਵਰਕਫਲੋ ਨੋਟਬੁੱਕ 04** ਜਾਨਬੂਝ ਕੇ `AzureAIAgentClient` (ਜੋ `agent-framework-azure-ai` ਤੋਂ ਹੈ) ਨੂੰ ਰੱਖਦਾ ਹੈ ਕਿਉਂਕਿ ਇਹ Microsoft Foundry Agent Service ਹੋਸਟਡ ਟੂਲਜ਼ (Bing grounding, ਕੋਡ ਇੰਟਰਪ੍ਰੀਟਰ) ਵਰਤਦਾ ਹੈ; ਇਹ ਪਹਿਲਾਂ ਹੀ Responses-ਅਧਾਰਿਤ ਹੈ।
- **.NET ਡਿਫ਼ਾਲਟ ਡਿਪਲੋਇਮੈਂਟ।** ਦੋ ਸਬਕ 08 dotNET ਵਰਕਫਲੋ ਨਮੂਨੇ ਪਹਿਲਾਂ ਇੱਕ ਖਾਸ ਮਾਡਲ ਨੂੰ ਹਾਰਡ-ਕੋਡ ਕਰਦੇ ਸਨ; ਹੁਣ ਉਹ ਡਿਫ਼ਾਲਟ ਤੌਰ ਤੇ `AZURE_OPENAI_DEPLOYMENT` (`gpt-4.1-mini`) ਉਤੇ ਸੈੱਟ ਹਨ। ਜੇ ਕਿਸੇ ਨਮੂਨੇ ਨੂੰ ਮਲਟੀਮੋਡਲ/ਦ੍ਰਿਸ਼ ਪਰਿਵੇਸ਼ ਦੀ ਲੋੜ ਹੈ, ਤਾਂ `AZURE_OPENAI_DEPLOYMENT` ਨੂੰ ਉਚਿਤ ਮਾਡਲ ਸੈੱਟ ਕਰੋ।
- **Foundry Local** ਇੱਕ OpenAI-ਅਨੁਕੂਲ **Chat Completions** ਐਂਡਪੌਇੰਟ ਮੁਹੱਈਆ ਕਰਵਾਂਦਾ ਹੈ ਅਤੇ ਸਥਾਨਕ ਵਿਕਾਸ ਲਈ ਹੈ; Responses API ਦੀ ਪੂਰੀ ਫੀਚਰ ਸੈਟ ਲਈ Azure OpenAI / Microsoft Foundry ਵਰਤੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->