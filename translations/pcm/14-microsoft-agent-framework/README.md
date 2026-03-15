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
- Apply di core features of Microsoft Agent Framework to your Agentic Use Cases
- Use advanced patterns like workflows, middleware, and observability

## Code Samples 

Code samples for [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) fit dey inside dis repository under `xx-python-agent-framework` and `xx-dotnet-agent-framework` files.

## Understanding Microsoft Agent Framework

![Framework Intro](../../../translated_images/pcm/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) na Microsoft's unified framework wey dem use build AI agents. E dey give di flexibility to handle di kain kain agentic use cases wey you fit see for production and research environment dem including:

- **Sequential Agent orchestration** for scenarios wey step-by-step workflows dey needed.
- **Concurrent orchestration** for scenarios wey agents suppose finish task for di same time.
- **Group chat orchestration** for scenarios wey agents fit collaborate together on one task.
- **Handoff Orchestration** for scenarios wey agents dey hand off task to each other as dem dey finish subtasks.
- **Magnetic Orchestration** for scenarios wey manager agent dey create and modify task list, also dey coordinate subagents to finish task.

To deliver AI Agents for Production, MAF still get features for:

- **Observability** through OpenTelemetry wey dey track every action of the AI Agent including tool use, orchestration steps, reasoning flows and performance monitoring through Microsoft Foundry dashboards.
- **Security** because agents dey hosted natively on Microsoft Foundry wey get security controls like role-based access, private data handling and built-in content safety.
- **Durability** because Agent threads and workflows fit pause, resume and recover from errors wey fit make them run longer process.
- **Control** because human in the loop workflows dey supported where tasks need human approval.

Microsoft Agent Framework dey also focus on interoperability by:

- **Being Cloud-agnostic** - Agents fit run inside containers, on-premise and across different clouds.
- **Being Provider-agnostic** - Agents fit create with your preferred SDK including Azure OpenAI and OpenAI
- **Integrating Open Standards** - Agents fit use protocols like Agent-to-Agent (A2A) and Model Context Protocol (MCP) to find and use other agents and tools.
- **Plugins and Connectors** - Connections fit join data and memory services like Microsoft Fabric, SharePoint, Pinecone and Qdrant.

Make we check how these features dey apply to some core concepts of Microsoft Agent Framework.

## Key Concepts of Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/pcm/agent-components.410a06daf87b4fef.webp)

**Creating Agents**

Agent creation dey happen by defining inference service (LLM Provider), a set of instructions for the AI Agent to follow, and them assign am `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Di one wey show top na `Azure OpenAI` but you fit create agents with different services including `Microsoft Foundry Agent Service`:

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

or remote agents using the A2A protocol:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Running Agents**

You dey run agents with `.run` or `.run_stream` methods for non-streaming or streaming responses.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Each agent run get options to customize parameters like `max_tokens` wey agent fit use, `tools` wey agent fit call, and even di `model` wey agent go use.

Dis one dey useful if specific models or tools suppose dey use to finish user task.

**Tools**

Tools fit define when you dey create agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Wen yu dae mek ChatAgent chọk-bọk

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

and also when you dey run agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Tool we dem provide just for dis run )
```

**Agent Threads**

Agent Threads dey help handle multi-turn conversations. Threads fit create by:

- Using `get_new_thread()` wey go save di thread over time
- Creating thread automatically when you run agent and thread go last only for current run.

To create thread, di code be like dis:

```python
# Make new thread.
thread = agent.get_new_thread() # Make the agent run wit the thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

You fit serialize di thread so dat e fit store for later use:

```python
# Make new thread.
thread = agent.get_new_thread() 

# Run the agent wit di thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Arrange di thread make e fit store.

serialized_thread = await thread.serialize() 

# Arrange di thread state again after dem don load am from storage.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Agent Middleware**

Agents dey interact with tools and LLMs to finish user tasks. Sometimes, we want execute or track tin for between these interactions. Agent middleware na wetin enable us do dis by:

*Function Middleware*

Dis middleware dey make us fit execute action between agent and function/tool wey e go call. Example na when you want do some logging on function call.

For dis code below, `next` mean if next middleware or the actual function suppose call.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pre-processing: Write log before function begin
    print(f"[Function] Calling {context.function.name}")

    # Continue to next middleware or make function run
    await next(context)

    # Post-processing: Write log after function don finish run
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Dis middleware enable us execute or log an action between agent and requests between LLM.

E get important information like `messages` wey dem dey send go AI service.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pre-processing: Write for log before AI call
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Continue to next middleware or AI service
    await next(context)

    # Post-processing: Write for log after AI response
    print("[Chat] AI response received")

```

**Agent Memory**

Like di `Agentic Memory` lesson talk, memory dey important to make agent fit work across different contexts. MAF get several types memory:

*In-Memory Storage*

Dis na di memory wey thread dey store during application runtime.

```python
# Make new thread.
thread = agent.get_new_thread() # Run di agent wit di thread.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Persistent Messages*

Dis memory dey use to store conversation history across different sessions. Dem dey define am using `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Make wan custom message store
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dynamic Memory*

Dis memory dey add for context before agents run. Dis memories fit store for outside services like mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Di use Mem0 for advanced memory capabilities
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

Observability dey important to build reliable and maintainable agent systems. MAF dey integrate with OpenTelemetry to give tracing and meters for better observability.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # do somtin
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflows

MAF get workflows wey are pre-defined steps to finish task and dem include AI agents as parts for those steps.

Workflows dey made of different components wey allow better control flow. Workflows fit also do **multi-agent orchestration** and **checkpointing** to save workflow states.

Core components of workflow na:

**Executors**

Executors dey receive input messages, perform their assigned tasks, then produce output message. Dis one dey make workflow move forward to finish bigger task. Executors fit be AI agent or custom logic.

**Edges**

Edges dey define flow of messages for workflow. Dem fit be:

*Direct Edges* - Simple one-to-one connections between executors:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Conditional Edges* - E dey activate after condition meet. For example, when hotel rooms no dey available, executor fit suggest other options.

*Switch-case Edges* - Dem route messages go different executors based on conditions wey dem define. For example, if travel customer get priority access, their tasks fit run through another workflow.

*Fan-out Edges* - Send one message to multiple targets.

*Fan-in Edges* - Collect many messages from different executors and send to one target.

**Events**

To make observability better inside workflows, MAF get built-in events for execution including:

- `WorkflowStartedEvent`  - Workflow start
- `WorkflowOutputEvent` - Workflow produce output
- `WorkflowErrorEvent` - Workflow get error
- `ExecutorInvokeEvent`  - Executor start to process
- `ExecutorCompleteEvent`  -  Executor finish process
- `RequestInfoEvent` - Request don issue

## Advanced MAF Patterns

Di sections wey dey top cover key concepts of Microsoft Agent Framework. As you dey build complex agents, here be some advanced patterns wey you fit consider:

- **Middleware Composition**: Chain many middleware handlers (logging, auth, rate-limiting) using function and chat middleware for fine control over agent behavior.
- **Workflow Checkpointing**: Use workflow events and serialization to save and resume long-running agent processes.
- **Dynamic Tool Selection**: Join RAG over tool descriptions with MAF's tool registration to show only relevant tools per query.
- **Multi-Agent Handoff**: Use workflow edges and conditional routing to orchestrate handoffs between special agents.

## Code Samples 

Code samples for Microsoft Agent Framework fit dey this repository under `xx-python-agent-framework` and `xx-dotnet-agent-framework` files.

## Got More Questions About Microsoft Agent Framework?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet other learners, attend office hours and get your AI Agents questions answered.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service wey dem call [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make e correct, abeg make you sabi say automated translation fit get some mistakes or no too correct. Di original document for dia own language be di true source. If na serious info you want, na make human translation wey professional person do you go better. We no responsible for any wahala or misunderstanding wey fit show because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->