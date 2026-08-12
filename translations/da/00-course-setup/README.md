# Kursusopsætning

## Introduktion

Denne lektion vil dække, hvordan man kører kodeeksemplerne i dette kursus.

## Deltag med andre lærende og få hjælp

Før du begynder at klone dit repo, så deltag i [AI Agents For Beginners Discord-kanalen](https://aka.ms/ai-agents/discord) for at få hjælp til opsætning, stille spørgsmål om kurset eller forbinde dig med andre lærende.

## Klon eller Fork dette Repo

For at komme i gang, skal du klone eller forke GitHub-repositoriet. Dette laver din egen version af kursusmaterialet, så du kan køre, teste og justere koden!

Dette kan gøres ved at klikke på linket til <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">at forke repoet</a>

Du skulle nu have din egen forkede version af dette kursus på følgende link:

![Forked Repo](../../../translated_images/da/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (anbefalet til workshop / Codespaces)

  >Det fulde repository kan være stort (~3 GB), når du downloader hele historikken og alle filer. Hvis du kun deltager i workshoppen eller kun har brug for nogle få lektionmapper, undgår en shallow clone (eller en sparse clone) det meste af denne download ved at forkorte historikken og/eller springe blobs over.

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

#### Delvis (sparse) clone — minimale blobs + kun valgte mapper

Dette bruger partial clone og sparse-checkout (kræver Git 2.25+ og anbefalet moderne Git med partial clone support):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå ind i repo mappen:

```bash|powershell
cd ai-agents-for-beginners
```

Angiv derefter hvilke mapper du ønsker (eksemplet nedenfor viser to mapper):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Efter kloning og verifikation af filerne, hvis du kun har brug for filerne og vil frigøre plads (ingen git-historik), slet da repository metadata (💀irreversibelt — du mister al Git funktionalitet: ingen commits, pulls, pushes eller historik adgang).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Brug af GitHub Codespaces (anbefalet for at undgå store lokale downloads)

- Opret et nyt Codespace til dette repo via [GitHub UI](https://github.com/codespaces).  

- Kør i terminalen i det nyoprettede codespace en af shallow/sparse clone kommandoerne ovenfor for kun at få de lektionmapper, du har brug for ind i Codespace workspace.
- Valgfrit: efter kloning inde i Codespaces, fjern .git for at få ekstra plads (se fjernelseskoder ovenfor).
- Bemærk: Hvis du foretrækker at åbne repoet direkte i Codespaces (uden ekstra cloning), så vær opmærksom på, at Codespaces opretter devcontainer miljøet og kan stadig provisionere mere end du behøver. Ved at klone et shallow kopi inde i et frisk Codespace får du bedre kontrol over disk-forbruget.

#### Tips

- Udskift altid clone URL med din fork, hvis du ønsker at redigere/committe.
- Hvis du senere har brug for mere historik eller filer, kan du hente dem eller justere sparse-checkout til at inkludere yderligere mapper.

## Køre Koden

Dette kursus tilbyder en serie af Jupyter Notebooks, som du kan køre for at få praktisk erfaring med at bygge AI-agenter.

Kodeeksemplerne bruger **Microsoft Agent Framework (MAF)** med `FoundryChatClient`, som forbinder til **Microsoft Foundry Agent Service V2** (Responses API) gennem **Microsoft Foundry**.

Alle Python notebooks er mærket `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **NOTE**: Hvis du ikke har installeret Python3.12, så sørg for at installere det. Opret derefter dit venv ved hjælp af python3.12 for at sikre, at de korrekte versioner installeres fra requirements.txt filen.
  
    >Eksempel

    Opret Python venv mappe:

    ```bash|powershell
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

- .NET 10+: For eksempel koden der bruger .NET, sørg for at installere [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere. Tjek derefter din installerede .NET SDK version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Krævet for autentificering. Installer fra [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — For adgang til Microsoft Foundry og Microsoft Foundry Agent Service.
- **Microsoft Foundry Projekt** — Et projekt med en implementeret model (f.eks. `gpt-5-mini`). Se [Trin 1](#trin-1-opret-et-microsoft-foundry-projekt) nedenfor.

Vi har inkluderet en `requirements.txt` fil i roden af dette repository, som indeholder alle nødvendige Python-pakker til at køre kodeeksemplerne.

Du kan installere dem ved at køre følgende kommando i din terminal i roden af repositoryet:

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler at oprette et Python virtuelt miljø for at undgå konflikter og problemer.

## Opsætning af VSCode

Sørg for, at du bruger den rigtige version af Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Opsæt Microsoft Foundry og Microsoft Foundry Agent Service

### Trin 1: Opret et Microsoft Foundry Projekt

Du skal bruge et Microsoft Foundry **hub** og **projekt** med en implementeret model for at kunne køre notebooks.

1. Gå til [ai.azure.com](https://ai.azure.com) og log ind med din Azure konto.
2. Opret en **hub** (eller brug en eksisterende). Se: [Hub ressources oversigt](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inde i hubben, opret et **projekt**.
4. Implementer en model (f.eks. `gpt-5-mini`) fra **Models + Endpoints** → **Deploy model**.

### Trin 2: Hent dit projekt endpoint og modelimplementeringsnavn

Fra dit projekt i Microsoft Foundry portalen:

- **Project Endpoint** — Gå til **Oversigt** siden og kopier endpoint URL'en.

![Project Connection String](../../../translated_images/da/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Gå til **Models + Endpoints**, vælg din implementerede model, og noter **Deployment name** (f.eks. `gpt-5-mini`).

### Trin 3: Log ind på Azure med `az login`

Alle notebooks bruger **`AzureCliCredential`** til autentificering — ingen API-nøgler at administrere. Det kræver, at du er logget ind via Azure CLI.

1. **Installer Azure CLI** hvis du ikke allerede har det: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Log ind** ved at køre:

    ```bash|powershell
    az login
    ```

    Eller hvis du er i et remote/Codespace miljø uden browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vælg dit abonnement** hvis du bliver bedt om det — vælg det, der indeholder dit Foundry projekt.

4. **Bekræft** du er logget ind:

    ```bash|powershell
    az account show
    ```

> **Hvorfor `az login`?** Notebooks autentificerer ved hjælp af `AzureCliCredential` fra `azure-identity` pakken. Det betyder, at din Azure CLI session leverer legitimationsoplysningerne — ingen API-nøgler eller hemmeligheder i din `.env` fil. Dette er en [bedste praksis for sikkerhed](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portal → dit projekt → **Oversigt** siden |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portal → **Models + Endpoints** → navnet på din implementerede model |

Det var det for de fleste lektioner! Notebooks vil automatisk autentificere gennem din `az login` session.

### Trin 5: Installer Python-afhængigheder

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler at køre dette inde i det virtuelle miljø, du oprettede tidligere.

## Yderligere opsætning for Lektion 5 (Agentic RAG)

Lektion 5 bruger **Azure AI Search** til retrieval-augmenteret generering. Hvis du planlægger at køre den lektion, tilføj da disse variabler til din `.env` fil:

| Variabel | Hvor finder du den |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portalen → din **Azure AI Search** ressource → **Oversigt** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-portalen → din **Azure AI Search** ressource → **Indstillinger** → **Nøgler** → primær administrator nøgle |

## Yderligere opsætning for lektioner der kalder Azure OpenAI direkte (lektioner 6 og 8)

Nogle notebooks i lektion 6 og 8 kalder **Azure OpenAI** direkte (ved brug af **Responses API**) i stedet for at gå gennem et Microsoft Foundry projekt. Disse eksempler brugte tidligere GitHub Models, som er forældet (udfaset juli 2026) og understøtter ikke Responses API. Hvis du planlægger at køre disse eksempler, tilføj da disse variabler til din `.env` fil:

| Variabel | Hvor finder du den |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure-portalen → din **Azure OpenAI** ressource → **Nøgler og Endpoint** → Endpoint (f.eks. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Navnet på din implementerede model (f.eks. `gpt-5-mini`) der understøtter Responses API |
| `AZURE_OPENAI_API_KEY` | Valgfri — kun hvis du bruger nøglebaseret autentificering i stedet for `az login` / Entra ID |

> Responses API bruger den stabile `/openai/v1/` endpoint, så ingen `api-version` er nødvendig. Log ind med `az login` for at bruge nøglefri Entra ID autentificering.

## Alternativ udbyder: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) tilbyder modeller med stort kontekstvindue (op til 204K tokens) via en OpenAI-kompatibel API. Eftersom Microsoft Agent Framework's `OpenAIChatClient` fungerer med enhver OpenAI-kompatibel endpoint, kan du bruge MiniMax som et plug-and-play alternativ til Azure OpenAI eller OpenAI.

Tilføj disse variabler til din `.env` fil:

| Variabel | Hvor finder du den |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API-nøgler |
| `MINIMAX_BASE_URL` | Brug `https://api.minimax.io/v1` (standardværdi) |
| `MINIMAX_MODEL_ID` | Modelnavnet der skal bruges (f.eks., `MiniMax-M3`) |

**Eksempelmodeller**: `MiniMax-M3` (anbefalet), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (hurtigere svar). Modelnavne og tilgængelighed kan ændre sig over tid, og adgang til en given model kan afhænge af din konto eller region — tjek [MiniMax Platform](https://platform.minimaxi.com/) for den aktuelle liste. Hvis `MiniMax-M3` ikke er tilgængelig for din konto, sæt `MINIMAX_MODEL_ID` til en model du har adgang til (f.eks. `MiniMax-M2.7`).

Kodeeksemplerne der bruger `OpenAIChatClient` (f.eks. Lektion 14 hotel booking workflow) vil automatisk detektere og bruge din MiniMax-konfiguration når `MINIMAX_API_KEY` er sat.

## Alternativ udbyder: Foundry Local (Kør modeller lokalt)

[Foundry Local](https://foundrylocal.ai) er en letvægts runtime, der downloader, administrerer og tjener sprogmodeller **helt på din egen maskine** gennem en OpenAI-kompatibel API — ingen cloud, ingen Azure abonnement, og ingen API-nøgler. Det er et fremragende valg til offline-udvikling, eksperimenter uden cloud-omkostninger, eller at holde data på enheden.

Fordi Microsoft Agent Framework's `OpenAIChatClient` fungerer med enhver OpenAI-kompatibel endpoint, er Foundry Local et lokalt plug-and-play alternativ til Azure OpenAI.

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

**3. Installer Python SDK'en** brugt til at finde den lokale endpoint:

```bash
pip install foundry-local-sdk
```

**4. Peg Microsoft Agent Framework til din lokale model:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Downloader (om nødvendigt) og tjener modellen lokalt, derefter opdager endpoint/port.
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

> **Bemærk:** Foundry Local udsætter en OpenAI-kompatibel **Chat Completions** endpoint. Brug den til lokal udvikling og offline scenarier. For det fulde **Responses API** funktionssæt (stateful samtaler, dyb værktøjsorkestrering og agent-stil udvikling), målret mod **Azure OpenAI** eller et **Microsoft Foundry** projekt som vist i lektionerne. Se [Foundry Local dokumentationen](https://foundrylocal.ai) for den aktuelle modelkatalog og platformunderstøttelse.

## Yderligere opsætning for Lektion 8 (Bing Grounding Workflow)


Det betingede workflow-notebook i lektion 8 bruger **Bing grounding** via Microsoft Foundry. Hvis du planlægger at køre det eksempel, skal du tilføje denne variabel til din `.env`-fil:

| Variabel | Hvor du finder den |
|----------|-------------------|
| `BING_CONNECTION_ID` | Microsoft Foundry-portalen → dit projekt → **Management** → **Connected resources** → din Bing-forbindelse → kopier forbindelses-ID'et |

## Fejlfinding

### SSL-certifikatverifikationsfejl på macOS

Hvis du er på macOS og støder på en fejl som:

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

I Lektion 6-notebooken (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) er en kommentar med en løsning allerede inkluderet. Fjern kommentaren på `connection_verify=False` når klienten oprettes:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktiver SSL-verifikation, hvis du støder på certifikatfejl
)
```

> **⚠️ Advarsel:** Deaktivering af SSL-verifikation (`connection_verify=False`) reducerer sikkerheden ved at springe certifikatvalidering over. Brug dette kun som en midlertidig løsning i udviklingsmiljøer, aldrig i produktion.

**Mulighed 3: Installer og brug `truststore`**

```bash
pip install truststore
```

Tilføj derefter følgende øverst i din notebook eller script, før du foretager netværkskald:

```python
import truststore
truststore.inject_into_ssl()
```

## Stuck et sted?

Hvis du har problemer med at køre denne opsætning, kan du hoppe ind i vores <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">oprette en issue</a>.

## Næste lektion

Du er nu klar til at køre koden til dette kursus. God fornøjelse med at lære mere om AI-agenternes verden! 

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->