<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T08:40:54+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "da"
}
-->
# Kursusopsætning

## Introduktion

Denne lektion vil dække, hvordan du kører kodeeksemplerne fra dette kursus.

## Deltag med andre kursister og få hjælp

Før du begynder at klone dit repository, skal du tilmelde dig [AI Agents For Beginners Discord-kanalen](https://aka.ms/ai-agents/discord) for at få hjælp til opsætning, stille spørgsmål om kurset eller komme i kontakt med andre kursister.

## Klon eller fork dette repository

For at komme i gang skal du klone eller fork GitHub-repositoriet. Dette vil give dig din egen version af kursusmaterialet, så du kan køre, teste og tilpasse koden!

Dette kan gøres ved at klikke på linket for at <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forke repositoriet</a>.

Du bør nu have din egen forkede version af dette kursus på følgende link:

![Forked Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.da.png)

### Shallow Clone (anbefales til workshop / Codespaces)

  >Det fulde repository kan være stort (~3 GB), når du downloader hele historikken og alle filer. Hvis du kun deltager i workshoppen eller kun har brug for nogle få lektionsmapper, undgår en shallow clone (eller en sparse clone) det meste af den download ved at afkorte historikken og/eller springe blobs over.

#### Hurtig shallow clone — minimal historik, alle filer

Erstat `<your-username>` i nedenstående kommandoer med din fork-URL (eller upstream-URL, hvis du foretrækker det).

For kun at klone den seneste commit-historik (lille download):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

For at klone en specifik branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Delvis (sparse) clone — minimal blobs + kun udvalgte mapper

Dette bruger delvis kloning og sparse-checkout (kræver Git 2.25+ og anbefales moderne Git med delvis kloningssupport):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå ind i repo-mappen:

For bash:

```bash
cd ai-agents-for-beginners
```

For Powershell:

```powershell
Set-Location ai-agents-for-beginners
```

Angiv derefter, hvilke mapper du ønsker (eksemplet nedenfor viser to mapper):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Efter kloning og verificering af filerne, hvis du kun har brug for filerne og vil frigøre plads (ingen git-historik), skal du slette repository-metadata (💀irreversibelt — du mister al Git-funktionalitet: ingen commits, pulls, pushes eller historikadgang).

For Linux/macOS:

```bash
rm -rf .git
```

For Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### Brug af GitHub Codespaces (anbefales for at undgå store lokale downloads)

- Opret en ny Codespace for dette repo via [GitHub UI](https://github.com/codespaces).  

- I terminalen i den nyoprettede Codespace skal du køre en af de shallow/sparse clone-kommandoer ovenfor for kun at hente de lektionsmapper, du har brug for, til Codespace-arbejdsområdet.
- Valgfrit: Efter kloning i Codespaces, fjern .git for at frigøre ekstra plads (se fjernelseskommandoer ovenfor).
- Bemærk: Hvis du foretrækker at åbne repoen direkte i Codespaces (uden en ekstra kloning), skal du være opmærksom på, at Codespaces vil konstruere devcontainer-miljøet og stadig kan provisionere mere, end du har brug for. At klone en shallow kopi inde i en ny Codespace giver dig mere kontrol over diskforbruget.

#### Tips

- Erstat altid klon-URL'en med din fork, hvis du vil redigere/committe.
- Hvis du senere har brug for mere historik eller flere filer, kan du hente dem eller justere sparse-checkout for at inkludere yderligere mapper.

## Kør koden

Dette kursus tilbyder en række Jupyter Notebooks, som du kan køre for at få praktisk erfaring med at bygge AI-agenter.

Kodeeksemplerne bruger enten:

**Kræver GitHub-konto - Gratis**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Mærket som (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Mærket som (autogen.ipynb)

**Kræver Azure-abonnement**:
3) Azure AI Foundry + Azure AI Agent Service. Mærket som (azureaiagent.ipynb)

Vi opfordrer dig til at prøve alle tre typer eksempler for at se, hvilken der fungerer bedst for dig.

Uanset hvilken mulighed du vælger, vil det afgøre, hvilke opsætningstrin du skal følge nedenfor:

## Krav

- Python 3.12+
  - **NOTE**: Hvis du ikke har Python3.12 installeret, skal du sørge for at installere det. Opret derefter din venv ved hjælp af python3.12 for at sikre, at de korrekte versioner installeres fra requirements.txt-filen.
  
    >Eksempel

    Opret Python venv-mappe:

    ``` bash
    python3 -m venv venv
    ```

    Aktiver derefter venv-miljøet for:

    macOS og Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- En GitHub-konto - For adgang til GitHub Models Marketplace
- Azure-abonnement - For adgang til Azure AI Foundry
- Azure AI Foundry-konto - For adgang til Azure AI Agent Service

Vi har inkluderet en `requirements.txt`-fil i roden af dette repository, som indeholder alle de nødvendige Python-pakker for at køre kodeeksemplerne.

Du kan installere dem ved at køre følgende kommando i din terminal i roden af repositoriet:

```bash
pip install -r requirements.txt
```

Vi anbefaler at oprette et Python-virtuelt miljø for at undgå konflikter og problemer.

## Opsætning af VSCode
Sørg for, at du bruger den rigtige version af Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Opsætning til eksempler med GitHub-modeller 

### Trin 1: Hent din GitHub Personal Access Token (PAT)

Dette kursus benytter GitHub Models Marketplace, som giver gratis adgang til Large Language Models (LLMs), som du vil bruge til at bygge AI-agenter.

For at bruge GitHub-modellerne skal du oprette en [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Dette kan gøres ved at gå til dine <a href="https://github.com/settings/personal-access-tokens" target="_blank">indstillinger for personlige adgangstokens</a> i din GitHub-konto.

Følg venligst [Principle of Least Privilege](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely), når du opretter din token. Det betyder, at du kun skal give token de tilladelser, den har brug for, for at køre kodeeksemplerne i dette kursus.

1. Vælg `Fine-grained tokens`-muligheden på venstre side af din skærm ved at navigere til **Developer settings**.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.da.png)

    Vælg derefter `Generate new token`.

    ![Generate Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.da.png)

2. Indtast et beskrivende navn for din token, der afspejler dens formål, så det er nemt at identificere senere.

    🔐 Anbefaling til token-varighed

    Anbefalet varighed: 30 dage
    For en mere sikker tilgang kan du vælge en kortere periode—såsom 7 dage 🛡️
    Det er en god måde at sætte et personligt mål og fuldføre kurset, mens din læringsmotivation er høj 🚀.

    ![Token Name and Expiration](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.da.png)

3. Begræns tokenens rækkevidde til din fork af dette repository.

    ![Limit scope to fork repository](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.da.png)

4. Begræns tokenens tilladelser: Under **Permissions**, klik på **Account**-fanen, og klik på knappen "+ Add permissions". En dropdown-menu vil dukke op. Søg efter **Models** og marker boksen for det.
    ![Add Models Permission](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.da.png)

5. Bekræft de nødvendige tilladelser, før du genererer token. ![Verify Permissions](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.da.png)

6. Før du genererer token, skal du sikre dig, at du er klar til at gemme tokenen et sikkert sted som en adgangskodehåndteringsboks, da den ikke vil blive vist igen efter oprettelsen. ![Store Token Securely](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.da.png)

Kopier din nye token, som du lige har oprettet. Du vil nu tilføje denne til din `.env`-fil, der er inkluderet i dette kursus.

### Trin 2: Opret din `.env`-fil

For at oprette din `.env`-fil skal du køre følgende kommando i din terminal.

```bash
cp .env.example .env
```

Dette vil kopiere eksempel-filen og oprette en `.env` i din mappe, hvor du udfylder værdierne for miljøvariablerne.

Med din token kopieret, skal du åbne `.env`-filen i din foretrukne teksteditor og indsætte din token i feltet `GITHUB_TOKEN`.
![GitHub Token Field](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.da.png)

Du bør nu kunne køre kodeeksemplerne fra dette kursus.

## Opsætning til eksempler med Azure AI Foundry og Azure AI Agent Service

### Trin 1: Hent din Azure-projektendepunkt

Følg trinnene for at oprette en hub og et projekt i Azure AI Foundry, som du finder her: [Hub resources overview](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Når du har oprettet dit projekt, skal du hente forbindelsesstrengen til dit projekt.

Dette kan gøres ved at gå til **Oversigt**-siden for dit projekt i Azure AI Foundry-portalen.

![Project Connection String](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.da.png)

### Trin 2: Opret din `.env`-fil

For at oprette din `.env`-fil skal du køre følgende kommando i din terminal.

```bash
cp .env.example .env
```

Dette vil kopiere eksempel-filen og oprette en `.env` i din mappe, hvor du udfylder værdierne for miljøvariablerne.

Med din token kopieret, skal du åbne `.env`-filen i din foretrukne teksteditor og indsætte din token i feltet `PROJECT_ENDPOINT`.

### Trin 3: Log ind på Azure

Som en sikkerhedsmæssig bedste praksis vil vi bruge [keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) til at autentificere til Azure OpenAI med Microsoft Entra ID. 

Åbn derefter en terminal og kør `az login --use-device-code` for at logge ind på din Azure-konto.

Når du er logget ind, skal du vælge dit abonnement i terminalen.

## Yderligere miljøvariabler - Azure Search og Azure OpenAI 

For Agentic RAG-lektionen - Lektion 5 - er der eksempler, der bruger Azure Search og Azure OpenAI.

Hvis du vil køre disse eksempler, skal du tilføje følgende miljøvariabler til din `.env`-fil:

### Oversigtsside (Projekt)

- `AZURE_SUBSCRIPTION_ID` - Tjek **Projektoplysninger** på **Oversigt**-siden for dit projekt.

- `AZURE_AI_PROJECT_NAME` - Se øverst på **Oversigt**-siden for dit projekt.

- `AZURE_OPENAI_SERVICE` - Find dette under fanen **Inkluderede kapaciteter** for **Azure OpenAI Service** på **Oversigt**-siden.

### Management Center

- `AZURE_OPENAI_RESOURCE_GROUP` - Gå til **Projektoplysninger** på **Oversigt**-siden for **Management Center**.

- `GLOBAL_LLM_SERVICE` - Under **Forbundne ressourcer**, find **Azure AI Services** forbindelsesnavnet. Hvis det ikke er angivet, tjek **Azure-portalen** under din ressourcegruppe for AI Services ressource-navnet.

### Models + Endpoints Page

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Vælg din embedding-model (f.eks. `text-embedding-ada-002`) og noter **Deployment name** fra modeldetaljerne.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Vælg din chat-model (f.eks. `gpt-4o-mini`) og noter **Deployment name** fra modeldetaljerne.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Se efter **Azure AI services**, klik på det, gå derefter til **Resource Management**, **Keys and Endpoint**, scroll ned til "Azure OpenAI endpoints", og kopier den, der siger "Language APIs".

- `AZURE_OPENAI_API_KEY` - Fra samme skærm, kopier KEY 1 eller KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Find din **Azure AI Search**-ressource, klik på den, og se **Oversigt**.

- `AZURE_SEARCH_API_KEY` - Gå derefter til **Indstillinger** og derefter **Keys** for at kopiere den primære eller sekundære admin-nøgle.

### Ekstern webside

- `AZURE_OPENAI_API_VERSION` - Besøg siden [API version lifecycle](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) under **Latest GA API release**.

### Opsætning af keyless authentication

I stedet for at hardkode dine legitimationsoplysninger, vil vi bruge en keyless-forbindelse med Azure OpenAI. For at gøre dette vil vi importere `DefaultAzureCredential` og senere kalde funktionen `DefaultAzureCredential` for at få legitimationsoplysningerne.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Sidder du fast et sted?
Hvis du oplever problemer med at køre denne opsætning, så hop ind på vores <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">opret en issue</a>.

## Næste Lektion

Du er nu klar til at køre koden for dette kursus. God fornøjelse med at lære mere om AI-agenter!

[Introduktion til AI-agenter og anvendelsesområder](../01-intro-to-ai-agents/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.