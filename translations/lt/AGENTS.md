# AGENTS.md

## Projekto apžvalga

Šis saugyklos projektas „AI Agents for Beginners“ yra išsamus mokomasis kursas, mokantis visų pagrindų, reikalingų AI agentų kūrimui. Kursas susideda iš daugiau nei 15 pamokų, aprėpiančių pagrindus, dizaino šablonus, karkasus ir AI agentų gamybinį diegimą.

**Pagrindinės technologijos:**
- Python 3.12+
- Jupyter užrašų knygelės interaktyviam mokymuisi
- AI karkasai: Microsoft Agent Framework (MAF)
- Azure AI paslaugos: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektūra:**
- Pagal pamokas struktūrizuota (katalogai 00-15+)
- Kiekviena pamoka turi: README dokumentaciją, kodo pavyzdžius (Jupyter užrašų knygelės) ir paveikslėlius
- Daugialypė kalbų palaikymas per automatizuotą vertimo sistemą
- Viena Python užrašų knygelė kiekvienai pamokai, naudojant Microsoft Agent Framework

## Sąrankos komandos

### Reikalavimai
- Python 3.12 arba naujesnė versija
- Azure prenumerata (Azure AI Foundry)
- Įdiegta ir autentifikuota Azure CLI (`az login`)

### Pradinė sąranka

1. **Klonuoti arba forkinti saugyklą:**
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
   # Redaguokite .env su savo API raktas ir galiniais taškais
   ```

### Būtini aplinkos kintamieji

Skirta **Azure AI Foundry** (būtina):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry projekto galinė taško nuoroda
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modelio diegimo pavadinimas (pvz., gpt-4o)

Skirta **Azure AI Search** (Pamoka 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search galinė taško nuoroda
- `AZURE_SEARCH_API_KEY` - Azure AI Search API raktas

Autentifikacija: paleiskite `az login` prieš vykdant užrašų knygeles (naudoja `AzureCliCredential`).

## Vystymo darbo eiga

### Jupyter užrašų knygelių paleidimas

Kiekviena pamoka turi kelias Jupyter užrašų knygeles skirtingiems karkasams:

1. **Paleiskite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Eikite į pamokos katalogą** (pvz., `01-intro-to-ai-agents/code_samples/`)

3. **Atidarykite ir vykdykite užrašų knygeles:**
   - `*-python-agent-framework.ipynb` - naudojant Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - naudojant Microsoft Agent Framework (.NET)

### Darbas su Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Reikalauja Azure prenumeratos
- Naudoja `AzureAIProjectAgentProvider` Agent Service V2 (agentai matomi Foundry portale)
- Gamybai paruoštas su integruota stebėsena
- Failų šablonas: `*-python-agent-framework.ipynb`

## Testavimo instrukcijos

Tai mokomoji saugykla su pavyzdiniu kodu, o ne gamybinis kodas su automatizuotais testais. Norint patikrinti sąranką ir pakeitimus:

### Rankinis testavimas

1. **Patikrinkite Python aplinką:**
   ```bash
   python --version  # Turėtų būti 3.12 ar naujesnė
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Patikrinkite užrašų knygelių vykdymą:**
   ```bash
   # Konvertuoti užrašų knygelę į skriptą ir paleisti (testuoja importus)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Patikrinkite aplinkos kintamuosius:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Atskirų užrašų knygelių paleidimas

Atidarykite užrašų knygeles Jupyter ir vykdykite langelius paeiliui. Kiekviena užrašų knygelė yra savarankiška ir apima:
- Importavimo sakinius
- Konfigūracijos įkėlimą
- Pavyzdinius agentų įgyvendinimus
- Tikėtinus rezultatus markdown langeliuose

## Kodo stilius

### Python konvencijos

- **Python versija**: 3.12+
- **Kodo stilius**: laikytis Python PEP 8 standartų
- **Užrašų knygelės**: naudoti aiškius markdown langelius koncepcijų paaiškinimui
- **Importai**: grupuoti pagal standartinę biblioteką, trečiųjų šalių ir vietinius importus

### Jupyter užrašų knygelių konvencijos

- Prieš kodo langelius pridėti aprašomuosius markdown langelius
- Įtraukti pavyzdinius rezultatus užrašų knygelėse kaip nuorodą
- Naudoti aiškius kintamųjų pavadinimus, atitinkančius pamokos temas
- Išlaikyti linijinę vykdymo seką (langelis 1 → 2 → 3...)

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

### CI/CD kanalas

Yra ` .github/workflows/` kataloge:

1. **co-op-translator.yml** - automatinis vertimas į >50 kalbų
2. **welcome-issue.yml** - pasveikina sukurtus issues
3. **welcome-pr.yml** - pasveikina pull request autorius

### Diegimas

Tai mokomoji saugykla – nėra diegimo proceso. Vartotojai:
1. Forkina arba klonina saugyklą
2. Vykdo užrašų knygeles vietoje arba GitHub Codespaces
3. Mokosi keisdami ir eksperimentuodami su pavyzdžiais

## Pull Request gairės

### Prieš teikiant

1. **Išbandyti pakeitimus:**
   - Kompleksiškai paleisti paveiktas užrašų knygeles
   - Užtikrinti, kad visi langeliai vykdomi be klaidų
   - Patikrinti, kad rezultatai yra tinkami

2. **Dokumentacijos atnaujinimai:**
   - Atnaujinti README.md, jei pridedama naujų koncepcijų
   - Komentuoti sudėtingą kodą užrašų knygelėse
   - Užtikrinti, kad markdown langeliai paaiškintų paskirtį

3. **Failų pakeitimai:**
   - Nevykdyti `.env` failų (naudokite `.env.example`)
   - Nevykdyti `venv/` ar `__pycache__/` katalogų
   - Išlaikyti užrašų knygelių rezultatus, kai demonstruoja koncepcijas
   - Pašalinti laikinuosius failus ir atsargines kopijas (`*-backup.ipynb`)

### PR pavadinimo formatas

Naudokite aprašomą pavadinimą:
- `[Lesson-XX] Pridėti naują pavyzdį <koncepcijai>`
- `[Fix] Ištaisyti rašybos klaidą lesson-XX README`
- `[Update] Patobulinti kodo pavyzdį lesson-XX`
- `[Docs] Atnaujinti sąrankos instrukcijas`

### Reikalingi patikrinimai

- Užrašų knygelės turi vykdyti be klaidų
- README failai turi būti aiškūs ir tikslūs
- Laikytis esamų kodo šablonų saugykloje
- Išlaikyti vienodumą su kitomis pamokomis

## Papildomos pastabos

### Dažnos problemos

1. **Python versijos neatitikimas:**
   - Naudoti Python 3.12 arba naujesnę versiją
   - Kai kurios pakuotės gali neveikti su senesnėmis versijomis
   - Naudoti `python3 -m venv` aiškiai nurodant versiją

2. **Aplinkos kintamieji:**
   - Visada kurti `.env` iš `.env.example`
   - Nevykdyti `.env` failo (jis įtrauktas į `.gitignore`)
   - GitHub tokenui reikalingos tinkamos leidimai

3. **Pakuočių konfliktai:**
   - Naudoti naują virtualią aplinką
   - Diegti pagal `requirements.txt`, o ne pavienes pakuotes
   - Kai kurios užrašų knygelės gali reikalauti papildomų pakuočių, nurodytų markdown langeliuose

4. **Azure paslaugos:**
   - Azure AI paslaugoms reikia aktyvios prenumeratos
   - Kai kurios funkcijos yra priklausomos nuo regiono
   - GitHub Models taikomi nemokamo lygio apribojimai

### Mokymosi kelias

Rekomenduojama tvarka pamokų eigoje:
1. **00-course-setup** - Pradėkite nuo sąrankos
2. **01-intro-to-ai-agents** - Sužinokite AI agentų pagrindus
3. **02-explore-agentic-frameworks** - Sužinokite apie skirtingus karkasus
4. **03-agentic-design-patterns** - Pagrindiniai dizaino šablonai
5. Toliau sekti pagal numeruojamas pamokas iš eilės

### Karkaso pasirinkimas

Pasirinkite karkasą pagal tikslus:
- **Visoms pamokoms**: Microsoft Agent Framework (MAF) su `AzureAIProjectAgentProvider`
- **Agentai registruojasi serverio pusėje** Azure AI Foundry Agent Service V2 ir matomi Foundry portale

### Pagalba

- Prisijunkite prie [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Peržiūrėkite pamokų README failus dėl konkrečių nurodymų
- Patikrinkite pagrindinį [README.md](./README.md) kursų apžvalgai
- Žr. [Course Setup](./00-course-setup/README.md) dėl detalių sąrankos instrukcijų

### Kūrimas

Tai atviras mokomasis projektas. Kviečiame prisidėti:
- Tobulinti kodo pavyzdžius
- Taisyti rašybos klaidas ar klaidas
- Pridėti paaiškinančius komentarus
- Siūlyti naujas pamokų temas
- Versti į kitas kalbas

Žiūrėkite [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) dėl esamų poreikių.

## Projekto specifinis kontekstas

### Daugialypė kalbų palaikymas

Ši saugykla naudoja automatizuotą vertimo sistemą:
- Palaikoma >50 kalbų
- Vertimai saugomi `/translations/<kalbos-kodas>/` kataloguose
- Vertimo atnaujinimus valdo GitHub Actions darbo eiga
- Šaltinio failai yra anglų kalba saugyklos šaknyje

### Pamokų struktūra

Kiekviena pamoka turi nuoseklų modelį:
1. Vaizdo miniatiūra su nuoroda
2. Rašytinė pamokos medžiaga (README.md)
3. Kodo pavyzdžiai keliems karkasams
4. Mokymosi tikslai ir reikalavimai
5. Papildomos mokymosi medžiagos nuorodos

### Kodo pavyzdžių vardai

Formatas: `<pamokos-numeris>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 1 pamoka, MAF Python
- `14-sequential.ipynb` - 14 pamoka, MAF pažangūs šablonai

### Specialūs katalogai

- `translated_images/` - lokalizuoti paveikslėliai vertimams
- `images/` - originalūs paveikslėliai anglų kalbai
- `.devcontainer/` - VS Code vystymo konteinerio konfigūracija
- `.github/` - GitHub Actions darbo eigos ir šablonai

### Priklausomybės

Svarbios pakuotės iš `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokolo palaikymas
- `azure-ai-inference`, `azure-ai-projects` - Azure AI paslaugos
- `azure-identity` - Azure autentifikacija (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integracija
- `mcp[cli]` - Model Context Protocol palaikymas

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Esant svarbiai informacijai, rekomenduojama kreiptis į profesionalius žmonių vertėjus. Mes neatsakome už bet kokius nesusipratimus ar klaidingus aiškinimus, kilusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->