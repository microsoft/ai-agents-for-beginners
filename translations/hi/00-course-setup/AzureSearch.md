<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:30:24+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "hi"
}
-->
# Azure AI Search सेटअप गाइड

यह गाइड आपको Azure पोर्टल का उपयोग करके Azure AI Search सेटअप करने में मदद करेगा। नीचे दिए गए चरणों का पालन करें ताकि आप अपना Azure AI Search सेवा बना और कॉन्फ़िगर कर सकें।

## आवश्यकताएँ

शुरू करने से पहले, सुनिश्चित करें कि आपके पास निम्नलिखित हैं:

- एक Azure सब्सक्रिप्शन। यदि आपके पास Azure सब्सक्रिप्शन नहीं है, तो आप [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) पर एक मुफ्त खाता बना सकते हैं।

## चरण 1: Azure स्टोरेज अकाउंट बनाएं

1. इस निर्देश का पालन करें, [Azure स्टोरेज अकाउंट बनाएं](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), एक नया Azure स्टोरेज अकाउंट बनाने के लिए।
   **NOTE**: सुनिश्चित करें कि स्टोरेज अकाउंट का प्रकार Standard General Purpose V2 है।

## चरण 2: Azure AI Search सेवा बनाएं

1. [Azure पोर्टल](https://portal.azure.com/?wt.mc_id=studentamb_258691) में साइन इन करें।
2. बाएँ नेविगेशन पैन में, **Create a resource** पर क्लिक करें।
3. सर्च बॉक्स में "Azure AI Search" टाइप करें और परिणामों की सूची से **Azure AI Search** चुनें।
4. **Create** बटन पर क्लिक करें।
5. **Basics** टैब में निम्नलिखित जानकारी प्रदान करें:
   - **Subscription**: अपना Azure सब्सक्रिप्शन चुनें।
   - **Resource group**: एक नया रिसोर्स ग्रुप बनाएं या मौजूदा चुनें।
   - **Resource name**: अपनी सर्च सेवा के लिए एक यूनिक नाम दर्ज करें।
   - **Region**: अपने उपयोगकर्ताओं के सबसे नजदीकी क्षेत्र का चयन करें।
   - **Pricing tier**: अपनी आवश्यकताओं के अनुसार एक प्राइसिंग टियर चुनें। आप परीक्षण के लिए Free टियर से शुरू कर सकते हैं।
6. **Review + create** पर क्लिक करें।
7. सेटिंग्स की समीक्षा करें और सर्च सेवा बनाने के लिए **Create** पर क्लिक करें।

## चरण 3: Azure AI Search के साथ शुरुआत करें

1. एक बार तैनाती पूरी हो जाने के बाद, Azure पोर्टल में अपनी सर्च सेवा पर जाएं।
2. सर्च सेवा ओवरव्यू पैन में, URL कॉपी करें। यह इस तरह दिखना चाहिए `https://<service-name>.search.windows.net`।
3. Settings > Keys पैन में, क्वेरी की कॉपी करें।
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) पेज पर दिए गए चरणों का पालन करें ताकि आप एक इंडेक्स बना सकें, डेटा अपलोड कर सकें, और सर्च क्वेरी कर सकें।

## चरण 4: Azure AI Search टूल्स का उपयोग करें

Azure AI Search विभिन्न टूल्स के साथ इंटीग्रेट होता है ताकि आपकी सर्च क्षमताओं को बढ़ाया जा सके। आप Azure CLI, Python SDK, .NET SDK और अन्य टूल्स का उपयोग उन्नत कॉन्फ़िगरेशन और संचालन के लिए कर सकते हैं।

### Azure CLI का उपयोग करना

1. Azure CLI इंस्टॉल करने के लिए [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) निर्देशों का पालन करें।
2. Azure CLI में साइन इन करने के लिए निम्नलिखित कमांड का उपयोग करें:

   ```bash
   az login
   ```

3. Azure AI Search इंस्टेंस के लिए दोनों endpoint और API key को एनवायरनमेंट वेरिएबल्स में स्टोर करें।

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

### Python SDK का उपयोग करना

1. Azure Cognitive Search क्लाइंट लाइब्रेरी को Python के लिए इंस्टॉल करें:

   ```bash
   pip install azure-search-documents
   ```

2. निम्नलिखित Python कोड का उपयोग करके एक इंडेक्स बनाएं और डॉक्यूमेंट अपलोड करें:

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

### .NET SDK का उपयोग करना

1. निम्नलिखित कमांड का उपयोग करके एक इंडेक्स बनाएं और डॉक्यूमेंट अपलोड करें:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. यहाँ `AzureSearch.cs` का .NET कोड है:

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

अधिक विस्तृत जानकारी के लिए निम्नलिखित दस्तावेज़ देखें:

- [Azure Cognitive Search सेवा बनाएं](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search के साथ शुरुआत करें](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search टूल्स](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

आपने सफलतापूर्वक Azure पोर्टल का उपयोग करके Azure AI Search सेटअप कर लिया है और टूल्स को इंटीग्रेट कर लिया है। अब आप Azure AI Search की अधिक उन्नत विशेषताओं और क्षमताओं का पता लगा सकते हैं ताकि अपनी सर्च सॉल्यूशंस को बेहतर बना सकें।

अधिक सहायता के लिए, [Azure Cognitive Search दस्तावेज़](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) पर जाएं।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।