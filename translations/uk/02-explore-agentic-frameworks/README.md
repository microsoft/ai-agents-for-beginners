[![Вивчення фреймворків агентів ШІ](../../../translated_images/uk/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Дослідження фреймворків агентів ШІ

Фреймворки агентів ШІ — це програмні платформи, які призначені для спрощення створення, розгортання та управління агентами ШІ. Ці фреймворки надають розробникам готові компоненти, абстракції та інструменти, які оптимізують розробку складних систем ШІ.

Вони допомагають розробникам зосередитися на унікальних аспектах своїх застосунків, забезпечуючи стандартизовані підходи до загальних викликів у розробці агентів ШІ. Вони покращують масштабованість, доступність та ефективність при створенні систем ШІ.

## Вступ

У цьому уроці буде розглянуто:

- Що таке фреймворки агентів ШІ та що вони дозволяють розробникам досягти?
- Як команди можуть використовувати їх для швидкого прототипування, ітерацій та покращення можливостей агентів?
- Які відмінності між фреймворками та інструментами, створеними Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> та <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Чи можу я інтегрувати свої існуючі інструменти екосистеми Azure безпосередньо, чи мені потрібні автономні рішення?
- Що таке Microsoft Foundry Agent Service і як це мені допомагає?

## Цілі навчання

Метою цього уроку є допомогти вам зрозуміти:

- Роль фреймворків агентів ШІ у розробці ШІ.
- Як використовувати фреймворки агентів ШІ для створення інтелектуальних агентів.
- Ключові можливості, які надають фреймворки агентів ШІ.
- Відмінності між Microsoft Agent Framework і Microsoft Foundry Agent Service.

## Що таке фреймворки агентів ШІ та що вони дозволяють розробникам робити?

Традиційні фреймворки ШІ допомагають вам інтегрувати ШІ у ваші додатки і покращувати їх наступним чином:

- **Персоналізація**: ШІ може аналізувати поведінку користувача та його вподобання, щоб надавати персоналізовані рекомендації, контент і досвід.
Приклад: Стримінгові сервіси, як Netflix, використовують ШІ для пропонування фільмів та шоу на основі історії переглядів, покращуючи залученість і задоволення користувачів.
- **Автоматизація та ефективність**: ШІ може автоматизувати повторювані завдання, оптимізувати робочі процеси та підвищувати операційну ефективність.
Приклад: Додатки служби підтримки використовують чат-ботів на базі ШІ для обробки поширених запитів, що скорочує час відповіді і звільняє людських агентів для складніших завдань.
- **Покращений користувацький досвід**: ШІ може покращити загальний досвід користувача за допомогою інтелектуальних функцій, таких як розпізнавання голосу, обробка природньої мови та передбачення тексту.
Приклад: Віртуальні помічники, як Siri і Google Assistant, використовують ШІ для розуміння та виконання голосових команд, спрощуючи взаємодію користувача з пристроями.

### Це все звучить чудово, тож навіщо нам потрібен фреймворк агентів ШІ?

Фреймворки агентів ШІ — це дещо більше, ніж просто фреймворки ШІ. Вони призначені для створення розумних агентів, які можуть взаємодіяти з користувачами, іншими агентами та навколишнім середовищем для досягнення конкретних цілей. Ці агенти можуть демонструвати автономну поведінку, приймати рішення та адаптуватися до змінних умов. Ось деякі ключові можливості, які надають фреймворки агентів ШІ:

- **Співпраця та координація агентів**: Дозволяють створювати кілька агентів ШІ, які можуть працювати разом, спілкуватися та координуватися для розв’язання складних завдань.
- **Автоматизація і управління завданнями**: Забезпечують механізми автоматизації багатокрокових робочих процесів, делегування завдань і динамічного управління завданнями між агентами.
- **Контекстне розуміння і адаптація**: Оснащують агентів здатністю розуміти контекст, адаптуватися до змін у середовищі та приймати рішення на основі інформації в реальному часі.

Отже, підсумовуючи, агенти дозволяють вам робити більше, піднести автоматизацію на новий рівень, створювати більш інтелектуальні системи, які можуть адаптуватися і вчитися з навколишнього середовища.

## Як швидко прототипувати, ітерувати та покращувати можливості агента?

Це швидкозмінна сфера, але є спільні риси для більшості фреймворків агентів ШІ, які допомагають швидко прототипувати і ітерувати — це модульні компоненти, інструменти для спільної роботи та навчання в режимі реального часу. Розглянемо їх детальніше:

- **Використовуйте модульні компоненти**: SDK ШІ пропонують готові компоненти, такі як коннектори AI і пам’яті, виклик функцій через природну мову або плагіни коду, шаблони запитів тощо.
- **Використовуйте інструменти для спільної роботи**: Розробляйте агентів із конкретними ролями та завданнями, що дозволяє тестувати і покращувати спільні робочі процеси.
- **Навчайтесь у реальному часі**: Організовуйте цикли зворотного зв’язку, де агенти навчаються на взаємодіях і динамічно коригують свою поведінку.

### Використання модульних компонентів

SDK, як Microsoft Agent Framework, пропонують готові компоненти, такі як AI-коннектори, визначення інструментів і управління агентами.

**Як команди можуть це використовувати**: Команди можуть швидко збирати ці компоненти, щоб створити функціональний прототип без початку з нуля, що дозволяє швидко експериментувати та ітерувати.

**Як це працює на практиці**: Ви можете використати готовий парсер для вилучення інформації з введення користувача, модуль пам’яті для збереження і отримання даних, генератор запитів для взаємодії з користувачами — все це без необхідності створювати ці компоненти з нуля.

**Приклад коду**. Розглянемо приклад використання Microsoft Agent Framework з `FoundryChatClient`, щоб модель відповідала на введення користувача з викликом інструментів:

``` python
# Приклад Microsoft Agent Framework на Python

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
    # Приклад виводу: Ваш рейс до Нью-Йорка на 1 січня 2025 року успішно заброньовано. Щасливої подорожі! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

З цього прикладу видно, як можна використати готовий парсер для вилучення ключової інформації з введення користувача, такої як місце відправлення, пункт призначення та дата запиту бронювання рейсу. Такий модульний підхід дозволяє зосередитися на логіці високого рівня.

### Використання інструментів для спільної роботи

Фреймворки, як Microsoft Agent Framework, полегшують створення кількох агентів, які працюють разом.

**Як команди можуть це використовувати**: Команди можуть проектувати агентів з конкретними ролями та завданнями, що дозволяє тестувати та вдосконалювати спільні робочі процеси і підвищувати загальну ефективність системи.

**Як це працює на практиці**: Ви можете створити команду агентів, де кожен виконує спеціалізовану функцію, наприклад, отримання даних, аналіз або ухвалення рішень. Ці агенти можуть спілкуватися і обмінюватися інформацією для досягнення спільної мети, наприклад, відповісти на запит користувача або завершити завдання.

**Приклад коду (Microsoft Agent Framework)**:

```python
# Створення кількох агентів, які працюють разом з використанням Microsoft Agent Framework

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

У наведеному вище коді показано, як створити завдання, що передбачає спільну роботу кількох агентів для аналізу даних. Кожен агент виконує певну функцію, і завдання виконується шляхом координації агентів для досягнення потрібного результату. Створюючи спеціалізованих агентів із певними ролями, можна підвищити ефективність і продуктивність завдань.

### Навчання у реальному часі

Сучасні фреймворки надають можливості для розуміння контексту і адаптації в реальному часі.

**Як команди можуть це використовувати**: Команди можуть впроваджувати цикли зворотного зв’язку, де агенти навчаються на основі взаємодій і динамічно коригують свою поведінку, що веде до безперервного вдосконалення та розвитку можливостей.

**Як це працює на практиці**: Агенти можуть аналізувати відгуки користувачів, дані навколишнього середовища та результати завдань, оновлювати свою базу знань, коригувати алгоритми прийняття рішень і з часом покращувати продуктивність. Цей ітеративний процес навчання дозволяє агентам адаптуватися до змінних умов і вподобань користувачів, підвищуючи загальну ефективність системи.

## Які відмінності між Microsoft Agent Framework і Microsoft Foundry Agent Service?

Існує багато способів порівняти ці підходи, але розглянемо ключові відмінності з огляду на їх дизайн, можливості та цільові випадки використання:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework надає оптимізований SDK для створення агентів ШІ за допомогою `FoundryChatClient`. Він дозволяє розробникам створювати агентів, які використовують моделі Azure OpenAI із вбудованим викликом інструментів, управлінням розмовами та безпекою корпоративного рівня через Azure ідентифікацію.

**Випадки використання**: Створення готових до виробництва агентів ШІ з використанням інструментів, багатокрокових робочих процесів і сценаріїв корпоративної інтеграції.

Ось деякі важливі основні концепції Microsoft Agent Framework:

- **Агенти**. Агент створюється через `FoundryChatClient` і налаштовується з ім’ям, інструкціями та інструментами. Агент може:
  - **Обробляти повідомлення користувача** і генерувати відповіді з використанням моделей Azure OpenAI.
  - **Автоматично викликати інструменти** відповідно до контексту розмови.
  - **Підтримувати стан розмови** під час кількох взаємодій.

  Ось фрагмент коду, що показує, як створити агента:

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

- **Інструменти**. Фреймворк підтримує визначення інструментів як функцій Python, які агент може викликати автоматично. Інструменти реєструються при створенні агента:

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

- **Координація кількох агентів**. Ви можете створювати кілька агентів з різними спеціалізаціями і координувати їхню роботу:

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

- **Інтеграція Azure Identity**. Фреймворк використовує `AzureCliCredential` (або `DefaultAzureCredential`) для безпечної автентифікації без ключів, усуваючи потребу управляти API-ключами безпосередньо.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service — це більш новий компонент, представлений на Microsoft Ignite 2024. Він дозволяє розробляти та розгортати агентів ШІ з більш гнучкими моделями, такими як прямий виклик відкритих LLM, як Llama 3, Mistral і Cohere.

Microsoft Foundry Agent Service забезпечує посилені механізми безпеки корпоративного рівня і методи зберігання даних, що робить його придатним для корпоративних застосунків.

Він працює "з коробки" разом з Microsoft Agent Framework для створення і розгортання агентів.

Ця служба наразі знаходиться в публічному прев’ю і підтримує Python і C# для створення агентів.

Використовуючи Python SDK Microsoft Foundry Agent Service, ми можемо створити агента з користувацьким інструментом:

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
        model="gpt-4.1-mini",
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

Microsoft Foundry Agent Service має такі основні концепції:

- **Агент**. Microsoft Foundry Agent Service інтегрується з Microsoft Foundry. В Microsoft Foundry агент ШІ виступає як "розумний" мікросервіс, який може відповідати на запитання (RAG), виконувати дії або повністю автоматизувати робочі процеси. Це досягається поєднанням потужності генеративних моделей ШІ з інструментами, які дозволяють отримувати доступ і взаємодіяти з реальними джерелами даних. Ось приклад агента:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    У цьому прикладі агент створений із моделлю `gpt-4.1-mini`, ім’ям `my-agent` та інструкціями `You are helpful agent`. Агент оснащений інструментами та ресурсами для виконання завдань інтерпретації коду.

- **Тред і повідомлення**. Тред — це ще одна важлива концепція. Він відображає розмову або взаємодію між агентом і користувачем. Треди можна використовувати для відстеження прогресу розмови, збереження контекстної інформації і управління станом взаємодії. Ось приклад треду:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Попросіть агента виконати роботу над потоком
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Отримайте та зафіксуйте всі повідомлення, щоб побачити відповідь агента
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    У наведеному коді створюється тред. Потім у цей тред надсилається повідомлення. Викликом `create_and_process_run` агенту доручається виконати роботу в треді. Врешті-решт повідомлення отримуються і журналюються, щоб побачити відповідь агента. Повідомлення відображають прогрес розмови між користувачем і агентом. Важливо також розуміти, що повідомлення можуть бути різних типів, як текст, зображення чи файл, тобто робота агента могла призвести, наприклад, до створення зображення або текстової відповіді. Розробник може використовувати цю інформацію для подальшої обробки відповіді або представлення її користувачу.

- **Інтеграція з Microsoft Agent Framework**. Microsoft Foundry Agent Service безшовно працює з Microsoft Agent Framework, що означає, що ви можете створювати агентів за допомогою `FoundryChatClient` і розгортати їх через Agent Service для виробничих сценаріїв.

**Випадки використання**: Microsoft Foundry Agent Service призначений для корпоративних застосунків, які потребують безпечного, масштабованого та гнучкого розгортання агентів ШІ.

## У чому різниця між цими підходами?
 
Виглядає так, ніби є перетин, але існують ключові відмінності в дизайні, можливостях та цільових варіантах застосування:
 
- **Microsoft Agent Framework (MAF)**: Це готовий для виробництва SDK для створення агентів ШІ. Він забезпечує оптимізований API для створення агентів із викликом інструментів, управлінням розмовами та інтеграцією Azure Identity.
- **Microsoft Foundry Agent Service**: Це платформа та сервіс розгортання в Microsoft Foundry для агентів. Пропонує вбудоване підключення до сервісів, таких як Azure OpenAI, Azure AI Search, Bing Search і виконання коду.
 
Все ще не впевнені, що обрати?

### Випадки використання
 
Давайте спробуємо допомогти, розглянувши деякі поширені випадки використання:
 
> Питання: Я створюю виробничі застосунки агентів ШІ і хочу швидко почати
>

>Відповідь: Microsoft Agent Framework — чудовий вибір. Він надає простий, «пітонічний» API через `FoundryChatClient`, який дозволяє визначати агентів з інструментами і інструкціями всього за кілька рядків коду.

>Питання: Мені потрібне корпоративне розгортання з інтеграціями Azure, такими як пошук і виконання коду
>
> Відповідь: Microsoft Foundry Agent Service — найкращий варіант. Це платформа, яка надає вбудовані можливості для роботи з кількома моделями, Azure AI Search, Bing Search та Azure Functions. Вона спрощує побудову агентів у порталі Foundry і масштабне розгортання.
 
> Питання: Я досі плутаюся, просто підкажіть один варіант
>
> Відповідь: Почніть з Microsoft Agent Framework для створення агентів, а потім використовуйте Microsoft Foundry Agent Service, коли потрібно розгорнути і масштабувати їх у виробництві. Такий підхід дозволяє швидко ітерувати логіку агентів та має чіткий шлях до корпоративного розгортання.
 
Підсумуємо ключові відмінності у таблиці:

| Фреймворк | Основний фокус | Основні концепції | Випадки використання |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Оптимізований SDK для агентів з викликом інструментів | Агенти, Інструменти, Azure Identity | Створення агентів ШІ, використання інструментів, багатокрокові робочі процеси |
| Microsoft Foundry Agent Service | Гнучкі моделі, корпоративна безпека, генерація коду, виклик інструментів | Модульність, Співпраця, Оркестрація процесів | Безпечне, масштабоване та гнучке розгортання агентів ШІ |

## Чи можу я інтегрувати свої існуючі інструменти екосистеми Azure безпосередньо, чи мені потрібні автономні рішення?


Відповідь — так, ви можете інтегрувати ваші наявні інструменти екосистеми Azure безпосередньо з Microsoft Foundry Agent Service, особливо оскільки він створений для безшовної роботи з іншими службами Azure. Наприклад, ви можете інтегрувати Bing, Azure AI Search і Azure Functions. Також існує глибока інтеграція з Microsoft Foundry.

Рамки агента Microsoft також інтегруються зі службами Azure через `FoundryChatClient` і ідентифікацію Azure, що дозволяє викликати служби Azure безпосередньо з ваших агентських інструментів.

## Зразки коду

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Потрібно більше питань про AI Agent Frameworks?

Приєднуйтесь до [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), щоб зустрітися з іншими учнями, відвідати години консультацій та отримати відповіді на ваші запитання про AI агентів.

## Посилання

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Попередній урок

[Вступ до AI агентів та сценаріїв використання агентів](../01-intro-to-ai-agents/README.md)

## Наступний урок

[Розуміння агентських патернів дизайну](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->