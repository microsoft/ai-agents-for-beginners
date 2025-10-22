<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:32:36+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "en"
}
-->
# Azure AI Search Setup Guide

This guide will help you set up Azure AI Search using the Azure portal. Follow the steps below to create and configure your Azure AI Search service.

## Prerequisites

Before you begin, make sure you have the following:

- An Azure subscription. If you don’t have one, you can create a free account at [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Step 1: Create an Azure AI Search Service

1. Sign in to the [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. In the left-hand navigation pane, click **Create a resource**.
3. In the search box, type "Azure AI Search" and select **Azure AI Search** from the results.
4. Click the **Create** button.
5. On the **Basics** tab, fill in the following details:
   - **Subscription**: Choose your Azure subscription.
   - **Resource group**: Create a new resource group or select an existing one.
   - **Resource name**: Enter a unique name for your search service.
   - **Region**: Select the region closest to your users.
   - **Pricing tier**: Pick a pricing tier that fits your needs. You can start with the Free tier for testing.
6. Click **Review + create**.
7. Review your settings and click **Create** to set up the search service.

## Step 2: Get Started with Azure AI Search

1. After deployment completes, go to your search service in the Azure portal.
2. On the search service overview page, click the **Quickstart** button.
3. Follow the Quickstart guide to create an index, upload data, and run a search query.

### Create an Index

1. In the Quickstart guide, click **Create an index**.
2. Define the index schema by specifying fields and their attributes (e.g., data type, searchable, filterable).
3. Click **Create** to set up the index.

### Upload Data

1. In the Quickstart guide, click **Upload data**.
2. Select a data source (e.g., Azure Blob Storage, Azure SQL Database) and provide the required connection details.
3. Map the data source fields to the index fields.
4. Click **Submit** to upload the data to the index.

### Perform a Search Query

1. In the Quickstart guide, click **Search explorer**.
2. Enter a search query in the search box to test the search functionality.
3. Review the search results and adjust the index schema or data as needed.

## Step 3: Use Azure AI Search Tools

Azure AI Search works with various tools to enhance your search capabilities. You can use Azure CLI, Python SDK, and other tools for advanced configurations and operations.

### Using Azure CLI

1. Install the Azure CLI by following the instructions at [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Sign in to Azure CLI using the command:
   ```bash
   az login
   ```
3. Create a new search service with Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Create an index using Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
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

For more detailed information, see the following documentation:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusion

You have successfully set up Azure AI Search using the Azure portal and integrated tools. Now you can explore more advanced features and capabilities of Azure AI Search to improve your search solutions.

For additional help, visit the [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.