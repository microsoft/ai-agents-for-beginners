# Azure AI Search ಸ್ಥಾಪನೆ ಮಾರ್ಗದರ್ಶಿ

ಈ ಮಾರ್ಗದರ್ಶಿ ನಿಮಗೆ Azure ಪೋರ್ಟಲ್ ಬಳಸಿ Azure AI Search ಅನ್ನು ಸ್ಥಾಪಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ. ನಿಮ್ಮ Azure AI Search ಸೇವೆಯನ್ನು ರಚಿಸಲು ಮತ್ತು ಸಂರಚಿಸಲು ಕೆಳಗಿನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ.

## ಅಗತ್ಯಗಳನ್ನು ಪೂರೈಸುವುದು

ಪ್ರಾರಂಭಿಸುವ ಮುಂಚೆ, ಕೆಳಗಿನವುಗಳನ್ನು ಹೊಂದಿರುವುದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:

- ಒಂದು Azure ಚಂದಾದಾರಿಕೆ. ನೀವು Azure ಚಂದಾದಾರಿಕೆ ಇಲ್ಲದಿದ್ದರೆ, ನೀವು [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ನಲ್ಲಿ ಉಚಿತ ಖಾತೆಯನ್ನು ರಚಿಸಬಹುದು.

## ಹಂತ 1: ಒಂದು Azure ಸಂಗ್ರಹಣೆ ಖಾತೆಯನ್ನು ರಚಿಸಿ

1. ಈ ಸೂಚನೆಯನ್ನು ಅನುಸರಿಸಿ, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) ಒಂದು ಹೊಸ Azure ಸಂಗ್ರಹಣೆ ಖಾತೆಯನ್ನು ರಚಿಸಲು.
   **గమనిక**: Storage Account ಪ್ರಕಾರವು Standard General Purpose V2 ಆಗಿರಬೇಕು ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

## ಹಂತ 2: ಒಂದು Azure AI Search ಸೇವೆಯನ್ನು ರಚಿಸಿ

1. [Azure ಪೋರ್ಟಲ್](https://portal.azure.com/?wt.mc_id=studentamb_258691) ಗೆ ಲಾಗಿನ್ ಆಗಿ.
2. ಎಡ ಬದಿಯ ನಾವಿಗೇಷನ್ ಪೇನಿನಲ್ಲಿ, **Create a resource** ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ಶೋಧೆ ಬಾಕ್ಸಿನಲ್ಲಿ "Azure AI Search" ಟೈಪ್ ಮಾಡಿ ಮತ್ತು ಫಲಿತಾಂಶಗಳ ಪಟ್ಟಿಯಿಂದ **Azure AI Search** ಆಯ್ಕೆಮಾಡಿ.
4. **Create** ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ.
5. **Basics** ಟ್ಯಾಬ್‌ನಲ್ಲಿ ಕೆಳಗಿನ ಮಾಹಿತಿಯನ್ನು ನೀಡಿ:
   - **Subscription**: ನಿಮ್ಮ Azure ಚಂದಾದಾರಿಕೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.
   - **Resource group**: ಹೊಸ ಸಂಪನ್ಮೂಲ ಗುಂಪನ್ನು ರಚಿಸಿ ಅಥವಾ ಇದಕ್ಕೆ ನುಡಿದ ಒಂದನ್ನು ಆಯ್ಕೆಮಾಡಿ.
   - **Resource name**: ನಿಮ್ಮ ಹುಡುಕಾಟ ಸೇವೆಗೆ ವಿಶಿಷ್ಟ ಹೆಸರನ್ನು ನಮೂದಿಸಿ.
   - **Region**: ನಿಮ್ಮ ಬಳಕೆದಾರರಿಗೆ ಸಮೀಪ ಇರುವ ಪ್ರದೇಶವನ್ನು ಆಯ್ಕೆಮಾಡಿ.
   - **Pricing tier**: ನಿಮ್ಮ ಅಗತ್ಯಗಳಿಗೆ ತಕ್ಕ मूल्य ಮಟ್ಟವನ್ನು ಆಯ್ಕೆಮಾಡಿ. ಪರೀಕ್ಷಣೆಗೆ ಉಚಿತ ಮಟ್ಟದಿಂದ ಪ್ರಾರಂಭಿಸಬಹುದು.
6. **Review + create** ಕ್ಲಿಕ್ ಮಾಡಿ.
7. ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ಹಿನ್ನೆಲನಕ್ಕಾಗಿ **Create** ಕ್ಲಿಕ್ ಮಾಡಿ.

## ಹಂತ 3: Azure AI Search ನೊಂದಿಗೆ ಪ್ರಾರಂಭಿಸಿ

1. ನಿಯೋಜನೆ ಪೂರ್ಣಗೊಂಡ ನಂತರ, Azure ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಮ್ಮ ಹುಡುಕಾಟ ಸೇವೆಗೆ ನಾವಿಗೇಟ್ ಮಾಡಿ.
2. ಹುಡುಕಾಟ ಸೇವೆಯ ಅವಲೋಕನ ಪೇನಿನಲ್ಲಿ URL ನಕಲಿಸಿ. ಅದು `https://<service-name>.search.windows.net` ಹಾಗಿರಬೇಕು.
3. **(ಶಿಫಾರಸು):** ಕೆಳಗಿನ ಹಂತ 4 ರಂತೆ Microsoft Entra ID (RBAC) ಬಳಸಿ ಕೀ ಇಲ್ಲದ ಪ್ರವೇಶವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ — ಯಾವುದೇ ಕೀ ಅಗತ್ಯವಿಲ್ಲ. ಈ ಮಾರ್ಗದರ್ಶಿಯ ಉದಾಹರಣೆಗಳು ಸೂಚ್ಯಂಕಗಳನ್ನು ರಚಿಸಲು/ನವೀಕರಿಸಲು ಮತ್ತು ದಾಖಲಾತಿಗಳನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಲು, **Search Service Contributor** ಮತ್ತು **Search Index Data Contributor** ಪಾತ್ರಗಳನ್ನು (ಅಥವಾ ಕೀ ಆಧಾರಿತ ಪ್ರಮಾಣೀಕರಣಕ್ಕೆ, **primary admin key** —=query ಕೀ ಅಲ್ಲ) ಅಗತ್ಯವಿದೆ. ನೀವು RBAC ಬಳಸಲು ಸಾಧ್ಯವಿಲ್ಲವಾದರೆ ಮಾತ್ರ **Settings > Keys** ಪೇನನ್ನು ತೆರೆಯಿರಿ ಮತ್ತು **primary admin key** ನಕಲಿಸಿ.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) ಪುಟದಲ್ಲಿ ಸೂಚಿಸಿದ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ ಸೂಚ್ಯಂಕವನ್ನು ರಚಿಸಿ, ಡೇಟಾವನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಿ ಮತ್ತು ಹುಡುಕಾಟವನ್ನು ನಿರ್ವಹಿಸಿ.

## ಹಂತ 4: Azure AI Search ಸಾಧನಗಳನ್ನು ಬಳಸುವುದು

Azure AI Search ವಿವಿಧ ಸಾಧನಗಳೊಂದಿಗೆ ಒಳಗೊಂಡಿದೆ ನಿಮ್ಮ ಹುಡುಕಾಟ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಹೆಚ್ಚಿಸಲು. ನೀವು ಕೌಶಲ್ಯರೂಪಿ ಸಂರಚನೆ ಮತ್ತು ಕಾರ್ಯಾಚರಣೆಯುಗಳಿಗೆ Azure CLI, Python SDK, .NET SDK ಮತ್ತು ಇತರ ಸಾಧನಗಳನ್ನು ಬಳಸಬಹುದು.

### Azure CLI ಬಳಸಿ

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) ನಲ್ಲಿ ನೀಡಿರುವ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ Azure CLI ಅನ್ನು ಸ್ಥಾಪಿಸಿ.
2. ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಬಳಸಿ Azure CLI ಗೆ ಸೈನ್ ಇನ್ ಆಗಿ:

   ```bash
   az login
   ```
3. **(ಶಿಫಾರಸು) Microsoft Entra ID (RBAC) ಬಳಸಿ ಕೀ ಇಲ್ಲದ ಪ್ರವೇಶವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search ಸೇವೆಯ ಪ್ರದರ್ಶನದಲ್ಲಿ "endpoint" ಫೀಲ್ಡ್ ಇಲ್ಲ; ಸೇವೆ ಹೆಸರುದಿಂದ URL ಅನ್ನು ರಚಿಸಿ.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC ಸಕ್ರಿಯಗೊಳಿಸಿದಾಗ, ಕೆಳಗಿನ Python ಮತ್ತು .NET SDK ಉದಾಹರಣೆಗಳು `DefaultAzureCredential` ನೊಂದಿಗೆ ಪ್ರಾಮಾಣೀಕರಿಸುತ್ತವೆ, ಇದು ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಯಲ್ಲಿರುವ ನಿಮ್ಮ `az login` ಅಧಿವೇಶನವನ್ನು ಬಳಸುತ್ತದೆ — ಯಾವುದೇ ಆಡ್ಮಿನ್ ಕೀ ಅಗತ್ಯವಿಲ್ಲ. ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗೆ [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) ನೋಡಿ.

4. **(ಬದಲಿ) ಕೀ ಆಧಾರಿತ ಪ್ರಮಾಣೀಕರಣ** — ನೀವು RBAC ಬಳಸಲು ಸಾಧ್ಯವಾಗದಿದ್ದರೆ ಮಾತ್ರ, ಆಡ್ಮಿನ್ ಕೀಯನ್ನು ಹೀಗೂ ಸಂಗ್ರಹಿಸಿ:

#### Azure AI Search ಘಟಕದ ಅಂತಿಮ ಬಿಂದು ಮತ್ತು API ಕಿಯನ್ನು ಪರಿಸರ ಚರಗಳಿಗೆ ಸಂಗ್ರಹಿಸಿ.

    ```bash
    # zsh/bash
    # az search service show ಗೆ "endpoint" ಕ್ಷೇತ್ರವಿಲ್ಲ; ಸೇವೆ ಪಟ್ಟಿಯಿಂದ URL ಅನ್ನು ನಿರ್ಮಿಸಿ.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show ಗೆ "endpoint" ಕ್ಷೇತ್ರವಿಲ್ಲ; ಸೇವೆ ಪಟ್ಟಿಯಿಂದ URL ಅನ್ನು ನಿರ್ಮಿಸಿ.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK ಬಳಸಿ

1. Azure Cognitive Search ಕ್ಲೈಂಟ್ ಗ್ರಂಥಾಲಯ ಮತ್ತು Python ನಲ್ಲಿ Azure Identity ಅನ್ನು ಸ್ಥಾಪಿಸಿ:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ಸೂಚ್ಯಂಕವನ್ನು ರಚಿಸಲು ಮತ್ತು ದಾಖಲಾತಿಗಳನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಲು ಕೆಳಗಿನ Python ಕೋಡ್ ಬಳಸಿ:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # ಕೀ ರಹಿತ (ಸೂಚಿಸಲ್ಪಟ್ಟದ್ದು): ನಿಮ್ಮ `az login` ಅಸೆಂಟ್ರಾ ID RBAC ಮೂಲಕ ಬಳಕೆ ಮಾಡುತ್ತದೆ.
    # "ಸರ್ಚ್ ಸರ್ವೀಸ್ ಕೊನ್ರಿಬ್ಯೂಟರ್" ಮತ್ತು "ಸರ್ಚ್ ಇಂಡೆಕ್ಸ್ ಡೇಟಾ ಕೊನ್ರಿಬ್ಯೂಟರ್" ಪಾತ್ರಗಳನ್ನು ಅಗತ್ಯವಿದೆ.
    credential = DefaultAzureCredential()
    # ಬ್ಯಾಕ್‌ಅಪ್ (ಕೀ ಆಧಾರಿತ ಪ್ರಮಾಣೀಕರಣ):
    # azure.core.credentials ನಿಂದ AzureKeyCredential ಅನ್ನು ಆಮದು ಮಾಡಿ
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

### .NET SDK ಬಳಸಿ

1. ಸೂಚ್ಯಂಕವನ್ನು ರಚಿಸಲು ಮತ್ತು ದಾಖಲೆಗಳನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಲು ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ರನ್ ಮಾಡಿ:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    ಕೆಳಗಿನ .NET ಉದಾಹರಣೆ `DefaultAzureCredential` ಬಳಸುತ್ತದೆ, ಇದು ಸ್ಥಳೀಯ ಅಭಿವೃದ್ಧಿಯಲ್ಲಿರುವ ನಿಮ್ಮ `az login` ಮೂಲಕ Azure CLI ಸೈನ್ ಇನ್ ಅನ್ನು ಬಳಸಬಹುದು.

2. ಕೆಳಗಿನಂತಿದ್ದು `AzureSearch.cs` ನ .NET ಕೋಡ್:

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

ಹೆಚ್ಚಿನ ವಿವರವಾದ ಮಾಹಿತಿಗೆ ಕೆಳಗಿನ ಡಾಕ್ಯುಮೆಂಟೇಷನ್ ನೋಡಿ:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ಉಪಸಂಪುಟ

ನೀವು ಯಶಸ್ವಿಯಾಗಿ Azure ಪೋರ್ಟಲ್ ಮತ್ತು ಸಂಯೋಜಿತ ಸಾಧನಗಳನ್ನು ಬಳಸಿ Azure AI Search ಅನ್ನು ಸ್ಥಾಪಿಸಿದ್ದಾರೆ. ಈಗ ನೀವು ಹೆಚ್ಚು ಕೌಶಲ್ಯಗಳು ಮತ್ತು ಸಾಮರ್ಥ್ಯಗಳನ್ನ while explore ಮಾಡಬಹುದು Azure AI Search ನಿಮ್ಮ ಹುಡುಕಾಟ ಪರಿಹಾರಗಳನ್ನು ಚೆನ್ನಾಗಿಸಬಹುದಾಗಿದೆ.

ಹೆಚ್ಚಿನ ಸಹಾಯಕ್ಕೆ, [Azure Cognitive Search ಡಾಕ್ಯುಮೆಂಟೇಷನ್](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ಭೇಟಿ ನೀಡಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಡ್ಡೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->