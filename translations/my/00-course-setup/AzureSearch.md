# Azure AI ရှာဖွေရေး သတ်မှတ်ချက် လမ်းညွှန်

ဒီလမ်းညွှန်က Azure ပေါ်တယ်ကို အသုံးပြုပြီး Azure AI ရှာဖွေရေးကို စတင်ပြင်ဆင်ပေးမှာဖြစ်ပါတယ်။ အောက်ဖော်ပြထားတဲ့ဆင့်ကိုလိုက်နာပြီး သင့် Azure AI ရှာဖွေရေးဝန်ဆောင်မှုကို ဖန်တီးပြီး သတ်မှတ်ရန်အတွက် အသုံးပြုနိုင်ပါတယ်။

## မဖြစ်မနေလိုအပ်ချက်များ

စတင်ဦးမယ့်အခါမှာ အောက်ပါအရာများရှိနေကြောင်း သေချာစေပါ။

- Azure စာရင်းသွင်းမှုတစ်ခု။ သင်မှာ Azure စာရင်းသွင်းမှု မရှိသေးရင် [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) မှာ အခမဲ့အကောင့်တစ်ခု ဖန်တီးနိုင်ပါတယ်။

## ဆင့် ၁: Azure သိုလှောင်မှုအကောင့် ဖန်တီးခြင်း

1. ဒီညွှန်ကြားချက်ကိုလိုက်နာပါ၊ [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)၊ Azure သိုလှောင်မှုအကောင့်အသစ်ကိုဖန်တီးရန်။
   **မှတ်ချက်**: သိုလှောင်မှုအကောင့်အမျိုးအစားကို Standard General Purpose V2 ဖြစ်စေရန် သေချာစေပါ။

## ဆင့် ၂: Azure AI ရှာဖွေရေး ဝန်ဆောင်မှု ဖန်တီးခြင်း

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) တွင် စနစ်ဝင်ပါ။
2. ဘယ်ဘက်ဘက် navigation panel တွင် **Create a resource** ကို နှိပ်ပါ။
3. ရှာဖွေရေးပုံးတစ်ခုတွင် "Azure AI Search" ဟု ရိုက်ထည့်ပြီး ရလဒ်စာရင်းထဲက **Azure AI Search** ကို ရွေးပါ။
4. **Create** ခလုတ်ကို နှိပ်ပါ။
5. **Basics** tab မှာ အောက်ပါအချက်အလက်များကို ဖြည့်ပါ။
   - **Subscription**: သင့် Azure စာရင်းသွင်းမှုကို ရွေးချယ်ပါ။
   - **Resource group**: အသစ် resource group တစ်ခုဖန်တီးပါ သို့မဟုတ် ရှိပြီးသား resource group များထဲမှ တစ်ခုကို ရွေးချယ်ပါ။
   - **Resource name**: သင့် ရှာဖွေရေး ဝန်ဆောင်မှုအတွက် ထူးခြားချင်သော နာမည် တစ်ခုထည့်ပါ။
   - **Region**: သုံးစွဲသူများနီးစပ်ရာ တိုင်းဒေသကို ရွေးချယ်ပါ။
   - **Pricing tier**: သင့်လိုအပ်ချက်နှင့် ကိုက်ညီသည့် စျေးနှုန်းအဆင့်ကို ရွေးချယ်ပါ။ စမ်းသပ်ရန်အတွက် Free tier ဖြင့် စတင်နိုင်သည်။
6. **Review + create** ကို နှိပ်ပါ။
7. သတ်မှတ်ချက်များကို ပြန်ကြည့်ပြီး **Create** ခလုတ်ကို နှိပ်ပြီး ရှာဖွေရေး ဝန်ဆောင်မှုကို ဖန်တီးပါ။

## ဆင့် ၃: Azure AI ရှာဖွေရေး စတင်အသုံးပြုခြင်း

1. တပ်ဆင်ခြင်းပြီးဆုံးပါက Azure portal တွင် သင့်ရဲ့ ရှာဖွေရေးဝန်ဆောင်မှုဆီ သွားပါ။
2. ရှာဖွေရေးဝန်ဆောင်မှု မျက်နှာပြင်တွင် URL ကို ကူးယူပါ။ ဥပမာ `https://<service-name>.search.windows.net` အဖြစ် ဖြစ်ရမည်။
3. **(အကြံပြုချက်)** Microsoft Entra ID (RBAC) ဖြင့် keyဖိုင်မလိုသော ဝင်ရောက်ခွင့် ကို အောက်တွင် ဆင့် ၄ မှာ ဖော်ပြထားတဲ့အတိုင်း ဖွင့်ထားပါ — key မလိုပါ။ ဒီလမ်းညွှန်မှ နမူနာများသည် ဂဏန်းများကို ဖန်တီးမှု၊ ပြင်ဆင်မှုနှင့် စာရွက်စာတမ်းများတင်ပြရာတွင် **Search Service Contributor** နှင့် **Search Index Data Contributor** အခန်းကဏ္ဍများ (သို့) key-based အသုံးပြုမှုအတွက် အဓိက အုပ်ချုပ်သူ key ကို လိုအပ်ပြီး ရှာဖွေရေးအခန်းကဏ္ဍ key ကိုမလိုပါ။ RBAC မအသုံးပြုနိုင်တော့မှသာ **Settings > Keys** ပျတွင် ဝင်ပြီး အဓိက အုပ်ချုပ်သူ key ကို ကူးယူပါ။
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) စာမျက်နှာအတိုင်း ဂဏန်းတစ်ခု ဖန်တီးခြင်း၊ ဒေတာတင်ခြင်းနှင့် ရှာဖွေရေး ပြုလုပ်ခြင်းဆိုင်ရာ ဆင့်များကို လိုက်နာပါ။

## ဆင့် ၄: Azure AI ရှာဖွေရေး ကိရိယာများ အသုံးပြုခြင်း

Azure AI ရှာဖွေရေးသည် သင့်ရဲ့ ရှာဖွေမှုစွမ်းဆောင်ရည်မြှင့်တင်ရန်ကိရိယာ များနှင့် ပေါင်းစပ်အသုံးပြုနိုင်သည်။ သင်သည် Azure CLI, Python SDK, .NET SDK နှင့် အခြားကိရိယာများကို ကြည့်ရှု၍ မြှင့်တင်ချင်သည့် သတ်မှတ်ချက်များလုပ်ဆောင်နိုင်သည်။

### Azure CLI အသုံးပြုခြင်း

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) ကနေ အသုံးပြုရန် Azure CLI ကို တပ်ဆင်ပါ။
2. command ကို အသုံးပြုပြီး Azure CLI တွင် စနစ်ဝင်ပါ။

   ```bash
   az login
   ```
3. **(အကြံပြုချက်) Microsoft Entra ID (RBAC) နဲ့ key မလိုသော ဝင်ခွင့် ဖွင့်ထားခြင်း:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show မှာ "endpoint" field မရှိပါ; URL ကို service name မှတည်ဆောက်ပါ။
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC ကို ဖွင့်ထားလျှင် Python နှင့် .NET SDK နမူနာများသည် `DefaultAzureCredential` ဖြင့် အတည်ပြုခြင်းလုပ်ဆောင်ပါသည်၊ ဒါကသင်၏ `az login` အစီအစဉ်ကို အသုံးပြု၍ ဒေသတြင် ဖွံ့ဖြိုးမှုအတွင်း ကီးမလိုသော အုပ်ချုပ်ခွင့် ကို သုံးစွဲနိုင်သည်။ ပိုမိုသိရှိရန် [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) ကိုကြည့်ပါ။

4. **(အစားထိုး) key-based authentication** — RBAC မသုံးနိုင်လျှင် admin key ကိုလည်း သိမ်းဆည်းပါ။

#### Azure AI ရှာဖွေရေး instance အတွက် endpoint နဲ့ API key နှစ်ခုလုံးကို ပတ်ဝန်းကျင် မတည်ငြိမ်ပြောင်းရန် variable များအဖြစ် သိမ်းဆည်းပါ။

    ```bash
    # zsh/bash
    # az search service show မှာ "endpoint" field မရှိပါ; service name ကနေ URL ကို ဖန်တီးပါ။
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show မှာ "endpoint" field မရှိပါ; service name ကနေ URL ကို ဖန်တီးပါ။
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK အသုံးပြုခြင်း

1. Azure Cognitive Search client library နှင့် Azure Identity များကို Python အတွက် တပ်ဆင်ပါ။

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. ဤ Python ကုဒ်ကို အသုံးပြု၍ ဂဏန်း ဖန်တီးပြီး စာရွက်စာတမ်းတင်ပါ။

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (အကြံပြု): သင့်ရဲ့ `az login` အသိအမှတ်ပြုချက်ကို Entra ID RBAC မှတဆင့် အသုံးပြုသည်။
    # "Search Service Contributor" နှင့် "Search Index Data Contributor" အခန်းကျမှာ ပေးရန် လိုအပ်သည်။
    credential = DefaultAzureCredential()
    # ပြန်လည်ဆောင်ရွက်မှု (key-based auth)။
    # azure.core.credentials မှ AzureKeyCredential ကို သွင်းယူသည်။
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

1. ဥပမာ အီးတပုဒ် command ကို အသုံးပြုပြီး ဂဏန်းဖန်တီးပြီး စာရွက်စာတမ်းတင်ပါ။

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    အောက်ပါ .NET နမူနာသည် `DefaultAzureCredential` ကို အသုံးပြုသည်၊ ဒါက သင့်ရဲ့ Azure CLI မှာ `az login` ဖြင့် စနစ်ဝင်မှုကို ဒေသတွင် ဖွံ့ဖြိုးမှုအတွင်း အသုံးပြုနိုင်သည်။

2. ဒီမှာ `AzureSearch.cs` .NET ကုဒ် ရှိပါသည်။

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

အသေးစိတ်သိရှိလိုပါက အောက်ပါစာရွက်စာတမ်းများကို ကိုးကားပါ။

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## အနှစ်ချုပ်

သင်သည် Azure ပေါ်တယ်ကို အသုံးပြု၍ Azure AI ရှာဖွေရေးကို အောင်မြင်စွာ ပြင်ဆင်ပြီး ကိရိယာများနှင့် ပေါင်းစပ်နိုင်ခဲ့ပါပြီ။ ယခုမှ Advanced features နှင့် စွမ်းဆောင်ရည်များကို လေ့လာကာ သင့် ရှာဖွေရေး ဖြေရှင်းချက်များကို မြှင့်တင်နိုင်ပါပြီ။

လိုအပ်သည်များအတွက် [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ကို သွားရောက်ကြည့်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->