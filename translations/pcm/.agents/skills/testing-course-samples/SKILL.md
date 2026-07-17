---
name: testing-course-samples
description: Use wen dem ask to check, test, do smoke-test, or run di course notebook
  and code samples against live Microsoft Foundry / Azure OpenAI setup. E cover how
  to set environment (.env, az login, packages), di scripts/validate-notebooks.ps1
  runner, how to understand PASS/FAIL results, and which lessons ~need extra resources
  (Azure AI Search, GitHub MCP, Foundry Local, Playwright).
---
# Testing di Course Samples

Check sey di lesson notebooks and code samples dey run against live
Microsoft Foundry / Azure OpenAI setup. Di repo get runner for
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) wey
dey run every Python notebook headlessly and dey show PASS/FAIL matrix.

## When to use
- "Make sure all di notebooks / samples dey work well wit my Azure subscription."
- "Quick test di course after upgrading packages or changing models."
- "Which lessons still dey pass / fail live?"

No **use** dis one for di AI Smoke Test GitHub Action (wey dey validate *deployed*
hosted agents — see [`tests/README.md`](../../../tests/README.md)). Dis skill
dey run di notebooks locally.

## Wetin you need before you start (check first)
1. **Python 3.12+** wit course deps: `python -m pip install -r requirements.txt`
   plus di executor: `python -m pip install nbconvert ipykernel`.
2. **`.env` for di repo root** (copy from [`.env.example`](../../../../../.env.example)) wey get at least:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry project endpoint
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — deployment wey no dey deprecated (e.g. `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) and `AZURE_OPENAI_DEPLOYMENT`
     for lessons wey dey call Azure OpenAI directly (Lesson 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** don finish — samples dey authenticate wit `AzureCliCredential` (Entra ID, keyless).
4. Check sey di model deployment dey:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## How to run di validation
```powershell
# All Python notebooks (no include .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# One lesson, with longer time wey e go take for each cell
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Just show wetin go run (no run am)
pwsh scripts/validate-notebooks.ps1 -List

# Clear interpreter (if `python` no dey PATH, e.g. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Di script go write executed copies, per-notebook logs, and `results.json` go
`$env:TEMP\aiab-nbval` and e go comot wit di number of failures.

## How to understand results
- `PASS` — di notebook run finish well without any cell error.
- `FAIL` — di first `*Error` / `*Exception` line go show; open di matching
  `log_*.txt` for di output folder to see full traceback.
- If one notebook fail, e go get `-Timeout` (for every cell), so hung
  human-in-the-loop cell go show as `StdinNotImplementedError` instead of hanging.

## Lessons wey need extra resources (dem go fail if dem no get am)
| Lesson | Extra requirement |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, key) — get in-memory fallback path |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 memory (cognee) | `cognee` set up wit model provider |
| 15 browser-use | Playwright browsers don install (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + Qwen model wey don download (on-device, no cloud) |
| `*-dotnet-*` notebooks | .NET Interactive kernel (no dey by default; use `-IncludeDotnet`) |

## How to report back
Summarize as PASS/FAIL table grouped by lesson. Separate real regressions
(code/config bugs wey need fix) from environment gaps (missing Search/Foundry Local/PAT),
and mention di failing `log_*.txt` for each real failure.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->