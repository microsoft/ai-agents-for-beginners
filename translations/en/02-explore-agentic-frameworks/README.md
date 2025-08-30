<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a9631d0898fc3c6ecbb3a8a0da7aaba3",
  "translation_date": "2025-08-30T07:04:43+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "en"
}
-->
## Azure AI Agent Service

Azure AI Agent Service is a managed service provided by Microsoft that simplifies the deployment and management of AI agents. It integrates seamlessly with the Azure ecosystem, enabling developers to leverage Azure's robust infrastructure and tools to build, deploy, and scale intelligent agents.

### Key Features

- **Managed Service**: Azure AI Agent Service provides a fully managed environment for running AI agents, reducing the operational overhead associated with managing infrastructure.
- **Integration with Azure Ecosystem**: The service integrates with other Azure tools and services, such as Azure Cognitive Services, Azure OpenAI, and Azure Machine Learning, allowing developers to create comprehensive AI solutions.
- **Scalability**: The service is designed to scale automatically based on demand, ensuring that agents can handle varying workloads efficiently.
- **Security and Compliance**: Azure AI Agent Service adheres to Microsoft's security and compliance standards, providing a secure environment for running AI agents.

### Use Cases

- **Customer Support**: Deploy AI agents to handle customer inquiries, provide personalized recommendations, and automate support workflows.
- **Business Process Automation**: Use AI agents to automate repetitive tasks, streamline operations, and improve efficiency.
- **Data Analysis**: Build agents that can analyze large datasets, generate insights, and assist in decision-making processes.

### Example Workflow

1. **Create an Agent**: Define the agent's capabilities, roles, and tasks using Azure AI Agent Service.
2. **Integrate with Azure Tools**: Connect the agent to Azure Cognitive Services for natural language processing, Azure OpenAI for advanced language models, and Azure Machine Learning for predictive analytics.
3. **Deploy and Monitor**: Deploy the agent to the Azure AI Agent Service and monitor its performance using Azure's monitoring tools.
4. **Iterate and Improve**: Use feedback and analytics to refine the agent's capabilities and improve its performance over time.

### Benefits

- **Ease of Use**: The managed service simplifies the process of creating and deploying AI agents, allowing developers to focus on building intelligent solutions.
- **Robust Infrastructure**: Leverage Azure's reliable and scalable infrastructure to ensure high availability and performance.
- **Seamless Integration**: Combine the power of Azure's AI tools and services to create comprehensive and intelligent systems.

## Summary

In this lesson, we've explored the concept of AI Agent Frameworks and their role in enabling developers to build intelligent agents. We covered the differences between AutoGen, Semantic Kernel, and Azure AI Agent Service, highlighting their unique features and use cases. By leveraging these frameworks, developers can create advanced AI systems that automate tasks, enhance user experiences, and adapt to changing environments.
So that's the basics of the Semantic Kernel framework, what about the Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service is a more recent addition, introduced at Microsoft Ignite 2024. It allows for the development and deployment of AI agents with more flexible models, such as directly calling open-source LLMs like Llama 3, Mistral, and Cohere.

Azure AI Agent Service provides stronger enterprise security mechanisms and data storage methods, making it suitable for enterprise applications. 

It works out-of-the-box with multi-agent orchestration frameworks like AutoGen and Semantic Kernel.

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

    In the previous code, a thread is created. Thereafter, a message is sent to the thread. By calling `create_and_process_run`, the agent is asked to perform work on the thread. Finally, the messages are fetched and logged to see the agent's response. The messages indicate the progress of the conversation between the user and the agent. It's also important to understand that the messages can be of different types such as text, image, or file, that is the agents work has resulted in for example an image or a text response for example. As a developer, you can then use this information to further process the response or present it to the user.

- **Integrates with other AI frameworks**. Azure AI Agent service can interact with other frameworks like AutoGen and Semantic Kernel, which means you can build part of your app in one of these frameworks and for example using the Agent service as an orchestrator or you can build everything in the Agent service.

**Use Cases**: Azure AI Agent Service is designed for enterprise applications that require secure, scalable, and flexible AI agent deployment.

## What's the difference between these frameworks?
 
It does sound like there is a lot of overlap between these frameworks, but there are some key differences in terms of their design, capabilities, and target use cases:
 
- **AutoGen**: Is an experimentation framework focused on leading-edge research on multi-agent systems. It is the best place to experiment and prototype sophisticated multi-agent systems.
- **Semantic Kernel**: Is a production-ready agent library for building enterprise agentic applications. Focuses on event-driven, distributed agentic applications, enabling multiple LLMs and SLMs, tools, and single/multi-agent design patterns.
- **Azure AI Agent Service**: Is a platform and deployment service in Azure Foundry for agents. It offers building connectivity to services support by Azure Found like Azure OpenAI, Azure AI Search, Bing Search and code execution.
 
Still not sure which one to choose?

### Use Cases
 
Let's see if we can help you by going through some common use cases:
 

> Q: I'm experimenting, learning and building proof-of-concept agent applications, and I want to be able to build and experiment quickly
>

>A: AutoGen would be a good choice for this scenario, as it focuses on event-driven, distributed agentic applications and supports advanced multi-agent design patterns.

> Q: What makes AutoGen a better choice than Semantic Kernel and Azure AI Agent Service for this use case?
>
> A: AutoGen is specifically designed for event-driven, distributed agentic applications, making it well-suited for automating code generation and data analysis tasks. It provides the necessary tools and capabilities to build complex multi-agent systems efficiently.

>Q: Sounds like Azure AI Agent Service could work here too, it has tools for code generation and more?

>
> A: Yes, Azure AI Agent Service is a platform service for agents and add built-in capabilities for multiple models, Azure AI Search, Bing Search and Azure Functions. It makes it easy to build your agents in the Foundry Portal and deploy them at scale.
 
> Q: I'm still confused just give me one option
>
> A: A great choice is to build your application in Semantic Kernel first and then use Azure AI Agent Service to deploy your agent. This approach allows you to easily persist your agents while leveraging the power to build multi-agent systems in Semantic Kernel. Additionally, Semantic Kernel has a connector in AutoGen, making it easy to use both frameworks together.
 
Let's summarize the key differences in a table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| AutoGen | Event-driven, distributed agentic applications | Agents, Personas, Functions, Data | Code generation, data analysis tasks |
| Semantic Kernel | Understanding and generating human-like text content | Agents, Modular Components, Collaboration | Natural language understanding, content generation |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

What's the ideal use case for each of these frameworks?

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?

The answer is yes, you can integrate your existing Azure ecosystem tools directly with Azure AI Agent Service especially, this because it has been built to work seamlessly with other Azure services. You could for example integrate Bing, Azure AI Search, and Azure Functions. There's also deep integration with Azure AI Foundry.

For AutoGen and Semantic Kernel, you can also integrate with Azure services, but it may require you to call the Azure services from your code. Another way to integrate is to use the Azure SDKs to interact with Azure services from your agents. Additionally, like was mentioned, you can use Azure AI Agent Service as an orchestrator for your agents built in AutoGen or Semantic Kernel which would give easy access to the Azure ecosystem.

### Got More Questions about AI Agent Frameworks?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## References

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.