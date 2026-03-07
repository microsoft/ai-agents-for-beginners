# Mipangilio ya Kozi

## Utangulizi

Somo hili litafundisha jinsi ya kuendesha sampuli za msimbo za kozi hii.

## Jiunge na Wanafunzi Wengine na Upate Msaada

Kabla ya kuanza kunakili repo yako, jiunge na [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) ili kupata msaada wowote wa usanidi, maswali kuhusu kozi, au kuungana na wanafunzi wengine.

## Nakili au Fanya Fork ya Repo hii

Ili kuanza, tafadhali nakili au fanya fork ya Hifadhi ya GitHub. Hii itakuwezesha kuwa na toleo lako mwenyewe la nyenzo za kozi ili uweze kuendesha, kujaribu, na kubadilisha msimbo!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fatilia repo</a>

You should now have your own forked version of this course in the following link:

![Folda iliyoifork](../../../translated_images/sw/forked-repo.33f27ca1901baa6a.webp)

### Kukopa Mfinyu (inayopendekezwa kwa warsha / Codespaces)

  > Hazina kamili inaweza kuwa kubwa (~3 GB) unapotembelea historia kamili na faili zote. Ikiwa unashiriki tu warsha au unahitaji folda chache za masomo pekee, kukopa mfinyu (au kukopa sparse) kunazuia sehemu kubwa ya upakuaji huo kwa kukata historia na/au kuruka blobs.

#### Haraka kukopa mfinyu — historia ndogo, faili zote

Replace `<your-username>` in the below commands with your fork URL (or the upstream URL if you prefer).

To clone only the latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Kukopa Sehemu (sparse) — blobs ndogo + folda chaguo tu

Hii inatumia kukopa sehemu na sparse-checkout (inahitaji Git 2.25+ na inashauriwa Git ya kisasa yenye msaada wa partial clone):

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

After cloning and verifying the files, if you only need files and want to free space (no git history), please delete the repository metadata (💀irreversible — you will lose all Git functionality: no commits, pulls, pushes, or history access).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Kutumia GitHub Codespaces (inayopendekezwa kuepuka upakuaji mkubwa kwa kompyuta ya eneo lako)

- Tengeneza Codespace mpya kwa repo hii kupitia [GitHub UI](https://github.com/codespaces).  

- Katika terminal ya codespace mpya iliyoundwa, run moja ya amri za shallow/sparse clone hapo juu ili kuleta folda za masomo unazohitaji ndani ya eneo la kazi la Codespace.
- Hiari: baada ya kunakili ndani ya Codespaces, ondoa .git ili kurudisha nafasi zaidi (angalia amri za kuondoa hapo juu).
- Kumbuka: Ikiwa unapendelea kufungua repo moja kwa moja katika Codespaces (bila nakili ya ziada), fahamu Codespaces itaunda mazingira ya devcontainer na inaweza bado kuandaa zaidi ya unachohitaji. Kunakili nakili ya mfinyu ndani ya Codespace safi kunakupa udhibiti zaidi juu ya matumizi ya diski.

#### Vidokezo

- Badilisha kila wakati URL ya clone na fork yako ikiwa unataka kuhariri/kujumuisha.
- Ikiwa baadaye utahitaji historia zaidi au faili zaidi, unaweza kuzipata kwa kufetch au kurekebisha sparse-checkout kujumuisha folda za ziada.

## Kukimbia Msimbo

Kozi hii inatoa mfululizo wa Jupyter Notebooks ambazo unaweza kuendesha kupata uzoefu wa vitendo wa kujenga Mawakala wa AI.

Sampuli za msimbo zinatumia **Microsoft Agent Framework (MAF)** na `AzureAIProjectAgentProvider`, ambayo inajuunga na **Azure AI Agent Service V2** (Responses API) kupitia **Microsoft Foundry**.

Notebooks zote za Python zimewekwa lebo `*-python-agent-framework.ipynb`.

## Mahitaji

- Python 3.12+
  - **KUMBUKA**: Ikiwa huna Python3.12 imewekwa, hakikisha unaisakinisha. Kisha tengeneza venv yako ukitumia python3.12 ili kuhakikisha toleo sahihi linawekwa kutoka kwenye faili requirements.txt.
  
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

- .NET 10+: Kwa sampuli za msimbo zinazotumia .NET, hakikisha unasakinisha [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) au baadaye. Kisha, angalia toleo la .NET SDK ulilosakinisha:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Inahitajika kwa uthibitisho. Sakinisha kutoka [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Kwa ufikiaji wa Microsoft Foundry na Azure AI Agent Service.
- **Microsoft Foundry Project** — Mradi wenye modeli iliyowekwa (k.m., `gpt-4o`). Tazama [Hatua 1](../../../00-course-setup) hapa chini.

Tumeganisha faili ya `requirements.txt` katika mizizi ya hifadhi hii ambayo ina vifurushi vyote vinavyohitajika vya Python ili kuendesha sampuli za msimbo.

Unaweza kuvisakinisha kwa kuendesha amri ifuatayo kwenye terminal yako kwenye mizizi ya hifadhi:

```bash|powershell
pip install -r requirements.txt
```

Tunapendekeza kutengeneza mazingira ya virtual ya Python ili kuepuka migongano na matatizo yoyote.

## Sanidi VSCode

Hakikisha unatumia toleo sahihi la Python katika VSCode.

![Picha ya skrini](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Sanidi Microsoft Foundry na Azure AI Agent Service

### Hatua 1: Unda Mradi wa Microsoft Foundry

Unahitaji **hub** na **mradi** wa Azure AI Foundry uliyo na modeli iliyotekelezwa ili kuendesha notebooks.

1. Nenda kwenye [ai.azure.com](https://ai.azure.com) na ingia kwa akaunti yako ya Azure.
2. Tengeneza **hub** (au tumia ile iliyopo). Tazama: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Ndani ya hub, tengeneza **mradi**.
4. Tekeleza modeli (k.m., `gpt-4o`) kutoka **Models + Endpoints** → **Deploy model**.

### Hatua 2: Pata Endpoint ya Mradi Wako na Jina la Utekelezaji wa Modeli

Kutoka kwenye mradi wako kwenye portal ya Microsoft Foundry:

- **Endpoint ya Mradi** — Nenda kwenye ukurasa wa **Muhtasari** na nakili URL ya endpoint.

![Muunganisho wa Mradi](../../../translated_images/sw/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Nenda kwenye **Models + Endpoints**, chagua modeli uliyoiweka, na chukulia **Deployment name** (k.m., `gpt-4o`).

### Hatua 3: Ingia kwenye Azure kwa kutumia `az login`

Notebooks zote zinatumia **`AzureCliCredential`** kwa uthibitisho — hakuna funguo za API za kusimamia. Hii inahitaji uwe umeingia kupitia Azure CLI.

1. **Sakinisha Azure CLI** ikiwa bado hujasakinisha: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Ingia** kwa kuendesha:

    ```bash|powershell
    az login
    ```

    Au kama uko katika mazingira ya mbali/Codespace bila kivinjari:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Chagua subscription yako** ikiwa itaulizwa — chagua ile yenye mradi wako wa Foundry.

4. **Thibitisha** umeingia:

    ```bash|powershell
    az account show
    ```

> **Kwanini `az login`?** Notebooks zinathibitisha kwa kutumia `AzureCliCredential` kutoka kwa kifurushi `azure-identity`. Hii ina maana kikao chako cha Azure CLI kinatoa uthibitisho — hakuna funguo za API au siri katika faili yako `.env`. Hii ni [mazoezi bora ya usalama](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Hatua 4: Unda Faili lako `.env`

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Wapi ya kuipata |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → mradi wako → ukurasa wa **Muhtasari** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → jina la modeli uliyoitekeleza |

Hizo ndiyo kwa masomo mengi! Notebooks zitathibitisha moja kwa moja kupitia kikao chako cha `az login`.

### Hatua 5: Sakinisha Utegemezi za Python

```bash|powershell
pip install -r requirements.txt
```

Tunapendekeza kuendesha hili ndani ya mazingira ya virtual uliyounda hapo awali.

## Usanidi wa Ziada kwa Somo la 5 (Agentic RAG)

Somo la 5 linatumia **Azure AI Search** kwa retrieval-augmented generation. Ikiwa unapanga kuendesha somo hilo, ongeza vigezo hivi kwenye faili yako `.env`:

| Variable | Wapi ya kuipata |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → rasilimali yako ya **Azure AI Search** → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → rasilimali yako ya **Azure AI Search** → **Settings** → **Keys** → funguo kuu ya msimamizi |

## Usanidi wa Ziada kwa Somo la 6 na Somo la 8 (GitHub Models)

Baadhi ya notebooks katika masomo 6 na 8 zinatumia **GitHub Models** badala ya Azure AI Foundry. Ikiwa unapanga kuendesha sampuli hizo, ongeza vigezo hivi kwenye faili yako `.env`:

| Variable | Wapi ya kuipata |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Tumia `https://models.inference.ai.azure.com` (thamani ya kawaida) |
| `GITHUB_MODEL_ID` | Jina la modeli kutumia (k.m. `gpt-4o-mini`) |

## Usanidi wa Ziada kwa Somo la 8 (Bing Grounding Workflow)

Notebook ya workflow inayobadilisha kwa masharti katika somo la 8 inatumia **Bing grounding** kupitia Azure AI Foundry. Ikiwa unapanga kuendesha sampuli hiyo, ongeza vigezo hivi kwenye faili yako `.env`:

| Variable | Wapi ya kuipata |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → mradi wako → **Management** → **Connected resources** → muunganisho wako wa Bing → nakili connection ID |

## Kutatua Matatizo

### Makosa ya Uthibitishaji wa Vyeti vya SSL kwenye macOS

Ikiwa uko kwenye macOS na unakutana na kosa kama:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Hili ni tatizo linalojulikana na Python kwenye macOS ambapo vyeti vya SSL vya mfumo havithaminiwi moja kwa moja. Jaribu suluhisho zifuatazo kwa mpangilio:

**Chaguo 1: Endesha skripti ya Install Certificates ya Python (inayopendekezwa)**

```bash
# Badilisha 3.XX na toleo lako la Python lililowekwa (kwa mfano, 3.12 au 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Chaguo 2: Tumia `connection_verify=False` katika notebook yako (kwa notebooks za GitHub Models pekee)**

Katika notebook ya Somo 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), suluhisho lililokomentiwa tayari limejumuishwa. Fungua kutoa komenti `connection_verify=False` unapotengeneza client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Zima uhakiki wa SSL ikiwa unakutana na makosa ya cheti
)
```

> **⚠️ Tahadhari:** Kuzima ukaguzi wa SSL (`connection_verify=False`) kunapunguza usalama kwa kuruka uthibitisho wa cheti. Tumia hili tu kama suluhisho la muda katika mazingira ya maendeleo, wala si katika uzalishaji.

**Chaguo 3: Sakinisha na tumia `truststore`**

```bash
pip install truststore
```

Kisha ongeza yafuatayo juu kabisa ya notebook yako au script kabla ya kufanya simu yoyote za mtandao:

```python
import truststore
truststore.inject_into_ssl()
```

## Umekwama Wapi?

Ikiwa una matatizo yoyote kuendesha usanidi huu, jiunge na <a href="https://discord.gg/kzRShWzttr" target="_blank">Jamii ya Azure AI kwenye Discord</a> au <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">tengeneza issue</a>.

## Somo Lifuatao

Sasa uko tayari kukimbia msimbo wa kozi hii. Furahia kujifunza zaidi kuhusu ulimwengu wa Mawakala wa AI! 

[Utangulizi kwa Mawakala wa AI na Matumizi yao](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Tamko la kutohusika:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya utafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kufanikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au ukosefu wa usahihi. Nyaraka ya awali katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, utafsiri wa kitaalamu unaofanywa na binadamu unashauriwa. Hatuwajibiki kwa uelewa au tafsiri zisizo sahihi zinazotokana na matumizi ya utafsiri huu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->