# ਅਜ਼ੂਰ ਏਆਈ ਸਰਚ ਸੈਟਅਪ ਗਾਈਡ

ਇਹ ਗਾਈਡ ਤੁਹਾਡੀ ਮਦਦ ਕਰੇਗੀ ਅਜ਼ੂਰ ਪੋਰਟਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਜ਼ੂਰ ਏਆਈ ਸਰਚ ਸੈਟਅਪ ਕਰਨ ਵਿੱਚ। ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਨੂੰ ਫਾਲੋ ਕਰੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਆਪਣੀ ਅਜ਼ੂਰ ਏਆਈ ਸਰਚ ਸੇਵਾ ਬਣਾਈ ਅਤੇ ਸੰਰਚਿਤ ਕਰ ਸਕੋ।

## ਸ਼ਰਤਾਂ

ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਹੇਠਾਲੇ ਹਨ:

- ਇੱਕ ਅਜ਼ੂਰ ਸਬਸਕ੍ਰਿਪਸ਼ਨ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਅਜ਼ੂਰ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਨਹੀਂ ਹੈ, ਤਾਂ ਤੁਸੀਂ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 'ਤੇ ਮੁਫ਼ਤ ਖਾਤਾ ਬਣਾ ਸਕਦੇ ਹੋ।

## ਕਦਮ 1: ਇੱਕ ਅਜ਼ੂਰ ਸਟੋਰੇਜ ਅਕਾਊਂਟ ਬਣਾਓ

1. ਹੇਠਾਂ ਦਿੱਤੀ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), ਤਾਂ ਜੋ ਇੱਕ ਨਵਾਂ ਅਜ਼ੂਰ ਸਟੋਰੇਜ ਅਕਾਊਂਟ ਬਣਾਇਆ ਜਾ ਸਕੇ।
   **ਨੋਟ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਟੋਰੇਜ ਅਕਾਊਂਟ ਦੀ ਕਿਸਮ Standard General Purpose V2 ਹੈ।

## ਕਦਮ 2: ਇੱਕ ਅਜ਼ੂਰ ਏਆਈ ਸਰਚ ਸੇਵਾ ਬਣਾਓ

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ।
2. ਖੱਬੇ ਹੱਥ ਦੇ ਨੈਵੀਗੇਸ਼ਨ ਪੈਨ ਵਿਚ, **Create a resource** ਤੇ ਕਲਿੱਕ ਕਰੋ।
3. ਖੋਜ ਬਾਕਸ ਵਿੱਚ "Azure AI Search" ਟਾਈਪ ਕਰੋ ਅਤੇ ਨਤੀਜਿਆਂ ਵਿੱਚੋਂ **Azure AI Search** ਚੁਣੋ।
4. **Create** ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
5. **Basics** ਟੈਬ ਵਿੱਚ, ਹੇਠਾਂ ਦਿੱਤੀ ਜਾਣਕਾਰੀ ਭਰੋ:
   - **Subscription**: ਆਪਣੀ ਅਜ਼ੂਰ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਚੁਣੋ।
   - **Resource group**: ਇੱਕ ਨਵਾਂ ਰਿਸੋਰਸ ਗਰੂਪ ਬਣਾਓ ਜਾਂ ਮੌਜੂਦਾ ਵਿੱਚੋਂ ਚੁਣੋ।
   - **Resource name**: ਆਪਣੀ ਸਰਚ ਸੇਵਾ ਲਈ ਇੱਕ ਵਿਲੱਖਣ ਨਾਮ ਦਿਓ।
   - **Region**: ਆਪਣੇ ਉਪਭੋਗਤਿਆਂ ਦੇ ਸਭ ਤੋਂ ਨੇੜਲੇ ਖੇਤਰ ਨੂੰ ਚੁਣੋ।
   - **Pricing tier**: ਆਪਣੀਆਂ ਲੋੜਾਂ ਮੁਤਾਬਕ ਇੱਕ ਪ੍ਰਾਈਸਿੰਗ ਟੀਅਰ ਚੁਣੋ। ਤੁਸੀਂ ਟੈਸਟ ਕਰਨ ਲਈ ਮੁਫ਼ਤ ਟੀਅਰ ਨਾਲ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹੋ।
6. **Review + create** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
7. ਸੈਟਿੰਗਜ਼ ਦੀ ਸਮੀਖਿਆ ਕਰੋ ਅਤੇ ਸਰਚ ਸੇਵਾ ਬਣਾਉਣ ਲਈ **Create** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।

## ਕਦਮ 3: ਅਜ਼ੂਰ ਏਆਈ ਸਰਚ ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰੋ

1. ਜਦੋਂ ਤਾਇਨਾਤੀ ਪੂਰੀ ਹੋ ਜਾਵੇ, ਤਦ ਆਪਣੇ ਸਰਚ ਸੇਵਾ ਵੱਲ ਅਜ਼ੂਰ ਪੋਰਟਲ ਵਿੱਚ ਜਾਓ।
2. ਸਰਚ ਸੇਵਾ ਓਵਰਵਿਊ ਪੈਨ ਵਿੱਚ, URL ਦੀ নਕਲ ਕਰੋ। ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਲੱਗੇਗਾ `https://<service-name>.search.windows.net`।
3. **(ਸਿਫਾਰਸ਼ੀ)** Microsoft Entra ID (RBAC) ਨਾਲ ਕੀ-ਰਹਿਤ ਪਹੁੰਚ ਸਕ੍ਰੀਨ ਕਰੋ ਜੋ ਹੇਠਾਂ ਕਦਮ 4 ਵਿੱਚ ਦਿੱਤੀ ਹੈ — ਕਿਸੇ ਵੀ ਚابی ਦੀ ਲੋੜ ਨਹੀਂ। ਇਸ ਗਾਈਡ ਦੇ ਉਦਾਹਰਨਸਾਰ ਇੰਡੈਕਸ ਬਣਾਉਣ/ਅੱਪਡੇਟ ਕਰਨ ਅਤੇ ਦਸਤਾਵੇਜ਼ਾਂ ਅਪਲੋਡ ਕਰਨ ਲਈ, **Search Service Contributor** ਤੇ **Search Index Data Contributor** ਭੂਮਿਕਾਵਾਂ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ (ਜਾਂ, ਕੀ ਅਧਾਰਤ ਪ੍ਰਮਾਣਿਕਤਾ ਲਈ, **primary admin key** — ਕਮਾਂਡ ਕੁੰਜੀ ਨਹੀਂ)। ਜੇ ਤੁਸੀਂ RBAC ਵਰਤ ਨਹੀਂ ਸਕਦੇ, ਤਾਂ **Settings > Keys** ਪੈਨ ਖੋਲ੍ਹੋ ਅਤੇ **primary admin key** ਦੀ ਨਕਲ ਕਰੋ।
4. ਇੰਡੈਕਸ ਬਣਾਉਣ, ਡਾਟਾ ਅਪਲੋਡ ਕਰਨ ਅਤੇ ਖੋਜ ਕਰਨ ਲਈ [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) 'ਤੇ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ।

## ਕਦਮ 4: ਅਜ਼ੂਰ ਏਆਈ ਸਰਚ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ

ਅਜ਼ੂਰ ਏਆਈ ਸਰਚ ਵੱਖ-ਵੱਖ ਟੂਲਾਂ ਨਾਲ ਇੱਕੀਕ੍ਰਿਤ ਹੁੰਦੀ ਹੈ ਤਾਂ ਜੋ ਤੁਹਾਡੇ ਖੋਜ ਯੋਗਤਾਵਾਂ ਨੂੰ ਵਧਾਇਆ ਜਾ ਸਕੇ। ਤੁਸੀਂ ਅਜ਼ੂਰ CLI, Python SDK, .NET SDK ਅਤੇ ਹੋਰ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਅੱਗੇਲੇ ਸੰਰਚਨਾਂ ਅਤੇ ਕਿਰਿਆਵਾਂ ਲਈ ਕਰ ਸਕਦੇ ਹੋ।

### ਅਜ਼ੂਰ CLI ਦੀ ਵਰਤੋਂ ਕਰਕੇ

1. ਹੇਠਾਂ ਦਿੱਤੇ ਨਿਰਦੇਸ਼ਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਅਜ਼ੂਰ CLI ਇੰਸਟਾਲ ਕਰੋ: [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)।
2. ਕਮਾਂਡ ਦਾ ਉਪਯੋਗ ਕਰਕੇ ਅਜ਼ੂਰ CLI ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ:

   ```bash
   az login
   ```
3. **(ਸਿਫਾਰਸ਼ੀ) Microsoft Entra ID (RBAC) ਨਾਲ ਕੀ-ਰਹਿਤ ਪਹੁੰਚ ਸਕ੍ਰੀਨ ਕਰੋ:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service ਵਿਖਾਉਂਦਾ ਹੈ ਕਿ "endpoint" ਫੀਲਡ ਨਹੀਂ ਹੈ; ਸੇਵਾ ਦੇ ਨਾਮ ਤੋਂ URL ਬਣਾਓ।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC ਯੋਗ ਹੈ, ਤਾਂ ਹੇਠਾਂ ਦਿੱਤੇ Python ਅਤੇ .NET SDK ਦੇ ਨਮੂਨੇ `DefaultAzureCredential` ਨਾਲ ਪ੍ਰਮਾਣੀਕਰਨ ਕਰਦੇ ਹਨ, ਜੋ ਤੁਹਾਡੇ `az login` ਸੈਸ਼ਨ ਨੂੰ ਲੋਕਲ ਵਿਕਾਸ ਦੌਰਾਨ ਵਰਤਦਾ ਹੈ — ਕਿਸੇ ਪ੍ਰਸ਼ਾਸਕੀ ਕੁੰਜੀ ਦੀ ਲੋੜ ਨਹੀਂ। ਵੇਖੋ [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)।

4. **(ਵਿਕਲਪਿਕ) ਕੀ-ਅਧਾਰਿਤ ਪ੍ਰਮਾਣਿਕਤਾ** — ਸਿਰਫ ਜੇ ਤੁਸੀਂ RBAC ਵਰਤ ਨਹੀਂ ਕਰ ਸਕਦੇ, ਤਾਂ ਪ੍ਰਸ਼ਾਸਕੀ ਕੁੰਜੀ ਨੂੰ ਵੀ ਸੰਭਾਲੋ:

#### ਅਜ਼ੂਰ ਏਆਈ ਸਰਚ ਉਦਾਹਰਨ ਲਈ Endpoint ਅਤੇ API ਕੁੰਜੀ ਦੋਹਾਂ ਨੂੰ ਵਾਤਾਵਰਣ ਚਰ (environment variables) ਵਿੱਚ ਸੰਜੋਇਓ।

    ```bash
    # zsh/bash
    # az search service show ਵਿੱਚ "endpoint" ਫੀਲਡ ਨਹੀਂ ਹੈ; URL ਨੂੰ ਸਰਵਿਸ ਨਾਮ ਤੋਂ ਬਣਾ ਕੇ ਬਣਾਓ।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show ਵਿੱਚ "endpoint" ਫੀਲਡ ਨਹੀਂ ਹੈ; URL ਨੂੰ ਸਰਵਿਸ ਨਾਮ ਤੋਂ ਬਣਾ ਕੇ ਬਣਾਓ।
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ

1. ਅਜ਼ੂਰ ਕੋਗਨੀਟਿਵ ਸਰਚ ਕਲਾਇੰਟ ਲਾਇਬ੍ਰੇਰੀ ਅਤੇ ਅਜ਼ੂਰ ਆਈਡੈਂਟਿਟੀ ਫਾਰ Python ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ਹੇਠਾਂ ਦਿੱਤੇ Python ਕੋਡ ਦੀ ਵਰਤੋਂ ਕਰ ਕੇ ਇੰਡੈਕਸ ਬਣਾਓ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਅਪਲੋਡ ਕਰੋ:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # ਕੀਲੇਸ (ਸਿਫਾਰਸ਼ੀ): ਤੁਹਾਡੇ `az login` ਪਛਾਣ ਨੂੰ Entra ID RBAC ਰਾਹੀਂ ਵਰਤਦਾ ਹੈ।
    # "ਸਰਚ ਸਰਵਿਸ ਕੰਟ੍ਰੀਬਿਊਟਰ" ਅਤੇ "ਸਰਚ ਇੰਡੈਕਸ ਡਾਟਾ ਕੰਟ੍ਰੀਬਿਊਟਰ" ਭੂਮਿਕਾਵਾਂ ਦੀ ਲੋੜ ਹੈ।
    credential = DefaultAzureCredential()
    # ਵਾਪਸੀ (ਕੀ-ਆਧਾਰਿਤ ਪ੍ਰਮਾਣਿਕਤਾ):
    # azure.core.credentials ਤੋਂ AzureKeyCredential ਨੂੰ ਆਯਾਤ ਕਰੋ
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

### .NET SDK ਦੀ ਵਰਤੋਂ ਕਰਕੇ

1. ਹੇਠਾਂ ਦਿੱਤੀ ਕਮਾਂਡ ਚਲਾਕੇ ਇੰਡੈਕਸ ਬਣਾਓ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਅਪਲੋਡ ਕਰੋ:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    ਹੇਠਾਂ ਦਿੱਤੇ .NET ਨਮੂਨੇ `DefaultAzureCredential` ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ, ਜੋ ਤੁਹਾਡੇ ਲੋਕਲ ਵਿਕਾਸ ਦੌਰਾਨ `az login` ਤੋਂ ਅਜ਼ੂਰ CLI ਸਾਈਨ-ਇਨ ਨੂੰ ਵਰਤ ਸਕਦਾ ਹੈ।

2. ਇੱਥੇ `AzureSearch.cs` ਦਾ .NET ਕੋਡ ਹੈ:

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

ਹੋਰ ਵਿਸਥਾਰਦਾਰ ਜਾਣਕਾਰੀ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੀ ਦਸਤਾਵੇਜ਼ੀ ਸੰਦਰਭ ਲੋੜੀਂਦਾ ਹੈ:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ਨਤੀਜਾ

ਤੁਸੀਂ ਸਫਲਤਾਪੂਰਕ ਤਰੀਕੇ ਨਾਲ ਅਜ਼ੂਰ ਪੋਰਟਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਜ਼ੂਰ ਏਆਈ ਸਰਚ ਸੈੱਟઅਪ ਕਰ ਲਿਆ ਹੈ ਅਤੇ ਟੂਲਾਂ ਨੂੰ ਇਕੱਠਾ ਕਰ ਲਿਆ ਹੈ। ਹੁਣ ਤੁਸੀਂ ਅਜ਼ੂਰ ਏਆਈ ਸਰਚ ਦੀਆਂ ਅਗਲੀ ਖਾਸੀਅਤਾਂ ਅਤੇ ਸਮਰੱਥਾਵਾਂ ਦਾ ਪਤਾ ਲਗਾ ਕੇ ਆਪਣੇ ਸਰਚ ਹੱਲਾਂ ਨੂੰ ਵਧਾ ਸਕਦੇ ਹੋ।

ਵਧੇਰੇ ਸਹਾਇਤਾ ਲਈ, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) 'ਤੇ ਜਾਓ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->