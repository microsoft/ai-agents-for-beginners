# ការស្វែងយល់អំពី Microsoft Agent Framework

![Agent Framework](../../../translated_images/km/lesson-14-thumbnail.90df0065b9d234ee.webp)

### ការណែនាំ

មេរៀននេះនឹងគ្របដណ្តប់៖

- ការយល់ដឹងអំពី Microsoft Agent Framework៖ លក្ខណៈសម្បត្តិសំខាន់ និងតម្លៃ  
- ការស្វែងយល់អំពីគំនិតសំខាន់ៗនៃ Microsoft Agent Framework
- ពុម្ពហ្គ្រាម MAF ដ៏ប្រសើរ៖ ប្រតិបត្តិការងារ (workflows), មេឌៀរផែរ (middleware), និងអង្គចងចាំ

## គោលបំណងការសិក្សា

បន្ទាប់ពីបញ្ចប់មេរៀននេះ អ្នកនឹងដឹងរបៀប៖

- បង្កើត AI Agents សម្រាប់ផលិតផលដោយប្រើ Microsoft Agent Framework
- អនុវត្តលក្ខណៈសម្បត្តិគោលនៃ Microsoft Agent Framework ទៅកាន់ករណីប្រើប្រាស់ Agentic របស់អ្នក
- ប្រើប្រាស់ពុម្ពហ្គ្រាមជាមុនរួច ដែលរួមមាន ប្រតិបត្តិការងារ មេឌៀរផែ និងការសង្កេតមើល

## ឧទាហរណ៍កូដ 

ឧទាហរណ៍កូដសម្រាប់ [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) អាចរកបាននៅក្នុងឃ្លាំងនេះក្រោមឯកសារ `xx-python-agent-framework` និង `xx-dotnet-agent-framework`។

## ការយល់ដឹងអំពី Microsoft Agent Framework

![Framework Intro](../../../translated_images/km/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) គឺជាស៊ុមប្រព័ន្ធរួមរបស់ Microsoft សម្រាប់បង្កើត AI Agents។ វានាំមកនូវភាពបត់បែនដើម្បីដោះស្រាយករណីប្រើប្រាស់ agentic ផ្សេងៗគ្នា ដែលធ្លាប់ឃើញនៅក្នុងបរិយាកាសផលិតផល និងស្រាវជ្រាវ រួមទាំង៖

- **ការដឹកនាំ Agent តាមលំដាប់** នៅក្នុងសេណារីយ៉ូចង់បានប្រតិបត្តិការជាជំហានទៅជំហាន។
- **ការដឹកនាំជាសម័យដើម** នៅក្នុងសេណារីយ័ដែល agents ត្រូវបញ្ចប់ភារកិច្ចនៅពេលដូចគ្នា។
- **ការដឹកនាំក្រុមជជែក** នៅក្នុងសេណារីយ័ដែល agents អាចសហការជាមួយគ្នាលើភារកិច្ចមួយ។
- **ការបញ្ជូនភារកិច្ច** នៅក្នុងសេណារីយ័ដែល agents ទុកភារកិច្ចផ្ទាល់ទៅម្នាក់ទៀតនៅពេលបញ្ចប់ការងារជាផ្នែកតូចៗ។
- **ការដឹកនាំមេគ្រប់គ្រង** នៅក្នុងសេណារីយ័ដែល agent មេគ្រប់គ្រងបង្កើតនិងកែប្រែបញ្ជីភារកិច្ច និងដោះស្រាយការសម្របសម្រួល subagents ដើម្បីបញ្ចប់ភារកិច្ច។

ដើម្បីផ្តល់ AI Agents នៅក្នុងផលិតផល MAF ក៏មានលក្ខណៈសម្បត្តិសម្រាប់៖

- **ការសង្កេតមើល** តាមរយៈការប្រើប្រាស់ OpenTelemetry ដែលសកម្មភាពរាល់អង្គ_AGENT រួមមានការហៅឧបករណ៍ ដំណើរការដឹកនាំ ការស្រាយតម្រង និងការត្រួតពិនិត្យសមត្ថភាពតាមរយៈ dashboards Microsoft Foundry។
- **សុវត្ថិភាព** ដោយផ្ទុក agents ដោយធម្មជាតិលើ Microsoft Foundry ដែលរួមមានការគ្រប់គ្រងសុវត្ថិភាពដូចជា ការចូលប្រើតាមតួនាទី ការដែលមានការដោះស្រាយទិន្នន័យឯកជន និងការការពារមាតិកាចាប់ផ្តើម។
- **ភាពធន់ទ្រាំ** ដូចជាស្នាក់ខ្សែ និងប្រតិបត្តិការងារអាចឈប់បន្ត ឬរងការជួសជុលពីកំហុស ដែលអាចចាប់ផ្តើមដំណើរការរយៈពេលវែង។
- **ការគ្រប់គ្រង** ដូចជាប្រតិបត្តិការងារមានមនុស្សរួមចំណែក ដែលភារកិច្ចត្រូវបានសម្គាល់ថាត្រូវការការអនុម័តពីមនុស្ស។

Microsoft Agent Framework ក៏ផ្តោតលើការអាចប្រើប្រាស់រួមគ្នាបានរយៈពេលយ៉ាងខ្លាំងដោយ៖

- **មិនពឹងផ្អែកលើពពកណាមួយ** - Agents អាចរត់ក្នុង containers លើទីតាំងក្នុងខាងត្រង់ និងលើពពកផ្សេងៗគ្នា។
- **មិនពឹងផ្អែកលើអ្នកផ្គត់ផ្គង់ណាមួយ** - Agents អាចត្រូវបានបង្កើតតាម SDK ដែលអ្នកចូលចិត្តរួមមាន Azure OpenAI និង OpenAI
- **រួមបញ្ចូលស្តង់ដារបើក** - Agents អាចប្រើប្រព័ន្ធផ្សព្វផ្សាយដូចជា Agent-to-Agent (A2A) និង Model Context Protocol (MCP) ដើម្បីរកឃើញ និងប្រើប្រាស់ agents និងឧបករណ៍ផ្សេងទៀត។
- **Plugins និង Connectors** - អាចភ្ជាប់ទៅកាន់សេវាកម្មទិន្នន័យ និងអង្គចងចាំដូចជា Microsoft Fabric, SharePoint, Pinecone និង Qdrant។

យើងមកមើលរបៀបដែលលក្ខណៈនេះត្រូវបានអនុវត្តទៅកាន់គំនិតសំខាន់ៗខ្លះៗនៃ Microsoft Agent Framework។

## គំនិតសំខាន់ៗនៃ Microsoft Agent Framework

### អេហ្សិន (Agents)

![Agent Framework](../../../translated_images/km/agent-components.410a06daf87b4fef.webp)

**ការបង្កើត Agents**

ការបង្កើត Agent ត្រូវបានធ្វើឡើងដោយកំណត់សេវាដំណើរការព្យាករណ៍ (LLM Provider), ការណែនាំឲ្យអង្គ_AGENT អនុវត្ត និងឈ្មោះ `name` ដែលបានផ្ដល់៖


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ខាងលើកំពុងប្រើ `Azure OpenAI` ប៉ុន្តែ agents អាចត្រូវបានបង្កើតជាមួយសេវាកម្មនានា រួមទាំង `Microsoft Foundry Agent Service`៖

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

ឬ [MiniMax](https://platform.minimaxi.com/) ដែលផ្ដល់ API ដែលគាំទ្រ OpenAI ជាមួយបង្អួច context ធំ (រហូតដល់ 204K tokens)៖

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ឬ agents ពីចម្ងាយដោយប្រើ compare with A2A protocol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ការរត់ Agents**

ការរត់ Agents គឺត្រូវបានប្រើ `.run` ឬ `.run_stream` សម្រាប់ចម្លើយដែលមិនប្រើបែបបទបញ្ច្រាស់ និងប្រើបែបបទបញ្ច្រាស់។

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ការរត់មួយនៃអង្គ_AGENT អាចមានជម្រើសសម្រាប់ប្តូរតម្លៃប៉ារ៉ាម៉ែត្រ ដូចជា `max_tokens` ដែលអង្គ_AGENT ប្រើប្រាស់, `tools` ដែលអង្គ_AGENT អាចហៅបាន និង ទូទៅ `model` ដែលប្រើសម្រាប់អង្គ_AGENT។

វាមានប្រយោជន៍នៅក្នុងករណីដែលត្រូវការម៉ូដែល ឬឧបករណ៍ជាក់លាក់សម្រាប់បញ្ចប់ភារកិច្ចរបស់អ្នកប្រើប្រាស់។

**ឧបករណ៍ (Tools)**

ឧបករណ៍អាចកំណត់ទាំងនៅពេលកំណត់អង្គ_AGENT៖

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ពេលបង្កើត ChatAgent ដោយផ្ទាល់

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ហើយនៅពេលកំពុងរត់អង្គ_AGENT ផងដែរ៖

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ឧបករណ៍ផ្តល់សម្រាប់ការប្រតិបត្ដិការនេះតែប៉ុណ្ណោះ )
```

**ស្នាដៃ Agent (Agent Threads)**

ស្នាដៃ Agent ត្រូវបានប្រើប្រាស់ដើម្បីគ្រប់គ្រងការសន្ទនាផ្តាច់មុខជាច្រើនជំហាន។ ស្នាដៃអាចត្រូវបានបង្កើតដោយ៖

- ការប្រើ `get_new_thread()` ដែលអនុញ្ញាតឲ្យស្នាដៃត្រូវបានរក្សាទុកឲ្យមានរយៈពេលវែង
- បង្កើតស្នាដៃដោយស្វ័យប្រវត្តិ នៅពេលរត់អង្គ_AGENT ហើយស្នាដៃនោះមានតែរយៈពេលរត់បច្ចុប្បន្ន។

ដើម្បីបង្កើតស្នាដៃ កូដមានរូបរាងដូចខាងក្រោម៖

```python
# បង្កើតខ្សែថ្មីមួយ។
thread = agent.get_new_thread() # ប្រតិបត្តិភាគីជាមួយខ្សែ។
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

អ្នកអាច serialize ស្នាដៃដើម្បីរក្សាទុកសម្រាប់ការប្រើប្រាស់នៅពេលក្រោយ៖

```python
# បង្កើតធ្រេដថ្មីមួយ។
thread = agent.get_new_thread() 

# ប្រតិបត្តិភ្នាក់ងារជាមួយធ្រេដ។

response = await agent.run("Hello, how are you?", thread=thread) 

# ស៊ីរីយ៉ាលផ្ទុកធ្រេដសម្រាប់ការផ្ទុក។

serialized_thread = await thread.serialize() 

# លុបចេញស្ថានភាពធ្រេដបន្ទាប់ពីដាក់ឡើងវិញពីការផ្ទុក។

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**មេឌៀរផែរ Agent (Agent Middleware)**

Agents អនុវត្តន៍ជាមួយឧបករណ៍ និង LLMs ដើម្បីបញ្ចប់ភារកិច្ចរបស់អ្នកប្រើប្រាស់។ នៅក្នុងសេណារីយ័ច某ំជាក់ ចង់អនុវត្ត ឬតាមដាននៅចន្លោះពួកវា។ Agent middleware អនុញ្ញាតឲ្យធ្វើបានដោយ៖

*Middleware នៃមុខងារ*

Middleware នេះអនុញ្ញាតឲ្យអនុវត្តសកម្មភាពចន្លោះអង្គ_AGENT និងមុខងារ/ឧបករណ៍ដែលវានឹងហៅ។ ឧទាហរណ៍នៃការប្រើប្រាស់ middleware នេះគឺនៅពេលអ្នកចង់កត់ត្រាការហៅមុខងារ។

នៅក្នុងកូដខាងក្រោម `next` កំណត់ថា middleware បន្ទាប់ ឬមុខងារពិតប្រាកដត្រូវបានហៅ។

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ការរៀបចំមុន: កំណត់ហេតុនៅមុនការអនុវត្តមុខងារ
    print(f"[Function] Calling {context.function.name}")

    # បន្តទៅមុខងារមជ្ឈដ្ឋានបន្ទាប់ឬអនុវត្តមុខងារ
    await next(context)

    # ការបន្ទាប់បន្សំ: កំណត់ហេតុនៅបន្ទាប់ការអនុវត្តមុខងារ
    print(f"[Function] {context.function.name} completed")
```

*Middleware ជជែក*

Middleware នេះអនុញ្ញាតអោយអនុវត្ត ឬកត់ត្រាសកម្មភាពចន្លោះអង្គ_AGENT និងសំណើររបស់ LLM។

វារួមមានព័ត៌មានសំខាន់ៗ ដូចជា `messages` ដែលត្រូវបានផ្ញើទៅសេវា AI។

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ការពិសោធន៍មុន: កត់ត្រាកំណត់ហេតុមុនការហៅ AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # បន្តទៅមេឌៀវែរ ឬសេវា AI បន្ទាប់
    await next(context)

    # ការពិសោធន៍បន្ទាប់: កត់ត្រាកំណត់ហេតុបន្ទាប់ពីការឆ្លើយតប AI
    print("[Chat] AI response received")

```

**អង្គចងចាំ Agent (Agent Memory)**

ដូចដែលបានពិភាក្សានៅក្នុងមេរៀន `Agentic Memory`, អង្គចងចាំគឺជាធាតុសំខាន់សម្រាប់អនុញ្ញាតឲ្យអង្គ_AGENT អនុវត្តនៅលើបរិបទផ្សេងៗ។ MAF ផ្ដល់ជូនអង្គចងចាំ ប្រភេទផ្សេងៗគ្នា៖

*ការផ្ទុកមេម៉ូរីក្នុងមេម៉ូរី*

នេះគឺជាអង្គចងចាំដែលផ្ទុកនៅក្នុងស្នាដៃរយៈពេលដំណើរការអនុវត្តកម្មវិធី។

```python
# បង្កើតខ្សែវិភាគថ្មី។
thread = agent.get_new_thread() # បញ្ជូនភ្នាក់ងារជាមួយខ្សែវិភាគ។
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*សារPersistent*

អង្គចងចាំនេះត្រូវបានប្រើពេលរក្សាប្រវត្តិសន្ទនា ឆ្លងកាត់សំនុំនៃសម័យផ្សេងៗគ្នា។ វាត្រូវបានកំណត់ដោយប្រើ `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# បង្កើតឃ្លាំងសារ​ផ្ទាល់ខ្លួន
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*អង្គចងចាំ Dynamic*

អង្គចងចាំនេះត្រូវបានបន្ថែមចូលទៅក្នុងបរិបទ មុនពេលអង្គ_AGENT រត់។ អង្គចងចាំទាំងនេះអាចរក្សាទុកនៅក្នុងសេវាកម្មខាងក្រៅ ដូចជា mem0:

```python
from agent_framework.mem0 import Mem0Provider

# កំពុងប្រើ Mem0 សម្រាប់សមត្ថភាពអង្គចងចាំកម្រិតខ្ពស់
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

**ការសង្កេតមើល Agent (Agent Observability)**

ការសង្កេតមើលគឺសំខាន់សម្រាប់ការកសាងប្រព័ន្ធ agentic ដែលអាចទុកចិត្ត និងថែរក្សាបាន។ MAF បញ្ចូលជាមួយ OpenTelemetry ដើម្បីផ្ដល់ការតាមដាន និងម៉ែត្រសម្រាប់ការសង្កេតមើលល្អប្រសើរ។

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

### ប្រតិបត្តិការងារ (Workflows)

MAF ផ្ដល់ប្រតិបត្តិការងារដែលជាជំហានដែលកំណត់រួចដើម្បីបញ្ចប់ភារកិច្ច និងរួមបញ្ចូល AI agents ជាគ្រឿងផ្សំនៅក្នុងជំហានទាំងនោះ។

ប្រតិបត្តិការងារត្រូវបានបង្កើតចេញពីគ្រឿងផ្សំនានា ដើម្បីអនុញ្ញាតលំនាំដំណើរការល្អប្រសើរ។ ប្រតិបត្តិការងារក៏អាចអនុញ្ញាតសម្រាប់ **ការដឹកនាំ multi-agent** និង **ការត្រួតពិនិត្យចំណុចផ្តាច់** ដើម្បីរក្សាស្ថានភាពប្រតិបត្តិការងារ។

គ្រឿងផ្សំសំខាន់នៃប្រតិបត្តិការងារមាន៖

**អ្នកអនុវត្ត (Executors)**

អ្នកអនុវត្តទទួលសារ input, ប្រតិបត្តិការងារដែលបានផ្ដល់, ហើយបញ្ចេញសារ output។ វាចល័តប្រតិបត្តិការងារទៅមុខ ទៅរកការសម្រេចភារកិច្ចធំ។ អ្នកអនុវត្តអាចជាអង្គ_AGENT AI ឬលLogic ផ្ទាល់ខ្លួន។

**ស្រទាប់ (Edges)**

ស្រទាប់ត្រូវបានប្រើ ដើម្បីកំណត់លំនាំសារនៅក្នុងប្រតិបត្តិការងារ។ វាអាចជា៖

*ស្រទាប់ផ្ទាល់ (Direct Edges)* - ការភ្ជាប់មួយទៅមួយយ៉ាងសាមញ្ញរវាងអ្នកអនុវត្ត៖

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*ស្រទាប់មានលក្ខខណ្ឌ (Conditional Edges)* - បើកប្រើបន្ទាប់ពីលក្ខខណ្ឌមួយត្រូវបានបំពេញ។ ឧទាហរណ៍ បើបន្ទប់សណ្ឋាគារមិនមានអាសយដ្ឋាន អ្នកអនុវត្តអាចស្នើរសុំជម្រើសផ្សេងទៀត។

*ស្រទាប់ប្ដូរករណី (Switch-case Edges)* - នាំសារទៅអ្នកអនុវត្ដផ្សេងៗគ្នាតាមលក្ខខណ្ឌកំណត់។ ឧទាហរណ៍ ប្រសិនបើអតិថិជនធ្វើដំណើរមានអាទិភាពចូល ប្រតិបត្តិការរបស់ពួកគេចាំបាច់ត្រូវរៀបចំតាមប្រតិបត្តិការងារផ្សេងទៀត។

*ស្រទាប់ផ្សាយចេញ (Fan-out Edges)* - ផ្ញើសារមួយទៅគោលដៅជាច្រើន។

*ស្រទាប់ផ្សាយចូល (Fan-in Edges)* - ប្រមូលសារជាច្រើនពីអ្នកអនុវត្តន៍ផ្សេងៗ ហើយផ្ញើទៅគោលដៅមួយ។

**ព្រឹត្តិការណ៍ (Events)**

ដើម្បីផ្ដល់ការសង្កេតមើលប្រសើរចំពោះប្រតិបត្តិការងារ MAF ផ្ដល់ព្រឹត្តិការណ៍ដែលបានបង្កើតរួចសម្រាប់ការអនុវត្តរួមមានៈ

- `WorkflowStartedEvent`  - ប្រតិបត្តិការងារចាប់ផ្តើមដំណើរការ
- `WorkflowOutputEvent` - ប្រតិបត្តិការងារផលិតលទ្ធផលមួយ
- `WorkflowErrorEvent` - ប្រតិបត្តិការងារសំរាប់មានកំហុស
- `ExecutorInvokeEvent`  - អ្នកអនុវត្តចាប់ផ្តើមដំណើរការ
- `ExecutorCompleteEvent`  - អ្នកអនុវត្តបញ្ចប់ដំណើរការ
- `RequestInfoEvent` - មានការផ្តល់សំណើ

## ពុម្ពបន្ទុះ MAF ។ ពុម្ពដំណើរការជំនាញ

ផ្នែកខាងលើគ្របដណ្តប់គំនិតសំខាន់ៗនៃ Microsoft Agent Framework។ ខណঃអ្នកកំពុងបង្កើត agents ស្មុគស្មាញជាងមុន នេះគឺជាពុម្ពបន្ទុះជំនាញមួយចំនួនដែលគួរតែពិចារណា៖

- **សមាសភាព Middleware**៖ បង្កើតខ្សែ middleware ជាច្រើន (កត់ត្រា, សិទ្ធិក្នុងការចូល, កំណត់អត្រា) ដោយប្រើ function និង chat middleware សម្រាប់ការគ្រប់គ្រងលំអិតលើអាកប្បកិរិយា agent។
- **Checkpointing ប្រតិបត្តិការងារ**៖ ប្រើព្រឹត្តិការណ៍ប្រតិបត្តិការងារ និងការតម្រៀបជាសេរី ដើម្បីរក្សាទុក និងបន្តដំណើរការលើ Agent រយៈពេលវែង។
- **ជម្រើសឧបករណ៍អាចបត់បែនបាន**៖ ផ្នែកបញ្ចូល RAG លើការពិពណ៌នាឧបករណ៍ជាមួយការចុះបញ្ជីឧបករណ៍ MAF ដើម្បីបង្ហាញឧបករណ៍ដែលពាក់ព័ន្ធតែមួយទៅម្នាក់។
- **ការបញ្ជូន Multi-Agent**៖ ប្រើ edges នៃប្រតិបត្តិការងារ និងការបញ្ជូនតាមលក្ខខណ្ឌ ដើម្បីដឹកនាំការបញ្ជូនរវាង agents ជំនាញផ្សេងៗ។

## ផ្ទុកអង្គ_AGENT LangChain / LangGraph លើ Microsoft Foundry

Microsoft Agent Framework គឺ **អាចប្រើរួមបានជាមួយ framework ផ្សេងៗ** — អ្នកមិនត្រូវដាក់កម្រិត agents ដែលបានសរសេរជាមួយ MAF តែប៉ុណ្ណោះទេ។ ប្រសិនបើអ្នកមាន agent ដែលបានបង្កើតជាមួយ **LangChain** ឬ **LangGraph** អ្នកអាចរត់វាជា **agent ផ្ទុកលើ Microsoft Foundry** ដើម្បីឲ្យ Foundry គ្រប់គ្រង runtime, សម័យ, ការកំណត់ទំហំ, អត្តសញ្ញាណ និងចំណុចផ្ដល់សេវា protocol សម្រាប់អ្នក ខណៈដែល logic អង្គ_AGENT របស់អ្នកនៅក្នុង LangGraph។

នេះធ្វើទៅដោយប្រើកញ្ចប់ `langchain_azure_ai.agents.hosting` ដែលបង្ហាញ graph LangGraph compiled តាម protocol ដដែលដែលបានប្រើដោយ agent ផ្ទុកលើ Foundry។

**1. ដំឡើង hosting extra ៖**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Extra `hosting` នេះដំឡើងបណ្ណាល័យ protocol Foundry៖ `azure-ai-agentserver-responses` (ចំណុចបញ្ចប់ /responses ផ្គូផ្គង OpenAI) និង `azure-ai-agentserver-invocations` (ចំណុចបញ្ចប់ /invocations ទូទៅ)។

**2. ជ្រើសរើស protocol hosting ៖**

| Protocol | ថ្នាក់ host | ចំណុចបញ្ចប់ | ប្រើប្រាស់ពេលណា |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | អ្នកចង់បាន chat, streaming, ប្រវត្តិចម្លើយ និងការច្រកមជួបទំនងដែលផ្គូផ្គង OpenAI — ជាជម្រើសកំណត់សម្រាប់ agent ក្នុងការសន្ទនា។ |
| **Invocations** | `InvocationsHostServer` | `/invocations` | អ្នកត្រូវការរូបរាង JSON ផ្ទាល់ខ្លួន, ចំណុចបញ្ចប់ kiểu webhook, ឬដំណើរការមិនមែនសន្ទនា។ |

ពីព្រោះ **Responses API គឺជាប្រភព API សំខាន់សម្រាប់ការអភិវឌ្ឍ agent នៅ Foundry**, ចាប់ផ្តើមជាមួយ `ResponsesHostServer` សម្រាប់ភាគច្រើនរបស់ agents។

**3. កំណត់បរិវេណផ្ទះបាយ** (`az login` ជាមុន ដើម្បីឲ្យ `DefaultAzureCredential` អាចផ្ទៀងផ្ទាត់):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

ពេល agent រត់ជាបន្ទាប់ជា agent ផ្ទុកលើ Foundry វាត្រូវបានផ្លាស់ប្តូរដោយស្វ័យប្រវត្តិសម្រាប់ `FOUNDRY_PROJECT_ENDPOINT`។

**4. បង្ហាញ agent LangGraph តាម protocol Responses៖**

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

    # ChatOpenAI នៅទីនេះផ្តោតលើចុងបញ្ចប់ (Responses) ដែលគាំទ្រដោយ OpenAI របស់គម្រោង Foundry។
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

រត់វាក្នុងកុំព្យូទ័រអ្នកដោយ `python main.py` បន្ទាប់មកផ្ញើសំណើ Responses ទៅកាន់ `http://localhost:8088/responses`។

**អាកប្បកិរិយាសំខាន់ៗ៖**

- **ការសន្ទនា**៖ អតិថិជនបន្តការសន្ទនាតាមរយៈការផ្ញើ `previous_response_id` ឬ ID `conversation`។ ប្រសិនបើ graph របស់អ្នកបានកំណត់ជា LangGraph checkpointer, Foundry ចងកាន់ស្ថានភាពសន្ទនាទៅ checkpoint (ប្រើ durable checkpointer ក្នុងផលិតផល; `MemorySaver` ល្អសម្រាប់ការតេស្តក្នុងមូលដ្ឋាន)។
- **មនុស្សនៅក្នុងដំណើរការ**៖ ប្រសិនបើ graph របស់អ្នកប្រើ LangGraph `interrupt()`, `ResponsesHostServer` នាំមុខសញ្ញាបង្ហាញការជួបប្រទៈ interrupt ដែលរង់ចាំជារបស់ Responses `function_call` / `mcp_approval_request`, ហើយអតិថិជនបន្តជាមួយ `function_call_output` / `mcp_approval_response` ដែលផ្គូផ្គង។
- **ដាក់បញ្ចូល Foundry**៖ ប្រើ Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ក្នុងកុំព្យូទ័រ, តម្រូវជាមួយ Docker), បន្ទាប់មក `azd provision` និង `azd deploy`។ ការដាក់បញ្ចូល agent ផ្ទុកលើតម្រូវតួនាទី **Foundry Project Manager**។

ជាឯកសារអាចរត់បាននៃឧទាហរណ៍នេះមាននៅក្នុង [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)។ សម្រាប់ការណែនាំពេញលេញ (protocol Invocations, គំរូសំណើផ្ទាល់ខ្លួន និងការដោះស្រាយបញ្ហា) សូមមើល [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)។

## ឧទាហរណ៍កូដ 

ឧទាហរណ៍កូដសម្រាប់ Microsoft Agent Framework អាចរកបានក្នុងឃ្លាំងនេះក្រោមឯកសារ `xx-python-agent-framework` និង `xx-dotnet-agent-framework`។

## មានសំណួរបន្ថែមអំពី Microsoft Agent Framework ទេ?

ចូលរួមនៅ [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ដើម្បីជួបសិស្សផ្សេងទៀត ចូលរួមម៉ោងការិយាល័យ ហើយទទួលបានការឆ្លើយសំណួរអំពី AI Agents របស់អ្នក។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->