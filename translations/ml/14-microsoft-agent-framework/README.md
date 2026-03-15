# Microsoft Agent Framework അവലോകനം

![ഏജന്റ് ഫ്രെയിംവർക്ക്](../../../translated_images/ml/lesson-14-thumbnail.90df0065b9d234ee.webp)

### പരിചയം

ഈ പാഠം ഇത് ഉൾക്കൊള്ളും:

- Microsoft Agent Framework: പ്രധാന സവിശേഷതകളും മൂല്യവും തിരിച്ചറിയൽ  
- Microsoft Agent Framework-ന്റെ പ്രധാന ആശയങ്ങൾ അന്വേഷിക്കൽ
- മോർ സങ്കീർണ്ണ MAF മാതൃകകൾ: പ്രവാഹങ്ങൾ, മിഡിൽവെയർ, മെമ്മറി

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാക്കിയാൽ, നിങ്ങൾക്ക് എന്തെല്ലാം അറിയാം എന്നതിൽ:

- Microsoft Agent Framework ഉപയോഗിച്ച് പ്രൊഡക്ഷൻ റെഡി AI ഏജന്റുകൾ നിർമ്മിക്കുക
- നിങ്ങളുടെ ഏജന്റിക് ഉപയോഗ-кേസുകൾക്കായി Microsoft Agent Framework-ന്റെ കോർ സവിശേഷതകൾ ബാധകംമാക്കുക
- പ്രവാഹങ്ങൾ, മിഡിൽവെയർ, ഒബ്സർവബി ലിറ്റി എന്നിവ ഉൾക്കൊള്ളുന്ന അവധിക്ക് മേൽ മാതൃകകൾ ഉപയോഗിക്കുക

## കോഡ് സാമ്പിളുകൾ 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok)-നുള്ള കോഡ് സാമ്പിളുകൾ ഈ റിപോസിറ്ററിയിൽ `xx-python-agent-framework` എന്നതിലും `xx-dotnet-agent-framework` എന്നതിലും ലഭ്യമാണ്.

## Microsoft Agent Framework മനസിലാക്കൽ

![ഫ്രെയിംവർക്ക് പരിചയം](../../../translated_images/ml/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) AI ഏജന്റുകൾ നിർമ്മിക്കാൻ Microsoft's ഏകീകരിച്ച ഫ്രെയിംവർക്കാണ്. പ്രൊഡക്ഷനും ഗവേഷണ സാഹചര്യങ്ങളിലും കാണപ്പെടുന്ന വ്യത്യസ്ത ഏജന്റിക് ഉപയോഗ സംഭവങ്ങൾ കൈകാര്യം ചെയ്യുന്നതിനുള്ള ഭേദഗതകൾ നൽകുന്നു, ഉദാഹരണത്തിന്:

- **ക്രമപരമായ ഏജന്റ് ഓർക്കസ്ട്രേഷൻ** - നടപടിക്രമാനുസൃത പ്രവാഹങ്ങൾ ആവശ്യമുള്ള അനുഭവങ്ങളിൽ.
- **സമകാലീന ഓർക്കസ്ട്രേഷൻ** - ഏജന്റുകൾ ഒരേസമയം ടാസ്‌കുകൾ പൂർത്തിയാക്കേണ്ട സാഹചര്യങ്ങളിൽ.
- **ഗ്രൂപ്പ് ചാറ്റ് ഓർക്കസ്ട്രേഷൻ** - ഒരു ടാസ്‌കിൽ ഏജന്റുകൾ തമ്മിൽ സഹകരിക്കാൻ കഴിയുന്ന സാഹചര്യങ്ങളിൽ.
- **ഹാൻഡോഫ് ഓർക്കസ്ട്രേഷൻ** - ഉപടാസ്‌കുകൾ പൂർത്തിയാകുമ്പോൾ ഏജന്റുകൾ ടാസ്‌ക് പരസ്പരം കൈമാറുന്ന സാഹചര്യങ്ങളിൽ.
- **മാഗ്‌നറ്റിക് ഓർക്കസ്ട്രേഷൻ** - മാനേജർ ഏജന്റ് ടാസ്ക് ലിസ്റ്റ് സൃഷ്ടിക്കുകയും മാറ്റുകയും ചെയ്ത് ഉപഏജന്റുകളുടെ കോഒർഡിനേഷൻ കൈകാര്യം ചെയ്യുന്ന സാഹചര്യങ്ങളിൽ.

പ്രൊഡക്ഷനിൽ AI ഏജന്റുകൾ എത്തിക്കാൻ MAF ഇതിന്റെ ഭാഗമായി താഴെപ്പറയുന്ന സവിശേഷതകളും ഉൾക്കൊള്ളുന്നു:

- **ഒബ്സർവബിലിറ്റി** - OpenTelemetry ഉപയോഗിച്ച്, ടൂൾ ഇൻവൊക്കേഷൻ, ഓർക്കസ്ട്രേഷൻ ഘട്ടങ്ങൾ, റീസണിംഗ് ഫ്ലോകൾ ഉൾപ്പെടെ AI ഏജന്റിൻ്റെ ഓരോ പ്രവർത്തനവും ട്രേസിംഗ്, മീറ്ററുകൾ vasit്ചൂടി ട്രാക്ക് ചെയ്യപ്പെടുകയും Microsoft Foundry ഡാഷ്ബോർഡുകൾ വഴി പ്രകടനം നിരീക്ഷിക്കപ്പെടുകയും ചെയ്യുന്നു.
- **സുരക്ഷ** - ഏജന്റുകൾ Microsoft Foundry-യിൽ നേറ്റീവ് ആയി ഹോസ്റ്റ് ചെയ്യുന്നതിലൂടെ റോൾ-ബേസ്ഡ് ആക്സസ്, സ്വകാര്യ ഡാറ്റ ഹാൻഡ്ലിംഗ്, ബിൽറ്റ്-ഇൻ കണ്ടന്റ് സേഫറ്റി എന്നിവ പോലെുള്ള സുരക്ഷാ നിയന്ത്രണങ്ങൾ ഉൾക്കൊള്ളുന്നു.
- **ദൈര്‍ഘ്യം (Durability)** - ഏജന്റ് ത്രെഡുകളും വേർഫ്ലോകളും സസ്പെൻഡ് ചെയ്യുക, റിസ്യൂം ചെയ്യുക, പിശകുകളിൽനിന്ന് പുനരുദ്ധരിപ്പ് ചെയ്യുക എന്നിവ സാധ്യമാകുന്നതിലൂടെ ദീർഘകാല പ്രോസസ്സുകൾക്ക് പിന്തുണ നൽകി.
- **കൺട്രോൾ** - മനുഷ്യൻ ലൂപ്പിൽ ഉള്ള പ്രവാഹങ്ങൾ പിന്തുണയ്ക്കപ്പെടുന്നു, ടാസ്‌കുകൾ മനുഷ്യ അംഗീകാരമോ അനുമതിയോ ആവശ്യമാണെന്ന് അടയാളപ്പെടുത്താം.

MAF ഇന്ററോപ്പറബിളായിരിക്കാനും ശ്രദ്ധ കേന്ദ്രീകരിച്ചിരിക്കുന്നു:

- **ക്ലൗഡ്-അഗ്നോസ്റ്റിക് ആകൽ** - ഏജന്റുകൾ കണ്ടെയ്‌നറുകളിൽ, ഓൺ-പ്രേം, വിവിധ ക്ലൗഡുകളിൽ ഓടാൻ കഴിയും.
- **പ്രൊവൈഡർ-അഗ്നോസ്റ്റിക് ആകൽ** - ഏജന്റുകൾ നിങ്ങളുടെ പ്രിയപ്പെട്ട SDK ഉപയോഗിച്ച് സൃഷ്ടിക്കാവുന്നതാണ്, ഉദാഹരണത്തിന് Azure OpenAI და OpenAI.
- **ഓപ്പൺ സ്റ്റാൻഡേർഡുകൾ സംയോജിപ്പിക്കൽ** - Agent-to-Agent (A2A) և Model Context Protocol (MCP) പോലുള്ള പ്രോട്ടോക്കോളുകൾ ഉപയോഗിച്ച് മറ്റ് ഏജന്റുകളും ടൂളുകളും കണ്ടെത്തി ഉപയോഗിക്കാവുന്ന രൂപത്തിൽ agents ഉപയോഗിക്കാം.
- **പ്ലഗിനുകളും കണക്ടറുകളും** - Microsoft Fabric, SharePoint, Pinecone, Qdrant പോലുള്ള ഡാറ്റാ-അഥവാ മെമ്മറി സേവനങ്ങളിലേക്ക് കണക്ഷനുകൾ ഉണ്ടാക്കാനാകും.

ഈ സവിശേഷതകൾ Microsoft Agent Framework-ന്റെ ചില കോർ ആശയങ്ങളിൽ എങ്ങനെ പ്രയോഗിക്കപ്പെടുന്നു എന്ന് നോക്കാം.

## Microsoft Agent Framework-ന്റെ പ്രധാന ആശയങ്ങൾ

### ഏജന്റുകൾ

![ഏജന്റ് ഫ്രെയിംവർക്ക്](../../../translated_images/ml/agent-components.410a06daf87b4fef.webp)

**ഏജന്റുകൾ സൃഷ്ടിക്കൽ**

ഏജന്റ് സൃഷ്ടിക്കൽ ചെയ്യുന്നത് ഇൻഫറൻസ് സർവീസ് (LLM Provider), AI ഏജന്റ് പിന്തുടരാനുള്ള നിർദ്ദേശങ്ങളുടെ ഒരു ക്രമം, കൂടാതെ നിർദിഷ്ടമായ `name` നിർവചിക്കൽ എന്നിവ വഴി ആണ്:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

മുകളിൽ `Azure OpenAI` ഉപയോഗിച്ചാണ് കാണിച്ചത്, പക്ഷേ ഏജന്റുകൾ `Microsoft Foundry Agent Service` ഉൾപ്പെടെയുള്ള നിരവധി സേവനങ്ങൾ ഉപയോഗിച്ച് സൃഷ്ടിക്കാനും കഴിയും:

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

അഥവാ A2A പ്രോട്ടോക്കോൾ ഉപയോഗിച്ച് റിമോട്ട് ഏജന്റുകളായും:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ഏജന്റുകൾ റൺ ചെയ്യൽ**

ഏജന്റുകൾ non-streaming അല്ലെങ്കിൽ streaming പ്രതികരണങ്ങൾക്കായി `.run` അല്ലെങ്കിൽ `.run_stream` മെഥഡുകൾ ഉപയോഗിച്ച് പ്രവർത്തിപ്പിക്കുന്നു.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ഓരോ ഏജന്റ് റൺക്കും ഏജന്റ് ഉപയോഗിക്കുന്ന `max_tokens`, ഏജന്റ് കോളു് ചെയ്യാൻ കഴിയുന്ന `tools`, അടങ്ങിയിരിക്കുന്ന `model` എന്നിവർ പോലുള്ള പാരാമീറ്ററുകൾ കസ്റ്റമൈസ് ചെയ്യുന്നതിനുള്ള ഓപ്ഷനുകൾ ഉണ്ടായിരിക്കും.

ഉപയോക്താവിന്റെ ടാസ്‌ക് പൂർത്തീകരിക്കാൻ പ്രത്യേക മോഡലുകളോ ടൂളുകളോ ആവശ്യമായ സാഹചര്യങ്ങളിൽ ഇത് ഉപയോഗപ്രദമാണ്.

**ഉപകരണങ്ങൾ (Tools)**

ഉപകരണങ്ങൾ ഏജന്റ് നിർവചിക്കുമ്പോഴെയും നിർവചിക്കുമ്പോഴും നിർവചിക്കാവുന്നതാണ്:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ChatAgent നേരിട്ട് സൃഷ്ടിക്കുമ്പോൾ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

എന്നും ഏജന്റ് ഓടുമ്പോഴും നിർവചിക്കാവുന്നതാണ്:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ഈ റൺക്കായി മാത്രമാണ് ഉപകരണം നൽകിയിരിക്കുന്നത് )
```

**ഏജന്റ് ത്രെഡുകൾ**

ഏജന്റ് ത്രെഡുകൾ മൾട്ടി-ടേൺ സംഭാഷണങ്ങൾ കൈകാര്യം ചെയ്യാൻ ഉപയോഗിക്കുന്നു. ത്രെഡുകൾ സൃഷ്ടിക്കാൻ രണ്ട് വഴികളുണ്ട്:

- `get_new_thread()` ഉപയോഗിച്ച്, ത്രെഡ് സമയം കഴിഞ്ഞും സേവ് ചെയ്യാൻ കഴിയും
- ഏജന്റ് ഓടിക്കുന്നപ്പോൾ തൻെെനേത്ര ത്രെഡ് ഓട്ടോമാറ്റിക്കായി സൃഷ്ടിക്കപ്പെടുകയും അത് നിലവിലെ റൺ കാലയളവിൽ മാത്രമേ നിലനിർത്തുകയുള്ളൂ.

ത്രെഡ് സൃഷ്ടിക്കാൻ കോഡ് ഇങ്ങനെ കാണപ്പെടും:

```python
# ഒരു പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() # ത്രെഡുമായി ഏജന്റ് ഓടിക്കുക.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

പിന്നീട് ത്രെഡ് സീരിയലൈസ് ചെയ്ത് പിന്നീട് ഉപയോഗിക്കുന്നതിനായി സൂക്ഷിക്കാം:

```python
# ഒരു പുതിയ ത്രീഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() 

# ഏജന്റിനെ ത്രീഡിനൊപ്പം പ്രവർത്തിപ്പിക്കുക.

response = await agent.run("Hello, how are you?", thread=thread) 

# സംരക്ഷണത്തിനായി ത്രീഡ് സീരിയലൈസ് ചെയ്യുക.

serialized_thread = await thread.serialize() 

# സംരക്ഷണത്തിൽ നിന്ന് ലോഡ് ചെയ്തതിനു ശേഷം ത്രീഡിന്റെ നില ഡീസീരിയലൈസ് ചെയ്യുക.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ഏജന്റ് മിഡിൽവെയർ**

ഏജന്റുകൾ ഉപകരണങ്ങളോടും LLM-കളോടും ഇടപെടുന്നു ഉപയോക്താവിന്റെ ടാസ്‌കുകൾ പൂർത്തിയാക്കാൻ. ചില സാഹചര്യങ്ങളിൽ, ഈ ഇടപെടലുകൾക്കിടയിൽ ഒരു പ്രവർത്തനം നടപ്പിലാക്കുകയോ ട്രാക്ക് ചെയ്യുകയോ ചെയ്യേണ്ടി വരും. ഏജന്റ് മിഡിൽവെയർ ഇത് സാധ്യമാക്കുന്നു:

*Function Middleware*

ഈ മിഡിൽവെയർ ഏജന്റ് ഒരു ഫംഗ്ഷൻ/ടൂൾ കോളു ചെയ്യുന്നതിനും മുൻപ് അല്ലെങ്കിൽ പിന്നീട് ഒരു പ്രവർത്തനം നടത്താൻ അനുവദിക്കുന്നു. ഉദാഹരണത്തിന് ഫംഗ്ഷൻ കോൾ ലോഗ് ചെയ്യേണ്ടതുണ്ടെങ്കിൽ ഇത് ഉപയോഗിക്കാം.

താഴെയുള്ള കോഡിൽ `next` അർത്ഥം അടുത്ത മിഡിൽവെയർ അല്ലെങ്കിൽ യഥാർത്ഥ ഫംഗ്ഷൻ വിളിക്കേണ്ടതുണ്ടോ എന്നതിനെ നിർവചിക്കുന്നു.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # മുൻപ്രോസസ്സിംഗ്: ഫംഗ്ഷൻ നടത്തുന്നതിന് മുമ്പ് ലോഗ്
    print(f"[Function] Calling {context.function.name}")

    # അടുത്ത മിഡിൽവെയറിലേക്കോ ഫംഗ്ഷൻ നിർവഹണത്തിലേക്കോ തുടരുക
    await next(context)

    # പോസ്റ്റ്-പ്രോസസ്സിംഗ്: ഫംഗ്ഷൻ നടത്തിച്ചതിന് ശേഷം ലോഗ്
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

ഈ മിഡിൽവെയർ ഏജന്റും LLM-നും ഇടയിൽ നടക്കുന്ന അഭ്യർത്ഥനകളിൽ ഇടപെടൽ നടത്തുകയോ ലോഗ് ചെയ്യുകയോ ചെയ്യാൻ അനുവദിക്കുന്നു.

ഇതിൽ AI സർവീസിലേക്ക് അയക്കപ്പെടുന്ന `messages` പോലുള്ള_mahatva വസ്തുക്കൾ ഉൾപ്പെടുന്നു.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # മുൻ-പ്രോസസ്സിംഗ്: AI വിളിക്കുന്നതിന് മുമ്പ് ലോഗ്
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # അടുത്ത മിഡിൽവെയറിലേയ്ക്കോ AI സേവനത്തിലേയ്ക്കോ തുടരുക
    await next(context)

    # പോസ്റ്റ്-പ്രോസസ്സിംഗ്: AI പ്രതികരണത്തിന് ശേഷം ലോഗ്
    print("[Chat] AI response received")

```

**ഏജന്റ് മെമ്മറി**

`Agentic Memory` പാഠത്തിൽ ചർച്ചചെയ്തതുപോലെ, വ്യത്യസ്ത കോൺടെക്സ്റ്റുകളിലായി ഏജന്റ് പ്രവർത്തിക്കാൻ മെമ്മറി ഒരു പ്രധാന ഘടകമാണ്. MAF വിവിധ തരം മെമ്മറികൾ ഓഫർ ചെയ്യുന്നു:

*In-Memory Storage*

ആപ്ലിക്കേഷൻ റൺടൈമിൽ ത്രെഡുകളിൽ സൂക്ഷിച്ചിരിക്കുന്ന മെമ്മറിയാണ് ഇത്.

```python
# ഒരു പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() # ത്രെഡിനൊപ്പം ഏജന്റ് പ്രവർത്തിപ്പിക്കുക.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

വിവിധ സെഷനുകൾക്കിടയിലെ സംഭാഷണ ചരിത്രം സേവ് ചെയ്യുന്നതിനുള്ള മെമ്മറിയാണ് ഇത്. അത് `chat_message_store_factory` ഉപയോഗിച്ച് നിർവ്വചിക്കപ്പെടുന്നു:

```python
from agent_framework import ChatMessageStore

# ഒരു ഇഷ്‌ടാനുസൃത സന്ദേശ സംഭരണം സൃഷ്‌ടിക്കുക
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamic Memory*

ഏജന്റുകൾ ഓടുന്നതിന് മുൻപ് കോൺടെക്സ്റ്റിൽ ചേർക്കുന്ന മെമ്മറിയാണ് ഇത്. ഈ മെമ്മറികൾ mem0 പോലുള്ള ബാഹ്യ സേവനങ്ങളിൽ സൂക്ഷിക്കാവുന്നതാണ്:

```python
from agent_framework.mem0 import Mem0Provider

# ഉന്നത മെമ്മറി കഴിവുകൾക്കായി Mem0 ഉപയോഗിക്കുന്നു
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

**ഏജന്റ് ഒബ്സർവബിലിറ്റി**

ഒബ്സർവബിലിറ്റി വിശ്വസനീയവും പരിപാലനയോഗ്യവുമായ ഏജന്റിക് സിസ്റ്റങ്ങൾ നിർമ്മിക്കാൻ അത്യാവശ്യമാണ്. MAF സ്ട്രേസിംഗ്, മീറ്ററുകൾ എന്നിവയ്ക്കായി OpenTelemetry-നുമായി ഇന്റഗ്രേറ്റ് ചെയ്യുന്നു.

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

### പ്രവാഹങ്ങൾ (Workflows)

MAF ടാസ്ക് പൂർത്തിയാക്കുന്നതിനുള്ള മുൻകരുതൽ ഘട്ടങ്ങളായ പ്രവാഹങ്ങൾ നൽകുന്നു, ഇവയിൽ AI ഏജന്റുകൾ ഘടകങ്ങളായിരിക്കും.

പ്രവാഹങ്ങൾ വിവിധ ഘടകങ്ങളാൽ നിർമ്മിതമാണ്, ഇതോടെ മികച്ച നിയന്ത്രണമാർഗ്ഗം ലഭിക്കുന്നു. പ്രവാഹങ്ങൾ **ബഹുഎജന്റ് ഓർക്കസ്ട്രേഷൻ**ക്കും **ചെക്ക്പോയിന്റിംഗ്**ക്കും പിന്തുണ നൽകുന്നു, അത് workflow സ്റ്റേറ്റുകൾ സേവ് ചെയ്യാൻ സാധ്യമാക്കുന്നു.

ഒരു പ്രവാഹത്തിന്റെ കോർ ഘടകങ്ങൾ:

**എക്സിക്യൂട്ടറുകൾ (Executors)**

എക്സിക്യൂട്ടറുകൾ ഇൻപുട്ട് സന്ദേശങ്ങൾ സ്വീകരിച്ച് അവയ്ക്ക് നിയോഗിച്ച ഉപയോഗങ്ങൾ നിർവഹിച്ച് ഔട്ട്‌പുട്ട് സന്ദേശം നിർമ്മിക്കും. ഇതോടെ വലിയ ടാസ്‌ക് പൂർത്തീകരണത്തിലേക്കായി പ്രവാഹം മുന്നേറുന്നു. എക്സിക്യൂട്ടറുകൾ AI ഏജന്റോ കസ്റ്റം ലജിക്കോ ആയിരിക്കാം.

**എഡ്ജുകൾ (Edges)**

എഡ്ജുകൾ പ്രവാഹത്തിൽ സന്ദേശങ്ങളുടെ ഫ്ലോകൾ നിർവചിക്കാൻ ഉപയോഗിക്കുന്നു. ഇവയെല്ലാം ഇപ്രകാരം ആയിരിക്കാം:

*Direct Edges* - എക്സിക്യൂട്ടറുകൾക്കിടയിലെ ലളിതമായ ഒരേ-റ്റു-ഒരേ ബന്ധങ്ങൾ:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - നിശ്ചിത ശരത്പൂർണം ആയതിനു ശേഷം പ്രവർത്തിക്കുന്നവ. ഉദാഹരണത്തിന്, ഹോട്ടൽ മുറികൾ ലഭ്യമല്ലെങ്കിൽ, ഒരു എക്സിക്യൂട്ടർ മറ്റു ഓപ്ഷനുകൾ നിർദ്ദേശിക്കാം.

*Switch-case Edges* - നിർവചിച്ച നിബന്ധനകളുടെ അടിസ്ഥാനത്തിൽ സന്ദേശങ്ങളെ വ്യത്യസ്ത എക്സിക്യൂട്ടറുകളിലേക്ക് റൂട്ടുചെയ്യുക. ഉദാഹരണത്തിന്, യാത്രാക്കാർക്ക് പ്രാധാന്യ ആക്സസ് ഉണ്ടെങ്കിൽ അവരുടെ ടാസ്‌കുകൾ വേറെ പ്രവാഹത്തിലൂടെ കൈകാര്യം ചെയ്യപ്പെടാം.

*Fan-out Edges* - ഒരേ സന്ദേശം പല ലക്ഷ്യങ്ങളിലേക്കും അയയ്‌ക്കുക.

*Fan-in Edges* - വ്യത്യസ്ത എക്സിക്യൂട്ടറുകളിൽ നിന്നുള്ള നിരവധി സന്ദേശങ്ങൾ ശേഖരിച്ച് ഒരേ ലക്ഷ്യത്തിലേക്ക് അയയ്‌ക്കുക.

**ഇവന്റുകൾ**

പ്രവാഹങ്ങളിലേക്ക് നല്ലതായ ഒബ്സർവബിലിറ്റി നൽകാൻ, MAF നടപ്പാക്കലിനുള്ള ബിൽറ്റ്-ഇൻ ഇവന്റുകൾ സാധ്യമായി നൽകുന്നു, ഉദാഹരണങ്ങൾ:

- `WorkflowStartedEvent`  - Workflow നിർവഹണം ആരംഭിക്കുന്നു
- `WorkflowOutputEvent` - Workflow ഒരു ഔട്ട്‌പുട്ട് ഉൽപാദനമാക്കി
- `WorkflowErrorEvent` - Workflow ഒരു പിശക് നേരിടുന്നു
- `ExecutorInvokeEvent`  - എക്സിക്യൂട്ടർ പ്രവർത്തനം ആരംഭിക്കുന്നു
- `ExecutorCompleteEvent`  -  എക്സിക്യൂട്ടർ പ്രവർത്തനം പൂര്‍ത്തിയാക്കി
- `RequestInfoEvent` - ഒരു അഭ്യർത്ഥന ഇറക്കപ്പെട്ടു

## മികച്ച MAF മാതൃകകൾ (Advanced MAF Patterns)

മുകളിലുള്ള വിഭാഗങ്ങൾ Microsoft Agent Framework-ന്റെ പ്രധാന ആശയങ്ങൾ ഉൾക്കൊള്ളുന്നു. നിങ്ങൾ കൂടുതൽ സങ്കീർണ്ണമായ ഏജന്റുകൾ നിർമ്മിക്കുമ്പോൾ പരിഗണിക്കാനുള്ള ചില ആഡ്‌വാൻസ്ഡ് മാതൃകകൾ ഇവയാണ്:

- **മിഡിൽവെയർ സംയോജനം**: ഫംഗ്ഷൻ മിഡിൽവെയറും ചാറ്റ് മിഡിൽവെയറും ഉപയോഗിച്ച് ലോഗ്ഗിംഗ്, ഓത്ഥ്, റേറ്റ്-ലിമിറ്റിംഗ് എന്നിവയുമായി മൾട്ടിപ്പിൾ മിഡിൽവെയർ ഹാൻഡ്‌ലേഴ്സ് സഖീകരിക്കുക എങ്കിൽ ഏജന്റ് പെരുമാറ്റത്തിൽ സൂക്ഷ്മ നിയന്ത്രണം ലഭിക്കും.
- **പ്രവാഹ ചെക്ക്പോയിന്റിംഗ്**: workflow ഇവന്റുകളും സീരിയലൈസേഷനും ഉപയോഗിച്ച് ദീർഘകാല ഏജന്റ് പ്രോസസുകൾ സംരക്ഷിക്കുകയും പുനരാരംഭിക്കുകയും ചെയ്യുക.
- **ഡൈനാമിക് ടൂൾ തിരഞ്ഞെടുപ്പ്**: ടൂൾ വിവരണങ്ങളുടെ മേൽ RAG സംയോജിപ്പിച്ച് MAF-യുടെ ടൂൾ രജിസ്ട്രേഷൻ ഉപയോഗിച്ച് ഓരോ ക്വെറിയിലും പ്രസക്തമായ ടൂളുകൾ മാത്രം അവതരിപ്പിക്കുക.
- **ബഹുഎജന്റ് ഹാൻഡോഫ്**: സ്പെഷ്യലൈസ്ഡ് ഏജന്റുകൾ തമ്മിലുള്ള ഹാൻഡോഫ് ഓർക്കസ്ട്രേറ്റ് ചെയ്യാൻ workflow എഡ്ജുകളും കൺഡീഷണൽ റൂട്ടിംഗും ഉപയോഗിക്കുക.

## കോഡ് സാമ്പിളുകൾ 

Microsoft Agent Framework-നുള്ള കോഡ് സാമ്പിളുകൾ ഈ റിപോസിറ്ററിയിൽ `xx-python-agent-framework` എന്നതിലും `xx-dotnet-agent-framework` എന്നതിലും ലഭ്യമാണ്.

## Microsoft Agent Framework-നെക്കുറിച്ച് കൂടുതൽ ചോദ്യങ്ങളുണ്ടോ?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) ചേർന്നു മറ്റു learners-നെ കാണൂ, office hours-കളിലേയ്ക്ക് ഹാജരാവൂ, നിങ്ങളുടെ AI ഏജന്റുകൾക്ക് അനുബന്ധമായ ചോദ്യങ്ങൾക്ക് ഉത്തരങ്ങൾ നേടൂ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
ഡിസ്ക്ലെയിമർ:
ഈ രേഖ AI പരിഭാഷാ സേവനം Co-op Translator (https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷ ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, ഓട്ടോമേറ്റഡ് (സ്വയംചാലിത) പരിഭാഷകളിൽ പിശകുകൾ അല്ലെങ്കിൽ തിപ്പുകൾ ഉണ്ടായിരിക്കാമെന്ന点 ദയവായി ശ്രദ്ധിക്കുക. മൂല രേഖ അതിന്റെ മാതൃഭാഷയിൽ ഉള്ളതു തന്നെ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശിപാർശ ചെയ്യപ്പെടുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ചതിനാൽ ഉണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റുവ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദിത്തം വഹിക്കില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->