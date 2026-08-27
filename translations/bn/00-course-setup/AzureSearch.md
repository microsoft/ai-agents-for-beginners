# Azure AI Search সেটআপ গাইড

এই গাইডটি আপনাকে Azure পোর্টাল ব্যবহার করে Azure AI Search সেটআপ করতে সাহায্য করবে। আপনার Azure AI Search সার্ভিস তৈরি ও কনফিগার করার জন্য নীচের ধাপগুলি অনুসরণ করুন।

## প্রয়োজনীয় তথ্য

শুরু করার আগে, নিশ্চিত করুন আপনার কাছে নিম্নলিখিতগুলো আছে:

- একটি Azure সাবস্ক্রিপশন। যদি আপনার Azure সাবস্ক্রিপশন না থাকে, তাহলে আপনি [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) এ গিয়ে একটি ফ্রি অ্যাকাউন্ট তৈরি করতে পারেন।

## ধাপ 1: Azure Storage Account তৈরি করুন

1. এই নির্দেশনা অনুসরণ করুন, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), একটি নতুন Azure Storage Account তৈরির জন্য।
   **NOTE**: নিশ্চিত করুন Storage Account এর টাইপ Standard General Purpose V2।

## ধাপ 2: Azure AI Search সার্ভিস তৈরি করুন

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) এ সাইন ইন করুন।
2. বাম দিকের নেভিগেশন প্যানে, **Create a resource** এ ক্লিক করুন।
3. সার্চ বক্সে "Azure AI Search" টাইপ করুন এবং ফলাফল তালিকা থেকে **Azure AI Search** নির্বাচন করুন।
4. **Create** বাটনে ক্লিক করুন।
5. **Basics** ট্যাবে নিম্নলিখিত তথ্য প্রদান করুন:
   - **Subscription**: আপনার Azure সাবস্ক্রিপশন নির্বাচন করুন।
   - **Resource group**: একটি নতুন রিসোর্স গ্রুপ তৈরি করুন অথবা বিদ্যমান একটি নির্বাচন করুন।
   - **Resource name**: আপনার সার্চ সার্ভিসের জন্য একটি অনন্য নাম প্রদান করুন।
   - **Region**: ব্যবহারকারীর কাছে সবচেয়ে কাছাকাছি অঞ্চল নির্বাচন করুন।
   - **Pricing tier**: আপনার প্রয়োজন অনুসারে একটি প্রাইসিং টিয়ার নির্বাচন করুন। টেস্ট করার জন্য আপনি ফ্রি টিয়ার দিয়ে শুরু করতে পারেন।
6. **Review + create** এ ক্লিক করুন।
7. সেটিংস রিভিউ করুন এবং সার্চ সার্ভিস তৈরি করতে **Create** এ ক্লিক করুন।

## ধাপ 3: Azure AI Search দিয়ে শুরু করুন

1. ডিপ্লয়মেন্ট শেষ হলে, Azure পোর্টালে আপনার সার্চ সার্ভিসে যান।
2. সার্চ সার্ভিস ওভারভিউ প্যানে URL নকল করুন। এটি হবে `https://<service-name>.search.windows.net` এর মতো।
3. **(প্রস্তাবিত)** Microsoft Entra ID (RBAC) দিয়ে কী ছাড়া অ্যাক্সেস সক্ষম করুন, নিচের ধাপ 4 এ দেখানো হয়েছে — কী লাগবে না। এই গাইডের স্যাম্পলগুলো ইনডেক্স তৈরি/আপডেট এবং ডকুমেন্ট আপলোড করে, যার জন্য প্রয়োজন **Search Service Contributor** এবং **Search Index Data Contributor** রোল (অথবা, কী ভিত্তিক অথেনটিকেশনের জন্য, **primary admin key** — কুয়েরি কী নয়)। শুধুমাত্র যদি আপনি RBAC ব্যবহার করতে না পারেন, তখন **Settings > Keys** প্যানে যান এবং **primary admin key** নকল করুন।
4. একটি ইনডেক্স তৈরি, ডেটা আপলোড, এবং সার্চ করার জন্য [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) পৃষ্ঠার ধাপগুলি অনুসরণ করুন।

## ধাপ 4: Azure AI Search টুলস ব্যবহার করুন

Azure AI Search বিভিন্ন টুলের সাথে সংযুক্ত হয় যা আপনার সার্চ ক্ষমতাগুলো উন্নত করে। উন্নত কনফিগারেশন ও অপারেশনগুলোর জন্য আপনি Azure CLI, Python SDK, .NET SDK এবং অন্যান্য টুল ব্যবহার করতে পারেন।

### Azure CLI ব্যবহার

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) নির্দেশনা অনুসরণ করে Azure CLI ইনস্টল করুন।
2. নিম্নলিখিত কমান্ড দিয়ে Azure CLI তে সাইন ইন করুন:

   ```bash
   az login
   ```
3. **(প্রস্তাবিত) Microsoft Entra ID (RBAC) দিয়ে কী ছাড়া অ্যাক্সেস সক্ষম করুন:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search সার্ভিস শো-তে "endpoint" ফিল্ড নেই; সার্ভিস নাম থেকে URL তৈরি করুন।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC সক্রিয় থাকলে, নিচের Python এবং .NET SDK উদাহরণগুলো `DefaultAzureCredential` দিয়ে অথেনটিকেট করে, যা আপনার `az login` সেশন ব্যবহার করে লোকাল ডেভেলপমেন্টে — কোনো অ্যাডমিন কী লাগবে না। দেখুন [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)।

4. **(ব্যাকআপ) কী ভিত্তিক অথেনটিকেশন** — শুধুমাত্র যদি আপনি RBAC ব্যবহার করতে না পারেন, অ্যাডমিন কী সংরক্ষণ করুন:

#### Azure AI Search ইন্সট্যান্সের জন্য এন্ডপয়েন্ট ও API কী একসাথে পরিবেশ ভেরিয়েবলে সংরক্ষণ করুন।

    ```bash
    # zsh/bash
    # az search service show-এ "endpoint" ফিল্ড নেই; সার্ভিস নাম থেকে URL তৈরি করুন।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show-এ "endpoint" ফিল্ড নেই; সার্ভিস নাম থেকে URL তৈরি করুন।
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK ব্যবহার

1. Azure Cognitive Search ক্লায়েন্ট লাইব্রেরি এবং Azure Identity ইনস্টল করুন Python এর জন্য:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. একটি ইনডেক্স তৈরি ও ডকুমেন্ট আপলোড করার জন্য নিচের Python কোড ব্যবহার করুন:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # কীলেস (প্রস্তাবিত): Entra ID RBAC-এর মাধ্যমে আপনার `az login` পরিচয় ব্যবহার করে।
    # "Search Service Contributor" এবং "Search Index Data Contributor" ভূমিকা প্রয়োজন।
    credential = DefaultAzureCredential()
    # ব্যাকআপ (কী-ভিত্তিক প্রমাণীকরণ):
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

### .NET SDK ব্যবহার

1. ইনডেক্স তৈরি ও ডকুমেন্ট আপলোড করার জন্য নিচের কমান্ড চালান:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    নিচের .NET স্যাম্পল `DefaultAzureCredential` ব্যবহার করে, যা লোকাল ডেভেলপমেন্টে আপনার Azure CLI `az login` সাইন-ইন ব্যবহার করতে পারে।

2. এখানে `AzureSearch.cs` এর .NET কোড:

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

আরও বিস্তারিত তথ্যের জন্য নীচের ডকুমেন্টেশন দেখুন:

- [Azure Cognitive Search সার্ভিস তৈরি করুন](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search শুরু করুন](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search টুলস](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## উপসংহার

আপনি সফলভাবে Azure পোর্টাল ব্যবহার করে Azure AI Search সেটআপ এবং টুলস ইন্টিগ্রেট করেছেন। এখন আপনি Azure AI Search এর আরও উন্নত বৈশিষ্ট্য ও ক্ষমতাগুলো অন্বেষণ করে আপনার সার্চ সলিউশন উন্নত করতে পারবেন।

আরও সাহায্যের জন্য, [Azure Cognitive Search ডকুমেন্টেশন](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) দেখুন।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->