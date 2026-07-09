# WAWAKILISHI.md

## Muhtasari wa Mradi

Hifadhi hii ina "Wawakilishi wa AI kwa Waanzilishi" - kozi kamili ya elimu inayo fundisha kila kitu kinachohitajika kujenga Wawakilishi wa AI. Kozi hii ina masomo 18 yanayogusia misingi, mifumo ya muundo, mifumo ya kazi, na utoaji wa wawakilishi wa AI kazini.

**Teknolojia Muhimu:**
- Python 3.12+
- Daftari za Jupyter kwa kujifunza kushirikiana
- Mifumo ya AI: Microsoft Agent Framework (MAF)
- Huduma za Azure AI: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Mhimili wa Mfumo:**
- Muundo wa somo-kujibukua (direktori 00-15+)
- Kila somo lina: nyaraka za README, mifano ya msimbo (daftari za Jupyter), na picha
- Msaada wa lugha nyingi kupitia mfumo wa kutafsiri kiotomatiki
- Daftari la Python moja kwa kila somo likitumia Microsoft Agent Framework

## Amri za Kuanzisha

### Masharti ya Awali
- Python 3.12 au juu zaidi
- Usajili wa Azure (kwa Microsoft Foundry)
- Azure CLI imewekwa na imethibitishwa (`az login`)

### Kuanzisha Awali

1. **Nakili au fanya fork ya hifadhi:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # AU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Tengeneza na wezesha mazingira ya Python virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Kwenye Windows: venv\Scripts\activate
   ```

3. **Sakinisha utegemezi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Weka mabadiliko ya mazingira:**
   ```bash
   cp .env.example .env
   # Hariri .env na funguo zako za API na maeneo ya mwisho
   ```

### Mabadiliko ya Mazingira Yanayohitajika

Kwa **Microsoft Foundry** (Inahitajika):
- `AZURE_AI_PROJECT_ENDPOINT` - mwisho wa mradi wa Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Jina la usambazaji wa mfano (mfano, gpt-4o)

Kwa **Azure AI Search** (Somo 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - mwisho wa Azure AI Search
- `AZURE_SEARCH_API_KEY` - ufunguo wa API wa Azure AI Search

Uthibitisho: Endesha `az login` kabla ya kuendesha daftari (inatumia `AzureCliCredential`).

## Mtiririko wa Maendeleo

### Kuendesha Daftari za Jupyter

Kila somo lina daftari nyingi za Jupyter za mifumo tofauti:

1. **Anzisha Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Elekeza kwa direktori ya somo** (mfano, `01-intro-to-ai-agents/code_samples/`)

3. **Fungua na endesha daftari:**
   - `*-python-agent-framework.ipynb` - Kutumia Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Kutumia Microsoft Agent Framework (.NET)

### Kufanya kazi na Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Inahitaji usajili wa Azure
- Inatumia `FoundryChatClient` kwa Agent Service V2 (mawakala yanaonekana katika lango la Foundry)
- Tayari kwa utengenezaji na mchakato wa ufuatiliaji uliotengenezwa
- Mfano wa faili: `*-python-agent-framework.ipynb`

## Maelekezo ya Upimaji

Hii ni hifadhi ya kielimu yenye mifano ya msimbo badala ya msimbo wa utengenezaji na vipimo vya kiotomatiki. Ili kuthibitisha usanidi na mabadiliko yako:

### Upimaji wa Mikono

1. **Jaribu mazingira ya Python:**
   ```bash
   python --version  # Inapaswa kuwa 3.12 au zaidi
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Jaribu utekelezaji wa daftari:**
   ```bash
   # Geuza daftari kuwa skiripti na uendeshe (hujaribu kuagiza)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Thibitisha mabadiliko ya mazingira:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Kuendesha Daftari Binafsi

Fungua daftari katika Jupyter na tekeleza seli mfululizo. Kila daftari ni huru na linajumuisha:
- Kauli za kuingiza
- Kupakia usanidi
- Mifano ya utekelezaji wa wakala
- Matokeo yanayotarajiwa katika seli za markdown

## Mtindo wa Msimbo

### Kanuni za Python

- **Toleo la Python**: 3.12+
- **Mtindo wa Msimbo**: Fuata kanuni za kawaida za PEP 8 za Python
- **Daftari**: Tumia seli za markdown zilizo wazi kuelezea dhana
- **Uingiliaji**: Pangilia kwa maktaba za kawaida, wa tatu, na wenyeji

### Kanuni za Daftari za Jupyter

- Jumuisha seli za markdown za maelezo kabla ya seli za msimbo
- Ongeza mifano ya matokeo katika daftari kwa rejea
- Tumia majina ya mabadiliko yaliyoeleweka yanayolingana na dhana za somo
- Hifadhi mtiririko wa utekelezaji wa daftari kuwa wa mstari (seli 1 → 2 → 3...)

### Uandaaji wa Faili

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Ujenzi na Utekelezaji

### Kujenga Nyaraka

Hifadhi hii inatumia Markdown kwa nyaraka:
- Faili za README.md katika kila folda ya somo
- README.md kuu katika mzizi wa hifadhi
- Mfumo wa kutafsiri kiotomatiki kupitia GitHub Actions

### Mlolongo wa CI/CD

Upatikanaji katika `.github/workflows/`:

1. **co-op-translator.yml** - Kutafsiri moja kwa moja kwa lugha 50+
2. **welcome-issue.yml** - Kuwakaribisha watoa masuala mapya
3. **welcome-pr.yml** - Kuwakaribisha watengenezaji wa ombi la pull

### Utekelezaji

Hii ni hifadhi ya kielimu - hakuna mchakato wa utekelezaji. Watumiaji:
1. Fanya fork au nakili hifadhi
2. Endesha daftari kwa ndani au katika GitHub Codespaces
3. Jifunze kwa kubadilisha na kujaribu mifano

## Miongozo ya Maombi ya Pull

### Kabla ya Kuwasilisha

1. **Jaribu mabadiliko yako:**
   - Endesha daftari zote zilizoathirika kikamilifu
   - Thibitisha seli zote zinaendeshwa bila makosa
   - Angalia matokeo ni sahihi

2. **Mabadiliko ya nyaraka:**
   - Sasisha README.md ikiwa unaongeza dhana mpya
   - Ongeza maelezo kwenye daftari kwa msimbo tata
   - Hakikisha seli za markdown zinaelezea kusudi

3. **Mabadiliko ya faili:**
   - Epuka kuingiza faili `.env` (tumia `.env.example`)
   - Usiongeze venv/ au __pycache__/ madirektori
   - Hifadhi matokeo ya daftari endapo yanathibitisha dhana
   - Ondoa faili za muda na daftari za hifadhi (`*-backup.ipynb`)

### Muundo wa Kichwa cha PR

Tumia vichwa vinavyoelezea:
- `[Somo-XX] Ongeza mfano mpya kwa <dhana>`
- `[Fix] Rekebisha makosa ya tahajia katika README ya somo-XX`
- `[Update] Boresha mfano wa msimbo katika somo-XX`
- `[Docs] Sasisha maelekezo ya usanidi`

### Vipimo Vinavyohitajika

- Daftari zinapaswa kuendeshwa bila makosa
- Faili za README ziwe wazi na sahihi
- Fuata mifumo ya msimbo iliyopo katika hifadhi
- Dhamini ulinganifu wa masomo mengine

## Vidokezo Zaidi

### Changamoto za Kawaida

1. **Toleo la Python halilingani:**
   - Hakikisha unatumia Python 3.12 au juu
   - Baadhi ya pakiti huenda zisifanye kazi na matoleo ya zamani
   - Tumia `python3 -m venv` kuainisha toleo la Python wazi

2. **Mabadiliko ya mazingira:**
   - Daima tengeneza `.env` kutoka `.env.example`
   - Usitingishe faili `.env` (iko `.gitignore`)
   - Ingia na `az login` kwa uthibitisho wa Entra ID bila funguo

3. **Migongano ya pakiti:**
   - Tumia mazingira mapya ya virtual
   - Sakinisha kutoka `requirements.txt` badala ya pakiti binafsi
   - Baadhi ya daftari huenda zikahitaji pakiti za ziada zilizotajwa katika seli za markdown

4. **Huduma za Azure:**
   - Huduma za Azure AI zinahitaji usajili hai
   - Baadhi ya vipengele ni maalum kwa maeneo
   - Hakikisha usambazaji wa mfano wa Azure OpenAI unaunga mkono API ya Majibu

### Njia ya Kujifunza

Mapendekezo ya msururu wa masomo:
1. **00-course-setup** - Anza hapa kwa usanidi wa mazingira
2. **01-intro-to-ai-agents** - Elewa misingi ya wakala wa AI
3. **02-explore-agentic-frameworks** - Jifunze kuhusu mifumo tofauti
4. **03-agentic-design-patterns** - Mifumo msingi ya muundo
5. Endelea kupitia masomo yaliyo nambariwa kwa mfuatano

### Uteuzi wa Mfumo

Chagua mfumo kulingana na malengo yako:
- **Masomo yote**: Microsoft Agent Framework (MAF) na `FoundryChatClient`
- **Wakala hujisajili upande wa seva** katika Microsoft Foundry Agent Service V2 na wanaonekana katika lango la Foundry

### Kupata Msaada

- Jiunge na [Jumuiya ya Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)
- Soma faili za README za somo kwa mwongozo maalum
- Angalia [README.md](./README.md) kuu kwa muhtasari wa kozi
- Rejelea [Usanidi wa Kozi](./00-course-setup/README.md) kwa maelekezo ya kina ya usanidi

### Kuchangia

Hii ni mradi wa kitaaluma wa wazi. Michango inakaribishwa:
- Boresha mifano ya msimbo
- Rekebisha makosa au tahajia
- Ongeza maelezo ya ufafanuzi
- Pendekeza mada mpya za somo
- Tafsiri kwa lugha zaidi

Angalia [Masuala ya GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) kwa mahitaji ya sasa.

## Muktadha Maalum wa Mradi

### Msaada wa Lugha Mbalimbali

Hifadhi hii inatumia mfumo wa kutafsiri kiotomatiki:
- Lugha 50+ zinazotumika
- Tafsiri katika ` /translations/<lang-code>/ ` direktori
- Mtiririko wa GitHub Actions huendesha masasisho ya tafsiri
- Faili za chanzo ziko kwa Kiingereza katika mzizi wa hifadhi

### Muundo wa Somo

Kila somo hufuata muundo thabiti:
1. Thumbnail ya video yenye kiungo
2. Maandishi ya somo (README.md)
3. Mifano ya msimbo katika mifumo mingi
4. Malengo ya kujifunza na masharti ya awali
5. Rasilimali za ziada za kujifunza zenye viungo

### Jina la Mfano wa Msimbo

Muundo: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Somo 1, MAF Python
- `14-sequential.ipynb` - Somo 14, mifumo ya juu ya MAF

### Direkta Maalum

- `translated_images/` - Picha zilizotafsiriwa kwa lugha mbalimbali
- `images/` - Picha za asili kwa maudhui ya Kiingereza
- `.devcontainer/` - Usanidi wa kontena ya maendeleo ya VS Code
- `.github/` - Mfantishaji wa GitHub Actions na mifano

### Utegemezi

Pakiti kuu kutoka `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Msaada wa itifaki ya Mawakala kwa Mawakala
- `azure-ai-inference`, `azure-ai-projects` - Huduma za Azure AI
- `azure-identity` - Uthibitisho wa Azure (AzureCliCredential)
- `azure-search-documents` - Muunganisho wa Azure AI Search
- `mcp[cli]` - Msaada wa Itifaki ya Muktadha wa Mfano

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->