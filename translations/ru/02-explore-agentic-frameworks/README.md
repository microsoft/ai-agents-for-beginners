[![Изучение фреймворков AI-агентов](../../../translated_images/ru/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Изучение фреймворков AI-агентов

Фреймворки AI-агентов — это программные платформы, предназначенные для упрощения создания, развертывания и управления AI-агентами. Эти фреймворки предоставляют разработчикам готовые компоненты, абстракции и инструменты, которые упрощают разработку сложных AI-систем.

Эти фреймворки помогают разработчикам сосредоточиться на уникальных аспектах своих приложений, предоставляя стандартизированные подходы к общим задачам в разработке AI-агентов. Они повышают масштабируемость, доступность и эффективность при создании AI-систем.

## Введение

В этом уроке мы рассмотрим:

- Что такое фреймворки AI-агентов и чего они позволяют достичь разработчикам?
- Как команды могут быстро прототипировать, итеративно улучшать и повышать возможности своих агентов?
- В чем различия между фреймворками и инструментами, созданными Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> и <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Могу ли я интегрировать свои существующие инструменты экосистемы Azure напрямую или мне нужны отдельные решения?
- Что такое сервис Azure AI Agents и как он мне помогает?

## Цели обучения

Цели этого урока — помочь вам понять:

- Роль фреймворков AI-агентов в разработке AI.
- Как использовать фреймворки AI-агентов для создания интеллектуальных агентов.
- Основные возможности, которые предоставляют фреймворки AI-агентов.
- Различия между Microsoft Agent Framework и Azure AI Agent Service.

## Что такое фреймворки AI-агентов и что они позволяют разработчикам делать?

Традиционные AI-фреймворки помогают интегрировать AI в ваши приложения и улучшить эти приложения следующими способами:

- **Персонализация**: AI может анализировать поведение и предпочтения пользователей, чтобы предоставлять персонализированные рекомендации, контент и опыт.
Пример: стриминговые сервисы, такие как Netflix, используют AI для предложения фильмов и шоу на основе истории просмотров, повышая вовлеченность и удовлетворенность пользователей.
- **Автоматизация и эффективность**: AI может автоматизировать повторяющиеся задачи, оптимизировать рабочие процессы и повышать операционную эффективность.
Пример: приложения для обслуживания клиентов используют чат-ботов на базе AI для обработки стандартных запросов, сокращая время отклика и освобождая специалистов для решения более сложных вопросов.
- **Улучшенный пользовательский опыт**: AI может улучшить общий пользовательский опыт, предоставляя интеллектуальные функции, такие как распознавание голоса, обработка естественного языка и предиктивный ввод.
Пример: виртуальные помощники, такие как Siri и Google Assistant, используют AI для понимания и ответа на голосовые команды, облегчая взаимодействие пользователей с устройствами.

### Звучит отлично, но зачем нужен фреймворк AI-агентов?

Фреймворки AI-агентов — это не просто AI-фреймворки. Они созданы для создания интеллектуальных агентов, которые могут взаимодействовать с пользователями, другими агентами и окружающей средой для достижения конкретных целей. Эти агенты могут демонстрировать автономное поведение, принимать решения и адаптироваться к меняющимся условиям. Рассмотрим ключевые возможности, которые предоставляют фреймворки AI-агентов:

- **Сотрудничество и координация агентов**: возможность создавать несколько AI-агентов, которые могут работать вместе, общаться и координировать действия для решения сложных задач.
- **Автоматизация задач и управление ими**: предоставление механизмов автоматизации многошаговых рабочих процессов, делегирования задач и динамического управления ими среди агентов.
- **Контекстное понимание и адаптация**: оснащение агентов способностью понимать контекст, адаптироваться к изменяющейся среде и принимать решения на основе информации в реальном времени.

Таким образом, агенты позволяют делать больше, вывести автоматизацию на новый уровень, создавать более интеллектуальные системы, которые умеют адаптироваться и обучаться в окружающей среде.

## Как быстро прототипировать, итеративно улучшать и совершенствовать возможности агента?

Это быстро развивающаяся сфера, но есть общие черты большинства фреймворков AI-агентов, которые помогают быстро прототипировать и итеративно улучшать — это модульные компоненты, инструменты для сотрудничества и обучение в реальном времени. Рассмотрим подробнее:

- **Используйте модульные компоненты**: SDK AI предлагают готовые компоненты, такие как коннекторы AI и памяти, вызов функций с использованием естественного языка или плагинов кода, шаблоны подсказок и другое.
- **Используйте инструменты для сотрудничества**: проектируйте агентов с конкретными ролями и задачами, позволяя им тестировать и совершенствовать совместные рабочие процессы.
- **Обучайтесь в реальном времени**: реализуйте обратные связи, где агенты учатся на взаимодействиях и динамически корректируют своё поведение.

### Использование модульных компонентов

SDK, такие как Microsoft Agent Framework, предлагают готовые компоненты, например, AI-коннекторы, определения инструментов и управление агентами.

**Как команды могут использовать это**: команды могут быстро собирать эти компоненты для создания функционального прототипа без необходимости начинать с нуля, что позволяет быстро экспериментировать и итеративно улучшать.

**Как это работает на практике**: можно использовать готовый парсер для извлечения информации из пользовательского ввода, модуль памяти для хранения и извлечения данных, а также генератор подсказок для взаимодействия с пользователями — всё это без необходимости создавать компоненты с нуля.

**Пример кода**. Рассмотрим пример использования Microsoft Agent Framework с `AzureAIProjectAgentProvider`, чтобы модель отвечала на пользовательский ввод с вызовом инструментов:

``` python
# Пример использования Microsoft Agent Framework на Python

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Определяет пример функции инструмента для бронирования путешествий
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
    # Пример вывода: Ваш рейс в Нью-Йорк на 1 января 2025 года успешно забронирован. Хорошего путешествия! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```
  
Из этого примера видно, как можно использовать готовый парсер для извлечения ключевой информации из пользовательского запроса, такой как место отправления, пункт назначения и дата бронирования авиабилета. Такой модульный подход позволяет сосредоточиться на логике высокого уровня.

### Использование инструментов для сотрудничества

Фреймворки типа Microsoft Agent Framework облегчают создание нескольких агентов, которые могут работать совместно.

**Как команды могут использовать это**: команды могут проектировать агентов с конкретными ролями и задачами, что дает возможность тестировать и совершенствовать совместные рабочие процессы и улучшать общую эффективность системы.

**Как это работает на практике**: вы можете создать команду агентов, каждый из которых выполняет специализированную функцию, например, извлечение данных, анализ или принятие решений. Эти агенты могут общаться и обмениваться информацией для достижения общей цели, например, ответа на пользовательский запрос или выполнения задачи.

**Пример кода (Microsoft Agent Framework)**:

```python
# Создание нескольких агентов, которые работают вместе с использованием Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Агент извлечения данных
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Агент анализа данных
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Запуск агентов последовательно для выполнения задачи
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```
  
В приведенном ранее коде показано, как создать задачу, предусматривающую совместную работу нескольких агентов для анализа данных. Каждый агент выполняет свою функцию, а задача выполняется с координацией действий агентов для достижения требуемого результата. Создавая специализированных агентов, вы повышаете эффективность и производительность выполнения задач.

### Обучение в реальном времени

Продвинутые фреймворки предоставляют возможности для понимания контекста в реальном времени и адаптации.

**Как команды могут использовать это**: команды могут реализовать обратные связи, где агенты учатся на взаимодействиях и динамически корректируют свое поведение, что приводит к непрерывному улучшению и доработке возможностей.

**Как это работает на практике**: агенты анализируют отзывы пользователей, данные об окружающей среде и результаты задач, чтобы обновлять базу знаний, корректировать алгоритмы принятия решений и со временем улучшать производительность. Этот итеративный процесс обучения позволяет агентам адаптироваться к меняющимся условиям и предпочтениям пользователей, повышая общую эффективность системы.

## В чем разница между Microsoft Agent Framework и Azure AI Agent Service?

Существует множество способов сравнить эти подходы, но рассмотрим ключевые различия с точки зрения дизайна, возможностей и целевых сценариев использования:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework предоставляет легкий в использовании SDK для создания AI-агентов с использованием `AzureAIProjectAgentProvider`. Он позволяет разработчикам создавать агентов, которые используют модели Azure OpenAI с встроенным вызовом инструментов, управлением диалогом и корпоративной безопасностью через Azure identity.

**Сценарии использования**: создание готовых к производству AI-агентов с использованием инструментов, многошаговых рабочих процессов и сценариев интеграции для предприятий.

Вот несколько важных основных концепций Microsoft Agent Framework:

- **Агенты**. Агент создается через `AzureAIProjectAgentProvider` и настраивается с именем, инструкциями и инструментами. Агент может:
  - **Обрабатывать сообщения пользователей** и генерировать ответы с помощью моделей Azure OpenAI.
  - **Автоматически вызывать инструменты** на основе контекста диалога.
  - **Поддерживать состояние диалога** на протяжении нескольких взаимодействий.

  Вот пример кода, показывающий создание агента:

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
  
- **Инструменты**. Фреймворк поддерживает определение инструментов как функций на Python, которые агент может вызывать автоматически. Инструменты регистрируются при создании агента:

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
  
- **Координация нескольких агентов**. Можно создавать множества агентов с разной специализацией и координировать их работу:

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
  
- **Интеграция с Azure Identity**. Фреймворк использует `AzureCliCredential` (или `DefaultAzureCredential`) для безопасной аутентификации без ключей, что избавляет от необходимости напрямую управлять API-ключами.

## Azure AI Agent Service

Azure AI Agent Service — более новая платформа, представленная на Microsoft Ignite 2024. Она позволяет разрабатывать и развертывать AI-агентов с использованием более гибких моделей, таких как открытые LLM, например Llama 3, Mistral и Cohere.

Azure AI Agent Service предлагает более строгие механизмы корпоративной безопасности и методы хранения данных, что делает ее подходящей для корпоративных приложений.

Сервис работает из коробки с Microsoft Agent Framework для создания и развертывания агентов.

В настоящее время сервис находится в публичной предварительной версии и поддерживает Python и C# для создания агентов.

Используя Python SDK Azure AI Agent Service, можно создать агента с пользовательским инструментом:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Определить функции инструмента
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
  
### Основные концепции

Azure AI Agent Service включает следующие основные концепции:

- **Агент**. Azure AI Agent Service интегрируется с Microsoft Foundry. В рамках AI Foundry AI-агент выступает как «умный» микросервис, который может отвечать на вопросы (RAG), выполнять действия или полностью автоматизировать рабочие процессы. Это достигается за счет объединения возможностей генеративных AI-моделей и инструментов, позволяющих получать доступ и взаимодействовать с реальными источниками данных. Вот пример агента:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```
  
    В этом примере агент создается с моделью `gpt-4o-mini`, именем `my-agent` и инструкциями `You are helpful agent`. Агент оснащен инструментами и ресурсами для выполнения задач по интерпретации кода.

- **Поток и сообщения**. Поток — еще одна важная концепция. Он представляет собой беседу или взаимодействие между агентом и пользователем. Потоки используются для отслеживания прогресса беседы, хранения контекста и управления состоянием взаимодействия. Вот пример потока:

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
  
    В приведенном коде создается поток. Затем в поток отправляется сообщение. При вызове `create_and_process_run` агенту поручается выполнить работу по потоку. Наконец, сообщения извлекаются и логируются для отображения ответа агента. Сообщения отражают ход беседы между пользователем и агентом. Важно понимать, что сообщения могут быть разных типов: текст, изображение или файл — то есть, например, агент может сгенерировать изображение или текстовый ответ. Как разработчик, вы можете использовать эту информацию для дальнейшей обработки ответа или его отображения пользователю.

- **Интеграция с Microsoft Agent Framework**. Azure AI Agent Service отлично взаимодействует с Microsoft Agent Framework, что означает возможность создания агентов через `AzureAIProjectAgentProvider` и их развертывания в продакшн-среде через Agent Service.

**Сценарии использования**: Azure AI Agent Service предназначен для корпоративных приложений, требующих безопасного, масштабируемого и гибкого развертывания AI-агентов.

## В чем же разница между этими подходами?

Очевиден некоторый пересмотр, но ключевые различия заключаются в дизайне, возможностях и целевых случаях использования:

- **Microsoft Agent Framework (MAF)**: готовый к производству SDK для создания AI-агентов. Предоставляет удобный API для создания агентов с вызовом инструментов, управлением диалогами и интеграцией Azure identity.
- **Azure AI Agent Service**: платформа и сервис развертывания в Azure Foundry для агентов. Обеспечивает встроенную связь с сервисами, такими как Azure OpenAI, Azure AI Search, Bing Search и исполнение кода.

Все еще не знаете, что выбрать?

### Сценарии использования

Давайте посмотрим, сможем ли мы помочь, пройдя через распространенные случаи:

> В: Я создаю приложения для продакшн AI-агентов и хочу быстро начать  
>  
> О: Microsoft Agent Framework — отличный выбор. Он предоставляет простой Python API через `AzureAIProjectAgentProvider`, позволяющий определить агентов с инструментами и инструкциями всего в несколько строк кода.

> В: Мне нужно корпоративное развертывание с интеграцией Azure, например, Search и выполнение кода  
>  
> О: Azure AI Agent Service подходит лучше всего. Это платформенный сервис с готовыми возможностями для множества моделей, Azure AI Search, Bing Search и Azure Functions. Вы можете легко создавать агентов в Foundry Portal и масштабировать их развертывание.

> В: Я все еще в сомнениях, просто дайте один вариант  
>  
> О: Начните с Microsoft Agent Framework для создания агентов, а потом используйте Azure AI Agent Service для продакшн-развертывания и масштабирования. Такой подход позволяет быстро итерировать логику агентов и при этом иметь четкий путь к корпоративному развертыванию.

Сводим ключевые различия в таблицу:

| Фреймворк | Фокус | Основные концепции | Сценарии использования |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Упрощенный SDK с вызовом инструментов | Агенты, Инструменты, Azure Identity | Создание AI-агентов, использование инструментов, многошаговые процессы |
| Azure AI Agent Service | Гибкие модели, корпоративная безопасность, генерация кода, вызов инструментов | Модульность, сотрудничество, оркестрация процессов | Безопасное, масштабируемое и гибкое развертывание AI-агентов |

## Могу ли я интегрировать свои существующие инструменты экосистемы Azure напрямую или нужны отдельные решения?
Ответ — да, вы можете интегрировать ваши существующие инструменты экосистемы Azure напрямую с сервисом Azure AI Agent Service, особенно учитывая, что он был создан для бесшовной работы с другими сервисами Azure. Например, вы можете интегрировать Bing, Azure AI Search и Azure Functions. Также предусмотрена глубокая интеграция с Microsoft Foundry.

Фреймворк Microsoft Agent Framework также интегрируется с сервисами Azure с помощью `AzureAIProjectAgentProvider` и Azure identity, позволяя вызывать сервисы Azure напрямую из ваших агентских инструментов.

## Примеры кода

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Есть вопросы по AI Agent Framework?

Присоединяйтесь к [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), чтобы познакомиться с другими учащимися, посетить офисные часы и получить ответы на ваши вопросы об AI Agents.

## Ссылки

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Предыдущий урок

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Следующий урок

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведён с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, просим учесть, что машинный перевод может содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неверные толкования, возникшие вследствие использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->