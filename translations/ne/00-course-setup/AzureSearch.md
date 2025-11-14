<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "11e38db0898a788612b917e329dcdb5b",
  "translation_date": "2025-11-07T08:32:38+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ne"
}
-->
# Azure AI Search सेटअप गाइड

यो गाइडले तपाईंलाई Azure पोर्टल प्रयोग गरेर Azure AI Search सेटअप गर्न मद्दत गर्नेछ। Azure AI Search सेवा सिर्जना र कन्फिगर गर्न तलका चरणहरू पालना गर्नुहोस्।

## आवश्यकताहरू

सुरु गर्नु अघि, सुनिश्चित गर्नुहोस् कि तपाईंसँग निम्न छन्:

- Azure सदस्यता। यदि तपाईंसँग Azure सदस्यता छैन भने, तपाईं [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) मा निःशुल्क खाता सिर्जना गर्न सक्नुहुन्छ।

## चरण १: Azure Storage Account सिर्जना गर्नुहोस्

1. नयाँ Azure Storage Account सिर्जना गर्नका लागि [Create an Azure storage account](https://learn.microsoft.com/azure/storage/common/storage-account-create?tabs=azure-portal) निर्देशन पालना गर्नुहोस्।
   **NOTE**: सुनिश्चित गर्नुहोस् कि Storage Account को प्रकार Standard General Purpose V2 हो।

## चरण २: Azure AI Search सेवा सिर्जना गर्नुहोस्

1. [Azure पोर्टल](https://portal.azure.com/?wt.mc_id=studentamb_258691) मा साइन इन गर्नुहोस्।
2. बाँया तर्फको नेभिगेसन प्यानमा, **Create a resource** मा क्लिक गर्नुहोस्।
3. खोज बाकसमा "Azure AI Search" टाइप गर्नुहोस् र परिणामहरूको सूचीबाट **Azure AI Search** चयन गर्नुहोस्।
4. **Create** बटनमा क्लिक गर्नुहोस्।
5. **Basics** ट्याबमा निम्न जानकारी प्रदान गर्नुहोस्:
   - **Subscription**: आफ्नो Azure सदस्यता चयन गर्नुहोस्।
   - **Resource group**: नयाँ स्रोत समूह सिर्जना गर्नुहोस् वा पहिलेको चयन गर्नुहोस्।
   - **Resource name**: आफ्नो सर्च सेवाको लागि एक अद्वितीय नाम प्रविष्ट गर्नुहोस्।
   - **Region**: तपाईंको प्रयोगकर्ताहरू नजिकको क्षेत्र चयन गर्नुहोस्।
   - **Pricing tier**: तपाईंको आवश्यकताहरू अनुसार मूल्य निर्धारण स्तर चयन गर्नुहोस्। परीक्षणको लागि तपाईं Free tier बाट सुरु गर्न सक्नुहुन्छ।
6. **Review + create** मा क्लिक गर्नुहोस्।
7. सेटिङहरू समीक्षा गर्नुहोस् र सर्च सेवा सिर्जना गर्न **Create** मा क्लिक गर्नुहोस्।

## चरण ३: Azure AI Search सुरु गर्नुहोस्

1. तैनाती पूरा भएपछि, Azure पोर्टलमा आफ्नो सर्च सेवामा जानुहोस्।
2. सर्च सेवा ओभरभ्यू प्यानमा, URL प्रतिलिपि गर्नुहोस्। यो `https://<service-name>.search.windows.net` जस्तो देखिनु पर्छ।
3. Settings > Keys प्यानमा, query key प्रतिलिपि गर्नुहोस्।
4. [Quickstart guide](https://learn.microsoft.com/azure/search/search-get-started-portal?pivots=import-data-new) पृष्ठमा चरणहरू पालना गरेर एक इन्डेक्स सिर्जना गर्नुहोस्, डेटा अपलोड गर्नुहोस्, र सर्च क्वेरी प्रदर्शन गर्नुहोस्।

## चरण ४: Azure AI Search उपकरणहरू प्रयोग गर्नुहोस्

Azure AI Search विभिन्न उपकरणहरूसँग एकीकृत हुन्छ जसले तपाईंको सर्च क्षमता सुधार गर्दछ। तपाईं Azure CLI, Python SDK, .NET SDK र अन्य उपकरणहरू प्रयोग गरेर उन्नत कन्फिगरेसन र अपरेसन गर्न सक्नुहुन्छ।

### Azure CLI प्रयोग गर्दै

1. [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) निर्देशन पालना गरेर Azure CLI स्थापना गर्नुहोस्।
2. निम्न कमाण्ड प्रयोग गरेर Azure CLI मा साइन इन गर्नुहोस्:

   ```bash
   az login
   ```

3. Azure AI Search इन्स्टेन्सको लागि दुवै endpoint र API key वातावरण चरमा भण्डारण गर्नुहोस्।

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

### Python SDK प्रयोग गर्दै

1. Python को लागि Azure Cognitive Search क्लाइन्ट लाइब्रेरी स्थापना गर्नुहोस्:

   ```bash
   pip install azure-search-documents
   ```

2. निम्न Python कोड प्रयोग गरेर एक इन्डेक्स सिर्जना गर्नुहोस् र कागजातहरू अपलोड गर्नुहोस्:

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

### .NET SDK प्रयोग गर्दै

1. निम्न कमाण्ड चलाएर एक इन्डेक्स सिर्जना गर्नुहोस् र कागजातहरू अपलोड गर्नुहोस्:

    ```bash
    dotnet run ./AzureSearch.cs
    ```

2. यहाँ `AzureSearch.cs` को .NET कोड छ:

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

थप विस्तृत जानकारीको लागि निम्न दस्तावेजहरू हेर्नुहोस्:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

तपाईंले Azure पोर्टल प्रयोग गरेर Azure AI Search सफलतापूर्वक सेटअप गर्नुभएको छ र उपकरणहरू एकीकृत गर्नुभएको छ। अब तपाईं Azure AI Search को थप उन्नत सुविधाहरू र क्षमता अन्वेषण गर्न सक्नुहुन्छ जसले तपाईंको सर्च समाधानलाई सुधार गर्दछ।

थप सहयोगको लागि, [Azure Cognitive Search documentation](https://learn.microsoft.com/azure/search/?wt.mc_id=studentamb_258691) भ्रमण गर्नुहोस्।

---

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुनेछैनौं।