# Azure AI தேடல் அமைப்பு வழிகாட்டி

இந்த வழிகாட்டி Azure போர்டலை பயன்படுத்தி Azure AI தேடலை அமைக்க உதவும். உங்கள் Azure AI தேடல் சேவையை உருவாக்கி அமைக்க கீழ்க்காணும் படிகளை பின்பற்றவும்.

## தேவையான முன்கூட்டல்கள்

நீங்கள் தொடங்குவதற்கு முன், கீழ்காணும் விஷயங்களை உறுதிசெய்க:

- ஒரு Azure சந்தா. உங்களிடம் Azure சந்தா இல்லையெனில், [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) இல் ஒரு இலவச கணக்கை உருவாக்கலாம்.

## படி 1: Azure சேமிப்பு கணக்கை உருவாக்கவும்

1. இந்த வழிகாட்டியை பின்பற்றவும், [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), புதிய Azure சேமிப்பு கணக்கை உருவாக்க.
   **குறிப்பு**: சேமிப்பு கணக்கு வகை Standard General Purpose V2 ஆக இருக்கிறதா என்பதை உறுதிசெய்க.

## படி 2: Azure AI தேடல் சேவையை உருவாக்கவும்

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) இல் சைன் இன் செய்யவும்.
2. இடது பக்க வழிசெலுத்தல் பகுதியில், **Create a resource** என்பதைக் கிளிக் செய்யவும்.
3. தேடல் பெட்டியில் "Azure AI Search" என்று تایப் செய்து, முடிவுகளிலிருந்து **Azure AI Search** ஐத் தேர்ந்தெடுக்கவும்.
4. **Create** பொத்தானை கிளிக் செய்க.
5. **Basics** தாவலில் கீழ்க்காணும் தகவல்களை வழங்கவும்:
   - **Subscription**: உங்கள் Azure சந்தாவை தேர்ந்தெடுக்கவும்.
   - **Resource group**: புதிய resource குழுவை உருவாக்கவோ அல்லது ஏற்கனவே இருக்கும் ஒன்றை தேர்ந்தெடுக்கவோ செய்யவும்.
   - **Resource name**: உங்கள் தேடல் சேவைக்கான தனித்துவமான பெயரை உள்ளிடவும்.
   - **Region**: உங்கள் பயனாளர்களுக்கு அருகிலுள்ள பிராந்தியத்தை தேர்ந்தெடுக்கவும்.
   - **Pricing tier**: உங்கள் தேவைகளுக்கு ஏற்ப பொருந்தக்கூடிய ஒரு விலை தொகுதி தேர்வு செய்யவும். சோதனைக்கு இலவச தொகுதியுடன் தொடங்கலாம்.
6. **Review + create** என்பதை கிளிக் செய்க.
7. அமைப்புகளை பரிசீலனை செய்து **Create** ஐ கிளிக் செய்து தேடல் சேவையை உருவாக்கவும்.

## படி 3: Azure AI தேடலுடன் தொடக்கம்

1. உருவாக்கல் முடிந்தவுடன், Azure போர்டல் இல் உங்கள் தேடல் சேவைக்கு செல்லவும்.
2. தேடல் சேவை முன்னோட்டப் பக்கத்தில் URL ஐ நகலெடுக்கவும். இது `https://<service-name>.search.windows.net` போன்றதாக இருக்கும்.
3. **(பரிந்துரைக்கப்பட்டது)** Microsoft Entra ID (RBAC) மூலம் கீயில்லா அணுகலை வழிகாட்டி படி 4-ல் காட்டியபடி இயக்கவும் — எந்த விசை தேவையில்லை. இந்த வழிகாட்டியில் உள்ள மாதிரிகள் குறியீடுகளை உருவாக்க/புதுப்பிக்கவும், ஆவணங்களை பதிவேற்றவும் செய்கின்றன, அதற்கு **Search Service Contributor** மற்றும் **Search Index Data Contributor** உரிமைகள் (அல்லது விசை அடிப்படையிலான அங்கீகாரம் அவசியமாயினால், **primary admin key** — query key அல்ல) தேவையானவை. நீங்கள் RBAC பயன்படுத்த முடியாவிட்டால் மட்டுமே **Settings > Keys** பக்கத்தைக் குலையுங்கள் மற்றும் **primary admin key** ஐ நகலெடுக்கவும்.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) பக்கத்தில் உள்ள படிகளை பின்பற்றி குறியீடு உருவாக்கி, தரவுகளை பதிவேற்று, தேடலை செயல்படுத்தவும்.

## படி 4: Azure AI தேடல் கருவிகளை பயன்படுத்துதல்

Azure AI தேடல் பல கருவிகளுடன் ஒருங்கிணைந்து உங்கள் தேடல் திறன்களை மேம்படுத்துகிறது. மேம்பட்ட கட்டமைப்புகள் மற்றும் செயல்பாட்டுக்கு Azure CLI, Python SDK, .NET SDK மற்றும் பிற கருவிகளை நீங்கள் பயன்படுத்தலாம்.

### Azure CLI பயன்படுத்துதல்

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) இல் உள்ள வழிமுறைகளை பின்பற்றி Azure CLI ஐ நிறுவவும்.
2. கீழ்க்காணும் கட்டளையை பயன்படுத்தி Azure CLI இல் உள்நுழையவும்:

   ```bash
   az login
   ```
3. **(பரிந்துரைக்கப்பட்டது) Microsoft Entra ID (RBAC) உடன் கீயில்லா அணுகலை இயக்கவும்:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC இயற்றப்பட்டுள்ளதாக Python மற்றும் .NET SDK மாதிரிகள் கீழே உள்ள `DefaultAzureCredential` உடன் அங்கீகாரம் செய்கின்றன, இது உங்கள் `az login` Beard-ல் உள்ள அமர்வைப் பயன்படுத்துகிறது — எந்த நிர்வாக விசையும் தேவையில்லை. [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) ஐ காணவும்.

4. **(மறு வழி) விசை அடிப்படையிலான அங்கீகாரம்** — RBAC பயன்படுத்த முடியாவிட்டால் மட்டுமே நிர்வாக விசையை சேமிக்கவும்:

#### Azure AI தேடல் அமைப்புக்கான Endpoint மற்றும் API விசையைக் சுற்றுப்புற மாறிலிகளாக சேமிக்கவும்.

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

### Python SDK உடன் பயன்படுத்துதல்

1. Azure Cognitive Search கே்ளயண்ட் நூலகத்தையும் Azure Identity for Python ஐ நிறுவுக:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. குறியீடு உருவாக்கவும் ஆவணங்களை பதிவேற்றவும் பின்வரும் Python குறியீட்டை பயன்படுத்தவும்:

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

### .NET SDK உடன் பயன்படுத்துதல்

1. குறியீடு உருவாக்கவும் ஆவணங்களை பதிவேற்றவும் பின்வரும் கட்டளையை இயக்கவும்:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    கீழ்காணும் .NET மாதிரி `DefaultAzureCredential` பயன்படுத்துகிறது, இது உள்ளூரில் வளர்ச்சி செய்வதற்கான உள்நாட்டில் Azure CLI உள்நுழைவை `az login` இல் பயன்படுத்தக்கூடும்.

2. `AzureSearch.cs` இன் .NET குறியீடு இதோ:

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

கூடுதல் விரிவான தகவலுக்கு பின்வரும் ஆவணங்களைப் பார்க்கவும்:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## முடிவுரை

நீங்கள் Azure போர்டலை பயன்படுத்தி Azure AI தேடலை வெற்றிகரமாக அமைத்துள்ளீர்கள் மற்றும் ஒருங்கிணைந்த கருவிகளை பயன்படுத்தி உள்ளீர்கள். இப்போது, உங்கள் தேடல் தீர்வுகளை மேம்படுத்த Azure AI தேடலின் மேம்பட்ட அம்சங்கள் மற்றும் திறன்களை ஆராயலாம்.

மேலதிக உதவிக்காக, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ஐ அணுகவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->