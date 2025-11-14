<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:25:59+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ur"
}
-->
# Azure AI Search سیٹ اپ گائیڈ

یہ گائیڈ آپ کو Azure پورٹل کے ذریعے Azure AI Search سیٹ اپ کرنے میں مدد دے گا۔ Azure AI Search سروس بنانے اور ترتیب دینے کے لیے نیچے دیے گئے مراحل پر عمل کریں۔

## ضروریات

شروع کرنے سے پہلے، یقینی بنائیں کہ آپ کے پاس درج ذیل چیزیں موجود ہیں:

- ایک Azure سبسکرپشن۔ اگر آپ کے پاس Azure سبسکرپشن نہیں ہے، تو آپ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) پر مفت اکاؤنٹ بنا سکتے ہیں۔

## مرحلہ 1: Azure Storage اکاؤنٹ بنائیں

1. ایک نیا Azure Storage اکاؤنٹ بنانے کے لیے [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) ہدایات پر عمل کریں۔
   **نوٹ**: یقینی بنائیں کہ Storage اکاؤنٹ کی قسم Standard General Purpose V2 ہو۔

## مرحلہ 2: Azure AI Search سروس بنائیں

1. [Azure پورٹل](https://portal.azure.com/?wt.mc_id=studentamb_258691) میں سائن ان کریں۔
2. بائیں طرف نیویگیشن پین میں، **Create a resource** پر کلک کریں۔
3. سرچ باکس میں "Azure AI Search" ٹائپ کریں اور نتائج کی فہرست سے **Azure AI Search** منتخب کریں۔
4. **Create** بٹن پر کلک کریں۔
5. **Basics** ٹیب میں درج ذیل معلومات فراہم کریں:
   - **Subscription**: اپنی Azure سبسکرپشن منتخب کریں۔
   - **Resource group**: ایک نیا ریسورس گروپ بنائیں یا موجودہ کو منتخب کریں۔
   - **Resource name**: اپنی سرچ سروس کے لیے ایک منفرد نام درج کریں۔
   - **Region**: اپنے صارفین کے قریب ترین علاقہ منتخب کریں۔
   - **Pricing tier**: اپنی ضروریات کے مطابق قیمت کا درجہ منتخب کریں۔ آپ ٹیسٹنگ کے لیے Free tier سے شروع کر سکتے ہیں۔
6. **Review + create** پر کلک کریں۔
7. سیٹنگز کا جائزہ لیں اور سرچ سروس بنانے کے لیے **Create** پر کلک کریں۔

## مرحلہ 3: Azure AI Search کے ساتھ شروعات کریں

1. جب ڈیپلائمنٹ مکمل ہو جائے، تو Azure پورٹل میں اپنی سرچ سروس پر جائیں۔
2. سرچ سروس کے اوورویو پین میں، URL کو کاپی کریں۔ یہ کچھ اس طرح نظر آنا چاہیے: `https://<service-name>.search.windows.net`۔
3. Settings > Keys پین میں، query key کو کاپی کریں۔
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) صفحے پر دیے گئے مراحل پر عمل کریں تاکہ ایک انڈیکس بنائیں، ڈیٹا اپلوڈ کریں، اور سرچ کوئری انجام دیں۔

## مرحلہ 4: Azure AI Search ٹولز استعمال کریں

Azure AI Search مختلف ٹولز کے ساتھ انٹیگریٹ ہوتا ہے تاکہ آپ کی سرچ صلاحیتوں کو بہتر بنایا جا سکے۔ آپ Azure CLI، Python SDK، .NET SDK اور دیگر ٹولز کو ایڈوانس کنفیگریشنز اور آپریشنز کے لیے استعمال کر سکتے ہیں۔

### Azure CLI استعمال کرتے ہوئے

1. Azure CLI انسٹال کرنے کے لیے [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) ہدایات پر عمل کریں۔
2. درج ذیل کمانڈ کے ذریعے Azure CLI میں سائن ان کریں:

   ```bash
   az login
   ```

3. Azure AI Search انسٹینس کے لیے endpoint اور API key کو ماحول کے متغیرات میں محفوظ کریں۔

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

### Python SDK استعمال کرتے ہوئے

1. Python کے لیے Azure Cognitive Search کلائنٹ لائبریری انسٹال کریں:

   ```bash
   pip install azure-search-documents
   ```

2. درج ذیل Python کوڈ استعمال کریں تاکہ ایک انڈیکس بنائیں اور دستاویزات اپلوڈ کریں:

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

### .NET SDK استعمال کرتے ہوئے

1. درج ذیل کمانڈ چلائیں تاکہ ایک انڈیکس بنائیں اور دستاویزات اپلوڈ کریں:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. یہاں `AzureSearch.cs` کا .NET کوڈ ہے:

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

مزید تفصیلی معلومات کے لیے درج ذیل دستاویزات دیکھیں:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## نتیجہ

آپ نے کامیابی سے Azure پورٹل کے ذریعے Azure AI Search سیٹ اپ کر لیا ہے اور ٹولز کو انٹیگریٹ کیا ہے۔ اب آپ Azure AI Search کی مزید ایڈوانس خصوصیات اور صلاحیتوں کو دریافت کر سکتے ہیں تاکہ اپنی سرچ سلوشنز کو بہتر بنایا جا سکے۔

مزید مدد کے لیے، [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) پر جائیں۔

---

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔