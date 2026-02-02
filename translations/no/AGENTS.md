# AGENTS.md

## Prosjektoversikt

Dette repositoriet inneholder "AI-agenter for nybegynnere" - et omfattende kurs som lærer alt du trenger for å bygge AI-agenter. Kurset består av over 15 leksjoner som dekker grunnleggende konsepter, designmønstre, rammeverk og produksjonsimplementering av AI-agenter.

**Nøkkelteknologier:**
- Python 3.12+
- Jupyter Notebooks for interaktiv læring
- AI-rammeverk: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI-tjenester: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (gratisnivå tilgjengelig)

**Arkitektur:**
- Leksjonsbasert struktur (00-15+ kataloger)
- Hver leksjon inneholder: README-dokumentasjon, kodeeksempler (Jupyter Notebooks) og bilder
- Støtte for flere språk via automatisert oversettelsessystem
- Flere rammeverksalternativer per leksjon (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Oppsettskommandoer

### Forutsetninger
- Python 3.12 eller nyere
- GitHub-konto (for GitHub Models - gratisnivå)
- Azure-abonnement (valgfritt, for Azure AI-tjenester)

### Første oppsett

1. **Klon eller fork repositoriet:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Opprett og aktiver et Python-virtuelt miljø:**
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


### Nødvendige miljøvariabler

For **GitHub Models (gratisnivå):**
- `GITHUB_TOKEN` - Personlig tilgangstoken fra GitHub

For **Azure AI-tjenester** (valgfritt):
- `PROJECT_ENDPOINT` - Azure AI Foundry-prosjektendepunkt
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API-nøkkel
- `AZURE_OPENAI_ENDPOINT` - URL for Azure OpenAI-endepunkt
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Distribusjonsnavn for chat-modell
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Distribusjonsnavn for embeddings
- Ytterligere Azure-konfigurasjon som vist i `.env.example`

## Utviklingsarbeidsflyt

### Kjøre Jupyter Notebooks

Hver leksjon inneholder flere Jupyter Notebooks for ulike rammeverk:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviger til en leksjonskatalog** (f.eks. `01-intro-to-ai-agents/code_samples/`)

3. **Åpne og kjør notebooks:**
   - `*-semantic-kernel.ipynb` - Bruker Semantic Kernel-rammeverket
   - `*-autogen.ipynb` - Bruker AutoGen-rammeverket
   - `*-python-agent-framework.ipynb` - Bruker Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Bruker Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Bruker Azure AI Agent Service

### Arbeide med ulike rammeverk

**Semantic Kernel + GitHub Models:**
- Gratisnivå tilgjengelig med GitHub-konto
- Bra for læring og eksperimentering
- Filmønster: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Gratisnivå tilgjengelig med GitHub-konto
- Muligheter for multi-agent orkestrering
- Filmønster: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Nyeste rammeverk fra Microsoft
- Tilgjengelig i Python og .NET
- Filmønster: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Krever Azure-abonnement
- Produksjonsklare funksjoner
- Filmønster: `*-azureaiagent.ipynb`

## Testinstruksjoner

Dette er et utdanningsrepositorium med eksempelkode, ikke produksjonskode med automatiserte tester. For å verifisere oppsettet og endringene dine:

### Manuell testing

1. **Test Python-miljøet:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Test notebook-kjøring:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifiser miljøvariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```


### Kjøre individuelle notebooks

Åpne notebooks i Jupyter og kjør cellene sekvensielt. Hver notebook er selvstendig og inkluderer:
- Importsetninger
- Konfigurasjonslasting
- Eksempelimplementeringer av agenter
- Forventede utdata i markdown-celler

## Kodestil

### Python-konvensjoner

- **Python-versjon**: 3.12+
- **Kodestil**: Følg standard Python PEP 8-konvensjoner
- **Notebooks**: Bruk tydelige markdown-celler for å forklare konsepter
- **Imports**: Grupper etter standardbibliotek, tredjeparts, lokale imports

### Jupyter Notebook-konvensjoner

- Inkluder beskrivende markdown-celler før kodeceller
- Legg til utdataeksempler i notebooks som referanse
- Bruk tydelige variabelnavn som samsvarer med leksjonskonsepter
- Hold notebook-kjøringsrekkefølgen lineær (celle 1 → 2 → 3...)

### Filorganisering

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


## Bygging og implementering

### Bygge dokumentasjon

Dette repositoriet bruker Markdown for dokumentasjon:
- README.md-filer i hver leksjonsmappe
- Hoved-README.md i repositoriets rot
- Automatisert oversettelsessystem via GitHub Actions

### CI/CD-pipeline

Plassert i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversettelse til 50+ språk
2. **welcome-issue.yml** - Velkomstmelding til nye issues
3. **welcome-pr.yml** - Velkomstmelding til nye pull request-bidragsytere

### Implementering

Dette er et utdanningsrepositorium - ingen implementeringsprosess. Brukere:
1. Fork eller klon repositoriet
2. Kjør notebooks lokalt eller i GitHub Codespaces
3. Lær ved å modifisere og eksperimentere med eksempler

## Retningslinjer for pull requests

### Før innsending

1. **Test endringene dine:**
   - Kjør berørte notebooks fullstendig
   - Verifiser at alle celler kjører uten feil
   - Sjekk at utdataene er passende

2. **Oppdater dokumentasjon:**
   - Oppdater README.md hvis du legger til nye konsepter
   - Legg til kommentarer i notebooks for kompleks kode
   - Sørg for at markdown-celler forklarer formålet

3. **Filendringer:**
   - Unngå å committe `.env`-filer (bruk `.env.example`)
   - Ikke commit `venv/` eller `__pycache__/`-kataloger
   - Behold notebook-utdata når de demonstrerer konsepter
   - Fjern midlertidige filer og backup-notebooks (`*-backup.ipynb`)

### PR-titelformat

Bruk beskrivende titler:
- `[Lesson-XX] Legg til nytt eksempel for <konsept>`
- `[Fix] Rett skrivefeil i lesson-XX README`
- `[Update] Forbedre kodeeksempel i lesson-XX`
- `[Docs] Oppdater oppsettsinstruksjoner`

### Nødvendige kontroller

- Notebooks skal kjøre uten feil
- README-filer skal være klare og nøyaktige
- Følg eksisterende kodeoppsett i repositoriet
- Oppretthold konsistens med andre leksjoner

## Tilleggsnotater

### Vanlige utfordringer

1. **Python-versjonskonflikt:**
   - Sørg for at Python 3.12+ brukes
   - Noen pakker fungerer kanskje ikke med eldre versjoner
   - Bruk `python3 -m venv` for å spesifisere Python-versjon eksplisitt

2. **Miljøvariabler:**
   - Opprett alltid `.env` fra `.env.example`
   - Ikke commit `.env`-filen (den er i `.gitignore`)
   - GitHub-token trenger riktige tillatelser

3. **Pakke-konflikter:**
   - Bruk et nytt virtuelt miljø
   - Installer fra `requirements.txt` i stedet for individuelle pakker
   - Noen notebooks kan kreve ekstra pakker nevnt i deres markdown-celler

4. **Azure-tjenester:**
   - Azure AI-tjenester krever aktivt abonnement
   - Noen funksjoner er regionsspesifikke
   - Begrensninger gjelder for gratisnivået til GitHub Models

### Læringssti

Anbefalt progresjon gjennom leksjonene:
1. **00-course-setup** - Start her for miljøoppsett
2. **01-intro-to-ai-agents** - Forstå grunnleggende AI-agentkonsepter
3. **02-explore-agentic-frameworks** - Lær om ulike rammeverk
4. **03-agentic-design-patterns** - Kjerne-designmønstre
5. Fortsett gjennom nummererte leksjoner sekvensielt

### Rammeverksvalg

Velg rammeverk basert på dine mål:
- **Læring/prototyping**: Semantic Kernel + GitHub Models (gratis)
- **Multi-agent systemer**: AutoGen
- **Nyeste funksjoner**: Microsoft Agent Framework (MAF)
- **Produksjonsimplementering**: Azure AI Agent Service

### Få hjelp

- Bli med i [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Gå gjennom README-filer for spesifikke leksjoner
- Sjekk hoved-[README.md](./README.md) for kursoversikt
- Se [Course Setup](./00-course-setup/README.md) for detaljerte oppsettsinstruksjoner

### Bidra

Dette er et åpent utdanningsprosjekt. Bidrag er velkomne:
- Forbedre kodeeksempler
- Fikse skrivefeil eller feil
- Legge til avklarende kommentarer
- Foreslå nye leksjonstemaer
- Oversette til flere språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for aktuelle behov.

## Prosjektspesifikk kontekst

### Støtte for flere språk

Dette repositoriet bruker et automatisert oversettelsessystem:
- Støtte for 50+ språk
- Oversettelser i `/translations/<lang-code>/`-kataloger
- GitHub Actions-arbeidsflyt håndterer oversettelsesoppdateringer
- Kildefiler er på engelsk i repositoriets rot

### Leksjonsstruktur

Hver leksjon følger et konsistent mønster:
1. Videominiatyrbilde med lenke
2. Skriftlig leksjonsinnhold (README.md)
3. Kodeeksempler i flere rammeverk
4. Læringsmål og forutsetninger
5. Ekstra læringsressurser lenket

### Navngivning av kodeeksempler

Format: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Leksjon 4, Semantic Kernel
- `07-autogen.ipynb` - Leksjon 7, AutoGen
- `14-python-agent-framework.ipynb` - Leksjon 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Leksjon 14, MAF .NET

### Spesielle kataloger

- `translated_images/` - Lokaliserte bilder for oversettelser
- `images/` - Originale bilder for engelsk innhold
- `.devcontainer/` - VS Code-utviklingscontainerkonfigurasjon
- `.github/` - GitHub Actions-arbeidsflyter og maler

### Avhengigheter

Viktige pakker fra `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen-rammeverk
- `semantic-kernel` - Semantic Kernel-rammeverk
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjenester
- `azure-search-documents` - Integrasjon med Azure AI Search
- `chromadb` - Vektordatabase for RAG-eksempler
- `chainlit` - Chat UI-rammeverk
- `browser_use` - Nettleserautomatisering for agenter
- `mcp[cli]` - Støtte for Model Context Protocol
- `mem0ai` - Minnehåndtering for agenter

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.