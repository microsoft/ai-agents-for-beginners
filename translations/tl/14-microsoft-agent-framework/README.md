# Pagsusuri sa Microsoft Agent Framework

![Agent Framework](../../../translated_images/tl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Panimula

Tatalakayin sa araling ito ang:

- Pag-unawa sa Microsoft Agent Framework: Mga Pangunahing Tampok at Halaga  
- Pagsusuri sa mga Pangunahing Konsepto ng Microsoft Agent Framework
- Mga Advanced na Pattern ng MAF: Mga Workflow, Middleware, at Memorya

## Mga Layunin ng Pagkatuto

Pagkatapos matapos ang araling ito, malalaman mo kung paano:

- Bumuo ng mga AI Agent na Handa na para sa Produksyon gamit ang Microsoft Agent Framework
- Ilapat ang mga pangunahing tampok ng Microsoft Agent Framework sa iyong mga Gamit na Agentic
- Gamitin ang mga advanced na pattern kabilang ang mga workflow, middleware, at obserbabilidad

## Mga Halimbawang Kodigo 

Makikita ang mga halimbawa ng kodigo para sa [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) sa repositoryong ito sa ilalim ng mga file na `xx-python-agent-framework` at `xx-dotnet-agent-framework`.

## Pag-unawa sa Microsoft Agent Framework

![Framework Intro](../../../translated_images/tl/framework-intro.077af16617cf130c.webp)

Ang [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) ay pinag-isang framework ng Microsoft para sa pagbuo ng mga AI agent. Nagbibigay ito ng kakayahang tugunan ang malawak na uri ng mga agentic na gamit na nakikita sa parehong produksyon at mga kapaligirang pananaliksik kabilang ang:

- **Sunod-sunod na Agent orchestration** sa mga sitwasyon kung saan kailangan ng hakbang-hakbang na mga workflow.
- **Kasabay-sabay na orchestration** sa mga sitwasyon kung saan kailangang tapusin ng mga agent ang mga gawain nang sabay.
- **Orchestration ng group chat** sa mga sitwasyon kung saan maaaring magtulungan ang mga agent sa isang gawain.
- **Handoff Orchestration** sa mga sitwasyon kung saan ipinapasa ng mga agent ang gawain sa isa’t isa habang natatapos ang mga subtasks.
- **Magnetic Orchestration** sa mga sitwasyon kung saan ang isang manager agent ay lumilikha at nagbabago ng listahan ng gawain at humahawak ng koordinasyon ng mga subagent para tapusin ang gawain.

Upang maghatid ng AI mga Agent sa Produksyon, may kasama ring mga tampok ang MAF para sa:

- **Obserbabilidad** gamit ang OpenTelemetry kung saan bawat aksyon ng AI Agent kabilang na ang pagtawag ng tool, mga hakbang ng orchestration, mga daloy ng pangangatwiran at pagsubaybay ng performance gamit ang mga dashboard ng Microsoft Foundry.
- **Seguridad** sa pamamagitan ng pagho-host ng mga agent nang native sa Microsoft Foundry na may mga control sa seguridad tulad ng role-based access, pribadong paghawak ng data at built-in na kaligtasan ng nilalaman.
- **Tibay** dahil ang mga Agent threads at workflow ay maaaring mag-pause, magpatuloy at makabawi mula sa mga error na nagpapahintulot sa mas mahaba na proseso.
- **Kontrol** bilang suportado ang human in the loop workflows kung saan ang mga gawain ay nilalagyan ng marka na nangangailangan ng aprubasyon ng tao.

Nakatuon din ang Microsoft Agent Framework sa pagiging interoperable sa pamamagitan ng:

- **Hindi nakadepende sa Cloud** - Maaaring patakbuhin ang mga agent sa mga container, on-prem at sa iba’t ibang cloud.
- **Hindi nakadepende sa Provider** - Maaaring likhain ang mga agent gamit ang iyong paboritong SDK kabilang ang Azure OpenAI at OpenAI
- **Pagsasama ng mga Bukas na Pamantayan** - Maaaring gamitin ng mga agent ang mga protocol tulad ng Agent-to-Agent (A2A) at Model Context Protocol (MCP) upang makahanap at gumamit ng ibang agent at mga tool.
- **Plugins at Connectors** - Maaaring kumonekta sa mga serbisyo ng data at memorya tulad ng Microsoft Fabric, SharePoint, Pinecone at Qdrant.

Tingnan natin kung paano inilalapat ang mga tampok na ito sa ilan sa mga pangunahing konsepto ng Microsoft Agent Framework.

## Pangunahing Konsepto ng Microsoft Agent Framework

### Mga Agent

![Agent Framework](../../../translated_images/tl/agent-components.410a06daf87b4fef.webp)

**Paglikha ng mga Agent**

Ginagawa ang paglikha ng agent sa pamamagitan ng pagtukoy sa inference service (LLM Provider), isang
hanay ng mga tagubilin para sundan ng AI Agent, at isang itinalagang `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ang nasa itaas ay gumagamit ng `Azure OpenAI` ngunit maaaring makalikha ng mga agent gamit ang iba't ibang serbisyo kabilang ang `Microsoft Foundry Agent Service`:

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

o [MiniMax](https://platform.minimaxi.com/), na nagbibigay ng OpenAI-compatible na API na may malalaking context windows (hanggang 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

o mga remote agent gamit ang protocol na A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Pagpapatakbo ng mga Agent**

Pinapatakbo ang mga agent gamit ang `.run` o `.run_stream` na mga metodo para sa non-streaming o streaming na mga tugon.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Bawat pagpapatakbo ng agent ay maaaring may mga opsyon din upang i-customize ang mga parameter tulad ng `max_tokens` na ginagamit ng agent, mga `tools` na maaaring tawagin ng agent, at maging ang mismong `model` na ginagamit para sa agent.

Kapaki-pakinabang ito sa mga pagkakataon kung saan kinakailangan ang mga tiyak na modelo o tool para matapos ang gawain ng gumagamit.

**Mga Tools**

Maaaring tukuyin ang mga tool sa parehong pagdidiklara ng agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kapag direktang lumilikha ng ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

at pati na rin kapag pinapatakbo ang agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Kasangkapang ibinigay para sa takdang pagtakbo lamang )
```

**Agent Threads**

Ginagamit ang Agent Threads upang hawakan ang multi-turn na mga pag-uusap. Maaaring malikha ang mga thread sa pamamagitan ng:

- Paggamit ng `get_new_thread()` na nagpapahintulot na masave ang thread sa paglipas ng panahon
- Awtomatikong paglikha ng thread kapag pinapatakbo ang isang agent at tumatagal lang ang thread sa kasalukuyang takbo.

Para lumikha ng thread, ganito ang hitsura ng kodigo:

```python
# Lumikha ng bagong thread.
thread = agent.get_new_thread() # Patakbuhin ang ahente gamit ang thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Maaari mo ring i-serialize ang thread para maiimbak at magamit sa ibang pagkakataon:

```python
# Lumikha ng bagong thread.
thread = agent.get_new_thread() 

# Patakbuhin ang ahente gamit ang thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Isalansan ang thread para sa imbakan.

serialized_thread = await thread.serialize() 

# I-deserialize ang estado ng thread matapos i-load mula sa imbakan.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Nakikipag-ugnayan ang mga agent sa mga tool at LLM upang matapos ang mga gawain ng gumagamit. Sa ilang mga sitwasyon, nais nating isagawa o subaybayan ang mga pagitan ng mga interaksyong ito. Pinapayagan tayo ng agent middleware na gawin ito sa pamamagitan ng:

*Function Middleware*

Pinapayagan tayo ng middleware na ito na magsagawa ng aksyon sa pagitan ng agent at isang function/tool na tatawagin nito. Halimbawa nito ay kung nais mong gumawa ng logging sa pagtawag ng function.

Sa code sa ibaba, tinutukoy ng `next` kung ang susunod na middleware o ang tunay na function ang dapat tawagin.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-processing: Mag-log bago ang pagpapatupad ng function
    print(f"[Function] Calling {context.function.name}")

    # Magpatuloy sa susunod na middleware o pagpapatupad ng function
    await next(context)

    # Post-processing: Mag-log pagkatapos ng pagpapatupad ng function
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Pinapayagan tayo ng middleware na ito na magsagawa o mag-log ng aksyon sa pagitan ng agent at ng mga request papunta sa LLM.

Naglalaman ito ng mahalagang impormasyon tulad ng mga `messages` na ipinapadala sa serbisyo ng AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Paunang pagproseso: Mag-log bago ang tawag sa AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Magpatuloy sa susunod na middleware o serbisyo ng AI
    await next(context)

    # Pagkatapos ng pagproseso: Mag-log pagkatapos ng tugon ng AI
    print("[Chat] AI response received")

```

**Agent Memory**

Gaya ng tinalakay sa araling `Agentic Memory`, mahalagang elemento ang memorya upang paganahin ang agent na gumana sa iba’t ibang konteksto. Nag-aalok ang MAF ng ilang uri ng mga memorya:

*In-Memory Storage*

Ito ang memorya na nakaimbak sa mga thread habang tumatakbo ang aplikasyon.

```python
# Gumawa ng bagong thread.
thread = agent.get_new_thread() # Patakbuhin ang ahente gamit ang thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Ginagamit ang memoryang ito kapag nag-iimbak ng kasaysayan ng pag-uusap sa iba’t ibang sesyon. Ito ay tinutukoy gamit ang `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Lumikha ng isang pasadyang tindahan ng mensahe
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamic Memory*

Idinadagdag ang memoryang ito sa konteksto bago patakbuhin ang mga agent. Maaaring i-imbak ang mga memoryang ito sa mga panlabas na serbisyo tulad ng mem0:

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

**Agent Observability**

Mahalaga ang obserbabilidad para sa pagbuo ng maaasahan at madaling mapanatili na mga sistemang agentic. Isinasama ng MAF ang OpenTelemetry upang magbigay ng tracing at meters para sa mas mahusay na obserbabilidad.

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

Nag-aalok ang MAF ng mga workflow na mga pre-defined na hakbang upang matapos ang isang gawain at isinasali ang AI agent bilang bahagi ng mga hakbang na iyon.

Binubuo ang mga workflow ng iba’t ibang komponent na nagbibigay ng mas mahusay na daloy ng kontrol. Pinapayagan din ng mga workflow ang **multi-agent orchestration** at **checkpointing** para masave ang mga estado ng workflow.

Ang mga pangunahing komponent ng isang workflow ay:

**Executors**

Tumatanggap ang mga executor ng mga input message, ginagampanan ang kani-kanilang mga gawain, at gumagawa ng output message. Ito ang nagtutulak sa workflow upang matapos ang mas malaking gawain. Maaaring AI agent o custom na lohika ang mga executor.

**Edges**

Ginagamit ang mga edge upang tukuyin ang daloy ng mga mensahe sa workflow. Maaari itong:

*Direct Edges* - Simpleng one-to-one na mga koneksyon sa pagitan ng mga executor:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - Aktibo kapag naabot ang isang tiyak na kondisyon. Halimbawa, kapag walang available na mga kuwarto sa hotel, maaaring magmungkahi ang isang executor ng ibang mga opsyon.

*Switch-case Edges* - Itinuturo ang mga mensahe sa iba't ibang executor batay sa mga tinukoy na kondisyon. Halimbawa, kung ang customer sa paglalakbay ay may priority access, ang kanilang mga gawain ay hahawakan sa pamamagitan ng ibang workflow.

*Fan-out Edges* - Magpadala ng isang mensahe sa maraming target.

*Fan-in Edges* - Kumuha ng maraming mensahe mula sa iba't ibang executor at ipadala sa isang target.

**Mga Kaganapan**

Upang magbigay ng mas mahusay na obserbabilidad sa workflow, nag-aalok ang MAF ng mga built-in na event para sa pagpapatupad kabilang ang:

- `WorkflowStartedEvent`  - Nagsisimula ang pagpapatupad ng workflow
- `WorkflowOutputEvent` - Nagbibigay ng workflow ng output
- `WorkflowErrorEvent` - Nagkaroon ng error ang workflow
- `ExecutorInvokeEvent`  - Nagsimula ang executor sa pagproseso
- `ExecutorCompleteEvent`  - Natapos ng executor ang pagproseso
- `RequestInfoEvent` - Inilabas ang isang request

## Mga Advanced na Pattern ng MAF

Tinatalakay sa mga seksyon sa itaas ang mga pangunahing konsepto ng Microsoft Agent Framework. Habang gumagawa ka ng mas komplikadong mga agent, narito ang ilang mga advanced na pattern na dapat isaalang-alang:

- **Middleware Composition**: Pagsamahin ang maraming middleware handler (logging, auth, rate-limiting) gamit ang function at chat middleware para sa maingat na kontrol sa pag-uugali ng agent.
- **Workflow Checkpointing**: Gamitin ang mga event ng workflow at serialization upang mai-save at maipagpatuloy ang mga mahabang proseso ng agent.
- **Dynamic Tool Selection**: Pagsamahin ang RAG sa mga paglalarawan ng tool kasama ng pagrehistro ng mga tool ng MAF upang ipakita lamang ang mga kaugnay na tool bawat query.
- **Multi-Agent Handoff**: Gamitin ang mga workflow edge at conditional routing upang i-orchestrate ang mga handoff sa pagitan ng mga espesyalistang agent.

## Pag-host ng LangChain / LangGraph Agents sa Microsoft Foundry

Ang Microsoft Agent Framework ay **framework-interoperable** — hindi ka limitado sa mga agent na isinulat gamit ang MAF. Kung mayroon ka nang agent na ginawa gamit ang **LangChain** o **LangGraph**, maaari mo itong patakbuhin bilang **Microsoft Foundry hosted agent** upang pamahalaan ng Foundry ang runtime, mga sesyon, scaling, identity, at mga endpoint ng protocol para sa iyo, habang nananatili ang iyong lohika ng agent sa LangGraph.

Ginagawa ito gamit ang package na `langchain_azure_ai.agents.hosting`, na naglalantad ng isang nakakompilang LangGraph graph gamit ang parehong mga protocol na ginagamit ng mga Foundry hosted agent.

**1. I-install ang hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Ang `hosting` extra ay nag-i-install ng mga Foundry protocol libraries: `azure-ai-agentserver-responses` (ang OpenAI-compatible na `/responses` endpoint) at `azure-ai-agentserver-invocations` (ang generic na `/invocations` endpoint).

**2. Piliin ang hosting protocol:**

| Protocol | Host class | Endpoint | Gamitin kapag |
|----------|-----------|----------|----------------|
| **Responses** | `ResponsesHostServer` | `/responses` | Nais mo ng OpenAI-compatible chat, streaming, kasaysayan ng tugon, at pag-thread ng pag-uusap — ang inirerekomendang default para sa mga conversational agent. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Kailangan mo ng custom JSON shape, isang webhook-style na endpoint, o hindi conversational na pagproseso. |

Dahil ang **Responses API ang pangunahing API para sa agent-style development sa Foundry**, magsimula sa `ResponsesHostServer` para sa karamihan ng mga agent.

**3. I-configure ang mga environment variable** (`az login` muna para makapag-authenticate ang `DefaultAzureCredential`):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Kapag tumakbo ang agent bilang hosted agent sa Foundry, awtomatikong ini-inject ng platform ang `FOUNDRY_PROJECT_ENDPOINT`.

**4. I-expose ang LangGraph agent gamit ang Responses protocol:**

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

    # Ang ChatOpenAI dito ay tumatarget sa Foundry project's OpenAI-compatible (Responses) endpoint.
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

Patakbuhin ito nang lokal gamit ang `python main.py`, pagkatapos magpadala ng Responses request sa `http://localhost:8088/responses`.

**Pangunahing pag-uugali:**

- **Mga Pag-uusap**: Nagpapatuloy ang mga kliyente ng pag-uusap sa pamamagitan ng pagbigay ng `previous_response_id` o isang `conversation` ID. Kung ang graph mo ay nakompila gamit ang LangGraph checkpointer, itinatala ng Foundry ang estado ng pag-uusap sa checkpoint (gumamit ng durable checkpointer sa produksyon; ang `MemorySaver` ay sapat na para sa lokal na pagsubok).
- **Human-in-the-loop**: Kung ginagamit ng graph mo ang LangGraph na `interrupt()`, inilalapit ng `ResponsesHostServer` ang pending interrupt bilang isang Responses `function_call` / `mcp_approval_request` na item, at nagpapatuloy ang mga kliyente gamit ang tugmang `function_call_output` / `mcp_approval_response`.
- **I-deploy sa Foundry**: Gamitin ang Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokal, kailangan ng Docker), pagkatapos ay `azd provision` at `azd deploy`. Nangangailangan ang deployment ng hosted-agent ng **Foundry Project Manager** na papel.

Isang executable na bersyon ng example na ito ay matatagpuan sa [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Para sa buong walkthrough (Invocations protocol, custom request schemas, at troubleshooting), tingnan ang [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Mga Halimbawang Kodigo 

Makikita ang mga halimbawa ng kodigo para sa Microsoft Agent Framework sa repositoryong ito sa ilalim ng mga file na `xx-python-agent-framework` at `xx-dotnet-agent-framework`.

## May Karagdagang Mga Tanong Tungkol sa Microsoft Agent Framework?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagtagpo sa ibang mga nag-aaral, dumalo sa mga office hour at masasagot ang iyong mga tanong tungkol sa AI Agents.
## Nakaraang Aralin

[Memory para sa AI Agents](../13-agent-memory/README.md)

## Susunod na Aralin

[Pagbuo ng mga Agent na Gumagamit ng Computer (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->