[![Як проектувати хороших AI агентів](../../../translated_images/uk/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Патерн проектування використання інструментів

Інструменти цікаві тим, що вони дозволяють AI агентам мати ширший спектр можливостей. Замість того, щоб агент мав обмежений набір дій, які він може виконувати, додавання інструменту дозволяє агенту виконувати широкий спектр дій. У цьому розділі ми розглянемо патерн проектування використання інструментів, який описує, як AI агенти можуть використовувати конкретні інструменти для досягнення своїх цілей.

## Вступ

У цьому уроці ми прагнемо відповісти на наступні питання:

- Що таке патерн проектування використання інструментів?
- До яких випадків застосування його можна застосувати?
- Які елементи/будівельні блоки потрібні для впровадження цього патерну?
- Які особливі міркування потрібно враховувати при використанні патерну проектування використання інструментів для побудови надійних AI агентів?

## Цілі навчання

Після проходження цього уроку ви зможете:

- Визначити патерн проектування використання інструментів та його призначення.
- Визначити випадки використання, де патерн проектування використання інструментів застосовний.
- Зрозуміти ключові елементи, необхідні для впровадження патерну.
- Визнавати міркування для забезпечення надійності AI агентів, які використовують цей патерн.

## Що таке патерн проектування використання інструментів?

**Патерн проектування використання інструментів** зосереджений на тому, щоб надати великим мовним моделям (LLM) можливість взаємодіяти з зовнішніми інструментами для досягнення конкретних цілей. Інструменти — це код, який агент може виконувати для здійснення дій. Інструментом може бути проста функція, наприклад калькулятор, або виклик API до стороннього сервісу, наприклад, для пошуку цін на акції чи прогнозу погоди. В контексті AI агентів, інструменти створені для виконання агентами у відповідь на **виклики функцій, згенеровані моделлю**.

## До яких випадків застосування його можна застосувати?

AI агенти можуть використовувати інструменти для виконання складних завдань, отримання інформації або прийняття рішень. Патерн проектування використання інструментів часто застосовується в ситуаціях, що вимагають динамічної взаємодії із зовнішніми системами, такими як бази даних, веб-сервіси або інтерпретатори коду. Ця здатність корисна для різноманітних випадків використання, зокрема:

- **Динамічне отримання інформації:** Агенти можуть запитувати зовнішні API або бази даних для отримання актуальних даних (наприклад, запит до SQLite бази даних для аналізу даних, отримання цін на акції або інформації про погоду).
- **Виконання та інтерпретація коду:** Агенти можуть виконувати код або скрипти для розв’язання математичних задач, генерації звітів або проведення симуляцій.
- **Автоматизація робочих процесів:** Автоматизація рутинних або багатокрокових процесів шляхом інтеграції інструментів, таких як планувальники завдань, поштові сервіси або канали обробки даних.
- **Підтримка клієнтів:** Агенти можуть взаємодіяти із CRM системами, платформами обробки заявок або базами знань для вирішення запитів користувачів.
- **Генерація та редагування контенту:** Агенти можуть використовувати інструменти, такі як перевірка граматики, резюмувачі тексту чи оцінювачі безпеки контенту, які допомагають у створенні матеріалів.

## Які елементи/будівельні блоки потрібні для впровадження патерну проектування використання інструментів?

Ці будівельні блоки дозволяють AI агенту виконувати широкий спектр завдань. Розглянемо ключові елементи, необхідні для впровадження патерну проектування використання інструментів:

- **Схеми функцій/інструментів**: Детальні визначення доступних інструментів, включно з назвою функції, призначенням, необхідними параметрами та очікуваними результатами. Ці схеми дають змогу LLM зрозуміти, які інструменти доступні і як формувати коректні запити.

- **Логіка виконання функцій**: Визначає, як і коли викликати інструменти на основі наміру користувача та контексту розмови. Може містити модулі планування, маршрутизації або умовні потоки, які динамічно визначають використання інструментів.

- **Система обробки повідомлень**: Компоненти, що керують потоком розмови між вводом користувача, відповідями LLM, викликами інструментів і їхніми результатами.

- **Фреймворк інтеграції інструментів**: Інфраструктура, що з’єднує агента з різними інструментами — від простих функцій до складних зовнішніх сервісів.

- **Обробка помилок та валідація**: Механізми для опрацювання збоїв у виконанні інструментів, перевірки параметрів і управління неочікуваними відповідями.

- **Управління станом**: Відстеження контексту розмови, попередніх взаємодій з інструментами та збережених даних для забезпечення послідовності в багатокрокових взаємодіях.

Далі розглянемо виклик функцій/інструментів більш детально.

### Виклик функцій/інструментів

Виклик функцій — це основний спосіб, яким ми дозволяємо великим мовним моделям (LLM) взаємодіяти з інструментами. Часто слова «функція» і «інструмент» використовуються як синоніми, оскільки «функції» (блоки багаторазового коду) є «інструментами», які агенти використовують для виконання завдань. Щоб викликати код функції, LLM має порівняти запит користувача із описом функцій. Для цього в LLM надсилається схема, що містить описи всіх доступних функцій. LLM потім обирає найбільш відповідну функцію для завдання і повертає її ім’я та аргументи. Вибрана функція виконується, її відповідь надсилається назад до LLM, який використовує цю інформацію, щоб відповісти на запит користувача.

Для розробників, які хочуть реалізувати виклик функцій для агентів, знадобиться:

1. LLM модель, яка підтримує виклик функцій
2. Схема, що містить описи функцій
3. Код для кожної описаної функції

Розглянемо приклад отримання поточного часу в місті:

1. **Ініціалізувати LLM, що підтримує виклик функцій:**

    Не всі моделі підтримують виклик функцій, тому важливо перевірити, чи підтримує це ваша модель. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> підтримує виклик функцій. Ми можемо почати з ініціалізації клієнта Azure OpenAI. 

    ```python
    # Ініціалізуйте клієнта Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Створити схему функції:**

    Далі визначимо JSON-схему, яка міститиме назву функції, опис того, що вона робить, а також назви і описи параметрів функції.
    Потім передамо цю схему клієнту, створеному раніше, разом із запитом користувача, щоб дізнатися час у Сан-Франциско. Важливо зауважити, що **виклик інструменту** повертається, **а не** остаточна відповідь на запит. Як було згадано раніше, LLM повертає ім’я обраної для завдання функції і аргументи, які будуть їй передані.

    ```python
    # Опис функції для моделі для прочитання
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
  
    # Перший виклик API: Запитайте модель використати функцію
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

    Тепер, коли LLM вибрав, яку функцію потрібно виконати, треба реалізувати і виконати код, який виконує завдання.
    Ми можемо реалізувати код для отримання поточного часу на Python. Також потрібно написати код для вилучення імені та аргументів із response_message, щоб отримати остаточний результат.

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
     # Обробити виклики функцій
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

Виклик функцій є основою більшості, якщо не всіх дизайнів використання інструментів агентів, проте впроваджувати його з нуля іноді буває складно.
Як ми дізналися в [Уроці 2](../../../02-explore-agentic-frameworks), агентні фреймворки надають нам готові будівельні блоки для реалізації використання інструментів.
 
## Приклади використання інструментів з агентними фреймворками

Ось кілька прикладів того, як можна впровадити патерн використання інструментів за допомогою різних агентних фреймворків:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> — це відкритий AI фреймворк для створення AI агентів. Він спрощує процес використання виклику функцій, дозволяючи визначати інструменти як Python-функції за допомогою декоратора `@tool`. Фреймворк обробляє двонаправлену комунікацію між моделлю і вашим кодом. Також він надає доступ до готових інструментів, таких як пошук файлів і інтерпретатор коду через `AzureAIProjectAgentProvider`.

Наступна діаграма ілюструє процес виклику функцій у Microsoft Agent Framework:

![function calling](../../../translated_images/uk/functioncalling-diagram.a84006fc287f6014.webp)

У Microsoft Agent Framework інструменти визначаються як функції з декоратором. Ми можемо перетворити функцію `get_current_time`, яку розглядали раніше, в інструмент, використавши декоратор `@tool`. Фреймворк автоматично серіалізує функцію та її параметри, створюючи схему для передачі LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Створіть клієнта
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Створіть агента та запустіть за допомогою інструменту
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> — це новіший агентний фреймворк, створений для того, щоб надати розробникам можливість безпечно будувати, розгортати і масштабувати високоякісних, розширюваних AI агентів без необхідності керувати обчислювальними та сховищними ресурсами. Він особливо корисний для корпоративних додатків, оскільки є повністю керованим сервісом із корпоративним рівнем безпеки.

Порівняно із розробкою безпосередньо через API LLM, Azure AI Agent Service надає такі переваги:

- Автоматичний виклик інструментів – немає потреби парсити виклик інструменту, запускати його та обробляти відповідь; все це тепер відбувається на сервері
- Безпечно керовані дані – замість управління власним станом розмови можна покладатися на потокові нитки (threads), що зберігають всю необхідну інформацію
- Готові інструменти – інструменти для взаємодії з джерелами даних, такими як Bing, Azure AI Search та Azure Functions.

Інструменти, доступні в Azure AI Agent Service, можна поділити на дві категорії:

1. Інструменти знань:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Земельна основа з Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Пошук файлів</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Інструменти дій:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Виклик функцій</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Інтерпретатор коду</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Інструменти, визначені через OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service дає змогу використовувати ці інструменти разом як `toolset`. Він також використовує `threads`, які відстежують історію повідомлень конкретної розмови.

Уявіть, що ви агент з продажу в компанії Contoso. Ви хочете розробити розмовного агента, який може відповідати на питання щодо ваших даних про продажі.

Наступне зображення ілюструє, як можна використати Azure AI Agent Service для аналізу ваших продажів:

![Agentic Service In Action](../../../translated_images/uk/agent-service-in-action.34fb465c9a84659e.webp)

Щоб використовувати будь-який із цих інструментів за допомогою сервісу, ми можемо створити клієнта і визначити інструмент або набір інструментів. Для практичної реалізації можна використати наступний Python код. LLM зможе подивитися на набір інструментів і вирішити, чи використовувати функцію користувача `fetch_sales_data_using_sqlite_query`, чи вбудований інтерпретатор коду в залежності від запиту користувача.

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

# Ініціалізувати агента виклику функції з функцією fetch_sales_data_using_sqlite_query та додати її до набору інструментів
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Ініціалізувати інструмент інтерпретатора коду та додати його до набору інструментів.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Які особливі міркування потрібно враховувати при використанні патерну проектування використання інструментів для побудови надійних AI агентів?

Поширена проблема з SQL, динамічно згенерованим LLM, — це безпека, особливо ризик ін’єкції SQL або шкідливих дій, таких як видалення чи пошкодження бази даних. Хоча ці занепокоєння є виправданими, їх можна ефективно пом’якшити, правильно налаштувавши права доступу до бази даних. Для більшості баз даних це означає налаштування бази як тільки для читання. Для сервісів баз даних, таких як PostgreSQL або Azure SQL, додатку слід присвоїти роль лише для читання (SELECT).

Запуск додатку у безпечному середовищі додатково підвищує захист. У корпоративних сценаріях дані зазвичай експортуються та трансформуються з операційних систем у базу даних тільки для читання або сховище даних з зручною схемою. Такий підхід забезпечує безпеку даних, оптимізує продуктивність і доступність, а також гарантує, що додаток має обмежений доступ лише для читання.

## Приклади коду

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Маєте більше запитань про патерн використання інструментів?

Приєднуйтесь до [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), щоб зустрічатися з іншими учнями, брати участь у office hours і отримувати відповіді на ваші запитання щодо AI агентів.

## Додаткові ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Майстер-клас Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Майстер-клас мультиагентної системи Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Огляд Microsoft Agent Framework</a>

## Попередній урок

[Розуміння агентних патернів проектування](../03-agentic-design-patterns/README.md)

## Наступний урок
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->