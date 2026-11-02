# ആസ്യൂർ AI സെർച്ച് സെറ്റ് അപ്പ് ഗൈഡ്

ഈ ഗൈഡ് ആസ്യൂർ പോർട്ടൽ ഉപയോഗിച്ച് ആസ്യൂർ AI സെർച്ച് സജ്ജമാക്കുന്നതിൽ സഹായിക്കും. താഴെ നൽകിയിരിക്കുന്ന ദശകഷണങ്ങൾ പിന്തുടർന്ന് നിങ്ങളുടെ ആസ്യൂർ AI സെർച്ച് സേവനം സൃഷ്ടിച്ച് കോൺഫിഗർ ചെയ്യുക.

## മുൻപുപോസണം

ആരംഭിക്കുന്നതിന് മുമ്പ്, നിങ്ങൾക്ക് താഴെപ്പറയുന്നവ ഉണ്ടെന്ന് ഉറപ്പാക്കുക:

- ഒരു ആസ്യൂർ സബ്സ്ക്രിപ്ഷൻ. നിങ്ങൾക്ക് ആസ്യൂർ സബ്സ്ക്രിപ്ഷൻ ഇല്ലെങ്കിൽ, നിങ്ങൾക്ക് [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ൽ സൗജന്യ അക്കൗണ്ട് സൃഷ്ടിക്കാം.

## ഘട്ടം 1: ആസ്യൂർ സ്റ്റോറേജ് അക്കൗണ്ട് സൃഷ്ടിക്കുക

1. ഈ നിർദ്ദേശം പിന്തുടരുക, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), പുതിയ ആസ്യൂർ സ്റ്റോറേജ് അക്കൗണ്ട് സൃഷ്ടിക്കാൻ.
   **കുറിപ്പ്**: സ്റ്റോറേജ് അക്കൗണ്ട് തരം Standard General Purpose V2 ആകുന്നതായി ഉറപ്പാക്കുക.

## ഘട്ടം 2: ആസ്യൂർ AI സെർച്ച് സേവനം സൃഷ്ടിക്കുക

1. [ആസ്യൂർ പോർട്ടലിൽ സൈൻ ഇൻ](https://portal.azure.com/?wt.mc_id=studentamb_258691) ചെയ്യുക.
2. ഇടതു നാവിക പശ്ചാത്തലത്തിൽ **Create a resource** ക്ലിക്ക് ചെയ്യുക.
3. തിരയൽ ബോക്സ്‌യിൽ "Azure AI Search" എന്ന് ടൈപ്പ് ചെയ്ത് ഫലങ്ങളിലുള്ള **Azure AI Search** തിരഞ്ഞെടുക്കുക.
4. **Create** ബട്ടൺ ക്ലിക്ക് ചെയ്യുക.
5. **Basics** ടാബിൽ താഴെ പറയുന്ന വിവരങ്ങൾ നൽകുക:
   - **Subscription**: നിങ്ങളുടെ ആസ്യൂർ സബ്സ്ക്രിപ്ഷൻ തിരഞ്ഞെടുക്കുക.
   - **Resource group**: പുതിയത് സൃഷ്ടിക്കുക അല്ലെങ്കിൽ നിലവിലുള്ള ഒരു റിസോഴ്‌സ് ഗ്രൂപ്പ് തിരഞ്ഞെടുക്കുക.
   - **Resource name**: നിങ്ങളുടെ സെർച്ച് സേവനത്തിന് ഇൻകോടയായ ഒരു പേര് നൽകുക.
   - **Region**: ഉപയോക്താക്കളുടെ ഏറ്റവും അടുത്ത മേഖലയെ തെരഞ്ഞെടുക്കുക.
   - **Pricing tier**: നിങ്ങളുടെ ആവശ്യങ്ങൾക്കനുസരിച്ച് ഒരു വിലനിരക്ക് തിരഞ്ഞെടുക്കുക. പരിശോധനയ്ക്കായി സൗജന്യ നിരക്ക് ആരംഭിക്കാം.
6. **Review + create** ക്ലിക്ക് ചെയ്യുക.
7. ക്രമീകരണങ്ങൾ പരിശോധിച്ച് **Create** ക്ലിക്ക് ചെയ്ത് സെർച്ച് സേവനം സൃഷ്ടിക്കുക.

## ഘട്ടം 3: ആസ്യൂർ AI സെർച്ച് ഉപയോഗം ആരംഭിക്കുക

1. ഡിപ്ലോയ്‌മെന്റ് പൂർത്തിയാകുമ്പോൾ, ആസ്യൂർ പോർട്ടലിലെ നിങ്ങളുടെ സെർച്ച് സേവനത്തിലേക്ക് പോവുക.
2. സേർച്ച് സേവനത്തിന്റെ അവലോകന പേജ് തുറന്ന് URL പകർത്തുക. ഇത് `https://<service-name>.search.windows.net` പോലെയിരിക്കണം.
3. **(പരാമർശിച്ചിരിക്കുന്നത്)** Microsoft Entra ID (RBAC) ഉപയോഗിച്ച് കീ ഇല്ലാത്ത ആക്‌സസ്സ് പ്രവർത്തിപ്പിക്കുക — കീ വേണ്ട. ഈ ഗൈഡിലെ ഉദാഹരണമോഡലുകൾ ഇൻഡെക്സുകൾ സൃഷ്ടിക്കുകയും അപ്‌ലോഡ് ഡോക്യുമെന്റുകളും ചെയ്യുകയും ചെയ്യുന്നു, ഇവയ്ക്ക് **Search Service Contributor** & **Search Index Data Contributor** റോളുകൾ ആവശ്യമാണ് (അല്ലെങ്കിൽ കീ അടിസ്ഥാനത്തിലുള്ള ഓത്ത് ഉപയോഗിക്കുന്നെങ്കിൽ **പ്രധാന അഡ്മിൻ കീ** — ക്വറി കീ അല്ല). RBAC ഉപയോഗിക്കാനാകാത്ത പക്ഷം മാത്രം **Settings > Keys** പേജ് തുറന്ന് **പ്രധാന അഡ്മിൻ കീ** പകർത്തുക.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) ൽ പറയുന്നവ പാലിച്ച് ഇൻഡെക്സ് സൃഷ്ടിക്കുക, ഡാറ്റ അപ്‌ലോഡ് ചെയ്യുക, സെർച്ച് നടത്തുക.

## ഘട്ടം 4: ആസ്യൂർ AI സെർച്ച് ടൂളുകൾ ഉപയോഗിക്കുക

ആസ്യൂർ AI സെർച്ച് വിവിധ ടൂളുകളുമായി സമന്വയം പുലർത്തുന്നു, നിങ്ങളുടെ സെർച്ച് ശേഷി വർദ്ധിപ്പിക്കാൻ. ആസ്യൂർ CLI, Python SDK, .NET SDK തുടങ്ങി മറ്റു ടൂളുകൾ പരിഗണിuvan സഞ്ചാരണങ്ങൾക്കും പ്രവർത്തനങ്ങൾക്കും ഉപയോഗിക്കാം.

### ആസ്യൂർ CLI ഉപയോഗിച്ച്

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) ൽ കൊടുത്തിരിക്കുന്ന നിർദ്ദേശങ്ങൾ പാലിച്ചാണ് ആസ്യൂർ CLI ഇൻസ്റ്റാൾ ചെയ്യുക.
2. താഴെയുള്ള കമാൻഡ് ഉപയോഗിച്ച് ആസ്യൂർ CLI ലേക്ക് സൈൻ ഇൻ ചെയ്യുക:

   ```bash
   az login
   ```
3. **(പരാമർശിച്ചിരിക്കുന്നത്) Microsoft Entra ID (RBAC) ഉപയോഗിച്ച് കീ ഇല്ലാത്ത ആക്‌സസ് പ്രവർത്തിക്കുക:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC പ്രവർത്തനക്ഷമമാകുമ്പോൾ, Python & .NET SDK ഉദാഹരണങ്ങൾ താഴെ പറയുന്ന `DefaultAzureCredential` ഉപയോഗിച്ച് ഓതന്റിക്കേറ്റ് ചെയ്യുന്നു, ഇത് നിങ്ങളുടെ `az login` സെഷന്‍ ലോക്കൽ ഡെവലപ്പ്മെന്റ് സമയത്ത് ഉപയോഗിക്കുന്നു — അഡ്മിൻ കീ ആവശ്യമില്ല. [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) കാണുക.

4. **(ഫാൾബാക്ക്) കീ അടിസ്ഥാനത്തിലുള്ള ഓത്ത്** — RBAC ഉപയോഗിക്കാനാകാത്ത പക്ഷം മാത്രമേ, അഡ്മിൻ കീയും സൂക്ഷിക്കുക:

#### ആസ്യൂർ AI സെർച്ച് ഇൻസ്റ്റൻസിന്റെ എൻഡ്‌പോയിന്റും API കീയും പരിസ്ഥിതി വേരിയബിൾസ് ആയി സ്റ്റോർ ചെയ്യുക.

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

### Python SDK ഉപയോഗിച്ച്

1. Python-ക്കുള്ള ആസ്യൂർ കോഗ്നിറ്റീവ് സെർച്ച് ക്ലയന്റ് ലൈബ്രറിയും ആസ്യൂർ ഐഡന്റിറ്റിയും ഇൻസ്റ്റാൾ ചെയ്യുക:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ഇൻഡെക്സ് സൃഷ്ടിച്ച് ഡോക്യുമെന്റ് അപ്‌ലോഡ് ചെയ്യാൻ താഴെക്കാണുന്ന Python കോഡ് ഉപയോഗിക്കുക:

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

### .NET SDK ഉപയോഗിച്ച്

1. ഇൻഡെക്സ് സൃഷ്ടിച്ച് ഡോക്യുമെന്റ് അപ്‌ലോഡ് ചെയ്യാൻ താഴെയുള്ള കമാൻഡ് റൺ ചെയ്യുക:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    താഴെപ്പറയുന്ന .NET ഉദാഹരണം `DefaultAzureCredential` ഉപയോഗിക്കുന്നു, ഇത് ലോക്കൽ ഡെവലപ്പ്മെന്റിൽ നിങ്ങളുടെ ആസ്യൂർ CLI സൈൻ ഇൻ അറിയിപ്പ് `az login` ഉപയോഗിക്കാം.

2. `AzureSearch.cs` ന്റെ .NET കോഡ് ഇവിടെയാണ്:

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

കൂടുതൽ വിശദമായ വിവരങ്ങൾക്ക്, താഴെപ്പറയുന്ന ഡോക്യുമെന്റേഷൻ കാണുക:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## സമാപനം

നിങ്ങൾ ആസ്യൂർ പോർട്ടൽ ഉപയോഗിച്ച് ആസ്യൂർ AI സെർച്ച് വിജയകരമായി സജ്ജമാക്കി, സംയോജിത ടൂളുകൾ ഉപയോഗിച്ചും പ്രവർത്തിപ്പിച്ചു. ഇനി കൂടുതൽ മികവാർന്ന ഫീച്ചറുകളും കഴിവുകളുമായി നിങ്ങളുടെ സെർച്ച് പരിഹാരങ്ങൾ മെച്ചപ്പെടുത്തുവാനും പരീക്ഷിക്കാം.

കൂടുതല് സഹായത്തിന്, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) സന്ദർശിക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->