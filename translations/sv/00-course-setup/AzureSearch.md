<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:38:53+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "sv"
}
-->
# Azure AI Search Installationsguide

Den här guiden hjälper dig att konfigurera Azure AI Search med hjälp av Azure-portalen. Följ stegen nedan för att skapa och konfigurera din Azure AI Search-tjänst.

## Förutsättningar

Innan du börjar, se till att du har följande:

- Ett Azure-abonnemang. Om du inte har ett Azure-abonnemang kan du skapa ett gratis konto på [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Steg 1: Skapa ett Azure Storage-konto

1. Följ instruktionen, [Skapa ett Azure Storage-konto](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), för att skapa ett nytt Azure Storage-konto.
   **NOTE**: Se till att typen av Storage-konto är Standard General Purpose V2.

## Steg 2: Skapa en Azure AI Search-tjänst

1. Logga in på [Azure-portalen](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Klicka på **Skapa en resurs** i navigeringspanelen till vänster.
3. Skriv "Azure AI Search" i sökrutan och välj **Azure AI Search** från listan med resultat.
4. Klicka på knappen **Skapa**.
5. På fliken **Grundläggande**, ange följande information:
   - **Abonnemang**: Välj ditt Azure-abonnemang.
   - **Resursgrupp**: Skapa en ny resursgrupp eller välj en befintlig.
   - **Resursnamn**: Ange ett unikt namn för din söktjänst.
   - **Region**: Välj den region som är närmast dina användare.
   - **Prisnivå**: Välj en prisnivå som passar dina behov. Du kan börja med den kostnadsfria nivån för testning.
6. Klicka på **Granska + skapa**.
7. Granska inställningarna och klicka på **Skapa** för att skapa söktjänsten.

## Steg 3: Kom igång med Azure AI Search

1. När distributionen är klar, navigera till din söktjänst i Azure-portalen.
2. I översiktspanelen för söktjänsten, kopiera URL:en. Den bör se ut som `https://<service-name>.search.windows.net`.
3. I Inställningar > Nycklar-panelen, kopiera frågenyckeln.
4. Följ stegen på sidan [Snabbstartsguide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) för att skapa ett index, ladda upp data och utföra en sökfråga.

## Steg 4: Använd Azure AI Search-verktyg

Azure AI Search integreras med olika verktyg för att förbättra dina sökfunktioner. Du kan använda Azure CLI, Python SDK, .NET SDK och andra verktyg för avancerade konfigurationer och operationer.

### Använda Azure CLI

1. Installera Azure CLI genom att följa instruktionerna på [Installera Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Logga in på Azure CLI med kommandot:

   ```bash
   az login
   ```

3. Spara både slutpunkt och API-nyckel för Azure AI Search-instansen till miljövariabler.

    ```bash
    # zsh/bash
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Använda Python SDK

1. Installera Azure Cognitive Search-klientbiblioteket för Python:

   ```bash
   pip install azure-search-documents
   ```

2. Använd följande Python-kod för att skapa ett index och ladda upp dokument:

    ```python
    import os
    from azure.core.credentials import AzureKeyCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")
    index_name = "sample-index"

    credential = AzureKeyCredential(api_key)
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

2. Här är .NET-koden för `AzureSearch.cs`:

    ```csharp
    #:package Azure.Search.Documents@11.*
    #:property PublishAot=false

    using Azure;
    using Azure.Search.Documents;
    using Azure.Search.Documents.Indexes;
    using Azure.Search.Documents.Indexes.Models;

    var serviceEndpoint = new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_SERVICE_ENDPOINT")!);
    var apiKey = Environment.GetEnvironmentVariable("AZURE_SEARCH_API_KEY")!;
    var indexName = "sample-index";

    var credential = new AzureKeyCredential(apiKey);
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

- [Skapa en Azure Cognitive Search-tjänst](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Kom igång med Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search-verktyg](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Slutsats

Du har framgångsrikt konfigurerat Azure AI Search med hjälp av Azure-portalen och integrerade verktyg. Du kan nu utforska mer avancerade funktioner och kapaciteter i Azure AI Search för att förbättra dina söklösningar.

För ytterligare hjälp, besök [Azure Cognitive Search-dokumentationen](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.