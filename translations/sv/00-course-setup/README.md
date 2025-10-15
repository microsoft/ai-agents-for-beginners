<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T11:48:09+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "sv"
}
-->
# Kursinställning

## Introduktion

Den här lektionen kommer att täcka hur du kör kodexemplen i denna kurs.

## Gå med andra deltagare och få hjälp

Innan du börjar klona ditt repo, gå med i [AI Agents For Beginners Discord-kanalen](https://aka.ms/ai-agents/discord) för att få hjälp med installationen, ställa frågor om kursen eller för att ansluta med andra deltagare.

## Klona eller Forka detta Repo

För att börja, klona eller forka GitHub-repositoriet. Detta skapar din egen version av kursmaterialet så att du kan köra, testa och justera koden!

Detta kan göras genom att klicka på länken för att <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">forka repositoriet</a>.

Du bör nu ha din egen forkade version av denna kurs på följande länk:

![Forkat Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.sv.png)

### Shallow Clone (rekommenderas för workshop / Codespaces)

  >Det fullständiga repositoriet kan vara stort (~3 GB) när du laddar ner hela historiken och alla filer. Om du bara deltar i workshopen eller endast behöver några lektionsmappar, undviker en shallow clone (eller en sparse clone) det mesta av den nedladdningen genom att begränsa historiken och/eller hoppa över blobbar.

#### Snabb shallow clone — minimal historik, alla filer

Byt ut `<your-username>` i kommandona nedan med din fork-URL (eller upstream-URL om du föredrar det).

För att klona endast den senaste commit-historiken (liten nedladdning):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

För att klona en specifik branch:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Partiell (sparse) clone — minimala blobbar + endast valda mappar

Detta använder partiell kloning och sparse-checkout (kräver Git 2.25+ och rekommenderas modern Git med stöd för partiell kloning):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Gå in i repo-mappen:

För bash:

```bash
cd ai-agents-for-beginners
```

För Powershell:

```powershell
Set-Location ai-agents-for-beginners
```

Ange sedan vilka mappar du vill ha (exemplet nedan visar två mappar):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Efter att ha klonat och verifierat filerna, om du bara behöver filerna och vill frigöra utrymme (ingen git-historik), ta bort repositoriets metadata (💀irreversibelt — du kommer att förlora all Git-funktionalitet: inga commits, pulls, pushes eller historikåtkomst).

För Linux/macOS:

```bash
rm -rf .git
```

För Windows:

```powershell
Remove-Item -Recurse -Force .git
```

#### Använda GitHub Codespaces (rekommenderas för att undvika lokala stora nedladdningar)

- Skapa ett nytt Codespace för detta repo via [GitHub UI](https://github.com/codespaces).  

- I terminalen för det nyss skapade Codespace, kör en av shallow/sparse clone-kommandona ovan för att endast ta in de lektionsmappar du behöver i Codespace-arbetsytan.
- Valfritt: efter kloning i Codespaces, ta bort .git för att återta extra utrymme (se borttagningskommandon ovan).
- Obs: Om du föredrar att öppna repositoriet direkt i Codespaces (utan en extra kloning), var medveten om att Codespaces kommer att konstruera devcontainer-miljön och kan fortfarande tillhandahålla mer än du behöver. Att klona en shallow copy i ett nytt Codespace ger dig mer kontroll över diskanvändningen.

#### Tips

- Byt alltid ut clone-URL:en med din fork om du vill redigera/committa.
- Om du senare behöver mer historik eller filer kan du hämta dem eller justera sparse-checkout för att inkludera ytterligare mappar.

## Köra koden

Denna kurs erbjuder en serie Jupyter Notebooks som du kan köra för att få praktisk erfarenhet av att bygga AI-agenter.

Kodexemplen använder antingen:

**Kräver GitHub-konto - Gratis**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Märkt som (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Märkt som (autogen.ipynb)

**Kräver Azure-prenumeration**:
3) Azure AI Foundry + Azure AI Agent Service. Märkt som (azureaiagent.ipynb)

Vi uppmuntrar dig att prova alla tre typer av exempel för att se vilken som fungerar bäst för dig.

Oavsett vilket alternativ du väljer, kommer det att avgöra vilka installationssteg du behöver följa nedan:

## Krav

- Python 3.12+
  - **OBS**: Om du inte har Python3.12 installerat, se till att installera det. Skapa sedan din venv med python3.12 för att säkerställa att rätt versioner installeras från requirements.txt-filen.
  
    >Exempel

    Skapa Python venv-katalog:

    ``` bash
    python3 -m venv venv
    ```

    Aktivera sedan venv-miljön för:

    macOS och Linux

    ```bash
    source venv/bin/activate
    ```
  
    Windows

    ```bash
    venv\Scripts\activate
    ```

- Ett GitHub-konto - För åtkomst till GitHub Models Marketplace
- Azure-prenumeration - För åtkomst till Azure AI Foundry
- Azure AI Foundry-konto - För åtkomst till Azure AI Agent Service

Vi har inkluderat en `requirements.txt`-fil i roten av detta repositorium som innehåller alla nödvändiga Python-paket för att köra kodexemplen.

Du kan installera dem genom att köra följande kommando i din terminal vid roten av repositoriet:

```bash
pip install -r requirements.txt
```
Vi rekommenderar att skapa en Python-virtuell miljö för att undvika konflikter och problem.

## Installera VSCode
Se till att du använder rätt version av Python i VSCode.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Installation för exempel med GitHub-modeller 

### Steg 1: Hämta din GitHub Personal Access Token (PAT)

Denna kurs använder GitHub Models Marketplace, som ger gratis tillgång till Large Language Models (LLMs) som du kommer att använda för att bygga AI-agenter.

För att använda GitHub-modellerna måste du skapa en [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Detta kan göras genom att gå till dina <a href="https://github.com/settings/personal-access-tokens" target="_blank">inställningar för personliga åtkomsttoken</a> i ditt GitHub-konto.

Följ [Principen om minst privilegium](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) när du skapar din token. Detta innebär att du endast bör ge token de behörigheter den behöver för att köra kodexemplen i denna kurs.

1. Välj alternativet `Fine-grained tokens` på vänster sida av skärmen genom att navigera till **Developer settings**.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.sv.png)

    Välj sedan `Generate new token`.

    ![Generera Token](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.sv.png)

2. Ange ett beskrivande namn för din token som reflekterar dess syfte, vilket gör det enkelt att identifiera senare.


    🔐 Rekommendation för tokenens varaktighet

    Rekommenderad varaktighet: 30 dagar
    För en säkrare inställning kan du välja en kortare period—som 7 dagar 🛡️
    Det är ett utmärkt sätt att sätta ett personligt mål och slutföra kursen medan din lärandeenergi är hög 🚀.

    ![Token Namn och Utgångsdatum](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.sv.png)

3. Begränsa tokenens räckvidd till din fork av detta repositorium.

    ![Begränsa räckvidd till fork-repositorium](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.sv.png)

4. Begränsa tokenens behörigheter: Under **Permissions**, klicka på fliken **Account** och klicka på knappen "+ Add permissions". En dropdown-meny kommer att visas. Sök efter **Models** och kryssa i rutan för det.
    ![Lägg till Models-behörighet](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.sv.png)

5. Verifiera de behörigheter som krävs innan du genererar token. ![Verifiera Behörigheter](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.sv.png)

6. Innan du genererar token, se till att du är redo att lagra token på en säker plats som ett lösenordshanteringsvalv, eftersom den inte kommer att visas igen efter att du skapat den. ![Lagra Token Säkert](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.sv.png)

Kopiera din nya token som du just har skapat. Du kommer nu att lägga till denna i din `.env`-fil som ingår i denna kurs.


### Steg 2: Skapa din `.env`-fil

För att skapa din `.env`-fil, kör följande kommando i din terminal.

```bash
cp .env.example .env
```

Detta kommer att kopiera exempel-filen och skapa en `.env` i din katalog där du fyller i värdena för miljövariablerna.

Med din token kopierad, öppna `.env`-filen i din favorittextredigerare och klistra in din token i fältet `GITHUB_TOKEN`.
![GitHub Token-fält](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.sv.png)


Du bör nu kunna köra kodexemplen i denna kurs.

## Installation för exempel med Azure AI Foundry och Azure AI Agent Service

### Steg 1: Hämta din Azure-projektendpoint


Följ stegen för att skapa en hub och projekt i Azure AI Foundry som finns här: [Hub-resurser översikt](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)


När du har skapat ditt projekt, måste du hämta anslutningssträngen för ditt projekt.

Detta kan göras genom att gå till **Översikt**-sidan för ditt projekt i Azure AI Foundry-portalen.

![Projektanslutningssträng](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.sv.png)

### Steg 2: Skapa din `.env`-fil

För att skapa din `.env`-fil, kör följande kommando i din terminal.

```bash
cp .env.example .env
```

Detta kommer att kopiera exempel-filen och skapa en `.env` i din katalog där du fyller i värdena för miljövariablerna.

Med din token kopierad, öppna `.env`-filen i din favorittextredigerare och klistra in din token i fältet `PROJECT_ENDPOINT`.

### Steg 3: Logga in på Azure

Som en säkerhetsbästa praxis kommer vi att använda [nyckellös autentisering](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) för att autentisera till Azure OpenAI med Microsoft Entra ID. 

Öppna sedan en terminal och kör `az login --use-device-code` för att logga in på ditt Azure-konto.

När du har loggat in, välj din prenumeration i terminalen.


## Ytterligare miljövariabler - Azure Search och Azure OpenAI 

För Agentic RAG-lektionen - Lektion 5 - finns det exempel som använder Azure Search och Azure OpenAI.

Om du vill köra dessa exempel, måste du lägga till följande miljövariabler i din `.env`-fil:

### Översiktssida (Projekt)

- `AZURE_SUBSCRIPTION_ID` - Kontrollera **Projektdetaljer** på **Översikt**-sidan för ditt projekt.

- `AZURE_AI_PROJECT_NAME` - Titta högst upp på **Översikt**-sidan för ditt projekt.

- `AZURE_OPENAI_SERVICE` - Hitta detta i fliken **Inkluderade kapaciteter** för **Azure OpenAI Service** på **Översikt**-sidan.

### Hanteringscenter

- `AZURE_OPENAI_RESOURCE_GROUP` - Gå till **Projektinställningar** på **Översikt**-sidan för **Hanteringscenter**.

- `GLOBAL_LLM_SERVICE` - Under **Anslutna resurser**, hitta **Azure AI Services** anslutningsnamn. Om det inte listas, kontrollera **Azure-portalen** under din resursgrupp för AI Services resursnamn.

### Models + Endpoints-sida

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Välj din embedding-modell (t.ex. `text-embedding-ada-002`) och notera **Deployment name** från modellens detaljer.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Välj din chat-modell (t.ex. `gpt-4o-mini`) och notera **Deployment name** från modellens detaljer.

### Azure Portal

- `AZURE_OPENAI_ENDPOINT` - Leta efter **Azure AI Services**, klicka på det, gå sedan till **Resurshantering**, **Nycklar och Endpoint**, scrolla ner till "Azure OpenAI endpoints", och kopiera den som säger "Language APIs".

- `AZURE_OPENAI_API_KEY` - Från samma skärm, kopiera KEY 1 eller KEY 2.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Hitta din **Azure AI Search**-resurs, klicka på den, och se **Översikt**.

- `AZURE_SEARCH_API_KEY` - Gå sedan till **Inställningar** och sedan **Nycklar** för att kopiera den primära eller sekundära administratörsnyckeln.

### Extern webbsida

- `AZURE_OPENAI_API_VERSION` - Besök sidan [API-versionens livscykel](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) under **Senaste GA API-release**.

### Installera nyckellös autentisering

Istället för att hårdkoda dina autentiseringsuppgifter, kommer vi att använda en nyckellös anslutning med Azure OpenAI. För att göra detta, kommer vi att importera `DefaultAzureCredential` och senare kalla på funktionen `DefaultAzureCredential` för att få autentiseringen.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Fastnat någonstans?
Om du stöter på problem med att köra denna setup, gå med i vår <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> eller <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">skapa ett ärende</a>.

## Nästa Lektion

Du är nu redo att köra koden för denna kurs. Lycka till med att lära dig mer om AI-agenter! 

[Introduktion till AI-agenter och användningsområden](../01-intro-to-ai-agents/README.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.