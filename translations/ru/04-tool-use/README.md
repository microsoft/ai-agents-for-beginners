[![Как создать хороших AI-агентов](../../../translated_images/ru/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Нажмите на изображение выше, чтобы посмотреть видео этого урока)_

# Паттерн проектирования использования инструментов

Инструменты интересны тем, что они позволяют AI-агентам расширять диапазон своих возможностей. Вместо того, чтобы агент имел ограниченный набор действий, которые он может выполнять, добавление инструмента позволяет агенту выполнять широкий спектр действий. В этой главе мы рассмотрим паттерн проектирования использования инструментов, который описывает, как AI-агенты могут использовать конкретные инструменты для достижения своих целей.

## Введение

В этом уроке мы постараемся ответить на следующие вопросы:

- Что такое паттерн проектирования использования инструментов?
- В каких случаях он применяется?
- Какие элементы/строительные блоки необходимы для реализации этого паттерна?
- Какие особенности нужно учитывать при использовании паттерна проектирования использования инструментов для создания надежных AI-агентов?

## Цели обучения

По окончании этого урока вы сможете:

- Определить паттерн проектирования использования инструментов и его назначение.
- Выявлять случаи применения паттерна использования инструментов.
- Понять ключевые элементы, необходимые для реализации этого паттерна.
- Определять особенности обеспечения надежности AI-агентов, использующих данный паттерн.

## Что такое паттерн проектирования использования инструментов?

**Паттерн проектирования использования инструментов** направлен на предоставление LLM (моделям с большим языковым потенциалом) возможности взаимодействовать с внешними инструментами для достижения конкретных целей. Инструменты — это код, который агент может выполнить для выполнения действий. Инструментом может быть простая функция, например калькулятор, или вызов API стороннего сервиса, например получение курса акций или прогноза погоды. В контексте AI-агентов инструменты предназначены для выполнения агентами в ответ на **функциональные вызовы, сгенерированные моделью**.

## В каких случаях применяется этот паттерн?

AI-агенты могут использовать инструменты для выполнения сложных задач, получения информации или принятия решений. Паттерн проектирования использования инструментов часто применяется в сценариях, требующих динамического взаимодействия с внешними системами, такими как базы данных, веб-сервисы или интерпретаторы кода. Эта возможность полезна в различных случаях, включая:

- **Динамическое получение информации:** Агент может запрашивать данные из внешних API или баз данных для получения актуальной информации (например, запрос данных из базы SQLite для анализа, получение цен на акции или прогноза погоды).
- **Выполнение и интерпретация кода:** Агент может выполнять код или скрипты для решения математических задач, генерации отчетов или проведения симуляций.
- **Автоматизация рабочих процессов:** Автоматизация повторяющихся или многошаговых процессов путем интеграции инструментов, таких как планировщики задач, почтовые сервисы или каналы обработки данных.
- **Поддержка клиентов:** Агент может взаимодействовать с CRM-системами, платформами поддержки или базами знаний для решения запросов пользователей.
- **Создание и редактирование контента:** Агент может использовать инструменты, такие как проверка грамматики, суммаризация текста или оценка безопасности контента, чтобы помочь в задачах создания контента.

## Какие элементы/строительные блоки необходимы для реализации паттерна использования инструментов?

Эти строительные блоки позволяют AI-агенту выполнять широкий спектр задач. Рассмотрим ключевые элементы, необходимые для реализации паттерна проектирования использования инструментов:

- **Схемы функций/инструментов**: Подробные определения доступных инструментов, включая имя функции, назначение, требуемые параметры и ожидаемые результаты. Эти схемы позволяют LLM понимать, какие инструменты доступны и как формировать корректные запросы.

- **Логика выполнения функций**: Управляет тем, как и когда вызываются инструменты на основе намерений пользователя и контекста разговора. Это может включать модули планирования, маршрутизации или условные потоки, динамически определяющие использование инструментов.

- **Система обработки сообщений**: Компоненты, которые управляют ходом диалога между вводом пользователя, ответами LLM, вызовами инструментов и их результатами.

- **Фреймворк интеграции инструментов**: Инфраструктура, которая связывает агента с разными инструментами, будь то простые функции или сложные внешние сервисы.

- **Обработка ошибок и валидация**: Механизмы для обработки сбоев в выполнении инструментов, проверки параметров и управления неожиданными ответами.

- **Управление состоянием**: Отслеживает контекст разговора, предыдущие взаимодействия с инструментами и постоянные данные для обеспечения согласованности в многошаговом взаимодействии.

Далее рассмотрим вызов функций/инструментов более подробно.
 
### Вызов функции/инструмента

Вызов функции — это основной способ, с помощью которого мы даём возможность крупным языковым моделям (LLM) взаимодействовать с инструментами. Часто термины «функция» и «инструмент» используются взаимозаменяемо, поскольку «функции» (блоки повторно используемого кода) — это «инструменты», которые агенты используют для выполнения задач. Чтобы вызвать код функции, LLM должен сравнить запрос пользователя с описанием функций. Для этого схему с описанием всех доступных функций отправляют модели. LLM выбирает наиболее подходящую функцию для задачи и возвращает её имя и аргументы. Выбранная функция вызывается, её результат возвращается LLM, который использует информацию для ответа на запрос пользователя.

Чтобы реализовать вызов функций для агентов, вам понадобится:

1. Модель LLM, поддерживающая вызов функций
2. Схема с описанием функций
3. Код для каждой описанной функции

Рассмотрим на примере получения текущего времени в городе:

1. **Инициализировать LLM с поддержкой вызова функций:**

    Не все модели поддерживают вызовы функций, поэтому важно проверить, поддерживает ли используемая вами LLM эту возможность. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> поддерживает вызов функций. Мы можем начать с инициализации клиента OpenAI для Azure OpenAI **Responses API** (стабильный эндпоинт `/openai/v1/` — без необходимости указывать `api_version`). 

    ```python
    # Инициализируйте клиент OpenAI для Azure OpenAI (Responses API, конечная точка v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Создать схему функции:**

    Далее мы определим JSON-схему, содержащую имя функции, описание её назначения, а также имена и описания параметров функции.
    Затем эту схему мы передадим ранее созданному клиенту вместе с запросом пользователя о времени в Сан-Франциско. Важно отметить, что возвращается не конечный ответ на вопрос, а **вызов инструмента**. Как упоминалось ранее, LLM возвращает имя выбранной для задачи функции и аргументы, которые будут ей переданы.

    ```python
    # Описание функции для модели (формат инструмента Responses API flat)
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
  
    # Начальное сообщение пользователя
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Первый вызов API: Попросите модель использовать функцию
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # API ответов возвращает вызовы инструментов как элементы function_call в response.output.
    # Добавьте их в разговор, чтобы модель имела полный контекст на следующем шаге.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Код функции, необходимый для выполнения задачи:**

    Теперь, когда LLM выбрала функцию, которая должна быть выполнена, нужно реализовать и запустить код, выполняющий задачу.
    Мы можем написать код на Python для получения текущего времени. Также нужно реализовать код, который извлечет имя функции и аргументы из response_message для получения окончательного результата.

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

                # Возврат результата инструмента в виде элемента function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Второй вызов API: Получение окончательного ответа от модели
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

Вызов функций лежит в основе большинства, если не всех, паттернов использования инструментов для агентов, однако реализовать его с нуля иногда сложно.
Как мы узнали в [Уроке 2](../../../02-explore-agentic-frameworks), агентные фреймворки предоставляют предварительно собранные строительные блоки для реализации использования инструментов.
 
## Примеры использования инструментов с агентными фреймворками

Вот несколько примеров того, как можно реализовать паттерн использования инструментов с помощью различных агентных фреймворков:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> — это открытый AI-фреймворк для создания AI-агентов. Он упрощает процесс вызова функций, позволяя определять инструменты как Python-функции с использованием декоратора `@tool`. Фреймворк обрабатывает двустороннюю коммуникацию между моделью и вашим кодом. Также предоставляет доступ к предварительно созданным инструментам, таким как Поиск по файлам и Интерпретатор кода через `FoundryChatClient`.

На следующей диаграмме показан процесс вызова функций с использованием Microsoft Agent Framework:

![вызов функции](../../../translated_images/ru/functioncalling-diagram.a84006fc287f6014.webp)

В Microsoft Agent Framework инструменты определяются как декорированные функции. Мы можем преобразовать функцию `get_current_time`, которую видели ранее, в инструмент, используя декоратор `@tool`. Фреймворк автоматически сериализует функцию и её параметры, создавая схему для отправки её LLM.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> — новый агентный фреймворк, созданный для того, чтобы разработчики могли безопасно создавать, развертывать и масштабировать высококачественных расширяемых AI-агентов без необходимости управлять базовой вычислительной и хранилищной инфраструктурой. Он особенно полезен для корпоративных приложений, так как является полностью управляемым сервисом с корпоративным уровнем безопасности.

По сравнению с разработкой напрямую с LLM API, Microsoft Foundry Agent Service предлагает следующие преимущества:

- Автоматический вызов инструментов — не нужно самостоятельно разбирать вызовы инструментов, запускать инструменты и обрабатывать ответы; всё это теперь выполняется на серверной стороне.
- Безопасное управление данными — вместо управления состоянием разговора вручную, вы можете полагаться на `threads`, которые хранят всю необходимую информацию.
- Инструменты из коробки — инструменты для взаимодействия с вашими источниками данных, такие как Bing, Azure AI Search и Azure Functions.

Инструменты, доступные в Microsoft Foundry Agent Service, можно разделить на две категории:

1. Инструменты знаний:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Поддержка поиска Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Поиск по файлам</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Инструменты действий:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Вызов функций</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Интерпретатор кода</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Инструменты, определённые через OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Сервис Agent Service позволяет использовать эти инструменты вместе как `набор инструментов`. Он также использует `threads`, которые отслеживают историю сообщений конкретного разговора.

Представьте, что вы агент по продажам в компании Contoso. Вы хотите создать разговорного агента, который сможет отвечать на вопросы о ваших данных по продажам.

Следующее изображение иллюстрирует, как можно использовать Microsoft Foundry Agent Service для анализа ваших данных по продажам:

![Agentic Service в действии](../../../translated_images/ru/agent-service-in-action.34fb465c9a84659e.webp)

Для использования любых из этих инструментов с сервисом мы можем создать клиента и определить инструмент или набор инструментов. Практическая реализация может выглядеть так в коде на Python. LLM сможет просмотреть набор инструментов и решить, использовать ли пользовательскую функцию `fetch_sales_data_using_sqlite_query` или встроенный Интерпретатор кода в зависимости от запроса пользователя.

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

# Инициализация агента вызова функции с использованием функции fetch_sales_data_using_sqlite_query и добавление ее в набор инструментов
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Инициализация инструмента интерпретатора кода и добавление его в набор инструментов.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Особые соображения при использовании паттерна проектирования использования инструментов для создания надежных AI-агентов

Распространённая проблема при динамическом формировании SQL-запросов LLM — это безопасность, в особенности риск SQL-инъекций или злонамеренных действий, таких как удаление или изменение базы данных. Хотя эти опасения обоснованы, их можно эффективно минимизировать правильной конфигурацией прав доступа к базе данных. Для большинства баз данных это означает настройку базы в режиме только для чтения. Для сервисов баз данных, таких как PostgreSQL или Azure SQL, приложению нужно назначить роль только для чтения (SELECT).

Запуск приложения в безопасной среде дополнительно усиливает защиту. В корпоративных сценариях данные обычно извлекаются и преобразуются из операционных систем в базу данных или хранилище данных с режимом только для чтения и удобной схемой. Такой подход обеспечивает безопасность данных, их оптимизацию для производительности и доступности, а также ограниченный доступ приложения только на чтение.

## Примеры кода

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Есть вопросы по паттерну проектирования использования инструментов?

Присоединяйтесь к [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), чтобы встретиться с другими учащимися, посетить офисные часы и получить ответы на ваши вопросы по AI-агентам.

## Дополнительные ресурсы

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Мастерская Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Мастерская Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Обзор Microsoft Agent Framework</a>


## Быстрый тест этого агента (необязательно)

После того как вы научитесь развертывать агентов в [Уроке 16](../16-deploying-scalable-agents/README.md), вы можете быстро протестировать `TravelToolAgent` из этого урока (вызывает ли он свои инструменты и отвечает ли?) с помощью [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). См. [`tests/README.md`](../tests/README.md) для инструкций по запуску.

## Предыдущий урок

[Понимание агентных шаблонов проектирования](../03-agentic-design-patterns/README.md)

## Следующий урок

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:
Этот документ был переведен с использованием сервиса машинного перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обратиться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->