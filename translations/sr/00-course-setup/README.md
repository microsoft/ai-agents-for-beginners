# Подешавање курса

## Увод

Овај час ће обухватити како покренути примере кода овог курса.

## Придружите се другим ученицима и добијте помоћ

Пре него што почнете са клонирањем вашег репозиторијума, придружите се [AI Agents For Beginners Discord каналу](https://aka.ms/ai-agents/discord) да бисте добили помоћ при подешавању, одговоре на питања о курсу или да бисте се повезали са другим ученицима.

## Клонирајте или форкујте овај репозиторијум

За почетак, молимо вас да клонирате или форкујете GitHub репозиторијум. Ово ће вам направити вашу верзију материјала курса како бисте могли да покренете, тестирате и мењате код!

Ово можете урадити кликом на линк <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork the repo</a>

Сада бисте требали имати своју форковану верзију овог курса на следећем линку:

![Forked Repo](../../../translated_images/sr/forked-repo.33f27ca1901baa6a.webp)

### Плитко клонирање (препоручено за радионице / Codespaces)

  >Пуни репозиторијум може бити велики (~3 ГБ) када преузмете целу историју и све фајлове. Ако присуствујете само радионици или вам требају само неке фасцикле лекција, плитко клонирање (или скарачено клонирање) избегава већину тих преузимања тако што скраћује историју и/или прескаче блобове.

#### Брзо плитко клонирање — минимална историја, сви фајлови

Замените `<your-username>` у следећим командама са URL-ом вашег форка (или upstream URL-ом ако желите).

Да клонирате само најновију историју комита (мали фајл за преузимање):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Да клонирате одређену грану:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Деловно (скарачено) клонирање — минимални блобови + само одабране фасцикле

Ово користи делимично клонирање и sparse-checkout (захтева Git 2.25+ и препоручује се модерни Git са подршком за делимично клонирање):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Уђите у фасциклу репозиторијума:

```bash|powershell
cd ai-agents-for-beginners
```

Затим наведите које фасцикле желите (пример испод показује две фасцикле):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Након клонирања и провере фајлова, ако вам требају само фајлови и желите да ослободите простор (без git историје), обришите метаподатке репозиторијума (💀неповратно — изгубићете све Git функције: нема комита, прелаза, пусхова или приступа историји).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Коришћење GitHub Codespaces (препоручено за избегавање великих локалних преузимања)

- Креирајте нови Codespace за овај репозиторијум преко [GitHub UI](https://github.com/codespaces).  

- У терминалу новокреираног Codespace-а покрените једну од горе наведених команди за плитко/скарачено клонирање да бисте довели само фасцикле лекција које су вам потребне у Codespace радни простор.
- Опционо: након клонирања у Codespaces, уклоните .git да бисте ослободили додатни простор (погледајте команде за уклањање горе).
- Напомена: Ако више волите да отворите репозиторијум директно у Codespaces (без додатног клонирања), имајте у виду да Codespaces подешава devcontainer окружење и можда ће и даље припремати више него што вам треба. Клонирање плитке копије унутар свежег Codespace-а даје вам већу контролу над коришћењем диска.

#### Савети

- Увек замените URL клонирања са вашим форком ако желите да мењате/комитујете.
- Ако вам касније треба више историје или фајлова, можете их дохватити или прилагодити sparse-checkout да укључите додатне фасцикле.

## Покретање кода

Овај курс нуди серију Jupyter бележница које можете покренути како бисте стекли практично искуство у изградњи AI агената.

Примери кода користе **Microsoft Agent Framework (MAF)** са `FoundryChatClient`, који се повезује са **Microsoft Foundry Agent Service V2** (Responses API) преко **Microsoft Foundry**.

Све Python бележнице су означене са `*-python-agent-framework.ipynb`.

## Захтеви

- Python 3.12+
  - **НАПОМЕНА**: Ако немате инсталиран Python 3.12, обавезно га инсталирајте. Затим направите ваш виртуелни енвиронмент користећи python3.12 како бисте осигурали исправне верзије из `requirements.txt`.
  
    >Пример

    Креирање Python виртуелног енвиронмента:

    ```bash|powershell
    python -m venv venv
    ```

    Затим активација виртуелног оквира за:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: За пример кода који користи .NET, обавезно инсталирајте [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или новију верзију. Затим проверите инсталирану .NET SDK верзију:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Захтевано за аутентификацију. Инсталирајте са [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure претплата** — За приступ Microsoft Foundry и Microsoft Foundry Agent Service.
- **Microsoft Foundry Пројекат** — Пројекат са распоређеним моделом (нпр. `gpt-4.1-mini`). Погледајте [Корак 1](#корак-1-креирајте-microsoft-foundry-пројекат) доле.

Укључили смо `requirements.txt` фајл у корен овог репозиторијума који садржи све потребне Python пакете за покретање примера кода.

Можете их инсталирати покретањем следеће команде у вашем терминалу у корену репозиторијума:

```bash|powershell
pip install -r requirements.txt
```

Препоручујемо да направите Python виртуелно окружење да бисте избегли конфликте и проблеме.

## Подешавање VSCode

Уверите се да користите праву верзију Python-а у VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Подешавање Microsoft Foundry и Microsoft Foundry Agent Service

### Корак 1: Креирајте Microsoft Foundry Пројекат

Потребан вам је Microsoft Foundry **hub** и **проект** са распоређеним моделом за покретање бележница.

1. Идите на [ai.azure.com](https://ai.azure.com) и пријавите се са вашим Azure налогом.
2. Креирајте **hub** (или користите постојећи). Погледајте: [Pregled Hub ресурса](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Унутар hub-а, креирајте **проект**.
4. Распоредите модел (нпр. `gpt-4.1-mini`) из **Models + Endpoints** → **Deploy model**.

### Корак 2: Преузмите URL ендпоинта вашег пројекта и име распоређеног модела

Из вашег пројекта у Microsoft Foundry порталу:

- **Project Endpoint** — Идите на страницу **Overview** и копирајте URL ендпоинта.

![Project Connection String](../../../translated_images/sr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Идите на **Models + Endpoints**, изаберите распоређени модел и забележите **Deployment name** (нпр. `gpt-4.1-mini`).

### Корак 3: Пријавите се у Azure помоћу `az login`

Све бележнице користе **`AzureCliCredential`** за аутентификацију — нема API кључева које треба управљати. Ово захтева да сте пријављени преко Azure CLI-а.

1. **Инсталирајте Azure CLI** ако већ нисте: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Пријавите се** покретањем:

    ```bash|powershell
    az login
    ```

    Или ако сте у удаљеном/Codespace окружењу без прегледача:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Изаберите вашу претплату** ако вас система то затражи — изаберите ону која садржи ваш Foundry пројекат.

4. **Проверите** да ли сте пријављени:

    ```bash|powershell
    az account show
    ```

> **Зашто `az login`?** Бележнице аутентификују користећи `AzureCliCredential` из `azure-identity` пакета. То значи да ваша Azure CLI сесија обезбеђује акредитације — нема API кључева или тајни у вашем `.env` фајлу. Ово је [безбедносна најбоља пракса](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Корак 4: Креирајте ваш `.env` фајл

Копирајте пример фајл:

```bash
# зш/баш
cp .env.example .env
```

```powershell
# ПоверШел
Copy-Item .env.example .env
```

Отворите `.env` и попуните ове вредности:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

| Променљива | Где је пронаћи |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry портал → ваш пројекат → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry портал → **Models + Endpoints** → име вашег распоређеног модела |

То је све за већину лекција! Бележнице ће аутоматски аутентификовати преко ваше `az login` сесије.

### Корак 5: Инсталирајте Python зависности

```bash|powershell
pip install -r requirements.txt
```

Препоручујемо да ово покренете унутар виртуелног окружења које сте раније креирали.

## Додатно подешавање за лекцију 5 (Agentic RAG)

Лекција 5 користи **Azure AI Search** за генерацију уз подршку преузимања. Ако планирате да покренете ту лекцију, додајте ове променљиве у ваш `.env` фајл:

| Променљива | Где је пронаћи |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure портал → ваш ресурс **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure портал → ваш ресурс **Azure AI Search** → **Settings** → **Keys** → примарни администраторски кључ |

## Додатно подешавање за лекције које позивају Azure OpenAI директно (лекције 6 и 8)

Неке бележнице у лекцијама 6 и 8 директно позивају **Azure OpenAI** (користећи **Responses API**) уместо да иду кроз Microsoft Foundry пројекат. Ови примери су раније користили GitHub Models, који је застарео (планирани крај у јулу 2026) и не подржава Responses API. Ако планирате покренути те примере, додајте ове променљиве у ваш `.env` фајл:

| Променљива | Где је пронаћи |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure портал → ваш ресурс **Azure OpenAI** → **Keys and Endpoint** → Endpoint (нпр. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Име вашег распоређеног модела (нпр. `gpt-4.1-mini`) који подржава Responses API |
| `AZURE_OPENAI_API_KEY` | Опционо — само ако користите аутентификацију на бази кључа уместо `az login` / Entra ID |

> Responses API користи стабилан `/openai/v1/` енпоинт, тако да није потребан `api-version`. Пријавите се са `az login` да бисте користили аутентификацију без кључа преко Entra ID.

## Алтернативни провајдер: MiniMax (компатибилан са OpenAI)

[MiniMax](https://platform.minimaxi.com/) пружа моделе са великим контекстом (до 204К токена) преко OpenAI-компатибилног API-ја. Пошто Microsoft Agent Framework-ов `OpenAIChatClient` ради са било којим OpenAI-компатибилним енпоинтом, можете користити MiniMax као замену за Azure OpenAI или OpenAI.

Додајте ове променљиве у ваш `.env` фајл:

| Променљива | Где је пронаћи |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Користите `https://api.minimax.io/v1` (подразумевана вредност) |
| `MINIMAX_MODEL_ID` | Име модела за коришћење (нпр. `MiniMax-M3`) |

**Пример модела**: `MiniMax-M3` (препоручени), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (брже одговоре). Имена модела и доступност се могу временом мењати, а приступ одређеном моделу може зависити од вашег налога или региона — проверите [MiniMax Platform](https://platform.minimaxi.com/) за тренутну листу. Ако `MiniMax-M3` није доступан вашем налогу, подесите `MINIMAX_MODEL_ID` на модел коме имате приступ (нпр. `MiniMax-M2.7`).

Примери кода који користе `OpenAIChatClient` (нпр. Лекција 14, процес резервације хотела) аутоматски ће препознати и користити вашу MiniMax конфигурацију када је подешен `MINIMAX_API_KEY`.

## Алтернативни провајдер: Foundry Local (покретање модела локално)

[Foundry Local](https://foundrylocal.ai) је лагано окружење које преузима, управља и сервира језичке моделе **потпуно на вашем рачунару** преко OpenAI-компатибилног API-ја — без облака, без Azure претплате и без API кључева. Одлична је опција за офлајн развој, експериментисање без трошкова облака или за чување података локално.

Пошто Microsoft Agent Framework-ов `OpenAIChatClient` ради са било којим OpenAI-компатибилним енпоинтом, Foundry Local је локална алтернатива Azure OpenAI-у.

**1. Инсталирајте Foundry Local**

```bash
# Виндоус
winget install Microsoft.FoundryLocal

# мacОС
brew install foundrylocal
```

**2. Преузмите и покрените модел** (ово такође стартује локалну услугу):

```bash
foundry model list          # видети доступне моделе
foundry model run phi-4-mini
```

**3. Инсталирајте Python SDK** који се користи за откривање локалног енпоинта:

```bash
pip install foundry-local-sdk
```

**4. Поставите Microsoft Agent Framework да користи ваш локални модел:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Преузима (ако је потребно) и сервира модел локално, затим открива крајњу тачку/порт.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # нпр. http://localhost:<порт>/v1
    api_key=manager.api_key,        # увек "необавезно" за Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Напомена:** Foundry Local излаже OpenAI-компатибилни **Chat Completions** енпоинт. Користите га за локални развој и офлајн сценарије. За пуну функционалност **Responses API** (дијалози са стањем, дубока оркестрација алата и развој у стилу агента) циљајте на **Azure OpenAI** или **Microsoft Foundry** пројекат као што је показано у лекцијама. Погледајте [Foundry Local документацију](https://foundrylocal.ai) за тренутни каталог модела и подршку платформе.


## Додатна подешавања за Лекцију 8 (Bing Grounding Workflow)

Кондиционални workflow notebook у лекцији 8 користи **Bing grounding** преко Microsoft Foundry. Ако планирате да покренете тај пример, додајте ову променљиву у ваш `.env` фајл:

| Променљива | Где се налази |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry портал → ваш пројекат → **Management** → **Connected resources** → ваша Bing конекција → копирајте connection ID |

## Решавање проблема

### Грешке приликом верификације SSL сертификата на macOS

Ако користите macOS и наиђете на грешку као што је:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ово је познат проблем са Питоном на macOS-у где системски SSL сертификати нису аутоматски поверења вредни. Покушајте следећа решења по редоследу:

**Опција 1: Покрените Python скрипту Install Certificates (препоручено)**

```bash
# Замените 3.XX са вашем инсталираном верзијом Питхона (нпр. 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Опција 2: Користите `connection_verify=False` у вашем notebook-у (само за GitHub Models notebook-е)**

У notebook-у из Лекције 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) већ је укључено решење које је закоментарисано. Откоментаришите `connection_verify=False` при креирању клијента:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Онемогући SSL верификацију ако наиђеш на грешке сертификата
)
```

> **⚠️ Упозорење:** Искључивање SSL верификације (`connection_verify=False`) смањује безбедност прескачући валидацију сертификата. Користите ово само као привремено решење у развојним окружењима, никада у продукцији.

**Опција 3: Инсталирајте и користите `truststore`**

```bash
pip install truststore
```

Затим додајте следеће на врх вашег notebook-а или скрипте пре него што направите било какве мрежне позиве:

```python
import truststore
truststore.inject_into_ssl()
```

## Запели сте негде?

Ако имате било каквих проблема са покретањем овог подешавања, придружите се нашем <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord-у</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">направите issue</a>.

## Следећа лекција

Сада сте спремни да покренете код за овај курс. Срећно у даљем учењу о свету AI агената! 

[Увод у AI агенте и њихове примене](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->