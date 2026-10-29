# एजेंट स्मोक टेस्ट

यह फ़ोल्डर उन एजेंटों के लिए **स्मोक-टेस्ट कैटलॉग** रखता है जिन्हें आप कोर्स में बनाते हैं।
एक स्मोक टेस्ट एक सस्ता, तेज़ जांच है कि एक **परिनियोजित Microsoft Foundry होस्टेड
एजेंट** पहुंच योग्य है, प्रतिक्रिया दे रहा है, और अपनी सबसे बुनियादी प्रॉम्प्ट
अपेक्षाओं का पालन कर रहा है। यह एक पहली बाधा है — [Lesson 10](../10-ai-agents-production/README.md) और
[Lesson 16](../16-deploying-scalable-agents/README.md) में आप जो पूर्ण मूल्यांकन
पाइपलाइन सीखते हैं उसके लिए प्रतिस्थापन नहीं है।

ये कैटलॉग [AI स्मोक टेस्ट](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action द्वारा [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
वर्कफ़्लो के माध्यम से उपभोग किए जाते हैं।

## कैसे चलाएं

1. पाठ का एजेंट Microsoft Foundry पर एक होस्टेड एजेंट के रूप में परिनियोजित करें (परिनियोजन वर्कफ़्लो के लिए
   Lesson 16 देखें)। **एजेंट नाम** और आपका **Foundry प्रोजेक्ट endpoint**
   नोट करें।
2. इन रिपॉज़िटरी सीक्रेट्स (Settings → Secrets and variables → Actions) को जोड़ें:
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`। संघीकृत
   पहचान को **Foundry प्रोजेक्ट स्कोप** में **Azure AI User** भूमिका की आवश्यकता होती है।
3. **Actions** टैब से, **Smoke-test hosted agents** चलाएं और पाठ के लिए
   `tests_file` चुनें, फिर मिलते जुलते `agent_name` और
   `project_endpoint` प्रदान करें।

## कैटलॉग → पाठ → एजेंट नाम

| कैटलॉग | पाठ | एजेंट के रूप में परिनियोजित करें |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Intro to AI Agents](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Tool Use](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Deploying Scalable Agents](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## किन पाठों के लिए स्मोक टेस्ट हैं?

स्मोक टेस्ट उन पाठों पर लागू होते हैं जहाँ आप **एजेंट परिनियोजित करते हैं** जिसका टेक्स्ट उत्तर ज्ञात सामग्री के खिलाफ सत्यापित किया जा सकता है।
जो पाठ वैचारिक हैं, केवल स्थानीय रूप से चलते हैं,
या गैर-नियतात्मक रचनात्मक आउटपुट उत्पन्न करते हैं वे जानबूझकर बाहर रखे गए हैं:

- **Lesson 17 (Creating Local AI Agents)** पूरी तरह से आपके कार्यस्थल पर Foundry Local के साथ चलता है और कोई Foundry Responses endpoint साझा नहीं करता, इसलिए यह
  कार्रवाई लागू नहीं होती। इसे स्थानीय रूप से नोटबुक चलाकर मान्य करें।
- डिज़ाइन-पैटर्न और सिद्धांत पाठ (02, 03, 06, 07, 09, 12) कोई एकल
  परिनियोजित एजेंट स्मोक-टेस्ट के लिए प्रदान नहीं करते।




प्रत्येक कैटलॉग एक JSON दस्तावेज़ है जिसमें एक शीर्ष-स्तरीय `tests` एरे होता है। प्रत्येक प्रविष्टि एक प्रॉम्प्ट पोस्ट करती है और प्रतिक्रिया पर पुष्टि करती है:
एक प्रॉम्प्ट पोस्ट करती है और प्रतिक्रिया पर पुष्टि करती है:

| फ़ील्ड | अर्थ |
|-------|---------|
| `id` | लॉग में मुद्रित एक अद्वितीय चरण पहचानकर्ता। |
| `description` | मानव-पठनीय उद्देश्य। |
| `prompt` | एजेंट को भेजा गया संदेश। |
| `assertions.status` | अपेक्षित HTTP स्थिति (डिफ़ॉल्ट 200)। |
| `assertions.contains_any` | पास अगर प्रतिक्रिया में इनमें से कोई भी उपस्ट्रिंग हो। |
| `assertions.contains_all` | पास अगर प्रतिक्रिया में हर उपस्ट्रिंग हो। |
| `assertions.contains_none` | पास अगर प्रतिक्रिया में इनमें से कोई भी उपस्ट्रिंग न हो। |
| `save_response_id_as` | बाद के मल्टी-टर्न चरण के लिए प्रतिक्रिया आईडी संग्रहित करें। |
| `use_previous_response_id` | इस टर्न को सहेजी गई प्रतिक्रिया आईडी से जोड़ा हुआ भेजें। |

पुष्टियां केस-असंवेदनशील उपस्ट्रिंग जांच हैं। पूर्ण स्कीमा के लिए देखें
[क्रिया प्रलेखन](https://github.com/marketplace/actions/ai-smoke-test),
जिसमें Foundry-प्रबंधित संवाद संसाधन शामिल हैं।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->