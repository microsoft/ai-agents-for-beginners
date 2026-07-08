# Pagsisiyasat sa Microsoft Agent Framework

![Agent Framework](../../../translated_images/tl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Panimula

Ang araling ito ay sasaklaw sa:

- Pag-unawa sa Microsoft Agent Framework: Mga Pangunahing Tampok at Halaga  
- Pagsusuri sa Mga Pangunahing Konsepto ng Microsoft Agent Framework
- Mga Advanced na Pattern ng MAF: Mga Workflows, Middleware, at Memorya

## Mga Layunin sa Pagkatuto

Matapos makumpleto ang araling ito, malalaman mo kung paano:

- Gumawa ng Mga AI Agent na Handa sa Produksyon gamit ang Microsoft Agent Framework
- I-apply ang mga pangunahing tampok ng Microsoft Agent Framework sa iyong Mga Agentic Use Cases
- Gumamit ng mga advanced na pattern kabilang ang workflows, middleware, at observability

## Mga Halimbawa ng Code 

Ang mga halimbawa ng code para sa [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) ay matatagpuan sa repositoryong ito sa ilalim ng mga file na `xx-python-agent-framework` at `xx-dotnet-agent-framework`.

## Pag-unawa sa Microsoft Agent Framework

![Framework Intro](../../../translated_images/tl/framework-intro.077af16617cf130c.webp)

Ang [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) ay ang pinag-isang framework ng Microsoft para sa paggawa ng mga AI agent. Nag-aalok ito ng kakayahang umangkop upang tugunan ang iba't ibang mga agentic use case na nakikita sa parehong production at research environments kabilang ang:

- **Sunod-sunod na orchestration ng Agent** sa mga senaryo kung saan kinakailangan ang hakbang-hakbang na mga workflow.
- **Sabayang orchestration** sa mga senaryo kung saan kailangang tapusin ng mga agent ang mga gawain nang sabay.
- **Orchestration ng group chat** sa mga senaryo kung saan maaaring magtulungan ang mga agent sa isang gawain.
- **Handoff Orchestration** sa mga senaryo kung saan ipinapasa-pasa ng mga agent ang gawain habang tinatapos ang mga subtask.
- **Magnetic Orchestration** sa mga senaryo kung saan ang isang manager agent ay lumilikha at nagbabago ng listahan ng mga gawain at pinangangasiwaan ang koordinasyon ng subagents upang makumpleto ang gawain.

Upang maghatid ng AI Agents sa Produksyon, naglalaman din ang MAF ng mga tampok para sa:

- **Observability** sa pamamagitan ng paggamit ng OpenTelemetry kung saan bawat aksyon ng AI Agent kasama ang pagtawag ng tool, mga hakbang ng orchestration, mga daloy ng pangangatwiran at performance monitoring sa pamamagitan ng Microsoft Foundry dashboards.
- **Seguridad** sa pamamagitan ng pagho-host ng mga agent nang lokal sa Microsoft Foundry na may kasamang mga control sa seguridad tulad ng role-based access, pribadong paghawak ng data at built-in na kaligtasan ng nilalaman.
- **Katibayan** dahil maaaring mag-pause, mag-resume at mag-recover mula sa mga error ang mga thread at workflow ng Agent na nagpapahintulot sa mas mahabang proseso.
- **Kontrol** dahil sinusuportahan ang mga human in the loop workflows kung saan ang mga gawain ay minarkahan bilang kailangan ng aprubasyon ng tao.

Nakatuon din ang Microsoft Agent Framework sa pagiging interoperable sa pamamagitan ng:

- **Hindi naka-depende sa Cloud** - Maaaring tumakbo ang mga agent sa mga container, on-prem, at sa iba't ibang cloud.
- **Hindi naka-depende sa Provider** - Maaaring malikha ang mga agent gamit ang iyong paboritong SDK kabilang ang Azure OpenAI at OpenAI
- **Pagsasama ng Open Standards** - Maaaring gamitin ng mga agent ang mga protocol tulad ng Agent-to-Agent(A2A) at Model Context Protocol (MCP) upang matagpuan at magamit ang ibang mga agent at tool.
- **Mga Plugin at Connector** - Maaaring kumonekta sa mga serbisyo ng data at memorya tulad ng Microsoft Fabric, SharePoint, Pinecone at Qdrant.

Tingnan natin kung paano inilalapat ang mga tampok na ito sa ilan sa mga pangunahing konsepto ng Microsoft Agent Framework.

## Mga Pangunahing Konsepto ng Microsoft Agent Framework

### Mga Agent

![Agent Framework](../../../translated_images/tl/agent-components.410a06daf87b4fef.webp)

**Paggawa ng mga Agent**

Ginagawa ang paglikha ng agent sa pamamagitan ng pagtukoy sa inference service (LLM Provider), isang
set ng mga tagubilin na susundin ng AI Agent, at isang itinalagang `pangalan`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ang nasa itaas ay gamit ang `Azure OpenAI` ngunit maaaring malikha ang mga agent gamit ang iba't ibang mga serbisyo kabilang ang `Microsoft Foundry Agent Service`:

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

o [MiniMax](https://platform.minimaxi.com/), na nag-aalok ng OpenAI-compatible API na may malalaking windows ng konteksto (hanggang 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

o mga remote na agent gamit ang A2A protocol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Pagpapatakbo ng mga Agent**

Pinapatakbo ang mga agent gamit ang `.run` o `.run_stream` na mga metodo para sa hindi streaming o streaming na mga tugon.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Ang bawat pagpapatakbo ng agent ay maaaring magkaroon ng mga opsyon para i-customize ang mga parameter tulad ng `max_tokens` na ginagamit ng agent, mga `tools` na maaaring tawagin ng agent, at maging ang mismong `model` na ginagamit para sa agent.

Ito ay kapaki-pakinabang sa mga kaso kung saan kinakailangan ang mga partikular na modelo o tool upang matapos ang gawain ng user.

**Mga Tool**

Maaaring tukuyin ang mga tool kapwa sa pagtukoy ng agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kapag direktang lumilikha ng isang ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

at kapag pinapatakbo ang agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Kasangkapang ibinigay para sa pagtakbong ito lamang )
```

**Mga Thread ng Agent**

Ginagamit ang mga Agent Thread upang hawakan ang mga multi-turn na pag-uusap. Maaaring malikha ang mga thread alinman sa pamamagitan ng:

- Paggamit ng `get_new_thread()` na nagpapahintulot sa pagpapanatili ng thread sa paglipas ng panahon
- Awtomatikong paglikha ng thread kapag pinapatakbo ang isang agent at nagtatagal lamang ang thread habang tumatakbo ang kasalukuyang session.

Para gumawa ng thread, ganito ang hitsura ng code:

```python
# Lumikha ng bagong thread.
thread = agent.get_new_thread() # Patakbuhin ang agent gamit ang thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Maaari mo ring i-serialize ang thread upang itabi para sa susunod na paggamit:

```python
# Gumawa ng bagong thread.
thread = agent.get_new_thread() 

# Patakbuhin ang agent gamit ang thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# I-serialize ang thread para sa pag-iimbak.

serialized_thread = await thread.serialize() 

# I-deserialize ang estado ng thread pagkatapos i-load mula sa imbakan.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Nakikipag-ugnayan ang mga agent sa mga tool at LLM upang tapusin ang mga gawain ng user. Sa ilang mga senaryo, nais nating magpatupad o mag-trace ng mga aksyon sa pagitan ng mga interaksyong ito. Pinapahintulutan tayo ng agent middleware na gawin ito sa pamamagitan ng:

*Function Middleware*

Pinapahintulutan tayo ng middleware na ito na magpatupad ng isang aksyon sa pagitan ng agent at ng isang function/tool na tatawagin nito. Halimbawa, maaaring gamitin ito para sa pag-log sa pagtawag ng function.

Sa code sa ibaba, tinutukoy ng `next` kung tatawagin ang susunod na middleware o ang aktwal na function.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Paunang pagproseso: Mag-log bago ang pagpapatupad ng function
    print(f"[Function] Calling {context.function.name}")

    # Magpatuloy sa susunod na middleware o pagpapatupad ng function
    await next(context)

    # Pagkatapos ng pagproseso: Mag-log pagkatapos ng pagpapatupad ng function
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Pinapahintulutan tayo ng middleware na ito na magpatupad o mag-log ng aksyon sa pagitan ng agent at ng mga request sa pagitan ng LLM .

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

    # Post-proseso: Mag-log pagkatapos ng tugon ng AI
    print("[Chat] AI response received")

```

**Memorya ng Agent**

Tulad ng tinalakay sa araling `Agentic Memory`, mahalagang elemento ang memorya upang mapagana ang agent sa iba't ibang mga konteksto. Nag-aalok ang MAF ng ilang iba't ibang uri ng memorya:

*Pag-iimbak sa Memorya*

Ito ang memorya na naitatago sa mga thread habang tumatakbo ang aplikasyon.

```python
# Gumawa ng bagong thread.
thread = agent.get_new_thread() # Patakbuhin ang ahente gamit ang thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Ginagamit ang memoryang ito kapag nagtago ng kasaysayan ng pag-uusap sa iba’t ibang session. Tinukoy ito gamit ang `chat_message_store_factory` :

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

Idinadagdag ang memoryang ito sa konteksto bago patakbuhin ang mga agent. Maaaring itago ang mga memoryang ito sa mga panlabas na serbisyo tulad ng mem0:

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

**Observability ng Agent**

Mahalaga ang Observability sa paggawa ng mga maaasahan at mapananatiling mga agentic system. Nakikisalamuha ang MAF sa OpenTelemetry upang magbigay ng tracing at meters para sa mas magandang obserbasyon.

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

### Mga Workflows

Nag-aalok ang MAF ng mga workflow na mga naunang tinukoy na hakbang upang matapos ang isang gawain at nagsasama ng mga AI agent bilang mga bahagi sa mga hakbang na iyon.

Binubuo ang mga workflow ng iba't ibang bahagi na nagpapahintulot ng mas magandang control flow. Pinapahintulutan din ng mga workflow ang **multi-agent orchestration** at **checkpointing** upang mai-save ang mga estado ng workflow.

Ang mga pangunahing bahagi ng workflow ay:

**Executors**

Tumatanggap ng input messages ang mga executor, isinasagawa ang kanilang itinalagang mga gawain, at pagkatapos ay gumagawa ng output message. Ito ang nagtutulak sa workflow pasulong upang matapos ang mas malaking gawain. Maaaring AI agent o custom logic ang mga executor.

**Edges**

Ginagamit ang mga edge upang tukuyin ang daloy ng mga mensahe sa workflow. Maaari itong:

*Mga Direct Edge* - Simple, one-to-one na koneksyon sa pagitan ng mga executor:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Mga Conditional Edge* - Nai-activate pagkatapos matugunan ang isang kundisyon. Halimbawa, kapag wala nang bakanteng hotel room, maaaring magmungkahi ang executor ng ibang opsyon.

*Mga Switch-case Edge* - Ruta ng mga mensahe sa iba't ibang executor base sa tinukoy na mga kundisyon. Halimbawa, kung may priority access ang travel customer at ang kanilang mga gawain ay hahawakan sa ibang workflow.

*Mga Fan-out Edge* - Magpadala ng isang mensahe sa maraming mga target.

*Mga Fan-in Edge* - Kolektahin ang maraming mensahe mula sa iba't ibang executor at ipadala sa isang target.

**Mga Kaganapan**

Upang mapabuti ang obserbasyon sa mga workflow, nag-aalok ang MAF ng mga built-in na kaganapan para sa executation kabilang ang:

- `WorkflowStartedEvent`  - Nagsisimula ang pagpapatupad ng workflow
- `WorkflowOutputEvent` - Lumilikha ang workflow ng output
- `WorkflowErrorEvent` - Nakaranas ng error ang workflow
- `ExecutorInvokeEvent`  - Nagsisimula ang executor sa pagproseso
- `ExecutorCompleteEvent`  - Natatapos ang executor sa pagproseso
- `RequestInfoEvent` - Isang request ang inilabas

## Mga Advanced na Pattern ng MAF

Sinasaklaw ng mga seksyon sa itaas ang mga pangunahing konsepto ng Microsoft Agent Framework. Habang gumagawa ka ng mas kumplikadong mga agent, narito ang ilang mga advanced na pattern na dapat isaalang-alang:

- **Middleware Composition**: I-chain ang maraming middleware handler (logging, auth, rate-limiting) gamit ang function at chat middleware para sa mas detalyadong kontrol sa pag-uugali ng agent.
- **Workflow Checkpointing**: Gamitin ang mga kaganapan sa workflow at serialization upang i-save at i-resume ang mga pangmatagalang proseso ng agent.
- **Dynamic Tool Selection**: Pagsamahin ang RAG sa mga paglalarawan ng tool gamit ang tool registration ng MAF para ipakita lamang ang mga mahahalagang tool bawat query.
- **Multi-Agent Handoff**: Gamitin ang mga edge ng workflow at conditional routing upang i-orchestrate ang mga handoff sa pagitan ng mga espesyalisadong agent.

## Pagho-host ng LangChain / LangGraph Agents sa Microsoft Foundry

Ang Microsoft Agent Framework ay **framework-interoperable** — hindi ka limitado sa mga agent na naisulat sa MAF. Kung mayroon ka nang agent na ginawa gamit ang **LangChain** o **LangGraph**, maaari mo itong patakbuhin bilang isang **Microsoft Foundry hosted agent** upang ang Foundry ang pamahala sa runtime, mga session, scaling, pagkakakilanlan, at mga protocol endpoint para sa iyo, habang nananatili ang iyong lohika ng agent sa LangGraph.

Ginagawa ito gamit ang `langchain_azure_ai.agents.hosting` package, na naglalantad ng isang compiled LangGraph graph sa parehong mga protocol na ginagamit ng mga hosted agent ng Foundry.

**1. I-install ang hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Inu-install ng `hosting` extra ang mga Foundry protocol library: `azure-ai-agentserver-responses` (ang OpenAI-compatible `/responses` endpoint) at `azure-ai-agentserver-invocations` (ang generic na `/invocations` endpoint).

**2. Pumili ng hosting protocol:**

| Protocol | Host class | Endpoint | Gamitin kapag |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Gusto mo ng OpenAI-compatible chat, streaming, kasaysayan ng tugon, at pagtatali ng pag-uusap — ang inirerekomendang default para sa mga conversational agent. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Kailangan mo ng custom na hugis ng JSON, isang webhook-style na endpoint, o di-konbersasyonal na pagproseso. |

Dahil ang **Responses API ang pangunahing API para sa pag-develop ng agent-style sa Foundry**, magsimula sa `ResponsesHostServer` para sa karamihan ng mga agent.

**3. I-configure ang environment variables** (`az login` muna para mag-authenticate ang `DefaultAzureCredential`):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Kapag tumakbo ang agent bilang hosted agent sa Foundry, awtomatikong ini-inject ng platform ang `FOUNDRY_PROJECT_ENDPOINT`.

**4. I-expose ang LangGraph agent sa Responses protocol:**

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

    # Ang ChatOpenAI dito ay tumutukoy sa OpenAI-compatible (Responses) endpoint ng proyektong Foundry.
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

**Pangunahing mga pag-uugali:**

- **Pag-uusap**: Ipinagpapatuloy ng mga kliyente ang pag-uusap sa pamamagitan ng pagpapasa ng `previous_response_id` o isang `conversation` ID. Kung ang iyong graph ay na-compile gamit ang LangGraph checkpointer, kinukulong ng Foundry ang estado ng pag-uusap sa checkpoint (gamitin ang durable checkpointer sa produksyon; ayos na ang `MemorySaver` para sa lokal na pagsubok).
- **Human-in-the-loop**: Kung ang iyong graph ay gumagamit ng LangGraph `interrupt()`, inilalantad ng `ResponsesHostServer` ang pending interrupt bilang isang Responses `function_call` / `mcp_approval_request` item, at nagpapatuloy ang mga kliyente gamit ang tugmang `function_call_output` / `mcp_approval_response`.
- **Deploy sa Foundry**: Gamitin ang Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokal, kailangan ng Docker), pagkatapos ay `azd provision` at `azd deploy`. Kinakailangan ang papel na **Foundry Project Manager** para sa deployment ng hosted-agent.

Isang runnable na bersyon ng halimbawa na ito ay nasa [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Para sa buong walkthrough (Invocations protocol, custom request schemas, at troubleshooting), tingnan ang [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Mga Halimbawa ng Code 

Ang mga halimbawa ng code para sa Microsoft Agent Framework ay matatagpuan sa repositoryong ito sa ilalim ng mga file na `xx-python-agent-framework` at `xx-dotnet-agent-framework`.

## May Karagdagang mga Tanong Tungkol sa Microsoft Agent Framework?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagkita sa iba pang mga nag-aaral, dumalo sa office hours at masagot ang iyong mga tanong tungkol sa AI Agents.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->