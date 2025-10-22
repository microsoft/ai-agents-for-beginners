<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86b9c2b24da3b3e61711182ffa72601c",
  "translation_date": "2025-09-29T23:04:28+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "uk"
}
-->
[![Дослідження фреймворків AI агентів](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.uk.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Дослідження фреймворків AI агентів

Фреймворки AI агентів — це програмні платформи, створені для спрощення розробки, розгортання та управління AI агентами. Ці фреймворки надають розробникам готові компоненти, абстракції та інструменти, які полегшують створення складних AI систем.

Фреймворки допомагають розробникам зосередитися на унікальних аспектах їхніх додатків, пропонуючи стандартизовані підходи до вирішення загальних викликів у розробці AI агентів. Вони покращують масштабованість, доступність та ефективність у створенні AI систем.

## Вступ

Цей урок охоплює:

- Що таке фреймворки AI агентів і що вони дозволяють розробникам досягти?
- Як команди можуть використовувати їх для швидкого прототипування, ітерації та покращення можливостей агентів?
- Які відмінності між фреймворками та інструментами, створеними Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> та <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- Чи можу я інтегрувати свої існуючі інструменти екосистеми Azure безпосередньо, чи потрібні окремі рішення?
- Що таке служба Azure AI Agents і як вона допомагає мені?

## Цілі навчання

Цілі цього уроку — допомогти вам зрозуміти:

- Роль фреймворків AI агентів у розробці AI.
- Як використовувати фреймворки AI агентів для створення інтелектуальних агентів.
- Основні можливості, які забезпечують фреймворки AI агентів.
- Відмінності між AutoGen, Semantic Kernel та Azure AI Agent Service.

## Що таке фреймворки AI агентів і що вони дозволяють розробникам робити?

Традиційні AI фреймворки можуть допомогти інтегрувати AI у ваші додатки та покращити їх у таких аспектах:

- **Персоналізація**: AI може аналізувати поведінку користувачів і їхні вподобання, щоб надавати персоналізовані рекомендації, контент і досвід.
Приклад: Стримінгові сервіси, такі як Netflix, використовують AI для пропонування фільмів і шоу на основі історії переглядів, підвищуючи залученість і задоволення користувачів.
- **Автоматизація та ефективність**: AI може автоматизувати повторювані завдання, оптимізувати робочі процеси та покращувати операційну ефективність.
Приклад: Додатки для обслуговування клієнтів використовують чат-ботів на основі AI для обробки загальних запитів, скорочуючи час відповіді та звільняючи людських агентів для вирішення складніших питань.
- **Покращений користувацький досвід**: AI може покращити загальний досвід користувача, надаючи інтелектуальні функції, такі як розпізнавання голосу, обробка природної мови та прогнозування тексту.
Приклад: Віртуальні асистенти, такі як Siri та Google Assistant, використовують AI для розуміння та реагування на голосові команди, полегшуючи взаємодію користувачів із пристроями.

### Це звучить чудово, правда? То чому нам потрібен фреймворк AI агентів?

Фреймворки AI агентів представляють щось більше, ніж просто AI фреймворки. Вони створені для забезпечення створення інтелектуальних агентів, які можуть взаємодіяти з користувачами, іншими агентами та середовищем для досягнення конкретних цілей. Ці агенти можуть демонструвати автономну поведінку, приймати рішення та адаптуватися до змінних умов. Давайте розглянемо ключові можливості, які забезпечують фреймворки AI агентів:

- **Співпраця та координація агентів**: Дозволяють створювати кілька AI агентів, які можуть працювати разом, спілкуватися та координуватися для вирішення складних завдань.
- **Автоматизація та управління завданнями**: Забезпечують механізми для автоматизації багатокрокових робочих процесів, делегування завдань і динамічного управління завданнями між агентами.
- **Контекстуальне розуміння та адаптація**: Оснащують агентів здатністю розуміти контекст, адаптуватися до змінних умов і приймати рішення на основі інформації в реальному часі.

Отже, підсумовуючи, агенти дозволяють робити більше, підняти автоматизацію на новий рівень, створювати більш інтелектуальні системи, які можуть адаптуватися та навчатися від свого середовища.

## Як швидко прототипувати, ітерувати та покращувати можливості агентів?

Це швидко змінюваний ландшафт, але є деякі речі, які є спільними для більшості фреймворків AI агентів і можуть допомогти вам швидко прототипувати та ітерувати, а саме модульні компоненти, інструменти для співпраці та навчання в реальному часі. Давайте розглянемо ці аспекти:

- **Використовуйте модульні компоненти**: SDK AI пропонують готові компоненти, такі як AI та Memory конектори, виклик функцій за допомогою природної мови або плагінів коду, шаблони підказок тощо.
- **Використовуйте інструменти для співпраці**: Проектуйте агентів із конкретними ролями та завданнями, що дозволяє тестувати та вдосконалювати робочі процеси співпраці.
- **Навчайтеся в реальному часі**: Реалізуйте цикли зворотного зв’язку, де агенти навчаються від взаємодій і динамічно коригують свою поведінку.

### Використовуйте модульні компоненти

SDK, такі як Microsoft Semantic Kernel і LangChain, пропонують готові компоненти, такі як AI конектори, шаблони підказок і управління пам’яттю.

**Як команди можуть використовувати це**: Команди можуть швидко зібрати ці компоненти, щоб створити функціональний прототип без необхідності починати з нуля, що дозволяє швидко експериментувати та ітерувати.

**Як це працює на практиці**: Ви можете використовувати готовий парсер для вилучення інформації з введення користувача, модуль пам’яті для зберігання та отримання даних і генератор підказок для взаємодії з користувачами, все це без необхідності створювати ці компоненти з нуля.

**Приклад коду**. Давайте розглянемо приклади того, як можна використовувати готовий AI конектор із Semantic Kernel Python і .Net, який використовує автоматичний виклик функцій, щоб модель реагувала на введення користувача:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

З цього прикладу видно, як можна використовувати готовий парсер для вилучення ключової інформації з введення користувача, наприклад, місця відправлення, призначення та дати запиту на бронювання рейсу. Цей модульний підхід дозволяє зосередитися на логіці високого рівня.

### Використовуйте інструменти для співпраці

Фреймворки, такі як CrewAI, Microsoft AutoGen і Semantic Kernel, сприяють створенню кількох агентів, які можуть працювати разом.

**Як команди можуть використовувати це**: Команди можуть проектувати агентів із конкретними ролями та завданнями, що дозволяє тестувати та вдосконалювати робочі процеси співпраці та покращувати загальну ефективність системи.

**Як це працює на практиці**: Ви можете створити команду агентів, де кожен агент має спеціалізовану функцію, наприклад, отримання даних, аналіз або прийняття рішень. Ці агенти можуть спілкуватися та обмінюватися інформацією для досягнення спільної мети, наприклад, відповіді на запит користувача або виконання завдання.

**Приклад коду (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

У попередньому коді показано, як можна створити завдання, яке передбачає співпрацю кількох агентів для аналізу даних. Кожен агент виконує певну функцію, а завдання виконується шляхом координації агентів для досягнення бажаного результату. Створюючи спеціалізованих агентів із конкретними ролями, ви можете покращити ефективність і продуктивність завдань.

### Навчайтеся в реальному часі

Розширені фреймворки забезпечують можливості для розуміння контексту в реальному часі та адаптації.

**Як команди можуть використовувати це**: Команди можуть реалізувати цикли зворотного зв’язку, де агенти навчаються від взаємодій і динамічно коригують свою поведінку, що призводить до постійного вдосконалення та покращення можливостей.

**Як це працює на практиці**: Агенти можуть аналізувати зворотний зв’язок користувачів, дані середовища та результати завдань, щоб оновлювати свою базу знань, коригувати алгоритми прийняття рішень і покращувати продуктивність з часом. Цей ітеративний процес навчання дозволяє агентам адаптуватися до змінних умов і вподобань користувачів, покращуючи загальну ефективність системи.

## Які відмінності між фреймворками AutoGen, Semantic Kernel та Azure AI Agent Service?

Існує багато способів порівняти ці фреймворки, але давайте розглянемо ключові відмінності з точки зору їхнього дизайну, можливостей і цільових сценаріїв використання:

## AutoGen

AutoGen — це фреймворк з відкритим кодом, розроблений лабораторією AI Frontiers Lab Microsoft Research. Він зосереджений на подієво-орієнтованих, розподілених *агентних* додатках, що дозволяють використовувати кілька LLMs і SLMs, інструменти та розширені шаблони дизайну багатокористувацьких агентів.

AutoGen побудований навколо основної концепції агентів, які є автономними сутностями, здатними сприймати своє середовище, приймати рішення та виконувати дії для досягнення конкретних цілей. Агенти спілкуються через асинхронні повідомлення, що дозволяє їм працювати незалежно та паралельно, покращуючи масштабованість і чутливість системи.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Агенти базуються на моделі акторів</a>. Згідно з Вікіпедією, актор — це _основний будівельний блок паралельних обчислень. У відповідь на отримане повідомлення актор може: приймати локальні рішення, створювати більше акторів, надсилати більше повідомлень і визначати, як реагувати на наступне отримане повідомлення_.

**Сценарії використання**: Автоматизація генерації коду, завдань аналізу даних і створення спеціальних агентів для функцій планування та дослідження.

Ось деякі важливі основні концепції AutoGen:

- **Агенти**. Агент — це програмна сутність, яка:
  - **Спілкується через повідомлення**, ці повідомлення можуть бути синхронними або асинхронними.
  - **Підтримує власний стан**, який може бути змінений вхідними повідомленнями.
  - **Виконує дії** у відповідь на отримані повідомлення або зміни свого стану. Ці дії можуть змінювати стан агента та створювати зовнішні ефекти, такі як оновлення журналів повідомлень, надсилання нових повідомлень, виконання коду або виклик API.

  Ось короткий фрагмент коду, у якому ви створюєте власного агента з можливостями чату:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    У попередньому коді створено `MyAgent`, який успадковує `RoutedAgent`. Він має обробник повідомлень, який друкує вміст повідомлення, а потім надсилає відповідь за допомогою делегата `AssistantAgent`. Особливо зверніть увагу, як ми призначаємо `self._delegate` екземпляр `AssistantAgent`, який є готовим агентом, здатним обробляти завершення чату.

    Давайте повідомимо AutoGen про цей тип агента та запустимо програму:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    У попередньому коді агенти реєструються в середовищі виконання, а потім повідомлення надсилається агенту, що призводить до наступного результату:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Багато агентів**. AutoGen підтримує створення кількох агентів, які можуть працювати разом для досягнення складних завдань. Агенти можуть спілкуватися, обмінюватися інформацією та координувати свої дії для більш ефективного вирішення проблем. Щоб створити систему з багатьма агентами, ви можете визначити різні типи агентів із спеціалізованими функціями та ролями, такими як отримання даних, аналіз, прийняття рішень і взаємодія з користувачем. Давайте подивимося, як виглядає таке створення:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```

    У попередньому коді у нас є `GroupChatManager`, який зареєстрований у середовищі виконання. Цей менеджер відповідає за координацію взаємодії між різними типами агентів, такими як письменники, ілюстратори, редактори та користувачі.

- **Середовище виконання агентів**. Фреймворк забезпечує середовище виконання, яке дозволяє спілкування між агентами, управляє їхніми ідентичностями та життєвими циклами, а також забезпечує дотримання меж безпеки та конфіденційності. Це означає, що ви можете запускати своїх агентів у безпечному та контрольованому середовищі, забезпечуючи їхню безпечну та ефективну взаємодію. Існує два середовища виконання, які заслуговують на увагу:
  - **Автономне середовище виконання**. Це хороший вибір для однопроцесних додатків, де всі агенти реалізовані однією мовою програмування та працюють у тому ж процесі. Ось ілюстрація того, як це працює:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Автономне середовище виконання</a>   
    *агенти спілкуються через повідомлення через середовище виконання, яке управляє життєвим циклом агентів*

  - **Розподілене середовище виконання агентів**, підходить для багатопроцесних додатків, де агенти можуть бути реалізовані різними мовами програмування та працювати на різних машинах. Ось ілюстрація того, як це працює:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Розподілене середовище виконання</a>

## Semantic Kernel + Agent Framework

Semantic Kernel — це SDK для оркестрації AI, готовий до використання в корпоративному середовищі. Він складається з AI та Memory конекторів, а також фреймворку агентів.

Спочатку розглянемо деякі основні компоненти:

- **AI конектори**: Це інтерфейс із зовнішніми AI сервісами та джерелами даних для використання як у Python, так і в C#.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  

    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```

    Тут наведено простий приклад того, як можна створити ядро та додати сервіс завершення чату. Semantic
Ці факти потім зберігаються в колекції пам'яті `SummarizedAzureDocs`. Це дуже спрощений приклад, але ви можете побачити, як можна зберігати інформацію в пам'яті для використання LLM.

Отже, це основи фреймворку Semantic Kernel, а як щодо Agent Framework?

## Сервіс Azure AI Agent

Сервіс Azure AI Agent — це більш нове доповнення, представлене на Microsoft Ignite 2024. Він дозволяє розробляти та розгортати AI-агенти з більш гнучкими моделями, такими як прямий виклик відкритих LLM, таких як Llama 3, Mistral і Cohere.

Сервіс Azure AI Agent забезпечує сильніші механізми безпеки для підприємств і методи зберігання даних, що робить його придатним для корпоративних застосувань.

Він працює "з коробки" з фреймворками оркестрації мультиагентів, такими як AutoGen і Semantic Kernel.

Цей сервіс наразі знаходиться в Public Preview і підтримує Python та C# для створення агентів.

Використовуючи Semantic Kernel Python, ми можемо створити Azure AI Agent з плагіном, визначеним користувачем:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Основні концепції

Сервіс Azure AI Agent має наступні основні концепції:

- **Агент**. Сервіс Azure AI Agent інтегрується з Azure AI Foundry. У рамках AI Foundry AI-агент діє як "розумний" мікросервіс, який можна використовувати для відповідей на запитання (RAG), виконання дій або повної автоматизації робочих процесів. Це досягається шляхом поєднання потужності генеративних AI-моделей з інструментами, які дозволяють отримувати доступ до реальних джерел даних і взаємодіяти з ними. Ось приклад агента:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    У цьому прикладі створюється агент з моделлю `gpt-4o-mini`, ім'ям `my-agent` і інструкціями `You are helpful agent`. Агент оснащений інструментами та ресурсами для виконання завдань інтерпретації коду.

- **Потік і повідомлення**. Потік — це ще одна важлива концепція. Він представляє розмову або взаємодію між агентом і користувачем. Потоки можна використовувати для відстеження прогресу розмови, зберігання контекстної інформації та управління станом взаємодії. Ось приклад потоку:

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

    У попередньому коді створюється потік. Потім до потоку надсилається повідомлення. Викликаючи `create_and_process_run`, агенту доручається виконати роботу над потоком. Нарешті, повідомлення отримуються і записуються, щоб побачити відповідь агента. Повідомлення вказують на прогрес розмови між користувачем і агентом. Також важливо розуміти, що повідомлення можуть бути різних типів, таких як текст, зображення або файл, тобто робота агента може призвести, наприклад, до створення зображення або текстової відповіді. Як розробник, ви можете використовувати цю інформацію для подальшої обробки відповіді або її представлення користувачеві.

- **Інтеграція з іншими AI-фреймворками**. Сервіс Azure AI Agent може взаємодіяти з іншими фреймворками, такими як AutoGen і Semantic Kernel, що означає, що ви можете створити частину вашого застосунку в одному з цих фреймворків, наприклад, використовуючи сервіс Agent як оркестратор, або створити все в сервісі Agent.

**Випадки використання**: Сервіс Azure AI Agent призначений для корпоративних застосунків, які потребують безпечного, масштабованого та гнучкого розгортання AI-агентів.

## У чому різниця між цими фреймворками?

Здається, що між цими фреймворками є багато спільного, але є ключові відмінності в їхньому дизайні, можливостях і цільових випадках використання:

- **AutoGen**: Це експериментальний фреймворк, орієнтований на передові дослідження мультиагентних систем. Це найкраще місце для експериментів і прототипування складних мультиагентних систем.
- **Semantic Kernel**: Це готова до виробництва бібліотека агентів для створення корпоративних агентних застосунків. Зосереджується на подіях, розподілених агентних застосунках, дозволяючи використовувати кілька LLM і SLM, інструменти та одно-/мультиагентні шаблони дизайну.
- **Azure AI Agent Service**: Це платформа і сервіс розгортання в Azure Foundry для агентів. Пропонує побудову підключення до сервісів, підтримуваних Azure, таких як Azure OpenAI, Azure AI Search, Bing Search і виконання коду.

Все ще не впевнені, який вибрати?

### Випадки використання

Давайте спробуємо допомогти вам, розглянувши деякі поширені випадки використання:

> Питання: Я експериментую, вивчаю і створюю прототипи агентних застосунків, і хочу мати можливість швидко створювати та експериментувати.

> Відповідь: AutoGen буде хорошим вибором для цього сценарію, оскільки він зосереджується на подіях, розподілених агентних застосунках і підтримує передові шаблони дизайну мультиагентів.

> Питання: Чому AutoGen є кращим вибором, ніж Semantic Kernel і Azure AI Agent Service для цього випадку використання?

> Відповідь: AutoGen спеціально розроблений для подій, розподілених агентних застосунків, що робить його добре підходящим для автоматизації завдань генерації коду та аналізу даних. Він забезпечує необхідні інструменти та можливості для ефективного створення складних мультиагентних систем.

> Питання: Здається, що Azure AI Agent Service також може підійти, адже він має інструменти для генерації коду та багато іншого?

> Відповідь: Так, Azure AI Agent Service — це платформний сервіс для агентів, який додає вбудовані можливості для кількох моделей, Azure AI Search, Bing Search і Azure Functions. Це дозволяє легко створювати ваших агентів у Foundry Portal і розгортати їх у масштабі.

> Питання: Я все ще заплутаний, просто дайте мені один варіант.

> Відповідь: Чудовим вибором буде спочатку створити ваш застосунок у Semantic Kernel, а потім використовувати Azure AI Agent Service для розгортання вашого агента. Цей підхід дозволяє легко зберігати ваших агентів, використовуючи потужність для створення мультиагентних систем у Semantic Kernel. Крім того, Semantic Kernel має конектор в AutoGen, що робить його легким для використання обох фреймворків разом.

Давайте підсумуємо ключові відмінності в таблиці:

| Фреймворк | Фокус | Основні концепції | Випадки використання |
| --- | --- | --- | --- |
| AutoGen | Події, розподілені агентні застосунки | Агенти, Персони, Функції, Дані | Генерація коду, завдання аналізу даних |
| Semantic Kernel | Розуміння та генерація текстового контенту, схожого на людський | Агенти, Модульні компоненти, Співпраця | Розуміння природної мови, генерація контенту |
| Azure AI Agent Service | Гнучкі моделі, корпоративна безпека, Генерація коду, Виклик інструментів | Модульність, Співпраця, Оркестрація процесів | Безпечне, масштабоване та гнучке розгортання AI-агентів |

Який ідеальний випадок використання для кожного з цих фреймворків?

## Чи можу я інтегрувати свої існуючі інструменти екосистеми Azure безпосередньо, чи мені потрібні автономні рішення?

Відповідь — так, ви можете інтегрувати свої існуючі інструменти екосистеми Azure безпосередньо з Azure AI Agent Service, особливо тому, що він був створений для безперебійної роботи з іншими сервісами Azure. Наприклад, ви можете інтегрувати Bing, Azure AI Search і Azure Functions. Також є глибока інтеграція з Azure AI Foundry.

Для AutoGen і Semantic Kernel ви також можете інтегруватися з сервісами Azure, але це може вимагати виклику сервісів Azure з вашого коду. Інший спосіб інтеграції — використовувати SDK Azure для взаємодії з сервісами Azure через ваших агентів. Крім того, як було згадано, ви можете використовувати Azure AI Agent Service як оркестратор для ваших агентів, створених в AutoGen або Semantic Kernel, що забезпечить легкий доступ до екосистеми Azure.

### Є ще питання про фреймворки AI Agent?

Приєднуйтесь до [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), щоб зустрітися з іншими учнями, відвідати години консультацій і отримати відповіді на ваші запитання про AI-агентів.

## Посилання

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Сервіс Azure Agent</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel і AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Сервіс Azure AI Agent</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Використання Azure AI Agent Service з AutoGen / Semantic Kernel для створення мультиагентного рішення</a>

## Попередній урок

[Вступ до AI-агентів і випадків використання агентів](../01-intro-to-ai-agents/README.md)

## Наступний урок

[Розуміння шаблонів агентного дизайну](../03-agentic-design-patterns/README.md)

---

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникають внаслідок використання цього перекладу.