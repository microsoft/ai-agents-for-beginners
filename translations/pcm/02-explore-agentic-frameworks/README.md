[![Exploring AI Agent Frameworks](../../../translated_images/pcm/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Click di image we dey top to watch video of dis lesson)_

# Explore AI Agent Frameworks

AI agent frameworks na software platforms wey dem design to make e easy to create, deploy, and manage AI agents. Dem frameworks dey give developers pre-built components, abstractions, and tools wey quicken di development of complex AI systems.

Dem frameworks dey help developers focus for di unique parts of dia applications by providing standard ways to solve common wahala for AI agent development. Dem dey improve scalability, accessibility, and efficiency for building AI systems.

## Introduction 

This lesson go cover:

- Wetin be AI Agent Frameworks and wetin dem dey help developers fit do?
- How teams fit use dem to quickly prototype, iterate, and improve dia agent’s abilities?
- Wetin be difference between di frameworks and tools wey Microsoft create (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> and <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- I fit connect my existing Azure ecosystem tools directly, or I need make e dey standalone?
- Wetin be Microsoft Foundry Agent Service and how e dey help me?

## Learning goals

Di goals of dis lesson na to help you understand:

- Di role wey AI Agent Frameworks get for AI development.
- How to take AI Agent Frameworks build smart agents.
- Key abilities wey AI Agent Frameworks fit enable.
- Di difference between Microsoft Agent Framework and Microsoft Foundry Agent Service.

## Wetin be AI Agent Frameworks and wetin dem enable developers to do?

Traditional AI Frameworks fit help you add AI give your apps and make di apps beta in dis kain ways:

- **Personalization**: AI fit analyze user behavior and preferences to give personalized recommendations, content, and experiences.
Example: Streaming services like Netflix dey use AI to suggest movies and shows based on how you don watch before, wey dey improve user engagement and satisfaction.
- **Automation and Efficiency**: AI fit automatic repetitive tasks, make workflows smooth, and improve how operations dey run.
Example: Customer service apps dey use AI-powered chatbots to handle common questions, shorten response times and free human agents to deal with more complex matters.
- **Enhanced User Experience**: AI dey improve overall user experience by giving smart features like voice recognition, natural language processing, and predictive text.
Example: Virtual assistants like Siri and Google Assistant dey use AI to understand and respond to voice commands, e make am easier for users to interact with their devices.

### All dis sounds beta abi, why we still need AI Agent Framework?

AI Agent frameworks no be just AI frameworks. Dem design to enable creation of smart agents wey fit interact with users, other agents, and environment to achieve special goals. These agents fit behave on dia own, make decisions, and adjust to changes. Make we see some key abilities wey AI Agent Frameworks enable:

- **Agent Collaboration and Coordination**: Make e possible to create plenty AI agents wey fit work together, communicate, and coordinate to solve complex tasks.
- **Task Automation and Management**: Provide ways to automate multi-step workflows, delegate tasks, and manage tasks dynamically among agents.
- **Contextual Understanding and Adaptation**: Give agents ability to understand context, adjust to changing environment, and make decisions based on real-time info.

So, to summarize, agents dey allow you to do more, take automation go next level, and create smarter systems wey fit adapt and learn from their environment.

## How to quickly prototype, iterate, and improve agent’s abilities?

Dis matter dey move quick, but some things dey common for most AI Agent Frameworks wey fit help you prototype and iterate fast, like module components, collaborative tools, and real-time learning. Make we explore dem:

- **Use Modular Components**: AI SDKs dey give pre-built components like AI and Memory connectors, function call wey fit use natural language or code plugins, prompt templates, plus more.
- **Leverage Collaborative Tools**: Design agents with particular roles and tasks, make dem test and improve how dem dey collaborate.
- **Learn in Real-Time**: Set up feedback loops wey agents dey learn from interactions and change how dem dey do things as e dey happen.

### Use Modular Components

SDKs like Microsoft Agent Framework dey provide pre-built components like AI connectors, tool definitions, and agent management.

**How teams fit use dem**: Teams fit quickly put together these components to create functional prototype without to start from scratch, e dey allow rapid experiments and iterations.

**How e dey work for practice**: You fit use pre-built parser to extract info from user input, memory module to store and get data, and prompt generator to interact with users, all without to build these parts from beginning.

**Example code**. Make we check example how you fit use Microsoft Agent Framework with `FoundryChatClient` to make model respond to user input with tool call:

``` python
# Microsoft Agent Framework Python Example

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Define one sample tool function wey go book travel
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
    # Example output: Your flight go New York on January 1, 2025, don book gidigba. Safe travels! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Wetin you go see for dis example na how you fit use pre-built parser to take important info from user input, like origin, destination, and travel date for flight booking. Dis modular approach make you fit focus on high-level logic.

### Leverage Collaborative Tools

Frameworks like Microsoft Agent Framework dey help create many agents wey fit work together.

**How teams fit use dem**: Teams fit design agents with special roles and tasks, so dem fit test and improve collaborative workflows and make system efficiency beta.

**How e dey work for practice**: You fit create team of agents wey each get special function, like data retrieval, analysis, or decision-making. These agents fit communicate and share info to achieve one goal, e.g., answer user question or finish task.

**Example code (Microsoft Agent Framework)**:

```python
# Dey create plenti agents wey go work together wit di Microsoft Agent Framework

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

# Make agents run one by one for di task
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Wetin you see for di code above na how you fit create task wey many agents dey work together to analyze data. Each agent dey do special work, and dem coordinate to finish di task as e suppost be. By creating agents with clear roles, you fit improve task efficiency and performance.

### Learn in Real-Time

Advanced frameworks get abilities for real-time context understanding and adjustment.

**How teams fit use dem**: Teams fit put feedback loops wey make agents learn from interactions and adjust behaviour as e dey go, so performance go continuously improve.

**How e dey work for practice**: Agents fit analyze user feedback, environment data, and task results to update knowledge base, adjust decision algorithms, and improve performance over time. This iterative learning make agents fit adapt to change and user preferences, improve system effectiveness.

## Wetin be di difference between Microsoft Agent Framework and Microsoft Foundry Agent Service?

Plenty ways dey to compare these, but make we look some key difference for their design, abilities, and intended use:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework dey provide streamlined SDK to build AI agents using `FoundryChatClient`. E enable devs create agents wey fit use Azure OpenAI models with built-in tool call, conversation management, and enterprise-grade security through Azure identity.

**Use Cases**: Build production-ready AI agents with tools, multi-step workflows, and enterprise integration scenarios.

Here be some important core concepts for Microsoft Agent Framework:

- **Agents**. Agent na one wey you create with `FoundryChatClient` and configure am with name, instructions, and tools. Agent fit:
  - **Process user messages** and generate responses using Azure OpenAI models.
  - **Call tools** automatically based on conversation context.
  - **Maintain conversation state** through many interactions.

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

- **Tools**. Framework fit support defining tools as Python functions wey agent fit call automatically. Tools go register when you create agent:

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

- **Multi-Agent Coordination**. You fit create many agents with different specialties and coordinate dia work:

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

- **Azure Identity Integration**. Framework dey use `AzureCliCredential` (or `DefaultAzureCredential`) for secure, keyless authentication, so you no need manage API keys directly.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service na newer addition, wey dem show for Microsoft Ignite 2024. E allow make people develop and deploy AI agents with more flexible models, like direct call open-source LLMs like Llama 3, Mistral, and Cohere.

Microsoft Foundry Agent Service get stronger enterprise security and data storage methods, so e good for enterprise applications. 

E work out-of-the-box with Microsoft Agent Framework for building and deploying agents.

Dis service dey Public Preview now and e support Python and C# for building agents.

Using Microsoft Foundry Agent Service Python SDK, we fit create agent with user-defined tool:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Define tool tins wey dem dey use do work
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
        model="gpt-4.1-mini",
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

Microsoft Foundry Agent Service get dis core concepts:

- **Agent**. Microsoft Foundry Agent Service integrate with Microsoft Foundry. For Microsoft Foundry, AI Agent na "smart" microservice wey fit answer questions (RAG), do actions, or fully automate workflows. E take power from generative AI models plus tools wey dey able to access and interact with real-world data. Here be example of agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    For dis example, agent create with model `gpt-4.1-mini`, name `my-agent`, and instructions `You are helpful agent`. Agent get tools and resources to do code interpretation tasks.

- **Thread and messages**. Thread na another important concept. E represent conversation or interaction between agent and user. Threads fit track conversation progress, store context info, and manage interaction state. Example of thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask di agent to do work for di thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch an log all di messages make you see how di agent go respond
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    For di code inside, thread create. Then message send to thread. By calling `create_and_process_run`, agent dey asked to do work for thread. In the end, messages fetch and logged to show agent response. Messages dey show conversation progress between user and agent. E important to sabi say messages fit get different types like text, image or file, meaning agent work fit come out as for example image or text answer. As developer, you fit use dis info for follow-up processing or to show user.

- **Integrates with Microsoft Agent Framework**. Microsoft Foundry Agent Service dey work well well with Microsoft Agent Framework, meaning you fit build agents with `FoundryChatClient` and deploy them through Agent Service for production.

**Use Cases**: Microsoft Foundry Agent Service design for enterprise applications wey need secure, scalable, flexible AI agent deployment.

## Wetin be di difference between dese approaches?
 
E be like overlap dey, but some key differences dey for design, powers, and target use cases:
 
- **Microsoft Agent Framework (MAF)**: Na production-ready SDK to build AI agents. E get streamlined API for creating agents with tool call, conversation management, and Azure identity integration.
- **Microsoft Foundry Agent Service**: Na platform and deployment service for agents inside Microsoft Foundry. E get built-in connection to services like Azure OpenAI, Azure AI Search, Bing Search and code execution.
 
Still dey wonder which one to pick?

### Use Cases
 
Make we help you by showing some common use cases:
 
> Q: I dey build production AI agent apps and I want start fast
>

>A: Microsoft Agent Framework na beta choice. E get simple, Python style API via `FoundryChatClient` wey let you define agents with tools and instructions in just small code.

>Q: I need enterprise-grade deployment with Azure features like Search and code execution
>
> A: Microsoft Foundry Agent Service na best fit. Na platform service wey get built-in support for many models, Azure AI Search, Bing Search and Azure Functions. E make am easy to build agents for Foundry Portal and deploy dem at scale.
 
> Q: I still dey confused, just give me one option
>
> A: Start with Microsoft Agent Framework to build your agents, then use Microsoft Foundry Agent Service when you ready to deploy and scale for production. This way, you fit quickly test your agent logic and still get enterprise deployment path clear.
 
Make we summarize key differences for table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool call | Agents, Tools, Azure Identity | Build AI agents, tool use, multi-step workflows |
| Microsoft Foundry Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, flexible AI agent deployment |

## I fit integrate my existing Azure ecosystem tools directly, or I need standalone solutions?


Di answer na yes, you fit connect your existing Azure ecosystem tools straight to Microsoft Foundry Agent Service specially, as e dey built to work well witoda oda Azure services. You fit for example connect Bing, Azure AI Search, and Azure Functions. E still get deep connection wit Microsoft Foundry.

Di Microsoft Agent Framework still dey connect wit Azure services through `FoundryChatClient` and Azure identity, wey fit make you yan Azure services direct from your agent tools.

## Sample Codes

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## You Get More Questions about AI Agent Frameworks?

Join di [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) to meet oda learners, join office hours and make you fit get answer for your AI Agents questions.

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