# Подешавање курса

## Увод

Ова лекција ће обухватити како покренути примере кода овог курса.

## Придружите се другим ученицима и добијте помоћ

Пре него што почнете да клонирате свој репозиторијум, придружите се [AI Agents For Beginners Discord каналу](https://aka.ms/ai-agents/discord) да бисте добили помоћ са подешавањем, поставили питања о курсу или се повезали са другим ученицима.

## Клонирајте или форкујте овај репозиторијум

Да бисте почели, молимо вас да клонирате или форкујете GitHub репозиторијум. Ово ће направити вашу верзију материјала курса тако да можете покретати, тестирати и подешавати код!

Ово можете урадити кликом на линк за <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">форковање репозиторијума</a>

Сада бисте требали имати своју форковану верзију овог курса на следећем линку:

![Forked Repo](../../../translated_images/sr/forked-repo.33f27ca1901baa6a.webp)

### Плитко клонирање (препоручено за радионице / Codespaces)

  >Цео репозиторј може бити велики (~3 ГБ) када преузмете целу историју и све фајлове. Ако присуствујете само радионици или су вам потребне само неке фасцикле са лекцијама, плитко клонирање (или делимично клонирање) избегава већину тог преузимања тако што скраћује историју и/или прескаче неке blob-ове.

#### Брзо плитко клонирање — минимална историја, сви фајлови

Замените `<your-username>` у наредбама испод са URL-ом вашег fork-а (или upstream URL ако више волите).

Да клонирате само најновију историју commit-а (мање преузимање):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Да клонирате одређену грану:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Делимично (sparse) клонирање — минимални blob-ови + само одабране фасцикле

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

Након клонирања и провере фајлова, ако вам требају само фајлови и желите да ослободите простор (без git историје), избришите метаподатке репозиторијума (💀неповратно — изгубићете сву Git функционалност: нема комита, пулова, пушова или приступа историји).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Коришћење GitHub Codespaces (препоручено да се избегну велика локална преузимања)

- Креирајте нови Codespace за овај репозиторцијум преко [GitHub UI](https://github.com/codespaces).  

- У терминалу новокреираног codespace-а покрените неку од наредби за плитко или sparse клонирање горе да бисте унели у радни простор само фасцикле са лекцијама које вам требају.
- Опционално: након клонирања унутар Codespaces, уклоните .git да ослободите додатни простор (погледајте наредбе за уклањање изнад).
- Напомена: Ако више волите да отворите репозиторјум директно у Codespaces (без додатног клонирања), имајте у виду да ће Codespaces конструисати devcontainer окружење и можда ће ипак обезбедити више него што вам треба. Клонирање плитке копије унутар свежег Codespace-а даје вам већу контролу над коришћењем диска.

#### Савети

- Увек замените URL клонирања са URL-ом вашег fork-а ако желите да измените/комитујете.
- Ако вам касније треба више историје или фајлова, можете их дохватити или подесити sparse-checkout да укључује додатне фасцикле.

## Покретање кода

Овај курс нуди серију Јупитер бележница које можете покренути да бисте стекли практично искуство у изградњи AI агената.

Примери кода користе **Microsoft Agent Framework (MAF)** са `AzureAIProjectAgentProvider`, који се повезује са **Azure AI Agent Service V2** (Responses API) преко **Microsoft Foundry**.

Све Python бележнице су означене као `*-python-agent-framework.ipynb`.

## Захтеви

- Python 3.12+
  - **НАПОМЕНА**: Ако немате инсталиран Python 3.12, уверите се да га инсталирате. Онда креирајте виртуелно окружење користећи python3.12 да будете сигурни да су исправне верзије инсталиране из фајла requirements.txt.
  
    >Пример

    Креирање директоријума за Python виртуелно окружење:

    ```bash|powershell
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

- .NET 10+: За примерке кода који користе .NET, уверите се да сте инсталирали [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) или новију верзију. Потом проверите верзију инсталираног .NET SDK-а:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — потребан за аутентификацију. Инсталирајте са [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure претплата** — за приступ Microsoft Foundry и Azure AI Agent Service.
- **Microsoft Foundry пројекат** — пројекат са распоређеним моделом (нпр. `gpt-4o`). Погледајте [Корак 1](#корак-1-креирање-microsoft-foundry-пројекта) доле.

Укључили смо фајл `requirements.txt` у корен овог репозиторијума који садржи све потребне Python пакете за покретање примера кода.

Можете их инсталирати покретањем следеће команде у вашем терминалу у корену репозиторијума:

```bash|powershell
pip install -r requirements.txt
```

Препоручујемо да направите Python виртуелно окружење да бисте избегли конфликте и проблеме.

## Подешавање VSCode

Уверите се да користите исправну верзију Python-а у VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Подешавање Microsoft Foundry и Azure AI Agent Service

### Корак 1: Креирање Microsoft Foundry пројекта

Потребан вам је Azure AI Foundry **hub** и **пројекат** са распоређеним моделом како бисте покренули бележнице.

1. Идите на [ai.azure.com](https://ai.azure.com) и пријавите се са својим Azure налогом.
2. Направите **hub** (или користите постојећи). Погледајте: [Преглед Hub ресурса](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Унутар хаба направите **пројекат**.
4. Распоредите модел (нпр. `gpt-4o`) преко **Models + Endpoints** → **Deploy model**.

### Корак 2: Преузмите URL пројектног Endpoint-а и име распоређеног модела

Из свог пројекта у Microsoft Foundry порталу:

- **Project Endpoint** — идите на страницу **Overview** и копирајте URL endpoint-а.

![Project Connection String](../../../translated_images/sr/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — идите на **Models + Endpoints**, одаберите ваш распоређени модел и запишите **Deployment name** (нпр. `gpt-4o`).

### Корак 3: Пријавите се у Azure преко `az login`

Све бележнице користе **`AzureCliCredential`** за аутентификацију — нема потребе да управљате API кључевима. Ово захтева да будете пријављени преко Azure CLI.

1. **Инсталирајте Azure CLI** ако већ нисте: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Пријавите се** покретањем:

    ```bash|powershell
    az login
    ```

    Или, ако сте у удаљеном/Codespace окружењу без претраживача:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Изаберите вашу претплату** ако се тражи — одаберите ону која садржи ваш Foundry пројекат.

4. **Проверите** да ли сте пријављени:

    ```bash|powershell
    az account show
    ```

> **Зашто `az login`?** Бележнице се аутентификују користећи `AzureCliCredential` из `azure-identity` пакета. То значи да ваша Azure CLI сесија обезбеђује креденцијале — нема API кључева или тајни у вашем `.env` фајлу. Ово је [најбоља безбедносна пракса](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Корак 4: Креирајте свој `.env` фајл

Копирајте пример:

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Променљива | Где је пронаћи |
|------------|---------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry портал → ваш пројекат → страница **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry портал → **Models + Endpoints** → име вашег распоређеног модела |

То је то за већину лекција! Бележнице ће аутоматски аутентификовати преко ваше `az login` сесије.

### Корак 5: Инсталирање Python зависности

```bash|powershell
pip install -r requirements.txt
```

Препоручујемо да ово покренете унутар виртуелног окружења које сте раније направили.

## Додатно подешавање за Лекцију 5 (Agentic RAG)

Лекција 5 користи **Azure AI Search** за retrieval-augmented generation. Ако планирате да покренете ту лекцију, додајте ове променљиве у свој `.env` фајл:

| Променљива | Где је пронаћи |
|------------|---------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure портал → ваш **Azure AI Search** ресурс → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure портал → ваш **Azure AI Search** ресурс → **Settings** → **Keys** → примарни администраторски кључ |

## Додатно подешавање за Лекцију 6 и Лекцију 8 (GitHub модели)

Неке бележнице у лекцијама 6 и 8 користе **GitHub моделе** уместо Azure AI Foundry. Ако планирате да покренете те примере, додајте ове променљиве у свој `.env` фајл:

| Променљива | Где је пронаћи |
|------------|---------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Користите `https://models.inference.ai.azure.com` (подразумевана вредност) |
| `GITHUB_MODEL_ID` | Име модела који желите да користите (нпр. `gpt-4o-mini`) |

## Алтернативни провајдер: MiniMax (компатибилан са OpenAI)

[MiniMax](https://platform.minimaxi.com/) обезбеђује моделе са великим контекстом (до 204К токена) преко OpenAI-компатибилног API-ја. Пошто Microsoft Agent Framework-ов `OpenAIChatClient` ради са било којим OpenAI-компатибилним endpoint-ом, можете користити MiniMax као замену за GitHub моделе или OpenAI.

Додајте ове променљиве у свој `.env` фајл:

| Променљива | Где је пронаћи |
|------------|---------------|
| `MINIMAX_API_KEY` | [MiniMax платформа](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Користите `https://api.minimax.io/v1` (подразумевана вредност) |
| `MINIMAX_MODEL_ID` | Име модела који желите да користите (нпр. `MiniMax-M3`) |

**Примери модела**: `MiniMax-M3` (препоручено), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (брже одговоре). Имена модела и доступност могу се временом мењати, а приступ одређеном моделу може зависити од вашег налога или региона — проверите [MiniMax платформу](https://platform.minimaxi.com/) за тренутну листу. Ако `MiniMax-M3` није доступан вашем налогу, поставите `MINIMAX_MODEL_ID` на модел коме имате приступ (нпр. `MiniMax-M2.7`).

Примери кода који користе `OpenAIChatClient` (нпр. ток рада резервације хотела у Лекцији 14) ће аутоматски препознати и користити вашу MiniMax конфигурацију када је `MINIMAX_API_KEY` подешен.

## Додатно подешавање за Лекцију 8 (Bing Grounding Workflow)

Бележница условног тока рада у лекцији 8 користи **Bing grounding** преко Azure AI Foundry. Ако планирате да покренете тај пример, додајте ову променљиву у свој `.env` фајл:

| Променљива | Где је пронаћи |
|------------|---------------|
| `BING_CONNECTION_ID` | Azure AI Foundry портал → ваш пројекат → **Management** → **Connected resources** → ваша Bing конекција → копирајте connection ID |

## Решавање проблема

### SSL сертификат верификациони проблеми на macOS

Ако сте на macOS и наиђете на грешку као што је:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ово је познат проблем са Python-ом на macOS где системски SSL сертификати нису аутоматски поуздани. Испробајте следећа решења по редоследу:

**Опција 1: Покрените Python скрипту за инсталацију сертификата (препоручено)**

```bash
# Замените 3.XX са верзијом Питхона коју сте инсталирали (на пример, 3.12 или 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Опција 2: Користите `connection_verify=False` у бележници (само за GitHub Models бележнице)**

У бележници за Лекцију 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), већ је укључен коментаром искључен начин да се заобиђе проблем. Откоментирајте `connection_verify=False` приликом креирања клијента:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Онемогући SSL проверу ако наидјеш на грешке са сертификатом
)
```

> **⚠️ Упозорење:** Искључивање SSL верификације (`connection_verify=False`) смањује безбедност прескачући проверу сертификата. Користите ово само као привремено решење у развојном окружењу, никад у продукцији.

**Опција 3: Инсталирајте и користите `truststore`**

```bash
pip install truststore
```

Затим додајте следеће на почетку своје бележнице или скрипте пре прављења било каквих мрежних позива:

```python
import truststore
truststore.inject_into_ssl()
```

## Нешто вам није јасно?

Ако имате проблема са покретањем овог подешавања, придружите се нашем <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> или <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">отворите issue</a>.
## Следећа лекција

Сада сте спремни да покренете код за овај курс. Срећно у даљем учењу о свету AI агената!

[Увод у AI агенте и случајеве употребе агената](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->