<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c069d7ff0feca3027f88819355866ca1",
  "translation_date": "2025-04-05T19:49:30+00:00",
  "source_file": "06-building-trustworthy-agents\\README.md",
  "language_code": "hi"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.74ea485dbd9a9c3fb4c749f30f2b8130d025072b4d7d911c6f540eac5a78e6b8.hi.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(ऊपर दी गई तस्वीर पर क्लिक करें इस पाठ का वीडियो देखने के लिए)_

# भरोसेमंद AI एजेंट बनाना

## परिचय

इस पाठ में शामिल हैं:

- सुरक्षित और प्रभावी AI एजेंट कैसे बनाएं और तैनात करें।
- AI एजेंट विकसित करते समय महत्वपूर्ण सुरक्षा विचार।
- AI एजेंट विकसित करते समय डेटा और उपयोगकर्ता गोपनीयता कैसे बनाए रखें।

## सीखने के लक्ष्य

इस पाठ को पूरा करने के बाद, आप जान पाएंगे:

- AI एजेंट बनाते समय जोखिमों की पहचान और उन्हें कम करना।
- सुरक्षा उपाय लागू करना ताकि डेटा और पहुंच सही तरीके से प्रबंधित हो।
- ऐसे AI एजेंट बनाना जो डेटा गोपनीयता बनाए रखें और उपयोगकर्ता अनुभव की गुणवत्ता प्रदान करें।

## सुरक्षा

चलो पहले सुरक्षित एजेंटिक एप्लिकेशन बनाने की बात करते हैं। सुरक्षा का मतलब है कि AI एजेंट अपने डिजाइन के अनुसार काम करता है। एजेंटिक एप्लिकेशन बनाने वालों के रूप में, हमारे पास सुरक्षा को अधिकतम करने के लिए तरीके और उपकरण होते हैं:

### सिस्टम संदेश फ्रेमवर्क बनाना

यदि आपने कभी बड़े भाषा मॉडल (LLMs) का उपयोग करके AI एप्लिकेशन बनाया है, तो आप जानते हैं कि मजबूत सिस्टम प्रॉम्प्ट या सिस्टम संदेश डिज़ाइन करना कितना महत्वपूर्ण है। ये प्रॉम्प्ट उपयोगकर्ता और डेटा के साथ LLM के इंटरैक्शन के लिए नियम, निर्देश और दिशानिर्देश स्थापित करते हैं।

AI एजेंटों के लिए, सिस्टम प्रॉम्प्ट और भी महत्वपूर्ण है क्योंकि AI एजेंटों को उन कार्यों को पूरा करने के लिए अत्यधिक विशिष्ट निर्देशों की आवश्यकता होती है जिन्हें हमने उनके लिए डिज़ाइन किया है।

स्केलेबल सिस्टम प्रॉम्प्ट बनाने के लिए, हम अपने एप्लिकेशन में एक या अधिक एजेंट बनाने के लिए सिस्टम संदेश फ्रेमवर्क का उपयोग कर सकते हैं:

![सिस्टम संदेश फ्रेमवर्क बनाना](../../../translated_images/system-message-framework.9df67f3d863520cd48878f71a1289740d8cb46e9d63ee065090ccf3b9b6b82a1.hi.png)

#### चरण 1: मेटा सिस्टम संदेश बनाएं 

मेटा प्रॉम्प्ट का उपयोग LLM द्वारा उन एजेंटों के सिस्टम प्रॉम्प्ट उत्पन्न करने के लिए किया जाएगा जिन्हें हम बनाते हैं। हम इसे एक टेम्पलेट के रूप में डिज़ाइन करते हैं ताकि यदि आवश्यक हो तो हम कुशलतापूर्वक कई एजेंट बना सकें।

यहां एक उदाहरण है कि हम LLM को क्या मेटा सिस्टम संदेश देंगे:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### चरण 2: एक बेसिक प्रॉम्प्ट बनाएं

अगला चरण AI एजेंट का वर्णन करने के लिए एक बेसिक प्रॉम्प्ट बनाना है। इसमें एजेंट की भूमिका, एजेंट द्वारा पूरे किए जाने वाले कार्य और एजेंट की अन्य जिम्मेदारियों को शामिल करना चाहिए।

यहां एक उदाहरण है:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### चरण 3: LLM को बेसिक सिस्टम संदेश प्रदान करें

अब हम इस सिस्टम संदेश को अनुकूलित कर सकते हैं, मेटा सिस्टम संदेश को सिस्टम संदेश के रूप में और हमारे बेसिक सिस्टम संदेश को प्रदान करके।

यह एक बेहतर डिज़ाइन किया गया सिस्टम संदेश उत्पन्न करेगा जो हमारे AI एजेंटों को निर्देशित करने के लिए उपयोगी होगा:

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

#### चरण 4: दोहराएं और सुधारें

इस सिस्टम संदेश फ्रेमवर्क का मूल्य यह है कि यह कई एजेंटों के लिए सिस्टम संदेश बनाना आसान बनाता है और समय के साथ आपके सिस्टम संदेशों को सुधारने में मदद करता है। यह दुर्लभ है कि आपका सिस्टम संदेश पहली बार में आपके पूरे उपयोग के मामले के लिए काम करेगा। बेसिक सिस्टम संदेश में छोटे बदलाव और सुधार करके और इसे सिस्टम के माध्यम से चलाकर आप परिणामों की तुलना और मूल्यांकन कर सकते हैं।

## खतरों को समझना

भरोसेमंद AI एजेंट बनाने के लिए, आपके AI एजेंट के जोखिमों और खतरों को समझना और उन्हें कम करना महत्वपूर्ण है। चलो AI एजेंटों के लिए केवल कुछ अलग-अलग खतरों को देखते हैं और आप उनके लिए बेहतर योजना और तैयारी कैसे कर सकते हैं।

![खतरों को समझना](../../../translated_images/understanding-threats.f8fbe6fe11e025b3085fc91e82d975937ad1d672260a2aeed40458aa41798d0e.hi.png)

### कार्य और निर्देश

**विवरण:** हमलावर AI एजेंट के निर्देशों या लक्ष्यों को प्रॉम्प्टिंग या इनपुट में बदलाव करके बदलने का प्रयास करते हैं।

**मिटिगेशन:** इनपुट फ़िल्टर और वैलिडेशन चेक लागू करें ताकि संभावित खतरनाक प्रॉम्प्ट को AI एजेंट द्वारा संसाधित होने से पहले ही पता लगाया जा सके। चूंकि इन हमलों के लिए आमतौर पर एजेंट के साथ बार-बार बातचीत की आवश्यकता होती है, बातचीत में टर्न की संख्या सीमित करना इन प्रकार के हमलों को रोकने का एक और तरीका है।

### महत्वपूर्ण सिस्टम तक पहुंच

**विवरण:** यदि AI एजेंट के पास संवेदनशील डेटा संग्रहीत करने वाली सिस्टम और सेवाओं तक पहुंच है, तो हमलावर एजेंट और इन सेवाओं के बीच संचार से समझौता कर सकते हैं। ये सीधे हमले हो सकते हैं या एजेंट के माध्यम से इन सिस्टम के बारे में जानकारी प्राप्त करने के अप्रत्यक्ष प्रयास हो सकते हैं।

**मिटिगेशन:** AI एजेंट को केवल आवश्यकतानुसार ही सिस्टम तक पहुंच प्रदान करें ताकि इन प्रकार के हमलों को रोका जा सके। एजेंट और सिस्टम के बीच संचार भी सुरक्षित होना चाहिए। प्रमाणन और पहुंच नियंत्रण लागू करना इस जानकारी को सुरक्षित रखने का एक और तरीका है।

### संसाधन और सेवा ओवरलोडिंग

**विवरण:** AI एजेंट विभिन्न टूल और सेवाओं तक पहुंच सकते हैं ताकि कार्य पूरे कर सकें। हमलावर इस क्षमता का उपयोग करके इन सेवाओं पर AI एजेंट के माध्यम से उच्च मात्रा में अनुरोध भेज सकते हैं, जिससे सिस्टम विफलताओं या उच्च लागतें हो सकती हैं।

**मिटिगेशन:** ऐसी नीतियां लागू करें जो किसी सेवा के लिए AI एजेंट द्वारा किए जाने वाले अनुरोधों की संख्या को सीमित करें। बातचीत में टर्न और आपके AI एजेंट को किए जाने वाले अनुरोधों की संख्या को सीमित करना इन प्रकार के हमलों को रोकने का एक और तरीका है।

### ज्ञान आधार में जहर

**विवरण:** इस प्रकार का हमला सीधे AI एजेंट को लक्षित नहीं करता बल्कि ज्ञान आधार और अन्य सेवाओं को लक्षित करता है जिनका उपयोग AI एजेंट करेगा। इसमें उस डेटा या जानकारी को दूषित करना शामिल हो सकता है जिसका उपयोग AI एजेंट कार्य पूरा करने के लिए करेगा, जिससे उपयोगकर्ता को पक्षपातपूर्ण या अनपेक्षित प्रतिक्रियाएं मिल सकती हैं।

**मिटिगेशन:** उस डेटा का नियमित रूप से सत्यापन करें जिसका उपयोग AI एजेंट अपने वर्कफ़्लो में करेगा। सुनिश्चित करें कि इस डेटा तक पहुंच सुरक्षित है और इसे केवल विश्वसनीय व्यक्तियों द्वारा बदला जा सकता है ताकि इस प्रकार के हमले से बचा जा सके।

### कैस्केडिंग त्रुटियां

**विवरण:** AI एजेंट विभिन्न टूल और सेवाओं तक पहुंचते हैं ताकि कार्य पूरे कर सकें। हमलावरों द्वारा उत्पन्न त्रुटियां उन अन्य सिस्टम की विफलताओं का कारण बन सकती हैं जिनसे AI एजेंट जुड़ा हुआ है, जिससे हमला अधिक व्यापक और समस्या को हल करना अधिक कठिन हो जाता है।

**मिटिगेशन:** इस समस्या से बचने का एक तरीका यह है कि AI एजेंट को सीमित वातावरण में संचालित करें, जैसे कि डॉकर कंटेनर में कार्यों को पूरा करना, ताकि सीधे सिस्टम हमलों से बचा जा सके। जब कुछ सिस्टम त्रुटि के साथ प्रतिक्रिया करते हैं, तो बैकअप तंत्र और पुनः प्रयास लॉजिक बनाना बड़ी सिस्टम विफलताओं को रोकने का एक और तरीका है।

## ह्यूमन-इन-द-लूप

भरोसेमंद AI एजेंट सिस्टम बनाने का एक और प्रभावी तरीका ह्यूमन-इन-द-लूप का उपयोग करना है। यह एक प्रवाह बनाता है जहां उपयोगकर्ता रन के दौरान एजेंटों को प्रतिक्रिया प्रदान कर सकते हैं। उपयोगकर्ता मूल रूप से एक मल्टी-एजेंट सिस्टम में एजेंटों के रूप में कार्य करते हैं और चल रही प्रक्रिया को स्वीकृति या समाप्ति प्रदान करते हैं।

![ह्यूमन-इन-द-लूप](../../../translated_images/human-in-the-loop.e9edbe8f6d42041b4213421410823250aa750fe8bdba5601d69ed46f3ff6489d.hi.png)

यहां AutoGen का उपयोग करके इस अवधारणा को लागू करने का एक कोड स्निपेट है:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## निष्कर्ष

भरोसेमंद AI एजेंट बनाना सावधानीपूर्वक डिज़ाइन, मजबूत सुरक्षा उपाय, और लगातार सुधार की आवश्यकता है। संरचित मेटा प्रॉम्प्टिंग सिस्टम को लागू करके, संभावित खतरों को समझकर, और शमन रणनीतियों को लागू करके, डेवलपर्स सुरक्षित और प्रभावी AI एजेंट बना सकते हैं। इसके अलावा, ह्यूमन-इन-द-लूप दृष्टिकोण को शामिल करना यह सुनिश्चित करता है कि AI एजेंट उपयोगकर्ता की आवश्यकताओं के साथ संरेखित रहें और जोखिमों को कम करें। जैसे-जैसे AI विकसित होता है, सुरक्षा, गोपनीयता और नैतिक विचारों पर सक्रिय रुख बनाए रखना AI-संचालित सिस्टम में विश्वास और विश्वसनीयता को बढ़ावा देने की कुंजी होगी।

## अतिरिक्त संसाधन

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Responsible AI का अवलोकन</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">जनरेटिव AI मॉडल और AI एप्लिकेशन का मूल्यांकन</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">सुरक्षा सिस्टम संदेश</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">जोखिम मूल्यांकन टेम्पलेट</a>

## पिछला पाठ

[Agentic RAG](../05-agentic-rag/README.md)

## अगला पाठ

[Planning Design Pattern](../07-planning-design/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।