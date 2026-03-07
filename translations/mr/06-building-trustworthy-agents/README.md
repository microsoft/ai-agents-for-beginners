[![विश्वसनीय एआय एजंट](../../../translated_images/mr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(वरील प्रतिमा क्लिक करून या धड्याचा व्हिडिओ पहा)_

# विश्वसनीय एआय एजंट तयार करणे

## परिचय

या धड्यात खालील गोष्टींचा समावेश असेल:

- सुरक्षित आणि प्रभावी एआय एजंट कसे तयार करायचे आणि तैनात करायचे
- एआय एजंट विकसित करताना महत्त्वाच्या सुरक्षा बाबी.
- एआय एजंट विकसित करताना डेटा आणि वापरकर्त्याची गोपनीयता कशी राखावी.

## शिक्षण उद्दिष्टे

हा धडा पूर्ण केल्यावर, तुम्हाला खालील गोष्टी करता येतील:

- एआय एजंट तयार करताना धोके कसे ओळखायचे आणि कमी करायचे.
- डेटा आणि प्रवेश योग्य प्रकारे व्यवस्थापित होतात याची खात्री करण्यासाठी सुरक्षा उपाय कसे लागू करायचे.
- डेटा गोपनीयता राखणारे आणि दर्जेदार वापरकर्ता अनुभव देणारे एआय एजंट कसे तयार करायचे.

## सुरक्षा

प्रथम सुरक्षित एजंट-आधारित अनुप्रयोग कसे तयार करायचे ते पाहूया. सुरक्षा म्हणजे एआय एजंट डिझाइन केलेल्या प्रमाणे कार्य करतो. एजंट-आधारित अनुप्रयोगांचे निर्माते म्हणून, सुरक्षितता वाढवण्यासाठी आमच्याकडे पद्धती आणि साधने आहेत:

### सिस्टम संदेश फ्रेमवर्क तयार करणे

जर तुम्ही कधीही Large Language Models (LLMs) वापरून एआय अनुप्रयोग तयार केले असल्यास, मजबूत सिस्टम प्रॉम्प्ट किंवा सिस्टम संदेश डिझाइन करण्याचे महत्त्व तुम्हाला माहित असेल. हे प्रॉम्प्ट LLM वापरकर्त्या आणि डेटासोबत कसा संवाद करेल यासंबंधीचे मेटा नियम, सूचना आणि मार्गदर्शक तत्त्वे निश्चित करतात.

एआय एजंटसाठी, सिस्टम प्रॉम्प्ट आणखी महत्त्वाचा असतो कारण एआय एजंट्सना आपण त्यांच्यासाठी डिझाइन केलेल्या कामे पूर्ण करण्यासाठी अत्यंत विशिष्ट सूचनांची आवश्यकता असते.

स्केलेबल सिस्टम प्रॉम्प्ट तयार करण्यासाठी, आपल्या अनुप्रयोगात एक किंवा अधिक एजंट तयार करण्यासाठी आपण सिस्टम संदेश फ्रेमवर्क वापरू शकतो:

![सिस्टम संदेश फ्रेमवर्क तयार करणे](../../../translated_images/mr/system-message-framework.3a97368c92d11d68.webp)

#### पाऊल 1: मेटा सिस्टम संदेश तयार करा 

मेटा प्रॉम्प्टचा वापर आम्ही तयार करणार्‍या एजंटसाठी LLM ने सिस्टम प्रॉम्प्ट तयार करण्यासाठी केला जाईल. आवश्यक असल्यास अनेक एजंट प्रभावीपणे तयार करण्यासाठी आम्ही त्याला एक टेम्पलेट म्हणून डिझाइन करतो.

खाली LLM ला दिला जाणारा मेटा सिस्टम संदेशाचा एक उदाहरण दिले आहे:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### पाऊल 2: एक मूलभूत प्रॉम्प्ट तयार करा

पुढील पाऊल एआय एजंटचे वर्णन करण्यासाठी एक मूलभूत प्रॉम्प्ट तयार करणे आहे. यात एजंटची भूमिका, एजंट कोणती कामे पूर्ण करेल आणि एजंटच्या इतर कोणत्या जबाबदा-या आहेत त्या समाविष्ट कराव्यात.

येथे एक उदाहरण आहे:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### पाऊल 3: मूलभूत सिस्टम संदेश LLM ला द्या

आता आपण मेटा सिस्टम संदेश सिस्टम संदेश म्हणून आणि आपला मूलभूत सिस्टम संदेश प्रदान करून हा सिस्टम संदेश ऑप्टिमाइझ करू शकतो.

यामुळे एक असा सिस्टम संदेश तयार होईल जो आपल्या एआय एजंट्सना मार्गदर्शन करण्यासाठी अधिक चांगला डिझाइन केलेला असेल:

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

#### पाऊल 4: पुनरावृत्ती करा आणि सुधारणा करा

या सिस्टम संदेश फ्रेमवर्कचे मूल्य म्हणजे अनेक एजंट्ससाठी सिस्टम संदेश तयार करणे स्केलेबल करणे आणि आपल्या सिस्टम संदेशांना कालांतराने सुधारण्यास सक्षम करणे. पूर्ण वापर केससाठी प्रथमच काम करणारा सिस्टम संदेश असणे क्वचितच होते. मूलभूत सिस्टम संदेश बदलून आणि तो सिस्टममधून चालवून लहान बदल व सुधारणा करण्याची क्षमता तुम्हाला परिणामांची तुलना व मूल्यांकन करण्यास मदत करेल.

## धोके समजून घेणे

विश्वसनीय एआय एजंट तयार करण्यासाठी, तुमच्या एआय एजंटवर होणारे धोके आणि आव्हाने समजून घेणे आणि कमी करणे महत्त्वाचे आहे. चला एआय एजंट्ससाठी काही वेगवेगळ्या धोक्यांवर आणि त्यांच्यासाठी तुम्ही कसे चांगले योजना करू शकता व तयार होऊ शकता ते पाहूया.

![धोके समजून घेणे](../../../translated_images/mr/understanding-threats.89edeada8a97fc0f.webp)

### कार्य आणि सूचना

**वर्णन:** हल्लेखोर एआय एजंटच्या सूचनां किंवा उद्दिष्टांमध्ये बदल करण्यासाठी प्रॉम्प्टिंग किंवा इनपुट्समध्ये हस्तक्षेप करण्याचा प्रयत्न करतात.

**कमी करणे:** प्रक्रियेत आणण्यापूर्वी संभाव्य धोकादायक प्रॉम्प्ट्स शोधण्यासाठी वैधता तपासणी आणि इनपुट फिल्टर लागू करा. हे हल्ले सहसा एजंटसोबत वारंवार संवाद आवश्यक असतात, म्हणून संभाषणातील टर्न्सची संख्या मर्यादित करणे ही अशा प्रकारच्या हल्ल्यांना रोखण्याचा आणखी एक मार्ग आहे.

### महत्त्वाच्या सिस्टम्समध्ये प्रवेश

**वर्णन:** जर एआय एजंटला संवेदनशील डेटा साठवणाऱ्या प्रणाली व सेवांमध्ये प्रवेश असेल, तर हल्लेखोर एजंट व या सेवांमधील संप्रेषणाचे तुटवड्या करू शकतात. हे थेट हल्ले असू शकतात किंवा एजंटद्वारे या प्रणालींबद्दल माहिती मिळवण्याच्या अप्रत्यक्ष प्रयत्नांद्वारे केले जाऊ शकतात.

**कमी करणे:** या प्रकारच्या हल्ल्यांना प्रतिबंध करण्यासाठी एआय एजंट्सना फक्त गरजेनुसारच प्रणालींमध्ये प्रवेश द्यावा. एजंट आणि प्रणाली यांच्यातील संप्रेषण सुरक्षित असावे. प्रमाणिकरण आणि प्रवेश नियंत्रण लागू करणे हा या माहितीस सुरक्षित ठेवण्याचा आणखी एक मार्ग आहे.

### संसाधन आणि सेवा ओव्हरलोडिंग

**वर्णन:** एआय एजंट्स विविध साधने आणि सेवा वापरून कामे पूर्ण करू शकतात. हल्लेखोर या क्षमतेचा वापर करून AI एजंटद्वारे मोठ्या प्रमाणात विनंत्या पाठवून या सेवांवर हल्ले करू शकतात, ज्यामुळे सिस्टम अपयश किंवा जास्त खर्च होऊ शकतो.

**कमी करणे:** एआय एजंट एखाद्या सेवेला किती विनंत्या करू शकतो यावर मर्यादा घालण्यासाठी धोरणे लागू करा. संभाषणातील टर्न्स आणि तुमच्या एआय एजंटकडे गेलेल्या विनंत्यांची संख्या मर्यादित करणे ही अशा प्रकारच्या हल्ल्यांना प्रतिबंध करण्याचा आणखी एक मार्ग आहे.

### ज्ञानसंच विषबाधा

**वर्णन:** या प्रकारचा हल्ला थेट एआय एजंटवर लक्ष्य करत नाही तर त्या ज्ञानसंचावर आणि इतर सेवांवर लक्ष्य करतो ज्यांचा एआय एजंट काम पूर्ण करण्यासाठी वापर करेल. यात एआय एजंट काम पूर्ण करण्यासाठी वापरणार्‍या डेटाची किंवा माहितीत बिघाड करणे समाविष्ट असू शकते, ज्यामुळे वापरकर्त्यास अपक्षिप्त किंवा अवांछित प्रतिसाद मिळू शकतो.

**कमी करणे:** एआय एजंट त्याच्या वर्कफ्लोमध्ये वापरणार्‍या डेटाची नियमित तपासणी करा. या डेटावर प्रवेश सुरक्षित ठेवला गेला आहे आणि केवळ विश्वसनीय व्यक्तींद्वारेच बदलला जातो याची खात्री करा जेणेकरून या प्रकारच्या हल्ल्यांना टाळता येईल.

### कॅस्केडिंग त्रुटी

**वर्णन:** एआय एजंट विविध साधने आणि सेवा वापरून कामे पूर्ण करतात. हल्लेखोरांमुळे झालेल्या त्रुटीमुळे एआय एजंट जोडलेल्या इतर प्रणालींचे अपयश होऊ शकते, ज्यामुळे हल्ला अधिक व्यापक होतो आणि त्रास निवारण करणे कठीण होते.

**कमी करणे:** यापासून टाळण्यासाठी एक पद्धत म्हणजे एआय एजंटला मर्यादित वातावरणात कार्य करण्यास सांगणे, उदाहरणार्थ Docker कंटेनरमध्ये काम करणे, जेणेकरून थेट प्रणाली हल्ले रोखता येतील. काही प्रणाली त्रुटी परत केल्यास फॉलबॅक यंत्रणा आणि पुनःप्रयत्न लॉजिक तयार करणे हा मोठ्या प्रमाणावर प्रणाली अपयश टाळण्याचा आणखी एक मार्ग आहे.

## मानव-इन-द-लूप

विश्वसनीय एआय एजंट सिस्टिम तयार करण्याचा आणखी एक प्रभावी मार्ग म्हणजे मानव-इन-द-लूप वापरणे. यामुळे एक असा प्रवाह तयार होतो ज्यात वापरकर्ते रन दरम्यान एजंट्सना अभिप्राय देऊ शकतात. वापरकर्ते बहु-एजंट प्रणालीमध्ये प्रत्यक्ष एजंट म्हणून कार्य करतात आणि चालू प्रक्रियेची मान्यता देणे किंवा थांबवणे यांसारखे निर्णय घेतात.

![मानव-इन-द-लूप](../../../translated_images/mr/human-in-the-loop.5f0068a678f62f4f.webp)

हा एक कोड स्निपेट आहे जो Microsoft Agent Framework वापरून हा संकल्पना कशी अंमलात आणली जाते हे दाखवतो:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# मानवी हस्तक्षेपाद्वारे मंजुरीसह प्रदाता तयार करा
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# मानवी मंजुरीच्या टप्प्यासह एजंट तयार करा
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# वापरकर्ता प्रतिसाद पुनरावलोकन करून तो मंजूर करू शकतो
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## निष्कर्ष

विश्वसनीय एआय एजंट तयार करण्यासाठी काळजीपूर्वक डिझाइन, मजबूत सुरक्षा उपाय आणि सातत्यपूर्ण पुनरावृत्ती आवश्यक आहे. संरचित मेटा प्रॉम्प्टिंग सिस्टम लागू करून, संभाव्य धोक्यांना समजून घेतले आणि प्रतिबंधात्मक धोरणे वापरून, डेव्हलपर्स सुरक्षित व प्रभावी एआय एजंट तयार करू शकतात. तसेच मानव-इन-द-लूप पध्दतीचा समावेश केल्याने एआय एजंट वापरकर्त्यांच्या गरजांसोबत सुसंगत राहतात आणि धोक्यांचे प्रमाण कमी होते. एआय विकसित होत राहिल्याने, सुरक्षा, गोपनीयता आणि नैतिक बाबींवर सक्रिय दृष्टी ठेवणे हे एआय-चालित प्रणालींमध्ये विश्वास आणि विश्वासार्हता वाढवण्यासाठी महत्वाचे ठरेल.

### विश्वसनीय एआय एजंट तयार करण्याबद्दल आणखी प्रश्न आहेत का?

इतर शिकणाऱ्यांशी भेटण्यासाठी, ऑफिस अवर्समध्ये सहभागी होण्यासाठी आणि तुमचे एआय एजंट्स संदर्भातील प्रश्न निराकरण करण्यासाठी [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा.

## अतिरिक्त संसाधने

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">जबाबदार एआय आढावा</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">जनरेटिव्ह एआय मॉडेल्स आणि एआय अनुप्रयोगांचे मूल्यांकन</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">सुरक्षा सिस्टम संदेश</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">जोखीम मूल्यांकन टेम्पलेट</a>

## मागील धडा

[एजंटिक RAG](../05-agentic-rag/README.md)

## पुढील धडा

[योजना डिझाइन पॅटर्न](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
अस्वीकरण:
हा दस्तऐवज एआय अनुवाद सेव्हिस [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील आहोत, परंतु कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चूक किंवा अचूकतेचा अभाव असू शकतो. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला जावा. अत्यावश्यक किंवा महत्त्वाच्या माहितीच्या बाबतीत व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजांबद्दल किंवा चुकीच्या अर्थ लावण्याबद्दल आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->