# Microsoft Foundry ఏజెంట్ సర్వీస్ అభివృద్ధి

ఈ వ్యాయామంలో, మీరు [Microsoft Foundry పోర్టల్](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)లో Microsoft Foundry ఏజెంట్ సర్వీస్ టూల్స్ ఉపయోగించి Flight Booking కోసం ఒక ఏజెంట్‌ను సృష్టిస్తారు. ఈ ఏజెంట్ వినియోగదారులతో ఇంటరాక్ట్ చేసి విమానాల గురించి సమాచారం అందించగలుగుతుంది.

## ముందస్తు అవసరాలు

ఈ వ్యాయామాన్ని పూర్తి చేయడానికి, మీ వద్ద ఈ క్రింది వాటి అవసరం:
1. యాక్టివ్ సబ్‌స్క్రిప్షన్ కలిగిన Azure ఖాతా. [ఉచితంగా ఖాతా సృష్టించండి](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Microsoft Foundry హబ్ సృష్టించడానికి అనుమతులు లేదా మీ కోసం ఒకటి సృష్టించబడినది కావాలి.
    - మీ పాత్ర Contributor లేదా Owner అయితే, మీరు ఈ ట్యూటోరియల్‌లో ఉన్న దశలను అనుసరించవచ్చు.

## Microsoft Foundry హబ్ సృష్టించాలి

> **గమనిక:** Microsoft Foundry ని మునుపటి పేరుగా Azure AI స్టూడియోగా పిలిచేవారు.

1. Microsoft Foundry హబ్ సృష్టించడానికి ఈ [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) బ్లాగ్ పోస్ట్ గైడ్లైన్స్ ను అనుసరించండి.
2. మీ ప్రాజెక్ట్ సృష్టించబడిన తర్వాత, ప్రదర్శించబడే సూచనలను మూసివేసి Microsoft Foundry పోర్టల్‌లో ప్రాజెక్ట్ పేజీని పరిశీలించండి, ఇది క్రింద చూపిన చిత్రానికి సాదృశ్యం వుంటుంది:

    ![Microsoft Foundry Project](../../../translated_images/te/azure-ai-foundry.88d0c35298348c2f.webp)

## ఒక మోడల్‌ని డిప్లాయ్ చేయండి

1. మీ ప్రాజెక్ట్ కోసం ఎడమ వైపు ఉన్న పేజీలో, **My assets** విభాగంలో, **Models + endpoints** పేజీని ఎంచుకోండి.
2. **Models + endpoints** పేజీలో, **Model deployments** ట్యాబ్‌లో, **+ Deploy model** మెనూ లో, **Deploy base model** ఎంచుకోండి.
3. జాబితాలో `gpt-5-mini` మోడల్ కోసం శోధించండి, దాన్ని ఎంచుకుని ధ్రువీకరించండి.

    > **గమనిక**: TPM తగ్గించడం ద్వారా మీరు ఉపయోగిస్తున్న సబ్‌స్క్రిప్షన్‌లో లభ్యమయ్యే క్వోటాను ఎక్కువగా ఉపయోగించకుండా ఉండవచ్చు.

    ![Model Deployed](../../../translated_images/te/model-deployment.3749c53fb81e18fd.webp)

## ఒక ఏజెంట్ సృష్టించండి

ఇప్పుడు మీరు మోడల్‌ను డిప్లాయ్ చేసుకున్నట్లు, మీరు ఒక ఏజెంట్ సృష్టించవచ్చు. ఏజెంట్ అనేది వినియోగదారులతో మిమ్మల్ని మాట్లాడుకోవడానికి ఉపయోగించే సంభాషణాత్మక AI మోడల్.

1. మీ ప్రాజెక్ట్ ఎడమ వైపు పేజీలో, **Build & Customize** విభాగంలో, **Agents** పేజీని ఎంచుకోండి.
2. కొత్త ఏజెంట్ సృష్టించడానికి **+ Create agent** క్లిక్ చేయండి. **Agent Setup** డైలాగ్ బాక్స్ కింద:
    - ఏజెంట్ కోసం పేరును నమోదు చేయండి, ఉదాహరణకు `FlightAgent`.
    - మీరు మునుపుగా సృష్టించిన `gpt-5-mini` మోడల్ డిప్లాయ్‌మెంట్ ఎంచుకున్నదిగా నిర్ధారించండి
    - ఏజెంట్ అనుసరించేటట్లు **Instructions** ను మీ ప్రాంప్ట్ ప్రకారం సెట్ చేయండి. ఇక్కడ ఒక ఉదాహరణ ఉంది:
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
> మరిన్ని వివరాల కోసం, మీరు [ఈ రిపోజిటరీ](https://github.com/ShivamGoyal03/RoamMind)ని చూడవచ్చు.
    
> అదనంగా, మీరు ఏజెంట్ సామర్థ్యాలను మెరుగుపర్చడానికీ, వినియోగదారుల అభ్యర్థనల ఆధారంగా మరింత సమాచారం అందించడానికి మరియు ఆటోమేటెడ్ పనులను నిర్వహించడానికి **Knowledge Base** మరియు **Actions** జోడించవచ్చు. ఈ వ్యాయామం కోసం ఈ దశలను మీరు దాటవేయవచ్చు.
    
![Agent Setup](../../../translated_images/te/agent-setup.9bbb8755bf5df672.webp)

3. కొత్త మల్టీ-AI ఏజెంట్ సృష్టించడానికి **New Agent** క్లిక్ చేయండి. నవ్వ-created ఏజెంట్ Agents పేజీలో ప్రదర్శించబడుతుంది.


## ఏజెంట్ ని పరీక్షించండి

ఏజెంట్ సృష్టించిన తరువాత, మీరు దాన్ని పరీక్షించి మైక్రోసాఫ్ట్ Foundry పోర్టల్ ప్లేగ్రౌండ్‌లో వినియోగదారుల ప్రశ్నలకు అది ఎలా స్పందిస్తుందో చూడవచ్చు.

1. మీ ఏజెంట్ **Setup** పేయ్లో పై భాగంలో **Try in playground** ఎంచుకోండి.
2. **Playground** పేయ్లోలో, చాట్ విండోలో ప్రశ్నలు టైప్ చేసి ఏజెంట్‌తో ఇంటరాక్ట్ చేయవచ్చు. ఉదాహరణకు, ఏజెంట్ను 28వ తేదీన Seattle నుండి New York కు విమానాలు శోధించాలని అడగవచ్చు.

    > **గమనిక:** ఈ వ్యాయామంలో ప్రత్యక్ష సమయ డేటా ఉపయోగించకపోవడంతో ఏజెంట్ ఖచ్చితమైన స్పందనలు ఇవ్వకపోవచ్చు. ఇంతటితో ఏజెంట్ వినియోగదారుల ప్రశ్నలను అర్థం చేసుకుని అందించిన సూచనల ప్రకారం ప్రత్యామ్నాయాలు ఇచ్చే సామర్థ్యాన్ని పరీక్షించడం లక్ష్యము.

    ![Agent Playground](../../../translated_images/te/agent-playground.dc146586de715010.webp)

3. ఏజెంట్‌ను పరీక్షించిన తర్వాత, దాని సామర్థ్యాలు మెరుగుపర్చడానికి మరిన్ని ఉద్దేశ్యాలు, శిక్షణ డేటా మరియు చర్యలు జోడించి దాన్ని కస్టమైజ్ చేయవచ్చు.

## వనరుల్ని క్లియర్ చేయండి

ఏజెంట్ పరీక్ష పూర్తి చేసిన తర్వాత అదనపు ఖర్చులు రావడంకాకుండా దాన్ని తొలగించండి.
1. [Azure పోర్టల్](https://portal.azure.com)ని ఓపెన్ చేసి మీరు ఈ వ్యాయామంలో ఉపయోగించిన హబ్ వనరులని డిప్లాయ్ చేసిన రిసోర్స్ గ్రూప్ కంటెంట్‌ని చూడండి.
2. టూల్‌బార్‌లో **Delete resource group** ఎంచుకోండి.
3. రిసోర్స్ గ్రూప్ పేరు నమోదు చేసి దాన్ని తొలగించాలని నిర్ధారించండి.

## వనరులు

- [Microsoft Foundry డాక్యూమెంటేషన్](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry పోర్టల్](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry తో శుభారంభం](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure మీద AI ఏజెంట్ల మౌలికాలు](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->