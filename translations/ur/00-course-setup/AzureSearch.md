<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:33:52+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ur"
}
-->
# Azure AI Search سیٹ اپ گائیڈ

یہ گائیڈ آپ کو Azure پورٹل کے ذریعے Azure AI Search سیٹ اپ کرنے میں مدد دے گی۔ نیچے دیے گئے مراحل پر عمل کریں تاکہ آپ اپنی Azure AI Search سروس بنا سکیں اور ترتیب دے سکیں۔

## ضروریات

شروع کرنے سے پہلے، یقینی بنائیں کہ آپ کے پاس درج ذیل چیزیں موجود ہیں:

- ایک Azure سبسکرپشن۔ اگر آپ کے پاس Azure سبسکرپشن نہیں ہے، تو آپ مفت اکاؤنٹ [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) پر بنا سکتے ہیں۔

## مرحلہ 1: Azure AI Search سروس بنائیں

1. [Azure پورٹل](https://portal.azure.com/?wt.mc_id=studentamb_258691) میں سائن ان کریں۔
2. بائیں جانب نیویگیشن پین میں، **Create a resource** پر کلک کریں۔
3. سرچ باکس میں "Azure AI Search" ٹائپ کریں اور نتائج کی فہرست سے **Azure AI Search** منتخب کریں۔
4. **Create** بٹن پر کلک کریں۔
5. **Basics** ٹیب میں درج ذیل معلومات فراہم کریں:
   - **Subscription**: اپنی Azure سبسکرپشن منتخب کریں۔
   - **Resource group**: نیا resource group بنائیں یا موجودہ میں سے کوئی منتخب کریں۔
   - **Resource name**: اپنی سرچ سروس کے لیے ایک منفرد نام درج کریں۔
   - **Region**: اپنے صارفین کے قریب ترین ریجن منتخب کریں۔
   - **Pricing tier**: اپنی ضروریات کے مطابق ایک پرائسنگ ٹئیر منتخب کریں۔ آپ ٹیسٹنگ کے لیے Free tier سے شروع کر سکتے ہیں۔
6. **Review + create** پر کلک کریں۔
7. سیٹنگز کا جائزہ لیں اور **Create** پر کلک کر کے سرچ سروس بنائیں۔

## مرحلہ 2: Azure AI Search کے ساتھ آغاز کریں

1. جب ڈپلائمنٹ مکمل ہو جائے، تو Azure پورٹل میں اپنی سرچ سروس پر جائیں۔
2. سرچ سروس کے اوورویو پیج میں، **Quickstart** بٹن پر کلک کریں۔
3. Quickstart گائیڈ میں دیے گئے مراحل پر عمل کریں تاکہ انڈیکس بنائیں، ڈیٹا اپلوڈ کریں، اور سرچ کوئری انجام دیں۔

### انڈیکس بنائیں

1. Quickstart گائیڈ میں، **Create an index** پر کلک کریں۔
2. انڈیکس اسکیمہ کی وضاحت کریں، یعنی فیلڈز اور ان کی خصوصیات (جیسے ڈیٹا ٹائپ، سرچ ایبل، فلٹر ایبل) متعین کریں۔
3. انڈیکس بنانے کے لیے **Create** پر کلک کریں۔

### ڈیٹا اپلوڈ کریں

1. Quickstart گائیڈ میں، **Upload data** پر کلک کریں۔
2. ایک ڈیٹا سورس منتخب کریں (مثلاً Azure Blob Storage، Azure SQL Database) اور ضروری کنکشن کی تفصیلات فراہم کریں۔
3. ڈیٹا سورس کے فیلڈز کو انڈیکس کے فیلڈز سے میپ کریں۔
4. ڈیٹا اپلوڈ کرنے کے لیے **Submit** پر کلک کریں۔

### سرچ کوئری انجام دیں

1. Quickstart گائیڈ میں، **Search explorer** پر کلک کریں۔
2. سرچ باکس میں ایک سرچ کوئری درج کریں تاکہ سرچ فنکشنالٹی کو ٹیسٹ کیا جا سکے۔
3. سرچ نتائج کا جائزہ لیں اور ضرورت کے مطابق انڈیکس اسکیمہ یا ڈیٹا میں تبدیلی کریں۔

## مرحلہ 3: Azure AI Search ٹولز استعمال کریں

Azure AI Search مختلف ٹولز کے ساتھ انٹیگریٹ ہوتا ہے تاکہ آپ کی سرچ صلاحیتوں کو بہتر بنایا جا سکے۔ آپ Azure CLI، Python SDK، اور دیگر ٹولز کا استعمال کر کے ایڈوانس کنفیگریشنز اور آپریشنز کر سکتے ہیں۔

### Azure CLI کا استعمال

1. Azure CLI انسٹال کریں، ہدایات کے لیے [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) دیکھیں۔
2. Azure CLI میں سائن ان کریں، کمانڈ استعمال کریں:
   ```bash
   az login
   ```
3. Azure CLI کے ذریعے نئی سرچ سروس بنائیں:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI کے ذریعے انڈیکس بنائیں:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK کا استعمال

1. Python کے لیے Azure Cognitive Search کلائنٹ لائبریری انسٹال کریں:
   ```bash
   pip install azure-search-documents
   ```
2. انڈیکس بنانے اور دستاویزات اپلوڈ کرنے کے لیے درج ذیل Python کوڈ استعمال کریں:
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

مزید تفصیلی معلومات کے لیے درج ذیل دستاویزات ملاحظہ کریں:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## نتیجہ

آپ نے کامیابی کے ساتھ Azure پورٹل اور انٹیگریٹڈ ٹولز کے ذریعے Azure AI Search سیٹ اپ کر لیا ہے۔ اب آپ Azure AI Search کی مزید ایڈوانس خصوصیات اور صلاحیتوں کو دریافت کر کے اپنی سرچ سولیوشنز کو بہتر بنا سکتے ہیں۔

مزید مدد کے لیے، [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) ملاحظہ کریں۔

**دستخطی نوٹ**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔