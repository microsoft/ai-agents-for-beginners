[![Як проектувати хороших AI агентів](../../../translated_images/uk/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Шаблон проектування використання інструментів

Інструменти цікаві тим, що вони дозволяють AI агентам мати ширший спектр можливостей. Замість того, щоб агент мав обмежений набір дій, які він може виконувати, додаючи інструмент, тепер агент може виконувати широкий спектр дій. У цій главі ми розглянемо Шаблон проектування використання інструментів, який описує, як AI агенти можуть використовувати певні інструменти для досягнення своїх цілей.

## Вступ

У цьому уроці ми прагнемо відповісти на такі питання:

- Що таке шаблон проектування використання інструментів?
- Для яких випадків він може бути застосований?
- Які елементи/будівельні блоки потрібні для реалізації цього шаблону проектування?
- Які особливі зауваження стосовно використання шаблону проектування використання інструментів для створення надійних AI агентів?

## Цілі навчання

Після завершення цього уроку ви зможете:

- Визначити Шаблон проектування використання інструментів та його призначення.
- Виявити випадки застосування, де доречно використання цього шаблону.
- Зрозуміти ключові елементи, необхідні для реалізації цього шаблону проектування.
- Визначити зауваження щодо забезпечення надійності AI агентів, які використовують цей шаблон.

## Що таке Шаблон проектування використання інструментів?

**Шаблон проектування використання інструментів** зосереджений на наданні LLM можливості взаємодіяти із зовнішніми інструментами для досягнення конкретних цілей. Інструменти — це код, який може бути виконаний агентом для виконання дій. Інструмент може бути простою функцією, наприклад калькулятором, або викликом API до стороннього сервісу, такого як пошук цін на акції або прогноз погоди. У контексті AI агентів інструменти розроблені для виконання агентами у відповідь на **генеровані моделлю виклики функцій**.

## Для яких випадків він може бути застосований?

AI агенти можуть використовувати інструменти для виконання складних завдань, отримання інформації чи прийняття рішень. Шаблон проектування використання інструментів часто застосовується в сценаріях, які вимагають динамічної взаємодії з зовнішніми системами, такими як бази даних, веб-сервіси або інтерпретатори коду. Ця здатність корисна для низки різних випадків використання, включаючи:

- **Динамічне отримання інформації:** Агенти можуть звертатися до зовнішніх API або баз даних для отримання актуальних даних (наприклад, запити до бази даних SQLite для аналізу даних, отримання цін акцій чи інформації про погоду).
- **Виконання та інтерпретація коду:** Агенти можуть виконувати код або скрипти для розв’язання математичних задач, створення звітів або проведення симуляцій.
- **Автоматизація робочих процесів:** Автоматизація повторюваних або багатокрокових робочих процесів за допомогою інтеграції інструментів, таких як планувальники завдань, сервіси електронної пошти або канали обробки даних.
- **Підтримка клієнтів:** Агенти можуть взаємодіяти з CRM системами, платформами обробки звернень або базами знань для вирішення запитів користувачів.
- **Генерація та редагування контенту:** Агенти можуть використовувати інструменти на кшталт граматичних перевірок, резюме тексту або оцінювачів безпеки контенту для допомоги у створенні матеріалів.

## Які елементи/будівельні блоки потрібні для реалізації шаблону використання інструментів?

Ці будівельні блоки дозволяють AI агенту виконувати широкий спектр завдань. Розглянемо ключові елементи, потрібні для реалізації Шаблону проектування використання інструментів:

- **Схеми функцій/інструментів**: Детальні визначення доступних інструментів, включно з ім’ям функції, призначенням, необхідними параметрами та очікуваними результатами. Ці схеми дозволяють LLM розуміти, які інструменти доступні і як формувати дійсні запити.

- **Логіка виконання функцій**: Визначає, як і коли інструменти викликаються на основі наміру користувача та контексту розмови. Може включати модулі планування, механізми маршрутизації або умовні потоки, які динамічно визначають використання інструментів.

- **Система обробки повідомлень**: Компоненти, що керують діалогом між введеннями користувача, відповідями LLM, викликами інструментів та їх відповідями.

- **Фреймворк інтеграції інструментів**: Інфраструктура, яка під’єднує агента до різних інструментів, будь то прості функції або складні зовнішні сервіси.

- **Обробка помилок та валідація**: Механізми для обробки помилок виконання інструментів, перевірки параметрів та керування непередбачуваними відповідями.

- **Управління станом**: Відстеження контексту розмови, попередніх взаємодій з інструментами та збережених даних для забезпечення узгодженості у багатокрокових діалогах.

Далі розглянемо докладніше Виклик функції/інструменту.
 
### Виклик функції/інструмента

Виклик функції — це основний спосіб, яким ми надаємо великим мовним моделям (LLM) змогу взаємодіяти з інструментами. Часто терміни «Функція» і «Інструмент» використовують як синоніми, бо «функції» (блоки багаторазового використання коду) є «інструментами», які агенти застосовують для виконання завдань. Щоб код функції був викликаний, LLM має порівняти запит користувача з описом функції. Для цього до LLM надсилається схема, що містить описи всіх доступних функцій. LLM тоді обирає найбільш підходящу для завдання функцію та повертає її ім’я і аргументи. Обрана функція виконується, її відповідь повертається LLM, який використовує цю інформацію для формування відповіді на запит користувача.

Щоб реалізувати виклик функції для агентів, вам знадобиться:

1. Модель LLM, що підтримує виклики функцій
2. Схема функцій із їх описами
3. Код для кожної описаної функції

Візьмемо приклад отримання поточного часу в місті:

1. **Ініціалізуємо LLM, що підтримує виклики функцій:**

    Не всі моделі підтримують виклики функцій, тому важливо переконатись, що обрана модель це робить. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> підтримує виклики функцій. Почнемо з ініціалізації клієнта Azure OpenAI.

    ```python
    # Ініціалізуйте клієнт Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Створення схеми функції**:

    Далі ми визначимо JSON-схему, що містить ім’я функції, опис її призначення, а також імена і описи параметрів функції.
    Потім передамо цю схему клієнту, створеному раніше, разом із запитом користувача, який хоче дізнатись час у Сан-Франциско. Важливо відзначити, що результатом є **виклик інструменту**, **а не** остаточна відповідь на запитання. Як зазначалося раніше, LLM повертає ім’я обраної функції та аргументи, які будуть передані.

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
  
    # Перший виклик API: Запитайте модель використовувати функцію
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Обробити відповідь моделі
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

    Тепер, коли LLM вибрав функцію для запуску, потрібно реалізувати і виконати код, який виконує завдання.
    Ми реалізуємо код отримання поточного часу на Python. Також необхідно написати код, який витягає ім’я та аргументи з response_message, щоб отримати кінцевий результат.

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
     # Обробка викликів функцій
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

Виклик функції є основою більшості, якщо не всіх, реалізацій шаблону використання інструментів, проте його імплементація з нуля може іноді бути складною.
Як ми дізналися в [Уроці 2](../../../02-explore-agentic-frameworks), агентні фреймворки надають нам готові будівельні блоки для реалізації використання інструментів.
 
## Приклади використання інструментів з агентними фреймворками

Ось кілька прикладів, як можна реалізувати Шаблон проектування використання інструментів, використовуючи різні агентні фреймворки:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> — це відкрите фреймворк для AI розробників на .NET, Python та Java, що працюють з великими мовними моделями (LLM). Він спрощує процес використання викликів функцій, автоматично описуючи ваші функції та їх параметри для моделі за допомогою процесу, який називається <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">серіалізацією</a>. Також він обробляє двосторонню комунікацію між моделлю та вашим кодом. Ще одна перевага використання агентного фреймворка, як Semantic Kernel, — це доступ до готових інструментів, таких як <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Пошук файлів</a> та <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Інтерпретатор коду</a>.

Наступна діаграма ілюструє процес виклику функції з Semantic Kernel:

![function calling](../../../translated_images/uk/functioncalling-diagram.a84006fc287f6014.webp)

У Semantic Kernel функції/інструменти називаються <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Плагінами</a>. Ми можемо перетворити функцію `get_current_time`, яку бачили раніше, у плагін, створивши з неї клас із функцією всередині. Ми також можемо імпортувати декоратор `kernel_function`, який приймає опис функції. При створенні kernel з GetCurrentTimePlugin, kernel автоматично серіалізує функцію та її параметри, створюючи схему для відправлення LLM.

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

# Створити ядро
kernel = Kernel()

# Створити плагін
get_current_time_plugin = GetCurrentTimePlugin(location)

# Додати плагін до ядра
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> — це новіший агентний фреймворк, призначений для того, щоб надати розробникам можливість безпечно створювати, розгортати та масштабувати високоякісних і розширюваних AI агентів без необхідності керувати базовими обчислювальними та сховищними ресурсами. Він особливо корисний для корпоративних застосунків, оскільки є повністю керованим сервісом із корпоративним рівнем безпеки.

У порівнянні з розробкою безпосередньо через LLM API, Azure AI Agent Service має кілька переваг, зокрема:

- Автоматичний виклик інструментів — немає потреби вручну розбирати виклики інструментів, викликати їх та обробляти відповіді; все це виконується на сервері.
- Безпечно керовані дані — замість управління власним станом розмови можна покластися на threads (ниті), які зберігають всю необхідну інформацію.
- Інструменти з коробки — інструменти, що дозволяють взаємодіяти з вашими джерелами даних, наприклад Bing, Azure AI Search та Azure Functions.

Інструменти, доступні в Azure AI Agent Service, поділяються на дві категорії:

1. Інструменти знань:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Опора на Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Пошук файлів</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Інструменти дій:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Виклики функцій</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Інтерпретатор коду</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Інструменти, визначені OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Сервіс Agent дозволяє використовувати ці інструменти разом як `toolset`. Він також використовує `threads`, які відстежують історію повідомлень конкретної розмови.

Уявіть, що ви торговий агент у компанії під назвою Contoso. Ви хочете створити діалогового агента, який зможе відповідати на питання про ваші продажі.

Наступне зображення ілюструє, як можна використовувати Azure AI Agent Service для аналізу продажів:

![Agentic Service In Action](../../../translated_images/uk/agent-service-in-action.34fb465c9a84659e.webp)

Щоб використати будь-який із цих інструментів із сервісом, ми можемо створити клієнта й визначити інструмент або набір інструментів. Для практичної реалізації ми можемо використати наступний код на Python. LLM зможе переглянути набір інструментів і вирішити, чи використовувати створену користувачем функцію `fetch_sales_data_using_sqlite_query`, чи вбудований Інтерпретатор коду залежно від запиту користувача.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # функція fetch_sales_data_using_sqlite_query, яка знаходиться у файлі fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Ініціалізація набору інструментів
toolset = ToolSet()

# Ініціалізація агента виклику функції з функцією fetch_sales_data_using_sqlite_query та додавання її до набору інструментів
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Ініціалізація інструменту Інтерпретатор коду та додавання його до набору інструментів.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Які особливі зауваження при використанні Шаблону проектування використання інструментів для створення надійних AI агентів?

Поширене занепокоєння щодо динамічно згенерованого LLM SQL пов’язане з безпекою, зокрема ризиком SQL ін’єкцій або шкідливої діяльності, такої як видалення чи модифікація бази даних. Хоча ці занепокоєння є обґрунтованими, їх можна ефективно пом’якшити правильним налаштуванням прав доступу до бази даних. Для більшості баз потрібно налаштувати базу у режимі лише для читання. Для сервісів баз даних, таких як PostgreSQL або Azure SQL, додаток має отримати роль лише для читання (SELECT).
Запуск додатка в захищеному середовищі додатково посилює захист. У корпоративних сценаріях дані зазвичай витягуються та трансформуються з операційних систем у базу даних або сховище даних лише для читання з дружньою до користувача схемою. Такий підхід забезпечує безпеку даних, оптимізацію продуктивності та доступності, а також обмежений, лише для читання, доступ додатка.

## Зразки коду

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Є ще питання про шаблони дизайну інструментів?

Приєднуйтесь до [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), щоб зустрітися з іншими учнями, відвідати години консультацій і отримати відповіді на питання щодо AI-агентів.

## Додаткові ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Майстерня з Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Майстерня Contoso Creative Writer з багатьма агентами</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Посібник із виклику функцій Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Інтерпретатор коду Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Інструменти Autogen</a>

## Попередній урок

[Розуміння агентних шаблонів дизайну](../03-agentic-design-patterns/README.md)

## Наступний урок

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу штучного інтелекту [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ його рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння чи неправильне тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->