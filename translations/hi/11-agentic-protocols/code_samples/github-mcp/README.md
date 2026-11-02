# Github MCP Server उदाहरण

## विवरण

यह Microsoft Reactor के माध्यम से होस्ट किए गए AI Agents Hackathon के लिए बनाया गया एक डेमो था।

यह उपकरण उपयोगकर्ता के Github रिपॉज़ के आधार पर हैकाथॉन परियोजनाओं की सिफारिश करने के लिए उपयोग किए जाते हैं।
यह इस प्रकार किया जाता है:

1. **Github Agent** - Github MCP Server का उपयोग करके रिपॉज़ और उन रिपॉज़ के बारे में जानकारी प्राप्त करना।
2. **Hackathon Agent** - Github Agent से डेटा लेकर उपयोगकर्ता द्वारा उपयोग किए गए प्रोजेक्ट्स, भाषाओं और AI Agents हैकाथॉन के प्रोजेक्ट ट्रैक के आधार पर रचनात्मक हैकाथॉन परियोजना विचार प्रस्तुत करता है।
3. **Events Agent** - हैकाथॉन एजेंट के सुझाव के आधार पर, इवेंट्स एजेंट AI Agent Hackathon सीरीज़ के प्रासंगिक इवेंट्स की सिफारिश करेगा।

## कोड चलाना 

### पर्यावरण वेरिएबल

यह डेमो Microsoft Agent Framework, Azure OpenAI Service, the Github MCP Server और Azure AI Search का उपयोग करता है।

इन टूल्स का उपयोग करने के लिए यह सुनिश्चित करें कि आपके पास उचित पर्यावरण वेरिएबल सेट हैं:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit सर्वर चलाना

MCP सर्वर से कनेक्ट करने के लिए, यह डेमो Chainlit को एक चैट इंटरफ़ेस के रूप में उपयोग करता है। 

सर्वर चलाने के लिए, अपने टर्मिनल में निम्न कमांड का उपयोग करें:

```bash
chainlit run app.py -w
```

यह आपके Chainlit सर्वर को `localhost:8000` पर शुरू कर देगा और साथ ही `event-descriptions.md` सामग्री के साथ आपके Azure AI Search Index को भी भर देगा। 

## MCP सर्वर से कनेक्ट करना

Github MCP Server से कनेक्ट करने के लिए, "यहाँ अपना संदेश टाइप करें.." चैट बॉक्स के नीचे "प्लग" आइकन का चयन करें:

![MCP कनेक्ट](../../../../../translated_images/hi/mcp-chainlit-1.7ed66d648e3cfb28.webp)

वहाँ से आप "एक MCP कनेक्ट करें" पर क्लिक करके Github MCP Server से कनेक्ट करने का कमांड जोड़ सकते हैं:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Replace "[YOUR PERSONAL ACCESS TOKEN]" with your actual Personal Access Token. 

कनेक्ट करने के बाद, पुष्टि के लिए प्लग आइकन के पास आपको (1) दिखाई देना चाहिए। अगर नहीं, तो chainlit सर्वर को `chainlit run app.py -w` के साथ पुनः आरंभ करने का प्रयास करें।

## डेमो का उपयोग 

हैकाथॉन परियोजनाओं की सिफारिश करने वाले एजेंट वर्कफ़्लो को शुरू करने के लिए, आप ऐसा संदेश टाइप कर सकते हैं:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent आपके अनुरोध का विश्लेषण करेगा और निर्धारित करेगा कि किन एजेंटों (GitHub, Hackathon, और Events) का संयोजन आपके प्रश्न को संभालने के लिए सबसे उपयुक्त है। एजेंट मिलकर GitHub रिपॉज़िटरी विश्लेषण, परियोजना विचार, और प्रासंगिक तकनीकी इवेंट्स के आधार पर व्यापक सिफारिशें प्रदान करते हैं।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम ज़िम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->