# AGENTS.md

## Project Overview

Ang repository na ito ay naglalaman ng "AI Agents for Beginners" - isang komprehensibong kursong pang-edukasyon na nagtuturo ng lahat ng kinakailangan upang makabuo ng AI Agents. Ang kurso ay binubuo ng higit sa 15 leksyon na sumasaklaw sa mga pundasyon, design patterns, frameworks, at produksyon ng deployment ng mga AI agent.

**Pangunahing Teknolohiya:**
- Python 3.12+
- Jupyter Notebooks para sa interaktibong pag-aaral
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkitektura:**
- Istrakturang nakabatay sa mga leksyon (mga direktoryo 00-15+)
- Bawat leksyon ay naglalaman ng: README dokumentasyon, mga code sample (Jupyter notebooks), at mga larawan
- Suporta sa maraming wika sa pamamagitan ng automated translation system
- Isang Python notebook kada leksyon gamit ang Microsoft Agent Framework

## Setup Commands

### Prerequisites
- Python 3.12 o mas mataas
- Azure subscription (para sa Azure AI Foundry)
- Azure CLI na naka-install at authenticated (`az login`)

### Initial Setup

1. **I-clone o i-fork ang repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # O PHP
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

4. **I-setup ang environment variables:**
   ```bash
   cp .env.example .env
   # I-edit ang .env gamit ang iyong mga API key at mga endpoint
   ```

### Kinakailangang Environment Variables

Para sa **Azure AI Foundry** (Kinakailangan):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Pangalan ng model deployment (e.g., gpt-4o)

Para sa **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Patakbuhin ang `az login` bago magpatakbo ng mga notebook (gamit ang `AzureCliCredential`).

## Development Workflow

### Pagpapatakbo ng Jupyter Notebooks

Ang bawat leksyon ay naglalaman ng maraming Jupyter notebooks para sa iba't ibang frameworks:

1. **Simulan ang Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pumunta sa direktoryo ng leksyon** (e.g., `01-intro-to-ai-agents/code_samples/`)

3. **Buksan at patakbuhin ang mga notebook:**
   - `*-python-agent-framework.ipynb` - Gamit ang Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Gamit ang Microsoft Agent Framework (.NET)

### Paggamit ng Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Nangangailangan ng Azure subscription
- Gumagamit ng `AzureAIProjectAgentProvider` para sa Agent Service V2 (nakikita ang mga agent sa Foundry portal)
- Handa para sa produksyon na may built-in na observability
- Pattern ng file: `*-python-agent-framework.ipynb`

## Testing Instructions

Ito ay isang edukasyonal na repository na may mga halimbawa ng code, hindi isang production code na may automated tests. Upang mapatunayan ang iyong setup at mga pagbabago:

### Manual Testing

1. **Subukan ang Python environment:**
   ```bash
   python --version  # Dapat ay 3.12 pataas
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Subukan ang notebook execution:**
   ```bash
   # I-convert ang notebook sa script at patakbuhin (nasusulit ang mga import)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Beripikahin ang environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Pagpatakbo ng Indibidwal na Notebooks

Buksan ang mga notebook sa Jupyter at isagawa ang mga cells nang sunud-sunod. Bawat notebook ay sariling kabuuan at may kasamang:
- Mga import statement
- Pag-load ng configuration
- Mga halimbawa ng implementasyon ng agent
- Mga inaasahang output sa markdown cells

## Code Style

### Mga Konbensiyon sa Python

- **Bersyon ng Python**: 3.12+
- **Code Style**: Sundin ang standard Python PEP 8 conventions
- **Mga Notebook**: Gumamit ng malinaw na markdown cells para ipaliwanag ang mga konsepto
- **Imports**: I-grupo ayon sa standard library, third-party, lokal na imports

### Konbensiyon ng Jupyter Notebook

- Maglagay ng mga deskriptibong markdown cells bago ang mga code cells
- Magdagdag ng mga halimbawa ng output sa notebooks bilang sanggunian
- Gumamit ng malinaw na mga pangalan ng variable na tumutugma sa mga konsepto ng leksyon
- Panatilihing linear ang order ng pagpapatakbo ng notebook (cell 1 → 2 → 3...)

### Organisasyon ng mga File

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Build and Deployment

### Paggawa ng Dokumentasyon

Gumagamit ang repository na ito ng Markdown para sa dokumentasyon:
- Mga README.md files sa bawat folder ng leksyon
- Pangunahing README.md sa root ng repository
- Automated translation system gamit ang GitHub Actions

### CI/CD Pipeline

Matatagpuan sa `.github/workflows/`:

1. **co-op-translator.yml** - Awtomatikong pagsasalin sa 50+ na wika
2. **welcome-issue.yml** - Pagsalubong sa mga bagong nag-create ng isyu
3. **welcome-pr.yml** - Pagsalubong sa mga bagong nag-contribute ng pull request

### Deployment

Ito ay isang edukasyonal na repository - walang proseso ng deployment. Ang mga gumagamit ay:
1. Mag-fork o mag-clone ng repository
2. Patakbuhin ang mga notebook lokal o sa GitHub Codespaces
3. Matuto sa pamamagitan ng pagbabago at pag-eeksperimento sa mga halimbawa

## Pull Request Guidelines

### Bago Mag-Submit

1. **Subukan ang mga pagbabago:**
   - Patakbuhin nang buo ang mga apektadong notebook
   - Siguraduhing lahat ng mga cells ay tumatakbo nang walang error
   - Tingnan na ang mga output ay naaangkop

2. **Mga update sa dokumentasyon:**
   - I-update ang README.md kung magdadagdag ng bagong konsepto
   - Maglagay ng mga komento sa notebooks para sa mahihirap na code
   - Siguraduhing ang mga markdown cells ay nagpapaliwanag ng layunin

3. **Mga pagbabago sa files:**
   - Iwasang i-commit ang mga `.env` files (gamitin ang `.env.example`)
   - Huwag i-commit ang mga direktoryo `venv/` o `__pycache__/`
   - Panatilihin ang output ng notebook kung nagpapakita ito ng mga konsepto
   - Alisin ang mga pansamantalang files at backup notebooks (`*-backup.ipynb`)

### Format ng PR Title

Gumamit ng mga deskriptibong titulo:
- `[Lesson-XX] Magdagdag ng bagong halimbawa para sa <concept>`
- `[Fix] Ayusin ang typo sa lesson-XX README`
- `[Update] Pagandahin ang code sample sa lesson-XX`
- `[Docs] I-update ang mga tagubilin sa setup`

### Kinakailangang Mga Check

- Dapat tumakbo ang mga notebook nang walang error
- Ang mga README files ay dapat malinaw at tumpak
- Sundin ang umiiral na mga pattern ng code sa repository
- Panatilihin ang pagkakapare-pareho sa ibang mga leksyon

## Karagdagang Tala

### Karaniwang Mga Isyu

1. **Hindi tugmang bersyon ng Python:**
   - Siguraduhing ginagamit ang Python 3.12+
   - Maaaring hindi gumana ang ilang packages sa mas lumang bersyon
   - Gamitin ang `python3 -m venv` upang tukuyin ang bersyon ng Python nang hayagan

2. **Mga environment variables:**
   - Laging gumawa ng `.env` mula sa `.env.example`
   - Huwag i-commit ang `.env` file (ito ay nasa `.gitignore`)
   - Ang GitHub token ay dapat may tamang mga permiso

3. **Mga conflict ng package:**
   - Gumamit ng bagong virtual environment
   - Mag-install mula sa `requirements.txt` kaysa sa mga indibidwal na package
   - Ang ilang mga notebook ay maaaring mangailangan ng karagdagang mga package na nakasaad sa kanilang markdown cells

4. **Mga serbisyo sa Azure:**
   - Nangangailangan ang Azure AI services ng aktibong subscription
   - Ang ilang features ay specific sa mga rehiyon
   - May mga limitasyon sa free tier para sa GitHub Models

### Landas ng Pag-aaral

Inirerekomendang sundan ang mga leksyon sa ganitong pagkakasunod:
1. **00-course-setup** - Simulan dito para sa setup ng environment
2. **01-intro-to-ai-agents** - Unawain ang mga pundasyon ng AI agent
3. **02-explore-agentic-frameworks** - Matuto tungkol sa iba't ibang frameworks
4. **03-agentic-design-patterns** - Mga pangunahing design patterns
5. Sundan ang mga susunod na numeradong leksyon nang sunud-sunod

### Pagpili ng Framework

Pumili ng framework batay sa iyong mga layunin:
- **Lahat ng leksyon**: Microsoft Agent Framework (MAF) gamit ang `AzureAIProjectAgentProvider`
- **Mga agent ay nire-register server-side** sa Azure AI Foundry Agent Service V2 at makikita sa Foundry portal

### Paghahanap ng Tulong

- Sumali sa [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Tingnan ang mga README file ng mga leksyon para sa partikular na gabay
- Suriin ang pangunahing [README.md](./README.md) para sa pangkalahatang-ideya ng kurso
- Basahin ang [Course Setup](./00-course-setup/README.md) para sa detalyadong tagubilin sa setup

### Pagsasangkot

Ito ay isang bukas na edukasyonal na proyekto. Malugod ang pagtanggap ng mga kontribusyon:
- Pagbutihin ang mga halimbawa ng code
- Ayusin ang mga typo o error
- Magdagdag ng mga paliwanag na komento
- Magmungkahi ng mga bagong paksa sa leksyon
- Isalin sa iba pang mga wika

Tingnan ang [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para sa kasalukuyang mga pangangailangan.

## Konteksto ng Proyekto

### Suporta sa Maramihang Wika

Gumagamit ang repository na ito ng automated translation system:
- Sinusuportahan ang 50+ na wika
- Mga pagsasalin sa `/translations/<lang-code>/` na mga direktoryo
- Pinangangasiwaan ng GitHub Actions workflow ang mga update sa pagsasalin
- Ang mga source file ay nasa Ingles sa root ng repository

### Istraktura ng Leksiyon

Ang bawat leksyon ay sumusunod sa isang consistent na pattern:
1. Thumbnail ng video na may link
2. Nakasaad na nilalaman ng leksyon (README.md)
3. Mga code sample sa iba't ibang framework
4. Mga layunin sa pag-aaral at mga kinakailangan
5. Mga karagdagang mapagkukunan ng pag-aaral na naka-link

### Pangalan ng Code Sample

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Leksiyon 1, MAF Python
- `14-sequential.ipynb` - Leksiyon 14, MAF advanced patterns

### Espesyal na Direktoryo

- `translated_images/` - Mga nilokalisa na larawan para sa mga pagsasalin
- `images/` - Orihinal na mga larawan para sa nilalaman na Ingles
- `.devcontainer/` - Konfigurasyon ng VS Code development container
- `.github/` - Mga workflow at template ng GitHub Actions

### Mga Dependencies

Pangunahing mga package mula sa `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suporta sa Agent-to-Agent protocol
- `azure-ai-inference`, `azure-ai-projects` - Mga serbisyo ng Azure AI
- `azure-identity` - Azure authentication (AzureCliCredential)
- `azure-search-documents` - Integrasyon ng Azure AI Search
- `mcp[cli]` - Suporta sa Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pahayag ng Pagwawakas**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat aming pinagsisikapang maging tumpak, pakatandaan na ang mga awtomatikong salin ay maaaring maglaman ng mga pagkakamali o di-katumpakan. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pinanggagalingang awtoridad. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng salin na ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->