# Azure AI ఏజెంట్ సర్వీస్ అభివృద్ధి

ఈ వ్యాయామంలో, మీరు [Microsoft Foundry పోర్టల్](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)లో Azure AI ఏజెంట్ సర్వీస్ టూల్స్ ఉపయోగించి ఫ్లైట్ బుకింగ్ కోసం ఒక ఏజెంట్‌ను సృష్టిస్తారు. ఏజెంట్ వినియోగదారులతో అనుసంధానం చేసుకొని ఫ్లైట్ల గురించి సమాచారం అందిస్తుంది.

## ముందస్తు అవసరాలు

ఈ వ్యాయామాన్ని పూర్తి చేయడానికి, మీరు ఈ క్రింది దాని అవసరం:
1. సక్రియమైన సభ్యత్వంతో కూడిన Azure ఖాతా. [ఉచితంగా ఖాతాను సృష్టించండి](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Microsoft Foundry హబ్‌ను సృష్టించే అనుమతులు లేదా మీ కోసం ఒకటి సృష్టించవలసి ఉంటుంది.
    - మీ పాత్ర Contributor లేదా Owner అయితే, మీరు ఈ ట్యుటోరియల్‌లోని దశలను అనుసరించవచ్చు.

## Microsoft Foundry హబ్ సృష్టించండి

> **గమనిక:** Microsoft Foundry పూర్వం Azure AI Studio గా పిలువబడేది.

1. Microsoft Foundry హబ్ సృష్టించేందుకు [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) బ్లాగ్ పోస్ట్ నుండి ఈ మార్గదర్శకాలను అనుసరించండి.
2. మీ ప్రాజెక్ట్ సృష్టించబడిన తర్వాత, చూపబడిన టిప్స్ ను మూసివేస్తూ Microsoft Foundry పోర్టల్ లో ప్రాజెక్ట్ పేజీని సమీక్షించండి, ఇది ఈ క్రింది చిత్రం లాగా కనిపించాలి:

    ![Microsoft Foundry Project](../../../translated_images/te/azure-ai-foundry.88d0c35298348c2f.webp)

## ఒక మోడల్‌ను అమలు చేయండి

1. మీ ప్రాజెక్ట్ కోసం ఎడమ పానెల్లో, **My assets** విభాగంలో **Models + endpoints** పేజీని ఎంచుకోండి.
2. **Models + endpoints** పేజీలో, **Model deployments** టాబ్‌లో, **+ Deploy model** మెనూ నుండి **Deploy base model** ను ఎంచుకోండి.
3. జాబితాలో `gpt-4o-mini` మోడల్‌ను శోధించి, దాన్ని ఎంచుకుని ధృవీకరించండి.

    > **గమనిక**: TPM ని తగ్గించడం సభ్యత్వం లో ఉన్న క్వాటాను ఎక్కువగా ఉపయోగించకుండా ఉంచుతుంది.

    ![Model Deployed](../../../translated_images/te/model-deployment.3749c53fb81e18fd.webp)

## ఏజెంట్ సృష్టించండి

ఇప్పుడు మీరు మోడల్‌ను అమలు చేశారు కనుక, ఏజెంట్‌ను సృష్టించవచ్చు. ఏజెంట్ అనేది వినియోగదారులతో సంభాషించగల కాన్వర్సేషనల్ AI మోడల్.

1. మీ ప్రాజెక్ట్ కోసం ఎడమ పానెల్లో, **Build & Customize** విభాగంలో **Agents** పేజీని ఎంచుకోండి.
2. **+ Create agent** క్లిక్ చేసి కొత్త ఏజెంట్‌ను సృష్టించండి. **Agent Setup** డైలాగ్ బాక్స్‌లో:
    - ఏజెంట్‌కి `FlightAgent` వంటి పేరు ఇవ్వండి.
    - మీరు раవి చేసిన `gpt-4o-mini` మోడల్ డిప్లాయ్మెంట్ ఎంచుకోబడిందని నిర్ధారించండి.
    - ఏజెంట్ అనుసరించాల్సిన సూచనలను **Instructions** లో సెట్ చేయండి. ఇక్కడ ఒక ఉదాహరణ ఉంది:
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
> ప్రామాణిక ప్రాంప్ట్ కోసం, మీరు [ఈ రిపోజిటరీ](https://github.com/ShivamGoyal03/RoamMind) ని చూడవచ్చు.

> అదనంగా, మీరు **Knowledge Base** మరియు **Actions** జోడించవచ్చు, ఇది ఏజెంట్ సామర్థ్యాలను పెంపొందించి మరింత సమాచారం అందించగలదు మరియు వినియోగదారుల అభ్యర్థనల ఆధారంగా ఆటోమేటెడ్ పనులు నిర్వహించగలదు. ఈ వ్యాయామం కొరకు, మీరు ఈ దశలను దాటిచెప్పవచ్చు.

![Agent Setup](../../../translated_images/te/agent-setup.9bbb8755bf5df672.webp)

3. కొత్త మల్టీ-AI ఏజెంట్ సృష్టించడానికి, సింప్లీ **New Agent** క్లిక్ చేయండి. కొత్తగా సృష్టించబడిన ఏజెంట్ Agents పేజీలో ప్రదర్శింపబడుతుంది.

## ఏజెంట్‌ను పరీక్షించండి

ఏజెంట్ సృష్టించిన తర్వాత, మైక్రోసాఫ్ట్ ఫౌండ్రీ పోర్టల్ ప్లేగ్రౌండ్‌లో వినియోగదారుల ప్రశ్నలకు దాని స్పందనను పరీక్షించవచ్చు.

1. మీ ఏజెంట్ కోసం **Setup** పానెల్లో, పైభాగంలో **Try in playground** ఎంచుకోండి.
2. **Playground** పానెల్లో, మీరు చాట్ విండోలో ప్రశ్నలు టైప్ చేసి ఏజెంట్‌తో సంభాషించవచ్చు. ఉదాహరణకు, ఏజెంట్‌ను 28వ తేదీ సియాటిల్ నుండి న్యూయార్క్‌కు ఫ్లైట్ల కోసం వెతకమంటూ అడగవచ్చు.

    > **గమనిక**: ఈ వ్యాయామంలో ఏమాత్రం రియల్-టైమ్ డేటా ఉపయోగించబడడం లేదు కనుక ఏజెంట్ నిర్దిష్ట సమాధానాలు ఇవ్వకపోవచ్చు. పాఠ్యమును అర్థం చేసుకొని వినియోగదారుల ప్రశ్నలకు స్పందించే సామర్థ్యాన్ని పరీక్షించడం ప్రధాన ఉద్దేశ్యం.

    ![Agent Playground](../../../translated_images/te/agent-playground.dc146586de715010.webp)

3. ఏజెంట్‌ను పరీక్షించిన తర్వాత, దాని సామర్థ్యాలను పెంచేందుకు మరిన్ని ఉద్దేశాలు, శిక్షణ డేటా, మరియు చర్యలను జోడించి దాన్ని మరింత అనుకూలీకరించవచ్చు.

## వనరుల్ని శుభ్రం చేయండి

ఏజెంట్ పరీక్షించిన తర్వాత, అదనపు ఖర్చులు తప్పించుకునేందుకు దాన్ని తొలగించవచ్చు.
1. [Azure పోర్టల్](https://portal.azure.com)ని ఓపెన్ చేసి ఈ వ్యాయామంలో ఉపయోగించిన హబ్ వనరులున్న రిసోర్స్ గ్రూప్ కంటెంట్ని వీక్షించండి.
2. టూల్‌బార్‌లో **Delete resource group** ఎంచుకోండి.
3. రిసోర్స్ గ్రూప్ పేరు ని టైప్ చేసి, దాన్ని తొలగించాలనేది ధృవీకరించండి.

## వనరులు

- [Microsoft Foundry డాక్యుమెంటేషన్](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry పోర్టల్](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Studio తో ప్రారంభించండి](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure పై AI ఏజెంట్ల మౌలిక సారాంశం](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI డిస్కార్డ్](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**వితంతువు**:
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించాము. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, స్వయంచాలక అనువాదాలలో లోపాలు లేదా తప్పిదాలు ఉండవచ్చు. ఆ పత్రం యొక్క మూల భాషలో ఉన్న దస్తావేజే అధికారికమైన మూలం గా పరిగణించబడాలి. ముఖ్యమైన సమాచారం కోసం, నిపుణుల చేతి అనువాదం చేయించడం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడుక ద్వారా కలిగే ఏవైనా తప్పుదోషాలు లేదా అభిప్రాయ భేదాలకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->