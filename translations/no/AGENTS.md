# AGENTS.md

## Project Overview

Dette depotet inneholder "AI Agents for Beginners" - et omfattende opplæringskurs som lærer alt som trengs for å bygge AI-agenter. Kurset består av 15+ leksjoner som dekker grunnleggende prinsipper, designmønstre, rammeverk og produksjonsutrulling av AI-agenter.

**Viktige teknologier:**
- Python 3.12+
- Jupyter-notatbøker for interaktiv læring
- AI-rammeverk: Microsoft Agent Framework (MAF)
- Azure AI-tjenester: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkitektur:**
- Leksjonsbasert struktur (00-15+ mapper)
- Hver leksjon inneholder: README-dokumentasjon, kodeeksempler (Jupyter-notatbøker) og bilder
- Flerspråklig støtte via automatisert oversettelsessystem
- Ett Python-notatark per leksjon som bruker Microsoft Agent Framework

## Setup Commands

### Prerequisites
- Python 3.12 eller nyere
- Azure-abonnement (for Azure AI Foundry)
- Azure CLI installert og autentisert (`az login`)

### Initial Setup

1. **Clone or fork the repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Create and activate Python virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # På Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Rediger .env med dine API-nøkler og endepunkter
   ```

### Required Environment Variables

For **Azure AI Foundry** (påkrevd):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (f.eks. gpt-4o)

For **Azure AI Search** (Leksjon 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Autentisering: Kjør `az login` før du kjører notatbøker (bruker `AzureCliCredential`).

## Development Workflow

### Running Jupyter Notebooks

Hver leksjon inneholder flere Jupyter-notatbøker for forskjellige rammeverk:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviger til en leksjonsmappe** (f.eks. `01-intro-to-ai-agents/code_samples/`)

3. **Åpne og kjør notatbøker:**
   - `*-python-agent-framework.ipynb` - Bruker Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Bruker Microsoft Agent Framework (.NET)

### Working with Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Krever Azure-abonnement
- Bruker `AzureAIProjectAgentProvider` for Agent Service V2 (agenter synlige i Foundry-portalen)
- Produksjonsklar med innebygd observabilitet
- Filnavnmønster: `*-python-agent-framework.ipynb`

## Testing Instructions

Dette er et pedagogisk depot med eksempelkode snarere enn produksjonskode med automatiserte tester. For å verifisere oppsettet og endringene dine:

### Manual Testing

1. **Test Python-miljøet:**
   ```bash
   python --version  # Bør være 3.12 eller nyere
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test kjøring av notatbøker:**
   ```bash
   # Konverter notatbok til skript og kjør (tester importene)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifiser miljøvariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Running Individual Notebooks

Åpne notatbøker i Jupyter og kjør cellene sekvensielt. Hver notatbok er selvstendig og inkluderer:
- Import-setninger
- Konfigurasjonslasting
- Eksempelimplementasjoner av agenter
- Forventede utdata i markdown-celler

## Code Style

### Python Conventions

- **Python-versjon**: 3.12+
- **Kode-stil**: Følg standard Python PEP 8-konvensjoner
- **Notatbøker**: Bruk klare markdown-celler for å forklare konsepter
- **Imports**: Grupper etter standardbibliotek, tredjeparts, lokale imports

### Jupyter Notebook Conventions

- Inkluder beskrivende markdown-celler før kodeceller
- Legg til eksempelutdata i notatbøkene som referanse
- Bruk klare variabelnavn som samsvarer med leksjonskonseptene
- Hold notatbokkjøringsrekkefølgen lineær (celle 1 → 2 → 3...)

### File Organization

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Build and Deployment

### Building Documentation

Dette depotet bruker Markdown for dokumentasjon:
- README.md filer i hver leksjonsmappe
- Hoved-README.md i repo-roten
- Automatisert oversettelsessystem via GitHub Actions

### CI/CD Pipeline

Ligger i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversettelse til 50+ språk
2. **welcome-issue.yml** - Ønsker nye issue-opprettelser velkommen
3. **welcome-pr.yml** - Ønsker nye pull request-bidragsytere velkommen

### Deployment

Dette er et pedagogisk depot - ingen deploy-prosess. Brukere:
1. Fork eller klon depotet
2. Kjør notatbøker lokalt eller i GitHub Codespaces
3. Lær ved å endre og eksperimentere med eksemplene

## Pull Request Guidelines

### Before Submitting

1. **Test endringene dine:**
   - Kjør berørte notatbøker helt igjennom
   - Verifiser at alle celler kjører uten feil
   - Sjekk at utdataene er passende

2. **Dokumentasjonsoppdateringer:**
   - Oppdater README.md hvis du legger til nye konsepter
   - Legg til kommentarer i notatbøker for kompleks kode
   - Forsikre deg om at markdown-celler forklarer formålet

3. **Filendringer:**
   - Unngå å commite `.env`-filer (bruk `.env.example`)
   - Ikke commite `venv/` eller `__pycache__/`-mapper
   - Behold notatbokutdata når de demonstrerer konsepter
   - Fjern midlertidige filer og backup-notatbøker (`*-backup.ipynb`)

### PR Title Format

Bruk beskrivende titler:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Required Checks

- Notatbøker bør kjøre uten feil
- README-filer bør være klare og nøyaktige
- Følg eksisterende kode-mønstre i depotet
- Oppretthold konsistens med andre leksjoner

## Additional Notes

### Common Gotchas

1. **Python-versjonsavvik:**
   - Sørg for at Python 3.12+ brukes
   - Noen pakker kan ikke fungere med eldre versjoner
   - Bruk `python3 -m venv` for å angi Python-versjon eksplisitt

2. **Miljøvariabler:**
   - Opprett alltid `.env` fra `.env.example`
   - Ikke commite `.env`-filen (den er i `.gitignore`)
   - GitHub-token trenger riktige tillatelser

3. **Pakke-konflikter:**
   - Bruk et nytt virtuelt miljø
   - Installer fra `requirements.txt` i stedet for enkeltpakker
   - Noen notatbøker kan kreve tilleggspakker nevnt i deres markdown-celler

4. **Azure-tjenester:**
   - Azure AI-tjenester krever aktivt abonnement
   - Noen funksjoner er region-spesifikke
   - Begrensninger for gratisnivå gjelder for GitHub Models

### Learning Path

Anbefalt progresjon gjennom leksjonene:
1. **00-course-setup** - Start her for miljøoppsett
2. **01-intro-to-ai-agents** - Forstå AI-agenters grunnprinsipper
3. **02-explore-agentic-frameworks** - Lær om forskjellige rammeverk
4. **03-agentic-design-patterns** - Kjerne-designmønstre
5. Fortsett gjennom nummererte leksjoner sekvensielt

### Framework Selection

Velg rammeverk basert på dine mål:
- **Alle leksjoner**: Microsoft Agent Framework (MAF) med `AzureAIProjectAgentProvider`
- **Agenter registreres server-side** i Azure AI Foundry Agent Service V2 og er synlige i Foundry-portalen

### Getting Help

- Bli med i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Gå gjennom leksjons-README-filer for spesifikk veiledning
- Sjekk hoved-[README.md](./README.md) for kursoversikt
- Se [Course Setup](./00-course-setup/README.md) for detaljert oppsettinstruksjon

### Contributing

Dette er et åpent pedagogisk prosjekt. Bidrag ønskes:
- Forbedre kodeeksempler
- Rett opp skrivefeil eller feil
- Legg til avklarende kommentarer
- Foreslå nye leksjonsemner
- Oversett til flere språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for nåværende behov.

## Project-Specific Context

### Multi-Language Support

Dette depotet bruker et automatisert oversettelsessystem:
- 50+ språk støttet
- Oversettelser i `/translations/<lang-code>/` mapper
- GitHub Actions workflow håndterer oversettelsesoppdateringer
- Kildefiler er på engelsk i repo-roten

### Lesson Structure

Hver leksjon følger et konsistent mønster:
1. Video-thumbnail med lenke
2. Skriftlig leksjonsinnhold (README.md)
3. Kodeeksempler i flere rammeverk
4. Læringsmål og forutsetninger
5. Ekstra læringsressurser lenket

### Code Sample Naming

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Leksjon 1, MAF Python
- `14-sequential.ipynb` - Leksjon 14, MAF avanserte mønstre

### Special Directories

- `translated_images/` - Lokaliserte bilder for oversettelser
- `images/` - Originale bilder for engelsk innhold
- `.devcontainer/` - VS Code development container-konfigurasjon
- `.github/` - GitHub Actions workflows og maler

### Dependencies

Nøkkelpakker fra `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protocol support
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjenester
- `azure-identity` - Azure-autentisering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search-integrasjon
- `mcp[cli]` - Model Context Protocol-støtte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfraskrivelse:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell, menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->