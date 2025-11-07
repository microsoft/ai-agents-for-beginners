<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86273689a010b5efecaf7fa23104e0fb",
  "translation_date": "2025-11-07T08:44:12+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "tl"
}
-->
# Pagsasaayos ng Kurso

## Panimula

Ang araling ito ay magtuturo kung paano patakbuhin ang mga halimbawa ng code sa kursong ito.

## Sumali sa Iba Pang Mga Mag-aaral at Humingi ng Tulong

Bago mo simulan ang pag-clone ng iyong repo, sumali sa [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) upang makakuha ng tulong sa pagsasaayos, anumang tanong tungkol sa kurso, o upang makipag-ugnayan sa iba pang mga mag-aaral.

## I-clone o I-fork ang Repo na Ito

Upang magsimula, mangyaring i-clone o i-fork ang GitHub Repository. Magkakaroon ka ng sariling bersyon ng materyal ng kurso upang maipatupad, masubukan, at mabago ang code!

Magagawa ito sa pamamagitan ng pag-click sa link upang <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">i-fork ang repo</a>

Dapat ay mayroon ka na ngayong sariling forked na bersyon ng kursong ito sa sumusunod na link:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.tl.png)

### Shallow Clone (inirerekomenda para sa workshop / Codespaces)

  >Ang buong repository ay maaaring malaki (~3 GB) kapag na-download ang buong kasaysayan at lahat ng mga file. Kung ikaw ay dadalo lamang sa workshop o kailangan lamang ng ilang mga folder ng aralin, ang shallow clone (o sparse clone) ay maiiwasan ang karamihan sa pag-download na iyon sa pamamagitan ng pag-truncate ng kasaysayan at/o pag-skip sa mga blobs.

#### Mabilis na shallow clone — minimal na kasaysayan, lahat ng mga file

Palitan ang `<your-username>` sa mga utos sa ibaba gamit ang iyong fork URL (o ang upstream URL kung mas gusto mo).

Upang i-clone lamang ang pinakabagong kasaysayan ng commit (maliit na pag-download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Upang i-clone ang isang partikular na branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimal na blobs + piling mga folder lamang

Ginagamit nito ang partial clone at sparse-checkout (nangangailangan ng Git 2.25+ at inirerekomendang modernong Git na may suporta sa partial clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Pumasok sa folder ng repo:

```bash|powershell
cd ai-agents-for-beginners
```

Pagkatapos tukuyin kung aling mga folder ang gusto mo (halimbawa sa ibaba ay nagpapakita ng dalawang folder):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Pagkatapos ng pag-clone at pag-verify ng mga file, kung kailangan mo lamang ng mga file at nais na magbakante ng espasyo (walang kasaysayan ng git), mangyaring tanggalin ang metadata ng repository (💀irreversible — mawawala ang lahat ng functionality ng Git: walang commits, pulls, pushes, o access sa kasaysayan).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Paggamit ng GitHub Codespaces (inirerekomenda upang maiwasan ang malalaking pag-download sa lokal)

- Gumawa ng bagong Codespace para sa repo na ito sa pamamagitan ng [GitHub UI](https://github.com/codespaces).  

- Sa terminal ng bagong nilikhang codespace, patakbuhin ang isa sa mga shallow/sparse clone na utos sa itaas upang dalhin lamang ang mga folder ng aralin na kailangan mo sa workspace ng Codespace.
- Opsyonal: pagkatapos ng pag-clone sa loob ng Codespaces, tanggalin ang .git upang mabawi ang dagdag na espasyo (tingnan ang mga utos ng pagtanggal sa itaas).
- Tandaan: Kung mas gusto mong buksan ang repo nang direkta sa Codespaces (nang walang dagdag na clone), tandaan na ang Codespaces ay magtatayo ng devcontainer environment at maaaring mag-provision pa rin ng higit sa kailangan mo. Ang pag-clone ng shallow copy sa loob ng sariwang Codespace ay nagbibigay sa iyo ng higit na kontrol sa paggamit ng disk.

#### Mga Tip

- Palaging palitan ang clone URL gamit ang iyong fork kung nais mong mag-edit/commit.
- Kung sa kalaunan ay kailangan mo ng higit pang kasaysayan o mga file, maaari mo itong i-fetch o ayusin ang sparse-checkout upang isama ang karagdagang mga folder.

## Pagpapatakbo ng Code

Ang kursong ito ay nag-aalok ng serye ng Jupyter Notebooks na maaari mong patakbuhin upang makakuha ng hands-on na karanasan sa paggawa ng AI Agents.

Ang mga halimbawa ng code ay gumagamit ng alinman sa:

**Kailangan ng GitHub Account - Libre**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Nakalabel bilang (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Nakalabel bilang (autogen.ipynb)

**Kailangan ng Azure Subscription**:
3) Azure AI Foundry + Azure AI Agent Service. Nakalabel bilang (azureaiagent.ipynb)

Hinihikayat namin kayong subukan ang lahat ng tatlong uri ng mga halimbawa upang makita kung alin ang pinakamahusay para sa inyo.

Anuman ang opsyon na pipiliin mo, ito ang magtatakda kung aling mga hakbang sa pagsasaayos ang kailangan mong sundin sa ibaba:

## Mga Kinakailangan

- Python 3.12+
  - **NOTE**: Kung wala kang Python3.12 na naka-install, tiyaking i-install ito. Pagkatapos ay gumawa ng iyong venv gamit ang python3.12 upang matiyak na ang tamang mga bersyon ay mai-install mula sa requirements.txt file.
  
    >Halimbawa

    Gumawa ng Python venv directory:

    ```bash|powershell
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

- .NET 10+: Para sa mga sample code na gumagamit ng .NET, tiyaking i-install ang [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o mas bago. Pagkatapos, suriin ang iyong naka-install na bersyon ng .NET SDK:

    ```bash|powershell
    dotnet --list-sdks
    ```

- Isang GitHub Account - Para sa Access sa GitHub Models Marketplace
- Azure Subscription - Para sa Access sa Azure AI Foundry
- Azure AI Foundry Account - Para sa Access sa Azure AI Agent Service

Kasama sa repository na ito ang isang `requirements.txt` file sa root na naglalaman ng lahat ng kinakailangang Python packages upang patakbuhin ang mga halimbawa ng code.

Maaari mong i-install ang mga ito sa pamamagitan ng pagpapatakbo ng sumusunod na utos sa iyong terminal sa root ng repository:

```bash|powershell
pip install -r requirements.txt
```

Inirerekomenda namin ang paggawa ng Python virtual environment upang maiwasan ang anumang mga conflict at isyu.

## Pagsasaayos ng VSCode

Tiyaking ginagamit mo ang tamang bersyon ng Python sa VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Pagsasaayos para sa Mga Halimbawa gamit ang GitHub Models 

### Hakbang 1: Kunin ang Iyong GitHub Personal Access Token (PAT)

Ang kursong ito ay gumagamit ng GitHub Models Marketplace, na nagbibigay ng libreng access sa Large Language Models (LLMs) na gagamitin mo upang bumuo ng AI Agents.

Upang magamit ang GitHub Models, kailangan mong gumawa ng [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Magagawa ito sa pamamagitan ng pagpunta sa iyong <a href="https://github.com/settings/personal-access-tokens" target="_blank">Personal Access Tokens settings</a> sa iyong GitHub Account.

Mangyaring sundin ang [Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) kapag gumagawa ng iyong token. Nangangahulugan ito na dapat mo lamang ibigay sa token ang mga pahintulot na kailangan nito upang patakbuhin ang mga halimbawa ng code sa kursong ito.

1. Piliin ang opsyon na `Fine-grained tokens` sa kaliwang bahagi ng iyong screen sa pamamagitan ng pagpunta sa **Developer settings**

   ![Developer settings](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.tl.png)

   Pagkatapos piliin ang `Generate new token`.

   ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.tl.png)

2. Maglagay ng deskriptibong pangalan para sa iyong token na sumasalamin sa layunin nito, upang madali itong makilala sa hinaharap.

    🔐 Rekomendasyon sa Tagal ng Token

    Inirerekomendang tagal: 30 araw
    Para sa mas ligtas na postura, maaari kang pumili ng mas maikling panahon—tulad ng 7 araw 🛡️
    Ito ay isang mahusay na paraan upang magtakda ng personal na target at tapusin ang kurso habang mataas ang iyong momentum sa pag-aaral 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.tl.png)

3. Limitahan ang saklaw ng token sa iyong fork ng repository na ito.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.tl.png)

4. Limitahan ang mga pahintulot ng token: Sa ilalim ng **Permissions**, i-click ang **Account** tab, at i-click ang "+ Add permissions" button. Lalabas ang isang dropdown. Mangyaring hanapin ang **Models** at i-check ang kahon para dito.

    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.tl.png)

5. I-verify ang mga kinakailangang pahintulot bago gumawa ng token. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.tl.png)

6. Bago gumawa ng token, tiyaking handa kang itago ang token sa isang ligtas na lugar tulad ng password manager vault, dahil hindi na ito ipapakita muli pagkatapos mong gawin ito. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.tl.png)

Kopyahin ang iyong bagong token na kakagawa mo lang. Idadagdag mo ito ngayon sa iyong `.env` file na kasama sa kursong ito.

### Hakbang 2: Gumawa ng Iyong `.env` File

Upang gumawa ng iyong `.env` file, patakbuhin ang sumusunod na utos sa iyong terminal.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Ito ay kokopya sa example file at gagawa ng `.env` sa iyong direktoryo kung saan mo pupunan ang mga halaga para sa mga environment variables.

Sa pagkopya ng iyong token, buksan ang `.env` file sa iyong paboritong text editor at i-paste ang iyong token sa `GITHUB_TOKEN` field.

![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.tl.png)

Dapat ay kaya mo nang patakbuhin ang mga halimbawa ng code sa kursong ito.

## Pagsasaayos para sa Mga Halimbawa gamit ang Azure AI Foundry at Azure AI Agent Service

### Hakbang 1: Kunin ang Iyong Azure Project Endpoint

Sundin ang mga hakbang sa paggawa ng hub at proyekto sa Azure AI Foundry na matatagpuan dito: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)

Kapag nagawa mo na ang iyong proyekto, kakailanganin mong kunin ang connection string para sa iyong proyekto.

Magagawa ito sa pamamagitan ng pagpunta sa **Overview** page ng iyong proyekto sa Azure AI Foundry portal.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.tl.png)

### Hakbang 2: Gumawa ng Iyong `.env` File

Upang gumawa ng iyong `.env` file, patakbuhin ang sumusunod na utos sa iyong terminal.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Ito ay kokopya sa example file at gagawa ng `.env` sa iyong direktoryo kung saan mo pupunan ang mga halaga para sa mga environment variables.

Sa pagkopya ng iyong token, buksan ang `.env` file sa iyong paboritong text editor at i-paste ang iyong token sa `PROJECT_ENDPOINT` field.

### Hakbang 3: Mag-sign in sa Azure

Bilang isang security best practice, gagamit tayo ng [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) upang mag-authenticate sa Azure OpenAI gamit ang Microsoft Entra ID. 

Susunod, buksan ang terminal at patakbuhin ang `az login --use-device-code` upang mag-sign in sa iyong Azure account.

Kapag naka-login ka na, piliin ang iyong subscription sa terminal.

## Karagdagang Environment Variables - Azure Search at Azure OpenAI 

Para sa Agentic RAG Lesson - Lesson 5 - may mga halimbawa na gumagamit ng Azure Search at Azure OpenAI.

Kung nais mong patakbuhin ang mga halimbawa na ito, kakailanganin mong idagdag ang sumusunod na mga environment variables sa iyong `.env` file:

### Overview Page (Project)

- `AZURE_SUBSCRIPTION_ID` - Tingnan ang **Project details** sa **Overview** page ng iyong proyekto.

- `AZURE_AI_PROJECT_NAME` - Tingnan ang itaas ng **Overview** page para sa iyong proyekto.

- `AZURE_OPENAI_SERVICE` - Hanapin ito sa **Included capabilities** tab para sa **Azure OpenAI Service** sa **Overview** page.

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - Pumunta sa **Project properties** sa **Overview** page ng **Management Center**.

- `GLOBAL_LLM_SERVICE` - Sa ilalim ng **Connected resources**, hanapin ang **Azure AI Services** connection name. Kung hindi nakalista, tingnan ang **Azure portal** sa ilalim ng iyong resource group para sa AI Services resource name.

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Piliin ang iyong embedding model (hal., `text-embedding-ada-002`) at tandaan ang **Deployment name** mula sa model details.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Piliin ang iyong chat model (hal., `gpt-4o-mini`) at tandaan ang **Deployment name** mula sa model details.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Hanapin ang **Azure AI services**, i-click ito, pagkatapos pumunta sa **Resource Management**, **Keys and Endpoint**, mag-scroll pababa sa "Azure OpenAI endpoints", at kopyahin ang isa na nagsasabing "Language APIs".

- `AZURE_OPENAI_API_KEY` - Mula sa parehong screen, kopyahin ang KEY 1 o KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Hanapin ang iyong **Azure AI Search** resource, i-click ito, at tingnan ang **Overview**.

- `AZURE_SEARCH_API_KEY` - Pagkatapos pumunta sa **Settings** at pagkatapos **Keys** upang kopyahin ang primary o secondary admin key.

### External Webpage

- `AZURE_OPENAI_API_VERSION` - Bisitahin ang [API version lifecycle](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) page sa ilalim ng **Latest GA API release**.

### Pagsasaayos ng keyless authentication

Sa halip na i-hardcode ang iyong mga kredensyal, gagamit tayo ng keyless connection sa Azure OpenAI. Upang gawin ito, mag-i-import tayo ng `DefaultAzureCredential` at tatawagin ang `DefaultAzureCredential` function upang makuha ang kredensyal.

```python
# Python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Nahihirapan?
Kung mayroon kang anumang problema sa pagpapatakbo ng setup na ito, sumali sa aming <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> o <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">gumawa ng isyu</a>.

## Susunod na Aralin

Handa ka nang patakbuhin ang code para sa kursong ito. Masaya naming pag-aaralan pa ang mundo ng AI Agents!

[Pagpapakilala sa AI Agents at Mga Gamit ng Agent](../01-intro-to-ai-agents/README.md)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.