# Kursinstallation

## Introduktion

Den här lektionen kommer att täcka hur du kör kodexemplen i den här kursen.

## Gå med andra elever och få hjälp

Innan du börjar klona ditt repo, gå med i [AI Agents For Beginners Discord-kanal](https://aka.ms/ai-agents/discord) för att få hjälp med installationen, ställa frågor om kursen eller för att koppla ihop med andra elever.

## Klona eller Forka detta Repo

För att börja, vänligen klona eller forka GitHub-förvaret. Detta skapar din egen version av kursmaterialet så att du kan köra, testa och justera koden!

Detta kan göras genom att klicka på länken för att <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forka repot</a>

Du bör nu ha din egen forkade version av denna kurs på följande länk:

![Forkat Repo](../../../translated_images/sv/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (rekommenderas för workshop / Codespaces)

  >Det fullständiga förvaret kan vara stort (~3 GB) när du laddar ner full historik och alla filer. Om du bara deltar i workshopen eller endast behöver några lektioners mappar, undviker en shallow clone (eller en sparsom clone) det mesta av den nedladdningen genom att trunkera historiken och/eller hoppa över blobbar.

#### Snabb shallow clone — minimal historik, alla filer

Byt ut `<your-username>` i nedanstående kommandon med din fork-URL (eller upstream-URL om du föredrar det).

För att klona endast den senaste commit-historiken (liten nedladdning):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

För att klona en specifik branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partiell (sparse) clone — minimala blobbar + endast valda mappar

Detta använder partial clone och sparse-checkout (kräver Git 2.25+ och rekommenderas med modern Git med partial clone-stöd):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå in i repomappen:

```bash|powershell
cd ai-agents-for-beginners
```

Ange sedan vilka mappar du vill ha (exemplet nedan visar två mappar):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Efter kloning och verifiering av filer, om du endast behöver filer och vill frigöra utrymme (ingen git-historik), vänligen ta bort repository-metadata (💀irreversibelt — du förlorar all Git-funktionalitet: inga commits, pulls, pushes eller historikåtkomst).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Använda GitHub Codespaces (rekommenderas för att undvika lokala stora nedladdningar)

- Skapa ett nytt Codespace för detta repo via [GitHub UI](https://github.com/codespaces).  

- I terminalen i det nyss skapade Codespacet, kör ett av shallow/sparse clone-kommandona ovan för att endast ta med de lektionmappar du behöver i Codespace-arbetsytan.
- Valfritt: efter kloning inuti Codespaces, ta bort .git för att återfå extra utrymme (se raderingskommandon ovan).
- Obs: Om du föredrar att öppna repot direkt i Codespaces (utan extra kloning), var medveten om att Codespaces kommer att skapa devcontainer-miljön och kan fortfarande provisionera mer än du behöver. Att klona en shallow kopia inuti ett fräscht Codespace ger dig mer kontroll över diskutrymmet.

#### Tips

- Ersätt alltid clone-URL:en med din fork om du vill redigera/committa.
- Om du senare behöver mer historik eller filer kan du hämta dem eller justera sparse-checkout för att inkludera ytterligare mappar.

## Köra koden

Den här kursen erbjuder en serie Jupyter Notebooks som du kan köra för att få praktisk erfarenhet av att bygga AI-agenter.

Kodexemplen använder **Microsoft Agent Framework (MAF)** med `FoundryChatClient`, som ansluter till **Microsoft Foundry Agent Service V2** (Responses API) via **Microsoft Foundry**.

Alla Python-notebooks är märkta `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **OBS**: Om du inte har Python3.12 installerat, se till att installera det. Skapa sedan din venv med python3.12 för att säkerställa att rätt versioner installeras från requirements.txt-filen.
  
    >Exempel

    Skapa Python venv-katalog:

    ```bash|powershell
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

- .NET 10+: För exempel som använder .NET, säkerställ att du installerar [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller senare. Kontrollera sedan din installerade .NET SDK-version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Krävs för autentisering. Installera från [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-prenumeration** — För tillgång till Microsoft Foundry och Microsoft Foundry Agent Service.
- **Microsoft Foundry-projekt** — Ett projekt med en distribuerad modell (t.ex. `gpt-4o`). Se [Steg 1](#steg-1-skapa-ett-microsoft-foundry-projekt) nedan.

Vi har inkluderat en `requirements.txt`-fil i root förvaret som innehåller alla nödvändiga Python-paket för att köra kodexemplen.

Du kan installera dem genom att köra följande kommando i terminalen i förvarets root-mapp:

```bash|powershell
pip install -r requirements.txt
```

Vi rekommenderar att du skapar en virtuell Python-miljö för att undvika konflikter och problem.

## Konfigurera VSCode

Se till att du använder rätt Python-version i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Ställ in Microsoft Foundry och Microsoft Foundry Agent Service

### Steg 1: Skapa ett Microsoft Foundry-projekt

Du behöver en Microsoft Foundry **hub** och ett **projekt** med en distribuerad modell för att kunna köra notebooks.

1. Gå till [ai.azure.com](https://ai.azure.com) och logga in med ditt Azure-konto.
2. Skapa en **hub** (eller använd en befintlig). Se: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inuti hubben, skapa ett **projekt**.
4. Distribuera en modell (t.ex. `gpt-4o`) från **Models + Endpoints** → **Deploy model**.

### Steg 2: Hämta din projekt-endpoint och modell-distributionsnamn

Från ditt projekt i Microsoft Foundry-portalen:

- **Project Endpoint** — Gå till **Overview**-sidan och kopiera endpoint-URL:en.

![Project Connection String](../../../translated_images/sv/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Gå till **Models + Endpoints**, välj din distribuerade modell och notera **Deployment name** (t.ex. `gpt-4o`).

### Steg 3: Logga in i Azure med `az login`

Alla notebooks använder **`AzureCliCredential`** för autentisering — inga API-nycklar att hantera. Detta kräver att du är inloggad via Azure CLI.

1. **Installera Azure CLI** om du inte redan gjort det: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logga in** genom att köra:

    ```bash|powershell
    az login
    ```

    Eller om du är i en fjärr-/Codespace-miljö utan webbläsare:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Välj din prenumeration** om du blir tillfrågad — välj den som innehåller ditt Foundry-projekt.

4. **Verifiera** att du är inloggad:

    ```bash|powershell
    az account show
    ```

> **Varför `az login`?** Notebooks autentiserar med `AzureCliCredential` från `azure-identity`-paketet. Det innebär att din Azure CLI-session tillhandahåller autentiseringsuppgifterna — inga API-nycklar eller hemligheter i din `.env`-fil. Detta är en [säkerhetsrekommendation](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Steg 4: Skapa din `.env`-fil

Kopiera exempelfilen:

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variabel | Var du hittar den |
|----------|------------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portalen → ditt projekt → **Overview**-sidan |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portalen → **Models + Endpoints** → din distribuerade modells namn |

Det är allt för de flesta lektioner! Notebooks autentiserar automatiskt via din `az login`-session.

### Steg 5: Installera Python-beroenden

```bash|powershell
pip install -r requirements.txt
```

Vi rekommenderar att köra detta inuti den virtuella miljön du skapade tidigare.

## Ytterligare installation för Lektion 5 (Agentic RAG)

Lektion 5 använder **Azure AI Search** för retrieval-augmented generation. Om du planerar att köra den lektionen, lägg till dessa variabler i din `.env`-fil:

| Variabel | Var du hittar den |
|----------|------------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portalen → din **Azure AI Search**-resurs → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-portalen → din **Azure AI Search**-resurs → **Settings** → **Keys** → primär admin-nyckel |

## Ytterligare installation för lektioner som använder Azure OpenAI direkt (Lektioner 6 och 8)

Några notebooks i lektion 6 och 8 använder **Azure OpenAI** direkt (via **Responses API**) istället för att gå via ett Microsoft Foundry-projekt. Dessa exempel använde tidigare GitHub Models, vilket är deprecated (avvecklas juli 2026) och stöder inte Responses API. Om du planerar att köra dessa exempel, lägg till dessa variabler i din `.env`-fil:

| Variabel | Var du hittar den |
|----------|------------------|
| `AZURE_OPENAI_ENDPOINT` | Azure-portalen → din **Azure OpenAI**-resurs → **Keys and Endpoint** → Endpoint (t.ex. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Namnet på din distribuerade modell (t.ex. `gpt-4o-mini`) som stöder Responses API |
| `AZURE_OPENAI_API_KEY` | Valfritt — endast om du använder nyckelbaserad autentisering istället för `az login` / Entra ID |

> Responses API använder den stabila `/openai/v1/`-endpoint:en, så ingen `api-version` krävs. Logga in med `az login` för att använda nyckelfri Entra ID-autentisering.

## Alternativ leverantör: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) tillhandahåller stora kontextmodeller (upp till 204K tokens) genom en OpenAI-kompatibel API. Eftersom Microsoft Agent Frameworks `OpenAIChatClient` fungerar med vilken OpenAI-kompatibel endpoint som helst, kan du använda MiniMax som ett drop-in-alternativ till Azure OpenAI eller OpenAI.

Lägg till dessa variabler i din `.env`-fil:

| Variabel | Var du hittar den |
|----------|------------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API-nycklar |
| `MINIMAX_BASE_URL` | Använd `https://api.minimax.io/v1` (standardvärde) |
| `MINIMAX_MODEL_ID` | Modellnamnet att använda (t.ex. `MiniMax-M3`) |

**Exempelmodeller:** `MiniMax-M3` (rekommenderad), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (snabbare svar). Modellnamn och tillgänglighet kan ändras över tid, och åtkomst till en given modell kan bero på ditt konto eller region — kontrollera [MiniMax Platform](https://platform.minimaxi.com/) för aktuell lista. Om `MiniMax-M3` inte är tillgänglig för ditt konto, sätt `MINIMAX_MODEL_ID` till en modell du har tillgång till (t.ex. `MiniMax-M2.7`).

Kodexemplen som använder `OpenAIChatClient` (t.ex. Lektion 14:s hotellbokningsflöde) kommer automatiskt att upptäcka och använda din MiniMax-konfiguration när `MINIMAX_API_KEY` är satt.

## Alternativ leverantör: Foundry Local (Kör modeller lokalt)

[Foundry Local](https://foundrylocal.ai) är en lättvikts-runtime som laddar ner, hanterar och tillhandahåller språkmodeller **helt på din egen maskin** via en OpenAI-kompatibel API — ingen molnanslutning, ingen Azure-prenumeration och inga API-nycklar krävs. Det är ett utmärkt alternativ för offlineutveckling, experiment utan molnkostnader, eller för att hålla data lokalt.

Eftersom Microsoft Agent Frameworks `OpenAIChatClient` fungerar med vilken OpenAI-kompatibel endpoint som helst, är Foundry Local ett lokalt alternativ till Azure OpenAI.

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

**3. Installera Python SDK** som används för att upptäcka den lokala endpointen:

```bash
pip install foundry-local-sdk
```

**4. Rikta Microsoft Agent Framework till din lokala modell:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Laddar ner (om det behövs) och tillhandahåller modellen lokalt, sedan hittar slutpunkten/porten.
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

> **Observera:** Foundry Local exponerar en OpenAI-kompatibel **Chat Completions**-endpoint. Använd den för lokal utveckling och offline-scenarier. För det fulla **Responses API**-funktionalitetsutbudet (stateful konversationer, djup verktygsorkestrering och agentlik utveckling), rikta mot **Azure OpenAI** eller ett **Microsoft Foundry**-projekt som visas i lektionerna. Se [Foundry Local-dokumentationen](https://foundrylocal.ai) för aktuell modellkatalog och plattformsstöd.

## Ytterligare installation för Lektion 8 (Bing Grounding Workflow)
Det villkorliga arbetsflödesanteckningsboken i lektion 8 använder **Bing grounding** via Microsoft Foundry. Om du planerar att köra det exemplet, lägg till denna variabel i din `.env`-fil:

| Variable | Var du hittar den |
|----------|-------------------|
| `BING_CONNECTION_ID` | Microsoft Foundry-portal → ditt projekt → **Management** → **Connected resources** → din Bing-anslutning → kopiera anslutnings-ID |

## Felsökning

### SSL-certifikatverifieringsfel på macOS

Om du använder macOS och får ett fel som:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Detta är ett känt problem med Python på macOS där systemets SSL-certifikat inte automatiskt godkänns. Prova följande lösningar i ordning:

**Alternativ 1: Kör Pythons Install Certificates-skript (rekommenderas)**

```bash
# Byt ut 3.XX mot din installerade Python-version (t.ex. 3.12 eller 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Alternativ 2: Använd `connection_verify=False` i din anteckningsbok (endast för GitHub Models-anteckningsböcker)**

I anteckningsboken för Lektion 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), finns en utkommenterad lösning redan med. Avkommentera `connection_verify=False` när du skapar klienten:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Inaktivera SSL-verifiering om du stöter på certifikatfel
)
```

> **⚠️ Varning:** Att inaktivera SSL-verifiering (`connection_verify=False`) minskar säkerheten genom att hoppa över certifikatvalidering. Använd detta endast som en tillfällig lösning i utvecklingsmiljöer, aldrig i produktion.

**Alternativ 3: Installera och använd `truststore`**

```bash
pip install truststore
```

Lägg sedan till följande högst upp i din anteckningsbok eller skript innan du gör några nätverksanrop:

```python
import truststore
truststore.inject_into_ssl()
```

## Fast någonstans?

Om du har några problem med att köra denna uppsättning, gå med i vår <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">skapa ett ärende</a>.

## Nästa lektion

Du är nu redo att köra koden för denna kurs. Lycka till med att lära dig mer om AI-agenter!

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->