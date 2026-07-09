# Mpangilio wa Kozi

## Utangulizi

Somo hili litaelezea jinsi ya kuendesha mifano ya msimbo ya kozi hii.

## Jiunge na Wanafunzi Wengine na Pata Msaada

Kabla ya kuanza kunakili repo yako, jiunge na [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) kupata msaada wowote kuhusu mpangilio, maswali yoyote kuhusu kozi, au kuwasiliana na wanafunzi wengine.

## Nakili au Futa Nakala hii Repo

Kuanza, tafadhali nakili au funguza Nakala ya GitHub. Hii itakuwezesha kuwa na toleo lako mwenyewe la vifaa vya kozi ili uweze kuendesha, kujaribu, na kubadilisha msimbo!

Hii inaweza kufanywa kwa kubofya kiungo cha <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">futa nakala repo</a>

Sasa unapaswa kuwa na toleo lako la makala la kozi hii kwenye kiungo kifuatacho:

![Forked Repo](../../../translated_images/sw/forked-repo.33f27ca1901baa6a.webp)

### Nakili Isiyo ya Kina (inayopendekezwa kwa warsha / Codespaces)

  >Repo kamili inaweza kuwa kubwa (~3 GB) unapo download historia yote na faili zote. Ikiwa unahudhuria warsha tu au unahitaji folda chache za somo tu, nakili isiyo ya kina (au sparse clone) inazuia sehemu kubwa ya download kwa kukata historia na/au kupita blobs.

#### Nakili dhaifu ya haraka — historia kidogo, faili zote

Badilisha `<your-username>` katika amri zilizo chini na URL ya makala yako (au URL ya upstream ikiwa unapendelea).

Kununua historia ya amri za hivi punde tu (download ndogo):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Kununua tawi maalum:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Nakili Sehemu (sparse) — blobs kidogo + folda zilizochaguliwa tu

Hii inatumia nakili sehemu na sparse-checkout (inahitaji Git 2.25+ na inapendekezwa Git ya kisasa yenye msaada wa nakili sehemu):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Ingia ndani ya folda ya repo:

```bash|powershell
cd ai-agents-for-beginners
```

Kisha eleza folda unazotaka (mfano hapo chini unaonyesha folda mbili):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Baada ya kunakili na kuthibitisha faili, kama unahitaji faili tu na unataka kuondoa kumbukumbu (history) ya git, tafadhali futa metadata ya repo (💀 isiyoweza kubadilishwa — utapoteza uwezo wote wa Git: hakuna commits, pulls, pushes, au kupata historia).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Kutumia GitHub Codespaces (inayopendekezwa ili kuepuka download kubwa za eneo la kompyuta)

- Tengeneza Codespace mpya kwa repo hii kupitia [GitHub UI](https://github.com/codespaces).  

- Katika terminal ya codespace iliyoundwa, endesha moja ya amri za nakili dhaifu/sparse ili kuleta folda za somo unazohitaji tu katika eneo la Codespace.
- Hiari: baada ya kunakili ndani ya Codespaces, ondoa .git ili urejeshe nafasi zaidi (ona amri za kuondoa hapo juu).
- Kumbuka: Ikiwa unapendelea kufungua repo moja kwa moja katika Codespaces (bila kunakili tena), fahamu Codespaces itatengeneza mazingira ya devcontainer na inaweza bado kuanzisha zaidi ya unachohitaji. Kunakili nakala dhaifu ndani ya Codespace safi hukupa udhibiti zaidi juu ya matumizi ya disk.

#### Vidokezo

- Daima badilisha URL ya kunakili na ile ya makala yako ikiwa unataka kuhariri/commit.
- Ikiwa baadaye utahitaji historia au faili zaidi, unaweza kuvichukua au kurekebisha sparse-checkout kuhusisha folda za ziada.

## Kuendesha Msimbo

Kozi hii inatoa mfululizo wa Daftari za Jupyter ambazo unaweza kuendesha kupata uzoefu wa vitendo wa kujenga Wakala wa AI.

Mifano ya msimbo hutumia **Microsoft Agent Framework (MAF)** na `FoundryChatClient`, inayounganisha na **Microsoft Foundry Agent Service V2** (API za Majibu) kupitia **Microsoft Foundry**.

Daftari zote za Python zina lebo `*-python-agent-framework.ipynb`.

## Mahitaji

- Python 3.12+
  - **KUMBUKUMBU**: Ikiwa huna Python3.12 imewekwa, hakikisha unaweka. Kisha tengeneza venv yako ukitumia python3.12 ili kuhakikisha toleo sahihi limewekwa kutoka kwa faili ya requirements.txt.
  
    >Mfano

    Tengeneza saraka ya venv ya Python:

    ```bash|powershell
    python -m venv venv
    ```

    Kisha wezesha mazingira ya venv kwa:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Kwa mifano ya msimbo inayotumia .NET, hakikisha umeweka [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) au baadaye. Kisha, angalia toleo la SDK ya .NET uliyoweka:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Inahitajika kwa uthibitishaji. Weka kutoka [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Kwa upatikanaji wa Microsoft Foundry na Microsoft Foundry Agent Service.
- **Mradi wa Microsoft Foundry** — Mradi wenye mfano uliowekwa (mfano, `gpt-4o`). Angalia [Hatua 1](#hatua-1-tengeneza-mradi-wa-microsoft-foundry) hapa chini.

Tumejumuisha faili ya `requirements.txt` kwenye ugani wa juu wa maktaba hii yenye vifurushi vyote vinavyohitajika vya Python kuendesha mifano ya msimbo.

Unaweza kuviweka kwa kuendesha amri ifuatayo kwenye terminal yako kwenye ugani wa maktaba:

```bash|powershell
pip install -r requirements.txt
```

Tunapendekeza kuunda mazingira ya virtual ya Python ili kuepuka mizozo na matatizo.

## Pangilia VSCode

Hakikisha unatumia toleo sahihi la Python katika VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Pangilia Microsoft Foundry na Microsoft Foundry Agent Service

### Hatua 1: Tengeneza Mradi wa Microsoft Foundry

Unahitaji **hub** na **mradi** wa Microsoft Foundry wenye mfano uliowekwa kuendesha daftari.

1. Nenda [ai.azure.com](https://ai.azure.com) na ingia na akaunti yako ya Azure.
2. Tengeneza **hub** (au tumia iliyokuwepo). Angalia: [Muhtasari wa Rasilimali za Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Ndani ya hub, tengeneza **mradi**.
4. Weka mfano (mfano, `gpt-4o`) kutoka **Models + Endpoints** → **Deploy model**.

### Hatua 2: Pata Endpoint ya Mradi Wako na Jina la Kueneza Mfano

Kutoka kwenye mradi wako katika bandari ya Microsoft Foundry:

- **Endpoint ya Mradi** — Nenda kwenye ukurasa wa **Overview** na nakili URL ya endpoint.

![Project Connection String](../../../translated_images/sw/project-endpoint.8cf04c9975bbfbf1.webp)

- **Jina la Kueneza Mfano** — Nenda kwenye **Models + Endpoints**, chagua mfano uliowekwa, na andika **Deployment name** (mfano, `gpt-4o`).

### Hatua 3: Ingia kwenye Azure kwa kutumia `az login`

Daftari zote hutumia **`AzureCliCredential`** kwa uthibitishaji — hakuna funguo za API za kusimamia. Hii inahitaji kuingia kupitia Azure CLI.

1. **Sakinisha Azure CLI** ikiwa bado hujafanya hivyo: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Ingia** kwa kuendesha:

    ```bash|powershell
    az login
    ```

    Au ikiwa uko katika mazingira ya mbali/Codespace bila kivinjari:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Chagua usajili wako** ikiwa itaonyeshwa — chagua ile yenye mradi wako wa Foundry.

4. **Thibitisha** umeingia:

    ```bash|powershell
    az account show
    ```

> **Kwa nini `az login`?** Daftari huyi huthibitisha kwa kutumia `AzureCliCredential` kutoka kifurushi cha `azure-identity`. Hii ina maana kikao chako cha Azure CLI kinatoa sifa — hakuna funguo za API au siri ndani ya faili .env yako. Hii ni [miondoko bora ya usalama](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Hatua 4: Tengeneza Faili Yako ya `.env`

Nakili faili mfano:

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Bandari ya Foundry → mradi wako → ukurasa wa **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Bandari ya Foundry → **Models + Endpoints** → jina la mfano uliowekwa |

Hapo ndipo kwa masomo mengi! Daftari zitatumia uthibitishaji moja kwa moja kupitia kikao chako cha `az login`.

### Hatua 5: Weka Vitegemezi vya Python

```bash|powershell
pip install -r requirements.txt
```

Tunapendekeza kuendesha hii ndani ya mazingira ya virtual uliyotengeneza awali.

## Mpangilio Zaidi kwa Somo la 5 (Agentic RAG)

Somo la 5 linatumia **Azure AI Search** kwa ajili ya kizazi kinachoimarishwa na utafutaji. Ikiwa unapanga kuendesha somo hilo, ongeza vigezo hivi kwenye faili yako ya `.env`:

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Bandari ya Azure → rasilimali yako ya **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Bandari ya Azure → rasilimali yako ya **Azure AI Search** → **Settings** → **Keys** → ufunguo mkuu wa msimamizi |

## Mpangilio Zaidi kwa Masomo Yanayowaita Azure OpenAI Moja kwa Moja (Masomo 6 na 8)

Baadhi ya daftari katika masomo 6 na 8 huita **Azure OpenAI** moja kwa moja (kutumia **Responses API**) badala ya kupitia mradi wa Microsoft Foundry. Mifano hii awali ilitumia GitHub Models, ambayo imekatizwa (itazimwa Julai 2026) na haitegemezi API za Responses. Ikiwa unapanga kuendesha mifano hiyo, ongeza vigezo hivi kwenye faili yako ya `.env`:

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Bandari ya Azure → rasilimali yako ya **Azure OpenAI** → **Keys and Endpoint** → Endpoint (mfano `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Jina la mfano uliowekwa (mfano `gpt-4o-mini`) unaounga mkono Responses API |
| `AZURE_OPENAI_API_KEY` | Hiari — ikiwa unatumia uthibitishaji wa kitufe badala ya `az login` / Entra ID |

> API za Responses hutumia endpoint thabiti ya `/openai/v1/`, hivyo haina haja ya `api-version`. Ingia na `az login` kutumia uthibitishaji wa Entra ID usio na funguo.

## Mtoaji Mbadala: MiniMax (Inayolingana na OpenAI)

[MiniMax](https://platform.minimaxi.com/) hutoa mifano ya muktadha mkubwa (hadi tiketi 204K) kupitia API inayolingana na OpenAI. Kwa kuwa Microsoft Agent Framework `OpenAIChatClient` hufanya kazi na endpoint yoyote inayolingana na OpenAI, unaweza kutumia MiniMax kama mbadala wa Azure OpenAI au OpenAI.

Ongeza vigezo hivi kwenye faili yako ya `.env`:

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → Funguo za API |
| `MINIMAX_BASE_URL` | Tumia `https://api.minimax.io/v1` (thamani ya msingi) |
| `MINIMAX_MODEL_ID` | Jina la mfano wa kutumia (mfano, `MiniMax-M3`) |

**Mifano ya mfano**: `MiniMax-M3` (inayopendekezwa), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (majibu ya haraka). Majina ya mifano na upatikanaji unaweza kubadilika kwa wakati, na upatikanaji wa mfano fulani unaweza kutegemea akaunti yako au eneo — angalia [MiniMax Platform](https://platform.minimaxi.com/) kwa orodha ya sasa. Ikiwa `MiniMax-M3` haipatikani kwa akaunti yako, weka `MINIMAX_MODEL_ID` kwa mfano unaoweza kufikia (mfano `MiniMax-M2.7`).

Mifano ya msimbo inayotumia `OpenAIChatClient` (mfano, mtiririko wa uhifadhi wa hoteli wa Somo 14) itagundua moja kwa moja na kutumia usanidi wako wa MiniMax wakati `MINIMAX_API_KEY` imewekwa.

## Mtoaji Mbadala: Foundry Local (Endesha Mifano Kwenye Kifaa)

[Foundry Local](https://foundrylocal.ai) ni wakati wa kuendesha mtaalamu nyepesi unaopakua, kusimamia, na kuhudumia mifano ya lugha **nzima kwa mashine yako mwenyewe** kupitia API inayolingana na OpenAI — hakuna wingu, hakuna usajili wa Azure, na hakuna funguo za API. Ni chaguo kubwa kwa maendeleo ya nje ya mtandao, kujaribu bila gharama za wingu, au kuhifadhi data ndani ya kifaa.

Kwa kuwa Microsoft Agent Framework `OpenAIChatClient` hufanya kazi na endpoint yoyote inayolingana na OpenAI, Foundry Local ni mbadala wa ndani wa Azure OpenAI.

**1. Sakinisha Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Pakua na endesha mfano** (hii pia huanzisha huduma ya ndani):

```bash
foundry model list          # ona mifano iliyopo
foundry model run phi-4-mini
```

**3. Sakinisha SDK ya Python** inayotumiwa kugundua endpoint ya ndani:

```bash
pip install foundry-local-sdk
```

**4. Elekeza Microsoft Agent Framework kwenye mfano wako wa ndani:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Inapakua (ikiwa inahitajika) na kuhudumia mfano hapa eneo la mtandao, kisha kugundua sehemu ya mwisho/kipenyo.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # mfano http://localhost:<port>/v1
    api_key=manager.api_key,        # daima "haijatakiwa" kwa Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Kumbuka:** Foundry Local huonyesha endpoint ya OpenAI inayoungwa mkono kwa **Chat Completions**. Tumia kwa maendeleo ya ndani na nyakati za nje ya mtandao. Kwa kipengele kamili cha **Responses API** (mazungumzo yenye hali, usimamizi wa zana kwa undani, na maendeleo ya aina ya wakala), lengo ni **Azure OpenAI** au mradi wa **Microsoft Foundry** kama ilivyoonyeshwa katika masomo. Angalia [nyaraka za Foundry Local](https://foundrylocal.ai) kwa katalogi ya mifano na msaada wa jukwaa uliopo.

## Mpangilio Zaidi kwa Somo la 8 (Mtiririko wa Bing Grounding)


Daftari la mtiririko wa kazi la masharti katika somo la 8 linatumia **Bing grounding** kupitia Microsoft Foundry. Ikiwa unapanga kuendesha sampuli hiyo, ongeza kigezo hiki kwenye faili yako `.env`:

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal ya Microsoft Foundry → mradi wako → **Management** → **Connected resources** → muunganisho wako wa Bing → nakili kitambulisho cha muunganisho |

## Utatuzi wa matatizo

### Makosa ya Uthibitishaji wa Cheti cha SSL kwenye macOS

Ikiwa uko kwenye macOS na unakutana na kosa kama:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Hili ni tatizo linalojulikana na Python kwenye macOS ambapo vyeti vya SSL vya mfumo haviaminiwi kiotomatiki. Jaribu suluhisho zifuatazo kwa mpangilio:

**Chaguo la 1: Endesha script ya Python ya Kufunga Vyeti (inapendekezwa)**

```bash
# Badilisha 3.XX na toleo lako la Python lililowekwa (mfano, 3.12 au 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Chaguo la 2: Tumia `connection_verify=False` katika daftari lako (kwa machapisho ya GitHub Models tu)**

Katika daftari la Somo la 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), suluhisho lililofichwa tayari limejumuishwa. Fungua `connection_verify=False` wakati wa kuunda mteja:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Zima uthibitishaji wa SSL ikiwa unakutana na makosa ya cheti
)
```

> **⚠️ Tahadhari:** Kuzima uthibitishaji wa SSL (`connection_verify=False`) kunapunguza usalama kwa kuruka uthibitishaji wa cheti. Tumia hii kama suluhisho la muda tu katika mazingira ya maendeleo, kamwe si kwenye uzalishaji.

**Chaguo la 3: Sakinisha na tumia `truststore`**

```bash
pip install truststore
```

Kisha ongeza yafuatayo juu ya daftari lako au script kabla ya kufanya miito yoyote ya mtandao:

```python
import truststore
truststore.inject_into_ssl()
```

## Umekwama Wapi?

Ikiwa una matatizo yoyote kuendesha usanidi huu, jiunge na <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> au <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">unda tatizo</a>.

## Somo Linalofuata

Sasa uko tayari kuendesha msimbo huu kwa kozi hii. Furahia kujifunza zaidi kuhusu ulimwengu wa Wakala wa AI!

[Utangulizi kwa Wakala wa AI na Matumizi ya Wakala](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->