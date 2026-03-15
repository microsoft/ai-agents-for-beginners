# Pagsasaliksik sa Microsoft Agent Framework

![Agent Framework](../../../translated_images/tl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Panimula

Tatalakayin sa araling ito ang mga sumusunod:

- Pag-unawa sa Microsoft Agent Framework: Pangunahing mga Katangian at Halaga  
- Pagsusuri sa Pangunahing mga Konsepto ng Microsoft Agent Framework  
- Mga Advanced na Pattern ng MAF: Mga Workflow, Middleware, at Memorya

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano:

- Gumawa ng Mga AI Agent na Handa para sa Produksyon gamit ang Microsoft Agent Framework  
- I-apply ang mga pangunahing katangian ng Microsoft Agent Framework sa iyong mga Use Case ng Ahente  
- Gumamit ng mga advanced na pattern kabilang ang mga workflow, middleware, at obserbabilidad

## Mga Halimbawa ng Code  

Makikita ang mga halimbawa ng code para sa [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) sa repositoryong ito sa ilalim ng mga file na `xx-python-agent-framework` at `xx-dotnet-agent-framework`.

## Pag-unawa sa Microsoft Agent Framework

![Framework Intro](../../../translated_images/tl/framework-intro.077af16617cf130c.webp)

Ang [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) ay pinag-isang framework ng Microsoft para sa paggawa ng mga AI agent. Nagbibigay ito ng kakayahang tugunan ang malawak na uri ng mga use case ng ahente na makikita sa parehong produksyon at mga environment ng pananaliksik kabilang ang:

- **Sunod-sunod na pag-o-orchestrate ng ahente** sa mga sitwasyon kung saan kinakailangan ang mga step-by-step na workflow.  
- **Sabay-sabay na pag-o-orchestrate** sa mga sitwasyon kung saan kailangang tapusin ng mga ahente ang mga gawain nang sabay-sabay.  
- **Pag-o-orchestrate ng group chat** sa mga sitwasyon kung saan maaaring mag-collaborate ang mga ahente sa isang gawain.  
- **Handoff Orchestration** sa mga sitwasyon kung saan ipinapasa ng mga ahente ang gawain sa isa’t isa habang natatapos ang mga subtasks.  
- **Magnetic Orchestration** sa mga sitwasyon kung saan ang isang manager agent ay lumilikha at nagbabago ng listahan ng gawain at nangangalaga sa koordinasyon ng mga subagent para matapos ang gawain.

Para maihatid ang mga AI Agent sa Produksyon, may mga katangian rin ang MAF para sa:

- **Obserbabilidad** gamit ang OpenTelemetry kung saan bawat aksyon ng AI Agent kabilang ang pagtawag sa tool, mga hakbang ng orchestrasyon, daloy ng pangangatwiran, at pagmamatyag sa performance sa pamamagitan ng mga Microsoft Foundry dashboard.  
- **Seguridad** sa pamamagitan ng pag-host ng mga ahente nang natively sa Microsoft Foundry na may kasamang mga control sa seguridad tulad ng role-based access, pribadong paghawak ng data, at built-in na content safety.  
- **Katibayan** dahil maaaring mag-pause, mag-resume, at mag-recover mula sa mga error ang mga thread ng ahente at mga workflow, na nagpapahintulot sa mas mahabang proseso.  
- **Kontrol** dahil sinusuportahan ang human in the loop workflows kung saan minamarka ang mga gawain bilang nangangailangan ng apruba ng tao.

Nakatuon din ang Microsoft Agent Framework sa pagiging interoperable sa pamamagitan ng:

- **Pagiging Cloud-agnostic** - Maaaring tumakbo ang mga ahente sa mga container, on-premises, at sa iba't ibang mga cloud.  
- **Pagiging Provider-agnostic** - Maaaring likhain ang mga ahente gamit ang iyong gustong SDK kabilang ang Azure OpenAI at OpenAI  
- **Pagsasama ng Mga Open Standards** - Maaaring gamitin ng mga ahente ang mga protocol tulad ng Agent-to-Agent (A2A) at Model Context Protocol (MCP) para mahanap at magamit ang ibang mga ahente at mga tool.  
- **Mga Plugin at Connector** - Maaaring kumonekta sa mga serbisyo ng data at memorya gaya ng Microsoft Fabric, SharePoint, Pinecone, at Qdrant.

Suriin natin kung paano ina-apply ang mga katangiang ito sa ilang mga pangunahing konsepto ng Microsoft Agent Framework.

## Pangunahing Mga Konsepto ng Microsoft Agent Framework

### Mga Ahente

![Agent Framework](../../../translated_images/tl/agent-components.410a06daf87b4fef.webp)

**Paglikha ng mga Ahente**

Ginagawa ang paglikha ng ahente sa pamamagitan ng pagtukoy ng inference service (LLM Provider), isang set ng mga instruksiyon na susundin ng AI Agent, at itinalagang `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```
  
Ang nasa itaas ay gumagamit ng `Azure OpenAI` pero maaaring lumikha ng mga ahente gamit ang iba't ibang serbisyo kabilang ang `Microsoft Foundry Agent Service`:

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
  
o remote agents gamit ang A2A protocol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```
  
**Pagpapatakbo ng mga Ahente**

Pinapatakbo ang mga ahente gamit ang `.run` o `.run_stream` na mga pamamaraan para sa hindi streaming o streaming na mga sagot.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```
  
```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```
  
Bawat pagpapatakbo ng ahente ay maaari ring magkaroon ng mga opsyon para i-customize ang mga parametro tulad ng `max_tokens` na ginagamit ng ahente, ang mga `tools` na maaaring tawagan ng ahente, at maging ang mismong `model` na ginagamit ng ahente.

Ito ay kapaki-pakinabang sa mga kaso kung saan kinakailangan ang partikular na mga modelo o mga tool para matapos ang gawain ng user.

**Mga Tool**

Maaaring tukuyin ang mga tool kapwa sa paggawa ng ahente:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kapag direktang lumilikha ng ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```
  
at pati na rin kapag pinapatakbo ang ahente:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Kagamitang ibinigay para lamang sa takbong ito )
```
  
**Mga Thread ng Ahente**

Ginagamit ang mga Thread ng Ahente upang hawakan ang mga pag-uusap na may maraming turn. Maaaring likhain ang mga thread sa alinman sa mga paraan na ito:

- Gamit ang `get_new_thread()` na nagpapahintulot sa thread na mai-save sa paglipas ng panahon  
- Awtomatikong paglikha ng thread kapag pinatatakbo ang ahente at ang thread ay tatagal lamang habang kasalukuyang pagpapatakbo.

Para gumawa ng isang thread, ganito ang itsura ng code:

```python
# Gumawa ng bagong thread.
thread = agent.get_new_thread() # Patakbuhin ang ahente gamit ang thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```
  
Maaari mo ring i-serialize ang thread upang maiimbak para sa hinaharap na paggamit:

```python
# Lumikha ng bagong thread.
thread = agent.get_new_thread() 

# Patakbuhin ang ahente gamit ang thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Isalaysay ang thread para sa pag-iimbak.

serialized_thread = await thread.serialize() 

# I-deserialize ang estado ng thread pagkatapos i-load mula sa imbakan.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```
  
**Middleware ng Ahente**

Nakikipag-ugnayan ang mga ahente sa mga tool at LLM upang tapusin ang mga gawain ng user. Sa ilang mga scenario, gusto nating magsagawa o magtala sa pagitan ng mga interaksyong ito. Pinapahintulutan tayo ng middleware ng ahente na gawin ito sa pamamagitan ng:

*Function Middleware*

Pinapayagan tayo ng middleware na ito na magsagawa ng isang aksyon sa pagitan ng ahente at isang function/tool na tatawagin nito. Isang halimbawa ng paggamit nito ay kung nais mong mag-log ng mga pag-tawag sa function.

Sa code sa ibaba, tinutukoy ng `next` kung tatawagin ang susunod na middleware o ang aktwal na function.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Paunang pagproseso: I-log bago ang pagpapatupad ng function
    print(f"[Function] Calling {context.function.name}")

    # Magpatuloy sa susunod na middleware o pagpapatupad ng function
    await next(context)

    # Pagkatapos ng pagproseso: I-log pagkatapos ng pagpapatupad ng function
    print(f"[Function] {context.function.name} completed")
```
  
*Chat Middleware*

Pinapayagan tayo ng middleware na ito na magsagawa o mag-log ng aksyon sa pagitan ng ahente at ng mga request sa pagitan ng LLM.

Naglalaman ito ng mahahalagang impormasyon tulad ng mga `messages` na ipinapadala sa AI service.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Paunang proseso: Mag-log bago ang tawag sa AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Magpatuloy sa susunod na middleware o serbisyo ng AI
    await next(context)

    # Pagkatapos ng proseso: Mag-log pagkatapos ng tugon ng AI
    print("[Chat] AI response received")

```
  
**Memorya ng Ahente**

Tulad ng tinalakay sa araling `Agentic Memory`, ang memorya ay isang mahalagang elemento upang payagan ang ahente na mag-operate sa iba't ibang mga konteksto. Nag-aalok ang MAF ng ilang magkakaibang uri ng mga memorya:

*In-Memory Storage*

Ito ang memorya na naka-imbak sa mga thread habang tumatakbo ang aplikasyon.

```python
# Lumikha ng bagong thread.
thread = agent.get_new_thread() # Patakbuhin ang ahente gamit ang thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```
  
*Matatagal na Mga Mensahe*

Ginagamit ang memoryang ito kapag iniimbak ang kasaysayan ng pag-uusap sa iba't ibang mga session. Tinukoy ito gamit ang `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Gumawa ng pasadyang imbakan ng mensahe
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```
  
*Dynamic Memory*

Idinagdag ang memoryang ito sa konteksto bago patakbuhin ang mga ahente. Maaaring itago ang mga memoryang ito sa mga panlabas na serbisyo tulad ng mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Paggamit ng Mem0 para sa mga advanced na kakayahan sa memorya
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
  
**Obserbabilidad ng Ahente**

Mahalaga ang obserbabilidad sa pagbuo ng mga maaasahan at madaling mapanatili na mga sistemang agentic. Nakikipag-integrate ang MAF sa OpenTelemetry upang magbigay ng tracing at meter para sa mas mahusay na obserbabilidad.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # gumawa ng isang bagay
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```
  
### Mga Workflow

Nag-aalok ang MAF ng mga workflow na mga paunang tukoy na mga hakbang upang tapusin ang isang gawain at kinabibilangan ang mga AI agent bilang bahagi ng mga hakbang na iyon.

Binubuo ang mga workflow ng iba't ibang mga bahagi na nagpapahintulot ng mas mahusay na daloy ng kontrol. Pinapayagan din ng mga workflow ang **multi-agent orchestration** at **checkpointing** upang mai-save ang mga estado ng workflow.

Ang mga pangunahing bahagi ng workflow ay:

**Executors**

Tumatanggap ang mga executor ng mga input message, isinasagawa ang kanilang mga itinalagang gawain, at pagkatapos ay gumagawa ng output message. Ito ang nagtutulak sa workflow upang matapos ang mas malaking gawain. Maaaring AI agent o custom logic ang mga executor.

**Edges**

Ginagamit ang mga edge upang tukuyin ang daloy ng mga message sa workflow. Maaari itong maging:

*Direct Edges* - Simpleng one-to-one na koneksyon sa pagitan ng mga executor:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```
  
*Conditional Edges* - Na-activate kapag natugunan ang isang partikular na kondisyon. Halimbawa, kapag walang available na mga kuwarto sa hotel, maaaring magmungkahi ang executor ng ibang mga opsyon.

*Switch-case Edges* - Nagpapadala ng mga message sa iba't ibang executor base sa mga tinukoy na kondisyon. Halimbawa, kung ang customer ng paglalakbay ay may priyoridad na access at ang kanilang mga gawain ay hahawakan sa ibang workflow.

*Fan-out Edges* - Nagpapadala ng isang message sa maraming target.

*Fan-in Edges* - Nangongolekta ng maraming message mula sa iba't ibang executor at ipinapadala ito sa isang target.

**Events**

Upang magbigay ng mas mahusay na obserbabilidad sa mga workflow, nag-aalok ang MAF ng mga built-in na event para sa pagpapatupad kabilang ang:

- `WorkflowStartedEvent`  - Nagsisimula ang pagpapatupad ng workflow  
- `WorkflowOutputEvent` - Gumagawa ng output ang workflow  
- `WorkflowErrorEvent` - Nakakaranas ang workflow ng error  
- `ExecutorInvokeEvent`  - Nagsisimula ang executor sa pagproseso  
- `ExecutorCompleteEvent`  - Natatapos ng executor ang pagproseso  
- `RequestInfoEvent` - Isang request ang inilabas

## Mga Advanced na Pattern ng MAF

Tinatalakay sa mga naunang seksyon ang mga pangunahing konsepto ng Microsoft Agent Framework. Habang gumagawa ka ng mas kumplikadong mga ahente, narito ang ilang mga advanced na pattern na maaaring isaalang-alang:

- **Middleware Composition**: Magkadugtong ng maraming middleware handler (logging, auth, rate-limiting) gamit ang function at chat middleware para sa pinong kontrol sa pag-uugali ng ahente.  
- **Workflow Checkpointing**: Gamitin ang mga event ng workflow at serialization para ma-save at ma-resume ang mga pangmatagalang proseso ng ahente.  
- **Dynamic Tool Selection**: Pagsamahin ang RAG sa mga paglalarawan ng tool gamit ang rehistrasyon ng tool ng MAF upang ipakita lamang ang mga kaugnay na tool sa bawat query.  
- **Multi-Agent Handoff**: Gamitin ang mga edge ng workflow at conditional routing upang i-orchestrate ang mga handoff sa pagitan ng mga espesyalisadong ahente.

## Mga Halimbawa ng Code  

Makikita ang mga halimbawa ng code para sa Microsoft Agent Framework sa repositoryong ito sa ilalim ng mga file na `xx-python-agent-framework` at `xx-dotnet-agent-framework`.

## May Iba Ka Pang Mga Tanong Tungkol sa Microsoft Agent Framework?

Sumali sa [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) upang makipagkita sa ibang mga nag-aaral, dumalo sa mga oras ng opisina, at masagot ang iyong mga tanong tungkol sa AI Agents.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay naisalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat pinagsusumikapan naming maging tumpak ang salin, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pinagtibay na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng salin na ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->