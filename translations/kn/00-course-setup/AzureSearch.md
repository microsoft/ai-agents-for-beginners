<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-12-03T17:29:44+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "kn"
}
-->
# Azure AI Search ಸೆಟಪ್ ಮಾರ್ಗದರ್ಶಿ

ಈ ಮಾರ್ಗದರ್ಶಿ ನಿಮಗೆ Azure ಪೋರ್ಟಲ್ ಬಳಸಿ Azure AI Search ಅನ್ನು ಸೆಟಪ್ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ. ನಿಮ್ಮ Azure AI Search ಸೇವೆಯನ್ನು ರಚಿಸಲು ಮತ್ತು ಸಂರಚಿಸಲು ಕೆಳಗಿನ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ.

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

ನೀವು ಪ್ರಾರಂಭಿಸುವ ಮೊದಲು, ಈ ಕೆಳಗಿನವುಗಳನ್ನು ಹೊಂದಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:

- ಒಂದು Azure ಚಂದಾದಾರಿಕೆ. ನೀವು Azure ಚಂದಾದಾರಿಕೆಯನ್ನು ಹೊಂದಿಲ್ಲದಿದ್ದರೆ, [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ನಲ್ಲಿ ಉಚಿತ ಖಾತೆಯನ್ನು ರಚಿಸಬಹುದು.

## ಹಂತ 1: Azure Storage ಖಾತೆಯನ್ನು ರಚಿಸಿ

1. ಹೊಸ Azure Storage ಖಾತೆಯನ್ನು ರಚಿಸಲು ಈ ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal).
   **NOTE**: Storage ಖಾತೆಯ ಪ್ರಕಾರ Standard General Purpose V2 ಆಗಿರಬೇಕು.

## ಹಂತ 2: Azure AI Search ಸೇವೆಯನ್ನು ರಚಿಸಿ

1. [Azure ಪೋರ್ಟಲ್](https://portal.azure.com/?wt.mc_id=studentamb_258691) ಗೆ ಸೈನ್ ಇನ್ ಮಾಡಿ.
2. ಎಡಗೈ ನಾವಿಗೇಶನ್ ಪೇನ್‌ನಲ್ಲಿ **Create a resource** ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ಹುಡುಕಾಟ ಬಾಕ್ಸಿನಲ್ಲಿ "Azure AI Search" ಟೈಪ್ ಮಾಡಿ ಮತ್ತು ಫಲಿತಾಂಶಗಳ ಪಟ್ಟಿಯಿಂದ **Azure AI Search** ಆಯ್ಕೆಮಾಡಿ.
4. **Create** ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ.
5. **Basics** ಟ್ಯಾಬ್‌ನಲ್ಲಿ ಈ ಮಾಹಿತಿಯನ್ನು ಒದಗಿಸಿ:
   - **Subscription**: ನಿಮ್ಮ Azure ಚಂದಾದಾರಿಕೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.
   - **Resource group**: ಹೊಸ ರಿಸೋರ್ಸ್ ಗುಂಪನ್ನು ರಚಿಸಿ ಅಥವಾ विद्यमानವನ್ನು ಆಯ್ಕೆಮಾಡಿ.
   - **Resource name**: ನಿಮ್ಮ ಹುಡುಕಾಟ ಸೇವೆಗೆ ವಿಶಿಷ್ಟ ಹೆಸರು ನಮೂದಿಸಿ.
   - **Region**: ನಿಮ್ಮ ಬಳಕೆದಾರರಿಗೆ ಹತ್ತಿರದ ಪ್ರದೇಶವನ್ನು ಆಯ್ಕೆಮಾಡಿ.
   - **Pricing tier**: ನಿಮ್ಮ ಅಗತ್ಯಗಳಿಗೆ ತಕ್ಕಂತೆ ಪ್ರೈಸಿಂಗ್ ಟಿಯರ್ ಆಯ್ಕೆಮಾಡಿ. ಪರೀಕ್ಷೆಗಾಗಿ Free ಟಿಯರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಬಹುದು.
6. **Review + create** ಕ್ಲಿಕ್ ಮಾಡಿ.
7. ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ಮತ್ತು **Create** ಕ್ಲಿಕ್ ಮಾಡಿ.

## ಹಂತ 3: Azure AI Search ನೊಂದಿಗೆ ಪ್ರಾರಂಭಿಸಿ

1. ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಪೂರ್ಣಗೊಂಡ ನಂತರ, Azure ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಮ್ಮ ಹುಡುಕಾಟ ಸೇವೆಗೆ ಹೋಗಿ.
2. ಹುಡುಕಾಟ ಸೇವೆಯ ಓವರ್‌ವ್ಯೂ ಪೇನ್‌ನಲ್ಲಿ URL ಅನ್ನು ನಕಲಿಸಿ. ಇದು `https://<service-name>.search.windows.net` ಹಾಗಿರುತ್ತದೆ.
3. Settings > Keys ಪೇನ್‌ನಲ್ಲಿ, query key ಅನ್ನು ನಕಲಿಸಿ.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) ಪುಟದ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ, ಒಂದು ಇಂಡೆಕ್ಸ್ ರಚಿಸಲು, ಡೇಟಾವನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಲು ಮತ್ತು ಹುಡುಕಾಟ ಕ್ವೆರಿ ನಡೆಸಲು.

## ಹಂತ 4: Azure AI Search ಟೂಲ್ಸ್ ಬಳಸಿ

Azure AI Search ವಿವಿಧ ಟೂಲ್ಸ್‌ಗಳೊಂದಿಗೆ ಸಂಯೋಜಿತವಾಗಿದ್ದು ನಿಮ್ಮ ಹುಡುಕಾಟ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ. ನೀವು Azure CLI, Python SDK, .NET SDK ಮತ್ತು ಇತರ ಟೂಲ್ಸ್‌ಗಳನ್ನು ಪ್ರಗತಿಶೀಲ ಸಂರಚನೆಗಳು ಮತ್ತು ಕಾರ್ಯಾಚರಣೆಗಳಿಗಾಗಿ ಬಳಸಬಹುದು.

### Azure CLI ಬಳಸಿ

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) ಸೂಚನೆಗಳನ್ನು ಅನುಸರಿಸಿ Azure CLI ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ.
2. ಈ ಕಮಾಂಡ್ ಬಳಸಿ Azure CLI ಗೆ ಸೈನ್ ಇನ್ ಮಾಡಿ:

   ```bash
   az login
   ```

3. Azure AI Search ಇನ್‌ಸ್ಟಾನ್ಸ್‌ನ ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮತ್ತು API ಕೀಗಳನ್ನು ಪರಿಸರ ವ್ಯಾರಿಯಬಲ್ಗಳಲ್ಲಿ ಸಂಗ್ರಹಿಸಿ.

    ```bash
    # ಝೆಡ್‌ಎಸ್‌ಎಚ್/ಬ್ಯಾಶ್
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # ಪವರ್‌ಶೆಲ್
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK ಬಳಸಿ

1. Python ಗೆ Azure Cognitive Search ಕ್ಲೈಂಟ್ ಲೈಬ್ರರಿಯನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ:

   ```bash
   pip install azure-search-documents
   ```

2. ಈ Python ಕೋಡ್ ಅನ್ನು ಬಳಸಿ ಇಂಡೆಕ್ಸ್ ರಚಿಸಿ ಮತ್ತು ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಿ:

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

### .NET SDK ಬಳಸಿ

1. ಈ ಕಮಾಂಡ್ ಅನ್ನು ರನ್ ಮಾಡಿ ಇಂಡೆಕ್ಸ್ ರಚಿಸಲು ಮತ್ತು ಡಾಕ್ಯುಮೆಂಟ್‌ಗಳನ್ನು ಅಪ್ಲೋಡ್ ಮಾಡಲು:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. `AzureSearch.cs` ನ .NET ಕೋಡ್ ಇಲ್ಲಿದೆ:

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

ಹೆಚ್ಚಿನ ವಿವರವಾದ ಮಾಹಿತಿಗಾಗಿ ಈ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಅನ್ನು ನೋಡಿ:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## ತೀರ್ಮಾನ

ನೀವು Azure ಪೋರ್ಟಲ್ ಬಳಸಿ Azure AI Search ಅನ್ನು ಯಶಸ್ವಿಯಾಗಿ ಸೆಟಪ್ ಮಾಡಿದ್ದೀರಿ ಮತ್ತು ಟೂಲ್ಸ್‌ಗಳನ್ನು ಸಂಯೋಜಿಸಿದ್ದೀರಿ. ಈಗ ನೀವು ನಿಮ್ಮ ಹುಡುಕಾಟ ಪರಿಹಾರಗಳನ್ನು ಹೆಚ್ಚಿಸಲು Azure AI Search ನ ಹೆಚ್ಚಿನ ಪ್ರಗತಿಶೀಲ ವೈಶಿಷ್ಟ್ಯಗಳು ಮತ್ತು ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಅನ್ವೇಷಿಸಬಹುದು.

ಹೆಚ್ಚಿನ ಸಹಾಯಕ್ಕಾಗಿ, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ಗೆ ಭೇಟಿ ನೀಡಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸಮೀಕ್ಷೆ**:  
ಈ ದಾಖಲೆ AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಮಂಜಸತೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆ ಪ್ರಾಮಾಣಿಕ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪುಅರ್ಥಗಳು ಅಥವಾ ತಪ್ಪುಅರ್ಥೈಸುವಿಕೆಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->