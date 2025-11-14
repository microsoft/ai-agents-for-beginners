<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86b9c2b24da3b3e61711182ffa72601c",
  "translation_date": "2025-11-11T14:15:10+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "pcm"
}
-->
[![Exploring AI Agent Frameworks](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.pcm.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Click di image wey dey up to watch di video for dis lesson)_

# Explore AI Agent Frameworks

AI agent frameworks na software platforms wey dey make am easy to create, deploy, and manage AI agents. Dis frameworks dey give developers ready-made components, tools, and ways wey go make di work of building complex AI systems no too hard.

Dis frameworks dey help developers focus on di special things wey dem wan do for dia apps by providing standard ways to handle di common wahala wey dey for AI agent development. E dey make am easy to scale, use, and build AI systems wey go work well.

## Introduction 

Dis lesson go cover:

- Wetin AI Agent Frameworks be and wetin dem fit help developers achieve?
- How teams fit use dem to quickly prototype, change, and improve di agent’s capabilities?
- Wetin be di difference between di frameworks and tools wey Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, and <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> create?
- I fit connect my existing Azure tools directly, or I go need standalone solutions?
- Wetin Azure AI Agents service be and how e dey help me?

## Learning goals

Di goals for dis lesson na to help you sabi:

- Di role wey AI Agent Frameworks dey play for AI development.
- How to use AI Agent Frameworks to build smart agents.
- Di key things wey AI Agent Frameworks fit do.
- Di difference between AutoGen, Semantic Kernel, and Azure AI Agent Service.

## Wetin AI Agent Frameworks be and wetin dem fit help developers do?

Di normal AI Frameworks fit help you put AI for your apps and make di apps better for di following ways:

- **Personalization**: AI fit check how users dey behave and wetin dem like to give dem recommendations, content, and experience wey fit dem.
Example: Streaming services like Netflix dey use AI to suggest movies and shows based on wetin person don watch before, e dey make users enjoy di app more.
- **Automation and Efficiency**: AI fit help automate work wey dey repeat, make workflows smooth, and make operations dey efficient.
Example: Customer service apps dey use AI chatbots to answer common questions, e dey reduce how long e go take to reply and e dey free human agents to handle di hard questions.
- **Better User Experience**: AI fit make di user experience better by adding smart features like voice recognition, natural language processing, and predictive text.
Example: Virtual assistants like Siri and Google Assistant dey use AI to understand and reply voice commands, e dey make am easy for users to use dia devices.

### E sound good abi? So why we need AI Agent Framework?

AI Agent frameworks dey do pass di normal AI frameworks. Dem dey help create smart agents wey fit interact with users, other agents, and di environment to achieve specific goals. Dis agents fit act on dia own, make decisions, and change as di situation dey change. Make we look di key things wey AI Agent Frameworks fit do:

- **Agent Collaboration and Coordination**: Dem fit help create plenty AI agents wey go work together, talk, and plan to solve hard tasks.
- **Task Automation and Management**: Dem dey provide ways to automate work wey get steps, share tasks, and manage tasks wey dey change among agents.
- **Contextual Understanding and Adaptation**: Dem dey give agents di ability to understand wetin dey happen, change as di environment dey change, and make decisions based on wetin dey happen at di moment.

So to summarize, agents dey help you do more, take automation to di next level, and create smarter systems wey fit learn and change based on wetin dey happen.

## How to quickly prototype, change, and improve di agent’s capabilities?

Dis area dey move fast, but some things dey common for most AI Agent Frameworks wey fit help you quickly prototype and change, like module components, tools for collaboration, and real-time learning. Make we look dem:

- **Use Modular Components**: AI SDKs dey provide ready-made components like AI and Memory connectors, function calling with natural language or code plugins, prompt templates, and more.
- **Leverage Collaborative Tools**: Design agents wey get specific roles and tasks, e go help test and improve how dem dey work together.
- **Learn in Real-Time**: Put feedback loops wey go make agents learn from interactions and change how dem dey behave.

### Use Modular Components

SDKs like Microsoft Semantic Kernel and LangChain dey provide ready-made components like AI connectors, prompt templates, and memory management.

**How teams fit use dem**: Teams fit quickly join dis components to create prototype wey dey work without starting from scratch, e go make dem fit test and change fast.

**How e dey work for real life**: You fit use ready-made parser to get information from user input, memory module to store and bring back data, and prompt generator to interact with users, all without building dem from scratch.

**Example code**. Make we look example of how you fit use ready-made AI Connector with Semantic Kernel Python and .Net wey dey use auto-function calling to make di model reply user input:

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

From dis example, you fit see how you fit use ready-made parser to get key information from user input, like di origin, destination, and date for flight booking request. Dis modular way dey help you focus on di main logic.

### Leverage Collaborative Tools

Frameworks like CrewAI, Microsoft AutoGen, and Semantic Kernel dey help create plenty agents wey fit work together.

**How teams fit use dem**: Teams fit design agents wey get specific roles and tasks, e go help test and improve how dem dey work together and make di system dey efficient.

**How e dey work for real life**: You fit create team of agents wey each one get special work, like data retrieval, analysis, or decision-making. Dis agents fit talk and share information to achieve one goal, like answer user question or complete task.

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

For di code wey dey up, you fit see how you fit create task wey involve plenty agents wey dey work together to analyze data. Each agent dey do one specific work, and di task dey happen by coordinating di agents to achieve di goal. By creating agents wey get special roles, you fit make di task dey efficient and perform well.

### Learn in Real-Time

Advanced frameworks dey provide ways for real-time understanding and adaptation.

**How teams fit use dem**: Teams fit put feedback loops wey go make agents learn from interactions and change how dem dey behave, e go lead to continuous improvement.

**How e dey work for real life**: Agents fit check user feedback, environmental data, and task results to update dia knowledge, change how dem dey make decisions, and perform better over time. Dis learning process dey help agents adapt to wetin dey happen and wetin users want, e dey make di system work better.

## Wetin be di difference between di frameworks AutoGen, Semantic Kernel and Azure AI Agent Service?

Plenty ways dey to compare dis frameworks, but make we look di main difference for dia design, wetin dem fit do, and di kind work dem dey good for:

## AutoGen

AutoGen na open-source framework wey Microsoft Research's AI Frontiers Lab develop. E dey focus on event-driven, distributed *agentic* applications, wey dey allow plenty LLMs and SLMs, tools, and advanced multi-agent design patterns.

AutoGen dey work around di idea of agents, wey be independent entities wey fit understand dia environment, make decisions, and take actions to achieve specific goals. Agents dey talk through asynchronous messages, e dey make dem work on dia own and at di same time, e dey make di system scale and respond well.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agents dey based on di actor model</a>. According to Wikipedia, actor na _di basic building block of concurrent computation. When actor receive message, e fit: make local decisions, create more actors, send more messages, and decide how e go reply di next message wey e receive_.

**Use Cases**: Automating code generation, data analysis tasks, and building custom agents for planning and research functions.

Here be di main ideas for AutoGen:

- **Agents**. Agent na software entity wey:
  - **Dey talk through messages**, di messages fit be synchronous or asynchronous.
  - **Get dia own state**, wey fit change based on di messages wey dem receive.
  - **Dey act** based on di messages wey dem receive or di changes for dia state. Di actions fit change di agent’s state and fit do things like update message logs, send new messages, run code, or make API calls.
    
  Here be short code example wey show how you fit create your own agent wey get Chat capabilities:

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
    
    For di code wey dey up, `MyAgent` don dey created and e dey inherit from `RoutedAgent`. E get message handler wey dey print di content of di message and e dey send reply using di `AssistantAgent` delegate. Note how we assign `self._delegate` to instance of `AssistantAgent` wey be ready-made agent wey fit handle chat completions.

    Make we let AutoGen sabi dis agent type and start di program:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    For di code wey dey up, di agents don dey registered with di runtime and message don dey sent to di agent wey result for di following output:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi agents**. AutoGen dey support creation of plenty agents wey fit work together to achieve hard tasks. Agents fit talk, share information, and plan dia actions to solve problems well. To create multi-agent system, you fit define different types of agents wey get special work and roles, like data retrieval, analysis, decision-making, and user interaction. Make we see how dis creation dey look like:

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

    For di code wey dey up, we get `GroupChatManager` wey don dey registered with di runtime. Dis manager dey responsible for coordinating di interactions between different types of agents, like writers, illustrators, editors, and users.

- **Agent Runtime**. Di framework dey provide runtime environment, e dey allow agents to talk, manage dia identities and lifecycles, and make sure security and privacy dey. Dis mean say you fit run your agents for safe and controlled environment, e go make dem fit interact well. Two runtimes dey important:
  - **Stand-alone runtime**. Dis one dey good for single-process applications wey all agents dey use di same programming language and dey run for di same process. Here be illustration of how e dey work:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Stand-alone runtime</a>   
Application stack

    *agents dey talk through messages via di runtime, and di runtime dey manage di lifecycle of agents*

  - **Distributed agent runtime**, e dey good for multi-process applications wey agents fit dey use different programming languages and dey run for different machines. Here be illustration of how e dey work:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Distributed runtime</a>

## Semantic Kernel + Agent Framework

Semantic Kernel na enterprise-ready AI Orchestration SDK. E get AI and memory connectors, plus Agent Framework.

Make we first talk about di main components:

- **AI Connectors**: Dis one dey connect external AI services and data sources for use for both Python and C#.

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

    Here be simple example of how you fit create kernel and add chat completion service. Semantic Kernel dey create connection to external AI service, for dis case, Azure OpenAI Chat Completion.

- **Plugins**: Dis one dey package functions wey application fit use. Dem get ready-made plugins and custom ones wey you fit create. One related idea na "prompt functions." Instead of giving natural language cues for function invocation, you dey broadcast some functions to di model. Based on di current chat context, di model fit decide to call one of dis functions to complete request or query. Here be example:

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

    Here, you first get template prompt `skPrompt` wey leave space for user to input text, `$userInput`. Then you create di kernel function `SummarizeText` and then import am into di kernel with di plugin name `SemanticFunctions`. Note di name of di function wey dey help Semantic Kernel understand wetin di function dey do and when e suppose call am.

- **Native function**: Di framework fit call native functions directly to carry out di task. Here be example of such function wey dey retrieve content from file:

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

- **Memory**: E dey simplify how AI apps dey manage context. Di idea for memory na say dis na wetin di LLM suppose sabi. You fit store dis information for vector store wey fit be in-memory database or vector database or similar. Here be example of simple scenario wey *facts* dey added to di memory:

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

Dis facts dem go dey store for memory collection wey dem call `SummarizedAzureDocs`. Dis na one simple example, but e show how you fit store info for memory wey LLM go use.

So na di basics of Semantic Kernel framework be dis, wetin we go talk about di Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service na new thing wey dem introduce for Microsoft Ignite 2024. E dey allow people develop and deploy AI agents wey get more flexible models, like to call open-source LLMs like Llama 3, Mistral, and Cohere directly.

Azure AI Agent Service dey provide strong enterprise security and data storage methods, wey make am good for enterprise applications.

E dey work straight out-of-the-box with multi-agent orchestration frameworks like AutoGen and Semantic Kernel.

Dis service dey Public Preview now and e dey support Python and C# to build agents.

With Semantic Kernel Python, we fit create Azure AI Agent wey get user-defined plugin:

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

Azure AI Agent Service get di following core concepts:

- **Agent**. Azure AI Agent Service dey work with Azure AI Foundry. Inside AI Foundry, AI Agent dey act like "smart" microservice wey fit answer questions (RAG), do actions, or automate workflows completely. E dey do dis by combining di power of generative AI models with tools wey allow am access and interact with real-world data sources. Example of agent na dis:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    For dis example, dem create agent wey get model `gpt-4o-mini`, name `my-agent`, and instructions `You are helpful agent`. Di agent get tools and resources to do code interpretation tasks.

- **Thread and messages**. Thread na another important concept. E represent conversation or interaction between agent and user. Threads fit dey used to track di progress of conversation, store context info, and manage di state of di interaction. Example of thread na dis:

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

    For di code wey dem show before, dem create thread. After dat, dem send message to di thread. When dem call `create_and_process_run`, di agent dey asked to do work for di thread. Finally, dem fetch and log di messages to see di agent response. Di messages dey show di progress of di conversation between di user and di agent. E important to understand say di messages fit dey different types like text, image, or file, wey mean say di agent work fit result in image or text response. As developer, you fit use dis info to process di response or show am to di user.

- **Integrates with other AI frameworks**. Azure AI Agent Service fit interact with other frameworks like AutoGen and Semantic Kernel, wey mean say you fit build part of your app for one of di frameworks and use di Agent Service as orchestrator or build everything for di Agent Service.

**Use Cases**: Azure AI Agent Service na for enterprise applications wey need secure, scalable, and flexible AI agent deployment.

## Wetin be di difference between dis frameworks?

E be like say di frameworks get plenty similarities, but dem get key differences for di way dem dey designed, wetin dem fit do, and di kind use cases dem dey target:

- **AutoGen**: Na experimentation framework wey dey focus on advanced research for multi-agent systems. E dey good for experiment and prototype sophisticated multi-agent systems.
- **Semantic Kernel**: Na production-ready agent library to build enterprise agentic applications. E dey focus on event-driven, distributed agentic applications, wey dey enable multiple LLMs and SLMs, tools, and single/multi-agent design patterns.
- **Azure AI Agent Service**: Na platform and deployment service for Azure Foundry agents. E dey offer connectivity to services wey Azure Foundry support like Azure OpenAI, Azure AI Search, Bing Search, and code execution.

Still dey confused about which one to choose?

### Use Cases

Make we try help you by going through some common use cases:

> Q: I dey experiment, learn, and dey build proof-of-concept agent applications, and I want make I fit build and experiment fast
>

>A: AutoGen go be better choice for dis scenario, as e dey focus on event-driven, distributed agentic applications and e dey support advanced multi-agent design patterns.

> Q: Wetin make AutoGen better pass Semantic Kernel and Azure AI Agent Service for dis use case?
>
> A: AutoGen dey specially designed for event-driven, distributed agentic applications, wey make am good for automating code generation and data analysis tasks. E dey provide di tools and capabilities wey you need to build complex multi-agent systems well.

>Q: E be like say Azure AI Agent Service fit work for dis use case too, e get tools for code generation and more?

>
> A: Yes, Azure AI Agent Service na platform service for agents and e get built-in capabilities for multiple models, Azure AI Search, Bing Search, and Azure Functions. E dey make am easy to build your agents for di Foundry Portal and deploy dem at scale.

> Q: I still dey confused, just give me one option
>
> A: Di best choice na to build your application for Semantic Kernel first, then use Azure AI Agent Service to deploy your agent. Dis approach go allow you persist your agents easily while you dey use di power to build multi-agent systems for Semantic Kernel. Plus, Semantic Kernel get connector for AutoGen, wey make am easy to use di two frameworks together.

Make we summarize di key differences for table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| AutoGen | Event-driven, distributed agentic applications | Agents, Personas, Functions, Data | Code generation, data analysis tasks |
| Semantic Kernel | Understanding and generating human-like text content | Agents, Modular Components, Collaboration | Natural language understanding, content generation |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

Wetin be di ideal use case for each of dis frameworks?

## Fit I integrate my existing Azure ecosystem tools directly, or I need standalone solutions?

Di answer na yes, you fit integrate your existing Azure ecosystem tools directly with Azure AI Agent Service especially, because e dey built to work well with other Azure services. You fit integrate Bing, Azure AI Search, and Azure Functions. E also get deep integration with Azure AI Foundry.

For AutoGen and Semantic Kernel, you fit also integrate with Azure services, but e fit require you to call di Azure services from your code. Another way to integrate na to use di Azure SDKs to interact with Azure services from your agents. Plus, like dem talk before, you fit use Azure AI Agent Service as orchestrator for your agents wey you build for AutoGen or Semantic Kernel, wey go make am easy to access di Azure ecosystem.

### Get More Questions about AI Agent Frameworks?

Join di [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet other learners, attend office hours, and get answers to your AI Agents questions.

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel and AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution</a>

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am accurate, abeg make you sabi say transle-shon wey machine do fit get mistake or no dey correct well. Di original dokyument for im native language na di one wey you go take as di correct source. For important mata, e good make you use professional human transle-shon. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->