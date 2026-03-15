# Kursoppsett

## Introduksjon

Denne leksjonen vil dekke hvordan du kjører kodeeksemplene i dette kurset.

## Bli med andre elever og få hjelp

Før du begynner å klone repoet ditt, bli med i [AI Agents For Beginners Discord-kanal](https://aka.ms/ai-agents/discord) for å få hjelp med oppsett, spørsmål om kurset eller for å koble deg til andre elever.

## Klon eller fork dette repoet

For å begynne, vennligst klon eller fork GitHub-repositoriet. Dette vil lage din egen versjon av kursmaterialet slik at du kan kjøre, teste og justere koden!

Dette kan gjøres ved å klikke på linken for å <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forke repoet</a>

Du bør nå ha din egen forket versjon av dette kurset på følgende link:

![Forked Repo](../../../translated_images/no/forked-repo.33f27ca1901baa6a.webp)

### Grunnleggende kloning (anbefalt for workshop / Codespaces)

  >Det fullstendige repositoriet kan være stort (~3 GB) når du laster ned full historikk og alle filer. Hvis du bare deltar på workshopen eller kun trenger noen få leksjonsmapper, unngår en grunnleggende kloning (eller en sparsom kloning) det meste av nedlastingen ved å kutte historikk og/eller hoppe over blobs.

#### Rask grunnleggende kloning — minimal historikk, alle filer

Erstatt `<your-username>` i kommandoene nedenfor med din fork-URL (eller upstream-URL hvis du foretrekker det).

For å klone bare siste commit-historikk (liten nedlasting):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

For å klone en spesifikk branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delvis (sparsom) kloning — minimale blobs + kun valgte mapper

Dette bruker delvis kloning og sparse-checkout (krever Git 2.25+ og anbefales med moderne Git med støtte for delvis kloning):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå inn i repo-mappen:

```bash|powershell
cd ai-agents-for-beginners
```

Deretter spesifiserer du hvilke mapper du vil ha (eksempel nedenfor viser to mapper):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Etter å ha klonet og verifisert filene, hvis du kun trenger filene og ønsker å frigjøre plass (ingen git-historikk), vennligst slett repository-metadataene (💀irreversibelt — du mister all Git-funksjonalitet: ingen commits, pulls, pushes eller historikktilgang).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Bruke GitHub Codespaces (anbefalt for å unngå lokale store nedlastinger)

- Opprett en ny Codespace for dette repositoriet via [GitHub UI](https://github.com/codespaces).  

- I terminalen til den nylig opprettede codespacen, kjør en av grunnleggende/sparse klone-kommandoene ovenfor for å hente kun leksjonsmappene du trenger inn i Codespace-arbeidsområdet.
- Valgfritt: etter kloning inne i Codespaces, fjern .git for å frigjøre ekstra plass (se fjerningskommandoer ovenfor).
- Merk: Hvis du foretrekker å åpne repoet direkte i Codespaces (uten ekstra kloning), vær klar over at Codespaces vil bygge devcontainer-miljøet og kan fortsatt provisjonere mer enn du trenger. Å klone en grunnleggende kopi inne i en fersk Codespace gir deg mer kontroll over diskbruk.

#### Tips

- Erstatt alltid clone-URL med din fork hvis du vil redigere/committe.
- Hvis du senere trenger mer historikk eller filer, kan du hente dem eller justere sparse-checkout for å inkludere flere mapper.

## Kjøre koden

Dette kurset tilbyr en serie med Jupyter Notebooks som du kan kjøre for å få praktisk erfaring med å bygge AI-agenter.

Kodeeksemplene bruker **Microsoft Agent Framework (MAF)** med `AzureAIProjectAgentProvider`, som kobler til **Azure AI Agent Service V2** (Responses API) via **Microsoft Foundry**.

Alle Python-notebookene er merket `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **MERK**: Hvis du ikke har Python3.12 installert, sørg for å installere det. Opprett deretter ditt venv ved å bruke python3.12 for å sikre at riktige versjoner installeres fra requirements.txt-filen.
  
    >Eksempel

    Opprett Python venv-katalog:

    ```bash|powershell
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

- .NET 10+: For eksempelkode som bruker .NET, sørg for å installere [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere. Sjekk deretter hvilken .NET SDK-versjon som er installert:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Påkrevd for autentisering. Installer fra [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-abonnement** — For tilgang til Microsoft Foundry og Azure AI Agent Service.
- **Microsoft Foundry-prosjekt** — Et prosjekt med en distribuert modell (f.eks. `gpt-4o`). Se [Trinn 1](../../../00-course-setup) nedenfor.

Vi har inkludert en `requirements.txt`-fil i roten av dette repositoriet som inneholder alle nødvendige Python-pakker for å kjøre kodeeksemplene.

Du kan installere dem ved å kjøre følgende kommando i terminalen i roten av repositoriet:

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler å opprette et Python virtuelt miljø for å unngå konflikter og problemer.

## Sett opp VSCode

Sørg for at du bruker riktig versjon av Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Sett opp Microsoft Foundry og Azure AI Agent Service

### Trinn 1: Opprett et Microsoft Foundry-prosjekt

Du trenger en Azure AI Foundry **hub** og et **prosjekt** med en distribuert modell for å kjøre notebookene.

1. Gå til [ai.azure.com](https://ai.azure.com) og logg inn med Azure-kontoen din.
2. Opprett en **hub** (eller bruk en eksisterende). Se: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inne i huben, opprett et **prosjekt**.
4. Deploy en modell (f.eks. `gpt-4o`) fra **Models + Endpoints** → **Deploy model**.

### Trinn 2: Hent prosjekt-endepunkt og navn på modellutplassering

Fra prosjektet ditt i Microsoft Foundry-portalen:

- **Prosjekt-endepunkt** — Gå til **Oversikt**-siden og kopier endepunkt-URLen.

![Project Connection String](../../../translated_images/no/project-endpoint.8cf04c9975bbfbf1.webp)

- **Navn på modellutplassering** — Gå til **Models + Endpoints**, velg modellen du har distribuert, og noter **Deployment name** (f.eks. `gpt-4o`).

### Trinn 3: Logg inn i Azure med `az login`

Alle notebookene bruker **`AzureCliCredential`** for autentisering — ingen API-nøkler å håndtere. Dette krever at du er logget inn via Azure CLI.

1. **Installer Azure CLI** hvis du ikke allerede har gjort det: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logg inn** ved å kjøre:

    ```bash|powershell
    az login
    ```

    Eller hvis du er i et eksternt/Codespace-miljø uten nettleser:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Velg abonnementet ditt** hvis du blir bedt om det — velg det som inneholder Foundry-prosjektet ditt.

4. **Sjekk** at du er logget inn:

    ```bash|powershell
    az account show
    ```

> **Hvorfor `az login`?** Notebookene autentiserer ved hjelp av `AzureCliCredential` fra `azure-identity`-pakken. Det betyr at Azure CLI-økten din gir legitimasjonen — ingen API-nøkler eller hemmeligheter i `.env`-filen din. Dette er en [beste praksis for sikkerhet](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Trinn 4: Opprett din `.env`-fil

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

| Variabel | Hvor du finner den |
|----------|--------------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portalen → prosjektet ditt → **Oversikt**-side |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portalen → **Models + Endpoints** → navnet på den distribuerte modellen |

Det er alt for de fleste leksjoner! Notebookene vil autentisere automatisk gjennom `az login`-økten din.

### Trinn 5: Installer Python-avhengigheter

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler å kjøre dette inne i det virtuelle miljøet du opprettet tidligere.

## Tillegg for oppsett for leksjon 5 (Agentic RAG)

Leksjon 5 bruker **Azure AI Search** for retrieval-augmented generation. Hvis du planlegger å kjøre den leksjonen, legg til disse variablene i `.env`-filen din:

| Variabel | Hvor du finner den |
|----------|--------------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portalen → din **Azure AI Search** ressurs → **Oversikt** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-portalen → din **Azure AI Search** ressurs → **Innstillinger** → **Nøkler** → primær admin-nøkkel |

## Tillegg for oppsett for leksjon 6 og 8 (GitHub modeller)

Noen notatbøker i leksjon 6 og 8 bruker **GitHub-modeller** i stedet for Azure AI Foundry. Hvis du planlegger å kjøre disse eksemplene, legg til disse variablene i `.env`-filen din:

| Variabel | Hvor du finner den |
|----------|--------------------|
| `GITHUB_TOKEN` | GitHub → **Innstillinger** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Bruk `https://models.inference.ai.azure.com` (standardverdi) |
| `GITHUB_MODEL_ID` | Navn på modell som skal brukes (f.eks. `gpt-4o-mini`) |

## Tillegg for oppsett for leksjon 8 (Bing Grounding Workflow)

Den betingede arbeidsflytnotatboken i leksjon 8 bruker **Bing grounding** via Azure AI Foundry. Hvis du planlegger å kjøre dette eksemplet, legg til denne variabelen i `.env`-filen din:

| Variabel | Hvor du finner den |
|----------|--------------------|
| `BING_CONNECTION_ID` | Azure AI Foundry-portalen → prosjektet ditt → **Management** → **Connected resources** → Bing-tilkoblingen din → kopier tilkoblings-IDen |

## Feilsøking

### SSL-sertifikatverifiseringsfeil på macOS

Hvis du er på macOS og får en feil som:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Dette er et kjent problem med Python på macOS hvor systemets SSL-sertifikater ikke automatisk stoles på. Prøv følgende løsninger i rekkefølge:

**Alternativ 1: Kjør Pythons Install Certificates-skript (anbefalt)**

```bash
# Erstatt 3.XX med din installerte Python-versjon (f.eks. 3.12 eller 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Alternativ 2: Bruk `connection_verify=False` i notatboken din (kun for GitHub Models-notebooks)**

I leksjon 6-notatboken (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) er en kommentert midlertidig løsning allerede inkludert. Fjern kommentaren på `connection_verify=False` når klienten opprettes:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Deaktiver SSL-verifisering hvis du opplever sertifikatfeil
)
```

> **⚠️ Advarsel:** Deaktivering av SSL-verifisering (`connection_verify=False`) reduserer sikkerheten ved å hoppe over sertifikatvalidering. Bruk dette kun som en midlertidig løsning i utviklingsmiljøer, aldri i produksjon.

**Alternativ 3: Installer og bruk `truststore`**

```bash
pip install truststore
```

Legg deretter til følgende øverst i notatboken eller skriptet ditt før du foretar nettverkskall:

```python
import truststore
truststore.inject_into_ssl()
```

## Stuck Somewhere?

Hvis du har problemer med å kjøre oppsettet, bli med i vår <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">opprett en issue</a>.

## Neste leksjon

Du er nå klar til å kjøre koden for dette kurset. Lykke til med å lære mer om verden av AI-agentene!

[Introduksjon til AI-agenter og agent brukstilfeller](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->