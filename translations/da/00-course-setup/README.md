# Kursusopsætning

## Introduktion

Denne lektion forklarer, hvordan du kører kodeeksemplerne i dette kursus.

## Deltag med andre kursister og få hjælp

Før du begynder at klone dit repo, deltag i [AI Agents For Beginners Discord channel](https://aka.ms/ai-agents/discord) for at få hjælp til opsætning, stille spørgsmål om kurset eller forbindes med andre kursister.

## Klon eller fork dette repo

For at begynde, klon eller fork venligst GitHub-repositoriet. Dette laver din egen version af kursusmaterialet, så du kan køre, teste og justere koden!

Dette kan gøres ved at klikke på linket til <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">oprette en fork af repoet</a>

Du bør nu have din egen forkede version af dette kursus på følgende link:

![Forket repo](../../../translated_images/da/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (anbefales til workshop / Codespaces)

  >Det fulde repository kan være stort (~3 GB), når du downloader fuld historik og alle filer. Hvis du kun deltager i workshoppen eller kun har brug for et par lektionsmapper, undgår en shallow clone (eller en sparse clone) det meste af den download ved at trunkere historik og/eller springe blobs over.

#### Hurtig shallow clone — minimal historik, alle filer

Erstat `<your-username>` i nedenstående kommandoer med din fork-URL (eller upstream-URL'en, hvis du foretrækker det).

To clone only the latest commit history (small download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

To clone a specific branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partial (sparse) clone — minimale blobs + kun valgte mapper

Dette bruger partial clone og sparse-checkout (kræver Git 2.25+ og anbefales med moderne Git med partial clone-understøttelse):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Traverse into the repo folder:

```bash|powershell
cd ai-agents-for-beginners
```

Then specify which folders you want (example below shows two folders):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

After cloning and verifying the files, if you only need files and want to free space (no git history), please delete the repository metadata (💀irreversible — you will lose all Git functionality: no commits, pulls, pushes, or history access).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Using GitHub Codespaces (recommended to avoid local large downloads)

- Opret en ny Codespace for dette repo via [GitHub UI](https://github.com/codespaces).  

- I terminalen i den nyskabte codespace, kør en af shallow/sparse clone-kommandoerne ovenfor for kun at bringe de lektionsmapper, du har brug for, ind i Codespace-arbejdsområdet.
- Valgfrit: efter cloning inde i Codespaces, fjern .git for at frigive ekstra plads (se fjern-kommandoerne ovenfor).
- Bemærk: Hvis du foretrækker at åbne repoet direkte i Codespaces (uden en ekstra clone), så vær opmærksom på, at Codespaces vil konstruere devcontainer-miljøet og muligvis stadig provisionere mere end du behøver. At clone en shallow kopi inde i en frisk Codespace giver dig mere kontrol over diskforbruget.

#### Tips

- Erstat altid clone-URL'en med din fork, hvis du vil redigere/committe.
- Hvis du senere har brug for mere historik eller filer, kan du hente dem eller justere sparse-checkout for at inkludere yderligere mapper.

## Kør koden

Dette kursus tilbyder en række Jupyter-notebooks, som du kan køre for at få praktisk erfaring med at bygge AI-agenter.

Kodeeksemplerne bruger **Microsoft Agent Framework (MAF)** med `AzureAIProjectAgentProvider`, som forbinder til **Azure AI Agent Service V2** (Responses API) via **Microsoft Foundry**.

Alle Python-notebooks er mærket `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **BEMÆRK**: Hvis du ikke har Python3.12 installeret, sørg for at installere det.  Opret derefter dit venv ved at bruge python3.12 for at sikre, at de korrekte versioner installeres fra requirements.txt-filen.
  
    >Eksempel

    Create Python venv directory:

    ```bash|powershell
    python -m venv venv
    ```

    Then activate venv environment for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: For eksempelkoderne, der bruger .NET, sørg for at installere [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller senere. Tjek derefter din installerede .NET SDK-version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Krævet for autentificering. Installer fra [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — For adgang til Microsoft Foundry og Azure AI Agent Service.
- **Microsoft Foundry Project** — Et projekt med en deployet model (f.eks. `gpt-4o`). Se [Trin 1](../../../00-course-setup) nedenfor.

Vi har inkluderet en `requirements.txt`-fil i roden af dette repository, som indeholder alle nødvendige Python-pakker for at køre kodeeksemplerne.

Du kan installere dem ved at køre følgende kommando i din terminal i rodmappen af repositoryet:

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler at oprette et Python-virtualmiljø for at undgå konflikter og problemer.

## Opsæt VSCode

Sørg for, at du bruger den rigtige version af Python i VSCode.

![billede](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Opsæt Microsoft Foundry og Azure AI Agent Service

### Trin 1: Opret et Microsoft Foundry-projekt

Du har brug for et Azure AI Foundry **hub** og **projekt** med en deployet model for at kunne køre notebooks.

1. Gå til [ai.azure.com](https://ai.azure.com) og log ind med din Azure-konto.
2. Opret et **hub** (eller brug et eksisterende). Se: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inde i hubben, opret et **projekt**.
4. Deploy en model (f.eks. `gpt-4o`) fra **Models + Endpoints** → **Deploy model**.

### Trin 2: Hent dit projekt-endpoint og navnet på modeldeployeringen

Fra dit projekt i Microsoft Foundry-portalen:

- **Project Endpoint** — Gå til **Oversigt**-siden og kopier endpoint-URL'en.

![Projektforbindelsesstreng](../../../translated_images/da/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Gå til **Models + Endpoints**, vælg din deployede model, og noter **Deployment name** (f.eks. `gpt-4o`).

### Trin 3: Log ind på Azure med `az login`

Alle notebooks bruger **`AzureCliCredential`** til autentificering — ingen API-nøgler at administrere. Dette kræver, at du er logget ind via Azure CLI.

1. **Installer Azure CLI** hvis du ikke allerede har gjort det: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Log ind** ved at køre:

    ```bash|powershell
    az login
    ```

    Eller hvis du er i et remote/Codespace-miljø uden en browser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Vælg dit abonnement** hvis du bliver bedt om det — vælg det, der indeholder dit Foundry-projekt.

4. **Bekræft**, at du er logget ind:

    ```bash|powershell
    az account show
    ```

> **Hvorfor `az login`?** Notebooks autentificerer ved hjælp af `AzureCliCredential` fra `azure-identity`-pakken. Det betyder, at din Azure CLI-session leverer legitimationsoplysningerne — ingen API-nøgler eller hemmeligheder i din `.env`-fil. Dette er en [sikkerhedsbedste praksis](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Trin 4: Opret din `.env`-fil

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variabel | Hvor du finder det |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portal → dit projekt → **Oversigt**-siden |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portal → **Models + Endpoints** → navnet på din deployede model |

Det var det for de fleste lektioner! Notebooks vil autentificere automatisk gennem din `az login`-session.

### Trin 5: Installer Python-afhængigheder

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler at køre dette inde i det virtualmiljø, du oprettede tidligere.

## Yderligere opsætning for Lektion 5 (Agentic RAG)

Lektion 5 bruger **Azure AI Search** til retrieval-augmented generation. Hvis du planlægger at køre den lektion, tilføj disse variabler til din `.env`-fil:

| Variabel | Hvor du finder det |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portalen → din **Azure AI Search**-ressource → **Oversigt** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-portalen → din **Azure AI Search**-ressource → **Indstillinger** → **Nøgler** → primær administratornøgle |

## Yderligere opsætning for Lektion 6 og Lektion 8 (GitHub Models)

Nogle notebooks i lektion 6 og 8 bruger **GitHub Models** i stedet for Azure AI Foundry. Hvis du planlægger at køre disse eksempler, tilføj disse variabler til din `.env`-fil:

| Variabel | Hvor du finder det |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Brug `https://models.inference.ai.azure.com` (standardværdi) |
| `GITHUB_MODEL_ID` | Modelnavn som skal bruges (f.eks. `gpt-4o-mini`) |

## Yderligere opsætning for Lektion 8 (Bing Grounding Workflow)

Den betingede workflow-notebook i lektion 8 bruger **Bing grounding** via Azure AI Foundry. Hvis du planlægger at køre det eksempel, tilføj denne variabel til din `.env`-fil:

| Variabel | Hvor du finder det |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry-portalen → dit projekt → **Management** → **Connected resources** → din Bing-forbindelse → kopier connection ID |

## Fejlfinding

### SSL-certifikatverificeringsfejl på macOS

Hvis du er på macOS og støder på en fejl som:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dette er et kendt problem med Python på macOS, hvor systemets SSL-certifikater ikke automatisk bliver betroet. Prøv følgende løsninger i rækkefølge:

**Mulighed 1: Kør Pythons Install Certificates-script (anbefalet)**

```bash
# Udskift 3.XX med din installerede Python-version (f.eks. 3.12 eller 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Mulighed 2: Brug `connection_verify=False` i din notebook (kun for GitHub Models-notebooks)**

I Lesson 6-notebooken (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) er en kommenteret workaround allerede inkluderet. Fjern kommentaren på `connection_verify=False`, når du opretter klienten:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktiver SSL-verifikation, hvis du støder på certifikatfejl
)
```

> **⚠️ Advarsel:** Deaktivering af SSL-verificering (`connection_verify=False`) reducerer sikkerheden ved at springe certifikatvalidering over. Brug dette kun som en midlertidig workaround i udviklingsmiljøer, aldrig i produktion.

**Mulighed 3: Installer og brug `truststore`**

```bash
pip install truststore
```

Tilføj derefter følgende øverst i din notebook eller script, før du foretager netværkskald:

```python
import truststore
truststore.inject_into_ssl()
```

## Står du fast et sted?

Hvis du har problemer med at køre denne opsætning, hop ind i vores <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">opret en issue</a>.

## Næste lektion

Du er nu klar til at køre koden i dette kursus. God fornøjelse med at lære mere om verdenen af AI-agenter! 

[Introduktion til AI-agenter og anvendelsestilfælde](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfraskrivelse:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten Co-op Translator (https://github.com/Azure/co-op-translator). Selvom vi stræber efter nøjagtighed, bedes du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales en professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, som måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->