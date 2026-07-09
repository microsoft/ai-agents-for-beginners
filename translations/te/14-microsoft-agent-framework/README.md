# మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ అన్వేషణ

![Agent Framework](../../../translated_images/te/lesson-14-thumbnail.90df0065b9d234ee.webp)

### పరిచయం

ఈ పాఠ్యము కవర్ చేయడం జరుగుతుంది:

- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్: ముఖ్య లక్షణాల మరియు విలువ యొక్క అవగాహన  
- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క ముఖ్య సూత్రాల అన్వేషణ
- అభివృద్ధిపరుచబడిన MAF నమూనాలు: వర్క్‌ఫ్లోస్, మిడిల్‌వేర్ మరియు మెమరీ

## అభ్యాస లక్ష్యాలు

ఈ పాఠ్యాన్ని పూర్తి చేసిన తరువాత, మీరు తెలిసుకుంటారు:

- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ ఉపయోగించి ఉత్పత్తి సిద్ధమైన AI ఏజెంట్లను నిర్మించడం
- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క ప్రధాన లక్షణాలను మీ ఏజెంటిక్ ఉపయోగ సందర్భాలకు అన్వయించడం
- వర్క్‌ఫ్లోస్, మిడిల్‌వేర్ మరియు అవగాహన వంటి అభివృద్ధి చేసిన నమూనాలను ఉపయోగించడం

## కోడ్ నమూనాలు 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) కోసం కోడ్ నమూనాలు ఈ రిపాజిటరీలో `xx-python-agent-framework` మరియు `xx-dotnet-agent-framework` ఫైళ్లలో లభిస్తాయి.

## మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ అవగాహన

![Framework Intro](../../../translated_images/te/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) అనేది AI ఏజెంట్లను నిర్మించడానికి మైక్రోసాఫ్ట్ యొక్క ఐక్యమైన ఫ్రేమ్‌వర్క్. ఇది ఉత్పత్తి మరియు పరిశోధన వాతావరణాలలో కనిపించే ఏజెంటిక్ ఉపయోగానుషంగాలలో విస్తృత రకాల అవసరాలను తీర్చడానికి సరళతను అందిస్తుంది, అవి:

- **క్రమపద్ధతిలో ఏజెంట్ ఆర్కెస్ట్రేషన్** తదుపరి దశల వర్క్‌ఫ్లోస్కు అవసరమయ్యే సందర్భాలలో.
- **సమకాలిన ఆర్కెస్ట్రేషన్** ఏజెంట్లు ఒకేసారి పనులు పూర్తి చేయాల్సిన సందర్భాలలో.
- **గ్రూప్ చాట్ ఆర్కెస్ట్రేషన్** ఏజెంట్లు ఒక అనేకుల tarefa పై కలిసి పనిచేసే సందర్భాలలో.
- **హ్యాండ్ ఆఫ్ ఆర్కెస్ట్రేషన్** ఏజెంట్లు ఉపపనులను పూర్తి చేసినప్పుడు పనిని ఒకరినుంచి మరొకరికి అప్పగించే సందర్భాలలో.
- **మాగ్నెటిక్ ఆర్కెస్ట్రేషన్** ఒక మేనేజర్ ఏజెంట్ పనుల జాబితాను సృష్టించి, మార్చి ఉప ఏజెంట్లను సమన్వయం చేయడం జరిగింది.

ఉత్పత్తిలో AI ఏజెంట్లను అందించడానికి, MAF కింద లక్షణాలు ఉన్నాయి:

- **అవగాహన** OpenTelemetry ఉపయోగించి, AI ఏజెంట్ యొక్క ప్రతి చర్య, సాధన పిలుపు, ఆర్కెస్ట్రేషన్ దశలు, కారణాలు, పనితీరు గమనింపు మైక్రోసాఫ్ట్ ఫౌండ్రి డాష్‌బోర్డ్స్ ద్వారా.
- **భద్రత** మైక్రోసాఫ్ట్ ఫౌండ్రి మీద ఏజెంట్లు స్థానికంగా హోస్ట్ చేయడం, ఇందులో పాత్ర ఆధారిత యాక్సెస్, వ్యక్తిగత డేటా నిర్వహణ మరియు కంటెంట్ భద్రత ఉన్నాయి.
- **దృఢత్వం** ఏజెంట్ థ్రెడ్లు మరియు వర్క్‌ఫ్లోలు నిలిపి, పునరారం‍భించి, పొరపాట్ల నుంచి మళ్ళీ పునరుద్ధరిం చేయగలవు, దీని వల్ల దీర్ఘకాలిక ప్రాసెసింగ్ సాధ్యమవుతుంది.
- **నియంత్రణ** మానవ ఒప్పందం అవసరమైన పనుల కోసం మానవ జLoop వర్క్‌ఫ్లోలు మద్దతు పొందుతాయి.

మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ అంతర్లీన అనుసంధానంపై కూడా దృష్టి పెట్టింది:

- **క్లౌడ్-అగ్నోస్టిక్** - ఏజెంట్లు కంటైనర్లలో, ఆన్-ప్రెం మరియు వివిధ క్లౌడ్లపై నడవగలవు.
- **ప్రొవైడర్-అగ్నోస్టిక్** - మీరు ఇష్టపడే SDKలతో ఏజెంట్లు సృష్టించగలవు, వాటిలో Azure OpenAI మరియు OpenAI ఉన్నాయి.
- **ఓపెన్ ప్రమాణాల అనుసంధానం** - ఏజెంట్లు Agent-to-Agent (A2A) మరియు Model Context Protocol (MCP) వంటి ప్రోటోకాల్‌లను ఉపయోగించి ఇతర ఏజెంట్లు మరియు సాధనాలను కనుగొని ఉపయోగించగలవు.
- **ప్లగిన్లు మరియు కనెక్టర్‌లు** - మైక్రోసాఫ్ట్ ఫ్యాబ్రిక్, షేర్‌పాయింట్, పైన్కోన్ మరియు క్యూడ్‌రాంట్ వంటి డేటా మరియు మెమరీ సేవలకి కనెక్షన్స్ ఏర్పరచవచ్చు.

ఇక్కడ వీటిని మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క కొన్ని ప్రధాన సూత్రాలకు ఎలా వర్తించబడతాయో చూద్దాం.

## మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ ముఖ్య సూత్రాలు

### ఏజెంట్లు

![Agent Framework](../../../translated_images/te/agent-components.410a06daf87b4fef.webp)

**ఏజెంట్లు సృష్టించడం**

ఏజెంట్ సృష్టి అనేది ఇన్ఫరెన్స్ సర్వీస్ (LLM ప్రొవైడర్), AI ఏజెంట్ అనుసరించాల్సిన ఆదేశాలు మరియు `name` అనే పేరును నిర్వచించడం ద్వారా జరగుతుంది:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

పై కోడ్ లో `Azure OpenAI` ఉపయోగిస్తున్నారు, కానీ ఏజెంట్లు వివిధ సేవలతో సహా `Microsoft Foundry Agent Service` ఉపయోగించి సృష్టించవచ్చు:

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

లేదా [MiniMax](https://platform.minimaxi.com/) ఉపయోగించి, ఇది OpenAI అనుకూల API మరియు పెద్ద కాంటెక్ట్ విండోస్ (204K టోకెన్స్ వరకు) కలిగి ఉంది:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

లేదా A2A ప్రోటోకాల్ ఉపయోగించి రిమోట్ ఏజెంట్లు:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ఏజెంట్లను నడపడం**

ఏజెంట్లు `.run` లేదా `.run_stream` పద్ధతులతో నడపబడతాయి, వీటిలో స్ట్రీమింగ్ లేదా غیر స్ట్రీమింగ్ ప్రతిస్పందనలకు ఉద్దేశించబడ్డాయి.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ప్రతి ఏజెంట్ రన్ కోసం `max_tokens`, ఏజెంట్ పిలవగల `tools`, మరియు ఏజెంట్ ఉపయోగించే `model` వంటి పారామీటర్లను అనుకూలీకరించడానికి ఎంపికలు అందుబాటులో ఉంటాయి.

ఇది వినియోగదారుని పని చివరితీరు పూర్తి చేయడానికి ప్రత్యేక నమూనాలు లేదా సాధనాలు అవసరమైన సందర్భాలలో ఉపయోగకరంగా ఉంటుంది.

**సాధనాలు (Tools)**

ఏజెంట్ నిర్వచించేటప్పుడు సాధనాలను నిర్వచించవచ్చు:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent ని నేరుగా సృష్టించినప్పుడు

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

అలాగే ఏజెంట్ నడిపేటప్పుడు కూడా:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ఈ ప్రదర్శన కోసం మాత్రమే అందించిన సాధనం )
```

**ఏజెంట్ థ్రెడ్లు**

ఏజెంట్ థ్రెడ్లు బహుళ సంభాషణలను నిర్వహించడానికి ఉపయోగిస్తారు. థ్రెడ్లు క్రింది విధంగా సృష్టించవచ్చు:

- `get_new_thread()` ఉపయోగించడం ద్వారా, ఇది థ్రెడ్‌ను కాలానుగుణంగా సేవ్ చేయడానికి సహాయపడుతుంది
- ఏజెంట్ నడిపేటప్పుడు ఆటోమేటిక్‌గా థ్రెడ్ సృష్టించడం, ఇది ప్రస్తుత రన్ సమయంలో మాత్రమే ఉంటుంది.

థ్రెడ్ సృష్టించడానికి కోడ్ ఇలాగే ఉంటుంది:

```python
# కొత్త థ్రెడ్‌ను సృష్టించండి.
thread = agent.get_new_thread() # ఆజెంట్‌ను థ్రెడ్‌తో నడపండి.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

తరువాత దీనిని సేవ్ చేయడానికి థృడ్‌ను సీరియలైజ్ చేయవచ్చు:

```python
# ఒక కొత్త థ్రెడ్‌ను సృష్టించండి.
thread = agent.get_new_thread() 

# థ్రెడ్‌తో ఏజెంట్‌ను నడపండి.

response = await agent.run("Hello, how are you?", thread=thread) 

# నిల్వ కోసం థ్రెడ్‌ను సిరియలైజ్ చేయండి.

serialized_thread = await thread.serialize() 

# నిల్వ నుండి లోడ్ చేసిన తర్వాత థ్రెడ్ స్థితిని డిసిరియలైజ్ చేయండి.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ఏజెంట్ మిడిల్‌వేర్**

ఏజెంట్లు సాధనాలు మరియు LLMలతో సంబంధం కలిగి వినియోగదారుల పనులను పూర్తి చేస్తాయి. కొన్ని సందర్భాలలో, ఈ పరస్పర చర్యల మధ్య లోపల అమలు చేయాలనిపిస్తే లేదా ట్రాక్ చేయాలనిపిస్తే, ఏజెంట్ మిడిల్‌వేర్ ద్వారా ఇది సాధ్యమవుతుంది:

*ఫంక్షన్ మిడిల్‌వేర్*

ఈ మిడిల్‌వేర్ ఏజెంట్ మరియు ఫంక్షన్/సాధనం మధ్య చర్యను అమలు చేయడానికి అనుమతిస్తుంది. ఉదాహరణకు, మీరు ఫంక్షన్ కాల్‌పై కొన్ని లాగింగ్ చేయాలనుకున్నప్పుడు ఉపయోగపడుతుంది.

క్రింద కోడ్ లో `next` భావం మిడిల్‌వేర్ లేదా అసలు ఫంక్షన్ ఎవరిని పిలవాలో నిర్వచిస్తుంది.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ముందస్తు ప్రాసెసింగ్: ఫంక్షన్ అమలుకు ముందు లాగ్ చేయండి
    print(f"[Function] Calling {context.function.name}")

    # తదుపరి మిడిల్వేర్ లేదా ఫంక్షన్ అమలుకు కొనసాగించండి
    await next(context)

    # అనంతర ప్రాసెసింగ్: ఫంక్షన్ అమలుకు తర్వాత లాగ్ చేయండి
    print(f"[Function] {context.function.name} completed")
```

*చాట్ మిడిల్‌వేర్*

ఈ మిడిల్‌వేర్ ఏజెంట్ మరియు LLM మధ్య అభ్యర్థనలు మధ్య చర్యను అమలు చేయడానికి లేదా లాగ్ చేయడానికి అనుమతిస్తుంది.

ఇందులో AI సేవకు పంపబడుతున్న `messages` వంటి ముఖ్య సమాచారం ఉంటుంది.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ముందస్తు ప్రాసెసింగ్: AI కాల్‌కి ముందు లాగ్ చేయండి
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # తదుపరి మిడిల్వేర్ లేదా AI సేవకు కొనసాగండి
    await next(context)

    # తర్వాతి ప్రాసెసింగ్: AI స్పందన తర్వాత లాగ్ చేయండి
    print("[Chat] AI response received")

```

**ఏజెంట్ మెమరీ**

`Agentic Memory` పాఠ్యంలో చెప్పినట్టు, మెమరీ ఏజెంట్‌ను వివిధ సందర్భాలలో పనిచేయడానికి అనుమతించే ఒక ముఖ్య భాగం. MAF వేర్వేరు రకాల మెమరీలను అందిస్తుంది:

*ఇన్-మెమరీ స్టోరేజ్*

ఇది అప్లికేషన్ రన్‌టైమ్ లో థ్రెడ్లలో నిల్వ చేసే మెమరీ.

```python
# ఒక కొత్త థ్రెడ్ సృష్టించండి.
thread = agent.get_new_thread() # ఆథర్ని థ్రెడ్ తో నడపండి.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*స్థిరమైన సందేశాలు*

విభిన్న సెషన్లలో సంభాషణ చరిత్ర నిల్వ చేయడానికి ఈ మెమరీ ఉపయోగించబడుతుంది. ఇది `chat_message_store_factory` ఉపయోగించి నిర్వచించబడింది:

```python
from agent_framework import ChatMessageStore

# కస్టమ్ మెసేజి స్టోర్ రూపొందించండి
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*డైనమిక్ మెమరీ*

ఏజెంట్లు నడపడంలో ముందు ఈ మెమరీని సందర్భంలో చేర్చేరు. ఈ మెమరీలు mem0 వంటి బాహ్య సేవల్లో నిల్వ చేయబడవచ్చు:

```python
from agent_framework.mem0 import Mem0Provider

# మెమ్0 ను అధునాతన మెమరీ సామర్థ్యాల కోసం ఉపయోగించడం
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

**ఏజెంట్ అవగాహన**


విశ్లేషణ అనేది విశ్వసనీయమైన మరియు నిర్వహించదగిన ఏజెంటిక్ వ్యవస్థలను నిర్మించడంలో ముఖ్యమైనది. మెఫ్ త్రేసింగ్ మరియు మెటర్ల కోసం మెరుగైన విశ్లేషణను అందించడానికి OpenTelemetryని అనుసంధానిస్తుంది.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ఏదైనా చేయండి
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### వర్క్‌ఫ్లో‌లు

మెఫ్ పని పూర్తి చేయడానికి ముందుగా నిర్వచించిన చర్యలుగా వర్క్‌ఫ్లోలను అందిస్తుంది మరియు ఆ చర్యలలో AI ఏజెంట్లను భాగాలుగా కలిగి ఉంటుంది.

వర్క్‌ఫ్లో‌లు మెరుగైన నియంత్రణ ప్రవాహం కోసం వివిధ భాగాలతో కూడి ఉంటాయి. వర్క్‌ఫ్లో‌లు కూడా **బహుఎజెంటు సమన్వయం** మరియు **చెక్‌పాయింటింగ్**ని ఉపయోగించి వర్క్‌ఫ్లో స్థితులను సురక్షితంగా నిల్వ చేస్తాయి.

వర్క్‌ఫ్లో యొక్క ముఖ్య భాగాలు ఇవి:

**ఎగ్జిక్యూటర్లు**

ఎగ్జిక్యూటర్లు ఇన్పుట్ సందేశాలను స్వీకరిస్తాయి, వాటికి కేటాయించిన పనులను నిర్వహిస్తూ, తరువాత అవుట్‌పుట్ సందేశాన్ని ఉత్పత్తి చేస్తాయి. ఇది పెద్ద పనిని పూర్తి చేసేందుకు వర్క్‌ఫ్లోని ముందుకు తీసుకుపోతుంది. ఎగ్జిక్యూటర్లు AI ఏజెంట్ లేదా కస్టమ్ లాజిక్ కాకూ ఉండవచ్చు.

**ఎడ్జిలు**

వర్క్‌ఫ్లోలో సందేశాల ప్రవాహాన్ని నిర్వచించడానికి ఎడ్జిలు ఉపయోగిస్తారు. ఇవి ఇలా ఉండవచ్చు:

*డైరెక్ట్ ఎడ్జిలు* - ఎగ్జిక్యూటర్ల మధ్య సులభమైన ఒకటి-కు-ఒకటి కనెక్షన్లు:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*కండిషనల్ ఎడ్జిలు* - ఒక నిర్దిష్ట షరతు చేరిన తరువాత ప్రారంభమవుతాయి. ఉదాహరణకు, హోటల్ గదులు లభించకపోవడమైతే, ఎగ్జిక్యూటర్ ఇతర ఎంపికలను సూచించవచ్చు.

*స్విచ్-కేస్ ఎడ్జిలు* - నిర్వచించబడిన షరతుల పై ఆధారపడి సందేశాలను వేరే ఎగ్జిక్యూటర్లకు మార్గదర్శనం చేస్తాయి. ఉదాహరణకు, ప్రయాణ కస్టమర్ ప్రాధాన్యత కలిగి ఉంటే, వారి పనులను మరో వర్క్‌ఫ్లో ద్వారా నిర్వహిస్తారు.

*ఫ్యాన్-ఔట్ ఎడ్జిలు* - ఒక సందేశాన్ని బహుళ లక్ష్యాలకు పంపుతాయి.

*ఫ్యాన్-ఇన్ ఎడ్జిలు* - వేర్వేరు ఎగ్జిక్యూటర్ల నుండి బహుళ సందేశాలను సేకరించి ఒక లక్ష్యానికి పంపుతాయి.

**ఈవెంట్లు**

వర్క్‌ఫ్లోలలో మెరుగైన విశ్లేషణ కోసం, మెఫ్‌లో ఈవెంట్లు అమలు చేయబడతాయి, ఉదాహరణకిరీతిగా:

- `WorkflowStartedEvent` - వర్క్‌ఫ్లో అమలును ప్రారంభిస్తుంది
- `WorkflowOutputEvent` - వర్క్‌ఫ్లో అవుట్‌పుట్ ఉత్పత్తి చేస్తుంది
- `WorkflowErrorEvent` - వర్క్‌ఫ్లో లో తప్పు సంభవించింది
- `ExecutorInvokeEvent` - ఎగ్జిక్యూటర్ ప్రాసెసింగ్ ప్రారంభిస్తుంది
- `ExecutorCompleteEvent` - ఎగ్జిక్యూటర్ ప్రాసెసింగ్ ముగుస్తుంది
- `RequestInfoEvent` - ఒక అభ్యర్థన విడుదల చేయబడింది

## అభివృద్ధి చెందిన మెఫ్ నమూనాలు

పై విభాగాలు Microsoft Agent Framework యొక్క ముఖ్యమైన సంప్రదాయాలను కవర్ చేస్తాయి. మీరు ఇంకా సంక్లిష్ట ఏజెంట్లను నిర్మించినప్పుడు, పరిగణించాల్సిన కొన్ని అభివృద్ధి చెందిన నమూనాలు ఇవి:

- **మిడిల్వేర్ సమ్మేళనం**: ఏజెంట్ ప్రవర్తనపై సున్నితమైన నియంత్రణ కోసం ఫంక్షన్ మరియు చాట్ మిడిల్వేర్ ఉపయోగించి (లాగింగ్, అథెంట్, రేట్-లిమిటింగ్) బహుళ మిడిల్వేర్ హ్యాండ్లర్లను లంకెచేయండి.
- **వర్క్‌ఫ్లో చెక్పాయింటింగ్**: వర్క్‌ఫ్లో ఈవెంట్లు మరియు సీరియలైజేషన్‌ను ఉపయోగించి దీర్ఘకాల ఏజెంట్ ప్రాసెస్‌లను నిల్వ చేసి తిరిగి ప్రారంభించండి.
- **డైనమిక్ టూల్ ఎంపిక**: టూల్ వివరణలపై RAGని మరియు మెఫ్ యొక్క టూల్ రిజిస్ట్రేషన్‌ను కలుపుకుని ప్రశ్నకు సంబంధించిన టూల్‌లను మాత్రమే అందించండి.
- **బహుఎజెంటు హ్యాండ్అఫ్**: ప్రత్యేక ఏజెంట్ల మధ్య హ్యాండ్అఫ్లను సమన్వయించడానికి వర్క్‌ఫ్లో ఎడ్జిలు మరియు కండిషనల్ మార్గదర్శకాన్ని ఉపయోగించండి.

## Microsoft Foundryపై LangChain / LangGraph ఏజెంట్ల ఆతిథ్యం

Microsoft Agent Framework **ఫ్రేమ్‌వర్క్-ఇంటరొపరబుల్** — మీరు మెఫ్ తో రాయబడిన ఏజెంట్లతో మాత్రమే పరిమితం కాదు. మీరు ఇప్పటికే **LangChain** లేదా **LangGraph**తో ఏజెంట్ నిర్మించి ఉంటే, మీరు దాన్ని **Microsoft Foundry ఆతిథ్యఏజెంట్**గా నడుపవచ్చు, తద్వారా Foundry రన్‌టైమ్, సెషన్లు, స్కేలింగ్, ఐడెంటిటీ మరియు ప్రోటోకాల్ ఎండ్పాయింట్లను నిర్వహిస్తుంది, మీ ఏజెంట్ లాజిక్ LangGraphలోనే ఉంటుంది.

ఇది `langchain_azure_ai.agents.hosting` ప్యాకేజీతో చేయబడుతుంది, ఇది సమాన ప్రోటోకాల్స్ ఉపయోగించే Foundry ఆతిథ్య ఏజెంట్లపై కంపైల్ అయిన LangGraph గ్రాఫ్‌ను తెలియజేస్తుంది.

**1. హోస్టింగ్ ఎక్స్‌ట్రా ఇన్‌స్టాల్ చేయండి:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` ఎక్స్‌ట్రా Foundry ప్రోటోకాల్ లైబ్రరీస్‌ను ఇన్‌స్టాల్ చేస్తుంది: `azure-ai-agentserver-responses` (OpenAI-తోడరישראొ /responses ఎండ్పాయింట్) మరియు `azure-ai-agentserver-invocations` (సాధారణ /invocations ఎండ్పాయింట్).

**2. హోస్టింగ్ ప్రోటోకాల్ ఎంచుకోండి:**

| ప్రోటోకాల్ | హోస్ట్ క్లాస్ | ఎండ్పాయింట్ | వాడే సందర్భం |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | మీరు OpenAI సమానమైన చాట్, స్ట్రీమింగ్, స్పందన చరిత్ర మరియు సంభాషణ థ్రెడింగ్ కోరుతున్నప్పుడు — సంభాషణాత్మక ఏజెంట్లకు సిఫార్సు చేయబడిన డిఫాల్ట్. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | మీరు కస్టమ్ JSON ఆకారం, వెబ్‌హుక్-శైలీ ఎండ్పాయింట్ లేదా అసంభాషణ తరగతి ప్రాసెసింగ్ అవసరం ఉన్నప్పుడు. |

ఎందుకంటే **Responses API Foundryలో ఏజెంట్-శైలి అభివృద్ధికి ప్రధాన API**, కాబట్టి చాలా ఏజెంట్లకు `ResponsesHostServer`తో ప్రారంభించండి.

**3. ఎన్విరాన్‌మెంట్ వేరియబుల్స్ కాన్ఫిగర్ చేయండి** (`az login` మొదట తీసుకోండి కాబట్టి `DefaultAzureCredential` చెలామణీ చేయగలదు):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

ఏజెంట్ తర్వాత Foundryలో హోస్టెడ్ ఏజెంట్‌గా నడుస్తున్నప్పుడు, ప్లాట్‌ఫారమ్ స్వయంచాలకంగా `FOUNDRY_PROJECT_ENDPOINT`ను ఇంజెక్ట్ చేస్తుంది.

**4. Responses ప్రోటోకాల్ ద్వారా LangGraph ఏజెంట్ ను ప్రదర్శించండి:**

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

    # ChatOpenAI ఇక్కడ Foundry ప్రాజెక్ట్ యొక్క OpenAI-అనుకూలమైన (Responses) ఎండ్‌పాయింట్‌ను లక్ష్యంగా పెట్టుకుంది.
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

దీన్ని స్థానికంగా `python main.py`తో నడపండి, ఆపై `http://localhost:8088/responses`కు Responses అభ్యర్థన పంపండి.

**ముఖ్య ప్రవర్తనలు:**

- **సంభాషణలు**: క్లైయింట్లు `previous_response_id` లేదా `conversation` IDని పంపుతూ సంభాషణను కొనసాగిస్తాయి. మీ గ్రాఫ్ LangGraph చెక్పాయింటర్‌తో కంపైల్ అయితే, Foundry సంభాషణ స్థితిని చెక్పాయింట్ కి కీలు ఇస్తుంది (ప్రొడక్షన్‌లో దృఢమైన చెక్పాయింటర్ ఉపయోగించండి; స్థానిక పరీక్షల కోసం `MemorySaver` సరిపోతుంది).
- **మానవ-ఇన్-ది-లూప్**: మీ గ్రాఫ్ LangGraph `interrupt()` ఉపయోగిస్తే, `ResponsesHostServer` పెండింగ్ ఇంటరప్ట్‌ను Responses `function_call` / `mcp_approval_request` అంశంగా ప్రదర్శిస్తుంది, మరియు క్లైయింట్లు సరిపోయే `function_call_output` / `mcp_approval_response`తో కొనసాగుతాయి.
- **Foundryకు పంపిణీ చేయండి**: Azure Developer CLI ఉపయోగించండి — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (స్థానికంగా, Docker అవసరం), ఆపై `azd provision` మరియు `azd deploy`. హోస్టెడ్-ఏజెంట్ పంపిణీకి **Foundry ప్రాజెక్ట్ మేనేజర్** పాత్ర అవసరం.

ఈ ఉదాహరణ యొక్క నడిపే వెర్షన్ [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)లో ఉంది. పూర్తి కార్యకలాపాల కోసం (Invocations ప్రోటోకాల్, కస్టమ్ అభ్యర్థన స్కీమాలు, సమస్యల పరిష్కారం) [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) చూడండి.

## కోడ్ నమూనాలు

Microsoft Agent Framework కోడ్ నమూనాలు ఈ రిపోజిటరీలో `xx-python-agent-framework` మరియు `xx-dotnet-agent-framework` ఫైళ్లలో నన్ను లభిస్తాయి.

## Microsoft Agent Framework గురించి మరింత ప్రశ్నలు ఉన్నాయా?

ఇతర అభ్యాసకులతో 만나ునేందుకు, ఆఫీస్ గంటల్లో పాల్గొనటానికి మరియు మీ AI ఏజెంట్ల ప్రశ్నలకు సమాధానాలు పొందటానికి [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)లో చేరండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->