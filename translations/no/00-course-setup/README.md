# Kursoppsett

## Introduksjon

Denne leksjonen vil dekke hvordan du kjører kodeeksemplene i denne kurset.

## Bli med andre elever og få hjelp

Før du begynner å klone repoet ditt, bli med i [AI Agents For Beginners Discord-kanalen](https://aka.ms/ai-agents/discord) for å få hjelp med oppsett, spørsmål om kurset, eller for å knytte kontakt med andre elever.

## Klon eller Fork dette repoet

For å starte, vennligst klon eller fork GitHub-repositoriet. Dette lager din egen versjon av kursmaterialet slik at du kan kjøre, teste og justere koden!

Dette kan du gjøre ved å klikke på linken for å <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forke repoet</a>

Du skal nå ha din egen forkede versjon av dette kurset på følgende lenke:

![Forked Repo](../../../translated_images/no/forked-repo.33f27ca1901baa6a.webp)

### Grunnleggende kloning (anbefalt for workshop / Codespaces)

  >Det fullstendige repositoriet kan være stort (~3 GB) hvis du laster ned full historikk og alle filer. Hvis du kun deltar på workshopen eller bare trenger noen få leksjonsmapper, unngår en grunnleggende kloning (shallow clone) eller sparsommelig kloning (sparse clone) mesteparten av nedlastingen ved å avkorte historikk og/eller ekskludere blobs.

#### Rask grunnleggende kloning — minimal historikk, alle filer

Erstatt `<your-username>` i kommandoene under med URL-en til din fork (eller upstream URL hvis du foretrekker det).

For å klone kun den siste commit-historikken (liten nedlasting):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

For å klone en spesifikk branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delvis (sparsom) kloning — minimal blobs + kun valgte mapper

Dette bruker delvis kloning og sparse-checkout (krever Git 2.25+ og anbefalt moderne Git med støtte for delvis kloning):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå inn i repo-mappen:

```bash|powershell
cd ai-agents-for-beginners
```

Deretter spesifiser hvilke mapper du ønsker (eksempel nedenfor viser to mapper):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Etter kloning og verifisering av filene, hvis du kun trenger filene og vil frigjøre plass (ingen git-historikk), vennligst slett repository-metakdata (💀irreversibelt — du mister all Git-funksjonalitet: ingen commits, pulls, pushes eller historikktilgang).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Bruke GitHub Codespaces (anbefalt for å unngå store lokale nedlastinger)

- Opprett et nytt Codespace for dette repoet via [GitHub UI](https://github.com/codespaces).  

- I terminalen til det nylig opprettede codespacet, kjør en av de grunnleggende/sparsomme klonekommandoene over for å hente kun leksjonsmappene du trenger inn i Codespace arbeidsområdet.
- Valgfritt: etter kloning inne i Codespaces, fjern .git for å frigjøre ekstra plass (se fjernkommandoer over).
- Merk: Hvis du foretrekker å åpne repoet direkte i Codespaces (uten ekstra kloning), vær klar over at Codespaces vil bygge devcontainer-miljøet og kan fortsatt provisjonere mer enn du trenger. Kloning av en grunnleggende kopi inne i et ferskt Codespace gir deg mer kontroll over diskbruk.

#### Tips

- Bytt alltid ut klone-URL med din fork hvis du ønsker å redigere/committe.
- Hvis du senere trenger mer historikk eller filer, kan du hente dem eller justere sparse-checkout for å inkludere flere mapper.

## Kjøre koden

Dette kurset tilbyr en serie Jupyter Notebooks som du kan kjøre for å få praktisk erfaring med å bygge AI-agenter.

Kodeeksemplene bruker **Microsoft Agent Framework (MAF)** med `FoundryChatClient`, som kobler til **Microsoft Foundry Agent Service V2** (Responses API) gjennom **Microsoft Foundry**.

Alle Python notebooks er merket `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **MERK**: Hvis du ikke har Python3.12 installert, sørg for å installere det. Opprett deretter ditt virtualenv med python3.12 for å sikre at riktige versjoner installeres fra requirements.txt-filen.
  
    >Eksempel

    Opprett Python virtualenv-mappe:

    ```bash|powershell
    python -m venv venv
    ```

    Aktiver deretter virtualenv for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: For eksempel kodene som bruker .NET, sørg for å installere [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere. Sjekk deretter den installerte .NET SDK-versjonen:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Påkrevd for autentisering. Installer fra [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-abonnement** — For tilgang til Microsoft Foundry og Microsoft Foundry Agent Service.
- **Microsoft Foundry-prosjekt** — Et prosjekt med en distribuert modell (f.eks. `gpt-5-mini`). Se [Trinn 1](#trinn-1-opprett-et-microsoft-foundry-prosjekt) nedenfor.

Vi har inkludert en `requirements.txt`-fil i roten av dette repositoriet som inneholder alle nødvendige Python-pakker for å kjøre kodeeksemplene.

Du kan installere dem ved å kjøre følgende kommando i terminalen på roten av repositoriet:

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler å opprette et Python virtuelt miljø for å unngå konflikter og problemer.

## Sett opp VSCode

Sørg for at du bruker riktig versjon av Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Sett opp Microsoft Foundry og Microsoft Foundry Agent Service

### Trinn 1: Opprett et Microsoft Foundry-prosjekt

Du trenger en Microsoft Foundry **hub** og **prosjekt** med en distribuert modell for å kjøre notebookene.

1. Gå til [ai.azure.com](https://ai.azure.com) og logg inn med din Azure-konto.
2. Opprett en **hub** (eller bruk en eksisterende). Se: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inne i huben, opprett et **prosjekt**.
4. Distribuer en modell (f.eks. `gpt-5-mini`) fra **Models + Endpoints** → **Deploy model**.

### Trinn 2: Hent prosjekt-endenpunkt og navn på modellutrulling

Fra prosjektet ditt i Microsoft Foundry-portalen:

- **Project Endpoint** — Gå til **Overview** siden og kopier endepunkt-URL.

![Project Connection String](../../../translated_images/no/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Gå til **Models + Endpoints**, velg den distribuerte modellen din, og noter **Deployment name** (f.eks. `gpt-5-mini`).

### Trinn 3: Logg inn i Azure med `az login`

Alle notebookene bruker **`AzureCliCredential`** for autentisering — ingen API-nøkler å håndtere. Dette krever at du er logget inn via Azure CLI.

1. **Installer Azure CLI** hvis du ikke allerede har det: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logg inn** ved å kjøre:

    ```bash|powershell
    az login
    ```

    Eller hvis du er i et eksternt/Codespace-miljø uten nettleser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Velg abonnementet ditt** hvis du blir spurt — velg det som inneholder Foundry-prosjektet ditt.

4. **Bekreft** at du er logget inn:

    ```bash|powershell
    az account show
    ```

> **Hvorfor `az login`?** Notebookene autentiserer med `AzureCliCredential` fra `azure-identity`-pakken. Det betyr at din Azure CLI-økt gir legitimasjon — ingen API-nøkler eller hemmeligheter i `.env`-filen din. Dette er en [sikkerhetsbest practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Trinn 4: Opprett din `.env` fil

Kopier eksempel-filen:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Åpne `.env` og fyll inn disse to verdiene:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variabel | Hvor finne den |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portalen → prosjektet ditt → **Overview** side |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portalen → **Models + Endpoints** → navnet på din distribuerte modell |

Det er det for de fleste leksjoner! Notebookene autentiserer automatisk via din `az login` økt.

### Trinn 5: Installer Python-avhengigheter

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler å kjøre dette inne i det virtuelle miljøet du opprettet tidligere.

## Ekstra oppsett for leksjon 5 (Agentic RAG)

Leksjon 5 bruker **Azure AI Search** for retrieval-augmented generation. Hvis du planlegger å kjøre denne leksjonen, legg til disse variablene i `.env`-filen din:

| Variabel | Hvor finne den |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portalen → din **Azure AI Search** ressurs → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-portalen → din **Azure AI Search** ressurs → **Settings** → **Keys** → primær admin-nøkkel |

## Ekstra oppsett for leksjoner som kaller Azure OpenAI direkte (Leksjoner 6 og 8)

Noen notebooks i leksjon 6 og 8 kaller **Azure OpenAI** direkte (bruker **Responses API**) i stedet for å gå gjennom et Microsoft Foundry-prosjekt. Disse eksemplene brukte tidligere GitHub Models, som er utdatert (utfases juli 2026) og støtter ikke Responses API. Hvis du planlegger å kjøre disse eksemplene, legg til disse variablene i `.env`-filen din:

| Variabel | Hvor finne den |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure-portalen → din **Azure OpenAI** ressurs → **Keys and Endpoint** → Endepunkt (f.eks. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Navnet på din distribuerte modell (f.eks. `gpt-5-mini`) som støtter Responses API |
| `AZURE_OPENAI_API_KEY` | Valgfritt — kun hvis du bruker nøkkelbasert autentisering i stedet for `az login` / Entra ID |

> Responses API bruker det stabile `/openai/v1/` endepunktet, så ingen `api-version` kreves. Logg inn med `az login` for å bruke nøkkelfri Entra ID-autentisering.

## Alternativ leverandør: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) tilbyr store-kontekst modeller (opptil 204K tokens) gjennom en OpenAI-kompatibel API. Siden Microsoft Agent Frameworks `OpenAIChatClient` fungerer med hvilket som helst OpenAI-kompatibelt endepunkt, kan du bruke MiniMax som en drop-in erstatning for Azure OpenAI eller OpenAI.

Legg til disse variablene i `.env`-filen din:

| Variabel | Hvor finne den |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API Keys |
| `MINIMAX_BASE_URL` | Bruk `https://api.minimax.io/v1` (standardverdi) |
| `MINIMAX_MODEL_ID` | Modellnavn du vil bruke (f.eks. `MiniMax-M3`) |

**Eksempelhvor**: `MiniMax-M3` (anbefalt), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (raskere responser). Modellnavn og tilgjengelighet kan endres over tid, og tilgang til en gitt modell kan avhenge av din konto eller region — sjekk [MiniMax Platform](https://platform.minimaxi.com/) for oppdatert liste. Hvis `MiniMax-M3` ikke er tilgjengelig for din konto, sett `MINIMAX_MODEL_ID` til en modell du har tilgang til (f.eks. `MiniMax-M2.7`).

Kodeeksemplene som bruker `OpenAIChatClient` (f.eks. Leksjon 14 hotellreservasjonsflyt) vil automatisk oppdage og bruke din MiniMax-konfigurasjon når `MINIMAX_API_KEY` er satt.

## Alternativ leverandør: Foundry Local (kjør modeller på enheten)

[Foundry Local](https://foundrylocal.ai) er en lettvekts runtime som laster ned, administrerer og betjener språkmodeller **fullstendig på din egen maskin** gjennom en OpenAI-kompatibel API — ingen skytjeneste, ingen Azure-abonnement, og ingen API-nøkler. Det er et flott alternativ for offline utvikling, eksperimentering uten sky-kostnader, eller å holde data på enheten.

Siden Microsoft Agent Frameworks `OpenAIChatClient` fungerer med hvilket som helst OpenAI-kompatibelt endepunkt, er Foundry Local en lokal drop-in erstatning for Azure OpenAI.

**1. Installer Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Last ned og kjør en modell** (dette starter også lokal tjeneste):

```bash
foundry model list          # se tilgjengelige modeller
foundry model run phi-4-mini
```

**3. Installer Python SDK** som brukes for å oppdage lokalt endepunkt:

```bash
pip install foundry-local-sdk
```

**4. Peker Microsoft Agent Framework til din lokale modell:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Laster ned (hvis nødvendig) og kjører modellen lokalt, deretter oppdager endepunkt/port.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # f.eks. http://localhost:<port>/v1
    api_key=manager.api_key,        # alltid "ikke-påkrevd" for Foundry Local
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Merk:** Foundry Local eksponerer et OpenAI-kompatibelt **Chat Completions** endepunkt. Bruk det for lokal utvikling og offline-scenarier. For full **Responses API** funksjonalitet (stateful samtaler, dyp verktøyorkestrering og agent-stil utvikling), målrett mot **Azure OpenAI** eller et **Microsoft Foundry** prosjekt som vist i leksjonene. Se [Foundry Local dokumentasjon](https://foundrylocal.ai) for gjeldende modellkatalog og plattformstøtte.

## Ekstra oppsett for leksjon 8 (Bing Grounding Workflow)


Den betingede arbeidsflytnotisboken i leksjon 8 bruker **Bing-grunnlag** via Microsoft Foundry. Hvis du planlegger å kjøre det eksemplet, legg til denne variabelen i din `.env`-fil:

| Variabel | Hvor du finner den |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry-portalen → prosjektet ditt → **Management** → **Connected resources** → din Bing-tilkobling → kopier tilkoblings-ID |

## Feilsøking

### SSL-sertifikatverifiseringsfeil på macOS

Hvis du bruker macOS og får en feil som:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dette er et kjent problem med Python på macOS hvor systemets SSL-sertifikater ikke automatisk blir tillatt. Prøv følgende løsninger i denne rekkefølgen:

**Alternativ 1: Kjør Pythons Install Certificates-script (anbefalt)**

```bash
# Erstatt 3.XX med din installerte Python-versjon (f.eks., 3.12 eller 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Alternativ 2: Bruk `connection_verify=False` i notisboken din (kun for GitHub Models-notisbøker)**

I notisboken fra Leksjon 6 (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), er en kommentert omgåelse allerede inkludert. Fjern kommentaren på `connection_verify=False` når du oppretter klienten:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktiver SSL-verifisering hvis du støter på sertifikatfeil
)
```

> **⚠️ Advarsel:** Å deaktivere SSL-verifisering (`connection_verify=False`) reduserer sikkerheten ved å hoppe over sertifikatvalidering. Bruk dette bare som en midlertidig løsning i utviklingsmiljøer, aldri i produksjon.

**Alternativ 3: Installer og bruk `truststore`**

```bash
pip install truststore
```

Deretter legger du til følgende øverst i notisboken eller skriptet ditt før du gjør noen nettverkskall:

```python
import truststore
truststore.inject_into_ssl()
```

## Stuck et sted?

Hvis du har problemer med å kjøre oppsettet, ta turen innom vår <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">opprett en issue</a>.

## Neste leksjon

Du er nå klar til å kjøre koden for dette kurset. Lykke til med å lære mer om verdenen til AI-agenter!

[Introduksjon til AI-agenter og brukstilfeller for agenter](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->