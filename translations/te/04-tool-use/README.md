[![ఎలా మంచి AI ఏజెన్ట్లను డిజైన్ చేయాలి](../../../translated_images/te/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ఈ పాఠం వీడియోని చూడటానికి పై చిత్రాన్ని క్లిక్ చేయండి)_

# టూల్ వినియోగ డిజైన్ ప్యాటర్న్

టూల్స్ ఆసక్తికరమైనవి ఎందుకంటే అవి AI ఏజెంట్లకు విస్తృత శ్రేణి సామర్థ్యాలను కలిగిస్తాయి. ఏజెంట్ పరిమిత చర్యల సెట్‌ను నిర్వహించడమునుపటి పరిస్థితి కాకుండా, ఒక టూల్‌ను చేర్పించడం ద్వారా, ఏజెంట్ ఇప్పుడు విస్తృత శ్రేణి చర్యలను నిర్వహించగలను. ఈ అధ్యాయంలో, మేము టూల్ వినియోగ డిజైన్ ప్యాటర్న్‌ను చూసుకుందాము, ఇది AI ఏజెంట్లు నిర్దిష్ట టూల్స్ ఉపయోగించి తమ లక్ష్యాలను సాధించడానికి ఎలా ఉపయోగించుకోవచ్చో వివరించును.

## పరిచయం

ఈ పాఠంలో, మేము క్రింది ప్రశ్నలకు సమాధానం ఇవ్వాలని చూస్తున్నాము:

- టూల్ వినియోగ డిజైన్ ప్యాటర్న్ ఏమిటి?
- ఇది ఎలాంటి ఉపయోగాలపై వర్తించవచ్చు?
- డిజైన్ ప్యాటర్న్ అమలు చేయడానికి ఏ అంశాలు/నిర్మాణ బ్లాకు లు అవసరం?
- విశ్వస్త AI ఏజెంట్లను నిర్మించేప్పుడు టూల్ వినియోగ డిజైన్ ప్యాటర్న్ ఉపయోగించేటప్పుడు ప్రత్యేక గమనికలు ఏవి?

## నేర్చుకోవాల్సిన లక్ష్యాలు

ఈ పాఠం పూర్తి చేసిన తర్వాత, మీరు ఈ క్రింది విషయాలను చేయగలుగుతారు:

- టూల్ వినియోగ డిజైన్ ప్యాటర్న్ మరియు దాని ఉద్దేశాన్ని నిర్వచించండి.
- టూల్ వినియోగ డిజైన్ ప్యాటర్న్ వర్తించే ఉపయోగ సందర్భాలను గుర్తించండి.
- డిజైన్ ప్యాటర్న్ అమలు చేయడానికి అవసరమైన ముఖ్య అంశాలను అర్థం చేసుకోండి.
- ఈ డిజైన్ ప్యాటర్న్ ఉపయోగించే AI ఏజెంట్లలో విశ్వాసనీయత నిర్ధారించుకునే ఆలోచనలను గుర్తించండి.

## టూల్ వినియోగ డిజైన్ ప్యాటర్న్ అంటే ఏమిటి?

**టూల్ వినియోగ డిజైన్ ప్యాటర్న్** LLMలకు నిర్దిష్ట లక్ష్యాలను సాధించడానికి బయటి టూల్స్‌తో సంబంధం కలిగించే సామర్థ్యాన్ని ఇస్తుంది. టూల్స్ అనేవి ఏజెంట్ అమలు చేయగల కోడ్‌ లు. ఒక టూల్ సాధారణంగా కలక్యులేటర్ వంటి సులభమైన ఫంక్షన్ కావచ్చు లేదా స్టాక్ ధరల పలకడిని లేదా వాతావరణ సూచనలను పొందటానికి మూడవ పక్ష సేవలకు API కాల్ ఉండవచ్చు. AI ఏజెంట్ల సందర్భంలో, టూల్స్ మోడల్-సృష్టించిన ఫంక్షన్ కాల్స్ కి స్పందిస్తూ ఏజెంట్లు అమలు చేయడానికి రూపొందించబడ్డాయి.

## ఇది ఎలాంటి ఉపయోగాల పై వర్తించవచ్చు?

AI ఏజెంట్లు టూల్స్‌ను ఉపయోగించి సంక్లిష్ట పనులు పూర్తి చేయవచ్చు, సమాచారం సేకరించవచ్చు లేదా నిర్ణయాలు తీసుకోవచ్చు. టూల్ వినియోగ డిజైన్ ప్యాటర్న్ సాధారణంగా డైనమిక్ బాహ్య వ్యవస్థలతో పరస్పర చర్య అవసరమయ్యే పరిస్థితులలో ఉపయోగిస్తారు, ఉదాహరణకు డేటాబేసులు, వెబ్ సర్వీసులు లేదా కోడ్ ఇంటర్ప్రెటర్లు. ఈ సామర్థ్యం క్రింద ఉన్న అనేక ఉపయోగాల కోసం ఉపయోగపడుతుంది:

- **డైనమిక్ సమాచారం సేకరణ:** ఏజెంట్లు బయటి APIలు లేదా డేటాబేసులను కాల్ చేసి తాజా డేటాను పొందవచ్చు (ఉదా: డేటా విశ్లేషణ కోసం SQLite డేటాబేస్ క్యూరీ, స్టాక్ ధరలు లేదా వాతావరణ సమాచారం పొందడం).
- **కోడ్ అమలు మరియు అనువాదం:** ఏజెంట్లు గణిత సమస్యల ప解决, నివేదికల నిర్మాణం లేదా సిమ్యులేషన్లు చేయడానికి కోడ్ లేదా స్క్రిప్ట్స్ ను అమలు చేయగలరు.
- **వర్క్‌ఫ్లో ఆటోమేషన్:** పనుల షెడ్యూలర్స్, ఇమెయిల్స్ సేవలు లేదా డేటా పైప్లైన్లు వంటి టూల్స్ కలిపి పునరావృత లేదా బహుళ దశల వర్క్‌ఫ్లోలను ఆటోమేట్ చేయడం.
- **కస్టమర్ సపోర్ట్:** ఏజెంట్లు CRM వ్యవస్థలు, టికెట్ ప్లాట్‌ఫామ్‌లు లేదా జ్ఞాన ఆధారాలతో పరస్పరం చర్య చేసి వినియోగదారుల ప్రశ్నలకు సమాధానం చెయ్యటం.
- **కంటెంట్ సృష్టి మరియు ఎడిటింగ్:** వ్యాకరణ పరిశీలకాలు, పాఠ్య సంగ్రహ కళాకారులు లేదా కంటెంట్ భద్రతా మూల్యాంకకుల వంటి టూల్స్ ఉపయోగించి సమగ్రంగా సాహాయం చేయడం.

## టూల్ వినియోగ డిజైన్ ప్యాటర్న్ అమలుకు అవసరమైన అంశాలు/నిర్మాణ బ్లాక్స్ ఏమిటి?

ఈ నిర్మాణ బ్లాక్స్ AI ఏజెంట్లకు విస్తృత శ్రేణి పనులు చేయడానికి అనుమతిస్తాయి. టూల్ వినియోగ డిజైన్ ప్యాటర్న్ అమలుకు అవసరమైన ముఖ్య అంశాలను చూద్దాం:

- **ఫంక్షన్/టూల్ స్కీమాలు:** అందుబాటులో ఉన్న టూల్స్ యొక్క వివరమైన నిర్వచనాలు, ఫంక్షన్ పేరు, ఉద్దేశం, అవసరమైన పారామితులు మరియు అనుమానిత అవుట్‌పుట్స్. ఈ స్కీమాలు LLM కు ఏ టూల్స్ అందుబాటులో ఉన్నాయో మరియు సరైన అభ్యర్థనలు ఎలా నిర్మించాలో అర్థం చేసుకోవడానికి సహాయపడతాయి.

- **ఫంక్షన్ అమలు తర్కం:** యూజర్ ఉద్దేశం మరియు సంభాషణ సందర్భంపై ఆధారపడి టూల్స్ ఎప్పుడు, ఎలా పిలవాలో నియంత్రిస్తుంది. దీంట్లో ప్లానర్ మాడ్యూల్స్, రౌటింగ్ మెకానిజమ్స్ లేదా డైనమిక్ టూల్ వినియోగాన్ని నిర్ణయించే షరతు ప్రవాహాలు ఉండవచ్చు.

- **సందేశ నిర్వహణ వ్యవస్థ:** యూజర్ ఇన్‌పుట్లు, LLM స్పందనలు, టూల్ కాల్స్ మరియు టూల్ అవుట్పుట్స్ మధ్య సంభాషణ ప్రవాహాన్ని నిర్వహించే భాగాలు.

- **టూల్ ఇంటిగ్రేషన్ ఫ్రేమ్‌వర్క్:** ఏజెంట్‌ను సులభమైన ఫంక్షన్లు గానీ, క్లిష్టమైన బాహ్య సేవలు గానీ కలిసి ఉన్న విభిన్న టూల్స్ కు అనుసంధానం చేసే మౌలిక నిర్మాణం.

- **లోపాల నిర్వహణ & ధృవీకరణ:** టూల్ అమల్లో విఫలమయ్యే సందర్భాలను నిర్వహించే, పారామితుల ధృవీకరణ చేయడానికి, మరియు అప్రత్యాశిత ప్రతిస్పందనలను నిర్వహించే వ్యవస్థలు.

- **స్థితి నిర్వహణ:** సంభాషణ సందర్భం, ముందు టూల్ పరస్పర చర్యలను మరియు బహుళ-టర్న్ పరస్పర చర్యల్లో సాదుపాయం సాధించడానికి శాశ్వత డేటాను ట్రాక్ చేస్తుంది.

తర్వాత, ఫంక్షన్/టూల్ కాలింగ్‌ను మరింత వివరంగా చూద్దాం.
 
### ఫంక్షన్/టూల్ కాలింగ్

ఫంక్షన్ కాలింగ్ అనేది LLM లకు టూల్స్‌తో సంబంధం కలిగించే ముఖ్యమైన మార్గం. మీరు తరచుగా 'ఫంక్షన్' మరియు 'టూల్' అనే పదాలను పరస్పరం ఉపయోగిస్తారు ఎందుకంటే 'ఫంక్షన్లు' (పునర్వినియోగం చేయదగిన కోడ్ బ్లాక్స్) ఏజెంట్లు పనులు చేయడానికి ఉపయోగించే 'టూల్స్' అవుతాయి. ఫంక్షన్ కోడ్‌ను పిలవడం కోసం, LLM యూజర్ అభ్యర్థనను ఫంక్షన్ వివరణతో సరిపోల్చాలి. దీన్ని సాధించడానికి అందుబాటులో ఉన్న ఫంక్షన్ల వివరాలను కలిగిన స్కీమా LLM కు పంపబడుతుంది. LLM అవసరమైన పనికి సరిగిన ఫంక్షన్ ను ఎంచుకుని దాని పేరు మరియు ఆర్గ్యుమెంట్లు తిరిగి ఇస్తుంది. ఎంచుకున్న ఫంక్షన్ అమలవుతుంది, ఆ జవాబు LLM కు పంపబడుతుంది, ఇది ఆ సమాచారంతో యూజర్ అభ్యర్థనకు స్పందిస్తుంది.

డెవలపర్ లు ఏజెంట్ల కోసం ఫంక్షన్ కాలింగ్ అమలు చేయాలంటే:

1. ఫంక్షన్ కాలింగ్ ను మద్దతిచ్చే LLM మోడల్
2. ఫంక్షన్ వివరణలతో కూడిన స్కీమా
3. వివరణ చేయబడిన ప్రతి ఫంక్షన్ కు కోడ్

సిటీ లో ప్రస్తుత సమయాన్ని పొందడం ఉదాహరణగా తీసుకొని చూద్దాం:

1. **ఫంక్షన్ కాలింగ్ ను మద్దతిచ్చే LLM ను ప్రారంభించండి:**

    అన్ని మోడల్స్ ఫంక్షన్ కాలింగ్ మద్దతు ఇవ్వవు, కనుక మీరు ఉపయోగిస్తున్న LLM మద్దతు ఇచ్చేది కాదా అని తనిఖీ చేయడం ముఖ్యము. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ఫంక్షన్ కాలింగ్ మద్దతు ఇస్తుంది. మేము OpenAI క్లయింట్ ను Azure OpenAI **Responses API** మీద ప్రారంభించవచ్చు (స్థిరమైన `/openai/v1/` ఎండ్పాయింట్ — `api_version` అవసరం లేదు).

    ```python
    # Azure OpenAI (ప్రతిస్పందనలు API, v1 ఎండ్‌పాయింట్) కోసం OpenAI క్లయింట్‌ను ప్రారంభించండి
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **ఫంక్షన్ స్కీమా సృష్టించండి**:

    తర్వాత, ఫంక్షన్ పేరు, ఫంక్షన్ చేసే పనితో పాటు దాని పారామితుల పేర్లను, వివరణలతో కలిపిన JSON స్కీమాను నిర్వచిస్తాము.
    ఆ స్కీమాను өмнటి క్లయింట్ కు, అలాగే యూజర్ అభ్యర్థన (సాన్ ఫ్రాన్సిస్కోలో సమయం తెలుసుకోవడం) తో పంపుతాము. ముఖ్యమయినది ఏమిటంటే, **టూల్ కాల్** తిరిగి వస్తుంది, **ప్రశ్నకు తుది సమాధానం కాదు**. ముందుగానే చెప్పినట్లుగా, LLM పనికి ఎంచుకున్న ఫంక్షన్ పేరు మరియు ఆ ఫంక్షన్ కు పంపవలసిన ఆర్గ్యుమెంట్లు ఇస్తుంది.

    ```python
    # మోడల్ చదవడానికి ఫంక్షన్ వివరణ (ప్రతిస్పందనల API ఫ్లాట్ టూల్ ఫార్మాట్)
    tools = [
        {
            "type": "function",
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    ]
    ```
   
    ```python
  
    # ప్రారంభ వినియోగదారు సందేశం
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # మొదటి API పిలుపు: మోడల్ ను ఫంక్షన్ ఉపయోగించమని అడుగు
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API టూల్ పిలుపులను function_call అంశాలుగా response.output లో తిరిగి ఇస్తుంది.
    # తదుపరి మలుపులో మోడల్ కు పూర్తిగా సन्दर्भం ఉండేందుకు వాటిని సంభాషణలో చేర్చండి.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **పనిని చేయడానికి అవసరమైన ఫంక్షన్ కోడ్:**

     ఇప్పుడు LLM ఎంచుకొన్న ఫంక్షన్ అమలు కావాల్సిన దానికి, ఆ పని చేయడానికి కోడ్ అమలు చేసి రాయాలి.
     ప్రస్తుత సమయాన్ని పొందడానికి Python లో కోడ్ రాయవచ్చు. అలాగే, response_message నుండి ఫంక్షన్ పేరు మరియు ఆర్గ్యుమెంట్లు బయటపెట్టడం కోడును కూడా రాశే అవసరం.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
    # ఫంక్షన్ కాల్స్ నిర్వహించండి
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # టూల్ ఫలితాన్ని function_call_output ఐటమ్‌గా తిరిగి ఇవ్వండి
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # రెండవ API కాల్: మోడల్ నుండి తుది ప్రతిస్పందన పొందండి
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

ఫంక్షన్ కాలింగ్ ఎక్కువ విస్తృతమైన ఏజెంట్ టూల్ వినియోగ డిజైన్ కు హృదయం, కాని దీన్ని మొదల నుండే అమలు చేయడం కొద్దిగా కష్టంగా ఉండొచ్చు.
[Lesson 2](../../../02-explore-agentic-frameworks) లో నేర్చుకున్నట్లుగా, ఏజెంటిక్ ఫ్రేమ్‌వర్క్‌లు టూల్ వినియోగం అమలుకు మునుపే నిర్మించిన నిర్మాణ బ్లాక్స్ ఇస్తాయి.
 
## ఏజెంటిక్ ఫ్రేమ్‌వర్క్‌లతో టూల్ వినియోగ ఉదాహరణలు

განსხვავებული ఏజెంటిక్ ఫ్రేమ్‌వర్క్‌లను ఉపయోగించి టూల్ వినియోగ డిజైన్ ప్యాటర్న్ ను ఎలా అమలు చేయవచ్చో కొన్ని ఉదాహరణలు ఇవి:

### Microsoft ఏజెంట్ ఫ్రేమ్‌వర్క్

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft ఏజెంట్ ఫ్రేమ్‌వర్క్</a> AI ఏజెంట్లను నిర్మించడానికి ఓపెన్-సోర్స్ ఫ్రేమ్‌వర్క్. ఇది ఫంక్షన్ కాలింగ్ ను సులభతరం చేస్తుంది, మీకు `@tool` డెకొరేటర్ తో Python ఫంక్షన్లను టూల్స్ గా నిర్వచించడానికి వీరవుతుంది. ఫ్రేమ్‌వర్క్ మోడల్ మరియు మీ కోడ్ మధ్య వెనుకబడిపై సంభాషణను నిర్వహిస్తుంది. ఇది File Search మరియు Code Interpreter లాంటి ముందుగా రూపొందించిన టూల్స్ కు `FoundryChatClient` ద్వారా ప్రాప్యత ఇస్తుంది.

క్రింది డైయాగ్రామ్ Microsoft ఏజెంట్ ఫ్రేమ్‌వర్క్ తో ఫంక్షన్ కాలింగ్ ప్రక్రియను చూపుతుంది:

![function calling](../../../translated_images/te/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework లో, టూల్స్ డెకొరేటర్ తో నిర్వచించిన ఫంక్షన్లుగా ఉంటాయి. మునుపటి `get_current_time` ఫంక్షన్ ను `@tool` డెకొరేటర్ తో టూల్ గా మార్చవచ్చు. ఫ్రేమ్‌వర్క్ ఆటోమేటిగగా ఫంక్షన్ మరియు దాని పారామితులను సిరియలైజ్ చేసి, LLM కు పంప్చే స్కీమాను రూపొందిస్తుంది.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# కస్టమర్‌ను తయారుచేసుకోండి
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ఏజెంట్‌ను సృష్టించి టూల్‌తో నిర్వహించండి
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry ఏజెంట్ సర్వీస్

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry ఏజెంట్ సర్వీస్</a> ఒక తాజా ఏజెంటిక్ ఫ్రేమ్‌వర్క్. ఇది డెవలపర్లకు భద్రతగా, అధికారికంగా AI ఏజెంట్లను నిర్మించడానికి, నిర్మాణం, మిదత, మరియు స్కేలు చేయడానికి సులభతరం చేస్తుంది. ఇది enterprise గ్రేడ్ సెక్యూరిటీతో పూర్తిగా నిర్వహించబడే సర్వీస్ కావడంతో ప్రత్యేకంగా ప్రయోజనకరం.

LLM API ని నేరుగా అభివృద్ధి చేసే సందర్భంలో పోల్చితే, Microsoft Foundry Agent Service కొన్ని ప్రయోజనాలు ఇస్తుంది:

- స్వయంచాలక టూల్ కాలింగ్ – టూల్ కాల్ ను విశ్లేషించడం, టూల్ ను పిలవడం, సమాధానాన్ని నిర్వహించడం అవసరం లేదు; ఇది అన్నీ సర్వర్ పార్టీ వద్ద జరిగిపోతాయి
- భద్రపరచబడిన డేటా – మీ స్వంత సంభాషణ స్థితిని నిర్వహించే బదులు, మీరు కావలసిన సమాచారమన్నీ థ్రెడ్‌లలో నిల్వ చేయవచ్చు
- ప్రీ-బిల్ట్ టూల్స్ – Bing, Azure AI Search మరియు Azure Functions వంటి డేటా మూలాలతో పరస్పరం చర్యకు టూల్స్ అందుబాటులో ఉన్నాయి

Microsoft Foundry Agent Service లో అందుబాటులో ఉన్న టూల్స్ రెండు వర్గాలుగా విభజించవచ్చు:

1. జ్ఞాన టూల్స్:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search తో గ్రౌండింగ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ఫైల్ శోధన</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. కార్యాచరణ టూల్స్:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ఫంక్షన్ కాలింగ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">కోడ్ ఇంటర్ప్రెటర్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI నిర్వచించిన టూల్స్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

ఏజెంట్ సర్వీస్ ఈ టూల్స్ ను కలిపి `toolset`గా వాడుకోవడానికి అనుమతిస్తుంది. ఇది ఒక సంభాషణ నుండి ప్రశ్నల చరిత్రను ట్రాక్ చేసే `threads` ను కూడా ఉపయోగిస్తుంది.

మీరు ఒక కంపెనీ పేరు Contoso లో సేల్స్ ఏజెంట్ అని ఊహించుకోండి. మీరు మీ సేల్స్ డేటా పై ప్రశ్నలకు సమాధానం ఇవ్వగల సంభాషణ ఏజెంట్‌ను రూపొందించాలని అనుకుంటున్నారు.

క్రింద ఇచ్చిన చిత్రం Microsoft Foundry Agent Service ఉపయోగించి మీ సేల్స్ డేటాను విశ్లేషించడాన్ని చూపిస్తుంది:

![Agentic Service In Action](../../../translated_images/te/agent-service-in-action.34fb465c9a84659e.webp)

ఈ సర్వీస్ తో ఏ టూల్ అయినా ఉపయోగించడానికి, మీరు ఒక క్లయింట్ సృష్టించి టూల్ లేదా టూల్ సెట్ ను నిర్వచించవచ్చు. ప్రాక్టికల్ గా అమలు చేయడానికి, క్రింది Python కోడ్ ఉపయోగించవచ్చు. LLM టూల్ సెట్ ను చూసి యూజర్ అభ్యర్థన ఆధారంగా యూజర్ రూపొందించిన ఫంక్షన్ `fetch_sales_data_using_sqlite_query` లేదా ప్రీ-బిల్ట్ కోడ్ ఇంటర్ప్రెటర్ ను ఎంచుకుంటుంది.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ఫంక్షన్ fetch_sales_data_functions.py ఫైల్లో కనిపిస్తుంది.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# టూల్‌సెట్‌ను ప్రారంభించండి
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ఫంక్షన్‌తో మరియు దాన్ని టూల్‌సెట్‌కు జోడించడం ద్వారా ఫంక్షన్ కాల్ ఏజెంట్‌ను ప్రారంభించండి
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# కోడ్ ఇంటర్‌ప్రెటర్ టూల్‌ను ప్రారంభించి టూల్‌సెట్‌కు జోడించడం.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## విశ్వసనీయ AI ఏజెంట్లు నిర్మించేప్పుడు టూల్ వినియోగ డిజైన్ ప్యాటర్న్ ఉపయోగించేటప్పుడు ప్రత్యేక గమనికలు?

LLMs ద్వారా డైనమిక్‌గా రూపొందించే SQLకు సాధారణంగా భద్రతా సంబంధించిన चिनివెంట్లు ఉన్నాయి, ముఖ్యంగా SQL ఇంజెక్షన్ లేదా దుర్మార్గ చర్యలు, ఉదాహరణకు డేటాబేస్‌ను తొలగించడం లేదా దుర్వినియోగం చేయడం. ఈ ఆందోళనలు సరిక్కానే ఉన్నప్పటికీ ఫలవంతంగా నివారించవచ్చును, ముఖ్యంగా డేటాబేస్ యాక్సెస్ అనుమతులను సరిగ్గా కంఫిగర్ చేస్తే. చాలా డేటాబేసుల కోసం ఇది సాధారణంగా డేటాబేస్ ను రీడ్-ఓన్‌లీ గా నిర్వచించడం కావాలి. PostgreSQL లేదా Azure SQL వంటి డేటాబేస్ సేవలకు యాప్ ను రీడ్-ఓన్‌లీ (SELECT) పాత్ర కేటాయించాలి.

యాప్‌ను భద్రతా వాతావరణంలో అమలుచేయడం మరిన్ని రక్షణలను ఇవ్వగలదు. ఎంటర్‌ప్రైజ్ సందర్భాలలో, డేటా సాధారణంగా ఆపరేషనల్ సిస్టమ్స్ కు చెందినది నుండి సేకరించి, రీడ్-ఓన్‌లీ డేటాబేస్ లేదా డేటా వేర్‌హౌస్ కు మార్చబడుతుంది, వీటికి సరళమైన స్కీమా ఉంటుంది. ఈ పద్ధతి డేటాను భద్రతతో, ప్రదర్శనకు అనుకూలంగా మరియు యాప్ కి పరిమితం అయిన రీడ్-ఓన్‌లీ యాక్సెస్ ఉంటుందని నిర్ధారిస్తుంది.

## నమూనా కోడ్‌లు

- Python: [ఏజెంట్ ఫ్రేమ్‌వర్క్](./code_samples/04-python-agent-framework.ipynb)
- .NET: [ఏజెంట్ ఫ్రేమ్‌వర్క్](./code_samples/04-dotnet-agent-framework.md)

## టూల్ వినియోగ డిజైన్ ప్యాటర్న్ల గురించి మరిన్ని ప్రశ్నలు ఉన్నాయా?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)లో చేరి ఇతర అభ్యర్థులతో కలుసుకోండి, ఆఫీస్ గంటలకు హాజరవండి మరియు మీ AI ఏజెంట్ల ప్రశ్నలకు సమాధానాలు పొందండి.

## అదనపు వనరులు

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service వర్క్‌షాప్</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer బహుళ ఏజెంట్ వర్క్‌షాప్</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework అవలోకనం</a>


## ఈ ఏజెంట్‌ను స్మోక్-టెస్టింగ్ చేయడం (ఐచ్ఛికం)

మీరు [పాఠం 16](../16-deploying-scalable-agents/README.md) లో ఏజెంట్లను ఎలా డిప్లాయ్ చేయాలో తెలుసుకున్న తర్వాత, మీరు ఈ పాఠంలోని `TravelToolAgent` ను స్మోక్-టెస్ట్ చేయవచ్చు (ఇది ఇంకా తన టూల్స్‌ను కాల్ చేసి జవాబివ్వుతుందా?) [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) తో. దాన్ని ఎలా నడిపించాలో తెలుసుకోవడానికి [`tests/README.md`](../tests/README.md) చూడండి.

## ముందు పాఠం

[ఎజెంటిక్ డిజైన్ ప్యాటర్న్స్‌ను అర్థం చేసుకోవడం](../03-agentic-design-patterns/README.md)

## తదుపరి పాఠం

[ఎజెంటిక్ RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->