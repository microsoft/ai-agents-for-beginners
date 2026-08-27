# ایژور اے آئی سرچ سیٹ اپ گائیڈ

یہ گائیڈ آپ کو ایژور پورٹل کا استعمال کرتے ہوئے ایژور اے آئی سرچ سیٹ اپ کرنے میں مدد دے گا۔ نیچے دیے گئے مراحل پر عمل کریں تاکہ اپنا ایژور اے آئی سرچ سروس بنائیں اور ترتیب دیں۔

## ضروریات

شروع کرنے سے پہلے، یقینی بنائیں کہ آپ کے پاس درج ذیل چیزیں موجود ہیں:

- ایک ایژور سبسکرپشن۔ اگر آپ کے پاس ایژور سبسکرپشن نہیں ہے، تو آپ ایک مفت اکاؤنٹ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) پر بنا سکتے ہیں۔

## مرحلہ 1: ایژور اسٹوریج اکاؤنٹ بنائیں

1. اس ہدایت پر عمل کریں، [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)، تاکہ نیا ایژور اسٹوریج اکاؤنٹ بنایا جا سکے۔
   **نوٹ**: یقینی بنائیں کہ اسٹوریج اکاؤنٹ کی قسم اسٹینڈرڈ جنرل پرپز V2 ہو۔

## مرحلہ 2: ایژور اے آئی سرچ سروس بنائیں

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) میں سائن ان کریں۔
2. بائیں جانب نیویگیشن پین میں، **Create a resource** پر کلک کریں۔
3. سرچ باکس میں "Azure AI Search" لکھیں اور نتیجوں کی فہرست میں سے **Azure AI Search** منتخب کریں۔
4. **Create** بٹن پر کلک کریں۔
5. **Basics** ٹیب میں، درج ذیل معلومات فراہم کریں:
   - **Subscription**: اپنا ایژور سبسکرپشن منتخب کریں۔
   - **Resource group**: ایک نیا ریسورس گروپ بنائیں یا موجودہ کو منتخب کریں۔
   - **Resource name**: اپنی سرچ سروس کے لیے ایک منفرد نام درج کریں۔
   - **Region**: اپنے صارفین کے قریب ترین خطہ منتخب کریں۔
   - **Pricing tier**: اپنی ضروریات کے مطابق پرائسنگ ٹئیر منتخب کریں۔ آپ ٹیسٹ کے لیے Free tier سے شروع کر سکتے ہیں۔
6. **Review + create** پر کلک کریں۔
7. ترتیبات کا جائزہ لیں اور سرچ سروس بنانے کے لیے **Create** پر کلک کریں۔

## مرحلہ 3: ایژور اے آئی سرچ کے ساتھ شروع کریں

1. تعیناتی مکمل ہونے پر، ایژور پورٹل میں اپنی سرچ سروس پر جائیں۔
2. سرچ سروس اووروریو پین میں، URL کی کاپی کریں۔ یہ کچھ اس طرح لگنا چاہیے `https://<service-name>.search.windows.net`۔
3. **(تجویز کردہ)** مائیکروسافٹ اینٹرا آئی ڈی (RBAC) کے ساتھ کی لیس رسائی فعال کریں جیسا کہ نیچے مرحلہ 4 میں دکھایا گیا ہے — کوئی کی ضرورت نہیں۔ اس گائیڈ کے نمونے انڈیکس بنانے/اپڈیٹ کرنے اور دستاویزات اپلوڈ کرنے کے لیے **Search Service Contributor** اور **Search Index Data Contributor** رولز کی ضرورت رکھتے ہیں (یا کی کی بنیاد پر تصدیق کے لیے، **primary admin key** — query key نہیں)۔ صرف اگر آپ RBAC استعمال نہیں کر سکتے، تو **Settings > Keys** پین کھولیں اور **primary admin key** کو کاپی کریں۔
4. انڈیکس بنانے، ڈیٹا اپلوڈ کرنے، اور سرچ کرنے کے لیے [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) صفحہ پر دیے گئے مراحل پر عمل کریں۔

## مرحلہ 4: ایژور اے آئی سرچ ٹولز کا استعمال

ایژور اے آئی سرچ مختلف ٹولز کے ساتھ مطابقت رکھتا ہے تاکہ آپ کی سرچ صلاحیتوں کو بڑھایا جا سکے۔ آپ اعلی ترتیبات اور آپریشنز کے لیے Azure CLI، Python SDK، .NET SDK اور دیگر ٹولز استعمال کر سکتے ہیں۔

### Azure CLI کا استعمال

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) پر دی گئی ہدایات پر عمل کرتے ہوئے Azure CLI انسٹال کریں۔
2. Azure CLI میں سائن ان کریں:

   ```bash
   az login
   ```
3. **(تجویز کردہ) مائیکروسافٹ اینٹرا آئی ڈی (RBAC) کے ساتھ کی لیس رسائی کو فعال کریں:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # اے زی سرچ سروس شو میں "این پوائنٹ" فیلڈ نہیں ہے؛ سروس کے نام سے یو آر ایل بنائیں۔
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC فعال ہونے پر، نیچے دیے گئے Python اور .NET SDK نمونے `DefaultAzureCredential` کے ساتھ تصدیق کرتے ہیں، جو لوکل ڈویلپمنٹ کے دوران آپ کے `az login` سیشن کا استعمال کرتا ہے — ایڈمن کی کی کوئی ضرورت نہیں۔ دیکھیں [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)۔

4. **(متبادل) کی کی بنیاد پر تصدیق** — صرف اگر آپ RBAC استعمال نہیں کر سکتے، تو ایڈمن کی بھی محفوظ کریں:

#### ایژور اے آئی سرچ انسٹنس کے لیے اینڈپوائنٹ اور API کی دونوں کو ماحول کی متغیرات میں محفوظ کریں۔

    ```bash
    # zsh/bash
    # az search service show میں "endpoint" فیلڈ نہیں ہے؛ URL سروس نام سے بنائیں۔
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show میں "endpoint" فیلڈ نہیں ہے؛ URL سروس نام سے بنائیں۔
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK کا استعمال

1. Azure Cognitive Search کلائنٹ لائبریری اور Azure Identity for Python انسٹال کریں:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. انڈیکس بنانے اور دستاویزات اپلوڈ کرنے کے لیے درج ذیل Python کوڈ استعمال کریں:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # بے کلید (تجویز کردہ): آپ کی `az login` شناخت کو Entra ID RBAC کے ذریعے استعمال کرتا ہے۔
    # "Search Service Contributor" اور "Search Index Data Contributor" کرداروں کی ضرورت ہے۔
    credential = DefaultAzureCredential()
    # متبادل (کلید کی بنیاد پر تصدیق):
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

1. انڈیکس بنانے اور دستاویزات اپلوڈ کرنے کے لیے درج ذیل کمانڈ چلائیں:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    نیچے دیا گیا .NET نمونہ `DefaultAzureCredential` استعمال کرتا ہے، جو لوکل ڈویلپمنٹ کے دوران آپ کے Azure CLI کے `az login` سے سائن ان کو استعمال کر سکتا ہے۔

2. یہاں `AzureSearch.cs` کا .NET کوڈ ہے:

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

مزید تفصیلی معلومات کے لیے درج ذیل دستاویزات ملاحظہ کریں:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## نتیجہ

آپ نے کامیابی کے ساتھ ایژور پورٹل اور مربوط ٹولز کا استعمال کرتے ہوئے ایژور اے آئی سرچ سیٹ اپ کر لیا ہے۔ اب آپ ایژور اے آئی سرچ کی مزید اعلی خصوصیات اور صلاحیتوں کو دریافت کر کے اپنی سرچ سلوشنز کو بہتر بنا سکتے ہیں۔

مزید معاونت کے لیے، [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ملاحظہ کریں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->