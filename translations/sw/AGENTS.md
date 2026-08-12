# AGENTS.md

## Muhtasari wa Mradi

Hifadhidata hii ina "Wakala wa AI kwa Waanzilishi" - kozi kamili ya elimu inayofundisha kila kinachohitajika kujenga Wakala wa AI. Kozi ina masomo 18 (yenye nambari 00-18) ikijumuisha misingi, mifumo ya muundo, fremu za kazi, utoaji wa uzalishaji, wakala wa eneo la ndani/kwenye kifaa, na usalama wa wakala wa AI.

**Teknolojia Muhimu:**
- Python 3.12+
- Daftari za Jupyter kwa kujifunza kwa mwingiliano
- Fremu za AI: Microsoft Agent Framework (MAF)
- Huduma za Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Mimarishaji:**
- Muundo wa somo kwa somo (folda 00-15+)
- Kila somo lina: hati ya README, mifano ya msimbo (daftari za Jupyter), na picha
- Usaidia lugha nyingi kupitia mfumo wa utafsiri wa kiotomatiki
- Daftari moja la Python kwa kila somo likitumia Microsoft Agent Framework

## Amri za Kusanidi

### Mahitaji ya Awali
- Python 3.12 au zaidi
- Usajili wa Azure (kwa Microsoft Foundry)
- CLI ya Azure imesanidiwa na kuthibitishwa (`az login`)

### Kusanidi Awali

1. **Nakili au fanyia fork hifadhidata:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # AU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Tengeneza na wezesha mazingira ya Python ya kweli (virtual environment):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Kwenye Windows: venv\Scripts\activate
   ```

3. **Sakinisha vyanzo vinavyotakiwa:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Sanidi mabadiliko ya mazingira:**
   ```bash
   cp .env.example .env
   # Hariri .env na funguo zako za API na vituo vya mwisho
   ```

### Mabadiliko ya Mazingira Yanayohitajika

Kwa **Microsoft Foundry** (Inahitajika):
- `AZURE_AI_PROJECT_ENDPOINT` - Mwangalizi wa mradi wa Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Jina la utekelezaji wa modeli (mfano, gpt-5-mini)

Kwa **Azure AI Search** (Somo 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Mwangalizi wa Azure AI Search
- `AZURE_SEARCH_API_KEY` - Funguo ya API ya Azure AI Search

Uthibitishaji: Endesha `az login` kabla ya kuendesha daftari za kazi (inatumia `AzureCliCredential`).

## Mtiririko wa Maendeleo

### Kuendesha Daftari za Jupyter

Kila somo lina daftari kadhaa za Jupyter kwa fremu za kazi tofauti:

1. **Anzisha Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Nenda kwenye folda ya somo** (mfano, `01-intro-to-ai-agents/code_samples/`)

3. **Fungua na endesha daftari:**
   - `*-python-agent-framework.ipynb` - Kutumia Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Kutumia Microsoft Agent Framework (.NET)

### Kufanya kazi na Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Inahitaji usajili wa Azure
- Inatumia `FoundryChatClient` kwa Agent Service V2 (wakala wanaonekana kwenye lango la Foundry)
- Tayari kwa uzalishaji na ufuatiliaji wa ndani
- Mifano ya faili: `*-python-agent-framework.ipynb`

## Maelekezo ya Kupima

Hii ni hifadhidata ya elimu yenye msimbo wa mfano badala ya msimbo wa uzalishaji wenye vipimo vya moja kwa moja. Ili kuthibitisha usanidi wako na mabadiliko:

### Kupima Kwa Mikono

1. **Pima mazingira ya Python:**
   ```bash
   python --version  # Inapaswa kuwa 3.12 au zaidi
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Pima uendeshaji wa daftari:**
   ```bash
   # Geuza daftari kuwa script na endesha (inamajaribio)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Hakikisha mabadiliko ya mazingira:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Kuendesha Daftari Pamoja Pamoja

Fungua daftari za kazi katika Jupyter na endesha seli moja baada ya nyingine kwa mpangilio. Kila daftari lina vitu vyenyewe na linajumuisha:
- Tamko la kuingiza
- Laden ya usanidi
- Mifano ya utekelezaji wa wakala
- Matokeo yanayotarajiwa katika seli za markdown

### Kupima Haraka Wakala Waliotekelezwa

Kwa masomo ambapo wakala ametekelezwa kama wakala mwenyeji wa Microsoft Foundry (01, 04, 05, 16), hifadhidata hupeleka katalogi za upimaji haraka chini ya `tests/` ambazo zinaendeshwa na mtiririko wa `.github/workflows/smoke-test.yml` kupitia tendo la [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Hizi ni lango la kupita lenye uzito mdogo baada ya utekelezaji (je, wakala anapatikana na anafuata matarajio ya maono ya msingi?), zikikamilisha mchakato wa tathmini katika Masomo 10 na 16. Tazama [tests/README.md](./tests/README.md) kwa muhtasari wa katalogi-kwa-somo-kwa-wakala. Somo la 17 linaendesha kwa ndani na Foundry Local na halina mwangalizi mwenyeji, hivyo linahakikishwa kwa kuendesha daftari lake moja kwa moja.

## Mtindo wa Msimbo

### Kanuni za Python

- **Toleo la Python**: 3.12+
- **Mtindo wa Msimbo**: Fuata kanuni za kawaida za Python PEP 8
- **Daftari**: Tumia seli wazi za markdown kuelezea dhana
- **Kuagiza**: Pangilia kwa maktaba ya kawaida, wa tatu, na wa eneo la ndani

### Kanuni za Daftari za Jupyter

- Jumuisha seli za kuelezea kabla ya seli za msimbo
- Ongeza mifano ya matokeo katika daftari kwa rejea
- Tumia majina ya wazi ya vigezo yanayolingana na dhana za somo
- Weka mpangilio wa kuendesha daftari kwa mstari (seli 1 → 2 → 3...)

### Mpangilio wa Faili

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Kujenga na Utekelezaji

### Kujenga Hati

Hifadhidata hii inatumia Markdown kwa hati:
- Faili za README.md katika kila saraka ya somo
- README.md kuu kwenye mizizi ya hifadhidata
- Mfumo wa utafsiri wa kiotomatiki kupitia Vitendo vya GitHub

### Mtiririko wa CI/CD

Iko katika `.github/workflows/`:

1. **co-op-translator.yml** - Utafsiri wa moja kwa moja kwa lugha 50+
2. **welcome-issue.yml** - Kuikaribisha watengeneza masuala mapya
3. **welcome-pr.yml** - Kuukaribisha washiriki wa maombi ya kuvuta (pull request)

### Utekelezaji

Hii ni hifadhidata ya elimu - hakuna mchakato wa utekelezaji. Watumiaji:
1. Fanyia fork au nakili hifadhidata
2. Endesha daftari kwa eneo la ndani au GitHub Codespaces
3. Jifunze kwa kubadilisha na kujaribu mifano

## Miongozo ya Maombi ya Kuvuta (Pull Request)

### Kabla ya Kutoa

1. **Pima mabadiliko yako:**
   - Endesha vyote vilivyoguswa kabisa
   - Hakikisha seli zote zinafanya kazi bila makosa
   - Kagua matokeo kuwa sahihi

2. **Sasisha hati:**
   - Sasisha README.md ikiwa unaongeza dhana mpya
   - Ongeza maelezo katika daftari kwa msimbo mgumu
   - Hakikisha seli za markdown zinaelezea madhumuni

3. **Mabadiliko ya faili:**
   - Epuka kuweka faili za `.env` (tumia `.env.example`)
   - Usiweka saraka za `venv/` au `__pycache__/`
   - Hifadhi matokeo ya daftari yanayoonyesha dhana
   - Ondoa faili za muda na daftari za akiba (`*-backup.ipynb`)

### Muundo wa Kichwa cha PR

Tumia vichwa vya kueleweka:
- `[Lesson-XX] Ongeza mfano mpya wa <concept>`
- `[Fix] Rekebisha kosa la herufi katika README ya somo-XX`
- `[Update] Boresha mfano wa msimbo katika somo-XX`
- `[Docs] Sasisha maelekezo ya kusanidi`

### Vipimo Vinavyohitajika

- Daftari za kazi ziendeshe bila makosa
- Faili za README ziwe wazi na sahihi
- Fuata mifumo ya msimbo iliyopo katika hifadhidata
- Dumisha mlingano na masomo mengine

## Vidokezo Zaidi

### Makosa Yanayojirudia Mara kwa Mara

1. **Toleo la Python halilingani:**
   - Hakikisha Python 3.12+ inatumika
   - Baadhi ya vifurushi haviwezi kufanya kazi na matoleo ya zamani
   - Tumia `python3 -m venv` kuainisha toleo la Python waziwazi

2. **Mabadiliko ya mazingira:**
   - Daima tengeneza `.env` kutoka kwa `.env.example`
   - Usitoe faili ya `.env` (iko katika `.gitignore`)
   - Jisajili kwa `az login` kwa uthibitishaji wa Entra ID usio na funguo

3. **Migongano ya vifurushi:**
   - Tumia mazingira mapya ya kweli (virtual environment)
   - Sakinisha kutoka `requirements.txt` badala ya vifurushi binafsi
   - Baadhi ya daftari zinaweza kuhitaji vifurushi vya ziada vilivyotajwa katika seli zao za markdown

4. **Huduma za Azure:**
   - Huduma za Azure AI zinahitaji usajili unaoendelea
   - Baadhi ya vipengele ni maalum kwa maeneo fulani
   - Hakikisha utekelezaji wa modeli ya Azure OpenAI unaunga mkono API za Majibu

### Njia ya Kujifunza

Mapendekezo ya mfuatano wa masomo:
1. **00-course-setup** - Anza hapa kwa usanidi wa mazingira
2. **01-intro-to-ai-agents** - Fahamu misingi ya wakala wa AI
3. **02-explore-agentic-frameworks** - Jifunze kuhusu fremu tofauti
4. **03-agentic-design-patterns** - Mifumo ya muundo ya msingi
5. Endelea kupitia masomo yenye namba kwa mpangilio

### Uchaguzi wa Fremu

Chagua fremu kulingana na malengo yako:
- **Masomo yote**: Microsoft Agent Framework (MAF) na `FoundryChatClient`
- **Wakala hujisajili upande wa seva** katika Microsoft Foundry Agent Service V2 na wanaonekana kwenye lango la Foundry

### Kupata Msaada

- Jiunge na [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Kagua faili za README za somo kwa mwongozo maalum
- Angalia [README.md](./README.md) kuu kwa muhtasari wa kozi
- Rejelea [Course Setup](./00-course-setup/README.md) kwa maelekezo ya usanidi ya kina

### Kuchangia

Huu ni mradi wa elimu wazi. Michango inakaribishwa:
- Boreshaji mifano ya msimbo
- Rekebisha makosa ya tahajia au makosa
- Ongeza maoni ya ufafanuzi
- Pendekeza mada mpya za somo
- Tafsiri kwa lugha zaidi

Angalia [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) kwa mahitaji yanayoendelea.

## Muktadha Maalum wa Mradi

### Usaidizi wa Lugha Nyingi

Hifadhidata hii inatumia mfumo wa utafsiri wa kiotomatiki:
- Lugha 50+ zinasaidiwa
- Tafsiri ziko katika saraka `/translations/<lang-code>/`
- Mtiririko wa Vitendo vya GitHub hudhibiti masasisho ya tafsiri
- Faili za asili ziko kwa Kiingereza kwenye mizizi ya hifadhidata

### Muundo wa Somo

Kila somo hufuata muundo wa kawaida:
1. Kipakiti cha video chenye kiungo
2. Maudhui yaliyoandikwa ya somo (README.md)
3. Mifano ya msimbo katika fremu nyingi
4. Malengo ya kujifunza na mahitaji ya awali
5. Rasilimali za ziada za kujifunza zimeunganishwa

### Jina la Mfano wa Msimbo

Muundo: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Somo 1, MAF Python
- `14-sequential.ipynb` - Somo 14, mifumo ya juu ya MAF
- `16-python-agent-framework.ipynb` - Somo 16, wakala wa huduma kwa wateja wa uzalishaji
- `17-local-agent-foundry-local.ipynb` - Somo 17, wakala wa eneo la ndani na Foundry Local + Qwen

### Saraka Maalum

- `translated_images/` - Picha zilizotafsiriwa kwa lugha mbalimbali
- `images/` - Picha za asili za maudhui ya Kiingereza
- `.devcontainer/` - Usanidi wa kontena ya maendeleo ya VS Code
- `.github/` - Vitendo na templeti za Vitendo vya GitHub

### Vitegemezi

Vifurushi muhimu kutoka `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Usaidizi wa itifaki ya Agent-to-Agent
- `azure-ai-inference`, `azure-ai-projects` - Huduma za Azure AI
- `azure-identity` - Uthibitishaji wa Azure (AzureCliCredential)
- `azure-search-documents` - Ujanibishaji wa Azure AI Search
- `mcp[cli]` - Usaidizi wa Itifaki ya Muktadha wa Modeli

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->