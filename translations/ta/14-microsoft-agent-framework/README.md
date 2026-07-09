# Microsoft Agent Framework ஐ ஆராய்வது

![Agent Framework](../../../translated_images/ta/lesson-14-thumbnail.90df0065b9d234ee.webp)

### அறிமுகம்

இந்த பாடத்தில் விவாதிக்கப்படுவது:

- Microsoft Agent Framework ஐப் பார்வையிடுதல்: முக்கிய அம்சங்கள் மற்றும் மதிப்பு  
- Microsoft Agent Framework இன் முக்கிய கருத்துக்களை ஆராய்தல்
- மேம்பட்ட MAF மாதிரிகள்: வேலைநடவடிக்கைகள், மிடில் வேர், மற்றும் நினைவகம்

## கற்றல் நோக்கங்கள்

இந்த பாடத்தை முடித்த பிறகு, நீங்கள் எப்படி என்பதை அறிய வாய்ப்பு உண்டு:

- Microsoft Agent Framework ஐ பயன்படுத்தி தயாரிப்பு தயாரா AI முகவர்களை உருவாக்க
- Microsoft Agent Framework இன் முக்கிய அம்சங்களை உங்கள் முகவர் பயன்பாடுகளில் பயன்படுத்த
- வேலைநடவடிக்கைகள், மிடில் வேர் மற்றும் கண்காணிப்பு உட்பட மேம்பட்ட மாதிரிகளை பயன்படுத்த

## குறியீட்டு உதாரணங்கள்

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) குறியீட்டு உதாரணங்கள் இந்த நிரல்படுத்தல் தொகுப்பில் `xx-python-agent-framework` மற்றும் `xx-dotnet-agent-framework` கோப்புகளில் காணலாம்.

## Microsoft Agent Framework ஐப் புரிந்துகொள்ளல்

![Framework Intro](../../../translated_images/ta/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) என்பது Microsoft இன் ஒரு ஒருங்கிணைந்த திட்டமாகும், இது AI முகவர்களை உருவாக்க உதவுகிறது. இது வியாபார மற்றும் ஆராய்ச்சித் சூழல்களில் காணப்படும் முகவரி பயன்பாடுகளை சரிசெய்வதற்கான வசதிகளை வழங்குகிறது, இதில்:

- படி படியாக வேலைநடவடிக்கைகள் தேவைப்படும் சூழல்களில் **வரிசைமுறை முகவர் ஒருங்கினைவு**.
- முகவர்கள் ஒரே நேரத்தில் பணிகளை முடிக்க வேண்டிய சூழல்களில் **ஒத்த ஒருங்கினைவு**.
- ஒரே பணியில் கூட்டு வேலை செய்வதற்கான சூழல்களில் **குழு அரட்டை ஒருங்கினைவு**.
- துணைப் பணிகள் முடிவடையும் போதே முகவர்கள் பணியை ஒருவருக்கொருவர் ஒப்படைக்கும் சூழல்களில் **கையளிப்பு ஒருங்கினைவு**.
- மேலாளர் முகவர் பணி பட்டியலை உருவாக்கி மாற்றி, துணை முகவர்களை ஒருங்கிணைப்பதற்கான **காந்த ஒழுங்குமுறை**.

AI முகவர்களை தயாரிப்பில் வழங்க MAF இல் கூடுதல் அம்சங்கள் உள்ளன:

- ஒவ்வொரு AI முகவர் நடவடிக்கும், கருவி அழைப்புகள், ஒருங்கினைவு படிகள், காரணச் செயல்முறை மற்றும் Microsoft Foundry கண்காணிப்பு பலகைகள் மூலம் செயல்திறன் கண்காணிப்பு என **OpenTelemetry** மூலம் **கண்காணிப்பு**.
- Microsoft Foundryல் முகவர்களை இயல்பாக நடத்துவதன் மூலம் **பாதுகாப்பு**, இதில் பங்கு வழிநடத்தல் அணுகல், தனிப்பட்ட தரவு கையாளல் மற்றும் உள்ளமைக்கப்பட்ட உள்ளடக்க பாதுகாப்பு கட்டுப்பாடுகள் அடங்கும்.
- முகவர் தொடர்கள் மற்றும் வேலைநடவடிக்கைகள் இடைநிறுத்தம், மீண்டும் தொடங்குதல் மற்றும் பிழைகள் இருந்து மீட்பு செய்ய முடியும், இது நீண்டகால நடைமுறை செயல்பாடுகளை எளிதாக்கும் என **தங்குதன்மை**.
- பணிகள் மனித அனுமதி தேவைப்படுவதாக குறிக்கப்பட்டபோது மனிதம் சுற்றில் வேலையடங்கல் **கட்டுப்பாடு**.

Microsoft Agent Framework இணக்கமானதாக இருக்க கவனம் செலுத்துகிறது:

- **கிளவுட் பொருந்தாதது** - முகவர்கள் கன்டெய்னர்கள், ஆனரகம் மற்றும் பல கிளவுட்கள் முழுவதும் இயங்க முடியும்.
- **வழங்குநர் பொருந்தாதது** - Azure OpenAI மற்றும் OpenAI உட்பட விரும்பிய SDK மூலம் முகவர்கள் உருவாக்க முடியும்.
- **திறந்த தரநிலைகளுடன் ஒருங்கிணைத்தல்** - Agent-to-Agent(A2A) மற்றும் Model Context Protocol (MCP) போன்ற நடைமுறைகளை பயன்படுத்தி பிற முகவர்களையும் கருவிகளையும் கண்டறியவும் பயன்படுத்தவும் முடியும்.
- **பிளக்கின்கள் மற்றும் இணைப்பிகள்** - Microsoft Fabric, SharePoint, Pinecone மற்றும் Qdrant போன்ற தரவு மற்றும் நினைவகம் சேவைகளுடன் இணைப்புகள் செய்ய முடியும்.

இப்போது இந்த அம்சங்கள் Microsoft Agent Framework இன் சில முக்கியக் கருத்துக்களில் எப்படி பயன்படுத்தப்படுகின்றன என்பதை பார்ப்போம்.

## Microsoft Agent Framework இன் முக்கியக் கருத்துக்கள்

### முகவர்கள்

![Agent Framework](../../../translated_images/ta/agent-components.410a06daf87b4fef.webp)

**முகவர்கள் உருவாக்குதல்**

முகவரி உருவாக்குவது திருத்தச் சேவை (LLM வழங்குநர்), AI முகவர் பின்பற்ற வேண்டிய வழிமுறைகள் மற்றும் வரையறுக்கப்பட்ட `name` மூலம் செய்யப்படுகிறது:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

மேலே `Azure OpenAI` பயன்படுத்தப்பட்டுள்ளது, ஆனால் முகவர்கள் பல்வேறு சேவைகளைப் பயன்படுத்தி உருவாக்க முடியும், உதாரணமாக `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIகள்

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

அல்லது [MiniMax](https://platform.minimaxi.com/), இது பெரிய உள்ளடக்க சாளரங்களுடன் (இருபத்து நான்கு ஆயிரம் கிளைகளுக்கு வரை) OpenAI תאம் API வழங்குகிறது:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

அல்லது A2A நடைமுறையை வைத்து தொலை முகவர்கள்:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**முகவர்கள் இயக்கல்**

முகவர்கள் `.run` அல்லது `.run_stream` முறைகளைப் பயன்படுத்தி ஓட்டப்படும், இது ஒற்றை அல்லது ஒளிபரப்பு பதில்களுக்கு பொருந்தும்.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ஒவ்வொரு முகவர் ஓட்டம்에도 முகவர் பயன்படுத்தும் `max_tokens`, அழைக்கக்கூடிய `tools`, மற்றும் முகவருக்கு உபயோகப்படுத்தப்படும் `model` போன்ற அளவுகோலை அமைக்க விருப்பங்கள் இருக்கலாம்.

இது பயனரின் பணியை முடிக்க குறிப்பிட்ட மாதிரிகள் அல்லது கருவிகள் தேவைப்பட்டால் உதவும்.

**கருவிகள்**

கருவிகள் முகவரைக் கூறுகையில் வரையறுக்கப்படலாம்:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ஒரு ChatAgent நேரடியாக உருவாக்கக்கட்கு

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

மற்றும் முகவரைக் இயக்குகையில்:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # இந்த இயக்கத்திற்காக மட்டுமே வழங்கப்பட்ட கருவி )
```

**முகவர் தொடர்கள்**

முகவர் தொடர்கள் பன்முறை உரையாடல்களை கையாள பயன்படுத்தப்படுகின்றன. தொடர்கள் உருவாக்கப்படலாம்:

- தொடர்ந்து சேமிக்க `get_new_thread()` பயன்படுத்தி
- முகவரைக் இயக்கும் போது தானாக தொடர் உருவாக்கி, அது தற்போதைய ஓட்டத்தில் மட்டுமே நீடிக்கும்.

தொடர் உருவாக்க குறியீடு இப்படி இருக்கும்:

```python
# புதிய திரெட்டை உருவாக்கவும்.
thread = agent.get_new_thread() # திரெட்டுடன் முகவரியை இயக்கவும்.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

பின்னர் தொடர் தொடர்ச்சிக்காக சேமிக்க மாற்றலாம்:

```python
# ஒரு புதிய பட்டையை உருவாக்கவும்.
thread = agent.get_new_thread() 

# அந்த பட்டையுடன் முகவரியை இயக்கவும்.

response = await agent.run("Hello, how are you?", thread=thread) 

# சேமிப்பிற்கு பட்டையை தொடரவரிசைப்படுத்தவும்.

serialized_thread = await thread.serialize() 

# சேமிப்பிலிருந்து ஏற்றிய பின்னர் பட்டை நிலை தொடரவரிசைதிருத்தவும்.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**முகவர் மிடில் வேர்**

முகவர்கள் கருவிகள் மற்றும் LLMகளுடன் தொடர்பு கொண்டு பயனர் பணிகளை முடிக்கின்றனர். சில நேரங்களில், இந்த இடைமுக அணுகல்களுக்கு இடையில் செயலாற்ற அல்லது கண்காணிக்க விரும்புகிறோம். முகவர் மிடில் வெர் இதனைச் சாத்தியமாக்குகிறது:

*Function Middleware*

இந்த மிடில் வெர் முகவர் மற்றும் அவர் அழைக்கும் செயலியில் நடக்கும் நடவடிக்கைகளுக்கு இடையே செயல்படுத்த உதவுகிறது. உதாரணமாக, செயலி அழைப்பில் लॉக்கிங் செய்ய விரும்பலாம்.

கீழ்காணும் குறியீட்டில் `next` அடுத்த middleware அல்லது உண்மையான செயலி அழைக்கப்பட வேண்டுமென்பதை அமைக்கிறது.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # முன்னுரிமை செயலாக்கம்: செயல்பாடு செயல்படுவதற்கு முன் பதிவு செய்யுங்கள்
    print(f"[Function] Calling {context.function.name}")

    # அடுத்த மிடில்வேர் அல்லது செயல்பாட்டு செயல்பாட்டுக்கு தொடர்க
    await next(context)

    # பிற்சேர்க்கை செயலாக்கம்: செயல்பாடு நிறைவடைந்த பிறகு பதிவு செய்யுங்கள்
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

இந்த middleware முகவர் மற்றும் LLM இடையேயான கோரிக்கைகளுக்கு இடையில் செயலாக்கம் அல்லது பதிவு செய்ய அனுமதிக்கிறது.

இதில் `messages` போன்ற AI சேவைக்கு அனுப்பப்படும் முக்கிய தகவல்கள் உள்ளன.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # முன்னமைதல்: AI அழைப்புக்கு முன்பு பதிவேடு
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # அடுத்த மிடில்வேர் அல்லது AI சேவைக்கு தொடரவும்
    await next(context)

    # பிந்தமைதல்: AI பதிலுக்குப் பிறகு பதிவேடு
    print("[Chat] AI response received")

```

**முகவர் நினைவகம்**

`Agentic Memory` பாடத்தில் விவரிக்கப்பட்டபடி, நினைவகம் முகவர்களின் வேறுபட்ட சூழல்களில் செயல்பட உதவுகிறது. MAF பல விதமான நினைவகங்களைக் கொண்டுள்ளது:

*நினைவகம் சேமிப்பு*

இது செயலியின் ஓட்டத்தின் போது தொடர்களில் சேமிக்கப்படும் நினைவகம்.

```python
# புதிய துருவத்தை உருவாக்கவும்.
thread = agent.get_new_thread() # துருவத்துடன் முகவரியை இயக்கவும்.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*திடநிலையுள்ள செய்திகள்*

இது உரையாடல் வரலாற்றை பல அமர்வுகளுக்கு இடையூறாக சேமிக்க பயன்படும். இது `chat_message_store_factory` மூலம் வரையறுக்கப்படுகிறது:

```python
from agent_framework import ChatMessageStore

# ஒரு தனித்துவமான செய்தி அங்காடியை உருவாக்கவும்
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*திரும்பத்தக்க நினைவகம்*

முகவர்கள் இயக்கப்படுவதற்கு முன் சூழலுக்கு இந்த நினைவகம் சேர்க்கப்படுகிறது. இத்தகைய நினைவகங்கள் mem0 போன்ற வெளிப்புற சேவைகளில் சேமிக்கப்படலாம்:

```python
from agent_framework.mem0 import Mem0Provider

# மேம்பட்ட நினைவக திறன்களுக்காக Mem0 ஐ பயன்படுத்துதல்
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

**முகவர் கண்காணிப்பு**

நம்பகமான மற்றும் பராமரிப்புக்குரிய முகவர் அமைப்புகளை உருவாக்கும் போது கண்காணிப்பு முக்கியம். MAF OpenTelemetry ஐ ஒருங்கிணைத்து கண்காணிப்பு மற்றும் அம்ச அளவுகோல்களை வழங்குகிறது.

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

### வேலைநடவடிக்கைகள்

MAF வேலைநடவடிக்கைகள் என்பது குறிப்பிட்ட படிகள் மூலம் ஒரு பணியை முடிப்பதாகும் மற்றும் அந்த படிகளில் AI முகவர்கள் கூறுகளாக உள்ளனர்.

வேலைநடவடிக்கைகள் பல கூறுகளைக் கொண்டு கட்டுப்பாடு நன்கு அமைய உதவுகின்றன. இது *பல முகவர் ஒருங்கினைப்படுத்தல்* மற்றும் *பதில் பதிவு* போன்ற அம்சங்களையும் வழங்குகிறது.

வேலைநடவடிக்கையின் முக்கிய கூறுகள்:

**நிர்வகிகள்**

நிர்வகிகள் உள்ளீடு செய்திகள் பெற்று பணிகளை செய்யும், பின்னர் வெளிநிலை செய்தியை உருவாக்குகின்றனர். இது வேலைநடவடிக்கையை பெரிய பணித் தொடர்வரிசைக்குள் முனைவதற்கு உதவும். நிர்வகிகள் AI முகவரோ அல்லது தனிப்பயன் தர்க்கமும் இருக்கக்கூடும்.

**எஜுகள்**

எஜுகள் வேலைநடவடிக்கையில் செய்தி ஓட்டத்தை வரையறுக்கப் பயன்படுகின்றன. அவை:

*நேரடி எஜுகள்* - நிர்வகிகளுக்கு இடையில் நேரடி தொடர்புகள்:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*நிபந்தனை எஜுகள்* - குறிப்பிட்ட நிபந்தனை பூர்த்தி ஆன பிறகு செயல்படும். உதாரணமாக, ஹோட்டல் அறைகள் கிடைக்காவிட்டால், நிர்வகி பிற விருப்பங்களை பரிந்துரைக்கலாம்.

*சுவிட்ச்-கேஸ் எஜுகள்* - குறிக்கப்பட்ட நிபந்தனைகளின் அடிப்படையில் செய்திகள் மாறி நிர்வகிகளுக்குத் தொலைச்செலுத்தப்படும். உதா: பயண வாடிக்கையாளர் முன்னுரிமை அங்கீகாரம் பெற்றால், அவர்களின் பணிகள் வேறு வேலைநடவடிக்கையின் மூலம் கையாளப்படும்.

*ஃபேன்-அவுட் எஜுகள்* - ஒரே செய்தியை பல இலக்குகளுக்கு அனுப்புதல்.

*ஃபேன்-இன் எஜுகள்* - பல நிர்வகிகளிடமிருந்து பல செய்திகளை சேகரித்து ஒரே இலக்குக்கு அனுப்புதல்.

**நிகழ்வுகள்**

வேலைநடவடிக்கை கண்காணிப்பை மேலோங்க டிஎங்ஙகள் வழங்கப்படும் நிகழ்வுக்கள்:

- `WorkflowStartedEvent`  - வேலைநடவடிக்கை துவக்கம்
- `WorkflowOutputEvent` - வேலைநடவடிக்கை வெளியீடு உண்டாகிறது 
- `WorkflowErrorEvent` - வேலைநடவடிக்கையில் பிழை ஏற்பட்டது
- `ExecutorInvokeEvent`  - நிர்வகி செயல்பாட்டை துவக்குகின்றது
- `ExecutorCompleteEvent`  -  நிர்வகி செயல்பாடு முடிந்தது
- `RequestInfoEvent` - கோரிக்கை வெளியிடப்பட்டது

## மேம்பட்ட MAF மாதிரிகள்

மேல் கூறிய பகுதிகள் Microsoft Agent Framework இன் முக்கியக் கருத்துக்களைப் பராமரிக்கின்றன. நீங்கள் சிக்கலான முகவர்களை உருவாக்கும் போது, கவனிக்க வேண்டிய சில மேம்பட்ட மாதிரிகள்:

- **Middleware சேர்க்கை**: பல மிடில் வெர் மேலாளர்களை (பதிவேற்று, அங்கீகாரம், விகிதக்குறைவு) செயல்படுத்திப் பரந்து வரும் தொகுப்புகளை செய்க.
- **வேலைநடவடிக்கை பதில் பதிவு**: வேலைநடவடிக்கை நிகழ்வுகளும் தொடரக்கூடிய பதிலாய்வுகளும் நீண்டகால முகவர் செயல்முறைகள் சேமிப்பிற்கு.
- **மாறும் கருவி தேர்வு**: கருவிக்குரிய விளக்கங்களுடன் RAG இணைத்து MAF கருவி பதிவு மூலம் கேள்விக்கு பொருத்தமான கருவிகளை மட்டும் வழங்குதல்.
- **பல முகவர் கையளிப்பு**: வேலைநடவடிக்கை எஜுகள் மற்றும் நிபந்தனை வழிமாற்றத்தைக் கொண்டு சிறப்பு முகவர்களின் கையளிப்புகளை ஒருங்கிணைத்தல்.

## Microsoft Foundry இல் LangChain / LangGraph முகவர்கள் நடத்தல்

Microsoft Agent Framework **பிரேம்வொர்க்-இணக்கமானது** — நீங்கள் MAF மூலம் எழுதப்பட்ட முகவர்களை மட்டுமே பயன்படுத்த தேவையில்லை. நீங்கள் ஏற்கனவே **LangChain** அல்லது **LangGraph** மூலம் உருவாக்கிய முகவர்களைக் கொண்டிருந்தால், அந்த முகவர்களை **Microsoft Foundry விருந்தோம்பலாளர் முகவராக** இயக்க முடியும், இவ்வாறு Foundry இயக்கு நேரம், அமர்வுகள், அளவுரை, அடையாளம் மற்றும் நடைமுறை இறுதிப்புள்ளிகளை நிர்வகிக்கும், ஆனால் உங்கள் முகவர் தர்க்கம் LangGraph இல் தொடரும்.

இது `langchain_azure_ai.agents.hosting` தொகுப்பினால் செயற்படுத்தப்படுகிறது, இது Foundry விருந்தோம்பலாளர் முகவர்கள் பயன்படுத்தும் அதே நடைமுறைகளின் மேல் LangGraph வரைபடத்தை வெளியிடுகிறது.

**1. விருந்தோம்பல் கூடுதலை நிறுவவும்:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` கூடுதல் Foundry நடைமுறை நூலகங்களை நிறுவுகிறது: `azure-ai-agentserver-responses` (OpenAI-பொருந்தும் `/responses` இறுதி புள்ளி) மற்றும் `azure-ai-agentserver-invocations` (பொதுவான `/invocations` இறுதி புள்ளி).

**2. விருந்தோம்பல் நடைமுறை தேர்வு செய்யவும்:**

| நடைமுறை | விருந்தோம்பலாளர் வகுப்பு | இறுதி புள்ளி | எப்போது பயன்படுத்துவது |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | நீங்கள் OpenAI-பொருந்தும் அரட்டை, ஒளிபரப்பு, பதில் வரலாறு மற்றும் உரையாடல் தொடு threading விரும்பும் போது — உரையாடல் முகவர்களுக்கு பரிந்துரைக்கப்படுகிறது. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | தனிப்பயன் JSON வடிவம், webhook வகை இறுதி புள்ளி, அல்லது உரையாடலற்ற செயலாக்கம் தேவையான போது. |

ஏனெனில் **Responses API Foundryவில் முகவர்-மாதிரி மேம்பாட்டுக்கான பிரதான API ஆகும்**, பெரும்பாலான முகவர்களுக்காக `ResponsesHostServer` உடனே துவங்கவும்.

**3. சூழல் மாறிலிகளை அமைக்கவும்** (`az login` முதலில், இன்றி `DefaultAzureCredential` உறுதிசெய்ய இயலாது):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

முகவர் பின்னர் Foundryவில் விருந்தோம்பலாளர் முகவராக ஓடும்போது, தளத்தில் தானாக `FOUNDRY_PROJECT_ENDPOINT` இடப்படும்.

**4. Responses நடைமுறையிலிருந்து LangGraph முகவரைக் வெளிக்காட்டவும்:**

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

    # ChatOpenAI இங்கே Foundry திட்டத்தின் OpenAI-உருவான (பதில்கள்) முடிவுத்தொடர்புக்கு இலக்கிடுகிறது.
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

`python main.py` கொண்டு உள்ளூர் இயக்கவும், பின்னர் `http://localhost:8088/responses` வுக்கு Responses கோரிக்கை அனுப்பவும்.

**முக்கிய நடத்தைகள்:**

- **உரையாடல்கள்**: கிளையண்டுகள் முன்னாள் பதிலடி_இடம் அல்லது உரையாடல் ஐடியை விடுவிக்க மூலம் உரையாடலை தொடர்கின்றன. உங்கள் வரைபடம் LangGraph பதில் பதிவு பணியாளருடன் கட்டமைக்கப்பட்டால், Foundry உரையாடல் நிலையை பதில் பதிவுடன் இணைக்கிறது (தயவுசெய்து தயாரிப்பிற்கு நிலையான பதில் பதிவு பணியாளரைப் பயன்படுத்தவும்; உள்ளூர் சோதனைக்கு `MemorySaver` சரி).
- **மனிதம்-சுற்றிலும்**: உங்கள் வரைபடம் LangGraph `interrupt()` ஐ பயன்படுத்தினால், `ResponsesHostServer` காத்திருக்கும் இடைதடையை Responses `function_call` / `mcp_approval_request` உருப்படி ஆக வெளிப்படுத்துகிறது, கிளையண்டுகள் சமமான `function_call_output` / `mcp_approval_response` உடன் தொடர்கின்றன.
- **Foundryக்குப் பதிலளிக்கவும்**: Azure Developer CLI ஐப் பயன்படுத்தவும் — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (உள்ளூர், Docker தேவை), பின்னர் `azd provision` மற்றும் `azd deploy`. விருந்தோம்பலாளர் முகவர் நிறுவலுக்கு **Foundry Project Manager** பங்கு தேவை.

இந்த உதாரணத்தின் ஓட்டமிடக்கூடிய பதிப்பு [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) இல் உள்ளது. முழு நடைமுறைக்கான வழிகாட்டி (Invocations நடைமுறை, தனிப்பயன் கோரிக்கை வடிவங்கள் மற்றும் பிழைத்திருத்தம்) க்கான விவரங்களுக்கு [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) பார்க்கவும்.

## குறியீட்டு உதாரணங்கள்

Microsoft Agent Framework இற்கான குறியீட்டு உதாரணங்கள் இந்த நிரல்படுத்தலில் `xx-python-agent-framework` மற்றும் `xx-dotnet-agent-framework` கோப்புகளில் காணலாம்.

## Microsoft Agent Framework குறித்த உங்கள் கேள்விகள் மேலும் உள்ளதா?

மற்ற கற்றலாளர்களுடன் சந்திக்க, அலுவலக நேரங்களில் கலந்துகொள் மற்றும் உங்கள் AI முகவர் கேள்விகளுக்கு பதில்களை பெற [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) இல் சேரவும்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->