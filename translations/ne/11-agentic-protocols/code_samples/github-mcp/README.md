# Github MCP सर्भर उदाहरण

## विवरण

यो Microsoft Reactor द्वारा आयोजना गरिएको AI Agents Hackathon का लागि बनाइएको डेमो हो।

उपकरण प्रयोगकर्ताको Github रिपोजिटरीहरूमा आधारित ह्याकाथन परियोजनाहरू सिफारिस गर्न प्रयोग गरिन्छ।
यो यसरी गरिन्छ:

1. **Github Agent** - Github MCP सर्भर प्रयोग गरेर रिपोहरू र ती रिपोहरूको जानकारी प्राप्त गर्न।
2. **Hackathon Agent** - Github Agent बाट ल्याइएको डेटा लिएर प्रयोगकर्ताका परियोजना, प्रयोग गरिएको भाषा र AI Agents ह्याकाथनका परियोजना ट्रयाकहरूमा आधारित सिर्जनात्मक ह्याकाथन परियोजना विचारहरू ल्याउँछ।
3. **Events Agent** - Hackathon एजेन्टको सुझावहरूको आधारमा, Events Agent ले AI Agent Hackathon शृंखलाबाट सान्दर्भिक कार्यक्रमहरू सिफारिस गर्नेछ।
## कोड चलाउने

### वातावरण चरहरू

यो डेमो Microsoft Agent Framework, Azure OpenAI Service, the Github MCP Server र Azure AI Search प्रयोग गर्दछ।

यी उपकरणहरू प्रयोग गर्नका लागि तपाईंसँग उपयुक्त वातावरण चरहरू सेट गरिएको छ भनी सुनिश्चित गर्नुहोस्:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit सर्भर चलाउने

MCP सर्भरसँग जडान गर्न, यो डेमोले च्याट इंटरफेसको रूपमा Chainlit प्रयोग गर्छ। 

सर्भर चलाउनको लागि, आफ्नो टर्मिनलमा निम्न कमान्ड प्रयोग गर्नुहोस्:

```bash
chainlit run app.py -w
```

यसले तपाईंको Chainlit सर्भर `localhost:8000` मा सुरु गर्नुका साथै तपाईंको Azure AI Search Index लाई `event-descriptions.md` सामग्रीले भरिदिनेछ। 

## MCP सर्भरसँग जडान गर्ने

Github MCP सर्भरसँग जडान गर्न, "Type your message here.." च्याट बक्स मुनि रहेको "plug" आइकन चयन गर्नुहोस्:

![MCP Connect](../../../../../translated_images/ne/mcp-chainlit-1.7ed66d648e3cfb28.webp)

त्यसपछि तपाईं "Connect an MCP" मा क्लिक गरेर Github MCP Server सँग जडान गर्ने कमाण्ड थप्न सक्नुहुन्छ:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" लाई तपाईंको वास्तविक Personal Access Token सँग बदल्नुहोस्। 

जडान गरेपछि, यसको पुष्टि गर्न plug आइकनको छेउमा (1) देखिनु पर्नेछ। यदि देखिदैन भने, chainlit सर्भरलाई `chainlit run app.py -w` कमाण्डबाट पुन:स्टार्ट गरेर प्रयास गर्नुहोस्।

## डेमो प्रयोग गर्ने

ह्याकाथन परियोजना सिफारिस गर्ने एजेन्ट कार्यप्रवाह सुरु गर्नका लागि, तपाईं यस्तो सन्देश टाइप गर्न सक्नुहुन्छ: 

"Recommend hackathon projects for the Github user koreyspace"

The Router Agent ले तपाईंको अनुरोध विश्लेषण गर्नेछ र कुन एजेन्टहरूको संयोजन (GitHub, Hackathon, and Events) तपाईंको प्रश्न ह्यान्डल गर्न उपयुक्त हुन्छ निर्णय गर्नेछ। एजेन्टहरूले GitHub रिपोजिटरी विश्लेषण, परियोजना विचार सिर्जना, र सान्दर्भिक प्रविधि कार्यक्रमहरूमा आधारित व्यापक सिफारिसहरू प्रदान गर्न सँगै काम गर्छन्।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
यो कागजात AI अनुवाद सेवा Co-op Translator (https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मौलिक कागजातलाई यसको मूल भाषामा नै अधिकृत स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->