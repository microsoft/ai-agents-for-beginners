# Постављање курса

## Увод

Ова лекција ће покрити како покренути примере кода из овог курса.

## Придружите се другим ученицима и добијте помоћ

Пре него што почнете са клонирањем свог репозиторијума, придружите се [AI Agents For Beginners Discord каналу](https://aka.ms/ai-agents/discord) да бисте добили помоћ око подешавања, поставили питања о курсу или се повезали са другим ученицима.

## Клонирајте или форкујте овај репозиторијум

Да бисте почели, молимо вас да клонирате или форкујете GitHub репозиторијум. Ово ће направити вашу верзију материјала курса како бисте могли да покрећете, тестирате и подешавате код!

Ово можете урадити кликом на линк да <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форкујете репо</a>

Сада бисте требали имати своју форкирану верзију овог курса на следећем линку:

![Forked Repo](../../../translated_images/sr/forked-repo.33f27ca1901baa6a.webp)

### Површинско клонирање (препоручено за радионице / Codespaces)

  >Пуни репозиторијум може бити велики (~3 GB) када преузмете пуну историју и све датотеке. Ако присуствујете само радионици или вам треба само неколико фолдера са лекцијама, површинско клонирање (или ређе клонирање) избегава већину тог преузимања скраћујући историју и/или прескачући blob-ове.

#### Брзо површинско клонирање — минимална историја, све датотеке

Замените `<your-username>` у доленаведеним командама својим URL-ом форка (или upstream URL ако више волите).

Да бисте клонирали само најновију историју комита (мали download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Да бисте клонирали специфичну грану:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Делимично (ређе) клонирање — минимални blob-ови + само одабрани фолдери

Ово користи делимично клонирање и sparse-checkout (захтева Git 2.25+ и препоручује се модерни Git са подршком за делимично клонирање):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Уђите у фолдер репозиторијума:

```bash|powershell
cd ai-agents-for-beginners
```

Затим наведите које фолдере желите (пример испод показује два фолдера):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Након клонирања и провере фајлова, ако вам требају само датотеке и желите да ослободите простор (нема git историје), молимо избришите метаподатке репозиторијума (💀непоправљиво — изгубићете сву Git функционалност: нема комита, пулова, пушова или приступа историји).

```bash
# зш/баш
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Коришћење GitHub Codespaces (препоручено за избегавање великих локалних преузимања)

- Направите нови Codespace за овај репо преко [GitHub UI](https://github.com/codespaces).  

- У терминалу новоотвореног Codespace покрените једну од горе наведених команди за површинско/ређе клонирање да бисте урадили само потребне фолдере са лекцијама у радни простор Codespace-а.
- Опционо: након клонирања унутар Codespaces, уклоните .git да бисте ослободили додатни простор (погледајте горе команде за уклањање).
- Напомена: Ако више волите да отворите репо директно у Codespaces (без додатног клонирања), имајте у виду да Codespaces конструише devcontainer окружење и можда ће и даље обезбедити више него што вам треба. Клонирање површинске копије унутар свежег Codespace-а даје вам већу контролу над коришћењем диска.

#### Савети

- Увек замените URL клонирања својим форком ако желите да мењате/комитујете.
- Ако вам касније затреба више историје или датотека, можете их дохватити или подесити sparse-checkout да укључи додатне фолдере.

## Покретање кода

Овај курс нуди серију Јупитер (Jupyter) бележница које можете покретати да бисте стекли практично искуство у прављењу AI агената.

Примери кода користе **Microsoft Agent Framework (MAF)** са `FoundryChatClient` који се повезује на **Microsoft Foundry Agent Service V2** (Responses API) преко **Microsoft Foundry**.

Све Python бележнице су означене као `*-python-agent-framework.ipynb`.

## Захтеви

- Python 3.12+
  - **НАПОМЕНА**: Ако немате инсталиран Python3.12, уверите се да га инсталирате. Затим креирајте виртуелно окружење користећи python3.12 да бисте осигурали да су исправне верзије инсталиране из датотеке requirements.txt.
  
    >Пример

    Креирајте Python venv директоријум:

    ```bash|powershell
    python -m venv venv
    ```

    Затим активирајте venv окружење за:

    ```bash
    # зш/баш
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: За пример кодове који користе .NET, уверите се да сте инсталирали [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или новији. Затим проверите инсталирану верзију .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Захтеван за аутентификацију. Инсталирајте са [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure претплата** — За приступ Microsoft Foundry и Microsoft Foundry Agent Service.
- **Microsoft Foundry пројекат** — Пројекат са распоређеним моделом (нпр. `gpt-5-mini`). Погледајте [Корак 1](#корак-1-креирајте-microsoft-foundry-пројекат) доле.

Укорену овог репозиторијума имамо датотеку `requirements.txt` која садржи све потребне Python пакете за покретање примера кода.

Можете их инсталирати тако што ћете покренути следећу команду у терминалу, у корену репозиторијума:

```bash|powershell
pip install -r requirements.txt
```

Препоручујемо креирање Python виртуелног окружења да бисте избегли конфликте и проблеме.

## Подешавање VSCode

Уверите се да користите исправну верзију Python-а у VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Подешавање Microsoft Foundry и Microsoft Foundry Agent Service

### Корак 1: Креирајте Microsoft Foundry пројекат

Потребан вам је Microsoft Foundry **hub** и **пројекат** са распоређеним моделом да би покренули бележнице.

1. Идите на [ai.azure.com](https://ai.azure.com) и пријавите се са својим Azure налогом.
2. Креирајте **hub** (или користите постојећи). Погледајте: [Преглед ресурса хаба](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Унутар хаба, креирајте **пројекат**.
4. Распоредите модел (нпр. `gpt-5-mini`) из **Models + Endpoints** → **Deploy model**.

### Корак 2: Преузмите URL вашег пројекта и име распоређеног модела

Из вашег пројекта у Microsoft Foundry порталу:

- **URL крајње тачке пројекта** — Идите на страницу **Overview** и копирајте URL крајње тачке.

![Project Connection String](../../../translated_images/sr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Име распоређеног модела** — Идите на **Models + Endpoints**, изаберите ваш распоређени модел и запишите **Deployment name** (нпр. `gpt-5-mini`).

### Корак 3: Пријавите се у Azure користећи `az login`

Све бележнице користе **`AzureCliCredential`** за аутентификацију — нема управљања API кључевима. Ово захтева да будете пријављени преко Azure CLI.

1. **Инсталирајте Azure CLI** ако већ нисте: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Пријавите се** покретањем:

    ```bash|powershell
    az login
    ```

    Или ако сте у удаљеном/Codespace окружењу без прегледача:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Изаберите претплату** ако будете питани — одаберите ону која садржи ваш Foundry пројекат.

4. **Проверите** да ли сте пријављени:

    ```bash|powershell
    az account show
    ```

> **Зашто `az login`?** Бележнице се аутентификују користећи `AzureCliCredential` из пакета `azure-identity`. Ово значи да ваша сесија Azure CLI пружа акредитиве — нема API кључева или тајни у вашем `.env` фајлу. Ово је [препорука за безбедност](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Корак 4: Креирајте свој `.env` фајл

Копирајте пример датотеке:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Отворите `.env` и унесите ове две вредности:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Променљива | Где је пронаћи |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry портал → ваш пројекат → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry портал → **Models + Endpoints** → име вашег распоређеног модела |

То је све за већину лекција! Бележнице ће се аутоматски аутентификовати преко ваше `az login` сесије.

### Корак 5: Инсталирајте Python зависности

```bash|powershell
pip install -r requirements.txt
```

Препоручујемо да ово покренете унутар виртуелног окружења које сте раније направили.

## Додатно подешавање за Лекцију 5 (Agentic RAG)

Лекција 5 користи **Azure AI Search** за retrieval-augmented generation. Ако планирате да покренете ту лекцију, додајте ове променљиве у свој `.env` фајл:

| Променљива | Где је пронаћи |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure портал → ваш **Azure AI Search** ресурс → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure портал → ваш **Azure AI Search** ресурс → **Settings** → **Keys** → примарни администраторски кључ |

## Додатно подешавање за лекције које директно позивају Azure OpenAI (лекције 6 и 8)

Неке бележнице у лекцијама 6 и 8 директно позивају **Azure OpenAI** (користећи **Responses API**) уместо да иду кроз Microsoft Foundry пројекат. Ови примери су раније користили GitHub моделе, који су укинути (пензионисање у јулу 2026) и не подржавају Responses API. Ако планирате да покренете те примере, додајте ове променљиве у `.env` фајл:

| Променљива | Где је пронаћи |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure портал → ваш **Azure OpenAI** ресурс → **Keys and Endpoint** → Endpoint (нпр. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Име вашег распоређеног модела (нпр. `gpt-5-mini`) који подржава Responses API |
| `AZURE_OPENAI_API_KEY` | Опционо — само ако користите автентикацију на бази кључа уместо `az login` / Entra ID |

> Responses API користи стабилни `/openai/v1/` endpoint, па није потребна `api-version`. Пријавите се са `az login` да користите keyless Entra ID аутентификацију.

## Алтернативни провајдер: MiniMax (OpenAI-Компатибилан)

[MiniMax](https://platform.minimaxi.com/) обезбеђује моделе великих контекста (до 204К токена) преко OpenAI-компатибилног API-ја. Пошто Microsoft Agent Framework-ов `OpenAIChatClient` ради са било којим OpenAI-компатибилним endpoint-ом, MiniMax можете користити као замену за Azure OpenAI или OpenAI.

Додајте ове променљиве у ваш `.env` фајл:

| Променљива | Где је пронаћи |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Користите `https://api.minimax.io/v1` (подразумевана вредност) |
| `MINIMAX_MODEL_ID` | Име модела за коришћење (нпр. `MiniMax-M3`) |

**Пример модела**: `MiniMax-M3` (препоручено), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (бржи одговори). Имена модела и доступност могу временом да се промене, а приступ одређеном моделу може зависити од вашег налога или региона — погледајте [MiniMax Platform](https://platform.minimaxi.com/) за актуелну листу. Ако `MiniMax-M3` није доступан вашем налогу, подесите `MINIMAX_MODEL_ID` на модел коме имате приступ (нпр. `MiniMax-M2.7`).

Примери кода који користе `OpenAIChatClient` (нпр. радни ток за резервације хотела у Лекцији 14) аутоматски ће детектовати и користити вашу MiniMax конфигурацију када је `MINIMAX_API_KEY` подешен.

## Алтернативни провајдер: Foundry Local (Покрените моделе на уређају)

[Foundry Local](https://foundrylocal.ai) је лагани runtime који преузима, управља и сервира језичке моделе **исключиво на вашем уређају** преко OpenAI-компатибилног API-ја — без облака, без Azure претплате и без API кључева. Одлична опција за оффлајн развој, експериментисање без трошкова за облак или чување података на уређају.

Пошто Microsoft Agent Framework-ов `OpenAIChatClient` ради са било којим OpenAI-компатибилним endpoint-ом, Foundry Local је замена за локално коришћење уместо Azure OpenAI.

**1. Инсталирајте Foundry Local**

```bash
# Виндоус
winget install Microsoft.FoundryLocal

# мацОС
brew install foundrylocal
```

**2. Преузмите и покрените модел** (ова команда такође покреће локални сервис):

```bash
foundry model list          # види расположиве моделе
foundry model run phi-4-mini
```

**3. Инсталирајте Python SDK** за проналажење локалне крајње тачке:

```bash
pip install foundry-local-sdk
```

**4. Усмерите Microsoft Agent Framework на свој локални модел:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Преузима (ако је потребно) и сервира модел локално, затим открива крајњу тачку/порт.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # нпр. http://localhost:<port>/v1
    api_key=manager.api_key,        # увек "није потребно" за Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Напомена:** Foundry Local изложи OpenAI-компатибилну крајњу тачку за **Chat Completions**. Користите је за локални развој и оффлајн сценарије. За пун скуп функција **Responses API** (државни разговори, дубока оркестрација алата и развој у стилу агента), усмерите се на **Azure OpenAI** или **Microsoft Foundry** пројекат као што је приказано у лекцијама. Погледајте [Foundry Local документацију](https://foundrylocal.ai) за актуелни каталог модела и подршку платформе.

## Додатно подешавање за Лекцију 8 (Bing Grounding радни ток)


Бележница са условним током рада у лекцији 8 користи **Bing поверљивост** преко Microsoft Foundry. Ако планирате да покренете тај пример, додајте ову променљиву у ваш `.env` фајл:

| Променљива | Где је пронаћи |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry портал → ваш пројекат → **Управљање** → **Повезани ресурси** → ваша Bing веза → копирајте ид везе |

## Решавање проблема

### Грешке везане за SSL сертификате на macOS

Ако користите macOS и наиђете на грешку као што је:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ово је познат проблем са Питхоном на macOS где системски SSL сертификати нису аутоматски поверењиви. Покушајте следећа решења по редоследу:

**Опција 1: Покрените Питхон скрипту за инсталацију сертификата (препоручено)**

```bash
# Замени 3.XX са твојом инсталираном верзијом Питона (нпр. 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Опција 2: Користите `connection_verify=False` у вашој бележници (само за GitHub Models бележнице)**

У бележници из Лекције 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), већ је укључено коментарисано решење. Уклоните коментар са `connection_verify=False` када креирате клијента:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Онемогући проверу SSL-а ако наиђеш на грешке сертификата
)
```

> **⚠️ Упозорење:** Искључивање SSL верификације (`connection_verify=False`) смањује безбедност јер прескаче проверу сертификата. Користите ово само као привремено решење у развојним окружењима, никада у продукцији.

**Опција 3: Инсталирајте и користите `truststore`**

```bash
pip install truststore
```

Затим додајте следеће на почетак ваше бележнице или скрипте пре било каквих мрежних позива:

```python
import truststore
truststore.inject_into_ssl()
```

## Заглавили сте негде?

Ако имате било каквих проблема при покретању овог подешавања, придружите се нашем <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">креирајте issue</a>.

## Следећа лекција

Сада сте спремни да покренете код за овај курс. Срећно у учењу више о свету AI агената!

[Увод у AI агенте и коришћење агената](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->