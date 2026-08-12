[![Изследване на рамки за AI агенти](../../../translated_images/bg/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Кликнете върху горното изображение, за да гледате видео на този урок)_

# Изследване на рамки за AI агенти

Рамките за AI агенти са софтуерни платформи, предназначени да улеснят създаването, разгръщането и управлението на AI агенти. Тези рамки предоставят на разработчиците предварително изградени компоненти, абстракции и инструменти, които опростяват разработката на сложни AI системи.

Тези рамки помагат на разработчиците да се съсредоточат върху уникалните аспекти на своите приложения, като предоставят стандартизирани подходи към общите предизвикателства при разработката на AI агенти. Те повишават мащабируемостта, достъпността и ефективността при изграждането на AI системи.

## Въведение 

Този урок ще обхване:

- Какво представляват рамките за AI агенти и какво позволяват на разработчиците да постигнат?
- Как екипите могат да ги използват за бързо прототипиране, итерация и подобряване на възможностите на своя агент?
- Какви са разликите между рамките и инструментите, създадени от Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> и <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Мога ли да интегрирам директно съществуващите инструменти от екосистемата на Azure, или ми трябват самостоятелни решения?
- Какво представлява Microsoft Foundry Agent Service и как ми помага?

## Учебни цели

Целите на този урок са да ви помогнат да разберете:

- Ролята на рамките за AI агенти в развитието на AI.
- Как да използвате рамки за AI агенти за изграждане на интелигентни агенти.
- Ключовите възможности, които рамките за AI агенти предоставят.
- Разликите между Microsoft Agent Framework и Microsoft Foundry Agent Service.

## Какво представляват рамките за AI агенти и какво позволяват на разработчиците да правят?

Традиционните AI рамки могат да ви помогнат да интегрирате AI в приложенията си и да ги подобрите по следните начини:

- **Персонализация**: AI може да анализира поведението и предпочитанията на потребителите, за да предложи персонализирани препоръки, съдържание и преживявания.
Пример: Услуги за стрийминг като Netflix използват AI, за да предложат филми и предавания въз основа на историята на гледане, което повишава ангажираността и удовлетвореността на потребителите.
- **Автоматизация и ефективност**: AI може да автоматизира повтарящи се задачи, оптимизира работните потоци и подобрява оперативната ефективност.
Пример: Приложения за обслужване на клиенти използват AI чатботове за обработка на често задавани въпроси, намалявайки времето за отговор и освобождавайки човешки агенти за по-сложни въпроси.
- **Подобрено потребителско изживяване**: AI може да подобри общото потребителско изживяване чрез интелигентни функции като разпознаване на глас, обработка на естествен език и предсказуем текст.
Пример: Виртуални асистенти като Siri и Google Assistant използват AI, за да разбират и реагират на гласови команди, което улеснява взаимодействието на потребителите с устройствата им.

### Звучи страхотно, нали? Защо тогава имаме нужда от рамка за AI агенти?

Рамките за AI агенти представляват нещо повече от просто AI рамки. Те са предназначени да позволят създаването на интелигентни агенти, които могат да взаимодействат с потребители, други агенти и средата, за да постигнат конкретни цели. Тези агенти могат да проявяват автономно поведение, да вземат решения и да се адаптират към променящи се условия. Нека разгледаме някои ключови възможности, които осигуряват рамките за AI агенти:

- **Сътрудничество и координация между агенти**: Позволява създаването на множество AI агенти, които могат да работят заедно, да комуникират и координират, за да решат сложни задачи.
- **Автоматизация и управление на задачи**: Осигурява механизми за автоматизиране на многократни стъпки в работни потоци, делегиране и динамично управление на задачи между агентите.
- **Контекстуално разбиране и адаптация**: Оборудва агентите с възможността да разбират контекста, да се адаптират към променящи се среди и да вземат решения на база информация в реално време.

В обобщение, агентите ви позволяват да правите повече, да издигнете автоматизацията на следващо ниво и да създадете по-интелигентни системи, които могат да се адаптират и учат от своята среда.

## Как бързо да прототипирате, итерате и подобрите възможностите на агента?

Това е бързо развиваща се област, но има някои общи характеристики в повечето рамки за AI агенти, които могат да ви помогнат бързо да прототипирате и итерате, а именно модулни компоненти, инструменти за сътрудничество и обучение в реално време. Нека разгледаме тези:

- **Използване на модулни компоненти**: AI SDK предлагат предварително изградени компоненти като AI и паметни конектори, извикване на функции чрез естествен език или плъгини за код, шаблони за подсказки и др.
- **Използване на сътруднически инструменти**: Проектирайте агенти с конкретни роли и задачи, позволяващи им да тестват и усъвършенстват съвместни работни потоци.
- **Обучение в реално време**: Внедрете обратни връзки, при които агентите учат от взаимодействия и динамично коригират поведението си.

### Използване на модулни компоненти

SDK като Microsoft Agent Framework предлагат предварително изградени компоненти като AI конектори, дефиниции на инструменти и управление на агенти.

**Как екипите могат да ги използват**: Екипите могат бързо да сглобят тези компоненти, за да създадат функционален прототип без да започват от нулата, позволявайки бързи експерименти и итерации.

**Как работи на практика**: Можете да използвате предварително изградения парсър за извличане на информация от потребителски вход, модул за памет за съхранение и извличане на данни и генератор на подсказки за взаимодействие с потребители, всичко това без да е необходимо да изграждате тези компоненти от нулата.

**Пример с код**. Нека разгледаме пример за това как можете да използвате Microsoft Agent Framework с `FoundryChatClient` за осъществяване на отговор на модел чрез извикване на инструменти:

``` python
# Пример на Microsoft Agent Framework на Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Дефинирайте примерна функция за инструмент за резервация на пътуване
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

Както виждате в този пример, можете да използвате предварително изграден парсър за извличане на ключова информация от потребителски вход, като начална точка, крайна точка и дата на заявка за резервация на полет. Този модулен подход ви позволява да се съсредоточите върху логиката на високо равнище.

### Използване на сътруднически инструменти

Рамки като Microsoft Agent Framework улесняват създаването на множество агенти, които могат да работят заедно.

**Как екипите могат да ги използват**: Екипите могат да проектират агенти с конкретни роли и задачи, позволявайки им да тестват и усъвършенстват съвместни работни потоци и да подобрят цялостната ефективност на системата.

**Как работи на практика**: Можете да създадете екип от агенти, като всеки агент има специализирана функция, като извличане на данни, анализ или вземане на решения. Тези агенти могат да комуникират и споделят информация, за да постигнат обща цел, като отговор на потребителски въпрос или изпълнение на задача.

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

# Агента за извличане на данни
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Агента за анализ на данни
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Стартирайте агентите последователно за изпълнение на задача
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Както виждате в предишния код, можете да създадете задача, включваща няколко агенти, които работят заедно за анализ на данни. Всеки агент изпълнява конкретна функция, а задачата се осъществява чрез координиране на агентите за постигане на желания резултат. Създавайки посветени агенти с специализирани роли, можете да подобрите ефективността и производителността на задачите.

### Обучение в реално време

Разширените рамки предоставят възможности за разбиране на контекст в реално време и адаптация.

**Как екипите могат да ги използват**: Екипите могат да внедрят обратни връзки, при които агентите учат от взаимодействия и динамично коригират поведението си, водейки до непрекъснато подобрение и усъвършенстване на възможностите.

**Как работи на практика**: Агентите могат да анализират потребителска обратна връзка, данни за околната среда и резултати от задачи, за да актуализират своята база знания, да коригират алгоритми за вземане на решения и да подобрят производителността с течение на времето. Този итеративен процес на учене позволява на агентите да се адаптират към променящи се условия и потребителски предпочитания, повишавайки цялостната ефективност на системата.

## Какви са разликите между Microsoft Agent Framework и Microsoft Foundry Agent Service?

Има много начини да се сравнят тези подходи, но нека разгледаме някои ключови разлики по отношение на тяхното проектиране, възможности и целеви случаи на използване:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework предоставя оптимизиран SDK за изграждане на AI агенти с помощта на `FoundryChatClient`. Той позволява на разработчиците да създават агенти, които използват модели на Azure OpenAI с вградена функционалност за извикване на инструменти, управление на разговори и корпоративна сигурност чрез Azure идентичност.

**Случаи на използване**: Създаване на AI агенти за продукция с използване на инструменти, многоредови работни потоци и корпоративна интеграция.

Ето някои важни основни концепции на Microsoft Agent Framework:

- **Агенти**. Агентът се създава чрез `FoundryChatClient` и се конфигурира с име, инструкции и инструменти. Агентът може:
  - **Да обработва потребителски съобщения** и да генерира отговори, използвайки модели на Azure OpenAI.
  - **Автоматично да извиква инструменти** в зависимост от контекста на разговора.
  - **Да поддържа състоянието на разговора** през множество взаимодействия.

  Ето откъс от код, показващ как да се създаде агент:

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

- **Инструменти**. Рамката поддържа дефиниране на инструменти като Python функции, които агентът може да извиква автоматично. Инструментите се регистрират при създаването на агента:

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

- **Координация между множество агенти**. Можете да създавате множество агенти със специализации и да координирате работата им:

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

- **Интеграция с Azure идентичност**. Рамката използва `AzureCliCredential` (или `DefaultAzureCredential`) за сигурна автентикация без ключ, елиминирайки нуждата от управление на API ключове директно.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service е по-ново допълнение, представено на Microsoft Ignite 2024. То позволява разработка и разгръщане на AI агенти с по-гъвкави модели, като директно извикване на отворени LLM модели като Llama 3, Mistral и Cohere.

Microsoft Foundry Agent Service осигурява по-силни механизми за корпоративна сигурност и методи за съхранение на данни, което го прави подходящ за корпоративни приложения.

Работи веднага с Microsoft Agent Framework за създаване и разгръщане на агенти.

Тази услуга в момента е в публичен преглед и поддържа Python и C# за изграждане на агенти.

Използвайки Python SDK на Microsoft Foundry Agent Service, можем да създадем агент с потребителски дефиниран инструмент:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Дефиниране на функции за инструменти
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

### Основни концепции

Microsoft Foundry Agent Service има следните основни концепции:

- **Агент**. Microsoft Foundry Agent Service се интегрира с Microsoft Foundry. В рамките на Microsoft Foundry, AI агентът действа като „умен“ микросървис, който може да отговаря на въпроси (RAG), да извършва действия или да автоматизира напълно работни потоци. Това се постига чрез съчетаване на мощността на генеративните AI модели с инструменти, които му позволяват да достъпва и взаимодейства с реални източници на данни. Ето пример за агент:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    В този пример, агентът е създаден с модела `gpt-5-mini`, име `my-agent` и инструкции `You are helpful agent`. Агентът е оборудван с инструменти и ресурси за изпълнение на задачи по тълкуване на код.

- **Тема и съобщения**. Темата е друга важна концепция. Тя представя разговор или взаимодействие между агент и потребител. Темите могат да се използват за проследяване на напредъка на разговора, съхранение на контекстна информация и управление на състоянието на взаимодействието. Ето пример за тема:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Помолете агента да извърши работа по нишката
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Вземете и запишете всички съобщения, за да видите отговора на агента
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    В предишния код, тема е създадена. След това се изпраща съобщение към темата. С извикване на `create_and_process_run`, на агента е зададена работа по темата. Накрая съобщенията се извличат и записват, за да се види отговорът на агента. Съобщенията указват напредъка на разговора между потребителя и агента. Важно е също да се разбере, че съобщенията могат да бъдат с различни типове като текст, изображение или файл — тоест работата на агентите е довела например до изображение или текстов отговор. Като разработчик, можете да използвате тази информация за допълнителна обработка или визуализация пред потребителя.

- **Интеграция с Microsoft Agent Framework**. Microsoft Foundry Agent Service работи безпроблемно с Microsoft Agent Framework, което означава, че можете да изграждате агенти с `FoundryChatClient` и да ги разгръщате чрез Agent Service за производствени сценарии.

**Случаи на използване**: Microsoft Foundry Agent Service е предназначен за корпоративни приложения, които изискват сигурно, мащабируемо и гъвкаво разгръщане на AI агенти.

## Каква е разликата между тези подходи?
 
Изглежда, че има припокриване, но има някои ключови разлики по отношение на проектирането им, възможностите и целевите случаи на използване:
 
- **Microsoft Agent Framework (MAF)**: Готов за производство SDK за изграждане на AI агенти. Предоставя оптимизиран API за създаване на агенти с извикване на инструменти, управление на разговори и интеграция с Azure идентичност.
- **Microsoft Foundry Agent Service**: Платформа и услуга за разгръщане в Microsoft Foundry за агенти. Предлага вградена свързаност към услуги като Azure OpenAI, Azure AI Search, Bing Search и изпълнение на код.
 
Още не сте сигурни кой да изберете?

### Случаи на използване
 
Нека да видим дали можем да ви помогнем, като разгледаме някои често срещани случаи:
 
> В: Изграждам производствени AI агент приложения и искам да започна бързо
>

>О: Microsoft Agent Framework е отличен избор. Той предоставя прост, Python стил API чрез `FoundryChatClient`, който ви позволява да дефинирате агенти с инструменти и инструкции само с няколко реда код.

>В: Имам нужда от корпоративно разгръщане с интеграции в Azure като Search и изпълнение на код
>
> О: Microsoft Foundry Agent Service е най-подходящият. Това е платформа, която предоставя вградени възможности за множество модели, Azure AI Search, Bing Search и Azure Functions. Лесно е да изградите агентите си в портала Foundry и да ги разгръщате в мащаб.
 
> В: Все още съм объркан, просто ми дайте един избор
>
> О: Започнете с Microsoft Agent Framework за изграждане на агентите си, а след това използвайте Microsoft Foundry Agent Service, когато имате нужда да ги разгръщате и мащабирате в продукция. Този подход ви позволява бързо да итерате върху логиката на агента, като имате ясен път към корпоративното разгръщане.
 
Нека обобщим ключовите разлики в таблица:

| Рамка | Фокус | Основни концепции | Случаи на използване |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Оптимизиран SDK за агенти с извикване на инструменти | Агенти, Инструменти, Azure идентичност | Изграждане на AI агенти, използване на инструменти, многоредови работни потоци |
| Microsoft Foundry Agent Service | Гъвкави модели, корпоративна сигурност, генериране на код, извикване на инструменти | Модулност, Сътрудничество, Оркестрация на процеси | Сигурно, мащабируемо и гъвкаво разгръщане на AI агенти |

## Мога ли да интегрирам директно съществуващите инструменти от екосистемата на Azure, или ми трябват самостоятелни решения?


Отговорът е да, можете да интегрирате съществуващите инструменти от екосистемата на Azure директно с Microsoft Foundry Agent Service, особено тъй като тя е изградена да работи безпроблемно с други Azure услуги. Например, можете да интегрирате Bing, Azure AI Search и Azure Functions. Съществува и дълбока интеграция с Microsoft Foundry.

Microsoft Agent Framework също се интегрира с Azure услугите чрез `FoundryChatClient` и Azure идентичност, което ви позволява да извиквате Azure услуги директно от инструментите на вашия агент.

## Примерни кодове

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Имаш ли още въпроси за AI Agent Frameworks?

Присъедини се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да се срещнеш с други учащи, да участваш в офис часове и да получиш отговори на въпросите си относно AI агентите.

## Референции

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Предишен урок

[Въведение в AI агентите и случаи на използване на агенти](../01-intro-to-ai-agents/README.md)

## Следващ урок

[Разбиране на агентни дизайни модели](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->