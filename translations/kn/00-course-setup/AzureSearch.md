# ಆಜೂರ್ AI ಶೋಧನಾ ಸೆಟ್ಟಪ್ ಮಾರ್ಗದರ್ಶಿ

ಈ ಮಾರ್ಗದರ್ಶಿ ನಿಮಗೆ ಆಜೂರ್ ಪೋರ್ಟಲ್ ಬಳಸಿ ಆಜೂರ್ AI ಶೋಧನೆಯನ್ನು ಸೆಟ್‌ಅಪ್ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ. ನಿಮ್ಮ ಆಜೂರ್ AI ಶೋಧನಾ ಸೇವೆಯನ್ನು ರಚಿಸಿ ಮತ್ತು ಸಂರಚಿಸಲು ಕೆಳಗಿನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ.

## ಪೂರ್ವಶರತ್ತುಗಳು

ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು, ನೀವು ಕೆಳಗಿನವುಗಳನ್ನು ಹೊಂದಿರಬೇಕು ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:

- ಆಜೂರ್ ಸಬ್ಸ್ಕ್ರಿಪ್ಶನ್. ನಿಮ್ಮ ಬಳಿ ಆಜೂರ್ ಸಬ್ಸ್ಕ್ರಿಪ್ಶನ್ ಇಲ್ಲದಿದ್ದರೆ, [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ನಲ್ಲಿ ಉಚಿತ ಖಾತೆಯನ್ನು ರಚಿಸಬಹುದು.

## ಹಂತ 1: ಆಜೂರ್ ಸಂಗ್ರಹ ಖಾತೆ ರಚಿಸಿ

1. ಈ ಸೂಚನೆಯನ್ನು ಅನುಸರಿಸಿ, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) ನಿಮಗೆ ಆಜೂರ್ ಸಂಗ್ರಹ ಖಾತೆಯನ್ನು ರಚಿಸುವಲ್ಲಿ ಸಹಾಯ ಮಾಡುತ್ತದೆ.
   **ಗಮನಿಸಿ**: ಸ್ಟೋರೇಜ್	account ಪ್ರಕಾರ Standard General Purpose V2 ಇರಬೇಕು ಎಂಬುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

## ಹಂತ 2: ಆಜೂರ್ AI ಶೋಧನಾ ಸೇವೆ ರಚಿಸು

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) ನಲ್ಲಿ ಸೈನ್ ಇನ್ ಆಗಿ.
2. ಎಡಹಸ್ತ ನಾವಿಗೇಷನ್ ಪೇನಲ್‌ನಲ್ಲಿ **Create a resource** ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ಶೋಧನಾ ಬಾಕ್ಸ್‌ನಲ್ಲಿ "Azure AI Search" ಟೈಪ್ ಮಾಡಿ ಮತ್ತು ಫಲಿತಾಂಶಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **Azure AI Search** ಆಯ್ಕೆಮಾಡಿ.
4. **Create** ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ.
5. **Basics** ಟ್ಯಾಬ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಮಾಹಿತಿಗಳನ್ನು ಒದಗಿಸಿ:
   - **Subscription**: ನಿಮ್ಮ ಆಜೂರ್ ಸಬ್ಸ್ಕ್ರಿಪ್ಶನ್ ಆಯ್ಕೆಮಾಡಿ.
   - **Resource group**: ಹೊಸ resource group ರಚಿಸಿ ಅಥವಾ ಇನ್ನು ಮುಂದೆ ಯಾವುದಾದರೂ ಒಂದನ್ನು ಆಯ್ಕೆಮಾಡಿ.
   - **Resource name**: ನಿಮ್ಮ ಶೋಧನಾ ಸೇವೆಗೆ ಒಂದು ಅನನ್ಯ ಹೆಸರನ್ನು ನಮೂದಿಸಿ.
   - **Region**: ನಿಮ್ಮ ಬಳಕೆದಾರರಿಗೆ ಅತ್ಯಂತ ಸಮೀಪದ ಪ್ರದೇಶವನ್ನು ಆಯ್ಕೆಮಾಡಿ.
   - **Pricing tier**: ನಿಮ್ಮ ಅಗತ್ಯಗಳಿಗೆ ತಕ್ಕಂತೆ ಪ್ರೈಸಿಂಗ್ ಟಿಯರ್ ಆಯ್ಕೆಮಾಡಿ. ಪರೀಕ್ಷೆಗಾಗಿ ಫ್ರೀ ಟಿಯರ್ ನಿಂದ ಪ್ರಾರಂಭಿಸಬಹುದು.
6. **Review + create** ಕ್ಲಿಕ್ ಮಾಡಿ.
7. ಸೆಟ್ಟಿಂಗ್ಸ್ ಪರಿಶೀಲಿಸಿ ಮತ್ತು ಶೋಧನಾ ಸೇವೆಯನ್ನು ರಚಿಸಲು **Create** ಕ್ಲಿಕ್ ಮಾಡಿ.

## ಹಂತ 3: ಆಜೂರ್ AI ಶೋಧನೆಯೊಂದಿಗೆ ಪ್ರಾರಂಭಿಸಿ

1. ನಿಯೋಜನೆ ಸಂಪೂರ್ಣವಾದ ನಂತರ, ಆಜೂರ್ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಮ್ಮ ಶೋಧನಾ ಸೇವೆಗೆ ನಕ್ಷೇತ್ರಣ ಮಾಡಿರಿ.
2. ಶೋಧನಾ ಸೇವೆಯ ಅವಲೋಕನ ಪೇನಲ್‌ನಲ್ಲಿ URL ನಕಲಿಸಿ. ಇದು `https://<service-name>.search.windows.net` ಹಾಗಿರಬೇಕು.
3. **(ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ)** ಕೆಳಗಿನ ಹಂತ 4 ರಲ್ಲಿ Microsoft Entra ID (RBAC) ಮೂಲಕ ಕೀಲಿಗೆ egestasವಿಲ್ಲದ ಪ್ರವೇಶವನ್ನು ಸಕ್ರಿಯ ಮಾಡಿ — ಯಾವುದೇ ಕೀಲಿಯ ಅಗತ್ಯವಿಲ್ಲ. ಈ ಮಾರ್ಗದರ್ಶಿಯಲ್ಲಿನ ಉದಾಹರಣೆಗಳು ಇನ್ಡೆಕ್ಸುಗಳ ರಚನೆ/ನವೀಕರಣ ಮತ್ತು ದಾಖಲೆಗಳ ಅಪ್ಲೋಡ್ ಮಾಡುತ್ತವೆ, ಇದಕ್ಕೆ **Search Service Contributor** ಮತ್ತು **Search Index Data Contributor** ಪಾತ್ರಗಳು ಬೇಕಾಗಿವೆ (ಅಥವಾ, ಕೀ-ಆಧಾರಿತ ದೃಢೀಕರಣಕ್ಕೆ, **ಪ್ರಾಥಮಿಕ ಆಡಳಿತ ಕೀ** — ಪ್ರಶ್ನಾ ಕೀ ಅಲ್ಲ). ನೀವು RBAC ಬಳಸಬಹುದು ಇಲ್ಲದಿದ್ದರೆ ಮಾತ್ರ, **Settings > Keys** ಪೇನಲ್ ತೆರೆಯಿರಿ ಮತ್ತು **ಪ್ರಾಥಮಿಕ ಆಡಳಿತ ಕೀ** ನಕಲಿಸಿ.
4. ಇನ್ಡೆಕ್ಸು ರಚಿಸಲು, ಡೇಟಾವನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಲು ಮತ್ತು ಶೋಧನೆಯನ್ನು ನಿರ್ವಹಿಸಲು [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) ನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ.

## ಹಂತ 4: ಆಜೂರ್ AI ಶೋಧನಾ ಸಾಧನಗಳನ್ನು ಬಳಸಿಕೊಳ್ಳಿ

ಆಜೂರ್ AI ಶೋಧನೆ ವಿವಿಧ ಸಾಧನಗಳೊಂದಿಗೆ ಸಂಯೋಜಿತವಾಗಿದೆ ताकि ನಿಮ್ಮ ಶೋಧನಾ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಉತ್ತಮಗೊಳಿಸಬಹುದು. ಹೆಚ್ಚುವರಿ ಸಂರಚನೆಗಳು ಮತ್ತು ಕಾರ್ಯಾಚರಣೆಗಳಿಗೆ ನೀವು ಆಜೂರ್ CLI, ಪೈಥಾನ್ SDK, .ನೆಟ್ SDK ಮತ್ತು ಇತರೆ ಸಾಧನಗಳನ್ನು ಬಳಸಬಹುದು.

### ಆಜೂರ್ CLI ಬಳಕೆ

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) ನಲ್ಲಿ ನೀಡಿರುವ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ ಆಜೂರ್ CLI ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ.
2. ಕೆಳಗಿನ ಕಮಾಂಡ್ ಬಳಸಿ ಆಜೂರ್ CLI ಗೆ ಸೈನ್ ಇನ್ ಆಗಿ:

   ```bash
   az login
   ```
3. **(ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ) Microsoft Entra ID (RBAC) ಮೂಲಕ ಕೀಲಿಗೆ ಏನೂ ಅಗತ್ಯವಿಲ್ಲದ ಪ್ರವೇಶವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # ಅಝ್ ಶೋಧನೆ ಸೇವೆಯ ಪ್ರದರ್ಶನದಲ್ಲಿ "ಎಂಡ್ಪಾಯಿಂಟ್" ಕ್ಷೇತ್ರವಿಲ್ಲ; ಸೇವೆಯ ಹೆಸರಿನಿಂದ URL ಅನ್ನು ನಿರ್ಮಿಸಿ.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC ಸಕ್ರಿಯಗೊಳ್ಳುವ ಮೂಲಕ, ಕೆಳಗಿನ ಪೈಥಾನ್ ಮತ್ತು .ನೆಟ್ SDK ಉದಾಹರಣೆಗಳು `DefaultAzureCredential` ಬಳಸಿ ದೃಢೀಕರಣ ಮಾಡುತ್ತವೆ, ಇದು ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಯಲ್ಲಿ ನಿಮ್ಮ `az login` ಸೆಷನ್ ಅನ್ನು ಬಳಸುತ್ತದೆ — ಯಾವುದೇ ಆಡಳಿತ ಕೀ ಅಗತ್ಯವಿಲ್ಲ. [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) ನೋಡಿ.

4. **(ವಿಕಲ್ಪ) ಕೀ-ಆಧಾರಿತ ದೃಢೀಕರಣ** — ನೀವು RBAC ಬಳಸಲು ಸಾಧ್ಯವಿಲ್ಲದಿದ್ದರೆ ಮಾತ್ರ ಆಡಳಿತ ಕಿಯನ್ನು ಕೂಡ ಸಂಗ್ರಹಿಸಿ:

#### ಆಜೂರ್ AI ಶೋಧನಾ ಉದಾಹರಣೆಯ ಅಂತಿಮ ಬಿಂದುವಿನ ಮತ್ತು API ಕೀಲಿಯನ್ನು ಪರಿಸರ ಚರಗಳಲ್ಲಿ ಸಂಗ್ರಹಿಸಿ.

    ```bash
    # zsh/bash
    # az search service show ನಲ್ಲಿ "endpoint" ಕ್ಷೇತ್ರವಿಲ್ಲ; ಸೇವೆಯ ಹೆಸರಿನಿಂದ URL ರಚಿಸಿ.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show ನಲ್ಲಿ "endpoint" ಕ್ಷೇತ್ರವಿಲ್ಲ; ಸೇವೆಯ ಹೆಸರಿನಿಂದ URL ರಚಿಸಿ.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### ಪೈಥಾನ್ SDK ಬಳಕೆ

1. ಆಜೂರ್ ಕಾಗ್ನಿಟಿವ್ ಶೋಧನೆ ಕ್ಲೈಂಟ್ ಲೈಬ್ರರಿ ಮತ್ತು ಆಜೂರ್ ಐಡೆಂಟಿಟಿ ಪೈಥಾನ್‌ಗೆ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ಇನ್ಡೆಕ್ಸು ರಚಿಸಲು ಮತ್ತು ದಾಖಲೆಗಳನ್ನು ಅಪ್ಲೋಡ್ಗಳನ್ನು ಮಾಡಲು ಕೆಳಗಿನ ಪೈಥಾನ್ ಕೋಡ್ ಬಳಸಿ:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # ಕೀಲಿಯಿಲ್ಲದ (ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ): ನಿಮ್ಮ `az login` ಗುರುತನ್ನು Entra ID RBAC ಮೂಲಕ ಬಳಸುತ್ತದೆ.
    # "ಸರ್ಚ್ ಸರ್ವೀಸ್ ಕೊಂತ್ರಿಬ್ಯೂಟರ್" ಮತ್ತು "ಸರ್ಚ್ ಇಂಡೆಕ್ಸ್ ಡೇಟಾ ಕೊಂತ್ರಿಬ್ಯೂಟರ್" ಪಾತ್ರಗಳನ್ನು ಅಗತ್ಯವಿದೆ.
    credential = DefaultAzureCredential()
    # ಮತ್ತೆFallback (ಕೀ ಆಧಾರಿತ ಪ್ರಾಮಾಣೀಕರಣ):
    # azure.core.credentials ನಿಂದ AzureKeyCredential ಅನ್ನು ಆಮದುಮಾಡಿ
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

### .ನೆಟ್ SDK ಬಳಕೆ

1. ಕೆಳಗಿನ ಕಮಾಂಡ್ ರನ್ ಮಾಡಿ ಇನ್ಡೆಕ್ಸು ರಚಿಸಿ ಮತ್ತು ದಾಖಲೆಗಳನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಿ:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    ಕೆಳಗಿನ .ನೆಟ್ ಉದಾಹರಣೆ `DefaultAzureCredential` ಬಳಸುತ್ತದೆ, ಇದು ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಯಲ್ಲಿ `az login` ನಿಂದ ನಿಮ್ಮ ಆಜೂರ್ CLI ಸೈನ್-ಯಿಂದ ಬಳಸಬಹುದು.

2. ಇಲ್ಲಿ `AzureSearch.cs` ನ .ನೆಟ್ ಕೋಡ್ ಇದೆ:

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

ಹೆಚ್ಚಿನ ವಿವರಗಳಿಗೆ ಕೆಳಗಿನ ದಾಖಲೆಗಳನ್ನು ನೋಡಿ:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ಸಮಾರೋಪ

ನೀವು ಯಶಸ್ವಿಯಾಗಿ ಆಜೂರ್ ಪೋರ್ಟಲ್ ಮತ್ತು ಸಂಯೋಜಿತ ಸಾಧನಗಳ ಬಳಸಿ ಆಜೂರ್ AI ಶೋಧನೆಯನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿದ್ದೀರಿ. ಈಗ ನೀವು ಆಜೂರ್ AI ಶೋಧನೆಯ ಹೆಚ್ಚುವರಿ ವೈಶಿಷ್ಟ್ಯಗಳು ಮತ್ತು ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಅನ್ವೇಷಿಸಿ ನಿಮ್ಮ ಶೋಧನಾ ಪರಿಹಾರಗಳನ್ನು ಹೆಚ್ಚಿಸಬಹುದು.

ಹೆಚ್ಚಿನ ಸಹಾಯಕ್ಕಾಗಿ, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ಗೆ ಭೇಟಿ ನೀಡಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->