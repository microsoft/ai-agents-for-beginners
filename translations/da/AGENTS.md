# AGENTS.md

## Projektoversigt

Dette repository indeholder "AI-agenter for begyndere" - et omfattende uddannelseskursus, der lærer alt, hvad der er nødvendigt for at bygge AI-agenter. Kurset består af 15+ lektioner, der dækker grundlæggende principper, designmønstre, frameworks og produktionsudrulning af AI-agenter.

**Nøgleteknologier:**
- Python 3.12+
- Jupyter Notebooks til interaktiv læring
- AI-frameworks: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI-tjenester: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (gratis niveau tilgængeligt)

**Arkitektur:**
- Lektion-baseret struktur (00-15+ mapper)
- Hver lektion indeholder: README-dokumentation, kodeeksempler (Jupyter Notebooks) og billeder
- Flersproget support via automatiseret oversættelsessystem
- Flere framework-muligheder pr. lektion (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Opsætningskommandoer

### Forudsætninger
- Python 3.12 eller nyere
- GitHub-konto (til GitHub Models - gratis niveau)
- Azure-abonnement (valgfrit, til Azure AI-tjenester)

### Initial opsætning

1. **Klon eller fork repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Opret og aktiver Python-virtuelt miljø:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Installer afhængigheder:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Opsæt miljøvariabler:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Påkrævede miljøvariabler

For **GitHub Models (gratis)**:
- `GITHUB_TOKEN` - Personlig adgangstoken fra GitHub

For **Azure AI-tjenester** (valgfrit):
- `PROJECT_ENDPOINT` - Azure AI Foundry projekt-endpoint
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API-nøgle
- `AZURE_OPENAI_ENDPOINT` - URL til Azure OpenAI endpoint
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Udrulningsnavn for chatmodel
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Udrulningsnavn for embeddings
- Yderligere Azure-konfiguration som vist i `.env.example`

## Udviklingsarbejdsgang

### Kørsel af Jupyter Notebooks

Hver lektion indeholder flere Jupyter Notebooks for forskellige frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Naviger til en lektionsmappe** (f.eks. `01-intro-to-ai-agents/code_samples/`)

3. **Åbn og kør notebooks:**
   - `*-semantic-kernel.ipynb` - Brug af Semantic Kernel framework
   - `*-autogen.ipynb` - Brug af AutoGen framework
   - `*-python-agent-framework.ipynb` - Brug af Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Brug af Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Brug af Azure AI Agent Service

### Arbejde med forskellige frameworks

**Semantic Kernel + GitHub Models:**
- Gratis niveau tilgængeligt med GitHub-konto
- Godt til læring og eksperimentering
- Filmønster: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Gratis niveau tilgængeligt med GitHub-konto
- Muligheder for multi-agent orkestrering
- Filmønster: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Nyeste framework fra Microsoft
- Tilgængelig i Python og .NET
- Filmønster: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Kræver Azure-abonnement
- Produktionsklare funktioner
- Filmønster: `*-azureaiagent.ipynb`

## Testinstruktioner

Dette er et uddannelsesrepository med eksempelkode frem for produktionskode med automatiserede tests. For at verificere din opsætning og ændringer:

### Manuel testning

1. **Test Python-miljø:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Test notebook-udførelse:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verificer miljøvariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Kørsel af individuelle notebooks

Åbn notebooks i Jupyter og udfør celler sekventielt. Hver notebook er selvstændig og inkluderer:
- Importerklæringer
- Konfigurationsindlæsning
- Eksempelimplementeringer af agenter
- Forventede outputs i markdown-celler

## Kodestil

### Python-konventioner

- **Python-version**: 3.12+
- **Kodestil**: Følg standard Python PEP 8-konventioner
- **Notebooks**: Brug klare markdown-celler til at forklare koncepter
- **Imports**: Grupper efter standardbibliotek, tredjepart, lokale imports

### Jupyter Notebook-konventioner

- Inkluder beskrivende markdown-celler før kodeceller
- Tilføj outputeksempler i notebooks som reference
- Brug klare variabelnavne, der matcher lektionskoncepter
- Hold notebook-udførelsesrækkefølgen lineær (celle 1 → 2 → 3...)

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

## Bygning og udrulning

### Bygning af dokumentation

Dette repository bruger Markdown til dokumentation:
- README.md-filer i hver lektionsmappe
- Hoved-README.md i repository-roden
- Automatiseret oversættelsessystem via GitHub Actions

### CI/CD-pipeline

Findes i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk oversættelse til 50+ sprog
2. **welcome-issue.yml** - Velkomst til nye issues
3. **welcome-pr.yml** - Velkomst til nye pull request-bidragydere

### Udrulning

Dette er et uddannelsesrepository - ingen udrulningsproces. Brugere:
1. Fork eller klon repository
2. Kør notebooks lokalt eller i GitHub Codespaces
3. Lær ved at modificere og eksperimentere med eksempler

## Retningslinjer for pull requests

### Før indsendelse

1. **Test dine ændringer:**
   - Kør de berørte notebooks fuldstændigt
   - Verificer, at alle celler udføres uden fejl
   - Tjek, at outputs er passende

2. **Opdater dokumentation:**
   - Opdater README.md, hvis du tilføjer nye koncepter
   - Tilføj kommentarer i notebooks for kompleks kode
   - Sørg for, at markdown-celler forklarer formålet

3. **Filændringer:**
   - Undgå at committe `.env`-filer (brug `.env.example`)
   - Commit ikke `venv/` eller `__pycache__/`-mapper
   - Behold notebook-outputs, når de demonstrerer koncepter
   - Fjern midlertidige filer og backup-notebooks (`*-backup.ipynb`)

### PR-titelformat

Brug beskrivende titler:
- `[Lesson-XX] Tilføj nyt eksempel for <koncept>`
- `[Fix] Ret stavefejl i lesson-XX README`
- `[Update] Forbedr kodeeksempel i lesson-XX`
- `[Docs] Opdater opsætningsinstruktioner`

### Påkrævede checks

- Notebooks skal udføres uden fejl
- README-filer skal være klare og præcise
- Følg eksisterende kodemønstre i repository
- Bevar konsistens med andre lektioner

## Yderligere noter

### Almindelige faldgruber

1. **Python-version mismatch:**
   - Sørg for, at Python 3.12+ bruges
   - Nogle pakker fungerer muligvis ikke med ældre versioner
   - Brug `python3 -m venv` til eksplicit at angive Python-version

2. **Miljøvariabler:**
   - Opret altid `.env` fra `.env.example`
   - Commit ikke `.env`-filen (den er i `.gitignore`)
   - GitHub-token skal have passende tilladelser

3. **Pakke-konflikter:**
   - Brug et nyt virtuelt miljø
   - Installer fra `requirements.txt` frem for individuelle pakker
   - Nogle notebooks kan kræve yderligere pakker nævnt i deres markdown-celler

4. **Azure-tjenester:**
   - Azure AI-tjenester kræver aktivt abonnement
   - Nogle funktioner er regionsspecifikke
   - Begrænsninger for gratis niveau gælder for GitHub Models

### Læringssti

Anbefalet progression gennem lektioner:
1. **00-course-setup** - Start her for miljøopsætning
2. **01-intro-to-ai-agents** - Forstå AI-agentens grundprincipper
3. **02-explore-agentic-frameworks** - Lær om forskellige frameworks
4. **03-agentic-design-patterns** - Centrale designmønstre
5. Fortsæt gennem nummererede lektioner sekventielt

### Framework-valg

Vælg framework baseret på dine mål:
- **Læring/Prototyping**: Semantic Kernel + GitHub Models (gratis)
- **Multi-agent systemer**: AutoGen
- **Nyeste funktioner**: Microsoft Agent Framework (MAF)
- **Produktionsudrulning**: Azure AI Agent Service

### Få hjælp

- Deltag i [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Gennemgå lektions-README-filer for specifik vejledning
- Tjek hoved-[README.md](./README.md) for kursusoversigt
- Se [Course Setup](./00-course-setup/README.md) for detaljerede opsætningsinstruktioner

### Bidrag

Dette er et åbent uddannelsesprojekt. Bidrag er velkomne:
- Forbedr kodeeksempler
- Ret stavefejl eller fejl
- Tilføj afklarende kommentarer
- Foreslå nye lektionsemner
- Oversæt til yderligere sprog

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) for aktuelle behov.

## Projekt-specifik kontekst

### Flersproget support

Dette repository bruger et automatiseret oversættelsessystem:
- 50+ understøttede sprog
- Oversættelser i `/translations/<lang-code>/`-mapper
- GitHub Actions workflow håndterer oversættelsesopdateringer
- Kildefiler er på engelsk i repository-roden

### Lektionstruktur

Hver lektion følger et konsistent mønster:
1. Videominiature med link
2. Skriftligt lektionsindhold (README.md)
3. Kodeeksempler i flere frameworks
4. Læringsmål og forudsætninger
5. Ekstra læringsressourcer linket

### Kodeeksempel-navngivning

Format: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Lektion 4, Semantic Kernel
- `07-autogen.ipynb` - Lektion 7, AutoGen
- `14-python-agent-framework.ipynb` - Lektion 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lektion 14, MAF .NET

### Specielle mapper

- `translated_images/` - Lokaliserede billeder til oversættelser
- `images/` - Originale billeder til engelsk indhold
- `.devcontainer/` - VS Code udviklingscontainer-konfiguration
- `.github/` - GitHub Actions workflows og skabeloner

### Afhængigheder

Nøglepakker fra `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen framework
- `semantic-kernel` - Semantic Kernel framework
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjenester
- `azure-search-documents` - Azure AI Search integration
- `chromadb` - Vektordatabase til RAG-eksempler
- `chainlit` - Chat UI framework
- `browser_use` - Browser-automatisering for agenter
- `mcp[cli]` - Model Context Protocol support
- `mem0ai` - Hukommelsesstyring for agenter

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.