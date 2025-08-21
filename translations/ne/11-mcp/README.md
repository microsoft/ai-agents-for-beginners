<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-08-21T12:15:29+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "ne"
}
-->
# पाठ ११: मोडल कन्टेक्स्ट प्रोटोकल (MCP) एकीकरण

## मोडल कन्टेक्स्ट प्रोटोकल (MCP) को परिचय

मोडल कन्टेक्स्ट प्रोटोकल (MCP) एक अत्याधुनिक फ्रेमवर्क हो जसले AI मोडलहरू र क्लाइन्ट एप्लिकेसनहरू बीचको अन्तरक्रियालाई मानकीकरण गर्न डिजाइन गरिएको छ। MCP ले AI मोडलहरू र तिनीहरूलाई प्रयोग गर्ने एप्लिकेसनहरू बीच पुलको रूपमा काम गर्दछ, जसले मोडलको कार्यान्वयनको प्रकारको परवाह नगरी एकसमान इन्टरफेस प्रदान गर्दछ।

MCP का मुख्य पक्षहरू:

- **मानकीकृत सञ्चार**: MCP ले एप्लिकेसनहरूलाई AI मोडलहरूसँग संवाद गर्न साझा भाषा स्थापना गर्दछ।
- **उन्नत कन्टेक्स्ट व्यवस्थापन**: AI मोडलहरूमा सन्दर्भात्मक जानकारी कुशलतापूर्वक पास गर्न अनुमति दिन्छ।
- **क्रस-प्ल्याटफर्म अनुकूलता**: C#, Java, JavaScript, Python, र TypeScript सहित विभिन्न प्रोग्रामिङ भाषाहरूमा काम गर्दछ।
- **सजिलो एकीकरण**: विकासकर्ताहरूलाई विभिन्न AI मोडलहरूलाई आफ्ना एप्लिकेसनहरूमा सजिलै एकीकृत गर्न सक्षम बनाउँछ।

MCP AI एजेन्ट विकासमा विशेष रूपमा उपयोगी छ किनभने यसले एजेन्टहरूलाई एकीकृत प्रोटोकल मार्फत विभिन्न प्रणालीहरू र डाटा स्रोतहरूसँग अन्तरक्रिया गर्न अनुमति दिन्छ, जसले एजेन्टहरूलाई थप लचिलो र शक्तिशाली बनाउँछ।

## सिकाइ उद्देश्यहरू
- MCP के हो र AI एजेन्ट विकासमा यसको भूमिका बुझ्नुहोस्।
- GitHub एकीकरणको लागि MCP सर्भर सेटअप र कन्फिगर गर्नुहोस्।
- MCP उपकरणहरू प्रयोग गरेर बहु-एजेन्ट प्रणाली निर्माण गर्नुहोस्।
- Azure Cognitive Search को साथ RAG (Retrieval Augmented Generation) कार्यान्वयन गर्नुहोस्।

## पूर्वशर्तहरू
- Python 3.8+
- Node.js 14+
- Azure सदस्यता
- GitHub खाता
- Semantic Kernel को आधारभूत ज्ञान

## सेटअप निर्देशनहरू

1. **पर्यावरण सेटअप**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure सेवाहरू कन्फिगर गर्नुहोस्**
   - Azure Cognitive Search स्रोत सिर्जना गर्नुहोस्।
   - Azure OpenAI सेवा सेटअप गर्नुहोस्।
   - `.env` मा वातावरण चरहरू कन्फिगर गर्नुहोस्।

3. **MCP सर्भर सेटअप**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## परियोजना संरचना

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

## मुख्य घटकहरू

### १. बहु-एजेन्ट प्रणाली
- GitHub एजेन्ट: रिपोजिटरी विश्लेषण
- Hackathon एजेन्ट: परियोजना सिफारिसहरू
- Events एजेन्ट: प्रविधि कार्यक्रम सुझावहरू

### २. Azure एकीकरण
- कार्यक्रम अनुक्रमणको लागि Cognitive Search
- एजेन्ट बुद्धिमत्ताको लागि Azure OpenAI
- RAG ढाँचा कार्यान्वयन

### ३. MCP उपकरणहरू
- GitHub रिपोजिटरी विश्लेषण
- कोड निरीक्षण
- मेटाडाटा निकाल्ने कार्य

## कोड वाकथ्रु

नमूनाले प्रदर्शन गर्दछ:
1. MCP सर्भर एकीकरण
2. बहु-एजेन्ट समन्वय
3. Azure Cognitive Search एकीकरण
4. RAG ढाँचा कार्यान्वयन

मुख्य विशेषताहरू:
- वास्तविक समय GitHub रिपोजिटरी विश्लेषण
- बुद्धिमान परियोजना सिफारिसहरू
- Azure Search प्रयोग गरेर कार्यक्रम मिलान
- Chainlit को साथ स्ट्रिमिङ प्रतिक्रिया

## नमूना चलाउने

विस्तृत सेटअप निर्देशनहरू र थप जानकारीको लागि, [Github MCP Server Example README](./code_samples/github-mcp/README.md) हेर्नुहोस्।

1. MCP सर्भर सुरु गर्नुहोस्:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. एप्लिकेसन सुरु गर्नुहोस्:
   ```bash
   chainlit run app.py -w
   ```

3. एकीकरण परीक्षण गर्नुहोस्:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## समस्या समाधान

सामान्य समस्या र समाधानहरू:
1. MCP जडान समस्या
   - सर्भर चलिरहेको छ भनी पुष्टि गर्नुहोस्।
   - पोर्ट उपलब्धता जाँच गर्नुहोस्।
   - GitHub टोकनहरू पुष्टि गर्नुहोस्।

2. Azure Search समस्या
   - जडान स्ट्रिङहरू मान्य गर्नुहोस्।
   - अनुक्रमणको अस्तित्व जाँच गर्नुहोस्।
   - दस्तावेज अपलोड पुष्टि गर्नुहोस्।

## आगामी कदमहरू
- थप MCP उपकरणहरू अन्वेषण गर्नुहोस्।
- कस्टम एजेन्टहरू कार्यान्वयन गर्नुहोस्।
- RAG क्षमता सुधार गर्नुहोस्।
- थप कार्यक्रम स्रोतहरू थप्नुहोस्।
- **उन्नत**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) मा एजेन्ट-देखि-एजेन्ट सञ्चार उदाहरणहरू हेर्नुहोस्।

## स्रोतहरू
- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Azure Cognitive Search Docs](https://learn.microsoft.com/azure/search/)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी यथासम्भव शुद्धताको प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। यसको मूल भाषामा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।