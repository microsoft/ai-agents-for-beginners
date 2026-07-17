# మైക്രోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ అన్వేషణ

![ఏజెంట్ ఫ్రేమ్‌వర్క్](../../../translated_images/te/lesson-14-thumbnail.90df0065b9d234ee.webp)

### పరిచయం

ఈ పాఠం కింద చూపబడుతుంది:

- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ అర్థం చేసుకోవడం: ముఖ్య గుణాలు మరియు విలువ  
- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క కీలక భావనలను అన్వేషించడం
- అధునాతన MAF నమూనాలు: వర్క్‌ఫ్లోల్స్, మధ్యస్థం, మరియు మెమొరీ

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం పూర్తి చేసిన తర్వాత మీరు ఎలా చేయాలో తెలుసుకుంటారు:

- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ ఉపయోగించి ప్రొడక్షన్ రెడీ AI ఏజెంట్లను నిర్మించడానికి
- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క ప్రధాన లక్షణాలను మీ ఏజెంటిక్ ఉపయోగ కేసులకు వర్తింపజేయడానికి
- వర్క్‌ఫ్లోల్స్, మధ్యస్థం, మరియు పరిశీలన సహా అధునాతన నమూనాలను ఉపయోగించడానికి

## కోడ్ నమూనాలు

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) కు సంబంధించిన కోడ్ నమూనాలు ఈ రిపోజిటరీలో `xx-python-agent-framework` మరియు `xx-dotnet-agent-framework` ఫైళ్లలో లభిస్తాయి.

## మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ అర్థం చేసుకోవడం

![ఫ్రేమ్‌వర్క్ పరిచయం](../../../translated_images/te/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) అనేది AI ఏజెంట్లను నిర్మించడానికి మైక్రోసాఫ్ట్ యొక్క ఏకీకృత ఫ్రేమ్‌వర్క్. ఇది ప్రొడక్షన్ మరియు పరిశోధనా వాతావరణాల్లో కనిపించే విభిన్న ఏజెంటిక్ ఉపయోగ కేసులను పరిష్కరించడానికి అనువైన విధంగా రూపొందించబడింది:

- **అనుక్రమ దశల ఏజెంట్ కార్యాచరణ** అర్ధం, ఎక్కడ దశల వారీగా వర్క్‌ఫ్లో అవసరం.
- **సమన్వయం కార్యాచరణ** ఎక్కడ ఏజెంట్లు ఏ పనులను ఒకదానితో ఒకటి పూర్తి చేయాలి.
- **గ్రూప్ చాట్ కార్యాచరణ** ఎక్కడ ఏజెంట్లు ఒకే పని మీద కలిసి పనిచేయవచ్చు.
- **హ్యాండ్ ఆఫ్ కార్యాచరణ** ఎక్కడ ఏజెంట్లు ఉపపనులను పూర్తిచేసి పనిని ఒకరినుంచి మరొకరు స్వీకరించాలి.
- **మాగ్నెటిక్ కార్యాచరణ** ఎక్కడ మేనేజర్ ఏజెంట్ ప‌ని జాబితా సృష్టించి మార్పులు చేస్తాడు, మరియు ఉపఏజెంట్ల సమన్వయం నిర్వహిస్తుంది.

ప్రొడక్షన్‌లో AI ఏజెంట్లను అందించడానికి, MAF ఈ లక్షణాలను కూడా కలిగి ఉంది:

- **పరిశీలన** OpenTelemetry ఉపయోగించి, AI ఏజెంట్ పనులన్నీ, టూల్ కాల్‌లు, కార్యాచరణ దశలు, తర్కం ప్రవాహాలు మరియు Microsoft Foundry డాష్‌బోర్డ్ల ద్వారా పనితీరు గమనింపునిచ్చుట.
- **భద్రత** Microsoft Foundryలో ఏజెంట్లను స్వదేశీగా హోస్ట్ చేయడం, అందులో పాత్ర ఆధారిత ఆక్సెస్, వ్యక్తిగత డేటా నిర్వహణ మరియు నిర్మిత కంటెంట్ సేఫ్టీ వంటి భద్రత నియంత్రణలు ఉన్నాయి.
- **దృఢత్వం** ఏజెంట్ థ్రెడ్లు మరియు వర్క్‌ఫ్లోలు విరామం, పునఃప్రారంభం మరియు లోపాల నుండి పునరుద్ధరణ చేయగలవు, దీని వలన పొడుదూరం పని జరగగలదు.
- **నియంత్రణ** మానవ-మధ్యవర్తిత్వం వర్క్‌ఫ్లోలు మద్దతు ఇస్తాయి, ఎక్కడ పనులను మానవ ఆమోదం అవసరమని గుర్తించబడతాయి.

మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ అంతర్లీనంగా ప‌ని చేయనీయడానికి కూడా కేంద్రీకృతమై ఉంది:

- **క్లౌడ్-నిరపేక్షంగా ఉండటం** - ఏజెంట్లు కంటైనర్లలో, లోకల్ సిస్టమ్స్ మరియు వివిధ క్లౌడ్లలో నడవగలవు.
- **ప్రొవైడర్-నిరపేక్షంగా ఉండటం** - ఏజెంట్లు Azure OpenAI మరియు OpenAI సహా మీ ఇష్టమైన SDKల ద్వారా సృష్టించబడవచ్చు.
- **ఓపెన్ స్టాండర్డ్స్ ఇంటిగ్రేషన్** - ఏజెంట్లు Agent-to-Agent (A2A) మరియు Model Context Protocol (MCP) వంటి ప్రోటోకాల్‌లను ఉపయోగించి ఇతర ఏజెంట్లు మరియు టూల్స్ కనుగొని ఉపయోగించగలవు.
- **ప్లగిన్లు మరియు కనెక్టర్స్** - Microsoft Fabric, SharePoint, Pinecone మరియు Qdrant వంటి డేటా మరియు మెమరీ సర్వీసులకు కనెక్షన్లు చేయవచ్చు.

మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క కొన్ని ప్రధాన భావనలకు ఈ లక్షణాలు ఎలా వర్తించబడ్డాయో చూద్దాము.

## మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క కీలక భావనలు

### ఏజెంట్లు

![ఏజెంట్ ఫ్రేమ్‌వర్క్](../../../translated_images/te/agent-components.410a06daf87b4fef.webp)

**ఏజెంట్ల సృష్టి**

ఏజెంట్ సృష్టి అనేది ఈన్ఫరెన్స్ సేవ (LLM ప్రొవైడర్), AI ఏజెంట్ అనుసరించే సూచనసమూహం, మరియు ఒక కేటాయించిన `name` నిర్వచించడం ద్వారా జరుగుతుంది:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

పై ఉదాహరణలో `Azure OpenAI` ఉపయోగించబడింది, కానీ ఏజెంట్లు వివిధ సేవలతో సృష్టించవచ్చు, ఉదా: `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIలు

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

లేదా [MiniMax](https://platform.minimaxi.com/), ఇది OpenAI అనుకూల API, పెద్ద కాంటెక్స్ట్ విండోస్‌తో (204K టోకెన్ల వరకు):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

లేదా A2A ప్రోటోకాల్ ఉపయోగించి రిమోట్ ఏజెంట్లు:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ఏజెంట్ల‌ను నడపడం**

ఏజెంట్లు `.run` లేదా `.run_stream` విధానాలను ఉపయోగించి నాన్-స్ట్రిమింగ్ లేదా స్ట్రీమింగ్ ప్రత్యుత్తరాల కోసం నడపబడతాయి.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ప్రతి ఏజెంట్ రన్ కూడా ఏజెంట్ ఉపయోగించే `max_tokens`, ఏజెంట్ కాల్ చేయగల `tools`, మరియు ఏజెంట్ కోసం ఉపయోగించే `model` ని అనుకూలీకరించే ఎంపికలు కలిగివుండవచ్చు.

ఇది వినియోగదారు పనిని పూర్తి చేయడానికి ప్రత్యేక మోడల్స్ లేదా టూల్స్ అవసరమయ్యే సందర్భాలలో ఉపయోగపడుతుంది.

**టూల్స్**

ఏజెంట్ నిర్వచించే సమయం మరియు ఏజెంట్ నడపడంలో టూల్స్ నిర్వచించవచ్చు:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# చాట్ఎజెంట్‌ను ప్రత్యక్షంగా సృష్టించినప్పుడు

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

మరియు ఏజెంట్ నడుపుతున్నపుడు:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ఈ రన్ కోసం మాత్రమే అందిస్తున్న సాధనం )
```

**ఏజెంట్ థ్రెడ్లు**

ఏజెంట్ థ్రెడ్లు బహుళ-తిరుగుబాటు సంభాషణలను నిర్వహించడానికి ఉపయోగిస్తారు. థ్రెడ్లను క్రింది విధంగా సృష్టించవచ్చు:

- `get_new_thread()` ఉపయోగించడం, ఇది థ్రెడ్‌ని కాలక్రమేణ సేకరించడానికి అనుమతిస్తుంది
- ఏజెంట్ నడపబడేటప్పుడు ఆటోమేటిక్ గా థ్రెడ్ సృష్టించడం, ఆ థ్రెడ్ ప్రస్తుత రన్ సమయంలో మాత్రమే ఉంటుంది.

థ్రెడ్ సృష్టించడానికి కోడ్ ఇలా ఉంటుంది:

```python
# ఒక కొత్త థ్రెడ్ను సృష్టించండి.
thread = agent.get_new_thread() # థ్రెడ్తో ఏజెంట్‌ని నడపండి.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

తర్వాత మీరు థ్రెడ్‌ను సీరియలైజ్ చేసి భవిష్యత్తులో ఉపయోగం కోసం నిల్వ చేయవచ్చు:

```python
# కొత్త త్రెడ్‌ని సృష్టించండి.
thread = agent.get_new_thread() 

# త్రెడ్‌తో కూడుకొని ఏజెంట్‌ను నడిపించండి.

response = await agent.run("Hello, how are you?", thread=thread) 

# నిల్వ కోసం త్రెడ్‌ను సీరియలైజ్ చేయండి.

serialized_thread = await thread.serialize() 

# నిల్వ నుండి లోడ్ చేసిన తర్వాత త్రెడ్ స్థితిని డీసీరియలైజ్ చేయండి.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ఏజెంట్ మధ్యస్థం**

ఏజెంట్లు టూల్స్ మరియు LLMలతో కలిసి వినియోగదారు పనులను పూర్తిచేస్తాయి. కొన్ని సందర్భాలలో, ఈ పరస్పర చర్యల్లో మధ్యలో పని చేయడం లేదా ట్రాక్ చేయడం అవసరం. ఏజెంట్ మధ్యస్థం దీన్ని ఇ వీలా అనుమతిస్తుంది:

*ఫంక్షన్ మధ్యస్థం*

ఈ మధ్యస్థం ఏజెంట్ మరియు దీని పిలిచే ఫంక్షన్/టూల్ మధ్య చర్యను అమలు చేయడానికి అనుమతిస్తుంది. ఉదాహరణకి, ఫంక్షన్ కాల్‌పై లాగ్ చేయడం కావచ్చు.

కింద ఇచ్చిన కోడ్‌లో `next` అనేది తర్వాతి middleware లేదా అసలు ఫంక్షన్‌ను పిలవలేదా అనేది నిర్ణయిస్తుంది.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ప్రీ-ప్రాసెసింగ్: ఫంక్షన్ అమలు ముందు లాగ్ చేయండి
    print(f"[Function] Calling {context.function.name}")

    # తదుపరి మిడిల్వేర్ లేదా ఫంక్షన్ అమలు కొనసాగించండి
    await next(context)

    # పోస్ట్-ప్రాసెసింగ్: ఫంక్షన్ అమలు తరువాత లాగ్ చేయండి
    print(f"[Function] {context.function.name} completed")
```

*చాట్ మధ్యస్థం*

ఈ middleware ఏజెంట్ మరియు LLM మధ్య అభ్యర్థనల మధ్య చర్యను అమలు లేదా లాగ్ చేయడానికి అనుమతిస్తుంది.

దీనిలో AI సేవకు పంపించే `messages` వంటి ముఖ్యమైన సమాచారముంటుంది.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ముందు ప్రాసెసింగ్: AI కాల్ ముందు లాగ్
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # తదుపరి మిడిల్‌వేర్ లేదా AI సేవకు కొనసాగించండి
    await next(context)

    # తర్వాత ప్రాసెసింగ్: AI స్పందన తర్వాత లాగ్
    print("[Chat] AI response received")

```

**ఏజెంట్ మెమరీ**

`Agentic Memory` పాఠంలో చర్చించినట్లు, మెమరీ ఏజెంట్ వివిధ కాంటెక్స్ట్‌లపై పనిచేయడానికి కీలక అంశం. MAF వివిధ రకాల మెమరీలను అందిస్తుంది:

*ఇన్-మెమరీ నిల్వ*

ఇది అర్జీలో స్వయంచాలకంగా నిల్వ అయ్యే థ్రెడ్లలోని మెమరీ.

```python
# ఒక కొత్త థ్రెడ్‌ను సృష్టించండి.
thread = agent.get_new_thread() # ఆ థ్రెడ్‌తో ఏజెంట్‌ను నడపండి.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*స్థిర సందేశాలు*

ఈ మెమరీ విభిన్న సెషన్స్ మధ్య సంభాషణ చరిత్ర నిల్వ చేసేటప్పుడు ఉపయోగిస్తారు. ఇది `chat_message_store_factory` వాడకం ద్వారా నిర్వచించబడుతుంది:

```python
from agent_framework import ChatMessageStore

# ఒక కస్టమ్ సందేశాల నిల్వను సృష్టించండి
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*డైనమిక్ మెమరీ*

ఈ మెమరీ ఏజెంట్లు నడిపే ముందు కాంటెక్స్ట్‌కు జోడించబడుతుంది. ఈ మెమరీలు mem0 వంటి బాహ్య సేవలలో నిల్వ చేయవచ్చు:

```python
from agent_framework.mem0 import Mem0Provider

# మెమ్0ను అధునాతన మెమరీ సామర్థ్యాల కోసం ఉపయోగించడం
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

**ఏజెంట్ పరిశీలన**

ఏజెంటిక్ వ్యవస్థలను విశ్వసనీయంగా మరియు నిర్వహించదగినట్లుగా నిర్మించడానికి పరిశీలన ముఖ్యం. MAF OpenTelemetry తో యాక్సెస్ ఇవ్వడం ద్వారా మంచి పరిదర్శన కోసం ట్రేసింగ్ మరియు మీటర్లను అందిస్తుంది.

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

### వర్క్‌ఫ్లోలు

MAF వర్క్‌ఫ్లోలను అందిస్తుంది, ఇవి ఒక పని పూర్తి చేయడానికి ముందుగా నిర్వచించబడ్డ దశలు మరియు ఆ దశల్లో AI ఏజెంట్లను భాగాలుగా ఉంటాయి.

వర్క్‌ఫ్లోలు వివిధ భాగాల కలయికతో కూడి, మెరుగైన నియంత్రణ ప్రవాహాన్నిచ్చేలా ఉంటుంది. ఇవి **బహుళ ఏజెంట్ కార్యాచరణ** మరియు **చెక్క్‌పాయింటింగ్** తో వర్క్‌ఫ్లో స్థితుల్ని సేవ్ చేయడాన్ని సాధ్యమవుతాయి.

వర్క్‌ఫ్లో యొక్క ప్రధాన భాగాలు:

**ఎగ్జిక్యూటర్లు**

ఎగ్జిక్యూటర్లు ఇన్‌పుట్ సందేశాలు తీసుకుంటాయి, కేటాయించిన పనులు నిర్వహిస్తాయి, తరువాత అవుట్‌పుట్ సందేశాన్ని ఉత్పత్తి చేస్తాయి. ఇది పెద్ద పని పూర్తి అవడంలో వర్క్‌ఫ్లోని ముందుకు తీసుకువెళ్తుంది. ఎగ్జిక్యూటర్లు AI ఏజెంట్ లేదా అనుకూల లాజిక్ ఉండవచ్చు.

**ఎడ్జెస్**

ఎడ్జెస్ వర్క్‌ఫ్లోలో సందేశాల ప్రవాహం నిర్వచించడానికి ఉపయోగపడతాయి. ఇవి:

*నేరుగా ఎడ్జెస్* - ఎగ్జిక్యూటర్ల మధ్య సరళమైన ఒకటి-కొన్ని కనెక్షన్లు:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*షరతు ఆధారిత ఎడ్జెస్* - నిర్దిష్ట షరతు తీరిన వెంటనే సక్రియమవుతాయి. ఉదా: హోటల్ గదులు అందుబాటులో లేకపోతే, ఒక ఎగ్జిక్యూటర్ ఇతర ఎంపికలను సూచించవచ్చు.

*స్విచ్-కేస్ ఎడ్జెస్* - నిర్వచించిన షరతుల ఆధారంగా సందేశాలను వివిధ ఎగ్జిక్యూటర్లకు పంపడం. ఉదా: ప్రయాణ పర్యాటకుడికి ప్రాధాన్యత గల యాక్సెస్ ఉన్నప్పుడు, వారి పనులు మరో వర్క్‌ఫ్లో ద్వారా నిర్వహించబడతాయి.

*ఫ్యాన్-అవుట్ ఎడ్జెస్* - ఒక సందేశాన్ని అనేక లక్ష్యాలకు పంపడం.

*ఫ్యాన్-ఇన్ ఎడ్జెస్* - వివిధ ఎగ్జిక్యూటర్ల నుండి బహుళ సందేశాలను సమీకరించి ఒక లక్ష్యానికి పంపడం.

**ఈవెంట్స్**

వర్క్‌ఫ్లోలకు మెరుగైన పరిశీలన అందించడానికి, MAF అమలు ఈవెంట్లను అందిస్తుంది:

- `WorkflowStartedEvent`  - వర్క్‌ఫ్లో అమలు ప్రారంభం
- `WorkflowOutputEvent` - వర్క్‌ఫ్లో అవుట్‌పుట్ తయారవుతుంది
- `WorkflowErrorEvent` - వర్క్‌ఫ్లోలో లోపం సంభవిస్తుంది
- `ExecutorInvokeEvent`  - ఎగ్జిక్యూటర్ ప్రాసెసింగ్ మొదలు
- `ExecutorCompleteEvent`  - ఎగ్జిక్యూటర్ ప్రాసెసింగ్ పూర్తిచేసింది
- `RequestInfoEvent` - అభ్యర్థన జారీ అవుతుంది

## అధునాతన MAF నమూనాలు

పై విభాగాలు మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క కీలక భావనలను కవర్ చేస్తాయి. మీరు మరింత క్లిష్టమైన ఏజెంట్లు నిర్మిస్తున్నప్పుడు, ఈ క్రింది అధునాతన నమూనాలను పరిగణించండి:

- **మధ్యస్థం కాంపోజిషన్**: ఫంక్షన్ మరియు చాట్ middleware ఉపయోగించి బహుళ middleware హ్యాండ్‌లర్లు (లాగింగ్, ఆత్మీకరణ, రేట్-లిమిటింగ్) లను చైన్ చేసి ఏజెంట్ ప్రవర్తనపై సన్నిహిత నియంత్రణ పొందడం.
- **వర్క్‌ఫ్లో చెక్క్‌పాయింటింగ్**: వర్క్‌ఫ్లో ఈవెంట్స్ మరియు సీరియలైజేషన్ ఉపయోగించి పొడవైన ఏజెంట్ ప్రాసెస్‌లను సేవ్ చేసి పునఃప్రారంభించడం.
- **డైనమిక్ టూల్ ఎంపిక**: టూల్ వివరణలపై RAG ని మిళితం చేసి, MAF టూల్ రిజిస్ట్రేషన్ ఉపయోగించి, ప్రతి ప్రశ్న కోసం సరైన టూల్స్ మాత్రమే చూపించడం.
- **బహుళ ఏజెంట్ హ్యాండ్‌ఆఫ్**: ప్రత్యేకాసేపి ఏజెంట్ల మధ్య హ్యాండ్‌ఆఫ్స్ చేయడానికి వర్క్‌ఫ్లో ఎడ్జెస్ మరియు షరతు ఆధారిత మార్గదర్శనం ఉపయోగించడం.

## Microsoft Foundry పై LangChain / LangGraph ఏజెంట్ల ఆతిథ్యం

మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ **ఫ్రేమ్‌వర్క్-ఇంటరొపరేబుల్** — మీరు MAF తో రాసిన ఏజెంట్లకే పరిమితం కాలేదు. మీరు ఇప్పటికే **LangChain** లేదా **LangGraph** తో ఏజెంట్ నిర్మించుకున్నట్లయితే, మీరు దాన్ని **Microsoft Foundry హోస్ట్ చేసిన ఏజెంట్** గా నడపవచ్చు. అందులో Foundry రన్‌టైమ్, సెషన్స్, స్కేలింగ్, ఐడెంటిటీ, మరియు ప్రోటోకాల్ ఎండ్పాయింట్ల నిర్వహణ చేస్తుంది, మీ ఏజెంట్ లాజిక్ LangGraph లోనే ఉంటుంది.

ఇది `langchain_azure_ai.agents.hosting` ప్యాకేజీతో చేయబడుతుంది, ఇది Foundry హోస్ట్ చేసిన ఏజెంట్లు ఉపయోగించే అదే ప్రోటోకాల్‌లపై కంపైల్డు LangGraph గ్రాఫ్‌ను ప్రదర్శిస్తుంది.

**1. హోస్టింగ్ అదనపు ప్యాకేజీని ఇన్‌స్టాల్ చేయండి:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` అదనపు ప్యాకేజీ Foundry ప్రోటోకాల్ లైబ్రరీలను ఇన్‌స్టాల్ చేస్తుంది: `azure-ai-agentserver-responses` (OpenAI అనుకూల `/responses` ఎండ్పాయింట్) మరియు `azure-ai-agentserver-invocations` (సాధారణ `/invocations` ఎండ్పాయింట్).

**2. హోస్టింగ్ ప్రోటోకాల్ ఎంచుకోండి:**

| ప్రోటోకాల్ | హోస్ట్ క్లాస్ | ఎండ్పాయింట్ | ఎప్పుడు ఉపయోగించాలి |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | మీరు OpenAI అనుకూల చాట్, స్ట్రీమింగ్, ప్రతిస్పందన చరిత్ర, మరియు సంభాషణ థ్రెడ్ అవసరం ఉంటే — సంభాషణ ఏజెంట్లకు సిఫార్సు చేయబడిన డిఫాల్ట్. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | మీరు అనుకూల JSON ఆకారం, webhook-శైలీ ఎండ్పాయింట్ లేదా అసంభాషణ ప్రక్రియ అవసరం ఉంటే. |

ఎందుకంటే **Responses API Foundryలో ఏజెంట్-శైలి అభివృద్ధికి ప్రధాన API కావడంతో**, ఎక్కువ ఏజెంట్లకు `ResponsesHostServer` తో ప్రారంభించండి.

**3. పరిసర వేరియబుల్లు కాన్ఫిగర్ చేయండి** (`az login` ముందుగా చేసి `DefaultAzureCredential` అథెంటికేట్ చేయగలుగుతుంది):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

ఏజెంట్ తరువాత Foundryలో హోస్ట్ చేసిన ఏజెంట్ గా నడిపినప్పుడు, ప్లాట్‌ఫారమ్ ఆటోమేటిక్‌గా `FOUNDRY_PROJECT_ENDPOINT` ని ఇంజెక్ట్ చేస్తుంది.

**4. Responses ప్రోటోకాల్‌పై LangGraph ఏజెంట్‌ను ఎక్స్‌పోజ్ చేయండి:**

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

    # ChatOpenAI ఇక్కడ Foundry ప్రాజెక్ట్ యొక్క OpenAI-అనుకూల (ప్రతిస్పందనలు) ఎండ్‌పాయింట్‌ను లక్ష్యంగా పెట్టుకుంది.
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

`python main.py` తో స్థానికంగా నడపండి, తరువాత `http://localhost:8088/responses` కి Responses అభ్యర్థన పంపండి.

**ప్రధాన ప్రవర్తనలు:**

- **సంభాషణలు**: క్లయింట్లు `previous_response_id` లేదా `conversation` ID ద్వారా సంభాషణ కొనసాగిస్తారు. మీ గ్రాఫ్ LangGraph చెక్క్‌పాయింటర్‌తో కంపైల్ అయితే, Foundry సంభాషణ స్థితిని చెక్‌పాయింటర్‌కు కీ చేస్తుంది (ప్రొడక్షన్‌లో ఒక దృఢమైన చెక్క్‌పాయింటర్ ఉపయోగించండి; స్థానిక పరీక్ష కోసం `MemorySaver` సరిపోతుంది).
- **మానవ-ఇన్-ది-లూప్**: మీ గ్రాఫ్ LangGraph `interrupt()` ఉపయోగిస్తే, `ResponsesHostServer` పెండింగ్ ఇంటరప్ట్‌ను Responses `function_call` / `mcp_approval_request` అంశంగా ప్రదర్శిస్తుంది, మరియు క్లయింట్లు సరిపోయే `function_call_output` / `mcp_approval_response` తో కొనసాగుతారు.
- **Foundryకి డిప్లాయ్ చేయండి**: Azure Developer CLI ఉపయోగించండి — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (స్థానిక, Docker అవసరం), తర్వాత `azd provision` మరియు `azd deploy`. హోస్ట్-ఏజెంట్ డిప్లాయ్‌మెంట్‌కు **Foundry ప్రాజెక్ట్ మేనేజర్** పాత్ర అవసరం.

ఈ ఉదాహరణ యొక్క నడుస్తున్న వెర్షన్ [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)లో ఉంది. పూర్తి వాక్‌థ్రూ కోసం (Invocations ప్రోటోకాల్, అనుకూల అభ్యర్థన స్కీమాలు, మరియు సమస్య పరిష్కారం), చూడండి [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## కోడ్ నమూనాలు

మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ కోడ్ నమూనాలు ఈ రిపోజిటరీలో `xx-python-agent-framework` మరియు `xx-dotnet-agent-framework` ఫైళ్లలో లభిస్తాయి.

## మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ పై ఇంకా ప్రశ్నలున్నాయా?

ఇతర నేర్చుకునేవారితో కలుసుకోవడానికి, ఆఫీస్ గంటల్లో పాల్గొనడానికి మరియు మీ AI ఏజెంట్ల ప్రశ్నలకు సమాధానాలు పొందడానికి [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) లో చేరండి.
## ముందు పాఠం

[AI ఏజెంట్లకు మెమరీ](../13-agent-memory/README.md)

## తదుపరి పాఠం

[కంప్యూటర్ వినియోగ ఏజెంట్ల నిర్మాణం (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->