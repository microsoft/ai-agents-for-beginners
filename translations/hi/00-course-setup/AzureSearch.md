<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "932a1f463f0fcf97090b93b5d0255dff",
  "translation_date": "2025-04-05T19:40:20+00:00",
  "source_file": "00-course-setup\\AzureSearch.md",
  "language_code": "hi"
}
-->
# Azure AI Search सेटअप गाइड

यह गाइड आपको Azure पोर्टल का उपयोग करके Azure AI Search सेटअप करने में मदद करेगा। नीचे दिए गए चरणों का पालन करें और अपने Azure AI Search सेवा को बनाएं और कॉन्फ़िगर करें।

## आवश्यकताएँ

शुरू करने से पहले सुनिश्चित करें कि आपके पास निम्नलिखित हैं:

- एक Azure सब्सक्रिप्शन। यदि आपके पास Azure सब्सक्रिप्शन नहीं है, तो आप [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) पर एक मुफ्त खाता बना सकते हैं।

## चरण 1: Azure AI Search सेवा बनाएं

1. [Azure पोर्टल](https://portal.azure.com/?wt.mc_id=studentamb_258691) में साइन इन करें।
2. बाएँ तरफ नेविगेशन पैन में **Create a resource** पर क्लिक करें।
3. सर्च बॉक्स में "Azure Cognitive Search" टाइप करें और परिणामों की सूची से **Azure Cognitive Search** चुनें।
4. **Create** बटन पर क्लिक करें।
5. **Basics** टैब में निम्न जानकारी प्रदान करें:
   - **Subscription**: अपना Azure सब्सक्रिप्शन चुनें।
   - **Resource group**: एक नया रिसोर्स ग्रुप बनाएं या मौजूदा चुनें।
   - **Resource name**: अपनी सर्च सेवा के लिए एक अनूठा नाम दर्ज करें।
   - **Region**: अपने उपयोगकर्ताओं के सबसे निकट का क्षेत्र चुनें।
   - **Pricing tier**: अपनी आवश्यकताओं के अनुसार एक प्राइसिंग टियर चुनें। परीक्षण के लिए आप Free टियर से शुरू कर सकते हैं।
6. **Review + create** पर क्लिक करें।
7. सेटिंग्स की समीक्षा करें और सर्च सेवा बनाने के लिए **Create** पर क्लिक करें।

## चरण 2: Azure AI Search का उपयोग शुरू करें

1. डिप्लॉयमेंट पूरा होने के बाद, Azure पोर्टल में अपनी सर्च सेवा पर जाएँ।
2. सर्च सेवा ओवरव्यू पेज पर, **Quickstart** बटन पर क्लिक करें।
3. Quickstart गाइड में दिए गए चरणों का पालन करें: एक इंडेक्स बनाएं, डेटा अपलोड करें, और सर्च क्वेरी करें।

### इंडेक्स बनाएं

1. Quickstart गाइड में, **Create an index** पर क्लिक करें।
2. इंडेक्स स्कीमा को परिभाषित करें, जिसमें फील्ड्स और उनके गुण (जैसे, डेटा टाइप, searchable, filterable) शामिल हों।
3. **Create** पर क्लिक करें ताकि इंडेक्स बन सके।

### डेटा अपलोड करें

1. Quickstart गाइड में, **Upload data** पर क्लिक करें।
2. डेटा स्रोत चुनें (जैसे, Azure Blob Storage, Azure SQL Database) और आवश्यक कनेक्शन विवरण प्रदान करें।
3. डेटा स्रोत फील्ड्स को इंडेक्स फील्ड्स से मैप करें।
4. **Submit** पर क्लिक करें ताकि डेटा इंडेक्स में अपलोड हो सके।

### सर्च क्वेरी करें

1. Quickstart गाइड में, **Search explorer** पर क्लिक करें।
2. सर्च बॉक्स में एक सर्च क्वेरी दर्ज करें ताकि सर्च कार्यक्षमता का परीक्षण किया जा सके।
3. सर्च परिणामों की समीक्षा करें और आवश्यकता अनुसार इंडेक्स स्कीमा या डेटा समायोजित करें।

## चरण 3: Azure AI Search टूल्स का उपयोग करें

Azure AI Search विभिन्न टूल्स के साथ इंटीग्रेट होता है ताकि आपकी सर्च क्षमताओं को बेहतर बनाया जा सके। आप Azure CLI, Python SDK और अन्य टूल्स का उपयोग करके उन्नत कॉन्फ़िगरेशन और संचालन कर सकते हैं।

### Azure CLI का उपयोग करना

1. Azure CLI को इंस्टॉल करने के लिए [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) पर दिए गए निर्देशों का पालन करें।
2. Azure CLI में साइन इन करें, इस कमांड का उपयोग करें:
   ```bash
   az login
   ```
3. Azure CLI का उपयोग करके नई सर्च सेवा बनाएं:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI का उपयोग करके एक इंडेक्स बनाएं:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK का उपयोग करना

1. Python के लिए Azure Cognitive Search क्लाइंट लाइब्रेरी इंस्टॉल करें:
   ```bash
   pip install azure-search-documents
   ```
2. निम्न Python कोड का उपयोग करें ताकि एक इंडेक्स बनाया जा सके और डॉक्युमेंट्स अपलोड किए जा सकें:
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

अधिक विस्तृत जानकारी के लिए निम्न दस्तावेज़ देखें:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

आपने सफलतापूर्वक Azure पोर्टल का उपयोग करके Azure AI Search सेटअप कर लिया है और इसे विभिन्न टूल्स के साथ इंटीग्रेट कर लिया है। अब आप Azure AI Search की उन्नत विशेषताओं और क्षमताओं का पता लगा सकते हैं ताकि अपने सर्च समाधान को बेहतर बना सकें।

अधिक सहायता के लिए [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) पर जाएँ।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।