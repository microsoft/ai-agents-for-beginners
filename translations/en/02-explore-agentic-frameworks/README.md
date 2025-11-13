<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T10:47:11+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "en"
}
-->
[![Exploring AI Agent Frameworks](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.en.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Click the image above to view the video of this lesson)_

# Explore AI Agent Frameworks

AI agent frameworks are software platforms designed to simplify the creation, deployment, and management of AI agents. These frameworks provide developers with pre-built components, abstractions, and tools that streamline the development of complex AI systems.

These frameworks help developers focus on the unique aspects of their applications by providing standardized approaches to common challenges in AI agent development. They enhance scalability, accessibility, and efficiency in building AI systems.

## Introduction 

This lesson will cover:

- What AI Agent Frameworks are and what they enable developers to achieve.
- How teams can use these frameworks to quickly prototype, iterate, and improve their agent’s capabilities.
- The differences between frameworks and tools created by Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, and <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>.
- Whether you can integrate your existing Azure ecosystem tools directly or need standalone solutions.
- What Azure AI Agents service is and how it can help you.

## Learning goals

The goals of this lesson are to help you understand:

- The role of AI Agent Frameworks in AI development.
- How to leverage AI Agent Frameworks to build intelligent agents.
- Key capabilities enabled by AI Agent Frameworks.
- The differences between AutoGen, Semantic Kernel, and Azure AI Agent Service.

## What are AI Agent Frameworks and what do they enable developers to do?

Traditional AI frameworks can help you integrate AI into your apps and improve them in the following ways:

- **Personalization**: AI can analyze user behavior and preferences to provide personalized recommendations, content, and experiences.
Example: Streaming services like Netflix use AI to suggest movies and shows based on viewing history, enhancing user engagement and satisfaction.
- **Automation and Efficiency**: AI can automate repetitive tasks, streamline workflows, and improve operational efficiency.
Example: Customer service apps use AI-powered chatbots to handle common inquiries, reducing response times and freeing up human agents for more complex issues.
- **Enhanced User Experience**: AI can improve the overall user experience by providing intelligent features such as voice recognition, natural language processing, and predictive text.
Example: Virtual assistants like Siri and Google Assistant use AI to understand and respond to voice commands, making it easier for users to interact with their devices.

### That all sounds great, right? So why do we need AI Agent Frameworks?

AI Agent frameworks go beyond traditional AI frameworks. They are designed to enable the creation of intelligent agents that can interact with users, other agents, and the environment to achieve specific goals. These agents can exhibit autonomous behavior, make decisions, and adapt to changing conditions. Let's look at some key capabilities enabled by AI Agent Frameworks:

- **Agent Collaboration and Coordination**: Enable the creation of multiple AI agents that can work together, communicate, and coordinate to solve complex tasks.
- **Task Automation and Management**: Provide mechanisms for automating multi-step workflows, task delegation, and dynamic task management among agents.
- **Contextual Understanding and Adaptation**: Equip agents with the ability to understand context, adapt to changing environments, and make decisions based on real-time information.

In summary, agents allow you to do more, take automation to the next level, and create more intelligent systems that can adapt and learn from their environment.

## How to quickly prototype, iterate, and improve the agent’s capabilities?

This is a fast-moving landscape, but there are some common features across most AI Agent Frameworks that can help you quickly prototype and iterate, namely modular components, collaborative tools, and real-time learning. Let's dive into these:

- **Use Modular Components**: AI SDKs offer pre-built components such as AI and Memory connectors, function calling using natural language or code plugins, prompt templates, and more.
- **Leverage Collaborative Tools**: Design agents with specific roles and tasks, enabling them to test and refine collaborative workflows.
- **Learn in Real-Time**: Implement feedback loops where agents learn from interactions and adjust their behavior dynamically.

### Use Modular Components

SDKs like Microsoft Semantic Kernel and LangChain offer pre-built components such as AI connectors, prompt templates, and memory management.

**How teams can use these**: Teams can quickly assemble these components to create a functional prototype without starting from scratch, allowing for rapid experimentation and iteration.

**How it works in practice**: You can use a pre-built parser to extract information from user input, a memory module to store and retrieve data, and a prompt generator to interact with users, all without having to build these components from scratch.

**Example code**. Let's look at examples of how you can use a pre-built AI Connector with Semantic Kernel Python and .Net that uses auto-function calling to have the model respond to user input:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

What you can see from this example is how you can leverage a pre-built parser to extract key information from user input, such as the origin, destination, and date of a flight booking request. This modular approach allows you to focus on the high-level logic.

### Leverage Collaborative Tools

Frameworks like CrewAI, Microsoft AutoGen, and Semantic Kernel facilitate the creation of multiple agents that can work together.

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

What you see in the previous code is how you can create a task that involves multiple agents working together to analyze data. Each agent performs a specific function, and the task is executed by coordinating the agents to achieve the desired outcome. By creating dedicated agents with specialized roles, you can improve task efficiency and performance.

### Learn in Real-Time

Advanced frameworks provide capabilities for real-time context understanding and adaptation.

**How teams can use these**: Teams can implement feedback loops where agents learn from interactions and adjust their behavior dynamically, leading to continuous improvement and refinement of capabilities.

**How it works in practice**: Agents can analyze user feedback, environmental data, and task outcomes to update their knowledge base, adjust decision-making algorithms, and improve performance over time. This iterative learning process enables agents to adapt to changing conditions and user preferences, enhancing overall system effectiveness.

## What are the differences between the frameworks AutoGen, Semantic Kernel, and Azure AI Agent Service?

There are many ways to compare these frameworks, but let's look at some key differences in terms of their design, capabilities, and target use cases:

## AutoGen

AutoGen is an open-source framework developed by Microsoft Research's AI Frontiers Lab. It focuses on event-driven, distributed *agentic* applications, enabling multiple LLMs and SLMs, tools, and advanced multi-agent design patterns.

AutoGen is built around the core concept of agents, which are autonomous entities that can perceive their environment, make decisions, and take actions to achieve specific goals. Agents communicate through asynchronous messages, allowing them to work independently and in parallel, enhancing system scalability and responsiveness.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agents are based on the actor model</a>. According to Wikipedia, an actor is _the basic building block of concurrent computation. In response to a message it receives, an actor can: make local decisions, create more actors, send more messages, and determine how to respond to the next message received_.

**Use Cases**: Automating code generation, data analysis tasks, and building custom agents for planning and research functions.

Here are some important core concepts of AutoGen:

- **Agents**. An agent is a software entity that:
  - **Communicates via messages**, these messages can be synchronous or asynchronous.
  - **Maintains its own state**, which can be modified by incoming messages.
  - **Performs actions** in response to received messages or changes in its state. These actions may modify the agent’s state and produce external effects, such as updating message logs, sending new messages, executing code, or making API calls.
    
  Here you have a short code snippet in which you create your own agent with Chat capabilities:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
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
    
    In the previous code, `MyAgent` has been created and inherits from `RoutedAgent`. It has a message handler that prints the content of the message and then sends a response using the `AssistantAgent` delegate. Especially note how we assign to `self._delegate` an instance of `AssistantAgent` which is a pre-built agent that can handle chat completions.


    Let's let AutoGen know about this agent type and kick off the program next:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    In the previous code the agents are registered with the runtime and then a message is sent to the agent resulting in the following output:

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

    In the previous code we have a `GroupChatManager` that is registered with the runtime. This manager is responsible for coordinating the interactions between different types of agents, such as writers, illustrators, editors, and users.

- **Agent Runtime**. The framework provides a runtime environment, enabling communication between agents, manages their identities and lifecycles, and enforces security and privacy boundaries. This means that you can run your agents in a secure and controlled environment, ensuring that they can interact safely and efficiently. There are two runtimes of interest:
  - **Stand-alone runtime**. This is a good choice for single-process applications where all agents are implemented in the same programming language and run in the same process. Here's an illustration of how it works:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Stand-alone runtime</a>   
Application stack

    *agents communicate via messages through the runtime, and the runtime manages the lifecycle of agents*

  - **Distributed agent runtime**, is suitable for multi-process applications where agents may be implemented in different programming languages and running on different machines. Here's an illustration of how it works:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Distributed runtime</a>

## Semantic Kernel + Agent Framework

Semantic Kernel is an enterprise-ready AI Orchestration SDK. It consists of AI and memory connectors, along with an Agent Framework.

Let's first cover some core components:

- **AI Connectors**: This is an interface with external AI services and data sources for use in both Python and C#.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
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

- **Plugins**: These encapsulate functions that an application can use. There are both ready-made plugins and custom ones you can create. A related concept is "prompt functions." Instead of providing natural language cues for function invocation, you broadcast certain functions to the model. Based on the current chat context, the model may choose to call one of these functions to complete a request or query. Here's an example:

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    Here, you first have a template prompt `skPrompt` that leaves room for the user to input text, `$userInput`. Then you create the kernel function `SummarizeText` and then import it into the kernel with the plugin name `SemanticFunctions`. Note the name of the function that helps Semantic Kernel understand what the function does and when it should be called.

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

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```

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

These facts are then stored in the memory collection `SummarizedAzureDocs`. This is a very simplified example, but it demonstrates how you can store information in memory for the LLM to utilize.

So that's the basics of the Semantic Kernel framework, but what about the Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service is a newer addition, introduced at Microsoft Ignite 2024. It enables the development and deployment of AI agents with more flexible models, such as directly calling open-source LLMs like Llama 3, Mistral, and Cohere.

Azure AI Agent Service offers enhanced enterprise security mechanisms and data storage methods, making it ideal for enterprise applications.

It works seamlessly with multi-agent orchestration frameworks like AutoGen and Semantic Kernel.

This service is currently in Public Preview and supports Python and C# for building agents.

Using Semantic Kernel Python, we can create an Azure AI Agent with a user-defined plugin:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Core concepts

Azure AI Agent Service has the following core concepts:

- **Agent**. Azure AI Agent Service integrates with Azure AI Foundry. Within AI Foundry, an AI Agent functions as a "smart" microservice that can answer questions (RAG), perform actions, or fully automate workflows. It accomplishes this by combining the capabilities of generative AI models with tools that allow it to access and interact with real-world data sources. Here's an example of an agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In this example, an agent is created using the model `gpt-4o-mini`, named `my-agent`, with instructions `You are helpful agent`. The agent is equipped with tools and resources to perform code interpretation tasks.

- **Thread and messages**. The thread is another key concept. It represents a conversation or interaction between an agent and a user. Threads can be used to track the progress of a conversation, store context information, and manage the state of the interaction. Here's an example of a thread:

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

    In the previous code, a thread is created. Then, a message is sent to the thread. By calling `create_and_process_run`, the agent is instructed to perform work on the thread. Finally, the messages are retrieved and logged to observe the agent's response. The messages reflect the progress of the conversation between the user and the agent. It's also important to note that messages can be of various types, such as text, image, or file, representing the agent's output—for example, an image or a text response. As a developer, you can use this information to further process the response or present it to the user.

- **Integrates with other AI frameworks**. Azure AI Agent Service can interact with other frameworks like AutoGen and Semantic Kernel, allowing you to build part of your application in one of these frameworks and, for example, use the Agent Service as an orchestrator, or you can build everything within the Agent Service.

**Use Cases**: Azure AI Agent Service is designed for enterprise applications requiring secure, scalable, and flexible AI agent deployment.

## What's the difference between these frameworks?

It may seem like there is significant overlap between these frameworks, but there are key differences in their design, capabilities, and target use cases:

- **AutoGen**: An experimentation framework focused on cutting-edge research in multi-agent systems. It's ideal for experimenting and prototyping advanced multi-agent systems.
- **Semantic Kernel**: A production-ready agent library for building enterprise agentic applications. It emphasizes event-driven, distributed agentic applications, enabling multiple LLMs and SLMs, tools, and single/multi-agent design patterns.
- **Azure AI Agent Service**: A platform and deployment service within Azure Foundry for agents. It provides connectivity to services supported by Azure Foundry, such as Azure OpenAI, Azure AI Search, Bing Search, and code execution.

Still unsure which one to choose?

### Use Cases

Let's explore some common use cases to help you decide:

> Q: I'm experimenting, learning, and building proof-of-concept agent applications, and I want to be able to build and experiment quickly.

> A: AutoGen would be a good choice for this scenario, as it focuses on event-driven, distributed agentic applications and supports advanced multi-agent design patterns.

> Q: What makes AutoGen a better choice than Semantic Kernel and Azure AI Agent Service for this use case?

> A: AutoGen is specifically designed for event-driven, distributed agentic applications, making it well-suited for automating code generation and data analysis tasks. It provides the necessary tools and capabilities to efficiently build complex multi-agent systems.

> Q: Sounds like Azure AI Agent Service could work here too; it has tools for code generation and more?

> A: Yes, Azure AI Agent Service is a platform service for agents and includes built-in capabilities for multiple models, Azure AI Search, Bing Search, and Azure Functions. It simplifies building agents in the Foundry Portal and deploying them at scale.

> Q: I'm still confused; just give me one option.

> A: A great choice is to build your application in Semantic Kernel first and then use Azure AI Agent Service to deploy your agent. This approach allows you to easily persist your agents while leveraging the power to build multi-agent systems in Semantic Kernel. Additionally, Semantic Kernel has a connector in AutoGen, making it easy to use both frameworks together.

Let's summarize the key differences in a table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| AutoGen | Event-driven, distributed agentic applications | Agents, Personas, Functions, Data | Code generation, data analysis tasks |
| Semantic Kernel | Understanding and generating human-like text content | Agents, Modular Components, Collaboration | Natural language understanding, content generation |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

What's the ideal use case for each of these frameworks?

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?

The answer is yes, you can integrate your existing Azure ecosystem tools directly with Azure AI Agent Service, as it has been designed to work seamlessly with other Azure services. For example, you could integrate Bing, Azure AI Search, and Azure Functions. There's also deep integration with Azure AI Foundry.

For AutoGen and Semantic Kernel, you can also integrate with Azure services, but it may require you to call the Azure services from your code. Another way to integrate is to use the Azure SDKs to interact with Azure services from your agents. Additionally, as mentioned earlier, you can use Azure AI Agent Service as an orchestrator for your agents built in AutoGen or Semantic Kernel, providing easy access to the Azure ecosystem.

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Got More Questions about AI Agent Frameworks?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to connect with other learners, attend office hours, and get your AI Agents questions answered.

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel and AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent solution</a>

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->