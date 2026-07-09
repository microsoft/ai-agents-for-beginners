# AGENTS.md

## Projekto apžvalga

Ši saugykla yra „AI agentai pradedantiesiems“ – išsamus mokomasis kursas, mokantis visko, ko reikia AI agentams kurti. Kursą sudaro 18 pamokų, apimančių pagrindus, dizaino šablonus, karkasus ir AI agentų diegimą gamyboje.

**Pagrindinės technologijos:**
- Python 3.12+
- Jupyter užrašų knygelės interaktyviam mokymuisi
- AI karkasai: Microsoft Agent Framework (MAF)
- Azure AI paslaugos: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektūra:**
- Pamokomis pagrįsta struktūra (00-15+ katalogai)
- Kiekviena pamoka turi: README dokumentaciją, kodo pavyzdžius (Jupyter užrašų knygelėse) ir paveikslėlius
- Daugiakalbė palaikymas per automatinę vertimų sistemą
- Viena Python užrašų knygelė kiekvienai pamokai naudojant Microsoft Agent Framework

## Nustatymo komandos

### Reikalavimai
- Python 3.12 arba naujesnė versija
- Azure prenumerata (Microsoft Foundry)
- Įdiegta ir autentifikuota Azure CLI (`az login`)

### Pradinis nustatymas

1. **Klonuokite arba padarykite fork saugyklos:**
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
   # Redaguokite .env su savo API raktas ir galiniais taškais
   ```

### Būtini aplinkos kintamieji

Dėl **Microsoft Foundry** (privalomi):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekto galinis taškas
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modelio diegimo pavadinimas (pvz., gpt-4o)

Dėl **Azure AI Search** (5 pamoka - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search galinis taškas
- `AZURE_SEARCH_API_KEY` - Azure AI Search API raktas

Autentifikacija: paleiskite `az login` prieš vykdant užrašų knygeles (naudoja `AzureCliCredential`).

## Vystymo darbo eiga

### Jupyter užrašų knygelių paleidimas

Kiekvienoje pamokoje yra keletas Jupyter užrašų knygelių skirtingiems karkasams:

1. **Paleiskite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Eikite į pamokos katalogą** (pvz., `01-intro-to-ai-agents/code_samples/`)

3. **Atidarykite ir vykdykite užrašų knygeles:**
   - `*-python-agent-framework.ipynb` - Naudoja Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Naudoja Microsoft Agent Framework (.NET)

### Darbas su Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Reikalinga Azure prenumerata
- Naudoja `FoundryChatClient` Agent Service V2 (agentai matomi Foundry portale)
- Paruošta gamybai su integruota stebėsena
- Failo pavyzdys: `*-python-agent-framework.ipynb`

## Testavimo instrukcijos

Tai mokomoji saugykla su pavyzdiniu kodu, o ne gamybos kodas su automatizuotais testais. Norėdami patikrinti nustatymą ir pakeitimus:

### Rankinis testavimas

1. **Patikrinkite Python aplinką:**
   ```bash
   python --version  # Turėtų būti 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Patikrinkite užrašų knygelės vykdymą:**
   ```bash
   # Konvertuoti užrašų knygelę į scenarijų ir paleisti (testuoja importus)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Patikrinkite aplinkos kintamuosius:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Atskirų užrašų knygelių paleidimas

Atidarykite užrašų knygeles Jupyter ir vykdykite langelius paeiliui. Kiekviena užrašų knygelė yra savarankiška ir apima:
- Importo sakinius
- Konfigūracijos įkėlimą
- Pavyzdinius agentų įgyvendinimus
- Tikėtinus rezultatus markdown langeliuose

## Kodo stilius

### Python konvencijos

- **Python versija**: 3.12+
- **Kodo stilius**: Laikykitės standartinių Python PEP 8 konvencijų
- **Užrašų knygelės**: Naudokite aiškius markdown langelius koncepcijoms paaiškinti
- **Importai**: Grupė pagal standartinę biblioteką, trečiųjų šalių, vietinius importus

### Jupyter užrašų knygelių konvencijos

- Įtraukite aprašomuosius markdown langelius prieš kodo langelius
- Užrašų knygelėse pridėkite išvesties pavyzdžius kaip nuorodą
- Naudokite aiškius kintamųjų pavadinimus, atitinkančius pamokų sąvokas
- Išlaikykite užrašų knygelės vykdymo tvarką tiesinę (langelis 1 → 2 → 3...)

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
- Automatizuota vertimų sistema per GitHub Actions

### CI/CD pipeline

Yra `.github/workflows/` kataloge:

1. **co-op-translator.yml** - Automatinė vertimas į 50+ kalbų
2. **welcome-issue.yml** - Sveikinimai naujiems problemų kūrėjams
3. **welcome-pr.yml** - Sveikinimai naujiems pull request prisidėjusiems

### Diegimas

Tai mokomoji saugykla - nėra diegimo proceso. Vartotojai:
1. Atšaka arba klonuokite saugyklą
2. Vykdykite užrašų knygeles vietoje arba GitHub Codespaces
3. Mokykitės modifikuodami ir eksperimentuodami su pavyzdžiais

## Pull Request gairės

### Prieš teikiant

1. **Išbandykite savo pakeitimus:**
   - Vykdykite paveiktas užrašų knygeles visiškai
   - Patikrinkite, ar visi langeliai veikia be klaidų
   - Įsitikinkite, kad išvestys yra tinkamos

2. **Dokumentacijos atnaujinimai:**
   - Atnaujinkite README.md, jei pridedate naujas sąvokas
   - Pridėkite komentarus užrašų knygelėse dėl sudėtingo kodo
   - Įsitikinkite, kad markdown langeliai paaiškina tikslą

3. **Failų pakeitimai:**
   - Venkite įkelti `.env` failų (naudokite `.env.example`)
   - Nekeiskite `venv/` ar `__pycache__/` katalogų
   - Išlaikykite užrašų knygelių išvestis, jei jos demonstruoja sąvokas
   - Pašalinkite laikinus failus ir atsargines užrašų knygeles (`*-backup.ipynb`)

### PR pavadinimo formatas

Naudokite aprašomuosius pavadinimus:
- `[Lesson-XX] Pridėti naują pavyzdį apie <koncepciją>`
- `[Fix] Pataisyti klaidą lesson-XX README faile`
- `[Update] Patobulinti kodo pavyzdį lesson-XX`
- `[Docs] Atnaujinti nustatymo instrukcijas`

### Privalomi patikrinimai

- Užrašų knygelės turi būti vykdomos be klaidų
- README failai turi būti aiškūs ir tikslingi
- Laikytis esamų kodo šablonų saugykloje
- Užtikrinkite nuoseklumą su kitomis pamokomis

## Papildomos pastabos

### Dažniausiai pasitaikančios problemos

1. **Python versijų neatitikimas:**
   - Naudokite Python 3.12+ versiją
   - Kai kurios bibliotekos gali neveikti su senesnėmis versijomis
   - Naudokite `python3 -m venv` nurodyti Python versiją aiškiai

2. **Aplinkos kintamieji:**
   - Visada sukurkite `.env` iš `.env.example`
   - Nekeiskite `.env` failo (jis įtrauktas į `.gitignore`)
   - Prisijunkite su `az login` dėl autentifikacijos be raktų Entra ID

3. **Paketu konfliktai:**
   - Naudokite švarią virtualią aplinką
   - Įdiekite paketus iš `requirements.txt`, o ne atskirų paketų
   - Kai kurios užrašų knygelės gali reikalauti papildomų paketų, nurodytų markdown langeliuose

4. **Azure paslaugos:**
   - Azure AI paslaugoms reikalinga aktyvi prenumerata
   - Kai kurios funkcijos yra regionui specifinės
   - Įsitikinkite, kad jūsų Azure OpenAI modelio diegimas palaiko Responses API

### Mokymosi eiga

Rekomenduojamas pamokų tvarkos seka:
1. **00-course-setup** - Pradėkite nuo čia dėl aplinkos nustatymo
2. **01-intro-to-ai-agents** - Supraskite AI agentų pagrindus
3. **02-explore-agentic-frameworks** - Susipažinkite su skirtingais karkasais
4. **03-agentic-design-patterns** - Pagrindiniai dizaino šablonai
5. Toliau eikite per pažymėtas pamokas paeiliui

### Karkaso pasirinkimas

Pasirinkite karkasą pagal savo tikslus:
- **Visoms pamokoms**: Microsoft Agent Framework (MAF) su `FoundryChatClient`
- **Agentai registruojasi serveryje** Microsoft Foundry Agent Service V2 ir matomi Foundry portale

### Pagalba

- Prisijunkite prie [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Peržvelkite pamokų README failus dėl specifinių gairių
- Patikrinkite pagrindinį [README.md](./README.md) dėl kurso apžvalgos
- Žr. [Course Setup](./00-course-setup/README.md) dėl detalių nustatymo instrukcijų

### Prisidėjimas

Tai atviras mokomasis projektas. Laukiami prisidėjimai:
- Tobulinti kodo pavyzdžius
- Taisyti rašybos klaidas ar klaidas
- Pridėti paaiškinančius komentarus
- Siūlyti naujas pamokų temas
- Versti į papildomas kalbas

Žiūrėkite [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) dėl esamų poreikių.

## Projekto specifinis kontekstas

### Daugiakalbė palaikymas

Ši saugykla naudoja automatizuotą vertimų sistemą:
- Palaikoma daugiau nei 50 kalbų
- Vertimai saugomi `/translations/<lang-code>/` kataloguose
- Vertimų atnaujinimus vykdo GitHub Actions darbo eiga
- Šaltinio failai yra anglų kalba saugyklos šaknyje

### Pamokų struktūra

Kiekviena pamoka laikosi nuoseklaus šablono:
1. Vaizdo miniatiūra su nuoroda
2. Rašytinė pamokos medžiaga (README.md)
3. Kodo pavyzdžiai keliais karkasais
4. Mokymosi tikslai ir reikalavimai
5. Nuorodos į papildomus mokymosi išteklius

### Kodo pavyzdžių pavadinimai

Formatas: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 1 pamoka, MAF Python
- `14-sequential.ipynb` - 14 pamoka, MAF pažangūs šablonai

### Specialūs katalogai

- `translated_images/` - Lokalių vertimų paveikslėliai
- `images/` - Pirminiai anglų kalbos paveikslėliai
- `.devcontainer/` - VS Code kūrimo konteinerio konfigūracija
- `.github/` - GitHub Actions darbo eigos ir šablonai

### Priklausomybės

Pagrindinės priklausomybės iš `requirements.txt`:
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