# AGENTS.md

## Pangkalahatang-ideya ng Proyekto

Ang repository na ito ay naglalaman ng "AI Agents for Beginners" - isang komprehensibong kurso na nagtuturo ng lahat ng kailangan upang makabuo ng AI Agents. Binubuo ang kurso ng mahigit 15 na mga aralin na sumasaklaw sa mga pangunahing kaalaman, disenyo ng mga pattern, mga framework, at pag-deploy ng AI agents sa produksyon.

**Pangunahing Teknolohiya:**
- Python 3.12+
- Jupyter Notebooks para sa interaktibong pag-aaral
- AI Frameworks: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI Services: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (may libreng tier)

**Arkitektura:**
- Estruktura batay sa aralin (00-15+ na mga direktoryo)
- Bawat aralin ay naglalaman ng: README na dokumentasyon, mga halimbawa ng code (Jupyter notebooks), at mga imahe
- Suporta sa maraming wika gamit ang automated na sistema ng pagsasalin
- Maramihang opsyon ng framework sa bawat aralin (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Mga Utos sa Setup

### Mga Kinakailangan
- Python 3.12 o mas mataas
- GitHub account (para sa GitHub Models - libreng tier)
- Azure subscription (opsyonal, para sa Azure AI services)

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

4. **I-set up ang mga environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### Mga Kinakailangang Environment Variables

Para sa **GitHub Models (Libre):**
- `GITHUB_TOKEN` - Personal access token mula sa GitHub

Para sa **Azure AI Services** (opsyonal):
- `PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API key
- `AZURE_OPENAI_ENDPOINT` - URL ng Azure OpenAI endpoint
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Pangalan ng deployment para sa chat model
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Pangalan ng deployment para sa embeddings
- Karagdagang Azure configuration na makikita sa `.env.example`

## Workflow ng Pag-develop

### Pagpapatakbo ng Jupyter Notebooks

Ang bawat aralin ay naglalaman ng maraming Jupyter notebooks para sa iba't ibang framework:

1. **Simulan ang Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pumunta sa direktoryo ng aralin** (hal., `01-intro-to-ai-agents/code_samples/`)

3. **Buksan at patakbuhin ang mga notebooks:**
   - `*-semantic-kernel.ipynb` - Gamit ang Semantic Kernel framework
   - `*-autogen.ipynb` - Gamit ang AutoGen framework
   - `*-python-agent-framework.ipynb` - Gamit ang Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Gamit ang Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Gamit ang Azure AI Agent Service

### Paggamit ng Iba't ibang Framework

**Semantic Kernel + GitHub Models:**
- May libreng tier gamit ang GitHub account
- Maganda para sa pag-aaral at eksperimento
- Pattern ng file: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- May libreng tier gamit ang GitHub account
- Kakayahan sa multi-agent orchestration
- Pattern ng file: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Pinakabagong framework mula sa Microsoft
- Available sa Python at .NET
- Pattern ng file: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Nangangailangan ng Azure subscription
- Mga tampok na handa para sa produksyon
- Pattern ng file: `*-azureaiagent.ipynb`

## Mga Tagubilin sa Pagsubok

Ito ay isang pang-edukasyong repository na may mga halimbawa ng code sa halip na production code na may automated tests. Upang i-verify ang iyong setup at mga pagbabago:

### Manual na Pagsubok

1. **Subukan ang Python environment:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Subukan ang pagpapatakbo ng notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **I-verify ang mga environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Pagpapatakbo ng Indibidwal na Notebooks

Buksan ang mga notebooks sa Jupyter at patakbuhin ang mga cells nang sunod-sunod. Ang bawat notebook ay self-contained at naglalaman ng:
- Mga import statements
- Pag-load ng configuration
- Mga halimbawa ng implementasyon ng agent
- Mga inaasahang output sa markdown cells

## Estilo ng Code

### Mga Convention sa Python

- **Bersyon ng Python**: 3.12+
- **Estilo ng Code**: Sundin ang standard na Python PEP 8 conventions
- **Notebooks**: Gumamit ng malinaw na markdown cells upang ipaliwanag ang mga konsepto
- **Imports**: I-grupo ayon sa standard library, third-party, at local imports

### Mga Convention sa Jupyter Notebook

- Isama ang mga deskriptibong markdown cells bago ang mga code cells
- Magdagdag ng mga halimbawa ng output sa notebooks para sa reference
- Gumamit ng malinaw na pangalan ng variable na tumutugma sa mga konsepto ng aralin
- Panatilihin ang linear na pagkakasunod-sunod ng notebook execution (cell 1 → 2 → 3...)

### Organisasyon ng File

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## Pagbuo at Pag-deploy

### Pagbuo ng Dokumentasyon

Ang repository na ito ay gumagamit ng Markdown para sa dokumentasyon:
- README.md files sa bawat folder ng aralin
- Pangunahing README.md sa ugat ng repository
- Automated na sistema ng pagsasalin gamit ang GitHub Actions

### CI/CD Pipeline

Matatagpuan sa `.github/workflows/`:

1. **co-op-translator.yml** - Awtomatikong pagsasalin sa mahigit 50 na wika
2. **welcome-issue.yml** - Binabati ang mga bagong tagalikha ng isyu
3. **welcome-pr.yml** - Binabati ang mga bagong contributor ng pull request

### Pag-deploy

Ito ay isang pang-edukasyong repository - walang proseso ng pag-deploy. Mga user:
1. I-fork o i-clone ang repository
2. Patakbuhin ang mga notebooks nang lokal o sa GitHub Codespaces
3. Matuto sa pamamagitan ng pagbabago at eksperimento sa mga halimbawa

## Mga Alituntunin sa Pull Request

### Bago Mag-submit

1. **Subukan ang iyong mga pagbabago:**
   - Patakbuhin ang mga notebooks na apektado nang buo
   - Siguraduhing walang error ang lahat ng cells
   - Suriin na ang mga output ay naaangkop

2. **Mga update sa dokumentasyon:**
   - I-update ang README.md kung magdaragdag ng bagong konsepto
   - Magdagdag ng mga komento sa notebooks para sa kumplikadong code
   - Siguraduhing ipinaliwanag ng markdown cells ang layunin

3. **Mga pagbabago sa file:**
   - Iwasang i-commit ang `.env` files (gumamit ng `.env.example`)
   - Huwag i-commit ang `venv/` o `__pycache__/` na mga direktoryo
   - Panatilihin ang mga output ng notebook kapag nagpapakita ng mga konsepto
   - Alisin ang mga temporary files at backup notebooks (`*-backup.ipynb`)

### Format ng PR Title

Gumamit ng deskriptibong mga pamagat:
- `[Lesson-XX] Magdagdag ng bagong halimbawa para sa <konsepto>`
- `[Fix] Ayusin ang typo sa lesson-XX README`
- `[Update] Pagbutihin ang halimbawa ng code sa lesson-XX`
- `[Docs] I-update ang mga tagubilin sa setup`

### Mga Kinakailangang Pagsusuri

- Ang mga notebooks ay dapat tumakbo nang walang error
- Ang mga README files ay dapat malinaw at tama
- Sundin ang umiiral na mga pattern ng code sa repository
- Panatilihin ang pagkakapare-pareho sa iba pang mga aralin

## Karagdagang Tala

### Karaniwang Problema

1. **Hindi tugma ang bersyon ng Python:**
   - Siguraduhing Python 3.12+ ang ginagamit
   - Ang ilang mga package ay maaaring hindi gumana sa mas lumang bersyon
   - Gumamit ng `python3 -m venv` upang tukuyin ang bersyon ng Python nang malinaw

2. **Mga environment variables:**
   - Laging gumawa ng `.env` mula sa `.env.example`
   - Huwag i-commit ang `.env` file (nasa `.gitignore` ito)
   - Ang GitHub token ay nangangailangan ng tamang mga pahintulot

3. **Mga salungatan sa package:**
   - Gumamit ng bagong virtual environment
   - Mag-install mula sa `requirements.txt` sa halip na indibidwal na mga package
   - Ang ilang mga notebooks ay maaaring mangailangan ng karagdagang mga package na binanggit sa kanilang markdown cells

4. **Azure services:**
   - Ang Azure AI services ay nangangailangan ng aktibong subscription
   - Ang ilang mga tampok ay partikular sa rehiyon
   - May mga limitasyon ang libreng tier para sa GitHub Models

### Landas ng Pag-aaral

Inirerekomendang pagkakasunod-sunod ng mga aralin:
1. **00-course-setup** - Magsimula dito para sa setup ng environment
2. **01-intro-to-ai-agents** - Unawain ang mga pangunahing kaalaman sa AI agent
3. **02-explore-agentic-frameworks** - Matutunan ang iba't ibang framework
4. **03-agentic-design-patterns** - Mga pangunahing disenyo ng pattern
5. Magpatuloy sa mga aralin ayon sa pagkakasunod-sunod ng numero

### Pagpili ng Framework

Pumili ng framework batay sa iyong layunin:
- **Pag-aaral/Pag-prototype**: Semantic Kernel + GitHub Models (libre)
- **Multi-agent systems**: AutoGen
- **Pinakabagong tampok**: Microsoft Agent Framework (MAF)
- **Pag-deploy sa produksyon**: Azure AI Agent Service

### Pagkuha ng Tulong

- Sumali sa [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Suriin ang README files ng aralin para sa partikular na gabay
- Tingnan ang pangunahing [README.md](./README.md) para sa pangkalahatang-ideya ng kurso
- Tingnan ang [Course Setup](./00-course-setup/README.md) para sa detalyadong tagubilin sa setup

### Pag-aambag

Ito ay isang bukas na pang-edukasyong proyekto. Malugod na tinatanggap ang mga kontribusyon:
- Pagbutihin ang mga halimbawa ng code
- Ayusin ang mga typo o error
- Magdagdag ng mga nakakapaglinaw na komento
- Magmungkahi ng mga bagong paksa ng aralin
- Isalin sa karagdagang mga wika

Tingnan ang [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para sa kasalukuyang pangangailangan.

## Konteksto ng Proyekto

### Suporta sa Maraming Wika

Ang repository na ito ay gumagamit ng automated na sistema ng pagsasalin:
- Suporta sa mahigit 50 na wika
- Mga pagsasalin sa `/translations/<lang-code>/` na mga direktoryo
- Ang workflow ng GitHub Actions ang humahawak sa mga update sa pagsasalin
- Ang mga source file ay nasa Ingles sa ugat ng repository

### Estruktura ng Aralin

Ang bawat aralin ay sumusunod sa pare-parehong pattern:
1. Thumbnail ng video na may link
2. Nakatalang nilalaman ng aralin (README.md)
3. Mga halimbawa ng code sa maraming framework
4. Mga layunin sa pag-aaral at mga kinakailangan
5. Mga karagdagang mapagkukunan ng pag-aaral na naka-link

### Pangalan ng Halimbawa ng Code

Format: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Aralin 4, Semantic Kernel
- `07-autogen.ipynb` - Aralin 7, AutoGen
- `14-python-agent-framework.ipynb` - Aralin 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Aralin 14, MAF .NET

### Mga Espesyal na Direktoryo

- `translated_images/` - Mga lokal na imahe para sa mga pagsasalin
- `images/` - Mga orihinal na imahe para sa nilalaman sa Ingles
- `.devcontainer/` - Konfigurasyon ng VS Code development container
- `.github/` - Mga workflow at template ng GitHub Actions

### Mga Dependencies

Pangunahing mga package mula sa `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen framework
- `semantic-kernel` - Semantic Kernel framework
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-search-documents` - Integrasyon ng Azure AI Search
- `chromadb` - Vector database para sa mga halimbawa ng RAG
- `chainlit` - Framework para sa Chat UI
- `browser_use` - Automation ng browser para sa mga agents
- `mcp[cli]` - Suporta sa Model Context Protocol
- `mem0ai` - Pamamahala ng memorya para sa mga agents

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.