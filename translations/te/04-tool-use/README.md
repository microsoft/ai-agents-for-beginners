[![ఎలా మంచి AI ఎజెంట్లను రూపకల్పన చేయాలి](../../../translated_images/te/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ఈ పాఠం వీడియోను వీక్షించడానికి పై చిత్రాన్ని క్లిక్ చేయండి)_

# టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్

ఈ టూల్స్ ఆసక్తికరమైనవే, ఎందుకంటే అవి AI ఏజెంట్లు విస్తృతమైన సామర్థ్యాలను కలిగి ఉండటానికి అనుమతిస్తాయి. ఏజెంట్ చేయగలిగే చర్యల పరిమిత సెట్ కలిగి ఉండటం కంటే, ఒక టూల్ జోడించడం వలన, ఏజెంట్ ఇప్పుడు విస్తృత స్థాయిలో చర్యలను చేయగలదు. ఈ అధ్యాయంలో, AI ఏజెంట్లు తమ లక్ష్యాలను సాధించడానికి ప్రత్యేక టూల్స్‌ను ఎలా ఉపయోగించగలరో వివరిస్తూ, టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్‌ను పరిశీలిస్తాము.

## పరిచయం

ఈ పాఠంలో, మనం క్రింది ప్రశ్నలకు సమాధానం ఇస్తాము:

- టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ అంటే ఏమిటి?
- దీన్ని ఎలాంటి ఉపయోగాలకు వర్తింపజేయవచ్చు?
- ఈ డిజైన్ ప్యాటర్న్ అమలు చేయడానికి అవసరమైన అంశాలు/నిర్మాణ బ్లాక్‌లు ఏమిటి?
- నమ్మకమైన AI ఏజెంట్లను నిర్మించేటప్పుడు టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ ఉపయోగిస్తున్నప్పుడు ప్రత్యేక చర్యలు ఏమిటి?

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం పూర్తి చేసుకోవడానికి తర్వాత, మీరు చేయగలరు:

- టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ మరియు దాని ఉద్దేశాన్ని నిర్వచించగలరు.
- టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ వర్తించగల ఉపయోగాల‌ను గుర్తించగలరు.
- డిజైన్ ప్యాటర్న్ అమలు చేయడానికి అవసరమైన ముఖ్య అంశాలు అర్థం చేసుకోవచ్చు.
- ఈ డిజైన్ ప్యాటర్న్ ఉపయోగించి AI ఏజెంట్ల నమ్మకాన్ని నిర్ధారించడానికి తీసుకోవలసిన చర్యలను గుర్తించగలరు.

## టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ అంటే ఏమిటి?

**టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్** LLMలకు బాహ్య టూల్స్‌తో పరస్పర చర్య చేసే సామర్థ్యాన్ని ఇవ్వడంపై దృష్టి సారిస్తుంది, ప్రత్యేక లక్ష్యాలను సాధించడానికి. టూల్స్ అంటే ఏజెంట్ ద్వారా అమలు చేయదగిన కోడ్. టూల్ ఒక సాధారణ ఫంక్షన్ (ఉదాహరణకు క్యూలిక్యులేటర్) కావచ్చు లేదా స్టాక్ ధర లుకప్ లేదా వాతావరణ అంచనా వంటి తృతీయ పక్ష సేవలకు API కాల్ కావచ్చు. AI ఏజెంట్ల సందర్భంలో, టూల్స్ **మోడల్ రూపొందించిన ఫంక్షన్ కాల్స్** కు ప్రతిస్పందనగా ఏజెంట్ ద్వారా అమలవుతాయి.

## దీన్ని ఎలాంటి ఉపయోగాలకు వర్తింపజేయవచ్చు?

AI ఏజెంట్లు పటిష్టమైన పనులను పూర్తి చేయడానికి, సమాచారాన్ని పొందడానికి లేదా నిర్ణయాలు తీసుకోవడానికి టూల్స్‌ను ఉపయోగించవచ్చు. టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ ప్రాముఖ్యత కలిగిన దృశ్యాలలో విస్తృతంగా ఉపయోగించబడుతుంది, వీటిలో డేటాబేసులు, వెబ్ సర్వీసులు, కేర్ ఇంటర్ప్రెటర్లు వంటి బాహ్య వ్యవస్థలతో డైనమిక్ పరస్పర చర్య అవసరం. కింది వివిధ ఉపయోగాలకోసం ఇది ఉపయోగపడుతుంది:

- **డైనమిక్ సమాచారం పొందుట:** ఏజెంట్లు సరికొత్త డేటాను పరిగణించడానికి బాహ్య APIs లేదా డేటాబేసులని query చేయగలరు (ఉదాహరణకు డేటా విశ్లేషణకు SQLite డేటాబేసును క్లుప్తి చేయడం, స్టాక్ ధరలు లేదా వాతావరణ సమాచారాన్ని తీసుకోవడం).
- **కోడ్ అమలు మరియు వ్యాఖ్యానం:** గణిత సమస్యలు పరిష్కరించడానికి, నివేదికలు సృష్టించడానికి లేదా అనుకరణలను నిర్వహించడానికి ఏజెంట్లు కోడ్ లేదా స్క్రిప్టులు అమలు చేయగలరు.
- **వర్క్‌ఫ్లో ఆటోమేషన్:** పనులను పునరావృతంగా చేయడం లేదా బహుళ దశల వర్క్‌ఫ్లోలను ఆటోమేట్ చేయడం, పని షెడ్యూలర్ల వంటి టూల్స్ లేదా ఇమెయిల్ సేవలు, డేటా పైప్లైన్లతో సమ్మిళితం చేయడం.
- **గ్రాహక మద్దతు:** ఏజెంట్లు CRM వ్యవస్థలు, టికెట్ ప్లాట్‌ఫారమ్‌లు లేదా జ్ఞాన బేసులతో పరస్పర చర్య చేసి వినియోగదారుల ప్రశ్నలకు సమాధానం ఇవ్వగలరు.
- **కంటెంట్ సృష్టి మరియు సవరణ:** వ్యాకరణ పరిశీలకులు, టెక్స్ట్ సమ్మరైజర్లు, కంటెంట్ భద్రతా మూల్యాంకకులు వంటి టూల్స్‌ను ఉపయోగించి కంటెంట్ సృష్టిలో సహాయం చేయగలరు.

## టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ అమలు చేయడానికి అవసరమైన అంశాలు/నిర్మాణ బ్లాక్‌లు ఏమిటి?

ఈ నిర్మాణ బ్లాక్‌లు AI ఏజెంట్లకు విస్తృతమైన పనులను చేయడానికి అనుమతిస్తాయి. టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ అమలు చేయడానికి అవసరమైన ముఖ్య అంశాలను పరిశీలిద్దాం:

- **ఫంక్షన్/టూల్ స్కీమాలు**: టూల్స్ గురించి సమగ్ర నిర్వచనలు, ఫంక్షన్ పేరు, ఉద్దేశ్యం, అవసరమైన పారామీటర్లు, మరియు ఆశించిన అవుట్‌పుట్లు. ఈ స్కీమాలు LLM-కు అందుబాటులో ఉన్న టూల్స్‌ను అర్థం చేసుకోవడానికి మరియు సరైన అభ్యర్థనలు సృష్టించడంలో సహాయపడతాయి.

- **ఫంక్షన్ అమలు లాజిక్**: యూజర్ ఉద్దేశ్యం మరియు సంభాషణ సందర్భాన్ని ఆధారంగా టూల్స్‌ను ఎప్పుడు మరియు ఎలా పిలవాలో నియంత్రిస్తుంది. ఇందులో ప్లానర్ మాడ్యూల్స్, రౌటింగ్ మెకానిజంలు లేదా షరతుల ఆధారిత ప్రవాహాలు ఉండవచ్చు.

- **సందేశం నిర్వహణ వ్యవస్థ**: యూజర్ ఇన్‌పుట్లు, LLM ప్రతిస్పందనలు, టూల్ కాల్స్ మరియు టూల్ అవుట్‌పుట్ల మధ్య సంభాషణ ప్రవాహం నిర్వహిస్తుంది.

- **టూల్ ఇంటిగ్రేషన్ ఫ్రేమ్‌వర్క్**: ఏజెంట్‌ను వివిధ టూల్స్ (సాధారణ ఫంక్షన్లు లేదా సంక్లిష్ట బాహ్య సేవలు) తో అనుసంధానం చేస్తుంది.

- **లోప నిర్వహణ & ధృవీకరణ**: టూల్ అమలులో తప్పిదాలను నిర్వహించడం, పారామీటర్లను ధృవీకరించడం మరియు అప్రమేయ ప్రతిస్పందనలను నిర్వహించడం కోసం మెకానిజంలు.

- **స్టేట్ మేనేజ్‌మెంట్**: సంభాషణ సందర్భం, గత టూల్ పరస్పర చర్యలు మరియు నిరంతర డేటాను ట్రాక్ చేయడం, బహుళ టర్న్ పరస్పర చర్యలలో సారూప్యాన్ని నిర్ధారించడం.

తర్వాత, ఫంక్షన్/టూల్ కాలింగ్ ను మరింత వివరంగా చూద్దాం.

### ఫంక్షన్/టూల్ కాలింగ్

ఫంక్షన్ కాలింగ్ LLMలు టూల్స్‌తో పరస్పరం చేయడానికి ప్రధాన మార్గం. మీరు తరచుగా 'ఫంక్షన్' మరియు 'టూల్' ని మార్పిడి గా వినిపిస్తారు, ఎందుకంటే ఫంక్షన్లు (పునఃప్రయోగించే కోడ్ బ్లాక్స్) ఏజెంట్లు పనులు చేయడానికి ఉపయోగించే 'టూల్స్'. ఫంక్షన్ కోడ్ అమలు కావడానికి, LLM యూజర్ అభ్యర్థనను ఫంక్షన్ వివరణతో సరిపోల్చాలి. అందుకోసం అందుబాటులో ఉన్న అన్ని ఫంక్షన్ల వివరణలతో స్కీమాను LLMకు పంపుతారు. LLM ఆ పనికి అత్యుత్తమమైన ఫంక్షన్‌ను ఎంచుకొని దాని పేరు మరియు ఆర్గ్యుమెంట్లను తిరిగి ఇస్తుంది. ఎంచుకున్న ఫంక్షన్ అమలు చేసి, దాని ప్రతిస్పందన LLMకు పంపబడుతుంది, అది సమాచారాన్ని యూజర్ అభ్యర్థనకు ప్రతిస్పందించడానికి ఉపయోగిస్తుంది.

డెవలపర్లకు ఏజెంట్ల కోసం ఫంక్షన్ కాలింగ్ అమలు చేయడానికి, మీరు కావాల్సిందల్లా:

1. ఫంక్షన్ కాలింగ్‌ని మద్దతు చేసే LLM మోడల్
2. ఫంక్షన్ వివరణలతో కూడిన స్కీమా
3. ప్రతి ఫంక్షన్ కోడ్ ఆమర్చబడింది

ఒక నగరంలో ప్రస్తుత సమయం తెలుసుకునే ఉదాహరణతో చూద్దాం:

1. **ఫంక్షన్ కాలింగ్ మద్దతు ఉన్న LLM ప్రారంభించండి:**

    అన్ని మోడల్స్ ఫంక్షన్ కాలింగ్ మద్దతు ఇవ్వవు, కాబట్టి మీరు ఉపయోగిస్తున్న LLM ఇలాంటి మద్దతు ఉందో చూడాలి. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ఫంక్షన్ కాలింగ్ మద్దతు ఇస్తుంది. మనం Azure OpenAI క్లయింట్ ప్రారంభించడం మొదలుపెట్టవచ్చు.

    ```python
    # Azure OpenAI క్లయింట్‌ను ప్రారంభించండి
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **ఫంక్షన్ స్కీమా సృష్టించండి**:

    తరువాత, ఫంక్షన్ పేరు, ఫంక్షన్ పని వివరణ మరియు ఫంక్షన్ పారామీటర్ల పేర్లు మరియు వివరణలతో కూడిన JSON స్కీమా నిర్వచిస్తాము.
    ఆ స్కీమాను క్రిందుగా సృష్టించిన క్లయింట్‌కు మరియు యూజర్ అడిగిన సాన్ ఫ్రాన్సిస్కో సమయం కొన్ని అభ్యర్థనతో పంపుతాము. ముఖ్యమైన విషయం ఏమిటంటే **టూల్ కాల్** తిరిగి వస్తుంది, ప్రశ్నకు తుది సమాధానం ఏది కాదు. ఇంతకు ముందు చెప్పినట్లు, LLM ఆ పనికి ఎంచుకున్న ఫంక్షన్ పేరు మరియు దానికి ఇచ్చే ఆర్గ్యుమెంట్లను తిరిగి ఇస్తుంది.

    ```python
    # నమూనా చదవడానికి ఫంక్షన్ వివరణ
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
  
    # మొదటి API కాల్: మోడల్‌ను ఫంక్షన్‌ను ఉపయోగించమని అడగండి
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # మోడల్ ప్రతిస్పందనను ప్రాసెస్ చేయండి
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

    ఇప్పుడు LLM ఎంచుకున్న ఫంక్షన్ అమలు చేయాలీ, ఆ పనిని నిర్వర్తించే కోడ్ అమలు చేయాలి.
    ప్రస్తుత సమయం పొందడానికి Pythonలో కోడ్ అమలు చేయగలం. ఫలితాన్ని పొందడానికి response_message నుంచి పేరు మరియు ఆర్గ్యుమెంట్లను ఎలా తీసుకోవాలో కూడా రాయాలి.

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
     # ఫంక్షన్ కాల్స్‌ను నిర్వహించండి
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
  
      # రెండవ API కాల్: మోడల్ నుండి తుది ప్రతిస్పందన పొందండి
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

ఫంక్షన్ కాలింగ్ చాలా ఏజెంట్ టూల్ ఉపయోగ డిజైన్ హృదయంలో ఉంటుంది, కాని కొన్నిసార్లు దీనిని మొదలుండి అమలు చేయడం కష్టం.
[Lesson 2](../../../02-explore-agentic-frameworks) లో నేర్చుకున్నట్టు, ఏజెంటిక్ ఫ్రేమ్‌వర్క్స్ పెట్టుబడి పని కోసం ముందుగానే తయారుచేసిన నిర్మాణ బ్లాక్‌లను అందిస్తాయి.

## ఏజెంటిక్ ఫ్రేమ్‌వర్క్‌లతో టూల్ ఉపయోగం ఉదాహరణలు

విభిన్న ఏజెంటిక్ ఫ్రేమ్‌వర్క్‌లను ఉపయోగించి టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్‌ను ఎలా అమలు చేయగలరో ఈ క్రింది కొన్ని ఉదాహరణలు ఉన్నాయి:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> AI ఏజెంట్లు నిర్మించడానికి ఓపెన్ సోర్స్ ఫ్రేమ్‌వర్క్. ఇది ఫంక్షన్ కాలింగ్ ప్రక్రియను సులభతరం చేస్తుంది, ఎందుకంటే మీరు టూల్స్‌ను Python ఫంక్షన్లు గా `@tool` డెకరేటర్ తో నిర్వచించవచ్చు. ఈ ఫ్రేమ్‌వర్క్ మోడల్ మరియు కోడ్ మధ్య పరస్పర టెలికం ని నిర్వహిస్తుంది. అలాగే, `AzureAIProjectAgentProvider` ద్వారా File Search మరియు Code Interpreter వంటి ముందుగానే తయారైన టూల్‌లకు యాక్సెస్ ఇస్తుంది.

క్రింది డయాగ్రామ్ Microsoft Agent Frameworkలో ఫంక్షన్ కాలింగ్ ప్రక్రియను చూపిస్తుంది:

![function calling](../../../translated_images/te/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework లో, టూల్స్ డెకరేటర్‌తో కూడిన ఫంక్షన్లుగా నిర్వచించబడతాయి. ముందు చూన `get_current_time` ఫంక్షన్‌ను `@tool` డెకరేటర్ తో టూల్గా మార్చవచ్చు. ఫ్రేమ్‌వర్క్ ఆటోమేటిక్‌గా ఫంక్షన్ మరియు దాని పారామీటర్లను సీరియలైజ్ చేసి LLMకి పంపే స్కీమాను తయారు చేస్తుంది.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# క్లైయింట్‌ను సృష్టించండి
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ఏజెంట్‌ను సృష్టించండి మరియు టూల్‌తో నడపండి
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> తక్కువగా నిర్వహణ అవసరమయ్యే, పటిష్టమైన AI ఏజెంట్లను సాధ securely గా నిర్మించడానికి, ఆపడానికి, మరియు స్కేల్ చేయడానికి డెవలపర్లకు సహాయపడే ఆధునిక ఏజెంటిక్ ఫ్రేమ్‌వర్క్. ఇది క్రింది కారణాల వల్ల ఎంటర్‌ప్రైజ్ అప్లికేషన్లకు ఉపయోగకరం:

- ఆటోమేటిక్ టూల్ కాలింగ్ – టూల్ కాల్ పార్స్ చేయాల్సిన అవసరం లేదు, టూల్‌ను కాల్ చేసి ప్రతిస్పందనను నిర్వహించడం ఇప్పుడు సర్వర్ వైపు జరుగుతుంది
- సురక్షితంగా నిర్వహించబడిన డేటా – మీ స్వంత సంభాషణ స్టేట్ నిర్వహించాల్సిన అవసరం లేదు, మీరు త్రెడ్‌లను ఉపయోగించి అవసరమైన సమాచారం నిల్వ చేయవచ్చు
- ముందుగానే సిద్ధమైన టూల్స్ – Bing, Azure AI Search, Azure Functions వంటి డేటా వనరులతో పరస్పరం చేసేందుకు టూల్స్

Azure AI Agent Serviceలో అందుబాటులో ఉన్న టూల్స్ రెండు వర్గాలుగా విభజించబడతాయి:

1. జ్ఞాన టూల్స్:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search తో గ్రౌండింగ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ఫైల్ సెర్చ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI సెర్చ్</a>

2. చర్య టూల్స్:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ఫంక్షన్ కాలింగ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">కోడ్ ఇండర్ప్రెటర్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI నిర్వచిత టూల్స్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

ఏజెంట్ సర్వీస్ ఈ టూల్స్‌ను `toolset` లుగా ఉపయోగించడానికి అనుమతిస్తుంది. ఇది ఒక సంభాషణ నుండి వచ్చిన సందేశాల చరిత్రను ట్రాక్ చేసే `threads` ను కూడా ఉపయోగిస్తోంది.

మీరు Contoso అనే సంస్థలో ఒక సేల్స్ ఏజెంట్ అని ఊహించండి. మీ సేల్స్ డేటా గురించి ప్రశ్నలకు సమాధానం చెప్పగల సంభాషణాత్మక ఏజెంట్ అభివృద్ధి చేయాలనుకుంటున్నారు.

క్రింది చిత్రం Azure AI Agent Service ఉపయోగించి సేల్స్ డేటా విశ్లేషించడం ఎలా సాధ్యం అనేదాన్ని చూపిస్తుంది:

![Agentic Service In Action](../../../translated_images/te/agent-service-in-action.34fb465c9a84659e.webp)

ఈ సర్వీస్‌తో ఏ టూల్ అయినా ఉపయోగించాలంటే, ఒక క్లయింట్ సృష్టించి టూల్ లేదా టూల్‌సెట్ నిర్వచించవచ్చు. ఫ్రాక్టికల్‌గా ఈ క్రింది Python కోడ్ ఉపయోగించవచ్చు. LLM టూల్‌సెట్‌ని పరిశీలించి, యూజర్ అభ్యర్థన ఆధారంగా `fetch_sales_data_using_sqlite_query` అనే యూజర్ సృష్టించిన ఫంక్షన్ లేదా ముందుగానే సిద్ధమైన కోడ్ ఇండర్ప్రెటర్ ఉపయోగించాలో నిర్ణయిస్తుంది.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ఫంక్షన్ fetch_sales_data_functions.py ఫైల్‌లోని ఉంది.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# టూల్‌సెట్‌ను ఆరంభించండి
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ఫంక్షన్‌తో ఫంక్షన్ కాలింగ్ ఏజెంట్‌ను ఆరంభించి, దాన్ని టూల్‌సెట్‌లో జోడించడం
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# కోడ్ ఇంటర్ప్రీటర్ టూల్‌ను ఆరంభించి టూల్‌సెట్‌లో జోడించడం.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## నమ్మకమైన AI ఏజెంట్లను నిర్మించడంలో టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ ఉపయోగించేటప్పుడు ప్రత్యేక చర్యలు ఏమిటి?

LLMs ద్వారా డైనమిక్‌గా సృష్టించిన SQL పై సాధారణ ఆందోళన భద్రత. ముఖ్యంగా SQL injection లేదా దుర్వినియోగ చర్యల ప్రమాదం, ఉదాహరణకు డేటాబేస్‌ను డ్రాప్ చేయడం లేదా దుర్వినియోగం. ఈ ఆందోళనలు సరైన డేటాబేస్ యాక్సెస్ అనుమతులు సర్దుబాటు చేయడం ద్వారా సమర్థవంతంగా తట్టుకుంటాయి. ఎక్కువ భాగం డేటాబేసులలో రీడ్-ఒన్‌గా కాన్ఫిగర్ చేయడం ఇందులో భాగం. PostgreSQL లేదా Azure SQL వంటి డేటాబేస్ సర్వీసులు ఉపయోగిస్తే, యాప్‌కు SELECT అనుమతి కలిగిన రీడ్-ఒన్ రోల్ ఇచ్చుతారు.

యాప్‌ను సురక్షితమైన వాతావరణంలో నడపడం భద్రతను పెంచుతుంది. ఎంటర్‌ప్రైజ్ సందర్భాలలో డేటాను సాధారణంగా ఆపరేషన్ వ్యవస్థల నుండి రీడ్-ఒన్ డేటాబేస్ లేదా డేటా వేర్‌హౌస్‌గా మార్చి, ఆదారమయ్యే స్కీమాతో మార్చి ఉపయోగిస్తారు. ఈ విధానం డేటా సురక్షితంగా ఉండటం, ప్రదర్శన మరియు అందుబాటులో ఉండటం, మరియు యాప్‌కు పరిమిత, రీడ్-ఒన్ యాక్సెస్ ఉండటం నిర్ధారిస్తుంది.

## నమూనా కోడ్లు

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## టూల్ ఉపయోగం డిజైన్ ప్యాటర్న్ల గురించి మరిన్ని ప్రశ్నలు ఉన్నాయా?

ఇతర అభ్యర్థులతో కలవడానికి, ఆఫీసు గంటలకు రాలడానికి మరియు మీ AI ఏజెంట్ల ప్రశ్నలకు సమాధానాలు పొందడానికి [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)లో చేరండి.

## అదనపు వనరులు

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service వర్క్షాప్</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer బహుళ ఏజెంట్ వర్క్షాప్</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework అవలోకనం</a>

## పూర్వపు పాఠం

[Agentic Design Patterns అర్ధం చేసుకోవడం](../03-agentic-design-patterns/README.md)

## తదుపరి పాఠం
[ఏజెంటిక్ RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->