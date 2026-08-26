# അഴ്യൂർ എഐ സെർച്ച് സജ്ജീകരണ ഗൈഡ്

ഈ ഗൈഡ് അഴ്യൂർ പോർട്ടൽ ഉപയോഗിച്ച് അഴ്യൂർ എഐ സെർച്ച് സജ്ജീകരിക്കാൻ സഹായിക്കും. നിങ്ങളുടെ അഴ്യൂർ എഐ സെർച്ച് സർവീസ് സൃഷ്‌ടിക്കുകയും കോൺഫിഗർ ചെയ്യുകയും ചെയ്യാൻ താഴെ കാണുന്ന ചുവടുകൾ പിന്തുടരുക.

## മുന്‍ ആവശ്യകതകള്‍

തുടങ്ങുന്നതിന് മുമ്പ്, താഴെ പറയുന്നവ ഉണ്ടെന്ന് ഉറപ്പാക്കുക:

- ഒരു അഴ്യൂർ സബ്സ്ക്രിപ്ഷൻ. നിങ്ങളുടെ কাছে അഴ്യൂർ സബ്സ്ക്രിപ്ഷൻ ഇല്ലെങ്കിൽ, [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) ല്‍ ഒരു സൗജന്യ അക്കൗണ്ട് സൃഷ്‌ടിക്കാനാകും.

## ഘട്ടം 1: ഒരു അഴ്യൂർ സ്റ്റോറേജ് അക്കൗണ്ട് സൃഷ്‌ടിക്കുക

1. പുതിയ അഴ്യൂർ സ്റ്റോറേജ് അക്കൗണ്ട് സൃഷ്‌ടിക്കാൻ [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) എന്ന നിർദ്ദേശം പിന്തുടരുക.
   **ശ്രദ്ധിക്കുക**: സ്റ്റോറേജ് അക്കൗണ്ടിന്റെ തരം Standard General Purpose V2 ആണെന്ന് ഉറപ്പാക്കുക.

## ഘട്ടം 2: അഴ്യൂർ എഐ സെർച്ച് സർവീസ് സൃഷ്‌ടിക്കുക

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) ലോഗിൻ ചെയ്യുക.
2. ഇടത്താറ് നാവിഗേഷൻ പാനിൽ **Create a resource** ക്ലിക്ക് ചെയ്യുക.
3. തിരയൽ ബോക്സിൽ "Azure AI Search" ടൈപ്പ് ചെയ്ത് ഫലങ്ങളിൽ നിന്നും **Azure AI Search** തിരഞ്ഞെടുക്കുക.
4. **Create** ബട്ടൺ ക്ലിക്ക് ചെയ്യുക.
5. **Basics** ടാബിൽ താഴെകാണുന്ന വിവരങ്ങൾ നല്‍കുക:
   - **Subscription**: നിങ്ങളുടെ അഴ്യൂർ സബ്സ്ക്രിപ്ഷൻ തിരഞ്ഞെടുക്കുക.
   - **Resource group**: പുതിയ റെസോഴ്‌സ് ഗ്രൂപ്പ് സൃഷ്‌ടിക്കുകയോ നിലവിലുള്ള ഒരു ഗ്രൂപ്പ് തിരഞ്ഞെടുക്കുകയോ ചെയ്യുക.
   - **Resource name**: നിങ്ങളുടെ സെർച്ച് സർവീസിന്ൊരു വിരലടയാളമുള്ള നാമം നൽകുക.
   - **Region**: നിങ്ങളുടെ ഉപയോക്താക്കളോട് ഏറ്റവും അടുത്ത സ്ഥലം തിരഞ്ഞെടുക്കുക.
   - **Pricing tier**: നിങ്ങളുടെ ആവശ്യങ്ങൾക്കു അനുയോജ്യമുള്ള ഒരു പ്രൈസിംഗ് ടിയർ തിരഞ്ഞെടുക്കുക. ടെസ്റ്റിംഗിന് Free ടിയർ ഉപയോഗിക്കുക.
6. **Review + create** ക്ലിക്ക് ചെയ്യുക.
7. സജ്ജീകരണങ്ങൾ പരിശോധിച്ച് **Create** ക്ലിക്ക് ചെയ്ത് സെർച്ച് സർവീസ് സൃഷ്‌ടിക്കുക.

## ഘട്ടം 3: അഴ്യൂർ എഐ സെർച്ച് ഉപയോഗിച്ച് തുടക്കം

1. ഡിപ്ലോയ്മെന്റ് പൂര്‍ത്തിയായശേഷം, അഴ്യൂർ പോർട്ടലിൽ നിങ്ങളുടെ സെർച്ച് സർവീസിലേക്ക് പോയി.
2. സെർച്ച് സർവീസ് അവലോകന പാനില്‍ URL കോപ്പ് ചെയ്യുക. ഇത് `https://<service-name>.search.windows.net` പോലെയുണ്ടാകും.
3. **( ശുപാർശ ചെയ്യുന്നു)** കീ ഇല്ലാതെ Microsoft Entra ID (RBAC) -നുമായി പ്രവേശനം സജ്ജമാക്കുക, താഴെ കാണുന്ന ഘട്ടം 4 ൽ വിശദീകരിച്ചതൊപ്പം - കീ വേണ്ട. ഈ ഗൈഡിലെ സാമ്പിളുകൾ ഇൻഡേക്‌സുകൾ സൃഷ്ടിക്കുകയും അപ്‌ലോഡ് ചെയ്യുകയും ചെയ്യുന്നു, അദ്ദേഹങ്ങൾക്ക് **Search Service Contributor** & **Search Index Data Contributor** റോളുകൾ ആവശ്യമാണ് (കീ ബേസ്ഡ് ഓതന്റിക്കേഷനായി, **primary admin key** വേണ്ടതാണ് - query key അല്ല). RBAC ഉപയോഗിക്കാനാകാത്ത പക്ഷം, **Settings > Keys** പാനില്‍ primary admin കി കോപ്പ് ചെയ്യുക.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) പേജ് വായിച്ച് ഇൻഡെക്‌സ് സൃഷ്ടിക്കുകയും ഡാറ്റ അപ്‌ലോഡ് ചെയ്യുകയും സെർച്ച് നടത്തുകയും ചെയ്യുക.

## ഘട്ടം 4: അഴ്യൂർ എഐ സെർച്ച് ടൂളുകൾ ഉപയോഗിക്കുക

നിങ്ങളുടെ സെർച്ച് കഴിവുകൾ വികസിപ്പിക്കാൻ അഴ്യൂർ എഐ സെർച്ച് വിവിധ ടൂളുകൾക്കൊപ്പം ചേർന്നു പ്രവർത്തിക്കുന്നു. പുരോഗമന കോൺഫിഗറേഷനുകളുടെയും പ്രവർത്തനങ്ങളുടെയും വേണ്ടി അഴ്യൂർ CLI, Python SDK, .NET SDK എന്നിവ ഉപയോഗിക്കാം.

### അഴ്യൂർ CLI ഉപയോഗിക്കൽ

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) എന്ഗവ инструкции অনুসരിച്ച് അഴ്യൂർ CLI ഇൻസ്റ്റാൾ ചെയ്യുക.
2. താഴെ കാണുന്ന കമാൻഡ് ഉപയോഗിച്ച് അഴ്യൂർ CLI ലോഗിൻ ചെയ്യുക:

   ```bash
   az login
   ```
3. **(ശുപാർശ ചെയ്യുന്നു) Microsoft Entra ID (RBAC) ഉപയോഗിച്ച് കീ ഇല്ലാത്ത പ്രവേശനം സജ്ജമാക്കുക:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show യിൽ "endpoint" ഫീൽഡ് ഇല്ല; സർവീസ് നാമത്തിൽ നിന്നുതന്നെ URL സൃഷ്ടിക്കുക.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC സജീവമാക്കിയാൽ python, .NET SDK സാമ്പിലുകൾ `DefaultAzureCredential` ഉപയോഗിച്ച് 인증 ചെയ്യും, ഇത് നിങ്ങളുടെ `az login` സെഷൻ പ്രാദേശിക ഡെവലപ്മെന്റിൽ ഉപയോഗിക്കും — അഡ്മിൻ കീ ആവശ്യമില്ല. കൂടുതൽ വിവരങ്ങൾക്ക് [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) കാണുക.

4. **(ബാക്കപ്പ്) കീ-ബേസ്ഡ് ഓതന്റിക്കേഷൻ** — നിങ്ങൾക്ക് RBAC ഉപയോഗിക്കാനാകാതെ വന്നാൽ മാത്രം അഡ്മിൻ കീ സേവ് ചെയ്യുക:

#### അഴ്യൂർ എഐ സെർച്ച് ഇൻസ്റ്റൻസിന്റെ അവസാന പോയിന്റും API കീയും പരിസ്ഥിതി ചാരങ്ങളായി സേവ് ചെയ്യുക.

    ```bash
    # zsh/bash
    # az search service show കമാൻഡിന് "endpoint" ഫീൽഡ് ഇല്ല; സർവീസ് നാമത്തിൽ നിന്ന് URL നിർമ്മിക്കുക.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show കമാൻഡിന് "endpoint" ഫീൽഡ് ഇല്ല; സർവീസ് നാമത്തിൽ നിന്ന് URL നിർമ്മിക്കുക.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK ഉപയോഗിക്കൽ

1. Pythonക്ക് Azure Cognitive Search ക്ലയന്റ് ലൈബ്രറി, Azure Identity ഇൻസ്റ്റാൾ ചെയ്യുക:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ഇൻഡെക്‌സ് സൃഷ്‌ടിച്ചു, ഡോക്യൂമെന്റുകൾ അപ്‌ലോഡ് ചെയ്യാൻ താഴെ കാണുന്ന Python കോഡ് ഉപയോഗിക്കുക:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # കീലെസ് (പരാമർശിക്കുന്നു): നിങ്ങളുടെ `az login` ഐഡന്റിറ്റി Entra ID RBAC വഴി ഉപയോഗിക്കുന്നു.
    # "Search Service Contributor" ഉം "Search Index Data Contributor" ഉം റോളുകൾ ആവശ്യമാണ്.
    credential = DefaultAzureCredential()
    # പിന്‍ഗാമി (കീ ആധാരിത പ്രാമാണീകരണം):
    # azure.core.credentials മുതൽ AzureKeyCredential ആമ്ദാനം ചെയ്യുന്നു
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

### .NET SDK ഉപയോഗിക്കൽ

1. ഇൻഡെക്‌സ് സൃഷ്‌ടിക്കുകയും ഡോക്യൂമെന്റുകൾ അപ്‌ലോഡ് ചെയ്യുകയും ചെയ്യാൻ താഴെയുള്ള കമാൻഡ് റൺ ചെയ്യുക:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    താഴെ കാണുന്ന .NET സാമ്പിള്‍ `DefaultAzureCredential` ഉപയോഗിക്കുന്നു, ഇത് നിങ്ങളുടെ `az login` CLI സൈൻ-ഇന് സെഷൻ പ്രാദേശിക ഡെവലപ്മെന്റിൽ ഉപയോഗിക്കും.

2. ഇവിടെ `AzureSearch.cs` ന്റെ .NET കോഡ് ഉണ്ട്:

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

കൂടുതൽ വിശദമായ വിവരങ്ങൾക്ക് താഴെ നൽകിയ ഡോക്യുമെന്റേഷൻ കാണുക:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## സമാപനം

അഴ്യൂർ പോർട്ടൽ ഉപയോഗിച്ച് അഴ്യൂർ എഐ സെർച്ച് സജ്ജീകരിക്കുകയും ടൂളുകൾ സംയോജിപ്പിക്കുകയും നിങ്ങൾ വിജയകരമായി ചെയ്തു. 이제 അഴ്യൂർ എഐ സെർച്ച് ന്റെ കൂടുതൽ പുരോഗമന ഘടകങ്ങൾ പരിശോധിച്ച് നിങ്ങളുടെ സെർച്ച് പരിഹാരങ്ങൾ മെച്ചപ്പെടുത്താം.

കൂടുതൽ സഹായത്തിനായി, [Azure Cognitive Search ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) സന്ദര്‍ശിക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->