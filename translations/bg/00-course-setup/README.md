# Настройка на курса

## Въведение

Този урок ще обхване как да стартирате примерите с код от този курс.

## Присъединете се към други учащи и получете помощ

Преди да започнете да клонирате вашето хранилище, присъединете се към [AI Agents For Beginners Discord канал](https://aka.ms/ai-agents/discord), за да получите помощ със настройката, да зададете въпроси за курса или да се свържете с други учащи.

## Клониране или разклоняване на това хранилище

За да започнете, моля, клонирайте или разклонете GitHub хранилището. Това ще създаде ваша собствена версия на учебните материали, за да можете да стартирате, тествате и коригирате кода!

Това може да стане като кликнете на линка за <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">разклоняване на хранилището</a>

Вече трябва да имате своя собствена разклонена версия на този курс на следния линк:

![Forked Repo](../../../translated_images/bg/forked-repo.33f27ca1901baa6a.webp)

### Повърхностно клониране (препоръчително за работилница / Codespaces)

  >Пълното хранилище може да е голямо (~3 GB), когато изтеглите цялата история и всички файлове. Ако посещавате само работилницата или ви трябват само няколко папки с уроци, повърхностното клониране (или частично клониране) избягва голяма част от изтеглянето като съкращава историята и/или пропуска blob файловете.

#### Бързо повърхностно клониране — минимална история, всички файлове

Заменете `<your-username>` в следните команди с URL-а на вашето разклонение (или с upstream URL ако предпочитате).

За да клонирате само най-новата история на комитите (малко изтегляне):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

За да клонирате конкретен клон:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частично (sparse) клониране — минимални blob файлове + само избрани папки

Това използва частично клониране и sparse-checkout (изисква Git 2.25+ и се препоръчва съвременен Git с поддръжка на частично клониране):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Влезте в директорията на хранилището:

```bash|powershell
cd ai-agents-for-beginners
```

След това укажете кои папки желаете (примерът по-долу показва две папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

След като клонирате и проверите файловете, ако се нуждаете само от файловете и искате да освободите място (без git история), изтрийте метаданните на хранилището (💀необратимо — ще загубите всички Git функционалности: няма комити, пулове, пушове или достъп до история).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Използване на GitHub Codespaces (препоръчително да избегнете големи локални изтегляния)

- Създайте нов Codespace за това хранилище чрез [GitHub UI](https://github.com/codespaces).  

- В терминала на новосъздадения Codespace, стартирайте една от горните команди за повърхностно/частично клониране, за да получите само необходимите папки с уроци в Codespace работната среда.
- По желание: след клониране в Codespaces, изтрийте .git, за да освободите допълнително място (вижте командите за почистване по-горе).
- Забележка: Ако предпочитате да отворите хранилището директно в Codespaces (без допълнително клониране), имайте предвид, че Codespaces ще построи devcontainer средата и може да осигури повече от необходимото. Клонирането на повърхностно копие в чист Codespace ви дава повече контрол върху използването на дисковото пространство.

#### Съвети

- Винаги заменяйте URL-а за клониране с вашето разклонение, ако искате да редактирате/комитирате.
- Ако по-късно ви трябва повече история или файлове, можете да ги изтеглите или да коригирате sparse-checkout, за да включите допълнителни папки.

## Стартиране на кода

Този курс предлага серия Jupyter бележници, които можете да стартирате, за да придобиете практически опит в създаването на AI агенти.

Примерите с код използват **Microsoft Agent Framework (MAF)** с `AzureAIProjectAgentProvider`, който се свързва с **Azure AI Agent Service V2** (Responses API) чрез **Microsoft Foundry**.

Всички Python бележници са означени с `*-python-agent-framework.ipynb`.

## Изисквания

- Python 3.12+
  - **ЗАБЕЛЕЖКА**: Ако нямате инсталиран Python3.12, уверете се, че го инсталирате. След това създайте виртуална среда с python3.12, за да осигурите правилните версии от файла requirements.txt.
  
    >Пример

    Създайте директория за Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    След това активирайте средата за:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: За примерите с .NET, уверете се, че сте инсталирали [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или по-нова версия. След това проверете версията на инсталирания .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — необходимо за удостоверяване. Инсталирайте от [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure абонамент** — за достъп до Microsoft Foundry и Azure AI Agent Service.
- **Microsoft Foundry проект** — проект с разположен модел (например `gpt-4o`). Вижте [Стъпка 1](#стъпка-1-създаване-на-microsoft-foundry-проект) по-долу.

В корена на това хранилище включихме файл `requirements.txt`, който съдържа всички необходими Python пакети за стартиране на примерите с код.

Можете да ги инсталирате като изпълните следната команда в терминала, в коренната директория на хранилището:

```bash|powershell
pip install -r requirements.txt
```

Препоръчваме да създадете Python виртуална среда, за да избегнете конфликти и проблеми.

## Настройка на VSCode

Уверете се, че използвате правилната версия на Python във VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка на Microsoft Foundry и Azure AI Agent Service

### Стъпка 1: Създаване на Microsoft Foundry проект

Ще ви трябва Azure AI Foundry **хъб** и **проект** с разположен модел, за да стартирате бележниците.

1. Отидете на [ai.azure.com](https://ai.azure.com) и влезте с вашия Azure акаунт.
2. Създайте **хъб** (или използвайте съществуващ). Вижте: [Обзор ресурсите на хъба](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. В хъба създайте **проект**.
4. Разположете модел (например `gpt-4o`) от **Models + Endpoints** → **Deploy model**.

### Стъпка 2: Вземете вашия проектен край и име на разполагане на модела

От вашия проект в портала Microsoft Foundry:

- **Project Endpoint** — отидете на страницата **Overview** и копирайте URL адреса на крайна точка.

![Project Connection String](../../../translated_images/bg/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — отидете на **Models + Endpoints**, изберете разположения модел и отбележете **Deployment name** (например `gpt-4o`).

### Стъпка 3: Влезте в Azure с `az login`

Всички бележници използват **`AzureCliCredential`** за удостоверяване — няма нужда да управлявате API ключове. За това трябва да сте влезли чрез Azure CLI.

1. **Инсталирайте Azure CLI**, ако не сте го направили: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Влезте** с командата:

    ```bash|powershell
    az login
    ```

    Ако сте в отдалечена/Кодспейс среда без браузър:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Изберете абонамента си**, ако бъдете подканени — изберете този, съдържащ Foundry проекта ви.

4. **Проверете** дали сте влезли:

    ```bash|powershell
    az account show
    ```

> **Защо `az login`?** Бележниците се удостоверяват чрез `AzureCliCredential` от пакета `azure-identity`. Това означава, че вашата сесия в Azure CLI осигурява идентификационните данни — без API ключове или тайни във вашия `.env` файл. Това е [препоръчителна практика за сигурност](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

| Променлива | Къде да я намерите |
|------------|-------------------|
| `AZURE_AI_PROJECT_ENDPOINT` | портал Foundry → вашият проект → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | портал Foundry → **Models + Endpoints** → името на вашия разположен модел |

Това е всичко за повечето уроци! Бележниците ще се удостоверяват автоматично чрез вашата `az login` сесия.

### Стъпка 5: Инсталирайте Python зависимостите

```bash|powershell
pip install -r requirements.txt
```

Препоръчваме да изпълните това в рамките на виртуалната среда, която създадохте по-рано.

## Допълнителна настройка за Урок 5 (Agentic RAG)

Урок 5 използва **Azure AI Search** за генерация с разширено извличане. Ако планирате да изпълнявате този урок, добавете тези променливи във вашия `.env` файл:

| Променлива | Къде да я намерите |
|------------|-------------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure портал → вашият **Azure AI Search** ресурс → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure портал → вашият **Azure AI Search** ресурс → **Settings** → **Keys** → основен администраторски ключ |

## Допълнителна настройка за Урок 6 и Урок 8 (GitHub модели)

Някои бележници в уроци 6 и 8 използват **GitHub Models** вместо Azure AI Foundry. Ако планирате да изпълните тези примери, добавете тези променливи във вашия `.env` файл:

| Променлива | Къде да я намерите |
|------------|-------------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Използвайте `https://models.inference.ai.azure.com` (по подразбиране) |
| `GITHUB_MODEL_ID` | Име на модела за използване (напр. `gpt-4o-mini`) |

## Алтернативен доставчик: MiniMax (съвместим с OpenAI)

[MiniMax](https://platform.minimaxi.com/) предоставя модели с голям контекст (до 204K токена) чрез OpenAI-съвместимо API. Тъй като Microsoft Agent Framework `OpenAIChatClient` работи с всеки OpenAI-съвместим край, можете да използвате MiniMax като директна алтернатива на GitHub Models или OpenAI.

Добавете тези променливи във вашия `.env` файл:

| Променлива | Къде да я намерите |
|------------|-------------------|
| `MINIMAX_API_KEY` | [MiniMax платформата](https://platform.minimaxi.com/) → API ключове |
| `MINIMAX_BASE_URL` | Използвайте `https://api.minimax.io/v1` (по подразбиране) |
| `MINIMAX_MODEL_ID` | Име на модела за използване (напр. `MiniMax-M3`) |

**Примерни модели**: `MiniMax-M3` (препоръчителен), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (по-бързи отговори). Имената и наличността на моделите може да се променят във времето, а достъпът до даден модел може да зависи от вашия акаунт или регион — проверете [MiniMax платформата](https://platform.minimaxi.com/) за актуалния списък. Ако `MiniMax-M3` не е достъпен за вашия акаунт, задайте `MINIMAX_MODEL_ID` на модел, до който имате достъп (например `MiniMax-M2.7`).

Примерите с код, които използват `OpenAIChatClient` (напр. Урок 14 работен процес за резервация на хотел), автоматично ще открият и използват вашата MiniMax конфигурация когато `MINIMAX_API_KEY` е зададен.

## Допълнителна настройка за Урок 8 (Bing grounding workflow)

Условният работен процес в урок 8 използва **Bing grounding** чрез Azure AI Foundry. Ако планирате да стартирате този пример, добавете тази променлива във вашия `.env` файл:

| Променлива | Къде да я намерите |
|------------|-------------------|
| `BING_CONNECTION_ID` | Azure AI Foundry портал → вашият проект → **Management** → **Connected resources** → вашата Bing връзка → копирайте Connection ID |

## Отстраняване на проблеми

### Грешки при валидиране на SSL сертификат на macOS

Ако сте на macOS и срещнете грешка като:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Това е известен проблем с Python на macOS, където системните SSL сертификати не се доверяват автоматично. Опитайте следните решения, в посочения ред:

**Опция 1: Стартирайте скрипта на Python за инсталиране на сертификати (препоръчително)**

```bash
# Заменете 3.XX с инсталираната версия на Python (например 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Опция 2: Използвайте `connection_verify=False` в бележника (само за бележници с GitHub Models)**

В бележника от Урок 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) вече има коментиран workaround. Разкоментирайте `connection_verify=False`, когато създавате клиента:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Деактивирайте проверката на SSL, ако срещнете грешки с сертификата
)
```

> **⚠️ Внимание:** Деактивирането на SSL верификацията (`connection_verify=False`) намалява сигурността, като пропуска проверката на сертификатите. Използвайте това само като временен workaround в развойна среда, никога в продукция.

**Опция 3: Инсталирайте и използвайте `truststore`**

```bash
pip install truststore
```

След това добавете следното в началото на вашия бележник или скрипт преди да правите мрежови повиквания:

```python
import truststore
truststore.inject_into_ssl()
```

## Застрян ли сте някъде?

Ако имате някакви проблеми при настройката, включете се в <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">създайте issue</a>.
## Next Lesson

Вече сте готови да стартирате кода за този курс. Приятно учене за света на AI агентите!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->