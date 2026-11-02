# ਐਜ਼ੂਅਰ ਏਆਈ ਸੇਰਚ ਸੈਟਅੱਪ ਗਾਈਡ

ਇਹ ਗਾਈਡ ਤੁਹਾਨੂੰ ਐਜ਼ੂਅਰ ਪੋਰਟਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਜ਼ੂਅਰ ਏਆਈ ਸੇਰਚ ਸੈਟਅੱਪ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇਗੀ। ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਆਪਣੀ ਐਜ਼ੂਅਰ ਏਆਈ ਸੇਰਚ ਸੇਵਾ ਬਣਾਓ ਅਤੇ ਸੰਰਚਿਤ ਕਰੋ।

## ਤਿਆਰੀਆਂ

ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਇਹ ਹਨ:

- ਇੱਕ ਐਜ਼ੂਅਰ ਸਬਸਕ੍ਰਿਪਸ਼ਨ। ਜੇਕਰ ਤੁਹਾਡੇ ਕੋਲ ਐਜ਼ੂਅਰ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਨਹੀਂ ਹੈ, ਤਾਂ ਤੁਸੀਂ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) 'ਤੇ ਇੱਕ ਮੁਫ਼ਤ ਖਾਤਾ ਬਣਾ ਸਕਦੇ ਹੋ।

## ਕਦਮ 1: ਇੱਕ ਐਜ਼ੂਅਰ ਸਟੋਰੇਜ ਐਕਾਊਂਟ ਬਣਾਓ

1. ਇਸ ਦਿਸ਼ਾ-ਦਰਸ਼ਨ [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) ਦੀ ਪਾਲਣਾ ਕਰਦੇ ਹੋਏ ਇੱਕ ਨਵਾਂ ਐਜ਼ੂਅਰ ਸਟੋਰੇਜ ਐਕਾਊਂਟ ਬਣਾਓ।
   **ਨੋਟ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਸਟੋਰੇਜ ਐਕਾਊਂਟ ਦੀ ਕਿਸਮ Standard General Purpose V2 ਹੈ।

## ਕਦਮ 2: ਇੱਕ ਐਜ਼ੂਅਰ ਏਆਈ ਸੇਰਚ ਸੇਵਾ ਬਣਾਓ

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ।
2. ਬਾਏਂ-ਹੱਥ ਦੇ ਨੈਵੀਗੇਸ਼ਨ ਪੈਨ ਵਿੱਚ, **Create a resource** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
3. ਖੋਜ ਬਾਕਸ ਵਿੱਚ "Azure AI Search" ਲਿਖੋ ਅਤੇ ਨਤੀਜਿਆਂ ਦੀ ਸੂਚੀ ਵਿੱਚੋਂ **Azure AI Search** ਚੁਣੋ।
4. **Create** ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
5. **Basics** ਟੈਬ ਵਿੱਚ ਹੇਠ ਲਿਖੀ ਜਾਣਕਾਰੀ ਦਿਓ:
   - **Subscription**: ਆਪਣਾ ਐਜ਼ੂਅਰ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਚੁਣੋ।
   - **Resource group**: ਇੱਕ ਨਵਾਂ ਰਿਸੋਰਸ ਗਰੁੱਪ ਬਣਾਓ ਜਾਂ ਮੌਜੂਦਾ ਚੁਣੋ।
   - **Resource name**: ਆਪਣੀ ਸੇਰਚ ਸੇਵਾ ਲਈ ਇਕ ਵਿਲੱਖਣ ਨਾਮ ਦਿਓ।
   - **Region**: ਉਪਭੋਗਤਿਆਂ ਦੇ ਸਭ ਤੋਂ ਨੇੜੇ ਖੇਤਰ ਦੀ ਚੋਣ ਕਰੋ।
   - **Pricing tier**: ਆਪਣੀਆਂ ਲੋੜਾਂ ਦੇ ਮੁਤਾਬਕ ਇਕ ਪ੍ਰਾਈਸਿੰਗ ਟੀਅਰ ਚੁਣੋ। ਤੁਸੀਂ ਟੈਸਟਿੰਗ ਲਈ ਮੁਫ਼ਤ ਟੀਅਰ ਨਾਲ ਸ਼ੁਰੂ ਕਰ ਸਕਦੇ ਹੋ।
6. **Review + create** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
7. ਸੈਟਿੰਗਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ ਅਤੇ ਸੇਰਚ ਸੇਵਾ ਬਣਾਉਣ ਲਈ **Create** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।

## ਕਦਮ 3: ਐਜ਼ੂਅਰ ਏਆਈ ਸੇਰਚ ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰੋ

1. ਜਦੋਂ ਡਿਪਲੋਇਮੈਂਟ ਪੂਰਾ ਹੋ ਜਾਵੇ, ਐਜ਼ੂਅਰ ਪੋਰਟਲ ਵਿੱਚ ਆਪਣੇ ਸੇਰਚ ਸੇਵਾ 'ਤੇ ਜਾਇਏ।
2. ਸੇਰਚ ਸੇਵਾ ਦੀ ਓਵਰਵਿਊ ਪੈਨ ਵਿੱਚ URL ਨੂੰ ਕਾਪੀ ਕਰੋ। ਇਹ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਦੇਖਣ ਨੂੰ ਮਿਲਣਾ ਚਾਹੀਦਾ ਹੈ `https://<service-name>.search.windows.net`।
3. **(ਸੁਝਾਅ)** ਮਾਇਕ੍ਰੋਸੌਫਟ ਐਂਟਰਾ ID (RBAC) ਨਾਲ ਕੀਂ ਰਹਿਤ ਐਕਸੈਸ ਯੋਗ ਕਰੋ ਜਿਵੇਂ ਕਿ ਹੇਠਾਂ ਕਦਮ 4 ਵਿੱਚ ਦਿਖਾਇਆ ਗਿਆ ਹੈ — ਕਿਸੇ ਕੀ ਦੀ ਲੋੜ ਨਹੀਂ। ਇਸ ਗਾਈਡ ਵਿਚ ਨਮੂਨੇ ਇੰਡੈਕਸ ਬਣਾਉਂਦੇ/ਅੱਪਡੇਟ ਕਰਦੇ ਹਨ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਅੱਪਲੋਡ ਕਰਦੇ ਹਨ, ਜਿਸ ਲਈ **Search Service Contributor** ਅਤੇ **Search Index Data Contributor** ਭੂਮਿਕਾਵਾਂ ਦੀ ਲੋੜ ਹੈ (ਜਾਂ, ਕੀ ਅਧਾਰਿਤ ਪ੍ਰਮਾਣਿਕਤਾ ਲਈ, **primary admin key** — ਨਾ ਕਿ query key)। ਸਿਰਫ ਜੇ ਤੁਸੀਂ RBAC ਨਹੀਂ ਵਰਤ ਸਕਦੇ, ਤਾਂ **Settings > Keys** ਪੈਨ ਖੋਲ੍ਹੋ ਅਤੇ **primary admin key** ਕਾਪੀ ਕਰੋ।
4. ਇੱਕ ਇੰਡੈਕਸ ਬਣਾਉਣ, ਡਾਟਾ ਅਪਲੋਡ ਕਰਨ ਅਤੇ ਖੋਜ ਕਰਨ ਲਈ [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) ਸਫ਼ੇ ਵਿੱਚ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ।

## ਕਦਮ 4: ਐਜ਼ੂਅਰ ਏਆਈ ਸੇਰਚ ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰੋ

ਐਜ਼ੂਅਰ ਏਆਈ ਸੇਰਚ ਵੱਖ-ਵੱਖ ਟੂਲਜ਼ ਨਾਲ ਜੁੜਦਾ ਹੈ ਤਾਂ ਜੋ ਤੁਹਾਡੇ ਸੇਰਚ ਸਮਰੱਥਾ ਨੂੰ ਵਧਾਇਆ ਜਾ ਸਕੇ। ਤੁਸੀਂ ਉन्नਤ ਸੰਰਚਨਾਵਾਂ ਅਤੇ ਕਾਰਜਾਂ ਲਈ ਐਜ਼ੂਅਰ CLI, ਪਾਇਥਨ SDK, .NET SDK ਅਤੇ ਹੋਰ ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਦੇ ਹੋ।

### ਐਜ਼ੂਅਰ CLI ਦੀ ਵਰਤੋਂ ਕਰਨਾ

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) 'ਤੇ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਐਜ਼ੂਅਰ CLI ਇੰਸਟਾਲ ਕਰੋ।
2. ਕਮਾਂਡ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਜ਼ੂਅਰ CLI ਵਿੱਚ ਸਾਈਨ ਇਨ ਕਰੋ:

   ```bash
   az login
   ```
3. **(ਸੁਝਾਅ) ਮਾਇਕ੍ਰੋਸੌਫਟ ਐਂਟਰਾ ID (RBAC) ਨਾਲ ਕੀਂ ਰਹਿਤ ਐਕਸੈਸ ਯੋਗ ਕਰੋ:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC ਯੋਗ ਹੁੰਦੇ ਹੋਏ, ਹੇਠਾਂ ਦਿੱਤੇ ਪਾਇਥਨ ਅਤੇ .NET SDK ਨਮੂਨੇ `DefaultAzureCredential` ਨਾਲ ਪਰਮਾਣਿਤ ਕਰਦੇ ਹਨ, ਜੋ ਤੁਹਾਡੇ `az login` ਸੈਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹਨ ਸਥਾਨਕ ਵਿਕਾਸ ਦੌਰਾਨ — ਕਿਸੇ ਐਡਮਿਨ ਕੀ ਦੀ ਲੋੜ ਨਹੀਂ। ਵੇਖੋ [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)।

4. **(ਵਿਕਲਪ) ਕੀ ਅਧਾਰਿਤ ਪ੍ਰਮਾਣਿਕਤਾ** — ਸਿਰਫ ਜੇ ਤੁਸੀਂ RBAC ਵਰਤ ਨਹੀਂ ਸਕਦੇ, ਤਾਂ ਐਡਮਿਨ ਕੀ ਵੀ ਸਟੋਰ ਕਰੋ:

#### ਐਜ਼ੂਅਰ ਏਆਈ ਸੇਰਚ ਇੰਸਟੈਂਸ ਲਈ ਦੋਨੋਂ ਐੰਡਪੋਇੰਟ ਅਤੇ API ਕੀ ਨੂੰ ਵਾਤਾਵਰਣ ਚਲਾਂਵਾਂ ਵਿੱਚ ਸਟੋਰ ਕਰੋ।

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

### ਪਾਇਥਨ SDK ਦੀ ਵਰਤੋਂ ਕਰਨਾ

1. Azure Cognitive Search ਕਲਾਇੰਟ ਲਾਇਬ੍ਰੇਰੀ ਅਤੇ ਐਜ਼ੂਅਰ ਆਈਡੈਂਟੀਟੀ ਫਾਰ ਪਾਇਥਨ ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ਇੰਡੈਕਸ ਬਣਾਉਣ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਅਪਲੋਡ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤਾ ਪਾਇਥਨ ਕੋਡ ਵਰਤੋ:

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

### .NET SDK ਦੀ ਵਰਤੋਂ ਕਰਨਾ

1. ਇੰਡੈਕਸ ਬਣਾਉਣ ਅਤੇ ਦਸਤਾਵੇਜ਼ ਅਪਲੋਡ ਕਰਨ ਲਈ ਹੇਠਾਂ ਦਿੱਤੀ ਕਮਾਂਡ ਚਲਾਓ:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    ਹੇਠਾਂ ਦਿੱਤਾ .NET ਨਮੂਨਾ `DefaultAzureCredential` ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ, ਜੋ ਤੁਹਾਡੇ ਐਜ਼ੂਅਰ CLI ਸਾਈਨ-ਇਨ ਦਾ ਸਥਾਨਕ ਵਿਕਾਸ ਦੌਰਾਨ `az login` ਤੋਂ ਪ੍ਰਯੋਗ ਕਰ ਸਕਦਾ ਹੈ।

2. ਇਹ ਲਾਭਵੰਤ .NET ਕੋਡ ਹੈ `AzureSearch.cs` ਦਾ:

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

ਵਧੇਰੇ ਵਿਸਥਾਰਵਾਲੀ ਜਾਣਕਾਰੀ ਲਈ, ਹੇਠਾਂ ਦਿੱਤੀ ਦਸਤਾਵੇਜ਼ੀ ਸੰਦਰਭ ਬਾਰੇ ਵੇਖੋ:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ਨਤੀਜਾ

ਤੁਸੀਂ ਐਜ਼ੂਅਰ ਪੋਰਟਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਐਜ਼ੂਅਰ ਏਆਈ ਸੇਰਚ ਸਫਲਤਾਪੂਰਵਕ ਸੈਟਅੱਪ ਕਰ ਲਈ ਹੈ ਅਤੇ इੰਟিগ੍ਰੇਟ ਟੂਲਜ਼ ਨਾਲ ਜੋੜ ਲਈ ਹੈ। ਹੁਣ ਤੁਸੀਂ ਐਜ਼ੂਅਰ ਏਆਈ ਸੇਰਚ ਦੀਆਂ ਹੋਰ ਉੱਚ ਦਰਜੇ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਤੇ ਯੋਗਤਾਵਾਂ ਦੀ ਖੋਜ ਕਰ ਸਕਦੇ ਹੋ ਜਿਨ੍ਹਾਂ ਨਾਲ ਆਪਣੇ ਸੇਰਚ ਹੱਲਾਂ ਨੂੰ ਸੁਧਾਰਿਆ ਜਾ ਸਕਦਾ ਹੈ।

ਹੋਰ ਮਦਦ ਲਈ, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ਦੀ ਸੈਰ ਕਰੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->