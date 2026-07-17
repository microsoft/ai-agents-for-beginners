---
name: testing-course-samples
---
# Тестирање узорака курса

Потврдити да се билешке лекција и примерци кода извршавају на live
Microsoft Foundry / Azure OpenAI подешавању. Репо испоручује извршни програм на
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) који
извршава сваки Python бележник без интерфејса и штампа PASS/FAIL матрицу.

## Када користити
- "Проверити све бележнице / узорке у односу на моју Azure претплату."
- "Извршити основно тестирање курса након надоградње пакета или промене модела."
- "Које лекције и даље пролазе / не пролазе уживо?"

Не користити за AI Smoke Test GitHub Акцију (која проверава *распоређене*
уграђене агенте — видети [`tests/README.md`](../../../tests/README.md)). Ова вештина
покреће бележнице локално.

## Захтеви (прво проверити)
1. **Python 3.12+** са зависностима курса: `python -m pip install -r requirements.txt`
   плус извршни део: `python -m pip install nbconvert ipykernel`.
2. **`.env` у корену репоа** (копирати са [`.env.example`](../../../../../.env.example)) са најмање:
   - `AZURE_AI_PROJECT_ENDPOINT` — крајња тачка пројекта Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — неповучена дистрибуција (нпр. `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) и `AZURE_OPENAI_DEPLOYMENT`
     за лекције које директно позивају Azure OpenAI (лекција 06, 02-azure-openai, 14 handoff/human-loop).
3. Завршен `az login` — узорци аутентификују се помоћу `AzureCliCredential` (Entra ID, без кључа).
4. Потврдити да дистрибуција модела постоји:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Извршавање провере
```powershell
# Сви Python нотебуци (без .NET, .venv, site-packages, преводи, ресурсима вештина)
pwsh scripts/validate-notebooks.ps1

# Једна лекција, са дужим временом чекања по ћелији
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Само навести шта би се покренуло (без извршења)
pwsh scripts/validate-notebooks.ps1 -List

# Јасан интерпретер (ако `python` није у PATH, нпр. Windows Store алјас)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Скрипта записује извршене копије, дневнике по бележници и `results.json` у
`$env:TEMP\aiab-nbval` и излази са бројем неуспеха.

## Тумачење резултата
- `PASS` — бележница се извршила од почетка до краја без грешке у ћелији.
- `FAIL` — приказан је први ред `*Error` / `*Exception`; отворити одговарајући
  `log_*.txt` у излазном директоријуму за потпуни приказ пратитеља грешке.
- Неуспех једне бележнице је ограничен са `-Timeout` (по ћелији), тако да ћелија са људским уласком која запне
  приказује се као `StdinNotImplementedError` уместо да виси.

## Лекције које захтевају додатне ресурсе (очекује се да неће проћи без њих)
| Лекција | Додатни захтев |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, кључ) — има резервни пут у памћењу |
| 11 MCP / GitHub | GitHub MCP сервер + PAT |
| 13 memory (cognee) | `cognee` конфигурисан са добављачем модела |
| 15 browser-use | Playwright прегледачи инсталирани (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + преузет Qwen модел (на уређају, без облака) |
| `*-dotnet-*` бележнице | .NET Interactive кернел (искључен по подразумеваној вредности; користити `-IncludeDotnet`) |

## Извештавање
Сажети као PASS/FAIL табелу по лекцијама. Раздвојити стварне регресије
(багове у коду/конфигурацији које треба исправити) од недостатака у окружењу (недостају Search/Foundry Local/PAT),
и навести неуспеле `log_*.txt` за сваки стварни неуспех.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->