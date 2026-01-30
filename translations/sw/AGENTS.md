# AGENTS.md

## Muhtasari wa Mradi

Hifadhi hii ina "Wakala wa AI kwa Kompyuta" - kozi ya kina ya elimu inayofundisha kila kitu kinachohitajika kujenga Wakala wa AI. Kozi hii ina masomo zaidi ya 15 yanayofunika misingi, mifumo ya muundo, mifumo ya kazi, na usambazaji wa wakala wa AI katika uzalishaji.

**Teknolojia Muhimu:**
- Python 3.12+
- Jupyter Notebooks kwa kujifunza kwa maingiliano
- Mifumo ya AI: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Huduma za Azure AI: Azure AI Foundry, Azure AI Agent Service
- Soko la Miundo la GitHub (kiwango cha bure kinapatikana)

**Muundo:**
- Muundo wa msingi wa masomo (00-15+ saraka)
- Kila somo lina: Nyaraka za README, sampuli za msimbo (Jupyter notebooks), na picha
- Msaada wa lugha nyingi kupitia mfumo wa tafsiri otomatiki
- Chaguo nyingi za mifumo kwa kila somo (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Amri za Usanidi

### Mahitaji ya Awali
- Python 3.12 au zaidi
- Akaunti ya GitHub (kwa Miundo ya GitHub - kiwango cha bure)
- Usajili wa Azure (hiari, kwa huduma za Azure AI)

### Usanidi wa Awali

1. **Clone au fork hifadhi:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Unda na wezesha mazingira ya Python virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Sakinisha utegemezi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Sanidi vigezo vya mazingira:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```


### Vigezo vya Mazingira Vinavyohitajika

Kwa **Miundo ya GitHub (Bure)**:
- `GITHUB_TOKEN` - Token ya ufikiaji wa kibinafsi kutoka GitHub

Kwa **Huduma za Azure AI** (hiari):
- `PROJECT_ENDPOINT` - Endpoint ya mradi wa Azure AI Foundry
- `AZURE_OPENAI_API_KEY` - Funguo ya API ya Azure OpenAI
- `AZURE_OPENAI_ENDPOINT` - URL ya endpoint ya Azure OpenAI
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Jina la usambazaji kwa mfano wa mazungumzo
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Jina la usambazaji kwa embeddings
- Usanidi wa ziada wa Azure kama ulivyoonyeshwa kwenye `.env.example`

## Mtiririko wa Kazi wa Maendeleo

### Kuendesha Jupyter Notebooks

Kila somo lina Jupyter notebooks nyingi kwa mifumo tofauti:

1. **Anzisha Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Nenda kwenye saraka ya somo** (mfano, `01-intro-to-ai-agents/code_samples/`)

3. **Fungua na endesha notebooks:**
   - `*-semantic-kernel.ipynb` - Kutumia mfumo wa Semantic Kernel
   - `*-autogen.ipynb` - Kutumia mfumo wa AutoGen
   - `*-python-agent-framework.ipynb` - Kutumia Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Kutumia Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Kutumia Azure AI Agent Service

### Kufanya Kazi na Mifumo Tofauti

**Semantic Kernel + Miundo ya GitHub:**
- Kiwango cha bure kinapatikana na akaunti ya GitHub
- Nzuri kwa kujifunza na majaribio
- Muundo wa faili: `*-semantic-kernel*.ipynb`

**AutoGen + Miundo ya GitHub:**
- Kiwango cha bure kinapatikana na akaunti ya GitHub
- Uwezo wa uratibu wa wakala wengi
- Muundo wa faili: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Mfumo wa hivi karibuni kutoka Microsoft
- Unapatikana kwa Python na .NET
- Muundo wa faili: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Inahitaji usajili wa Azure
- Vipengele tayari kwa uzalishaji
- Muundo wa faili: `*-azureaiagent.ipynb`

## Maelekezo ya Kupima

Hii ni hifadhi ya elimu yenye msimbo wa mfano badala ya msimbo wa uzalishaji wenye majaribio otomatiki. Ili kuthibitisha usanidi wako na mabadiliko:

### Upimaji wa Mwongozo

1. **Pima mazingira ya Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Pima utekelezaji wa notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Thibitisha vigezo vya mazingira:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Kuendesha Notebooks za Kipekee

Fungua notebooks kwenye Jupyter na tekeleza seli kwa mpangilio. Kila notebook ni ya kujitegemea na inajumuisha:
- Amri za kuingiza
- Upakiaji wa usanidi
- Utekelezaji wa wakala wa mfano
- Matokeo yanayotarajiwa kwenye seli za markdown

## Mtindo wa Msimbo

### Miongozo ya Python

- **Toleo la Python**: 3.12+
- **Mtindo wa Msimbo**: Fuata miongozo ya kawaida ya Python PEP 8
- **Notebooks**: Tumia seli za markdown wazi kuelezea dhana
- **Amri za kuingiza**: Panga kwa maktaba ya kawaida, ya watu wa tatu, na ya ndani

### Miongozo ya Jupyter Notebook

- Jumuisha seli za markdown zenye maelezo kabla ya seli za msimbo
- Ongeza mifano ya matokeo kwenye notebooks kwa marejeleo
- Tumia majina ya vigezo wazi yanayolingana na dhana za somo
- Weka mpangilio wa utekelezaji wa notebook kuwa wa mstari (seli 1 → 2 → 3...)

### Mpangilio wa Faili

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


## Ujenzi na Usambazaji

### Kujenga Nyaraka

Hifadhi hii inatumia Markdown kwa nyaraka:
- Faili za README.md kwenye kila folda ya somo
- README.md kuu kwenye mzizi wa hifadhi
- Mfumo wa tafsiri otomatiki kupitia GitHub Actions

### Mkondo wa CI/CD

Ipo kwenye `.github/workflows/`:

1. **co-op-translator.yml** - Tafsiri otomatiki kwa lugha zaidi ya 50
2. **welcome-issue.yml** - Karibu kwa waumbaji wa masuala mapya
3. **welcome-pr.yml** - Karibu kwa wachangiaji wa maombi ya kuvuta mapya

### Usambazaji

Hii ni hifadhi ya elimu - hakuna mchakato wa usambazaji. Watumiaji:
1. Fork au clone hifadhi
2. Endesha notebooks kwa ndani au kwenye GitHub Codespaces
3. Jifunze kwa kurekebisha na kujaribu mifano

## Miongozo ya Maombi ya Kuvuta (Pull Request)

### Kabla ya Kuwasilisha

1. **Pima mabadiliko yako:**
   - Endesha notebooks zilizoathiriwa kikamilifu
   - Thibitisha seli zote zinafanya kazi bila makosa
   - Angalia kwamba matokeo ni sahihi

2. **Sasisho za nyaraka:**
   - Sasisha README.md ikiwa unaongeza dhana mpya
   - Ongeza maoni kwenye notebooks kwa msimbo mgumu
   - Hakikisha seli za markdown zinaelezea kusudi

3. **Mabadiliko ya faili:**
   - Epuka kuwasilisha faili za `.env` (tumia `.env.example`)
   - Usisambaze saraka za `venv/` au `__pycache__/`
   - Weka matokeo ya notebook wakati yanaonyesha dhana
   - Ondoa faili za muda na notebooks za hifadhi nakala (`*-backup.ipynb`)

### Muundo wa Kichwa cha PR

Tumia vichwa vya kuelezea:
- `[Lesson-XX] Ongeza mfano mpya kwa <dhana>`
- `[Fix] Rekebisha typo kwenye README ya somo-XX`
- `[Update] Boresha sampuli ya msimbo kwenye somo-XX`
- `[Docs] Sasisha maelekezo ya usanidi`

### Ukaguzi Unaohitajika

- Notebooks zinapaswa kutekelezwa bila makosa
- Faili za README zinapaswa kuwa wazi na sahihi
- Fuata mifumo ya msimbo iliyopo kwenye hifadhi
- Dumisha uthabiti na masomo mengine

## Vidokezo vya Ziada

### Changamoto za Kawaida

1. **Toleo la Python lisilolingana:**
   - Hakikisha Python 3.12+ inatumika
   - Baadhi ya pakiti zinaweza kutoendana na matoleo ya zamani
   - Tumia `python3 -m venv` kubainisha toleo la Python waziwazi

2. **Vigezo vya mazingira:**
   - Daima unda `.env` kutoka `.env.example`
   - Usisambaze faili ya `.env` (ipo kwenye `.gitignore`)
   - Token ya GitHub inahitaji ruhusa sahihi

3. **Migongano ya pakiti:**
   - Tumia mazingira safi ya virtual
   - Sakinisha kutoka `requirements.txt` badala ya pakiti za kibinafsi
   - Baadhi ya notebooks zinaweza kuhitaji pakiti za ziada zilizotajwa kwenye seli za markdown

4. **Huduma za Azure:**
   - Huduma za Azure AI zinahitaji usajili hai
   - Baadhi ya vipengele ni maalum kwa mikoa
   - Vikwazo vya kiwango cha bure vinatumika kwa Miundo ya GitHub

### Njia ya Kujifunza

Mpangilio unaopendekezwa kupitia masomo:
1. **00-course-setup** - Anza hapa kwa usanidi wa mazingira
2. **01-intro-to-ai-agents** - Elewa misingi ya wakala wa AI
3. **02-explore-agentic-frameworks** - Jifunze kuhusu mifumo tofauti
4. **03-agentic-design-patterns** - Mifumo ya muundo wa msingi
5. Endelea kupitia masomo yaliyopangwa kwa namba mfululizo

### Uchaguzi wa Mfumo

Chagua mfumo kulingana na malengo yako:
- **Kujifunza/Kujaribu**: Semantic Kernel + Miundo ya GitHub (bure)
- **Mifumo ya wakala wengi**: AutoGen
- **Vipengele vya hivi karibuni**: Microsoft Agent Framework (MAF)
- **Usambazaji wa uzalishaji**: Azure AI Agent Service

### Kupata Msaada

- Jiunge na [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Tathmini faili za README za somo kwa mwongozo maalum
- Angalia [README.md kuu](./README.md) kwa muhtasari wa kozi
- Rejelea [Usanidi wa Kozi](./00-course-setup/README.md) kwa maelekezo ya kina ya usanidi

### Kuchangia

Huu ni mradi wa elimu wazi. Mchango unakaribishwa:
- Boresha mifano ya msimbo
- Rekebisha typos au makosa
- Ongeza maoni ya kufafanua
- Pendekeza mada mpya za somo
- Tafsiri kwa lugha za ziada

Angalia [Masuala ya GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) kwa mahitaji ya sasa.

## Muktadha Maalum wa Mradi

### Msaada wa Lugha Nyingi

Hifadhi hii inatumia mfumo wa tafsiri otomatiki:
- Lugha zaidi ya 50 zinasaidiwa
- Tafsiri zipo kwenye saraka za `/translations/<lang-code>/`
- Mkondo wa kazi wa GitHub Actions hushughulikia sasisho za tafsiri
- Faili za chanzo zipo kwa Kiingereza kwenye mzizi wa hifadhi

### Muundo wa Somo

Kila somo linafuata muundo thabiti:
1. Picha ya video na kiungo
2. Maudhui ya somo yaliyoandikwa (README.md)
3. Sampuli za msimbo katika mifumo mingi
4. Malengo ya kujifunza na mahitaji ya awali
5. Rasilimali za ziada za kujifunza zilizounganishwa

### Muundo wa Jina la Sampuli ya Msimbo

Muundo: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Somo la 4, Semantic Kernel
- `07-autogen.ipynb` - Somo la 7, AutoGen
- `14-python-agent-framework.ipynb` - Somo la 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Somo la 14, MAF .NET

### Saraka Maalum

- `translated_images/` - Picha zilizotafsiriwa kwa tafsiri
- `images/` - Picha asili kwa maudhui ya Kiingereza
- `.devcontainer/` - Usanidi wa kontena la maendeleo la VS Code
- `.github/` - Mkondo wa kazi wa GitHub Actions na templeti

### Utegemezi

Pakiti muhimu kutoka `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - Mfumo wa AutoGen
- `semantic-kernel` - Mfumo wa Semantic Kernel
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Huduma za Azure AI
- `azure-search-documents` - Muunganisho wa Azure AI Search
- `chromadb` - Hifadhidata ya vector kwa mifano ya RAG
- `chainlit` - Mfumo wa UI wa mazungumzo
- `browser_use` - Uendeshaji wa kivinjari kwa mawakala
- `mcp[cli]` - Msaada wa Model Context Protocol
- `mem0ai` - Usimamizi wa kumbukumbu kwa mawakala

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.