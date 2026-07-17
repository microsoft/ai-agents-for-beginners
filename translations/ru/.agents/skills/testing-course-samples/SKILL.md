---
name: testing-course-samples
---
# Тестирование примеров курса

Проверьте, что ноутбуки уроков и примеры кода работают с живой
настройкой Microsoft Foundry / Azure OpenAI. Репозиторий содержит скрипт
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), который
выполняет каждый Python-ноутбук без интерфейса и выводит матрицу PASS/FAIL.

## Когда использовать
- "Проверить все ноутбуки / примеры на моей подписке Azure."
- "Быстрый тест курса после обновления пакетов или изменения моделей."
- "Какие уроки успешно проходят / не проходят тест в живой среде?"

Не используйте это для GitHub Action AI Smoke Test (который проверяет *развернутые*
хостинговые агенты — см. [`tests/README.md`](../../../tests/README.md)). Этот инструмент
запускает ноутбуки локально.

## Предварительные требования (проверьте сначала)
1. **Python 3.12+** с зависимостями курса: `python -m pip install -r requirements.txt`
   а также исполнитель: `python -m pip install nbconvert ipykernel`.
2. **`.env` в корне репозитория** (копируйте из [`.env.example`](../../../../../.env.example)) с минимум:
   - `AZURE_AI_PROJECT_ENDPOINT` — конечная точка проекта Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — неустаревшее развертывание (например, `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) и `AZURE_OPENAI_DEPLOYMENT`
     для уроков, вызывающих Azure OpenAI напрямую (Урок 06, 02-azure-openai, 14 handoff/human-loop).
3. Выполнен **`az login`** — примеры аутентифицируются через `AzureCliCredential` (Entra ID, без ключа).
4. Проверьте наличие развертывания модели:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Запуск проверки
```powershell
# Все ноутбуки Python (исключая .NET, .venv, site-packages, переводы, ресурсы навыков)
pwsh scripts/validate-notebooks.ps1

# Один урок с увеличенным тайм-аутом на ячейку
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Просто перечислить, что будет запущено (без выполнения)
pwsh scripts/validate-notebooks.ps1 -List

# Явный интерпретатор (если `python` отсутствует в PATH, например, псевдоним Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Скрипт записывает выполненные копии, логи по каждому ноутбуку и `results.json` в
`$env:TEMP\aiab-nbval` и завершается с числом ошибок.

## Интерпретация результатов
- `PASS` — ноутбук выполнен полностью без ошибок в ячейках.
- `FAIL` — показывается первая строка с `*Error` / `*Exception`; откройте соответствующий
  файл `log_*.txt` в выходном каталоге для полного трейсбека.
- Ошибка одного ноутбука ограничена `-Timeout` (по каждой ячейке), поэтому зависание
  с человеко-в-петле ячейкой отображается как `StdinNotImplementedError`, а не зависает.

## Уроки, требующие дополнительных ресурсов (ожидается, что без них не пройдут)
| Урок | Дополнительное требование |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, ключ) — есть путь с запасным вариантом в памяти |
| 11 MCP / GitHub | Сервер GitHub MCP + PAT |
| 13 memory (cognee) | `cognee`, настроенный с провайдером модели |
| 15 browser-use | Установленные браузеры Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + загруженная модель Qwen (на устройстве, без облака) |
| Ноутбуки `*-dotnet-*` | Ядро .NET Interactive (по умолчанию исключено; используйте `-IncludeDotnet`) |

## Отчет
Составьте сводную таблицу PASS/FAIL по урокам. Отделяйте реальные регрессии
(ошибки кода/конфигурации для исправления) от проблем с окружением (отсутствует Search/Foundry Local/PAT),
и указывайте неудачные файлы `log_*.txt` для каждой реальной ошибки.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->