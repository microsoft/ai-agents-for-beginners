# មេរៀនដាក់កំណត់ Azure AI Search

មេរៀននេះជួយអ្នកដាក់កំណត់ Azure AI Search ដោយប្រើទ្វារគ្រប់គ្រង Azure។ សូមអនុវត្តជំហានខាងក្រោមដើម្បីបង្កើតនិងកំណត់រចនាសម្ព័ន្ធសេវាកម្ម Azure AI Search របស់អ្នក។

## លក្ខខណ្ឌមុនពេលចាប់ផ្តើម

មុនចាប់ផ្តើម សូមប្រាកដថាអ្នកមានរបស់ខាងក្រោម៖

- រក្សាសុពលភាព Azure។ ប្រសិនបើអ្នកគ្មានសុពលភាព Azure អ្នកអាចបង្កើតគណនីឥតគិតថ្លៃនៅ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)។

## ជំហានទី 1: បង្កើតគណនីផ្ទុក Azure Storage Account

1. អនុវត្តតាមការណែនាំនេះ [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) ដើម្បីបង្កើតគណនីផ្ទុក Azure ថ្មី។
   **ចំណាំ**៖ សូមប្រាកដថាប្រភេទគណនីផ្ទុកគឺជា Standard General Purpose V2។

## ជំហានទី 2: បង្កើតសេវាកម្ម Azure AI Search

1. ចូលទៅកាន់ [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691)។
2. នៅផ្ទៃបវេសនាក្ស(left-hand navigation pane), ចុចលើ **Create a resource**។
3. នៅប្រអប់ស្វែងរក បញ្ចូលពាក្យ "Azure AI Search" ហើយជ្រើស **Azure AI Search** ពីបញ្ជីលទ្ធផល។
4. ចុចប៊ូតុង **Create**។
5. នៅផ្ទាំង **Basics**, បំពេញព័ត៌មានដូចខាងក្រោម៖
   - **Subscription**: ជ្រើសសុពលភាព Azure របស់អ្នក។
   - **Resource group**: បង្កើតក្រុមធនធានថ្មី ឬជ្រើសក្រុមធនធានដែលមានរួច។
   - **Resource name**: បញ្ចូលឈ្មោះតែមួយសម្រាប់សេវាកម្មស្វែងរករបស់អ្នក។
   - **Region**: ជ្រើសតំបន់ដែលនៅជិតអ្នកប្រើប្រាស់បំផុត។
   - **Pricing tier**: ជ្រើសតម្លៃសេវាកម្មដែលសមរម្យនឹងតម្រូវការរបស់អ្នក។ អ្នកអាចចាប់ផ្តើមជាមួយតម្លៃឥតគិតថ្លៃសម្រាប់ការប្រមូលផ្តុំ។
6. ចុច **Review + create**។
7. ពិនិត្យមើលការកំណត់ និងចុច **Create** ដើម្បីបង្កើតសេវាកម្មស្វែងរក។

## ជំហានទី 3: ចាប់ផ្តើមជាមួយ Azure AI Search

1. បន្ទាប់ពីការដាក់ចេញបានសម្រេច អ្នកអាចចូលទៅកាន់សេវាកម្មស្វែងរករបស់អ្នកនៅក្នុងទ្វារគ្រប់គ្រង Azure។
2. នៅផ្ទាំងពិពណ៌នាសេវាកម្មស្វែងរក ប្រមូល URL មួយ។ វាគួរតែមានរូបរាងដូចជា `https://<service-name>.search.windows.net`។
3. **(ផ្តល់អនុសាសន៍)** បើកការចូលរួមដោយគ្មានកូនសោជាមួយ Microsoft Entra ID (RBAC) ដូចបង្ហាញនៅជំហានទី 4 ខាងក្រោម—មិនចាំបាច់ប្រើកូនសោទេ។ ឧទាហរណ៍ក្នុងមេរៀននេះបង្កើត/បន្ទាន់សម័យព័ត៌មាន និងបញ្ចូលឯកសារ ដែលតម្រូវឲ្យមានតួនាទី **Search Service Contributor** និង **Search Index Data Contributor** (ឬសម្រាប់ការផ្ទៀងផ្ទាត់ដោយកូនសោ, ប្រើ **primary admin key** — មិនមែន query key)។ ប្រសិនបើអ្នកមិនអាចប្រើ RBAC, បើកផ្ទាំង **Settings > Keys** ហើយចម្លង **primary admin key**។
4. អនុវត្តតាមជំហានដែលមាននៅក្នុងទំព័រ [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) ដើម្បីបង្កើតសន្ទស្សន៍ (index), បញ្ចូលទិន្នន័យ និងអនុវត្តការស្វែងរក។

## ជំហានទី 4: ប្រើឧបករណ៍ Azure AI Search

Azure AI Search ស្របទ្រង់ទ្រាយជាមួយឧបករណ៍ផ្សេងៗដើម្បីបង្កើនសមត្ថភាពស្វែងរករបស់អ្នក។ អ្នកអាចប្រើ Azure CLI, Python SDK, .NET SDK និងឧបករណ៍ផ្សេងៗសម្រាប់ការកំណត់រចនាសម្ព័ន្ធច្រើនជាងនេះ និងប្រតិបត្តិការរបស់អ្នក។

### ការប្រើប្រាស់ Azure CLI

1. តំឡើង Azure CLI ដោយអនុវត្តតាមការណែនាំនៅ [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)។
2. ចូលទៅក្នុង Azure CLI ដោយប្រើពាក្យបញ្ជា៖

   ```bash
   az login
   ```
3. **(ផ្តល់អនុសាសន៍) បើកការចូលរួមដោយគ្មានកូនសោជាមួយ Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    ជាមួយការបើក RBAC, ឧទាហរណ៍ Python និង .NET SDK ខាងក្រោមផ្ទៀងផ្ទាត់ដោយប្រើ `DefaultAzureCredential` ដែលប្រើសម័យ `az login` របស់អ្នកនៅពេលអភិវឌ្ឍន៍ក្នុងស្រុក — មិនចាំបាច់មានកូនសោរដ្ឋបាលទេ។ សូមមើល [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)។

4. **(ជំនួស) ការផ្ទៀងផ្ទាត់ដោយកូនសោ** — មានតែប្រសិនបើអ្នកមិនអាចប្រើ RBAC, រក្សាទុកកូនសោរដ្ឋបាលផងដែរ៖

#### រក្សាទុកទាំងអ័ព្ទទ៏ចូល និងកូនសោ API សម្រាប់ស្ថាប័ន Azure AI Search ទៅក្នុងអថេរបរិស្ថាន។

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

### ការប្រើប្រាស់ Python SDK

1. តំឡើងបណ្ណាល័យ Azure Cognitive Search client និង Azure Identity សម្រាប់ Python៖

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ប្រើកូដ Python ខាងក្រោមដើម្បីបង្កើតសន្ទស្សន៍ និងបញ្ចូលឯកសារ៖

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

### ការប្រើប្រាស់ .NET SDK

1. ប្រតិបត្តិពាក្យបញ្ជាខាងក្រោមដើម្បីបង្កើតសន្ទស្សន៍ និងបញ្ចូលឯកសារ៖

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    ឧទាហរណ៍ .NET ខាងក្រោមប្រើ `DefaultAzureCredential` ដែលអាចប្រើការចូលគណនី Azure CLI របស់អ្នកពី `az login` នៅពេលអភិវឌ្ឍនៅក្នុងស្រុក។

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

សម្រាប់ព័ត៌មានលម្អិតបន្ថែម សូមយោងឯកសារខាងក្រោម៖

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## សេចក្ដីសន្និដ្ឋាន

អ្នកបានដាក់កំណត់ Azure AI Search ដោយជោគជ័យប្រើទ្វារគ្រប់គ្រង Azure និងឧបករណ៍ផ្សេងៗរួចរាល់។ ឥឡូវនេះ អ្នកអាចស្វែងយល់សមត្ថភាពលម្អិត និងលក្ខណៈពិសេសធម្មច្រើនបន្ថែមរបស់ Azure AI Search ដើម្បីបង្កើនដំណោះស្រាយស្វែងរករបស់អ្នក។

សម្រាប់ជំនួយបន្ថែម សូមចូលទៅកាន់ [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->