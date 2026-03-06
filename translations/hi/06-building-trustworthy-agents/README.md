[![विश्वसनीय एआई एजेंट](../../../translated_images/hi/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(इस पाठ का वीडियो देखने के लिए ऊपर की छवि पर क्लिक करें)_

# विश्वसनीय एआई एजेंट बनाना

## परिचय

यह पाठ निम्नलिखित को कवर करेगा:

- सुरक्षित और प्रभावी एआई एजेंट कैसे बनाएं और तैनात करें
- एआई एजेंट विकसित करते समय महत्वपूर्ण सुरक्षा विचार।
- एआई एजेंट विकसित करते समय डेटा और उपयोगकर्ता गोपनीयता कैसे बनाए रखें।

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप जानेंगे कि:

- एआई एजेंट बनाने में जोखिमों की पहचान और उनका मुकाबला कैसे करें।
- सुनिश्चित करें कि डेटा और अभिगम को सही ढंग से प्रबंधित किया जाए, इसके लिए सुरक्षा उपाय लागू करना।
- ऐसे एआई एजेंट बनाना जो डेटा गोपनीयता बनाए रखें और उत्कृष्ट उपयोगकर्ता अनुभव प्रदान करें।

## सुरक्षा

पहले सुरक्षित एजेंटिक एप्लिकेशन बनाने को देखें। सुरक्षा का मतलब है कि एआई एजेंट अपने डिजाइन के अनुसार कार्य करे। एजेंटिक एप्लिकेशन के निर्माता के रूप में, हमारे पास सुरक्षा अधिकतम करने के लिए विधियां और उपकरण हैं:

### सिस्टम संदेश फ्रेमवर्क बनाना

यदि आपने कभी बड़े भाषा मॉडल (LLMs) का उपयोग करके एआई एप्लिकेशन बनाया है, तो आप जानते हैं कि मजबूत सिस्टम प्रॉम्प्ट या सिस्टम संदेश डिजाइन करना कितना महत्वपूर्ण है। ये प्रॉम्प्ट उस तरीके के लिए मेटा नियम, निर्देश और दिशानिर्देश स्थापित करते हैं जिससे LLM उपयोगकर्ता और डेटा के साथ इंटरैक्ट करेगा।

एआई एजेंट्स के लिए, सिस्टम प्रॉम्प्ट और भी महत्वपूर्ण होता है क्योंकि एआई एजेंट्स को उन कार्यों को पूरा करने के लिए अत्यधिक विशिष्ट निर्देशों की आवश्यकता होगी जिन्हें हमने उनके लिए डिजाइन किया है।

मापनीय सिस्टम प्रॉम्प्ट बनाने के लिए, हम अपने एप्लिकेशन में एक या अधिक एजेंट बनाने के लिए एक सिस्टम संदेश फ्रेमवर्क का उपयोग कर सकते हैं:

![सिस्टम संदेश फ्रेमवर्क बनाना](../../../translated_images/hi/system-message-framework.3a97368c92d11d68.webp)

#### चरण 1: एक मेटा सिस्टम संदेश बनाएँ

मेटा प्रॉम्प्ट का उपयोग एक LLM द्वारा हमारे बनाए गए एजेंट्स के लिए सिस्टम प्रॉम्प्ट उत्पन्न करने के लिए किया जाएगा। हम इसे एक टेम्पलेट के रूप में डिज़ाइन करते हैं ताकि जरूरत पड़ने पर हम आसानी से कई एजेंट बना सकें।

यहाँ एक मेटा सिस्टम संदेश का उदाहरण है जिसे हम LLM को देंगे:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### चरण 2: एक बुनियादी प्रॉम्प्ट बनाएँ

अगला कदम एक बुनियादी प्रॉम्प्ट बनाना है जो एआई एजेंट का वर्णन करे। इसमें एजेंट की भूमिका, एजेंट द्वारा पूरा किए जाने वाले कार्य, और एजेंट की अन्य जिम्मेदारियों को शामिल किया जाना चाहिए।

यहाँ एक उदाहरण है:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### चरण 3: LLM को बुनियादी सिस्टम संदेश प्रदान करें

अब हम इस सिस्टम संदेश को बेहतर बनाने के लिए मेटा सिस्टम संदेश को सिस्टम संदेश के रूप में और हमारा बुनियादी सिस्टम संदेश प्रदान कर सकते हैं।

यह एक बेहतर डिज़ाइन किए गए सिस्टम संदेश का उत्पादन करेगा जो हमारे एआई एजेंट्स का मार्गदर्शन करने के लिए उपयुक्त होगा:

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

#### चरण 4: पुनरावृत्ति करें और सुधार करें

इस सिस्टम संदेश फ्रेमवर्क का मूल्य यह है कि कई एजेंट्स के सिस्टम संदेश बनाने को आसान और स्केलेबल बनाया जा सके, साथ ही समय के साथ आपके सिस्टम संदेशों में सुधार हो। यह दुर्लभ है कि प्रथम प्रयास में आपके पूर्ण उपयोग के लिए एक सिस्टम संदेश काम करेगा। छोटे संशोधन और बुनियादी सिस्टम संदेश में परिवर्तन करके और उसे सिस्टम से चलाकर तुलना करने और परिणामों का मूल्यांकन करने में सक्षम होना आपको बेहतर बनाने में मदद करेगा।

## खतरों को समझना

विश्वसनीय एआई एजेंट बनाने के लिए, आपके एआई एजेंट पर खतरों और जोखिमों को समझना और उनका मुकाबला करना जरूरी है। आइए कुछ मुख्य खतरों और उनके लिए आपकी बेहतर योजना और तैयारी के तरीकों पर नज़र डालें।

![खतरों को समझना](../../../translated_images/hi/understanding-threats.89edeada8a97fc0f.webp)

### कार्य और निर्देश

**विवरण:** हमलावर एआई एजेंट के निर्देशों या लक्ष्यों को प्रॉम्प्टिंग या इनपुट को नियंत्रित करके बदलने का प्रयास करते हैं।

**मिटिगेशन**: संभावित खतरनाक प्रॉम्प्ट्स का पता लगाने के लिए सत्यापन जांच और इनपुट फ़िल्टर लागू करें इससे पहले कि वे एआई एजेंट द्वारा संसाधित हों। चूंकि ये हमले आमतौर पर एजेंट के साथ बार-बार संपर्क की मांग करते हैं, इसलिए बातचीत में मुड़ (turns) की संख्या सीमित करना इन हमलों को रोकने का एक तरीका है।

### महत्वपूर्ण सिस्टम तक अभिगम

**विवरण**: यदि किसी एआई एजेंट को उन सिस्टम और सेवाओं तक पहुँच है जो संवेदनशील डेटा संग्रहीत करते हैं, तो हमलावर एजेंट और उन सेवाओं के बीच संचार को बाधित कर सकते हैं। ये सीधे हमले हो सकते हैं या एजेंट के माध्यम से उन सिस्टम के बारे में जानकारी प्राप्त करने के अप्रत्यक्ष प्रयास हो सकते हैं।

**मिटिगेशन**: सुरक्षा के लिए एजेंट के पास सिस्टम तक केवल आवश्यकतानुसार पहुंच होनी चाहिए। एजेंट और सिस्टम के बीच संचार भी सुरक्षित होना चाहिए। प्रमाणीकरण और अभिगम नियंत्रण लागू करना इस जानकारी की सुरक्षा का एक अन्य तरीका है।

### संसाधन और सेवा अधिभार

**विवरण:** एआई एजेंट विभिन्न उपकरण और सेवाओं का उपयोग कार्य पूरा करने के लिए कर सकते हैं। हमलावर इस क्षमता का उपयोग सेवाओं पर हमला करने के लिए कर सकते हैं, एआई एजेंट के माध्यम से बहुत अधिक अनुरोध भेजकर, जिससे सिस्टम विफलताएँ या उच्च लागत हो सकती है।

**मिटिगेशन:** एक सेवा को एजेंट द्वारा किए जाने वाले अनुरोधों की संख्या को सीमित करने के लिए नीतियाँ लागू करें। बातचीत के मुड़ और एआई एजेंट के अनुरोधों की संख्या सीमित करना इस प्रकार के हमलों को रोकने का एक अन्य तरीका है।

### ज्ञान आधार विषाक्तता

**विवरण:** इस प्रकार का हमला सीधे एआई एजेंट को लक्षित नहीं करता, बल्कि ज्ञान आधार और अन्य सेवाओं को लक्षित करता है जिनका उपयोग एआई एजेंट कार्य पूरा करने के लिए करता है। इसमें डेटा या जानकारी को भ्रष्ट करना शामिल हो सकता है, जिससे एजेंट उपयोगकर्ता को पक्षपाती या अनपेक्षित प्रतिक्रिया दे सकता है।

**मिटिगेशन:** उन डेटा का नियमित सत्यापन करें जिनका उपयोग एआई एजेंट अपने वर्कफ़्लोज़ में करता है। इस डेटा तक पहुँच सुरक्षित होनी चाहिए और इसे केवल भरोसेमंद व्यक्तियों द्वारा ही बदला जाना चाहिए ताकि इस प्रकार के हमलों से बचा जा सके।

### झरना प्रभाव वाली त्रुटियाँ

**विवरण:** एआई एजेंट अलग-अलग उपकरणों और सेवाओं का उपयोग कार्य पूरा करने के लिए करते हैं। हमलावरों द्वारा उत्पन्न त्रुटियाँ अन्य सिस्टम की विफलताएँ कर सकती हैं, जिससे हमला व्यापक और समस्या निवारण कठिन हो जाता है।

**मिटिगेशन**: इसका एक तरीका यह है कि एआई एजेंट को सीमित वातावरण में चलाया जाए, जैसे डॉकर कंटेनर में कार्य करना, ताकि सीधे सिस्टम हमलों से बचा जा सके। जब कुछ सिस्टम त्रुटि के साथ प्रतिक्रिया देते हैं तो बैकअप मैकेनिज्म और पुन: प्रयास तर्क (retry logic) बनाना व्यापक सिस्टम विफलताओं को रोकने का एक अन्य तरीका है।

## मानव-इन-द-लूप

विश्वसनीय एआई एजेंट सिस्टम बनाने का एक और प्रभावी तरीका है मानव-इन-द-लूप का उपयोग। यह एक ऐसा प्रवाह बनाता है जहाँ उपयोगकर्ता एजेंट्स को रन के दौरान प्रतिक्रिया प्रदान कर सकते हैं। उपयोगकर्ता मूल रूप से एक बहु-एजेंट सिस्टम में एजेंट के रूप में कार्य करते हैं और रनिंग प्रक्रिया को मंजूरी देने या समाप्त करने द्वारा योगदान देते हैं।

![ह्यूमन इन द लूप](../../../translated_images/hi/human-in-the-loop.5f0068a678f62f4f.webp)

यहाँ Microsoft Agent Framework का उपयोग करके इस अवधारणा को लागू करने वाला एक कोड स्निपेट है:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# मानव-इन-द-लूप अनुमोदन के साथ प्रदाता बनाएं
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# मानव अनुमोदन चरण के साथ एजेंट बनाएं
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# उपयोगकर्ता प्रतिक्रिया की समीक्षा कर सकता है और अनुमोदित कर सकता है
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## निष्कर्ष

विश्वसनीय एआई एजेंट बनाने के लिए सावधानीपूर्वक डिजाइन, मजबूत सुरक्षा उपाय, और सतत पुनरावृत्ति आवश्यक है। संरचित मेटा प्रॉम्प्टिंग सिस्टम लागू करके, संभावित खतरों को समझकर, और निवारण रणनीतियाँ अपनाकर डेवलपर्स ऐसे एआई एजेंट बना सकते हैं जो सुरक्षित और प्रभावी दोनों हों। इसके अतिरिक्त, मानव-इन-द-लूप दृष्टिकोण को अपनाने से एआई एजेंट उपयोगकर्ता की आवश्यकताओं के अनुरूप बने रहते हैं और जोखिम कम होते हैं। जैसे-जैसे एआई विकसित होता रहेगा, सुरक्षा, गोपनीयता, और नैतिक विचारों पर सक्रिय दृष्टिकोण बनाए रखना एआई-संचालित सिस्टम में विश्वसनीयता और विश्वास बनाए रखने में महत्वपूर्ण होगा।

### विश्वसनीय एआई एजेंट बनाने के बारे में और प्रश्न हैं?

अन्य शिक्षार्थियों से मिलने, कार्यालय समय में भाग लेने और अपने एआई एजेंट्स के प्रश्नों के उत्तर प्राप्त करने के लिए [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) में शामिल हों।

## अतिरिक्त संसाधन

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">जिम्मेदार एआई का अवलोकन</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">जनरेटिव एआई मॉडल और एआई अनुप्रयोगों का मूल्यांकन</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">सुरक्षा सिस्टम संदेश</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">जोखिम आकलन टेम्पलेट</a>

## पिछला पाठ

[एजेंटिक RAG](../05-agentic-rag/README.md)

## अगला पाठ

[परियोजना डिज़ाइन पैटर्न](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्राधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->