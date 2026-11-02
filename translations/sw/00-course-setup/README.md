# Mpangilio wa Kozi

## Utangulizi

Somo hili litatua jinsi ya kuendesha mifano ya msimbo wa kozi hii.

## Jiunge na Wanafunzi Wengine na Pata Msaada

Kabla ya kuanza kunakili repo yako, jiunge na [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) ili kupata msaada wowote kuhusu mpangilio, maswali yoyote kuhusu kozi, au kuungana na wanafunzi wengine.

## Nakili au Funda Repo hii

Ili kuanza, tafadhali nakili au funda Hifadhi ya GitHub (GitHub Repository). Hii itaunda toleo lako la nyenzo za kozi ili uweze kuendesha, kujaribu, na kurekebisha msimbo!

Hii inaweza kufanyika kwa kubofya kiungo cha <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">funda repo</a>

Sasa unapaswa kuwa na toleo lako la mlolongo tuli wa kozi hii kwenye kiungo kinachofuata:

![Forked Repo](../../../translated_images/sw/forked-repo.33f27ca1901baa6a.webp)

### Nakili Nyaupe (inayopendekezwa kwa warsha / Codespaces)

  >Hifadhi nzima inaweza kuwa kubwa (~3 GB) unapo pakua historia kamili na faili zote. Ikiwa unashiriki tu kwenye warsha au unahitaji folda chache za somo, nakili nyaupe (au nakili chache) hupakua kidogo sana.

#### Nakili Nyaupe Haraka — historia kidogo, faili zote

Badilisha `<your-username>` katika amri zilizo chini na URL ya funda yako (au URL ya juu ikiwa unavutiwa).

Ili kunakili tu historia ya mojawapo ya maombi ya hivi karibuni (pakua kidogo):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Ili kunakili tawi maalum:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Nakili Sehemu (Sparse) — blob chache + folda zilizochaguliwa tu

Hii inatumia nakili sehemu na sparse-checkout (inahitaji Git 2.25+ na inashauri kutumia Git ya kisasa yenye msaada wa nakili sehemu):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pitia kwenye folda ya repo:

```bash
cd ai-agents-for-beginners
```

Kisha bainisha folda unazotaka (mfano chini unaonyesha folda mbili):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Baada ya kunakili na kuthibitisha faili, ikiwa unahitaji tu faili na unataka kuachilia nafasi (bila historia ya git), tafadhali futa metadata ya repo (💀isiyoweza kubadilika — utapoteza ufanisi wote wa Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Kutumia GitHub Codespaces (inayopendekezwa kuepuka upakuaji mkubwa wa eneo la kompyuta)

- Tengeneza Codespace mpya kwa repo hii kupitia [GitHub UI](https://github.com/codespaces).  

- Katika terminal ya codespace iliyotengenezwa, endesha moja ya amri za nakili nyaupe/sparse zilizotajwa juu ili kuleta folda za somo unazohitaji tu kwenye eneo la kazi la Codespace.
- Hiari: baada ya kunakili ndani ya Codespaces, ondoa .git ili kurejesha nafasi zaidi (angalia amri za uondoaji zilizo juu).
- Kumbuka: Ikiwa unapendelea kufungua repo moja kwa moja ndani ya Codespaces (bila kunakili tena), fahamu Codespaces itatengeneza mazingira ya devcontainer na bado inaweza kuandaa zaidi ya unachohitaji.

#### Vidokezo

- Daima badilisha URL ya nakili na funda yako ikiwa unataka kuhariri/kuweka maombi.
- Ikiwa baadaye unahitaji historia zaidi au faili, unaweza kuvifetch au kubadilisha sparse-checkout ili kujumuisha folda za ziada.

## Kuendesha Msimbo

Kozi hii inatoa mfululizo wa Jupyter Notebooks ambao unaweza kuendesha kupata uzoefu wa vitendo wa kujenga Maajenti wa AI.

Mifano ya msimbo hutumia **Microsoft Agent Framework (MAF)** na `FoundryChatClient`, ambayo inaunganishwa na **Microsoft Foundry Agent Service V2** (API ya Mijibu) kupitia **Microsoft Foundry**.

Notebooks zote za Python zimeandikwa `*-python-agent-framework.ipynb`.

## Mahitaji

- Python 3.12+
  - **KUMBUKA**: Ikiwa huna Python3.12 imewekwa, hakikisha unaisakinisha. Kisha tengeneza venv yako ukitumia python3.12 kuhakikisha toleo sahihi limewekwa kutoka kwenye faili la requirements.txt.
  
    >Mfano

    Tengeneza saraka ya Python venv:

    ```bash
    python -m venv venv
    ```

    Kisha wawezesha mazingira ya venv kwa:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Kwa mifano inayotumia .NET, hakikisha unaweka [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) au baadaye. Kisha, angalia toleo la SDK la .NET uliolisakinisha:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Inahitajika kwa uthibitishaji. Sakinisha kutoka [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Kwa kupata huduma ya Microsoft Foundry na Microsoft Foundry Agent Service.
- **Mradi wa Microsoft Foundry** — Mradi wenye mfano uliowekwa (mfano, `gpt-5-mini`). Angalia [Hatua 1](#hatua-1-tengeneza-mradi-wa-microsoft-foundry) hapa chini.

Tumewashirikisha faili ya `requirements.txt` kwenye mzizi wa hifadhi hii ambayo ina vifurushi vyote vya Python vinavyohitajika kuendesha mifano ya msimbo.

Unaweza kuvisakinisha kwa kuendesha amri ifuatayo kwenye terminal yako kwenye mzizi wa hifadhi:

```bash
pip install -r requirements.txt
```

Tunapendekeza kutengeneza mazingira ya Python virtual ili kuepuka migogoro na matatizo.

## Mpangilio wa VSCode

Hakikisha unatumia toleo sahihi la Python ndani ya VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Weka Microsoft Foundry na Microsoft Foundry Agent Service

### Hatua 1: Tengeneza Mradi wa Microsoft Foundry

Unahitaji **hub** na **mradi** wa Microsoft Foundry wenye mfano uliowekwa ili kuendesha notebooks.

1. Nenda kwenye [ai.azure.com](https://ai.azure.com) na fungua akaunti yako ya Azure.
2. Tengeneza **hub** (au tumia iliyopo). Angalia: [Muhtasari wa rasilimali za Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Ndani ya hub, tengeneza **mradi**.
4. Weka mfano wa mfano (mfano, `gpt-5-mini`) kutoka **Models + Endpoints** → **Deploy model**.

### Hatua 2: Pata Kiungo cha Mradi Wako na Jina la Utekelezaji wa Mfano

Kutoka kwenye mradi wako katika lango la Microsoft Foundry:

- **Kiungo cha Mradi** — Nenda kwenye ukurasa wa **Overview** na nakili URL ya kiungo.

![Project Connection String](../../../translated_images/sw/project-endpoint.8cf04c9975bbfbf1.webp)

- **Jina la Utekelezaji wa Mfano** — Nenda kwenye **Models + Endpoints**, chagua mfano uliowekwa, na chukua **Jina la Utekelezaji** (mfano, `gpt-5-mini`).

### Hatua 3: Ingia kwenye Azure kwa `az login`

Notebooks nyingi zinathibitisha kupitia **Azure CLI sign-in** — kwa kutumia `AzureCliCredential` au `DefaultAzureCredential` (yote huleta kikao chako cha `az login`) kutoka kwa kifurushi cha `azure-identity` — hivyo hazihitaji funguo za API. Baadhi ya masomo na ushirikiano wa hiari hutumia funguo za API; angalia mahitaji ya kila somo kwa mabadiliko yoyote ya mazingira. Hii inahitaji uingie kupitia Azure CLI.

1. **Sakinisha Azure CLI** ikiwa bado hujafanya hivyo: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Ingia** kwa kuendesha:

    ```bash
    az login
    ```

    Au ikiwa uko kwenye mazingira ya mbali/Codespace bila kivinjari:

    ```bash
    az login --use-device-code
    ```

3. **Chagua usajili** ikiwa utaulizwa — chagua lile lenye mradi wako wa Foundry.

4. **Thibitisha** umeingia:

    ```bash
    az account show
    ```

> **Kwa nini `az login`?** Notebooks zinathibitisha kwa kutumia `AzureCliCredential` (au `DefaultAzureCredential`, ambayo pia huchukua `az login`) kutoka kwa kifurushi cha `azure-identity`. Hii ina maana kikao chako cha Azure CLI kinatoa leseni — hakuna funguo za API au siri kwenye faili lako la `.env`. Hii ni [mambo bora ya usalama](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Hatua 4: Tengeneza Faili Lako la `.env`

Nakili faili la mfano:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Fungua `.env` na jaza haya maadili mawili:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Lango la Foundry → mradi wako → ukurasa wa **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Lango la Foundry → **Models + Endpoints** → jina la mfano uliowekwa |

Hiyo ni kwa masomo mengi! Notebooks zitathibitisha moja kwa moja kupitia kikao chako cha `az login`.

### Hatua 5: Sakinisha Mipangilio ya Python

```bash
pip install -r requirements.txt
```

Tunapendekeza kuendesha hii ndani ya mazingira ya virtual uliyounda awali.

## Mpangilio wa Hiari: Azure AI Search (Masomo 5 na 16)

Masomo ya 5 (Agentic RAG) na 16 hufanya kazi mara moja na **hifadhidata ya maarifa ya ndani** — hakuna rasilimali za ziada za Azure zinazohitajika. Ikiwa unataka kutumia hakiki halisi ya **Azure AI Search**, kumbuka kuwa **notebook ya Somo 16 kwa sasa hutumia uthibitishaji wa funguo**: inabadilika kutoka kwenye hakiki ya ndani hadi Azure AI Search tu wakati **pamoja** `AZURE_SEARCH_SERVICE_ENDPOINT` **na** `AZURE_SEARCH_API_KEY` vimewekwa, na vinginevyo inaendelea kuwa kwenye hakiki ya ndani — kwa hivyo kuendesha dhidi ya hakiki halisi lazima iwe umeweka ufunguo wa msimamizi pia. Uthibitishaji bila funguo kwa Microsoft Entra ID (RBAC) ni njia inayopendekezwa kwa msimbo wako wa uzalishaji, sawa na mtiririko wa `az login` unaotumika sehemu zote za kozi hii.

Hatua za RBAC zilizo hapa chini zinatumika kwa mifano ya mwongozo wa mpangilio na msimbo wako mwenyewe. Haziwashii uthibitishaji bila funguo katika notebook ya Somo 16; Somo 16 bado linahitaji endpoint na funguo ya msimamizi ili kutumia Azure AI Search.

1. **Washa upatikanaji unaotegemea majukumu** kwenye huduma yako ya utafutaji:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Jipa majukumu yanayohitajika** (kutengeneza/kupakia hakiki na kuulizia):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Ongeza endpoint** kwenye faili yako ya `.env`:

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Lango la Azure → rasilimali yako ya **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Inahitajika (pamoja na endpoint) kuwezesha Azure AI Search kwenye notebook ya Somo 16, inayotumia uthibitishaji wa funguo. Lango la Azure → **Settings** → **Keys** → funguo kuu ya msimamizi |

> **Kwa nini bila funguo?** Funguo za msimamizi huruhusu uandikishaji kamili kwenye huduma yako ya utafutaji na zinaweza kuvuja kupitia faili za `.env`. Kwa RBAC, utambulisho wako wa `az login` hutumika badala yake — mfano huo waEntra ID usio na funguo unaotumika na notebooks za kozi (kupitia `AzureCliCredential` / `DefaultAzureCredential`). Angalia [Unganisha kwa Azure AI Search kwa kutumia majukumu](https://learn.microsoft.com/azure/search/search-security-rbac).

Angalia [mwongozo wa mpangilio wa Azure AI Search](./AzureSearch.md) kwa mifano kamili ya utengenezaji wa hakiki kwa Python na .NET.

## Mpangilio Zaidi kwa Masomo yanayopiga Azure OpenAI Moja kwa Moja (Masomo 6 na 8)

Baadhi ya notebooks katika masomo 6 na 8 hupiga **Azure OpenAI** moja kwa moja (kutumia **Responses API**) badala ya kupitia mradi wa Microsoft Foundry. Mifano hii hapo awali ilitumia GitHub Models, ambayo imekataliwa na haitegemezi Responses API. Ongeza vigezo hivi kwenye faili yako ya `.env`:

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Lango la Azure → rasilimali yako ya **Azure OpenAI** → **Keys and Endpoint** → Endpoint (mfano `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Jina la mfano uliowekwa (mfano `gpt-5-mini`) unaoendana na Responses API |
| `AZURE_OPENAI_API_KEY` | Hiari — ikiwa unatumia uthibitishaji wa funguo badala ya `az login` / Entra ID |

> API ya Mijibu hutumia endpoint thabiti ya `/openai/v1/`, kwa hivyo hakuna `api-version` inayohitajika. Ingia kwa `az login` kutumia uthibitishaji wa Entra ID usio na funguo.

## Mtoa Mbadala: MiniMax (Inaoendana na OpenAI)

[MiniMax](https://platform.minimaxi.com/) hutoa mifano ya muktadha mkubwa (hadi tokeni 204K) kupitia API inayolingana na OpenAI. Kwa kuwa Microsoft Agent Framework's `OpenAIChatClient` hufanya kazi na endpoint yoyote inayolingana na OpenAI, unaweza kutumia MiniMax kama mbadala wa moja kwa moja kwa masomo yanayotumia `OpenAIChatClient`.

Ongeza vigezo hivi kwenye faili yako ya `.env`:

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → Funguo za API |
| `MINIMAX_BASE_URL` | Tumia `https://api.minimax.io/v1` (thamani ya kawaida) |
| `MINIMAX_MODEL_ID` | Jina la mfano wa kutumia (mfano, `MiniMax-M3`) |

**Mifano ya mfano**: `MiniMax-M3` (inayopendekezwa), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (majibu ya haraka zaidi). Majina ya mifano na upatikano yanaweza kubadilika kwa muda, na upatikanaji wa mfano fulani unategemea akaunti yako.

Mifano ya msimbo inayotumia `OpenAIChatClient` (mfano, mtiririko wa uhifadhi wa hoteli wa Somo la 14) itagundua na kutumia usanidi wako wa MiniMax moja kwa moja wakati `MINIMAX_API_KEY` imewekwa.


## Mtoa Huduma Mbadala: Novita AI (Inayoungana na OpenAI)

[Novita AI](https://novita.ai/llm-api) hutoa API inayoungana na OpenAI kwa ajili ya LLM za chanzo huria na za kisasa (DeepSeek, Llama, Qwen, na zaidi). Kwa kuwa `OpenAIChatClient` ya Microsoft Agent Framework hufanya kazi na kipokezi chochote kinachoungana na OpenAI, unaweza kutumia Novita AI kama mbadala rahisi kwa Azure OpenAI au OpenAI.

Ongeza vigezo hivi kwenye faili lako la `.env`:

| Kigezo | Iko wapi |
|----------|-----------------|
| `NOVITA_API_KEY` | [Dashibodi ya Novita AI](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | Tumia `https://api.novita.ai/openai/v1` (thamani ya chaguo-msingi) |
| `NOVITA_MODEL_ID` | Jina la modeli la kutumia (mfano, `moonshotai/kimi-k3`) |

**Mifano ya modeli**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI pia ina makundi mengi ya modeli za chanzo huria (Llama, Qwen, GLM, na zaidi) — angalia [maktaba ya modeli ya Novita AI](https://novita.ai/llm-api) kwa orodha ya sasa ya modeli zinazopatikana na ID zao za modeli.

Sampuli za sasa hazitumi vigezo vya `NOVITA_*` moja kwa moja. Ili kutumia Novita AI, pita vigezo hivi wazi unapojenga `OpenAIChatClient` kwenye sampuli unayoendesha.

## Mtoa Huduma Mbadala: Foundry Local (Endesha Modeli Kwenye Kifaa Chako)

[Foundry Local](https://foundrylocal.ai) ni runtime nyepesi inayopakua, kusimamia, na kuhudumia modeli za lugha **kote kabisa kwenye kompyuta yako** kupitia API inayoungana na OpenAI — haina haja ya wingu.

Kwa kuwa `OpenAIChatClient` ya Microsoft Agent Framework hufanya kazi na kipokezi chochote kinachoungana na OpenAI, Foundry Local ni mbadala wa ndani rahisi kwa Azure OpenAI.

**1. Sakinisha Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Pakua na endesha modeli** (hii pia huanzisha huduma ya ndani):

```bash
foundry model list          # ona mifano inayopatikana
foundry model run phi-4-mini
```

**3. Sakinisha SDK ya Python** inayotumika kugundua kipokezi cha ndani:

```bash
pip install foundry-local-sdk
```

**4. Elekeza Microsoft Agent Framework kwenye modeli yako ya ndani:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Inapakua (ikiwa inahitajika) na kuendesha modeli kwa ndani, kisha hugundua sehemu ya mwisho/lango.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # mfano http://localhost:<port>/v1
    api_key=manager.api_key,        # daima "haihitaji" kwa Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Kumbuka:** Foundry Local huweka wazi endpoint ya **Chat Completions** inayoungana na OpenAI. Tumia kwa maendeleo ya ndani na hali zisizo na mtandao. Kwa seti kamili ya vipengele vya **Responses API** (mazungumzo ya hali, n.k.), tumia Azure OpenAI au mradi wa Microsoft Foundry.

## Mipangilio Zaidi kwa Somo la 8 (Mtiririko wa Kuweka Msingi wa Bing)

Kitabu cha mtiririko wa masharti katika somo la 8 kinatumia ** kuweka msingi kwa Bing** kupitia Microsoft Foundry. Ikiwa unapanga kuendesha sampuli hiyo, ongeza kigezo hiki kwenye faili lako la `.env`:

| Kigezo | Iko wapi |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal ya Microsoft Foundry → mradi wako → **Management** → **Connected resources** → muunganisho wako wa Bing → nakili ID ya muunganisho |

## Utatuzi wa Matatizo

### Makosa ya Uthibitishaji wa SSL kwenye macOS

Ikiwa uko kwenye macOS na unakutana na kosa kama:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Hili ni tatizo lililotambuliwa na Python kwenye macOS ambapo vyeti vya SSL vya mfumo havautiwi kwa moja kwa moja. Jaribu suluhisho zifuatazo kwa mpangilio:

**Chaguo 1: Endesha script ya Kusakinisha Vyeti ya Python (inapendekezwa)**

```bash
# Badilisha 3.XX na toleo lako la Python ulilolisanisha (mfano, 3.12 au 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Chaguo 2: Tumia `connection_verify=False` katika kitabu chako (kwa vitabu vya GitHub Models pekee)**

Katika kitabu cha Somo la 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), suluhisho lililokataliwa tayari limejumuishwa. Futa maoni kwenye `connection_verify=False` unapoona makosa ya vyeti:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Zima uhakiki wa SSL ikiwa unakutana na makosa ya cheti
)
```

> **⚠️ Onyo:** Kuzima uthibitishaji wa SSL (`connection_verify=False`) kunapunguza usalama kwa kuruka uthibitishaji wa cheti. Tumia hii kama suluhisho la muda tu katika mazingira ya maendeleo. Usitumie duniani wa uzalishaji.

**Chaguo 3: Sakinisha na tumia `truststore`**

```bash
pip install truststore
```

Kisha ongeza zifuatazo juu ya kitabu chako au script kabla ya kuita mitandao yoyote:

```python
import truststore
truststore.inject_into_ssl()
```

## Umefungwa Wapi?

Ikiwa unapata matatizo yoyote kuendesha usanidi huu, ingia kwenye <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> au <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">tengeneza tatizo</a>.

## Somo Linalofuata

Sasa uko tayari kuendesha msimbo wa kozi hii. Furahia kujifunza zaidi kuhusu ulimwengu wa Wakala wa AI!

[Utangulizi wa Wakala wa AI na Matumizi ya Wakala](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->