# மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்பை ஆராய்தல்

![Agent Framework](../../../translated_images/ta/lesson-14-thumbnail.90df0065b9d234ee.webp)

### அறிமுகம்

இந்த பாடத்தில் பின்வருவன கையாளப்படுகின்றன:

- மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்பை புரிந்துக் கொள்ளுதல்: முக்கிய அம்சங்கள் மற்றும் மதிப்பு  
- மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்பின் முக்கிய கருத்துக்களை ஆராய்தல்
- மேம்பட்ட MAF முன்ன்மாதிரிகள்: வேலைபட்டிகள், மிடில் வேர் மற்றும் நினைவு

## கற்றல் இலக்குகள்

இந்த பாடத்தை முடித்த பிறகு நீங்கள் முடியும்:

- மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்பை பயன்படுத்தி தயாரிப்புக்கு தயாரான AI ஏஜெண்டுகளை கட்டமைக்க
- உங்கள் ஏஜென்டிக் பயன்பாட்டுக்கேஸ் களுக்கு மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்பின் மைய அம்சங்களை பயன்படுத்த
- வேலைபட்டிகள், மிடில் வேர் மற்றும் கவனிப்புத்தன்மை போன்ற முன்ன்மாதிரிகளை பயன்படுத்த

## குறியீட்டுக்கான எடுத்துக்காட்டுகள்

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) க்கான குறியீட்டு எடுத்துக்காட்டுகள் இந்த நிரலகத்தில் `xx-python-agent-framework` மற்றும் `xx-dotnet-agent-framework` கோப்புகளின் கீழ் கிடைக்கின்றன.

## மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்பை புரிதல்

![Framework Intro](../../../translated_images/ta/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) என்பது AI ஏஜெண்டுகளை உருவாக்குவதற்கான மைக்ரோசாஃப்டின் ஒருங்கிணைந்த கட்டமைப்பாகும். இது தயாரிப்பு மற்றும் ஆராய்ச்சி சூழல்களில் காணப்படும் பல்வேறு ஏஜென்டிக் பயன்பாட்டுக்கேஸ்களை கையாள்வதற்கான நெகிழ்மையை வழங்குகிறது:

- **தொடர்ச்சியான ஏஜென்ட் ஒர்க்செஷன்** தேவையான படி படி வேலைபட்டிகள் உள்ள சூழல்களில்.
- **ஒரே நேரத்தில் ஒர்க்செஷன்** ஏஜென்ட்கள் ஒரே நேரத்தில் பணிகளை முடிக்க வேண்டிய சூழல்களில்.
- **குழு உரையாடல் ஒர்க்செஷன்** ஏஜென்ட்கள் ஒரே பணியில் சேர்ந்து வேலை செய்வதற்கான சூழல்களில்.
- **ஹேண்ட்ஆஃப் ஒர்க்செஷன்** துணைப் பணிகள் முடிந்தபோது ஏஜென்ட்கள் பணியை ஒருவரிடமிருந்து மற்றவருக்கு வைக்கின்ற சூழல்களில்.
- **மேக்னெட்டிக் ஒர்க்செஷன்** மேலாளர் ஏஜென்ட் பணியாளர்களை ஒழுங்கு செய்வதில் பொறுப்பேற்கும் பணியாளரின் பணிப் பட்டியலை உருவாக்கி மாற்றும் சூழலில்.

தயாரிப்பில் AI ஏஜென்டுகளை வழங்க, MAF அடுத்த அம்சங்களையும் கொண்டுள்ளது:

- **கவனிப்புத்தன்மை** OpenTelemetry ஐப் பயன்படுத்தி, AI ஏஜென்டின் ஒவ்வொரு நடவடிக்கையும் ஆக்டிவேஷன், ஒர்க்செஷன் படிகள், காரணமமைவு நடைமுறை மற்றும் Microsoft Foundry டாஷ்போர்ட்கள் மூலம் செயல்திறன் கட்டுப்பாடு ஆகியவற்றை கண்காணிக்கிறது.
- **பாதுகாப்பு** Microsoft Foundry இல் உள்ள ஏஜென்ட்கள் இயல்புநிலை பாதுகாப்பு கட்டுப்பாடுகள் கொண்டிருக்கின்றன, இதில் நாள் அடிப்படையிலான அணுகல், தனிப்பட்ட தரவு கையாளுதல் மற்றும் உள்ளடக்க பாதுகாப்பு உள்ளடங்கும்.
- **நிலைமை நிலைத்தன்மை** ஏஜென்ட் திரெட்கள் மற்றும் வேலைபட்டிகள் இடைநிறுத்த, மீண்டும் தொடக்கம் மற்றும் பிழைகள் இருந்து மீட்க முடியும், இது நீண்ட நேரம் இயங்கும் செயல்முறைக்கு உதவுகிறது.
- **கட்டுப்பாடு** மனித ஒப்புதலுடன் செயல்படும் வேலைபட்டிகள் ஆதரிக்கப்படுகின்றன, பணிகளை மனித ஒப்புதலை தேவைப்படுத்தி குறிக்கின்றன.

மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்பு இன்டர்ஓபரேபிளாகும் என்று கவனம் செலுத்துகிறது:

- **கிளவுட் கட்டுப்பாடு இல்லாதது** - ஏஜெண்டுகள் கன்டெயிநர்கள், உள்ளக மற்றும் பலவகை கிளவுட்களில் இயங்க முடியும்.
- **பிரொவைய்டர் கட்டுப்பாடு இல்லாதது** - Azure OpenAI மற்றும் OpenAI உள்ளிட்ட உங்கள் விருப்பமான SDK மூலம் ஏஜெண்டுகள் உருவாக்கப்படலாம்.
- **திறந்த தரநிலை ஒருங்கிணைப்பு** - Agent-to-Agent(A2A) மற்றும் Model Context Protocol (MCP) போன்ற நடைமுறைகள் மூலம் பிற ஏஜெண்டுகள் மற்றும் கருவிகளை கண்டறிய மற்றும் பயன்படுத்த முடியும்.
- **பிளக்கின்கள் மற்றும் கனெக்டார்கள்** - Microsoft Fabric, SharePoint, Pinecone மற்றும் Qdrant போன்ற தரவு மற்றும் நினைவு சேவைகளுடன் இணைக்க முடியும்.

இப்போது இந்த அம்சங்கள் Microsoft Agent Framework இன் சில முக்கிய கருத்துக்களில் எப்படி பயன்படுத்தப்படுகின்றன என்று பார்க்கலாம்.

## Microsoft Agent Framework இன் முக்கிய கருத்துக்கள்

### ஏஜெண்ட்கள்

![Agent Framework](../../../translated_images/ta/agent-components.410a06daf87b4fef.webp)

**ஏஜெண்ட்கள் உருவாக்குதல்**

ஏஜெண்ட் உருவாக்கம் வரைவான் சேவையை (LLM வழங்குநர்), ஒரு
AI ஏஜெண்ட் பின்பற்ற வேண்டிய கட்டளைகளின் தொகுதியாகவும், ஒதுக்கப்பட்ட `name` எனும் பெயராகவும் செய்யப்படுகிறது:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

மேலே `Azure OpenAI` பயன்படுத்தப்பட்டுள்ளது ஆனால் ஏஜெண்ட்கள் `Microsoft Foundry Agent Service` உட்பட பல்வேறு சேவைகள் பயன்படுத்தி உருவாக்கப்படலாம்:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

அல்லது [MiniMax](https://platform.minimaxi.com/) பயன்படுத்தலாம், இது பெரிய கான்டெக்ஸ்ட் விண்டோக்களுடன் (204K பார்சல்கள் வரை) OpenAI-ஐப் பொருந்தும் API வழங்குகிறது:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

அல்லது A2A நடைமுறையை பயன்படுத்தி தொலைநிலையேயான ஏஜெண்டுகள்:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ஏஜெண்ட்கள் இயக்கு**

ஏஜெண்ட்களை `.run` அல்லது `.run_stream` முறைகளைக் கொண்டு இயக்கு, இதில் ஒவ்வொரு முறையும் கட்டற்ற பதில் அல்லது ஸ்ட்ரீம் பதில் கிடைக்கும்.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ஒவ்வொரு ஏஜெண்ட் இயக்கத்துக்கும் ஏஜெண்ட் பயன் ப்படுத்தும் `max_tokens`, `tools` அழைக்கும் கருவிகள் மற்றும் `model` போன்ற விருப்பங்களை தனிப்பயன் செய்யலாம்.

இது குறிப்பிட்ட மாதிரிகள் அல்லது கருவிகள் பயனரின் பணியை நிறைவேற்ற தேவையான போது உதவும்.

**கருவிகள்**

கருவிகள் ஏஜெண்ட் வரையறுக்கும் போது வரையறுக்கப்படலாம்:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# நேரடியாக ஒரு ChatAgent உருவாக்கும்போது

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

மற்றும் ஏஜெண்ட் இயக்கும் போது:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # இந்த ஓட்டத்திற்கான கருவி மட்டும் வழங்கப்பட்டது )
```

**ஏஜெண்ட் திரெட்கள்**

ஏஜெண்ட் திரெட்கள் பல-துறை உரையாடல்களை கையாள பயன்படுத்தப்படுகின்றன. திரெட்கள் உருவாகலாம்:

- `get_new_thread()` பயன்படுத்தி, இது திரெட்களை காலத்திற்கு சேமிக்க உதவும்
- ஏஜெண்ட் இயக்கும் போது தானாக திரெடுகள் உருவாக்கப்பட்டு தற்போதைய இயக்கத்தில் மட்டுமே இருப்பது.

திரெடு உருவாக்குவதற்கு, குறியீடு இதுவாக இருக்கும்:

```python
# புதிய திரட்டை உருவாக்கவும்.
thread = agent.get_new_thread() # அந்த திரையுடன் முகவரியை இயக்கவும்.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

பின்னர் இந்த திரெடுகளை சேமிக்க சீரியலைஸ் செய்யலாம்:

```python
# புதிய திரெட்யை உருவாக்கு.
thread = agent.get_new_thread() 

# திரெடு உடன் முகவரியை இயக்குக.

response = await agent.run("Hello, how are you?", thread=thread) 

# சேமிப்புக்காக திரெட்யை தொடர்துறைக.

serialized_thread = await thread.serialize() 

# சேமிப்பிலிருந்து சரிவர பிறகு திரெட்டின் நிலையை தொடர்துறைக.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ஏஜெண்ட் மிடில் வேர்**

ஏஜெண்ட்கள் கருவிகள் மற்றும் LLM களுடன் தொடர்பு கொண்டு பயனர் பணிகளை முடிக்கின்றன. சில சூழல்களில், இந்த தொடர்புகளுக்கு இடையே செயல்பட அல்லது கண்காணிக்கவேண்டும். ஏஜெண்ட் மிடில் வேர் இதை சாத்தியமாக்குகிறது:

*செயல்பாட்டு மிடில் வேர்*

இந்த மிடில் வேர் ஏஜெண்டும் அழைக்கும் கருவி/செயல்பாட்டிற்கிடையில் செயல் செய்யவும், பதிவு செய்யவும் உதவுகிறது. உதாரணமாக, செயல்பாடு அழைக்கும் போது பதிவு செய்ய இந்த மிதில் வேர் பயன்படும்.

கீழே `next` என்றால் அடுத்த மிடில்வேர் அல்லது உண்மையான செயல்பாடு அழைக்கப்படவுள்ளதா என்பதை குறிப்பிடுகிறது.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # முன் செயலாக்கம்: செயல்பாட்டு இயங்குவதற்கு முன் பதிவேடு
    print(f"[Function] Calling {context.function.name}")

    # அடுத்த மிடில்‌வர்க்கை அல்லது செயல்பாட்டு இயங்குதலை தொடர்க
    await next(context)

    # பின்பற்றும் செயலாக்கம்: செயல்பாட்டு இயங்கும்பின் பதிவேடு
    print(f"[Function] {context.function.name} completed")
```

*உரையாடல் மிடில் வேர்*

ஏஜெண்டுக்கும் LLM ஓடும் கோரிக்கைகளுக்கிடையேயும் செயல்பட அல்லது பதிவு செய்ய இந்த மிடில் வேர் உதவுகிறது.

இதில் AI சேவைக்கு அனுப்பப்படும் `messages` போன்ற முக்கிய தகவல்கள் அடக்கம்.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # முன் செயலாக்கம்: AI அழைப்பிற்கு முன் பதிவு செய்யவும்
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # அடுத்த மிடில்வேர் அல்லது AI சேவைக்கு தொடரவும்
    await next(context)

    # பின் செயலாக்கம்: AI பதிலுக்குப் பிறகு பதிவு செய்யவும்
    print("[Chat] AI response received")

```

**ஏஜெண்ட் நினைவு**

`Agentic Memory` பாடத்தில் பேசியதுபோல், நினைவு ஏஜெண்ட் வெவ்வேறு சூழல்களில் செயல்பட முக்கியமான கூறாகும். MAF பல வகை நினைவுகளை வழங்குகிறது:

*உள்ளூரில் சேமிப்பு*

பயன்பாட்டு ஓட்டத்தின் போது திரெட்களில் நிலைத்த நினைவு இது.

```python
# புதிய நூலை உருவாக்கவும்.
thread = agent.get_new_thread() # thread உடன் एजன்டை இயக்கவும்.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*நிறுத்த முடிய கூடிய செய்திகள்*

பல அமர்வுகளுக்கு இடையில் உரையாடல் வரலாற்றை சேமிக்க இது பயன்படுத்தப்படுகிறது. `chat_message_store_factory` மூலம் வரையறுக்கப்படுகிறது:

```python
from agent_framework import ChatMessageStore

# ஒரு விருப்பமான செய்தி சேமிப்பகத்தை உருவாக்கவும்
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*மாறும் நினைவு*

ஏஜெண்ட்கள் இயக்கும் முன் சூழலுக்கு இந்த நினைவு சேர்க்கப்படுகிறது. mem0 போன்ற வெளியூர் சேவைகளில் சேமிக்க கூடும்:

```python
from agent_framework.mem0 import Mem0Provider

# மேம்பட்ட நினைவக திறன்களுக்காக Mem0 பயன்படுத்துதல்
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**ஏஜெண்ட் கவனிப்புத்தன்மை**

கவனிப்புத்தன்மை நம்பகமான மற்றும் பராமரிக்கும் ஏஜெண்ட் அமைப்புகளை கட்டமைக்க முக்கியம். MAF OpenTelemetry உடன் இணைந்து உயர் கவனிப்புத்தன்மையை வழங்குகிறது.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ஏதாவது செய்
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### வேலைபட்டிகள்

MAF வேலைபட்டிகள் என்பது ஒரு பணியை முடிக்க முன்கூட்டியே வரையறுக்கப்பட்ட படிகள் மற்றும் அதில் AI ஏஜெண்ட்கள் கூறுகளாக அடங்குகின்றன.

வேலைபட்டிகள் பல கூறுகளைக் கொண்டு உருவாக்கப்படுகின்றன, இது சிறந்த கட்டுப்பாட்டு தரவை வழங்குகிறது. வேலைபட்டிகள் **பல ஏஜெண்ட் ஒர்க்செஷன்** மற்றும் **சேமிப்பு புள்ளி** க்கும் உதவுகின்றன.

வேலைபட்டியின் முக்கிய கூறுகள்:

**நிர்வாகிகள்**

நிர்வாகிகள் உள்ளீட்டுச் செய்திகள் பெறுவர், தங்கள் பணிகளைச் செய்து பின்பு வெளியீட்டுச் செய்தி வழங்குவர். இது வேலைபட்டியை பெரிய பணியை முடிக்கும் நோக்கத்தில் முன்னேற்றி நகர்த்தும். நிர்வாகிகள் AI ஏஜெண்ட் அல்லது தனிப்பயன் தந்திரம் ஆக இருக்கலாம்.

**நிழல்கள்**

நிழல்கள் வேலைபட்டியில் செய்தி கட்டுப்பாட்டை வரையறுக்க பயன்படுகின்றன. அவை:

*நேரடி நிழல்கள்* - நிர்வாகிகள் இடையேயான எளிய ஒருநிலை கனெக்ஷன்கள்:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*கூடுதல் நிழல்கள்* - குறிப்பிட்ட நிபந்தனை பூர்த்தி ஆனபின் செயல்படுகின்றன. உதாரணமாக, ஹோட்டல் அறைகள் கிடைக்காவிட்டால், நிர்வாகி மாற்றுச் சலுகைகளை பரிந்துரைக்க முடியும்.

*மாறுதல்-வாய்ப்பு நிழல்கள்* - நிபந்தனைகளின்படி செய்திகளை வேறு நிர்வாகிகளுக்கு வழியனுப்பும். உதா: பயணக் கஸ்டமர் முன்னுரிமை பெற்றிருந்தால் அவர்களின் பணிகள் வேறு வேலைபட்டியின் வழியாக கையாளப்படலாம்.

*வீசல்-வெளி நிழல்கள்* - ஒரு செய்தியை பல இலக்குகளுக்கு அனுப்பும்.

*வீசல்-உள்ளே நிழல்கள்* - பல நிர்வாகிகளிடமிருந்து பல செய்திகளை சேகரித்து ஒரே இலக்குக்கு அனுப்பும்.

**நிகழ்வுகள்**

வேலைபட்டிகளில் சிறந்த கவனிப்புத்தன்மைக்காக MAF நிறைவேற்ற நிகழ்வுகளுக்கு உள்ளடக்க நிகழ்வுகளை வழங்குகிறது:

- `WorkflowStartedEvent`  - வேலைபட்டி செயல்பட தொடங்கும்
- `WorkflowOutputEvent` - வேலைபட்டி வெளியீடு உருவாக்கும்
- `WorkflowErrorEvent` - வேலைபட்டியில் பிழை ஏற்படும்
- `ExecutorInvokeEvent`  - நிர்வாகி செயல்பட தொடங்கும்
- `ExecutorCompleteEvent`  -  நிர்வாகி செயல்பாடு முடியும்
- `RequestInfoEvent` - கோரிக்கை செய்யப்படும்

## மேம்பட்ட MAF முன்ன்மாதிரிகள்

மேலே கூறிய பகுதிகள் மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்பின் முக்கிய கருத்துக்களை உள்ளடக்கியவை. நீங்கள் கூடுதல் சிக்கலான ஏஜெண்டுகளை உருவாக்கும் போது, பின்வரும் மேம்பட்ட முன்மாதிரிகளை பரிசீலிக்கலாம்:

- **மிடில் வேர் சேர்க்கை**: பல மிடில் வேர் கையாள்பவர்களை (பதிவு, அங்கீகாரம், விகித கட்டுப்பாடு) செயல் மற்றும் உரையாடல் மிடில் வேர் மூலம் சங்கிலியடைத்து ஏஜெண்ட் நடத்தை மேம்படுத்துதல்.
- **வேலைபட்டி சேமிப்பு புள்ளிகள்**: வேலைபட்டி நிகழ்வுகள் மற்றும் சீரியல் செய்தியைப் பயன்படுத்தி நீண்டநேர ஏஜெண்ட் செயல்முறைகளை சேமித்து மீண்டும் தொடருதல்.
- **டயனமிக் கருவி தேர்வு**: MAF கருவி பதிவு மூலம் கருவி விளக்கங்களுக்குமேல் RAG ஐ இணைத்து கேள்விக்கு தொடர்புடைய கருவிகளை மட்டுமே வழங்குதல்.
- **பல ஏஜெண்ட் ஹேண்ட்அஃப்**: வேலைபட்டி நிழல்கள் மற்றும் கூடுதல் வழிமொழிகள் மூலம் சிறப்பு ஏஜெண்ட்களுக்கு இடையிலான பணிநிறுவல் ஒருங்கிணைப்பு.

## Microsoft Foundry இல் LangChain / LangGraph ஏஜெண்ட்களை ஹோஸ்ட் செய்வது

Microsoft Agent Framework என்பது **கட்டமைப்பு ஒருங்கிணைப்புக்ககூடியது** — MAF கொண்டு எழுதப்பட்ட ஏஜெண்டுகள் மட்டுமல்ல. நீங்கள் ஏற்கனவே **LangChain** அல்லது **LangGraph** கொண்டு உருவாக்கிய ஏஜெண்ட் இருந்தால், அதை **Microsoft Foundry ஹோஸ்ட் ஏஜெண்ட்** ஆக இயக்கு முடியும், இதனால் Foundry ரன்டைம், அமர்வுகள், ஸ்திதிகேடுகள், அடையாளம் மற்றும் நடைமுறை இடைமுகங்களை நிர்வகிக்கும், உங்கள் ஏஜெண்ட் நிலைமுறை LangGraph இல் இருப்பது போல.

இது `langchain_azure_ai.agents.hosting` தொகுப்பினால் செய்யப்படுகிறது, இது ஒன்றுபட்ட Foundry ஹோஸ்ட் ஏஜெண்டுகள் பயன்படுத்தும் நடைமுறைகளில் LangGraph கிராபை வெளிப்படுத்துகிறது.

**1. ஹோஸ்டிங் கூடுதலை நிறுவுக:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` கூடுதல் Foundry நடைமுறை நூலகங்களை நிறுவுகிறது: `azure-ai-agentserver-responses` (OpenAI சார்ந்த `/responses` முடிச்சு) மற்றும் `azure-ai-agentserver-invocations` (பொதுவான `/invocations` முடிச்சு).

**2. ஹோஸ்டிங் நடைமுறையை தெரிவுசெய்க:**

| நடைமுறை | ஹோஸ்ட் வகுப்பு | முடிச்சு | பயன்படும் போது |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | நீங்கள் OpenAI-ன் உரையாடல், ஸ்ட்ரீமிங், பதில் வரலாறு மற்றும் உரையாடல் திரெடிங் வேண்டும் என்றால் — உரையாடல் ஏஜெண்டுகளுக்கு பரிந்துரைக்கப்படும் இயல்புநிலை. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | தனிப்பயன் JSON வடிவமைப்பு, webhook-போன்ற முடிச்சு, அல்லது உரையாடல் அல்லாத செயலாக்கம் தேவைப்படின். |

ஏனெனில் **Responses API Foundry இல் ஏஜெண்ட் வகை மேம்பாட்டுக்கான முக்கிய API ஆகும்**, பெரும்பாலான ஏஜெண்டுக்களுக்கு `ResponsesHostServer` உடன் தொடங்கவும்.

**3. புவி சூழல் மாறிலிகளை அமைக்கவும்** (`az login` செய்க, அதனால் `DefaultAzureCredential` அங்கீகாரம் செய்யும்):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

ஏஜெண்ட் பின்னர் Foundry ஹோஸ்ட் ஏஜெண்டாக இயங்கும் போது, தளம்தானாக `FOUNDRY_PROJECT_ENDPOINT` ஐ நிரப்பும்.

**4. Responses நடைமுறையில் LangGraph ஏஜெண்டை வெளிப்படுத்தவும்:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI இங்கு Foundry திட்டத்தின் OpenAI-பொருந்தக்கூடிய (பதில்) முடிவை குறிக்கிறது.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

`python main.py` மூலம் உள்ளகமாக இயக்கு, பின்னர் `http://localhost:8088/responses` க்கு Responses கோரிக்கை அனுப்பவும்.

**முக்கிய நடத்தை:**

- **உரையாடல்கள்**: வாடிக்கையாளர்கள் உரையாடலை தொடர்ந்து தொடர முன்னைய பதில் ஐ.டி. `previous_response_id` அல்லது `conversation` ஐ.டி. வழங்குவர். உங்கள் கிராப் LangGraph சேமிப்பகத்துடன் திரும்பப்பட்டால் Foundry உரையாடல் நிலையினை சேமிப்பகத்துடன் இணைப்பதைக் கண்காணிக்கும் (தயாரிப்பு சூழலுக்கு உறுதிப் பணியாளர் தேவை, உள்ளக சோதனையின் জন্য `MemorySaver` போதும்).
- **மனிதர் சம்மந்தப்பட்ட செயல்முறை**: உங்கள் கிராப் LangGraph இன் `interrupt()` பயன்படுத்தினால் `ResponsesHostServer` எதிர்பார்க்கும் இடைநிறுத்தத்தை Responses `function_call` / `mcp_approval_request` உருப்படி ஆக வெளிக்காட்டும் மற்றும் வாடிக்கையாளர்கள் ஒத்த function_call_output` / `mcp_approval_response` உடன் தொடர்வார்கள்.
- **Foundryக்கு வெளியிடவும்**: Azure Developer CLI பயன்படுத்தவும் — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (உள்ளக, Docker தேவை), பின்னர் `azd provision` மற்றும் `azd deploy`. ஹோஸ்ட் ஏஜெண்ட் வெளியீடு **Foundry Project Manager** வேடத்தில் அங்கீகாரம் தேவை.

இதற்கான இயக்கும் உதாரணம் [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) இல் உள்ளது. முழு வழிகாட்டலுக்காக (Invocations நடைமுறை, தனிப்பயன் கோரிக்கை வடிவங்கள் மற்றும் சிக்கல் தீர்க்கை), [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) பாருங்கள்.

## குறியீட்டுக்கான எடுத்துக்காட்டுகள்

மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்புக்கான குறியீட்டு எடுத்துக்காட்டுகள் இந்த நிரலகத்தில் `xx-python-agent-framework` மற்றும் `xx-dotnet-agent-framework` கோப்புகளுக்குள் கிடைக்கின்றன.

## மைக்ரோசாஃப்ட் ஏஜென்ட் கட்டமைப்புக்கான கூடுதல் கேள்விகள் உள்ளதா?

மற்ற கற்றலர்களை சந்திக்க, அலுவலக நேரத்தில் கலந்துகொள்ள மற்றும் உங்கள் AI ஏஜெண்ட் கேள்விகளுக்கு பதில் பெற [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) சேருக.
## முந்தைய பாடம்

[AI ஏஜெண்டுகளுக்கான நினைவு](../13-agent-memory/README.md)

## அடுத்த பாடம்

[கணினி பயன்பாட்டு ஏஜெண்டுகள் (CUA) உருவாக்குதல்](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->