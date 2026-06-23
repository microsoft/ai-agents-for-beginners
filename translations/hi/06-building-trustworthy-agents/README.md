[![विश्वसनीय एआई एजेंट](../../../translated_images/hi/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(इस पाठ का वीडियो देखने के लिए ऊपर छवि पर क्लिक करें)_

# विश्वसनीय AI एजेंट बनाना

## परिचय

यह पाठ निम्नलिखित विषयों को कवर करेगा:

- कैसे सुरक्षित और प्रभावी AI एजेंट बनाएँ और तैनात करें
- AI एजेंट विकसित करते समय महत्वपूर्ण सुरक्षा विचार
- AI एजेंट विकसित करते समय डेटा और उपयोगकर्ता गोपनीयता कैसे बनाए रखें

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप जानेंगे कि कैसे:

- AI एजेंट बनाते समय जोखिमों की पहचान और उन्हें कम करें।
- डेटा और पहुंच को उचित रूप से प्रबंधित करने के लिए सुरक्षा उपाय लागू करें।
- ऐसे AI एजेंट बनाएँ जो डेटा गोपनीयता बनाए रखें और गुणवत्ता युक्त उपयोगकर्ता अनुभव प्रदान करें।

## सुरक्षा

पहले सुरक्षित एजेंटिक एप्लिकेशन बनाने पर नज़र डालते हैं। सुरक्षा का अर्थ है कि AI एजेंट जैसा डिज़ाइन किया गया है वैसा प्रदर्शन करे। एजेंटिक एप्लिकेशन के निर्माता के रूप में, हमारे पास सुरक्षा अधिकतम करने के लिए तरीके और उपकरण हैं:

### सिस्टम संदेश फ्रेमवर्क बनाना

यदि आपने कभी बड़े भाषा मॉडल (LLMs) का उपयोग करके AI एप्लिकेशन बनाया है, तो आप जानते हैं कि एक मजबूत सिस्टम प्रॉम्प्ट या सिस्टम संदेश डिज़ाइन करना कितना महत्वपूर्ण है। ये प्रॉम्प्ट उस तरीके के लिए मेटा नियम, निर्देश, और दिशानिर्देश स्थापित करते हैं कि LLM उपयोगकर्ता और डेटा के साथ कैसे इंटरैक्ट करेगा।

AI एजेंट के लिए, सिस्टम प्रॉम्प्ट और भी अधिक महत्वपूर्ण है क्योंकि AI एजेंटों को उन कार्यों को पूरा करने के लिए अत्यंत विशिष्ट निर्देशों की आवश्यकता होगी जिन्हें हमने उनके लिए डिज़ाइन किया है।

स्केलेबल सिस्टम प्रॉम्प्ट बनाने के लिए, हम अपने एप्लिकेशन में एक या अधिक एजेंटों को बनाने के लिए सिस्टम संदेश फ्रेमवर्क का उपयोग कर सकते हैं:

![सिस्टम संदेश फ्रेमवर्क बनाना](../../../translated_images/hi/system-message-framework.3a97368c92d11d68.webp)

#### चरण 1: एक मेटा सिस्टम संदेश बनाएँ

मेटा प्रॉम्प्ट का उपयोग LLM द्वारा उन एजेंटों के लिए सिस्टम प्रॉम्प्ट बनाने के लिए किया जाएगा जिन्हें हम बनाते हैं। हम इसे एक टेम्प्लेट के रूप में डिज़ाइन करते हैं ताकि आवश्यकतानुसार बहु एजेंटों को आसानी से बनाया जा सके।

यहाँ एक मेटा सिस्टम संदेश का उदाहरण है जो हम LLM को देंगे:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### चरण 2: एक बुनियादी प्रॉम्प्ट बनाएँ

अगला चरण AI एजेंट का वर्णन करने के लिए एक बुनियादी प्रॉम्प्ट बनाना है। आपको एजेंट की भूमिका, एजेंट द्वारा किए जाने वाले कार्य, और एजेंट की अन्य ज़िम्मेदारियों को शामिल करना चाहिए।

यहाँ एक उदाहरण है:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### चरण 3: LLM को बुनियादी सिस्टम संदेश प्रदान करें

अब हम इस सिस्टम संदेश को बेहतर बना सकते हैं। इसके लिए मेटा सिस्टम संदेश को सिस्टम संदेश के रूप में प्रदान करें और अपने बुनियादी सिस्टम संदेश को भी शामिल करें।

इससे एक ऐसा सिस्टम संदेश उत्पन्न होगा जो हमारे AI एजेंटों का मार्गदर्शन करने के लिए बेहतर डिज़ाइन किया गया है:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### चरण 4: पुनरावृति और सुधार करें

इस सिस्टम संदेश फ्रेमवर्क का मूल्य यह है कि आप एक से अधिक एजेंटों के लिए सिस्टम संदेश बनाने को आसान और स्केलेबल बना सकते हैं और समय के साथ अपने सिस्टम संदेशों में सुधार कर सकते हैं। पहली बार में आपके पूरे उपयोग मामले के लिए काम करने वाला सिस्टम संदेश होना दुर्लभ है। बुनियादी सिस्टम संदेश में छोटे समायोजन और सुधार करना, और उसे सिस्टम के माध्यम से चलाना आपको परिणामों की तुलना और मूल्यांकन करने में मदद करेगा।

## खतरों को समझना

विश्वसनीय AI एजेंट बनाने के लिए, आपके AI एजेंट के लिए जोखिमों और खतरों को समझना और कम करना महत्वपूर्ण है। आइए कुछ AI एजेंटों के विभिन्न खतरों को देखें और आप उनके लिए बेहतर योजना और तैयारी कैसे कर सकते हैं।

![खतरों को समझना](../../../translated_images/hi/understanding-threats.89edeada8a97fc0f.webp)

### कार्य और निर्देश

**वर्णन:** हमलावर AI एजेंट के निर्देशों या लक्ष्यों को प्रॉम्प्टिंग या इनपुट को नियंत्रित करके बदलने का प्रयास करते हैं।

**रोकथाम:** ऐसे संभावित खतरनाक प्रॉम्प्ट का पता लगाने के लिए सत्यापन जांच और इनपुट फिल्टर लागू करें इससे पहले कि AI एजेंट इसे प्रक्रिया करे। चूंकि ये हमले आमतौर पर एजेंट के साथ बार-बार संवाद की मांग करते हैं, इसलिए बातचीत में टर्न्स की संख्या सीमित करना इन हमलों को रोकने का एक तरीका है।

### महत्वपूर्ण सिस्टमों तक पहुंच

**वर्णन:** यदि AI एजेंट को संवेदनशील डेटा संग्रहित करने वाले सिस्टम और सेवाओं तक पहुंच प्राप्त है, तो हमलावर एजेंट और इन सेवाओं के बीच संचार से छेड़छाड़ कर सकते हैं। ये सीधे हमले हो सकते हैं या एजेंट के माध्यम से इन सिस्टमों के बारे में जानकारी प्राप्त करने के अप्रत्यक्ष प्रयास हो सकते हैं।

**रोकथाम:** AI एजेंटों को केवल आवश्यकतानुसार सिस्टमों तक पहुंच होनी चाहिए ताकि इन प्रकार के हमलों से बचा जा सके। एजेंट और सिस्टम के बीच संचार भी सुरक्षित होना चाहिए। प्रमाणीकरण और पहुंच नियंत्रण लागू करना इस जानकारी की सुरक्षा करने का एक और तरीका है।

### संसाधन और सेवा अधिभारित करना

**वर्णन:** AI एजेंट कार्यों को पूरा करने के लिए विभिन्न टूल और सेवाओं तक पहुंच सकता है। हमलावर AI एजेंट के माध्यम से बड़ी संख्या में अनुरोध भेजकर इन सेवाओं पर हमले कर सकते हैं, जिससे सिस्टम विफलताएं या उच्च लागत हो सकती है।

**रोकथाम:** ऐसी नीतियाँ लागू करें जो AI एजेंट को किसी सेवा पर अनुरोधों की संख्या सीमित करें। AI एजेंट के लिए बातचीत के टर्न्स और अनुरोधों की संख्या सीमित करना इन हमलों को रोकने का एक और तरीका है।

### ज्ञान आधार विषाक्तकरण

**वर्णन:** इस प्रकार का हमला सीधे AI एजेंट को लक्षित नहीं करता लेकिन ज्ञान आधार और अन्य सेवाओं को लक्षित करता है जिन्हें AI एजेंट उपयोग करता है। यह डेटा या जानकारी को भ्रष्ट कर सकता है जिसका AI एजेंट कार्य पूरा करने में उपयोग करता है, जिससे पक्षपाती या अनियोजित प्रतिक्रियाएँ उपयोगकर्ता को मिलती हैं।

**रोकथाम:** उन डेटा की नियमित जांच करें जिन्हें AI एजेंट अपने वर्कफ़्लोज़ में उपयोग करता है। सुनिश्चित करें कि इस डेटा तक पहुंच सुरक्षित हो और केवल विश्वसनीय व्यक्तियों द्वारा बदली जा सके ताकि इस प्रकार के हमले से बचा जा सके।

### झरझरा त्रुटियाँ

**वर्णन:** AI एजेंट कार्यों को पूरा करने के लिए विभिन्न टूल और सेवाओं तक पहुंचता है। हमलावरों के कारण हुई त्रुटियाँ अन्य सिस्टमों की विफलताएँ पैदा कर सकती हैं जिनसे AI एजेंट जुड़ा होता है, जिससे हमला व्यापक हो जाता है और समस्या का समाधान करना अधिक कठिन हो जाता है।

**रोकथाम:** इस से बचने का एक तरीका है कि AI एजेंट सीमित पर्यावरण में कार्य करे, जैसे डॉकर कंटेनर में कार्य करना, ताकि सीधे सिस्टम हमलों को रोका जा सके। जब कुछ सिस्टम त्रुटि के साथ प्रतिक्रिया देते हैं तो पुनः प्रयास तंत्र और बैकअप व्यवस्था बनाना बड़ा सिस्टम विफलताओं को रोकने का एक तरीका है।

## मानव-इन-द-लूप

विश्वसनीय AI एजेंट सिस्टम बनाने का एक और प्रभावी तरीका है मानव-इन-द-लूप का उपयोग करना। यह एक ऐसी प्रक्रिया बनाता है जहां उपयोगकर्ता एजेंटों को रन के दौरान प्रतिक्रिया प्रदान कर सकते हैं। उपयोगकर्ता वास्तव में एक बहु-एजेंट सिस्टम में एजेंट के रूप में कार्य करते हैं और चल रहे प्रक्रिया को अनुमोदन या समाप्त कर सकते हैं।

![मानव-इन-द-लूप](../../../translated_images/hi/human-in-the-loop.5f0068a678f62f4f.webp)

यहाँ Microsoft Agent Framework का उपयोग करते हुए कोड स्निपेट है जो दिखाता है कि यह अवधारणा कैसे लागू की जाती है:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# मानव की स्वीकृति के साथ प्रदाता बनाएं
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# मानव स्वीकृति चरण के साथ एजेंट बनाएं
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# उपयोगकर्ता प्रतिक्रिया की समीक्षा कर सकता है और उसे अनुमोदित कर सकता है
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## निष्कर्ष

विश्वसनीय AI एजेंट बनाने के लिए सावधानीपूर्वक डिज़ाइन, मजबूत सुरक्षा उपाय, और निरंतर पुनरावृति आवश्यक है। संरचित मेटा प्रॉम्प्टिंग सिस्टम लागू करके, संभावित खतरों को समझकर, और रोकथाम रणनीतियाँ अपनाकर, डेवलपर्स सुरक्षित और प्रभावी AI एजेंट बना सकते हैं। इसके अतिरिक्त, मानव-इन-द-लूप दृष्टिकोण को शामिल करने से यह सुनिश्चित होता है कि AI एजेंट उपयोगकर्ता की आवश्यकताओं के अनुरूप बने रहें और जोखिमों को कम किया जा सके। जैसे-जैसे AI विकसित होता रहेगा, सुरक्षा, गोपनीयता, और नैतिक विचारों पर सक्रिय दृष्टिकोण बनाए रखना AI-चालित सिस्टमों में भरोसे और विश्वसनीयता बढ़ाने के लिए महत्वपूर्ण होगा।

## कोड उदाहरण

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): मेटा-प्रॉम्प्ट सिस्टम-संदेश फ्रेमवर्क का चरण-दर-चरण प्रदर्शन।
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): भरोसेमंद एजेंटों के लिए पूर्व-क्रियान्वयन अनुमोदन गेट्स, जोखिम स्तर निर्धारण, और ऑडिट लॉगिंग।

### विश्वसनीय AI एजेंट बनाने के बारे में और प्रश्न हैं?

अन्य शिक्षार्थियों से मिलने, ऑफिस आवर्स में भाग लेने, और अपने AI एजेंट प्रश्नों के उत्तर पाने के लिए [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) से जुड़ें।

## अतिरिक्त संसाधन

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">जिम्मेदार AI का अवलोकन</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">सृजनात्मक AI मॉडल और AI एप्लिकेशन का मूल्यांकन</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">सुरक्षा सिस्टम संदेश</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">जोखिम आकलन टेम्पलेट</a>

## पिछला पाठ

[Agentic RAG](../05-agentic-rag/README.md)

## अगला पाठ

[योजना डिजाइन पैटर्न](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->