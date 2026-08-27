# Подешавање курса

## Увод

У овом лекцији покрићемо како покренути примере кода овог курса.

## Придружите се другим ученицима и затражите помоћ

Пре него што почнете да клонирате свој репозиторијум, придружите се [AI Agents For Beginners Discord каналу](https://aka.ms/ai-agents/discord) да бисте добили било какву помоћ са подешавањем, поставили питања о курсу или се повезали са другим ученицима.

## Клонирајте или форкујте овај репозиторијум

Да бисте почели, молимо вас да клонирате или форкујете GitHub репозиторијум. Ово ће направити вашу верзију материјала курса тако да можете да покрећете, тестирате и подешавате код!

Ово можете урадити кликом на линк за <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форковање репозиторијума</a>

Сада би требало да имате своју форковану верзију овог курса на следећем линку:

![Forked Repo](../../../translated_images/sr/forked-repo.33f27ca1901baa6a.webp)

### Плитко клонирање (препоручује се за радионице / Codespaces)

  >Потпуни репозиторијум може бити велики (~3 ГБ) када преузмете целу историју и све фајлове. Ако идете само на радионицу или вам требају само неки фасцикли лекција, плитко клонирање (или ретко клонирање) преузима много мање.

#### Брзо плитко клонирање — минимална историја, сви фајлови

Замените `<your-username>` у командaма испод URL-ом вашег форка (или URL-ом upstream ако више волите).

Да клонирате само најновију историју комита (мали преузимање):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

За клонирање одређене гране:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Делимично (ретко) клонирање — минимални blob фајлови + само изабране фасцикле

Ово користи делимично клонирање и sparse-checkout (потребан Git 2.25+ и препоручен модерни Git са подршком за делимично клонирање):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Уђите у фасциклу репозиторијума:

```bash
cd ai-agents-for-beginners
```

Затим назначите које фасцикле желите (пример испод показује две фасцикле):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Након клонирања и провере фајлова, ако вам требају само фајлови и желите да ослободите простор (без Git историје), обришите метаподатке репозиторијума (💀непоправљиво — изгубићете сву Git функционалност):

```bash
# зш/баш
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Коришћење GitHub Codespaces (препоручује се да се избегне велико локално преузимање)

- Направите нови Codespace за овај репо преко [GitHub UI](https://github.com/codespaces).  

- У терминалу новокреираног codespace-а, покрените једну од горе наведених команда плитког/ретког клонирања да вучете само потребне фасцикле курсева у workspace Codespace-а.
- Опционо: након клонирања унутар Codespaces-а, уклоните .git да бисте ослободили додатни простор (погледајте команде за брисање изнад).
- Напомена: ако више волите да отворите репозиториј директно у Codespaces (без додатног клонирања), имајте на уму да ће Codespaces конструисати devcontainer окружење и можда ће припремити више него што вам треба.

#### Савети

- Увек замените URL за клонирање са вашим форком ако желите да уређујете/комитујете.
- Ако вам касније затреба више историје или фајлова, можете их дохватити или подесити sparse-checkout да укључите додатне фасцикле.

## Покретање кода

Овај курс нуди серију Jupyter свезака које можете покретати да бисте стекли практично искуство у изградњи AI агената.

Примери кода користе **Microsoft Agent Framework (MAF)** са `FoundryChatClient`, који се повезује са **Microsoft Foundry Agent Service V2** (Responses API) преко **Microsoft Foundry**.

Сви Python свезци имају ознаку `*-python-agent-framework.ipynb`.

## Захтеви

- Python 3.12+
  - **НАПОМЕНА**: Ако немате инсталиран Python3.12, обавезно га инсталирајте. Затим направите своје виртуелно окружење користећи python3.12 да бисте осигурали да се инсталирају исправне верзије из requirements.txt фајла.
  
    >Пример

    Направите Python venv директоријум:

    ```bash
    python -m venv venv
    ```

    Затим активирајте venv окружење за:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: За пример кодове који користе .NET, инсталирајте [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или новију верзију. Затим проверите инсталирану верзију .NET SDK-а:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Потребан за аутентификацију. Инсталирајте са [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure претплата** — За приступ Microsoft Foundry и Microsoft Foundry Agent Service.
- **Microsoft Foundry пројекат** — Пројекат са развијеним моделом (нпр. `gpt-5-mini`). Погледајте [Први корак](#корак-1-направите-microsoft-foundry-пројекат) доле.

Укључили смо `requirements.txt` фајл у корен овог репозиторијума који садржи све потребне Python пакете за покретање примера кода.

Можете их инсталирати покретањем следеће команде у терминалу у корену репозиторијума:

```bash
pip install -r requirements.txt
```

Препоручујемо креирање виртуелног Python окружења да избегнете било какве конфликте и проблеме.

## Постављање VSCode

Уверите се да користите исправну верзију Python-а у VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Подешавање Microsoft Foundry и Microsoft Foundry Agent Service

### Корак 1: Направите Microsoft Foundry Пројекат

Потребан вам је Microsoft Foundry **хаб** и **пројекат** са развијеним моделом да бисте покретали свезке.

1. Идите на [ai.azure.com](https://ai.azure.com) и пријавите се са својим Azure налогом.
2. Направите **хаб** (или искористите постојећи). Погледајте: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. У оквиру хаба направите **пројекат**.
4. Распоредите модел (нпр. `gpt-5-mini`) из **Models + Endpoints** → **Deploy model**.

### Корак 2: Преузмите URL пројектног ендпоинта и име распоређеног модела

Из вашег пројекта у Microsoft Foundry порталу:

- **Project Endpoint** — Идите на страницу **Overview** и копирајте URL ендпоинта.

![Project Connection String](../../../translated_images/sr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Идите на **Models + Endpoints**, изаберите свој распоређени модел и забележите име распоређивања (нпр. `gpt-5-mini`).

### Корак 3: Пријавите се у Azure преко `az login`

Већина свезака се аутентификује путем вашег **Azure CLI пријављивања** — користећи `AzureCliCredential` или `DefaultAzureCredential` (оба преузимају вашу `az login` сесију) из пакета `azure-identity` — тако да не захтевају API кључеве. Неки лекције и опционе интеграције користе API кључеве; погледајте претпоставке по свакој лекцији за додатне променљиве окружења. Ово захтева да сте пријављени преко Azure CLI.

1. **Инсталирајте Azure CLI** ако већ нисте: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Пријавите се** покретањем:

    ```bash
    az login
    ```

    Или ако сте у удаљеном/Codespace окружењу без прегледача:

    ```bash
    az login --use-device-code
    ```

3. **Изаберите своју претплату** ако добијете упит — одаберите онај који садржи ваш Foundry пројекат.

4. **Проверите** да ли сте пријављени:

    ```bash
    az account show
    ```

> **Зашто `az login`?** Свезци се аутентификују коришћењем `AzureCliCredential` (или `DefaultAzureCredential`, који такође преузима ваше Azure CLI пријављивање) из пакета `azure-identity`. То значи да ваша Azure CLI сесија даје креденцијале — нема API кључева или тајни у вашем `.env` фајлу. Ово је [ајте најбоља безбедносна пракса](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Корак 4: Направите ваш `.env` фајл

Копирајте пример фајл:

```bash
# зш/баш
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Отворите `.env` и попуните ове две вредности:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Променљива | Где је пронаћи |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry портал → ваш пројекат → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry портал → **Models + Endpoints** → име вашег распоређеног модела |

То је све за већину лекција! Свезци ће се аутоматски аутентификовати кроз вашу `az login` сесију.

### Корак 5: Инсталирајте Python зависности

```bash
pip install -r requirements.txt
```

Препоручујемо да ово покренете унутар виртуелног окружења које сте претходно креирали.

## Опционо Подешавање: Azure AI Search (лекције 5 и 16)

Лекције 5 (Agentic RAG) и 16 свезци раде одмах са **in-memory knowledge base** — није потребно додатно Azure ресурсa. Ако желите да их подржите стварним **Azure AI Search** индексом, напомињемо да **лекција 16 тренутно користи аутентификацију на основу кључева**: пребацује се са in-memory претраге на Azure AI Search само када су подешене **и** `AZURE_SEARCH_SERVICE_ENDPOINT` **и** `AZURE_SEARCH_API_KEY`, иначе остаје на in-memory претрази — тако да за коришћење стварног индекса морате поставити и администраторски кључ. Аутентификација без кључева путем Microsoft Entra ID (RBAC) је препоручена метода за ваш производни код, у складу са `az login` током који се користи широм овог курса.

RBAC кораци испод важе за примере из овог водича и ваш код. Не омогућавају аутентификацију без кључева у лекцији 16; лекција 16 и даље захтева и ендпоинт и администраторски кључ да би користила Azure AI Search.

1. **Омогућите приступ заснован на улогама (RBAC)** на вашем сервису за претрагу:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Доделите себи потребне улоге** (креирање/учитавање индекса и упити):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Додајте ендпоинт** у ваш `.env` фајл:

| Променљива | Где је пронаћи |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure портал → ваш **Azure AI Search** ресурс → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Потребно (уз ендпоинт) за омогућавање Azure AI Search у лекцији 16, која користи аутентификацију на основу кључева. Azure портал → **Settings** → **Keys** → примарни администраторски кључ |

> **Зашто без кључева?** Администраторски кључеви пружају пун приступ за писање на ваш сервис за претрагу и могу се процурити преко `.env` фајлова. Са RBAC, користи се ваша `az login` идентитет — исти модел без кључева који користе свезци курса (путем `AzureCliCredential` / `DefaultAzureCredential`). Погледајте [Повежите се на Azure AI Search користећи улоге](https://learn.microsoft.com/azure/search/search-security-rbac).

Погледајте [водич за подешавање Azure AI Search](./AzureSearch.md) за потпуне примере креирања индекса у Python-у и .NET-у.

## Додатно подешавање за лекције које директно позивају Azure OpenAI (лекције 6 и 8)

Неки свезци у лекцијама 6 и 8 директно позивају **Azure OpenAI** (користећи **Responses API**) уместо да иду кроз Microsoft Foundry пројекат. Ови примери раније су користили GitHub Models, који је застарео и не подржава Responses API. Додајте ове променљиве у свој `.env` фајл:

| Променљива | Где је пронаћи |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure портал → ваш **Azure OpenAI** ресурс → **Keys and Endpoint** → Endpoint (нпр. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Име вашег распоређеног модела (нпр. `gpt-5-mini`) који подржава Responses API |
| `AZURE_OPENAI_API_KEY` | Опционо — само ако користите аутентификацију засновану на кључу уместо `az login` / Entra ID |

> Responses API користи стабилан `/openai/v1/` ендпоинт, тако да `api-version` није потребан. Пријавите се преко `az login` за коришћење аутентификације без кључева преко Entra ID.

## Алтернативни провајдер: MiniMax (компатибилан са OpenAI)

[MiniMax](https://platform.minimaxi.com/) пружа моделе са великим контекстом (до 204К токена) кроз OpenAI-компатибилан API. Пошто Microsoft Agent Framework-ов `OpenAIChatClient` ради са било којим OpenAI-компатибилним ендпоинтом, можете користити MiniMax као drop-in алтернативу за лекције које користе `OpenAIChatClient`.

Додајте ове променљиве у ваш `.env` фајл:

| Променљива | Где је пронаћи |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Користите `https://api.minimax.io/v1` (подразумевана вредност) |
| `MINIMAX_MODEL_ID` | Име модела који ћете користити (нпр. `MiniMax-M3`) |

**Пример модела**: `MiniMax-M3` (препоручено), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (бржи одговори). Имена и доступност модела могу се мењати током времена, а приступ одређеном моделу може зависити од вашег налога.

Примери кода који користе `OpenAIChatClient` (нпр. радни ток за резервацију хотела из лекције 14) аутоматски ће открити и користити вашу MiniMax конфигурацију када је `MINIMAX_API_KEY` подешен.


## Алтернативни провајдер: Foundry Local (Покрени моделе на уређају)

[Foundry Local](https://foundrylocal.ai) је лагано време извршавања које преузима, управља и сервира језичке моделе **потпуно на вашем рачунару** преко OpenAI-ускладивог API-ја — без потребе за облаком.

Пошто `OpenAIChatClient` из Microsoft Agent Framework ради са било којим OpenAI-ускладиштеним крајњим тачкама, Foundry Local је локална алтернатива Azure OpenAI-ју.

**1. Инсталирајте Foundry Local**

```bash
# Виндоус
winget install Microsoft.FoundryLocal

# макОС
brew install foundrylocal
```

**2. Преузмите и покрените модел** (ово такође покреће локалну услугу):

```bash
foundry model list          # погледајте доступне моделе
foundry model run phi-4-mini
```

**3. Инсталирајте Python SDK** који се користи за откривање локалне крајње тачке:

```bash
pip install foundry-local-sdk
```

**4. Усмерите Microsoft Agent Framework на ваш локални модел:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Преузима (ако је потребно) и служи модел локално, затим открива крајњу тачку/порт.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # на пример http://localhost:<port>/v1
    api_key=manager.api_key,        # увек "није потребно" за Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Напомена:** Foundry Local излаже OpenAI-ускладиштену крајњу тачку за **Chat Completions**. Користите је за локални развој и офлајн сценарије. За пун сет функција **Responses API** (државне конверзације и др.), користите Azure OpenAI или Microsoft Foundry пројекат.

## Додатна подешавања за Лекцију 8 (Bing Grounding радни ток)

Условни радни ток у лекцији 8 користи **Bing grounding** преко Microsoft Foundry. Ако планирате да покренете тај пример, додајте ову променљиву у ваш `.env` фајл:

| Променљива | Где се налази |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry портал → ваш пројекат → **Management** → **Connected resources** → ваша Bing конекција → копирајте ID конекције |

## Решавање проблема

### SSL грешке приликом валидације на macOS-у

Ако користите macOS и наиђете на грешку као што је:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ово је познати проблем са Python-ом на macOS-у где системски SSL сертификати нису аутоматски прихваћени. Покушајте следећа решења по реду:

**Опција 1: Покрените Python Install Certificates скрипту (препоручено)**

```bash
# Замените 3.XX својом инсталираном верзијом Питхона (нпр. 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Опција 2: Користите `connection_verify=False` у вашем нотебооку (само за GitHub Models нотебуке)**

У Лекцији 6 нотебоку (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), већ је укључено коментарисано решење. Декоментаришите `connection_verify=False` када наиђете на SSL грешке:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Онемогући SSL верификацију ако наиштиш на грешке са сертификатом
)
```

> **⚠️ Упозорење:** Искључивање SSL валидације (`connection_verify=False`) смањује безбедност прескачући верификацију сертификата. Користите ово само као привремено решење у развојним окружењима. Нико не користите у продукцији.

**Опција 3: Инсталирајте и користите `truststore`**

```bash
pip install truststore
```

Затим додајте следеће на врх вашег нотебоока или скрипте пре било каквих мрежних позива:

```python
import truststore
truststore.inject_into_ssl()
```

## Запели сте негде?

Ако имате неких проблема са овим подешавањем, придружите нам се на <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">отворите issue</a>.

## Следећа лекција

Сада сте спремни да покренете код за овај курс. Срећно у учењу о свету AI агената! 

[Увод у AI агенте и примене агената](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->