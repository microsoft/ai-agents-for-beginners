# Azure AI Search सेटअप गाइड

यह गाइड आपको Azure पोर्टल का उपयोग करके Azure AI Search सेटअप करने में मदद करेगा। अपने Azure AI Search सेवा को बनाने और कॉन्फ़िगर करने के लिए नीचे दिए गए चरणों का पालन करें।

## पूर्वापेक्षाएँ

शुरू करने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित हैं:

- एक Azure सब्सक्रिप्शन। यदि आपके पास Azure सब्सक्रिप्शन नहीं है, तो आप [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) पर जाकर एक मुफ्त खाता बना सकते हैं।

## चरण 1: एक Azure स्टोरेज अकाउंट बनाएं

1. इस निर्देश, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), का पालन करें और एक नया Azure स्टोरेज अकाउंट बनाएं।
   **नोट**: सुनिश्चित करें कि स्टोरेज अकाउंट का प्रकार Standard General Purpose V2 हो।

## चरण 2: एक Azure AI Search सेवा बनाएं

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) में साइन इन करें।
2. बाएं हाथ के नेविगेशन पेन में, **Create a resource** पर क्लिक करें।
3. खोज बॉक्स में "Azure AI Search" टाइप करें और परिणामों में से **Azure AI Search** चुनें।
4. **Create** बटन पर क्लिक करें।
5. **Basics** टैब में, निम्नलिखित जानकारी प्रदान करें:
   - **Subscription**: अपनी Azure सब्सक्रिप्शन चुनें।
   - **Resource group**: नया रिसोर्स ग्रुप बनाएं या मौजूदा में से चुनें।
   - **Resource name**: अपनी खोज सेवा के लिए एक अद्वितीय नाम दर्ज करें।
   - **Region**: अपने उपयोगकर्ताओं के नज़दीकी क्षेत्र का चयन करें।
   - **Pricing tier**: एक ऐसा मूल्य निर्धारण स्तर चुनें जो आपकी आवश्यकताओं के अनुरूप हो। परीक्षण के लिए आप Free tier से शुरुआत कर सकते हैं।
6. **Review + create** पर क्लिक करें।
7. सेटिंग्स की समीक्षा करें और सेवा बनाने के लिए **Create** पर क्लिक करें।

## चरण 3: Azure AI Search के साथ शुरुआत करें

1. तैनाती पूरी होने के बाद, Azure पोर्टल में अपनी खोज सेवा पर जाएं।
2. खोज सेवा के अवलोकन पेन में, URL कॉपी करें। यह `https://<service-name>.search.windows.net` जैसा दिखना चाहिए।
3. **(अनुशंसित)** Microsoft Entra ID (RBAC) के साथ बिना कुंजी पहुँच (keyless access) सक्षम करें जैसा कि नीचे चरण 4 में दिखाया गया है — कोई कुंजी आवश्यक नहीं। इस गाइड के नमूने इंडेक्स बनाने/अपडेट करने और दस्तावेज़ अपलोड करने के लिए **Search Service Contributor** एवं **Search Index Data Contributor** भूमिकाओं (या कुंजी-आधारित प्रमाणीकरण के लिए, **primary admin key** — क्वेरी कुंजी नहीं) की आवश्यकता होती है। केवल यदि आप RBAC का उपयोग नहीं कर सकते हैं, तो **Settings > Keys** पेन खोलें और **primary admin key** कॉपी करें।
4. इंडेक्स बनाने, डेटा अपलोड करने और खोज करने के लिए [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) के चरणों का पालन करें।

## चरण 4: Azure AI Search टूल्स का उपयोग करें

Azure AI Search आपकी खोज क्षमताओं को बढ़ाने के लिए विभिन्न टूल्स के साथ एकीकृत होता है। आप उन्नत कॉन्फ़िगरेशन और संचालन के लिए Azure CLI, Python SDK, .NET SDK और अन्य टूल्स का उपयोग कर सकते हैं।

### Azure CLI का उपयोग करना

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) पर दिए गए निर्देशों का पालन करके Azure CLI इंस्टॉल करें।
2. कमांड का उपयोग करके Azure CLI में साइन इन करें:

   ```bash
   az login
   ```
3. **(अनुशंसित) Microsoft Entra ID (RBAC) के साथ बिना कुंजी पहुँच सक्षम करें:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search सेवा शो में "endpoint" फ़ील्ड नहीं है; सेवा नाम से URL बनाएं।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC सक्षम होने पर, नीचे दिए गए Python और .NET SDK नमूने `DefaultAzureCredential` के साथ प्रमाणीकरण करते हैं, जो स्थानीय विकास के समय आपके `az login` सत्र का उपयोग करता है — कोई एडमिन कुंजी आवश्यक नहीं। देखें [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)।

4. **(बैकअप विकल्प) कुंजी-आधारित प्रमाणीकरण** — केवल यदि आप RBAC का उपयोग नहीं कर सकते, तो एडमिन कुंजी भी स्टोर करें:

#### Azure AI Search इंस्टेंस के लिए दोनों एंडपॉइंट और API कुंजी को पर्यावरण वेरिएबल्स में स्टोर करें।

    ```bash
    # zsh/bash
    # az search service show में "endpoint" फील्ड नहीं है; सेवा नाम से URL बनाएं।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show में "endpoint" फील्ड नहीं है; सेवा नाम से URL बनाएं।
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK का उपयोग करना

1. Azure Cognitive Search क्लाइंट लाइब्रेरी और Azure Identity Python के लिए इंस्टॉल करें:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. एक इंडेक्स बनाने और दस्तावेज़ अपलोड करने के लिए निम्न Python कोड का उपयोग करें:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # कीलेस (सिफ़ारिश की गई): आपका `az login` पहचान Entra ID RBAC के माध्यम से उपयोग करता है।
    # "सर्च सर्विस कॉन्ट्रिब्यूटर" और "सर्च इंडेक्स डेटा कॉन्ट्रिब्यूटर" भूमिकाओं की आवश्यकता होती है।
    credential = DefaultAzureCredential()
    # फॉलबैक (की-आधारित प्रमाणीकरण):
    # azure.core.credentials से AzureKeyCredential आयात करें
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

### .NET SDK का उपयोग करना

1. एक इंडेक्स बनाने और दस्तावेज़ अपलोड करने के लिए निम्न कमांड चलाएं:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    नीचे दिया .NET नमूना `DefaultAzureCredential` का उपयोग करता है, जो स्थानीय विकास के दौरान आपके Azure CLI `az login` साइन-इन का उपयोग कर सकता है।

2. यहाँ `AzureSearch.cs` की .NET कोड है:

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

अधिक विस्तृत जानकारी के लिए, निम्नलिखित दस्तावेज़ देखें:

- [एक Azure Cognitive Search सेवा बनाएं](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search के साथ शुरुआत करें](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search टूल्स](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

आपने Azure पोर्टल और एकीकृत टूल्स का उपयोग करके सफलतापूर्वक Azure AI Search सेटअप कर लिया है। अब आप अपनी खोज समाधानों को बेहतर बनाने के लिए Azure AI Search की अधिक उन्नत विशेषताओं और क्षमताओं का पता लगा सकते हैं।

अतिरिक्त सहायता के लिए [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) पर जाएं।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->