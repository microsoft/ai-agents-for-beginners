# AGENTS.md

## Projekto apžvalga

Šiame saugykloje pateikiamas kursas „AI agentai pradedantiesiems“ – išsamus edukacinis kursas, mokantis visko, ko reikia norint sukurti AI agentus. Kursą sudaro daugiau nei 15 pamokų, apimančių pagrindus, dizaino šablonus, sistemas ir AI agentų diegimą gamyboje.

**Pagrindinės technologijos:**
- Python 3.12+
- Jupyter Notebooks interaktyviam mokymuisi
- AI sistemos: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI paslaugos: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (galimas nemokamas planas)

**Architektūra:**
- Pamokų struktūra (00–15+ katalogai)
- Kiekviena pamoka apima: README dokumentaciją, kodo pavyzdžius (Jupyter Notebooks) ir vaizdus
- Daugiakalbė palaikymo sistema per automatizuotą vertimo sistemą
- Keli sistemos pasirinkimai kiekvienai pamokai (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Nustatymo komandos

### Būtinos sąlygos
- Python 3.12 ar naujesnė versija
- GitHub paskyra (GitHub Models – nemokamas planas)
- Azure prenumerata (neprivaloma, Azure AI paslaugoms)

### Pradinis nustatymas

1. **Klonuokite arba „forkinkite“ saugyklą:**
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


### Reikalingi aplinkos kintamieji

GitHub Models (nemokamas planas):
- `GITHUB_TOKEN` – asmeninis prieigos raktas iš GitHub

Azure AI paslaugoms (neprivaloma):
- `PROJECT_ENDPOINT` – Azure AI Foundry projekto galinis taškas
- `AZURE_OPENAI_API_KEY` – Azure OpenAI API raktas
- `AZURE_OPENAI_ENDPOINT` – Azure OpenAI galinio taško URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` – pokalbių modelio diegimo pavadinimas
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` – įterpimų diegimo pavadinimas
- Papildoma Azure konfigūracija, pateikta `.env.example` faile

## Kūrimo darbo eiga

### Jupyter Notebooks paleidimas

Kiekviena pamoka apima kelis Jupyter Notebooks skirtingoms sistemoms:

1. **Paleiskite Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Eikite į pamokos katalogą** (pvz., `01-intro-to-ai-agents/code_samples/`)

3. **Atidarykite ir vykdykite Notebooks:**
   - `*-semantic-kernel.ipynb` – naudojant Semantic Kernel sistemą
   - `*-autogen.ipynb` – naudojant AutoGen sistemą
   - `*-python-agent-framework.ipynb` – naudojant Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` – naudojant Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` – naudojant Azure AI Agent Service

### Darbas su skirtingomis sistemomis

**Semantic Kernel + GitHub Models:**
- Galimas nemokamas planas su GitHub paskyra
- Tinka mokymuisi ir eksperimentavimui
- Failų šablonas: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Galimas nemokamas planas su GitHub paskyra
- Daugiagentės orkestracijos galimybės
- Failų šablonas: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Naujausia Microsoft sistema
- Galima Python ir .NET
- Failų šablonas: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Reikalinga Azure prenumerata
- Funkcijos, paruoštos gamybai
- Failų šablonas: `*-azureaiagent.ipynb`

## Testavimo instrukcijos

Tai edukacinė saugykla su pavyzdiniu kodu, o ne gamybos kodu su automatizuotais testais. Norėdami patikrinti savo nustatymus ir pakeitimus:

### Rankinis testavimas

1. **Testuokite Python aplinką:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Testuokite Notebook vykdymą:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Patikrinkite aplinkos kintamuosius:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Atskirų Notebooks vykdymas

Atidarykite Notebooks Jupyter ir vykdykite langelius nuosekliai. Kiekvienas Notebook yra savarankiškas ir apima:
- Importo teiginius
- Konfigūracijos įkėlimą
- Agentų įgyvendinimo pavyzdžius
- Tikėtinus rezultatus markdown langeliuose

## Kodo stilius

### Python konvencijos

- **Python versija**: 3.12+
- **Kodo stilius**: laikykitės standartinių Python PEP 8 konvencijų
- **Notebooks**: naudokite aiškius markdown langelius, kad paaiškintumėte koncepcijas
- **Importai**: grupuokite pagal standartinę biblioteką, trečiųjų šalių ir vietinius importus

### Jupyter Notebook konvencijos

- Prieš kodo langelius įtraukite aprašomuosius markdown langelius
- Pridėkite rezultatų pavyzdžius Notebooks kaip nuorodą
- Naudokite aiškius kintamųjų pavadinimus, atitinkančius pamokos koncepcijas
- Išlaikykite Notebook vykdymo tvarką linijinę (langelis 1 → 2 → 3...)

### Failų organizavimas

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```


## Kūrimas ir diegimas

### Dokumentacijos kūrimas

Ši saugykla naudoja Markdown dokumentacijai:
- README.md failai kiekviename pamokos kataloge
- Pagrindinis README.md saugyklos šaknyje
- Automatinė vertimo sistema per GitHub Actions

### CI/CD procesas

Esantis `.github/workflows/`:

1. **co-op-translator.yml** – automatinis vertimas į daugiau nei 50 kalbų
2. **welcome-issue.yml** – pasveikina naujus problemų kūrėjus
3. **welcome-pr.yml** – pasveikina naujus „pull request“ prisidėtojus

### Diegimas

Tai edukacinė saugykla – nėra diegimo proceso. Vartotojai:
1. „Forkinkite“ arba klonuokite saugyklą
2. Vykdykite Notebooks lokaliai arba GitHub Codespaces
3. Mokykitės modifikuodami ir eksperimentuodami su pavyzdžiais

## „Pull Request“ gairės

### Prieš pateikimą

1. **Testuokite savo pakeitimus:**
   - Vykdykite paveiktus Notebooks pilnai
   - Patikrinkite, ar visi langeliai vykdomi be klaidų
   - Įsitikinkite, kad rezultatai yra tinkami

2. **Dokumentacijos atnaujinimai:**
   - Atnaujinkite README.md, jei pridedate naujas koncepcijas
   - Pridėkite komentarus Notebooks sudėtingam kodui
   - Įsitikinkite, kad markdown langeliai paaiškina tikslą

3. **Failų pakeitimai:**
   - Venkite įtraukti `.env` failų (naudokite `.env.example`)
   - Neįtraukite `venv/` ar `__pycache__/` katalogų
   - Išlaikykite Notebook rezultatus, kai jie demonstruoja koncepcijas
   - Pašalinkite laikinus failus ir atsarginius Notebooks (`*-backup.ipynb`)

### PR pavadinimo formatas

Naudokite aprašomuosius pavadinimus:
- `[Lesson-XX] Pridėti naują pavyzdį <koncepcijai>`
- `[Fix] Ištaisyti klaidą pamokos-XX README`
- `[Update] Patobulinti kodo pavyzdį pamokoje-XX`
- `[Docs] Atnaujinti nustatymo instrukcijas`

### Reikalingi patikrinimai

- Notebooks turi būti vykdomi be klaidų
- README failai turi būti aiškūs ir tikslūs
- Laikykitės esamų kodo šablonų saugykloje
- Išlaikykite nuoseklumą su kitomis pamokomis

## Papildomos pastabos

### Dažniausios problemos

1. **Python versijos neatitikimas:**
   - Įsitikinkite, kad naudojate Python 3.12+
   - Kai kurios paketai gali neveikti su senesnėmis versijomis
   - Naudokite `python3 -m venv`, kad aiškiai nurodytumėte Python versiją

2. **Aplinkos kintamieji:**
   - Visada sukurkite `.env` iš `.env.example`
   - Neįtraukite `.env` failo (jis yra `.gitignore`)
   - GitHub raktas turi turėti tinkamus leidimus

3. **Paketų konfliktai:**
   - Naudokite šviežią virtualią aplinką
   - Įdiekite iš `requirements.txt`, o ne atskirų paketų
   - Kai kurie Notebooks gali reikalauti papildomų paketų, nurodytų jų markdown langeliuose

4. **Azure paslaugos:**
   - Azure AI paslaugoms reikalinga aktyvi prenumerata
   - Kai kurios funkcijos yra specifinės regionui
   - Nemokamo plano apribojimai taikomi GitHub Models

### Mokymosi kelias

Rekomenduojama pamokų seka:
1. **00-course-setup** – pradėkite nuo aplinkos nustatymo
2. **01-intro-to-ai-agents** – supraskite AI agentų pagrindus
3. **02-explore-agentic-frameworks** – sužinokite apie skirtingas sistemas
4. **03-agentic-design-patterns** – pagrindiniai dizaino šablonai
5. Tęskite numeruotas pamokas nuosekliai

### Sistemos pasirinkimas

Pasirinkite sistemą pagal savo tikslus:
- **Mokymasis/Prototipavimas**: Semantic Kernel + GitHub Models (nemokamas)
- **Daugiagentės sistemos**: AutoGen
- **Naujausios funkcijos**: Microsoft Agent Framework (MAF)
- **Diegimas gamyboje**: Azure AI Agent Service

### Pagalbos gavimas

- Prisijunkite prie [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Peržiūrėkite pamokų README failus, kad gautumėte konkrečią pagalbą
- Patikrinkite pagrindinį [README.md](./README.md) dėl kurso apžvalgos
- Žiūrėkite [Course Setup](./00-course-setup/README.md) dėl detalių nustatymo instrukcijų

### Prisidėjimas

Tai atviras edukacinis projektas. Prisidėjimai laukiami:
- Tobulinkite kodo pavyzdžius
- Taisykite klaidas ar netikslumus
- Pridėkite paaiškinančius komentarus
- Siūlykite naujas pamokų temas
- Verskite į papildomas kalbas

Žiūrėkite [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) dėl esamų poreikių.

## Projekto specifinis kontekstas

### Daugiakalbė palaikymo sistema

Ši saugykla naudoja automatizuotą vertimo sistemą:
- Palaikoma daugiau nei 50 kalbų
- Vertimai saugomi `/translations/<lang-code>/` kataloguose
- GitHub Actions darbo eiga tvarko vertimo atnaujinimus
- Šaltinio failai yra anglų kalba saugyklos šaknyje

### Pamokų struktūra

Kiekviena pamoka laikosi nuoseklaus šablono:
1. Vaizdo įrašo miniatiūra su nuoroda
2. Rašytinis pamokos turinys (README.md)
3. Kodo pavyzdžiai keliomis sistemomis
4. Mokymosi tikslai ir būtinos sąlygos
5. Papildomi mokymosi ištekliai su nuorodomis

### Kodo pavyzdžių pavadinimai

Formatas: `<pamokos-numeris>-<sistemos-pavadinimas>.ipynb`
- `04-semantic-kernel.ipynb` – Pamoka 4, Semantic Kernel
- `07-autogen.ipynb` – Pamoka 7, AutoGen
- `14-python-agent-framework.ipynb` – Pamoka 14, MAF Python
- `14-dotnet-agent-framework.ipynb` – Pamoka 14, MAF .NET

### Specialūs katalogai

- `translated_images/` – lokalizuoti vaizdai vertimams
- `images/` – originalūs vaizdai anglų turiniui
- `.devcontainer/` – VS Code kūrimo konteinerio konfigūracija
- `.github/` – GitHub Actions darbo eigos ir šablonai

### Priklausomybės

Pagrindiniai paketai iš `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` – AutoGen sistema
- `semantic-kernel` – Semantic Kernel sistema
- `agent-framework` – Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` – Azure AI paslaugos
- `azure-search-documents` – Azure AI Search integracija
- `chromadb` – Vektorinė duomenų bazė RAG pavyzdžiams
- `chainlit` – Pokalbių UI sistema
- `browser_use` – Naršyklės automatizavimas agentams
- `mcp[cli]` – Model Context Protocol palaikymas
- `mem0ai` – Atminties valdymas agentams

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.