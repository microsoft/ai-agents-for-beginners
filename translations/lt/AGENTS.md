# AGENTS.md

## Projekto apžvalga

Šiame saugykloje yra „AI agentai pradedantiesiems“ – išsamus mokomasis kursas, kuriame mokoma visko, ko reikia AI agentų kūrimui. Kursą sudaro 18 pamokų (numeruotas nuo 00 iki 18), apimančių pagrindus, dizaino šablonus, karkasus, gamybinį diegimą, vietinius/įrenginio agentus ir AI agentų saugumą.

**Pagrindinės technologijos:**
- Python 3.12+
- Jupyter bloknotai interaktyviam mokymuisi
- AI karkasai: Microsoft Agent Framework (MAF)
- Azure AI paslaugos: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektūra:**
- Pagal pamokas suskirstyta struktūra (00-15+ katalogai)
- Kiekviena pamoka turi: README dokumentaciją, kodo pavyzdžius (Jupyter bloknotai) ir paveikslėlius
- Daugiakalbė palaikymas per automatinę vertimo sistemą
- Vienas Python bloknotas kiekvienai pamokai, naudojant Microsoft Agent Framework

## Nustatymo komandos

### Išankstiniai reikalavimai
- Python 3.12 arba naujesnė versija
- Azure prenumerata (Microsoft Foundry naudojimui)
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
   source venv/bin/activate  # Windows sistemoje: venv\Scripts\activate
   ```

3. **Įdiegti priklausomybes:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nustatyti aplinkos kintamuosius:**
   ```bash
   cp .env.example .env
   # Redaguokite .env su savo API raktus ir galiniais taškais
   ```

### Būtini aplinkos kintamieji

Microsoft Foundry (privaloma):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekto pabaigos taškas
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modelio diegimo pavadinimas (pvz., gpt-4.1-mini)

Azure AI Search (pamoka 05 – RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search pabaigos taškas
- `AZURE_SEARCH_API_KEY` - Azure AI Search API raktas

Autentifikavimui paleiskite `az login` prieš paleisdami bloknotus (naudoja `AzureCliCredential`).

## Vystymo procesas

### Jupyter bloknotų paleidimas

Kiekviena pamoka turi kelis Jupyter bloknotus skirtingiems karkasams:

1. **Paleiskite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviguokite į pamokos katalogą** (pvz., `01-intro-to-ai-agents/code_samples/`)

3. **Atidarykite ir vykdykite bloknotus:**
   - `*-python-agent-framework.ipynb` - Naudoja Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Naudoja Microsoft Agent Framework (.NET)

### Darbas su Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Reikalinga Azure prenumerata
- Naudoja `FoundryChatClient` Agent Service V2 (agentai matomi Foundry portale)
- Paruošta gamybai su integruotu stebėjimu
- Failų šablonas: `*-python-agent-framework.ipynb`

## Testavimo instrukcijos

Tai edukacinė saugykla su pavyzdiniu kodu, o ne gamybinis kodas su automatizuotais testais. Norint patikrinti nustatymą ir pakeitimus:

### Rankinis testavimas

1. **Testuoti Python aplinką:**
   ```bash
   python --version  # Turi būti 3.12 arba naujesnė
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testuoti bloknoto vykdymą:**
   ```bash
   # Konvertuoti užrašų knygelę į skriptą ir paleisti (testuoja importus)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Patikrinti aplinkos kintamuosius:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Individualių bloknotų vykdymas

Atidarykite bloknotus Jupyter ir vykdykite eilutė po eilutės. Kiekvienas bloknotas yra savarankis ir apima:
- Importo sakinius
- Konfigūracijos įkėlimą
- Pavyzdinius agentų įgyvendinimus
- Tikėtinas rezultatas markdown langeliuose

### Diegtų agentų pirminis testavimas

Pamokose, kur agentas diegiamas kaip Microsoft Foundry hostinamas agentas (01, 04, 05, 16), saugykla pateikia pirminio testavimo katalogus `tests/` aplanke, kurie vykdomi `.github/workflows/smoke-test.yml` darbo eiga per [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) veiksmą. Tai lengvas po diegimo patikrinimas (ar agentas pasiekiamas ir atlieka pagrindinius užklausų lūkesčius?), papildantis vertinimo procesą pamokose 10 ir 16. Žr. [tests/README.md](./tests/README.md) katalogo-pamokos-agentų susiejimą. Pamoka 17 veikia lokaliai su Foundry Local ir neturi hostinamo pabaigos taško, todėl ji tikrinama tiesiogiai paleidus jos bloknotą.

## Kodo stilius

### Python konvencijos

- **Python versija**: 3.12+
- **Kodo stilius**: Laikytis standartinių Python PEP 8 taisyklių
- **Bloknotai**: Naudoti aiškius markdown langelius konceptų paaiškinimui
- **Importai**: Grupuoti pagal standartinę biblioteką, trečiųjų šalių ir vietinius importus

### Jupyter bloknotų konvencijos

- Prie kodo langelių įtraukti aprašomuosius markdown langelius
- Bloknotuose pateikti rezultatų pavyzdžius
- Naudoti aiškius kintamųjų pavadinimus, atitinkančius pamokos konceptus
- Laikyti bloknotų vykdymo tvarką linijinę (langelis 1 → 2 → 3...)

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

Šioje saugykloje dokumentacijai naudojamas Markdown:
- README.md failai kiekviename pamokos kataloge
- Pagrindinis README.md saugyklos šaknyje
- Automatinė vertimo sistema per GitHub Actions

### CI/CD procesas

Vyksta naudojant `.github/workflows/` katalogą:

1. **co-op-translator.yml** – Automatinis vertimas į 50+ kalbų
2. **welcome-issue.yml** – Naujos problemos kūrėjų pasveikinimas
3. **welcome-pr.yml** – Naujos traukimo užklausos dalyvių pasveikinimas

### Diegimas

Tai edukacinė saugykla – diegimo proceso nėra. Vartotojai:
1. Forkina arba klonuoja saugyklą
2. Paleidžia bloknotus lokaliai arba GitHub Codespaces aplinkoje
3. Mokosi modifikuodami ir eksperimentuodami su pavyzdžiais

## Pullo užklausų gairės

### Prieš pateikiant

1. **Išbandykite savo pakeitimus:**
   - Pilnai paleiskite paveiktus bloknotus
   - Patikrinkite, kad visi langeliai vykdomi be klaidų
   - Įsitikinkite, kad išvedimai yra tinkami

2. **Dokumentacijos atnaujinimas:**
   - Atnaujinkite README.md, jei pridedate naujus konceptus
   - Pridėkite komentarus bloknotuose prie sudėtingo kodo
   - Įsitikinkite, kad markdown langeliai paaiškina paskirtį

3. **Failų pakeitimai:**
   - Venkite įsipareigoti `.env` failų (naudokite `.env.example`)
   - Neišsaugokite `venv/` ar `__pycache__/` katalogų
   - Išlaikykite bloknotų išvedimus, jei jie demonstruoja konceptus
   - Pašalinkite laikinuosius failus ir atsargines bloknotų kopijas (`*-backup.ipynb`)

### PR pavadinimo formatas

Naudokite aprašomuosius pavadinimus:
- `[Lesson-XX] Pridėti naują pavyzdį <konceptui>`
- `[Fix] Pataisyti klaidą lesson-XX README faile`
- `[Update] Patobulinti kodo pavyzdį lesson-XX`
- `[Docs] Atnaujinti nustatymo instrukcijas`

### Būtini patikrinimai

- Bloknotai turėtų vykdyti be klaidų
- README failai turėtų būti aiškūs ir tikslūs
- Laikytis esamų kodo šablonų saugykloje
- Išlaikyti nuoseklumą su kitomis pamokomis

## Papildomos pastabos

### Dažnos problemos

1. **Python versijos neatitikimas:**
   - Naudoti Python 3.12+ versiją
   - Kai kurios paketo versijos neveikia su senesnėmis versijomis
   - Naudokite `python3 -m venv`, kad aiškiai nurodytumėte Python versiją

2. **Aplinkos kintamieji:**
   - Visada sukurkite `.env` remiantis `.env.example`
   - Neišsaugokite `.env` failo (įtrauktas į `.gitignore`)
   - Prisijunkite naudodami `az login` be raktų per Entra ID autentifikavimą

3. **Paketo konfliktai:**
   - Naudokite švarią virtualią aplinką
   - Įdiekite priklausomybes iš `requirements.txt`, o ne po vieną paketą
   - Kai kurie bloknotai gali reikalauti papildomų paketų, nurodytų jų markdown langeliuose

4. **Azure paslaugos:**
   - Azure AI paslaugoms reikalinga aktyvi prenumerata
   - Kai kurios funkcijos yra regiono specifinės
   - Įsitikinkite, kad jūsų Azure OpenAI modelio diegimas palaiko Responses API

### Mokymosi kelias

Rekomenduojama pamokų eiga:
1. **00-course-setup** – Pradėkite nuo čia aplinkos nustatymui
2. **01-intro-to-ai-agents** – Susipažinkite su AI agentų pagrindais
3. **02-explore-agentic-frameworks** – Sužinokite apie skirtingus karkasus
4. **03-agentic-design-patterns** – Pagrindiniai dizaino šablonai
5. Toliau sekti pamokas pagal numeraciją

### Karkaso pasirinkimas

Pasirinkite karkasą pagal savo tikslus:
- **Visoms pamokoms**: Microsoft Agent Framework (MAF) su `FoundryChatClient`
- **Agentai registruojasi pusės serverio** Microsoft Foundry Agent Service V2 ir yra matomi Foundry portale

### Pagalba

- Prisijunkite prie [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Peržiūrėkite pamokų README failus dėl konkrečios informacijos
- Patikrinkite pagrindinį [README.md](./README.md) kursų apžvalgai
- Žr. [Course Setup](./00-course-setup/README.md) detalioms nustatymo instrukcijoms

### Prisidėjimas

Tai atviras edukacinis projektas. Kviečiame prisidėti:
- Tobulinti kodo pavyzdžius
- Taisyti rašybos klaidas ar kitus trūkumus
- Pridėti išsamius komentarus
- Siūlyti naujas pamokų temas
- Versti į papildomas kalbas

Žr. [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) dabartiniams poreikiams.

## Projekto specifinis kontekstas

### Daugiakalbė palaikymas

Ši saugykla naudoja automatizuotą vertimo sistemą:
- Palaiko 50+ kalbų
- Vertimai saugomi `/translations/<lang-code>/` aplankuose
- Vertimų atnaujinimus atlieka GitHub Actions darbo eiga
- Šaltinio failai yra anglų kalba saugyklos šaknyje

### Pamokos struktūra

Kiekviena pamoka laikosi nuoseklaus šablono:
1. Vaizdo miniatiūra su nuoroda
2. Parašyta pamokos medžiaga (README.md)
3. Kodo pavyzdžiai keliuose karkasuose
4. Mokymosi tikslai ir išankstiniai reikalavimai
5. Papildomi mokymosi ištekliai su nuorodomis

### Kodo pavyzdžių pavadinimai

Formatavimas: `<pamokos-numeris>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` – Pamoka 1, MAF Python
- `14-sequential.ipynb` – Pamoka 14, MAF pažangūs šablonai
- `16-python-agent-framework.ipynb` – Pamoka 16, gamybinis klientų palaikymo agentas
- `17-local-agent-foundry-local.ipynb` – Pamoka 17, vietinis agentas su Foundry Local + Qwen

### Specialūs katalogai

- `translated_images/` – Lokalizuoti paveikslėliai vertimams
- `images/` – Originalūs anglų kalbos paveikslėliai
- `.devcontainer/` – VS Code kūrimo konteinerių konfigūracija
- `.github/` – GitHub Actions darbo eigos ir šablonai

### Priklausomybės

Pagrindiniai paketai iš `requirements.txt`:
- `agent-framework` – Microsoft Agent Framework
- `a2a-sdk` – Agent-to-Agent protokolo palaikymas
- `azure-ai-inference`, `azure-ai-projects` – Azure AI paslaugos
- `azure-identity` – Azure autentifikacija (AzureCliCredential)
- `azure-search-documents` – Azure AI Search integracija
- `mcp[cli]` – Modelio konteksto protokolo palaikymas

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->