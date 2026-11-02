# Azure AI Search सेटअप गाइड

यह गाइड आपको Azure पोर्टल का उपयोग करके Azure AI Search सेटअप करने में मदद करेगी। नीचे दिए गए चरणों का पालन करके अपने Azure AI Search सेवा बनाएं और कॉन्फ़िगर करें।

## पूर्वापेक्षाएँ

शुरू करने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित हैं:

- एक Azure सदस्यता। यदि आपके पास Azure सदस्यता नहीं है, तो आप [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) पर जाकर एक मुफ्त खाता बना सकते हैं।

## चरण 1: एक Azure स्टोरेज खाता बनाएँ

1. इस निर्देश, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), का पालन करें और एक नया Azure स्टोरेज खाता बनाएं।
   **नोट**: सुनिश्चित करें कि Storage Account का प्रकार Standard General Purpose V2 हो।

## चरण 2: एक Azure AI Search सेवा बनाएँ

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) में साइन इन करें।
2. बाएँ हाथ की नेविगेशन पेन में, **Create a resource** पर क्लिक करें।
3. खोज बॉक्स में "Azure AI Search" टाइप करें और परिणामों की सूची से **Azure AI Search** चुनें।
4. **Create** बटन पर क्लिक करें।
5. **Basics** टैब में निम्नलिखित जानकारी प्रदान करें:
   - **Subscription**: अपनी Azure सदस्यता चुनें।
   - **Resource group**: नया रिसोर्स ग्रुप बनाएं या कोई मौजूदा चुनें।
   - **Resource name**: अपनी सर्च सेवा के लिए एक यूनिक नाम दर्ज करें।
   - **Region**: अपने उपयोगकर्ताओं के सबसे नजदीकी क्षेत्र को चुनें।
   - **Pricing tier**: अपने आवश्यकताओं के अनुसार प्राइसिंग टियर चुनें। आप परीक्षण के लिए Free टियर से शुरू कर सकते हैं।
6. **Review + create** पर क्लिक करें।
7. सेटिंग्स की समीक्षा करें और सर्च सेवा बनाने के लिए **Create** पर क्लिक करें।

## चरण 3: Azure AI Search के साथ शुरू करें

1. डिप्लॉयमेंट पूरी होने के बाद, Azure पोर्टल में अपनी सर्च सेवा पर जाएं।
2. सर्च सेवा ओवरव्यू पेन में, URL कॉपी करें। यह कुछ ऐसा दिखना चाहिए: `https://<service-name>.search.windows.net`।
3. **(अनुशंसित)** Microsoft Entra ID (RBAC) के साथ कीलेस एक्सेस सक्षम करें जैसा कि नीचे चरण 4 में दिखाया गया है — किसी कुंजी की आवश्यकता नहीं। इस गाइड के उदाहरण इंडेक्स बनाने/अपडेट करने और दस्तावेज़ अपलोड करने के लिए हैं, जिन्हें **Search Service Contributor** और **Search Index Data Contributor** भूमिकाओं की आवश्यकता होती है (या, की-आधारित प्रमाणीकरण के लिए, **primary admin key** — query key नहीं)। केवल यदि आप RBAC का उपयोग नहीं कर सकते हैं, तो **Settings > Keys** पेन खोलें और **primary admin key** कॉपी करें।
4. इंडेक्स बनाने, डेटा अपलोड करने और खोज करने के लिए [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) पेज में दिए गए चरणों का पालन करें।

## चरण 4: Azure AI Search उपकरणों का उपयोग करें

Azure AI Search विभिन्न उपकरणों के साथ एकीकृत होता है ताकि आपकी खोज क्षमताओं को बढ़ाया जा सके। आप उन्नत कॉन्फ़िगरेशन और ऑपरेशनों के लिए Azure CLI, Python SDK, .NET SDK और अन्य उपकरणों का उपयोग कर सकते हैं।

### Azure CLI का उपयोग करना

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) पर दिए निर्देशों का पालन करके Azure CLI स्थापित करें।
2. Azure CLI में साइन इन करने के लिए कमांड चलाएं:

   ```bash
   az login
   ```
3. **(अनुशंसित) Microsoft Entra ID (RBAC) के साथ कीलेस एक्सेस सक्षम करें:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC सक्षम होने पर, नीचे दिए गए Python और .NET SDK उदाहरण `DefaultAzureCredential` के साथ प्रमाणीकरण करते हैं, जो आपके `az login` सत्र का उपयोग स्थानीय विकास के दौरान करता है — किसी admin key की आवश्यकता नहीं। देखें [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)।

4. **(वैकल्पिक) की-आधारित प्रमाणीकरण** — यदि आप RBAC का उपयोग नहीं कर सकते हैं, तो admin key भी संग्रहित करें:

#### Azure AI Search उदाहरण के लिए अंत बिंदु और API कुंजी को पर्यावरण चर के रूप में संग्रहित करें।

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

### Python SDK का उपयोग करना

1. Azure Cognitive Search क्लाइंट लाइब्रेरी और Azure Identity for Python इंस्टॉल करें:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. आगे दिए गए Python कोड का उपयोग करके इंडेक्स बनाएं और दस्तावेज़ अपलोड करें:

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

### .NET SDK का उपयोग करना

1. इंडेक्स बनाने और दस्तावेज़ अपलोड करने के लिए निम्न कमांड चलाएं:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    नीचे दिया गया .NET उदाहरण `DefaultAzureCredential` का उपयोग करता है, जो स्थानीय विकास के दौरान आपके Azure CLI साइन-इन `az login` का उपयोग कर सकता है।

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

अधिक विस्तार से जानकारी के लिए, निम्नलिखित दस्तावेज़ देखें:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

आपने सफलतापूर्वक Azure पोर्टल का उपयोग करके Azure AI Search सेटअप कर लिया है और उपकरणों को एकीकृत कर लिया है। अब आप Azure AI Search की और अधिक उन्नत सुविधाओं और क्षमताओं का अन्वेषण कर सकते हैं ताकि अपने खोज समाधान को बेहतर बनाया जा सके।

आगे सहायता के लिए, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) पर जाएं।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->