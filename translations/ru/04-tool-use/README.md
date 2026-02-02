[![Как проектировать хорошие AI-агенты](../../../translated_images/ru/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Паттерн проектирования использования инструментов

Инструменты интересны тем, что позволяют AI-агентам иметь более широкий спектр возможностей. Вместо того, чтобы агент имел ограниченный набор действий, которые он может выполнять, добавление инструмента позволяет агенту выполнять широкий спектр действий. В этой главе мы рассмотрим паттерн проектирования использования инструментов, который описывает, как AI-агенты могут использовать конкретные инструменты для достижения своих целей.

## Введение

В этом уроке мы постараемся ответить на следующие вопросы:

- Что такое паттерн проектирования использования инструментов?
- В каких случаях его можно применять?
- Какие элементы/строительные блоки необходимы для реализации этого паттерна?
- Какие особенности нужно учитывать при использовании паттерна проектирования использования инструментов для создания надежных AI-агентов?

## Цели обучения

После изучения этого урока вы сможете:

- Определить паттерн проектирования использования инструментов и его назначение.
- Опознать случаи использования, когда применение этого паттерна уместно.
- Понять ключевые элементы, необходимые для реализации паттерна.
- Определять особенности, необходимые для обеспечения надежности AI-агентов при использовании этого паттерна.

## Что такое паттерн проектирования использования инструментов?

**Паттерн проектирования использования инструментов** фокусируется на предоставлении LLM возможности взаимодействовать с внешними инструментами для достижения конкретных целей. Инструменты — это код, который может быть выполнен агентом для выполнения действий. Инструментом может быть простая функция, например калькулятор, или вызов API стороннего сервиса, например для получения цены акций или прогноза погоды. В контексте AI-агентов инструменты предназначены для выполнения агентами в ответ на **вызовы функций, сгенерированные моделью**.

## В каких случаях его можно применять?

AI-агенты могут использовать инструменты для выполнения сложных задач, получения информации или принятия решений. Паттерн проектирования использования инструментов часто применяется в сценариях, требующих динамического взаимодействия с внешними системами, такими как базы данных, веб-сервисы или интерпретаторы кода. Эта возможность полезна для различных случаев использования, включая:

- **Динамический поиск информации:** агенты могут запрашивать внешние API или базы данных для получения актуальных данных (например, запрос в SQLite для анализа данных, получение цен на акции или информации о погоде).
- **Выполнение и интерпретация кода:** агенты могут выполнять код или скрипты для решения математических задач, создания отчетов или проведения симуляций.
- **Автоматизация рабочих процессов:** автоматизация повторяющихся или многошаговых процессов с помощью интеграции таких инструментов, как планировщики задач, почтовые сервисы или конвейеры обработки данных.
- **Поддержка клиентов:** агенты могут взаимодействовать с CRM-системами, системами тикетов или базами знаний для решения запросов пользователей.
- **Генерация и редактирование контента:** агенты могут использовать инструменты проверки грамматики, суммирования текста или оценки безопасности контента для помощи в создании материалов.

## Какие элементы/строительные блоки необходимы для реализации паттерна проектирования использования инструментов?

Эти строительные блоки позволяют AI-агенту выполнять широкий спектр задач. Рассмотрим ключевые элементы, необходимые для реализации паттерна проектирования использования инструментов:

- **Схемы функций/инструментов**: детальные описания доступных инструментов, включая название функции, назначение, необходимые параметры и ожидаемые результаты. Эти схемы позволяют LLM понимать, какие инструменты доступны и как формировать корректные запросы.

- **Логика вызова функций**: управляет тем, как и когда инструменты вызываются, исходя из намерений пользователя и контекста беседы. Может включать модули планирования, механизмы маршрутизации или условные потоки, определяющие динамическое использование инструментов.

- **Система обработки сообщений**: компоненты, управляющие диалоговым потоком между пользовательскими вводами, ответами LLM, вызовами инструментов и их результатами.

- **Фреймворк интеграции инструментов**: инфраструктура, соединяющая агента с различными инструментами, будь то простые функции или сложные внешние сервисы.

- **Обработка ошибок и валидация**: механизмы для обработки сбоев при выполнении инструментов, проверки параметров и управления неожиданными ответами.

- **Управление состоянием**: отслеживание контекста беседы, предыдущих взаимодействий с инструментами и постоянных данных для обеспечения согласованности в многошаговых взаимодействиях.

Далее рассмотрим более подробно вызов функций/инструментов.

### Вызов функций/инструментов

Вызов функций — это основной способ, которым мы позволяем Большим Языковым Моделям (LLM) взаимодействовать с инструментами. Вы часто будете видеть, что термины «Функция» и «Инструмент» используются как синонимы, потому что «функции» (блоки многократно используемого кода) являются «инструментами», которые агенты используют для выполнения задач. Чтобы код функции был вызван, LLM должен сопоставить запрос пользователя с описанием функций. Для этого схема, содержащая описания всех доступных функций, отправляется LLM. Затем LLM выбирает наиболее подходящую функцию для задачи и возвращает её имя и аргументы. Выбранная функция вызывается, её ответ отправляется обратно LLM, которая использует эту информацию для ответа на запрос пользователя.

Для разработчиков, чтобы реализовать вызов функций для агентов, потребуется:

1. LLM-модель, поддерживающая вызов функций
2. Схема, содержащая описания функций
3. Код для каждой описанной функции

Приведём пример получения текущего времени в городе:

1. **Инициализировать LLM, поддерживающую вызов функций:**

    Не все модели поддерживают вызов функций, поэтому важно проверить, что используемая вами LLM это умеет. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> поддерживает вызов функций. Начать можно с инициализации клиента Azure OpenAI.

    ```python
    # Инициализация клиента Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Создать схему функции**:

    Далее определим JSON-схему, которая содержит имя функции, описание того, что функция делает, а также имена и описания параметров функции. Затем передадим эту схему клиенту, созданному ранее, вместе с запросом пользователя о времени в Сан-Франциско. Важно отметить, что **возвращается вызов инструмента**, **а не конечный ответ** на вопрос. Как упоминалось ранее, LLM возвращает имя выбранной для задачи функции и аргументы, которые будут переданы ей.

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
  
    # Начальное сообщение пользователя
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Первый вызов API: Попросить модель использовать функцию
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Обработка ответа модели
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Код функции для выполнения задачи:**

    Теперь, когда LLM выбрала функцию, которую нужно вызвать, необходимо реализовать и выполнить код, выполняющий задачу. Можно написать код получения текущего времени на Python. Также потребуется код для извлечения имени и аргументов из response_message, чтобы получить окончательный результат.

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
  
      # Второй вызов API: Получение окончательного ответа от модели
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

Вызов функций лежит в основе большинства, если не всех, реализаций паттерна использования инструментов агентов, однако реализовать его с нуля иногда бывает сложно. Как мы узнали в [Уроке 2](../../../02-explore-agentic-frameworks), агентные фреймворки предоставляют нам готовые строительные блоки для реализации использования инструментов.

## Примеры использования инструментов с агентными фреймворками

Ниже приведены примеры того, как можно реализовать паттерн проектирования использования инструментов с помощью различных агентных фреймворков:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> — это open-source AI-фреймворк для разработчиков на .NET, Python и Java, работающих с Большими Языковыми Моделями (LLM). Он упрощает процесс использования вызова функций, автоматически описывая ваши функции и их параметры модели через процесс, называемый <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">сериализацией</a>. Он также управляет двусторонним взаимодействием между моделью и вашим кодом. Другим преимуществом использования агентного фреймворка, такого как Semantic Kernel, является возможность обращаться к готовым инструментам, таким как <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Поиск файлов</a> и <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Интерпретатор кода</a>.

Следующая диаграмма иллюстрирует процесс вызова функций с Semantic Kernel:

![function calling](../../../translated_images/ru/functioncalling-diagram.a84006fc287f6014.webp)

В Semantic Kernel функции/инструменты называются <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">плагинами</a>. Мы можем преобразовать функцию `get_current_time`, которую рассматривали ранее, в плагин, превратив её в класс с функцией внутри. Также можно импортировать декоратор `kernel_function`, который принимает описание функции. Когда вы создаёте kernel с GetCurrentTimePlugin, kernel автоматически сериализует функцию и её параметры, создавая схему для отправки в LLM в процессе.

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

# Создать ядро
kernel = Kernel()

# Создать плагин
get_current_time_plugin = GetCurrentTimePlugin(location)

# Добавить плагин в ядро
kernel.add_plugin(get_current_time_plugin)
```
  
### Сервис агентов Azure AI

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> — более новый агентный фреймворк, предназначенный для того, чтобы позволить разработчикам безопасно создавать, развёртывать и масштабировать высококачественных и расширяемых AI-агентов без необходимости управлять базовыми вычислительными и хранилищными ресурсами. Он особенно полезен для корпоративных приложений, поскольку является полностью управляемым сервисом корпоративного уровня безопасности.

В сравнении с разработкой напрямую через API LLM Azure AI Agent Service предлагает следующие преимущества:

- Автоматический вызов инструментов — нет необходимости парсить вызов инструмента, запускать его и обрабатывать ответ; всё это теперь происходит на стороне сервера
- Безопасное управление данными — вместо управления собственным состоянием беседы можно полагаться на потоки (threads) для хранения всей необходимой информации
- Инструменты из коробки — инструменты, с помощью которых можно взаимодействовать с источниками данных, такими как Bing, Azure AI Search и Azure Functions.

Инструменты, доступные в Azure AI Agent Service, делятся на две категории:

1. Инструменты знаний:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Задействование Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Поиск файлов</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Инструменты действий:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Вызов функций</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Интерпретатор кода</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Инструменты, определённые через OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Сервис агентов позволяет использовать эти инструменты вместе как `toolset`. Он также использует `threads`, которые отслеживают историю сообщений в конкретном диалоге.

Представьте, что вы менеджер по продажам в компании Contoso. Вы хотите разработать диалогового агента, который сможет отвечать на вопросы о ваших данных по продажам.

Следующее изображение иллюстрирует, как можно использовать Azure AI Agent Service для анализа ваших данных продаж:

![Agentic Service In Action](../../../translated_images/ru/agent-service-in-action.34fb465c9a84659e.webp)

Чтобы использовать любой из этих инструментов в сервисе, можно создать клиента и определить инструмент или набор инструментов. Для практической реализации можно использовать следующий код на Python. LLM сможет посмотреть на toolset и решить, использовать ли пользовательскую функцию `fetch_sales_data_using_sqlite_query` или предустановленный Интерпретатор кода в зависимости от запроса пользователя.

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

# Инициализация набора инструментов
toolset = ToolSet()

# Инициализация агента вызова функций с функцией fetch_sales_data_using_sqlite_query и добавление его в набор инструментов
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Инициализация инструмента Code Interpreter и добавление его в набор инструментов.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Какие особенности нужно учитывать при использовании паттерна проектирования использования инструментов для создания надежных AI-агентов?

Распространённая проблема с динамически генерируемым LLM SQL — это безопасность, особенно риск SQL-инъекций или вредоносных действий, таких как удаление или повреждение базы данных. Хотя эти опасения обоснованы, их можно эффективно смягчить, правильно настроив права доступа к базе данных. Для большинства баз данных это включает настройку базы в режиме только для чтения. Для сервисов баз данных, таких как PostgreSQL или Azure SQL, приложению следует назначить роль только для чтения (SELECT).
Запуск приложения в защищённой среде дополнительно повышает уровень защиты. В корпоративных сценариях данные обычно извлекаются и преобразуются из операционных систем в базу данных или хранилище данных только для чтения с удобной для пользователей схемой. Такой подход обеспечивает безопасность данных, оптимизацию производительности и доступности, а также ограниченный доступ приложения только для чтения.

## Примеры кода

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Есть ещё вопросы об использовании паттернов проектирования инструментов?

Присоединяйтесь к [Discord Azure AI Foundry](https://aka.ms/ai-agents/discord), чтобы встретиться с другими обучающимися, посетить часы приёмов и получить ответы на вопросы по AI Agents.

## Дополнительные ресурсы

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Мастерская по службе Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Учебник по вызову функций Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Интерпретатор кода Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Инструменты Autogen</a>

## Предыдущий урок

[Понимание агентных паттернов проектирования](../03-agentic-design-patterns/README.md)

## Следующий урок

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на языке оригинала следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или искажения смысла, возникшие вследствие использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->