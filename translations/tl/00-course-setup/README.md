# Pagsasaayos ng Kurso

## Panimula

Tatalakayin ng araling ito kung paano patakbuhin ang mga halimbawa ng code ng kursong ito.

## Sumali sa Iba pang mga Nag-aaral at Humingi ng Tulong

Bago ka magsimulang i-clone ang iyong repo, sumali sa <a href="https://aka.ms/ai-agents/discord" target="_blank">Discord channel ng AI Agents For Beginners</a> upang makakuha ng tulong sa setup, magtanong tungkol sa kurso, o makipag-ugnayan sa ibang mga nag-aaral.

## I-clone o I-fork ang Repo na ito

Upang magsimula, i-clone o i-fork muna ang GitHub Repository. Gagawa ito ng sarili mong bersyon ng materyal ng kurso upang maaari mong patakbuhin, subukan, at baguhin ang code!

This can be done by clicking the link to <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">i-fork ang repo</a>

Dapat mayroon ka na ngayong sarili mong na-fork na bersyon ng kursong ito sa sumusunod na link:

![Na-fork na Repo](../../../translated_images/tl/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (inirerekomenda para sa workshop / Codespaces)

  >Ang buong repository ay maaaring maging malaki (~3 GB) kapag dina-download mo ang buong kasaysayan at lahat ng file. Kung pupunta ka lamang sa workshop o kailangan mo lang ng ilang lesson folder, ang shallow clone (o sparse clone) ay makakaiwas sa karamihan ng pag-download na iyon sa pamamagitan ng pagpapaikli ng kasaysayan at/o pag-skip sa mga blobs.

#### Mabilis na shallow clone — minimal na historya, lahat ng mga file

Palitan ang `<your-username>` sa mga utos sa ibaba ng iyong fork URL (o ang upstream URL kung mas gusto mo).

To clone only the latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal blobs + only selected folders

This uses partial clone and sparse-checkout (requires Git 2.25+ and recommended modern Git with partial clone support):

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

#### Using GitHub Codespaces (recommended to avoid local large downloads)

- Gumawa ng bagong Codespace para sa repo na ito gamit ang [UI ng GitHub](https://github.com/codespaces).  

- Sa terminal ng bagong likhang codespace, patakbuhin ang isa sa mga shallow/sparse clone na utos sa itaas para dalhin lang ang mga lesson folder na kailangan mo papunta sa workspace ng Codespace.
- Opsyonal: pagkatapos mag-clone sa loob ng Codespaces, tanggalin ang .git upang makabalik ng ekstrang espasyo (tingnan ang mga utos ng pagtanggal sa itaas).
- Tandaan: Kung mas gusto mong buksan ang repo nang direkta sa Codespaces (nang walang dagdag na clone), tandaan na bubuuin ng Codespaces ang devcontainer environment at maaaring mag-provision pa rin ng higit kaysa sa kailangan mo. Ang pag-clone ng shallow copy sa loob ng bagong Codespace ay nagbibigay sa iyo ng mas kontrol sa paggamit ng disk.

#### Mga Tip

- Palaging palitan ang clone URL ng iyong fork kung gusto mong mag-edit/commit.
- Kung kailangan mo ng mas maraming history o file mamaya, maaari mo silang i-fetch o ayusin ang sparse-checkout upang isama ang karagdagang mga folder.

## Pagpapatakbo ng Code

Nag-aalok ang kursong ito ng serye ng mga Jupyter Notebooks na maaari mong patakbuhin upang magkaroon ng hands-on na karanasan sa pagbubuo ng AI Agents.

Gumagamit ang mga halimbawa ng code ng **Microsoft Agent Framework (MAF)** kasama ang `AzureAIProjectAgentProvider`, na kumokonekta sa **Azure AI Agent Service V2** (ang Responses API) sa pamamagitan ng **Microsoft Foundry**.

Lahat ng mga Python notebook ay may label na `*-python-agent-framework.ipynb`.

## Mga Kinakailangan

- Python 3.12+
  - **TANDAAN**: Kung wala ka pang Python3.12 na naka-install, tiyaking i-install ito. Pagkatapos nito, gumawa ng iyong venv gamit ang python3.12 upang matiyak na ang tamang mga bersyon ay mai-install mula sa requirements.txt file.
  
    >Halimbawa

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

- .NET 10+: Para sa mga sample code na gumagamit ng .NET, tiyaking i-install ang [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o mas bago. Pagkatapos, i-check ang naka-install mong .NET SDK na bersyon:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Kinakailangan para sa authentication. I-install mula sa [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Para sa access sa Microsoft Foundry at Azure AI Agent Service.
- **Microsoft Foundry Project** — Isang proyekto na may naka-deploy na modelo (hal., `gpt-4o`). Tingnan ang [Hakbang 1](../../../00-course-setup) sa ibaba.

Naka-include ang isang `requirements.txt` file sa root ng repository na ito na naglalaman ng lahat ng kinakailangang Python package upang patakbuhin ang mga halimbawa ng code.

Maaari mong i-install ang mga ito sa pamamagitan ng pagpapatakbo ng sumusunod na utos sa iyong terminal sa root ng repository:

```bash|powershell
pip install -r requirements.txt
```

Inirerekomenda naming gumawa ng Python virtual environment upang maiwasan ang anumang conflict at isyu.

## I-setup ang VSCode

Siguraduhin na ginagamit mo ang tamang bersyon ng Python sa VSCode.

![larawan](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## I-set up ang Microsoft Foundry at Azure AI Agent Service

### Hakbang 1: Gumawa ng Microsoft Foundry Project

Kailangan mo ng Azure AI Foundry **hub** at **project** na may naka-deploy na modelo upang patakbuhin ang mga notebook.

1. Pumunta sa [ai.azure.com](https://ai.azure.com) at mag-sign in gamit ang iyong Azure account.
2. Gumawa ng **hub** (o gumamit ng umiiral na). Tingnan: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Sa loob ng hub, gumawa ng **project**.
4. I-deploy ang isang modelo (hal., `gpt-4o`) mula sa **Models + Endpoints** → **Deploy model**.

### Hakbang 2: Kunin ang Endpoint ng Iyong Project at Pangalan ng Model Deployment

Mula sa iyong proyekto sa Microsoft Foundry portal:

- **Project Endpoint** — Pumunta sa **Overview** page at kopyahin ang endpoint URL.

![String ng Koneksyon ng Proyekto](../../../translated_images/tl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Pumunta sa **Models + Endpoints**, piliin ang iyong na-deploy na modelo, at tandaan ang **Deployment name** (hal., `gpt-4o`).

### Hakbang 3: Mag-sign in sa Azure gamit ang `az login`

Lahat ng notebook ay gumagamit ng **`AzureCliCredential`** para sa authentication — walang API keys na kailangan i-manage. Nangangailangan ito na naka-sign in ka sa pamamagitan ng Azure CLI.

1. **I-install ang Azure CLI** kung hindi mo pa ito nai-install: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Mag-sign in** sa pamamagitan ng pagpapatakbo:

    ```bash|powershell
    az login
    ```

    Or if you're in a remote/Codespace environment without a browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Piliin ang iyong subscription** kung pinaprompt — piliin ang subscription na naglalaman ng iyong Foundry project.

4. **Beripikahin** na naka-sign in ka:

    ```bash|powershell
    az account show
    ```

> **Bakit `az login`?** Nag-a-authenticate ang mga notebook gamit ang `AzureCliCredential` mula sa `azure-identity` package. Nangangahulugan ito na ang iyong Azure CLI session ang nagbibigay ng mga kredensyal — walang API keys o secrets sa iyong `.env` file. Ito ay isang [security best practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Hakbang 4: Gumawa ng Iyong `.env` File

Kopyahin ang example file:

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → iyong proyekto → **Overview** page |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → ang pangalan ng iyong na-deploy na modelo |

Tapos na! Para sa karamihan ng mga aralin, mag-a-authenticate nang awtomatiko ang mga notebook sa pamamagitan ng iyong `az login` session.

### Hakbang 5: I-install ang mga Depedensiya ng Python

```bash|powershell
pip install -r requirements.txt
```

Inirerekomenda naming patakbuhin ito sa loob ng virtual environment na ginawa mo kanina.

## Karagdagang Setup para sa Lesson 5 (Agentic RAG)

Gumagamit ang Lesson 5 ng **Azure AI Search** para sa retrieval-augmented generation. Kung balak mong patakbuhin ang araling iyon, idagdag ang mga variable na ito sa iyong `.env` file:

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → iyong **Azure AI Search** resource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → iyong **Azure AI Search** resource → **Settings** → **Keys** → primary admin key |

## Karagdagang Setup para sa Lesson 6 at Lesson 8 (GitHub Models)

Ang ilang notebook sa mga lesson 6 at 8 ay gumagamit ng **GitHub Models** sa halip na Azure AI Foundry. Kung plano mong patakbuhin ang mga sample na iyon, idagdag ang mga variable na ito sa iyong `.env` file:

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default na halaga) |
| `GITHUB_MODEL_ID` | Pangalan ng modelong gagamitin (hal., `gpt-4o-mini`) |

## Karagdagang Setup para sa Lesson 8 (Bing Grounding Workflow)

Ang conditional workflow notebook sa lesson 8 ay gumagamit ng **Bing grounding** via Azure AI Foundry. Kung balak mong patakbuhin ang sample na iyon, idagdag ang variable na ito sa iyong `.env` file:

| Variable | Saan ito mahahanap |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portal → iyong proyekto → **Management** → **Connected resources** → ang iyong Bing connection → kopyahin ang connection ID |

## Pag-aayos ng Problema

### Mga Error sa Pag-verify ng SSL Certificate sa macOS

Kung nasa macOS ka at naka-encounter ng error na tulad nito:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ito ay isang kilalang isyu sa Python sa macOS kung saan hindi awtomatikong tinatanggap ang mga system SSL certificate. Subukan ang mga sumusunod na solusyon ayon sa pagkakasunod:

**Opsyon 1: Patakbuhin ang Install Certificates script ng Python (inirerekomenda)**

```bash
# Palitan ang 3.XX ng naka-install mong bersyon ng Python (hal., 3.12 o 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Opsyon 2: Gamitin ang `connection_verify=False` sa iyong notebook (para lamang sa mga GitHub Models notebooks)**

Sa Lesson 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), mayroon nang naka-komentong workaround. I-uncomment ang `connection_verify=False` kapag lumilikha ng client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # I-disable ang pag-verify ng SSL kung makaranas ka ng mga error sa sertipiko
)
```

> **⚠️ Babala:** Ang pag-disable ng SSL verification (`connection_verify=False`) ay nagpapababa ng seguridad sa pamamagitan ng pag-skip ng certificate validation. Gamitin ito lamang bilang pansamantalang workaround sa mga development environment, hindi sa production.

**Opsyon 3: I-install at gamitin ang `truststore`**

```bash
pip install truststore
```

Pagkatapos idagdag ang sumusunod sa itaas ng iyong notebook o script bago gumawa ng anumang network calls:

```python
import truststore
truststore.inject_into_ssl()
```

## Natigil Ka Ba?

Kung may anumang isyu sa pagpapatakbo ng setup na ito, sumali sa aming <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> o <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">gumawa ng isyu</a>.

## Susunod na Aralin

Handa ka nang patakbuhin ang code para sa kursong ito. Maligayang pag-aaral pa tungkol sa mundo ng AI Agents! 

[Panimula sa AI Agents at Mga Use Case](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Paunawa:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa pagiging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa katutubong wika nito ang dapat ituring na awtoritatibong sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin na ginawa ng tao. Hindi kami mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->