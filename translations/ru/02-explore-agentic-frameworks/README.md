[![Изучение фреймворков AI-агентов](../../../translated_images/ru/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Изучение фреймворков AI-агентов

Фреймворки AI-агентов — это программные платформы, предназначенные для упрощения создания, развертывания и управления AI-агентами. Эти фреймворки предоставляют разработчикам готовые компоненты, абстракции и инструменты, которые упрощают разработку сложных AI-систем.

Эти фреймворки помогают разработчикам сосредоточиться на уникальных аспектах своих приложений, предоставляя стандартизированные подходы к распространённым задачам разработки AI-агентов. Они повышают масштабируемость, доступность и эффективность при создании AI-систем.

## Введение 

В этом уроке будут рассмотрены следующие темы:

- Что такое AI-фреймворки агентов и что они позволяют разработчикам достигать?
- Как команды могут использовать их для быстрой прототипизации, итераций и улучшения возможностей своего агента?
- В чем различия между фреймворками и инструментами, созданными Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> и <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Могу ли я интегрировать существующие инструменты экосистемы Azure напрямую или нужны автономные решения?
- Что такое Microsoft Foundry Agent Service и как он мне помогает?

## Цели обучения

Цели этого урока — помочь вам понять:

- Роль AI-фреймворков агентов в разработке AI.
- Как использовать AI-фреймворки агентов для создания интеллектуальных агентов.
- Основные возможности, которые предоставляют AI-фреймворки агентов.
- Различия между Microsoft Agent Framework и Microsoft Foundry Agent Service.

## Что такое AI-фреймворки агентов и что они позволяют разработчикам делать?

Традиционные AI-фреймворки помогают интегрировать AI в ваши приложения и улучшить эти приложения следующими способами:

- **Персонализация**: AI может анализировать поведение и предпочтения пользователей, чтобы предоставлять персонализированные рекомендации, контент и опыт.
Пример: Сервисы потокового видео, такие как Netflix, используют AI для предложения фильмов и шоу на основе истории просмотров, повышая вовлеченность и удовлетворенность пользователей.
- **Автоматизация и эффективность**: AI может автоматизировать повторяющиеся задачи, оптимизировать рабочие процессы и улучшать операционную эффективность.
Пример: Приложения клиентской поддержки используют чат-боты на базе AI для обработки общих запросов, сокращая время ответа и освобождая человеческих агентов для решения более сложных вопросов.
- **Улучшенный пользовательский опыт**: AI может повысить общий пользовательский опыт, предоставляя интеллектуальные функции, такие как распознавание голоса, обработка естественного языка и предиктивный ввод текста.
Пример: Виртуальные ассистенты, такие как Siri и Google Assistant, используют AI для понимания и реагирования на голосовые команды, облегчая взаимодействие пользователей с устройствами.

### Звучит отлично, но зачем нам нужен AI Agent Framework?

Фреймворки AI-агентов представляют собой нечто большее, чем просто AI-фреймворки. Они предназначены для создания интеллектуальных агентов, которые могут взаимодействовать с пользователями, другими агентами и окружением для достижения конкретных целей. Эти агенты могут проявлять автономное поведение, принимать решения и адаптироваться к меняющимся условиям. Рассмотрим ключевые возможности, обеспечиваемые AI Agent Frameworks:

- **Сотрудничество и координация агентов**: Возможность создавать несколько AI-агентов, которые могут работать вместе, общаться и координироваться для решения сложных задач.
- **Автоматизация и управление задачами**: Обеспечение механизмов для автоматизации многоэтапных рабочих процессов, делегирования задач и динамического управления задачами среди агентов.
- **Контекстное понимание и адаптация**: Оснащение агентов способностью понимать контекст, адаптироваться к меняющейся среде и принимать решения на основе информации в реальном времени.

В итоге, агенты позволяют вам делать больше, поднимая автоматизацию на новый уровень, создавая более интеллектуальные системы, которые могут адаптироваться и учиться на своём окружении.

## Как быстро прототипировать, итеративно улучшать и развивать возможности агента?

Эта сфера развивается очень быстро, но есть некоторые общие аспекты у большинства AI Agent Frameworks, которые помогают быстро прототипировать и делать итерации, а именно модульные компоненты, инструменты совместной работы и обучение в реальном времени. Рассмотрим их подробнее:

- **Используйте модульные компоненты**: AI SDK предлагают готовые компоненты, такие как AI и модули памяти, вызов функций с помощью естественного языка или плагинов кода, шаблоны подсказок и многое другое.
- **Используйте инструменты для совместной работы**: Создавайте агентов с конкретными ролями и задачами, позволяя им тестировать и улучшать совместные рабочие процессы.
- **Обучение в реальном времени**: Внедряйте обратную связь, где агенты учатся на взаимодействиях и динамически корректируют своё поведение.

### Используйте модульные компоненты

Такие SDK, как Microsoft Agent Framework, предлагают готовые компоненты, такие как AI-коннекторы, определения инструментов и управление агентами.

**Как команды могут использовать это**: Команды могут быстро собирать эти компоненты для создания рабочего прототипа без необходимости начинать с нуля, что позволяет экспериментировать и проводить итерации быстрее.

**Как это работает на практике**: Вы можете использовать готовый парсер для извлечения информации из пользовательского ввода, модуль памяти для хранения и извлечения данных, и генератор подсказок для взаимодействия с пользователями — всё это без необходимости создавать компоненты с нуля.

**Пример кода**. Рассмотрим пример использования Microsoft Agent Framework с `FoundryChatClient`, когда модель отвечает на ввод пользователя с вызовом инструментов:

``` python
# Пример использования Microsoft Agent Framework на Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Определите пример функции инструмента для бронирования путешествия
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
    # Пример вывода: Ваш рейс в Нью-Йорк на 1 января 2025 года успешно забронирован. Счастливого путешествия! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

В этом примере видно, как можно использовать готовый парсер для извлечения ключевой информации из пользовательского запроса, такой как отправление, пункт назначения и дата бронирования рейса. Такой модульный подход позволяет сосредоточиться на логике высокого уровня.

### Используйте инструменты для совместной работы

Фреймворки, например Microsoft Agent Framework, облегчают создание множества агентов, которые могут работать вместе.

**Как команды могут использовать это**: Команды могут проектировать агентов с конкретными ролями и задачами, что позволяет испытывать и улучшать совместные рабочие процессы и повышать производительность всей системы.

**Как это работает на практике**: Вы можете создать команду агентов, где каждый агент специализируется на определённой функции, например сбор данных, анализ или принятие решений. Эти агенты могут общаться и делиться информацией для достижения общей цели, например для ответа на запрос пользователя или выполнения задачи.

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

# Запуск агентов последовательно для выполнения задачи
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

В приведённом выше коде показано, как создать задачу, в которой несколько агентов работают вместе для анализа данных. Каждый агент выполняет определённую функцию, а задача реализуется через координацию работы агентов для достижения желаемого результата. Создавая специализированных агентов с конкретными ролями, можно повысить эффективность и производительность задач.

### Обучение в реальном времени

Продвинутые фреймворки обеспечивают возможности для понимания контекста и адаптации в реальном времени.

**Как команды могут использовать это**: Команды могут внедрять петли обратной связи, где агенты учатся на взаимодействиях и динамически корректируют своё поведение, что ведёт к постоянному улучшению и развитию возможностей.

**Как это работает на практике**: Агенты могут анализировать отзывы пользователей, данные окружающей среды и результаты задач для обновления базы знаний, корректировки алгоритмов принятия решений и повышения производительности со временем. Этот итеративный процесс обучения позволяет агентам адаптироваться к меняющимся условиям и предпочтениям пользователей, улучшая общую эффективность системы.

## В чем различия между Microsoft Agent Framework и Microsoft Foundry Agent Service?

Существует много способов сравнить эти подходы, но рассмотрим ключевые различия с точки зрения их дизайна, возможностей и целевых сценариев использования:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework предоставляет упрощённый SDK для построения AI-агентов с использованием `FoundryChatClient`. Он позволяет разработчикам создавать агентов, использующих модели Azure OpenAI с встроенным вызовом инструментов, управлением диалогами и корпоративной безопасностью через Azure identity.

**Сценарии использования**: Создание готовых к производству AI-агентов с поддержкой вызова инструментов, многоэтапных рабочих процессов и сценариев интеграции с корпоративными системами.

Вот несколько важных ключевых концепций Microsoft Agent Framework:

- **Агенты**. Агент создаётся через `FoundryChatClient` и настраивается с именем, инструкциями и инструментами. Агент может:
  - **Обрабатывать сообщения пользователей** и создавать ответы с использованием моделей Azure OpenAI.
  - **Автоматически вызывать инструменты** на основе контекста разговора.
  - **Поддерживать состояние диалога** на протяжении нескольких взаимодействий.

  Вот пример кода создания агента:

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

- **Инструменты**. Фреймворк поддерживает определение инструментов как Python-функций, которые агент может вызывать автоматически. Инструменты регистрируются при создании агента:

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

- **Координация нескольких агентов**. Можно создавать нескольких агентов с различными специализациями и координировать их работу:

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

- **Интеграция с Azure Identity**. Фреймворк использует `AzureCliCredential` (или `DefaultAzureCredential`) для безопасной аутентификации без ключей, устраняя необходимость напрямую управлять API-ключами.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service — это более новое решение, представленное на Microsoft Ignite 2024. Оно позволяет разрабатывать и развертывать AI-агентов с более гибкими моделями, такими как прямой вызов открытых LLM, например Llama 3, Mistral и Cohere.

Microsoft Foundry Agent Service предлагает более расширенные механизмы корпоративной безопасности и методы хранения данных, что делает его подходящим для корпоративных приложений.

Он напрямую интегрируется с Microsoft Agent Framework для создания и развертывания агентов.

На данный момент сервис находится в публичной превью и поддерживает Python и C# для разработки агентов.

С помощью Python SDK Microsoft Foundry Agent Service можно создать агента с пользовательским инструментом:

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

### Ключевые концепции

Microsoft Foundry Agent Service имеет следующие ключевые концепции:

- **Агент**. Microsoft Foundry Agent Service интегрируется с Microsoft Foundry. Внутри Microsoft Foundry AI-агент — это "умный" микросервис, который может отвечать на вопросы (RAG), выполнять действия или полностью автоматизировать рабочие процессы. Это достигается благодаря сочетанию мощи генеративных AI-моделей с инструментами, позволяющими получать доступ и взаимодействовать с реальными источниками данных. Пример агента:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    В этом примере создаётся агент с моделью `gpt-4.1-mini`, именем `my-agent` и инструкцией `You are helpful agent`. Агент оснащён инструментами и ресурсами для выполнения задач по интерпретации кода.

- **Потоки и сообщения**. Поток — ещё одна важная концепция. Он представляет собой разговор или взаимодействие между агентом и пользователем. Потоки могут использоваться для отслеживания ходa разговора, хранения информации о контексте и управления состоянием взаимодействия. Пример потока:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Попросите агента выполнить работу в потоке
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Получите и зарегистрируйте все сообщения, чтобы видеть ответ агента
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    В приведённом коде создаётся поток. Затем в поток отправляется сообщение. Вызовом `create_and_process_run` агенту поручается выполнить работу в потоке. В конце сообщения извлекаются и выводятся для просмотра ответа агента. Сообщения показывают ход беседы между пользователем и агентом. Важно понимать, что сообщения могут быть различных типов: текст, изображение или файл, что означает, что агент может, например, создать изображение или текстовый ответ. Как разработчик, вы можете использовать эту информацию для дальнейшей обработки ответа или его отображения пользователю.

- **Интеграция с Microsoft Agent Framework**. Microsoft Foundry Agent Service работает без проблем с Microsoft Agent Framework, что позволяет создавать агентов с помощью `FoundryChatClient` и развертывать их через Agent Service для производственных сценариев.

**Сценарии использования**: Microsoft Foundry Agent Service предназначен для корпоративных приложений, требующих безопасного, масштабируемого и гибкого развертывания AI-агентов.

## В чем разница между этими подходами?
 
Кажется, что они пересекаются, но есть ключевые различия в дизайне, возможностях и целевых сценариях использования:
 
- **Microsoft Agent Framework (MAF)**: Готовый к производству SDK для создания AI-агентов. Предоставляет упрощённый API для создания агентов с вызовом инструментов, управлением диалогами и интеграцией с Azure identity.
- **Microsoft Foundry Agent Service**: Платформа и сервис развертывания в Microsoft Foundry для агентов. Обеспечивает встроенную связность с сервисами, такими как Azure OpenAI, Azure AI Search, Bing Search и выполнение кода.
 
Всё ещё не уверены, что выбрать?

### Сценарии использования
 
Посмотрим, сможем ли помочь, рассмотрев распространённые сценарии:
 
> В: Я разрабатываю производственные приложения AI-агентов и хочу быстро начать
>

>О: Microsoft Agent Framework — отличный выбор. Он предоставляет простой, похожий на Python API через `FoundryChatClient`, позволяющий определить агентов с инструментами и инструкциями всего в несколько строк кода.

>В: Мне нужно корпоративное развертывание с интеграциями Azure, такими как поиск и выполнение кода
>
> О: Microsoft Foundry Agent Service подходит лучше всего. Это платформенный сервис с встроенными возможностями для работы с множеством моделей, Azure AI Search, Bing Search и Azure Functions. Легко создавать агентов в портале Foundry и масштабировать их развертывание.
 
> В: Я всё ещё в замешательстве, дайте один вариант
>
> О: Начните с Microsoft Agent Framework для создания агентов, а затем используйте Microsoft Foundry Agent Service для развертывания и масштабирования в производстве. Такой подход позволит быстро итеративно развивать логику агента и иметь чёткий путь к корпоративному развертыванию.
 
Подведём итоги ключевых различий в таблице:

| Фреймворк | Фокус | Ключевые концепции | Сценарии использования |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Упрощённый SDK для агентов с вызовом инструментов | Агенты, Инструменты, Azure Identity | Создание AI-агентов, использование инструментов, многоэтапные рабочие процессы |
| Microsoft Foundry Agent Service | Гибкие модели, корпоративная безопасность, генерация кода, вызов инструментов | Модульность, Сотрудничество, Оркестрация процессов | Безопасное, масштабируемое и гибкое развертывание AI-агентов |

## Могу ли я интегрировать мои существующие инструменты экосистемы Azure напрямую или нужны автономные решения?


Ответ — да, вы можете интегрировать существующие инструменты экосистемы Azure напрямую с Microsoft Foundry Agent Service, особенно поскольку он был создан для бесшовной работы с другими сервисами Azure. Например, вы можете интегрировать Bing, Azure AI Search и Azure Functions. Также есть глубокая интеграция с Microsoft Foundry.

Microsoft Agent Framework также интегрируется с сервисами Azure через `FoundryChatClient` и Azure identity, что позволяет вам вызывать сервисы Azure напрямую из инструментов вашего агента.

## Примеры кода

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Есть ещё вопросы о AI Agent Frameworks?

Присоединяйтесь к [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), чтобы встретиться с другими учениками, посетить часы работы и получить ответы на ваши вопросы по AI агентам.

## Ссылки

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Предыдущее занятие

[Введение в AI Агентов и сценарии использования агентов](../01-intro-to-ai-agents/README.md)

## Следующее занятие

[Понимание паттернов агентного проектирования](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->