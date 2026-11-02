---
name: testing-course-samples
---
# കോഴ്സ് സാമ്പിൾസിനുള്ള ടെസ്റ്റിങ്

ഈ പാഠപുസ്തക നോട്ട് ബുക്കുകളും കോഡ് സാമ്പിളുകളും ഒരു സജീവമായ
Microsoft Foundry / Azure OpenAI സജ്ജീകരണത്തിൽ പ്രവർത്തിക്കുന്നതായി സാധുതാപെടുത്തുക. റഫ്പോയിൽ
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) എന്ന ഒരു റണ്ണർയുണ്ട്,
ഇത് ഓരോ Python നോട്ട് ബുക്കും ഹെഡ്‌ലസായി ആ اجراച ചെയ്യുകയും PASS/FAIL മെട്രിക്‌സും പ്രിന്റുചെയ്യുകയും ചെയ്യുന്നു.

## ഉപയോഗിക്കേണ്ട സമയങ്ങൾ
- "എന്റെ Azure സബ്സ്ക്രിപ്ഷനിൽ എല്ലാ നോട്ട് ബുക്കുകളും / സാമ്പിളുകളും സാധുതാപെടുത്തുക."
- "പാക്കേജുകൾ അപ്ഗ്രേഡ് ചെയ്‌തശേഷം അല്ലെങ്കിൽ മോഡലുകൾ മാറ്റിയശേഷം കോഴ്സ് സ്മോക്ക്-ടെസ്റ്റ് നടത്തുക."
- "എന്തെല്ലാം പാഠങ്ങൾ ഇപ്പോഴും ലൈവിൽ പാസ്സോ ഫെയ്ലോ ആണ്?"

ഈ അക്കൗണ്ടിനുള്ള AI Smoke Test GitHub Action (വിതരണത്തിലുള്ള
ഹോസ്റ്റ് ചെയ്ത ഏജന്റുകൾ സാധുതാപെടുത്തുന്നു — കാണുക [`tests/README.md`](../../../tests/README.md)) ഉപയോഗിക്കാൻ **പോയി** വേണ്ട.
ഇത് നോട്ട് ബുക്കുകൾ ലോകലായി പ്രവർത്തിപ്പിക്കുന്നു.

## മുൻ‌അവശ്യങ്ങൾ (ആദ്യമേ പരിശോധിക്കുക)
1. **Python 3.12+** കോഴ്സ് ഡിപ്പെൻഡൻസികളോടെ: `python -m pip install -r requirements.txt`
   കൂടാതെ എക്സിക്യൂട്ടർ: `python -m pip install nbconvert ipykernel`.
2. **`.env` റപോസിറ്ററി റൂട്ടിൽ** ([Copy from `.env.example`](../../../../../.env.example)) കുറഞ്ഞത് ഇതുകാര്യങ്ങളോടുകൂടി:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry പ്രോജക്ട് എൻഡ്‌പോയിന്റ്
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — പഴകാത്ത ഒരു ഡിപ്ലോയ്മെന്റ് (ഉദാഹരണം: `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) കൂടാതെ `AZURE_OPENAI_DEPLOYMENT`
     Azure OpenAI നേരിട്ട് വിളിക്കുന്ന പാഠങ്ങൾക്ക് (Lesson 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** പൂർത്തിയായി — സാമ്പിളുകൾ `AzureCliCredential` ഉപയോഗിച്ച് ഓതൻറിക്കറ്റ് ചെയ്യുന്നു (Entra ID, കീലെസ്).
4. മോഡൽ ഡിപ്ലോയ്മെന്റ് നിലവിലുണ്ടെന്ന് സ്ഥിരീകരിക്കുക:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## സാധുതാപെടുത്തൽ നടത്തുന്നത്
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
സ്ക്രിപ്റ്റ് നടപ്പിലാക്കിയ പകർപ്പുകൾ, ഓരോ നോട്ട് ബുക്കിനും ലോഗുകൾ, `results.json`
`$env:TEMP\aiab-nbval` ലേക്ക് എഴുതുകയും പരാജയങ്ങളുടെ എണ്ണം സഹിതം.EXIT ചെയ്യും.

താൽക്കാലിക പരാജയങ്ങൾ (പങ്കിടുന്ന സബ്സ്ക്രിപ്ഷൻ HTTP 429 നിരക്കുകാലപരിധികൾ, ചിലപ്പോൾ 
`AzureCliCredential` ടോക്കൺ ഹിക്കപ്പുകൾ, അല്ലെങ്കിൽ ടൈംഔട്ട്) സ്വയം തിരിച്ചടിക്കപ്പെടുന്നു
(`-Retries`, ഡീഫോള്റ്റ് 2, `-RetryDelaySeconds` ബാക്ക്ഓഫ്, ഡീഫോള്റ്റ് 20). ഒരു
മോഡൽ ഡിപ്ലോയ്മെന്റ് സ്ഥിരമായി 429 ഉണ്ടെങ്കിൽ, സബ്സ്ക്രിപ്ഷന്റെ GlobalStandard
TPM ക്വോട്ട പരിശോധിക്കുക (`az cognitiveservices usage list -l <region>`) — ഒരു പ്രത്യേക
ഡിപ്ലോയ്മെന്റിന്റെ ശേഷി വർദ്ധിപ്പിക്കുന്നത് സബ്സ്ക്രിപ്ഷൻ ക്വോട്ട തീർത്ത് കഴിഞ്ഞാൽ സഹായിക്കില്ല.

## ഫലങ്ങൾ വ്യാഖ്യാനിക്കൽ
- `PASS` — നോട്ട് ബുക്ക് എല്ലാം അവസാനിപ്പിച്ചു ഒരു സെൽ error കൂടാതെ റൺ ചെയ്തു.
- `FAIL` — ആദ്യത്തെ `*Error` / `*Exception` ലൈനുകൾ കാണിക്കുന്നു; പൊരുത്തപ്പെടുന്ന
  `log_*.txt` ഔട്ട്‌പുട്ട് ഡയറക്ടറിയിൽ തുറന്നാൽ മുഴുവൻ ട്രേസ്ബാക്ക് കാണാം.
- ഒറ്റ നോട്ട് ബുക്കിന്റെ പരാജയം `-Timeout` (ഓരോ സെൽ)കൊണ്ടു പരിധിയിലാണെന്നും, അതുകൊണ്ട്
  ഹെം-ഇൻ-ദി-ലൂപ്പ് സെൽ കുടുങ്ങിയാൽ അത് `StdinNotImplementedError` ആയി പ്രത്യക്ഷപ്പെടും, കുടുങ്ങാത്ത നിലയിൽ അല്ല.

## കൂടുതൽ സ്രോതസ്സുകൾ ആവശ്യമായ പാഠങ്ങൾ (അവയുടെ അപ്രാപ്തിയോടെ പരാജയവും പ്രതീക്ഷിക്കാം)
| പാഠം | അധിക ആവശ്യകത |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, കീ) — മുടക്കില്ലാത്ത ഫലബാക്ക് പാത്ത് ഉള്ളത് |
| 11 MCP / GitHub | GitHub MCP സെർവർ + PAT |
| 13 memory (cognee) | `cognee` മോഡൽ പ്രൊവൈഡറിനോട് കൺഫിഗർ ചെയ്തത് |
| 15 browser-use | Playwright ബ്രൗസറുകൾ ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ട് (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + ഡൗൺലോഡ് ചെയ്ത Qwen മോഡൽ (ഓൺ-ഡിവൈസ്, ക്ലൗഡ് ഇല്ല) |
| `*-dotnet-*` നോട്ട്ബുക്കുകൾ | .NET Interactive കർണൽ (ഡീഫാൾട്ട് exclude ചെയ്തിട്ടുണ്ട്; ഉപയോഗിക്കുക `-IncludeDotnet`) |

## ഫീഡ്‌ബാക്ക് നൽകൽ
പാഠങ്ങളുടെ അടിസ്ഥാനത്തിൽ ഗ്രൂപ്പുചെയ്ത് PASS/FAIL പട്ടികയായി സംഗ്രഹിക്കുക. യഥാർത്ഥ
പുനരാക്രമണങ്ങൾ (കോഡ്/കൺഫിഗ് പിശകുകൾ പരിഹരിക്കേണ്ടത്) പരിസ്ഥിതി കുറവുകളിലും (Search/Foundry Local/PAT
നഷ്ടപ്പെട്ടത്) വേർതിരിക്കുക, ഓരോ യഥാർത്ഥ പരാജയത്തിനും പരാജയപ്പെട്ട `log_*.txt` സൂചിപ്പിക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->