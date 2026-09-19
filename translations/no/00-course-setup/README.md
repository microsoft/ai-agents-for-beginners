# Kursoppsett

## Introduksjon

Denne leksjonen vil dekke hvordan du kjører kodeeksemplene i dette kurset.

## Bli med andre elever og få hjelp

Før du begynner å klone ditt repo, bli med i [AI Agents For Beginners Discord-kanal](https://aka.ms/ai-agents/discord) for å få hjelp med oppsett, spørsmål om kurset, eller for å komme i kontakt med andre elever.

## Klon eller Forgren dette repositioriet

For å begynne, vennligst klon eller forgrenen GitHub-repositoriet. Dette vil lage din egen versjon av kursmaterialet slik at du kan kjøre, teste og justere koden!

Dette kan gjøres ved å klikke på linken for å <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forgrene repoet</a>

Du bør nå ha din egen forgrenede versjon av dette kurset på følgende link:

![Forked Repo](../../../translated_images/no/forked-repo.33f27ca1901baa6a.webp)

### Grunnleggende kloning (anbefalt for workshop / Codespaces)

  >Hele repositoriet kan være stort (~3 GB) når du laster ned full historikk og alle filer. Hvis du bare deltar på workshopen eller bare trenger noen få leksjonsmapper, laster en grunnleggende kloning (eller en sparsommelig kloning) ned mye mindre.

#### Rask grunnleggende kloning — minimal historikk, alle filer

Erstatt `<your-username>` i kommandoene nedenfor med din forgrenede URL (eller opprinnelig URL hvis du foretrekker).

For å klone bare siste forpliktelsehistorikk (liten nedlasting):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

For å klone en spesifikk gren:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delvis (sparsommelig) kloning — minimale blobs + bare valgte mapper

Dette bruker delvis kloning og sparsommelig utsjekking (krever Git 2.25+ og anbefalt moderne Git med delvis kloning støtte):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå inn i repo-mappen:

```bash
cd ai-agents-for-beginners
```

Så spesifiser hvilke mapper du vil ha (eksempelet under viser to mapper):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Etter kloning og verifisering av filene, hvis du bare trenger filene og vil frigjøre plass (ingen git-historikk), slett repository metadata (💀irreversibelt — du mister all Git-funksjonalitet):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Bruke GitHub Codespaces (anbefalt for å unngå store nedlastinger lokalt)

- Opprett en ny Codespace for dette repo via [GitHub UI](https://github.com/codespaces).  

- I terminalen i den nylig opprettede codespacen, kjør en av de grunnleggende/sparsomme klonekommandoene over for å bare hente leksjonsmappene du trenger inn i Codespace arbeidsområdet.
- Valgfritt: etter kloning inne i Codespaces, fjern .git for å frigjøre ekstra plass (se fjerning kommandoer over).
- Merk: Hvis du foretrekker å åpne repoet direkte i Codespaces (uten ekstra kloning), vær oppmerksom på at Codespaces vil bygge utviklingsmiljøet og kan fortsatt opprette mer enn du trenger.

#### Tips

- Bytt alltid ut klone-URL med din forgrening hvis du vil redigere/utføre commit.
- Hvis du senere trenger mer historikk eller filer, kan du hente dem eller justere sparse-checkout for å inkludere flere mapper.

## Kjøre koden

Dette kurset tilbyr en serie med Jupyter Notebooks som du kan kjøre for å få praktisk erfaring med bygging av AI-agenter.

Kodeeksemplene bruker **Microsoft Agent Framework (MAF)** med `FoundryChatClient`, som kobler til **Microsoft Foundry Agent Service V2** (Responses API) gjennom **Microsoft Foundry**.

Alle Python-notebooks er merket `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **MERK**: Hvis du ikke har Python3.12 installert, sørg for å installere det. Lag deretter ditt virtuelle miljø med python3.12 for å sikre at riktige versjoner installeres fra requirements.txt-filen.
  
    >Eksempel

    Lag Python venv-katalog:

    ```bash
    python -m venv venv
    ```

    Aktiver deretter venv-miljø for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: For eksempel koder som bruker .NET, sørg for å installere [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere. Sjekk deretter din installerte .NET SDK-versjon:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Kreves for autentisering. Installer fra [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-abonnement** — For tilgang til Microsoft Foundry og Microsoft Foundry Agent Service.
- **Microsoft Foundry-prosjekt** — Et prosjekt med en distribuert modell (f.eks. `gpt-5-mini`). Se [Steg 1](#steg-1-opprett-et-microsoft-foundry-prosjekt) nedenfor.

Vi har inkludert en `requirements.txt`-fil i roten av dette repository som inneholder alle nødvendige Python-pakker for å kjøre kodeeksemplene.

Du kan installere dem ved å kjøre følgende kommando i terminalen i roten av repository:

```bash
pip install -r requirements.txt
```

Vi anbefaler å opprette et Python virtuelt miljø for å unngå konflikter og problemer.

## Sett opp VSCode

Sørg for at du bruker riktig versjon av Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Sett opp Microsoft Foundry og Microsoft Foundry Agent Service

### Steg 1: Opprett et Microsoft Foundry-prosjekt

Du trenger et Microsoft Foundry **hub** og **prosjekt** med en distribuert modell for å kjøre notebookene.

1. Gå til [ai.azure.com](https://ai.azure.com) og logg inn med din Azure-konto.
2. Opprett en **hub** (eller bruk en eksisterende). Se: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inne i huben, opprett et **prosjekt**.
4. Distribuer en modell (f.eks. `gpt-5-mini`) fra **Models + Endpoints** → **Deploy model**.

### Steg 2: Hent prosjekt-endepunkt og modell-distribusjonsnavn

Fra ditt prosjekt i Microsoft Foundry-portalen:

- **Project Endpoint** — Gå til **Overview**-siden og kopier endepunkt-URLen.

![Project Connection String](../../../translated_images/no/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Gå til **Models + Endpoints**, velg din distribuerte modell, og noter **Deployment name** (f.eks. `gpt-5-mini`).

### Steg 3: Logg inn i Azure med `az login`

De fleste notebookene autentiserer via din **Azure CLI sign-in** — ved å bruke `AzureCliCredential` eller `DefaultAzureCredential` (begge bruker din `az login`-økt) fra `azure-identity`-pakken — så de trenger ikke API-nøkler. Noen få leksjoner og valgfrie integrasjoner bruker API-nøkler; sjekk hver leksjons forutsetninger for eventuelle ekstra miljøvariabler. Dette krever at du er logget inn via Azure CLI.

1. **Installer Azure CLI** hvis du ikke allerede har gjort det: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logg inn** ved å kjøre:

    ```bash
    az login
    ```

    Eller hvis du er i et fjern-/Codespace-miljø uten nettleser:

    ```bash
    az login --use-device-code
    ```

3. **Velg abonnementet ditt** hvis du blir bedt om det — velg det som inneholder Foundry-prosjektet ditt.

4. **Bekreft** at du er logget inn:

    ```bash
    az account show
    ```

> **Hvorfor `az login`?** Notebookene autentiserer ved hjelp av `AzureCliCredential` (eller `DefaultAzureCredential`, som også bruker din Azure CLI login) fra `azure-identity`-pakken. Det betyr at din Azure CLI-økt gir legitimajsonen — ingen API-nøkler eller hemmeligheter i `.env`-filen. Dette er en [sikkerhetsbeste praksis](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Steg 4: Opprett din `.env`-fil

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

| Variabel | Hvor du finner den |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portalen → ditt prosjekt → **Overview**-side |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portalen → **Models + Endpoints** → navnet på din distribuerte modell |

Det er alt for de fleste leksjoner! Notebookene vil autentisere automatisk gjennom din `az login`-økt.

### Steg 5: Installer Python-avhengigheter

```bash
pip install -r requirements.txt
```

Vi anbefaler å kjøre dette inne i det virtuelle miljøet du opprettet tidligere.

## Valgfritt oppsett: Azure AI Search (Leksjon 5 og 16)

Leksjon 5 (Agentic RAG) og Leksjon 16 notebookene kjører ut av boksen med en **intern kunnskapsbase** — ingen ekstra Azure-ressurser nødvendig. Hvis du vil støtte dem med en virkelig **Azure AI Search** indeks, merk at **Leksjon 16 notebook for øyeblikket bruker nøkkelbasert autentisering**: den bytter fra intern søk til Azure AI Search bare når **både** `AZURE_SEARCH_SERVICE_ENDPOINT` **og** `AZURE_SEARCH_API_KEY` er satt, og ellers forblir på intern søk — så for å kjøre mot en ekte indeks må du også sette admin-nøkkelen. Nøkkelfri autentisering med Microsoft Entra ID (RBAC) er anbefalt tilnærming for din egne produksjonskode, i samsvar med `az login`-flyten som brukes overalt ellers i kurset.

RBAC-steget nedenfor gjelder for oppsett-guide-eksemplene og din egen kode. De aktiverer ikke nøkkelfri autentisering i Leksjon 16 notebook; Leksjon 16 krever fortsatt både endepunkt og admin-nøkkel for å bruke Azure AI Search.

1. **Aktiver rollebasert tilgang** på din søketjeneste:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Tildel nødvendige roller til deg selv** (opprett/laste indekser og spørring):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Legg til endepunktet** i din `.env`-fil:

| Variabel | Hvor du finner den |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portalen → din **Azure AI Search** ressurs → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Krevd (med endepunkt) for å aktivere Azure AI Search i Leksjon 16 notebook, som bruker nøkkelbasert autentisering. Azure portal → **Settings** → **Keys** → primær admin-nøkkel |

> **Hvorfor uten nøkler?** Admin-nøkler gir full skrive-tilgang til søketjenesten din og kan lekke via `.env`-filer. Med RBAC brukes din `az login` identitet i stedet — samme nøkkelfrie Entra ID-mønster som kursnotebookene bruker (via `AzureCliCredential` / `DefaultAzureCredential`). Se [Koble til Azure AI Search med roller](https://learn.microsoft.com/azure/search/search-security-rbac).

Se [Azure AI Search oppsettsguide](./AzureSearch.md) for fullstendige indeks-opprettelseseksempler i Python og .NET.

## Tilleggsoppsett for leksjoner som kaller Azure OpenAI direkte (Leksjon 6 og 8)

Noen notebooker i leksjon 6 og 8 kaller **Azure OpenAI** direkte (ved bruk av **Responses API**) i stedet for gjennom et Microsoft Foundry-prosjekt. Disse eksemplene brukte tidligere GitHub Models, som er utdatert og støtter ikke Responses API. Legg til disse variablene i din `.env`-fil:

| Variabel | Hvor du finner den |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure-portalen → din **Azure OpenAI** ressurs → **Keys and Endpoint** → Endepunkt (f.eks. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Navnet på din distribuerte modell (f.eks. `gpt-5-mini`) som støtter Responses API |
| `AZURE_OPENAI_API_KEY` | Valgfritt — bare hvis du bruker nøkkelbasert autentisering i stedet for `az login` / Entra ID |

> Responses API bruker det stabile `/openai/v1/` endepunktet, så ingen `api-version` kreves. Logg inn med `az login` for å bruke nøkkelfri Entra ID-autentisering.

## Alternativ leverandør: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) tilbyr store-kontekstmodeller (opptil 204K tokens) gjennom en OpenAI-kompatibel API. Siden Microsoft Agent Frameworks `OpenAIChatClient` fungerer med alle OpenAI-kompatible endepunkter, kan du bruke MiniMax som et direkte alternativ for leksjoner som bruker `OpenAIChatClient`.

Legg til disse variablene i din `.env`-fil:

| Variabel | Hvor du finner den |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API-nøkler |
| `MINIMAX_BASE_URL` | Bruk `https://api.minimax.io/v1` (standardverdi) |
| `MINIMAX_MODEL_ID` | Modellnavn å bruke (f.eks., `MiniMax-M3`) |

**Eksempelmodeller**: `MiniMax-M3` (anbefalt), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (raskere svar). Modellnavn og tilgjengelighet kan endre seg over tid, og tilgang til en gitt modell kan avhenge av din konto.

Kodeeksemplene som bruker `OpenAIChatClient` (f.eks. Leksjon 14 hotellbookingflyt) vil automatisk oppdage og bruke din MiniMax-konfigurasjon når `MINIMAX_API_KEY` er satt.


## Alternativ leverandør: Novita AI (OpenAI-kompatibel)

[Novita AI](https://novita.ai/llm-api) tilbyr en OpenAI-kompatibel API for open source og nyeste LLM-er (DeepSeek, Llama, Qwen, og flere). Siden Microsoft Agent Frameworks `OpenAIChatClient` fungerer med alle OpenAI-kompatible endepunkter, kan du bruke Novita AI som et direkte alternativ til Azure OpenAI eller OpenAI.

Legg til disse variablene i din `.env`-fil:

| Variabel | Hvor du finner den |
|----------|--------------------|
| `NOVITA_API_KEY` | [Novita AI Dashboard](https://novita.ai/settings/key-management) → API Keys |
| `NOVITA_BASE_URL` | Bruk `https://api.novita.ai/openai/v1` (standardverdi) |
| `NOVITA_MODEL_ID` | Modellnavn som skal brukes (f.eks. `moonshotai/kimi-k3`) |

**Eksempemodeller**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. Novita AI hoster også mange andre open source modellfamilier (Llama, Qwen, GLM, og flere) — sjekk [Novita AI modellbibliotek](https://novita.ai/llm-api) for gjeldende liste over tilgjengelige modeller og deres modell-ID-er.

De nåværende eksemplene bruker ikke automatisk `NOVITA_*`-variablene. For å bruke Novita AI, må du eksplisitt sende disse verdiene når du konstruerer `OpenAIChatClient` i eksempelet du kjører.

## Alternativ leverandør: Foundry Local (Kjør modeller på enheten)

[Foundry Local](https://foundrylocal.ai) er en lettvekts runtime som laster ned, administrerer og betjener språkmodeller **fullstendig på din egen maskin** gjennom en OpenAI-kompatibel API — ingen sky kreves.

Siden Microsoft Agent Frameworks `OpenAIChatClient` fungerer med alle OpenAI-kompatible endepunkter, er Foundry Local et lokalt alternativ til Azure OpenAI.

**1. Installer Foundry Local**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Last ned og kjør en modell** (dette starter også den lokale tjenesten):

```bash
foundry model list          # se tilgjengelige modeller
foundry model run phi-4-mini
```

**3. Installer Python SDK-en** som brukes for å oppdage det lokale endepunktet:

```bash
pip install foundry-local-sdk
```

**4. Pek Microsoft Agent Framework til din lokale modell:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Laster ned (om nødvendig) og betjener modellen lokalt, deretter oppdager endepunkt/port.
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

> **Merk:** Foundry Local eksponerer et OpenAI-kompatibelt **Chat Completions**-endepunkt. Bruk det til lokal utvikling og offline-scenarier. For full funksjonalitet i **Responses API** (tilstandsbevarende samtaler, osv.), bruk Azure OpenAI eller et Microsoft Foundry-prosjekt.

## Tilleggsoppsett for Lekse 8 (Bing Grounding Workflow)

Den betingede arbeidsflytnotatboken i lekse 8 bruker **Bing grounding** via Microsoft Foundry. Hvis du planlegger å kjøre dette eksempelet, legg til denne variabelen i `.env`-filen din:

| Variabel | Hvor du finner den |
|----------|--------------------|
| `BING_CONNECTION_ID` | Microsoft Foundry-portalen → ditt prosjekt → **Management** → **Connected resources** → din Bing-tilkobling → kopier tilkoblings-ID |

## Feilsøking

### SSL-sertifikatverifiseringsfeil på macOS

Hvis du er på macOS og støter på en feil som:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dette er et kjent problem med Python på macOS hvor systemets SSL-sertifikater ikke automatisk blir anerkjent som trygge. Prøv følgende løsninger i rekkefølge:

**Alternativ 1: Kjør Pythons Install Certificates-skript (anbefalt)**

```bash
# Erstatt 3.XX med din installerte Python-versjon (f.eks., 3.12 eller 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Alternativ 2: Bruk `connection_verify=False` i notatboken din (kun for GitHub Models notatbøker)**

I Lekse 6-notatboken (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) er en kommentert løsning allerede inkludert. Fjern kommentaren fra `connection_verify=False` når du møter sertifikatfeil:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktiver SSL-verifisering hvis du støter på sertifikatfeil
)
```

> **⚠️ Advarsel:** Å deaktivere SSL-verifisering (`connection_verify=False`) reduserer sikkerheten ved å hoppe over sertifikatvalidering. Bruk dette kun som en midlertidig løsning i utviklingsmiljøer. Bruk det aldri i produksjon.

**Alternativ 3: Installer og bruk `truststore`**

```bash
pip install truststore
```

Legg deretter til følgende øverst i notatboken eller skriptet ditt før du gjør noen nettverkskall:

```python
import truststore
truststore.inject_into_ssl()
```

## Sitter du fast et sted?

Hvis du har problemer med å kjøre dette oppsettet, bli med i vår <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">opprett en sak</a>.

## Neste leksjon

Du er nå klar til å kjøre koden for dette kurset. Lykke til med å lære mer om verden av AI-agenter!

[Introduksjon til AI-agenter og bruksområder for agenter](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->