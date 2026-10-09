# Настройка курса

## Введение

В этом уроке будет объяснено, как запускать примеры кода из этого курса.

## Присоединяйтесь к другим обучающимся и получите помощь

Перед тем, как начать клонировать репозиторий, присоединяйтесь к [Discord-каналу AI Agents For Beginners](https://aka.ms/ai-agents/discord), чтобы получить помощь с настройкой, задать вопросы по курсу или связаться с другими обучающимися.

## Клонирование или форк этого репозитория

Для начала клонируйте или создайте форк репозитория GitHub. Это создаст вашу собственную версию материала курса, чтобы вы могли запускать, тестировать и настраивать код!

Это можно сделать, кликнув по ссылке <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">создать форк репозитория</a>

Теперь у вас должна быть своя собственная версия форка курса по следующей ссылке:

![Forked Repo](../../../translated_images/ru/forked-repo.33f27ca1901baa6a.webp)

### Поверхностное клонирование (рекомендуется для воркшопов / Codespaces)

  >Полный репозиторий может занимать много места (~3 ГБ), если скачивать всю историю и все файлы. Если вы только посещаете воркшоп или нужны только некоторые папки уроков, поверхностное клонирование (или частичное) скачивает значительно меньше.

#### Быстрое поверхностное клонирование — минимальная история, все файлы

Замените `<your-username>` в командах ниже на URL вашего форка (или на URL исходного репозитория, если предпочитаете).

Чтобы клонировать только последнюю историю коммитов (небольшая загрузка):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Чтобы клонировать конкретную ветку:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частичное (разреженное) клонирование — минимальное количество blob и только выбранные папки

Использует частичное клонирование и sparse-checkout (требуется Git 2.25+ и рекомендуется современный Git с поддержкой частичного клонирования):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Перейдите в папку репозитория:

```bash
cd ai-agents-for-beginners
```

Затем укажите, какие папки вам нужны (пример ниже показывает две папки):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

После клонирования и проверки файлов, если вам нужны только файлы и вы хотите освободить место (без истории git), удалите метаданные репозитория (💀 необратимо — вы потеряете все функции Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Использование GitHub Codespaces (рекомендуется избегать больших загрузок на локальный компьютер)

- Создайте новый Codespace для этого репозитория через [GitHub UI](https://github.com/codespaces).  

- В терминале только что созданного Codespace выполните одну из указанных выше команд поверхностного/разреженного клонирования, чтобы загрузить только нужные папки уроков в рабочее пространство Codespace.
- Опционально: после клонирования внутри Codespaces удалите .git, чтобы освободить дополнительное место (см. команды удаления выше).
- Внимание: если вы предпочитаете открыть репозиторий непосредственно в Codespaces (без дополнительного клонирования), знайте, что Codespaces создаст devcontainer-среду и может по-прежнему загружать больше, чем требуется.

#### Советы

- Всегда заменяйте URL клона на ваш форк, если хотите редактировать/вносить коммиты.
- Если позже вам потребуется больше истории или файлов, вы можете их получить или настроить sparse-checkout для добавления дополнительных папок.

## Запуск кода

В этом курсе предоставлены серии ноутбуков Jupyter, с помощью которых вы получите практический опыт создания AI-агентов.

Примеры кода используют **Microsoft Agent Framework (MAF)** с `FoundryChatClient`, который подключается к **Microsoft Foundry Agent Service V2** (Responses API) через **Microsoft Foundry**.

Все Python-ноутбуки имеют название формата `*-python-agent-framework.ipynb`.

## Требования

- Python 3.12+
  - **ПРИМЕЧАНИЕ**: Если у вас не установлен Python 3.12, обязательно установите его. Затем создайте виртуальное окружение с помощью python3.12, чтобы гарантировать установку правильных версий из файла requirements.txt.
  
    >Пример

    Создайте директорию виртуального окружения Python:

    ```bash
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

- .NET 10+: Для примеров кода на .NET, убедитесь, что установлен [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или новее. Затем проверьте установленную версию .NET SDK:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — требуется для аутентификации. Установите с [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Подписка Azure** — для доступа к Microsoft Foundry и Microsoft Foundry Agent Service.
- **Проект Microsoft Foundry** — проект с развернутой моделью (например, `gpt-5-mini`). См. [Шаг 1](#шаг-1-создайте-проект-microsoft-foundry) ниже.

В корне репозитория есть файл `requirements.txt`, содержащий все необходимые пакеты Python для запуска примеров кода.

Вы можете установить их, запустив следующую команду в терминале из корня репозитория:

```bash
pip install -r requirements.txt
```

Рекомендуется создать виртуальное окружение Python, чтобы избежать конфликтов и проблем.

## Настройка VSCode

Убедитесь, что в VSCode используется правильная версия Python.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка Microsoft Foundry и Microsoft Foundry Agent Service

### Шаг 1: Создайте проект Microsoft Foundry

Для запуска ноутбуков вам понадобится **hub** и **проект** Microsoft Foundry с развернутой моделью.

1. Перейдите на [ai.azure.com](https://ai.azure.com) и войдите в аккаунт Azure.
2. Создайте **hub** (или используйте существующий). См.: [Обзор ресурсов Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Внутри hub создайте **проект**.
4. Разверните модель (например, `gpt-5-mini`) через **Models + Endpoints** → **Deploy model**.

### Шаг 2: Получите URL проекта и имя развертывания модели

В частности, в портал Microsoft Foundry для вашего проекта:

- **Project Endpoint** — перейдите на страницу **Overview** и скопируйте URL-адрес endpoint.

![Project Connection String](../../../translated_images/ru/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — перейдите в раздел **Models + Endpoints**, выберите развернутую модель и запомните **Deployment name** (например, `gpt-5-mini`).

### Шаг 3: Войдите в Azure с помощью `az login`

Большинство ноутбуков аутентифицируются через ваш **вход в Azure CLI** — используя `AzureCliCredential` или `DefaultAzureCredential` (оба используют вашу сессию `az login`) из пакета `azure-identity` — поэтому им не нужны API-ключи. Некоторые уроки и опциональные интеграции используют API-ключи; ознакомьтесь с требованиями каждого урока для дополнительных переменных окружения. Для этого необходимо войти через Azure CLI.

1. **Установите Azure CLI**, если еще не сделали этого: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Войдите** с помощью команды:

    ```bash
    az login
    ```

    Или, если вы в удаленной среде / Codespace без браузера:

    ```bash
    az login --use-device-code
    ```

3. **Выберите подписку**, если появится запрос — выберите ту, где находится ваш проект Foundry.

4. **Проверьте**, что вы вошли:

    ```bash
    az account show
    ```

> **Почему `az login`?** Ноутбуки аутентифицируются с помощью `AzureCliCredential` (или `DefaultAzureCredential`, который также использует вход в Azure CLI) из пакета `azure-identity`. Это значит, что ваша сессия Azure CLI предоставляет учетные данные — API-ключи или секреты в файле `.env` не требуются. Это считается [лучшей практикой безопасности](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Шаг 4: Создайте файл `.env`

Скопируйте пример файла:

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
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Портал Foundry → **Models + Endpoints** → имя вашей развернутой модели |

На этом настройка для большинства уроков завершена! Ноутбуки будут автоматически аутентифицироваться через вашу сессию `az login`.

### Шаг 5: Установите зависимости Python

```bash
pip install -r requirements.txt
```

Рекомендуется запускать эту команду внутри виртуального окружения, созданного вами ранее.

## Дополнительная настройка: Azure AI Search (уроки 5 и 16)

Ноутбуки уроков 5 (Agentic RAG) и 16 работают «из коробки» с **in-memory knowledge base** — дополнительные ресурсы Azure не требуются. Если вы хотите использовать настоящий индекс **Azure AI Search**, обратите внимание, что **на данный момент ноутбук урока 16 использует аутентификацию по ключу**: он переключается с in-memory поиска на Azure AI Search только если установлены **и** `AZURE_SEARCH_SERVICE_ENDPOINT`, **и** `AZURE_SEARCH_API_KEY`. В противном случае используется in-memory поиск — чтобы запустить на реальном индексе, нужно указать ключ администратора. Безключевая аутентификация с Microsoft Entra ID (RBAC) — рекомендуемый подход для вашего продакшн-кода, он совпадает с `az login`, используемым в остальных частях курса.

Шаги RBAC ниже применимы к примерам-просмотрам в руководстве по настройке и вашему коду. Они не включают безключевую аутентификацию в ноутбуке урока 16; там по-прежнему требуется и endpoint, и ключ администратора для Azure AI Search.

1. **Включите ролевой доступ** (role-based access) для сервиса поиска:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Назначьте себе необходимые роли** (создание/загрузка индексов и запросы):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Добавьте endpoint** в ваш файл `.env`:

| Переменная | Где найти |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Портал Azure → ваш ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Требуется (вместе с endpoint) для включения Azure AI Search в ноутбуке урока 16, который использует аутентификацию по ключу. Портал Azure → **Settings** → **Keys** → основной ключ администратора |

> **Почему безключевая аутентификация?** Админские ключи предоставляют полный доступ на запись к вашему сервису поиска и могут случайно утечь через `.env` файлы. С RBAC используется ваша идентичность из `az login` — тот же безключевой шаблон Entra ID, что и в ноутбуках курса (через `AzureCliCredential` / `DefaultAzureCredential`). Подробнее: [Подключение к Azure AI Search с ролями](https://learn.microsoft.com/azure/search/search-security-rbac).

См. [руководство по настройке Azure AI Search](./AzureSearch.md) с полными примерами создания индексов на Python и .NET.

## Дополнительная настройка для уроков, которые вызывают Azure OpenAI напрямую (уроки 6 и 8)

Некоторые ноутбуки из уроков 6 и 8 используют **Azure OpenAI** напрямую (через **Responses API**) без Microsoft Foundry. Ранее эти примеры использовали GitHub Models, которые устарели и не поддерживают Responses API. Добавьте в файл `.env` эти переменные:

| Переменная | Где найти |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Портал Azure → ваш ресурс **Azure OpenAI** → **Keys and Endpoint** → Endpoint (например, `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Имя вашей развернутой модели (например, `gpt-5-mini`), поддерживающей Responses API |
| `AZURE_OPENAI_API_KEY` | Опционально — только если используете аутентификацию по ключу вместо `az login` / Entra ID |

> Responses API использует стабильный endpoint `/openai/v1/`, поэтому параметр `api-version` не требуется. Войдите с `az login` для безключевой аутентификации Entra ID.

## Альтернативный провайдер: MiniMax (совместим с OpenAI)

[MiniMax](https://platform.minimaxi.com/) предоставляет модели с большим контекстом (до 204K токенов) через API, совместимый с OpenAI. Поскольку `OpenAIChatClient` Microsoft Agent Framework работает с любым совместимым OpenAI endpoint, вы можете использовать MiniMax как альтернативу для уроков, где используется `OpenAIChatClient`.

Добавьте эти переменные в ваш `.env` файл:

| Переменная | Где найти |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Платформа MiniMax](https://platform.minimaxi.com/) → API ключи |
| `MINIMAX_BASE_URL` | Используйте `https://api.minimax.io/v1` (значение по умолчанию) |
| `MINIMAX_MODEL_ID` | Имя модели для использования (например, `MiniMax-M3`) |

**Примеры моделей**: `MiniMax-M3` (рекомендуется), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (быстрее ответов). Имена моделей и их доступность могут со временем меняться, а доступ к модели зависит от вашей учетной записи.

Примеры кода с `OpenAIChatClient` (например, рабочий процесс бронирования отеля из урока 14) автоматически обнаружат и используют вашу конфигурацию MiniMax, если установлен `MINIMAX_API_KEY`.


## Альтернативный провайдер: Novita AI (совместимый с OpenAI)

[Novita AI](https://novita.ai/llm-api) предоставляет API, совместимый с OpenAI, для открытых и передовых LLM (DeepSeek, Llama, Qwen и других). Поскольку `OpenAIChatClient` из Microsoft Agent Framework работает с любым совместимым с OpenAI эндпоинтом, вы можете использовать Novita AI как замену Azure OpenAI или OpenAI.

Добавьте эти переменные в ваш файл `.env`:

| Переменная | Где найти |
|----------|-----------------|
| `NOVITA_API_KEY` | [Панель управления Novita AI](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | Используйте `https://api.novita.ai/openai/v1` (значение по умолчанию) |
| `NOVITA_MODEL_ID` | Имя модели для использования (например, `moonshotai/kimi-k3`) |

**Пример моделей**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI также размещает многие другие семейства открытых моделей (Llama, Qwen, GLM и другие) — ознакомьтесь с [библиотекой моделей Novita AI](https://novita.ai/llm-api) для актуального списка доступных моделей и их идентификаторов.

Текущие примеры не используют переменные `NOVITA_*` автоматически. Чтобы использовать Novita AI, явно передайте эти значения при создании `OpenAIChatClient` в используемом вами примере.

## Альтернативный провайдер: Foundry Local (запуск моделей на устройстве)

[Foundry Local](https://foundrylocal.ai) — это легковесное окружение, которое загружает, управляет и обслуживает языковые модели **полностью на вашем собственном устройстве** через API, совместимый с OpenAI — без необходимости облака.

Поскольку `OpenAIChatClient` из Microsoft Agent Framework работает с любым эндпоинтом, совместимым с OpenAI, Foundry Local является локальной заменой Azure OpenAI.

**1. Установите Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Скачайте и запустите модель** (это также запускает локальный сервис):

```bash
foundry model list          # посмотреть доступные модели
foundry model run phi-4-mini
```

**3. Установите Python SDK**, используемый для обнаружения локального эндпоинта:

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
    base_url=manager.endpoint,      # например, http://localhost:<порт>/v1
    api_key=manager.api_key,        # всегда "не требуется" для Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Примечание:** Foundry Local предоставляет OpenAI-совместимый эндпоинт **Chat Completions**. Используйте его для локальной разработки и работы офлайн. Для полного набора функций **Responses API** (состояния бесед и пр.) используйте Azure OpenAI или проект Microsoft Foundry.

## Дополнительные настройки для урока 8 (процесс привязки к Bing)

Блокнот условного рабочего процесса в уроке 8 использует **привязку к Bing** через Microsoft Foundry. Если вы планируете запускать этот пример, добавьте эту переменную в ваш `.env` файл:

| Переменная | Где найти |
|----------|-----------------|
| `BING_CONNECTION_ID` | Портал Microsoft Foundry → ваш проект → **Управление** → **Подключенные ресурсы** → ваше соединение Bing → скопируйте ID подключения |

## Устранение неполадок

### Ошибки проверки SSL-сертификата на macOS

Если вы используете macOS и столкнулись с ошибкой вроде:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Это известная проблема Python на macOS, когда системные SSL-сертификаты не доверяются автоматически. Попробуйте следующие решения по порядку:

**Вариант 1: Запустите скрипт установки сертификатов Python (рекомендуется)**

```bash
# Замените 3.XX на установленную версию Python (например, 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Вариант 2: Используйте `connection_verify=False` в вашем блокноте (только для блокнотов GitHub Models)**

В блокноте Урока 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) уже есть закомментированное обходное решение. Раскомментируйте `connection_verify=False`, если возникают ошибки сертификата:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Отключите проверку SSL, если вы сталкиваетесь с ошибками сертификата
)
```

> **⚠️ Внимание:** Отключение проверки SSL (`connection_verify=False`) снижает безопасность, пропуская проверку сертификатов. Используйте это только как временное решение в средах разработки. Никогда не применяйте в продакшене.

**Вариант 3: Установите и используйте `truststore`**

```bash
pip install truststore
```

Затем добавьте следующее в начало вашего блокнота или скрипта перед любыми сетевыми вызовами:

```python
import truststore
truststore.inject_into_ssl()
```

## Застряли?

Если у вас возникли проблемы с этой настройкой, присоединяйтесь к нашему <a href="https://discord.gg/kzRShWzttr" target="_blank">сообществу Azure AI в Discord</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">создайте issue</a>.

## Следующий урок

Теперь вы готовы запускать код этого курса. Успехов в изучении мира AI-агентов!

[Введение в AI-агентов и варианты их использования](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->