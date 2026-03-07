[![Вивчення фреймворків AI агентів](../../../translated_images/uk/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Вивчення фреймворків AI агентів

Фреймворки AI агентів — це програмні платформи, створені для спрощення розробки, розгортання та управління AI агентами. Ці фреймворки надають розробникам готові компоненти, абстракції та інструменти, які спрощують розробку складних AI систем.

Вони допомагають розробникам зосередитися на унікальних аспектах їхніх додатків, надаючи стандартизовані підходи до поширених викликів у розробці AI агентів. Вони підвищують масштабованість, доступність і ефективність при створенні AI систем.

## Вступ

У цьому уроці ви дізнаєтеся:

- Що таке фреймворки AI агентів і що вони дозволяють розробникам досягти?
- Як команди можуть використовувати їх для швидкого прототипування, ітерації та покращення можливостей свого агента?
- В чому різниця між фреймворками і інструментами, створеними Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> та <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Чи можу я інтегрувати свої існуючі інструменти екосистеми Azure безпосередньо, чи потрібні окремі рішення?
- Що таке Azure AI Agents service і яку користь він мені приносить?

## Цілі навчання

Мета цього уроку — допомогти вам зрозуміти:

- Роль фреймворків AI агентів у розробці AI.
- Як використовувати фреймворки AI агентів для створення інтелектуальних агентів.
- Ключові можливості, які надають фреймворки AI агентів.
- Відмінності між Microsoft Agent Framework та Azure AI Agent Service.

## Що таке фреймворки AI агентів і що вони дозволяють розробникам робити?

Традиційні AI фреймворки допомагають вам інтегрувати AI у ваші додатки і покращувати їх наступними способами:

- **Персоналізація**: AI може аналізувати поведінку користувача і вподобання для надання персоналізованих рекомендацій, контенту та досвіду.
Приклад: Стрімінгові сервіси, як Netflix, використовують AI, щоб пропонувати фільми та шоу на основі історії переглядів, підвищуючи залученість і задоволення користувачів.
- **Автоматизація та ефективність**: AI може автоматизувати рутинні завдання, оптимізувати робочі процеси та покращувати операційну ефективність.
Приклад: Додатки підтримки клієнтів використовують чатботів на базі AI для обробки типових запитів, скорочуючи час відповіді і звільняючи людських агентів для складніших випадків.
- **Покращений користувацький досвід**: AI може покращити загальний досвід користувача, надаючи інтелектуальні функції, такі як розпізнавання голосу, обробка природної мови та прогнозування тексту.
Приклад: Віртуальні помічники, як Siri і Google Assistant, використовують AI для розуміння та реагування на голосові команди, полегшуючи взаємодію користувачів з пристроями.

### Звучить чудово, але навіщо тоді потрібен AI Agent Framework?

Фреймворки AI агентів — це щось більше, ніж просто AI фреймворки. Вони створені для підтримки створення інтелектуальних агентів, які можуть взаємодіяти з користувачами, іншими агентами та навколишнім середовищем для досягнення конкретних цілей. Ці агенти можуть проявляти автономну поведінку, приймати рішення та адаптуватися до змінних умов. Розглянемо ключові можливості, які надають фреймворки AI агентів:

- **Співпраця та координація агентів**: Дозволяють створювати кілька AI агентів, які можуть працювати разом, спілкуватися і координуватися для розв’язання складних завдань.
- **Автоматизація та управління завданнями**: Надають механізми для автоматизації багатокрокових робочих процесів, делегування завдань і динамічного управління завданнями серед агентів.
- **Контекстуальне розуміння та адаптація**: Оснащують агентів здатністю розуміти контекст, адаптуватися до змінного середовища і приймати рішення на основі інформації в реальному часі.

Отже, підсумовуючи, агенти дозволяють робити більше, виводити автоматизацію на наступний рівень, створювати більш інтелектуальні системи, які можуть адаптуватися і навчатися від свого оточення.

## Як швидко прототипувати, ітерувати та покращувати можливості агента?

Ця сфера швидко розвивається, але є деякі спільні речі для більшості AI Agent Frameworks, які допоможуть швидко прототипувати і ітерувати, а саме: модульні компоненти, інструменти для співпраці та навчання в реальному часі. Розглянемо це докладніше:

- **Використовуйте модульні компоненти**: SDK AI пропонують готові компоненти, такі як AI та пам’яттєві конектори, виклики функцій за допомогою природної мови або кодових плагінів, шаблони запитів тощо.
- **Використовуйте інструменти для співпраці**: Проєктуйте агентів з конкретними ролями та завданнями, що дозволяє тестувати та вдосконалювати спільні робочі процеси.
- **Навчайтеся в реальному часі**: Реалізуйте цикли зворотного зв’язку, де агенти навчаються на взаємодіях і динамічно коригують свою поведінку.

### Використання модульних компонентів

SDK, як Microsoft Agent Framework, пропонують готові компоненти, такі як AI конектори, визначення інструментів і управління агентами.

**Як команди можуть їх використовувати**: Команди можуть швидко збирати ці компоненти для створення функціонального прототипу без початку з нуля, що дозволяє проводити швидкі експерименти та ітерації.

**Як це працює на практиці**: Ви можете використовувати готовий парсер для вилучення інформації з введення користувача, модуль пам’яті для збереження і отримання даних, генератор запитів для взаємодії з користувачем — все це без необхідності створювати компоненти з нуля.

**Приклад коду**. Розглянемо приклад використання Microsoft Agent Framework з `AzureAIProjectAgentProvider`, щоб модель відповідала на введення користувача з викликом інструментів:

``` python
# Приклад Microsoft Agent Framework для Python

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Визначте зразкову функцію інструмента для бронювання подорожей
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
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

У цьому прикладі видно, як можна використати готовий парсер для вилучення ключової інформації з введення користувача, такої як пункт відправлення, пункт призначення та дата бронювання рейсу. Такий модульний підхід дозволяє зосередитися на загальній логіці.

### Використання інструментів для співпраці

Фреймворки, як Microsoft Agent Framework, полегшують створення кількох агентів, які можуть працювати разом.

**Як команди можуть їх використовувати**: Команди можуть проектувати агентів з визначеними ролями та завданнями, що дозволяє тестувати і вдосконалювати спільні робочі процеси й підвищувати загальну ефективність системи.

**Як це працює на практиці**: Можна створити команду агентів, де кожен агент має спеціалізовану функцію, наприклад, отримання даних, аналіз або прийняття рішень. Ці агенти можуть спілкуватися і обмінюватися інформацією для досягнення спільної мети, наприклад відповіді на запит користувача або виконання завдання.

**Приклад коду (Microsoft Agent Framework)**:

```python
# Створення кількох агентів, що працюють разом за допомогою Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Агент отримання даних
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Агент аналізу даних
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Запустити агентів послідовно для виконання завдання
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

У наведеному прикладі коду видно, як створюється завдання з кількома агентами, які спільно працюють для аналізу даних. Кожен агент виконує конкретну функцію, а завдання виконується шляхом координації агентів для досягнення потрібного результату. Створюючи спеціалізованих агентів з визначеними ролями, можна покращити ефективність і продуктивність завдань.

### Навчання в реальному часі

Розвинуті фреймворки надають можливості для розуміння контексту і адаптації в реальному часі.

**Як команди можуть це використовувати**: Команди можуть впроваджувати цикли зворотного зв’язку, де агенти навчаються на основі взаємодій і динамічно коригують свою поведінку, що веде до постійного покращення та вдосконалення можливостей.

**Як це працює на практиці**: Агенти можуть аналізувати відгуки користувачів, дані про навколишнє середовище та результати виконання завдань для оновлення бази знань, регулювання алгоритмів прийняття рішень і покращення продуктивності з часом. Цей ітеративний процес навчання дозволяє агентам адаптуватися до змінних умов і вподобань користувачів, підвищуючи загальну ефективність системи.

## В чому різниця між Microsoft Agent Framework і Azure AI Agent Service?

Існує багато способів порівняти ці підходи, але розглянемо ключові відмінності з точки зору дизайну, можливостей і цільових випадків використання:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework надає спрощений SDK для створення AI агентів за допомогою `AzureAIProjectAgentProvider`. Він дозволяє розробникам створювати агентів, що використовують моделі Azure OpenAI з вбудованим викликом інструментів, управлінням розмовами та корпоративною безпекою через Azure identity.

**Випадки використання**: Створення агентів готових до виробництва з використанням інструментів, багатокрокових робочих процесів і сценаріїв корпоративної інтеграції.

Ось деякі важливі основні поняття Microsoft Agent Framework:

- **Агенти**. Агент створюється через `AzureAIProjectAgentProvider` і налаштовується з ім’ям, інструкціями та інструментами. Агент може:
  - **Обробляти повідомлення користувача** та генерувати відповіді за допомогою моделей Azure OpenAI.
  - **Автоматично викликати інструменти** на основі контексту розмови.
  - **Підтримувати стан розмови** під час кількох взаємодій.

  Ось фрагмент коду, який показує створення агента:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Інструменти**. Фреймворк підтримує визначення інструментів як функцій Python, які агент може викликати автоматично. Інструменти реєструються під час створення агента:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Координація мультиагентів**. Можна створювати кілька агентів із різними спеціалізаціями та координувати їхню роботу:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Інтеграція Azure Identity**. Фреймворк використовує `AzureCliCredential` (або `DefaultAzureCredential`) для безпечної безключової автентифікації, усуваючи необхідність управляти API-ключами безпосередньо.

## Azure AI Agent Service

Azure AI Agent Service — це новіше доповнення, представлене на Microsoft Ignite 2024. Воно дозволяє розробляти і розгортати AI агентів з більш гнучкими моделями, такими як прямий виклик відкритих LLM, наприклад Llama 3, Mistral і Cohere.

Azure AI Agent Service надає більш потужні механізми корпоративної безпеки та методи зберігання даних, що робить його придатним для корпоративних застосунків.

Він працює "з коробки" з Microsoft Agent Framework для створення і розгортання агентів.

Цей сервіс наразі знаходиться в відкритому прев’ю і підтримує Python та C# для створення агентів.

За допомогою Python SDK для Azure AI Agent Service можна створити агента з інструментом, визначеним користувачем:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Визначте функції інструментів
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
        model="gpt-4o-mini",
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

### Основні поняття

Основні поняття Azure AI Agent Service:

- **Агент**. Azure AI Agent Service інтегрується з Microsoft Foundry. В AI Foundry AI Агент виступає як "розумний" мікросервіс, який може відповідати на запитання (RAG), виконувати дії або повністю автоматизувати робочі процеси. Він досягає цього, поєднуючи можливості генеративних AI моделей з інструментами, що дозволяють йому отримувати доступ і взаємодіяти з реальними джерелами даних. Ось приклад агента:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    У цьому прикладі агент створюється з моделлю `gpt-4o-mini`, іменем `my-agent` і інструкціями `You are helpful agent`. Агент оснащений інструментами та ресурсами для виконання завдань інтерпретації коду.

- **Тред і повідомлення**. Тред — це ще одне важливе поняття. Він представляє розмову або взаємодію між агентом і користувачем. Треди можна використовувати для відстеження прогресу розмови, збереження контекстної інформації та управління станом взаємодії. Ось приклад треда:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    У наведеному прикладі створюється тред. Потім у тред надсилається повідомлення. Викликом `create_and_process_run` агенту доручається виконати роботу в треді. Нарешті, повідомлення отримуються і записуються в журнал, щоб побачити відповідь агента. Повідомлення демонструють прогрес розмови між користувачем і агентом. Важливо розуміти, що повідомлення можуть бути різних типів: текст, зображення або файл, тобто робота агента могла призвести, наприклад, до створення зображення або текстової відповіді. Як розробник, ви можете далі обробляти цю інформацію або відображати її користувачу.

- **Інтеграція з Microsoft Agent Framework**. Azure AI Agent Service працює бездоганно з Microsoft Agent Framework, що означає, що ви можете створювати агентів за допомогою `AzureAIProjectAgentProvider` і розгортати їх через Agent Service для виробничих сценаріїв.

**Випадки використання**: Azure AI Agent Service призначений для корпоративних застосувань, що потребують безпечного, масштабованого і гнучкого розгортання AI агентів.

## У чому різниця між цими підходами?

Звісно, є деяке перекриття, але існують ключові відмінності в дизайні, можливостях і цільових випадках використання:

- **Microsoft Agent Framework (MAF)**: Це SDK, готовий до виробництва, для створення AI агентів. Він пропонує простий API для створення агентів з викликом інструментів, управлінням розмовами та інтеграцією Azure identity.
- **Azure AI Agent Service**: Це платформа і сервіс розгортання в Azure Foundry для агентів. Пропонує вбудоване підключення до сервісів, таких як Azure OpenAI, Azure AI Search, Bing Search та виконання коду.

Ви все ще вагаєтеся, що обрати?

### Випадки використання

Розглянемо кілька поширених сценаріїв:

> П: Я створюю виробничі додатки AI агентів і хочу швидко почати.
>

>В: Microsoft Agent Framework є чудовим вибором. Він надає простий, зручний API на Python через `AzureAIProjectAgentProvider`, який дозволяє визначати агентів із інструментами і інструкціями всього в кілька рядків коду.

>П: Мені потрібне корпоративне розгортання з інтеграцією Azure, як Search та виконання коду.
>
>В: Azure AI Agent Service краще підходить. Це платформа, яка надає вбудовані можливості для роботи з декількома моделями, Azure AI Search, Bing Search та Azure Functions. Легко створюйте агентів в Foundry Portal і масштабовано розгортайте їх.
 
> П: Я все ще не впевнений, просто дайте мені один варіант.
>
>В: Почніть з Microsoft Agent Framework для створення агентів, а коли буде потрібно розгортати і масштабувати їх у виробництві — використовуйте Azure AI Agent Service. Такий підхід дозволяє швидко ітерувати логіку агента та одночасно мати чіткий шлях до корпоративного розгортання.

Підсумуємо ключові відмінності у таблиці:

| Фреймворк | Фокус | Основні поняття | Випадки використання |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Спрощений SDK з викликом інструментів | Агенти, Інструменти, Azure Identity | Створення AI агентів, використання інструментів, багатокрокові робочі процеси |
| Azure AI Agent Service | Гнучкі моделі, корпоративна безпека, генерація коду, виклик інструментів | Модульність, Співпраця, Оркестрація процесів | Безпечне, масштабоване та гнучке розгортання AI агентів |

## Чи можу я інтегрувати свої існуючі інструменти екосистеми Azure напряму, чи потрібні окремі рішення?
Відповідь — так, ви можете інтегрувати свої існуючі інструменти екосистеми Azure безпосередньо з Azure AI Agent Service, особливо оскільки вона створена для безперешкодної роботи з іншими сервісами Azure. Наприклад, ви можете інтегрувати Bing, Azure AI Search та Azure Functions. Також існує глибока інтеграція з Microsoft Foundry.

Microsoft Agent Framework також інтегрується із сервісами Azure через `AzureAIProjectAgentProvider` та ідентифікацію Azure, що дозволяє викликати сервіси Azure безпосередньо з ваших агентських інструментів.

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Got More Questions about AI Agent Frameworks?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## References

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Previous Lesson

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Next Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений із використанням сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоч ми і прагнемо до точності, просимо враховувати, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння чи неправильне тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->