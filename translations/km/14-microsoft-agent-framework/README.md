# ការស្វែងរក Microsoft Agent Framework

![Agent Framework](../../../translated_images/km/lesson-14-thumbnail.90df0065b9d234ee.webp)

### មតិយោបល់ផ្ដើម

មេរៀននេះនឹងគ្របដណ្តប់៖

- ការយល់ដឹងអំពី Microsoft Agent Framework: លក្ខណៈសំខាន់ និងតម្លៃ  
- ការស្វែងរកគំនិតមូលដ្ឋាននៃ Microsoft Agent Framework
- លំនាំ MAF ខ្ពស់: ការងារ Workflow, Middleware និង Memory

## គោល​បំណង​រៀន

បន្ទាប់ពីបញ្ចប់មេរៀននេះ អ្នកនឹងដឹងរបៀប:

- សាងសង់ AI Agents ដែលមានស្រាប់សម្រាប់ផលិតកម្មដោយប្រើ Microsoft Agent Framework
- ប្រើលក្ខណៈសម្បត្តិមូលដ្ឋានរបស់ Microsoft Agent Framework ទៅកាន់ករណីប្រើប្រាស់ Agentic របស់អ្នក
- ប្រើលំនាំខ្ពស់រួមមាន workflow, middleware និងការសង្កេតឃើញ

## គំរូកូដ 

គំរូកូដសម្រាប់ [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) អាចរកឃើញបាននៅក្នុង repository នេះក្រោមឯកសារ `xx-python-agent-framework` និង `xx-dotnet-agent-framework`។

## ការយល់ដឹងអំពី Microsoft Agent Framework

![Framework Intro](../../../translated_images/km/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) គឺជាស៊ុមផ្ដុំរួមមួយរបស់ Microsoft សម្រាប់បង្កើត AI agents។ វាប្រគល់នូវភាពបត់បែនដើម្បីដោះស្រាយករណីប្រើប្រាស់ agentic ដែលមានជាច្រើនដែលមើលឃើញបានទាំងក្នុងបរិស្ថានផលិតកម្ម និងស្រាវជ្រាវរួមមាន៖

- **ការគ្រប់គ្រង Agent តាមជំហាន** ក្នុងស្ថានការណ៍ដែលត្រូវការចងក្រង workflow ជាដើម។
- **ការគ្រប់គ្រងពហុដំណើរការ** ក្នុងស្ថានការណ៍ដែល agents ត្រូវបញ្ចប់ភារកិច្ចជាមួយគ្នាឲ្យបានស្ទើមៗនៅពេលតែមួយ។
- **ការគ្រប់គ្រងការជជែកជាក្រុម** ក្នុងស្ថានការណ៍ដែល agents អាចសហការជាមួយគ្នានៅលើភារកិច្ចមួយ។
- **ការគ្រប់គ្រងការផ្ទេរ** ក្នុងស្ថានការណ៍ដែល agents ផ្ទេរភារកិច្ចទៅគ្នាក្នុងពេលដែលភារកិច្ចរងត្រូវបានបញ្ចប់។
- **ការគ្រប់គ្រងម៉ាញេទិច** ក្នុងស្ថានការណ៍ដែល agent គ្រប់គ្រងបង្កើតនិងកែប្រែបញ្ជីភារកិច្ច ហើយដោះស្រាយនូវការសម្របសម្រួលរវាង subagents ដើម្បីបញ្ចប់ភារកិច្ច។

ដើម្បីផ្ដល់ AI Agents ក្នុងផលិតកម្ម MAF ក៏បានរួមបញ្ចូលលក្ខណៈសំខាន់សម្រាប់៖

- **ការសង្កេតឃើញ** តាមរយៈការប្រើប្រាស់ OpenTelemetry ដែលសកម្មភាពរាល់យ៉ាងរបស់ AI Agent រួមមានការហៅឧបករណ៍ ជំហាន orchestration, ដំណើរការពិចារណា និងការត្រួតពិនិត្យគុណភាពតាមរយៈ dashboard Microsoft Foundry។
- **សុវត្ថិភាព** ដោយផ្ទុក agents ដោយដើមនៅលើ Microsoft Foundry ដែលរួមបញ្ចូលការត្រួតពិនិត្យសុវត្ថិភាពដូចជា ការចូលប្រើដោយមនុស្សតាមតួនាទី ការគ្រប់គ្រងទិន្នន័យឯកជន និងសុវត្ថិភាពមាតិកាដែលមានក្នុងគេហារ។
- **ភាពរឹងមាំ** ដោយសារច្រើន Thread និង workflow របស់ Agent អាចផ្អាក់បន្ត និងស្ដារឡើងវិញពីកំហុស ដែលអាចអនុញ្ញាតឱ្យមានដំណើរវែងជាងមុន។
- **ការគ្រប់គ្រង** ដោយមាន workflow ដែលមានមនុស្សក្នុងលក្ខណៈផ្ទាល់ក្នុងដំណើរការ ដែលភារកិច្ចត្រូវបានសម្គាល់ថាត្រូវការការយល់ព្រមពីមនុស្ស។

Microsoft Agent Framework ក៏ផ្តោតលើការអាចប្រើរួមបានដោយ៖

- **មិនពឹងផ្អែកលើCloud** - Agents អាចដំណើរការនៅក្នុង containers, ទីតាំងក្នុងបរិក្ខារនិងលើClouds ពហុប្រភេទ។
- **មិនពឹងផ្អែកលើអ្នកផ្គត់ផ្គង់** - Agents អាចត្រូវបានបង្កើតតាម SDK ដែលអ្នកចូលចិត្ត រួមមាន Azure OpenAI និង OpenAI
- **ការចូលរួមនូវស្តង់ដារពិព័រណ៍បើក** - Agents អាចប្រើប្រាស់ពិធីការដូចជា Agent-to-Agent(A2A) និង Model Context Protocol (MCP) ដើម្បីរកឃើញនិងប្រើប្រាស់ agents និងឧបករណ៍ផ្សេងទៀត។
- **Plugins និង Connectors** - ការតភ្ជាប់អាចត្រូវបានធ្វើទៅកាន់សេវាកម្មទិន្នន័យ និង memory ដូចជា Microsoft Fabric, SharePoint, Pinecone និង Qdrant។

យើងមកមើលថាលក្ខណៈសំខាន់ទាំងនេះត្រូវបានអនុវត្តដោយរបៀបណាចំពោះគំនិតមូលដ្ឋានមួយចំនួននៃ Microsoft Agent Framework។

## គំនិតសំខាន់ៗរបស់ Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/km/agent-components.410a06daf87b4fef.webp)

**ការបង្កើត Agents**

ការបង្កើត Agent ត្រូវបានធ្វើដោយកំណត់សេវាកម្មនិយាយផ្សំ (LLM Provider), ការណែនាំសម្រាប់ AI Agent ដើម្បីអនុវត្តន៍ និងលេខឈ្មោះ `name` ដែលបានផ្ដល់៖


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ខាងលើប្រើប្រាស់ `Azure OpenAI` ប៉ុន្តែ agents អាចត្រូវបានបង្កើតដោយសេវាកម្មជាច្រើនរួមមាន `Microsoft Foundry Agent Service`។

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

API OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ឬ [MiniMax](https://platform.minimaxi.com/), ដែលផ្តល់ API ផ្គូរផ្គង OpenAI ជាមួយវីនដូ context ធំ (រហូតដល់ 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ឬ agents ពីចម្ងាយដោយប្រើពិធីការពីរបៀប A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ការដំណើរការ Agents**

Agents ត្រូវបានដំណើរការ​ដោយប្រើ `.run` ឬ `.run_stream` សម្រាប់ការឆ្លើយតបរបស់មិនម៉ោងចំហៀង ឬ មានម៉ោងចំហៀង។

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ការរត់ agent អាចមានជម្រើសប្តូរប៉ារ៉ាម៉ែត្រដូចជា `max_tokens` ដែលបានប្រើដោយ agent, `tools` ដែល agent អាចហៅ, រួមទាំង `model` ដែលរបស់ agent ផ្ទាល់ដែរ។

នេះមានប្រយោជន៍ក្នុងករណីដែលតម្រូវឲ្យបំផុតនូវម៉ូដែលឬឧបករណ៍ជាក់លាក់សម្រាប់បញ្ចប់ភារកិច្ចរបស់អ្នកប្រើ។

**ឧបករណ៍**

ឧបករណ៍អាចកំណត់ទាំងពេលកំណត់ agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ពេលបង្កើត ChatAgent ដោយផ្ទាល់

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

និងពេលដំណើរការ agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ឧបករណ៍ផ្តល់ជូនសម្រាប់ការរត់នេះប៉ុណ្ណោះ)
```

**Agent Threads**

Agent Threads ត្រូវបានប្រើសម្រាប់គ្រប់គ្រងការសន្ទនាច្រើនជំហាន។ Threads អាចត្រូវបានបង្កើតដោយ៖

- ប្រើ `get_new_thread()` ដែលអនុញ្ញាតឲ្យ thread នោះត្រូវរក្សាទុកជាបណ្តោះអាសន្ន
- បង្កើត thread ស្វ័យប្រវត្តិពេលដំណើរការ agent ហើយ thread នោះសុទ្ធតែមានអាយុកាលនៅពេលដំណើរការបច្ចុប្បន្នតែប៉ុណ្ណោះ។

ដើម្បីបង្កើត thread កូដមានរបៀបដូចខាងក្រោម៖

```python
# បង្កើតខ្សែប្រឡាយថ្មីមួយ។
thread = agent.get_new_thread() # បើកប្រតិភូជាមួយខ្សែប្រឡាយ។
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

អ្នកអាចស៊េរីនៃ thread ដើម្បីរក្សាទុកសម្រាប់ប្រើប្រាស់ក្រោយបាន:

```python
# បង្កើតខ្សែថ្មីមួយ។
thread = agent.get_new_thread() 

# ដំណើរការភ្នាក់ងារជាមួយខ្សែ។

response = await agent.run("Hello, how are you?", thread=thread) 

# ស៊េរ៊ីថលខ្សែសម្រាប់ផ្ទុក។

serialized_thread = await thread.serialize() 

# បំបញ្ចេញស្ថានភាពខ្សែមកវិញបន្ទាប់ពីផ្ទុកពីការផ្ទុក។

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agents បញ្ចេញសកម្មភាពជាមួយឧបករណ៍ និង LLMs ដើម្បីបញ្ចប់ភារកិច្ចរបស់អ្នកប្រើ។ ក្នុងស្ថានការណ៍ខ្លះ យើងចង់អនុវត្តឬតាមដាននៅចន្លោះនៃសកម្មភាពទាំងនេះ។ Agent middleware អនុញ្ញាតឲ្យយើងធ្វើបានវិញតាមរយៈ៖

*Function Middleware*

Middleware នេះអនុញ្ញាតឲ្យយើងអនុវត្តសកម្មភាពរវាង agent និងមុខងារ/ឧបករណ៍ដែលវានឹងហៅ។ ឧទាហរណ៍ដែលប្រើប្រាស់ middleware នេះគឺពេលដែលអ្នកចង់ធ្វើការចុះក្នុងកំណត់ហេតុលើការហៅមុខងារ។

ក្នុងកូដខាងក្រោម `next` កំណត់ថាតើ middleware បន្ទាប់ឬមុខងារពិតប្រាកដគួរត្រូវបានហៅ។

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ការបំរែបំរួលមុន: កំណត់ហាក់សំរាប់មុនការអនុវត្តមុខងារ
    print(f"[Function] Calling {context.function.name}")

    # បន្តទៅ middleware ឬអនុវត្តមុខងារបន្ត
    await next(context)

    # ការបំរែបំរួលបន្ទាប់: កំណត់ហាក់សំរាប់បន្ទាប់ការអនុវត្តមុខងារ
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Middleware នេះអនុញ្ញាតឲ្យយើងអនុវត្តឬចុះកំណត់ហេតុសកម្មភាពរវាង agent និងសំណើរផ្សេងៗរបស់ LLM។

វាមានព័ត៌មានសំខាន់ដូចជា `messages` ដែលត្រូវបានផ្ញើទៅសេវាកម្ម AI។

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ការប្រាស្រ័យព្រឹក្សា៖ កំណត់ហេតុនៅមុនហៅ AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # បន្តទៅ middleware បន្ទាប់ឬសេវា AI
    await next(context)

    # ការប្រាស្រ័យបន្ទាប់៖ កំណត់ហេតុនៅបន្ទាប់ពេលទទួលបានការឆ្លើយតបពី AI
    print("[Chat] AI response received")

```

**Agent Memory**

ដូចបានបង្ហាញក្នុងមេរៀន `Agentic Memory`, memory គឺជាធាតុសំខាន់សម្រាប់អនុញ្ញាតឲ្យ agent ដំណើរការនៅលើ context ចម្រុះ។ MAF ផ្តល់ memory ពីប្រភេទផ្សេងៗ៖

*In-Memory Storage*

Memory នេះគឺសម្រាប់រក្សាទុកនៅក្នុង threads ក្នុងអំឡុងពេលដំណើរការកម្មវិធី។

```python
# បង្កើតខ្សែថ្មីមួយ។
thread = agent.get_new_thread() # រត់ភ្នាក់ងារជាមួយខ្សែ។
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Memory នេះប្រើសម្រាប់រក្សាទុកប្រវត្តិសន្ទនា ឆ្លងកាត់សម័យផ្សេងៗ។ វាត្រូវបានកំណត់ដោយប្រើ `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# បង្កើតហាងសារប្រាក់ផ្ទាល់ខ្លួន
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamic Memory*

Memory នេះត្រូវបន្ថែមទៅក្នុង context មុនពេល agents ដំណើរការ។ មេម៉ូរីទាំងនេះអាចត្រូវបានរក្សាទុកនៅក្នុងសេវាកម្មខាងក្រៅដូចជា mem0:

```python
from agent_framework.mem0 import Mem0Provider

# កំពុងប្រើ Mem0 សម្រាប់សមត្ថភាពតម្រឹមអនុទ្រព្យស្មារតីកម្រិតខ្ពស់
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

**Agent Observability**

Observability គឺសំខាន់សម្រាប់កសាងប្រព័ន្ធ agentic ដែលអាចទុកចិត្តបាន និងថែរក្សាកាន់តែប្រសើរ។ MAF សម្របខ្លួនជាមួយ OpenTelemetry ដើម្បីផ្ដល់ tracing និង meter សម្រាប់ការសង្កេតឃើញប្រសើរឡើង។

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ធ្វើអ្វីមួយ
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflow

MAF ផ្តល់នូវ workflow ដែលជាជំហានដែលបានកំណត់ជាមុនសម្រាប់បញ្ចប់ភារកិច្ច និងរួមបញ្ចូល AI agents ជាផ្នែកមួយក្នុងជំហានទាំងនោះ។

Workflow ត្រូវបានបង្កើតពីផ្នែកផ្សេងៗដែលអនុញ្ញាតចូលចិត្តល្អឡើងនូវការត្រួតពិនិត្យចរន្ត។ Workflow ក៏ធ្វើអោយអាចមាន **multi-agent orchestration** និង **checkpointing** ដើម្បីរក្សាទុកស្ថានភាព workflow។

ផ្នែកសំខាន់នៃ workflow មាន:

**Executors**

Executors ទទួលសារចូល, អនុវត្តភារកិច្ចដែលបានចាត់តាំង ហើយបង្កើតសារចេញ។ នេះជំរុញ workflow ទៅខាងមុខដើម្បីបញ្ចប់ភារកិច្ចធំទូលាយជាង។ Executors អាចជាជំនាញ AI agent ឬ តម្លៃ logic ផ្ទាល់ខ្លួន។

**Edges**

Edges ត្រូវបានប្រើសម្រាប់កំណត់ចរន្តសារជាលំដាប់នៅ workflow។ វាអាចជារៀងខាងក្រោម៖

*Direct Edges* - ការតភ្ជាប់តាមវិធីមួយទៅមួយរវាង executors:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - បើកអខ័ណ្ឌបន្ទាប់ពីលក្ខខណ្ឌមួយបានបំពេញ។ ជាឧទាហរណ៍ នៅពេលបន្ទប់សណ្ឋាគារមិនអាចប្រើបាន អ្នកបំពេញភារកិច្ចអាចផ្ដល់ជម្រើសផ្សេងទៀត។

*Switch-case Edges* - ផ្សាយសារទៅ executors ផ្សេងៗជាបណ្តឹងនៃលក្ខខណ្ឌដែលបានកំណត់។ ជាឧទាហរណ៍ ប្រសិនបើអតិថិជនធ្វើដំណើរមានអាទិភាព ចំណាត់ថ្នាក់នឹងត្រូវបានដោះស្រាយតាម workflow ផ្សេងទៀត។

*Fan-out Edges* - ផ្ញើសារមួយទៅគោលដៅច្រើន។

*Fan-in Edges* - ប្រមូលសារពី executors ច្រើន និងផ្ញើទៅគោលដៅមួយ។

**Events**

ដើម្បីផ្ដល់នូវការសង្កេតឃើញល្អបំផុតចូលទៅក្នុង workflow, MAF ផ្ដល់នូវព្រឹត្តិការណ៍ដែលបានបង្កើតមុនសម្រាប់ការអនុវត្តរួមមាន៖

- `WorkflowStartedEvent`  - ការចាប់ផ្តើមការអនុវត្ត workflow
- `WorkflowOutputEvent` - Workflow ផ្ដល់ផលប៉ៈពាល់
- `WorkflowErrorEvent` - Workflow ស្ថិតក្នុងកំហុស
- `ExecutorInvokeEvent`  - Executor កំពុងចាប់ផ្តើមដំណើរការ
- `ExecutorCompleteEvent`  -  Executor បានបញ្ចប់ដំណើរការ
- `RequestInfoEvent` - មានសំណើមួយត្រូវបានបញ្ចេញ

## លំនាំ MAF ខ្ពស់

ផ្នែកខាងលើបានគ្របដណ្តប់គំនិតសំខាន់នៃ Microsoft Agent Framework។ ខណៈដែលអ្នកសាងសង់ agents ដែលស្មុគស្មាញ ក៏មានលំនាំខ្ពស់មួយចំនួនដែលគួរប្រុងប្រយ័ត្ន៖

- **Middleware Composition**: ចងភ្ជាប់អ្នកចាប់ middleware ច្រើន (logging, authentication, rate-limiting) ដោយប្រើ function និង chat middleware សម្រាប់ការត្រួតពិនិត្យរបៀប agent យ៉ាងក្នុងលម្អិត។
- **Workflow Checkpointing**: ប្រើព្រឹត្តិការណ៍ workflow និង serialization ដើម្បីរក្សាទុក និងបន្តដំណើរការអាយុកាលវែងរបស់ agent។
- **Dynamic Tool Selection**: ផ្សំ RAG លើការពិពណ៌នាឧបករណ៍ជាមួយបញ្ជីចុះបញ្ជីឧបករណ៍ MAF ដើម្បីបង្ហាញឧបករណ៍ដែលពាក់ព័ន្ធត្រឹមតែសម្រាប់សំណួរ។
- **Multi-Agent Handoff**: ប្រើមាត់ទន្លេ workflow និងការបញ្ជូនតាមលក្ខខណ្ឌសម្រាប់ការគ្រប់គ្រងការផ្ទេរភារកិច្ចរវាង agents ឯកទេសគ្នា។

## ការតំលើង LangChain / LangGraph Agents លើ Microsoft Foundry

Microsoft Agent Framework គឺ **អាចប្រើរួមបានជាមួយ framework ផ្សេងៗ** — អ្នកមិនត្រូវបានកំណត់ត្រឹមតែagents ដែលបានសរសេរដោយ MAF ទេ។ ប្រសិនបើអ្នកមាន agent ដែលបានបង្កើតដោយ **LangChain** ឬ **LangGraph** អ្នកអាចដំណើរការវាជា **agent ដែលបម្រើដោយ Microsoft Foundry** ដើម្បីឲ្យ Foundry គ្រប់គ្រងរយៈពេលដំណើរការ, សម័យ, ការពង្រីក, អត្តសញ្ញាណ និងចុងបញ្ចប់ពិធីការសម្រាប់អ្នក ខណៈពេលដែល logic agent របស់អ្នកនៅក្នុង LangGraph។

នេះត្រូវបានអនុវត្តជាមួយ package `langchain_azure_ai.agents.hosting` ដែលបង្ហាញនូវតំណាង LangGraph ផ្តិតតាមពិធីការដដែលដែល agent ផ្តល់ជូនដោយ Foundry ប្រើ។

**១. តំម្លើង hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Hosting extra នេះតំម្លើងអាសយដ្ឋាន protocol Foundry: `azure-ai-agentserver-responses` (ចុងបញ្ចប់ OpenAI-compatible `/responses`) និង `azure-ai-agentserver-invocations` (ចុងបញ្ចប់ទូទៅ `/invocations`)។

**២. ជ្រើសរើស protocol hosting:**

| Protocol | Host class | Endpoint | ប្រើនៅពេល |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | អ្នកចង់បាន chat, streaming, ប្រវត្តិការឆ្លើយ, និង threading សន្ទនា ដែលត្រូវបានផ្ដល់ជាមូលដ្ឋានសម្រាប់ agents លេខសម្គាល់ជជែកនិយម។ |
| **Invocations** | `InvocationsHostServer` | `/invocations` | អ្នកត្រូវការទ្រង់ទ្រាយ JSON ផ្ទាល់ខ្លួន, ចុងបញ្ចប់ដូច webhook ឬដំណើរការមិនមែនជាសន្ទនា។ |

ពីព្រោះ **Responses API គឺជាអាសយដ្ឋាន API សំខាន់សម្រាប់ការអភិវឌ្ឍ agent នៅ Foundry**, ចាប់ផ្តើមជាមួយ `ResponsesHostServer` សម្រាប់ agents ច្រើន។

**៣. កំណត់អថេរបរិវេណ** (`az login` មុនដើម្បីអោយ `DefaultAzureCredential` អាចផ្ទៀងផ្ទាត់បាន):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

នៅពេល agent រត់ជាបន្ទាប់មកជា agent បម្រើនៅ Foundry វេទិកានេះនឹងបញ្ចូល `FOUNDRY_PROJECT_ENDPOINT` ដោយស្វ័យប្រវត្តិ។

**៤. បង្ហាញ agent LangGraph តាម protocol Responses៖**

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

    # ChatOpenAI នៅទីនេះគោលដៅទៅកាន់ច្រកតភ្ជាប់ស្រប OpenAI (Responses) របស់គម្រោង Foundry។
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

ដំណើរការចូលក្នុង localhost ដោយ `python main.py` បន្ទាប់មកផ្ញើសំណើ Responses ទៅ `http://localhost:8088/responses`។

**អាកប្បកិរិយាសំខាន់ៗ:**

- **ការជជែក**: អតិថិជនបន្តកិច្ចសន្ទនា ដោយផ្ញើ `previous_response_id` ឬ `conversation` ID ។ ប្រសិនបើ graph របស់អ្នកបានបង្កើតជាមួយជន់ត្រួតពិនិត្យរបស់ LangGraph, Foundry នឹងគឺនូវស្ថានភាពជជែកទៅ checkpoint (ប្រើ durable checkpointer នៅផលិតកម្ម; `MemorySaver` ល្អសម្រាប់សាកល្បងក្នុងស្រុក)។
- **មនុស្សក្នុងចរន្ត**: ប្រសិនបើ graph របស់អ្នកប្រើ LangGraph `interrupt()`, `ResponsesHostServer` នឹងបង្ហាញការរាំងស្ទះដែលកំពុងរង់ចាំជា Responses `function_call` / `mcp_approval_request` ហើយអតិថិជននឹងបន្តជាមួយ `function_call_output` / `mcp_approval_response` ផ្គូរផ្គង។
- **ចាក់ចេញទៅ Foundry**: ប្រើ Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ក្នុងស្រុក, តម្រូវការជាមួយ Docker), បន្ទាប់មក `azd provision` និង `azd deploy`។ ការចាក់ចេញ hosted-agent ទាមទារតួនាទី **Foundry Project Manager**។

ជំនួញនៃឧទាហរណ៍នេះរស់នៅ [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)។ សម្រាប់ការណែនាំពេញលេញ (protocol Invocations, schemas សំណើផ្ទាល់ខ្លួន និងការដោះស្រាយបញ្ហា) សូមមើល [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)។

## គំរូកូដ 

គំរូកូដសម្រាប់ Microsoft Agent Framework អាចរកឃើញនៅ repository នេះក្រោមឯកសារ `xx-python-agent-framework` និង `xx-dotnet-agent-framework`។

## តើអ្នកមានសំណួរបន្ថែមអំពី Microsoft Agent Framework មែនទេ?

ចូលរួមនៅក្នុង [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ដើម្បីជួបជាមួយអ្នករៀនផ្សេងទៀត, ចូលរួមកណ្តាលម៉ោងការិយាល័យ និងទទួលបានចម្លើយសម្រាប់សំណួរអំពី AI Agents របស់អ្នក។
## មេរៀនមុន

[Memory for AI Agents](../13-agent-memory/README.md)

## មេរៀនបន្ទាប់

[Building Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->