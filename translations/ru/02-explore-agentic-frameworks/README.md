[![Изучение фреймворков AI-агентов](../../../translated_images/ru/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Изучение фреймворков AI-агентов

Фреймворки AI-агентов — это программные платформы, предназначенные для упрощения создания, развертывания и управления AI-агентами. Эти фреймворки предоставляют разработчикам готовые компоненты, абстракции и инструменты, которые упрощают разработку сложных AI-систем.

Эти фреймворки помогают разработчикам сосредоточиться на уникальных аспектах своих приложений, предоставляя стандартизированные подходы к распространённым задачам в разработке AI-агентов. Они повышают масштабируемость, доступность и эффективность создания AI-систем.

## Введение 

В этом уроке мы рассмотрим:

- Что такое фреймворки AI-агентов и что они позволяют разработчикам достичь?
- Как команды могут использовать их для быстрого прототипирования, итераций и улучшения возможностей агента?
- В чем различия между фреймворками и инструментами, созданными Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> и <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Могу ли я интегрировать существующие инструменты экосистемы Azure напрямую или мне нужны отдельные решения?
- Что такое Microsoft Foundry Agent Service и как он помогает мне?

## Цели обучения

Цели этого урока — помочь вам понять:

- Роль фреймворков AI-агентов в разработке AI.
- Как использовать фреймворки AI-агентов для создания интеллектуальных агентов.
- Ключевые возможности, предоставляемые фреймворками AI-агентов.
- Различия между Microsoft Agent Framework и Microsoft Foundry Agent Service.

## Что такое фреймворки AI-агентов и что они позволяют разработчикам делать?

Традиционные AI-фреймворки могут помочь интегрировать AI в ваши приложения и улучшить их следующим образом:

- **Персонализация**: AI может анализировать поведение пользователей и предпочтения, чтобы предоставлять персонализированные рекомендации, контент и опыт.
Пример: Сервисы потокового видео, такие как Netflix, используют AI для предложения фильмов и сериалов на основе истории просмотров, повышая вовлечённость и удовлетворенность пользователей.
- **Автоматизация и эффективность**: AI может автоматизировать повторяющиеся задачи, оптимизировать рабочие процессы и повышать операционную эффективность.
Пример: Приложения службы поддержки используют чат-ботов на базе AI для обработки типичных запросов, сокращая время ответа и освобождая сотрудников для решения более сложных задач.
- **Улучшенный пользовательский опыт**: AI может улучшать весь пользовательский опыт, предоставляя интеллектуальные функции, такие как распознавание голоса, обработка естественного языка и предиктивный ввод.
Пример: Виртуальные ассистенты, такие как Siri и Google Assistant, используют AI для понимания и реагирования на голосовые команды, облегчая взаимодействие пользователей с устройствами.

### Всё это звучит отлично, но зачем нам фреймворк AI-агента?

Фреймворки AI-агентов — это не просто AI-фреймворки. Они предназначены для создания интеллектуальных агентов, которые могут взаимодействовать с пользователями, другими агентами и окружающей средой для достижения конкретных целей. Эти агенты могут проявлять автономное поведение, принимать решения и адаптироваться к меняющимся условиям. Рассмотрим ключевые возможности, которые предоставляют фреймворки AI-агентов:

- **Взаимодействие и координация агентов**: Позволяют создавать множество AI-агентов, которые могут работать вместе, общаться и координироваться для решения сложных задач.
- **Автоматизация и управление задачами**: Обеспечивают механизмы автоматизации многошаговых рабочих процессов, делегирования задач и динамического управления задачами между агентами.
- **Контекстуальное понимание и адаптация**: Предоставляют агентам возможность понимать контекст, адаптироваться к изменяющимся условиям и принимать решения на основе информации в реальном времени.

Таким образом, агенты позволяют сделать больше, вывести автоматизацию на новый уровень, создавать более интеллектуальные системы, которые могут адаптироваться и учиться на основе окружения.

## Как быстро прототипировать, итеративно улучшать и развивать возможности агента?

Это быстро меняющийся ландшафт, но есть некоторые общие особенности большинства AI-фреймворков агентов, которые могут помочь быстро прототипировать и итеративно улучшать — это модульные компоненты, инструменты совместной работы и обучение в реальном времени. Рассмотрим их подробнее:

- **Использование модульных компонентов**: AI SDK предлагают готовые компоненты, такие как AI- и память-коннекторы, вызов функций через естественный язык или плагины кода, шаблоны запросов и многое другое.
- **Использование инструментов совместной работы**: Проектируйте агентов с определёнными ролями и задачами, что позволяет тестировать и совершенствовать совместные рабочие процессы.
- **Обучение в реальном времени**: Реализуйте обратную связь, при которой агенты учатся на взаимодействиях и динамически корректируют своё поведение.

### Использование модульных компонентов

SDK, такие как Microsoft Agent Framework, предлагают готовые компоненты — AI-коннекторы, определения инструментов и управление агентами.

**Как команды могут использовать их**: Команды могут быстро собрать функциональный прототип без написания с нуля, что позволяет быстро экспериментировать и итеративно улучшать.

**Как это работает на практике**: Можно использовать готовый парсер для извлечения информации из пользовательского ввода, модуль памяти для хранения и извлечения данных, генератор запросов для взаимодействия с пользователями — всё это без создания компонентов с нуля.

**Пример кода**. Рассмотрим пример того, как использовать Microsoft Agent Framework с `FoundryChatClient` для того, чтобы модель отвечала на ввод пользователя с вызовом инструментов:

``` python
# Пример на Python для Microsoft Agent Framework

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Определите пример функции инструмента для бронирования поездки
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
    # Пример вывода: Ваш рейс в Нью-Йорк на 1 января 2025 года был успешно забронирован. Счастливого пути! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Из этого примера видно, как можно использовать готовый парсер для извлечения ключевой информации из пользовательского ввода, такой как origin, destination и дата запроса на бронирование рейса. Такой модульный подход позволяет сосредоточиться на логике высокого уровня.

### Использование инструментов совместной работы

Фреймворки, такие как Microsoft Agent Framework, облегчают создание нескольких агентов, которые могут сотрудничать.

**Как команды могут использовать их**: Команды могут проектировать агентов с определёнными ролями и задачами, что позволяет тестировать и улучшать совместные рабочие процессы и повышать эффективность общей системы.

**Как это работает на практике**: Вы можете создать команду агентов, где каждый агент выполняет специализированную функцию, например, извлечение данных, анализ или принятие решений. Эти агенты могут общаться и обмениваться информацией для достижения общей цели — например, ответа на запрос пользователя или выполнения задачи.

**Пример кода (Microsoft Agent Framework)**:

```python
# Создание нескольких агентов, которые работают вместе с использованием Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Агент извлечения данных
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Агент анализа данных
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Выполнение агентов последовательно по задаче
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

В приведённом коде показано, как создать задачу, включающую несколько агентов, работающих вместе для анализа данных. Каждый агент выполняет конкретную функцию, а задача выполняется путём координации работы агентов для достижения желаемого результата. Создавая специализированных агентов, можно повысить эффективность и производительность задачи.

### Обучение в реальном времени

Продвинутые фреймворки предоставляют возможности для понимания контекста и адаптации в реальном времени.

**Как команды могут использовать их**: Команды могут реализовывать обратные связи, где агенты учатся на взаимодействиях и динамически корректируют поведение, что ведёт к постоянному улучшению и развитию возможностей.

**Как это работает на практике**: Агенты могут анализировать отзывы пользователей, данные из окружающей среды и результаты задач, обновлять базу знаний, корректировать алгоритмы принятия решений и со временем улучшать результаты. Этот итеративный процесс обучения позволяет агентам адаптироваться к изменяющимся условиям и предпочтениям пользователей, повышая эффективность всей системы.

## В чем различия между Microsoft Agent Framework и Microsoft Foundry Agent Service?

Сравнений этих подходов много, но рассмотрим ключевые различия в дизайне, возможностях и целевых сценариях использования:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework предоставляет упрощённый SDK для создания AI-агентов с использованием `FoundryChatClient`. Это позволяет разработчикам создавать агентов с использованием моделей Azure OpenAI с встроенным вызовом инструментов, управлением беседой и корпоративной защитой через Azure identity.

**Сценарии использования**: Создание готовых к производству AI-агентов с использованием инструментов, многошаговыми рабочими процессами и интеграцией в корпоративные среды.

Вот некоторые важные ключевые понятия в Microsoft Agent Framework:

- **Агенты**. Агент создаётся через `FoundryChatClient` и настраивается с именем, инструкциями и инструментами. Агент может:
  - **Обрабатывать сообщения пользователей** и генерировать ответы с помощью моделей Azure OpenAI.
  - **Автоматически вызывать инструменты** в зависимости от контекста беседы.
  - **Поддерживать состояние беседы** на протяжении нескольких взаимодействий.

  Вот пример кода, показывающий создание агента:

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

- **Инструменты**. Фреймворк поддерживает определение инструментов как функций Python, которые агент может автоматически вызывать. Инструменты регистрируются при создании агента:

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

- **Координация нескольких агентов**. Можно создавать нескольких агентов с разными специализациями и координировать их работу:

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

- **Интеграция Azure identity**. Фреймворк использует `AzureCliCredential` (или `DefaultAzureCredential`) для безопасной аутентификации без ключей, исключая необходимость прямо управлять API-ключами.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service — это более новый продукт, представленный на Microsoft Ignite 2024. Он позволяет разрабатывать и развертывать AI-агентов с более гибкими моделями, такими как вызов open-source LLM, например Llama 3, Mistral и Cohere.

Microsoft Foundry Agent Service предлагает более мощные механизмы корпоративной безопасности и методы хранения данных, что делает его подходящим для корпоративных приложений. 

Он работает из коробки с Microsoft Agent Framework для создания и развертывания агентов.

Эта служба сейчас находится в публичном превью и поддерживает Python и C# для создания агентов.

С помощью Python SDK Microsoft Foundry Agent Service можно создать агента с инструментом, определённым пользователем:

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

### Основные концепции

Microsoft Foundry Agent Service включает в себя следующие ключевые понятия:

- **Агент**. Microsoft Foundry Agent Service интегрируется с Microsoft Foundry. В Foundry AI Agent выступает как «умный» микросервис, который можно использовать для ответов на вопросы (RAG), выполнения действий или полной автоматизации рабочих процессов. Это достигается за счёт сочетания генеративных AI-моделей с инструментами, позволяющими обращаться и взаимодействовать с реальными источниками данных. Вот пример агента:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    В этом примере агент создаётся с моделью `gpt-5-mini`, именем `my-agent` и инструкциями `You are helpful agent`. Агент оснащён инструментами и ресурсами для выполнения задач интерпретации кода.

- **Поток и сообщения**. Поток — ещё одна важная концепция. Он представляет собой беседу или взаимодействие между агентом и пользователем. Потоки используются для отслеживания хода беседы, хранения контекстной информации и управления состоянием взаимодействия. Вот пример потока:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Попросить агента выполнить работу в потоке
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Получить и записать все сообщения, чтобы увидеть ответ агента
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    В приведённом коде создаётся поток. Затем в поток отправляется сообщение. Вызовом `create_and_process_run` агенту поручается выполнить работу в рамках потока. Наконец, сообщения извлекаются и логируются для просмотра ответа агента. Сообщения отражают ход беседы между пользователем и агентом. Важно понимать, что сообщения могут быть разных типов, таких как текст, изображение или файл — то есть работа агента может привести к созданию, например, изображения или текстового ответа. Как разработчик, вы можете использовать эту информацию для дальнейшей обработки ответа или его отображения пользователю.

- **Интеграция с Microsoft Agent Framework**. Microsoft Foundry Agent Service работает безупречно с Microsoft Agent Framework, что позволяет строить агентов с помощью `FoundryChatClient` и развертывать их через Agent Service для производственных сценариев.

**Сценарии использования**: Microsoft Foundry Agent Service предназначен для корпоративных приложений, требующих безопасного, масштабируемого и гибкого развертывания AI-агентов.

## В чем разница между этими подходами?
 
Кажется, что они пересекаются, но есть ключевые различия в дизайне, возможностях и целевых сценариях использования:
 
- **Microsoft Agent Framework (MAF)**: Готовый к производству SDK для создания AI-агентов. Обеспечивает упрощённый API для создания агентов с вызовом инструментов, управлением беседой и интеграцией с Azure identity.
- **Microsoft Foundry Agent Service**: Платформа и служба развертывания в Microsoft Foundry для агентов. Предлагает встроенную связь с такими сервисами, как Azure OpenAI, Azure AI Search, Bing Search и выполнение кода.
 
Всё ещё не уверены, что выбрать?

### Сценарии использования
 
Попробуем помочь, рассмотрев несколько распространённых сценариев:
 
> В: Я создаю производственные AI-агент приложения и хочу начать быстро
>

>О: Microsoft Agent Framework — отличный выбор. Он предоставляет простой, питоничный API через `FoundryChatClient`, который позволяет определять агентов с инструментами и инструкциями всего в нескольких строках кода.

>В: Мне нужно корпоративное развертывание с интеграциями Azure, такими как Поиск и выполнение кода
>
> О: Лучший вариант — Microsoft Foundry Agent Service. Это платформа с встроенными возможностями для нескольких моделей, Azure AI Search, Bing Search и Azure Functions. Она позволяет легко создавать агентов в Foundry Portal и масштабировать их развертывание.
 
> В: Всё ещё запутался, просто дай один вариант
>
> О: Начните с Microsoft Agent Framework для создания агентов, а затем используйте Microsoft Foundry Agent Service, когда потребуется развертывание и масштабирование в производстве. Такой подход позволяет быстро итеративно разрабатывать логику агентов с чётким путём для корпоративного развертывания.
 
Подведём ключевые различия в таблице:

| Фреймворк | Фокус | Основные понятия | Сценарии использования |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Упрощённый SDK для агентов с вызовом инструментов | Агенты, Инструменты, Azure Identity | Создание AI-агентов, использование инструментов, многошаговые рабочие процессы |
| Microsoft Foundry Agent Service | Гибкие модели, корпоративная безопасность, генерация кода, вызов инструментов | Модульность, Совместная работа, Организация процессов | Безопасное, масштабируемое и гибкое развертывание AI-агентов |

## Могу ли я интегрировать мои существующие инструменты экосистемы Azure напрямую или мне нужны отдельные решения?


Ответ — да, вы можете интегрировать ваши существующие инструменты из экосистемы Azure напрямую с Microsoft Foundry Agent Service, особенно учитывая, что он был создан для бесшовной работы с другими сервисами Azure. Например, вы можете интегрировать Bing, Azure AI Search и Azure Functions. Также существует глубокая интеграция с Microsoft Foundry.

Фреймворк Microsoft Agent также интегрируется с сервисами Azure через `FoundryChatClient` и Azure identity, позволяя вызывать сервисы Azure напрямую из ваших агентских инструментов.

## Примеры кода

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Есть ещё вопросы про AI Agent Framework?

Присоединяйтесь к [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), чтобы встретиться с другими обучающимися, участвовать в часах консультаций и получить ответы на ваши вопросы о AI агентах.

## Ресурсы

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Сервис Azure Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Фреймворк Microsoft Agent - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Предыдущий урок

[Введение в AI Агентов и сценарии их использования](../01-intro-to-ai-agents/README.md)

## Следующий урок

[Понимание агентных дизайн-паттернов](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->