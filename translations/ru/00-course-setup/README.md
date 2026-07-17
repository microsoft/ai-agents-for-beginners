# Настройка курса

## Введение

В этом уроке будет рассказано, как запускать примеры кода из этого курса.

## Присоединяйтесь к другим учащимся и получайте помощь

Перед началом клонирования вашего репозитория присоединяйтесь к [Discord-каналу AI Agents For Beginners](https://aka.ms/ai-agents/discord), чтобы получить помощь с настройкой, задать вопросы по курсу или пообщаться с другими учащимися.

## Клонирование или форк репозитория

Для начала, пожалуйста, клонируйте или сделайте форк репозитория на GitHub. Это создаст вашу собственную версию материала курса, чтобы вы могли запускать, тестировать и изменять код!

Это можно сделать, нажав на ссылку <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">сделать форк репозитория</a>

Теперь у вас должна быть своя форк-версия этого курса по следующей ссылке:

![Forked Repo](../../../translated_images/ru/forked-repo.33f27ca1901baa6a.webp)

### Мелкое клонирование (рекомендуется для воркшопа / Codespaces)

  >Полный репозиторий может быть большим (~3 ГБ) при скачивании всей истории и всех файлов. Если вы участвуете только в воркшопе или вам нужны только некоторые папки с уроками, мелкое клонирование (или частичное) позволяет избежать большей части загрузки, обрезая историю и/или пропуская блобы.

#### Быстрое мелкое клонирование — минимальная история, все файлы

Замените `<your-username>` в командах ниже на URL вашего форка (или upstream URL, если предпочитаете).

Для клонирования только последней истории коммитов (малый объём загрузки):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Для клонирования определённой ветки:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частичное (sparse) клонирование — минимальные блобы + только выбранные папки

Используется частичное клонирование и sparse-checkout (требуется Git 2.25+ и рекомендуется современный Git с поддержкой частичного клонирования):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Переход в папку репозитория:

```bash|powershell
cd ai-agents-for-beginners
```

Затем укажите, какие папки вам нужны (пример для двух папок):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

После клонирования и проверки файлов, если вам нужны только сами файлы и вы хотите освободить место (без истории git), удалите метаданные репозитория (💀безвозвратно — вы потеряете функционал Git: не будет коммитов, pull, push и доступа к истории).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Использование GitHub Codespaces (рекомендуется для избежания больших локальных загрузок)

- Создайте новый Codespace для этого репозитория через [GitHub UI](https://github.com/codespaces).  

- В терминале вновь созданного Codespace выполните одну из команд мелкого или частичного клонирования выше, чтобы загрузить только нужные папки уроков в рабочее пространство Codespace.
- По желанию: после клонирования внутри Codespaces удалите .git для освобождения дополнительного места (см. команды удаления выше).
- Примечание: если хотите открыть репозиторий напрямую в Codespaces (без дополнительного клонирования), имейте в виду, что Codespaces создаст окружение devcontainer и может по-прежнему выделить больше ресурсов, чем нужно. Клонирование мелкой копии внутри свежего Codespace даёт больше контроля над использованием диска.

#### Советы

- Всегда заменяйте URL клонирования на ваш форк, если хотите редактировать или делать коммиты.
- Если позже нужны будут дополнительные история или файлы, вы можете получить их или скорректировать sparse-checkout, чтобы добавить папки.

## Запуск кода

В этом курсе представлены серии блокнотов Jupyter, которые можно запускать для практического опыта создания AI-агентов.

Примеры кода используют **Microsoft Agent Framework (MAF)** с `FoundryChatClient`, который подключается к **Microsoft Foundry Agent Service V2** (Responses API) через **Microsoft Foundry**.

Все Python-блокноты имеют обозначение `*-python-agent-framework.ipynb`.

## Требования

- Python 3.12+
  - **ПРИМЕЧАНИЕ**: Если у вас не установлен Python 3.12, установите его. Затем создайте виртуальное окружение с python3.12, чтобы гарантировать установку нужных версий из requirements.txt.
  
    >Пример

    Создание директории виртуального окружения Python:

    ```bash|powershell
    python -m venv venv
    ```

    Затем активируйте виртуальное окружение:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Для кода на .NET убедитесь, что установлен [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или новее. Затем проверьте версию установленного .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — требуется для аутентификации. Установите с [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — для доступа к Microsoft Foundry и Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — проект с развернутой моделью (например, `gpt-4.1-mini`). См. [Шаг 1](#шаг-1-создайте-проект-microsoft-foundry) ниже.

В корне репозитория есть файл `requirements.txt` со всеми необходимыми Python-пакетами для запуска примеров.

Установить их можно командой в терминале в корне репозитория:

```bash|powershell
pip install -r requirements.txt
```

Рекомендуется создать виртуальное Python-окружение, чтобы избежать конфликтов и проблем.

## Настройка VSCode

Убедитесь, что в VSCode используется правильная версия Python.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка Microsoft Foundry и Microsoft Foundry Agent Service

### Шаг 1: Создайте проект Microsoft Foundry

Вам нужен **hub** и **проект** в Microsoft Foundry с развернутой моделью для запуска блокнотов.

1. Перейдите на [ai.azure.com](https://ai.azure.com) и войдите с учётной записью Azure.
2. Создайте **hub** (или используйте существующий). См.: [Обзор ресурсов хаба](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Внутри хаба создайте **проект**.
4. Разверните модель (например, `gpt-4.1-mini`) через **Models + Endpoints** → **Deploy model**.

### Шаг 2: Получите URL эндпоинта проекта и имя развертывания модели

В вашем проекте на портале Microsoft Foundry:

- **Project Endpoint** — Перейдите на страницу **Overview** и скопируйте URL эндпоинта.

![Project Connection String](../../../translated_images/ru/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Перейдите в **Models + Endpoints**, выберите развернутую модель и запомните **Deployment name** (например, `gpt-4.1-mini`).

### Шаг 3: Войдите в Azure с помощью `az login`

Все блокноты используют **`AzureCliCredential`** для аутентификации — никаких API-ключей не надо. Требуется войти через Azure CLI.

1. **Установите Azure CLI**, если ещё не сделали это: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Войдите** командой:

    ```bash|powershell
    az login
    ```

    Или если вы в удалённой среде/Codespace без браузера:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Выберите подписку**, если будет запрос — выберите ту, где расположен ваш Foundry проект.

4. **Проверьте**, что вы вошли:

    ```bash|powershell
    az account show
    ```

> **Почему `az login`?** Блокноты аутентифицируются через `AzureCliCredential` из пакета `azure-identity`. Это значит, что сессия Azure CLI предоставляет данные для доступа — никаких API ключей или секретов в `.env` файле. Это [рекомендуемая практика безопасности](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

Откройте `.env` и заполните эти две переменные:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Переменная | Где найти |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Портал Foundry → ваш проект → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Портал Foundry → **Models + Endpoints** → имя вашей развернутой модели |

Это всё для большинства уроков! Блокноты будут автоматически аутентифицироваться через вашу сессию `az login`.

### Шаг 5: Установите Python-зависимости

```bash|powershell
pip install -r requirements.txt
```

Рекомендуется запускать эту команду внутри ранее созданного виртуального окружения.

## Дополнительная настройка для Урока 5 (Agentic RAG)

Урок 5 использует **Azure AI Search** для генерации с поддержкой поиска. Если планируете запускать этот урок, добавьте эти переменные в ваш `.env` файл:

| Переменная | Где найти |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Портал Azure → ваш ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Портал Azure → ваш ресурс **Azure AI Search** → **Settings** → **Keys** → основной ключ администратора |

## Дополнительная настройка для уроков, вызывающих Azure OpenAI напрямую (уроки 6 и 8)

Некоторые блокноты из уроков 6 и 8 обращаются к **Azure OpenAI** напрямую (используя **Responses API**), а не через проект Microsoft Foundry. Ранее эти образцы использовали GitHub Models, которые устарели (вывод из эксплуатации в июле 2026) и не поддерживают Responses API. Если планируете запускать эти примеры, добавьте эти переменные в ваш `.env` файл:

| Переменная | Где найти |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Портал Azure → ваш ресурс **Azure OpenAI** → **Keys and Endpoint** → Endpoint (например, `https://<ваш-ресурс>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Имя развернутой модели (например, `gpt-4.1-mini`), поддерживающей Responses API |
| `AZURE_OPENAI_API_KEY` | Опционально — только если используете аутентификацию по ключу вместо `az login` / Entra ID |

> Responses API использует стабильный endpoint `/openai/v1/`, поэтому параметр `api-version` не требуется. Войдите с помощью `az login`, чтобы использовать бесключевую аутентификацию Entra ID.

## Альтернативный провайдер: MiniMax (совместимый с OpenAI)

[MiniMax](https://platform.minimaxi.com/) предоставляет модели с большим контекстом (до 204K токенов) через API, совместимый с OpenAI. Поскольку `OpenAIChatClient` из Microsoft Agent Framework работает с любым OpenAI-совместимым endpoint, вы можете использовать MiniMax в качестве замены Azure OpenAI или OpenAI.

Добавьте эти переменные в ваш `.env` файл:

| Переменная | Где найти |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Платформа MiniMax](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Используйте `https://api.minimax.io/v1` (значение по умолчанию) |
| `MINIMAX_MODEL_ID` | Имя модели для использования (например, `MiniMax-M3`) |

**Пример моделей**: `MiniMax-M3` (рекомендуется), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (быстрее ответы). Имена моделей и их наличие могут изменяться, а доступ к конкретной модели зависит от вашего аккаунта или региона — проверьте [Платформу MiniMax](https://platform.minimaxi.com/) для актуального списка. Если `MiniMax-M3` недоступна вашему аккаунту, укажите `MINIMAX_MODEL_ID` модели с доступом (например, `MiniMax-M2.7`).

Примеры кода, использующие `OpenAIChatClient` (например, рабочий процесс бронирования гостиницы в уроке 14), автоматически обнаружат и воспользуются вашей конфигурацией MiniMax при наличии `MINIMAX_API_KEY`.

## Альтернативный провайдер: Foundry Local (запуск моделей на устройстве)

[Foundry Local](https://foundrylocal.ai) — это лёгкая среда выполнения, которая загружает, управляет и обслуживает языковые модели **полностью на вашем компьютере** через API, совместимый с OpenAI — без облака, подписки Azure и API ключей. Отличный вариант для офлайн-разработки, экспериментов без затрат на облако или сохранения данных локально.

Поскольку `OpenAIChatClient` из Microsoft Agent Framework работает с любым OpenAI-совместимым endpoint, Foundry Local — это полноценная локальная замена Azure OpenAI.

**1. Установите Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Загрузите и запустите модель** (это также запускает локальный сервис):

```bash
foundry model list          # посмотреть доступные модели
foundry model run phi-4-mini
```

**3. Установите Python SDK** для обнаружения локального эндпоинта:

```bash
pip install foundry-local-sdk
```

**4. Настройте Microsoft Agent Framework для работы с вашей локальной моделью:**

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

> **Примечание:** Foundry Local предоставляет OpenAI-совместимый endpoint для **Chat Completions**. Используйте его для локальной разработки и офлайн-сценариев. Для полного набора функций **Responses API** (состояния бесед, глубокая оркестрация инструментов, агентская разработка) обращайтесь к **Azure OpenAI** или проекту **Microsoft Foundry**, как показано в уроках. См. [документацию Foundry Local](https://foundrylocal.ai) для актуального каталога моделей и поддержки платформ.


## Дополнительная настройка для урока 8 (Рабочий процесс Bing Grounding)

В условном ноутбуке урока 8 используется **Bing grounding** через Microsoft Foundry. Если вы планируете запускать этот пример, добавьте эту переменную в ваш файл `.env`:

| Переменная | Где найти |
|-----------|-----------|
| `BING_CONNECTION_ID` | Портал Microsoft Foundry → ваш проект → **Management** → **Connected resources** → ваше подключение Bing → скопируйте ID подключения |

## Устранение неполадок

### Ошибки проверки SSL-сертификата на macOS

Если вы используете macOS и столкнулись с ошибкой вида:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Это известная проблема Python на macOS, когда системные SSL-сертификаты не доверяются автоматически. Попробуйте следующие решения по порядку:

**Вариант 1: Запустите скрипт установки сертификатов Python (рекомендуется)**

```bash
# Замените 3.XX на установленную версию Python (например, 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Вариант 2: Используйте `connection_verify=False` в вашем ноутбуке (только для ноутбуков GitHub Models)**

В ноутбуке урока 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) уже включено закомментированное решение. Раскомментируйте `connection_verify=False` при создании клиента:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Отключите проверку SSL, если возникают ошибки сертификата
)
```

> **⚠️ Внимание:** Отключение проверки SSL (`connection_verify=False`) снижает безопасность, пропуская проверку сертификата. Используйте это только как временное решение в средах разработки, никогда не применяйте в продакшене.

**Вариант 3: Установите и используйте `truststore`**

```bash
pip install truststore
```

Затем добавьте следующее в начало вашего ноутбука или скрипта до выполнения любых сетевых вызовов:

```python
import truststore
truststore.inject_into_ssl()
```

## Застряли где-то?

Если у вас возникли проблемы с этой настройкой, присоединяйтесь к нашему <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">создайте обращение (issue)</a>.

## Следующий урок

Теперь вы готовы запускать код этого курса. Желаем успехов в изучении мира AI-агентов!

[Введение в AI-агентов и примеры их использования](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->