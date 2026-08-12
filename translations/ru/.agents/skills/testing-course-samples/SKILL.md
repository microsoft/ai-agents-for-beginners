---
name: testing-course-samples
---
# Тестирование примеров курса

Проверьте, что тетради уроков и примеры кода запускаются с использованием живой
среды Microsoft Foundry / Azure OpenAI. В репозитории есть скрипт запуска по пути
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), который
выполняет каждую Python тетрадь без интерфейса и выводит матрицу PASS/FAIL.

## Когда использовать
- «Проверить все тетради/примеры в моей подписке Azure.»
- «Быстро протестировать курс после обновления пакетов или изменения моделей.»
- «Какие уроки всё ещё проходят / не проходят в реальном времени?»

**Не** используйте это для AI Smoke Test GitHub Action (который проверяет *развёрнутых*
агентов — смотрите [`tests/README.md`](../../../tests/README.md)). Этот скрипт
запускает тетради локально.

## Предварительные требования (проверьте сначала)
1. **Python 3.12+** с зависимостями курса: `python -m pip install -r requirements.txt`
   плюс исполнитель: `python -m pip install nbconvert ipykernel`.
2. **`.env` в корне репозитория** (скопировать из [`.env.example`](../../../../../.env.example)) с минимум:
   - `AZURE_AI_PROJECT_ENDPOINT` — конечная точка проекта Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — неустаревшее развертывание (например, `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) и `AZURE_OPENAI_DEPLOYMENT`
     для уроков, которые обращаются напрямую к Azure OpenAI (Урок 06, 02-azure-openai, 14 handoff/human-loop).
3. Выполнен **`az login`** — образцы аутентифицируются с помощью `AzureCliCredential` (Entra ID, без ключа).
4. Проверьте, что развертывание модели существует:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Запуск проверки
```powershell
# Все блокноты Python (исключая .NET, .venv, site-packages, переводы, ресурсы навыков)
pwsh scripts/validate-notebooks.ps1

# Один урок с увеличенным временем ожидания на ячейку
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Прекратить выполнение после вывода списка запускаемых элементов (без выполнения)
pwsh scripts/validate-notebooks.ps1 -List

# Явно указать интерпретатор (если `python` не в PATH, например, псевдоним из Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Скрипт записывает выполненные копии, логи для каждой тетради и `results.json` в
`$env:TEMP\aiab-nbval` и завершается с количеством ошибок.

Временные ошибки (ограничения по HTTP 429 в общей подписке, редкие
сбои токена `AzureCliCredential` или таймаут) автоматически повторяются
(`-Retries`, по умолчанию 2, с задержкой `-RetryDelaySeconds`, по умолчанию 20). Если
развертывание модели регулярно возвращает 429, проверьте квоту GlobalStandard
TPM подписки (`az cognitiveservices usage list -l <region>`) — увеличение мощности
одного развертывания не помогает, если квота *подписки* исчерпана.

## Интерпретация результатов
- `PASS` — тетрадь выполнилась полностью без ошибок в ячейках.
- `FAIL` — показана первая строка с `*Error` / `*Exception`; откройте соответствующий
  файл `log_*.txt` в директории вывода для полного трассирования.
- Ошибка одной тетради ограничена параметром `-Timeout` (на ячейку), поэтому зависшая
  ячейка с взаимодействием с человеком вызовет `StdinNotImplementedError` вместо зависания.

## Уроки, для которых нужны дополнительные ресурсы (ожидается ошибка без них)
| Урок | Дополнительное требование |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, ключ) — есть резервный путь в памяти |
| 11 MCP / GitHub | GitHub MCP сервер + PAT |
| 13 memory (cognee) | `cognee` настроен с провайдером модели |
| 15 browser-use | Установлены браузеры Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + загруженная модель Qwen (локально, без облака) |
| тетради с `*-dotnet-*` | .NET Interactive kernel (по умолчанию исключены; используйте `-IncludeDotnet`) |

## Отчет о результатах
Подведите итог в виде таблицы PASS/FAIL по урокам. Разделите реальные регрессии
(ошибки кода/конфигурации, которые нужно исправить) и проблемы окружения (отсутствие Search/Foundry Local/PAT),
с указанием файла `log_*.txt` для каждой настоящей ошибки.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->