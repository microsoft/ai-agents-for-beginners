# មគ្គុទេសក៍ដំឡើង Azure AI Search

មគ្គុទេសក៍នេះនឹងជួយអ្នកដំឡើង Azure AI Search ដោយប្រើទ្វារ Azure ។ អនុវត្តជំហានខាងក្រោម ដើម្បីបង្កើត និងកំណត់រចនាសម្ព័ន្ធសេវាកម្ម Azure AI Search របស់អ្នក។

## លក្ខខណ្ឌមុនដំនើរការ

មុនចាប់ផ្តើម សូមធានាថាអ្នកមានអ្វីខ្លះខាងក្រោម៖

- មានការជាវ Azure មួយ។ ប្រសិនបើអ្នកមិនមានការជាវ Azure សូមបង្កើតគណនីដោយឥតគិតថ្លៃនៅ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)។

## ជំហានទី 1: បង្កើតគណនីផ្ទុកទិន្នន័យ Azure

1. អនុវត្តតាមការណែនាំនេះ [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) ដើម្បីបង្កើតគណនីផ្ទុកទិន្នន័យ Azure ថ្មីមួយ។
   **កំណត់ចំណាំ**៖ សូមប្រាកដថាប្រភេទគណនីផ្ទុកទិន្នន័យគឺ Standard General Purpose V2។

## ជំហានទី 2: បង្កើតសេវាកម្ម Azure AI Search

1. ចូលទៅកាន់ [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691)។
2. នៅផ្នែកផ្ទាំងរុករកខាងឆ្វេង ចុចលើ **Create a resource**។
3. នៅប្រអប់ស្វែងរក វាយ "Azure AI Search" ហើយជ្រើស **Azure AI Search** ពីបញ្ជីលទ្ធផល។
4. ចុចប៊ូតុង **Create**។
5. នៅផ្ទាំង **Basics** ផ្តល់ពត៌មានខាងក្រោម៖
   - **Subscription**៖ ជ្រើសការជាវ Azure របស់អ្នក។
   - **Resource group**៖ បង្កើតក្រុមធនធានថ្មី ឬជ្រើសក្រុមដែលមានរួច។ 
   - **Resource name**៖ បញ្ចូលឈ្មោះតែមួយសម្រាប់សេវាកម្មស្វែងរករបស់អ្នក។
   - **Region**៖ ជ្រើសតំបន់ដែលនៅជិតអ្នកប្រើប្រាស់បំផុត។
   - **Pricing tier**៖ ជ្រើសថ្នាក់តម្លៃដែលសមរម្យនឹងតម្រូវការ។ អ្នកអាចចាប់ផ្តើមជាជំនាន់ឥតគិតថ្លៃសម្រាប់ការធ្វើតេស្ត។
6. ចុច **Review + create**។
7. ពិនិត្យការកំណត់ ហើយចុច **Create** ដើម្បីបង្កើតសេវាកម្មស្វែងរក។

## ជំហានទី 3: ចាប់ផ្តើមប្រើ Azure AI Search

1. ពេលបញ្ចប់ដំឡើង សូមទៅកាន់សេវាកម្មស្វែងរករបស់អ្នកនៅលើទ្វារ Azure។
2. នៅផ្ទាំងសង្ខេបសេវាកម្មស្វែងរក ចម្លង URL ។ វាគួរតែមានរូបរាងជា `https://<service-name>.search.windows.net`។
3. **(ផ្តល់អនុសាសន៍)** បើកការចូលប្រើដោយគ្មានសោជាមួយ Microsoft Entra ID (RBAC) ដូចបង្ហាញនៅជំហានទី 4 ខាងក្រោម — មិនត្រូវការសោឡើងវិញទេ។ តំណាងទិន្នន័យក្នុងមគ្គុទេសក៍នេះបង្កើត/ធ្វើបច្ចុប្បន្នភាពវិស័យ និងអាប់ឡូដឯកសារ ដែលត្រូវការនាទី **Search Service Contributor** និង **Search Index Data Contributor** (ឬ សម្រាប់ការផ្ទៀងផ្ទាត់ដោយសោ អ្នកត្រូវការសោគ្រប់គ្រងសំខាន់ - primary admin key — មិនមែនសោស្វែងរក​ទេ)។ បើអ្នកមិនអាចប្រើ RBAC បាន គ្រាន់តែបើកផ្ទាំង **Settings > Keys** ហើយចម្លងសោគ្រប់គ្រងសំខាន់។
4. អនុវត្តជំហាននៅក្នុងទំព័រ [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) ដើម្បីបង្កើតវិស័យ អាប់ឡូដទិន្នន័យ និងអនុវត្តការស្វែងរក។

## ជំហានទី 4: ប្រើឧបករណ៍ Azure AI Search

Azure AI Search សំរុងជាមួយឧបករណ៍ច្រើនដើម្បីបង្កើនសមត្ថភាពស្វែងរករបស់អ្នក។ អ្នកអាចប្រើ Azure CLI, Python SDK, .NET SDK និងឧបករណ៍ផ្សេងទៀតសម្រាប់ការកំណត់ និងបំពេញបន្ថែមកម្រិតខ្ពស់។

### ប្រើ Azure CLI

1. ដំឡើង Azure CLI ដោយអនុវត្តតាមការណែនាំនៅ [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)។
2. ចូលទៅកាន់ Azure CLI ដោយប្រើពាក្យបញ្ជា៖

   ```bash
   az login
   ```
3. **(ផ្តល់អនុសាសន៍) បើកការចូលប្រើគ្មានសោជាមួយ Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # សេវាកម្មស្វែងរក az បង្ហាញគ្មានចន្លោះ "endpoint"; បង្កើត URL ពីឈ្មោះសេវាកម្ម។
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    ជាមួយ RBAC ដែលបានបើក ប្រើលំនាំឧទាហរណ៍ Python និង .NET SDK ខាងក្រោម អាក្រក់​សក្ដានុពល `DefaultAzureCredential` ដែលប្រើករណី `az login` សម្រាប់ការអភិវឌ្ឍន៍ក្នុងកន្លែង — មិនត្រូវការសោគ្រប់គ្រងទេ។ សូមមើល [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)។

4. **(ជំនួស) ការផ្ទៀងផ្ទាត់ដោយសោ** — គ្រាន់តែបើអ្នកមិនអាចប្រើ RBAC ត្រូវរក្សាទុកសោគ្រប់គ្រងផងដែរ៖

#### រក្សាទុកទាំងចំណុចបញ្ចប់និងសោ API សម្រាប់យន្តការជាមួយ Azure AI Search ទៅក្នុង environment variables។

    ```bash
    # zsh/bash
    # az search service show មិនមានពត៌មាន "endpoint"; សាងសង់ URL ពីឈ្មោះសេវា។
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show មិនមានពត៌មាន "endpoint"; សាងសង់ URL ពីឈ្មោះសេវា។
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### ប្រើ Python SDK

1. ដំឡើងបណ្ណាល័យ Azure Cognitive Search Client និង Azure Identity សម្រាប់ Python៖

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ប្រើកូដ Python ខាងក្រោមដើម្បីបង្កើតវិស័យ និងអាប់ឡូដឯកសារ៖

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # គ្មានកូនសោ (ផ្ដល់អនុសាសន៍): ប្រើអត្តសញ្ញាណ `az login` របស់អ្នកតាមរយៈ Entra ID RBAC។
    # ត្រូវការតួនាទី "អ្នករួមចំណែកសេវាកម្មស្វែងរក" និង "អ្នករួមចំណែកទិន្នន័យស្វែងរកផ្សេងទៀត"។
    credential = DefaultAzureCredential()
    # វិជ្ជមានជំនួស (ការផ្ទៀងផ្ទាត់ដោយកូនសោ):
    # ពី azure.core.credentials នាំចូល AzureKeyCredential
    # ពាក្យសម្ងាត់ = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

### ប្រើ .NET SDK

1. រត់ពាក្យបញ្ជាខាងក្រោមដើម្បីបង្កើតវិស័យ និងអាប់ឡូដឯកសារ៖

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    ឧទាហរណ៍ .NET ខាងក្រោមប្រើឧទាហរណ៍ `DefaultAzureCredential` ដែលអាចប្រើ Azure CLI sign-in របស់អ្នកពី `az login` នៅពេលអភិវឌ្ឍន៍ក្នុងកន្លែង។

2. នេះគឺជាកូដ .NET របស់ `AzureSearch.cs`៖

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

សម្រាប់ព័ត៌មានលម្អិតបន្ថែម សូមយោងឯកសារខាងក្រោម៖

- [បង្កើតសេវាកម្ម Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [ចាប់ផ្តើមជាមួយ Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [ឧបករណ៍ Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## សេចក្តីសន្និដ្ឋាន

អ្នកបានដំឡើង Azure AI Search ជោគជ័យ ដោយប្រើ Azure portal និងឧបករណ៍ផ្សំរួម។ ឥឡូវនេះ អ្នកអាចស្រាវជ្រាវលក្ខណៈពិសេសនិងសមត្ថភាពបន្ថែមរបស់ Azure AI Search ដើម្បីបង្កើនដំណោះស្រាយស្វែងរករបស់អ្នក។

សម្រាប់ជំនួយបន្ថែម សូមចូលទៅកាន់ [ឯកសារ Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->