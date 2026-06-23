[![विश्वसनीय AI एजेन्टहरू](../../../translated_images/ne/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(यो पाठको भिडियो हेर्न माथि रहेको चित्रमा क्लिक गर्नुहोस्)_

# विश्वसनीय AI एजेन्टहरू बनाउँदै

## परिचय

यस पाठमा समावेश हुनेछ:

- कसरी सुरक्षित र प्रभावकारी AI एजेन्ट बनाउन र तैनाथ गर्ने
- AI एजेन्टहरू विकास गर्दा महत्वपूर्ण सुरक्षा विचारहरू।
- AI एजेन्टहरू विकास गर्दा डाटा र प्रयोगकर्ता गोपनीयता कसरी कायम राख्ने।

## सिकाइ लक्ष्यहरू

यस पाठ पूरा गरेपछि, तपाईं जान्नुहुनेछ:

- AI एजेन्टहरू सिर्जना गर्दा जोखिमहरू पहिचान गर्ने र कम गर्ने।
- डाटा र पहुँच उचित रूपमा व्यवस्थापन गर्न सुरक्षा उपायहरू लागू गर्ने।
- डाटा गोपनीयता कायम राख्ने र गुणस्तरीय प्रयोगकर्ता अनुभव प्रदान गर्ने AI एजेन्टहरू सिर्जना गर्ने।

## सुरक्षा

पहिले सुरक्षित एजेन्टिक अनुप्रयोगहरू बनाउने कुरा हेरौं। सुरक्षा भनेको AI एजेन्टले डिजाइनअनुसार कार्य गर्नु हो। एजेन्टिक अनुप्रयोगहरूका विकासकर्ताहरूले सुरक्षा अधिकतम बनाउनका लागि विधि र उपकरणहरू छन्:

### सिस्टम सन्देश फ्रेमवर्क बनाउँदै

यदि तपाईंले कहिल्यै ठूलो भाषा मोडेलहरू (LLMs) प्रयोग गरेर AI अनुप्रयोग बनाउनु भएको छ भने, बलियो सिस्टम प्रम्प्ट वा सिस्टम सन्देश डिजाइनको महत्त्व थाहा पाउनु भएको छ। यी प्रम्प्टहरूले LLM कसरि प्रयोगकर्ता र डाटासँग अन्तरक्रिया गर्ने भन्ने मेटा नियम, निर्देशन र दिशानिर्देशहरू बनाउँछन्।

AI एजेन्टहरूको लागि सिस्टम प्रम्प्ट अझ महत्त्वपूर्ण हुन्छ किनभने AI एजेन्टहरूले हामीले डिजाइन गरेका कार्यहरू पूरा गर्न अत्यधिक विशिष्ट निर्देशनहरू आवश्यक हुन्छन्।

स्केलेबल सिस्टम प्रम्प्टहरू सिर्जना गर्न, हामीले हाम्रो अनुप्रयोगमा एक वा बढी एजेन्टहरू बनाउनको लागि सिस्टम सन्देश फ्रेमवर्क प्रयोग गर्न सक्छौं:

![सिस्टम सन्देश फ्रेमवर्क बनाउँदै](../../../translated_images/ne/system-message-framework.3a97368c92d11d68.webp)

#### चरण १: मेटा सिस्टम सन्देश सिर्जना गर्नुहोस्

मेटा प्रम्प्टलाई LLM ले हामीले सिर्जना गर्ने एजेन्टहरूको सिस्टम प्रम्प्टहरू उत्पादन गर्न प्रयोग गर्नेछ। यसलाई टेम्प्लेटको रूपमा डिजाइन गर्छौं ताकि आवश्यकता अनुसार धेरै एजेन्टहरू सजिलै बनाउन सकियोस्।

यहाँ मेटा सिस्टम सन्देशको एउटा उदाहरण छ जुन हामी LLM लाई दिनेछौं:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### चरण २: आधारभूत प्रम्प्ट सिर्जना गर्नुहोस्

अगामी चरणमा AI एजेन्टलाई वर्णन गर्ने आधारभूत प्रम्प्ट तयार गर्नुहोस्। तपाईंले एजेन्टको भूमिका, एजेन्टले पूरा गर्ने कार्यहरू, र एजेन्टका अन्य जिम्मेवारीहरू समावेश गर्नुपर्छ।

यहाँ एउटा उदाहरण छ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### चरण ३: LLM लाई आधारभूत सिस्टम सन्देश प्रदान गर्नुहोस्

अब हामी यो सिस्टम सन्देशलाई मेटा सिस्टम सन्देश र हाम्रो आधारभूत सिस्टम सन्देश प्रदान गरेर अनुकूलन गर्न सक्छौं।

यसले हामीले बनाउने AI एजेन्टहरूलाई मार्गदर्शन गर्न उपयुक्त सिस्टम सन्देश उत्पादन गर्नेछ:

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

#### चरण ४: पुनरावृत्ति गर्नुहोस् र सुधार गर्नुहोस्

यस सिस्टम सन्देश फ्रेमवर्कको मूल्य भनेको धेरै एजेन्टहरूको लागि सिस्टम सन्देशहरू सहजै सिर्जना गर्न र तपाईंकै सिस्टम सन्देशहरू समयसँगै सुधार गर्न सक्नु हो। प्राय: पहिलो पटक पूर्ण प्रयोग मामला लागि ठीक काम गर्ने सिस्टम सन्देश मिल्दैन। साना समायोजन गरेर आधारभूत सिस्टम सन्देश परिवर्तन गरी परिणामहरूको तुलना र मूल्याङ्कन गर्न सकिने हुनाले सुधार गर्न सकिन्छ।

## खतराको बुझाइ

विश्वसनीय AI एजेन्ट बनाउनका लागि तपाईंको AI एजेन्टमा भएका जोखिम र खतराहरू बुझ्न र कम गर्न जरूरी छ। AI एजेन्टहरूमा हुने केही खतराहरू भनेका के के हुन् र तिनीहरूका लागि कसरी योजना बनाउने र तयारी गर्ने भन्ने कुरा हेरौं।

![खतराको बुझाइ](../../../translated_images/ne/understanding-threats.89edeada8a97fc0f.webp)

### कार्य र निर्देशन

**वर्णन:** आक्रमणकारीहरूले AI एजेन्टका निर्देशनहरू वा लक्ष्यहरू परिवर्तन गर्ने प्रयास गर्दछन्, जसलाई प्रम्प्टिङ वा इनपुटहरूमा हेरफेर गरेर गर्छन्।

**कमजोर पक्ष व्यवस्थापन:** सम्भावित खतरनाक प्रम्प्टहरू पत्ता लगाउन मान्यताको जाँच र इनपुट फिल्टरहरू कार्यान्वयन गर्नुहोस्। यी आक्रमणहरू सामान्यतः वार्तालापमा बारम्बार अन्तर्क्रियाको आवश्यकता पर्ने भएकाले वार्तालापमा चरणहरूको संख्या सीमित पार्नु अर्को उपाय हो।

### संवेदनशील प्रणालीहरूमा पहुँच

**वर्णन:** यदि AI एजेन्टसँग संवेदनशील डाटा राख्ने प्रणाली र सेवाहरूमा पहुँच छ भने, आक्रमणकारीहरूले एजेन्ट र यी सेवाहरू बीचको सञ्चारमा सेंधमारी गर्न सक्छन्। यी सिधा आक्रमण वा एजेन्टमार्फत यी प्रणालीहरूको जानकारी लिन खोज्ने अप्रत्यक्ष प्रयास हुन सक्छ।

**कमजोर पक्ष व्यवस्थापन:** AI एजेन्टहरूले आवश्यकताको आधारमा मात्र सिस्टमहरूमा पहुँच पाउनुपर्छ। एजेन्ट र प्रणाली बीचको सञ्चार सुरक्षित हुनुपर्छ। प्रमाणीकरण र पहुँच नियन्त्रण लागू गर्नु जानकारी सुरक्षा गर्ने अर्को उपाय हो।

### स्रोत र सेवा ओभरलोडिंग

**वर्णन:** AI एजेन्टहरूले कार्य पूरा गर्न विभिन्न उपकरण र सेवाहरू प्रयोग गर्न सक्छन्। आक्रमणकारीहरूले यो क्षमता प्रयोग गरेर एआई एजेन्ट मार्फत धेरै रिक्वेस्टहरू पठाएर यी सेवाहरूमा आक्रमण गर्न सक्छन्, जसले प्रणाली फेल हुन सक्छ वा धेरै खर्च लाग्न सक्छ।

**कमजोर पक्ष व्यवस्थापन:** सेवा प्रति AI एजेन्टले गर्न सक्ने रिक्वेस्टहरूको संख्या सीमित गर्ने नीति लागू गर्नुहोस्। AI एजेन्टसँगको वार्तालाप चरणहरूको संख्या र रिक्वेस्टहरू सीमित गर्नु यी आक्रमणहरू रोक्ने अर्को तरिका हो।

### ज्ञान आधार विषाक्तता (Knowledge Base Poisoning)

**वर्णन:** यो प्रकारको आक्रमण सीधा AI एजेन्टमाथि नभई ज्ञान आधार र अन्य सेवाहरूमाथि लक्षित हुन्छ जुन AI एजेन्टले प्रयोग गर्नेछ। यसले एजेन्टलाई काम पूरा गर्दा प्रयोग हुने डाटा वा जानकारी भ्रष्ट पार्न सक्छ, जसले पूर्वाग्रही वा अनपेक्षित प्रतिक्रिया दिन सक्छ।

**कमजोर पक्ष व्यवस्थापन:** AI एजेन्टले काम गर्ने क्रममा प्रयोग गर्ने डाटाको नियमित जाँच गर्नुहोस्। यस डाटामा पहुँच सुरक्षित राख्नुहोस् र विश्वासिलो व्यक्तिहरूद्वारा मात्र परिवर्तन गर्न दिनुहोस् ताकि यस्तो प्रकारको आक्रमणबाट बच्न सकियोस्।

### संक्रमण त्रुटिहरू (Cascading Errors)

**वर्णन:** AI एजेन्टले विभिन्न उपकरण र सेवाहरू प्रयोग गर्छ। आक्रमणकारीहरूले सिर्जना गरेका त्रुटिहरूले अन्य प्रणालीहरूमा विफलता ल्याउन सक्छ, जसले आक्रमणलाई अझ फैलिने र समाधान गर्न गाह्रो बनाउँछ।

**कमजोर पक्ष व्यवस्थापन:** यसबाट बच्न AI एजेन्टलाई सीमित वातावरणमा सञ्चालन गराउने, जस्तै Docker कन्टेनरमा कार्यसम्पादन गर्ने व्यवस्था गर्नुहोस् ताकि सिधा प्रणाली आक्रमणबाट बच्न सकियोस्। कुनै प्रणालीले त्रुटि फर्काउँदा फ्यालब्याक म्याकानिजम र पुनः प्रयास गर्ने कार्यान्वयन अर्को उपाय हो।

## मानव-इन-द-ल्याप (Human-in-the-Loop)

विश्वसनीय AI एजेन्ट प्रणालीहरू बनाउन अर्को प्रभावकारी तरिका मानव-इन-द-ल्याप प्रयोग गर्नु हो। यसले यस्तो प्रक्रिया सिर्जना गर्छ जहाँ प्रयोगकर्ताहरू एजेन्टहरूलाई प्रतिक्रिया दिन सक्छन् दौडाइँको क्रममा। प्रयोगकर्ताहरू बहु-एजेन्ट प्रणालीमा एजेन्टको रूपमा काम गर्छन् र प्रक्रियाको अनुमोदन वा रोकेर समापन गर्न सक्छन्।

![लूपमा मानव](../../../translated_images/ne/human-in-the-loop.5f0068a678f62f4f.webp)

यहाँ Microsoft Agent Framework प्रयोग गरेर यस अवधारणा कसरी कार्यान्वयन गरिएको छ भन्ने कोड स्निपेट छ:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# मान्छे-इन-द-लूप अनुमोदनको साथ प्रदाता सिर्जना गर्नुहोस्
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# मान्छे अनुमोदन चरणसहित एजेन्ट सिर्जना गर्नुहोस्
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# प्रयोगकर्ताले प्रतिक्रिया समीक्षा गर्न र अनुमोदन गर्न सक्छन्
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## निष्कर्ष

विश्वसनीय AI एजेन्टहरू बनाउँदा सावधानीपूर्वक डिजाइन, बलियो सुरक्षा उपायहरू र निरन्तर पुनरावृत्तिको आवश्यकता पर्छ। संरचित मेटा प्रम्प्टिङ प्रणालीहरू लागू गरेर, सम्भावित खतराहरू बुझेर र कम गर्ने रणनीतिहरू लागू गरेर, विकासकर्ताहरू सुरक्षित र प्रभावकारी AI एजेन्टहरू बनाउन सक्छन्। थप रूपमा, मानव-इन-द-ल्याप दृष्टिकोण समावेश गर्दा AI एजेन्टहरूले प्रयोगकर्ता आवश्यकतासँग मिलेर जोखिम न्यूनिकरण गर्छन्। AI विकास हुँदै जाँदा सुरक्षा, गोपनीयता र नैतिक पक्षमा सक्रिय ध्यान राख्नु विश्वास र विश्वसनीयताको आधार हुनेछ।

## कोड नमूना

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): मेटा-प्रम्प्ट सिस्टम-सन्देश फ्रेमवर्कको चरणबद्ध प्रदर्शन।
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): विश्वसनीय एजेन्टहरूको लागि क्रियापूर्व अनुमोदन गेट, जोखिम स्तर र अडिट लगिङ।

### विश्वसनीय AI एजेन्टहरू निर्माण सम्बन्धी थप प्रश्नहरू छन्?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मा गई अन्य सिक्नेहरूसँग भेटघाट गर्नुहोस्, कार्यालय समयहरूमा सहभागी हुनुहोस् र आफ्नो AI एजेन्ट सम्बन्धी प्रश्नहरू समाधान गर्नुहोस्।

## थप स्रोतहरू

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">जिम्मेवार AI अवलोकन</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">सृजनात्मक AI मोडेलहरू र AI अनुप्रयोगहरूको मूल्याङ्कन</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">सुरक्षा सिस्टम सन्देशहरू</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">जोखिम मूल्याङ्कन टेम्प्लेट</a>

## अघिल्लो पाठ

[Agentic RAG](../05-agentic-rag/README.md)

## अर्को पाठ

[योजना डिजाइन ढाँचा](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->