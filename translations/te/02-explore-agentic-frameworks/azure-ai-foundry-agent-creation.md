# Microsoft Foundry ఏజెంట్ సేవా అభివృద్ధి

ఈ వ్యాయామంలో, మీరు [Microsoft Foundry పోర్టల్](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)లో Microsoft Foundry ఏజెంట్ సేవా సాధనాలను ఉపయోగించి ఫ్లైట్ బుక్ చేయడానికి ఒక ఏజెంట్‌ను సృష్టిస్తారు. ఆ ఏజెంట్ వినియోగదారులతో సంబంధించి మాట్లాడగలదు మరియు విమానాల గురించి సమాచారం అందించగలదు.

## ప్రస్తుతపరచుకోవలసినవే

ఈ వ్యాయామాన్ని పూర్తి చేయడానికి, మీకు క్రింది వస్తువులు అవసరం:
1. సక్రియ సభ్యతతో కూడిన ఒక ఆజ్యూర్ ఖాతా. [ఉచితంగా ఖాతాను సృష్టించండి](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Microsoft Foundry హబ్ సృష్టించడానికి అనుమతులు లేదా మీ కోసం ఒకటి సృష్టించబడాలి.
    - మీ పాత్ర కంస్ట్రిబ్యూటర్ లేదా ఓనర్ అయితే, మీరు ఈ పాఠంలో ఉన్న దశలను అనుసరించవచ్చు.

## Microsoft Foundry హబ్ సృష్టించండి

> **గమనిక:** మైక్రోసాఫ్ట్ Foundry ముందు Azure AI స్టూడియో అని పిలువబడింది.

1. Microsoft Foundry బ్లాగ్ పోస్ట్ నుండి ఈ మార్గదర్శకాలను అనుసరించి Microsoft Foundry హబ్ సృష్టించండి ([Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)).
2. మీ ప్రాజెక్టు సృష్టించబడిన తర్వాత, చూపించబడే ఏదైనా సూచనలను మూసివేసి Microsoft Foundry పోర్టల్‌లోని ప్రాజెక్టు పేజీని సమీక్షించండి, అది క్రింద ఇచ్చిన చిత్రంలోనిట్లు ఉండాలి:

    ![Microsoft Foundry Project](../../../translated_images/te/azure-ai-foundry.88d0c35298348c2f.webp)

## మోడల్‌ను ప్రదర్శించండి

1. మీ ప్రాజెక్టు కోసం ఎడమవైపు ఉన్న ప్యాన్‌లో, **నా ఆస్తులు** విభాగంలో, **మోడల్స్ + ఎండ్‌పాయింట్స్** పేజీని ఎంచుకోండి.
2. **మోడల్స్ + ఎండ్‌పాయింట్స్** పేజీలో, **మోడల్ డిప్లాయ్‌మెంట్‌లు** టాబ్‌లో, **+ మోడల్ డిప్లాయ్ చేయండి** మెనూలో, **ప్రాథమిక మోడల్ డిప్లాయ్ చేయండి**ని ఎంచుకోండి.
3. జాబితాలో `gpt-4.1-mini` మోడల్‌ను వెతకండి, ఆ తరువాత దాన్ని ఎంచుకుని నిర్ధారించండి.

    > **గమనిక**: TPM ను తగ్గించడం మీ సబ్స్క్రిప్షన్‌లో అందుబాటులో ఉన్న క్వోటాను అధికంగా ఉపయోగించడం నుండి నివారిస్తుంది.

    ![Model Deployed](../../../translated_images/te/model-deployment.3749c53fb81e18fd.webp)

## ఏజెంట్ సృష్టించండి

ఇప్పుడు మీరు మోడల్‌ను ప్రదర్శించి ఉన్నారు, మీరు ఒక ఏజెంట్‌ను సృష్టించవచ్చు. ఏజెంట్ అనేది వినియోగదారులతో సంభాషించేందుకు ఉపయోగించే సంభాషణ AI మోడల్.

1. మీ ప్రాజెక్టు కోసం ఎడమవైపు ఉన్న ప్యాన్‌లో, **అడగండి & అనుకూలీకరించండి** విభాగంలో, **ఏజెంట్లు** పేజీని ఎంచుకోండి.
2. కొత్త ఏజెంట్ సృష్టించేందుకు **+ ఏజెంట్ సృష్టించండి** క్లిక్ చేయండి. **ఏజెంట్ సెటప్** డైలాగ్ బాక్స్ క్రింద:
    - ఏజెంట్‌కు పేరు ఇవ్వండి, ఉదా: `FlightAgent`.
    - మీ మునుపు సృష్టించిన `gpt-4.1-mini` మోడల్ డిప్లాయ్‌మెంట్ ఎంచుకోబడిందని నిర్ధారించండి
    - ఏజెంట్ అనుసరించవలసిన సూచనలు **సూచనలు**లో సెట్ చేయండి. ఉదాహరణ ఇక్కడ ఉంది:
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
> మరిన్ని వివరాలతో కూడిన ప్రాంప్ట్ కోసం, మీరు [ఈ రిపాజిటరీ](https://github.com/ShivamGoyal03/RoamMind)ని పరిశీలించవచ్చు.
    
> అదనంగా, మీరు ఏజెంట్ యొక్క సామర్థ్యాలను పెంచేందుకు **జ్ఞాన నిలువు** మరియు **చర్యలు**ను జోడించవచ్చు, వినియోగదారుల అభ్యర్థనల ఆధారంగా మరింత సమాచారం అందించటం మరియు ఆటోమేటెడ్ పనులు చేయడం కోసం. ఈ వ్యాయామంలో, మీరు ఈ దశలను దాటవేయవచ్చు.
    
![Agent Setup](../../../translated_images/te/agent-setup.9bbb8755bf5df672.webp)

3. కొత్త బహిరంగ AI ఏజెంట్ సృష్టించడానికి, సాదాగా **New Agent**పై క్లిక్ చేయండి. కొత్తగా సృష్టించిన ఏజెంట్ తర్వాత ఏజెంట్ల పేజీలో ప్రదర్శించబడుతుంది.


## ఏజెంట్‌ని పరీక్షించండి

ఏజెంట్ సృష్టించిన తర్వాత, Microsoft Foundry పోర్టల్ ప్లేగ్రౌండ్‌లో అది వినియోగదారుల ప్రశ్నలకు ఎట్లా స్పందిస్తుంది అనేది మీరు పరీక్షించవచ్చు.

1. మీ ఏజెంట్ కోసం **Setup** ప్యాన్ పైభాగంలో, **Playground లో ప్రయత్నించండి**ని ఎంచుకోండి.
2. **Playground** ప్యాన్‌లో మీరు చాట్ విండోలో ప్రశ్నలు టైపు చేయడం ద్వారా ఏజెంట్‌తో సంభాషించవచ్చు. ఉదాహరణకు, మీరు ఏజెంట్‌ను 28న సియాటెల్ నుండి న్యూయార్క్ విమానాలు వెతకమని అడగవచ్చు.

    > **గమనిక**: ఈ వ్యాయామంలో ఏజెంట్ నిజ సమయ డేటాను ఉపయోగించడం లేదు కనుక సహజసిద్ధమైన సమాధానాలు అందుకోవకపోవచ్చు. ఈ వ్యాయామం ఉద్దేశం సూచనల ఆధారంగా వినియోగదారుల ప్రశ్నలను అర్థం చేసుకుని స్పందించే ఏజెంట్ సామర్థ్యాన్ని పరీక్షించడం.

    ![Agent Playground](../../../translated_images/te/agent-playground.dc146586de715010.webp)

3. ఏజెంట్‌ను పరీక్షించిన తర్వాత, దాని సామర్థ్యాలను పెంచేందుకు మరిన్ని అభిలాషలు, శిక్షణ డేటా, మరియు చర్యలను జోడించి మరింత అనుకూలీకరించవచ్చు.

## వనరులను శుభ్రపరచండి

ఏజెంట్‌ను పరీక్షించటం ముగించాక, అదనపు ఖర్చులు తగలకుండా దాన్ని తీయొచ్చు.
1. [Azure పోర్టల్](https://portal.azure.com) ఓపెన్ చేసి మీరు ఈ వ్యాయామంలో ఉపయోగించిన హబ్ వనరులు డిప్లాయ్ చేసిన రిసోర్స్ గ్రూప్ కంటెంట్ను వీక్షించండి.
2. టూల్‌బార్‌లో, **రిసోర్స్ గ్రూప్ తొలగించండి**ను ఎంచుకోండి.
3. రిసోర్స్ గ్రూప్ పేరు నమోదు చేసి దాన్ని తొలగించాలనుకుంటున్నట్టు నిర్ధారించండి.

## వనరులు

- [Microsoft Foundry డాక్యుమెంటేషన్](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry పోర్టల్](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry తో ప్రారంభించండి](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azureపై AI ఏజెంట్ల ప్రాథమికాలు](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->