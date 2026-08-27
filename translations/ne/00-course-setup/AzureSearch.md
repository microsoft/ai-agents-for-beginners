# Azure AI Search सेटअप गाइड

यो गाइडले तपाईंलाई Azure पोर्टल प्रयोग गरेर Azure AI Search सेटअप गर्न मद्दत गर्नेछ। तलका चरणहरू पालना गर्दै आफ्नो Azure AI Search सेवा सिर्जना र कन्फिगर गर्नुहोस्।

## आवश्यकताहरू

सुरु गर्नु अघि, निम्न कुरा सुनिश्चित गर्नुहोस्:

- एउटा Azure सदस्यता। यदि तपाईं सँग Azure सदस्यता छैन भने, तपाईं [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) मा निशुल्क खाता बनाउन सक्नुहुन्छ।

## चरण 1: Azure Storage Account सिर्जना गर्नुहोस्

1. यो निर्देशिका पालना गर्नुहोस्, [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal), नयाँ Azure Storage Account सिर्जना गर्न।
   **टिप्पणी**: Storage Account को प्रकार Standard General Purpose V2 हुनुपर्छ सुनिश्चित गर्नुहोस्।

## चरण 2: Azure AI Search सेवा सिर्जना गर्नुहोस्

1. [Azure portal](https://portal.azure.com/?wt.mc_id=studentamb_258691) मा साइन इन गर्नुहोस्।
2. बायाँपट्टि रहेको नेभिगेसन प्यानमा, **Create a resource** मा क्लिक गर्नुहोस्।
3. सर्च बाकसमा "Azure AI Search" टाइप गर्नुहोस् र नतिजाबाट **Azure AI Search** चयन गर्नुहोस्।
4. **Create** बटनमा क्लिक गर्नुहोस्।
5. **Basics** ट्याबमा तलको जानकारी प्रविष्ट गर्नुहोस्:
   - **Subscription**: आफ्नो Azure सदस्यता चयन गर्नुहोस्।
   - **Resource group**: नयाँ रिसोर्स समूह सिर्जना गर्नुहोस् वा अवस्थित समूह चयन गर्नुहोस्।
   - **Resource name**: आफ्नो खोज सेवाका लागि अनौठो नाम प्रविष्ट गर्नुहोस्।
   - **Region**: तपाईंका प्रयोगकर्ताहरूको नजिक रहेको क्षेत्र चयन गर्नुहोस्।
   - **Pricing tier**: तपाईको आवश्यकताजस्तो मूल्य निर्धारण स्तर छान्नुहोस्। परीक्षणका लागि Free tier बाट सुरु गर्न सक्नुहुन्छ।
6. **Review + create** मा क्लिक गर्नुहोस्।
7. सेटिङ्हरू समीक्षा गरी **Create** मा क्लिक गरेर खोज सेवा सिर्जना गर्नुहोस्।

## चरण 3: Azure AI Search सँग सुरु गर्नुहोस्

1. डिप्लोयमेन्ट पूरा भएपछि, Azure पोर्टलमा आफ्नो खोज सेवामा जानुहोस्।
2. खोज सेवा ओभरभ्यू प्यानमा, URL कपी गर्नुहोस्। यसले `https://<service-name>.search.windows.net` जस्तो देखिनुपर्छ।
3. **(सिफारिस गरिन्छ)** Microsoft Entra ID (RBAC) सहितको किलेशून्य पहुँच सक्षम गर्नुहोस् जस्तै तल चरण 4 मा देखाइएको छ — कुनै चाबी चाहिँदैन। यस गाइडका नमुनाहरूले इन्डेक्सहरू सिर्जना/अपडेट गर्छन् र कागजातहरू अपलोड गर्छन्, जसका लागि **Search Service Contributor** र **Search Index Data Contributor** भूमिका आवश्यक पर्दछ (वा, किलाभित्ता प्रमाणीकरणका लागि, **primary admin key** — क्वेरी किलाभन्दा होइन)। यदि तपाईं RBAC प्रयोग गर्न सक्नुहुन्न भने मात्र, **Settings > Keys** प्यान खोल्नुहोस् र **primary admin key** कपी गर्नुहोस्।
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) पृष्ठका चरणहरू पालना गरी इन्डेक्स सिर्जना गर्नुहोस्, डाटा अपलोड गर्नुहोस्, र खोज कार्यान्वयन गर्नुहोस्।

## चरण 4: Azure AI Search उपकरणहरू प्रयोग गर्नुहोस्

Azure AI Search विभिन्न उपकरणहरूसँग एकीकृत हुन्छ जुन तपाईंको खोज क्षमता बढाउँछ। तपाईं Azure CLI, Python SDK, .NET SDK र अन्य उपकरणहरू प्रयोग गरेर उन्नत कन्फिगरेसनहरू र अपरेसनहरू गर्न सक्नुहुन्छ।

### Azure CLI प्रयोग गर्दै

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) मा भएका निर्देशनहरू पालना गरेर Azure CLI इन्स्टल गर्नुहोस्।
2. तलको आदेश प्रयोग गरी Azure CLI मा साइन इन गर्नुहोस्:

   ```bash
   az login
   ```
3. **(सिफारिस गरिन्छ) Microsoft Entra ID (RBAC) सहितको किलेशून्य पहुँच सक्षम गर्नुहोस्:**

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    # az search सेवा देखाउन "endpoint" फिल्ड छैन; सेवा नामबाट URL बनाउनुहोस्।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    ```

    RBAC सक्षम गरेपछि, तलका Python र .NET SDK नमूनाहरूले `DefaultAzureCredential` प्रयोग गरेर प्रमाणीकरण गर्छन्, जसले स्थानीय विकासको क्रममा तपाईंको `az login` सेसन प्रयोग गर्छ — कुनै admin की आवश्यक पर्दैन। हेर्नुहोस् [Connect to Azure AI Search using roles](https://learn.microsoft.com/azure/search/search-security-rbac)।

4. **(वैकल्पिक) किलाभित्ता प्रमाणीकरण** — केवल उहाँहरूका लागि जसले RBAC प्रयोग गर्न सक्दैनन्, admin key पनि भण्डारण गर्नुहोस्:

#### Azure AI Search उदाहरणको लागि endpoint र API key दुवै वातावरण चरमा भण्डारण गर्नुहोस्।

    ```bash
    # zsh/bash
    # az search service show सँग "endpoint" क्षेत्र हुँदैन; सेवा नामबाट URL निर्माण गर्नुहोस्।
    export AZURE_SEARCH_SERVICE_ENDPOINT="https://<service-name>.search.windows.net"
    export AZURE_SEARCH_API_KEY=$(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

    ```powershell
    # PowerShell
    # az search service show सँग "endpoint" क्षेत्र हुँदैन; सेवा नामबाट URL निर्माण गर्नुहोस्।
    $env:AZURE_SEARCH_SERVICE_ENDPOINT = "https://<service-name>.search.windows.net"
    $env:AZURE_SEARCH_API_KEY = $(az search admin-key show -g <resource-group> --service-name <service-name> --query "primaryKey" -o tsv)
    ```

### Python SDK प्रयोग गर्दै

1. Azure Cognitive Search क्लाइन्ट लाइब्रेरी र Azure Identity Python का लागि इन्स्टल गर्नुहोस्:

   ```bash
   pip install azure-search-documents azure-identity
   ```

2. तलको Python कोड प्रयोग गरी इन्डेक्स सिर्जना गर्नुहोस् र कागजातहरू अपलोड गर्नुहोस्:

    ```python
    import os
    from azure.identity import DefaultAzureCredential
    from azure.search.documents import SearchClient
    from azure.search.documents.indexes import SearchIndexClient
    from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

    service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    index_name = "sample-index"

    # कीलेस (सिफारिस गरिएको): तपाईँको `az login` पहिचान Entra ID RBAC मार्फत प्रयोग गर्दछ।
    # "Search Service Contributor" र "Search Index Data Contributor" भूमिकाहरू आवश्यक छ।
    credential = DefaultAzureCredential()
    # फलब्याक (की-आधारित प्रमाणीकरण):
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

1. इन्डेक्स सिर्जना गर्न र कागजातहरू अपलोड गर्न निम्न आदेश चलाउनुहोस्:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

    तलको .NET नमूनाले `DefaultAzureCredential` प्रयोग गर्दछ, जसले स्थानीय विकासको क्रममा `az login` बाट Azure CLI साइन-इन प्रयोग गर्न सक्छ।

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

तपाईंले Azure पोर्टल र एकीकृत उपकरणहरू प्रयोग गरी Azure AI Search सफलतापूर्वक सेटअप गर्नुभएको छ। अब तपाईं Azure AI Search का थप उन्नत सुविधाहरू र क्षमता अन्वेषण गरेर आफ्नो खोज समाधानहरू सुधार गर्न सक्नुहुन्छ।

थप सहयोगका लागि, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) भ्रमण गर्नुहोस्।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->