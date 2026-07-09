# Настройка на курса

## Въведение

Този урок ще обясни как да стартирате примерите с код от този курс.

## Присъединете се към други обучаващи се и потърсете помощ

Преди да започнете с клонирането на вашето хранилище, присъединете се към [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord), за да получите помощ със настройката, въпроси относно курса или да се свържете с други обучаващи се.

## Клониране или форкване на това хранилище

За да започнете, моля, клонирайте или форкнете GitHub хранилището. Това ще създаде ваша собствена версия на материала от курса, която да можете да изпълнявате, тествате и променяте!

Това може да стане, като кликнете на линка за <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форк на репото</a>

Сега би трябвало да имате ваша собствена форкната версия на този курс на следния линк:

![Forked Repo](../../../translated_images/bg/forked-repo.33f27ca1901baa6a.webp)

### Плитко клониране (препоръчително за работилница / Codespaces)

  >Пълното хранилище може да е голямо (~3 GB), ако изтеглите цялата история и всички файлове. Ако участвате само в работилницата или ви трябват само няколко папки с уроци, плиткото клониране (или частично клониране) ще ви спести голяма част от изтеглянето, като съкрати историята и/или пропусне големи двоични файлове.

#### Бързо плитко клониране — минимална история, всички файлове

Заменете `<your-username>` в долуописаните команди с URL-а на вашия форк (или URL-а на upstream, ако предпочитате).

За да клонирате само най-новата история на комитите (малко изтегляне):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

За да клонирате конкретен клон:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частично (sparse) клониране — минимални двоични файлове + само избрани папки

Това използва частично клониране и sparse-checkout (изисква Git 2.25+ и препоръчително съвременен Git с поддръжка на partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Влезте в папката на репото:

```bash|powershell
cd ai-agents-for-beginners
```

След това посочете кои папки желаете (примерът по-долу показва две папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

След клонирането и проверката на файловете, ако се нуждаете само от файловете и искате да освободите място (без git история), моля изтрийте метаданните на хранилището (💀независимо — ще загубите всички Git функционалности: нямате комити, pull, push или достъп до историята).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Използване на GitHub Codespaces (препоръчително за избягване на големи местни изтегляния)

- Създайте нов Codespace за това хранилище чрез [GitHub UI](https://github.com/codespaces).

- В терминала на новосъздадения Codespace стартирайте някоя от командите за плитко/частично клониране, за да вкарате само нужните ви папки с уроци в работното пространство на Codespace.
- По избор: след клониране в Codespaces, премахнете .git за освобождаване на допълнително място (вижте командите за премахване по-горе).
- Забележка: Ако предпочитате да отворите директно репото в Codespaces (без допълнително клониране), имайте предвид, че Codespaces ще създаде devcontainer среда и може да подготви повече неща от необходимото. Клонирането на плитко копие в чист Codespace ви дава повече контрол върху използването на дисковото пространство.

#### Съвети

- Винаги заменяйте URL-то за клониране с това на вашия форк, ако искате да редактирате/комитирате.
- Ако по-късно имате нужда от повече история или файлове, можете да ги изтеглите или да настроите sparse-checkout за допълнителни папки.

## Стартиране на кода

Този курс предоставя серия от Jupyter Notebook-и, които можете да стартирате за практически опит в изграждането на AI агенти.

Примерите с код използват **Microsoft Agent Framework (MAF)** с `FoundryChatClient`, който се свързва с **Microsoft Foundry Agent Service V2** (Responses API) чрез **Microsoft Foundry**.

Всички Python notebooks са маркирани като `*-python-agent-framework.ipynb`.

## Изисквания

- Python 3.12+
  - **ЗАБЕЛЕЖКА**: Ако нямате инсталиран Python3.12, уверете се, че го инсталирате. След това създайте виртуална среда със python3.12, за да се инсталират правилните версии от файла requirements.txt.
  
    >Пример

    Създайте директория за Python виртуалната среда:

    ```bash|powershell
    python -m venv venv
    ```

    След това активирайте виртуалната среда за:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: За примерните кодове с .NET, уверете се, че сте инсталирали [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или по-нова версия. След това проверете версията на инсталирания .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Необходим за автентикация. Инсталирайте от [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — За достъп до Microsoft Foundry и Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Проект с разположен модел (напр. `gpt-4o`). Вижте [Стъпка 1](#стъпка-1-създайте-microsoft-foundry-проект) по-долу.

В корена на това хранилище е добавен файл `requirements.txt`, който съдържа всички нужни Python пакети за изпълнение на примерите с код.

Можете да ги инсталирате като изпълните следната команда в терминала в корена на хранилището:

```bash|powershell
pip install -r requirements.txt
```

Препоръчваме да създадете виртуална среда на Python, за да избегнете конфликти и проблеми.

## Настройка на VSCode

Уверете се, че използвате правилната версия на Python във VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка на Microsoft Foundry и Microsoft Foundry Agent Service

### Стъпка 1: Създайте Microsoft Foundry Проект

Трябва да имате Microsoft Foundry **хъб** и **проект** с разположен модел, за да стартирате notebook-ите.

1. Отидете на [ai.azure.com](https://ai.azure.com) и влезте със своя Azure акаунт.
2. Създайте **хъб** (или използвайте съществуващ). Вижте: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Влезте в хъба и създайте **проект**.
4. Разположете модел (напр. `gpt-4o`) от **Models + Endpoints** → **Deploy model**.

### Стъпка 2: Вземете Project Endpoint и името на Model Deployment

От проектора в портала на Microsoft Foundry:

- **Project Endpoint** — Отидете на страницата **Overview** и копирайте URL адреса на енпойнта.

![Project Connection String](../../../translated_images/bg/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Отидете на **Models + Endpoints**, изберете разположения модел и отбележете **Deployment name** (напр. `gpt-4o`).

### Стъпка 3: Влезте в Azure с `az login`

Всички notebooks използват **`AzureCliCredential`** за автентикация — без нужда от API ключове. Това изисква да сте влезли чрез Azure CLI.

1. **Инсталирайте Azure CLI**, ако още не сте: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Влезте** като изпълните:

    ```bash|powershell
    az login
    ```

    Или ако сте в отдалечена/кодспейс среда без браузър:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Изберете вашия абонамент**, ако сте подканени — изберете този съдържащ Foundry проекта ви.

4. **Проверете**, че сте влезли:

    ```bash|powershell
    az account show
    ```

> **Защо `az login`?** Notebook-ите се автентикират чрез `AzureCliCredential` от пакета `azure-identity`. Това значи, че сесията ви в Azure CLI предоставя необходимите данни — без API ключове или тайни във файла ви `.env`. Това е [най-добра практика за сигурност](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Порталът на Foundry → ваш проект → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Порталът на Foundry → **Models + Endpoints** → името на разположения модел |

Това е за повечето уроци! Notebook-ите ще се автентикират автоматично чрез сесията ви `az login`.

### Стъпка 5: Инсталирайте Python зависимости

```bash|powershell
pip install -r requirements.txt
```

Препоръчваме да стартирате това в създадената по-рано виртуална среда.

## Допълнителна настройка за урок 5 (Agentic RAG)

Урок 5 използва **Azure AI Search** за генериране с помощта на търсене. Ако планирате да стартирате този урок, добавете тези променливи във вашия `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure портал → вашият ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure портал → вашият ресурс **Azure AI Search** → **Settings** → **Keys** → основен администраторски ключ |

## Допълнителна настройка за уроци, които извикват Azure OpenAI директно (уроци 6 и 8)

Някои notebooks в уроци 6 и 8 използват **Azure OpenAI** директно (чрез **Responses API**) вместо през Microsoft Foundry проект. Тези примери преди са използвали GitHub Models, които са остарели (пенсиониране през юли 2026) и не поддържат Responses API. Ако планирате да стартирате тези примери, добавете тези променливи във вашия `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure портал → вашият ресурс **Azure OpenAI** → **Keys and Endpoint** → Endpoint (напр. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Името на разположения ви модел (напр. `gpt-4o-mini`), който поддържа Responses API |
| `AZURE_OPENAI_API_KEY` | По избор — само ако използвате автентикация с ключ вместо чрез `az login` / Entra ID |

> Responses API използва стабилен `/openai/v1/` енпойнт, така че не се изисква `api-version`. Влезте с `az login`, за да използвате автентикация с Entra ID без ключове.

## Алтернативен доставчик: MiniMax (съвместим с OpenAI)

[MiniMax](https://platform.minimaxi.com/) предоставя модели с голям контекст (до 204K токена) чрез API съвместим с OpenAI. Тъй като Microsoft Agent Framework `OpenAIChatClient` работи с всеки съвместим с OpenAI енпойнт, можете да използвате MiniMax като заместител на Azure OpenAI или OpenAI.

Добавете тези променливи във вашия `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Използвайте `https://api.minimax.io/v1` (по подразбиране) |
| `MINIMAX_MODEL_ID` | Името на модела за използване (напр. `MiniMax-M3`) |

**Примерни модели**: `MiniMax-M3` (препоръчителен), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (по-бързи отговори). Имената и наличността на моделите могат да се променят с времето, а достъпът до даден модел може да зависи от вашия акаунт или регион — проверете текущия списък на [MiniMax Platform](https://platform.minimaxi.com/). Ако `MiniMax-M3` не е наличен за вашия акаунт, задайте `MINIMAX_MODEL_ID` с модел, до който имате достъп (напр. `MiniMax-M2.7`).

Примерните кодове, използващи `OpenAIChatClient` (напр. Lesson 14 workflow за резервация на хотел), автоматично ще откриват и използват вашата MiniMax конфигурация, когато `MINIMAX_API_KEY` е зададен.

## Алтернативен доставчик: Foundry Local (стартиране на модели локално)

[Foundry Local](https://foundrylocal.ai) е лека runtime среда, която изтегля, управлява и обслужва езикови модели **изцяло на вашата машина** чрез API, съвместим с OpenAI — без облак, без абонамент в Azure и без API ключове. Отличен избор за офлайн разработка, експериментиране без облачни разходи или съхранение на данни локално.

Тъй като Microsoft Agent Framework `OpenAIChatClient` работи с всеки съвместим с OpenAI енпойнт, Foundry Local е локална алтернатива на Azure OpenAI.

**1. Инсталирайте Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Изтеглете и стартирайте модел** (това също стартира локалната услуга):

```bash
foundry model list          # виж наличните модели
foundry model run phi-4-mini
```

**3. Инсталирайте Python SDK**, използван за откриване на локалния енпойнт:

```bash
pip install foundry-local-sdk
```

**4. Насочете Microsoft Agent Framework към вашия локален модел:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Изтегля (ако е необходимо) и обслужва модела локално, след което открива крайна точка/порт.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # например http://localhost:<port>/v1
    api_key=manager.api_key,        # винаги "не е задължително" за Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Забележка:** Foundry Local предоставя OpenAI-съвместим **Chat Completions** енпойнт. Използвайте го за локална разработка и офлайн ситуации. За пълната функционалност на **Responses API** (състояние на разговорите, дълбока оркестрация на инструменти и разработка тип агент), използвайте **Azure OpenAI** или Microsoft Foundry проект както е показано в уроците. Вижте [документацията на Foundry Local](https://foundrylocal.ai) за текущ каталог на модели и поддръжка на платформи.

## Допълнителна настройка за урок 8 (Bing Grounding Workflow)


Задължителният работен бележник с условен поток в урок 8 използва **Bing grounding** чрез Microsoft Foundry. Ако планирате да стартирате този пример, добавете тази променлива във вашия `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `BING_CONNECTION_ID` | Портал Microsoft Foundry → вашия проект → **Management** → **Connected resources** → вашата Bing връзка → копирайте ID на връзката |

## Отстраняване на неизправности

### Грешки при проверка на SSL сертификат на macOS

Ако сте на macOS и срещнете грешка като:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Това е известен проблем с Python на macOS, където системните SSL сертификати не се доверяват автоматично. Опитайте следните решения по ред:

**Опция 1: Стартирайте Python скрипта Install Certificates (препоръчително)**

```bash
# Заменете 3.XX с вашата инсталирана версия на Python (напр. 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Опция 2: Използвайте `connection_verify=False` в своя бележник (само за GitHub Models бележници)**

В бележника от Урок 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) вече е включено закоментирано обходно решение. Премахнете коментара от `connection_verify=False` при създаване на клиента:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Деактивирайте проверката на SSL, ако срещнете грешки с сертификата
)
```

> **⚠️ Внимание:** Изключването на проверката на SSL (`connection_verify=False`) намалява сигурността, като пропуска валидирането на сертификата. Използвайте това само като временно решение в среди за разработка, никога в продукция.

**Опция 3: Инсталирайте и използвайте `truststore`**

```bash
pip install truststore
```

След това добавете следното в началото на вашия бележник или скрипт преди да правите мрежови повиквания:

```python
import truststore
truststore.inject_into_ssl()
```

## Закъсали ли сте някъде?

Ако имате проблеми с тази настройка, присъединете се към <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord общността на Azure AI</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">създайте проблем</a>.

## Следващ урок

Вече сте готови да стартирате кода за този курс. Приятно учене за света на AI агентите!

[Въведение в AI агентите и примери за случаи на използване](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->