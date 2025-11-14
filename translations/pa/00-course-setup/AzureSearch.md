<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:33:43+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "pa"
}
-->
# Azure AI Search ਸੈਟਅੱਪ ਗਾਈਡ

ਇਹ ਗਾਈਡ ਤੁਹਾਨੂੰ Azure ਪੋਰਟਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Azure AI Search ਸੈਟਅੱਪ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇਗੀ। ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਆਪਣੀ Azure AI Search ਸੇਵਾ ਬਣਾਓ ਅਤੇ ਸੰਰਚਿਤ ਕਰੋ।

## ਪੂਰਵ ਸ਼ਰਤਾਂ

ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਹੇਠਾਂ ਦਿੱਤੀ ਚੀਜ਼ਾਂ ਹਨ:

- ਇੱਕ Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਨਹੀਂ ਹੈ, ਤਾਂ ਤੁਸੀਂ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 'ਤੇ ਮੁਫ਼ਤ ਖਾਤਾ ਬਣਾਉਣ ਲਈ ਸਾਈਨ ਅੱਪ ਕਰ ਸਕਦੇ ਹੋ।

## ਕਦਮ 1: ਇੱਕ Azure Storage Account ਬਣਾਓ

1. [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) ਦੇ ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ, ਇੱਕ ਨਵਾਂ Azure Storage Account ਬਣਾਉਣ ਲਈ।
   **NOTE**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ Storage Account ਦੀ ਕਿਸਮ Standard General Purpose V2 ਹੈ।

## ਕਦਮ 2: ਇੱਕ Azure AI Search ਸੇਵਾ ਬਣਾਓ

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) 'ਤੇ ਸਾਈਨ ਇਨ ਕਰੋ।
2. ਖੱਬੇ ਪਾਸੇ ਨੈਵੀਗੇਸ਼ਨ ਪੈਨ ਵਿੱਚ, **Create a resource** 'ਤੇ ਕਲਿਕ ਕਰੋ।
3. ਖੋਜ ਬਾਕਸ ਵਿੱਚ "Azure AI Search" ਟਾਈਪ ਕਰੋ ਅਤੇ ਨਤੀਜਿਆਂ ਦੀ ਸੂਚੀ ਵਿੱਚੋਂ **Azure AI Search** ਚੁਣੋ।
4. **Create** ਬਟਨ 'ਤੇ ਕਲਿਕ ਕਰੋ।
5. **Basics** ਟੈਬ ਵਿੱਚ ਹੇਠਾਂ ਦਿੱਤੀ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰੋ:
   - **Subscription**: ਆਪਣੀ Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਚੁਣੋ।
   - **Resource group**: ਇੱਕ ਨਵਾਂ ਰਿਸੋਰਸ ਗਰੁੱਪ ਬਣਾਓ ਜਾਂ ਮੌਜੂਦਾ ਚੁਣੋ।
   - **Resource name**: ਆਪਣੀ ਸੇਵਾ ਲਈ ਇੱਕ ਵਿਲੱਖਣ ਨਾਮ ਦਾਖਲ ਕਰੋ।
   - **Region**: ਆਪਣੇ ਉਪਭੋਗਤਾਵਾਂ ਦੇ ਨੇੜੇ ਖੇਤਰ ਚੁਣੋ।
   - **Pricing tier**: ਆਪਣੀ ਜ਼ਰੂਰਤਾਂ ਅਨੁਸਾਰ ਇੱਕ ਪ੍ਰਾਈਸਿੰਗ ਟੀਅਰ ਚੁਣੋ। ਟੈਸਟਿੰਗ ਲਈ ਤੁਸੀਂ ਮੁਫ਼ਤ ਟੀਅਰ ਨਾਲ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹੋ।
6. **Review + create** 'ਤੇ ਕਲਿਕ ਕਰੋ।
7. ਸੈਟਿੰਗਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ ਅਤੇ ਸੇਵਾ ਬਣਾਉਣ ਲਈ **Create** 'ਤੇ ਕਲਿਕ ਕਰੋ।

## ਕਦਮ 3: Azure AI Search ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ

1. ਜਦੋਂ ਡਿਪਲੌਇਮੈਂਟ ਪੂਰਾ ਹੋ ਜਾਵੇ, ਤਾਂ Azure ਪੋਰਟਲ ਵਿੱਚ ਆਪਣੀ ਸੇਵਾ 'ਤੇ ਜਾਓ।
2. ਸੇਵਾ ਦੇ ਓਵਰਵਿਊ ਪੈਨ ਵਿੱਚ URL ਕਾਪੀ ਕਰੋ। ਇਹ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ `https://<service-name>.search.windows.net`।
3. Settings > Keys ਪੈਨ ਵਿੱਚ, ਕੁਇਰੀ ਕੀ ਕਾਪੀ ਕਰੋ।
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) ਪੇਜ ਵਿੱਚ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ, ਇੱਕ ਇੰਡੈਕਸ ਬਣਾਉਣ, ਡਾਟਾ ਅੱਪਲੋਡ ਕਰਨ ਅਤੇ ਸੇਰਚ ਕੁਇਰੀ ਕਰਨ ਲਈ।

## ਕਦਮ 4: Azure AI Search ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰੋ

Azure AI Search ਵੱਖ-ਵੱਖ ਟੂਲਜ਼ ਨਾਲ ਇੰਟੀਗਰੇਟ ਹੁੰਦਾ ਹੈ ਜੋ ਤੁਹਾਡੇ ਸੇਰਚ ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਵਧਾਉਂਦਾ ਹੈ। ਤੁਸੀਂ Azure CLI, Python SDK, .NET SDK ਅਤੇ ਹੋਰ ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ ਉੱਨਤ ਸੰਰਚਨਾਵਾਂ ਅਤੇ ਕਾਰਵਾਈਆਂ ਲਈ।

### Azure CLI ਦੀ ਵਰਤੋਂ

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) ਦੇ ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ Azure CLI ਇੰਸਟਾਲ ਕਰੋ।
2. ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Azure CLI ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ:

   ```bash
   az login
   ```

3. Azure AI Search ਇੰਸਟੈਂਸ ਲਈ ਐਂਡਪੌਇੰਟ ਅਤੇ API ਕੀ ਨੂੰ ਵਾਤਾਵਰਣ ਵੈਰੀਏਬਲ ਵਿੱਚ ਸਟੋਰ ਕਰੋ।

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

### Python SDK ਦੀ ਵਰਤੋਂ

1. Python ਲਈ Azure Cognitive Search ਕਲਾਇੰਟ ਲਾਇਬ੍ਰੇਰੀ ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   pip install azure-search-documents
   ```

2. ਹੇਠਾਂ ਦਿੱਤੇ Python ਕੋਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਇੰਡੈਕਸ ਬਣਾਓ ਅਤੇ ਡੌਕੂਮੈਂਟ ਅੱਪਲੋਡ ਕਰੋ:

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

### .NET SDK ਦੀ ਵਰਤੋਂ

1. ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਨੂੰ ਚਲਾਓ ਇੱਕ ਇੰਡੈਕਸ ਬਣਾਉਣ ਅਤੇ ਡੌਕੂਮੈਂਟ ਅੱਪਲੋਡ ਕਰਨ ਲਈ:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. ਇਹ .NET ਕੋਡ `AzureSearch.cs` ਹੈ:

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

ਹੋਰ ਵਿਸਥਾਰਿਤ ਜਾਣਕਾਰੀ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੇ ਦਸਤਾਵੇਜ਼ਾਂ ਨੂੰ ਵੇਖੋ:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ਨਤੀਜਾ

ਤੁਸੀਂ ਸਫਲਤਾਪੂਰਵਕ Azure ਪੋਰਟਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Azure AI Search ਸੈਟਅੱਪ ਕਰ ਲਿਆ ਹੈ ਅਤੇ ਟੂਲਜ਼ ਨੂੰ ਇੰਟੀਗਰੇਟ ਕੀਤਾ ਹੈ। ਹੁਣ ਤੁਸੀਂ Azure AI Search ਦੀ ਹੋਰ ਉੱਨਤ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਤੇ ਸਮਰੱਥਾਵਾਂ ਦੀ ਖੋਜ ਕਰ ਸਕਦੇ ਹੋ ਆਪਣੇ ਸੇਰਚ ਹੱਲਾਂ ਨੂੰ ਵਧਾਉਣ ਲਈ।

ਹੋਰ ਮਦਦ ਲਈ, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) 'ਤੇ ਜਾਓ।

---

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।