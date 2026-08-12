# AGENTS.md

## Pangkalahatang-ideya ng Proyekto

Ang repositoryong ito ay naglalaman ng "AI Agents para sa Mga Nagsisimula" - isang komprehensibong kursong pang-edukasyon na nagtuturo ng lahat ng kinakailangan upang makagawa ng AI Agents. Ang kurso ay binubuo ng 18 na leksiyon (may bilang 00-18) na sumasaklaw sa mga pundasyon, disenyo ng mga pattern, mga framework, pag-deploy sa produksyon, mga lokal/on-device na agents, at seguridad ng mga AI agents.

**Pangunahing Teknolohiya:**
- Python 3.12+
- Jupyter Notebooks para sa interaktibong pag-aaral
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkitektura:**
- Istrukturang nakabatay sa leksiyon (mga direktoryo 00-15+)
- Bawat leksiyon ay may: dokumentasyong README, mga halimbawa ng code (Jupyter notebooks), at mga larawan
- Suporta sa maraming wika gamit ang automated translation system
- Isang Python notebook bawat leksiyon gamit ang Microsoft Agent Framework

## Mga Utos para sa Setup

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

3. **I-install ang mga dependency:**
   ```bash
   pip install -r requirements.txt
   ```

4. **I-set up ang mga environment variables:**
   ```bash
   cp .env.example .env
   # I-edit ang .env gamit ang iyong mga API key at mga endpoint
   ```

### Kinakailangang Environment Variables

Para sa **Microsoft Foundry** (Kailangan):
- `AZURE_AI_PROJECT_ENDPOINT` - endpoint ng proyekto sa Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - pangalan ng pag-deploy ng modelo (hal., gpt-5-mini)

Para sa **Azure AI Search** (Leksiyon 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - endpoint ng Azure AI Search
- `AZURE_SEARCH_API_KEY` - API key ng Azure AI Search

Pag-authenticate: Patakbuhin ang `az login` bago patakbuhin ang mga notebook (gamit ang `AzureCliCredential`).

## Daloy ng Pag-unlad

### Pagpapatakbo ng Jupyter Notebooks

Ang bawat leksiyon ay naglalaman ng maraming Jupyter notebooks para sa iba't ibang mga framework:

1. **Simulan ang Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Pumunta sa direktoryo ng leksiyon** (hal., `01-intro-to-ai-agents/code_samples/`)

3. **Buksan at patakbuhin ang mga notebook:**
   - `*-python-agent-framework.ipynb` - Gamit ang Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Gamit ang Microsoft Agent Framework (.NET)

### Paggamit ng Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Nangangailangan ng Azure subscription
- Gumagamit ng `FoundryChatClient` para sa Agent Service V2 (mga agent na makikita sa Foundry portal)
- Handa na para sa produksyon na may built-in na observability
- Pattern ng file: `*-python-agent-framework.ipynb`

## Mga Tagubilin sa Pagsubok

Ito ay isang repositoryong pang-edukasyon na may mga halimbawa ng code at hindi para sa produksyon na may automated tests. Upang beripikahin ang iyong setup at mga pagbabago:

### Manwal na Pagsubok

1. **Subukan ang Python environment:**
   ```bash
   python --version  # Dapat ay 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Subukan ang pagpapatakbo ng notebook:**
   ```bash
   # I-convert ang notebook sa script at patakbuhin (tumatakbo ang mga import para sa pagsusuri)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Beripikahin ang mga environment variables:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Pagpapatakbo ng Indibidwal na Mga Notebook

Buksan ang mga notebook sa Jupyter at patakbuhin ng sunud-sunod ang mga cells. Ang bawat notebook ay sapat na at naglalaman ng:
- Mga import statement
- Pag-load ng configuration
- Halimbawa ng mga implementasyon ng agent
- Mga inaasahang output sa mga markdown cell

### Smoke-Testing ng Mga Na-deploy na Agents

Para sa mga leksiyon kung saan ang agent ay na-deploy bilang isang Microsoft Foundry hosted agent (01, 04, 05, 16), nagbibigay ang repositoryo ng mga smoke-test catalog sa ilalim ng `tests/` na pinapatakbo ng `.github/workflows/smoke-test.yml` workflow gamit ang [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) action. Ito ay isang magaan na post-deploy na pag-gate (maaabot ba ang agent at sumusunod sa mga pangunahing prompt expectations?), na kumukumpleto sa evaluation pipeline sa Leksiyon 10 at 16. Tingnan ang [tests/README.md](./tests/README.md) para sa catalog-to-lesson-to-agent na pagkakaugnay. Ang Leksiyon 17 ay pinapatakbo nang lokal gamit ang Foundry Local at walang hosted endpoint, kaya ito ay beripikado sa pamamagitan ng direktang pagpapatakbo ng notebook nito.

## Estilo ng Code

### Mga Kumbensyon sa Python

- **Bersyon ng Python**: 3.12+
- **Estilo ng Code**: Sundin ang standard na PEP 8 na kumbensyon ng Python
- **Mga Notebook**: Gumamit ng malinaw na mga markdown cell upang ipaliwanag ang mga konsepto
- **Imports**: Pagsamahin ayon sa standard library, third-party, local imports

### Mga Kumbensyon sa Jupyter Notebook

- Isama ang mga deskriptibong markdown cell bago ang mga code cell
- Magdagdag ng halimbawa ng output sa mga notebook bilang sanggunian
- Gumamit ng malinaw na mga pangalan ng variable na tumutugma sa mga konsepto ng leksiyon
- Panatilihin ang linear na pagkakasunod-sunod ng pagpapatakbo ng notebook (cell 1 → 2 → 3...)

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

## Pagbuo at Pag-deploy

### Pagbuo ng Dokumentasyon

Ang repositoryong ito ay gumagamit ng Markdown para sa dokumentasyon:
- Mga README.md file sa bawat folder ng leksiyon
- Pangunahing README.md sa ugat ng repositoryo
- Automated translation system gamit ang GitHub Actions

### CI/CD Pipeline

Matatagpuan sa `.github/workflows/`:

1. **co-op-translator.yml** - Awtomatikong pagsasalin sa 50+ na mga wika
2. **welcome-issue.yml** - Pagsalubong sa mga bagong gumawa ng isyu
3. **welcome-pr.yml** - Pagsalubong sa mga bagong nag-ambag ng pull request

### Pag-deploy

Ito ay isang repositoryong pang-edukasyon - walang proseso ng pag-deploy. Ang mga gumagamit:
1. Mag-fork o mag-clone ng repositoryo
2. Patakbuhin ang mga notebook nang lokal o sa GitHub Codespaces
3. Matuto sa pamamagitan ng pagbabago at pagsubok sa mga halimbawa

## Mga Alituntunin sa Pull Request

### Bago Magpadala

1. **Subukin ang mga pagbabago:**
   - Patakbuhin nang buo ang apektadong mga notebook
   - Siguraduhin na walang error sa pag-execute ng mga cell
   - Tingnan kung ang mga output ay angkop

2. **Pag-update ng dokumentasyon:**
   - I-update ang README.md kung magdadagdag ng bagong konsepto
   - Magdagdag ng mga komento sa mga notebook para sa komplikadong code
   - Siguraduhing naipaliwanag sa mga markdown cell ang layunin

3. **Pagbabago ng mga file:**
   - Iwasang mag-commit ng `.env` files (gamitin ang `.env.example`)
   - Huwag mag-commit ng `venv/` o `__pycache__/` na mga direktoryo
   - Panatilihin ang mga output ng notebook kapag nagpapakita ito ng mga konsepto
   - Alisin ang pansamantalang mga file at backup notebooks (`*-backup.ipynb`)

### Format ng PR Title

Gumamit ng mga deskriptibong pamagat:
- `[Lesson-XX] Magdagdag ng bagong halimbawa para sa <konsepto>`
- `[Fix] Ayusin ang typo sa lesson-XX README`
- `[Update] Pagbutihin ang halimbawa ng code sa lesson-XX`
- `[Docs] I-update ang mga tagubilin sa setup`

### Kinakailangang Mga Suriin

- Dapat magpatakbo ang mga notebook nang walang error
- Dapat malinaw at tumpak ang mga README files
- Sundin ang umiiral na mga pattern ng code sa repositoryo
- Panatilihin ang pagkakapare-pareho sa ibang mga leksiyon

## Karagdagang Mga Tala

### Mga Karaniwang Palusot

1. **Hindi pagtugma ng bersyon ng Python:**
   - Siguraduhing gumagamit ng Python 3.12+ 
   - Maaaring hindi gumana ang ilang mga pakete sa mas lumang mga bersyon
   - Gamitin ang `python3 -m venv` para tahasang tukuyin ang bersyon ng Python

2. **Mga environment variables:**
   - Laging gumawa ng `.env` mula sa `.env.example`
   - Huwag mag-commit ng `.env` file (kasama ito sa `.gitignore`)
   - Mag-sign in gamit ang `az login` para sa keyless Entra ID authentication

3. **Mga tunggalian sa pakete:**
   - Gumamit ng bagong virtual environment
   - Mag-install mula sa `requirements.txt` kaysa sa mga indibidwal na pakete
   - Ang ilang mga notebook ay maaaring mangailangan ng karagdagang mga pakete na nakasaad sa kanilang mga markdown cell

4. **Mga serbisyo ng Azure:**
   - Nangangailangan ng aktibong subscription ang mga Azure AI services
   - Ang ilang mga tampok ay partikular sa rehiyon
   - Siguraduhing sinusuportahan ng iyong Azure OpenAI model deployment ang Responses API

### Landas ng Pagkatuto

Inirerekomendang daloy ng mga leksiyon:
1. **00-course-setup** - Simulan dito para sa setup ng kapaligiran
2. **01-intro-to-ai-agents** - Unawain ang mga pundasyon ng AI agent
3. **02-explore-agentic-frameworks** - Matuto tungkol sa iba't ibang framework
4. **03-agentic-design-patterns** - Mga pangunahing disenyo ng patterns
5. Magpatuloy nang sunud-sunod sa mga numbered lessons

### Pagpili ng Framework

Pumili ng framework base sa iyong mga layunin:
- **Lahat ng leksiyon**: Microsoft Agent Framework (MAF) gamit ang `FoundryChatClient`
- **Mga agent ay nagrerehistro sa server-side** sa Microsoft Foundry Agent Service V2 at makikita sa Foundry portal

### Paghahanap ng Tulong

- Sumali sa [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Suriin ang mga README files ng leksiyon para sa tiyak na mga gabay
- Tingnan ang pangunahing [README.md](./README.md) para sa pangkalahatang-ideya ng kurso
- Tumukoy sa [Course Setup](./00-course-setup/README.md) para sa detalyadong mga tagubilin sa setup

### Pagtutulungan

Ito ay isang bukas na proyektong pang-edukasyon. Malugod ang pagtanggap ng kontribusyon:
- Pagbutihin ang mga halimbawa ng code
- Ayusin ang mga typo o error
- Magdagdag ng mga komentaryo na nagpapalinaw
- Magmungkahi ng mga bagong paksang leksiyon
- Isalin sa karagdagang mga wika

Tingnan ang [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) para sa kasalukuyang mga pangangailangan.

## Konteksto na Natatangi sa Proyekto

### Suporta sa Maramihang Wika

Ang repositoryong ito ay gumagamit ng automated translation system:
- Sinuportahan ang 50+ na mga wika
- Mga pagsasalin ay nasa mga direktoryo na `/translations/<lang-code>/`
- Ang GitHub Actions workflow ang humahawak sa pag-update ng mga pagsasalin
- Ang mga source file ay nasa Ingles sa ugat ng repositoryo

### Istruktura ng Leksiyon

Bawat leksiyon ay sumusunod sa isang pare-parehong pattern:
1. Thumbnail ng video na may link
2. Nakasulat na nilalaman ng leksiyon (README.md)
3. Mga sample ng code sa maraming mga framework
4. Mga layunin sa pag-aaral at mga kinakailangan
5. Karagdagang mga pinagkukunan ng pagkatuto na naka-link

### Pangalan ng Sample ng Code

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Leksiyon 1, MAF Python
- `14-sequential.ipynb` - Leksiyon 14, mga advanced na pattern ng MAF
- `16-python-agent-framework.ipynb` - Leksiyon 16, production customer-support agent
- `17-local-agent-foundry-local.ipynb` - Leksiyon 17, lokal na agent gamit ang Foundry Local + Qwen

### Espesyal na mga Direktoryo

- `translated_images/` - Mga lokal na larawan para sa mga pagsasalin
- `images/` - Orihinal na mga larawan para sa nilalamang Ingles
- `.devcontainer/` - Konfigurasyon ng development container para sa VS Code
- `.github/` - Mga workflow at template ng GitHub Actions

### Mga Dependency

Mga pangunahing pakete mula sa `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Suporta sa Agent-to-Agent protocol
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure authentication (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integration
- `mcp[cli]` - Suporta sa Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->