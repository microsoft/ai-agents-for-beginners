# Azure AI தேடல் அமைப்பு வழிகாட்டி

இந்த வழிகாட்டி Azure போர்டலை பயன்படுத்தி Azure AI தேடலை அமைக்க உதவும். உங்கள் Azure AI தேடல் சேவையை உருவாக்கவும் ஒழுங்குபடுத்தவும் கீழ்காணும் படிகளை பின்பற்றுங்கள்.

## முன் நிபந்தனைகள்

தொடங்குவதற்கு முன், கீழ்கண்டவை உங்களிடம் இருப்பதை உறுதி செய்க:

- ஒரு Azure சந்தா. உங்களிடம் Azure சந்தா இல்லையெனில், [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) இல் ஒரு இலவச கணக்கை உருவாக்கலாம்.

## படி 1: Azure சேமிப்பு கணக்கை உருவாக்கவும்

1. இந்த வழிமுறைகளை பின்பற்றி, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) புதிய Azure சேமிப்பு கணக்கை உருவாக்குங்கள்.
   **குறிப்பு**: சேமிப்பு கணக்கின் வகை Standard General Purpose V2 ஆக இருக்க வேண்டும் என்பதை உறுதி செய்யுங்கள்.

## படி 2: Azure AI தேடல் சேவையை உருவாக்கவும்

1. [Azure போர்டலில்](https://portal.azure.com/?wt.mc_id=studentamb_258691) உள்நுழைக.
2. இடது பக்கப் படையலில், **Create a resource** என்பதைக் கிளிக் செய்யுங்கள்.
3. தேடு பெட்டியில் "Azure AI Search" என எழுதி, பெறுபவர்கள் பட்டியலில் இருந்து **Azure AI Search** ஐ தேர்ந்தெடுக்கவும்.
4. **Create** பொத்தானை அழுத்தவும்.
5. **Basics** தாவலில் கீழ்காணும் தகவல்களை வழங்கவும்:
   - **Subscription**: உங்கள் Azure சந்தாவை தேர்வு செய்யவும்.
   - **Resource group**: புதிய ஒரு resource குழுவை உருவாக்குங்கள் அல்லது ஏற்கனவே உள்ள ஒன்றை தேர்ந்தெடுக்கவும்.
   - **Resource name**: உங்கள் தேடல் சேவைக்கான தனித்துவமான பெயரை உள்ளிடவும்.
   - **Region**: உங்கள் பயனர்களுக்கு அருகிலுள்ள மண்டலத்தைத் தேர்ந்தெடுக்கவும்.
   - **Pricing tier**: உங்கள் தேவைகளுக்கு ஏற்ப விலைப்பட்டியல ضلعை தேர்ந்தெடுக்கவும். சோதனைக்காக Free tier ஐ ஆரம்பிக்கலாம்.
6. **Review + create** என்பதை அழுத்தவும்.
7. அமைப்புகளை பரிசீலித்து **Create** பொத்தானை கிளிக் செய்து தேடல் சேவையை உருவாக்கவும்.

## படி 3: Azure AI தேடலைத் தொடங்குதல்

1. நடைமுறை நிறைவடைந்தவுடன், Azure போர்டலில் உங்கள் தேடல் சேவைக்கு செல்லவும்.
2. தேடல் சேவை மேலாண்மை தாவலில் URL ஐ பிரதिलிபி செய்யவும். அது `https://<service-name>.search.windows.net` போன்றதாக இருக்கும்.
3. **(பரிந்துரைக்கப்படும்)** கீழே உள்ள படி 4ில் காண்பித்த Microsoft Entra ID (RBAC) உடன் முக்கியமற்ற அணுகலை இயந்திரப்பொருள் சேர்க்கவும் — எந்த விசையும் தேவையில்லை. இந்த வழிகாட்டியில் உள்ள உதாரணங்கள் குறியீடுகள் உருவாக்குதல்/புதுப்பித்தல் மற்றும் ஆவணங்களை பதிவேற்றுவதற்காக **Search Service Contributor** மற்றும் **Search Index Data Contributor** பங்கு உரிமைகள் (அல்லது விசை அடிப்படையிலான அங்கீகாரம் பயன்படுத்தினால் **primary admin key** — கேள்வி விசை அல்ல) தேவைப்படுகிறது. நீங்கள் RBAC பயன்படுத்த இயலவில்லை என்றால் மட்டும், **Settings > Keys** தாவலை திறந்து **primary admin key** ஐ பிரதிலிபி செய்யவும்.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) பக்கத்தில் உள்ள படிகளை பின்பற்றி குறியீடு உருவாக்கவும், தரவை பதிவேற்றவும் மற்றும் தேடல் செய்யவும்.

## படி 4: Azure AI தேடல் கருவிகளைப் பயன்படுத்துதல்

Azure AI தேடல் பல கருவிகள் மூலம் ஒருங்கிணைக்கப்பட்டுள்ளது, இது உங்கள் தேடல் திறன்களை மேம்படுத்த உதவும். Azure CLI, Python SDK, .NET SDK மற்றும் பிற கருவிகளை விரிவான அமைப்புகளுக்கும் செயல்பாடுகளுக்கும் பயன்படுத்தலாம்.

### Azure CLI பயன்படுத்துதல்

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) இல் உள்ள வழிமுறைகளை பின்பற்றிக் Azure CLI ஐ நிறுவுங்கள்.
2. கீழ்கண்ட கட்டளையை பயன்படுத்தி Azure CLI இல் உள்நுழையவும்:

   ```bash
   az login
   ```
3. **(பரிந்துரைக்கப்படும்) Microsoft Entra ID (RBAC) உடன் முக்கியமற்ற அணுகலை இயக்கவும்:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search சேவை காட்டும் "endpoint" புலம் இல்லை; சேவை பெயர் மூலம் URL உருவாக்கவும்.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC இயங்கும்போது, கீழ்காணும் Python மற்றும் .NET SDK உதாரணங்கள் `DefaultAzureCredential` மூலம் அங்கீகாரம் பெறுகின்றன, இது உள்ளூர் அபிவிருத்தி போது உங்கள் `az login` அமர்வைப் பயன்படுத்துகிறது — எந்த நிர்வாக விசையும் தேவையில்லை. விவரங்களுக்கு [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) பார்க்கவும்.

4. **(மீள்நிறைவு) விசை அடிப்படையிலான அங்கீகாரம்** — நீங்கள் RBAC பயன்படுத்த இயலவில்லை என்றால் மட்டும் நிர்வாக விசையையும் சேமிக்கவும்:

#### Azure AI தேடல் எடுத்துக்காட்டுக்கான இடைக் முகவரி மற்றும் API விசையை சுற்றுப்புற மாறிகளாக சேமிக்கவும்.

    ```bash
    # zsh/bash
    # az search service show க்கு "endpoint" புலம் இல்லை; சேவை பெயரை பயன்படுத்தி URL உருவாக்கவும்.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show க்கு "endpoint" புலம் இல்லை; சேவை பெயரை பயன்படுத்தி URL உருவாக்கவும்.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK பயன்படுத்துதல்

1. Azure Cognitive Search கிளையன்ட் நூலகம் மற்றும் Azure Identity ஐ Python க்குச் நிறுவவும்:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ஒரு குறியீடு உருவாக்கி ஆவணங்களை பதிவேற்ற கீழ்கண்ட Python குறியீட்டை பயன்படுத்தவும்:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # சாவியில்லா (பரிந்துரைக்கப்பட்டது): உங்கள் `az login` அடையாளத்தை Entra ID RBAC மூலம் பயன்படுத்துகிறது.
    # "Search Service Contributor" மற்றும் "Search Index Data Contributor" பணியாளர்கள் தேவைப்படுகிறது.
    credential = DefaultAzureCredential()
    # மாற்றுத்திட்டம் (சாவி அடிப்படையிலான அங்கீகாரம்):
    # azure.core.credentials இருந்து AzureKeyCredential ஐ இறக்குமதி செய்க
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

1. குறியீடு உருவாக்கி ஆவணங்களை பதிவேற்ற கீழ்காணும் கட்டளையை இயக்கவும்:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    கீழ்காணும் .NET உதாரணம் உள்ளூர் அபிவிருத்தி போது `az login` இலிருந்து Azure CLI உள்நுழையலை பயன்படுத்தும் `DefaultAzureCredential` ஐப் பயன்படுத்துகிறது.

2. இதோ `AzureSearch.cs` இன் .NET குறியீடு:

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

விரிவான தகவலுக்கு, கீழ்காணும் ஆவணங்களைப் பார்க்கவும்:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## முடிவுரை

நீங்கள் வெற்றிகரமாக Azure போர்டலைப் பயன்படுத்தி Azure AI தேடலை அமைத்துக் கொண்டு கருவிகளை ஒருங்கிணைத்துவிட்டீர்கள். இப்போது Azure AI தேடலின் மேலும் விரிவான அம்சங்கள் மற்றும் திறன்களை ஆராய்ந்து உங்கள் தேடல் தீர்வுகளை மேம்படுத்தலாம்.

மேலதிக உதவிக்கு, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ஐப் பார்வையிடவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->