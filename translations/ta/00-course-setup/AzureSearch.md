# அஜூர் AI தேடல் அமைப்பு வழிகாட்டி

இந்த வழிகாட்டி மூலம் நீங்கள் அஜூர் போர்டலைப் பயன்படுத்தி அஜூர் AI தேடலை அமைக்க உதவும். கீழ்க்காணும் படிகளை பின்பற்றி உங்கள் அஜூர் AI தேடல் சேவையை உருவாக்கி அமைக்கவும்.

## தேவையானவை

துவங்குவதற்கு முன், இது உங்களிடமிருக்க வேண்டும் என்று உறுதி செய்யுங்கள்:

- ஒரு அஜூர் சந்தா(plan). அஜூர் சந்தா இல்லையெனில், நீங்கள் [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)இல் இலவச கணக்கை உருவாக்கலாம்.

## படி 1: அஜூர் சேமிப்பு கணக்கை உருவாக்குதல்

1. இந்த வழிமுறையை பின்பற்றவும், [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), புதிய அஜூர் சேமிப்பு கணக்கை உருவாக்க.
   **குறிப்பு**: சேமிப்பு கணக்கு வகை Standard General Purpose V2 என்பதாக இருக்க வேண்டும் என்பதை உறுதி செய்யவும்.

## படி 2: அஜூர் AI தேடல் சேவையை உருவாக்குதல்

1. [அஜூர் போர்டலில்](https://portal.azure.com/?wt.mc_id=studentamb_258691) உள்நுழையவும்.
2. இடதுபுற வழிசெலுத்தல் பட்டியில் **Create a resource** என்பதை சொடுக்கவும்.
3. தேடல் பெட்டியில் "Azure AI Search" எனைத் தட்டச்சு செய்து, முடிவுகளில் இருந்து **Azure AI Search** ஐத் தேர்ந்தெடுக்கவும்.
4. **Create** கноп்டனை சொடுக்கவும்.
5. **Basics** டேபில் கீழ்க்கண்ட தகவல்களை வழங்கவும்:
   - **Subscription**: உங்கள் அஜூர் சந்தாவைத் தேர்ந்தெடுக்கவும்.
   - **Resource group**: புதிய ரிசோர்ஸ் குழுவை உருவாக்கவும் அல்லது ஏற்கனவே உள்ள ஒன்றைத் தேர்ந்தெடுக்கவும்.
   - **Resource name**: உங்கள் தேடல் சேவைக்கு தனிப்பட்ட பெயரை வழங்கவும்.
   - **Region**: உங்கள் பயனர்களுக்கு அருகிலுள்ள பிராந்தியத்தைத் தேர்வு செய்யவும்.
   - **Pricing tier**: உங்கள் தேவைகளுக்கு ஏற்ப ஒரு விலைப் படியை தேர்ந்தெடுக்கவும். சோதனைக்காக இலவச படியுடன் துவங்கலாம்.
6. **Review + create** என்பதை சொடுக்கவும்.
7. அமைப்புகளை மதிப்பாய்வு செய்து, சேவையை உருவாக்க **Create** ஐ சொடுக்கவும்.

## படி 3: அஜூர் AI தேடலைத் துவங்குதல்

1. நிறுவல் முடிந்தவுடன், அஜூர் போர்டலில் உங்கள் தேடல் சேவைக்குச் செல்லவும்.
2. தேடல் சேவை ஓவர்வியூ பகுதியில் உள்ள URL ஐ நகலெடுக்கவும். இது `https://<service-name>.search.windows.net` போன்றதாக இருக்கும்.
3. **(பதிவு செய்ய பரிந்துரை செய்யப்படுகிறது)** கீழ்க்கண்ட படி 4 இல் காணப்படும் Microsoft Entra ID (RBAC) உடன் விசையில்லா அணுகலை செயல்படுத்தவும் — விசை தேவையில்லை. இந்த வழிகாட்டியில் உள்ள உதாரணங்கள் குறியீटுகளை உருவாக்குகின்றன/புதுப்பிக்கின்றன மற்றும் ஆவணங்களை பதிவேற்றுகின்றன, ஆகவே இவை **Search Service Contributor** மற்றும் **Search Index Data Contributor** பணியாளர்கள் (அல்லது விசை அடிப்படையிலான அங்கீகாரம் பயன்படுத்தின், **primary admin key** — கேள்வி விசை அல்ல) விருப்பமானவை. RBAC பயன்படுத்த இயலாவிட்டால் மட்டுமே, **Settings > Keys** பகுதியைப் திறந்து **primary admin key** ஐ நகலெடுக்கவும்.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) பக்கத்தில் உள்ள படிகளைப் பின்பற்றி குறியீட்டு உருவாக்கம், தரவிறக்கம் மற்றும் தேடலைச் செய்யவும்.

## படி 4: அஜூர் AI தேடல் கருவிகளை பயன்படுத்துதல்

அஜூர் AI தேடல் பல்வேறு கருவிகளுடன் ஒருங்கிணைக்கப்படுகிறது, இது உங்கள் தேடல் திறன்களை அதிகரிக்கும். விரிவான அமைப்புகள் மற்றும் செயல்பாடுகளுக்கு, நீங்கள் அஜூர் CLI, பைதான் SDK, .NET SDK மற்றும் பிற கருவிகளைப் பயன்படுத்தலாம்.

### அஜூர் CLI பயன்படுத்துதல்

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) இல் உள்ள வழிமுறைகளைக் கையாள்ந்து அஜூர் CLI ஐ நிறுவவும்.
2. கீழ்க்கண்ட கட்டளையைப் பயன்படுத்தி அஜூர் CLI இல் உள்நுழையவும்:

   ```bash
   az login
   ```
3. **(பதிவு செய்ய பரிந்துரை செய்யப்படுகிறது) Microsoft Entra ID (RBAC) உடன் விசையில்லா அணுகலை செயல்படுத்தவும்:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search சேவை “endpoint” புலம் இல்லை என்பதை காட்டுகிறது; சேவை பெயரிலிருந்து URL உருவாக்கவும்.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC செயல்படுத்தப்பட்டால், கீழ்காணும் பைதான் மற்றும் .NET SDK எடுத்துக்காட்டுகள் `DefaultAzureCredential` உடன் அங்கீகரிப்பதைக் கொண்டு உங்கள் `az login` அமர்வைப் பயன்படுத்தும் - அதாவது நிர்வாக விசை தேவையில்லை. விரிவுக்கு [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) பார்க்கவும்.

4. **(மாற்று வழி) விசை அடிப்படையிலான அங்கீகாரம்** — RBAC இனைப் பயன்படுத்த முடியாவிட்டால் மட்டுமே, நிர்வாக விசையையும் சேமிக்கவும்:

#### Azure AI தேடல் நிகழ்விற்கான என்ட்பாயிண்ட் மற்றும் API விசையினை சுற்றுச்சூழல் மாறிகளாக சேமிக்கவும்.

    ```bash
    # zsh/bash
    # az search service show இல் "endpoint" புலம் இல்லை; சேவை பெயரிலிருந்து URL உருவாக்கவும்.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show இல் "endpoint" புலம் இல்லை; சேவை பெயரிலிருந்து URL உருவாக்கவும்.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### பைதான் SDK பயன்படுத்துதல்

1. அஜூர் காக்னிடிவ் தேடல் கிளையன்ட் நூலகமேலும் அஜூர் அடையாளத்தை Python க்கான நிறுவவும்:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. குறியீட்டு உருவாக்கம் மற்றும் ஆவணங்களை பதிவேற்ற கீழ்காணும் பைதான் குறியீட்டைப் பயன்படுத்தவும்:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # திறவுகோல் இல்லாதது (பரிந்துரைக்கப்படுகிறது): உங்கள் `az login` அடையாளத்தை Entra ID RBAC மூலம் பயன்படுத்துகிறது.
    # "Search Service Contributor" மற்றும் "Search Index Data Contributor" பங்கை requமியதாகும்.
    credential = DefaultAzureCredential()
    # மாற்று வழி (திறவுகோல் அடிப்படையிலான அங்கீகாரம்):
    # azure.core.credentials இலிருந்து AzureKeyCredential ஐ இறக்குமதி செய்க
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

### .NET SDK பயன்படுத்துதல்

1. குறியீட்டு உருவாக்கம் மற்றும் ஆவணங்களை பதிவேற்ற கீழ்காணும் கட்டளையை இயக்கவும்:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    கீழ்காணும் .NET உதாரணம் `DefaultAzureCredential` ஐப் பயன்படுத்தி, இது உள்ளூரில் `az login` இல் இருந்து உங்கள் அஜூர் CLI உள்நுழைவைக் கையாளலாம்.

2. கீழே `AzureSearch.cs` என்ற .NET குறியீடு உள்ளது:

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

விரிவான தகவலுக்கு, கீழ்க்கண்ட ஆவணங்களைப் பார்க்கவும்:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## முடிவுரை

நீங்கள் அஜூர் போர்டலைப் பயன்படுத்தி அஜூர் AI தேடலை வெற்றிகரமாக அமைத்துக் கொண்டு, ஒருங்கிணைந்த கருவிகளையும் பயன்படுத்தி விட்டீர்கள். இப்போது நீங்கள் அஜூர் AI தேடலின் மேம்பட்ட அம்சங்களையும் திறன்களையும் ஆராய்ந்து, உங்கள் தேடல் தீர்வுகளை முன்னேற்றலாம்.

மேலதிக உதவிக்காக, [Azure Cognitive Search ஆவணங்களை](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) அணுகவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->