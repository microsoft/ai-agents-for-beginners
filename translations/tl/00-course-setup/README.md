# Pagsasaayos ng Kurso

## Panimula

Tatalakayin sa leksyon na ito kung paano patakbuhin ang mga halimbawa ng code ng kursong ito.

## Sumali sa Iba pang mga Nag-aaral at Humingi ng Tulong

Bago mo simulan ang pag-clone ng iyong repo, sumali sa [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) upang makakuha ng tulong sa pagsasaayos, mga tanong tungkol sa kurso, o upang makipag-ugnayan sa iba pang mga nag-aaral.

## I-clone o I-fork ang Repo na ito

Upang magsimula, mangyaring i-clone o i-fork ang GitHub Repository. Gagawa ito ng sarili mong bersyon ng materyal ng kurso upang mapatakbo, masubukan, at mabago ang code!

Magagawa ito sa pamamagitan ng pag-click sa link para <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">i-fork ang repo</a>

Dapat mayroon ka na ngayong sariling forked na bersyon ng kursong ito sa sumusunod na link:

![Forked Repo](../../../translated_images/tl/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (inirerekomenda para sa workshop / Codespaces)

  >Maaaring malaki ang buong repository (~3 GB) kapag dina-download mo ang buong kasaysayan at lahat ng mga file. Kung dumadalo ka lamang ng workshop o kailangan mo lamang ng ilang mga folder ng leksyon, ang shallow clone (o sparse clone) ay iniiwasan ang karamihan ng pag-download na iyon sa pamamagitan ng pagpaputol ng kasaysayan at/o pag-skip ng mga blobs.

#### Mabilis na shallow clone — minimal na kasaysayan, lahat ng file

Palitan ang `<your-username>` sa mga utos sa ibaba ng iyong fork URL (o ang upstream URL kung mas gusto mo).

Upang i-clone lamang ang pinakabagong kasaysayan ng commit (maliit na pag-download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Upang i-clone ang isang tiyak na branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal na blobs + tanging mga napiling folder lang

Gumagamit ito ng partial clone at sparse-checkout (nangangailangan ng Git 2.25+ at inirerekomendang modernong Git na may suporta sa partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pumasok sa folder ng repo:

```bash|powershell
cd ai-agents-for-beginners
```

Pagkatapos ay tukuyin kung aling mga folder ang gusto mo (halimbawa sa ibaba ay nagpapakita ng dalawang folder):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Pagkatapos ng pag-clone at pag-verify ng mga file, kung kailangan mo lamang ang mga file at nais makatipid ng espasyo (walang kasaysayan ng git), mangyaring tanggalin ang metadata ng repositoryo (💀hindi na mababawi — mawawala ang lahat ng functionality ng Git: walang commits, pulls, pushes, o access sa kasaysayan).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Paggamit ng GitHub Codespaces (inirerekomenda upang maiwasan ang malalaking lokal na pag-download)

- Gumawa ng bagong Codespace para sa repo na ito sa pamamagitan ng [GitHub UI](https://github.com/codespaces).  

- Sa terminal ng bagong ginawa na codespace, patakbuhin ang isa sa mga utos na shallow/sparse clone sa itaas upang dalhin lamang ang mga folder ng leksyon na kailangan mo papunta sa workspace ng Codespace.
- Opsyonal: pagkatapos ng pag-clone sa loob ng Codespaces, tanggalin ang .git upang mabawi ang dagdag na espasyo (tingnan ang mga utos sa pagtanggal sa itaas).
- Tandaan: Kung mas gusto mong buksan ang repo nang direkta sa Codespaces (nang walang dagdag na clone), tandaan na bubuuin ng Codespaces ang devcontainer environment at maaaring magbibigay pa rin ng higit pa kaysa sa kailangan mo. Ang pag-clone ng shallow na kopya sa loob ng bagong Codespace ay nagbibigay sa iyo ng higit na kontrol sa paggamit ng disk.

#### Mga Tip

- Palaging palitan ang clone URL ng iyong fork kung nais mong mag-edit/komit.
- Kung kakailanganin mo ng higit pang kasaysayan o mga file, maaari mo itong kunin o ayusin ang sparse-checkout upang isama ang karagdagang mga folder.

## Pagpapatakbo ng Code

Nag-aalok ang kursong ito ng serye ng mga Jupyter Notebooks na maaari mong patakbuhin upang magkaroon ng hands-on na karanasan sa paggawa ng AI Agents.

Ginagamit ng mga halimbawa ng code ang **Microsoft Agent Framework (MAF)** kasama ang `FoundryChatClient`, na kumokonekta sa **Microsoft Foundry Agent Service V2** (ang Responses API) sa pamamagitan ng **Microsoft Foundry**.

Lahat ng Python notebooks ay may label na `*-python-agent-framework.ipynb`.

## Mga Kinakailangan

- Python 3.12+
  - **TANDAAN**: Kung wala ka pang naka-install na Python3.12, siguraduhing i-install mo ito. Pagkatapos ay gumawa ng iyong venv gamit ang python3.12 upang masiguro ang tamang mga bersyon na naka-install mula sa requirements.txt na file.
  
    >Halimbawa

    Gumawa ng Python venv directory:

    ```bash|powershell
    python -m venv venv
    ```

    Pagkatapos ay i-activate ang venv na kapaligiran para sa:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Para sa mga sample code na gumagamit ng .NET, tiyakin na naka-install ang [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o mas bago. Pagkatapos, suriin ang bersyon ng .NET SDK na naka-install:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Kinakailangan para sa pagpapatunay. Mag-install mula sa [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Para sa pag-access sa Microsoft Foundry at Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Isang proyekto na may na-deploy na modelo (hal., `gpt-5-mini`). Tingnan ang [Hakbang 1](#hakbang-1-gumawa-ng-microsoft-foundry-project) sa ibaba.

Kasama sa repositoryo na ito ang `requirements.txt` na file sa root na naglalaman ng lahat ng kinakailangang Python na mga package para patakbuhin ang mga halimbawa ng code.

Maaari mo itong i-install sa pamamagitan ng pagpapatakbo ng sumusunod na utos sa iyong terminal sa root ng repositoryo:

```bash|powershell
pip install -r requirements.txt
```

Inirerekomenda naming gumawa ng isang Python virtual na kapaligiran upang maiwasan ang mga conflict at problema.

## Pagsasaayos ng VSCode

Siguraduhing ginagamit mo ang tamang bersyon ng Python sa VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Isaayos ang Microsoft Foundry at Microsoft Foundry Agent Service

### Hakbang 1: Gumawa ng Microsoft Foundry Project

Kailangan mo ng Microsoft Foundry **hub** at **project** na may na-deploy na modelo upang mapatakbo ang mga notebooks.

1. Pumunta sa [ai.azure.com](https://ai.azure.com) at mag-sign in gamit ang iyong Azure account.
2. Gumawa ng isang **hub** (o gamitin ang isang umiiral). Tingnan: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Sa loob ng hub, gumawa ng isang **project**.
4. I-deploy ang isang modelo (hal., `gpt-5-mini`) mula sa **Models + Endpoints** → **Deploy model**.

### Hakbang 2: Kunin ang Iyong Project Endpoint at Pangalan ng Model Deployment

Mula sa iyong proyekto sa Microsoft Foundry portal:

- **Project Endpoint** — Pumunta sa pahina ng **Overview** at i-copy ang endpoint URL.

![Project Connection String](../../../translated_images/tl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Pumunta sa **Models + Endpoints**, piliin ang iyong na-deploy na modelo, at tandaan ang **Deployment name** (hal., `gpt-5-mini`).

### Hakbang 3: Mag-sign in sa Azure gamit ang `az login`


Lahat ng notebook ay gumagamit ng **`AzureCliCredential`** para sa pag-authenticate — walang mga API key na kailangan pang pamahalaan. Nangangailangan ito na naka-sign in ka gamit ang Azure CLI.

1. **I-install ang Azure CLI** kung hindi mo pa nagagawa: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Mag-sign in** sa pamamagitan ng pagpapatakbo:

    ```bash|powershell
    az login
    ```

    O kung ikaw ay nasa remote/Codespace na kapaligiran na walang browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Pumili ng iyong subscription** kung may lalabas na prompt — piliin ang naglalaman ng iyong Foundry project.

4. **Suriin** kung ikaw ay naka-sign in:

    ```bash|powershell
    az account show
    ```

> **Bakit `az login`?** Nag-a-authenticate ang mga notebook gamit ang `AzureCliCredential` mula sa `azure-identity` package. Ibig sabihin, ang iyong Azure CLI session ang nagsisilbing kredensyal — walang API keys o mga sikreto sa iyong `.env` file. Ito ay isang [pinakamahusay na kasanayan sa seguridad](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Hakbang 4: Gumawa ng Iyong `.env` File

Kopyahin ang halimbawa ng file:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Buksan ang `.env` at punan ang dalawang halagang ito:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → iyong proyekto → **Overview** na pahina |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → pangalan ng iyong na-deploy na modelo |

Iyon lang para sa karamihan ng mga leksyon! Mag-a-authenticate ang mga notebook nang awtomatiko sa pamamagitan ng iyong `az login` session.

### Hakbang 5: I-install ang mga Dependency ng Python

```bash|powershell
pip install -r requirements.txt
```

Inirerekomenda naming patakbuhin ito sa loob ng virtual environment na ginawa mo kanina.

## Karagdagang Setup para sa Leksyon 5 (Agentic RAG)

Gumagamit ang Leksyon 5 ng **Azure AI Search** para sa retrieval-augmented generation. Kung balak mong patakbuhin ang leksyon na iyon, idagdag ang mga variable na ito sa iyong `.env` file:

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → ang iyong **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → ang iyong **Azure AI Search** resource → **Settings** → **Keys** → pangunahing admin key |

## Karagdagang Setup para sa Mga Leksyon na Direktang Tumatawag sa Azure OpenAI (Mga Leksyon 6 at 8)

Ang ilang notebook sa mga leksyon 6 at 8 ay direktang tumatawag sa **Azure OpenAI** (gamit ang **Responses API**) sa halip na dumaan sa Microsoft Foundry project. Ginamit ng mga sample na ito noon ang GitHub Models, na deprecated na (tatapusin sa Hulyo 2026) at hindi sumusuporta sa Responses API. Kung balak mong patakbuhin ang mga sample na ito, idagdag ang mga variable na ito sa iyong `.env` file:

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → iyong **Azure OpenAI** resource → **Keys and Endpoint** → Endpoint (hal. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Pangalan ng iyong na-deploy na modelo (hal. `gpt-5-mini`) na sumusuporta sa Responses API |
| `AZURE_OPENAI_API_KEY` | Opsyonal — kung gumagamit ka ng key-based na authentication sa halip na `az login` / Entra ID |

> Ginagamit ng Responses API ang stable na `/openai/v1/` endpoint, kaya hindi kailangan ang `api-version`. Mag-sign in gamit ang `az login` para gumamit ng keyless na Entra ID authentication.

## Alternatibong Provider: MiniMax (OpenAI-Compatible)

Nagbibigay ang [MiniMax](https://platform.minimaxi.com/) ng malalaking-context na mga modelo (hanggang 204K tokens) sa pamamagitan ng OpenAI-compatible na API. Dahil ang Microsoft Agent Framework na `OpenAIChatClient` ay gumagana sa anumang OpenAI-compatible na endpoint, maaari mong gamitin ang MiniMax bilang alternatibong drop-in sa Azure OpenAI o OpenAI.

Idagdag ang mga variable na ito sa iyong `.env` file:

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Gamitin ang `https://api.minimax.io/v1` (default na halaga) |
| `MINIMAX_MODEL_ID` | Pangalan ng modelong gagamitin (hal., `MiniMax-M3`) |

**Mga halimbawa ng modelo**: `MiniMax-M3` (inirerekomenda), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (mas mabilis na mga tugon). Maaaring magbago ang mga pangalan at availability ng modelo sa paglipas ng panahon, at ang akses sa isang tiyak na modelo ay maaaring depende sa iyong account o rehiyon — tingnan ang [MiniMax Platform](https://platform.minimaxi.com/) para sa kasalukuyang listahan. Kung hindi available sa iyong account ang `MiniMax-M3`, itakda ang `MINIMAX_MODEL_ID` sa isang modelong may akses ka (hal. `MiniMax-M2.7`).

Ang mga sample ng code na gumagamit ng `OpenAIChatClient` (hal., workflow ng hotel booking sa Leksyon 14) ay awtomatikong magde-detect at gagamitin ang iyong MiniMax configuration kapag naka-set ang `MINIMAX_API_KEY`.

## Alternatibong Provider: Foundry Local (Patakbuhin ang Mga Modelo Sa Iyong Device)

Ang [Foundry Local](https://foundrylocal.ai) ay isang magaan na runtime na nagda-download, namamahala, at nagseserbisyo ng mga language model **nasa sariling makina mo** sa pamamagitan ng OpenAI-compatible na API — walang cloud, walang Azure subscription, at walang API keys. Magandang opsyon ito para sa offline na development, pagsubok nang hindi gumagastos sa cloud, o pagpapanatili ng data sa device.

Dahil gumagana ang Microsoft Agent Framework na `OpenAIChatClient` sa anumang OpenAI-compatible na endpoint, ang Foundry Local ay isang lokal na alternatibo sa Azure OpenAI.

**1. I-install ang Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. I-download at patakbuhin ang isang modelo** (sinisimulan din nito ang lokal na serbisyo):

```bash
foundry model list          # tingnan ang mga available na modelo
foundry model run phi-4-mini
```

**3. I-install ang Python SDK** na ginagamit para ma-discover ang lokal na endpoint:

```bash
pip install foundry-local-sdk
```

**4. Ituro ang Microsoft Agent Framework sa iyong lokal na modelo:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Ida-download (kung kinakailangan) at ihahain ang modelo nang lokal, pagkatapos ay hahanapin ang endpoint/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # hal. http://localhost:<port>/v1
    api_key=manager.api_key,        # palaging "not-required" para sa Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Tandaan:** Nag-e-expose ang Foundry Local ng OpenAI-compatible na **Chat Completions** endpoint. Gamitin ito para sa lokal na development at offline na mga sitwasyon. Para sa buong set ng features ng **Responses API** (stateful na mga pag-uusap, malalim na orchestration ng tool, at agent-style na development), gamitin ang **Azure OpenAI** o ang **Microsoft Foundry** project tulad ng ipinapakita sa mga leksyon. Tingnan ang [Foundry Local documentation](https://foundrylocal.ai) para sa kasalukuyang katalogo ng mga modelo at suportang platform.


## Karagdagang Pagsasaayos para sa Aralin 8 (Bing Grounding Workflow)


Ang conditional workflow notebook sa lesson 8 ay gumagamit ng **Bing grounding** sa pamamagitan ng Microsoft Foundry. Kung plano mong patakbuhin ang sample na iyon, idagdag ang variable na ito sa iyong `.env` file:

| Variable | Saan ito makikita |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → iyong proyekto → **Management** → **Connected resources** → ang iyong Bing connection → kopyahin ang connection ID |

## Pag-aayos ng Problema

### Mga Error sa SSL Certificate Verification sa macOS

Kung ikaw ay nasa macOS at makaranas ng error tulad ng:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ito ay isang kilalang isyu sa Python sa macOS kung saan ang system SSL certificates ay hindi awtomatikong pinagkakatiwalaan. Subukan ang mga sumusunod na solusyon sa pagkakasunod-sunod:

**Opsyon 1: Patakbuhin ang Install Certificates script ng Python (inirerekomenda)**

```bash
# Palitan ang 3.XX ng iyong naka-install na bersyon ng Python (halimbawa, 3.12 o 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opsyon 2: Gamitin ang `connection_verify=False` sa iyong notebook (para lang sa GitHub Models notebooks)**

Sa Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), may naka-comment out na workaround na kasama na. I-undo ang pagkakacomment sa `connection_verify=False` kapag gumagawa ng client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Patayin ang SSL verification kung makaranas ng mga error sa sertipiko
)
```

> **⚠️ Babala:** Ang pag-disable ng SSL verification (`connection_verify=False`) ay nagpapababa ng seguridad dahil nilalaktawan nito ang certificate validation. Gamitin ito bilang pansamantalang solusyon lamang sa development environment, huwag sa production.

**Opsyon 3: I-install at gamitin ang `truststore`**

```bash
pip install truststore
```

Pagkatapos, idagdag ang sumusunod sa itaas ng iyong notebook o script bago gumawa ng anumang network calls:

```python
import truststore
truststore.inject_into_ssl()
```

## Naka-stuck sa Isang Lugar?

Kung mayroon kang anumang mga isyu sa pagpapatakbo ng setup na ito, sumali sa aming <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> o <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">gumawa ng isang isyu</a>.

## Susunod na Aralin

Handa ka nang patakbuhin ang code para sa kursong ito. Maligayang pag-aaral pa tungkol sa mundo ng AI Agents!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->