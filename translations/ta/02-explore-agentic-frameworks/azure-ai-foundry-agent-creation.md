# Microsoft Foundry முகவர் சேவை மேம்பாடு

இந்த பயிற்சியில், நீங்கள் [Microsoft Foundry போர்டல்](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) இல் Microsoft Foundry முகவர் சேவை கருவிகளை பயன்படுத்தி Flight Booking க்கான முகவரை உருவாக்குகிறீர்கள். இந்த முகவர் பயனர்களுடன் தொடர்பு கொண்டு விமானங்களைப் பற்றி தகவல்களை வழங்கக்கூடியது.

## முன்னோட்டங்கள்

இந்த பயிற்சியை முடிக்க, உங்களுக்கு பின்வரும் தேவை:
1. ஒரு செயல்பாட்டிலுள்ள சந்தா கொண்ட Azure கணக்கு. [ஒரு கணக்கை இலவசமாக உருவாக்கவும்](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. நீங்கள் Microsoft Foundry ஹப் உருவாக்கும் உரிமைகள் அல்லது உங்களுக்காக ஒன்று உருவாக்கப்பட்டிருக்க வேண்டும்.
    - உங்கள் பங்கு Contributor அல்லது Owner என்றால், இந்த பயிற்சியின் படிகளை நீங்கள் பின்பற்றலாம்.

## Microsoft Foundry ஹப் உருவாக்கு

> **குறிப்பு:** Microsoft Foundry முன் பெயர் Azure AI Studio ஆகும்.

1. Microsoft Foundryவை உருவாக்க [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) வலைப்பதிவிலிருந்து வழிகாட்டுதல்களை பின்பற்றுங்கள்.
2. உங்கள் திட்டம் உருவாக்கப்பட்டதும், காட்டப்படும் எந்தவொரு குறிப்பையும் மூடுங்கள் மற்றும் Microsoft Foundry போர்டலில் உள்ள திட்டப் பக்கத்தை பரிசீலியுங்கள், அது பின்வருமாறு தோன்றும்:

    ![Microsoft Foundry Project](../../../translated_images/ta/azure-ai-foundry.88d0c35298348c2f.webp)

## ஒரு மாதிரியை வைக்கும்

1. உங்கள் திட்டத்தின் இடது பக்க பட்டையில், **My assets** பகுதியின் கீழ், **Models + endpoints** பக்கத்தை தேர்வு செய்யவும்.
2. **Models + endpoints** பக்கத்தில், **Model deployments** தாவலில், **+ Deploy model** மெனுவில், **Deploy base model** ஐ தேர்ந்தெடுக்கவும்.
3. பட்டியலில் `gpt-4.1-mini` மாதிரியை தேடி, அதைத் தேர்ந்தெடுத்து உறுதிசெய்யவும்.

    > **குறிப்பு**: TPM ஐ குறைப்பது நீங்கள் பயன்படுத்தும் சந்தாவில் கிடைக்கும் கொட்டாவை அதிகமாக பயன்படுத்த வேண்டாமென உதவும்.

    ![Model Deployed](../../../translated_images/ta/model-deployment.3749c53fb81e18fd.webp)

## ஒரு முகவரை உருவாக்கவும்

இப்போது நீங்கள் ஒரு மாதிரியை வைத்துவிட்டீர்கள், நீங்கள் ஒரு முகவரை உருவாக்கலாம். முகவர் என்பது பயனர்களுடன் உரையாடும் AI மாதிரி ஆகும்.

1. உங்கள் திட்டத்தின் இடது பக்க பட்டையில், **Build & Customize** பகுதியின் கீழ், **Agents** பக்கத்தை தேர்ந்தெடுக்கவும்.
2. புதிய முகவரை உருவாக்க **+ Create agent** ஐ கிளிக் செய்யவும். **Agent Setup** உரையாடல் பெட்டியில்:
    - முகவருக்கு, எடுத்துக்காட்டு `FlightAgent` என்று ஒரு பெயரை உள்ளிடவும்.
    - முன்பு உருவாக்கிய `gpt-4.1-mini` மாதிரி நியமனத்தை தேர்ந்தெடுக்கவும்
    - முகவர் பின்பற்ற விரும்பும் அறிவுரைகள் (Instructions) ஐ அமைக்கவும். உதாரணமாக இதுபோன்றது:
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
> விரிவான அறிவுரைக்காக, [இந்த தொகுப்பு](https://github.com/ShivamGoyal03/RoamMind) ஐ பார்க்கலாம்.
    
> மேலும், முகவரின் திறன்களை மேம்படுத்த **Knowledge Base** மற்றும் **Actions** ஐ சேர்க்கலாம். இந்த பயிற்சிக்காக, நீங்கள் இந்த படிகளைக் கடக்கலாம்.
    
![Agent Setup](../../../translated_images/ta/agent-setup.9bbb8755bf5df672.webp)

3. புதிய பல-AI முகவரை உருவாக்க, **New Agent** ஐ கிளிக் செய்யவும். புதிய முகவர் Agents பக்கத்தில் காட்டப்படும்.


## முகவரை பரிசோதிக்கவும்

முகவரை உருவாக்கிய பின்னர், அது Microsoft Foundry போர்டல் விளையாட்டு பகுதிக்கு பயனர் கேள்விகளுக்கு எப்படி பதிலளிக்கிறது என்பதை பரிசோதிக்கலாம்.

1. உங்கள் முகவருக்கான **Setup** பகுதியில், மேல் பகுதியில், **Try in playground** ஐ தேர்ந்தெடுக்கவும்.
2. **Playground** பகுதியில், உரையாடல் சாளரத்தில் கேள்விகளைத் تایப்பிட்டு முகவருடன் தொடர்பு கொள்ளலாம். உதாரணமாக, 28ம் தேதி Seattle இருந்து New Yorkக்கு விமானங்களை தேட முகவரை கேட்டுக்கொள்ளலாம்.

    > **குறிப்பு**: இந்த பயிற்சியில் நேரடி தரவு பயன்படுத்தப்படவில்லை என்பதால் முகவர் சரியான பதில்களை வழங்காமலும் இருக்கலாம். முகவரின் பயனர் கேள்விகளை புரிந்து பதிலளிக்கும் திறனை பரிசோதிக்க இது நோக்கம்.

    ![Agent Playground](../../../translated_images/ta/agent-playground.dc146586de715010.webp)

3. முகவரை பரிசோதிக்கும் பிறகு, அதன் திறன்களை மேம்படுத்த மேலதிக நோக்கங்கள், பயிற்சி தரவு, மற்றும் நடவடிக்கைகள் சேர்க்கலாம்.

## வளங்களைச் சுத்தம் செய்யவும்

முகவரை பரிசோதனை முடிந்ததும், கூடுதல் செலவுகளை தவிர்க்க அதை நீக்கலாம்.
1. [Azure போர்டல்](https://portal.azure.com) திறந்து, இந்த பயிற்சியில் பயன்படுத்தப்பட்ட ஹப் வளங்களின் குழு உள்ளடக்கத்தைப் பாருங்கள்.
2. கருவிப்பட்டியில், **Delete resource group** ஐ தேர்ந்தெடுக்கவும்.
3. வள குழுவின் பெயரை உள்ளிட்டு, அதைப் நீக்க விரும்புகிறீர்கள் என்பதை உறுதி செய்யவும்.

## வளங்கள்

- [Microsoft Foundry ஆவணங்கள்](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry போர்டல்](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry உடன் துவங்குதல்](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure இல் AI முகவரின் அடிப்படைகள்](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->