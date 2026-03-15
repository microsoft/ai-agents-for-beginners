# Настройка курса

## Введение

В этом уроке мы рассмотрим, как запускать примеры кода из этого курса.

## Присоединяйтесь к другим учащимся и получите помощь

Перед тем, как клонировать репозиторий, присоединяйтесь к каналу [AI Agents For Beginners Discord](https://aka.ms/ai-agents/discord), чтобы получить помощь с настройкой, задать вопросы по курсу или пообщаться с другими учащимися.

## Клонирование или форк этого репозитория

Для начала клонируйте или форкните репозиторий с GitHub. Это создаст вашу собственную версию материалов курса, чтобы вы могли запускать, тестировать и изменять код!

Это можно сделать, кликнув по ссылке <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкнуть репозиторий</a>

Теперь у вас должна быть своя форкнутая версия этого курса по следующей ссылке:

![Forked Repo](../../../translated_images/ru/forked-repo.33f27ca1901baa6a.webp)

### Поверхностное клонирование (рекомендуется для воркшопа / Codespaces)

> Полный репозиторий может быть большим (~3 ГБ), если загружать всю историю и все файлы. Если вы только посещаете воркшоп или вам нужны только несколько папок с уроками, поверхностное (shallow) или разреженное (sparse) клонирование позволяет избежать большей части загрузки, сокращая историю и/или пропуская бинарные файлы.

#### Быстрое поверхностное клонирование — минимальная история, все файлы

Замените `<your-username>` в командах ниже на URL вашего форка (или URL исходного репозитория, если предпочитаете).

Для клонирования только последней истории коммита (малый объём загрузки):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Для клонирования конкретной ветки:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частичное (sparse) клонирование — минимальное количество blob'ов + только выбранные папки

Используется частичное клонирование и sparse-checkout (требуется Git 2.25+ и рекомендуется современный Git с поддержкой частичного клонирования):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Перейдите в папку репозитория:

```bash|powershell
cd ai-agents-for-beginners
```

Затем укажите папки, которые вам нужны (пример ниже показывает две папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

После клонирования и проверки файлов, если вам нужны только файлы и хотите освободить место (без истории git), удалите файлы метаданных репозитория (💀безвозвратно — вы потеряете всю функциональность Git: коммиты, операции pull/push и доступ к истории).

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

- В терминале вновь созданного Codespace выполните одну из команд поверхностного/разреженного клонирования выше, чтобы подтянуть только нужные папки уроков в рабочее пространство Codespace.
- По желанию: после клонирования внутри Codespaces удалите .git для освобождения дополнительного места (см. команды удаления выше).
- Внимание: если вы предпочитаете сразу открыть репозиторий в Codespaces (без дополнительного клонирования), учтите, что Codespaces создаст devcontainer и возможно задействует больше компонентов, чем вам нужно. Клонирование поверхностной копии внутри нового Codespace даёт больше контроля над использованием диска.

#### Советы

- Всегда заменяйте URL клона на ваш форк, если хотите редактировать и коммитить.
- Если позже понадобится больше истории или файлов, вы можете их получить или изменить настройки sparse-checkout для включения дополнительных папок.

## Запуск кода

Курс включает серию ноутбуков Jupyter, которые вы можете запускать для практического опыта создания AI-агентов.

Примеры кода используют **Microsoft Agent Framework (MAF)** с провайдером `AzureAIProjectAgentProvider`, который подключается к **Azure AI Agent Service V2** (API ответов) через **Microsoft Foundry**.

Все Python ноутбуки имеют название в формате `*-python-agent-framework.ipynb`.

## Требования

- Python 3.12+
  - **ПРИМЕЧАНИЕ**: Если у вас не установлен Python 3.12, обязательно установите его. Затем создайте виртуальное окружение с использованием python3.12, чтобы правильно установить версии из файла requirements.txt.

    >Пример

    Создание виртуального окружения Python:

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

- .NET 10+: Для примеров кода на .NET убедитесь, что установлен [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или новее. Проверьте версию установленного .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — требуется для аутентификации. Установите с [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Подписка Azure** — для доступа к Microsoft Foundry и Azure AI Agent Service.
- **Проект Microsoft Foundry** — проект с развернутой моделью (например, `gpt-4o`). См. [Шаг 1](../../../00-course-setup) ниже.

В корне репозитория есть файл `requirements.txt` со всеми необходимыми Python пакетами для запуска примеров.

Установите пакеты, выполнив в терминале команду из корня репозитория:

```bash|powershell
pip install -r requirements.txt
```

Рекомендуется создавать виртуальное окружение Python, чтобы избежать конфликтов.

## Настройка VSCode

Убедитесь, что в VSCode используется нужная версия Python.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка Microsoft Foundry и Azure AI Agent Service

### Шаг 1: Создайте проект Microsoft Foundry

Вам нужен **центр** (hub) и **проект** в Azure AI Foundry с развернутой моделью для запуска ноутбуков.

1. Перейдите на [ai.azure.com](https://ai.azure.com) и войдите в свою учетную запись Azure.
2. Создайте **центр** (или используйте существующий). Подробнее: [Обзор ресурсов хаба](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Внутри хаба создайте **проект**.
4. Разверните модель (например, `gpt-4o`) из раздела **Models + Endpoints** → **Deploy model**.

### Шаг 2: Получите адрес конечной точки проекта и имя развертывания модели

В портале Microsoft Foundry в вашем проекте:

- **Project Endpoint** — перейдите на страницу **Overview** и скопируйте URL конечной точки.

![Project Connection String](../../../translated_images/ru/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — зайдите в **Models + Endpoints**, выберите развернутую модель и запомните имя развертывания (**Deployment name**), например `gpt-4o`.

### Шаг 3: Войдите в Azure с помощью `az login`

Все ноутбуки используют **`AzureCliCredential`** для аутентификации — ключи API не нужны. Вам просто нужно войти через Azure CLI.

1. **Установите Azure CLI**, если еще не сделали это: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Войдите в систему**, выполнив:

    ```bash|powershell
    az login
    ```

    Или, если вы работаете в удаленной среде/Codespace без браузера:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Выберите подписку**, если будет запрос — выберите подписку с вашим проектом Foundry.

4. **Проверьте**, что вы вошли:

    ```bash|powershell
    az account show
    ```

> **Почему `az login`?** Ноутбуки аутентифицируются с помощью `AzureCliCredential` из пакета `azure-identity`. Это значит, что ваша сессия Azure CLI обеспечивает учетные данные — никаких ключей API или секретов в файле `.env`. Это [лучший подход с точки зрения безопасности](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

Откройте `.env` и заполните эти два значения:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Переменная | Где найти |
|------------|-----------|
| `AZURE_AI_PROJECT_ENDPOINT` | Портал Foundry → ваш проект → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Портал Foundry → **Models + Endpoints** → имя в развернутой модели |

Вот и все для большинства уроков! Ноутбуки будут аутентифицироваться автоматически через вашу сессию `az login`.

### Шаг 5: Установите зависимости Python

```bash|powershell
pip install -r requirements.txt
```

Рекомендуется запускать это внутри ранее созданного виртуального окружения.

## Дополнительная настройка для урока 5 (Agentic RAG)

Урок 5 использует **Azure AI Search** для retrieval-augmented generation. Если вы собираетесь запускать этот урок, добавьте в свой `.env` следующие переменные:

| Переменная | Где найти |
|------------|-----------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Портал Azure → ваш ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Портал Azure → ваш ресурс **Azure AI Search** → **Settings** → **Keys** → основной ключ администратора |

## Дополнительная настройка для уроков 6 и 8 (GitHub Models)

Некоторые ноутбуки из уроков 6 и 8 используют **GitHub Models** вместо Azure AI Foundry. Если планируете запускать эти примеры, добавьте в `.env` следующие переменные:

| Переменная | Где найти |
|------------|-----------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Используйте `https://models.inference.ai.azure.com` (значение по умолчанию) |
| `GITHUB_MODEL_ID` | Имя модели для использования (например, `gpt-4o-mini`) |

## Дополнительная настройка для урока 8 (Bing Grounding Workflow)

Условный workflow в уроке 8 использует **Bing grounding** через Azure AI Foundry. Если планируете запускать этот пример, добавьте в `.env` переменную:

| Переменная | Где найти |
|------------|-----------|
| `BING_CONNECTION_ID` | Портал Azure AI Foundry → ваш проект → **Management** → **Connected resources** → ваше соединение Bing → скопируйте ID соединения |

## Решение проблем

### Ошибки проверки SSL-сертификата на macOS

Если вы используете macOS и сталкиваетесь с ошибкой вида:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Это известная проблема с Python на macOS, где системные SSL сертификаты не автоматически доверяются. Попробуйте следующие решения по порядку:

**Вариант 1: Запустите скрипт установки сертификатов Python (рекомендуется)**

```bash
# Замените 3.XX на установленную версию Python (например, 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Вариант 2: Используйте `connection_verify=False` в ноутбуках (только для ноутбуков GitHub Models)**

В ноутбуке урока 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) уже есть закомментированное решение. Раскомментируйте `connection_verify=False` при создании клиента:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Отключите проверку SSL, если возникают ошибки сертификата
)
```

> **⚠️ Внимание:** Отключение проверки SSL (`connection_verify=False`) снижает безопасность, пропуская проверку сертификатов. Используйте это только как временное решение в процессе разработки, никогда не применяйте в продакшене.

**Вариант 3: Установите и используйте `truststore`**

```bash
pip install truststore
```

Затем добавьте следующее в начало вашего ноутбука или скрипта перед сетевыми вызовами:

```python
import truststore
truststore.inject_into_ssl()
```

## Застряли?

Если у вас возникли проблемы с запуском настройки, присоединяйтесь к нашему <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">создайте issue</a>.

## Следующий урок

Теперь вы готовы запускать код этого курса. Желаем успехов в изучении мира AI-агентов!

[Введение в AI-агентов и варианты использования агентов](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с помощью службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует рассматривать как авторитетный источник. Для получения критически важной информации рекомендуется обращаться к профессиональному переводу, выполненному человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->