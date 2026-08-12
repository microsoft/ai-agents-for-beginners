[![Как создавать хорошие AI-агенты](../../../translated_images/ru/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Шаблон проектирования использования инструментов

Инструменты интересны тем, что позволяют AI-агентам иметь более широкий спектр возможностей. Вместо того чтобы агент имел ограниченный набор действий, которые он может выполнять, при добавлении инструмента агент теперь может выполнять широкий спектр действий. В этой главе мы рассмотрим шаблон проектирования использования инструментов, который описывает, как AI-агенты могут использовать конкретные инструменты для достижения своих целей.

## Введение

В этом уроке мы постараемся ответить на следующие вопросы:

- Что такое шаблон проектирования использования инструментов?
- Для каких случаев применения он подходит?
- Какие элементы/строительные блоки нужны для реализации этого шаблона?
- Какие особые соображения необходимо учитывать при использовании шаблона проектирования для создания надежных AI-агентов?

## Цели обучения

После завершения этого урока вы сможете:

- Определить что такое шаблон проектирования использования инструментов и его назначение.
- Опознать случаи применения, где шаблон использования инструментов применим.
- Понять ключевые элементы, необходимые для реализации шаблона.
- Осознать соображения для обеспечения надежности AI-агентов, использующих этот шаблон.

## Что такое шаблон проектирования использования инструментов?

**Шаблон проектирования использования инструментов** сосредоточен на предоставлении LLM возможности взаимодействовать с внешними инструментами для достижения конкретных целей. Инструменты — это код, который агент может выполнять для совершения действий. Инструментом может быть простая функция, такая как калькулятор, или вызов API стороннего сервиса, например, для поиска цены акции или прогноза погоды. В контексте AI-агентов инструменты разработаны для исполнения агентами в ответ на **вызовы функций, сгенерированные моделью**.

## Для каких случаев применения он подходит?

AI-агенты могут использовать инструменты для выполнения сложных задач, получения информации или принятия решений. Шаблон использования инструментов часто применяется в сценариях, требующих динамического взаимодействия с внешними системами, такими как базы данных, веб-сервисы или интерпретаторы кода. Эта возможность полезна для различных случаев, включая:

- **Динамический поиск информации:** агенты могут запрашивать внешние API или базы данных для получения актуальных данных (например, запрос в базу данных SQLite для анализа данных, получение цен акций или информации о погоде).
- **Выполнение и интерпретация кода:** агенты могут выполнять код или скрипты для решения математических задач, создания отчетов или проведения симуляций.
- **Автоматизация рабочих процессов:** автоматизация повторяющихся или многоэтапных процессов посредством интеграции таких инструментов, как планировщики задач, почтовые сервисы или конвейеры обработки данных.
- **Клиентская поддержка:** агенты могут взаимодействовать с CRM-системами, платформами тикетов или базами знаний для решения запросов пользователей.
- **Создание и редактирование контента:** агенты могут использовать инструменты, такие как проверка грамматики, суммирование текста или оценка безопасности контента, чтобы помогать в создании материалов.

## Какие элементы/строительные блоки нужны для реализации шаблона использования инструментов?

Эти строительные блоки позволяют AI-агенту выполнять широкий спектр задач. Рассмотрим ключевые элементы, необходимые для реализации шаблона проектирования использования инструментов:

- **Схемы функций/инструментов**: подробные определения доступных инструментов, включая имя функции, назначение, обязательные параметры и ожидаемые результаты. Эти схемы позволяют LLM понять, какие инструменты доступны и как формировать корректные запросы.

- **Логика выполнения функций**: определяет, как и когда вызываются инструменты на основе намерений пользователя и контекста разговора. Это может включать модули планирования, механизмы маршрутизации или условные переходы, которые динамически определяют использование инструментов.

- **Система обработки сообщений**: компоненты, управляющие потоком взаимодействия между вводом пользователя, ответами LLM, вызовами инструментов и их результатами.

- **Фреймворк интеграции инструментов**: инфраструктура, соединяющая агента с различными инструментами, будь то простые функции или сложные внешние сервисы.

- **Обработка ошибок и валидация**: механизмы для обработки сбоев при исполнении инструментов, проверки параметров и управления неожиданными ответами.

- **Управление состоянием**: отслеживает контекст разговора, предыдущие взаимодействия с инструментами и постоянные данные, чтобы обеспечить последовательность в многошаговых взаимодействиях.

Далее рассмотрим более подробно вызов функций/инструментов.
 
### Вызов функций/инструментов

Вызов функций — это основной способ, с помощью которого мы даем возможностям больших языковых моделей (LLM) взаимодействовать с инструментами. Вы часто увидите, что 'Функция' и 'Инструмент' используются взаимозаменяемо, потому что «функции» (блоки переиспользуемого кода) являются «инструментами», с помощью которых агенты выполняют задачи. Чтобы вызвать код функции, LLM должен сопоставить запрос пользователя с описанием функций. Для этого схема, содержащая описания всех доступных функций, отправляется LLM. LLM выбирает наиболее подходящую функцию для задачи и возвращает её имя и аргументы. Выбранная функция вызывается, её ответ отправляется обратно в LLM, который использует эту информацию для ответа на запрос пользователя.

Чтобы разработчикам реализовать вызов функций для агентов, вам понадобятся:

1. Модель LLM, поддерживающая вызов функций
2. Схема с описаниями функций
3. Код для каждой описанной функции

Рассмотрим пример получения текущего времени в городе:

1. **Инициализировать LLM, поддерживающую вызов функций:**

    Не все модели поддерживают вызов функций, поэтому важно проверить, что используемая вами модель это умеет.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> поддерживает вызов функций. Мы можем начать с инициализации клиента OpenAI к Azure OpenAI **Responses API** (стабильный эндпоинт `/openai/v1/` — `api_version` не нужен).

    ```python
    # Инициализируйте клиент OpenAI для Azure OpenAI (Responses API, конечная точка v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Создать схему функции**:

    Далее мы определим JSON-схему, которая содержит имя функции, описание того, что она делает, а также имена и описания параметров функции.
    Затем мы передадим эту схему клиенту, созданному ранее, вместе с запросом пользователя узнать время в Сан-Франциско. Важно отметить, что возвращается **вызов инструмента**, а **не** окончательный ответ на вопрос. Как упоминалось выше, LLM возвращает имя выбранной функции и аргументы, которые будут ей переданы.

    ```python
    # Описание функции для модели для чтения (формат инструмента Responses API flat)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # Исходное сообщение пользователя
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Первый вызов API: попросить модель использовать функцию
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # API ответов возвращает вызовы инструментов как элементы function_call в response.output.
    # Добавьте их в разговор, чтобы у модели был полный контекст на следующий ход.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Код функции, необходимый для выполнения задачи:**

    Теперь, когда LLM выбрала, какую функцию нужно исполнить, необходимо реализовать и выполнить код, выполняющий задачу.
    Мы можем реализовать код для получения текущего времени на Python. Также нам потребуется написать код для извлечения имени и аргументов из response_message, чтобы получить окончательный результат.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Вернуть результат инструмента как элемент function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Второй вызов API: Получить окончательный ответ от модели
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Вызов функций лежит в основе большинства, если не всех, реализаций шаблона использования инструментов для агентов, однако реализовать это с нуля порой бывает сложно.
Как мы узнали в [Уроке 2](../../../02-explore-agentic-frameworks), агентские фреймворки предоставляют нам готовые строительные блоки для реализации использования инструментов.
 
## Примеры использования инструментов с агентскими фреймворками

Вот некоторые примеры того, как можно реализовать шаблон использования инструментов с помощью различных агентских фреймворков:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> — это открытый AI-фреймворк для создания AI-агентов. Он упрощает процесс использования вызова функций, позволяя определять инструменты как Python-функции с декоратором `@tool`. Фреймворк обрабатывает двунаправленное общение между моделью и вашим кодом. Также он предоставляет доступ к готовым инструментам, таким как Поиск файлов и Интерпретатор кода, через `FoundryChatClient`.

Следующая диаграмма иллюстрирует процесс вызова функций с Microsoft Agent Framework:

![function calling](../../../translated_images/ru/functioncalling-diagram.a84006fc287f6014.webp)

В Microsoft Agent Framework инструменты определяются как декорированные функции. Мы можем преобразовать функцию `get_current_time`, рассмотренную ранее, в инструмент, используя декоратор `@tool`. Фреймворк автоматически сериализует функцию и её параметры, создавая схему для передачи в LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Создать клиента
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Создать агента и запустить с инструментом
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> — более современный агентский фреймворк, предназначенный для того, чтобы дать разработчикам возможность безопасно создавать, развертывать и масштабировать высококачественных и расширяемых AI-агентов без необходимости управлять вычислительными и хранилищными ресурсами. Он особенно полезен в корпоративных приложениях, поскольку является полностью управляемым сервисом с корпоративным уровнем безопасности.

По сравнению с разработкой напрямую через API LLM, Microsoft Foundry Agent Service предоставляет некоторые преимущества, включая:

- Автоматический вызов инструментов — не нужно парсить вызов инструмента, запускать инструмент и обрабатывать ответ; всё это теперь выполняется на стороне сервера
- Безопасно управляемые данные — вместо управления состоянием разговора самостоятельно, можно полагаться на ветки (threads), которые сохраняют всю необходимую информацию
- Инструменты "из коробки" — инструменты для взаимодействия с вашими источниками данных, такие как Bing, Azure AI Search и Azure Functions.

Инструменты, доступные в Microsoft Foundry Agent Service, можно разделить на две категории:

1. Инструменты знаний:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Поиск с Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Поиск файлов</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Инструменты действий:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Вызов функций</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Интерпретатор кода</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Инструменты, определённые OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Сервис агентов позволяет использовать эти инструменты вместе как `toolset`. Он также использует `threads`, которые отслеживают историю сообщений конкретного разговора.

Представьте, что вы агент по продажам в компании Contoso. Вы хотите разработать разговорного агента, который сможет отвечать на вопросы о ваших данных по продажам.

Следующее изображение иллюстрирует, как вы могли бы использовать Microsoft Foundry Agent Service для анализа данных по продажам:

![Agentic Service In Action](../../../translated_images/ru/agent-service-in-action.34fb465c9a84659e.webp)

Чтобы использовать любой из этих инструментов с сервисом, мы можем создать клиента и определить инструмент или набор инструментов. Для практической реализации можно использовать следующий код на Python. LLM сможет посмотреть на набор инструментов и решить, использовать ли созданную пользователем функцию `fetch_sales_data_using_sqlite_query` или встроенный Интерпретатор кода в зависимости от запроса пользователя.

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

# Инициализировать набор инструментов
toolset = ToolSet()

# Инициализировать агент вызова функции с функцией fetch_sales_data_using_sqlite_query и добавить его в набор инструментов
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Инициализировать инструмент интерпретатора кода и добавить его в набор инструментов.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Какие особые соображения необходимо учитывать при использовании шаблона проектирования для создания надежных AI-агентов?

Частая проблема с динамически генерируемым LLM SQL — безопасность, особенно риск SQL-инъекций или злонамеренных действий, таких как удаление или повреждение базы данных. Хотя эти опасения обоснованы, их можно эффективно снизить, правильно настроив права доступа к базе данных. Для большинства баз данных это означает конфигурацию в режиме только для чтения. Для сервисов баз данных, таких как PostgreSQL или Azure SQL, приложению следует назначить роль только для чтения (SELECT).

Запуск приложения в безопасной среде дополнительно повышает защиту. В корпоративных сценариях данные обычно извлекаются и трансформируются из операционных систем в базу данных или хранилище данных только для чтения с удобной схемой. Такой подход обеспечивает безопасность данных, оптимизацию по производительности и доступности, а также ограниченный, только для чтения, доступ для приложения.

## Примеры кода

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Остались вопросы по шаблону проектирования использования инструментов?

Присоединяйтесь к [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), чтобы встретиться с другими учащимися, посетить часы приёма и получить ответы на вопросы о ваших AI-агентах.

## Дополнительные ресурсы

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Мастерская по сервису Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Мастерская многоагентной системы Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Обзор Microsoft Agent Framework</a>


## Быстрое тестирование этого агента (по желанию)

После того как вы научитесь разворачивать агентов в [Уроке 16](../16-deploying-scalable-agents/README.md), вы можете быстро протестировать `TravelToolAgent` из этого урока (вызывает ли он по-прежнему свои инструменты и отвечает ли?) с помощью [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Смотрите [`tests/README.md`](../tests/README.md), чтобы узнать, как это сделать.

## Предыдущий урок

[Понимание агентных шаблонов проектирования](../03-agentic-design-patterns/README.md)

## Следующий урок

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->