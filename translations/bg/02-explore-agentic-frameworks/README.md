[![Изследване на рамките за AI агенти](../../../translated_images/bg/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Кликнете на изображението по-горе, за да гледате видеото на този урок)_

# Изследване на рамките за AI агенти

Рамките за AI агенти са софтуерни платформи, предназначени да опростят създаването, разгръщането и управлението на AI агенти. Тези рамки предоставят на разработчиците предварително изградени компоненти, абстракции и инструменти, които улесняват разработката на сложни AI системи.

Тези рамки помагат на разработчиците да се съсредоточат върху уникалните аспекти на своите приложения, като предоставят стандартизирани подходи към общите предизвикателства при разработката на AI агенти. Те подобряват мащабируемостта, достъпността и ефективността при изграждането на AI системи.

## Въведение

Този урок ще обхване:

- Какво са рамките за AI агенти и какво позволяват на разработчиците да постигнат?
- Как екипите могат да използват тези рамки за бързо прототипиране, итерации и подобряване на възможностите на своя агент?
- Какви са разликите между рамките и инструментите, създадени от Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> и <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Мога ли директно да интегрирам съществуващите инструменти от Azure екосистемата, или имам нужда от самостоятелни решения?
- Какво е Microsoft Foundry Agent Service и как ми помага?

## Цели за учене

Целите на този урок са да ви помогнат да разберете:

- Ролята на рамките за AI агенти в разработката на AI.
- Как да използвате рамките за AI агенти за изграждане на интелигентни агенти.
- Ключови възможности, предоставени от рамките за AI агенти.
- Разликите между Microsoft Agent Framework и Microsoft Foundry Agent Service.

## Какво са рамките за AI агенти и какво позволяват на разработчиците да правят?

Традиционните рамки за AI могат да ви помогнат да интегрирате AI в приложенията си и да ги направите по-добри по следните начини:

- **Персонализация**: AI може да анализира поведението и предпочитанията на потребителя, за да предостави персонализирани препоръки, съдържание и преживявания.
Пример: Потокови услуги като Netflix използват AI, за да предлагат филми и предавания въз основа на историята на гледане, повишавайки ангажираността и удовлетворението на потребителите.
- **Автоматизация и ефективност**: AI може да автоматизира повтарящи се задачи, да оптимизира работните потоци и да подобри оперативната ефективност.
Пример: Обслужващи клиенти приложения използват чатботове с AI, които обработват общи запитвания, намалявайки времето за отговор и освобождавайки човешки агенти за по-сложни въпроси.
- **Подобрено потребителско изживяване**: AI може да подобри цялостното потребителско преживяване, като предоставя интелигентни функции, като разпознаване на глас, обработка на естествен език и предсказуем текст.
Пример: Виртуални асистенти като Siri и Google Assistant използват AI, за да разбират и отговарят на гласови команди, улеснявайки взаимодействието на потребителите с устройствата им.

### Звучи страхотно, нали? Защо тогава имаме нужда от рамка за AI агенти?

Рамките за AI агенти представляват нещо повече от просто AI рамки. Те са проектирани да позволят създаването на интелигентни агенти, които могат да взаимодействат с потребители, други агенти и околната среда, за да постигнат конкретни цели. Тези агенти могат да проявяват автономно поведение, да вземат решения и да се адаптират към променящи се условия. Нека разгледаме някои ключови възможности, предоставени от рамките за AI агенти:

- **Сътрудничество и координация между агенти**: Позволява създаване на множество AI агенти, които могат да работят заедно, да комуникират и да координират изпълнението на сложни задачи.
- **Автоматизация и управление на задачи**: Предоставя механизми за автоматизиране на многоетапни работни потоци, делегиране на задачи и динамично управление между агентите.
- **Контекстуално разбиране и адаптация**: Оборудва агентите с възможността да разбират контекста, да се адаптират към променяща се среда и да вземат решения на базата на информация в реално време.

В обобщение, агентите ви позволяват да правите повече, да издигнете автоматизацията на следващото ниво, да създавате по-интелигентни системи, които могат да се адаптират и учат от своята среда.

## Как бързо да прототипираме, итерараме и подобряваме възможностите на агента?

Това е бързо развиваща се област, но има някои общи черти в повечето рамки за AI агенти, които могат да ви помогнат бързо да прототипирате и итерарате — на първо място модулни компоненти, сътруднически инструменти и учене в реално време. Нека разгледаме тези:

- **Използвайте модулни компоненти**: AI SDK предлагат предварително изградени компоненти като AI и паметни конектори, извикване на функции с естествен език или плъгини с код, шаблони за подканяне и други.
- **Възползвайте се от сътруднически инструменти**: Проектирайте агенти с конкретни роли и задачи, позволявайки им да тестват и усъвършенстват сътруднически работни потоци.
- **Учете в реално време**: Прилагайте обратни връзки, където агентите се учат от взаимодействия и динамично настройват поведението си.

### Използвайте модулни компоненти

SDK-та като Microsoft Agent Framework предлагат предварително създадени компоненти като AI конектори, дефиниции на инструменти и управление на агенти.

**Как екипите могат да използват това**: Екипите могат бързо да компилират тези компоненти, за да създадат функционален прототип без да започват от нулата, което позволява бърза експериментация и итерации.

**Как работи на практика**: Можете да използвате предварително изграден парсер за извличане на информация от потребителски вход, модул за памет за съхранение и извличане на данни и генератор на подканване за взаимодействие с потребителите, всичко това без да изграждате тези компоненти сами.

**Примерен код**: Нека разгледаме пример как можете да използвате Microsoft Agent Framework с `FoundryChatClient`, за да накарате модела да отговаря на потребителски вход с извикване на инструменти:

``` python
# Пример с Microsoft Agent Framework на Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Дефинирайте примерна функция на инструмент за резервация на пътувания
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
    # Примерен изход: Вашият полет до Ню Йорк на 1 януари 2025 г. е успешно резервиран. Приятно пътуване! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Това, което можете да видите от този пример, е как можете да използвате предварително изграден парсер, за да извлечете ключова информация от потребителския вход, като произход, местоназначение и дата на заявка за полет. Този модулен подход ви позволява да се съсредоточите върху логиката на по-високо ниво.

### Възползвайте се от сътруднически инструменти

Рамки като Microsoft Agent Framework улесняват създаването на множество агенти, които могат да работят заедно.

**Как екипите могат да използват това**: Екипите могат да проектират агенти с конкретни роли и задачи, позволявайки им да тестват и усъвършенстват сътруднически работни потоци и да подобрят общата ефективност на системата.

**Как работи на практика**: Можете да създадете екип от агенти, където всеки агент има специализирана функция, като извличане на данни, анализ или вземане на решения. Тези агенти могат да комуникират и споделят информация, за да постигнат обща цел, като отговаряне на потребителска заявка или изпълнение на задача.

**Примерен код (Microsoft Agent Framework)**:

```python
# Създаване на множество агенти, които работят заедно, използвайки Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Агент за извличане на данни
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Агент за анализ на данни
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Стартирайте агентите в последователност за задача
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Както виждате в предишния код, можете да създадете задача, която включва множество агенти, работещи заедно за анализ на данни. Всеки агент изпълнява конкретна функция, а задачата се изпълнява чрез координиране на агентите за постигане на желания резултат. Създавайки посветени агенти с специализирани роли, можете да подобрите ефективността и производителността на задачата.

### Учете в реално време

Разширените рамки предоставят възможности за разбиране и адаптация на контекста в реално време.

**Как екипите могат да използват това**: Екипите могат да прилагат обратни връзки, където агентите се учат от взаимодействия и динамично коригират поведението си, водейки до непрекъснато подобрение и усъвършенстване на възможностите.

**Как работи на практика**: Агентите могат да анализират обратна връзка от потребителите, данни от околната среда и резултатите от задачите, за да актуализират своята база знания, да настройват алгоритмите за вземане на решения и да подобряват изпълнението с времето. Този итеративен процес на учене позволява на агентите да се адаптират към променящи се условия и предпочитания на потребителите, подобрявайки общата ефективност на системата.

## Какви са разликите между Microsoft Agent Framework и Microsoft Foundry Agent Service?

Има много начини да се сравнят тези подходи, но нека разгледаме някои ключови разлики по отношение на техния дизайн, възможности и целеви случаи на употреба:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework предоставя олекотен SDK за изграждане на AI агенти с използване на `FoundryChatClient`. Той позволява на разработчиците да създават агенти, които използват Azure OpenAI модели с вградена възможност за извикване на инструменти, управление на разговори и корпоративна сигурност чрез Azure идентичност.

**Случаи на употреба**: Изграждане на AI агенти, готови за продукция, с използване на инструменти, многоетапни работни потоци и корпоративни интеграции.

Ето някои важни основни концепции на Microsoft Agent Framework:

- **Агенти**. Агентът се създава чрез `FoundryChatClient` и се конфигурира с име, инструкции и инструменти. Агентът може:
  - **Да обработва потребителски съобщения** и да генерира отговори с помощта на Azure OpenAI модели.
  - **Автоматично да извиква инструменти** в зависимост от контекста на разговора.
  - **Да поддържа състоянието на разговора** през множество взаимодействия.

  Ето примерен код, показващ как се създава агент:

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

- **Инструменти**. Рамката поддържа дефиниране на инструменти като Python функции, които агентът може да извиква автоматично. Инструментите се регистрират при създаване на агента:

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

- **Координация на множество агенти**. Можете да създадете множество агенти с различни специализации и да координирате работата им:

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

- **Интеграция с Azure идентичност**. Рамката използва `AzureCliCredential` (или `DefaultAzureCredential`) за сигурна, безключова автентикация, като елиминира нуждата от директно управление на API ключове.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service е по-нова добавка, представена на Microsoft Ignite 2024. Тя позволява разработка и разгръщане на AI агенти с по-гъвкави модели, като директно извикване на отворен код LLM модели като Llama 3, Mistral и Cohere.

Microsoft Foundry Agent Service предлага по-силни механизми за корпоративна сигурност и методи за съхранение на данни, което го прави подходящ за корпоративни приложения.

Работи директно с Microsoft Agent Framework за изграждане и разгръщане на агенти.

Тази услуга в момента е в Публична предварителна версия и поддържа Python и C# за изграждане на агенти.

Използвайки Python SDK на Microsoft Foundry Agent Service, можем да създадем агент с потребителски дефиниран инструмент:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Дефинирайте функции на инструмента
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

### Основни концепции

Microsoft Foundry Agent Service разполага със следните основни концепции:

- **Агент**. Microsoft Foundry Agent Service се интегрира с Microsoft Foundry. В Microsoft Foundry, AI агентът действа като "умен" микросървис, който може да отговаря на въпроси (RAG), да извършва действия или напълно да автоматизира работни потоци. Това се постига чрез комбиниране на силата на генеративните AI модели с инструменти, които му позволяват да получи достъп и да взаимодейства с реални източници на данни. Ето един пример за агент:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    В този пример агентът е създаден с модела `gpt-4o-mini`, име `my-agent` и инструкции `You are helpful agent`. Агентът е оборудван с инструменти и ресурси за изпълнение на задачи по интерпретиране на код.

- **Поток и съобщения**. Потокът е друга важна концепция. Той представлява разговор или взаимодействие между агент и потребител. Потоците могат да се използват за проследяване на прогреса на разговор, съхраняване на контекстна информация и управление на състоянието на взаимодействието. Ето един пример за поток:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Помолете агента да изпълни работа по нишката
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Извлечете и регистрирайте всички съобщения, за да видите отговора на агента
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    В предходния код е създаден поток. След това се изпраща съобщение към потока. Чрез извикване на `create_and_process_run`, се иска от агента да извърши работа по потока. Накрая се извличат и записват съобщенията, за да се види отговорът на агента. Съобщенията показват прогреса на разговора между потребителя и агента. Важно е да се разбере, че съобщенията могат да са от различен тип като текст, изображение или файл, което означава, че работата на агента е довела например до изображение или текстов отговор. Като разработчик можете да използвате тази информация, за да обработите по-нататък отговора или да го представите на потребителя.

- **Интеграция с Microsoft Agent Framework**. Microsoft Foundry Agent Service работи безпроблемно с Microsoft Agent Framework, което означава, че можете да създавате агенти с `FoundryChatClient` и да ги разгръщате чрез Agent Service за продукционни сценарии.

**Случаи на употреба**: Microsoft Foundry Agent Service е предназначен за корпоративни приложения, които изискват сигурно, мащабируемо и гъвкаво разгръщане на AI агенти.

## Каква е разликата между тези подходи?
 
Звучи сякаш има припокриване, но има някои ключови разлики в дизайна, възможностите и целевите случаи на употреба:
 
- **Microsoft Agent Framework (MAF)**: Производствено готов SDK за създаване на AI агенти. Предоставя олекотен API за създаване на агенти с инструментално извикване, управление на разговори и интеграция с Azure идентичност.
- **Microsoft Foundry Agent Service**: Платформа и услуга за разгръщане в Microsoft Foundry за агенти. Предлага вградена свързаност с услуги като Azure OpenAI, Azure AI Search, Bing Search и изпълнение на код.
 
Все още не сте сигурни кой да изберете?

### Случаи на употреба
 
Нека видим дали можем да ви помогнем, като разгледаме някои общи случаи на употреба:
 
> В: Създавам производствени AI приложения с агенти и искам да започна бързо.
>

>О: Microsoft Agent Framework е отличен избор. Той предоставя прост, Python API чрез `FoundryChatClient`, който ви позволява да дефинирате агенти с инструменти и инструкции само с няколко реда код.

>В: Имам нужда от корпоративно ниво на разгръщане с Azure интеграции като Търсене и изпълнение на код.
>
> О: Microsoft Foundry Agent Service е най-подходящ. Това е платформа, която предоставя вградени възможности за множество модели, Azure AI Search, Bing Search и Azure Functions. Улеснява изграждането на агентите в Foundry Portal и тяхното разгръщане в мащаб.
 
> В: Все още съм объркан, просто ми дайте една опция.
>
> О: Започнете с Microsoft Agent Framework, за да изградите агентите си, и след това използвайте Microsoft Foundry Agent Service, когато трябва да ги разгръщате и мащабирате в продукция. Този подход ви позволява да итерате бързо върху логиката на агента си с ясен път към корпоративно разгръщане.
 
Нека обобщим ключовите разлики в таблица:

| Рамка | Фокус | Основни концепции | Случаи на употреба |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Олекотен SDK за агенти с извикване на инструменти | Агенти, Инструменти, Azure Идентичност | Изграждане на AI агенти, използване на инструменти, многоетапни работни потоци |
| Microsoft Foundry Agent Service | Гъвкави модели, корпоративна сигурност, генериране на код, извикване на инструменти | Модуларност, Сътрудничество, Ориентация към процеси | Сигурно, мащабируемо и гъвкаво разгръщане на AI агенти |

## Мога ли да интегрирам съществуващите инструменти от Azure екосистемата директно, или имам нужда от самостоятелни решения?


Отговорът е да, можете да интегрирате съществуващите инструменти на вашата Azure екосистема директно с Microsoft Foundry Agent Service, особено тъй като тя е изградена да работи безпроблемно с други Azure услуги. Например, можете да интегрирате Bing, Azure AI Search и Azure Functions. Има и задълбочена интеграция с Microsoft Foundry.

Microsoft Agent Framework също се интегрира с Azure услуги чрез `FoundryChatClient` и Azure идентичност, позволявайки ви да извиквате Azure услуги директно от вашите агентски инструменти.

## Примерен код

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Имате ли още въпроси за AI Agent Frameworks?

Присъединете се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да се срещнете с други учащи, да участвате в консултации и да получите отговори на въпросите си за AI агенти.

## Източници

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Предишен урок

[Въведение в AI агенти и примери за използване на агенти](../01-intro-to-ai-agents/README.md)

## Следващ урок

[Разбиране на дизайн шаблони за агентност](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->