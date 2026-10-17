# അസ്യൂർ AI സെർച്ച് സജ്ജീകരിക്കൽ ഗൈഡിൻ

ഈ ഗൈഡ് അസ്യൂർ പോർട്ടൽ ഉപയോഗിച്ച് അസ്യൂർ AI സെർച്ച് സജ്ജീകരിക്കാൻ നിങ്ങളെ സഹായിക്കും. നിങ്ങളുടെ അസ്യൂർ AI സെർച്ച് സേവനം സൃഷ്ടിക്കുകയും ക്രമീകരിക്കുകയും ചെയ്യാൻ താഴെ തന്നിരിക്കുന്ന ഘട്ടങ്ങൾ പിന്തുടരുക.

## മുൻകൂട്ടിയുള്ള ആവശ്യങ്ങൾ

നിങ്ങൾ ആരംഭിക്കുന്നതിന് മുമ്പ്, താഴെ പറയുന്നവ ഉറപ്പാക്കുക:

- ഒരു അസ്യൂർ സബ്സ്ക്രിപ്ഷൻ. നിങ്ങൾക്ക് അസ്യൂർ സബ്സ്ക്രിപ്ഷൻ ഇല്ലെങ്കിൽ, [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ൽ സൗജന്യ അക്കൗണ്ട് സൃഷ്ടിക്കാവുന്നതാണ്.

## ഘട്ടം 1: അസ്യൂർ സ്റ്റോറേജ് അക്കൗണ്ട് സൃഷ്ടിക്കുക

1. ഈ നിർദ്ദേശം പിന്തുടരുക, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) എന്ന ലിങ്കിലേക്കുപോയി പുതിയ അസ്യൂർ സ്റ്റോറേജ് അക്കൗണ്ട് സൃഷ്ടിക്കുക.
   **കുറിപ്പ്**: സ്റ്റോറേജ് അക്കൗണ്ടിന്റെ തരം Standard General Purpose V2 ആണെന്ന് ഉറപ്പ് വരുത്തുക.

## ഘട്ടം 2: അസ്യൂർ AI സെർച്ച് സേവനം സൃഷ്ടിക്കുക

1. [അസ്യൂർ പോർട്ടൽ](https://portal.azure.com/?wt.mc_id=studentamb_258691) ൽ സൈൻ ഇൻ ചെയ്യുക.
2. ഇടത്തരം ഡാഷ്‌ബോർഡിലെ സൈഡ് നാവിഗേഷൻ പാനിൽ, **Create a resource** ക്ലിക്കുചെയ്യുക.
3. സെർച്ലൊപ്പിൽ "Azure AI Search" എന്ന് ടൈപ്പ് ചെയ്ത് ഫലം നിന്നുള്ള ലിസ്റ്റിൽ നിന്ന് **Azure AI Search** തിരഞ്ഞെടുക്കുക.
4. **Create** ബട്ടൺ ക്ലിക്ക് ചെയ്യുക.
5. **Basics** ടാബിൽ താഴെ പറയുന്ന വിവരങ്ങൾ നൽകിയതിന് ശേഷം:
   - **Subscription**: നിങ്ങളുടെ അസ്യൂർ സബ്സ്ക്രിപ്ഷൻ തിരഞ്ഞെടുക്കുക.
   - **Resource group**: പുതിയ റിസോഴ്‌സ് ഗ്രൂപ്പ് സൃഷ്ടിക്കുക അല്ലെങ്കിൽ നിലവിലുള്ളത് തിരഞ്ഞെടുക്കുക.
   - **Resource name**: നിങ്ങളുടെ സെർച്ച് സേവനത്തിന് ഒരു വ്യത്യസ്തമായ പേരൊന്ന് നൽകുക.
   - **Region**: നിങ്ങളുടെ ഉപയോക്താക്കൾക്ക് ഏറ്റവും അടുത്ത പ്രദേശം തിരഞ്ഞെടുക്കുക.
   - **Pricing tier**: നിങ്ങളുടെ ആവശ്യങ്ങൾക്കനുസരിച്ചുള്ള പ്രൈസിംഗ് ടിയർ തിരഞ്ഞെടുക്കുക. പരീക്ഷണത്തിനായി സൗജന്യ ടിയർ ഉപയോഗിക്കാം.
6. **Review + create** ക്ലിക്ക് ചെയ്യുക.
7. ക്രമീകരണങ്ങൾ പരിശോധിച്ച് **Create** ക്ലിക്ക് ചെയ്ത് സെർച്ച് സേവനം സൃഷ്ടിക്കുക.

## ഘട്ടം 3: അസ്യൂർ AI സെർച്ച് തുടങ്ങുക

1. ഡിപ്ലോയ്മെന്റ് പൂർത്തിയായതിനു ശേഷം, അസ്യൂർ പോർട്ടലിൽ നിങ്ങളുടെ സെർച്ച് സേവനത്തിലേക്ക് പോകുക.
2. സെർച്ച് സേവനത്തിന്റെ അവലോകന പാനിൽ URL കോപ്പി ചെയ്യുക. ഇത് `https://<service-name>.search.windows.net` എന്ന രൂപത്തിലായിരിക്കും.
3. **(ശുപാർശചെയ്യുന്നു)** കീ ഇല്ലാത്ത ആക്സസ് മൈക്രോസോഫ്റ്റ് എന്‍ട്ര ID (RBAC) ഉപയോഗിച്ച് സജ്ജീകരിക്കുക, താഴെ 4-ാം ഘട്ടത്തിൽ കാണുന്നപോലെ — കീ ആവശ്യമില്ല. ഈ ഗൈഡിലുള്ള ഉദാഹരണങ്ങൾ ഇൻഡക്സുകൾ സൃഷ്ടിക്കുകയും അപ്‌ലോഡ് ചെയ്യുകയും ചെയ്യുന്നു, ഇത് **Search Service Contributor** અને **Search Index Data Contributor** റോളുകൾ ആവശ്യമാണ് (അല്ലെങ്കിൽ അതിന്റെ കീ അടിസ്ഥാനAuth വേണ്ടി, **primary admin key** — query key അല്ല). നിങ്ങൾക്ക് RBAC ഉപയോഗിക്കാനാകാതെപോകുമ്പോഴാകും**, **Settings > Keys** പാനിലേക്ക് പോവുകയും **primary admin key** കോപ്പി ചെയ്യുകയും ചെയ്യുക.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) പേജിലെ ഘട്ടങ്ങൾ അനുസരിച്ച് ഒരു ഇൻഡക്സ് സൃഷ്ടിക്കുകയും ഡാറ്റ അപ്‌ലോഡ് ചെയ്യുകയും സെർച്ച് നടത്തുകയും ചെയ്യുക.

## ഘട്ടം 4: അസ്യൂർ AI സെർച്ച് ഉപകരണങ്ങൾ ഉപയോഗിക്കുക

അസ്യൂർ AI സെർച്ച് വിവിധ ഉപകരണങ്ങളുമായി ഇന്റഗ്രേറ്റ് ചെയ്ത് നിങ്ങളുടെ സെർച്ച് ശേഷികൾ മെച്ചപ്പെടുത്തുന്നു. അസ്യൂർ CLI, Python SDK, .NET SDK മുതലായവ ഉപയോഗിച്ച് പ്രഗത്ഭമായ ക്രമീകരണങ്ങൾക്കും പ്രവർത്തനങ്ങൾക്കും ഉപയോഗിക്കാം.

### അസ്യൂർ CLI ഉപയോഗിച്ചു

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) ലിങ്കിലെ നിർദ്ദേശങ്ങൾ പിന്തുടർന്നു അസ്യൂർ CLI ഇൻസ്റ്റാൾ ചെയ്യുക.
2. താഴെ കാണിച്ച കമാൻഡ് ഉപയോഗിച്ച് അസ്യൂർ CLI-യിൽ സൈൻ ഇൻ ചെയ്യുക:

   ```bash
   az login
   ```
3. **(ശുപാർശ) കീ ഇല്ലാത്ത ആക്സസ് മൈക്രോസോഫ്റ്റ് എന്‍ട്ര ID (RBAC) ഉപയോഗിച്ച് സജ്ജീകരിക്കുക:** 

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show എന്നതിന് "endpoint" എന്ന ഫീൽഡ് ഇല്ല; സർവീസ് പേരിൽ നിന്നാണ് URL നിർമ്മിക്കുന്നത്.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC സജ്ജമാക്കിയാൽ, Python, .NET SDK ഉദാഹരണങ്ങൾ താഴെ കാണുന്ന `DefaultAzureCredential` ഉപയോഗിച്ച് പ്രാദേശിക വികസനത്തിനിടെ നിങ്ങളുടെ `az login` സെഷൻ ഉപയോഗിച്ച് പ്രാമാണീകരണം നടത്തും — അഡ്മിൻ കീ ആവശ്യമില്ല. [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) കാണുക.

4. **(ഫാൾബാക്ക്) കീ അടിസ്ഥാനAuth** — RBAC ഉപയോഗിക്കാൻ കഴിയാതെപോവുകയാണെങ്കിൽ, അഡ്മിൻ കീ സൂക്ഷിക്കുക:

#### അസ്യൂർ AI സെർച്ച് ഇൻസ്റ്റൻസിനായി എൻഡ്പോയിന്റും API കിയും പരിസ്ഥിതി ചാരങ്ങളായി സൂക്ഷിക്കുക.

    ```bash
    # zsh/bash
    # az search service show-ന് "endpoint" ഫീൽഡ് ഇല്ല; സർവീസ് പേരിൽ നിന്നു URL നിർമ്മിക്കുക.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show-ന് "endpoint" ഫീൽഡ് ഇല്ല; സർവീസ് പേരിൽ നിന്നു URL നിർമ്മിക്കുക.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK ഉപയോഗിച്ചു

1. അസ്യൂർ കോഗ്‌നിറ്റീവ് സെർച്ച് ക്ലയന്റ് ലൈബ്രറി അതുപോലെ Python-ക്കുള്ള അസ്യൂർ ഐഡന്റിറ്റി ഇൻസ്റ്റാൾ ചെയ്യുക:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ഇൻഡക്സ് സൃഷ്ടിച്ച് രേഖകൾ അപ്‌ലോഡ് ചെയ്യാൻ താഴെ പറയുന്ന Python കോഡ് ഉപയോഗിക്കുക:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # കീലെസ് ( ശിപാർശചെയ്തത് ): നിങ്ങളുടെ `az login` തിരിച്ചറിയൽ Entra ID RBAC വഴി ഉപയോഗിക്കും.
    # "സേർക്ക്സ് സർവീസ് കോൺട്രിബ്യൂട്ടർ"നും "സേർക്ക്സ് ഇൻഡക്സ് ഡേറ്റ കോൺട്രിബ്യൂട്ടർ" റോളുകളും ആവശ്യമാണ്.
    credential = DefaultAzureCredential()
    # ഫോള്ബാക്ക് (കീ അധിഷ്ഠിത ഓത്തന്റിക്കേഷൻ):
    # azure.core.credentials എന്നയിടത്ത് നിന്ന് AzureKeyCredential ഇറക്കുമതി ചെയ്യുക
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

### .NET SDK ഉപയോഗിച്ചു

1. ഇൻഡക്സ് സൃഷ്ടിക്കുകയും രേഖകൾ അപ്‌ലോഡ് ചെയ്യുകയും ചെയ്യാൻ അടുത്ത കമാൻഡ് റൺ ചെയ്യുക:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    താഴെ കാണുന്ന .NET ഉദാഹരണം `DefaultAzureCredential` ഉപയോഗിക്കുന്നു, ഇത് പ്രാദേശിക വികസനത്തിനിടെ `az login` വഴി അസ്യൂർ CLI സൈൻ ഇൻ കാണിച്ച് ഉപയോഗിക്കാമെന്ന്.

2. ഇതാ `AzureSearch.cs` യുടെ .NET കോഡ്:

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

കൂടുതൽ വിശദമായ വിവരങ്ങൾക്കായി, താഴെ നൽകിയുള്ള ഡോക്യുമെന്റേഷനുകൾ കാണുക:

- [അസ്യൂർ കോഗ്‌നിറ്റീവ് സെർച്ച് സേവനം സൃഷ്ടിക്കുക](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [അസ്യൂർ കോഗ്‌നിറ്റീവ് സെർച്ച് തുടങ്ങുക](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [അസ്യൂർ AI സെർച്ച് ഉപകരണങ്ങൾ](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## നിഗമനം

അസ്യൂർ പോർട്ടൽ ഉപയോഗിച്ച് അസ്യൂർ AI സെർച്ച് വിജയകരമായി സജ്ജീകരിച്ച് ഉപകരണങ്ങളും ഇന്റഗ്രേറ്റ് ചെയ്‌തു. ഇനി മെച്ചപ്പെട്ട സെർച്ച് പരിഹാരങ്ങൾക്കായി അസ്യൂർ AI സെർച്ചിന്റെ കൂടുതൽ അതിവിശിഷ്ട സവിശേഷതകളും ശേഷികളും പരിശോധിക്കാം.

കൂടുതൽ സഹായത്തിന്, [അസ്യൂർ കോഗ്‌നിറ്റീവ് സെർച്ച് ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) സന്ദർശിക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->