[![How to Design Good AI Agents](../../../translated_images/ta/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(மேலுள்ள படத்தை கிளிக் செய்து இந்த பாடத்தின் வீடியோவை பார்வையிடவும்)_

# கருவி பயன்பாட்டுக் வடிவமைப்பு Pattern

கருவிகள் சுவாரசியமானவை, ஏனெனில் அவை AI எஜெண்ட்களுக்கு பரபரப்பான திறன்களை வழங்குகின்றன. எஜெண்ட் செய்யக்கூடிய படிகமான செயல் வரம்பை விட, ஒரு கருவியைச் சேர்ப்பதன் மூலம், எஜெண்ட் பலவகை செயல்களை செய்ய முடியும். இந்த அத்தியாயத்தில், AI எஜெண்ட்கள் தங்கள் குறிக்கோள்களை அடைய குறிப்பிட்ட கருவிகளை எவ்வாறு பயன்படுத்த முடியும் என்பதைக் கூறும் கருவி பயன்பாடு வடிவமைப்பு Pattern ஐப் பார்க்கப்போகிறோம்.

## அறிமுகம்

இந்த பாடத்தில், கீழ்கண்ட கேள்விகளுக்கு பதிலளிப்பதே நோக்கம்:

- கருவி பயன்பாட்டு வடிவமைப்பு Pattern என்றால் என்ன?
- எந்த பயன்பாடுகளில் இது பாவிக்கப்படலாம்?
- இந்த வடிவமைப்பு Pattern உடன் செயல்படுத்த தேவையான கூறுகள்/கட்டமைப்புகள் என்ன?
- நம்பகத்தன்மை வாய்ந்த AI எஜெண்ட்களை உருவாக்க கருவி பயன்பாடு Design Pattern பயன்படுத்தும்போது கவனிக்க வேண்டிய விசேஷங்கள் என்ன?

## கற்றல் இலக்குகள்

இந்த பாடத்தை முடித்த பிறகு, நீங்கள்:

- கருவி பயன்பாடு Design Pattern மற்றும் அதன் நோக்கத்தை வரையறுக்க முடியும்.
- இந்த Design Pattern பாவிக்கக்கூடிய பயன்பாடுகளை அடையாளம் காண முடியும்.
- வடிவமைப்பை செயல்படுத்த தேவையான முக்கிய கூறுகளை புரிந்துகொள்ள முடியும்.
- இந்த வடிவமைப்பைப் பயன்படுத்தும் AI எஜெண்ட்களில் நம்பகத்தன்மையை உறுதிசெய்யும் கவனிக்க வேண்டிய அம்சங்களை அறிந்து கொள்வீர்கள்.

## கருவி பயன்பாட்டு வடிவமைப்பு Pattern என்பது?

**கருவி பயன்பாட்டு வடிவமைப்பு Pattern** LLM களை குறிப்பிட்ட குறிக்கோள்களை அடைவதற்கு வெளிப்புற கருவிகளுடன் தொடர்பு கொள்ளும் திறனை வழங்கும். கருவிகள் என்பது ஒரு எஜெண்ட் செயல்களை மேற்கொள்ள செயல்படுத்தக்கூடிய கோட் ஆகும். ஒரு கருவி எளிய function ஆக இருக்கலாம், எடுத்துக்காட்டாக கணக்கிடும் இயந்திரம், அல்லது பங்கு விலை தேடல் அல்லது வானிலை முன்னறிக்கையைப் பெறும் third-party சேவைக்கு API அழைப்பு ஆக இருக்கலாம். AI எஜெண்ட்களின் சூழலில், கருவிகள் **மாதிரி-உருவாக்கிய function அழைப்புகளுக்கு பதிலளித்து** எஜெண்ட்களால் செயல்பட வடிவமைக்கப்படுகின்றன.

## இது எந்த பயன்பாடுகளில் பாவிக்கப்படலாம்?

AI எஜெண்ட்கள் கருவிகளை பயன்படுத்தி சிக்கலான பணிகளை முடிக்க, தகவல்களை பெற, அல்லது முடிவுகளை எடுக்க முடியும். கருவி பயன்பாடு வடிவமைப்பு Pattern பெரும்பாலும் வெளியீட்டு அமைப்புகளுடன் டைனமிக் தொடர்புகொள்ள வேண்டிய சூழலில் பயன்படுகிறது, எடுத்துக்காட்டாக தரவுத்தளம், வலை சேவைகள் அல்லது கோடுகளைப் புரிந்துகொள்ளும் நிரலர்கள். இதன் திறன் பலவகை பயன்பாடுகளுக்கு பயனுள்ளதாக இருக்கிறது:

- **டைனமிக் தகவல் பெறல்:** எஜெண்ட்கள் வெளியீட்டு API கள் அல்லது தரவுத்தளங்களை கேட்டு சமீபத்திய தரவை பெறலாம் (எ.கா., SQLite தரவுத்தளத்தில் தரவு பகுப்பாய்வு செய்ய, பங்கு விலை அல்லது வானிலை தகவல் பெற).
- **கோட் செயல்படுத்தல் மற்றும் விளக்கம்:** எஜெண்ட்கள் கணிதப் பிரச்சனைகள் தீர்க்க, அறிக்கைகள் உருவாக்க, அல்லது சிமுலேஷன்களைச் செய்ய கோட் அல்லது ஸ்கிரிப்ட்களை செய்ய இயலும்.
- **வேலைவழி தானியக்கம்:** பணிகள் அல்லது பல படிகள் கொண்ட வேலைவழிகளை தானியக்கமாக்க, பணிப் பகிரல்கூட்டிகள், மின்னஞ்சல் சேவைகள், அல்லது தரவு பைப்லைன்கள் போன்ற கருவிகளை இணைக்கும்.
- **வாடிக்கையாளர் உதவி:** எஜெண்ட்கள் CRM அமைப்புகள், டிக்கெட் சுற்றுச்சூழல்கள், அல்லது அறிவுத்தளம் மூலம் பயனர் கேள்விகளை தீர்க்கலாம்.
- **உள்ளடக் கட்டமைப்பு மற்றும் திருத்தம்:** எஜெண்ட்கள் குற்றச்சாட்டு சரிபார்ப்பாளர்கள், உரை சுருக்கிகள், அல்லது உள்ளடக் பாதுகாப்பு மதிப்பாய்வாளர் போன்ற கருவிகளை பயன்படுத்தி உள்ளடக்க உருவாக்க உதவல்.

## கருவி பயன்பாடு Design Pattern செயல்படுத்த தேவையான கூறுகள்/கட்டமைப்புகள் என்ன?

இந்த கட்டமைப்புகள் AI எஜெண்டுக்கு பரபரப்பான பணிகளை செய்வதற்கு வேண்டிய ஆதாரங்கள். கருவி பயன்பாட்டு Design Pattern செயல்படுத்த தேவையான முக்கிய கூறுகள்:

- **Function/Tool திட்டங்கள்**: கிடைக்கும் கருவிகளின் விரிவான வரைவுகள், அதில் function பெயர், நோக்கு, தேவையான அளவுருக்கள் மற்றும் எதிர்பார்க்கப்படும் வெளியீடுகள். இந்த திட்டங்கள் LLM க்கு கிடைக்கும் கருவிகளைக் புரிந்து கொண்டு சரியான வேண்டுகோள்களை உருவாக்க உதவுகின்றன.

- **Function செயல்படுத்தும் விதிகள்**: பயனர் நோக்கம் மற்றும் உரையாடல் சூழலைப் பொருத்து எந்த நேரத்தில் கருவி அழைக்கப்படவேண்டும் என்பதைக் கையாள்கிறது. இதில் திட்டமிடல் முறைகள், வழிப் பாய்வு முறைகள் அல்லது நிபந்தனை அடிப்படையிலான வழிகள் அடங்கலாம்.

- **செய்தி கையாளும் அமைப்பு**: பயனர் உள்ளீடுகள், LLM பதில்கள், கருவி அழைப்புகள் மற்றும் கருவி வெளியீடுகள் இடையேயான உரையாடல் ஓட்டத்தை நிர்வகிக்கும் கூறுகள்.

- **கருவி ஒருங்கிணைப்பு சட்டமேல் தொகுப்பு**: எஜெண்டை பல கருவிகளுடன், எளிய function கள் ஆக இருந்தாலும், கிளப்பி பெரிய வெளிப்புற சேவைகள் ஆக இருந்தாலும் இணைக்கும் கட்டமைப்பு.

- **பிழை கையாளும் மற்றும் சரிபார்ப்பு**: கருவி செயல்பாட்டில் தோல்விகளை கையாள, அளவுருக்கள் சரிபார்க்க, எதிர்பாராத பதில்களை நிர்வகிக்க பயன்படும் முறைகள்.

- **அமைப்பு மேலாண்மை**: உரையாடல் சூழல், முந்தைய கருவி தொடர்புகள் மற்றும் நீடித்த தரவுகளை கண்காணித்து, பல சுற்றுக்களுக்குள் பொருந்துதலை உறுதிசெய்கிறது.

அடுத்து, Function/Tool அழைப்பைப் விரிவாக பார்க்கலாம்.

### Function/Tool அழைப்புகள்

Function அழைப்பு என்பது Large Language Models (LLMs) கருவிகளுடன் தொடர்புகொள்ள முதன்மையான முறை. பொதுவாக 'Function' மற்றும் 'Tool' என்றவை பரிமாறி பயன்படுத்தப்படுகின்றன, ஏனெனில் 'functions' (மறு பயன்பாட்டுக்கான கோட் தொகுதிகள்) என்பது எஜெண்ட்கள் பணிகள் செய்ய பயன்படும் 'tools' ஆகும். ஒரு function கோடு அழைக்கப்பட வேண்டுமானால், LLM பயனர் கோரிக்கையை அந்த function விளக்கத்துடன் ஒப்பிட வேண்டும். அதற்கு கிடைக்கும் அனைத்து functions விளக்கங்களைக் கொண்ட ஒரு திட்டத்தை LLM க்கு அனுப்ப வேண்டும். LLM அவற்றுள் மிக பொருத்தமான function ஐ தேர்ந்தெடுத்து அதன் பெயர் மற்றும் அளவுருக்களை திருப்பி விடும். தேர்ந்தெடுக்கப்பட்ட function அழைக்கப்படுகிறது, பதில் LLM க்கு செல்லும், பின்னர் அது பயனர் கோரிக்கைக்கு பதிலளிக்க தகவலைப் பயன்படுத்தும்.

எஜெண்ட்கள் Function அழைப்பை செயல்படுத்த, நீங்கள் தேவையென்பவை:

1. Function அழைப்பை ஆதரிக்கும் LLM மாதிரி
2. Function விளக்கங்கள் கொண்ட திட்டம்
3. ஒவ்வொரு function என்பதும் செயல்முறைக்கான கோட்

ஒரு நகரின் தற்போதைய நேரத்தைப் பெறும் உதாரணத்தைப் பயன்படுத்தி விளக்குகிறோம்:

1. **Function அழைப்பை ஆதரிக்கும் LLM ஐ துவக்கவும்:**

    எல்லா மாதிரிகளும் Function அழைப்பை ஆதரிக்காது, எனவே நீங்கள் பயன்படுத்தும் LLM இதை ஆதரிக்கிறதா என்பதை உறுதி செய்ய வேண்டும். <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> Function அழைப்பை ஆதரிக்கிறது. Azure OpenAI கிளையண்டை துவக்கம் செய்துக்கொள்ள முடியும்.

    ```python
    # Azure OpenAI க்ளையன்ட்டை ஆரம்பிக்கவும்
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Function திட்டத்தை உருவாக்குக**:

    அடுத்ததாக, function பெயர், அதன் செயலில் விளக்கம் மற்றும் function அளவுருக்கள் பெயர் மற்றும் விளக்கங்கள் உள்ள JSON திட்டத்தை வரையறுக்கிறோம்.
    இந்த திட்டத்தை முன்பு உருவாக்கிய கிளையண்டுக்கு மற்றும் பயனர் கோரிக்கையை, உதாரணமாக San Francisco நேரம் பெற உத்தரவிடுவோம்.
    முக்கியமாக கருத வேண்டியது என்னவென்றால் **கருவி அழைப்பு** மட்டுமே திருப்பப்படுகிறது, கேள்வியின் இறுதி பதில் அல்ல.
    LLM தேர்ந்தெடுத்த function பெயர் மற்றும் அதன் அளவுருக்கள் திருப்பும் என முன் கூறப்பட்டதுபோல்.

    ```python
    # படிக்க மாதிரிக்கு செயல்பாட்டு விளக்கம்
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
  
    # ஆரம்ப பயனர் செய்தி
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # முதல் API அழைப்பு: மாதிரியை செயல்பாட்டைப் பயன்படுத்த கேளுங்கள்
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # மாதிரியின் பதிலை செயலாக்கு
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **பணியை நிறைவேற்ற தேவையான function கோட்:**

    LLM தேர்வு செய்த function இப்போது செயல்படுத்தப்பட வேண்டும்.
    Python-ல் தற்போதைய நேரத்தைப் பெறுவதற்கான கோட்டை உருவாக்கலாம்.
    பதில் செய்தியிலிருந்து பெயர் மற்றும் அளவுருக்களை எடுத்து இறுதி முடிவை பெறுமாறு கோட் எழுத வேண்டும்.

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
     # செயல்பாட்டு அழைப்புகளை கையாளவும்
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
  
      # இரண்டாவது API அழைப்பு: மாதிரியில் இருந்து இறுதி பதிலை பெற்றுகொள்ளவும்
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

Function Calling என்பது பெரும்பாலும், இல்லையெனில் அனைத்து எஜெண்ட் கருவி பயன்பாட்டுக் வடிவமைப்புகளின் மையம் ஆகும், ஆனால் அதை பூஜ்ஜியமாக உருவாக்குவது சில நேரங்களில் சிரமமாக இருக்கலாம்.
[Lesson 2](../../../02-explore-agentic-frameworks) இல் கற்றதுபோல், எஜெண்ட் சட்டமேல் தொகுப்புகள் கருவி பயன்பாட்டைக் கையாளுவதற்கான முன் தயாரிக்கப்பட்ட கட்டமைப்புகளை வழங்குகின்றன.

## Agentic Frameworks உடன் கருவி பயன்பாட்டு உதாரணங்கள்

வேறுபட்ட எஜெண்ட் சட்டமேல் தொகுப்புகளை பயன்படுத்தி கருவி பயன்பாடு Design Pattern இப்படி செயல்படுத்தலாம்:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> என்பது AI எஜெண்ட்கள் உருவாக்கும் திறனைக் கொடுக்கும் ஓப்பன்-சோர்ஸ் AI சட்டமேல் தொகுப்பு. இது function அழைப்பை எளிமையாக்கி, Python functions ஐ `@tool` அலங்காரச்சொல்லுடன் வரையறுக்க அனுமதிக்கிறது. மாதிரி மற்றும் உங்கள் கோட்டின் இடையேயான தொடர்பினை சட்டமேல் கையாளும். மேலும், `AzureAIProjectAgentProvider` வாயிலாக File Search மற்றும் Code Interpreter போன்ற முன் தயாரிக்கப்பட்ட கருவிகளையும் அணுகலாம்.

Microsoft Agent Framework உடன் Function calling செயல்முறை இதுபோல இருக்கிறது:

![function calling](../../../translated_images/ta/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework இல், கருவிகள் அலங்காரம் செய்யப்பட்ட functions ஆக வரையறுக்கப்படுகின்றன. முன்பு பார்த்த `get_current_time` function ஐ `@tool` அலங்காரச்சொல்லுடன் கருவியாக மாற்றலாம். சட்டமேல் function மற்றும் அதன் அளவுருக்களை தானாகவே உருமாற்றி, LLM க்குப் கிடைக்கும் திட்டத்தை உருவாக்கும்.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# கிளையண்டை உருவாக்கவும்
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# ஒரு முகவரியை உருவாக்கி கருவியுடன் இயக்கவும்
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> என்பது புதிதாக வரும் எஜெண்ட் சட்டமேல் தொகுப்பு. இது டெவலப்பர்களுக்கு நிலையான கணினி மற்றும் சேமிப்பு வளங்களை நிர்வகிக்காவிட்டாலும், பாதுகாப்பாக உயர்தர மற்றும் விரிவாக்கமுடியுமாய்ச் AI எஜெண்ட்கள் உருவாக்க, பிரயோகிப்பதில் உதவுகிறது. இது, குறிப்பாக நிறுவன பயன்பாடுகளுக்கு ஏற்ற ஒருங்கிணைந்த, பாதுகாப்பான முழுமையான சேவையாகும்.

LLM API உடன் நேரடியாக உருவாக்குவதும் Azure AI Agent சேவையைப்போல் பார்க்கும்போது, கீழ்காணும் நன்மைகள் உள்ளன:

- தானாகவே கருவி அழைக்கப்படுகிறது – கருவி அழைப்பைப் பகுப்பாய்வு செய்து, கருவியை அழைத்து பதிலை கையாள வேண்டியதில்லை; இது எல்லாம் சர்வர் பக்கத்தில் சாத்தியமாகிறது
- பாதுகாப்பாக நிர்வகிக்கப்பட்ட தரவு – உங்கள் உரையாடல் நிலையைத் தனி முறையில் நிர்வகிக்காமல், threads இல் அனைத்துத் தகவல்களும் சேமிக்கப்படும்
- உடனடி கருவிகள் – Bing, Azure AI Search, மற்றும் Azure Functions போன்ற தரவுத்தளங்களுடன் தொடர்பு கொள்ள பயன்படும் கருவிகள்.

Azure AI Agent சேவையில் கிடைக்கும் கருவிகள் இரண்டு வகையாக பிரிக்கப்படுகின்றன:

1. அறிவியல் கருவிகள்:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Search உடன் தகவல் அடிப்படைவதை</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">கோப்பு தேடல்</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. செயல் கருவிகள்:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function அழைப்பு</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">கோட் Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI வரையறுக்கப்பட்ட கருவிகள்</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service இல் இந்த கருவிகளை `toolset` ஆக பயன்படுத்த முடியும். மேலும், குறிப்பிட்ட உரையாடலின் செய்தி வரலாறு இனைப்பதாக `threads` ஐ பயன்படுத்துகிறது.

நீங்கள் “Contoso” என்ற நிறுவனத்தில் விற்பனை எஜெண்ட் ஆக இருக்கிறீர்கள் என்று கனவுகாணுங்கள். உங்கள் விற்பனை தரவுகள் தொடர்பான கேள்விகளுக்கு பதிலளிக்கும் உரையாடல் எஜெண்டை உருவாக்க விரும்புகிறீர்கள்.

Azure AI Agent Service உபயோகித்து உங்கள் விற்பனை தரவுகளைப் பகுப்பாய்வு செய்வதை இந்த படம் விளக்குகிறது:

![Agentic Service In Action](../../../translated_images/ta/agent-service-in-action.34fb465c9a84659e.webp)

இந்த சேவையுடன் எந்த ஒரு கருவியையும் பயன்படுத்த, நாம் கிளையண்ட் உருவாக்கி கருவி அல்லது கருவிப் தொகுப்பை வரையறுக்கலாம். இதில் பயனர் உருவாக்கிய `fetch_sales_data_using_sqlite_query` function அல்லது முன் தயாரிக்கப்பட்ட Code Interpreter உடன் LLM கருவி தொகுப்பைக் கண்டு பயன்படுத்த முடியும்.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query என்ற செயல்பாடு fetch_sales_data_functions.py கோப்பில் காணப்படலாம்.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# கருவி தொகுப்பை ஆரம்பிப்பது
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query செயல்பாட்டுடன் மற்றும் அதை கருவி தொகுப்பில் சேர்த்துக் கொண்டு function calling agent ஐ ஆரம்பித்தல்
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Code Interpreter கருவியைக் INIT செய்து அதை கருவி தொகுப்பில் சேர்த்தல்.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## நம்பகத்தன்மை வாய்ந்த AI எஜெண்ட்களை உருவாக்க கருவி பயன்பாடு Design Pattern பயன்படுத்தும் போது கவனிக்க வேண்டிய விசேஷங்கள்?

LLM-கள் உருவாக்கும் SQL-வைப் பற்றிய பொதுவான கவலைவாக பாதுகாப்பு உள்ளது, குறிப்பாக SQL injection அல்லது தீங்கான செயல்கள் (தரவுத்தளத்தை drop செய்வது அல்லது மாற்றுவது போன்ற) காரணமாக. இத்தகைய கவலைகள் உண்மையானவை, ஆனால் தரவுத்தள அணுகல் அனுமதிகளை சரியாக கட்டமைத்தால் மிகுந்த பாதுகாப்பு ஏற்படுகிறது. பெரும்பாலான தரவுத்தளங்களில், தரவுத்தளம் படிக்க மட்டுமே அனுமதிக்கப்பட வேண்டும். PostgreSQL அல்லது Azure SQL போன்ற சேவைகளுக்கு, செயலிக்கு read-only (SELECT) பங்கு ஒதுக்கப்படும்.

செயலியை பாதுகாப்பான சூழலில் ஓட்டுவது அமைச்சர் பாதுகாப்பை மேம்படுத்தும். நிறுவன சூழல்களில், தரவு பொதுவாக இயங்கும் அமைப்புகளிலிருந்து படித்து மாற்றப்பட்டு படிக்க மட்டும் அனுமதிக்கப்படும் தரவுத்தளமாக மாற்றப்படும். இது தரவின் பாதுகாப்பையும், செயல்திறனையும், மற்றும் பயன்பாட்டின் கட்டுப்பட்ட படிக்கவேண்டிய அணுகலை உறுதிசெய்கிறது.

## மாதிரி குறியீடுகள்

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## கருவி பயன்பாட்டு வடிவமைப்புகளைக் குறித்து மேலதிக கேள்விகள் உள்ளதா?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) இல் சேர்ந்து மற்ற கற்றுதலாளர்களை சந்தித்து, அலுவலக நேரங்களில் பங்கேற்று, உங்கள் AI எஜெண்ட்கள் தொடர்பான கேள்விகளுக்கு பதில் பெறுங்கள்.

## கூடுதல் வளங்கள்

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service செய்முறைப் பயிற்சி</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer மது-எஜெண்ட் வேலைப்பாடு</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework மேற்சொல்லல்</a>

## முந்தைய பாடம்

[Agentic Design Patterns புரிதல்](../03-agentic-design-patterns/README.md)

## அடுத்து வரவிருக்கும் பாடம்
[ஏஜென்டிக் RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவையான [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சித்தாலும், தானாக செய்யப்பட்ட மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் உள்ளூர் மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பின் பயன்பாட்டிலிருந்து ஏற்படும் எந்தத் தவறுகளுக்கும் நாங்கள் பொறுப்பேற்கமாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->