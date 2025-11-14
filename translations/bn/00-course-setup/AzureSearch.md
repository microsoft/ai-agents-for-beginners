<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:31:04+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "bn"
}
-->
# Azure AI Search সেটআপ গাইড

এই গাইডটি আপনাকে Azure পোর্টাল ব্যবহার করে Azure AI Search সেটআপ করতে সাহায্য করবে। Azure AI Search সার্ভিস তৈরি এবং কনফিগার করার জন্য নিচের ধাপগুলো অনুসরণ করুন।

## প্রয়োজনীয়তা

শুরু করার আগে নিশ্চিত করুন যে আপনার কাছে নিম্নলিখিত জিনিসগুলো রয়েছে:

- একটি Azure সাবস্ক্রিপশন। যদি আপনার Azure সাবস্ক্রিপশন না থাকে, তাহলে [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) এ একটি ফ্রি অ্যাকাউন্ট তৈরি করতে পারেন।

## ধাপ ১: একটি Azure Storage অ্যাকাউন্ট তৈরি করুন

1. একটি নতুন Azure Storage অ্যাকাউন্ট তৈরি করতে এই নির্দেশনা অনুসরণ করুন: [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)।
   **NOTE**: নিশ্চিত করুন যে Storage অ্যাকাউন্টের ধরন Standard General Purpose V2।

## ধাপ ২: একটি Azure AI Search সার্ভিস তৈরি করুন

1. [Azure পোর্টাল](https://portal.azure.com/?wt.mc_id=studentamb_258691)-এ সাইন ইন করুন।
2. বাম পাশের নেভিগেশন প্যানেলে **Create a resource**-এ ক্লিক করুন।
3. সার্চ বক্সে "Azure AI Search" টাইপ করুন এবং ফলাফলের তালিকা থেকে **Azure AI Search** নির্বাচন করুন।
4. **Create** বোতামে ক্লিক করুন।
5. **Basics** ট্যাবে নিম্নলিখিত তথ্য প্রদান করুন:
   - **Subscription**: আপনার Azure সাবস্ক্রিপশন নির্বাচন করুন।
   - **Resource group**: একটি নতুন রিসোর্স গ্রুপ তৈরি করুন অথবা বিদ্যমান একটি নির্বাচন করুন।
   - **Resource name**: আপনার সার্চ সার্ভিসের জন্য একটি ইউনিক নাম দিন।
   - **Region**: আপনার ব্যবহারকারীদের কাছাকাছি একটি অঞ্চল নির্বাচন করুন।
   - **Pricing tier**: আপনার প্রয়োজন অনুযায়ী একটি প্রাইসিং টিয়ার নির্বাচন করুন। টেস্টিংয়ের জন্য আপনি Free টিয়ার দিয়ে শুরু করতে পারেন।
6. **Review + create**-এ ক্লিক করুন।
7. সেটিংস পর্যালোচনা করুন এবং সার্চ সার্ভিস তৈরি করতে **Create**-এ ক্লিক করুন।

## ধাপ ৩: Azure AI Search ব্যবহার শুরু করুন

1. ডিপ্লয়মেন্ট সম্পন্ন হলে, Azure পোর্টালে আপনার সার্চ সার্ভিসে যান।
2. সার্চ সার্ভিসের ওভারভিউ প্যান থেকে URL কপি করুন। এটি দেখতে এমন হবে `https://<service-name>.search.windows.net`।
3. Settings > Keys প্যান থেকে কুয়েরি কী কপি করুন।
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) পেজের ধাপগুলো অনুসরণ করে একটি ইনডেক্স তৈরি করুন, ডেটা আপলোড করুন এবং সার্চ কুয়েরি সম্পাদন করুন।

## ধাপ ৪: Azure AI Search টুলস ব্যবহার করুন

Azure AI Search বিভিন্ন টুলের সাথে ইন্টিগ্রেট করে আপনার সার্চ সক্ষমতাকে উন্নত করে। আপনি Azure CLI, Python SDK, .NET SDK এবং অন্যান্য টুল ব্যবহার করতে পারেন উন্নত কনফিগারেশন এবং অপারেশনের জন্য।

### Azure CLI ব্যবহার করা

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) নির্দেশনা অনুসরণ করে Azure CLI ইনস্টল করুন।
2. নিম্নলিখিত কমান্ড ব্যবহার করে Azure CLI-তে সাইন ইন করুন:

   ```bash
   az login
   ```

3. Azure AI Search ইনস্ট্যান্সের এন্ডপয়েন্ট এবং API কী এনভায়রনমেন্ট ভেরিয়েবল হিসেবে সংরক্ষণ করুন।

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

### Python SDK ব্যবহার করা

1. Azure Cognitive Search ক্লায়েন্ট লাইব্রেরি Python-এর জন্য ইনস্টল করুন:

   ```bash
   pip install azure-search-documents
   ```

2. নিম্নলিখিত Python কোড ব্যবহার করে একটি ইনডেক্স তৈরি করুন এবং ডকুমেন্ট আপলোড করুন:

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

### .NET SDK ব্যবহার করা

1. নিম্নলিখিত কমান্ড চালিয়ে একটি ইনডেক্স তৈরি করুন এবং ডকুমেন্ট আপলোড করুন:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. এখানে `AzureSearch.cs` এর .NET কোড রয়েছে:

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

আরও বিস্তারিত তথ্যের জন্য নিম্নলিখিত ডকুমেন্টেশন দেখুন:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## উপসংহার

আপনি সফলভাবে Azure পোর্টাল ব্যবহার করে Azure AI Search সেটআপ করেছেন এবং টুলস ইন্টিগ্রেট করেছেন। এখন আপনি Azure AI Search-এর আরও উন্নত ফিচার এবং সক্ষমতা অন্বেষণ করতে পারেন আপনার সার্চ সলিউশন উন্নত করার জন্য।

আরও সহায়তার জন্য, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) দেখুন।

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়বদ্ধ থাকব না।