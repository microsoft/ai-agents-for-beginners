<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "88258b03f2893aa2e69eb8fb24baabbc",
  "translation_date": "2025-07-11T14:34:59+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "ru"
}
-->
[![Как проектировать хорошие AI-агенты](../../../04-tool-use/images/lesson-4-thumbnail.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Шаблон проектирования использования инструментов

Инструменты интересны тем, что они позволяют AI-агентам иметь более широкий спектр возможностей. Вместо того чтобы агент имел ограниченный набор действий, которые он может выполнять, добавив инструмент, агент теперь может выполнять широкий спектр действий. В этой главе мы рассмотрим шаблон проектирования использования инструментов, который описывает, как AI-агенты могут использовать конкретные инструменты для достижения своих целей.

## Введение

В этом уроке мы стремимся ответить на следующие вопросы:

- Что такое шаблон проектирования использования инструментов?
- В каких случаях его можно применять?
- Какие элементы/строительные блоки необходимы для реализации шаблона проектирования?
- Какие особые соображения следует учитывать при использовании шаблона проектирования использования инструментов для создания надежных AI-агентов?

## Цели обучения

После завершения этого урока вы сможете:

- Определить шаблон проектирования использования инструментов и его назначение.
- Определить случаи использования, в которых применим шаблон проектирования использования инструментов.
- Понять ключевые элементы, необходимые для реализации шаблона проектирования.
- Признать соображения для обеспечения надежности AI-агентов, использующих этот шаблон проектирования.

## Что такое шаблон проектирования использования инструментов?

**Шаблон проектирования использования инструментов** фокусируется на предоставлении LLM возможности взаимодействовать с внешними инструментами для достижения конкретных целей. Инструменты — это код, который может быть выполнен агентом для выполнения действий. Инструмент может быть простой функцией, такой как калькулятор, или вызовом API к стороннему сервису, такому как поиск цен на акции или прогноз погоды. В контексте AI-агентов инструменты предназначены для выполнения агентами в ответ на **вызовы функций, сгенерированные моделью**.

## В каких случаях его можно применять?

AI-агенты могут использовать инструменты для выполнения сложных задач, получения информации или принятия решений. Шаблон проектирования использования инструментов часто используется в сценариях, требующих динамического взаимодействия с внешними системами, такими как базы данных, веб-сервисы или интерпретаторы кода. Эта возможность полезна для множества различных случаев использования, включая:

- **Динамическое получение информации:** Агенты могут запрашивать внешние API или базы данных для получения актуальных данных (например, запрос в базе данных SQLite для анализа данных, получение цен на акции или информации о погоде).
- **Выполнение и интерпретация кода:** Агенты могут выполнять код или скрипты для решения математических задач, создания отчетов или проведения симуляций.
- **Автоматизация рабочих процессов:** Автоматизация повторяющихся или многоэтапных рабочих процессов путем интеграции инструментов, таких как планировщики задач, почтовые сервисы или конвейеры данных.
- **Поддержка клиентов:** Агенты могут взаимодействовать с системами CRM, платформами тикетов или базами знаний для решения запросов пользователей.
- **Создание и редактирование контента:** Агенты могут использовать инструменты, такие как проверка грамматики, суммаризация текста или оценка безопасности контента, для помощи в задачах создания контента.

## Какие элементы/строительные блоки необходимы для реализации шаблона проектирования использования инструментов?

Эти строительные блоки позволяют AI-агенту выполнять широкий спектр задач. Давайте рассмотрим ключевые элементы, необходимые для реализации шаблона проектирования использования инструментов:

- **Схемы функций/инструментов**: Подробные определения доступных инструментов, включая имя функции, назначение, требуемые параметры и ожидаемые выходные данные. Эти схемы позволяют LLM понять, какие инструменты доступны и как строить допустимые запросы.

- **Логика выполнения функций**: Управляет тем, как и когда инструменты вызываются на основе намерений пользователя и контекста разговора. Это может включать модули планирования, механизмы маршрутизации или условные потоки, которые динамически определяют использование инструментов.

- **Система обработки сообщений**: Компоненты, которые управляют потоком разговора между вводом пользователя, ответами LLM, вызовами инструментов и выходными данными инструментов.

- **Фреймворк интеграции инструментов**: Инфраструктура, которая соединяет агента с различными инструментами, будь то простые функции или сложные внешние сервисы.

- **Обработка ошибок и валидация**: Механизмы для обработки сбоев в выполнении инструментов, проверки параметров и управления неожиданными ответами.

- **Управление состоянием**: Отслеживает контекст разговора, предыдущие взаимодействия с инструментами и постоянные данные для обеспечения согласованности в многоходовых взаимодействиях.

Далее давайте подробнее рассмотрим вызов функций/инструментов.

### Вызов функций/инструментов

Вызов функций — это основной способ, которым мы позволяем большим языковым моделям (LLM) взаимодействовать с инструментами. Вы часто увидите, что 'функция' и 'инструмент' используются взаимозаменяемо, потому что 'функции' (блоки повторно используемого кода) — это 'инструменты', которые агенты используют для выполнения задач. Чтобы код функции был вызван, LLM должен сравнить запрос пользователя с описанием функции. Для этого схема, содержащая описания всех доступных функций, отправляется в LLM. Затем LLM выбирает наиболее подходящую функцию для задачи и возвращает ее имя и аргументы. Выбранная функция вызывается, ее ответ отправляется обратно в LLM, который использует информацию для ответа на запрос пользователя.

Для того чтобы разработчики могли реализовать вызов функций для агентов, вам потребуется:

1. Модель LLM, поддерживающая вызов функций
2. Схема, содержащая описания функций
3. Код для каждой описанной функции

Давайте используем пример получения текущего времени в городе для иллюстрации:

1. **Инициализация LLM, поддерживающей вызов функций:**

    Не все модели поддерживают вызов функций, поэтому важно убедиться, что используемая вами LLM это делает. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> поддерживает вызов функций. Мы можем начать с инициализации клиента Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Создание схемы функции**:

    Далее мы определим схему JSON, содержащую имя функции, описание того, что делает функция, и имена и описания параметров функции. Затем мы возьмем эту схему и передадим ее клиенту, созданному ранее, вместе с запросом пользователя на нахождение времени в Сан-Франциско. Важно отметить, что возвращается **вызов инструмента**, а не окончательный ответ на вопрос. Как упоминалось ранее, LLM возвращает имя функции, которую она выбрала для задачи, и аргументы, которые будут переданы ей.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
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

    Теперь, когда LLM выбрала, какую функцию нужно запустить, код, выполняющий задачу, должен быть реализован и выполнен. Мы можем реализовать код для получения текущего времени на Python. Нам также нужно будет написать код для извлечения имени и аргументов из response_message, чтобы получить окончательный результат.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

Вызов функций является основой большинства, если не всех, дизайнов использования инструментов агентами, однако его реализация с нуля может быть сложной задачей. Как мы узнали в [Уроке 2](../../../02-explore-agentic-frameworks), агентные фреймворки предоставляют нам предварительно созданные строительные блоки для реализации использования инструментов.

## Примеры использования инструментов с агентными фреймворками

Вот несколько примеров того, как вы можете реализовать шаблон проектирования использования инструментов, используя различные агентные фреймворки:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> — это открытый AI-фреймворк для разработчиков на .NET, Python и Java, работающих с большими языковыми моделями (LLM). Он упрощает процесс использования вызова функций, автоматически описывая ваши функции и их параметры модели через процесс, называемый <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">сериализацией</a>. Он также обрабатывает обмен сообщениями между моделью и вашим кодом. Еще одно преимущество использования агентного фреймворка, такого как Semantic Kernel, заключается в том, что он позволяет вам получить доступ к предварительно созданным инструментам, таким как <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Поиск файлов</a> и <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Интерпретатор кода</a>.

Следующая диаграмма иллюстрирует процесс вызова функций с помощью Semantic Kernel:

![вызов функций](../../../04-tool-use/images/functioncalling-diagram.png)

В Semantic Kernel функции/инструменты называются <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Плагинами</a>. Мы можем преобразовать функцию `get_current_time`, которую мы видели ранее, в плагин, превратив ее в класс с функцией внутри. Мы также можем импортировать декоратор `kernel_function`, который принимает описание функции. Когда вы создаете ядро с GetCurrentTimePlugin, ядро автоматически сериализует функцию и ее параметры, создавая схему для отправки в LLM в процессе.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Служба агентов Azure AI

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Служба агентов Azure AI</a> — это новый агентный фреймворк, который предназначен для того, чтобы дать разработчикам возможность безопасно создавать, развертывать и масштабировать высококачественных и расширяемых AI-агентов без необходимости управлять основными вычислительными и хранилищными ресурсами. Он особенно полезен для корпоративных приложений, так как является полностью управляемым сервисом с корпоративной безопасностью.

По сравнению с разработкой с использованием API LLM напрямую, служба агентов Azure AI предоставляет некоторые преимущества, включая:

- Автоматический вызов инструментов — нет необходимости разбирать вызов инструмента, вызывать инструмент и обрабатывать ответ; все это теперь выполняется на стороне сервера
- Безопасно управляемые данные — вместо управления собственным состоянием разговора вы можете полагаться на потоки для хранения всей необходимой информации
- Готовые инструменты — инструменты, которые вы можете использовать для взаимодействия с вашими источниками данных, такие как Bing, Azure AI Search и Azure Functions.

Инструменты, доступные в службе агентов Azure AI, можно разделить на две категории:

1. Инструменты знаний:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Основание с помощью Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Поиск файлов</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Инструменты действий:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Вызов функций</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Интерпретатор кода</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Инструменты, определенные OpenAI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Служба агентов позволяет нам использовать эти инструменты вместе как `набор инструментов`. Она также использует `потоки`, которые отслеживают историю сообщений из конкретного разговора.

Представьте, что вы агент по продажам в компании под названием Contoso. Вы хотите разработать разговорного агента, который может отвечать на вопросы о ваших данных о продажах.

Следующее изображение иллюстрирует, как вы могли бы использовать службу агентов Azure AI для анализа ваших данных о продажах:

![Служба агентов в действии](../../../04-tool-use/images/agent-service-in-action.jpg)

Чтобы использовать любой из этих инструментов с сервисом, мы можем создать клиента и определить инструмент или набор инструментов. Чтобы реализовать это на практике, мы можем использовать следующий код на Python. LLM сможет просмотреть набор инструментов и решить, использовать ли пользовательскую функцию `fetch_sales_data_using_sqlite_query` или предварительно созданный интерпретатор кода в зависимости от запроса пользователя.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fecth_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Какие особые соображения следует учитывать при использовании шаблона проектирования использования инструментов для создания надежных AI-агентов?

Общей проблемой с SQL, динамически генерируемым LLM, является безопасность, особенно риск SQL-инъекций или злонамеренных действий, таких как удаление или изменение базы данных. Хотя эти опасения обоснованы, их можно эффективно смягчить, правильно настроив разрешения на доступ к базе данных. Для большинства баз данных это включает настройку базы данных как только для чтения. Для таких сервисов баз данных, как PostgreSQL или Azure SQL, приложению следует назначить роль только для чтения (SELECT).

Запуск приложения в безопасной среде дополнительно повышает защиту. В корпоративных сценариях данные обычно извлекаются и преобразуются из операционных систем в базу данных только для чтения или хранилище данных с удобной для пользователя схемой. Этот подход обеспечивает безопасность данных, оптимизацию производительности и доступности, а также ограниченный доступ приложения только для чтения.

## Дополнительные ресурсы

-
<a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">
Azure AI Agents Service Workshop
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Мастерская Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Учебник по вызову функций в Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Интерпретатор кода в Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Инструменты Autogen</a>

## Предыдущий урок

[Понимание агентных шаблонов проектирования](../03-agentic-design-patterns/README.md)

## Следующий урок

[Agentic RAG](../05-agentic-rag/README.md)

**Отказ от ответственности**:  
Этот документ был переведен с помощью службы автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникающие в результате использования этого перевода.