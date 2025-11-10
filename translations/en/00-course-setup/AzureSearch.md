<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:21:35+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "en"
}
-->
# Azure AI Search Setup Guide

This guide will help you set up Azure AI Search using the Azure portal. Follow the steps below to create and configure your Azure AI Search service.

## Prerequisites

Before you begin, ensure you have the following:

- An Azure subscription. If you don't have an Azure subscription, you can create a free account at [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Step 1: Create an Azure Storage Account

1. Follow this instruction, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), to create a new Azure Storage Account.
   **NOTE**: Make sure that the type of Storage Account is Standard General Purpose V2.

## Step 2: Create an Azure AI Search Service

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

## Step 3: Get Started with Azure AI Search

1. Once the deployment is complete, navigate to your search service in the Azure portal.
2. In the search service overview pane, copy the URL. It should look like `https://<service-name>.search.windows.net`.
3. In the Settings > Keys pane, copy the query key.
4. Follow the steps in the [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) page to create an index, upload data, and perform a search query.

## Step 4: Use Azure AI Search Tools

Azure AI Search integrates with various tools to enhance your search capabilities. You can use Azure CLI, Python SDK, .NET SDK and other tools for advanced configurations and operations.

### Using Azure CLI

1. Install the Azure CLI by following the instructions at [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Sign in to Azure CLI using the command:

   ```bash
   az login
   ```

3. Store both endpoint and API key for Azure AI Search instance to environment variables.

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

1. Install the Azure Cognitive Search client library for Python:

   ```bash
   pip install azure-search-documents
   ```

2. Use the following Python code to create an index and upload documents:

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

1. Run the following command to create an index and upload documents:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Here's the .NET code of `AzureSearch.cs`:

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

For more detailed information, refer to the following documentation:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusion

You have successfully set up Azure AI Search using the Azure portal and integrated tools. You can now explore more advanced features and capabilities of Azure AI Search to enhance your search solutions.

For further assistance, visit the [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.