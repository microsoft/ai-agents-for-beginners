[![Дослідження фреймворків AI агентів](../../../translated_images/uk/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Огляд фреймворків AI агентів

Фреймворки AI агентів — це програмні платформи, створені для спрощення розробки, розгортання та керування AI агентами. Ці фреймворки надають розробникам готові компоненти, абстракції та інструменти, які оптимізують розробку складних AI систем.

Вони допомагають розробникам зосередитися на унікальних аспектах їхніх застосунків, надаючи стандартизовані підходи до поширених викликів у розробці AI агентів. Вони підвищують масштабованість, доступність та ефективність у створенні AI систем.

## Вступ

У цьому уроці ми розглянемо:

- Що таке фреймворки AI агентів і що вони дозволяють розробникам досягати?
- Як команди можуть швидко прототипувати, ітерувати та покращувати можливості своїх агентів?
- Які відмінності між фреймворками та інструментами, створеними Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> та <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Чи можна інтегрувати мої існуючі інструменти екосистеми Azure безпосередньо, чи потрібні автономні рішення?
- Що таке Microsoft Foundry Agent Service і як він мені допомагає?

## Мета навчання

Мета цього уроку — допомогти вам зрозуміти:

- Роль фреймворків AI агентів у розробці AI.
- Як використовувати фреймворки AI агентів для створення інтелектуальних агентів.
- Ключові можливості, які надають фреймворки AI агентів.
- Відмінності між Microsoft Agent Framework та Microsoft Foundry Agent Service.

## Що таке фреймворки AI агентів і що вони дозволяють розробникам робити?

Традиційні AI фреймворки можуть допомогти вам інтегрувати AI у ваші додатки та покращити їх такими способами:

- **Персоналізація**: AI може аналізувати поведінку користувача та його вподобання, щоб надавати персоналізовані рекомендації, контент і досвід.
Приклад: Стрімінгові сервіси, як Netflix, використовують AI, щоб пропонувати фільми та шоу на основі історії переглядів, підвищуючи залучення та задоволення користувача.
- **Автоматизація та ефективність**: AI може автоматизувати рутинні завдання, оптимізувати робочі процеси та покращувати операційну ефективність.
Приклад: Додатки служби підтримки використовують чатботів на основі AI для обробки типових запитів, скорочуючи час відповіді і звільняючи людських агентів для складніших питань.
- **Покращення користувацького досвіду**: AI може покращити загальний досвід користувача, надаючи інтелектуальні функції, такі як розпізнавання голосу, обробка природньої мови та прогнозування тексту.
Приклад: Віртуальні помічники, такі як Siri та Google Assistant, використовують AI для розуміння та реагування на голосові команди, полегшуючи користувачам взаємодію з пристроями.

### Це все звучить чудово, тож навіщо нам потрібен AI Agent Framework?

Фреймворки AI агентів — це більше, ніж просто AI фреймворки. Вони розроблені для створення інтелектуальних агентів, які можуть взаємодіяти з користувачами, іншими агентами та середовищем для досягнення конкретних цілей. Ці агенти можуть проявляти автономну поведінку, приймати рішення та адаптуватися до змінних умов. Розглянемо основні можливості, які надають фреймворки AI агентів:

- **Співпраця та координація агентів**: Забезпечують створення кількох агентів, які можуть працювати разом, спілкуватися та координуватися для розв’язання складних завдань.
- **Автоматизація та управління завданнями**: Надають механізми автоматизації багатокрокових робочих процесів, делегування завдань і динамічного управління завданнями серед агентів.
- **Контекстуальне розуміння та адаптація**: Оснащують агентів здатністю розуміти контекст, адаптуватися до змін середовища та приймати рішення на основі інформації в реальному часі.

Отже, узагальнюючи, агенти дають вам можливість робити більше, підняти автоматизацію на новий рівень, створювати більш інтелектуальні системи, які можуть адаптуватися та навчатися зі свого оточення.

## Як швидко прототипувати, ітерувати і покращувати можливості агента?

Це динамічна сфера, але існують спільні риси у більшості фреймворків AI агентів, які допомагають швидко створювати прототипи та ітерувати — модульні компоненти, спільні інструменти та навчання в реальному часі. Розглянемо їх детальніше:

- **Використовуйте модульні компоненти**: AI SDK пропонують готові компоненти, такі як AI та Memory коннектори, виклик функцій через природну мову або плагіни коду, шаблони підказок тощо.
- **Застосовуйте спільні інструменти**: Створюйте агентів із конкретними ролями та завданнями, дозволяючи тестувати і вдосконалювати спільні робочі процеси.
- **Навчайте в режимі реального часу**: Впроваджуйте петлі зворотного зв’язку, де агенти вчаться зі взаємодій і динамічно коригують свою поведінку.

### Використання модульних компонентів

SDK, як Microsoft Agent Framework, пропонують готові компоненти, наприклад AI коннектори, визначення інструментів і керування агентами.

**Як команди можуть їх використовувати**: Команди можуть швидко збирати ці компоненти, щоб створити функціональний прототип без початку "з нуля", що дозволяє швидко експериментувати та ітерувати.

**Як це працює на практиці**: Ви можете використати готовий парсер для вилучення інформації з вводу користувача, модуль пам’яті для збереження і отримання даних та генератор підказок для взаємодії з користувачами — усе це без необхідності будувати компоненти самотужки.

**Приклад коду**. Розглянемо приклад використання Microsoft Agent Framework з `FoundryChatClient`, щоб модель відповідала на ввід користувача з викликом інструментів:

``` python
# Приклад використання Microsoft Agent Framework на Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Визначте приклад функції інструменту для бронювання поїздки
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Приклад виводу: Ваш рейс до Нью-Йорка на 1 січня 2025 року успішно заброньовано. Бажаємо безпечної подорожі! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Ви бачите в цьому прикладі, як можна використати готовий парсер для вилучення ключової інформації з вводу користувача, наприклад, пункт відправлення, пункт призначення і дату бронювання рейсу. Такий модульний підхід дає змогу зосередитися на логіці високого рівня.

### Використання спільних інструментів

Фреймворки, як Microsoft Agent Framework, дозволяють створювати кілька агентів, які можуть працювати разом.

**Як команди можуть їх використовувати**: Команди можуть проектувати агентів із конкретними ролями та завданнями, що дає можливість тестувати і вдосконалювати спільні робочі процеси та підвищувати ефективність системи.

**Як це працює на практиці**: Ви можете створити команду агентів, де кожен агент спеціалізується на певній функції — наприклад, збір даних, аналіз або прийняття рішень. Ці агенти можуть спілкуватися і обмінюватися інформацією, щоб досягти спільної мети, наприклад відповісти на запит користувача або виконати завдання.

**Приклад коду (Microsoft Agent Framework)**:

```python
# Створення кількох агентів, які працюють разом, використовуючи Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Агент отримання даних
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Агент аналізу даних
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Запуск агентів послідовно для виконання завдання
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

З попереднього коду ви бачите, як створити завдання, що залучає кількох агентів для спільного аналізу даних. Кожен агент виконує певну функцію, а завдання виконується шляхом координації агентів для досягнення бажаного результату. Створюючи агентів із спеціалізованими ролями, ви можете покращити ефективність і продуктивність завдання.

### Навчання в режимі реального часу

Просунуті фреймворки забезпечують можливості розуміння контексту в реальному часі і адаптації.

**Як команди можуть їх використовувати**: Команди можуть впроваджувати петлі зворотного зв’язку, де агенти вчаться зі взаємодій і динамічно коригують свою поведінку, що призводить до безперервного покращення та вдосконалення можливостей.

**Як це працює на практиці**: Агенти можуть аналізувати відгуки користувачів, дані оточення та результати завдань для оновлення своєї бази знань, коригування алгоритмів прийняття рішень та покращення продуктивності з часом. Цей ітеративний процес навчання дозволяє агентам адаптуватися до змінних умов і вподобань користувачів, підвищуючи ефективність системи загалом.

## Які відмінності між Microsoft Agent Framework та Microsoft Foundry Agent Service?

Існує багато способів порівняти ці підходи, тому давайте розглянемо основні відмінності з точки зору дизайну, можливостей та цільових випадків використання:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework надає оптимізований SDK для створення AI агентів з використанням `FoundryChatClient`. Він дає змогу розробникам створювати агентів, які використовують моделі Azure OpenAI з вбудованим викликом інструментів, керуванням розмовами та корпоративною безпекою через Azure identity.

**Випадки використання**: Створення готових до продакшн AI агентів з використанням інструментів, багатокроковими робочими процесами та сценаріями інтеграції в корпоративні середовища.

Ось кілька важливих основних концепцій Microsoft Agent Framework:

- **Агенти**. Агент створюється через `FoundryChatClient` і налаштовується ім’ям, інструкціями та інструментами. Агент може:
  - **Обробляти повідомлення користувача** та генерувати відповіді за допомогою моделей Azure OpenAI.
  - **Автоматично викликати інструменти** залежно від контексту розмови.
  - **Підтримувати стан розмови** через кілька взаємодій.

  Ось приклад коду створення агента:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Інструменти**. Фреймворк підтримує визначення інструментів як Python функцій, які агент може викликати автоматично. Інструменти реєструються під час створення агента:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Координація кількох агентів**. Ви можете створювати кілька агентів з різною спеціалізацією та координувати їхню роботу:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Інтеграція з Azure Identity**. Фреймворк використовує `AzureCliCredential` (або `DefaultAzureCredential`) для безпечної аутентифікації без ключів, що усуває потребу управляти API ключами безпосередньо.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service — це нещодавня новинка, представлена на Microsoft Ignite 2024. Він дозволяє розробляти та розгортати AI агентів з більш гнучкими моделями, такими як прямий виклик open-source LLM, наприклад Llama 3, Mistral і Cohere.

Microsoft Foundry Agent Service забезпечує потужніші механізми корпоративної безпеки та методи зберігання даних, що робить його придатним для корпоративних додатків.

Він працює з коробки разом із Microsoft Agent Framework для створення і розгортання агентів.

Ця служба наразі перебуває в публічному огляді і підтримує Python та C# для створення агентів.

Використовуючи Python SDK Microsoft Foundry Agent Service, можна створити агента з користувацьким інструментом:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Визначити функції інструментів
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Основні концепції

Основні концепції Microsoft Foundry Agent Service:

- **Агент**. Microsoft Foundry Agent Service інтегрується з Microsoft Foundry. В Microsoft Foundry AI Агент виступає як "розумний" мікросервіс, який може відповідати на питання (RAG), виконувати дії або повністю автоматизувати робочі процеси. Це досягається поєднанням потужності генеративних AI моделей з інструментами, що дозволяють отримувати доступ та взаємодіяти з реальними джерелами даних. Ось приклад агента:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    У цьому прикладі агент створюється з моделлю `gpt-5-mini`, ім’ям `my-agent` та інструкціями `You are helpful agent`. Агент оснащений інструментами та ресурсами для виконання задач інтерпретації коду.

- **Тред та повідомлення**. Тред — це ще одна важлива концепція. Вона представляє розмову чи взаємодію між агентом і користувачем. Треди можна використовувати для відстеження прогресу розмови, збереження контекстної інформації та керування станом взаємодії. Ось приклад треда:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Попросіть агента виконати роботу над потоком
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Отримайте та зареєструйте всі повідомлення, щоб побачити відповідь агента
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    В попередньому коді створюється тред. Потім до треда надсилається повідомлення. Викликом `create_and_process_run` агент виконує роботу над тредом. Нарешті, повідомлення отримуються і логуються для перегляду відповіді агента. Повідомлення ілюструють прогрес розмови між користувачем та агентом. Важливо розуміти, що повідомлення можуть бути різних типів, наприклад текст, зображення або файл — тобто робота агента могла призвести, наприклад, до створення зображення або текстової відповіді. Як розробник, ви можете використовувати цю інформацію для подальшої обробки відповіді або її подання користувачу.

- **Інтеграція з Microsoft Agent Framework**. Microsoft Foundry Agent Service працює безперешкодно з Microsoft Agent Framework, тож можна створювати агентів за допомогою `FoundryChatClient` і розгортати їх через Agent Service для продакшн сценаріїв.

**Випадки використання**: Microsoft Foundry Agent Service призначений для корпоративних застосунків, що потребують безпечного, масштабованого та гнучкого розгортання AI агентів.

## У чому різниця між цими підходами?
 
Звучить так, ніби є певне перекриття, але є ключові відмінності в дизайні, можливостях і цільових випадках використання:
 
- **Microsoft Agent Framework (MAF)**: Продакшн-ready SDK для створення AI агентів. Надає спрощений API для створення агентів з викликом інструментів, керуванням розмовами та інтеграцією Azure identity.
- **Microsoft Foundry Agent Service**: Платформа та сервіс розгортання в Microsoft Foundry для агентів. Має вбудоване підключення до сервісів, таких як Azure OpenAI, Azure AI Search, Bing Search і виконання коду.
 
Ще не впевнені, який вибрати?

### Випадки використання
 
Давайте спробуємо допомогти, розглянувши деякі типові випадки використання:
 
> П: Я створюю продакшн AI агентів і хочу швидко почати
>

>В: Microsoft Agent Framework — відмінний вибір. Він надає простий, «пітонічний» API через `FoundryChatClient`, який дозволяє визначати агентів із інструментами та інструкціями всього у декілька рядків коду.

>П: Мені потрібне корпоративне розгортання з інтеграціями Azure, такими як Search та виконання коду
>
> В: Microsoft Foundry Agent Service найкраще підходить. Це платформа-сервіс, що надає вбудовані можливості для багатьох моделей, Azure AI Search, Bing Search та Azure Functions. Він дозволяє легко створювати агентів у порталі Foundry і розгортати їх у масштабі.
 
> П: Я все ще заплутався, просто порадь один варіант
>
> В: Починайте з Microsoft Agent Framework для створення агентів, а потім використовуйте Microsoft Foundry Agent Service, коли потрібно розгортати та масштабувати їх у продакшні. Такий підхід дозволяє швидко ітерувати вашу логіку агента, одночасно маючи чіткий шлях до корпоративного розгортання.
 
Підсумуємо ключові відмінності в таблиці:

| Фреймворк | Фокус | Основні концепції | Випадки використання |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Оптимізований SDK для агентів з викликом інструментів | Агенти, Інструменти, Azure Identity | Створення AI агентів, використання інструментів, багатокрокові робочі процеси |
| Microsoft Foundry Agent Service | Гнучкі моделі, корпоративна безпека, генерація коду, виклик інструментів | Модульність, Співпраця, Оркестрація процесів | Безпечне, масштабоване та гнучке розгортання AI агентів |

## Чи можна інтегрувати мої існуючі інструменти екосистеми Azure безпосередньо, чи потрібні автономні рішення?


Відповідь: так, ви можете інтегрувати існуючі інструменти екосистеми Azure безпосередньо з Microsoft Foundry Agent Service, особливо оскільки він створений для безшовної роботи з іншими сервісами Azure. Наприклад, ви можете інтегрувати Bing, Azure AI Search і Azure Functions. Також існує глибока інтеграція з Microsoft Foundry.

Microsoft Agent Framework також інтегрується зі службами Azure через `FoundryChatClient` і Azure identity, що дозволяє викликати сервіси Azure безпосередньо з ваших агентських інструментів.

## Приклади коду

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Бажаєте більше дізнатись про AI Agent Frameworks?

Приєднуйтесь до [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), щоб поспілкуватися з іншими учасниками, відвідати офіс-години та отримати відповіді на свої питання про AI агенти.

## Джерела

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Попередній урок

[Вступ до AI агентів та варіанти їх використання](../01-intro-to-ai-agents/README.md)

## Наступний урок

[Розуміння агентних патернів проектування](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->