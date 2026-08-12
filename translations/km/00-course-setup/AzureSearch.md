# Azure AI Search Setup Guide

ផែនការណ៍នេះនឹងជួយអ្នកក្នុងការតម្លើង Azure AI Search ដោយប្រើផតថល Azure។ សូមអនុវត្តដំណាក់កាលខាងក្រោម ដើម្បីបង្កើត និងកំណត់រចនាសម្ព័ន្ធសេវាកម្ម Azure AI Search របស់អ្នក។

## Prerequisites

មុននឹងចាប់ផ្តើម សូមប្រាកដថាអ្នកមានរឿងខាងក្រោម:

- មានការចុះឈ្មោះជាមួយ Azure។ ប្រសិនបើអ្នកមិនទាន់មានការចុះឈ្មោះ Azure ទេ អ្នកអាចបង្កើតគណនីឥតគិតថ្លៃនៅ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)។

## Step 1: Create an Azure Storage Account

1. អនុវត្តតាមសេចក្តីណែនាំនេះ, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), ដើម្បីបង្កើតគណនី Azure Storage ថ្មី។
   **សម្គាល់**: សូមប្រាកដថាប្រភេទនៃគណនីផ្ទុកគឺ Standard General Purpose V2។

## Step 2: Create an Azure AI Search Service

1. ចូលទៅកាន់ [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691)។
2. នៅផ្នែកផ្លូវចរណ៍ខាងឆ្វេង ចុចលើ **Create a resource**។
3. នៅលើប្រអប់ស្វែងរក អ្នកនៅត្រូវវាយ "Azure AI Search" និងជ្រើស **Azure AI Search** ចេញពីបញ្ជីលទ្ធផល។
4. ចុចប៊ូតុង **Create**។
5. នៅក្នុងផ្ទាំង **Basics** សូមផ្តល់ព័ត៌មានដូចខាងក្រោម។
   - **Subscription**: ជ្រើសរើសការចុះឈ្មោះ Azure របស់អ្នក។
   - **Resource group**: បង្កើតក្រុមធនធានថ្មី ឬជ្រើសរើសមួយដែលមានរួចស្រេច។
   - **Resource name**: បញ្ចូលឈ្មោះមួយឲ្យមានតែមួយសម្រាប់សេវាកម្មស្វែងរករបស់អ្នក។
   - **Region**: ជ្រើសតំបន់ដែលនៅជិតអ្នកប្រើប្រាស់របស់អ្នកបំផុត។
   - **Pricing tier**: ជ្រើសជាន់ថ្លៃដែលសមស្របទៅនឹងតម្រូវការរបស់អ្នក។ អ្នកអាចចាប់ផ្តើមដោយជាន់ Free សម្រាប់ការធ្វើតេស្ត។
6. ចុច **Review + create**។
7. ពិនិត្យការកំណត់ ហើយចុច **Create** ដើម្បីបង្កើតសេវាកម្មស្វែងរក។

## Step 3: Get Started with Azure AI Search

1. បន្ទាប់ពីការដាក់ពាក្យបានសម្រេច សូមទៅកាន់សេវាកម្មស្វែងរករបស់អ្នកក្នុងផតថល Azure។
2. នៅក្នុងផ្ទាំងទិដ្ឋភាពទូទៅរបស់សេវាកម្មស្វែងរក សូមចម្លង URL។ វាគួរតែមានទ្រង់ទ្រាយដូចជា `https://<service-name>.search.windows.net`។
3. នៅក្នុង Settings > Keys pane សូមចម្លង query key។
4. អនុវត្តតាមដំណាក់កាលក្នុងទំព័រ [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) ដើម្បីបង្កើត index បញ្ចូលទិន្នន័យ និងអនុវត្តការស្វែងរក។

## Step 4: Use Azure AI Search Tools

Azure AI Search រួមបញ្ចូលជាមួយឧបករណ៍ផ្សេងៗ ដើម្បីពង្រឹងសមត្ថភាពស្វែងរករបស់អ្នក។ អ្នកអាចប្រើ Azure CLI, Python SDK, .NET SDK និងឧបករណ៍ផ្សេងទៀតសម្រាប់ការកំណត់កម្រិតខ្ពស់ និងប្រតិបត្តិការជ្រៅ។

### Using Azure CLI

1. តម្លើង Azure CLI ដោយអនុវត្តតាមការណែនាំនៅ [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691)។
2. ចូលទៅ Azure CLI ដោយប្រើពាក្យបញ្ជា:

   ```bash
   az login
   ```

3. រក្សាទុក endpoint និង API key សម្រាប់ instance Azure AI Search ទៅជាផ្លាស់ប្ដូរបរិយាកាស (environment variables)។

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

### Using Python SDK

1. តម្លើងបណ្ណាល័យ Azure Cognitive Search សម្រាប់ Python:

   ```bash
   pip install azure-search-documents
   ```

2. ប្រើកូដ Python ខាងក្រោម ដើម្បីបង្កើត index និងបញ្ចូលឯកសារ:

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

### Using .NET SDK

1. ដំណើរការពាក្យបញ្ជាខាងក្រោម ដើម្បីបង្កើត index និងបញ្ចូលឯកសារ:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. នេះគឺជា​កូដ .NET របស់ `AzureSearch.cs`:

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

សម្រាប់ព័ត៌មានលម្អិតបន្ថែម សូមយោងឯកសារ៖

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## Conclusion

អ្នកបានតម្លើង Azure AI Search ដោយជោគជ័យប្រើផតថល Azure និងឧបករណ៍រួមផ្សំ។ ឥឡូវនេះ អ្នកអាចស្វែងយល់លើលក្ខណៈពិសេស និងសមត្ថភាពកម្រិតខ្ពស់របស់ Azure AI Search ដើម្បីបង្កើនដំណោះស្រាយស្វែងរករបស់អ្នក។

សម្រាប់ជំនួយបន្ថែម សូមចូលទៅកាន់ [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការមិនទទួលខុសត្រូវ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែដោយប្រព័ន្ធ AI [Co-op Translator](https://github.com/Azure/co-op-translator). ខណៈពេលយើងខិតខំសម្រាប់ភាពត្រឹមត្រូវ សូមចំណាំថា ការបកប្រែដោយស្វ័យប្រវត្តិនេះអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមក្នុងភាសាមូលដ្ឋានគួរត្រូវបានគេយកថាជាប្រភពដែលអាចទុកចិត្តបាន។ សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ គេផ្តល់អនុសាសន៍ឲ្យប្រើសេវាកម្មបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកន័យខុសណាមួយ ដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->