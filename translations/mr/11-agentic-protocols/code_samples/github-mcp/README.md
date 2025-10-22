<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T10:57:59+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "mr"
}
-->
# Github MCP Server Example

## वर्णन

ही डेमो Microsoft Reactor द्वारे आयोजित AI Agents Hackathon साठी तयार केली गेली होती.

हे टूल वापरकर्त्याच्या Github रिपॉजिटरीजच्या आधारे हॅकाथॉन प्रोजेक्ट्सची शिफारस करण्यासाठी वापरले जाते. हे खालीलप्रमाणे कार्य करते:

1. **Github Agent** - Github MCP Server चा वापर करून रिपॉजिटरीज आणि त्यांच्याशी संबंधित माहिती मिळवणे.
2. **Hackathon Agent** - Github Agent कडून डेटा घेऊन, वापरकर्त्याच्या प्रोजेक्ट्स, वापरलेल्या प्रोग्रामिंग भाषांवर आधारित आणि AI Agents हॅकाथॉनसाठीच्या प्रोजेक्ट ट्रॅक्सवर आधारित सर्जनशील हॅकाथॉन प्रोजेक्ट कल्पना तयार करणे.
3. **Events Agent** - Hackathon Agent च्या शिफारसींवर आधारित, AI Agent Hackathon मालिकेतील संबंधित इव्हेंट्सची शिफारस करणे.

## कोड चालवणे

### पर्यावरणीय व्हेरिएबल्स

या डेमोमध्ये Azure Open AI Service, Semantic Kernel, Github MCP Server आणि Azure AI Search चा वापर केला जातो.

या टूल्सचा वापर करण्यासाठी योग्य पर्यावरणीय व्हेरिएबल्स सेट केलेले असल्याची खात्री करा:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
```

## Chainlit Server चालवणे

MCP Server शी कनेक्ट होण्यासाठी, या डेमोमध्ये Chainlit चॅट इंटरफेस म्हणून वापरले जाते.

सर्व्हर चालवण्यासाठी, तुमच्या टर्मिनलमध्ये खालील कमांड वापरा:

```bash
chainlit run app.py -w
```

हे `localhost:8000` वर तुमचा Chainlit सर्व्हर सुरू करेल आणि `event-descriptions.md` सामग्रीसह तुमचा Azure AI Search Index भरून काढेल.

## MCP Server शी कनेक्ट होणे

Github MCP Server शी कनेक्ट होण्यासाठी, "Type your message here.." च्या खाली असलेल्या "plug" आयकॉनवर क्लिक करा:

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.mr.png)

तिथून, "Connect an MCP" वर क्लिक करा आणि Github MCP Server शी कनेक्ट होण्यासाठी कमांड जोडा:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

"[YOUR PERSONAL ACCESS TOKEN]" च्या जागी तुमचा खरा Personal Access Token टाका.

कनेक्ट झाल्यानंतर, प्लग आयकॉनच्या शेजारी (1) दिसेल, ज्यामुळे कनेक्शनची पुष्टी होईल. जर तसे झाले नाही, तर `chainlit run app.py -w` वापरून Chainlit सर्व्हर पुन्हा सुरू करण्याचा प्रयत्न करा.

## डेमो वापरणे

हॅकाथॉन प्रोजेक्ट्सची शिफारस करण्यासाठी एजंट वर्कफ्लो सुरू करण्यासाठी, तुम्ही असा संदेश टाइप करू शकता:

"Recommend hackathon projects for the Github user koreyspace"

Router Agent तुमच्या विनंतीचे विश्लेषण करेल आणि कोणत्या एजंट्सच्या (GitHub, Hackathon, आणि Events) संयोजनाने तुमच्या क्वेरीला उत्तम प्रकारे हाताळता येईल हे ठरवेल. हे एजंट्स एकत्र काम करून Github रिपॉजिटरी विश्लेषण, प्रोजेक्ट कल्पना आणि संबंधित टेक इव्हेंट्सच्या आधारे सर्वसमावेशक शिफारसी प्रदान करतात.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर केल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.