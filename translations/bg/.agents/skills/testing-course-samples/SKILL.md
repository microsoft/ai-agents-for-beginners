---
name: testing-course-samples
---
# Тестване на примерите от курса

Валидирайте, че тетрадките на уроците и примерите с код се изпълняват спрямо активна
Microsoft Foundry / Azure OpenAI конфигурация. Репозиторият предоставя скрипт за изпълнение на
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), който
изпълнява всяка Python тетрадка без графичен интерфейс и отпечатва матрица PASS/FAIL.

## Кога да се използва
- "Валидирайте всички тетрадки / примери спрямо моя Azure абонамент."
- "Направете бърз тест на курса след ъпгрейд на пакети или промяна на модели."
- "Кои уроци все още минават / не минават на живо?"

Не използвайте това за AI Smoke Test GitHub Action (който валидира *публикувани*
хостнати агенти — вижте [`tests/README.md`](../../../tests/README.md)). Тази функционалност
изпълнява тетрадките локално.

## Предварителни изисквания (проверете първо)
1. **Python 3.12+** с зависимости от курса: `python -m pip install -r requirements.txt`
   плюс изпълнителя: `python -m pip install nbconvert ipykernel`.
2. **`.env` в корена на репото** (копирайте от [`.env.example`](../../../../../.env.example)) с поне:
   - `AZURE_AI_PROJECT_ENDPOINT` — крайна точка на Foundry проекта
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — неоттеглено разгръщане (например `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) и `AZURE_OPENAI_DEPLOYMENT`
     за уроците, които ползват Azure OpenAI директно (Урок 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** изпълнено — примерите удостоверяват чрез `AzureCliCredential` (Entra ID, без ключ).
4. Проверете дали разгръщането на модела съществува:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Изпълнение на валидацията
```powershell
# Всички Python тетрадки (пропуска .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# Един урок, с по-дълго време за изчакване на клетка
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Просто изброява какво би се изпълнило (без изпълнение)
pwsh scripts/validate-notebooks.ps1 -List

# Ясен интерпретатор (ако `python` не е в PATH, например псевдоним от Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Скриптът записва изпълнени копия, дневници за всяка тетрадка и `results.json` в
`$env:TEMP\aiab-nbval` и излиза с брой на неуспешните тестове.

Временни грешки (HTTP 429 ограничения на споделен абонамент, случайни
прекъсвания на `AzureCliCredential` токена или таймаути) се повтарят автоматично
(`-Retries`, по подразбиране 2, с `-RetryDelaySeconds` пауза, по подразбиране 20). Ако някое
разгръщане на модел редовно дава 429, проверете квотата GlobalStandard
TPM на абонамента (`az cognitiveservices usage list -l <region>`) — увеличаването на капацитета на
единично разгръщане не помага, ако квотата на *абонамента* е изчерпана.

## Интерпретиране на резултатите
- `PASS` — тетрадката се изпълни изцяло без грешки в клетки.
- `FAIL` — показва се първият ред `*Error` / `*Exception`; отворете съответния
  `log_*.txt` в изходната папка за пълния traceback.
- Провал на една тетрадка е ограничен от `-Timeout` (за всяка клетка), така че зацикляща
  клетка с човешка намеса се показва като `StdinNotImplementedError` вместо да замръзне.

## Уроци, които изискват допълнителни ресурси (очакват се неуспехи без тях)
| Урок | Допълнително изискване |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, ключ) — има резервен маршрут с памет |
| 11 MCP / GitHub | GitHub MCP сървър + PAT |
| 13 memory (cognee) | `cognee` конфигуриран с доставчик на модел |
| 15 browser-use | Инсталирани браузъри Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + изтеглен Qwen модел (на устройството, без облак) |
| `*-dotnet-*` тетрадки | .NET Interactive kernel (изключени по подразбиране; използвайте `-IncludeDotnet`) |

## Отчитане обратно
Сумирайте като таблица PASS/FAIL групирана по урок. Разделете на реални регресии
(грешки в код/конфигурация за оправяне) от липси в средата (липсващ Search/Foundry Local/PAT),
и цитирате неуспелия `log_*.txt` за всеки реален провал.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->