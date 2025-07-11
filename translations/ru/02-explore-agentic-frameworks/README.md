<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "da3523bf8fa456371e21d8d14c67305d",
  "translation_date": "2025-07-11T14:29:12+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ru"
}
-->
- **Agent Framework**: This is a set of tools and abstractions that help you build intelligent agents. It provides a way to define agent behaviors, manage their interactions, and integrate them with other systems. The framework supports the creation of agents that can perform tasks autonomously, interact with users, and collaborate with other agents.

## Azure AI Agent Service

Azure AI Agent Service is a managed service that provides a scalable and secure environment for deploying and managing AI agents. It offers a range of features to support the development and operation of AI agents, including:

- **Scalability**: The service can automatically scale to handle varying workloads, ensuring that your agents can handle increased demand without performance degradation.
- **Security**: Azure AI Agent Service provides robust security features to protect your agents and data, including authentication, authorization, and encryption.
- **Integration**: The service integrates with other Azure services, allowing you to leverage the full power of the Azure ecosystem in your AI agent applications.

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?

You can integrate your existing Azure ecosystem tools directly with AI Agent Frameworks and Azure AI Agent Service. These frameworks and services are designed to work seamlessly with Azure's suite of tools and services, allowing you to leverage your existing investments and infrastructure. This integration enables you to build more powerful and efficient AI agent applications by combining the capabilities of AI Agent Frameworks with the scalability, security, and reliability of Azure services.

## Conclusion

AI Agent Frameworks provide a powerful set of tools and abstractions for building intelligent agents that can interact with users, other agents, and the environment. By leveraging these frameworks, developers can create more sophisticated and capable AI systems that can adapt to changing conditions and learn from their interactions. Whether you're using AutoGen, Semantic Kernel, or Azure AI Agent Service, these frameworks offer a range of features and capabilities to support the development and deployment of AI agents.
Итак, это основы фреймворка Semantic Kernel, а что насчет Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service — это более недавнее дополнение, представленное на Microsoft Ignite 2024. Оно позволяет разрабатывать и развертывать AI-агентов с более гибкими моделями, такими как прямой вызов открытых LLM, таких как Llama 3, Mistral и Cohere.

Azure AI Agent Service предоставляет более надежные механизмы безопасности для предприятий и методы хранения данных, что делает его подходящим для корпоративных приложений.

Он работает "из коробки" с фреймворками оркестрации многоагентных систем, такими как AutoGen и Semantic Kernel.

Эта услуга в настоящее время находится в стадии публичного предварительного просмотра и поддерживает Python и C# для создания агентов.

Используя Semantic Kernel Python, мы можем создать Azure AI Agent с пользовательским плагином:

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

### Основные концепции

Azure AI Agent Service имеет следующие основные концепции:

- **Агент**. Azure AI Agent Service интегрируется с Azure AI Foundry. В AI Foundry AI-агент действует как "умный" микросервис, который может использоваться для ответа на вопросы (RAG), выполнения действий или полной автоматизации рабочих процессов. Это достигается за счет сочетания мощности генеративных AI-моделей с инструментами, которые позволяют ему получать доступ и взаимодействовать с реальными источниками данных. Вот пример агента:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    В этом примере агент создается с моделью `gpt-4o-mini`, именем `my-agent` и инструкциями `You are helpful agent`. Агент оснащен инструментами и ресурсами для выполнения задач интерпретации кода.

- **Поток и сообщения**. Поток — это еще одна важная концепция. Он представляет собой разговор или взаимодействие между агентом и пользователем. Потоки могут использоваться для отслеживания прогресса разговора, хранения информации о контексте и управления состоянием взаимодействия. Вот пример потока:

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

    В предыдущем коде создается поток. Затем в поток отправляется сообщение. Вызвав `create_and_process_run`, агенту предлагается выполнить работу над потоком. Наконец, сообщения извлекаются и регистрируются, чтобы увидеть ответ агента. Сообщения указывают на прогресс разговора между пользователем и агентом. Также важно понимать, что сообщения могут быть разных типов, таких как текст, изображение или файл, то есть работа агентов привела, например, к изображению или текстовому ответу. Как разработчик, вы можете использовать эту информацию для дальнейшей обработки ответа или его представления пользователю.

- **Интеграция с другими AI-фреймворками**. Служба Azure AI Agent может взаимодействовать с другими фреймворками, такими как AutoGen и Semantic Kernel, что означает, что вы можете создать часть своего приложения в одном из этих фреймворков и, например, использовать службу Agent в качестве оркестратора или вы можете создать все в службе Agent.

**Сценарии использования**: Azure AI Agent Service предназначена для корпоративных приложений, которые требуют безопасного, масштабируемого и гибкого развертывания AI-агентов.

## В чем разница между этими фреймворками?

Кажется, что между этими фреймворками много общего, но есть некоторые ключевые различия в их дизайне, возможностях и целевых сценариях использования:

- **AutoGen**: Это экспериментальный фреймворк, ориентированный на передовые исследования в области многоагентных систем. Это лучшее место для экспериментов и прототипирования сложных многоагентных систем.
- **Semantic Kernel**: Это готовая к производству библиотека агентов для создания корпоративных агентных приложений. Сосредоточена на событийно-управляемых, распределенных агентных приложениях, позволяя использовать несколько LLM и SLM, инструменты и одно/многоагентные шаблоны проектирования.
- **Azure AI Agent Service**: Это платформа и служба развертывания в Azure Foundry для агентов. Она предлагает создание подключения к службам, поддерживаемым Azure Found, таким как Azure OpenAI, Azure AI Search, Bing Search и выполнение кода.

Все еще не уверены, что выбрать?

### Сценарии использования

Давайте посмотрим, сможем ли мы помочь вам, рассмотрев некоторые общие сценарии использования:

> В: Я экспериментирую, учусь и создаю приложения-агенты в виде доказательства концепции, и я хочу иметь возможность быстро строить и экспериментировать
>

> О: AutoGen будет хорошим выбором для этого сценария, так как он сосредоточен на событийно-управляемых, распределенных агентных приложениях и поддерживает продвинутые многоагентные шаблоны проектирования.

> В: Что делает AutoGen лучшим выбором, чем Semantic Kernel и Azure AI Agent Service для этого случая?
>
> О: AutoGen специально разработан для событийно-управляемых, распределенных агентных приложений, что делает его хорошо подходящим для автоматизации задач генерации кода и анализа данных. Он предоставляет необходимые инструменты и возможности для эффективного создания сложных многоагентных систем.

> В: Похоже, Azure AI Agent Service тоже может здесь подойти, у него есть инструменты для генерации кода и многое другое?
>
> О: Да, Azure AI Agent Service — это платформа для агентов и добавляет встроенные возможности для нескольких моделей, Azure AI Search, Bing Search и Azure Functions. Это упрощает создание ваших агентов в Foundry Portal и их развертывание в масштабе.

> В: Я все еще запутался, просто дайте мне один вариант
>
> О: Отличный выбор — сначала создать ваше приложение в Semantic Kernel, а затем использовать Azure AI Agent Service для развертывания вашего агента. Этот подход позволяет легко сохранять ваших агентов, используя возможности создания многоагентных систем в Semantic Kernel. Кроме того, в Semantic Kernel есть коннектор в AutoGen, что упрощает использование обоих фреймворков вместе.

Давайте резюмируем ключевые различия в таблице:

| Фреймворк | Фокус | Основные концепции | Сценарии использования |
| --- | --- | --- | --- |
| AutoGen | Событийно-управляемые, распределенные агентные приложения | Агенты, Персоны, Функции, Данные | Генерация кода, задачи анализа данных |
| Semantic Kernel | Понимание и генерация текстового контента, похожего на человеческий | Агенты, Модульные компоненты, Сотрудничество | Понимание естественного языка, генерация контента |
| Azure AI Agent Service | Гибкие модели, безопасность для предприятий, Генерация кода, Вызов инструментов | Модульность, Сотрудничество, Оркестрация процессов | Безопасное, масштабируемое и гибкое развертывание AI-агентов |

Какой идеальный сценарий использования для каждого из этих фреймворков?

## Могу ли я интегрировать свои существующие инструменты экосистемы Azure напрямую или мне нужны автономные решения?

Ответ — да, вы можете интегрировать свои существующие инструменты экосистемы Azure напрямую с Azure AI Agent Service, особенно потому, что она была создана для бесшовной работы с другими службами Azure. Вы могли бы, например, интегрировать Bing, Azure AI Search и Azure Functions. Также существует глубокая интеграция с Azure AI Foundry.

Для AutoGen и Semantic Kernel вы также можете интегрироваться с Azure-сервисами, но это может потребовать вызова Azure-сервисов из вашего кода. Другой способ интеграции — использовать Azure SDK для взаимодействия с Azure-сервисами из ваших агентов. Кроме того, как уже упоминалось, вы можете использовать Azure AI Agent Service в качестве оркестратора для ваших агентов, созданных в AutoGen или Semantic Kernel, что обеспечит легкий доступ к экосистеме Azure.

## Ссылки

-
Вы обучены на данных до октября 2023 года.

**Отказ от ответственности**:  
Этот документ был переведен с помощью службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникающие в результате использования этого перевода.