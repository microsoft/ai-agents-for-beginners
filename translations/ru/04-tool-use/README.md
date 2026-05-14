[![Как проектировать хорошие ИИ-агенты](../../../translated_images/ru/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Щелкните изображение выше, чтобы посмотреть видео этого урока)_

# Паттерн проектирования использования инструментов

Инструменты интересны тем, что позволяют ИИ-агентам обладать более широким спектром возможностей. Вместо того, чтобы агент имел ограниченный набор действий, которые он может выполнять, добавляя инструмент, агент теперь может выполнять широкий спектр действий. В этой главе мы рассмотрим паттерн проектирования использования инструментов, который описывает, как ИИ-агенты могут использовать конкретные инструменты для достижения своих целей.

## Введение

В этом уроке мы постараемся ответить на следующие вопросы:

- Что такое паттерн проектирования использования инструментов?
- В каких случаях его можно применять?
- Какие элементы/строительные блоки необходимы для реализации этого паттерна?
- Какие особые соображения необходимо учитывать при использовании паттерна проектирования использования инструментов для создания надежных ИИ-агентов?

## Цели обучения

После завершения этого урока вы сможете:

- Определить паттерн проектирования использования инструментов и его назначение.
- Опознать случаи использования, где паттерн проектирования использования инструментов применим.
- Понять ключевые элементы, необходимые для реализации данного паттерна.
- Осознать важные аспекты для обеспечения надежности ИИ-агентов, использующих этот паттерн проектирования.

## Что такое паттерн проектирования использования инструментов?

**Паттерн проектирования использования инструментов** сосредоточен на предоставлении LLM возможности взаимодействовать с внешними инструментами для достижения конкретных целей. Инструменты — это код, который может быть выполнен агентом для выполнения действий. Инструментом может быть простая функция, например калькулятор, или вызов API стороннего сервиса, например, поиск цены акций или прогноз погоды. В контексте ИИ-агентов инструменты предназначены для выполнения агентами в ответ на **вызовы функций, сгенерированные моделью**.

## В каких случаях его можно применять?

ИИ-агенты могут использовать инструменты для выполнения сложных задач, получения информации или принятия решений. Паттерн проектирования использования инструментов часто используется в сценариях, требующих динамического взаимодействия с внешними системами, такими как базы данных, веб-сервисы или интерпретаторы кода. Эта возможность полезна для ряда различных случаев использования, включая:

- **Динамическое получение информации:** агенты могут делать запросы к внешним API или базам данных для получения актуальных данных (например, запросы к базе данных SQLite для анализа данных, получение цен на акции или информации о погоде).
- **Выполнение и интерпретация кода:** агенты могут запускать код или скрипты для решения математических задач, создания отчетов или проведения симуляций.
- **Автоматизация рабочих процессов:** автоматизация повторяющихся или многошаговых рабочих процессов с помощью интеграции инструментов, таких как планировщики задач, службы электронной почты или каналы обработки данных.
- **Поддержка клиентов:** агенты могут взаимодействовать с CRM-системами, платформами тикетов или базами знаний для решения пользовательских запросов.
- **Создание и редактирование контента:** агенты могут использовать инструменты, такие как проверка грамматики, суммирование текста или оценки безопасности контента, для помощи в создании контента.

## Какие элементы/строительные блоки необходимы для реализации паттерна проектирования использования инструментов?

Эти строительные блоки позволяют ИИ-агенту выполнять широкий спектр задач. Рассмотрим ключевые элементы, необходимые для реализации паттерна:

- **Схемы функций/инструментов:** подробные определения доступных инструментов, включая название функции, назначение, необходимые параметры и ожидаемые выходные данные. Эти схемы позволяют LLM понимать, какие инструменты доступны и как формировать корректные запросы.

- **Логика выполнения функций:** определяет, как и когда вызываются инструменты на основе намерения пользователя и контекста диалога. Может включать модули планирования, механизмы маршрутизации или условные потоки, динамически определяющие использование инструментов.

- **Система управления сообщениями:** компоненты, управляющие ходом диалога между пользовательскими вводами, ответами LLM, вызовами инструментов и их результатами.

- **Фреймворк интеграции инструментов:** инфраструктура, которая связывает агента с разными инструментами, будь то простые функции или сложные внешние сервисы.

- **Обработка ошибок и валидация:** механизмы для обработки сбоев при выполнении инструментов, проверки параметров и управления неожиданными ответами.

- **Управление состоянием:** отслеживает контекст диалога, предыдущие взаимодействия с инструментами и персистентные данные для обеспечения согласованности в многоходовых взаимодействиях.

Далее рассмотрим подробнее вызов функций/инструментов.

### Вызов функций/инструментов

Вызов функций — это основной способ, с помощью которого мы даем Large Language Models (LLM) возможность взаимодействовать с инструментами. Часто термины «Функция» и «Инструмент» используются взаимозаменяемо, поскольку «функции» (блоки повторно используемого кода) и являются «инструментами», которые агенты используют для выполнения задач. Чтобы код функции был вызван, LLM должен сопоставить запрос пользователя с описанием функции. Для этого в LLM передается схема, содержащая описания всех доступных функций. Затем LLM выбирает наиболее подходящую функцию для задачи и возвращает ее имя и аргументы. Выбранная функция вызывается, ее ответ передается обратно в LLM, которое использует информацию для ответа на запрос пользователя.

Для разработчиков, желающих реализовать вызов функций для агентов, потребуются:

1. Модель LLM, поддерживающая вызов функций
2. Схема, содержащая описания функций
3. Код для каждой описанной функции

Приведем пример получения текущего времени в городе:

1. **Инициализировать LLM с поддержкой вызова функций:**

    Не все модели поддерживают вызов функций, поэтому важно проверить, поддерживает ли ваша модель. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> поддерживает вызов функций. Мы можем начать с инициализации клиента Azure OpenAI.

    ```python
    # Инициализация клиента Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Создать схему функции:**

    Далее определим JSON-схему, содержащую название функции, описание того, что она делает, а также названия и описания параметров функции.
    После этого передадим эту схему клиенту, созданному ранее, вместе с запросом пользователя о времени в Сан-Франциско. Важно отметить, что возвращается именно **вызов инструмента**, **а не** окончательный ответ на вопрос. Как отмечалось выше, LLM возвращает имя выбранной для задачи функции и аргументы, которые ей будут переданы.

    ```python
    # Описание функции для чтения модели
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Исходное сообщение пользователя
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Первый вызов API: Попросить модель использовать функцию
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Обработать ответ модели
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Код функции, необходимый для выполнения задачи:**

    Теперь, когда LLM выбрал функцию, которую необходимо выполнить, нужно реализовать и выполнить код, выполняющий задачу.
    Мы можем написать код для получения текущего времени на Python. Также потребуется код для извлечения имени и аргументов из response_message для получения конечного результата.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Обработка вызовов функций
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Второй вызов API: Получить окончательный ответ от модели
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Вызов функций является центральным элементом большинства, если не всех, решений по использованию инструментов в дизайне агентов, однако реализация этого с нуля иногда может быть сложной.
Как мы узнали в [Уроке 2](../../../02-explore-agentic-frameworks), агентские фреймворки предоставляют нам готовые строительные блоки для реализации использования инструментов.
 
## Примеры использования инструментов с агентскими фреймворками

Вот несколько примеров, как можно реализовать паттерн проектирования использования инструментов с помощью разных агентских фреймворков:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> — это фреймворк с открытым исходным кодом для построения ИИ-агентов. Он упрощает процесс использования вызова функций, позволяя определять инструменты как Python-функции с декоратором `@tool`. Фреймворк обрабатывает двустороннюю коммуникацию между моделью и вашим кодом. Также он предоставляет доступ к встроенным инструментам, таким как поиск файлов и интерпретатор кода через `AzureAIProjectAgentProvider`.

На следующей диаграмме показан процесс вызова функций в Microsoft Agent Framework:

![function calling](../../../translated_images/ru/functioncalling-diagram.a84006fc287f6014.webp)

В Microsoft Agent Framework инструменты определяются как функции с декоратором. Мы можем преобразовать функцию `get_current_time`, которую видели ранее, в инструмент, используя декоратор `@tool`. Фреймворк автоматически сериализует функцию и ее параметры, создавая схему для передачи в LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Создать клиента
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Создать агента и запустить с помощью инструмента
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> — более современный агентский фреймворк, предназначенный для того, чтобы помочь разработчикам безопасно создавать, развертывать и масштабировать высококачественные и расширяемые ИИ-агенты без необходимости управлять вычислительными и хранилищными ресурсами. Особенно полезен для корпоративных приложений, поскольку является полностью управляемым сервисом с корпоративным уровнем безопасности.

По сравнению с разработкой напрямую через API LLM, Azure AI Agent Service предлагает следующие преимущества:

- Автоматический вызов инструментов — нет необходимости самостоятельно парсить вызов инструмента, запускать его и обрабатывать ответ; все это теперь происходит на стороне сервера
- Безопасное управление данными — вместо управления собственным состоянием диалога можно полагаться на threads для хранения всей необходимой информации
- Инструменты «из коробки» — инструменты для взаимодействия с вашими источниками данных, такие как Bing, Azure AI Search и Azure Functions.

Доступные в Azure AI Agent Service инструменты можно разделить на две категории:

1. Инструменты знаний:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Основание на Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Поиск файлов</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Инструменты действий:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Вызов функций</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Интерпретатор кода</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Инструменты, определяемые OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service позволяет использовать эти инструменты вместе в виде `toolset`. Также он использует `threads`, которые отслеживают историю сообщений для конкретного диалога.

Представьте, что вы торговый агент в компании Contoso. Вы хотите разработать диалогового агента, который сможет отвечать на вопросы о ваших продажах.

На следующем изображении показано, как можно использовать Azure AI Agent Service для анализа продаж:

![Agentic Service In Action](../../../translated_images/ru/agent-service-in-action.34fb465c9a84659e.webp)

Для использования любого из этих инструментов с сервисом можно создать клиент и определить инструмент или набор инструментов. Для практической реализации можем использовать следующий код на Python. LLM сможет просмотреть набор инструментов и решить, использовать ли пользовательскую функцию `fetch_sales_data_using_sqlite_query` или встроенный интерпретатор кода в зависимости от запроса пользователя.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # функция fetch_sales_data_using_sqlite_query, которая находится в файле fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Инициализация набора инструментов
toolset = ToolSet()

# Инициализация агента вызова функций с функцией fetch_sales_data_using_sqlite_query и добавление её в набор инструментов
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Инициализация инструмента Code Interpreter и добавление его в набор инструментов.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Какие особые соображения необходимо учитывать при использовании паттерна проектирования использования инструментов для создания надежных ИИ-агентов?

Распространенной проблемой при динамически генерируемом LLM SQL является безопасность, особенно риск SQL-инъекций или злонамеренных действий, таких как удаление или изменение базы данных. Хотя эти опасения оправданы, их можно эффективно минимизировать, правильно настроив права доступа к базе данных. Для большинства баз данных это включает настройку базы в режиме только для чтения. Для сервисов баз данных, таких как PostgreSQL или Azure SQL, приложению следует назначить роль только для чтения (SELECT).

Запуск приложения в безопасной среде дополнительно повышает защиту. В корпоративных сценариях данные обычно извлекаются и трансформируются из операционных систем в базу данных или хранилище данных с доступом только для чтения и удобной схемой. Такой подход гарантирует безопасность данных, оптимизацию производительности и доступности, а также ограниченный доступ приложения только на чтение.

## Примеры кода

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Есть еще вопросы о паттернах проектирования использования инструментов?

Присоединяйтесь к [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), чтобы познакомиться с другими обучающимися, посетить офисные часы и получить ответы на вопросы по ИИ-агентам.

## Дополнительные ресурсы

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Мастерская Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Мастерская Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Обзор Microsoft Agent Framework</a>

## Предыдущий урок

[Понимание агентских паттернов проектирования](../03-agentic-design-patterns/README.md)

## Следующий урок
[Агентский RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->