---
name: testing-course-samples
description: ប្រើនៅពេលត្រូវបានស្នើឱ្យផ្ទៀងផ្ទាត់ ពិសោធន៍ ពិសោធន៍ស្ពឹក ឬរត់សៀវភៅកំណត់ត្រានិងគំរូកូដនៃវគ្គសិក្សាពីលើការកំណត់
  Microsoft Foundry / Azure OpenAI ដែលកំពុងដំណើរការ។ គ្របដណ្ដប់ការតំឡើងបរិយាកាស (.env,
  az login, packages), កម្មវិធីរត់ scripts/validate-notebooks.ps1, ការបកស្រាយលទ្ធផល
  PASS/FAIL, និងមេរៀនណាដែលត្រូវការធនធានបន្ថែម (Azure AI Search, GitHub MCP, Foundry
  Local, Playwright)।
---
# ការធ្វើតេស្តគំរូវគ្គសិក្សា

ផ្ទៀងផ្ទាត់ថា សៀវភៅកំណត់ត្រាបង្រៀននិងគំរូកូដរត់បានលើការតំឡើង Microsoft Foundry / Azure OpenAI ត៌មានជាក់លាក់មួយ។ ឃ្លាំងកូដផ្ដល់ឧបករណ៌ដំណើរការនៅ
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) ដែល
អនុវត្តសៀវភៅកំណត់ត្រា Python ទាំងអស់ដោយគ្មានការបង្ហាញ UI និងបោះពុម្ពមាត្រលេខ PASS/FAIL។


- "ផ្ទៀងផ្ទាត់សៀវភៅកំណត់ត្រា / គំរូទាំងអស់នៅលើការជាវ Azure របស់ខ្ញុំ។"
- "ធ្វើតេស្តសម្រាប់ការបើកវគ្គបណ្តុះបណ្តាល បន្ទាប់ពីធ្វើបច្ចុប្បន្នភាពកញ្ចប់ឬប្ដូរម៉ូដែល។"
- "មេរៀនណាដែលនៅតែឆ្លងតេស្ត / បរាជ័យនៅលើប្រព័ន្ធតូច?"


កុំប្រើនេះសម្រាប់សកម្មភាព AI Smoke Test GitHub (ដែលធ្វើការត្រួតពិនិត្យ *បានបញ្ចូន*
អ្នកតំណាងដែលភ្ជាប់រួច — មើល [`tests/README.md`](../../../tests/README.md))។ ជំនាញនេះ
ប្រតិបត្ដិការវិចសៀវបណ្ណនៅក្នុងកន្លែង។

## លក្ខខណ្ឌមុន (ត្រួតពិនិត្យមុន)
1. **Python 3.12+** ជាមួយ deps តាមវគ្គ៖ `python -m pip install -r requirements.txt`
   បូកបន្ថែមអ្នកប្រតិបត្ដិការ៖ `python -m pip install nbconvert ipykernel`។
2. **`.env` នៅឬបាតដើម repo** (ចម្លងពី [`.env.example`](../../../../../.env.example)) ជាមួយយ៉ាងហោចណាស់៖
   - `AZURE_AI_PROJECT_ENDPOINT` — ចំណុចបញ្ចប់ផែនការរបស់ Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — ការដាក់បង្ហាញមិនត្រូវបានចាកចេញ (ឧ. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) និង `AZURE_OPENAI_DEPLOYMENT`
     សម្រាប់មេរៀនដែលហៅ Azure OpenAI តាមរយៈផ្ទាល់ (មេរៀន 06, 02-azure-openai, 14 handoff/human-loop)។
3. **`az login`** បានបញ្ចប់ — គំរូត្រូវបាន Authenticate ជាមួយ `AzureCliCredential` (Entra ID, keyless)។
4. ត្រួតពិនិត្យមើលការដាក់បង្ហាញម៉ូដែលមានអត់៖
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`។

## ការប្រតិបត្ដិការត្រួតពិនិត្យ
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
ស្គ្រីបនិពន្ធចម្លងបានអនុវត្ត, កំណត់ត្រាបានភាគNotebook, និង `results.json` ទៅ
`$env:TEMP\aiab-nbval` ហើយចាកចេញជាមួយចំនួនជំហានបរាជ័យ។

ជំហានបរាជ័យបណ្តោះអាសន្ន (កំណត់អត្រា HTTP 429 អ្នកជាវចែករំលែក, ការខូច token `AzureCliCredential` តិចតួច, ឬការបញ្ចប់ពេលវេលា) ត្រូវបានព្យាយាមឡើងវិញដោយស្វ័យប្រវត្តិ
(`-Retries`, លំនាំដើម 2, ជាមួយការផ្តាច់ `-RetryDelaySeconds`, លំនាំដើម 20)។ ប្រសិនបើ
ការដាក់ម៉ូដែលត្រូវបាន 429 ជាប្រចាំ, សូមពិនិត្យ quota TPM GlobalStandard
នៃការជាវ (`az cognitiveservices usage list -l <region>`) — ការលើកសមត្ថភាពនៃការដាក់បង្ហាញតែមួយមិនជួយប្រសិនបើ quota *ជាវ* ត្រូវបានប្រើប្រាស់។



- `PASS` — វិចសៀវបណ្ណបានរត់លង្កតបញ្ចប់ដោយគ្មានកំហុសគ្រាប់កោសិកា។
- `FAIL` — បន្ទាត់ `*Error` / `*Exception` ជួរដំបូងត្រូវបានបង្ហាញ; បើក
  `log_*.txt` ត្រូវគ្នាក្នុងកន្លែងលទ្ធផលសម្រាប់ការត្រួតពិនិត្យពេញលេញ។
- ការបរាជ័យតែមួយនៃវិចសៀវបណ្ណត្រូវបានដាក់កំណត់ដោយ `-Timeout` (ក្នុងមួយគ្រាប់កោសិកា), ដូច្នេះគ្រាប់កោសិកាដែលមានមនុស្សនៅក្នុងលំនាំមិនសកម្មបង្ហាញជា `StdinNotImplementedError` មិនមែននៅក្នុងស្ថានភាពរង់ចាំទេ។

## មេរៀនដែលត្រូវការពាណិជ្ជកម្មបន្ថែម (រំពឹងថាបរាជ័យដោយគ្មានវា)

|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, key) — មានផ្លូវ fallback ក្នុងចំណោមនាទីមួយ |
| 11 MCP / GitHub | ម៉ាស៊ីនបម្រើ GitHub MCP + PAT |
| 13 memory (cognee) | `cognee` ត្រូវបានកំណត់ជាមួយអ្នកផ្គត់ផ្គង់ម៉ូដែល |
| 15 browser-use | កម្មវិធីរុករក Playwright ត្រូវបានដំឡើង (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + ម៉ូដែល Qwen ដែលបានទាញយក (នៅលើឧបករណ៍, គ្មានវេប) |
| `*-dotnet-*` notebooks | កឺរណែល .NET Interactive (មិនបានរួមបញ្ចូលដោយលំនាំដើម; ប្រើ `-IncludeDotnet`) |

## ការរាយការណ៍ត្រឡប់មកវិញ

## រាយការណ៍ត្រឡប់វិញ
សង្ខេបជាតារាង PASS/FAIL ក្រុមតាមមេរៀន។ បំបែកការកើនឡើងពិតប្រាកដ
(កំហុសកូដ/កំណត់រចនាសម្ព័ន្ធត្រូវបានជួសជុល) ពីចន្លោះបរិស្ថាន (គណនី Search/Foundry Local/PAT ខ្វះ),
ហើយយោងនៅ `log_*.txt` ដែលបរាជ័យសម្រាប់ជំហរបរាជ័យពិតប្រាកដនីមួយៗ។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->