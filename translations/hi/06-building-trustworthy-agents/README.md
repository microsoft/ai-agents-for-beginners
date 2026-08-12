[![विश्वसनीय एआई एजेंट](../../../translated_images/hi/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(इस पाठ का वीडियो देखने के लिए ऊपर की छवि पर क्लिक करें)_

# विश्वसनीय एआई एजेंट बनाना

## परिचय

इस पाठ में शामिल होंगे:

- सुरक्षित और प्रभावी AI एजेंट बनाने और तैनात करने का तरीका
- AI एजेंट विकसित करते समय महत्वपूर्ण सुरक्षा विचार।
- AI एजेंट विकसित करते समय डेटा और उपयोगकर्ता गोपनीयता बनाए रखने का तरीका।

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप जानेंगे कि कैसे:

- AI एजेंट बनाते समय जोखिमों की पहचान करना और उन्हें कम करना।
- डेटा और पहुँच को सही ढंग से प्रबंधित करने के लिए सुरक्षा उपाय लागू करना।
- ऐसे AI एजेंट बनाना जो डेटा गोपनीयता बनाए रखें और एक गुणवत्तापूर्ण उपयोगकर्ता अनुभव प्रदान करें।

## सुरक्षा

आइए पहले सुरक्षित एजेंटिक अनुप्रयोग बनाने को देखें। सुरक्षा का मतलब है कि AI एजेंट जैसा डिजाइन किया गया है, वैसा काम करे। एजेंटिक अनुप्रयोगों के निर्माता के रूप में, हमारे पास सुरक्षा अधिकतम करने के लिए तरीके और उपकरण होते हैं:

### सिस्टम संदेश फ्रेमवर्क बनाना

यदि आपने कभी बड़े भाषा मॉडल (LLMs) का उपयोग करके AI अनुप्रयोग बनाया है, तो आप जानते हैं कि एक मजबूत सिस्टम प्रॉम्प्ट या सिस्टम संदेश डिजाइन करना कितना महत्वपूर्ण है। ये प्रॉम्प्ट LLM के उपयोगकर्ता और डेटा के साथ कैसे इंटरैक्ट करेगा, इसके लिए मेटा नियम, निर्देश, और दिशानिर्देश स्थापित करते हैं।

AI एजेंटों के लिए, सिस्टम प्रॉम्प्ट और भी महत्वपूर्ण होता है क्योंकि AI एजेंटों को उन कार्यों को पूरा करने के लिए अत्यधिक विशिष्ट निर्देशों की आवश्यकता होगी जो हमने उनके लिए डिजाइन किए हैं।

स्केलेबल सिस्टम प्रॉम्प्ट बनाने के लिए, हम अपने अनुप्रयोग में एक या अधिक एजेंट बनाने के लिए सिस्टम संदेश फ्रेमवर्क का उपयोग कर सकते हैं:

![सिस्टम संदेश फ्रेमवर्क बनाना](../../../translated_images/hi/system-message-framework.3a97368c92d11d68.webp)

#### चरण 1: एक मेटा सिस्टम संदेश बनाएं

मेटा प्रॉम्प्ट का उपयोग LLM द्वारा हम जो एजेंट बनाते हैं उनके सिस्टम प्रॉम्प्ट उत्पन्न करने के लिए किया जाएगा। हम इसे एक टेम्पलेट के रूप में डिजाइन करते हैं ताकि आवश्यक होने पर हम कई एजेंट आसानी से बना सकें।

यहाँ एक मेटा सिस्टम संदेश का उदाहरण दिया गया है जो हम LLM को देंगे:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### चरण 2: एक बुनियादी प्रॉम्प्ट बनाएं

अगला चरण AI एजेंट का वर्णन करने के लिए एक बुनियादी प्रॉम्प्ट बनाना है। इसमें आपको एजेंट की भूमिका, एजेंट के कार्य, और एजेंट की अन्य जिम्मेदारियों को शामिल करना चाहिए।

यहाँ एक उदाहरण है:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### चरण 3: बुनियादी सिस्टम संदेश LLM को दें

अब हम इस सिस्टम संदेश को अनुकूलित कर सकते हैं, मेटा सिस्टम संदेश को सिस्टम संदेश के रूप में प्रदान करके और हमारे बुनियादी सिस्टम संदेश को भी शामिल करके।

इससे ऐसा सिस्टम संदेश उत्पन्न होगा जो हमारे AI एजेंटों का मार्गदर्शन करने के लिए बेहतर डिजाइन किया गया है:

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

#### चरण 4: पुनरावृत्ति और सुधार करें

इस सिस्टम संदेश फ्रेमवर्क का मूल्य यह है कि यह कई एजेंटों से सिस्टम संदेश बनाना आसान बनाता है और आपकी सिस्टम संदेशों को समय के साथ सुधारने में मदद करता है। यह दुर्लभ होता है कि आपका सिस्टम संदेश पहली बार पूरी तरह से आपके उपयोग के केस के लिए काम करे। छोटे बदलाव और सुधार करना, बुनियादी सिस्टम संदेश बदलकर और उसे सिस्टम के माध्यम से चलाकर, आपको परिणामों की तुलना और मूल्यांकन करने की अनुमति देगा।

## खतरों को समझना

विश्वसनीय AI एजेंट बनाने के लिए, यह महत्वपूर्ण है कि आप अपने AI एजेंट के लिए जोखिमों और खतरों को समझें और उन्हें कम करें। आइए कुछ खतरों पर नजर डालें और देखें कि आप बेहतर योजना कैसे बना सकते हैं और उनकी तैयारी कैसे कर सकते हैं।

![खतरों को समझना](../../../translated_images/hi/understanding-threats.89edeada8a97fc0f.webp)

### कार्य और निर्देश

**वर्णन:** हमलावर AI एजेंट के निर्देशों या लक्ष्यों को प्रॉम्प्टिंग या इनपुट को मैनिपुलेट करके बदलने का प्रयास करते हैं।

**निवारण**: संभावित खतरनाक प्रॉम्प्ट को पहचानने के लिए प्रमाणीकरण जांच और इनपुट फ़िल्टर लागू करें इससे पहले कि वे AI एजेंट द्वारा संसाधित किए जाएं। क्योंकि ये हमले आमतौर पर एजेंट के साथ बार-बार इंटरैक्शन की मांग करते हैं, संवाद में टर्न्स की संख्या सीमित करना इन हमलों को रोकने का एक और तरीका है।

### महत्वपूर्ण प्रणालियों तक पहुंच

**वर्णन**: यदि AI एजेंट संवेदनशील डेटा रखने वाली प्रणालियों और सेवाओं तक पहुँच रखता है, तो हमलावर एजेंट और इन सेवाओं के बीच संचार को अधिग्रहित कर सकते हैं। ये सीधे हमले हो सकते हैं या एजेंट के माध्यम से इन प्रणालियों के बारे में जानकारी प्राप्त करने के अप्रत्यक्ष प्रयास हो सकते हैं।

**निवारण**: AI एजेंटों को केवल आवश्यकतानुसार प्रणालियों तक पहुंचनी चाहिए ताकि ऐसे हमलों को रोका जा सके। एजेंट और सिस्टम के बीच संचार भी सुरक्षित होना चाहिए। प्रमाणीकरण और पहुंच नियंत्रण लागू करना इस जानकारी की सुरक्षा का एक और तरीका है।

### संसाधन और सेवा अतिभार

**वर्णन:** AI एजेंट विभिन्न उपकरणों और सेवाओं का उपयोग कार्यों को पूरा करने के लिए कर सकते हैं। हमलावर इस क्षमता का उपयोग इन सेवाओं पर उच्च मात्रा में अनुरोध भेज कर उन्हें निशाना बनाने के लिए कर सकते हैं, जिससे सिस्टम विफलताओं या उच्च लागत हो सकती है।

**निवारण:** ऐसी नीतियां लागू करें जो एक सेवा को AI एजेंट द्वारा किए जाने वाले अनुरोधों की संख्या को सीमित करें। संवाद टर्न्स और AI एजेंट को अनुरोधों की संख्या सीमित करना ऐसे हमलों को रोकने का एक और तरीका है।

### ज्ञान आधार विषाक्तता

**वर्णन:** इस प्रकार का हमला सीधे AI एजेंट को लक्षित नहीं करता बल्कि ज्ञान आधार और अन्य सेवाओं को निशाना बनाता है जो AI एजेंट उपयोग करेगा। इसमें डेटा या जानकारी को भ्रष्ट करना शामिल हो सकता है जो AI एजेंट कार्य पूरा करने के लिए उपयोग करेगा, जिससे पक्षपाती या अनपेक्षित प्रतिक्रियाएं उपयोगकर्ता को मिल सकती हैं।

**निवारण:** नियमित रूप से उस डेटा का सत्यापन करें जिसका AI एजेंट अपने वर्कफ़्लो में उपयोग करने वाला है। सुनिश्चित करें कि इस डेटा तक पहुंच सुरक्षित है और केवल विश्वसनीय व्यक्तियों द्वारा ही इसमें परिवर्तन किया जाता है ताकि इस प्रकार के हमलों से बचा जा सके।

### त्रुटियाँ बढ़ना (कैस्केडिंग एरर्स)

**वर्णन:** AI एजेंट विभिन्न उपकरणों और सेवाओं का उपयोग कार्यों को पूरा करने के लिए करता है। हमलावरों द्वारा उत्पन्न त्रुटियाँ अन्य प्रणालियों की विफलताओं का कारण बन सकती हैं जिनसे AI एजेंट जुड़ा हुआ है, जिससे हमला व्यापक हो जाता है और समस्या को समझना और हल करना कठिन होता है।

**निवारण**: इस से बचने का एक तरीका है कि AI एजेंट सीमित वातावरण में कार्य करे, जैसे कि डॉकर कंटेनर में कार्य करना, ताकि सीधे सिस्टम हमलों से बचा जा सके। जब कुछ सिस्टम त्रुटि के साथ प्रतिक्रिया देते हैं तो फॉलबैक तंत्र और पुनः प्रयास तर्क बनाना बड़े सिस्टम विफलताओं को रोकने का एक तरीका है।

## मानव की भागीदारी (Human-in-the-Loop)

विश्वसनीय AI एजेंट सिस्टम बनाने का एक और प्रभावी तरीका है मानव की भागीदारी। इससे ऐसा प्रवाह बनता है जहाँ उपयोगकर्ता चलाए जा रहे एजेंट को प्रतिक्रिया प्रदान कर सकते हैं। उपयोगकर्ता मल्टी-एजेंट सिस्टम में एजेंट की तरह कार्य करते हैं और चल रहे प्रक्रिया को अनुमोदित या समाप्त कर सकते हैं।

![Human in The Loop](../../../translated_images/hi/human-in-the-loop.5f0068a678f62f4f.webp)

यहाँ Microsoft Agent Framework का उपयोग करते हुए एक कोड स्निपेट दिया गया है जो दिखाता है कि यह अवधारणा कैसे लागू की जाती है:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# मानव-इन-द-लूप अनुमोदन के साथ प्रदाता बनाएँ
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# मानव अनुमोदन चरण के साथ एजेंट बनाएँ
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# उपयोगकर्ता प्रतिक्रिया की समीक्षा कर सकता है और उसे स्वीकृत कर सकता है
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## निष्कर्ष

विश्वसनीय AI एजेंट बनाने के लिए सावधान डिज़ाइन, मजबूत सुरक्षा उपाय, और निरंतर पुनरावृत्ति आवश्यक है। संरचित मेटा प्रॉम्प्टिंग सिस्टम लागू करके, संभावित खतरों को समझकर, और निवारण रणनीतियाँ अपनाकर, डेवलपर्स ऐसे AI एजेंट बना सकते हैं जो सुरक्षित और प्रभावी दोनों हों। इसके साथ ही, मानव की भागीदारी दृष्टिकोण को शामिल करने से सुनिश्चित होता है कि AI एजेंट उपयोगकर्ता की आवश्यकताओं के अनुरूप बने रहें और जोखिम न्यूनतम हो। जैसे-जैसे AI विकसित होता रहेगा, सुरक्षा, गोपनीयता और नैतिक विचारों पर सक्रिय दृष्टिकोण बनाए रखना AI-चालित सिस्टम में विश्वास और विश्वसनीयता बढ़ाने के लिए महत्वपूर्ण होगा।

## कोड उदाहरण

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): मेटा-प्रॉम्प्ट सिस्टम-संदेश फ्रेमवर्क का चरण-दर-चरण प्रदर्शन।
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): विश्वसनीय एजेंटों के लिए पूर्व-कार्रवाई अनुमोदन गेट, जोखिम स्तरीकरण, और ऑडिट लॉगिंग।

### विश्वसनीय AI एजेंट बनाने के बारे में और प्रश्न?

अन्य शिक्षार्थियों से मिलने, कार्यालय समय में भाग लेने और अपने AI एजेंट प्रश्नों का उत्तर पाने के लिए [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) में शामिल हों।

## अतिरिक्त संसाधन

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">जिम्मेदार AI अवलोकन</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">जनरेटिव AI मॉडल और AI अनुप्रयोगों का मूल्यांकन</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">सुरक्षा सिस्टम संदेश</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">जोखिम मूल्यांकन टेम्पलेट</a>

## पिछला पाठ

[Agentic RAG](../05-agentic-rag/README.md)

## अगला पाठ

[योजना डिजाइन पैटर्न](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->