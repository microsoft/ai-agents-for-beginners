# ایزور اے آئی سرچ سیٹ اپ گائیڈ

یہ رہنما آپ کو ایزور پورٹل استعمال کرتے ہوئے ایزور اے آئی سرچ سیٹ اپ کرنے میں مدد دے گی۔ اپنے ایزور اے آئی سرچ سروس کو بنانے اور ترتیب دینے کے لیے نیچے دیے گئے مراحل پر عمل کریں۔

## ضروریات

شروع کرنے سے پہلے، یقینی بنائیں کہ آپ کے پاس درج ذیل ہے:

- ایک ایزور سبسکرپشن۔ اگر آپ کے پاس ایزور سبسکرپشن نہیں ہے، تو آپ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) پر مفت اکاؤنٹ بنا سکتے ہیں۔

## مرحلہ 1: ایک ایزور اسٹوریج اکاؤنٹ بنائیں

1. اس ہدایت نامے، [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)، کی پیروی کریں تاکہ نیا ایزور اسٹوریج اکاؤنٹ بنایا جا سکے۔
   **نوٹ**: یقینی بنائیں کہ اسٹوریج اکاؤنٹ کی قسم Standard General Purpose V2 ہے۔

## مرحلہ 2: ایک ایزور اے آئی سرچ سروس بنائیں

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) میں سائن ان کریں۔
2. بائیں طرف کے نیویگیشن پین میں، **Create a resource** پر کلک کریں۔
3. سرچ باکس میں "Azure AI Search" ٹائپ کریں اور نتائج کی فہرست سے **Azure AI Search** منتخب کریں۔
4. **Create** بٹن پر کلک کریں۔
5. **Basics** ٹیب میں درج ذیل معلومات فراہم کریں:
   - **Subscription**: اپنی ایزور سبسکرپشن منتخب کریں۔
   - **Resource group**: نیا ریسورس گروپ بنائیں یا موجودہ میں سے کوئی منتخب کریں۔
   - **Resource name**: اپنی سرچ سروس کے لیے ایک منفرد نام درج کریں۔
   - **Region**: اپنے صارفین کے قریب ترین علاقہ منتخب کریں۔
   - **Pricing tier**: اپنی ضروریات کے مطابق ایک قیمت بندی کا درجہ منتخب کریں۔ آپ ٹیسٹنگ کے لیے مفت درجے سے شروع کر سکتے ہیں۔
6. **Review + create** پر کلک کریں۔
7. ترتیبات کا جائزہ لیں اور سرچ سروس بنانے کے لیے **Create** پر کلک کریں۔

## مرحلہ 3: ایزور اے آئی سرچ کے ساتھ شروع کریں

1. جب تعیناتی مکمل ہو جائے تو، ایزور پورٹل میں اپنی سرچ سروس پر جائیں۔
2. سرچ سروس اوورویو پین میں URL کو کاپی کریں۔ اس کا اندازہ لگ بھگ `https://<service-name>.search.windows.net` ہوگا۔
3. **(تجویز کردہ)** مائیکروسافٹ اینٹرا آئی ڈی (RBAC) کے ساتھ بغیر کلید کے رسائی فعال کریں جیسا کہ نیچے مرحلہ 4 میں دکھایا گیا ہے — کلید کی ضرورت نہیں۔ اس گائیڈ کے نمونے انڈیکس بنانے/اپ ڈیٹ کرنے اور دستاویزات اپ لوڈ کرنے کے لیے **Search Service Contributor** اور **Search Index Data Contributor** رولز کی ضرورت رکھتے ہیں (یا کلید کی بنیاد پر تصدیق کے لیے، **primary admin key** — کوئری کلید نہیں)۔ اگر آپ RBAC استعمال نہیں کر سکتے تو، **Settings > Keys** پین کھولیں اور **primary admin key** کی کاپی کریں۔
4. انڈیکس بنانے، ڈیٹا اپ لوڈ کرنے، اور سرچ کرنے کے لیے [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) صفحے میں دیے گئے مراحل پر عمل کریں۔

## مرحلہ 4: ایزور اے آئی سرچ ٹولز استعمال کریں

ایزور اے آئی سرچ مختلف ٹولز کے ساتھ مربوط ہوتا ہے تاکہ آپ کی تلاش کی صلاحیتوں کو بہتر بنایا جا سکے۔ آپ Azure CLI، Python SDK، .NET SDK اور دیگر ٹولز کو جدید ترتیبات اور آپریشنز کے لیے استعمال کر سکتے ہیں۔

### Azure CLI استعمال کرنا

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) پر دی گئی ہدایات کی پیروی کرتے ہوئے Azure CLI انسٹال کریں۔
2. Azure CLI میں سائن ان کرنے کے لیے کمانڈ استعمال کریں:

   ```bash
   az login
   ```
3. **(تجویز کردہ) مائیکروسافٹ اینٹرا آئی ڈی (RBAC) کے ساتھ بغیر کلید کے رسائی فعال کریں:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC فعال ہونے کے ساتھ، نیچے دیے گئے Python اور .NET SDK نمونے `DefaultAzureCredential` کے ساتھ تصدیق کرتے ہیں، جو آپ کے `az login` سیشن کا استعمال لوکل ڈیولپمنٹ کے دوران کرتے ہیں — ایڈمن کی ضرورت نہیں۔ مزید جاننے کے لیے [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) دیکھیں۔

4. **(اختیاری) کلید کی بنیاد پر تصدیق** — صرف اگر آپ RBAC استعمال نہیں کر سکتے، ایڈمن کلید کو بھی محفوظ کریں:

#### ایزور اے آئی سرچ انسٹینس کے اینڈ پوائنٹ اور API کی دونوں کو ماحولیاتی متغیرات میں محفوظ کریں۔

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

### Python SDK استعمال کرنا

1. Azure Cognitive Search کلائنٹ لائبریری اور Azure Identity for Python انسٹال کریں:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. انڈیکس بنانے اور دستاویزات اپ لوڈ کرنے کے لیے درج ذیل Python کوڈ استعمال کریں:

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

### .NET SDK استعمال کرنا

1. انڈیکس بنانے اور دستاویزات اپ لوڈ کرنے کے لیے درج ذیل کمانڈ چلائیں:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    نیچے دیا گیا .NET نمونہ `DefaultAzureCredential` استعمال کرتا ہے، جو آپ کے Azure CLI سائن ان کو لوکل ڈیولپمنٹ کے دوران `az login` سے استعمال کر سکتا ہے۔

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

مزید تفصیلی معلومات کے لیے، درج ذیل دستاویزات ملاحظہ کریں:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## نتیجہ

آپ نے کامیابی سے ایزور پورٹل اور مربوط ٹولز کا استعمال کرتے ہوئے ایزور اے آئی سرچ سیٹ اپ کر لیا ہے۔ آپ اب ایزور اے آئی سرچ کی مزید جدید خصوصیات اور صلاحیتوں کو دریافت کر کے اپنی تلاش کے حل کو بہتر بنا سکتے ہیں۔

مزید مدد کے لیے، [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ملاحظہ کریں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈس کلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ جبکہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم اس بات سے آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنے مادری زبان میں مستند ماخذ سمجھی جائے گی۔ حساس معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم قبول نہیں کرتے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->