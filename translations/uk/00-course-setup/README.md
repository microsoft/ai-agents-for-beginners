# Налаштування курсу

## Вступ

У цьому уроці ми розглянемо, як запускати приклади коду цього курсу.

## Приєднуйтеся до інших учнів та отримуйте допомогу

Перед початком клонування вашого репозиторію, приєднайтеся до [Discord-каналу AI Agents For Beginners](https://aka.ms/ai-agents/discord), щоб отримати допомогу з налаштування, відповіді на запитання про курс або зв’язатися з іншими учнями.

## Клонування або форк цього репозиторію

Для початку будь ласка клонувйте або форкніть репозиторій GitHub. Це створить вашу власну версію матеріалів курсу, щоб ви могли запускати, тестувати та змінювати код!

Це можна зробити, натиснувши на посилання <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкнути репозиторій</a>

Зараз ви повинні мати власну форкнуту версію цього курсу за наступним посиланням:

![Forked Repo](../../../translated_images/uk/forked-repo.33f27ca1901baa6a.webp)

### Поверхневе клонування (рекомендується для воркшопу / Codespaces)

  >Повний репозиторій може бути великим (~3 ГБ), якщо ви завантажите всю історію та всі файли. Якщо ви відвідуєте лише воркшоп або потрібні лише декілька папок з уроків, поверхневе клонування (або розріджене клонування) уникає більшості завантажень, скорочуючи історію чи пропускаючи дублі файлів.

#### Швидке поверхневе клонування — мінімальна історія, всі файли

Замініть `<your-username>` у наведених командах на URL вашого форку (або URL оригінального репозиторію, якщо бажаєте).

Щоб клонувати лише останню історію комітів (невелике завантаження):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Щоб клонувати конкретну гілку:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Часткове (розріджене) клонування — мінімум дублікатів + тільки вибрані папки

Це використовує часткове клонування та sparse-checkout (потребує Git 2.25+ і рекомендується сучасний Git з підтримкою часткового клонування):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Перейдіть у папку репозиторію:

```bash|powershell
cd ai-agents-for-beginners
```

Потім вкажіть, які папки вам потрібні (у прикладі нижче показано дві папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Після клонування і перевірки файлів, якщо вам потрібні лише файли і ви хочете звільнити місце (без історії git), будь ласка, видаліть метадані репозиторію (💀 це незворотно — ви втратите всі функції Git: не буде комітів, пулів, пушів чи доступу до історії).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Використання GitHub Codespaces (рекомендується щоб уникнути великих локальних завантажень)

- Створіть новий Codespace для цього репозиторію через [GitHub UI](https://github.com/codespaces).  

- У терміналі новоствореного codespace виконайте одну із команд поверхневого/розрідженого клонування вище, щоб завантажити лише потрібні папки уроків у робочий простір Codespace.
- Опціонально: після клонування всередині Codespaces видаліть .git для звільнення додаткового місця (див. команди видалення вище).
- Примітка: якщо ви віддаєте перевагу відкриттю репозиторію безпосередньо в Codespaces (без додаткового клонування), майте на увазі, що Codespaces створить середовище devcontainer і може все одно надати більше, ніж потрібно. Клонування поверхневої копії в новому Codespace дає вам більший контроль над використанням диска.

#### Поради

- Завжди замінюйте URL клонування на ваш форк, якщо плануєте редагувати/комітити.
- Якщо пізніше знадобиться більше історії або файлів, ви можете отримати їх або налаштувати sparse-checkout, щоб включити додаткові папки.

## Запуск коду

Цей курс пропонує серію Jupyter Notebook, які ви можете запускати, щоб отримати практичний досвід у створенні AI-агентів.

Приклади коду використовують **Microsoft Agent Framework (MAF)** з `FoundryChatClient`, який підключається до **Microsoft Foundry Agent Service V2** (API Responses) через **Microsoft Foundry**.

Всі Python нотатники мають назву `*-python-agent-framework.ipynb`.

## Вимоги

- Python 3.12+
  - **ПРИМІТКА**: Якщо у вас не встановлено Python 3.12, будь ласка, встановіть його. Потім створіть віртуальне оточення, використовуючи python3.12, щоб переконатися, що встановлено правильні версії з requirements.txt.
  
    >Приклад

    Створіть директорію для Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    Потім активуйте venv для:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Для прикладів коду на .NET переконайтеся, що встановили [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) або новішу версію. Потім перевірте версію встановленого .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Потрібен для аутентифікації. Встановіть з [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Підписка Azure** — Для доступу до Microsoft Foundry та Microsoft Foundry Agent Service.
- **Проєкт Microsoft Foundry** — Проєкт з розгорнутим моделем (наприклад, `gpt-5-mini`). Див. [Крок 1](#крок-1-створіть-проєкт-microsoft-foundry) нижче.

У корені цього репозиторію є файл `requirements.txt`, який містить усі необхідні пакети Python для запуску прикладів коду.

Ви можете встановити їх, виконавши цю команду у терміналі в корені репозиторію:

```bash|powershell
pip install -r requirements.txt
```

Рекомендуємо створити віртуальне середовище Python, щоб уникнути конфліктів і проблем.

## Налаштування VSCode

Переконайтеся, що у VSCode використовується правильна версія Python.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Налаштування Microsoft Foundry та Microsoft Foundry Agent Service

### Крок 1: Створіть проєкт Microsoft Foundry

Вам потрібен **хаб** Microsoft Foundry та **проєкт** з розгорнутою моделлю, щоб запускати нотатники.

1. Зайдіть на [ai.azure.com](https://ai.azure.com) і увійдіть у свій обліковий запис Azure.
2. Створіть **хаб** (або використайте існуючий). Деталі: [Огляд ресурсів хабу](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Усередині хабу створіть **проєкт**.
4. Розгорніть модель (наприклад, `gpt-5-mini`) у розділі **Models + Endpoints** → **Deploy model**.

### Крок 2: Отримайте URL кінцевої точки проєкту та ім'я розгортання моделі

Відкрийте свій проєкт у порталі Microsoft Foundry:

- **Project Endpoint** — Перейдіть на сторінку **Overview** та скопіюйте URL кінцевої точки.

![Project Connection String](../../../translated_images/uk/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — У розділі **Models + Endpoints** виберіть розгорнуту модель та зверніть увагу на **Deployment name** (наприклад, `gpt-5-mini`).

### Крок 3: Увійдіть в Azure за допомогою `az login`

Всі нотатники використовують **`AzureCliCredential`** для аутентифікації — ключі API не потрібні. Для цього потрібно увійти через Azure CLI.

1. **Встановіть Azure CLI**, якщо ще не зробили це: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Увійдіть**, виконавши команду:

    ```bash|powershell
    az login
    ```

    А якщо ви у віддаленому середовищі/Codespace без браузера:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Обрати підписку**, якщо буде запит — виберіть ту, що містить ваш проєкт Foundry.

4. **Перевірити**, що ви увійшли:

    ```bash|powershell
    az account show
    ```

> **Чому `az login`?** Нотатники аутентифікуються через `AzureCliCredential` з пакету `azure-identity`. Це означає, що ваша сесія Azure CLI забезпечує облікові дані — немає ключів API чи секретів у файлі `.env`. Це [краща практика безпеки](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Крок 4: Створіть файл `.env`

Скопіюйте приклад файлу:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Відкрийте `.env` і заповніть два цих значення:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Портал Foundry → ваш проєкт → сторінка **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Портал Foundry → **Models + Endpoints** → назва вашої розгорнутої моделі |

Ось і все для більшості уроків! Нотатники автоматично аутентифікуються через вашу сесію `az login`.

### Крок 5: Встановіть залежності Python

```bash|powershell
pip install -r requirements.txt
```

Рекомендуємо запускати це у віртуальному середовищі, яке ви створили раніше.

## Додаткове налаштування для Уроку 5 (Agentic RAG)

Урок 5 використовує **Azure AI Search** для генерації з доповненням за допомогою пошуку. Якщо ви плануєте запускати цей урок, додайте ці змінні до вашого `.env` файлу:

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Портал Azure → ваш ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Портал Azure → ваш ресурс **Azure AI Search** → **Settings** → **Keys** → первинний ключ адміністратора |

## Додаткове налаштування для уроків, які безпосередньо викликають Azure OpenAI (уроки 6 та 8)

Деякі нотатники в уроках 6 і 8 звертаються безпосередньо до **Azure OpenAI** (використовуючи **Responses API**), замість роботи через проєкт Microsoft Foundry. Раніше ці приклади використовували GitHub Models, які є застарілими (будуть вилучені у липні 2026) і не підтримують Responses API. Якщо ви плануєте запускати ці приклади, додайте ці змінні до вашого `.env` файлу:

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Портал Azure → ваш ресурс **Azure OpenAI** → **Keys and Endpoint** → Кінцева точка (наприклад, `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Назва вашої розгорнутої моделі (наприклад, `gpt-5-mini`), що підтримує Responses API |
| `AZURE_OPENAI_API_KEY` | Опційно — лише якщо ви використовуєте аутентифікацію на основі ключа замість `az login` / Entra ID |

> Responses API використовує стабільний endpoint `/openai/v1/`, тому параметр `api-version` не потрібен. Увійдіть з `az login`, щоб використовувати безключову аутентифікацію Entra ID.

## Альтернативний провайдер: MiniMax (Сумісний з OpenAI)

[MiniMax](https://platform.minimaxi.com/) надає моделі з великим контекстом (до 204 тис. токенів) через API сумісний з OpenAI. Оскільки Microsoft Agent Framework `OpenAIChatClient` працює з будь-якою OpenAI-сумісною кінцевою точкою, ви можете використовувати MiniMax як заміну для Azure OpenAI або OpenAI.

Додайте ці змінні до вашого `.env` файлу:

| Змінна | Де знайти |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Платформа MiniMax](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Вкажіть `https://api.minimax.io/v1` (значення за замовчуванням) |
| `MINIMAX_MODEL_ID` | Назва моделі для використання (наприклад, `MiniMax-M3`) |

**Приклад моделей**: `MiniMax-M3` (рекомендовано), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (швидші відповіді). Назви моделей і доступність можуть змінюватися з часом, а також доступ до певної моделі може залежати від вашого облікового запису або регіону — перевіряйте актуальний список на [Платформі MiniMax](https://platform.minimaxi.com/). Якщо `MiniMax-M3` недоступна для вашого облікового запису, встановіть `MINIMAX_MODEL_ID` на модель, до якої ви маєте доступ (наприклад, `MiniMax-M2.7`).

Приклади коду, що використовують `OpenAIChatClient` (наприклад, робочий процес бронювання готелю в уроці 14), автоматично визначатимуть і використовуватимуть вашу конфігурацію MiniMax, якщо задано `MINIMAX_API_KEY`.

## Альтернативний провайдер: Foundry Local (Запуск моделей локально)

[Foundry Local](https://foundrylocal.ai) — це легковагове середовище виконання, яке завантажує, керує і надає мовні моделі **повністю на вашому власному пристрої** через API, сумісний з OpenAI — без хмари, без підписки Azure і без ключів API. Це відмінний варіант для оффлайн-розробки, експериментів без витрат на хмару або зберігання даних локально.

Оскільки Microsoft Agent Framework `OpenAIChatClient` працює з будь-якою OpenAI-сумісною кінцевою точкою, Foundry Local є локальною альтернативою Azure OpenAI.

**1. Встановіть Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Завантажте і запустіть модель** (це також запускає локальний сервіс):

```bash
foundry model list          # дивитися доступні моделі
foundry model run phi-4-mini
```

**3. Встановіть Python SDK**, який використовується для виявлення локальної кінцевої точки:

```bash
pip install foundry-local-sdk
```

**4. Вкажіть Microsoft Agent Framework вашу локальну модель:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Завантажує (за потреби) та обслуговує модель локально, потім виявляє кінцеву точку/порт.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # наприклад http://localhost:<port>/v1
    api_key=manager.api_key,        # завжди "непотрібно" для Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Примітка:** Foundry Local надає OpenAI-сумісну кінцеву точку **Chat Completions**. Використовуйте її для локальної розробки та офлайн-сценаріїв. Для повного набору функцій **Responses API** (станові розмови, глибока оркестрація інструментів та розробка в стилі агента) використовуйте **Azure OpenAI** або проєкт Microsoft Foundry, як показано в уроках. Деталі дивіться в [документації Foundry Local](https://foundrylocal.ai).

## Додаткове налаштування для Уроку 8 (Робочий процес Bing Grounding)


Блокнот умовного робочого процесу у уроці 8 використовує **прив’язку Bing** через Microsoft Foundry. Якщо ви плануєте запустити цей приклад, додайте цю змінну до вашого файлу `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `BING_CONNECTION_ID` | Портал Microsoft Foundry → ваш проект → **Management** → **Connected resources** → ваше підключення Bing → скопіюйте ідентифікатор підключення |

## Усунення несправностей

### Помилки перевірки SSL-сертифікатів на macOS

Якщо ви користуєтесь macOS і отримуєте помилку на кшталт:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Це відома проблема з Python на macOS, коли системні SSL-сертифікати не довіряються автоматично. Спробуйте наступні рішення по черзі:

**Варіант 1: Запустіть скрипт Install Certificates для Python (рекомендується)**

```bash
# Замініть 3.XX на вашу встановлену версію Python (наприклад, 3.12 або 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Варіант 2: Використайте `connection_verify=False` у вашому блокноті (тільки для ноутбуків GitHub Models)**

У блокноті уроку 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) вже є закоментоване тимчасове рішення. Розкоментуйте `connection_verify=False` при створенні клієнта:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Вимкніть перевірку SSL, якщо ви стикаєтеся з помилками сертифіката
)
```

> **⚠️ Увага:** Вимкнення перевірки SSL (`connection_verify=False`) знижує безпеку через пропуск перевірки сертифікатів. Використовуйте це лише як тимчасове рішення в середовищах розробки, ніколи у продакшені.

**Варіант 3: Встановіть і використовуйте `truststore`**

```bash
pip install truststore
```

Потім додайте наступне на початок вашого блокнота або скрипта перед будь-якими мережевими викликами:

```python
import truststore
truststore.inject_into_ssl()
```

## Застрягли десь?

Якщо у вас виникли проблеми з виконанням цього налаштування, приєднуйтесь до нашого <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord-спільноти Azure AI</a> або <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">створіть проблему</a>.

## Наступний урок

Тепер ви готові запускати код для цього курсу. Приємного навчання світу AI-агентів!

[Вступ до AI-агентів та випадків їх використання](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->