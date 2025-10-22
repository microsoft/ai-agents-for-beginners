<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:41:00+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "my"
}
-->
# Azure AI Search စတင်အသုံးပြုခြင်းလမ်းညွှန်

ဤလမ်းညွှန်သည် Azure portal ကို အသုံးပြု၍ Azure AI Search ကို စတင်တပ်ဆင်ရန် ကူညီပေးပါမည်။ အောက်ပါအဆင့်များကို လိုက်နာပြီး သင့် Azure AI Search ဝန်ဆောင်မှုကို ဖန်တီး၊ ပြင်ဆင်နိုင်ပါသည်။

## မတိုင်မီလိုအပ်ချက်များ

စတင်မလုပ်မီ အောက်ပါအချက်များရှိကြောင်း သေချာစေပါ။

- Azure subscription တစ်ခု။ Azure subscription မရှိပါက [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) မှာ အခမဲ့အကောင့်ဖန်တီးနိုင်ပါသည်။

## အဆင့် ၁: Azure AI Search ဝန်ဆောင်မှု ဖန်တီးခြင်း

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) တွင် လက်မှတ်ထိုးဝင်ပါ။
2. ဘယ်ဘက် navigation panel တွင် **Create a resource** ကိုနှိပ်ပါ။
3. ရှာဖွေရေးဘောက်စ်တွင် "Azure AI Search" ဟု ရိုက်ထည့်ပြီး ရလဒ်စာရင်းမှ **Azure AI Search** ကို ရွေးချယ်ပါ။
4. **Create** ခလုတ်ကို နှိပ်ပါ။
5. **Basics** တက်ဘ်တွင် အောက်ပါအချက်များကို ဖြည့်ပါ။
   - **Subscription**: သင့် Azure subscription ကို ရွေးချယ်ပါ။
   - **Resource group**: အသစ် resource group ဖန်တီးရန် သို့မဟုတ် ရှိပြီးသား resource group တစ်ခုကို ရွေးချယ်ပါ။
   - **Resource name**: သင့် search ဝန်ဆောင်မှုအတွက် ထူးခြားသော နာမည်တစ်ခု ထည့်ပါ။
   - **Region**: သင့်အသုံးပြုသူများနီးစပ်ရာ ဒေသကို ရွေးချယ်ပါ။
   - **Pricing tier**: သင့်လိုအပ်ချက်နှင့် ကိုက်ညီသော စျေးနှုန်းအဆင့်ကို ရွေးချယ်ပါ။ စမ်းသပ်ရန် Free tier ဖြင့် စတင်နိုင်ပါသည်။
6. **Review + create** ကို နှိပ်ပါ။
7. ဆက်လက်စစ်ဆေးပြီး **Create** ကို နှိပ်၍ search ဝန်ဆောင်မှုကို ဖန်တီးပါ။

## အဆင့် ၂: Azure AI Search ကို စတင်အသုံးပြုခြင်း

1. တပ်ဆင်မှု ပြီးဆုံးသည့်အခါ Azure portal တွင် သင့် search ဝန်ဆောင်မှုသို့ သွားပါ။
2. Search ဝန်ဆောင်မှု အနှစ်ချုပ်စာမျက်နှာတွင် **Quickstart** ခလုတ်ကို နှိပ်ပါ။
3. Quickstart လမ်းညွှန်အတိုင်း index ဖန်တီးခြင်း၊ ဒေတာတင်ခြင်းနှင့် ရှာဖွေရေးမေးခွန်း တင်ခြင်း အဆင့်များကို လိုက်နာပါ။

### Index ဖန်တီးခြင်း

1. Quickstart လမ်းညွှန်တွင် **Create an index** ကို နှိပ်ပါ။
2. Index schema ကို ဖော်ပြပါ။ (ဥပမာ - ဒေတာအမျိုးအစား၊ ရှာဖွေရန်အတွက် အသုံးပြုနိုင်မှု၊ စစ်ထုတ်နိုင်မှု စသည့် attribute များ)
3. **Create** ကို နှိပ်၍ index ကို ဖန်တီးပါ။

### ဒေတာတင်ခြင်း

1. Quickstart လမ်းညွှန်တွင် **Upload data** ကို နှိပ်ပါ။
2. ဒေတာရင်းမြစ် (ဥပမာ - Azure Blob Storage, Azure SQL Database) ကို ရွေးချယ်ပြီး လိုအပ်သော ချိတ်ဆက်မှု အသေးစိတ်များကို ဖြည့်ပါ။
3. ဒေတာရင်းမြစ်၏ field များကို index field များနှင့် တွဲဖက်ပါ။
4. **Submit** ကို နှိပ်၍ ဒေတာကို index သို့ တင်ပါ။

### ရှာဖွေရေးမေးခွန်း တင်ခြင်း

1. Quickstart လမ်းညွှန်တွင် **Search explorer** ကို နှိပ်ပါ။
2. ရှာဖွေရေးဘောက်စ်တွင် မေးခွန်းတစ်ခု ရိုက်ထည့်ပြီး ရှာဖွေရေး လုပ်ဆောင်မှုကို စမ်းသပ်ပါ။
3. ရလဒ်များကို ကြည့်ရှု၍ လိုအပ်သလို index schema သို့မဟုတ် ဒေတာကို ပြင်ဆင်ပါ။

## အဆင့် ၃: Azure AI Search ကိရိယာများ အသုံးပြုခြင်း

Azure AI Search သည် ရှာဖွေရေးစွမ်းရည်များ တိုးတက်စေရန် အမျိုးမျိုးသော ကိရိယာများနှင့် ပေါင်းစပ်အသုံးပြုနိုင်ပါသည်။ Azure CLI, Python SDK နှင့် အခြားကိရိယာများကို အသုံးပြု၍ တိုးတက်သော ပြင်ဆင်မှုများနှင့် လုပ်ဆောင်ချက်များ ပြုလုပ်နိုင်ပါသည်။

### Azure CLI အသုံးပြုခြင်း

1. [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) တွင် ဖော်ပြထားသည့် အညွှန်းများအတိုင်း Azure CLI ကို ထည့်သွင်းပါ။
2. အောက်ပါ command ဖြင့် Azure CLI တွင် လက်မှတ်ထိုးဝင်ပါ။
   ```bash
   az login
   ```
3. Azure CLI ကို အသုံးပြု၍ search ဝန်ဆောင်မှု အသစ် ဖန်တီးပါ။
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI ဖြင့် index ဖန်တီးပါ။
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK အသုံးပြုခြင်း

1. Python အတွက် Azure Cognitive Search client library ကို ထည့်သွင်းပါ။
   ```bash
   pip install azure-search-documents
   ```
2. အောက်ပါ Python ကုဒ်ကို အသုံးပြု၍ index ဖန်တီးခြင်းနှင့် စာရွက်စာတမ်းများ တင်ခြင်း ပြုလုပ်ပါ။
   ```python
   from azure.core.credentials import AzureKeyCredential
   from azure.search.documents import SearchClient
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

   service_endpoint = "https://<service-name>.search.windows.net"
   api_key = "<api-key>"

   index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))

   fields = [
       SimpleField(name="id", type=edm.String, key=True),
       SimpleField(name="content", type=edm.String, searchable=True),
   ]

   index = SearchIndex(name="sample-index", fields=fields)

   index_client.create_index(index)

   search_client = SearchClient(service_endpoint, "sample-index", AzureKeyCredential(api_key))

   documents = [
       {"id": "1", "content": "Hello world"},
       {"id": "2", "content": "Azure Cognitive Search"}
   ]

   search_client.upload_documents(documents)
   ```

အသေးစိတ်အချက်အလက်များအတွက် အောက်ပါစာရွက်စာတမ်းများကို ကြည့်ရှုနိုင်ပါသည်။

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## နိဂုံးချုပ်

Azure portal နှင့် ပေါင်းစပ်ကိရိယာများကို အသုံးပြု၍ Azure AI Search ကို အောင်မြင်စွာ တပ်ဆင်ပြီးဖြစ်ပါသည်။ ယခုအခါ Azure AI Search ၏ တိုးတက်သော လုပ်ဆောင်ချက်များနှင့် စွမ်းဆောင်ရည်များကို ပိုမိုလေ့လာနိုင်ပါပြီ။

ထပ်မံအကူအညီလိုပါက [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) ကို သွားရောက်ကြည့်ရှုနိုင်ပါသည်။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အချက်အလက်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။