# Налаштування Курсу

## Вступ

У цьому уроці буде розглянуто, як запускати приклади коду цього курсу.

## Приєднуйтесь до інших учнів та отримуйте допомогу

Перед тим, як почати клонувати своє сховище, приєднуйтесь до [Discord-каналу AI Agents For Beginners](https://aka.ms/ai-agents/discord), щоб отримати допомогу з налаштування, задати питання щодо курсу або зв’язатися з іншими учнями.

## Клонувати або Форкнути це Сховище

Щоб почати, будь ласка, клонувати або форкнути репозиторій GitHub. Це створить вашу власну версію матеріалів курсу, щоб ви могли запускати, тестувати та налаштовувати код!

Це можна зробити, натиснувши на посилання <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкнути репозиторій</a>

Тепер у вас має бути ваша власна форкнута версія цього курсу за посиланням:

![Forked Repo](../../../translated_images/uk/forked-repo.33f27ca1901baa6a.webp)

### Мілкий клон (рекомендовано для воркшопів / Codespaces)

  >Повне сховище може бути великим (~3 ГБ) при завантаженні повної історії та всіх файлів. Якщо ви лише відвідуєте воркшоп або потрібні лише кілька папок з уроками, мілкий клон (або розріджений клон) уникає більшої частини цього завантаження шляхом скорочення історії та/або пропуску об’єктів (blobs).

#### Швидкий мілкий клон — мінімальна історія, усі файли

Змініть `<your-username>` у наведених нижче командах на URL вашого форка (або на URL upstream, якщо бажаєте).

Щоб клонувати лише останню історію комітів (малий обсяг завантаження):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Щоб клонувати конкретну гілку:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частковий (розріджений) клон — мінімум об’єктів + лише вибрані папки

Це використовує частковий клон і sparse-checkout (потрібен Git 2.25+ і рекомендовано сучасний Git з підтримкою часткового клонування):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Перейдіть у папку репозиторію:

```bash|powershell
cd ai-agents-for-beginners
```

Потім вкажіть, які папки вам потрібні (приклад нижче показує дві папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Після клонування та перевірки файлів, якщо вам потрібні лише файли і ви хочете звільнити місце (без історії git), видаліть метадані репозиторію (💀безповоротно — ви втратите всю функціональність Git: не буде комітів, pull, push або доступу до історії).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Використання GitHub Codespaces (рекомендовано для уникнення великих локальних завантажень)

- Створіть новий Codespace для цього репозиторію через [GitHub UI](https://github.com/codespaces).  

- У терміналі створеного Codespace запустіть одну з команд мілкого/розрідженого клонування, щоб завантажити лише потрібні вам папки з уроків у робоче середовище Codespace.
- Опціонально: після клонування в Codespaces видаліть .git, щоб звільнити додаткове місце (див. команди видалення вище).
- Примітка: якщо ви віддаєте перевагу відкривати репозиторій напряму в Codespaces (без додаткового клонування), майте на увазі, що Codespaces створить середовище devcontainer і може все одно завантажити більше, ніж потрібно. Мілкий клон всередині свіжого Codespace дає більший контроль над використанням диску.

#### Поради

- Завжди замінюйте URL клонування на ваш форк, якщо збираєтесь редагувати/комітити.
- Якщо згодом вам знадобиться більше історії або файлів, ви можете їх отримати або налаштувати sparse-checkout для додавання додаткових папок.

## Запуск Коду

Цей курс пропонує серію Jupyter нотатників, які ви можете запускати, щоб отримати практичний досвід з побудови AI-агентів.

Приклади коду використовують **Microsoft Agent Framework (MAF)** з `FoundryChatClient`, який підключається до **Microsoft Foundry Agent Service V2** (API відповідей) через **Microsoft Foundry**.

Усі Python-нотатники позначені як `*-python-agent-framework.ipynb`.

## Вимоги

- Python 3.12+
  - **ПРИМІТКА**: Якщо у вас не встановлено Python3.12, переконайтеся, що встановили його. Потім створіть ваше віртуальне середовище з python3.12, щоб забезпечити правильні версії з файлу requirements.txt.
  
    >Приклад

    Створення директорії Python venv:

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

- .NET 10+: Для прикладів коду на .NET переконайтеся, що встановлено [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) або новішу версію. Потім перевірте вашу версію встановленого .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — потрібен для аутентифікації. Встановіть з [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Підписка Azure** — для доступу до Microsoft Foundry і Microsoft Foundry Agent Service.
- **Проєкт Microsoft Foundry** — проєкт з розгорнутою моделлю (наприклад, `gpt-4.1-mini`). Див. [Крок 1](#крок-1-створіть-проект-microsoft-foundry) нижче.

У корені цього репозиторію міститься файл `requirements.txt` з усіма необхідними Python пакетами для запуску прикладів коду.

Ви можете встановити їх, виконавши наступну команду у вашому терміналі в корені репозиторію:

```bash|powershell
pip install -r requirements.txt
```

Рекомендуємо створити віртуальне середовище Python, щоб уникнути конфліктів та проблем.

## Налаштування VSCode

Переконайтесь, що в VSCode ви використовуєте правильну версію Python.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Налаштування Microsoft Foundry та Microsoft Foundry Agent Service

### Крок 1: Створіть проект Microsoft Foundry

Вам потрібен **hub** та **проєкт** Microsoft Foundry із розгорнутою моделлю для запуску нотатників.

1. Перейдіть на [ai.azure.com](https://ai.azure.com) та увійдіть в свій Azure-акаунт.
2. Створіть **hub** (або використайте існуючий). Див.: [Огляд ресурсів hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Усередині hub створіть **проєкт**.
4. Розгорніть модель (наприклад, `gpt-4.1-mini`) через **Models + Endpoints** → **Deploy model**.

### Крок 2: Отримайте Endpoint проєкту та назву розгортання моделі

У вашому проєкті в порталі Microsoft Foundry:

- **Endpoint проєкту** — Перейдіть на сторінку **Overview** і скопіюйте URL endpoint-а.

![Project Connection String](../../../translated_images/uk/project-endpoint.8cf04c9975bbfbf1.webp)

- **Назва розгортання моделі** — Перейдіть у **Models + Endpoints**, виберіть вашу розгорнуту модель та запишіть **Deployment name** (наприклад, `gpt-4.1-mini`).

### Крок 3: Увійдіть в Azure за допомогою `az login`

Всі нотатники використовують **`AzureCliCredential`** для аутентифікації — без ключів API для керування. Для цього потрібно увійти через Azure CLI.

1. **Встановіть Azure CLI**, якщо ще не зробили це: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Ввійдіть**, виконавши:

    ```bash|powershell
    az login
    ```

    Якщо ви в середовищі remote/Codespace без браузера:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Виберіть вашу підписку**, якщо з’явиться запит — оберіть ту, що містить ваш проєкт Foundry.

4. **Перевірте**, що ви увійшли:

    ```bash|powershell
    az account show
    ```

> **Чому `az login`?** Для аутентифікації нотатники використовують `AzureCliCredential` із пакету `azure-identity`. Це означає, що сесія Azure CLI надає облікові дані — немає ключів API або секретів у вашому `.env` файлі. Це [краща практика безпеки](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

Відкрийте `.env` і заповніть ці два значення:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Портал Foundry → ваш проєкт → сторінка **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Портал Foundry → **Models + Endpoints** → назва вашої розгорнутої моделі |

Це все для більшості уроків! Нотатники автоматично аутентифікуються через вашу сесію `az login`.

### Крок 5: Встановіть залежності Python

```bash|powershell
pip install -r requirements.txt
```

Рекомендуємо запускати це всередині створеного вами віртуального середовища.

## Додаткове налаштування для уроку 5 (Agentic RAG)

Урок 5 використовує **Azure AI Search** для генерування з підсиленням за допомогою пошуку. Якщо плануєте запускати цей урок, додайте ці змінні у файл `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Портал Azure → ваш ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Портал Azure → ваш ресурс **Azure AI Search** → **Settings** → **Keys** → основний адміністраторський ключ |

## Додаткове налаштування для уроків, що використовують Azure OpenAI напряму (уроки 6 та 8)

Деякі нотатники у уроках 6 і 8 викликають **Azure OpenAI** напряму (використовуючи **Responses API**) замість Microsoft Foundry проєкту. Ці приклади раніше використовували GitHub Models, які застаріли (зупинка у липні 2026) і не підтримують Responses API. Якщо плануєте запускати ці приклади, додайте ці змінні у файл `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Портал Azure → ваш ресурс **Azure OpenAI** → **Keys and Endpoint** → Endpoint (наприклад, `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Назва вашої розгорнутої моделі (наприклад, `gpt-4.1-mini`), що підтримує Responses API |
| `AZURE_OPENAI_API_KEY` | Опційно — лише якщо ви використовуєте автентифікацію на основі ключа замість `az login` / Entra ID |

> Responses API використовує стабільний endpoint `/openai/v1/`, тому параметр `api-version` не потрібен. Використовуйте `az login` для безключової автентифікації через Entra ID.

## Альтернативний провайдер: MiniMax (сумісний з OpenAI)

[MiniMax](https://platform.minimaxi.com/) надає моделі з великим контекстом (до 204К токенів) через API сумісне з OpenAI. Оскільки `OpenAIChatClient` Microsoft Agent Framework працює з будь-яким сумісним OpenAI endpoint, ви можете використовувати MiniMax як заміну Azure OpenAI або OpenAI.

Додайте ці змінні у ваш файл `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Платформа MiniMax](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Використовуйте `https://api.minimax.io/v1` (значення за замовчуванням) |
| `MINIMAX_MODEL_ID` | Назва моделі для використання (наприклад, `MiniMax-M3`) |

**Приклади моделей**: `MiniMax-M3` (рекомендовано), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (швидші відповіді). Назви моделей і доступність можуть змінюватись з часом, а доступ до певної моделі може залежати від вашого акаунта або регіону — дивіться [Платформу MiniMax](https://platform.minimaxi.com/) для поточного списку. Якщо `MiniMax-M3` недоступна для вашого акаунта, встановіть `MINIMAX_MODEL_ID` на модель, до якої маєте доступ (наприклад, `MiniMax-M2.7`).

Приклади коду, що використовують `OpenAIChatClient` (наприклад, робочий процес бронювання готелю в уроці 14), автоматично виявлятимуть і використовуватимуть вашу конфігурацію MiniMax, коли встановлено `MINIMAX_API_KEY`.

## Альтернативний провайдер: Foundry Local (Запуск моделей на пристрої)

[Foundry Local](https://foundrylocal.ai) — це легковага середовище виконання, яка завантажує, керує та обслуговує мовні моделі **повністю на вашому комп’ютері** через сумісний з OpenAI API — без хмари, без підписки Azure і без ключів API. Це чудовий варіант для офлайн-розробки, експериментів без витрат на хмару або збереження даних на пристрої.

Оскільки `OpenAIChatClient` Microsoft Agent Framework працює з будь-яким сумісним OpenAI endpoint, Foundry Local є локальною заміною Azure OpenAI.

**1. Встановіть Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Завантажте і запустіть модель** (це також запускає локальний сервіс):

```bash
foundry model list          # переглянути доступні моделі
foundry model run phi-4-mini
```

**3. Встановіть Python SDK**, який використовується для виявлення локального endpoint:

```bash
pip install foundry-local-sdk
```

**4. Вкажіть Microsoft Agent Framework вашій локальній моделі:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Завантажує (за потребою) та обслуговує модель локально, потім визначає кінцеву точку/порт.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # наприклад, http://localhost:<port>/v1
    api_key=manager.api_key,        # завжди "непотрібно" для Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Примітка:** Foundry Local надає сумісний з OpenAI endpoint для **Chat Completions**. Використовуйте його для локальної розробки та офлайн-сценаріїв. Для повного набору функцій **Responses API** (станові розмови, глибока оркестрація інструментів і агентське програмування) націлюйтеся на **Azure OpenAI** або проєкт **Microsoft Foundry**, як показано в уроках. Див. [документацію Foundry Local](https://foundrylocal.ai) для поточного каталогу моделей і підтримки платформи.


## Додаткове налаштування для уроку 8 (Bing Grounding Workflow)

У нотатнику умовного робочого процесу в уроці 8 використовується **Bing grounding** через Microsoft Foundry. Якщо ви плануєте запускати цей приклад, додайте цю змінну до вашого файлу `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `BING_CONNECTION_ID` | Портал Microsoft Foundry → ваш проект → **Управління** → **Підключені ресурси** → ваше Bing-з'єднання → скопіюйте ID з'єднання |

## Усунення неполадок

### Помилки перевірки SSL-сертифіката на macOS

Якщо ви використовуєте macOS і бачите помилку типу:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Це відома проблема з Python на macOS, коли системні SSL-сертифікати не довіряються автоматично. Спробуйте такі рішення у порядку:

**Варіант 1: Запустіть скрипт встановлення сертифікатів Python (рекомендується)**

```bash
# Замініть 3.XX на вашу встановлену версію Python (наприклад, 3.12 або 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Варіант 2: Використовуйте `connection_verify=False` у вашому нотатнику (тільки для нотатників GitHub Models)**

У нотатнику уроку 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) вже включено закоментоване обходження. Розкоментуйте `connection_verify=False` при створенні клієнта:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Вимкніть перевірку SSL, якщо ви стикаєтеся з помилками сертифіката
)
```

> **⚠️ Увага:** Вимкнення перевірки SSL-сертифіката (`connection_verify=False`) знижує безпеку, оминаючи валідацію сертифікату. Використовуйте це лише як тимчасове рішення в середовищах розробки, ніколи в продакшені.

**Варіант 3: Встановіть і використовуйте `truststore`**

```bash
pip install truststore
```

Потім додайте наступне на початок вашого нотатника або скрипта перед виконанням будь-яких мережевих викликів:

```python
import truststore
truststore.inject_into_ssl()
```

## Зациклитись десь?

Якщо у вас виникли проблеми з налаштуванням, заходьте до нашого <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> або <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">створіть проблему</a>.

## Наступний урок

Тепер ви готові запускати код цього курсу. Успішного вивчення світу AI агентів! 

[Вступ до AI агентів та випадків використання агентів](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->