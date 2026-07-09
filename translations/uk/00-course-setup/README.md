# Налаштування курсу

## Вступ

Цей урок розгляне, як запускати приклади коду цього курсу.

## Приєднуйтесь до інших учнів і отримуйте допомогу

Перед тим, як почати клонувати ваш репозиторій, приєднуйтесь до [каналу AI Agents For Beginners у Discord](https://aka.ms/ai-agents/discord), щоб отримати допомогу з налаштування, будь-які питання щодо курсу або познайомитись з іншими учнями.

## Клонуйте або Форкуйте цей репозиторій

Для початку будь ласка клонувати або форкнути GitHub репозиторій. Це створить вашу власну версію матеріалів курсу, щоб ви могли запускати, тестувати і налаштовувати код!

Це можна зробити, натиснувши на посилання для <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкнути репозиторій</a>

Тепер у вас має бути власна версія цього курсу за посиланням нижче:

![Forked Repo](../../../translated_images/uk/forked-repo.33f27ca1901baa6a.webp)

### Мілкий клон (рекомендується для воркшопів / Codespaces)

  >Повний репозиторій може бути великим (~3 ГБ), якщо завантажувати повну історію та всі файли. Якщо ви відвідуєте лише воркшоп або вам потрібно лише кілька папок з уроками, мілкий клон (або sparse клон) уникає більшості такого завантаження, обрізаючи історію або пропускаючи blobs.

#### Швидкий мілкий клон — мінімальна історія, всі файли

Замініть `<your-username>` в командах нижче на адресу вашого форку (або upstream URL, якщо бажаєте).

Щоб клонувати лише останню історію коммітів (невелике завантаження):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Щоб клонувати конкретну гілку:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частковий (sparse) клон — мінімум blobs + лише обрані папки

Це використовує частковий клон і sparse-checkout (потрібен Git 2.25+ і рекомендується сучасний Git з підтримкою partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Перейдіть у папку репозиторію:

```bash|powershell
cd ai-agents-for-beginners
```

Тоді вкажіть, які папки вам потрібні (приклад нижче показує дві папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Після клонування та перевірки файлів, якщо вам потрібні лише файли і ви хочете звільнити місце (без історії git), видаліть метадані репозиторію (💀 безповоротно — ви втратите всі функції Git: комміти, пулли, пуші, доступ до історії).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Використання GitHub Codespaces (рекомендується, щоб уникнути великих локальних завантажень)

- Створіть новий Codespace для цього репозиторію через [GitHub UI](https://github.com/codespaces).  

- У терміналі новоствореного codespace виконайте одну з команд мілкого/спарс клонування вище, щоб завантажити лише ті папки з уроками, які вам потрібні у робочому просторі Codespace.
- Опціонально: після клонування всередині Codespaces видаліть .git, щоб звільнити додаткове місце (дивіться команди видалення вище).
- Примітка: Якщо ви хочете відкрити репозиторій напряму в Codespaces (без додаткового клонування), майте на увазі, що Codespaces створює середовище devcontainer і може призначити більше ресурсів, ніж вам потрібно. Мілкий клон всередині свіжого Codespace надає кращий контроль за використанням диску.

#### Поради

- Завжди замінюйте URL клонування на ваш форк, якщо збираєтесь редагувати/робити комміти.
- Якщо пізніше потрібна більша історія або файли, ви можете їх отримати або налаштувати sparse-checkout, щоб включити додаткові папки.

## Запуск коду

Цей курс пропонує серію Jupyter Notebook-ів, які ви можете запускати, щоб отримати практичний досвід створення AI агентів.

Приклади коду використовують **Microsoft Agent Framework (MAF)** з `FoundryChatClient`, який підключається до **Microsoft Foundry Agent Service V2** (API Responses) через **Microsoft Foundry**.

Всі Python ноутбуки позначені як `*-python-agent-framework.ipynb`.

## Вимоги

- Python 3.12+
  - **ПРИМІТКА**: Якщо ви не маєте Python3.12, встановіть його. Потім створіть своє віртуальне середовище за допомогою python3.12, щоб переконатися, що встановлені правильні версії з requirements.txt.
  
    >Приклад

    Створіть директорію віртуального середовища Python:

    ```bash|powershell
    python -m venv venv
    ```

    Потім активуйте середовище venv для:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Для прикладів коду на .NET, встановіть [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) або пізнішу версію. Потім перевірте версію встановленого .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — потрібен для автентифікації. Встановіть з [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Підписка Azure** — для доступу до Microsoft Foundry і Microsoft Foundry Agent Service.
- **Проєкт Microsoft Foundry** — проєкт з розгорнутим моделем (наприклад, `gpt-4o`). Дивіться [Крок 1](#крок-1-створіть-проєкт-microsoft-foundry) нижче.

У корені цього репозиторію є файл `requirements.txt`, який містить всі необхідні пакети Python для запуску прикладів коду.

Ви можете встановити їх, виконавши таку команду у вашому терміналі в корені репозиторію:

```bash|powershell
pip install -r requirements.txt
```

Рекомендуємо створити віртуальне середовище Python, щоб уникнути конфліктів і проблем.

## Налаштування VSCode

Переконайтеся, що ви використовуєте правильну версію Python у VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Налаштування Microsoft Foundry і Microsoft Foundry Agent Service

### Крок 1: Створіть проєкт Microsoft Foundry

Вам потрібні Microsoft Foundry **хаб** та **проєкт** з розгорнутою моделлю для запуску ноутбуків.

1. Перейдіть на [ai.azure.com](https://ai.azure.com) і увійдіть у свій обліковий запис Azure.
2. Створіть **хаб** (або використайте існуючий). Дивіться: [Огляд ресурсів хабу](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. У хабі створіть **проєкт**.
4. Розгорніть модель (наприклад, `gpt-4o`) у розділі **Models + Endpoints** → **Deploy model**.

### Крок 2: Отримайте URL кінцевої точки проєкту та ім’я розгортання моделі

З вашого проєкту у порталі Microsoft Foundry:

- **Project Endpoint** — Перейдіть на сторінку **Overview** і скопіюйте URL кінцевої точки.

![Project Connection String](../../../translated_images/uk/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Перейдіть до **Models + Endpoints**, виберіть розгорнуту модель і запишіть її **Deployment name** (наприклад, `gpt-4o`).

### Крок 3: Увійдіть у Azure за допомогою `az login`

Всі ноутбуки використовують **`AzureCliCredential`** для автентифікації — без API ключів для управління. Для цього потрібно увійти через Azure CLI.

1. **Встановіть Azure CLI**, якщо ще не встановлено: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Увійдіть**, виконавши:

    ```bash|powershell
    az login
    ```

    Якщо ви у віддаленому/Codespace середовищі без браузера:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Виберіть підписку**, якщо буде запит — виберіть ту, що містить ваш проєкт Foundry.

4. **Перевірте** вхід у систему:

    ```bash|powershell
    az account show
    ```

> **Чому `az login`?** Ноутбуки автентифікують за допомогою `AzureCliCredential` з пакету `azure-identity`. Це означає, що ваша сесія Azure CLI надає облікові дані — жодних API ключів або секретів у файлі `.env`. Це [рекомендована практика безпеки](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Крок 4: Створіть ваш файл `.env`

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Портал Foundry → ваш проєкт → сторінка **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Портал Foundry → **Models + Endpoints** → ім’я вашої розгорнутої моделі |

На цьому більшість уроків завершуються! Ноутбуки автоматично автентифікуватимуться через вашу сесію `az login`.

### Крок 5: Встановіть залежності Python

```bash|powershell
pip install -r requirements.txt
```

Рекомендуємо запускати це всередині віртуального середовища, яке ви створили раніше.

## Додаткове налаштування для уроку 5 (Agentic RAG)

Урок 5 використовує **Azure AI Search** для генерації з доповненням пошуком. Якщо плануєте запускати цей урок, додайте ці змінні у файл `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Портал Azure → ваш ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Портал Azure → ваш ресурс **Azure AI Search** → **Settings** → **Keys** → основний адміністративний ключ |

## Додаткове налаштування для уроків, які напряму викликають Azure OpenAI (уроки 6 та 8)

Деякі ноутбуки в уроках 6 і 8 викликають **Azure OpenAI** напряму (через **Responses API**) замість використання Microsoft Foundry проєкту. Раніше ці зразки використовували GitHub Models, які застаріли (будуть скасовані у липні 2026) та не підтримують Responses API. Якщо плануєте запускати ці зразки, додайте ці змінні у файл `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Портал Azure → ваш ресурс **Azure OpenAI** → **Keys and Endpoint** → Кінцева точка (наприклад, `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Ім’я вашої розгорнутої моделі (наприклад, `gpt-4o-mini`), що підтримує Responses API |
| `AZURE_OPENAI_API_KEY` | Опційно — лише якщо використовуєте автентифікацію через ключ замість `az login` / Entra ID |

> Responses API використовує стабільну кінцеву точку `/openai/v1/`, тож `api-version` не потрібен. Використовуйте `az login` для безключової автентифікації через Entra ID.

## Альтернативний провайдер: MiniMax (сумісний з OpenAI)

[MiniMax](https://platform.minimaxi.com/) надає моделі з великим контекстом (до 204К токенів) через API сумісний з OpenAI. Оскільки `OpenAIChatClient` з Microsoft Agent Framework працює з будь-якою кінцевою точкою сумісною з OpenAI, ви можете використовувати MiniMax як альтернативу Azure OpenAI або OpenAI.

Додайте ці змінні у файл `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Платформа MiniMax](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Використовуйте `https://api.minimax.io/v1` (значення за замовчуванням) |
| `MINIMAX_MODEL_ID` | Назва моделі для використання (наприклад, `MiniMax-M3`) |

**Приклади моделей**: `MiniMax-M3` (рекомендується), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (швидші відповіді). Назви моделей і їх доступність можуть змінюватися з часом, а доступ до тієї чи іншої моделі може залежати від вашого акаунту чи регіону — перевірте [Платформу MiniMax](https://platform.minimaxi.com/) для актуального списку. Якщо `MiniMax-M3` недоступний для вашого акаунту, встановіть `MINIMAX_MODEL_ID` на модель, до якої у вас є доступ (наприклад, `MiniMax-M2.7`).

Приклади коду, що використовують `OpenAIChatClient` (наприклад, робочий процес бронювання готелю з уроку 14), автоматично виявлять і застосують вашу конфігурацію MiniMax, коли встановлений `MINIMAX_API_KEY`.

## Альтернативний провайдер: Foundry Local (запуск моделей на пристрої)

[Foundry Local](https://foundrylocal.ai) — це легковагове середовище, яке завантажує, керує і обслуговує мовні моделі **повністю на вашому комп’ютері** через API сумісний з OpenAI — без хмари, без підписки Azure і без API ключів. Це чудовий варіант для офлайн-розробки, експериментів без витрат на хмару або збереження даних на пристрої.

Оскільки `OpenAIChatClient` з Microsoft Agent Framework працює з будь-якою OpenAI-сумісною кінцевою точкою, Foundry Local є зручною місцевою альтернативою Azure OpenAI.

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

**3. Встановіть Python SDK** для виявлення локальної кінцевої точки:

```bash
pip install foundry-local-sdk
```

**4. Вкажіть Microsoft Agent Framework використовувати вашу локальну модель:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Завантажує (якщо потрібно) і обслуговує модель локально, потім знаходить кінцеву точку/порт.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # наприклад http://localhost:<порт>/v1
    api_key=manager.api_key,        # завжди "непотрібно" для Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Примітка:** Foundry Local надає OpenAI-сумісну кінцеву точку **Chat Completions**. Використовуйте її для локальної розробки і офлайн-сценаріїв. Для повної функціональності **Responses API** (станові розмови, глибока оркестрація інструментів, розробка в стилі агентів) орієнтуйтесь на **Azure OpenAI** або **Microsoft Foundry** проєкт, як показано в уроках. Див. [документацію Foundry Local](https://foundrylocal.ai) для актуального каталогу моделей і підтримки платформи.

## Додаткове налаштування для уроку 8 (робочий процес із Bing Grounding)


Умовний робочий блокнот у уроці 8 використовує **Bing grounding** через Microsoft Foundry. Якщо ви плануєте запустити цей приклад, додайте цю змінну у ваш файл `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `BING_CONNECTION_ID` | Портал Microsoft Foundry → ваш проект → **Management** → **Connected resources** → ваше підключення Bing → скопіюйте connection ID |

## Вирішення проблем

### Помилки перевірки SSL-сертифікатів на macOS

Якщо ви на macOS і отримуєте помилку на кшталт:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Це відома проблема з Python на macOS, де системні SSL-сертифікати не довіряються автоматично. Спробуйте наступні рішення по черзі:

**Опція 1: Запустіть скрипт Install Certificates Python (рекомендується)**

```bash
# Замініть 3.XX на встановлену версію Python (наприклад, 3.12 або 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Опція 2: Використовуйте `connection_verify=False` у вашому блокноті (тільки для блокнотів GitHub Models)**

У блокноті з уроку 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) вже включено закоментований обхідний шлях. Розкоментуйте `connection_verify=False` під час створення клієнта:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Вимкніть перевірку SSL, якщо ви зіштовхуєтесь із помилками сертифіката
)
```

> **⚠️ Попередження:** Вимкнення перевірки SSL (`connection_verify=False`) знижує безпеку, оминаючи перевірку сертифікатів. Використовуйте це лише як тимчасове рішення в середовищах розробки, ніколи в продуктиві.

**Опція 3: Встановіть та використовуйте `truststore`**

```bash
pip install truststore
```

Потім додайте наступне на початок вашого блокнота або скрипта перед будь-якими мережевими викликами:

```python
import truststore
truststore.inject_into_ssl()
```

## Застрягли десь?

Якщо у вас виникли проблеми з налаштуванням, приєднуйтесь до нашого <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> або <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">створіть заявку</a>.

## Наступний урок

Тепер ви готові запускати код цього курсу. Бажаємо приємного навчання у світі AI-агентів! 

[Вступ до AI-агентів та випадки використання агентів](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->