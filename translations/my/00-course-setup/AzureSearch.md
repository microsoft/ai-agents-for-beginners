# Azure AI ရှာဖွေမှု စတင်ပြုလုပ်ခြင်း လမ်းညွှန်

ဒီလမ်းညွှန်က Azure portal ကို အသုံးပြုပြီး Azure AI ရှာဖွေမှုကို စတင်ပြုလုပ်ရန် ကူညီပေးပါမည်။ ကေအောက်ပါ အဆင့်များကို အတိုက်အခံ လိုက်နာပြီး Azure AI ရှာဖွေမှု ဝန်ဆောင်မှုကို ဖန်တီးခြင်းနှင့် ဆက်တင်ပြုလုပ်ပါ။

## လိုအပ်ချက်များ

စတင်ရန်မပြုမီ အောက်ပါအချက်များ ရှိကြောင်း သေချာစေပါ။

- Azure subscription တစ်ခု။ သင်မှာ Azure subscription မရှိပါက [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) တွင် အခမဲ့ အကောင့် တစ်ခု ဖန်တီးနိုင်သည်။

## အဆင့် ၁: Azure Storage Account တစ်ခု ဖန်တီးခြင်း

1. ဒီညွှန်ကြားချက်ဖြင့်, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) ကို လိုက်နာကာ Azure Storage Account အသစ် တစ်ခု ဖန်တီးပါ။
   **မှတ်စု**: Storage Account အမျိုးအစားသည် Standard General Purpose V2 ဖြစ်သည်ကို သေချာစေပါ။

## အဆင့် ၂: Azure AI Search ဝန်ဆောင်မှု တစ်ခု ဖန်တီးခြင်း

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) မှာ ဆိုင်ရာအကောင့်ဖြင့် လက်မှတ်ထိုးဝင်ပါ။
2. ဘယ်ဘက် navigation pane တွင် **Create a resource** ကို နှိပ်ပါ။
3. ရှာဖွေမှု ထဲတွင် "Azure AI Search" ဟု ရိုက်ထည့်ပြီး ရလဒ်စာရင်းမှ **Azure AI Search** ကို ရွေးချယ်ပါ။
4. **Create** ခလုတ်ကို နှိပ်ပါ။
5. **Basics** tab တွင် အောက်ပါအချက်များ ထည့်သွင်းပါ။
   - **Subscription**: သင့် Azure subscription ကို ရွေးချယ်ပါ။
   - **Resource group**: အသစ် Resource group တစ်ခု ဖန်တီးခြင်း သို့မဟုတ် ရှိပြီးသားကို ရွေးချယ်ပါ။
   - **Resource name**: သင့် ရှာဖွေမှု ဝန်ဆောင်မှု အတွက် ထူးခြားသော နာမည် ထည့်ပါ။
   - **Region**: သင့် အသုံးပြုသူများနီးစပ်ရာ ဒေသကို ရွေးချယ်ပါ။
   - **Pricing tier**: သင့်လိုအပ်ချက်နှင့် ကိုက်ညီသည့် ပိုက်ဆံပမာဏအဆင့်ကို ရွေးပါ။ စမ်းသပ်ရန် အခမဲ့ tier ဖြင့် စတင်နိုင်ပါသည်။
6. **Review + create** ကို နှိပ်ပါ။
7. ဆက်တင်များကို ပြန်လည်သုံးသပ်ပြီး **Create** ကို နှိပ်ကာ ရှာဖွေမှု ဝန်ဆောင်မှုကို ဖန်တီးပါ။

## အဆင့် ၃: Azure AI ရှာဖွေမှု စတင်အသုံးပြုခြင်း

1. ထည့်သွင်းခြင်း ပြီးဆုံးသည်နောက် သင့်ရှာဖွေမှု ဝန်ဆောင်မှုသို့ Azure portal မှ သွားရောက်ပါ။
2. ရှာဖွေမှု ဝန်ဆောင်မှု အကျဉ်း စာမျက်နှာတွင် URL ကို မိတ္တူကူးပါ။ ၎င်းသည် `https://<service-name>.search.windows.net` ကဲ့သို့ ရှိရမည်။
3. **(အကြံပြုချက်)** Microsoft Entra ID (RBAC) ဖြင့် keyless access ကို ဖွင့်ပါ — key မလိုအပ်ပါ။ ဒီလမ်းညွှန်ရှိ စမ်းသပ်မှုများတွင် index ဖန်တီးခြင်း၊ စာရွက်စာတမ်းများ တင်ခြင်း ပါဝင်လျက်ရှိပြီး ဒီအရာများအတွက် **Search Service Contributor** နှင့် **Search Index Data Contributor** အခန်းကဏ္ဍလိုအပ်သည် (သို့မဟုတ် key-based auth အတွက် **primary admin key** — query key မဟုတ်ပါ။) RBAC မသုံးနိုင်လျှင်သာ **Settings > Keys** ကျောဘက်မှာ primary admin key ကို ကူးယူပါ။
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) စာမျက်နှာတွင် အဆင့်များအတိုင်း index ဖန်တီးခြင်း၊ ဒေတာတင်ခြင်းနှင့် ရှာဖွေမှု ပြုလုပ်ခြင်းကို လိုက်နာပါ။

## အဆင့် ၄: Azure AI ရှာဖွေမှု ကိရိယာများ အသုံးပြုခြင်း

Azure AI ရှာဖွေမှုသည် ရှာဖွေမှု စွမ်းဆောင်မှုများ တိုးတက်စေရန် ကိရိယာစုံနှင့် ပေါင်းစပ်ထားသည်။ Azure CLI, Python SDK, .NET SDK နှင့် အခြား ကိရိယာများကို တိုးတက်သော ဆက်တင်များနှင့် လုပ်ဆောင်ချက်များအတွက် အသုံးပြုနိုင်သည်။

### Azure CLI အသုံးပြုခြင်း

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) တွင် နည်းလမ်းများအတိုင်း Azure CLI ကို တပ်ဆင်ပါ။
2. အောက်ပါ command ဖြင့် Azure CLI သို့ လက်မှတ်ထိုးဝင်ပါ။

   ```bash
   az login
   ```
3. **(အကြံပြု) Microsoft Entra ID (RBAC) ဖြင့် keyless access ကို ဖွင့်ပါ။**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC ဖွင့်ထားခြင်းဖြင့် Python နှင့် .NET SDK စမ်းသပ်ရန် အောက်ပါအတိုင်း `DefaultAzureCredential` ဖြင့် သင့် `az login` session ကို ဒေသန္တရ ဖန်တီးမှုအချိန်မှာ အသုံးပြုသည်။ အဲဒါကြောင့် admin key မလိုအပ်။ [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) ကို ကြည့်ပါ။

4. **(အဆင်မပြေမှ) key-based auth** — RBAC ကို မသုံးနိုင်ပါက admin key ကို သိုလှောင်ပါ။

#### Azure AI Search instance များအတွက် endpoint နှင့် API key ကို environment variables တွင် သိုလှောင်ပါ။

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

### Python SDK အသုံးပြုခြင်း

1. Azure Cognitive Search client library နှင့် Azure Identity ကို Python အတွက် တပ်ဆင်ပါ။

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. index ဖန်တီးရန်နှင့် စာရွက်စာတမ်းများ တင်ရန် အောက်ပါ Python ကုဒ်ကို အသုံးပြုပါ။

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

### .NET SDK အသုံးပြုခြင်း

1. index ဖန်တီးရန်နှင့် စာရွက်စာတမ်းများ တင်ရန် အောက်ပါ command ကို လုပ်ဆောင်ပါ။

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    အောက်ပါ .NET စမ်းသပ်မှု သည် `DefaultAzureCredential` ကို အသုံးပြု၍ ဒေသန္တရ ဖန်တီးမှုအချိန်တွင် Azure CLI အကောင့် sign-in မှ `az login` ကို အသုံးပြုနိုင်သည်။

2. အောက်မှာ `AzureSearch.cs` ၏ .NET ကုဒ်ဖြစ်သည်။

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

အသေးစိတ် အချက်အလက်များအတွက် အောက်ဖော်ပြပါစာရွက်များကို သွားရောက်ကြည့်ရှုပါ။

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## အနှုတ်ချုပ်

သင်သည် Azure portal အသုံးပြု၍ Azure AI Search ကို အောင်မြင်စွာ စတင်ဖန်တီးပြီး ဘေးကင်းသော ကိရိယာများနှင့် ပေါင်းစပ်အသုံးပြုပြီး ဖြစ်ပါသည်။ ယခုအချိန်တွင် Azure AI Search ၏ တိုးတက်သော အင်္ဂါရပ်များနှင့် စွမ်းဆောင်ရည်များကို ရှာဖွေတိုက်တွန်းနိုင်ပါသည်။

ဆက်လက်အကူအညီများအတွက် [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) သို့ သွားရောက်ကြည့်ရှုပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->