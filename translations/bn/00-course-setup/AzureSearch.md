# অ্যাজুর AI সার্চ সেটআপ গাইড

এই গাইডটি আপনাকে অ্যাজুর পোর্টালের সাহায্যে অ্যাজুর AI সার্চ সেটআপ করতে সাহায্য করবে। আপনার অ্যাজুর AI সার্চ সার্ভিস তৈরি এবং কনফিগার করতে নিচের ধাপগুলি অনুসরণ করুন।

## প্রয়োজনীয়তা

শুরু করার আগে, নিশ্চিত করুন আপনার কাছে নিচেরগুলো আছে:

- একটি অ্যাজুর সাবস্ক্রিপশন। যদি আপনার অ্যাজুর সাবস্ক্রিপশন না থাকে, আপনি [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) এ একটি বিনামূল্যের অ্যাকাউন্ট তৈরি করতে পারেন।

## ধাপ ১: একটি অ্যাজুর স্টোরেজ অ্যাকাউন্ট তৈরি করুন

১. এই নির্দেশিকা অনুসরণ করুন, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), একটি নতুন অ্যাজুর স্টোরেজ অ্যাকাউন্ট তৈরি করার জন্য।
   **NOTICE**: নিশ্চিত করুন স্টোরেজ অ্যাকাউন্টের ধরন Standard General Purpose V2 হচ্ছে।

## ধাপ ২: একটি অ্যাজুর AI সার্চ সার্ভিস তৈরি করুন

১. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) এ সাইন ইন করুন।
২. বাম দিকের ন্যাভিগেশন প্যানেলে, **Create a resource** ক্লিক করুন।
৩. সার্চ বক্সে "Azure AI Search" টাইপ করুন এবং ফলাফলের তালিকা থেকে **Azure AI Search** নির্বাচন করুন।
৪. **Create** বোতামে ক্লিক করুন।
৫. **Basics** ট্যাবে নিচের তথ্য প্রদান করুন:
   - **Subscription**: আপনার অ্যাজুর সাবস্ক্রিপশন নির্বাচন করুন।
   - **Resource group**: একটি নতুন রিসোর্স গ্রুপ তৈরি করুন অথবা বিদ্যমান একটি নির্বাচন করুন।
   - **Resource name**: আপনার সার্চ সার্ভিসের জন্য একটি অনন্য নাম লিখুন।
   - **Region**: আপনার ব্যবহারকারীদের সবচেয়ে কাছের অঞ্চল নির্বাচন করুন।
   - **Pricing tier**: আপনার প্রয়োজন অনুযায়ী একটি মূল্য নির্ধারণ স্তর নির্বাচন করুন। পরীক্ষা করার জন্য ফ্রি স্তর দিয়ে শুরু করতে পারেন।
৬. **Review + create** ক্লিক করুন।
৭. সেটিংস পর্যালোচনা করুন এবং সার্চ সার্ভিস তৈরি করতে **Create** ক্লিক করুন।

## ধাপ ৩: অ্যাজুর AI সার্চ দিয়ে শুরু করুন

১. ডিপ্লয়মেন্ট সম্পন্ন হওয়ার পর, অ্যাজুর পোর্টালে আপনার সার্চ সার্ভিসে যান।
২. সার্চ সার্ভিস ওভারভিউ প্যানেলে URL কপি করুন। এটি দেখতে হবে `https://<service-name>.search.windows.net` এর মতো।
৩. **(প্রস্তাবিত)** Microsoft Entra ID (RBAC) সহ কীবিহীন অ্যাক্সেস সক্ষম করুন যেমন নিচের ধাপ ৪ তে দেখানো হয়েছে — কোন কি লাগবে না। এই গাইডের উদাহরণগুলি ইনডেক্স তৈরি/আপডেট করে এবং ডকুমেন্ট আপলোড করে, যা **Search Service Contributor** এবং **Search Index Data Contributor** রোল প্রয়োজন (অথবা, কীভিত্তিক অথেন্টিকেশনের জন্য, **primary admin key** — কুয়েরি কি নয়)। শুধুমাত্র যদি আপনি RBAC ব্যবহার করতে না পারেন, তাহলে **Settings > Keys** প্যানেল খুলুন এবং **primary admin key** কপি করুন।
৪. একটি ইনডেক্স তৈরি করতে, ডেটা আপলোড করতে এবং সার্চ চালাতে [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) পৃষ্ঠার ধাপগুলি অনুসরণ করুন।

## ধাপ ৪: অ্যাজুর AI সার্চ টুলস ব্যবহার করুন

অ্যাজুর AI সার্চ বিভিন্ন টুলের সাথে সংহত করা হয়েছে যা আপনার সার্চ ক্ষমতাকে উন্নত করে। উন্নত কনফিগারেশন এবং অপারেশনের জন্য আপনি Azure CLI, Python SDK, .NET SDK এবং অন্যান্য টুল ব্যবহার করতে পারেন।

### Azure CLI ব্যবহার

১. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) এ নির্দেশনা অনুসরণ করে Azure CLI ইনস্টল করুন।
২. কমান্ড দিয়ে Azure CLI তে সাইন ইন করুন:

   ```bash
   az login
   ```
3. **(প্রস্তাবিত) Microsoft Entra ID (RBAC) সহ কীবিহীন অ্যাক্সেস সক্ষম করুন:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC সক্রিয় হলে, নিচের Python এবং .NET SDK এর উদাহরণগুলি `DefaultAzureCredential` দিয়ে অথেন্টিকেট করে, যা আপনার `az login` সেশনটি লোকাল ডেভেলপমেন্টের সময় ব্যবহার করে — কোন অ্যাডমিন কি দরকার নেই। দেখুন [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)।

৪. **(বিকল্প) কীভিত্তিক অথেন্টিকেশন** — শুধুমাত্র যদি আপনি RBAC ব্যবহার করতে না পারেন, অ্যাডমিন কি সংরক্ষণ করুন:

#### Azure AI Search ইনস্ট্যান্সের জন্য শেষবিন্দু এবং API কী উভয়ই পরিবেশ ভেরিয়েবলে সংরক্ষণ করুন।

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

### Python SDK ব্যবহার

১. Azure Cognitive Search ক্লায়েন্ট লাইব্রেরি এবং Azure Identity for Python ইনস্টল করুন:

   ```bash
   pip install azure-search-documents azure-identity
   ```

২. ইনডেক্স তৈরি করতে এবং ডকুমেন্ট আপলোড করতে নিচের Python কোড ব্যবহার করুন:

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

### .NET SDK ব্যবহার

১. ইনডেক্স তৈরি এবং ডকুমেন্ট আপলোড করতে নিচের কমান্ডটি চালান:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    নিচের .NET উদাহরণটি `DefaultAzureCredential` ব্যবহার করে, যা আপনার অ্যাজুর CLI সাইন-ইন থেকে `az login` এর সময় ব্যবহার করতে পারে লোকাল ডেভেলপমেন্টে।

২. এখানে `AzureSearch.cs` এর .NET কোড দেওয়া হলো:

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

আরও বিস্তারিত তথ্যের জন্য নিম্নলিখিত ডকুমেন্টেশন দেখুন:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## উপসংহার

আপনি সফলভাবে অ্যাজুর পোর্টাল ব্যবহার করে অ্যাজুর AI সার্চ সেটআপ করেছেন এবং সংহত টুলগুলি ব্যবহার শুরু করেছেন। এখন আপনি অ্যাজুর AI সার্চের আরও উন্নত বৈশিষ্ট্য এবং ক্ষমতা অন্বেষণ করতে পারেন আপনার সার্চ সলিউশন উন্নত করার জন্য।

অতিরিক্ত সহায়তার জন্য, দেখুন [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691)।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা শুদ্ধতার জন্য চেষ্টা করি, অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার স্বভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে প্রয়োজনীয় ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->