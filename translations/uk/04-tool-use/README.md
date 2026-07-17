[![Як розробити хороших AI агентів](../../../translated_images/uk/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Шаблон дизайну використання інструментів

Інструменти цікаві тим, що вони дозволяють AI агентам мати ширший спектр можливостей. Замість того, щоб агент мав обмежений набір дій, які він може виконувати, додавання інструменту дає агенту можливість виконувати широкий спектр дій. У цій главі ми розглянемо шаблон дизайну використання інструментів, який описує, як AI агенти можуть використовувати конкретні інструменти для досягнення своїх цілей.

## Вступ

У цьому уроці ми прагнемо відповісти на такі питання:

- Що таке шаблон дизайну використання інструментів?
- Для яких випадків застосування він підходить?
- Які елементи/будівельні блоки потрібні для реалізації шаблону дизайну?
- Які особливі аспекти слід враховувати під час використання шаблону дизайну використання інструментів для створення надійних AI агентів?

## Цілі навчання

Після завершення цього уроку ви зможете:

- Визначити шаблон дизайну використання інструментів та його мету.
- Виявити випадки використання, де застосовується цей шаблон.
- Розуміти ключові елементи, необхідні для реалізації шаблону.
- Визначати аспекти, що забезпечують довіру до AI агентів, які використовують цей шаблон.

## Що таке шаблон дизайну використання інструментів?

**Шаблон дизайну використання інструментів** фокусується на наданні LLM можливості взаємодіяти із зовнішніми інструментами для досягнення конкретних цілей. Інструменти — це код, який може виконувати агент для здійснення дій. Інструментом може бути проста функція, наприклад калькулятор, або виклик API сторонньої служби, як-от запит ціни акцій чи прогноз погоди. В контексті AI агентів інструменти розробляються для виконання агентами у відповідь на **генеровані моделлю виклики функцій**.

## Для яких випадків застосування це підходить?

AI агенти можуть використовувати інструменти для виконання складних завдань, отримання інформації або прийняття рішень. Шаблон використання інструментів часто застосовується у сценаріях, де потрібна динамічна взаємодія із зовнішніми системами, такими як бази даних, веб-сервіси або інтерпретатори коду. Ця здатність корисна для різних випадків, зокрема:

- **Динамічне отримання інформації:** агенти можуть звертатися до зовнішніх API або баз даних для отримання актуальних даних (наприклад, запити до бази даних SQLite для аналізу даних, отримання цін акцій чи інформації про погоду).
- **Виконання та інтерпретація коду:** агенти можуть виконувати код або скрипти для розв’язання математичних задач, генерації звітів або проведення симуляцій.
- **Автоматизація робочих процесів:** автоматизація повторюваних або багатокрокових робочих процесів через інтеграцію інструментів, таких як планувальники завдань, поштові служби або канали обробки даних.
- **Підтримка клієнтів:** агенти можуть взаємодіяти з CRM-системами, платформами обробки звернень або базами знань для вирішення запитів користувачів.
- **Генерація та редагування контенту:** агенти можуть використовувати інструменти, такі як перевірка граматики, підсумовування текстів, або оцінка безпеки контенту для допомоги у створенні матеріалів.

## Які елементи/будівельні блоки потрібні для реалізації шаблону використання інструментів?

Ці будівельні блоки дозволяють AI агенту виконувати широкий спектр завдань. Розглянемо ключові елементи, необхідні для реалізації шаблону дизайну використання інструментів:

- **Схеми функцій/інструментів**: детальні описи доступних інструментів, включно з іменем функції, призначенням, необхідними параметрами та очікуваними результатами. Ці схеми дають змогу LLM розуміти, які інструменти доступні та як формувати правильні запити.

- **Логіка виконання функцій:** керує тим, як і коли викликаються інструменти на основі намірів користувача та контексту розмови. Це може включати модулі планування, маршрутизації або умовні потоки, які визначають динамічне використання інструментів.

- **Система обробки повідомлень:** компоненти, які керують потоком діалогу між вхідними повідомленнями користувача, відповідями LLM, викликами інструментів та їхніми результатами.

- **Інфраструктура інтеграції інструментів:** структура, що підключає агента до різних інструментів — чи то прості функції, чи складні зовнішні сервіси.

- **Обробка помилок та валідація:** механізми обробки збоїв виконання інструментів, валідації параметрів та управління несподіваними відповідями.

- **Управління станом:** відстежує контекст розмови, попередні взаємодії з інструментами та постійні дані для забезпечення послідовності у багатокрокових діалогах.

Далі розглянемо детальніше виклик функції/інструменту.
 
### Виклик функції/інструменту

Виклик функції — це основний спосіб, яким ми дозволяємо великим мовним моделям (LLM) взаємодіяти з інструментами. Ви часто побачите, що «Функція» і «Інструмент» використовуються як синоніми, бо «функції» (блоки багаторазового коду) є «інструментами», які агенти використовують для виконання завдань. Щоб викликати код функції, LLM має порівняти запит користувача з описом функції. Для цього LLM надсилається схема з описами всіх доступних функцій. LLM потім вибирає найвідповіднішу функцію для завдання й повертає її ім’я та аргументи. Обрана функція виконується, а її відповідь надсилається назад до LLM, який надає відповідь користувачу.

Розробникам для реалізації виклику функцій для агентів потрібні:

1. Модель LLM, що підтримує виклик функцій
2. Схема з описами функцій
3. Код для кожної описаної функції

Наведемо приклад отримання поточного часу в місті:

1. **Ініціалізувати LLM, що підтримує виклик функцій:**

    Не всі моделі підтримують виклик функцій, тому важливо перевірити цю можливість для вашої LLM. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> підтримує виклик функцій. Почнемо з ініціалізації клієнта OpenAI через Azure OpenAI **Responses API** (стабільний `/openai/v1/` endpoint — `api_version` не потрібен). 

    ```python
    # Ініціалізуйте клієнта OpenAI для Azure OpenAI (API Відповідей, кінцева точка v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Створити схему функції:**

    Далі визначимо JSON схему, що містить ім’я функції, опис її призначення, а також імена та описи параметрів функції.
    Потім цю схему передамо клієнту разом із запитом користувача на отримання часу в Сан-Франциско. Важливо відзначити, що **виклик інструменту** є тим, що повертається, а не кінцевою відповіддю на запит. Як уже згадувалося, LLM повертає ім’я вибраної функції для завдання і аргументи, які будуть передані їй.

    ```python
    # Опис функції для моделі для читання (плоский формат інструменту Responses API)
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
  
    # Початкове повідомлення користувача
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Перший виклик API: Попросіть модель використати функцію
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # API відповідей повертає виклики інструментів як елементи function_call у response.output.
    # Додайте їх до розмови, щоб модель мала повний контекст для наступного кроку.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Код функції для виконання завдання:**

    Після того, як LLM обрав, яку функцію потрібно викликати, код, що виконує завдання, має бути реалізований і виконаний.
    Ми реалізуємо код для отримання поточного часу на Python. Також потрібно написати код для вилучення імені та аргументів із response_message, щоб отримати кінцевий результат.

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
    # Обробка викликів функції
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Повернути результат інструменту як елемент function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Другий виклик API: Отримати остаточну відповідь від моделі
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

Виклик функцій лежить в основі більшості, якщо не всіх, реалізацій шаблону використання інструментів агентами, проте його реалізація з нуля іноді може бути складною.
Як ми дізналися у [Уроці 2](../../../02-explore-agentic-frameworks), агентні фреймворки надають готові будівельні блоки для реалізації використання інструментів.
 
## Приклади використання інструментів з агентними фреймворками

Ось кілька прикладів, як можна реалізувати шаблон використання інструментів за допомогою різних агентних фреймворків:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> — це відкритий AI фреймворк для створення AI агентів. Він спрощує процес виклику функцій, дозволяючи визначати інструменти як функції Python з декоратором `@tool`. Фреймворк управляє передачею повідомлень між моделлю та вашим кодом. Також він надає доступ до попередньо створених інструментів, таких як Пошук Файлів та Інтерпретатор Коду через `FoundryChatClient`.

Наступна діаграма ілюструє процес виклику функцій з Microsoft Agent Framework:

![function calling](../../../translated_images/uk/functioncalling-diagram.a84006fc287f6014.webp)

У Microsoft Agent Framework інструменти визначаються як функції з декоратором. Ми можемо перетворити функцію `get_current_time`, яку бачили раніше, в інструмент за допомогою декоратора `@tool`. Фреймворк автоматично серіалізує функцію та її параметри, створюючи схему для відправки в LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Створити клієнта
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Створити агента та запустити з інструментом
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> — це більш новий агентній фреймворк, розроблений для того, щоб допомогти розробникам безпечно створювати, розгортати та масштабувати високоякісних і розширюваних AI агентів без необхідності керувати обчислювальними та сховищними ресурсами. Він особливо корисний для корпоративних застосунків, оскільки є повністю керованим сервісом з корпоративною степенню безпеки.

У порівнянні з розробкою через LLM API безпосередньо, Microsoft Foundry Agent Service має кілька переваг, зокрема:

- Автоматичний виклик інструментів — немає потреби самостійно розбирати виклики інструментів, викликати їх та обробляти відповіді; все це виконується на сервері
- Безпечно керовані дані — замість керування власним станом розмови можна покладатися на «threads», які зберігають усю необхідну інформацію
- Інструменти із коробки — інструменти для взаємодії з джерелами даних, такі як Bing, Azure AI Search, та Azure Functions.

Інструменти, доступні в Microsoft Foundry Agent Service, можна поділити на дві категорії:

1. Інструменти знань:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Пошук на основі Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Пошук файлів</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Інструменти дій:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Виклик функцій</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Інтерпретатор коду</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Інструменти на основі OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service дозволяє використовувати ці інструменти разом як `toolset`. Він також використовує `threads`, які відстежують історію повідомлень окремої розмови.

Уявіть, що ви агент з продажу в компанії Contoso. Ви хочете розробити розмовного агента, який може відповідати на запитання про ваші дані продажів.

Наступне зображення ілюструє, як можна використати Microsoft Foundry Agent Service для аналізу даних про продажі:

![Agentic Service In Action](../../../translated_images/uk/agent-service-in-action.34fb465c9a84659e.webp)

Щоб використовувати будь-які з цих інструментів із сервісом, ми можемо створити клієнта і визначити інструмент або комплект інструментів. Для практичної реалізації можна скористатися наведеним кодом Python. LLM зможе переглянути цей комплект та вирішити, чи використовувати користувацьку функцію `fetch_sales_data_using_sqlite_query`, чи попередньо побудований Інтерпретатор Коду залежно від запиту користувача.

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

# Ініціалізація набору інструментів
toolset = ToolSet()

# Ініціалізація агента виклику функцій з функцією fetch_sales_data_using_sqlite_query та додаванням її до набору інструментів
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Ініціалізація інструменту Code Interpreter та додавання його до набору інструментів.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Особливі аспекти використання шаблону дизайну інструментів для створення надійних AI агентів

Поширена проблема з динамічно згенерованим SQL від LLM — безпека, особливо ризик SQL-ін’єкцій або шкідливих дій, таких як видалення чи зміни бази даних. Хоча ці проблеми справедливі, їх ефективно можна уникнути правильно налаштувавши права доступу до бази даних. Для більшості баз даних це означає налаштування бази у режимі лише для читання. Для таких сервісів, як PostgreSQL або Azure SQL, додатку призначають роль лише для читання (SELECT).

Запуск програми в захищеному середовищі додатково підвищує рівень захисту. У корпоративних сценаріях дані зазвичай екстрагуються та трансформуються з операційних систем у базу даних або сховище з доступом лише для читання та зручною схемою. Такий підхід забезпечує безпеку даних, оптимізацію продуктивності та доступність, а також обмежений доступ додатку лише для читання.

## Приклади коду

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Є додаткові питання щодо шаблону використання інструментів?

Приєднуйтесь до [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), щоб зустрітися з іншими учнями, відвідати годину запитань і відповідей і отримати відповіді на питання про AI агентів.

## Додаткові ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Практична робота з Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Мультиагентський майстер-клас Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Огляд Microsoft Agent Framework</a>


## Попереднє тестування цього агента (необов’язково)

Після того, як ви навчитеся розгортати агентів у [Уроці 16](../16-deploying-scalable-agents/README.md), ви можете здійснити швидке тестування `TravelToolAgent` із цього уроку (чи він досі викликає свої інструменти та відповідає?) за допомогою [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Дивіться [`tests/README.md`](../tests/README.md) про те, як це запустити.

## Попередній урок

[Розуміння агентських шаблонів проектування](../03-agentic-design-patterns/README.md)

## Наступний урок

[Агентський RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->