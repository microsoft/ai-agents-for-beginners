# Налаштування курсу

## Вступ

У цьому уроці буде розглянуто, як запускати приклади коду з цього курсу.

## Приєднуйтесь до інших учасників і отримуйте допомогу

Перед тим, як розпочати клонування вашого репозиторію, приєднуйтесь до [Discord-каналу AI Agents For Beginners](https://aka.ms/ai-agents/discord), щоб отримати допомогу з налаштування, відповіді на запитання щодо курсу або поспілкуватися з іншими учнями.

## Клонуйте або створіть форк цього репозиторію

Щоб почати, будь ласка, клонувати або створити форк репозиторію на GitHub. Це створить вашу власну версію матеріалів курсу, щоб ви могли запускати, тестувати і змінювати код!

Це можна зробити, натиснувши на посилання для <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">створення форку репозиторію</a>

Тепер у вас має бути власна форк-версія цього курсу за посиланням:

![Forked Repo](../../../translated_images/uk/forked-repo.33f27ca1901baa6a.webp)

### Поверхневе клонування (рекомендовано для воркшопів / Codespaces)

> Повний репозиторій може бути великим (~3 ГБ), якщо завантажувати всю історію та всі файли. Якщо ви відвідуєте лише воркшоп або вам потрібні тільки кілька папок з уроками, поверхневе клонування (або розріджене клонування) завантажує значно менше.

#### Швидке поверхневе клонування — мінімальна історія, всі файли

Замініть `<your-username>` у командах нижче на URL вашого форку (або на URL upstream, якщо бажаєте).

Щоб клонувати лише останню історію комітів (невелике завантаження):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Щоб клонувати конкретну гілку:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Часткове (розріджене) клонування — мінімальні бульбашки + лише вибрані папки

Використовується часткове клонування та sparse-checkout (потрібен Git 2.25+ і рекомендовано сучасний Git з підтримкою часткового клонування):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Перейдіть у папку репозиторію:

```bash
cd ai-agents-for-beginners
```

Потім вкажіть, які папки ви хочете (приклад нижче показує дві папки):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Після клонування та перевірки файлів, якщо вам потрібні лише файли і бажаєте звільнити місце (без історії git), видаліть метадані репозиторію (💀 незворотно — ви втратите всю функціональність Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Використання GitHub Codespaces (рекомендовано, щоб уникнути великих локальних завантажень)

- Створіть новий Codespace для цього репозиторію через [GitHub UI](https://github.com/codespaces).  

- У терміналі нового Codespace запустіть одну з команд поверхневого або розрідженого клонування, щоб завантажити лише потрібні папки уроків у робочий простір Codespace.
- За бажанням: після клонування у Codespaces видаліть .git, щоб звільнити додаткове місце (див. вище команди видалення).
- Примітка: якщо хочете відкрити репозиторій безпосередньо в Codespaces (без додаткового клонування), майте на увазі, що Codespaces створить середовище devcontainer і може надати більше, ніж вам потрібно.

#### Поради

- Завжди замінюйте URL клонування на ваш форк, якщо плануєте редагувати/комітити.
- Якщо пізніше потрібна більша історія або більше файлів, ви можете отримати їх або налаштувати sparse-checkout для додавання папок.

## Запуск коду

Цей курс пропонує серію Jupyter Notebook, які ви можете запускати, щоб отримати практичний досвід у створенні AI агентів.

Приклади коду використовують **Microsoft Agent Framework (MAF)** з `FoundryChatClient`, який підключається до **Microsoft Foundry Agent Service V2** (Responses API) через **Microsoft Foundry**.

Всі ноутбуки на Python мають назву, що закінчується на `*-python-agent-framework.ipynb`.

## Вимоги

- Python 3.12+
  - **ПРИМІТКА**: Якщо у вас не встановлений Python 3.12, встановіть його. Потім створіть віртуальне оточення за допомогою python3.12, щоб переконатися, що з requirements.txt встановляться правильні версії пакетів.
  
    >Приклад

    Створіть директорію Python venv:

    ```bash
    python -m venv venv
    ```

    Потім активуйте віртуальне оточення для:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Для прикладів коду на .NET встановіть [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) або новіший. Потім перевірте вашу версію .NET SDK:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Необхідний для автентифікації. Встановіть з [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Підписка** — Для доступу до Microsoft Foundry і Microsoft Foundry Agent Service.
- **Microsoft Foundry проект** — Проект із розгорнутою моделлю (наприклад, `gpt-5-mini`). Див. [Крок 1](#крок-1-створіть-проект-microsoft-foundry) нижче.

У корені цього репозиторію є файл `requirements.txt` із усіма необхідними Python пакетами для запуску прикладів коду.

Ви можете встановити їх, виконавши наступну команду у терміналі в корені репозиторію:

```bash
pip install -r requirements.txt
```

Рекомендуємо створити віртуальне оточення Python, щоб уникнути конфліктів і проблем.

## Налаштування VSCode

Перевірте, що ви використовуєте правильну версію Python у VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Налаштування Microsoft Foundry та Microsoft Foundry Agent Service

### Крок 1: Створіть проект Microsoft Foundry

Вам потрібен Microsoft Foundry **хаб** та **проект** з розгорнутою моделлю, щоб запускати ноутбуки.

1. Перейдіть на [ai.azure.com](https://ai.azure.com) і увійдіть у свій акаунт Azure.
2. Створіть **хаб** (або використайте існуючий). Див.: [Огляд ресурсів хабу](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. У хабі створіть **проект**.
4. Розгорніть модель (наприклад, `gpt-5-mini`) у розділі **Models + Endpoints** → **Deploy model**.

### Крок 2: Отримайте кінцеву точку проекту і назву розгортання моделі

У вашому проекті в порталі Microsoft Foundry:

- **Endpoint проекту** — Перейдіть на сторінку **Overview** і скопіюйте URL кінцевої точки.

![Project Connection String](../../../translated_images/uk/project-endpoint.8cf04c9975bbfbf1.webp)

- **Назва розгортання моделі** — Перейдіть у **Models + Endpoints**, виберіть вашу розгорнуту модель і зверніть увагу на **Deployment name** (наприклад, `gpt-5-mini`).

### Крок 3: Увійдіть в Azure через `az login`

Більшість ноутбуків автентифікуються через **Azure CLI sign-in** — за допомогою `AzureCliCredential` або `DefaultAzureCredential` (вони використовують сесію `az login`) з пакету `azure-identity` — тому API-ключі не потрібні. Деякі уроки й опційні інтеграції використовують API-ключі; перевірте умови кожного уроку для додаткових змінних оточення. Для цього потрібно увійти через Azure CLI.

1. **Встановіть Azure CLI**, якщо ще не встановлено: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Увійдіть**, виконавши:

    ```bash
    az login
    ```

    Якщо ви у віддаленому середовищі або Codespace без браузера:

    ```bash
    az login --use-device-code
    ```

3. **Обрати підписку**, якщо буде запит — виберіть ту, що містить ваш Foundry проект.

4. **Перевірте**, що ви увійшли:

    ```bash
    az account show
    ```

> **Чому `az login`?** Ноутбуки автентифікуються за допомогою `AzureCliCredential` (або `DefaultAzureCredential`, який теж використовує Azure CLI sign-in) з `azure-identity`. Це означає, що сесія Azure CLI надає облікові дані без API-ключів чи секретів у `.env`. Це [краща практика безпеки](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Крок 4: Створіть файл `.env`

Скопіюйте зразок файлу:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Відкрийте `.env` і заповніть ці два значення:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Портал Foundry → ваш проект → сторінка **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Портал Foundry → **Models + Endpoints** → назва вашої розгорнутої моделі |

Ось і все для більшості уроків! Ноутбуки автоматично автентифікуються через вашу сесію `az login`.

### Крок 5: Встановіть залежності Python

```bash
pip install -r requirements.txt
```

Рекомендуємо запускати це у віртуальному оточенні, яке було створене раніше.

## Опціональне налаштування: Azure AI Search (Уроки 5 і 16)

Уроки 5 (Agentic RAG) і 16 працюють «з коробки» з **пам’яттю в оперативній пам'яті** — без додаткових ресурсів Azure. Якщо хочете підключити реальний індекс **Azure AI Search**, зверніть увагу, що **Урок 16 використовує автентифікацію за ключем**: він переключається з пам’яті в Azure AI Search лише коли **обидва** `AZURE_SEARCH_SERVICE_ENDPOINT` **і** `AZURE_SEARCH_API_KEY` встановлені, інакше працює з пам’яттю — тому для роботи з реальним індексом потрібно вказати ключ адміністратора. Безключова автентифікація через Microsoft Entra ID (RBAC) рекомендована для власного продуктивного коду і відповідає `az login` процесу, що використовується у всьому курсі.

Кроки RBAC нижче застосовуються до прикладів у посібнику налаштування та вашого коду. Вони не активують безключову автентифікацію у Уроці 16, де все ще потрібні і endpoint, і адміністраторський ключ, щоб використовувати Azure AI Search.

1. **Активуйте управління доступом на основі ролей** для вашої служби пошуку:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Призначте собі потрібні ролі** (створювати/завантажувати індекси та виконувати запити):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Додайте endpoint** до вашого `.env` файлу:

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Портал Azure → ваш ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Потрібно (разом із endpoint) для включення Azure AI Search у Уроці 16, який використовує автентифікацію за ключем. Портал Azure → **Settings** → **Keys** → основний адміністраторський ключ |

> **Чому без ключа?** Ключі адміністратора дають повний запис у вашу службу пошуку і можуть просочитись через `.env` файли. З RBAC використовується ваша ідентичність з `az login` — така сама безключова автентифікація Entra ID, що використовується в ноутбуках курсу (через `AzureCliCredential` / `DefaultAzureCredential`). Дивіться [Підключення до Azure AI Search за ролями](https://learn.microsoft.com/azure/search/search-security-rbac).

Дивіться [Посібник налаштування Azure AI Search](./AzureSearch.md) для повних прикладів створення індексів на Python і .NET.

## Додаткове налаштування для уроків із прямим викликом Azure OpenAI (Уроки 6 і 8)

Деякі ноутбуки на уроках 6 та 8 безпосередньо викликають **Azure OpenAI** (через **Responses API**) замість Microsoft Foundry. Раніше ці приклади використовували GitHub Models, які застаріли і не підтримують Responses API. Додайте ці змінні у ваш `.env` файл:

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Портал Azure → ваш ресурс **Azure OpenAI** → **Keys and Endpoint** → Endpoint (наприклад, `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Назва вашої розгорнутої моделі (наприклад, `gpt-5-mini`), що підтримує Responses API |
| `AZURE_OPENAI_API_KEY` | Опціонально — лише якщо використовується автентифікація за ключем замість `az login` / Entra ID |

> Responses API використовує стабільний endpoint `/openai/v1/`, отже `api-version` не потрібен. Увійдіть за допомогою `az login` для безключової автентифікації Entra ID.

## Альтернативний провайдер: MiniMax (сумісний з OpenAI)

[MiniMax](https://platform.minimaxi.com/) надає моделі з довгим контекстом (до 204К токенів) через сумісний з OpenAI API. Оскільки `OpenAIChatClient` Microsoft Agent Framework працює з будь-яким сумісним OpenAI endpoint, ви можете використовувати MiniMax як заміну для уроків, що використовують `OpenAIChatClient`.

Додайте ці змінні у ваш `.env` файл:

| Змінна | Де знайти |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Платформа MiniMax](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Використовуйте `https://api.minimax.io/v1` (значення за замовчуванням) |
| `MINIMAX_MODEL_ID` | Назва моделі для використання (наприклад, `MiniMax-M3`) |

**Приклади моделей**: `MiniMax-M3` (рекомендовано), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (швидші відповіді). Назви моделей і доступність можуть змінюватися з часом, а доступ може залежати від вашого акаунту.

Приклади коду, що використовують `OpenAIChatClient` (наприклад, робочий процес бронювання готелю у Уроці 14) автоматично визначать і використовують вашу конфігурацію MiniMax, якщо встановлено `MINIMAX_API_KEY`.


## Альтернативний постачальник: Novita AI (сумісний з OpenAI)

[Novita AI](https://novita.ai/llm-api) надає API, сумісний з OpenAI, для відкритих та передових великих мовних моделей (DeepSeek, Llama, Qwen і інших). Оскільки `OpenAIChatClient` у Microsoft Agent Framework працює з будь-якою кінцевою точкою, сумісною з OpenAI, ви можете використовувати Novita AI як готову альтернативу Azure OpenAI або OpenAI.

Додайте ці змінні до вашого файлу `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `NOVITA_API_KEY` | [Панель Novita AI](https://novita.ai/settings/key-management) → API Ключі |
| `NOVITA_BASE_URL` | Використовуйте `https://api.novita.ai/openai/v1` (значення за замовчуванням) |
| `NOVITA_MODEL_ID` | Назва моделі для використання (наприклад, `moonshotai/kimi-k3`) |

**Приклад моделей**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI також хостить багато інших родин відкритих моделей (Llama, Qwen, GLM та інші) — дивіться [бібліотеку моделей Novita AI](https://novita.ai/llm-api) для актуального переліку доступних моделей та їх ідентифікаторів.

Поточні зразки коду не автоматично використовують змінні `NOVITA_*`. Щоб скористатися Novita AI, передайте ці значення явно при створенні `OpenAIChatClient` у вашому прикладі.

## Альтернативний постачальник: Foundry Local (запуск моделей на пристрої)

[Foundry Local](https://foundrylocal.ai) — це легкий середовище виконання, яке завантажує, керує і обслуговує мовні моделі **повністю на вашому комп’ютері** через API, сумісний з OpenAI — без хмари.

Оскільки `OpenAIChatClient` Microsoft Agent Framework працює з будь-якою кінцевою точкою, сумісною з OpenAI, Foundry Local є локальною альтернативою Azure OpenAI.

**1. Встановіть Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Завантажте та запустіть модель** (це також запускає локальний сервіс):

```bash
foundry model list          # переглянути доступні моделі
foundry model run phi-4-mini
```

**3. Встановіть Python SDK**, який використовується для виявлення локальної кінцевої точки:

```bash
pip install foundry-local-sdk
```

**4. Вкажіть Microsoft Agent Framework вашій локальній моделі:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Завантажує (за потребою) і запускає модель локально, потім виявляє кінцеву точку/порт.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # наприклад, http://localhost:<port>/v1
    api_key=manager.api_key,        # завжди "необов’язковий" для Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Примітка:** Foundry Local надає OpenAI-сумісну кінцеву точку **Chat Completions**. Використовуйте її для локальної розробки та офлайн-сценаріїв. Для повного набору можливостей **Responses API** (станові розмови і т.д.) використовуйте Azure OpenAI або проєкт Microsoft Foundry.

## Додаткове налаштування для уроку 8 (Bing Grounding Workflow)

Умовний робочий процес у ноутбуці уроку 8 використовує **Bing grounding** через Microsoft Foundry. Якщо ви плануєте запускати цей приклад, додайте цю змінну до вашого файлу `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `BING_CONNECTION_ID` | Портал Microsoft Foundry → ваш проєкт → **Управління** → **Підключені ресурси** → ваше Bing-з’єднання → скопіюйте ідентифікатор з’єднання |

## Усунення несправностей

### Помилки перевірки SSL-сертифіката на macOS

Якщо ви користуєтесь macOS та отримуєте помилку на кшталт:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Це відома проблема з Python на macOS, де системні SSL-сертифікати не довіряються автоматично. Спробуйте наступні рішення по черзі:

**Варіант 1: Запустіть скрипт встановлення сертифікатів Python (рекомендується)**

```bash
# Замініть 3.XX на версію Python, встановлену у вас (наприклад, 3.12 або 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Варіант 2: Використовуйте `connection_verify=False` у вашому ноутбуці (тільки для ноутбуків GitHub Models)**

У ноутбуці Уроку 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) вже включено закоментоване обхідне рішення. Розкоментуйте `connection_verify=False`, якщо виникають помилки сертифікатів:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Вимкніть перевірку SSL, якщо ви стикаєтесь з помилками сертифіката
)
```

> **⚠️ Попередження:** Вимкнення перевірки SSL (`connection_verify=False`) знижує безпеку, оминаючи валідацію сертифіката. Використовуйте це лише як тимчасове рішення у розробницькому середовищі. Ніколи не використовуйте у продакшені.

**Варіант 3: Встановіть і використовуйте `truststore`**

```bash
pip install truststore
```

Потім додайте наступне на початок вашого ноутбука або скрипта перед будь-якими мережевими викликами:

```python
import truststore
truststore.inject_into_ssl()
```

## Застрягли десь?

Якщо у вас виникли труднощі з запуском цього налаштування, приєднуйтесь до нашого <a href="https://discord.gg/kzRShWzttr" target="_blank">спільноти Azure AI у Discord</a> або <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">створіть питання</a>.

## Наступний урок

Ви тепер готові запускати код цього курсу. Успішного вивчення світу AI-агентів!

[Вступ до AI-агентів та сценаріїв їх використання](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->