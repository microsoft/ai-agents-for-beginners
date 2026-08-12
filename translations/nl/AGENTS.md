# AGENTS.md

## Projectoverzicht

Deze repository bevat "AI Agents voor Beginners" - een uitgebreide educatieve cursus die alles leert wat nodig is om AI Agents te bouwen. De cursus bestaat uit 18 lessen (genummerd 00-18) die de basisprincipes, ontwerp patronen, frameworks, productiedeployments, lokale/apparaatgebonden agents en beveiliging van AI agents behandelen.

**Belangrijke technologieën:**
- Python 3.12+
- Jupyter Notebooks voor interactief leren
- AI Frameworks: Microsoft Agent Framework (MAF)
- Azure AI Services: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architectuur:**
- Les-gebaseerde structuur (00-15+ mappen)
- Elke les bevat: README-documentatie, codevoorbeelden (Jupyter notebooks) en afbeeldingen
- Meertalige ondersteuning via geautomatiseerd vertaalsysteem
- Eén Python notebook per les met Microsoft Agent Framework

## Installatiecommando's

### Vereisten
- Python 3.12 of hoger
- Azure abonnement (voor Microsoft Foundry)
- Azure CLI geïnstalleerd en ingelogd (`az login`)

### Eerste installatie

1. **Clone of fork de repository:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OF
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Creëer en activeer een Python virtuele omgeving:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Op Windows: venv\Scripts\activate
   ```

3. **Installeer de dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Stel omgevingsvariabelen in:**
   ```bash
   cp .env.example .env
   # Bewerk .env met je API-sleutels en eindpunten
   ```

### Vereiste omgevingsvariabelen

Voor **Microsoft Foundry** (vereist):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projectendpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Naam van modeldeployment (bijv. gpt-5-mini)

Voor **Azure AI Search** (Les 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API-sleutel

Authenticatie: Voer `az login` uit voordat je de notebooks draait (gebruikt `AzureCliCredential`).

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
- Productierijp met ingebouwde observability
- Bestands patroon: `*-python-agent-framework.ipynb`

## Testinstructies

Dit is een educatieve repository met voorbeeldcode in plaats van productcode met geautomatiseerde tests. Om je setup en wijzigingen te verifiëren:

### Handmatig testen

1. **Test de Python-omgeving:**
   ```bash
   python --version  # Moet 3.12+ zijn
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Test notebookuitvoering:**
   ```bash
   # Converteer notebook naar script en voer uit (test imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Verifieer omgevingsvariabelen:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Individuele notebooks draaien

Open notebooks in Jupyter en voer cellen opeenvolgend uit. Elke notebook is zelfstandig en bevat:
- Import statements
- Configuratie laden
- Voorbeeldimplementaties van agents
- Verwachte output in markdown cellen

### Smoke-testen van gedeploide Agents

Voor lessen waarin een agent is gedeployed als een door Microsoft Foundry gehoste agent (01, 04, 05, 16), levert de repo smoke-test catalogi onder `tests/` die uitgevoerd worden via de `.github/workflows/smoke-test.yml` workflow met de [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) actie. Dit is een lichte post-deploy controle (is de agent bereikbaar en volgt deze basis prompt verwachtingen?), als aanvulling op de evaluatiepipeline in Lessen 10 en 16. Zie [tests/README.md](./tests/README.md) voor de mapping tussen catalogus, les en agent. Les 17 draait lokaal met Foundry Local en heeft geen gehost endpoint, dus wordt gevalideerd door het direct uitvoeren van de notebook.

## Code Stijl

### Python conventies

- **Python versie**: 3.12+
- **Code stijl**: Volg standaard Python PEP 8 conventies
- **Notebooks**: Gebruik duidelijke markdown cellen om concepten uit te leggen
- **Imports**: Groepeer op standaardbibliotheek, third-party en lokale imports

### Jupyter Notebook conventies

- Neem beschrijvende markdown cellen op voor codecellen
- Voeg outputvoorbeelden toe in notebooks ter referentie
- Gebruik duidelijke variabelenamen die overeenkomen met lesconcepten
- Houd de uitvoering van de notebook lineair (cel 1 → 2 → 3...)

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

## Build en Deploy

### Documentatie bouwen

Deze repository gebruikt Markdown voor documentatie:
- README.md bestanden in elke lesmap
- Hoofd README.md in de root van de repository
- Geautomatiseerd vertaalsysteem via GitHub Actions

### CI/CD Pipeline

Gelegen in `.github/workflows/`:

1. **co-op-translator.yml** - Automatische vertaling naar 50+ talen
2. **welcome-issue.yml** - Verwelkomt nieuwe issue aanmakers
3. **welcome-pr.yml** - Verwelkomt nieuwe pull request bijdragers

### Deploy

Dit is een educatieve repository - geen deployproces. Gebruikers:
1. Forken of clonen de repository
2. Draaien notebooks lokaal of in GitHub Codespaces
3. Leren door voorbeelden aan te passen en te experimenteren

## Pull Request Richtlijnen

### Voor het indienen

1. **Test je wijzigingen:**
   - Voer de aangetaste notebooks volledig uit
   - Controleer dat alle cellen zonder fouten draaien
   - Controleer of de outputs passend zijn

2. **Documentatie updates:**
   - Werk README.md bij bij toevoeging van nieuwe concepten
   - Voeg commentaar toe in notebooks voor complexe code
   - Zorg dat markdown cellen het doel uitleggen

3. **Bestandswijzigingen:**
   - Vermijd het toevoegen van `.env` bestanden (gebruik `.env.example`)
   - Voeg geen `venv/` of `__pycache__/` mappen toe
   - Behoud notebook outputs als ze concepten demonstreren
   - Verwijder tijdelijke bestanden en backup notebooks (`*-backup.ipynb`)

### PR Titel Formaat

Gebruik beschrijvende titels:
- `[Lesson-XX] Voeg nieuw voorbeeld toe voor <concept>`
- `[Fix] Corrigeer typefout in les-XX README`
- `[Update] Verbeter codevoorbeeld in les-XX`
- `[Docs] Werk installatie-instructies bij`

### Vereiste controles

- Notebooks moeten zonder fouten uitvoeren
- README bestanden moeten duidelijk en nauwkeurig zijn
- Volg bestaande codepatronen in de repository
- Handhaaf consistentie met andere lessen

## Aanvullende notities

### Veelvoorkomende valkuilen

1. **Mismatch Python versie:**
   - Zorg dat Python 3.12+ wordt gebruikt
   - Sommige pakketten werken mogelijk niet met oudere versies
   - Gebruik `python3 -m venv` om expliciet Python versie te specificeren

2. **Omgevingsvariabelen:**
   - Maak altijd `.env` aan op basis van `.env.example`
   - Voeg het `.env` bestand niet toe aan git (staat in `.gitignore`)
   - Log in met `az login` voor sleutelvrije Entra ID authenticatie

3. **Pakketconflicten:**
   - Gebruik een verse virtuele omgeving
   - Installeer vanuit `requirements.txt` in plaats van individuele pakketten
   - Sommige notebooks vereisen extra pakketten die in markdown cellen worden vermeld

4. **Azure services:**
   - Azure AI services vereisen een actief abonnement
   - Sommige functies zijn regio-afhankelijk
   - Zorg dat je Azure OpenAI model deployment de Responses API ondersteunt

### Leerpad

Aanbevolen volgorde van lessen:
1. **00-course-setup** - Begin hier voor het instellen van de omgeving
2. **01-intro-to-ai-agents** - Begrijp de basisprincipes van AI agents
3. **02-explore-agentic-frameworks** - Leer over verschillende frameworks
4. **03-agentic-design-patterns** - Kern ontwerppatronen
5. Ga door met de genummerde lessen in volgorde

### Framework selectie

Kies een framework op basis van je doelen:
- **Alle lessen**: Microsoft Agent Framework (MAF) met `FoundryChatClient`
- **Agents registreren server-side** in Microsoft Foundry Agent Service V2 en zijn zichtbaar in de Foundry portal

### Hulp krijgen

- Word lid van de [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Bekijk de les README bestanden voor specifieke aanwijzingen
- Check de hoofd [README.md](./README.md) voor cursusoverzicht
- Raadpleeg [Course Setup](./00-course-setup/README.md) voor gedetailleerde installatie-instructies

### Bijdragen

Dit is een open educatief project. Bijdragen zijn welkom:
- Verbeter codevoorbeelden
- Corrigeer typefouten of fouten
- Voeg verduidelijkende opmerkingen toe
- Stel nieuwe lesonderwerpen voor
- Vertaal naar extra talen

Zie [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) voor huidige behoeften.

## Project-specifieke context

### Meertalige ondersteuning

Deze repository gebruikt een geautomatiseerd vertaalsysteem:
- Ondersteund in 50+ talen
- Vertalingen in `/translations/<lang-code>/` mappen
- GitHub Actions workflow beheert vertaalupdates
- Bronbestanden zijn in het Engels in de root van de repository

### Lesstructuur

Elke les volgt een consistente opzet:
1. Videominiatuur met link
2. Geschreven lesinhoud (README.md)
3. Codevoorbeelden in meerdere frameworks
4. Leerdoelen en vereisten
5. Extra leerbronnen gelinkt

### Codevoorbeeldnaamgeving

Formaat: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - Les 1, MAF Python
- `14-sequential.ipynb` - Les 14, geavanceerde MAF patronen
- `16-python-agent-framework.ipynb` - Les 16, productie klantondersteuningsagent
- `17-local-agent-foundry-local.ipynb` - Les 17, lokale agent met Foundry Local + Qwen

### Speciale mappen

- `translated_images/` - Gelokaliseerde afbeeldingen voor vertalingen
- `images/` - Originele afbeeldingen voor Engelse inhoud
- `.devcontainer/` - VS Code ontwikkelcontainer configuratie
- `.github/` - GitHub Actions workflows en sjablonen

### Dependencies

Belangrijke pakketten uit `requirements.txt`:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protocol ondersteuning
- `azure-ai-inference`, `azure-ai-projects` - Azure AI services
- `azure-identity` - Azure authenticatie (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integratie
- `mcp[cli]` - Model Context Protocol ondersteuning

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->