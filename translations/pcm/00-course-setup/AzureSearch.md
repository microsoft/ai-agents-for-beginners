# Azure AI Search Setup Guide

Dis guide go help you set up Azure AI Search wit di Azure portal. Follow di steps wey dey below to create and configure your Azure AI Search service.

## Prerequisites

Before you start, make sure say you get di following:

- One Azure subscription. If you no get Azure subscription, you fit create free account for [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Step 1: Create an Azure Storage Account

1. Follow dis instruction, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), to create new Azure Storage Account.
   **NOTE**: Make sure say di type of Storage Account na Standard General Purpose V2.

## Step 2: Create an Azure AI Search Service

1. Sign in to di [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. For di left-hand navigation pane, click on **Create a resource**.
3. For di search box, type "Azure AI Search" and select **Azure AI Search** from di list.
4. Click di **Create** button.
5. For di **Basics** tab, provide di following information:
   - **Subscription**: Select your Azure subscription.
   - **Resource group**: Create new resource group or select one wey dey.
   - **Resource name**: Put unique name for your search service.
   - **Region**: Select di region wey dey near your users.
   - **Pricing tier**: Choose di pricing tier wey fit your need. You fit start with Free tier for testing.
6. Click **Review + create**.
7. Review di settings and click **Create** to create di search service.

## Step 3: Get Started with Azure AI Search

1. Once deployment finish, go your search service for Azure portal.
2. For di search service overview pane, copy di URL. E go be like `https://<service-name>.search.windows.net`.
3. **(Recommended)** Enable keyless access wit Microsoft Entra ID (RBAC) like e dey for Step 4 below — no key necessary. Di samples for dis guide dey create/update indexes and upload documents wey need **Search Service Contributor** and **Search Index Data Contributor** roles (or for key-based auth, di **primary admin key** — no be query key). Only if you no fit use RBAC, open **Settings > Keys** pane and copy **primary admin key**.
4. Follow di steps for di [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) page to create index, upload data, and perform search.

## Step 4: Use Azure AI Search Tools

Azure AI Search dey work with different tools to make your search beta. You fit use Azure CLI, Python SDK, .NET SDK and other tools for advanced configurations and operations.

### Using Azure CLI

1. Install Azure CLI by following instructions for [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Sign in to Azure CLI wit dis command:

   ```bash
   az login
   ```
3. **(Recommended) Enable keyless access wit Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service no get "endpoint" field; make di URL from di service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    Wit RBAC enabled, di Python and .NET SDK samples below dey authenticate wit `DefaultAzureCredential`, wey dey use your `az login` session during local development — no admin key needed. See [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(Fallback) Key-based auth** — only if you no fit use RBAC, store di admin key too:

#### Store both endpoint and API key for Azure AI Search instance to environment variables.

    ```bash
    # zsh/bash
    # az search service show no get "endpoint" field; build di URL from di service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show no get "endpoint" field; build di URL from di service name.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Using Python SDK

1. Install Azure Cognitive Search client library and Azure Identity for Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. Use di Python code below to create index and upload documents:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (wey dem recommend): e dey use your `az login` identity tru Entra ID RBAC.
    # E need di "Search Service Contributor" and "Search Index Data Contributor" roles.
    credential = DefaultAzureCredential()
    # If e no work (auth wey use key):
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

### Using .NET SDK

1. Run di command below to create index and upload documents:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    Di .NET sample below dey use `DefaultAzureCredential`, wey fit use your Azure CLI sign-in from `az login` during local development.

2. Dis na di .NET code for `AzureSearch.cs`:

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

For more detailed info, check di following documentation:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusion

You don successfully set up Azure AI Search using Azure portal and integrated tools. Now you fit explore beta features and capabilities of Azure AI Search to improve your search solutions.

For more help, visit di [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->