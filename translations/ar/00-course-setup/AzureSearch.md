# دليل إعداد Azure AI Search

سيساعدك هذا الدليل في إعداد Azure AI Search باستخدام بوابة Azure. اتبع الخطوات أدناه لإنشاء وتكوين خدمة Azure AI Search الخاصة بك.

## المتطلبات الأساسية

قبل البدء، تأكد من أن لديك ما يلي:

- اشتراك في Azure. إذا لم يكن لديك اشتراك في Azure، يمكنك إنشاء حساب مجاني على [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## الخطوة 1: إنشاء حساب تخزين Azure

1. اتبع هذه التعليمات، [إنشاء حساب تخزين Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)، لإنشاء حساب تخزين Azure جديد.
   **ملاحظة**: تأكد من أن نوع حساب التخزين هو Standard General Purpose V2.

## الخطوة 2: إنشاء خدمة Azure AI Search

1. سجّل الدخول إلى [بوابة Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. في لوحة التنقل على اليسار، انقر على **إنشاء مورد**.
3. في مربع البحث، اكتب "Azure AI Search" واختر **Azure AI Search** من قائمة النتائج.
4. انقر على زر **إنشاء**.
5. في علامة تبويب **الأساسيات**، قدم المعلومات التالية:
   - **الاشتراك**: اختر اشتراك Azure الخاص بك.
   - **مجموعة الموارد**: أنشئ مجموعة موارد جديدة أو اختر مجموعة موجودة.
   - **اسم المورد**: أدخل اسمًا فريدًا لخدمة البحث الخاصة بك.
   - **المنطقة**: اختر المنطقة الأقرب إلى مستخدميك.
   - **طبقة التسعير**: اختر طبقة التسعير التي تناسب احتياجاتك. يمكنك البدء بطبقة مجانية للاختبار.
6. انقر على **مراجعة + إنشاء**.
7. استعرض الإعدادات وانقر على **إنشاء** لإنشاء خدمة البحث.

## الخطوة 3: البدء مع Azure AI Search

1. بمجرد اكتمال النشر، انتقل إلى خدمة البحث الخاصة بك في بوابة Azure.
2. في لوحة نظرة عامة على خدمة البحث، انسخ عنوان URL. يجب أن يكون شكله `https://<service-name>.search.windows.net`.
3. **(موصى به)** فعّل الوصول بدون مفتاح باستخدام Microsoft Entra ID (RBAC) كما هو موضح في الخطوة 4 أدناه — لا حاجة إلى مفتاح. تقوم العينات في هذا الدليل بإنشاء/تحديث الفهارس وتحميل المستندات، والتي تتطلب أدوار **Search Service Contributor** و **Search Index Data Contributor** (أو، للمصادقة باستخدام المفتاح، **مفتاح المسؤول الأساسي** — وليس مفتاح الاستعلام). فقط إذا لم تتمكن من استخدام RBAC، افتح لوحة **الإعدادات > المفاتيح** وانسخ **مفتاح المسؤول الأساسي**.
4. اتبع الخطوات في صفحة [الدليل السريع](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) لإنشاء فهرس، تحميل بيانات، وإجراء بحث.

## الخطوة 4: استخدام أدوات Azure AI Search

يدمج Azure AI Search مع أدوات مختلفة لتعزيز قدرات البحث الخاصة بك. يمكنك استخدام Azure CLI، حزمة تطوير بايثون SDK، حزمة تطوير .NET SDK، وأدوات أخرى للتكوينات والعمليات المتقدمة.

### استخدام Azure CLI

1. قم بتثبيت Azure CLI باتباع التعليمات على [تثبيت Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. سجّل الدخول إلى Azure CLI باستخدام الأمر:

   ```bash
   az login
   ```
3. **(موصى به) فعّل الوصول بدون مفتاح باستخدام Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    مع تمكين RBAC، تقوم عينات بايثون و .NET SDK أدناه بالمصادقة باستخدام `DefaultAzureCredential`، الذي يستخدم جلسة `az login` الخاصة بك أثناء التطوير المحلي — لا حاجة إلى مفتاح المسؤول. راجع [الاتصال بـ Azure AI Search باستخدام الأدوار](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(خطة بديلة) المصادقة باستخدام المفتاح** — فقط إذا لم تتمكن من استخدام RBAC، خزّن مفتاح المسؤول أيضًا:

#### خزّن كلًا من نقطة النهاية ومفتاح API لحالة Azure AI Search في متغيرات البيئة.

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

### استخدام حزمة تطوير بايثون SDK

1. قم بتثبيت مكتبة عميل Azure Cognitive Search و Azure Identity لبايثون:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. استخدم الشيفرة التالية بلغة بايثون لإنشاء فهرس وتحميل المستندات:

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

### استخدام حزمة تطوير .NET SDK

1. نفذ الأمر التالي لإنشاء فهرس وتحميل المستندات:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    النموذج الخاص بـ .NET أدناه يستخدم `DefaultAzureCredential`، الذي يمكنه استخدام تسجيل الدخول الخاص بك في Azure CLI من `az login` أثناء التطوير المحلي.

2. إليك شيفرة .NET الخاصة بـ `AzureSearch.cs`:

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

لمزيد من المعلومات التفصيلية، ارجع إلى الوثائق التالية:

- [إنشاء خدمة Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [البدء مع Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [أدوات Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## الخلاصة

لقد قمت بإعداد Azure AI Search بنجاح باستخدام بوابة Azure والأدوات المتكاملة. يمكنك الآن استكشاف المزيد من الميزات والقدرات المتقدمة لـ Azure AI Search لتعزيز حلول البحث الخاصة بك.

للمزيد من المساعدة، زر [توثيقات Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->