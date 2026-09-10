# Azure AI Search সেটআপ গাইড

এই গাইডটি আপনাকে Azure পোর্টাল ব্যবহার করে Azure AI Search সেট আপ করতে সাহায্য করবে। আপনার Azure AI Search সার্ভিস তৈরি এবং কনফিগার করার জন্য নীচের ধাপগুলো অনুসরণ করুন।

## পূর্বশর্তসমূহ

শুরু করার আগে, নিশ্চিত হয়ে নিন আপনার কাছে নিম্নলিখিত রয়েছে:

- একটি Azure সাবস্ক্রিপশন। যদি আপনার Azure সাবস্ক্রিপশন না থাকে, তবে আপনি [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) এ একটি ফ্রি অ্যাকাউন্ট তৈরি করতে পারেন।

## ধাপ ১: একটি Azure স্টোরেজ অ্যাকাউন্ট তৈরি করুন

১. এই নির্দেশনা [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) অনুসরণ করে একটি নতুন Azure স্টোরেজ অ্যাকাউন্ট তৈরি করুন।
   **NOTE**: নিশ্চিত করুন যে স্টোরেজ অ্যাকাউন্টের ধরণ Standard General Purpose V2।

## ধাপ ২: একটি Azure AI Search সার্ভিস তৈরি করুন

১. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) এ সাইন ইন করুন।
২. বাম দিকের নেভিগেশন প্যানেলে, **Create a resource** এ ক্লিক করুন।
৩. সার্চ বক্সে "Azure AI Search" টাইপ করুন এবং ফলাফল তালিকা থেকে **Azure AI Search** নির্বাচন করুন।
৪. **Create** বোতামে ক্লিক করুন।
৫. **Basics** ট্যাবে নিম্নলিখিত তথ্য প্রদান করুন:
   - **Subscription**: আপনার Azure সাবস্ক্রিপশন নির্বাচন করুন।
   - **Resource group**: একটি নতুন রিসোর্স গ্রুপ তৈরি করুন অথবা পূর্বে থাকা একটি নির্বাচন করুন।
   - **Resource name**: আপনার সার্চ সার্ভিসের জন্য একটি ইউনিক নাম দিন।
   - **Region**: আপনার ব্যবহারকারীদের কাছে সবচেয়ে কাছাকাছি অঞ্চল নির্বাচন করুন।
   - **Pricing tier**: এমন একটি প্রাইসিং টিয়ার নির্বাচন করুন যা আপনার প্রয়োজন মেটায়। পরীক্ষার জন্য Free tier দিয়ে শুরু করতে পারেন।
৬. **Review + create** তে ক্লিক করুন।
৭. সেটিংস পর্যালোচনা করে **Create** ক্লিক করুন সার্চ সার্ভিস তৈরির জন্য।

## ধাপ ৩: Azure AI Search দিয়ে শুরু করুন

১. ডেপ্লয়মেন্ট শেষ হলে, Azure পোর্টালে আপনার সার্চ সার্ভিসে যান।
২. সার্চ সার্ভিস ওভারভিউ প্যানেলে URL কপি করুন। এটি দেখতে হবে `https://<service-name>.search.windows.net` এর মত।
৩. **(প্রস্তাবিত)** Microsoft Entra ID (RBAC) দিয়ে কী ছাড়াই প্রবেশাধিকার সক্ষম করুন নিচের ধাপ ৪-এর মতো — কোন কীয়ের প্রয়োজন নেই। এই গাইডের স্যাম্পলগুলো ইনডেক্স তৈরি/আপডেট এবং ডকুমেন্ট আপলোড করে, যার জন্য **Search Service Contributor** এবং **Search Index Data Contributor** ভূমিকা দরকার (অথবা কী-ভিত্তিক অথেন্টিকেশনের জন্য **primary admin key** — query key নয়)। শুধুমাত্র যদি আপনি RBAC ব্যবহার করতে না পারেন, তাহলে **Settings > Keys** প্যানেল থেকে **primary admin key** কপি করুন।
৪. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) পাতার ধাপগুলো অনুসরণ করে ইনডেক্স তৈরি করুন, ডাটা আপলোড করুন, এবং সার্চ পরিচালনা করুন।

## ধাপ ৪: Azure AI Search টুলস ব্যবহার করুন

Azure AI Search বিভিন্ন টুলের সাথে ইন্টিগ্রেট করে আপনার সার্চ কার্যক্ষমতা উন্নত করে। উন্নত কনফিগারেশন এবং অপারেশনের জন্য আপনি Azure CLI, Python SDK, .NET SDK এবং অন্যান্য টুল ব্যবহার করতে পারেন।

### Azure CLI ব্যবহার করে

১. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) তে নির্দেশিকা অনুসরণ করে Azure CLI ইন্সটল করুন।
২. কমান্ড দিয়ে Azure CLI তে সাইন ইন করুন:

   ```bash
   az login
   ```
৩. **(প্রস্তাবিত) Microsoft Entra ID (RBAC) দিয়ে কী ছাড়াই প্রবেশাধিকার সক্ষম করুন:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az সার্চ সার্ভিসে কোনও "endpoint" ফিল্ড নেই; সার্ভিসের নাম থেকে URL তৈরি করুন।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC সক্রিয় থাকলে, নীচের Python এবং .NET SDK স্যাম্পলগুলো `DefaultAzureCredential` দিয়ে অথেন্টিকেট করে, যা আপনার `az login` সেশনের ব্যবহার করে লোকাল ডেভেলপমেন্টে — কোন অ্যাডমিন কীয়ের প্রয়োজন হয় না। দেখুন [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)।

৪. **(ফলব্যাক) কী-ভিত্তিক অথেন্টিকেশন** — শুধুমাত্র যদি আপনি RBAC ব্যবহার করতে না পারেন, অ্যাডমিন কীও সংরক্ষণ করুন:

#### Azure AI Search ইনস্ট্যান্সের জন্য এন্ডপয়েন্ট এবং API কী উভয়কে পরিবেশ ভেরিয়েবলে সংরক্ষণ করুন।

    ```bash
    # zsh/bash
    # az search service show এ "endpoint" ফিল্ড নেই; সার্ভিস নাম থেকে URL তৈরি করুন।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show এ "endpoint" ফিল্ড নেই; সার্ভিস নাম থেকে URL তৈরি করুন।
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK ব্যবহার করে

১. Azure Cognitive Search ক্লায়েন্ট লাইব্রেরি এবং Azure Identity for Python ইন্সটল করুন:

   ```bash
   pip install azure-search-documents azure-identity
   ```

২. ইনডেক্স তৈরি এবং ডকুমেন্ট আপলোড করার জন্য নিম্নলিখিত Python কোড ব্যবহার করুন:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # কীলেস (পরামর্শকৃত): Entra ID RBAC এর মাধ্যমে আপনার `az login` পরিচয় ব্যবহার করে।
    # "Search Service Contributor" এবং "Search Index Data Contributor" ভূমিকা প্রয়োজন।
    credential = DefaultAzureCredential()
    # ফলব্যাক (কী-ভিত্তিক প্রমাণীকরণ):
    # azure.core.credentials থেকে AzureKeyCredential আমদানি করুন
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

### .NET SDK ব্যবহার করে

১. ইনডেক্স তৈরি এবং ডকুমেন্ট আপলোড করার জন্য নিচের কমান্ড চালান:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    নীচের .NET স্যাম্পলটি `DefaultAzureCredential` ব্যবহার করে, যা লোকাল ডেভেলপমেন্টে আপনার Azure CLI থেকে `az login` ব্যবহার করতে পারে।

২. এখানে `AzureSearch.cs` এর .NET কোড আছে:

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

আরও বিস্তারিত তথ্যের জন্য নিচের ডকুমেন্টেশনগুলো দেখুন:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## উপসংহার

আপনি সফলভাবে Azure পোর্টাল ব্যবহার করে Azure AI Search সেটআপ করেছেন এবং ইন্টিগ্রেটেড টুলস ব্যবহার করেছেন। এখন আপনি Azure AI Search এর আরও উন্নত বৈশিষ্ট্য এবং ক্ষমতা অনুসন্ধান করে আপনার সার্চ সমাধান উন্নত করতে পারেন।

আরও সাহায্যের জন্য, যান [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->