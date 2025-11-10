<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:44:41+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "tl"
}
-->
# Gabay sa Pagsasaayos ng Azure AI Search

Ang gabay na ito ay tutulong sa iyo na i-set up ang Azure AI Search gamit ang Azure portal. Sundin ang mga hakbang sa ibaba upang lumikha at i-configure ang iyong Azure AI Search service.

## Mga Kinakailangan

Bago ka magsimula, tiyakin na mayroon ka ng mga sumusunod:

- Isang subscription sa Azure. Kung wala ka pang subscription sa Azure, maaari kang gumawa ng libreng account sa [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## Hakbang 1: Gumawa ng Azure Storage Account

1. Sundin ang mga tagubilin sa [Gumawa ng Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) upang lumikha ng bagong Azure Storage Account.  
   **NOTE**: Siguraduhin na ang uri ng Storage Account ay Standard General Purpose V2.

## Hakbang 2: Gumawa ng Azure AI Search Service

1. Mag-sign in sa [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. Sa kaliwang navigation pane, i-click ang **Create a resource**.
3. Sa search box, i-type ang "Azure AI Search" at piliin ang **Azure AI Search** mula sa listahan ng mga resulta.
4. I-click ang **Create** button.
5. Sa **Basics** tab, ibigay ang sumusunod na impormasyon:
   - **Subscription**: Piliin ang iyong Azure subscription.
   - **Resource group**: Gumawa ng bagong resource group o piliin ang umiiral na.
   - **Resource name**: Maglagay ng natatanging pangalan para sa iyong search service.
   - **Region**: Piliin ang rehiyon na pinakamalapit sa iyong mga user.
   - **Pricing tier**: Piliin ang pricing tier na naaayon sa iyong pangangailangan. Maaari kang magsimula sa Free tier para sa testing.
6. I-click ang **Review + create**.
7. Suriin ang mga settings at i-click ang **Create** upang lumikha ng search service.

## Hakbang 3: Simulan ang Paggamit ng Azure AI Search

1. Kapag tapos na ang deployment, pumunta sa iyong search service sa Azure portal.
2. Sa search service overview pane, kopyahin ang URL. Dapat itong magmukhang `https://<service-name>.search.windows.net`.
3. Sa Settings > Keys pane, kopyahin ang query key.
4. Sundin ang mga hakbang sa [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) page upang lumikha ng index, mag-upload ng data, at magsagawa ng search query.

## Hakbang 4: Gamitin ang Mga Tool ng Azure AI Search

Ang Azure AI Search ay maaaring isama sa iba't ibang mga tool upang mapahusay ang iyong search capabilities. Maaari mong gamitin ang Azure CLI, Python SDK, .NET SDK, at iba pang mga tool para sa advanced na configurations at operations.

### Paggamit ng Azure CLI

1. I-install ang Azure CLI sa pamamagitan ng pagsunod sa mga tagubilin sa [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. Mag-sign in sa Azure CLI gamit ang command:

   ```bash
   az login
   ```

3. I-store ang endpoint at API key ng Azure AI Search instance sa environment variables.

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

### Paggamit ng Python SDK

1. I-install ang Azure Cognitive Search client library para sa Python:

   ```bash
   pip install azure-search-documents
   ```

2. Gamitin ang sumusunod na Python code upang lumikha ng index at mag-upload ng mga dokumento:

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

### Paggamit ng .NET SDK

1. Patakbuhin ang sumusunod na command upang lumikha ng index at mag-upload ng mga dokumento:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. Narito ang .NET code ng `AzureSearch.cs`:

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

Para sa mas detalyadong impormasyon, bisitahin ang mga sumusunod na dokumentasyon:

- [Gumawa ng Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Simulan ang paggamit ng Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Mga Tool ng Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Konklusyon

Matagumpay mong na-set up ang Azure AI Search gamit ang Azure portal at mga integrated tools. Maaari mo nang tuklasin ang mas advanced na features at capabilities ng Azure AI Search upang mapahusay ang iyong search solutions.

Para sa karagdagang tulong, bisitahin ang [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.