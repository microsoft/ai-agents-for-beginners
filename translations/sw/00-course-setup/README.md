# Usanidi wa Kozi

## Utangulizi

Somo hili litashughulikia jinsi ya kuendesha sampuli za msimbo za kozi hii.

## Jiunge na Wanafunzi Wengine na Pata Msaada

Kabla hujaanza kukloni repo yako, jiunge na [Kituo cha Discord cha AI Agents kwa Waanziaji](https://aka.ms/ai-agents/discord) ili upate msaada wa usanidi, maswali kuhusu kozi, au kuungana na wanafunzi wengine.

## Kloni au Forki Hazina hii

Ili kuanza, tafadhali kloni au forki Hazina ya GitHub. Hii itakuwekea toleo lako la nyenzo za kozi ili uweze kuendesha, kujaribu, na kubadilisha msimbo!

Hii inaweza kufanywa kwa kubofya kiungo cha <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">kuforki hazina</a>

Sasa unapaswa kuwa na toleo lako la kozi uliyoforkiwa kwenye kiungo kinachofuata:

![Hazina iliyoforkiwa](../../../translated_images/sw/forked-repo.33f27ca1901baa6a.webp)

### Kloni Mfinyu (inayopendekezwa kwa warsha / Codespaces)

  >Hazina kamili inaweza kuwa kubwa (~3 GB) unapopakua historia kamili na faili zote. Ikiwa unashiriki tu kwenye warsha au unahitaji folda chache za masomo, kloni mfinyu (au kloni sparse) hupunguza sehemu kubwa ya upakuaji huo kwa kukata historia na/au kupitisha blobs.

#### Kloni mfinyu ya haraka — historia ndogo, faili zote

Badilisha `<your-username>` katika amri zilizo hapa chini na URL ya fork yako (au URL ya upstream ikiwa unapendelea).

To clone only the latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Kloni Sehemu (sparse) — blobs ndogo + folda zilizochaguliwa tu

Hii inatumia kloni ya sehemu na sparse-checkout (inahitaji Git 2.25+ na inashauriwa Git ya kisasa yenye msaada wa kloni ya sehemu):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Traverse into the repo folder:

```bash|powershell
cd ai-agents-for-beginners
```

Then specify which folders you want (example below shows two folders):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

After cloning and verifying the files, if you only need files and want to free space (no git history), please delete the repository metadata (💀 isiyoweza kurejeshwa — utapoteza utendaji wote wa Git: hakuna commits, pulls, pushes, au upatikanaji wa historia).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Kutumia GitHub Codespaces (inayopendekezwa ili kuepuka upakuaji mkubwa kwa eneo la ndani)

- Unda Codespace mpya kwa hazina hii kupitia [GitHub UI](https://github.com/codespaces).  

- Katika terminal ya codespace iliyoundwa hivi karibuni, endesha moja ya amri za kloni mfinyu/kloni sparse zilizo hapo juu ili kuleta folda za somo unazohitaji tu kwenye nafasi ya kazi ya Codespace.
- Hiari: baada ya kukloni ndani ya Codespaces, ondoa .git ili upate nafasi zaidi (ona amri za kuondoa hapo juu).
- Kumbuka: Ikiwa unapendelea kufungua hazina moja kwa moja katika Codespaces (bila kloni ya ziada), fahamu Codespaces itaunda mazingira ya devcontainer na bado inaweza kuandaa zaidi ya unachohitaji. Kukloni nakala mfinyu ndani ya Codespace safi kunakupa udhibiti zaidi juu ya matumizi ya diski.

#### Vidokezo

- Daima badilisha URL ya kloni na fork yako ikiwa unataka kuhariri/commit.
- Ikiwa baadaye utahitaji historia zaidi au faili, unaweza kuzivuta (fetch) au kurekebisha sparse-checkout ili kujumuisha folda za ziada.

## Kuendesha Msimbo

Kozi hii inatoa mfululizo wa Jupyter Notebooks ambazo unaweza kuendesha ili kupata uzoefu wa vitendo katika kujenga Wakala wa AI.

Sampuli za msimbo zinatumia **Microsoft Agent Framework (MAF)** pamoja na `AzureAIProjectAgentProvider`, ambayo inaunganisha na **Azure AI Agent Service V2** (Responses API) kupitia **Microsoft Foundry**.

Notebooks zote za Python zimelebeiwa `*-python-agent-framework.ipynb`.

## Mahitaji

- Python 3.12+
  - **Kumbuka**: Ikiwa huna Python3.12 imewekwa, hakikisha uliweka. Kisha tengeneza venv yako ukitumia python3.12 ili kuhakikisha toleo sahihi linawekwa kutoka kwenye faili requirements.txt.
  
    >Mfano

    Create Python venv directory:

    ```bash|powershell
    python -m venv venv
    ```

    Then activate venv environment for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Kwa sampuli za msimbo zinazotumia .NET, hakikisha umeweka [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) au baadaye. Kisha, angalia toleo la .NET SDK ulioweka:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Inahitajika kwa uthibitisho. Install kutoka [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Kwa upatikanaji wa Microsoft Foundry na Azure AI Agent Service.
- **Microsoft Foundry Project** — Mradi wenye modeli iliyowekwa (mfano, `gpt-4o`). Angalia [Hatua 1](../../../00-course-setup) hapo chini.

Tumejumuisha faili ya `requirements.txt` katika mzizi wa hazina hii ambayo ina vifurushi vyote vya Python vinavyohitajika kuendesha sampuli za msimbo.

Unaweza kuvisanidi kwa kuendesha amri ifuatayo katika terminal yako kwenye mzizi wa hazina:

```bash|powershell
pip install -r requirements.txt
```

Tunapendekeza kuunda mazingira ya virtual ya Python ili kuepuka migongano na matatizo yoyote.

## Sanidi VSCode

Hakikisha unatumia toleo sahihi la Python ndani ya VSCode.

![picha](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Sanidi Microsoft Foundry na Azure AI Agent Service

### Hatua 1: Tengeneza Mradi wa Microsoft Foundry

Unahitaji **hub** na **mradi** wa Azure AI Foundry yenye modeli iliyowekwa ili kuendesha noti.

1. Nenda kwenye [ai.azure.com](https://ai.azure.com) na ingia kwa akaunti yako ya Azure.
2. Tengeneza **hub** (au tumia iliyo tayari). Angalia: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Ndani ya hub, tengeneza **mradi**.
4. Weka (deploy) modeli (mfano, `gpt-4o`) kutoka **Models + Endpoints** → **Deploy model**.

### Hatua 2: Pata Mwisho wa Mradi Wako na Jina la Utekelezaji wa Modeli

Kutoka kwenye mradi wako katika kiunga cha Microsoft Foundry:

- **Project Endpoint** — Nenda kwenye ukurasa wa **Overview** na nakili URL ya endpoint.

![Mstari wa Unganisho wa Mradi](../../../translated_images/sw/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Nenda kwenye **Models + Endpoints**, chagua modeli uliyoitekeleza, na kumbuka **Deployment name** (mfano, `gpt-4o`).

### Hatua 3: Ingia kwenye Azure kwa kutumia `az login`

Notebooks zote zinatumia **`AzureCliCredential`** kwa uthibitisho — hakuna vibonye za API vya kusimamia. Hii inahitaji uwe umeingia kwa kupitia Azure CLI.

1. **Sakinisha Azure CLI** ikiwa bado hujafanya hivyo: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Ingia** kwa kuendesha:

    ```bash|powershell
    az login
    ```

    Au ikiwa uko katika mazingira ya mbali/Codespace bila kivinjari:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Chagua usajili wako (subscription)** ikiwa utaulizwa — chagua ile yenye mradi wako wa Foundry.

4. **Thibitisha** kuwa umeingia:

    ```bash|powershell
    az account show
    ```

> **Kwa nini `az login`?** Notebooks zinathibitisha kwa kutumia `AzureCliCredential` kutoka kwa kifurushi `azure-identity`. Hii ina maana kikao chako cha Azure CLI kinatoa mamlaka — hakuna vibonye za API au siri katika faili yako `.env`. Hii ni mfano wa mazoea bora ya usalama.

### Hatua 4: Tengeneza Faili Yako `.env`

Nakili faili la mfano:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Fungua `.env` na jaza thamani hizi mbili:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Wapi pa kupatikana |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Portal ya Foundry → mradi wako → ukurasa wa **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Portal ya Foundry → **Models + Endpoints** → jina la modeli uliyoitekeleza |

Hivyo ndivyo kwa masomo mengi! Notebooks zitatumia uthibitisho moja kwa moja kupitia kikao chako cha `az login`.

### Hatua 5: Sakinisha Mategemeo ya Python

```bash|powershell
pip install -r requirements.txt
```

Tunashauri kuendesha hili ndani ya mazingira ya virtual uliyoleta hapo awali.

## Usanidi wa Ziada kwa Somo la 5 (Agentic RAG)

Somo la 5 linatumia **Azure AI Search** kwa generation iliyoimarishwa na utafutaji. Ikiwa unapanga kuendesha somo hilo, ongeza vigezo hivi kwenye faili yako `.env`:

| Variable | Wapi pa kupatikana |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → rasilimali yako ya **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → rasilimali yako ya **Azure AI Search** → **Settings** → **Keys** → primary admin key |

## Usanidi wa Ziada kwa Somo la 6 na Somo la 8 (GitHub Models)

Baadhi ya noti katika masomo 6 na 8 zinatumia **GitHub Models** badala ya Azure AI Foundry. Ikiwa unapanga kuendesha sampuli hizo, ongeza vigezo hivi kwenye faili yako `.env`:

| Variable | Wapi pa kupatikana |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Tumia `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## Usanidi wa Ziada kwa Somo la 8 (Bing Grounding Workflow)

Notebook ya workflow ya masharti katika somo la 8 inatumia **Bing grounding** kupitia Azure AI Foundry. Ikiwa unapanga kuendesha sampuli hiyo, ongeza kigezo hiki kwenye faili yako `.env`:

| Variable | Wapi pa kupatikana |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → mradi wako → **Management** → **Connected resources** → muunganisho wako wa Bing → nakili connection ID |

## Utatuzi wa Matatizo

### Makosa ya Uthibitisho wa Cheti cha SSL kwenye macOS

Ikiwa uko macOS na unakutana na kosa kama:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Hili ni tatizo linalojulikana na Python kwenye macOS ambapo vyeti vya SSL vya mfumo havitambwi moja kwa moja. Jaribu ufumbuzi ufuatao kwa mpangilio:

**Chaguo 1: Endesha skripti ya Install Certificates ya Python (inayopendekezwa)**

```bash
# Badilisha 3.XX na toleo lako la Python lililowekwa (kwa mfano, 3.12 au 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Chaguo 2: Tumia `connection_verify=False` katika notebook yako (kwa noti za GitHub Models pekee)**

Katika notebook ya Somo la 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), mbinu ya kufanya kazi iliyozimwa kwa sehemu tayari imejumuishwa. Fungua sehemu ya maelezo kwa kuondoa maoni `connection_verify=False` wakati unaunda client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Zima uhakiki wa SSL ikiwa utakutana na makosa ya cheti
)
```

> **⚠️ Onyo:** Kuizima uhakiki wa SSL (`connection_verify=False`) kunapunguza usalama kwa kuruka uthibitishaji wa vyeti. Tumia hili tu kama suluhisho la muda katika mazingira ya maendeleo, kamwe si kwa uzalishaji.

**Chaguo 3: Sakinisha na tumia `truststore`**

```bash
pip install truststore
```

Kisha ongeza yafuatayo juu ya noti yako au skripti kabla ya kufanya simu yoyote ya mtandao:

```python
import truststore
truststore.inject_into_ssl()
```

## Umekwama Wapi?

Ikiwa una matatizo yoyote ya kuendesha usanidi huu, jiunge na <a href="https://discord.gg/kzRShWzttr" target="_blank">Discord ya Jumuiya ya Azure AI</a> au <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">tengeneza issue</a>.

## Somo Lifuatao

Sasa uko tayari kuendesha msimbo wa kozi hii. Furahia kujifunza zaidi kuhusu ulimwengu wa Wakala wa AI! 

[Utangulizi kwa Wakala wa AI na Matumizi ya Wakala](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Tamko la kutokuwa na dhamana:
Waraka huu umetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kasoro za usahihi. Waraka asili katika lugha yake ya asili unapaswa kuchukuliwa kama chanzo chenye mamlaka. Kwa taarifa muhimu, inapendekezwa kutumia tafsiri ya mtaalamu wa binadamu. Hatuwajibiki kwa kutoelewana au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->