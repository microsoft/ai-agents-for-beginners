<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:31:51+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "mr"
}
-->
# Azure AI Search सेटअप मार्गदर्शक

हा मार्गदर्शक तुम्हाला Azure पोर्टल वापरून Azure AI Search सेटअप करण्यात मदत करेल. Azure AI Search सेवा तयार आणि कॉन्फिगर करण्यासाठी खालील चरणांचे अनुसरण करा.

## पूर्वअट

सुरुवात करण्यापूर्वी, तुमच्याकडे खालील गोष्टी असणे आवश्यक आहे:

- Azure सदस्यता. जर तुमच्याकडे Azure सदस्यता नसेल, तर तुम्ही [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) येथे विनामूल्य खाते तयार करू शकता.

## चरण 1: Azure स्टोरेज खाते तयार करा

1. नवीन Azure स्टोरेज खाते तयार करण्यासाठी [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) या सूचनांचे अनुसरण करा.  
   **NOTE**: खात्री करा की स्टोरेज अकाउंटचा प्रकार Standard General Purpose V2 आहे.

## चरण 2: Azure AI Search सेवा तयार करा

1. [Azure पोर्टल](https://portal.azure.com/?wt.mc_id=studentamb_258691) मध्ये साइन इन करा.
2. डाव्या बाजूच्या नेव्हिगेशन पॅनमध्ये, **Create a resource** वर क्लिक करा.
3. शोध बॉक्समध्ये "Azure AI Search" टाइप करा आणि निकालांच्या यादीतून **Azure AI Search** निवडा.
4. **Create** बटणावर क्लिक करा.
5. **Basics** टॅबमध्ये, खालील माहिती भरा:
   - **Subscription**: तुमची Azure सदस्यता निवडा.
   - **Resource group**: नवीन रिसोर्स ग्रुप तयार करा किंवा विद्यमान निवडा.
   - **Resource name**: तुमच्या सर्च सेवेचे एक अद्वितीय नाव प्रविष्ट करा.
   - **Region**: तुमच्या वापरकर्त्यांच्या जवळचा प्रदेश निवडा.
   - **Pricing tier**: तुमच्या गरजेनुसार प्राइसिंग टियर निवडा. चाचणीसाठी तुम्ही Free टियरने सुरुवात करू शकता.
6. **Review + create** वर क्लिक करा.
7. सेटिंग्ज पुनरावलोकन करा आणि सर्च सेवा तयार करण्यासाठी **Create** वर क्लिक करा.

## चरण 3: Azure AI Search सुरू करा

1. डिप्लॉयमेंट पूर्ण झाल्यावर, Azure पोर्टलमध्ये तुमच्या सर्च सेवेकडे जा.
2. सर्च सेवा ओव्हरव्ह्यू पॅनमध्ये, URL कॉपी करा. हे `https://<service-name>.search.windows.net` असे दिसेल.
3. Settings > Keys पॅनमध्ये, क्वेरी की कॉपी करा.
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) पृष्ठावरील चरणांचे अनुसरण करून इंडेक्स तयार करा, डेटा अपलोड करा आणि सर्च क्वेरी करा.

## चरण 4: Azure AI Search साधने वापरा

Azure AI Search विविध साधनांसह एकत्रित होते ज्यामुळे तुमच्या सर्च क्षमतांमध्ये सुधारणा होते. प्रगत कॉन्फिगरेशन आणि ऑपरेशन्ससाठी तुम्ही Azure CLI, Python SDK, .NET SDK आणि इतर साधने वापरू शकता.

### Azure CLI वापरणे

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) येथे दिलेल्या सूचनांचे अनुसरण करून Azure CLI स्थापित करा.
2. खालील कमांड वापरून Azure CLI मध्ये साइन इन करा:

   ```bash
   az login
   ```

3. Azure AI Search इंस्टन्ससाठी एंडपॉइंट आणि API की पर्यावरणीय व्हेरिएबल्समध्ये साठवा.

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

### Python SDK वापरणे

1. Python साठी Azure Cognitive Search क्लायंट लायब्ररी स्थापित करा:

   ```bash
   pip install azure-search-documents
   ```

2. खालील Python कोड वापरून इंडेक्स तयार करा आणि दस्तऐवज अपलोड करा:

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

### .NET SDK वापरणे

1. इंडेक्स तयार करण्यासाठी आणि दस्तऐवज अपलोड करण्यासाठी खालील कमांड चालवा:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. `AzureSearch.cs` चा .NET कोड येथे आहे:

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

अधिक तपशीलवार माहितीसाठी, खालील दस्तऐवजांचा संदर्भ घ्या:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

तुम्ही Azure पोर्टल वापरून Azure AI Search यशस्वीरित्या सेटअप केले आहे आणि साधने एकत्रित केली आहेत. आता तुम्ही Azure AI Search च्या अधिक प्रगत वैशिष्ट्ये आणि क्षमतांचा शोध घेऊ शकता आणि तुमच्या सर्च सोल्यूशन्स सुधारू शकता.

अधिक मदतीसाठी, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) ला भेट द्या.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.