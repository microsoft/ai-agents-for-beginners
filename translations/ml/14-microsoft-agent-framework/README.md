# മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനെ പറ്റി അന്വേഷിക്കൽ

![Agent Framework](../../../translated_images/ml/lesson-14-thumbnail.90df0065b9d234ee.webp)

### പരിചയം

ഈ പാഠംപുസ്തകത്തിൽ ഉൾപ്പെടുന്നത്:

- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക്: പ്രധാന പ്രത്യേകതകളും മൂല്യവും മനസ്സിലാക്കൽ  
- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ കീ ആശയങ്ങൾ അന്വേഷിക്കൽ
- അഡ്വാൻസ്ഡ് MAF മാതൃകകൾ: വേർക്ക്‌ഫ്ലോസ്, മിഡിൽവെയർ, മെമ്മറി

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠംപുസ്തകം പൂർത്തിയാക്കിയ ശേഷം, നിങ്ങളക്ക് അറിയാവുന്നത്:

- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് ഉപയോഗിച്ച് പ്രൊഡക്ഷൻ റെഡിയായി എഐ ഏജന്റുകൾ നിർമ്മിക്കാൻ
- മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ പ്രധാന സവിശേഷതകൾ നിങ്ങളുടെ ഏജന്റിക് ഉപയോഗ കേസുകളിൽ പ്രയോഗിക്കാൻ
- വേർക്ക്‌ഫ്ലോസ്, മിഡിൽവെയർ, ഓബ്സർവബിലിറ്റി ഉൾപ്പെടുന്ന അഡ്വാൻസ്ഡ് മാതൃകകൾ ഉപയോഗിക്കാൻ

## കോഡ് സാമ്പിൾസ് 

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) ന്റെ കോഡ് സാമ്പിളുകൾ ഈ റിപ്പോസിറ്ററിയിൽ `xx-python-agent-framework` മയും `xx-dotnet-agent-framework` ഫയലുകളിലും കാണാം.

## മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനെ മനസ്സിലാക്കുക

![Framework Intro](../../../translated_images/ml/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) മൈക്രോസോഫ്റ്റിന്റെ ഐക്യരൂപത്തിലുള്ള എഐ ഏജന്റുകൾ നിർമ്മിക്കുന്ന ഫ്രെയിംവർക്കാണ്. ഇത് പ്രൊഡക്ഷനും ഗവേഷണ പരിസ്ഥിതികളിലും കാണപ്പെടുന്ന വ്യത്യസ്ത റൈനോ ത്തിലെ ഏജന്റിക് ഉപയോഗ കേസുകൾ കൈകാര്യം ചെയ്യാനുള്ള സൗകര്യം നൽകുന്നു, അവയിൽ:

- **ക്രമപ്പെടുത്തിയ ഏജന്റ് ഓർക്കസ്ട്രേഷൻ** വീണുമുറ്റตรിപ്പ് വേർക്ക്‌ഫ്ലോസ് ആവശ്യമായ സാഹചര്യങ്ങളിൽ.
- **ഒഴുകുന്നു ഓർക്കസ്ട്രേഷൻ** ഏജന്റുകൾ ഒരേ സമയം ജോലി പൂർത്തിയാക്കേണ്ട സാഹചര്യങ്ങളിൽ.
- **ഗ്രൂപ്പ് ചാറ്റ് ഓർക്കസ്ട്രേഷൻ** ഏജന്റുകൾ ഒരുമിച്ച് ഒരു ജോലി ചെയ്യണം എന്ന സാഹചര്യങ്ങളിലും.
- **ഹാൻഡോഫ് ഓർക്കസ്ട്രേഷൻ** സബ്ടാസ്കുകൾ പൂർത്തിയാകുമ്പോൾ ഏജന്റുകൾ തമ്മിൽ ജോലി കൈമാറേണ്ട സാഹചര്യങ്ങളിൽ.
- **മെഗ്നറ്റിക് ഓർക്കസ്ട്രേഷൻ** ഒരു മേധാവി ഏജന്റ് ഒരു ടാസ്‌ക് ലിസ്റ്റ് സൃഷ്ടിച്ച് മാറ്റങ്ങൾ വരുത്തുകയും സബ്എജന്റുകൾ തമ്മിൽ ബന്ധപ്പെടുത്തുകയും ചെയ്യുന്ന സാഹചര്യങ്ങളിൽ.

പ്രൊഡക്ഷൻ സജ്ജമായ എഐ ഏജന്റുകൾ നൽകാൻ, MAF ഉൾപ്പെടുത്തിയിരിക്കുന്നത്:

- ഓരോ എഐ ഏജന്റിന്റെ എല്ലാ പ്രവർത്തനങ്ങളും ഉൾപ്പെടെ ഓപ്പൺ ടെലിമെട്രി ഉപയോഗിച്ച് നിരീക്ഷണം, ഉപകരണം വിളിക്കൽ, ഓർക്കസ്ട്രേഷൻ ഘട്ടങ്ങൾ, നിരീക്ഷണ പ്രവാഹങ്ങൾ,Microsoft Foundry ഡാഷ്ബോർഡുകൾ വഴി പ്രകടന നിരീക്ഷണം എന്നിവ.
- **സുരക്ഷ** Microsoft Foundry ൽ സ്വദേശിയായി ഏജന്റുകൾ ഹോസ്റ്റ് ചെയ്യുന്നതിലൂടെ, റോള്ബേസ് ആക്‌സസ്, സ്വകാര്യ ഡാറ്റ കൈകാര്യം, ഇൻബിൽറ്റ് ഉള്ളടക്ക സുരക്ഷ തുടങ്ങിയ സുരക്ഷാ നിയന്ത്രണങ്ങൾ ഉൾപ്പെട്ടതാണ്.
- **ദൃഢത** ഏജന്റ് ത്രെഡുകളും വേർക്‌ഫ്ലോസുകളും പause ചെയ്ത് തുടക്കം വയ്ക്കാനും പിഴവുകളിൽ നിന്ന് വീണ്ടെടുക്കാനും സാധിക്കും, ഇത് ദീർഘകാല പ്രവർത്തനങ്ങൾക്ക് സഹായകരമാണ്.
- **നിയന്ത്രണം** മനുഷ്യ സ്വീകാര്യത ആവശ്യമായ താസ്കുകൾ പോലെ മാനവ നിഗമന പങ്കാളിത്തം പ്രവർത്തനങ്ങളിലൂടെ പിന്തുണയ്ക്കുന്നു.

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് ഇന്റർഓപ്പറബിലിറ്റിയിലും ശ്രദ്ധകേന്ദ്രീകരിക്കുന്നു:

- **ക്ലൗഡ്-നിർപേക്ഷം** - ഏജന്റുകൾ കണ്ടെയ്‌നറുകളിൽ, ഓൺ-പ്രെം, പല ക്ലൗഡുകളിലായി പ്രവർത്തിക്കാം.
- **ദാതാവ്-നിർപേക്ഷം** - ഏജന്റുകൾ നിങ്ങളുടെ ഇഷ്ടപ്പെട്ട SDK വഴിയാണ് സൃഷ്ടിക്കത്തക്കത്,Azure OpenAI, OpenAI എന്നിവ ഉൾപ്പെടെ.
- **ഒപ്പൺ സ്റ്റാൻഡേർഡുകൾ സംയോജനം** - Agent-to-Agent (A2A), Model Context Protocol (MCP) പോലുള്ള പ്രോട്ടോകോളുകൾ ഉപയോഗിച്ച് മറ്റ് ഏജന്റുകളെയും ഉപകരണങ്ങളെയും കണ്ടെത്തുകയും ഉപയോഗിക്കുകയും ചെയ്യും.
- **പ്ലഗിൻസും കണക്ഷൻസും** - Microsoft Fabric, SharePoint, Pinecone, Qdrant പോലുള്ള ഡാറ്റയും മെമ്മറിയുമായി ബന്ധം സ്ഥാപിക്കാൻ കഴിയും.

ഈ സവിശേഷതകൾ മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ ചില പ്രാഥമിക ആശയങ്ങളിലേക്ക് എങ്ങനെ പ്രയോഗിക്കപ്പെടുന്നു എന്നു നോക്കാം.

## മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിന്റെ പ്രധാന ആശയങ്ങൾ

### ഏജന്റുകൾ

![Agent Framework](../../../translated_images/ml/agent-components.410a06daf87b4fef.webp)

**ഏജന്റുകൾ സൃഷ്ടിക്കൽ**

ഏജന്റ് സൃഷ്ടിക്കൽ ഇൻഫറൻസ് സർവീസ് (LLM പ്രൊവൈഡർ), AI ഏജന്റ് പിന്തുടരാനിരിക്കുന്ന നിബന്ധനകൾ, ഒപ്പം നിയോഗിച്ച `name` എന്നതു നിർവ്വചിച്ച് നടത്തുന്നു:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

മുകളിൽ `Azure OpenAI` ഉപയോഗിക്കുന്നുണ്ടെങ്കിലും, `Microsoft Foundry Agent Service` ഉൾപ്പെടെ വിവിധ സേവനങ്ങൾ ഉപയോഗിച്ച് ഏജന്റുകൾ സൃഷ്ടിക്കാം:

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

അല്ലെങ്കിൽ [MiniMax](https://platform.minimaxi.com/), വലിയ കൺടെക്‌സ്റ്റ് വിൻഡോകളോടുള്ള (204K ടോക്കൺ വരെ) OpenAI-ഓളം അനുയോജ്യമായ API പ്രദാനം ചെയ്യുന്നു:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

അല്ലെങ്കിൽ A2A പ്രോട്ടോക്കോൾ ഉപയോഗിച്ച് റിമോട്ട് ഏജന്റുകൾ:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**ഏജന്റ് പ്രവർത്തനങ്ങൾ**

ഏജന്റുകൾ നൺ-സ്ട്രീമിംഗ് അല്ലെങ്കിൽ സ്ട്രീമിംഗ് പ്രതികരണത്തിന് `.run` അല്ലെങ്കിൽ `.run_stream` മെത്തഡുകൾ ഉപയോഗിച്ച് പ്രവർത്തിപ്പിക്കുന്നു.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

ഓരോ ഏജന്റ് റൺക്കും `max_tokens` പോലുള്ള പാരാമീറ്ററുകൾ, ഏജന്റ് വിളിക്കാനാകുന്ന `tools`, ഏജന്റിനായി ഉപയോഗിക്കുന്ന `model` തുടങ്ങിയവ പ്രത്യേകമായി ഇഷ്ടാനുസൃതമാക്കാനുള്ള ഓപ്ഷനുകൾ ഉണ്ടായേക്കാം.

ഉപയോക്താവിന്റെ ജോലി പൂർത്തിയാക്കാൻ പ്രത്യേക മോഡലുകളും ഉപകരണങ്ങളും ആവശ്യമായ സാഹചര്യങ്ങളിൽ ഇതു ഉപകാരപ്രദമാണ്.

**ഉപകരണങ്ങൾ**

ഉപകരണങ്ങൾ ഏജന്റ് നിർവചിക്കുമ്പോൾ നിർവ്വചിക്കാനും,

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# ചാറ്റ് ഏജന്റിനെ നേരിട്ടുള്ള സൃഷ്ടിക്കുമ്പോൾ

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ഏജന്റ് പ്രവർത്തിപ്പിക്കുമ്പോഴും നിർവ്വചിക്കാം:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # ഈ റൺ മാത്രമാണ് ഈ ടൂൾ നൽകിയത് )
```

**ഏജന്റ് ത്രെഡുകൾ**

ഏജന്റ് ത്രെഡുകൾ മൾട്ടി-ടേൺ സംഭാഷണങ്ങൾ കൈകാര്യം ചെയ്യാനാണ് ഉപയോഗിക്കുന്നത്. ത്രെഡുകൾ സൃഷ്ടിക്കപ്പെടുന്നത്:

- `get_new_thread()` ഉപയോഗിച്ച്, ഇത് ത്രെഡ് കാലാകാലങ്ങളിൽ സൂക്ഷിക്കാൻ സഹായിക്കുന്നു
- ഏജന്റ് ഓടുമ്പോൾ ത്രെഡ് സ്വയം സൃഷ്ടിച്ച് നിലവിലെ പ്രവർത്തനത്തിൽ മാത്രമേ ത്രെഡ് നിലനിൽക്കൂ.

ത്രെഡ് സൃഷ്ടിക്കാൻ, കോഡ് ഇങ്ങനെ കാണപ്പെടും:

```python
# പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() # ആജന്റ് ത്രെഡുമായി ഓടിക്കുക.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

പിന്നീട് ത്രെഡ് പിന്നീട് ഉപയോഗിക്കാനായി സീരിയലൈസ് ചെയ്യാം:

```python
# ഒരു പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() 

# ത്രെഡിനൊപ്പം ഏജന്റ് പ്രവർത്തിപ്പിക്കുക.

response = await agent.run("Hello, how are you?", thread=thread) 

# സംഭരണത്തിനായി ത്രെഡ് സീരിയലൈസ് ചെയ്യുക.

serialized_thread = await thread.serialize() 

# സംഭരണത്തിൽ നിന്നു ലോഡ് ചെയ്ത ശേഷം ത്രെഡ് സ്റ്റേറ്റ് ഡിസീരിയലൈസ് ചെയ്യുക.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**ഏജന്റ് മിഡിൽവെയർ**

ഉപകരണങ്ങളുമായി LLM കളുമായുള്ള ഇടപെടലുകൾക്കിടെ ഞങ്ങൾ നിർവ്വഹിക്കാനോ ട്രാക്ക് ചെയ്യാനോ ആഗ്രഹിക്കുന്ന സാഹചര്യങ്ങളിൽ ഏജന്റ് മിഡിൽവെയർ സഹായിക്കുന്നു:

*ഫൺക്ഷൻ മിഡിൽവെയർ*

ഈ മിഡിൽവെയർ ഏജന്റും ഫൺക്ഷൻ/ഉപകരണവും തമ്മിലുള്ള ഇടപെടലിൽ പ്രവർത്തനം നിർവ്വഹിക്കാൻ അവസരം നൽകുന്നു. കാൽ കോൾ സമയത്ത് ലോഗിങ് പോലുള്ള പ്രവൃത്തികൾ ചെയ്യാൻ ഇതു ഉപകാരപ്രദമാണ്.

താഴെ കൊഡിൽ `next` അർത്ഥവത്താക്കുന്നത് അടുത്ത മിഡിൽവെയറും യഥാർത്ഥ ഫങ്ഷനും വിളിക്കപ്പെട്ടോ എന്നതാണ്.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # മുൻ-പ്രോസസ്സിംഗ്: ഫംഗ്ഷൻ പ്രവർത്തനം ആരംഭിക്കുന്നതിന് മുൻപ് ലോഗ് ചെയ്യുക
    print(f"[Function] Calling {context.function.name}")

    # അടുത്ത മിഡിൽവെയർ അല്ലെങ്കിൽ ഫംഗ്ഷൻ പ്രവർത്തനത്തിലേക്കുപോകുക
    await next(context)

    # പിന്-പ്രോസസ്സിംഗ്: ഫംഗ്ഷൻ പ്രവർത്തനം കഴിഞ്ഞതിന് ശേഷം ലോഗ് ചെയ്യുക
    print(f"[Function] {context.function.name} completed")
```

*ചാറ്റ് മിഡിൽവെയർ*

ഈ മിഡിൽവെയർ LLM ഉം ഏജന്റും ഇടയിലുള്ള അന്തർപ്രേഷണങ്ങളിൽ പ്രവർത്തിക്കാൻ അല്ലെങ്കിൽ ലോഗ് ചെയ്യാൻ സഹായിക്കുന്നു.

ഇതിൽ AI സർവീസിലേക്ക് അയയ്ക്കപ്പെട്ട `messages` പോലുള്ള പ്രധാന വിവരങ്ങൾ അടങ്ങിയിരിക്കുന്നു.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # മുൻപ്രോസസ്സ്: AI കോള്‍ നടത്തുന്നതിന് മുമ്പ് ലോഗ് ചെയ്‌യുക
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # അടുത്ത മിഡിൽവെയർ അല്ലെങ്കിൽ AI സേവനത്തിലേക്ക് തുടരും
    await next(context)

    # പോസ്റ്റ്-പ്രോസസ്സ്: AI പ്രതികരണത്തിന് ശേഷമുള്ള ലോഗ്
    print("[Chat] AI response received")

```

**ഏജന്റ് മെമ്മറി**

`Agentic Memory` പാഠത്തിൽ ആശയപ്പെടുത്തിയതുപോലെ, മെമ്മറി ഏജന്റിന് വ്യത്യസ്ത കോൺടെക്സ്റ്റുകളിൽ പ്രവർത്തിക്കാൻ സഹായിക്കുന്ന പ്രധാന ഘടകമാണ്. MAF ൽ വിവിധ തരം മെമ്മറികൾ ഉണ്ട്:

*ഇൻ-മെമ്മറി സ്റ്റോറേജ്*

ആപ്ലിക്കേഷൻ റൺടൈം സമയത്ത് ത്രെഡുകളിലെ ഓർമ്മ.

```python
# പുതിയ ത്രെഡ് സൃഷ്ടിക്കുക.
thread = agent.get_new_thread() # ആജന്റ് ആ ത്രെഡിൽ പ്രവർത്തിപ്പിക്കുക.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*സ്ഥിര സന്ദേശങ്ങൾ*

വിവിധ സെഷനുകളിലായി സംഭാഷണചരിത്രം സൂക്ഷിക്കാൻ ഉപയോഗിക്കുന്നു. ഇത് `chat_message_store_factory` ഉപയോഗിച്ച് നിർവചിക്കുന്നു:

```python
from agent_framework import ChatMessageStore

# ഒരു കസ്റ്റം സന്ദേശം സ്റ്റോർ സൃഷ്ടിക്കുക
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*ഡൈനാമിക് മെമ്മറി*

ഏജന്റുകൾ പ്രവർത്തിപ്പിക്കപ്പെടുന്നതിനു മുൻപ് കോൺടെക്സ്റ്റിലേക്ക് ചേർക്കപ്പെടുന്നു. mem0 പോലുള്ള ബാഹ്യ സേവനങ്ങളിൽ സൂക്ഷിക്കാവുന്നതാണ്.

```python
from agent_framework.mem0 import Mem0Provider

# മെം0 ലെ പ്രഗത്ഭമായ മെമ്മറി കഴിവുകൾക്കായി ഉപയോഗിക്കുന്നു
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


വിശകലനക്ഷമത വിശ്വസനീയവും പരിപാലനയോഗ്യവുമായ ഏജന്റിക് സിസ്റ്റങ്ങൾ നിർമ്മിക്കാൻ പ്രാധാന്യമർഹിക്കുന്നു. മികച്ച വിശകലനക്ഷമതക്കായി MAF ഓപൺടെലിമെട്രിയുമായി സംയോജിപ്പിച്ച് ട്രേസിംഗ്‌മാരും മീറ്ററുകളും വാഗ്ദാനം ചെയ്യുന്നു.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # ഏതെങ്കിലും ഒരു കാര്യമാണ് ചെയ്യുക
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### പ്രവൃത്തി പ്രവാഹങ്ങൾ

MAF മുമ്പെ നിർദ്ദേശിച്ച പ്രവൃത്തി മുന്നേറ്റക്രമങ്ങൾ വാഗ്ദാനം ചെയ്യുന്നു, ഇവ ഒരു ജോലി പൂർത്തിയാക്കാനുള്ള കാൽവയ്പ്പുകളാണ്, ആ കാൽവയ്പ്പുകളിലായി AI ഏജന്റുകൾ ഘടകങ്ങളായി ഉൾക്കൊള്ളുന്നു.

പ്രവൃത്തി പ്രവാഹങ്ങൾ മെച്ചപ്പെട്ട നിയന്ത്രണ പ്രവാഹത്തിനായി വ്യത്യസ്ത ഘടകങ്ങളാൽ സമ്പന്നമാണ്. പ്രവൃത്തി പ്രവാഹങ്ങൾ **ബഹുഏജന്റ് ഓർക്കസ്ട്രേഷനും** **ചെക്കുംപോയിന്റിംഗ്** എന്നവയ്‌ക്കായി സ്റ്റേറ്റ് സംരക്ഷിക്കാൻ സഹായിക്കുന്നു.

പ്രവൃത്തി പ്രവാഹത്തിന്റെ പ്രധാന ഘടകങ്ങൾ:

**എക്സിക്യൂട്ടറുകൾ**

എക്സിക്യൂട്ടറുകൾ ഇൻപുട്ട് സന്ദേശങ്ങൾ സ്വീകരിക്കുകയും, നിശ്ചിത ജോലി നിർവഹിച്ച്, പിന്നീട് ഔട്ട്‌പുട്ട് സന്ദേശങ്ങൾ നൽകുകയും ചെയ്യുന്നു. ഇത് വലിയ ജോലിയുടെ പൂർത്തീകരണത്തിലേക്ക് പ്രവൃത്തി മുന്നോട്ടുപോകാൻ സഹായിക്കുന്നു. എക്സിക്യൂട്ടറുകൾ AI ഏജന്റോ കസ്റ്റം ലജിക്കോ ആകാം.

**എഡ്ജുകൾ**

പ്രവൃത്തി പ്രവാഹത്തിൽ സന്ദേശങ്ങളുടെ പ്രവാഹം നിർവചിക്കാൻ എഡ്ജുകൾ ഉപയോഗിക്കുന്നു. ഇവ ഇപ്രകാരം ആകാം:

*ഡയറക്ട് എഡ്ജുകൾ* - എക്സിക്യൂട്ടർമാരുടെ ഇടയിലെ ലളിതമായ ഒറ്റക്ക് ഒറ്റക്ക് ബന്ധങ്ങൾ:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*കണ്ടീഷണൽ എഡ്ജുകൾ* - ചില നിബന്ധനകളിൽ പൂരണമായശേഷം സജീവമാകുന്നു. ഉദാഹരണത്തിന്, ഹോട്ടൽ മുറികൾ ലഭ്യമല്ലാതായാൽ, എക്സിക്യൂട്ടർ മറ്റ് വഴികൾ സൂചിപ്പിക്കാം.

*സ്വിച്ച്-കേസ് എഡ്ജുകൾ* - നിശ്ചിത നിബന്ധനകളുടെ അടിസ്ഥാനത്തിൽ സന്ദേശങ്ങൾ വ്യത്യസ്ത എക്സിക്യൂട്ടർമാർക്ക് റൂട്ടുചെയ്യുന്നു. ഉദാഹരണത്തിന്, യാത്രാ ഉപഭോക്താവിന് മുൻഗണന ലഭ്യമെങ്കിൽ അവരുടെ ജോലികൾ മറ്റൊരു പ്രവൃത്തി പ്രവാഹത്തിലൂടെ കൈകാര്യം ചെയ്യപ്പെടും.

*ഫാൻ-ഔട്ട് എഡ്ജുകൾ* - ഒരു സന്ദേശം നിരവധി ലക്ഷ്യങ്ങളിലേക്ക് അയയ്ക്കുക.

*ഫാൻ-ഇൻ എഡ്ജുകൾ* - വ്യത്യസ്ത എക്സിക്യൂട്ടർമാരിൽ നിന്നുള്ള പല സന്ദേശങ്ങളും ശേഖരിച്ച് ഒരു ലക്ഷ്യത്തിലേക്ക് അയയ്ക്കുക.

**ഇവന്റുകൾ**

പ്രവൃത്തി പ്രവാഹങ്ങളിൽ മികച്ച വിശകലനക്ഷമത നൽകാൻ MAF നിർവ്വഹണത്തിനുള്ള ആഭ്യന്തര ഇവന്റുകൾ വാഗ്ദാനം ചെയ്യുന്നു, അവയിൽ:

- `WorkflowStartedEvent`  - പ്രവൃത്തി പ്രവാഹം ആരംഭിക്കുന്നു
- `WorkflowOutputEvent` - പ്രവൃത്തി പ്രവാഹം ഔട്ട്‌പുട്ട് ഉല്പാദിപ്പിക്കുന്നു
- `WorkflowErrorEvent` - പ്രവൃത്തി പ്രവാഹം പിശക് നേരിടുന്നു
- `ExecutorInvokeEvent`  - എക്സിക്യൂട്ടർ പ്രോസസ്സിങ് ആരംഭിക്കുന്നു
- `ExecutorCompleteEvent`  -  എക്സിക്യൂട്ടർ പ്രോസസ്സിങ് പൂർത്തിയാക്കുന്നു
- `RequestInfoEvent` - ഒരു അഭ്യർത്ഥന പുറപ്പെടുവിക്കുന്നു

## ആധുനിക MAF പാറ്റേണുകൾ

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് മുഖ്യ ആശയങ്ങളെക്കുറിച്ച് മുകളിലുള്ള വിഭാഗങ്ങൾ ഉൾക്കൊള്ളുന്നു. കൂടുതൽ സങ്കീർണ്ണ ഏജന്റുകൾ നിർമ്മിക്കുമ്പോൾ, പരിഗണിക്കാനുള്ള ചില ആധുനിക പാറ്റേണുകൾ:

- **മിഡിൽവെയർ സംയോജനം**: ഏജന്റിന്റെ പെരുമാറ്റം സൂക്ഷ്മമായി നിയന്ത്രിക്കാൻ ഫംഗ്ഷൻ, ചാറ്റ് മിഡിൽവെയർ എന്നിവ ഉപയോഗിച്ച് പല മിഡിൽവെയർ ഹാൻഡ്ലറുകളെ (ലോഗിംഗ്, അനുമതി, നിരക്ക്-പരിമിയൽ) ചേഇൻ ചെയ്യുക.
- **പ്രവൃത്തി പ്രവാഹം ചെക്കുംപോയിന്റിംഗ്**: പ്രവൃത്തി പ്രവാഹ ഇവന്റുകൾ ഉപയോഗിച്ച് ദീർഘകാലം ഓടുന്ന ഏജന്റ് പ്രക്രിയകൾ സംരക്ഷിക്കുകയും പുനരാരംഭിക്കുകയും ചെയ്യുക.
- **ഡൈനാമിക് ടൂൾ സെലക്ഷൻ**: ടൂൾ വിവരണങ്ങളിലുള്ള RAG-നെ MAF ന്റെ ടൂൾ രജിസ്‌ട്രേഷനുമായി സംയോജിപ്പിച്ച് ഓരോ ചോദ്യംക്കും അനുയോജ്യമായ ടൂളുകൾ മാത്രം കാണിക്കുക.
- **ബഹുഏജന്റ് കൈമാറ്റം**: പ്രത്യേക ഏജന്റുകള്ക്ക് മധ്യേ കൈമാറ്റങ്ങൾക്ക് പ്രവൃത്തി പ്രവാഹത്തിന്റെ എഡ്ജുകളും കണ്ടീഷണൽ റൂട്ടിങ്ങും ഉപയോഗിക്കുക.

## മൈക്രോസോഫ്റ്റ് ഫൗണ്ട്രിയിൽ LangChain / LangGraph ഏജന്റുകൾ ഹോസ്റ്റ് ചെയ്യൽ

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്ക് **ഫ്രെയിംവർക്ക്-ഇന്റർഓപ്പറബിളാണ്** — MAF ഉപയോഗിച്ച് എഴുതപ്പെട്ട ഏജന്റുകളിലേക്ക് മാത്രം നിങ്ങൾ പരിമിതീകരിക്കപ്പെട്ടിട്ടില്ല. നിങ്ങൾക്ക് ഇതിനകം **LangChain** അല്ലെങ്കിൽ **LangGraph** ഉപയോഗിച്ച് ഏജന്റ് ഉണ്ടെങ്കിൽ, അത് **Microsoft Foundry ഹോസ്റ്റ് ചെയ്ത ഏജന്റായി** ഓടിക്കാം, ഫൗണ്ട്രി റൺടൈം, സെഷനുകൾ, സ്കേലിംഗ്, ഐഡന്റിറ്റി, പ്രോട്ടോട്ടോൾ എന്റ്പോയിന്റുകൾ എന്നിവ മാനേജ് ചെയ്യുമ്പോൾ നിങ്ങളുടെ ഏജന്റ് ലജിക്ക് LangGraph-ൽ തുടരുന്നു.

ഇത് `langchain_azure_ai.agents.hosting` പാക്കേജ് ഉപയോഗിച്ച് ചെയ്യുന്നു, ഇത് ഫൗണ്ട്രി ഹോസ്റ്റ് ചെയ്ത ഏജന്റുകൾ ഉപയോഗിക്കുന്ന സമാന പ്രോട്ടോകോൾവഴി ഒരു കമ്പൈൽ ചെയ്ത LangGraph ഗ്രാഫ് പ്രദാനം ചെയ്യുന്നു.

**1. ഹോസ്റ്റിംഗ് എക്സ്ട്ര ഇൻസ്റ്റാൾ ചെയ്യുക:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` എക്സ്ട്ര ഇൻസ്റ്റാൾ ചെയ്യുന്നത് ഫൗണ്ട്രി പ്രോട്ടോക്കോൾ ലൈബ്രറികൾ ഇൻസ്റ്റാൾ ചെയ്യുന്നു: `azure-ai-agentserver-responses` (ഓപ്പൺഎഐ-സമരൂപമായ `/responses` എൻഡ്പോയിന്റ്)യും `azure-ai-agentserver-invocations` (ജനറിക് `/invocations` എൻഡ്പോയിന്റ്)യും.

**2. ഹോസ്റ്റിംഗ് പ്രോട്ടോക്കോൾ തിരഞ്ഞെടുക്കുക:**

| പ്രോട്ടോക്കോൾ | ഹോസ്റ്റ് ക്ലാസ് | എൻഡ്പോയിന്റ് | ഉപയോഗിക്കേണ്ടത് |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | നിങ്ങളുടെ ആവശ്യമാണ് ഓപ്പൺഎഐ-സമരൂപമായ ചാറ്റ്, സ്ട്രീമിംഗ്, പ്രതികരണ ചരിത്രം, സംഭാഷണ ത്രെഡിങ്ങ് — സംവാദ ഏജന്റുകൾക്കുള്ള ശുപാർശ ചെയ്ത കാര്യം. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | നിങ്ങൾക്ക് കസ്റ്റം JSON ആകൃതി, വെബ്‌ഹുക്ക് ശൈലിയിലുള്ള എൻഡ്ബോയിന്റ്, അല്ലെങ്കിൽ സംവാദത്തിനു പക്ഷേ അംഗീകൃതമല്ലാത്ത പ്രോസസ്സിംഗ് വേണ്ടയിരിക്കുന്നു. |

കാരണം **Responses API ഫൗണ്ട്രിയിൽ ഏജന്റ്-ശൈലിയുടെ വികസനത്തിന് പ്രാഥമിക API ആണെന്ന്**, മിക്ക ഏജന്റുകൾക്കും `ResponsesHostServer` ഉപയോഗിച്ച് തുടങ്ങുക.

**3. പരിസരപ്രവർത്തക മാറികൾ ക്രമീകരിക്കുക** (`az login` ആദ്യം ചെയ്യുക, അതിനാൽ `DefaultAzureCredential` സ്ഥിരീകരണം നടത്തും):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

ഏജന്റ് പിന്നീട് ഫൗണ്ട്രിയിലെ ഹോസ്റ്റ് ചെയ്ത ഏജന്റായി പ്രവർത്തിക്കുമ്പോൾ, പ്ലാറ്റ്ഫോം സ്വയം `FOUNDRY_PROJECT_ENDPOINT` ഇഞ്ചെക്റ്റ് ചെയ്യും.

**4. Responses പ്രോട്ടോക്കോൾ വഴി LangGraph ഏജന്റ് പ്രകടിപ്പിക്കുക:**

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

    # ChatOpenAI ഇവിടെ Foundry പദ്ധതിയുടെ OpenAI-സമ്ബർക്കമുള്ള (Responses) എൻഡ്പോയിന്റിനെ ലക്ഷ്യമിടുന്നു.
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

ലൊക്കൽ ആയി `python main.py` ഓടിക്കുക, പിന്നീട് `http://localhost:8088/responses`-ന് Responses അഭ്യർത്ഥന അയയ്ക്കുക.

**പ്രധാന പെരുമാറ്റങ്ങൾ:**

- **സംഭാഷണങ്ങൾ**: ക്ലയന്റുകൾ `previous_response_id` അല്ലെങ്കിൽ `conversation` ID അയച്ച് സംഭാഷണം തുടര്ന്നു കൊണ്ടിരിക്കുന്നു. നിങ്ങളുടെ ഗ്രാഫ് LangGraph ചെക്കുംപോയിന്ററോടുകൂടി കമ്പൈൽ ചെയ്തിട്ടുണ്ടെങ്കിൽ, ഫൗണ്ട്രി സംഭാഷണ സ്ഥിതിഗതികള് ചെക്കുംപോയിന്റിലേക്കു കീ ചെയ്യുന്നു (തീവ്രമായ ചെക്കുംപോയിന്റർ പ്രൊഡക്ഷനിൽ ഉപയോഗിക്കുക; ലൊക്കൽ ടെസ്റ്റിങ്ങിനായി `MemorySaver` പോരാ).
- **ഇൻ-ലൂപ് മനുഷ്യൻ**: നിങ്ങളുടെ ഗ്രാഫ് LangGraph `interrupt()` ഉപയോഗിക്കുന്നെങ്കിൽ, `ResponsesHostServer` പണ്ടിങ്ങിലുള്ള ഇടപെടൽ Responsesയിലെ `function_call` / `mcp_approval_request` എന്ന ഉപാധിയായി കാണിക്കുന്നു, ക്ലയന്റുകൾ അപേക്ഷിച്ച `function_call_output` / `mcp_approval_response` ഉപയോഗിച്ച് പുനരാരംഭിക്കുന്നു.
- **ഫൗണ്ട്രിയിൽ വിന్యസിക്കുക**: അല്പം ഉപയോക്തൃ ഉപാധിയോടുകൂടിയ Azure Developer CLI ഉപയോഗിക്കുക — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (ലൊക്കൽ, Docker ആവശ്യമാണ്), ശേഷം `azd provision` , `azd deploy` നടത്തുക. ഹോസ്റ്റ് ചെയ്ത ഏജന്റ് വിന്യസം **Foundry പ്രോജക്റ്റ് മാനേജർ** റോളിനാണ് കീഴടങ്ങിയിട്ടുള്ളത്.

ഈ ഉദാഹരണത്തിന്റെ പ്രവർത്തനക്ഷമമായ പതിപ്പ് [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)-ൽ കാണാം. പൂർണ്ണ വാക്ക്‌ത്രൂ (Invocations പ്രോട്ടോക്കോൾ, കസ്റ്റം അഭ്യർത്ഥന സ്‌കീമകൾ, പ്രശ്ന പരിഹാരങ്ങൾ) വേണ്ടി [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) കാണുക.

## കോഡ് സാമ്പിളുകൾ

മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനുള്ള കോഡ് സാമ്പിളുകൾ ഈ റിപ്പോസിറ്ററിയിലെ `xx-python-agent-framework` এবং `xx-dotnet-agent-framework` ഫയലുകളിൽ ലഭ്യമാണ്.

## മൈക്രോസോഫ്റ്റ് ഏജന്റ് ഫ്രെയിംവർക്കിനെക്കുറിച്ച് കൂടുതൽ ചോദ്യങ്ങളുണ്ടോ?

മറ്റുള്ള പഠിതാക്കളെ കാണാനും ഓഫീസിന്റെ സമയം പങ്കുവെക്കാനും നിങ്ങളുടെ AI ഏജന്റുകൾക്കായുള്ള ചോദ്യങ്ങൾ ഉത്തരം ലഭിക്കാനുമായി [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) ചേരുക.
## മുൻപത്തെ പാഠം

[AI ഏജന്റുകൾക്കുള്ള മെമ്മറി](../13-agent-memory/README.md)

## അടുത്ത പാഠം

[കമ്പ്യൂട്ടർ ഉപയോഗ ഏജന്റുകൾ (CUA) നിർമ്മിക്കൽ](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. അതിന്റെ സ്വാഭാവിക ഭാഷയിലുള്ള അസൽ രേഖയാണ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കേണ്ടത്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->