# AGENTS.md

## Projectoverzicht

Deze repository bevat "AI Agents voor Beginners" - een uitgebreide educatieve cursus die alles leert wat nodig is om AI Agents te bouwen. De cursus bestaat uit 18 lessen (genummerd 00-18) over fundamenten, ontwerppatronen, frameworks, productie-implementatie, lokale/on-device agents en beveiliging van AI agents.

**Belangrijkste Technologieën:**
- Python 3.12+
- Jupyter Notebooks voor interactief leren
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architectuur:**
- Lesgebaseerde structuur (00-18 mappen)
- Elke les bevat: README documentatie, codevoorbeelden (Jupyter notebooks), en afbeeldingen
- Meertalige ondersteuning via geautomatiseerd vertaalsysteem
- Eén Python notebook per les met Microsoft Agent Framework

## Setup Commando's

### Vereisten
- Python 3.12 of hoger
- Azure abonnement (voor Microsoft Foundry)
- Azure CLI geïnstalleerd en geauthenticeerd (`az login`)

### Eerste Setup

1. **Clone of fork de repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Maak en activeer de Python virtuele omgeving:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Installeer afhankelijkheden:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configureer omgevingsvariabelen:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Vereiste Omgevingsvariabelen

Voor **Microsoft Foundry** (Vereist):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Naam van model-implementatie (bijv. gpt-5-mini)

Voor **Azure AI Search** (Les 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Authenticatie: Voer `az login` uit voordat je de notebooks draait (maakt gebruik van `AzureCliCredential`).

## Ontwikkelworkflow

### Jupyter Notebooks draaien

Elke les bevat meerdere Jupyter notebooks voor verschillende frameworks:

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Navigeer naar een lesmap** (bijv. `01-intro-to-ai-agents/code_samples/`)

3. **Open en voer notebooks uit:**
   - `*-python-agent-framework.ipynb` - Met Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Met Microsoft Agent Framework (.NET)

### Werken met Microsoft Agent Framework

**Microsoft Agent Framework + Microsoft Foundry:**
- Vereist Azure abonnement
- Gebruikt `FoundryChatClient` voor Agent Service V2 (agents zichtbaar in Foundry portal)
- Productieklaar met ingebouwde observability
- Bestandsnaam patroon: `*-python-agent-framework.ipynb`

## Testinstructies

Dit is een educatieve repository met voorbeeldcode in plaats van productiecode met geautomatiseerde tests. Om je setup en wijzigingen te verifiëren:

### Handmatig Testen

1. **Test Python omgeving:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebook uitvoering:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifieer omgevingsvariabelen:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Individuele Notebooks Draaien

Open notebooks in Jupyter en voer cellen achtereenvolgens uit. Elke notebook is zelfstandig en bevat:
- Import statements
- Configuratie laden
- Voorbeeldagent implementaties
- Verwachte outputs in markdown cellen

### Smoke-Testing van Geïmplementeerde Agents

Voor lessen waar een agent is geïmplementeerd als Microsoft Foundry hosted agent (01, 04, 05, 16), bevat de repo smoke-test catalogi onder `tests/` die worden uitgevoerd door de `.github/workflows/smoke-test.yml` workflow via de [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) actie. Dit is een lichte post-implementatiepoort (is de agent bereikbaar en voldoet hij aan basis promptverwachtingen?), als aanvulling op de evaluatiepijplijn in Lessen 10 en 16. Zie [tests/README.md](./tests/README.md) voor de catalogus-naar-les-naar-agent mapping. Les 17 draait lokaal met Foundry Local en heeft geen hosted endpoint, dus wordt deze gevalideerd door het notebook direct uit te voeren.

## Code Stijl

### Python Conventies

- **Python Versie**: 3.12+
- **Code Stijl**: Volg standaard Python PEP 8 conventies
- **Notebooks**: Gebruik duidelijke markdown cellen om concepten uit te leggen
- **Imports**: Groepeer naar standaardbibliotheek, derde-partij, lokale imports

### Jupyter Notebook Conventies

- Voeg beschrijvende markdown cellen toe vóór codecellen
- Voeg uitvoervoorbeelden toe in notebooks ter referentie
- Gebruik duidelijke variabelnamen die aansluiten bij lesconcepten
- Houd de uitvoering van notebooks lineair (cel 1 → 2 → 3...)

### Bestandsorganisatie

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Bouw en Implementatie

### Documentatie Bouwen

Deze repository gebruikt Markdown voor documentatie:
- README.md bestanden in elke lesmap
- Hoofd README.md in repository root
- Geautomatiseerd vertaalsysteem via GitHub Actions

### CI/CD Pipeline

Gelegen in `.github/workflows/`:

1. **co-op-translator.yml** - Automatische vertaling naar 50+ talen
2. **welcome-issue.yml** - Verwelkomt nieuwe issue-makers
3. **welcome-pr.yml** - Verwelkomt nieuwe pull request bijdragers

### Implementatie

Dit is een educatieve repository - geen implementatieproces. Gebruikers:
1. Forken of clonen de repository
2. Draaien notebooks lokaal of in GitHub Codespaces
3. Leren door voorbeelden te wijzigen en experimenteren

## Richtlijnen voor Pull Requests

### Voor het Indienen

1. **Test je wijzigingen:**
   - Voer volledig de aangedane notebooks uit
   - Verifieer dat alle cellen zonder fouten draaien
   - Controleer dat outputs passend zijn

2. **Documentatie updates:**
   - Werk README.md bij als je nieuwe concepten toevoegt
   - Voeg commentaar toe in notebooks voor complexe code
   - Zorg dat markdown cellen het doel uitleggen

3. **Bestandswijzigingen:**
   - Vermijd het committen van `.env` bestanden (gebruik `.env.example`)
   - Commit geen `venv/` of `__pycache__/` mappen
   - Behoud notebook outputs waar ze concepten demonstreren
   - Verwijder tijdelijke bestanden en backup notebooks (`*-backup.ipynb`)

### PR Titel Formaat

Gebruik beschrijvende titels:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Vereiste Checks

- Notebooks moeten foutloos uitvoeren
- README bestanden moeten duidelijk en accuraat zijn
- Volg bestaande codepatronen in de repository
- Houd consistentie met andere lessen

## Aanvullende Notities

### Veelvoorkomende Valstrikken

1. **Mismatch Python versie:**
   - Gebruik Python 3.12+ gegarandeerd
   - Sommige pakketten werken niet met oudere versies
   - Gebruik `python3 -m venv` om de Python versie expliciet te specificeren

2. **Omgevingsvariabelen:**
   - Maak altijd `.env` vanuit `.env.example`
   - Commit het `.env` bestand niet (staat in `.gitignore`)
   - Meld je aan met `az login` voor sleutelvrije Entra ID authenticatie

3. **Pakketconflicten:**
   - Gebruik een schone virtuele omgeving
   - Installeer uit `requirements.txt` in plaats van individuele pakketten
   - Sommige notebooks hebben extra pakketten nodig die in hun markdown cellen genoemd worden

4. **Azure services:**
   - Azure AI services vereisen een actief abonnement
   - Sommige functies zijn regio-specifiek
   - Zorg dat je Azure OpenAI model-implementatie de Responses API ondersteunt

### Leerpad

Aanbevolen volgorde voor de lessen:
1. **00-course-setup** - Begin hier voor de omgeving setup
2. **01-intro-to-ai-agents** - Begrijp AI agent fundamenten
3. **02-explore-agentic-frameworks** - Leer over verschillende frameworks
4. **03-agentic-design-patterns** - Kern ontwerppatronen
5. Ga door met de genummerde lessen in volgorde

### Framework Selectie

Kies framework op basis van je doelen:
- **Alle lessen**: Microsoft Agent Framework (MAF) met `FoundryChatClient`
- **Agents registreren server-side** in Microsoft Foundry Agent Service V2 en zijn zichtbaar in het Foundry portal

### Hulp Krijgen

- Word lid van de [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Bekijk les README bestanden voor specifieke richtlijnen
- Raadpleeg de hoofd-[README.md](./README.md) voor cursusoverzicht
- Zie [Course Setup](./00-course-setup/README.md) voor gedetailleerde setup instructies

### Bijdragen

Dit is een open educatief project. Bijdragen welkom:
- Verbeter codevoorbeelden
- Corrigeer typfouten of fouten
- Voeg verduidelijkende opmerkingen toe
- Stel nieuwe lesthema's voor
- Vertaal naar extra talen

Zie [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) voor huidige behoeften.

## Projectspecifieke Context

### Meertalige Ondersteuning

Deze repository gebruikt een geautomatiseerd vertaalsysteem:
- 50+ ondersteunde talen
- Vertalingen in `/translations/<lang-code>/` mappen
- GitHub Actions workflow verzorgt vertaalupdates
- Brondocumenten in het Engels in de repository root

### Lesstructuur

Elke les volgt een consistent patroon:
1. Video thumbnail met link
2. Geschreven lesinhoud (README.md)
3. Codevoorbeelden in meerdere frameworks
4. Leerdoelen en vereisten
5. Extra leermaterialen gelinkt

### Naamgeving van Codevoorbeelden

Formaat: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Les 1, MAF Python
- `14-sequential.ipynb` - Les 14, MAF gevorderde patronen
- `16-python-agent-framework.ipynb` - Les 16, productie klantenservice agent
- `17-local-agent-foundry-local.ipynb` - Les 17, lokale agent met Foundry Local + Qwen

### Speciale Mappen

- `translated_images/` - Gelokaliseerde afbeeldingen voor vertalingen
- `images/` - Originele afbeeldingen voor Engelse inhoud
- `.devcontainer/` - VS Code ontwikkelcontainer configuratie
- `.github/` - GitHub Actions workflows en sjablonen

### Afhankelijkheden

Belangrijke pakketten van `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-naar-Agent protocol ondersteuning
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure authenticatie (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integratie
- `mcp[cli]` - Model Context Protocol ondersteuning

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->