# Explore AI Agent Frameworks

AI agent frameworks are software platforms designed to simplify the creation, deployment, and management of AI agents. These frameworks provide developers with pre-built components, abstractions, and tools that streamline the development of complex AI systems.

These frameworks help developers focus on the unique aspects of their applications by providing standardized approaches to common challenges in AI agent development. They enhance scalability, accessibility, and efficiency in building AI systems.

## Introduction

This lesson will cover:

- What are AI Agent Frameworks and what do they enable developers to do?
- How can teams use these to quickly prototype, iterate, and improve my agent’s capabilities?
- What are the difference between the frameworks and tools created by Microsoft ( [AutoGen](https://aka.ms/ai-agents/autogen){target="_blank"} / [Semantic Kernel](https://aka.ms/ai-agents-beginners/semantic-kernel){target="_blank"} / [Azure AI Agent Service](https://aka.ms/ai-agents-beginners/ai-agent-service){target="_blank"}) 
- Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?
- What is Azure AI Agents service and how is this helping me?

## Learning goals

The goals of this lesson is to help you understand:

- The role of AI Agent Frameworks in AI development.
- How to leverage AI Agent Frameworks to build intelligent agents.
- Key capabilities enabled by AI Agent Frameworks.
- The differences between AutoGen, Semantic Kernel, and Azure AI Agent Service.

## What are AI Agent Frameworks and what do they enable developers to do?

Traditional AI Frameworks can help you integrate AI into your apps and make these apps better in the following ways:

- **Personalization**: AI can analyze user behavior and preferences to provide personalized recommendations, content, and experiences.
Example: Streaming services like Netflix use AI to suggest movies and shows based on viewing history, enhancing user engagement and satisfaction.
- **Automation and Efficiency**: AI can automate repetitive tasks, streamline workflows, and improve operational efficiency.
Example: Customer service apps use AI-powered chat bots to handle common inquiries, reducing response times and freeing up human agents for more complex issues.
- **Enhanced User Experience**: AI can improve the overall user experience by providing intelligent features such as voice recognition, natural language processing, and predictive text.
Example: Virtual assistants like Siri and Google Assistant use AI to understand and respond to voice commands, making it easier for users to interact with their devices.

### That all sounds great right, so why we do we need AI Agent Framework?

AI Agent frameworks represent something more than just AI frameworks. They are designed to enable the creation of intelligent agents that can interact with users, other agents, and the environment to achieve specific goals. These agents can exhibit autonomous behavior, make decisions, and adapt to changing conditions. Let's look at some key capabilities enabled by AI Agent Frameworks:

- **Agent Collaboration and Coordination**: Enable the creation of multiple AI agents that can work together, communicate, and coordinate to solve complex tasks.
- **Task Automation and Management**: Provide mechanisms for automating multi-step workflows, task delegation, and dynamic task management among agents.
- **Contextual Understanding and Adaptation**: Equip agents with the ability to understand context, adapt to changing environments, and make decisions based on real-time information.

So in summary, agents allow you to do more, to take automation to the next level, to create more intelligent systems that can adapt and learn from their environment.

## How to quickly prototype, iterate, and improve the agent’s capabilities?

This is fast moving landscape, but there are some things that are common across most AI Agent Frameworks that can help you quickly prototype and iterate namely module components, collaborative tools, and real-time learning. Let's dive into these:

- **Use Modular Components**: AI Frameworks offer pre-built components such as prompts, parsers, and memory management.
- **Leverage Collaborative Tools**: Design agents with specific roles and tasks, enabling them to test and refine collaborative workflows.
- **Learn in Real-Time**: Implement feedback loops where agents learn from interactions and adjust their behavior dynamically.

### Use Modular Components

Frameworks like LangChain and Microsoft Semantic Kernel offer pre-built components such as prompts, parsers, and memory management.

**How teams can use these**: Teams can quickly assemble these components to create a functional prototype without starting from scratch, allowing for rapid experimentation and iteration.

**How it works in practice**: You can use a pre-built parser to extract information from user input, a memory module to store and retrieve data, and a prompt generator to interact with users, all without having to build these components from scratch.

**Example code**. Let's look at an example of how you can use a pre-built parser to extract information from user input:

```python
import os
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define a Pydantic model for structured data
class FlightBooking(BaseModel):
    origin: str = Field(description="Departure city")
    destination: str = Field(description="Arrival city")
    date: str = Field(description="Flight date")

# Initialize parser
parser = PydanticOutputParser(pydantic_object=FlightBooking)

# Define the prompt template
prompt = PromptTemplate(
    template="Extract structured flight details from the following text:\n{text}\n{format_instructions}",
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Initialize Azure OpenAI LLM
llm = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    temperature=0
)

# Chain together the prompt, model, and parser
chain = prompt | llm | parser

# Invoke the chain
parsed_data = chain.invoke({"text": user_input})

print(parsed_data)
# Output: origin='New York' destination='London' date='July 15th'
```

What you can see from this example is how you can leverage a pre-built parser to extract key information from user input, such as the origin, destination, and date of a flight booking request. This modular approach allows you to focus on the high-level logic.

### Leverage Collaborative Tools

Frameworks like CrewAI and Microsoft AutoGen facilitate the creation of multiple agents that can work together.

**How teams can use these**: Teams can design agents with specific roles and tasks, enabling them to test and refine collaborative workflows and improve overall system efficiency.

**How it works in practice**: You can create a team of agents where each agent has a specialized function, such as data retrieval, analysis, or decision-making. These agents can communicate and share information to achieve a common goal, such as answering a user query or completing a task.

**Example code (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

What you see in above code is how you can create a task that involves multiple agents working together to analyze data. Each agent performs a specific function, and the task is executed by coordinating the agents to achieve the desired outcome. By creating dedicated agents with specialized roles, you can improve task efficiency and performance.

### Learn in Real-Time

Advanced frameworks provide capabilities for real-time context understanding and adaptation. 

**How teams can use these**: Teams can implement feedback loops where agents learn from interactions and adjust their behavior dynamically, leading to continuous improvement and refinement of capabilities.

**How it works in practice**: Agents can analyze user feedback, environmental data, and task outcomes to update their knowledge base, adjust decision-making algorithms, and improve performance over time. This iterative learning process enables agents to adapt to changing conditions and user preferences, enhancing overall system effectiveness.

## What are the differences between the frameworks AutoGen, Semantic Kernel and Azure AI Agent Service?

There are many ways to compare these frameworks, but let's look at some key differences in terms of their design, capabilities, and target use cases:

## AutoGen

Open-source framework developed by Microsoft Research's AI Frontiers Lab. Focuses on event-driven, distributed *agentic* applications, enabling multiple LLMs and SLMs, tools, and advanced multi-agent design patterns.

AutoGen is built around the core concept of agents, which are autonomous entities that can perceive their environment, make decisions, and take actions to achieve specific goals. Agents communicate through asynchronous messages, allowing them to work independently and in parallel, enhancing system scalability and responsiveness.

Agents are based on the [actor model](https://en.wikipedia.org/wiki/Actor_model){target="_blank"}. Which according to Wikipedia states that an actor is _the basic building block of concurrent computation. In response to a message it receives, an actor can: make local decisions, create more actors, send more messages, and determine how to respond to the next message received_.

**Use Cases**: Automating code generation, data analysis tasks, and building custom agents for planning and research functions.

Here's some important core concepts of AutoGen:

- **Agents**. An agent is a software entity that: 
  - **Communicates via messages**, these messages can be synchronous or asynchronous.
  - **Maintains its own state**, which can be modified by incoming messages.
  - **Performs actions** in response to received messages or changes in its state. These actions may modify the agent’s state and produce external effects, such as updating message logs, sending new messages, executing code, or making API calls.
    
  Here you have a short code snippet in which you create your own agent with Chat capabilities:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAssistant(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    In above code, `MyAssistant` has been created and inherits from `RoutedAgent`. It has a message handler that prints the content of the message and then sends a response using the `AssistantAgent` delegate. Especially note how we assign to `self._delegate` an instance of `AssistantAgent` which is a pre-built agent that can handle chat completions.


    Let's let AutoGen know about this agent type and kick off the program next:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Above the agents is registered with the runtime and then a message is sent to the agent resulting in the below output:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi agents**. AutoGen supports the creation of multiple agents that can work together to achieve complex tasks. Agents can communicate, share information, and coordinate their actions to solve problems more efficiently. To create a multi-agent system, you can define different types of agents with specialized functions and roles, such as data retrieval, analysis, decision-making, and user interaction. Let's see how such a creation looks like so we get a sense of it:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    Above we have a `GroupChatManager` that is registered with the runtime. This manager is responsible for coordinating the interactions between different types of agents, such as writers, illustrators, editors, and users.

- **Agent Runtime**. The framework provides a runtime environment, enabling communication between agents, manages their identities and lifecycles, and enforce security and privacy boundaries. This means that you can run your agents in a secure and controlled environment, ensuring that they can interact safely and efficiently. There are two runtimes of interest:
  - **Stand-alone runtime**. This is a good choice for single-process applications where all agents are implemented in the same programming language and runs in the same process. Here's an illustration of how it works:
  
      ![Stand-alone runtime](https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg){target="_blank"}   
Application stack

    *agents communicate via messages through the runtime, and the runtime manages the lifecycle of agents*

  - **Distributed agent runtime**, is suitable for multi-process applications where agents may be implemented in different programming languages and running on different machine. Here's an illustration of how it works:
  
      ![Distributed runtime](https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg){target="_blank"}

## Semantic Kernel + Agent Framework

Semantic Kernel consists of two things, the Semantic Kernel Agent Framework and the Semantic Kernel itself.

Let's first talk about the Semantic Kernel. It has the following core concepts:

- **Connections**: This is an interface with external AI services and data sources.

    ```csharp
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    Here you have a simple example of how you can create a kernel and add a chat completion service. Semantic Kernel creates a connection to an external AI service, in this case, Azure OpenAI Chat Completion.

- **Plugins**: Encapsulate functions that an application can use. There are both ready-made plugins and plugins you can create yourself. There's a concept here called "Semantic functions". What makes it semantic is that you provide it semantic information that helps Semantic Kernel figure out that this function needs to be called. Here's an example:

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // Register the function
    kernel.CreateSemanticFunction(
        promptTemplate: skPrompt,
        functionName: "SummarizeText",
        pluginName: "SemanticFunctions"
    );
    ```

    Here, you first have a template prompt `skPrompt` that leaves room for the user to input text, `$userInput`. Then you register the function `SummarizeText` with the plugin `SemanticFunctions`. Note the name of the function that helps Semantic Kernel understand what the function does and when it should be called.

- **Native function**: There's also native functions that the framework can call directly to carry out the task. Here's an example of such a function retrieving the content from a file:

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";
    
    var nativeFunctions = new NativeFunctions();
    kernel.ImportFunctions(nativeFunctions, plugInName);
    ```

- **Planner**: The planner orchestrates execution plans and strategies based on user input. The idea is to express how things should be carried out which then surveys as an instruction for Semantic Kernel to follow. It then invoke the necessary functions to carry out the task. Here' an example of such a plan:

    ```csharp
    string planDefinition = "Read content from a local file and summarize the content.";
    SequentialPlanner sequentialPlanner = new SequentialPlanner(kernel);
    
    string assetsFolder = @"../../assets";
    string fileName = Path.Combine(assetsFolder,"docs","06_SemanticKernel", "aci_documentation.txt");
    
    ContextVariables contextVariables = new ContextVariables();
    contextVariables.Add("fileName", fileName);
    
    var customPlan = await sequentialPlanner.CreatePlanAsync(planDefinition);
    
    // Execute the plan
    KernelResult kernelResult = await kernel.RunAsync(contextVariables, customPlan);
    Console.WriteLine($"Summarization: {kernelResult.GetValue<string>()}");
    ```

    Note especially `planDefinition` which is a simple instruction for the planner to follow. The appropriate functions are then called based on this plan, in this case our semantic function `SummarizeText` and the native function `RetrieveLocalFile`.
- **Memory**:  Abstracts and simplifies context management for AI apps. The idea with memory is that this is something the LLM should know about. You can store this information in a vector store which ends up being an in-memory database or a vector database or similar. Here's an example of a very simplified scenario where *facts* are added to the memory:

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

    These facts are then stored in the memory collection `SummarizedAzureDocs`. This is a very simplified example, but you can see how you can store information in the memory for the LLM to use.

So that's the basics of the Semantic Kernel framework, what about the Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service is a more recent addition, introduced at Microsoft Ignite 2024. It allows for the development and deployment of AI agents with more flexible models, such as directly calling open-source LLMs like Llama 3, Mistral, and Cohere.

Azure AI Agent Service provides stronger enterprise security mechanisms and data storage methods, making it suitable for enterprise applications. 

It works out-of-the-box with multi-agent orchestration frameworks like AutoGen and Semantic Kernel.

This service is currently in Public Preview and supports Python and C# for building agents

### Core concepts

Azure AI Agent Service has the following core concepts:

- **Agent**. Azure AI Agent Service integrates with Azure AI Foundry. Within AI Foundry, an AI Agent acts as a "smart" microservice that can be used to answer questions (RAG), perform actions, or completely automate workflows. It achieves this by combining the power of generative AI models with tools that allow it to access and interact with real-world data sources. Here's an example of an agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In this example, an agent is created with the model `gpt-4o-mini`, a name `my-agent`, and instructions `You are helpful agent`. The agent is equipped with tools and resources to perform code interpretation tasks.

- **Thread and messages**. The thread is another important concept. It represents a conversation or interaction between an agent and a user. Threads can be used to track the progress of a conversation, store context information, and manage the state of the interaction. Here's an example of a thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    In the above code, a thread is created. Thereafter, a message is sent to the thread. By calling `create_and_process_run`, the agent is asked to perform work on the thread. Finally, the messages are fetched and logged to see the agent's response. The messages indicate the progress of the conversation between the user and the agent. It's also important to understand that the messages can be of different types such as text, image, or file, that is the agents work has resulted in for example an image or a text response for example. As a developer, you can then use this information to further process the response or present it to the user.

- **Integrates with other AI frameworks**. Azure AI Agent service can interact with other frameworks like AutoGen and Semantic Kernel, which means you can build part of your app in one of these frameworks and for example using the Agent service as an orchestrator or you can build everything in the Agent service.

**Use Cases**: Azure AI Agent Service is designed for enterprise applications that require secure, scalable, and flexible AI agent deployment.

## What's the difference between these frameworks?

It does sound like there is a lot of overlap between these frameworks, but there are some key differences in terms of their design, capabilities, and target use cases:

- **AutoGen**: Focuses on event-driven, distributed agentic applications, enabling multiple LLMs and SLMs, tools, and advanced multi-agent design patterns.
- **Semantic Kernel**: Focuses on understanding and generating human-like text content by capturing deeper semantic meanings. It is designed to automate complex workflows and initiate tasks based on project goals.
- **Azure AI Agent Service**: Provides more flexible models, such as directly calling open-source LLMs like Llama 3, Mistral, and Cohere. It offers stronger enterprise security mechanisms and data storage methods, making it suitable for enterprise applications.

Still not sure which one to choose?

### Use Cases

Let's see if we can help you by going through some common use cases:

> Q: My team is working on a project that involves automating code generation and data analysis tasks. Which framework should we use?
>
>A: AutoGen would be a good choice for this scenario, as it focuses on event-driven, distributed agentic applications and supports advanced multi-agent design patterns.

> Q: What makes AutoGen a better choice than Semantic Kernel and Azure AI Agent Service for this use case?
>
> A: AutoGen is specifically designed for event-driven, distributed agentic applications, making it well-suited for automating code generation and data analysis tasks. It provides the necessary tools and capabilities to build complex multi-agent systems efficiently.

>Q: Sounds like Azure AI Agent Service could work here too, it tools like code generation and more?
>
> A: Yes, Azure AI Agent Service also supports code generation and data analysis tasks, but it may be more suitable for enterprise applications that require secure, scalable, and flexible AI agent deployment. AutoGen is more focused on event-driven, distributed agentic applications and advanced multi-agent design patterns.

> Q: so you are saying if I want to go enterprise, I should go with Azure AI Agent Service?
>
> A: Yes, Azure AI Agent Service is designed for enterprise applications that require secure, scalable, and flexible AI agent deployment. It offers stronger enterprise security mechanisms and data storage methods, making it suitable for enterprise use cases.

Let's summarize the key differences in a table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| AutoGen | Event-driven, distributed agentic applications | Agents, Personas, Functions, Data | Code generation, data analysis tasks |
| Semantic Kernel | Understanding and generating human-like text content | Agents, Modular Components, Collaboration | Natural language understanding, content generation |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

What's the ideal use case for each of these frameworks?

- **AutoGen**: Event-driven, distributed agentic applications, advanced multi-agent design patterns. Ideal for automating code generation, data analysis tasks.
- **Semantic Kernel**: Understanding and generating human-like text content, automating complex workflows, initiating tasks based on project goals. Ideal for natural language understanding, content generation. 
- **Azure AI Agent Service**: Flexible models, enterprise security mechanisms, data storage methods. Ideal for secure, scalable, and flexible AI agent deployment in enterprise applications.

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?

The answer is yes, you can integrate your existing Azure ecosystem tools directly with Azure AI Agent Service especially, this because it has been built to work seamlessly with other Azure services. You could for example integrate Bing, Azure AI Search, and Azure Functions. There's also deep integration with Azure AI Foundry.

For AutoGen and Semantic Kernel, you can also integrate with Azure services, but it may require you to call the Azure services from your code. Another way to integrate is to use the Azure SDKs to interact with Azure services from your agents. Additionally, like was mentioned, you can use Azure AI Agent Service as an orchestrator for your agents built in AutoGen or Semantic Kernel which would give easy access to the Azure ecosystem.

## References

- [1] - [Azure Agent Service](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357){target="_blank"}
- [2] - [Semantic Kernel and AutoGen](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/){target="_blank"}
- [3] - [Semantic Kernel Agent Framework](https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp){target="_blank"}
- [4] - [Azure AI Agent service](https://learn.microsoft.com/azure/ai-services/agents/overview){target="_blank"}
- [5] - [Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution](https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121){target="_blank"}
