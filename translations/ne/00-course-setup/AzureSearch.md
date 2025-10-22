<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:35:40+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "ne"
}
-->
# Azure AI Search सेटअप गाइड

यो गाइडले तपाईंलाई Azure पोर्टल प्रयोग गरी Azure AI Search सेटअप गर्न मद्दत गर्नेछ। तलका चरणहरू पालना गरेर आफ्नो Azure AI Search सेवा सिर्जना र कन्फिगर गर्नुहोस्।

## पूर्व आवश्यकताहरू

सुरु गर्नु अघि, सुनिश्चित गर्नुहोस् कि तपाईंसँग निम्न कुरा छ:

- Azure सदस्यता। यदि तपाईंसँग Azure सदस्यता छैन भने, तपाईँले [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) मा निःशुल्क खाता बनाउन सक्नुहुन्छ।

## चरण १: Azure AI Search सेवा सिर्जना गर्नुहोस्

1. [Azure पोर्टल](https://portal.azure.com/?wt.mc_id=studentamb_258691) मा साइन इन गर्नुहोस्।
2. बाँया नेभिगेसन प्यानमा, **Create a resource** मा क्लिक गर्नुहोस्।
3. खोज बक्समा "Azure AI Search" टाइप गर्नुहोस् र परिणामहरूको सूचीबाट **Azure AI Search** चयन गर्नुहोस्।
4. **Create** बटनमा क्लिक गर्नुहोस्।
5. **Basics** ट्याबमा, तलका जानकारीहरू प्रदान गर्नुहोस्:
   - **Subscription**: आफ्नो Azure सदस्यता चयन गर्नुहोस्।
   - **Resource group**: नयाँ रिसोर्स समूह सिर्जना गर्नुहोस् वा पहिलेको कुनै एक चयन गर्नुहोस्।
   - **Resource name**: आफ्नो सर्च सेवाको लागि अनौठो नाम प्रविष्ट गर्नुहोस्।
   - **Region**: प्रयोगकर्ताहरूको नजिकको क्षेत्र चयन गर्नुहोस्।
   - **Pricing tier**: आफ्नो आवश्यकताअनुसार मूल्य निर्धारण स्तर चयन गर्नुहोस्। परीक्षणका लागि Free tier बाट सुरु गर्न सक्नुहुन्छ।
6. **Review + create** मा क्लिक गर्नुहोस्।
7. सेटिङहरू समीक्षा गरी **Create** मा क्लिक गरेर सर्च सेवा सिर्जना गर्नुहोस्।

## चरण २: Azure AI Search सुरु गर्नुहोस्

1. डिप्लोयमेन्ट पूरा भएपछि, Azure पोर्टलमा आफ्नो सर्च सेवामा जानुहोस्।
2. सर्च सेवा अवलोकन पृष्ठमा, **Quickstart** बटनमा क्लिक गर्नुहोस्।
3. Quickstart गाइडका चरणहरू पालना गरेर इन्डेक्स सिर्जना गर्नुहोस्, डेटा अपलोड गर्नुहोस्, र सर्च क्वेरी प्रदर्शन गर्नुहोस्।

### इन्डेक्स सिर्जना गर्नुहोस्

1. Quickstart गाइडमा, **Create an index** मा क्लिक गर्नुहोस्।
2. इन्डेक्स स्किमालाई परिभाषित गर्नुहोस् जसमा फिल्डहरू र तिनीहरूको विशेषताहरू (जस्तै, डेटा प्रकार, खोजयोग्य, फिल्टरयोग्य) समावेश छन्।
3. इन्डेक्स सिर्जना गर्न **Create** मा क्लिक गर्नुहोस्।

### डेटा अपलोड गर्नुहोस्

1. Quickstart गाइडमा, **Upload data** मा क्लिक गर्नुहोस्।
2. डेटा स्रोत चयन गर्नुहोस् (जस्तै, Azure Blob Storage, Azure SQL Database) र आवश्यक कनेक्शन विवरणहरू प्रदान गर्नुहोस्।
3. डेटा स्रोतका फिल्डहरूलाई इन्डेक्सका फिल्डहरूसँग म्याप गर्नुहोस्।
4. डेटा इन्डेक्समा अपलोड गर्न **Submit** मा क्लिक गर्नुहोस्।

### सर्च क्वेरी प्रदर्शन गर्नुहोस्

1. Quickstart गाइडमा, **Search explorer** मा क्लिक गर्नुहोस्।
2. सर्च बक्समा सर्च क्वेरी प्रविष्ट गरेर सर्च कार्यक्षमता परीक्षण गर्नुहोस्।
3. सर्च परिणामहरू समीक्षा गर्नुहोस् र आवश्यक परे इन्डेक्स स्किमा वा डेटा समायोजन गर्नुहोस्।

## चरण ३: Azure AI Search उपकरणहरू प्रयोग गर्नुहोस्

Azure AI Search विभिन्न उपकरणहरूसँग एकीकृत हुन्छ जसले तपाईंको सर्च क्षमताहरूलाई बढावा दिन्छ। तपाईं Azure CLI, Python SDK, र अन्य उपकरणहरू प्रयोग गरेर उन्नत कन्फिगरेसन र अपरेसनहरू गर्न सक्नुहुन्छ।

### Azure CLI प्रयोग गर्दै

1. [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) मा दिइएका निर्देशनहरू पालना गरेर Azure CLI इन्स्टल गर्नुहोस्।
2. Azure CLI मा साइन इन गर्न यो कमाण्ड प्रयोग गर्नुहोस्:
   ```bash
   az login
   ```
3. Azure CLI प्रयोग गरेर नयाँ सर्च सेवा सिर्जना गर्नुहोस्:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI प्रयोग गरेर इन्डेक्स सिर्जना गर्नुहोस्:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK प्रयोग गर्दै

1. Python का लागि Azure Cognitive Search क्लाइन्ट लाइब्रेरी इन्स्टल गर्नुहोस्:
   ```bash
   pip install azure-search-documents
   ```
2. तलको Python कोड प्रयोग गरेर इन्डेक्स सिर्जना गर्नुहोस् र कागजातहरू अपलोड गर्नुहोस्:
   ```python
   from azure.core.credentials import AzureKeyCredential
   from azure.search.documents import SearchClient
   from azure.search.documents.indexes import SearchIndexClient
   from azure.search.documents.indexes.models import SearchIndex, SimpleField, edm

   service_endpoint = "https://<service-name>.search.windows.net"
   api_key = "<api-key>"

   index_client = SearchIndexClient(service_endpoint, AzureKeyCredential(api_key))

   fields = [
       SimpleField(name="id", type=edm.String, key=True),
       SimpleField(name="content", type=edm.String, searchable=True),
   ]

   index = SearchIndex(name="sample-index", fields=fields)

   index_client.create_index(index)

   search_client = SearchClient(service_endpoint, "sample-index", AzureKeyCredential(api_key))

   documents = [
       {"id": "1", "content": "Hello world"},
       {"id": "2", "content": "Azure Cognitive Search"}
   ]

   search_client.upload_documents(documents)
   ```

थप विस्तृत जानकारीका लागि तलका कागजातहरू हेर्नुहोस्:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

तपाईंले Azure पोर्टल र एकीकृत उपकरणहरू प्रयोग गरी सफलतापूर्वक Azure AI Search सेटअप गर्नुभयो। अब तपाईं Azure AI Search का थप उन्नत सुविधाहरू र क्षमताहरू अन्वेषण गरेर आफ्नो सर्च समाधानहरूलाई अझ प्रभावकारी बनाउन सक्नुहुन्छ।

थप सहयोगका लागि, [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) भ्रमण गर्नुहोस्।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।