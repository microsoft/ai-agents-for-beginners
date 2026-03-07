# AGENTS.md

## Muhtasari wa Mradi

Hifadhi hii ina "Maajenti wa AI kwa Waanzilishi" - kozi ya kuelewa kwa kina inayofundisha kila kitu kinachohitajika kujenga Maajenti wa AI. Kozi ina masomo 15+ yanayojumuisha misingi, mifumo ya kubuni, fremu za kazi, na uzalishaji wa maajenti wa AI.

**Teknolojia Muhimu:**
- Python 3.12+
- Daftari za Jupyter kwa kujifunza kwa ushirikiano
- Fremu za AI: Microsoft Agent Framework (MAF)
- Huduma za Azure AI: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Majaribio ya Usanifu:**
- Muundo wa msingi wa masomo (folda 00-15+)
- Kila somo lina: kumbukumbu za README, sampuli za nambari (daftari za Jupyter), na picha
- Msaada wa lugha nyingi kupitia mfumo wa utafsiri otomatiki
- Daftari moja la Python kwa kila somo likitumia Microsoft Agent Framework

## Amri za Kuandaa Mazingira

### Masharti ya Kabla

- Python 3.12 au zaidi
- Usajili wa Azure (kwa Azure AI Foundry)
- Azure CLI imewekwa na kuthibitishwa (`az login`)

### Kuanzisha Mwanzo

1. **Kokotoa au toa nakala ya hifadhi:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # AU
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Tengeneza na uanzishe mazingira ya Python ya mtando:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Kwenye Windows: venv\Scripts\activate
   ```

3. **Sakinisha utegemezi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Sanidi vigezo vya mazingira:**
   ```bash
   cp .env.example .env
   # Hariri .env kwa funguo zako za API na vyanzo vya data
   ```

### Vigezo Vinavyohitajika vya Mazingira

Kwa **Azure AI Foundry** (Inahitajika):
- `AZURE_AI_PROJECT_ENDPOINT` - anuani ya mradi wa Azure AI Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - jina la usambazaji wa mfano (mfano, gpt-4o)

Kwa **Azure AI Search** (Somo 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - anuani ya huduma ya Azure AI Search
- `AZURE_SEARCH_API_KEY` - ufunguo wa API wa Azure AI Search

Uthibitishaji: Endesha `az login` kabla ya kuendesha daftari (inatumia `AzureCliCredential`).

## Mtiririko wa Maendeleo

### Kuendesha Daftari za Jupyter

Kila somo lina daftari nyingi za Jupyter kwa fremu tofauti:

1. **Anzisha Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Elekea kwenye folda ya somo** (mfano, `01-intro-to-ai-agents/code_samples/`)

3. **Fungua na endesha daftari:**
   - `*-python-agent-framework.ipynb` - Kutumia Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Kutumia Microsoft Agent Framework (.NET)

### Kufanya Kazi na Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Inahitaji usajili wa Azure
- Inatumia `AzureAIProjectAgentProvider` kwa Agent Service V2 (maajenti yanaonekana kwenye lango la Foundry)
- Tayari kwa uzalishaji na ufuatiliaji wa ndani
- Mfano wa faili: `*-python-agent-framework.ipynb`

## Maelekezo ya Kujaribu

Hii ni hifadhi ya kielimu na nambari za mfano badala ya nambari ya uzalishaji yenye vipimo vya moja kwa moja. Ili kuthibitisha usanidi wako na mabadiliko:

### Kujaribu Kwa Mkono

1. **Jaribu mazingira ya Python:**
   ```bash
   python --version  # Inapaswa kuwa 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Jaribu utekelezaji wa daftari:**
   ```bash
   # Geuza daftari kuwa skripti na uendeshe (inapima uingizaji)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Thibitisha vigezo vya mazingira:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Kuendesha Daftari Binafsi

Fungua daftari katika Jupyter na endesha seli moja baada ya nyingine. Kila daftari lina vitu vyote ndani na linajumuisha:
- Matamko ya kuingiza
- Kupakia usanidi
- Mifano ya utekelezaji wa maajenti
- Matokeo yanayotarajiwa katika seli za markdown

## Mtindo wa Nambari

### Kanuni za Python

- **Toleo la Python**: 3.12+
- **Mtindo wa Nambari**: Fuata kanuni za kawaida za Python PEP 8
- **Daftari**: Tumia seli za markdown zilizo wazi kuelezea dhana
- **Imports**: Pangilia kwa maktaba ya kawaida, wa tatu, na paikizi

### Kanuni za Daftari za Jupyter

- Jumuisha seli za markdown zenye maelezo kabla ya seli za nambari
- Ongeza mifano ya matokeo ndani ya daftari kwa rejea
- Tumia majina ya vigezo yaliyo wazi yanayolingana na dhana za somo
- Weka mpangilio wa utekelezaji wa daftari kuwa wa mstari (seli 1 → 2 → 3...)

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

## Kujenga na Kusambaza

### Kujenga Nyaraka

Hifadhi hii inatumia Markdown kwa nyaraka:
- Faili za README.md katika kila folda ya somo
- README.md kuu kwenye mzizi wa hifadhi
- Mfumo wa utafsiri otomatiki kupitia GitHub Actions

### Mchakato wa CI/CD

Upo katika `.github/workflows/`:

1. **co-op-translator.yml** - Utafsiri otomatiki kwa lugha 50+
2. **welcome-issue.yml** - Karibisha waandishi wa masuala mapya
3. **welcome-pr.yml** - Karibisha wachangiaji wa maombi mapya ya pull

### Usambazaji

Hii ni hifadhi ya kielimu - hakuna mchakato wa usambazaji. Watumiaji:
1. Fanya fork au kokotoa hifadhi
2. Endesha daftari kwa eneo au katika GitHub Codespaces
3. Jifunze kwa kubadilisha na kujaribu mifano

## Mwongozo wa Maombi ya Pull

### Kabla ya Kuwasilisha

1. **Jaribu mabadiliko yako:**
   - Endesha daftari zilizoathirika kwa ukamilifu
   - Thibitisha kwamba seli zote zinafanya kazi bila makosa
   - Angalia matokeo yanafaa

2. **Mabadiliko ya nyaraka:**
   - Sasisha README.md ikiwa unaongeza dhana mpya
   - Ongeza maoni katika daftari kwa nambari ngumu
   - Hakikisha seli za markdown zinaelezea lengo

3. **Mabadiliko ya Faili:**
   - Epuka kuingiza faili `.env` (tumia `.env.example`)
   - Usingize folda `venv/` au `__pycache__/`
   - Hifadhi matokeo ya daftari wakati yanaonyesha dhana
   - Ondoa faili za muda na nakala za daftari (`*-backup.ipynb`)

### Muundo wa Kichwa cha PR

Tumia vichwa vinavyoelezea:
- `[Lesson-XX] Ongeza mfano mpya kwa <dhana>`
- `[Fix] Rekebisha typo katika README ya somo-XX`
- `[Update] Boresha mfano wa nambari katika somo-XX`
- `[Docs] Sasisha maelekezo ya usanidi`

### Ukaguzi Unaohitajika

- Daftari zinapaswa kuendeshwa bila makosa
- Faili za README ziwe wazi na sahihi
- Fuata mifumo ya nambari iliyopo katika hifadhi
- Kuhakikisha mfanano na masomo mengine

## Vidokezo Zaidi

### Mambo ya Kuepuka

1. **Toleo la Python lisilolingana:**
   - Hakikisha unatumia Python 3.12+
   - Baadhi ya pakiti haziwezi kufanya kazi na matoleo ya zamani
   - Tumia `python3 -m venv` kuainisha toleo la Python wazi

2. **Vigezo vya mazingira:**
   - Daima tengeneza `.env` kutoka `.env.example`
   - Usingize faili `.env` (ipo kwenye `.gitignore`)
   - Tokeni ya GitHub inahitaji ruhusa zinazofaa

3. **Migogoro ya pakiti:**
   - Tumia mazingira ya mtando safi
   - Sakinisha kutoka `requirements.txt` kuliko pakiti binafsi
   - Baadhi ya daftari zinaweza kuhitaji pakiti za ziada zilizotajwa kwenye seli za markdown

4. **Huduma za Azure:**
   - Huduma za Azure AI zinahitaji usajili hai
   - Baadhi ya sifa ni za maeneo maalum
   - Mipaka ya ngazi ya bure iko kwa GitHub Models

### Njia ya Kujifunza

Mwelekeo unaopendekezwa wa masomo:
1. **00-course-setup** - Anza hapa kwa usanidi wa mazingira
2. **01-intro-to-ai-agents** - Fahamu misingi ya maajenti wa AI
3. **02-explore-agentic-frameworks** - Jifunze kuhusu fremu tofauti
4. **03-agentic-design-patterns** - Mifumo kuu ya kubuni
5. Endelea na masomo yaliyo na namba kwa mpangilio

### Uchaguzi wa Fremu

Chagua fremu kulingana na malengo yako:
- **Masomo yote**: Microsoft Agent Framework (MAF) na `AzureAIProjectAgentProvider`
- **Maajenti hujisajili upande wa server** katika Azure AI Foundry Agent Service V2 na yanaonekana kwenye lango la Foundry

### Kupata Msaada

- Jiunge na [Jumuiya ya Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)
- Pitia faili za README za masomo kwa mwongozo maalum
- Angalia [README.md Kuu](./README.md) kwa muhtasari wa kozi
- Rejelea [Usanidi wa Kozi](./00-course-setup/README.md) kwa maelekezo ya kina

### Kuchangia

Hii ni mradi wa wazi wa kielimu. Michango inakaribishwa:
- Boresha mifano ya nambari
- Rekebisha typos au makosa
- Ongeza maoni ya kufafanua
- Pendekeza mada mpya za masomo
- Tafsiri kwa lugha zaidi

Angalia [Masuala ya GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) kwa mahitaji ya sasa.

## Muktadha Maalum wa Mradi

### Msaada wa Lugha Nyingi

Hifadhi hii inatumia mfumo wa utafsiri otomatiki:
- Lugha 50+ zinahudumiwa
- Tafsiri ziko katika `/translations/<lang-code>/` folda
- Mtiririko wa GitHub Actions husimamia masasisho ya utafsiri
- Faili za chanzo ziko kwa Kiingereza kwenye mzizi wa hifadhi

### Muundo wa Somo

Kila somo hufuata muundo thabiti:
1. Kipuzi cha video chenye kiungo
2. Maandishi ya somo (README.md)
3. Sampuli za nambari katika fremu mbalimbali
4. Malengo ya kujifunza na masharti
5. Vyanzo vya ziada vyenye viungo

### Jina la Mfano wa Nambari

Muundo: `<nambari-ya-somo>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Somo 1, MAF Python
- `14-sequential.ipynb` - Somo 14, mifumo ya juu ya MAF

### Folda Maalum

- `translated_images/` - Picha zilizo ya mtafsiri kwa lugha tofauti
- `images/` - Picha za asili za maudhui ya Kiingereza
- `.devcontainer/` - Usanidi wa kontena wa maendeleo wa VS Code
- `.github/` - Mtiririko wa GitHub Actions na mitindo

### Utegemezi

Pakiti kuu kutoka `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Msaada wa Itifaki ya Agent kwa Agent
- `azure-ai-inference`, `azure-ai-projects` - Huduma za Azure AI
- `azure-identity` - Uthibitishaji wa Azure (AzureCliCredential)
- `azure-search-documents` - Egyunganishi wa Azure AI Search
- `mcp[cli]` - Msaada wa Itifaki ya Muktadha wa Mfano

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Onyo**:
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za moja kwa moja zinaweza kuwa na makosa au upotoshaji. Nyaraka asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu kutoka kwa mtafsiri wa binadamu inashauriwa. Sisi hatuwajibiki kwawazi au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->