# Постављање курса

## Увод

Ова лекција ће објаснити како да покренете примерке кода из овог курса.

## Придружите се другим ученицима и затражите помоћ

Пре него што почнете да клонирате свој репозиторијум, придружите се [AI Agents For Beginners Discord каналу](https://aka.ms/ai-agents/discord) да бисте добили помоћ у вези са подешавањем, поставили питања о курсу или се повезали са другим ученицима.

## Клонирајте или направите форк овог репозиторијума

Да бисте почели, молимо вас да клонирате или направите форк ГитХаб репозиторијума. Ово ће направити вашу верзију материјала курса тако да можете да покрећете, тестирате и прилагођавате код!

Ово можете урадити кликом на линк за <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форк репозиторијум</a>

Сада бисте требали имати своју форковану верзију овог курса на следећем линку:

![Forked Repo](../../../translated_images/sr/forked-repo.33f27ca1901baa6a.webp)

### Плитки клон (препоручује се за радионицу / Codespaces)

  >Цео репозиторијум може бити велики (~3 ГБ) када преузмете целокупну историју и све фајлове. Ако похађате само радионицу или су вам потребне само неке фасцикле са лекцијама, плитки клон (или sparse клон) преузима много мање.

#### Брзи плитки клон — минимална историја, сви фајлови

Замените `<your-username>` у наредбама испод са URL-ом вашег форка (или са URL-ом upstream-а ако више волите).

Да бисте клонирали само најновију историју комита (мање преузимање):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Да бисте клонирали одређену грану:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Делимични (sparse) клон — минимални blob-ови + само изабране фасцикле

Ово користи делимични клон и sparse-checkout (захтева Git 2.25+ и препоручује се модеран Git са подршком за делимични клон):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Уђите у фасциклу репозиторијума:

```bash
cd ai-agents-for-beginners
```

Затим наведите које фасцикле желите (пример испод показује две фасцикле):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Након клонирања и провере фајлова, ако вам требају само фајлови и желите да ослободите простор (без историје Git-а), обавезно обришите метаподатке репозиторијума (💀непоправљиво — изгубићете сву Git функционалност):

```bash
# зш/баш
rm -rf .git
```

```powershell
# ПоверШел
Remove-Item -Recurse -Force .git
```

#### Коришћење GitHub Codespaces (препоручује се да се избегну велика локална преузимања)

- Направите нови Codespace за овај репозиторијум преко [GitHub UI](https://github.com/codespaces).  

- У терминалу новоотвореног codespace-а покрените неку од горе наведених shallow/sparse clone наредби да бисте у радни простор Codespace-а довели само фасцикле са лекцијама које су вам потребне.
- Опционо: након клонирања унутар Codespaces-а, уклоните .git да бисте ослободили додатни простор (погледајте наредбе за уклањање горе).
- Напомена: ако више волите да отворите репозиторијум директно у Codespaces (без додатног клонирања), имајте на уму да ће Codespaces подесити devcontainer окружење и можда ће захтевати више ресурса него што вам треба.

#### Савети

- Увек замените URL за клон вашег форка ако желите да уређујете или правите комите.
- Ако вам касније затреба више историје или фајлова, можете их дохватити или подесити sparse-checkout да укључује додатне фасцикле.

## Покретање кода

Овај курс нуди серију Јупитер Нотебоок-ова које можете покренути да бисте стекли практично искуство у креирању AI агената.

Примери кода користе **Microsoft Agent Framework (MAF)** са `FoundryChatClient`, који се повезује на **Microsoft Foundry Agent Service V2** (Responses API) преко **Microsoft Foundry**.

Сви Python нотебоок-ови имају назив `*-python-agent-framework.ipynb`.

## Захтеви

- Python 3.12+
  - **НАПОМЕНА**: Ако немате инсталиран Python 3.12, обавезно га инсталирајте. Затим креирајте ваше виртуелно окружење користећи python3.12 да бисте обезбедили инсталацију исправних верзија из requirements.txt фајла.
  
    >Пример

    Креирање Python виртуелног окружења:

    ```bash
    python -m venv venv
    ```

    Затим активирајте виртуелно окружење за:

    ```bash
    # зш/баш
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: За примерке кода који користе .NET, обезбедите да имате инсталиран [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или новији. Након тога, проверите вашу инсталирану верзију .NET SDK-а:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Потребан за аутентификацију. Инсталирајте са [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — За приступ Microsoft Foundry и Microsoft Foundry Agent Service-у.
- **Microsoft Foundry Project** — Пројекат са развијеним моделом (нпр., `gpt-5-mini`). Погледајте [Корак 1](#корак-1-креирање-microsoft-foundry-пројекта) у наставку.

Укључили смо `requirements.txt` фајл у корен овог репозиторијума који садржи све неопходне Python пакете за покретање примерка кода.

Можете их инсталирати покретањем следеће команде у терминалу са корена репозиторијума:

```bash
pip install -r requirements.txt
```

Препоручујемо да направите Python виртуелно окружење како бисте избегли конфликте и проблеме.

## Подешавање VSCode

Уверите се да користите исправну верзију Python-а у VSCode-у.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Подешавање Microsoft Foundry и Microsoft Foundry Agent Service

### Корак 1: Креирање Microsoft Foundry пројекта

Потребан вам је Microsoft Foundry **hub** и **проект** са развијеним моделом да бисте могли да покренете нотебоок-ове.

1. Идите на [ai.azure.com](https://ai.azure.com) и пријавите се са својим Azure налогом.
2. Креирајте **hub** (или искористите постојећи). Погледајте: [Преглед Hub ресурса](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Унутар hub-а направите **проект**.
4. Развијте модел (нпр., `gpt-5-mini`) преко **Models + Endpoints** → **Deploy model**.

### Корак 2: Пронађите Endpoint вашег пројекта и име имплементираног модела

У вашем пројекту у Microsoft Foundry порталу:

- **Project Endpoint** — Идите на страницу **Overview** и копирајте URL endpoint-а.

![Project Connection String](../../../translated_images/sr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Идите на **Models + Endpoints**, изаберите развијени модел и запишите **Deployment name** (нпр., `gpt-5-mini`).

### Корак 3: Пријавите се у Azure користећи `az login`

Већина нотебоок-ова аутентификује се преко вашег **Azure CLI пријављивања** — помоћу `AzureCliCredential` или `DefaultAzureCredential` (обе користе вашу `az login` сесију) из пакета `azure-identity` — тако да нису потребни API кључеви. Поједине лекције и опциони интеграциони захтевају API кључеве; проверите предуслове сваке лекције за додатне променљиве окружења. Ово захтева да се пријавите преко Azure CLI-а.

1. **Инсталирајте Azure CLI** ако већ нисте: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Пријавите се** покретањем:

    ```bash
    az login
    ```

    Или ако сте у удаљеном/Codespace окружењу без браузера:

    ```bash
    az login --use-device-code
    ```

3. **Изаберите вашу претплату** ако вам буде затражено — изаберите ону која садржи ваш Foundry пројекат.

4. **Потврдите** да сте пријављени:

    ```bash
    az account show
    ```

> **Зашто `az login`?** Нотебоок-ови се аутентификују користећи `AzureCliCredential` (или `DefaultAzureCredential`, који такође користи вашу Azure CLI пријаву) из пакета `azure-identity`. Ово значи да ваша Azure CLI сесија пружа креденцијале — нема потребе за API кључевима или тајнама у `.env` фајлу. Ово је [најбоља пракса у области безбедности](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Корак 4: Креирајте свој `.env` фајл

Копирајте пример:

```bash
# зш/баш
cp .env.example .env
```

```powershell
# Powershell
Copy-Item .env.example .env
```

Отворите `.env` и унесите ове две вредности:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Променљива | Где је наћи |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry портал → ваш пројекат → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry портал → **Models + Endpoints** → име вашег развијеног модела |

То је све за већину лекција! Нотебоок-ови ће аутентификовати аутоматски преко ваше `az login` сесије.

### Корак 5: Инсталирајте зависности за Python

```bash
pip install -r requirements.txt
```

Препоручујемо да ово покренете у виртуелном окружењу које сте раније креирали.

## Опционо подешавање: Azure AI Search (лекције 5 и 16)

Лекција 5 (Agentic RAG) и лекција 16 нотебоок-ови раде одмах са **in-memory knowledge base** — није потребно додатно Azure ресурса. Ако желите да их повежете са правим **Azure AI Search** индексом, имајте у виду да Леција 16 нотебоок тренутно користи аутентификацију на бази кључа: прелази са in-memory претраге на Azure AI Search само када су постављене **обе** променљиве `AZURE_SEARCH_SERVICE_ENDPOINT` **и** `AZURE_SEARCH_API_KEY`, у супротном остаје на in-memory претрази — дакле, да бисте је покренули са правим индексом морате такође поставити администраторски кључ. Аутентификација без кључа уз Microsoft Entra ID (RBAC) је препоручени приступ за ваш властити продукцијски код, у складу са `az login` током који се користи у свим деловима овог курса.

RBAC кораци доле важе за примерке из овог водича и за ваш властити код. Не омогућавају аутентификацију без кључа у лекцији 16; лекција 16 и даље захтева оба, endpoint и администраторски кључ, за коришћење Azure AI Search-а.

1. **Омогућите приступ заснован на улогама (RBAC)** на вашем претраживачком сервису:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Доделите себи потребне улоге** (креирање/учитавање индекса и упити):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Додајте endpoint** у ваш `.env` фајл:

| Променљива | Где је наћи |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure портал → ваш **Azure AI Search** ресурс → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Потребно (заједно са endpoint-ом) да би се омогућио Azure AI Search у лекцији 16 нотебоок-у који користи аутентификацију на бази кључа. Azure портал → **Settings** → **Keys** → примарни администраторски кључ |

> **Зашто без кључа?** Администраторски кључеви пружају пун приступ за писање на вашем сервису за претрагу и могу бити откривени преко `.env` фајлова. Са RBAC, користи се ваш `az login` идентитет — исти безклучни Entra ID образац који курсни нотебоок-ови користе (помоћу `AzureCliCredential` / `DefaultAzureCredential`). Погледајте [Повезивање са Azure AI Search-ом коришћењем улога](https://learn.microsoft.com/azure/search/search-security-rbac).

Погледајте [Azure AI Search водич за подешавање](./AzureSearch.md) за потпуне примере креирања индекса на Python и .NET-у.

## Додатно подешавање за лекције које директно позивају Azure OpenAI (лекције 6 и 8)

Неки нотебоок-ови у лекцијама 6 и 8 директно позивају **Azure OpenAI** (користећи **Responses API**) уместо да иду преко Microsoft Foundry пројекта. Ови примерци су раније користили GitHub Models, који је застарео и не подржава Responses API. Додајте ове променљиве у свој `.env` фајл:

| Променљива | Где је наћи |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure портал → ваш **Azure OpenAI** ресурс → **Keys and Endpoint** → Endpoint (нпр. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Назив вашег развијеног модела (нпр. `gpt-5-mini`) који подржава Responses API |
| `AZURE_OPENAI_API_KEY` | Опционо — само ако користите аутентификацију на бази кључа уместо `az login` / Entra ID |

> Responses API користи стабилан `/openai/v1/` endpoint, тако да није потребна `api-version`. Пријавите се са `az login` да корисите безклучну Entra ID аутентификацију.

## Алтернативни провајдер: MiniMax (OpenAI-компатибилан)

[MiniMax](https://platform.minimaxi.com/) пружа моделе са великим контекстом (до 204К токена) преко OpenAI-компатибилног API-ја. Пошто `OpenAIChatClient` Microsoft Agent Framework-а ради са било којим OpenAI-компатибилним endpoint-ом, можете користити MiniMax као замена за лекције које користе `OpenAIChatClient`.

Додајте ове променљиве у свој `.env` фајл:

| Променљива | Где је наћи |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax платформа](https://platform.minimaxi.com/) → API кључеви |
| `MINIMAX_BASE_URL` | Користите `https://api.minimax.io/v1` (дифолт вредност) |
| `MINIMAX_MODEL_ID` | Назив модела који желите (нпр., `MiniMax-M3`) |

**Пример модела**: `MiniMax-M3` (препоручени), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (бржи одговори). Називи модела и доступност могу се мењати, а приступ одређеном моделу зависи од вашег налога.

Примерци кода који користе `OpenAIChatClient` (нпр. ток рада за резервацију хотела у лекцији 14) аутоматски ће открити и користити вашу MiniMax конфигурацију када је `MINIMAX_API_KEY` постављен.


## Алтернативни добављач: Novita AI (компатибилан са OpenAI)

[Novita AI](https://novita.ai/llm-api) пружа API компатибилан са OpenAI за open-source и најновије LLM-ове (DeepSeek, Llama, Qwen и друге). Пошто `OpenAIChatClient` из Microsoft Agent Framework-а ради са било којом OpenAI-компатибилном крајњом тачком, можете користити Novita AI као drop-in алтернативу Azure OpenAI или OpenAI.

Додајте ове променљиве у ваш `.env` фајл:

| Променљива | Где је пронаћи |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI контролна табла](https://novita.ai/settings/key-management) → API Кључеви |
| `NOVITA_BASE_URL` | Користите `https://api.novita.ai/openai/v1` (подразумевана вредност) |
| `NOVITA_MODEL_ID` | Назив модела за коришћење (нпр. `moonshotai/kimi-k3`) |

**Пример модела**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI такође хостује много других open-source породица модела (Llama, Qwen, GLM и друге) — проверите [Novita AI библиотеку модела](https://novita.ai/llm-api) за текућу листу доступних модела и њихове ID-ове.

Тренутни примери не користе аутоматски `NOVITA_*` променљиве. Да бисте користили Novita AI, проследите те вредности изричито при конструисању `OpenAIChatClient` у примеру који покрећете.

## Алтернативни добављач: Foundry Local (Покретање модела на уређају)

[Foundry Local](https://foundrylocal.ai) је лагано окружење за извршавање које преузима, управља и сервира језичке моделе **потпуно на вашем уређају** путем OpenAI-компатибилног API-ја — без облака.

Пошто `OpenAIChatClient` из Microsoft Agent Framework-а ради са било којом OpenAI-компатибилном крајњом тачком, Foundry Local је локална drop-in алтернатива Azure OpenAI.

**1. Инсталирајте Foundry Local**

```bash
# Виндоус
winget install Microsoft.FoundryLocal

# макОС
brew install foundrylocal
```

**2. Преузмите и покрените модел** (ово такође покреће локалну услугу):

```bash
foundry model list          # погледај доступне моделе
foundry model run phi-4-mini
```

**3. Инсталирајте Python SDK** који се користи за откривање локалне крајње тачке:

```bash
pip install foundry-local-sdk
```

**4. Укажите Microsoft Agent Framework да користи ваш локални модел:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Преузима (ако је потребно) и покреће модел локално, затим проналази крајњу тачку/порт.
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

> **Напомена:** Foundry Local излаже OpenAI-компатибилну крајњу тачку за **Chat Completions**. Користите је за локални развој и офлајн сценарије. За пун скуп могућности **Responses API-ja** (држава разговора итд.), користите Azure OpenAI или Microsoft Foundry пројекат.

## Додатна подешавања за Лекцију 8 (Bing Grounding Workflow)

Условни workflow у лекцији 8 користи **Bing grounding** преко Microsoft Foundry. Ако планирате да покренете тај пример, додајте ову променљиву у ваш `.env` фајл:

| Променљива | Где је пронаћи |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry портал → ваш пројекат → **Management** → **Connected resources** → ваша Bing веза → копирајте ID везе |

## Решавање проблема

### Грешке о верификацији SSL сертификата на macOS

Ако користите macOS и наиђете на грешку као што је:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ово је познати проблем са Python-ом на macOS-у где системски SSL сертификати нису аутоматски поуздани. Испробајте следећа решења по редоследу:

**Опција 1: Покрените Python скрипту за инсталацију сертификата (препоручено)**

```bash
# Замените 3.XX са верзијом Питона коју имате инсталирану (нпр. 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Опција 2: Користите `connection_verify=False` у вашем notebook-у (само за GitHub Models notebook-ове)**

У Лекцији 6 notebook-у (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), већ је укључено закоментарисано решење. Откоментирајте `connection_verify=False` када наиђете на грешке сертификата:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Онемогући SSL верификацију ако наиђеш на грешке са сертификатом
)
```

> **⚠️ Упозорење:** Искључивање верификације SSL-а (`connection_verify=False`) смањује безбедност прескакањем валидације сертификата. Користите ово само као привремено решење у развојним окружењима. Никада не користите у производњи.

**Опција 3: Инсталирајте и користите `truststore`**

```bash
pip install truststore
```

Затим додајте следеће на почетак вашег notebook-а или скрипте пре било каквих мрежних позива:

```python
import truststore
truststore.inject_into_ssl()
```

## Запели сте негде?

Ако имате било каквих проблема током овог подешавања, придружите се нашем <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">отворите issue</a>.

## Следећа лекција

Сада сте спремни да покренете код за овај курс. Срећно у учењу више о свету AI агената!

[Увод у AI агенте и примере употребе агената](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->