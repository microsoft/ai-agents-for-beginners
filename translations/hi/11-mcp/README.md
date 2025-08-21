<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:11:32+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "hi"
}
-->
# पाठ 11: मॉडल कॉन्टेक्स्ट प्रोटोकॉल (MCP) इंटीग्रेशन

## मॉडल कॉन्टेक्स्ट प्रोटोकॉल (MCP) का परिचय

मॉडल कॉन्टेक्स्ट प्रोटोकॉल (MCP) एक अत्याधुनिक फ्रेमवर्क है जिसे AI मॉडल और क्लाइंट एप्लिकेशन के बीच इंटरैक्शन को मानकीकृत करने के लिए डिज़ाइन किया गया है। MCP AI मॉडल और उन एप्लिकेशन के बीच पुल का काम करता है जो इनका उपयोग करते हैं, और यह एक समान इंटरफ़ेस प्रदान करता है, चाहे मॉडल का कार्यान्वयन कैसा भी हो।

MCP की मुख्य विशेषताएँ:

- **मानकीकृत संचार**: MCP एप्लिकेशन और AI मॉडल के बीच संवाद के लिए एक सामान्य भाषा स्थापित करता है।
- **बेहतर कॉन्टेक्स्ट प्रबंधन**: AI मॉडल को संदर्भित जानकारी को कुशलतापूर्वक पास करने की अनुमति देता है।
- **क्रॉस-प्लेटफ़ॉर्म संगतता**: C#, Java, JavaScript, Python, और TypeScript सहित विभिन्न प्रोग्रामिंग भाषाओं में काम करता है।
- **सहज इंटीग्रेशन**: डेवलपर्स को अपने एप्लिकेशन में विभिन्न AI मॉडल को आसानी से एकीकृत करने में सक्षम बनाता है।

MCP AI एजेंट विकास में विशेष रूप से उपयोगी है क्योंकि यह एजेंटों को एकीकृत प्रोटोकॉल के माध्यम से विभिन्न सिस्टम और डेटा स्रोतों के साथ इंटरैक्ट करने की अनुमति देता है, जिससे वे अधिक लचीले और शक्तिशाली बनते हैं।

## सीखने के उद्देश्य
- MCP क्या है और AI एजेंट विकास में इसकी भूमिका को समझें।
- GitHub इंटीग्रेशन के लिए MCP सर्वर सेटअप और कॉन्फ़िगर करें।
- MCP टूल्स का उपयोग करके एक मल्टी-एजेंट सिस्टम बनाएं।
- Azure Cognitive Search के साथ RAG (Retrieval Augmented Generation) को लागू करें।

## आवश्यकताएँ
- Python 3.8+
- Node.js 14+
- Azure सब्सक्रिप्शन
- GitHub अकाउंट
- Semantic Kernel की बुनियादी समझ

## सेटअप निर्देश

1. **पर्यावरण सेटअप**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure सेवाओं को कॉन्फ़िगर करें**
   - Azure Cognitive Search संसाधन बनाएं।
   - Azure OpenAI सेवा सेटअप करें।
   - `.env` में पर्यावरण वेरिएबल्स कॉन्फ़िगर करें।

3. **MCP सर्वर सेटअप**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## प्रोजेक्ट संरचना

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## मुख्य घटक

### 1. मल्टी-एजेंट सिस्टम
- GitHub एजेंट: रिपॉजिटरी विश्लेषण
- हैकाथॉन एजेंट: प्रोजेक्ट सिफारिशें
- इवेंट्स एजेंट: टेक इवेंट सुझाव

### 2. Azure इंटीग्रेशन
- इवेंट इंडेक्सिंग के लिए Cognitive Search
- एजेंट इंटेलिजेंस के लिए Azure OpenAI
- RAG पैटर्न का कार्यान्वयन

### 3. MCP टूल्स
- GitHub रिपॉजिटरी विश्लेषण
- कोड निरीक्षण
- मेटाडेटा एक्सट्रैक्शन

## कोड वॉकथ्रू

सैंपल में निम्नलिखित प्रदर्शित किया गया है:
1. MCP सर्वर इंटीग्रेशन
2. मल्टी-एजेंट ऑर्केस्ट्रेशन
3. Azure Cognitive Search इंटीग्रेशन
4. RAG पैटर्न का कार्यान्वयन

मुख्य विशेषताएँ:
- रियल-टाइम GitHub रिपॉजिटरी विश्लेषण
- बुद्धिमान प्रोजेक्ट सिफारिशें
- Azure Search का उपयोग करके इवेंट मिलान
- Chainlit के साथ स्ट्रीमिंग प्रतिक्रियाएँ

## सैंपल चलाना

विस्तृत सेटअप निर्देश और अधिक जानकारी के लिए [Github MCP Server Example README](./code_samples/github-mcp/README.md) देखें।

1. MCP सर्वर शुरू करें:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. एप्लिकेशन लॉन्च करें:
   ```bash
   chainlit run app.py -w
   ```

3. इंटीग्रेशन का परीक्षण करें:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## समस्या निवारण

सामान्य समस्याएँ और समाधान:
1. MCP कनेक्शन समस्याएँ
   - सुनिश्चित करें कि सर्वर चल रहा है।
   - पोर्ट उपलब्धता की जाँच करें।
   - GitHub टोकन की पुष्टि करें।

2. Azure Search समस्याएँ
   - कनेक्शन स्ट्रिंग्स की वैधता की जाँच करें।
   - इंडेक्स की उपस्थिति की पुष्टि करें।
   - दस्तावेज़ अपलोड सत्यापित करें।

## अगले कदम
- अतिरिक्त MCP टूल्स का अन्वेषण करें।
- कस्टम एजेंट लागू करें।
- RAG क्षमताओं को बढ़ाएँ।
- अधिक इवेंट स्रोत जोड़ें।
- **उन्नत**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) में एजेंट-टू-एजेंट संचार उदाहरण देखें।

## संसाधन
- [MCP के लिए शुरुआती गाइड](https://aka.ms/mcp-for-beginners)  
- [MCP दस्तावेज़](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search दस्तावेज़](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel गाइड्स](https://learn.microsoft.com/semantic-kernel/)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में लिखा गया दस्तावेज़ ही आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।