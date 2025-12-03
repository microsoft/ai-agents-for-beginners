<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-12-03T17:28:48+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ml"
}
-->
# Azure AI Search സെറ്റപ്പ് ഗൈഡ്

ഈ ഗൈഡ് ഉപയോഗിച്ച് Azure പോർട്ടൽ വഴി Azure AI Search സജ്ജമാക്കാൻ നിങ്ങളെ സഹായിക്കും. Azure AI Search സേവനം സൃഷ്ടിക്കുകയും ക്രമീകരിക്കുകയും ചെയ്യാൻ താഴെ നൽകിയിരിക്കുന്ന ഘട്ടങ്ങൾ പിന്തുടരുക.

## മുൻ‌വശരൂപങ്ങൾ

തുടങ്ങുന്നതിന് മുമ്പ്, നിങ്ങൾക്ക് താഴെ പറയുന്നവ ഉണ്ടെന്ന് ഉറപ്പാക്കുക:

- ഒരു Azure സബ്സ്ക്രിപ്ഷൻ. നിങ്ങൾക്ക് Azure സബ്സ്ക്രിപ്ഷൻ ഇല്ലെങ്കിൽ, [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ലിങ്ക് വഴി ഒരു സൗജന്യ അക്കൗണ്ട് സൃഷ്ടിക്കാം.

## ഘട്ടം 1: Azure സ്റ്റോറേജ് അക്കൗണ്ട് സൃഷ്ടിക്കുക

1. പുതിയ Azure സ്റ്റോറേജ് അക്കൗണ്ട് സൃഷ്ടിക്കാൻ [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) എന്ന നിർദ്ദേശം പിന്തുടരുക.  
   **NOTE**: സ്റ്റോറേജ് അക്കൗണ്ടിന്റെ തരം Standard General Purpose V2 ആണെന്ന് ഉറപ്പാക്കുക.

## ഘട്ടം 2: Azure AI Search സേവനം സൃഷ്ടിക്കുക

1. [Azure പോർട്ടൽ](https://portal.azure.com/?wt.mc_id=studentamb_258691) ലോഗിൻ ചെയ്യുക.
2. ഇടത് വശത്തെ നാവിഗേഷൻ പാനലിൽ **Create a resource** ക്ലിക്കുചെയ്യുക.
3. തിരയൽ ബോക്സിൽ "Azure AI Search" ടൈപ്പ് ചെയ്യുക, ഫലങ്ങളിൽ നിന്ന് **Azure AI Search** തിരഞ്ഞെടുക്കുക.
4. **Create** ബട്ടൺ ക്ലിക്കുചെയ്യുക.
5. **Basics** ടാബിൽ താഴെ പറയുന്ന വിവരങ്ങൾ നൽകുക:
   - **Subscription**: നിങ്ങളുടെ Azure സബ്സ്ക്രിപ്ഷൻ തിരഞ്ഞെടുക്കുക.
   - **Resource group**: ഒരു പുതിയ റിസോഴ്‌സ് ഗ്രൂപ്പ് സൃഷ്ടിക്കുക അല്ലെങ്കിൽ നിലവിലുള്ളത് തിരഞ്ഞെടുക്കുക.
   - **Resource name**: നിങ്ങളുടെ സെർച്ച് സേവനത്തിന് ഒരു യുണീക് പേര് നൽകുക.
   - **Region**: നിങ്ങളുടെ ഉപയോക്താക്കൾക്ക് ഏറ്റവും അടുത്തുള്ള പ്രദേശം തിരഞ്ഞെടുക്കുക.
   - **Pricing tier**: നിങ്ങളുടെ ആവശ്യങ്ങൾക്കനുസരിച്ച് ഒരു പ്രൈസിംഗ് ടയർ തിരഞ്ഞെടുക്കുക. ടെസ്റ്റിംഗിനായി Free ടയർ ഉപയോഗിച്ച് തുടങ്ങാം.
6. **Review + create** ക്ലിക്കുചെയ്യുക.
7. ക്രമീകരണങ്ങൾ പരിശോധിച്ച് **Create** ക്ലിക്കുചെയ്ത് സെർച്ച് സേവനം സൃഷ്ടിക്കുക.

## ഘട്ടം 3: Azure AI Search ഉപയോഗിച്ച് ആരംഭിക്കുക

1. ഡിപ്ലോയ്മെന്റ് പൂർത്തിയായ ശേഷം, Azure പോർട്ടലിൽ നിങ്ങളുടെ സെർച്ച് സേവനത്തിലേക്ക് നാവിഗേറ്റ് ചെയ്യുക.
2. സെർച്ച് സേവനത്തിന്റെ ഓവർവ്യൂ പാനലിൽ URL കോപ്പി ചെയ്യുക. ഇത് `https://<service-name>.search.windows.net` എന്ന രൂപത്തിൽ കാണപ്പെടും.
3. Settings > Keys പാനലിൽ, query key കോപ്പി ചെയ്യുക.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) പേജിലെ ഘട്ടങ്ങൾ പിന്തുടർന്ന് ഒരു ഇൻഡക്സ് സൃഷ്ടിക്കുക, ഡാറ്റ അപ്‌ലോഡ് ചെയ്യുക, സെർച്ച് ക്വറി നടത്തുക.

## ഘട്ടം 4: Azure AI Search ടൂളുകൾ ഉപയോഗിക്കുക

Azure AI Search വിവിധ ടൂളുകളുമായി സംയോജിപ്പിച്ച് നിങ്ങളുടെ സെർച്ച് കഴിവുകൾ മെച്ചപ്പെടുത്തുന്നു. Azure CLI, Python SDK, .NET SDK എന്നിവ ഉപയോഗിച്ച് ഉയർന്ന തലത്തിലുള്ള ക്രമീകരണങ്ങളും പ്രവർത്തനങ്ങളും നടത്താം.

### Azure CLI ഉപയോഗിച്ച്

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) ലിങ്ക് വഴി Azure CLI ഇൻസ്റ്റാൾ ചെയ്യുക.
2. താഴെ കാണുന്ന കമാൻഡ് ഉപയോഗിച്ച് Azure CLI ലോഗിൻ ചെയ്യുക:

   ```bash
   az login
   ```

3. Azure AI Search ഇൻസ്റ്റൻസിന്റെ എൻഡ്പോയിന്റും API കീയും എൻവയോൺമെന്റ് വേരിയബിളുകളിലേക്ക് സംഭരിക്കുക.

    ```bash
    # zsh/bash
    export AZURE_SEARCH_SERVICE_ENDPOINT=$(az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv)
    export AZURE_SEARCH_API_KEY=$(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # പവർഷെൽ
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = az search service show -g <resource-group> -n <service-name> --query "endpoint" -o tsv
    $env:AZURE_SEARCH_API_KEY = $(az search service admin-key list -g <resource-group> --search-service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK ഉപയോഗിച്ച്

1. Python-നായി Azure Cognitive Search ക്ലയന്റ് ലൈബ്രറി ഇൻസ്റ്റാൾ ചെയ്യുക:

   ```bash
   pip install azure-search-documents
   ```

2. താഴെ കാണുന്ന Python കോഡ് ഉപയോഗിച്ച് ഒരു ഇൻഡക്സ് സൃഷ്ടിക്കുകയും ഡോക്യുമെന്റുകൾ അപ്‌ലോഡ് ചെയ്യുകയും ചെയ്യുക:

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

### .NET SDK ഉപയോഗിച്ച്

1. ഒരു ഇൻഡക്സ് സൃഷ്ടിക്കുകയും ഡോക്യുമെന്റുകൾ അപ്‌ലോഡ് ചെയ്യുകയും ചെയ്യാൻ താഴെ കാണുന്ന കമാൻഡ് പ്രവർത്തിപ്പിക്കുക:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. `AzureSearch.cs` എന്ന .NET കോഡ് ഇതാ:

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

കൂടുതൽ വിശദമായ വിവരങ്ങൾക്ക്, താഴെ പറയുന്ന ഡോക്യുമെന്റേഷൻ കാണുക:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## സമാപനം

Azure പോർട്ടൽ ഉപയോഗിച്ച് Azure AI Search വിജയകരമായി സജ്ജമാക്കി, ടൂളുകൾ സംയോജിപ്പിച്ചു. നിങ്ങളുടെ സെർച്ച് സൊല്യൂഷനുകൾ മെച്ചപ്പെടുത്താൻ Azure AI Search-ന്റെ കൂടുതൽ ഉയർന്ന തലത്തിലുള്ള സവിശേഷതകളും കഴിവുകളും നിങ്ങൾക്ക് ഇപ്പോൾ അന്വേഷിക്കാം.

കൂടുതൽ സഹായത്തിനായി, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) സന്ദർശിക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസത്യവാദം**:  
ഈ രേഖ AI വിവർത്തന സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. കൃത്യതയ്ക്കായി ഞങ്ങൾ ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള മൗലിക രേഖ പ്രാമാണികമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->