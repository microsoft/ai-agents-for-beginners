# Pagsisiyasat sa Microsoft Agent Framework

![Agent Framework](../../../translated_images/tl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Panimula

Saklawin ng araling ito:

- Pag-unawa sa Microsoft Agent Framework: Mga Pangunahing Tampok at Halaga  
- Pagsisiyasat sa mga Pangunahing Konsepto ng Microsoft Agent Framework
- Mga Advanced na Pattern ng MAF: Workflows, Middleware, at Memorya

## Mga Layunin ng Pagkatuto

Pagkatapos makumpleto ang araling ito, malalaman mo kung paano:

- Gumawa ng AI Agents na Handa para sa Produksyon gamit ang Microsoft Agent Framework
- Ilapat ang mga pangunahing tampok ng Microsoft Agent Framework sa iyong mga Agentic Use Cases
- Gumamit ng mga advanced na pattern kabilang ang workflows, middleware, at observability

## Mga Halimbawa ng Code 

Makikita ang mga halimbawa ng code para sa [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) sa repositoryong ito sa ilalim ng mga file na `xx-python-agent-framework` at `xx-dotnet-agent-framework`.

## Pag-unawa sa Microsoft Agent Framework

![Framework Intro](../../../translated_images/tl/framework-intro.077af16617cf130c.webp)

Ang [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) ay pinag-isang framework ng Microsoft para sa paggawa ng AI agents. Nagbibigay ito ng kakayahang tugunan ang malawak na hanay ng mga agentic use cases na makikita sa parehong produksyon at pananaliksik kabilang ang:

- **Sequential Agent orchestration** sa mga sitwasyong kinakailangan ang hakbang-hakbang na workflows.
- **Concurrent orchestration** sa mga sitwasyong kailangang sabay-sabay na matapos ng mga agent ang mga gawain.
- **Group chat orchestration** sa mga sitwasyong maaaring magtulungan ang mga agent sa isang gawain.
- **Handoff Orchestration** sa mga sitwasyong ipinagpapasa-pasa ng mga agent ang gawain habang natatapos ang mga subtasks.
- **Magnetic Orchestration** sa mga sitwasyong ang isang manager agent ay lumilikha at nagbabago ng listahan ng mga gawain at humahawak sa koordinasyon ng mga subagent upang matapos ang gawain.

Para sa paghahatid ng AI Agents sa Produksyon, ang MAF ay may kasamang mga tampok para sa:

- **Observability** gamit ang OpenTelemetry kung saan bawat aksyon ng AI Agent kabilang ang pagtawag ng tool, mga hakbang ng orchestration, mga daloy ng pangangatwiran at pagmamanman ng pagganap ay nasusubaybayan sa pamamagitan ng mga Microsoft Foundry dashboard.
- **Security** sa pamamagitan ng pagho-host ng mga agent nang native sa Microsoft Foundry na may kasamang mga kontrol sa seguridad tulad ng role-based access, pribadong paghawak ng data at built-in na content safety.
- **Durability** dahil maaari i-pause, i-resume at i-recover mula sa mga error ang mga Agent threads at workflows na nagpapahintulot ng mas matagal na pagpapatakbo.
- **Control** dahil sinusuportahan ang mga workflow na human in the loop kung saan ang mga gawain ay minamarkahan bilang nangangailangan ng pag-apruba ng tao.

Nakatuon din ang Microsoft Agent Framework sa pagiging interoperable sa pamamagitan ng:

- **Being Cloud-agnostic** - Maaaring tumakbo ang mga agent sa containers, on-prem, at sa iba’t ibang mga ulap.
- **Being Provider-agnostic** - Maaaring likhain ang mga agent gamit ang iyong paboritong SDK kabilang ang Azure OpenAI at OpenAI
- **Integrating Open Standards** - Maaaring gamitin ng mga agent ang mga protocol gaya ng Agent-to-Agent(A2A) at Model Context Protocol (MCP) upang tuklasin at gamitin ang ibang mga agent at tool.
- **Plugins and Connectors** - Maaaring kumonekta sa mga serbisyo ng data at memorya tulad ng Microsoft Fabric, SharePoint, Pinecone at Qdrant.

Tingnan natin kung paano inilalapat ang mga tampok na ito sa ilan sa mga pangunahing konsepto ng Microsoft Agent Framework.

## Mga Pangunahing Konsepto ng Microsoft Agent Framework

### Mga Agents

![Agent Framework](../../../translated_images/tl/agent-components.410a06daf87b4fef.webp)

**Paglikha ng Mga Agent**

Ang paglikha ng agent ay ginagawa sa pamamagitan ng pagtukoy sa inference service (LLM Provider), isang
set ng mga tagubilin para sundan ng AI Agent, at isang itinalagang `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Ang nasa itaas ay gumagamit ng `Azure OpenAI` ngunit maaaring likhain ang mga agent gamit ang iba't ibang serbisyo kabilang ang `Microsoft Foundry Agent Service`:

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

o [MiniMax](https://platform.minimaxi.com/), na nagbibigay ng OpenAI-compatible API na may malalaking context window (hanggang 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

o mga remote agents gamit ang A2A protocol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Pagpapatakbo ng Mga Agent**

Ang mga agent ay pinapatakbo gamit ang `.run` o `.run_stream` na mga pamamaraan para sa non-streaming o streaming na mga sagot.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Ang bawat pagpapatakbo ng agent ay maaari ring magkaroon ng mga opsyon para i-customize ang mga parametro tulad ng `max_tokens` na ginagamit ng agent, mga `tools` na maaaring tawagin ng agent, at maging ang mismong `model` na ginagamit ng agent.

Ito ay kapaki-pakinabang sa mga kaso kung saan kinakailangan ang mga partikular na modelo o tool para matapos ang gawain ng isang user.

**Mga Tools**

Maaaring tukuyin ang mga tool kapwa kapag idinedeklara ang agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Kapag direktang lumilikha ng isang ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

at kapag pinapatakbo ang agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Kasangkapang ibinigay para sa takbong ito lamang )
```

**Mga Agent Threads**

Ginagamit ang Agent Threads upang hawakan ang multi-turn conversations. Maaaring likhain ang mga threads sa pamamagitan ng:

- Paggamit ng `get_new_thread()` na nagpapahintulot na mase-save ang thread sa paglipas ng panahon
- Awtomatikong paglikha ng thread kapag pinapatakbo ang isang agent at ang thread ay tumatagal lamang sa kasalukuyang pagpapatakbo.

Para gumawa ng thread, ganito ang hitsura ng code:

```python
# Gumawa ng bagong thread.
thread = agent.get_new_thread() # Patakbuhin ang ahente gamit ang thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Maaari mo itong i-serialize upang maiimbak para sa susunod na paggamit:

```python
# Gumawa ng bagong thread.
thread = agent.get_new_thread() 

# Patakbuhin ang ahente gamit ang thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Iseriyalisa ang thread para sa imbakan.

serialized_thread = await thread.serialize() 

# I-deseriyalisa ang estado ng thread pagkatapos i-load mula sa imbakan.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Nakikipag-interact ang mga agent sa tools at LLM para matapos ang mga gawain ng user. Sa ilang mga senaryo, nais nating magsagawa o mag-track sa pagitan ng mga interaksyong ito. Pinapayagan tayo ng Agent middleware na gawin ito sa pamamagitan ng:

*Function Middleware*

Pinapahintulutan tayo ng middleware na ito na magsagawa ng aksyon sa pagitan ng agent at isang function/tool na tatawagin nito. Halimbawa nito ay kapag nais mong gumawa ng logging sa function call.

Sa code sa ibaba, ang `next` ay tumutukoy kung tatawagin ang susunod na middleware o ang aktwal na function.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Paunang pagproseso: Mag-log bago ang pagpapatakbo ng function
    print(f"[Function] Calling {context.function.name}")

    # Magpatuloy sa susunod na middleware o pagpapatakbo ng function
    await next(context)

    # Pagkatapos ng pagproseso: Mag-log pagkatapos ng pagpapatakbo ng function
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Pinapahintulutan tayo ng middleware na ito na magsagawa o mag-log ng aksyon sa pagitan ng agent at mga request sa pagitan ng LLM.

Nagtataglay ito ng mahahalagang impormasyon tulad ng mga `messages` na ipinapadala sa AI service.

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

    # Panghuling pagproseso: Mag-log pagkatapos ng tugon ng AI
    print("[Chat] AI response received")

```

**Agent Memory**

Tulad ng tinalakay sa araling `Agentic Memory`, mahalagang elemento ang memorya upang paganahin ang agent na mag-operate sa iba't ibang konteksto. Nag-aalok ang MAF ng ilang iba't ibang uri ng memorya:

*In-Memory Storage*

Ito ang memoryang nakaimbak sa mga thread habang tumatakbo ang aplikasyon.

```python
# Gumawa ng bagong thread.
thread = agent.get_new_thread() # Patakbuhin ang agent gamit ang thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Ginagamit ang memoryang ito kapag nag-iimbak ng kasaysayan ng pag-uusap sa iba't ibang mga session. Tinukoy ito gamit ang `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Lumikha ng pasadyang tindahan ng mensahe
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamic Memory*

Ang memoryang ito ay idinadagdag sa konteksto bago patakbuhin ang mga agent. Ang mga memoryang ito ay maaaring i-imbak sa mga external na serbisyo tulad ng mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Paggamit ng Mem0 para sa mga advanced na kakayahan ng memorya
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

Mahalaga ang observability sa paggawa ng mga maaasahan at madaling panatilihin na mga agentic system. Nakikipag-integrate ang MAF sa OpenTelemetry upang magbigay ng tracing at mga meters para sa mas mahusay na observability.

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

Nag-aalok ang MAF ng workflows na mga pre-defined na hakbang upang matapos ang isang gawain at nagsasama ng AI agents bilang mga bahagi ng mga hakbang na iyon.

Binubuo ang workflows ng iba't ibang mga bahagi na nagbibigay-daan sa mas mahusay na kontrol ng daloy. Pinapahintulutan din ng workflows ang **multi-agent orchestration** at **checkpointing** para mase-save ang mga estado ng workflow.

Ang pangunahing mga bahagi ng isang workflow ay:

**Mga Executors**

Tumatanggap ng input messages ang mga executors, isinasagawa ang kanilang mga itinalagang gawain, at pagkatapos ay gumagawa ng output message. Ito ang nagpapasulong sa workflow patungo sa pagtapos ng mas malaking gawain. Ang mga executors ay maaaring AI agent o custom na lohika.

**Mga Edges**

Ginagamit ang mga edges para tukuyin ang daloy ng mga mensahe sa isang workflow. Maaari itong maging:

*Direct Edges* - Simpleng koneksyon na one-to-one sa pagitan ng mga executor:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - Na-a-activate kapag natugunan ang isang partikular na kondisyon. Halimbawa, kapag wala nang available na kwarto sa hotel, maaaring magmungkahi ang executor ng ibang opsyon.

*Switch-case Edges* - Nagreruta ng mga mensahe sa iba't ibang executor base sa mga takdang kondisyon. Halimbawa, kung may priority access ang customer sa paglalakbay at ang mga gawain nila ay hahawakan sa ibang workflow.

*Fan-out Edges* - Nagpapadala ng isang mensahe sa maraming target.

*Fan-in Edges* - Nangongolekta ng maraming mensahe mula sa iba't ibang executor at nagpapadala sa isang target.

**Mga Kaganapan**

Para magbigay ng mas mahusay na observability sa workflows, nag-aalok ang MAF ng mga builtin na kaganapan para sa pagpapatupad kabilang ang:

- `WorkflowStartedEvent`  - Nagsisimula ang pagpapatakbo ng workflow
- `WorkflowOutputEvent` - Nakakagawa ang workflow ng output
- `WorkflowErrorEvent` - Nakakaranas ng error ang workflow
- `ExecutorInvokeEvent`  - Nagsisimula ang executor ng pagproseso
- `ExecutorCompleteEvent`  - Natatapos ng executor ang pagproseso
- `RequestInfoEvent` - Isinasaayos ang isang request

## Mga Advanced na Pattern ng MAF

Tinalakay sa mga seksyon sa itaas ang mga pangunahing konsepto ng Microsoft Agent Framework. Habang gumagawa ka ng mas komplikadong mga agent, narito ang ilang mga advanced na pattern na dapat isaalang-alang:

- **Middleware Composition**: Pagkabit-kabit ng maraming middleware handlers (logging, auth, rate-limiting) gamit ang function at chat middleware para sa mas pinong kontrol sa pag-uugali ng agent.
- **Workflow Checkpointing**: Gamitin ang mga kaganapan at serialization ng workflow upang i-save at ipagpatuloy ang mga pangmatagalang proseso ng agent.
- **Dynamic Tool Selection**: Pagsamahin ang RAG sa tool descriptions gamit ang rehistrasyon ng tool ng MAF upang ipakita lamang ang mga kaugnay na tool per query.
- **Multi-Agent Handoff**: Gamitin ang mga workflow edges at conditional routing upang i-orchestrate ang mga pagpasa-pasa sa pagitan ng mga espesyalistang agent.

## Pagho-host ng LangChain / LangGraph Agents sa Microsoft Foundry

Ang Microsoft Agent Framework ay **framework-interoperable** — hindi ka limitado sa mga agent na naisulat gamit ang MAF. Kung mayroon ka nang agent na ginawa gamit ang **LangChain** o **LangGraph**, maaari mo itong patakbuhin bilang isang **Microsoft Foundry hosted agent** upang pamahalaan ng Foundry ang runtime, sessions, scaling, identity, at protocol endpoints para sa iyo, habang nananatili ang iyong agent logic sa LangGraph.

Ginagawa ito gamit ang `langchain_azure_ai.agents.hosting` package, na naglalantad ng compiled LangGraph graph sa mga kaparehong protocol na ginagamit ng mga Foundry hosted agent.

**1. I-install ang hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Ang `hosting` extra ay nag-i-install ng mga Foundry protocol libraries: `azure-ai-agentserver-responses` (ang OpenAI-compatible na `/responses` endpoint) at `azure-ai-agentserver-invocations` (ang generic na `/invocations` endpoint).

**2. Piliin ang hosting protocol:**

| Protocol | Host class | Endpoint | Use when |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Kapag gusto mong magkaroon ng OpenAI-compatible chat, streaming, response history, at conversation threading — ang inirerekomendang default para sa mga conversational agent. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Kapag kailangan mo ng custom JSON shape, webhook-style endpoint, o non-conversational processing. |

Dahil ang **Responses API ang pangunahing API para sa agent-style development sa Foundry**, simulan sa `ResponsesHostServer` para sa karamihan ng mga agent.

**3. Isaayos ang mga environment variable** (`az login` muna para makapag-authenticate ang `DefaultAzureCredential`):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Kapag pinatakbo ang agent bilang hosted agent sa Foundry, awtomatikong ini-inject ng platform ang `FOUNDRY_PROJECT_ENDPOINT`.

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # Dito, tinatarget ng ChatOpenAI ang OpenAI-compatible (Mga Tugon) endpoint ng Foundry project.
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

- **Mga Pag-uusap**: Pinagpapatuloy ng mga kliyente ang pag-uusap sa pamamagitan ng pagpapasa ng `previous_response_id` o ng `conversation` ID. Kung nakompila ang iyong graph gamit ang LangGraph checkpointer, ini-key ng Foundry ang estado ng pag-uusap sa checkpoint (gumamit ng durable checkpointer sa produksyon; ang `MemorySaver` ay ayos para sa lokal na pagsubok).
- **Human-in-the-loop**: Kung gumagamit ang graph ng LangGraph ng `interrupt()`, inilalabas ng `ResponsesHostServer` ang nakabinbing interrupt bilang Responses `function_call` / `mcp_approval_request` item, at nagpapatuloy ang mga kliyente gamit ang katugmang `function_call_output` / `mcp_approval_response`.
- **Deployment sa Foundry**: Gamitin ang Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokal, nangangailangan ng Docker), pagkatapos ay `azd provision` at `azd deploy`. Ang deployment ng hosted-agent ay nangangailangan ng **Foundry Project Manager** role.

Isang tumatakbong bersyon ng halimbawang ito ay matatagpuan sa [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Para sa buong walkthrough (Invocations protocol, custom request schemas, at troubleshooting), tingnan ang [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Mga Halimbawa ng Code 

Makikita ang mga halimbawa ng code para sa Microsoft Agent Framework sa repositoryong ito sa ilalim ng mga file na `xx-python-agent-framework` at `xx-dotnet-agent-framework`.

## May Karagdagang Mga Tanong Tungkol sa Microsoft Agent Framework?

Sumali sa [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) upang makipagkita sa ibang mga nag-aaral, dumalo sa office hours, at masagot ang iyong mga tanong tungkol sa AI Agents.
## Nakaraang Aralin

[Memory for AI Agents](../13-agent-memory/README.md)

## Susunod na Aralin

[Paggawa ng Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->