# WAKALA.md

## Muhtasari wa Mradi

Hifadhidata hii ina "Wakala wa AI kwa Waanzilishi" - kozi kamili ya elimu inayofundisha kila kinachohitajika kujenga Wakala wa AI. Kozi ina masomo 18 (yenye nambari 00-18) yanayofunika misingi, mifumo ya kubuni, mifumo ya kazi, uanzishaji wa uzalishaji, wakala wa eneo la karibu/kifaa, na usalama wa wakala wa AI.

**Teknolojia Muhimu:**
- Python 3.12+
- Daftari la Jupyter kwa kujifunza kwa mwingiliano
- Mifumo ya AI: Mfumo wa Wakala wa Microsoft (MAF)
- Huduma za Azure AI: Microsoft Foundry, Huduma ya Wakala ya Microsoft Foundry V2

**Usanifu:**
- Muundo wa masomo (folda 00-18)
- Kila somo lina: hati ya README, mfano wa msimbo (daftari la Jupyter), na picha
- Usaidizi wa lugha nyingi kupitia mfumo wa tafsiri wa moja kwa moja
- Daftari la Python moja kwa kila somo likitumia Mfumo wa Wakala wa Microsoft

## Amri za Kuandaa

### Mahitaji ya Mwanzo
- Python 3.12 au zaidi
- Usajili wa Azure (kwa Microsoft Foundry)
- Azure CLI imewekwa na kuthibitishwa (`az login`)

### Kuanzisha Mwanzo

1. **Kopea au fanya fork ya hifadhidata:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Tengeneza na washwe mazingira ya virtual ya Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Sakinisha utegemezi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Weka vigezo vya mazingira:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Vigezo Muhimu vya Mazingira

Kwa **Microsoft Foundry** (Inahitajika):
- `AZURE_AI_PROJECT_ENDPOINT` - Mwisho wa mradi wa Microsoft Foundry
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Jina la uanzishaji wa mfano (mfano, gpt-5-mini)

Kwa **Azure AI Search** (Somo 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Mwisho wa Azure AI Search
- `AZURE_SEARCH_API_KEY` - Msimbo wa API wa Azure AI Search

Uthibitishaji: Endesha `az login` kabla ya kuendesha daftari (inatumia `AzureCliCredential`).

## Mtiririko wa Maendeleo

### Kuendesha Daftari za Jupyter

Kila somo lina daftari nyingi za Jupyter kwa mifumo tofauti:

1. **Anza Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Nenda kwenye folda ya somo** (mfano, `01-intro-to-ai-agents/code_samples/`)

3. **Fungua na endesha daftari:**
   - `*-python-agent-framework.ipynb` - Kutumia Mfumo wa Wakala wa Microsoft (Python)
   - `*-dotnet-agent-framework.ipynb` - Kutumia Mfumo wa Wakala wa Microsoft (.NET)

### Kufanya kazi na Mfumo wa Wakala wa Microsoft

**Mfumo wa Wakala wa Microsoft + Microsoft Foundry:**
- Inahitaji usajili wa Azure
- Inatumia `FoundryChatClient` kwa Huduma ya Wakala V2 (wakala wanaonekana katika lango la Foundry)
- Tayari kwa uzalishaji na ufuatiliaji wa ndani
- Mfano wa faili: `*-python-agent-framework.ipynb`

## Maelekezo ya Kupima

Hii ni hifadhidata ya elimu yenye mfano wa msimbo badala ya msimbo wa uzalishaji na majaribio ya moja kwa moja. Ili kuthibitisha maandalizi na mabadiliko yako:

### Kupima Kwa Mkono

1. **Jaribu mazingira ya Python:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Jaribu uendeshaji wa daftari:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Thibitisha vigezo vya mazingira:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Kuendesha Daftari Binafsi

Fungua daftari katika Jupyter na endesha seli kwa mpangilio. Kila daftari ni huru na lina:
- Tamko la kuleta maktaba
- Kupakia usanidi
- Mifano ya utekelezaji wa wakala
- Matokeo yanayotarajiwa katika seli za markdown

### Kupima Haraka Wakala Walioanzishwa

Kwa masomo ambayo wakala ameanzishwa kama wakala aliyehifadhiwa Microsoft Foundry (01, 04, 05, 16), hifadhidata hupeleka vitabu vya mtihani wa moshi chini ya `tests/` vinavyotekelezwa na mtiririko wa kazi wa `.github/workflows/smoke-test.yml` kupitia kitendo cha [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test). Hizi ni ngazi ya mlangoni baada ya uanzishaji (je, wakala anapatikana na anafuata matarajio ya msingi ya amri?), zinakamilisha mchakato wa tathmini wa Masomo 10 na 16. Angalia [tests/README.md](./tests/README.md) kwa ramani ya kitabu-cha-somo-cha-wakala. Somo la 17 linaendeshwa eneo la karibu na Foundry Local na halina kiunganishi cha kuhifadhiwa, hivyo linathibitishwa kwa kuendesha daftari lake moja kwa moja.

## Mtindo wa Msimbo

### Mambo ya Python

- **Toleo la Python**: 3.12+
- **Mtindo wa Msimbo**: Fuata taratibu za kawaida za Python PEP 8
- **Daftari**: Tumia seli wazi za markdown kuelezea dhana
- **Kuleta maktaba**: Gawanya kwa maktaba za kawaida, za mtu wa tatu, na zile za hapa eneo

### Mambo ya Daftari la Jupyter

- Jumuisha seli za maelezo kabla ya seli za msimbo
- Ongeza mifano ya matokeo katika daftari kama rejea
- Tumia majina wazi ya vigezo yanayolingana na dhana za somo
- Hifadhi mfuatano wa uendeshaji daftari (seli 1 → 2 → 3...)

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

## Ujenzi na Uanzishaji

### Kujenga Hati

Hifadhidata hii inatumia Markdown kwa hati:
- Faili za README.md katika kila folda ya somo
- README.md kuu kwenye mizizi ya hifadhidata
- Mfumo wa tafsiri wa moja kwa moja kupitia Vitendo vya GitHub

### Mlolongo wa CI/CD

Iko katika `.github/workflows/`:

1. **co-op-translator.yml** - Tafsiri otomatiki kwa lugha zaidi ya 50
2. **welcome-issue.yml** - Kuwakaribisha wasaidizi wa masuala mapya
3. **welcome-pr.yml** - Kuwakaribisha wasaidizi wa ombi la mabadiliko

### Uanzishaji

Hii ni hifadhidata ya elimu - hakuna mchakato wa uanzishaji. Watumiaji:
1. Fanya fork au kopea hifadhidata
2. Endesha daftari eneo lako la karibu au katika GitHub Codespaces
3. Jifunze kwa kubadilisha na kujaribu mifano

## Miongozo ya Ombi la Mabadiliko

### Kabla ya Kuwasilisha

1. **Jaribu mabadiliko yako:**
   - Endesha daftari zilizoathirika kikamilifu
   - Thibitisha seli zote zinaendeshwa bila makosa
   - Hakikisha matokeo ni sahihi

2. **Sasisho la Hati:**
   - Sasisha README.md ikiwa unaongeza dhana mpya
   - Ongeza maelezo katika daftari kwa msimbo mgumu
   - Hakikisha seli za markdown zinaelezea madhumuni

3. **Mabadiliko ya Faili:**
   - Epuka kuingiza faili za `.env` (tumia `.env.example`)
   - Usitoe `venv/` au folda za `__pycache__/`
   - Hifadhi matokeo ya daftari pale yanapotambulisha dhana
   - Ondoa faili za muda na nakala za daftari (`*-backup.ipynb`)

### Muundo wa Kichwa cha PR

Tumia vichwa vya kueleweka:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Ukaguzi Unaohitajika

- Daftari zipaswa kuendesha bila makosa
- Faili za README zipaswa kuwa wazi na sahihi
- Fuata mifumo ya msimbo iliyopo hifadhidata
- Hakikisha utekelezaji unafanana na masomo mengine

## Vidokezo Zaidi

### Makosa ya Kawaida

1. **Toleo la Python linalolingana:**
   - Hakikisha Python 3.12+ inatumika
   - Baadhi ya vifurushi havitafanya kazi na toleo la zamani
   - Tumia `python3 -m venv` kuainisha toleo la Python wazi

2. **Vigezo vya Mazingira:**
   - Daima tengeneza `.env` kutoka `.env.example`
   - Usitoe faili ya `.env` (iko katika `.gitignore`)
   - Ingia kwa `az login` kwa uthibitishaji wa Entra ID bila funguo

3. **Migogoro ya vifurushi:**
   - Tumia mazingira ya virtual safi
   - Sakinisha kutoka `requirements.txt` badala ya vifurushi binafsi
   - Baadhi ya daftari huenda zikahitaji vifurushi zaidi vilivyoelezwa katika seli za markdown

4. **Huduma za Azure:**
   - Huduma za AI za Azure zinahitaji usajili unaoendeshwa
   - Baadhi ya vipengele ni maalum kwa mikoa fulani
   - Hakikisha ujumbe wako wa Azure OpenAI unaunga mkono API ya Majibu

### Njia ya Kujifunza

Kupitia masomo haya yanayopendekezwa:
1. **00-course-setup** - Anza hapa kwa maandalizi ya mazingira
2. **01-intro-to-ai-agents** - Fahamu misingi ya wakala wa AI
3. **02-explore-agentic-frameworks** - Jifunze kuhusu mifumo tofauti
4. **03-agentic-design-patterns** - Mifumo mikuu ya kubuni
5. Endelea na masomo yenye nambari kwa mpangilio

### Uchaguzi wa Mfumo

Chagua mfumo kulingana na malengo yako:
- **Masomo yote**: Mfumo wa Wakala wa Microsoft (MAF) na `FoundryChatClient`
- **Wakala hujisajili upande wa seva** katika Huduma ya Wakala ya Microsoft Foundry V2 na wanaonekana katika lango la Foundry

### Kupata Msaada

- Jiunge na [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Angalia faili za README za somo kwa mwongozo maalum
- Angalia [README.md kuu](./README.md) kwa muhtasari wa kozi
- Rejelea [Course Setup](./00-course-setup/README.md) kwa maelekezo ya kina ya maandalizi

### Kuchangia

Huu ni mradi wa elimu wa wazi. Michango inakaribishwa:
- Boresha mifano ya msimbo
- Rekebisha tahajia au makosa
- Ongeza maelezo ya ufafanuzi
- Pendekeza mada mpya za somo
- Tafsiri kwa lugha zaidi

Tazama [Masuala ya GitHub](https://github.com/microsoft/ai-agents-for-beginners/issues) kwa mahitaji ya sasa.

## Muktadha Maalum wa Mradi

### Usaidizi wa Lugha Nyingi

Hifadhidata hii inatumia mfumo wa tafsiri wa moja kwa moja:
- Lugha zaidi ya 50 zinaungwa mkono
- Tafsiri ziko katika folda za `/translations/<lang-code>/`
- Mtiririko wa Vitendo vya GitHub unasimamia sasisho la tafsiri
- Faili za chanzo ni kwa Kiingereza kwenye mizizi ya hifadhidata

### Muundo wa Somo

Kila somo lina mtindo thabiti:
1. Kidude cha video chenye kiungo
2. Maudhui ya somo yaliyoandikwa (README.md)
3. Mifano ya msimbo katika mifumo mingi
4. Malengo ya kujifunza na mahitaji
5. Rasilimali za ziada za kujifunza zimeunganishwa

### Kumbukumbu za Mifano ya Msimbo

Muundo: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Somo 1, MAF Python
- `14-sequential.ipynb` - Somo 14, mifumo ya juu ya MAF
- `16-python-agent-framework.ipynb` - Somo 16, wakala wa huduma kwa wateja uzalishaji
- `17-local-agent-foundry-local.ipynb` - Somo 17, wakala wa eneo la karibu na Foundry Local + Qwen

### Folda Maalum

- `translated_images/` - Picha zilizotafsiriwa za eneo
- `images/` - Picha za kiingilio kwa maudhui ya Kiingereza
- `.devcontainer/` - Usanidi wa kontena wa maendeleo VS Code
- `.github/` - Mtiririko wa Vitendo vya GitHub na templeti

### Vitegemezi

Vifurushi muhimu kutoka `requirements.txt`:
- `agent-framework` - Mfumo wa Wakala wa Microsoft
- `a2a-sdk` - Msaada wa itifaki ya Wakala kwa Wakala
- `azure-ai-inference`, `azure-ai-projects` - Huduma za AI za Azure
- `azure-identity` - Uthibitishaji wa Azure (AzureCliCredential)
- `azure-search-documents` - Integrasiyo ya Azure AI Search
- `mcp[cli]` - Msaada wa Itifaki ya Muktadha wa Mfano

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->