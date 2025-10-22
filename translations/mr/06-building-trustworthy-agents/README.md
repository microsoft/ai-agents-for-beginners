<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T10:02:57+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "mr"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.mr.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(वरील प्रतिमेवर क्लिक करून या धड्याचा व्हिडिओ पाहा)_

# विश्वासार्ह AI एजंट्स तयार करणे

## परिचय

या धड्यात आपण शिकणार आहोत:

- सुरक्षित आणि प्रभावी AI एजंट्स कसे तयार करायचे आणि तैनात करायचे
- AI एजंट्स विकसित करताना महत्त्वाच्या सुरक्षा बाबी
- AI एजंट्स विकसित करताना डेटा आणि वापरकर्त्याच्या गोपनीयतेचे संरक्षण कसे करायचे

## शिकण्याची उद्दिष्टे

हा धडा पूर्ण केल्यानंतर, तुम्हाला हे समजेल:

- AI एजंट्स तयार करताना धोके ओळखणे आणि त्यावर उपाय करणे
- डेटा आणि प्रवेश योग्य प्रकारे व्यवस्थापित होण्यासाठी सुरक्षा उपाय अंमलात आणणे
- डेटा गोपनीयता राखणारे आणि दर्जेदार वापरकर्ता अनुभव देणारे AI एजंट्स तयार करणे

## सुरक्षा

सुरुवातीला, सुरक्षित एजंटिक अनुप्रयोग तयार करण्याबद्दल जाणून घेऊया. सुरक्षा म्हणजे AI एजंटने अपेक्षेप्रमाणे कार्य करणे. एजंटिक अनुप्रयोग तयार करणाऱ्या विकासकांकडे सुरक्षा वाढवण्यासाठी पद्धती आणि साधने असतात:

### सिस्टम मेसेज फ्रेमवर्क तयार करणे

जर तुम्ही कधी Large Language Models (LLMs) वापरून AI अनुप्रयोग तयार केला असेल, तर तुम्हाला मजबूत सिस्टम प्रॉम्प्ट किंवा सिस्टम मेसेज डिझाइन करण्याचे महत्त्व माहीत असेल. हे प्रॉम्प्ट्स LLM वापरकर्त्याशी आणि डेटाशी कसे संवाद साधेल यासाठी नियम, सूचना आणि मार्गदर्शक तत्त्वे स्थापित करतात.

AI एजंट्ससाठी, सिस्टम प्रॉम्प्ट अधिक महत्त्वाचे आहे कारण AI एजंट्सना आम्ही डिझाइन केलेल्या कार्ये पूर्ण करण्यासाठी अत्यंत विशिष्ट सूचना आवश्यक असतात.

स्केलेबल सिस्टम प्रॉम्प्ट तयार करण्यासाठी, आपण आपल्या अनुप्रयोगात एक किंवा अधिक एजंट्स तयार करण्यासाठी सिस्टम मेसेज फ्रेमवर्क वापरू शकतो:

![सिस्टम मेसेज फ्रेमवर्क तयार करणे](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.mr.png)

#### पाऊल 1: मेटा सिस्टम मेसेज तयार करा

मेटा प्रॉम्प्ट LLM ला आम्ही तयार केलेल्या एजंट्ससाठी सिस्टम प्रॉम्प्ट्स तयार करण्यासाठी वापरले जाईल. आम्ही ते टेम्पलेट म्हणून डिझाइन करतो जेणेकरून आवश्यक असल्यास अनेक एजंट्स कार्यक्षमतेने तयार करता येतील.

खाली मेटा सिस्टम मेसेजचे एक उदाहरण दिले आहे:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### पाऊल 2: मूलभूत प्रॉम्प्ट तयार करा

पुढील पाऊल म्हणजे AI एजंटचे वर्णन करणारा मूलभूत प्रॉम्प्ट तयार करणे. यात एजंटची भूमिका, एजंट पूर्ण करणार्या कार्यांची यादी आणि एजंटच्या इतर जबाबदाऱ्या समाविष्ट कराव्यात.

खाली एक उदाहरण दिले आहे:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### पाऊल 3: LLM ला मूलभूत सिस्टम मेसेज द्या

आता आपण मेटा सिस्टम मेसेजला सिस्टम मेसेज म्हणून आणि आपला मूलभूत सिस्टम मेसेज देऊन हा सिस्टम मेसेज ऑप्टिमाइझ करू शकतो.

यामुळे आपल्या AI एजंट्सना मार्गदर्शन करण्यासाठी अधिक चांगल्या प्रकारे डिझाइन केलेला सिस्टम मेसेज तयार होईल:

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

या सिस्टम मेसेज फ्रेमवर्कचे मूल्य म्हणजे अनेक एजंट्ससाठी सिस्टम मेसेज तयार करणे सुलभ करणे तसेच वेळोवेळी आपल्या सिस्टम मेसेजमध्ये सुधारणा करणे. तुमच्या संपूर्ण उपयोग प्रकरणासाठी पहिल्यांदाच कार्य करणारा सिस्टम मेसेज असणे दुर्मिळ आहे. मूलभूत सिस्टम मेसेजमध्ये लहान बदल करून आणि सिस्टमद्वारे चालवून परिणामांची तुलना आणि मूल्यांकन करण्याची क्षमता तुम्हाला सुधारणा करण्यात मदत करेल.

## धोके समजून घेणे

विश्वासार्ह AI एजंट्स तयार करण्यासाठी, तुमच्या AI एजंटला असलेल्या धोके आणि धमक्या समजून घेणे आणि त्यावर उपाय करणे महत्त्वाचे आहे. चला AI एजंट्सना असलेल्या काही वेगवेगळ्या धमक्यांकडे आणि त्यासाठी तुम्ही कसे चांगले नियोजन करू शकता याकडे पाहूया.

![धोके समजून घेणे](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.mr.png)

### कार्य आणि सूचना

**वर्णन:** हल्लेखोर AI एजंटच्या सूचना किंवा उद्दिष्टे बदलण्याचा प्रयत्न करतात, प्रॉम्प्टिंग किंवा इनपुटमध्ये फेरफार करून.

**उपाय:** AI एजंटद्वारे प्रक्रिया होण्यापूर्वी संभाव्य धोकादायक प्रॉम्प्ट्स ओळखण्यासाठी वैधता तपासणी आणि इनपुट फिल्टर्स अंमलात आणा. या प्रकारच्या हल्ल्यांसाठी सामान्यतः एजंटशी वारंवार संवाद आवश्यक असतो, त्यामुळे संभाषणातील टप्प्यांची संख्या मर्यादित करणे हा हल्ला टाळण्याचा आणखी एक मार्ग आहे.

### महत्त्वाच्या प्रणालींमध्ये प्रवेश

**वर्णन:** जर AI एजंटला संवेदनशील डेटा साठवणाऱ्या प्रणालींमध्ये प्रवेश असेल, तर हल्लेखोर एजंट आणि या सेवा यांच्यातील संवादाशी छेडछाड करू शकतात. हे थेट हल्ले किंवा अप्रत्यक्षपणे या प्रणालींबद्दल माहिती मिळवण्याचे प्रयत्न असू शकतात.

**उपाय:** AI एजंट्सना फक्त आवश्यकतेनुसार प्रणालींमध्ये प्रवेश द्या. एजंट आणि प्रणाली यांच्यातील संवाद सुरक्षित ठेवा. प्रमाणीकरण आणि प्रवेश नियंत्रण अंमलात आणणे ही माहिती संरक्षित करण्याचा आणखी एक मार्ग आहे.

### संसाधन आणि सेवा ओव्हरलोडिंग

**वर्णन:** AI एजंट्स विविध साधने आणि सेवा वापरून कार्य पूर्ण करतात. हल्लेखोर या सेवांवर हल्ला करण्यासाठी AI एजंटद्वारे मोठ्या प्रमाणात विनंत्या पाठवू शकतात, ज्यामुळे प्रणाली अयशस्वी होऊ शकते किंवा जास्त खर्च होऊ शकतो.

**उपाय:** AI एजंटला सेवा करण्यासाठी विनंत्यांची संख्या मर्यादित करण्यासाठी धोरणे अंमलात आणा. संभाषणातील टप्प्यांची संख्या आणि AI एजंटला पाठवलेल्या विनंत्यांची मर्यादा घालणे हा हल्ला टाळण्याचा आणखी एक मार्ग आहे.

### ज्ञानभांडार विषबाधा

**वर्णन:** या प्रकारचा हल्ला थेट AI एजंटवर होत नाही, तर ज्ञानभांडार आणि इतर सेवांवर होतो, ज्या AI एजंट वापरतो. यात डेटा किंवा माहिती दूषित करणे समाविष्ट असते, ज्यामुळे वापरकर्त्याला पक्षपाती किंवा अनपेक्षित प्रतिसाद मिळतो.

**उपाय:** AI एजंट त्यांच्या कार्यप्रवाहांमध्ये वापरत असलेल्या डेटाची नियमितपणे पडताळणी करा. या डेटामध्ये प्रवेश सुरक्षित ठेवा आणि केवळ विश्वासार्ह व्यक्तींनीच बदल करू शकतील याची खात्री करा.

### साखळीतील त्रुटी

**वर्णन:** AI एजंट्स विविध साधने आणि सेवा वापरून कार्य पूर्ण करतात. हल्लेखोरांमुळे झालेल्या त्रुटी इतर प्रणालींच्या अयशस्वी होण्यास कारणीभूत ठरू शकतात, ज्यामुळे हल्ला अधिक व्यापक होतो आणि तोडगा काढणे कठीण होते.

**उपाय:** AI एजंटला मर्यादित वातावरणात कार्य करण्यास सांगा, जसे की Docker कंटेनरमध्ये कार्ये पार पाडणे, थेट प्रणालीवरील हल्ले टाळण्यासाठी. काही प्रणाली त्रुटींसह प्रतिसाद देतात तेव्हा बॅकअप यंत्रणा आणि पुन्हा प्रयत्न करण्याचे लॉजिक तयार करणे ही मोठ्या प्रणाली अयशस्वी होण्यापासून वाचवण्याची आणखी एक पद्धत आहे.

## ह्युमन-इन-द-लूप

विश्वासार्ह AI एजंट प्रणाली तयार करण्याचा आणखी एक प्रभावी मार्ग म्हणजे ह्युमन-इन-द-लूप वापरणे. यामुळे वापरकर्त्यांना एजंट्सना फीडबॅक देण्याची प्रक्रिया तयार होते. वापरकर्ते मूलत: मल्टी-एजंट प्रणालीतील एजंट्सप्रमाणे कार्य करतात आणि चालू असलेल्या प्रक्रियेची मंजुरी किंवा समाप्ती देतात.

![ह्युमन-इन-द-लूप](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.mr.png)

खाली AutoGen वापरून या संकल्पनेची अंमलबजावणी कशी केली जाते याचे कोड उदाहरण दिले आहे:

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

विश्वासार्ह AI एजंट्स तयार करणे म्हणजे काळजीपूर्वक डिझाइन, मजबूत सुरक्षा उपाय आणि सतत सुधारणा करणे. संरचित मेटा प्रॉम्प्टिंग प्रणाली अंमलात आणून, संभाव्य धोके समजून घेऊन आणि त्यावर उपाययोजना करून, विकासक सुरक्षित आणि प्रभावी AI एजंट्स तयार करू शकतात. याशिवाय, ह्युमन-इन-द-लूप दृष्टिकोन समाविष्ट केल्याने AI एजंट्स वापरकर्त्यांच्या गरजांशी सुसंगत राहतात आणि धोके कमी होतात. AI सतत विकसित होत असताना, सुरक्षा, गोपनीयता आणि नैतिक विचारांवर सक्रिय भूमिका घेणे AI-चालित प्रणालींमध्ये विश्वास आणि विश्वासार्हता वाढवण्यासाठी महत्त्वाचे ठरेल.

### विश्वासार्ह AI एजंट्स तयार करण्याबद्दल अधिक प्रश्न आहेत का?

[Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) मध्ये सामील व्हा, इतर शिकणाऱ्यांशी चर्चा करा, ऑफिस तासांमध्ये सहभागी व्हा आणि तुमचे AI एजंट्स संबंधित प्रश्न विचारून उत्तरे मिळवा.

## अतिरिक्त संसाधने

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">जबाबदार AI चे विहंगावलोकन</a>  
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">जनरेटिव्ह AI मॉडेल्स आणि AI अनुप्रयोगांचे मूल्यांकन</a>  
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">सुरक्षा प्रणाली संदेश</a>  
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">जोखीम मूल्यांकन टेम्पलेट</a>  

## मागील धडा

[Agentic RAG](../05-agentic-rag/README.md)

## पुढील धडा

[Planning Design Pattern](../07-planning-design/README.md)

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर केल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमजांकरिता किंवा चुकीच्या अर्थ लावण्याकरिता आम्ही जबाबदार राहणार नाही.