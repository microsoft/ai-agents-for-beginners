# Kursusopsætning

## Introduktion

Denne lektion vil dække, hvordan du kører kodeeksemplerne i dette kursus.

## Deltag i andre elever og få hjælp

Før du begynder at klone dit repo, så deltag i [AI Agents For Beginners Discord-kanalen](https://aka.ms/ai-agents/discord) for at få hjælp med opsætningen, stille spørgsmål om kurset eller for at forbinde med andre elever.

## Klon eller fork dette repo

For at begynde, klon eller fork venligst GitHub-repositoriet. Dette laver din egen version af kursusmaterialet, så du kan køre, teste og justere koden!

Dette kan gøres ved at klikke på linket til <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">fork repoet</a>

Du burde nu have din egen forkede version af dette kursus på følgende link:

![Forket Repo](../../../translated_images/da/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (anbefalet til workshop / Codespaces)

  >Det fulde repositorium kan være stort (~3 GB), når du downloader hele historikken og alle filer. Hvis du kun deltager i workshoppen eller kun har brug for et par lektioner, undgår en shallow clone (eller en sparsom clone) det meste af denne download ved at forkorte historikken og/eller springe blobs over.

#### Hurtig shallow clone — minimal historik, alle filer

Erstat `<your-username>` i kommandoerne nedenfor med din fork URL (eller upstream URL hvis du foretrækker det).

For kun at klone den seneste commit-historik (lille download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

For at klone en specifik gren:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delvis (sparsom) clone — minimale blobs + kun valgte mapper

Dette bruger delvis clone og sparse-checkout (kræver Git 2.25+ og anbefales med moderne Git, der understøtter delvis clone):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå ind i repo-mappen:

```bash|powershell
cd ai-agents-for-beginners
```

Angiv derefter, hvilke mapper du ønsker (eksempel nedenfor viser to mapper):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Efter kloning og verificering af filerne, hvis du kun har brug for filerne og vil frigøre plads (ingen git-historik), så slet repository-metadatarne (💀uforstørlig — du mister al Git-funktionalitet: ingen commits, pulls, pushes eller adgang til historik).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Brug af GitHub Codespaces (anbefalet for at undgå store lokale downloads)

- Opret et nyt Codespace for dette repo via [GitHub UI](https://github.com/codespaces).  

- I terminalen for det nyligt oprettede codespace, kør en af shallow/sparse clone-kommandoerne ovenfor for kun at bringe de lektionmapper ind, du har brug for i Codespace-arbejdsområdet.
- Valgfrit: efter kloning inde i Codespaces, fjern .git for at få ekstra plads tilbage (se slettekommandoer ovenfor).
- Bemærk: Hvis du foretrækker at åbne repoet direkte i Codespaces (uden ekstra clone), skal du være opmærksom på, at Codespaces opbygger devcontainer-miljøet og stadig kan provisionere mere, end du har brug for. En shallow copy clone inde i en frisk Codespace giver mere kontrol over diskforbruget.

#### Tips

- Udskift altid clone URL'en med din fork, hvis du vil redigere/committe.
- Hvis du senere har brug for mere historik eller filer, kan du hente dem eller justere sparse-checkout for at inkludere flere mapper.

## Kørsel af koden

Dette kursus tilbyder en serie af Jupyter Notebooks, som du kan køre for at få praktisk erfaring med at bygge AI-agenter.

Kodeeksemplerne bruger **Microsoft Agent Framework (MAF)** med `FoundryChatClient`, som forbinder til **Microsoft Foundry Agent Service V2** (Responses API) gennem **Microsoft Foundry**.

Alle Python notebooks er mærket `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **NOTE**: Hvis du ikke har Python3.12 installeret, skal du sikre dig at installere det. Opret derefter dit venv ved hjælp af python3.12 for at sikre de korrekte versioner installeres fra requirements.txt-filen.
  
    >Eksempel

    Opret Python venv-mappe:

    ```bash|powershell
    python -m venv venv
    ```

    Aktivér derefter venv-miljøet for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: For eksempelkode, der bruger .NET, skal du sikre dig at installere [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere. Tjek derefter hvilken .NET SDK version du har installeret:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Påkrævet for autentificering. Installer fra [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — For adgang til Microsoft Foundry og Microsoft Foundry Agent Service.
- **Microsoft Foundry Project** — Et projekt med en udrullet model (fx `gpt-4o`). Se [Trin 1](#trin-1-opret-et-microsoft-foundry-projekt) nedenfor.

Vi har inkluderet en `requirements.txt` fil i roden af dette repository, som indeholder alle nødvendige Python-pakker til at køre kodeeksemplerne.

Du kan installere dem ved at køre følgende kommando i dit terminalvindue i roden af repositoriet:

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler at oprette et Python virtual environment for at undgå konflikter og problemer.

## Opsæt VSCode

Sørg for, at du bruger den rigtige Python-version i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Opsæt Microsoft Foundry og Microsoft Foundry Agent Service

### Trin 1: Opret et Microsoft Foundry-projekt

Du skal bruge en Microsoft Foundry **hub** og et **projekt** med en udrullet model for at køre notebooks.

1. Gå til [ai.azure.com](https://ai.azure.com) og log ind med din Azure-konto.
2. Opret en **hub** (eller brug en eksisterende). Se: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Opret en **projekt** inde i hubben.
4. Udrul en model (fx `gpt-4o`) fra **Models + Endpoints** → **Deploy model**.

### Trin 2: Hent dit projekts endpoint og modeldeploymentsnavn

Fra dit projekt i Microsoft Foundry-portalen:

- **Project Endpoint** — Gå til **Oversigt** siden og kopier endpoint-URL'en.

![Project Connection String](../../../translated_images/da/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Gå til **Models + Endpoints**, vælg din udrullede model, og noter **Deployment name** (fx `gpt-4o`).

### Trin 3: Log ind på Azure med `az login`

Alle notebooks bruger **`AzureCliCredential`** til autentificering — ingen API-nøgler at håndtere. Dette kræver, at du er logget ind via Azure CLI.

1. **Installer Azure CLI** hvis du ikke allerede har det: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Log ind** ved at køre:

    ```bash|powershell
    az login
    ```

    Eller hvis du er i et fjern-/Codespace-miljø uden browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vælg dit abonnement** hvis du bliver bedt om det — vælg det, der indeholder dit Foundry-projekt.

4. **Bekræft** at du er logget ind:

    ```bash|powershell
    az account show
    ```

> **Hvorfor `az login`?** Notebooks autentificerer med `AzureCliCredential` fra `azure-identity` pakken. Det betyder, at din Azure CLI session leverer legitimationsoplysningerne — ingen API-nøgler eller hemmeligheder i din `.env` fil. Dette er en [bedste sikkerhedspraksis](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Trin 4: Opret din `.env` fil

Kopiér eksempel-filen:

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variabel | Hvor findes den |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → dit projekt → **Oversigt** side |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → navnet på din udrullede model |

Det var det for de fleste lektioner! Notebooks vil automatisk autentificere gennem din `az login` session.

### Trin 5: Installer Python-afhængigheder

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler at køre dette inden i det virtuelle miljø, som du oprettede tidligere.

## Yderligere opsætning for lektion 5 (Agentic RAG)

Lektion 5 bruger **Azure AI Search** til retrieval-augmented generation. Hvis du planlægger at køre denne lektion, tilføj disse variabler til din `.env` fil:

| Variabel | Hvor findes den |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portal → din **Azure AI Search** ressource → **Oversigt** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portal → din **Azure AI Search** ressource → **Indstillinger** → **Nøgler** → primær admin-nøgle |

## Yderligere opsætning for lektioner, der kalder Azure OpenAI direkte (Lektion 6 og 8)

Nogle notebooks i lektion 6 og 8 kalder **Azure OpenAI** direkte (ved hjælp af **Responses API**) i stedet for at gå gennem et Microsoft Foundry-projekt. Disse eksempler brugte tidligere GitHub Models, som er udfaset (udgår juli 2026) og understøtter ikke Responses API. Hvis du planlægger at køre disse eksempler, tilføj disse variabler til din `.env` fil:

| Variabel | Hvor findes den |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portal → din **Azure OpenAI** ressource → **Nøgler og Endpoint** → Endpoint (fx `https://<din-ressource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Navnet på din udrullede model (fx `gpt-4o-mini`), der understøtter Responses API |
| `AZURE_OPENAI_API_KEY` | Valgfrit — kun hvis du bruger nøglebaseret autentificering i stedet for `az login` / Entra ID |

> Responses API bruger det stabile `/openai/v1/` endpoint, så der kræves ingen `api-version`. Log ind med `az login` for at bruge nøglefri Entra ID autentificering.

## Alternativ udbyder: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) leverer store kontekstmodeller (op til 204K tokens) gennem en OpenAI-kompatibel API. Da Microsoft Agent Frameworks `OpenAIChatClient` virker med alle OpenAI-kompatible endpoints, kan du bruge MiniMax som et drop-in alternativ til Azure OpenAI eller OpenAI.

Tilføj disse variabler til din `.env` fil:

| Variabel | Hvor findes den |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API-nøgler |
| `MINIMAX_BASE_URL` | Brug `https://api.minimax.io/v1` (standardværdi) |
| `MINIMAX_MODEL_ID` | Modelnavn til brug (fx `MiniMax-M3`) |

**Eksempelmodeller**: `MiniMax-M3` (anbefalet), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (hurtigere responser). Modelnavne og tilgængelighed kan ændre sig over tid, og adgang til en given model kan afhænge af din konto eller region — tjek [MiniMax Platform](https://platform.minimaxi.com/) for den aktuelle liste. Hvis `MiniMax-M3` ikke er tilgængelig for din konto, sæt `MINIMAX_MODEL_ID` til en model, du har adgang til (fx `MiniMax-M2.7`).

De kodeeksempler, der bruger `OpenAIChatClient` (fx Lektion 14 hotel booking workflow) vil automatisk registrere og bruge din MiniMax-konfiguration, når `MINIMAX_API_KEY` er sat.

## Alternativ udbyder: Foundry Local (kør modeller på enheden)

[Foundry Local](https://foundrylocal.ai) er en let runtime, der downloader, administrerer og servicerer sprogmodeller **helt på din egen maskine** gennem en OpenAI-kompatibel API — ingen cloud, ingen Azure abonnement, og ingen API-nøgler. Det er et godt valg til offline udvikling, eksperimenter uden omkostninger i skyen, eller for at holde data på enheden.

Fordi Microsoft Agent Frameworks `OpenAIChatClient` virker med alle OpenAI-kompatible endpoints, er Foundry Local et drop-in lokalt alternativ til Azure OpenAI.

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

**3. Installer Python SDK** brugt til at opdage det lokale endpoint:

```bash
pip install foundry-local-sdk
```

**4. Peg Microsoft Agent Framework mod din lokale model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Downloader (om nødvendigt) og betjener modellen lokalt, derefter opdager endpoint/porten.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # f.eks. http://localhost:<port>/v1
    api_key=manager.api_key,        # altid "ikke-påkrævet" for Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Bemærk:** Foundry Local eksponerer et OpenAI-kompatibelt **Chat Completions** endpoint. Brug det til lokal udvikling og offline scenarier. For det fulde **Responses API** funktionssæt (stateful samtaler, dyb værktøjsorkestrering og agent-stil udvikling), ret mod **Azure OpenAI** eller et **Microsoft Foundry** projekt som vist i lektionerne. Se den [Foundry Local dokumentation](https://foundrylocal.ai) for den aktuelle modelliste og platformsupport.

## Yderligere opsætning for lektion 8 (Bing Grounding Workflow)


Den betingede workflow-notebook i lektion 8 bruger **Bing grounding** via Microsoft Foundry. Hvis du planlægger at køre det eksempel, skal du tilføje denne variabel til din `.env`-fil:

| Variabel | Hvor du finder den |
|----------|-------------------|
| `BING_CONNECTION_ID` | Microsoft Foundry-portalen → dit projekt → **Management** → **Connected resources** → din Bing-forbindelse → kopier forbindelses-ID'et |

## Fejlfinding

### SSL-certifikatverifikationsfejl på macOS

Hvis du bruger macOS og støder på en fejl som:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dette er et kendt problem med Python på macOS, hvor systemets SSL-certifikater ikke automatisk godkendes. Prøv følgende løsninger i rækkefølge:

**Mulighed 1: Kør Pythons Install Certificates-script (anbefalet)**

```bash
# Erstat 3.XX med din installerede Python-version (f.eks. 3.12 eller 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Mulighed 2: Brug `connection_verify=False` i din notebook (kun for GitHub Models-notebooks)**

I Lesson 6-notebooken (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) er der allerede inkluderet en udkommenteret løsning. Fjern kommentaren fra `connection_verify=False`, når du opretter klienten:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktiver SSL-verificering, hvis du støder på certifikatfejl
)
```

> **⚠️ Advarsel:** Deaktivering af SSL-verifikation (`connection_verify=False`) nedsætter sikkerheden ved at springe certifikatvalidering over. Brug dette kun som en midlertidig løsning i udviklingsmiljøer, aldrig i produktion.

**Mulighed 3: Installer og brug `truststore`**

```bash
pip install truststore
```

Tilføj derefter følgende øverst i din notebook eller dit script, før du foretager netværksopkald:

```python
import truststore
truststore.inject_into_ssl()
```

## Sidder du fast et sted?

Hvis du har problemer med at køre denne opsætning, kan du hoppe ind i vores <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">oprette en issue</a>.

## Næste lektion

Du er nu klar til at køre koden til dette kursus. God fornøjelse med at lære mere om AI-agenterens verden! 

[Introduktion til AI-agenter og agentanvendelsestilfælde](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->