# AGENTS.md

## Projekto apžvalga

Šiame saugykloje yra „AI Agentai pradedantiesiems“ – išsamus mokomasis kursas, kuriame išmokstama visko, kas reikalinga AI agentų kūrimui. Kursą sudaro 18 pamokų (numeruotos nuo 00 iki 18), apimančių pagrindus, dizaino šablonus, karkasus, gamybos diegimą, vietinius/įrenginių agentus ir AI agentų saugumą.

**Pagrindinės technologijos:**
- Python 3.12+
- Jupyter notebook'ai interaktyviam mokymuisi
- AI karkasai: Microsoft Agent Framework (MAF)
- Azure AI paslaugos: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektūra:**
- Pamokomis pagrįsta struktūra (00-15+ katalogai)
- Kiekviena pamoka turi: README dokumentaciją, kodo pavyzdžius (Jupyter notebook'ai) ir paveikslėlius
- Daugiakalbė palaikymas per automatizuotą vertimo sistemą
- Kiekvienai pamokai atskiras Python notebook'as naudojant Microsoft Agent Framework

## Parengimo komandos

### Išankstinės sąlygos
- Python 3.12 arba naujesnė versija
- Azure prenumerata (Microsoft Foundry)
- Įdiegtas ir autentifikuotas Azure CLI (`az login`)

### Pradinis nustatymas

1. **Klonuoti arba forkuoti saugyklą:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ARBA
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Sukurti ir aktyvuoti Python virtualią aplinką:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows operacinėje sistemoje: venv\Scripts\activate
   ```

3. **Įdiegti priklausomybes:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nustatyti aplinkos kintamuosius:**
   ```bash
   cp .env.example .env
   # Redaguokite .env su savo API raktų ir galinių taškų reikšmėmis
   ```

### Būtini aplinkos kintamieji

Dėl **Microsoft Foundry** (būtina):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekto galutinė vieta
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modelio diegimo pavadinimas (pvz., gpt-5-mini)

Dėl **Azure AI Search** (Pamoka 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search galutinė vieta
- `AZURE_SEARCH_API_KEY` - Azure AI Search API raktas

Autentifikavimas: Paleiskite `az login` prieš paleisdami notebook'us (naudoja `AzureCliCredential`).

## Kūrimo darbo eiga

### Jupyter notebook'ų paleidimas

Kiekviena pamoka turi kelis Jupyter notebook'us skirtingiems karkasams:

1. **Paleisti Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Eiti į pamokos katalogą** (pvz., `01-intro-to-ai-agents/code_samples/`)

3. **Atidaryti ir vykdyti notebook'us:**
   - `*-python-agent-framework.ipynb` - naudojant Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - naudojant Microsoft Agent Framework (.NET)

### Darbas su Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Reikalinga Azure prenumerata
- Naudoja `FoundryChatClient` Agent Service V2 (agentai matomi Foundry portale)
- Paruošta gamybai su įmontuota stebėsena
- Failų šablonas: `*-python-agent-framework.ipynb`

## Testavimo instrukcijos

Tai mokomoji saugykla su pavyzdiniu kodu, o ne gamybinis kodas su automatizuotais testais. Norėdami patikrinti savo nustatymus ir pakeitimus:

### Rankinis testavimas

1. **Patikrinti Python aplinką:**
   ```bash
   python --version  # Turi būti 3.12 ar daugiau
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Patikrinti notebook'o vykdymą:**
   ```bash
   # Konvertuoti užrašų knygelę į scenarijų ir paleisti (tikrina importus)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Patikrinti aplinkos kintamuosius:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Atskirų notebook'ų paleidimas

Atidarykite notebook'us Jupyter ir vykdykite langelius paeiliui. Kiekvienas notebook'as yra savarankiškas ir apima:
- Importų sakinius
- Konfigūracijos įkėlimą
- Pavyzdinius agentų įgyvendinimus
- Tikėtinus išvesties pavyzdžius markdown langeliuose

### Išmestinių testų vykdymas išdiegtiesiems agentams

Pamokose, kur agentas išdiegtas kaip Microsoft Foundry talpinamas agentas (01, 04, 05, 16), saugykla turi išmestinių testų katalogus po `tests/`, kurie paleidžiami `.github/workflows/smoke-test.yml` darbo eigos per [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) veiksmą. Tai lengvas po-diegimo patikrinimas (ar agentas pasiekiamas ir ar vykdo pagrindines užklausas tinkamai?), kuris papildo vertinimo srautą pamokose 10 ir 16. Peržvelkite [tests/README.md](./tests/README.md) dėl katalogo-pamokos-agento žemėlapio. Pamoka 17 veikia lokaliai su Foundry Local ir neturi talpinamos galutinės vietos, todėl ji validačiuojama tiesiogiai vykdant jos notebook'ą.

## Kodo stilius

### Python konvencijos

- **Python versija**: 3.12+
- **Kodo stilius**: Laikytis standartinių Python PEP 8 konvencijų
- **Notebook'ai**: Naudoti aiškius markdown langelius konceptų paaiškinimui
- **Importai**: Grupuoti pagal standartinę biblioteką, trečiųjų šalių, vietinius importus

### Jupyter Notebook konvencijos

- Pridėti aprašomuosius markdown langelius prieš kodo langelius
- Notebook'uose pateikti išvesties pavyzdžius kaip nuorodą
- Naudoti aiškius kintamųjų pavadinimus, atitinkančius pamokos konceptus
- Laikyti notebook'o vykdymo tvarką linearią (langelis 1 → 2 → 3...)

### Failų organizavimas

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Kūrimas ir diegimas

### Dokumentacijos kūrimas

Ši saugykla naudoja Markdown dokumentacijai:
- README.md failai kiekviename pamokos aplanke
- Pagrindinis README.md saugyklos šaknyje
- Automatizuota vertimo sistema per GitHub Actions

### CI/CD srautas

Vieta `.github/workflows/`:

1. **co-op-translator.yml** - Automatinis vertimas į 50+ kalbų
2. **welcome-issue.yml** - Naujo klausimo kūrėjų sveikinimas
3. **welcome-pr.yml** - Naujo priedo prie PR dalyvių sveikinimas

### Diegimas

Tai mokomoji saugykla – nėra diegimo proceso. Vartotojai:
1. Fork'ina arba klonuoja saugyklą
2. Paleidžia notebook'us lokaliai arba GitHub Codespaces
3. Mokosi keisdami ir eksperimentuodami su pavyzdžiais

## Pull request gairės

### Prieš pateikiant

1. **Išbandykite savo pakeitimus:**
   - Pilnai vykdykite paveiktus notebook'us
   - Patikrinkite, kad visi langeliai vykdytųsi be klaidų
   - Įsitikinkite, kad išvestys tinkamos

2. **Dokumentacijos atnaujinimai:**
   - Atnaujinkite README.md jei pridedate naujas sąvokas
   - Pridėkite komentarus notebook'uose sudėtingam kodui
   - Užtikrinkite, kad markdown langeliai aiškintų paskirtį

3. **Failų pakeitimai:**
   - Venkite pateikti `.env` failų (naudokite `.env.example`)
   - Nepateikite `venv/` ar `__pycache__/` katalogų
   - Išlaikykite notebook'ų išvestis, kai jos demonstruoja konceptus
   - Pašalinkite laikinuosius failus ir atsargines kopijas (`*-backup.ipynb`)

### PR pavadinimo formatas

Naudokite aprašomuosius pavadinimus:
- `[Lesson-XX] Pridėti naują pavyzdį <koncepcijai>`
- `[Fix] Pataisyti klaidą lesson-XX README`
- `[Update] Pagerinti kodo pavyzdį lesson-XX`
- `[Docs] Atnaujinti diegimo instrukcijas`

### Būtini patikrinimai

- Notebook'ai turi vykdytis be klaidų
- README failai turi būti aiškūs ir tikslūs
- Laikytis esamų kodo šablonų saugykloje
- Išlaikyti nuoseklumą su kitomis pamokomis

## Papildomos pastabos

### Dažniausios klaidos

1. **Python versijos neatitikimas:**
   - Užtikrinti, kad naudojate Python 3.12+
   - Kai kurios bibliotekos gali neveikti su senesnėmis versijomis
   - Naudokite `python3 -m venv` nurodydami Python versiją aiškiai

2. **Aplinkos kintamieji:**
   - Visada sukurkite `.env` iš `.env.example`
   - Nepateikite `.env` failo (jis yra `.gitignore`)
   - Prisijunkite naudodami `az login` be rakto Entra ID autentifikacijai

3. **Paketo konfliktai:**
   - Naudokite švarią virtualią aplinką
   - Įdiekite iš `requirements.txt`, o ne atskirų paketų
   - Kai kurie notebook'ai gali reikalauti papildomų paketų, nurodytų jų markdown langeliuose

4. **Azure paslaugos:**
   - Azure AI paslaugoms reikalinga aktyvi prenumerata
   - Kai kurios funkcijos yra regioninės
   - Užtikrinkite, kad jūsų Azure OpenAI modelio diegimas palaiko Responses API

### Mokymosi kelias

Rekomenduojama seka per pamokas:
1. **00-course-setup** - pradėti nuo čia, siekiant aplinkos paruošimo
2. **01-intro-to-ai-agents** - suprasti AI agentų pagrindus
3. **02-explore-agentic-frameworks** - sužinoti apie skirtingus karkasus
4. **03-agentic-design-patterns** - pagrindiniai dizaino šablonai
5. Toliau vykdyti pamokas iš eilės pagal numeraciją

### Karkaso pasirinkimas

Pasirinkite karkasą pagal savo tikslus:
- **Visos pamokos**: Microsoft Agent Framework (MAF) su `FoundryChatClient`
- **Agentai registruojasi serverio pusėje** Microsoft Foundry Agent Service V2 ir matomi Foundry portale

### Pagalba

- Prisijunkite prie [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Peržiūrėkite pamokų README failus dėl konkrečių nurodymų
- Peržiūrėkite pagrindinį [README.md](./README.md) dėl kurso apžvalgos
- Žiūrėkite [Course Setup](./00-course-setup/README.md) detalioms įdiegimo instrukcijoms

### Indėlis

Tai atviras mokomasis projektas. Kviečiame prisidėti:
- Tobulinti kodo pavyzdžius
- Taisyti klaidas ar rašybos klaidas
- Pridėti paaiškinančius komentarus
- Siūlyti naujas pamokų temas
- Versti į papildomas kalbas

Peržiūrėkite [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) dėl esamų poreikių.

## Projekto specifinis kontekstas

### Daugiakalbė palaikymas

Ši saugykla naudoja automatizuotą vertimo sistemą:
- Palaikoma 50+ kalbų
- Vertimai kataloguose `/translations/<kalbos-kodas>/`
- Vertimų atnaujinimus valdo GitHub Actions darbo eiga
- Šaltinio failai anglų kalba saugyklos šaknyje

### Pamokos struktūra

Kiekviena pamoka laikosi nuoseklumo:
1. Vaizdo miniatiūra su nuoroda
2. Rašytinė pamokos medžiaga (README.md)
3. Kodo pavyzdžiai keliuose karkasuose
4. Mokymosi tikslai ir išankstiniai reikalavimai
5. Nuorodos į papildomus mokymosi šaltinius

### Kodo pavyzdžių vardai

Formatas: `<pamokos-numeris>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 1 pamoka, MAF Python
- `14-sequential.ipynb` - 14 pamoka, MAF pažangūs šablonai
- `16-python-agent-framework.ipynb` - 16 pamoka, gamybinis klientų aptarnavimo agentas
- `17-local-agent-foundry-local.ipynb` - 17 pamoka, vietinis agentas su Foundry Local + Qwen

### Specifiniai katalogai

- `translated_images/` - Lokalizuoti paveikslėliai vertimams
- `images/` - Originalūs anglų kalbos paveikslėliai
- `.devcontainer/` - VS Code kūrimo konteinerio konfigūracija
- `.github/` - GitHub Actions darbo eigų ir šablonų katalogas

### Priklausomybės

Pagrindiniai paketai iš `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokolo palaikymas
- `azure-ai-inference`, `azure-ai-projects` - Azure AI paslaugos
- `azure-identity` - Azure autentifikacija (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integracija
- `mcp[cli]` - Model Context Protocol palaikymas

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->