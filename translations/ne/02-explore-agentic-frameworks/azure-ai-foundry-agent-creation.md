# माइक्रोसफ्ट फाउन्ड्री एजेन्ट सेवा विकास

यस अभ्यासमा, तपाईं माइक्रोसफ्ट फाउन्ड्री एजेन्ट सेवा उपकरणहरू प्रयोग गरेर [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) मा फ्लाइट बुकिंगको लागि एक एजेन्ट सिर्जना गर्नुहुनेछ। एजेन्टले प्रयोगकर्तासँग अन्तरक्रिया गर्न र फ्लाइटहरूको बारेमा जानकारी प्रदान गर्न सक्षम हुनेछ।

## आवश्यकताहरू

यस अभ्यास पूरा गर्न तपाईंलाई तलका कुराहरू आवश्यक छन्:
1. एक सक्रिय सदस्यता भएको Azure खात। [निःशुल्क खाता सिर्जना गर्नुहोस्](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
2. तपाईंले माइक्रोसफ्ट फाउन्ड्री हब सिर्जना गर्ने अनुमति हुनुपर्छ वा तपाईंको लागि कुनै हब सिर्जना गरिएको हुनुपर्छ।
    - यदि तपाईंको भूमिका Contributor वा Owner हो भने, तपाईं यो ट्यूटोरियलका चरणहरू अनुसरण गर्न सक्नुहुन्छ।

## माइक्रोसफ्ट फाउन्ड्री हब सिर्जना गर्नुहोस्

> **सूचना:** माइक्रोसफ्ट फाउन्ड्रीलाई पहिले Azure AI Studio भनिन्थ्यो।

1. माइक्रोसफ्ट फाउन्ड्री सम्बन्धी [ब्लग पोस्ट](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) मा दिइएको मार्गनिर्देशनहरू पालना गरी माइक्रोसफ्ट फाउन्ड्री हब सिर्जना गर्नुहोस्।
2. तपाईंको परियोजनाले सिर्जना भएपछि, देखाइएको कुनै पनि सुझावहरू बन्द गर्नुहोस् र माइक्रोसफ्ट फाउन्ड्री पोर्टलमा परियोजना पृष्ठ पुनरावलोकन गर्नुहोस्, जुन तलको तस्वीरजस्तै देखिनुपर्छ:

    ![Microsoft Foundry Project](../../../translated_images/ne/azure-ai-foundry.88d0c35298348c2f.webp)

## मोडेल स्थापना गर्नुहोस्

1. परियोजनाको बाँया प्यानलमा, **My assets** सेक्सनमा, **Models + endpoints** पृष्ठ चयन गर्नुहोस्।
2. **Models + endpoints** पृष्ठमा, **Model deployments** ट्याबमा, **+ Deploy model** मेनूबाट **Deploy base model** चयन गर्नुहोस्।
3. सूचीबाट `gpt-5-mini` मोडेल खोज्नुहोस् र त्यसलाई चयन गरी पुष्टि गर्नुहोस्।

    > **सूचना**: TPM घटाउने कार्यले तपाईंले प्रयोग गरिरहेको सदस्यतामा उपलब्ध कोटा अत्यधिक प्रयोग हुनबाट बचाउछ।

    ![Model Deployed](../../../translated_images/ne/model-deployment.3749c53fb81e18fd.webp)

## एक एजेन्ट सिर्जना गर्नुहोस्

अब तपाईंले मोडेल स्थापना गरेपछि, तपाइँ एजेन्ट सिर्जना गर्न सक्नुहुन्छ। एजेन्ट भनेको संवादात्मक एआई मोडेल हो जुन प्रयोगकर्तासँग अन्तरक्रिया गर्न प्रयोग गर्न सकिन्छ।

1. परियोजनाको बाँया प्यानलमा, **Build & Customize** सेक्सनमा, **Agents** पृष्ठ चयन गर्नुहोस्।
2. नयाँ एजेन्ट सिर्जना गर्न **+ Create agent** क्लिक गर्नुहोस्। **Agent Setup** संवाद बक्समा:
    - एजेन्टको नाम लेख्नुहोस्, जस्तै `FlightAgent`।
    - पहिले सिर्जना गर्नुभएको `gpt-5-mini` मोडेल स्थापना चयन गरिएको छ भनेर सुनिश्चित गर्नुहोस्।
    - एजेन्टले पालना गर्नुपर्ने निर्देशनहरू **Instructions** मा सेट गर्नुहोस्। यहाँ एक उदाहरण छ:
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
> विस्तृत प्रॉम्प्टको लागि, तपाईं [यो रिपोजिटरी](https://github.com/ShivamGoyal03/RoamMind) मा थप जानकारी प्राप्त गर्न सक्नुहुन्छ।
    
> थप रूपमा, तपाईं एजेन्टको क्षमता बढाउन **Knowledge Base** र **Actions** थप्न सक्नुहुन्छ जसले प्रयोगकर्ताको अनुरोधअनुसार थप जानकारी दिने र स्वचालित कार्यहरू पूर्ति गर्नेछ। यो अभ्यासको लागि, यी चरणहरू छोड्न सकिन्छ।
    
![Agent Setup](../../../translated_images/ne/agent-setup.9bbb8755bf5df672.webp)

3. नयाँ बहु-एआई एजेन्ट बनाउन, केवल **New Agent** क्लिक गर्नुहोस्। नयाँ एजेन्ट त्यसपछि एजेन्टहरू पृष्ठमा देखिनेछ।


## एजेन्ट परीक्षण गर्नुहोस्

एजेन्ट सिर्जना गरेपछि, तपाईं यसलाई Microsoft Foundry पोर्टलको प्लेग्राउन्डमा प्रयोगकर्ताको प्रश्नहरूको जवाफ कसरी दिन्छ भनेर परीक्षण गर्न सक्नुहुन्छ।

1. एजेन्टको **Setup** प्यानलको माथि, **Try in playground** चयन गर्नुहोस्।
2. **Playground** प्यानलमा, तपाईं च्याट विन्डोमा प्रश्नहरू टाइप गरेर एजेन्टसँग अन्तरक्रिया गर्न सक्नुहुन्छ। उदाहरणका लागि, तपाइँ एजेन्टलाई सोध्न सक्नुहुन्छ कि सिएटलबाट न्यूयोर्क २८ मा उडानहरू खोज्नुहोस्।

    > **सूचना**: एजेन्टले सटीक उत्तर नदिन सक्छ किनभने यस अभ्यासमा कुनै वास्तविक-समय डेटा प्रयोग गरिएको छैन। उद्देश्य भनेको एजेन्टले दिइएका निर्देशनहरूको आधारमा प्रयोगकर्ताका प्रश्नहरू बुझ्न र जवाफ दिन सक्ने क्षमता परीक्षण गर्नु हो।

    ![Agent Playground](../../../translated_images/ne/agent-playground.dc146586de715010.webp)

3. एजेन्ट परीक्षणपछि, तपाईं थप अभिप्राय, प्रशिक्षण डेटा, र क्रियाहरू थपेर यसको क्षमता अझ बढाउन सक्नुहुन्छ।

## स्रोतहरू सफा गर्नुहोस्

एजेन्ट परीक्षण समाप्त भएपछि, थप खर्च हुन नदिन यसलाई मेटाउन सक्नुहुन्छ।
1. [Azure portal](https://portal.azure.com) खोल्नुहोस् र यस अभ्यासमा प्रयोग गरिएको हब स्रोतहरू रहेको स्रोत समूहको सामग्रीहरू हेर्नुहोस्।
2. टूलबारमा, **Delete resource group** चयन गर्नुहोस्।
3. स्रोत समूहको नाम प्रविष्ट गरी मेटाउन चाहनु भएको पुष्टि गर्नुहोस्।

## स्रोतहरू

- [Microsoft Foundry कागजात](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry पोर्टल](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry सँग सुरूवात](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure मा AI एजेन्टको आधारभूत सिद्धान्तहरू](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->