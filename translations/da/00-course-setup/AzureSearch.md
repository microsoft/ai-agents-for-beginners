<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:39:28+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "da"
}
-->
# Azure AI Search Opsætningsguide

Denne guide hjælper dig med at opsætte Azure AI Search ved hjælp af Azure-portalen. Følg trinnene nedenfor for at oprette og konfigurere din Azure AI Search-tjeneste.

## Forudsætninger

Før du begynder, skal du sikre dig, at du har følgende:

- Et Azure-abonnement. Hvis du ikke har et Azure-abonnement, kan du oprette en gratis konto på [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Trin 1: Opret en Azure Storage-konto

1. Følg denne vejledning, [Opret en Azure storage-konto](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), for at oprette en ny Azure Storage-konto.
   **NOTE**: Sørg for, at typen af Storage-konto er Standard General Purpose V2.

## Trin 2: Opret en Azure AI Search-tjeneste

1. Log ind på [Azure-portalen](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Klik på **Opret en ressource** i navigationspanelet til venstre.
3. Skriv "Azure AI Search" i søgefeltet, og vælg **Azure AI Search** fra listen over resultater.
4. Klik på knappen **Opret**.
5. På fanen **Grundlæggende** skal du angive følgende oplysninger:
   - **Abonnement**: Vælg dit Azure-abonnement.
   - **Ressourcegruppe**: Opret en ny ressourcegruppe eller vælg en eksisterende.
   - **Ressourcenavn**: Indtast et unikt navn til din søgetjeneste.
   - **Region**: Vælg den region, der er tættest på dine brugere.
   - **Prisniveau**: Vælg et prisniveau, der passer til dine behov. Du kan starte med den gratis niveau til test.
6. Klik på **Gennemse + opret**.
7. Gennemgå indstillingerne, og klik på **Opret** for at oprette søgetjenesten.

## Trin 3: Kom i gang med Azure AI Search

1. Når udrulningen er fuldført, skal du navigere til din søgetjeneste i Azure-portalen.
2. I oversigtspanelet for søgetjenesten skal du kopiere URL'en. Den bør se sådan ud: `https://<service-name>.search.windows.net`.
3. I Indstillinger > Nøgler-panelet skal du kopiere forespørgselsnøglen.
4. Følg trinnene på siden [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) for at oprette et indeks, uploade data og udføre en søgeforespørgsel.

## Trin 4: Brug Azure AI Search-værktøjer

Azure AI Search integreres med forskellige værktøjer for at forbedre dine søgemuligheder. Du kan bruge Azure CLI, Python SDK, .NET SDK og andre værktøjer til avancerede konfigurationer og operationer.

### Brug af Azure CLI

1. Installer Azure CLI ved at følge vejledningen på [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Log ind på Azure CLI ved hjælp af kommandoen:

   ```bash
   az login
   ```

3. Gem både endpoint og API-nøgle for Azure AI Search-instansen i miljøvariabler.

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

### Brug af Python SDK

1. Installer Azure Cognitive Search-klientbiblioteket til Python:

   ```bash
   pip install azure-search-documents
   ```

2. Brug følgende Python-kode til at oprette et indeks og uploade dokumenter:

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

### Brug af .NET SDK

1. Kør følgende kommando for at oprette et indeks og uploade dokumenter:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Her er .NET-koden for `AzureSearch.cs`:

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

For mere detaljeret information, se følgende dokumentation:

- [Opret en Azure Cognitive Search-tjeneste](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Kom i gang med Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search-værktøjer](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Konklusion

Du har nu med succes opsat Azure AI Search ved hjælp af Azure-portalen og integrerede værktøjer. Du kan nu udforske mere avancerede funktioner og muligheder i Azure AI Search for at forbedre dine søgeløsninger.

For yderligere hjælp, besøg [Azure Cognitive Search-dokumentationen](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.