# മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനെ സംശോധനം ചെയ്യൽ

![Agent Framework](../../../translated_images/ml/lesson-14-thumbnail.90df0065b9d234ee.webp)

### പരിചയം

ഈ പാഠം കവർ ചെയ്യുന്നത്:

- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ അവഗാഹനം: പ്രധാന സവിശേഷതകളും മൂല്യവും  
- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ പ്രധാന ധാരണകൾ പരിശോധിക്കൽ
- ഉയർന്ന MAF പാറ്റേണുകൾ: വർക്ക്‌ഫ്ലോകൾ, മിഡിൽവെയർ, മെമ്മറി

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാക്കിയ ശേഷം, നിങ്ങൾക്ക് എങ്ങനെ അറിയാം:

- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനെ ഉപയോഗിച്ച് പ്രൊഡക്ഷൻ റെഡി AI ഏജന്റുമാർ നിർമ്മിക്കുക
- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ പ്രാഥമിക സവിശേഷതകൾ നിങ്ങളുടെ ഏജന്റിക്ക് അനുയോജ്യമായ കാര്യങ്ങളിൽ പ്രയോഗിക്കുക
- വർക്ക്‌ഫ്ലോകൾ, മിഡിൽവെയർ, നിരീക്ഷണങ്ങൾ ഉൾപ്പെടെ ഉയർന്ന പാറ്റേണുകൾ ഉപയോഗിക്കുക

## കോഡ് സാമ്പിളുകൾ

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) -നുള്ള കോഡ് സാമ്പിളുകൾ ഈ റിപ്പോസിറ്ററിയിൽ `xx-python-agent-framework`യും `xx-dotnet-agent-framework` ഫയലുകളിൽ കണ്ടെത്താനാകും.

## മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ അവഗാഹനം

![Framework Intro](../../../translated_images/ml/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) മൈക്രോസോഫ്റ്റിന്റെ ഐക്യദാർഢ്യത്തോടെയാണ് AI ഏജന്റുമാർ നിർമ്മിക്കുന്ന ഫ്രെയിംവർക്കാണ്. പ്രൊഡക്ഷൻ, ഗവേഷണ പരിസരങ്ങളിൽ കാണപ്പെടുന്നവ പോലുള്ള വൈവിധ്യമാർന്ന ഏജന്റ് ഉപയോഗകേസുകളെ മറുപടി നൽകുന്ന സാഹചര്യങ്ങൾ ഉൾക്കൊള്ളിക്കുന്നു:

- **നിരക്കേട് ഏജന്റ് ഓർക്കസ്ട്രേഷൻ** - ഘട്ടംഘട്ട workflows ആവശ്യമായ സാഹചര്യങ്ങളിൽ.
- **സമകാലിക ഓർക്കസ്ട്രേഷൻ** - ഏജന്റുമാർ ഒരേ സമയത്തു തങ്ങളുടെ പ്രവൃത്തി പൂർത്തിയാക്കേണ്ട സാഹചര്യങ്ങൾ.
- **ഗ്രൂപ്പ് ചാറ്റ് ഓർക്കസ്ട്രേഷൻ** - ഒരു ജോലി പൂർത്തിയാക്കാൻ ഏജന്റുമാർ ഒത്തുചേരുന്ന സാഹചര്യങ്ങൾ.
- **ഹാൻഡോഫ് ഓർക്കസ്ട്രേഷൻ** - ഉപജോലികൾ പൂർത്തിയാകുമ്പോൾ ഏജന്റുമാർ ജോലി ഒരുമിച്ച് കൈമാറുന്ന സാഹചര്യങ്ങൾ.
- **മാഗ്നറ്റിക് ഓർക്കസ്ട്രേഷൻ** - ഒരു മാനേജർ ഏജന്റ് ജോലി പട്ടിക സൃഷ്ടിച്ച്, മാറ്റങ്ങൾ വരുത്തുകയും ഉപ ഏജന്റുമാരുടെ സംക്രമണം കൈകാര്യം ചെയ്യുകയും ചെയ്യുന്ന സാഹചര്യങ്ങൾ.

പ്രൊഡക്ഷനിൽ AI ഏജന്റുമാർ നൽകാൻ, MAF-യിൽ അടങ്ങിയിരിക്കുന്ന സവിശേഷതകൾ:

- **നിയന്ത്രണക്ഷമത** OpenTelemetry ഉപയോഗിച്ച്, AI ഏജന്റിന്റെ ഓരോ പ്രവർത്തിയും ഉൾപ്പെടെ ടൂൾ വിളിക്കൽ, ഓർക്കസ്ട്രേഷൻ ഘട്ടങ്ങൾ, വിവേക പ്രവാഹങ്ങൾ, Microsoft Foundry ഡാഷ്ബോർഡിലൂടെ പ്രവർത്തന നിരീക്ഷണം.
- **സുരക്ഷ** Microsoft Foundry-യിൽ അസാധാരണമായി ഏജന്റുമാർ ഹോസ്റ്റ് ചെയ്യുന്നു, റോളഭിതമായ ആക്സസ്, സ്വകാര്യ ഡാറ്റ കൈകാര്യം, ഉള്ളടക്ക സുരക്ഷ.
- **ദൃഢത** ഏജന്റ് ത്രെഡുകളും workflow-കളും പാസ്, പുനരാരംഭം ചെയ്യാനും പിശകുകളിൽ നിന്ന് പകരാത്തതിനു സാധിക്കുന്നു, ദീർഘകാല പ്രവർത്തനത്തിന്.
- **നിയന്ത്രണം** മനുഷ്യൻ ഇന്റർവീനിങ് പ്രവർത്തനങ്ങളെ പിന്തുണയ്ക്കുന്നു, മനുഷ്യ അംഗീകാരം ആവശ്യമായ പ്രസിഡണ്ടുകൾ.

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് ഇന്റർഓപ്പറബിൾ ആകാൻ ശ്രദ്ധിക്കുന്നു:

- **ക്ലൗഡ്-അഗ്നോസ്റ്റിക്** - ഏജന്റുമാർ കണ്ടെയിനറുകളിൽ, ഓൺ-പ്രെം, വ്യത്യസ്ത ക്ലൗഡുകളിൽ ഓടാം.
- **പ്രൊവൈഡർ-അഗ്നോസ്റ്റിക്** - Azure OpenAI, OpenAI തുടങ്ങിയ SDK-കളിലൂടെ ഏജന്റുമാർ സൃഷ്ടിക്കാം.
- **ഓപ്പൺ സ്റ്റാൻഡേർഡുകൾ** - Agent-to-Agent (A2A), Model Context Protocol (MCP) പോലെയുള്ള പ്രോട്ടോക്കോളുകൾ ഉപയോഗിച്ച് മറ്റ് ഏജന്റുമാരെയും ടൂളുകളെയും കണ്ടെത്താനും ഉപയോഗിക്കാനും.
- **പ്ലഗിൻസും കണექტർസും** - Microsoft Fabric, SharePoint, Pinecone, Qdrant പോലെയുള്ള ഡാറ്റാ, മെമ്മറി സ വീസുകളുമായി ബന്ധിപ്പിക്കുന്നതിനു.

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ പ്രധാന ആശയങ്ങളിൽ ഈ സവിശേഷതകൾ എങ്ങനെ പ്രയോഗിക്കപ്പെടുന്നതാണെന്ന് നോക്കാം.

## മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ പ്രധാന ആശയങ്ങൾ

### ഏജന്റുമാർ

![Agent Framework](../../../translated_images/ml/agent-components.410a06daf87b4fef.webp)

**ഏജന്റുമാർ സൃഷ്ടിക്കൽ**

ഏജന്റ് സൃഷ്ടിക്കൽ ചെയ്യുന്നത് ഇൻഫെറെൻസ് സർവീസ് (LLM പ്രൊവൈഡർ), AI ഏജന്റിന് പാലിക്കവുന്ന നിർദ്ദേശങ്ങളുടെ സമുച്ചയം, ഒപ്പം ```name``` എന്നു നാമനിർദ്ദേശം നൽകി.


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

മുകളിൽ `Azure OpenAI` ഉപയോഗിച്ചിരിക്കുന്നു, എന്നാൽ ഒന്നിലധികം സർവീസുകൾ ഉപയോഗിച്ചും ഏജന്റുമാർ സൃഷ്ടിക്കാം, `Microsoft Foundry Agent Service` ഉൾപ്പെടെ:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API-കൾ

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

അല്ലെങ്കിൽ [MiniMax](https://platform.minimaxi.com/), വലിയ കോൺ‌ടെക്സ്റ്റ് വിൻഡോകൾ (204K ടോകൺ വരെ) ഉള്ള OpenAI-സമാന API പ്രദാനം ചെയ്യുന്നു:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

അല്ലെങ്കിൽ A2A പ്രോട്ടോക്കോൾ ഉപയോഗിച്ച് ദൂരസ്ഥ എൻസാനുകൾ:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ഏജന്റുമാർ ഓടിക്കൽ**

ഏജന്റുമാർ `.run` അല്ലെങ്കിൽ `.run_stream` മാർഗ്ഗങ്ങൾ ഉപയോഗിച്ച് സ്റ്റ്രീമിംഗ് ഉള്ളടക്കം അല്ലെങ്കിൽ ഇല്ലാത്ത സ്റ്റ്രീമിംഗ് റൺ ലഭ്യമാക്കുന്നു.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ഏജന്റ് ഓടിക്കുമ്പോൾ `max_tokens`, `tools` ഉപയോഗിക്കൽ, ഏജന്റിന്റെ ഉപയോഗം, `model` എന്നിവ ഉൾപ്പെടെ പാരാമീറ്ററുകൾ ക്രമീകരിക്കാൻ ഓപ്ഷനുകൾ ഉണ്ടാകാം.

ഉപയോക്താവിന്റെ ജോലി പൂർത്തിയാക്കാൻ പ്രത്യേക മോഡലുകൾ അല്ലെങ്കിൽ ടൂളുകൾ ആവശ്യമുള്ള സാഹചര്യങ്ങളിൽ ഇത് പ്രയോജനപ്പെടുന്നു.

**ടൂൾസ്**

ടൂളുകൾ ഏജന്റ് നിർവചിക്കുമ്പോഴും:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ഒരു ChatAgent നേരGrassമായി സൃഷ്ടിക്കുമ്പോൾ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ഏജന്റ് ഓടിക്കുമ്പോഴും:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ഈ റൺക്ക് മാത്രമായുള്ള ടൂൾ നൽകുന്നു )
```

**ഏജന്റ് ത്രെഡുകൾ**

മള്‍ട്ടി-ടേൺ സംഭാഷണങ്ങൾ കൈകാര്യം ചെയ്യാൻ ഏജന്റ് ത്രെഡുകൾ ഉപയോഗിക്കുന്നു. ത്രെഡ് സൃഷ്ടിക്കുന്നത് ഇങ്ങനെ:

- `get_new_thread()` ഉപയോഗിച്ച്, ഇത് ത്രെഡ് കാലാനുസൃതമായി സേവ് ചെയ്യാൻ അനുവദിക്കുന്നു
- ഏജന്റ് ഓടിക്കുമ്പോൾ സ്വയം ത്രെഡ് സൃഷ്ടിച്ച്, തുടരുന്ന ഓട്ടത്താണ് ത്രെഡ് ഉണ്ടായിരുന്നത്.

ത്രെഡ് സൃഷ്ടിക്കാൻ കോഡ് ഇപ്രകാരമാണ്:

```python
# ഒരു പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() # ത്രെഡുമായി ഏജന്റ് പ്രവർത്തിപ്പിക്കുക.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

പിന്നീട് ത്രെഡ് സീരിയലൈസ് ചെയ്ത് പിന്നീട് ഉപയോഗത്തിനായി സൂക്ഷിക്കാം:

```python
# പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() 

# ത്രെഡിൽ ഏജന്റെ ഓടിക്കുക.

response = await agent.run("Hello, how are you?", thread=thread) 

# സംഭരണത്തിനായി ത്രെഡ് സീരിയലൈസ് ചെയ്യുക.

serialized_thread = await thread.serialize() 

# സംഭരണത്തിൽ നിന്ന് ലോഡ് ചെയ്തത് ശേഷം ത്രെഡ് സ്റ്റേറ്റ് ഡിസീരിയലൈസ് ചെയ്യുക.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ഏജന്റ് മിഡിൽവെയർ**

ഉപയോക്താവിന്റെ ജോലികൾ പൂർത്തിയാക്കാൻ ഏജന്റുമാർ ടൂളുകളുമായി, LLM-കളുമായി ഇടപെടുന്നു. ചില സാഹചര്യങ്ങളിൽ ഈ ഇടപെടലുകൾക്കിടയിൽ പ്രവർത്തിക്കുകയോ ട്രാക്ക് ചെയ്യുകയോ വേണം. ഏജന്റ് മിഡിൽവെയർ ഇതിന് സഹായിക്കുന്നു:

*ഫങ്ഷൻ മിഡിൽവെയർ*

ഏജന്റും ഫങ്ഷനും/ടൂളും തമ്മിൽ ഇടയിൽ പ്രവർത്തനം നടത്താൻ ഈ മിഡിൽവെയർ സഹായിക്കുന്നു. ഉദാഹരണത്തിന്, ഫങ്ഷൻ കോൾ ലോഗ് ചെയ്യാനുള്ളത്.

താഴെയുള്ള കോഡിൽ `next` അടുത്ത മിഡിൽവെയർ അല്ലെങ്കിൽ യഥാർത്ഥ ഫങ്ഷൻ വിളിക്കണമെന്ന് നിർണ്ണയിക്കുന്നു.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # പ്രീ-പ്രോസസ്സിംഗ്: ഫംഗ്ഷൻ പ്രവർത്തനം ആരംഭിക്കുന്നതിന് മുമ്പ് ലോഗ് ചെയ്യുക
    print(f"[Function] Calling {context.function.name}")

    # അടുത്ത മിഡിൽവെയർ അല്ലെങ്കിൽ ഫംഗ്ഷൻ പ്രവർത്തനം തുടരണം
    await next(context)

    # പോസ്റ്റ്-പ്രോസസ്സിംഗ്: ഫംഗ്ഷൻ പ്രവർത്തനം കഴിഞ്ഞ് ലോഗ് ചെയ്യുക
    print(f"[Function] {context.function.name} completed")
```

*ചാറ്റ് മിഡിൽവെയർ*

ഏജന്റും LLM-ഉമാകുന്ന അഭ്യർത്ഥനകളുടെ ഇടയിൽ പ്രവർത്തനം നടത്താൻ ഈ മിഡിൽവെയർ സഹായിക്കുന്നു.

ഇതിൽ AI സർവീസിന് അയക്കുന്ന `messages` പോലുള്ള പ്രധാന വിവരങ്ങൾ ഉൾക്കൊള്ളുന്നു.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # പ്രീ-പ്രോസസിംഗ്: AI കോളിന് മുമ്പിൽ ലോഗ് ചെയ്യുക
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # അടുത്ത മിഡിൽവെയർ അല്ലെങ്കിൽ AI സേവനത്തിലേക്ക് തുടരുക
    await next(context)

    # പോസ്റ്റ്-പ്രോസസിംഗ്: AI പ്രതികരണത്തിന് ശേഷം ലോഗ് ചെയ്യുക
    print("[Chat] AI response received")

```

**ഏജന്റ് മെമ്മറി**

`Agentic Memory` പാഠത്തിൽ പറഞ്ഞതുപോലെ, മെമ്മറി ഏജന്റ് വിവിധ സാന്ദർഭങ്ങളിൽ പ്രവർത്തിക്കാൻ അനിവാര്യമാണ്. MAF പലതരം മെമ്മറികളും ഒരുക്കുന്നു:

*ഇൻ-മെമ്മറി സംഭരണം*

അപ്ലിക്കേഷൻ റൺടൈമിൽ ത്രെഡുകളിൽ സൂക്ഷിക്കുന്ന മെമ്മറി.

```python
# പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() # ത്രെഡോടുകൂടി ഏജენტი ഓടിക്കുക.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*പെർസിസ്റ്റന്റ് മെസ്സേജുകൾ*

വേർതിരിച്ച സെഷനുകളുടെ സംഭാഷണ ചരിത്രം സൂക്ഷിക്കാനുപയോഗിക്കുന്നു. `chat_message_store_factory` ഉപയോഗിച്ച് നിർവ്വചിക്കുന്നു:

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

*ഡൈനാമിക്ക് മെമ്മറി*

ഏജന്റുമാർ ഓടിക്കുന്നതിന് മുമ്പ് കോൺടെക്സ്റ്റിലേക്ക് ചേർക്കപ്പെടുന്ന മെമ്മറികൾ. mem0 പോലെയുള്ള ബാഹ്യ സേവനങ്ങളിൽ സൂക്ഷിക്കാം:

```python
from agent_framework.mem0 import Mem0Provider

# പുരോഗമിത മെമ്മറി കഴിവുകൾക്കായി Mem0 ഉപയോഗിക്കുന്നു
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

**ഏജന്റ് നിരീക്ഷണക്ഷമത**

വിശ്വാസയോഗ്യമായ, പരിപാലിക്കാവുന്ന ഏജന്റിക് സിസ്റ്റങ്ങൾ നിർമ്മിക്കാൻ നിരീക്ഷണക്ഷമത അനിവാര്യമാണ്. മികച്ച നിരീക്ഷണത്തിനായി MAF OpenTelemetry-യുമായി ഒത്തുചേർന്ന് ട്രേസിസും മീറ്ററുകളും നൽകുന്നു.

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

MAF മുൻകൂട്ടി നിർവ്വചിച്ച ഘട്ടങ്ങളടങ്ങിയ workflows നൽകുന്നു, അവയിൽ AI ഏജന്റുമാർ ഘടകങ്ങളായി ഉൾക്കൊള്ളുന്നു.

workflows മികച്ച നിയന്ത്രണഫ്രെയ്‌മ്വർക്ക് നൽകുന്ന വിവിധ ഘടകങ്ങളുള്ളതാണ്. workflows **മൾട്ടി-ഏജന്റ് ഓർക്കസ്ട്രേഷൻ**ക്കും **ചെക്ക്‌പോയിന്റിങ്**ക്കും (workflow നിലകൾ സംരക്ഷിക്കാൻ) സഹകരിക്കുന്നു.

ഒരു workflow-ന്റെ മുൽ ഘടകങ്ങൾ:

**എക്സിക്യൂട്ടർമാർ**

എക്‌സിക്യൂട്ടർമാർ ഇൻപുട്ട് സന്ദേശങ്ങൾ സ്വീകരിച്ച് തങ്ങളുടെ ചുമതലയുള്ള ജോലികൾ നടത്തുകയും ഔട്ട്പുട്ട് സന്ദേശം സൃഷ്ടിക്കുകയും workflow-നെ മുന്നേറിക്കുന്നു. ഇത് AI ഏജന്റ് അല്ലെങ്കിൽ കസ്റ്റം ലിസ്റ്റിക് ആകാം.

**എഡ്ജുകൾ**

workflow-യിലെ സന്ദേശങ്ങൾ പ്രവഹിപ്പിക്കാൻ എഡ്ജുകൾ ഉപയോഗിക്കുന്നു. അവ:

*ഡിറക്ട് എഡ്ജുകൾ* - എക്‌സിക്യൂട്ടർമാരുടെ തമ്മിലുള്ള ലളിതമായ ഒറ്റത്തൊട്ട് ബന്ധങ്ങൾ:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*പശ്ചാത്തല ശക്തി എഡ്ജുകൾ* - ചില നിബന്ധനകൾ നിറവേറ്റുമ്പോൾ സജീവമാകുന്നു. ഉദാ: ഹോട്ടൽ മുറികൾ ലഭ്യമല്ലെങ്കിൽ മറ്റൊരു പരിഹാരം നിർദ്ദേശിക്കുക.

*സ്വിച്ച്-കേസ് എഡ്ജുകൾ* - നിബന്ധനകൾ അനുസരിച്ച് സന്ദേശങ്ങൾ വിവിധ എക്‌സിക്യൂട്ടർമാർക്ക് റൂട്ട് ചെയ്യുക. ഉദാ: പ്രവാസ യാത്രക്കാരുടെ പ്രാധാന്യമുള്ള ആക്സസ് വേനൽ, മറ്റൊരു workflow വഴി ടാസ്കുകൾ കൈകാര്യം ചെയ്യുക.

*ഫാൻ-ഔട്ട് എഡ്ജുകൾ* - ഒരു സന്ദേശം ഒന്നിലധികം ലക്ഷ്യങ്ങളിലേക്കു അയയ്‌ക്കുക.

*ഫാൻ-ഇൻ എഡ്ജുകൾ* - വ്യത്യസ്ത എക്‌സിക്യൂട്ടർമാർ നിന്ന് സന്ദേശങ്ങൾ സമാഹരിച്ച് ഒരു ലക്ഷ്യത്തിലേക്ക് അയയ്‌ക്കുക.

**ഇവന്റുകൾ**

workflow-കളിൽ മെച്ചപ്പെട്ട നിരീക്ഷണത്തിന് MAF വിവിധ നിർമ്മിത ഇവന്റുകൾ നൽകുന്നു:

- `WorkflowStartedEvent` - workflow പ്രവർത്തനം ആരംഭിക്കുന്നു
- `WorkflowOutputEvent` - workflow ഔട്ട്‌പുട്ട് ഉണ്ടാക്കുന്നു
- `WorkflowErrorEvent` - workflow പിശക് നേരിടുന്നു
- `ExecutorInvokeEvent` - എക്‌സിക്യൂട്ടർ പ്രവർത്തനം ആരംഭിക്കുന്നു
- `ExecutorCompleteEvent` - എക്‌സിക്യൂട്ടർ പ്രവർത്തനം പൂർത്തിയാക്കുന്നു
- `RequestInfoEvent` - അഭ്യർത്ഥന പുറത്തിറക്കുന്നു

## ഉയർന്ന MAF പാറ്റേണുകൾ

മുകളിൽ മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ പ്രധാന ആശയങ്ങൾ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്. നിങ്ങൾ കൂടുതൽ സമന്വിതമായ ഏജന്റുമാർ നിർമ്മിക്കുമ്പോൾ, പരിഗണിക്കേണ്ട ഉയർന്ന പാറ്റേണുകൾ:

- **മിഡിൽവെയർ കോംപോസിഷൻ**: ഫങ്ഷൻ, ചാറ്റ് മിഡിൽവെയറുകളെ ലഗ്, 인증ം, നിരക്ക്-പരിധി എന്നിവയുമായി ശരിതിരുത്തൽ ഓർമ്മപ്പെടുത്തൽ സാധിക്കും.
- **വർക്ക്‌ഫ്ലോ ചെക്ക്‌പോയിന്റിങ്**: workflow ഇവന്റുകൾ ഉപയോഗിച്ച് ദീർഘകാല പ്രവർത്തനങ്ങൾ പുനരാരംഭിക്കാൻ സീരിയലൈസേഷൻ ഉപയോഗിക്കുക.
- **ഡൈനാമിക് ടൂൾ തിരഞ്ഞെടുപ്പ്**: ടൂൾ വിവരണങ്ങളിലെ RAG MAF-യുടെ ടൂൾ രജിസ്ട്രേഷൻ ഉപയോഗിച്ച് കേവലം അനുയോജ്യമായ ടൂളുകൾ ലഭ്യമാക്കുക.
- **മൾട്ടി-ഏജന്റ് ഹാൻഡോഫ്**: workflow എഡ്ജുകളും പാശ്ച few മത്സരുനിർബന്ധിത റൂട്ടിംഗും ഉപയോഗിച്ച് പ്രത്യേക ഏജന്റ്മാർ തമ്മിലുള്ള കൈമാറ്റം നിയന്ത്രിക്കുക.

## മൈക്രോസോഫ്റ്റ് ഫൗണ്ടറിയിൽ LangChain / LangGraph ഏജന്റ്മാർ ഹോസ്റ്റ് ചെയ്യുക

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് **ഫ്രെയിംവർക്ക്-ഇന്റർഓപ്പറബിൾ** ആണ് — MAF ഉപയോഗിച്ച് എഴുതിയ ഏജന്റുമാരിൽ മാത്രം നിങ്ങൾ പരിമിതനല്ല. നിങ്ങൾക്കു മുൻപേ LangChain അല്ലെങ്കിൽ LangGraph ഉപയോഗിച്ച് നിർമ്മിച്ച ഏജന്റ് ഉണ്ടെങ്കിൽ, അത് **Microsoft Foundry** ഹോസ്റ്റ് ചെയ്യുന്ന ഏജന്റ് ആയി ഓടിക്കാൻ കഴിയും, Foundry റൺടൈം, സെഷനുകൾ, സ്കെയ്ലിംഗ്, ഐഡന്റിറ്റി, പ്രോട്ടോക്കോൾ എൻഡ്‌പോയിന്റുകൾ കൈകാര്യം ചെയ്യുമ്പോൾ നിങ്ങളുടെ ഏജന്റ് ലാജിക്ക് LangGraph-ൽ തന്നെ തുടരുന്നു.

ഇത് `langchain_azure_ai.agents.hosting` പാക്കേജ് ഉപയോഗിച്ച് നടത്തുന്നു, Foundry ഹോസ്റ്റ് ചെയ്യുന്ന ഏജന്റുമാർ ഉപയോഗിക്കുന്ന സമാന പ്രോട്ടോക്കോളുകൾക്ക് മേൽ ഒരു എസ്‌ട്രാക്ടഡ് LangGraph ഗ്രാഫ് പരസ്യപ്പെടുത്തുന്നു.

**1. ഹോസ്റ്റിംഗ് എക്സ്ട്ര പാക്കേജ് ഇൻസ്റ്റാൾ ചെയ്യുക:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` എക്സ്ട്ര പാക്കേജ് Foundry പ്രോട്ടോക്കോൾ ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യുന്നു: `azure-ai-agentserver-responses` (OpenAI-സഹജമായ `/responses` എൻഡ്‌പോയിന്റ്) & `azure-ai-agentserver-invocations` (ജനറിക് `/invocations` എൻഡ്‌പോയിന്റ്).

**2. ഒരു ഹോസ്റ്റിംഗ് പ്രോട്ടോക്കോൾ തിരഞ്ഞെടുക്കുക:**

| പ്രോട്ടോക്കോൾ | ഹോസ്റ്റ് ക്ലാസ് | എൻഡ്‌പോയിന്റ് | ഉപയോഗിക്കേണ്ടപ്പോൾ |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI-സമാന ചാറ്റ്, സ്റ്റ്രീമിംഗ്, പ്രതികരണ ചരിത്രം, സംഭാഷണ ത്രെഡിംഗ് ആവശ്യപ്പെടുന്നവർക്കുള്ള ശുപാർശ ചെയ്ത ഡീഫോൾട്ട് |
| **Invocations** | `InvocationsHostServer` | `/invocations` | കസ്റ്റം JSON ഷേപ്പ്, വെബ്ഹുക്ക്-സ്റ്റൈൽ എൻഡ്‌പോയിന്റ്, അല്ലെങ്കിൽ അപസംവേദന പ്രവർത്തനങ്ങൾ ആവശ്യമായപ്പോൾ |

Foundry-യിലെ ഏജന്റ്-ശൈലി വികസനത്തിനായി പ്രധാന API ആയതിനാൽ, അധികം ഏജന്റ്മാർക്കായി `ResponsesHostServer` ഉപയോഗിച്ച് ആരംഭിക്കുക.

**3. പരിസരവും മാറ്റങ്ങളും ക്രമീകരിക്കുക** (`az login` ആദ്യം നടത്തുക ताकि `DefaultAzureCredential` സാധൂകരിക്കാം):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

ഏജന്റ് പിന്നീട് Foundry-യിൽ ഹോസ്റ്റ് ചെയ്ത ഏജന്റ് ആയി ഓടുമ്പോൾ, പ്ലാറ്റ്ഫോം `FOUNDRY_PROJECT_ENDPOINT` ഓട്ടോമാറ്റിക്കായി ഇൻജെക്ട് ചെയ്യും.

**4. Responses പ്രോട്ടോക്കോളിൽ LangGraph ഏജന്റ് പരസ്യമാക്കുക:**

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

    # ChatOpenAI ഇവിടെ Foundry പ്രോജക്റ്റിന്റെ OpenAI-സുമായ (Responses) എന്റ്പോയിന്റിനെ ലക്ഷ്യംവെക്കുന്നു.
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

`python main.py` കൊണ്ട് ലോക്കലായി പ്രവർത്തിപ്പിക്കുക, തുടർന്ന് `http://localhost:8088/responses` -ലേക്ക് Responses അഭ്യർത്ഥന അയയ്ക്കുക.

**പ്രധാന പ്രവർത്തനങ്ങൾ:**

- **സംഭാഷണങ്ങൾ**: ക്ലയന്റുകൾ `previous_response_id` അല്ലെങ്കിൽ `conversation` ID നൽകി സംഭാഷണം തുടരുന്നു. LangGraph ചെക്ക്‌പോയിന്ററും ഉപയോഗിച്ചാൽ, Foundry ചാറ്റ് സ്റ്റേറ്റ് ചെക്ക്‌പോയിന്റുമായി ബന്ധിപ്പിക്കുന്നു (പ്രൊഡക്ഷൻ-പയോഗത്തിനായി ദീർഘജീവി ചെക്ക്‌പോയിന്റ്; ലോക്കൽ ടെസ്റ്റിംഗിനായി `MemorySaver` മതിയാകും).
- **മനുഷ്യൻ-ഇൻ-ലുപ്**: LangGraph-ന്റെ `interrupt()` ഉപയോഗിച്ചാൽ, `ResponsesHostServer` പendente interrupt-നെ Responses `function_call` / `mcp_approval_request` ആയി കാണിക്കുന്നു, ക്ലയന്റുകൾ `function_call_output` / `mcp_approval_response` കൂടി മടങ്ങുന്നു.
- **Foundry-ലേക്ക് ദേശിയമാക്കി**: Azure Developer CLI ഉപയോഗിക്കുക — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (സാങ്കേതികമായി Docker ആവശ്യമാണ്), തുടർന്ന് `azd provision` & `azd deploy`. ഹോസ്റ്റ് ചെയ്ത ഏജന്റ് വിന്യാസത്തിനായി **Foundry Project Manager** റോളും ആവശ്യമാണ്.

ഈ ഉദാഹരണത്തിന്റെ പ്രവർത്തനശേഷിയുള്ള പതിപ്പ് [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) -ൽ ലഭ്യമാണ്. പൂർണ്ണ ഘട്ടങ്ങൾക്കായി (Invocations പ്രോട്ടോക്കോൾ, കസ്റ്റം അഭ്യർത്ഥന സ്കീമകൾ, പ്രശ്നപരിഹാരങ്ങൾ) കാണുക [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## കോഡ് സാമ്പിളുകൾ

Microsoft Agent Framework-അധികം കോഡ് സാമ്പിളുകൾ ഈ റിപ്പോസിറ്ററിയിൽ `xx-python-agent-framework`യും `xx-dotnet-agent-framework` ഫയലുകളിലുമുണ്ട്.

## Microsoft Agent Framework-നെക്കുറിച്ച് കൂടുതൽ ചോദ്യങ്ങൾ ഉണ്ടോ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) -യിൽ മറ്റ് പഠനക്കാരുമായി കാണുക, ഓഫീസ്സ് മണിക്കൂറുകളിൽ പങ്കെടുക്കുക, നിങ്ങളുടെ AI ഏജന്റ് ചോദ്യങ്ങൾക്ക് ഉത്തരങ്ങൾ നേടുക.
## മുൻപ് പാഠം

[Memory for AI Agents](../13-agent-memory/README.md)

## അടുത്ത പാഠം

[Building Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->