<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:54:31+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ta"
}
-->
# Azure AI Search அமைப்பு வழிகாட்டி

இந்த வழிகாட்டி Azure AI Search ஐ Azure போர்டல் மூலம் அமைக்க உதவுகிறது. உங்கள் Azure AI Search சேவையை உருவாக்கி அமைக்க கீழே உள்ள படிகளை பின்பற்றவும்.

## முன் தேவைகள்

தொடங்குவதற்கு முன், உங்களிடம் பின்வருவன இருக்க வேண்டும்:

- ஒரு Azure சந்தா. Azure சந்தா இல்லையெனில், [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) இல் இலவச கணக்கை உருவாக்கலாம்.

## படி 1: Azure சேமிப்பு கணக்கை உருவாக்கவும்

1. புதிய Azure சேமிப்பு கணக்கை உருவாக்க [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) வழிகாட்டியை பின்பற்றவும்.
   **NOTE**: சேமிப்பு கணக்கின் வகை Standard General Purpose V2 ஆக இருக்க வேண்டும் என்பதை உறுதிப்படுத்தவும்.

## படி 2: Azure AI Search சேவையை உருவாக்கவும்

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) இல் உள்நுழைக.
2. இடது பக்க வழிசெலுத்தல் பட்டியில் **Create a resource** என்பதைக் கிளிக் செய்யவும்.
3. தேடல் பெட்டியில் "Azure AI Search" என தட்டச்சு செய்து, முடிவுகளின் பட்டியலில் **Azure AI Search** ஐத் தேர்ந்தெடுக்கவும்.
4. **Create** பொத்தானை கிளிக் செய்யவும்.
5. **Basics** தாவலில் பின்வரும் தகவல்களை வழங்கவும்:
   - **Subscription**: உங்கள் Azure சந்தாவைத் தேர்ந்தெடுக்கவும்.
   - **Resource group**: புதிய resource group ஐ உருவாக்கவும் அல்லது ஏற்கனவே உள்ள resource group ஐத் தேர்ந்தெடுக்கவும்.
   - **Resource name**: உங்கள் தேடல் சேவைக்கு தனித்துவமான பெயரை உள்ளிடவும்.
   - **Region**: உங்கள் பயனர்களுக்கு அருகிலுள்ள பிராந்தியத்தைத் தேர்ந்தெடுக்கவும்.
   - **Pricing tier**: உங்கள் தேவைகளுக்கு ஏற்ப ஒரு விலை நிலையைத் தேர்ந்தெடுக்கவும். சோதனைக்காக Free tier ஐத் தொடங்கலாம்.
6. **Review + create** என்பதைக் கிளிக் செய்யவும்.
7. அமைப்புகளை சரிபார்த்து, தேடல் சேவையை உருவாக்க **Create** என்பதைக் கிளிக் செய்யவும்.

## படி 3: Azure AI Search ஐ தொடங்கவும்

1. அமைப்பு முடிந்தவுடன், Azure போர்டலில் உங்கள் தேடல் சேவைக்கு செல்லவும்.
2. தேடல் சேவை ஒட்டுமொத்தப் பக்கத்தில் URL ஐ நகலெடுக்கவும். இது `https://<service-name>.search.windows.net` போல இருக்கும்.
3. Settings > Keys பக்கத்தில் query key ஐ நகலெடுக்கவும்.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) பக்கத்தில் உள்ள படிகளை பின்பற்றி ஒரு index ஐ உருவாக்கி, தரவுகளை பதிவேற்றி, தேடல் கேள்வியைச் செய்யவும்.

## படி 4: Azure AI Search கருவிகளைப் பயன்படுத்தவும்

Azure AI Search பல்வேறு கருவிகளுடன் ஒருங்கிணைக்கிறது, இது உங்கள் தேடல் திறன்களை மேம்படுத்த உதவுகிறது. Azure CLI, Python SDK, .NET SDK மற்றும் பிற கருவிகளை மேம்பட்ட அமைப்புகள் மற்றும் செயல்பாடுகளுக்கு பயன்படுத்தலாம்.

### Azure CLI ஐப் பயன்படுத்துதல்

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) வழிகாட்டியை பின்பற்றி Azure CLI ஐ நிறுவவும்.
2. கீழே உள்ள கட்டளையைப் பயன்படுத்தி Azure CLI இல் உள்நுழைக:

   ```bash
   az login
   ```

3. Azure AI Search instance க்கான endpoint மற்றும் API key ஐ சுற்றுச்சூழல் மாறிகளில் சேமிக்கவும்.

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

### Python SDK ஐப் பயன்படுத்துதல்

1. Python க்கான Azure Cognitive Search client library ஐ நிறுவவும்:

   ```bash
   pip install azure-search-documents
   ```

2. கீழே உள்ள Python குறியீட்டை பயன்படுத்தி ஒரு index ஐ உருவாக்கி, ஆவணங்களை பதிவேற்றவும்:

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

### .NET SDK ஐப் பயன்படுத்துதல்

1. கீழே உள்ள கட்டளையை இயக்கி ஒரு index ஐ உருவாக்கி, ஆவணங்களை பதிவேற்றவும்:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. `AzureSearch.cs` இன் .NET குறியீடு இதோ:

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

மேலும் விரிவான தகவலுக்கு, பின்வரும் ஆவணங்களைப் பார்க்கவும்:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## முடிவு

Azure போர்டல் மற்றும் ஒருங்கிணைந்த கருவிகளைப் பயன்படுத்தி Azure AI Search ஐ வெற்றிகரமாக அமைத்துள்ளீர்கள். உங்கள் தேடல் தீர்வுகளை மேம்படுத்த Azure AI Search இன் மேம்பட்ட அம்சங்கள் மற்றும் திறன்களை இப்போது ஆராயலாம்.

மேலும் உதவிக்காக, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ஐ பார்வையிடவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.