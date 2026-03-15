# Microsoft Agent Framework అన్వేషణ

![Agent Framework](../../../translated_images/te/lesson-14-thumbnail.90df0065b9d234ee.webp)

### పరిచయం

ఈ పాఠం కవర్ చేస్తుంది:

- Microsoft Agent Framework ని అర్థం చేసుకోవడం: ముఖ్య లక్షణాలు మరియు విలువు  
- Microsoft Agent Framework యొక్క ముఖ్య భావాలను అన్వేషించడం
- అభివృద్ధినుండి MAF ఆకృతులు: వర్క్‌ఫ్లోల, మిడిల్‌వేర్, మరియు మెమొరీ

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠాన్ని పూర్తిచేసిన తర్వాత, మీరు తెలుసు:

- Microsoft Agent Framework ఉపయోగించి ప్రొడక్షన్ రెడీ AI ఏజెంట్లను నిర్మించడం
- Microsoft Agent Framework యొక్క కోర్ లక్షణాలను మీ ఏజెంటిక్ ఉపయోగ కేసులకు వర్తింపచేయడం
- వర్క్‌ఫ్లోలు, మిడిల్‌వేర్, మరియు ఆబ్జర్వబిలిటీతో కూడిన అభివృద్ధి ఆకృతులను ఉపయోగించడం

## కోడ్ ఉదాహరణలు 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) కొరకు కోడ్ ఉదాహరణలు ఈ రిపాజిటరీలో `xx-python-agent-framework` మరియు `xx-dotnet-agent-framework` ఫైళ్ల క్రింద అందుబాటులో ఉన్నాయి.

## Microsoft Agent Framework అర్థం చేసుకోవడం

![Framework Intro](../../../translated_images/te/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) Microsoft యొక్క ఏఐ ఏజెంట్లను నిర్మించడానికి ఐక్యపరిచిన ఫ్రేమ్‌వర్క్. ఇది ప్రొడక్షన్ మరియు పరిశోధనా వాతావరణాలలో కనిపించే విభిన్న ఏజెంటిక్ ఉపయోగ కేసులను పరిష్కరించడానికి సరిపోయే సరళతను అందిస్తుంది, అందులో:

- **క్రమబద్దమైన ఏజెంట్ సంయోజనం**: దశల వారీ వర్క్‌ఫ్లో అవసరమయ్యే సందర్భాలలో.
- **సమాంతర సంయోజనం**: ఏజెంట్లు ఒకేసారి పనులు పూర్తి చేయవలసిన సందర్భాలలో.
- **గ్రూప్ చాట్ సంయోజనం**: ఏజెంట్లు ఒకే పని పై కలిసి పని చేసే సందర్భాలలో.
- **హాండ్ ఆఫ్ సంయోజనం**: సబ్టాస్క్‌లు పూర్తైతే ఏజెంట్లు ఒకరితో ఒకరు పనిని అప్పగించే సందర్భాలలో.
- **మ్యాగ్నెటిక్ సంయోజనం**: మేనేజర్ ఏజెంట్ టాస్క్‌లను సృష్టించి సవరించి సబ్ ఏజెంట్ల సమన్వయాన్ని నిర్వహించే సందర్భాలలో.

AI ఏజెంట్లను ప్రొడక్షన్‌లో డెలివరీ చేయడానికి, MAF ఈ క్రింది లక్షణాలను కూడా కలిగి ఉంది:

- **ఆబ్జర్వబిలిటీ**: ప్రతి ఏఐ ఏజెంట్ చర్య, టూల్ ఆహ్వానం, సంయోజనా దశలు, కారణేభావిత ప్రవాహాలు మరియు Microsoft Foundry డాష్‌బోర్డ్ల ద్వారా పనితీరు గమనించడం OpenTelemetry ఉపయోగించి.
- **సెక్యూరిటీ**: Microsoft Foundry లో స్థానికంగా ఏజెంట్లను హోస్ట్ చేయడం ద్వారా, పాత్ర ఆధారిత ప్రాప్తి నియంత్రణలు, గోప్యమైన డేటా నిర్వహణ, మరియు బిల్ట్-ఇన్ కంటెంట్ సేఫ్టీ వంటి భద్రత నియంత్రణలతో.
- **దృఢత్వం**: ఏజెంట్ థ్రెడ్లు మరియు వర్క్‌ఫ్లోలు పాజ్, రీస్యూమ్ మరియు లోపాల నుంచి రికవర్ చేయగలవు, దీని వలన దీర్ఘకాలిక ప్రాసెస్ నిర్వహణ సౌకర్యం కలుగుతుంది.
- **కంట్రోల్**: హ్యూమన్-ఇన్-ది-లూప్ వర్క్‌ఫ్లోలు మద్దతు, పనులు మానవ ఆమోదం అవసరం అని గుర్తించబడతాయి.

Microsoft Agent Framework అంతరఘటనా (ఇంటర్‌ఒపరేబుల్)కి కూడా దృష్టి పెట్టింది:

- **క్లౌడ్-ఆగ్నాస్టిక్‌గా ఉండటం** - ఏజెంట్లు కంటైనర్లలో, ఆన్-ప్రెమిస్ లో మరియు బహుముఖ క్లౌడ్‌లలో నడపవచ్చు.
- **ప్రొవైడర్-ఆగ్నాస్టిక్‌గా ఉండటం** - Azure OpenAI మరియు OpenAI సహా మీరు ఇష్టపడే SDK ద్వారా ఏజెంట్లు సృష్టించవచ్చు.
- **ఓపెన్ స్టాండర్డ్లను సమీకరించటం** - Agent-to-Agent(A2A) మరియు Model Context Protocol (MCP) వంటి ప్రోటోకాల్లను ఉపయోగించి ఇతర ఏజెంట్లు మరియు టూల్స్‌ని కనుగొని ఉపయోగించవచ్చు.
- **ప్లగిన్లు మరియు కనెక్టర్లు** - Microsoft Fabric, SharePoint, Pinecone, Qdrant వంటి డేటా మరియు మెమొరీ సేవలకు కనెక్షన్లు చేయవచ్చు.

ఇప్పుడు Microsoft Agent Framework యొక్క కొన్ని ముఖ్య భావాలకు ఈ లక్షణాలు ఎలా వర్తిస్తాయో చూద్దాం.

## Microsoft Agent Framework ముఖ్య భావాలు

### ఏజెంట్లు

![Agent Framework](../../../translated_images/te/agent-components.410a06daf87b4fef.webp)

**ఏజెంట్లు సృష్టించడం**

ఏజెంట్ సృష్టి అనేది ఇన్ఫరెన్స్ సర్వీస్ (LLM ప్రొవైడర్), AI ఏజెంట్ అనుసరించాల్సిన సూచనల సముదాయం, మరియు కేటాయించబడిన `name` ని నిర్వచించడం ద్వారా జరుగుతుంది:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

పై ఉదాహరణలో `Azure OpenAI` ఉపయోగిస్తున్నారు కానీ ఏజెంట్లు వివిధ సేవలతో సృష్టించవచ్చు, ఉదాహరణకు `Microsoft Foundry Agent Service`:

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

లేదా A2A ప్రోటోకాల్ ఉపయోగించి రిమోట్ ఏజెంట్లు:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ఏజెంట్లను నడపడం**

ఏజెంట్లను non-streaming లేదా streaming ప్రతిస్పందనలకు `.run` లేదా `.run_stream` పద్ధతుల ద్వారా నడుపుతారు.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ప్రతి ఏజెంట్ రన్ కూడా `max_tokens` వంటి పారామీటర్లను, ఏజెంట్ పిలవగల `tools`, మరియు ఏజెంట్ కోసం ఉపయోగించే `model` ను మార్చుకునే ఎంపికలను కలిగి ఉంటుంది.

ఇది ఒక వినియోగదారుడి పనిని పూర్తి చేయడానికి నిర్దిష్ట మోడల్లు లేదా టూల్స్ అవసరమైన సందర్భాలలో ఉపయోగకరం.

**టూల్స్**

టూల్స్‌ను ఏజెంట్ నిర్వచించే సమయంలో కూడా నిర్వచించవచ్చు:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# చాట్ ఏజెంట్ ను ప్రత్యక్షంగా సృష్టించినప్పుడు

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

మరియు ఏజెంట్ నడిపినప్పుడు కూడా నిర్వచించవచ్చు:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ఈ రన్ కోసం మాత్రమే అందించిన పరికరం )
```

**ఏజెంట్ థ్రెడ్లు**

ఏజెంట్ థ్రెడ్లు బహుళ-తిరుగుడు సంభాషణల కోసం ఉపయోగపడతాయి. థ్రెడ్లు క్రింది విధంగా సృష్టించవచ్చు:

- `get_new_thread()` ఉపయోగించి, ఇది థ్రెడ్‌ను కాలానికి పాజ్ చేసి నిల్వ చేయడానికి అనుమతిస్తుంది
- ఏజెంట్ నడిపితప్పుడు ఆటోమేటిక్‌గా థ్రెడ్ను సృష్టించి ప్రస్తుత రన్ సమయంలోనే అస్థాయిగా ఉండడానికి.

థ్రెడ్ సృష్టించడానికి కోడ్ ఇలా ఉంటుంది:

```python
# కొత్త థ్రెడ్‌ను సృష్టించండి.
thread = agent.get_new_thread() # ఆ ఏజెంట్‌ను థ్రెడ్‌తో నడపండి.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

తరువాత ఈ థ్రెడ్‌ను స్రియలైజ్ చేసి భవిష్యత్తులో ఉపయోగానికి నిల్వ చేయవచ్చు:

```python
# కొత్త థ్రెడ్‌ను సృష్టించండి.
thread = agent.get_new_thread() 

# థ్రెడ్‌తో ఏజెంట్‌ను నడపండి.

response = await agent.run("Hello, how are you?", thread=thread) 

# నిల్వ కోసం థ్రెడ్‌ను సిరియలైజ్ చేయండి.

serialized_thread = await thread.serialize() 

# నిల్వ నుండి లోడ్ చేసిన తర్వాత థ్రెడ్ స్థితిని డిసిరియలైజ్ చేయండి.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ఏజెంట్ మిడిల్‌వేర్**

ఏజెంట్లు టూల్స్ మరియు LLM లతో పరస్పరం సానుకూలంగా పనిచెయ్యాలి. కొన్నిసార్లు, ఈ పరస్పర చర్యల మధ్యలో కొన్ని చర్యలు లేదా ట్రాకింగ్ అవసరమవుతుంది. ఏజెంట్ మిడిల్‌వేర్ ఇది సాధ్యం చేస్తుంది:

*ఫంక్షన్ మిడిల్‌వేర్*

ఈ మిడిల్‌వేర్ ఏజెంట్ మరియు ఏ ఫంక్షన్/టూల్ మధ్య చర్యను అమలు చేయడానికి అనుమతిస్తుంది. ఉదాహరణకు, ఫంక్షన్ కాల్‌పై లాగ్ చేయడం అవసరమైనప్పుడు దీనిని ఉపయోగిస్తారు.

కోడ్‌లో `next` అనేది తర్వాత మిడిల్‌వేర్ లేదా వాస్తవ ఫంక్షన్ ను పిలవాలా అన్నదాన్ని నిర్వచిస్తుంది.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ప్రీ-ప్రాసెసింగ్: ఫంక్షన్ నడుపుకునే ముందు లాగ్ చేయండి
    print(f"[Function] Calling {context.function.name}")

    # తదుపరి మిడ్‌ల్వేర్ లేదా ఫంక్షన్ నడుపుట కొనసాగించండి
    await next(context)

    # పోస్ట్-ప్రాసెసింగ్: ఫంక్షన్ నడుపుకునే తర్వాత లాగ్ చేయండి
    print(f"[Function] {context.function.name} completed")
```

*చాట్ మిడిల్‌వేర్*

ఈ మిడిల్‌వేర్ ఏజెంట్ మరియు LLM మధ్య అభ్యర్థనల మధ్య చర్యను అమలు చేయడానికి లేదా లాగ్ చేయడానికి అనుమతిస్తుంది.

ఇది AI సర్వీస్‌కు పంపబడుతున్న `messages` వంటి ముఖ్య సమాచారాన్ని కలిగి ఉంటుంది.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ముందస్తు ప్రాసెసింగ్: AI కాల్ ముందు లాగ్ చేయండి
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # తదుపరి మిడిల్‌వేర్ లేదా AI సర్వీస్‌కు కొనసాగండి
    await next(context)

    # తర్వాతి ప్రాసెసింగ్: AI స్పందన తర్వాత లాగ్ చేయండి
    print("[Chat] AI response received")

```

**ఏజెంట్ మెమోరీ**

`Agentic Memory` పాఠంలో వివరించినట్లుగా, మెమరీ ఏజెంట్‌ను వివిధ సందర్భాలలో పని చేయడానికి సహాయపడే కీలక అంశం. MAF అనేకవిధాల మెమరీలను అందిస్తుంది:

*ఇన్-మెమరీ స్టోరేజ్*

ఇది ది ఆప్లికేషన్ రన్‌టైమ్ సమయంలో థ్రెడ్లలో నిల్వ చేయబడే మెమరీ.

```python
# ఒక కొత్త థ్రెడ్ సృష్టించండి.
thread = agent.get_new_thread() # ఆ థ్రెడ్ తో ఏజెంట్ ను నడపండి.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*స్థిర persist మెసేజ్‌లు*

ఈ మెమరీ వివిధ సెషన్లలో సంభాషణ చరిత్ర నిల్వ చేయడానికి ఉపయోగిస్తారు. ఇది `chat_message_store_factory` ఉపయోగించి నిర్వచించబడుతుంది:

```python
from agent_framework import ChatMessageStore

# ఒక అనుకూల సందేశం నిల్వను సృష్టించండి
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*డైనమిక్ మెమరీ*

ఈ మెమరీ ఏజెంట్లు నడపడంలో ముందు కంటెక్స్ట్‌కు జోడించబడుతుంది. దీన్ని mem0 వంటి బయటి సేవలలో నిల్వ చేయవచ్చు:

```python
from agent_framework.mem0 import Mem0Provider

# Mem0ని ఉన్నతమైన స్మృతి లక్షణాల కోసం ఉపయోగించడం
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

**ఏజెంట్ ఆబ్జర్వబిలిటీ**

ఆబ్జర్వబిలిటీ అనేది నమ్మదగిన మరియు నిర్వహించదగిన ఏజెంటిక్ సిస్టమ్లను నిర్మించడానికి ముఖ్యం. MAF OpenTelemetryతో సమన్వయ పడుతుంది, ట్రేసింగ్ మరియు మెటర్లను అందించే మంచి ఆబ్జర్వబిలిటి కొరకు.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ఏదైన కార్యం చేయండి
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### వర్క్‌ఫ్లోలు

MAF వర్చుసారితలైన పనులను పూర్తి చేయడానికి ముందుగా నిర్వచించిన దశలను అందిస్తుంది మరియు ఆ దశల్లో AI ఏజెంట్లను భాగాలుగా కలిగి ఉంటుంది.

వర్క్‌ఫ్లోలు వివిధ భాగాలతో కూడి ఉంటాయి, ఇవి నియంత్రణను మెరుగుపరుస్తాయి. వర్క్‌ఫ్లోలు **బహుళ-ఏజెంట్ సంయోజనం** మరియు **చెక్‌పాయింటింగ్** లను కూడా అనుమతిస్తాయి, వర్క్‌ఫ్లో స్టేట్లను సేవ్ చేయడం కొరకు.

వర్క్‌ఫ్లో యొక్క మూల భాగాలు:

**ఎగ్జిక్యూటర్లు**

ఎగ్జిక్యూటర్లు ఇన్పుట్ సందేశాలను పొందుతారు, అప్పటి విధంగా ఏ పనిని చేస్తారు, మరియు అవుట్పుట్ సందేశాన్ని ఉత్పత్తి చేస్తారు. ఇది వర్క్‌ఫ్లోని పెద్ద పని పూర్తి దిశగా కదలిస్తుంది. ఎగ్జిక్యూటర్లు AI ఏజెంట్ లేక ప్రాచీన లాజిక్ కూడా కావచ్చు.

**ఎడ్జ్‌లు**

ఎడ్జ్‌లు వర్క్‌ఫ్లోలో సందేశాల ప్రవాహాన్ని నిర్వచించడానికి ఉపయోగిస్తారు. ఇవి:

*డైరెక్ట్ ఎడ్జ్‌లు* - ఎగ్జిక్యూటర్ల మధ్య సరళమైన ఒక-కు-ఒక కనెక్షన్లు:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*కండీషనల్ ఎడ్జ్‌లు* - నిర్దిష్ట పరిస్థితి తీరిన తర్వాత ప్రారంభమవుతాయి. ఉదాహరణకు, హోటల్ గదులు అందుబాటులో లేనప్పుడు, ఎగ్జిక్యూటర్ ఇతర ఎంపికలను సూచించవచ్చు.

*స్విచ్-కేస్ ఎడ్జ్‌లు* - నిర్దిష్ట పరిస్థితుల ఆధారంగా సందేశాలను వేరే ఎగ్జిక్యూటర్లకు రవాణా చేస్తాయి. ఉదాహరణకు, ప్రయాణ కస్టమర్ కు ప్రాధాన్యత ప్రాప్తి ఉన్నట్లయితే వారి పనులు వేరే వర్క్‌ఫ్లో ద్వారా నిర్వహించబడతాయి.

*ఫ్యాన్-అవుట్ ఎడ్జ్‌లు* - ఒక సందేశాన్ని అనేక గమ్యస్థానాలకు పంపుతాయి.

*ఫ్యాన్-ఇన్ ఎడ్జ్‌లు* - అనేక ఎగ్జిక్యూటర్ల నుండి సందేశాలను సమీకరించి ఒకే లక్ష్యానికి పంపుతాయి.

**ఈవెంట్స్**

వర్క్‌ఫ్లోలను మంచిగా గమనించడానికి MAF క్రిందివిధమైన ఎగ్జిక్యూషన్ ఈవెంట్స్ అందిస్తుంది:

- `WorkflowStartedEvent`  - వర్క్‌ఫ్లో ఎగ్జిక్యూషన్ మొదలవుతుంది
- `WorkflowOutputEvent` - వర్క్‌ఫ్లో అవుట్పుట్ ఉత్పత్తి చేస్తుంది
- `WorkflowErrorEvent` - వర్క్‌ఫ్లో లో లోపం వస్తుంది
- `ExecutorInvokeEvent`  - ఎగ్జిక్యూటర్ ప్రాసెసింగ్ ప్రారంభం
- `ExecutorCompleteEvent`  -  ఎగ్జిక్యూటర్ ప్రాసెసింగ్ ముగింపు
- `RequestInfoEvent` - అభ్యర్థన సమర్పించబడింది

## అభివృద్ధి MAF ఆకృతులు

పై విభాగాలు Microsoft Agent Framework యొక్క ముఖ్య భావాలను కవర్ చేస్తాయి. మీరు మరింత క్లిష్ట ఏజెంట్లు నిర్మిస్తున్నప్పుడు, కొన్ని అభివృద్ధి ఆకృతులను పరిశీలించండి:

- **మిడిల్‌వేర్ కాంపోజిషన్**: ఫంక్షన్ మరియు చాట్ మిడిల్‌వేర్‌లను ఉపయోగించి అనేక మిడిల్‌వేర్ హ్యాండలర్స్ (లాగ్, ఆథ్, రేట్-లిమిటింగ్) ను జత చేయడం ద్వారా ఏజెంట్ ప్రవర్తనపై సరికొత్త నియంత్రణ.
- **వర్క్‌ఫ్లో చెక్‌పాయింటింగ్**: వర్క్‌ఫ్లో ఈవెంట్స్ మరియు స్రియలైజేషన్ ఉపయోగించి దీర్ఘకాలిక ఏజెంట్ ప్రాసెస్‌లను సేవ్ చేసి తిరిగి ప్రారంభించడం.
- **డైనమిక్ టూల్ సెలక్షన్**: MAF యొక్క టూల్ రిజిస్ట్రేషన్ తో RAG ఆధారంగా టూల్ వివరణలపై కీవోయర్డ్లను ఉపయోగించి ఉపయోగకరమైన టూల్స్ మాత్రమే ప్రదర్శించడం.
- **బహుళ ఏజెంట్ హాండ్ఫ్**: వర్క్‌ఫ్లో ఎడ్జ్‌లు మరియు కండీషనల్ రౌటింగ్ ఉపయోగించి ప్రత్యేక ఏజెంట్ల మధ్య హాండ్ఫ్‌లను సంయోజించడం.

## కోడ్ ఉదాహరణలు 

Microsoft Agent Framework కొరకు కోడ్ ఉదాహరణలు ఈ రిపాజిటరీలో `xx-python-agent-framework` మరియు `xx-dotnet-agent-framework` ఫైళ్ల క్రింద అందుబాటులో ఉన్నాయి.

## Microsoft Agent Framework గురించి మరిన్ని ప్రశ్నలు ఉన్నాయా?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) లో చేరండి, ఇతర అభ్యాసకులతో కలుసుకోండి, ఆఫీస్ అవర్స్ వెళ్ళండి మరియు మీ AI ఏజెంట్ల ప్రశ్నలకు సమాధానం పొందండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**హేతుబద్ధత**:  
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో తప్పులు లేదా అసమర్థతలు ఉండొచ్చు అని దయచేసి గమనించండి. ఇది మూల పుస్తకం native భాషలో ఉండే డాక్యుమెంట్‌ను అధికారిక ఆధారంగా తీసుకోవాలి. ముఖ్య సమాచారం కోసం, వృత్తిపరమైన మానవ అనువాదాన్ని సిఫార్సు చేస్తున్నాం. ఈ అనువాదం ఉపయోగించడం ద్వారా ఎటువంటి సందేహాలు లేదా తప్పుదారుల వల్ల కలిగే బాధ్యత మేము తీసుకోము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->