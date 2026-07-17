# മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് എക്സ്പ്ലോർ ചെയ്‌തൽ

![Agent Framework](../../../translated_images/ml/lesson-14-thumbnail.90df0065b9d234ee.webp)

### പരിചയം

ഈ പാഠത്തിൽ ഉൾപ്പെടുന്നത്:

- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക്: പ്രധാന സവിശേഷതകളും മൂല്യവും മനസ്സിലാക്കൽ  
- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് முக்கிய ആശയങ്ങൾ പഠിക്കുക
- മേന്മയുള്ള MAF പാറ്റേണുകൾ: വർക്ക്ഫ്ലോകൾ, മിഡിൽവെയർ, മെമ്മറി

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാക്കിയശേഷം, നിങ്ങൾക്ക് അറിയാൻ കഴിയും:

- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് പ്രൊഡക്ഷൻ റെഡി AI ഏജന്റുകൾ നിർമ്മിക്കുക
- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ കോർ സവിശേഷതകൾ നിങ്ങളുടെ ഏജന്റിക് ഉപയോക്തൃ കേസുകളിൽ ബാധകമാക്കുക
- വർക്ക്ഫ്ലോകൾ, മിഡിൽവെയർ, ഓബ്സർവബിലിറ്റി ഉൾപ്പെടെ മുൻപരിചയ പാറ്റേണുകൾ ഉപയോഗിക്കുക

## കോഡ് സാമ്പിളുകൾ 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) ന്റെ കോഡ് സാമ്പിളുകൾ ഈ റിപ്പോസിറ്ററിയിൽ `xx-python-agent-framework` എന്നും `xx-dotnet-agent-framework` എന്നും ഉള്ള ഫയലുകളിൽ കാണാം.

## മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് മനസ്സിലാക്കുക

![Framework Intro](../../../translated_images/ml/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) മൈക്രോസോഫ്റ്റിന്റെ ഏകീകൃത AI ഏജന്റ് കെട്ടിടเฟ്രയിം‌വർക്ക് ആണ്. ഇത് പ്രൊഡക്ഷനും ഗവേഷണപരമായ ചുറ്റുപാടുകളിലും കാണപ്പെടുന്ന വിവിധ ഏജന്റിക് ഉപയോഗകേസുകൾ പരിഹരിക്കാൻ ലോചിപ്പിക്കുന്ന അനേകം സവിശേഷതകൾ നൽകുന്നു:

- **സീരിയൽ ഏജന്റ് ഓർക്കസ്ട്രേഷൻ** സ്റ്റെപ്പ്-ബൈ-സ്റ്റെപ്പ് വർക്ക്ഫ്ലോകളുടെ ആവശ്യമുള്ള സാഹചര്യങ്ങളിൽ.
- **സമകാലീന ഓർക്കസ്ട്രേഷൻ** ഏജന്റുകൾ ഒരേ സമയം multiple ഉപാധികാരങ്ങൾ പൂർത്തിയാക്കേണ്ടവിധം.
- **ഗ്രൂപ്പ് ചാറ്റ് ഓർക്കസ്ട്രേഷൻ** ഏജന്റുകൾ ഒരുമിച്ച് ഒരേ ടാസ്‌ക്കിൽ സഹകരിക്കുന്ന സാഹചര്യങ്ങളിൽ.
- **ഹാൻഡ്‌ഓഫ് ഓർക്കസ്ട്രേഷൻ** ഉപടാസ്‌ക്കുകൾ പൂർത്തിയാകുമ്പോൾ ഏജന്റുകൾ പരസ്പരം ടാസ്‌ക്കുകൾ കൈമാറുന്ന സ്ഥിതികളിൽ.
- **മാഗ്നറ്റിക് ഓർക്കസ്ട്രേഷൻ** ഒരു മാനേജർ ഏജന്റ് ടാസ്‌ക്ക് ലിസ്റ്റ് സൃഷ്ടിക്കുകയും അതിൽ മാറ്റം വരുത്തുകയും പടിസ്ഥാപിച്ച ഏജന്റുകളെ ഏകോപിപ്പിക്കാൻ കൈകാര്യം ചെയ്യുകയും ചെയ്യുന്ന സാഹചര്യങ്ങളിൽ.

പ്രൊഡക്ഷനിൽ AI ഏജന്റുകൾ നൽകുന്നതിന്, MAF താഴെപ്പറയുന്ന സവിശേഷതകളും ഉൾപ്പെടുത്തിയിട്ടുണ്ട്:

- **ഓബ്സർവബിലിറ്റി** OpenTelemetry ഉപയോഗിച്ച്, ഏജന്റിന്റെ എല്ലാ പ്രവർത്തനങ്ങളും ഉൾപ്പെടെ ടൂൾ വിളிப்பு, ഓർക്കസ്ട്രേഷൻ ഘട്ടങ്ങൾ, റീസണിംഗ് ഫ്ലോസ്, മൈക്രോസോഫ്റ്റ് ഫൗണ്ട്രി ഡാഷ്‌ബോർഡ് വഴി പ്രകടന നിരീക്ഷണം.
- **സെക്യൂരിറ്റി** മൈക്രോസോഫ്റ്റ് ഫൗണ്ട്രിയിൽ ഏജന്റുകൾ സ്വദേശമായി ഹോസ്റ്റ് ചെയ്യുന്നു, റോള്ബേസ് ആക്സസ്, സ്വകാര്യ ഡാറ്റ കൈകാര്യം, ബിൽറ്റ്-ഇൻ ഉള്ളടക്ക സുരക്ഷ പോലുള്ള നിയന്ത്രണങ്ങൾ ഉൾപ്പെടുന്നു.
- **ദൈർഘ്യമുള്ള പ്രവർത്തനം** ഏജന്റ് ത്രെഡ്‌സും വർക്ക്ഫ്ലോകളും പPauseച്, പുനരാരംഭിച്ച് പിഴവുകളിൽ നിന്ന് വീണ്ടെടുക്കാൻ കഴിയുന്നു, ഇത് ദീർഘകാല പ്രവർത്തനങ്ങൾ സായൂജ്യം ആക്കുന്നു.
- **നിയന്ത്രണം** മനുഷ്യ സ്ഥലം വർക്ക്ഫ്ലോകൾ പിന്തുണയ്ക്കുന്നു, ടാസ്‌ക്കുകൾ മനുഷ്യ അംഗീകാര താത്പര്യം കാണിക്കുന്നു.

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് ഇന്റർഓപ്പറബിളിറ്റിയിലും കേന്ദ്രീകൃതമാണ്:

- **ക്ലൗഡ്-അഗ്നോസ്റ്റിക്** - ഏജന്റുകൾ കണ്ടെയ്‌നറുകളിൽ, ഓൺ-പ്രീം, പല ക്ലൗഡുകളിലുമാണ് ഓടാൻ കഴിയും.
- **പ്രൊവൈഡർ-അഗ്നോസ്റ്റിക്** - ഏജന്റുകൾ നിങ്ങളുടെ ഇഷ്ടമുള്ള SDK ഉപയോഗിച്ച് സൃഷ്ടിക്കാം, Azure OpenAI, OpenAI ഉൾപ്പെടെ.
- **ഒപ്പൺ സ്റ്റാൻഡേർഡുകൾ ഇന്റഗ്രേറ്റ് ചെയ്യുന്നു** - Agent-to-Agent (A2A)വും Model Context Protocol (MCP)യും പോലുള്ള പ്രോട്ടോക്കോളുകൾ മറ്റു ഏജന്റുകൾക്കും ടൂളുകൾക്കും കണ്ടെത്തി ഉപയോഗിക്കാൻ.
- **പ്ലഗിൻസും കണക്റ്ററുകളും** - മൈക്രോസോഫ്റ്റ് ഫാബ്രിക്, ഷെയർപോയിന്റ്, പൈൻകോൺ, Qdrant പോലുള്ള ഡാറ്റയും മെമ്മറി സേവനങ്ങളുമായുള്ള കണക്ഷനുകൾ.

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ ചില കോർ ആശയങ്ങളിലേക്കായി ഈ സവിശേഷതകൾ എങ്ങനെ ബാധകമാകുന്നു എന്ന് നോക്കാം.

## മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ പ്രധാന ആശയങ്ങൾ

### ഏജന്റുകൾ

![Agent Framework](../../../translated_images/ml/agent-components.410a06daf87b4fef.webp)

**ഏജന്റുകൾ സൃഷ്ടിക്കൽ**

ഏജന്റ് സൃഷ്ടിക്കൽ inference service (LLM Provider), ഏജന്റ് പിന്തുടരേണ്ട നിബന്ധനകൾ, `name` എന്ന ഫോം നിർവചിക്കുന്നത് വഴി നടത്തുന്നു:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

മുകളിൽ `Azure OpenAI` ആണ് ഉപയോഗിച്ചിരിക്കുന്നത്, പക്ഷേ `Microsoft Foundry Agent Service` പോലുള്ള പല സേവനങ്ങളും ഉപയോഗിച്ച് ഏജന്റുകൾ സൃഷ്ടിക്കാം:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API കളും

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

അല്ലെങ്കിൽ [MiniMax](https://platform.minimaxi.com/), OpenAI-സാദൃശ്യ API വലുത് കോൺടെക്സ്‌റ്റ് വിൻഡോകളുമായി (ആകെ 204K ടോക്കൺ വരെ):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

അല്ലെങ്കിൽ A2A പ്രോട്ടോക്കോൾ ഉപയോഗിച്ച് റിമോട്ട് ഏജന്റുകൾ:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ഏജന്റുകൾ പ്രവർത്തിപ്പിക്കൽ**

.run അല്ലെങ്കിൽ .run_stream മെത്തഡുകൾ വഴി ഏജന്റുകൾ ഓടുന്നു; non-streaming അല്ലെങ്കിൽ streaming പ്രതികരണങ്ങൾക്ക്.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ഓരോ ഏജന്റ് പ്രവർത്തനത്തിനും `max_tokens`, `tools` (ഏജൻറ് വിളിക്കാവുന്ന ടൂളുകൾ), `model` എന്നിവയുടെയുള്ള പാരാമീറ്ററുകൾ കസ്റ്റമൈസ് ചെയ്യുന്നതിനുള്ള ഓപ്ഷനുകൾ ഉണ്ട്.

ക്ലയന്റിൻറെ ടാസ്‌ക്ക് പൂർത്തിയാക്കുന്നതിന് പ്രത്യേക മോഡലുകൾ അല്ലെങ്കിൽ ടൂളുകൾ ആവശ്യമായ അവസരങ്ങളിൽ ഇത് സഹായകമാണ്.

**ടൂളുകൾ**

ഏജന്റ് നിർവചിക്കുന്നപ്പോൾ ടൂളുകൾ നിർവചിക്കാം:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ഒരു ChatAgent നേരിട്ട് സൃഷ്ടിക്കുമ്പോള്‍

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

കൂടാതെ ഏജന്റ് ഓടുമ്പോഴും ടൂളുകൾ ഉൾപ്പെടുത്താം:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ഈ റൺക്ക് മാത്രമുള്ള ഉപകരണം )
```

**ഏജന്റ് ത്രെഡുകൾ**

ബഹുസ്റ്റെപ്പ് സംസാരങ്ങൾ കൈകാര്യം ചെയ്യാൻ ഏജന്റ് ത്രെഡുകൾ ഉപയോഗിക്കുന്നു. ത്രെഡുകൾ നന്നായി സേവ് ചെയ്യപ്പെടാൻ `get_new_thread()` ഉപയോഗിക്കാം അല്ലെങ്കിൽ ഏജന്റ് ഓടുമ്പോൾ ഓട്ടോമാറ്റിക്കായി സൃഷ്ടിക്കാം.

- `get_new_thread()` ഉപയോഗിച്ച് ത്രെഡ് സേവ് ചെയ്യാവുന്നതായിത്തീരും
- ഏജന്റ് ഓടുമ്പോൾ ത്രെഡ് സൃഷ്ടിച്ച് ആ പ്രവർത്തനത്തിനുള്ളിൽ മാത്രമായിരിക്കും ത്രെഡിന്റെ കാലാവധി.

ത്രെഡ് സൃഷ്ടിക്കാൻ കോഡ്:

```python
# ഒരു പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() # ത്രെഡിലുമായി ഏജന്റ് പ്രവർത്തിപ്പിക്കുക.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

പിന്നീട് ത്രെഡ് സീരിയലൈസ് ചെയ്ത് പിന്നീട് ഉപയോഗത്തിനായി സേവ് ചെയ്യാം:

```python
# ഒരു പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() 

# ആജന്റിനെ ത്രെഡോടെ പ്രവർത്തിപ്പിക്കുക.

response = await agent.run("Hello, how are you?", thread=thread) 

# സംഭരണത്തിനായി ത്രെഡ് സീരിയലൈസ് ചെയ്യുക.

serialized_thread = await thread.serialize() 

# സംഭരണത്തിൽ നിന്ന് ലോഡ് ചെയ്തശേഷം ത്രെഡ് നില ഡീസീരിയലൈസ് ചെയ്യുക.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ഏജന്റ് മിഡിൽവെയർ**

ഉപയോക്താവിന്റെ ടാസ്‌ക്കുകൾ പൂർത്തിയാക്കാൻ ഏജന്റുകൾ ടൂളുകളുമായി, LLMs-ഉം ഇടപഴകുന്നു. ചില സാഹചര്യങ്ങളിൽ ഈ ഇടപഴകൽ ഇടയിൽ ചില പ്രവർത്തനങ്ങൾ എക്സിക്യൂട്ട് ചെയ്യേണ്ടതിനായി ഏജന്റ് മിഡിൽവെയർ സഹായിക്കുന്നു:

*ഫങ്ഷൻ മിഡിൽവെയർ*

ഏജന്റും ഫങ്ഷൻ/ടൂൾ കോളും തമ്മിലുള്ള ഇടയിൽ ഒരു പ്രവർത്തനം ചെയ്യാൻ സാധിക്കും. ഉദാഹരണത്തിന് ഫങ്ഷൻ കോളിൽ ലോഗിംഗ്.

താഴെയുള്ള കോഡിൽ `next` അടുത്ത മിഡിൽവെയർക്കും ഫങ്ഷനും എഥ് വിളിക്കണമെന്നതിനെ നിർവചിക്കുന്നു.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # മുൻ-പ്രോസസ്സ്: ഫംഗ്ഷൻ നടത്തിപ്പ് മുൻപ് ലോഗ് ചെയ്യുക
    print(f"[Function] Calling {context.function.name}")

    # അടുത്ത മിഡിൽവെയർ അല്ലെങ്കിൽ ഫംഗ്ഷൻ നടത്തിപ്പിലേക്ക് തുടരുക
    await next(context)

    # പിയിൽ-പ്രോസസ്സ്: ഫംഗ്ഷൻ നടത്തിപ്പ് കഴിഞ്ഞ് ലോഗ് ചെയ്യുക
    print(f"[Function] {context.function.name} completed")
```

*ചാറ്റ് മിഡിൽവെയർ*

ഏജന്റും LLM-ഉം തമ്മിലുള്ള അഭ്യർത്ഥനകളിൽ ഇടയിൽ പ്രവർത്തനങ്ങൾ എക്സിക്യൂട്ട് ചെയ്യുകയോ ലോഗ് ചെയ്യുകയോ ചെയ്യുന്നു.

`messages` പോലുള്ള പ്രധാന വിവരങ്ങൾ ഇത് ഉൾക്കൊള്ളുന്നു.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # മുൻക്രമസംസ്‌ക്കരണം: AI കോളിന് മുമ്പ് ലോഗ് ചെയ്യുക
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # അടുത്ത മിഡിൽവെയർ അല്ലെങ്കിൽ AI സേവനത്തിലേക്ക് തുടരുക
    await next(context)

    # ശേഷസംസ്‌ക്കരണം: AI പ്രതികരണത്തിന് ശേഷം ലോഗ് ചെയ്യുക
    print("[Chat] AI response received")

```

**ഏജന്റ് മെമ്മറി**

`Agentic Memory` പാഠത്തിൽ പറഞ്ഞതുപോലെ, മെമ്മറി ഏജന്റിന് വ്യത്യസ്ത പ്രാസാവിക സാഹചര്യങ്ങളിൽ പ്രവർത്തിക്കാൻ അനുകൂലമാണ്. MAF വിവിധ തരത്തിലുള്ള മെമ്മറികൾ നൽകുന്നു:

*ഇൻ-മെമ്മറി സ്റ്റോറേജ്*

ആപ്ലിക്കേഷൻ റൺടൈം സമയത്ത് ത്രെഡ്സിനുള്ളിൽ സൂക്ഷിക്കുന്ന മെമ്മറി.

```python
# ഒരു പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() # ത്രെഡുമായി ഏജന്റിനെ പ്രവർത്തിപ്പിക്കുക.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*പേഴ്സിസ്റ്റന്റ് മെസേജുകൾ*

വിവിധ സെഷനുകൾക്ക് ഇടയിൽ സംഭാഷണ ചരിത്രം സൂക്ഷിക്കാൻ ഉപയോഗിക്കുന്നു. ഇത് `chat_message_store_factory` ഉപയോഗിച്ച് നിർവചിക്കാം:

```python
from agent_framework import ChatMessageStore

# ഒരു കസ്റ്റം സന്ദേശ സംഭരം സൃഷ്ടിക്കുക
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*ഡൈനോമിക് മെമ്മറി*

ഏജന്റുകൾ ഓടിക്കുന്നതിന് മുമ്പ് ഈ മെമ്മറികൾ കോൺടെക്സ്‌റ്റിലേക്കു ചേർക്കുന്നു. mem0 പോലുള്ള eksternal സേവനങ്ങളിൽ ഇത് സൂക്ഷിക്കാം:

```python
from agent_framework.mem0 import Mem0Provider

# അത്യാധുനിക മെമ്മറി കഴിവുകൾക്ക് Mem0 ഉപയോഗിക്കുന്നു
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

വിശ്വസനീയമായ, പരിപാലിക്കാൻ കഴിഞ്ഞ സിസ്റ്റങ്ങൾ നിർമ്മിക്കാന്‍ ഓബ്സർവബിലിറ്റി ആവശ്യമാണ്. MAF OpenTelemetry ഇന്റഗ്രേറ്റ് ചെയ്ത് ട്രേസിങ്, മീറ്ററുകൾ നൽകുന്നു.

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

### വർക്ക്ഫ്ലോകൾ

MAF വർക്ക്ഫ്ലോകൾ നൽകുന്നു, ഇത് ടാസ്‌ക്ക് പൂർത്തിയാക്കാനുള്ള മുൻകൂട്ടി നിർവചിച്ച ഘട്ടങ്ങളാണ്, AI ഏജന്റുകൾ ഘട്ടങ്ങളുടെ ഘടകങ്ങളായി ഉൾക്കൊള്ളിക്കുന്നു.

വർക്ക്ഫ്ലോകൾ വിവിധ ഘടകങ്ങളാൽ രൂപപ്പെടുത്തിയിരിക്കുന്നു, ഇതിലൂടെ മികച്ച നിയന്ത്രണ പ്രവാഹവും സാധ്യമാണ്. **മൾട്ടി-ഏജന്റ് ഓർക്കസ്ട്രേഷൻ**ക്കും **ചെക്ക്പോയിന്റിംഗ്**ക്കും സൗകര്യം നൽകുന്നു.

വർക്ക്ഫ്ലോയുടെ പ്രധാന ഘടകങ്ങൾ:

**എക്സിക്യുട്ടേഴ്സ്**

എക്സിക്യുട്ടേഴ്സ് ഇൻപുട്ട് മെസേജുകൾ സ്വീകരിക്കുകയും ചുമതലയുള്ള ടാസ്‌ക്കുകൾ നിർവഹിച്ചു ഔട്ട്പുട്ട് മെസേജ് നൽകുകയും ചെയ്യും. ഇത് വർക്ക്ഫ്ലോ മുന്നോട്ട് കൊണ്ടു പോകുന്നു. എക്സിക്യുട്ടറുകൾ AI ഏജന്റ് അല്ലെങ്കിൽ കസ്റ്റം ലൊജിക്ക് ആകാം.

**എഡ്ജുകൾ**

വർക്ക്ഫ്ലോയിൽ മെസേജുകളുടെ പ്രവാഹം നിർവചിക്കാൻ ഉപയോഗിക്കുന്നു. ഇവ:

*ഡയറക്റ്റ് എഡ്ജുകൾ* - എക്സിക്യുട്ടർമാരെ തമ്മിൽ ഒരു-ഓരൊന്നായി ബന്ധിപ്പിക്കുന്നു:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*ഷരതുവരെയുള്ള എഡ്ജുകൾ* - നിർവചിച്ച ഷരതുകൾ പാലിക്കുമ്പോൾ പ്രവർത്തിക്കുന്നു. ഉദാ: ഹോട്ടൽ മുറികൾ ലഭ്യമല്ലെങ്കിൽ എക്സിക്യുട്ടർ മറ്റൊരു ഓപ്ഷൻ നിര്‍ദ്ദേശിക്കും.

*സ്വിച്ച്ച്-കേസ് എഡ്ജുകൾ* - വ്യത്യസ്ത എക്സിക്യുട്ടർമാർക്ക് വ്യത്യസ്ത സന്ദേശങ്ങൾ റൂട്ടു ചെയ്യും. ഉദാ: യാത്രാ ഉപഭോക്താവിന് പ്രയോജനം ലഭ്യമെങ്കിൽ മറ്റൊരു വർക്ക്ഫ്ലോയിലൂടെ ടാസ്‌ക്കുകൾ കൈകാര്യം ചെയ്യും.

*ഫാൻ-ഔട്ട് എഡ്ജുകൾ* - ഒരേ സന്ദേശം പല ലക്ഷ്യങ്ങളിലും അയക്കും.

*ഫാൻ-ഇൻ എഡ്ജുകൾ* - പല എക്സിക്യുട്ടർമാരിൽ നിന്നുള്ള സന്ദേശങ്ങൾ ഒറ്റ ലക്ഷ്യത്തിലേക്ക് കൂട്ടിച്ചേർക്കും.

**ഇവന്റുകൾ**

വർക്ക്ഫ്ലോകളിൽ മികച്ച ഓബ്സർവബിലിറ്റി നൽകാൻ MAF പ്രവർത്തന ഇവന്റുകൾ നൽകുന്നു:

- `WorkflowStartedEvent`  - വർക്ക്ഫ്ലോ ആരംഭിക്കുന്നു
- `WorkflowOutputEvent` - വർക്ക്ഫ്ലോ ഔട്ട്പുട്ട് നൽകുന്നു
- `WorkflowErrorEvent` - വർക്ക്ഫ്ലോ പിഴവ് നേരിടുന്നു
- `ExecutorInvokeEvent`  - എക്സിക്യുട്ടർ പ്രോസസ്സ് തുടങ്ങി
- `ExecutorCompleteEvent`  -  എക്സിക്യുട്ടർ പ്രോസസ്സ് പൂർത്തിയായി
- `RequestInfoEvent` - അഭ്യർത്ഥന പുറത്തിറങ്ങി

## മുൻനിര MAF പാറ്റേണുകൾ

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ പ്രധാന ആശയങ്ങൾ മേൽപ്പറഞ്ഞപ്പോൾ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്. കൂടുതൽ സങ്കീർണ്ണമായ ഏജന്റുകൾ നിർമ്മിക്കുമ്പോൾ പരിഗണിക്കേണ്ട മുന്നേറ്റ പാറ്റേണുകൾ:

- **മിഡിൽവെയർ സംയോജനം**: ഫങ്ഷൻ മിഡിൽവെയറും ചാറ്റ് മിഡിൽവെയറും ഉപയോഗിച്ച് ലോഗിംഗ്, ഓത്തന്റിക്കേഷൻ, റേറ്റ്-ലിമിറ്റിംഗ് മുതലായ മിഡിൽവെയർ ഹാൻഡ്‌ലറുകൾ ചൈൻ ചെയ്‌തുകൊണ്ട് ഏജന്റ് പെരുമാറ്റത്തെ സൂക്ഷ്മമായി നിയന്ത്രിക്കുക.
- **വർക്ക്ഫ്ലോ ചെക്ക്പോയിന്റിംഗ്**: വർക്ക്ഫ്ലോ ഇവന്റുകളും സീരിയലൈസേഷനും ഉപയോഗിച്ച് ദൈർഘ്യമുള്ള ഏജന്റ് പ്രോസസ്സുകൾ സേവ് ചെയ്ത് പുനരാരംഭിക്കുക.
- **ഡൈനാമിക് ടൂൾ തിരഞ്ഞെടുപ്പ്**: ടൂൾ വിവരണങ്ങളിൽ RAG ചേർത്ത് MAF ടൂൾ രജിസ്ട്രേഷൻ ഉപയോഗിച്ച് പ്രസക്തമായ ടൂളുകൾ ചോദ്യംപ്രകാരം മാത്രം പ്രദർശിപ്പിക്കുക.
- **മൾട്ടി-ഏജന്റ് ഹാൻഡ്‌ഓഫ്**: പ്രത്യേകപ്പെട്ട ഏജന്റുകൾ തമ്മിലുള്ള ഹാൻഡ്‌ഓഫ് ഓർക്കസ്ട്രേറ്റ് ചെയ്യുന്നതിന് വർക്ക്ഫ്ലോ എഡ്ജുകളും ഷരത കാരുണ്യ റൂട്ടിംഗും ഉപയോഗിക്കുക.

## ലാംഗ്‌ചെയിൻ / ലാംഗ്‌ഗ്രാഫ് ഏജന്റുകൾ Microsoft Foundry-ൽ ഹോസ്റ്റ് ചെയ്യൽ

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് **ഫ്രെയിംവർക്ക്-ഇന്റർഓപ്പറബിൾ** ആണ് — MAF ഉപയോഗിച്ച് എഴുതാത്ത ഏജന്റുകൾക്കും നിയന്ത്രണമില്ല. നിങ്ങൾക്കു തന്നെയാണ് **LangChain** അല്ലെങ്കിൽ **LangGraph** ഉപയോഗിച്ച് നിർമ്മിച്ച ഏജന്റ് ഉണ്ടെങ്കിൽ, അത് **Microsoft Foundry ഹോസ്റ്റ് ചെയ്ത ഏജന്റായി** ഓടിക്കാം, Foundry റൺടൈം, സെഷനുകൾ, സ്കേലിംഗ്, ഐഡന്റിറ്റി, പ്രോട്ടോക്കോൾ എങ്ക്പോയിന്റുകൾ കൈകാര്യം ചെയ്യുന്നുണ്ട്, നിങ്ങളുടെ ഏജന്റ് ലൊജിക് LangGraph മുതൽ നിലനിൽക്കും.

ഇത് `langchain_azure_ai.agents.hosting` പാക്കേജ് ഉപയോഗിച്ച് സാദ്ധ്യമാക്കുന്നു, ഇത് ഫൗണ്ട്രി ഹോസ്റ്റ് ചെയ്ത ഏജന്റുകൾ ഉപയോഗിക്കുന്ന സമാന പ്രോട്ടോക്കോളുകൾ വഴി ഒരു കമ്പൈൽ ചെയ്ത LangGraph ഗ്രാഫ് പുറത്തു വിടുന്നു.

**1. ഹോസ്റ്റിംഗ് എക്സ്ട്ര ഇൻസ്റ്റാൾ ചെയ്യുക:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` എക്സ്ട്ര സ്വന്തമായി ഫൗണ്ട്രി പ്രോട്ടോക്കോൾ ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യുന്നു: `azure-ai-agentserver-responses` (OpenAI-സാദൃശ്യ `/responses` എങ്ക്പോയിന്റ്) ഉം `azure-ai-agentserver-invocations` (ജനറിക്ക് `/invocations` എങ്ക്പോയിന്റ്).

**2. ഹോസ്റ്റിംഗ് പ്രോട്ടോക്കോൾ തിരഞ്ഞെടുക്കുക:**

| പ്രോട്ടോക്കോൾ | ഹോസ്റ്റ് ക്ലാസ് | എങ്ക്പോയിന്റ് | ഉപയോഗിക്കേണ്ട സ്ഥിതികൾ |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | നിങ്ങള് OpenAI-സാദൃശ്യ ചാറ്റ്, streaming, പ്രതികരണ ചരിത്രം, സംഭാഷണ ത്രെഡിംഗ് ആഗ്രഹിക്കുന്നതായി - സംവാദ ഏജന്റുകൾക്കുള്ള ശിപാർശ ചെയ്ത ഡീഫോൾട്ട്. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | നിങ്ങൾക്ക് കസ്റ്റം JSON രൂപം, വെബ്ഹുക്ക്-സ്റ്റൈൽ എങ്ക്പോയിന്റ് അല്ലെങ്കിൽ നോൺ-സമ്പ്രദായിക പ്രോസസ്സിംഗ് ആവശ്യമാണെങ്കിൽ. |

**Responses API ആണ് ഫൗണ്ട്രിയിൽ ഏജന്റ്-സ്റ്റൈൽ വികസനത്തിന് പ്രധാന API**, കൂടുതലായി ഏജന്റുകൾക്ക് `ResponsesHostServer` ഉപയോഗിച്ച് തുടങ്ങുക.

**3. പരിസരം വേരിയബിളുകൾ കോൺഫിഗർ ചെയ്യുക** (`az login` ആദ്യം ചെയ്യുക, അതുകൊണ്ട് `DefaultAzureCredential` അഥന്റിക്കേറ്റ് ചെയ്യാം):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

ഏജന്റ് പിന്നീട് ഫൗണ്ട്രിയിൽ ഹോസ്റ്റ് ചെയ്ത ഏജന്റായി ഓടുമ്പോൾ, പ്ലാറ്റ്ഫോം `FOUNDRY_PROJECT_ENDPOINT` സ്വയം ഇൻജെക്ട് ചെയ്യും.

**4. Responses പ്രോട്ടോക്കോൾ വഴി LangGraph ഏജന്റ് പുറത്തുവിടുക:**

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

    # ChatOpenAI ഇവിടെ Foundry പ്രോജക്ടിന്റെ OpenAI-ക്രമാനുസൃതമായ (Responses) എന്റ്പോയിന്റിനെ ലക്ഷ്യമിടുന്നു.
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

`python main.py` ഉപയോഗിച്ച് ലോക്കലായി ഓടിക്കുക, ശേഷം `http://localhost:8088/responses` എന്ന URL-ലേക്ക് Responses അഭ്യർത്ഥന അയക്കുക.

**മുഖ്യ പെരുമാറ്റങ്ങൾ:**

- **സംഭാഷണങ്ങൾ**: ക്ലയന്റുകൾ `previous_response_id` അല്ലെങ്കിൽ `conversation` ID പാസ്സിങ് ചെയ്തു സംഭാഷണം തുടരുന്നു. നിങ്ങളുടെ ഗ്രാഫ് LangGraph ചെക്ക്പോയിന്റർ ഉപയോഗിച്ചുണ്ടെങ്കിൽ, ഫൗണ്ട്രി സംഭാഷണ സ്ഥിതിയെ ചെക്ക്പോയിന്റിലേക്ക് കീ ചെയ്യുന്നു (പ്രൊഡക്ഷനിൽ ദൈർഘ്യമുള്ള ചെക്ക്പോയിന്റർ ഉപയോഗിക്കുക; ലോക്കലിൽ `MemorySaver` ശരിക്കും).
- **ഹ്യൂമൺ-ഇൻ-ദി-ലൂപ്പ്**: നിങ്ങളുടെ ഗ്രാഫ് LangGraph `interrupt()` ഉപയോഗിച്ചാൽ, `ResponsesHostServer` പ്രന്തിയിൽ ഉളള ഇടപാടിനെ Responses `function_call` / `mcp_approval_request` ആയി കാണിക്കുന്നു, ക്ലയന്റുകൾ ഈ വിളികളുമായി വീണ്ടും തുടരും.
- **ഫൗണ്ട്രിയിലേക്ക് ഡിപ്പ്ലോയ് ചെയ്യുക**: Azure Developer CLI ഉപയോഗിക്കുക — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ലോക്കലിൽ, Docker ആവശ്യമാണ്), ശേഷം `azd provision` , `azd deploy`. ഹോസ്റ്റ് ചെയ്‌ത ഏജന്റ് ഡിപ്പ്ലോയ്മെന്റ് **Foundry Project Manager** റോളിന് മാത്രമേ സാധിക്കൂ.

ഈ ഉദാഹരണത്തിന്റെ റണ്ണബിൾ പതിപ്പ് [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) ല് ഉണ്ട്. പൂർണ്ണ വാക്ക്‌തുള്ളക്കായി (Invocations പ്രോട്ടോക്കോൾ, കസ്റ്റം അഭ്യർത്ഥന സ്കീമകൾ, പ്രശ്നപരിഹാരം), കാണുക [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## കോഡ് സാമ്പിളുകൾ 

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനുള്ള കോഡ് സാമ്പിളുകൾ ഈ റിപ്പോസിറ്ററിയിൽ `xx-python-agent-framework` എന്നും `xx-dotnet-agent-framework` എന്നും ഉള്ള ഫയലുകളിൽ കാണാം.

## മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനെക്കുറിച്ചും കൂടുതൽ ചോദിക്കാനുള്ളതുണ്ടോ?

[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) യിൽ ചേരുക, മറ്റു പഠനക്കാരെ കാണാനും ഓഫീസ് മണിക്കൂറുകളിൽ പങ്കെടുക്കാനും നിങ്ങളുടെ AI ഏജന്റ് ചോദ്യങ്ങൾക്ക് മറുപടി ലഭിക്കാനും.
## മുൻ പാഠം

[AI ഏജന്റുകൾക്കായുള്ള മെമ്മറി](../13-agent-memory/README.md)

## അടുത്ത പാഠം

[കമ്പ്യൂട്ടർ ഉപയോഗ ഏജന്റുകൾ നിർമ്മിക്കൽ (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->