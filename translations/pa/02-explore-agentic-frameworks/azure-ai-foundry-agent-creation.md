# ਮਾਈਕ੍ਰੋਸੌਫਟ ਫਾਊਂਡਰੀ ਏਜੰਟ ਸਰਵਿਸ ਵਿਕਾਸ

ਇਸ ਕਸਰਤ ਵਿੱਚ, ਤੁਸੀਂ [Microsoft Foundry ਪੋਰਟਲ](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) ਵਿੱਚ Microsoft Foundry ਏਜੰਟ ਸਰਵਿਸ ਟੂਲਜ਼ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਲਾਈਟ ਬੁਕਿੰਗ ਲਈ ਇੱਕ ਏਜੰਟ ਬਣਾਉਂਦੇ ਹੋ। ਏਜੰਟ ਯੂਜ਼ਰਾਂ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕੇਗਾ ਅਤੇ ਫਲਾਈਟਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰੇਗਾ।

## ਸ਼ਰਤਾਂ

ਇਸ ਕਸਰਤ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ ਹੇਠ ਲਿਖੀਆਂ ਚੀਜ਼ਾਂ ਦੀ ਲੋੜ ਹੈ:
1. ਇਕ Azure ਖਾਤਾ ਜਿਸ ਵਿੱਚ ਐਕਟਿਵ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਹੋਵੇ। [ਮੁਫ਼ਤ ਲਈ ਖਾਤਾ ਬਣਾਓ](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)।
2. ਤੁਹਾਨੂੰ Microsoft Foundry ਹੱਬ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦੀ ਲੋੜ ਹੈ ਜਾਂ ਤੁਹਾਡੇ ਲਈ ਇੱਕ ਬਣਾਇਆ ਗਿਆ ਹੋਵੇ।
    - ਜੇ ਤੁਹਾਡਾ ਰੋਲ ਕਨਟ੍ਰੀਬਿਊਟਰ ਜਾਂ ਓਨਰ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਇਸ ਟਿਊਟੋਰਿਯਲ ਵਿੱਚ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰ ਸਕਦੇ ਹੋ।

## Microsoft Foundry ਹੱਬ ਬਣਾਓ

> **ਨੋਟ:** Microsoft Foundry ਨੂੰ ਪਹਿਲਾਂ Azure AI Studio ਦੇ ਨਾਮ ਨਾਲ ਜਾਣਿਆ ਜਾਂਦਾ ਸੀ।

1. Microsoft Foundry ਬਲੋਗ ਪੋਸਟ ਤੋਂ ਹੇਠ ਲਿਖੀਆਂ ਹਦਾਇਤਾਂ ਦੀ ਪਾਲਣਾ ਕਰੋ [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) ਹੱਬ ਬਣਾਉਣ ਲਈ।
2. ਜਦੋਂ ਤੁਹਾਡਾ ਪ੍ਰੋਜੈਕਟ ਬਣ ਜਾਏ, ਤਦ ਪ੍ਰਦਰਸ਼ਿਤ ਕਿਸੇ ਵੀ ਟਿੱਪ ਨੂੰ ਬੰਦ ਕਰੋ ਅਤੇ Microsoft Foundry ਪੋਰਟਲ ਵਿੱਚ ਪ੍ਰੋਜੈਕਟ ਸਫ਼ਾ ਸਮੀਖਿਆ ਕਰੋ, ਜੋ ਕਿ ਹੇਠ ਦਿੱਤੀ ਤਸਵੀਰ ਵਾਲਾ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ:

    ![Microsoft Foundry Project](../../../translated_images/pa/azure-ai-foundry.88d0c35298348c2f.webp)

## ਮਾਡਲ ਤਾਇਨਾਤ ਕਰੋ

1. ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਲਈ ਖੱਬੇ ਪੈਨ ਵਿੱਚ, **ਮੇਰੇ ਅਸੈੱਟ्स** ਸੈਕਸ਼ਨ ਵਿੱਚ, **ਮਾਡਲ + ਐਂਡਪਾਈਂਟਸ** ਪৃষ্ঠা ਚੁਣੋ।
2. **ਮਾਡਲ + ਐਂਡਪਾਈਂਟਸ** ਪੰਨੇ ਵਿੱਚ, **ਮਾਡਲ ਤਾਇਨਾਤੀ** ਟੈਬ ਵਿੱਚ, **+ ਮਾਡਲ ਤਾਇਨਾਤ ਕਰੋ** ਮੀਨੂ ਵਿੱਚੋਂ, **ਬੇਸ ਮਾਡਲ ਤਾਇਨਾਤ ਕਰੋ** ਚੁਣੋ।
3. ਸੂਚੀ ਵਿੱਚ `gpt-5-mini` ਮਾਡਲ ਲਈ ਖੋਜ ਕਰੋ, ਫਿਰ ਚੁਣੋ ਅਤੇ ਪੁਸ਼ਟੀ ਕਰੋ।

    > **ਨੋਟ**: TPM ਘਟਾਉਣਾ ਤੁਹਾਡੇ ਵਰਤ ਰਹੇ ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਵਿੱਚ ਉਪਲਬਧ ਕੋਟਾ ਦੇ ਵੱਧ ਵਰਤੋਂ ਤੋਂ ਬਚਾਉਂਦਾ ਹੈ।

    ![Model Deployed](../../../translated_images/pa/model-deployment.3749c53fb81e18fd.webp)

## ਇੱਕ ਏਜੰਟ ਬਣਾਓ

ਹੁਣ ਜਦੋਂ ਤੁਸੀਂ ਮਾਡਲ ਤਾਇਨਾਤ ਕਰ ਚੁੱਕੇ ਹੋ, ਤੁਸੀਂ ਇੱਕ ਏਜੰਟ ਬਣਾਉਂ ਸਕਦੇ ਹੋ। ਏਜੰਟ ਇੱਕ ਗੱਲਬਾਤੀ AI ਮਾਡਲ ਹੈ ਜੋ ਯੂਜ਼ਰਾਂ ਨਾਲ ਸੰਵਾਦ ਕਰ ਸਕਦਾ ਹੈ।

1. ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਲਈ ਖੱਬੇ ਪੈਨ ਵਿੱਚ, **ਬਿਲਡ ਅਤੇ ਕਸਟਮਾਈਜ਼** ਸੈਕਸ਼ਨ ਵਿੱਚ, **ਏਜੰਟਸ** ਪੰਨਾ ਚੁਣੋ।
2. ਨਵਾਂ ਏਜੰਟ ਬਣਾਉਣ ਲਈ **+ ਏਜੰਟ ਬਣਾਓ** 'ਤੇ ਕਲਿੱਕ ਕਰੋ। **ਏਜੰਟ ਸੈਟਅੱਪ** ਡਾਇਲਾਗ ਬਾਕਸ ਵਿੱਚ:
    - ਏਜੰਟ ਲਈ ਇੱਕ ਨਾਮ ਦਿਓ, ਜਿਵੇਂ ਕਿ `FlightAgent`।
    - ਪੱਕਾ ਕਰੋ ਕਿ ਪਹਿਲਾਂ ਬਣਾਈ ਗਈ `gpt-5-mini` ਮਾਡਲ ਤਾਇਨਾਤੀ ਚੁਣੀ ਗਈ ਹੈ।
    - **ਨਿਰਦੇਸ਼** ਨੂੰ ਉਸ ਪ੍ਰੰਪਟ ਦੇ ਅਨੁਸਾਰ ਸੈੱਟ ਕਰੋ ਜਿਸਨੂੰ ਤੁਸੀਂ ਏਜੰਟ ਨੂੰ ਫੋਲੋ ਕਰਵਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ। ਮਿਸਾਲ ਵਜੋਂ ਇਹ ਹੈ:
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
> ਵਾਰੀਕ ਪਰੰਪਟ ਲਈ, ਤੁਸੀਂ [ਇਸ ਰਿਪੋਜ਼ਿਟਰੀ](https://github.com/ShivamGoyal03/RoamMind) ਵਿੱਚ ਹੋਰ ਜਾਣਕਾਰੀ ਵੇਖ ਸਕਦੇ ਹੋ।
    
> ਇਸਦੇ ਅਲਾਵਾ, ਤੁਸੀਂ ਏਜੰਟ ਦੀ ਸਮਰੱਥਾ ਵਧਾਉਣ ਲਈ **ਜਾਣਕਾਰੀ ਅਧਾਰ** ਅਤੇ **ਕਿਰਿਆਵਾਂ** ਭੀ ਜੋੜ ਸਕਦੇ ਹੋ, ਜਿਸ ਨਾਲ ਯੂਜ਼ਰ ਅਨੁਰੋਧਾਂ ਦੇ ਆਧਾਰ 'ਤੇ ਹੋਰ ਜਾਣਕਾਰੀ ਦੇਣ ਅਤੇ ਸੁਚਾਲਿਤ ਕੰਮ ਕਰਨ ਵਿੱਚ ਸਹਾਇਤਾ ਮਿਲੇਗੀ। ਇਸ ਕਸਰਤ ਲਈ, ਤੁਸੀਂ ਇਹ ਕਦਮ ਛੱਡ ਸਕਦੇ ਹੋ।
    
![Agent Setup](../../../translated_images/pa/agent-setup.9bbb8755bf5df672.webp)

3. ਇੱਕ ਨਵਾਂ ਮਲਟੀ-AI ਏਜੰਟ ਬਣਾਉਣ ਲਈ ਸਿਰਫ਼ **ਨਵਾਂ ਏਜੰਟ** 'ਤੇ ਕਲਿੱਕ ਕਰੋ। ਨਵਾਂ ਬਣਿਆ ਏਜੰਟ ਫਿਰ ਏਜੰਟਸ ਪੰਨੇ 'ਤੇ ਦਿਖਾਈ ਦੇਵੇਗਾ।


## ਏਜੰਟ ਦਾ ਪਰੀਖਣ ਕਰੋ

ਏਜੰਟ ਬਣਾਉਣ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਇਸਨੂੰ ਟੈਸਟ ਕਰ ਸਕਦੇ ਹੋ ਕਿ ਇਹ Microsoft Foundry ਪੋਰਟਲ ਦੇ ਖੇਡ ਮੈਦਾਨ ਵਿੱਚ ਯੂਜ਼ਰ ਪੁੱਛੀਆਂ ਦਾ ਕਿਵੇਂ ਜਵਾਬ ਦਿੰਦਾ ਹੈ।

1. ਆਪਣੇ ਏਜੰਟ ਲਈ **ਸੈਟਅੱਪ** ਪੈਨ ਦੇ ਸਿਰ 'ਤੇ, **ਖੇਡ ਮੈਦਾਨ ਵਿੱਚ ਕੋਸ਼ਿਸ਼ ਕਰੋ** ਚੁਣੋ।
2. **ਖੇਡ ਮੈਦਾਨ** ਪੈਨ ਵਿੱਚ, ਤੁਸੀਂ ਚੈਟ ਵਿਂਡੋ ਵਿੱਚ ਪੁੱਛੀਆਂ ਟਾਈਪ ਕਰਕੇ ਏਜੰਟ ਨਾਲ ਗੱਲਬਾਤ ਕਰ ਸਕਦੇ ਹੋ। ਉਦਾਹਰਨ ਵਜੋਂ, ਤੁਸੀਂ ਏਜੰਟ ਤੋਂ 28 ਤਾਰੀਖ ਨੂੰ ਸਿਐਟਲ ਤੋਂ ਨ੍ਯੂਯਾਰਕ ਲਈ ਫਲਾਈਟ ਲੱਭਣ ਲਈ ਕਹਿ ਸਕਦੇ ਹੋ।

    > **ਨੋਟ**: ਏਜੰਟ ਸਹੀ ਜਵਾਬ ਨਹੀਂ ਦੇ ਸਕਦਾ ਕਿਉਂਕਿ ਇਸ ਕਸਰਤ ਵਿੱਚ ਕਿਸੇ ਸਰਗਰਮ ਡੇਟਾ ਦਾ ਉਪਯੋਗ ਨਹੀਂ ਹੋ ਰਿਹਾ। ਮਕਸਦ ਇਹ ਦੇਖਣਾ ਹੈ ਕਿ ਏਜੰਟ ਦਿਤੀਆਂ ਗਈਆਂ ਹਦਾਇਤਾਂ ਦੇ ਅਧਾਰ 'ਤੇ ਯੂਜ਼ਰ ਦੀਆਂ ਪੁੱਛੀਆਂ ਨੂੰ ਸਮਝ ਸਕਦਾ ਹੈ ਅਤੇ ਜਵਾਬ ਦੇ ਸਕਦਾ ਹੈ।

    ![Agent Playground](../../../translated_images/pa/agent-playground.dc146586de715010.webp)

3. ਟੈਸਟ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਹੋਰ ਮਨਚਾਹੇ ਇਰਾਦੇ, ਟ੍ਰੇਨਿੰਗ ਡੇਟਾ, ਅਤੇ ਕਿਰਿਆਵਾਂ ਜੋੜ ਕੇ ਇਸਦੀ ਸਮਰੱਥਾ ਵਧਾ ਸਕਦੇ ਹੋ।

## ਸਾਧਨਾਂ ਨੂੰ ਸਾਫ ਕਰੋ

ਜਦੋਂ ਤੁਸੀਂ ਏਜੰਟ ਦੀ ਟੈਸਟਿੰਗ ਮੁਕੰਮਲ ਕਰ ਲੈਂਦੇ ਹੋ, ਤਾਂ ਅਤਿਰਿਕਤ ਖਰਚਿਆਂ ਤੋਂ ਬਚਣ ਲਈ ਇਸਨੂੰ ਮਿਟਾ ਸਕਦੇ ਹੋ।
1. [Azure ਪੋਰਟਲ](https://portal.azure.com) ਖੋਲ੍ਹੋ ਅਤੇ ਉਸ ਰਿਸੋਰਸ ਗਰੂਪ ਦੀ ਸਮੱਗਰੀ ਵੇਖੋ ਜਿੱਥੇ ਤੁਸੀਂ ਇਸ ਕਸਰਤ ਲਈ ਹੱਬ ਸਾਧਨ ਤਾਇਨਾਤ ਕੀਤੇ ਸਨ।
2. ਟੂਲਬਾਰ 'ਤੇ, **ਰਿਸੋਰਸ ਗਰੂਪ ਮਿਟਾਓ** ਚੁਣੋ।
3. ਰਿਸੋਰਸ ਗਰੂਪ ਦਾ ਨਾਮ ਦਾਖਲ ਕਰੋ ਅਤੇ ਪੁਸ਼ਟੀ ਕਰੋ ਕਿ ਤੁਸੀਂ ਇਸਨੂੰ ਮਿਟਾਉਣਾ ਚਾਹੁੰਦੇ ਹੋ।

## ਸਾਧਨ

- [Microsoft Foundry ਦਸਤਾਵੇਜ਼](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry ਪੋਰਟਲ](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry ਨਾਲ ਸ਼ੁਰੂਆਤ](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure 'ਤੇ AI ਏਜੰਟਸ ਦੀਆਂ ਬੁਨਿਆਦਾਂ](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪਣ**:
ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਅਨੁਵਾਦ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾਵਾਂ ਲਈ ਯਤਨਸ਼ੀਲ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮੱਤਿਆਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜਵਾਬਦੇਹ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->