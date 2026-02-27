# AGENTS.md

## Projekto apžvalga

Šis saugykla talpina „Dirbtinio intelekto agentai pradedantiesiems“ – išsamų mokymų kursą, mokantį visko, kas reikalinga dirbtinio intelekto agentų kūrimui. Kursą sudaro daugiau nei 15 pamokų, kurios apima pagrindus, dizaino šablonus, karkasus ir dirbtinio intelekto agentų gamybinį diegimą.

**Pagrindinės technologijos:**
- Python 3.12+
- Jupyter bloknotai interaktyviam mokymuisi
- AI karkasai: Microsoft Agent Framework (MAF)
- Azure AI paslaugos: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektūra:**
- Pamokomis pagrįsta struktūra (00-15+ katalogai)
- Kiekviena pamoka turi: README dokumentaciją, kodo pavyzdžius (Jupyter bloknotus) ir paveikslėlius
- Daugiakalbė palaikymas automatizuotos vertimo sistemos pagalba
- Kiekvienoje pamokoje viena Python bloknotas, naudojant Microsoft Agent Framework

## Nustatymo komandos

### Prieš tai būtina turėti
- Python 3.12 ar naujesnę versiją
- Azure prenumeratą (Azure AI Foundry)
- Įdiegtą ir autentifikuotą Azure CLI (`az login`)

### Pradinis nustatymas

1. **Klonuokite arba fork‘inkite saugyklą:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ARBA
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Sukurkite ir aktyvuokite Python virtualią aplinką:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows sistemoje: venv\Scripts\activate
   ```

3. **Įdiekite priklausomybes:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nustatykite aplinkos kintamuosius:**
   ```bash
   cp .env.example .env
   # Redaguokite .env su savo API raktai ir galinio taško adresais
   ```

### Būtini aplinkos kintamieji

Azure AI Foundry (būtina):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry projekto galinis taškas
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modelio diegimo pavadinimas (pvz., gpt-4o)

Azure AI Search (05 pamoka - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search galinis taškas
- `AZURE_SEARCH_API_KEY` - Azure AI Search API raktas

Autentifikacija: prieš paleisdami bloknotus vykdykite `az login` (naudojama `AzureCliCredential`).

## Vystymo darbo eiga

### Jupyter bloknotų paleidimas

Kiekviena pamoka turi keletą Jupyter bloknotų skirtingiems karkasams:

1. **Paleiskite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Eikite į pamokos katalogą** (pvz., `01-intro-to-ai-agents/code_samples/`)

3. **Atidarykite ir vykdykite bloknotus:**
   - `*-python-agent-framework.ipynb` - naudojant Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - naudojant Microsoft Agent Framework (.NET)

### Darbas su Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Reikia Azure prenumeratos
- Naudoja `AzureAIProjectAgentProvider` Agent Service V2 (agentai matomi Foundry portale)
- Gamybai paruošta su integruotu stebėjimu
- Failo šablonas: `*-python-agent-framework.ipynb`

## Testavimo instrukcijos

Tai edukacinė saugykla su pavyzdiniu kodu, o ne gamybinis kodas su automatizuotais testais. Norėdami patikrinti savo nustatymus ir pakeitimus:

### Rankinis testavimas

1. **Patikrinkite Python aplinką:**
   ```bash
   python --version  # Turėtų būti 3.12 ar daugiau
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Patikrinkite bloknoto vykdymą:**
   ```bash
   # Konvertuoti užrašų knygelę į scenarijų ir paleisti (testuoja importus)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Patikrinkite aplinkos kintamuosius:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Atskirų bloknotų paleidimas

Atidarykite bloknotus Jupyter ir vykdykite langelius paeiliui. Kiekvienas bloknotas yra savarankiškas ir apima:
- Importavimo sakinius
- Konfigūracijos įkėlimą
- Pavyzdinius agentų įgyvendinimus
- Tikėtinus rezultatus markdown langeliuose

## Kodo stilius

### Python konvencijos

- **Python versija**: 3.12+
- **Kodo stilius**: laikykitės standartinių Python PEP 8 konvencijų
- **Bloknotai**: naudokite aiškius markdown langelius, paaiškinančius koncepcijas
- **Importai**: grupuokite pagal standartinę biblioteką, trečiųjų šalių, vietinius importus

### Jupyter bloknotų konvencijos

- Prieš kodo langelius įterpkite aiškius aprašomuosius markdown langelius
- Bloknotuose pateikite rezultatų pavyzdžius
- Naudokite aiškius kintamųjų pavadinimus, atitinkančius pamokos temas
- Laikykitės liniarinės bloknotų vykdymo tvarkos (langelis 1 → 2 → 3...)

### Failų organizacija

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
- Pagrindinis README.md saugyklos šakniniame kataloge
- Automatizuota vertimo sistema per GitHub Actions

### CI/CD kanalas

Vieta: `.github/workflows/`:

1. **co-op-translator.yml** - Automatinis vertimas į daugiau nei 50 kalbų
2. **welcome-issue.yml** - Sveikina naujus problemų kūrėjus
3. **welcome-pr.yml** - Sveikina naujus pull request autoriaus indėlius

### Diegimas

Tai edukacinė saugykla – nėra diegimo proceso. Vartotojai:
1. Fork‘ina arba klonuoja saugyklą
2. Paleidžia bloknotus vietoje arba GitHub Codespaces
3. Mokosi, modifikuodami ir eksperimentuodami su pavyzdžiais

## Pull request gairės

### Prieš pateikiant

1. **Ištestuokite savo pakeitimus:**
   - Pilnai vykdykite paveiktus bloknotus
   - Įsitikinkite, kad visi langeliai įvykdomi be klaidų
   - Patikrinkite, ar rezultatai tinkami

2. **Dokumentacijos atnaujinimai:**
   - Atnaujinkite README.md, jei pridedate naujas sąvokas
   - Įtraukite komentarus į bloknotus sudėtingam kodui
   - Įsitikinkite, kad markdown langeliai paaiškina tikslą

3. **Failų pakeitimai:**
   - Venkite commit‘inti `.env` failų (naudokite `.env.example`)
   - Nekomitinkite `venv/` ar `__pycache__/` katalogų
   - Išlaikykite bloknotų rezultatus, jei jie iliustruoja koncepcijas
   - Pašalinkite laikinus failus ir atsarginių kopijų bloknotus (`*-backup.ipynb`)

### PR pavadinimo formatas

Naudokite aiškius pavadinimus:
- `[Lesson-XX] Pridėti naują pavyzdį susijusį su <konceptu>`
- `[Fix] Ištaisyti klaidą lesson-XX README`
- `[Update] Patobulinti kodo pavyzdį lesson-XX`
- `[Docs] Atnaujinti nustatymo instrukcijas`

### Būtini patikrinimai

- Bloknotai turi veikti be klaidų
- README failai turi būti aiškūs ir tikslūs
- Laikyti esamus kodo šablonus saugykloje
- Išlaikyti nuoseklumą su kitomis pamokomis

## Papildomos pastabos

### Dažniausios problemos

1. **Python versijos neatitikimas:**
   - Naudokite Python 3.12 ar naujesnę versiją
   - Kai kurie paketai neveiks su senesnėmis versijomis
   - Naudokite `python3 -m venv`, kad aiškiai nurodytumėte Python versiją

2. **Aplinkos kintamieji:**
   - Visada sukurkite `.env` iš `.env.example`
   - Neįtraukti `.env` į commit‘us (įrašyta `.gitignore`)
   - GitHub token reikalauja atitinkamų leidimų

3. **Paketų konfliktai:**
   - Naudokite švarią virtualią aplinką
   - Įdiekite iš `requirements.txt`, o ne atskirų paketų
   - Kai kuriems bloknotams gali prireikti papildomų paketų, minimų jų markdown langeliuose

4. **Azure paslaugos:**
   - Azure AI paslaugos reikalauja aktyvios prenumeratos
   - Kai kurios funkcijos yra regioniniai
   - Nemokamos ribos taikomos GitHub modeliams

### Mokymosi eiga

Rekomenduojamas pamokų eiliškumas:
1. **00-course-setup** – pradėti nuo čia dėl aplinkos nustatymo
2. **01-intro-to-ai-agents** – suprasti AI agentų pagrindus
3. **02-explore-agentic-frameworks** – susipažinti su skirtingais karkasais
4. **03-agentic-design-patterns** – pagrindiniai dizaino šablonai
5. Toliau tęsti pamokas skaičiavimo tvarka

### Karkaso pasirinkimas

Pasirinkite karkasą pagal savo tikslus:
- **Visos pamokos**: Microsoft Agent Framework (MAF) su `AzureAIProjectAgentProvider`
- **Agentai registruojami serverio pusėje** Azure AI Foundry Agent Service V2 ir matomi Foundry portale

### Pagalba

- Prisijunkite prie [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Peržiūrėkite pamokų README failus dėl specifinių nurodymų
- Žr. pagrindinį [README.md](./README.md) kursų apžvalgai
- Rekomenduojama [Course Setup](./00-course-setup/README.md) detaliam nustatymui

### Dalyvavimas

Tai atvira edukacinė iniciatyva. Kviečiame prisidėti:
- Tobulinti kodo pavyzdžius
- Taisyti klaidas ar rašybos klaidas
- Pridėti paaiškinančius komentaru
- Pasiūlyti naujų pamokų temų
- Versti į papildomas kalbas

Žr. [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) aktualiems poreikiams.

## Projekto kontekstas

### Daugiakalbis palaikymas

Ši saugykla naudoja automatizuotą vertimo sistemą:
- Palaikoma daugiau nei 50 kalbų
- Vertimai saugomi kataloguose `/translations/<lang-code>/`
- GitHub Actions vykdo vertimų atnaujinimus
- Šaltinio failai anglų kalba saugyklos šaknyje

### Pamokų struktūra

Kiekviena pamoka eina pagal nuoseklų šabloną:
1. Vaizdo įrašo miniatiūra su nuoroda
2. Rašytinė pamokos medžiaga (README.md)
3. Kodo pavyzdžiai keliais karkasais
4. Mokymosi tikslai ir reikalavimai
5. Papildomi mokymosi ištekliai su nuorodomis

### Kodo pavyzdžių pavadinimai

Formatas: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` – 1 pamoka, MAF Python
- `14-sequential.ipynb` – 14 pamoka, MAF pažangūs šablonai

### Specialūs katalogai

- `translated_images/` – lokalizuoti paveikslėliai vertimams
- `images/` – originalūs paveikslėliai anglų medžiagai
- `.devcontainer/` – VS Code kūrimo konteinerio konfigūracija
- `.github/` – GitHub Actions darbo eigų ir šablonų katalogas

### Priklausomybės

Pagrindiniai paketai iš `requirements.txt`:
- `agent-framework` – Microsoft Agent Framework
- `a2a-sdk` – Agent-to-Agent protokolo palaikymas
- `azure-ai-inference`, `azure-ai-projects` – Azure AI paslaugos
- `azure-identity` – Azure autentifikacija (AzureCliCredential)
- `azure-search-documents` – Azure AI Search integracija
- `mcp[cli]` – Model Context Protocol palaikymas

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsisakymas nuo atsakomybės**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas pagrindiniu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neprisiimame atsakomybės už bet kokius nesusipratimus ar klaidingas interpretacijas, kylančias dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->