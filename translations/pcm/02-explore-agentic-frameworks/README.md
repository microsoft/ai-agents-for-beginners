[![Explorin AI Agent Frameworks](../../../translated_images/pcm/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Click di picture wey dey up to watch dis lesson video)_

# Make We Explore AI Agent Frameworks

AI agent frameworks na software platforms wey dem design to make e easy to create, deploy, and manage AI agents. Dem frameworks dey give developers pre-built components, abstractions, and tools wey dey help make the development of complex AI systems faster.

Dem frameworks dey help developers concentrate on wetin dey unique for their apps by giving standard ways to handle common wahala for AI agent development. Dem dey boost scalability, accessibility, and efficiency for building AI systems.

## Introduction 

This lesson go cover:

- Wetin be AI Agent Frameworks and wetin dem fit make developers achieve?
- How teams fit use dem to quickly prototype, iterate, and improve their agent’s capabilities?
- Wetin be differences between the frameworks and tools wey Microsoft create (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> and the <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- I fit integrate my existing Azure ecosystem tools directly, or I need standalone solutions?
- Wetin be Azure AI Agents service and how e dey help me?

## Learning goals

Di goals for dis lesson na to help you sabi:

- Di role wey AI Agent Frameworks dey play for AI development.
- How to use AI Agent Frameworks take build intelligent agents.
- Key capabilities wey AI Agent Frameworks dey enable.
- Differences wey dey between the Microsoft Agent Framework and Azure AI Agent Service.

## What are AI Agent Frameworks and what do they enable developers to do?

Traditional AI Frameworks fit help you integrate AI inside your apps and make these apps beta for di following ways:

- **Personalization**: AI fit analyze user behaviour and preferences to give personalized recommendations, content, and experiences.
Example: Streaming services like Netflix dey use AI to suggest movies and shows based on viewing history, wey dey make users engage more and dey happy.
- **Automation and Efficiency**: AI fit automate repetitive tasks, streamline workflows, and improve operational efficiency.
Example: Customer service apps dey use AI-powered chatbots to handle common inquiries, wey dey reduce response times and free human agents to handle more complex issues.
- **Enhanced User Experience**: AI fit improve overall user experience by giving intelligent features like voice recognition, natural language processing, and predictive text.
Example: Virtual assistants like Siri and Google Assistant dey use AI to understand and respond to voice commands, wey dey make am easier for users to interact with their devices.

### That all sounds great right, so why do we need the AI Agent Framework?

AI Agent frameworks mean something pass normal AI frameworks. Dem design dem to enable the creation of intelligent agents wey fit interact with users, other agents, and the environment to achieve specific goals. These agents fit show autonomous behaviour, make decisions, and adapt to changing conditions. Make we look some key capabilities wey AI Agent Frameworks dey enable:

- **Agent Collaboration and Coordination**: Dem enable you create many AI agents wey fit work together, communicate, and coordinate to solve complex tasks.
- **Task Automation and Management**: Dem give mechanisms for automating multi-step workflows, task delegation, and dynamic task management among agents.
- **Contextual Understanding and Adaptation**: Dem equip agents with ability to understand context, adapt to changing environments, and make decisions based on real-time information.

So in short, agents dey allow you do more, make automation reach next level, and create more intelligent systems wey fit adapt and learn from their environment.

## How to quickly prototype, iterate, and improve the agent’s capabilities?

This landscape dey move quick, but some things common for most AI Agent Frameworks fit help you quickly prototype and iterate — like modular components, collaborative tools, and real-time learning. Make we dive into these:

- **Use Modular Components**: AI SDKs dey offer pre-built components like AI and Memory connectors, function calling using natural language or code plugins, prompt templates, and more.
- **Leverage Collaborative Tools**: Design agents with specific roles and tasks, make dem test and refine collaborative workflows.
- **Learn in Real-Time**: Implement feedback loops wey make agents learn from interactions and adjust their behaviour dynamically.

### Use Modular Components

SDKs like the Microsoft Agent Framework dey offer pre-built components like AI connectors, tool definitions, and agent management.

**How teams fit use these**: Teams fit quickly assemble these components to create a working prototype without starting from scratch, so dem fit experiment and iterate fast.

**How e dey work for practice**: You fit use pre-built parser to extract information from user input, a memory module to store and retrieve data, and a prompt generator to interact with users, all without building these components from scratch.

**Example code**. Make we look one example of how you fit use the Microsoft Agent Framework with `AzureAIProjectAgentProvider` to make the model respond to user input with tool calling:

``` python
# Microsoft Agent Framework Python Example

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Define wan sample tool function to book travel
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Example output: Your flight go New York on January 1, 2025, don successfully book. Safe travels! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Wetin you fit see from this example na how you fit use pre-built parser to extract key information from user input, like origin, destination, and date for flight booking request. Dis modular approach allow you focus on the high-level logic.

### Leverage Collaborative Tools

Frameworks like the Microsoft Agent Framework dey make am easy to create multiple agents wey fit work together.

**How teams fit use these**: Teams fit design agents with specific roles and tasks, make dem test and refine collaborative workflows and improve overall system efficiency.

**How e dey work for practice**: You fit create team of agents where each agent get specialized function, like data retrieval, analysis, or decision-making. These agents fit communicate and share info to achieve common goal, like answer user question or complete task.

**Example code (Microsoft Agent Framework)**:

```python
# Di mek plenty agents wey dey work togeder wit di Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Data Retrieve Agent
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Data Analyse Agent
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Make agents run one after di oda for one work
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Wetin you see for the code wey pass na how you fit create task wey involve multiple agents wey dey work together to analyze data. Each agent dey do specific function, and the task dey executed by coordinating the agents to reach the desired outcome. By creating dedicated agents with specialized roles, you fit improve task efficiency and performance.

### Learn in Real-Time

Advanced frameworks dey provide capability for real-time context understanding and adaptation.

**How teams fit use these**: Teams fit implement feedback loops wey make agents learn from interactions and change their behaviour dynamically, so dem go continue to improve and refine capabilities.

**How e dey work for practice**: Agents fit analyze user feedback, environmental data, and task outcomes to update their knowledge base, adjust decision-making algorithms, and improve performance over time. Dis iterative learning process make agents fit adapt to changing conditions and user preferences, and e dey boost overall system effectiveness.

## What are the differences between the Microsoft Agent Framework and Azure AI Agent Service?

Plenty ways dey compare these approaches, but make we look some key differences for their design, capabilities, and target use cases:

## Microsoft Agent Framework (MAF)

The Microsoft Agent Framework na streamlined SDK for building AI agents using `AzureAIProjectAgentProvider`. E enable developers to create agents wey use Azure OpenAI models with built-in tool calling, conversation management, and enterprise-grade security through Azure identity.

**Use Cases**: Build production-ready AI agents wey fit use tools, run multi-step workflows, and integrate with enterprise scenarios.

Here be some important core concepts of the Microsoft Agent Framework:

- **Agents**. Agent dey create via `AzureAIProjectAgentProvider` and you configure am with name, instructions, and tools. The agent fit:
  - **Process user messages** and generate responses using Azure OpenAI models.
  - **Call tools** automatically based on conversation context.
  - **Maintain conversation state** across multiple interactions.

  Here be code snippet wey show how to create an agent:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Tools**. The framework support defining tools as Python functions wey the agent fit invoke automatically. Tools dey register when creating the agent:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Multi-Agent Coordination**. You fit create multiple agents with different specializations and coordinate their work:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure Identity Integration**. The framework dey use `AzureCliCredential` (or `DefaultAzureCredential`) for secure, keyless authentication, so you no need manage API keys directly.

## Azure AI Agent Service

Azure AI Agent Service na newer option wey dem present for Microsoft Ignite 2024. E allow development and deployment of AI agents with more flexible models, for example direct call open-source LLMs like Llama 3, Mistral, and Cohere.

Azure AI Agent Service dey provide stronger enterprise security mechanisms and data storage ways, so e good for enterprise apps.

E dey work out-of-the-box with the Microsoft Agent Framework for building and deploying agents.

This service dey Public Preview now and e support Python and C# for building agents.

Using the Azure AI Agent Service Python SDK, we fit create agent with user-defined tool:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Define tool functions na wetin deh for do small small samting dem
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
        model="gpt-4o-mini",
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

Azure AI Agent Service get these core concepts:

- **Agent**. Azure AI Agent Service integrate with Microsoft Foundry. For AI Foundry, AI Agent act like "smart" microservice wey fit answer questions (RAG), perform actions, or fully automate workflows. E do this by combining the power of generative AI models with tools wey allow am access and interact with real-world data sources. Example of an agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    For this example, agent dey create with the model `gpt-4o-mini`, name `my-agent`, and instructions `You are helpful agent`. The agent get tools and resources to perform code interpretation tasks.

- **Thread and messages**. Thread na another important concept. E represent conversation or interaction between an agent and user. Threads fit track the progress of conversation, store context info, and manage the state of the interaction. Example of a thread:

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

    For the code wey pass, thread dey create. After dat, message dey send to the thread. By calling `create_and_process_run`, the agent dey asked to perform work on the thread. Finally, the messages dey fetched and logged to show the agent's response. The messages dey indicate the progress of the conversation between user and agent. E also important to sabi say messages fit dey different types like text, image, or file — for example the agent work fit result in an image or text response. As developer, you fit use this info to further process the response or present am to the user.

- **Integrates with the Microsoft Agent Framework**. Azure AI Agent Service dey work well with the Microsoft Agent Framework, which mean you fit build agents using `AzureAIProjectAgentProvider` and deploy dem through the Agent Service for production scenarios.

**Use Cases**: Azure AI Agent Service design for enterprise applications wey need secure, scalable, and flexible AI agent deployment.

## What's the difference between these approaches?
 
E dey seem like overlap dey, but some key differences dey for design, capabilities, and target use cases:
 
- **Microsoft Agent Framework (MAF)**: Na production-ready SDK for building AI agents. E provide streamlined API for creating agents with tool calling, conversation management, and Azure identity integration.
- **Azure AI Agent Service**: Na platform and deployment service for agents inside Azure Foundry. E offer built-in connectivity to services like Azure OpenAI, Azure AI Search, Bing Search and code execution.
 
Still no sure which one to choose?

### Use Cases
 
Make we try help you by going through common use cases:
 
> Q: I dey build production AI agent applications and I want to start quick
>

>A: The Microsoft Agent Framework na good choice. E provide simple, Pythonic API via `AzureAIProjectAgentProvider` wey let you define agents with tools and instructions in just few lines of code.

>Q: I need enterprise-grade deployment with Azure integrations like Search and code execution
>
> A: Azure AI Agent Service na the best fit. Na platform service wey get built-in capabilities for multiple models, Azure AI Search, Bing Search and Azure Functions. E make am easy to build agents for the Foundry Portal and deploy dem for scale.
 
> Q: I still dey confused, just give me one option
>
> A: Start with the Microsoft Agent Framework to build your agents, then use Azure AI Agent Service when you need deploy and scale them for production. This way you fit iterate quick on your agent logic and still get clear path to enterprise deployment.
 
Make we summarize key differences for a table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?
Di ansa na yes — you fit integrate your existing Azure ecosystem tools directly wit Azure AI Agent Service, especially as e don build make e work seamlessly wit oda Azure services. You fit, for example, integrate Bing, Azure AI Search, and Azure Functions. E still get deep integration wit Microsoft Foundry.

The Microsoft Agent Framework sef dey integrate wit Azure services through `AzureAIProjectAgentProvider` and Azure identity, letting you call Azure services directly from your agent tools.

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## You get more questions about AI Agent Frameworks?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet wit oda learners, attend office hours, and make dem answer your AI Agents questions.

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Previous Lesson

[Intro to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Disclaimer:
Dis document dem translate wit AI translation service wey dem dey call Co-op Translator (https://github.com/Azure/co-op-translator). Even though we dey try make am correct, abeg sabi say automatic translations fit get mistakes or things wey no too correct. The original document for im original language na the main/official source. If na important information, better make professional human translator do am. We no go liable for any misunderstanding or wrong interpretation wey fit come from this translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->