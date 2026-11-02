[![विश्वसनीय AI एजेन्टहरू](../../../translated_images/ne/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(यो पाठको भिडियो हेर्न माथिको तस्बिरमा क्लिक गर्नुहोस्)_

# विश्वसनीय AI एजेन्टहरू बनाउँदै

## परिचय

यस पाठले समेट्ने विषयहरू:

- सुरक्षित र प्रभावकारी AI एजेन्टहरू कसरी बनाउने र लागू गर्ने
- AI एजेन्टहरू विकास गर्दा महत्त्वपूर्ण सुरक्षा विचारहरू।
- AI एजेन्टहरू विकास गर्दा डाटा र प्रयोगकर्ता गोपनीयता कसरी कायम गर्ने।

## सिकाइका लक्ष्यहरू

यस पाठ पूरा गरेपछि, तपाईं जान्नु हुनेछ कि:

- AI एजेन्टहरू सिर्जना गर्दा जोखिमहरू पहिचान र घटाउने।
- डाटा र पहुँचलाई सही तरिकाले व्यवस्थापन गर्न सुरक्षा उपायहरू कार्यान्वयन गर्ने।
- यस्ता AI एजेन्टहरू सिर्जना गर्ने जसले डाटा गोपनीयता कायम राख्छ र गुणस्तरीय प्रयोगकर्ता अनुभव दिन्छ।

## सुरक्षा

पहिले सुरक्षित एजेन्टिक अनुप्रयोगहरू बनाउन हेरौं। सुरक्षा भनेको AI एजेन्टले डिजाइन अनुसार काम गर्ने हो। एजेन्टिक अनुप्रयोगहरूका निर्माताहरूका रूपमा हामीसँग सुरक्षा अधिकतम बनाउन विधिहरू र उपकरणहरू छन्:

### प्रणाली सन्देश फ्रेमवर्क निर्माण गर्नु

यदि तपाईंले कहिल्यै ठूलो भाषाई मोडेल (LLMs) प्रयोग गरेर AI अनुप्रयोग बनाउनु भएको छ भने, तपाईंलाई प्रणाली प्रॉम्प्ट वा प्रणाली सन्देश डिजाइन गर्नको महत्त्व थाहा छ। यी प्रॉम्प्टहरूले LLM प्रयोगकर्ता र डाटासँग कसरी अन्तरक्रिया गर्ने भनेर मेटा नियमहरू, निर्देशनहरू, र दिशानिर्देशहरू स्थापना गर्छन्।

AI एजेन्टहरूको लागि, प्रणाली प्रॉम्प्ट अझै महत्त्वपूर्ण हुन्छ किनकि AI एजेन्टहरूले हाम्रो डिजाइन गरिएका कार्यहरू पूरा गर्न उच्च विशिष्ट निर्देशनहरू चाहिन्छ।

स्केलेबल प्रणाली प्रॉम्प्टहरू बनाउन, हामी हाम्रो अनुप्रयोगमा एक वा धेरै एजेन्टहरू निर्माण गर्न प्रणाली सन्देश फ्रेमवर्क प्रयोग गर्न सक्छौं:

![प्रणाली सन्देश फ्रेमवर्क निर्माण](../../../translated_images/ne/system-message-framework.3a97368c92d11d68.webp)

#### चरण १: एक मेटा प्रणाली सन्देश सिर्जना गर्नुहोस् 

मेटा प्रॉम्प्टलाई LLM एजेन्टहरूको प्रणाली प्रॉम्प्टहरु उत्पादन गर्न प्रयोग गर्नेछ। हामी यसलाई टेम्प्लेटको रूपमा डिजाइन गर्छौं जसले आवश्यक भएमा धेरै एजेन्टहरू सजिलै सिर्जना गर्न सक्षम बनाउँछ।

यहाँ LLM लाई दिने एउटा मेटा प्रणाली सन्देशको उदाहरण छ:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### चरण २: एउटा आधारभूत प्रॉम्प्ट सिर्जना गर्नुहोस्

अर्को चरण AI एजेन्ट वर्णन गर्ने आधारभूत प्रॉम्प्ट बनाउनु हो। तपाईंले एजेन्टको भूमिका, एजेन्टले पूरा गर्ने कार्यहरू, र एजेन्टका अरू जिम्मेवारीहरू समावेश गर्नुपर्छ।

यहाँ एउटा उदाहरण छ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### चरण ३: आधारभूत प्रणाली सन्देश LLM लाई प्रदान गर्नुहोस्

अब हामी यस प्रणाली सन्देशलाई मेटा प्रणाली सन्देश र हाम्रो आधारभूत प्रणाली सन्देश प्रदान गरेर अनुकूलित गर्न सक्छौं।

यसले हाम्रो AI एजेन्टहरूलाई मार्गदर्शन गर्न राम्रो डिजाइन गरिएको प्रणाली सन्देश उत्पादन गर्नेछ:

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

#### चरण ४: दोहोर्याउनुहोस् र सुधार गर्नुहोस्

यस प्रणाली सन्देश फ्रेमवर्कको मूल्य स्केलेबल रूपमा धेरै एजेन्टका लागि प्रणाली सन्देशहरू बनाई सजिलो बनाउनु मात्र होइन, समयसँगै प्रणाली सन्देशहरू सुधार गर्नु पनि हो। तपाईंको पूरै प्रयोग केसका लागि पहिलो पटक काम गर्ने प्रणाली सन्देश पाउनु दुर्लभ हुन्छ। साना परिवर्तनहरू र सुधारहरू गर्दा आधारभूत प्रणाली सन्देश परिमार्जन गरी पुन: चलाएर परिणामहरूको तुलना र मूल्यांकन गर्न सकिन्छ।

## खतरा बुझ्नुहोस्

विश्वसनीय AI एजेन्ट बनाउन, तपाईंको AI एजेन्टलाई हुने जोखिम र खतरा बुझ्नु र घटाउनु महत्त्वपूर्ण छ। AI एजेन्टहरूलाई हुने केही खतरा र तिनीहरूका लागि तयारी गर्ने तरिकाहरूमा हेरौं।

![खतरा बुझ्न](../../../translated_images/ne/understanding-threats.89edeada8a97fc0f.webp)

### कार्य र निर्देशन

**विवरण:** आक्रमणकारीहरूले AI एजेन्टका निर्देशन वा उद्देश्य परिवर्तन गर्न प्रॉम्प्टिङ वा इनपुटहरूमा हेरफेर गर्ने प्रयास गर्छन्।

**न्युनीकरण:** सम्भावित खतरनाक प्रॉम्प्टहरू AI एजेन्टले प्रक्रिया गर्नु अघि मान्यकरण चेकहरू र इनपुट फिल्टरहरू लागू गर्नुहोस्। यी आक्रमणहरूले प्रायः एजेण्टसँग बारम्बार अन्तरक्रिया चाहन्छन्, त्यसैले कुराकानीको संख्या सीमित गर्नु अर्को रोकथाम विधि हो।

### संवेदनशील प्रणालीहरूको पहुँच

**विवरण:** यदि AI एजेन्टसँग संवेदनशील डाटा भण्डारण गर्ने प्रणाली र सेवाहरूको पहुँच छ भने, आक्रमणकारीहरूले एजेन्ट र ती सेवाहरू बीचको सञ्चारमा पहुँच पाउन सक्छन्। यो प्रत्यक्ष आक्रमण वा एजेन्टमार्फत तिनीहरूका बारेमा सूचना प्राप्ति प्रयास हुन सक्छ।

**न्युनीकरण:** यी प्रकारका आक्रमणबाट बच्न AI एजेन्टहरूलाई आवश्यक पर्दा मात्र प्रणालीहरूले पहुँच दिनुहोस्। एजेन्ट र प्रणालीबीचको सञ्चार पनि सुरक्षित हुनुपर्छ। प्रमाणीकरण र पहुँच नियन्त्रण कार्यान्वयन गर्नु अर्को संरक्षण विधि हो।

### स्रोत र सेवा भार बढी हुनु

**विवरण:** AI एजेन्टहरूले विभिन्न उपकरण र सेवाहरू पहुँच गरेर कार्य पूरा गर्छन्। आक्रमणकारीहरूले AI एजेन्टमार्फत धेरै अनुरोधहरू पठाएर यी सेवाहरूमाथि आक्रमण गर्न सक्छन्, जसले प्रणाली विफलता वा महँगो लागत निम्त्याउन सक्छ।

**न्युनीकरण:** AI एजेन्टले सेवामा गर्ने अनुरोधहरूको संख्या सीमित गर्ने नीतिहरू लागू गर्नुहोस्। कुराकानीको चरण र अनुरोधहरूको संख्या सीमित गर्नु अर्को रोकथाम हो।

### ज्ञान आधार विषाक्तता

**विवरण:** यो आक्रमण AI एजेन्टलाई सिधै लक्षित गर्दैन, तर एजेन्टले प्रयोग गर्ने ज्ञान आधार र अन्य सेवाहरूलाई लक्षित गर्छ। यसले एजेन्टले कार्य पुरा गर्न प्रयोग गर्ने डाटा वा सूचना दूषित पार्न सक्छ, जसले पक्षपाती वा अनपेक्षित प्रतिक्रिया दिन सक्छ।

**न्युनीकरण:** एजेन्टले प्रयोग गर्ने डाटाको नियमित जाँच गर्नुहोस्। पहुँच सुरक्षित राख्नुहोस् र विश्वासिल व्यक्तिहरूद्वारा मात्र डाटा परिवर्तन गर्न दिनुहोस् ताकि यस्तो प्रकारको आक्रमण नहोस्।

### साङ्लो गल्तीहरू

**विवरण:** AI एजेन्टहरूले कार्य पुरा गर्न विभिन्न उपकरण र सेवाहरू पहुँच गर्छन्। आक्रमणकारीहरूले कारण बनाएका त्रुटिहरूले अन्य प्रणालीहरूमा विफलता निम्त्याउन सक्छ जसलाई AI एजेन्ट जोडिएको हुन्छ, जसले आक्रमणलाई व्यापक र समस्या समाधान गर्न गाह्रो बनाउँछ।

**न्युनीकरण:** यसलाई रोक्नको लागि AI एजेन्टलाई सीमित वातावरणमा चलाउने (जस्तो कि Docker कन्टेनरमा कार्य गर्नु) राम्रो हुन्छ जसले प्रत्यक्ष प्रणाली आक्रमण रोक्छ। केही प्रणाली त्रुटि प्रतिक्रिया गर्दा फेलब्याक मिक्यानिजम र पुन: प्रयास लॉजिक सिर्जना गर्नु अर्को उपाय हो।

## मानव-द्वारा-चक्र

अर्को प्रभावकारी तरिका विश्वसनीय AI एजेन्ट प्रणाली बनाउने भनेको मानव-द्वारा-चक्र प्रयोग गर्नु हो। यसले यस्तो प्रवाह सिर्जना गर्छ जहाँ प्रयोगकर्ताहरूले एजेण्टहरूलाई प्रतिक्रिया दिन सक्दछन्। प्रयोगकर्ताहरू बहु-एजेन्ट प्रणालीमा एजेन्टको भूमिका निर्वाह गर्दछन् र प्रक्रिया स्वीकृति वा समाप्ति प्रदान गर्दछन्।

![मानव चक्रमा](../../../translated_images/ne/human-in-the-loop.5f0068a678f62f4f.webp)

यहाँ Microsoft Agent Framework प्रयोग गरी यो अवधारणा कसरी लागू गरिन्छ भन्ने कोड टुक्रा छ:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# मानव-इन-दी-लूप स्वीकृतिसहित प्रदायक सिर्जना गर्नुहोस्
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# मानव स्वीकृति चरणसहित एजेन्ट सिर्जना गर्नुहोस्
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# प्रयोगकर्ताले प्रतिक्रिया समीक्षा गर्न र स्वीकृत गर्न सक्छन्
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## निष्कर्ष

विश्वसनीय AI एजेन्टहरू बनाउन सावधानीपूर्वक डिजाइन, मजबूत सुरक्षा उपायहरू, र निरन्तर iteration आवश्यक छ। संरचित मेटा प्रॉम्प्टिङ प्रणालीहरू लागू गरेर, सम्भावित खतरा बुझेर, र न्युनीकरण रणनीतिहरू लागू गरेर, बिकासकर्ताहरूले सुरक्षित र प्रभावकारी AI एजेन्टहरू सिर्जना गर्न सक्छन्। यसबाहेक, मानव-द्वारा-चक्र दृष्टिकोण समावेश गर्दा AI एजेन्टहरू प्रयोगकर्ता आवश्यकतासँग अनुकूल रहन्छन् र जोखिम घट्छ। AI बढ्दै जाँदा सुरक्षा, गोपनीयता, र नैतिक विचारहरूमा सक्रिय स्थिति राख्नु विश्वसनीयता र भरोसा कायम गर्न मुख्य हुनेछ।

## कोड नमूनाहरू

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): मेटा-प्रॉम्प्ट प्रणाली-सन्देश फ्रेमवर्कको चरणबद्ध डेमोन्ट्रेशन।
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): पूर्व-कार्य स्वीकृति गेटहरू, जोखिम स्तरीकरण, र विश्वसनीय एजेण्टहरूको लागि अडिट लगिङ।

### विश्वसनीय AI एजेन्टहरू बनाउने बारे थप प्रश्नहरू?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) मा सहभागी हुनुहोस् जहाँ तपाईं अन्य सिक्नेहरूलाई भेट्न, अफिस आवर्समा जान, र AI एजेन्टहरू सम्बन्धी प्रश्नहरूको उत्तर प्राप्त गर्न सक्नुहुन्छ।

## थप स्रोतहरू

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">जिम्मेवार AI अवलोकन</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">जेनेरेटिभ AI मोडेलहरू र AI अनुप्रयोगहरूको मूल्यांकन</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">सुरक्षा प्रणाली सन्देशहरू</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">जोखिम मूल्याङ्कन ढाँचा</a>

## अघिल्लो पाठ

[Agentic RAG](../05-agentic-rag/README.md)

## अर्को पाठ

[योजना डिजाइन ढाँचा](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->