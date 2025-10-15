<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:58:07+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "uk"
}
-->
# Налаштування курсу

## Вступ

У цьому уроці ми розглянемо, як запускати зразки коду цього курсу.

## Приєднуйтесь до інших учасників та отримуйте допомогу

Перш ніж почати клонувати ваш репозиторій, приєднайтеся до [каналу Discord для початківців AI Agents](https://aka.ms/ai-agents/discord), щоб отримати допомогу з налаштуванням, відповіді на запитання щодо курсу або зв'язатися з іншими учасниками.

## Клонування або форк репозиторію

Для початку, будь ласка, клонуйте або зробіть форк репозиторію GitHub. Це дозволить створити вашу власну версію матеріалів курсу, щоб ви могли запускати, тестувати та змінювати код!

Це можна зробити, натиснувши на посилання <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форк репозиторію</a>.

Тепер у вас має бути власна форкована версія цього курсу за наступним посиланням:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.uk.png)

### Поверхневе клонування (рекомендується для воркшопів / Codespaces)

  >Повний репозиторій може бути великим (~3 ГБ), якщо ви завантажуєте всю історію та всі файли. Якщо ви лише берете участь у воркшопі або вам потрібні лише кілька папок уроків, поверхневе клонування (або вибіркове клонування) дозволяє уникнути більшої частини цього завантаження, скоротивши історію та/або пропустивши великі файли.

#### Швидке поверхневе клонування — мінімальна історія, всі файли

Замініть `<your-username>` у наведених нижче командах на URL вашого форку (або URL оригінального репозиторію, якщо ви віддаєте перевагу).

Щоб клонувати лише останню історію комітів (невелике завантаження):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Щоб клонувати конкретну гілку:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Часткове (вибіркове) клонування — мінімальні файли + лише вибрані папки

Це використовує часткове клонування та вибіркове завантаження (вимагає Git 2.25+ і рекомендованої сучасної версії Git з підтримкою часткового клонування):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Перейдіть до папки репозиторію:

Для bash:

```bash
cd ai-agents-for-beginners
```

Для Powershell:

```powershell
Set-Location ai-agents-for-beginners
```

Потім вкажіть, які папки вам потрібні (приклад нижче показує дві папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Після клонування та перевірки файлів, якщо вам потрібні лише файли і ви хочете звільнити місце (без історії git), будь ласка, видаліть метадані репозиторію (💀необоротно — ви втратите всі функції Git: коміти, завантаження, відправлення або доступ до історії).

Для Linux/macOS:

```bash
rm -rf .git
```

Для Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### Використання GitHub Codespaces (рекомендується для уникнення великих локальних завантажень)

- Створіть новий Codespace для цього репозиторію через [інтерфейс GitHub](https://github.com/codespaces).  

- У терміналі новоствореного Codespace виконайте одну з команд поверхневого/вибіркового клонування, щоб завантажити лише потрібні папки уроків у робочий простір Codespace.
- Опціонально: після клонування в Codespaces видаліть .git, щоб звільнити додаткове місце (див. команди видалення вище).
- Примітка: якщо ви віддаєте перевагу відкриттю репозиторію безпосередньо в Codespaces (без додаткового клонування), майте на увазі, що Codespaces створить середовище devcontainer і може все ще завантажити більше, ніж вам потрібно. Клонування поверхневої копії у свіжому Codespace дає вам більше контролю над використанням дискового простору.

#### Поради

- Завжди замінюйте URL клонування на ваш форк, якщо ви хочете редагувати/комітити.
- Якщо вам пізніше знадобиться більше історії або файлів, ви можете їх завантажити або налаштувати вибіркове завантаження для включення додаткових папок.

## Запуск коду

Цей курс пропонує серію Jupyter Notebooks, які ви можете запускати, щоб отримати практичний досвід створення AI Agents.

Зразки коду використовують:

**Потрібен обліковий запис GitHub - безкоштовно**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Позначено як (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Позначено як (autogen.ipynb)

**Потрібна підписка Azure**:
3) Azure AI Foundry + Azure AI Agent Service. Позначено як (azureaiagent.ipynb)

Ми рекомендуємо вам спробувати всі три типи прикладів, щоб побачити, який з них найкраще підходить для вас.

Який би варіант ви не обрали, це визначить, які кроки налаштування вам потрібно виконати нижче:

## Вимоги

- Python 3.12+
  - **NOTE**: Якщо у вас не встановлений Python 3.12, переконайтеся, що ви його встановили. Потім створіть ваш venv, використовуючи python3.12, щоб забезпечити встановлення правильних версій з файлу requirements.txt.
  
    >Приклад

    Створіть каталог Python venv:

    ``` bash
    python3 -m venv venv
    ```

    Потім активуйте середовище venv для:

    macOS та Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- Обліковий запис GitHub - для доступу до GitHub Models Marketplace
- Підписка Azure - для доступу до Azure AI Foundry
- Обліковий запис Azure AI Foundry - для доступу до Azure AI Agent Service

Ми включили файл `requirements.txt` у кореневу папку цього репозиторію, який містить усі необхідні пакети Python для запуску зразків коду.

Ви можете встановити їх, виконавши наступну команду у вашому терміналі в кореневій папці репозиторію:

```bash
pip install -r requirements.txt
```

Ми рекомендуємо створити віртуальне середовище Python, щоб уникнути будь-яких конфліктів та проблем.

## Налаштування VSCode
Переконайтеся, що ви використовуєте правильну версію Python у VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Налаштування для зразків з використанням GitHub Models 

### Крок 1: Отримайте ваш персональний токен доступу GitHub (PAT)

Цей курс використовує GitHub Models Marketplace, який надає безкоштовний доступ до великих мовних моделей (LLMs), які ви будете використовувати для створення AI Agents.

Щоб використовувати GitHub Models, вам потрібно створити [персональний токен доступу GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Це можна зробити, перейшовши до <a href="https://github.com/settings/personal-access-tokens" target="_blank">налаштувань персональних токенів доступу</a> у вашому обліковому записі GitHub.

Будь ласка, дотримуйтесь [Принципу найменших привілеїв](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) при створенні вашого токена. Це означає, що ви повинні надати токену лише ті дозволи, які необхідні для запуску зразків коду цього курсу.

1. Виберіть опцію `Fine-grained tokens` на лівій стороні екрана, перейшовши до **Developer settings**.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.uk.png)

    Потім виберіть `Generate new token`.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.uk.png)

2. Введіть описову назву для вашого токена, яка відображає його призначення, щоб його було легко ідентифікувати пізніше.

    🔐 Рекомендація щодо тривалості токена

    Рекомендована тривалість: 30 днів
    Для більшої безпеки ви можете вибрати коротший період — наприклад, 7 днів 🛡️
    Це чудовий спосіб встановити особисту мету та завершити курс, поки ваша мотивація висока 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.uk.png)

3. Обмежте область дії токена вашим форком цього репозиторію.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.uk.png)

4. Обмежте дозволи токена: У розділі **Permissions** натисніть вкладку **Account**, а потім кнопку "+ Add permissions". З'явиться випадаюче меню. Будь ласка, знайдіть **Models** і поставте галочку біля нього.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.uk.png)

5. Перевірте необхідні дозволи перед створенням токена. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.uk.png)

6. Перед створенням токена переконайтеся, що ви готові зберегти токен у безпечному місці, наприклад, у сховищі паролів, оскільки він більше не буде показаний після створення. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.uk.png)

Скопіюйте ваш новий токен, який ви щойно створили. Тепер ви додасте його до вашого `.env` файлу, включеного в цей курс.

### Крок 2: Створіть ваш `.env` файл

Щоб створити ваш `.env` файл, виконайте наступну команду у вашому терміналі.

```bash
cp .env.example .env
```

Це скопіює приклад файлу та створить `.env` у вашій директорії, де ви заповните значення для змінних середовища.

Скопіювавши ваш токен, відкрийте файл `.env` у вашому улюбленому текстовому редакторі та вставте ваш токен у поле `GITHUB_TOKEN`.
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.uk.png)

Тепер ви повинні бути готові до запуску зразків коду цього курсу.

## Налаштування для зразків з використанням Azure AI Foundry та Azure AI Agent Service

### Крок 1: Отримайте кінцеву точку вашого проекту Azure

Виконайте кроки для створення хаба та проекту в Azure AI Foundry, описані тут: [Огляд ресурсів хаба](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources).

Після створення проекту вам потрібно буде отримати рядок підключення для вашого проекту.

Це можна зробити, перейшовши на сторінку **Overview** вашого проекту в порталі Azure AI Foundry.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.uk.png)

### Крок 2: Створіть ваш `.env` файл

Щоб створити ваш `.env` файл, виконайте наступну команду у вашому терміналі.

```bash
cp .env.example .env
```

Це скопіює приклад файлу та створить `.env` у вашій директорії, де ви заповните значення для змінних середовища.

Скопіювавши ваш токен, відкрийте файл `.env` у вашому улюбленому текстовому редакторі та вставте ваш токен у поле `PROJECT_ENDPOINT`.

### Крок 3: Увійдіть до Azure

Як найкращу практику безпеки, ми будемо використовувати [автентифікацію без ключів](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) для автентифікації в Azure OpenAI за допомогою Microsoft Entra ID. 

Далі відкрийте термінал і виконайте команду `az login --use-device-code`, щоб увійти до вашого облікового запису Azure.

Після входу виберіть вашу підписку в терміналі.

## Додаткові змінні середовища - Azure Search та Azure OpenAI 

Для уроку Agentic RAG - Урок 5 - є зразки, які використовують Azure Search та Azure OpenAI.

Якщо ви хочете запустити ці зразки, вам потрібно буде додати наступні змінні середовища до вашого `.env` файлу:

### Сторінка огляду (Проект)

- `AZURE_SUBSCRIPTION_ID` - Перевірте **Project details** на сторінці **Overview** вашого проекту.

- `AZURE_AI_PROJECT_NAME` - Подивіться на верхню частину сторінки **Overview** вашого проекту.

- `AZURE_OPENAI_SERVICE` - Знайдіть це на вкладці **Included capabilities** для **Azure OpenAI Service** на сторінці **Overview**.

### Центр управління

- `AZURE_OPENAI_RESOURCE_GROUP` - Перейдіть до **Project properties** на сторінці **Overview** Центру управління.

- `GLOBAL_LLM_SERVICE` - У розділі **Connected resources** знайдіть назву підключення **Azure AI Services**. Якщо не вказано, перевірте **Azure portal** у вашій групі ресурсів для назви ресурсу AI Services.

### Сторінка моделей + кінцевих точок

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Виберіть вашу модель вбудовування (наприклад, `text-embedding-ada-002`) і запишіть **Deployment name** з деталей моделі.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Виберіть вашу модель чату (наприклад, `gpt-4o-mini`) і запишіть **Deployment name** з деталей моделі.

### Портал Azure

- `AZURE_OPENAI_ENDPOINT` - Знайдіть **Azure AI services**, натисніть на нього, потім перейдіть до **Resource Management**, **Keys and Endpoint**, прокрутіть вниз до "Azure OpenAI endpoints" і скопіюйте той, що зазначений як "Language APIs".

- `AZURE_OPENAI_API_KEY` - На тому ж екрані скопіюйте KEY 1 або KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Знайдіть ваш ресурс **Azure AI Search**, натисніть на нього і перегляньте **Overview**.

- `AZURE_SEARCH_API_KEY` - Потім перейдіть до **Settings**, а потім **Keys**, щоб скопіювати основний або вторинний адміністративний ключ.

### Зовнішня веб-сторінка

- `AZURE_OPENAI_API_VERSION` - Відвідайте сторінку [життєвого циклу версії API](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) у розділі **Latest GA API release**.

### Налаштування автентифікації без ключів

Замість того, щоб жорстко кодувати ваші облікові дані, ми будемо використовувати підключення без ключів до Azure OpenAI. Для цього ми імпортуємо `DefaultAzureCredential`, а потім викличемо функцію `DefaultAzureCredential`, щоб отримати облікові дані.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Застрягли десь?
Якщо у вас виникли проблеми з запуском цього налаштування, приєднуйтесь до нашого <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord спільноти Azure AI</a> або <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">створіть запит</a>.

## Наступний урок

Тепер ви готові запустити код для цього курсу. Бажаємо приємного навчання про світ AI-агентів!

[Вступ до AI-агентів та їх застосування](../01-intro-to-ai-agents/README.md)

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.