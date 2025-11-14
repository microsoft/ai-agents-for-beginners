<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T10:58:13+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "ne"
}
-->
# Github MCP Server Example

## विवरण

यो डेमो माइक्रोसफ्ट रिएक्टरद्वारा आयोजित एआई एजेन्ट्स ह्याकाथनको लागि तयार गरिएको थियो।

यो उपकरण प्रयोगकर्ताको Github रिपोजको आधारमा ह्याकाथन प्रोजेक्टहरू सिफारिस गर्न प्रयोग गरिन्छ। यो निम्न तरिकाले गरिन्छ:

1. **Github Agent** - Github MCP Server प्रयोग गरेर रिपोज र ती रिपोजको जानकारी प्राप्त गर्ने।
2. **Hackathon Agent** - Github Agent बाट प्राप्त डाटाको आधारमा प्रयोगकर्ताले प्रयोग गरेका प्रोजेक्टहरू, भाषाहरू, र एआई एजेन्ट्स ह्याकाथनको प्रोजेक्ट ट्र्याकहरूलाई ध्यानमा राख्दै सिर्जनात्मक ह्याकाथन प्रोजेक्ट आइडिया तयार गर्ने।
3. **Events Agent** - ह्याकाथन एजेन्टको सिफारिसको आधारमा, एआई एजेन्ट ह्याकाथन सिरिजका सम्बन्धित इभेन्टहरू सिफारिस गर्ने।

## कोड चलाउने

### वातावरणीय चरहरू

यो डेमोले Azure Open AI Service, Semantic Kernel, Github MCP Server, र Azure AI Search प्रयोग गर्दछ।

यी उपकरणहरू प्रयोग गर्नको लागि आवश्यक वातावरणीय चरहरू सेट गर्नुहोस्:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit Server चलाउने

MCP Serverसँग जडान गर्न, यो डेमोले Chainlit लाई च्याट इन्टरफेसको रूपमा प्रयोग गर्दछ।

सर्भर चलाउनको लागि, आफ्नो टर्मिनलमा निम्न कमाण्ड प्रयोग गर्नुहोस्:

```bash
chainlit run app.py -w
```

यसले तपाईंको Chainlit सर्भरलाई `localhost:8000` मा सुरु गर्नुका साथै `event-descriptions.md` सामग्रीलाई Azure AI Search Index मा भरिनेछ।

## MCP Serverसँग जडान गर्ने

Github MCP Serverसँग जडान गर्न, "Type your message here.." च्याट बक्सको तल रहेको "plug" आइकन चयन गर्नुहोस्:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.ne.png)

त्यसपछि "Connect an MCP" क्लिक गरेर Github MCP Serverसँग जडान गर्न कमाण्ड थप्न सक्नुहुन्छ:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" लाई आफ्नो वास्तविक Personal Access Token ले प्रतिस्थापन गर्नुहोस्।

जडान गरेपछि, plug आइकनको छेउमा (1) देखिनेछ जसले जडान पुष्टि गर्दछ। यदि देखिएन भने, `chainlit run app.py -w` प्रयोग गरेर Chainlit सर्भर पुनः सुरु गर्नुहोस्।

## डेमो प्रयोग गर्ने

ह्याकाथन प्रोजेक्ट सिफारिस गर्ने एजेन्ट वर्कफ्लो सुरु गर्न, तपाईं यस्तो सन्देश टाइप गर्न सक्नुहुन्छ:

"Github प्रयोगकर्ता koreyspace का लागि ह्याकाथन प्रोजेक्टहरू सिफारिस गर्नुहोस्"

Router Agent ले तपाईंको अनुरोधको विश्लेषण गर्नेछ र कुन एजेन्टहरूको संयोजन (GitHub, Hackathon, र Events) तपाईंको प्रश्नलाई समाधान गर्न उपयुक्त छ भनेर निर्धारण गर्नेछ। एजेन्टहरूले Github रिपोजिटरी विश्लेषण, प्रोजेक्ट आइडिया निर्माण, र सम्बन्धित टेक इभेन्टहरूको आधारमा व्यापक सिफारिसहरू प्रदान गर्न सँगै काम गर्नेछन्।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।