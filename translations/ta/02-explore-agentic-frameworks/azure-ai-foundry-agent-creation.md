# Microsoft Foundry முகவர் சேவை மேம்பாடு

இந்த பயிற்சியில், [Microsoft Foundry portal](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) இல் Microsoft Foundry முகவர் சேவை உபகரணங்களை பயன்படுத்தி, விமானத் தாங்கல் முகவரை உருவாக்குவீர்கள். அந்த முகவர் பயனர்களுடன் தொடர்பு கொண்டு விமானங்களுக்கான தகவலை வழங்கும்.

## தேவையான முன்னிலை

இந்த பயிற்சியை முடிக்க, நீங்கள் கீழ்கண்டவை தேவை:
1. செயல்பாட்டில் இருக்கும் சந்தா கொண்ட Azure கணக்கு. [இலவசமாக ஒரு கணக்கை உருவாக்கவும்](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Microsoft Foundry ஹப் உருவாக்க அனுமதிகள் அல்லது உங்களுக்கு ஒருவரை உருவாக்கி தரப்பட வேண்டும்.
    - உங்கள் பங்கு Contributor அல்லது Owner என்றால், இந்த பயிற்சியின் படிகள் பின்பற்றலாம்.

## Microsoft Foundry ஹப் உருவாக்கவும்

> **குறிப்பு:** Microsoft Foundry முந்தைய பெயர் Azure AI Studio ஆகும்.

1. Microsoft Foundry ஹப் உருவாக்குவதற்கான [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) வலைப்பதிவிலுள்ள வழிமுறைகளை பின்பற்றவும்.
2. உங்கள் திட்டம் உருவாக்கப்பட்டவுடன், எத்வும் காண்பிக்கப்பட்ட ஆலோசனைகளை மூடி, Microsoft Foundry போர்டலில் திட்டப் பக்கத்தை ஆய்வு செய்யவும். இதோ அதற்கான ஒரு படம்தான் கீழே உள்ளது:

    ![Microsoft Foundry Project](../../../translated_images/ta/azure-ai-foundry.88d0c35298348c2f.webp)

## ஒரு மாதிரியை இயக்கவும்

1. உங்கள் திட்ட அடுத்த பக்கத்தில், **My assets** பகுதியில், **Models + endpoints** பக்கத்தைக் தேர்ந்தெடுக்கவும்.
2. **Models + endpoints** பக்கத்தில், **Model deployments** தாவலைத் திறந்து, **+ Deploy model** மெனுவில், **Deploy base model** தேர்ந்தெடுக்கவும்.
3. பட்டியலில் `gpt-5-mini` மாதிரியை தேடி, அதை தேர்ந்தெடுத்து உறுதிப்படுத்தவும்.

    > **குறிப்பு**: TPM ஐ குறைப்பது நீங்கள் பயன்படுத்தும் சந்தாவில் உள்ள அனுமதி அளவை அதிகமாக பயன்படுத்துவதைக் கட்டுப்படுத்த உதவும்.

    ![Model Deployed](../../../translated_images/ta/model-deployment.3749c53fb81e18fd.webp)

## ஒரு முகவரை உருவாக்கவும்

இப்போது நீங்கள் ஒரு மாதிரியை இயக்கியுள்ளீர்கள், ஒரு முகவரை உருவாக்கலாம். முகவர் என்பது பயனர்களுடன் தொடர்பு கொள்ளும் உரையாடல் செயற்கை நுண்ணறிவு மாதிரி ஆகும்.

1. திட்ட அடுத்த பக்கத்தில், **Build & Customize** பகுதியில், **Agents** பக்கத்தைத் தேர்ந்தெடுக்கவும்.
2. புதிய முகவரை உருவாக்க **+ Create agent** என்பதைக் கிளிக் செய்யவும். **Agent Setup** கலப்பு பெட்டியில்:
    - முகவருக்கு பெயர் இடவும், உதாரணத்திற்கு `FlightAgent`.
    - நீங்கள் முன்பு உருவாக்கிய `gpt-5-mini` மாதிரி பயன்படுத்தப்படுவதை உறுதிசெய்யவும்
    - முகவர் பின்பற்ற வேண்டிய அறிவுறுத்தல்களை **Instructions** என்ற இடத்தில் அமைக்கவும். கீழே ஒரு உதাহாரணம் உள்ளது:
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
> விரிவான அறிவுறுத்தலுக்காக [இந்த தளம்](https://github.com/ShivamGoyal03/RoamMind) யைப் பார்க்கலாம்.
    
> மேலும, முகவரின் திறனை மேம்படுத்த **Knowledge Base** மற்றும் **Actions** ஐச் சேர்க்கலாம், பயனர் கோரிக்கைகள் அடிப்படையில் மேலதிக தகவல் வழங்க மற்றும் தானாக வேலை செய்ய. இந்த பயிற்சிக்கு, இச்செயல்களை தவிர்க்கலாம்.
    
![Agent Setup](../../../translated_images/ta/agent-setup.9bbb8755bf5df672.webp)

3. புதிய பல-எய்ஐ முகவரை உருவாக்க **New Agent** ஐ கிளிக் செய்யவும். உருவாக்கப்பட்ட புதிய முகவர் Agents பக்கத்தில் காணப்படும்.


## முகவரை சோதிக்கவும்

முகவரை உருவாக்கிய பிறகு, Microsoft Foundry போர்டல் விளையாட்டு பகுதியில் பயனர் கோரிக்கைகளுக்கு முகவர் எப்படி பதிலளிக்கிறது என்பதை சோதிக்கலாம்.

1. உங்கள் முகவருக்கான **Setup** பகுதியின் மேல், **Try in playground** ஐத் தேர்ந்தெடுக்கவும்.
2. **Playground** பகுதியில், பேச்சு வினாடியில் கேள்விகள் எழுதி முகவருடன் தொடர்பு கொள்ளலாம். உதாரணமாக, 28 ஆம் தேதி சியாட்டிலிருந்து நியூயார்க் விமானங்களை தேடுமாறு கேட்கலாம்.

    > **குறிப்பு**: முகவர் சரியான பதில்களை வழங்காமல் இருக்கலாம், ஏனெனில் இந்த பயிற்சியில் நேரடி தரவு பயன்படுத்தப்படவில்லை. முகவரின் பயனரின் கோரிக்கைகளை புரிந்து பதிலளிக்கும் திறனை சோதிப்பது இதன் நோக்கம்.

    ![Agent Playground](../../../translated_images/ta/agent-playground.dc146586de715010.webp)

3. முகவரை சோதித்த பிறகு, அதை அதிக நன்மைகள் பெற புதிய நோக்கங்களையும் பயிற்சி தரவும் மற்றும் செயல்களையும் சேர்க்க மறக்காதீர்கள்.

## வளங்களை சுத்தம் செய்யவும்

முகவரை சோதனை முடிந்தவுடன், கூடுதல் செலவுகளைக் குறைக்க அதை நீக்கலாம்.
1. [Azure portal](https://portal.azure.com) திறந்து, இந்த பயிற்சியில் பயன்படுத்திய ஹப் வளங்களைக் கொண்ட வளக் குழுமத்தின் உள்ளடக்கங்களைப் பார்க்கவும்.
2. கருவிப்பட்டையில், **Delete resource group** என்பதைத் தேர்ந்தெடுக்கவும்.
3. வளக் குழுமத்தின் பெயரை உள்ளிட்டு, அதை நீக்க விரும்புவதை உறுதிப்படுத்தவும்.

## வளங்கள்

- [Microsoft Foundry விண்ணப்பக் குறிப்புகள்](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry போர்டல்](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry தொடக்கம்](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure இல் AI முகவர்கள் அடிப்படைகள்](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->