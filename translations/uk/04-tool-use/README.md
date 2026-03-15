[![Як проектувати хороших агентів ШІ](../../../translated_images/uk/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Патерн Використання Інструментів

Інструменти цікаві тим, що вони дозволяють агентам ШІ мати ширший набір можливостей. Замість того, щоб агент мав обмежений набір дій, додавання інструмента дає агенту змогу виконувати набагато ширший спектр операцій. У цій главі ми розглянемо Патерн Використання Інструментів, який описує, як агенти ШІ можуть використовувати конкретні інструменти для досягнення своїх цілей.

## Вступ

У цьому уроці ми прагнемо відповісти на такі питання:

- Що таке патерн використання інструментів?
- Для яких сценаріїв його можна застосувати?
- Які елементи/будівельні блоки потрібні для реалізації патерну?
- Які спеціальні міркування слід враховувати при використанні Патерну Використання Інструментів для створення надійних агентів ШІ?

## Цілі навчання

Після завершення цього уроку ви зможете:

- Визначити Патерн Використання Інструментів та його призначення.
- Визначити випадки використання, де застосовний Патерн Використання Інструментів.
- Зрозуміти ключові елементи, необхідні для реалізації патерну.
- Розпізнати міркування щодо забезпечення надійності агентів ШІ, які використовують цей патерн.

## Що таке Патерн Використання Інструментів?

Патерн використання інструментів зосереджується на наданні LLM можливості взаємодіяти з зовнішніми інструментами для досягнення конкретних цілей. Інструменти — це код, який агент може виконати для виконання дій. Інструментом може бути проста функція, така як калькулятор, або виклик API до стороннього сервісу, наприклад для отримання цін на акції чи прогнозу погоди. У контексті агентів ШІ інструменти розроблені для виконання агентами у відповідь на виклики функцій, згенеровані моделлю.

## Для яких сценаріїв його можна застосувати?

Агенти ШІ можуть використовувати інструменти для виконання складних завдань, отримання інформації або прийняття рішень. Патерн використання інструментів часто застосовується в сценаріях, що вимагають динамічної взаємодії із зовнішніми системами, такими як бази даних, веб-служби або інтерпретатори коду. Ця можливість корисна для низки випадків використання, зокрема:

- **Динамічне отримання інформації:** Агенти можуть звертатися до зовнішніх API або баз даних для отримання актуальних даних (наприклад, запит до SQLite бази даних для аналізу даних, отримання цін на акції або інформації про погоду).
- **Виконання та інтерпретація коду:** Агенти можуть виконувати код або скрипти для вирішення математичних задач, створення звітів або проведення симуляцій.
- **Автоматизація робочих процесів:** Автоматизація повторюваних або багатокрокових робочих процесів за допомогою інтеграції інструментів, таких як планувальники завдань, поштові сервіси або канали передачі даних.
- **Підтримка клієнтів:** Агенти можуть взаємодіяти з CRM-системами, платформами для звернень або базами знань для вирішення запитів користувачів.
- **Генерація та редагування контенту:** Агенти можуть використовувати інструменти, такі як перевірка граматики, підсумовувачі текстів або оцінювачі безпеки контенту, щоб допомагати у створенні матеріалів.

## Які елементи/будівельні блоки потрібні для реалізації патерну використання інструментів?

Ці будівельні блоки дозволяють агенту ШІ виконувати широкий спектр завдань. Розглянемо ключові елементи, необхідні для реалізації Патерну Використання Інструментів:

- **Схеми функцій/інструментів:** Детальні визначення доступних інструментів, включаючи назву функції, призначення, обов'язкові параметри та очікувані результати. Ці схеми дозволяють LLM розуміти, які інструменти доступні і як формувати дійсні запити.

- **Логіка виконання функцій:** Регулює, як і коли викликаються інструменти на основі намірів користувача та контексту розмови. Це може включати модулі планування, механізми маршрутизації або умовні сценарії, які визначають використання інструментів динамічно.

- **Система обробки повідомлень:** Компоненти, що керують потоком розмови між введеннями користувача, відповідями LLM, викликами інструментів та їх результатами.

- **Фреймворк інтеграції інструментів:** Інфраструктура, що підключає агента до різних інструментів, будь то прості функції або складні зовнішні служби.

- **Обробка помилок та валідація:** Механізми для обробки збоїв виконання інструментів, валідації параметрів та керування несподіваними відповідями.

- **Управління станом:** Відстеження контексту бесіди, попередніх взаємодій з інструментами та постійних даних, щоб забезпечити послідовність у багатокрокових взаємодіях.

Далі розглянемо Виклик Функцій/Інструментів детальніше.
 
### Виклик функцій/інструментів

Виклик функцій — це основний спосіб, яким ми надаємо великим мовним моделям (LLM) можливість взаємодіяти з інструментами. Ви часто побачите, що 'Function' і 'Tool' використовуються взаємозамінно, оскільки 'функції' (блоки багаторазового коду) є 'інструментами', які агенти використовують для виконання завдань. Щоб код функції було викликано, LLM має порівняти запит користувача з описом функцій. Для цього схема, що містить описи всіх доступних функцій, надсилається до LLM. LLM потім обирає найбільш відповідну функцію для завдання і повертає її назву та аргументи. Обрана функція виконується, її відповідь надсилається назад до LLM, яке використовує цю інформацію для відповіді на запит користувача.

Щоб розробники могли реалізувати виклик функцій для агентів, вам знадобиться:

1. Модель LLM, яка підтримує виклик функцій
2. Схема, що містить описи функцій
3. Код для кожної описаної функції

Розглянемо приклад отримання поточного часу в місті:

1. **Ініціалізувати LLM, який підтримує виклик функцій:**

    Не всі моделі підтримують виклик функцій, тому важливо перевірити, чи підтримує це та модель, яку ви використовуєте.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> підтримує виклик функцій. Ми можемо почати з ініціалізації клієнта Azure OpenAI. 

    ```python
    # Ініціалізуйте клієнта Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Створити схему функції:**

    Далі ми визначимо JSON-схему, яка містить назву функції, опис того, що вона робить, а також назви й описи параметрів функції.
    Потім ми передамо цю схему клієнту, створеному раніше, разом із запитом користувача знайти час у Сан-Франциско. Важливо зазначити, що **виклик інструмента** — це те, що повертається, **а не** остаточна відповідь на запит. Як уже було сказано, LLM повертає назву функції, яку воно обрало для завдання, та аргументи, які будуть передані їй.

    ```python
    # Опис функції для читання моделлю
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
  
    # Початкове повідомлення користувача
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Перший виклик API: Попросіть модель використати функцію
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Обробіть відповідь моделі
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Код функції, необхідний для виконання завдання:**

    Тепер, коли LLM обрало, яку функцію потрібно запустити, необхідно реалізувати і виконати код, що виконує завдання.
    Ми можемо реалізувати код для отримання поточного часу на Python. Також нам потрібно буде написати код для витягання назви й аргументів із response_message, щоб отримати остаточний результат.

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
     # Обробляти виклики функцій
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
  
      # Другий виклик API: Отримати остаточну відповідь від моделі
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

Виклик функцій є в основі більшості, якщо не всіх, рішень з використання інструментів для агентів, проте реалізувати його з нуля іноді буває складно.
Як ми дізналися в [Lesson 2](../../../02-explore-agentic-frameworks), агентні фреймворки надають нам готові будівельні блоки для реалізації використання інструментів.
 
## Приклади використання інструментів з агентними фреймворками

Ось кілька прикладів того, як ви можете реалізувати Патерн Використання Інструментів за допомогою різних агентних фреймворків:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> — це open-source фреймворк для створення агентів ШІ. Він спрощує процес використання виклику функцій, дозволяючи визначати інструменти як Python-функції з декоратором `@tool`. Фреймворк обробляє двосторонню комунікацію між моделлю та вашим кодом. Він також надає доступ до готових інструментів, таких як Пошук у файлах і Інтерпретатор коду через `AzureAIProjectAgentProvider`.

Наступна діаграма ілюструє процес виклику функцій з Microsoft Agent Framework:

![function calling](../../../translated_images/uk/functioncalling-diagram.a84006fc287f6014.webp)

У Microsoft Agent Framework інструменти визначаються як задекоровані функції. Ми можемо перетворити функцію `get_current_time`, яку ми бачили раніше, на інструмент, використавши декоратор `@tool`. Фреймворк автоматично серіалізує функцію та її параметри, створюючи схему для надсилання до LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Створити клієнта
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Створити агента і запустити його за допомогою інструменту
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> — це новіший агентний фреймворк, розроблений для того, щоб дати розробникам змогу безпечно створювати, розгортати та масштабувати високоякісні та розширювані агенти ШІ без необхідності керувати базовими обчислювальними та сховищними ресурсами. Він особливо корисний для корпоративних застосунків, оскільки є повністю керованим сервісом із корпоративним рівнем безпеки.

У порівнянні з розробкою безпосередньо через API LLM, Azure AI Agent Service надає кілька переваг, зокрема:

- Автоматичний виклик інструментів — немає потреби розбирати виклик інструмента, викликати інструмент і обробляти відповідь; все це тепер виконується на сервері
- Безпечно керовані дані — замість того, щоб керувати власним станом розмови, ви можете покладатися на threads для збереження всієї необхідної інформації
- Готові інструменти — інструменти, які можна використовувати для взаємодії з джерелами даних, такі як Bing, Azure AI Search та Azure Functions.

Інструменти, доступні в Azure AI Agent Service, можна поділити на дві категорії:

1. Інструменти знань:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Інструменти дій:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service дозволяє нам використовувати ці інструменти разом як `toolset`. Він також використовує `threads`, які відстежують історію повідомлень з певної розмови.

Уявіть, що ви торговий представник у компанії під назвою Contoso. Ви хочете розробити розмовного агента, який може відповідати на запитання щодо ваших продажів.

Наступне зображення ілюструє, як ви могли б використовувати Azure AI Agent Service для аналізу ваших даних про продажі:

![Agentic Service In Action](../../../translated_images/uk/agent-service-in-action.34fb465c9a84659e.webp)

Щоб використовувати будь-який із цих інструментів у сервісі, ми можемо створити клієнта та визначити інструмент або набір інструментів. Щоб реалізувати це на практиці, ми можемо використати наступний код на Python. LLM зможе подивитися на toolset і вирішити, чи використовувати створену користувачем функцію `fetch_sales_data_using_sqlite_query`, чи вбудований Code Interpreter залежно від запиту користувача.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # функція fetch_sales_data_using_sqlite_query, яку можна знайти у файлі fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Ініціалізувати набір інструментів
toolset = ToolSet()

# Ініціалізувати агента, що викликає функцію, з функцією fetch_sales_data_using_sqlite_query та додати його до набору інструментів
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Ініціалізувати інструмент Code Interpreter і додати його до набору інструментів.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Які спеціальні міркування слід враховувати при використанні Патерну Використання Інструментів для побудови надійних агентів ШІ?

Поширеною проблемою щодо динамічно згенерованого SQL від LLM є безпека, зокрема ризик SQL-ін'єкцій або шкідливих дій, таких як видалення або підробка бази даних. Хоча ці занепокоєння є обґрунтованими, їх можна ефективно пом'якшити шляхом належної конфігурації дозволів доступу до бази даних. Для більшості баз даних це передбачає налаштування бази даних у режимі тільки для читання. Для служб баз даних, таких як PostgreSQL або Azure SQL, додаток повинен мати призначену роль тільки для читання (SELECT).

Запуск додатка в безпечному середовищі додатково підвищує захист. У корпоративних сценаріях дані зазвичай витягуються та перетворюються з операційних систем у базу даних тільки для читання або сховище даних з дружньою схемою. Такий підхід забезпечує безпеку даних, оптимізує їх для продуктивності та доступності, а також гарантує, що додаток має обмежений доступ тільки для читання.

## Зразки коду

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Маєте ще питання про Патерни Використання Інструментів?

Приєднуйтесь до [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), щоб зустрітися з іншими учнями, відвідати години консультацій і отримати відповіді на свої запитання щодо агентів ШІ.

## Додаткові ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overview</a>

## Попередній урок

[Розуміння агентних патернів проектування](../03-agentic-design-patterns/README.md)

## Наступний урок
[Агентний RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено із використанням сервісу машинного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, просимо звернути увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ мовою оригіналу слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного перекладу, виконаного людиною. Ми не несемо відповідальності за будь-які непорозуміння чи неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->