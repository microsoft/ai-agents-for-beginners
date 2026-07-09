# Exploring Microsoft Agent Framework

![Agent Framework](../../../translated_images/pcm/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Introduction

Dis lesson go cover:

- Understanding Microsoft Agent Framework: Key Features and Value  
- Exploring the Key Concepts of Microsoft Agent Framework
- Advanced MAF Patterns: Workflows, Middleware, and Memory

## Learning Goals

After you finish dis lesson, you go sabi how to:

- Build Production Ready AI Agents using Microsoft Agent Framework
- Apply the core features of Microsoft Agent Framework to your Agentic Use Cases
- Use advanced patterns including workflows, middleware, and observability

## Code Samples 

Code samples for [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) fit dey for dis repository under `xx-python-agent-framework` and `xx-dotnet-agent-framework` files.

## Understanding Microsoft Agent Framework

![Framework Intro](../../../translated_images/pcm/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) na Microsoft's unified framework for building AI agents. E dey give the flexibility to handle the plenty kinds agentic use cases wey you fit see for both production and research environment dem, including:

- **Sequential Agent orchestration** for things wey need step-by-step workflows.
- **Concurrent orchestration** for where agents need to finish tasks together at the same time.
- **Group chat orchestration** for where agents fit work together on one task.
- **Handoff Orchestration** for where agents dey hand task from one to another as dem dey finish subtasks.
- **Magnetic Orchestration** for where manager agent dey create and modify task list and handle the coordination of subagents to finish the task.

To deliver AI Agents for Production, MAF also get features for:

- **Observability** through OpenTelemetry wey dey track every action of the AI Agent including tool use, orchestration steps, reasoning and performance monitoring through Microsoft Foundry dashboard.
- **Security** by hosting agents natively on Microsoft Foundry wey include security controls like role-based access, private data handling and built-in content safety.
- **Durability** as Agent threads and workflows fit pause, resume and recover from error dem, wey allow longer running process.
- **Control** as human in the loop workflows support, where tasks go need human approval.

Microsoft Agent Framework still dey focused on making am interoperable by:

- **Being Cloud-agnostic** - Agents fit run for containers, on-prem and across different clouds.
- **Being Provider-agnostic** - Agents fit be created through your preferred SDK including Azure OpenAI and OpenAI
- **Integrating Open Standards** - Agents fit use protocols like Agent-to-Agent(A2A) and Model Context Protocol (MCP) to find and use other agents and tools.
- **Plugins and Connectors** - Connections fit dey to data and memory services like Microsoft Fabric, SharePoint, Pinecone and Qdrant.

Make we check how these features dey apply to some core concepts of Microsoft Agent Framework.

## Key Concepts of Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/pcm/agent-components.410a06daf87b4fef.webp)

**Creating Agents**

To create agent, you go define di inference service (LLM Provider),  
set of instructions wey AI Agent go follow, and assign am `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Di one wey dey above dey use `Azure OpenAI` but agents fit be created with different services like `Microsoft Foundry Agent Service`:

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

or [MiniMax](https://platform.minimaxi.com/), wey dey provide OpenAI-compatible API with large context windows (up to 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

or remote agents using the A2A protocol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Running Agents**

Agents dey run using `.run` or `.run_stream` method for either non-streaming or streaming responses.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Each agent run fit get options to customize parameters like `max_tokens` wey agent go use, `tools` wey agent fit call, and even `model` wey agent go use.

E dey useful for cases where specific models or tools dey need to complete user task.

**Tools**

Tools fit dey defined both when you dey define the agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Wen yu di create ChatAgent direktly

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

and also when you dey run the agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Tool wey dem provide for dis run only )
```

**Agent Threads**

Agent Threads dey help handle multi-turn conversations. Threads fit be created by either:

- Using `get_new_thread()` which allow the thread to dey saved over time
- Creating thread automatically when you run agent and thread fit last only during di current run.

To create thread, di code dey like dis:

```python
# Make new thread.
thread = agent.get_new_thread() # Run di agent wit di thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

You fit serialize thread make you store am for later use:

```python
# Make new thread.
thread = agent.get_new_thread() 

# Run di agent wit di thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Turn di thread to serial format for store.

serialized_thread = await thread.serialize() 

# Turn di thread state back after dem load am from storage.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agents dey interact with tools and LLMs to finish user task. For some cases, we want to dey execute or track wetin happen between these interactions. Agent middleware dey enable us do dis through:

*Function Middleware*

Dis middleware dey allow us to execute action between agent and function/tool wey e go call. For example, you fit want do some logging on function call.

For the code below, `next` mean if next middleware or actual function suppose dey called.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-processing: Write log before function run
    print(f"[Function] Calling {context.function.name}")

    # Continue to next middleware or function execution
    await next(context)

    # Post-processing: Write log after function run
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Dis middleware dey allow us execute or log action between agent and requests wey go LLM.

E get beta important info like `messages` wey dem dey send to AI service.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-processing: Make log before AI call
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continue to next middleware or AI service
    await next(context)

    # Post-processing: Make log after AI response
    print("[Chat] AI response received")

```

**Agent Memory**

As we cover for `Agentic Memory` lesson, memory na important part to make agent fit work for different contexts. MAF get different types of memories:

*In-Memory Storage*

Dis memory na the one wey dey stored inside threads during app runtime.

```python
# Make new thread.
thread = agent.get_new_thread() # Run di agent wit di thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Dis memory dey used to store conversation history across different sessions. E dey defined using `chat_message_store_factory` :

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

Dis memory dey added to context before agents run. Dis memories fit dey stored for external services like mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Di use of Mem0 na for beta memory power
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
    # make sometin
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflows

MAF get workflows wey be pre-defined steps to complete task and dem include AI agents as components inside those steps.

Workflows consist of different components wey allow better control flow. Workflows still dey enable **multi-agent orchestration** and **checkpointing** to save workflow states.

The main components of workflow na:

**Executors**

Executors go receive input messages, do the work wey dem assigned, then produce output message. Dis one dey push workflow go front to complete bigger task. Executors fit be AI agent or custom logic.

**Edges**

Edges dey used to define how messages flow for workflow. Dem fit be:

*Direct Edges* - Simple one-to-one connections between executors:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - Dem go activate after certain condition happen. For example, when hotel rooms no dey available, executor fit suggest other options.

*Switch-case Edges* - Dem go route messages to different executors based on condition wey define. For example, if travel customer get priority access, their tasks go dey handled through another workflow.

*Fan-out Edges* - Send one message to plenty targets.

*Fan-in Edges* - Collect plenty messages from different executors and send am to one target.

**Events**

To provide beta observability into workflows, MAF get built-in events for execution wey include:

- `WorkflowStartedEvent`  - Workflow execution don start
- `WorkflowOutputEvent` - Workflow don produce output
- `WorkflowErrorEvent` - Workflow jam error
- `ExecutorInvokeEvent`  - Executor don start processing
- `ExecutorCompleteEvent`  -  Executor don finish processing
- `RequestInfoEvent` - Request don issue  

## Advanced MAF Patterns

The sections wey dey above cover the key concepts of Microsoft Agent Framework. As you dey build more complex agents, here be some advanced patterns to consider:

- **Middleware Composition**: Chain plenty middleware handlers (logging, auth, rate-limiting) using function and chat middleware to get fine control over agent behavior.
- **Workflow Checkpointing**: Use workflow events and serialization to save and resume long-running agent process dem.
- **Dynamic Tool Selection**: Join RAG over tool descriptions with MAF's tool registration to show only relevant tools per query.
- **Multi-Agent Handoff**: Use workflow edges and conditional routing to orchestrate handoffs between specialized agents.

## Hosting LangChain / LangGraph Agents for Microsoft Foundry

Microsoft Agent Framework na **framework-interoperable** — you no limited to agents wey write with MAF. If you get agent wey already build with **LangChain** or **LangGraph**, you fit run am as **Microsoft Foundry hosted agent** so Foundry go manage runtime, sessions, scaling, identity, and protocol endpoints for you, while your agent logic go still dey LangGraph.

Dis one dey done with the `langchain_azure_ai.agents.hosting` package, wey dey expose compiled LangGraph graph over the same protocols wey Foundry hosted agents dey use.

**1. Install the hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

The `hosting` extra go install Foundry protocol libraries: `azure-ai-agentserver-responses` (the OpenAI-compatible `/responses` endpoint) and `azure-ai-agentserver-invocations` (the generic `/invocations` endpoint).

**2. Choose hosting protocol:**

| Protocol | Host class | Endpoint | Use when |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | If you want OpenAI-compatible chat, streaming, response history, and conversation threading — dis one be the recommended default for conversational agents. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | If you need custom JSON shape, webhook-style endpoint, or non-conversational processing. |

Because **Responses API na primary API for agent-style development for Foundry**, start with `ResponsesHostServer` for most agents.

**3. Configure environment variables** (`az login` first so `DefaultAzureCredential` fit authenticate):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

When agent begin run as hosted agent for Foundry, platform go inject `FOUNDRY_PROJECT_ENDPOINT` automatically.

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

    # ChatOpenAI na here e dey target di Foundry project OpenAI-compatible (Responses) endpoint.
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

- **Conversations**: Clients fit continue conversation by passing `previous_response_id` or `conversation` ID. If your graph compile wit LangGraph checkpointer, Foundry go key conversation state to checkpoint (make you use durable checkpointer in production; `MemorySaver` okay for local testing).
- **Human-in-the-loop**: If your graph dey use LangGraph `interrupt()`, `ResponsesHostServer` go show pending interrupt as Responses `function_call` / `mcp_approval_request` item, and clients fit resume with matching `function_call_output` / `mcp_approval_response`.
- **Deploy to Foundry**: Use Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (local, need Docker), then `azd provision` and `azd deploy`. Hosted-agent deployment need **Foundry Project Manager** role.

Runnable version of this example dey [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). For full walkthrough (Invocations protocol, custom request schemas, troubleshooting), see [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Code Samples 

Code samples for Microsoft Agent Framework fit find for this repository under `xx-python-agent-framework` and `xx-dotnet-agent-framework` files.

## You Get More Questions About Microsoft Agent Framework?

Join the [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet other learners, attend office hours and get your AI Agents questions answer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->