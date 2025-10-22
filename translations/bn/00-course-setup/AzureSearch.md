<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:35:16+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "bn"
}
-->
# Azure AI Search সেটআপ গাইড

এই গাইডটি আপনাকে Azure পোর্টাল ব্যবহার করে Azure AI Search সেটআপ করতে সাহায্য করবে। নিচের ধাপগুলো অনুসরণ করে আপনার Azure AI Search সার্ভিস তৈরি ও কনফিগার করুন।

## প্রয়োজনীয়তা

শুরু করার আগে, নিশ্চিত করুন আপনার কাছে নিম্নলিখিতগুলো আছে:

- একটি Azure সাবস্ক্রিপশন। যদি আপনার Azure সাবস্ক্রিপশন না থাকে, তাহলে আপনি [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) থেকে একটি ফ্রি অ্যাকাউন্ট তৈরি করতে পারেন।

## ধাপ ১: একটি Azure AI Search সার্ভিস তৈরি করুন

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) এ সাইন ইন করুন।
2. বাম দিকের নেভিগেশন প্যানেলে **Create a resource** ক্লিক করুন।
3. সার্চ বক্সে "Azure AI Search" টাইপ করুন এবং ফলাফল থেকে **Azure AI Search** নির্বাচন করুন।
4. **Create** বাটনে ক্লিক করুন।
5. **Basics** ট্যাবে নিচের তথ্য দিন:
   - **Subscription**: আপনার Azure সাবস্ক্রিপশন নির্বাচন করুন।
   - **Resource group**: একটি নতুন রিসোর্স গ্রুপ তৈরি করুন অথবা বিদ্যমান একটি নির্বাচন করুন।
   - **Resource name**: আপনার সার্চ সার্ভিসের জন্য একটি ইউনিক নাম দিন।
   - **Region**: আপনার ব্যবহারকারীদের সবচেয়ে কাছের অঞ্চল নির্বাচন করুন।
   - **Pricing tier**: আপনার প্রয়োজন অনুযায়ী একটি প্রাইসিং টিয়ার নির্বাচন করুন। টেস্টিং এর জন্য Free tier দিয়ে শুরু করতে পারেন।
6. **Review + create** ক্লিক করুন।
7. সেটিংসগুলো পর্যালোচনা করে **Create** ক্লিক করে সার্চ সার্ভিস তৈরি করুন।

## ধাপ ২: Azure AI Search শুরু করুন

1. ডিপ্লয়মেন্ট সম্পন্ন হলে, Azure পোর্টালে আপনার সার্চ সার্ভিসে যান।
2. সার্চ সার্ভিস ওভারভিউ পেজে **Quickstart** বাটনে ক্লিক করুন।
3. Quickstart গাইডের ধাপগুলো অনুসরণ করে একটি ইনডেক্স তৈরি করুন, ডেটা আপলোড করুন এবং সার্চ কোয়েরি চালান।

### একটি ইনডেক্স তৈরি করুন

1. Quickstart গাইডে **Create an index** ক্লিক করুন।
2. ইনডেক্স স্কিমা নির্ধারণ করুন, যেখানে ফিল্ড এবং তাদের বৈশিষ্ট্য (যেমন, ডেটা টাইপ, সার্চেবল, ফিল্টারেবল) উল্লেখ থাকবে।
3. ইনডেক্স তৈরি করতে **Create** ক্লিক করুন।

### ডেটা আপলোড করুন

1. Quickstart গাইডে **Upload data** ক্লিক করুন।
2. একটি ডেটা সোর্স নির্বাচন করুন (যেমন, Azure Blob Storage, Azure SQL Database) এবং প্রয়োজনীয় কানেকশন ডিটেইলস দিন।
3. ডেটা সোর্সের ফিল্ডগুলো ইনডেক্সের ফিল্ডের সাথে ম্যাপ করুন।
4. ডেটা ইনডেক্সে আপলোড করতে **Submit** ক্লিক করুন।

### সার্চ কোয়েরি চালান

1. Quickstart গাইডে **Search explorer** ক্লিক করুন।
2. সার্চ বক্সে একটি সার্চ কোয়েরি লিখে সার্চ ফাংশনালিটি পরীক্ষা করুন।
3. সার্চ ফলাফল পর্যালোচনা করুন এবং প্রয়োজনে ইনডেক্স স্কিমা বা ডেটা সামঞ্জস্য করুন।

## ধাপ ৩: Azure AI Search টুলস ব্যবহার করুন

Azure AI Search বিভিন্ন টুলের সাথে ইন্টিগ্রেট করে আপনার সার্চ ক্ষমতা বাড়ায়। উন্নত কনফিগারেশন এবং অপারেশনের জন্য আপনি Azure CLI, Python SDK এবং অন্যান্য টুল ব্যবহার করতে পারেন।

### Azure CLI ব্যবহার

1. [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) এ দেওয়া নির্দেশনা অনুসরণ করে Azure CLI ইনস্টল করুন।
2. Azure CLI তে সাইন ইন করতে নিচের কমান্ড ব্যবহার করুন:
   ```bash
   az login
   ```
3. Azure CLI ব্যবহার করে একটি নতুন সার্চ সার্ভিস তৈরি করুন:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI দিয়ে একটি ইনডেক্স তৈরি করুন:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK ব্যবহার

1. Python এর জন্য Azure Cognitive Search ক্লায়েন্ট লাইব্রেরি ইনস্টল করুন:
   ```bash
   pip install azure-search-documents
   ```
2. নিচের Python কোড ব্যবহার করে একটি ইনডেক্স তৈরি করুন এবং ডকুমেন্ট আপলোড করুন:
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

বিস্তারিত তথ্যের জন্য নিচের ডকুমেন্টেশনগুলো দেখুন:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## উপসংহার

আপনি সফলভাবে Azure পোর্টাল এবং ইন্টিগ্রেটেড টুলস ব্যবহার করে Azure AI Search সেটআপ করেছেন। এখন আপনি Azure AI Search এর আরও উন্নত ফিচার এবং ক্ষমতা অন্বেষণ করে আপনার সার্চ সলিউশন উন্নত করতে পারেন।

অতিরিক্ত সহায়তার জন্য [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) দেখুন।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।