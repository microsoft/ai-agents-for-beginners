# Настройка курса

## Введение

В этом уроке рассматривается, как запускать примеры кода этого курса.

## Присоединяйтесь к другим учащимся и получайте помощь

Прежде чем начинать клонировать ваш репозиторий, присоединитесь к [каналу Discord AI Agents For Beginners](https://aka.ms/ai-agents/discord), чтобы получить помощь с настройкой, задать вопросы по курсу или связаться с другими учащимися.

## Клонируйте или форкните этот репозиторий

Для начала, пожалуйста, клонируйте или форкните репозиторий GitHub. Это создаст вашу собственную версию материалов курса, чтобы вы могли запускать, тестировать и настраивать код!

Это можно сделать, щелкнув по ссылке <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкнуть репозиторий</a>

Теперь у вас должна быть своя форк-версия этого курса по следующей ссылке:

![Forked Repo](../../../translated_images/ru/forked-repo.33f27ca1901baa6a.webp)

### Поверхностный клон (рекомендуется для воркшопа / Codespaces)

  >Полный репозиторий может быть большим (~3 ГБ), если скачивать всю историю и все файлы. Если вы посещаете только воркшоп или нужны лишь несколько папок уроков, поверхностный клон (shallow clone) или частичный клон (sparse clone) позволяет избежать большей части загрузки, сокращая историю и/или пропуская блобы.

#### Быстрый поверхностный клон — минимальная история, все файлы

Замените `<your-username>` в командах ниже на URL вашего форка (или на URL upstream, если предпочитаете).

Чтобы клонировать только историю последних коммитов (малый объем загрузки):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Чтобы клонировать определенную ветку:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частичный (sparse) клон — минимальное количество blob-объектов + только выбранные папки

Для этого используется partial clone и sparse-checkout (требуется Git 2.25+ и рекомендуется современный Git с поддержкой partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Перейдите в папку репозитория:

```bash|powershell
cd ai-agents-for-beginners
```

Затем укажите, какие папки вам нужны (пример ниже показывает две папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

После клонирования и проверки файлов, если вам нужны только файлы и вы хотите освободить место (без истории git), удалите метаданные репозитория (💀 необратимо — потеряете всю функциональность Git: коммиты, pull, push и история станут недоступны).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Использование GitHub Codespaces (рекомендуется для избежания локальных больших загрузок)

- Создайте новый Codespace для этого репозитория через [GitHub UI](https://github.com/codespaces).  

- В терминале созданного Codespace выполните одну из команд поверхностного/частичного клона выше, чтобы загрузить только нужные папки уроков в рабочее пространство Codespace.
- Опционально: после клонирования внутри Codespaces удалите .git для освобождения места (см. команды удаления выше).
- Примечание: если вы хотите открыть репозиторий напрямую в Codespaces (без дополнительного клона), учтите, что Codespaces создаст devcontainer и может провизировать больше, чем нужно. Клонирование поверхностной копии внутри нового Codespace дает вам больше контроля над использованием диска.

#### Советы

- Всегда заменяйте URL клонирования на ваш форк, если планируете вносить изменения/делать коммиты.
- Если в дальнейшем понадобится больше истории или файлов, их можно получить с помощью fetch или изменить sparse-checkout для включения дополнительных папок.

## Запуск кода

Этот курс предлагает серию Jupyter Notebooks, которые вы можете запускать, чтобы получить практический опыт создания AI-агентов.

Примеры кода используют **Microsoft Agent Framework (MAF)** с `FoundryChatClient`, который подключается к **Microsoft Foundry Agent Service V2** (API ответов) через **Microsoft Foundry**.

Все Python ноутбуки имеют в названии `*-python-agent-framework.ipynb`.

## Требования

- Python 3.12+
  - **ПРИМЕЧАНИЕ**: Если у вас не установлен Python 3.12, установите его. Затем создайте виртуальное окружение с помощью python3.12, чтобы установить правильные версии из файла requirements.txt.
  
    >Пример

    Создание директории виртуального окружения Python:

    ```bash|powershell
    python -m venv venv
    ```

    Затем активируйте виртуальное окружение для:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Для примеров кода на .NET убедитесь, что установлен [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или новее. Проверьте установленную версию SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Необходим для аутентификации. Установите с [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Подписка Azure** — Для доступа к Microsoft Foundry и Microsoft Foundry Agent Service.
- **Проект Microsoft Foundry** — Проект с развернутой моделью (например, `gpt-5-mini`). См. [Шаг 1](#шаг-1-создайте-проект-microsoft-foundry) ниже.

В корне репозитория есть файл `requirements.txt` с перечнем необходимых Python пакетов для запуска примеров кода.

Установить их можно, выполнив следующую команду в терминале в корне репозитория:

```bash|powershell
pip install -r requirements.txt
```

Рекомендуется создать виртуальное окружение Python, чтобы избежать конфликтов и проблем.

## Настройка VSCode

Убедитесь, что в VSCode используется правильная версия Python.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка Microsoft Foundry и Microsoft Foundry Agent Service

### Шаг 1: Создайте проект Microsoft Foundry

Для запуска ноутбуков вам понадобится Microsoft Foundry **hub** и **проект** с развернутой моделью.

1. Перейдите на [ai.azure.com](https://ai.azure.com) и войдите в свою учетную запись Azure.
2. Создайте **hub** (или используйте существующий). См.: [Обзор ресурсов Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Внутри hub создайте **проект**.
4. Разверните модель (например, `gpt-5-mini`) через **Models + Endpoints** → **Deploy model**.

### Шаг 2: Получите URL эндпоинта проекта и имя развертывания модели

В вашем проекте на портале Microsoft Foundry:

- **Project Endpoint** — Перейдите на страницу **Overview** и скопируйте URL эндпоинта.

![Project Connection String](../../../translated_images/ru/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Зайдите в **Models + Endpoints**, выберите развернутую модель и запишите **Deployment name** (например, `gpt-5-mini`).

### Шаг 3: Войдите в Azure с помощью `az login`

Все ноутбуки используют **`AzureCliCredential`** для аутентификации — никаких API ключей в управлении. Требуется вход через Azure CLI.

1. **Установите Azure CLI**, если еще не сделали этого: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Войдите** с помощью команды:

    ```bash|powershell
    az login
    ```

    Или, если вы в удаленной среде/Codespace без браузера:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Выберите подписку**, если будет запрос — укажите ту, в которой находится ваш проект Foundry.

4. **Проверьте** успешный вход:

    ```bash|powershell
    az account show
    ```

> **Зачем `az login`?** Ноутбуки аутентифицируются с `AzureCliCredential` из пакета `azure-identity`. Это значит, что ваша сессия Azure CLI предоставляет учетные данные — никаких ключей или секретов в файле `.env`. Это [лучший подход к безопасности](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Шаг 4: Создайте файл `.env`

Скопируйте файл примера:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Откройте `.env` и заполните два значения:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Переменная | Где найти |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Портал Foundry → ваш проект → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Портал Foundry → **Models + Endpoints** → имя развернутой модели |

На этом настройка большинства уроков завершена! Ноутбуки будут автоматически аутентифицироваться через вашу сессию `az login`.

### Шаг 5: Установите зависимости Python

```bash|powershell
pip install -r requirements.txt
```

Рекомендуется запускать это внутри ранее созданного виртуального окружения.

## Дополнительная настройка для урока 5 (Agentic RAG)

Урок 5 использует **Azure AI Search** для retrieval-augmented generation. Если вы планируете запускать этот урок, добавьте эти переменные в файл `.env`:

| Переменная | Где найти |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Портал Azure → ваш ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Портал Azure → ваш ресурс **Azure AI Search** → **Settings** → **Keys** → основной административный ключ |

## Дополнительная настройка для уроков с прямым вызовом Azure OpenAI (уроки 6 и 8)

Некоторые ноутбуки в уроках 6 и 8 вызывают **Azure OpenAI** напрямую (используя **Responses API**), а не через проект Microsoft Foundry. Ранее эти примеры использовали GitHub Models, которые устарели (будут отключены в июле 2026) и не поддерживают Responses API. Если вы планируете запускать эти примеры, добавьте следующие переменные в `.env`:

| Переменная | Где найти |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Портал Azure → ресурс **Azure OpenAI** → **Keys and Endpoint** → Endpoint (например, `https://<ваш-ресурс>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Имя вашей развернутой модели (например, `gpt-5-mini`), которая поддерживает Responses API |
| `AZURE_OPENAI_API_KEY` | Опционально — если вы используете аутентификацию по ключу, а не `az login` / Entra ID |

> Responses API использует стабильный эндпоинт `/openai/v1/`, поэтому параметр `api-version` не нужен. Войдите через `az login` для безключевой аутентификации Entra ID.

## Альтернативный провайдер: MiniMax (совместим с OpenAI)

[MiniMax](https://platform.minimaxi.com/) предоставляет модели с большим контекстом (до 204К токенов) через API, совместимый с OpenAI. Поскольку `OpenAIChatClient` Microsoft Agent Framework работает с любым совместимым эндпоинтом OpenAI, вы можете использовать MiniMax как замену Azure OpenAI или OpenAI.

Добавьте эти переменные в ваш файл `.env`:

| Переменная | Где найти |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Используйте `https://api.minimax.io/v1` (значение по умолчанию) |
| `MINIMAX_MODEL_ID` | Имя модели для использования (например, `MiniMax-M3`) |

**Пример моделей**: `MiniMax-M3` (рекомендуется), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (более быстрые ответы). Названия моделей и их доступность могут изменяться со временем, а доступ к конкретной модели может зависеть от вашей учетной записи или региона — проверьте текущий список на [MiniMax Platform](https://platform.minimaxi.com/). Если модель `MiniMax-M3` недоступна для вашей учетной записи, установите `MINIMAX_MODEL_ID` в модель, к которой у вас есть доступ (например, `MiniMax-M2.7`).

Примеры кода, использующие `OpenAIChatClient` (например, урок 14 с бронированием отеля), будут автоматически обнаруживать и использовать вашу конфигурацию MiniMax при установке `MINIMAX_API_KEY`.

## Альтернативный провайдер: Foundry Local (запуск моделей на устройстве)

[Foundry Local](https://foundrylocal.ai) — это лёгкая среда исполнения, которая загружает, управляет и обслуживает языковые модели **полностью на вашем собственном компьютере** через OpenAI-совместимый API — без облака, подписки Azure и API ключей. Отличный вариант для офлайн-разработки, экспериментов без облачных затрат или хранения данных локально.

Поскольку Microsoft Agent Framework’s `OpenAIChatClient` работает с любым OpenAI-совместимым эндпоинтом, Foundry Local является заменой Azure OpenAI на локальной машине.

**1. Установите Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Скачайте и запустите модель** (это также запустит локальный сервис):

```bash
foundry model list          # посмотреть доступные модели
foundry model run phi-4-mini
```

**3. Установите Python SDK** для обнаружения локального эндпоинта:

```bash
pip install foundry-local-sdk
```

**4. Укажите Microsoft Agent Framework использовать вашу локальную модель:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Загружает (при необходимости) и обслуживает модель локально, затем обнаруживает конечную точку/порт.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # например http://localhost:<port>/v1
    api_key=manager.api_key,        # всегда "не требуется" для Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Примечание:** Foundry Local предоставляет OpenAI-совместимый эндпоинт **Chat Completions**. Используйте его для локальной разработки и офлайн-сценариев. Для полного функционала **Responses API** (сохранение состояния бесед, глубокая оркестрация инструментов и агентская разработка) используйте **Azure OpenAI** или проект **Microsoft Foundry**, как показано в уроках. Смотрите [документацию Foundry Local](https://foundrylocal.ai) для актуального каталога моделей и поддержки платформы.

## Дополнительная настройка для урока 8 (Bing Grounding Workflow)


В условной рабочей тетради из урока 8 используется **Bing grounding** через Microsoft Foundry. Если вы планируете запустить этот пример, добавьте эту переменную в ваш файл `.env`:

| Переменная | Где найти |
|----------|-----------------|
| `BING_CONNECTION_ID` | Портал Microsoft Foundry → ваш проект → **Управление** → **Подключенные ресурсы** → ваше соединение Bing → скопируйте идентификатор соединения |

## Решение проблем

### Ошибки проверки SSL сертификата на macOS

Если вы используете macOS и получаете ошибку вроде:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Это известная проблема Python на macOS, когда системные SSL сертификаты не доверяются автоматически. Попробуйте следующие решения по порядку:

**Вариант 1: Запустите скрипт установки сертификатов Python (рекомендуется)**

```bash
# Замените 3.XX на установленную версию Python (например, 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Вариант 2: Используйте `connection_verify=False` в вашей рабочей тетради (только для GitHub Models notebooks)**

В рабочей тетради урока 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) уже включено закомментированное решение. Раскомментируйте `connection_verify=False` при создании клиента:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Отключите проверку SSL, если возникают ошибки сертификата
)
```

> **⚠️ Внимание:** Отключение проверки SSL (`connection_verify=False`) снижает безопасность, пропуская проверку сертификата. Используйте это только как временное решение в средах разработки, никогда в продакшене.

**Вариант 3: Установите и используйте `truststore`**

```bash
pip install truststore
```

Затем добавьте следующее в начало вашей рабочей тетради или скрипта перед выполнением любых сетевых вызовов:

```python
import truststore
truststore.inject_into_ssl()
```

## Застряли?

Если у вас возникли проблемы с запуском этой настройки, присоединяйтесь к нашему <a href="https://discord.gg/kzRShWzttr" target="_blank">сообществу Azure AI в Discord</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">создайте issue</a>.

## Следующий урок

Теперь вы готовы запускать код этого курса. Желаем успехов в изучении мира AI-агентов!

[Введение в AI-агентов и примеры использования агентов](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->