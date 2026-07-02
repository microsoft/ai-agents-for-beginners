# AGENTS.md

## Prosjektoversikt

Dette repoet inneholder "AI-agenter for nybegynnere" - et omfattende utdanningskurs som lærer alt som trengs for å bygge AI-agenter. Kurset består av 18 leksjoner som dekker grunnleggende begreper, designmønstre, rammeverk og produksjonsutrulling av AI-agenter.

**Nøkkelteknologier:**
- Python 3.12+
- Jupyter Notebooks for interaktiv læring
- AI-rammeverk: Microsoft Agent Framework (MAF)
- Azure AI-tjenester: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkitektur:**
- Lekson-basert struktur (00-15+ mapper)
- Hver leksjon inneholder: README-dokumentasjon, kodeeksempler (Jupyter-notebooks) og bilder
- Flerspråklig støtte via automatisert oversettelsessystem
- Én Python-notatbok per leksjon som bruker Microsoft Agent Framework

## Oppsettskommandoer

### Forutsetninger
- Python 3.12 eller nyere
- Azure-abonnement (for Azure AI Foundry)
- Azure CLI installert og autentisert (`az login`)

### Første oppsett

1. **Klon eller fork repoet:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Lag og aktiver Python virtuelt miljø:**
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

For **Azure AI Foundry** (påkrevd):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry prosjektendepunkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modellutrullingsnavn (f.eks. gpt-4o)

For **Azure AI Search** (Leksjon 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endepunkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nøkkel

Autentisering: Kjør `az login` før du kjører notebooks (bruker `AzureCliCredential`).

## Utviklingsflyt

### Kjøre Jupyter Notebooks

Hver leksjon inneholder flere Jupyter notebooks for ulike rammeverk:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviger til en leksjonsmappe** (f.eks. `01-intro-to-ai-agents/code_samples/`)

3. **Åpne og kjør notebooks:**
   - `*-python-agent-framework.ipynb` - Bruker Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Bruker Microsoft Agent Framework (.NET)

### Arbeide med Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Krever Azure-abonnement
- Bruker `AzureAIProjectAgentProvider` for Agent Service V2 (agenter synlige i Foundry-portalen)
- Produksjonsklar med innebygd observabilitet
- Filnavnmønster: `*-python-agent-framework.ipynb`

## Testinstruksjoner

Dette er et utdanningsrepo med eksempel-kode, ikke produksjonskode med automatiserte tester. For å verifisere oppsett og endringer:

### Manuell testing

1. **Test Python-miljø:**
   ```bash
   python --version  # Bør være 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notatbokkjøring:**
   ```bash
   # Konverter notatbok til skript og kjør (tester importering)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifiser miljøvariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Kjøre individuelle notebooks

Åpne notebooks i Jupyter og kjør celler sekvensielt. Hver notebook er selvstendig og inkluderer:
- Import-setninger
- Laster konfigurasjon
- Eksempler på agent-implementasjoner
- Forventede utdata i markdown-celler

## Kodestil

### Python-konvensjoner

- **Python-versjon**: 3.12+
- **Kodestil**: Følg standard Python PEP 8 konvensjoner
- **Notebooks**: Bruk klare markdown-celler for å forklare konsepter
- **Imports**: Grupper etter standardbibliotek, tredjepart, lokale imports

### Jupyter Notebook-konvensjoner

- Inkluder beskrivende markdown-celler før kodeceller
- Legg til utdataeksempler i notebooks som referanse
- Bruk klare variabelnavn som matcher leksjonskonsepter
- Hold notebooks kjørerekkefølge lineær (celle 1 → 2 → 3...)

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

Dette repoet bruker Markdown for dokumentasjon:
- README.md filer i hver leksjonsmappe
- Hoved-README.md i repoets rot
- Automatisert oversettelsessystem via GitHub Actions

### CI/CD-pipeline

Ligger i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversettelse til 50+ språk
2. **welcome-issue.yml** - Ønsker nye issues velkommen
3. **welcome-pr.yml** - Ønsker nye pull requests velkommen

### Distribusjon

Dette er et utdanningsrepo - ingen distribusjonsprosess. Brukere:
1. Forker eller kloner repoet
2. Kjører notebooks lokalt eller i GitHub Codespaces
3. Lærer ved å modifisere og eksperimentere med eksempler

## Retningslinjer for Pull Requests

### Før innsending

1. **Test endringene dine:**
   - Kjør berørte notebooks helt ut
   - Bekreft at alle celler kjører uten feil
   - Sjekk at utdata er passende

2. **Oppdater dokumentasjon:**
   - Oppdater README.md ved nye konsepter
   - Legg til kommentarer i notebooks for kompleks kode
   - Sørg for at markdown-celler forklarer hensikten

3. **Filendringer:**
   - Unngå å committe `.env` filer (bruk `.env.example`)
   - Ikke commit `venv/` eller `__pycache__/` mapper
   - Behold notebook-utdata når de demonstrerer konsepter
   - Fjern midlertidige filer og backup notebooks (`*-backup.ipynb`)

### PR-tittelformat

Bruk beskrivende titler:
- `[Lesson-XX] Legg til nytt eksempel for <konsept>`
- `[Fix] Rett skrivefeil i lesson-XX README`
- `[Update] Forbedre kodeeksempel i lesson-XX`
- `[Docs] Oppdater oppsettsinstruksjoner`

### Nødvendige sjekker

- Notebooks må kjøre uten feil
- README-filer må være klare og korrekte
- Følg eksisterende kodekonvensjoner i repoet
- Oppretthold konsistens med andre leksjoner

## Tilleggsnotater

### Vanlige fallgruver

1. **Python-versjonskonflikt:**
   - Sørg for at Python 3.12+ brukes
   - Noen pakker fungerer ikke med eldre versjoner
   - Bruk `python3 -m venv` for å spesifisere versjon eksplisitt

2. **Miljøvariabler:**
   - Lag alltid `.env` fra `.env.example`
   - Ikke commit `.env` (er i `.gitignore`)
   - GitHub-token krever riktige tillatelser

3. **Pakke-konflikter:**
   - Bruk et ferskt virtuelt miljø
   - Installer fra `requirements.txt` i stedet for individuelle pakker
   - Noen notebooks krever ekstra pakker nevnt i markdown-celler

4. **Azure-tjenester:**
   - Azure AI-tjenester krever aktivt abonnement
   - Noen funksjoner er regionsspesifikke
   - Gratisnivå-grenser gjelder for GitHub Models

### Læringsvei

Anbefalt progresjon gjennom leksjoner:
1. **00-course-setup** - Start her for miljøoppsett
2. **01-intro-to-ai-agents** - Forstå AI-agenters grunnprinsipper
3. **02-explore-agentic-frameworks** - Lær om ulike rammeverk
4. **03-agentic-design-patterns** - Kjerne designmønstre
5. Fortsett gjennom nummererte leksjoner i rekkefølge

### Velge rammeverk

Velg rammeverk basert på dine mål:
- **Alle leksjoner**: Microsoft Agent Framework (MAF) med `AzureAIProjectAgentProvider`
- **Agenter registreres server-side** i Azure AI Foundry Agent Service V2 og er synlige i Foundry-portalen

### Få hjelp

- Bli med i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Se leksjons-README-filer for spesifikk veiledning
- Sjekk hoved-README.md for kursoversikt
- Referer til [Course Setup](./00-course-setup/README.md) for detaljert oppsettinstruksjoner

### Bidra

Dette er et åpent utdanningsprosjekt. Bidrag er velkomne:
- Forbedre kodeeksempler
- Rett opp skrivefeil eller feil
- Legg til forklarende kommentarer
- Foreslå nye leksjonsemner
- Oversett til flere språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for gjeldende behov.

## Prosjekt-spesifikk kontekst

### Flerspråklig støtte

Dette repoet bruker et automatisert oversettelsessystem:
- Støtter 50+ språk
- Oversettelser i `/translations/<lang-code>/` mapper
- GitHub Actions workflow håndterer oversettelsesoppdateringer
- Kildefiler er på engelsk i repoets rot

### Leksjonsstruktur

Hver leksjon følger et konsekvent mønster:
1. Videominiatyr med lenke
2. Skriftlig leksjonsinnhold (README.md)
3. Kodeeksempler i flere rammeverk
4. Læringsmål og forutsetninger
5. Ekstra læringsressurser lenket

### Navngiving av kodeeksempler

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Leksjon 1, MAF Python
- `14-sequential.ipynb` - Leksjon 14, MAF avanserte mønstre

### Spesielle mapper

- `translated_images/` - Lokalisert bilder for oversettelser
- `images/` - Originale bilder for engelsk innhold
- `.devcontainer/` - VS Code utviklingscontainer konfigurasjon
- `.github/` - GitHub Actions workflows og maler

### Avhengigheter

Nøkkelpakker fra `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokollstøtte
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjenester
- `azure-identity` - Azure autentisering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integrasjon
- `mcp[cli]` - Model Context Protocol støtte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->