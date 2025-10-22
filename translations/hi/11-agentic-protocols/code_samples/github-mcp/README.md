<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-30T14:51:00+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "hi"
}
-->
# Github MCP Server Example

## विवरण

यह एक डेमो है जो Microsoft Reactor द्वारा आयोजित AI Agents Hackathon के लिए बनाया गया था।

यह टूल उपयोगकर्ता के Github रिपोज़िटरी के आधार पर हैकाथॉन प्रोजेक्ट्स की सिफारिश करने के लिए उपयोग किया जाता है। यह निम्नलिखित तरीके से काम करता है:

1. **Github Agent** - Github MCP Server का उपयोग करके रिपोज़िटरी और उनके बारे में जानकारी प्राप्त करता है।
2. **Hackathon Agent** - Github Agent से प्राप्त डेटा का उपयोग करके उपयोगकर्ता के प्रोजेक्ट्स, उपयोग की गई भाषाओं और AI Agents Hackathon के प्रोजेक्ट ट्रैक्स के आधार पर रचनात्मक हैकाथॉन प्रोजेक्ट आइडियाज तैयार करता है।
3. **Events Agent** - Hackathon Agent की सिफारिशों के आधार पर, Events Agent AI Agent Hackathon सीरीज़ से संबंधित इवेंट्स की सिफारिश करता है।

## कोड चलाना 

### एनवायरनमेंट वेरिएबल्स

यह डेमो Azure Open AI Service, Semantic Kernel, Github MCP Server और Azure AI Search का उपयोग करता है।

सुनिश्चित करें कि इन टूल्स का उपयोग करने के लिए आपके पास सही एनवायरनमेंट वेरिएबल्स सेट हैं:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Chainlit Server चलाना

MCP Server से कनेक्ट करने के लिए, यह डेमो Chainlit को चैट इंटरफेस के रूप में उपयोग करता है।

सर्वर चलाने के लिए, अपने टर्मिनल में निम्नलिखित कमांड का उपयोग करें:

```bash
chainlit run app.py -w
```

यह आपके Chainlit सर्वर को `localhost:8000` पर शुरू कर देगा और साथ ही `event-descriptions.md` सामग्री के साथ आपके Azure AI Search Index को पॉप्युलेट करेगा।

## MCP Server से कनेक्ट करना

Github MCP Server से कनेक्ट करने के लिए, "Type your message here.." चैट बॉक्स के नीचे "plug" आइकन पर क्लिक करें:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.hi.png)

इसके बाद आप "Connect an MCP" पर क्लिक करके Github MCP Server से कनेक्ट करने के लिए कमांड जोड़ सकते हैं:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" को अपने वास्तविक Personal Access Token से बदलें।

कनेक्ट करने के बाद, आपको प्लग आइकन के पास (1) दिखाई देगा, जो पुष्टि करता है कि यह कनेक्ट हो गया है। यदि ऐसा नहीं होता है, तो `chainlit run app.py -w` के साथ Chainlit सर्वर को पुनः शुरू करने का प्रयास करें।

## डेमो का उपयोग करना 

हैकाथॉन प्रोजेक्ट्स की सिफारिश करने के लिए एजेंट वर्कफ़्लो शुरू करने के लिए, आप ऐसा संदेश टाइप कर सकते हैं:

"Github उपयोगकर्ता koreyspace के लिए हैकाथॉन प्रोजेक्ट्स की सिफारिश करें"

Router Agent आपके अनुरोध का विश्लेषण करेगा और यह निर्धारित करेगा कि कौन सा एजेंट (GitHub, Hackathon, और Events) का संयोजन आपके प्रश्न को संभालने के लिए सबसे उपयुक्त है। एजेंट्स मिलकर Github रिपोज़िटरी विश्लेषण, प्रोजेक्ट आइडियेशन और संबंधित टेक इवेंट्स के आधार पर व्यापक सिफारिशें प्रदान करते हैं।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।