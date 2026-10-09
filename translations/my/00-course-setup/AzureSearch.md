# Azure AI Search စတက်အပ်လုပ်နည်းလမ်းညွှန်

ဒီလမ်းညွှန်က Azure ပေါ်တယ်ကို အသုံးပြုပြီး Azure AI Search ကို စတက်အပ်လုပ်နည်းကို အကူအညီပေးပါလိမ့်မယ်။ အောက်ပါအဆင့်များကို လိုက်နာပြီး သင့် Azure AI Search ၀န်ဆောင်မှုကို ဖန်တီးပြီး ပြင်ဆင်ပါ။

## မလိုအပ်ခင် ပြင်ဆင်ရန်များ

စတင်မလုပ်မီ အောက်ပါအရာများရှိမှသာပါ။

- Azure subscription တစ်ခု။ Azure subscription မရှိသေးပါက [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) တွင် အခမဲ့အကောင့် တစ်ခု ဖန်တီးနိုင်ပါသည်။

## အဆင့် ၁: Azure Storage အကောင့် ဖန်တီးခြင်း

1. ဒီညွှန်ကြားချက်အတိုင်း လုပ်ဆောင်ပြီး [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) မှာ အသစ် Azure Storage အကောင့် ဖန်တီးပါ။
   **NOTE**: Storage Account အမျိုးအစားကို Standard General Purpose V2 ဖြစ်စေရန် သေချာပါစေ။

## အဆင့် ၂: Azure AI Search ၀န်ဆောင်မှု ဖန်တီးခြင်း

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) မှာ စာရင်းဝင်ပါ။
2. ဘယ်ဖက် navigation ဖက်မှာ **Create a resource** ကို နှိပ်ပါ။
3. ရှာဖွေခြင်းမိုးကြီးမှာ "Azure AI Search" ဟုပုံစံရိုက်ထည့်ပြီး ရလဒ်စာရင်းမှ **Azure AI Search** ကို ရွေးချယ်ပါ။
4. **Create** ခလုတ်ကို နှိပ်ပါ။
5. **Basics** တက်ဘ်အတွင်း အောက်ပါအချက်အလက်များကို ဖြည့်စွက်ပါ။
   - **Subscription**: သင့် Azure subscription ကို ရွေးပါ။
   - **Resource group**: အသစ် Resource group တစ်ခု ဖန်တီးရန် သို့မဟုတ် ရှိပြီးသား ရွေးချယ်ပါ။
   - **Resource name**: သင့် search ၀န်ဆောင်မှုအတွက် ထူးခြားသောနာမည် ရိုက်ထည့်ပါ။
   - **Region**: သင့်အသုံးပြုသူများနီးပါးတည့်ရာ ဒေသကို ရွေးပါ။
   - **Pricing tier**: သင့်လိုအပ်ချက်နှင့် ကိုက်ညီသော စျေးနှုန်းအဆင့်ကို ရွေးပါ။ စမ်းသပ်ရန် Free tier နဲ့ စတင်နိုင်ပါသည်။
6. **Review + create** ကို နှိပ်ပါ။
7. အဆင်ပြေအောင် ပြုပြင်ပြီး **Create** ကို နှိပ်ကာ search ၀န်ဆောင်မှု ဖန်တီးပါ။

## အဆင့် ၃: Azure AI Search စတင်အသုံးပြုခြင်း

1. တပ်ဆင်ပြီးဆုံးသည်နှင့် သင့် search ၀န်ဆောင်မှုပေါ်သို့ သွားပါ။
2. Search ၀န်ဆောင်မှု အနှစ်ချုပ် မျက်နှာပြင်တွင် URL ကို ကူးယူပါ။ `https://<service-name>.search.windows.net` သို့မဟုတ် ထိုသို့ပုံစံရှိပါမည်။
3. **(အကြံပြု)** Microsoft Entra ID (RBAC) ဖြင့် keyless access ကို အောက်ပါ အဆင့် ၄ မှာ ဖော်ပြသည့်အတိုင်း ဖွင့်ပါ — key မလိုပါ။ ဒီလမ်းညွှန်အတွက် ဥပမာများသည် index များ ဖန်တီး/တိုးမြှင့်ခြင်းနှင့် စာရွက်စာတမ်းများ အပ်လုပ္ခြင်းကို လုပ်သည်။ ၎င်းအတွက် **Search Service Contributor** နှင့် **Search Index Data Contributor** အခန်းကဏ္ဍများ လိုအပ်သည် (သို့မဟုတ် key-based authentication အတွက်, **primary admin key** သာ အဆင်ပြေပြီး query key မလိုပါ။) RBAC မသုံးနိုင်ရင်ဘဲ **Settings > Keys** ဖောက်ရှာပြီး **primary admin key** ကို ကူးယူပါ။
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) စာမျက်နှာမှ အဆင့်များကို လိုက်နာကာ index ဖန်တီးခြင်း၊ data အပ်လုပ္ခြင်း၊ နှင့် ရှာဖွေရေးလုပ်ဆောင်ပါ။

## အဆင့် ၄: Azure AI Search ကိရိယာများ အသုံးပြုခြင်း

Azure AI Search သည် သင့်ရှာဖွေမှု စွမ်းဆောင်ရည်အား ပိုမိုကောင်းမွန်အောင် အမျိုးမျိုးသောကိရိယာများနှင့် ပေါင်းစပ် အသုံးပြုနိုင်သည်။ Azure CLI၊ Python SDK၊ .NET SDK နှင့် အခြားကိရိယာများကို အဆင့်မြင့်ချိန်ညှိမှုနှင့် လုပ်ဆောင်ချက်များအတွက် အသုံးပြုနိုင်သည်။

### Azure CLI အသုံးပြုခြင်း

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) ပြဿနာများကိုလိုက်နာပြီး Azure CLI ကို ဒေါင်းလုဒ်လုပ်ပါ။
2. Azure CLI သို့ အောက်ပါ command ဖြင့် စာရင်းဝင်ပါ။

   ```bash
   az login
   ```
3. **(အကြံပြု) Microsoft Entra ID (RBAC) ဖြင့် keyless access ဖွင့်ပါ:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show တွင် "endpoint" နယ်ပယ်မရှိပါ; URL ကို ဝန်ဆောင်မှုအမည်မှ တည်ဆောက်ပါ။
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC ဖွင့်ထားပါက Python နှင့် .NET SDK ဥပမာများသည် `DefaultAzureCredential` ဖြင့် authentication ပြုလုပ်သည်၊ ၎င်းသည် သင့်ရဲ့ `az login` စာရင်းဝင် အစီအစဉ်ကို local ဖွံ့ဖြိုးမှုတွင် အသုံးပြုသည် --- admin key မလိုအပ်ပါ။ ကြည့်ရှုရန် [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)။

4. **(Fallback) Key-based authentication** — RBAC မသုံးနိုင်သည့်အခါ admin key ကိုလည်းသိမ်းဆည်းပါ။

#### Azure AI Search instance အတွက် endpoint နှင့် API key တို့ကို environment variables တွင် သိမ်းဆည်းရန်။

    ```bash
    # zsh/bash
    # az search service show တွင် "endpoint" field မရှိပါ; service name မှ URL ဖန်တီးပါ။
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show တွင် "endpoint" field မရှိပါ; service name မှ URL ဖန်တီးပါ။
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK အသုံးပြုခြင်း

1. Azure Cognitive Search client library နှင့် Azure Identity ကို Python အတွက် 설치ပါ:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ဤ Python ကုဒ်ကို အသုံးပြုပြီး index ဖန်တီးခြင်းနှင့် စာရွက်စာတမ်းများ အပ်လုပ္နိုင်သည်။

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (အကြံပြုသည်): သင်၏ `az login` ကို Entra ID RBAC မှတဆင့် အသုံးပြုသည်။
    # "Search Service Contributor" နှင့် "Search Index Data Contributor" အခန်းကဏ္ဍများလိုအပ်သည်။
    credential = DefaultAzureCredential()
    # နောက်ထပ်လမ်းစဉ် (key-based auth):
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

1. အောက်ပါ command ဖြင့် index ဖန်တီးခြင်းနှင့် စာရွက်စာတမ်းများ အပ်လုပ္ပါ:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    အောက်ပါ .NET ဥပမာသည် `DefaultAzureCredential` ကို အသုံးပြုသည်၊ ၎င်းသည် သင့် Azure CLI မှ `az login` ဖွင့်ထားသောစာရင်းဝင်မှုကို local ဖွံ့ဖြိုးမှုတွင် အသုံးပြုနိုင်သည်။

2. ဒီမှာ `AzureSearch.cs` .NET ကုဒ် ပါသည်:

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

အချက်အလက်ပိုမို အသေးစိတ်များအတွက် အောက်ပါစာရွက်စာတမ်းများကို ကြည့်ပါ။

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## နိဂုံးချုပ်

သင်သည် Azure ပေါ်တယ်ကို အသုံးပြု၍ Azure AI Search ကို အောင်မြင်စွာ စတက်အပ်လုပ်ပြီး ကိရိယာများနှင့်ပေါင်းစပ်အသုံးပြုမှုများ ပြုလုပ်နိုင်ပါပြီ။ ယခုတွင် Azure AI Search ၏ အဆင့်မြင့် လုပ်ဆောင်ချက်များနှင့် စွမ်းရည်များကို ပိုမိုလေ့လာပြီး ရှာဖွေရေး ဖြေရှင်းချက်များ မြှင့်တင်နိုင်ပါပြီ။

ထပ်မံ အကူအညီလိုပါက [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) သို့ သွားရောက်ကြည့်ရှုပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->