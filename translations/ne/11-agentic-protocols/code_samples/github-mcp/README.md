# Github MCP Server उदाहरण

## विवरण

यो Microsoft Reactor मार्फत आयोजित AI Agents Hackathon का लागि सिर्जना गरिएको डेमो हो।

यो उपकरण प्रयोगकर्ताको Github रेपोहरूलाई आधारित गरेर ह्याकाथन परियोजनाहरू सिफारिस गर्न प्रयोग हुन्छ।
यसरी गरिन्छ:

1. **Github Agent** - Github MCP Server प्रयोग गरेर रेपोहरू र ती रेपोहरूको जानकारी प्राप्त गर्ने।
2. **Hackathon Agent** - Github Agent बाट प्राप्त डाटालाई लिएर प्रयोगकर्ताका प्रोजेक्टहरू, प्रयोग भएका भाषाहरू र AI Agents hackathon का प्रोजेक्ट ट्र्याकहरूका आधारमा रचनात्मक ह्याकाथन परियोजना विचारहरू निकाल्ने।
3. **Events Agent** - Hackathon agent को सुझाव अनुसार, Events Agent ले AI Agent Hackathon सिरिजका सान्दर्भिक घटनाहरू सिफारिस गर्ने।
## Running the code 

### Environment Variables

यो डेमो Microsoft Agent Framework, Azure OpenAI Service, Github MCP Server र Azure AI Search प्रयोग गर्दछ।

यी उपकरणहरू प्रयोग गर्नका लागि सुनिश्चित गर्नुहोस् कि आवश्यक वातावरण भेरिएबलहरू सेट भएका छन्:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Running the Chainlit Server

MCP सर्भरमा जडान गर्न यो डेमोले Chainlit लाई च्याट इन्टरफेसको रूपमा प्रयोग गर्छ। 

सर्भर चलाउन, तलको आदेश तपाईंको टर्मिनलमा प्रयोग गर्नुहोस्:

```bash
chainlit run app.py -w
```

यसले तपाईंको Chainlit सर्भर `localhost:8000` मा सुरु गर्नुका साथै `event-descriptions.md` सामग्रीको साथ तपाईंको Azure AI Search Index मा डेटा भर्नु पर्छ। 

## Connecting to the MCP Server

Github MCP Server मा जडान गर्न, "Type your message here.." च्याट बाक्सको मुनि रहेको "plug" आइकन छान्नुहोस्:

![MCP जडान](../../../../../translated_images/ne/mcp-chainlit-1.7ed66d648e3cfb28.webp)

त्यहाँबाट तपाईं "Connect an MCP" मा क्लिक गरेर Github MCP Server सँग जडान गर्न कमाण्ड थप गर्न सक्नुहुनेछ:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" लाई तपाईंको वास्तविक Personal Access Token सँग प्रतिस्थापन गर्नुहोस्। 

जडान भएपछि, plug आइकनको छेउमा (1) देखिनु पर्छ जसले जडान पुष्टि गर्छ। यदि देखिदैन भने, `chainlit run app.py -w` संग chainlit सर्भर पुन: सुरु गर्न प्रयास गर्नुहोस्।

## Using the Demo 

ह्याकाथन परियोजनाहरू सिफारिस गर्ने एजेन्ट वर्कफ्लो सुरु गर्न, तपाईंले यस्ता सन्देश टाइप गर्न सक्नुहुन्छ: 

"Recommend hackathon projects for the Github user koreyspace"

Router Agent ले तपाईंको अनुरोध विश्लेषण गरी कुन संयोजनका एजेन्टहरू (GitHub, Hackathon, र Events) तपाईंको सोधलाई ह्यान्डल गर्न उपयुक्त छन् निर्धारण गर्नेछ। यी एजेन्टहरूले GitHub repository विश्लेषण, परियोजना विचार र सान्दर्भिक टेक घटनाहरूका आधारमा व्यापक सिफारिसहरू प्रदान गर्न मिलेर काम गर्छन्।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौँ, तथापि कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि पेशेवर मानव अनुवादको सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलत बुझाइ वा दुभ्रम्य व्याख्याहरूको लागि हामी जिम्मेवार हुनेछैनौँ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->