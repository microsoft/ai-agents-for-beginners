<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-11T14:19:48+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "pcm"
}
-->
# Azure AI Search Setup Guide

Dis guide go help you set up Azure AI Search using di Azure portal. Follow di steps wey dey below to create and configure your Azure AI Search service.

## Prerequisites

Before you start, make sure say you get di following:

- One Azure subscription. If you no get Azure subscription, you fit create free account for [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Step 1: Create an Azure Storage Account

1. Follow dis instruction, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), to create new Azure Storage Account.
   **NOTE**: Make sure say di type of Storage Account na Standard General Purpose V2.

## Step 2: Create an Azure AI Search Service

1. Log in to di [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. For di left-hand navigation pane, click **Create a resource**.
3. For di search box, type "Azure AI Search" and select **Azure AI Search** from di list of results.
4. Click di **Create** button.
5. For di **Basics** tab, provide di following information:
   - **Subscription**: Select your Azure subscription.
   - **Resource group**: Create new resource group or select di one wey dey already.
   - **Resource name**: Enter unique name for your search service.
   - **Region**: Select di region wey near your users pass.
   - **Pricing tier**: Choose pricing tier wey fit your needs. You fit start with di Free tier for testing.
6. Click **Review + create**.
7. Check di settings and click **Create** to create di search service.

## Step 3: Get Started with Azure AI Search

1. Once di deployment don complete, go to your search service for di Azure portal.
2. For di search service overview pane, copy di URL. E go look like `https://<service-name>.search.windows.net`.
3. For di Settings > Keys pane, copy di query key.
4. Follow di steps for di [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) page to create index, upload data, and perform search query.

## Step 4: Use Azure AI Search Tools

Azure AI Search dey work with different tools to make your search better. You fit use Azure CLI, Python SDK, .NET SDK and other tools for advanced configurations and operations.

### Using Azure CLI

1. Install di Azure CLI by following di instructions for [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Log in to Azure CLI using dis command:

   ```bash
   az login
   ```

3. Store di endpoint and API key for Azure AI Search instance for environment variables.

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

### Using Python SDK

1. Install di Azure Cognitive Search client library for Python:

   ```bash
   pip install azure-search-documents
   ```

2. Use dis Python code to create index and upload documents:

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

### Using .NET SDK

1. Run dis command to create index and upload documents:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Dis na di .NET code for `AzureSearch.cs`:

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

For more detailed information, check di following documentation:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusion

You don successfully set up Azure AI Search using di Azure portal and di tools wey dey work with am. You fit now explore more advanced features and capabilities of Azure AI Search to make your search solutions better.

If you need more help, visit di [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleto service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am correct, abeg sabi say machine translation fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important mata, e good make professional human transleto check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->