# AGENTS.md

## Projektoversigt

Dette repository indeholder "AI Agents for begyndere" - et omfattende uddannelsesforløb, der lærer alt, hvad du behøver for at bygge AI-agenter. Kurset består af 15+ lektioner, der dækker grundlæggende principper, designmønstre, frameworks og produktionsimplementering af AI-agenter.

**Nøgle-teknologier:**
- Python 3.12+
- Jupyter Notebooks til interaktiv læring
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Arkitektur:**
- Lektion-baseret struktur (00-15+ mapper)
- Hver lektion indeholder: README-dokumentation, kodeeksempler (Jupyter notebooks) og billeder
- Flersproget support via automatiseret oversættelsessystem
- Én Python-notebook per lektion, der bruger Microsoft Agent Framework

## Opsætningskommandoer

### Forudsætninger
- Python 3.12 eller nyere
- Azure-abonnement (til Azure AI Foundry)
- Azure CLI installeret og autentificeret (`az login`)

### Første opsætning

1. **Klon eller fork repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Opret og aktiver Python virtuel miljø:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # På Windows: venv\Scripts\activate
   ```

3. **Installer afhængigheder:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Sæt miljøvariabler op:**
   ```bash
   cp .env.example .env
   # Rediger .env med dine API-nøgler og endpoints
   ```

### Påkrævede miljøvariabler

For **Azure AI Foundry** (påkrævet):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry projekt-endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model-deployments navn (fx gpt-4o)

For **Azure AI Search** (lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search-endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nøgle

Autentificering: Kør `az login` før kørsel af notebooks (bruger `AzureCliCredential`).

## Udviklingsworkflow

### Kørsel af Jupyter Notebooks

Hver lektion indeholder flere Jupyter notebooks for forskellige frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviger til en lektionsmappe** (fx `01-intro-to-ai-agents/code_samples/`)

3. **Åbn og kør notebooks:**
   - `*-python-agent-framework.ipynb` - Brug af Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Brug af Microsoft Agent Framework (.NET)

### Arbejde med Microsoft Agent Framework

**Microsoft Agent Framework + Azure AI Foundry:**
- Kræver Azure-abonnement
- Bruger `AzureAIProjectAgentProvider` til Agent Service V2 (agenter synlige i Foundry-portalen)
- Produktionsklar med indbygget observabilitet
- Filmønster: `*-python-agent-framework.ipynb`

## Testinstruktioner

Dette er et uddannelsesrepository med eksempel kode i stedet for produktionskode med automatiske tests. For at verificere din opsætning og ændringer:

### Manuel test

1. **Test Python-miljø:**
   ```bash
   python --version  # Skal være 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook-kørsel:**
   ```bash
   # Konverter notesbog til script og kør (tester imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verificer miljøvariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Kør individuelle notebooks

Åbn notebooks i Jupyter og udfør celler sekventielt. Hver notebook er selvstændig og inkluderer:
- Import-udsagn
- Konfigurationsindlæsning
- Eksempler på agent-implementeringer
- Forventede output i markdown-celler

## Kodestil

### Python-konventioner

- **Python-version**: 3.12+
- **Kodestil**: Følg standard Python PEP 8 konventioner
- **Notebooks**: Brug klare markdown-celler til at forklare koncepter
- **Imports**: Grupper efter standardbibliotek, tredjepart, lokale imports

### Jupyter Notebook-konventioner

- Inkluder beskrivende markdown-celler før kodeceller
- Tilføj output-eksempler i notebooks til reference
- Brug klare variabelnavne, der matcher lektionernes begreber
- Hold notebookens kørselsrækkefølge lineær (celle 1 → 2 → 3...)

### Filorganisation

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Byg og implementering

### Byg dokumentation

Dette repository bruger Markdown til dokumentation:
- README.md-filer i hver lektionsmappe
- Hoved-README.md i repository-roden
- Automatiseret oversættelsessystem via GitHub Actions

### CI/CD Pipeline

Findes i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversættelse til 50+ sprog
2. **welcome-issue.yml** - Byder nye issues velkommen
3. **welcome-pr.yml** - Byder nye pull request bidragydere velkommen

### Implementering

Dette er et uddannelsesrepository - ingen implementeringsproces. Brugere:
1. Fork eller klon repository
2. Kører notebooks lokalt eller i GitHub Codespaces
3. Lærer ved at modificere og eksperimentere med eksempler

## Pull Request Retningslinjer

### Før indsendelse

1. **Test dine ændringer:**
   - Kør berørte notebooks fuldt ud
   - Verificer, at alle celler kører uden fejl
   - Kontroller, at output er passende

2. **Dokumentationsopdateringer:**
   - Opdater README.md, hvis nye koncepter tilføjes
   - Tilføj kommentarer i notebooks til kompleks kode
   - Sørg for, at markdown-celler forklarer formålet

3. **Filændringer:**
   - Undgå at committe `.env`-filer (brug `.env.example`)
   - Commit ikke `venv/` eller `__pycache__/` mapper
   - Behold notebook-output, hvis de demonstrerer koncepter
   - Fjern midlertidige filer og backup notebooks (`*-backup.ipynb`)

### PR titel-format

Brug beskrivende titler:
- `[Lesson-XX] Tilføj nyt eksempel for <koncept>`
- `[Fix] Ret stavefejl i lesson-XX README`
- `[Update] Forbedr kodeeksempel i lesson-XX`
- `[Docs] Opdater opsætningsinstruktioner`

### Påkrævede tjek

- Notebooks skal køre uden fejl
- README-filer skal være klare og korrekte
- Følg eksisterende kode-mønstre i repository
- Oprethold konsistens med andre lektioner

## Yderligere noter

### Almindelige faldgruber

1. **Python versionsmismatch:**
   - Sørg for at bruge Python 3.12+
   - Nogle pakker kan ikke fungere med ældre versioner
   - Brug `python3 -m venv` for eksplicit at specificere Python-version

2. **Miljøvariabler:**
   - Opret altid `.env` ud fra `.env.example`
   - Commit ikke `.env` filen (den er i `.gitignore`)
   - GitHub token skal have passende tilladelser

3. **Pakke-konflikter:**
   - Brug et frisk virtuelt miljø
   - Installer fra `requirements.txt` frem for individuelle pakker
   - Nogle notebooks kræver ekstra pakker nævnt i deres markdown-celler

4. **Azure services:**
   - Azure AI services kræver aktivt abonnement
   - Nogle funktioner er regionsspecifikke
   - Gratis-lager begrænsninger gælder for GitHub-modeller

### Læringsvej

Anbefalet progression gennem lektioner:
1. **00-course-setup** - Start her for opsætning af miljø
2. **01-intro-to-ai-agents** - Forstå AI-agent grundprincipper
3. **02-explore-agentic-frameworks** - Lær om forskellige frameworks
4. **03-agentic-design-patterns** - Kerne designmønstre
5. Fortsæt gennem nummererede lektioner sekventielt

### Framework-valg

Vælg framework baseret på dine mål:
- **Alle lektioner**: Microsoft Agent Framework (MAF) med `AzureAIProjectAgentProvider`
- **Agenter registreres server-side** i Azure AI Foundry Agent Service V2 og er synlige i Foundry-portalen

### Få hjælp

- Deltag i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Gennemgå lektionernes README-filer for specifik vejledning
- Se hoved-[README.md](./README.md) for kursusoversigt
- Henvis til [Course Setup](./00-course-setup/README.md) for detaljerede opsætningsinstruktioner

### Bidrag

Dette er et åbent uddannelsesprojekt. Bidrag er velkomne:
- Forbedr kodeeksempler
- Ret stavefejl eller fejl
- Tilføj forklarende kommentarer
- Foreslå nye lektionsemner
- Oversæt til yderligere sprog

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for aktuelle behov.

## Projektspecifik kontekst

### Flersproget support

Dette repository bruger et automatiseret oversættelsessystem:
- 50+ sprog understøttet
- Oversættelser i `/translations/<lang-code>/` mapper
- GitHub Actions workflow håndterer oversættelsesopdateringer
- Kildefiler er på engelsk i repository-roden

### Lektionsstruktur

Hver lektion følger et ensartet mønster:
1. Video-thumbnail med link
2. Skrevet lektionsindhold (README.md)
3. Kodeeksempler i flere frameworks
4. Læringsmål og forudsætninger
5. Ekstra læringsressourcer linket

### Navngivning af kodeeksempler

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF avancerede mønstre

### Specielle mapper

- `translated_images/` - Lokalt oversatte billeder
- `images/` - Originale billeder til engelsk indhold
- `.devcontainer/` - VS Code udviklingscontainer konfiguration
- `.github/` - GitHub Actions workflows og skabeloner

### Afhængigheder

Vigtige pakker fra `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-til-Agent protokol support
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure autentificering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integration
- `mcp[cli]` - Model Context Protocol support

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->