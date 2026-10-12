# មាតិកាជំនួយការដំឡើង Azure AI Search

មាតិកានេះនឹងជួយអ្នកក្នុងការដំឡើង Azure AI Search តាមរយៈវីបសាយ Azure portal ។ សូមអនុវត្តជំហានខាងក្រោមដើម្បីបង្កើតនិងកំណត់រចនាសម្ព័ន្ធសេវាកម្ម Azure AI Search របស់អ្នក។

## លក្ខណៈត្រូវមានមុន

មុនដែលអ្នកចាប់ផ្តើម សូមធានាថាអ្នកមានធាតុដូចខាងក្រោម៖

- ប្រើប្រាស់ Azure subscription ។ ប្រសិនបើអ្នកមិនមាន Azure subscription, អ្នកអាចបង្កើតគណនីឥតគិតថ្លៃនៅ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)។

## ជំហានទី ១៖ បង្កើតគណនីផ្ទុកទិន្នន័យ Azure Storage Account

1. អនុវត្តតាមការណែនាំនេះ [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) ដើម្បីបង្កើតគណនីផ្ទុកទិន្នន័យថ្មីមួយ។
   **ចំណាំ**៖ សូមប្រាកដថាប្រភេទ Storage Account គឺជាប្រភេទ Standard General Purpose V2។

## ជំហានទី ២៖ បង្កើតសេវាកម្ម Azure AI Search

1. ចូលដំណើរការទៅកាន់ [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691)។
2. នៅផ្នែកបញ្ជីនៅខាងឆ្វេង សូមចុចលើ **Create a resource**។
3. នៅប្រអប់ស្វែងរក សូមវាយពាក្យ "Azure AI Search" ហើយជ្រើសរើស **Azure AI Search** ពីបញ្ជីលទ្ធផល។
4. ចុចប៊ូតុង **Create**។
5. នៅក្នុងផ្ទាំង **Basics** សូមផ្តល់ព័ត៌មានដូចខាងក្រោម៖
   - **Subscription**៖ ជ្រើសរើស Azure subscription របស់អ្នក។
   - **Resource group**៖ បង្កើត resource group ថ្មី ឬជ្រើសរើស resource group តាមដែលមាន។
   - **Resource name**៖ បញ្ជូលឈ្មោះដើម្បីពិសេសសម្រាប់សេវាកម្មស្វែងរករបស់អ្នក។
   - **Region**៖ ជ្រើសរើសតំបន់ដែលមានអ្នកប្រើប្រាស់នៅជិតជាងគេ។
   - **Pricing tier**៖ ជ្រើសរើសតម្រាក់តម្លៃដែលសមស្របនឹងតម្រូវការរបស់អ្នក។ អ្នកអាចចាប់ផ្តើមដោយតម្រាក់ Free សម្រាប់សាកល្បង។
6. ចុច **Review + create**។
7. ត្រួតពិនិត្យការកំណត់ និងចុច **Create** ដើម្បីបង្កើតសេវាកម្មស្វែងរក។

## ជំហានទី ៣៖ ចាប់ផ្តើមប្រើប្រាស់ Azure AI Search

1. បន្ទាប់ពីការដំឡើងបានសម្រេច សូមរុករកទៅកាន់សេវាកម្មស្វែងរករបស់អ្នកនៅក្នុង Azure portal។
2. នៅផ្ទាំងមើលទិដ្ឋភាពសេវាកម្មស្វែងរក សូមចម្លង URL ដែលគួរតែមានទម្រង់ `https://<service-name>.search.windows.net`។
3. **(ណែនាំ)** បើកការចូលប្រើដោយគ្មាន key ជាមួយ Microsoft Entra ID (RBAC) ដូចបានបង្ហាញនៅជំហានទី ៤ ខាងក្រោម — មិនត្រូវការចូល key ទេ។ គំរូនៅក្នុងមាតិការនេះបង្កើត/ធ្វើបច្ចុប្បន្នភាព indexes និងផ្ទុកឯកសារ ដែលតម្រូវឲ្យមានតួនាទី **Search Service Contributor** និង **Search Index Data Contributor** (ឬសម្រាប់ authentication ប្រើ key គឺ ត្រូវការចូលprimary admin key — មិនមែន query key)។ គ្រាន់តែ ប្រសិនបើអ្នកមិនអាចប្រើ RBAC បាន សូមបើកផ្ទាំង **Settings > Keys** ហើយចម្លង **primary admin key**។
4. អនុវត្តជំហានក្នុង [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) ដើម្បីបង្កើត index, ផ្ទុកទិន្នន័យ និងធ្វើការស្វែងរក។

## ជំហានទី ៤៖ ប្រើប្រាស់ឧបករណ៍ Azure AI Search

Azure AI Search បញ្ចូលជាមួយឧបករណ៍មួយចំនួនដើម្បីបង្កើនសមត្ថភាពស្វែងរករបស់អ្នក។ អ្នកអាចប្រើ Azure CLI, Python SDK, .NET SDK និងឧបករណ៍ផ្សេងទៀតសម្រាប់ការកំណត់រចនាសម្ព័ន្ធ និងប្រតិបត្តិការលំអិត។

### ប្រើប្រាស់ Azure CLI

1. តំឡើង Azure CLI ដោយអនុវត្តតាមការណែនាំនៅ [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)។
2. ចូលដំណើរការ Azure CLI ដោយប្រើពាក្យបញ្ជា:

   ```bash
   az login
   ```
3. **(ណែនាំ) បើកការចូលប្រើដោយគ្មាន key ជាមួយ Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show មិនមានដែន "endpoint"; សង់ URL ពីឈ្មោះសេវាកម្ម។
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    ជាមួយ RBAC បើក, គំរូ Python និង .NET SDK ខាងក្រោម Authenticate ជាមួយ `DefaultAzureCredential` ដែលប្រើសម័យ `az login` របស់អ្នកក្នុងពេលអភិវឌ្ឍន៍ក្នុងស្រុក — មិនត្រូវការចូល key admin ទេ។ សូមមើល [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)។

4. **(ជំនួស) Authentication​ ដោយប្រើ key** — គ្រាន់តែប្រសិនបើមិនអាចប្រើ RBAC បាន, សូមផ្ទុក key admin ផងដែរ៖

#### ផ្ទុកទាំង endpoint និង API key សម្រាប់ Azure AI Search instance ទៅ environment variables ។

    ```bash
    # zsh/bash
    # az search service show មិនមាន "endpoint" field ទេ; សង់ URL ពីឈ្មោះសេវាកម្ម។
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show មិនមាន "endpoint" field ទេ; សង់ URL ពីឈ្មោះសេវាកម្ម។
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### ប្រើប្រាស់ Python SDK

1. តំឡើងបណ្ណាល័យ Azure Cognitive Search client និង Azure Identity សម្រាប់ Python៖

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ប្រើកូដ Python ខាងក្រោមដើម្បីបង្កើត index និងផ្ទុកឯកសារ៖

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # គ្មានគន្លឹះ (ផ្ដល់អនុសាសន៍): ប្រើអត្តសញ្ញាណ `az login` របស់អ្នកតាមរយៈ Entra ID RBAC។
    # តម្រូវឱ្យមានតួនាទី "Search Service Contributor" និង "Search Index Data Contributor"។
    credential = DefaultAzureCredential()
    # ជំនួយបម្រុង (អត្តសញ្ញាណផ្អែកលើគន្លឹះ):
    # ពី azure.core.credentials នាំចូល AzureKeyCredential
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

### ប្រើប្រាស់ .NET SDK

1. ប្រើពាក្យបញ្ជាខាងក្រោមដើម្បីបង្កើត index និងផ្ទុកឯកសារ៖

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    គំរូ .NET ខាងក្រោមប្រើ `DefaultAzureCredential` ដែលអាចប្រើការចូលរបស់ Azure CLI របស់អ្នកពីពាក្យបញ្ជា `az login` នៅពេលអភិវឌ្ឍន៍ក្នុងស្រុក។

2. នេះគឺជាកូដ .NET នៃ `AzureSearch.cs`៖

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

សម្រាប់ព័ត៌មានលម្អិតបន្ថែម សូមយោងឯកសារទាំងនេះ៖

- [បង្កើតសេវាកម្ម Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [ចាប់ផ្តើមប្រើ Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [ឧបករណ៍ Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## សេចក្ដីសន្និដ្ឋាន

អ្នកបានដំឡើង Azure AI Search ជោគជ័យដោយប្រើ Azure portal និងឧបករណ៍ផ្សំផ្សាយ។ ឥឡូវនេះ អ្នកអាចស្វែងរកលក្ខណៈពិសេសនិងសមត្ថភាពលំអិតនៃ Azure AI Search ដើម្បីបង្កើនដំណោះស្រាយស្វែងរករបស់អ្នក។

សម្រាប់ជំនួយបន្ថែម សូមចូលទៅកាន់ [ឯកសារអំពី Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->