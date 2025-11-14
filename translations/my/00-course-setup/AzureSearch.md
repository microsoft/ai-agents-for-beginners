<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:51:43+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "my"
}
-->
# Azure AI Search Setup Guide

ဤလမ်းညွှန်သည် Azure portal ကို အသုံးပြု၍ Azure AI Search ကို စတင်တပ်ဆင်ရန် ကူညီပေးပါမည်။ Azure AI Search service ကို ဖန်တီးပြီး ဖွဲ့စည်းရန် အောက်ပါအဆင့်များကို လိုက်နာပါ။

## မလိုအပ်မဖြစ်လိုအပ်သောအရာများ

စတင်မလုပ်မီ အောက်ပါအရာများရှိကြောင်း သေချာပါစေ-

- Azure subscription တစ်ခု။ သင်တွင် Azure subscription မရှိပါက [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) တွင် အခမဲ့အကောင့် ဖန်တီးနိုင်ပါသည်။

## အဆင့် ၁: Azure Storage Account တစ်ခု ဖန်တီးပါ

1. [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) လမ်းညွှန်ကို လိုက်နာပြီး Azure Storage Account အသစ်တစ်ခု ဖန်တီးပါ။
   **NOTE**: Storage Account အမျိုးအစားသည် Standard General Purpose V2 ဖြစ်ကြောင်း သေချာပါစေ။

## အဆင့် ၂: Azure AI Search Service တစ်ခု ဖန်တီးပါ

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) တွင် လက်မှတ်ထိုးဝင်ပါ။
2. ဘယ်ဘက် navigation pane တွင် **Create a resource** ကို နှိပ်ပါ။
3. ရှာဖွေမှု box တွင် "Azure AI Search" ဟု ရိုက်ထည့်ပြီး ရလဒ်များထဲမှ **Azure AI Search** ကို ရွေးပါ။
4. **Create** ခလုတ်ကို နှိပ်ပါ။
5. **Basics** tab တွင် အောက်ပါအချက်အလက်များကို ဖြည့်ပါ-
   - **Subscription**: သင့် Azure subscription ကို ရွေးပါ။
   - **Resource group**: Resource group အသစ်တစ်ခု ဖန်တီးပါ သို့မဟုတ် ရှိပြီးသားကို ရွေးပါ။
   - **Resource name**: သင့် search service အတွက် ထူးခြားသောနာမည်တစ်ခု ထည့်ပါ။
   - **Region**: သင့်အသုံးပြုသူများအနီးဆုံးရှိဒေသကို ရွေးပါ။
   - **Pricing tier**: သင့်လိုအပ်ချက်များနှင့် ကိုက်ညီသော pricing tier ကို ရွေးပါ။ စမ်းသပ်ရန် Free tier ဖြင့် စတင်နိုင်ပါသည်။
6. **Review + create** ကို နှိပ်ပါ။
7. အချက်အလက်များကို ပြန်လည်သုံးသပ်ပြီး **Create** ကို နှိပ်၍ search service ကို ဖန်တီးပါ။

## အဆင့် ၃: Azure AI Search ကို စတင်အသုံးပြုပါ

1. Deployment ပြီးဆုံးသောအခါ Azure portal တွင် သင့် search service သို့ သွားပါ။
2. Search service overview pane တွင် URL ကို ကူးယူပါ။ ၎င်းသည် `https://<service-name>.search.windows.net` အတိုင်း ဖြစ်ရမည်။
3. Settings > Keys pane တွင် query key ကို ကူးယူပါ။
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) စာမျက်နှာရှိ အဆင့်များကို လိုက်နာ၍ index ဖန်တီးပါ၊ data upload လုပ်ပါ၊ search query တစ်ခု ပြုလုပ်ပါ။

## အဆင့် ၄: Azure AI Search Tools ကို အသုံးပြုပါ

Azure AI Search သည် သင့် search စွမ်းရည်များကို တိုးတက်စေရန် အမျိုးမျိုးသော tools များနှင့် ပေါင်းစပ်ထားသည်။ Advanced configurations နှင့် operations များအတွက် Azure CLI, Python SDK, .NET SDK နှင့် အခြား tools များကို အသုံးပြုနိုင်ပါသည်။

### Azure CLI ကို အသုံးပြုခြင်း

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) လမ်းညွှန်ကို လိုက်နာ၍ Azure CLI ကို install လုပ်ပါ။
2. အောက်ပါ command ကို အသုံးပြု၍ Azure CLI တွင် လက်မှတ်ထိုးဝင်ပါ-

   ```bash
   az login
   ```

3. Azure AI Search instance အတွက် endpoint နှင့် API key ကို environment variables တွင် သိမ်းဆည်းပါ။

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

### Python SDK ကို အသုံးပြုခြင်း

1. Azure Cognitive Search client library for Python ကို install လုပ်ပါ-

   ```bash
   pip install azure-search-documents
   ```

2. အောက်ပါ Python code ကို အသုံးပြု၍ index ဖန်တီးပြီး documents upload လုပ်ပါ-

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

### .NET SDK ကို အသုံးပြုခြင်း

1. အောက်ပါ command ကို run လုပ်၍ index ဖန်တီးပြီး documents upload လုပ်ပါ-

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. `AzureSearch.cs` ၏ .NET code ကို အောက်ပါအတိုင်း ဖြစ်ပါသည်-

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

အသေးစိတ်အချက်အလက်များအတွက် အောက်ပါ documentation ကို ရည်ညွှန်းပါ-

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## နိဂုံး

သင်သည် Azure portal ကို အသုံးပြု၍ Azure AI Search ကို အောင်မြင်စွာ တပ်ဆင်ပြီး tools များနှင့် ပေါင်းစပ်ထားပါပြီ။ Azure AI Search ၏ အဆင့်မြင့် features များနှင့် စွမ်းရည်များကို ရှာဖွေပြီး သင့် search solutions ကို တိုးတက်စေရန် အခွင့်အရေးရှိပါသည်။

ထပ်မံအကူအညီလိုအပ်ပါက [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) သို့ သွားပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။