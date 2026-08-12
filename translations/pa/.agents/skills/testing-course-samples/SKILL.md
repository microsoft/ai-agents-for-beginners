---
name: testing-course-samples
---
# ਕੋਰਸ ਸੈਂਪਲਾਂ ਦੀ ਜਾਂਚ ਕਰਨਾ

ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ ਲੈਸਨ ਨੋਟਬੁੱਕ ਅਤੇ ਕੋਡ ਸੈਂਪਲਜ਼ ਇੱਕ ਲਾਈਵ
Microsoft Foundry / Azure OpenAI ਸੈਟਅੱਪ ਵਿਰੁੱਧ ਚੱਲ ਰਹੇ ਹਨ। ਰਿਪੋ ਵਿੱਚ ਇੱਕ ਰਨਰ ਸ਼ਾਮਿਲ ਹੈ
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) ਜੋ
ਸਾਰੇ ਪਾਇਥਨ ਨੋਟਬੁੱਕ ਨੂੰ ਬਿਨਾਂ ਵਿਖਾਵਟ ਦੇ ਚਲਾਉਂਦਾ ਹੈ ਅਤੇ ਇੱਕ PASS/FAIL ਮੈਟ੍ਰਿਕਸ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ।

## ਕਦੋਂ ਵਰਤਣਾ ਹੈ
- "ਮੇਰੇ Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਵਿਰੁੱਧ ਸਾਰੇ ਨੋਟਬੁੱਕ / ਸੈਂਪਲਜ਼ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।"
- "ਪੈਕੇਜ ਰੁੱਪਾਂਤਰਾਂ ਜਾਂ ਮਾਡਲ ਬਦਲਣ ਤੋਂ ਬਾਅਦ ਕੋਰਸ ਦਾ ਸਟੈਮ ਟੈਸਟ ਕਰੋ।"
- "ਕਿਹੜੇ ਲੈਸਨ ਜੀਵੰਤ ਤੌਰ ਤੇ ਅਜੇ ਵੀ ਪਾਸ / ਫੇਲ ਹੋ ਰਹੇ ਹਨ?"

ਇਸਨੂੰ AI Smoke Test GitHub Action (ਜੋ ਤैनਾਤ ਕੀਤੇ
ਹੋਏ ਏਜੰਟਾਂ ਦੀ ਪੁਸ਼ਟੀ ਕਰਦਾ ਹੈ — ਵੇਖੋ [`tests/README.md`](../../../tests/README.md)) ਲਈ ਵਰਤੋਂ ਨਾ ਕਰੋ। ਇਹ ਸਕਿਲ
ਨੋਟਬੁੱਕਸ ਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਚਲਾਉਂਦਾ ਹੈ।

## ਪੂਰਵ-ਸ਼ਰਤਾਂ (ਪਹਿਲਾਂ ਚੈੱਕ ਕਰੋ)
1. **Python 3.12+** ਕੋਰਸ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਨਾਲ: `python -m pip install -r requirements.txt`
   ਅਤੇ ਐਗਜ਼ੀਕਿਊਟਰ: `python -m pip install nbconvert ipykernel`।
2. **ਰਿਪੋ ਰੂਟ ਤੇ `.env`** (ਨਕਲ ਕਰੋ [`.env.example`](../../../../../.env.example) ਤੋਂ) ਘੱਟੋ-ਘੱਟ:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry ਪ੍ਰੋਜੈਕਟ ਐਂਡਪੌਇੰਟ
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — ਇੱਕ ਗੈਰ-ਡਿਪ੍ਰੀਕੇਟਿਡ ਡਿਪਲੋਇਮੈਂਟ (ਜਿਵੇਂ `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) ਅਤੇ `AZURE_OPENAI_DEPLOYMENT`
     ਉਹਨਾਂ ਲੈਸਨਾਂ ਲਈ ਜੋ ਸਿੱਧਾ Azure OpenAI ਨੂੰ ਕਾਲ ਕਰਦੇ ਹਨ (ਲੈਸਨ 06, 02-azure-openai, 14 handoff/human-loop)।
3. **`az login`** ਮੁਕੰਮਲ ਕੀਤਾ ਹੋਇਆ — ਸੈਂਪਲਜ਼ `AzureCliCredential` ਨਾਲ ਪ੍ਰਮਾਣਿਤ ਹੁੰਦੇ ਹਨ (Entra ID, ਕੀ-ਬਿਨਾਂ)।
4. ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਮੌਜੂਦ ਹੈ ਜਾਂ ਨਹੀਂ ਇਹ ਪੁਸ਼ਟੀ ਕਰੋ:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`।

## ਜਾਂਚ ਚਲਾਉਣਾ
```powershell
# ਸਾਰੇ ਪਾਇਥਨ ਨੋਟਬੁੱਕ (।NET, .venv, ਸਾਈਟ-ਪੈਕੇਜ, ਅਨੁਵਾਦ, ਸкил assets ਨੂੰ ਛੱਡ ਕੇ)
pwsh scripts/validate-notebooks.ps1

# ਇੱਕ ਇਕੱਲਾ ਪਾਠ, ਪ੍ਰਤੀ-ਸੈੱਲ ਲੰਮੀ ਟਾਈਮਆਉਟ ਦੇ ਨਾਲ
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# ਸਿਰਫ਼ ਦਰਸਾਓ ਕਿ ਕੀ ਚਲੇਗਾ (ਕੋਈ ਚਲਾਉਣਾ ਨਹੀਂ)
pwsh scripts/validate-notebooks.ps1 -List

# ਖ਼ਾਸ ਤੌਰ ਤੇ ਵਿਆਖਿਆਕਾਰ (ਜੇ `python` PATH 'ਤੇ ਨਹੀਂ ਹੈ, ਜਿਵੇਂ ਕਿ Windows Store ਦਾ ਜੁਗ੍ਹਾ)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
 ਸਕ੍ਰਿਪਟ ਚਲਾਵਾਂ ਕਾਪੀਆਂ, ਪ੍ਰਤੀ-ਨੋਟਬੁੱਕ ਲੌਗਾਂ, ਅਤੇ `results.json` ਨੂੰ
`$env:TEMP\aiab-nbval` ਵਿੱਚ ਲਿਖਦਾ ਹੈ ਅਤੇ ਅਸਫਲਤਾਵਾਂ ਦੀ ਗਿਣਤੀ ਨਾਲ ਬਾਹਰ ਨਿਕਲਦਾ ਹੈ।

ਅਸਥਾਈ ਅਸਫਲਤਾਵਾਂ (ਸਾਂਝੇ ਸਬਸਕ੍ਰਿਪਸ਼ਨ HTTP 429 ਦਰ ਸੀਮਾਵਾਂ, ਕਦੇ-ਕਦੇ
`AzureCliCredential` ਟੋਕਨ ਵਿੱਚ ਰੁਕਾਵਟ, ਜਾਂ ਸਮਾਂ ਸਮਾਪਤੀ) ਆਪਣੇ ਆਪ ਮੁੜ ਕੋਸ਼ਿਸ਼ ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ
(`-Retries`, ਡੀਫਾਲਟ 2, ਨਾਲ `-RetryDelaySeconds` ਬੈਕਆਫ, ਡੀਫਾਲਟ 20)। ਜੇਕਰ
ਇੱਕ ਮਾਡਲ ਡਿਪਲੋਇਮੈਂਟ ਲਗਾਤਾਰ 429 ਕਰ ਰਿਹਾ ਹੈ, ਤਾਂ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਦੇ GlobalStandard
TPM ਕੋਟਾ ਨੂੰ ਚੈੱਕ ਕਰੋ (`az cognitiveservices usage list -l <region>`) — ਇੱਕ ਸਿਰਫ
ਡਿਪਲੋਇਮੈਂਟ ਦੀ ਸਮਰੱਥਾ ਵਧਾਉਣਾ ਮਦਦਗਾਰ ਨਹੀਂ ਜਦੋਂ *ਸਬਸਕ੍ਰਿਪਸ਼ਨ* ਕੋਟਾ ਖਤਮ ਹੋ ਜਾਵੇ।

## ਨਤੀਜੇ ਸਮਝਣਾ
- `PASS` — ਨੋਟਬੁੱਕ ਬਿਨਾਂ ਕਿਸੇ ਸੈੱਲ ਦੀ ਗਲਤੀ ਦੇ ਕਮਲ ਤੱਕ ਚੱਲਿਆ।
- `FAIL` — ਪਹਿਲੀ `*Error` / `*Exception` ਲਾਈਨ ਦਿਖਾਈ ਜਾਂਦੀ ਹੈ; ਪੂਰੇ ਟ੍ਰੇਸਬੈਕ ਲਈ
  ਆਉਟਪੁੱਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਮਿਲਦੇ ਜੁਲਦੇ `log_*.txt` ਨੂੰ ਖੋਲ੍ਹੋ।
- ਇੱਕ ਹੀ ਨੋਟਬੁੱਕ ਦੀ ਅਸਫਲਤਾ `-Timeout` (ਹਰੇਕ ਸੈੱਲ) ਨਾਲ ਸੀਮਿਤ ਹੁੰਦੀ ਹੈ, ਇਸ ਲਈ ਇੱਕ ਫਸਿਆ ਹੋਇਆ
  human-in-the-loop ਸੈੱਲ `StdinNotImplementedError` ਵਜੋਂ ਉਤਪੰਨ ਹੁੰਦਾ ਹੈ ਨਾ ਕਿ ਫਸਦਾ ਹੈ।

## ਉਹ ਲੈਸਨ ਜਿਨ੍ਹਾਂ ਨੂੰ ਵੱਧ ਸਰੋਤਾਂ ਦੀ ਲੋੜ ਹੈ (ਬਿਨਾਂ ਉਹਨਾਂ ਦੇ ਫੇਲ ਹੋਣ ਦੀ ਸੰਭਾਵਨਾ)
| ਲੈਸਨ | ਵਾਧੂ ਜ਼ਰੂਰਤ |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, ਕੁੰਜੀ) — ਇੱਕ ਮੈਮੋਰੀ ਬੈਕਅੱਪ ਪਾਥ ਹੈ |
| 11 MCP / GitHub | GitHub MCP ਸਰਵਰ + PAT |
| 13 memory (cognee) | `cognee` ਇੱਕ ਮਾਡਲ ਪ੍ਰਦਾਤਾ ਨਾਲ ਸੰਰਚਿਤ |
| 15 browser-use | Playwright ਬਰਾਊਜ਼ਰ ਇੰਸਟਾਲ ਕੀਤੇ (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry ਲੋਕਲ ਰਨਟਾਈਮ + ਡਾਊਨਲੋਡ ਕੀਤਾ ਹੋਇਆ Qwen ਮਾਡਲ (ਡਿਵਾਈਸ ਉਤੇ, ਕੋਈ ਕਲਾਉਡ ਨਹੀਂ) |
| `*-dotnet-*` ਨੋਟਬੁੱਕ | .NET Interactive ਕੇਰਨਲ (ਡਿਫਾਲਟ ਤੌਰ 'ਤੇ ਬਾਹਰ; `-IncludeDotnet` ਵਰਤਣ) |

## ਵਾਪਸੀ ਰਿਪੋਰਟਿੰਗ
ਇੱਕ PASS/FAIL ਟੇਬਲ ਵਜੋਂ ਸਾਰ ਸੰਖੇਪ ਜੋ ਲੈਸਨ ਅਨੁਸਾਰ ਗਰੁੱਪ ਕੀਤਾ ਹੋਇਆ ਹੈ। ਅਸਲੀ ਰਿਗ੍ਰੈਸ਼ਨ
(ਕੋਡ/ਕੰਫਿਗ ਬੱਗ ਸਮਝਦਾਰ) ਨੂੰ ਮਾਹੌਲ ਦੇ ਫਰਕਾਂ (ਗੁੰਮਸ਼ੁਦਾ Search/Foundry Local/PAT)
ਤੋਂ ਵੱਖਰੇ ਕਰੋ, ਅਤੇ ਹਰ ਅਸਲੀ ਅਸਫਲਤਾ ਲਈ ਫੇਲਿੰਗ `log_*.txt` ਨੂੰ ਹਵਾਲਾ ਦਿਓ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->