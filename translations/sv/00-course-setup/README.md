# Kursinställning

## Introduktion

Denna lektion går igenom hur du kör kodexemplen i den här kursen.

## Gå med andra deltagare och få hjälp

Innan du börjar klona ditt repo, gå med i [AI Agents For Beginners Discord-kanal](https://aka.ms/ai-agents/discord) för att få hjälp med installation, ställa frågor om kursen eller för att komma i kontakt med andra deltagare.

## Klona eller fork:a det här repot

För att börja, klona eller forka GitHub-repositoryt. Detta skapar din egen version av kursmaterialet så att du kan köra, testa och justera koden!

Detta kan göras genom att klicka på länken för att <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">skapa en fork av repot</a>

Du bör nu ha din egen forkade version av denna kurs på följande länk:

![Forkat repo](../../../translated_images/sv/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (rekommenderas för workshop / Codespaces)

  >Det fulla repositoryt kan vara stort (~3 GB) när du laddar ner full historik och alla filer. Om du bara deltar i workshopen eller bara behöver några lektionsmappar så undviker en shallow clone (eller en sparse clone) det mesta av den nedladdningen genom att trunkera historik och/eller hoppa över blobs.

#### Snabb shallow clone — minimal historik, alla filer

Byt ut `<your-username>` i kommandona nedan mot din fork-URL (eller upstream-URL om du föredrar).

För att bara klona den senaste commit-historiken (liten nedladdning):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

För att klona en specifik branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partiell (sparse) clone — minimala blobs + endast valda mappar

Detta använder partial clone och sparse-checkout (kräver Git 2.25+ och rekommenderas modern Git med partial clone-stöd):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå in i repomappen:

```bash|powershell
cd ai-agents-for-beginners
```

Ange sedan vilka mappar du vill ha (exemplet nedan visar två mappar):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Efter kloning och verifiering av filerna, om du bara behöver filerna och vill frigöra utrymme (ingen git-historik), radera repository-metadata (💀irreversibelt — du kommer att förlora all Git-funktionalitet: inga commits, pulls, pushes eller historikåtkomst).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### Använda GitHub Codespaces (rekommenderas för att undvika stora lokala nedladdningar)

- Skapa en ny Codespace för detta repo via [GitHub UI](https://github.com/codespaces).  

- I terminalen i den nyskapade Codespacen, kör ett av shallow/sparse clone-kommandona ovan för att endast ta in de lektionsmappar du behöver i Codespace-arbetsytan.
- Valfritt: efter kloning inne i Codespaces, ta bort .git för att återfå extra utrymme (se borttagningskommandon ovan).
- Obs: Om du föredrar att öppna repot direkt i Codespaces (utan en extra kloning), var medveten om att Codespaces kommer att konstruera devcontainer-miljön och kan fortfarande provisionera mer än du behöver. Att klona en shallow-kopia inne i en ny Codespace ger dig mer kontroll över diskutrymmet.

#### Tips

- Byt alltid ut clone-URL:en mot din fork om du vill redigera/committa.
- Om du senare behöver mer historik eller fler filer kan du hämta dem eller justera sparse-checkout för att inkludera ytterligare mappar.

## Köra koden

Denna kurs innehåller en serie Jupyter-notebookar som du kan köra för att få praktisk erfarenhet av att bygga AI-agenter.

Exempelkoden använder **Microsoft Agent Framework (MAF)** med `AzureAIProjectAgentProvider`, som ansluter till **Azure AI Agent Service V2** (Responses API) via **Microsoft Foundry**.

Alla Python-notebookar är märkta `*-python-agent-framework.ipynb`.

## Krav

- Python 3.12+
  - **OBS**: Om du inte har Python 3.12 installerad, se till att installera den. Skapa sedan ditt venv med python3.12 för att säkerställa att rätt versioner installeras från requirements.txt-filen.
  
    >Exempel

    Skapa Python venv-katalog:

    ```bash|powershell
    python -m venv venv
    ```

    Aktivera sedan venv-miljön för:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: För sample-koderna som använder .NET, se till att du installerar [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) eller senare. Kontrollera sedan din installerade .NET SDK-version:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Krävs för autentisering. Installera från [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure Subscription** — För åtkomst till Microsoft Foundry och Azure AI Agent Service.
- **Microsoft Foundry Project** — Ett projekt med en utplacerad modell (t.ex. `gpt-4o`). Se [Steg 1](../../../00-course-setup) nedan.

Vi har inkluderat en `requirements.txt`-fil i rotmappen av detta repository som innehåller alla nödvändiga Python-paket för att köra kodexemplen.

Du kan installera dem genom att köra följande kommando i din terminal i repositoryts rot:

```bash|powershell
pip install -r requirements.txt
```

Vi rekommenderar att du skapar ett Python-virtuellt miljö (venv) för att undvika konflikter och problem.

## Konfigurera VSCode

Se till att du använder rätt version av Python i VSCode.

![bild](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee1f)

## Ställ in Microsoft Foundry och Azure AI Agent Service

### Steg 1: Skapa ett Microsoft Foundry-projekt

Du behöver ett Azure AI Foundry **hub** och ett **project** med en utplacerad modell för att köra notebookarna.

1. Gå till [ai.azure.com](https://ai.azure.com) och logga in med ditt Azure-konto.
2. Skapa ett **hub** (eller använd ett befintligt). Se: [Hub resources overview](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. Inne i hubben, skapa ett **project**.
4. Distribuera en modell (t.ex. `gpt-4o`) från **Modeller + Endpoints** → **Distribuera modell**.

### Steg 2: Hämta ditt projekts slutpunkt och modellens utplaceringsnamn

Från ditt projekt i Microsoft Foundry-portalen:

- **Projektets slutpunkt** — Gå till sidan **Översikt** och kopiera slutpunkts-URL:en.

![Projektets anslutningssträng](../../../translated_images/sv/project-endpoint.8cf04c9975bbfbf1.webp)

- **Modellens utplaceringsnamn** — Gå till **Modeller + Endpoints**, välj din utplacerade modell och notera **Utplaceringsnamn** (t.ex. `gpt-4o`).

### Steg 3: Logga in i Azure med `az login`

Alla notebookar använder **`AzureCliCredential`** för autentisering — inga API-nycklar att hantera. Detta kräver att du är inloggad via Azure CLI.

1. **Installera Azure CLI** om du inte redan gjort det: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Logga in** genom att köra:

    ```bash|powershell
    az login
    ```

    Eller om du befinner dig i en remote/Codespace-miljö utan webbläsare:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Välj din prenumeration** om du uppmanas — välj den som innehåller ditt Foundry-projekt.

4. **Verifiera** att du är inloggad:

    ```bash|powershell
    az account show
    ```

> **Varför `az login`?** Notebookarna autentiserar med `AzureCliCredential` från paketet `azure-identity`. Detta innebär att din Azure CLI-session tillhandahåller autentiseringsuppgifterna — inga API-nycklar eller hemligheter i din `.env`-fil. Detta är en [säkerhetsrutin](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### Steg 4: Skapa din `.env`-fil

Kopiera exempel-filen:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Öppna `.env` och fyll i dessa två värden:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry-portalen → ditt projekt → **Översikt**-sidan |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry-portalen → **Modeller + Endpoints** → din utplacerade modells namn |

Det är allt för de flesta lektioner! Notebookarna kommer att autentisera automatiskt via din `az login`-session.

### Steg 5: Installera Python-beroenden

```bash|powershell
pip install -r requirements.txt
```

Vi rekommenderar att köra detta inne i den virtuella miljö du skapade tidigare.

## Ytterligare setup för lektion 5 (Agentic RAG)

Lektion 5 använder **Azure AI Search** för retrieval-augmented generation. Om du planerar att köra den lektionen, lägg till dessa variabler i din `.env`-fil:

| Variable | Where to find it |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure-portalen → din **Azure AI Search**-resurs → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure-portalen → din **Azure AI Search**-resurs → **Settings** → **Keys** → primär admin-nyckel |

## Ytterligare setup för lektion 6 och lektion 8 (GitHub Models)

Vissa notebookar i lektion 6 och 8 använder **GitHub Models** istället för Azure AI Foundry. Om du planerar att köra dessa exempel, lägg till dessa variabler i din `.env`-fil:

| Variable | Where to find it |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Use `https://models.inference.ai.azure.com` (default value) |
| `GITHUB_MODEL_ID` | Model name to use (e.g. `gpt-4o-mini`) |

## Ytterligare setup för lektion 8 (Bing Grounding Workflow)

Den villkorade workflow-notebooken i lektion 8 använder **Bing grounding** via Azure AI Foundry. Om du planerar att köra det exemplet, lägg till denna variabel i din `.env`-fil:

| Variable | Where to find it |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry-portalen → ditt projekt → **Management** → **Connected resources** → din Bing-anslutning → kopiera connection ID |

## Felsökning

### SSL-certifikatverifieringsfel på macOS

Om du är på macOS och får ett fel som liknar:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Detta är ett känt problem med Python på macOS där systemets SSL-certifikat inte automatiskt litas på. Prova följande lösningar i ordning:

**Alternativ 1: Kör Pythons Install Certificates-skript (rekommenderas)**

```bash
# Byt ut 3.XX mot din installerade Python-version (t.ex. 3.12 eller 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**Alternativ 2: Använd `connection_verify=False` i din notebook (endast för GitHub Models-notebookar)**

I Lesson 6-notebooken (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) finns en utkommenterad workaround redan inkluderad. Avkommentera `connection_verify=False` när du skapar klienten:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Inaktivera SSL-verifiering om du stöter på certifikatfel
)
```

> **⚠️ Varning:** Att inaktivera SSL-verifiering (`connection_verify=False`) minskar säkerheten genom att hoppa över certifikatvalidering. Använd detta endast som en tillfällig lösning i utvecklingsmiljöer, aldrig i produktion.

**Alternativ 3: Installera och använd `truststore`**

```bash
pip install truststore
```

Lägg sedan till följande högst upp i din notebook eller skript innan du gör några nätverksanrop:

```python
import truststore
truststore.inject_into_ssl()
```

## Fast någonstans?

Om du har problem med att köra denna installation, hoppa in i vår <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">skapa ett ärende</a>.

## Nästa lektion

Du är nu redo att köra koden för denna kurs. Lycka till med att lära dig mer om AI-agenternas värld! 

[Introduktion till AI-agenter och användningsfall](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfriskrivning:
Detta dokument har översatts med hjälp av AI-översättningstjänsten Co-op Translator (https://github.com/Azure/co-op-translator). Vi strävar efter att vara korrekta, men vänligen observera att automatiska översättningar kan innehålla fel eller brister. Originaldokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->