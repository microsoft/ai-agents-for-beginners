# ការស្វែងយល់អំពី Microsoft Agent Framework

![Agent Framework](../../../translated_images/km/lesson-14-thumbnail.90df0065b9d234ee.webp)

### សេចក្ដីគណនាបឋម

មេរៀននេះនឹងគ្របដណ្តប់៖

- ការយល់ដឹងអំពី Microsoft Agent Framework៖ លក្ខណៈសំខាន់ និងតម្លៃ  
- ការស្វែងយល់គំនិតសំខាន់ៗនៃ Microsoft Agent Framework
- លំនាំ MAF ដែលមានភាពចំរូងចំរាសៈ៖ ការប្រតិបត្តិការទំនើប, មេឌៀវ៉ែរ, និងអង្គចងចាំ

## គោលបំណងការសិក្សា

បន្ទាប់ពីបញ្ចប់មេរៀននេះ អ្នកនឹងដឹងពីរបៀបធ្វើ៖

- បង្កើតភ្នាក់ងារបញ្ញាសិប្បនិម្មិតដែលត្រៀមប្រើប្រាស់ផលិតកម្មដោយប្រើ Microsoft Agent Framework
- អនុវត្តលក្ខណៈសំខាន់ៗនៃ Microsoft Agent Framework ទៅកាន់ករណីប្រើប្រាស់ Agentic របស់អ្នក
- ប្រើលំនាំពិសេសរួមមានការប្រតិបត្តិការទំនើប, មេឌៀវ៉ែរ និងការគ្រប់គ្រងមើលទស្សនា

## គំរូកូដ

គំរូកូដសម្រាប់ [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) អាចស្វែងរកបាននៅក្នុងឃ្លាំងនេះនៅក្រោមឯកសារ `xx-python-agent-framework` និង `xx-dotnet-agent-framework`។

## ការយល់ដឹងអំពី Microsoft Agent Framework

![Framework Intro](../../../translated_images/km/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) គឺជា​ក្របខ័ណ្ឌឯកភាពរបស់ Microsoft សម្រាប់ការបង្កើតភ្នាក់ងារ AI។ វាផ្ដល់នូវភាពបត់បែន ដើម្បីដោះស្រាយករណីប្រើប្រាស់ Agentic ច្រើនទូលំទូលាយដែលឃើញទាំងក្នុងបរិស្ថានផលិតកម្ម និងស្រាវជ្រាវ ដូចជា៖

- **ការរៀបចំភ្នាក់ងារតាមលំដាប់** ក្នុងករណីដែលត្រូវការជំហានមួយទៅមួយ។
- **ការរៀបចំជាមួយគ្នា** នៅករណីដែលភ្នាក់ងារត្រូវបញ្ចប់កិច្ចការជាពេលតែមួយ។
- **ការរៀបចំការជជែកជាក្រុម** នៅករណីដែលភ្នាក់ងារអាចសហការជាមួយគ្នាលើកិច្ចការតែមួយ។
- **ការរៀបចំការ​ផ្ទេរ** នៅករណីដែលភ្នាក់ងារផ្ទេរកិច្ចការជាភ្នាក់ងារផ្សេងទៀតពេលកិច្ចការតូចត្រូវបានបញ្ចប់។
- **ការរៀបចំដោយម៉ាញេទិច** នៅករណីដែលភ្នាក់ងារតំបន់គ្រប់គ្រងបង្កើត និងកែប្រែបញ្ជីកិច្ចការ និងគ្រប់គ្រងសមាសភាគដើម្បីបញ្ចប់កិច្ចការ។

ដើម្បីផ្តល់ភ្នាក់ងារ AI ក្នុងផលិតកម្ម MAF ក៏រួមបញ្ចូលលក្ខណៈសំខាន់សម្រាប់៖

- **ការមើលទស្សនា** តាមប្រើប្រាស់ OpenTelemetry ដែលសកម្មភាពនីមួយៗរបស់ភ្នាក់ងារ AI រួមមានការហៅឧបករណ៍, ជំហានរៀបចំ, តម្រង់ហេតុ និងការត្រួតពិនិត្យសមត្ថភាពតាមផ្ទាំងព័ត៌មាន Microsoft Foundry។
- **សុវត្ថិភាព** ដោយបម្រើភ្នាក់ងារជាដើមនៅលើ Microsoft Foundry ដែលរួមបញ្ចូលការត្រួតពិនិត្យសុវត្ថិភាពដូចជាការចូលរួមមានតួនាទី, ការដោះស្រាយព័ត៌មានផ្ទៃក្នុង និងសុវត្ថិភាពមាតិកាក្នុងប្រព័ន្ធ។
- **ការអាចធន់បាន** ពីព្រោះខ្សែអាជីពភ្នាក់ងារ និងក្រុមហ៊ុនអាចបញ្ឈប់បន្ត និងស្ដារឡើងវិញពីកំហុសដែលអនុញ្ញាតឲ្យដំណើរការលើរយៈពេលវែង។
- **ការគ្រប់គ្រង** ពីព្រោះរបៀបការងារជាមួយមនុស្សក្នុងបន្ទាត់ត្រូវបានគាំទ្រ ដែលកិច្ចការត្រូវបានសម្គាល់ថាត្រូវការការយល់ព្រមពីមនុស្ស។

Microsoft Agent Framework ក៏ផ្តោតលើភាពអាចប្រើរួមគ្នាតាមរយៈ៖

- **មិនពឹងផ្អែកលើប្លុកឦ្យាស្មៅ (Cloud-agnostic)** - ភ្នាក់ងារអាចរត់ក្នុង containers, នៅលើបរិវេណរបស់ខ្លួន និងបណ្តោយតាមប្លុកឦ្យាស្មៅច្រើន។
- **មិនពឹងផ្អែកលើអ្នកផ្តល់ (Provider-agnostic)** - ភ្នាក់ងារអាចបង្កើតតាម SDK ដែលអ្នកចូលចិត្ត រួមមាន Azure OpenAI និង OpenAI
- **បញ្ចូលស្តង់ដារបើក (Open Standards)** - ភ្នាក់ងារអាចប្រើប្រព័ន្ធដូចជា Agent-to-Agent(A2A) និង Model Context Protocol (MCP) ដើម្បីរកឃើញ និងប្រើភ្នាក់ងារ និងឧបករណ៍ផ្សេងៗ។
- **ផ្លក់អ៊ីន និង ខ្សែភ្ជាប់ (Plugins and Connectors)** - ការតភ្ជាប់អាចធ្វើទៅកាន់សេវាកម្មទិន្នន័យ និងអង្គចងចាំ ដូច Microsoft Fabric, SharePoint, Pinecone និង Qdrant។

ចង់មើលថាតើលក្ខណៈពិសេសទាំងនេះត្រូវបានអនុវត្តទៅលើគំនិតសំខាន់ៗនៃ Microsoft Agent Framework ដូចម្តេច។

## គំនិតសំខាន់ៗនៃ Microsoft Agent Framework

### ភ្នាក់ងារ (Agents)

![Agent Framework](../../../translated_images/km/agent-components.410a06daf87b4fef.webp)

**ការបង្កើតភ្នាក់ងារ**

ការបង្កើតភ្នាក់ងារត្រូវធ្វើដោយកំណត់សេវាកម្មស្រាវជ្រាវ (LLM Provider), ការណែនាំសម្រាប់ភ្នាក់ងារ AI អោយអនុវត្ត និង `name` ដែលបានផ្ដល់:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

ខាងលើប្រើប្រាស់ `Azure OpenAI` ប៉ុន្តែភ្នាក់ងារអាចត្រូវបានបង្កើតដោយប្រើសេវាកម្មជាច្រើនរួមមាន `Microsoft Foundry Agent Service`:

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

ឬ [MiniMax](https://platform.minimaxi.com/), ដែលផ្ដល់ API ដែលគាំទ្រ OpenAI ដោយមានបង្អួចភាពយន្ដធំ (ដល់ 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ឬភ្នាក់ងារពីចម្ងាយប្រើពិធីសាស្ត្រ A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ការប្រតិបត្ដិភ្នាក់ងារ**

ភ្នាក់ងារត្រូវបានរត់ដោយប្រើវិធី `.run` ឬ `.run_stream` សម្រាប់ចម្លើយមិនស្ទ្រីម ឬស្ទ្រីម។

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ការរត់ភ្នាក់ងារនីមួយៗអាចមានជម្រើសក្នុងការប្ដូរប៉ារ៉ាម៉ែត្រ ដូចជា `max_tokens` ដែលភ្នាក់ងារប្រើ, `tools` ដែលភ្នាក់ងារអាចហៅ, និងម៉ូឌែលផ្ទាល់ដែលត្រូវបានប្រើសម្រាប់ភ្នាក់ងារ។

វាមានប្រយោជន៍សម្រាប់ករណីដែលត្រូវការម៉ូឌែល ឬឧបករណ៍ជាក់លាក់សម្រាប់បញ្ចប់កិច្ចការរបស់អ្នកប្រើ។

**ឧបករណ៍ (Tools)**

ឧបករណ៍អាចត្រូវបានកំណត់ពេលកំណត់ភ្នាក់ងារ:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# នៅពេលបង្កើត ChatAgent របស់ខ្លួនផ្ទាល់

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ហើយក៏ពេលរត់ភ្នាក់ងារ:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ឧបករណ៍ផ្តល់ឲ្យសម្រាប់ការរត់នេះតែប៉ុណ្ណោះ )
```

**ខ្សែអាជីពភ្នាក់ងារ (Agent Threads)**

ខ្សែអាជីពភ្នាក់ងារត្រូវបានប្រើដើម្បីដោះស្រាយការជជែកពហុជំហាន។ ខ្សែអាជីពអាចត្រូវបានបង្កើតដោយ:

- ប្រើ `get_new_thread()` ដែលអនុញ្ញាតឲ្យរក្សាទុកខ្សែអាជីពជារយៈពេលវែង
- បង្កើតខ្សែអាជីពដោយស្វ័យប្រវត្តិពេលរត់ភ្នាក់ងារ ហើយខ្សែអាជីពនោះមានអាយុកាលគ្រាន់តែពេលរត់បច្ចុប្បន្នប៉ុណ្ណោះ។

ដើម្បីបង្កើតខ្សែអាជីព កូដមានរូបមន្តដូចខាងក្រោម៖

```python
# បង្កើតផ្លូវថ្មីមួយ។
thread = agent.get_new_thread() # ប្រតិបត្តិភ្នាក់ងារជាមួយផ្លូវនោះ។
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

អ្នកអាច serialize ខ្សែអាជីពដើម្បីរក្សាទុកសម្រាប់ការប្រើប្រាស់ក្រោយ៖

```python
# បង្កើតខ្សែថ្មី។
thread = agent.get_new_thread() 

# ដំណើរការអ្នកភ្នាក់ងារជាមួយខ្សែ។

response = await agent.run("Hello, how are you?", thread=thread) 

# ស៊េរីឡាយខ្សែសម្រាប់ការផ្ទុក។

serialized_thread = await thread.serialize() 

# បញ្ច្រាសស្ថានភាពខ្សែបន្ទាប់ពីផ្ទុកពីការផ្ទុកឡើងវិញ។

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**មេឌៀវ៉ែរ ភ្នាក់ងារ (Agent Middleware)**

ភ្នាក់ងារប៉ះពាល់ជាមួយឧបករណ៍ និង LLM ដើម្បីបញ្ចប់កិច្ចការអ្នកប្រើ។ នៅក្នុងករណីជាក់លាក់ មនុស្សចង់អនុវត្ត ឬតាមដានជារវាងការប៉ះពាល់ទាំងនេះ។ មេឌៀវ៉ែរភ្នាក់ងារអនុញ្ញាតឲ្យយើងធ្វើការនេះតាមរយៈ៖

*មេឌៀវ៉ែរ មុខងារ (Function Middleware)*

មេឌៀវ៉ែរ​នេះអនុញ្ញាតឲ្យយើងអនុវត្តសកម្មភាពរវាងភ្នាក់ងារ និងមុខងារ/ឧបករណ៍ដែលវានឹងហៅ។ ឧទាហរណ៍កាលណាអ្នកចង់ធ្វើការចុះបញ្ជីលើការហៅមុខងារ។

នៅក្នុងកូដខាងក្រោម `next` កំណត់ថាតើមេឌៀវ៉ែរ​បន្ទាប់ ឬមុខងារពិតប្រាកដគួរត្រូវហៅ។

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # ការប្រព្រឹត្តិមុន: កំណត់ប្រវត្តិមុនការអនុវត្តមុខងារ
    print(f"[Function] Calling {context.function.name}")

    # បន្តទៅមុខវេរ្ម័ទ័រឬការអនុវត្តមុខងារបន្ទាប់
    await next(context)

    # ការប្រព្រឹត្តិបន្ទាប់: កំណត់ប្រវត្តិបន្ទាប់ការអនុវត្តមុខងារ
    print(f"[Function] {context.function.name} completed")
```

*មេឌៀវ៉ែរ ជជែក (Chat Middleware)*

មេឌៀវ៉ែរ​នេះអនុញ្ញាតឲ្យយើងអនុវត្ត ឬចុះបញ្ជីសកម្មភាពរវាងភ្នាក់ងារនិងសំណើរវាង LLM។

វាមានព័ត៌មានសំខាន់ៗដូចជា `messages` ដែលត្រូវបានផ្ញើទៅសេវា AI។

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # ការព្រមានមុនដំណើរការ: កំណត់ឡើងវិញមុនការហៅ AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # បន្តទៅកាន់មធ្យមសេវាកម្មបន្ទាប់ ឬសេវា AI
    await next(context)

    # ការថតបន្ទាប់: កំណត់ឡើងវិញបន្ទាប់ពីការឆ្លើយតប AI
    print("[Chat] AI response received")

```

**អង្គចងចាំភ្នាក់ងារ (Agent Memory)**

ដូចបានគ្របដណ្តប់ក្នុងមេរៀន `Agentic Memory`, អង្គចងចាំគឺជាធាតុសំខាន់សម្រាប់អនុញ្ញាតឲ្យភ្នាក់ងារប្រតិបត្ដិលើបរិបទនានា។ MAF ផ្ដល់អង្គចងចាំជាប្រភេទផ្សេងៗគ្នា៖

*ទិន្នន័យក្នុងអង្គចងចាំក្នុងកម្រិតមួយ (In-Memory Storage)*

នេះគឺជាអង្គចងចាំដែលរក្សាទុកនៅខ្សែអាជីពក្នុងរយៈពេលដំណើរការកម្មវិធី។

```python
# បង្កើតទីប្រឹក្សាថ្មី។
thread = agent.get_new_thread() # ប្រតិបត្តិប្រតិបត្តិការជាមួយទីប្រឹក្សា។
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*សារទំនើប (Persistent Messages)*

អង្គចងចាំនេះត្រូវបានប្រើពេលរក្សាទុកប្រវត្តិការសន្ទនា ទាក់ទងនឹងសម័យថែមទៀត។ វាត្រូវបានកំណត់ដោយប្រើ `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# បង្កើតឃ្លាំងសារបរិដ្ឋានផ្ទាល់ខ្លួន
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*អង្គចងចាំឌីណាមិក (Dynamic Memory)*

អង្គចងចាំនេះត្រូវបានបន្ថែមទៅcontext មុនពេលរត់ភ្នាក់ងារ។ អង្គចងចាំខ្លះ អាចរក្សាទុកនៅសេវាកម្មខាងក្រៅដូចជា mem0:

```python
from agent_framework.mem0 import Mem0Provider

# ការប្រើប្រាស់ Mem0 សម្រាប់សមត្ថភាពមេម៉ូរីចុងក្រោយ
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

**ការមើលទស្សនាភ្នាក់ងារ (Agent Observability)**

ការមើលទស្សនា​គឺសំខាន់សម្រាប់ការបង្កើតប្រព័ន្ធ agentic ដែលទុកចិត្តបាន និងងាយស្រួលថែទាំ។ MAF បញ្ចូលជាមួយ OpenTelemetry ដើម្បីផ្តល់ការតាមដាននិងម៉ែត្រសម្រាប់ការមើលទស្សនាដែលល្អជាង។

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ធ្វើអ្វីមុខ
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### ជំហានប្រតិបត្តិការ (Workflows)

MAF ផ្ដល់ជំហានប្រតិបត្តិការ ដែលជាជំហានបានកំណត់ជាមុនសម្រាប់បញ្ចប់កិច្ចការ និងរួមបញ្ចូលភ្នាក់ងារ AI ជាផ្នែករបស់ជំហានទាំងនោះ។

ជំហានប្រតិបត្តិការត្រូវបានបង្កើតពីសមាសភាគផ្សេងៗ ដែលអនុញ្ញាតឲ្យមានការត្រួតពិនិត្យល្អប្រសើរ។ ជំហានប្រតិបត្តិការនៅក្នុង MAF ក៏អាចគាំទ្រការរៀបចំភ្នាក់ងារច្រើន និងការសន្សំព្រឹត្តិការណ៍ដើម្បីរក្សាស្ថានភាពជំហាន។

សមាសភាគសំខាន់នៃជំហានប្រតិបត្តិការ​មាន៖

**អ្នកអនុវត្ដ (Executors)**

អ្នកអនុវត្ដទទួលសារបញ្ចូល, អនុវត្តកិច្ចការដែលបានផ្ដល់ចាត់តាំង ហើយបញ្ចេញផ្សាយសារចេញ។ នេះជារបៀបធ្វើឲ្យជំហានប្រតិបត្តិការបន្តទៅមុខដើម្បីបញ្ចប់កិច្ចការធំ។ អ្នកអនុវត្ដអាចជាភ្នាក់ងារ AI ឬ ឡូជិចផ្ទាល់ខ្លួន។

**ខ្សែកំណត់ (Edges)**

ខ្សែកំណត់ត្រូវបានប្រើក្នុងការកំណត់ប្រតិបត្តិការសារនៅក្នុងជំហានប្រតិបត្តិការ។ វាអាចជាប្រភេទ៖

*ខ្សែកំណត់ផ្ទាល់ (Direct Edges)* - ការតភ្ជាប់មួយទៅមួយរវាងអ្នកអនុវត្ដ៖

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*ខ្សែកំណត់បើកលក្ខខណ្ឌ (Conditional Edges)* - ត្រូវបានបើកប្រើបន្ទាប់ពីលក្ខខណ្ឌជាក់លាក់ត្រូវបានបំពេញ។ ឧទាហរណ៍ ពេលបន្ទប់សណ្ឋាគារមិនអាចរកបាន អ្នកអនុវត្ដអាចផ្តល់យោបល់ជម្រុងផ្សេងៗ។

*ខ្សែកំណត់ប្តូរករណី (Switch-case Edges)* - បញ្ជូនសារទៅអ្នកអនុវត្ដផ្សេងៗទៅតាមលក្ខខណ្ឌបានកំណត់។ ឧទាហរណ៍ ប្រសិនបើអតិថិជនធ្វើដំណើរមានអាទិភាព កិច្ចការរបស់ពួកគេនឹងត្រូវគ្រប់គ្រងតាមជំហានប្រតិបត្តិការផ្សេង។

*ខ្សែកំណត់បង្ហោះចេញ (Fan-out Edges)* - ផ្ញើសារមួយទៅគោលដៅច្រើន។

*ខ្សែកំណត់បង្ហោះចូល (Fan-in Edges)* - ប្រមូលសារច្រើនពីអ្នកអនុវត្ដផ្សេងៗ ហើយផ្ញើទៅគោលដៅមួយ។

**ព្រឹត្តិការណ៍ (Events)**

ដើម្បីផ្តល់ការមើលទស្សនាល្អប្រសើរពីជំហានប្រតិបត្តិការ MAF ផ្ដល់ព្រឹត្តិការណ៍បង្កើតក្នុងសម្រាប់ការអនុវត្ត រួមមាន៖

- `WorkflowStartedEvent`  - ការអនុវត្តជំហានប្រតិបត្តិការចាប់ផ្តើម
- `WorkflowOutputEvent` - ជំហានប្រតិបត្តិការបញ្ចេញផលលទ្ធផល
- `WorkflowErrorEvent` - ជំហានប្រតិបត្តិការប្រទះឃើញកំហុស
- `ExecutorInvokeEvent`  - អ្នកអនុវត្ដចាប់ផ្តើមដំណើរការ
- `ExecutorCompleteEvent`  - អ្នកអនុវត្ដបញ្ចប់ដំណើរការ
- `RequestInfoEvent` - ការស្នើសុំត្រូវបានចេញផ្សាយ

## លំនាំ MAF ទំនើប

ផ្នែកខាងលើគ្របដណ្តប់គំនិតសំខាន់ៗនៃ Microsoft Agent Framework។ នៅពេលអ្នកបង្កើតភ្នាក់ងារលំដាប់ខ្ពស់ ខាងក្រោមជាលំនាំទំនើបដែលត្រូវចាត់ទុក៖

- **រួមបញ្ចូលមេឌៀវ៉ែរ**៖ ស្វ័យប្រវត្តិភ្ជាប់អ្នកដំណើរការមេឌៀវ៉ែរ ច្រើន (ចុះបញ្ជី, ផ្ទៀងផ្ទាត់, ការកាត់បន្ថយអត្រា) ដោយប្រើមេឌៀវ៉ែរ មុខងារ និងជជែកសម្រាប់ការគ្រប់គ្រងលំដាប់តូចល្មមលើអាកប្បកម្មភ្នាក់ងារ។
- **បញ្ចាក់ព្រឹត្តិការណ៍ជំហានប្រតិបត្តិការ**៖ ប្រើព្រឹត្តិការណ៍ជំហាន និងការស៊ីលរីសកម្មភាពដើម្បីរក្សា និងបន្តដំណើរការភ្នាក់ងារដំណើរការវែង។
- **ជ្រើសយកឧបករណ៍ឌីណាមិក**៖ ប្រើសមាសភាព RAG លើការពិពណ៌នាឧបករណ៍ជាមួយការចុះបញ្ជីឧបករណ៍ពី MAF ដើម្បីបង្ហាញឧបករណ៍ដែលមានសារៈសំខាន់តែមួយសម្រាប់សំណើ។
- **ការផ្ទេរភ្នាក់ងារជាច្រើន**៖ ប្រើខ្សែកំណត់ប្រតិបត្តិការ និងចំណងជើងលក្ខខណ្ឌដើម្បីរៀបចំការផ្ទេរជាមួយភ្នាក់ងារដែលមានជំនាញ។

## ការផ្ទុកភ្នាក់ងារ LangChain / LangGraph នៅលើ Microsoft Foundry

Microsoft Agent Framework គឺជា **framework-interoperable** — អ្នកមិនត្រូវបានដាក់កំណត់ត្រឹមតែភ្នាក់ងារដែលចងក្រងជាមួយ MAF ទេ។ ប្រសិនបើអ្នកមានភ្នាក់ងារមួយដែលបង្កើតជាមួយ **LangChain** ឬ **LangGraph**, អ្នកអាចរត់វាជាភ្នាក់ងារដែល **Microsoft Foundry ផ្ទុក** ដើម្បីឲ្យ Foundry គ្រប់គ្រង runtime, សម័យ, ការលៃតម្រូវ, អត្តសញ្ញាណ និងចំណុច protocol សម្រាប់អ្នក ខណៈដែលយុទ្ធសាស្ត្រភ្នាក់ងាររបស់អ្នកនៅក្នុង LangGraph។

នេះត្រូវធ្វើដោយកញ្ចប់ `langchain_azure_ai.agents.hosting` ដែលបង្ហាញការបង្កើតរូបភាព LangGraph នៅលើ protocol ដូចគ្នាដែលភ្នាក់ងារដែលបានផ្ទុកនៅ Foundry ប្រើ។

**1. តំឡើងបន្ថែម hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

កញ្ចប់ `hosting` តំឡើងបណ្ណាល័យ Foundry protocol៖ `azure-ai-agentserver-responses` (ចំណុចបញ្ចប់ `/responses` ដែលគាំទ្រ OpenAI) និង `azure-ai-agentserver-invocations` (ចំណុចបញ្ចប់ `/invocations` ទាំងមូល)។

**2. ជ្រើសរើស protocol hosting:**

| Protocol | ថ្នាក់ Host | ចំណុច Endpoint | ប្រើពេល |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | អ្នកចង់បានការជជែកដែលគាំទ្រ OpenAI, ស្ទ្រីម, ប្រវត្តិចម្លើយ និងខ្សែការសន្ទនា — ជាជម្រើសដែលផ្តល់អនុសាសន៏សម្រាប់ភ្នាក់ងារជជែក។ |
| **Invocations** | `InvocationsHostServer` | `/invocations` | អ្នកត្រូវការរូបរាង JSON ផ្ទាល់ខ្លួន, ចំណុច webhook, ឬដំណើរការមិនមែនជាជជែក។ |

ពីព្រោះ **API Responses គឺជាអ្នកសំខាន់សម្រាប់អភិវឌ្ឍន៍ភ្នាក់ងារស្តាយនៅ Foundry**, ចាប់ផ្តើមជាមួយ `ResponsesHostServer` សម្រាប់ភ្នាក់ងារច្រើន។

**3. កំណត់បរិយាកាសអថេរបរិដ្ឋាន** (`az login` ជាមុនដើម្បីឲ្យ `DefaultAzureCredential` អាចផ្ទៀងផ្ទាត់បាន):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

ពេលភ្នាក់ងាររត់ក្នុងនាមភ្នាក់ងារផ្ទុកនៅ Foundry វេទិកានេះនឹងបញ្ចូល `FOUNDRY_PROJECT_ENDPOINT` ដោយស្វ័យប្រវត្តិ។

**4. បញ្ចូលភ្នាក់ងារ LangGraph លើ protocol Responses:**

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

    # ChatOpenAI នៅទីនេះគោលបំណងទៅកាន់ចុងបង្អស់ (Responses) ដែលត្រូវផ្គូផ្គងនឹង OpenAI របស់គម្រោង Foundry។
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

រត់វាលើកន្លែងស្ថានីយ `python main.py` បន្ទាប់ពីផ្ញើសំណើ Responses ទៅ `http://localhost:8088/responses`។

**អាកប្បកម្មសំខាន់ៗ:**

- **ការជជែក**៖ អតិថិជនបន្តសន្ទនាដោយផ្ញើ `previous_response_id` ឬ ID `conversation` មកវិញ។ ប្រសិនបើរូបភាពរបស់អ្នកបានបង្កើតជាមួយ LangGraph checkpointer, Foundry នឹងពិនិត្យស្ថានភាពសន្ទนา​តាម checkpoint (ប្រើ durable checkpointer ក្នុងផលិតកម្ម; `MemorySaver` នៅល្អសម្រាប់សាកល្បងក្នុងតំបន់មូលដ្ឋាន)។
- **មនុស្សនៅក្នុងបន្ទាត់**៖ ប្រសិនបើរូបភាពរបស់អ្នកប្រើ LangGraph `interrupt()`, `ResponsesHostServer` នឹងបង្ហាញការជ្រាបចិត្តដែលនៅជំពូកជារបស់ Responses `function_call` / `mcp_approval_request` ហើយអតិថិជននឹងបន្តជាមួយ `function_call_output` / `mcp_approval_response` ត្រូវគ្នា។
- **ចម្លងទៅ Foundry**៖ ប្រើ Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ក្នុងតំបន់, តម្រូវ Docker), បន្ទាប់ `azd provision` និង `azd deploy`។ ការតម្លើងភ្នាក់ងារផ្ទុកតម្រូវតួនាទី **Foundry Project Manager**។

រូបមន្តដែលអាចរត់បាននៃឧទាហរណ៍នេះស្ថិតនៅ [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)។ សម្រាប់ការបណ្តុះបណ្តាលពេញលេញ (protocol Invocations, ខ្នាតសំណើផ្ទាល់ខ្លួន, និងដោះស្រាយបញ្ហា), សូមមើល [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)។

## គំរូកូដ

គំរូកូដសម្រាប់ Microsoft Agent Framework អាចស្វែងរកបាននៅក្នុងឃ្លាំងនេះនៅក្រោមឯកសារ `xx-python-agent-framework` និង `xx-dotnet-agent-framework`។

## មានសំនួរច្រើនទៀតអំពី Microsoft Agent Framework?

ចូលរួមជាមួយ [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ដើម្បីជួបជាមួយអ្នករៀនផ្សេងទៀត ចូលរួមម៉ោងការិយាល័យ និងទទួលបានពចម្លើយសំនួរអំពី AI Agents របស់អ្នក។
## មេរៀនមុន

[Memory for AI Agents](../13-agent-memory/README.md)

## មេរៀនបន្ទាប់

[Building Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->