---
name: testing-course-samples
description: Use wen dem ask you to validate, test, smoke-test, or run di course notebook
  and code samples against live Microsoft Foundry / Azure OpenAI configuration. E
  cover environment setup (.env, az login, packages), di scripts/validate-notebooks.ps1
  runner, how to understand PASS/FAIL results, and which lessons need extra resources
  (Azure AI Search, GitHub MCP, Foundry Local, Playwright).
---
# Testing di Course Samples

Make sure say di lesson notebooks and code samples dey run well well for one live
Microsoft Foundry / Azure OpenAI setup. Di repo get one runner wey dey for
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) wey
dey run every Python notebook without display and e go show PASS/FAIL matrix.

## Wen you go use am
- "Make sure say all di notebooks / samples dey work for my Azure subscription."
- "Quick check di course after you upgrade packages or change models."
- "Which lessons still dey pass / fail for live?"

No use am for di AI Smoke Test GitHub Action (wey dey check *deployed*
hosted agents — see [`tests/README.md`](../../../tests/README.md)). Dis skill
dey run di notebooks for local machine.

## Wetin you go need (check first)
1. **Python 3.12+** with all di course dependencies: `python -m pip install -r requirements.txt`
   plus di executor: `python -m pip install nbconvert ipykernel`.
2. **`.env` for di root of di repo** (copy am from [`.env.example`](../../../../../.env.example)) with at least:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry project endpoint
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — one deployment wey no old (e.g. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) and `AZURE_OPENAI_DEPLOYMENT`
     for di lessons wey dey call Azure OpenAI directly (Lesson 06, 02-azure-openai, 14 handoff/human-loop).
3. **You don do `az login` finish** — di samples dey use `AzureCliCredential` (Entra ID, no need key).
4. Make sure say di model deployment dey:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## How to run the validation
```powershell
# All Python notebooks (no go include .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# One lesson, wit longer time wey e fit run per cell
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Only show wetin go run (no dey run anything)
pwsh scripts/validate-notebooks.ps1 -List

# Clear interpreter (if `python` no dey for PATH, like Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Di script dey write di runs copy, per-notebook logs, and `results.json` go
`$env:TEMP\aiab-nbval` and e go exit with di number of failures.

Temporary failures (shared-subscription HTTP 429 rate limits, one-time
`AzureCliCredential` token wahala, or timeout) e go try again automatically
(`-Retries`, default 2, plus `-RetryDelaySeconds` backoff, default 20). If
one model deployment dey always 429, check di subscription's GlobalStandard
TPM quota (`az cognitiveservices usage list -l <region>`) — even if you raise one
deployment capacity e no go help if di *subscription* quota don finish.

## How to understand di results
- `PASS` — di notebook run finish without any cell error.
- `FAIL` — di first `*Error` / `*Exception` line dey appear; open di right
  `log_*.txt` for di output folder to see di full problem.
- One single notebook failure dey controlled by `-Timeout` (per cell), so if one
  human-in-the-loop cell jam, e go show `StdinNotImplementedError` instead of hang.

## Lessons wey need extra things (dem go fail if no get dem)
| Lesson | Extra requirement |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, key) — get fallback way wey dey memory |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 memory (cognee) | `cognee` setup with one model provider |
| 15 browser-use | Playwright browsers installed (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + Qwen model wey you don download (on-device, no cloud) |
| `*-dotnet-*` notebooks | .NET Interactive kernel (no include by default; use `-IncludeDotnet`) |

## How to report back
Summarize am as PASS/FAIL table grouped by lesson. Separate real regressions
(code/config bugs wey need fix) from environment problems (missing Search/Foundry Local/PAT),
and talk about di failing `log_*.txt` for each real failure.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->