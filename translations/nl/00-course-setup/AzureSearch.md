<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:41:28+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "nl"
}
-->
# Azure AI Search Installatiehandleiding

Deze handleiding helpt je bij het instellen van Azure AI Search via de Azure portal. Volg de onderstaande stappen om je Azure AI Search-service te maken en configureren.

## Vereisten

Voordat je begint, zorg ervoor dat je het volgende hebt:

- Een Azure-abonnement. Als je nog geen Azure-abonnement hebt, kun je een gratis account aanmaken op [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Stap 1: Maak een Azure Storage Account

1. Volg deze instructie, [Maak een Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), om een nieuw Azure Storage Account aan te maken.
   **NOTE**: Zorg ervoor dat het type Storage Account Standard General Purpose V2 is.

## Stap 2: Maak een Azure AI Search Service

1. Meld je aan bij de [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Klik in het navigatiemenu aan de linkerkant op **Create a resource**.
3. Typ in het zoekvak "Azure AI Search" en selecteer **Azure AI Search** uit de lijst met resultaten.
4. Klik op de knop **Create**.
5. Vul op het tabblad **Basics** de volgende informatie in:
   - **Subscription**: Selecteer je Azure-abonnement.
   - **Resource group**: Maak een nieuwe resourcegroep of selecteer een bestaande.
   - **Resource name**: Voer een unieke naam in voor je zoekservice.
   - **Region**: Selecteer de regio die het dichtst bij je gebruikers ligt.
   - **Pricing tier**: Kies een prijsklasse die past bij je behoeften. Je kunt beginnen met de gratis versie voor testen.
6. Klik op **Review + create**.
7. Controleer de instellingen en klik op **Create** om de zoekservice te maken.

## Stap 3: Aan de slag met Azure AI Search

1. Zodra de implementatie is voltooid, ga naar je zoekservice in de Azure portal.
2. Kopieer in het overzichtspaneel van de zoekservice de URL. Deze zou eruit moeten zien als `https://<service-name>.search.windows.net`.
3. Kopieer in het paneel Instellingen > Keys de querysleutel.
4. Volg de stappen op de [Quickstart-gids](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) pagina om een index te maken, gegevens te uploaden en een zoekopdracht uit te voeren.

## Stap 4: Gebruik Azure AI Search Tools

Azure AI Search integreert met verschillende tools om je zoekmogelijkheden te verbeteren. Je kunt Azure CLI, Python SDK, .NET SDK en andere tools gebruiken voor geavanceerde configuraties en bewerkingen.

### Gebruik van Azure CLI

1. Installeer de Azure CLI door de instructies te volgen op [Azure CLI installeren](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Meld je aan bij Azure CLI met het volgende commando:

   ```bash
   az login
   ```

3. Sla zowel de endpoint als de API-sleutel van de Azure AI Search-instantie op in omgevingsvariabelen.

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

### Gebruik van Python SDK

1. Installeer de Azure Cognitive Search clientbibliotheek voor Python:

   ```bash
   pip install azure-search-documents
   ```

2. Gebruik de volgende Python-code om een index te maken en documenten te uploaden:

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

### Gebruik van .NET SDK

1. Voer het volgende commando uit om een index te maken en documenten te uploaden:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Hier is de .NET-code van `AzureSearch.cs`:

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

Voor meer gedetailleerde informatie, raadpleeg de volgende documentatie:

- [Maak een Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Aan de slag met Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusie

Je hebt Azure AI Search succesvol ingesteld via de Azure portal en geïntegreerde tools. Je kunt nu meer geavanceerde functies en mogelijkheden van Azure AI Search verkennen om je zoekoplossingen te verbeteren.

Voor verdere hulp, bezoek de [Azure Cognitive Search documentatie](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.