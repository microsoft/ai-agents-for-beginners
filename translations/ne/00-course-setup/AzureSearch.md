# Azure AI Search सेटअप गाइड

यो गाइडले तपाईंलाई Azure पोर्टल प्रयोग गरी Azure AI Search सेटअप गर्न मद्दत गर्नेछ। तलका चरणहरू पालना गरेर तपाईंले Azure AI Search सेवा सिर्जना र कन्फिगर गर्न सक्नुहुन्छ।

## पूर्वशर्तहरू

सुरु गर्नु अघि, सुनिश्चित गर्नुहोस् कि तपाईंलाई तलका वस्तुहरू छन्:

- एउटा Azure सदस्यता। यदि तपाईंको Azure सदस्यता छैन भने, तपाईं [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) मा निःशुल्क खाता सिर्जना गर्न सक्नुहुन्छ।

## चरण 1: Azure Storage Account सिर्जना गर्नुहोस्

1. यो निर्देशन [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) पालन गरेर नयाँ Azure Storage Account सिर्जना गर्नुहोस्।
   **NOTE**: Storage Account को प्रकार Standard General Purpose V2 हुनु आवश्यक छ।

## चरण 2: Azure AI Search सेवा सिर्जना गर्नुहोस्

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) मा साइन इन गर्नुहोस्।
2. बायाँ नेभिगेसन प्यानमा, **Create a resource** मा क्लिक गर्नुहोस्।
3. खोज बाकसमा "Azure AI Search" टाइप गरी परिणाम सूचीबाट **Azure AI Search** छान्नुस्।
4. **Create** बटनमा क्लिक गर्नुहोस्।
5. **Basics** ट्याबमा, तलको जानकारी प्रदान गर्नुहोस्:
   - **Subscription**: तपाईंको Azure सदस्यता चयन गर्नुहोस्।
   - **Resource group**: नयाँ resource group सिर्जना गर्नुहोस् वा कुनै पहिलेको चयन गर्नुहोस्।
   - **Resource name**: तपाईंको खोज सेवा लागि अद्वितीय नाम प्रविष्ट गर्नुहोस्।
   - **Region**: तपाईंका प्रयोगकर्ताहरूको नजिकको क्षेत्र चयन गर्नुहोस्।
   - **Pricing tier**: तपाईंको आवश्यकताअनुसार मूल्य तालिका छनोट गर्नुहोस्। परीक्षणका लागि Free tier बाट सुरु गर्न सक्नुहुन्छ।
6. **Review + create** मा क्लिक गर्नुहोस्।
7. सेटिङहरू समीक्षा गरेर **Create** मा क्लिक गरी खोज सेवा सिर्जना गर्नुहोस्।

## चरण 3: Azure AI Search प्रयोग शुरू गर्नुहोस्

1. एकपटक परिनियोजन पूरा भएपछि, Azure पोर्टलमा तपाईंको खोज सेवामा जानुहोस्।
2. खोज सेवा अवलोकन प्यानमा URL प्रतिलिपि गर्नुहोस्। यो यसरी देखिनु पर्छ `https://<service-name>.search.windows.net`।
3. **(सुझाव गरिएको)** तल देखाएझैँ चरण 4 अनुसार Microsoft Entra ID (RBAC) संग कुञ्जी रहित पहुँच सक्षम गर्नुहोस् — कुनै कुञ्जी आवश्यक छैन। यस गाइडका नमुनाहरू अनुक्रमणिका सिर्जना/अपडेट र कागजातहरू अपलोड गर्छन्, जुन **Search Service Contributor** र **Search Index Data Contributor** भूमिकाहरू (वा कुञ्जी आधारित प्रमाणीकरणको लागि **primary admin key** — प्रश्न कुञ्जी होइन) आवश्यक पर्छ। यदि तपाईं RBAC प्रयोग गर्न सक्नुहुन्न भने मात्र, **Settings > Keys** प्यान खोल्नुहोस् र **primary admin key** प्रतिलिपि गर्नुहोस्।
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) पृष्ठमा दिइएका चरणहरू पालना गरेर अनुक्रमणिका सिर्जना गर्न, डेटा अपलोड गर्न, र खोज प्रदर्शन गर्न सक्नुहुन्छ।

## चरण 4: Azure AI Search उपकरणहरू प्रयोग गर्नुहोस्

Azure AI Search विभिन्न उपकरणहरूसँग एकीकरण हुन्छ जसले तपाईंको खोज क्षमताहरू विस्तार गर्छ। तपाईं Azure CLI, Python SDK, .NET SDK र अन्य उपकरणहरू उन्नत कन्फिगरेसन र अपरेशन्सका लागि प्रयोग गर्न सक्नुहुन्छ।

### Azure CLI प्रयोग गर्दै

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) मा निर्देशनहरू पालना गरेर Azure CLI इन्स्टल गर्नुहोस्।
2. तलको कमाण्ड प्रयोग गरी Azure CLI मा साइन इन गर्नुहोस्:

   ```bash
   az login
   ```
3. **(सुझाव गरिएको) Microsoft Entra ID (RBAC) का साथ कुञ्जी रहित पहुँच सक्षम गर्नुहोस्:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search service show has no "endpoint" field; build the URL from the service name.
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC सक्षम हुँदा तलका Python र .NET SDK नमूनाहरू `DefaultAzureCredential` मार्फत प्रमाणीकरण गर्छन्, जसले स्थानीय विकास अवधिमा तपाईंको `az login` सत्र प्रयोग गर्छ — कुनै प्रशासक कुञ्जी आवश्यक छैन। हेर्नुहोस् [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)।

4. **(वैकल्पिक) कुञ्जी आधारित प्रमाणीकरण** — RBAC प्रयोग गर्न नसकेमा मात्र, प्रशासक कुञ्जी पनि सुरक्षित गर्नुहोस्:

#### Azure AI Search उदाहरणको लागि दुवै endpoint र API कुञ्जी वातावरण चरमा सुरक्षित गर्नुहोस्।

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

### Python SDK प्रयोग गर्दै

1. Azure Cognitive Search क्लाइन्ट लाइब्रेरी र Azure Identity Python को लागि इन्स्टल गर्नुहोस्:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. अनुक्रमणिका सिर्जना गर्न र कागजातहरू अपलोड गर्न तलको Python कोड प्रयोग गर्नुहोस्:

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

### .NET SDK प्रयोग गर्दै

1. अनुक्रमणिका सिर्जना गर्न र कागजातहरू अपलोड गर्न तलको कमाण्ड चलाउनुहोस्:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    तल दिइएको .NET नमूना `DefaultAzureCredential` प्रयोग गर्छ, जसले स्थानीय विकासमा तपाईंको Azure CLI साइन इन `az login` प्रयोग गर्न सक्छ।

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

थप विस्तृत जानकारीको लागि निम्न कागजातहरू हेर्नुहोस्:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

तपाईंले सफलतापूर्वक Azure पोर्टल र सम्बद्ध उपकरणहरू प्रयोग गरी Azure AI Search सेटअप गर्नुभएको छ। अब तपाईं Azure AI Search का थप उन्नत सुविधाहरू र क्षमता अन्वेषण गरी तपाईंको खोज समाधानहरूलाई अझ विकसित बनाउन सक्नुहुन्छ।

थप सहायता लागि, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) भ्रमण गर्नुहोस्।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->