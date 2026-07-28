# Mpangilio wa Kozi

## Utangulizi

Somo hili litaelezea jinsi ya kuendesha sampuli za msimbo wa kozi hii.

## Jiunge na Wanafunzi Wengine na Pata Msaada

Kabla ya kuanza kunakili repo yako, jiunge na [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) ili kupata msaada wowote kuhusu mpangilio, maswali yoyote kuhusu kozi, au kuungana na wanafunzi wengine.

## Nakili au Fanya Fork ya Repo Hii

Ili kuanza, tafadhali nakili au fanya fork ya Repositori ya GitHub. Hii itakuwezesha kuwa na toleo lako la nyenzo za kozi ili uweze kuendesha, kujaribu, na kubadilisha msimbo!

Hii inaweza kufanywa kwa kubonyeza kiungo kwenda <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">kufork repo</a>

Sasa unapaswa kuwa na toleo lako la fork la kozi hii kwenye kiungo kinachofuata:

![Forked Repo](../../../translated_images/sw/forked-repo.33f27ca1901baa6a.webp)

### Nakili ya Kipepeo (inapendekezwa kwa warsha / Codespaces)

  >Repositori kamili inaweza kuwa kubwa (~3 GB) wakati unapakua historia kamili na faili zote. Ikiwa unaenda tu warshani au unahitaji folda chache za masomo, nakili ya kipepeo (au nakili nyembamba) huzuia sehemu kubwa ya upakuaji huo kwa kukata historia na/au kupita blobs.

#### Nakili ya kipepeo ya haraka — historia kidogo, faili zote

Badilisha `<your-username>` katika amri zilizo hapa chini na URL ya fork yako (au URL ya asili ikiwa unayoipendelea).

Ili kunakili tu historia ya kamishna wa hivi karibuni (upakuaji mdogo):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Ili kunakili tawi maalum:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Nakili Sehemu (nyembamba) — blobs kidogo + folda zilizochaguliwa pekee

Hii inatumia nakili ya sehemu na sparse-checkout (inahitaji Git 2.25+ na inashauriwa Git ya kisasa yenye msaada wa nakili ya sehemu):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pitia ndani ya folda ya repo:

```bash|powershell
cd ai-agents-for-beginners
```

Kisha eleza folda unazotaka (mfano hapa chini unaonyesha folda mbili):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Baada ya kunakili na kuthibitisha faili, ikiwa unahitaji faili tu na unataka kuachilia nafasi (hakuna historia ya git), tafadhali futa metadata ya repositori (💀haiwezi kubadilishwa — utapoteza utendaji wote wa Git: hakuna maombi, kuvuta, kupeleka, au kufikia historia).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Kutumia GitHub Codespaces (inapendekezwa kuepuka upakuaji mkubwa wa eneo la ndani)

- Tengeneza Codespace mpya kwa repo hii kupitia [GitHub UI](https://github.com/codespaces).  

- Katika terminal ya codespace mpya, endesha moja ya amri za nakili kipepeo/nyembamba zilizotajwa hapo juu ili kuleta folda za masomo unazohitaji tu kwenye eneo la kazi la Codespace.
- Hiari: baada ya kunakili ndani ya Codespaces, ondoa .git ili kurudisha nafasi zaidi (angalia amri za kuondoa hapo juu).
- Kumbuka: Ikiwa unapendelea kufungua repo moja kwa moja ndani ya Codespaces (bila kunakili tena), fahamu Codespaces itatengeneza mazingira ya devcontainer na bado inaweza kuweka zaidi ya unachohitaji. Kunakili nakili ya kipepeo ndani ya Codespace safi hukupa udhibiti zaidi juu ya matumizi ya diski.

#### Vidokezo

- Daima badilisha URL ya nakili na fork yako ikiwa unataka kuhariri/kuomba mabadiliko.
- Ikiwa baadaye unahitaji historia au faili zaidi, unaweza kuvijumuisha au kurekebisha sparse-checkout kuongeza folda zaidi.

## Kuendesha Msimbo

Kozi hii inatoa safu ya Daftari za Jupyter ambazo unaweza kuendesha ili kupata uzoefu wa vitendo wa kujenga Wakala wa AI.

Sampuli za msimbo hutumia **Microsoft Agent Framework (MAF)** na `FoundryChatClient`, ambayo inaunganisha na **Microsoft Foundry Agent Service V2** (API ya Majibu) kupitia **Microsoft Foundry**.

Daftari zote za Python zimeandikwa `*-python-agent-framework.ipynb`.

## Mahitaji

- Python 3.12+
  - **KUMBUKA**: Ikiwa huna Python3.12 imewekwa, hakikisha unaeza kuisakinisha. Kisha tengeneza mazingira ya venv ukitumia python3.12 ili kuhakikisha toleo sahihi limewekwa kutoka kwa faili requirements.txt.
  
    >Mfano

    Tengeneza saraka ya Python venv:

    ```bash|powershell
    python -m venv venv
    ```

    Kisha washaji mazingira ya venv kwa:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Kwa sampuli za msimbo zinazotumia .NET, hakikisha umeisakinisha [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) au zaidi. Kisha, angalia toleo la SDK ya .NET ulilolisakinisha:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Inahitajika kwa uthibitishaji. Sakinisha kutoka [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Usajili wa Azure** — Kwa ajili ya kupata huduma za Microsoft Foundry na Microsoft Foundry Agent Service.
- **Mradi wa Microsoft Foundry** — Mradi wenye mfano uliowekwa (mfano, `gpt-5-mini`). Angalia [Hatua 1](#hatua-1-tengeneza-mradi-wa-microsoft-foundry) hapa chini.

Tumekuwa na faili ya `requirements.txt` kwenye mzizi wa repositori hii inayojumuisha vifurushi vya Python vinavyohitajika kuendesha sampuli za msimbo.

Unaweza kuvisakinisha kwa kuendesha amri ifuatayo kwenye terminal yako katika mzizi wa repositori:

```bash|powershell
pip install -r requirements.txt
```

Tunapendekeza kuunda mazingira halisi ya Python ili kuepuka mvutano wowote na matatizo.

## Mpangilio wa VSCode

Hakikisha unatumia toleo sahihi la Python ndani ya VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Weka Microsoft Foundry na Microsoft Foundry Agent Service

### Hatua 1: Tengeneza Mradi wa Microsoft Foundry

Unahitaji **hub** na **mradi** wa Microsoft Foundry wenye mfano uliowekwa kuendesha daftari.

1. Nenda kwenye [ai.azure.com](https://ai.azure.com) na ingia kwa akaunti yako ya Azure.
2. Tengeneza **hub** (au tumia ile iliyopo). Angalia: [Muhtasari wa rasilimali za Hub](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Ndani ya hub, tengeneza **mradi**.
4. Wekeza mfano (mfano, `gpt-5-mini`) kutoka **Models + Endpoints** → **Deploy model**.

### Hatua 2: Pata Kiungo cha Mradi Wako na Jina la Uwekaji Mfano

Kutoka kwa mradi wako katika lango la Microsoft Foundry:

- **Kiungo cha Mradi** — Nenda kwenye ukurasa wa **Muhtasari** na nakili URL ya kiungo.

![Project Connection String](../../../translated_images/sw/project-endpoint.8cf04c9975bbfbf1.webp)

- **Jina la Uwekaji Mfano** — Nenda kwenye **Models + Endpoints**, chagua mfano wako uliowekwa, na kumbuka **Jina la Uwekaji** (mfano, `gpt-5-mini`).

### Hatua 3: Ingia Azure kwa kutumia `az login`


Vitabu vyote vinatumia **`AzureCliCredential`** kwa uthibitishaji — hakuna funguo za API za kusimamia. Hii inahitaji uwe umeingia kupitia Azure CLI.

1. **Sakinisha Azure CLI** ikiwa hujafanya hivyo bado: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Ingia** kwa kuendesha:

    ```bash|powershell
    az login
    ```

    Au ikiwa uko katika mazingira ya mbali/Codespace bila kivinjari:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Chagua usajili wako** ikiwa utaombwa — chagua ile yenye mradi wako wa Foundry.

4. **Thibitisha** umeingia:

    ```bash|powershell
    az account show
    ```

> **Kwa nini `az login`?** Vitabu vinathibitisha kwa kutumia `AzureCliCredential` kutoka kwa kifurushi cha `azure-identity`. Hii inamaanisha kikao chako cha Azure CLI kinatoa vyeti — hakuna funguo za API au siri kwenye faili yako `.env`. Hii ni [mbinu bora ya usalama](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Hatua ya 4: Unda Faili Yako `.env`

Nakili faili la mfano:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Fungua `.env` na jaza hizi thamani mbili:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal ya Foundry → mradi wako → ukurasa wa **Muhtasari** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal ya Foundry → **Models + Endpoints** → jina la mfano uliouanzisha |

Hilo ndilo kwa masomo mengi! Vitabu vitathibitisha kiotomatiki kupitia kikao chako cha `az login`.

### Hatua ya 5: Sakinisha Mategemeo ya Python

```bash|powershell
pip install -r requirements.txt
```

Tunapendekeza kuendesha hili ndani ya mazingira pepe uliyounda awali.

## Mipangilio Mbalimbali kwa Somo la 5 (Agentic RAG)

Somo la 5 linatumia **Azure AI Search** kwa kizazi kilichoimarishwa kwa urejeshaji. Ikiwa unapanga kuendesha somo hilo, ongeza vigezo hivi kwenye faili yako `.env`:

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Portal ya Azure → rasilimali yako ya **Azure AI Search** → **Muhtasari** → URL |
| `AZURE_SEARCH_API_KEY` | Portal ya Azure → rasilimali yako ya **Azure AI Search** → **Mipangilio** → **Funguo** → funguo kuu ya msimamizi |

## Mipangilio Mbalimbali kwa Masomo Yanayowaita Azure OpenAI Moja kwa Moja (Masomo 6 na 8)

Baadhi ya vitabu katika masomo 6 na 8 huwaita **Azure OpenAI** moja kwa moja (kwa kutumia **Responses API**) badala ya kupitia mradi wa Microsoft Foundry. Sampuli hizi awali zilikuwa zinatumia GitHub Models, ambayo imepitwa na wakati (itazimwa Julai 2026) na haitegemezi Responses API. Ikiwa unapanga kuendesha sampuli hizo, ongeza vigezo hivi kwenye faili yako `.env`:

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Portal ya Azure → rasilimali yako ya **Azure OpenAI** → **Funguo na Endpoint** → Endpoint (mfano `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Jina la mfano uliouanzisha (mfano `gpt-5-mini`) unaounga mkono Responses API |
| `AZURE_OPENAI_API_KEY` | Hiari — tu ikiwa unatumia uthibitishaji wa msingi badala ya `az login` / Entra ID |

> Responses API inatumia endpoint thabiti ya `/openai/v1/`, hivyo hakuna `api-version` inayohitajika. Ingia na `az login` kutumia uthibitishaji wa Entra ID usio na funguo.

## Mtoa Huduma Mbadala: MiniMax (Inayoungwa Mkono na OpenAI)

[MiniMax](https://platform.minimaxi.com/) hutoa mifano yenye muktadha mkubwa (hadi tokeni 204K) kupitia API inayoungwa mkono na OpenAI. Kwa kuwa `OpenAIChatClient` ya Microsoft Agent Framework hufanya kazi na endpoint yoyote inayoungwa mkono na OpenAI, unaweza kutumia MiniMax kama mbadala wa kubandika kwa Azure OpenAI au OpenAI.

Ongeza vigezo hivi kwenye faili yako `.env`:

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `MINIMAX_API_KEY` | [Jukwaa la MiniMax](https://platform.minimaxi.com/) → Funguo za API |
| `MINIMAX_BASE_URL` | Tumia `https://api.minimax.io/v1` (thamani ya msingi) |
| `MINIMAX_MODEL_ID` | Jina la mfano wa kutumia (mfano, `MiniMax-M3`) |

**Mifano ya mfano**: `MiniMax-M3` (inayopendekezwa), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (majibu ya haraka). Majina ya mfano na upatikanaji yanaweza kubadilika kwa muda, na ufikiaji wa mfano fulani unaweza kutegemea akaunti yako au eneo — angalia [Jukwaa la MiniMax](https://platform.minimaxi.com/) kwa orodha ya sasa. Ikiwa `MiniMax-M3` haipatikani kwa akaunti yako, weka `MINIMAX_MODEL_ID` kwa mfano unaoweza kufikia (mfano `MiniMax-M2.7`).

Sampuli za msimbo zinazotumia `OpenAIChatClient` (mfano, mchakato wa kuhifadhi hoteli wa Somo la 14) zitagundua kiotomatiki na kutumia usanidi wako wa MiniMax wakati `MINIMAX_API_KEY` imewekwa.

## Mtoa Huduma Mbadala: Foundry Local (Endesha Mifano Kwenye Kifaa Chako)

[Foundry Local](https://foundrylocal.ai) ni mazingira nyepesi ya utendaji ambayo hupakua, kusimamia, na kuhudumia mifano ya lugha **kabisa kwenye mashine yako mwenyewe** kupitia API inayoungwa mkono na OpenAI — hakuna wingu, hakuna usajili wa Azure, na hakuna funguo za API. Ni chaguo nzuri kwa maendeleo bila mtandao, kujaribu bila gharama za wingu, au kuhifadhi data kwenye kifaa.

kwa sababu `OpenAIChatClient` ya Microsoft Agent Framework hufanya kazi na endpoint yoyote inayoungwa mkono na OpenAI, Foundry Local ni mbadala wa ndani wa kubandika kwa Azure OpenAI.

**1. Sakinisha Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Pakua na endesha mfano** (hii pia huanzisha huduma ya ndani):

```bash
foundry model list          # ona mifano inayopatikana
foundry model run phi-4-mini
```

**3. Sakinisha SDK ya Python** inayotumika kugundua endpoint ya ndani:

```bash
pip install foundry-local-sdk
```

**4. Elekeza Microsoft Agent Framework kwenye mfano wako wa ndani:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Inapakua (ikiwa inahitajika) na kuhudumia mfano kwa ndani, kisha kugundua endpoint/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # mfano http://localhost:<port>/v1
    api_key=manager.api_key,        # daima "sio muhimu" kwa Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Kumbuka:** Foundry Local huonyesha endpoint ya OpenAI-compatible **Chat Completions**. Tumia kwa maendeleo ya ndani na matukio bila mtandao. Kwa seti kamili ya vipengele vya **Responses API** (mazungumzo ya hali ya juu, usimamizi wa zana kwa kina, na maendeleo ya aina ya wakala), lenga **Azure OpenAI** au mradi wa **Microsoft Foundry** kama ilivyoonyeshwa katika masomo. Angalia [nyaraka za Foundry Local](https://foundrylocal.ai) kwa katalogi ya mfano wa sasa na msaada wa jukwaa.


## Usanidi Zaidi kwa Somo la 8 (Mtiririko wa Kuweka Msingi wa Bing)


Daftari la mtiririko wa kazi wa masharti katika somo la 8 linatumia **Bing grounding** kupitia Microsoft Foundry. Ikiwa unapanga kuendesha sampuli hiyo, ongeza vigezo hivi kwenye faili yako ya `.env`:

| Kigezo | Mahali pa kukipata |
|----------|-----------------|
| `BING_CONNECTION_ID` | Portal ya Microsoft Foundry → mradi wako → **Management** → **Connected resources** → muunganisho wako wa Bing → nakili ID ya muunganisho |

## Kusuluhisha Matatizo

### Makosa ya Uthibitishaji wa Cheti cha SSL kwenye macOS

Ikiwa uko kwenye macOS na unakutana na hitilafu kama:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Hili ni tatizo lililojulikana na Python kwenye macOS ambapo vyeti vya SSL vya mfumo havitumiki moja kwa moja. Jaribu suluhisho zifuatazo kwa mpangilio:

**Chaguo 1: Endesha skripti ya Python ya Kusakinisha Vyeti (inapendekezwa)**

```bash
# Badilisha 3.XX na toleo lako la Python lililowekwa (mfano, 3.12 au 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Chaguo 2: Tumia `connection_verify=False` katika daftari lako (kwa daftari za GitHub Models pekee)**

Katika daftari la Somo la 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), suluhisho la muda lililokatwa tayari limejumuishwa. Fungua `connection_verify=False` unapotengeneza mteja:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Zima uthibitisho wa SSL ikiwa unatokea makosa ya cheti
)
```

> **⚠️ Onyo:** Kuzima uthibitishaji wa SSL (`connection_verify=False`) kupunguza usalama kwa kuepuka uthibitishaji wa cheti. Tumia hii kama suluhisho la muda tu katika mazingira ya maendeleo, kamwe si kwa uzalishaji.

**Chaguo 3: Sakinisha na tumia `truststore`**

```bash
pip install truststore
```

Kisha ongeza ifuatayo juu ya daftari lako au skripti kabla ya kuita mtandao wowote:

```python
import truststore
truststore.inject_into_ssl()
```

## Umekwama Wapi?

Ikiwa unapata matatizo yoyote katika kuendesha usanidi huu, jisajili katika <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> au <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">unda tatizo</a>.

## Somo Lijalo

Sasa uko tayari kuendesha msimbo wa kozi hii. Furahia kujifunza zaidi kuhusu ulimwengu wa Wakala wa AI!

[Utangulizi wa Wakala wa AI na Matumizi ya Wakala](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->