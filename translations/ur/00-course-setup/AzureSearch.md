# ایزور اے آئی سرچ سیٹ اپ گائیڈ

یہ گائیڈ آپ کی مدد کرے گا کہ آپ ایزور پورٹل استعمال کرتے ہوئے ایزور اے آئی سرچ سیٹ اپ کریں۔ نیچے دیے گئے مراحل پر عمل کریں تاکہ آپ اپنی ایزور اے آئی سرچ سروس بنا سکیں اور اس کی تشکیلات مکمل کر سکیں۔

## ضروری تقاضے

شروع کرنے سے پہلے، یقینی بنائیں کہ آپ کے پاس درج ذیل چیزیں موجود ہیں:

- ایک ایزور سبسکرپشن۔ اگر آپ کے پاس ایزور سبسکرپشن نہیں ہے تو، آپ ایک مفت اکاؤنٹ یہاں بنا سکتے ہیں [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691)۔

## مرحلہ 1: ایک ایزور اسٹوریج اکاؤنٹ بنائیں

1۔ اس ہدایت پر عمل کریں، [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)، تاکہ ایک نیا ایزور اسٹوریج اکاؤنٹ بنائیں۔
   **نوٹ**: یقینی بنائیں کہ اسٹوریج اکاؤنٹ کی قسم Standard General Purpose V2 ہو۔

## مرحلہ 2: ایک ایزور اے آئی سرچ سروس بنائیں

1۔ [ایزور پورٹل](https://portal.azure.com/?wt.mc_id=studentamb_258691) میں سائن ان کریں۔
2۔ بائیں طرف والے نیویگیشن پین میں **Create a resource** پر کلک کریں۔
3۔ سرچ باکس میں "Azure AI Search" لکھیں اور نتائج کی فہرست سے **Azure AI Search** کو منتخب کریں۔
4۔ **Create** بٹن پر کلک کریں۔
5۔ **Basics** ٹیب میں درج ذیل معلومات فراہم کریں:
   - **Subscription**: اپنی ایزور سبسکرپشن منتخب کریں۔
   - **Resource group**: ایک نیا ریسورس گروپ بنائیں یا موجودہ میں سے منتخب کریں۔
   - **Resource name**: اپنی سرچ سروس کے لیے ایک منفرد نام درج کریں۔
   - **Region**: اپنے صارفین کے قریب ترین ریجن منتخب کریں۔
   - **Pricing tier**: اپنی ضرورت کے مطابق ایک قیمت کی سطح منتخب کریں۔ آپ ٹیسٹنگ کے لیے Free tier سے شروع کر سکتے ہیں۔
6۔ **Review + create** پر کلک کریں۔
7۔ سیٹنگز کا جائزہ لیں اور سرچ سروس بنانے کے لیے **Create** پر کلک کریں۔

## مرحلہ 3: ایزور اے آئی سرچ کے ساتھ شروعات کریں

1۔ ایک بار تعیناتی مکمل ہو جائے، ایزور پورٹل میں اپنی سرچ سروس پر جائیں۔
2۔ سرچ سروس اوورویو پین میں URL کو کاپی کریں۔ یہ کچھ اس طرح نظر آنا چاہئے `https://<service-name>.search.windows.net`۔
3۔ **(تجویز کردہ)** Microsoft Entra ID (RBAC) کے ساتھ کی لیس رسائی فعال کریں جیسا کہ نیچے مرحلہ 4 میں دکھایا گیا ہے — کوئی کی ضروری نہیں۔ اس گائیڈ کے نمونے انڈیکسز بنانے/اپ ڈیٹ کرنے اور دستاویزات اپ لوڈ کرنے کے لیے **Search Service Contributor** اور **Search Index Data Contributor** رولز کی ضرورت ہے (یا، کی بیسڈ تصدیق کے لیے، **primary admin key** — کوئری کی نہیں)۔ صرف اگر آپ RBAC استعمال نہیں کر سکتے تو **Settings > Keys** پین کھولیں اور **primary admin key** کاپی کریں۔
4۔ [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) صفحے میں دیے گئے مراحل پر عمل کریں تاکہ انڈیکس بنائیں، ڈیٹا اپ لوڈ کریں، اور سرچ کریں۔

## مرحلہ 4: ایزور اے آئی سرچ کے ٹولز استعمال کریں

ایزور اے آئی سرچ مختلف ٹولز کے ساتھ ایک ساتھ کام کرتا ہے تاکہ آپ کی سرچ کی صلاحیتوں کو بہتر بنایا جا سکے۔ آپ ایزور CLI، پائتھون SDK، .NET SDK اور دیگر ٹولز جدید تشکیلات اور آپریشنز کے لیے استعمال کر سکتے ہیں۔

### ایزور CLI کا استعمال

1۔ [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) پر دی گئی ہدایات کے مطابق ایزور CLI انسٹال کریں۔
2۔ ایزور CLI میں سائن ان کریں:

   ```bash
   az login
   ```
3۔ **(تجویز کردہ) Microsoft Entra ID (RBAC) کے ساتھ کی لیس رسائی فعال کریں:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az سرچ سروس شو میں "endpoint" فیلڈ نہیں ہے؛ URL سروس کے نام سے بنائیں۔
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC فعال ہونے پر، نیچے دی گئی پائتھون اور .NET SDK کے نمونے `DefaultAzureCredential` کے ساتھ تصدیق کرتے ہیں، جو آپ کے `az login` سیشن کو لوکل ترقی کے دوران استعمال کرتا ہے — کوئی ایڈمن کی ضرورت نہیں۔ دیکھیں [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)۔

4۔ **(متبادل) کی بیسڈ تصدیق** — صرف اگر آپ RBAC استعمال نہیں کر سکتے تو ایڈمن کی کو بھی محفوظ کریں:

#### ایزور اے آئی سرچ کی مثال کے لیے اینڈپوائنٹ اور API کی کو ماحول کے متغیرات میں محفوظ کریں۔

    ```bash
    # zsh/bash
    # az search service show میں "endpoint" فیلڈ نہیں ہے؛ سروس کے نام سے URL بنائیں۔
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show میں "endpoint" فیلڈ نہیں ہے؛ سروس کے نام سے URL بنائیں۔
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### پائتھون SDK کا استعمال

1۔ ایزور کوگنیٹو سرچ کلائنٹ لائبریری اور ایزور آئیڈینٹیٹی برائے پائتھون انسٹال کریں:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2۔ انڈیکس بنانے اور دستاویزات اپ لوڈ کرنے کے لیے درج ذیل پائتھون کوڈ استعمال کریں:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # بغیر کلید (تجویز کردہ): آپ کی `az login` شناخت کو Entra ID RBAC کے ذریعے استعمال کرتا ہے۔
    # "Search Service Contributor" اور "Search Index Data Contributor" کرداروں کی ضرورت ہے۔
    credential = DefaultAzureCredential()
    # بیک اپ (کلید کی بنیاد پر تصدیق):
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

### .NET SDK کا استعمال

1۔ انڈیکس بنانے اور دستاویزات اپ لوڈ کرنے کے لیے درج ذیل کمانڈ چلائیں:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    نیچے دیا گیا .NET نمونہ `DefaultAzureCredential` استعمال کرتا ہے، جو لوکل ترقی کے دوران `az login` سے آپ کے ایزور CLI سائن ان کو استعمال کر سکتا ہے۔

2۔ یہ ہے .NET کوڈ `AzureSearch.cs` کا:

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

مزید تفصیلی معلومات کے لیے درج ذیل ڈاکیومنٹیشن کو ملاحظہ کریں:

- [ایزور کوگنیٹو سرچ سروس بنائیں](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [ایزور کوگنیٹو سرچ کے ساتھ شروعات کریں](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [ایزور اے آئی سرچ ٹولز](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## نتیجہ

آپ نے کامیابی کے ساتھ ایزور پورٹل اور مربوط ٹولز استعمال کرتے ہوئے ایزور اے آئی سرچ سیٹ اپ کر لیا ہے۔ اب آپ ایزور اے آئی سرچ کی مزید جدید خصوصیات اور صلاحیتوں کو دریافت کر سکتے ہیں تاکہ اپنی سرچ حل کو بہتر بنائیں۔

مزید مدد کے لیے، [ایزور کوگنیٹو سرچ کی ڈاکیومنٹیشن](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ملاحظہ کریں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->