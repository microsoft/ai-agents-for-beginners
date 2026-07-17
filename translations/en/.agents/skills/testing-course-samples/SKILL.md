---
name: testing-course-samples
description: Use when asked to validate, test, smoke-test, or run the course's notebook
  and code samples against a live Microsoft Foundry / Azure OpenAI configuration.
  Covers environment setup (.env, az login, packages), the scripts/validate-notebooks.ps1
  runner, interpreting PASS/FAIL results, and which lessons need extra resources (Azure
  AI Search, GitHub MCP, Foundry Local, Playwright).
---
# Testing the Course Samples

Validate that the lesson notebooks and code samples run against a live
Microsoft Foundry / Azure OpenAI setup. The repo ships a runner at
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) that
executes every Python notebook headlessly and prints a PASS/FAIL matrix.

## When to use
- "Validate all the notebooks / samples against my Azure subscription."
- "Smoke-test the course after upgrading packages or changing models."
- "Which lessons still pass / fail live?"

Do **not** use this for the AI Smoke Test GitHub Action (that validates *deployed*
hosted agents — see [`tests/README.md`](../../../tests/README.md)). This skill
runs the notebooks locally.

## Prerequisites (check first)
1. **Python 3.12+** with course deps: `python -m pip install -r requirements.txt`
   plus the executor: `python -m pip install nbconvert ipykernel`.
2. **`.env` at the repo root** (copy from [`.env.example`](../../../../../.env.example)) with at least:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry project endpoint
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — a non-deprecated deployment (e.g. `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) and `AZURE_OPENAI_DEPLOYMENT`
     for lessons that call Azure OpenAI directly (Lesson 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** completed — samples authenticate with `AzureCliCredential` (Entra ID, keyless).
4. Verify the model deployment exists:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Running the validation
```powershell
# All Python notebooks (skips .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# A single lesson, with a longer per-cell timeout
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Just list what would run (no execution)
pwsh scripts/validate-notebooks.ps1 -List

# Explicit interpreter (if `python` is not on PATH, e.g. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
The script writes executed copies, per-notebook logs, and `results.json` to
`$env:TEMP\aiab-nbval` and exits with the number of failures.

## Interpreting results
- `PASS` — the notebook ran end-to-end with no cell error.
- `FAIL` — the first `*Error` / `*Exception` line is shown; open the matching
  `log_*.txt` in the output dir for the full traceback.
- A single notebook's failure is bounded by `-Timeout` (per cell), so a hung
  human-in-the-loop cell surfaces as `StdinNotImplementedError` rather than hanging.

## Lessons that need extra resources (expected to fail without them)
| Lesson | Extra requirement |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, key) — has an in-memory fallback path |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 memory (cognee) | `cognee` configured with a model provider |
| 15 browser-use | Playwright browsers installed (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + a downloaded Qwen model (on-device, no cloud) |
| `*-dotnet-*` notebooks | .NET Interactive kernel (excluded by default; use `-IncludeDotnet`) |

## Reporting back
Summarise as a PASS/FAIL table grouped by lesson. Separate genuine regressions
(code/config bugs to fix) from environment gaps (missing Search/Foundry Local/PAT),
and cite the failing `log_*.txt` for each real failure.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
This document has been translated using AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->