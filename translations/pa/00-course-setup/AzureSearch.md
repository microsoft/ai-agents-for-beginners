# ਅਜੂਰ ਏਆਈ ਸੇਰਚ ਸੈੱਟਅਪ ਗਾਇਡ

ਇਹ ਗਾਇਡ ਤੁਹਾਡੀ ਮਦਦ ਕਰੇਗੀ ਅਜੂਰ ਪੋਰਟਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਜੂਰ ਏਆਈ ਸੇਰਚ ਸੈੱਟਅਪ ਕਰਨ ਵਿੱਚ। ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦਾ ਪਾਲਣ ਕਰਕੇ ਆਪਣੀ ਅਜੂਰ ਏਆਈ ਸੇਰਚ ਸੇਵਾ ਬਣਾਓ ਅਤੇ ਸੰਰਚਿਤ ਕਰੋ।

## ਜਰੂਰੀਆਂ

ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਇਹ ਹਨ:

- ਇੱਕ ਅਜੂਰ ਸ਼੍ਰੇਣੀ। ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਅਜੂਰ ਸ਼੍ਰੇਣੀ ਨਹੀਂ ਹੈ, ਤਾਂ ਤੁਸੀਂ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 'ਤੇ ਇੱਕ ਮੁਫਤ ਖਾਤਾ ਬਣਾਉਂ ਸਕਦੇ ਹੋ।

## ਕਦਮ 1: ਇੱਕ ਅਜੂਰ ਸਟੋਰੇਜ ਖਾਤਾ ਬਣਾਓ

1. ਇਸ ਸੂਚਨਾ ਨੂੰ ਫਾਲੋ ਕਰੋ, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), ਇੱਕ ਨਵਾਂ ਅਜੂਰ ਸਟੋਰੇਜ ਖਾਤਾ ਬਣਾਉਣ ਲਈ।
   **ਨੋਟ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਟੋਰੇਜ ਅਕਾਊਂਟ ਦਾ ਕਿਸਮ Standard General Purpose V2 ਹੈ।

## ਕਦਮ 2: ਇੱਕ ਅਜੂਰ ਏਆਈ ਸੇਰਚ ਸੇਵਾ ਬਣਾਓ

1. [ਅਜੂਰ ਪੋਰਟਲ](https://portal.azure.com/?wt.mc_id=studentamb_258691) ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ।
2. ਖੱਬੇ ਹੱਥ ਦੇ ਨੈਵੀਗੇਸ਼ਨ ਪੇਨ ਵਿੱਚ, **Create a resource** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
3. ਖੋਜ ਬਕਸੇ ਵਿੱਚ, "Azure AI Search" ਟਾਈਪ ਕਰੋ ਅਤੇ ਨਤੀਜਿਆਂ ਦੀ ਸੂਚੀ ਵਿੱਚੋਂ **Azure AI Search** ਚੁਣੋ।
4. **Create** ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
5. **Basics** ਟੈਬ ਵਿੱਚ, ਹੇਠਾਂ ਦਿੱਤੀ ਜਾਣਕਾਰੀ ਦਿਓ:
   - **Subscription**: ਆਪਣੀ ਅਜੂਰ ਸ਼੍ਰੇਣੀ ਚੁਣੋ।
   - **Resource group**: ਨਵਾਂ ਰਿਸੋਰਸ ਗਰੁੱਪ ਬਣਾਓ ਜਾਂ ਮੌਜੂਦਾ ਚੁਣੋ।
   - **Resource name**: ਆਪਣੇ ਸੇਰਚ ਸੇਵਾ ਲਈ ਇੱਕ ਵਿਲੱਖਣ ਨਾਂ ਦਿਓ।
   - **Region**: ਉਹ ਖੇਤਰ ਚੁਣੋ ਜੋ ਤੁਹਾਡੇ ਉਪਭੋਗਤਾਵਾਂ ਦੇ ਨੇੜੇ ਹੋਵੇ।
   - **Pricing tier**: ਆਪਣੇ ਲੋੜਾਂ ਅਨੁਸਾਰ ਇੱਕ ਪ੍ਰਾਈਸਿੰਗ ਟੀਅਰ ਚੁਣੋ। ਤੁਸੀਂ ਟੈਸਟਿੰਗ ਲਈ ਮੁਫਤ ਟੀਅਰ ਤੋਂ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹੋ।
6. **Review + create** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
7. ਸੈਟਿੰਗਜ਼ ਨੂੰ ਸਮੀਖਿਆ ਕਰੋ ਅਤੇ ਸੇਰਚ ਸੇਵਾ ਬਣਾਉਣ ਲਈ **Create** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।

## ਕਦਮ 3: ਅਜੂਰ ਏਆਈ ਸੇਰਚ ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰੋ

1. ਜਦੋਂ ਤਿਆਰੀ ਮੁਕੰਮਲ ਹੋ ਜਾਵੇ, ਅਜੂਰ ਪੋਰਟਲ ਵਿੱਚ ਆਪਣੀ ਸੇਰਚ ਸੇਵਾ ਤੇ ਜਾਓ।
2. ਸੇਰਚ ਸੇਵਾ ਦੇ ਓਵਰਵਿਊ ਪੇਨ ਵਿੱਚ, URL ਨਕਲ ਕਰੋ। ਇਹ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ `https://<service-name>.search.windows.net`।
3. **(ਸਿਫਾਰਸ਼ ਕੀਤੀ)** Microsoft Entra ID (RBAC) ਨਾਲ ਕੀ-ਰਹਿਤ ਐਕਸੈਸ ਯੋਗ ਕਰੋ ਜਿਵੇਂ ਕਿ ਹੇਠਾਂ ਕਦਮ 4 ਵਿੱਚ ਦਿੱਤਾ ਗਿਆ ਹੈ — ਕੋਈ ਕੀ ਲੋੜ ਨਹੀਂ। ਇਸ ਗਾਇਡ ਵਿੱਚ ਨਮੂਨੇ ਇੰਡੈਕਸ ਬਣਾਉਂਦੇ/ਅਪਡੇਟ ਕਰਦੇ ਹਨ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਅਪਲੋਡ ਕਰਦੇ ਹਨ, ਜਿਹੜੇ **Search Service Contributor** ਅਤੇ **Search Index Data Contributor** ਭੂਮਿਕਾਵਾਂ (ਜਾਂ, ਕੀ ਅਧਾਰਿਤ ਪ੍ਰਮਾਣੀਕਰਨ ਲਈ, **ਪਰਾਈਮਰੀ ਐਡਮਿਨ ਕੀ** — ਨਾ ਕਿ ਕਵੈਰੀ ਕੀ) ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਜੇ ਤੁਸੀਂ RBAC ਵਰਤ ਨਹੀਂ ਸਕਦੇ, ਤਾਂ **Settings > Keys** ਪੈਨ ਖੋਲ੍ਹੋ ਅਤੇ **ਪਰਾਈਮਰੀ ਐਡਮਿਨ ਕੀ** ਨਕਲ ਕਰੋ।
4. ਇੰਡੈਕਸ ਬਣਾਉਣ, ਡੇਟਾ ਅਪਲੋਡ ਕਰਨ ਅਤੇ ਸੇਰਚ ਕਰਨ ਲਈ [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) ਵਿੱਚ ਦਿੱਤੇ ਕਦਮਾਂ ਦਾ ਪਾਲਣ ਕਰੋ।

## ਕਦਮ 4: ਅਜੂਰ ਏਆਈ ਸੇਰਚ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰੋ

ਅਜੂਰ ਏਆਈ ਸੇਰਚ ਵੱਖ-ਵੱਖ ਟੂਲਾਂ ਨਾਲਇੰਟਿਗਰੇਟ ਹੁੰਦਾ ਹੈ ਤਾਂ ਜੋ ਤੁਹਾਡੀ ਖੋਜ ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਬਹਿਤਰ बनाया ਜਾ ਸਕੇ। ਤੁਸੀਂ ਅਜੂਰ CLI, ਪਾਇਥਨ SDK, .NET SDK ਅਤੇ ਹੋਰ ਟੂਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਉੱਚ-ਪੱਧਰੀ ਸੰਰਚਨਾ ਅਤੇ ਕਾਰਜ ਕਰ ਸਕਦੇ ਹੋ।

### ਅਜੂਰ CLI ਦੀ ਵਰਤੋਂ ਕਰਨਾ

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 'ਤੇ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਅਨੁਸਾਰ ਅਜੂਰ CLI ਇੰਸਟਾਲ ਕਰੋ।
2. ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਨਾਲ ਅਜੂਰ CLI ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ:

   ```bash
   az login
   ```
3. **(ਸਿਫਾਰਸ਼ ਕੀਤੀ) Microsoft Entra ID (RBAC) ਨਾਲ ਕੀ-ਰਹਿਤ ਐਕਸੈਸ ਯੋਗ ਕਰੋ:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search ਸਰਵਿਸ ਦਿਖਾਉਂਦੀ ਹੈ ਕਿ "endpoint" ਫੀਲ্ড ਨਹੀਂ ਹੈ; URL ਨੂੰ ਸਰਵਿਸ ਨਾਮ ਤੋਂ ਬਣਾਓ।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC ਯੋਗ ਹੋਣ ਨਾਲ, ਹੇਠਾਂ ਦਿੱਤੇ ਪਾਇਥਨ ਅਤੇ .NET SDK ਨਮੂਨੇ `DefaultAzureCredential` ਨਾਲ ਪ੍ਰਮਾਣੀਕਰਨ ਕਰਦੇ ਹਨ, ਜੋ ਤੁਹਾਡੇ `az login` ਸੈਸ਼ਨ ਨੂੰ ਸਥਾਨਕ ਵਿਕਾਸ ਦੌਰਾਨ ਵਰਤਦਾ ਹੈ — ਕੋਈ ਐਡਮਿਨ ਕੀ ਲੋੜ ਨਹੀਂ। ਵੇਖੋ [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)।

4. **(ਬੈਕਅਪ) ਕੀ-ਅਧਾਰਿਤ ਪ੍ਰਮਾਣੀਕਰਨ** — ਸਿਰਫ ਜੇ ਤੁਸੀਂ RBAC ਵਰਤ ਨਹੀਂ ਸਕਦੇ, ਤਦ ਐਡਮਿਨ ਕੀ ਵੀ ਸਟੋਰ ਕਰੋ:

#### ਅਜੂਰ ਏਆਈ ਸੇਰਚ ਇੰਸਟੈਂਸ ਲਈ ਐਂਡਪੌਇੰਟ ਅਤੇ API ਕੀ ਦੋਹਾਂ ਨੂੰ ਮਾਹੌਲ ਚਲਕ ਪ੍ਰਵਰਤਾਵਾਂ ਵਿੱਚ ਸਟੋਰ ਕਰੋ।

    ```bash
    # zsh/bash
    # az search service show ਵਿੱਚ "endpoint" ਫੀਲਡ ਨਹੀਂ ਹੁੰਦੀ; ਸੇਵਾ ਨਾਂ ਤੋਂ URL ਬਣਾਓ।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show ਵਿੱਚ "endpoint" ਫੀਲਡ ਨਹੀਂ ਹੁੰਦੀ; ਸੇਵਾ ਨਾਂ ਤੋਂ URL ਬਣਾਓ।
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### ਪਾਇਥਨ SDK ਦੀ ਵਰਤੋਂ ਕਰਨਾ

1. ਅਜੂਰ ਕੋਗਨਿਟਿਵ ਸੇਰਚ ਕਲਾਇੰਟ ਲਾਇਬ੍ਰੇਰੀ ਅਤੇ ਅਜੂਰ ਆਈਡੈਂਟੀਟੀ ਲਈ ਪਾਇਥਨ ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ਇੱਕ ਇੰਡੈਕਸ ਬਣਾਉਣ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਅਪਲੋਡ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਪਾਇਥਨ ਕੋਡ ਵਰਤੋਂ:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # ਕੀਲੇਸ (ਸਿਫ਼ਾਰਸ਼ੀ): ਤੁਹਾਡੇ `az login` ਪਹਿਚਾਣ ਨੂੰ Entra ID RBAC ਰਾਹੀਂ ਵਰਤਦਾ ਹੈ।
    # "Search Service Contributor" ਅਤੇ "Search Index Data Contributor" ਭੂਮਿਕਾਵਾਂ ਦੀ ਲੋੜ ਹੈ।
    credential = DefaultAzureCredential()
    # ਫੋਲਬੈਕ (ਕੀ-ਆਧਾਰਿਤ ਪ੍ਰਮਾਣਿਕਤਾ):
    # azure.core.credentials ਤੋਂ AzureKeyCredential ਇੰਪੋਰਟ ਕਰੋ
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

### .NET SDK ਦੀ ਵਰਤੋਂ ਕਰਨਾ

1. ਇੱਕ ਇੰਡੈਕਸ ਬਣਾਉਣ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਅਪਲੋਡ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਕਮਾਂਡ ਚਲਾਓ:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    ਹੇਠਾਂ ਦਿੱਤਾ .NET ਨਮੂਨਾ `DefaultAzureCredential` ਵਰਤਦਾ ਹੈ, ਜੋ ਸਥਾਨਕ ਵਿਕਾਸ ਦੌਰਾਨ ਤੁਹਾਡੇ Azure CLI ਦੇ `az login` ਸਾਈਨ-ਇਨ ਨੂੰ ਵਰਤ ਸਕਦਾ ਹੈ।

2. ਇਹ ਹੈ `AzureSearch.cs` ਦਾ .NET ਕੋਡ:

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

ਹੋਰ ਵਿਸਥਾਰਤ ਜਾਣਕਾਰੀ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੀ ਦਸਤਾਵੇਜ਼ੀ ਸੂਚੀ ਵੇਖੋ:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ਨਿਸ਼ਕਰਸ਼

ਤੁਸੀਂ ਸਫਲਤਾਪੂਰਵਕ ਅਜੂਰ ਪੋਰਟਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਜੂਰ ਏਆਈ ਸੇਰਚ ਸੈੱਟਅਪ ਕਰ ਲਈ ਹੈ ਅਤੇ ਇੰਟਿਗਰੇਟ ਟੂਲਾਂ ਨਾਲ ਕੰਮ ਕਰ ਰਹੇ ਹੋ। ਹੁਣ ਤੁਸੀਂ ਅਜੂਰ ਏਆਈ ਸੇਰਚ ਦੇ ਵਧੇਰੇ ਉੱਚ ਪੱਧਰੀ ਫੀਚਰਾਂ ਅਤੇ ਸਮਰੱਥਾਵਾਂ ਦਾ ਪਤਾ ਲਾ ਸਕਦੇ ਹੋ ਤਾਂ ਜੋ ਆਪਣੇ ਸੇਰਚ ਹੱਲਾਂ ਨੂੰ ਬਹਿਤਰ ਬਣਾਇਆ ਜਾ ਸਕੇ।

ਹੋਰ ਮਦਦ ਲਈ, [ਅਜੂਰ ਕੋਗਨਿਟਿਵ ਸੇਰਚ ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ਵੇਖੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->