# మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్‌ను అన్వేషించడం

![Agent Framework](../../../translated_images/te/lesson-14-thumbnail.90df0065b9d234ee.webp)

### పరిచయం

ఈ పాఠం కేవలం కవర్ చేస్తుంది:

- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్‌ను అర్థం చేసుకోవడం: ముఖ్య లక్షణాలు మరియు విలువ  
- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క ముఖ్య సూత్రాలను అన్వేషించడం
- అభివృద్ధి చెందిన MAF నమూనాలు: వర్క్‌ఫ్లోలు, మిడిల్‌వేర్, మరియు మెమరీ

## నేర్చుకొనే లక్ష్యాలు

ఈ పాఠం పూర్తి చేసిన తర్వాత, మీరు ఎలా చేయాలో తెలుసుకోగలరు:

- మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ ఉపయోగించి ప్రొడక్షన్ సిద్ధమైన AI ఏజెంట్స్‌ను నిర్మించడం
- మీ ఏజెంటిక్ ఉపయోగ కేసులకు మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క ప్రాధమిక లక్షణాలను వర్తింపచేసుకోవడం
- వర్క్‌ఫ్లోలు, మిడిల్‌వేర్, మరియు పరిశీలనను సహా అభివృద్ధి చెందిన నమూనాలను ఉపయోగించడం

## కోడ్ నమూనాలు

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) కోసం కోడ్ నమూనాలు ఈ రిపోజిటరీలో `xx-python-agent-framework` మరియు `xx-dotnet-agent-framework` ఫైళ్లలో పొందుపరచబడి ఉన్నాయి.

## మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ అర్థం చేసుకోవడం

![Framework Intro](../../../translated_images/te/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) అనేది మైక్రోసాఫ్ట్ యొక్క ఏ ఐ ఏజెంట్లను నిర్మించడానికి ఏకీకృత ఫ్రేమ్‌వర్క్. ఇది ప్రొడక్షన్ మరియు పరిశోధనా వాతావరణాలలో కనిపించే వివిధ ఏజెంటిక్ ఉపయోగ కేసులకు పరిష్కారం ఇవ్వడానికి సౌకర్యాన్ని అందిస్తుంది:

- **క్రమబద్ధ ఏజెంట్ సమన్వయం** ఆవశ్యకమైన వర్క్‌ఫ్లోలు ఉన్న సందర్భాలలో.
- **సమకాలీన సమన్వయం** ఏజెంట్లు ఒకేసారి పనులను పూర్తి చేయాల్సిన సందర్భాలలో.
- **గ్రూప్ చాట్ సమన్వయం** ఏజెంట్లు ఒకటే పని పై కలిసి పనిచేసే సందర్భాలలో.
- **హాండ్ ఆఫ్ సమన్వయం** ఏజెంట్లు ఉపపనులను పూర్తి చేసిన తర్వాత పనులను ఒకరిని మరొకరికి హస్తాంతరం చేసే సందర్భాలలో.
- **మాగ్నటిక్ సమన్వయం** ఒక మేనేజర్ ఏజెంట్ టాస్క్ జాబితాను సృష్టించి మార్పు చేస్తున్నప్పుడు, ఉప ఏజెంట్ల సమన్వయాన్ని నిర్వహించే సందర్భాలలో.

ప్రొడక్షన్‌లో AI ఏజెంట్లను ప్రదర్శించడానికి, MAF క్రింది లక్షణాలను కూడా కలిగి ఉంది:

- **పరిశీలనతా** OpenTelemetryను ఉపయోగించి, ఏజెంట్ యొక్క ప్రతీ చర్య, టూల్ పిలుపు, సమన్వయ దశలు, తర్క ప్రవాహాలు మరియు Microsoft Foundry డాష్‌బోర్డుల ద్వారా పనితీరు అనుసరణ.
- **భద్రత** Microsoft Foundryలో స్వదేశీగా ఏజెంట్లను హోస్ట్ చేయడం, అందులో రోల్-ఆధారిత ప్రాప్యత నియంత్రణలు, గోప్యమైన డేటా నిర్వహణ మరియు నిర్మిత కంటెంట్ సురక్షత ఉన్నాయి.
- **దృఢత్వం** ఏజెంట్ థ్రెడ్‌లు మరియు వర్క్‌ఫ్లోలు నిలిపివేయడం, పునఃప్రారంభించడం మరియు లోపాల నుంచి కోలుకోవడం సాధ్యం, దీని వల్ల ఎక్కువ కాలం నడిచే ప్రాసెసులు సాధ్యంకాకుండా అవుతాయి.
- **నియంత్రణ** మానవ ఇన్ ది లూప్ వర్క్‌ఫ్లోలను మద్దతు ఇచ్చి, పనులను మానవ అనుమతి కావాలని గుర్తిస్తాయి.

మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ ఇంగేజిబుల్‌గా ఉండటంపై కూడా కేంద్రీకృతమవుతుంది:

- **క్లౌడ్-నిరపేక్షత** - ఏజెంట్లు కంటైనర్లలో, ఆన్-ప్రెమైస్ మరియు పలు క్లౌడ్‌లలో నడుపగలవు.
- **ప్రొవైడర్-నిరపేక్షత** - Azure OpenAI మరియు OpenAI సహా మీ ఇష్టమైన SDK ద్వారా ఏజెంట్లు సృష్టించవచ్చు.
- **ఓపెన్ స్టాండార్డులను అనుసంధానం** - Agent-to-Agent (A2A) మరియు Model Context Protocol (MCP) వంటి ప్రోటోకాల్స్ ద్వారా ఇతర ఏజెంట్లు మరియు టూల్స్‌ను కనుగొని ఉపయోగించవచ్చు.
- **ప్లగిన్లు మరియు కనెక్టర్లు** - Microsoft Fabric, SharePoint, Pinecone మరియు Qdrant వంటి డేటా మరియు మెమరీ సర్వీసులకు కనెక్షన్లు చేయవచ్చు.

ఈ లక్షణాలు మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క కొన్ని ప్రధాన సూత్రాలకు ఎలా వర్తిస్తాయో చూద్దాం.

## మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ ముఖ్య సూత్రాలు

### ఏజెంట్లు

![Agent Framework](../../../translated_images/te/agent-components.410a06daf87b4fef.webp)

**ఏజెంట్లను సృష్టించడం**

ఏజెంట్ సృష్టి అనేది అనుమాన సేవ (LLM ప్రొవైడర్), 
ఏజెంట్ అనుసరించవలసిన సూచనలు మరియు ఒక `name` విధానం నిర్వచించడం ద్వారా చేస్తారు:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

పై కోడ్ `Azure OpenAI` ఉపయోగిస్తోంది కాని ఏజెంట్లు müxtəlif సేవలను ఉపయోగించి సృష్టించవచ్చు, అందులో `Microsoft Foundry Agent Service` కూడా ఉంది:

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

లేదా [MiniMax](https://platform.minimaxi.com/), ఇది OpenAI అనుకూల APIని పెద్ద కంటెక్స్ట్ విండోలతో (204K టోకెన్ల వరకు) అందిస్తుంది:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

లేదా A2A ప్రోటోకాల్ ఉపయోగించి రిమోట్ ఏజెంట్లు:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ఏజెంట్లను నడపడం**

ఏజెంట్లను స్ట్రీమ్ కాని లేదా స్ట్రీమ్ సమాధానాల కోసం `.run` లేదా `.run_stream` పద్ధతులతో నడుపుతారు.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ప్రతి ఏజెంట్ నడపడం కొరకు `max_tokens`, ఏజెంట్ పిలవగల `tools`, మరియు ఏజెంట్ కోసం ఉపయోగించే `model` వంటి పారామితులను అనుకూలం చేసుకోవచ్చు.

ఇది వినియోగదారుల పనులను పూర్తి చేయడానికి ప్రత్యేక మోడల్లు లేదా టూల్స్ అవసరమైన సందర్భాలలో ఉపయోగపడుతుంది.

**టూల్స్**

ఏజెంట్ నిర్వచించేటప్పుడు కూడా టూల్స్ నిర్వచించవచ్చు:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent ను నేరుగా సృష్టిస్తున్నప్పుడు

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

అలాగే ఏజెంట్ నడిపేటప్పుడు కూడా:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ఈ రన్ కోసం మాత్రమే అందించిన సాధనం )
```

**ఏజెంట్ థ్రెడ్స్**

ఏజెంట్ థ్రెడ్స్ బహుళ-టర్న్ సంభాషణలను నిర్వహించడానికి ఉపయోగిస్తారు. థ్రెడ్స్ సృష్టించటం రెండు విధాలుగా జరుగుతుంది:

- `get_new_thread()` ఉపయోగించడం, ఇది థ్రెడ్‌ను కాలక్రమేణా సేవ్ చేయడానికి అనుమతిస్తుంది
- ఏజెంట్ నడుపుతున్నప్పుడు фоне ఆగారని థ్రెడ్‌ను స్వయంచాలకంగా సృష్టించడం మరియు ఆ థ్రెడ్ ప్రస్తుత నడిచే సమయంలో మాత్రమే ఉంటుంది.

థ్రెడ్‌ను సృష్టించడానికి, కోడ్ ఇది ఉంటుంది:

```python
# కొత్త థ్రెడ్ సృష్టించండి.
thread = agent.get_new_thread() # ఆ థ్రెడ్‌తో ఏజెంట్‌ను నడపండి.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

తరువాత ఈ థ్రెడ్‌ను సీరియలైజ్ చేసి భవిష్యత్తులో ఉపయోగానికి స్టోర్ చేయవచ్చు:

```python
# ఒక కొత్త థ్రెడ్ ని సృష్టించండి.
thread = agent.get_new_thread() 

# ఆ థ్రెడ్ తో ఏజెంట్ ని నడపండి.

response = await agent.run("Hello, how are you?", thread=thread) 

# నిల్వ కోసం థ్రెడ్ ని సీరియలైజ్ చేయండి.

serialized_thread = await thread.serialize() 

# నిల్వ నుండి లోడ్ చేసిన తర్వాత థ్రెడ్ స్థితి ని డీసీరియలైజ్ చేయండి.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ఏజెంట్ మిడిల్‌వేర్**

ఏజెంట్లు టూల్స్ మరియు LLMs తో వినియోగదారుల పనులను పూర్తి చేయడానికి పరస్పరం చేస్తాయి. కొన్ని పరిస్థితుల్లో, ఈ పరస్పర చర్యల మధ్య ఎక్కడో నిర్వహణ లేదా ట్రాకింగ్ అవసరం. ఏజెంట్ మిడిల్‌వేర్ ఇది సాధ్యం చేస్తుంది:

*ఫంక్షన్ మిడిల్‌వేర్*

ఈ మిడిల్‌వేర్ ఏజెంట్ మరియు ఫంక్షన్/టూల్ మధ్య ఒక చర్యను అమలు చేయడానికి అనుమతిస్తుంది. ఉదాహరణకు ఫంక్షన్ పిలుపుపై లాగింగ్ చేసుకోవడం అవసరమైతే ఇది ఉపయోగపడుతుంది.

కింది కోడ్‌లో `next` నిర్ణయిస్తుంది తదుపరి మిడిల్‌వేర్ లేదా అసలు ఫంక్షన్ పిలవబడాలా అని.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ప్రీ-ప్రాసెసింగ్: ఫంక్షన్ అమలుకు ముందు లాగ్ చేయండి
    print(f"[Function] Calling {context.function.name}")

    # తదుపరి మిడిల్వేర్ లేదా ఫంక్షన్ అమలుకు కొనసాగించండి
    await next(context)

    # పోస్ట్-ప్రాసెసింగ్: ఫంక్షన్ అమలుకు తర్వాత లాగ్ చేయండి
    print(f"[Function] {context.function.name} completed")
```

*చాట్ మిడిల్‌వేర్*

ఈ మిడిల్‌వేర్ ఏజెంట్ మరియు LLM మధ్య అభ్యర్థనలు మధ్య చర్యను అమలు చేయడానికి లేదా లాగ్ చేయడానికి అనుమతిస్తుంది.

ఇందులో AI సేవకు పంపబడే `messages` వంటి ముఖ్య సమాచారముంటుంది.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ప్రీ-ప్రాసెసింగ్: AI కాల్ ముందు లాగ్ చేయండి
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # తదుపరి మిడ్‌ల్వేర్ లేదా AI సర్వీస్ కు కొనసాగించండి
    await next(context)

    # పోస్ట్-ప్రాసెసింగ్: AI స్పందన తరువాత లాగ్ చేయండి
    print("[Chat] AI response received")

```

**ఏజెంట్ మెమరీ**

`Agentic Memory` పాఠంలో వివరించినట్లుగా, మెమరీ ఏజెంట్‌కు వివిధ సందర్భాలలో పనిచేయడానికి ముఖ్యాంశం. MAF వివిధ రకాల మెమరీలను అందిస్తోంది:

*ఇన్-మెమరీ స్టోరేజ్*

ఇది అప్లికేషన్ రంటైమ్ సమయంలో థ్రెడ్స్‌లో నిల్వ అవుతుంది.

```python
# కొత్త థ్రెడ్‌ను సృష్టించండి.
thread = agent.get_new_thread() # ఆ థ్రెడ్‌తో ఏజెంట్‌ను నడపండి.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*స్థిరమైన సందేశాలు*

ఇది వివిధ సెషన్లలో సంభాషణ చరితాన్ని నిల్వ చేయడానికి ఉపయోగిస్తారు. ఇది `chat_message_store_factory` ఉపయోగించి నిర్వచించబడుతుంది:

```python
from agent_framework import ChatMessageStore

# కస్టమ్ సందేశ నిల్వను సృష్టించండి
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*డైనమిక్ మెమరీ*

ఇది ఏజెంట్లు నడపడంలో ముందే సందర్భంలో జతచేస్తారు. ఈ మెమరీలను mem0 వంటి బాహ్య సేవల్లో నిల్వ చేయవచ్చు:

```python
from agent_framework.mem0 import Mem0Provider

# ఆధునిక మెమరీ శక్తులకు Mem0 ఉపయోగించడం
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

**ఏజెంట్ పరిశీలనతా**


విశ్లేషణ-agentic వ్యవస్థలను నమ్మదగినవి మరియు నిర్వహించదగినవి చేయడానికి ముఖ్యం. MAF మెరుగైన విశ్లేషణ కోసం ట్రేసింగ్ మరియు మీటర్లు అందించడానికి OpenTelemetryతో ఇంటిగ్రేట్ అవుతుంది.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ఏమి చేయాలి
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### వర్క్‌ఫ్లోలు

MAF టాస్క్ పూర్తి చేయడానికి ముందుగా నిర్వచించిన దశలను అందించే వర్క్‌ఫ్లోలను అందిస్తుంది, వాటిలో AI ఏజెంట్లు భాగాలుగా ఉంటాయి.

వర్క్‌ఫ్లోలు మెరుగైన నియంత్రణ ప్రవాహాన్ని అనుమతించే వివిధ భాగాలతో రూపొందించబడతాయి. వర్క్‌ఫ్లోలు **బహుళ ఏజెంట్ సమన్వయం** మరియు **చెక్‌పాయింటింగ్** కూడా సాధ్యంగా చేస్తాయి, వర్క్‌ఫ్లో స్థితులని సేవ్ చేయడానికి.

వర్క్‌ఫ్లో యొక్క మౌలిక భాగాలు:

**ఎగ్జిక్యూటర్లు**

ఎగ్జిక్యూటర్లు ఇన్‌పుట్ సందేశాలను స్వీకరించి, వారి విధులను నిర్వర్తించి, అవుట్‌పుట్ సందేశాన్ని ఉత్పత్తి చేస్తారు. ఇది పెద్ద టాస్క్ పూర్తి వైపు వర్క్‌ఫ్లోని ముందుకు నడిపిస్తుంది. ఎగ్జిక్యూటర్లు AI ఏజెంట్ లేదా కస్టమ్ లాజిక్ కావచ్చు.

**ఎడ్జెస్**

వర్క్‌ఫ్లోలో సందేశాల ప్రవాహాన్ని నిర్వచించడానికి ఎడ్జెస్ ఉపయోగిస్తారు. ఇవి:

*డైరెక్ట్ ఎడ్జెస్* - ఎగ్జిక్యూటర్ల మధ్య సరళమైన ఒకటి నుండి ఒకటి కలయికలు:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*కండీషనల్ ఎడ్జెస్* - నిర్దిష్ట పరిస్థితి తీరిన తర్వాత సక్రియం అవుతున్నవి. ఉదాహరణకు, హోటల్ గదులు అందుబాటులో లేనప్పుడు, ఎగ్జిక్యూటర్ ఇతర ఎంపికలను సూచించవచ్చు.

*స్విచ్-కేస్ ఎడ్జెస్* - నిర్వచించిన పరిస్థితుల ఆధారంగా సందేశాలను వివిధ ఎగ్జిక్యూటర్లకు మార్గనిర్దేశం చేస్తాయి. ఉదాహరణకి, ప్రయాణ వినియోగదారునికి ప్రాధాన్య ప్రాప్యత ఉంటే వారి టాస్కులను ఇతర వర్క్‌ఫ్లో ద్వారా నిర్వహిస్తారు.

*ఫ్యాన్-అవుట్ ఎడ్జెస్* - ఒక సందేశాన్ని బహుళ లక్ష్యాలకు పంపడం.

*ఫ్యాన్-ఇన్ ఎడ్జెస్* - వేర్వేరు ఎగ్జిక్యూటర్ల నుండి బహుళ సందేశాలను సేకరించి ఒక లక్ష్యానికి పంపటం.

**ఈవెంట్స్**

వర్క్‌ఫ్లోలలో మెరుగైన విశ్లేషణ కోసం, MAF అమలు సంభవించే ఈవెంట్స్‌ను అందిస్తుంది, వీటిలో:

- `WorkflowStartedEvent`  - వర్క్‌ఫ్లో అమలు ప్రారంభమవుతుంది
- `WorkflowOutputEvent` - వర్క్‌ఫ్లో అవుట్‌పుట్ ఉత్పత్తి చేస్తుంది
- `WorkflowErrorEvent` - వర్క్‌ఫ్లోలో లోపం సంభవిస్తుంది
- `ExecutorInvokeEvent`  - ఎగ్జిక్యూటర్ ప్రాసెసింగ్ ప్రారంభం
- `ExecutorCompleteEvent`  -  ఎగ్జిక్యూటర్ ప్రాసెసింగ్ ముగింపు
- `RequestInfoEvent` - అభ్యర్థన జారీ చేయబడింది

## అధునాతన MAF ప్యాటర్న్లు

పై విభాగాలు Microsoft Agent Framework యొక్క ముఖ్య భావనలు కవర్ చేస్తాయి. మీరు మరింత సంక్లిష్ట ఏజెంట్లను నిర్మిస్తున్నప్పుడు పరిగణించవలసిన కొన్ని అధునాతన ప్యాటర్న్లు:

- **మిడిల్‌వేర్ కంపోజిషన్**: ఏజెంట్ ప్రవర్తనపైన ఖచ్చితమైన నియంత్రణ కోసం ఫంక్షన్ మరియు చాట్ మిడిల్‌వేర్ ఉపయోగించి బహుళ మిడిల్‌వేర్ హ్యాండ్లర్లను (లॉगింగ్, ఆథ్, రేట్ లిమిటింగ్) మళ్ళీ కట్టు.
- **వర్క్‌ఫ్లో చెక్పాయింటింగ్**: వర్క్‌ఫ్లో ఈవెంట్స్ మరియు సీరియలైజేషన్ ఉపయోగించి దీర్ఘకాలిక ఏజెంట్ ప్రక్రియలను సేవ్ చేసి పునఃప్రారంభించుట.
- **డైనమిక్ టూల్ ఎంపిక**: టూల్ వివరణలపై RAG ని MAF యొక్క టూల్ రిజిస్ట్రేషన్ తో కలిపి ప్రశ్నకు మాత్రమే సంబంధించిన టూల్స్ అందించడం.
- **బహుళ ఏజెంట్ హ్యాండ్ఓఫ్**: ప్రత్యేక ఏజెంట్ల మధ్య హ్యాండ్ఓఫ్‌లను సమన్వయింపజేయడానికి వర్క్‌ఫ్లో ఎడ్జెస్ మరియు శ్రితదర్శి రూటింగ్ ఉపయోగించు.

## Microsoft Foundry పై LangChain / LangGraph ఏజెంట్ల ఆతిథ్యం

Microsoft Agent Framework **ఫ్రేమ్‌వర్క్-పరస్పరసంబంధపూర్వకం** — మీరు MAFతో రాయబడిన ఏజెంట్లకు పరిమితనంగా ఉండరు. మీరు ఇప్పటికే **LangChain** లేదా **LangGraph**తో ఏజెంట్ నిర్మించి ఉంటే, దాన్ని **Microsoft Foundry హోస్టెడ్ ఏజెంట్**గా నడపవచ్చు, తద్వారా Foundry ఆ runtime, సెషన్స్, స్కేలింగ్, ఐడెంటిటీ మరియు ప్రోటోకాల్ ఎండ్పాయింట్లను నిర్వహిస్తుంది, మీ ఏజెంట్ లాజిక్ LangGraph లో ఇరుగుపడుతుంది.

ఇది `langchain_azure_ai.agents.hosting` ప్యాకేజీతో చేయబడుతుంది, ఇది Foundry హోస్టెడ్ ఏజెంట్లు ఉపయోగించే అదే ప్రోటోకాల్స్‌పై కంపైల్ అయిన LangGraph గ్రాఫ్‌ను వెల్లడిస్తుంది.

**1. హోస్టింగ్ ఎక్స్‌ట్రాను ఇన్స్టాల్ చేయండి:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` ఎక్స్‌ట్రా Foundry ప్రోటోకాల్ లైబ్రరీలను ఇన్స్టాల్ చేస్తుంది: `azure-ai-agentserver-responses` (OpenAI-పరిచిత `/responses` ఎండ్పాయింట్) మరియు `azure-ai-agentserver-invocations` (సాధారణ `/invocations` ఎండ్పాయింట్).

**2. హోస్టింగ్ ప్రోటోకాల్ ఎంచుకోండి:**

| ప్రోటోకాల్ | హోస్ట్ క్లాస్ | ఎండ్పాయింట్ | ఎప్పుడు ఉపయోగించాలి |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI-పరిచిత చాట్, స్ట్రీమింగ్, స్పందన చరిత్ర మరియు సంభాషణ థ్రెడింగ్ కావాలనుకుంటే — సంభాషణ ఏజెంట్లకు సిఫార్సు చేసిన డిఫాల్ట్. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | కస్టమ్ JSON ఆకారం, వెబ్‌హుక్-శైలి ఎండ్పాయింట్ లేదా అఘటిత ప్రాసెసింగ్ అవసరమైతే. |

ఎందుకంటే **Responses API Foundryలో ఏజెంట్ శైలి అభివృద్ధి కోసం ప్రధాన API** కాబట్టి, చాలా ఏజెంట్లకు `ResponsesHostServer` తో ప్రారంభించండి.

**3. పరిసర వేరియబుల్స్ సెటప్ చేయండి** (`az login` ముందు `DefaultAzureCredential` ఆథెంటికేట్ చేయడానికి):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

ఏజెంట్ తర్వాత Foundryలో హోస్టెడ్ ఏజెంట్‌గా నడిచేటప్పుడు, ప్లాట్‌ఫారమ్ স্বయంచాలకంగా `FOUNDRY_PROJECT_ENDPOINT` ని ఇంజెక్ట్ చేస్తుంది.

**4. Responses ప్రోటోకాల్ పై LangGraph ఏజెంట్‌ను ప్రదర్శించండి:**

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

    # ChatOpenAI ఇక్కడ Foundry ప్రాజెక్ట్ యొక్క OpenAI- అనుకూల (ప్రతిస్పందనలు) ఎండ్‌పాయింట్‌ను లక్ష్యం చేస్తుంది.
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

`python main.py` తో స్థానికంగా నడపండి, తరువాత `http://localhost:8088/responses` కు Responses అభ్యర్థన పంపండి.

**ప్రధాన ప్రవర్తనలు:**

- **సంభాషణలు**: క్లయింట్లు `previous_response_id` లేక `conversation` ID ను అందజేసి సంభాషణ కొనసాగిస్తాయి. మీ గ్రాఫ్ LangGraph చెక్పాయింటర్ తో కంపైల్ అయితే, Foundry సంభాషణ స్థితిని చెక్పాయింట్‌కు కీ చేస్తుంది (ఉత్పత్తిలో మెటిరియల్ చెక్పాయింటర్ ఉపయోగించండి; లోకల్ టెస్టింగ్ కు `MemorySaver` సరిపోతుంది).
- **హ్యూమన్-ఇన్-ది-లూప్**: మీ గ్రాఫ్ LangGraph `interrupt()` ఉపయోగిస్తే, `ResponsesHostServer` పెండింగ్ ఇంటరప్트를 Responses `function_call` / `mcp_approval_request` ఐటమ్ గా ప్రదర్శిస్తుంది, మరియు క్లయింట్లు సరిపోయే `function_call_output` / `mcp_approval_response` తో కొనసాగుతాయి.
- **Foundryకి పంపండి**: Azure Developer CLI ఉపయోగించండి — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (లోకల్, Docker అవసరం), తరువాత `azd provision` మరియు `azd deploy` చేయండి. హోస్టెడ్-ఏజెంట్ పంపిణీకి **Foundry ప్రాజెక్ట్ మేనేజర్** పాత్ర అవసరం.

ఈ ఉదాహరణకు నడిపించదగిన వెర్షన్ [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) లో ఉంది. పూర్తి వాక్ త్రూ (Invocations ప్రోటోకాల్, కస్టమ్ అభ్యర్థన స్కీమాలు మరియు సమస్యల పరిష్కారం) కోసం, [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) చూడండి.

## కోడ్ నమూనాలు

Microsoft Agent Framework కోడ్ నమూనాలు ఈ రిపోజిటరీలో `xx-python-agent-framework` మరియు `xx-dotnet-agent-framework` ఫైళ్ల కింద లభిస్తాయి.

## Microsoft Agent Framework గురించి మరిన్ని ప్రశ్నలు ఉన్నాయా?

ఇతర అభ్యాసకులతో కలవడానికి, ఆఫీసు గంటలకు హాజరవడానికి మరియు మీ AI ఏజెంట్ల ప్రశ్నలకు సమాధానాలు పొందడానికి [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) చేరండి.
## మునుపటి పాఠం

[AI ఏజెంట్ల కోసం మెమరీ](../13-agent-memory/README.md)

## తరువాత పాఠం

[కంప్యూటర్ వినియోగ ఏజెంట్లు (CUA) నిర్మించడం](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->