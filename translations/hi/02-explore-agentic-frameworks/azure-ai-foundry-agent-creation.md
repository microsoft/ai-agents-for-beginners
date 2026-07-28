# Microsoft Foundry एजेंट सेवा विकास

इस अभ्यास में, आप [Microsoft Foundry पोर्टल](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) में Microsoft Foundry एजेंट सेवा टूल्स का उपयोग कर Flight Booking के लिए एक एजेंट बनाएंगे। एजेंट उपयोगकर्ताओं के साथ बातचीत करने और उड़ानों के बारे में जानकारी प्रदान करने में सक्षम होगा।

## आवश्यकताएँ

इस अभ्यास को पूरा करने के लिए, आपके पास निम्नलिखित होने चाहिए:
1. एक Azure खाता जिसमें एक सक्रिय सदस्यता हो। [मुफ्त में खाता बनाएं](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
2. आपके पास Microsoft Foundry हब बनाने की अनुमति हो या आपके लिए एक बनाया गया हो।
    - यदि आपकी भूमिका Contributor या Owner है, तो आप इस ट्यूटोरियल में दिए चरणों का पालन कर सकते हैं।

## Microsoft Foundry हब बनाएं

> **टिप्पणी:** Microsoft Foundry पहले Azure AI Studio के नाम से जाना जाता था।

1. Microsoft Foundry हब बनाने के लिए [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) ब्लॉग पोस्ट से इन निर्देशों का पालन करें।
2. जब आपका प्रोजेक्ट बन जाए, तो प्रदर्शित किसी भी टिप्स को बंद करें और Microsoft Foundry पोर्टल में प्रोजेक्ट पेज की समीक्षा करें, जो निम्न छवि के समान दिखना चाहिए:

    ![Microsoft Foundry Project](../../../translated_images/hi/azure-ai-foundry.88d0c35298348c2f.webp)

## एक मॉडल तैनात करें

1. अपने प्रोजेक्ट के बाएँ पेन में, **My assets** अनुभाग में, **Models + endpoints** पेज चुनें।
2. **Models + endpoints** पेज में, **Model deployments** टैब में, **+ Deploy model** मेनू से **Deploy base model** चुनें।
3. सूची में `gpt-5-mini` मॉडल खोजें, फिर इसे चुनें और पुष्टि करें।

    > **टिप्पणी**: TPM कम करने से आप उपयोग की जा रही सदस्यता में उपलब्ध कोटा का अत्यधिक उपयोग करने से बच सकते हैं।

    ![Model Deployed](../../../translated_images/hi/model-deployment.3749c53fb81e18fd.webp)

## एक एजेंट बनाएं

अब जब आपने एक मॉडल तैनात कर लिया है, तो आप एक एजेंट बना सकते हैं। एजेंट एक वार्तालाप AI मॉडल है जिसे उपयोगकर्ताओं के साथ बातचीत के लिए उपयोग किया जाता है।

1. अपने प्रोजेक्ट के बाएँ पेन में, **Build & Customize** अनुभाग में, **Agents** पेज चुनें।
2. नया एजेंट बनाने के लिए **+ Create agent** पर क्लिक करें। **Agent Setup** संवाद बॉक्स में:
    - एजेंट के लिए एक नाम दर्ज करें, जैसे `FlightAgent`।
    - सुनिश्चित करें कि आपने पहले जो `gpt-5-mini` मॉडल तैनात किया था, वह चयनित हो।
    - एजेंट को पालन करने के लिए निर्देश (Instructions) अपने अनुसार सेट करें। यहाँ एक उदाहरण है:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> अधिक विस्तृत प्रॉम्प्ट के लिए, आप [इस रिपॉजिटरी](https://github.com/ShivamGoyal03/RoamMind) को देख सकते हैं।
    
> इसके अलावा, आप एजेंट की क्षमताओं को बढ़ाने के लिए **Knowledge Base** और **Actions** जोड़ सकते हैं ताकि वह अधिक जानकारी प्रदान कर सके और उपयोगकर्ता के अनुरोधों के अनुसार स्वचालित कार्य कर सके। इस अभ्यास के लिए, आप इन चरणों को छोड़ सकते हैं।
    
![Agent Setup](../../../translated_images/hi/agent-setup.9bbb8755bf5df672.webp)

3. नया मल्टी-AI एजेंट बनाने के लिए सीधे **New Agent** पर क्लिक करें। नया बनाया गया एजेंट Agents पेज पर दिखाई देगा।


## एजेंट का परीक्षण करें

एजेंट बनाने के बाद, आप Microsoft Foundry पोर्टल के playground में परीक्षण कर सकते हैं कि वह उपयोगकर्ता प्रश्नों का कैसे उत्तर देता है।

1. अपने एजेंट के **Setup** पेन के शीर्ष पर, **Try in playground** चुनें।
2. **Playground** पेन में, आप चैट विंडो में प्रश्न टाइप करके एजेंट से बातचीत कर सकते हैं। उदाहरण के लिए, आप एजेंट से 28 तारीख को सिएटल से न्यूयॉर्क की उड़ानें खोजने को कह सकते हैं।

    > **टिप्पणी**: एजेंट सटीक उत्तर नहीं दे सकता है क्योंकि इस अभ्यास में वास्तविक समय का डेटा उपयोग नहीं किया जा रहा है। उद्देश्य एजेंट की उपयोगकर्ता प्रश्नों को समझने और दिए गए निर्देशों के अनुसार उत्तर देने की क्षमता का परीक्षण करना है।

    ![Agent Playground](../../../translated_images/hi/agent-playground.dc146586de715010.webp)

3. एजेंट का परीक्षण करने के बाद, आप इसे और बेहतर बनाने के लिए अधिक intents, प्रशिक्षण डेटा और actions जोड़ सकते हैं।

## संसाधनों को साफ़ करें

एजेंट का परीक्षण पूरा होने पर, अतिरिक्त लागत से बचने के लिए आप इसे हटा सकते हैं।
1. [Azure पोर्टल](https://portal.azure.com) खोलें और उस रिसोर्स ग्रुप की सामग्री देखें जहाँ आपने इस अभ्यास में हब संसाधन तैनात किए हैं।
2. टूलबार में, **Delete resource group** चुनें।
3. संसाधन समूह का नाम दर्ज करें और पुष्टि करें कि आप इसे हटाना चाहते हैं।

## संसाधन

- [Microsoft Foundry प्रलेखन](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry पोर्टल](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry के साथ शुरूआत](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure पर AI एजेंटों के मूल सिद्धांत](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->