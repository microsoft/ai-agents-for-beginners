# Setup ng Kurso

## Panimula

Tatalakayin sa leksyong ito kung paano patakbuhin ang mga halimbawa ng code ng kursong ito.

## Sumali sa Iba Pang mga Nag-aaral at Humingi ng Tulong

Bago ka magsimulang i-clone ang iyong repo, sumali sa [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) para makakuha ng tulong sa setup, mga tanong tungkol sa kurso, o para makipag-ugnayan sa iba pang mga nag-aaral.

## I-clone o I-fork ang Repo na Ito

Upang magsimula, mangyaring i-clone o i-fork ang GitHub Repository. Ito ay gagawa ng sarili mong bersyon ng materyal ng kurso upang maaari mong patakbuhin, subukan, at i-tweak ang code!

Magagawa ito sa pamamagitan ng pag-click sa link upang <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">i-fork ang repo</a>

Dapat ay mayroon ka nang iyong sariling forked na bersyon ng kursong ito sa sumusunod na link:

![Forked Repo](../../../translated_images/tl/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (inirerekomenda para sa workshop / Codespaces)

  >Maaaring maging malaki (~3 GB) ang buong repository kapag dina-download mo ang buong kasaysayan at lahat ng mga file. Kung dadalo ka lamang sa workshop o kailangan mo lamang ng ilang folder ng leksyon, ang shallow clone (o sparse clone) ay magda-download ng mas kaunti.

#### Mabilis na shallow clone — minimal na kasaysayan, lahat ng mga file

Palitan ang `<your-username>` sa mga sumusunod na utos ng iyong fork URL (o ang upstream URL kung nais mo).

Para mag-clone lamang ng pinakabagong kasaysayan ng commit (maliit na download):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Para mag-clone ng isang partikular na sanga:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal blobs + pili lamang na mga folder

Ginagamit nito ang partial clone at sparse-checkout (nangangailangan ng Git 2.25+ at inirerekomenda ang modernong Git na may suporta sa partial clone):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pumasok sa folder ng repo:

```bash
cd ai-agents-for-beginners
```

Pagkatapos tukuyin kung aling mga folder ang gusto mo (halimbawa sa ibaba ay ipinapakita ang dalawang folder):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Pagkatapos i-clone at i-verify ang mga file, kung kailangan mo lamang ng mga file at nais mong magbakante ng espasyo (walang kasaysayan ng git), pakibura ang repository metadata (💀irereversible — mawawala ang lahat ng functionality ng Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Paggamit ng GitHub Codespaces (inirerekomenda para maiwasan ang malalaking lokal na download)

- Gumawa ng bagong Codespace para sa repo na ito gamit ang [GitHub UI](https://github.com/codespaces).  

- Sa terminal ng bagong ginawa na codespace, patakbuhin ang isa sa mga shallow/sparse clone na mga utos sa itaas upang dalhin lamang ang mga folder ng leksyon na kailangan mo sa Codespace workspace.
- Opsyonal: pagkatapos mag-clone sa loob ng Codespaces, alisin ang .git para makabawi ng dagdag na espasyo (tingnan ang mga utos sa pagtanggal sa itaas).
- Tandaan: Kung mas gusto mong buksan ang repo direkta sa Codespaces (nang walang dagdag na clone), alamin na bubuuin pa rin ng Codespaces ang devcontainer environment at maaaring mag-provide pa rin ng higit kaysa sa kailangan mo.

#### Mga Tip

- Palaging palitan ang clone URL ng iyong fork kung gusto mong mag-edit/mag-commit.
- Kung kakailanganin mo ng mas maraming kasaysayan o mga file sa susunod, maaari mo silang i-fetch o i-adjust ang sparse-checkout upang isama ang karagdagang mga folder.

## Pagpapatakbo ng Code

Nag-aalok ang kursong ito ng isang serye ng Jupyter Notebooks na maaari mong patakbuhin upang magkaroon ng hands-on na karanasan sa pagbuo ng AI Agents.

Gumagamit ang mga halimbawa ng code ng **Microsoft Agent Framework (MAF)** gamit ang `FoundryChatClient`, na kumokonekta sa **Microsoft Foundry Agent Service V2** (ang Responses API) sa pamamagitan ng **Microsoft Foundry**.

Lahat ng Python notebooks ay may label na `*-python-agent-framework.ipynb`.

## Mga Kinakailangan

- Python 3.12+
  - **TANDAAN**: Kung wala ka pang naka-install na Python3.12, tiyaking mai-install mo ito. Pagkatapos, gumawa ng iyong venv gamit ang python3.12 upang matiyak na tama ang mga bersyon na mai-install mula sa requirements.txt file.
  
    >Halimbawa

    Gumawa ng Python venv directory:

    ```bash
    python -m venv venv
    ```

    Pagkatapos i-activate ang venv environment para sa:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Para sa mga sample code gamit ang .NET, tiyaking na-install mo ang [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o mas bago. Pagkatapos, suriin ang naka-install mong bersyon ng .NET SDK:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Kinakailangan para sa authentication. I-install mula sa [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Para sa akses sa Microsoft Foundry at Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Isang proyekto na may naka-deploy na modelo (hal., `gpt-5-mini`). Tingnan ang [Step 1](#hakbang-1-gumawa-ng-microsoft-foundry-project) sa ibaba.

May kasama kaming `requirements.txt` file sa root ng repositoryong ito na naglalaman ng lahat ng kailangang Python packages para patakbuhin ang mga halimbawa ng code.

Maaari mo itong i-install sa pamamagitan ng pagpapatakbo ng sumusunod na utos sa iyong terminal sa root ng repository:

```bash
pip install -r requirements.txt
```

Inirerekumenda namin ang paggawa ng Python virtual environment upang maiwasan ang anumang salungatan at problema.

## Setup ng VSCode

Tiyaking ginagamit mo ang tamang bersyon ng Python sa VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## I-Set Up ang Microsoft Foundry at Microsoft Foundry Agent Service

### Hakbang 1: Gumawa ng Microsoft Foundry Project

Kailangan mo ng Microsoft Foundry **hub** at **project** na may naka-deploy na modelo upang patakbuhin ang mga notebook.

1. Pumunta sa [ai.azure.com](https://ai.azure.com) at mag-sign in gamit ang iyong Azure account.
2. Gumawa ng **hub** (o gamitin ang isang umiiral na). Tingnan: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Sa loob ng hub, gumawa ng **project**.
4. Mag-deploy ng modelo (hal., `gpt-5-mini`) mula sa **Models + Endpoints** → **Deploy model**.

### Hakbang 2: Kunin ang Iyong Project Endpoint at Pangalan ng Model Deployment

Mula sa iyong proyekto sa Microsoft Foundry portal:

- **Project Endpoint** — Pumunta sa pahina ng **Overview** at kopyahin ang URL ng endpoint.

![Project Connection String](../../../translated_images/tl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Pangalan ng Model Deployment** — Pumunta sa **Models + Endpoints**, piliin ang iyong na-deploy na modelo, at tandaan ang **Pangalan ng Deployment** (hal., `gpt-5-mini`).

### Hakbang 3: Mag-sign in sa Azure gamit ang `az login`

Karamihan sa mga notebook ay nag-authenticate sa pamamagitan ng iyong **Azure CLI sign-in** — gamit ang `AzureCliCredential` o `DefaultAzureCredential` (parehong kinukuha ang iyong `az login` session) mula sa `azure-identity` package — kaya hindi nila kailangan ng mga API key. Ilang leksyon at opsyonal na mga integrasyon ay gumagamit ng API keys; suriin ang mga kinakailangan ng bawat leksyon para sa iba pang mga environment variable. Kinakailangan na naka-sign in ka sa Azure CLI.

1. **I-install ang Azure CLI** kung hindi mo pa nagagawa: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Mag-sign in** sa pamamagitan ng pagpapatakbo:

    ```bash
    az login
    ```

    O kung nasa remote/Codespace environment ka nang walang browser:

    ```bash
    az login --use-device-code
    ```

3. **Piliin ang iyong subscription** kung papipiliin — piliin ang naglalaman ng iyong Foundry project.

4. **Suriin** kung naka-sign in ka:

    ```bash
    az account show
    ```

> **Bakit `az login`?** Ang mga notebook ay nag-authenticate gamit ang `AzureCliCredential` (o `DefaultAzureCredential`, na kumukuha rin ng iyong Azure CLI sign-in) mula sa `azure-identity` package. Ibig sabihin nito ay ang iyong Azure CLI session ang nagbibigay ng mga kredensyal — walang API key o sikreto sa iyong `.env` file. Ito ay isang [pinakamahusay na kasanayan sa seguridad](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

| Variable | Saan ito makikita |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → iyong proyekto → pahina ng **Overview** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → pangalan ng iyong na-deploy na modelo |

Iyon na para sa karamihan ng mga leksyon! Ang mga notebook ay mag-authenticate nang awtomatiko sa pamamagitan ng iyong `az login` session.

### Hakbang 5: I-install ang Mga Depedensiya ng Python

```bash
pip install -r requirements.txt
```

Inirerekomenda namin na patakbuhin ito sa loob ng virtual environment na ginawa mo kanina.

## Opsyonal na Setup: Azure AI Search (Mga Leksiyon 5 at 16)

Ang Mga Notebook ng Leksiyon 5 (Agentic RAG) at Leksiyon 16 ay tumatakbo agad gamit ang isang **in-memory knowledge base** — walang karagdagang Azure resources na kailangan. Kung nais mong suportahan ang mga ito gamit ang totoong **Azure AI Search** index, tandaan na ang **Lesson 16 notebook ay kasalukuyang gumagamit ng key-based authentication**: lumilipat ito mula sa in-memory search papuntang Azure AI Search lamang kapag **parehong** nakaset ang `AZURE_SEARCH_SERVICE_ENDPOINT` **at** `AZURE_SEARCH_API_KEY`, kung hindi ay nananatili ito sa in-memory search — kaya upang patakbuhin ito laban sa tunay na index kailangang itakda ang admin key din. Ang keyless authentication gamit ang Microsoft Entra ID (RBAC) ay ang inirerekomendang pamamaraan para sa sariling production code, na pareho sa `az login` flow na ginagamit sa ibang bahagi ng kursong ito.

Ang mga hakbang ng RBAC sa ibaba ay para sa setup-guide samples at sa sarili mong code. Hindi nito pina-enable ang keyless authentication sa Lesson 16 notebook; kailangan pa rin nito ang parehong endpoint at admin key para gamitin ang Azure AI Search.

1. **I-enable ang role-based access** sa iyong search service:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **I-assign sa sarili mo ang mga kinakailangang roles** (gumawa/mag-load ng mga index at query):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Idagdag ang endpoint** sa iyong `.env` file:

| Variable | Saan ito makikita |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → iyong **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Kinakailangan (kasama ng endpoint) upang paganahin ang Azure AI Search sa Lesson 16 notebook, na gumagamit ng key-based auth. Azure portal → **Settings** → **Keys** → pangunahing admin key |

> **Bakit keyless?** Ang mga admin key ay nagbibigay ng buong write access sa iyong search service at maaaring malantad sa pamamagitan ng `.env` files. Sa RBAC, ang iyong `az login` identity ang ginagamit sa halip — ang parehong keyless Entra ID pattern na ginagamit ng mga notebook ng kurso (sa pamamagitan ng `AzureCliCredential` / `DefaultAzureCredential`). Tingnan ang [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

Tingnan ang [Azure AI Search setup guide](./AzureSearch.md) para sa mga buong halimbawa ng paglikha ng index sa Python at .NET.

## Karagdagang Setup para sa Mga Leksiyon na Direktang Tumatawag sa Azure OpenAI (Mga Leksiyon 6 at 8)

Ilang mga notebook sa mga leksiyon 6 at 8 ay direktang tumatawag sa **Azure OpenAI** (gamit ang **Responses API**) sa halip na dumaan sa Microsoft Foundry project. Ang mga halimbawang ito ay dating gumagamit ng GitHub Models, na deprecated na at hindi sumusuporta sa Responses API. Idagdag ang mga variable na ito sa iyong `.env` file:

| Variable | Saan ito makikita |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → iyong **Azure OpenAI** resource → **Keys and Endpoint** → Endpoint (hal., `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Pangalan ng iyong na-deploy na modelo (hal., `gpt-5-mini`) na sumusuporta sa Responses API |
| `AZURE_OPENAI_API_KEY` | Opsyonal — kung gagamit ka ng key-based auth sa halip na `az login` / Entra ID |

> Ginagamit ng Responses API ang matatag na `/openai/v1/` endpoint, kaya hindi kailangan ng `api-version`. Mag-sign in gamit ang `az login` para sa keyless Entra ID authentication.

## Alternatibong Provider: MiniMax (OpenAI-Compatible)

Nagbibigay ang [MiniMax](https://platform.minimaxi.com/) ng malalaking context na mga modelo (hanggang 204K tokens) sa pamamagitan ng OpenAI-compatible API. Dahil gumagana ang Microsoft Agent Framework's `OpenAIChatClient` sa kahit anong OpenAI-compatible endpoint, magagamit mo ang MiniMax bilang kapalit para sa mga leksiyon na gumagamit ng `OpenAIChatClient`.

Idagdag ang mga variable na ito sa iyong `.env` file:

| Variable | Saan ito makikita |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Gamitin ang `https://api.minimax.io/v1` (default na halaga) |
| `MINIMAX_MODEL_ID` | Pangalan ng modelong gagamitin (hal., `MiniMax-M3`) |

**Mga Halimbawang modelo**: `MiniMax-M3` (inirerekomenda), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (mas mabilis ang mga tugon). Maaaring magbago ang mga pangalan at availability ng modelo sa paglipas ng panahon, at ang akses sa isang modelo ay maaaring depende sa iyong account.

Ang mga halimbawa ng code na gumagamit ng `OpenAIChatClient` (hal., workflow ng Lesson 14 sa hotel booking) ay awtomatikong makakakita at gagamitin ang iyong MiniMax configuration kapag nakaset ang `MINIMAX_API_KEY`.


## Alternatibong Tagabigay: Foundry Local (Patakbuhin ang mga Modelo sa Device)

[Foundry Local](https://foundrylocal.ai) ay isang magaan na runtime na nagda-download, nagma-manage, at nagseserbisyo ng mga language model **entirely on your own machine** sa pamamagitan ng isang OpenAI-compatible API — walang kinakailangang cloud.

Dahil ang Microsoft Agent Framework's `OpenAIChatClient` ay gumagana sa anumang OpenAI-compatible na endpoint, ang Foundry Local ay isang lokal na alternatibo na pwedeng ipalit sa Azure OpenAI.

**1. I-install ang Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. I-download at patakbuhin ang isang modelo** (nagsisimula rin ito ng lokal na serbisyo):

```bash
foundry model list          # tingnan ang mga magagamit na modelo
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

# Nagda-download (kung kailangan) at naghahain ng modelo nang lokal, pagkatapos ay hinahanap ang endpoint/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # hal. http://localhost:<port>/v1
    api_key=manager.api_key,        # palaging "hindi-kailangan" para sa Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Tandaan:** Nagbibigay ang Foundry Local ng OpenAI-compatible na **Chat Completions** endpoint. Gamitin ito para sa lokal na development at offline na mga sitwasyon. Para sa buong set ng mga feature ng **Responses API** (stateful conversations, atbp.), gamitin ang Azure OpenAI o isang Microsoft Foundry na proyekto.

## Karagdagang Setup para sa Lesson 8 (Bing Grounding Workflow)

Ang conditional workflow notebook sa lesson 8 ay gumagamit ng **Bing grounding** sa pamamagitan ng Microsoft Foundry. Kung balak mong patakbuhin ang sample na iyon, idagdag ang variable na ito sa iyong `.env` file:

| Variable | Saan ito mahahanap |
|----------|--------------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → ang iyong proyekto → **Management** → **Connected resources** → ang iyong Bing connection → kopyahin ang connection ID |

## Pag-troubleshoot

### Mga Error sa SSL Certificate Verification sa macOS

Kung ikaw ay nasa macOS at nakakaranas ng error tulad ng:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ito ay isang kilalang isyu sa Python sa macOS kung saan ang system SSL certificates ay hindi awtomatikong pinagkakatiwalaan. Subukan ang mga sumusunod na solusyon nang sunud-sunod:

**Opsyon 1: Patakbuhin ang Install Certificates script ng Python (inirerekomenda)**

```bash
# Palitan ang 3.XX ng iyong naka-install na bersyon ng Python (hal., 3.12 o 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opsyon 2: Gamitin ang `connection_verify=False` sa iyong notebook (para lamang sa GitHub Models notebooks)**

Sa Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), may nakacomment na workaround na kasama na. I-uncomment ang `connection_verify=False` kapag nakatagpo ka ng certificate errors:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # I-disable ang SSL verification kung makaranas ka ng mga error sa sertipiko
)
```

> **⚠️ Babala:** Ang pag-disable ng SSL verification (`connection_verify=False`) ay nagpapababa ng seguridad sa pamamagitan ng pag-skip sa certificate validation. Gamitin lamang ito bilang pansamantalang workaround sa mga development environment. Huwag kailanman gamitin ito sa production.

**Opsyon 3: I-install at gamitin ang `truststore`**

```bash
pip install truststore
```

Pagkatapos idagdag ang sumusunod sa taas ng iyong notebook o script bago gumawa ng anumang tawag sa network:

```python
import truststore
truststore.inject_into_ssl()
```

## Nahirapan Ka Ba sa Kung Saan?

Kung may mga isyu ka sa pagpapatakbo ng setup na ito, sumali sa aming <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> o <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">gumawa ng isyu</a>.

## Susunod na Aralin

Handang-handa ka nang patakbuhin ang code para sa kursong ito. Maligayang pag-aaral ng higit pa tungkol sa mundo ng AI Agents!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->