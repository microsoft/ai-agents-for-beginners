[![Exploring AI Agent Frameworks](../../../translated_images/pcm/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Click di piktia wey dey up dere make you watch video of dis lesson)_

# Explore AI Agent Frameworks

AI agent frameworks na software platforms wey dem design to make e easy to create, deploy, and manage AI agents. Dem frameworks dey provide developers with pre-built parts, abstractions, and tools wey dey make e easy to build complex AI systems.

Dem frameworks dey help developers focus on the unique tins wey concern their apps by giving standard ways to handle common wahala for AI agent development. Dem dey improve how scalable, accessible, and efficient e go be to build AI systems.

## Introduction 

Dis lesson go cover:

- Wetin AI Agent Frameworks be and wetin dem fit make developers achieve?
- How teams fit take dem quickly prototype, change, and improve their agent's abilities?
- Wetin be di differences between di frameworks and tools wey Microsoft don create (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> and di <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- I fit connect my existing Azure tools directly, or I need separate solutions?
- Wetin be Microsoft Foundry Agent Service and how e dey help me?

## Learning goals

Di goals of dis lesson na to help you sabi:

- Di role of AI Agent Frameworks for AI development.
- How to use AI Agent Frameworks to build smart agents.
- Key things wey AI Agent Frameworks dey enable.
- Di difference between Microsoft Agent Framework and Microsoft Foundry Agent Service.

## Wetin be AI Agent Frameworks and wetin dem allow developers to do?

Old school AI Frameworks fit help you put AI inside your apps and make di apps better in dis kain ways:

- **Personalization**: AI fit check how user dey behave and wetin dem like to give personalized advice, content, and experiences.
Example: Streaming services like Netflix dey use AI to talk movie and shows wey you fit like based on wetin you don watch before, to make user happy and join well well.
- **Automation and Efficiency**: AI fit do repetitive work automatically, make workflow smooth, and improve how things dey run.
Example: Customer service apps dey use AI-powered chatbots to answer common questions fast, reduce wait time and allow human agents to handle big wahala.
- **Better User Experience**: AI fit improve how user dey experience things by giving smart features like voice recognition, natural talk processing, and predictive text.
Example: Virtual assistants like Siri and Google Assistant dey use AI to understand and reply voice commands, to make e easy to use their device.

### E sound good, but why we need AI Agent Framework?

AI Agent frameworks no just be ordinary AI frameworks. Dem dey build to create smart agents wey fit interact with users, other agents, and environment to achieve specific goals. These agents fit do autonomous work, make decision, and adjust to changing situations. Make we look key abilities wey AI Agent Frameworks dey enable:

- **Agent Collaboration and Coordination**: Make e possible to create plenty AI agents wey fit work together, yarn, and coordinate to solve big tasks.
- **Task Automation and Management**: Provide ways to automate multi-step workflow, share task, and manage task dynamically between agents.
- **Contextual Understanding and Adaptation**: Give agents power to understand context, adjust to changes, and make decisions based on correct time info.

So in short, agents go allow you do more, take automation go higher level, and build smart systems wey fit adjust and learn from environment.

## How to quickly prototype, change, and improve agent’s abilities?

Dis place dey move fast, but some tins dey common for most AI Agent Frameworks wey fit help you quickly prototype and change dem, like module parts, collaborative tools, and real-time learning. Make we dive into dem:

- **Use Modular Components**: AI SDKs get pre-built parts like AI and Memory connectors, function calling using natural talk or code plugins, prompt templates, and more.
- **Use Collaborative Tools**: Design agents with clear roles and tasks, make dem fit test and fix collaborative workflows.
- **Learn in Real-Time**: Do feedback loops where agents learn from interaction and adjust how dem dey behave quick quick.

### Use Modular Components

SDKs like Microsoft Agent Framework get pre-built parts like AI connectors, tool definitions, and agent management.

**How teams fit use dem**: Teams fit quickly join these parts to build prototype wey work without start from ground zero, to test and change quick quick.

**How e dey work for real**: You fit use pre-built parser to take info from user input, memory module to store and find data, and prompt generator to interact with users, all without building these parts yourself.

**Example code**. Make we look example of how you fit use Microsoft Agent Framework with `FoundryChatClient` to make model respond user input with tool calling:

``` python
# Microsoft Agent Framework Python Example

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Define one sample tool function to book travel
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Example output: Your flight go New York on January 1, 2025, don land well well. Safe travels! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Wetin you see from dis example na how you fit use pre-built parser to take key info from user input, like origin, destination, and date of flight booking request. Dis modular way allow you focus on high-level logic.

### Use Collaborative Tools

Frameworks like Microsoft Agent Framework dey make am easy to create many agents wey fit work together.

**How teams fit use dem**: Teams fit design agents with special roles and tasks, make dem fit test and make collaborative workflows better and improve system efficiency.

**How e dey work for real**: You fit create team of agents wey each get special job, like data collection, analysis, or decision-making. Agents fit yarn and share info to achieve common goal like answer user question or finish task.

**Example code (Microsoft Agent Framework)**:

```python
# Di mekplenti agents wey dem go work together wit di Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Data Retrieval Agent
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Data Analysis Agent
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Make di agents run one after di oda for di task
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Wetin you see for code before na how you fit create task wey involve many agents working together to analyze data. Each agent get special function, and task dey done when agents coordinate to get correct result. By creating agents with special roles, you fit improve how task dey performed and how e go.

### Learn in Real-Time

Better frameworks get power for real-time context understanding and adjustment.

**How teams fit use dem**: Teams fit do feedback loops wey agents dey learn from interaction and adjust their behavior quick quick, to keep improving and fixing their abilities.

**How e dey work for real**: Agents fit analyze user feedback, environment data, and task results to update their knowledge, adjust decision making, and do better work over time. Dis learning process allow agents to adjust to change and user choice, to make system more effective.

## Wetin be di difference between Microsoft Agent Framework and Microsoft Foundry Agent Service?

Plenty ways dey to compare dem, but make we look key difference for design, abilities, and where dem fit use well:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework na simple SDK for building AI agents using `FoundryChatClient`. E make developers fit create agents wey use Azure OpenAI models with tool calling, conversation management, and correct enterprise security using Azure identity.

**Use Cases**: Build production-ready AI agents wey fit use tools, do multi-step workflow, and fit connect with enterprise systems.

Here be some important core ideas for Microsoft Agent Framework:

- **Agents**. Agent na wetin e be when you create am with `FoundryChatClient` and set name, instructions, and tools. Agent fit:
  - **Process user message** and answer with Azure OpenAI models.
  - **Call tools** automatically based on conversation context.
  - **Keep conversation state** for many interactions.

  Here be code snippet wey show how to create agent:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Tools**. Framework fit define tools as Python functions wey agent fit call automatically. Tools get register when creating agent:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Multi-Agent Coordination**. You fit create many agents with different specialties and coordinate their work:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure Identity Integration**. Framework dey use `AzureCliCredential` (or `DefaultAzureCredential`) for secure, keyless authentication, so you no need manage API keys direct.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service na new one, wey dem show for Microsoft Ignite 2024. E allow develop and deploy AI agents with more flexible models, like direct calling open-source LLMs like Llama 3, Mistral, and Cohere.

Microsoft Foundry Agent Service get better security and data storage ways for enterprise use.

E work well with Microsoft Agent Framework to build and deploy agents.

Dis service dey Public Preview now and support Python and C# for building agents.

Using Microsoft Foundry Agent Service Python SDK, we fit create agent wey get user-defined tool:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Define tool functions for use
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Core concepts

Microsoft Foundry Agent Service get these core ideas:

- **Agent**. Microsoft Foundry Agent Service connect with Microsoft Foundry. For Microsoft Foundry, AI Agent na "smart" microservice wey fit answer questions (RAG), do actions, or automate whole workflows. E dey do dis by cutting generative AI models power with tools wey make am fit access and interact with real-world data. Here be example of agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    For dis example, agent don create with model `gpt-5-mini`, name `my-agent`, and instructions `You are helpful agent`. Agent get tools and resources to do code interpretation tasks.

- **Thread and messages**. Thread na another important idea. E mean conversation or interaction between agent and user. Threads fit track how conversation dey go, hold context info, and manage interaction state. Here be example of thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask di agent make e do work for di thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Find and write down all di messages to see how di agent respond
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    For di code before, thread don create. Then message dey send to thread. By calling `create_and_process_run`, agent na im dey do work on the thread. Later, messages dey get and logged to see agent response. Messages show how conversation dey go between user and agent. E also important to know messages fit different types like text, image, or file, like agent work don produce image or text wey dem fit see. As developer, you fit use dis info to take response go further or show am to user.

- **Connect well with Microsoft Agent Framework**. Microsoft Foundry Agent Service dey work well with Microsoft Agent Framework, meaning say you fit build agents with `FoundryChatClient` and deploy dem through Agent Service for production.

**Use Cases**: Microsoft Foundry Agent Service na for enterprise apps wey need secure, scalable, and flexible AI agent deployment.

## Wetin be difference between these approaches?
 
E sound like dem get some similar tin, but dem get key difference for design, capabilities, and use cases:
 
- **Microsoft Agent Framework (MAF)**: E be production-ready SDK for building AI agents. E provide simple API to create agents with tool calling, conversation management, and Azure identity integration.
- **Microsoft Foundry Agent Service**: Na platform and deployment service inside Microsoft Foundry for agents. E get built-in connection to services like Azure OpenAI, Azure AI Search, Bing Search and code execution.
 
Still dey confuse which one to choose?

### Use Cases
 
Make we try help by going through common use cases:
 
> Q: I dey build production AI agent apps and I want start quick quick
>

>A: Microsoft Agent Framework na better choice. E get simple, Python-like API through `FoundryChatClient` wey let you define agents with tools and instructions with only few lines of code.

>Q: I need enterprise-grade deployment with Azure things like Search and code execution
>
> A: Microsoft Foundry Agent Service na di best. E be platform service wey get built-in ability for many models, Azure AI Search, Bing Search and Azure Functions. E make e easy to build your agents inside Foundry Portal and deploy them for big scale.
 
> Q: I still dey confuse, just give me one option
>
> A: Start with Microsoft Agent Framework to build your agents, then use Microsoft Foundry Agent Service when you need to deploy and scale am production side. Dis way fit help you change your agent logic quick quick while get clear road to enterprise deployment.
 
Make we summarize key difference for table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Microsoft Foundry Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## I fit connect my existing Azure ecosystem tools directly, or I need standalone solutions?


Di answer na yes, you fit connect your current Azure ecosystem tools direct wit Microsoft Foundry Agent Service specially, becos e don build to work well wit oda Azure services. You fit for example connect Bing, Azure AI Search, and Azure Functions. E get also deep connection wit Microsoft Foundry.

Di Microsoft Agent Framework sef dey connect wit Azure services through `FoundryChatClient` and Azure identity, wey dey allow you call Azure services direct from your agent tools.

## Sample Codes

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## You Get More Questions About AI Agent Frameworks?

Join di [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet oda learners, attend office hours and get your AI Agents questions answer.

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->