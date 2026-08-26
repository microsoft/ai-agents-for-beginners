# മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനെ പരീക്ഷിക്കുക

![Agent Framework](../../../translated_images/ml/lesson-14-thumbnail.90df0065b9d234ee.webp)

### പരിചയം

ഈ പാഠം ഉൾക്കൊള്ളുന്നത്:

- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക്: പ്രധാന സവിശേഷതകളും മൂല്യവും മനസ്സിലാക്കുക  
- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ പ്രധാന ആശയങ്ങൾ പരിശോധിക്കുക
- പുരോഗമനപരമായ MAF മാതൃകകൾ: വർക്ക്‌ഫ്ളോകളം, മിഡിൽവെയർ, മെമ്മറി

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാക്കിയതിന് ശേഷം, നിങ്ങൾ അറിയാം:

- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് പ്രൊഡക്ഷൻ റെഡി AI ഏജന്റുകൾ നിർമ്മിക്കുക
- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ മുഖ്യ സവിശേഷതകൾ ഏജന്റിക് ഉപയോഗ കേസുകളിൽ പ്രയോഗിക്കുക
- വർക്ക്‌ഫ്ളോകളും മിഡിൽവെയറും ഒബ്സർവബിലിറ്റിയും ഉൾപ്പെടെയുള്ള പുരോഗമിച്ച മാതൃകകൾ ഉപയോഗിക്കുക

## കോഡ് സാമ്പിൾകൾ 

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) യുടെ കോഡ് സാമ്പിൾകൾ ഈ റെപ്പോസിറ്ററിയിൽ `xx-python-agent-framework` և `xx-dotnet-agent-framework` ഫയലുകളിൽ കാണാം.

## മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് അറിയുക

![Framework Intro](../../../translated_images/ml/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) AI ഏജന്റുകൾ നിർമ്മിക്കാൻ മൈക്രോസോഫ്റ്റിന്റെയുള്ള ഐക്യശാസ്ത്രീയ ഫ്രെയിംവർക്ക് ആണ്. പ്രൊഡക്ഷൻ, ഗവേഷണം എന്നിവിടങ്ങളിൽ കണ്ടുവരുന്ന വ്യത്യസ്തമായ ഏജന്റിക് ഉപയോഗ കേസുകൾ പ്രതിരോധിക്കാൻ ഇത് സൗകര്യം നൽകുന്നു, ഉൾപ്പെടെ:

- **സംക്രമ ക്രമീകരണം** അമ്പുലാർ ഏജന്റുകൾ ഒരു പടി പോലെ പ്രവർത്തിക്കാറുള്ള സാഹചര്യങ്ങളിൽ.
- **സമകാലിക ക്രമീകരണം** ഏജന്റുകൾ ഒരേസമയം ജോലികൾ പൂർത്തിയാക്കേണ്ട സാഹചരികളിൽ.
- **ഗ്രൂപ്പ് ചാറ്റ് ക്രമീകരണം** ഏജന്റുകൾ ഒരേ ജോലി സംബന്ധിച്ച് ഒന്നിച്ച് സഹകരിക്കാവുന്ന സാഹചര്യങ്ങളിൽ.
- **ഹാൻഡ്ഓഫ് ക്രമീകരണം** സബ്ടാസ്കുകൾ പൂർത്തിയായപ്പോൾ ഏജന്റുകൾ ഒരു രണ്ടിലേയ്ക്ക് ജോലി കൈമാറുന്ന സാഹചര്യങ്ങളിൽ.
- **മാഗ്നറ്റിക് ക്രമീകരണം** മാനേജർ ഏജന്റ് ജോലി പട്ടിക ഉണ്ടാക്കുകയും തിരുത്തുകയും സബ്എജന്റുകളുടെ കോഓർഡിനേഷൻ കൈകാര്യം ചെയ്യുകയും ചെയ്യുന്ന സാഹചര്യങ്ങളിൽ.

പ്രൊഡക്ഷനിൽ AI ഏജന്റുകൾ ഡെലിവർ ചെയ്യാൻ MAF ഉൾപ്പെടുത്തിയ സവിശേഷതകൾ ഉൾക്കൊള്ളുന്നു:

- **ഓബ്സർവബിലിറ്റി** OpenTelemetry ഉപയോഗിച്ച്, AI ഏജന്റിന്റെ എല്ലാ പ്രവർത്തനങ്ങളും ഉൾപ്പെടെ ടൂൾ കോളുകൾ, ക്രമീകരണ ഘട്ടങ്ങൾ, കാരണചിന്തനം, Microsoft Foundry ഡാഷ്ബോർഡുകൾ വഴി പ്രകടന നിരീക്ഷണം.
- **സുരക്ഷ** Microsoft Foundryയിൽ നൈറടിവ് ഏജന്റുകൾ ഹോസ്റ്റുചെയ്യലിലൂടെ, ഭാഗിക ആക്സസ് നിയന്ത്രണങ്ങൾ, സ്വകാര്യ ഡാറ്റ കൈകാര്യം ചെയ്യൽ, ഉള്ളടക്കസുരക്ഷ എന്നിവ.
- **ദൃഢത** ഏജന്റ് ത്രെഡ്‌സ്, വർക്ക്‌ഫ്ളോകൾ പause, പുനരാരംഭം, പിശകുകളിൽ നിന്നും വീണ്ടെടുക്കൽ സാധ്യമാക്കുന്നു, ദീർഘകാല പ്രവർത്തനം.
- **നിയന്ത്രണം** മനുഷ്യ അംഗത്തിലൂടെ പ്രവൃത്തി നടക്കുന്നതിന് പിന്തുണ, മനുഷ്യ മಂಜൂർ മാർക്ക് ചെയ്യേണ്ട പ്രവർത്തികൾ.

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് ഇന്റർഓപ്പറബിൾ ആകാൻ ശ്രദ്ധിക്കുന്നു:

- **ക്ലൗഡ്-അഗ്നോസ്റി** - ഏജന്റുകൾ കണ്ടെയ്നറുകളിലും ഓൺ-പ്രേംലും പല ക്ലൗഡുകളിൽ പ്രവർത്തിക്കാം.
- **പ്രൊവൈഡർ-അഗ്നോസ്റി** - Azure OpenAI, OpenAI ഉൾപ്പെടെയുള്ള ഇഷ്ട SDK ഉപയോഗിച്ച് ഏജന്റുകൾ സൃഷ്ടിക്കാം.
- **ഓപ്പൺ സ്റ്റാൻഡാർഡുകളുടെ സംയോജനം** - Agent-to-Agent (A2A), Model Context Protocol (MCP) പോലുള്ള പ്രോട്ടോകോളുകൾ ഉപയോഗിച്ച് മറ്റ് ഏജന്റുകളും ടൂളുകളും കണ്ടെത്തി ഉപയോഗിക്കുക.
- **പ്ലഗിനുകൾ, കണക്റ്ററുകൾ** - Microsoft Fabric, SharePoint, Pinecone, Qdrant പോലുള്ള ഡാറ്റ, മെമ്മറി സേവനങ്ങളുമായി കണക്റ്റ് ചെയ്യാം.

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ ഈ സവിശേഷതകൾ പ്രധാന ആശയങ്ങളിൽ എങ്ങനെ പ്രയോഗിക്കപ്പെടുന്നു നോക്കാം.

## മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ പ്രധാന ആശയങ്ങൾ

### ഏജന്റുകൾ

![Agent Framework](../../../translated_images/ml/agent-components.410a06daf87b4fef.webp)

**ഏജന്റുകൾ സൃഷ്ടിക്കൽ**

ഏജന്റ് സൃഷ്ടിക്കുന്നത് ഇൻഫറൻസ് സർവിസ് (LLM പ്രൊവൈഡർ), AI ഏജന്റ് അനുസരിക്കേണ്ട നിർദ്ദേശങ്ങൾ, ഒരു `name` നിശ്ചയിച്ചെഴുതലാണ്:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

മുകളിൽ `Azure OpenAI` ഉപയോഗിച്ചിരിക്കുന്നതാണെങ്കിലും വിവിധ സേവനങ്ങൾ ഉപയോഗിച്ച് ഏജന്റുകൾ സൃഷ്ടിക്കാം, ഉദാഹരണം `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIകൾ

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

അല്ലെങ്കിൽ [MiniMax](https://platform.minimaxi.com/), അത് വലിയ കോൺടെക്സ്റ്റ് വിൻഡോകളുള്ള (204K ടോക്കൺ വരെ) OpenAI-സൗഹൃദ API ആണ്:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

അല്ലെങ്കിൽ A2A പ്രോട്ടോക്കോൾ ഉപയോഗിച്ച് ദൂര ഏജന്റുകൾ:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ഏജന്റുകൾ പ്രവർത്തിപ്പിക്കുക**

ഏജന്റുകൾ `.run` അല്ലെങ്കിൽ `.run_stream` മെഥഡുകൾ ഉപയോഗിച്ച് സ്ട്രീമിംഗ് അല്ലാത്തതോ സ്ട്രീമിംഗ് പ്രതികരണത്തിനോ പ്രവർത്തിപ്പിക്കുന്നു.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ഓരോ ഏജന്റ് റൺ സമയത്തും `max_tokens`, `tools` (ഏജന്റ് വിളിക്കാൻ കഴിയുന്ന) എന്നിങ്ങനെ ഒപ്ഷനുകൾ പ്രത്യേകം ഉദ്യോഗസ്ഥർക്ക്, അവരെ ഉപയോഗിച്ചുള്ള `model` എന്നിവകം സജ്ജീകരിക്കാം.

ഇത് ഉപയോക്താവിന്റെ ജോലിയെ തികയ്ക്കാൻ പ്രത്യേക മാതൃകകളും ടൂളുകളും ആവശ്യമായ കാര്യങ്ങളിൽ ഉപയോഗിക്കുന്നു.

**ടൂളുകൾ**

ടൂളുകൾ ഏജന്റ് നിർവചിക്കുമ്പോഴും պുഴ

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# നേരിട്ട് ഒരു ChatAgent സൃഷ്ടിക്കുമ്പോൾ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ഏജന്റ് പ്രവർത്തിപ്പിക്കുമ്പോഴും:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ഈ റണ്ണിനായി മാത്രമുള്ള ഉപകരണം )
```

**ഏജന്റ് ത്രെഡ്‌സ്**

ഏജന്റ് ത്രെഡ്‌സ് മൾട്ടി-ടേൺ സംഭാഷണങ്ങൾ കൈകാര്യം ചെയ്യാൻ ഉപയോഗിക്കുന്നു. ത്രെഡുകൾ ഉണ്ടാക്കുന്നത്:

- `get_new_thread()` ഉപയോഗിച്ച്, ഇത് ത്രെഡ്‌ സമയം കൊണ്ടു സംരക്ഷിക്കുവാൻ സഹായിക്കുന്നു
- ഏജന്റ് പ്രവർത്തിപ്പിക്കുമ്പോൾ ത്രെഡ് സ്വയം‌ സൃഷ്ടിക്കുകയും നിലവിലെ റണ്ണിലെ മാത്രം നിലനിൽക്കുകയും ചെയ്യുന്നു.

ത്രെഡ് സൃഷ്ടിക്കാൻ കോഡ് ഇങ്ങനെ കാണാം:

```python
# പുതിയ ഒരു ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() # അതേ ത്രെഡിൽ ഏജന്റ് പ്രവർത്തിപ്പിക്കുക.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

പിന്നീട് ത്രെഡ് സ്ഥിരപ്പെടുത്തുന്നതിനുള്ള സീരിയലൈസേഷൻ ചെയ്യാം:

```python
# ഒരു പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() 

# ത്രെഡിനൊപ്പം ഏജന്റ് പ്രവർത്തിപ്പിക്കുക.

response = await agent.run("Hello, how are you?", thread=thread) 

# സംഭരണത്തിനായി ത്രെഡ് സീരിയലൈസ് ചെയ്യുക.

serialized_thread = await thread.serialize() 

# സംഭരണത്തിൽ നിന്ന് ലോഡ് ചെയ്തതിനു ശേഷം ത്രെഡ് സ്റ്റേറ്റ് ഡിസീരിയലൈസ് ചെയ്യുക.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ഏജന്റ് മിഡിൽവെയർ**

ഉപയോക്താക്കളുടെ പ്രവർത്തനങ്ങൾ പൂർത്തിയാക്കാൻ ഏജന്റുകൾ ടൂളുകളുമായും LLMഉം ഇടപഴകുന്നു. ഇത്തരത്തിലുള്ള ഇടപെടലുകൾക്കിടയിൽ പ്രവർത്തനം നടപ്പിലാക്കണമെങ്കിൽ ഏജന്റ് മിഡിൽവെയർ ഇത് സാധ്യമാക്കുന്നു:

*ഫംഗ്ഷൻ മിഡിൽവെയർ*

ഏജന്റ് ടൂൾ/ഫംഗ്ഷനെ വിളിക്കുന്നതിന് ഇടയിൽ പ്രവർത്തനം നടത്താമെന്നതാണ് ഈ മിഡിൽവെയർ. ഉദാഹരണത്തിന് ഫംഗ്ഷൻ കോളിന്റെ ലോഗിംഗ്.

താഴെയുള്ള കോഡിൽ `next` നിർവചിക്കുന്നത് അടുത്ത മിഡിൽവെയർ അല്ലെങ്കിൽ തൽസമയം ഫംഗ്ഷൻ വിളിക്കണമെന്ന്.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # പ്രി-പ്രോസസ്സിംഗ്: ഫംഗ്ഷൻ എന്നമുമ്പ് ലോഗ് ചെയ്യുക
    print(f"[Function] Calling {context.function.name}")

    # അടുത്ത മിഡിൽവെയർ അല്ലെങ്കിൽ ഫംഗ്ഷൻ എക്സിക്യൂഷനിലേക്ക് തുടരുക
    await next(context)

    # പോസ്റ്റ്-പ്രോസസ്സിംഗ്: ഫംഗ്ഷൻ എക്സിക്യൂഷൻ കഴിഞ്ഞ് ലോഗ് ചെയ്യുക
    print(f"[Function] {context.function.name} completed")
```

*ചാറ്റ് മിഡിൽവെയർ*

ഏജന്റും LLM തമ്മിലുള്ള അപേക്ഷകളിൽ ഇടയിൽ പ്രവർത്തനമോ ലോഗിംഗോ നടത്താൻ ഇതാണ്.

ഇതിൽ AI സേവനത്തിന് അയയ്ക്കപ്പെടുന്ന `messages` പോലുള്ള പ്രധാന വിവരങ്ങൾ കിടക്കുന്നു.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # മുൻപ്രക്രിയ: AI کالിന് മുമ്പ് ലോഗ് ചെയ്യുക
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # അടുത്ത മിഡിൽവെയർ അല്ലെങ്കില്‍ AI സേവനത്തിലേക്ക് തുടരുക
    await next(context)

    # പിന്‍പ്രക്രിയ: AI പ്രതികരണത്തിന് ശേഷം ലോഗ് ചെയ്യുക
    print("[Chat] AI response received")

```

**ഏജന്റ് മെമ്മറി**

`Agentic Memory` പാഠത്തിൽ പറഞ്ഞതുപോലെ, മെമ്മറി ഏജന്റിനെ വ്യത്യസ്ത സന്ദർഭങ്ങളിൽ പ്രവർത്തിക്കാനാകുവാൻ സഹായിക്കുന്നു. MAF വിവിധ മെമ്മറി തരങ്ങൾ നൽകുന്നു:

*ഇൻ-മെമ്മറി സംഭരണം*

ആപ്ലിക്കേഷൻ ഓട്ടത്തിലെ ത്രെഡ്‌സിൽ സൂക്ഷിക്കപ്പെടുന്ന മെമ്മറി.

```python
# ഒരു പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() # ത്രെഡിനൊപ്പം ഏജന്റ് ആരംഭിക്കുക.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*സ്ഥിരതയുള്ള സന്ദേശങ്ങൾ*

പല സെഷനുകളിലായി സംവാദ ചരിത്രം നൽകരുതാൻ ഉപയോഗിക്കുന്ന മെമ്മറി. ഇത് `chat_message_store_factory` ഉപയോഗിച്ച് നിർവചിക്കുന്നു:

```python
from agent_framework import ChatMessageStore

# ഒരു കസ്റ്റം സന്ദേശ സ്റ്റോർ സൃഷ്‌ടിക്കുക
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*ഡൈനാമിക് മെമ്മറി*

ഏജന്റുകൾ പ്രവർത്തിക്കുന്നതിന് മുൻപ് കോൺടെക്സ്റ്റിൽ ചേർക്കുന്ന മെമ്മറി. ഇത് മെയ്മോ പോലുള്ള പുറം സേവനങ്ങളിൽ സൂക്ഷിക്കാം:

```python
from agent_framework.mem0 import Mem0Provider

# വിസ്തൃതമായ മെമ്മറി ശേഷികൾക്ക് Mem0 ഉപയോഗിക്കുന്നു
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

**ഏജന്റ് ഓബ്സർവബിലിറ്റി**

വിശ്വസനീയവും പരിരക്ഷണമായതുമായ ഏജന്റിക് സംവിധാനങ്ങൾ നിർമ്മിക്കാൻ ഓബ്സർവബിലിറ്റി പ്രധാനമാണ്. MAF OpenTelemetryഒടൊപ്പം സംയോജിപ്പിച്ച് ട്രേസിംഗ്‌, മീറ്ററുകൾ എന്നിവ നൽകുന്നു.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # എന്തെങ്കിലും ചെയ്യുക
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### വർക്ക്‌ഫ്ലോകൾ

MAF മുൻ നിർവചിച്ച പ്രവർത്തന ഘട്ടങ്ങൾ ഉള്ള വർക്ക്‌ഫ്ലോകൾ നൽകുന്നു, അവയിൽ AI ഏജന്റുകൾ ഘടകങ്ങൾ ആയി ഉൾക്കൊള്ളുന്നു.

വർക്ക്‌ഫ്ലോകൾ വ്യത്യസ്ത ഘടകങ്ങളാൽ നിർമ്മിതമാണ്, കൂടാതെ മെച്ചപ്പെട്ട നിയന്ത്രണം നൽകുന്നു. ഇത് **മൾട്ടി-ഏജന്റ് ക്രമീകരണം**ക്കും **ചെക്ക്പോയിന്റിംഗ്**ക്കുമായി സഹായിക്കുന്നു.

വർക്ക്‌ഫ്ലോയുടെ പ്രധാന ഘടകങ്ങൾ:

**എക്സിക്യൂട്ടറുകൾ**

എൻപുട്ട് സന്ദേശം സ്വീകരിക്കുകയും നിയോഗിത ജോലിയെടുക്കുകയും പിന്നീട് ഔട്ട്പുട്ട് സന്ദേശം നൽകിയതും വർക്ക്‌ഫ്ലോ മുന്നോട്ട് കൊണ്ടുപോകുന്നു. എക്സിക്യൂട്ടർ AI ഏജന്റ് അല്ലെങ്കിൽ കസ്റ്റം ലാജിക് ആയിരിക്കും.

**എഡ്ജുകൾ**

വർക്ക്‌ഫ്ലോയിൽ സന്ദേശങ്ങൾ കൊണ്ടുപോകാൻ എഡ്ജുകൾ നിർവചിക്കുന്നു. ഇവ:

*ഡയറക്ട് എഡ്ജുകൾ* - എക്സിക്യൂട്ടറുകൾ തമ്മിലുള്ള ലളിതമായ ബന്ധങ്ങൾ:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*കണ്ടീഷണൽ എഡ്ജുകൾ* - നിബന്ധനകൾ പാലിച്ച ശേഷം സജീവമാകുന്നു, ഉദാഹരണം, ഹോട്ടൽ റൂമുകൾ ലഭ്യമല്ലാത്തപ്പോൾ മറ്റൊരു നിർദ്ദേശം.

*സ്വിച്ച്-കേസ് എഡ്ജുകൾ* - നിബന്ധന അനുസരിച്ച് സന്ദേശങ്ങൾ വിവിധ എക്സിക്യൂട്ടറുകൾക്ക് റൂട്ടുചെയ്യുന്നു, ഉദാഹരണം, പ്രധാനാപ layering ഉപഭോക്താക്കളുടെ കാര്യങ്ങൾ മറ്റൊരു വർക്ക്‌ഫ്ലോയിലൂടെ കൈകാര്യം ചെയ്യുന്നു.

*ഫാൻ-ഔട്ട് എഡ്ജുകൾ* - ഒറ്റ സന്ദേശം പല ലക്ഷ്യങ്ങളിലേക്ക് അയയ്ക്കുന്നു.

*ഫാൻ-ഇൻ എഡ്ജുകൾ* - വ്യത്യസ്ത എക്സിക്യൂട്ടറുകളിൽ നിന്നും സന്ദേശങ്ങൾ പകര്‍ത്തി ഒന്നിലേയ്ക്ക് അയയ്ക്കുന്നു.

**ഇവന്റുകൾ**

വർക്ക്‌ഫ്ലോകളിൽ മെച്ചപ്പെട്ട ഓബ്സർവബിലിറ്റി വേണ്ടി MAF നിർമിച്ചിട്ടുള്ള ഇവന്റുകൾ:

- `WorkflowStartedEvent` - വർക്ക്‌ഫ്ലോ പ്രവർത്തനം ആരംഭിക്കുന്നു
- `WorkflowOutputEvent` - വർക്ക്‌ഫ്ലോ ഔട്ട്പുട്ട് സൃഷ്ടിക്കുന്നു
- `WorkflowErrorEvent` - വർക്ക്‌ഫ്ലോ പിശക് നേരിടുന്നു
- `ExecutorInvokeEvent` - എക്സിക്യൂട്ടർ പ്രവർത്തനം തുടങ്ങി
- `ExecutorCompleteEvent` - എക്സിക്യൂട്ടർ പ്രവർത്തനം പൂർത്തിയായി
- `RequestInfoEvent` - അഭ്യർത്ഥന പുറപ്പെടുന്നു

## പുരോഗമിച്ച MAF മാതൃകകൾ

മുകളിൽ മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ പ്രധാന ആശയങ്ങൾ ഉൾക്കൊള്ളിക്കുന്നു. കൂടുതൽ സങ്കീര്‍ണ്ണമായ ഏജന്റുകൾ നിർമ്മിക്കുമ്പോൾ പരിഗണിക്കാവുന്ന ചില പുരോഗമിത മാതൃകകൾ:

- **മിഡിൽവെയർ സംയോജനം**: നിരവധി മിഡിൽവെയർ ഹാൻഡ്ലറുകൾ (ലോഗിംഗ്, അഥോറൈസേഷൻ, റേറ്റ്-ലിമിറ്റിംഗ്) ഫങ്ഷൻ, ചാറ്റ് മിഡിൽവെയർ വഴി ക്രീമ ചെയ്ത ചൈൻ ചെയ്യുക, ഏജന്റ് പെരുമാറ്റം സൂക്ഷ്മമായി നിയന്ത്രിക്കാൻ.
- **വർക്ക്‌ഫ്ലോ ചെക്ക്പോയിന്റിംഗ്**: വർക്ക്‌ഫ്ലോ ഇവന്റുകളും സീരിയലൈസേഷനും ഉപയോഗിച്ച് ദീർഘകാല ഓടുന്ന ഏജന്റ് പ്രോസസുകൾ സംരക്ഷിക്കുകയും പുനരാരംഭിക്കുകയും ചെയ്യുക.
- **ഡൈനാമിക് ടൂൾ സെലക്ഷൻ**: RAG ഉപയോക്തൃ അഭ്യാസങ്ങളുടെ അടിസ്ഥാനത്തിൽ MAF-യുടെ ടൂൾ രജിസ്ട്രേഷൻ ഉപയോഗിച്ച് പ്രാധാന്യമുള്ള ടൂളുകൾ മാത്രം പ്രദർശിപ്പിക്കുക.
- **മൾട്ടി-ഏജന്റ് ഹാൻഡ്ഓഫ്**: വർക്ക്‌ഫ്ലോ എഡ്ജുകളും കണ്ടീഷണൽ റൂട്ടിങ്ങും ഉപയോഗിച്ച് പ്രത്യേക ഏജന്റുകൾക്കിടയിൽ ഹാൻഡ്ഓഫ് ക്രമീകരിക്കുക.

## Microsoft Foundryയിൽ LangChain / LangGraph ഏജന്റുകൾ ഹോസ്റ്റ് ചെയ്യൽ

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് **ഫ്രെയിംവർക്ക് ഇന്റർഓപ്പറേബിൾ** ആണ് — MAF ഉപയോഗിച്ചുകൊണ്ടുള്ള ഏജന്റുകൾക്കുതന്നെ സ്മിതമായ അന്തരീക്ഷമല്ല. നിങ്ങൾക്ക് ഇതിനകം നിർമ്മിച്ച **LangChain** അല്ലെങ്കിൽ **LangGraph** ഏജന്റ് **Microsoft Foundry ഹോസ്റ്റുചെയ്ത ഏജന്റ്** ആയി പ്രവർത്തിക്കാൻ കഴിയും, Foundry റൺടൈം, സെഷനുകൾ, സ്കെയ്ലിംഗ്, ഐഡന്റിറ്റി, പ്രോട്ടോക്കോൾ എന്റ്പോയിന്റുകൾ കൈകാര്യം ചെയ്യുന്നതായി, നിങ്ങളുടെ ഏജന്റ് ലാജിക് LangGraph-ൽ തന്നെ തുടരുന്നു.

ഇത് `langchain_azure_ai.agents.hosting` പാക്കേജ് ഉപയോഗിച്ച് സാധ്യമാകുന്നു, ഇത് Compiled LangGraph ഗ്രാഫ് Foundry ഹോസ്റ്റുചെയ്ത ഏജന്റുകൾ ഉപയോഗിക്കുന്ന സമാന പ്രോട്ടോക്കോളുകൾ വഴി പ്രദർശിപ്പിക്കുന്നു.

**1. ഹോസ്റ്റിംഗ് എക്‌ട്രാ ഇൻസ്റ്റാൾ ചെയ്യുക:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` എക്‌ട്ര അതിൽ Foundry പ്രോട്ടോക്കോൾ ലൈബ്രറികൾ: `azure-ai-agentserver-responses` (OpenAI-സൗകര്യമുള്ള `/responses` എന്റ്പോയിന്റ്), `azure-ai-agentserver-invocations` (ജനറിക് `/invocations` എന്റ്പോയിന്റ്) ഉൾക്കൊള്ളുന്നു.

**2. ഹോസ്റ്റിംഗ് പ്രോട്ടോക്കോൾ തിരഞ്ഞെടുക്കുക:**

| പ്രോട്ടോക്കോൾ | ഹോസ്റ്റ് ക്ലാസ് | എന്റ്പോയിന്റ് | ഉപയോഗസമയം |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI-സൗകര്യമുള്ള ചാറ്റ്, സ്ട്രീമിംഗ്, പ്രതികരണ ചരിത്രം, സംഭാഷണ ത്രെഡിങ് വേണ്ടപ്പോൾ - ആഗോള ശുപാർശയായി. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | കസ്റ്റം JSON രൂപം, webhook-സ്റ്റൈൽ എന്റ്പോയിന്റ്, അല്ലെങ്കിൽ സംഭാഷണാതീത പ്രോസസ്സിംഗ് ആവശ്യമായപ്പോൾ. |

**Responses API Foundry-യിലെ ഏജന്റ്-സ്റ്റൈൽ ഡെവലപ്‌മെന്റിന് പ്രധാന API ആണെന്ന്** കാരണം, കൂടുതൽ ഏജന്റുകൾക്ക് `ResponsesHostServer` ഉപയോഗിച്ച് ആരംഭിക്കുക.

**3. പരിസ്ഥിതി വേരിയബിൾസ് കോൺഫിഗർ ചെയ്യുക** (`az login` മുൻപ് പ്രവർത്തിക്കണം, `DefaultAzureCredential` ബാധകമാക്കുന്നതിന്):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

ഏജന്റ് പിന്നീട് Foundry ഹോസ്റ്റുചെയ്ത ഏജന്റായി പ്രവർത്തിക്കുമ്പോൾ പ്ലാറ്റ്‌ഫോം സ്വയം `FOUNDRY_PROJECT_ENDPOINT` നൽകും.

**4. Responses പ്രോട്ടോക്കോൾ വഴി LangGraph ഏജന്റ് പ്രദർശിപ്പിക്കുക:**

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

    # ChatOpenAI ഇവിടെ Foundry പ്രോജക്റ്റിന്റെ OpenAI-අനുകൂല (Responses) എൻഡ്‌പോയിന്റിനെ ലക്ഷ്യമിടുന്നു.
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

`python main.py` ഉപയോഗിച്ച് ലൊക്കലായി പ്രവർത്തിപ്പിക്കുക, തുടർന്ന് `http://localhost:8088/responses`-ന് Responses അഭ്യർത്ഥന അയയ്ക്കുക.

**പ്രധാന പെരുമാറ്റങ്ങൾ:**

- **സംഭാഷണങ്ങൾ**: ക്ലയന്റുകൾ `previous_response_id` അല്ലെങ്കിൽ `conversation` ID കൈമാറിയാണ് സംഭാഷണം തുടയ്ക്കുന്നത്. നിങ്ങളുടെ ഗ്രാഫ് LangGraph ചെക്ക്പോയിന്ററുമായി কম്പൈൽ ചെയ്താൽ, Foundry ചെക്ക്പോയിന്റിലേക്ക് സംഭാഷണ നില നിശ്ചയിക്കും (പ്രൊഡക്ഷനിൽ ദൃശ്യമേറിയ ചെക്ക്പോയിന്റർ, പ്രാദേശിക പരിശോധനയ്ക്ക് `MemorySaver` ആവശ്യമാണ്).
- **മനുഷ്യ-ഇൻ-ദി-ലൂപ്**: നിങ്ങളുടെ ഗ്രാഫ് LangGraph `interrupt()` ഉപയോഗിച്ചാൽ, `ResponsesHostServer` നെ പോകുന്ന ഇടപെടൽ Responses `function_call` / `mcp_approval_request` ഐറ്റമായി കാണിക്കും, ക്ലയന്റുകൾ `function_call_output` / `mcp_approval_response` കൈമാറി തുടരും.
- **Foundry-ലേക്ക് ഡിപ്ലോയ് ചെയ്യുക**: Azure Developer CLI ഉപയോഗിക്കുക — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ലൊക്കൽ, Docker ആവശ്യമാണ്), തുടർന്ന് `azd provision` , `azd deploy`. ഹോസ്റ്റ്-ഏജന്റ് ഡിപ്ലോയ്‌മെന്റിന് **Foundry Project Manager** റൊൾ ആവശ്യമാണ്.

ഈ ഉദാഹരണത്തിന്റെ പ്രവർത്തനരാജി [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ൽ കിടക്കുന്നു. പൂർണ്ണ വിശദീകരണത്തിന് (Invocations പ്രോട്ടോക്കോൾ, കസ്റ്റം അഭ്യർത്ഥന സ്കീമകൾ, പ്രശ്‌നം പരിഹാരങ്ങൾ) [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) കാണുക.

## കോഡ് സാമ്പിൾകൾ 

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ കോഡ് സാമ്പിൾകൾ ഈ റെപ്പോസിറ്ററിയിൽ `xx-python-agent-framework` և `xx-dotnet-agent-framework` ഫയലുകളിൽ കാണാം.

## മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനെ സംബന്ധിച്ച് കൂടുതൽ ചോദിക്കാനുണ്ടോ?

മറ്റ് പഠിതാക്കളുമായി 만나ാനും ഓഫീസ് മണിക്കൂറുകളിൽ പങ്കെടുക്കാനും നിങ്ങളുടെ AI ഏജന്റ് ചോദ്യങ്ങൾക്കുള്ള ഉത്തരം ലഭിക്കാനും [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ലേക് ചേരൂ.
## മുൻപത്തെ പാഠം

[AI ഏജന്റുകൾക്കായുള്ള മെമ്മറി](../13-agent-memory/README.md)

## അടുത്ത പാഠം

[കമ്പ്യൂട്ടർ ഉപയോഗ ഏജന്റുകൾ നിർമ്മിക്കൽ (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->