# ಅಜೂರ್ AI ಹುಡುಕಾಟ ಸೆಟ್ ಅಪ್ ಮಾರ್ಗದರ್ಶಿ

ಈ ಮಾರ್ಗದರ್ಶಿ ಅದೃಶ್ಯ ಪೋರ್ಟಲ್ ಬಳಸಿ ಅಜೂರ್ AI ಹುಡುಕಾಟವನ್ನು ವ್ಯವಸ್ಥೆಗೊಳಿಸುವಲ್ಲಿ ನಿಮಗೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ. ಅಜೂರ್ AI ಹುಡುಕಾಟ ಸೇವೆಯನ್ನು ಸೃಷ್ಟಿಸುವಾಗ ಮತ್ತು ಸಂರಚಿಸುವಾಗ ಕೆಳಗಿನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ.

## ಪೂರ್ವಾಪೇಕ್ಷೆಗಳು

ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು, ನಿಮಗಾಗಿ ಕೆಳಗಿನವುಗಳು ಇದ್ದಾರೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:

- ಅಜೂರ್ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್. ನಿಮಗೆ ಅಜೂರ್ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್ ಇಲ್ಲದಿದ್ದರೆ, [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ನಲ್ಲಿ ಉಚಿತ ಖಾತೆಯನ್ನು ರಚಿಸಬಹುದು.

## ಹಂತ 1: ಅಜೂರ್ ಸ್ಟೋರೇಜ್ ಖಾತೆಯನ್ನು ರಚಿಸಿ

1. ಈ ಸೂಚನೆಯನ್ನು ಅನುಸರಿಸಿ, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), ಹೊಸ ಅಜೂರ್ ಸ್ಟೋರೇಜ್ ಖಾತೆಯನ್ನು ರಚಿಸಲು.
   **ಗುರುತು**: ಸ್ಟೋರೇಜ್ ಖಾತೆಯ ಪ್ರಕಾರ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಜನರಲ್ ಪರ್ಪಸ್ V2 ಆಗಿರುವುದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

## ಹಂತ 2: ಅಜೂರ್ AI ಹುಡುಕಾಟ ಸೇವೆಯನ್ನು ರಚಿಸಿ

1. [ಆಜೂರ್ ಪೋರ್ಟಲ್](https://portal.azure.com/?wt.mc_id=studentamb_258691) ನಲ್ಲಿ ಲಾಗಿನ್ ಮಾಡಿ.
2. ಎಡಹಸ್ತ ನ್ಯಾವಿಗೇಶನ್ ಪ್ಯಾನೆಲ್ನಲ್ಲಿ **Create a resource** ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ಹುಡುಕಾಟ ಬಾಕ್ಸಿನಲ್ಲಿ "Azure AI Search" ಎಂದು ಟೈಪ್ ಮಾಡಿ ಮತ್ತು ಫಲಿತಾಂಶಗಳಲ್ಲಿ **Azure AI Search** ಆಯ್ಕೆಮಾಡಿ.
4. **Create** ಬಟನ್ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ.
5. **Basics** ಟ್ಯಾಬ್ನಲ್ಲಿ ಕೆಳಗಿನ ಮಾಹಿತಿಗಳನ್ನು ಒದಗಿಸಿ:
   - **Subscription**: ನಿಮ್ಮ ಅಜೂರ್ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್ ಆಯ್ಕೆಮಾಡಿ.
   - **Resource group**: ಹೊಸ ರಿಸೋರ್ಸ್ ಗುಂಪನ್ನು ರಚಿಸಿ ಅಥವಾ ಇತ್ತೀಚೆಗೆ ಇರುವುದನ್ನು ಆರಿಸಿ.
   - **Resource name**: ನಿಮ್ಮ ಹುಡುಕಾಟ ಸೇವೆಗೆ ವಿಶಿಷ್ಟ ಹೆಸರು ನಮೂದಿಸಿ.
   - **Region**: ನಿಮ್ಮ ಬಳಕೆದಾರರಿಗೆ 가장 ಸಮೀಪದ ಪ್ರದೇಶವನ್ನು ಆಯ್ಕೆಮಾಡಿ.
   - **Pricing tier**: ನಿಮ್ಮ ಅಗತ್ಯಗಳಿಗಾಗಿ ಸೂಕ್ತವಾದ ಬೆಲೆಮಾಪನ ತಗುಲಿಸಿಕೊಳ್ಳಿ. ಪರೀಕ್ಷಿಗಾಗಿ ಉಚಿತ ತಗಲುವಿಕೆಯನ್ನು ಪ್ರಾರಂಭಿಸಬಹುದು.
6. **Review + create** ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿ.
7. ಸಂಯೋಜನೆಯನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ಹುಡುಕಾಟ ಸೇವೆಯನ್ನು ರಚಿಸಲು **Create** ಕ್ಲಿಕ್ ಮಾಡಿ.

## ಹಂತ 3: ಅಜೂರ್ AI ಹುಡುಕಾಟವನ್ನು ಶುರುಮಾಡಿ

1. ನಿಯೋಜನೆ ಪೂರ್ಣವಾದ ಮೇಲೆ, ಅಜೂರ್ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಮ್ಮ ಹುಡುಕಾಟ ಸೇವೆ ಕಡೆಗೆ ನ್ಯಾವಿಗೇಟ್ ಮಾಡಿ.
2. ಹುಡುಕಾಟ ಸೇವೆ ಅವಲೋಕನ ಪ್ಯಾನ್ನಲ್ಲಿ URL ನಕಲಿಸಿ. ಇದು `https://<service-name>.search.windows.net` ಹಾಗಿರಬೇಕು.
3. **(ಶಿಫಾರಸು)** ಮೈಕ್ರೋಸಾಫ್ಟ್ ಎಂಟ್ರಾ ಐಡಿ (RBAC) ಮೂಲಕ ಕೀಲಿಯಿಲ್ಲದ ಪ್ರವೇಶವನ್ನು ಹಿಗ್ಗಿಸಿ — ಯಾವುದೇ ಕೀಲಿಯ ಅವಶ್ಯಕತೆ ಇರುವುದಿಲ್ಲ. ಈ ಮಾರ್ಗದರ್ಶಿಯಲ್ಲಿನ ಮಾದರಿಗಳು ಸೂಚ್ಯಂಕಗಳನ್ನು ಸೃಷ್ಟಿಸುವುದು/ನವೀಕರಿಸುವುದು ಮತ್ತು ಡಾಕ್ಯುಮೆಂಟ್ಗಳನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡುತ್ತವೆ, ಇವುಗಳಿಗೆ **Search Service Contributor** ಮತ್ತು **Search Index Data Contributor** ಪಾತ್ರಗಳು ಬೇಕು (ಅಥವಾ ಕೀ-ಆಧಾರಿತ ಪ್ರಮಾಣೀಕರಣಕ್ಕಾಗಿ, **ಪ್ರಾಥಮಿಕ ಆಡಳಿತ ಕೀ** — ಕ್ವೆರೀ ಕೀ ಅಲ್ಲ). ನೀವು RBAC ಬಳಸಲಾಗದಿದ್ದರೆ ಮಾತ್ರ **Settings > Keys** ಪರದೆ ತೆರೆದು **ಪ್ರಾಥಮಿಕ ಆಡಳಿತ ಕೀ** ನಕಲಿಸಿ.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) ಪುಟದಲ್ಲಿನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ, ಸೂಚ್ಯಂಕ ಸೃಷ್ಟಿಸಿ, ಡೇಟಾವನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಿ ಮತ್ತು ಹುಡುಕಾಟ ಮಾಡಿ.

## ಹಂತ 4: ಅಜೂರ್ AI ಹುಡುಕಾಟ ಉಪಕರಣಗಳನ್ನು ಬಳಸಿ

ಅಜೂರ್ AI ಹುಡುಕಾಟ ವಿವಿಧ ಉಪಕರಣಗಳೊಂದಿಗೆ ಸಮನ್ವಯಗೊಳ್ಳುತ್ತದೆ ನಿಮ್ಮ ಹುಡುಕಾಟ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಸುಧಾರಿಸಲು. ನೀವು ಅಜೂರ್ CLI, ಪೈಥಾನ್ SDK, .ನெட் SDK ಮತ್ತು ಇತರೆ ಉಪಕರಣಗಳನ್ನು ಸುಧಾರಿತ ಸಂರಚನೆಗಳು ಮತ್ತು ಕಾರ್ಯಾಚರಣೆಗಳಿಗಾಗಿ ಬಳಸಿ.

### ಅಜೂರ್ CLI ಬಳಸಿ

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) ಯಲ್ಲಿ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ ಅಜೂರ್ CLI ಅನ್ನು ಇನ್ಸ್ಟಾಲ್ ಮಾಡಿ.
2. ಕೆಳಗಿನ ಕಮಾಂಡ್ ಬಳಸಿ ಅಜೂರ್ CLI ಯಲ್ಲಿ ಸೈನ್ ಇನ್ ಮಾಡಿ:

   ```bash
   az login
   ```
3. **(ಶಿಫಾರಸು) ಮೈಕ್ರೋಸಾಫ್ಟ್ ಎಂಟ್ರಾ ಐಡಿ (RBAC) ಮೂಲಕ ಕೀಲಿಯಿಲ್ಲದ ಪ್ರವೇಶವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC ಸಕ್ರಿಯಗೊಂಡಾಗ, ಕೆಳಗಿನ ಪೈಥಾನ್ ಮತ್ತು .ನೆಟ್ SDK ಮಾದರಿಗಳು `DefaultAzureCredential` ಮೂಲಕ ಪ್ರಮಾಣೀಕರಿಸುತ್ತವೆ, ಇದು ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಯಲ್ಲಿ ನಿಮ್ಮ `az login` ಸೆಷನ್ ಬಳಸುತ್ತದೆ — ಯಾವುದೇ ಆಡಳಿತ ಕೀಲಿಯ ಅಗತ್ಯವಿಲ್ಲ. [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) ನೋಡಿ.

4. **(ಬದಲಿ) ಕೀ-ಆಧಾರಿತ ಪ್ರಮಾಣೀಕರಣ** — RBAC ಬಳಸದಿದ್ದರೆ, ಆಡಳಿತ ಕೀಲಿಯನ್ನು ಕೂಡ ಸಂಗ್ರಹಿಸಿ:

#### ಅಜೂರ್ AI ಹುಡುಕಾಟ ಉದಾಹರಣೆಗಾಗಿ ಎಂಡ್ಪಾಯಿಂಟ್ ಮತ್ತು API ಕೀಲಿಯನ್ನು ಪರಿಸರ ಬದಲಾವಣೆಗಳಾಗಿ ಸಂಗ್ರಹಿಸಿ.

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

### ಪೈಥಾನ್ SDK ಬಳಸಿ

1. ಅಜೂರ್ ಕಾಗ್ನಿಟಿವ್ ಹುಡುಕಾಟ ಕ್ಲೈಂಟ್ ಲೈಬ್ರರಿ ಮತ್ತು ಅಜೂರ್ ಐಡೆಂಟಿಟಿ ಪೈಥಾನ್ ಪ್ಯಾಕೇಜುಗಳನ್ನು ಇನ್ಸ್ಟಾಲ್ ಮಾಡಿ:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ಸೂಚ್ಯಂಕವನ್ನು ಸೃಷ್ಟಿಸಿ ಮತ್ತು ಡಾಕ್ಯುಮೆಂಟ್ಗಳನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಲು ಕೆಳಗಿನ ಪೈಥಾನ್ ಕೋಡ್ ಉಪಯೋಗಿಸಿ:

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

### .ನೆಟ್ SDK ಬಳಸಿ

1. ಸೂಚ್ಯಂಕ ಸೃಷ್ಟಿಸಲು ಮತ್ತು ಡಾಕ್ಯುಮೆಂಟ್ಗಳನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಲು ಕೆಳಗಿನ ಕಮಾಂಡ್ ಅನ್ನು ಚಲಾಯಿಸಿ:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    ಕೆಳಗಿನ .ನೆಟ್ ಮಾದರಿ `DefaultAzureCredential` ಬಳಸುತ್ತದೆ, ಇದು ನಿಮ್ಮ ಅಜೂರ್ CLI ಸೈನ್ ಇನ್ ಅನ್ನು ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಯಲ್ಲಿ `az login` ನಿಂದ ಬಳಸಬಹುದು.

2. ಇದು `AzureSearch.cs` ನ .ನೆಟ್ ಕೋಡ್:

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

ಹೆಚ್ಚಿನ ವಿವರಗಳಿಗೆ, ಕೆಳಗಿನ ಡಾಕ್ಯುಮೆಂಟೇಶನ್‌ಗೆ ಸಂಬಂದಿಸಿ:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ಸಾರಾಂಶ

ನೀವು ಅಜೂರ್ ಪೋರ್ಟಲ್ ಬಳಸಿ ಅಜೂರ್ AI ಹುಡುಕಾಟವನ್ನು ಯಶಸ್ವಿಯಾಗಿ ಸ್ಥಾಪಿಸಿ, ಮತ್ತು ಇಂಟಿಗ್ರೇಟೆಡ್ ಉಪಕರಣಗಳನ್ನು ಬಳಸಿ. ಈಗ ನೀವು ಅಜೂರ್ AI ಹುಡುಕಾಟದ ಹೆಚ್ಚಿನ ಸುಧಾರಿತ ವೈಶಿಷ್ಟ್ಯಗಳು ಮತ್ತು ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಅನ್ವೇಷಿಸಬಹುದು ನಿಮ್ಮ ಹುಡುಕಾಟ ಪರಿಹಾರಗಳನ್ನು ಇನ್ನೂ ಬೆಸುಗೆಮಾಡಲು.

ಹೆಚ್ಚಿನ ಸಹಾಯಕ್ಕಾಗಿ, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ಭೇಟಿ ನೀಡಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->