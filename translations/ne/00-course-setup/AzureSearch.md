# Azure AI खोज सेटअप गाइड

यस गाइडले तपाईंलाई Azure पोर्टल प्रयोग गरी Azure AI खोज सेटअप गर्न मद्दत गर्नेछ। तपाईंको Azure AI खोज सेवा सिर्जना र कन्फिगर गर्न तलका चरणहरू अनुसरण गर्नुहोस्।

## पूर्वापेक्षाहरू

सुरु गर्नुभन्दा पहिले, सुनिश्चित गर्नुहोस् कि तपाईंसँग तलका वस्तुहरू छन्:

- एउटा Azure सदस्यता। यदि तपाईंसँग Azure सदस्यता छैन भने, तपाईं [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) मा निःशुल्क खाता बनाउन सक्नुहुन्छ।

## चरण 1: Azure स्टोरेज खाता सिर्जना गर्नुहोस्

1. नयाँ Azure स्टोरेज खाता सिर्जना गर्न यो निर्देशन अनुसरण गर्नुहोस्, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal)।
   **NOTE**: स्टोरेज खाताको प्रकार Standard General Purpose V2 हुनुपर्नेछ।

## चरण 2: Azure AI खोज सेवा सिर्जना गर्नुहोस्

1. [Azure पोर्टल](https://portal.azure.com/?wt.mc_id=studentamb_258691) मा साइन इन गर्नुहोस्।
2. बाँया नेभिगेसन प्यानमा, **Create a resource** मा क्लिक गर्नुहोस्।
3. खोज बक्समा "Azure AI Search" टाइप गर्नुहोस् र नतिजाहरूबाट **Azure AI Search** चयन गर्नुहोस्।
4. **Create** बटनमा क्लिक गर्नुहोस्।
5. **Basics** ट्याबमा तलका विवरणहरू प्रदान गर्नुहोस्:
   - **Subscription**: तपाईंको Azure सदस्यता चयन गर्नुहोस्।
   - **Resource group**: नयाँ स्रोत समूह सिर्जना गर्नुहोस् वा अवस्थित समूह चयन गर्नुहोस्।
   - **Resource name**: तपाईंको खोज सेवाको लागि अनौठो नाम प्रविष्ट गर्नुहोस्।
   - **Region**: तपाईंका प्रयोगकर्तासँग नजिकको क्षेत्र चयन गर्नुहोस्।
   - **Pricing tier**: तपाईंको आवश्यकताअनुसार मूल्य निर्धारण तह चयन गर्नुहोस्। परीक्षणका लागि नि:शुल्क तहबाट सुरु गर्न सक्नुहुन्छ।
6. **Review + create** मा क्लिक गर्नुहोस्।
7. सेटिङहरू समीक्षा गरी सेवा सिर्जना गर्न **Create** मा क्लिक गर्नुहोस्।

## चरण 3: Azure AI खोजबाट सुरू गर्नुहोस्

1. एक पटक डिप्लोयमेन्ट पूरा भएपछि, Azure पोर्टलमा तपाईंको खोज सेवामा जानुहोस्।
2. खोज सेवा अवलोकन प्यानमा, URL प्रतिलिपि गर्नुहोस्। यसले `https://<service-name>.search.windows.net` जस्तो देखिनुपर्छ।
3. **(सिफारिस गरिएको)** Microsoft Entra ID (RBAC) सँग कुञ्जी-रहित पहुँच सक्षम गर्नुहोस् (सुरुमा चरण 4 मा देखाइएको अनुसार) — कुञ्जी आवश्यक छैन। यस गाइडका नमूनाहरू इन्डेक्सहरू सिर्जना/अपडेट र कागजातहरू अपलोड गर्छन्, जसले **Search Service Contributor** र **Search Index Data Contributor** भूमिका (वा कुञ्जी-आधारित प्रमाणीकरणका लागि, मुख्य प्रशासक कुञ्जी — प्रश्न कुञ्जी होइन) आवश्यक पर्छ। RBAC प्रयोग गर्न नसकेको खण्डमा मात्र, **Settings > Keys** प्यान खोल्नुहोस् र **primary admin key** प्रतिलिपि गर्नुहोस्।
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) पृष्ठमा उल्लिखित चरणहरू अनुसरण गरी इन्डेक्स सिर्जना गर्नुहोस्, डेटा अपलोड गर्नुहोस्, र खोज प्रदर्शन गर्नुहोस्।

## चरण 4: Azure AI खोज उपकरणहरू प्रयोग गर्नुहोस्

Azure AI खोजले तपाईंको खोज क्षमताहरू सुधार गर्न विभिन्न उपकरणहरू सँग एकीकृत गर्छ। तपाईं Azure CLI, Python SDK, .NET SDK र अन्य उपकरणहरू प्रयोग गरी उन्नत कन्फिगरेसन र अपरेसनहरू गर्न सक्नुहुन्छ।

### Azure CLI प्रयोग गर्दै

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) मा उल्लेखित निर्देशन अनुसार Azure CLI स्थापना गर्नुहोस्।
2. तलको कमाण्ड प्रयोग गरेर Azure CLI मा साइन इन गर्नुहोस्:

   ```bash
   az login
   ```
3. **(सिफारिस गरिएको) Microsoft Entra ID (RBAC) सँग कुञ्जी-रहित पहुँच सक्षम गर्नुहोस्:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search सर्भिस शोमा "endpoint" फिल्ड छैन; सेवा नामबाट URL निर्माण गर्नुहोस्।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC सक्षम हुँदा, तलका Python र .NET SDK नमूनाहरू `DefaultAzureCredential` सँग प्रमाणित हुन्छन्, जसले स्थानीय विकासका समयमा तपाईंको `az login` सत्र प्रयोग गर्छ — कुनै प्रशासक कुञ्जी आवश्यक छैन। [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac) हेर्नुहोस्।

4. **(फ्यालब्याक) कुञ्जी-आधारित प्रमाणीकरण** — मात्र RBAC प्रयोग गर्न नसकेको खण्डमा, प्रशासक कुञ्जी पनि संग्रह गर्नुहोस्:

#### Azure AI खोज उदाहरणको लागि अन्तिम बिन्दु र API कुञ्जी वातावरण चरहरूमा संग्रह गर्नुहोस्।

    ```bash
    # zsh/bash
    # az search service show मा "endpoint" फिल्ड छैन; सेवाको नामबाट URL बनाउनुहोस्।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show मा "endpoint" फिल्ड छैन; सेवाको नामबाट URL बनाउनुहोस्।
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK प्रयोग गर्दै

1. Azure Cognitive Search क्लाइन्ट लाइब्रेरी र Azure Identity Python को लागि स्थापना गर्नुहोस्:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. इन्डेक्स सिर्जना गर्न र कागजातहरू अपलोड गर्न तलको Python कोड प्रयोग गर्नुहोस्:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # Keyless (सिफारिस गरिएको): Entra ID RBAC मार्फत तपाईँको `az login` पहिचान प्रयोग गर्दछ।
    # "Search Service Contributor" र "Search Index Data Contributor" भूमिकाहरू आवश्यक पर्दछ।
    credential = DefaultAzureCredential()
    # फल्याक (चाबी-आधारित प्रमाणीकरण):
    # azure.core.credentials बाट AzureKeyCredential आयात गर्नुहोस्
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

### .NET SDK प्रयोग गर्दै

1. इन्डेक्स सिर्जना गर्न र कागजातहरू अपलोड गर्न तलको कमाण्ड चलाउनुहोस्:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    तलको .NET नमूनाले `DefaultAzureCredential` प्रयोग गर्छ, जसले स्थानीय विकासमा तपाईंको `az login` Azure CLI साइन-इन प्रयोग गर्न सक्छ।

2. यहाँ `AzureSearch.cs` को .NET कोड छ:

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

थप विस्तृत जानकारीको लागि तलका दस्तावेजहरू हेर्नुहोस्:

- [Azure Cognitive Search सेवा सिर्जना गर्नुहोस्](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Azure Cognitive Search बाट सुरू गर्नुहोस्](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI खोज उपकरणहरू](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

तपाईंले Azure पोर्टल र एकीकृत उपकरणहरू प्रयोग गरेर सफलतापूर्वक Azure AI खोज सेटअप गर्नुभएको छ। अब तपाईं Azure AI खोजका थप उन्नत फिचरहरू र क्षमताहरू अन्वेषण गरी तपाईंको खोज समाधानहरूलाई सुधार गर्न सक्नुहुनेछ।

थप सहयोगका लागि, [Azure Cognitive Search कागजात](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) भ्रमण गर्नुहोस्।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->