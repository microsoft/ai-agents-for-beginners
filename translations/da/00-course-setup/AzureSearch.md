# Azure AI Search Opsætningsguide

Denne guide hjælper dig med at opsætte Azure AI Search ved hjælp af Azure-portalen. Følg trinene nedenfor for at oprette og konfigurere din Azure AI Search-service.

## Forudsætninger

Før du begynder, skal du sikre dig, at du har følgende:

- Et Azure-abonnement. Hvis du ikke har et Azure-abonnement, kan du oprette en gratis konto på [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Trin 1: Opret en Azure Storage-konto

1. Følg denne vejledning, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), for at oprette en ny Azure Storage-konto.
   **NOTE**: Sørg for, at typen af Storage Account er Standard General Purpose V2.

## Trin 2: Opret en Azure AI Search-service

1. Log ind på [Azure-portalen](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Klik på **Create a resource** i navigationsruden til venstre.
3. Skriv "Azure AI Search" i søgefeltet, og vælg **Azure AI Search** fra listen over resultater.
4. Klik på knappen **Create**.
5. I fanen **Basics** skal du angive følgende oplysninger:
   - **Subscription**: Vælg dit Azure-abonnement.
   - **Resource group**: Opret en ny ressourcegruppe eller vælg en eksisterende.
   - **Resource name**: Angiv et unikt navn til din søgeservice.
   - **Region**: Vælg den region, der er tættest på dine brugere.
   - **Pricing tier**: Vælg en prismodel, der passer til dine behov. Du kan starte med Free-tier til testformål.
6. Klik på **Review + create**.
7. Gennemse indstillingerne, og klik på **Create** for at oprette søgeservicen.

## Trin 3: Kom i gang med Azure AI Search

1. Når implementeringen er færdig, skal du gå til din søgeservice i Azure-portalen.
2. Kopier URL’en i oversigten for søgeservicen. Den skulle se ud som `https://<service-name>.search.windows.net`.
3. **(Anbefalet)** Aktiver nøgelfri adgang med Microsoft Entra ID (RBAC) som vist i trin 4 herunder — ingen nøgle nødvendig. Eksemplerne i denne guide opretter/opdaterer indeks og uploader dokumenter, som kræver rollerne **Search Service Contributor** og **Search Index Data Contributor** (eller ved nøglebaseret autentifikation den **primære admin-nøgle** — ikke forespørgselsnøglen). Kun hvis du ikke kan bruge RBAC, skal du åbne **Settings > Keys** og kopiere den **primære admin-nøgle**.
4. Følg trinene på siden [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) for at oprette et indeks, uploade data og foretage en søgning.

## Trin 4: Brug Azure AI Search-værktøjer

Azure AI Search integreres med forskellige værktøjer for at forbedre dine søgemuligheder. Du kan bruge Azure CLI, Python SDK, .NET SDK og andre værktøjer til avancerede konfigurationer og operationer.

### Brug af Azure CLI

1. Installer Azure CLI ved at følge instruktionerne på [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Log ind på Azure CLI med kommandoen:

   ```bash
   az login
   ```
3. **(Anbefalet) Aktiver nøgelfri adgang med Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Med RBAC aktiveret autentificerer Python- og .NET SDK-eksemplerne nedenfor med `DefaultAzureCredential`, som bruger din `az login` session under lokal udvikling — ingen admin-nøgle nødvendig. Se [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Fallback) Nøglebaseret autentifikation** — kun hvis du ikke kan bruge RBAC, skal du også gemme admin-nøglen:

#### Gem både endpoint og API-nøgle til Azure AI Search-instans som miljøvariabler.

   * **zsh / bash**
     ```bash
     # az search service show has no "endpoint" field; build the URL from the service name.
     export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
     export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

   * **PowerShell**
     ```powershell
     # az search service show has no "endpoint" field; build the URL from the service name.
     $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
     $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
     ```

### Brug af Python SDK

1. Installer Azure Cognitive Search-klientbiblioteket og Azure Identity til Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Brug følgende Python-kode til at oprette et indeks og uploade dokumenter:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (recommended): uses your `az login` identity via Entra ID RBAC.
    # Requires the "Search Service Contributor" and "Search Index Data Contributor" roles.
    credential = DefaultAzureCredential()
    # Fallback (key-based auth):
    # from azure.core.credentials import AzureKeyCredential
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

### Brug af .NET SDK

1. Kør følgende kommando for at oprette et indeks og uploade dokumenter:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    .NET-eksemplet nedenfor bruger `DefaultAzureCredential`, som kan bruge din Azure CLI-login fra `az login` under lokal udvikling.

2. Her er .NET-koden for `AzureSearch.cs`:

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

For mere detaljeret information, henvises der til følgende dokumentation:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Konklusion

Du har nu med succes opsat Azure AI Search ved hjælp af Azure-portalen og integreret værktøjer. Du kan nu udforske mere avancerede funktioner og muligheder i Azure AI Search for at forbedre dine søgeløsninger.

For yderligere assistance, besøg [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->