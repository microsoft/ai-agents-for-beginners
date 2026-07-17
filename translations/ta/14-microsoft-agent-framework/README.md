# மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்க் ஆராய்ச்சி

![Agent Framework](../../../translated_images/ta/lesson-14-thumbnail.90df0065b9d234ee.webp)

### அறிமுகம்

இந்த பாடம் இவற்றை உள்ளடக்கியது:

- மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்க்: முக்கிய அம்சங்கள் மற்றும் மதிப்பு புரிதல்  
- மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்கின் முக்கிய கருத்துக்களை ஆராய்தல்
- மேம்படுத்தப்பட்ட MAF வடிவங்கள்: வேலைபட்டறைகள், மிடில்வேர் மற்றும் நினைவகம்

## கற்றல் இலக்குகள்

இந்த பாடத்தை முடித்தவுடன், நீங்கள் அறிந்துகொள்ளுவீர்கள்:

- மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்கைப் பயன்படுத்தி தயாரிப்பு தயார கணினி ஏஜெண்ட்களை உருவாக்குதல்
- உங்கள் ஏஜெண்டிக் பயன்படுத்தல் வழக்குகளில் மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்கின் மைய அம்சங்களைப் பயன்படுத்துதல்
- வேலைபட்டறைகள், மிடில்வேர் மற்றும் பார்வையிடல் உட்பட மேம்பட்ட வடிவங்களைப் பயன்படுத்துதல்

## குறியீடு உதாரணங்கள் 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) குறியீடு உதாரணங்கள் இந்த கோப்பகத்தில் `xx-python-agent-framework` மற்றும் `xx-dotnet-agent-framework` கோப்புகளுக்குள் காணலாம்.

## மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்க் புரிதல்

![Framework Intro](../../../translated_images/ta/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) என்பது மைக்ரோசாஃப்டின் ஒருங்கிணைந்த ஃபிரேம்வொர்க் ஆகும், இது AI ஏஜெண்ட்களை உருவாக்குவதற்காகும். இது தயாரிப்பு மற்றும் ஆய்வு சூழல்களில் காணப்படும் பலவித ஏஜெண்டிக் பயன்படுத்தல் வழக்குகளுக்கு தகுந்த தகுதிகளை வழங்குகிறது:

- **வரிசையான ஏஜெண்ட் ஒர்க்ச்டிரேஷன்** - நிலை தவறாமல் படி படியாக வேலைபட்டறைகள் தேவையான சூழல்களில்.
- **ஒத்த ஓட்ட ஒர்க்ச்டிரேஷன்** - ஏஜெண்ட்கள் ஒரே நேரத்தில் பணிகளை முடிக்க வேண்டும் என்ற சூழல்களில்.
- **குழு உரையாடல் ஒர்க்ச்டிரேஷன்** - ஏஜெண்ட்கள் ஒரே பணியில் ஒன்றாக பணியாற்றும் சூழல்களில்.
- **ஹேண்ட்ஓஃப் ஒர்க்ச்டிரேஷன்** - துணைப் பணிகள் முடிந்தவுடன் ஏஜெண்ட்கள் பணியை பரிமாறிக் கொள்வது.
- **மேக்நெடிக் ஒர்க்ச்டிரேஷன்** - ஒரு மேலாளர் ஏஜெண்ட் பணியினை உருவாக்கி மாற்றி, துணை ஏஜெண்ட்களை ஒருங்கிணைத்து பணி முடிப்பது.

தயாரிப்பில் AI ஏஜெண்ட்களை வழங்க MAF இல் கீழ்காணும் அம்சங்கள் உள்ளன:

- **பார்வையிடல்** OpenTelemetry பயன்படுத்தி AI ஏஜெண்டின் ஒவ்வொரு செயலும் (கருவி அழைப்பு, ஒர்க்ச்டிரேஷன் படிகள், எண்ணம் சுழற்சிகள் மற்றும் Microsoft Foundry டாஷ்போர்ட்கள் மூலம் செயல்திறன் கண்காணிப்பு) காணப்படக்கூடியது.
- **பாதுகாப்பு** Microsoft Foundry இல் இயல்பாக ஏஜெண்ட்களை நடத்துதல்; இதில் வேடிக்கை அடிப்படையிலான அணுகல், தனிப்பட்ட தரவுகளின் கையாள்தல் மற்றும் உள்ளமைக்கப்பட்ட உள்ளடக்கு பாதுகாப்பு உள்ளது.
- **மடுங்குணம்** ஏஜெண்ட் திரைகள் மற்றும் வேலைபட்டறைகள் இடைநிறுத்தம், தொடக்கம் மற்றும் பிழைகளிலிருந்து மீட்பு செயலாற்றலாம், இது நீண்டநாட்கள் இயக்கத்தைக் கொண்டுள்ளது.
- **கட்டுப்பாடு** மனித பங்கு கொண்ட வேலைபட்டறைகள் ஆதரிக்கப்படுகின்றன, பணிகளை மனித ஒப்புதலுக்கு அடையாளப்படுத்துகின்றன.

மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்க் ஒருங்கிணைப்பிற்கும் கவனம் செலுத்துகிறது:

- **கிளவுட்-அக்‌னோஸ்டிக்** - ஏஜெண்ட்கள் கன்டெய்னர்கள், ஆன-பிரேமிஸ் மற்றும் பல கிளவுட்கள் முழுவதும் இயங்கலாம்.
- **வழங்குநர்-அக்‌னோஸ்டிக்** - உங்கள் விருப்பமான SDK உடன் ஏஜெண்ட்களை உருவாக்கலாம், Azure OpenAI மற்றும் OpenAI உட்பட.
- **திறந்த தரநிலைகளை ஒருங்கிணைத்தல்** - Agent-to-Agent (A2A) மற்றும் Model Context Protocol (MCP) போன்ற நெறிமுறைகளை பயன்படுத்தி பிற ஏஜெண்ட்கள் மற்றும் கருவிகளை கண்டறிந்து பயன்படுத்த முடியும்.
- **பிளக்கின்கள் மற்றும் இணைப்பிகள்** - Microsoft Fabric, SharePoint, Pinecone மற்றும் Qdrant போன்ற தரவு மற்றும் நினைவக சேவைகளுடன் இணக்கங்கள் உருவாக்கப்படலாம்.

இந்த அம்சங்கள் மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்கின் சில மைய கருத்துக்களில் எப்படி செயல்படுகின்றன பார்ப்போம்.

## மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்கின் முக்கிய கருத்துகள்

### ஏஜெண்ட்கள்

![Agent Framework](../../../translated_images/ta/agent-components.410a06daf87b4fef.webp)

**ஏஜெண்ட்களை உருவாக்குதல்**

ஏஜெண்ட் உருவாக்கம் என்பது கணிப்பு சேவையை (LLM வழங்குநர்), AI ஏஜெண்ட் பின்பற்ற வேண்டிய கட்டளைகள் தொகுப்பை மற்றும் முக்கியமான `name` கட்டுத்தொடரை வரையறுத்து செய்யப்படுகிறது:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

மேலே `Azure OpenAI` பயன்படுத்தப்பட்டுள்ளது, ஆனால் ஏஜெண்ட்கள் பல்வேறு சேவைகள் மூலம் உருவாக்கப்படலாம், அதில் `Microsoft Foundry Agent Service` அடங்கும்:

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

அல்லது [MiniMax](https://platform.minimaxi.com/), இது மிகப் பெரிய ஏற்பாடுப் பாவனைக் கோப்புகளுடன் (204K டோக்கன்கள் வரையிலும்) OpenAI-உடன் பொருந்தக்கூடிய API வழங்குகிறது:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

அல்லது A2A நெறிமுறை பயன்பாட்டில் தொலைநிலைய ஏஜெண்ட்கள்:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ஏஜெண்ட்களை இயக்குதல்**

ஏஜெண்ட்கள் `.run` மற்றும் `.run_stream` முறைகளை பயன்படுத்தி இயங்குகின்றன; இது இல்லை என்றால் ஓர் ஒழுங்கான அல்லது ஓர் பாடலுக்கு பதிலளிக்கும் செயல்கள்.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ஒவ்வொரு ஏஜெண்ட் இயக்கத்துக்கும் `max_tokens`, `tools` மற்றும் ஏஜெண்ட் பயன்படுத்தும் `model` போன்ற மாற்றங்களை விருப்பப்படி அமைக்கலாம்.

இது பயனர்களின் பணிகளை நிறைவேற்றப் ப்ரத்யேகமான மாதிரிகள் அல்லது கருவிகள் தேவைப்படும் சந்தர்ப்பங்களில் உதவுகிறது.

**கருவிகள்**

கருவிகள் ஏஜெண்ட் வரையறுப்பின்போது:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# நேரடியாக ஒரு чат்எஜென்டை உருவாக்கும்போது

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

மற்றும் ஏஜெண்ட் இயங்கும்போது:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # இந்த இயக்கத்திற்கு மட்டும் வழங்கப்பட்ட கருவி )
```

**ஏஜெண்ட் திரைகள்**

ஏஜெண்ட் திரைகள் பேச்சுவார்த்தைகள் பல முறையிலும் நடத்தப்படுகின்றன. திரைகள் உண்டாக்கப்படலாம் கீழ்கண்ட முறைகளில்:

- `get_new_thread()` பயன்படுத்தி திரை கால அடைவில் சேமிக்க அதற்கு அனுமதிக்கும்
- அல்லது ஒரு ஏஜெண்ட் இயங்கும்போது தானாக திரை உருவாக்கப்படலாம் மற்றும் அது தற்போதைய இயக்கத்தில்தான் நிலைத்திருக்கும்.

திரை உருவாக்க குறியீடு இப்படிப் பார்க்கப்படுகிறது:

```python
# புதிய திரெட்டை உருவாக்கவும்.
thread = agent.get_new_thread() # திரெட்டை பயன்படுத்தி முகவரியை இயக்கவும்.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

பின்னர் அந்த திரையை சேமிக்கத் தொகுக்கலாம்:

```python
# புதிய த்ரெட்டை உருவாக்கு.
thread = agent.get_new_thread() 

# த்ரெட்டை பயன்படுத்தி முகவரியை இயக்கு.

response = await agent.run("Hello, how are you?", thread=thread) 

# சேமிப்பதற்காக த்ரெட்டை தொடர் வடிவில் மாற்று.

serialized_thread = await thread.serialize() 

# சேமிப்பில் இருந்து ஏற்றிய பிறகு த்ரெட் நிலையில் இருந்து தொடர் வடிவை மாற்று.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ஏஜெண்ட் மிடில்வேர்**

ஏஜெண்ட்கள் கருவிகள் மற்றும் LLM களுடன் பணி நிறைவேற்றுகின்றன. சில சூழல்களில், இந்த தொடர்புகளுக்கு இடையில் செயல்களை இயக்கு அல்லது கண்காணிக்க நாம் விரும்பினால், ஏஜெண்ட் மிடில்வேர் இதை செய்யும் வழியைத் தருகிறது:

*Function Middleware*

இது ஏஜெண்ட் மற்றும் அழைக்கும் செயல்பாடு/கருவி இடையே செயல்பாட்டை செய்ய உதவுகிறது. எடுத்துக்காட்டாக, செயல்பாடு அழைப்பைப் பதிவு செய்ய வேண்டுமெனில் பயன்படுத்தலாம்.

கீழ்காணும் குறியீட்டில் `next` என்பது அடுத்த மிடில்வேர் அல்லது அசல் செயல்பாட்டை அழைக்கக் கூறுகிறது.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # முன்னொற்று செயலாக்கம்: செயல்வழி தொடங்குவதற்கு முன் பதிவேற்று
    print(f"[Function] Calling {context.function.name}")

    # அடுத்த மிடில்வேர் அல்லது செயல்வழி செயல்பாட்டுக்கு தொடரவும்
    await next(context)

    # பிந்தைய செயலாக்கம்: செயல்வழி முடிந்தபின் பதிவேற்று
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

இது ஏஜெண்ட் மற்றும் LLM இடையேயான கோரிக்கைகளுக்கு இடையில் செயல்பாடுகள் செய்ய அல்லது பதிவு செய்ய உதவுகிறது.

இதில் AI சேவைக்கு அனுப்பப்படும் `messages` போன்ற முக்கிய தகவல்கள் உள்ளடங்குபவையாகும்.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # முன்னோக்கி செயலாக்கம்: AI அழைப்புக்கு முன் பதிவு செய்யவும்
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # அடுத்த மிடில்웨어 அல்லது AI சேவைக்குப் போக்கினால் தொடரவும்
    await next(context)

    # பின்னோக்கி செயலாக்கம்: AI பதிலுக்கு பிறகு பதிவு செய்யவும்
    print("[Chat] AI response received")

```

**ஏஜெண்ட் நினைவகம்**

`Agentic Memory` பாடத்தில் விவரிக்கப்பட்டபடி, நினைவகம் ஏஜெண்ட் வேறு சூழல்களில் இயங்க முக்கிய கூறாகும். MAF இல் பல வகையான நினைவகம் உள்ளது:

*நினைவகம் உள் சேமிப்பு*

செயலியில் திரைகள் ஓடும் போது உள்ள நினைவகம்.

```python
# புதிய திரெட்டை உருவாக்கவும்.
thread = agent.get_new_thread() # திரெட்டுடன் முகவரியை இயக்கவும்.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*நிலையான செய்திகள்*

வெவ்வேறு அமர்வுகளின் பேச்சுவார்த்தை வரலாற்றை சேமிக்கும் நினைவகம். `chat_message_store_factory` மூலம் வரையறுக்கப்பட்டுள்ளது:

```python
from agent_framework import ChatMessageStore

# ஒரு தனிப்பயன் செய்தி சேமிப்பகத்தை உருவாக்கவும்
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*நடைமுறைய நினைவகம்*

இது ஏஜெண்ட்கள் இயங்குவதற்கு முன் சூழலில் சேர்க்கப்படும் நினைவகம். mem0 போன்ற வெளியில் சேவைகளில் சேமிக்கப்படலாம்:

```python
from agent_framework.mem0 import Mem0Provider

# மேம்பட்ட நினைவக திறன்களுக்காக Mem0 பயன்படுத்தப்படுகிறது
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

**ஏஜெண்ட் பார்வையிடல்**

பார்வையிடல் நம்பகமான மற்றும் பராமரிக்கக்கூடிய ஏஜெண்ட் அமைப்புகளை கட்டுவதற்கு முக்கியம். MAF OpenTelemetry உடன் ஒருங்கிணைந்து சரிசெய்தல் மற்றும் அளவுகோல்களை வழங்குகிறது.

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

### வேலைப்பட்டறைகள்

MAF வேலைப்பட்டறைகள் என்றன, இது ஒரு பணியை முடிக்க முன் வரையறுக்கப்பட்ட படிகளாகவும், அதில் AI ஏஜெண்ட்கள் கூறுகளாக உள்ளன.

வேலைப்பட்டறைகள் பல கூறுகளால் ஆனவை, இது சிறந்த கட்டுப்பாட்டை வழங்கும். வேலைப்பட்டறைகள் **பல ஏஜெண்ட் ஒர்க்ச்டிரேஷன்** மற்றும் **Checkpointing** வசதியையும் தருகின்றன, வேலைப்பட்டறை நிலைகளை சேமிக்க.

வேலைப்பட்டறையின் முக்கிய கூறுகள்:

**நடவடிக்கை ஆட்கள்**

நடுவர்கள் உள்ளீட்டுப் செய்திகளை பெறுகின்றனர், அவர்களுக்கு உட்பட்ட பணிகளை செய்கிறார்கள், பிறகு வெளியீட்டு செய்தியை உருவாக்குகிறார்கள். இது வேலைப்பட்டறையை பெரிய பணியை முடிக்க முன்னோக்கி நகர்த்துகிறது. நடுவர்கள் AI ஏஜெண்ட் அல்லது தனிப்பயன் மெய்நிகர் ஆகலாம்.

**கடம்புகள்**

வேலைப்பட்டறையின் செய்தித்தொகுப்பின் ஓட்டத்தை வரையறுக்க கடம்புகள் பயன்படுத்தப்படுகின்றன. இவை:

*நேரடி கடம்புகள்* - நடுவர்களுக்கு நேரடியாக ஒரு-ஒரு இணைப்புகள்:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*நிபந்தனை கடம்புகள்* - குறிப்பிட்ட நிபந்தனை பூர்த்தியாயின் செயல்படும். எடுத்துக்காட்டாக, ஹோட்டல் அறைகள் கிடைக்காவிட்டால், நடுவர் பிற விருப்பங்களை பரிந்துரைக்கலாம்.

*மாற்று-பிரிவுகள் கடம்புகள்* - நிபந்தனைகளின் அடிப்படையில் செய்திகள் வெவ்வேறு நடுவருக்கு வழிமாற்றம் செய்யப்படுகின்றன. எடுத்துக்காட்டாக, பயண வாடிக்கையாளர் முன்னுரிமை அணுகல் உள்ள போது அவர்களது பணிகள் வேறு வேலைப்பட்டறையின் மூலம் செய்யப்படும்.

*பரவல்-வெளியே கடம்புகள்* - ஒரு செய்தியை பல இலக்குகளுக்கு அனுப்புதல்.

*பரவல்-உள்ளே கடம்புகள்* - பல நடுவர்களிடமிருந்து பல செய்திகள் சேர்த்து ஒரே இலக்குக்கு அனுப்புதல்.

**நிகழ்வுகள்**

வேலைப்பட்டறைகளுக்குள் சிறந்த பார்வையிடலை வழங்க, MAF பின்வரும் என்கார்ச் நிகழ்வுகளை தருகிறது:

- `WorkflowStartedEvent`  - வேலைப்பட்டறை இயக்கம் தொடக்கம்
- `WorkflowOutputEvent` - வேலைப்பட்டறை வெளியீடு உருவாக்கல்
- `WorkflowErrorEvent` - வேலைப்பட்டறையில் பிழை ஏற்பட்டல்
- `ExecutorInvokeEvent`  - நடுவர் செயல்முறை தொடக்கம்
- `ExecutorCompleteEvent`  -  நடுவர் செயல்முறை நிறைவு
- `RequestInfoEvent` - கோரிக்கை வெளியீடு

## மேம்பட்ட MAF வடிவங்கள்

மேலே கூறப்பட்டவை மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்கின் முக்கிய கருத்துக்களை உள்ளடக்குகின்றன. நீங்கள் அதிக சிக்கலான ஏஜெண்ட்களை உருவாக்கும்போது, இங்கே சில மேம்பட்ட வடிவங்களை பரிசீலிக்கலாம்:

- **மிடில்வேர் கட்டமைப்பு**: பல மிடில்வேர் கையாளர்களை தொடுகலாக இணைத்து (பதிவேடு, அங்கீகாரம், விகித வரம்பு) செயல்பாட்டை நுட்பமாக கட்டுப்படுத்துதல்.
- **வேலைப்பட்டறை சேமிப்பு**: வேலைப்பட்டறை நிகழ்வுகள் மற்றும் தொடுக்குதல் கொண்டு நீண்டநாட்கள் இயக்கும் ஏஜெண்ட் செயல்களைச் சேமித்து மீண்டும் தொடங்கு.
- **செயல்பாட்டுக் கருவி தேர்வு**: கருவி விளக்கங்களின் மீது RAG வடிவமைப்பு மற்றும் MAF கருவி பதிவு மூலம் கேள்விக்கு பொருத்தமான கருவிகளையே மட்டும் வழங்குதல்.
- **பல ஏஜெண்ட் ஹேண்ட்ஓஃப்**: வேலைப்பட்டறை கடம்புகள் மற்றும் நிபந்தனை வழிமாற்றிகள் உதவி கொண்டு சிறப்பான ஏஜெண்ட்கள் இடையேயான பணிப் பரிமாற்றம்.

## மைக்ரோசாஃப்ட் ஃபவுன்ட்ரியில் LangChain / LangGraph ஏஜெண்ட்களை ஏற்படுத்தல்

மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்க் **ஃபிரேம்வொர்க்-இணைக்கும் வகை** — நீங்கள் MAF உடன் எழுதப்பட்ட ஏஜெண்ட்களால் மட்டுப்படுத்தப்படவில்லை. ஏற்கனவே **LangChain** அல்லது **LangGraph** உடன் உருவாக்கிய ஏஜெண்ட் இருந்தால், அதனை **Microsoft Foundry** இல் ஹோஸ்ட் செய்ய கூடிய ஏஜெண்டாக இயக்கலாம். இதனால் Foundry ரன்டைம், அமர்வு, பரிமாணம், அடையாளம் மற்றும் நெறிமுறை இடமுகங்களை நிர்வகிக்கும்; உங்கள் ஏஜெண்ட் செயல் LangGraph இல் இருக்கிறது.

இது `langchain_azure_ai.agents.hosting` தொகுப்பின் மூலம் செய்யப்படுகிறது, இது LangGraph வரைபடத்தை Foundry ஹோஸ்ட் ஏஜெண்ட்கள் பயன்படுத்தும் அதே நெறிமுறைகளில் வெளியிடுகிறது.

**1. ஹோஸ்டிங் கூடுதல் தொகுப்பை நிறுவுக:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` கூடுதல் Foundry நெறிமுறை நூலகங்கள்: `azure-ai-agentserver-responses` (OpenAI பொருந்தக்கூடிய `/responses` இடமுகம்) மற்றும் `azure-ai-agentserver-invocations` (பொது `/invocations` இடமுகம்) நிறுவுகிறது.

**2. ஹோஸ்டிங் நெறிமுறையை தேர்ந்தெடுக்கவும்:**

| நெறிமுறை | ஹோஸ்ட் வகுப்பு | முடிவுச்சுடு | எப்போது பயன்படுத்தவேண்டும் |
|----------|-----------|----------|----------|
| **உத்தரவுகள்** | `ResponsesHostServer` | `/responses` | இந்திய OpenAI பொருந்தக்கூடிய உரையாடல், பதிவு, பதில்ச் சுழற்சி, உரையாடல் திரைகள் — பரிந்துரைக்கப்படும் இயல்புநிலை உரையாடல் ஏஜெண்ட்களுக்கு. |
| **அழைப்புகள்** | `InvocationsHostServer` | `/invocations` | தனிப்பயன் JSON அமைப்பு, webhook பாணி இடமுகம் அல்லது உரையாடல் அல்லாத செயலாக்கம் தேவையானபோது. |

**Foundry இல் ஏஜெண்ட் வடிவமைப்புக்கு Responses API முதன்மை API ஆகவே உள்ளது**, ஆகவே பெரும்பாலும் `ResponsesHostServer` நெறிமுறையை முதலில் தொடங்குக.

**3. சுற்றுச்சூழல் மாறிலிகளை அமைக்கவும்** (`az login` முதலில் செய்வது, `DefaultAzureCredential` அதிகாரமளிக்கும்):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

ஏஜெண்ட் பின்னர் Foundry ஹோஸ்ட்டான ஏஜெண்டாக இயங்கும்போது, `FOUNDRY_PROJECT_ENDPOINT` தானாகச் சேர்க்கப்படும்.

**4. Responses நெறிமுறையில் LangGraph ஏஜெண்டை வெளிப்படுத்துக:**

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI இங்கு Foundry திட்டத்தின் OpenAI-இன் பொருத்தமான (பதில்) endpoint ஐ குறிக்கிறது.
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

`python main.py` உடன் உள்ளூரில் இயக்கவும், பிறகு `http://localhost:8088/responses`-க்கு Responses கோரிக்கை அனுப்பவும்.

**முக்கிய செயல்பாடுகள்:**

- **உரையாடல்கள்**: வாடிக்கையாளர்கள் உரையாடலை தொடர `previous_response_id` அல்லது `conversation` ID-வை தருகின்றனர். உங்கள் வரைபடம் LangGraph Checkpointer உடன் தொகுக்கப்பட்டிருந்தால், Foundry உரையாடல் நிலையை அதை அடிப்படையாகக் காப்பது (உற்பத்திக்கு தகுந்த Checkpointer பயன்படுத்தவும்; உள்ளூரில் சோதனைக்க `MemorySaver` சரியானது).
- **மனிதன் இடையில்**: உங்கள் வரைபடம் LangGraph `interrupt()` பயன்படுத்தினால், `ResponsesHostServer` நிலவும் இடையூறுகளை Responses `function_call` / `mcp_approval_request` உருப்படி முறையில் காட்டு, வாடிக்கையாளர் `function_call_output` / `mcp_approval_response` உடன் மறுபடியும் தொடர்கின்றனர்.
- **Foundry-க்கு இயக்குக**: Azure Developer CLI பயன்பாடு — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (உள்ளூர், Docker தேவை), பின்னர் `azd provision` மற்றும் `azd deploy`. ஹோஸ்ட்-ஏஜெண்ட் 배포க்கு **Foundry Project Manager** பங்கு தேவை.

இந்த உதாரணத்தின் இயங்கக்கூடிய பதிப்பு [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) இல் உள்ளது. முழு நடைமுறை (அழைப்புகள் நெறிமுறை, தனிப்பயன் கோரிக்கை வடிவங்கள் மற்றும் பிழைதிருத்தம்) க்காக [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) பாருங்கள்.

## குறியீடு உதாரணங்கள் 

மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்க் குறியீடு உதாரணங்கள் இந்த கோப்பகத்தில் `xx-python-agent-framework` மற்றும் `xx-dotnet-agent-framework` கோப்புகளுக்குள் காணலாம்.

## மைக்ரோசாஃப்ட் ஏஜெண்ட் ஃபிரேம்வொர்க் பற்றி மேலதிக கேள்விகள் உள்ளதா?

மற்ற கற்றல் பயணிகளுடன் சந்திக்க, அலுவலக நேரங்களில் கலந்துகொள்ள மற்றும் உங்கள் AI ஏஜெண்ட் கேள்விகளுக்கு பதில்கள் பெற [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)வைச் சேர்ந்துகொள்ளுங்கள்.
## முந்தைய பாடம்

[AI ஏஜெண்ட்களுக்கான நினைவகம்](../13-agent-memory/README.md)

## அடுத்த பாடம்

[கணினி பயன்படுத்தும் ஏஜெண்ட்களை உருவாக்குதல் (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->