[![బాగున్న AI ఏజెంట్స్ ఎలా డిజైన్ చేయాలి](../../../translated_images/te/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ఈ పాఠం వీడియోను చూడడానికి పై చిత్రం మీద క్లిక్ చేయండి)_

# టూల్ వాడకం డిజైన్ ప్యాటర్న్

టూల్స్ ఆసక్తికరమైనవి ఎందుకంటే అవి AI ఏజెంట్స్‌కు మరింత విస్తృతమైన సామర్థ్యాలను కల్పిస్తాయి. ఏజెంట్ చేయగలిగే చర్యలు పరిమితమైన సెట్ మాత్రమే ఉండటానికి బదులు, ఒక టూల్‌ను చేర్చడం ద్వారా, ఏజెంట్ ఇప్పుడు విస్తృతమైన చర్యలను చేయగలడు. ఈ అధ్యాయంలో, మేము టూల్ వాడకం డిజైన్ ప్యాటర్న్‌ను చూస్తాము, ఇది AI ఏజెంట్స్ నిర్దిష్ట లక్ష్యాలను సాధించడానికి ప్రత్యేక టూల్స్‌ని ఎలా ఉపయోగించగలరో వివరిస్తుంది.

## పరిచయం

ఈ పాఠంలో మేము ఈ కింది ప్రశ్నలకు సమాధానం ఇవ్వాలనుకుంటున్నాము:

- టూల్ వాడకం డిజైన్ ప్యాటర్న్ అంటే ఏమిటి?
- ఇది ఏవే ఉపయోగాలపై వర్తించవచ్చు?
- డిజైన్ ప్యాటర్న్ అమలు చేయడానికి అవసరమైన అంశాలు/బిల్డింగ్ బ్లాక్స్ ఏమిటి?
- నమ్మదగిన AI ఏజెంట్స్‌ను నిర్మించడానికి టూల్ వాడకం డిజైన్ ప్యాటర్న్ ఉపయోగిస్తే ప్రత్యేక శ్రద్ధ పెట్టవలసిన అంశాలు ఏమిటి?

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం పూర్తి చేసిన తర్వాత, మీరు వీటిని చేయగలుగుతారు:

- టూల్ వాడకం డిజైన్ ప్యాటర్న్ మరియు దాని ప్రయోజనాన్ని నిర్వచించగలరు.
- టూల్ వాడకం డిజైన్ ప్యాటర్న్ వర్తించగల ఉపయోగాల‌ను గుర్తించగలరు.
- డిజైన్ ప్యాటర్న్ అమలు చేయడానికి అవసరమైన ప్రధాన అంశాలను అర్థం చేసుకోగలరు.
- ఈ డిజైన్ ప్యాటర్న్ ఉపయోగించే AI ఏజెంట్స్ నమ్మకం కల్పించేందుకు అవసరమయ్యే శ్రద్ధలను గుర్తించగలరు.

## టూల్ వాడకం డిజైన్ ప్యాటర్న్ అంటే ఏమిటి?

**టూల్ వాడకం డిజైన్ ప్యాటర్న్** LLMs (లార్జ్ లాంగ్వేజ్ మోడల్స్)కు ప్రత్యేక లక్ష్యాలను సాధించడానికి బాహ్య టూల్స్‌తో సన్నిహితంగా పనిచేసే సామర్థ్యాన్ని ఇస్తుంది. టూల్స్ అనేవి ఏజెంట్ చర్యలు నిర్వహించడానికి అమలు చేయగల కోడ్. ఒక సాధారణ ఫంక్షన్ (ఉదా: కాలిక్యులేటర్) లేదా స్టాక్ ధర చూడటం లేదా వాతావరణ ఫోరకాస్ట్ వంటి మూడవ పక్ష సేవకు API కాల్ వంటి వాటి రూపంలో ఉండవచ్చు. AI ఏజెంట్స్ సందర్భంలో, టూల్స్ అనేవి **మోడల్-తయారు చేసిన ఫంక్షన్ కాల్‌ల‌కు స్పందనగా** ఏజెంట్లు అమలు చేయడానికి రూపొందించబడతాయి.

## ఇది ఏవే ఉపయోగాలపై వర్తించవచ్చు?

AI ఏజెంట్స్ టూల్స్ ఉపయోగించి సంక్లిష్ట పనులను పూర్తి చేయగలరు, సమాచారాన్ని పొందగలరు, లేదా నిర్ణయాలు తీసుకోగలరు. టూల్ వాడకం డిజైన్ ప్యాటర్న్ ఎక్కువగా డైనమిక్ పరస్పర చర్య అవసరమయ్యే సందర్భాలలో వినియోగిస్తారు, ఉదా: డేటాబేసులు, వెబ్ సర్వీసులు, లేదా కోడ్ ఇంటర్‌ప్రెటర్స్ వంటి బాహ్య వ్యవస్థలతో. ఈ సామర్థ్యం అనేక ఉపయోగాల కోసం ఉపయోగించబడుతుంది, వాటిలో:

- **డైనమిక్ సమాచారం పొందడం:** ఏజెంట్లు తాజా డేటాను పొందేందుకు బాహ్య APIలు లేదా డేటాబేసులను క్వెరీ చేయగలరు (ఉదా: డేటా విశ్లేషణకు SQLite డేటాబేసును క్వెరీ చేయడం, స్టాక్ ధరలు లేదా వాతావరణ సమాచారాన్ని తీసుకోవడం).
- **కోడ్ అమలు మరియు వివరణ:** ఏజెంట్లు గణిత సమస్యలను పరిష్కరించడానికి, రిపోర్టులు రూపొందించడానికి, లేదా సిమ్యులేషన్లు నిర్వహించడానికి కోడ్ లేదా స్క్రిప్టులను అమలు చేయగలరు.
- **వర్క్‌ఫ్లో ఆటోమేషన్:** కార్యాచరణ పునరావృతమైన లేదా బహుళ దశల పనులను అటోమేటె చేయడం, ఉదా: టాస్క్ షెడ్యూలర్స్, ఇమెయిల్ సర్వీసులు లేదా డేటా పైప్లైన్లను ఇంటిగ్రేట్ చేయడం.
- **గ్రాహక సేవా:** ఏజెంట్లు CRM వ్యవస్థలు, టికెటింగ్ ప్లాట్ఫార్ములు లేదా జ్ఞాన కేంద్రాలతో ఇంటరాక్ట్ చేసి వినియోగదారుల ప్రశ్నలకు పరిష్కారం నిస్తారు.
- **విషయ సృష్టి మరియు సవరణ:** ఏజెంట్లు వ్యాకరణ పరిశీలకులు, టెక్స్ట్ సమ్మరీజర్లు, లేదా విషయం భద్రతా మదింపు వంటి టూల్స్ ఉపయోగించి విషయ నిర్మాణ పనుల్లో సహాయం చేయగలరు.

## టూల్ వాడకం డిజైన్ ప్యాటర్న్ అమలు చేయడానికి అవసరమైన అంశాలు/బిల్డింగ్ బ్లాక్స్ ఏమిటి?

ఈ బిల్డింగ్ బ్లాక్స్ AI ఏజెంట్‌ను విస్తృతంగా పనులు చేయగలనివ్వడానికి అనుమతిస్తాయి. టూల్ వాడకం డిజైన్ ప్యాటర్న్ అమలు చేయడానికి అవసరమైన ముఖ్యమైన అంశాలను చూద్దాం:

- **ఫంక్షన్/టూల్ స్కీమాలు**: అందుబాటులో ఉన్న టూల్స్ యొక్క విస్తృత నిర్వచనాలు, ఫంక్షన్ పేరు, ప్రయోజనం, అవసరమైన పరిమాణాలు, మరియు ఆశించిన అవుట్పుట్స్ సహా. ఈ స్కీమాలు LLMకు ఏ టూల్స్ అందుబాటులో ఉన్నాయో, ఎలా సరైన అభ్యర్థనలు నిర్మించాలో అర్థం చేసుకోడానికి సహాయపడతాయి.

- **ఫంక్షన్ అమలైన తర్కం:** వినియోగదారుడి ఉద్దేశ్యం మరియు సంభాషణ సందర్భాన్ని బట్టి టూల్స్ ఎప్పుడు మరియు ఎలా పిలవబడతాయో నియంత్రిస్తుంది. ఇందులో ప్లానర్ మాడ్యూల్స్, రౌటింగ్ విధానాలు, లేదా డైనమిక్ టూల్ వాడకం నిర్ణయించే షరతు ప్రవాహాలు ఉండవచ్చు.

- **మెసేజ్ హాండ్లింగ్ సిస్టమ్:** వినియోగదారుల ఇన్‌పుట్లు, LLM ప్రతిస్పందనలు, టూల్ కాల్స్, మరియు టూల్ మూల్యాంశాల మధ్య సంభాషణ ప్రవాహాన్ని నిర్వహించే భాగాలు.

- **టూల్ ఇంటిగ్రేషన్ ఫ్రేమ్వర్క్:** ఏజెంట్‌ను వివిధ టూల్స్‌తో అనుసంధానం చేసే మౌలిక సదుపాయాలు, అవి సాదారణ ఫంక్షన్లైనా గానీ, క్లిష్టమైన బాహ్య సేవలైనా గానీ.

- **లోపాల నిర్వహణ & ధృవీకరణ:** టూల్ అమరణ లోపాలు ఎదురైనపుడు, పరిమాణాలను ధ్రువీకరించడం, మరియు అపేక్షించని ప్రతిస్పందనలను నిర్వహించే చర్యలు.

- **స్టేట్ మేనేజ్‌మెంట్:** సంభాషణ సందర్భం, పూర్వ టూల్ పరస్పర చర్యలు, మరియు బహుళ తవ్వలు సంభాషణల్లో స్థిరత్వం కోసం స్థిర-పరిశ్రమ డేటాను ట్రాక్ చేయడం.

తదుపరి, ఫంక్షన్/టూల్ కాలింగ్‌ను మరింత వివరంగా చూద్దాం.
 
### ఫంక్షన్/టూల్ కాలింగ్

ఫంక్షన్ కాలింగ్ అనేది LLMs‌కు టూల్స్‌తో ఇంటరాక్ట్ చేయడానికి ప్రధాన మార్గం. మీరు తరచూ 'ఫంక్షన్' మరియు 'టూల్' शब्दాలు మిళితంగా వాడబడతాయని చూడగలరు, ఎందుకంటే 'ఫంక్షన్లు' (మళ్లీ వినియోగించగల కోడ్ బ్లాక్స్) ఏజెంట్స్ పనులు చేయడానికి ఉపయోగించే 'టూల్స్' గా ఉంటాయి. ఫంక్షన్ కోడ్ను పిలవడానికి, LLM వినియోగదారుడి అభ్యర్థనను ఫంక్షన్ వివరణతో సరిపోల్చాలి. దీని కోసం అందుబాటులో ఉన్న అన్ని ఫంక్షన్ల వివరణలతో కూడిన ఒక స్కీమాను LLMకు పంపిస్తారు. LLM తరువాత పనికి అత్యంత అనుకూలమైన ఫంక్షన్‌ను ఎంపిక చేసి దాని పేరు మరియు ఆర్గుమెంట్లను తిరిగి ఇస్తుంది. ఎంపిక చేసిన ఫంక్షన్ కాల్ అవుతుంది, దాని ప్రతిస్పందన LLMకి పంపబడుతుంది, తరువాత LLM ఆ సమాచారంతో వినియోగదారుడి అభ్యర్థనకు జవాబు ఇస్తుంది.

ఏజెంట్స్ కోసం ఫంక్షన్ కాలింగ్‌ను అమలు చేయాలంటే, మీరు అవసరం:

1. ఫంక్షన్ కాలింగ్‌ను మద్దతు ఇచ్చే LLM మోడల్
2. ఫంక్షన్ వివరణలతో కూడిన స్కీము
3. వివరిస్తున్న ప్రతి ఫంక్షన్ కోడ్

ఉదాహరణకి, ఒక నగరంలో ప్రస్తుత సమయం పొందడం ఎలా జరుగుతుందో చూద్దాం:

1. **ఫంక్షన్ కాలింగ్ మద్దతు ఉన్న LLMని ప్రారంభించండి:**

    అన్ని మోడల్స్ ఫంక్షన్ కాలింగ్ మద్దతు ఇవ్వవు, కాబట్టి మీరు ఉపయోగిస్తున్న LLM చేయునట్లు నిర్ధారించుకోవడం ముఖ్యం. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ఫంక్షన్ కాలింగ్ మద్దతు ఇస్తుంది. మనం Azure OpenAI **Responses API** (స్థిర `/openai/v1/` ఎండ్‌పాయింట్ — ఎటువంటి `api_version` అవసరం లేదు)పై OpenAI క్లయింట్‌ను ప్రారంభిస్తూ మొదలుపెడదాం.

    ```python
    # Azure OpenAI (Responses API, v1 endpoint) కోసం OpenAI క్లయింట్‌ను ప్రారంభించండి
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **ఫంక్షన్ స్కీము సృష్టించండి**:

    తర్వాత మేము ఒక JSON స్కీమాను నిర్వచిస్తాము, ఇది ఫంక్షన్ పేరు, ఫంక్షన్ ఏమి చేస్తుందో వివరణ, మరియు ఫంక్షన్ పరిమాణాల పేర్లు మరియు వివరణలను కలిగి ఉంటుంది.
    తరువాత ఈ స్కీమాను పూర్వంలో సృష్టించిన క్లయింట్‌కు, వినియోగదారుడి సాన్ ఫ్రాన్సిస్కోలో సమయాన్ని తెలుసుకోవాలనే అభ్యర్థనతో కలిసి పంపుతాము. ముఖ్యంగా గమనించదగ్గ విషయం ఏమిటంటే, **టూల్ కాల్** తిరిగి వస్తుంది, ప్రశ్నకు తుది సమాధానం కాదు. ముందుగా చెప్పినట్టు, LLM పని కోసం ఎంపిక చేసిన ఫంక్షన్ పేరును మరియు దానికి పంపే ఆర్గుమెంట్లను ఇస్తుంది.

    ```python
    # మోడల్ చదవటానికి ఫంక్షన్ వివరణ (ప్రతిస్పందనలు API ఫ్లాట్ టూల్ ఫార్మాట్)
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

    # మొదటి API కాల్: మోడల్‌ను ఫంక్షన్‌ను ఉపయోగించమని అడగండి
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API ప్రతిస్పందనా.output‌లో function_call అంశాలుగా టూల్ కాల్‌లను తిరిగి ఇస్తుంది.
    # తదుపరి టర్న్‌లో మోడల్‌కు పూర్తి సందర్భం ఉండేలా వాటిని సంభాషణకు జతచేయండి.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **పని పూర్తి చేయడానికి అవసరమైన ఫంక్షన్ కోడ్:**

    ఇప్పుడు LLM ఎంచుకున్న ఫంక్షన్ ఏదో స్పష్టమైనది, ఆ పనిని నిర్వహించే కోడ్ అమలు చేసి నడిపించాలి.
    ప్రస్తుత సమయాన్ని Pythonలో పొందేందుకు మేము కోడ్ రాస్తాము. అలాగే, ఫైనల్ ఫలితాన్ని పొందేందుకు response_message నుండి పేరు మరియు ఆర్గుమెంట్లను తీసే కోడ్ను కూడా రాయవలసి ఉంటుంది.

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
    # ఫంక్షన్ కాల్స్ ని నిర్వహించండి
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # టూల్ ఫలితాన్ని function_call_output ఐటెమ్ గా తిరిగి ఇవ్వండి
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # రెండవ API కాల్: మోడల్ నుండి చివరి ప్రతిస్పందన పొందండి
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

ఫంక్షన్ కాలింగ్ చాలా ఏజెంట్ టూల్ వాడకం డిజైన్ల హృదయంలో ఉంది, ఇది ఒకటో సరే కానీ అమలు చేయడం కొంచెం సవాలుగా ఉంటుంది.
మేము [Lesson 2](../../../02-explore-agentic-frameworks)లో నేర్చుకున్నట్టు ఏజెంటిక్ ఫ్రేమ్వర్క్స్ ముందుండి తయారుచేసిన బిల్డింగ్ బ్లాక్స్ ఇస్తాయి టూల్ వాడకం అమలుకు.
 
## ఏజెంటిక్ ఫ్రేమ్వర్క్స్‌తో టూల్ వాడకపు ఉదాహరణలు

మీరు వివిధ ఏజెంటిక్ ఫ్రేమ్వర్క్స్ ఉపయోగించి టూల్ వాడకం డిజైన్ ప్యాటర్న్ ఎలా అమలు చేయవచ్చో కొన్ని ఉదాహరణలు ఇక్కడ ఉన్నాయి:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> AI ఏజెంట్లు నిర్మించడానికి ఓపెన్-సోర్స్ AI ఫ్రేమ్వర్క్. ఇది ఫంక్షన్ కాలింగ్ ఉపయోగాన్ని సులభతరం చేస్తుంది, మీరు Python ఫంక్షన్లను `@tool` డెకరేటర్‌తో టూల్స్‌గా నిర్వచించవచ్చు. ఈ ఫ్రేమ్వర్క్ మోడల్ మరియు మీ కోడ్ మధ్య సందేశ మార్పిడి నిర్వహిస్తుంది. ఇది File Search మరియు Code Interpreter వంటి ముందుగా తయారైన టూల్స్‌కి `FoundryChatClient` ద్వారా యాక్సెస్ ను కూడా అందిస్తుంది.

దిగువ డైగ్రామ్ Microsoft Agent Framework తో ఫంక్షన్ కాలింగ్ ప్రక్రియను చూపిస్తుంది:

![function calling](../../../translated_images/te/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Frameworkలో, టూల్స్‌ను డెకరేటర్ చేయబడిన ఫంక్షన్‌లుగా నిర్వచిస్తారు. ఆ ముందుగా చూసిన `get_current_time` ఫంక్షన్‌ను `@tool` డెకరేటర్ ఉపయోగించి టూల్‌గా మార్చవచ్చు. ఫ్రేమ్వర్క్ ఆటోమాటిక్ గా ఫంక్షన్ మరియు దాని పరిమాణాలను సీరియలైజ్ చేసి LLMకు పంపే స్కీమా సృష్టిస్తుంది.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# క్లయింట్‌ను సృష్టించండి
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# ఏజెంట్‌ని సృష్టించి టూల్‌తో అమలు చేయండి
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> ఒక కొత్త ఏజెంటిక్ ఫ్రేమ్వర్క్, ఇది డెవలపర్లకు తక్కువ కంప్యూట్ మరియు స్టోరేజ్ నిర్వహణతో సురక్షితంగా అధిక-గुणాత్మక మరియు విస్తరించదగిన AI ఏజెంట్లను నిర్మించడానికి శక్తిని ఇస్తుంది. ఇది కంపెనీ అనువర్తనాలకు చాలా ఉపయోగకరమైనదని, పూర్తి నిర్వహిత సేవగా, ఎంటర్‌ప్రైజ్ స్థాయిలో భద్రతతో ఉంటుంది.

LLM APIతో ప్రత్యక్షంగా అభివృద్ధి చేయడంనుంచి Microsoft Foundry Agent Service కొన్ని ప్రయోజనాలను ఇస్తుంది, వాటిలో:

- ఆటోమేటిక్ టూల్ కాలింగ్ – టూల్ కాల్‌ను పాస్ చేయడం, టూల్‌ను పిలవడం మరియు స్పందనను నిర్వహించడం అవసరం కాదు; ఇవన్నీ ఇప్పుడు సర్వర్-పక్షంలో జరుగుతాయి
- సురక్షితంగా నిర్వహిత డేటా – మీ స్వంత సంభాషణ స్థితి నిర్వహించే బదులుగా, అవసరమైన అన్ని సమాచారం నిల్వ చేయడానికి థ్రెడ్స్‌పై ఆధారపడవచ్చు
- తయారుచేసిన టూల్స్ – Bing, Azure AI Search, మరియు Azure Functions వంటి డేటా మూలాల‌తో ఇంటరాక్ట్ చేయడానికి మీరు ఉపయోగించగల టూల్స్.

Microsoft Foundry Agent Serviceలో అందుబాటులో ఉన్న టూల్స్ రెండు వర్గాలుగా విభజించవచ్చు:

1. జ్ఞాన టూల్స్:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search తో గ్రౌండింగ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ఫైల్ సెర్చ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI సెర్చ్</a>

2. చర్య టూల్స్:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ఫంక్షన్ కాలింగ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">కోడ్ ఇంటర్‌ప్రెటర్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI నిర్వచించబడిన టూల్స్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure ఫంక్షన్స్</a>

Agent Service మాకు ఈ టూల్స్‌ని `toolset`గా కలిపి ఉపయోగించాలనుకునే వీలును ఇస్తుంది. అదేవిధంగా ఒక సంభాషణ యొక్క సందేశ చరిత్రను నిర్వహించడానికి `థ్రెడ్స్` ఉపయోగిస్తుంది.

మీరు Contoso అనే కంపెనీలో ఒక సేల్స్ ఏజెంట్ అని ఊహించుకోండి. మీరు మీ సేల్స్ డేటా గురించి ప్రశ్నలకు జవాబివ్వగల ఒక సంభాషణాత్మక ఏజెంట్‌ను అభివృద్ధి చేయాలనుకుంటున్నారు.

దిగువ చిత్రంలో Microsoft Foundry Agent Serviceను ఉపయోగించి మీ సేల్స్ డేటాను విశ్లేషించడంపై చూపబడింది:

![Agentic Service In Action](../../../translated_images/te/agent-service-in-action.34fb465c9a84659e.webp)

ఈ సేవతో ఏ టూల్ ఉపయోగించాలనుకున్నా, మేము క్లయింట్‌ను సృష్టించి టూల్ లేదా టూల్‌సెట్‌ను నిర్వచించవచ్చు. వాస్తవికంగా అమలు చేయడానికి ఈ క్రింది Python కోడ్ ఉపయోగించవచ్చు. LLM టూల్‌సెట్‌ను చూసుకొని వినియోగదారు సృష్టించిన ఫంక్షన్ `fetch_sales_data_using_sqlite_query` తో పనిచేయాలో, లేదా ముందుగా తయారుచేసిన Code Interpreter ఉపయోగించాలో నిర్ణయించగలదు.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ఫంక్షన్ fetch_sales_data_functions.py ఫైల్‌లో ఉండేది.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# టూల్‌సెట్ ని ప్రారంభించండి
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ఫంక్షన్‌తో ఒక ఫంక్షన్ కాలింగ్ ఏజెంట్‌ను ప్రారంభించి, దానిని టూల్‌సెట్‌లో చేర్చండి
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# కోడ్ ఇంటర్‌ప్రెటర్ టూల్‌ని ప్రారంభించి, దానిని టూల్‌సెట్‌లో చేర్చండి.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## నమ్మదగిన AI ఏజెంట్స్ నిర్మించడానికి టూల్ వాడకం డిజైన్ ప్యాటర్న్ ఉపయోగంపై ప్రత్యేక శ్రద్ధలు ఏమిటి?

LLMs ద్వారా డైనమిక్‌గా సృష్టించబడే SQLతో సాధారణంగా భయంకరమైన విషయం సెక్యూరిటీ, ముఖ్యంగా SQL ఇంజెక్షన్ లేదా మరుష్య క్రూర చర్యల ప్రమాదం, ఉదా: డేటాబేస్‌ను డ్రాప్ చేయడం లేదా తవ్వడం. ఈ భయాలు నిజమైనవైనా, డేటాబేస్ యాక్సెస్ అనుమతులను సరైన విధంగా కాన్ఫిగర్ చేయడం ద్వారా అర్ధవంతంగా నివారించవచ్చు. చాలామందికి ఈ అవసరం డేటాబేస్‌ను రీడ్-ఓన్లీగా నెలకొల్పటం. PostgreSQL లేదా Azure SQL వంటి డేటాబేస్ సేవల కోసం, యాప్‌కు రీడ్-ఓన్లీ (SELECT) పాత్ర కేటాయించడం మంచిది.

యాప్‌ను సురక్షిత వాతావరణంలో నడిపించడం మరింత రక్షణను పెంపొందిస్తుంది. ఎంటర్‌ప్రైజ్ సందర్భాలలో, డేటా సాధారణంగా ఆపరేషనల్ సిస్టమ్స్ నుండి పొందిన తర్వాత రీడ్-ఓన్లీ డేటాబేస్ లేదా డేటా నిల్వ ప్రాంతంలో ఉంచబడుతుంది, అది వినియోగదారునికి సౌకర్యవంతమైన స్కీమాతో ఉంటుంది. ఈ పద్దతి డేటాను సురక్షితంగా ఉంచుతుంది, ప్రదర్శన మరియు ప్రాప్యతకు అనుకూలంగా చేస్తుంది, మరియు యాప్‌కు పరిమితమైన రీడ్-ఓన్లీ ప్రాప్యతను ఇస్తుంది.

## నమూనా కోడ్లు

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## ఇంకేమైనా ప్రశ్నలు టూల్ వాడకం డిజైన్ ప్యాటర్న్ల గురించి?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)లో చేరండి, ఇతర అభ్యాసకులను కలుసుకోండి, ఆఫీస్ గంటలకు హాజరవండి మరియు మీ AI ఏజెంట్స్ ప్రశ్నలకు జవాబులు పొందండి.

## అదనపు వనరులు

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service వర్క్షాప్</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer బహుళ ఏజెంట్ వర్క్షాప్</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework అవలోకనం</a>


## ఈ ఏజెంట్‌ను స్మోక్-టెస్టింగ్ చేయడం (ఐచ్ఛికం)

మీరు [పాఠం 16](../16-deploying-scalable-agents/README.md)లో ఏజెంట్లను డిప్లాయ్ చేయడం నేర్చుకున్న తర్వాత, మీరు ఈ పాఠంలో ఉన్న `TravelToolAgent` ను స్మోక్-టెస్ట్ చేయవచ్చు (ఇది ఇంకా తన టూల్స్‌ను کال చేస్తుందా మరియు సమాధానం ఇస్తుందా?) [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) తో. దీన్ని ఎలా పరిగణించాలో తెలుసుకోవడానికి [`tests/README.md`](../tests/README.md) చూడండి.

## మునుపటి పాఠం

[ఏజెంటిక్ డిజైన్ నమూనాలు అర్థం చేసుకోవడం](../03-agentic-design-patterns/README.md)

## తదుపరి పాఠం

[ఏజెంటిక్ RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->