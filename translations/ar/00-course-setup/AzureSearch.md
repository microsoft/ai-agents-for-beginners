<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:24:35+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ar"
}
-->
# دليل إعداد Azure AI Search

سيساعدك هذا الدليل في إعداد Azure AI Search باستخدام بوابة Azure. اتبع الخطوات أدناه لإنشاء وتكوين خدمة Azure AI Search الخاصة بك.

## المتطلبات الأساسية

قبل أن تبدأ، تأكد من توفر ما يلي:

- اشتراك في Azure. إذا لم يكن لديك اشتراك في Azure، يمكنك إنشاء حساب مجاني على [حساب Azure المجاني](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## الخطوة 1: إنشاء حساب تخزين Azure

1. اتبع التعليمات الموجودة في [إنشاء حساب تخزين Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) لإنشاء حساب تخزين جديد في Azure.
   **NOTE**: تأكد من أن نوع حساب التخزين هو Standard General Purpose V2.

## الخطوة 2: إنشاء خدمة Azure AI Search

1. قم بتسجيل الدخول إلى [بوابة Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. في لوحة التنقل على الجانب الأيسر، انقر على **إنشاء مورد**.
3. في مربع البحث، اكتب "Azure AI Search" واختر **Azure AI Search** من قائمة النتائج.
4. انقر على زر **إنشاء**.
5. في علامة التبويب **الأساسيات**، قدم المعلومات التالية:
   - **الاشتراك**: اختر اشتراك Azure الخاص بك.
   - **مجموعة الموارد**: قم بإنشاء مجموعة موارد جديدة أو اختر واحدة موجودة.
   - **اسم المورد**: أدخل اسمًا فريدًا لخدمة البحث الخاصة بك.
   - **المنطقة**: اختر المنطقة الأقرب لمستخدميك.
   - **فئة التسعير**: اختر فئة التسعير التي تناسب احتياجاتك. يمكنك البدء بالفئة المجانية للاختبار.
6. انقر على **مراجعة + إنشاء**.
7. راجع الإعدادات وانقر على **إنشاء** لإنشاء خدمة البحث.

## الخطوة 3: البدء باستخدام Azure AI Search

1. بمجرد اكتمال النشر، انتقل إلى خدمة البحث الخاصة بك في بوابة Azure.
2. في لوحة نظرة عامة على خدمة البحث، انسخ عنوان URL. يجب أن يبدو مثل `https://<service-name>.search.windows.net`.
3. في الإعدادات > لوحة المفاتيح، انسخ مفتاح الاستعلام.
4. اتبع الخطوات الموجودة في صفحة [دليل البدء السريع](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) لإنشاء فهرس، تحميل البيانات، وإجراء استعلام بحث.

## الخطوة 4: استخدام أدوات Azure AI Search

يتكامل Azure AI Search مع أدوات مختلفة لتعزيز قدرات البحث لديك. يمكنك استخدام Azure CLI، Python SDK، .NET SDK وغيرها من الأدوات لإعدادات وعمليات متقدمة.

### استخدام Azure CLI

1. قم بتثبيت Azure CLI باتباع التعليمات الموجودة في [تثبيت Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. قم بتسجيل الدخول إلى Azure CLI باستخدام الأمر:

   ```bash
   az login
   ```

3. قم بتخزين كل من نقطة النهاية ومفتاح API لخدمة Azure AI Search في متغيرات البيئة.

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

### استخدام Python SDK

1. قم بتثبيت مكتبة عميل البحث المعرفي لـ Python:

   ```bash
   pip install azure-search-documents
   ```

2. استخدم الكود التالي في Python لإنشاء فهرس وتحميل المستندات:

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

### استخدام .NET SDK

1. قم بتشغيل الأمر التالي لإنشاء فهرس وتحميل المستندات:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. إليك كود .NET الخاص بـ `AzureSearch.cs`:

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

للحصول على معلومات أكثر تفصيلًا، راجع الوثائق التالية:

- [إنشاء خدمة البحث المعرفي في Azure](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [البدء باستخدام البحث المعرفي في Azure](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [أدوات Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## الخاتمة

لقد قمت بإعداد Azure AI Search بنجاح باستخدام بوابة Azure ودمج الأدوات. يمكنك الآن استكشاف المزيد من الميزات والقدرات المتقدمة لـ Azure AI Search لتعزيز حلول البحث الخاصة بك.

للحصول على مساعدة إضافية، قم بزيارة [وثائق البحث المعرفي في Azure](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.