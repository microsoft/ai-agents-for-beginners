# Azure AI Search सेटअप गाइड

यह गाइड आपको Azure पोर्टल का उपयोग करके Azure AI Search सेटअप करने में मदद करेगी। अपना Azure AI Search सेवा बनाने और कॉन्फ़िगर करने के लिए नीचे दिए गए चरणों का पालन करें।

## आवश्यकताएँ

शुरू करने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित हैं:

- एक Azure सब्सक्रिप्शन। यदि आपके पास Azure सब्सक्रिप्शन नहीं है, तो आप [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) पर एक मुफ्त खाता बना सकते हैं।

## चरण 1: एक Azure Storage Account बनाएं

1. इस निर्देश का पालन करें, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), एक नया Azure Storage Account बनाने के लिए।
   **NOTE**: सुनिश्चित करें कि Storage Account का प्रकार Standard General Purpose V2 हो।

## चरण 2: एक Azure AI Search सेवा बनाएं

1. [Azure पोर्टल](https://portal.azure.com/?wt.mc_id=studentamb_258691) में साइन इन करें।
2. बाएँ हाथ के नेविगेशन पेन में, **Create a resource** पर क्लिक करें।
3. खोज बॉक्स में, "Azure AI Search" टाइप करें और परिणामों की सूची में से **Azure AI Search** चुनें।
4. **Create** बटन पर क्लिक करें।
5. **Basics** टैब में, निम्न जानकारी प्रदान करें:
   - **Subscription**: अपना Azure सब्सक्रिप्शन चुनें।
   - **Resource group**: एक नया resource group बनाएं या किसी मौजूदा को चुनें।
   - **Resource name**: अपनी खोज सेवा के लिए एक अद्वितीय नाम दर्ज करें।
   - **Region**: अपने उपयोगकर्ताओं के सबसे नजदीकी क्षेत्र को चुनें।
   - **Pricing tier**: अपनी आवश्यकताओं के अनुसार एक मूल्य निर्धारण स्तर चुनें। परीक्षण के लिए आप Free tier से शुरू कर सकते हैं।
6. **Review + create** पर क्लिक करें।
7. सेटिंग्स की समीक्षा करें और खोज सेवा बनाने के लिए **Create** पर क्लिक करें।

## चरण 3: Azure AI Search के साथ शुरुआत करें

1. एक बार डिप्लॉयमेंट पूरा हो जाने पर, Azure पोर्टल में अपनी खोज सेवा पर जाएं।
2. खोज सेवा अवलोकन पेन में, URL कॉपी करें। यह इस तरह दिखना चाहिए `https://<service-name>.search.windows.net`।
3. **(अनुशंसित)** Microsoft Entra ID (RBAC) के साथ keyless access सक्षम करें जैसा कि नीचे चरण 4 में दिखाया गया है — किसी कुंजी की आवश्यकता नहीं। इस गाइड में उदाहरण इंडेक्स बनाने/अपडेट करने और दस्तावेज़ अपलोड करने के लिए हैं, जिनके लिए **Search Service Contributor** और **Search Index Data Contributor** भूमिकाओं की आवश्यकता होती है (या key-based auth के लिए, **primary admin key** — query key नहीं)। केवल यदि आप RBAC का उपयोग नहीं कर पाते हैं, तो **Settings > Keys** पेन खोलें और **primary admin key** कॉपी करें।
4. एक इंडेक्स बनाने, डेटा अपलोड करने, और खोज करने के लिए [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) पेज में दिए गए चरणों का पालन करें।

## चरण 4: Azure AI Search टूल्स का उपयोग करें

Azure AI Search विभिन्न टूल्स के साथ एकीकृत होता है ताकि आपकी खोज क्षमताओं को बढ़ाया जा सके। आप उन्नत कॉन्फ़िगरेशन और ऑपरेशनों के लिए Azure CLI, Python SDK, .NET SDK और अन्य टूल्स का उपयोग कर सकते हैं।

### Azure CLI का उपयोग करना

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) पर दिए गए निर्देशों का पालन करके Azure CLI इंस्टॉल करें।
2. Azure CLI में साइन इन करने के लिए कमांड चलाएं:

   ```bash
   az login
   ```
3. **(अनुशंसित) Microsoft Entra ID (RBAC) के साथ keyless access सक्षम करें:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search सेवा प्रदर्शित में कोई "endpoint" फ़ील्ड नहीं है; सेवा नाम से URL बनाएं।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC सक्षम होने पर, नीचे दिए गए Python और .NET SDK उदाहरण `DefaultAzureCredential` के साथ प्रमाणीकृत होते हैं, जो स्थानीय विकास के दौरान आपके `az login` सत्र का उपयोग करता है — किसी एडमिन कुंजी की आवश्यकता नहीं। देखें [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)।

4. **(गलतफ़हमी निकास) Key-based auth** — केवल यदि आप RBAC का उपयोग नहीं कर पाते हैं, तो एडमिन कुंजी भी सहेजें:

#### Azure AI Search इंस्टेंस के लिए एंडपॉइंट और API कुंजी दोनों को पर्यावरण चर के रूप में सहेजें।

    ```bash
    # zsh/bash
    # az search service show में "endpoint" फ़ील्ड नहीं है; सेवा नाम से URL बनाएं।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show में "endpoint" फ़ील्ड नहीं है; सेवा नाम से URL बनाएं।
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK का उपयोग करना

1. Azure Cognitive Search क्लाइंट लाइब्रेरी और Azure Identity को Python के लिए इंस्टॉल करें:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. इंडेक्स बनाने और दस्तावेज़ अपलोड करने के लिए निम्न Python कोड का उपयोग करें:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # बिना कुंजी के (अनुशंसित): Entra ID RBAC के माध्यम से आपके `az login` पहचान का उपयोग करता है।
    # "Search Service Contributor" और "Search Index Data Contributor" भूमिकाओं की आवश्यकता होती है।
    credential = DefaultAzureCredential()
    # प्रतिक्रिया विकल्प (कुंजी-आधारित प्रमाणीकरण):
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

1. इंडेक्स बनाने और दस्तावेज़ अपलोड करने के लिए निम्न कमांड चलाएं:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    नीचे दिया गया .NET उदाहरण `DefaultAzureCredential` का उपयोग करता है, जो स्थानीय विकास के दौरान आपके `az login` से Azure CLI साइन-इन का उपयोग कर सकता है।

2. यहाँ `AzureSearch.cs` का .NET कोड है:

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

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

आपने सफलतापूर्वक Azure पोर्टल और एकीकृत टूल्स का उपयोग करके Azure AI Search सेटअप कर लिया है। अब आप Azure AI Search की अधिक उन्नत सुविधाओं और क्षमताओं का उपयोग करके अपनी खोज समाधानों को बेहतर बना सकते हैं।

आगे सहायता के लिए, [Azure Cognitive Search दस्तावेज़](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) पर जाएं।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->