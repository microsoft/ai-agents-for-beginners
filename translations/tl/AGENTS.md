# AGENTS.md

## Pangkalahatang Ideya ng Proyekto

Ang repositoryong ito ay naglalaman ng "Mga AI Agents para sa mga Baguhan" - isang komprehensibong kurso sa edukasyon na nagtuturo ng lahat ng kinakailangan upang makagawa ng AI Agents. Ang kurso ay binubuo ng 18 na aralin na sumasaklaw sa mga pundasyon, disenyo ng mga pattern, mga framework, at pagpapalaganap sa produksyon ng mga AI agent.

**Pangunahing Teknolohiya:**
- Python 3.12+
- Jupyter Notebooks para sa interaktibong pagkatuto
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkitektura:**
- Istruktura batay sa aralin (00-15+ mga direktoryo)
- Bawat aralin ay naglalaman ng: README na dokumentasyon, mga halimbawa ng code (Jupyter notebooks), at mga larawan
- Multi-language support gamit ang automated translation system
- Isang Python notebook bawat aralin gamit ang Microsoft Agent Framework

## Mga Utos sa Setup

### Mga Kinakailangan
- Python 3.12 o mas mataas pa
- Azure subscription (para sa Microsoft Foundry)
- Azure CLI na naka-install at naka-authenticate (`az login`)

### Paunang Setup

1. **I-clone o i-fork ang repositoryo:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # O
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Gumawa at i-activate ang Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sa Windows: venv\Scripts\activate
   ```

3. **I-install ang mga dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **I-set up ang mga environment variables:**
   ```bash
   cp .env.example .env
   # I-edit ang .env gamit ang iyong mga API key at mga endpoint
   ```

### Kinakailangang Mga Environment Variable

Para sa **Microsoft Foundry** (Kinakailangan):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Pangalan ng deployment ng modelo (e.g., gpt-4o)

Para sa **Azure AI Search** (Aralin 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Patakbuhin ang `az login` bago patakbuhin ang mga notebook (gamit ang `AzureCliCredential`).

## Daloy ng Pag-unlad

### Pagpapatakbo ng mga Jupyter Notebooks

Bawat aralin ay naglalaman ng maraming Jupyter notebooks para sa iba't ibang mga framework:

1. **Simulan ang Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pumunta sa direktoryo ng aralin** (hal., `01-intro-to-ai-agents/code_samples/`)

3. **Buksan at patakbuhin ang mga notebook:**
   - `*-python-agent-framework.ipynb` - Gamit ang Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Gamit ang Microsoft Agent Framework (.NET)

### Paggamit ng Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Nangangailangan ng Azure subscription
- Ginagamit ang `FoundryChatClient` para sa Agent Service V2 (mga agent nakikita sa Foundry portal)
- Handa para sa produksyon na may built-in na obserbabilidad
- Pattern ng filename: `*-python-agent-framework.ipynb`

## Mga Panuto sa Pagsusuri

Ito ay isang edukasyonal na repositoryo na may mga halimbawa ng code sa halip na code para sa produksyon na may automated tests. Upang beripikahin ang iyong setup at mga pagbabago:

### Manual na Pagsusuri

1. **Subukan ang Python environment:**
   ```bash
   python --version  # Dapat ay 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Subukan ang pagpapatakbo ng notebook:**
   ```bash
   # I-convert ang notebook sa script at patakbuhin (tinetest ang mga import)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Beripikahin ang mga environment variable:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Pagpapatakbo ng Indibidwal na mga Notebook

Buksan ang mga notebook sa Jupyter at ipatupad ang mga cell nang sunud-sunod. Ang bawat notebook ay self-contained at naglalaman ng:
- Mga import statement
- Pag-load ng configuration
- Mga halimbawa ng implementasyon ng agent
- Mga inaasahang output sa mga markdown cell

## Estilo ng Code

### Mga Konbensyon sa Python

- **Bersyon ng Python**: 3.12+
- **Estilo ng Code**: Sundin ang karaniwang konbensyon ng Python PEP 8
- **Mga Notebook**: Gumamit ng malinaw na mga markdown cell upang ipaliwanag ang mga konsepto
- **Mga Import**: I-grupo ayon sa standard library, third-party, local imports

### Mga Konbensyon sa Jupyter Notebook

- Isama ang mga naglalarawang markdown cell bago ang mga code cell
- Magdagdag ng mga halimbawa ng output sa mga notebook para sa sanggunian
- Gumamit ng malinaw na mga pangalan ng variable na tumutugma sa mga konsepto ng aralin
- Panatilihin ang linear na pagkakasunud-sunod ng pagpapatakbo ng notebook (cell 1 → 2 → 3...)

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

## Pagbuo at Pagpapalaganap

### Pagbuo ng Dokumentasyon

Ginagamit ng repositoryong ito ang Markdown para sa dokumentasyon:
- Mga README.md na file sa bawat folder ng aralin
- Pangunahing README.md sa root ng repositoryo
- Automated na sistema ng pagsasalin gamit ang GitHub Actions

### CI/CD Pipeline

Matatagpuan sa `.github/workflows/`:

1. **co-op-translator.yml** - Awtomatikong pagsasalin sa higit 50+ na mga wika
2. **welcome-issue.yml** - Pagtanggap sa mga bagong gumawa ng isyu
3. **welcome-pr.yml** - Pagtanggap sa mga bagong nag-aambag na pull request

### Pagpapalaganap

Ito ay isang edukasyonal na repositoryo - walang proseso ng pagpapalaganap. Mga gumagamit:
1. I-fork o i-clone ang repositoryo
2. Patakbuhin ang mga notebook nang lokal o sa GitHub Codespaces
3. Matuto sa pamamagitan ng pagbabago at pagsubok sa mga halimbawa

## Mga Gabay sa Pull Request

### Bago Mag-submit

1. **Subukan ang iyong mga pagbabago:**
   - Patakbuhin nang buo ang mga apektadong notebook
   - Siguraduhing lahat ng cell ay tumatakbo nang walang error
   - Tingnan na ang mga output ay naaayon

2. **Update sa dokumentasyon:**
   - I-update ang README.md kung magdadagdag ng bagong mga konsepto
   - Magdagdag ng mga komento sa mga notebook para sa komplikadong code
   - Siguraduhing ang mga markdown cell ay nagpapaliwanag ng layunin

3. **Pagbabago sa mga file:**
   - Iwasan ang pag-commit ng `.env` na mga file (gamitin ang `.env.example`)
   - Huwag i-commit ang mga directory ng `venv/` o `__pycache__/`
   - Panatilihin ang mga output ng notebook kapag nagpapakita ng mga konsepto
   - Alisin ang mga pansamantalang file at backup na notebook (`*-backup.ipynb`)

### Format ng PR Title

Gumamit ng deskriptibong mga pamagat:
- `[Lesson-XX] Magdagdag ng bagong halimbawa para sa <concept>`
- `[Fix] Itama ang typo sa lesson-XX README`
- `[Update] Pagbutihin ang sample code sa lesson-XX`
- `[Docs] I-update ang mga tagubilin sa setup`

### Kinakailangang Mga Check

- Ang mga notebook ay dapat tumakbo nang walang error
- Ang mga README file ay dapat malinaw at tumpak
- Sundin ang umiiral na mga pattern ng code sa repositoryo
- Panatilihin ang pagkakapare-pareho sa iba pang mga aralin

## Karagdagang Mga Tala

### Karaniwang mga Problema

1. **Hindi pagtugma ng bersyon ng Python:**
   - Siguraduhing Python 3.12+ ang ginagamit
   - Ang ilang mga package ay maaaring hindi gumana sa mga mas lumang bersyon
   - Gamitin ang `python3 -m venv` para tukuyin ang bersyon ng Python nang malinaw

2. **Mga environment variable:**
   - Laging gumawa ng `.env` mula sa `.env.example`
   - Huwag i-commit ang `.env` na file (ito ay nasa `.gitignore`)
   - Mag-sign in gamit ang `az login` para sa keyless Entra ID authentication

3. **Mga conflict sa package:**
   - Gumamit ng bagong virtual environment
   - Mag-install mula sa `requirements.txt` kaysa sa indibidwal na mga package
   - Ang ilang mga notebook ay maaaring mangailangan ng karagdagang mga package na binabanggit sa kanilang mga markdown cell

4. **Azure services:**
   - Nangangailangan ng aktibong subscription ang Azure AI services
   - Ang ilang mga feature ay naka-region specific
   - Siguraduhing sinusuportahan ng iyong Azure OpenAI model deployment ang Responses API

### Landas ng Pagkatuto

Inirerekomendang pagkakasunod-sunod ng mga aralin:
1. **00-course-setup** - Magsimula dito para sa setup ng environment
2. **01-intro-to-ai-agents** - Unawain ang mga pundasyon ng AI agent
3. **02-explore-agentic-frameworks** - Matutunan ang tungkol sa iba't ibang framework
4. **03-agentic-design-patterns** - Mga pangunahing disenyo ng pattern
5. Magpatuloy sa mga numbered na aralin nang sunud-sunod

### Pagpili ng Framework

Pumili ng framework batay sa iyong mga layunin:
- **Lahat ng aralin**: Microsoft Agent Framework (MAF) gamit ang `FoundryChatClient`
- **Agents ay nagrerehistro server-side** sa Microsoft Foundry Agent Service V2 at makikita sa Foundry portal

### Pagkuha ng Tulong

- Sumali sa [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Suriin ang mga README file ng aralin para sa partikular na gabay
- Tingnan ang pangunahing [README.md](./README.md) para sa pangkalahatang ideya ng kurso
- Tumukoy sa [Course Setup](./00-course-setup/README.md) para sa detalyadong mga tagubilin sa setup

### Pagsusumite ng Ambag

Ito ay isang bukas na edukasyonal na proyekto. Malugod na tinatanggap ang mga kontribusyon:
- Pagbutihin ang mga halimbawa ng code
- Itama ang mga typo o error
- Magdagdag ng mga paliwanag na komento
- Magmungkahi ng mga bagong paksa sa aralin
- Magsalin sa karagdagang mga wika

Tingnan ang [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para sa kasalukuyang mga pangangailangan.

## Konteksto na Tiyak sa Proyekto

### Suporta sa Maramihang Wika

Ginagamit ng repositoryong ito ang isang automated translation system:
- Sinusuportahan ang higit sa 50+ wika
- Mga pagsasalin ay nasa mga direktoryo ng `/translations/<lang-code>/`
- Ang GitHub Actions workflow ang humahawak ng mga update sa pagsasalin
- Ang mga source file ay nasa Ingles sa root ng repositoryo

### Istruktura ng Aralin

Ang bawat aralin ay sumusunod sa isang pare-parehong pattern:
1. Video thumbnail na may link
2. Nakasulat na nilalaman ng aralin (README.md)
3. Mga halimbawa ng code sa iba't ibang framework
4. Mga layunin sa pagkatuto at mga kinakailangan
5. Mga dagdag na mapagkukunan ng pagkatuto na naka-link

### Pagpapangalan ng Halimbawa ng Code

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Aralin 1, MAF Python
- `14-sequential.ipynb` - Aralin 14, mga advanced na pattern ng MAF

### Espesyal na Mga Direktoryo

- `translated_images/` - Mga lokal na larawan para sa mga pagsasalin
- `images/` - Orihinal na mga larawan para sa nilalaman sa Ingles
- `.devcontainer/` - Konfigurasyon ng VS Code development container
- `.github/` - Mga workflow at template ng GitHub Actions

### Mga Dependency

Pangunahing mga package mula sa `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suporta sa Agent-to-Agent protocol
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure authentication (AzureCliCredential)
- `azure-search-documents` - Integrasyon ng Azure AI Search
- `mcp[cli]` - Suporta sa Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->