<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86273689a010b5efecaf7fa23104e0fb",
  "translation_date": "2025-11-07T08:39:38+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "no"
}
-->
# Kursoppsett

## Introduksjon

Denne leksjonen vil dekke hvordan du kjører kodeeksemplene i dette kurset.

## Bli med andre lærere og få hjelp

Før du begynner å klone ditt repo, bli med i [AI Agents For Beginners Discord-kanalen](https://aka.ms/ai-agents/discord) for å få hjelp med oppsett, stille spørsmål om kurset, eller for å koble deg med andre lærere.

## Klon eller fork dette repoet

For å komme i gang, vennligst klon eller fork GitHub-repositoriet. Dette vil lage din egen versjon av kursmaterialet slik at du kan kjøre, teste og tilpasse koden!

Dette kan gjøres ved å klikke på lenken for å <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forke repoet</a>

Du bør nå ha din egen forkede versjon av dette kurset på følgende lenke:

![Forket Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.no.png)

### Grunnleggende kloning (anbefalt for workshop / Codespaces)

  >Det fulle repositoriet kan være stort (~3 GB) når du laster ned hele historikken og alle filer. Hvis du kun deltar på workshop eller bare trenger noen få leksjonsmapper, unngår en grunnleggende kloning (eller en sparsom kloning) mesteparten av den nedlastingen ved å kutte historikken og/eller hoppe over blobs.

#### Rask grunnleggende kloning — minimal historikk, alle filer

Erstatt `<your-username>` i kommandoene nedenfor med din fork-URL (eller upstream-URL hvis du foretrekker det).

For å klone kun den nyeste commit-historikken (liten nedlasting):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

For å klone en spesifikk gren:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delvis (sparsom) kloning — minimal blobs + kun utvalgte mapper

Dette bruker delvis kloning og sparsom utsjekking (krever Git 2.25+ og anbefalt moderne Git med støtte for delvis kloning):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå inn i repo-mappen:

```bash|powershell
cd ai-agents-for-beginners
```

Deretter spesifiser hvilke mapper du ønsker (eksempelet nedenfor viser to mapper):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Etter kloning og verifisering av filene, hvis du kun trenger filene og vil frigjøre plass (ingen git-historikk), vennligst slett repositoriets metadata (💀irreversibelt — du vil miste all Git-funksjonalitet: ingen commits, pulls, pushes eller tilgang til historikk).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Bruke GitHub Codespaces (anbefalt for å unngå lokale store nedlastinger)

- Opprett en ny Codespace for dette repoet via [GitHub UI](https://github.com/codespaces).  

- I terminalen til den nyopprettede Codespace, kjør en av de grunnleggende/sparsomme klonekommandoene ovenfor for å hente kun de leksjonsmappene du trenger inn i Codespace-arbeidsområdet.
- Valgfritt: etter kloning inne i Codespaces, fjern .git for å frigjøre ekstra plass (se fjerningskommandoer ovenfor).
- Merk: Hvis du foretrekker å åpne repoet direkte i Codespaces (uten en ekstra kloning), vær oppmerksom på at Codespaces vil konstruere devcontainer-miljøet og kan fortsatt tilrettelegge mer enn du trenger. Å klone en grunnleggende kopi inne i en ny Codespace gir deg mer kontroll over diskbruk.

#### Tips

- Erstatt alltid klone-URL-en med din fork hvis du ønsker å redigere/committe.
- Hvis du senere trenger mer historikk eller filer, kan du hente dem eller justere sparsom utsjekking for å inkludere flere mapper.

## Kjøre koden

Dette kurset tilbyr en serie Jupyter Notebooks som du kan kjøre for å få praktisk erfaring med å bygge AI-agenter.

Kodeeksemplene bruker enten:

**Krever GitHub-konto - Gratis**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Merket som (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Merket som (autogen.ipynb)

**Krever Azure-abonnement**:
3) Azure AI Foundry + Azure AI Agent Service. Merket som (azureaiagent.ipynb)

Vi oppfordrer deg til å prøve alle tre typer eksempler for å se hvilken som fungerer best for deg.

Uansett hvilket alternativ du velger, vil det avgjøre hvilke oppsettsteg du må følge nedenfor:

## Krav

- Python 3.12+
  - **MERK**: Hvis du ikke har Python3.12 installert, sørg for å installere det. Deretter opprett din venv ved hjelp av python3.12 for å sikre at riktige versjoner installeres fra requirements.txt-filen.
  
    >Eksempel

    Opprett Python venv-katalog:

    ```bash|powershell
    python -m venv venv
    ```

    Deretter aktiver venv-miljøet for:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: For eksempelene som bruker .NET, sørg for å installere [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller nyere. Deretter, sjekk din installerte .NET SDK-versjon:

    ```bash|powershell
    dotnet --list-sdks
    ```

- En GitHub-konto - For tilgang til GitHub Models Marketplace
- Azure-abonnement - For tilgang til Azure AI Foundry
- Azure AI Foundry-konto - For tilgang til Azure AI Agent Service

Vi har inkludert en `requirements.txt`-fil i roten av dette repositoriet som inneholder alle nødvendige Python-pakker for å kjøre kodeeksemplene.

Du kan installere dem ved å kjøre følgende kommando i terminalen i roten av repositoriet:

```bash|powershell
pip install -r requirements.txt
```

Vi anbefaler å opprette et Python-virtuelt miljø for å unngå konflikter og problemer.

## Oppsett av VSCode

Sørg for at du bruker riktig versjon av Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Oppsett for eksempler som bruker GitHub-modeller 

### Steg 1: Hent din GitHub Personal Access Token (PAT)

Dette kurset benytter GitHub Models Marketplace, som gir gratis tilgang til Large Language Models (LLMs) som du vil bruke til å bygge AI-agenter.

For å bruke GitHub-modellene, må du opprette en [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Dette kan gjøres ved å gå til <a href="https://github.com/settings/personal-access-tokens" target="_blank">Innstillinger for Personal Access Tokens</a> i din GitHub-konto.

Vennligst følg [Prinsippet om minst privilegium](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) når du oppretter tokenet. Dette betyr at du kun bør gi tokenet de tillatelsene det trenger for å kjøre kodeeksemplene i dette kurset.

1. Velg alternativet `Fine-grained tokens` på venstre side av skjermen ved å navigere til **Utviklerinnstillinger**

   ![Utviklerinnstillinger](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.no.png)

   Deretter velg `Generer nytt token`.

   ![Generer Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.no.png)

2. Skriv inn et beskrivende navn for tokenet som reflekterer dets formål, slik at det er lett å identifisere senere.

    🔐 Anbefaling for token-varighet

    Anbefalt varighet: 30 dager
    For en mer sikker tilnærming, kan du velge en kortere periode—som 7 dager 🛡️
    Det er en flott måte å sette et personlig mål og fullføre kurset mens læringsmomentet ditt er høyt 🚀.

    ![Token-navn og utløpsdato](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.no.png)

3. Begrens tokenets omfang til din fork av dette repositoriet.

    ![Begrens omfang til fork-repositoriet](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.no.png)

4. Begrens tokenets tillatelser: Under **Tillatelser**, klikk på **Konto**-fanen, og klikk på "+ Legg til tillatelser"-knappen. En rullegardinmeny vil vises. Vennligst søk etter **Modeller** og merk av for det.

    ![Legg til modeller-tillatelse](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.no.png)

5. Verifiser de nødvendige tillatelsene før du genererer tokenet. ![Verifiser tillatelser](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.no.png)

6. Før du genererer tokenet, sørg for at du er klar til å lagre tokenet på et sikkert sted som en passordhåndteringshvelv, da det ikke vil bli vist igjen etter at du har opprettet det. ![Lagre token sikkert](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.no.png)

Kopier ditt nye token som du nettopp har opprettet. Du vil nå legge dette til din `.env`-fil inkludert i dette kurset.

### Steg 2: Opprett din `.env`-fil

For å opprette din `.env`-fil, kjør følgende kommando i terminalen.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Dette vil kopiere eksempel-filen og opprette en `.env` i katalogen din hvor du fyller inn verdiene for miljøvariablene.

Med ditt token kopiert, åpne `.env`-filen i din favoritt tekstredigerer og lim inn tokenet ditt i `GITHUB_TOKEN`-feltet.

![GitHub Token-felt](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.no.png)

Du bør nå kunne kjøre kodeeksemplene i dette kurset.

## Oppsett for eksempler som bruker Azure AI Foundry og Azure AI Agent Service

### Steg 1: Hent din Azure-prosjektendepunkt

Følg stegene for å opprette en hub og prosjekt i Azure AI Foundry som finnes her: [Hubressurser oversikt](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources)

Når du har opprettet prosjektet ditt, må du hente tilkoblingsstrengen for prosjektet ditt.

Dette kan gjøres ved å gå til **Oversikt**-siden for prosjektet ditt i Azure AI Foundry-portalen.

![Prosjekt tilkoblingsstreng](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.no.png)

### Steg 2: Opprett din `.env`-fil

For å opprette din `.env`-fil, kjør følgende kommando i terminalen.

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Dette vil kopiere eksempel-filen og opprette en `.env` i katalogen din hvor du fyller inn verdiene for miljøvariablene.

Med ditt token kopiert, åpne `.env`-filen i din favoritt tekstredigerer og lim inn tokenet ditt i `PROJECT_ENDPOINT`-feltet.

### Steg 3: Logg inn på Azure

Som en sikkerhetsbest praksis, vil vi bruke [nøkkelfri autentisering](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) for å autentisere til Azure OpenAI med Microsoft Entra ID. 

Deretter åpner du en terminal og kjører `az login --use-device-code` for å logge inn på din Azure-konto.

Når du har logget inn, velg abonnementet ditt i terminalen.

## Ekstra miljøvariabler - Azure Search og Azure OpenAI 

For Agentic RAG-leksjonen - Leksjon 5 - finnes det eksempler som bruker Azure Search og Azure OpenAI.

Hvis du ønsker å kjøre disse eksemplene, må du legge til følgende miljøvariabler i din `.env`-fil:

### Oversiktsside (Prosjekt)

- `AZURE_SUBSCRIPTION_ID` - Sjekk **Prosjektdetaljer** på **Oversikt**-siden for prosjektet ditt.

- `AZURE_AI_PROJECT_NAME` - Se øverst på **Oversikt**-siden for prosjektet ditt.

- `AZURE_OPENAI_SERVICE` - Finn dette i **Inkluderte kapabiliteter**-fanen for **Azure OpenAI Service** på **Oversikt**-siden.

### Administrasjonssenter

- `AZURE_OPENAI_RESOURCE_GROUP` - Gå til **Prosjektegenskaper** på **Oversikt**-siden for **Administrasjonssenteret**.

- `GLOBAL_LLM_SERVICE` - Under **Tilkoblede ressurser**, finn **Azure AI Services**-tilkoblingsnavnet. Hvis det ikke er oppført, sjekk **Azure-portalen** under din ressursgruppe for AI Services-ressursnavnet.

### Modeller + Endepunktside

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Velg din embedding-modell (f.eks. `text-embedding-ada-002`) og noter **Deploymentsnavnet** fra modellens detaljer.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Velg din chat-modell (f.eks. `gpt-4o-mini`) og noter **Deploymentsnavnet** fra modellens detaljer.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Se etter **Azure AI-tjenester**, klikk på det, gå deretter til **Ressursadministrasjon**, **Nøkler og endepunkt**, bla ned til "Azure OpenAI-endepunkter", og kopier den som sier "Språk-API-er".

- `AZURE_OPENAI_API_KEY` - Fra samme skjerm, kopier NØKKEL 1 eller NØKKEL 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Finn din **Azure AI Search**-ressurs, klikk på den, og se **Oversikt**.

- `AZURE_SEARCH_API_KEY` - Gå deretter til **Innstillinger** og deretter **Nøkler** for å kopiere den primære eller sekundære admin-nøkkelen.

### Ekstern nettside

- `AZURE_OPENAI_API_VERSION` - Besøk siden [API-versjon livssyklus](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) under **Siste GA API-utgivelse**.

### Oppsett nøkkelfri autentisering

I stedet for å hardkode dine legitimasjoner, vil vi bruke en nøkkelfri tilkobling med Azure OpenAI. For å gjøre dette, vil vi importere `DefaultAzureCredential` og senere kalle funksjonen `DefaultAzureCredential` for å hente legitimasjonen.

```python
# Python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Sitter du fast et sted?
Hvis du har problemer med å kjøre denne oppsettet, bli med i vår <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">opprett en sak</a>.

## Neste leksjon

Du er nå klar til å kjøre koden for dette kurset. Lykke til med å lære mer om verdenen av AI-agenter!

[Introduksjon til AI-agenter og bruksområder for agenter](../01-intro-to-ai-agents/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.