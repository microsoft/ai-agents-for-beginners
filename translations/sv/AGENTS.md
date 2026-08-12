# AGENTS.md

## Projektöversikt

Detta arkiv innehåller "AI-agenter för nybörjare" - en omfattande utbildningskurs som lär ut allt som behövs för att bygga AI-agenter. Kursen består av 18 lektioner (numrerade 00-18) som täcker grunder, designmönster, ramverk, produktionsdistribution, lokala/enhetsbaserade agenter och säkerhet för AI-agenter.

**Nyckelteknologier:**
- Python 3.12+
- Jupyter Notebooks för interaktivt lärande
- AI-ramverk: Microsoft Agent Framework (MAF)
- Azure AI-tjänster: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Arkitektur:**
- Lektion-baserad struktur (00-15+ kataloger)
- Varje lektion innehåller: README-dokumentation, kodexempel (Jupyter notebooks), och bilder
- Flerspråkigt stöd via automatiserat översättningssystem
- En Python-notebook per lektion som använder Microsoft Agent Framework

## Installationskommandon

### Förutsättningar
- Python 3.12 eller högre
- Azure-prenumeration (för Microsoft Foundry)
- Azure CLI installerat och autentiserat (`az login`)

### Initial installation

1. **Klona eller forka arkivet:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # ELLER
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Skapa och aktivera Python virtuell miljö:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # På Windows: venv\Scripts\activate
   ```

3. **Installera beroenden:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ställ in miljövariabler:**
   ```bash
   cp .env.example .env
   # Redigera .env med dina API-nycklar och slutpunkter
   ```

### Obligatoriska miljövariabler

För **Microsoft Foundry** (Obligatoriskt):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry-projektendpunkt
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modellimplementeringsnamn (t.ex. gpt-5-mini)

För **Azure AI Search** (Lektion 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search-endpunkt
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-nyckel

Autentisering: Kör `az login` innan du kör notebooks (använder `AzureCliCredential`).

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
- Produktionsredo med inbyggd observerbarhet
- Filnamnsmönster: `*-python-agent-framework.ipynb`

## Testinstruktioner

Detta är ett utbildningsarkiv med exempel på kod snarare än produktionskod med automatiserade tester. För att verifiera din installation och ändringar:

### Manuell testning

1. **Testa Python-miljön:**
   ```bash
   python --version  # Bör vara 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Testa körning av notebook:**
   ```bash
   # Konvertera anteckningsbok till skript och kör (testar importer)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifiera miljövariabler:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Köra enskilda notebooks

Öppna notebooks i Jupyter och kör celler sekventiellt. Varje notebook är självständig och innehåller:
- Import-satser
- Konfigurationsladdning
- Exempel på agentimplementationer
- Förväntade utdata i markdown-celler

### Röktestning av distribuerade agenter

För lektioner där en agent är distribuerad som en Microsoft Foundry-hostad agent (01, 04, 05, 16) innehåller repo röktestkataloger under `tests/` som körs av `.github/workflows/smoke-test.yml` arbetsflödet via [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) åtgärden. Dessa fungerar som en lättviktig post-distributionsgrind (är agenten nåbar och följer grundläggande promptförväntningar?), som kompletterar utvärderingspipelinjen i Lektion 10 och 16. Se [tests/README.md](./tests/README.md) för kartläggning katalog-till-lektion-till-agent. Lektion 17 körs lokalt med Foundry Local och har ingen hostad endpunkt, så den valideras genom att köra dess notebook direkt.

## Kodstil

### Python-konventioner

- **Python-version**: 3.12+
- **Kodstil**: Följ standard Python PEP 8-konventioner
- **Notebooks**: Använd tydliga markdown-celler för att förklara koncept
- **Imports**: Gruppera standardbibliotek, tredjeparts- och lokala imports

### Jupyter Notebook-konventioner

- Inkludera beskrivande markdown-celler före kodceller
- Lägg till exempel på utdata i notebooks för referens
- Använd tydliga variabelnamn som matchar lektionskoncept
- Håll notebook-körningsordningen linjär (cell 1 → 2 → 3...)

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

## Bygg och Distribution

### Bygga dokumentation

Detta arkiv använder Markdown för dokumentation:
- README.md-filer i varje lektionsmapp
- Huvudsaklig README.md i arkivroten
- Automatiserat översättningssystem via GitHub Actions

### CI/CD-pipeline

Belägen i `.github/workflows/`:

1. **co-op-translator.yml** - Automatisk översättning till 50+ språk
2. **welcome-issue.yml** - Välkomnar nya issueskapare
3. **welcome-pr.yml** - Välkomnar nya pull request-bidragsgivare

### Distribution

Detta är ett utbildningsarkiv - ingen distributionsprocess. Användare:
1. Fork eller klona arkivet
2. Kör notebooks lokalt eller i GitHub Codespaces
3. Lär dig genom att modifiera och experimentera med exempel

## Riktlinjer för pull requests

### Innan du skickar in

1. **Testa dina ändringar:**
   - Kör berörda notebooks komplett
   - Verifiera att alla celler kör utan fel
   - Kontrollera att utdata är lämpliga

2. **Dokumentationsuppdateringar:**
   - Uppdatera README.md om nya koncept läggs till
   - Lägg till kommentarer i notebooks för komplex kod
   - Säkerställ att markdown-celler förklarar syftet

3. **Filändringar:**
   - Undvik att committa `.env` filer (använd `.env.example`)
   - Commita inte `venv/` eller `__pycache__/` kataloger
   - Behåll notebook-utdata när de demonstrerar koncept
   - Ta bort temporära filer och backup-notebooks (`*-backup.ipynb`)

### PR-titelformat

Använd beskrivande titlar:
- `[Lesson-XX] Lägg till nytt exempel för <concept>`
- `[Fix] Korrigera stavfel i lesson-XX README`
- `[Update] Förbättra kodexempel i lesson-XX`
- `[Docs] Uppdatera installationsinstruktioner`

### Obligatoriska kontroller

- Notebooks ska köras utan fel
- README-filer ska vara tydliga och korrekta
- Följ existerande kodmönster i arkivet
- Behåll konsistens med andra lektioner

## Ytterligare anteckningar

### Vanliga fallgropar

1. **Python version mismatch:**
   - Säkerställ att Python 3.12+ används
   - Vissa paket fungerar inte med äldre versioner
   - Använd `python3 -m venv` för att specificera Python-version explicit

2. **Miljövariabler:**
   - Skapa alltid `.env` från `.env.example`
   - Committra inte `.env` filen (den finns i `.gitignore`)
   - Logga in med `az login` för nyckellös Entra ID-autentisering

3. **Paketkonflikter:**
   - Använd en fräsch virtuell miljö
   - Installera från `requirements.txt` istället för enskilda paket
   - Vissa notebooks kan kräva ytterligare paket, nämnda i deras markdown-celler

4. **Azure-tjänster:**
   - Azure AI-tjänster kräver aktiv prenumeration
   - Vissa funktioner är regionsspecifika
   - Säkerställ att din Azure OpenAI-modellimplementering stödjer Responses API

### Inlärningsväg

Rekommenderad progression genom lektionerna:
1. **00-course-setup** - Börja här för miljöinställning
2. **01-intro-to-ai-agents** - Förstå grunderna för AI-agenter
3. **02-explore-agentic-frameworks** - Lär dig om olika ramverk
4. **03-agentic-design-patterns** - Kärndesignmönster
5. Fortsätt genom numrerade lektioner i ordning

### Val av ramverk

Välj ramverk baserat på dina mål:
- **Alla lektioner**: Microsoft Agent Framework (MAF) med `FoundryChatClient`
- **Agenter registreras server-side** i Microsoft Foundry Agent Service V2 och syns i Foundry-portalen

### Skaffa hjälp

- Gå med i [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Granska lektions-READMEs för specifik vägledning
- Kolla huvud-[README.md](./README.md) för kursöversikt
- Se [Course Setup](./00-course-setup/README.md) för detaljerade installationsinstruktioner

### Bidra

Detta är ett öppet utbildningsprojekt. Bidrag välkomnas:
- Förbättra kodexempel
- Rätta stavfel eller fel
- Lägg till förtydligande kommentarer
- Föreslå nya lektionsteman
- Översätt till ytterligare språk

Se [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) för aktuella behov.

## Projektspecifik kontext

### Flerspråkigt stöd

Detta arkiv använder ett automatiserat översättningssystem:
- 50+ språk stöds
- Översättningar i `/translations/<lang-code>/` kataloger
- GitHub Actions-arbetsflöde hanterar översättningsuppdateringar
- Källfiler är på engelska i arkivroten

### Lektionsstruktur

Varje lektion följer ett konsekvent mönster:
1. Video-miniature med länk
2. Skrivet lektionsinnehåll (README.md)
3. Kodexempel i flera ramverk
4. Läromål och förutsättningar
5. Ytterligare lärresurser länkade

### Namngivning av kodexempel

Format: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Lektion 1, MAF Python
- `14-sequential.ipynb` - Lektion 14, MAF avancerade mönster
- `16-python-agent-framework.ipynb` - Lektion 16, produktionsagent för kundsupport
- `17-local-agent-foundry-local.ipynb` - Lektion 17, lokal agent med Foundry Local + Qwen

### Specialkataloger

- `translated_images/` - Lokaliserade bilder för översättningar
- `images/` - Originalbilder för engelskt innehåll
- `.devcontainer/` - VS Code utvecklingscontainerskonfiguration
- `.github/` - GitHub Actions arbetsflöden och mallar

### Beroenden

Nyckelpaket från `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokollstöd
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-tjänster
- `azure-identity` - Azure autentisering (AzureCliCredential)
- `azure-search-documents` - Azure AI Search-integration
- `mcp[cli]` - Model Context Protocol-stöd

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->