# AGENTS.md

## Pangkalahatang Pagsusuri ng Proyekto

Ang repositoryong ito ay naglalaman ng "AI Agents para sa mga Baguhan" - isang komprehensibong edukasyonal na kurso na nagtuturo ng lahat ng kailangan para makabuo ng AI Agents. Binubuo ang kurso ng 18 na leksyon (may bilang 00-18) na sumasaklaw sa mga pundasyon, disenyo ng mga pattern, mga framework, pag-deploy sa produksyon, mga lokal/on-device na ahente, at seguridad ng mga AI agents.

**Pangunahing Teknolohiya:**
- Python 3.12+
- Jupyter Notebooks para sa interaktibong pag-aaral
- Mga Framework ng AI: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkitektura:**
- Istruktura batay sa leksyon (mga direktoryo 00-18)
- Bawat leksyon ay may kasamang: README na dokumentasyon, mga halimbawa ng code (Jupyter notebooks), at mga larawan
- Suporta sa maramihang wika sa pamamagitan ng automated na sistema ng pagsasalin
- Isang Python notebook bawat leksyon gamit ang Microsoft Agent Framework

## Mga Utos para sa Setup

### Mga Kinakailangan
- Python 3.12 o mas mataas pa
- Azure subscription (para sa Microsoft Foundry)
- Nakainstall at na-authenticate ang Azure CLI (`az login`)

### Paunang Setup

1. **I-clone o i-fork ang repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Gumawa at i-activate ang Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **I-install ang mga dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **I-set up ang mga environment variable:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Mga Kinakailangang Environment Variable

Para sa **Microsoft Foundry** (Kinakailangan):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Pangalan ng deployment ng modelo (hal. gpt-5-mini)

Para sa **Azure AI Search** (Leksiyon 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Patakbuhin ang `az login` bago patakbuhin ang mga notebook (gamit ang `AzureCliCredential`).

## Workflow sa Pagbuo

### Pagtakbo ng Jupyter Notebooks

Bawat leksyon ay may maramihang Jupyter notebooks para sa iba't ibang framework:

1. **Simulan ang Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pumunta sa isang direktoryo ng leksyon** (hal. `01-intro-to-ai-agents/code_samples/`)

3. **Buksan at patakbuhin ang mga notebook:**
   - `*-python-agent-framework.ipynb` - Gamit ang Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Gamit ang Microsoft Agent Framework (.NET)

### Paggamit ng Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Nangangailangan ng Azure subscription
- Ginagamit ang `FoundryChatClient` para sa Agent Service V2 (mga agent na makikita sa Foundry portal)
- Handa na para sa produksyon na may naka-built-in na observability
- Pattern ng file: `*-python-agent-framework.ipynb`

## Mga Tagubilin sa Pagsusuri

Ito ay isang edukasyonal na repository na may mga halimbawa ng code sa halip na production code na may automated tests. Para beripikahin ang iyong setup at mga pagbabago:

### Manwal na Pagsusuri

1. **Subukan ang Python environment:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Subukan ang pagpapatakbo ng notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Beripikahin ang mga environment variable:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Pagtakbo ng Indibidwal na Notebook

Buksan ang mga notebook sa Jupyter at patakbuhin nang sunud-sunod ang mga cells. Bawat notebook ay kumpleto sa sarili nito at may kasamang:
- Import statements
- Pag-load ng configuration
- Mga halimbawa ng implementasyon ng agent
- Inaasahang output sa mga markdown cells

### Smoke-Testing para sa mga Na-deploy na Agent

Para sa mga leksyon kung saan ang isang agent ay na-deploy bilang Microsoft Foundry hosted agent (01, 04, 05, 16), naglalagay ang repo ng mga smoke-test catalog sa loob ng `tests/` na pinapatakbo ng `.github/workflows/smoke-test.yml` workflow sa pamamagitan ng [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) action. Ito ay isang magaan na post-deploy gate (maaabot ba ang agent at sumusunod sa mga pangunahing inaasahan sa prompt?), na kumukumplemento sa evaluation pipeline sa Leksiyon 10 at 16. Tingnan ang [tests/README.md](./tests/README.md) para sa mapping ng catalog-to-lesson-to-agent. Ang Leksiyon 17 ay tumatakbo nang lokal gamit ang Foundry Local at walang hosted endpoint, kaya't sinusuri ito sa pamamagitan ng direktang pagpapatakbo ng notebook.

## Estilo ng Code

### Mga Konbensyon sa Python

- **Bersyon ng Python**: 3.12+
- **Estilo ng Code**: Sundin ang karaniwang Python PEP 8 na mga konbensyon
- **Notebooks**: Gumamit ng malinaw na markdown cells para ipaliwanag ang mga konsepto
- **Imports**: Igrupo ayon sa standard library, third-party, lokal na imports

### Mga Konbensyon sa Jupyter Notebook

- Isama ang mga naglalarawang markdown cells bago ang mga code cells
- Magdagdag ng mga halimbawa ng output sa mga notebook bilang sanggunian
- Gumamit ng malinaw na mga pangalan ng variable na tumutugma sa mga konsepto ng leksyon
- Panatilihing linear ang pagpapatakbo ng notebook (cell 1 → 2 → 3...)

### Organisasyon ng File

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Pagbuo at Deployment

### Pagbuo ng Dokumentasyon

Ang repositoryong ito ay gumagamit ng Markdown para sa dokumentasyon:
- Mga README.md na file sa bawat folder ng leksyon
- Pangunahing README.md sa root ng repository
- Automated na sistema ng pagsasalin gamit ang GitHub Actions

### CI/CD Pipeline

Matatagpuan sa `.github/workflows/`:

1. **co-op-translator.yml** - Awtomatikong pagsasalin sa mahigit 50 wika
2. **welcome-issue.yml** - Pagbati sa mga bagong naglalagay ng isyu
3. **welcome-pr.yml** - Pagbati sa mga bagong nag-aambag ng pull request

### Deployment

Ito ay isang edukasyonal na repository - walang proseso ng deployment. Mga gumagamit:
1. I-fork o i-clone ang repository
2. Patakbuhin ang mga notebook nang lokal o sa GitHub Codespaces
3. Matuto sa pamamagitan ng pagbabago at pagsubok ng mga halimbawa

## Mga Alituntunin para sa Pull Request

### Bago Mag-submit

1. **Subukan ang mga pagbabago:**
   - Patakbuhin nang buo ang mga naapektuhang notebook
   - Siguraduhing ang lahat ng cells ay nagpapatakbo nang walang error
   - Tingnan kung ang mga output ay angkop

2. **Pag-update ng dokumentasyon:**
   - I-update ang README.md kung magdaragdag ng bagong konsepto
   - Magdagdag ng mga komento sa mga notebook para sa kumplikadong code
   - Tiyakin na nagpapaliwanag ang mga markdown cells sa layunin

3. **Pagbabago sa file:**
   - Iwasang i-commit ang `.env` files (gamitin ang `.env.example`)
   - Huwag i-commit ang `venv/` o `__pycache__/` na mga direktoryo
   - Panatilihin ang mga output ng notebook kapag nagpapakita ito ng mga konsepto
   - Alisin ang mga pansamantala at backup na mga notebook (`*-backup.ipynb`)

### Format ng Pamagat ng PR

Gumamit ng mga naglalarawang pamagat:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Mga Kinakailangang Check

- Dapat magpatakbo nang walang error ang mga notebook
- Dapat malinaw at tumpak ang mga README files
- Sundin ang umiiral na mga pattern ng code sa repository
- Panatilihin ang pagkakapare-pareho sa ibang mga leksyon

## Karagdagang Tala

### Mga Karaniwang Problema

1. **Hindi tugmang bersyon ng Python:**
   - Tiyakin na Python 3.12+ ang ginagamit
   - Maaaring hindi gumana ang ilang mga package sa lumang bersyon
   - Gamitin ang `python3 -m venv` para tukuyin nang malinaw ang bersyon ng Python

2. **Mga environment variable:**
   - Laging gumawa ng `.env` mula sa `.env.example`
   - Huwag i-commit ang `.env` na file (nasa `.gitignore` ito)
   - Mag-sign in gamit ang `az login` para sa keyless Entra ID authentication

3. **Mga salungatan sa package:**
   - Gumamit ng bagong virtual environment
   - Mag-install gamit ang `requirements.txt` sa halip na indibidwal na mga package
   - Ang ilang mga notebook ay maaaring mangailangan ng karagdagang mga package na binanggit sa kanilang mga markdown cells

4. **Mga serbisyo sa Azure:**
   - Nangangailangan ang Azure AI services ng aktibong subscription
   - Ang ilang mga tampok ay region-specific
   - Siguraduhing sinusuportahan ng Azure OpenAI model deployment ang Responses API

### Landas ng Pagkatuto

Inirerekomendang pagkakasunod-sunod sa mga leksyon:
1. **00-course-setup** - Simulan dito para sa setup ng environment
2. **01-intro-to-ai-agents** - Unawain ang mga pundasyon ng AI agent
3. **02-explore-agentic-frameworks** - Matutunan ang tungkol sa iba't ibang mga framework
4. **03-agentic-design-patterns** - Mga pangunahing disenyo na pattern
5. Magpatuloy sa mga leksyon ayon sa numero nang sunud-sunod

### Pagpili ng Framework

Piliin ang framework ayon sa iyong mga layunin:
- **Lahat ng leksyon**: Microsoft Agent Framework (MAF) gamit ang `FoundryChatClient`
- **Mga agents ay nagrerehistro sa server-side** sa Microsoft Foundry Agent Service V2 at makikita sa Foundry portal

### Pagkuha ng Tulong

- Sumali sa [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Suriin ang mga README file ng leksyon para sa tiyak na gabay
- Tingnan ang pangunahing [README.md](./README.md) para sa pangkalahatang kurso
- Tumukoy sa [Course Setup](./00-course-setup/README.md) para sa detalyadong mga tagubilin sa setup

### Pagsang-ayon

Ito ay isang bukas na edukasyonal na proyekto. Malugod ang mga kontribusyon:
- Pagandahin ang mga halimbawa ng code
- Ayusin ang mga typo o error
- Magdagdag ng nakapapalinaw na mga komento
- Mungkahi ng mga bagong paksa ng leksyon
- Isalin sa iba pang mga wika

Tingnan ang [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para sa kasalukuyang mga pangangailangan.

## Kontekstong Espesipiko sa Proyekto

### Suporta sa Maramihang Wika

Ang repositoryong ito ay gumagamit ng automated na sistema ng pagsasalin:
- Suportado ang mahigit 50 na wika
- Mga pagsasalin ay nasa mga direktoryo ng `/translations/<lang-code>/`
- Pinamamahalaan ng GitHub Actions workflow ang mga pag-update sa pagsasalin
- Ang mga source file ay nasa Ingles sa root ng repository

### Istruktura ng Leksiyon

Sinusunod ng bawat leksyon ang isang pare-parehong pattern:
1. Thumbnail ng video na may link
2. Nakalarawang nilalaman ng leksyon (README.md)
3. Mga halimbawa ng code sa iba't ibang framework
4. Mga layunin sa pag-aaral at mga kinakailangan
5. Mga dagdag na mapagkukunan sa pag-aaral na naka-link

### Pagpapangalan ng Code Sample

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Leksiyon 1, MAF Python
- `14-sequential.ipynb` - Leksiyon 14, mga advanced na pattern ng MAF
- `16-python-agent-framework.ipynb` - Leksiyon 16, ahente sa suporta ng customer sa produksyon
- `17-local-agent-foundry-local.ipynb` - Leksiyon 17, lokal na ahente gamit ang Foundry Local + Qwen

### Mga Espesyal na Direktoryo

- `translated_images/` - Lokal na mga larawan para sa pagsasalin
- `images/` - Orihinal na mga larawan para sa nilalamang Ingles
- `.devcontainer/` - Konfigurasyon ng development container para sa VS Code
- `.github/` - Mga workflow at template ng GitHub Actions

### Mga Dependencies

Pangunahing mga package mula sa `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suporta sa Agent-to-Agent protocol
- `azure-ai-inference`, `azure-ai-projects` - Mga serbisyo ng Azure AI
- `azure-identity` - Authentication ng Azure (AzureCliCredential)
- `azure-search-documents` - Integrasyon ng Azure AI Search
- `mcp[cli]` - Suporta sa Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->