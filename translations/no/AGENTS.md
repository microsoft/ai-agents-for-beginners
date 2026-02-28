# AGENTS.md

## Prosjektoversikt

Dette repositoriet inneholder "AI Agents for Beginners" - et omfattende utdanningskurs som lærer alt som trengs for å bygge AI-agenter. Kurset består av 15+ leksjoner som dekker det grunnleggende, designmønstre, rammeverk og produksjonsutrulling av AI-agenter.

**Nøkkelteknologier:**
- Python 3.12+
- Jupyter-notatbøker for interaktiv læring
- AI-rammeverk: Microsoft Agent Framework (MAF)
- Azure AI-tjenester: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkitektur:**
- Leksjonsbasert struktur (00-15+ directories)
- Hver leksjon inneholder: README-dokumentasjon, kodeeksempler (Jupyter-notatbøker), og bilder
- Flerspråklig støtte via automatisert oversettelsessystem
- Én Python-notatbok per leksjon som bruker Microsoft Agent Framework

## Oppsettkommandoer

### Forutsetninger
- Python 3.12 eller høyere
- Azure-abonnement (for Azure AI Foundry)
- Azure CLI installert og autentisert (`az login`)

### Initialt oppsett

1. **Klon eller fork depotet:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Opprett og aktiver Python-virtuelt miljø:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # På Windows: venv\Scripts\activate
   ```

3. **Installer avhengigheter:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Konfigurer miljøvariabler:**
   ```bash
   cp .env.example .env
   # Rediger .env med dine API-nøkler og endepunkter
   ```

### Nødvendige miljøvariabler

For **Azure AI Foundry** (påkrevd):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry prosjektendepunkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Navn på modellutrulling (f.eks. gpt-4o)

For **Azure AI Search** (Leksjon 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endepunkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nøkkel

Autentisering: Kjør `az login` før du kjører notatbøkene (bruker `AzureCliCredential`).

## Utviklingsarbeidsflyt

### Kjøre Jupyter-notatbøker

Hver leksjon inneholder flere Jupyter-notatbøker for ulike rammeverk:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviger til en leksjonsmappe** (f.eks. `01-intro-to-ai-agents/code_samples/`)

3. **Åpne og kjør notatbøker:**
   - `*-python-agent-framework.ipynb` - Bruke Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Bruke Microsoft Agent Framework (.NET)

### Arbeide med Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Krever Azure-abonnement
- Bruker `AzureAIProjectAgentProvider` for Agent Service V2 (agenter synlige i Foundry-portalen)
- Produksjonsklar med innebygd observabilitet
- Filnavnmønster: `*-python-agent-framework.ipynb`

## Testinstruksjoner

Dette er et utdanningsrepo med eksempel-kode fremfor produksjonskode med automatiserte tester. For å verifisere oppsettet og endringene dine:

### Manuell testing

1. **Test Python-miljøet:**
   ```bash
   python --version  # Bør være 3.12+
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

### Kjøre individuelle notatbøker

Åpne notatbøker i Jupyter og kjør cellene sekvensielt. Hver notatbok er selvstendig og inkluderer:
- Import-utsagn
- Lasting av konfigurasjon
- Eksempelimplementasjoner av agenter
- Forventede utdata i markdown-celler

## Kodestil

### Python-konvensjoner

- **Python-versjon**: 3.12+
- **Kodeformat**: Følg standard Python PEP 8-konvensjoner
- **Notatbøker**: Bruk klare markdown-celler for å forklare konsepter
- **Importer**: Gruppér etter standardbibliotek, tredjeparts- og lokale importer

### Konvensjoner for Jupyter-notatbøker

- Inkluder beskrivende markdown-celler før kodeceller
- Legg til eksempelutdata i notatbøkene for referanse
- Bruk tydelige variabelnavn som samsvarer med leksjonskonseptene
- Hold kjørerekkefølgen i notatbøkene lineær (celle 1 → 2 → 3...)

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

### Generering av dokumentasjon

Dette repositoriet bruker Markdown for dokumentasjon:
- README.md-filer i hver leksjonsmappe
- Hoved README.md i repoets rot
- Automatisert oversettelsessystem via GitHub Actions

### CI/CD-pipeline

Ligger i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversettelse til 50+ språk
2. **welcome-issue.yml** - Ønsker nye issue-opprettende velkommen
3. **welcome-pr.yml** - Ønsker nye pull request-bidragsytere velkommen

### Distribusjon

Dette er et utdanningsrepo - ingen distribusjonsprosess. Brukere:
1. Fork eller klon depotet
2. Kjør notatbøker lokalt eller i GitHub Codespaces
3. Lær ved å endre og eksperimentere med eksemplene

## Retningslinjer for pull requests

### Før innsending

1. **Test endringene dine:**
   - Kjør berørte notatbøker fullstendig
   - Bekreft at alle celler kjører uten feil
   - Sjekk at utdataene er passende

2. **Oppdateringer i dokumentasjon:**
   - Oppdater README.md hvis du legger til nye konsepter
   - Legg til kommentarer i notatbøkene for kompleks kode
   - Sørg for at markdown-celler forklarer formålet

3. **Filendringer:**
   - Unngå å comitte `.env`-filer (bruk `.env.example`)
   - Ikke comitte `venv/` eller `__pycache__/`-mapper
   - Behold notatbokutdata når de demonstrerer konsepter
   - Fjern midlertidige filer og backup-notatbøker (`*-backup.ipynb`)

### PR-tittelformat

Bruk beskrivende titler:
- `[Lesson-XX] Legg til nytt eksempel for <concept>`
- `[Fix] Korriger skrivefeil i lesson-XX README`
- `[Update] Forbedre kodeeksempel i lesson-XX`
- `[Docs] Oppdater oppsettsinstruksjoner`

### Påkrevde sjekker

- Notatbøker bør kjøre uten feil
- README-filer bør være klare og nøyaktige
- Følg eksisterende kodekonvensjoner i depotet
- Oppretthold konsistens med andre leksjoner

## Ytterligere merknader

### Vanlige fallgruver

1. **Uoverensstemmelse i Python-versjon:**
   - Sørg for at Python 3.12+ brukes
   - Noen pakker kan ikke fungere med eldre versjoner
   - Bruk `python3 -m venv` for å spesifisere Python-versjon eksplisitt

2. **Miljøvariabler:**
   - Opprett alltid `.env` fra `.env.example`
   - Ikke comitte `.env`-filen (den er i `.gitignore`)
   - GitHub-token trenger riktige tillatelser

3. **Pakke-konflikter:**
   - Bruk et nytt virtuelt miljø
   - Installer fra `requirements.txt` i stedet for individuelle pakker
   - Noen notatbøker kan kreve ekstra pakker nevnt i deres markdown-celler

4. **Azure-tjenester:**
   - Azure AI-tjenester krever aktivt abonnement
   - Noen funksjoner er regionsspesifikke
   - Begrensninger for gratisnivå gjelder for GitHub Models

### Læringssti

Anbefalt rekkefølge gjennom leksjonene:
1. **00-course-setup** - Start her for oppsett av miljøet
2. **01-intro-to-ai-agents** - Forstå grunnprinsippene for AI-agenter
3. **02-explore-agentic-frameworks** - Lær om forskjellige rammeverk
4. **03-agentic-design-patterns** - Kjerne designmønstre
5. Fortsett gjennom nummererte leksjoner i rekkefølge

### Valg av rammeverk

Velg rammeverk basert på dine mål:
- **Alle leksjoner**: Microsoft Agent Framework (MAF) med `AzureAIProjectAgentProvider`
- **Agenter registreres på serversiden** i Azure AI Foundry Agent Service V2 og er synlige i Foundry-portalen

### Få hjelp

- Bli med i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Gå gjennom leksjons-README-filer for spesifikk veiledning
- Sjekk hoved [README.md](./README.md) for kursoversikt
- Se [Course Setup](./00-course-setup/README.md) for detaljerte oppsettsinstruksjoner

### Bidra

Dette er et åpent utdanningsprosjekt. Bidrag ønskes:
- Forbedre kodeeksempler
- Rett opp skrivefeil eller feil
- Legg til forklarende kommentarer
- Foreslå nye leksjonsemner
- Oversett til flere språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for nåværende behov.

## Prosjektrelatert kontekst

### Flerspråklig støtte

Dette repositoriet bruker et automatisert oversettelsessystem:
- Støtte for 50+ språk
- Oversettelser i `/translations/<lang-code>/`-mapper
- GitHub Actions workflow håndterer oversettelsesoppdateringer
- Kildefiler er på engelsk i repository-roten

### Leksjonsstruktur

Hver leksjon følger et konsekvent mønster:
1. Videominiatyr med lenke
2. Skrevet leksjonsinnhold (README.md)
3. Kodeeksempler i flere rammeverk
4. Læringsmål og forutsetninger
5. Ekstra læringsressurser lenket

### Navngivning av kodeeksempler

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Leksjon 1, MAF Python
- `14-sequential.ipynb` - Leksjon 14, MAF avanserte mønstre

### Spesielle kataloger

- `translated_images/` - Lokaliserte bilder for oversettelser
- `images/` - Originale bilder for engelsk innhold
- `.devcontainer/` - VS Code development container-konfigurasjon
- `.github/` - GitHub Actions workflows og maler

### Avhengigheter

Viktige pakker fra `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Støtte for Agent-til-Agent-protokoll
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjenester
- `azure-identity` - Azure-autentisering (`AzureCliCredential`)
- `azure-search-documents` - Integrasjon med Azure AI Search
- `mcp[cli]` - Støtte for Model Context Protocol

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfraskrivelse:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet i sitt opprinnelige språk skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->