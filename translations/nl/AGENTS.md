# AGENTS.md

## Projectoverzicht

Deze repository bevat "AI Agents for Beginners" - een uitgebreide educatieve cursus die alles leert wat nodig is om AI Agents te bouwen. De cursus bestaat uit meer dan 15 lessen die de basisprincipes, ontwerpmodellen, frameworks en productie-implementatie van AI-agents behandelen.

**Belangrijke technologieën:**
- Python 3.12+
- Jupyter Notebooks voor interactief leren
- AI-frameworks: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI Services: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (gratis niveau beschikbaar)

**Architectuur:**
- Lesgebaseerde structuur (00-15+ mappen)
- Elke les bevat: README-documentatie, codevoorbeelden (Jupyter-notebooks) en afbeeldingen
- Meertalige ondersteuning via een geautomatiseerd vertaalsysteem
- Meerdere frameworkopties per les (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Installatiecommando's

### Vereisten
- Python 3.12 of hoger
- GitHub-account (voor GitHub Models - gratis niveau)
- Azure-abonnement (optioneel, voor Azure AI-services)

### Initiële installatie

1. **Kloon of fork de repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Maak en activeer een Python-virtuele omgeving:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Installeer afhankelijkheden:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Stel omgevingsvariabelen in:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Vereiste omgevingsvariabelen

Voor **GitHub Models (gratis)**:
- `GITHUB_TOKEN` - Persoonlijke toegangstoken van GitHub

Voor **Azure AI Services** (optioneel):
- `PROJECT_ENDPOINT` - Azure AI Foundry-projectendpoint
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API-sleutel
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI endpoint-URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Naam van de implementatie voor chatmodel
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Naam van de implementatie voor embeddings
- Aanvullende Azure-configuratie zoals weergegeven in `.env.example`

## Ontwikkelworkflow

### Jupyter Notebooks uitvoeren

Elke les bevat meerdere Jupyter-notebooks voor verschillende frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigeer naar een lesmap** (bijv. `01-intro-to-ai-agents/code_samples/`)

3. **Open en voer notebooks uit:**
   - `*-semantic-kernel.ipynb` - Gebruik van Semantic Kernel-framework
   - `*-autogen.ipynb` - Gebruik van AutoGen-framework
   - `*-python-agent-framework.ipynb` - Gebruik van Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Gebruik van Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Gebruik van Azure AI Agent Service

### Werken met verschillende frameworks

**Semantic Kernel + GitHub Models:**
- Gratis niveau beschikbaar met GitHub-account
- Geschikt voor leren en experimenteren
- Bestandspatroon: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Gratis niveau beschikbaar met GitHub-account
- Mogelijkheden voor multi-agent orkestratie
- Bestandspatroon: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Nieuwste framework van Microsoft
- Beschikbaar in Python en .NET
- Bestandspatroon: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Vereist Azure-abonnement
- Productieklaar met uitgebreide functies
- Bestandspatroon: `*-azureaiagent.ipynb`

## Testinstructies

Dit is een educatieve repository met voorbeeldcode in plaats van productiecode met geautomatiseerde tests. Om je installatie en wijzigingen te verifiëren:

### Handmatig testen

1. **Test de Python-omgeving:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Test de uitvoering van notebooks:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Controleer omgevingsvariabelen:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Individuele notebooks uitvoeren

Open notebooks in Jupyter en voer de cellen opeenvolgend uit. Elk notebook is zelfstandig en bevat:
- Importverklaringen
- Configuratie laden
- Voorbeeldimplementaties van agents
- Verwachte uitvoer in markdown-cellen

## Code Stijl

### Python-conventies

- **Python-versie**: 3.12+
- **Codestijl**: Volg standaard Python PEP 8-conventies
- **Notebooks**: Gebruik duidelijke markdown-cellen om concepten uit te leggen
- **Imports**: Groepeer op standaardbibliotheek, externe bibliotheken, lokale imports

### Jupyter Notebook-conventies

- Voeg beschrijvende markdown-cellen toe vóór codecellen
- Voeg uitvoervoorbeelden toe in notebooks ter referentie
- Gebruik duidelijke variabelenamen die overeenkomen met lesconcepten
- Houd de uitvoeringsvolgorde van notebooks lineair (cel 1 → 2 → 3...)

### Bestandsorganisatie

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

## Build en implementatie

### Documentatie bouwen

Deze repository gebruikt Markdown voor documentatie:
- README.md-bestanden in elke lesmap
- Hoofd-README.md in de root van de repository
- Geautomatiseerd vertaalsysteem via GitHub Actions

### CI/CD-pijplijn

Te vinden in `.github/workflows/`:

1. **co-op-translator.yml** - Automatische vertaling naar 50+ talen
2. **welcome-issue.yml** - Verwelkomt nieuwe issue-makers
3. **welcome-pr.yml** - Verwelkomt nieuwe pull request-bijdragers

### Implementatie

Dit is een educatieve repository - geen implementatieproces. Gebruikers:
1. Fork of kloon de repository
2. Voer notebooks lokaal of in GitHub Codespaces uit
3. Leer door voorbeelden te wijzigen en te experimenteren

## Richtlijnen voor pull requests

### Voor het indienen

1. **Test je wijzigingen:**
   - Voer de betreffende notebooks volledig uit
   - Controleer of alle cellen zonder fouten worden uitgevoerd
   - Controleer of de uitvoer correct is

2. **Documentatie-updates:**
   - Werk README.md bij als je nieuwe concepten toevoegt
   - Voeg opmerkingen toe in notebooks voor complexe code
   - Zorg ervoor dat markdown-cellen het doel uitleggen

3. **Bestandswijzigingen:**
   - Vermijd het committen van `.env`-bestanden (gebruik `.env.example`)
   - Commit geen `venv/` of `__pycache__/`-mappen
   - Houd notebook-uitvoer wanneer deze concepten demonstreert
   - Verwijder tijdelijke bestanden en back-up notebooks (`*-backup.ipynb`)

### PR-titelindeling

Gebruik beschrijvende titels:
- `[Lesson-XX] Voeg nieuw voorbeeld toe voor <concept>`
- `[Fix] Corrigeer typefout in les-XX README`
- `[Update] Verbeter codevoorbeeld in les-XX`
- `[Docs] Werk installatie-instructies bij`

### Vereiste controles

- Notebooks moeten zonder fouten worden uitgevoerd
- README-bestanden moeten duidelijk en accuraat zijn
- Volg bestaande codepatronen in de repository
- Zorg voor consistentie met andere lessen

## Aanvullende opmerkingen

### Veelvoorkomende valkuilen

1. **Python-versiemismatch:**
   - Zorg ervoor dat Python 3.12+ wordt gebruikt
   - Sommige pakketten werken mogelijk niet met oudere versies
   - Gebruik `python3 -m venv` om expliciet de Python-versie te specificeren

2. **Omgevingsvariabelen:**
   - Maak altijd `.env` aan vanuit `.env.example`
   - Commit geen `.env`-bestand (staat in `.gitignore`)
   - GitHub-token heeft de juiste machtigingen nodig

3. **Pakketconflicten:**
   - Gebruik een nieuwe virtuele omgeving
   - Installeer vanuit `requirements.txt` in plaats van individuele pakketten
   - Sommige notebooks vereisen aanvullende pakketten die in hun markdown-cellen worden vermeld

4. **Azure-services:**
   - Azure AI-services vereisen een actief abonnement
   - Sommige functies zijn regio-specifiek
   - Gratis niveaubeperkingen zijn van toepassing op GitHub Models

### Leerpad

Aanbevolen volgorde van lessen:
1. **00-course-setup** - Begin hier voor de installatie van de omgeving
2. **01-intro-to-ai-agents** - Begrijp de basisprincipes van AI-agents
3. **02-explore-agentic-frameworks** - Leer over verschillende frameworks
4. **03-agentic-design-patterns** - Kernontwerpmodellen
5. Ga verder met de genummerde lessen in volgorde

### Frameworkselectie

Kies een framework op basis van je doelen:
- **Leren/Prototypen**: Semantic Kernel + GitHub Models (gratis)
- **Multi-agent systemen**: AutoGen
- **Nieuwste functies**: Microsoft Agent Framework (MAF)
- **Productie-implementatie**: Azure AI Agent Service

### Hulp krijgen

- Word lid van de [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Bekijk de README-bestanden van lessen voor specifieke begeleiding
- Raadpleeg de hoofd-[README.md](./README.md) voor een cursusoverzicht
- Raadpleeg [Course Setup](./00-course-setup/README.md) voor gedetailleerde installatie-instructies

### Bijdragen

Dit is een open educatief project. Bijdragen zijn welkom:
- Verbeter codevoorbeelden
- Corrigeer typefouten of fouten
- Voeg verduidelijkende opmerkingen toe
- Stel nieuwe lesonderwerpen voor
- Vertaal naar extra talen

Zie [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) voor huidige behoeften.

## Projectspecifieke context

### Meertalige ondersteuning

Deze repository gebruikt een geautomatiseerd vertaalsysteem:
- Ondersteuning voor 50+ talen
- Vertalingen in `/translations/<lang-code>/`-mappen
- GitHub Actions workflow verwerkt vertaalupdates
- Bronbestanden zijn in het Engels in de root van de repository

### Lesstructuur

Elke les volgt een consistent patroon:
1. Videominiatuur met link
2. Geschreven lesinhoud (README.md)
3. Codevoorbeelden in meerdere frameworks
4. Leerdoelen en vereisten
5. Extra leermiddelen gelinkt

### Naamgeving van codevoorbeelden

Formaat: `<lesnummer>-<framework-naam>.ipynb`
- `04-semantic-kernel.ipynb` - Les 4, Semantic Kernel
- `07-autogen.ipynb` - Les 7, AutoGen
- `14-python-agent-framework.ipynb` - Les 14, MAF Python
- `14-dotnet-agent-framework.ipynb` - Les 14, MAF .NET

### Speciale mappen

- `translated_images/` - Gelokaliseerde afbeeldingen voor vertalingen
- `images/` - Originele afbeeldingen voor Engelse inhoud
- `.devcontainer/` - VS Code ontwikkelcontainerconfiguratie
- `.github/` - GitHub Actions workflows en sjablonen

### Afhankelijkheden

Belangrijke pakketten uit `requirements.txt`:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen-framework
- `semantic-kernel` - Semantic Kernel-framework
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI-services
- `azure-search-documents` - Integratie met Azure AI Search
- `chromadb` - Vector database voor RAG-voorbeelden
- `chainlit` - Chat UI-framework
- `browser_use` - Browserautomatisering voor agents
- `mcp[cli]` - Ondersteuning voor Model Context Protocol
- `mem0ai` - Geheugenbeheer voor agents

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.