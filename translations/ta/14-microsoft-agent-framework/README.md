# மைக்ரோசாஃப்ட் முகவர் கூறமைப்பை ஆய்வு செய்வோம்

![Agent Framework](../../../translated_images/ta/lesson-14-thumbnail.90df0065b9d234ee.webp)

### அறிமுகம்

இந்த பாடத்தில் பேசப்படும் বিষয়ங்கள்:

- மைக்ரோசாஃப்ட் முகவர் கூறமைப்பை հասկகுதல்: முக்கிய அம்சங்கள் மற்றும் மதிப்பு  
- மைக்ரோசாஃப்ட் முகவர் கூறமைப்பின் முக்கிய கருத்துக்களை ஆராய்தல்
- மேம்பட்ட MAF மாதிரிகள்: பணிச்சுழற்சிகள், நடுநிலைமை, மற்றும் நினைவகம்

## கற்றல் இலக்குகள்

இந்த பாடத்தை முடித்ததும், நீங்கள் அறிவீர்கள்:

- மைக்ரோசாஃப்ட் முகவர் கூறமைப்பை பயன்படுத்தி தயாரிப்பு தயாராகும் AI முகவர்களை உருவாக்குவது
- உங்கள் முகவர் பயன்பாட்டு பயன்பாடுகளுக்கு மைக்ரோசாஃப்ட் முகவர் கூறமைப்பின் முக்கிய அம்சங்களை பயன்படுத்துவது
- பணிச்சுழற்சிகள், நடுநிலைமை மற்றும் கண்காணிப்பு உட்பட மேம்பட்ட மாதிரிகளைப் பயன்படுத்துவது

## குறியீட்டு மாதிரிகள்

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) குறியீட்டு மாதிரிகளை இந்த தொகுப்பில் `xx-python-agent-framework` மற்றும் `xx-dotnet-agent-framework` கோப்புகளில் காணலாம்.

## மைக்ரோசாஃப்ட் முகவர் கூறமைப்பை புரிந்துகொள்வது

![Framework Intro](../../../translated_images/ta/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) என்பது AI முகவர்களை உருவாக்கும் மைக்ரோசாஃப்டின் ஒருங்கிணைந்த கூறமைப்பாகும். இது பல்வேறு முகவர் பயன்பாடுகளுக்கு இன்னும் ஆராய்ச்சி சூழ்நிலையிலும் பயன்படும் வகையில் தொகுத்தமைக்கப்பட்டுள்ளது:

- **செயல்முறை முகவர் ஒருங்கிணைப்பு** - படி படி பணிச்சுழற்சிகள் தேவையான சூழ்நிலைகளில்.
- **நிகழ்கால ஒருங்கிணைப்பு** - முகவர்கள் ஒரே நேரத்தில் பணிகளை முடிக்க வேண்டும் என்ற சூழ்நிலைகளில்.
- **குழு உரையாடல் ஒருங்கிணைப்பு** - முகவர்கள் ஒரே பணியில் சேர்ந்து பணியாற்றும் சூழ்நிலைகளில்.
- **பணிவாங்கும் ஒருங்கிணைப்பு** - துணைப்பணிகள் முடிந்தவுடன் முகவர்கள் பணியை மாற்றிச் செய்வதில்.
- **காந்த உறுப்பு ஒருங்கிணைப்பு** - ஒரு மேலாளர் முகவர் பணிப்பட்டியலை உருவாக்கி மாற்றம் செய்வதுடன் துணை முகவர்களை ஒருங்கிணைத்து பணியை முடிப்பதில்.

தயாரிப்பு AI முகவர்களை வழங்க MAF இல் உள்ளடக்கப்பட்டுள்ள அம்சங்கள்:

- **கண்காணிப்பு** - OpenTelemetry மூலம், AI முகவரின் ஒவ்வொரு செயல்பாடும் (கருவி அழைப்பு, ஒருங்கிணைப்பு படிகள், காரணம்சார்ந்த ஓட்டங்கள் மற்றும் செயல்திறன் கண்காணிப்பு - Microsoft Foundry டாஷ்போர்ட்கள் மூலம்) கண்காணிக்கப்படுகிறது.
- **பாதுகாப்பு** - Microsoft Foundry இல் உள்ளடக்க முறையில் முகவர்களை நடுநிலைபடுத்துவதன் மூலம், வேட்பாளர் அடிப்படையிலான அணுகல், தனிப்பட்ட தரவு கையாளுதல் மற்றும் உள்ளமைவான உள்ளடக்க பாதுகாப்பு அடக்கங்கள் உள்ளன.
- **திடம்செய்தல்** - முகவர் நூல்கள் மற்றும் பணிச்சுழற்சிகள் நிறுத்தப்படவும், மீண்டும் தொடங்கவும் பிழைகள் இருந்தால் மீட்கவும் முடியும், இது நீண்ட கால செயல்பாடுகளுக்கு உதவுகிறது.
- **கட்டுப்பாடு** - மனித ஒப்புதல் தேவைப்படும் பணிகள் குறிக்கப்படும் மனித கலப்பு பணிச்சுழற்சிகள் ஆதரிக்கப்படுகிறது.

மைக்ரோசாஃப்ட் முகவர் கூறமைப்பு பின்வரும் அம்சங்களுடன் ஒத்திசைவானதாக உள்ளது:

- **மேகப்பொருள் சாராதது** - முகவர்கள் கன்டெய்னர்கள், உள்ளூர் மற்றும் பல மாக்கள் மேகங்களில் இயங்க முடியும்.
- **வழங்குபவர் சாராதது** - உங்கள் விருப்பமான SDK மூலம் முகவர்கள் உருவாக்கப்படமுடியும், அதில் Azure OpenAI மற்றும் OpenAI உள்ளது.
- **திறந்த நிலையான ஒருங்கிணைப்பு** - முகவர்கள் Agent-to-Agent (A2A) மற்றும் Model Context Protocol (MCP) போன்ற நெறிமுறைகளை பயன்படுத்தி மற்ற முகவர்கள் மற்றும் கருவிகளை கண்டுபிடித்து பயன்படு்்க்க முடியும்.
- **பிளக்கின்கள் மற்றும் இணைப்பிகள்** - Microsoft Fabric, SharePoint, Pinecone மற்றும் Qdrant போன்ற தரவு மற்றும் நினைவக சேவைகளுடன் இணைப்புகள் உருவாக்க முடியும்.

இப்போ நாம் இந்த அம்சங்கள் மைக்ரோசாஃப்ட் முகவர் கூறமைப்பின் முக்கிய கருத்துக்களில் எவ்வாறு பயன்படுகின்றன என்று பார்ப்போம்.

## மைக்ரோசாஃப்ட் முகவர் கூறமைப்பின் முக்கிய கருத்துக்கள்

### முகவர்கள்

![Agent Framework](../../../translated_images/ta/agent-components.410a06daf87b4fef.webp)

**முகவர்களை உருவாக்குதல்**

முகவர் உருவாக்கல் என்பது inference சேவையை (LLM வழங்குநர்) வரையறுத்து,
AI முகவர் பின்பற்ற வேண்டிய வழிமுறைகளின் தொகுப்பையும் மற்றும் ஒரு `name` எனும் பெயரிடலைக் குறிப்பிடுவதுமாகும்:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

மேலே `Azure OpenAI` பயன்படுத்தி உள்ளது, ஆனால் `Microsoft Foundry Agent Service` உட்பட பல்வேறு சேவைகளைப் பயன்படுத்தி முகவர்கள் உருவாக்க முடியும்:

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

அல்லது [MiniMax](https://platform.minimaxi.com/), இது பெரிய உரையாடல் சாளரங்களுடன் (204K டோக்கன்கள் வரை) OpenAI-உடை API வழங்குகிறது:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

அல்லது A2A நெறிமுறையை பயன்படுத்தி தொலை முகவர்கள்:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**முகவர்களை இயக்குதல்**

முகவர்கள் `.run` அல்லது `.run_stream` முறைகளை பயன்படுத்தி சகமில்லாத அல்லது ஓட்ட ஊர்வலம் பதில்களை இயக்கப்படுகின்றன.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ஒவ்வொரு முகவர் இயக்கமும் முகவரின் பயன்படுத்தும் `max_tokens`, அழைக்கக் கூடிய `tools` மற்றும் முகவருக்கு பயன்படுத்தப்படும் `model` போன்ற அளவுரைகள் தனிப்பயனாக்கப்படக்கூடும்.

இது பயனர் பணிகளை முடிக்க குறிப்பிட்ட மாதிரிகள் அல்லது கருவிகள் தேவைப்படும் நேரங்களில் பயனுள்ளதாக இருக்கும்.

**கருவிகள்**

கருவிகள் முகவர்களை வரையறுக்கும் போது மற்றும் முகவரைக் கையாளும் போது இரண்டும் வரையறுக்கப்பட முடியும்:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# நேரடியாக ஒரு ChatAgent உருவாக்கும் போது

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

மற்றும் முகவர்களை இயக்கும் போது:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # இந்த ஓட்டத்திற்கு மட்டும் வழங்கப்பட்ட கருவி )
```

**முகவர் நூல்கள்**

முகவர் நூல்கள் பல-திரும்பும் உரையாடல்களை கையாள பயன்படுத்தப்படுகின்றன. நூல்கள் உருவாக்கப்படுகின்றன:

- `get_new_thread()` பயன்படுத்தி, இது நூலை நேரம் கடந்து சேமிக்க உதவுகிறது
- முகவர்களை இயக்கும்போது தானாக நூல் உருவாக்கப்படும், மற்றும் நூல் தற்போதைய இயக்கத்திற்குள் மட்டுமே நிலைக்கும்.

நூல் உருவாக்க குறியீடு இதுமாறு உள்ளது:

```python
# புதிய த்ரெட்டை உருவாக்கவும்.
thread = agent.get_new_thread() # அந்த த்ரெட்டுடன் முகவரியை இயக்கவும்.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

பின்னர் நூலை சேமிக்கக்கூடிய வகையில் ஒழுங்குபடுத்து:

```python
# ஒரு புதிய துறையை உருவாக்கவும்.
thread = agent.get_new_thread() 

# அந்த துறையுடன் முகவரியை இயக்கவும்.

response = await agent.run("Hello, how are you?", thread=thread) 

# சேமிப்பிற்கு துறையை தொடர் முறைப்படுத்தவும்.

serialized_thread = await thread.serialize() 

# சேமிப்பிலிருந்து ஏற்றிய பிறகு துறை நிலையை தொடர் முறையிலிருந்து மீட்டெடுக்கவும்.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**முகவர் நடுநிலைமை**

முகவர்கள் கருவி மற்றும் LLMகளுடன் தொடர்பு கொண்டு பயனர் பணிகளை முடிக்கின்றனர். சில சூழ்நிலைகளில் இந்த தொடர்புகளுக்கு இடையில் செயல்பாடுகள் அல்லது கண்காணிப்பு தேவைப்படுகிறது. முகவர் நடுநிலைமை இது மூலம் சாத்தியமாகிறது:

* செயல்பாடு நடுநிலைமை *

இந்த நடுநிலைமை முகவரும் அழைக்கும் செயல்பாட்டிற்கும் இடையில் செயல் நடாத்துவதற்கு உதவுகிறது. உதாரணமாக, செயல்பாடு அழைப்பில் பதிவு பதிவு செய்யலாம்.

கீழ்காணும் குறியீட்டில் `next` கடைசியில் அழைக்கப்பட வேண்டியதும், அடுத்த நடுநிலைமை அல்லது செயல்பாடு இருக்கிறதோ என்பதைக் குறிப்பிடுகிறது.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # முன்-செயலாக்கம்: செயல்பாடு செயல்படுத்துவதற்கு முன் பதிவுசெய்
    print(f"[Function] Calling {context.function.name}")

    # அடுத்து உள்ள மிட்‌லுஸர் அல்லது செயல்பாடு செயல்படுத்த தொடரவும்
    await next(context)

    # பிந்தைய செயலாக்கம்: செயல்பாடு செயல்படுத்தப்பட்ட பிறகு பதிவுசெய்
    print(f"[Function] {context.function.name} completed")
```

* உரையாடல் நடுநிலைமை *

இந்த நடுநிலைமை முகவரும் LLMக்குமான கோரிக்கைகளுக்கு இடையே செயல்பாடுகள் அல்லது பதிவு செய்ய உதவுகிறது.

இதில் AI சேவைக்குக் கட்டணப்படுத்தப்படும் `messages` போன்ற முக்கிய தகவல்கள் உள்ளன.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # முன்னணி செயலாக்கம்: AI அழைப்புக்கு முன் பதிவு செய்யவும்
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # அடுத்த மிடில்வேர் அல்லது AI சேவைக்கு தொடரவும்
    await next(context)

    # பின் செயலாக்கம்: AI பதிலுக்கு பிறகு பதிவு செய்யவும்
    print("[Chat] AI response received")

```

**முகவர் நினைவகம்**

`Agentic Memory` பாடத்தில் பேசப்பட்டபோல், நினைவகம் முகவரின் பல சூழல்களில் செயல்பட உதவும் முக்கிய கூறு ஆகும். MAF பல்வேறு நினைவக வகைகளை வழங்குகிறது:

*நினைவகத்தில் சேமிப்பு*

இது பயன்பாட்டு நேரத்தில் நூல்களில் சேமிக்கப்பட்ட நினைவாகும்.

```python
# புதிய திரெட்னை உருவாக்கவும்.
thread = agent.get_new_thread() # அந்த திரெட்டுடன் முகவரியை இயக்குக.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*நிலையான செய்திகள்*

இது வெவ்வேறு அமர்வுகளில் உரையாடல் வரலாற்றை சேமிக்க பயன்படுத்தப்படும். இது `chat_message_store_factory` மூலம் வரையறுக்கப்படுகிறது:

```python
from agent_framework import ChatMessageStore

# ஒரு தனிப்பயன் செய்தி கடை உருவாக்கவும்
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*இடையில் நினைவகம்*

முகவர்கள் இயக்கப்படும் முன் சூழலுக்கு இது சேர்க்கப்படுகிறது. இது mem0 போன்ற வெளி சேவைகளில் சேமிக்கப்படலாம்:

```python
from agent_framework.mem0 import Mem0Provider

# மேம்பட்ட நினைவக திறன்களுக்கு Mem0 ஐ பயன்படுத்துதல்
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

கண்காணிப்பு நம்பகமான மற்றும் பராமரிக்கக்கூடிய முகவர் அமைப்புகளை உருவாக்க முக்கியம். MAF OpenTelemetry உடன் இணைந்து கண்காணிப்பு மற்றும் அளவைகள் வழங்குகிறது.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # எதையாவது செய்யுங்கள்
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### பணிச்சுழற்சிகள்

MAF பணிச்சுழற்சிகள் என்பதை முன்நிர்ணயிக்கப்பட்ட படிகள் அமைப்பாக வழங்குகிறது, இதில் AI முகவர்கள் கூறுகளாக இருக்கின்றனர்.

பணிச்சுழற்சிகள் கட்டுப்பாட்டை மேம்படுத்தும் வேறுபட்ட கூறுகளைக் கொண்டிருக்கின்றன. பணிச்சுழற்சிகள் **பல-முகவர் ஒருங்கிணைப்பு** மற்றும் **சேமிப்பு புள்ளிகள்** கொண்டுள்ளதாலும் பணிச்சுழற்சி நிலைகளை சேமிக்க உதவுகிறது.

பணிச்சுழற்சியின் முக்கிய கூறுகள்:

**இயக்கும் கூறுகள் (Executors)**

இயக்கும் கூறுகள் உள்ளீட்டு செய்திகளை பெற்று, ஒதுக்கப்பட்ட பணிகளைச் செய்து, வெளிப்படையான செய்தியை உருவாக்குகின்றன. இது பணிச்சுழற்சியை முன்னெடுத்து பெரிய பணியை முடிக்க உதவுகிறது. இயக்கும் கூறுகள் AI முகவரோ அல்லது தனிப்பயன் தர்க்கமாக இருக்கலாம்.

**எட்ஜ்கள்**

எட்ஜ்கள் மூலம் பணிச்சுழற்சியில் செய்திகள் ஓட்டத்தை வரையறுக்கலாம். இவை:

*நேரடி எட்ஜ்கள்* - இயக்கும் கூறுகளுக்கு இடையேயான எளிய ஒருக்கு ஒரு இணைப்புகள்:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*நிலை முறை நாட்கள்(Conditional Edges)* - குறிப்பிட்ட நிபந்தனை பூர்த்திக் செய்யும்போது செயல்படும். எடுத்துக்காட்டு, ஓட்டல்கள் கிடைக்காமை நிலைத் தோன்றும்போது, இயக்கும் கூறு மற்ற விருப்பங்களை பரிந்துரைக்கலாம்.

*மாற்று வழி எட்ஜ்கள்(Switch-case Edges)* - நிபந்தனைகளின் அடிப்படையில் செய்திகள் வேறுபட்ட இயக்கும் கூறுகளுக்கு செல்லும். உதாரணம், பயண வாடிக்கையாளர் முன்னுரிமை அணுகல் இருந்தால், அவர்களின் பணிகள் வேறு பணிச்சுழற்சியில் கையாளப்படும்.

*பகிர்தல் எட்ஜ்கள்(Fan-out Edges)* - ஒரு செய்தியை பல இலக்குகளுக்கு அனுப்பு.

*சேகரிக்கும் எட்ஜ்கள்(Fan-in Edges)* - பல இயக்கும் கூறுகளிலிருந்து செய்திகளை சேகரித்து ஒரு இலக்குக்கு அனுப்பல்.

**நிகழ்வுகள்**

பணிச்சுழற்சிகளுக்குள் மேம்பட்ட கண்காணிப்பை வழங்க MAF பின்வரும் நிகழ்வுகளை கொண்டுள்ளது:

- `WorkflowStartedEvent`  - பணிச்சுழற்சி தொடங்கப்பட்டது
- `WorkflowOutputEvent` - பணிச்சுழற்சி வெளிப்படையானதை வழங்கியது
- `WorkflowErrorEvent` - பிழை ஏற்பட்டது
- `ExecutorInvokeEvent` - இயக்கும் கூறு செயல்படுத்த தொடங்கியது
- `ExecutorCompleteEvent` - இயக்கும் கூறு செயல்பட முடித்தது
- `RequestInfoEvent` - கோரிக்கை விடுக்கப்பட்டது

## மேம்பட்ட MAF மாதிரிகள்

மேல் பகுதிகள் மைக்ரோசாஃப்ட் முகவர் கூறமைப்பின் முக்கிய கருத்துக்களை வழங்குகின்றன. மேலும் சிக்கலான முகவர்களை உருவாக்கும் போது, பின்வரும் மேம்பட்ட மாதிரிகளை பரிசீலிக்கவும்:

- **நடுநிலைமை இணைவு**: பல நடுநிலைமை கையாளுநர்களை (பதிவு, அங்கீகாரம், வீதம் கட்டுப்பாடு) செயல்பாட்டிலும் உரையாடல் நடுநிலையிலும் சங்கிலிநோக்கி இணைத்து முகவர் நடத்தைக்கு சிறந்த கட்டுப்பாடு.
- **பணிச்சுழற்சி சேமிப்பு புள்ளிகள்**: பணிச்சுழற்சி நிகழ்வுகள் மற்றும் ஒழுங்குபடுத்தல்களைப் பயன்படுத்தி நீண்ட கால முகவர் செயல்முறைகளைச் சேமித்து மறுபதிவு செய்ய.
- **மாற்றும் கருவி தேர்வு**: கருவி விளக்கங்களில் RAG ஐ ஒன்றிணைத்து MAF கருவி பதிவு மூலம் கேட்டுக்கான பொருத்தமான கருவிகளை மட்டும் வழங்க.
- **பல முகவர் பணிவாங்கல்**: பணிச்சுழற்சி எட்ஜ்கள் மற்றும் நிலை முறை மாறும் வழிகளுடன் சிறப்பு முகவர்களுக்கு பணியை மாற்ற ஒருங்கிணைக்க.

## Microsoft Foundry இல் LangChain / LangGraph முகவர்களை வைத்திருத்தல்

Microsoft Agent Framework **பகிர்ந்துகொள்ளக்கூடிய கூறமைப்பாகும்** — நீங்கள் MAF மூலம் எழுதப்பட்ட முகவர்களுக்கு மட்டுமல்ல. ஏற்கனவே **LangChain** அல்லது **LangGraph** உடன் உருவாக்கிய முகவர் இருந்தால், அதை **Microsoft Foundry வைத்திருக்கும் முகவராக** இயக்க முடியும், அப்போது Foundry இயக்க நேரம், அமர்வுகள், அளவை, அடையாள மற்றும் நெறிமுறை முடிவுகளை மேலாண்மை செய்வது, உங்கள் முகவர் தர்க்கம் LangGraph இல் இருக்கும்.

இது `langchain_azure_ai.agents.hosting` தொகுப்பால் செய்யப்படுகிறது, இது LangGraph வலைப் பெரிமாணத்தை Foundry வைத்திருக்கும் முகவர்கள் பயன்படுத்தும் ஒரே நெறிமுறைகளுக்கு வெளிக்காட்டுகிறது.

**1. hosting கூடுதல் தொகுப்பை நிறுவுக:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` கூடுதல் Foundry நெறிமுறை நூலகங்களை நிறுவுகிறது: `azure-ai-agentserver-responses` (OpenAI-உடை `/responses` முடிவு) மற்றும் `azure-ai-agentserver-invocations` (பொதுவான `/invocations` முடிவு).

**2. ஓர் வைத்திருக்கும் நெறிமுறையை தேர்ந்தெடுக்க:**

| நெறிமுறை | வைத்திருக்கும் வகுப்பு | முடிவு | எப்போது பயன்படுத்தவும் |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI-உடை உரையாடல், ஓட்ட ஊர்வலம், பதில் வரலாறு மற்றும் உரையாடல் நூல் ஆரம்பிப்பிற்கு பரிந்துரைக்கப்படும் இயல்பு. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | தனிப்பயன் JSON வடிவமைப்பு, webhook-ஒன்றான முடிவு அல்லது உரையாடல் அல்லாத செயலாக்கத்திற்கு. |

**Responses API Foundry இல் முகவர் முறையில் முதன்மை API ஆக இருப்பதால்**, பெரும்பான்மையான முகவர்களுக்கு `ResponsesHostServer` மூலம் துவங்கு.

**3. சுற்றுச் சூழல் மாறிகளைக் கட்டமைக்க (முதலில் `az login` செய்து `DefaultAzureCredential` அங்கீகாரம் பெற):**

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

முகவர் பின்னர் Foundry இல் வைத்திருக்கும் முகவராக இயங்கும்போது, தளம் `FOUNDRY_PROJECT_ENDPOINT` ஐ தானாக சேர்க்கும்.

**4. Responses நெறிமுறையில் LangGraph முகவரைக் வெளிப்படுத்த:**

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

    # ChatOpenAI இங்கு Foundry திட்டத்தின் OpenAI-ஐ பொருந்தக்கூடிய (Responses) முடிவுவாய்ச் சேவையை குறிக்கின்றது.
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

`python main.py` விட்டு உள்ளூராக இயக்கி, பின்னர் `http://localhost:8088/responses` க்கு Responses கோரிக்கை அனுப்புங்கள்.

**முக்கிய நடத்தை:**

- **உரையாடல்கள்**: வாடிக்கையாளர்கள் உரையாடலை தொடர `previous_response_id` அல்லது `conversation` ஐ வழங்குவர். உங்கள் கிராப் LangGraph சேமிப்பான் கொண்டு தொகுக்கப்பட்டிருந்தால், Foundry உரையாடல் நிலையை சேமிப்புக் கட்டுக்குள் வாங்கி கீ எடுக்கும் (தயாரிப்பில் நீடித்த சேமிப்பானது இருக்க வேண்டும்; உள்ளூரில் சோதனைக்கு `MemorySaver` சென்று விடும்).
- **மனித ஒப்புதல் உள்ளடக்கம்**: நீங்கள் LangGraph `interrupt()` ஐ பயன்படுத்தினால், `ResponsesHostServer` நிலுவை இடைமறுக்கு Responses `function_call` / `mcp_approval_request` உருப்படியை வெளிக்காட்டும், வாடிக்கையாளர்கள் பொருத்தமான `function_call_output` / `mcp_approval_response` கொண்டு மீண்டும் தொடங்குவர்.
- **Foundryக்கு விண்ணப்பி**: Azure Developer CLI பயன்படுத்துங்கள் — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (உள்ளூரில், Docker தேவை), பின்னர் `azd provision` மற்றும் `azd deploy`. Hosted-agent орналுத்தல் **Foundry Project Manager** உரிமையை தேவைப்படும்.

இந்த எடுத்துக்காட்டின் இயங்கக்கூடிய பதிப்பு [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) இல் உள்ளது. முழு அறிவுரைக்கு (Invocations நெறிமுறை, தனிப்பயன் கோரிக்கை வடிவங்கள் மற்றும் பிரச்சினை தீர்வு) [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) பார்க்கவும்.

## குறியீட்டு மாதிரிகள்

மைக்ரோசாஃப்ட் முகவர் கூறமைப்புக்கான குறியீட்டு மாதிரிகள் இந்த தொகுப்பில் `xx-python-agent-framework` மற்றும் `xx-dotnet-agent-framework` கோப்புகளில் உள்ளன.

## மைக்ரோசாஃப்ட் முகவர் கூறமைப்பைப் பற்றி மேலும் கேள்விகள் உள்ளதா?

மற்ற கற்றுள்ளவர்களைச் சந்திக்க, அலுவலக நேரங்களில் கலந்துகொள்ள மற்றும் உங்கள் AI முகவர் தொடர்பான கேள்விகளுக்கு பதில் பெற [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) இல் சேரவும்.
## முந்தய பாடம்

[AI முகவர்களின் நினைவகம்](../13-agent-memory/README.md)

## அடுத்த பாடம்

[கணினி பயன்முறை முகவர்கள் (CUA) உருவாக்கல்](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->