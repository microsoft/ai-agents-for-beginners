# Azure AI Search Setup Guide

This guide will help you set up Azure AI Search using the Azure portal. Follow the steps below to create and configure your Azure AI Search service.

## Prerequisites

Before you begin, ensure you have the following:

- An Azure subscription. If you don't have an Azure subscription, you can create a free account at [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Step 1: Create an Azure AI Search Service

1. Sign in to the [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. In the left-hand navigation pane, click on **Create a resource**.
3. In the search box, type "Azure AI Search" and select **Azure AI Search** from the list of results.
4. Click the **Create** button.
5. In the **Basics** tab, provide the following information:
   - **Subscription**: Select your Azure subscription.
   - **Resource group**: Create a new resource group or select an existing one.
   - **Resource name**: Enter a unique name for your search service.
   - **Region**: Select the region closest to your users.
   - **Pricing tier**: Choose a pricing tier that suits your requirements. You can start with the Free tier for testing.
6. Click **Review + create**.
7. Review the settings and click **Create** to create the search service.

## Step 2: Get Started with Azure AI Search

1. Once the deployment is complete, navigate to your search service in the Azure portal.
2. In the search service overview page, click on the **Quickstart** button.
3. Follow the steps in the Quickstart guide to create an index, upload data, and perform a search query.

### Create an Index

1. In the Quickstart guide, click on **Create an index**.
2. Define the index schema by specifying the fields and their attributes (e.g., data type, searchable, filterable).
3. Click **Create** to create the index.

### Upload Data

1. In the Quickstart guide, click on **Upload data**.
2. Choose a data source (e.g., Azure Blob Storage, Azure SQL Database) and provide the necessary connection details.
3. Map the data source fields to the index fields.
4. Click **Submit** to upload the data to the index.

### Perform a Search Query

1. In the Quickstart guide, click on **Search explorer**.
2. Enter a search query in the search box to test the search functionality.
3. Review the search results and adjust the index schema or data as needed.

## Step 3: Use Azure AI Search Tools

Azure AI Search integrates with various tools to enhance your search capabilities. You can use Azure CLI, Python SDK, .NET SDK and other tools for advanced configurations and operations.

### Using Azure CLI

1. Install the Azure CLI by following the instructions at [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Sign in to Azure CLI using the command:

   ```bash
   az login
   ```

3. Create a new search service using the Azure CLI:

   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```

4. Create an index using the Azure CLI:

   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

5. Store both endpoint and API key for Azure AI Search instance to environment variables.

    ```bash
    # zsh/bash
    export AZURE_SEARCH_SERVICE_ENDPOINT=$()
    export AZURE_SEARCH_API_KEY=$()
    ```

    ```powershell
    # PowerShell
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = $()
    $env:AZURE_SEARCH_API_KEY = $()
    ```

### Using Python SDK

1. Install the Azure Cognitive Search client library for Python:

   ```bash
   pip install azure-search-documents
   ```

2. Use the following Python code to create an index and upload documents:

   ```python
   from azure.core.credentials import AzureKeyCredential
   from azure.search.documents import SearchClient
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

   service_endpoint = "https://<service-name>.search.windows.net"
   api_key = "<api-key>"

   index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))

   fields = [
       SimpleField(name="id", type=edm.String, key=True),
       SimpleField(name="content", type=edm.String, searchable=True),
   ]

   index = SearchIndex(name="sample-index", fields=fields)

   index_client.create_index(index)

   search_client = SearchClient(service_endpoint, "sample-index", AzureKeyCredential(api_key))

   documents = [
       {"id": "1", "content": "Hello world"},
       {"id": "2", "content": "Azure Cognitive Search"}
   ]

   search_client.upload_documents(documents)
   ```

### Using .NET SDK

Store both Azure Search API endpoint and API key to environment variables:


Run the following command to create an index and upload documents:

```bash
dotnet run ./AzureSearch.cs
```

Here's the .NET code of `AzureSearch.cs`:

```csharp
#r "nuget: Azure.Search.Documents, 11.*"

using System;

using Azure;
using Azure.Search.Documents;
using Azure.Search.Documents.Indexes;
using Azure.Search.Documents.Indexes.Models;
using Azure.Search.Documents.Models;

var serviceEndpoint = new Uri("https://<service-name>.search.windows.net");
var apiKey = "<api-key>"; // Consider using an environment variable for security.
var indexName = "sample-index";

var credential = new AzureKeyCredential(apiKey);
var indexClient = new SearchIndexClient(serviceEndpoint, credential);

var index = new SearchIndex(indexName)
{
    Fields =
    {
        new SimpleField("id", SearchFieldDataType.String) { IsKey = true },
        new SearchableField("content")
    }
};

try
{
    // Idempotent create/update
    await indexClient.CreateOrUpdateIndexAsync(index);
    Console.WriteLine($"Index '{indexName}' ready.");
}
catch (RequestFailedException ex)
{
    Console.WriteLine($"Index operation failed: {ex.Message}");
    return;
}

var searchClient = new SearchClient(serviceEndpoint, indexName, credential);

// Documents to upload
var documents = new[]
{
    new { id = "1", content = "Hello world" },
    new { id = "2", content = "Azure Cognitive Search" }
};

try
{
    var uploadResult = await searchClient.UploadDocumentsAsync(documents);
    Console.WriteLine($"Uploaded {uploadResult.Value.Results.Count} documents.");
}
catch (RequestFailedException ex)
{
    Console.WriteLine($"Upload failed: {ex.Message}");
    return;
}

// Optional quick verification search
var searchText = "Azure";
var results = await searchClient.SearchAsync<SearchDocument>(searchText);
Console.WriteLine($"\nSearch results for '{searchText}':");
await foreach (var result in results.Value.GetResultsAsync())
{
    var doc = result.Document;
    Console.WriteLine($"{doc["id"]}: {doc["content"]}");
}

Console.WriteLine("\nDone.");
```

For more detailed information, refer to the following documentation:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusion

You have successfully set up Azure AI Search using the Azure portal and integrated tools. You can now explore more advanced features and capabilities of Azure AI Search to enhance your search solutions.

For further assistance, visit the [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).
