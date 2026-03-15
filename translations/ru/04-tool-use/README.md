[![Как проектировать хороших ИИ-агентов](../../../translated_images/ru/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Паттерн использования инструментов

Инструменты интересны тем, что они позволяют агентам ИИ иметь более широкий набор возможностей. Вместо того, чтобы агент обладал ограниченным набором действий, добавление инструмента позволяет агенту выполнять широкий спектр действий. В этой главе мы рассмотрим Паттерн использования инструментов, который описывает, как агенты ИИ могут использовать конкретные инструменты для достижения своих целей.

## Введение

В этом уроке мы постараемся ответить на следующие вопросы:

- Что такое паттерн использования инструментов?
- Для каких задач его можно применять?
- Какие элементы/строительные блоки нужны для реализации этого паттерна?
- Какие особые моменты следует учитывать при использовании паттерна использования инструментов для создания надежных агентов ИИ?

## Цели обучения

После завершения этого урока вы сможете:

- Определить Паттерн использования инструментов и его назначение.
- Выявить сценарии, где применим Паттерн использования инструментов.
- Понять ключевые элементы, необходимые для реализации паттерна.
- Распознать соображения для обеспечения надежности агентов ИИ, использующих этот паттерн.

## Что такое Паттерн использования инструментов?

Паттерн использования инструментов сосредоточен на предоставлении LLMs возможности взаимодействовать с внешними инструментами для достижения конкретных целей. Инструменты — это код, который может быть выполнен агентом для выполнения действий. Инструментом может быть простая функция, например калькулятор, или вызов API стороннего сервиса, например получение цен на акции или прогноз погоды. В контексте агентов ИИ инструменты разработаны для выполнения агентами в ответ на **сгенерированные моделью вызовы функций**.

## Для каких задач его можно применять?

Агенты ИИ могут использовать инструменты для выполнения сложных задач, получения информации или принятия решений. Паттерн использования инструментов часто применяется в сценариях, требующих динамического взаимодействия с внешними системами, такими как базы данных, веб‑сервисы или интерпретаторы кода. Эта возможность полезна для множества различных случаев использования, в том числе:

- **Динамический поиск информации:** агенты могут обращаться к внешним API или базам данных для получения актуальных данных (например, запросы в SQLite для анализа данных, получение цен на акции или информации о погоде).
- **Выполнение и интерпретация кода:** агенты могут выполнять код или скрипты для решения математических задач, генерации отчетов или проведения симуляций.
- **Автоматизация рабочих процессов:** автоматизация повторяющихся или многошаговых рабочих процессов путем интеграции инструментов, таких как планировщики задач, почтовые сервисы или конвейеры данных.
- **Поддержка клиентов:** агенты могут взаимодействовать с CRM‑системами, платформами тикетов или базами знаний для решения запросов пользователей.
- **Генерация и редактирование контента:** агенты могут использовать инструменты, такие как проверка грамматики, суммаризация текста или оценщики безопасности контента, чтобы помогать в задачах создания контента.

## Какие элементы/строительные блоки нужны для реализации паттерна использования инструментов?

Эти строительные блоки позволяют агенту ИИ выполнять широкий набор задач. Рассмотрим ключевые элементы, необходимые для реализации Паттерна использования инструментов:

- **Схемы функций/инструментов:** подробные определения доступных инструментов, включая имя функции, назначение, требуемые параметры и ожидаемые выходные данные. Эти схемы позволяют LLMs понять, какие инструменты доступны и как формировать корректные запросы.

- **Логика выполнения функций:** управляет тем, как и когда вызываются инструменты на основе намерения пользователя и контекста разговора. Это может включать модули планирования, механизмы маршрутизации или условные потоки, которые динамически определяют использование инструментов.

- **Система обработки сообщений:** компоненты, которые управляют разговорным потоком между входами пользователя, ответами LLM, вызовами инструментов и результатами инструментов.

- **Фреймворк интеграции инструментов:** инфраструктура, которая подключает агента к различным инструментам, будь то простые функции или сложные внешние сервисы.

- **Обработка ошибок и валидация:** механизмы для обработки сбоев при выполнении инструментов, валидации параметров и управления неожиданными ответами.

- **Управление состоянием:** отслеживает контекст разговора, предыдущие взаимодействия с инструментами и постоянные данные, чтобы обеспечить согласованность в многошаговых взаимодействиях.

Далее рассмотрим Вызов функций/инструментов более подробно.
 
### Вызов функций/инструментов

Вызов функций является основным способом, с помощью которого мы даем Большим языковым моделям (LLMs) возможность взаимодействовать с инструментами. Вы часто увидите, что термины 'Function' и 'Tool' используются взаимозаменяемо, потому что 'функции' (блоки переиспользуемого кода) — это те 'инструменты', которые агенты используют для выполнения задач. Для того чтобы код функции был вызван, LLM должен сопоставить запрос пользователя с описанием функций. Для этого в LLM отправляется схема, содержащая описания всех доступных функций. Затем LLM выбирает наиболее подходящую функцию для задачи и возвращает ее имя и аргументы. Выбранная функция вызывается, ее ответ отправляется обратно в LLM, который использует эту информацию для ответа на запрос пользователя.

Для разработчиков, реализующих вызов функций для агентов, потребуется:

1. Модель LLM, которая поддерживает вызов функций
2. Схема, содержащая описания функций
3. Код для каждой описанной функции

Воспользуемся примером получения текущего времени в городе:

1. **Инициализировать LLM, который поддерживает вызов функций:**

    Не все модели поддерживают вызов функций, поэтому важно проверить, поддерживает ли модель, которую вы используете, эту возможность.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> поддерживает вызов функций. Мы можем начать с инициализации клиента Azure OpenAI. 

    ```python
    # Инициализировать клиент Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Создать схему функции:**

    Далее мы определим JSON‑схему, содержащую имя функции, описание того, что делает функция, и имена и описания параметров функции.
    Затем мы передадим эту схему клиенту, созданному ранее, вместе с запросом пользователя на получение времени в Сан‑Франциско. Что важно отметить — **инструментальный вызов** — это то, что возвращается, **а не** окончательный ответ на вопрос. Как упоминалось ранее, LLM возвращает имя выбранной для задачи функции и аргументы, которые будут ей переданы.

    ```python
    # Описание функции для чтения моделью
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

    Теперь, когда LLM выбрала, какая функция должна быть запущена, необходимо реализовать и выполнить код, который выполняет задачу.
    Мы можем реализовать код для получения текущего времени на Python. Нам также потребуется написать код для извлечения имени и аргументов из response_message, чтобы получить окончательный результат.

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

Вызов функций лежит в основе большинства, если не всех, реализаций паттерна использования инструментов агентов, однако реализация этого механизма с нуля иногда может быть сложной.
Как мы узнали в [Уроке 2](../../../02-explore-agentic-frameworks), агентные фреймворки предоставляют готовые строительные блоки для реализации использования инструментов.
 
## Примеры использования инструментов с агентными фреймворками

Ниже приведены примеры того, как вы можете реализовать Паттерн использования инструментов с помощью различных агентных фреймворков:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> — это открытый фреймворк для создания агентов ИИ. Он упрощает процесс использования вызовов функций, позволяя определять инструменты как функции Python с декоратором `@tool`. Фреймворк обрабатывает обмен сообщениями между моделью и вашим кодом. Он также предоставляет доступ к готовым инструментам, таким как Поиск по файлам и Интерпретатор кода через `AzureAIProjectAgentProvider`.

Следующая диаграмма иллюстрирует процесс вызова функций с Microsoft Agent Framework:

![вызов функций](../../../translated_images/ru/functioncalling-diagram.a84006fc287f6014.webp)

В Microsoft Agent Framework инструменты определяются как декорированные функции. Мы можем преобразовать функцию `get_current_time`, которую видели ранее, в инструмент, используя декоратор `@tool`. Фреймворк автоматически сериализует функцию и ее параметры, создавая схему для отправки в LLM.

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

# Создать агента и запустить его с помощью инструмента
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> — это более новый агентный фреймворк, предназначенный для того, чтобы помочь разработчикам надежно создавать, разворачивать и масштабировать высококачественных и расширяемых агентов ИИ без необходимости управлять базовыми ресурсами вычислений и хранения. Он особенно полезен для корпоративных приложений, так как является полностью управляемым сервисом с корпоративным уровнем безопасности.

По сравнению с разработкой напрямую через LLM API, Azure AI Agent Service предоставляет некоторые преимущества, в том числе:

- Автоматический вызов инструментов – нет нужды разбирать вызов инструмента, запускать инструмент и обрабатывать ответ; все это теперь выполняется на стороне сервера
- Безопасное управление данными – вместо того, чтобы управлять собственным состоянием разговоров, вы можете полагаться на threads для хранения всей необходимой информации
- Готовые инструменты – инструменты для взаимодействия с источниками данных, такими как Bing, Azure AI Search и Azure Functions

Доступные в Azure AI Agent Service инструменты можно разделить на две категории:

1. Инструменты знаний:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Инструменты действий:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Сервис агентов позволяет использовать эти инструменты вместе как `toolset`. Он также использует `threads`, которые отслеживают историю сообщений в рамках конкретного разговора.

Представьте, что вы торговый агент в компании под названием Contoso. Вы хотите разработать разговорного агента, который может отвечать на вопросы о ваших торговых данных.

Следующее изображение иллюстрирует, как вы могли бы использовать Azure AI Agent Service для анализа ваших торговых данных:

![Agentic Service In Action](../../../translated_images/ru/agent-service-in-action.34fb465c9a84659e.webp)

Чтобы использовать любой из этих инструментов со службой, мы можем создать клиента и определить инструмент или набор инструментов. Для практической реализации мы можем использовать следующий код на Python. LLM сможет просмотреть toolset и решить, использовать ли пользовательскую функцию `fetch_sales_data_using_sqlite_query` или встроенный Интерпретатор кода в зависимости от запроса пользователя.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # функция fetch_sales_data_using_sqlite_query, которую можно найти в файле fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Инициализировать набор инструментов
toolset = ToolSet()

# Инициализировать агент, вызывающий функцию fetch_sales_data_using_sqlite_query, и добавить его в набор инструментов
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Инициализировать инструмент Code Interpreter и добавить его в набор инструментов.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Какие особые моменты следует учитывать при использовании Паттерна использования инструментов для создания надежных агентов ИИ?

Распространенная проблема при динамически генерируемом LLM SQL — безопасность, в частности риск SQL‑инъекций или вредоносных действий, таких как удаление или искажение базы данных. Несмотря на то, что эти опасения обоснованы, их можно эффективно смягчить, правильно настроив разрешения доступа к базе данных. Для большинства баз данных это включает настройку базы данных в режиме только для чтения. Для сервисов баз данных, таких как PostgreSQL или Azure SQL, приложению следует назначать роль только для чтения (SELECT).

Запуск приложения в безопасной среде дополнительно усиливает защиту. В корпоративных сценариях данные обычно извлекаются и преобразуются из операционных систем в базу данных только для чтения или хранилище данных с удобной схемой. Такой подход обеспечивает безопасность данных, оптимизацию производительности и доступность, а также ограниченный доступ приложения только для чтения.

## Примеры кода

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Хотите узнать больше о Паттернах использования инструментов?

Присоединяйтесь к [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), чтобы встретиться с другими учащимися, посетить office hours и получить ответы на ваши вопросы об агентах ИИ.

## Дополнительные ресурсы

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## Предыдущий урок

[Понимание агентных паттернов проектирования](../03-agentic-design-patterns/README.md)

## Следующий урок
[Агентный RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с помощью сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на стремление к точности, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->