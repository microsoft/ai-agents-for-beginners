# AGENTS.md

## Muhtasari wa Mradi

Hifadhi hii ina "Wakaguzi wa AI kwa Waanzilishi" - kozi ya elimu kamili inayofundisha yote yanayohitajika kujenga Wakaguzi wa AI. Kozi ina somo 15+ zinazohusu misingi, mifumo ya muundo, mfumo, na utoaji wa uzalishaji wa wakaguzi wa AI.

**Teknolojia Muhimu:**
- Python 3.12+
- Daftari za Jupyter kwa kujifunza kwa ushirikiano
- Mifumo ya AI: Mfumo wa Wakala wa Microsoft (MAF)
- Huduma za Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Mimeloleshaji:**
- Muundo wa somo (directories 00-15+)
- Kila somo lina: nyaraka README, mifano ya nambari (daftari za Jupyter), na picha
- Msaada wa lugha nyingi kupitia mfumo wa utafsiri wa moja kwa moja
- Daftari moja la Python kwa kila somo likitumia Mfumo wa Wakala wa Microsoft

## Amri za Kusanidi

### Sharti la Awali
- Python 3.12 au ya juu
- Usajili wa Azure (kwa Azure AI Foundry)
- Azure CLI imesakinishwa na kuthibitishwa (`az login`)

### Kusanidi Mwanzo

1. **Kokotoa au fork hifadhi:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # AU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Unda na wezesha mazingira ya virtual ya Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Kwenye Windows: venv\Scripts\activate
   ```

3. **Sakinisha mahitaji:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Weka vigezo vya mazingira:**
   ```bash
   cp .env.example .env
   # Hariri .env na funguo zako za API na maeneo ya mwisho
   ```

### Vigezo Vinavyohitajika vya Mazingira

Kwa **Azure AI Foundry** (Inahitajika):
- `AZURE_AI_PROJECT_ENDPOINT` - anuani ya mradi wa Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - jina la utoaji wa mfano (mfano, gpt-4o)

Kwa **Azure AI Search** (Somo 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - anuani ya Azure AI Search
- `AZURE_SEARCH_API_KEY` - funguo ya API ya Azure AI Search

Uthibitishaji: Endesha `az login` kabla ya kuendesha daftari (inatumia `AzureCliCredential`).

## Mtiririko wa Maendeleo

### Kuendesha Daftari za Jupyter

Kila somo lina daftari nyingi za Jupyter kwa mifumo tofauti:

1. **Anzisha Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Nenda kwenye directory ya somo** (mfano, `01-intro-to-ai-agents/code_samples/`)

3. **Fungua na endesha daftari:**
   - `*-python-agent-framework.ipynb` - Kutumia Mfumo wa Wakala wa Microsoft (Python)
   - `*-dotnet-agent-framework.ipynb` - Kutumia Mfumo wa Wakala wa Microsoft (.NET)

### Kufanya kazi na Mfumo wa Wakala wa Microsoft

**Mfumo wa Wakala wa Microsoft + Azure AI Foundry:**
- Inahitaji usajili wa Azure
- Inatumia `AzureAIProjectAgentProvider` kwa Huduma ya Wakala V2 (wakaguzi wanaoonekana kwenye mlango wa Foundry)
- Tayari kwa uzalishaji na ufuatiliaji uliojengwa
- Muundo wa faili: `*-python-agent-framework.ipynb`

## Maelekezo ya Upimaji

Hii ni hifadhi ya elimu yenye mifano ya nambari badala ya nambari ya uzalishaji yenye majaribio ya moja kwa moja. Kuangalia usanidi na mabadiliko yako:

### Upimaji wa Mikono

1. **Jaribu mazingira ya Python:**
   ```bash
   python --version  # Inapaswa kuwa 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Jaribu utekelezaji wa daftari:**
   ```bash
   # Geuza daftari kuwa skripti na uendeshe (inajaribu kuingiza)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Hakikisha vigezo vya mazingira:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Kuendesha Daftari Binafsi

Fungua daftari za Jupyter na endesha seli kwa mpangilio. Kila daftari lina vitu vya ndani na linajumuisha:
- Matamko ya kuingiza
- Kupakia usanidi
- Mifano ya utekelezaji wa wakala
- Matokeo yanayotarajiwa kwenye seli za markdown

## Mtindo wa Nambari

### Kanuni za Python

- **Toleo la Python**: 3.12+
- **Mtindo wa nambari**: Fuata kanuni za kawaida za PEP 8 za Python
- **Daftari**: Tumia seli za markdown zilizo wazi kuelezea dhana
- **Kuingiza**: Pangilia kwa maktaba za kawaida, wa tatu, na za ndani

### Kanuni za Daftari la Jupyter

- Jumuisha seli za markdown zenye maelezo kabla ya seli za nambari
- Ongeza mifano ya matokeo kwenye daftari kwa marejeleo
- Tumia majina ya vigezo wazi yanayoendana na dhana za somo
- Weka mpangilio wa utekelezaji wa daftari kwa mstari (seli 1 → 2 → 3...)

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

## Ujenzi na Utoaji

### Kujenga Nyaraka

Hifadhi hii inatumia Markdown kwa nyaraka:
- Faili za README.md katika kila folda ya somo
- README.md kuu kwenye mzizi wa hifadhi
- Mfumo wa utafsiri wa moja kwa moja kupitia GitHub Actions

### Mtaalamu wa CI/CD

Iko katika `.github/workflows/`:

1. **co-op-translator.yml** - Utafsiri wa moja kwa moja kwa lugha 50+
2. **welcome-issue.yml** - Karibisha waandaaji wa masuala mapya
3. **welcome-pr.yml** - Karibisha wafanyakazi wa maombi ya mchoraji

### Utoaji

Hii ni hifadhi ya elimu - hakuna mchakato wa utoaji. Watumiaji:
1. Fork au kokotoa hifadhi
2. Endesha daftari kwa karibu au katika GitHub Codespaces
3. Jifunze kwa kubadilisha na kujaribu mifano

## Mwongozo wa Maombi ya Mchoraji

### Kabla ya Kuwasilisha

1. **Jaribu mabadiliko yako:**
   - Endesha daftari zilizoathirika kwa ukamilifu
   - Hakikisha seli zote zinafanya kazi bila makosa
   - Angalia kuwa matokeo ni sahihi

2. **Sasisha nyaraka:**
   - Sasisha README.md ikiwa unaongeza dhana mpya
   - Ongeza maelezo katika daftari kwa nambari ngumu
   - Hakikisha seli za markdown zinaelezea madhumuni

3. **Mabadiliko ya faili:**
   - Epuka kujumuisha faili `.env` (tumia `.env.example`)
   - Usijumuishe direktorii `venv/` au `__pycache__/`
   - Weka matokeo ya daftari yanayoonyesha dhana
   - Ondoa faili za muda na daftari za nakala za akiba (`*-backup.ipynb`)

### Muundo wa Kichwa cha PR

Tumia vichwa vinaelezea:
- `[Lesson-XX] Ongeza mfano mpya kwa <concept>`
- `[Fix] Rekebisha makosa ya tahajia kwenye README ya somo-XX`
- `[Update] Boresha mfano wa nambari katika somo-XX`
- `[Docs] Sasisha maelekezo ya kusanidi`

### Ukaguzi Unaohitajika

- Daftari ziendeshe bila makosa
- Faili za README ziwe wazi na sahihi
- Fuata mifumo ya nambari iliyopo katika hifadhi
- Dumu na somo zingine

## Vidokezo Zaidi

### Mambo ya Kuepuka

1. **Toleo la Python halilingani:**
   - Hakikisha unapitia Python 3.12+
   - Baadhi ya vifurushi havifanyi kazi kwa matoleo ya zamani
   - Tumia `python3 -m venv` kubainisha toleo la Python wazi

2. **Vigezo vya mazingira:**
   - Daima tengeneza `.env` kutoka `.env.example`
   - Usijumuishe faili `.env` (iko `.gitignore`)
   - Token ya GitHub inahitaji ruhusa sahihi

3. **Migogoro ya vifurushi:**
   - Tumia mazingira mapya ya virtual
   - Sakinisha kutoka `requirements.txt` badala ya vifurushi binafsi
   - Baadhi ya daftari yanaweza kuhitaji vifurushi vya ziada vinavyoelezwa katika seli za markdown

4. **Huduma za Azure:**
   - Huduma za Azure AI zinahitaji usajili hai
   - Baadhi ya vipengele vina eneo maalum
   - Mipaka ya tier ya bure inahusiana na GitHub Models

### Njia ya Kujifunza

Kupitia kwa mapendekezo ya masomo:
1. **00-course-setup** - Anza hapa kwa usanidi wa mazingira
2. **01-intro-to-ai-agents** - Elewa misingi ya wakala wa AI
3. **02-explore-agentic-frameworks** - Jifunze kuhusu mifumo tofauti
4. **03-agentic-design-patterns** - Mifumo ya msingi ya muundo
5. Endelea kupitia somo zilizo nambari moja baada ya nyingine

### Uchaguzi wa Mfumo

Chagua mfumo kulingana na malengo yako:
- **Masomo yote**: Mfumo wa Wakala wa Microsoft (MAF) na `AzureAIProjectAgentProvider`
- **Wakaguzi wanajiandikisha upande wa seva** katika Huduma ya Azure AI Foundry Agent V2 na wanavyoonekana kwenye mlango wa Foundry

### Kupata Msaada

- Jiunge na [Jamii ya Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)
- Pitia faili za README za somo kwa mwongozo maalum
- Angalia [README.md](./README.md) kuu kwa muhtasari wa kozi
- Rejelea [Kusanidi Kozi](./00-course-setup/README.md) kwa maelekezo kamili

### Kuchangia

Hii ni mradi wa elimu ulio wazi. Michango inakaribishwa:
- Boresha mifano ya nambari
- Rekebisha michache au makosa
- Ongeza maelezo ya ufafanuzi
- Pendekeza mada mpya za somo
- Tafsiri kwa lugha za ziada

Angalia [Masuala ya GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) kwa mahitaji ya sasa.

## Muktadha wa Mradi

### Msaada wa Lugha Nyingi

Hifadhi hii inatumia mfumo wa utafsiri wa moja kwa moja:
- Lugha 50+ zinasaidiwa
- Tafsiri ziko katika `/translations/<lang-code>/` directories
- Mchakato wa GitHub Actions unasimamia masasisho ya utafsiri
- Faili za chanzo ziko kwa Kiingereza katika mzizi wa hifadhi

### Muundo wa Somo

Kila somo hufuata mtindo thabiti:
1. Picha ya video na kiungo
2. Maandishi ya somo (README.md)
3. Mifano ya nambari katika mifumo mingi
4. Malengo ya kujifunza na vigezo vya awali
5. Rasilimali za ziada za kujifunza zilizo na viungo

### Jina la Mfano wa Nambari

Fomati: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Somo 1, MAF Python
- `14-sequential.ipynb` - Somo 14, mifumo ya juu ya MAF

### Directories Maalum

- `translated_images/` - Picha zilizotafsiriwa kwa tafsiri
- `images/` - Picha asilia za maudhui ya Kiingereza
- `.devcontainer/` - Usanidi wa kontena ya maendeleo wa VS Code
- `.github/` - Mifumo ya kazi za GitHub Actions na templates

### Vitegemezi

Vifurushi muhimu kutoka `requirements.txt`:
- `agent-framework` - Mfumo wa Wakala wa Microsoft
- `a2a-sdk` - Msaada wa itifaki ya Wakala kwa Wakala
- `azure-ai-inference`, `azure-ai-projects` - Huduma za Azure AI
- `azure-identity` - Uthibitishaji wa Azure (AzureCliCredential)
- `azure-search-documents` - Muungano wa Azure AI Search
- `mcp[cli]` - Msaada wa Itifaki ya Muktadha wa Mfano

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiarifu cha Kukataa**:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Wakati tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upotovu wa maana. Nyaraka ya asili kwa lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha kuaminika. Kwa taarifa muhimu, tafsiri ya mtaalamu wa binadamu inashauriwa. Hatuna dhamana kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->