# دليل إعداد Azure AI Search

سيساعدك هذا الدليل في إعداد Azure AI Search باستخدام بوابة Azure. اتبع الخطوات أدناه لإنشاء وتكوين خدمة Azure AI Search الخاصة بك.

## المتطلبات المسبقة

قبل البدء، تأكد من أن لديك ما يلي:

- اشتراك في Azure. إذا لم يكن لديك اشتراك في Azure، يمكنك إنشاء حساب مجاني على [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## الخطوة 1: إنشاء حساب تخزين Azure

1. اتبع هذا الدليل، [إنشاء حساب تخزين Azure](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)، لإنشاء حساب تخزين Azure جديد.
   **ملاحظة**: تأكد من أن نوع حساب التخزين هو Standard General Purpose V2.

## الخطوة 2: إنشاء خدمة Azure AI Search

1. سجّل الدخول إلى [بوابة Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. في الجزء الجانبي الأيسر للتنقل، انقر على **إنشاء مورد**.
3. في مربع البحث، اكتب "Azure AI Search" واختر **Azure AI Search** من قائمة النتائج.
4. انقر على زر **إنشاء**.
5. في علامة التبويب **الأساسيات**، قدّم المعلومات التالية:
   - **الاشتراك**: اختر اشتراك Azure الخاص بك.
   - **مجموعة الموارد**: أنشئ مجموعة موارد جديدة أو اختر مجموعة موجودة.
   - **اسم المورد**: أدخل اسمًا فريدًا لخدمة البحث الخاصة بك.
   - **المنطقة**: اختر المنطقة الأقرب إلى المستخدمين لديك.
   - **طبقة التسعير**: اختر طبقة التسعير التي تناسب متطلباتك. يمكنك البدء بالطبقة المجانية للاختبار.
6. انقر على **مراجعة + إنشاء**.
7. راجع الإعدادات وانقر على **إنشاء** لإنشاء خدمة البحث.

## الخطوة 3: بدء الاستخدام مع Azure AI Search

1. بمجرد اكتمال النشر، انتقل إلى خدمة البحث الخاصة بك في بوابة Azure.
2. في جزء نظرة عامة على خدمة البحث، انسخ عنوان URL. يجب أن يكون بالشكل `https://<service-name>.search.windows.net`.
3. **(مستحسن)** فعّل الوصول بدون مفتاح باستخدام Microsoft Entra ID (RBAC) كما هو موضح في الخطوة 4 أدناه — لا حاجة لمفتاح. العينات في هذا الدليل تقوم بإنشاء/تحديث الفهارس ورفع المستندات، والتي تتطلب صلاحيات **مساهم خدمة البحث** و**مساهم بيانات فهرس البحث** (أو، للمصادقة المعتمدة على المفتاح، **المفتاح الإداري الأساسي** — وليس مفتاح الاستعلام). فقط إذا لم تتمكن من استخدام RBAC، افتح قائمة **الإعدادات > المفاتيح** وانسخ **المفتاح الإداري الأساسي**.
4. اتبع الخطوات في صفحة [الدليل السريع](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) لإنشاء فهرس، رفع بيانات، وإجراء بحث.

## الخطوة 4: استخدام أدوات Azure AI Search

يتكامل Azure AI Search مع أدوات متعددة لتعزيز قدرات البحث لديك. يمكنك استخدام Azure CLI، وPython SDK، و.NET SDK، وأدوات أخرى للتكوينات والعمليات المتقدمة.

### استخدام Azure CLI

1. قم بتثبيت Azure CLI باتباع الإرشادات في [تثبيت Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. قم بتسجيل الدخول إلى Azure CLI باستخدام الأمر:

   ```bash
   az login
   ```
3. **(مستحسن) فعّل الوصول بدون مفتاح باستخدام Microsoft Entra ID (RBAC):**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # تظهر خدمة az search أنه لا يحتوي على حقل "endpoint"؛ قم ببناء عنوان URL من اسم الخدمة.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    مع تفعيل RBAC، تتحقق العينات في Python و.NET SDK أدناه من خلال `DefaultAzureCredential`، الذي يستخدم جلسة `az login` الخاصة بك أثناء التطوير المحلي — لا حاجة لمفتاح إداري. راجع [الاتصال بـ Azure AI Search باستخدام الأدوار](https://learn.microsoft.com/azure/search/search-security-rbac).

4. **(خيار بديل) المصادقة المعتمدة على المفتاح** — فقط إذا لم تتمكن من استخدام RBAC، خزّن المفتاح الإداري أيضًا:

#### تخزين كل من نقطة النهاية والمفتاح API لحالة Azure AI Search في متغيرات البيئة.

    ```bash
    # zsh/bash
    # لا يحتوي az search service show على حقل "endpoint"؛ قم ببناء URL من اسم الخدمة.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # لا يحتوي az search service show على حقل "endpoint"؛ قم ببناء URL من اسم الخدمة.
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### استخدام Python SDK

1. قم بتثبيت مكتبة عميل Azure Cognitive Search وAzure Identity لـ Python:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. استخدم الكود التالي بـ Python لإنشاء فهرس ورفع المستندات:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # بدون مفتاح (مُوصى به): يستخدم هويتك من `az login` عبر التحكم في الوصول القائم على الدور في Entra ID.
    # يتطلب أدوار "مساهم خدمة البحث" و"مساهم بيانات فهرس البحث".
    credential = DefaultAzureCredential()
    # الاحتياطي (المصادقة بالمفتاح):
    # من azure.core.credentials استيراد AzureKeyCredential
    # الاعتماد = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
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

1. نفذ الأمر التالي لإنشاء فهرس ورفع المستندات:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    المثال في .NET أدناه يستخدم `DefaultAzureCredential`، الذي يمكنه استخدام تسجيل الدخول الخاص بك إلى Azure CLI عبر `az login` أثناء التطوير المحلي.

2. هذا هو كود .NET لملف `AzureSearch.cs`:

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

لمزيد من المعلومات التفصيلية، راجع الوثائق التالية:

- [إنشاء خدمة Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [البدء مع Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [أدوات Azure AI Search](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## الخاتمة

لقد قمت بإعداد Azure AI Search بنجاح باستخدام بوابة Azure والأدوات المتكاملة. يمكنك الآن استكشاف ميزات وقدرات أكثر تقدمًا في Azure AI Search لتعزيز حلول البحث الخاصة بك.

للحصول على مزيد من المساعدة، قم بزيارة [وثائق Azure Cognitive Search](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->