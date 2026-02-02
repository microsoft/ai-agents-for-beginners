[![How to Design Good AI Agents](../../../translated_images/te/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ఈ పాఠం వీడియోను చూడటానికి పై చిత్రం పై క్లిక్ చేయండి)_

# టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్

టూల్స్ ఆసక్తికరమైనవి ఎందుకంటే అవి AI ఏజెంట్స్ కు విస్తృత పరిధి సామర్థ్యాలను 허ాయించాయి. ఏజెంట్ పరిమిత చర్యల సెట్ మాత్రమే చేయగలిగిన పరిమితమైన చర్యల స్థానంలో, ఓ టూల్ జోడించడంతో, ఏజెంట్ ఇప్పుడు విస్తృత పరిధి చర్యలను చేయగలుగుతుంది. ఈ అధ్యాయంలో మనం టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ ని పరిశీలిస్తాము, ఇది AI ఏజెంట్స్ తమ లక్ష్యాలను సాధించడానికి నిర్దిష్ట టూల్స్ ఎలా ఉపయోగించగలరో వివరిస్తుంది.

## పరిచయం

ఈ పాఠంలో, మనం క్రింది ప్రశ్నలకు సమాధానం ఇవ్వడానికి చూస్తున్నాము:

- టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ అంటే ఏమిటి?
- ఇది ఎటువంటి వినియోగ కేసులకు వర్తిస్తుంది?
- ఈ డిజైన్ ప్యాటర్న్ అమలు చేయడానికి అవసరమైన మూలకాలు/నిర్మాణ బ్లాక్స్ ఏమిటి?
- నమ్మకదాయక AI ఏజెంట్స్ తయారు చేయడానికి టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ ఉపయోగించేటప్పుడు ప్రత్యేక పరిగణనలు ఏమిటి?

## öğrenme లక్ష్యాలు

ఈ పాఠం పూర్తిచేసిన తర్వాత, మీరు వీటిని చేయగలుగుతారు:

- టూల్ ఉపయోగ డిజైన్ ప్యాటర్న్ మరియు దాని ఉద్దేశ్యాన్ని నిర్వచించండి.
- టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ వర్తించగల ఉపయోగ కేసులను గుర్తించండి.
- డిజైన్ ప్యాటర్న్ అమలులో అవసరమైన ముఖ్య మూలకాలను అర్థం చేసుకోండి.
- ఈ డిజైన్ ప్యాటర్న్ ఉపయోగించే AI ఏజెంట్స్ నమ్మకదారితనాన్ని నిర్ధారించడానికి పరిగణించాల్సిన అంశాలను తెలుసుకోండి.

## టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ అంటే ఏమిటి?

**టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్** LLMs కి నిర్దిష్ట లక్ష్యాలను సాధించడానికి బాహ్య టూల్స్ తో సంభాషణ చేయగల సామర్థ్యాన్ని ఇస్తుంది. టూల్స్ అనేవి ఒక ఏజెంట్ చేత అమలు చేయదగ్గ కోడ్. ఒక టూల్ సాధారణంగా లెక్కింపుకర్త వంటి ఫంక్షన్ అవొచ్చును లేదా స్టాక్ ధరలు లేదా వాతావరణ అంచనాకు సంబంధించిన మూడవ పక్ష సేవల API కాల్ అయివుండొచ్చు. AI ఏజెంట్స్ సందర్భంలో, టూల్స్ ఎదురు **మోడల్-జనరేట్ చేసిన ఫంక్షన్ కాల్స్** కి ప్రతిస్పందనగా Agents అమలు చేసేందుకు రూపొందించబడ్డాయి.

## ఇది ఎటువంటి వినియోగ కేసులకు వర్తిస్తుంది?

AI ఏజెంట్స్ సంక్లిష్ట పనులు పూర్తిచేయడానికి, సమాచారం పొందడానికి లేదా నిర్ణయాలు తీసుకోవడానికి టూల్స్ ఉపయోగించవచ్చు. టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ కి సాధారణంగా డైనమిక్ ఇంటరాక్షన్ అవసరమైన సందర్భాలలో, ఉదాహరణకు డేటాబేసులు, వెబ్ సర్వీస్లు లేదా కోడ్ ఇంటర్ప్రిటర్లు లాంటి బాహ్య వ్యవస్థలతో ఉపయోగిస్తారు. ఇది కింది వివిధ సందర్భాలకు ఉపయోగకరం:

- **డైనమిక్ సమాచారం పొందడం:** ఏజెంట్లు బాహ్య APIs లేదా డేటాబేసులను క్యారీ చేసి తాజా డేటా పొందగలవు (ఉదాహరణకు, SQLite డేటాబేస్ క్వెరీ చేసి డేటా విశ్లేషణ, స్టాక్ ధరలు లేదా వాతావరణ సమాచారం పొందడం).
- **కోడ్ అమలుచేయడం మరియు విశ్లేషణ:** ఏజెంట్లు గణిత సమస్యలు పరిష్కరించేందుకు, నివేదికలు సృష్టించేందుకు లేదా అనుకరణలు నిర్వహించడానికి కోడ్ లేదా స్క్రిప్టులను అమలు చేయగలవు.
- **వర్క్‌ఫ్లో ఆటోమేషన్:** పనులను నియమకాలికంగా లేదా బహుళ దశలుగా ఆటోమేట్ చేయడం, ఉదాహరణకు, టాస్క్ షెడ్యూలర్స్, ఇమెయిల్ సేవలు లేదా డేటా పైప్‌లైన్లను ఇంటిగ్రేట్ చేయడం.
- **కస్టమర్ సపోర్ట్:** ఏజెంట్లు CRM వ్యవస్థలు, టికెటింగ్ ప్లాట్‌ఫారమ్లు, లేదా నోలేజ్ బేస్‌లతో ఇంటరాక్ట్ చేసి వినియోగదారుల ప్రశ్నలకు సమాధానమిస్తాయి.
- **కంటెంట్ ఉత్పత్తి మరియు ఎడిటింగ్:** ఏజెంట్లు గ్రామర్ చెకర్లు, టెక్స్ట్ సారాంశాలు, లేదా కంటెంట్ సురక్షితత మూల్యాంకన టూల్స్ లాంటి సహాయక టూల్స్ ఉపయోగించి కంటెంట్ సృష్టి పనుల్లో సహాయం చేస్తాయి.

## టూల్ ఉపయోగ డిజైన్ ప్యాటర్న్ అమలుకు అవసరమైన మూలకాలు/నిర్మాణ బ్లాక్స్ ఏమిటి?

ఈ బ్లాక్స్ AI ఏజెంట్ కు విస్తృత పనులు చేయడానికి అవకాశం ఇస్తాయి. టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ అమలు చేయడానికి అవసరమైన ముఖ్య అంశాలు:

- **ఫంక్షన్/టూల్ స్కీమాలు**: అందుబాటులో ఉన్న టూల్స్ వివరమైన నిర్వచనాలు, ఫంక్షన్ పేరు, ఉద్దేశ్యం, అవసరమైన పారామితులు మరియు ఆశించిన అవుట్పుట్ లతో. ఈ స్కీమాలు LLM కి అందుబాటులో ఉన్న టూల్స్ ఏమిటి, ఎలా చెలాయించాలో అర్థం చేసుకోవడంలో సహాయపడతాయి.

- **ఫంక్షన్ అమలుచేసే తర్కం**: వినియోగదారుడి ఉద్దేశ్యానికి మరియు సంభాషణ సందర్భానుసారం టూల్స్ ఎప్పుడు మరియు ఎలా పిలవబడాలో నియంత్రిస్తుంది. దీంట్లో ప్లానర్ మాడ్యూల్స్, రౌటింగ్ యంత్రాంగాలు, లేదా షరతు ఆధారిత ప్రవాహాలు ఉండవచ్చు.

- **మెసేజ్ హ్యాండ్లింగ్ సిస్టం**: వినియోగదారుల ఇన్‌పుట్లు, LLM స్పందనలు, టూల్ కాల్స్, టూల్ అవుట్పుట్ల మధ్య సంభాషణ ప్రవాహాన్ని నిర్వహించే భాగాలు.

- **టూల్ ఇంటిగ్రేషన్ ఫ్రేమ్‌వర్క్**: ఏజెంట్‌ను వివిధ టూల్స్‌కి కలుపుతుంది, అవి సాధారణ ఫంక్షన్స్ కావచ్చు లేదా సంక్లిష్ట బాహ్య సేవలు కావచ్చు.

- **లోపాల నిర్వహణ మరియు సరైనదీనా ధృవీకరణ**: టూల్ అమలులో వైఫల్యాలను నిర్వహించడం, పారామితులను ధృవీకరించడం, మరియు అనుకోని ప్రతిస్పందనల్ని నిర్వహించడం.

- **స్థితి నిర్వహణ**: సంభాషణ సందర్భం, గత టూల్ ఇంటరాక్షన్‌లు మరియు నిర్దిష్ట డేటా ట్రాక్ చేయడం, బహుళ తత్వ సంభాషణల్లో సుసంగతిని నిర్ధారించడానికి.

తరువాత, మనం ఫంక్షన్/టూల్ కాలింగ్ ని మరిన్ని వివరాలతో చూద్దాం.
 
### ఫంక్షన్/టూల్ కాలింగ్

ఫంక్షన్ కాలింగ్ అనేది LLMs కి టూల్స్ తో సంభాషణ చేయడానికి ప్రధాన పద్ధతి. తరచుగా ‘ఫంక్షన్’ మరియు ‘టూల్’ పదాలు మార్పిడిగా ఉపయోగిస్తారు ఎందుకంటే ‘ఫంక్షన్‌లు’ (పునః ఉపయోగించదగిన కోడ్ బ్లాక్స్) అనేవి ఏజెంట్లు పనులు సమర్పించడానికి ఉపయోగించే ‘టూల్స్’ అవుతాయి. ఒక ఫంక్షన్ కోడ్ అమలుచేయబడాలంటే, LLM వినియోగదారి అభ్యర్థనను ఆ ఫంక్షన్ వివరణతో సరిపోల్చాలి. అందుకోసం అందుబాటులో ఉన్న అన్ని ఫంక్షన్‌ల వివరణలతో కూడిన ఒక స్కీమాను LLM కి పంపుతారు. LLM ఆ పని కోసం సరైన ఫంక్షన్‌ని ఎంచుకుని దాని పేరు మరియు పారామితులను తిరిగి ఇస్తుంది. ఆ ఫంక్షన్ అమలుచేయబడుతుంది, దాని స్పందన ఆ LLM కి పంపబడుతుంది, అది సమాచారం ఆధారంగా వినియోగదారుని అభ్యర్థనకు స్పందన ఇస్తుంది.

డెవలపర్లకు ఏజెంట్లకు ఫంక్షన్ కాలింగ్ అమలు చేయాలంటే, అవసరం:

1. ఫంక్షన్ కాలింగ్‌కు మద్దతు ఇచ్చే LLM మోడల్
2. ఫంక్షన్ వివరణలతో కూడిన స్కీమా
3. ప్రతి ఫంక్షన్ వివరణ కోసం కోడ్

నాలెడ్జ్ కోసం నగరంలో ప్రస్తుత సమయాన్ని పొందడాన్ని ఉదాహరణగా తీసుకుందాం:

1. **ఫంక్షన్ కాలింగ్ మద్దతు కలిగిన LLM ను ప్రారంభించండి:**

    అన్ని మోడళ్లు ఫంక్షన్ కాలింగ్ మద్దతు ఇవ్వవు, కాబట్టి మీరు ఉపయోగిస్తున్న LLM దీనిని మద్దతిస్తుందో లేదో తనిఖీ చేయడం ముఖ్యం. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ఫంక్షన్ కాలింగ్ మద్దతు ఇస్తుంది. మేము Azure OpenAI క్లయింట్ ను ప్రారంభించడం మొదలు పెట్టవచ్చు.

    ```python
    # Azure OpenAI clientని ప్రారంభించండి
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **ఫంక్షన్ స్కీమా సృష్టించండి**:

    తరువాత, ఫంక్షన్ పేరు, ఫంక్షన్ ఏ పని చేస్తుందో వివరణ, ఫంక్షన్ పారామితుల పేర్లు మరియు వివరణలతో కూడిన JSON స్కీమాను నిర్వచిస్తాము.
    ఈ స్కీమాను మేము ఇప్పటికే సృష్టించిన క్లయింట్‌కు పంపుతాము, అందుబాటులో ఉన్న వినియోగదారి అభ్యర్థనతో సాన్ ఫ్రాన్సిస్కోలో సమయం తెలుసుకోవడానికి. ముఖ్యమైన విషయం ఏంటంటే, **టూల్ కాల్** తిరిగి వస్తుంది, ప్రశ్నకు ధృవీకరించిన సమాధానం కాదు. ముందుగా చెప్పినట్లుగా, LLM పని కోసం ఎంచుకున్న ఫంక్షన్ పేరు మరియు అందుబాటులో పంపవలసిన ఆర్గ్యుమెంట్లు ఇస్తుంది.

    ```python
    # మోడల్ చదవడానికి ఫంక్షన్ వివరణ
    tools = [
        {
            "type": "function",
            "function": {
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
        }
    ]
    ```
   
    ```python
  
    # ప్రారంభ వినియోగదారు సందేశం
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # మొదటి API కాల్: మోడల్‌ను ఫంక్షన్ ఉపయోగించమని అడగండి
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # మోడల్ యొక్క ప్రతిసారీని ప్రాసెస్ చేయండి
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **పని నిర్వహించడానికి అవసరమైన ఫంక్షన్ కోడ్:**

    ఇప్పుడు LLM ఎన్నుకున్న ఫంక్షన్ అమలు చేయడానికి కావలసిన కోడ్ ను మీరు అమలు చేసి అమలు చేయాలి.
    Pythonలో ప్రస్తుత సమయాన్ని పొందడానికి కోడ్ ని అమలు చేయవచ్చు. చివరి ఫలితాన్ని పొందడానికి, response_message నుండి ఫంక్షన్ పేరు మరియు ఆర్గ్యుమెంట్లను వెలికి తీసే కోడ్ కూడా వ్రాయాల్సి ఉంటుంది.

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
     # ఫంక్షన్ కాల్స్‌ని నిర్వహించండి
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # రెండవ API కాల్: మోడల్ నుండి తుది ప్రతిస్పందనను పొందండి
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

ఫంక్షన్ కాలింగ్ చాలా ఏజెంట్ టూల్ ఉపయోగ డిజైన్ గుండెల్లో ఉంటుంది, అయితే దాన్ని మొదటి నుండి అమలు చేయడం కొద్దిగా కష్టమైనది కావచ్చు. మనం [Lesson 2](../../../02-explore-agentic-frameworks) లో నేర్చుకున్నట్లు ఏజెంటిక్ ఫ్రేమ్‌వర్క్లు ఇప్పటికే రూపొందించిన మూలకాలు అందిస్తాయి టూల్ ఉపయోగాన్ని అమలు చేయడానికి.

## ఏజెంటిక్ ఫ్రేమ్‌వర్క్స్ తో టూల్ ఉపయోగం ఉదాహరణలు

వివిధ ఏజెంటిక్ ఫ్రేమ్‌వర్క్స్ ఉపయోగించి టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ ని ఎలా అమలు చేయవచ్చో కొన్ని ఉదాహరణలు ఇక్కడ ఉన్నాయి:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> అనేది .NET, Python, మరియు Java డెవలపర్లు LLMs తో పనిచేయడానికి ఓపెన్ సోర్స్ AI ఫ్రేమ్‌వర్క్. ఇది మీరు ఫంక్షన్లను ఆటోమేటిక్ గా వివరిస్తూ, ఫంక్షన్ కాలింగ్ ప్రక్రియను సులభతరం చేస్తుంది <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">సీరియలైజింగ్</a> అనే ప్రక్రియ ద్వారా. ఇది మోడల్ మరియు మీ కోడ్ మధ్య సమాచారం మార్పిడిని కూడా నిర్వహిస్తుంది. Semantic Kernel వంటి ఏజెంటిక్ ఫ్రేమ్‌వర్క్ ఉపయోగించడం మరో లాభం, ఇది ముందుగా ఉంటుంది రూపొందించిన టూల్స్, ఉదాహరణకు <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">ఫైల్ సెర్చ్</a> మరియు <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">కోడ్ ఇంటర్ప్రిటర్</a> అందిస్తుంది.

క్రింది చిత్రం Semantic Kernel తో ఫంక్షన్ కాలింగ్ ప్రాసెస్ ను చూపిస్తుంది:

![function calling](../../../translated_images/te/functioncalling-diagram.a84006fc287f6014.webp)

Semantic Kernel లో ఫంక్షన్స్/టూల్స్ ని <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">ప్లగిన్స్</a> అంటారు. మనం ముందుగా చూడిన `get_current_time` ఫంక్షన్ ను ఒక క్లాస్ గా మార్చి, ఆ క్లాస్ లో ఫంక్షన్ ను ఉంచి ఒక ప్లగిన్ గా మార్చవచ్చు. అప్పుడు మీరు GetCurrentTimePlugin తో kernel సృష్టిస్తే, kernel ఆటోమేటిక్ గా ఫంక్షన్ మరియు దాని పారామితులను సీరియలైజ్ చేసి LLM కి పంపే స్కీమాను సృష్టిస్తుంది.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# కర్నల్‌ను సృష్టించండి
kernel = Kernel()

# ప్లగిన్‌ను సృష్టించండి
get_current_time_plugin = GetCurrentTimePlugin(location)

# ప్లగిన్‌ను కర్నల్‌లో జోడించండి
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> అనేది కొత్త ఏజెంటిక్ ఫ్రేమ్‌వర్క్, ఇది డెవలపర్లకు సురక్షితంగా, అధిక-నాణ్యత, మరియు విస్తరింపునిచ్చే AI ఏజెంట్లను నిర్మించడానికి, డిప్లాయ్ చేయడానికి, మరియు పరిమాణాన్ని పెంచడం కోసం రూపొందించబడింది, లోపలి కంప్యూటు మరియు నిల్వ వనరులను నిర్వహించాల్సిన అవసరం లేకుండా. ఇది ముఖ్యంగా ఎంటర్‌ప్రైజ్ అప్లికేషన్లకు ఉపయోగకరం ఎందుకంటే ఇది పూర్తిగా మేనేజ్ అయ్యే సర్వీస్ గాను ఎంటర్‌ప్రైజ్ స్థాయి భద్రత కల్గివున్నది.

నేరుగా LLM APIతో అభివృద్ధి చేసినందునAzure AI Agent Service కొన్ని ఇబ్బందులను బాగా సులభతరం చేస్తుంది, ఉదాహరణకు:

- ఆటోమేటిక్ టూల్ కాలింగ్ – టూల్ కాల్ పార్స్ చేయాల్సిన అవసరం లేదు, టూల్ ను పిలవడం, మరియు ప్రతిస్పందన నిర్వహించడం; ఇవి ఇప్పుడు సర్వర్‌ సైడ్‌లో జరుగుతాయి
- సురక్షితంగా నిర్వహించే డేటా – మీ స్వంత సంభాషణ స్థితిని నిర్వహించాల్సిన అవసరం లేకుండా, మీరు కావలసిన అన్ని సమాచారాన్ని స్టోర్ చేయడానికి థ్రెడ్స్‌పై ఆధారపడవచ్చు
- రెడీ-టు-యూజ్ టూల్స్ – Bing, Azure AI Search మరియు Azure Functions లాంటి డేటా మూలాలతో ఇంటరాక్ట్ చేయడానికి ఉపయోగించే టూల్స్.

Azure AI Agent Service లో అందుబాటులో ఉన్న టూల్స్ రెండు విభాగాల్లో విభజించవచ్చు:

1. జ్ఞాన టూల్స్:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search తో గ్రౌండింగ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ఫైల్ సెర్చ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. చర్య టూల్స్:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ఫంక్షన్ కాలింగ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">కోడ్ ఇంటర్ప్రిటర్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI నిర్వచించిన టూల్స్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ఈ టూల్స్ ని `toolset` గా కలిసి ఉపయోగించే వీలును ఇస్తుంది. ఇది ఒకటేప్పుడు ప్రత్యేక సంభాషణ నుండి సందేశాల చరిత్రను ట్రాక్ చేసే `సంభాషణ థ్రెడ్స్` ను కూడా ఉంచుతుంది.

మీరు Contoso అనే కంపెనీలో ఒక సేల్స్ ఏజెంట్‌‌గా ఉన్నారని ఊహించుకోండి. మీరు మీ సేల్స్ డేటా గురించి ప్రశ్నలకు సమాధానం ఇవ్వగల సంభాషణ ఏజెంట్ ని అభివృద్ధి చేయాలనుకుంటున్నారు.

క్రింద చిత్రం Azure AI Agent Service ఉపయోగించి మీ సేల్స్ డేటా విశ్లేషణ ఎలా చేయవచ్చో చూపిస్తుంది:

![Agentic Service In Action](../../../translated_images/te/agent-service-in-action.34fb465c9a84659e.webp)

ఈ టూల్స్ లో ఏదైనా టూల్ ను సర్వీస్ తో ఉపయోగించడానికి క్లయింట్ సృష్టించి టూల్ లేదా టూల్‌సెట్ నిర్వచించవచ్చు. ప్రాక్టికల్ గా ఈ పైన ఇచ్చిన Python కోడ్ ను ఉపయోగించి తీసుకొని అమలు చేసుకోవచ్చు. LLM టూల్‌సెట్ ను చూసి వినియోగదారుడు రూపొందించిన ఫంక్షన్ `fetch_sales_data_using_sqlite_query` ను ఉపయోగించాలా లేదా ముందుగా ఉన్న కోడ్ ఇంటర్ప్రిటర్ ను ఉపయోగించేలా నిర్ణయం తీసుకుంటుంది వినియోగదారి అభ్యర్థన ఆధారంగా.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_functions.py ఫైల్‌లో ఉన్నాయి fetch_sales_data_using_sqlite_query ఫంక్షన్.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# టూల్‌సెట్ ప్రారంభించండి
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ఫంక్షన్‌తో ఫంక్షన్ కాలింగ్ ఏజెంట్‌ను ప్రారంభించి దాన్ని టూల్‌సెట్‌కు జోడించండి
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# కోడ్ ఇంటర్‌ప్రీటర్ టూల్‌ను ప్రారంభించి దాన్ని టూల్‌సెట్‌కు జోడించండి.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## నమ్మకత కలిగిన AI ఏజెంట్స్ రూపొందించడానికి టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ ఉపయోగిస్తున్నప్పుడు ప్రత్యేక పరిగణనలు ఏమిటి?

LLMs ద్వారా డైనమిక్ గా రూపొందించిన SQL కి సాధారణ పోకడ భద్రతకు సంబంధించిన సమస్యలు ఉంటాయి, ముఖ్యంగా SQL ఇంజెక్షన్ లేదా హానికర చర్యల ప్రమాదం, ఉదాహరణకు డేటాబేస్ డ్రాప్ చేయడం లేదా దేనితో సరదాగా చెలాయించడం. ఈ ఆందోళనలు సరైనవైనా, డేటాబేస్ యాక్సెస్ అనుమతులను సరైన రీతిలో అమర్చడం ద్వారా అవి సమర్థవంతంగా తట్టుకొనవచ్చు. చాలా డేటాబేస్ లకు దీనిలో భాగంగా డేటాబేస్ ను చదవడానికి మాత్రమే అనుమతులు కల్పించడం ఉంటుంది. PostgreSQL లేదా Azure SQL వంటి డేటాబేస్ సేవల కోసం, యాప్ కు చదవడానికి మాత్రమే (SELECT) రోల్ ఇవ్వాలి.
అప్లికేషన్‌ను సురక్షిత వాతావరణంలో నడిపించడం మరింత పరిరక్షణను పెంచుతుంది. ఎంటర్ప్రైజ్ పరిసరాల్లో, డేటాను సాధారణంగా ఆపరేషనల్ సిస్టమ్‌ల నుండి తీసుకుని, రీడ్-ఒన్లీ డేటాబేస్ లేదా డేటా గోదాములో యూజర్-ఫ్రెండ్లీ స్కీమాతో మార్చబడుతుంది. ఈ విధానం డేటా సురక్షితంగా ఉండడం, పనితీరు మరియు ప్రాప్తి కోసం అభివృద్ధి చేయడం మరియు అప్లికేషన్‌కు పరిమితమైన, రీడ్-ఒన్లీ యాక్సెస్ ఉండడం నిర్ధారిస్తుంది.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**డిస్క్లెయిమర్**:  
ఈ డాక్యుమెంట్ [Co-op Translator](https://github.com/Azure/co-op-translator) అనే AI అనువాద సేవని ఉపయోగించి అనువదించబడింది. స్పష్టత కోసం ప్రయత్నించినప్పటికీ, స్వయంచాలక అనువాదాల్లో పొరపాట్లు లేదా తప్పులొ ప్రమాణాలు ఉండవచ్చును. అతి ముఖ్యమైన సమాచారం కోసం, నేటివ్భాషలో ఉన్న మూల పత్రాన్ని అధికార మూలంగా పరిగణించాలి. కీలకమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం ఆవశ్యకం. ఈ అనువాదం వలన ఏర్పడిన ఏదైనా అవగాహన లోపాలు లేదా తప్పుబాటులకు మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->