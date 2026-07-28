[![विश्वसनीय AI एजंट्स](../../../translated_images/mr/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(या धड्याचा व्हिडिओ पाहण्यासाठी वरील प्रतिमा क्लिक करा)_

# विश्वसनीय AI एजंट्स तयार करणे

## परिचय

हा धडा या गोष्टींचा आढावा घेईल:

- सुरक्षित आणि प्रभावी AI एजंट तयार करणे आणि तैनात कसे करायचे
- AI एजंट विकसित करताना महत्त्वाचे सुरक्षा विचार.
- AI एजंट विकसित करताना डेटा आणि वापरकर्ता गोपनीयता कशी राखायची.

## शिक्षणाची उद्दिष्टे

हा धडा पूर्ण केल्यावर आपल्याला माहित असेल कसे:

- AI एजंट तयार करताना धोके ओळखणे आणि कमी करणे.
- डेटा व प्रवेश योग्यरित्या व्यवस्थापित करण्यासाठी सुरक्षा उपाय अमलात आणणे.
- डेटा गोपनीयता राखणारे आणि चांगले वापरकर्ता अनुभव देणारे AI एजंट तयार करणे.

## सुरक्षा

आपण प्रथम सुरक्षित एजंटिक अनुप्रयोग तयार करण्याकडे पाहूया. सुरक्षा म्हणजे AI एजंट डिझाइननुसार काम करतो. एजंटिक अनुप्रयोग तयार करणाऱ्यां म्हणून, आपल्याकडे सुरक्षितता वाढवण्यासाठी पद्धती आणि साधने आहेत:

### सिस्टम मेसेज फ्रेमवर्क तयार करणे

जर तुम्ही कधी मोठ्या भाषा मॉडेल्स (LLMs) वापरून AI अनुप्रयोग तयार केला असेल, तर तुम्हाला खात्री आहे की मजबूत सिस्टम प्रॉम्प्ट किंवा सिस्टम मेसेज डिझाइन करणे किती महत्त्वाचे आहे. हे प्रॉम्प्ट मेटा नियम, सूचना आणि मार्गदर्शक तत्त्वे तयार करतात ज्याद्वारे LLM वापरकर्ता आणि डेटाशी संवाद साधतो.

AI एजंटसाठी, सिस्टम प्रॉम्प्ट आणखी महत्त्वाचा असतो कारण AI एजंटसाठी आपण तयार केलेल्या कार्यांसाठी त्यांना अत्यंत विशिष्ट सूचना आवश्यक असतात.

स्केलेबल सिस्टम प्रॉम्प्ट तयार करण्यासाठी, आपण आमच्या अनुप्रयोगात एक किंवा अधिक एजंट तयार करण्यासाठी सिस्टम मेसेज फ्रेमवर्क वापरू शकतो:

![सिस्टम मेसेज फ्रेमवर्क तयार करणे](../../../translated_images/mr/system-message-framework.3a97368c92d11d68.webp)

#### पाऊल 1: मेटा सिस्टम मेसेज तयार करा

मेटा प्रॉम्प्टचा वापर LLM कडून एजंटसाठी सिस्टम प्रॉम्प्ट निर्माण करण्यासाठी केला जाईल. आपण ते टेम्प्लेट स्वरूपात डिझाइन करू जेणेकरून आवश्यक असल्यास अनेक एजंट्स सहज तयार करता येतील.

येथे LLM ला दिला जाणारा मेटा सिस्टम मेसेजचा एक उदाहरण आहे:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### पाऊल 2: प्राथमिक प्रॉम्प्ट तयार करा

पुढील पाऊल म्हणजे AI एजंटचे वर्णन करणारा प्राथमिक प्रॉम्प्ट तयार करणे. तुम्हाला एजंटची भूमिका, एजंट पूर्ण करेल अशा कार्ये आणि एजंटची इतर जबाबदाऱ्या समाविष्ट कराव्यात.

येथे एक उदाहरण आहे:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### पाऊल 3: LLM ला प्राथमिक सिस्टम मेसेज द्या

आता आपण हा सिस्टम मेसेज ऑप्टिमाइझ करू शकतो, ज्यासाठी मेटा सिस्टम मेसेज व आपल्या प्राथमिक सिस्टम मेसेजचा वापर केला जाईल.

यामुळे एक असे सिस्टम मेसेज तयार होईल जे AI एजंट मार्गदर्शनासाठी अधिक प्रभावी असेल:

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

#### पाऊल 4: पुनरावलोकन आणि सुधारणा करा

या सिस्टम मेसेज फ्रेमवर्कचे मूल्य म्हणजे अनेक एजंटकरिता सिस्टम मेसेज तयार करणे अधिक सोपे करणे तसेच आपल्या सिस्टम मेसेजांचा कालांतराने सुधारणा करणे. प्रथम वेळेस आपल्या सर्व वापर प्रकरणासाठी परिपूर्ण सिस्टम मेसेज असणे क्वचितच शक्य आहे. प्राथमिक सिस्टम मेसेज बदलून लहान बदल आणि सुधारणा करण्याची क्षमता आपल्याला निकाल तुलना आणि मूल्यमापन करण्यास सक्षम करते.

## धोके समजून घेणे

विश्वसनीय AI एजंट तयार करण्यासाठी, आपल्या AI एजंटवरील धोके आणि धमक्यांना समजून घेणे आणि त्यांचा सामना करणे महत्त्वाचे आहे. AI एजंटवरील काही वेगवेगळ्या धमक्यांकडे पाहू आणि त्यासाठी चांगली नियोजन आणि तयारी कशी करावी, ते पाहू.

![धमक्या समजून घेणे](../../../translated_images/mr/understanding-threats.89edeada8a97fc0f.webp)

### कार्य आणि सूचना

**वर्णन:** हल्लेखोर AI एजंटच्या सूचनांमध्ये किंवा उद्दिष्टांमध्ये बदल करण्याचा प्रयत्न करतात, प्रॉम्प्टिंग किंवा इनपुट्समध्ये फेरफार करून.

**तोडगा**: AI एजंट प्रक्रियेसाठी नेहमीच खतरनाक प्रॉम्प्ट्स शोधण्यासाठी सत्यापन तपासणी आणि इनपुट फिल्टर्स अंमलात आणा. या हल्ल्यांसाठी एजंटबरोबर वारंवार संपर्क आवश्यक असल्यामुळे, संभाषणातील वळणांची संख्या मर्यादित करणे हा हल्ल्यांपासून बचाव करण्याचा आणखी एक मार्ग आहे.

### महत्त्वाच्या सिस्टम्सचा प्रवेश

**वर्णन**: जर AI एजंटला संवेदनशील डेटा ठेवणाऱ्या सिस्टम्स आणि सेवा यांचा प्रवेश असेल, तर हल्लेखोर एजंट आणि या सेवांमधील संवाद बिघडवू शकतात. हे थेट हल्ले किंवा एजंटद्वारे या सिस्टम्सविषयी माहिती मिळवण्याच्या अप्रत्यक्ष प्रयत्न असू शकतात.

**तोडगा**: AI एजंटना केवळ आवश्यकता असल्यावरच सिस्टम्सचा प्रवेश असावा. एजंट आणि सिस्टममधील संवाद सुरक्षित असावा. प्रमाणीकरण आणि प्रवेश नियंत्रण लागू करणे हा या माहितीचे संरक्षण करण्याचा आणखी एक मार्ग आहे.

### संसाधने आणि सेवा अधिभार

**वर्णन:** AI एजंट विविध साधने आणि सेवा वापरून कार्य पूर्ण करतात. हल्लेखोर AI एजंट वापरून अनेक विनंत्या पाठवून या सेवांवर हल्ला करू शकतात, ज्यामुळे सिस्टम अपयशी ठरू शकतो किंवा खूप खर्च होऊ शकतो.

**तोडगा:** AI एजंट कडून सेवा कडे पाठविल्या जाणाऱ्या विनंत्यांची संख्या मर्यादित करण्यासाठी धोरणे तयार करा. संभाषणातील टर्न्स आणि AI एजंटकडे विनंतींची संख्या मर्यादित करणे हा हल्ल्यांपासून बचाव करण्याचा आणखी एक मार्ग आहे.

### ज्ञानसंग्रह विषारीकरण

**वर्णन:** या प्रकारचा हल्ला AI एजंटवर थेट हल्ला करत नाही, पण त्या एजंट वापरतील अशा ज्ञानसंग्रह आणि इतर सेवांवर हल्ला होतो. यात डेटा किंवा माहिती भ्रष्ट करणं समाविष्ट असू शकते, ज्यामुळे AI एजंट गैरप्रातिनिधिक किंवा अनपेक्षित प्रतिसाद देऊ शकतो.

**तोडगा:** AI एजंटच्या कार्यप्रवाहांमध्ये वापरल्या जाणाऱ्या डेटाची नियमित पडताळणी करा. या डेटाचा प्रवेश सुरक्षित असावा आणि फक्त विश्वासार्ह व्यक्तींनीच बदलावा, हे सुनिश्चित करा, ज्यामुळे अशा प्रकारच्या हल्ल्यांपासून बचाव होईल.

### साखळीसारखी चुका

**वर्णन:** AI एजंट विविध साधने आणि सेवा वापरून कार्य पूर्ण करतात. हल्लेखोरांमुळे होणाऱ्या चुका अशा इतर सिस्टम्सना अपयशी बनवू शकतात ज्यांच्याशी AI एजंट जोडलेला आहे, ज्यामुळे हल्ला अधिक प्रमाणात पसरतो आणि निवारण कठीण होते.

**तोडगा**: यापासून बचाव करण्याचा एक मार्ग म्हणजे AI एजंटला मर्यादित वातावरणात (उदा. डॉकर कंटेनरमध्ये) कार्य करण्यास सांगणे, ज्यामुळे थेट सिस्टमवर हल्ले होणार नाहीत. काही सिस्टम्स चुकांच्या प्रतिसादाने फिर्ता यंत्रणा आणि पुनर्प्रयत्न लॉजिक तयार करणे हा आणखी एक मार्ग आहे मोठ्या प्रणालीच्या अपयशापासून बचाव करण्याचा.

## मानव-इन-द-लूप

विश्वसनीय AI एजंट प्रणाली तयार करण्याचा आणखी एक प्रभावी मार्ग म्हणजे मानव-इन-द-लूप वापरणे. यामुळे वापरकर्त्यांना चालू असलेल्या एजंटला प्रतिक्रिया देण्याची संधी मिळते. वापरकर्ते बहु-एजंट प्रणालीतील एजंटसारखे काम करतात आणि चालू प्रक्रियेची मंजुरी देणे किंवा थांबवणे शक्य होते.

![मानव-इन-द-लूप](../../../translated_images/mr/human-in-the-loop.5f0068a678f62f4f.webp)

येथे मीक्रोसॉफ्ट एजंट फ्रेमवर्क वापरून हा संकल्पना कशी अमलात आणली जाते, याचा केलेला कोड उदाहरण:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# मानवी-इन-द-लूप मंजुरीसह प्रदाता तयार करा
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# मानवी मंजुरी टप्प्यासह एजंट तयार करा
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# वापरकर्ता प्रतिसाद पुनरावलोकन आणि मंजूर करू शकतो
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## निष्कर्ष

विश्वसनीय AI एजंट तयार करणे काळजीपूर्वक डिझाइन, मजबूत सुरक्षा उपाय आणि सातत्यपूर्ण पुनरावलोकन आवश्यक आहे. संरचित मेटा प्रॉम्प्टिंग प्रणाली, संभाव्य धमक्यांचा समज आणि प्रतिबंधात्मक धोरणे अमलात आणून, विकसक सुरक्षित आणि प्रभावी AI एजंट तयार करू शकतात. याशिवाय, मानव-इन-द-लूप दृष्टिकोन समाविष्ट केल्याने AI एजंट वापरकर्त्यांच्या गरजांसह समर्पित राहतात आणि धोके कमी होतात. AI सतत विकसित होत असताना, सुरक्षा, गोपनीयता आणि नैतिक विचारांवर सक्रिय लक्ष ठेवणे AI आधारित प्रणालींमध्ये विश्वास आणि विश्वसनीयता वाढविण्यासाठी महत्त्वाचे ठरेल.

## कोड नमुने

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): मेटा-प्रॉम्प्ट सिस्टम मेसेज फ्रेमवर्कचे टप्प्याटप्प्याने प्रदर्शन.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): विश्वसनीय एजंटसाठी प्री-ऍक्शन अप्रूव्हल गेट्स, धोका स्तर निर्धारण आणि ऑडिट लॉगिंग.

### विश्वसनीय AI एजंटच्या संदर्भात अधिक प्रश्न आहेत का?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) येथे सामील व्हा, इतर शिकणाऱ्यांशी भेटा, ऑफिस ऑवर्सला उपस्थित राहा आणि तुमचे AI एजंट प्रश्नांची उत्तरे मिळवा.

## अतिरिक्त संसाधने

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">जबाबदार AI चे आढावा</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">जनरेटिव्ह AI मॉडेल आणि AI अनुप्रयोग मूल्यांकन</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">सुरक्षितता सिस्टम मेसेजेस</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">धोका मूल्यांकन टेम्प्लेट</a>

## मागील धडा

[एजंटिक RAG](../05-agentic-rag/README.md)

## पुढील धडा

[योजना डिझाइन नमुना](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->