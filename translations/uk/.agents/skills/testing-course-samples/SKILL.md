---
name: testing-course-samples
---
# Тестування прикладів курсу

Перевірте, що нотатники уроків і приклади коду запускаються у живому середовищі
Microsoft Foundry / Azure OpenAI. Репозиторій містить виконувач у
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), який
виконує кожен Python ноутбук без користувацького інтерфейсу й виводить матрицю PASS/FAIL.

## Коли використовувати
- "Перевірити всі ноутбуки / приклади на моїй підписці Azure."
- "Швидко протестувати курс після оновлення пакетів або зміни моделей."
- "Які уроки все ще проходять / провалюються у живому режимі?"

**Не** використовуйте це для AI Smoke Test GitHub Action (який перевіряє *розгорнуті*
хостовані агенти — див. [`tests/README.md`](../../../tests/README.md)). Цей скрипт
запускає ноутбуки локально.

## Вимоги (перевірити спочатку)
1. **Python 3.12+** з залежностями курсу: `python -m pip install -r requirements.txt`
   та виконувачем: `python -m pip install nbconvert ipykernel`.
2. **`.env` у корені репо** (скопіювати з [`.env.example`](../../../../../.env.example)) з принаймні:
   - `AZURE_AI_PROJECT_ENDPOINT` — кінцева точка проекту Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — не застаріле розгортання (наприклад, `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) та `AZURE_OPENAI_DEPLOYMENT`
     для уроків, що звертаються безпосередньо до Azure OpenAI (Lesson 06, 02-azure-openai, 14 handoff/human-loop).
3. Виконано **`az login`** — приклади аутентифікуються через `AzureCliCredential` (Entra ID, без ключів).
4. Перевірте, що розгортання моделі існує:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Запуск перевірки
```powershell
# Всі Python ноутбуки (ігнорує .NET, .venv, site-packages, переклади, ресурси навичок)
pwsh scripts/validate-notebooks.ps1

# Окремий урок із більшим часом очікування на кожну клітинку
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Просто перелічити, що буде виконано (без запуску)
pwsh scripts/validate-notebooks.ps1 -List

# Явний інтерпретатор (якщо `python` не в PATH, наприклад, псевдонім Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Скрипт записує виконані копії, логи по кожному ноутбуку та `results.json` у
`$env:TEMP\aiab-nbval` і завершується з кількістю помилок.

## Інтерпретація результатів
- `PASS` — ноутбук виконався повністю без помилок у клітинках.
- `FAIL` — показується перший рядок `*Error` / `*Exception`; відкрийте відповідний
  файл `log_*.txt` у вихідному каталозі для повного трасування.
- Помилка одного ноутбука обмежена таймаутом `-Timeout` (для кожної клітинки), тому зависання
  клітинки з human-in-the-loop викликає `StdinNotImplementedError` замість зависання.

## Уроки, що потребують додаткових ресурсів (очікувано що проваляться без них)
| Урок | Додаткові вимоги |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, ключ) — має резервний варіант у пам’яті |
| 11 MCP / GitHub | MCP сервер GitHub + PAT |
| 13 memory (cognee) | `cognee` налаштований із провайдером моделей |
| 15 browser-use | Встановлені браузери Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + завантажена модель Qwen (на пристрої, без хмари) |
| `*-dotnet-*` ноутбуки | Ядро .NET Interactive (за замовчуванням виключене; використовувати `-IncludeDotnet`) |

## Звітність
Підсумуйте у таблиці PASS/FAIL, згрупованій за уроками. Відокреміть реальні регресії
(помилки коду/конфігурації, які потрібно виправити) від проблем середовища (відсутній Search/Foundry Local/PAT),
та наведіть лог-файли `log_*.txt` для кожної реальної помилки.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->