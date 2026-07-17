# Explorin Microsoft Agent Framework

![Agent Framework](../../../translated_images/pcm/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Intro

Dis lesson go cover:

- Understand Microsoft Agent Framework: Main Features and Wahala E Go Solve  
- Check Di Main Ideas of Microsoft Agent Framework
- Advanced MAF Patterns: Workflows, Middleware, and Memory

## Learning Goals

After you finish dis lesson, you go sabi how to:

- Build Production Ready AI Agents using Microsoft Agent Framework
- Use di main features of Microsoft Agent Framework for your Agentic Use Cases
- Use advanced patterns like workflows, middleware, and observability

## Code Samples 

Code samples for [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) dey for dis repository under `xx-python-agent-framework` and `xx-dotnet-agent-framework` files.

## Understand Microsoft Agent Framework

![Framework Intro](../../../translated_images/pcm/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) na Microsoft unified framework wey dem use build AI agents. E get flexibility to handle plenty different agentic use cases wey dem dey see for production and research like:

- **Sequential Agent orchestration** for situations wey step-by-step workflows dey needed.
- **Concurrent orchestration** for situations wey agents need finish task for the same time.
- **Group chat orchestration** for situations wey agents fit work together on one task.
- **Handoff Orchestration** for situations wey agents dey pass task from one to another as subtasks dey finish.
- **Magnetic Orchestration** for situations wey one manager agent dey create and change task list and dey arrange subagents to finish the task.

To deliver AI Agents for Production, MAF also get features for:

- **Observability** with OpenTelemetry wey dey track every action of the AI Agent including tool usage, orchestration steps, reasoning flows and performance for Microsoft Foundry dashboards.
- **Security** by hosting agents for Microsoft Foundry wey get security controls like role-based access, private data handling and built-in content safety.
- **Durability** as Agent threads and workflows fit pause, resume and recover from errors wey fit make process run for long time.
- **Control** as human in the loop workflows dey wey require human to approve task before e go continue.

Microsoft Agent Framework dey try make e fit work well wit others by:

- **Being Cloud-agnostic** - Agents fit run for containers, on-prem and for plenty different clouds.
- **Being Provider-agnostic** - Agents fit dey created with your preferred SDK including Azure OpenAI and OpenAI
- **Integrating Open Standards** - Agents fit use protocols like Agent-to-Agent(A2A) and Model Context Protocol (MCP) to find and use other agents and tools.
- **Plugins and Connectors** - Connections fit connect to data and memory services like Microsoft Fabric, SharePoint, Pinecone and Qdrant.

Make we look how these features dey apply for some main concepts of Microsoft Agent Framework.

## Main Concepts of Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/pcm/agent-components.410a06daf87b4fef.webp)

**Creating Agents**

You go create agent by defining the inference service (LLM Provider), a
set of instructions wey the AI Agent suppose follow, and assign am `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Di example dey use `Azure OpenAI` but you fit create agents with different services like `Microsoft Foundry Agent Service`:

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

or [MiniMax](https://platform.minimaxi.com/), wey get OpenAI-compatible API with big context windows (up to 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

or remote agents wey use the A2A protocol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Running Agents**

You fit run agents with `.run` or `.run_stream` methods for non-streaming or streaming responses.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Every agent run get options to customize parameters like `max_tokens` wey the agent go use, `tools` wey the agent fit call, and even `model` wey the agent go use.

Dis one good if you need specific models or tools to finish user’s task.

**Tools**

Tools fit dey defined when you dey define the agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Wen you dey create ChatAgent direct

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

and also when you dey run the agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Tool we dem provide just for dis run only )
```

**Agent Threads**

Agent Threads dey handle multi-turn conversations. Threads fit dey created by:

- Using `get_new_thread()` wey go allow the thread to dey saved over time
- Creating thread automatic when you run agent and the thread go last only for that run.

To create thread, your code go be like dis:

```python
# Mek new thread.
thread = agent.get_new_thread() # Run di agent wit di thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

You fit serialize the thread to store am for later use:

```python
# Make new thread.
thread = agent.get_new_thread() 

# Run di agent wit di thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Change di thread to one format wey fit store.

serialized_thread = await thread.serialize() 

# Change di thread state back afta we load am from storage.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agents dey interact wit tools and LLMs to finish user tasks. Sometimes, we want make something happen or track wetin happen for inside these interactions. Agent middleware help us do dis by:

*Function Middleware*

Dis middleware allow us run action between agent and function/tool wey e dey call. Example na when you want do some logging for function call.

For code below `next` talk whether next middleware or the real function go run.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-processing: Log before the function run
    print(f"[Function] Calling {context.function.name}")

    # Continue to next middleware or function run
    await next(context)

    # Post-processing: Log after the function don run
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Dis middleware allow us run or log action between agent and requests between the LLM.

E get important info like `messages` wey dem dey send to AI service.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-processing: Make log before AI call
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continue go next middleware or AI service
    await next(context)

    # Post-processing: Make log after AI response
    print("[Chat] AI response received")

```

**Agent Memory**

Like we explain for `Agentic Memory` lesson, memory serious so that agent fit work over different contexts. MAF get different types of memory:

*In-Memory Storage*

Dis memory dey stored in threads while app dey run.

```python
# Make new thread.
thread = agent.get_new_thread() # Run di agent wit di thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Dis memory dey keep conversation history over different sessions. E dey defined with `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Make one custom message store
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamic Memory*

Dis memory dey add to the context before agents go run. These memories fit dey store inside external services like mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Di use of Mem0 na for advanced memory tori dem
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


Observability na important tin for building reliable and maintainable agentic systems. MAF dey integrate wit OpenTelemetry to provide tracing and meters for beta observability.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # make somtin
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflows

MAF get workflows wey be pre-defined steps to complete task and dem include AI agents as components for those steps.

Workflows dey made up of different components wey allow beta control flow. Workflows too dey enable **multi-agent orchestration** and **checkpointing** to save workflow states.

The core components of workflow na:

**Executors**

Executors go receive input messages, perform their assigned tasks, den produce output message. Dis one dey move workflow go forward to complete the bigger task. Executors fit be AI agent or custom logic.

**Edges**

Edges dey used to define flow of messages inside workflow. Dem fit be:

*Direct Edges* - Simple one-to-one connections between executors:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - Dey activate after some condition don met. For example, if hotel room no dey, executor fit suggest other options.

*Switch-case Edges* - Route messages go different executors based on defined conditions. As example, if travel customer get priority access and their tasks go handled through another workflow.

*Fan-out Edges* - Send one message go multiple targets.

*Fan-in Edges* - Collect multiple messages from different executors den send am go one target.

**Events**

To provide beta observability inside workflows, MAF dey offer built-in events for execution wey include:

- `WorkflowStartedEvent`  - Workflow execution don start
- `WorkflowOutputEvent` - Workflow don produce output
- `WorkflowErrorEvent` - Workflow meet error
- `ExecutorInvokeEvent`  - Executor don start processing
- `ExecutorCompleteEvent`  -  Executor don finish processing
- `RequestInfoEvent` - Request don issue

## Advanced MAF Patterns

The sections wey dey above don cover di key concepts of Microsoft Agent Framework. As you dey build more complex agents, here some advanced patterns to consider:

- **Middleware Composition**: Chain multiple middleware handlers (logging, auth, rate-limiting) using function and chat middleware for fine-grained control over agent behavior.
- **Workflow Checkpointing**: Use workflow events and serialization to save and resume long-running agent processes.
- **Dynamic Tool Selection**: Combine RAG over tool descriptions with MAF's tool registration to present only relevant tools per query.
- **Multi-Agent Handoff**: Use workflow edges and conditional routing to orchestrate handoffs between specialized agents.

## Hosting LangChain / LangGraph Agents on Microsoft Foundry

Microsoft Agent Framework na **framework-interoperable** — you no limited to agents wey dem write wit MAF. If you get agent wey don build wit **LangChain** or **LangGraph**, you fit run am as **Microsoft Foundry hosted agent** so Foundry fit manage runtime, sessions, scaling, identity, and protocol endpoints for you, while your agent logic dey remain for LangGraph.

Dis one na to do wit `langchain_azure_ai.agents.hosting` package, wey dey expose compiled LangGraph graph over di same protocols wey Foundry hosted agents dey use.

**1. Install di hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Di `hosting` extra dey install Foundry protocol libraries: `azure-ai-agentserver-responses` (di OpenAI-compatible `/responses` endpoint) and `azure-ai-agentserver-invocations` (di generic `/invocations` endpoint).

**2. Choose your hosting protocol:**

| Protocol | Host class | Endpoint | Use when |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | You want OpenAI-compatible chat, streaming, response history, and conversation threading — di recommended default for conversational agents. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | You need custom JSON shape, webhook-style endpoint, or non-conversational processing. |

Because **Responses API na di primary API for agent-style development for Foundry**, start wit `ResponsesHostServer` for most agents.

**3. Configure environment variables** (`az login` first so `DefaultAzureCredential` fit authenticate):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

When agent later run as hosted agent for Foundry, platform go inject `FOUNDRY_PROJECT_ENDPOINT` automatically.

**4. Expose LangGraph agent over Responses protocol:**

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

    # ChatOpenAI ya target di Foundry project OpenAI-compatible (Responses) endpoint.
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

Run am locally wit `python main.py`, then send Responses request to `http://localhost:8088/responses`.

**Key behaviors:**

- **Conversations**: Clients go continue conversation by passing `previous_response_id` or `conversation` ID. If your graph compile wit LangGraph checkpointer, Foundry go key conversation state to checkpoint (use durable checkpointer for production; `MemorySaver` good for local test).
- **Human-in-the-loop**: If your graph dey use LangGraph `interrupt()`, `ResponsesHostServer` go surface pending interrupt as Responses `function_call` / `mcp_approval_request` item, and clients go resume wit matching `function_call_output` / `mcp_approval_response`.
- **Deploy to Foundry**: Use Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, need Docker), then `azd provision` and `azd deploy`. Hosted-agent deployment dey require **Foundry Project Manager** role.

Runnable version of dis example dey for [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). For full walkthrough (Invocations protocol, custom request schemas, and troubleshooting), see [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Code Samples 

Code samples for Microsoft Agent Framework fit find inside dis repository under `xx-python-agent-framework` and `xx-dotnet-agent-framework` files.

## Get More Questions About Microsoft Agent Framework?

Join [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet other learners, attend office hours and get your AI Agents questions answered.
## Previous Lesson

[Memory for AI Agents](../13-agent-memory/README.md)

## Next Lesson

[Building Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->