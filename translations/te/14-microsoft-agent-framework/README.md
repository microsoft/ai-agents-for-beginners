# Microsoft Agent Framework ను అన్వేషించడం

![Agent Framework](../../../translated_images/te/lesson-14-thumbnail.90df0065b9d234ee.webp)

### పరిచయం

ఈ పాఠం కవర్ చేస్తుంది:

- Microsoft Agent Frameworkను అర్థం చేసుకోవడం: ముఖ్య లక్షణాలు మరియు విలువ  
- Microsoft Agent Framework యొక్క ప్రధాన భావనలు అన్వేషించడం
- అభివృద్ధి చెందిన MAF నమూనాలు: వర్క్‌ఫ్లోలు, మిడిల్వేర్, మరియు మెమొరీ

## నేర్చుకునే లక్ష్యాలు

ఈ పాఠం పూర్తి చేసిన తర్వాత, మీరు తెలుసుకోగలుగుతారు:

- Microsoft Agent Framework ఉపయోగించి ప్రొడక్షన్ రెഡിയ్ AI ఏజెంట్లను నిర్మించడం
- Microsoft Agent Framework యొక్క ముఖ్య లక్షణాలను మీ ఏజెంటిక్ ఉపయోగ కేసులకు వర్తింపజేయడం
- వర్క్‌ఫ్లోలు, మిడిల్వేర్ మరియు పరిశీలనాత్మకత సహా అభివృద్ధి చెందిన నమూనాలను ఉపయోగించడం

## కోడ్ నమూనాలు 

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) కోసం కోడ్ నమూనాలు ఈ రిపోజిటరీలో `xx-python-agent-framework` మరియు `xx-dotnet-agent-framework` ఫైళ్ళ క్రింద ఉన్నాయి.

## Microsoft Agent Framework అర్థం చేసుకోవడం

![Framework Intro](../../../translated_images/te/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) Microsoft యొక్క AI ఏజెంట్లను తయారుచేసేందుకు ఏకీకృత ఫ్రేమ్‌వర్క్. ఇది ప్రొడక్షన్ మరియు పరిశోధన వాతావరణాలలో కనిపించే విభిన్న agentic ఉపయోగ కేసులను ఎదుర్కోవడానికి తగిన సరైన లవచిగా అందిస్తుంది:

- **అనుక్రమ యాజమాన్యం** అక్కడ ఎక్కడి స్టెప్-బై-స్టెప్ వర్క్‌ఫ్లోలు అవసరం.
- **సమకాలీన యాజమాన్యం** అక్కడ ఎక్కడి ఏజెంట్లు ఒకేసారి పనులు పూర్తి చేయాలి.
- **గ్రూప్ చాట్ యాజమాన్యం** అక్కడ ఏజెంట్లు ఒకటే పనిమీద కలిసి పని చేయగలరు.
- **హ్యాండాఫ్ యాజమాన్యం** అక్కడ ఏజెంట్లు ఉపపనులు పూర్తిచేసినప్పుడు పనిని ఒకరికి మరొకరు బదిలీ చేస్తారు.
- **మెగ్నెటిక్ యాజమాన్యం** అక్కడ మేనేజర్ ఏజెంట్ పని జాబితాను సృష్టించి మారుస్తుంది మరియు ఉపఏజెంట్ల సమన్వయాన్ని నిర్వహిస్తుంది.

AI ఏజెంట్లను ప్రొడక్షన్‌లో అందించడం కోసం, MAF క్రింది లక్షణాలను కలిగి ఉంది:

- **పరిశీలనాత్మకత** OpenTelemetry ఉపయోగించుట ద్వారా AI ఏజెంట్ యొక్క ప్రతీ చర్య, టూల్ పిలుపు, యాజమాన్య దశలు, ఆలోచనా ప్రవాహాలు మరియు Microsoft Foundry డాష్‌బోర్డ్ల ద్వారా పనితన పర్యవేక్షణ.
- **భద్రత** Microsoft Foundryలో ఏజెంట్లను ప్రయోజనాత్మక భద్రత నియంత్రణలతో (పాత్ర ఆధారిత ప్రాప్తి, ప్రైవేట్ డేటా నిర్వహణ, నియమిత భద్రత) హోస్ట్ చేయడం.
- **టికారుపాయితనం** ఏజెంట్ థ్రెడ్‌లు మరియు వర్క్‌ఫ్లోలు విరామం, తిరిగి ప్రారంభం, లోపాల నుంచి పునఃప్రాప్తి చేయగలవు.
- **నియంత్రణ** మానవ అంగీకారాన్ని అవసరమయ్యే పనుల కోసం మానవ-సహజ వర్క్‌ఫ్లోలను మద్దతు.

Microsoft Agent Framework కూడా ఇంటరాక్టబుల్ ([interop]) కావడంపై దృష్టి సారిస్తుంది:

- **క్లౌడ్-నిర్పేక్ష** - ఏజెంట్లు కంటైనర్లు, ఆన్-ప్రెమైస్ మరియు విభిన్న క్లౌడ్లలో నడవగలవు.
- **ప్రొవైడర్-నిర్పేక్ష** - ఏజెంట్లు మీ ఇష్టమైన SDK ఉపయోగించి, జంటగా Azure OpenAI మరియు OpenAI సహా సృష్టించబడవచ్చు.
- **ఓపెన్ స్టాండర్డ్లకు అనుసంధానం** - Agent-to-Agent(A2A) మరియు Model Context Protocol (MCP) వంటి ప్రొటోకాల్స్ ద్వారా ఇతర ఏజెంట్లు మరియు టూల్స్ కనుగొని ఉపయోగించగలగడం.
- **ప్లగిన్లు మరియు కనెక్టర్లు** - Microsoft Fabric, SharePoint, Pinecone మరియు Qdrant వంటి డేటా మరియు మెమరీ సర్వీసులకు కనెక్షన్లు.

Microsoft Agent Framework యొక్క కొన్ని ప్రాతిపదిక భావనలపై ఈ లక్షణాలు ఎలా వర్తింపబడతాయో చూద్దాం.

## Microsoft Agent Framework ముఖ్య భావనలు

### ఏజెంట్లు

![Agent Framework](../../../translated_images/te/agent-components.410a06daf87b4fef.webp)

**ఏజెంట్ల సృష్టి**

ఏజెంట్ సృష్టి అనేది ఇన్ఫెరెన్స్ సర్వీస్ (LLM ప్రొవైడర్), AI ఏజెంట్ అనుసరించాల్సిన సూచనలు, మరియు ఇచ్చిన `name`ని నిర్వచించడం ద్వారా జరుగుతుంది:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

పై ఉదాహరణలో `Azure OpenAI` ఉపయోగించబడింది కానీ ఏజెంట్లు వివిధ సర్వీసుల ద్వారా సృష్టించవచ్చు, ఉదాహరణకి `Microsoft Foundry Agent Service`:

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

లేదా [MiniMax](https://platform.minimaxi.com/), ఇది పెద్ద కాంటెక్స్ట్ విండోలతో(OpenAI అనుకూల API 204K టోకెన్లు వరకు) అందిస్తుంది:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

లేదా A2A ప్రోటోకాల్ ఉపయోగించి రిమోట్ ఏజెంట్లు:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ఏజెంట్లను నడిపించడం**

ఏజెంట్లను స్ట్రీమింగ్ లేదా నాన్-స్ట్రీమింగ్ స్పందనల కోసం `.run` లేదా `.run_stream` మెథడ్లతో నడపవచ్చు.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ప్రతి ఏజెంట్ నడుపుకి `max_tokens`, ఏజెంట్ పిలవగల `tools`, మరియు ఏజెంట్ కోసం ఉపయోగించే `model` వంటి పారామితులు అనుకూలీకరించే ఆప్షన్లు కూడా ఉండవచ్చు.

ఇది ఉపయోగపడుతుంది, ప్రత్యేక మోడళ్ళు లేదా టూల్స్ వినియోగదారు పనిని పూర్తి చేయడానికి అవసరమైన సందర్భాలలో.

**టూల్స్**

ఏజెంట్ నిర్వచించేటప్పుడు:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent నేరుగా సృష్టిస్తున్నప్పుడు

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

మరియు ఏజెంట్ నడిపేటప్పుడు కూడా:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ఈ రన్ కోసం మాత్రమే అందించబడిన సాధనం )
```

**ఏజెంట్ థ్రెడ్స్**

ఏజెంట్ థ్రెడ్స్ మల్టీ-టర్న్ సంభాషణలను నిర్వహించడానికి ఉపయోగిస్తారు. థ్రెడ్స్ సృష్టించవచ్చు:

- `get_new_thread()` ఉపయోగించి దీన్ని కాలక్రమేణా భద్రపరచడానికి
- ఏజెంట్ నడుపుతూ ఆటోమేటిక్‌గా థ్రెడ్ సృష్టించడం, ఈ థ్రెడ్ ప్రస్తుత నడుపుకే పరిమితం.

థ్రెడ్ సృష్టించడానికి కోడ్ ఇలా ఉంటోంది:

```python
# ఒక కొత్త త్రెడ్ ను సృష్టించండి.
thread = agent.get_new_thread() # ఆ త్రెడ్ తో ఏజెంట్ ను నడపండి.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

తర్వాత మీరు థ్రెడ్‌ని భవిష్యత్తులో ఉపయోగం కోసం సీరియలైజ్ చేయవచ్చు:

```python
# కొత్త థ్రెడ్‌ను సృష్టించండి.
thread = agent.get_new_thread() 

# థ్రెడ్‌తో ఏజెంట్‌ను నడపండి.

response = await agent.run("Hello, how are you?", thread=thread) 

# నిల్వ కోసం థ్రెడ్‌ను సీరియలైజ్ చేయండి.

serialized_thread = await thread.serialize() 

# నిల్వ నుండి లోడ్ చేసిన తర్వాత థ్రెడ్ స్థితిని డీసీరియలైజ్ చేయండి.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ఏజెంట్ మిడిల్వేర్**

ఏజెంట్లు టూల్స్ మరియు LLMలతో సహకరించి వినియోగదారు పనులను పూర్తి చేస్తాయి. కొన్ని పరిస్థితుల్లో, ఈ ఇంటరాక్షన్ మధ్యలో అమలు లేదా ట్రాక్ చేయాలి. ఏజెంట్ మిడిల్వేర్ దీనిని సాధ్యం చేస్తుంది:

*ఫంక్షన్ మిడిల్వేర్*

ఈ మిడిల్వేర్ ఏజెంట్ మరియు పిలవబడ్డ ఫంక్షన్/టూల్ మధ్య చర్యను అమలు చేయడానికి అనుమతిస్తుంది. ఉదాహరణకి, ఫంక్షన్ పిలుపు లాగింగ్ ఈ సమయంలో చేయవచ్చు.

క్రింది కోడులో `next` తదుపరి మిడిల్వేర్ లేదా ఫంక్షన్‌ని పిలవాలని నిర్వచిస్తుంది.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ముందు ప్రాసెసింగ్: ఫంక్షన్ అమలు ముందు లాగ్ చేయండి
    print(f"[Function] Calling {context.function.name}")

    # తదుపరి మిడిల్‌వేర్ లేదా ఫంక్షన్ అమలుకు కొనసాగండి
    await next(context)

    # తరువాత ప్రాసెసింగ్: ఫంక్షన్ అమలు తర్వాత లాగ్ చేయండి
    print(f"[Function] {context.function.name} completed")
```

*చాట్ మిడిల్వేర్*

ఈ మిడిల్వేర్ ఏజెంట్ మరియు LLM మధ్య అభ్యర్థనల మధ్య చర్యను అమలు లేదా లాగ్ చేయడానికి ఉపయోగపడుతుంది.

ఇది AI సర్వీస్‌కు పంపబడుతున్న `messages` వంటి ముఖ్య సమాచారం కలిగి ఉంటుంది.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ప్రీ-ప్రాసెసింగ్: AI కాల్ ముందు లాగ్ చేయండి
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # తదుపరి మిడిల్వేర్ లేదా AI సేవకు కొనసాగండి
    await next(context)

    # పోస్ట్-ప్రాసెసింగ్: AI స్పందన తర్వాత లాగ్ చేయండి
    print("[Chat] AI response received")

```

**ఏజెంట్ మెమొరీ**

`Agentic Memory` పాఠంలో కవర్డ్ ప్రకారం, మెమొరీ ఏజెంట్ ని వేరే సందర్భాల్లో పని చేయడానికి ముఖ్యమైన అంశం. MAF అనేక రకాల మెమొరీలను అందిస్తుంది:

*ఇన్-మెమొరీ నిల్వ*

ఇది అప్లికేషన్ రన్‌టైమ్ సమయంలో థ్రెడ్‌లలో నిల్వ చేయబడే మెమొరీ.

```python
# ఒక కొత్త థ్రెడ్‌ను సృష్టించండి.
thread = agent.get_new_thread() # ఆ ఎజెంట్‌ను ఆ థ్రెడ్తో నడిపించండి.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*స్థిర మేసేజెస్*

ఇది వేరే సెషన్ల మధ్య సంభాషణ చరిత్ర నిల్వ చేయడానికి ఉపయోగపడుతుంది. ఇది `chat_message_store_factory` ఉపయోగించి నిర్వచించబడింది:

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

*డైనమిక్ మెమొరీ*

ఏజెంట్లు నడించే ముందు ఈ మెమొరీ కాంటెక్స్ట్‌లో జత చేయబడుతుంది. ఇవి mem0 వంటి బాహ్య సేవల్లో నిల్వ చేయవచ్చు:

```python
from agent_framework.mem0 import Mem0Provider

# అభివృద్ధి చేసిన మెమరీ సామర్థ్యాల కోసం Mem0 ఉపయోగించడం
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

**ఏజెంట్ పరిశీలనాత్మకత**

విశ్వసనీయమైన మరియు నిర్వహించదగిన ఏజెంటిక్ సిస్టమ్స్ నిర్మించడంలో పరిశీలనాత్మకత ముఖ్యం. MAF OpenTelemetryతో ఏకీకృతం చెయ్యబడింది, ఇది మెరుగైన పరిశీలనాత్మకత కొరకు ట్రేసింగ్ మరియు మీటర్లను అందిస్తుంది.

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

MAF వర్క్‌ఫ్లోలు పనిని పూర్తి చేయడానికి ముందుగా నిర్వచించిన దశలను మరియు వాటి దశల్లో AI ఏజెంట్లను భాగాలుగా కలిగి ఉంటాయి.

వర్క్‌ఫ్లోలు వివిధ భాగాల నుండి తయారవుతాయి, ఇవి నియంత్రణ ప్రవాహాన్ని మెరుగుపరుస్తాయి. వర్క్‌ఫ్లోలు **బహుళ ఏజెంట్ యాజమాన్యం** మరియు **చెక్‌పాయింటింగ్**ను కూడా సపోర్ట్ చేస్తాయి.

వర్క్‌ఫ్లో యొక్క ప్రధాన భాగాలు:

**ఎగ్జిక్యూటర్లు**

ఎగ్జిక్యూటర్లు ఇన్పుట్ మెసేజెస్ అందుకుని, తమ కేటాయింపులు చేస్తారు, ఆ తరువాత అవుట్పుట్ మెసేజ్ ఉత్పత్తి చేస్తారు. ఇది మొత్తం పనిని పూర్తి చేయడానికి వర్క్‌ఫ్లోను ముందుకెళ్తుంది. ఎగ్జిక్యూటర్లు AI ఏజెంట్ లేదా క్రొత్త లాజిక్ కావచ్చు.

**ఎడ్జస్**

ఎడ్జస్ వర్క్‌ఫ్లోలో మెసేజెస్ ప్రవాహాన్ని నిర్వచించడానికి ఉపయోగిస్తారు. ఇవి:

*నేరుగా కనెక్షన్లు* - ఎగ్జిక్యూటర్ల మధ్య సాధారణ ఒకటి నుండి ఒక్కటి కనెక్షన్:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*నిబంధనాధారిత ఎడ్జస్* - నిర్దిష్ట పరిస్థితి సంతృప్తి అయ్యాక యాక్టివేట్ అవుతాయి. ఉదాహరణకి హోటల్ గదులు అందుబాటులో లేని సందర్భంలో, ఎగ్జిక్యూటర్ ఆప్షన్స్ సూచించవచ్చు.

*స్విచ్-కేస్ ఎడ్జస్* - పరిస్థితుల ఆధారంగా మెసేజస్‌ను విభిన్న ఎగ్జిక్యూటర్లకు రూట్ చేస్తాయి. ఉదాహరణకి, ప్రయాణ వినియోగదారుకు ప్రాధాన్యత ప్రాప్తి ఉన్నప్పుడు, వారి పనులు వేరే వర్క్‌ఫ్లో ద్వారా నిర్వహించబడతాయి.

*ఫ్యాన్-ఆవుట్ ఎడ్జస్* - ఒక మెసేజ్‌ను అనేక గమ్యస్థానాలకు పంపుతుంది.

*ఫ్యాన్-ఇన్ ఎడ్జస్* - విభిన్న ఎగ్జిక్యూటర్ల నుండి అనేక మెసేజెస్ సేకరించి ఒక గమ్యస్థానానికి పంపుతుంది.

**ఈవెంట్లు**

వర్క్‌ఫ్లోలలో మెరుగైన పరిశీలనాత్మకత కోసం, MAF అమలు ఈవెంట్లను అందిస్తుంది:

- `WorkflowStartedEvent`  - వర్క్‌ఫ్లో అమలు ప్రారంభమవుతుంది
- `WorkflowOutputEvent` - వర్క్‌ఫ్లో అవుట్పుట్ ఉత్పత్తి చేస్తుంది
- `WorkflowErrorEvent` - వర్క్‌ఫ్లోలో లోపం సంభవిస్తుంది
- `ExecutorInvokeEvent`  - ఎగ్జిక్యూటర్ ప్రాసెసింగ్ మొదలుపెడుతుంది
- `ExecutorCompleteEvent`  - ఎగ్జిక్యూటర్ ప్రాసెసింగ్ ముగిస్తుంది
- `RequestInfoEvent` - అభ్యర్థన జారీ చేయబడుతుంది

## అభివృద్ధి చెందిన MAF నమూనాలు

పై భాగాలు Microsoft Agent Framework యొక్క ముఖ్య భావనలను కవర్ చేస్తాయి. మీరు మరింత క్లిష్ట ఏజెంట్లను నిర్మిస్తున్నప్పుడు, ఇక్కడ కొన్ని అభివృద్ధి చెందిన నమూనాలు ఉన్నాయి:

- **మిడిల్వేర్ కంపోజిషన్**: ఎజెంట్ ప్రవర్తనపై సున్నితమైన నియంత్రణ కోసం ఫంక్షన్ మరియు చాట్ మిడిల్వేర్ ద్వారా బహుళ మిడిల్వేర్ హ్యాండ్లర్లను (లాగింగ్, గుర్తింపు, రేట్-లిమిటింగ్) చైన్ చేయండి.
- **వర్క్‌ఫ్లో తనిఖీ స్పాట్(Checkpointing)**: వర్క్‌ఫ్లో ఈవెంట్లు మరియు సీరియలైజేషన్ ఉపయోగించి దీర్ఘ కాలం నడిచే ఏజెంట్ ప్రాసెస్‌లను సేవ్ చేసి తిరిగి ప్రారంభించండి.
- **డైనమిక్ టూల్ ఎంపిక**: టూల్ వివరణలపై RAGని కలిపి MAF యొక్క టూల్ రిజిస్ట్రేషన్ తో నిర్దిష్ట ప్రశ్నకి సంబంధించిన టూల్స్ మాత్రమే ప్రదర్శించండి.
- **బహుళ ఏజెంట్ హ్యాండాఫ్**: స్పెషలైజ్డ్ ఏజెంట్ల మధ్య హ్యాండాఫ్లను ఆర్గనైజ్ చేయడానికి వర్క్‌ఫ్లో ఎడ్జస్ మరియు నిబంధన రూటింగ్ ఉపయోగించండి.

## Microsoft Foundryలో LangChain / LangGraph ఏజెంట్లని హోస్టింగ్ చేయడం

Microsoft Agent Framework **ఫ్రేమ్‌వర్క్-ఇంటరాపరబుల్** — మీరు MAFతో రాసిన ఏజెంట్లతో పరిమితం కాదు. మీరు ఇప్పటికే **LangChain** లేదా **LangGraph** సహా ఏజెంట్ నిర్మించుకున్నట్లయితే, దీనిని **Microsoft Foundry హోస్టెడ్ ఏజెంట్**గా నడుపవచ్చు, తద్వారా Foundry రన్‌టైమ్, సెషన్లు, స్కేలింగ్, ఐడెంటిటీ మరియు ప్రోటోకాల్ ఎండ్‌పాయింట్లను నిర్వహిస్తుంది, మీ ఏజెంట్ లాజిక్ LangGraphలోనే ఉంటుంది.

ఇది `langchain_azure_ai.agents.hosting` ప్యాకేజితో చేయబడుతుంది, ఇది Foundry హోస్టెడ్ ఏజెంట్లు ఉపయోగించే ప్రోటోకాల్స్ పై కంపైల్ చేసిన LangGraph గ్రాఫ్‌ని ప్రకటిస్తుంది.

**1. హోస్టింగ్ అదనాన్ని ఇన్స్టాల్ చేయండి:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` అదనంతో Foundry ప్రోటోకాల్ లైబ్రరీలు ఇన్స్టాల్ అవుతాయి: `azure-ai-agentserver-responses` (OpenAI అనుకూల `/responses` ఎండ్ పాయింట్) మరియు `azure-ai-agentserver-invocations` (జనరల్ `/invocations` ఎండ్ పాయింట్).

**2. హోస్టింగ్ ప్రోటోకాల్ ఎంచుకోండి:**

| ప్రోటోకాల్ | హోస్ట్ క్లాస్ | ఎండ్‌పాయింట్ | ఎప్పుడు ఉపయోగించాలంటే |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | మీరు OpenAI అనుకూల చాట్, స్ట్రీమింగ్, ప్రతిస్పందన చరిత్ర మరియు సంభాషణ థ్రెడ్‌లను కోరుతుంటే — చాట్ ఏజెంట్లకు సిఫార్సు చేసిన యథాస్థితి. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | మీరు కస్టమ్ JSON ఆకారం, వెబ్‌హుక్-శైలి ఎండ్‌పాయింట్ లేదా అసంభాషణ ప్రోసెసింగ్ అవసరం ఉంటే. |

ఎందుకంటే **Responses API Foundryలో ఏజెంట్-శైలి అభివృద్ది కోసం ప్రధాన API**, ఎక్కువ ఏజెంట్ల కోసం `ResponsesHostServer` తో ప్రారంభించండి.

**3. పర్యావరణ వేరియబిల్స్‌ను కాన్ఫిగర్ చేయండి** (`az login` ముందుగా చేయండి, తద్వారా `DefaultAzureCredential` ప్రామాణీకరణ అందిస్తుంది):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

ఏజెంట్ తరువాత Foundryలో హోస్టెడ్ ఏజెంట్‌గా నడిచేటప్పుడు, ప్లాట్‌ఫారమ్ ఆటోమేటిక్‌గా `FOUNDRY_PROJECT_ENDPOINT`ని ఇంజెక్ట్ చేస్తుంది.

**4. Responses ప్రోటోకాల్‌పై LangGraph ఏజెంట్‌ను ప్రదర్శించండి:**

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

    # ChatOpenAI ఇక్కడ Foundry ప్రాజెక్టు యొక్క OpenAI-సమర్థన (ప్రతిస్పందనలు) ఎండ్‌పాయింట్‌ను లక్ష్యంగా ఉంచుతుంది.
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

స్థానికంగా `python main.py`తో నడిపించండి, ఆపై `http://localhost:8088/responses`కి Responses అభ్యర్థన పంపండి.

**ప్రధాన ప్రవర్తనలు:**

- **సంభాషణలు**: క్లయింట్లు సంభాషణను `previous_response_id` లేదా `conversation` ID పంపి కొనసాగిస్తారు. మీ గ్రాఫ్ LangGraph చెక్‌పాయింటర్ తో కంపైల్ అయితే, Foundry సంభాషణ స్థితిని చెక్‌పాయింట్ కు కీ చేస్తుంది (ప్రొడక్షన్ లో దీర్ఘచిరకాల చెక్‌పాయింటర్ వాడండి; స్థానిక పరీక్షలకు `MemorySaver` సరిపోతుంది).
- **మానవ-ఇన్-ది-లూప్**: మీరు LangGraph `interrupt()` ఉపయోగిస్తే, `ResponsesHostServer` పెండింగ్ ఇంటరుప్ట్‌ను Responses `function_call` / `mcp_approval_request` అంశంగా ప్రదర్శిస్తుంది, మరియు క్లయింట్లు సరిపోలే `function_call_output` / `mcp_approval_response`తో తిరిగి ప్రారంభిస్తారు.
- **Foundryకి డిప్లాయ్ చేయండి**: Azure Developer CLI ఉపయోగించండి — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (స్థానిక, Docker అవసరం), తరువాత `azd provision` మరియు `azd deploy`. హోస్టెడ్-ఏజెంట్ డిప్లాయ్‌మెంట్ కు **Foundry Project Manager** పాత్ర అవసరం.

ఈ ఉదాహరణ యొక్క నడిపించదగిన సంస్కరణ [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) లో ఉంటుంది. పూర్తి వాక్‌థ్రూ కోసం (Invocations ప్రోటోకాల్, కస్టమ్ రిక్వెస్ట్ స్కీమాలు మరియు సమస్యల పరిష్కారం), చూడండి [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## కోడ్ నమూనాలు 

Microsoft Agent Framework కోసం కోడ్ నమూనాలు ఈ రిపోజిటరీలో `xx-python-agent-framework` మరియు `xx-dotnet-agent-framework` ఫైళ్ళ క్రింద ఉన్నాయి.

## Microsoft Agent Framework గురించి ఇంకేమైనా ప్రశ్నలు ఉన్నాయా?

ఇతర అభ్యాసకులతో కలుసుకోవడానికి, ఆఫీసు గంటలకు హాజరుకావడానికి మరియు మీ AI ఏజెంట్ల ప్రశ్నలకు సమాధానాలు పొందడానికి [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)లో చేరండి.
## గత పాఠం

[AI ఏజెంట్ల కోసం మెమొరీ](../13-agent-memory/README.md)

## తదుపరి పాఠం

[కంప్యూటర్ ఉపయోగ ఏజెంట్లను నిర్మించడం (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->