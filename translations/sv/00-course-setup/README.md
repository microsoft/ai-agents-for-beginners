# Kursinställning

## Introduktion

Denna lektion kommer att täcka hur du kör kodexemplen i denna kurs.

## Gå med andra elever och få hjälp

Innan du börjar klona ditt repo, gå med i [AI Agents For Beginners Discord-kanal](https://aka.ms/ai-agents/discord) för att få hjälp med inställning, frågor om kursen, eller för att koppla ihop med andra elever.

## Klona eller fork detta repo

För att börja, klona eller fork GitHub-repositoriet. Detta skapar en egen version av kursmaterialet så att du kan köra, testa och justera koden!

Detta görs genom att klicka på länken för att <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forka repot</a>

Du bör nu ha din egen forkade version av denna kurs på följande länk:

![Forked Repo](../../../translated_images/sv/forked-repo.33f27ca1901baa6a.webp)

### Grundläggande kloning (rekommenderas för workshop / Codespaces)

>Hela repositoriet kan vara stort (~3 GB) när du laddar ner full historik och alla filer. Om du bara deltar i workshopen eller bara behöver några lektionsmappar, laddar en grundläggande klon (eller en sparsam klon) ner mycket mindre.

#### Snabb grundläggande kloning — minimal historik, alla filer

Ersätt `<your-username>` i kommandona nedan med din fork URL (eller upstream URL om du föredrar).

För att klona endast senaste commit-historik (liten nedladdning):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

För att klona en specifik gren:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partiell (sparsam) kloning — minimala blobs + endast utvalda mappar

Detta använder partiell kloning och sparse-checkout (kräver Git 2.25+ och rekommenderas modern Git med stöd för partiell kloning):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå in i repomappen:

```bash
cd ai-agents-for-beginners
```

Specificera sedan vilka mappar du vill ha (exempel nedan visar två mappar):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Efter kloning och verifiering av filerna, om du bara behöver filerna och vill frigöra utrymme (ingen git-historik), radera repometadatan (💀 irreversibelt — du förlorar all Git-funktionalitet):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Använda GitHub Codespaces (rekommenderas för att undvika stora lokala nedladdningar)

- Skapa en ny Codespace för detta repo via [GitHub UI](https://github.com/codespaces).  

- I terminalen i den nyss skapade codespacen, kör något av kommando för grundläggande eller sparsam kloning ovan för att bara ta in de lektionsmappar du behöver i Codespace-arbetsytan.
- Valfritt: efter kloning inne i Codespaces, ta bort .git för att återfå extra utrymme (se borttagningskommandon ovan).
- Obs: Om du föredrar att öppna repot direkt i Codespaces (utan extra kloning), var medveten om att Codespaces bygger devcontainer-miljön och kan fortfarande provisionera mer än du behöver.

#### Tips

- Byt alltid ut klonings-URL till din fork om du vill redigera/commita.
- Om du senare behöver mer historik eller filer, kan du hämta dem eller justera sparse-checkout för att inkludera ytterligare mappar.

## Köra koden

Denna kurs erbjuder en serie Jupyter Notebookar som du kan köra för att få praktisk erfarenhet av att bygga AI-agenter.

Kodexemplen använder **Microsoft Agent Framework (MAF)** med `FoundryChatClient`, som ansluter till **Microsoft Foundry Agent Service V2** (Responses API) genom **Microsoft Foundry**.

Alla Python-notebookar är märkta `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **NOTERA**: Om du inte har Python3.12 installerat, se till att installera det. Skapa sedan ditt venv med python3.12 för att säkerställa att korrekt versioner installeras från requirements.txt-filen.
  
    >Exempel

    Skapa Python venv-mapp:

    ```bash
    python -m venv venv
    ```

    Aktivera sedan venv-miljön för:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: För exempelkoder som använder .NET, se till att installera [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller senare. Kontrollera sedan din installerade .NET SDK-version:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Krävs för autentisering. Installera från [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Prenumeration** — För åtkomst till Microsoft Foundry och Microsoft Foundry Agent Service.
- **Microsoft Foundry-projekt** — Ett projekt med distribuerad modell (t.ex., `gpt-5-mini`). Se [Steg 1](#steg-1-skapa-ett-microsoft-foundry-projekt) nedan.

Vi har inkluderat en `requirements.txt` fil i roten av detta repository som innehåller alla nödvändiga Pythonpaket för att köra kodexemplen.

Du kan installera dem genom att köra följande kommando i din terminal i repo-roten:

```bash
pip install -r requirements.txt
```

Vi rekommenderar att skapa en Python virtuell miljö för att undvika konflikter och problem.

## Ställ in VSCode

Se till att du använder rätt version av Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Ställ in Microsoft Foundry och Microsoft Foundry Agent Service

### Steg 1: Skapa ett Microsoft Foundry-projekt

Du behöver en Microsoft Foundry **hub** och **projekt** med en distribuerad modell för att köra notebookarna.

1. Gå till [ai.azure.com](https://ai.azure.com) och logga in med ditt Azure-konto.
2. Skapa en **hub** (eller använd en befintlig). Se: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inom hubben, skapa ett **projekt**.
4. Distribuera en modell (t.ex., `gpt-5-mini`) från **Models + Endpoints** → **Deploy model**.

### Steg 2: Hämta din projektendpoint och modellens namn för distribution

Från ditt projekt i Microsoft Foundry-portalen:

- **Project Endpoint** — Gå till **Overview**-sidan och kopiera endpoint-URL.

![Project Connection String](../../../translated_images/sv/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Gå till **Models + Endpoints**, välj din distribuerade modell, och notera **Deployment name** (t.ex., `gpt-5-mini`).

### Steg 3: Logga in i Azure med `az login`

De flesta notebookar autentiserar via din **Azure CLI-inloggning** — med `AzureCliCredential` eller `DefaultAzureCredential` (båda hämtar din `az login`-session) från `azure-identity` paketet — så de kräver inga API-nycklar. Några lektioner och valfria integrationer använder API-nycklar; kontrollera varje lektions förutsättningar för eventuella extra miljövariabler. Detta kräver att du är inloggad via Azure CLI.

1. **Installera Azure CLI** om du inte redan gjort det: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logga in** genom att köra:

    ```bash
    az login
    ```

    Eller om du är i en remote/Codespace-miljö utan webbläsare:

    ```bash
    az login --use-device-code
    ```

3. **Välj din prenumeration** om du blir tillfrågad — välj den som innehåller ditt Foundry-projekt.

4. **Verifiera** att du är inloggad:

    ```bash
    az account show
    ```

> **Varför `az login`?** Notebookarna autentiserar med `AzureCliCredential` (eller `DefaultAzureCredential`, som även plockar upp din Azure CLI-inloggning) från `azure-identity`-paketet. Det innebär att din Azure CLI-session tillhandahåller uppgifterna — inga API-nycklar eller hemligheter i din `.env`-fil. Detta är en [säkerhetsbästa praxis](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Steg 4: Skapa din `.env`-fil

Kopiera exempel-filen:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Öppna `.env` och fyll i dessa två värden:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variabel | Var hittar du den |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portalen → ditt projekt → **Overview**-sidan |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portalen → **Models + Endpoints** → namnet på din distribuerade modell |

Det är allt för de flesta lektioner! Notebookarna kommer att autentisera automatiskt via din `az login`-session.

### Steg 5: Installera Pythonberoenden

```bash
pip install -r requirements.txt
```

Vi rekommenderar att köra detta inne i den virtuella miljö du skapade tidigare.

## Valfri installation: Azure AI Search (Lektioner 5 och 16)

Lektion 5 (Agentic RAG) och Lektion 16 notebookarna fungerar direkt med en **in-memory knowledge base** — inga extra Azure-resurser behövs. Om du vill stödja dem med en riktig **Azure AI Search**-index, notera att **Lektion 16 notebook för närvarande använder nyckelbaserad autentisering**: den byter från in-memory-sök till Azure AI Search endast när **båda** `AZURE_SEARCH_SERVICE_ENDPOINT` **och** `AZURE_SEARCH_API_KEY` är satta, och stannar annars med in-memory-sök — så för att köra mot en riktig index måste du också sätta admin-nyckeln. Nyckellös autentisering med Microsoft Entra ID (RBAC) är rekommenderat för egen produktionskod, i linje med `az login`-flödet som används överallt i denna kurs.

RBAC-stegen nedan gäller för installationsguidens exempel och din egen kod. De möjliggör inte nyckellös autentisering i Lektion 16 notebook; Lektion 16 kräver fortfarande både endpoint och admin-nyckel för att använda Azure AI Search.

1. **Aktivera rollbaserad åtkomst** på din söktjänst:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Tilldela dig själv de nödvändiga rollerna** (skapa/ladda index och fråga):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Lägg till endpointen** i din `.env`-fil:

| Variabel | Var hittar du den |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portalen → din **Azure AI Search**-resurs → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Krävs (med endpoint) för att aktivera Azure AI Search i Lektion 16 notebook, som använder nyckelbaserad autentisering. Azure-portalen → **Settings** → **Keys** → primär admin-nyckel |

> **Varför nyckellös?** Admin-nycklar ger fullt skrivåtkomst till din söktjänst och kan läcka via `.env`-filer. Med RBAC används istället din `az login`-identitet — samma nyckellösa Entra ID-mönster som kursens notebookar använder (via `AzureCliCredential` / `DefaultAzureCredential`). Se [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

Se [Azure AI Search setup guide](./AzureSearch.md) för kompletta exempel på index-skapande i Python och .NET.

## Ytterligare inställningar för lektioner som anropar Azure OpenAI direkt (lektioner 6 och 8)

Några notebookar i lektion 6 och 8 anropar **Azure OpenAI** direkt (med **Responses API**) istället för via Microsoft Foundry-projekt. Dessa exempel använde tidigare GitHub Models, som är föråldrat och stödjer inte Responses API. Lägg till dessa variabler i din `.env`-fil:

| Variabel | Var hittar du den |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure-portalen → din **Azure OpenAI**-resurs → **Keys and Endpoint** → Endpoint (t.ex., `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Namnet på din distribuerade modell (t.ex., `gpt-5-mini`) som stödjer Responses API |
| `AZURE_OPENAI_API_KEY` | Valfri — endast om du använder nyckelbaserad autentisering istället för `az login` / Entra ID |

> Responses API använder den stabila `/openai/v1/`-endpointen, så ingen `api-version` behövs. Logga in med `az login` för att använda nyckellös Entra ID-autentisering.

## Alternativ leverantör: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) erbjuder storskaliga kontextmodeller (upp till 204K tokens) via ett OpenAI-kompatibelt API. Eftersom Microsoft Agent Frameworks `OpenAIChatClient` fungerar med alla OpenAI-kompatibla endpoints, kan du använda MiniMax som ett drop-in-alternativ för lektioner som använder `OpenAIChatClient`.

Lägg till dessa variabler i din `.env`-fil:

| Variabel | Var hittar du den |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Använd `https://api.minimax.io/v1` (standardvärde) |
| `MINIMAX_MODEL_ID` | Modellnamn att använda (t.ex., `MiniMax-M3`) |

**Exempelmodeller**: `MiniMax-M3` (rekommenderad), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (snabbare svar). Modellnamn och tillgänglighet kan ändras över tid, och tillgång till en given modell kan bero på ditt konto.

Kodexemplen som använder `OpenAIChatClient` (t.ex., Lektion 14 hotellbokningsflöde) kommer automatiskt att upptäcka och använda din MiniMax-konfiguration när `MINIMAX_API_KEY` är satt.


## Alternativ leverantör: Novita AI (OpenAI-kompatibel)

[Novita AI](https://novita.ai/llm-api) erbjuder ett OpenAI-kompatibelt API för open-source och frontier LLMs (DeepSeek, Llama, Qwen och fler). Eftersom Microsoft Agent Frameworks `OpenAIChatClient` fungerar med vilken OpenAI-kompatibel slutpunkt som helst, kan du använda Novita AI som ett direkt alternativ till Azure OpenAI eller OpenAI.

Lägg till dessa variabler i din `.env`-fil:

| Variabel | Var du hittar den |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | Använd `https://api.novita.ai/openai/v1` (standardvärde) |
| `NOVITA_MODEL_ID` | Modellnamn att använda (t.ex., `moonshotai/kimi-k3`) |

**Exempelmodeller**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI tillhandahåller även många andra open-source modellfamiljer (Llama, Qwen, GLM och fler) — kolla in [Novita AI modellbibliotek](https://novita.ai/llm-api) för aktuell lista över tillgängliga modeller och deras modell-ID:n.

De nuvarande exemplen använder inte automatiskt `NOVITA_*`-variablerna. För att använda Novita AI, skicka dessa värden explicit när du skapar `OpenAIChatClient` i det exempel du kör.

## Alternativ leverantör: Foundry Local (Kör modeller på enheten)

[Foundry Local](https://foundrylocal.ai) är en lättviktig runtime som laddar ner, hanterar och betjänar språkmodeller **helt och hållet på din egen dator** genom ett OpenAI-kompatibelt API — ingen molntjänst krävs.

Eftersom Microsoft Agent Frameworks `OpenAIChatClient` fungerar med vilken OpenAI-kompatibel slutpunkt som helst, är Foundry Local ett direkt lokalt alternativ till Azure OpenAI.

**1. Installera Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Ladda ner och kör en modell** (detta startar också den lokala tjänsten):

```bash
foundry model list          # se tillgängliga modeller
foundry model run phi-4-mini
```

**3. Installera Python SDK** som används för att upptäcka den lokala slutpunkten:

```bash
pip install foundry-local-sdk
```

**4. Anslut Microsoft Agent Framework till din lokala modell:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Laddar ner (om det behövs) och tillhandahåller modellen lokalt, sedan upptäcker slutpunkten/porten.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # t.ex. http://localhost:<port>/v1
    api_key=manager.api_key,        # alltid "not-required" för Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Notis:** Foundry Local exponerar en OpenAI-kompatibel **Chat Completions**-slutpunkt. Använd den för lokal utveckling och offline-scenarier. För hela funktionen **Responses API** (tillståndsbaserade konversationer etc.), använd Azure OpenAI eller ett Microsoft Foundry-projekt.

## Ytterligare inställningar för Lektion 8 (Bing Grounding Workflow)

Det villkorliga arbetsflödesanteckningsboken i lektion 8 använder **Bing grounding** via Microsoft Foundry. Om du planerar att köra det exemplet, lägg till denna variabel i din `.env`-fil:

| Variabel | Var du hittar den |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry-portal → ditt projekt → **Management** → **Connected resources** → din Bing-anslutning → kopiera anslutnings-ID |

## Felsökning

### SSL-certifikatvalideringsfel på macOS

Om du använder macOS och får ett fel som:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Detta är ett känt problem med Python på macOS där systemets SSL-certifikat inte automatiskt litas på. Prova följande lösningar i ordning:

**Alternativ 1: Kör Pythons Install Certificates-skript (rekommenderas)**

```bash
# Ersätt 3.XX med din installerade Python-version (t.ex., 3.12 eller 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Alternativ 2: Använd `connection_verify=False` i din anteckningsbok (endast för GitHub Models-anteckningsböcker)**

I Lektion 6-anteckningsboken (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) finns redan en kommenterad lösning. Avkommentera `connection_verify=False` när du stöter på certifikatfel:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Inaktivera SSL-verifiering om du stöter på certifikatfel
)
```

> **⚠️ Varning:** Att inaktivera SSL-verifiering (`connection_verify=False`) minskar säkerheten genom att hoppa över certifikatvalidering. Använd detta bara som en tillfällig lösning i utvecklingsmiljöer. Använd det aldrig i produktion.

**Alternativ 3: Installera och använd `truststore`**

```bash
pip install truststore
```

Lägg sedan till följande högst upp i din anteckningsbok eller script innan några nätverksanrop görs:

```python
import truststore
truststore.inject_into_ssl()
```

## Fast någonstans?

Om du har några problem med att köra denna installation, hoppa in i vår <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">skapa ett ärende</a>.

## Nästa lektion

Du är nu redo att köra koden för denna kurs. Lycka till med att lära dig mer om världen av AI-agenter!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->