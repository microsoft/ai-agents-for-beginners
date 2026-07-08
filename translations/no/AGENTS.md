# AGENTS.md

## Prosjektoversikt

Dette depotet inneholder "AI-agenter for nybegynnere" - et omfattende utdanningskurs som lærer alt som trengs for å bygge AI-agenter. Kurset består av 18 leksjoner som dekker grunnleggende konsepter, designmønstre, rammeverk og produksjonsutplassering av AI-agenter.

**Nøkkelteknologier:**
- Python 3.12+
- Jupyter Notebooks for interaktiv læring
- AI-rammeverk: Microsoft Agent Framework (MAF)
- Azure AI-tjenester: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkitektur:**
- Leksjonsbasert struktur (00-15+ kataloger)
- Hver leksjon inneholder: README-dokumentasjon, kodeeksempler (Jupyter notebooks) og bilder
- Flerspråklig støtte via automatisert oversettelsessystem
- Ett Python-notatbok per leksjon som bruker Microsoft Agent Framework

## Oppsettskommandoer

### Forutsetninger
- Python 3.12 eller høyere
- Azure-abonnement (for Microsoft Foundry)
- Azure CLI installert og autentisert (`az login`)

### Initielt oppsett

1. **Klon eller fork depotet:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Opprett og aktiver Python virtuelt miljø:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # På Windows: venv\Scripts\activate
   ```

3. **Installer avhengigheter:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Sett opp miljøvariabler:**
   ```bash
   cp .env.example .env
   # Rediger .env med dine API-nøkler og endepunkter
   ```

### Nødvendige miljøvariabler

For **Microsoft Foundry** (påkrevd):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry prosjektendepunkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modellutplasseringsnavn (f.eks. gpt-4o)

For **Azure AI Search** (Leksjon 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endepunkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nøkkel

Autentisering: Kjør `az login` før du kjører notatbøker (bruker `AzureCliCredential`).

## Utviklingsarbeidsflyt

### Kjøre Jupyter Notebooks

Hver leksjon inneholder flere Jupyter-notatbøker for ulike rammeverk:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviger til en leksjonsmappe** (f.eks. `01-intro-to-ai-agents/code_samples/`)

3. **Åpne og kjør notatbøker:**
   - `*-python-agent-framework.ipynb` - Bruker Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Bruker Microsoft Agent Framework (.NET)

### Arbeide med Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Krever Azure-abonnement
- Bruker `FoundryChatClient` for Agent Service V2 (agenter synlig i Foundry-portalen)
- Produksjonsklar med innebygd observabilitet
- Filnavnmønster: `*-python-agent-framework.ipynb`

## Testinstruksjoner

Dette er et pedagogisk depot med eksempel kode i stedet for produksjonskode med automatiserte tester. For å verifisere oppsett og endringer:

### Manuell testing

1. **Test Python-miljøet:**
   ```bash
   python --version  # Bør være 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notatbokeksekvering:**
   ```bash
   # Konverter notatbok til skript og kjør (tester importeringer)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifiser miljøvariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Kjøre individuelle notatbøker

Åpne notatbøker i Jupyter og kjør celler sekvensielt. Hver notatbok er selvstendig og inneholder:
- Import-setninger
- Laste konfigurasjon
- Eksempelimplementasjoner av agenter
- Forventede utdata i markdown-celler

## Kodestil

### Python-konvensjoner

- **Python-versjon**: 3.12+
- **Kodestil**: Følg standard Python PEP 8-konvensjoner
- **Notatbøker**: Bruk klare markdown-celller for å forklare konsepter
- **Importer**: Grupper etter standardbibliotek, tredjepart, lokale importer

### Jupyter Notebook-konvensjoner

- Inkluder beskrivende markdown-celler før kodeceller
- Legg til utdataeksempler i notatbøker for referanse
- Bruk klare variabelnavn som samsvarer med leksjonskonsepter
- Hold notatbokeksekveringsrekkefølgen lineær (celle 1 → 2 → 3...)

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

## Bygg og distribusjon

### Bygge dokumentasjon

Dette depotet bruker Markdown for dokumentasjon:
- README.md-filer i hver leksjonsmappe
- Hoved README.md i depotrot
- Automatisk oversettelsessystem via GitHub Actions

### CI/CD Pipeline

Ligger i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversettelse til 50+ språk
2. **welcome-issue.yml** - Ønsker nye issues velkommen
3. **welcome-pr.yml** - Ønsker nye pull request-bidragsytere velkommen

### Distribusjon

Dette er et pedagogisk depot - ingen distribusjonsprosess. Brukere:
1. Fork eller klon depotet
2. Kjør notatbøker lokalt eller i GitHub Codespaces
3. Lær ved å modifisere og eksperimentere med eksempler

## Retningslinjer for Pull Requests

### Før innsending

1. **Test endringene dine:**
   - Kjør de berørte notatbøkene fullstendig
   - Verifiser at alle celler kjører uten feil
   - Sjekk at utdataene er passende

2. **Oppdater dokumentasjon:**
   - Oppdater README.md ved tillegg av nye konsepter
   - Legg til kommentarer i notatbøker for kompleks kode
   - Sørg for at markdown-celler forklarer formålet

3. **Filendringer:**
   - Unngå å committe `.env` filer (bruk `.env.example`)
   - Ikke commit `venv/` eller `__pycache__/` kataloger
   - Behold notatbokutdata når de demonstrerer konsepter
   - Fjern midlertidige filer og backup-notatbøker (`*-backup.ipynb`)

### PR Tittel-format

Bruk beskrivende titler:
- `[Lesson-XX] Legg til nytt eksempel for <concept>`
- `[Fix] Rett skrivefeil i leksjon-XX README`
- `[Update] Forbedre kodeeksempel i leksjon-XX`
- `[Docs] Oppdater oppsettinstruksjoner`

### Påkrevde kontroller

- Notatbøker skal kjøre uten feil
- README-filer skal være klare og presise
- Følg eksisterende kode mønstre i depotet
- Bevar konsistens med andre leksjoner

## Ytterligere notater

### Vanlige fallgruver

1. **Python-versjonsmismatch:**
   - Sørg for at Python 3.12+ brukes
   - Noen pakker fungerer ikke med eldre versjoner
   - Bruk `python3 -m venv` for å spesifisere Python-versjon eksplisitt

2. **Miljøvariabler:**
   - Lag alltid `.env` fra `.env.example`
   - Ikke commit `.env` filen (den er i `.gitignore`)
   - Logg inn med `az login` for nøkkelfri Entra ID-autentisering

3. **Pakkekonflikter:**
   - Bruk et ferskt virtuelt miljø
   - Installer fra `requirements.txt` i stedet for individuelle pakker
   - Noen notatbøker kan kreve ekstra pakker nevnt i deres markdown-celler

4. **Azure-tjenester:**
   - Azure AI-tjenester krever aktivt abonnement
   - Noen funksjoner er regionsspesifikke
   - Sørg for at din Azure OpenAI-modellutplassering støtter Responses API

### Læringsvei

Anbefalt progresjon gjennom leksjoner:
1. **00-course-setup** - Start her for miljøoppsett
2. **01-intro-to-ai-agents** - Forstå AI-agenters grunnprinsipper
3. **02-explore-agentic-frameworks** - Lær om ulike rammeverk
4. **03-agentic-design-patterns** - Kjerne designmønstre
5. Fortsett gjennom nummererte leksjoner sekvensielt

### Rammeverksvalg

Velg rammeverk basert på dine mål:
- **Alle leksjoner**: Microsoft Agent Framework (MAF) med `FoundryChatClient`
- **Agenter registrerer seg serverside** i Microsoft Foundry Agent Service V2 og er synlige i Foundry-portalen

### Få hjelp

- Bli med i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Se gjennom leksjonenes README-filer for spesifikk veiledning
- Sjekk hoved-README.md for kursoversikt
- Se [Course Setup](./00-course-setup/README.md) for detaljerte oppsettinstruksjoner

### Bidra

Dette er et åpent utdanningsprosjekt. Bidrag ønskes velkommen:
- Forbedre kodeeksempler
- Rett skrivefeil eller feil
- Legg til klargjørende kommentarer
- Foreslå nye leksjonstemaer
- Oversett til flere språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for aktuelle behov.

## Prosjektspesifikk kontekst

### Flerspråklig støtte

Dette depotet bruker et automatisert oversettelsessystem:
- Støtter 50+ språk
- Oversettelser i `/translations/<lang-code>/` kataloger
- GitHub Actions arbeidsflyt håndterer oversettelsesoppdateringer
- Kildefiler er på engelsk i depotets rot

### Leksjonsstruktur

Hver leksjon følger et konsistent mønster:
1. Videominiatyr med link
2. Skrevet leksjonsinnhold (README.md)
3. Kodeeksempler i flere rammeverk
4. Læringsmål og forutsetninger
5. Ekstra læringsressurser lenket

### Navngivning av kodeeksempler

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Leksjon 1, MAF Python
- `14-sequential.ipynb` - Leksjon 14, MAF avanserte mønstre

### Spesialkataloger

- `translated_images/` - Lokalisert bilder for oversettelser
- `images/` - Opprinnelige bilder for engelsk innhold
- `.devcontainer/` - VS Code utviklingscontainerkonfigurasjon
- `.github/` - GitHub Actions arbeidsflyter og maler

### Avhengigheter

Nøkkelpakker fra `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokollstøtte
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjenester
- `azure-identity` - Azure autentisering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integrasjon
- `mcp[cli]` - Model Context Protocol-støtte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->