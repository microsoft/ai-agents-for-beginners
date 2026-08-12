# मायक्रोसॉफ्ट फाउंड्री एजंट सेवा विकास

या व्यायामात, तुम्ही [मायक्रोसॉफ्ट फाउंड्री पोर्टल](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) मध्ये मायक्रोसॉफ्ट फाउंड्री एजंट सेवा साधने वापरून फ्लाइट बुकिंगसाठी एक एजंट तयार करता. एजंट वापरकर्त्यांशी संवाद साधू शकतो आणि फ्लाइट्स विषयी माहिती देऊ शकतो.

## पूर्वअट

हा व्यायाम पूर्ण करण्यासाठी, तुमच्याकडे खालील गोष्टी असणे आवश्यक आहेत:
1. सक्रिय सदस्यत्व असलेले Azure खाते. [मोफत खाते तयार करा](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. तुम्हाला मायक्रोसॉफ्ट फाउंड्री हब तयार करण्याची परवानगी असणे आवश्यक आहे किंवा तुमच्यासाठी एक तयार करावे लागेल.
    - तुमची भूमिका Contributor किंवा Owner असल्यास, तुम्ही या ट्यूटोरियलमधील चरणांचे अनुसरण करू शकता.

## मायक्रोसॉफ्ट फाउंड्री हब तयार करा

> **टीप:** मायक्रोसॉफ्ट फाउंड्री पूर्वी Azure AI Studio म्हणून ओळखले जात असे.

1. मायक्रोसॉफ्ट फाउंड्री हब तयार करण्यासाठी [मायक्रोसॉफ्ट फाउंड्री](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) ब्लॉग पोस्ट मधील मार्गदर्शक तत्त्वांचे अनुसरण करा.
2. तुमचा प्रकल्प तयार झाल्यानंतर, दर्शविलेली कोणतीही टीप बंद करा आणि मायक्रोसॉफ्ट फाउंड्री पोर्टलमध्ये प्रकल्प पृष्ठ पाहा, जे खालील चित्रासारखे दिसायला पाहिजे:

    ![Microsoft Foundry Project](../../../translated_images/mr/azure-ai-foundry.88d0c35298348c2f.webp)

## मॉडेल तैनात करा

1. तुमच्या प्रकल्पासाठी डाव्या बाजूच्या पॅनेलमध्ये, **My assets** विभागात, **Models + endpoints** पृष्ठ निवडा.
2. **Models + endpoints** पृष्ठात, **Model deployments** टॅबमध्ये, **+ Deploy model** मेनूमध्ये, **Deploy base model** निवडा.
3. `gpt-5-mini` मॉडेल यादीत शोधा, नंतर ते निवडा आणि पुष्टी करा.

    > **टीप**: TPM कमी केल्याने तुम्ही वापरत असलेल्या सदस्यत्वातील कोटाचा अति वापर टाळता येतो.

    ![Model Deployed](../../../translated_images/mr/model-deployment.3749c53fb81e18fd.webp)

## एजंट तयार करा

आता तुम्ही मॉडेल तैनात केले आहे, तुम्ही एजंट तयार करू शकता. एजंट हा संवादात्मक AI मॉडेल आहे जो वापरकर्त्यांशी संवाद करता येतो.

1. तुमच्या प्रकल्पासाठी डाव्या बाजूच्या पॅनेलमध्ये, **Build & Customize** विभागात, **Agents** पृष्ठ निवडा.
2. नवीन एजंट तयार करण्यासाठी **+ Create agent** क्लिक करा. **Agent Setup** संवाद बॉक्समध्ये:
    - एजंटसाठी नाव द्या, जसे की `FlightAgent`.
    - पूर्वी तुम्ही तयार केलेले `gpt-5-mini` मॉडेल तैनाती निवडा
    - एजंटने अनुसरण करावयाचा प्रॉम्प्ट म्हणून **Instructions** सेट करा. येथे एक उदाहरण आहे:
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
> सविस्तर प्रॉम्प्टसाठी, तुम्ही [या रिपॉजिटरी](https://github.com/ShivamGoyal03/RoamMind) तपासू शकता अधिक माहितीसाठी.
    
> शिवाय, तुम्ही एजंटच्या क्षमता वाढवण्यासाठी **Knowledge Base** आणि **Actions** जोडू शकता जे वापरकर्त्यांच्या विनंतीनुसार अधिक माहिती प्रदान करतात आणि स्वयंचलित कार्ये पार पाडतात. या व्यायामासाठी, तुम्ही हे टप्पे टाळू शकता.
    
![Agent Setup](../../../translated_images/mr/agent-setup.9bbb8755bf5df672.webp)

3. नवीन मल्टि-AI एजंट तयार करण्यासाठी, फक्त **New Agent** क्लिक करा. नवीन तयार एजंट नंतर Agents पृष्ठावर दिसेल.


## एजंटची चाचणी

एजंट तयार केल्यानंतर, तुम्ही त्याची तपासणी करू शकता की ते वापरकर्त्यांच्या प्रश्नांना कसे प्रतिसाद देते मायक्रोसॉफ्ट फाउंड्री पोर्टल प्लेग्राउंडमध्ये.

1. एजंटसाठी **Setup** पॅनेलच्या शीर्षस्थानी, **Try in playground** निवडा.
2. **Playground** पॅनेलमध्ये, तुम्ही चॅट विंडोमध्ये प्रश्न टाकून एजंटशी संवाद साधू शकता. उदाहरणार्थ, तुम्ही एजंटला विचारू शकता 28 तारखेला सिएटलपासून न्यूयॉर्कला फ्लाइट शोधा.

    > **टीप**: एजंट अचूक प्रतिसाद देऊ शकणार नाही, कारण या व्यायामात कोणताही रियल-टाइम डेटा वापरला जात नाही. उद्देश एजंटच्या वापरकर्त्यांच्या प्रश्नांना दिलेल्या सूचनांवर आधारित समजून घेण्याची आणि प्रतिसाद देण्याची क्षमता तपासणे आहे.

    ![Agent Playground](../../../translated_images/mr/agent-playground.dc146586de715010.webp)

3. एजंटची चाचणी केल्यानंतर, तुम्ही त्यात अधिक हेतू, प्रशिक्षण डेटा आणि कृती जोडून त्याच्या क्षमता वाढवू शकता.

## संसाधने स्वच्छ करा

एजंटची चाचणी पूर्ण झाल्यावर, अतिरिक्त खर्च टाळण्यासाठी तुम्ही तो हटवू शकता.
1. [Azure portal](https://portal.azure.com) उघडा आणि त्या रिसोर्स ग्रुपची सामग्री पहा ज्यात तुम्ही या व्यायामासाठी हब संसाधने तैनात केली आहेत.
2. टूलबारवर, **Delete resource group** निवडा.
3. रिसोर्स ग्रुपचे नाव टाका आणि हटवण्याची पुष्टी करा.

## संसाधने

- [मायक्रोसॉफ्ट फाउंड्री दस्तऐवजीकरण](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [मायक्रोसॉफ्ट फाउंड्री पोर्टल](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [मायक्रोसॉफ्ट फाउंड्री सह प्रारंभ करणे](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure वरील AI एजंट्सचे मूलतत्त्व](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI डिस्कॉर्ड](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->