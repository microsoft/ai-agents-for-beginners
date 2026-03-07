[![विश्वसनीय AI एजेन्टहरू](../../../translated_images/ne/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(यो पाठको भिडियो हेर्न माथिको छविमा क्लिक गर्नुहोस्)_

# विश्वसनीय AI एजेन्टहरू निर्माण गर्दै

## परिचय

यो पाठमा समावेश हुनेछ:

- कसरी सुरक्षित र प्रभावकारी AI एजेन्टहरू निर्माण र प्रवर्तन गर्ने
- AI एजेन्टहरू विकास गर्दा महत्वपूर्ण सुरक्षा विचारहरू।
- AI एजेन्टहरू विकास गर्दा डाटा र प्रयोगकर्ता गोपनीयता कसरी कायम गर्ने।

## सिकाइ लक्ष्यहरू

यो पाठ पूरा गरेपछि, तपाईं जान्नु हुनेछ:

- AI एजेन्टहरू सिर्जना गर्दा जोखिमहरू पहिचान र न्यूनीकरण कसरी गर्ने।
- डाटा र पहुँचलाई उचित रूपमा व्यवस्थापन गर्न सुरक्षा उपायहरू कसरी लागू गर्ने।
- डाटा गोपनीयता कायम राख्ने र गुणस्तरीय प्रयोगकर्ता अनुभव प्रदान गर्ने AI एजेन्टहरू कसरी सिर्जना गर्ने।

## सुरक्षा

पहिला सुरक्षित एजेण्टिक अनुप्रयोगहरू निर्माण गर्ने कुरा हेरौं। सुरक्षा भन्नाले AI एजेन्टले डिजाइन अनुसार काम गर्नुलाई जनाउँछ। एजेण्टिक अनुप्रयोगहरूका निर्माताहरूका रूपमा, हामीसँग सुरक्षा अधिकतम गर्नका लागि विधिहरू र उपकरणहरू छन्:

### सिस्टम मेसेज फ्रेमवर्क बनाउँदै

यदि तपाईंले कहिल्यै ठूला भाषा मोडेलहरू (LLMs) प्रयोग गरेर AI अनुप्रयोग निर्माण गर्नुभएको छ भने, शक्तिशाली सिस्टम प्रॉम्प्ट वा सिस्टम मेसेज डिजाइनको महत्त्व तपाईंलाई थाहा छ। यी प्रॉम्प्टहरूले LLM प्रयोगकर्ता र डाटासँग कसरी अन्तरक्रिया गर्ने भनेर मेटा नियम, निर्देशनहरू र मार्गनिर्देशनहरू स्थापना गर्छन्।

AI एजेन्टहरूको लागि, सिस्टम प्रॉम्प्ट बढी महत्त्वपूर्ण हुन्छ किनकि AI एजेन्टहरूले हामीले डिजाइन गरेको कार्यहरू पूरा गर्न अत्यन्त विशिष्ट निर्देशनहरू आवश्यक पर्छ।

स्केलेबल सिस्टम प्रॉम्प्टहरू सिर्जना गर्न, हामी हाम्रो अनुप्रयोगमा एक वा धेरै एजेन्टहरू निर्माण गर्न सिस्टम मेसेज फ्रेमवर्क प्रयोग गर्न सक्छौं:

![सिस्टम मेसेज फ्रेमवर्क बनाउँदै](../../../translated_images/ne/system-message-framework.3a97368c92d11d68.webp)

#### चरण १: मेटा सिस्टम मेसेज सिर्जना गर्नुहोस्

मेटा प्रॉम्प्टलाई LLM द्वारा हामीले सिर्जना गर्ने एजेन्टहरूको लागि सिस्टम प्रॉम्प्टहरू उत्पादन गर्न प्रयोग गरिनेछ। हामी यसलाई टेम्पलेटको रूपमा डिजाइन गर्छौं ताकि आवश्यक परे एकै साथ धेरै एजेन्टहरू प्रभावकारी रूपमा सिर्जना गर्न सकियोस्।

यहाँ LLM लाई दिने एउटा मेटा सिस्टम मेसेज उदाहरण छ:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### चरण २: आधारभूत प्रॉम्प्ट सिर्जना गर्नुहोस्

अर्को चरणमा AI एजेन्टलाई वर्णन गर्ने आधारभूत प्रॉम्प्ट सिर्जना गर्ने हो। तपाईंले एजेन्टको भूमिका, एजेन्टले पूरा गर्ने कार्यहरू, र एजेन्टका अन्य जिम्मेवारीहरू समावेश गर्नुपर्नेछ।

यहाँ एउटा उदाहरण छ:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### चरण ३: LLM लाई आधारभूत सिस्टम मेसेज प्रदान गर्नुहोस्

अब हामी यस सिस्टम मेसेजलाई मेटा सिस्टम मेसेजलाई सिस्टम मेसेजको रूपमा र हाम्रो आधारभूत सिस्टम मेसेजलाई प्रदान गरेर अनुकूलित गर्न सक्छौं।

यसले हाम्रो AI एजेन्टहरू मार्गदर्शन गर्न अझ राम्रो डिजाइन गरिएको सिस्टम मेसेज उत्पादन गर्नेछ:

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

#### चरण ४: पुनरावृति र सुधार गर्नुहोस्

यस सिस्टम मेसेज फ्रेमवर्कको मूल्य विभिन्न एजेन्टहरूबाट प्रणाली मेसेजहरू सिर्जना गर्न सजिलो बनाउनु हो साथै तपाईंका सिस्टम मेसेजहरूको समयसँग सुधार गर्नु हो। पहिलो पटक तपाईंको पूर्ण प्रयोग केसका लागि काम गर्ने सिस्टम मेसेज पाउनु दुर्लभ हुन्छ। साना समायोजनहरू र सुधारहरू गर्न सक्नु भनेको आधारभूत सिस्टम मेसेज परिवर्तन गरेर र प्रणालीमार्फत चलाएर नतिजाहरू तुलना र मूल्यांकन गर्न सक्नु हो।

## खतरा बुझ्दै

विश्वसनीय AI एजेन्टहरू निर्माण गर्न तपाईंको AI एजेन्टमाथि जोखिम र खतराहरू बुझ्नु र न्यूनीकरण गर्नु महत्वपूर्ण छ। हामी AI एजेन्टहरूलाई लागेको केही खतरा मात्र हेरौं र तपाईंले तिनीहरूका लागि कसरी राम्रो योजना बनाउने र तयारी गर्ने सक्नुहुन्छ।

![खतराहरू बुझ्दै](../../../translated_images/ne/understanding-threats.89edeada8a97fc0f.webp)

### कार्य र निर्देशन

**विवरण:** आक्रमणकारीहरूले प्रॉम्प्टिङ वा इनपुटहरू हेरफेर गरेर AI एजेन्टको निर्देशन वा लक्ष्य परिवर्तन गर्ने प्रयास गर्छन्।

**न्यूनीकरण**: AI एजेन्टले प्रक्रिया गर्नु अघि सम्भावित खतरनाक प्रॉम्प्टहरू पत्ता लगाउन वैधता जाँच र इनपुट फिल्टरहरू लागू गर्नुहोस्। यी आक्रमणहरू प्रायः एजेन्टसँग बारम्बार अन्तरक्रिया आवश्यक पार्ने हुँदा, संवादमा टर्नहरूको संख्या सीमित गर्नु यस प्रकारका आक्रमण रोक्ने अर्को उपाय हो।

### महत्वपूर्ण प्रणालीहरूमा पहुँच

**विवरण:** यदि AI एजेन्टसँग संवेदनशील डाटा भण्डारण गर्ने प्रणालीहरू र सेवाहरूमा पहुँच छ भने, आक्रमणकारीहरूले एजेन्ट र ती सेवाहरू बीचको सञ्चारमा हानी पुर्याउन सक्छन्। यी प्रत्यक्ष आक्रमण वा एजेन्टमार्फत ती प्रणालीहरूको बारेमा जानकारी प्राप्त गर्ने अप्रत्यक्ष प्रयास हुन सक्छ।

**न्यूनीकरण:** यी प्रकारका आक्रमण रोक्न AI एजेन्टले आवश्यकता अनुसार मात्र प्रणालीहरूमा पहुँच पाउनुपर्छ। एजेन्ट र प्रणालीबीचको सञ्चार सुरक्षित हुनु पनि जरुरी छ। प्रमाणीकरण र पहुँच नियन्त्रण लागू गर्नु अर्को सुरक्षा उपाय हो।

### स्रोत र सेवा ओभरलोडिंग

**विवरण:** AI एजेन्टहरू विभिन्न उपकरण र सेवाहरूमा पहुँच पाउन सक्छन् कार्यहरू पूरा गर्न। आक्रमणकारीहरूले यो क्षमता प्रयोग गरेर ती सेवाहरूमा ठूलो मात्रामा अनुरोध पठाएर प्रणाली अवरुद्ध वा उच्च लागत निम्त्याउन सक्छन्।

**न्यूनीकरण:** AI एजेन्टले कुनै सेवामा पठाउन सक्ने अनुरोधहरूको संख्या सीमित गर्ने नीतिहरू लागू गर्नुहोस्। संवाद टर्नहरू र AI एजेन्टमा अनुरोधहरूको संख्या सीमित गर्नु पनि यस प्रकारका आक्रमण रोक्ने उपाय हो।

### ज्ञान आधार विषाक्तता

**विवरण:** यो प्रकारको आक्रमणले AI एजेन्टलाई सिधा लक्ष्य बनाउँदैन, बरु AI एजेन्टले प्रयोग गर्ने ज्ञान आधार र अन्य सेवाहरूलाई लक्षित गर्छ। यसले AI एजेन्टले कार्य पूरा गर्न प्रयोग गर्ने डाटा वा जानकारीमा भ्रष्टाचार पार्न सक्छ, जसले प्रयोगकर्तालाई पक्षपातपूर्ण वा अनपेक्षित प्रतिक्रिया दिन सक्छ।

**न्यूनीकरण:** AI एजेन्टले आफ्नो वर्कफ्लोमा प्रयोग गर्ने डाटाको नियमित रूपमा प्रमाणीकरण गर्नुहोस्। यो डाटा सुरक्षित रहोस् र मात्र विश्वासिलो व्यक्तिहरूले मात्र परिवर्तन गर्न सकून् भनेर सुनिश्चित गर्नुहोस्, जसले यस प्रकारको आक्रमणबाट बचाउँछ।

### श्रृंखलाबद्ध त्रुटिहरू

**विवरण:** AI एजेन्टहरूले विभिन्न उपकरण र सेवाहरूमा पहुँच पाउँछन् कार्यहरू पूरा गर्न। आक्रमणकारीहरूले पार्ने गल्तीहरूले AI एजेन्ट जडित अन्य प्रणालीहरूको असफलता निम्त्याउन सक्छ, जसले आक्रमणलाई व्यापक र समस्या समाधान गाह्रो बनाउन सक्छ।

**न्यूनीकरण**: यसबाट बच्न AI एजेन्टलाई सीमित वातावरणमा सञ्चालन गर्नुपर्छ, जस्तै Docker कन्टेनरमा कार्यहरू गर्ने, जसले प्रत्यक्ष प्रणाली आक्रमणबाट जोगाउँछ। केही प्रणालीहरूले त्रुटि प्रतिक्रिया गर्दा फालब्याक मेकानिजम र पुनः प्रयास तर्क सिर्जना गर्नु ठूलो प्रणाली असफलता रोक्ने अर्को उपाय हो।

## मानव-इन-द-लूप

विश्वसनीय AI एजेन्ट प्रणाली निर्माण गर्ने अर्को प्रभावकारी तरिका हो मानव-इन-द-लूप प्रयोग गर्नु। यसले प्रयोगकर्ताहरूलाई रनको दौरान एजेन्टहरूलाई प्रतिपुष्टि प्रदान गर्ने प्रवाह सिर्जना गर्छ। प्रयोगकर्ताहरू बहु-एजेन्ट प्रणालीमा एजेन्टको रूपमा कार्य गर्दछन् र चलिरहेको प्रक्रियाको स्वीकृति वा समाप्ति प्रदान गरेर नियन्त्रण गर्छन्।

![मानव इन द लूप](../../../translated_images/ne/human-in-the-loop.5f0068a678f62f4f.webp)

यहाँ Microsoft Agent Framework प्रयोग गरेर कसरी यो अवधारणा कार्यान्वयन गरिएको छ भन्ने कोड स्निपेट छ:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# मानवीय-जाँच अनुमोदन सहित प्रदायक सिर्जना गर्नुहोस्
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# मानवीय अनुमोदन चरण सहित एजेन्ट सिर्जना गर्नुहोस्
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# प्रयोगकर्ताले प्रतिक्रिया समीक्षा र अनुमोदन गर्न सक्दछ
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## निष्कर्ष

विश्वसनीय AI एजेन्टहरू निर्माण गर्न सावधानीपूर्वक डिजाइन, मजबूत सुरक्षा उपायहरू र निरन्तर पुनरावृति आवश्यक हुन्छ। संरचित मेटा प्रॉम्प्टिङ सिस्टमहरू लागू गरेर, सम्भावित खतराहरू बुझेर, र न्यूनीकरण रणनीतिहरू लागू गरेर विकासकर्ताहरू सुरक्षित र प्रभावकारी AI एजेन्टहरू सिर्जना गर्न सक्छन्। साथै, मानव-इन-द-लूप दृष्टिकोण समावेश गर्दा AI एजेन्टहरू प्रयोगकर्ताको आवश्यकता अनुरूप रहन्छन् र जोखिम न्यून हुन्छ। AI निरन्तर विकास भइरहँदा सुरक्षा, गोपनीयता, र नैतिक विचारहरूमा सक्रिय रहनुले AI संचालित प्रणालीहरूमा विश्वास र भरपर्दोता बढाउने प्रमुख कुरा हुनेछ।

### विश्वसनीय AI एजेन्टहरू बनाउने बारे थप प्रश्नहरू छन्?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मा सामेल हुनुहोस् जहाँ तपाईंले अन्य सिक्नेहरूसँग भेट्न, कार्यालय समयहरूमा भाग लिन र तपाईंका AI एजेन्ट सम्बन्धी प्रश्नहरूको जवाफ प्राप्त गर्न सक्नुहुन्छ।

## थप स्रोतहरू

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">जिम्मेवार AI अवलोकन</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">सृजनात्मक AI मोडेल र AI अनुप्रयोगहरूको मूल्यांकन</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">सुरक्षा प्रणाली मेसेजहरू</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">जोखिम मूल्याङ्कन टेम्प्लेट</a>

## अघिल्लो पाठ

[एजेन्टिक RAG](../05-agentic-rag/README.md)

## अर्को पाठ

[योजना डिजाइन ढाँचा](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरी अनुवाद गरिएको हो। हामी सटीकताको लागि प्रयासरत छौं, तर कृपया जानकार हुनुहोस् कि स्वचालित अनुवादमा त्रुटि वा गलतिहरू हुन सक्छन्। मूल दस्तावेज़लाई यसको स्वदेशी भाषामा नै अधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीका लागि पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याप्रति हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->