[![AI एजेंट फ़्रेमवर्क का अन्वेषण](../../../translated_images/hi/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(ऊपर की छवि पर क्लिक करके इस पाठ का वीडियो देखें)_

# AI एजेंट फ़्रेमवर्क का अन्वेषण

AI एजेंट फ़्रेमवर्क ऐसे सॉफ्टवेयर प्लेटफ़ॉर्म हैं जिन्हें AI एजेंट बनाने, तैनात करने और प्रबंधित करने को सरल बनाने के लिए डिज़ाइन किया गया है। ये फ़्रेमवर्क डेवलपर्स को प्री-बिल्ट कॉम्पोनेंट्स, एब्स्ट्रैक्शन्स और टूल्स प्रदान करते हैं जो जटिल AI सिस्टम के विकास को सुगम बनाते हैं।

ये फ़्रेमवर्क आम चुनौतियों के लिए मानकीकृत दृष्टिकोण प्रदान करके डेवलपर्स को उनके ऐप्लिकेशन के अनोखे पहलुओं पर ध्यान केंद्रित करने में मदद करते हैं। ये AI सिस्टम बनाने में स्केलेबिलिटी, पहुँच और दक्षता बढ़ाते हैं।

## Introduction 

This lesson will cover:

- What are AI Agent Frameworks and what do they enable developers to achieve?
- How can teams use these to quickly prototype, iterate, and improve their agent’s capabilities?
- What are the differences between the frameworks and tools created by Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI एजेंट सेवा</a> and the <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft एजेंट फ़्रेमवर्क</a>)?
- Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?
- What is Azure AI Agents service and how is this helping me?

## Learning goals

The goals of this lesson are to help you understand:

- The role of AI Agent Frameworks in AI development.
- How to leverage AI Agent Frameworks to build intelligent agents.
- Key capabilities enabled by AI Agent Frameworks.
- The differences between the Microsoft Agent Framework and Azure AI Agent Service.

## What are AI Agent Frameworks and what do they enable developers to do?

Traditional AI Frameworks can help you integrate AI into your apps and make these apps better in the following ways:

- **Personalization**: AI उपयोगकर्ता व्यवहार और प्राथमिकताओं का विश्लेषण कर व्यक्तिगत सिफारिशें, सामग्री और अनुभव प्रदान कर सकता है।
Example: Streaming services like Netflix use AI to suggest movies and shows based on viewing history, enhancing user engagement and satisfaction.
- **Automation and Efficiency**: AI दोहराए जाने वाले कार्यों को स्वचालित कर सकता है, वर्कफ़्लो को सरल बना सकता है, और परिचालन दक्षता बेहतर कर सकता है।
Example: Customer service apps use AI-powered chatbots to handle common inquiries, reducing response times and freeing up human agents for more complex issues.
- **Enhanced User Experience**: AI वॉइस रिकग्निशन, नेचुरल लैंग्वेज प्रोसेसिंग, और प्रेडिक्टिव टेक्स्ट जैसे बुद्धिमान फीचर्स प्रदान करके समग्र उपयोगकर्ता अनुभव को बेहतर बना सकता है।
Example: Virtual assistants like Siri and Google Assistant use AI to understand and respond to voice commands, making it easier for users to interact with their devices.

### That all sounds great right, so why do we need the AI Agent Framework?

AI Agent frameworks सिर्फ़ AI फ़्रेमवर्क से अधिक कुछ प्रस्तुत करते हैं। इन्हें बुद्धिमान एजेंट बनाने के लिए डिज़ाइन किया गया है जो उपयोगकर्ताओं, अन्य एजेंट्स, और पर्यावरण के साथ संवाद कर सकते हैं और विशिष्ट लक्ष्यों को प्राप्त कर सकते हैं। ये एजेंट स्वायत्त व्यवहार दिखा सकते हैं, निर्णय ले सकते हैं, और बदलती परिस्थितियों के अनुकूल हो सकते हैं। आइए AI Agent Frameworks से सक्षम कुछ प्रमुख क्षमताओं को देखें:

- **Agent Collaboration and Coordination**: कई AI एजेंट बनाने में सक्षम करते हैं जो साथ मिलकर काम कर सकते हैं, संवाद कर सकते हैं, और जटिल कार्यों को हल करने के लिए समन्वय कर सकते हैं।
- **Task Automation and Management**: बहु-स्टेप वर्कफ़्लो को स्वचालित करने, कार्य प्रतिनिधि निर्धारण, और एजेंट्स के बीच डायनामिक टास्क प्रबंधन के लिए मैकेनिज़्म प्रदान करते हैं।
- **Contextual Understanding and Adaptation**: एजेंट्स को संदर्भ समझने, बदलते परिवेश के अनुसार अनुकूलित होने, और वास्तविक-समय जानकारी के आधार पर निर्णय लेने की क्षमता से सुसज्जित करते हैं।

सार में, एजेंट आपको अधिक करने की अनुमति देते हैं, स्वचालन को अगले स्तर तक ले जाते हैं, और अधिक बुद्धिमान सिस्टम बनाने में मदद करते हैं जो अपने परिवेश से अनुकूलित और सीख सकते हैं।

## How to quickly prototype, iterate, and improve the agent’s capabilities?

यह तेज़ी से बदलने वाला क्षेत्र है, लेकिन अधिकांश AI Agent Frameworks में कुछ सामान्य बातें होती हैं जो आपको जल्दी प्रोटोटाइप बनाने और पुनरावृत्ति करने में मदद कर सकती हैं, विशेष रूप से मॉड्यूलर कॉम्पोनेंट्स, सहयोगी टूल्स, और रियल-टाइम लर्निंग। आइए इन्हें देखें:

- **Use Modular Components**: AI SDKs प्री-बिल्ट कॉम्पोनेंट्स प्रदान करते हैं जैसे AI और Memory कनेक्टर्स, फ़ंक्शन कॉलिंग नेचुरल लैंग्वेज या कोड प्लगइन्स के माध्यम से, प्रॉम्प्ट टेम्प्लेट्स, और अधिक।
- **Leverage Collaborative Tools**: एजेंट्स को विशिष्ट भूमिकाओं और कार्यों के साथ डिजाइन करें, जिससे वे सहयोगी वर्कफ़्लो का परीक्षण और परिष्करण कर सकें।
- **Learn in Real-Time**: फीडबैक लूप्स लागू करें जहाँ एजेंट इंटरैक्शन से सीखते हैं और अपने व्यवहार को डायनामिक रूप से समायोजित करते हैं।

### Use Modular Components

SDKs जैसे Microsoft एजेंट फ़्रेमवर्क प्री-बिल्ट कॉम्पोनेंट्स प्रदान करते हैं जैसे AI कनेक्टर्स, टूल डेफिनिशन्स, और एजेंट मैनेजमेंट।

**How teams can use these**: टीमें जल्दी से इन कॉम्पोनेंट्स को जोड़कर एक कार्यात्मक प्रोटोटाइप बना सकती हैं बिना शुरुआत से सब कुछ बनाने के, जिससे तीव्र प्रयोग और पुनरावृत्ति संभव होती है।

**How it works in practice**: आप उपयोगकर्ता इनपुट से जानकारी निकालने के लिए एक प्री-बिल्ट पार्सर, डेटा स्टोर और पुनःप्राप्त करने के लिए एक मेमोरी मॉड्यूल, और उपयोगकर्ताओं के साथ इंटरैक्ट करने के लिए एक प्रॉम्प्ट जनरेटर का उपयोग कर सकते हैं, और यह सब बिना इन कॉम्पोनेंट्स को शून्य से बनाने के किया जा सकता है।

**Example code**. Let's look at an example of how you can use the Microsoft Agent Framework with `AzureAIProjectAgentProvider` to have the model respond to user input with tool calling:

``` python
# माइक्रोसॉफ्ट एजेंट फ्रेमवर्क पाइथन उदाहरण

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# यात्रा बुक करने के लिए एक नमूना टूल फ़ंक्शन परिभाषित करें
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
    # उदाहरण आउटपुट: आपकी फ्लाइट 1 जनवरी 2025 को न्यूयॉर्क के लिए सफलतापूर्वक बुक हो गई है। सुरक्षित यात्रा! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

What you can see from this example is how you can leverage a pre-built parser to extract key information from user input, such as the origin, destination, and date of a flight booking request. This modular approach allows you to focus on the high-level logic.

### Leverage Collaborative Tools

Frameworks like the Microsoft Agent Framework facilitate the creation of multiple agents that can work together.

**How teams can use these**: टीमें विशिष्ट भूमिकाओं और कार्यों के साथ एजेंट डिजाइन कर सकती हैं, जिससे वे सहयोगी वर्कफ़्लो का परीक्षण और सुधार कर सकें और समग्र सिस्टम की दक्षता बढ़ा सकें।

**How it works in practice**: आप एजेंट्स की एक टीम बना सकते हैं जहाँ प्रत्येक एजेंट का एक विशेष कार्य होता है, जैसे डेटा पुनःप्राप्ति, विश्लेषण, या निर्णय-निर्माण। ये एजेंट एक सामान्य लक्ष्य प्राप्त करने के लिए एक-दूसरे से संवाद और जानकारी साझा कर सकते हैं, जैसे उपयोगकर्ता प्रश्न का उत्तर देना या कोई कार्य पूरा करना।

**Example code (Microsoft Agent Framework)**:

```python
# माइक्रोसॉफ्ट एजेंट फ्रेमवर्क का उपयोग करके एक साथ काम करने वाले कई एजेंट बनाना

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# डेटा पुनःप्राप्ति एजेंट
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# डेटा विश्लेषण एजेंट
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# एक कार्य पर एजेंटों को क्रम में चलाना
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

What you see in the previous code is how you can create a task that involves multiple agents working together to analyze data. Each agent performs a specific function, and the task is executed by coordinating the agents to achieve the desired outcome. By creating dedicated agents with specialized roles, you can improve task efficiency and performance.

### Learn in Real-Time

Advanced frameworks provide capabilities for real-time context understanding and adaptation.

**How teams can use these**: टीमें ऐसे फीडबैक लूप्स लागू कर सकती हैं जहाँ एजेंट इंटरैक्शन से सीखते हैं और अपने व्यवहार को डायनामिक रूप से समायोजित करते हैं, जिससे क्षमताओं में सतत सुधार और परिष्करण होता है।

**How it works in practice**: एजेंट उपयोगकर्ता फीडबैक, पर्यावरणीय डेटा और कार्य परिणामों का विश्लेषण कर सकते हैं ताकि वे अपना नॉलेज बेस अपडेट करें, निर्णय-निर्माण एल्गोरिद्म समायोजित करें, और समय के साथ प्रदर्शन बेहतर करें। यह पुनरावर्ती सीखने की प्रक्रिया एजेंट्स को बदलती परिस्थितियों और उपयोगकर्ता प्राथमिकताओं के अनुसार अनुकूलित होने में सक्षम बनाती है, जो समग्र सिस्टम की प्रभावशीलता बढ़ाती है।

## What are the differences between the Microsoft Agent Framework and Azure AI Agent Service?

There are many ways to compare these approaches, but let's look at some key differences in terms of their design, capabilities, and target use cases:

## Microsoft Agent Framework (MAF)

The Microsoft Agent Framework provides a streamlined SDK for building AI agents using `AzureAIProjectAgentProvider`. It enables developers to create agents that leverage Azure OpenAI models with built-in tool calling, conversation management, and enterprise-grade security through Azure identity.

**Use Cases**: Building production-ready AI agents with tool use, multi-step workflows, and enterprise integration scenarios.

Here are some important core concepts of the Microsoft Agent Framework:

- **Agents**. An agent is created via `AzureAIProjectAgentProvider` and configured with a name, instructions, and tools. The agent can:
  - **Process user messages** and generate responses using Azure OpenAI models.
  - **Call tools** automatically based on the conversation context.
  - **Maintain conversation state** across multiple interactions.

  Here is a code snippet showing how to create an agent:

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

- **Tools**. The framework supports defining tools as Python functions that the agent can invoke automatically. Tools are registered when creating the agent:

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

- **Multi-Agent Coordination**. You can create multiple agents with different specializations and coordinate their work:

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

- **Azure Identity Integration**. The framework uses `AzureCliCredential` (or `DefaultAzureCredential`) for secure, keyless authentication, eliminating the need to manage API keys directly.

## Azure AI Agent Service

Azure AI Agent Service is a more recent addition, introduced at Microsoft Ignite 2024. It allows for the development and deployment of AI agents with more flexible models, such as directly calling open-source LLMs like Llama 3, Mistral, and Cohere.

Azure AI Agent Service provides stronger enterprise security mechanisms and data storage methods, making it suitable for enterprise applications. 

It works out-of-the-box with the Microsoft Agent Framework for building and deploying agents.

This service is currently in Public Preview and supports Python and C# for building agents.

Using the Azure AI Agent Service Python SDK, we can create an agent with a user-defined tool:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# उपकरण कार्यों को परिभाषित करें
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

Azure AI Agent Service has the following core concepts:

- **Agent**. Azure AI Agent Service integrates with Microsoft Foundry. Within AI Foundry, an AI Agent acts as a "smart" microservice that can be used to answer questions (RAG), perform actions, or completely automate workflows. It achieves this by combining the power of generative AI models with tools that allow it to access and interact with real-world data sources. Here's an example of an agent:

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

- **Integrates with the Microsoft Agent Framework**. Azure AI Agent Service works seamlessly with the Microsoft Agent Framework, which means you can build agents using `AzureAIProjectAgentProvider` and deploy them through the Agent Service for production scenarios.

**Use Cases**: Azure AI Agent Service is designed for enterprise applications that require secure, scalable, and flexible AI agent deployment.

## What's the difference between these approaches?
 
It does sound like there is overlap, but there are some key differences in terms of their design, capabilities, and target use cases:
 
- **Microsoft Agent Framework (MAF)**: Is a production-ready SDK for building AI agents. It provides a streamlined API for creating agents with tool calling, conversation management, and Azure identity integration.
- **Azure AI Agent Service**: Is a platform and deployment service in Azure Foundry for agents. It offers built-in connectivity to services like Azure OpenAI, Azure AI Search, Bing Search and code execution.
 
Still not sure which one to choose?

### Use Cases
 
Let's see if we can help you by going through some common use cases:
 
> Q: I'm building production AI agent applications and want to get started quickly
>

>A: The Microsoft Agent Framework is a great choice. It provides a simple, Pythonic API via `AzureAIProjectAgentProvider` that lets you define agents with tools and instructions in just a few lines of code.

>Q: I need enterprise-grade deployment with Azure integrations like Search and code execution
>
> A: Azure AI Agent Service is the best fit. It's a platform service that provides built-in capabilities for multiple models, Azure AI Search, Bing Search and Azure Functions. It makes it easy to build your agents in the Foundry Portal and deploy them at scale.
 
> Q: I'm still confused, just give me one option
>
> A: Start with the Microsoft Agent Framework to build your agents, and then use Azure AI Agent Service when you need to deploy and scale them in production. This approach lets you iterate quickly on your agent logic while having a clear path to enterprise deployment.
 
Let's summarize the key differences in a table:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?
उत्तर हाँ है, आप अपने मौजूदा Azure इकोसिस्टम टूल्स को सीधे Azure AI Agent Service के साथ एकीकृत कर सकते हैं, क्योंकि इसे अन्य Azure सेवाओं के साथ निर्बाध रूप से काम करने के लिए बनाया गया है। उदाहरण के लिए आप Bing, Azure AI Search, और Azure Functions को एकीकृत कर सकते हैं। Microsoft Foundry के साथ भी गहरा एकीकरण है।

The Microsoft Agent Framework also integrates with Azure services through `AzureAIProjectAgentProvider` and Azure identity, letting you call Azure services directly from your agent tools.

## नमूना कोड

- Python: [एजेंट फ्रेमवर्क](./code_samples/02-python-agent-framework.ipynb)
- .NET: [एजेंट फ्रेमवर्क](./code_samples/02-dotnet-agent-framework.md)

## क्या AI एजेंट फ्रेमवर्क के बारे में आपके और प्रश्न हैं?

अन्य शिक्षार्थियों से मिलने, ऑफिस आवर्स में शामिल होने और अपने AI Agents से संबंधित प्रश्नों के उत्तर पाने के लिए [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) से जुड़ें।

## संदर्भ

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure एजेंट सेवा</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI प्रतिक्रियाएँ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent सेवा</a>

## पिछला पाठ

[AI एजेंट और एजेंट उपयोग मामलों का परिचय](../01-intro-to-ai-agents/README.md)

## अगला पाठ

[एजेंटिक डिज़ाइन पैटर्न्स को समझना](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यह दस्तावेज़ एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->