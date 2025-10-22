<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T10:17:40+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "ne"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.ne.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(माथिको तस्बिरमा क्लिक गरेर यो पाठको भिडियो हेर्नुहोस्)_

# भरपर्दो एआई एजेन्टहरू निर्माण

## परिचय

यो पाठले समेट्नेछ:

- सुरक्षित र प्रभावकारी एआई एजेन्टहरू कसरी निर्माण गर्ने र तैनाथ गर्ने।
- एआई एजेन्टहरू विकास गर्दा ध्यान दिनुपर्ने महत्त्वपूर्ण सुरक्षा पक्षहरू।
- एआई एजेन्टहरू विकास गर्दा डाटा र प्रयोगकर्ताको गोपनीयता कसरी कायम राख्ने।

## सिकाइका लक्ष्यहरू

यो पाठ पूरा गरेपछि, तपाईंले जान्नुहुनेछ:

- एआई एजेन्टहरू सिर्जना गर्दा जोखिमहरू पहिचान र न्यूनीकरण गर्ने।
- डाटा र पहुँचलाई सही रूपमा व्यवस्थापन गर्न सुरक्षा उपायहरू कार्यान्वयन गर्ने।
- डाटा गोपनीयता कायम राख्ने र गुणस्तरीय प्रयोगकर्ता अनुभव प्रदान गर्ने एआई एजेन्टहरू सिर्जना गर्ने।

## सुरक्षा

सुरक्षित एजेन्टिक एप्लिकेसनहरू निर्माण गर्ने कुरा पहिले हेरौं। सुरक्षा भन्नाले एआई एजेन्टले डिजाइनअनुसार काम गर्ने सुनिश्चितता हो। एजेन्टिक एप्लिकेसनहरू निर्माण गर्ने क्रममा, हामीसँग सुरक्षा अधिकतम बनाउनका लागि विधिहरू र उपकरणहरू छन्:

### सिस्टम सन्देश फ्रेमवर्क निर्माण

यदि तपाईंले कहिल्यै ठूलो भाषा मोडेल (LLMs) प्रयोग गरेर एआई एप्लिकेसन निर्माण गर्नुभएको छ भने, तपाईंलाई बलियो सिस्टम प्रम्प्ट वा सिस्टम सन्देश डिजाइनको महत्त्व थाहा छ। यी प्रम्प्टहरूले LLM कसरी प्रयोगकर्ता र डाटासँग अन्तरक्रिया गर्ने भन्ने नियम, निर्देशन, र दिशानिर्देशहरू स्थापना गर्छन्।

एआई एजेन्टहरूको लागि, सिस्टम प्रम्प्ट अझ महत्त्वपूर्ण हुन्छ किनभने एआई एजेन्टहरूले हामीले डिजाइन गरेका कार्यहरू पूरा गर्न अत्यन्तै विशिष्ट निर्देशनहरू आवश्यक पर्छ।

स्केलेबल सिस्टम प्रम्प्टहरू सिर्जना गर्न, हामी हाम्रो एप्लिकेसनमा एक वा बढी एजेन्टहरू निर्माण गर्न प्रणाली सन्देश फ्रेमवर्क प्रयोग गर्न सक्छौं:

![सिस्टम सन्देश फ्रेमवर्क निर्माण](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.ne.png)

#### चरण १: मेटा सिस्टम सन्देश सिर्जना गर्नुहोस्

मेटा प्रम्प्ट LLM लाई हामीले सिर्जना गर्ने एजेन्टहरूको लागि सिस्टम प्रम्प्टहरू उत्पन्न गर्न प्रयोग गरिनेछ। हामी यसलाई टेम्प्लेटको रूपमा डिजाइन गर्छौं ताकि आवश्यक परेमा धेरै एजेन्टहरू कुशलतापूर्वक सिर्जना गर्न सकियोस्।

यहाँ मेटा सिस्टम सन्देशको उदाहरण छ जुन हामी LLM लाई दिनेछौं:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### चरण २: आधारभूत प्रम्प्ट सिर्जना गर्नुहोस्

अर्को चरण भनेको एआई एजेन्टलाई वर्णन गर्न आधारभूत प्रम्प्ट सिर्जना गर्नु हो। तपाईंले एजेन्टको भूमिका, एजेन्टले पूरा गर्ने कार्यहरू, र एजेन्टका अन्य जिम्मेवारीहरू समावेश गर्नुपर्छ।

यहाँ एउटा उदाहरण छ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### चरण ३: आधारभूत सिस्टम सन्देश LLM लाई प्रदान गर्नुहोस्

अब हामी मेटा सिस्टम सन्देशलाई सिस्टम सन्देशको रूपमा र हाम्रो आधारभूत सिस्टम सन्देशलाई प्रदान गरेर यो सिस्टम सन्देशलाई अनुकूलित गर्न सक्छौं।

यसले हाम्रो एआई एजेन्टहरूलाई मार्गदर्शन गर्न राम्रोसँग डिजाइन गरिएको सिस्टम सन्देश उत्पादन गर्नेछ:

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

#### चरण ४: पुनरावृत्ति र सुधार गर्नुहोस्

यस सिस्टम सन्देश फ्रेमवर्कको मूल्य भनेको धेरै एजेन्टहरूको लागि सिस्टम सन्देशहरू सिर्जना गर्न सजिलो बनाउनु र समयसँगै तपाईंको सिस्टम सन्देशहरू सुधार गर्नु हो। तपाईंको सम्पूर्ण प्रयोग केसको लागि पहिलो पटकमा काम गर्ने सिस्टम सन्देश पाउनु दुर्लभ हुन्छ। आधारभूत सिस्टम सन्देश परिवर्तन गरेर र प्रणाली मार्फत चलाएर साना समायोजनहरू र सुधारहरू गर्न सक्षम हुनुले तपाईंलाई परिणामहरूको तुलना र मूल्याङ्कन गर्न अनुमति दिन्छ।

## खतराहरू बुझ्दै

भरपर्दो एआई एजेन्टहरू निर्माण गर्न, तपाईंको एआई एजेन्टमा हुने जोखिम र खतराहरू बुझ्नु र न्यूनीकरण गर्नु महत्त्वपूर्ण छ। एआई एजेन्टहरूमा हुने विभिन्न खतराहरू र तिनीहरूलाई कसरी राम्रोसँग योजना र तयारी गर्न सकिन्छ भन्ने केही उदाहरणहरू हेरौं।

![खतराहरू बुझ्दै](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.ne.png)

### कार्य र निर्देशन

**विवरण:** आक्रमणकारीहरूले प्रम्प्टिङ वा इनपुटहरू हेरफेर गरेर एआई एजेन्टका निर्देशनहरू वा लक्ष्यहरू परिवर्तन गर्न प्रयास गर्छन्।

**निवारण:** एआई एजेन्टले प्रक्रिया गर्नु अघि सम्भावित खतरनाक प्रम्प्टहरू पत्ता लगाउन मान्यकरण जाँच र इनपुट फिल्टरहरू कार्यान्वयन गर्नुहोस्। यी आक्रमणहरू सामान्यतया एजेन्टसँग बारम्बार अन्तरक्रिया आवश्यक पर्ने भएकाले, कुराकानीको पालाहरू सीमित गर्नु अर्को रोकथाम उपाय हो।

### महत्त्वपूर्ण प्रणालीहरूको पहुँच

**विवरण:** यदि एआई एजेन्टसँग संवेदनशील डाटा भण्डारण गर्ने प्रणालीहरू र सेवाहरूमा पहुँच छ भने, आक्रमणकारीहरूले एजेन्ट र ती सेवाहरू बीचको सञ्चारलाई सम्झौता गर्न सक्छन्। यी प्रत्यक्ष आक्रमणहरू वा ती प्रणालीहरूको बारेमा जानकारी प्राप्त गर्न अप्रत्यक्ष प्रयासहरू हुन सक्छन्।

**निवारण:** एआई एजेन्टहरूले यी प्रकारका आक्रमणहरू रोक्न आवश्यक आधारमा मात्र प्रणालीहरूमा पहुँच पाउनुपर्छ। एजेन्ट र प्रणाली बीचको सञ्चार सुरक्षित हुनुपर्छ। प्रमाणीकरण र पहुँच नियन्त्रण कार्यान्वयन गर्नु अर्को सुरक्षा उपाय हो।

### स्रोत र सेवा ओभरलोडिङ

**विवरण:** एआई एजेन्टहरूले कार्यहरू पूरा गर्न विभिन्न उपकरणहरू र सेवाहरूमा पहुँच गर्न सक्छन्। आक्रमणकारीहरूले एआई एजेन्टमार्फत उच्च मात्रामा अनुरोधहरू पठाएर यी सेवाहरूलाई आक्रमण गर्न सक्छन्, जसले प्रणाली असफलता वा उच्च लागत निम्त्याउन सक्छ।

**निवारण:** एआई एजेन्टले सेवामा गर्न सक्ने अनुरोधहरूको संख्या सीमित गर्न नीतिहरू कार्यान्वयन गर्नुहोस्। एआई एजेन्टसँगको कुराकानीको पालाहरू र अनुरोधहरूको संख्या सीमित गर्नु अर्को रोकथाम उपाय हो।

### ज्ञान आधार विषाक्तता

**विवरण:** यो प्रकारको आक्रमणले एआई एजेन्टलाई प्रत्यक्ष रूपमा लक्षित गर्दैन तर ज्ञान आधार र अन्य सेवाहरूलाई लक्षित गर्छ जुन एआई एजेन्टले प्रयोग गर्नेछ। यसले डाटा वा जानकारीलाई बिगार्न समावेश गर्न सक्छ, जसले प्रयोगकर्तालाई पूर्वाग्रही वा अनपेक्षित प्रतिक्रिया दिन सक्छ।

**निवारण:** एआई एजेन्टले आफ्नो कार्यप्रवाहमा प्रयोग गर्ने डाटाको नियमित रूपमा प्रमाणीकरण गर्नुहोस्। यो डाटामा पहुँच सुरक्षित गर्नुहोस् र यो प्रकारको आक्रमण रोक्न विश्वासिला व्यक्तिहरूले मात्र परिवर्तन गर्न सक्ने सुनिश्चित गर्नुहोस्।

### क्यास्केडिङ त्रुटिहरू

**विवरण:** एआई एजेन्टहरूले कार्यहरू पूरा गर्न विभिन्न उपकरणहरू र सेवाहरूमा पहुँच गर्छन्। आक्रमणकारीहरूले गराएका त्रुटिहरूले एआई एजेन्टसँग जडित अन्य प्रणालीहरूको असफलता निम्त्याउन सक्छ, जसले आक्रमणलाई अझ व्यापक र समस्या समाधान गर्न गाह्रो बनाउँछ।

**निवारण:** यसलाई रोक्नको लागि एउटा विधि भनेको एआई एजेन्टलाई सीमित वातावरणमा सञ्चालन गराउनु हो, जस्तै डकर कन्टेनरमा कार्यहरू प्रदर्शन गर्नु, ताकि प्रत्यक्ष प्रणाली आक्रमणहरू रोक्न सकियोस्। फलब्याक मेकानिज्म र पुन: प्रयास गर्ने तर्क सिर्जना गर्नु अर्को उपाय हो जब निश्चित प्रणालीहरूले त्रुटिसहित प्रतिक्रिया दिन्छन्।

## मानव-इन-द-लूप

भरपर्दो एआई एजेन्ट प्रणालीहरू निर्माण गर्ने अर्को प्रभावकारी उपाय भनेको मानव-इन-द-लूप प्रयोग गर्नु हो। यसले प्रयोगकर्ताहरूलाई एजेन्टहरूको प्रक्रियामा प्रतिक्रिया प्रदान गर्न सक्षम बनाउने प्रवाह सिर्जना गर्छ। प्रयोगकर्ताहरूले बहु-एजेन्ट प्रणालीमा एजेन्टको रूपमा काम गर्छन् र चलिरहेको प्रक्रियाको स्वीकृति वा समाप्ति प्रदान गर्छन्।

![मानव-इन-द-लूप](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.ne.png)

यहाँ AutoGen प्रयोग गरेर यो अवधारणा कसरी कार्यान्वयन गरिन्छ भन्ने देखाउने कोड स्निपेट छ:

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

भरपर्दो एआई एजेन्टहरू निर्माण गर्न सावधानीपूर्वक डिजाइन, बलियो सुरक्षा उपायहरू, र निरन्तर पुनरावृत्ति आवश्यक पर्छ। संरचित मेटा प्रम्प्टिङ प्रणालीहरू कार्यान्वयन गरेर, सम्भावित खतराहरू बुझेर, र न्यूनीकरण रणनीतिहरू लागू गरेर, विकासकर्ताहरूले सुरक्षित र प्रभावकारी एआई एजेन्टहरू सिर्जना गर्न सक्छन्। साथै, मानव-इन-द-लूप दृष्टिकोणलाई समावेश गर्दा एआई एजेन्टहरूले प्रयोगकर्ताको आवश्यकतासँग मेल खाने सुनिश्चित गर्दछ र जोखिमहरू न्यूनतम बनाउँछ। एआई निरन्तर विकसित भइरहँदा, सुरक्षा, गोपनीयता, र नैतिक विचारहरूमा सक्रिय दृष्टिकोण कायम राख्नु एआई-चालित प्रणालीहरूमा विश्वास र विश्वसनीयता बढाउन महत्त्वपूर्ण हुनेछ।

### भरपर्दो एआई एजेन्टहरू निर्माणबारे थप प्रश्नहरू छन्?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) मा सामेल हुनुहोस्, अन्य सिक्नेहरूसँग भेट्नुहोस्, अफिस आवरहरूमा सहभागी हुनुहोस्, र तपाईंका एआई एजेन्टसम्बन्धी प्रश्नहरूको उत्तर पाउनुहोस्।

## थप स्रोतहरू

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">उत्तरदायी एआईको अवलोकन</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">जनरेटिभ एआई मोडेल र एआई एप्लिकेसनहरूको मूल्याङ्कन</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">सुरक्षा प्रणाली सन्देशहरू</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">जोखिम मूल्याङ्कन टेम्प्लेट</a>

## अघिल्लो पाठ

[एजेन्टिक RAG](../05-agentic-rag/README.md)

## अर्को पाठ

[योजना डिजाइन ढाँचा](../07-planning-design/README.md)

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।