# Kursoppsett

## Introduksjon

Denne leksjonen vil dekke hvordan du kan kjøre kodeeksemplene i denne kursen.

## Bli med andre elever og få hjelp

Før du begynner å klone repoet ditt, bli med i [AI Agents For Beginners Discord-kanalen](https://aka.ms/ai-agents/discord) for å få hjelp med oppsett, spørsmål om kurset, eller for å knytte forbindelser med andre elever.

## Klon eller Fork dette repoet

For å begynne, vennligst klon eller fork GitHub-repositoriet. Dette lager din egen versjon av kursmaterialet slik at du kan kjøre, teste og justere koden!

Dette kan gjøres ved å klikke på linken for å <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forke repoet</a>

Du bør nå ha din egen forket versjon av dette kurset på følgende lenke:

![Forked Repo](../../../translated_images/no/forked-repo.33f27ca1901baa6a.webp)

### Grunnleggende kloning (anbefalt for workshop / Codespaces)

  >Det fullstendige repositoriet kan være stort (~3 GB) når du laster ned full historikk og alle filer. Hvis du bare deltar på workshop eller bare trenger noen få leksjonsmapper, laster en grunnleggende kloning (eller en sparsommelig kloning) ned mye mindre.

#### Rask grunnleggende kloning — minimal historikk, alle filer

Erstatt `<your-username>` i kommandoene nedenfor med din fork-URL (eller den oppstrøms URLen hvis du foretrekker det).

For å kun klone siste commit historikk (liten nedlasting):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

For å klone en spesifikk gren:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delvis (sparsommelig) kloning — minimale blobs + kun utvalgte mapper

Dette bruker delvis kloning og sparse-checkout (krever Git 2.25+ og anbefalt moderne Git med støtte for delvis kloning):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå inn i repomappen:

```bash
cd ai-agents-for-beginners
```

Spesifiser deretter hvilke mapper du vil ha (eksempel under viser to mapper):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Etter kloning og verifisering av filene, hvis du bare trenger filene og vil frigjøre plass (ingen git-historikk), vennligst slett repositoriets metadata (💀irreversibelt — du vil miste all Git-funksjonalitet):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Bruke GitHub Codespaces (anbefalt for å unngå store lokale nedlastinger)

- Opprett en ny Codespace for dette repoet via [GitHub UI](https://github.com/codespaces).  

- I terminalen i den nylig opprettede Codespace, kjør en av de grunnleggende eller sparsommelig klonings-kommandoene ovenfor for å hente kun de leksjonsmappene du trenger inn i Codespace-arbeidsområdet.
- Valgfritt: etter kloning inne i Codespaces, fjern .git for å gjenvinne ekstra plass (se fjerningskommandoer ovenfor).
- Merk: Hvis du foretrekker å åpne repoet direkte i Codespaces (uten ekstra kloning), vær klar over at Codespaces vil konstruere devcontainer-miljøet og kan fortsatt provisjonere mer enn du trenger.

#### Tips

- Erstatt alltid klone-URLen med din fork hvis du ønsker å redigere/committe.
- Hvis du senere trenger mer historikk eller flere filer, kan du hente dem eller justere sparse-checkout til å inkludere flere mapper.

## Kjøre Koden

Dette kurset tilbyr en serie med Jupyter Notebooks som du kan kjøre for å få praktisk erfaring med å bygge AI-agenter.

Kodeeksemplene bruker **Microsoft Agent Framework (MAF)** med `FoundryChatClient`, som kobler til **Microsoft Foundry Agent Service V2** (Responses API) gjennom **Microsoft Foundry**.

Alle Python-notebookene er merket `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **MERK**: Hvis du ikke har Python3.12 installert, sørg for å installere det. Opprett deretter ditt virtuelle miljø (venv) med python3.12 for å sikre at riktige versjoner blir installert fra requirements.txt-filen.
  
    >Eksempel

    Opprett Python venv-mappe:

    ```bash
    python -m venv venv
    ```

    Aktiver deretter venv-miljøet for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: For kodeeksemplene som bruker .NET, sørg for at du har installert [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere. Sjekk deretter hvilken versjon av .NET SDK som er installert:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Kreves for autentisering. Installer fra [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-abonnement** — For tilgang til Microsoft Foundry og Microsoft Foundry Agent Service.
- **Microsoft Foundry-prosjekt** — Et prosjekt med en utplassert modell (f.eks. `gpt-5-mini`). Se [Steg 1](#steg-1-opprett-et-microsoft-foundry-prosjekt) nedenfor.

Vi har inkludert en `requirements.txt`-fil i roten av dette repositoriet som inneholder alle nødvendige Python-pakker for å kjøre kodeeksemplene.

Du kan installere dem ved å kjøre følgende kommando i terminalen i repoets rot:

```bash
pip install -r requirements.txt
```

Vi anbefaler å opprette et Python virtuelt miljø for å unngå konflikter og problemer.

## Sett opp VSCode

Sørg for at du bruker riktig versjon av Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Sett Opp Microsoft Foundry og Microsoft Foundry Agent Service

### Steg 1: Opprett et Microsoft Foundry Prosjekt

Du trenger et Microsoft Foundry **hub** og **prosjekt** med en utplassert modell for å kjøre notatbøkene.

1. Gå til [ai.azure.com](https://ai.azure.com) og logg inn med din Azure-konto.
2. Opprett en **hub** (eller bruk en eksisterende). Se: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inne i huben, opprett et **prosjekt**.
4. Utplasser en modell (f.eks. `gpt-5-mini`) fra **Models + Endpoints** → **Deploy model**.

### Steg 2: Hent prosjekt-endepunktet og modellutplasseringsnavnet

Fra prosjektet ditt i Microsoft Foundry-portalen:

- **Project Endpoint** — Gå til **Oversikts**siden og kopier endepunkt-URLen.

![Project Connection String](../../../translated_images/no/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Gå til **Models + Endpoints**, velg din deployerte modell, og noter **Deployment name** (f.eks. `gpt-5-mini`).

### Steg 3: Logg inn på Azure med `az login`

De fleste notatbøker autentiserer gjennom din **Azure CLI pålogging** — med `AzureCliCredential` eller `DefaultAzureCredential` (begge benytter din `az login`-sesjon) fra `azure-identity`-pakken — så de krever ikke API-nøkler. Noen få leksjoner og valgfrie integrasjoner bruker API-nøkler; sjekk forutsetningene i hver leksjon for eventuelle ekstra miljøvariabler. Dette krever at du er logget inn via Azure CLI.

1. **Installer Azure CLI** hvis du ikke allerede har den: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logg inn** ved å kjøre:

    ```bash
    az login
    ```

    Eller hvis du er i et fjern-/Codespace-miljø uten nettleser:

    ```bash
    az login --use-device-code
    ```

3. **Velg abonnementet ditt** hvis du blir spurt — velg det som inneholder Foundry-prosjektet ditt.

4. **Verifiser** at du er pålogget:

    ```bash
    az account show
    ```

> **Hvorfor `az login`?** Notatbøkene autentiserer med `AzureCliCredential` (eller `DefaultAzureCredential`, som også benytter Azure CLI-påloggingen) fra `azure-identity`-pakken. Dette betyr at Azure CLI-sesjonen din gir legitimasjonen — ingen API-nøkler eller hemmeligheter i `.env`-filen. Dette er en [sikkerhetsanbefaling](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

Åpne `.env` og fyll ut disse to verdiene:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Variabel | Hvor du finner den |
|----------|------------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portalen → ditt prosjekt → **Oversikt**-side |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portalen → **Models + Endpoints** → navnet på din deployerte modell |

Det er alt for de fleste leksjoner! Notatbøkene autentiserer automatisk gjennom din `az login`-sesjon.

### Steg 5: Installer Python-avhengigheter

```bash
pip install -r requirements.txt
```

Vi anbefaler å kjøre dette inne i det virtuelle miljøet du laget tidligere.

## Valgfritt oppsett: Azure AI Search (Leksjoner 5 og 16)

Leksjon 5 (Agentic RAG) og Leksjon 16-notatbøkene kjører ut av boksen med en **minnebasert kunnskapsbase** — ingen ekstra Azure-ressurser trengs. Hvis du ønsker å støtte dem med en ekte **Azure AI Search** indeks, merk at **Leksjon 16-notatboken for øyeblikket bruker nøkkelbasert autentisering**: den bytter fra minnesøk til Azure AI Search kun når **både** `AZURE_SEARCH_SERVICE_ENDPOINT` **og** `AZURE_SEARCH_API_KEY` er satt, ellers bruker den minnesøk — for å kjøre mot en ekte indeks må du sette admin-nøkkelen også. Nøkkelfri autentisering med Microsoft Entra ID (RBAC) er den anbefalte metoden for din egen produksjonskode, i samsvar med `az login`-flyten som brukes ellers i kurset.

Stegene for RBAC nedenfor gjelder for oppsett-eksemplene og din egen kode. De aktiverer ikke nøkkelfri autentisering i Leksjon 16-notatboken; Leksjon 16 krever fortsatt både endepunkt og admin-nøkkel for å bruke Azure AI Search.

1. **Aktiver rollebasert tilgang** på søketjenesten din:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Tildel deg selv de nødvendige rollene** (opprette/laste indekser og spørre):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Legg til endepunktet** i `.env`-filen din:

| Variabel | Hvor du finner den |
|----------|------------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portalen → din **Azure AI Search**-ressurs → **Oversikt** → URL |
| `AZURE_SEARCH_API_KEY` | Påkrevd (sammen med endepunkt) for å aktivere Azure AI Search i Leksjon 16-notatboken, som bruker nøkkelbasert autentisering. Azure-portalen → **Innstillinger** → **Nøkler** → primær administrator-nøkkel |

> **Hvorfor nøkkelfri?** Admin-nøkler gir full skrivetilgang til søketjenesten og kan lekke via `.env`-filer. Med RBAC brukes i stedet identiteten fra `az login` — samme nøkkelfrie Entra ID-mønster som kursnotatbøkene bruker (via `AzureCliCredential` / `DefaultAzureCredential`). Se [Koble til Azure AI Search med roller](https://learn.microsoft.com/azure/search/search-security-rbac).

Se [Azure AI Search oppsettsveiledning](./AzureSearch.md) for komplette eksempler på indeksopprettelse i Python og .NET.

## Ekstra oppsett for leksjoner som kaller Azure OpenAI direkte (Leksjoner 6 og 8)

Noen notatbøker i leksjon 6 og 8 kaller **Azure OpenAI** direkte (bruker **Responses API**) i stedet for via et Microsoft Foundry-prosjekt. Disse eksemplene brukte tidligere GitHub Models, som er avviklet og støtter ikke Responses API. Legg til disse variablene i `.env`-filen din:

| Variabel | Hvor du finner den |
|----------|------------------|
| `AZURE_OPENAI_ENDPOINT` | Azure-portalen → din **Azure OpenAI**-ressurs → **Nøkler og Endepunkt** → Endepunkt (f.eks. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Navn på din deployerte modell (f.eks. `gpt-5-mini`) som støtter Responses API |
| `AZURE_OPENAI_API_KEY` | Valgfritt — kun hvis du bruker nøkkelbasert autentisering i stedet for `az login` / Entra ID |

> Responses API bruker det stabile `/openai/v1/` endepunktet, så ingen `api-version` er nødvendig. Logg inn med `az login` for nøkkelfri Entra ID-autentisering.

## Alternativ leverandør: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) tilbyr modeller med stor kontekst (opptil 204K tokens) gjennom en OpenAI-kompatibel API. Siden Microsoft Agent Frameworks `OpenAIChatClient` fungerer med hvilken som helst OpenAI-kompatibel endepeunt, kan du bruke MiniMax som et drop-in-alternativ for leksjoner som bruker `OpenAIChatClient`.

Legg til disse variablene i `.env`-filen din:

| Variabel | Hvor du finner den |
|----------|------------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API-nøkler |
| `MINIMAX_BASE_URL` | Bruk `https://api.minimax.io/v1` (standardverdi) |
| `MINIMAX_MODEL_ID` | Modellnavn som skal brukes (f.eks. `MiniMax-M3`) |

**Eksempelmodeller**: `MiniMax-M3` (anbefalt), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (raskere responser). Modellnavn og tilgjengelighet kan endres over tid, og tilgang til en gitt modell kan avhenge av kontoen din.

Kodeeksemplene som bruker `OpenAIChatClient` (f.eks. Lekjson 14 hotellbestillingsflyt) vil automatisk oppdage og bruke MiniMax-konfigurasjonen din når `MINIMAX_API_KEY` er satt.


## Alternativ leverandør: Foundry Local (Kjør modeller på enheten)

[Foundry Local](https://foundrylocal.ai) er en lettvekts runtime som laster ned, administrerer og betjener språkmodeller **helt på din egen maskin** gjennom en OpenAI-kompatibel API — ingen sky kreves.

Fordi Microsoft Agent Frameworks `OpenAIChatClient` fungerer med hvilken som helst OpenAI-kompatibel endepunkt, er Foundry Local et enkelt lokalt alternativ til Azure OpenAI.

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

**4. Pek Microsoft Agent Framework mot din lokale modell:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Laster ned (om nødvendig) og kjører modellen lokalt, deretter oppdager endepunkt/port.
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

> **Merk:** Foundry Local eksponerer en OpenAI-kompatibel **Chat Completions**-endepunkt. Bruk det for lokal utvikling og frakoblede scenarier. For hele funksjonssettet i **Responses API** (tilstandsholdige samtaler osv.), bruk Azure OpenAI eller et Microsoft Foundry-prosjekt.

## Ytterligere oppsett for leksjon 8 (Bing Grounding Workflow)

Den betingede arbeidsflytnotisboken i leksjon 8 bruker **Bing grounding** via Microsoft Foundry. Hvis du planlegger å kjøre det eksempelet, legg til denne variabelen i din `.env`-fil:

| Variabel | Hvor du finner den |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry-portalen → ditt prosjekt → **Management** → **Connected resources** → din Bing-tilkobling → kopier tilkoblings-ID |

## Feilsøking

### Feil med SSL-sertifikatverifisering på macOS

Hvis du er på macOS og møter en feil som:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dette er et kjent problem med Python på macOS hvor systemets SSL-sertifikater ikke automatisk anses som pålitelige. Prøv følgende løsninger i rekkefølge:

**Alternativ 1: Kjør Pythons Install Certificates-skript (anbefalt)**

```bash
# Erstatt 3.XX med din installerte Python-versjon (f.eks. 3.12 eller 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Alternativ 2: Bruk `connection_verify=False` i notisboken din (kun for GitHub Models-notiser)**

I leksjon 6-notisboken (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) er en utkommentert løsning allerede inkludert. Fjern kommentaren på `connection_verify=False` når du får sertifikatfeil:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktiver SSL-verifisering hvis du støter på sertifikatfeil
)
```

> **⚠️ Advarsel:** Deaktivering av SSL-verifisering (`connection_verify=False`) reduserer sikkerheten ved å hoppe over sertifikatvalidering. Bruk dette kun som en midlertidig løsning i utviklingsmiljøer. Aldri i produksjon.

**Alternativ 3: Installer og bruk `truststore`**

```bash
pip install truststore
```

Legg så til følgende øverst i notisboken eller skriptet ditt før du gjør nettverksanrop:

```python
import truststore
truststore.inject_into_ssl()
```

## Sitter du fast et sted?

Hvis du har problemer med å kjøre dette oppsettet, bli med i vår <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">opprett et problem</a>.

## Neste leksjon

Du er nå klar til å kjøre koden for dette kurset. Lykke til med å lære mer om verden av AI-agenter! 

[Introduksjon til AI-agenter og bruksområder](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->