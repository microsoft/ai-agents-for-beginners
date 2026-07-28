[![Як створити хороших AI агентів](../../../translated_images/uk/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Шаблон використання інструментів

Інструменти цікаві тим, що вони дозволяють AI агентам мати ширший спектр можливостей. Замість того, щоб агент мав обмежений набір дій, які він може виконувати, додаючи інструмент, агент тепер може виконувати широкий спектр дій. У цій главі ми розглянемо шаблон використання інструментів, який описує, як AI агенти можуть використовувати конкретні інструменти для досягнення своїх цілей.

## Вступ

У цьому уроці ми прагнемо відповісти на наступні питання:

- Що таке шаблон використання інструментів?
- Для яких випадків його можна застосовувати?
- Які елементи/будівельні блоки потрібні для реалізації цього шаблону?
- Які особливі міркування необхідні для використання шаблону використання інструментів для створення надійних AI агентів?

## Цілі навчання

Після завершення цього уроку ви зможете:

- Визначити шаблон використання інструментів та його призначення.
- Виявити випадки використання, де застосовується цей шаблон.
- Розуміти ключові елементи, необхідні для впровадження шаблону.
- Визначати міркування для забезпечення надійності AI агентів, що використовують цей шаблон.

## Що таке шаблон використання інструментів?

**Шаблон використання інструментів** зосереджується на наданні LLM можливості взаємодіяти з зовнішніми інструментами для досягнення конкретних цілей. Інструменти — це код, який агент може виконувати для виконання дій. Інструментом може бути проста функція, наприклад калькулятор, або виклик API до стороннього сервісу, такого як перевірка ціни акцій або прогноз погоди. У контексті AI агентів інструменти розроблені для виконання агентами у відповідь на **функціональні виклики, створені моделлю**.

## Для яких випадків можна застосовувати цей шаблон?

AI агенти можуть використовувати інструменти для виконання складних завдань, отримання інформації або прийняття рішень. Шаблон використання інструментів часто застосовується в сценаріях, що вимагають динамічної взаємодії із зовнішніми системами, такими як бази даних, веб-сервіси або інтерпретатори коду. Ця можливість корисна для ряду випадків, зокрема:

- **Динамічне отримання інформації:** Агенти можуть запитувати зовнішні API або бази даних для отримання актуальних даних (наприклад, запити до SQLite-бази для аналізу даних, отримання цін на акції чи інформації про погоду).
- **Виконання та інтерпретація коду:** Агенти можуть запускати код або скрипти для розв’язання математичних завдань, генерування звітів або проведення симуляцій.
- **Автоматизація робочих процесів:** Автоматизація повторюваних або багатокрокових процесів шляхом інтеграції інструментів, таких як планувальники завдань, поштові служби або конвеєри даних.
- **Підтримка клієнтів:** Агенти можуть взаємодіяти з CRM-системами, платформами обробки запитів або базами знань для розв’язання питань користувачів.
- **Генерація та редагування контенту:** Агенти можуть використовувати інструменти, такі як перевірка граматики, підсумовувачі тексту або оцінювачі безпеки контенту для допомоги у створенні контенту.

## Які елементи/будівельні блоки потрібні для реалізації шаблону використання інструментів?

Ці будівельні блоки дозволяють AI агенту виконувати широкий спектр завдань. Розглянемо ключові елементи, необхідні для реалізації шаблону використання інструментів:

- **Схеми функцій/інструментів**: Докладні визначення доступних інструментів, включаючи назву функції, призначення, необхідні параметри та очікувані вихідні дані. Ці схеми дозволяють LLM розуміти, які інструменти доступні та як формувати дійсні запити.

- **Логіка виконання функцій:** Регламентує, як і коли інструменти викликаються на основі наміру користувача та контексту розмови. Це може включати модулі планування, маршрутизації або умовні потоки, які визначають динамічне використання інструментів.

- **Система обробки повідомлень:** Компоненти, що керують ходом розмови між ввідними даними користувача, відповідями LLM, викликами інструментів та їхніми результатами.

- **Інфраструктура інтеграції інструментів:** Інфраструктура, що з'єднує агента з різноманітними інструментами, будь то прості функції або складні зовнішні сервіси.

- **Обробка помилок і валідація:** Механізми для обробки збоїв виконання інструментів, перевірки параметрів та управління непередбаченими відповідями.

- **Керування станом:** Відстежує контекст розмови, попередні взаємодії з інструментами та постійні дані, щоб забезпечити послідовність у багаторазових взаємодіях.

Тепер розглянемо детальніше функціональні виклики (Function/Tool Calling).
 
### Функціональні виклики / виклики інструментів

Виклики функцій — це основний спосіб, яким ми даємо змогу великим мовним моделям (LLM) взаємодіяти з інструментами. Часто ви бачите, як «Функція» та «Інструмент» використовуються як синоніми, оскільки "функції" (блоки повторно використовуваного коду) є "інструментами", які агенти використовують для виконання завдань. Щоб код функції був викликаний, LLM має порівняти запит користувача з описом функції. Для цього LLM надсилають схему, що містить описи всіх доступних функцій. Потім LLM обирає найбільш відповідну функцію для завдання та повертає її ім'я й аргументи. Вибрана функція виконується, її відповідь надсилається назад LLM, який використовує цю інформацію для відповіді на запит користувача.

Для розробників, щоб реалізувати виклики функцій для агентів, необхідно:

1. Модель LLM, що підтримує виклики функцій
2. Схема, що містить описи функцій
3. Код для кожної описаної функції

Розглянемо приклад отримання поточного часу в місті для ілюстрації:

1. **Ініціалізувати LLM, що підтримує виклики функцій:**

    Не всі моделі підтримують виклики функцій, тому важливо перевірити, чи модель, яку ви використовуєте, це робить. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> підтримує виклики функцій. Ми можемо почати з ініціалізації клієнта OpenAI для Azure OpenAI **Responses API** (стабільна точка доступу `/openai/v1/` — не потрібен параметр `api_version`). 

    ```python
    # Ініціалізувати клієнт OpenAI для Azure OpenAI (API відповідей, кінцева точка v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Створити схему функції**:

    Далі ми визначимо схему JSON, що містить ім'я функції, опис її дії та назви і описи параметрів функції.
    Потім передамо цю схему клієнту, створеному раніше разом із запитом користувача, щоб знайти час у Сан-Франциско. Важливо відзначити, що повертається **виклик інструменту**, а не кінцева відповідь на запитання. Як зазначалося раніше, LLM повертає ім'я функції, яку він обрав для завдання, та аргументи, які будуть передані функції.

    ```python
    # Опис функції для читання моделі (формат інструменту Responses API flat)
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

    # Перший виклик API: Запросити модель використовувати функцію
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
  
1. **Код функції, необхідний для виконання завдання:**

    Після того як LLM вибрав, яку функцію потрібно запустити, потрібно реалізувати та виконати код, що виконує завдання.
    Ми можемо реалізувати код для отримання поточного часу на Python. Також потрібно написати код для вилучення імені та аргументів із response_message, щоб отримати кінцевий результат.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Повернути результат інструмента як елемент function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Другий виклик API: отримати остаточну відповідь від моделі
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

Виклики функцій є основою більшості, якщо не всіх, дизайнів використання інструментів агентами; однак реалізувати це з нуля іноді може бути складно.
Як ми дізнались у [Уроці 2](../../../02-explore-agentic-frameworks), агентські фреймворки надають попередньо побудовані будівельні блоки для реалізації використання інструментів.
 
## Приклади використання інструментів з агентськими фреймворками

Ось кілька прикладів, як ви можете реалізувати шаблон використання інструментів за допомогою різних агентських фреймворків:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> — це відкритий AI-фреймворк для створення AI агентів. Він спрощує процес використання викликів функцій, дозволяючи визначати інструменти як функції Python із декоратором `@tool`. Фреймворк керує обміном повідомленнями між моделлю та вашим кодом. Також надається доступ до попередньо створених інструментів, як пошук файлів і інтерпретатор коду через `FoundryChatClient`.

Наступна діаграма ілюструє процес виклику функцій з Microsoft Agent Framework:

![виклик функцій](../../../translated_images/uk/functioncalling-diagram.a84006fc287f6014.webp)

У Microsoft Agent Framework інструменти визначаються як декоровані функції. Ми можемо перетворити функцію `get_current_time`, яку бачили раніше, в інструмент, використовуючи декоратор `@tool`. Фреймворк автоматично серіалізує функцію та її параметри, створюючи схему для надсилання LLM.

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

# Створити агента і запустити з інструментом
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> — це новіший агентський фреймворк, створений для того, щоб допомагати розробникам безпечно створювати, розгортати та масштабувати високоякісних і розширюваних AI агентів без необхідності керувати обчислювальними та сховищними ресурсами. Особливо корисний для корпоративних застосунків, оскільки це повністю керована служба з корпоративним рівнем безпеки.

Порівняно з розробкою безпосередньо через API LLM, Microsoft Foundry Agent Service має деякі переваги, зокрема:

- Автоматичний виклик інструментів — немає потреби парсити виклики інструментів, викликати їх і обробляти відповіді; усе це тепер виконується на стороні сервера.
- Безпечно керовані дані — замість управління власним станом розмови можна покладатися на threads, які зберігають всю необхідну інформацію.
- Інструменти «з коробки» — інструменти для взаємодії з джерелами даних, такими як Bing, Azure AI Search та Azure Functions.

Інструменти, доступні в Microsoft Foundry Agent Service, можна поділити на дві категорії:

1. Інструменти знань:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Підґрунтя з Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Пошук файлів</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Інструменти дії:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Виклик функцій</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Інтерпретатор коду</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Інструменти, визначені OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service дозволяє нам використовувати ці інструменти разом як `комплект інструментів`. Він також використовує `threads`, які відстежують історію повідомлень конкретної розмови.

Уявіть, що ви торговий агент у компанії Contoso. Ви хочете створити розмовного агента, який може відповідати на питання щодо ваших даних продажів.

Наступне зображення ілюструє, як можна використати Microsoft Foundry Agent Service для аналізу даних продажів:

![Agentic Service в дії](../../../translated_images/uk/agent-service-in-action.34fb465c9a84659e.webp)

Щоб використовувати будь-які з цих інструментів зі службою, ми можемо створити клієнта та визначити інструмент або комплект інструментів. Для практичної реалізації можна використати наступний код на Python. LLM зможе розглянути комплект інструментів і вирішити, чи використовувати функцію, створену користувачем, `fetch_sales_data_using_sqlite_query`, або вбудований Інтерпретатор коду залежно від запиту користувача.

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

# Ініціалізувати інструмент Code Interpreter та додати його до набору інструментів.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Які особливі міркування при використанні шаблону використання інструментів для створення надійних AI агентів?

Загальною турботою при динамічно створеному SQL від LLM є безпека, особливо ризик SQL-ін’єкції або зловмисних дій, таких як видалення або пошкодження бази даних. Хоча ці занепокоєння є обґрунтованими, їх можна ефективно уникнути шляхом належної конфігурації прав доступу до бази даних. Для більшості баз даних це означає налаштування її в режимі лише для читання. Для баз даних, таких як PostgreSQL або Azure SQL, додатку потрібно призначити роль лише для читання (SELECT).

Запуск додатка в захищеному середовищі додатково посилює захист. У корпоративних сценаріях дані зазвичай вилучаються та трансформуються з операційних систем у базу даних або сховище лише для читання з зручною схемою. Такий підхід забезпечує безпеку даних, оптимізує продуктивність і доступність, а також гарантовано обмежує доступ додатка до режиму лише для читання.

## Приклади коду

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Є ще питання щодо шаблону використання інструментів?

Приєднуйтесь до [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), щоб познайомитися з іншими учнями, відвідати офісні години та отримати відповіді на питання щодо AI агентів.

## Додаткові ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Майстер-клас Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Майстер-клас Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Огляд Microsoft Agent Framework</a>


## Смоук-тестування цього агента (додатково)

Після того, як ви навчитеся розгортати агентів у [Уроці 16](../16-deploying-scalable-agents/README.md), ви можете провести смоук-тестування `TravelToolAgent` з цього уроку (чи він все ще викликає свої інструменти та відповідає?) за допомогою [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Дивіться [`tests/README.md`](../tests/README.md), щоб дізнатися, як його запустити.

## Попередній урок

[Розуміння агентних шаблонів проектування](../03-agentic-design-patterns/README.md)

## Наступний урок

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->