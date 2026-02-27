# AGENTS.md

## Project Overview

Ang repositoryong ito ay naglalaman ng "AI Agents para sa mga Nagsisimula" - isang komprehensibong kursong pang-edukasyon na nagtuturo ng lahat ng kinakailangan upang makabuo ng AI Agents. Ang kurso ay binubuo ng 15+ na mga aralin na sumasaklaw sa mga pundasyon, disenyo ng mga pattern, mga frameworks, at produksyon deployment ng AI agents.

**Pangunahing Teknolohiya:**
- Python 3.12+
- Jupyter Notebooks para sa interaktibong pag-aaral
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkitektura:**
- Estruktura batay sa mga aralin (00-15+ mga direktoryo)
- Ang bawat aralin ay naglalaman: README dokumentasyon, mga halimbawa ng code (Jupyter notebooks), at mga larawan
- Suporta sa maraming wika gamit ang awtomatikong sistema ng pagsasalin
- Isang Python notebook kada aralin gamit ang Microsoft Agent Framework

## Setup Commands

### Prerequisites
- Python 3.12 o mas mataas pa
- Azure subscription (para sa Azure AI Foundry)
- Azure CLI na naka-install at naka-authenticate (`az login`)

### Initial Setup

1. **I-clone o i-fork ang repository:**
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

3. **I-install ang dependencies:**
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
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Pangalan ng deployment ng modelo (hal., gpt-4o)

Para sa **Azure AI Search** (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authentication: Patakbuhin ang `az login` bago patakbuhin ang mga notebook (gamit ang `AzureCliCredential`).

## Development Workflow

### Pagpapatakbo ng Jupyter Notebooks

Ang bawat aralin ay may maraming Jupyter notebooks para sa iba't ibang frameworks:

1. **Simulan ang Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pumunta sa direktoryo ng aralin** (hal., `01-intro-to-ai-agents/code_samples/`)

3. **Buksan at patakbuhin ang mga notebook:**
   - `*-python-agent-framework.ipynb` - Gamit ang Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Gamit ang Microsoft Agent Framework (.NET)

### Paggamit ng Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Nangangailangan ng Azure subscription
- Gumagamit ng `AzureAIProjectAgentProvider` para sa Agent Service V2 (nakikita ang mga agents sa Foundry portal)
- Handa na sa production na may built-in na observability
- Pattern ng file: `*-python-agent-framework.ipynb`

## Testing Instructions

Ito ay isang edukasyonal na repository na may mga halimbawa ng code, hindi mga production code na may automated tests. Para ma-verify ang iyong setup at mga pagbabago:

### Manual Testing

1. **Subukan ang Python environment:**
   ```bash
   python --version  # Dapat ay 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Subukan ang pagpapatakbo ng notebook:**
   ```bash
   # I-convert ang notebook sa script at patakbuhin (sinusubukan ang mga import)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Beripikahin ang environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Pagpapatakbo ng Bawat Notebook

Buksan ang mga notebook sa Jupyter at patakbuhin ang mga cells nang sunud-sunod. Ang bawat notebook ay self-contained at may kasamang:
- Mga import statements
- Pag-load ng configuration
- Mga halimbawa ng pag-implementa ng agent
- Inaasahang outputs sa mga markdown cells

## Code Style

### Mga Panuntunan sa Python

- **Bersyon ng Python**: 3.12+
- **Code Style**: Sundin ang standard na PEP 8 sa Python
- **Notebooks**: Gumamit ng malinaw na markdown cells para ipaliwanag ang mga konsepto
- **Imports**: I-group ayon sa standard library, third-party, at lokal na mga imports

### Mga Panuntunan sa Jupyter Notebook

- Maglagay ng deskriptibong markdown cells bago ang mga code cells
- Magdagdag ng mga halimbawa ng outputs sa mga notebook bilang reference
- Gumamit ng malinaw na pangalan ng variable na tumutugma sa mga konsepto ng aralin
- Panatilihing linear ang pagkakasunod ng pagpapatakbo ng notebook (cell 1 → 2 → 3...)

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

## Build and Deployment

### Pagbuo ng Dokumentasyon

Gumagamit ang repositoryong ito ng Markdown para sa dokumentasyon:
- README.md files sa bawat folder ng aralin
- Pangunahing README.md sa root ng repository
- Awtomatikong sistema ng pagsasalin gamit ang GitHub Actions

### CI/CD Pipeline

Matatagpuan sa `.github/workflows/`:

1. **co-op-translator.yml** - Awtomatikong pagsasalin sa 50+ wika
2. **welcome-issue.yml** - Pagbati sa mga bagong nagmumungkahi ng isyu
3. **welcome-pr.yml** - Pagbati sa mga bagong contributor ng pull request

### Deployment

Ito ay isang edukasyonal na repository - walang proseso ng deployment. Ang mga user ay:
1. Nagfo-fork o nagke-clone ng repository
2. Nagpapatakbo ng mga notebooks lokal o sa GitHub Codespaces
3. Nag-aaral sa pamamagitan ng pagbabago at pagsubok ng mga halimbawa

## Pull Request Guidelines

### Bago Mag-submit

1. **Subukan ang iyong mga pagbabago:**
   - Patakbuhin nang buo ang mga apektadong notebook
   - Siguraduhing walang error kapag pinatakbo lahat ng cells
   - Suriin kung ang mga outputs ay angkop

2. **Mga update sa Dokumentasyon:**
   - I-update ang README.md kapag nagdaragdag ng bagong konsepto
   - Maglagay ng komento sa mga notebook para sa mga kumplikadong code
   - Siguraduhing ipinapaliwanag ng mga markdown cells ang layunin

3. **Pagbabago ng mga File:**
   - Iwasang mag-commit ng `.env` files (gamitin ang `.env.example`)
   - Huwag mag-commit ng `venv/` o `__pycache__/` mga direktoryo
   - Panatilihin ang outputs ng notebook kapag nagpapakita ito ng mga konsepto
   - Tanggalin ang mga temporary files at backup notebooks (`*-backup.ipynb`)

### Format ng PR Title

Gumamit ng malinaw na mga pamagat:
- `[Lesson-XX] Magdagdag ng bagong halimbawa para sa <konsepto>`
- `[Fix] Itama ang typo sa lesson-XX README`
- `[Update] Pagbutihin ang halimbawa ng code sa lesson-XX`
- `[Docs] I-update ang mga tagubilin sa setup`

### Mga Kinakailangang Checks

- Dapat mapatakbo ang mga notebook nang walang error
- Dapat malinaw at tumpak ang mga README files
- Sundin ang umiiral na mga pattern ng code sa repository
- Panatilihin ang pagkakatugma sa iba pang mga leksyon

## Karagdagang Tala

### Mga Karaniwang Problema

1. **Hindi pagtugma ng bersyon ng Python:**
   - Siguraduhing gamit ang Python 3.12+
   - Ang ilang mga pakete ay maaaring hindi gumana sa mas lumang bersyon
   - Gamitin ang `python3 -m venv` upang tukuyin nang malinaw ang bersyon ng Python

2. **Environment variables:**
   - Palaging gumawa ng `.env` mula sa `.env.example`
   - Huwag mag-commit ng `.env` file (nasa `.gitignore` ito)
   - Kinakailangan ng GitHub token ang tamang mga pahintulot

3. **Mga conflict sa mga pakete:**
   - Gumamit ng bagong virtual environment
   - Mag-install mula sa `requirements.txt` kaysa sa individual na pakete
   - Ang ilang mga notebook ay maaaring mangailangan ng karagdagang mga pakete na binanggit sa kanilang mga markdown cells

4. **Mga serbisyo ng Azure:**
   - Nangangailangan ng aktibong subscription ang Azure AI services
   - Ang ilang mga tampok ay specific sa rehiyon
   - May mga limitasyon sa free tier para sa GitHub Models

### Daan ng Pag-aaral

Inirerekomendang pag-usad sa mga aralin:
1. **00-course-setup** - Simulan dito para sa setup ng environment
2. **01-intro-to-ai-agents** - Unawain ang mga pundasyon ng AI agent
3. **02-explore-agentic-frameworks** - Alamin ang iba't ibang frameworks
4. **03-agentic-design-patterns** - Mga pangunahing design patterns
5. Ipagpatuloy ang sunud-sunod na mga aralin ayon sa bilang

### Pagpili ng Framework

Piliin ang framework batay sa iyong mga layunin:
- **Lahat ng aralin**: Microsoft Agent Framework (MAF) gamit ang `AzureAIProjectAgentProvider`
- **Nagre-register ang mga agents server-side** sa Azure AI Foundry Agent Service V2 at makikita sa Foundry portal

### Paghahanap ng Tulong

- Sumali sa [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Suriin ang mga README files ng aralin para sa tiyak na gabay
- Tingnan ang pangunahing [README.md](./README.md) para sa overview ng kurso
- Refer sa [Course Setup](./00-course-setup/README.md) para sa detalyadong mga tagubilin sa setup

### Pag-aambag

Ito ay isang open educational project. Malugod ang pag-aambag:
- Pagbutihin ang mga halimbawa ng code
- Itama ang mga typograpikal na error o mali
- Magdagdag ng mga paliwanag na komento
- Magmungkahi ng mga bagong paksang aralin
- Isalin sa karagdagang mga wika

Tingnan ang [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para sa kasalukuyang pangangailangan.

## Project-Specific Context

### Suporta sa Maraming Wika

Gumagamit ang repositoryong ito ng awtomatikong sistema ng pagsasalin:
- Sinusuportahan ang 50+ na wika
- Mga pagsasalin sa `/translations/<lang-code>/` mga direktoryo
- Ginagawa ng GitHub Actions workflow ang pag-update ng pagsasalin
- Ang mga source file ay nasa Ingles sa root ng repository

### Estruktura ng Aralin

Ang bawat aralin ay sumusunod sa isang pare-parehong pattern:
1. Video thumbnail na may link
2. Nakasulat na nilalaman ng aralin (README.md)
3. Mga halimbawa ng code sa maraming frameworks
4. Mga layunin sa pag-aaral at mga kinakailangan
5. Karagdagang mga pinagkukunan ng pag-aaral na naka-link

### Pagpapangalan ng Code Sample

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Aralin 1, MAF Python
- `14-sequential.ipynb` - Aralin 14, MAF advanced patterns

### Espesyal na Mga Direktoryo

- `translated_images/` - Mga lokal na larawan para sa mga pagsasalin
- `images/` - Orihinal na mga larawan para sa Ingles na nilalaman
- `.devcontainer/` - VS Code development container configuration
- `.github/` - GitHub Actions workflows at mga template

### Mga Dependency

Pangunahing mga pakete mula sa `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suporta sa Agent-to-Agent protocol
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure authentication (AzureCliCredential)
- `azure-search-documents` - Integrasyon ng Azure AI Search
- `mcp[cli]` - Suporta sa Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->