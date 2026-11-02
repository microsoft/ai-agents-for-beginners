# AGENTS.md

## Projektöversikt

Detta arkiv innehåller "AI Agents for Beginners" - en omfattande utbildningskurs som lär ut allt som behövs för att bygga AI-agenter. Kursen består av 18 lektioner (numrerade 00-18) som täcker grunder, designmönster, ramverk, produktionsdistribution, lokala/enhetsagenter och säkerhet för AI-agenter.

**Nyckelteknologier:**
- Python 3.12+
- Jupyter Notebooks för interaktivt lärande
- AI-ramverk: Microsoft Agent Framework (MAF)
- Azure AI-tjänster: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkitektur:**
- Lektionbaserad struktur (00-18 kataloger)
- Varje lektion innehåller: README-dokumentation, kodexempel (Jupyter-notebooks) och bilder
- Flerspråkigt stöd via automatiserat översättningssystem
- En Python-notebook per lektion som använder Microsoft Agent Framework

## Installationskommandon

### Förutsättningar
- Python 3.12 eller högre
- Azure-prenumeration (för Microsoft Foundry)
- Azure CLI installerat och autentiserat (`az login`)

### Initial installation

1. **Klona eller fork:a arkivet:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Skapa och aktivera Python virtuellt miljö:**
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

### Obligatoriska miljövariabler

För **Microsoft Foundry** (obligatoriskt):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projektendpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modellutplaceringsnamn (t.ex. gpt-5-mini)

För **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nyckel

Autentisering: Kör `az login` före körning av notebooks (använder `AzureCliCredential`).

## Utvecklingsarbetsflöde

### Köra Jupyter Notebooks

Varje lektion innehåller flera Jupyter notebooks för olika ramverk:

1. **Starta Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigera till en lektionskatalog** (t.ex. `01-intro-to-ai-agents/code_samples/`)

3. **Öppna och kör notebooks:**
   - `*-python-agent-framework.ipynb` - Använder Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Använder Microsoft Agent Framework (.NET)

### Arbeta med Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Kräver Azure-prenumeration
- Använder `FoundryChatClient` för Agent Service V2 (agenter synliga i Foundry-portalen)
- Produktionsredo med inbyggd observabilitet
- Filnamnsmönster: `*-python-agent-framework.ipynb`

## Testinstruktioner

Detta är ett utbildningsarkiv med exempel på kod snarare än produktionskod med automatiska tester. För att verifiera din installation och ändringar:

### Manuell testning

1. **Testa Python-miljö:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testa körning av notebook:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifiera miljövariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Köra enskilda notebooks

Öppna notebooks i Jupyter och kör celler sekventiellt. Varje notebook är fristående och innehåller:
- Importuttalanden
- Konfigurationsladdning
- Exempel på agentimplementationer
- Förväntade resultat i markdown-celler

### Röktester av distribuerade agenter

För lektioner där en agent distribueras som en Microsoft Foundry värdagent (01, 04, 05, 16), levererar repot röktestkataloger under `tests/` som körs av `.github/workflows/smoke-test.yml` arbetsflödet via [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) action. Dessa är en lättviktig post-distributionskontroll (är agenten nåbar och följer grundläggande promptförväntningar?), som kompletterar utvärderingspipelinjen i Lektion 10 och 16. Se [tests/README.md](./tests/README.md) för katalog-till-lektion-till-agent mappning. Lektion 17 körs lokalt med Foundry Local och har ingen värdendpoint, så den valideras genom att köra sin notebook direkt.

## Kodstil

### Python-konventioner

- **Pythonversion**: 3.12+
- **Kodstil**: Följ standard PEP 8-konventioner för Python
- **Notebooks**: Använd tydliga markdown-celler för att förklara koncept
- **Importeringar**: Gruppera efter standardbibliotek, tredjepartsbibliotek och lokala importeringar

### Jupyter Notebook-konventioner

- Inkludera beskrivande markdown-celler före kodceller
- Lägg till exempel på utdata i notebooks som referens
- Använd tydliga variabelnamn som matchar lektionskoncept
- Håll ordningen på notebook-exekvering linjär (cell 1 → 2 → 3...)

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

## Bygg och distribution

### Bygga dokumentation

Detta arkiv använder Markdown för dokumentation:
- README.md-filer i varje lektionsmapp
- Huvud-README.md i arkivets rot
- Automatiskt översättningssystem via GitHub Actions

### CI/CD-pipeline

Belägen i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk översättning till 50+ språk
2. **welcome-issue.yml** - Välkomnar nya ärendeskapare
3. **welcome-pr.yml** - Välkomnar nya pull request-bidragsgivare

### Distribution

Detta är ett utbildningsarkiv - ingen distributionsprocess. Användare:
1. Fork:a eller klona arkivet
2. Kör notebooks lokalt eller i GitHub Codespaces
3. Lär genom att modifiera och experimentera med exempel

## Riktlinjer för pull requests

### Innan inlämning

1. **Testa dina ändringar:**
   - Kör berörda notebooks helt
   - Verifiera att alla celler körs utan fel
   - Kontrollera att utdata är lämpliga

2. **Uppdatera dokumentation:**
   - Uppdatera README.md om nya koncept läggs till
   - Lägg till kommentarer i notebooks för komplex kod
   - Säkerställ att markdown-celler förklarar syftet

3. **Filändringar:**
   - Undvik att committa `.env` filer (använd `.env.example`)
   - Commita inte `venv/` eller `__pycache__/` kataloger
   - Behåll notebook-utdata när de demonstrerar koncept
   - Ta bort temporära filer och backup-notebooks (`*-backup.ipynb`)

### Format för PR-titel

Använd beskrivande titlar:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Obligatoriska kontroller

- Notebooks ska köras utan fel
- README-filer ska vara tydliga och korrekta
- Följ befintliga kodmönster i arkivet
- Håll konsekvens med andra lektioner

## Ytterligare anteckningar

### Vanliga fallgropar

1. **Pythonversionsmissanpassning:**
   - Säkerställ att Python 3.12+ används
   - Vissa paket fungerar kanske inte med äldre versioner
   - Använd `python3 -m venv` för att explicit ange Python-version

2. **Miljövariabler:**
   - Skapa alltid `.env` från `.env.example`
   - Commita inte `.env` fil (den finns i `.gitignore`)
   - Logga in med `az login` för nyckellös Entra ID-autentisering

3. **Paketkonflikter:**
   - Använd en ren virtuell miljö
   - Installera från `requirements.txt` snarare än enstaka paket
   - Vissa notebooks kan kräva ytterligare paket som nämns i deras markdown-celler

4. **Azure-tjänster:**
   - Azure AI-tjänster kräver aktiv prenumeration
   - Vissa funktioner är regionsspecifika
   - Säkerställ att din Azure OpenAI-modellutplacering stödjer Responses API

### Läroväg

Rekommenderad progression genom lektionerna:
1. **00-course-setup** - Starta här för miljöinstallation
2. **01-intro-to-ai-agents** - Förstå AI-agenters grunder
3. **02-explore-agentic-frameworks** - Lär dig om olika ramverk
4. **03-agentic-design-patterns** - Kärndesignmönster
5. Fortsätt genom numrerade lektioner i ordning

### Ramverksval

Välj ramverk baserat på dina mål:
- **Alla lektioner**: Microsoft Agent Framework (MAF) med `FoundryChatClient`
- **Agenter registrerar sig server-side** i Microsoft Foundry Agent Service V2 och syns i Foundry-portalen

### Få hjälp

- Gå med i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Granska lektions-README-filer för specifik vägledning
- Kolla huvud-[README.md](./README.md) för kursöversikt
- Se [Course Setup](./00-course-setup/README.md) för detaljerade installationsinstruktioner

### Bidra

Detta är ett öppet utbildningsprojekt. Bidrag välkomnas:
- Förbättra kodexempel
- Rätta stavfel eller felaktigheter
- Lägg till förtydligande kommentarer
- Föreslå nya lektionsämnen
- Översätt till fler språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) för aktuella behov.

## Projekt-specifik kontext

### Flerspråkigt stöd

Detta arkiv använder ett automatiserat översättningssystem:
- 50+ språk stöds
- Översättningar i `/translations/<lang-code>/` kataloger
- GitHub Actions-arbetsflöde hanterar översättningsuppdateringar
- Källfilerna är på engelska i arkivets rot

### Lektionsstruktur

Varje lektion följer ett konsekvent mönster:
1. Videominiatyr med länk
2. Skrivet lektionsinnehåll (README.md)
3. Kodexempel i flera ramverk
4. Lärandemål och förutsättningar
5. Extra lärresurser länkade

### Namngivning av kodexempel

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF avancerade mönster
- `16-python-agent-framework.ipynb` - Lektion 16, produktionsagent för kundsupport
- `17-local-agent-foundry-local.ipynb` - Lektion 17, lokal agent med Foundry Local + Qwen

### Specialkataloger

- `translated_images/` - Lokalt anpassade bilder för översättningar
- `images/` - Originalbilder för engelskt innehåll
- `.devcontainer/` - VS Code utvecklingscontainerkonfiguration
- `.github/` - GitHub Actions arbetsflöden och mallar

### Beroenden

Nyckelpaket från `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-till-agent protokollstöd
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjänster
- `azure-identity` - Azure-autentisering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search-integration
- `mcp[cli]` - Model Context Protocol-stöd

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->