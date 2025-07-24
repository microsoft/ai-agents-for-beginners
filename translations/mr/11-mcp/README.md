<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T08:05:39+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "mr"
}
-->
# धडा ११: मॉडेल संदर्भ प्रोटोकॉल (MCP) एकत्रीकरण

## मॉडेल संदर्भ प्रोटोकॉल (MCP) ची ओळख

मॉडेल संदर्भ प्रोटोकॉल (MCP) हा एक अत्याधुनिक फ्रेमवर्क आहे, जो AI मॉडेल्स आणि क्लायंट अ‍ॅप्लिकेशन्समधील संवादांचे मानकीकरण करण्यासाठी डिझाइन केला गेला आहे. MCP AI मॉडेल्स आणि त्यांचा वापर करणाऱ्या अ‍ॅप्लिकेशन्समधील पूल म्हणून काम करतो, ज्यामुळे अंतर्गत मॉडेल अंमलबजावणी कशीही असली तरी एकसंध इंटरफेस प्रदान होतो.

MCP चे मुख्य पैलू:

- **मानकीकृत संवाद**: MCP अ‍ॅप्लिकेशन्सना AI मॉडेल्ससोबत संवाद साधण्यासाठी एक सामान्य भाषा प्रदान करतो  
- **वाढीव संदर्भ व्यवस्थापन**: AI मॉडेल्सकडे संदर्भात्मक माहिती कार्यक्षमतेने पाठविण्याची परवानगी देते  
- **क्रॉस-प्लॅटफॉर्म सुसंगतता**: C#, Java, JavaScript, Python, आणि TypeScript यांसारख्या विविध प्रोग्रामिंग भाषांमध्ये कार्य करते  
- **सुलभ एकत्रीकरण**: विकसकांना त्यांच्या अ‍ॅप्लिकेशन्समध्ये विविध AI मॉडेल्स सहजपणे समाविष्ट करण्यास सक्षम करते  

MCP AI एजंट विकासामध्ये विशेषतः उपयुक्त आहे, कारण तो एजंट्सना एकसंध प्रोटोकॉलद्वारे विविध प्रणाली आणि डेटा स्रोतांसोबत संवाद साधण्याची परवानगी देतो, ज्यामुळे एजंट्स अधिक लवचिक आणि शक्तिशाली बनतात.

## शिकण्याची उद्दिष्टे
- MCP म्हणजे काय आणि AI एजंट विकासामध्ये त्याची भूमिका समजून घेणे  
- GitHub एकत्रीकरणासाठी MCP सर्व्हर सेट अप आणि कॉन्फिगर करणे  
- MCP साधनांचा वापर करून मल्टी-एजंट प्रणाली तयार करणे  
- Azure Cognitive Search सह RAG (Retrieval Augmented Generation) अंमलात आणणे  

## पूर्वअट
- Python 3.8+  
- Node.js 14+  
- Azure सदस्यता  
- GitHub खाते  
- Semantic Kernel चे मूलभूत ज्ञान  

## सेटअप सूचना

1. **पर्यावरण सेटअप**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Azure सेवा कॉन्फिगर करा**  
   - Azure Cognitive Search संसाधन तयार करा  
   - Azure OpenAI सेवा सेट अप करा  
   - `.env` मध्ये पर्यावरणीय चल (environment variables) कॉन्फिगर करा  

3. **MCP सर्व्हर सेटअप**  
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## प्रकल्प संरचना

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

### १. मल्टी-एजंट प्रणाली
- GitHub एजंट: रेपॉजिटरी विश्लेषण  
- हॅकाथॉन एजंट: प्रकल्प शिफारसी  
- इव्हेंट्स एजंट: तांत्रिक कार्यक्रमांच्या सूचना  

### २. Azure एकत्रीकरण
- इव्हेंट इंडेक्सिंगसाठी Cognitive Search  
- एजंट इंटेलिजन्ससाठी Azure OpenAI  
- RAG पॅटर्न अंमलबजावणी  

### ३. MCP साधने
- GitHub रेपॉजिटरी विश्लेषण  
- कोड तपासणी  
- मेटाडेटा काढणे  

## कोड वॉकथ्रू

उदाहरण दाखवते:
1. MCP सर्व्हर एकत्रीकरण  
2. मल्टी-एजंट ऑर्केस्ट्रेशन  
3. Azure Cognitive Search एकत्रीकरण  
4. RAG पॅटर्न अंमलबजावणी  

मुख्य वैशिष्ट्ये:
- GitHub रेपॉजिटरीचे रिअल-टाइम विश्लेषण  
- बुद्धिमान प्रकल्प शिफारसी  
- Azure Search चा वापर करून इव्हेंट जुळवणी  
- Chainlit सह स्ट्रीमिंग प्रतिसाद  

## नमुना चालवणे

तपशीलवार सेटअप सूचना आणि अधिक माहितीसाठी, [Github MCP Server Example README](./code_samples/github-mcp/README.md) पहा.

1. MCP सर्व्हर सुरू करा:  
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. अ‍ॅप्लिकेशन लाँच करा:  
   ```bash
   chainlit run app.py -w
   ```

3. एकत्रीकरणाची चाचणी करा:  
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## समस्या निवारण

सामान्य समस्या आणि उपाय:
1. MCP कनेक्शन समस्या  
   - सर्व्हर चालू आहे याची खात्री करा  
   - पोर्ट उपलब्धता तपासा  
   - GitHub टोकन्सची पुष्टी करा  

2. Azure Search समस्या  
   - कनेक्शन स्ट्रिंग्ज वैध आहेत का ते तपासा  
   - इंडेक्स अस्तित्वात आहे का ते तपासा  
   - दस्तऐवज अपलोड सत्यापित करा  

## पुढील पावले
- अतिरिक्त MCP साधने एक्सप्लोर करा  
- सानुकूल एजंट्स अंमलात आणा  
- RAG क्षमता वाढवा  
- अधिक इव्हेंट स्रोत जोडा  
- **प्रगत**: [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) येथे एजंट-टू-एजंट संवादाचे उदाहरण पहा  

## संसाधने
- [MCP सुरुवातीसाठी](https://aka.ms/mcp-for-beginners)  
- [MCP दस्तऐवजीकरण](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)  
- [Azure Cognitive Search दस्तऐवज](https://learn.microsoft.com/azure/search/)  
- [Semantic Kernel मार्गदर्शक](https://learn.microsoft.com/semantic-kernel/)  

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार नाही.