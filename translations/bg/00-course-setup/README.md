# Настройка на курса

## Въведение

Този урок ще обясни как да стартирате примерния код от този курс.

## Присъединете се към други учащи и получете помощ

Преди да започнете да клонирате своя репозиторий, присъединете се към [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord), за да получите помощ с настройката, отговори на въпроси за курса или за да се свържете с други учащи.

## Клониране или форкване на този репозиторий

За да започнете, моля клонирайте или форкнете GitHub репозиторията. Това ще ви създаде собствена версия на материала от курса, така че да можете да стартирате, тествате и променяте кода!

Това може да се направи като кликнете на линка за <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкване на репото</a>

Сега трябва да имате собствен форк на този курс на следния линк:

![Forked Repo](../../../translated_images/bg/forked-repo.33f27ca1901baa6a.webp)

### Леко клониране (препоръчително за работилници / Codespaces)

  >Целият репозиторий може да е голям (~3 GB), когато изтеглите цялата история и всички файлове. Ако посещавате само работилницата или ви трябват само няколко папки с уроци, лекото клониране (или частично клониране) предотвратява изтеглянето на голяма част от историята и/или пропуска blob обекти.

#### Бързо леко клониране — минимална история, всички файлове

Заменете `<your-username>` в долните команди с URL адреса на вашия форк (или с URL адреса на upstream, ако предпочитате).

За да клонирате само последната история на комита (малко изтегляне):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

За да клонирате конкретен клон:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Частично (разредено) клониране — минимални blob обекти и само избрани папки

Това използва частично клониране и sparse-checkout (изисква Git 2.25+ и се препоръчва модерен Git с поддръжка на частично клониране):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Влезте в папката на репото:

```bash|powershell
cd ai-agents-for-beginners
```

После посочете кои папки искате (примерът по-долу показва две папки):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

След клонирането и проверката на файловете, ако ви трябват само файловете и искате да освободите място (без история на git), изтрийте метаданните на репозитория (💀невъзвратно — ще загубите цялата Git функционалност: няма комити, извличания, натискане или достъп до история).

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

- В терминала на новосъздадения кодспейс, изпълнете една от горните команди за леко/разредено клониране, за да донесете само папките с уроци, които ви трябват в работното пространство на Codespace.
- По избор: след клониране вътре в Codespaces, премахнете .git, за да освободите допълнително място (вижте командите за премахване по-горе).
- Забележка: Ако предпочитате да отворите директно репото в Codespaces (без допълнително клониране), имайте предвид, че Codespaces ще конструира devcontainer средата и може да зареди повече отколкото ви трябва. Клониране на леко копие в чист Codespace ви дава повече контрол върху използването на дисково пространство.

#### Съвети

- Винаги заменяйте URL за клониране с този на вашия форк, ако искате да редактирате/комитирате.
- Ако по-късно ви трябва повече история или файлове, можете да ги изтеглите или да нагласите sparse-checkout, за да включите допълнителни папки.

## Стартиране на кода

Този курс предлага серия от Jupyter тетрадки, които можете да стартирате, за да получите практически опит в изграждането на AI агенти.

Примерният код използва **Microsoft Agent Framework (MAF)** с `FoundryChatClient`, който се свързва с **Microsoft Foundry Agent Service V2** (отговарящият API) чрез **Microsoft Foundry**.

Всички Python тетрадки имат етикет `*-python-agent-framework.ipynb`.

## Изисквания

- Python 3.12+
  - **ЗАБЕЛЕЖКА**: Ако нямате инсталиран Python3.12, уверете се, че го инсталирате. След това създайте вашата виртуална среда с python3.12, за да сте сигурни, че се инсталират правилните версии от файла requirements.txt.
  
    >Пример

    Създайте директория за Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    След това активирайте venv средата с:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: За примерния код с .NET, уверете се, че сте инсталирали [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или по-нова версия. След това проверете версията на инсталирания .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Изисква се за автентикация. Инсталирайте от [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure абонамент** — За достъп до Microsoft Foundry и Microsoft Foundry Agent Service.
- **Microsoft Foundry проект** — Проект с разположен модел (напр. `gpt-5-mini`). Вижте [Стъпка 1](#стъпка-1-създаване-на-microsoft-foundry-проект) по-долу.

В корена на този репозиторий сме включили файл `requirements.txt`, който съдържа всички необходими Python пакети за стартиране на примерния код.

Можете да ги инсталирате, като стартирате следната команда в терминала си в корена на репото:

```bash|powershell
pip install -r requirements.txt
```

Препоръчваме ви да създадете Python виртуална среда, за да избегнете конфликти и проблеми.

## Настройване на VSCode

Уверете се, че използвате правилната версия на Python във VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Настройка на Microsoft Foundry и Microsoft Foundry Agent Service

### Стъпка 1: Създаване на Microsoft Foundry проект

Трябва ви Microsoft Foundry **hub** и **проект** с разположен модел, за да стартирате тетрадките.

1. Отидете на [ai.azure.com](https://ai.azure.com) и влезте със своя Azure акаунт.
2. Създайте **hub** (или използвайте съществуващ). Вижте: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Вътре в hub-а създайте **проект**.
4. Разположете модел (например `gpt-5-mini`) от **Models + Endpoints** → **Deploy model**.

### Стъпка 2: Вземете своя проектен крайна точка и име на разполагане на модела

От вашия проект в портала на Microsoft Foundry:

- **Project Endpoint** — Отидете на страницата **Overview** и копирайте URL на крайна точка.

![Project Connection String](../../../translated_images/bg/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Отидете на **Models + Endpoints**, изберете своя разположен модел и запишете **Deployment name** (напр. `gpt-5-mini`).

### Стъпка 3: Влезте в Azure с `az login`

Всички тетрадки използват **`AzureCliCredential`** за автентикация — няма нужда да управлявате API ключове. Това изисква да сте влезли през Azure CLI.

1. **Инсталирайте Azure CLI**, ако не сте го направили: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Влезте** като стартирате:

    ```bash|powershell
    az login
    ```

    Или ако сте в отдалечена/Codespace среда без браузър:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Изберете своя абонамент**, ако ви попита — изберете този, съдържащ вашия Foundry проект.

4. **Потвърдете**, че сте влезли:

    ```bash|powershell
    az account show
    ```

> **Защо `az login`?** Тетрадките се автентикират чрез `AzureCliCredential` от пакета `azure-identity`. Това означава, че вашата Azure CLI сесия осигурява идентификацията — без API ключове или тайни във вашия `.env` файл. Това е [най-добра практика за сигурност](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Стъпка 4: Създайте своя `.env` файл

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
| `AZURE_AI_PROJECT_ENDPOINT` | Портал на Foundry → вашият проект → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Портал на Foundry → **Models + Endpoints** → името на вашия разположен модел |

Това е всичко за повечето уроци! Тетрадките ще се автентикират автоматично чрез вашата сесия `az login`.

### Стъпка 5: Инсталирайте Python зависимости

```bash|powershell
pip install -r requirements.txt
```

Препоръчваме да изпълните това вътре във виртуалната среда, която създадохте по-рано.

## Допълнителна настройка за урок 5 (Agentic RAG)

Урок 5 използва **Azure AI Search** за генериране с разширено извличане. Ако планирате да изпълните този урок, добавете тези променливи към своя `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Портал на Azure → вашият ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Портал на Azure → вашият ресурс **Azure AI Search** → **Settings** → **Keys** → първичен администраторски ключ |

## Допълнителна настройка за уроци, които използват директно Azure OpenAI (уроци 6 и 8)

Някои тетрадки в уроци 6 и 8 извикват **Azure OpenAI** директно (чрез **Responses API**) вместо чрез Microsoft Foundry проект. Тези примери по-рано са използвали GitHub Models, които са остарели (прекратяващи поддръжка през юли 2026) и не поддържат Responses API. Ако планирате да използвате тези примери, добавете тези променливи към своя `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Портал на Azure → вашия ресурс **Azure OpenAI** → **Keys and Endpoint** → Endpoint (напр. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Името на разположения модел (напр. `gpt-5-mini`), който поддържа Responses API |
| `AZURE_OPENAI_API_KEY` | По избор — само ако използвате удостоверяване с ключ вместо `az login` / Entra ID |

> Responses API използва стабилната крайна точка `/openai/v1/`, така че не се изисква `api-version`. Влезте с `az login`, за да използвате удостоверяване без ключ с Entra ID.

## Алтернативен доставчик: MiniMax (съвместим с OpenAI)

[MiniMax](https://platform.minimaxi.com/) предоставя модели с голям контекст (до 204K токена) чрез API, съвместимо с OpenAI. Тъй като Microsoft Agent Framework `OpenAIChatClient` работи с всяка крайна точка, съвместима с OpenAI, можете да използвате MiniMax като директна алтернатива на Azure OpenAI или OpenAI.

Добавете тези променливи към вашия `.env` файл:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API ключове |
| `MINIMAX_BASE_URL` | Използвайте `https://api.minimax.io/v1` (по подразбиране) |
| `MINIMAX_MODEL_ID` | Име на модела за използване (напр., `MiniMax-M3`) |

**Примерни модели**: `MiniMax-M3` (препоръчително), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (по-бързи отговори). Имената на моделите и наличността им може да се променят с времето, а достъпът до даден модел може да зависи от вашия акаунт или регион — проверете [MiniMax Platform](https://platform.minimaxi.com/) за актуален списък. Ако `MiniMax-M3` не е наличен за вашия акаунт, задайте `MINIMAX_MODEL_ID` на модел, до който имате достъп (напр. `MiniMax-M2.7`).

Примерният код, който използва `OpenAIChatClient` (например работния процес за резервация на хотел в урок 14), автоматично ще открие и използва вашата MiniMax конфигурация, когато `MINIMAX_API_KEY` е зададен.

## Алтернативен доставчик: Foundry Local (стартиране на модели на устройството)

[Foundry Local](https://foundrylocal.ai) е лека среда за изпълнение, която изтегля, управлява и предоставя езикови модели **изцяло на вашата машина** чрез API, съвместимо с OpenAI — без облак, без Azure абонамент и без API ключове. Това е чудесна опция за офлайн разработка, експериментиране без облачни разходи или за съхранение на данни на устройството.

Тъй като Microsoft Agent Framework-ът `OpenAIChatClient` работи с всяка OpenAI-съвместима крайна точка, Foundry Local е директна локална алтернатива на Azure OpenAI.

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

**3. Инсталирайте Python SDK-то**, използвано за откриване на локалната крайна точка:

```bash
pip install foundry-local-sdk
```

**4. Насочете Microsoft Agent Framework към локалния модел:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Изтегля (ако е необходимо) и обслужва модела локално, след което открива крайната точка/порта.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # напр. http://localhost:<port>/v1
    api_key=manager.api_key,        # винаги "не е задължително" за Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Забележка:** Foundry Local предоставя OpenAI-съвместима крайна точка за **Chat Completions**. Използвайте я за локална разработка и офлайн сценарии. За пълния набор от функции на **Responses API** (състояниеви разговори, дълбока оркестрация на инструменти и агентски стил на разработка) насочете към **Azure OpenAI** или **Microsoft Foundry** проект, както е показано в уроците. Вижте [Foundry Local документацията](https://foundrylocal.ai) за актуален каталог на модели и поддръжка на платформи.

## Допълнителна настройка за урок 8 (работен процес Bing Grounding)


Учебникът за условния работен процес в урок 8 използва **Bing grounding** чрез Microsoft Foundry. Ако планирате да стартирате този пример, добавете тази променлива във вашия файл `.env`:

| Променлива | Къде да я намерите |
|----------|-----------------|
| `BING_CONNECTION_ID` | Портал Microsoft Foundry → вашия проект → **Management** → **Connected resources** → вашата Bing връзка → копирайте connection ID |

## Отстраняване на проблеми

### Грешки при верификация на SSL сертификати на macOS

Ако използвате macOS и срещнете грешка като:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Това е известен проблем с Python на macOS, при който системните SSL сертификати не се доверяват автоматично. Опитайте следните решения по ред:

**Вариант 1: Стартирайте скрипта за инсталиране на сертификати на Python (препоръчително)**

```bash
# Заменете 3.XX с инсталираната версия на Python (напр. 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Вариант 2: Използвайте `connection_verify=False` във вашия учебник (само за GitHub Models учебници)**

В учебника от урок 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) вече има закоментирано решение. Декоментирайте `connection_verify=False` при създаването на клиента:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Деактивирайте проверката на SSL, ако срещнете грешки с сертификата
)
```

> **⚠️ Внимание:** Изключването на SSL проверката (`connection_verify=False`) намалява сигурността, като пропуска валидирането на сертификата. Използвайте това само като временно решение в среди за разработка, никога в продукция.

**Вариант 3: Инсталирайте и използвайте `truststore`**

```bash
pip install truststore
```

След това добавете следното в началото на вашия учебник или скрипт преди да правите мрежови обаждания:

```python
import truststore
truststore.inject_into_ssl()
```

## Закъсали ли сте някъде?

Ако имате проблеми с изпълнението на тази настройка, присъединете се към нашия <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">създайте проблем</a>.

## Следващ урок

Вече сте готови да стартирате кода за този курс. Желая ви приятно учене за света на AI агентите!

[Въведение в AI агентите и случаи на използване на агенти](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->