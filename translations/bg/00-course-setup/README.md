# Настройка на курса

## Въведение

Този урок ще покрие как да стартирате примерния код от този курс.

## Присъединете се към други учащи и получете помощ

Преди да започнете да клонирате вашето репо, присъединете се към [AI Agents For Beginners Discord канала](https://aka.ms/ai-agents/discord), за да получите помощ с настройката, да зададете въпроси за курса или да се свържете с други учащи.

## Клониране или форкване на това репо

За да започнете, моля клонирайте или фокусирайте GitHub репозитория. Това ще ви даде собствена версия на учебния материал, за да можете да стартирате, тествате и настройвате кода!

Това може да стане чрез кликване на линка за <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкване на репото</a>

Сега трябва да имате собствена форкната версия на този курс на следния линк:

![Forked Repo](../../../translated_images/bg/forked-repo.33f27ca1901baa6a.webp)

### Плитко клониране (препоръчително за работилници / Codespaces)

  >Пълното хранилище може да е голямо (~3 GB), когато изтеглите цялата история и всички файлове. Ако посещавате само работилницата или имате нужда само от няколко папки за уроци, плиткото клониране (или частично клониране) избягва по-голямата част от тегленето чрез съкращаване на историята и/или пропускане на blob обекти.

#### Бързо плитко клониране — минимална история, всички файлове

Заменете `<your-username>` в командите по-долу с URL адреса на вашия форк (или на оригиналния upstream, ако предпочитате).

За да клонирате само най-новата история на комитите (малко теглене):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

За да клонирате конкретен клон:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частично (sparse) клониране — минимални blob обекти + само избрани папки

Това използва частично клониране и sparse-checkout (изисква Git 2.25+ и се препоръчва съвременен Git с поддръжка на частично клониране):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Влезте в папката на репото:

```bash|powershell
cd ai-agents-for-beginners
```

След това задайте кои папки искате (примерът по-долу показва две папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

След клонирането и проверката на файловете, ако ви трябват единствено файловете и желаете да освободите място (без git история), изтрийте метаданните на репото (💀необратимо — ще загубите цялата Git функционалност: няма комити, pull, push или достъп до историята).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Използване на GitHub Codespaces (препоръчително за избягване на големи локални изтегляния)

- Създайте нов Codespace за това репо чрез [GitHub UI](https://github.com/codespaces).  

- В терминала на новосъздадения Codespace стартирайте една от командите за плитко/частично клониране по-горе, за да внесете само нужните ви папки за уроците в работната среда на Codespace.
- По избор: след клонирането в Codespaces, премахнете .git, за да освободите допълнително място (вижте командите за премахване по-горе).
- Забележка: Ако предпочитате да отворите репото директно в Codespaces (без допълнително клониране), имайте предвид, че Codespaces ще създаде devcontainer средата и може да зареди повече от необходимото. Клонирането на плитко копие вътре в нов Codespace ви дава по-голям контрол върху дисковото пространство.

#### Съвети

- Винаги заменяйте URL адреса за клониране с вашия форк, ако искате да редактирате или комитвате.
- Ако по-късно имате нужда от повече история или файлове, можете да ги изтеглите или да коригирате sparse-checkout, за да включите допълнителни папки.

## Стартиране на кода

Този курс предлага серия от Jupyter notebooks, които можете да стартирате, за да получите практически опит в изграждането на AI агенти.

Примерите използват **Microsoft Agent Framework (MAF)** с `FoundryChatClient`, който се свързва с **Microsoft Foundry Agent Service V2** (Responses API) чрез **Microsoft Foundry**.

Всички Python notebooks са маркирани като `*-python-agent-framework.ipynb`.

## Изисквания

- Python 3.12+
  - **ЗАБЕЛЕЖКА**: Ако нямате инсталиран Python3.12, уверете се, че го инсталирате. След това създайте вашата виртуална среда с python3.12, за да гарантирате инсталацията на правилните версии от файла requirements.txt.
  
    >Пример

    Създаване на директория за Python виртуална среда:

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

- .NET 10+: За примерния код, използващ .NET, уверете се, че инсталирате [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или по-нова версия. След това проверете версията на инсталирания .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Необходим за автентикация. Инсталирайте от [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Абонамент** — За достъп до Microsoft Foundry и Microsoft Foundry Agent Service.
- **Microsoft Foundry Проект** — Проект с разположен модел (например `gpt-4.1-mini`). Вижте [Стъпка 1](#стъпка-1-създаване-на-microsoft-foundry-проект) по-долу.

Включили сме файл `requirements.txt` в корена на това хранилище, който съдържа всички необходими Python пакети за стартиране на примерния код.

Можете да ги инсталирате, като изпълните следната команда в терминала в корена на репото:

```bash|powershell
pip install -r requirements.txt
```

Препоръчваме създаване на Python виртуална среда, за да избегнете конфликти и проблеми.

## Настройка на VSCode

Уверете се, че използвате правилната версия на Python във VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка на Microsoft Foundry и Microsoft Foundry Agent Service

### Стъпка 1: Създаване на Microsoft Foundry Проект

Необходим ви е Microsoft Foundry **hub** и **проект** с разположен модел, за да стартирате notebooks.

1. Отидете на [ai.azure.com](https://ai.azure.com) и влезте с вашия Azure акаунт.
2. Създайте **hub** (или използвайте съществуващ). Вижте: [Преглед на hub ресурсите](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Вътре в hub-а създайте **проект**.
4. Разположете модел (например `gpt-4.1-mini`) от **Models + Endpoints** → **Deploy model**.

### Стъпка 2: Намиране на Project Endpoint и Име на Моделната Деплоймънт

От вашия проект в Microsoft Foundry портала:

- **Project Endpoint** — Отидете на страницата **Overview** и копирайте URL адреса на endpoint-а.

![Project Connection String](../../../translated_images/bg/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Отидете в **Models + Endpoints**, изберете разположения модел и отбележете името на **Deployment** (например `gpt-4.1-mini`).

### Стъпка 3: Влизане в Azure с `az login`

Всички notebooks използват **`AzureCliCredential`** за автентикация — без нужда да управлявате API ключове. Това изисква да сте влезли чрез Azure CLI.

1. **Инсталирайте Azure CLI**, ако все още не сте: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Влезте**, като изпълните:

    ```bash|powershell
    az login
    ```

    Или ако сте в отдалечена среда/Codespace без браузър:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Изберете вашия абонамент**, ако бъдете подканени — изберете този, който съдържа вашия Foundry проект.

4. **Потвърдете**, че сте влезли:

    ```bash|powershell
    az account show
    ```

> **Защо `az login`?** Notebooks-те се автентикират чрез `AzureCliCredential` от пакета `azure-identity`. Това означава, че вашата сесия в Azure CLI предоставя кредитите — без API ключове или тайни във вашия `.env` файл. Това е [най-добра практика за сигурност](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Променлива | Къде да я намерите |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry портал → вашият проект → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry портал → **Models + Endpoints** → името на разположения модел |

Това е всичко за повечето уроци! Notebooks-те ще се автентикират автоматично чрез вашата сесия `az login`.

### Стъпка 5: Инсталирайте Python зависимости

```bash|powershell
pip install -r requirements.txt
```

Препоръчваме да изпълните това вътре във виртуалната среда, която създадохте по-рано.

## Допълнителна настройка за Урок 5 (Agentic RAG)

Урок 5 използва **Azure AI Search** за retrieval-augmented generation. Ако планирате да стартирате този урок, добавете тези променливи във вашия `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure портал → вашият ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure портал → вашият ресурс **Azure AI Search** → **Settings** → **Keys** → основен администраторски ключ |

## Допълнителна настройка за уроци, които извикват Azure OpenAI директно (уроци 6 и 8)

Някои notebooks в уроци 6 и 8 извикват **Azure OpenAI** директно (чрез **Responses API**) вместо да минават през Microsoft Foundry проект. Тези примери преди използваха GitHub Models, които са остарели (спиране през юли 2026) и не поддържат Responses API. Ако планирате да стартирате тези примери, добавете тези променливи във вашия `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure портал → вашият ресурс **Azure OpenAI** → **Keys and Endpoint** → Endpoint (например `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Името на вашия разположен модел (например `gpt-4.1-mini`), който поддържа Responses API |
| `AZURE_OPENAI_API_KEY` | По избор — само ако използвате автентикация с ключ вместо `az login` / Entra ID |

> Responses API използва стабилен `/openai/v1/` endpoint, така че не се изисква `api-version`. Влезте с `az login`, за да използвате идентификация с Entra ID без ключове.

## Алтернативен доставчик: MiniMax (съвместим с OpenAI)

[MiniMax](https://platform.minimaxi.com/) предоставя модели с голям контекст (до 204K токена) чрез OpenAI-съвместим API. Тъй като Microsoft Agent Framework `OpenAIChatClient` работи с всеки OpenAI-съвместим endpoint, можете да използвате MiniMax като алтернатива на Azure OpenAI или OpenAI.

Добавете тези променливи във вашия `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Използвайте `https://api.minimax.io/v1` (по подразбиране) |
| `MINIMAX_MODEL_ID` | Име на модела за използване (например `MiniMax-M3`) |

**Примерни модели**: `MiniMax-M3` (препоръчано), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (по-бързи отговори). Имената и наличността на моделите могат да се променят с времето, а достъпът до даден модел може да зависи от вашия акаунт или регион — проверявайте [MiniMax Platform](https://platform.minimaxi.com/) за актуалния списък. Ако `MiniMax-M3` не е достъпен за акаунта ви, задайте `MINIMAX_MODEL_ID` на модел, до който имате достъп (например `MiniMax-M2.7`).

Примерите, използващи `OpenAIChatClient` (например работния процес за резервация на хотел от урок 14), ще разпознават и използват вашата MiniMax конфигурация автоматично, когато `MINIMAX_API_KEY` е зададен.

## Алтернативен доставчик: Foundry Local (стартиране на модели локално)

[Foundry Local](https://foundrylocal.ai) е лека runtime среда, която изтегля, управлява и обслужва езикови модели **изцяло на вашата машина** чрез OpenAI-съвместим API — без облак, без Azure абонамент, без API ключове. Отличен избор за офлайн разработка, експерименти без облачни разходи или за съхранение на данни локално.

Тъй като Microsoft Agent Framework `OpenAIChatClient` работи с всеки OpenAI-съвместим endpoint, Foundry Local е локална алтернатива на Azure OpenAI.

**1. Инсталирайте Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Изтеглете и стартирайте модел** (това също стартира локалната услуга):

```bash
foundry model list          # вижте наличните модели
foundry model run phi-4-mini
```

**3. Инсталирайте Python SDK**, използван за откриване на локалния endpoint:

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
    base_url=manager.endpoint,      # напр. http://localhost:<port>/v1
    api_key=manager.api_key,        # винаги "не-необходимо" за Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Забележка:** Foundry Local предоставя OpenAI-съвместим **Chat Completions** endpoint. Използвайте го за локална разработка и офлайн сценарии. За пълната функционалност на **Responses API** (състояния на разговори, дълбока инструментална оркестрация и агентски стил разработка), насочете към **Azure OpenAI** или **Microsoft Foundry** проект, както е показано в уроците. Вижте [документацията на Foundry Local](https://foundrylocal.ai) за текущия каталог на модели и поддръжка на платформи.


## Допълнителна настройка за урок 8 (Bing Grounding Workflow)

В условния workflow бележник в урок 8 се използва **Bing grounding** чрез Microsoft Foundry. Ако планирате да стартирате този пример, добавете тази променлива във вашия файл `.env`:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `BING_CONNECTION_ID` | Портал Microsoft Foundry → вашият проект → **Management** → **Connected resources** → вашата Bing връзка → копирайте connection ID |

## Отстраняване на проблеми

### Грешки при проверка на SSL сертификат на macOS

Ако използвате macOS и се появи грешка като:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Това е известен проблем с Python на macOS, при който SSL сертификатите на системата не се доверяват автоматично. Опитайте следните решения по ред:

**Вариант 1: Стартирайте инсталационния скрипт за сертификати на Python (препоръчително)**

```bash
# Заменете 3.XX с инсталираната версия на Python (например 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Вариант 2: Използвайте `connection_verify=False` в своя бележник (само за бележници с GitHub модели)**

В бележника от урок 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) вече е включено коментирано решение. Разкоментирайте `connection_verify=False`, когато създавате клиента:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Деактивирайте проверката на SSL, ако срещнете грешки със сертификата
)
```

> **⚠️ Внимание:** Изключването на проверката на SSL (`connection_verify=False`) намалява сигурността, като пропуска валидирането на сертификати. Използвайте го само като временно решение в развойна среда, никога в продукция.

**Вариант 3: Инсталирайте и използвайте `truststore`**

```bash
pip install truststore
```

След това добавете следното в началото на вашия бележник или скрипт преди да правите мрежови повиквания:

```python
import truststore
truststore.inject_into_ssl()
```

## Закъсали ли сте някъде?

Ако срещнете проблеми с тази настройка, присъединете се към нашия <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">създайте проблем</a>.

## Следващ урок

Вече сте готови да стартирате кода за този курс. Приятно учене за света на AI агентите! 

[Въведение в AI агентите и случаи на използване на агентите](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->