---
name: testing-course-samples
---
# Тестирање узорака курса

Потврдите да ли бележнице са лекцијама и узорци кода раде са активном
Microsoft Foundry / Azure OpenAI конфигурацијом. Репозиторијум обухвата извршни фајл у
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) који
извршава сваку Python бележницу у позадини и приказује PASS/FAIL матрицу.

## Када користити
- "Проверите све бележнице / узорке у складу са мојом Azure претплатом."
- "Брзи тест курса након ажурирања пакета или промене модела."
- "Које лекције и даље пролазе / не пролазе уживо?"

Не користите ово за AI Smoke Test GitHub Action (који потврђује *распоређене*
хостоване агенте — видети [`tests/README.md`](../../../tests/README.md)). Ова вештина
покреће бележнице локално.

## Претпоставке (прво проверити)
1. **Python 3.12+** са зависностима курса: `python -m pip install -r requirements.txt`
   плус извршилац: `python -m pip install nbconvert ipykernel`.
2. **`.env` у корену репозиторијума** (копирати из [`.env.example`](../../../../../.env.example)) са најмање:
   - `AZURE_AI_PROJECT_ENDPOINT` — крајња тачка Foundry пројекта
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — незастарела расподела (нпр. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) и `AZURE_OPENAI_DEPLOYMENT`
     за лекције које директно позивају Azure OpenAI (Лекција 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** извршен — узорци се аутентификују преко `AzureCliCredential` (Entra ID, без кључа).
4. Потврдите да расподела модела постоји:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Покретање валидације
```powershell
# Сви Питон бележници (прескаче .NET, .venv, site-packages, преводе, скилл ресурсе)
pwsh scripts/validate-notebooks.ps1

# Једна лекција, са дужим временским ограничењем по ћелији
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Само наведите шта би се покренуло (без извршавања)
pwsh scripts/validate-notebooks.ps1 -List

# Јасан интерпретер (ако `python` није у PATH, нпр. Windows Store алијас)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Скрипта уписује извршене копије, логове по бележници и `results.json` у
`$env:TEMP\aiab-nbval` и излази са бројем неуспеха.

Привремени неуспеси (ограничења HTTP 429 за дељену претплату, повремени
`AzureCliCredential` прекид токена или тајмаут) се аутоматски поново покушавају
(`-Retries`, подразумевано 2, са `-RetryDelaySeconds` застојем, подразумевано 20). Ако се
расподела модела често враћа 429 грешке, проверите GlobalStandard
TPM квоту претплате (`az cognitiveservices usage list -l <region>`) — повећање капацитета једне
расподеле не помаже када је *квота претплате* исцрпљена.

## Тумачење резултата
- `PASS` — бележница је успешно извршена од почетка до краја без грешака у ћелијама.
- `FAIL` — показује се прва линија `*Error` / `*Exception`; отвори одговарајући
  `log_*.txt` у излазном директоријуму за пун traceback.
- Један неуспех бележнице је ограничен са `-Timeout` (по ћелији), тако да ћелија са
  интеракцијом човека је означена као `StdinNotImplementedError` уместо да се заглави.

## Лекције којима су потребни додатни ресурси (оријентовано на неуспех без њих)
| Лекција | Додатни захтев |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, кључ) — има алтернативни пут у меморији |
| 11 MCP / GitHub | GitHub MCP сервер + PAT |
| 13 memory (cognee) | `cognee` конфигурисан са провајдером модела |
| 15 browser-use | Playwright прегледачи инсталирани (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry локално окружење + преузети Qwen модел (на уређају, без облака) |
| `*-dotnet-*` бележнице | .NET Interactive kernel (подразумевано искључено; користити `-IncludeDotnet`) |

## Извештавање назад
Сажети у PASS/FAIL табелу груписану по лекцијама. Разделити праве регресије
(багове кода/конфигурације за исправку) од недостатака окружења (недостају Search/Foundry Local/PAT),
и навести неуспеле `log_*.txt` за сваки стварни неуспех.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->