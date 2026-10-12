# Kursusopsætning

## Introduktion

Denne lektion vil dække, hvordan man kører kodeeksemplerne i dette kursus.

## Deltag med andre lærende og få hjælp

Før du begynder at klone dit repo, kan du tilslutte dig [AI Agents For Beginners Discord-kanalen](https://aka.ms/ai-agents/discord) for at få hjælp til opsætning, stille spørgsmål om kurset eller forbinde dig med andre lærende.

## Klon eller fork dette repo

For at begynde, skal du klone eller fork GitHub-repositoriet. Dette laver din egen version af kursusmaterialet, så du kan køre, teste og justere koden!

Dette kan gøres ved at klikke på linket til <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">at fork'e repoet</a>

Du burde nu have din egen forkede version af dette kursus på følgende link:

![Forked Repo](../../../translated_images/da/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (anbefales til workshop / Codespaces)

  >Det fulde repository kan være stort (~3 GB) når du downloader fuld historik og alle filer. Hvis du kun deltager i workshoppen eller kun har brug for nogle få lektions-mapper, downloader en shallow clone (eller en sparse clone) meget mindre.

#### Hurtig shallow clone — minimal historik, alle filer

Udskift `<your-username>` i kommandoerne nedenfor med din fork URL (eller upstream URL hvis du foretrækker det).

For kun at klone den seneste commit historik (lille download):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

For at klone en specifik gren:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partiell (sparse) clone — minimale blobs + kun udvalgte foldere

Dette bruger partial clone og sparse-checkout (kræver Git 2.25+ og anbefalet moderne Git med partial clone support):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå ind i repo mappen:

```bash
cd ai-agents-for-beginners
```

Angiv derefter hvilke foldere du ønsker (eksempel nedenfor viser to foldere):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Efter kloning og verifikation af filer, hvis du kun behøver filerne og vil frigive plads (ingen git historik), slet venligst repository metadata (💀irreversibelt — du mister al Git funktionalitet):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Brug af GitHub Codespaces (anbefales for at undgå store lokale downloads)

- Opret et nyt Codespace for dette repo via [GitHub UI](https://github.com/codespaces).  

- I terminalen i det nyligt oprettede codespace, kør en af de ovenstående shallow/sparse clone kommandoer for kun at hente de lektion-mapper du behøver ind i Codespace arbejdsrummet.
- Valgfrit: efter kloning inde i Codespaces, fjern .git for at frigøre ekstra plads (se fjern kommandoerne ovenfor).
- Bemærk: Hvis du foretrækker at åbne repoet direkte i Codespaces (uden ekstra kloning), vær opmærksom på, at Codespaces vil konstruere devcontainer miljøet og stadig kan provisionere mere end du behøver.

#### Tips

- Udskift altid clone URL med din fork, hvis du vil redigere/committe.
- Hvis du senere behøver mere historik eller filer, kan du hente dem eller justere sparse-checkout til at inkludere yderligere foldere.

## Køre koden

Dette kursus tilbyder en række Jupyter Notebooks, som du kan køre for at få praktisk erfaring med at bygge AI-agenter.

Kodeeksemplerne bruger **Microsoft Agent Framework (MAF)** med `FoundryChatClient`, som forbinder til **Microsoft Foundry Agent Service V2** (Responses API) gennem **Microsoft Foundry**.

Alle Python notebooks er mærket `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **BEMÆRK**: Hvis du ikke har Python3.12 installeret, skal du sikre dig, at du installerer det. Opret derefter dit venv ved brug af python3.12 for at sikre, at de korrekte versioner installeres fra requirements.txt filen.
  
    >Eksempel

    Opret Python venv mappe:

    ```bash
    python -m venv venv
    ```

    Aktiver derefter venv miljøet for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: For kodeeksemplerne der bruger .NET, skal du sikre dig, at du har installeret [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere. Tjek herefter din installerede .NET SDK version:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Påkrævet til autentificering. Installer fra [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure abonnement** — For adgang til Microsoft Foundry og Microsoft Foundry Agent Service.
- **Microsoft Foundry Projekt** — Et projekt med en deployeret model (f.eks. `gpt-5-mini`). Se [Trin 1](#trin-1-opret-et-microsoft-foundry-projekt) nedenfor.

Vi har inkluderet en `requirements.txt` fil i roden af dette repositorium, som indeholder alle nødvendige Python pakker for at køre kodeeksemplerne.

Du kan installere dem ved at køre følgende kommando i din terminal i roden af repositoriet:

```bash
pip install -r requirements.txt
```

Vi anbefaler at oprette et Python virtuelt miljø for at undgå konflikter og problemer.

## Opsætning af VSCode

Sørg for at du bruger den rigtige version af Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Opsæt Microsoft Foundry og Microsoft Foundry Agent Service

### Trin 1: Opret et Microsoft Foundry Projekt

Du har brug for et Microsoft Foundry **hub** og **projekt** med en deployeret model for at kunne køre notebooks.

1. Gå til [ai.azure.com](https://ai.azure.com) og log ind med din Azure konto.
2. Opret en **hub** (eller brug en eksisterende). Se: [Hub ressourcer oversigt](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inde i hubben, opret et **projekt**.
4. Deploy en model (f.eks. `gpt-5-mini`) fra **Models + Endpoints** → **Deploy model**.

### Trin 2: Hent dit Projekt Endepunkt og Model Deploymentsnavn

Fra dit projekt i Microsoft Foundry portalen:

- **Projekt Endepunkt** — Gå til **Oversigts** siden og kopier endpoint URL’en.

![Project Connection String](../../../translated_images/da/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deploymentsnavn** — Gå til **Models + Endpoints**, vælg din deployerede model, og se **Deployment name** (f.eks. `gpt-5-mini`).

### Trin 3: Log ind i Azure med `az login`

De fleste notebooks autentificerer via din **Azure CLI login** — ved brug af `AzureCliCredential` eller `DefaultAzureCredential` (begge bruger din `az login` session) fra `azure-identity` pakken — så de behøver ikke API-nøgler. Nogle få lektioner og valgfrie integrationer bruger API-nøgler; tjek hver lektions forudsætninger for yderligere miljøvariabler. Dette kræver, at du er logget ind via Azure CLI.

1. **Installer Azure CLI** hvis du ikke allerede har det: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Log ind** ved at køre:

    ```bash
    az login
    ```

    Eller hvis du er i et remote/Codespace miljø uden browser:

    ```bash
    az login --use-device-code
    ```

3. **Vælg dit abonnement** hvis du bliver bedt om det — vælg det, der indeholder dit Foundry projekt.

4. **Bekræft** at du er logget ind:

    ```bash
    az account show
    ```

> **Hvorfor `az login`?** Notebooks autentificerer ved brug af `AzureCliCredential` (eller `DefaultAzureCredential`, som også bruger din Azure CLI login) fra `azure-identity` pakken. Det betyder, at din Azure CLI session forsyner legitimationsoplysninger — ingen API-nøgler eller hemmeligheder i din `.env` fil. Dette er en [sikkerhedsmæssig best practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Trin 4: Opret din `.env` fil

Kopier eksempel-filen:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Åbn `.env` og udfyld disse to værdier:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variabel | Hvor finder du den |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portalen → dit projekt → **Oversigt** siden |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portalen → **Models + Endpoints** → navnet på din deployede model |

Det var det for de fleste lektioner! Notebooks vil autentificere automatisk gennem din `az login` session.

### Trin 5: Installer Python afhængigheder

```bash
pip install -r requirements.txt
```

Vi anbefaler at køre dette inde i det virtuelle miljø, du oprettede tidligere.

## Valgfri opsætning: Azure AI Search (lektioner 5 og 16)

Lektion 5 (Agentic RAG) og Lektion 16 notebooks kører ud af boksen med en **in-memory knowledge base** — ingen ekstra Azure ressourcer nødvendige. Hvis du vil understøtte dem med en rigtig **Azure AI Search** indeks, skal du bemærke, at **Lektion 16 notebookpt bruger i øjeblikket nøgle-baseret autentificering**: den skifter fra in-memory search til Azure AI Search kun når **både** `AZURE_SEARCH_SERVICE_ENDPOINT` **og** `AZURE_SEARCH_API_KEY` er sat, og ellers forbliver på in-memory search — så for at køre den mod et rigtigt indeks skal du også sætte admin-nøglen. Nøglefri autentificering med Microsoft Entra ID (RBAC) er den anbefalede tilgang til din egen produktionskode, i overensstemmelse med `az login` flowet brugt andre steder i dette kursus.

RBAC-trinene nedenfor gælder for opsætnings-guide eksemplerne og din egen kode. De aktiverer ikke nøglefri autentificering i Lektion 16 notebook; Lektion 16 kræver stadig både endepunkt og admin-nøgle for at bruge Azure AI Search.

1. **Aktiver rollebaseret adgang** til din search service:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Tildel dig selv de nødvendige roller** (opret/indlæs indices og slå op):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Tilføj endepunktet** til din `.env` fil:

| Variabel | Hvor finder du den |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portalen → din **Azure AI Search** ressource → **Oversigt** → URL |
| `AZURE_SEARCH_API_KEY` | Påkrævet (sammen med endepunkt) for at aktivere Azure AI Search i Lektion 16 notebook, som bruger nøglebaseret autentificering. Azure portalen → **Indstillinger** → **Nøgler** → primær admin nøgle |

> **Hvorfor nøglefri?** Admin nøgler giver fuld skrivetilladelse til din search service og kan lække via `.env` filer. Med RBAC bruges i stedet din `az login` identitet — det samme nøglefri Entra ID mønster som kursus notebooks bruger (via `AzureCliCredential` / `DefaultAzureCredential`). Se [Forbind til Azure AI Search med roller](https://learn.microsoft.com/azure/search/search-security-rbac).

Se [Azure AI Search opsætningsguiden](./AzureSearch.md) for komplette index-oprettelses eksempler i Python og .NET.

## Yderligere opsætning for lektioner, der kalder Azure OpenAI direkte (lektioner 6 og 8)

Nogle notebooks i lektion 6 og 8 kalder **Azure OpenAI** direkte (ved brug af **Responses API**) i stedet for at gå gennem et Microsoft Foundry projekt. Disse eksempler brugte tidligere GitHub Models, som er udfaset og understøtter ikke Responses API. Tilføj disse variabler til din `.env` fil:

| Variabel | Hvor finder du den |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portalen → din **Azure OpenAI** ressource → **Nøgler og Endpoints** → Endpoint (f.eks. `https://<din-ressource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Navnet på din deployede model (f.eks. `gpt-5-mini`) der understøtter Responses API |
| `AZURE_OPENAI_API_KEY` | Valgfri — kun hvis du bruger nøglebaseret autentificering i stedet for `az login` / Entra ID |

> Responses API bruger det stabile `/openai/v1/` endepunkt, så ingen `api-version` er påkrævet. Log ind med `az login` for at bruge nøglefri Entra ID autentificering.

## Alternativ udbyder: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) tilbyder store kontekst-modeller (op til 204K tokens) gennem en OpenAI-kompatibel API. Da Microsoft Agent Framework's `OpenAIChatClient` fungerer med ethvert OpenAI-kompatibelt endepunkt, kan du bruge MiniMax som et plug-and-play alternativ til lektioner, der bruger `OpenAIChatClient`.

Tilføj disse variabler til din `.env` fil:

| Variabel | Hvor finder du den |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Nøgler |
| `MINIMAX_BASE_URL` | Brug `https://api.minimax.io/v1` (standardværdi) |
| `MINIMAX_MODEL_ID` | Modelnavn der skal bruges (f.eks. `MiniMax-M3`) |

**Eksempelmodeller**: `MiniMax-M3` (anbefalet), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (hurtigere svar). Modelnavne og tilgængelighed kan ændre sig over tid, og adgang til en given model kan afhænge af din konto.

Kodeeksemplerne, der bruger `OpenAIChatClient` (f.eks. Lektion 14’s hotelbooking workflow), vil automatisk opdage og bruge din MiniMax konfiguration, når `MINIMAX_API_KEY` er sat.


## Alternativ Udbyder: Novita AI (OpenAI-kompatibel)

[Novita AI](https://novita.ai/llm-api) leverer en OpenAI-kompatibel API til open source og avancerede LLM'er (DeepSeek, Llama, Qwen og mere). Da Microsoft Agent Frameworks `OpenAIChatClient` fungerer med enhver OpenAI-kompatibel endepunkt, kan du bruge Novita AI som et plug-and-play alternativ til Azure OpenAI eller OpenAI.

Tilføj disse variabler til din `.env`-fil:

| Variabel | Hvor du finder den |
|----------|-------------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Nøgler |
| `NOVITA_BASE_URL` | Brug `https://api.novita.ai/openai/v1` (standardværdi) |
| `NOVITA_MODEL_ID` | Modelnavn til brug (f.eks. `moonshotai/kimi-k3`) |

**EksempelmSodeller**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI hoster også mange andre open source-modelserier (Llama, Qwen, GLM og mere) — se [Novita AI modelbiblioteket](https://novita.ai/llm-api) for den aktuelle liste over tilgængelige modeller og deres model-ID'er.

De nuværende eksempler bruger ikke automatisk `NOVITA_*` variablerne. For at bruge Novita AI, skal du eksplicit tildele disse værdier ved oprettelse af `OpenAIChatClient` i den prøve, du kører.

## Alternativ Udbyder: Foundry Local (Kør modeller på enheden)

[Foundry Local](https://foundrylocal.ai) er en letvægts runtime, der downloader, håndterer og serverer sprogmodeller **fuldstændig på din egen maskine** via en OpenAI-kompatibel API — ingen cloud krævet.

Fordi Microsoft Agent Frameworks `OpenAIChatClient` virker med enhver OpenAI-kompatibel endepunkt, er Foundry Local et plug-and-play lokalt alternativ til Azure OpenAI.

**1. Installer Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Download og kør en model** (dette starter også den lokale service):

```bash
foundry model list          # se tilgængelige modeller
foundry model run phi-4-mini
```

**3. Installer Python SDK'en** brugt til at opdage det lokale endepunkt:

```bash
pip install foundry-local-sdk
```

**4. Peg Microsoft Agent Framework mod din lokale model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Downloader (hvis nødvendigt) og server modellen lokalt, derefter opdages endpoint/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # f.eks. http://localhost:<port>/v1
    api_key=manager.api_key,        # altid "not-required" for Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Bemærk:** Foundry Local eksponerer en OpenAI-kompatibel **Chat Completions**-endepunkt. Brug den til lokal udvikling og offline scenarios. For det fulde **Responses API** funktionssæt (tilstandshåndterede samtaler osv.), brug Azure OpenAI eller et Microsoft Foundry projekt.

## Yderligere Opsætning til Lektion 8 (Bing Grounding Workflow)

Den betingede workflow-notebook i lektion 8 bruger **Bing grounding** via Microsoft Foundry. Hvis du planlægger at køre den prøve, så tilføj denne variabel til din `.env`-fil:

| Variabel | Hvor du finder den |
|----------|-------------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portalen → dit projekt → **Management** → **Connected resources** → din Bing-forbindelse → kopier forbindelses-ID |

## Fejlfinding

### SSL-Certifikatverificeringsfejl på macOS

Hvis du er på macOS og støder på en fejl som:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dette er et kendt problem med Python på macOS, hvor systemets SSL-certifikater ikke automatisk betros. Prøv følgende løsninger i rækkefølge:

**Mulighed 1: Kør Pythons Install Certificates script (anbefalet)**

```bash
# Erstat 3.XX med din installerede Python-version (f.eks. 3.12 eller 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Mulighed 2: Brug `connection_verify=False` i din notebook (kun for GitHub Models notebooks)**

I Lesson 6-notebooken (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) er en kommenteret workaround allerede inkluderet. Fjern kommentaren på `connection_verify=False` når du rammer certifikatfejl:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktiver SSL-verificering, hvis du støder på certifikatfejl
)
```

> **⚠️ Advarsel:** Deaktivering af SSL-verificering (`connection_verify=False`) reducerer sikkerheden ved at springe certifikatvalidering over. Brug dette kun som en midlertidig løsning i udviklingsmiljøer. Brug det aldrig i produktion.

**Mulighed 3: Installer og brug `truststore`**

```bash
pip install truststore
```

Tilføj derefter følgende øverst i din notebook eller script, før du laver netværkskald:

```python
import truststore
truststore.inject_into_ssl()
```

## Stuck et sted?

Hvis du har problemer med at køre denne opsætning, så hop ind i vores <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">opret en issue</a>.

## Næste Lektion

Du er nu klar til at køre koden for dette kursus. God fornøjelse med at lære mere om AI Agents-verdenen! 

[Introduktion til AI Agents og Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->