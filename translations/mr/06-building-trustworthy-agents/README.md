[![विश्वसनीय AI एजंट्स](../../../translated_images/mr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(या धड्याचा व्हिडिओ पाहण्यासाठी वरच्या प्रतिमेवर क्लिक करा)_

# विश्वसनीय AI एजंट्स तयार करणे

## परिचय

हा धडा खालील गोष्टी उलगडेल:

- सुरक्षित आणि कार्यक्षम AI एजंट्स कसे तयार करावे आणि तैनात करावेत
- AI एजंट्स विकसित करताना महत्त्वाच्या सुरक्षा बाबी.
- AI एजंट्स विकसित करताना डेटा आणि वापरकर्त्यांच्या गोपनीयतेचे कसे जतन करावे.

## शिकण्याचे उद्दिष्ट

हा धडा पूर्ण केल्यानंतर, आपण कसे करू शकाल:

- AI एजंट्स तयार करताना जोखमीची ओळख पटवून त्यावर उपाययोजना करणे.
- डेटा आणि प्रवेश योग्यरित्या व्यवस्थापित होण्यासाठी सुरक्षा उपाय राबविणे.
- AI एजंट तयार करणे जे डेटा गोपनीयता कायम ठेवतात आणि दर्जेदार वापरकर्त्याचा अनुभव पुरवतात.

## सुरक्षितता

सुरक्षित एजंटिक अनुप्रयोग तयार करण्याकडे प्रथम पाहूया. सुरक्षितता म्हणजे AI एजंट त्यानुसार काम करतो जसे डिझाइन केले आहे. एजंटिक अनुप्रयोगांच्या बांधकामामध्ये, आपल्याकडे सुरक्षितता जास्तीत जास्त वाढवण्यासाठी पद्धती आणि साधने आहेत:

### सिस्टम मेसेज फ्रेमवर्क तयार करणे

जर तुम्ही कधी मोठ्या भाषा मॉडेल्स (LLMs) वापरून AI अनुप्रयोग तयार केला असेल, तर तुम्हाला मजबूत सिस्टम प्रांप्ट किंवा सिस्टम मेसेज डिझाइन करण्याचे महत्त्व माहीत असेल. हे प्रांप्ट LLM कसे वापरकर्त्यांशी आणि डेटाशी संवाद साधेल यासाठी मेटा नियम, सूचना आणि मार्गदर्शक तत्त्व तयार करतात.

AI एजंट्ससाठी, सिस्टम प्रांप्ट आणखी महत्त्वाचा असतो, कारण AI एजंट्सना आपल्याने त्यांच्यासाठी तयार केलेल्या कामांची पूर्तता करण्यासाठी अत्यंत विशिष्ट सूचना आवश्यक असतात.

स्केलेबल सिस्टम प्रांप्ट तयार करण्यासाठी, आपण आपल्या अनुप्रयोगात एक किंवा अधिक एजंट तयार करण्यासाठी सिस्टम मेसेज फ्रेमवर्क वापरू शकतो:

![सिस्टम मेसेज फ्रेमवर्क तयार करणे](../../../translated_images/mr/system-message-framework.3a97368c92d11d68.webp)

#### पाऊल 1: मेटा सिस्टम मेसेज तयार करा

मेटा प्रांप्टचा वापर LLM द्वारे तयार केलेल्या एजंट्ससाठी सिस्टम प्रांप्ट निर्माण करण्यासाठी होईल. आम्ही ते एक साचे म्हणून डिझाइन करतो जेणेकरून आवश्यक असल्यास अनेक एजंट्स प्रभावीपणे तयार करता येतील.

येथे LLM ला दिला जाणारा मेटा सिस्टम मेसेजचा एक उदाहरण आहे:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### पाऊल 2: मूलभूत प्रांप्ट तयार करा

पुढील पाऊल म्हणजे AI एजंटचे वर्णन करणारा मूलभूत प्रांप्ट तयार करणे. तुम्ही एजंटची भूमिका, एजंट पूर्ण करावयाची कामे आणि एजंटच्या इतर जबाबदाऱ्या समाविष्ट कराव्यात.

येथे एक उदाहरण आहे:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### पाऊल 3: LLM ला मूलभूत सिस्टम मेसेज पुरवा

आता आपण या सिस्टम मेसेजचे ऑप्टिमायझेशन करू शकतो, मेटा सिस्टम मेसेजला सिस्टम मेसेज म्हणून आणि आपला मूलभूत सिस्टम मेसेज म्हणून पुरवून.

यामुळे आपल्या AI एजंट्ससाठी मार्गदर्शन करणारा अधिक चांगला डिझाइन केलेला सिस्टम मेसेज तयार होईल:

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

#### पाऊल 4: पुनरावृत्ती करून सुधारणा करा

या सिस्टम मेसेज फ्रेमवर्कचे मूल्य म्हणजे अनेक एजंटच्या सिस्टम मेसेजेस तयार करणे सुलभ करणे आणि आपल्या सिस्टम मेसेजेस वेळोवेळी सुधारणा करणे. तुमच्याकडे प्रथमच पूर्ण वापर प्रकरणासाठी काम करणारा सिस्टम मेसेज असणे अवघड आहे. मूलभूत सिस्टम मेसेज बदलून आणि त्याला सिस्टममधून चालवून लहान सुधारणा आणि बदल करता येणे तुम्हाला परिणामांची तुलना आणि मूल्यांकन करण्यास मदत करेल.

## धोके समजून घेणे

विश्वसनीय AI एजंट तयार करण्यासाठी, आपल्या AI एजंटवरील धोके आणि जोखमी समजून घेणे आणि त्यावर उपाययोजना करणे महत्त्वाचे आहे. चला AI एजंटच्या काही वेगवेगळ्या धोक्यांकडे पाहू आणि तुम्ही त्यासाठी कसे उत्तम नियोजन आणि तयारी करू शकता हे समजून घेऊ.

![धोके समजून घेणे](../../../translated_images/mr/understanding-threats.89edeada8a97fc0f.webp)

### काम आणि सूचनांवरील हल्ला

**वर्णन:** हल्लेखोर AI एजंटच्या सूचनांमध्ये बदल करण्याचा किंवा उद्दिष्टे बदलण्याचा प्रयत्न करतात, प्रांप्टिंग किंवा इनपुट्समध्ये फेरबदल करून.

**उपाय:** AI एजंट प्रक्रिया करण्यापूर्वी संभाव्य धोके निर्माण करणारे प्रॉम्प्ट शोधण्यासाठी प्रमाणीकरण तपासणी आणि इनपुट फिल्टर्स वापरा. हे हल्ले सामान्यतः एजंटशी वारंवार संवाद साधल्यामुळे संभाषणातील टर्न्सची मर्यादा घालणेही ह्या प्रकारच्या हल्ल्यांना प्रतिबंध करण्याचा एक मार्ग आहे.

### महत्त्वाच्या प्रणालींमध्ये प्रवेश

**वर्णन:** AI एजंटला संवेदनशील डेटा संग्रहित करणाऱ्या प्रणाली आणि सेवांमध्ये प्रवेश असल्यास, हल्लेखोर एजंट आणि या सेवांमधील संप्रेषणात भंग करु शकतात. हे थेट हल्ले असू शकतात किंवा एजंटमार्गे या प्रणालींबाबत माहिती मिळवण्याचा अप्रत्यक्ष प्रयत्न असू शकतो.

**उपाय:** ह्या प्रकारच्या हल्ल्यांना प्रतिबंध करण्यासाठी AI एजंट्सकडे फक्त आवश्यकतेनुसार प्रवेश असावा. एजंट आणि प्रणालीतील संप्रेषण देखील सुरक्षित असावे. प्रमाणपत्र आणि प्रवेश नियंत्रणाची अंमलबजावणी करणे देखील हा डेटा संरक्षित ठेवण्याचा एक मार्ग आहे.

### संसाधने आणि सेवा ओव्हरलोड होणे

**वर्णन:** AI एजंट्स विविध उपकरणे आणि सेवा वापरून कामे पूर्ण करतात. हल्लेखोर एजंटच्या माध्यमातून उच्च प्रमाणात विनंत्या पाठवून या सेवांवर हल्ला करू शकतात, ज्यामुळे प्रणाली अपयशी होऊ शकते किंवा उच्च खर्च येऊ शकतो.

**उपाय:** एखाद्या सेवेसाठी AI एजंट किती विनंत्या करू शकतो यावर धोरणे लागू करा. संभाषणातील टर्न्स आणि विनंत्यांवर मर्यादा घालणे ह्या प्रकारच्या हल्ल्यांना प्रतिबंध करण्याचा आणखी एक मार्ग आहे.

### ज्ञानाधार प्रदूषण

**वर्णन:** ह्या प्रकारचा हल्ला थेट AI एजंटवर नव्हे तर वापरणाऱ्या ज्ञानाधार किंवा इतर सेवा यावर होतो. हा डेटा किंवा माहिती भ्रष्ट करून एजंटने दिलेली प्रतिक्रिया पक्षपातपूर्ण किंवा अनपेक्षित होऊ शकते.

**उपाय:** AI एजंट कार्यप्रवाहांमध्ये वापरणार्‍या डेटाची नियमित पडताळणी करा. या डेटावर प्रवेश सुरक्षित ठेवा आणि फक्त विश्वासू व्यक्तींनी बदल होऊ देणे याची खात्री करा.

### चोवेळ आरोग्य समस्या (Cascading Errors)

**वर्णन:** AI एजंट विविध उपकरणे आणि सेवा वापरतो. हल्लेखोरांनी त्रुटी निर्माण केल्यास हे इतर प्रणालींमध्ये समस्या निर्माण करु शकते, ज्यामुळे हल्ला अधिक विस्तृत होतो आणि त्रुटी शोधणे कठीण होते.

**उपाय:** यासाठी एखाद्या मर्यादित वातावरणात AI एजंट चालवणे जसे की Docker कंटेनरमध्ये कार्य करणे, थेट प्रणालीवर हल्ला होण्यापासून बचाव करेल. चुकीच्या प्रतिसाद मिळाल्यास वापरली जाणारी फॉलबॅक यंत्रणा आणि रीट्राय लॉजिक तयार करणे हे मोठ्या प्रणालीतील त्रुटींना प्रतिबंधित करणे होय.

## मानवी सहभाग

विश्वसनीय AI एजंट प्रणाली तयार करण्याचा आणखी एक प्रभावी मार्ग म्हणजे मानवी-इन-द-लूप वापरणे. यामुळे वापरकर्ते एजंट चालू असताना अभिप्राय देऊ शकतात. वापरकर्ते मल्टी-एजंट प्रणालीतील एजंटच्या भूमिकेत असतात आणि चालू प्रक्रियेचे मंजुरी अथवा बंदी देतात.

![मानवी-इन-द-लूप](../../../translated_images/mr/human-in-the-loop.5f0068a678f62f4f.webp)

ही संकल्पना कशी राबवली जाते हे दाखवण्यासाठी Microsoft Agent Framework वापरून एक कोड स्निपेट:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# मानवी अभिप्रायासह प्रोव्हायडर तयार करा
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# मानवी अभिप्राय टप्प्यासह एजंट तयार करा
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# वापरकर्ता प्रतिसाद पुनरावलोकन करू शकतो आणि मंजूर करू शकतो
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## निष्कर्ष

विश्वसनीय AI एजंट तयार करणे काळजीपूर्वक डिझाइन, मजबूत सुरक्षा उपाय आणि सातत्यपूर्ण पुनरावृत्ती आवश्यक आहे. संरचित मेटा प्रांप्टिंग सिस्टिम्स अंमलात आणून, संभाव्य धोके समजून आणि उपाययोजना राबवून, विकसक सुरक्षित आणि कार्यक्षम AI एजंट तयार करू शकतात. शिवाय, मानवी-इन-द-लूप पद्धत समाविष्ट करणे यामुळे AI एजंट वापरकर्त्यांच्या गरजांशी संरेखित रहातात आणि धोके कमी होतात. AI विकसित होत राहिल्यामुळे, सुरक्षा, गोपनीयता आणि नैतिक बाबींवर सक्रिय लक्ष ठेवणे AI-चालित सिस्टममध्ये विश्वास आणि विश्वासार्हता वाढविण्यासाठी महत्त्वाचे ठरेल.

## कोड नमुने

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): मेटा-प्रांप्ट सिस्टम-मसेज फ्रेमवर्कचे पायरी-पायरीने प्रदर्शन.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): विश्वसनीय एजंटसाठी प्री-ऍक्शन मंजुरी गेट्स, जोखमीची स्तरवारी, आणि तपासणी लॉगिंग.

### विश्वसनीय AI एजंट्स तयार करण्याबाबत आणखी प्रश्न?

इतर शिकणाऱ्यांशी भेटण्यासाठी, ऑफिस ऑवर्स अटेंड करण्यासाठी आणि तुमचे AI एजंट्सचे प्रश्न विचारण्यासाठी [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा.

## अतिरिक्त संसाधने

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">जबाबदार AI ओव्हरव्यू</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">उत्पादक AI मॉडेल्स आणि AI अनुप्रयोगांचे मूल्यांकन</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">सुरक्षितता सिस्टम मेसेजेस</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">जोखीम मूल्यांकन टेम्प्लेट</a>

## मागील धडा

[Agentic RAG](../05-agentic-rag/README.md)

## पुढील धडा

[परियोजना डिझाइन पॅटर्न](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->