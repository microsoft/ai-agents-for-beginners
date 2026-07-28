---
name: testing-course-samples
---
# Тестування прикладів курсу

Перевірте, що навчальні зошити та приклади коду працюють з живим
налаштуванням Microsoft Foundry / Azure OpenAI. Репозиторій містить утиліту
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), яка
запускає кожен Python-зошит без інтерфейсу та виводить матрицю PASS/FAIL.

## Коли використовувати
- "Перевірити усі зошити / приклади на моїй Azure підписці."
- "Швидке тестування курсу після оновлення пакетів або зміни моделей."
- "Які уроки проходять / не проходять у живому режимі?"

Не використовуйте це для GitHub Action AI Smoke Test (який перевіряє *розгорнуті*
хостовані агенти — див. [`tests/README.md`](../../../tests/README.md)). Цей навик
запускає зошити локально.

## Попередні умови (перевірте перед запуском)
1. **Python 3.12+** з зависимостями курсу: `python -m pip install -r requirements.txt`
   плюс виконавець: `python -m pip install nbconvert ipykernel`.
2. **`.env` у корені репозиторію** (скопіюйте з [`.env.example`](../../../../../.env.example)) з мінімумом:
   - `AZURE_AI_PROJECT_ENDPOINT` — кінцева точка проєкту Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — не застаріле розгортання (наприклад, `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) та `AZURE_OPENAI_DEPLOYMENT`
     для уроків, що викликають Azure OpenAI напряму (Урок 06, 02-azure-openai, 14 handoff/human-loop).
3. Завершена команда **`az login`** — приклади автентифікуються через `AzureCliCredential` (Entra ID, безключовий доступ).
4. Перевірте, що розгортання моделі існує:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Запуск валідації
```powershell
# Усі блокноти Python (пропускає .NET, .venv, site-packages, переклади, ресурси навичок)
pwsh scripts/validate-notebooks.ps1

# Окремий урок з більшим тайм-аутом для кожної комірки
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Проста перелічення того, що буде запускатися (без виконання)
pwsh scripts/validate-notebooks.ps1 -List

# Явний інтерпретатор (якщо `python` немає в PATH, наприклад, псевдонім Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Скрипт записує виконані копії, логи для кожного зошиту, та `results.json` у
`$env:TEMP\aiab-nbval` і завершується з кількістю збоїв.

Тимчасові збої (поділена підписка з HTTP 429 обмеженнями частоти, поодинокі
збої токена `AzureCliCredential` або таймаут) автоматично повторюються
(`-Retries`, за замовчуванням 2, з затримкою `-RetryDelaySeconds`, за замовчуванням 20). Якщо
розгортання моделі постійно викликає 429, перевірте глобальну квоту TPM підписки
(`az cognitiveservices usage list -l <region>`) — збільшення потужності окремого
розгортання не допоможе, коли вичерпана квота *підписки*.

## Тлумачення результатів
- `PASS` — зошит запустився повністю без помилок у комірках.
- `FAIL` — показується перший рядок з `*Error` / `*Exception`; відкрийте відповідний
  файл `log_*.txt` у вихідній папці для повного трасування.
- Збої в одному зошиті обмежені параметром `-Timeout` (для кожної комірки), тож зависання
  з людиною у циклі виводить `StdinNotImplementedError` замість зависання.

## Уроки, що потребують додаткових ресурсів (очікувано не пройдуть без них)
| Урок | Додаткова вимога |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, ключ) — має резервний шлях з пам’яті |
| 11 MCP / GitHub | GitHub MCP сервер + PAT |
| 13 memory (cognee) | `cognee` налаштований з провайдером моделей |
| 15 browser-use | Встановлені браузери Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + завантажена модель Qwen (на пристрої, без хмари) |
| `*-dotnet-*` зошити | .NET Interactive kernel (за замовчуванням виключений; використовуйте `-IncludeDotnet`) |

## Звітність
Підсумуйте у таблиці PASS/FAIL згруповано за уроком. Відокремте справжні регресії
(помилки в коді/налаштуванні, які слід виправити) від прогалин у середовищі (відсутній Search/Foundry Local/PAT),
та наведіть файл `log_*.txt` для кожного реального збою.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->