# Настройка на курса

## Въведение

Този урок ще обясни как да стартирате примерния код от курса.

## Присъединете се към други обучаващи се и получете помощ

Преди да започнете с клонирането на вашето репо, присъединете се към [AI Agents For Beginners Discord канала](https://aka.ms/ai-agents/discord), за да получите помощ с настройването, въпроси относно курса или за да се свържете с други обучаващи се.

## Клонирайте или Форкнете това Репо

За да започнете, моля, клонирайте или форкнете GitHub хранилището. Това ще създаде ваша собствена версия на учебния материал, така че да може да пускате, тествате и променяте кода!

Това може да стане като кликнете върху линка за <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкване на репото</a>

Сега трябва да имате своя собствена форкната версия на този курс на следния линк:

![Forked Repo](../../../translated_images/bg/forked-repo.33f27ca1901baa6a.webp)

### Повърхностно Клониране (препоръчително за работилници / Codespaces)

  >Пълното хранилище може да е голямо (~3 GB), ако изтеглите цялата история и всички файлове. Ако участвате само в работилницата или ви трябват само няколко папки с уроци, повърхностно клониране (или частично клониране) изтегля много по-малко.

#### Бързо повърхностно клониране — минимална история, всички файлове

Заменете `<your-username>` в командите по-долу с URL на вашия форк (или на главното репо, ако предпочитате).

За да клонирате само най-новата история на комитите (малко теглене):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

За да клонирате конкретен клон:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частично (sparse) клониране — минимални blob файлове + само избрани папки

Това използва частично клониране и sparse-checkout (изисква Git 2.25+ и препоръчителен модерен Git с поддръжка на частично клониране):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Влезте в папката на репото:

```bash
cd ai-agents-for-beginners
```

След това посочете кои папки искате (примерът по-долу показва две папки):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

След като клонирате и проверите файловете, ако искате само файлове и да освободите пространство (без git история), моля, изтрийте метаданните на репото (💀необратимо — ще загубите цялата Git функционалност):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Използване на GitHub Codespaces (препоръчително за избягване на големи локални тегления)

- Създайте нов Codespace за това репо чрез [GitHub потребителския интерфейс](https://github.com/codespaces).  

- В терминала на новосъздадения кодспейс стартирайте някоя от повърхностните или sparse клониращи команди по-горе, за да внесете само папките с уроци, които ви трябват в работното пространство на Codespace.
- По избор: след клониране вътре в Codespaces, премахнете .git, за да възстановите допълнително пространство (вижте командите за премахване по-горе).
- Забележка: Ако предпочитате да отворите репото директно в Codespaces (без допълнително клониране), имайте предвид, че Codespaces ще създаде devcontainer средата и може да зарежда повече от необходимото.

#### Съвети

- Винаги сменяйте URL за клониране с вашето форкване, ако искате да редактирате/комитирате.
- Ако по-късно ви трябва повече история или файлове, може да ги изтеглите или да настроите sparse-checkout за включване на допълнителни папки.

## Стартиране на кода

Този курс предлага серия от Jupyter Notebook файлове, които може да стартирате, за да придобиете практически опит в изграждането на AI агенти.

Примерите използват **Microsoft Agent Framework (MAF)** с `FoundryChatClient`, който се свързва с **Microsoft Foundry Agent Service V2** (API за отговори) чрез **Microsoft Foundry**.

Всички Python тетрадки са означени `*-python-agent-framework.ipynb`.

## Изисквания

- Python 3.12+
  - **ЗАБЕЛЕЖКА**: Ако нямате инсталиран Python3.12, уверете се, че го инсталирате. След това създайте виртуална среда (venv) с python3.12, за да бъдат инсталирани правилните версии от файла requirements.txt.
  
    >Пример

    Създайте директория за Python виртуална среда:

    ```bash
    python -m venv venv
    ```

    Активирайте виртуалната среда за:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: За примерния код с .NET, уверете се, че сте инсталирали [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или по-нова версия. След това проверете версията на инсталирания .NET SDK:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Необходим за автентикация. Инсталирайте от [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Абонамент** — За достъп до Microsoft Foundry и Microsoft Foundry Agent Service.
- **Microsoft Foundry Проект** — Проект с разположен модел (напр. `gpt-5-mini`). Вижте [Стъпка 1](#стъпка-1-създайте-microsoft-foundry-проект) по-долу.

Включили сме файл `requirements.txt` в корена на това хранилище с всички необходими Python пакети за стартиране на примерния код.

Можете да ги инсталирате като изпълните следната команда в терминала си в корена на репото:

```bash
pip install -r requirements.txt
```

Препоръчваме да създадете Python виртуална среда, за да избегнете конфликт и проблеми.

## Настройка на VSCode

Уверете се, че използвате правилната версия на Python във VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка на Microsoft Foundry и Microsoft Foundry Agent Service

### Стъпка 1: Създайте Microsoft Foundry Проект

Трябва да имате Microsoft Foundry **hub** и **проект** с разположен модел, за да стартирате тетрадките.

1. Отидете на [ai.azure.com](https://ai.azure.com) и влезте с вашия Azure акаунт.
2. Създайте **hub** (или използвайте съществуващ). Вижте: [Преглед на hub ресурсите](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. В hub-а създайте **проект**.
4. Разположете модел (напр. `gpt-5-mini`) от **Models + Endpoints** → **Deploy model**.

### Стъпка 2: Вземете адреса на крайна точка и името на разположения модел

От вашия проект в Microsoft Foundry портала:

- **Project Endpoint** — Отидете на страницата **Overview** и копирайте URL адреса на крайна точка.

![Project Connection String](../../../translated_images/bg/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Отидете на **Models + Endpoints**, изберете разположения модел и забележете **Deployment name** (напр. `gpt-5-mini`).

### Стъпка 3: Влезте в Azure с `az login`

Повечето тетрадки се удостоверяват чрез вашето **Azure CLI вписване** — използвайки `AzureCliCredential` или `DefaultAzureCredential` (и двете ползват вашата `az login` сесия) от пакета `azure-identity` — така че не изискват API ключове. Някои уроци и опционални интеграции използват API ключове; проверете изискванията на всеки урок за допълнителни променливи на средата. Това изисква да сте вписани чрез Azure CLI.

1. **Инсталирайте Azure CLI**, ако още не сте: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Влезте** като изпълните:

    ```bash
    az login
    ```

    Или ако сте в отдалечена/кодспейс среда без браузър:

    ```bash
    az login --use-device-code
    ```

3. **Изберете вашия абонамент** ако бъдете попитани — изберете този, който съдържа вашия Foundry проект.

4. **Проверете** дали сте вписани:

    ```bash
    az account show
    ```

> **Защо `az login`?** Тетрадките се удостоверяват чрез `AzureCliCredential` (или `DefaultAzureCredential`, който също използва вашето Azure CLI вписване) от пакета `azure-identity`. Това означава, че вашата Azure CLI сесия предоставя идентификационните данни — не са нужни API ключове или тайни във вашия `.env` файл. Това е [добра практика за сигурност](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Стъпка 4: Създайте файл `.env`

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Променлива | Къде да я намерите |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry портал → вашият проект → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry портал → **Models + Endpoints** → името на вашия разположен модел |

Това е за повечето уроци! Тетрадките ще се удостоверяват автоматично чрез вашата `az login` сесия.

### Стъпка 5: Инсталирайте Python зависимости

```bash
pip install -r requirements.txt
```

Препоръчваме да изпълните това вътре във виртуалната среда, която създадохте по-рано.

## Опционална настройка: Azure AI Search (Уроци 5 и 16)

Урок 5 (Agentic RAG) и урок 16 се изпълняват веднага с **паметен знание базиран индекс** — без нужда от допълнителни Azure ресурси. Ако искате да ги подпомогнете с реален **Azure AI Search** индекс, имайте предвид, че **тетрадката от урок 16 използва в момента удостоверяване с ключ**: тя преминава от паметно търсене към Azure AI Search само когато **и двата** `AZURE_SEARCH_SERVICE_ENDPOINT` **и** `AZURE_SEARCH_API_KEY` са зададени, иначе остава с паметното търсене — затова за да го стартирате с реален индекс трябва също да зададете и администраторския ключ. Безключовото удостоверяване с Microsoft Entra ID (RBAC) е препоръчителният подход за вашия собствен продукционен код, съответстващ на потока „az login“, използван навсякъде в този курс.

Стъпките с RBAC по-долу важат за примерите от наръчника и вашия собствен код. Те не активират безключово удостоверяване в тетрадката на урок 16; урок 16 все още изисква и крайна точка, и администраторски ключ за използване на Azure AI Search.

1. **Активирайте контрол на достъпа на базата на роли** на вашата търсеща услуга:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Присвоете си необходимите роли** (създаване/зареждане на индекси и заявки):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Добавете крайна точка** във вашия `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure портал → вашия **Azure AI Search** ресурс → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Задължително (с крайна точка) за активиране на Azure AI Search в тетрадката на урок 16, която използва удостоверяване с ключ. Azure портал → **Настройки** → **Ключове** → първичен администраторски ключ |

> **Защо безключово?** Администраторските ключове дават пълен достъп за запис на вашата търсеща услуга и могат да изтекат през `.env` файлове. С RBAC вместо това се използва вашата идентичност от `az login` — същият безключов Entra ID модел, който използват учебните тетрадки (чрез `AzureCliCredential` / `DefaultAzureCredential`). Вижте [Свързване към Azure AI Search с роли](https://learn.microsoft.com/azure/search/search-security-rbac).

Вижте [Azure AI Search наръчника за настройка](./AzureSearch.md) за пълни примери за създаване на индекс в Python и .NET.

## Допълнителна настройка за уроци, които извикват Azure OpenAI директно (Уроки 6 и 8)

Някои тетрадки в уроци 6 и 8 извикват **Azure OpenAI** директно (използвайки **Responses API**), а не през Microsoft Foundry проект. Тези примери по-рано използваха GitHub Models, което е остаряло и не поддържа Responses API. Добавете тези променливи във вашия `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure портал → вашия **Azure OpenAI** ресурс → **Keys and Endpoint** → Крайна точка (напр. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Името на вашия разположен модел (напр. `gpt-5-mini`), който поддържа Responses API |
| `AZURE_OPENAI_API_KEY` | По избор — само ако използвате удостоверяване с ключ вместо `az login` / Entra ID |

> Responses API използва стабилната крайна точка `/openai/v1/`, затова не е необходим параметър `api-version`. Влезте с `az login`, за да ползвате безключово удостоверяване с Entra ID.

## Алтернативен доставчик: MiniMax (съвместим с OpenAI)

[MiniMax](https://platform.minimaxi.com/) предоставя модели с голям контекст (до 204K токена) чрез съвместим с OpenAI API. Тъй като Microsoft Agent Framework`OpenAIChatClient` работи с всяка крайна точка, съвместима с OpenAI, можете да използвате MiniMax като заместител за уроци, които използват `OpenAIChatClient`.

Добавете тези променливи във вашия `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Платформа](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Използвайте `https://api.minimax.io/v1` (по подразбиране) |
| `MINIMAX_MODEL_ID` | Име на модела за използване (напр. `MiniMax-M3`) |

**Примерни модели**: `MiniMax-M3` (препоръчван), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (по-бързи отговори). Имената на моделите и тяхната наличност могат да се сменят във времето, а достъпът до определен модел може да зависи от вашия акаунт.

Примерите с код, които използват `OpenAIChatClient` (напр. работния процес за резервация на хотел от урок 14) автоматично ще разпознаят и използват вашата MiniMax конфигурация, когато е зададен `MINIMAX_API_KEY`.


## Алтернативен доставчик: Novita AI (съвместим с OpenAI)

[Novita AI](https://novita.ai/llm-api) предоставя API съвместим с OpenAI за отворени и най-нови езикови модели (DeepSeek, Llama, Qwen и други). Тъй като `OpenAIChatClient` в Microsoft Agent Framework работи с всяка крайна точка, съвместима с OpenAI, можете да използвате Novita AI като директна алтернатива на Azure OpenAI или OpenAI.

Добавете тези променливи във вашия файл `.env`:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `NOVITA_API_KEY` | [Табло Novita AI](https://novita.ai/settings/key-management) → API ключове |
| `NOVITA_BASE_URL` | Използвайте `https://api.novita.ai/openai/v1` (по подразбиране) |
| `NOVITA_MODEL_ID` | Име на модела, който ще използвате (например `moonshotai/kimi-k3`) |

**Примери за модели**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI хоства и много други семейства от отворени модели (Llama, Qwen, GLM и др.) — разгледайте [библиотеката с модели на Novita AI](https://novita.ai/llm-api) за актуален списък на наличните модели и техните ID-та.

Текущите примери не използват автоматично променливите `NOVITA_*`. За да използвате Novita AI, подайте тези стойности изрично при конструиране на `OpenAIChatClient` в изпълнявания пример.

## Алтернативен доставчик: Foundry Local (Изпълнение на модели на устройството)

[Foundry Local](https://foundrylocal.ai) е лек сървър за изпълнение, който сваля, управлява и обслужва езикови модели **изцяло на вашия собствен компютър** чрез API, съвместимо с OpenAI — без необходимост от облак.

Тъй като `OpenAIChatClient` на Microsoft Agent Framework работи с всяка крайна точка, съвместима с OpenAI, Foundry Local е локална директна алтернатива на Azure OpenAI.

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

**3. Инсталирайте Python SDK**, използван за откриване на локалната крайна точка:

```bash
pip install foundry-local-sdk
```

**4. Насочете Microsoft Agent Framework към вашия локален модел:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Изтегля (ако е необходимо) и предоставя модела локално, след което открива крайна точка/порт.
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

> **Забележка:** Foundry Local предоставя OpenAI-съвместима крайна точка за **Chat Completions**. Използвайте я за локална разработка и офлайн сценарии. За пълния набор от функции на **Responses API** (състояние на разговорите и др.) използвайте Azure OpenAI или проект на Microsoft Foundry.

## Допълнителна настройка за урок 8 (Бинг Grounding Workflow)

Условният работен поток в урок 8 използва **Bing grounding** чрез Microsoft Foundry. Ако планирате да изпълните този пример, добавете тази променлива във вашия `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `BING_CONNECTION_ID` | Портал Microsoft Foundry → вашия проект → **Management** → **Connected resources** → вашата Бинг връзка → копирайте ID на връзката |

## Отстраняване на проблеми

### Грешки при проверка на SSL сертификат на macOS

Ако сте на macOS и получите грешка като:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Това е известен проблем с Python на macOS, където системните SSL сертификати не се доверяват автоматично. Опитайте следните решения по ред:

**Опция 1: Стартирайте скрипта Install Certificates на Python (препоръчително)**

```bash
# Заменете 3.XX с инсталираната версия на Python (например, 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Опция 2: Използвайте `connection_verify=False` във вашия ноутбук (само за GitHub Models notebooks)**

В ноутбука за урок 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) вече има коментирано решение. Декоментирайте `connection_verify=False`, когато срещнете грешки със сертификат:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Деактивирайте проверката на SSL, ако срещнете грешки с сертификата
)
```

> **⚠️ Внимание:** Изключването на SSL проверката (`connection_verify=False`) намалява сигурността, като пропуска валидирането на сертификатите. Използвайте това само като временно решение в развойна среда. Никога не го използвайте в продукция.

**Опция 3: Инсталирайте и използвайте `truststore`**

```bash
pip install truststore
```

След това добавете следното в началото на вашия ноутбук или скрипт преди да правите каквито и да било мрежови повиквания:

```python
import truststore
truststore.inject_into_ssl()
```

## Застрянали ли сте някъде?

Ако имате някакви проблеми с тази настройка, присъединете се към нашия <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">създайте въпрос</a>.

## Следващ урок

Вече сте готови да стартирате кода за този курс. Приятно учене в света на AI агентите!

[Въведение в AI агентите и техните употреби](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->