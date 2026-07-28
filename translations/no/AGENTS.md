# AGENTS.md

## Prosjektoversikt

Dette depotet inneholder "AI-agenter for nybegynnere" - et omfattende utdanningskurs som lærer alt som trengs for å bygge AI-agenter. Kurset består av 18 leksjoner (nummerert 00-18) som dekker grunnleggende konsepter, designmønstre, rammeverk, produksjonsutrulling, lokale/enhetsbaserte agenter, og sikkerhet for AI-agenter.

**Nøkkelteknologier:**
- Python 3.12+
- Jupyter Notebooks for interaktiv læring
- AI-rammeverk: Microsoft Agent Framework (MAF)
- Azure AI-tjenester: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkitektur:**
- Leksjonsbasert struktur (mapper 00-15+)
- Hver leksjon inneholder: README-dokumentasjon, kodeeksempler (Jupyter-notebooks), og bilder
- Flerspråklig støtte via automatisert oversettelsessystem
- En Python-notebook per leksjon som bruker Microsoft Agent Framework

## Oppsettskommandoer

### Forutsetninger
- Python 3.12 eller nyere
- Azure-abonnement (for Microsoft Foundry)
- Azure CLI installert og autentisert (`az login`)

### Første oppsett

1. **Klon eller fork depotet:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Opprett og aktiver Python virtuell miljø:**
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

For **Microsoft Foundry** (nødvendig):
- `AZURE_AI_PROJECT_ENDPOINT` - Endepunktet for Microsoft Foundry-prosjektet
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modellutrullingsnavn (f.eks. gpt-5-mini)

For **Azure AI Search** (Leksjon 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search-endepunkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nøkkel

Autentisering: Kjør `az login` før du kjører notatbøkene (bruker `AzureCliCredential`).

## Utviklingsflyt

### Kjøring av Jupyter Notebooks

Hver leksjon inneholder flere Jupyter-notebooks for forskjellige rammeverk:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviger til en leksjonsmappe** (f.eks. `01-intro-to-ai-agents/code_samples/`)

3. **Åpne og kjør notatbøker:**
   - `*-python-agent-framework.ipynb` - Bruker Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Bruker Microsoft Agent Framework (.NET)

### Arbeid med Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Krever Azure-abonnement
- Bruker `FoundryChatClient` for Agent Service V2 (agenter synlige i Foundry-portalen)
- Produksjonsklar med innebygd observasjon
- Filnavnmønster: `*-python-agent-framework.ipynb`

## Testinstruksjoner

Dette er et utdanningsdepot med eksempel-kode, ikke produksjonskode med automatiske tester. For å verifisere oppsett og endringer:

### Manuell testing

1. **Test Python-miljø:**
   ```bash
   python --version  # Bør være 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test kjøring av notatbok:**
   ```bash
   # Konverter notatbok til skript og kjør (tester import)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifiser miljøvariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Kjøre individuelle notatbøker

Åpne notatbøker i Jupyter og kjør celler sekvensielt. Hver notatbok er selvstendig og inkluderer:
- Import-setninger
- Konfigurasjonslasting
- Eksempelimplementasjoner av agenter
- Forventede utganger i markdown-celler

### Røyk-testing av utrullede agenter

For leksjoner der en agent er utrullet som Microsoft Foundry-hostet agent (01, 04, 05, 16), leverer repoet røyk-testkataloger under `tests/` som kjøres av `.github/workflows/smoke-test.yml`-arbeidsflyten via [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)-handlingen. Dette er et lettvekts post-utrullingsfilter (er agenten tilgjengelig og følger grunnleggende promptforventninger?), som kompletterer evalueringsrøret i leksjonene 10 og 16. Se [tests/README.md](./tests/README.md) for kartleggingen katalog → leksjon → agent. Leksjon 17 kjøres lokalt med Foundry Local og har ikke et hostet endepunkt, så den valideres ved å kjøre sin notebook direkte.

## Kodepraksis

### Python-konvensjoner

- **Python-versjon**: 3.12+
- **Kodepraksis**: Følg standard Python PEP 8-konvensjoner
- **Notebooks**: Bruk klare markdown-celler for å forklare konsepter
- **Imports**: Grupper etter standardbibliotek, tredjepartsbiblioteker, lokale imports

### Jupyter Notebook-konvensjoner

- Inkluder beskrivende markdown-celler før kodeceller
- Legg til utgangseksempler i notatbøker som referanse
- Bruk klare variabelnavn som samsvarer med leksjonskonsepter
- Oppretthold lineær kjøringsrekkefølge (celle 1 → 2 → 3 ...)

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

## Bygging og Utrulling

### Bygge dokumentasjonen

Dette depotet bruker Markdown for dokumentasjon:
- README.md-filer i hver leksjonsmappe
- Hoved-README.md i depotets rotmappe
- Automatisert oversettelsessystem via GitHub Actions

### CI/CD-rørledning

Ligger i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversettelse til 50+ språk
2. **welcome-issue.yml** - Ønsker nye issues velkommen
3. **welcome-pr.yml** - Ønsker nye pull request-bidragsytere velkommen

### Utrulling

Dette er et utdanningsdepot - ingen utrullingsprosess. Brukere:
1. Fork eller klon depotet
2. Kjør notatbøker lokalt eller i GitHub Codespaces
3. Lær ved å modifisere og eksperimentere med eksemplene

## Retningslinjer for Pull Requests

### Før innsending

1. **Test endringene dine:**
   - Kjør berørte notatbøker fullstendig
   - Verifiser at alle celler kjører uten feil
   - Sjekk at utganger er passende

2. **Oppdater dokumentasjon:**
   - Oppdater README.md hvis nye konsepter legges til
   - Legg til kommentarer i notatbøker for kompleks kode
   - Sørg for at markdown-celler forklarer formålet

3. **Filendringer:**
   - Unngå å committe `.env`-filer (bruk `.env.example`)
   - Ikke commit `venv/` eller `__pycache__/` mapper
   - Behold notatbok-utganger når de demonstrerer konsepter
   - Fjern midlertidige filer og backup-notebooks (`*-backup.ipynb`)

### PR Tittel-format

Bruk beskrivende titler:
- `[Lesson-XX] Legg til nytt eksempel for <konsept>`
- `[Fix] Rett skrivefeil i lesson-XX README`
- `[Update] Forbedre kodeeksempel i lesson-XX`
- `[Docs] Oppdater oppsettsinstruksjoner`

### Obligatoriske sjekker

- Notatbøker skal kjøre uten feil
- README-filer skal være klare og nøyaktige
- Følg eksisterende kode-mønstre i depotet
- Oppretthold konsistens med andre leksjoner

## Ytterligere notater

### Vanlige fallgruver

1. **Python-versjonsfeil:**
   - Sørg for at Python 3.12+ brukes
   - Noen pakker fungerer kanskje ikke med eldre versjoner
   - Bruk `python3 -m venv` for å angi Python-versjon eksplisitt

2. **Miljøvariabler:**
   - Lag alltid `.env` fra `.env.example`
   - Ikke commit `.env`-filen (den er i `.gitignore`)
   - Logg inn med `az login` for nøkkelfri Entra ID-autentisering

3. **Pakke-konflikter:**
   - Bruk et nytt virtuelt miljø
   - Installer fra `requirements.txt` i stedet for individuelle pakker
   - Noen notatbøker kan kreve ekstra pakker nevnt i markdown-cellene sine

4. **Azure-tjenester:**
   - Azure AI-tjenester krever aktivt abonnement
   - Noen funksjoner er regionspesifikke
   - Sørg for at Azure OpenAI-modellutrullingen din støtter Responses API

### Læringsvei

Anbefalt progresjon gjennom leksjonene:
1. **00-course-setup** - Start her for oppsett av miljø
2. **01-intro-to-ai-agents** - Forstå grunnleggende AI-agentkonsepter
3. **02-explore-agentic-frameworks** - Lær om ulike rammeverk
4. **03-agentic-design-patterns** - Kjerne-designmønstre
5. Fortsett gjennom nummererte leksjoner sekvensielt

### Rammeverksvalg

Velg rammeverk basert på dine mål:
- **Alle leksjoner**: Microsoft Agent Framework (MAF) med `FoundryChatClient`
- **Agenter registreres serverside** i Microsoft Foundry Agent Service V2 og er synlige i Foundry-portalen

### Få hjelp

- Bli med i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Gå gjennom leksjons-README-filer for spesifikk veiledning
- Sjekk hoved-[README.md](./README.md) for kursoversikt
- Referer til [Course Setup](./00-course-setup/README.md) for detaljerte oppsettsinstruksjoner

### Bidra

Dette er et åpent utdanningsprosjekt. Bidrag er velkomne:
- Forbedre kodeeksempler
- Rett skrivefeil eller feil
- Legg til klargjørende kommentarer
- Foreslå nye leksjonstemaer
- Oversett til flere språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for nåværende behov.

## Prosjektspesifikk kontekst

### Flerspråklig støtte

Dette depotet bruker et automatisert oversettelsessystem:
- 50+ språk støttes
- Oversettelser i `/translations/<lang-code>/` mapper
- GitHub Actions-arbeidsflyt håndterer oppdatering av oversettelser
- Kildefiler er på engelsk i depotets rotmappe

### Leksjonsstruktur

Hver leksjon følger et konsekvent mønster:
1. Videominiatyr med lenke
2. Skriftlig leksjonsinnhold (README.md)
3. Kodeeksempler i flere rammeverk
4. Læringsmål og forutsetninger
5. Ekstra læringsressurser lenket

### Navngivning av kodeeksempler

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Leksjon 1, MAF Python
- `14-sequential.ipynb` - Leksjon 14, MAF avanserte mønstre
- `16-python-agent-framework.ipynb` - Leksjon 16, produksjonsagent for kundesupport
- `17-local-agent-foundry-local.ipynb` - Leksjon 17, lokal agent med Foundry Local + Qwen

### Spesielle mapper

- `translated_images/` - Lokalt oversatte bilder for oversettelser
- `images/` - Originalbilder for engelsk innhold
- `.devcontainer/` - VS Code utviklingscontainer-konfigurasjon
- `.github/` - GitHub Actions-arbeidsflyter og maler

### Avhengigheter

Nøkkelpakkene fra `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-til-Agent protokollstøtte
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjenester
- `azure-identity` - Azure-autentisering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search-integrasjon
- `mcp[cli]` - Model Context Protocol-støtte

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->