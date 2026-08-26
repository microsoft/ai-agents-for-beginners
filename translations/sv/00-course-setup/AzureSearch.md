# Azure AI Search installationsguide

Denna guide hjälper dig att ställa in Azure AI Search med hjälp av Azure-portalen. Följ stegen nedan för att skapa och konfigurera din Azure AI Search-tjänst.

## Förutsättningar

Innan du börjar, se till att du har följande:

- Ett Azure-prenumeration. Om du inte har en Azure-prenumeration kan du skapa ett gratis konto på [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Steg 1: Skapa ett Azure Storage-konto

1. Följ denna instruktion, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), för att skapa ett nytt Azure Storage-konto.
   **OBS**: Se till att typen av Storage-konto är Standard General Purpose V2.

## Steg 2: Skapa en Azure AI Search-tjänst

1. Logga in på [Azure-portalen](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. I navigationspanelen till vänster klickar du på **Skapa en resurs**.
3. Skriv "Azure AI Search" i sökrutan och välj **Azure AI Search** från resultatlistan.
4. Klicka på **Skapa**-knappen.
5. Under fliken **Grundläggande** anger du följande information:
   - **Prenumeration**: Välj din Azure-prenumeration.
   - **Resursgrupp**: Skapa en ny resursgrupp eller välj en befintlig.
   - **Resursnamn**: Ange ett unikt namn för din söktjänst.
   - **Region**: Välj den region som är närmast dina användare.
   - **Prisnivå**: Välj en prisnivå som passar dina krav. Du kan börja med gratisnivån för testning.
6. Klicka på **Granska + skapa**.
7. Granska inställningarna och klicka på **Skapa** för att skapa söktjänsten.

## Steg 3: Kom igång med Azure AI Search

1. När distributionen är klar, navigera till din söktjänst i Azure-portalen.
2. Kopiera URL:en i översikten för söktjänsten. Den bör se ut som `https://<service-name>.search.windows.net`.
3. **(Rekommenderas)** Aktivera nyckellös åtkomst med Microsoft Entra ID (RBAC) som visas i Steg 4 nedan — ingen nyckel behövs. Exemplen i denna guide skapar/uppdaterar index och laddar upp dokument, vilket kräver rollerna **Search Service Contributor** och **Search Index Data Contributor** (eller, för nyckelbaserad autentisering, **primär administratörsnyckel** — inte frågenyckeln). Endast om du inte kan använda RBAC, öppna **Inställningar > Nycklar** och kopiera den **primära administratörsnyckeln**.
4. Följ stegen i [Snabbstartsguiden](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) för att skapa ett index, ladda upp data och utföra en sökning.

## Steg 4: Använd Azure AI Search-verktyg

Azure AI Search integreras med olika verktyg för att förbättra dina sökmöjligheter. Du kan använda Azure CLI, Python SDK, .NET SDK och andra verktyg för avancerade konfigurationer och operationer.

### Använda Azure CLI

1. Installera Azure CLI genom att följa instruktionerna på [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Logga in i Azure CLI med kommandot:

   ```bash
   az login
   ```
3. **(Rekommenderas) Aktivera nyckellös åtkomst med Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show har inget "endpoint"-fält; bygg URL:en från tjänstens namn.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Med RBAC aktiverat autentiserar Python- och .NET SDK-exemplen nedan med `DefaultAzureCredential`, som använder din `az login`-session under lokal utveckling — ingen administratörsnyckel behövs. Se [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Reservplan) Nyckelbaserad autentisering** — endast om du inte kan använda RBAC, lagra administratörsnyckeln också:

#### Spara både slutpunkt och API-nyckel för Azure AI Search-instansen som miljövariabler.

    ```bash
    # zsh/bash
    # az search service show har inget "endpoint"-fält; bygg URL:en från servicens namn.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show har inget "endpoint"-fält; bygg URL:en från servicens namn.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Använda Python SDK

1. Installera Azure Cognitive Search-klientbiblioteket och Azure Identity för Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Använd följande Python-kod för att skapa ett index och ladda upp dokument:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (rekommenderas): använder din `az login`-identitet via Entra ID RBAC.
    # Kräver rollerna "Search Service Contributor" och "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Reservlösning (nyckelbaserad autentisering):
    # från azure.core.credentials importera AzureKeyCredential
    # credential = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
    index_client = SearchIndexClient(service_endpoint, credential)

    fields = [
        SimpleField(name="id", type=edm.String, key=True),
        SimpleField(name="content", type=edm.String, searchable=True),
    ]

    index = SearchIndex(name=index_name, fields=fields)

    index_client.create_index(index)

    search_client = SearchClient(service_endpoint, index_name, credential)

    documents = [
        {"id": "1", "content": "Hello world"},
        {"id": "2", "content": "Azure Cognitive Search"}
    ]

    search_client.upload_documents(documents)
    ```

### Använda .NET SDK

1. Kör följande kommando för att skapa ett index och ladda upp dokument:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    .NET-exemplet nedan använder `DefaultAzureCredential`, som kan använda din Azure CLI-inloggning från `az login` under lokal utveckling.

2. Här är .NET-koden för `AzureSearch.cs`:

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:package Azure.Identity@1.21.0
    #:property PublishAot=false

    using Azure;
    using Azure.Identity;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var indexName = "sample-index";

    // Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    // Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    var credential = new DefaultAzureCredential();
    // Fallback (key-based auth): the `using Azure;` directive above already imports
    // AzureKeyCredential; replace the credential line above with:
    // var credential = new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!);
    var indexClient = new SearchIndexClient(serviceEndpoint, credential);

    var fields = new List<SearchField>()
    {
        new SimpleField("id", SearchFieldDataType.String) { IsKey = true },
        new SearchableField("content")
    };

    var index = new SearchIndex(name: indexName, fields: fields);

    var response = await indexClient.CreateOrUpdateIndexAsync(index);
    Console.WriteLine($"Index '{response.Value.Name}' ready.");

    var searchClient = new SearchClient(serviceEndpoint, indexName, credential);

    var documents = new[]
    {
        new { id = "1", content = "Hello world" },
        new { id = "2", content = "Azure Cognitive Search" }
    };

    var result = await searchClient.UploadDocumentsAsync(documents);
    Console.WriteLine($"Uploaded {result.Value.Results.Count} documents to index '{response.Value.Name}'.");
    ```

För mer detaljerad information, se följande dokumentation:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Slutsats

Du har nu framgångsrikt ställt in Azure AI Search med hjälp av Azure-portalen och integrerade verktyg. Du kan nu utforska mer avancerade funktioner och möjligheter i Azure AI Search för att förbättra dina söklösningar.

För ytterligare hjälp, besök [Azure Cognitive Search-dokumentationen](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->