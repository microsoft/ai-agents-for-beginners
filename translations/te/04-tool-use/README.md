[![How to Design Good AI Agents](../../../translated_images/te/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(ఈ పాఠం యొక్క వీడియోను చూడటానికి పై చిత్రం పై క్లిక్ చేయండి)_

# టూల్ వినియోగ డిజైన్ నమూనా

టూల్స్ ఆసక్తికరమైనవి ఎందుకంటే అవి AI ఏజెంట్స్ కు విస్తృతమైన సామర్థ్యాలను కల్పిస్తాయి. ఏజెంట్ను పరిమిత చర్యల సెట్ మాత్రమే చేయగలిగితే, టూల్ ను జోడించడం ద్వారా ఏజెంట్ ఇప్పుడు విస్తృత ఉత్పన్నాలను చేయగలుగుతుంది. ఈ అధ్యాయంలో, AI ఏజెంట్స్ తమ లక్ష్యాలను సాధించడానికి నిర్దిష్ట టూల్స్ ను ఎలా ఉపయోగించగలరో వివరిస్తూ టూల్ వినియోగ డిజైన్ నమూనాను చూద్దాము.

## పరిచయం

ఈ పాఠంలో, మేము క్రింది ప్రశ్నలకు సమాధానం పొందడానికి చూస్తున్నాము:

- టూల్ వినియోగ డిజైన్ నమూనా అంటే ఏమిటి?
- ఇది ఎటువంటి వినియోగ కేసులకు వర్తిస్తుంది?
- డిజైన్ నమూనాను అమలు చేయడానికి ఏ అంశాలు/నిర్మాణ భాగాలు అవసరం?
- నమ్మదగిన AI ఏజెంట్స్ ను నిర్మించడంలో టూల్ వినియోగ డిజైన్ నమూనా ఉపయోగిస్తూఉండే ప్రత్యేక విషయాలు ఏమిటి?

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం పూర్తయిన తర్వాత, మీరు చేయగలుగుతారు:

- టూల్ వినియోగ డిజైన్ నమూనా మరియు దీని ఉద్దేశాన్ని నిర్వచించండి.
- టూల్ వినియోగ డిజైన్ నమూనా ఎక్కడ వర్తించవచ్చు అనేది గుర్తించండి.
- డిజైన్ నమూనా అమలుకు అవసరమైన ముఖ్య అంశాలను అర్థం చేసుకోండి.
- ఈ డిజైన్ నమూనాను ఉపయోగించి AI ఏజెంట్లలో నమ్మకాన్ని నిర్ధారించడానికి సంబంధమైన విషయాలను గుర్తించండి.

## టూల్ వినియోగ డిజైన్ నమూనా అంటే ఏమిటి?

**టూల్ వినియోగ డిజైన్ నమూనా** LLMలను నిర్దిష్ట లక్ష్యాలను సాధించేందుకు బాహ్య టూల్స్ తో పరస్పరం చేసుకునే సామర్థ్యాన్ని ఇవ్వడాన్ని కేంద్రీకరిస్తుంది. టూల్స్ అనేవి ఏజెంట్ చేస్తున్న చర్యలను అమలు చేయడానికి కోడ్ రూపంలో ఉంటాయి. ఒక టూల్ సాధారణ ఫంక్షన్ (ఉదాహరణకు గణన యంత్రం) లేదా స్టాక్ ధరల చూడటం లేదా వాతావరణ సూచించటం వంటి మూడవ పక్ష సేవలకు API కాల్ కూడా కావచ్చు. AI ఏజెంట్ల సందర్భంలలో, టూల్స్ **మోడల్ ఉత్పత్తి చేసిన ఫంక్షన్ కాల్స్** కు ప్రతిస్పందనగా ఏజెంట్లచే అమలు చేయడానికి డిజైన్ చేయబడ్డాయి.

## ఇది ఎటువంటి వినియోగ కేసులకు వర్తించవచ్చు?

AI ఏజెంట్లు క్లిష్టమైన పనులను పూర్తిచేయడానికి, సమాచారాన్ని పొందడానికి లేదా నిర్ణయాలు తీసుకోవడానికి టూల్స్ ను ఉపయోగించవచ్చు. టూల్ వినియోగ డిజైన్ నమూనా సాధారణంగా డేటాబేసులు, వెబ్ సర్వీసులు లేదా కోడ్ ఇంటერპ్రెటర్లు లాంటి బాహ్య వ్యవస్థలతో డైనమిక్ పరస్పరం అవసరమైన సందర్భాల్లో ఉపయోగిస్తారు. ఈ సామర్థ్యం వివిధ వినియోగాల్లో ఉపయోగకరంగా ఉంటుంది, ఉదాహరణలు:

- **డైనమిక్ సమాచార సేకరణ:** ఏజెంట్లు బాహ్య APIలు లేదా డేటాబేసులను ప్రశ్నించి తాజా సమాచారం పొందగలుగుతాయి (ఉదా: డేటా విశ్లేషణకు SQLite డాటాబేస్ ప్రశ్నించడం, స్టాక్ ధరలు లేదా వాతావరణ సమాచారం తీసుకొనడం).
- **కోడ్ అమలు మరియు అర్థం చేసుకోవడం:** గణిత సమస్యలను పూరణ చేయడానికి, నివేదికలు తలపెట్టడానికి లేదా సిమ్యులేషన్లు నిర్వహించడానికి ఏజెంట్లు కోడ్ లేదా స్క్రిప్ట్ లను అమలు చేయగలరు.
- **వర్క్‌ఫ్లో ఆటోమేషన్:** పనులు పునరావృత అవుతుంటే లేదా బహుళ దశల వర్క్‌ఫ్లోలను టాస్క్ షెడ్యూలర్లు, ఇమెయిల్ సర్వీస్‌లు లేదా డేటా పైపలైన్ల జతచేసి ఆటోమేట్ చేయడం.
- **కస్టమర్ సపోర్ట్:** ఏజెంట్లు CRM వ్యవస్థలు, టికెట్లు ప్లాట్‌ఫారములు లేదా నాలెడ్జ్ బేసుల తో పరస్పరం చేసి వినియోగదారు ప్రశ్నలకు సమాధానం ఇస్తాయి.
- **కంటెంట్ తయారీ మరియు సవరణ:** వ్యాకరణ తనిఖీ, టెక్స్ట్ సారాంశ సమర్పణ లేదా కంటెంట్ సేఫ్టీ మూల్యాంకనం వంటి టూల్స్ ఉపయోగించి కంటెంట్ సృష్టి పనులలో సహాయం చేసుకోవచ్చు.

## టూల్ వినియోగ డిజైన్ నమూనా అమలుకు అవసరమైన అంశాలు/నిర్మాణ భాగాలు ఏమిటి?

ఈ నిర్మాణ భాగాలు AI ఏజెంట్ విస్తృతమైన పనులను చేయగల సామర్థ్యం ఇస్తాయి. టూల్ వినియోగ డిజైన్ నమూనా అమలుకు అవసరమైన ముఖ్య అంశాలు:

- **ఫంక్షన్/టూల్ స్కీమాలు**: అందుబాటులో ఉన్న టూల్స్ యొక్క సవివరమైన నిర్వచనాలు, అందులో ఫంక్షన్ పేరు, ఉద్దేశ్యం, అవసరమైన పరామితులు మరియు ఓటు ఫలితాలు ఉంటాయి. ఈ స్కీమాలు LLMకు ఏ టూల్స్ అందుబాటులో ఉన్నాయో మరియు చెలామణి యోగ్య అభ్యర్థనలు ఎలా తయారుచేయాలో అర్థం చేసుకోవడంలో సహాయం చేస్తాయి.

- **ఫంక్షన్ అమలులో తర్కం**: వాడుకరి ఉద్దేశం మరియు సంభాషణ సందర్భం ఆధారంగా టూల్స్ ఎప్పుడు, ఎలా వాడాలో నియంత్రిస్తుంది. ఇందులో ప్లానర్ మాడ్యూల్‌లు, రౌటర్ విధానాలు లేదా కండిషనల్ ఫ్లోలు ఉంటాయి.

- **సందేశ నిర్వహణ వ్యవస్థ**: వాడుకరి ఇన్‌పుట్స్, LLM ప్రతిస్పందనలు, టూల్ కాల్స్ మరియు టూల్ అవుట్‌పుట్స్ మధ్య సంభాషణ ప్రవాహాన్ని నిర్వహించే భాగాలు.

- **టూల్ సమకూర్చే ఫ్రేమ్‌వర్క్**: ఏజెంట్ ను వివిధ టూల్స్ (సాధారణ ఫంక్షన్స్ లేదా గందరగోళమైన బాహ్య సేవలు) కు అనుసంధానం చేసే మౌలికవసతలు.

- **లోప నిర్వహణ & సరైనదని నిర్ధారణ**: టూల్ అమలులో విఫలమైన సందర్భాలను నిర్వహించటం, పరామితులను ధృవీకరించటం మరియు అనుకోని ప్రతిస్పందనలను నిర్వహించే చర్యలు.

- **స్థితి నిర్వహణ**: సంభాషణ సందర్భం, పూర్వ టూల్ పరస్పర చర్యలు మరియు పర్యావృత డేటాను ట్రాక్ చేసి బహుళ త్రిటి పరస్పర చర్యల్లో సౌకర్యం కల్పిస్తుంది.

తరువాత, ఫంక్షన్/టూల్ కాలింగ్ విషయాన్ని మరింత విశదీకరించుకుందాం.

### ఫంక్షన్/టూల్ కాలింగ్

ఫంక్షన్ కాలింగ్ అనేది LLMలను టూల్స్‌తో పరస్పరం చేయించడానికి ప్రధాన మార్గం. మీరు ‘ఫంక్షన్’ మరియు ‘టూల్’ అన్న పదాలను అనేకసార్లు మార్పిడి భావంలో వాడినట్లే ఉంటారు ఎందుకంటే ‘ఫంక్షన్స్’ (మరల ఉపయోగించదగిన కోడ్ బ్లాక్స్) ఏజెంట్లు పనులను చేపట్టడానికి ఉపయోగించే ‘టూల్స్’ మాత్రమే. ఒక ఫంక్షన్ కోడ్ ను పిలవడానికి, LLM వాడుకరి అభ్యర్థనను ఫంక్షన్ వివరణతో సరిపోల్చాలి. అందుకోసం అందుబాటులో ఉన్న ఫంక్షన్ల వివరాలతో కూడిన ఒక స్కీమాను LLMకు పంపిస్తారు. LLM ఆ పనికి సరైన ఫంక్షన్ ఎంచుకొని దాని పేరు మరియు ఆర్గ్యుమెంట్లను తిరిగి ఇస్తుంది. ఆ ఎంపికైన ఫంక్షన్ అమలు చేయబడుతుంది, దాని స్పందన LLMకి తిరిగి పంపబడుతుంది, LLM ఆ సమాచారంతో వాడుకరి అభ్యర్థనకు సమాధానం ఇస్తుంది.

డెవలపర్లు ఏజెంట్లకు ఫంక్షన్ కాలింగ్ అమలు చేయాలంటే, ఈవి అవసరం:

1. ఫంక్షన్ కాలింగ్‌ని మద్దతిచ్చే LLM మోడల్
2. ఫంక్షన్ వివరణలతో కూడిన స్కీమా
3. ప్రతి ఫంక్షన్ యొక్క అమలుకోడ్

ప్రస్తుతం ఒక నగరంలో ప్రస్తుతం సమయం తెలుసుకోవటానికి ఉదాహరణ:

1. **ఫంక్షన్ కాలింగ్ మద్దతు ఇచ్చే LLM ప్రారంభం చేయండి:**

   అన్ని మోడల్స్ ఫంక్షన్ కాలింగ్ మద్దతు ఇవ్వవు, కాబట్టి మీరు ఉపయోగిస్తున్న LLM దీన్ని మద్దతు ఇవ్వడాన్ని నిర్ధారించాలి.  <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ఫంక్షన్ కాలింగ్ మద్దతు ఇస్తుంది. మేము Azure OpenAI క్లయింట్‌ను ప్రారంభించవచ్చు.

    ```python
    # Azure OpenAI క్లయింట్‌ను ఆරంభించండి
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **ఫంక్షన్ స్కీమా సృష్టించండి**:

   తరువాత, మేము ఫంక్షన్ పేరు, దాని ఉపయోగం, ఫంక్షన్ పారామితుల పేర్లు మరియు వివరణలతో కూడిన JSON స్కీమా నిర్వచిస్తాము. ఆ స్కీమాను మునుపటి క్లయింట్‌కు పంపించి, సాన్ ఫ్రాన్సిస్కోలో సమయం తెలుసుకోవడానికి వాడుకరి అభ్యర్థనతో కలిసి అందజేస్తాము. ముఖ్యంగా గమనించవలసింది ఏమంటే **టూల్ కాల్** తిరిగి వస్తుంది, ఇది ప్రశ్నకు తుది సమాధానం కాదు. LLM ఆ పనికి ఎంచుకున్న ఫంక్షన్ పేరు మరియు ఆర్గ్యుమెంట్లను ఇస్తుంది.

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
  
1. **పనిని చేయడానికి అవసరమైన ఫంక్షన్ కోడ్:**

   ఇప్పుడు LLM ఎంచుకున్న ఫంక్షన్ అమలుకు, ఆ కోడ్ రాయడం మరియు అమలు చేయడం అవసరం. కరెంట్టైమ్ పొందటానికి Python లో కోడ్ రాయవచ్చు. ఫలితాన్ని పొందేందుకు response_message నుండి పేరు మరియు ఆర్గ్యుమెంట్లను ఎలా తీసుకోవాలో కూడా కోడ్ రాయాలి.

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
     # ఫంక్షన్ కాల్లను నిర్వహించండి
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
  
      # రెండవ API కాల్: మోడల్ నుండి తుది స్పందనను పొందండి
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

ఫంక్షన్ కాలింగ్ పెద్ద ఎత్తున ఏజెంట్ టూల్ వినియోగ డిజైన్ హృదయం, కానీ ప్రారంభంలో దీనిని అమలు చేయడం కొన్నిసార్లు కష్టం అవుతుంది.
[Lesson 2](../../../02-explore-agentic-frameworks) లో నేర్చుకున్నట్టు ఏజెంటిక్ ఫ్రేమ్‌వర్క్లు టూల్ వినియోగాన్ని అమలు చేయడానికి ముందుగా సిద్ధం చేసిన నిర్మాణ భాగాలు అందిస్తాయి.

## ఏజెంటిక్ ఫ్రేమ్‌వర్క్లతో టూల్ వినియోగ ఉదాహరణలు

ఇక్కడ వివిధ ఏజెంటిక్ ఫ్రేమ్‌వర్క్లు ఉపయోగించి టూల్ వినియోగ డిజైన్ నమూనాని ఎలా అమలు చేయవచ్చో కొన్ని ఉదాహరణలు:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> AI ఏజెంట్లను నిర్మించడానికి ఓపెన్ సోర్స్ ఫ్రేమ్‌వర్క్. ఇది ఫంక్షన్ కాలింగ్ ప్రక్రియను సులభతరం చేస్తుంది, Python ఫంక్షన్స్ గా `@tool` డెకరేటర్ తో టూల్స్ నిర్వచించేందుకు అనుమతిస్తుంది. ఫ్రేమ్‌వర్క్ మోడల్ మరియు మీ కోడ్ మధ్య వెళ్లి వస్తూ కమ్యూనికేషన్ ని నిర్వహిస్తుంది. ఇది `AzureAIProjectAgentProvider` ద్వారా ముందుగా సృష్టించిన టూల్స్ (ఫైల్ సెర్చ్, కోడ్ ఇంటర్ప్రెటర్) అందజేస్తుంది.

కింది చిత్రణ Microsoft Agent Framework లో ఫంక్షన్ కాలింగ్ ప్రక్రియను వివరిస్తుంది:

![function calling](../../../translated_images/te/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework లో టూల్స్ డెకరేటెడ్ ఫంక్షన్స్ గా నిర్వచిస్తారు. ఇంతముందు చూశాం `get_current_time` ఫంక్షన్‌ని `@tool` డెకరేటర్ ఉపయోగించి టూల్ గా మార్చవచ్చు. ఫ్రేమ్‌వర్క్ ఆటోమేటిగ్గా ఆ ఫంక్షన్ మరియు దాని పారామితుల సిరియలైజేషన్ చేసి, LLM కి పంపే స్కీమాను సృష్టిస్తుంది.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# క్లయింట్‌ను సృష్టించండి
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ఏజెంట్‌ను సృష్టించండి మరియు టూల్‌తో రన్ చేయండి
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> ఒక తాజాగా అభివృద్ధి చేసిన ఏజెంటిక్ ఫ్రేమ్‌వర్క్. ఇది డెవలపర్లకు ఆధునిక, విస్తరణ సులభమైన AI ఏజెంట్లు సురక్షితంగా నిర్మించి, పంపిణీ చేసి, స్కేల్ చేసుకునే సామర్ధ్యాన్ని ఇస్తుంది, క్రిందిల ప్రక్రియల నిర్వహణ లేకుండానే. ఇది నిర్ధిష్టంగా ఎంటర్ప్రైజ్ అప్లికేషన్లకే ఉపయోగకరం ఎందుకంటే ఇది enterprise-grade securityతో పూర్తి నియంత్రణ సేవ.

LLM APIతో నేరుగా అభివృద్ధి చేసుకునేందుకు స్థానంలో, Azure AI Agent Service కొన్ని ప్రయోజనాలు కల్పిస్తుంది, అందులో:

- ఆటోమేటిక్ టూల్ కాలింగ్ – టూల్ కాల్ విశ్లేషించడానికి, టూల్ ని పిలవడానికి, ఆ తర్వాత సమాధానం నిర్వహించడానికి అవశ్యం లేదు; ఇవన్నీ ఇప్పుడు సర్వర్ పక్కనే చేయబడతాయి
- సురక్షితంగా నిర్వహించబడిన డేటా – మీ స్వంత సంభాషణ స్థితి నిర్వహించడానికి కాకుండా, కావలసిన సమాచారాన్ని నిల్వ చేయడానికి threads పైన ఆధారపడవచ్చు
- తయారుచేసిన టూల్స్ – Bing, Azure AI Search, Azure Functions వంటి డేటా మూలాలతో పరస్పరం చేసేందుకు టూల్స్ అందుబాటులో ఉన్నాయి.

Azure AI Agent Service లో అందుబాటులో ఉన్న టూల్స్ ఈ రెండుభాగాలుగా విభజించబడతాయి:

1. జ్ఞాన టూల్స్:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search తో గ్రౌండింగ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">ఫైల్ సెర్చ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. చర్య టూల్స్:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">ఫంక్షన్ కాలింగ్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">కోడ్ ఇంటర్ప్రెటర్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI నిర్వచించిన టూల్స్</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ఈ టూల్స్ ను `toolset` గా కలిపి ఉపయోగించేందుకు అనుమతిస్తుంది. ఇది నిర్దిష్ట సంభాషణకు సంబంధించి సందేశాల చరిత్రను ట్రాక్ చేసే `threads` ను కూడా ఉపయోగిస్తుంది.

నీవు Contoso అనే సంస్థలో ఒక సేల్స్ ఏజెంట్ అనే ఊహించుకో. మీరు మీ సేల్స్ డేటాపై ప్రశ్నలకు సమాధానం ఇచ్చే సంభాషణాత్మక ఏజెంటును అభివృద్ధి చేయాలనుకుంటున్నారు.

కింది చిత్రం Azure AI Agent Service ఉపయోగించి సేల్స్ డేటా విశ్లేషణ ఎలా చేయచ్చో చూపిస్తుంది:

![Agentic Service In Action](../../../translated_images/te/agent-service-in-action.34fb465c9a84659e.webp)

సర్వీస్ తో ఏ టూల్ ఉపయోగించాలంటే, మేము క్లయింట్ సృష్టించి టూల్ లేదా టూల్ సెట్ నిర్వచించవచ్చు. దాన్ని ప్రాక్టికల్ గా అమలు చేయడానికి ఈ క్రింది Python కోడ్ గమనించండి. LLM టూల్ సెట్ పైన చూడగలదు, వాడుకరి అభ్యర్థనకు తగినట్టు `fetch_sales_data_using_sqlite_query` అనే వినియోగదారు సృష్టించిన ఫంక్షన్ లేదా ముందు నుంచే తయారైన కోడ్ ఇంటర్ప్రెటర్ ను ఎంపిక చేసుకునేది.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query ఫంక్షన్, ఇది fetch_sales_data_functions.py ఫైల్‌లో కనిపిస్తుంది.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# టూల్‌సెట్‌ను ప్రారంభించండి
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query ఫంక్షన్‌తో ఫంక్షన్ కాలింగ్ ఏజెంట్‌ను ప్రారంభించి, దానిని టూల్‌సెట్‌లోకి జతపరచండి
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# కోడ్ ఇంటర్‌ప్రెటర్ టూల్‌ను ప్రారంభించి దానిని టూల్‌సెట్‌లోకి జతపరచండి.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## నమ్మదగిన AI ఏజెంట్లు నిర్మించడంలో టూల్ వినియోగ డిజైన్ నమూనా ఉపయోగించే ప్రత్యేక విషయాలు ఏమిటి?

LLMs ద్వారా డైనమిక్ గా రూపొందించబడే SQL విషయంలో సాధారణమైన భయం భద్రత, ముఖ్యంగా SQL ఇంజెక్షన్ లేదా దుర్బాచక అక్షమ చర్యలు (ఉదా: డేటాబేస్‌ను విసర్జించడం లేదా తప్పుడు మార్పులు చేయడం) పై ఉంటాయి. ఈ ఆందోళనలు సమర్థవంతంగా తగ్గించుకోవచ్చు డేటాబేస్ యాక్సెస్ అనుమతులను సరైన రీతిలో అమర్చిఉండటం ద్వారా. చాలా డేటాబేసులకీ ఇది చదవే మోడ్ గా కట్టుబడటం అవసరం. PostgreSQL లేదా Azure SQL లాంటి డేటాబేస్ సర్వీసుల్లో యాప్‌కు రీడ్-ఓన్లీ (SELECT) పాత్ర ఇవ్వడం ముఖ్యం.

యాప్‌ను భద్రంగా నిర్వహించే వాతావరణంలో నడపటం రక్షణను మరింత బలోపేతం చేస్తుంది. ఎంటర్ప్రైజ్ సందర్భాల్లో, డేటా సాధారణంగా ఆపరేషనల్ సిస్టమ్స్ నుండి, వినియోగదారుకు సౌకర్యవంతమైన స్కీమాతో, రీడ్-ఓన్లీ డేటాబేస్ లేదా డేటా గిడ్డంగి లోకి తీసుకురాబడుతుంది. ఇది డేటా భద్రతా, పనితీరు మరియు ప్రాప్యతకు అనుకూలంగా ఉంటుందని, యాప్ కు పరిమిత, చదవే యాక్సెస్ ఉండటం నిర్ధారిస్తుంది.

## నమూనా కోడ్స్

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## టూల్ వినియోగ డిజైన్ నమూనాల గురించి మరిన్ని ప్రశ్నలు ఉన్నారా?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) లో చేరండి, ఇలాంటి ఇతర నేర్చుకునే వారికి కలుసుకుని, ఆఫీస్ గంటలలో పాల్గొని మీ AI ఏజెంట్ల ప్రశ్నలకు సమాధానాలు పొందండి.

## అదనపు వనరులు

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service వర్క్‌షాప్</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer బహుళ ఏజెంట్ వర్క్‌షాప్</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework అవలోకనం</a>

## గత పాఠం

[Agentic Design Patterns అర్థం చేసుకోవడం](../03-agentic-design-patterns/README.md)

## తదుసరమైన పాఠం
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**హుటాహమా**:  
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ద్వారా అనువదించబడింది. మేము సరిదిద్దే ప్రయత్నం చేస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చును. మూల పత్రం భాషలోనే అధికారిక మూలంగా పరిగణించబడాలి. ముఖ్యమైన సమాచారానికి ప్రొఫెషనల్ మానవ అనువాదం 권장ించబడును. ఈ అనువాదం వలన కలిగే ఏవిధమైన అపార్థాలు లేదా తప్పుదెబ్బలకు మేము బాధ్యులు కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->