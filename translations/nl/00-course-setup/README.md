# Cursus Instellen

## Introductie

Deze les behandelt hoe je de codesamples van deze cursus kunt uitvoeren.

## Sluit je aan bij andere cursisten en krijg hulp

Voordat je begint met het klonen van je repo, sluit je aan bij het [AI Agents For Beginners Discord-kanaal](https://aka.ms/ai-agents/discord) om hulp te krijgen bij de setup, vragen over de cursus te stellen, of om in contact te komen met andere cursisten.

## Clone of Fork deze Repo

Om te beginnen, clone of fork je de GitHub Repository. Dit maakt een eigen versie van het cursusmateriaal zodat je de code kunt uitvoeren, testen en aanpassen!

Dit kan gedaan worden door te klikken op de link om <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">de repo te fork'en</a>

Je zou nu je eigen geforkte versie van deze cursus moeten hebben op de volgende link:

![Geforkte Repo](../../../translated_images/nl/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (aanbevolen voor workshop / Codespaces)

  >De volledige repository kan groot zijn (~3 GB) wanneer je de volledige geschiedenis en alle bestanden downloadt. Als je alleen aan de workshop deelneemt of slechts een paar lesmappen nodig hebt, voorkomt een shallow clone (of een sparse clone) het grootste deel van die download door de geschiedenis in te korten en/of blobs over te slaan.

#### Snelle shallow clone — minimale geschiedenis, alle bestanden

Vervang `<your-username>` in de onderstaande opdrachten door je fork-URL (of de upstream-URL als je dat liever hebt).

Om alleen de laatste commitgeschiedenis te clonen (kleine download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Om een specifieke branch te clonen:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Gedeeltelijke (sparse) clone — minimale blobs + alleen geselecteerde mappen

Dit gebruikt partial clone en sparse-checkout (vereist Git 2.25+ en aanbevolen moderne Git met partial clone ondersteuning):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Ga naar de repo map:

```bash|powershell
cd ai-agents-for-beginners
```

Specificeer dan welke mappen je wilt (voorbeeld hieronder toont twee mappen):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Na het klonen en verifiëren van de bestanden, als je alleen bestanden nodig hebt en ruimte wilt vrijmaken (geen git geschiedenis), verwijder dan de repository metadata (💀onherroepelijk — je verliest alle Git-functionaliteit: geen commits, pulls, pushes, of toegang tot geschiedenis).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces gebruiken (aanbevolen om grote lokale downloads te vermijden)

- Maak een nieuwe Codespace voor deze repo via de [GitHub UI](https://github.com/codespaces).  

- Voer in de terminal van de nieuw aangemaakte codespace een van de shallow/sparse clone commando's hierboven uit om alleen de benodigde lesmappen in de Codespace-werkruimte te krijgen.
- Optioneel: verwijder na het klonen binnen Codespaces .git om extra ruimte vrij te maken (zie verwijderingscommando's hierboven).
- Let op: als je de repo liever direct in Codespaces opent (zonder extra clone), wees ervan bewust dat Codespaces de devcontainer omgeving opbouwt en mogelijk meer provisioning doet dan je nodig hebt. Het klonen van een shallow kopie binnen een verse Codespace geeft je meer controle over schijfruimte.

#### Tips

- Vervang altijd de clone URL door je fork als je wilt bewerken/committen.
- Als je later meer geschiedenis of bestanden nodig hebt, kun je deze ophalen of sparse-checkout aanpassen om extra mappen toe te voegen.

## Code Uitvoeren

Deze cursus biedt een reeks Jupyter Notebooks die je kunt uitvoeren om praktijkervaring op te doen met het bouwen van AI Agents.

De codesamples gebruiken **Microsoft Agent Framework (MAF)** met de `FoundryChatClient`, die verbinding maakt met **Microsoft Foundry Agent Service V2** (de Responses API) via **Microsoft Foundry**.

Alle Python-notebooks zijn gelabeld met `*-python-agent-framework.ipynb`.

## Vereisten

- Python 3.12+
  - **OPMERKING**: Als je Python3.12 niet geïnstalleerd hebt, zorg dan dat je het installeert. Maak daarna je virtuele omgeving (venv) aan met python3.12 om ervoor te zorgen dat de correcte versies worden geïnstalleerd vanuit het requirements.txt bestand.
  
    >Voorbeeld

    Maak een Python venv map aan:

    ```bash|powershell
    python -m venv venv
    ```

    Activeer dan de venv omgeving voor:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Voor de voorbeeldcode die .NET gebruikt, zorg dat je [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) of hoger installeert. Controleer daarna je geïnstalleerde .NET SDK versie:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Vereist voor authenticatie. Installeer via [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Abonnement** — Voor toegang tot Microsoft Foundry en Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Een project met een gedeplooyeerd model (bijvoorbeeld `gpt-5-mini`). Zie [Stap 1](#stap-1-maak-een-microsoft-foundry-project-aan) hieronder.

In de root van deze repository is een `requirements.txt` bestand opgenomen met alle benodigde Python packages om de codesamples uit te voeren.

Je kunt deze installeren door het volgende commando uit te voeren in je terminal in de root van de repository:

```bash|powershell
pip install -r requirements.txt
```

We raden aan een Python virtuele omgeving te creëren om conflicten en problemen te voorkomen.

## VSCode Instellen

Zorg dat je de juiste versie van Python in VSCode gebruikt.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry en Microsoft Foundry Agent Service instellen

### Stap 1: Maak een Microsoft Foundry Project aan

Je hebt een Microsoft Foundry **hub** en **project** met een gedeplooyeerd model nodig om de notebooks uit te voeren.

1. Ga naar [ai.azure.com](https://ai.azure.com) en log in met je Azure-account.
2. Maak een **hub** aan (of gebruik een bestaande). Zie: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Maak binnen de hub een **project** aan.
4. Deploy een model (bijvoorbeeld `gpt-5-mini`) via **Models + Endpoints** → **Deploy model**.

### Stap 2: Haal je Project Endpoint en Model Deploy Naam op

Vanuit je project in het Microsoft Foundry portal:

- **Project Endpoint** — Ga naar de pagina **Overzicht** en kopieer de endpoint URL.

![Project Connectiestring](../../../translated_images/nl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deploy Naam** — Ga naar **Models + Endpoints**, selecteer je gedeplooyeerde model en noteer de **Deployment name** (bijvoorbeeld `gpt-5-mini`).

### Stap 3: Log in op Azure met `az login`

Alle notebooks gebruiken **`AzureCliCredential`** voor authenticatie — geen API-sleutels om te beheren. Dit vereist dat je bent ingelogd via de Azure CLI.

1. **Installeer de Azure CLI** als je dat nog niet hebt gedaan: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Log in** door uit te voeren:

    ```bash|powershell
    az login
    ```

    Of als je in een remote/Codespace omgeving bent zonder browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Selecteer je abonnement** als hierom wordt gevraagd — kies degene met je Foundry project.

4. **Controleer** of je bent ingelogd:

    ```bash|powershell
    az account show
    ```

> **Waarom `az login`?** De notebooks authenticeren met `AzureCliCredential` uit het `azure-identity` pakket. Dit betekent dat je Azure CLI sessie de referenties levert — geen API-sleutels of geheimen in je `.env` bestand. Dit is een [security best practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Stap 4: Maak je `.env` bestand aan

Kopieer het voorbeeldbestand:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Open `.env` en vul deze twee waarden in:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variabele | Waar te vinden |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → je project → pagina **Overzicht** |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → naam van je gedeplooyeerde model |

Dat is alles voor de meeste lessen! De notebooks authenticeren automatisch via je `az login` sessie.

### Stap 5: Installeer Python Afhankelijkheden

```bash|powershell
pip install -r requirements.txt
```

We raden aan dit binnen de eerder gemaakte virtuele omgeving te doen.

## Extra Setup voor Les 5 (Agentic RAG)

Les 5 gebruikt **Azure AI Search** voor retrieval-augmented generation. Als je die les wilt draaien, voeg dan deze variabelen toe aan je `.env` bestand:

| Variabele | Waar te vinden |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → je **Azure AI Search** resource → **Overzicht** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → je **Azure AI Search** resource → **Instellingen** → **Sleutels** → primaire beheerderssleutel |

## Extra Setup voor Lessen die Direct Azure OpenAI Aanroepen (Lessen 6 en 8)

Sommige notebooks in lessen 6 en 8 roepen direct **Azure OpenAI** aan (met de **Responses API**) in plaats van via een Microsoft Foundry project te gaan. Deze samples gebruikten voorheen GitHub Models, welke deprecated zijn (terugdraaien in juli 2026) en de Responses API niet ondersteunen. Als je die samples wilt draaien, voeg dan deze variabelen toe aan je `.env` bestand:

| Variabele | Waar te vinden |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → je **Azure OpenAI** resource → **Sleutels en Endpoint** → Endpoint (bijv. `https://<je-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Naam van je gedeplooyeerde model (bijv. `gpt-5-mini`) dat de Responses API ondersteunt |
| `AZURE_OPENAI_API_KEY` | Optioneel — alleen als je key-based auth gebruikt in plaats van `az login` / Entra ID |

> De Responses API gebruikt de stabiele `/openai/v1/` endpoint, dus er is geen `api-version` vereist. Log in met `az login` voor sleutelvrije Entra ID authenticatie.

## Alternatieve Provider: MiniMax (OpenAI-Compatibel)

[MiniMax](https://platform.minimaxi.com/) biedt large-context modellen (tot 204K tokens) via een OpenAI-compatibele API. Omdat de Microsoft Agent Framework's `OpenAIChatClient` werkt met elke OpenAI-compatibele endpoint, kun je MiniMax als een directe vervanger van Azure OpenAI of OpenAI gebruiken.

Voeg deze variabelen toe aan je `.env` bestand:

| Variabele | Waar te vinden |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Sleutels |
| `MINIMAX_BASE_URL` | Gebruik `https://api.minimax.io/v1` (standaardwaarde) |
| `MINIMAX_MODEL_ID` | Modelnaam om te gebruiken (bijv. `MiniMax-M3`) |

**Voorbeeldmodellen**: `MiniMax-M3` (aanbevolen), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (snellere reacties). Modelnamen en beschikbaarheid kunnen in de loop van de tijd veranderen, en toegang tot een bepaald model kan afhangen van je account of regio — bekijk de [MiniMax Platform](https://platform.minimaxi.com/) voor de actuele lijst. Als `MiniMax-M3` niet beschikbaar is voor je account, stel `MINIMAX_MODEL_ID` in op een model waar je wel toegang toe hebt (bijv. `MiniMax-M2.7`).

De codesamples die `OpenAIChatClient` gebruiken (bijv. Les 14 hotelboeking workflow) zullen automatisch je MiniMax configuratie detecteren en gebruiken wanneer `MINIMAX_API_KEY` is ingesteld.

## Alternatieve Provider: Foundry Local (Voer Modellen Uit op je Eigen Apparaat)

[Foundry Local](https://foundrylocal.ai) is een lichte runtime die taalmodellen **volledig op je eigen apparaat** downloadt, beheert en serveert via een OpenAI-compatibele API — geen cloud, geen Azure-abonnement en geen API-sleutels. Het is een uitstekende optie voor offline ontwikkeling, experimenteren zonder clouddkosten, of het houden van data op het apparaat.

Omdat de Microsoft Agent Framework's `OpenAIChatClient` werkt met elke OpenAI-compatibele endpoint, is Foundry Local een lokale directe vervanger van Azure OpenAI.

**1. Installeer Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Download en start een model** (dit start ook de lokale service):

```bash
foundry model list          # zie beschikbare modellen
foundry model run phi-4-mini
```

**3. Installeer de Python SDK** die wordt gebruikt om de lokale endpoint te ontdekken:

```bash
pip install foundry-local-sdk
```

**4. Verwijs het Microsoft Agent Framework naar je lokale model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Downloadt (indien nodig) en serveert het model lokaal, en ontdekt vervolgens de endpoint/poort.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # bijv. http://localhost:<poort>/v1
    api_key=manager.api_key,        # altijd "niet vereist" voor Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Opmerking:** Foundry Local biedt een OpenAI-compatibele **Chat Completions** endpoint. Gebruik het voor lokale ontwikkeling en offline scenario's. Voor de volledige **Responses API** functie-set (toestandsvolle gesprekken, diepe tool-orkestratie, en agent-stijl ontwikkeling), richt op **Azure OpenAI** of een **Microsoft Foundry** project zoals gedemonstreerd in de lessen. Zie de [Foundry Local documentatie](https://foundrylocal.ai) voor de huidige modelcatalogus en platformondersteuning.

## Extra Setup voor Les 8 (Bing Grounding Workflow)


Het voorwaardelijke workflow-notebook in les 8 gebruikt **Bing grounding** via Microsoft Foundry. Als je van plan bent om dat voorbeeld uit te voeren, voeg dan deze variabele toe aan je `.env`-bestand:

| Variabele | Waar te vinden |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry-portaal → je project → **Management** → **Connected resources** → je Bing-verbinding → kopieer het verbindings-ID |

## Problemen oplossen

### SSL Certificate Verification Errors op macOS

Als je macOS gebruikt en een fout tegenkomt zoals:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dit is een bekend probleem met Python op macOS waarbij de systeem-SSL-certificaten niet automatisch vertrouwd worden. Probeer de volgende oplossingen op volgorde:

**Optie 1: Voer het Install Certificates-script van Python uit (aanbevolen)**

```bash
# Vervang 3.XX door je geïnstalleerde Python-versie (bijv. 3.12 of 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Optie 2: Gebruik `connection_verify=False` in je notebook (alleen voor GitHub Models-notebooks)**

In het Lesson 6-notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) is al een uitgecommentarieerde workaround opgenomen. Haal de commentaar weg bij `connection_verify=False` bij het aanmaken van de client:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Schakel SSL-verificatie uit als u certificaatfouten tegenkomt
)
```

> **⚠️ Waarschuwing:** Het uitschakelen van SSL-verificatie (`connection_verify=False`) vermindert de veiligheid door certificaatvalidatie over te slaan. Gebruik dit alleen als tijdelijke workaround in ontwikkelomgevingen, nooit in productie.

**Optie 3: Installeer en gebruik `truststore`**

```bash
pip install truststore
```

Voeg vervolgens het volgende toe bovenaan je notebook of script voordat je netwerkoproepen doet:

```python
import truststore
truststore.inject_into_ssl()
```

## Vastgelopen?

Als je problemen hebt met deze setup, sluit dan aan bij onze <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> of <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">maak een issue aan</a>.

## Volgende les

Je bent nu klaar om de code voor deze cursus uit te voeren. Veel plezier met het verder ontdekken van de wereld van AI Agents!

[Introductie tot AI Agents en Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->