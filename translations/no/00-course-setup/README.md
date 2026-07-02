# Kursoppsett

## Introduksjon

Denne leksjonen vil dekke hvordan kjøre kodeeksemplene i dette kurset.

## Bli med andre elever og få hjelp

Før du begynner å klone din repo, bli med i [AI Agents For Beginners Discord-kanalen](https://aka.ms/ai-agents/discord) for å få hjelp med oppsett, spørsmål om kurset eller for å koble deg til andre elever.

## Klon eller Fork dette Repository

For å begynne, vennligst klon eller fork GitHub-repositoriet. Dette vil lage din egen versjon av kursmaterialet slik at du kan kjøre, teste og justere koden!

Dette kan gjøres ved å klikke på linken for å <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forke repoet</a>

Du skal nå ha din egen forked versjon av dette kurset under følgende link:

![Forked Repo](../../../translated_images/no/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (anbefalt for workshop / Codespaces)

  >Det fullstendige repositoriet kan være stort (~3 GB) når du laster ned full historikk og alle filer. Hvis du bare deltar på workshopen eller kun trenger noen leksjonsmapper, unngår en shallow clone (eller sparse clone) mesteparten av nedlastingen ved å forkorte historikk og/eller hoppe over blobs.

#### Rask shallow clone — minimal historikk, alle filer

Erstatt `<your-username>` i kommandoene under med URL-en til din fork (eller upstream-URL hvis du foretrekker det).

For å klone kun siste commit-historikk (lite nedlasting):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

For å klone en spesifikk branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delvis (sparsom) clone — minimale blobs + kun valgte mapper

Dette bruker partial clone og sparse-checkout (krever Git 2.25+ og anbefales med moderne Git med partial clone-støtte):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå inn i repo-mappen:

```bash|powershell
cd ai-agents-for-beginners
```

Angi så hvilke mapper du ønsker (eksempelet viser to mapper):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Etter kloning og verifisering av filer, hvis du kun trenger filene og ønsker å frigjøre plass (ingen git-historikk), slett repository-metadata (💀irreversibelt — du mister all Git-funksjonalitet: ingen commits, pulls, pushes eller tilgang til historikk).

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

- I terminalen til den nyskapte codespacen, kjør en av shallow/sparse clone-kommandoene over for kun å hente leksjonsmapper du trenger til Codespace-arbeidsområdet.
- Valgfritt: etter kloning i Codespaces, fjern .git for å frigjøre ekstra plass (se fjerningskommandoene over).
- Merk: Om du foretrekker å åpne repoet direkte i Codespaces (uten ekstra kloning), vær oppmerksom på at Codespaces vil bygge devcontainer-miljøet og kan fortsatt provisionere mer enn du trenger. Å klone en shallow kopi inne i en ny Codespace gir mer kontroll over diskbruk.

#### Tips

- Erstatt alltid clone-URL med din fork hvis du vil redigere/committe.
- Hvis du senere trenger mer historikk eller filer, kan du hente dem eller justere sparse-checkout for å inkludere flere mapper.

## Kjøre Koden

Dette kurset tilbyr en serie av Jupyter Notebook-er du kan kjøre for å få praktisk erfaring med å bygge AI-agenter.

Kodeeksemplene bruker **Microsoft Agent Framework (MAF)** med `AzureAIProjectAgentProvider`, som kobler til **Azure AI Agent Service V2** (Responses API) gjennom **Microsoft Foundry**.

Alle Python-notebooks er merket `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **MERK**: Hvis du ikke har Python3.12 installert, sørg for å installere det. Opprett deretter ditt virtuelle miljø med python3.12 for å sikre at riktige versjoner installeres fra requirements.txt-filen.
  
    >Eksempel

    Lag Python venv-mappe:

    ```bash|powershell
    python -m venv venv
    ```

    Aktiver så venv miljø for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: For eksempel-kode som bruker .NET, sørg for å installere [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere. Sjekk deretter hvilken .NET SDK-versjon du har installert:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Kreves for autentisering. Installer fra [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-abonnement** — For tilgang til Microsoft Foundry og Azure AI Agent Service.
- **Microsoft Foundry-prosjekt** — Et prosjekt med en deployert modell (f.eks. `gpt-4o`). Se [Steg 1](#steg-1-opprett-et-microsoft-foundry-prosjekt) nedenfor.

Vi har inkludert en `requirements.txt`-fil i roten av dette repositoriet som inneholder alle nødvendige Python-pakker for å kjøre kodeeksemplene.

Du kan installere dem ved å kjøre følgende kommando i terminalen i repo-rotmappen:

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler å opprette et Python virtuelt miljø for å unngå konflikter og problemer.

## Sett opp VSCode

Sørg for at du bruker riktig versjon av Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Sett opp Microsoft Foundry og Azure AI Agent Service

### Steg 1: Opprett et Microsoft Foundry-prosjekt

Du trenger en Azure AI Foundry **hub** og **prosjekt** med en deployert modell for å kjøre notebookene.

1. Gå til [ai.azure.com](https://ai.azure.com) og logg på med din Azure-konto.
2. Lag en **hub** (eller bruk en eksisterende). Se: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inne i huben, opprett et **prosjekt**.
4. Deploy en modell (f.eks. `gpt-4o`) under **Models + Endpoints** → **Deploy model**.

### Steg 2: Hent din prosjekt-endepunkt og modell-deployment navn

Fra prosjektet ditt i Microsoft Foundry-portalen:

- **Project Endpoint** — Gå til **Oversikt**-siden og kopier endepunkt-URL-en.

![Project Connection String](../../../translated_images/no/project-endpoint.8cf04c9975bbfbf1.webp)

- **Model Deployment Name** — Gå til **Models + Endpoints**, velg din deployerte modell, og noter **Deployment name** (f.eks. `gpt-4o`).

### Steg 3: Logg inn på Azure med `az login`

Alle notebooks bruker **`AzureCliCredential`** for autentisering — ingen API-nøkler å håndtere. Dette krever at du er innlogget via Azure CLI.

1. **Installer Azure CLI** hvis du ikke har gjort det: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logg inn** ved å kjøre:

    ```bash|powershell
    az login
    ```

    Eller om du er i et remote/Codespace-miljø uten nettleser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Velg abonnement** hvis du blir spurt — velg det som inneholder Foundry-prosjektet ditt.

4. **Bekreft** at du er innlogget:

    ```bash|powershell
    az account show
    ```

> **Hvorfor `az login`?** Notebookene autentiserer via `AzureCliCredential` fra `azure-identity`-pakken. Det betyr at din Azure CLI-økt gir legitimasjonen — ingen API-nøkler eller hemmeligheter i `.env`-filen. Dette er en [sikkerhetsbest practice](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Steg 4: Lag din `.env`-fil

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
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variabel | Hvor finne den |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portalen → ditt prosjekt → **Oversikt**-side |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portalen → **Models + Endpoints** → navnet på din deployerte modell |

Det er alt for de fleste leksjoner! Notebookene autentiserer automatisk via din `az login` økt.

### Steg 5: Installer Python-avhengigheter

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler å kjøre dette i det virtuelle miljøet du opprettet tidligere.

## Ekstra oppsett for Lekse 5 (Agentic RAG)

Leksjon 5 bruker **Azure AI Search** for retrieval-augmented generation. Hvis du planlegger å kjøre denne leksjonen, legg til disse variablene i din `.env`-fil:

| Variabel | Hvor finne den |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portalen → din **Azure AI Search**-ressurs → **Oversikt** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-portalen → din **Azure AI Search**-ressurs → **Innstillinger** → **Nøkler** → primær administratornøkkel |

## Ekstra oppsett for Lekse 6 og Lekse 8 (GitHub-modeller)

Noen notebooker i leksjon 6 og 8 bruker **GitHub Models** i stedet for Azure AI Foundry. Hvis du planlegger å kjøre disse eksemplene, legg til disse variablene i din `.env`-fil:

| Variabel | Hvor finne den |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Innstillinger** → **Utviklerinnstillinger** → **Personlige tilgangsnøkler** |
| `GITHUB_ENDPOINT` | Bruk `https://models.inference.ai.azure.com` (standardverdi) |
| `GITHUB_MODEL_ID` | Modellnavn som skal brukes (f.eks. `gpt-4o-mini`) |

## Alternativ leverandør: MiniMax (OpenAI-kompatibel)

[MiniMax](https://platform.minimaxi.com/) tilbyr store kontekstmodeller (opptil 204K tokens) gjennom et OpenAI-kompatibelt API. Siden Microsoft Agent Frameworks `OpenAIChatClient` fungerer med enhver OpenAI-kompatibel endpoint, kan du bruke MiniMax som en drop-in erstatning for GitHub Models eller OpenAI.

Legg til disse variablene i din `.env`-fil:

| Variabel | Hvor finne den |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API-nøkler |
| `MINIMAX_BASE_URL` | Bruk `https://api.minimax.io/v1` (standardverdi) |
| `MINIMAX_MODEL_ID` | Modellnavn som skal brukes (f.eks. `MiniMax-M3`) |

**Eksempelmodeller**: `MiniMax-M3` (anbefalt), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (raskere responser). Modellnavn og tilgjengelighet kan endres over tid, og tilgang til en gitt modell kan avhenge av din konto eller region — sjekk [MiniMax Platform](https://platform.minimaxi.com/) for gjeldende liste. Hvis `MiniMax-M3` ikke er tilgjengelig for din konto, sett `MINIMAX_MODEL_ID` til en modell du har tilgang til (f.eks. `MiniMax-M2.7`).

Kodeeksemplene som bruker `OpenAIChatClient` (f.eks. Lekse 14 hotellbooking-workflow) vil automatisk oppdage og bruke MiniMax-konfigurasjonen din når `MINIMAX_API_KEY` er satt.

## Ekstra oppsett for Lekse 8 (Bing Grounding Workflow)

Den betingede workflow-notebook i leksjon 8 bruker **Bing grounding** via Azure AI Foundry. Hvis du planlegger å kjøre dette eksempelet, legg til denne variabelen i din `.env`-fil:

| Variabel | Hvor finne den |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry-portalen → ditt prosjekt → **Management** → **Connected resources** → din Bing-tilkobling → kopier tilkoblings-ID |

## Feilsøking

### SSL-sertifikatverifiseringsfeil på macOS

Hvis du er på macOS og får en feil som:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dette er et kjent problem med Python på macOS hvor systemets SSL-sertifikater ikke automatisk stoles på. Prøv følgende løsninger i denne rekkefølgen:

**Alternativ 1: Kjør Python sin Install Certificates script (anbefalt)**

```bash
# Erstatt 3.XX med din installerte Python-versjon (f.eks. 3.12 eller 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Alternativ 2: Bruk `connection_verify=False` i notebooken (kun for GitHub Models notebooks)**

I Lekse 6 notebook (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`), er det allerede inkludert en kommentert workaround. Fjern kommentaren på `connection_verify=False` ved oppretting av klienten:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktiver SSL-verifisering hvis du får sertifikatfeil
)
```

> **⚠️ Advarsel:** Å deaktivere SSL-verifisering (`connection_verify=False`) reduserer sikkerheten ved å hoppe over sertifikatvalidering. Bruk dette kun som en midlertidig løsning i utviklingsmiljø, aldri i produksjon.

**Alternativ 3: Installer og bruk `truststore`**

```bash
pip install truststore
```

Legg så til følgende øverst i notebooken eller skriptet før noen nettverkskall:

```python
import truststore
truststore.inject_into_ssl()
```

## Fast et sted?

Hvis du har problemer med å kjøre oppsettet, bli med i vår <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">opprett en issue</a>.
## Neste leksjon

Du er nå klar til å kjøre koden for dette kurset. Lykke til med å lære mer om verdenen av AI-agenter! 

[Introduksjon til AI-agenter og bruksområder for agenter](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->