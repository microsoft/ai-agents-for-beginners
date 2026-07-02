# Kursusopsætning

## Introduktion

Denne lektion vil dække, hvordan du kører kodeeksemplerne i dette kursus.

## Deltag med Andre Lærende og Få Hjælp

Før du begynder at klone dit repo, kan du tilslutte dig [AI Agents For Beginners Discord-kanalen](https://aka.ms/ai-agents/discord) for at få hjælp til opsætning, stille spørgsmål om kurset eller for at komme i kontakt med andre lærende.

## Klon eller Fork dette Repo

For at komme i gang, skal du klone eller forke GitHub-repositoriet. Dette vil lave din egen version af kursusmaterialet, så du kan køre, teste og justere koden!

Dette kan gøres ved at klikke på linket til <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">at forke repoet</a>

Du bør nu have din egen forke version af dette kursus på følgende link:

![Forked Repo](../../../translated_images/da/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (anbefalet til workshop / Codespaces)

  >Det fulde repositorium kan være stort (~3 GB) når du downloader hele historikken og alle filer. Hvis du kun deltager i workshoppen eller kun har brug for et par lektionsmapper, undgår en shallow clone (eller en sparse clone) det meste af denne download ved at afkorte historikken og/eller springe blobs over.

#### Hurtig shallow clone — minimal historik, alle filer

Erstat `<your-username>` i kommandoerne nedenfor med din fork URL (eller upstream URL hvis du foretrækker det).

For kun at klone den seneste commit historik (lille download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

For at klone en specifik gren:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partiell (sparse) clone — minimale blobs + kun udvalgte mapper

Dette bruger partial clone og sparse-checkout (kræver Git 2.25+ og anbefales med moderne Git med partial clone support):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Naviger ind i repo mappen:

```bash|powershell
cd ai-agents-for-beginners
```

Angiv derefter, hvilke mapper du ønsker (eksemplet nedenfor viser to mapper):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Efter kloning og verifikation af filerne, hvis du kun har brug for filerne og ønsker at frigøre plads (ingen git historie), slet venligst repositories metadata (💀irreversibelt — du mister al Git funktionalitet: ingen commits, pulls, pushes eller historik adgang).

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

- Kør i terminalen i det nyoprettede codespace en af shallow/sparse clone kommandoerne ovenfor for kun at få lektionsmapperne, du skal bruge, ind i Codespace arbejdsområdet.
- Valgfrit: efter kloning inde i Codespaces, fjern .git for at frigøre ekstra plads (se fjernelseskoder ovenfor).
- Bemærk: Hvis du foretrækker at åbne repoet direkte i Codespaces (uden ekstra clone), skal du være opmærksom på, at Codespaces vil konstruere devcontainer-miljøet og måske stadig provisionere mere, end du har brug for. At klone en shallow kopi inde i et nyt Codespace giver dig mere kontrol over diskforbruget.

#### Tips

- Erstat altid clone URL’en med din fork, hvis du vil redigere/committe.
- Hvis du senere har brug for mere historik eller filer, kan du hente dem eller justere sparse-checkout for at inkludere flere mapper.

## Kørsel af Koden

Dette kursus tilbyder en række Jupyter Notebooks, som du kan køre for at få praktisk erfaring med at bygge AI-agenter.

Kodeeksemplerne bruger **Microsoft Agent Framework (MAF)** med `AzureAIProjectAgentProvider`, som forbinder til **Azure AI Agent Service V2** (Respons-API'en) via **Microsoft Foundry**.

Alle Python-notebooks er mærket `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **NOTE**: Hvis du ikke har Python3.12 installeret, skal du sørge for at installere det. Opret derefter dit venv ved at bruge python3.12 for at sikre, at de korrekte versioner installeres fra requirements.txt filen.
  
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

- .NET 10+: For eksempelkoder, der bruger .NET, skal du sikre dig, at du har installeret [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere. Tjek derefter din installerede .NET SDK version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Påkrævet til autentificering. Installer fra [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — For adgang til Microsoft Foundry og Azure AI Agent Service.
- **Microsoft Foundry-projekt** — Et projekt med en udrullet model (f.eks. `gpt-4o`). Se [Trin 1](#trin-1-opret-et-microsoft-foundry-projekt) nedenfor.

Vi har inkluderet en `requirements.txt` fil i roden af dette repo, som indeholder alle nødvendige Python-pakker for at køre kodeeksemplerne.

Du kan installere dem ved at køre følgende kommando i din terminal i roden af repoet:

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler at oprette et Python virtuelt miljø for at undgå konflikter og problemer.

## Opsæt VSCode

Sørg for, at du bruger den rigtige version af Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Opsæt Microsoft Foundry og Azure AI Agent Service

### Trin 1: Opret et Microsoft Foundry-projekt

Du skal bruge en Azure AI Foundry **hub** og et **projekt** med en udrullet model for at køre notebooks.

1. Gå til [ai.azure.com](https://ai.azure.com) og log ind med din Azure-konto.
2. Opret en **hub** (eller brug en eksisterende). Se: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inden i hubben, opret et **projekt**.
4. Udrul en model (f.eks. `gpt-4o`) fra **Models + Endpoints** → **Deploy model**.

### Trin 2: Hent dit projekt-endpoint og modeludrulningsnavn

Fra dit projekt i Microsoft Foundry-portalen:

- **Project Endpoint** — Gå til **Overview** siden og kopier endpoint URL'en.

![Project Connection String](../../../translated_images/da/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Gå til **Models + Endpoints**, vælg din udrullede model, og noter **Deployment name** (f.eks. `gpt-4o`).

### Trin 3: Log ind i Azure med `az login`

Alle notebooks bruger **`AzureCliCredential`** til autentificering — ingen API-nøgler at administrere. Det kræver, at du er logget ind via Azure CLI.

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

> **Hvorfor `az login`?** Notebooks autentificerer ved hjælp af `AzureCliCredential` fra `azure-identity` pakken. Det betyder, at din Azure CLI-session leverer legitimationsoplysningerne — ingen API-nøgler eller hemmeligheder i din `.env` fil. Dette er en [sikkerhedspraksis](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portal → dit projekt → **Overview** siden |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portal → **Models + Endpoints** → din udrullede models navn |

Det var det for de fleste lektioner! Notebooks vil autentificere automatisk via din `az login` session.

### Trin 5: Installer Python-afhængigheder

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler at køre dette inde i det virtuelle miljø, du oprettede tidligere.

## Yderligere Opsætning til Lektion 5 (Agentic RAG)

Lektion 5 bruger **Azure AI Search** til retrieval-augmented generation. Hvis du planlægger at køre denne lektion, tilføj disse variabler til din `.env` fil:

| Variabel | Hvor findes den |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portalen → din **Azure AI Search** ressource → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-portalen → din **Azure AI Search** ressource → **Settings** → **Keys** → primær administrator-nøgle |

## Yderligere Opsætning til Lektion 6 og Lektion 8 (GitHub Models)

Nogle notebooks i lektion 6 og 8 bruger **GitHub Models** i stedet for Azure AI Foundry. Hvis du planlægger at køre disse eksempler, tilføj disse variabler til din `.env` fil:

| Variabel | Hvor findes den |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Brug `https://models.inference.ai.azure.com` (standardværdi) |
| `GITHUB_MODEL_ID` | Modelnavn at bruge (f.eks. `gpt-4o-mini`) |

## Alternativ Udbyder: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) tilbyder store kontekstmodeller (op til 204K tokens) via en OpenAI-kompatibel API. Da Microsoft Agent Frameworks `OpenAIChatClient` fungerer med enhver OpenAI-kompatibel endpoint, kan du bruge MiniMax som et drop-in alternativ til GitHub Models eller OpenAI.

Tilføj disse variabler til din `.env` fil:

| Variabel | Hvor findes den |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API-nøgler |
| `MINIMAX_BASE_URL` | Brug `https://api.minimax.io/v1` (standardværdi) |
| `MINIMAX_MODEL_ID` | Modelnavn at bruge (f.eks. `MiniMax-M3`) |

**Eksempelmarter**: `MiniMax-M3` (anbefalet), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (hurtigere svar). Modelnavne og tilgængelighed kan ændre sig over tid, og adgang til en given model kan afhænge af din konto eller region — tjek [MiniMax Platform](https://platform.minimaxi.com/) for den aktuelle liste. Hvis `MiniMax-M3` ikke er tilgængelig for din konto, sæt `MINIMAX_MODEL_ID` til en model, du har adgang til (f.eks. `MiniMax-M2.7`).

Kodeeksempler, der bruger `OpenAIChatClient` (f.eks. Lektion 14 hotelbooking workflow), vil automatisk registrere og bruge din MiniMax konfiguration, når `MINIMAX_API_KEY` er angivet.

## Yderligere Opsætning til Lektion 8 (Bing Grounding Workflow)

Den betingede workflow-notebook i lektion 8 bruger **Bing grounding** via Azure AI Foundry. Hvis du planlægger at køre det eksempel, tilføj denne variabel til din `.env` fil:

| Variabel | Hvor findes den |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portalen → dit projekt → **Management** → **Connected resources** → din Bing-forbindelse → kopier forbindelses-ID’en |

## Fejlfinding

### SSL Certifikat Verifikationsfejl på macOS

Hvis du er på macOS og støder på en fejl som:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dette er et kendt problem med Python på macOS, hvor systemets SSL-certifikater ikke automatisk stoles på. Prøv følgende løsninger i rækkefølge:

**Mulighed 1: Kør Pythons Install Certificates script (anbefalet)**

```bash
# Erstat 3.XX med din installerede Python-version (f.eks. 3.12 eller 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Mulighed 2: Brug `connection_verify=False` i din notebook (kun for GitHub Models notebooks)**

I lektion 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) er en kommenteret workaround allerede inkluderet. Fjern kommentaren på `connection_verify=False`, når klienten oprettes:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktiver SSL-verifikation, hvis du støder på certifikatfejl
)
```

> **⚠️ Advarsel:** Deaktivering af SSL-verifikation (`connection_verify=False`) reducerer sikkerheden ved at omgå certificeringsvalidering. Brug dette kun som en midlertidig løsning i udviklingsmiljøer, aldrig i produktion.

**Mulighed 3: Installer og brug `truststore`**

```bash
pip install truststore
```

Tilføj derefter følgende øverst i din notebook eller script, før du foretager netværkskald:

```python
import truststore
truststore.inject_into_ssl()
```

## Sidder du fast?

Hvis du har problemer med at køre denne opsætning, så hop ind i vores <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">opret et issue</a>.
## Næste lektion

Du er nu klar til at køre koden til dette kursus. God fornøjelse med at lære mere om verdenen af AI-agenter!

[Introduktion til AI-agenter og agentbrugstilfælde](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->