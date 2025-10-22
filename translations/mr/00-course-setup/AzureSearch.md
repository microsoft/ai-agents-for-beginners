<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f0ce2d470f3efad6f8c7df376f416a4b",
  "translation_date": "2025-07-12T07:35:28+00:00",
  "source_file": "00-course-setup/AzureSearch.md",
  "language_code": "mr"
}
-->
# Azure AI Search सेटअप मार्गदर्शक

हा मार्गदर्शक तुम्हाला Azure पोर्टल वापरून Azure AI Search सेटअप करण्यात मदत करेल. तुमचा Azure AI Search सेवा तयार करण्यासाठी आणि कॉन्फिगर करण्यासाठी खालील चरणांचे पालन करा.

## पूर्वअट

सुरू करण्यापूर्वी, खालील गोष्टी तुमच्याकडे असणे आवश्यक आहे:

- एक Azure सदस्यता. जर तुमच्याकडे Azure सदस्यता नसेल, तर तुम्ही [Azure Free Account](https://azure.microsoft.com/free/?wt.mc_id=studentamb_258691) येथे मोफत खाते तयार करू शकता.

## चरण 1: Azure AI Search सेवा तयार करा

1. [Azure पोर्टल](https://portal.azure.com/?wt.mc_id=studentamb_258691) मध्ये साइन इन करा.
2. डाव्या बाजूच्या नेव्हिगेशन पॅनमध्ये, **Create a resource** वर क्लिक करा.
3. शोध बॉक्समध्ये "Azure AI Search" टाइप करा आणि निकालांमधून **Azure AI Search** निवडा.
4. **Create** बटणावर क्लिक करा.
5. **Basics** टॅबमध्ये खालील माहिती भरा:
   - **Subscription**: तुमची Azure सदस्यता निवडा.
   - **Resource group**: नवीन रिसोर्स ग्रुप तयार करा किंवा आधीचा एक निवडा.
   - **Resource name**: तुमच्या सर्च सेवेचा एक अनोखा नाव द्या.
   - **Region**: तुमच्या वापरकर्त्यांजवळील सर्वात जवळचा प्रदेश निवडा.
   - **Pricing tier**: तुमच्या गरजेनुसार योग्य किंमत स्तर निवडा. चाचणीसाठी तुम्ही Free tier पासून सुरू करू शकता.
6. **Review + create** वर क्लिक करा.
7. सेटिंग्ज तपासा आणि सर्च सेवा तयार करण्यासाठी **Create** वर क्लिक करा.

## चरण 2: Azure AI Search वापर सुरू करा

1. डिप्लॉयमेंट पूर्ण झाल्यानंतर, Azure पोर्टलमध्ये तुमच्या सर्च सेवेकडे जा.
2. सर्च सेवा ओव्हरव्ह्यू पृष्ठावर, **Quickstart** बटणावर क्लिक करा.
3. Quickstart मार्गदर्शकातील चरणांचे पालन करा, ज्यात इंडेक्स तयार करणे, डेटा अपलोड करणे आणि सर्च क्वेरी करणे यांचा समावेश आहे.

### इंडेक्स तयार करा

1. Quickstart मार्गदर्शकात, **Create an index** वर क्लिक करा.
2. इंडेक्स स्कीमा परिभाषित करा, ज्यात फील्ड्स आणि त्यांचे गुणधर्म (उदा. डेटा प्रकार, शोधण्यायोग्य, फिल्टर करण्यायोग्य) नमूद करा.
3. इंडेक्स तयार करण्यासाठी **Create** वर क्लिक करा.

### डेटा अपलोड करा

1. Quickstart मार्गदर्शकात, **Upload data** वर क्लिक करा.
2. डेटा स्रोत निवडा (उदा. Azure Blob Storage, Azure SQL Database) आणि आवश्यक कनेक्शन तपशील द्या.
3. डेटा स्रोत फील्ड्सना इंडेक्स फील्ड्सशी मॅप करा.
4. डेटा इंडेक्समध्ये अपलोड करण्यासाठी **Submit** वर क्लिक करा.

### सर्च क्वेरी करा

1. Quickstart मार्गदर्शकात, **Search explorer** वर क्लिक करा.
2. सर्च बॉक्समध्ये सर्च क्वेरी टाका आणि सर्च कार्यक्षमता तपासा.
3. सर्च निकाल तपासा आणि आवश्यकतेनुसार इंडेक्स स्कीमा किंवा डेटा समायोजित करा.

## चरण 3: Azure AI Search टूल्स वापरा

Azure AI Search विविध टूल्ससह एकत्रित होते जे तुमच्या सर्च क्षमतांना वाढवतात. तुम्ही Azure CLI, Python SDK आणि इतर टूल्स वापरून प्रगत कॉन्फिगरेशन आणि ऑपरेशन्स करू शकता.

### Azure CLI वापरणे

1. [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?wt.mc_id=studentamb_258691) येथे दिलेल्या सूचनांचे पालन करून Azure CLI इन्स्टॉल करा.
2. खालील कमांड वापरून Azure CLI मध्ये साइन इन करा:
   ```bash
   az login
   ```
3. Azure CLI वापरून नवीन सर्च सेवा तयार करा:
   ```bash
   az search service create --resource-group <resource-group> --name <service-name> --sku Free
   ```
4. Azure CLI वापरून इंडेक्स तयार करा:
   ```bash
   az search index create --service-name <service-name> --name <index-name> --fields "field1:type, field2:type"
   ```

### Python SDK वापरणे

1. Python साठी Azure Cognitive Search क्लायंट लायब्ररी इन्स्टॉल करा:
   ```bash
   pip install azure-search-documents
   ```
2. खालील Python कोड वापरून इंडेक्स तयार करा आणि दस्तऐवज अपलोड करा:
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

अधिक सविस्तर माहितीसाठी खालील दस्तऐवज पहा:

- [Create an Azure Cognitive Search service](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal?wt.mc_id=studentamb_258691)
- [Get started with Azure Cognitive Search](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal?wt.mc_id=studentamb_258691)
- [Azure AI Search Tools](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=code-examples?wt.mc_id=studentamb_258691)

## निष्कर्ष

तुम्ही Azure पोर्टल आणि एकत्रित टूल्स वापरून यशस्वीपणे Azure AI Search सेटअप केले आहे. आता तुम्ही Azure AI Search चे अधिक प्रगत वैशिष्ट्ये आणि क्षमता शोधू शकता आणि तुमच्या सर्च सोल्यूशन्सना सुधारू शकता.

अधिक मदतीसाठी, [Azure Cognitive Search documentation](https://learn.microsoft.com/en-us/azure/search/?wt.mc_id=studentamb_258691) भेट द्या.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.