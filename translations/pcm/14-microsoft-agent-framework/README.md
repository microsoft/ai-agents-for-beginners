# Di Microsoft Agent Framework Exploration

![Agent Framework](../../../translated_images/pcm/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduction

Dis lesson go cover:

- Understanding Microsoft Agent Framework: Di Main Features and Di Importance  
- Explaining Di Main Concepts of Microsoft Agent Framework
- Advanced MAF Patterns: Workflows, Middleware, and Memory

## Learning Goals

After you finish dis lesson, you go sabi how to:

- Build AI Agents wey ready for production using Microsoft Agent Framework
- Apply di main features of Microsoft Agent Framework to your Agent tasks
- Use advanced patterns like workflows, middleware, and observability

## Code Samples 

Code samples for [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) dey inside dis repo for `xx-python-agent-framework` and `xx-dotnet-agent-framework` files.

## Understanding Microsoft Agent Framework

![Framework Intro](../../../translated_images/pcm/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) na Microsoft wahala wey join everything to fit build AI agents. E get flexibility to handle different kinds agent tasks for both production and research environment including:

- **Sequential Agent orchestration** for situations where step-by-step workflow dey needed.
- **Concurrent orchestration** where multiple agents dey do work at the same time.
- **Group chat orchestration** where agents fit work together on one task.
- **Handoff Orchestration** where agents dey pass task from one to another as subtasks complete.
- **Magnetic Orchestration** where manager agent dey create and change task list then coordinate subagents to finish task.

To deliver AI Agents well for Production, MAF also get features for:

- **Observability** with OpenTelemetry wey dey track every action of AI Agent including tool call, orchestration steps, reasoning, and performance for Microsoft Foundry dashboards.
- **Security** by hosting agents for Microsoft Foundry wey get security controls like role-based access, private data handling, and built-in content safety.
- **Durability** so agent threads and workflows fit pause, resume and recover from errors, making processes fit last longer.
- **Control** where human in the loop workflows fit happen and tasks fit need human approval.

Microsoft Agent Framework also dey focus on being interoperable by:

- **Being Cloud-agnostic** - Agents fit run for containers, on-premise and different clouds.
- **Being Provider-agnostic** - Agents fit be created with your preferred SDK like Azure OpenAI and OpenAI
- **Integrating Open Standards** - Agents fit use protocols like Agent-to-Agent(A2A) and Model Context Protocol (MCP) to find and use other agents and tools.
- **Plugins and Connectors** - Connections fit join data and memory services like Microsoft Fabric, SharePoint, Pinecone and Qdrant.

Make we see how dem dey apply these features to the main concepts of Microsoft Agent Framework.

## Key Concepts of Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/pcm/agent-components.410a06daf87b4fef.webp)

**Creating Agents**

You dey create agent by setting the inference service (LLM Provider), a
set of instructions wey AI Agent go follow, plus assign am a `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Di one wey dey above dey use `Azure OpenAI` but you fit create agents using many services including `Microsoft Foundry Agent Service`:

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

or remote agents wey dey use the A2A protocol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Running Agents**

Agents go run with `.run` or `.run_stream` method for non-stream or streaming responses.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Every agent run fit get options to change parameters like `max_tokens` agent fit use, `tools` wey agent fit call, and even `model` wey agent go use.

Dis dey important when you need certain models or tools to finish user task.

**Tools**

You fit define tools both when you dey define the agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Wen you dey create ChatAgent direct

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

and also when you dey run the agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Tool we dem give for dis run only )
```

**Agent Threads**

Agent Threads dey handle multi-turn conversations. Threads fit be created by either:

- Using `get_new_thread()` wey fit save thread over time
- Automatically creating thread when you run agent and thread only last during this run.

To create thread, di code look like dis:

```python
# Make new thread.
thread = agent.get_new_thread() # Run the agent wit di thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

You fit then serialize thread to store am for later use:

```python
# Make new thread.
thread = agent.get_new_thread() 

# Run di agent wit di thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Put di thread for storage.

serialized_thread = await thread.serialize() 

# Waka di thread state afta comot from storage.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agents dey interact with tools and LLMs to finish user task. For sometimes, we want execute or track in-between these interactions. Agent middleware allow us do dis by:

*Function Middleware*

Dis middleware let us run action between agent and function/tool wey e go call. Example be say you fit want do some logging on the function call.

For code below `next` dey show if the next middleware or the real function go call.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-processing: Log before dem run di function
    print(f"[Function] Calling {context.function.name}")

    # Continue to next middleware or function run
    await next(context)

    # Post-processing: Log after dem don run di function
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Dis middleware allow us do or log action between agent and requests to the LLM.

E get important info like `messages` wey dem dey send to AI service.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-processing: Log before AI call
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continue to next middleware or AI service
    await next(context)

    # Post-processing: Log after AI response
    print("[Chat] AI response received")

```

**Agent Memory**

As e be for `Agentic Memory` lesson, memory na important part to make agent fit operate well over different contexts. MAF get different kinds memory:

*In-Memory Storage*

Dis memory dey store inside threads while app dey run.

```python
# Make new thread.
thread = agent.get_new_thread() # Run the agent wit di thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Dis memory dey store conversation history across different sessions. E dey defined with `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Make one correct message store for yourself
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamic Memory*

Dis memory dey add to the context before agent dem run. Dem fit store memory for external services like mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Di use of Mem0 for better memory waka
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

Observability dey important to build reliable, easy-to-maintain agentic systems. MAF join OpenTelemetry to give tracing and meters for better observability.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # do sometin
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflows

MAF get workflows wey be pre-defined steps to finish task, and dem get AI agents as part of these steps.

Workflows get different parts wey make control better. Workflows also support **multi-agent orchestration** and **checkpointing** to save workflow states.

Di main parts of workflow na:

**Executors**

Executors dey receive input messages, do their assigned work, then give output message. Dis dey move workflow go ahead to finish bigger task. Executors fit be AI agent or custom logic.

**Edges**

Edges dey define message flow inside workflow. Dem fit be:

*Direct Edges* - Simple one-to-one connections between executors:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - Dem go active once certain condition meet. Example be say hotel rooms no dey, executor fit suggest other options.

*Switch-case Edges* - Dem route messages go different executors based on conditions wey dem define. Example be say if travel customer get priority access, their tasks go dey handled through another workflow.

*Fan-out Edges* - Dem send one message to many targets.

*Fan-in Edges* - Dem collect many messages from different executors and send to one target.

**Events**

To give better observability for workflows, MAF get built-in events for execution including:

- `WorkflowStartedEvent` - Workflow execution start
- `WorkflowOutputEvent` - Workflow produce output
- `WorkflowErrorEvent` - Workflow hit error
- `ExecutorInvokeEvent` - Executor start work
- `ExecutorCompleteEvent` - Executor finish work
- `RequestInfoEvent` - Request don come

## Advanced MAF Patterns

Di tins wey I talk before na di main concepts for Microsoft Agent Framework. As you dey build dey more complex agents, here be some advanced patterns to check:

- **Middleware Composition**: Chain many middleware handlers (logging, auth, rate-limiting) using function and chat middleware to control agent behavior well well.
- **Workflow Checkpointing**: Use workflow events and serialization to save and continue long-running agent process.
- **Dynamic Tool Selection**: Mix RAG on tool descriptions with MAF tool registration so as to show only relevant tools for each query.
- **Multi-Agent Handoff**: Use workflow edges and conditional routing to manage handoff between special agents.

## Hosting LangChain / LangGraph Agents for Microsoft Foundry

Microsoft Agent Framework na **framework-interoperable** — you no dey limited to agents wey dem write with MAF. If you don build agent with **LangChain** or **LangGraph**, you fit run am as **Microsoft Foundry hosted agent** so Foundry go handle runtime, sessions, scaling, identity, and protocol endpoints for you, as your agent logic still dey LangGraph.

Dis na with the `langchain_azure_ai.agents.hosting` package, wey expose compiled LangGraph graph over di same protocols wey Foundry hosted agents dey use.

**1. Install di hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

The `hosting` extra install Foundry protocol libraries: `azure-ai-agentserver-responses` (OpenAI-compatible `/responses` endpoint) and `azure-ai-agentserver-invocations` (generic `/invocations` endpoint).

**2. Choose hosting protocol:**

| Protocol | Host class | Endpoint | Use when |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | You want OpenAI-compatible chat, streaming, response history, and conversation threading — di recommended default for conversational agents. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | You need custom JSON shape, webhook-style endpoint, or non-conversational processing. |

Because **Responses API na di main API for agent-style development for Foundry**, make you start with `ResponsesHostServer` for most agents.

**3. Configure environment variables** (`az login` first so `DefaultAzureCredential` fit authenticate):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

When agent go run later as hosted agent for Foundry, platform go inject `FOUNDRY_PROJECT_ENDPOINT` automatically.

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI de target di Foundry project OpenAI-compatible (Responses) endpoint.
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

Run am locally with `python main.py`, then send Responses request go `http://localhost:8088/responses`.

**Key behaviors:**

- **Conversations**: Clients fit continue conversation by passing `previous_response_id` or `conversation` ID. If your graph na LangGraph checkpointer compile, Foundry go link conversation state to checkpoint (make you use durable checkpointer for production; `MemorySaver` dey okay for local testing).
- **Human-in-the-loop**: If your graph use LangGraph `interrupt()`, `ResponsesHostServer` go show pending interrupt as Responses `function_call` / `mcp_approval_request` item, and clients go continue with matching `function_call_output` / `mcp_approval_response`.
- **Deploy to Foundry**: Use Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, need Docker), then `azd provision` and `azd deploy`. Hosted-agent deployment need **Foundry Project Manager** role.

Runnable version of this example dey for [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). For full walkthrough (Invocations protocol, custom request schemas, and troubleshooting), check [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Code Samples 

Code samples for Microsoft Agent Framework dey inside dis repo under `xx-python-agent-framework` and `xx-dotnet-agent-framework` files.

## Get More Questions About Microsoft Agent Framework?

Join [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet other learners, attend office hours and get your AI Agents questions answer.
## Previous Lesson

[Memory for AI Agents](../13-agent-memory/README.md)

## Next Lesson

[Building Computer Use Agents (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->