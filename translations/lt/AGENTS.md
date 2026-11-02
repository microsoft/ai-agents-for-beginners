# AGENTS.md

## Projekto apžvalga

Ši saugykla yra „AI Agentai pradedantiesiems“ – išsamus edukacinis kursas, mokantis visko, kas reikalinga AI agentų kūrimui. Kursą sudaro 18 pamokų (numeruotos nuo 00 iki 18), apimančių pagrindus, projektavimo šablonus, karkasus, gamybinį diegimą, vietinius/įrenginyje veikiančius agentus ir AI agentų saugumą.

**Pagrindinės technologijos:**
- Python 3.12+
- Jupyter užrašų knygelės interaktyviam mokymuisi
- AI karkasai: Microsoft Agent Framework (MAF)
- Azure AI paslaugos: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektūra:**
- Pamokų pagrindu struktūrizuota (00-18 katalogai)
- Kiekviena pamoka turi: README dokumentaciją, kodo pavyzdžius (Jupyter užrašų knygeles) ir paveikslėlius
- Daugiakalbė palaikymas automatizuotos vertimo sistemos dėka
- Po vieną Python užrašų knygelę kiekvienai pamokai, naudojant Microsoft Agent Framework

## Sąrankos komandos

### Reikalavimai
- Python 3.12 arba naujesnė versija
- Azure prenumerata (Microsoft Foundry)
- Azure CLI įdiegtas ir autentifikuotas (`az login`)

### Pradinis nustatymas

1. **Klonuokite arba sukite saugyklą:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Sukurkite ir aktyvuokite Python virtualią aplinką:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Įdiekite priklausomybes:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Nustatykite aplinkos kintamuosius:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Būtini aplinkos kintamieji

Microsoft Foundry (būtina):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekto galinis taškas
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modelio diegimo pavadinimas (pvz., gpt-5-mini)

Azure AI Search (Pamoka 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search galinis taškas
- `AZURE_SEARCH_API_KEY` - Azure AI Search API raktas

Autentifikacija: paleiskite `az login` prieš paleisdami užrašų knygeles (naudoja `AzureCliCredential`).

## Vystymo darbo eiga

### Jupyter užrašų knygelių paleidimas

Kiekviena pamoka turi keletą Jupyter užrašų knygelių, skirtų skirtingiems karkasams:

1. **Paleiskite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Eikite į pamokos katalogą** (pvz., `01-intro-to-ai-agents/code_samples/`)

3. **Atidarykite ir paleiskite užrašų knygeles:**
   - `*-python-agent-framework.ipynb` - Naudojant Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Naudojant Microsoft Agent Framework (.NET)

### Darbas su Microsoft Agent Framework

Microsoft Agent Framework + Microsoft Foundry:
- Reikalinga Azure prenumerata
- Naudoja `FoundryChatClient` Agent Service V2 (agentai matomi Foundry portale)
- Gamybai paruošta su įmontuotu stebėjimu
- Failų šablonas: `*-python-agent-framework.ipynb`

## Testavimo instrukcijos

Tai edukacinė saugykla su pavyzdiniu kodu, o ne gamybinis kodas su automatizuotais testais. Norėdami patikrinti savo sąranką ir pakeitimus:

### Rankinis testavimas

1. **Patikrinkite Python aplinką:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Patikrinkite užrašų knygelių vykdymą:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Patikrinkite aplinkos kintamuosius:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Atskirų užrašų knygelių paleidimas

Atidarykite užrašų knygeles Jupyter ir vykdykite langelius iš eilės. Kiekviena užrašų knygelė yra savarankiška ir apima:
- Importavimo teiginius
- Konfigūracijos įkėlimą
- Pavyzdinius agentų įgyvendinimus
- Numatomus rezultatus markdown langeliuose

### Išdėstytų agentų vardiklio testavimas

Pamokose, kuriose agentas diegiamas kaip Microsoft Foundry talpinamas agentas (01, 04, 05, 16), saugykla turi vardiklio testų katalogus `tests/`, kurie vykdomi `.github/workflows/smoke-test.yml` darbo eigos per [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) veiksmą. Tai lengvi po diegimo išankstiniai patikrinimai (ar agentas pasiekiamas ir ar atitinka pagrindinius užklausų lūkesčius?), papildantys vertinimo procesą pamokose 10 ir 16. Žr. [tests/README.md](./tests/README.md) dėl katalogo-pamokos-agentų atitikimo. Pamoka 17 paleidžiama vietoje su Foundry Local ir neturi talpinamo galinio taško, todėl ji validuojama tiesiogiai paleidžiant jos užrašų knygelę.

## Kodo stilius

### Python konvencijos

- **Python versija**: 3.12+
- **Kodo stilius**: Laikykitės standartinių Python PEP 8 konvencijų
- **Užrašų knygelės**: Naudokite aiškius markdown langelius koncepcijoms paaiškinti
- **Importai**: Grupėkite pagal standartinę biblioteką, trečiųjų šalių ir vietinius importus

### Jupyter užrašų knygelių konvencijos

- Įtraukite aprašomuosius markdown langelius prieš kodo langelius
- Užrašų knygelėse pridėkite pavyzdinius išėjimus
- Naudokite aiškius kintamųjų pavadinimus, atitinkančius pamokos koncepcijas
- Išlaikykite užrašų knygelės vykdymo tvarką nuoseklią (langelis 1 → 2 → 3...)

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
- README.md failai kiekviename pamokos kataloge
- Pagrindinis README.md saugyklos šaknyje
- Automatizuota vertimo sistema per GitHub Actions

### CI/CD srautas

Vieta: `.github/workflows/`:

1. **co-op-translator.yml** - Automatinis vertimas į 50+ kalbų
2. **welcome-issue.yml** - Sveikina naujus problemų kūrėjus
3. **welcome-pr.yml** - Sveikina naujus pull request bendradarbius

### Diegimas

Tai edukacinė saugykla – nėra diegimo proceso. Vartotojai:
1. Klonuoja arba sukuria saugyklos forką
2. Paleidžia užrašų knygeles vietoje arba GitHub Codespaces aplinkoje
3. Mokosi modifikuodami ir eksperimentuodami su pavyzdžiais

## Pull Request (PR) gairės

### Prieš pateikiant

1. **Išbandykite savo pakeitimus:**
   - Paleiskite paveiktas užrašų knygeles pilnai
   - Patikrinkite, kad visi langeliai vyksta be klaidų
   - Įsitikinkite, kad rezultatai yra teisingi

2. **Dokumentacijos atnaujinimai:**
   - Atnaujinkite README.md, jei pridedate naujas sąvokas
   - Pridėkite komentarus užrašų knygelėse dėl sudėtingo kodo
   - Įsitikinkite, kad markdown langeliai paaiškina paskirtį

3. **Failų pakeitimai:**
   - Venkite įsipareigojimų `.env` failams (naudokite `.env.example`)
   - Neišsaugokite `venv/` ar `__pycache__/` katalogų
   - Išlaikykite užrašų knygelių išėjimus, kai jie demonstruoja sąvokas
   - Pašalinkite laikinuosius failus ir atsargines užrašų knygeles (`*-backup.ipynb`)

### PR antraštės formatas

Naudokite aprašomas antraštes:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Būtini patikrinimai

- Užrašų knygelės turi vykdyti be klaidų
- README failai turi būti aiškūs ir tikslūs
- Vadovaukitės esamais kodo šablonais saugykloje
- Išlaikykite nuoseklumą su kitomis pamokomis

## Papildomos pastabos

### Dažnos klaidos

1. **Python versijų neatitikimas:**
   - Naudokite Python 3.12+ versiją
   - Kai kurios bibliotekos gali neveikti su senesnėmis versijomis
   - Naudokite `python3 -m venv`, kad nurodytumėte Python versiją tiksliai

2. **Aplinkos kintamieji:**
   - Visada kurkite `.env` iš `.env.example`
   - Neišsaugokite `.env` failo (jis yra `.gitignore`)
   - Autentifikuokitės naudodami `az login` be rakto Entra ID autentifikacijai

3. **Paketo konfliktai:**
   - Naudokite švarią virtualią aplinką
   - Įdiekite iš `requirements.txt`, o ne atskirus paketus
   - Kai kurios užrašų knygelės gali reikalauti papildomų paketų, minimų jų markdown langeliuose

4. **Azure paslaugos:**
   - Azure AI paslaugos reikalauja aktyvios prenumeratos
   - Kai kurios funkcijos priklauso nuo regiono
   - Įsitikinkite, kad jūsų Azure OpenAI modelio diegimas palaiko Responses API

### Mokymosi kelias

Rekomenduojama sesijų tvarka:
1. **00-course-setup** - pradžia su aplinkos nustatymu
2. **01-intro-to-ai-agents** - Supažindinimas su AI agentų pagrindais
3. **02-explore-agentic-frameworks** - Susipažinimas su skirtingais karkasais
4. **03-agentic-design-patterns** - Pagrindiniai projektavimo šablonai
5. Toliau pereikite per pamokas nuosekliai pagal numeraciją

### Karkaso pasirinkimas

Pasirinkite karkasą pagal tikslus:
- **Visos pamokos**: Microsoft Agent Framework (MAF) su `FoundryChatClient`
- **Agentai registruojasi serveryje** Microsoft Foundry Agent Service V2 ir matomi Foundry portale

### Pagalba

- Prisijunkite prie [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Peržiūrėkite pamokų README failus dėl konkrečių nurodymų
- Patikrinkite pagrindinį [README.md](./README.md) dėl kurso apžvalgos
- Žr. [Course Setup](./00-course-setup/README.md) dėl detalių sąrankos instrukcijų

### Prisidėjimas

Tai atviras edukacinis projektas. Kviečiame prisidėti:
- Tobulinti kodo pavyzdžius
- Taisyti rašybos klaidas arba klaidas
- Pridėti paaiškinančius komentarus
- Siūlyti naujas pamokų temas
- Versti į kitas kalbas

Žr. [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) dėl esamų poreikių.

## Projekto specifinis kontekstas

### Daugiakalbė palaikymas

Ši saugykla naudoja automatizuotą vertimo sistemą:
- Palaikoma daugiau nei 50 kalbų
- Vertimai saugomi `/translations/<lang-code>/` kataloguose
- GitHub Actions darbo eiga tvarko vertimų atnaujinimus
- Šaltinio failai yra anglų kalba saugyklos šaknyje

### Pamokos struktūra

Kiekviena pamoka laikosi nuoseklaus šablono:
1. Vaizdo miniatiūra su nuoroda
2. Rašytinė pamokos medžiaga (README.md)
3. Kodo pavyzdžiai keliuose karkasuose
4. Mokymosi tikslai ir reikalavimai
5. Papildomi mokymosi ištekliai su nuorodomis

### Kodo pavyzdžių pavadinimai

Formatas: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Pamoka 1, MAF Python
- `14-sequential.ipynb` - Pamoka 14, MAF pažangūs šablonai
- `16-python-agent-framework.ipynb` - Pamoka 16, gamybinis klientų aptarnavimo agentas
- `17-local-agent-foundry-local.ipynb` - Pamoka 17, vietinis agentas su Foundry Local + Qwen

### Specialūs katalogai

- `translated_images/` - Vietiniai paveikslėliai vertimams
- `images/` - Originalūs paveikslėliai anglų turiniui
- `.devcontainer/` - VS Code vystymo konteinerio konfigūracija
- `.github/` - GitHub Actions darbo eigos ir šablonai

### Priklausomybės

Pagrindiniai paketai iš `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agentų tarpusavio protokolo palaikymas
- `azure-ai-inference`, `azure-ai-projects` - Azure AI paslaugos
- `azure-identity` - Azure autentifikacija (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integracija
- `mcp[cli]` - Modelio konteksto protokolo palaikymas

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->