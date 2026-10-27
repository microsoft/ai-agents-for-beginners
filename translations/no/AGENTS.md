# AGENTS.md

## Prosjektoversikt

Dette depotet inneholder "AI-agenter for nybegynnere" - et omfattende utdanningskurs som lærer alt som trengs for å bygge AI-agenter. Kurset består av 18 leksjoner (nummerert 00-18) som dekker grunnleggende, designmønstre, rammeverk, produksjonsdistribusjon, lokale/enhetsbaserte agenter og sikkerhet for AI-agenter.

**Nøkkelteknologier:**
- Python 3.12+
- Jupyter Notebooks for interaktiv læring
- AI-rammeverk: Microsoft Agent Framework (MAF)
- Azure AI-tjenester: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkitektur:**
- Leksjonsbasert struktur (00-18 mapper)
- Hver leksjon inneholder: README-dokumentasjon, kodeeksempler (Jupyter-notebooks) og bilder
- Flerspråklig støtte via automatisert oversettelsessystem
- En Python-notebook per leksjon som bruker Microsoft Agent Framework

## Oppsettkommandoer

### Forutsetninger
- Python 3.12 eller høyere
- Azure-abonnement (for Microsoft Foundry)
- Azure CLI installert og autentisert (`az login`)

### Initialt oppsett

1. **Klone eller forke depotet:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Opprett og aktiver Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Installer avhengigheter:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Sett opp miljøvariabler:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Påkrevde miljøvariabler

For **Microsoft Foundry** (påkrevd):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry prosjektendepunkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modellutplasseringsnavn (f.eks., gpt-5-mini)

For **Azure AI Search** (Leksjon 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search-endepunkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nøkkel

Autentisering: Kjør `az login` før kjøring av notebooks (bruker `AzureCliCredential`).

## Utviklingsarbeidsflyt

### Kjøre Jupyter Notebooks

Hver leksjon inneholder flere Jupyter-notebooks for forskjellige rammeverk:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviger til en leksjonsmappe** (f.eks., `01-intro-to-ai-agents/code_samples/`)

3. **Åpne og kjør notebooks:**
   - `*-python-agent-framework.ipynb` - Bruke Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Bruke Microsoft Agent Framework (.NET)

### Arbeide med Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Krever Azure-abonnement
- Bruker `FoundryChatClient` for Agent Service V2 (agenter synlige i Foundry-portalen)
- Produksjonsklar med innebygd observabilitet
- Filnavnmønster: `*-python-agent-framework.ipynb`

## Testinstruksjoner

Dette er et utdanningsdepot med eksempel-kode, ikke produksjonskode med automatiserte tester. For å verifisere oppsett og endringer:

### Manuell testing

1. **Test Python-miljøet:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test kjøring av notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifiser miljøvariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Kjøre individuelle notebooks

Åpne notebooks i Jupyter og kjør cellene sekvensielt. Hver notebook er selvstendig og inkluderer:
- Import-setninger
- Laste inn konfigurasjon
- Eksempel-agentimplementasjoner
- Forventede utdata i markdown-celler

### Røyk-testing av distribuerte agenter

For leksjoner hvor en agent distribueres som en Microsoft Foundry-hostet agent (01, 04, 05, 16), tilbyr repo røyk-testkataloger under `tests/` som kjøres av `.github/workflows/smoke-test.yml`-arbeidsflyten via [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)-actionen. Dette er en lettvekts post-distribusjonsport (er agenten tilgjengelig og følger grunnleggende promptforventninger?), som utfyller evalueringspipelinen i leksjonene 10 og 16. Se [tests/README.md](./tests/README.md) for katalog-til-leksjon-til-agent kartlegging. Leksjon 17 kjøres lokalt med Foundry Local og har ingen hostet endepunkt, så den valideres ved å kjøre sin notebook direkte.

## Kodeformat

### Python-konvensjoner

- **Python-versjon**: 3.12+
- **Kodeformat**: Følg standard Python PEP 8-konvensjoner
- **Notebooks**: Bruk klare markdown-celler for å forklare konsepter
- **Imports**: Grupper etter standardbibliotek, tredjepart, lokale imports

### Jupyter Notebook-konvensjoner

- Inkluder beskrivende markdown-celler før kodeceller
- Legg til utdataeksempler i notebooks for referanse
- Bruk klare variabelnavn som samsvarer med leksjonskonsepter
- Hold notebook kjørerekkefølge lineær (celle 1 → 2 → 3...)

### Filorganisering

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Bygging og distribusjon

### Bygge dokumentasjon

Dette depotet bruker Markdown for dokumentasjon:
- README.md filer i hver leksjonsmappe
- Hoved-README.md i depotets rot
- Automatisert oversettelsessystem via GitHub Actions

### CI/CD-pipeline

Ligger i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversettelse til 50+ språk
2. **welcome-issue.yml** - Ønsker nye issue-opprettelser velkommen
3. **welcome-pr.yml** - Ønsker nye pull request-bidragsytere velkommen

### Distribusjon

Dette er et utdanningsdepot - ingen distribusjonsprosess. Brukere:
1. Fork eller klon depotet
2. Kjør notebooks lokalt eller i GitHub Codespaces
3. Lær ved å modifisere og eksperimentere med eksempler

## Retningslinjer for pull request

### Før innsending

1. **Test endringene dine:**
   - Kjør berørte notebooks fullstendig
   - Verifiser at alle celler kjører uten feil
   - Sjekk at utdata er passende

2. **Oppdater dokumentasjon:**
   - Oppdater README.md hvis du legger til nye konsepter
   - Legg til kommentarer i notebooks for komplisert kode
   - Sørg for at markdown-celler forklarer formålet

3. **Filendringer:**
   - Unngå å commite `.env` filer (bruk `.env.example`)
   - Ikke commit `venv/` eller `__pycache__/` mapper
   - Behold notebook-utdata når de demonstrerer konsepter
   - Fjern midlertidige filer og backup-notebooks (`*-backup.ipynb`)

### PR-tittelformat

Bruk beskrivende titler:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Påkrevde sjekker

- Notebooks skal kjøre uten feil
- README-filer skal være klare og korrekte
- Følg eksisterende kode-mønstre i depotet
- Oppretthold konsistens med andre leksjoner

## Tilleggsnotater

### Vanlige fallgruver

1. **Python-versjonsmismatch:**
   - Sørg for å bruke Python 3.12+
   - Noen pakker fungerer kanskje ikke med eldre versjoner
   - Bruk `python3 -m venv` for å spesifisere Python-versjon eksplisitt

2. **Miljøvariabler:**
   - Lag alltid `.env` fra `.env.example`
   - Ikke commit `.env` fil (den er i `.gitignore`)
   - Logg på med `az login` for nøkkelfri Entra ID-autentisering

3. **Pakke-konflikter:**
   - Bruk et nytt virtuelt miljø
   - Installer fra `requirements.txt` i stedet for individuelle pakker
   - Noen notebooks kan kreve tilleggspakker nevnt i markdown-cellene

4. **Azure-tjenester:**
   - Azure AI-tjenester krever aktivt abonnement
   - Noen funksjoner er regionspesifikke
   - Sørg for at din Azure OpenAI-modellutplassering støtter Responses API

### Læringsbane

Anbefalt progresjon gjennom leksjonene:
1. **00-course-setup** - Start her for miljøoppsett
2. **01-intro-to-ai-agents** - Forstå AI-agenters grunnprinsipper
3. **02-explore-agentic-frameworks** - Lær om forskjellige rammeverk
4. **03-agentic-design-patterns** - Kjerne-designmønstre
5. Fortsett gjennom nummererte leksjoner sekvensielt

### Rammeverksvalg

Velg rammeverk basert på dine mål:
- **Alle leksjoner**: Microsoft Agent Framework (MAF) med `FoundryChatClient`
- **Agenter registreres serverside** i Microsoft Foundry Agent Service V2 og er synlige i Foundry-portalen

### Få hjelp

- Bli med i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Les leksjons-README-filer for spesifikk veiledning
- Sjekk hoved-[README.md](./README.md) for kursoversikt
- Se [Course Setup](./00-course-setup/README.md) for detaljerte oppsettinstruksjoner

### Bidra

Dette er et åpent utdanningsprosjekt. Bidrag er velkomne:
- Forbedre kodeeksempler
- Rett opp skrivefeil eller feil
- Legg til forklarende kommentarer
- Foreslå nye leksjonstemaer
- Oversett til flere språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for nåværende behov.

## Prosjektrelatert kontekst

### Flerspråklig støtte

Dette depotet bruker et automatisert oversettelsessystem:
- Støtter 50+ språk
- Oversettelser i `/translations/<lang-code>/` mapper
- GitHub Actions-arbeidsflyt håndterer oversettelsesoppdateringer
- Kildefiler er på engelsk i depotets rot

### Leksjonsstruktur

Hver leksjon følger et konsistent mønster:
1. Video-miniature med lenke
2. Skriftlig leksjonsinnhold (README.md)
3. Kodeeksempler i flere rammeverk
4. Læringsmål og forutsetninger
5. Ekstra læringsressurser lenket

### Navngiving av kodeeksempler

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Leksjon 1, MAF Python
- `14-sequential.ipynb` - Leksjon 14, MAF avanserte mønstre
- `16-python-agent-framework.ipynb` - Leksjon 16, produksjons agent for kundestøtte
- `17-local-agent-foundry-local.ipynb` - Leksjon 17, lokal agent med Foundry Local + Qwen

### Spesielle mapper

- `translated_images/` - Lokale bilder for oversettelser
- `images/` - Originalbilder for engelsk innhold
- `.devcontainer/` - VS Code utviklingscontainerkonfigurasjon
- `.github/` - GitHub Actions arbeidsflyter og maler

### Avhengigheter

Nøkkelpakker fra `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-til-Agent protokollstøtte
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjenester
- `azure-identity` - Azure autentisering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search-integrasjon
- `mcp[cli]` - Model Context Protocol-støtte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->