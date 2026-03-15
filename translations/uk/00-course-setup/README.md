# Налаштування курсу

## Вступ

У цьому уроці буде розглянуто, як запускати приклади коду цього курсу.

## Приєднуйтесь до інших учнів і отримуйте допомогу

Перед тим, як почати клонувати ваше сховище, приєднуйтесь до [Discord-каналу AI Agents For Beginners](https://aka.ms/ai-agents/discord), щоб отримати допомогу з налаштування, поставити запитання про курс або поспілкуватися з іншими учнями.

## Клонувати або форкнути це сховище

Для початку будь ласка клонувати або форкнути репозиторій GitHub. Це створить вашу власну версію матеріалів курсу, щоб ви могли запускати, тестувати та налаштовувати код!

Це можна зробити, натиснувши посилання на <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкнути репозиторій</a>

Тепер у вас має бути власна форкнута версія цього курсу за наступним посиланням:

![Forked Repo](../../../translated_images/uk/forked-repo.33f27ca1901baa6a.webp)

### Поверхневий клон (рекомендовано для воркшопу / Codespaces)

  > Повний репозиторій може бути великим (~3 ГБ), якщо ви завантажуєте всю історію та всі файли. Якщо ви лише відвідуєте воркшоп або вам потрібні лише кілька папок з уроками, поверхневий клон (або розріджений клон) дозволяє уникнути більшості цього завантаження, скорочуючи історію та/або пропускаючи блоби.

#### Швидкий поверхневий клон — мінімальна історія, всі файли

Замініть `<your-username>` в наведених нижче командах на URL вашого форку (або URL upstream, якщо бажаєте).

Щоб клонувати лише останню історію комітів (малий об’єм завантаження):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Щоб клонувати певну гілку:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частковий (розріджений) клон — мінімальні блоби + лише вибрані папки

Це використовує частковий клон і sparse-checkout (потрібен Git 2.25+ та рекомендований сучасний Git із підтримкою часткових клонів):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Перейдіть у папку репозиторію:

```bash|powershell
cd ai-agents-for-beginners
```

Потім вкажіть, які папки ви хочете (приклад нижче показує дві папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Після клонування та перевірки файлів, якщо вам потрібні лише файли і ви хочете звільнити місце (без історії git), будь ласка, видаліть метадані репозиторію (💀безповоротно — ви втратите всю функціональність Git: жодних комітів, пулів, пушів чи доступу до історії).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Використання GitHub Codespaces (рекомендується для уникнення великих локальних завантажень)

- Створіть новий Codespace для цього репозиторію через [GitHub UI](https://github.com/codespaces).  

- У терміналі новоствореного Codespace запустіть одну з команд поверхневого/розрідженого клонування вище, щоб витягти лише папки уроків, які потрібні у робочому просторі Codespace.
- Опціонально: після клонування всередині Codespaces видаліть .git, щоб звільнити додаткове місце (див. команди видалення вище).
- Примітка: Якщо ви хочете відкрити репозиторій безпосередньо в Codespaces (без додаткового клонування), майте на увазі, що Codespaces створить середовище devcontainer і може все одно надати більше, ніж потрібно. Клонування поверхневої копії всередині новоствореного Codespace дає більше контролю над використанням диску.

#### Поради

- Завжди замінюйте URL клонування на ваш форк, якщо плануєте редагувати/комітити.
- Якщо пізніше потрібна більша історія чи файли, можна їх завантажити або налаштувати sparse-checkout для включення додаткових папок.

## Запуск коду

Цей курс містить серію Jupyter Notebook-ів, які ви можете запускати, щоб отримати практичний досвід створення AI агентів.

Приклади коду використовують **Microsoft Agent Framework (MAF)** з `AzureAIProjectAgentProvider`, який підключається до **Azure AI Agent Service V2** (API відповідей) через **Microsoft Foundry**.

Всі Python ноутбуки позначені `*-python-agent-framework.ipynb`.

## Вимоги

- Python 3.12+
  - **ПРИМІТКА**: Якщо у вас не встановлено Python 3.12, обов’язково встановіть його. Потім створіть віртуальне середовище, використовуючи python3.12, щоб забезпечити встановлення правильних версій пакунків згідно з файлом requirements.txt.
  
    >Приклад

    Створення папки для Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    Потім активуйте віртуальне середовище для:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Для прикладів коду, які використовують .NET, встановіть [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) або новішу версію. Потім перевірте версію встановленого SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — необхідний для автентифікації. Встановіть з [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Підписка Azure** — для доступу до Microsoft Foundry та Azure AI Agent Service.
- **Проєкт Microsoft Foundry** — Проєкт із розгорнутою моделлю (наприклад, `gpt-4o`). Див. [Крок 1](../../../00-course-setup) нижче.

Ми включили файл `requirements.txt` у корінь цього репозиторію, в якому містяться всі необхідні пакунки Python для запуску прикладів коду.

Ви можете встановити їх, запустивши наступну команду в терміналі у корені репозиторію:

```bash|powershell
pip install -r requirements.txt
```

Рекомендуємо створити віртуальне середовище Python, щоб уникнути конфліктів і проблем.

## Налаштування VSCode

Переконайтеся, що у VSCode використовується правильна версія Python.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Налаштування Microsoft Foundry та Azure AI Agent Service

### Крок 1: Створіть проєкт Microsoft Foundry

Для запуску ноутбуків вам потрібен Azure AI Foundry **hub** і **проект** із розгорнутою моделлю.

1. Перейдіть на [ai.azure.com](https://ai.azure.com) і увійдіть у свій обліковий запис Azure.
2. Створіть **hub** (або використайте існуючий). Див.: [Огляд ресурсів Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Усередині hub створіть **проект**.
4. Розгорніть модель (наприклад, `gpt-4o`) через **Models + Endpoints** → **Deploy model**.

### Крок 2: Отримайте URL кінцевої точки проєкту і ім’я розгортання моделі

У порталі Microsoft Foundry:

- **Project Endpoint** — Перейдіть на сторінку **Overview** і скопіюйте URL кінцевої точки.

![Project Connection String](../../../translated_images/uk/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Перейдіть до **Models + Endpoints**, виберіть розгорнуту модель і зауважте **Deployment name** (наприклад, `gpt-4o`).

### Крок 3: Увійдіть в Azure через `az login`

Всі ноутбуки використовують **`AzureCliCredential`** для автентифікації — вам не потрібно керувати API ключами. Для цього ви маєте увійти через CLI Azure.

1. **Встановіть Azure CLI**, якщо ще не встановлено: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Увійдіть**, виконавши:

    ```bash|powershell
    az login
    ```

    Або, якщо ви в середовищі remote/Codespace без браузера:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Виберіть свою підписку**, якщо буде запит — оберіть ту, що містить ваш проєкт Foundry.

4. **Перевірте**, що ви увійшли:

    ```bash|powershell
    az account show
    ```

> **Чому `az login`?** Ноутбуки автентифікуються через `AzureCliCredential` з пакету `azure-identity`. Це означає, що ваш сеанс Azure CLI надає облікові дані — ніяких API ключів чи секретів у файлі `.env`. Це [краща практика безпеки](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Крок 4: Створіть ваш файл `.env`

Скопіюйте файл прикладу:

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

Ось і все для більшості уроків! Ноутбуки автентифікуються автоматично через вашу сесію `az login`.

### Крок 5: Встановіть Python залежності

```bash|powershell
pip install -r requirements.txt
```

Рекомендуємо запускати це у віртуальному середовищі, створеному раніше.

## Додаткове налаштування для Уроку 5 (Agentic RAG)

Урок 5 використовує **Azure AI Search** для генерації з підкріпленням за допомогою пошуку. Якщо плануєте запускати цей урок, додайте ці змінні у файл `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Портал Azure → ваш ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Портал Azure → ваш ресурс **Azure AI Search** → **Settings** → **Keys** → основний адміністраторський ключ |

## Додаткове налаштування для Уроків 6 і 8 (GitHub Models)

Деякі ноутбуки у уроках 6 і 8 використовують **GitHub Models** замість Azure AI Foundry. Якщо плануєте запускати ці зразки, додайте ці змінні у файл `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Використовуйте `https://models.inference.ai.azure.com` (значення за замовчуванням) |
| `GITHUB_MODEL_ID` | Ім’я моделі для використання (наприклад, `gpt-4o-mini`) |

## Додаткове налаштування для Уроку 8 (Bing Grounding Workflow)

У ноутбуці умовного робочого процесу в уроці 8 використовується **Bing grounding** через Azure AI Foundry. Якщо плануєте запускати цей зразок, додайте цю змінну у файл `.env`:

| Змінна | Де знайти |
|----------|-----------------|
| `BING_CONNECTION_ID` | Портал Azure AI Foundry → ваш проєкт → **Management** → **Connected resources** → підключення Bing → скопіюйте ID підключення |

## Вирішення проблем

### Помилки перевірки SSL сертифікатів на macOS

Якщо ви користуєтеся macOS і виникає помилка:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Це відома проблема Python на macOS, коли системні SSL сертифікати не довіряються автоматично. Спробуйте ці рішення в порядку:

**Опція 1: Запустіть скрипт встановлення сертифікатів Python (рекомендовано)**

```bash
# Замініть 3.XX на вашу встановлену версію Python (наприклад, 3.12 або 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Опція 2: Використовуйте `connection_verify=False` у вашому ноутбуці (тільки для ноутбуків GitHub Models)**

В ноутбуці уроку 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) вже є закоментоване рішення. Розкоментуйте `connection_verify=False` при створенні клієнта:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Вимкніть перевірку SSL, якщо ви стикаєтесь із помилками сертифікатів
)
```

> **⚠️ Попередження:** Вимкнення перевірки SSL (`connection_verify=False`) знижує безпеку, оминаючи перевірку сертифікатів. Використовуйте це лише тимчасово в середовищах розробки, ніколи у продуктиві.

**Опція 3: Встановіть і використовуйте `truststore`**

```bash
pip install truststore
```

Потім додайте наступне на початок вашого ноутбука або скрипта перед будь-якими мережевими викликами:

```python
import truststore
truststore.inject_into_ssl()
```

## Застрягли десь?

Якщо у вас виникли труднощі з запуском цього налаштування, приєднуйтесь до нашого <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> або <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">створіть issue</a>.

## Наступний урок

Тепер ви готові запускати код цього курсу. Бажаємо успіхів у вивченні світу AI Аґентів!

[Вступ до AI Агентів та Випадків Використання Агентів](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу штучного інтелекту [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, зверніть увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що можуть виникнути внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->