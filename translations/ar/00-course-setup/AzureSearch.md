<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:33:27+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ar"
}
-->
# دليل إعداد Azure AI Search

سيساعدك هذا الدليل في إعداد Azure AI Search باستخدام بوابة Azure. اتبع الخطوات أدناه لإنشاء وتكوين خدمة Azure AI Search الخاصة بك.

## المتطلبات الأساسية

قبل أن تبدأ، تأكد من توفر ما يلي:

- اشتراك في Azure. إذا لم يكن لديك اشتراك في Azure، يمكنك إنشاء حساب مجاني على [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691).

## الخطوة 1: إنشاء خدمة Azure AI Search

1. سجّل الدخول إلى [بوابة Azure](https://portal.azure.com/?wt.mc_id=studentamb_258691).
2. في لوحة التنقل على الجانب الأيسر، انقر على **إنشاء مورد**.
3. في مربع البحث، اكتب "Azure AI Search" واختر **Azure AI Search** من قائمة النتائج.
4. انقر على زر **إنشاء**.
5. في علامة التبويب **الأساسيات**، قدّم المعلومات التالية:
   - **الاشتراك**: اختر اشتراك Azure الخاص بك.
   - **مجموعة الموارد**: أنشئ مجموعة موارد جديدة أو اختر واحدة موجودة.
   - **اسم المورد**: أدخل اسمًا فريدًا لخدمة البحث الخاصة بك.
   - **المنطقة**: اختر المنطقة الأقرب إلى مستخدميك.
   - **فئة التسعير**: اختر فئة التسعير التي تناسب متطلباتك. يمكنك البدء بالفئة المجانية للاختبار.
6. انقر على **مراجعة + إنشاء**.
7. راجع الإعدادات ثم انقر على **إنشاء** لإنشاء خدمة البحث.

## الخطوة 2: البدء باستخدام Azure AI Search

1. بمجرد اكتمال النشر، انتقل إلى خدمة البحث الخاصة بك في بوابة Azure.
2. في صفحة نظرة عامة على خدمة البحث، انقر على زر **البدء السريع**.
3. اتبع الخطوات في دليل البدء السريع لإنشاء فهرس، وتحميل البيانات، وإجراء استعلام بحث.

### إنشاء فهرس

1. في دليل البدء السريع، انقر على **إنشاء فهرس**.
2. عرّف مخطط الفهرس بتحديد الحقول وخصائصها (مثل نوع البيانات، قابلية البحث، قابلية التصفية).
3. انقر على **إنشاء** لإنشاء الفهرس.

### تحميل البيانات

1. في دليل البدء السريع، انقر على **تحميل البيانات**.
2. اختر مصدر البيانات (مثل Azure Blob Storage، Azure SQL Database) وقدم تفاصيل الاتصال اللازمة.
3. اربط حقول مصدر البيانات بحقول الفهرس.
4. انقر على **إرسال** لتحميل البيانات إلى الفهرس.

### إجراء استعلام بحث

1. في دليل البدء السريع، انقر على **مستكشف البحث**.
2. أدخل استعلام بحث في مربع البحث لاختبار وظيفة البحث.
3. راجع نتائج البحث وقم بتعديل مخطط الفهرس أو البيانات حسب الحاجة.

## الخطوة 3: استخدام أدوات Azure AI Search

يتكامل Azure AI Search مع أدوات مختلفة لتعزيز قدرات البحث لديك. يمكنك استخدام Azure CLI، وPython SDK، وأدوات أخرى لإعدادات وعمليات متقدمة.

### استخدام Azure CLI

1. قم بتثبيت Azure CLI باتباع التعليمات في [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691).
2. سجّل الدخول إلى Azure CLI باستخدام الأمر:
   ```bash
   az login
   ```
3. أنشئ خدمة بحث جديدة باستخدام Azure CLI:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. أنشئ فهرسًا باستخدام Azure CLI:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### استخدام Python SDK

1. قم بتثبيت مكتبة عميل Azure Cognitive Search لـ Python:
   ```bash
   pip install azure-search-documents
   ```
2. استخدم الكود التالي في Python لإنشاء فهرس وتحميل المستندات:
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

لمزيد من المعلومات التفصيلية، راجع الوثائق التالية:

- [إنشاء خدمة Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [البدء باستخدام Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [أدوات Azure AI Search](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## الخاتمة

لقد قمت بإعداد Azure AI Search بنجاح باستخدام بوابة Azure والأدوات المتكاملة. يمكنك الآن استكشاف المزيد من الميزات والقدرات المتقدمة لـ Azure AI Search لتعزيز حلول البحث الخاصة بك.

للمساعدة الإضافية، قم بزيارة [توثيق Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691).

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.