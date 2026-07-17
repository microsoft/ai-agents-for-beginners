---
name: testing-course-samples
---
# Тестване на примерите от курса

Проверете дали тетрадките с уроци и примерите с код се изпълняват успешно срещу активна
среда Microsoft Foundry / Azure OpenAI. Репозиторият съдържа скрипт за изпълнение в
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), който
изпълнява всяка Python тетрадка без графичен интерфейс и извежда матрица с PASS/FAIL резултати.

## Кога да се използва
- "Проверете дали всички тетрадки / примери работят срещу моя Azure абонамент."
- "Извършете бърз тест на курса след ъпгрейд на пакети или смяна на модели."
- "Кои уроци все още преминават / провалят изпитанието на живо?"

Не използвайте това за AI Smoke Test GitHub Action (който валидира *действащите*
хоствани агенти — вижте [`tests/README.md`](../../../tests/README.md)). Тази функционалност
изпълнява тетрадките локално.

## Предварителни условия (проверете първо)
1. **Python 3.12+** с зависимостите на курса: `python -m pip install -r requirements.txt`
   плюс изпълнителя: `python -m pip install nbconvert ipykernel`.
2. **`.env` в корена на репото** (копирайте от [`.env.example`](../../../../../.env.example)) с поне следното:
   - `AZURE_AI_PROJECT_ENDPOINT` — крайна точка на Foundry проекта
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — активна (неоттеглена) версия на модела (например `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) и `AZURE_OPENAI_DEPLOYMENT`
     за уроци, които директно извикват Azure OpenAI (Урок 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** е изпълнен — примерите се удостоверяват с `AzureCliCredential` (Entra ID, без ключ).
4. Уверете се, че разполагането на модела съществува:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Изпълнение на проверката
```powershell
# Всички Python тетрадки (пропуска .NET, .venv, site-packages, преводи, skill assets)
pwsh scripts/validate-notebooks.ps1

# Единичен урок, с по-дълъг таймаут на клетка
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Просто изброява какво би се изпълнило (без изпълнение)
pwsh scripts/validate-notebooks.ps1 -List

# Ясен интерпретатор (ако `python` не е в PATH, напр. псевдоним от Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Скриптът създава изпълнени копия, логове за всяка тетрадка и `results.json` в
`$env:TEMP\aiab-nbval` и излиза с брой на неуспехите.

## Интерпретиране на резултатите
- `PASS` — тетрадката е изпълнена изцяло без грешки в клетки.
- `FAIL` — показва се първият ред с `*Error` / `*Exception`; отворете съответния
  `log_*.txt` в изходната папка за пълния traceback.
- Провал на единична тетрадка е ограничен от `-Timeout` (за всяка клетка), така че зацикляща
  клетка с участието на човек се показва като `StdinNotImplementedError` вместо да блокира.

## Уроци, които изискват допълнителни ресурси (очаква се да не минат без тях)
| Урок | Допълнително изискване |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, ключ) — има резервен път в паметта |
| 11 MCP / GitHub | GitHub MCP сървър + PAT |
| 13 memory (cognee) | `cognee` конфигуриран с доставчик на модел |
| 15 browser-use | Инсталирани браузъри Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + изтеглен модел Qwen (на устройството, без облак) |
| `*-dotnet-*` тетрадки | .NET Interactive kernel (по подразбиране изключен; използвайте `-IncludeDotnet`) |

## Отчети
Обобщете като таблица PASS/FAIL групирана по урок. Отделете истинските регресии
(грешки в код/конфигурация за поправка) от пропуски в средата (липсващ Search/Foundry Local/PAT),
и посочете съответния провален `log_*.txt` за всеки реален провал.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->