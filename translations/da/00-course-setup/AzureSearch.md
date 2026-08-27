# Azure AI Search Opsætningsvejledning

Denne vejledning hjælper dig med at opsætte Azure AI Search ved hjælp af Azure-portalen. Følg trinene nedenfor for at oprette og konfigurere din Azure AI Search-tjeneste.

## Forudsætninger

Før du begynder, skal du sikre dig, at du har følgende:

- Et Azure-abonnement. Hvis du ikke har et Azure-abonnement, kan du oprette en gratis konto på [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Trin 1: Opret en Azure Storage-konto

1. Følg denne vejledning, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), for at oprette en ny Azure Storage-konto.
   **NOTE**: Sørg for, at typen af Storage-konto er Standard General Purpose V2.

## Trin 2: Opret en Azure AI Search-tjeneste

1. Log ind på [Azure-portalen](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Klik på **Opret en ressource** i navigationspanelet til venstre.
3. Skriv "Azure AI Search" i søgefeltet og vælg **Azure AI Search** i resultatlisten.
4. Klik på knappen **Opret**.
5. På fanen **Grundlæggende** angiv følgende oplysninger:
   - **Abonnement**: Vælg dit Azure-abonnement.
   - **Ressourcegruppe**: Opret en ny ressourcegruppe eller vælg en eksisterende.
   - **Ressourcenavn**: Indtast et unikt navn til din søgetjeneste.
   - **Region**: Vælg den region, der er tættest på dine brugere.
   - **Prisniveau**: Vælg et prisniveau, der passer til dine behov. Du kan starte med det gratis niveau til test.
6. Klik på **Gennemse + opret**.
7. Gennemgå indstillingerne, og klik på **Opret** for at oprette søgetjenesten.

## Trin 3: Kom i gang med Azure AI Search

1. Når udrulningen er fuldført, naviger til din søgetjeneste i Azure-portalen.
2. Kopiér URL'en i oversigtsruden for søgetjenesten. Den bør se sådan ud: `https://<service-name>.search.windows.net`.
3. **(Anbefalet)** Aktivér nøglefri adgang med Microsoft Entra ID (RBAC) som vist i trin 4 nedenfor — ingen nøgle nødvendig. Eksemplerne i denne vejledning opretter/opdaterer indeks og uploader dokumenter, hvilket kræver rollerne **Search Service Contributor** og **Search Index Data Contributor** (eller for nøglebaseret godkendelse den **primære administratørnøgle** — ikke forespørgselsnøglen). Kun hvis du ikke kan bruge RBAC, åbn panelet **Indstillinger > Nøgler** og kopier den **primære administratørnøgle**.
4. Følg trinnene i [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) for at oprette et indeks, uploade data og udføre en søgning.

## Trin 4: Brug Azure AI Search-værktøjer

Azure AI Search integreres med forskellige værktøjer for at forbedre dine søgemuligheder. Du kan bruge Azure CLI, Python SDK, .NET SDK og andre værktøjer til avancerede konfigurationer og operationer.

### Brug af Azure CLI

1. Installer Azure CLI ved at følge instruktionerne på [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Log ind på Azure CLI med kommandoen:

   ```bash
   az login
   ```
3. **(Anbefalet) Aktivér nøglefri adgang med Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show har ikke et "endpoint" felt; byg URL'en ud fra servicenavnet.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Med RBAC aktiveret, godkender Python- og .NET SDK-eksemplerne nedenfor med `DefaultAzureCredential`, som bruger din `az login`-session under lokal udvikling — ingen administratørnøgle nødvendig. Se [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Nødvendigt) Nøglebaseret godkendelse** — kun hvis du ikke kan bruge RBAC, opbevar også administratørnøglen:

#### Gem både slutpunkt og API-nøgle for Azure AI Search-forekomst som miljøvariable.

    ```bash
    # zsh/bash
    # az search service show har ikke feltet "endpoint"; opbyg URL'en ud fra servicenavnet.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show har ikke feltet "endpoint"; opbyg URL'en ud fra servicenavnet.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Brug af Python SDK

1. Installer klientbiblioteket Azure Cognitive Search og Azure Identity til Python:

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

    # Keyless (anbefalet): bruger din `az login` identitet via Entra ID RBAC.
    # Kræver rollerne "Search Service Contributor" og "Search Index Data Contributor".
    credential = DefaultAzureCredential()
    # Tilbagefald (nøglebaseret autentificering):
    # fra azure.core.credentials import AzureKeyCredential
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

2. Her er .NET-koden i `AzureSearch.cs`:

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

For mere detaljeret information henvises til følgende dokumentation:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Konklusion

Du har med succes opsat Azure AI Search ved hjælp af Azure-portalen og integrerede værktøjer. Du kan nu udforske mere avancerede funktioner og muligheder i Azure AI Search for at forbedre dine søgeløsninger.

For yderligere hjælp, besøg [Azure Cognitive Search dokumentationen](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->