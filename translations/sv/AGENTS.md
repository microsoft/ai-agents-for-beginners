# AGENTS.md

## Projektöversikt

Detta arkiv innehåller "AI-agenter för nybörjare" - en omfattande utbildningskurs som lär ut allt som behövs för att bygga AI-agenter. Kursen består av 15+ lektioner som täcker grunderna, designmönster, ramverk och produktionsimplementering av AI-agenter.

**Nyckelteknologier:**
- Python 3.12+
- Jupyter Notebooks för interaktivt lärande
- AI-ramverk: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI-tjänster: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (gratisnivå tillgänglig)

**Arkitektur:**
- Lektionbaserad struktur (00-15+ kataloger)
- Varje lektion innehåller: README-dokumentation, kodexempel (Jupyter-notebooks) och bilder
- Fler språk stöds via ett automatiserat översättningssystem
- Flera ramverksalternativ per lektion (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Installationskommandon

### Förutsättningar
- Python 3.12 eller högre
- GitHub-konto (för GitHub Models - gratisnivå)
- Azure-prenumeration (valfritt, för Azure AI-tjänster)

### Initial installation

1. **Klona eller forka arkivet:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Skapa och aktivera en virtuell Python-miljö:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Installera beroenden:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ställ in miljövariabler:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Nödvändiga miljövariabler

För **GitHub Models (gratis)**:
- `GITHUB_TOKEN` - Personlig åtkomsttoken från GitHub

För **Azure AI-tjänster** (valfritt):
- `PROJECT_ENDPOINT` - Azure AI Foundry-projektets slutpunkt
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API-nyckel
- `AZURE_OPENAI_ENDPOINT` - URL för Azure OpenAI-slutpunkt
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Distributionsnamn för chattmodellen
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Distributionsnamn för inbäddningar
- Ytterligare Azure-konfiguration som visas i `.env.example`

## Utvecklingsarbetsflöde

### Köra Jupyter-notebooks

Varje lektion innehåller flera Jupyter-notebooks för olika ramverk:

1. **Starta Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigera till en lektionskatalog** (t.ex. `01-intro-to-ai-agents/code_samples/`)

3. **Öppna och kör notebooks:**
   - `*-semantic-kernel.ipynb` - Använder Semantic Kernel-ramverket
   - `*-autogen.ipynb` - Använder AutoGen-ramverket
   - `*-python-agent-framework.ipynb` - Använder Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Använder Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Använder Azure AI Agent Service

### Arbeta med olika ramverk

**Semantic Kernel + GitHub Models:**
- Gratisnivå tillgänglig med GitHub-konto
- Bra för lärande och experimentering
- Filmönster: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Gratisnivå tillgänglig med GitHub-konto
- Kapacitet för multi-agent orkestrering
- Filmönster: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Senaste ramverket från Microsoft
- Tillgängligt i Python och .NET
- Filmönster: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Kräver Azure-prenumeration
- Produktionsklara funktioner
- Filmönster: `*-azureaiagent.ipynb`

## Testinstruktioner

Detta är ett utbildningsarkiv med exempel på kod snarare än produktionskod med automatiserade tester. För att verifiera din installation och ändringar:

### Manuell testning

1. **Testa Python-miljön:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Testa notebook-körning:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifiera miljövariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Köra enskilda notebooks

Öppna notebooks i Jupyter och kör cellerna sekventiellt. Varje notebook är fristående och inkluderar:
- Importsatser
- Konfigurationsladdning
- Exempel på agentimplementeringar
- Förväntade utdata i markdown-celler

## Kodstil

### Python-konventioner

- **Python-version**: 3.12+
- **Kodstil**: Följ standarden Python PEP 8
- **Notebooks**: Använd tydliga markdown-celler för att förklara koncept
- **Imports**: Gruppera efter standardbibliotek, tredjepartsbibliotek, lokala imports

### Jupyter Notebook-konventioner

- Inkludera beskrivande markdown-celler före kodceller
- Lägg till exempel på utdata i notebooks som referens
- Använd tydliga variabelnamn som matchar lektionskoncept
- Håll notebook-körningsordningen linjär (cell 1 → 2 → 3...)

### Filorganisation

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

## Bygg och distribution

### Bygga dokumentation

Detta arkiv använder Markdown för dokumentation:
- README.md-filer i varje lektionsmapp
- Huvud-README.md i arkivets rot
- Automatiserat översättningssystem via GitHub Actions

### CI/CD-pipeline

Finns i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk översättning till 50+ språk
2. **welcome-issue.yml** - Välkomnar nya ärendeskapare
3. **welcome-pr.yml** - Välkomnar nya pull request-bidragsgivare

### Distribution

Detta är ett utbildningsarkiv - ingen distributionsprocess. Användare:
1. Forka eller klona arkivet
2. Kör notebooks lokalt eller i GitHub Codespaces
3. Lär dig genom att modifiera och experimentera med exempel

## Riktlinjer för pull requests

### Innan du skickar in

1. **Testa dina ändringar:**
   - Kör de påverkade notebooks helt
   - Verifiera att alla celler körs utan fel
   - Kontrollera att utdata är lämpliga

2. **Uppdateringar av dokumentation:**
   - Uppdatera README.md om nya koncept läggs till
   - Lägg till kommentarer i notebooks för komplex kod
   - Se till att markdown-celler förklarar syftet

3. **Filändringar:**
   - Undvik att committa `.env`-filer (använd `.env.example`)
   - Commita inte `venv/` eller `__pycache__/`-kataloger
   - Behåll notebook-utdata när de demonstrerar koncept
   - Ta bort temporära filer och backup-notebooks (`*-backup.ipynb`)

### PR-titelformat

Använd beskrivande titlar:
- `[Lesson-XX] Lägg till nytt exempel för <koncept>`
- `[Fix] Korrigera stavfel i lesson-XX README`
- `[Update] Förbättra kodexempel i lesson-XX`
- `[Docs] Uppdatera installationsinstruktioner`

### Obligatoriska kontroller

- Notebooks ska köras utan fel
- README-filer ska vara tydliga och korrekta
- Följ befintliga kodmönster i arkivet
- Behåll konsekvens med andra lektioner

## Ytterligare anteckningar

### Vanliga fallgropar

1. **Python-version mismatch:**
   - Se till att Python 3.12+ används
   - Vissa paket kanske inte fungerar med äldre versioner
   - Använd `python3 -m venv` för att specificera Python-version explicit

2. **Miljövariabler:**
   - Skapa alltid `.env` från `.env.example`
   - Commita inte `.env`-filen (den är i `.gitignore`)
   - GitHub-token behöver lämpliga behörigheter

3. **Paketkonflikter:**
   - Använd en ny virtuell miljö
   - Installera från `requirements.txt` istället för enskilda paket
   - Vissa notebooks kan kräva ytterligare paket som nämns i deras markdown-celler

4. **Azure-tjänster:**
   - Azure AI-tjänster kräver aktiv prenumeration
   - Vissa funktioner är regionsspecifika
   - Begränsningar för gratisnivå gäller för GitHub Models

### Lärandebana

Rekommenderad progression genom lektionerna:
1. **00-course-setup** - Börja här för miljöinställning
2. **01-intro-to-ai-agents** - Förstå grunderna i AI-agenter
3. **02-explore-agentic-frameworks** - Lär dig om olika ramverk
4. **03-agentic-design-patterns** - Kärndesignmönster
5. Fortsätt genom numrerade lektioner i ordning

### Ramverksval

Välj ramverk baserat på dina mål:
- **Lärande/Prototyping**: Semantic Kernel + GitHub Models (gratis)
- **Multi-agent system**: AutoGen
- **Senaste funktioner**: Microsoft Agent Framework (MAF)
- **Produktionsdistribution**: Azure AI Agent Service

### Få hjälp

- Gå med i [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Granska README-filer för specifik vägledning
- Kontrollera huvud-[README.md](./README.md) för kursöversikt
- Se [Course Setup](./00-course-setup/README.md) för detaljerade installationsinstruktioner

### Bidra

Detta är ett öppet utbildningsprojekt. Bidrag välkomnas:
- Förbättra kodexempel
- Rätta stavfel eller fel
- Lägg till förtydligande kommentarer
- Föreslå nya lektionsämnen
- Översätt till fler språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) för aktuella behov.

## Projekt-specifik kontext

### Fler språk stöds

Detta arkiv använder ett automatiserat översättningssystem:
- 50+ språk stöds
- Översättningar i `/translations/<lang-code>/`-kataloger
- GitHub Actions-arbetsflöde hanterar översättningsuppdateringar
- Källfiler är på engelska i arkivets rot

### Lektionsstruktur

Varje lektion följer ett konsekvent mönster:
1. Videominiatyr med länk
2. Skrivet lektionsinnehåll (README.md)
3. Kodexempel i flera ramverk
4. Lärandemål och förutsättningar
5. Extra läranderesurser länkade

### Namngivning av kodexempel

Format: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - Lektion 4, Semantic Kernel
- `07-autogen.ipynb` - Lektion 7, AutoGen
- `14-python-agent-framework.ipynb` - Lektion 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Lektion 14, MAF .NET

### Speciella kataloger

- `translated_images/` - Lokaliserade bilder för översättningar
- `images/` - Originalbilder för engelskt innehåll
- `.devcontainer/` - VS Code-konfiguration för utvecklingsmiljö
- `.github/` - GitHub Actions-arbetsflöden och mallar

### Beroenden

Viktiga paket från `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen-ramverk
- `semantic-kernel` - Semantic Kernel-ramverk
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjänster
- `azure-search-documents` - Azure AI Search-integration
- `chromadb` - Vektordatabas för RAG-exempel
- `chainlit` - Chat UI-ramverk
- `browser_use` - Webbläsarautomatisering för agenter
- `mcp[cli]` - Stöd för Model Context Protocol
- `mem0ai` - Minneshantering för agenter

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.