# Настройка на курса

## Въведение

В този урок ще обясним как да стартирате примерите с код от този курс.

## Присъединете се към други обучаеми и получете помощ

Преди да започнете да клонирате вашето хранилище, присъединете се към [Discord канал 'AI Agents For Beginners'](https://aka.ms/ai-agents/discord) за помощ при настройката, въпроси относно курса или за контакт с други обучаеми.

## Клониране или форкване на това хранилище

За да започнете, моля клонирайте или форкнете GitHub хранилището. Това ще създаде ваша собствена версия на материалите от курса, така че да можете да стартирате, тествате и настройвате кода!

Това може да стане чрез кликване на линка към <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкнете хранилището</a>

Сега трябва да имате ваша собствена форкната версия на този курс на следния линк:

![Форкнато хранилище](../../../translated_images/bg/forked-repo.33f27ca1901baa6a.webp)

### Плитко клониране (препоръчително за работилници / Codespaces)

  >Пълното хранилище може да бъде голямо (~3 GB), когато изтеглите цялата история и всички файлове. Ако присъствате само на работилницата или ви трябват само няколко папки от уроците, плитко клониране (или sparse clone) избягва повечето от това изтегляне чрез съкращаване на историята и/или пропускане на blob-ове.

#### Бързо плитко клониране — минимална история, всички файлове

Заменете `<your-username>` в командите по-долу с URL-а на вашия форк (или с upstream URL-а, ако предпочитате).

За да клонирате само последната история на комитите (малко сваляне):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

За да клонирате конкретен клон:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частично (sparse) клониране — минимални blob-ове + само избрани папки

Това използва partial clone и sparse-checkout (изисква Git 2.25+ и се препоръчва модерна версия на Git с поддръжка за partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Отидете в директорията на хранилището:

```bash|powershell
cd ai-agents-for-beginners
```

След това посочете кои папки искате (примерът по-долу показва две папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

След клониране и проверка на файловете, ако ви трябват само файловете и искате да освободите пространство (без git история), моля изтрийте метаданните на хранилището (💀необратимо — ще загубите цялата Git функционалност: няма комити, pulls, pushes или достъп до историята).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Използване на GitHub Codespaces (препоръчително за избягване на локални големи изтегляния)

- Създайте нов Codespace за това хранилище чрез [GitHub UI](https://github.com/codespaces).  

- В терминала на новосъздадения Codespace изпълнете една от горните плитко/sparse clone команди, за да внесете само урокните папки, от които се нуждаете, в работното пространство на Codespace.
- По избор: след клониране във вътрешността на Codespaces, премахнете .git, за да възвърнете допълнително пространство (вижте командите за премахване по-горе).
- Забележка: Ако предпочитате да отворите репото директно в Codespaces (без допълнително клониране), имайте предвид, че Codespaces ще конструира devcontainer средата и може все пак да предостави повече от това, от което се нуждаете. Клониране на плитко копие вътре в свеж Codespace ви дава повече контрол върху използването на дисковото пространство.

#### Съвети

- Винаги заменяйте clone URL-а с вашия форк, ако искате да редактирате/commit-вате.
- Ако по-късно ви трябва повече история или файлове, можете да ги изтеглите или да коригирате sparse-checkout, за да включите допълнителни папки.

## Изпълнение на кода

Този курс предлага серия Jupyter Notebook-и, които можете да изпълнявате, за да получите практическо изживяване при изграждането на AI агенти.

Примерите с код използват **Microsoft Agent Framework (MAF)** с `AzureAIProjectAgentProvider`, който се свързва с **Azure AI Agent Service V2** (Responses API) чрез **Microsoft Foundry**.

Всички Python бележници са маркирани като `*-python-agent-framework.ipynb`.

## Изисквания

- Python 3.12+
  - **NOTE**: Ако нямате инсталиран Python 3.12, уверете се, че го инсталирате. След това създайте venv, използвайки python3.12, за да сте сигурни, че правилните версии ще бъдат инсталирани от файла requirements.txt.
  
    >Пример

    Създайте директория за Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    След това активирайте venv средата за:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: За примерните кодове, използващи .NET, уверете се, че сте инсталирали [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или по-нова версия. След това проверете инсталираната версия на .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Изисква се за автентикация. Инсталирайте от [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — За достъп до Microsoft Foundry и Azure AI Agent Service.
- **Microsoft Foundry Project** — Проект с разгърнат модел (например `gpt-4o`). Вижте [Стъпка 1](../../../00-course-setup) по-долу.

В корена на това хранилище сме включили файл `requirements.txt`, който съдържа всички необходими Python пакети за стартиране на примерите с код.

Можете да ги инсталирате, като изпълните следната команда в терминала в корена на хранилището:

```bash|powershell
pip install -r requirements.txt
```

Препоръчваме да създадете Python виртуална среда, за да избегнете конфликти и проблеми.

## Настройка на VSCode

Уверете се, че използвате правилната версия на Python в VSCode.

![изображение](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка на Microsoft Foundry и Azure AI Agent Service

### Стъпка 1: Създайте проект в Microsoft Foundry

Трябва ви Azure AI Foundry **hub** и **project** с разгърнат модел, за да стартирате бележниците.

1. Отидете на [ai.azure.com](https://ai.azure.com) и влезте с вашия Azure акаунт.
2. Създайте **hub** (или използвайте вече съществуващ). Вижте: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Вътре в hub-а създайте **project**.
4. Разгърнете модел (напр. `gpt-4o`) от **Models + Endpoints** → **Deploy model**.

### Стъпка 2: Вземете крайния адрес на проекта и името на разгръщане на модела

От вашия проект в портала Microsoft Foundry:

- **Project Endpoint** — Отидете на страницата **Overview** и копирайте endpoint URL-а.

![Връзка към проекта](../../../translated_images/bg/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Отидете в **Models + Endpoints**, изберете разгърнатия си модел и отбележете **Deployment name** (например `gpt-4o`).

### Стъпка 3: Впишете се в Azure с `az login`

Всички бележници използват **`AzureCliCredential`** за автентикация — няма API ключове за управление. Това изисква да сте вписани чрез Azure CLI.

1. **Инсталирайте Azure CLI** ако все още не сте: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Впишете се** като изпълните:

    ```bash|powershell
    az login
    ```

    Или ако сте в отдалечена/Codespace среда без браузър:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Изберете вашия subscription** ако бъдете подканени — изберете този, който съдържа Foundry проекта ви.

4. **Проверете** дали сте вписани:

    ```bash|powershell
    az account show
    ```

> **Защо `az login`?** Бележниците се удостоверяват, използвайки `AzureCliCredential` от пакета `azure-identity`. Това означава, че вашата Azure CLI сесия предоставя удостоверенията — няма API ключове или тайни във вашия `.env` файл. Това е [добра практика за сигурност](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Стъпка 4: Създайте вашия `.env` файл

Копирайте примерния файл:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Отворете `.env` и попълнете тези две стойности:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Къде да го намерите |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry портал → вашият проект → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry портал → **Models + Endpoints** → името на разгърнатия модел |

Това е всичко за повечето уроци! Бележниците ще се удостоверят автоматично чрез вашата `az login` сесия.

### Стъпка 5: Инсталирайте Python зависимости

```bash|powershell
pip install -r requirements.txt
```

Препоръчваме да изпълните това вътре във виртуалната среда, която създадохте по-рано.

## Допълнителна настройка за Урок 5 (Agentic RAG)

Урок 5 използва **Azure AI Search** за retrieval-augmented generation. Ако планирате да изпълните този урок, добавете тези променливи във вашия `.env` файл:

| Variable | Къде да го намерите |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure портал → вашият **Azure AI Search** ресурс → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure портал → вашият **Azure AI Search** ресурс → **Settings** → **Keys** → primary admin key |

## Допълнителна настройка за Урок 6 и Урок 8 (GitHub Models)

Някои бележници в уроците 6 и 8 използват **GitHub Models** вместо Azure AI Foundry. Ако планирате да стартирате тези примери, добавете тези променливи във вашия `.env` файл:

| Variable | Къде да го намерите |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Използвайте `https://models.inference.ai.azure.com` (по подразбиране) |
| `GITHUB_MODEL_ID` | Името на модела за използване (напр. `gpt-4o-mini`) |

## Допълнителна настройка за Урок 8 (Bing Grounding Workflow)

Условният workflow бележник в урок 8 използва **Bing grounding** чрез Azure AI Foundry. Ако планирате да изпълните този пример, добавете тази променлива във вашия `.env` файл:

| Variable | Къде да го намерите |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry портал → вашият проект → **Management** → **Connected resources** → вашата Bing връзка → копирайте connection ID |

## Отстраняване на неизправности

### Грешки при проверка на SSL сертификатите на macOS

Ако сте на macOS и срещнете грешка като:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Това е известен проблем с Python на macOS, при който системните SSL сертификати не се доверяват автоматично. Опитайте следните решения в този ред:

**Опция 1: Стартирайте Install Certificates скрипта на Python (препоръчително)**

```bash
# Заменете 3.XX с инсталираната версия на Python (например 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Опция 2: Използвайте `connection_verify=False` в бележника си (само за бележници с GitHub Models)**

В бележника за Урок 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) вече е включено закоментирано решение. Разкоментирайте `connection_verify=False` при създаване на клиента:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Деактивирайте проверката на SSL, ако срещнете грешки с сертификата
)
```

> **⚠️ Warning:** Деактивирането на проверката на SSL (`connection_verify=False`) намалява сигурността, като прескача валидацията на сертификатите. Използвайте това само като временна мярка в развойна среда, никога в продукция.

**Опция 3: Инсталирайте и използвайте `truststore`**

```bash
pip install truststore
```

След това добавете следното в горната част на вашия бележник или скрипт преди да правите каквито и да е мрежови повиквания:

```python
import truststore
truststore.inject_into_ssl()
```

## Закъсали ли сте някъде?

Ако имате проблеми при изпълнението на тази настройка, присъединете се към нашия <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord общността на Azure AI</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">създайте issue</a>.

## Следващ урок

Вече сте готови да стартирате кода за този курс. Приятно учене и откриване на света на AI агентите! 

[Въведение в AI агентите и случаи на използване на агенти](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на езика, на който е написан, трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален превод, извършен от човешки преводач. Не носим отговорност за каквито и да е недоразумения или погрешни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->