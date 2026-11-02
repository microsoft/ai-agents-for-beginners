# Setup ng Kurso

## Panimula

Tatalakayin sa araling ito kung paano patakbuhin ang mga halimbawa ng code sa kursong ito.

## Sumali sa Iba Pang mga Nag-aaral at Humingi ng Tulong

Bago ka magsimulang mag-clone ng iyong repo, sumali sa [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) upang humingi ng tulong sa setup, anumang mga tanong tungkol sa kurso, o upang makipag-ugnayan sa ibang mga nag-aaral.

## I-clone o I-fork ang Repo na ito

Upang magsimula, mangyaring i-clone o i-fork ang GitHub Repository. Ito ay gagawa ng sarili mong bersyon ng mga materyal ng kurso upang mapatakbo, masubukan, at maiayos mo ang code!

Magagawa ito sa pamamagitan ng pag-click sa link para <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">i-fork ang repo</a>

Dapat mayroon ka na ngayong sariling forked na bersyon ng kursong ito sa sumusunod na link:

![Forked Repo](../../../translated_images/tl/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (inirerekomenda para sa workshop / Codespaces)

  >Ang buong repositoryo ay maaaring malaki (~3 GB) kapag dina-download mo ang buong kasaysayan at lahat ng mga file. Kung dadalo ka lang sa workshop o kailangan mo lang ang ilang folder ng aralin, ang shallow clone (o sparse clone) ay nagda-download ng mas kaunti.

#### Mabilis na shallow clone — minimal na kasaysayan, lahat ng file

Palitan ang `<your-username>` sa mga utos sa ibaba ng iyong fork URL (o ang upstream URL kung mas gusto mo).

Para i-clone lang ang pinakabagong commit history (maliit na download):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Para i-clone ang isang partikular na branch:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal blobs + piniling mga folder lang

Ginagamit nito ang partial clone at sparse-checkout (nangangailangan ng Git 2.25+ at inirerekomendang modernong Git na may partial clone support):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pumasok sa folder ng repo:

```bash
cd ai-agents-for-beginners
```

Pagkatapos tukuyin kung aling mga folder ang gusto mo (ang halimbawa sa ibaba ay nagpapakita ng dalawang folder):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Matapos i-clone at beripikahin ang mga file, kung kailangan mo lang ng mga file at gusto mong magbakante ng espasyo (walang kasaysayan ng git), pakitanggal ang repository metadata (💀hindi na maibabalik — mawawala lahat ng functionality ng Git):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Paggamit ng GitHub Codespaces (inirerekomenda upang maiwasan ang malalaking lokal na download)

- Gumawa ng bagong Codespace para sa repo na ito sa pamamagitan ng [GitHub UI](https://github.com/codespaces).  

- Sa terminal ng bagong likhang codespace, patakbuhin ang isa sa mga shallow/sparse clone na utos sa itaas upang kunin lang ang lesson folders na kailangan mo sa Codespace workspace.
- Opsyonal: pagkatapos mag-clone sa Codespaces, alisin ang .git para makabawi ng dagdag na espasyo (tingnan ang mga utos ng pag-aalis sa itaas).
- Tandaan: Kung gusto mong direktang buksan ang repo sa Codespaces (walang dagdag na clone), maging maingat dahil bubuuin ng Codespaces ang devcontainer environment at maaaring mag-provision pa rin ng higit pa sa kailangan mo.

#### Mga Tip

- Palaging palitan ang clone URL ng iyong fork kung gusto mong i-edit/commit.
- Kung kakailanganin mo ng mas maraming kasaysayan o mga file, maaari mo silang kunin (fetch) o i-adjust ang sparse-checkout para isama ang karagdagang mga folder.

## Pagpapatakbo ng Code

Nagbibigay ang kursong ito ng serye ng Jupyter Notebooks na maaari mong patakbuhin upang magkaroon ng hands-on na karanasan sa pagbuo ng AI Agents.

Ginagamit ng mga halimbawa ng code ang **Microsoft Agent Framework (MAF)** gamit ang `FoundryChatClient`, na kumokonekta sa **Microsoft Foundry Agent Service V2** (ang Responses API) sa pamamagitan ng **Microsoft Foundry**.

Lahat ng Python notebooks ay may label na `*-python-agent-framework.ipynb`.

## Mga Kinakailangan

- Python 3.12+
  - **TANDAAN**: Kung wala ka pang naka-install na Python3.12, siguraduhing i-install ito. Pagkatapos ay gumawa ng iyong venv gamit ang python3.12 upang masiguro na ang tamang mga bersyon ay na-install mula sa requirements.txt file.
  
    >Halimbawa

    Gumawa ng directory para sa Python venv:

    ```bash
    python -m venv venv
    ```

    Pagkatapos aktibahin ang venv environment para sa:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Para sa mga sample code gamit ang .NET, siguraduhing naka-install ang [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o mas bago. Pagkatapos, tingnan ang iyong naka-install na bersyon ng .NET SDK:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Kinakailangan para sa authentication. I-install mula sa [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Para sa access sa Microsoft Foundry at Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Isang proyekto na may deployed na modelo (hal., `gpt-5-mini`). Tingnan ang [Hakbang 1](#hakbang-1-gumawa-ng-microsoft-foundry-project) sa ibaba.

Naka-include sa root ng repositoryo ang `requirements.txt` file na naglalaman ng lahat ng kinakailangang Python packages para mapatakbo ang mga halimbawa ng code.

Maaari mong i-install ang mga ito sa pamamagitan ng pagpapatakbo ng sumusunod na utos sa iyong terminal sa root ng repositoryo:

```bash
pip install -r requirements.txt
```

Inirerekomenda naming gumawa ng Python virtual environment upang maiwasan ang anumang mga conflict at isyu.

## Setup ng VSCode

Siguraduhin na ginagamit mo ang tamang bersyon ng Python sa VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## I-setup ang Microsoft Foundry at Microsoft Foundry Agent Service

### Hakbang 1: Gumawa ng Microsoft Foundry Project

Kailangan mo ng Microsoft Foundry **hub** at **project** na may deployed na modelo upang mapatakbo ang notebooks.

1. Pumunta sa [ai.azure.com](https://ai.azure.com) at mag-sign in gamit ang iyong Azure account.
2. Gumawa ng **hub** (o gamitin ang isang umiiral na). Tingnan: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Sa loob ng hub, gumawa ng isang **project**.
4. Ideploy ang isang modelo (hal., `gpt-5-mini`) mula sa **Models + Endpoints** → **Deploy model**.

### Hakbang 2: Kunin ang Endpoint ng Project at Pangalan ng Deployment ng Modelo

Mula sa iyong proyekto sa Microsoft Foundry portal:

- **Project Endpoint** — Pumunta sa **Overview** na pahina at kopyahin ang URL ng endpoint.

![Project Connection String](../../../translated_images/tl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Pumunta sa **Models + Endpoints**, piliin ang iyong deployed na modelo, at tandaan ang **Deployment name** (hal., `gpt-5-mini`).

### Hakbang 3: Mag-sign in sa Azure gamit ang `az login`

Karamihan sa mga notebooks ay nag-a-authenticate sa pamamagitan ng iyong **Azure CLI sign-in** — gamit ang `AzureCliCredential` o `DefaultAzureCredential` (kapwa kumukuha ng iyong `az login` session) mula sa `azure-identity` package — kaya hindi na kailangan ng API keys. Ilang leksiyon at opsyonal na integrasyon ay gumagamit ng API keys; tingnan ang prerequisites ng bawat leksiyon para sa anumang karagdagang environment variables. Nangangailangan ito na nakalog-in ka sa Azure CLI.

1. **I-install ang Azure CLI** kung hindi mo pa nagagawa: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Mag-sign in** sa pamamagitan ng pagpapatakbo ng:

    ```bash
    az login
    ```

    O kung nasa remote/Codespace ka na walang browser:

    ```bash
    az login --use-device-code
    ```

3. **Piliin ang iyong subscription** kapag hiningan — piliin ang naglalaman ng iyong Foundry project.

4. **Beripikahin** na naka-sign in ka:

    ```bash
    az account show
    ```

> **Bakit `az login`?** Nag-a-authenticate ang mga notebooks gamit ang `AzureCliCredential` (o `DefaultAzureCredential`, na kumukuha rin ng iyong Azure CLI sign-in) mula sa `azure-identity` package. Ibig sabihin nito, ang Azure CLI session mo ang nagbibigay ng credentials — wala nang API keys o secrets sa iyong `.env` file. Ito ay isang [security best practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Hakbang 4: Gumawa ng Iyong `.env` File

Kopyahin ang halimbawa na file:

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
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → pangalan ng deployed na modelo |

Iyon na para sa karamihan sa mga leksiyon! Mag-a-authenticate nang awtomatiko ang mga notebooks sa pamamagitan ng iyong `az login` session.

### Hakbang 5: Mag-install ng Python Dependencies

```bash
pip install -r requirements.txt
```

Inirerekomenda naming patakbuhin ito sa loob ng virtual environment na ginawa mo kanina.

## Opsyonal na Setup: Azure AI Search (Mga Aralin 5 at 16)

Ang Lesson 5 (Agentic RAG) at Lesson 16 notebooks ay tumatakbo agad gamit ang isang **in-memory knowledge base** — walang kailangang dagdag na Azure resources. Kung gusto mong gawing backed ito ng totoong **Azure AI Search** index, tandaan na ang **Lesson 16 notebook ay kasalukuyang gumagamit ng key-based authentication**: lumilipat ito mula sa in-memory search patungo sa Azure AI Search lamang kapag parehong naka-set ang `AZURE_SEARCH_SERVICE_ENDPOINT` **at** `AZURE_SEARCH_API_KEY`, at kung hindi ay nananatili sa in-memory search — kaya para patakbuhin ito laban sa totoong index, kailangan mo ring i-set ang admin key. Ang keyless authentication gamit ang Microsoft Entra ID (RBAC) ang inirerekomendang paraan para sa iyong sariling production code, tugma sa `az login` flow na ginamit sa buong kurso.

Ang mga hakbang sa RBAC sa ibaba ay naaangkop sa setup-guide samples at sa iyong sariling code. Hindi nito pinapagana ang keyless authentication sa Lesson 16 notebook; patuloy na kailangan ng Lesson 16 ng parehong endpoint at admin key para magamit ang Azure AI Search.

1. **Paganahin ang role-based access** sa iyong search service:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Bigyan ang iyong sarili ng mga kinakailangang roles** (gumawa/mag-load ng mga indexes at mag-query):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Ilagay ang endpoint** sa iyong `.env` file:

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → iyong **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Kinakailangan (kasama ng endpoint) para paganahin ang Azure AI Search sa Lesson 16 notebook, na gumagamit ng key-based auth. Azure portal → **Settings** → **Keys** → pangunahing admin key |

> **Bakit keyless?** Ang mga admin key ay nagbibigay ng buong write access sa iyong search service at maaaring mabunyag sa pamamagitan ng `.env` files. Sa RBAC, ginagamit ang iyong `az login` identity bilang kapalit — parehas na keyless Entra ID pattern na ginagamit ng mga notebooks sa kurso (sa pamamagitan ng `AzureCliCredential` / `DefaultAzureCredential`). Tingnan ang [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

Tingnan ang [Azure AI Search setup guide](./AzureSearch.md) para sa buong mga halimbawa ng paggawa ng index sa Python at .NET.

## Karagdagang Setup para sa Mga Aralin na Tumatawag ng Azure OpenAI Diretso (Mga Aralin 6 at 8)

Ang ilang notebooks sa mga aralin 6 at 8 ay tumatawag ng **Azure OpenAI** diretso (gamit ang **Responses API**) sa halip na dumaan sa Microsoft Foundry project. Ang mga sample na ito ay dating gumagamit ng GitHub Models, na deprecated na at hindi sumusuporta sa Responses API. Idagdag ang mga sumusunod na variable sa iyong `.env` file:

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → iyong **Azure OpenAI** resource → **Keys and Endpoint** → Endpoint (hal., `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Pangalan ng iyong deployed na modelo (hal., `gpt-5-mini`) na sumusuporta sa Responses API |
| `AZURE_OPENAI_API_KEY` | Opsyonal — kung gagamit ka ng key-based auth sa halip na `az login` / Entra ID |

> Ginagamit ng Responses API ang stable na `/openai/v1/` endpoint, kaya hindi kailangan ang `api-version`. Mag-sign in gamit ang `az login` para gumamit ng keyless Entra ID authentication.

## Alternatibong Provider: MiniMax (OpenAI-Compatible)

Nagbibigay ang [MiniMax](https://platform.minimaxi.com/) ng large-context models (hanggang 204K tokens) sa pamamagitan ng OpenAI-compatible API. Dahil ang `OpenAIChatClient` ng Microsoft Agent Framework ay gumagana sa anumang OpenAI-compatible endpoint, maaari mong gamitin ang MiniMax bilang drop-in na alternatibo para sa mga lessons na gumagamit ng `OpenAIChatClient`.

Idagdag ang mga variable na ito sa iyong `.env` file:

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Gamitin ang `https://api.minimax.io/v1` (default na halaga) |
| `MINIMAX_MODEL_ID` | Pangalan ng modelong gagamitin (hal., `MiniMax-M3`) |

**Mga halimbawa ng modelo**: `MiniMax-M3` (inirerekomenda), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (mas mabilis na mga tugon). Maaaring magbago ang mga pangalan ng modelo at availability sa paglipas ng panahon, at ang access sa isang partikular na modelo ay maaaring naka-depende sa iyong account.

Awtomatikong madedetect at gagamitin ng mga halimbawa ng code na gumagamit ng `OpenAIChatClient` (hal., Lesson 14 hotel booking workflow) ang iyong MiniMax configuration kapag naka-set ang `MINIMAX_API_KEY`.


## Alternatibong Tagapagbigay: Novita AI (Katugma sa OpenAI)

[Novita AI](https://novita.ai/llm-api) ay naglalaan ng API na katugma sa OpenAI para sa open-source at frontier LLMs (DeepSeek, Llama, Qwen, at iba pa). Dahil ang `OpenAIChatClient` ng Microsoft Agent Framework ay gumagana sa anumang OpenAI-compatible na endpoint, maaari mong gamitin ang Novita AI bilang drop-in na alternatibo sa Azure OpenAI o OpenAI.

Idagdag ang mga variable na ito sa iyong `.env` na file:

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | Gamitin ang `https://api.novita.ai/openai/v1` (default na halaga) |
| `NOVITA_MODEL_ID` | Pangalan ng modelong gagamitin (hal., `moonshotai/kimi-k3`) |

**Halimbawa ng mga modelo**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Nagho-host din ang Novita AI ng maraming iba pang open-source na pamilya ng mga modelo (Llama, Qwen, GLM, at iba pa) — tingnan ang [Novita AI model library](https://novita.ai/llm-api) para sa kasalukuyang listahan ng mga available na modelo at kanilang model IDs.

Ang mga kasalukuyang halimbawa ay hindi awtomatikong kumukuha ng `NOVITA_*` na mga variable. Upang magamit ang Novita AI, ipasa nang hayag ang mga halagang ito kapag binubuo ang `OpenAIChatClient` sa sample na iyong pinapatakbo.

## Alternatibong Tagapagbigay: Foundry Local (Patakbuhin ang mga Modelo sa Device)

[Foundry Local](https://foundrylocal.ai) ay isang magaan na runtime na nagda-download, nagma-manage, at nagsisilbi ng mga modelong pangwika **sa sarili mong makina nang buo** sa pamamagitan ng OpenAI-compatible na API — hindi kailangan ng cloud.

Dahil ang `OpenAIChatClient` ng Microsoft Agent Framework ay gumagana sa anumang OpenAI-compatible na endpoint, ang Foundry Local ay isang drop-in lokal na alternatibo sa Azure OpenAI.

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

**3. I-install ang Python SDK** na ginagamit upang matuklasan ang lokal na endpoint:

```bash
pip install foundry-local-sdk
```

**4. Ituro ang Microsoft Agent Framework sa iyong lokal na modelo:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Ina-download (kung kinakailangan) at pinaglilingkuran ang modelo nang lokal, pagkatapos ay hinahanap ang endpoint/port.
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

> **Note:** Naglalabas ang Foundry Local ng OpenAI-compatible na **Chat Completions** endpoint. Gamitin ito para sa lokal na pag-develop at offline na mga scenario. Para sa buong tampok ng **Responses API** (stateful na mga pag-uusap, atbp.), gamitin ang Azure OpenAI o isang proyekto ng Microsoft Foundry.

## Karagdagang Setup para sa Lesson 8 (Bing Grounding Workflow)

Ginagamit ng conditional workflow notebook sa lesson 8 ang **Bing grounding** sa pamamagitan ng Microsoft Foundry. Kung balak mong patakbuhin ang sample na iyon, idagdag ang variable na ito sa iyong `.env` na file:

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → iyong proyekto → **Management** → **Connected resources** → iyong Bing connection → kopyahin ang connection ID |

## Pag-troubleshoot

### Mga Error sa SSL Certificate Verification sa macOS

Kung ikaw ay nasa macOS at nakaranas ng error na gaya ng:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Kilala ito na isyu sa Python sa macOS kung saan ang system SSL certificates ay hindi awtomatikong pinagtitiwalaan. Subukan ang mga sumusunod na solusyon nang sunod-sunod:

**Opsyon 1: Patakbuhin ang Install Certificates script ng Python (inirerekomenda)**

```bash
# Palitan ang 3.XX ng naka-install mong bersyon ng Python (hal., 3.12 o 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opsyon 2: Gamitin ang `connection_verify=False` sa iyong notebook (para lamang sa GitHub Models notebooks)**

Sa Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), may kasama nang commented-out na workaround. I-uncomment ang `connection_verify=False` kapag nakatagpo ng mga certificate errors:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # I-disable ang SSL verification kung makaranas ka ng mga error sa sertipiko
)
```

> **⚠️ Babala:** Ang pag-disable ng SSL verification (`connection_verify=False`) ay nagpapababa ng seguridad sa pamamagitan ng pag-skip ng certificate validation. Gamitin lamang ito bilang pansamantalang workaround sa mga development environment. Huwag gamitin sa production.

**Opsyon 3: I-install at gamitin ang `truststore`**

```bash
pip install truststore
```

Pagkatapos idagdag ang mga sumusunod sa itaas ng iyong notebook o script bago gumawa ng anumang network calls:

```python
import truststore
truststore.inject_into_ssl()
```

## Naharang Sa Isang Lugar?

Kung mayroon kang anumang problema sa pagpapatakbo ng setup na ito, sumali sa aming <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> o <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">gumawa ng issue</a>.

## Susunod na Leksyon

Handang-handa ka na ngayong patakbuhin ang code para sa kursong ito. Maligayang pag-aaral pa tungkol sa mundo ng mga AI Agents!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->