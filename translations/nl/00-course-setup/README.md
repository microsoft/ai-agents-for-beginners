# Cursusconfiguratie

## Introductie

Deze les behandelt hoe je de voorbeeldcode van deze cursus kunt uitvoeren.

## Word lid van andere studenten en krijg hulp

Voordat je begint met het klonen van je repository, sluit je aan bij het [AI Agents For Beginners Discord-kanaal](https://aka.ms/ai-agents/discord) om hulp te krijgen bij de setup, vragen over de cursus te stellen of om in contact te komen met andere studenten.

## Clone of Fork deze Repo

Om te beginnen, clone of fork je de GitHub-repository. Hierdoor krijg je je eigen versie van het cursusmateriaal zodat je de code kunt uitvoeren, testen en aanpassen!

Dit kan worden gedaan door op de link te klikken om <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">de repo te forken</a>

Je zou nu je eigen geforkte versie van deze cursus moeten hebben via de volgende link:

![Geforkte Repo](../../../translated_images/nl/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (aanbevolen voor workshop / Codespaces)

  >De volledige repository kan groot zijn (~3 GB) als je de volledige geschiedenis en alle bestanden downloadt. Als je alleen de workshop bijwoont of maar een paar lesmappen nodig hebt, downloadt een shallow clone (of sparse clone) aanzienlijk minder.

#### Snelle shallow clone — minimale geschiedenis, alle bestanden

Vervang `<your-username>` in de onderstaande commando’s door je fork-URL (of de upstream-URL als je dat liever hebt).

Om alleen de nieuwste commitgeschiedenis te klonen (kleine download):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Om een specifieke branch te klonen:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Gedeeltelijke (sparse) clone — minimale blobs + alleen geselecteerde mappen

Dit gebruikt partial clone en sparse-checkout (vereist Git 2.25+ en aanbevolen moderne Git met ondersteuning voor partial clone):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Navigeer naar de repo-map:

```bash
cd ai-agents-for-beginners
```

Specificeer vervolgens welke mappen je wilt hebben (voorbeeld hieronder toont twee mappen):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Na het klonen en het verifiëren van de bestanden, als je alleen bestanden nodig hebt en ruimte wilt vrijmaken (geen git-geschiedenis), verwijder dan de repository-metadata (💀onherroepelijk — je verliest alle Git-functionaliteit):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Gebruik GitHub Codespaces (aanbevolen om grote lokale downloads te vermijden)

- Maak een nieuwe Codespace voor deze repo via de [GitHub UI](https://github.com/codespaces).  

- Voer in de terminal van de nieuw gemaakte codespace een van de bovenstaande shallow/sparse clone-commando’s uit om alleen de benodigde lesmappen in de Codespace-werkruimte te krijgen.
- Optioneel: verwijder na het klonen in Codespaces de .git-map om extra ruimte vrij te maken (zie verwijdercommando’s hierboven).
- Opmerking: als je de repo direct in Codespaces opent (zonder extra clone), houdt er dan rekening mee dat Codespaces de devcontainer-omgeving opzet en mogelijk meer instelt dan je nodig hebt.

#### Tips

- Vervang de clone-URL altijd door je fork als je wilt bewerken/commiten.
- Als je later meer geschiedenis of bestanden nodig hebt, kun je deze opvragen of sparse-checkout aanpassen om extra mappen op te nemen.

## Code Uitvoeren

Deze cursus biedt een reeks Jupyter Notebooks die je kunt uitvoeren om praktijkervaring op te doen met het bouwen van AI Agents.

De codevoorbeelden gebruiken **Microsoft Agent Framework (MAF)** met de `FoundryChatClient`, die verbinding maakt met **Microsoft Foundry Agent Service V2** (de Responses API) via **Microsoft Foundry**.

Alle Python-notebooks zijn gelabeld als `*-python-agent-framework.ipynb`.

## Vereisten

- Python 3.12+
  - **OPMERKING**: Als je Python3.12 niet hebt geïnstalleerd, zorg dan dat je dit installeert. Maak vervolgens je virtuele omgeving aan met python3.12 om de juiste versies te garanderen van de packages in het requirements.txt-bestand.
  
    >Voorbeeld

    Maak een Python virtual environment-directory aan:

    ```bash
    python -m venv venv
    ```

    Activeer vervolgens de virtuele omgeving voor:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: Voor de voorbeeldcode die .NET gebruikt, zorg dat je [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) of hoger installeert. Controleer daarna je geïnstalleerde .NET SDK-versie:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Vereist voor authenticatie. Installeer via [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — Voor toegang tot Microsoft Foundry en Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Een project met een gedeployd model (bijv. `gpt-5-mini`). Zie [Stap 1](#stap-1-maak-een-microsoft-foundry-project-aan) hieronder.

We hebben een `requirements.txt`-bestand opgenomen in de root van deze repository met alle benodigde Python-pakketten om de codevoorbeelden uit te voeren.

Je kunt deze installeren door het volgende commando in je terminal uit te voeren in de root van de repository:

```bash
pip install -r requirements.txt
```

We raden aan een Python virtuele omgeving aan te maken om conflicten en problemen te voorkomen.

## VSCode configureren

Zorg dat je de juiste versie van Python gebruikt in VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry en Microsoft Foundry Agent Service instellen

### Stap 1: Maak een Microsoft Foundry Project aan

Je hebt een Microsoft Foundry **hub** en **project** met een gedeployd model nodig om de notebooks uit te voeren.

1. Ga naar [ai.azure.com](https://ai.azure.com) en log in met je Azure-account.
2. Maak een **hub** aan (of gebruik een bestaande). Zie: [Overzicht hub resources](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Maak binnen de hub een **project** aan.
4. Deploy een model (bijv. `gpt-5-mini`) via **Modellen + Eindpunten** → **Model deployen**.

### Stap 2: Haal je project endpoint en model deployment naam op

Vanuit je project in de Microsoft Foundry-portal:

- **Project Endpoint** — Ga naar de **Overzicht**-pagina en kopieer de endpoint-URL.

![Project Connection String](../../../translated_images/nl/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Naam** — Ga naar **Modellen + Eindpunten**, selecteer je gedeployde model en noteer de **Deployment naam** (bijv. `gpt-5-mini`).

### Stap 3: Meld je aan bij Azure met `az login`

De meeste notebooks authenticeren via je **Azure CLI-aanmelding** — met `AzureCliCredential` of `DefaultAzureCredential` (beide maken gebruik van je `az login`-sessie) uit het `azure-identity`-pakket — zodat ze geen API-sleutels vereisen. Sommige lessen en optionele integraties gebruiken API-sleutels; controleer per les welke extra omgevingsvariabelen nodig zijn. Hiervoor moet je aangemeld zijn via de Azure CLI.

1. **Installeer de Azure CLI** als je dat nog niet hebt gedaan: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Log in** door het volgende uit te voeren:

    ```bash
    az login
    ```

    Of als je in een remote/Codespace-omgeving zonder browser zit:

    ```bash
    az login --use-device-code
    ```

3. **Selecteer je abonnement** als daarom wordt gevraagd — kies het abonnement met jouw Foundry-project.

4. **Controleer** of je bent aangemeld:

    ```bash
    az account show
    ```

> **Waarom `az login`?** De notebooks authenticeren met `AzureCliCredential` (of `DefaultAzureCredential` dat ook je Azure CLI-aanmelding gebruikt) uit het `azure-identity`-pakket. Dit betekent dat je Azure CLI-sessie de referenties levert — geen API-sleutels of geheimen in je `.env`-bestand. Dit is een [beveiligingsbest practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Stap 4: Maak je `.env`-bestand aan

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
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portal → je project → **Overzicht** pagina |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portal → **Modellen + Eindpunten** → naam van je gedeployde model |

Dat is alles voor de meeste lessen! De notebooks authenticeren automatisch via je `az login`-sessie.

### Stap 5: Installeer Python-afhankelijkheden

```bash
pip install -r requirements.txt
```

We raden aan dit uit te voeren binnen de virtuele omgeving die je eerder hebt aangemaakt.

## Optionele setup: Azure AI Search (lessen 5 en 16)

De les 5 (Agentic RAG) en les 16 notebooks werken direct met een **in-memory kennisbasis** — er zijn geen extra Azure-resources nodig. Wil je ze ondersteunen met een echte **Azure AI Search** index, let dan op dat de **les 16 notebook momenteel sleutel-gebaseerde authenticatie gebruikt**: het wisselt van in-memory search naar Azure AI Search alleen wanneer **zowel** `AZURE_SEARCH_SERVICE_ENDPOINT` **als** `AZURE_SEARCH_API_KEY` zijn ingesteld, en blijft anders bij de in-memory search — dus om het tegen een echte index uit te voeren moet je ook de admin-sleutel instellen. Keyless authenticatie met Microsoft Entra ID (RBAC) is de aanbevolen aanpak voor je eigen productiecode, consistent met de `az login` flow die in de rest van deze cursus wordt gebruikt.

De onderstaande RBAC-stappen gelden voor de setup-gidsvoorbeelden en je eigen code. Ze maken keyless authenticatie in de les 16 notebook niet mogelijk; les 16 vereist nog steeds zowel de endpoint als admin key om Azure AI Search te gebruiken.

1. **Schakel rolgebaseerde toegang in** op je zoekservice:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Ken jezelf de vereiste rollen toe** (maken/laden van indexen en query’s):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Voeg de endpoint toe** aan je `.env`-bestand:

| Variabele | Waar te vinden |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → je **Azure AI Search** resource → **Overzicht** → URL |
| `AZURE_SEARCH_API_KEY` | Vereist (met de endpoint) om Azure AI Search in les 16 in te schakelen die key-based auth gebruikt. Azure portal → **Instellingen** → **Sleutels** → primaire adminsleutel |

> **Waarom keyless?** Admin-sleutels geven volledige schrijfrechten op je zoekservice en kunnen lekken via `.env`-bestanden. Met RBAC wordt je `az login`-identiteit gebruikt — hetzelfde keyless Entra ID-patroon dat de cursus notebooks gebruikt (via `AzureCliCredential` / `DefaultAzureCredential`). Zie [Verbinden met Azure AI Search met rollen](https://learn.microsoft.com/azure/search/search-security-rbac).

Zie de [Azure AI Search setup-gids](./AzureSearch.md) voor volledige voorbeeldcode om indexen aan te maken in Python en .NET.

## Extra setup voor lessen die direct Azure OpenAI aanroepen (lessen 6 en 8)

Sommige notebooks in lessen 6 en 8 roepen **Azure OpenAI** direct aan (via de **Responses API**) in plaats van via een Microsoft Foundry-project. Deze voorbeelden gebruikten eerder GitHub Models, die verouderd zijn en de Responses API niet ondersteunen. Voeg deze variabelen toe aan je `.env`-bestand:

| Variabele | Waar te vinden |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → je **Azure OpenAI** resource → **Sleutels en Endpoint** → Endpoint (bijv. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | De naam van je gedeployde model (bijv. `gpt-5-mini`) die de Responses API ondersteunt |
| `AZURE_OPENAI_API_KEY` | Optioneel — alleen als je sleutel-gebaseerde auth gebruikt in plaats van `az login` / Entra ID |

> De Responses API gebruikt de stabiele `/openai/v1/` endpoint, dus `api-version` is niet nodig. Meld je aan met `az login` om keyless Entra ID-authenticatie te gebruiken.

## Alternatieve provider: MiniMax (OpenAI-compatibel)

[MiniMax](https://platform.minimaxi.com/) biedt modellen met een groot contextvenster (tot 204K tokens) via een OpenAI-compatibele API. Omdat de `OpenAIChatClient` van het Microsoft Agent Framework werkt met elke OpenAI-compatibele endpoint, kun je MiniMax als drop-in alternatief gebruiken voor lessen die `OpenAIChatClient` gebruiken.

Voeg deze variabelen toe aan je `.env`-bestand:

| Variabele | Waar te vinden |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API-sleutels |
| `MINIMAX_BASE_URL` | Gebruik `https://api.minimax.io/v1` (standaardwaarde) |
| `MINIMAX_MODEL_ID` | Te gebruiken modelnaam (bijv. `MiniMax-M3`) |

**Voorbeeldmodellen**: `MiniMax-M3` (aanbevolen), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (snellere reacties). Modelnamen en beschikbaarheid kunnen in de loop van de tijd veranderen, en de toegang tot een model kan afhankelijk zijn van je account.

De codevoorbeelden die `OpenAIChatClient` gebruiken (bijv. les 14 hotelboekingsworkflow) detecteren en gebruiken automatisch je MiniMax-configuratie wanneer `MINIMAX_API_KEY` is ingesteld.


## Alternatieve Provider: Novita AI (OpenAI-compatibel)

[Novita AI](https://novita.ai/llm-api) biedt een OpenAI-compatibele API voor open-source en frontier LLM's (DeepSeek, Llama, Qwen, en meer). Omdat het Microsoft Agent Framework's `OpenAIChatClient` werkt met elk OpenAI-compatibel eindpunt, kun je Novita AI gebruiken als een drop-in alternatief voor Azure OpenAI of OpenAI.

Voeg deze variabelen toe aan je `.env` bestand:

| Variabele | Waar te vinden |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | Gebruik `https://api.novita.ai/openai/v1` (standaardwaarde) |
| `NOVITA_MODEL_ID` | Modelnaam om te gebruiken (bijv. `moonshotai/kimi-k3`) |

**Voorbeeldmodellen**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI host ook vele andere open-source modelgroepen (Llama, Qwen, GLM, en meer) — bekijk de [Novita AI modellibrary](https://novita.ai/llm-api) voor de huidige lijst van beschikbare modellen en hun model-ID's.

De huidige voorbeelden gebruiken niet automatisch de `NOVITA_*` variabelen. Om Novita AI te gebruiken, geef deze waarden expliciet door bij het aanmaken van de `OpenAIChatClient` in het voorbeeld dat je uitvoert.

## Alternatieve Provider: Foundry Local (Modellen op je apparaat draaien)

[Foundry Local](https://foundrylocal.ai) is een lichtgewicht runtime die taalmodellen **geheel op je eigen machine** downloadt, beheert en serveert via een OpenAI-compatibele API — geen cloud vereist.

Omdat het Microsoft Agent Framework's `OpenAIChatClient` werkt met elk OpenAI-compatibel eindpunt, is Foundry Local een drop-in lokale alternatief voor Azure OpenAI.

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

**3. Installeer de Python SDK** die wordt gebruikt om het lokale eindpunt te ontdekken:

```bash
pip install foundry-local-sdk
```

**4. Richt het Microsoft Agent Framework op je lokale model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Downloadt (indien nodig) en serveert het model lokaal, en ontdekt vervolgens de endpoint/poort.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # bv. http://localhost:<poort>/v1
    api_key=manager.api_key,        # altijd "niet-vereist" voor Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Opmerking:** Foundry Local biedt een OpenAI-compatibel **Chat Completions** eindpunt. Gebruik dit voor lokale ontwikkeling en offline scenario's. Voor de volledige **Responses API** functieset (toestandachtige gesprekken, enz.), gebruik Azure OpenAI of een Microsoft Foundry-project.

## Extra Instellingen voor Les 8 (Bing Grounding Workflow)

De conditionele workflow notebook in les 8 gebruikt **Bing grounding** via Microsoft Foundry. Als je van plan bent dat voorbeeld uit te voeren, voeg dan deze variabele toe aan je `.env` bestand:

| Variabele | Waar te vinden |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portal → jouw project → **Management** → **Connected resources** → jouw Bing-verbinding → kopieer de verbindings-ID |

## Problemen oplossen

### SSL Certificaat Verificatiefouten op macOS

Als je op macOS bent en een fout zoals deze tegenkomt:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dit is een bekend probleem met Python op macOS waarbij de systeem SSL-certificaten niet automatisch worden vertrouwd. Probeer de volgende oplossingen in volgorde:

**Optie 1: Voer het installatie-script voor certificaten van Python uit (aanbevolen)**

```bash
# Vervang 3.XX door je geïnstalleerde Python-versie (bijv. 3.12 of 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Optie 2: Gebruik `connection_verify=False` in je notebook (alleen voor GitHub Models notebooks)**

In de Les 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) is al een uitgecommentarieerde workaround opgenomen. Haal het commentaar van `connection_verify=False` weg als je certificaatfouten krijgt:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Schakel SSL-verificatie uit als u certificaatfouten tegenkomt
)
```

> **⚠️ Waarschuwing:** SSL-verificatie uitschakelen (`connection_verify=False`) vermindert de veiligheid doordat certificaatvalidatie wordt overgeslagen. Gebruik dit alleen als tijdelijke oplossing in ontwikkelomgevingen. Nooit in productie.

**Optie 3: Installeer en gebruik `truststore`**

```bash
pip install truststore
```

Voeg dan het volgende toe aan het begin van je notebook of script voordat je netwerkverzoeken doet:

```python
import truststore
truststore.inject_into_ssl()
```

## Vastgelopen?

Als je problemen hebt met deze setup, sluit dan aan bij onze <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> of <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">maak een issue aan</a>.

## Volgende Les

Je bent nu klaar om de code voor deze cursus uit te voeren. Veel succes met het leren over de wereld van AI Agents!

[Introductie tot AI Agents en Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->