[![Изследване на рамките за AI агенти](../../../translated_images/bg/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Кликнете върху изображението по-горе, за да гледате видеото на този урок)_

# Изследване на рамките за AI агенти

Рамките за AI агенти са софтуерни платформи, създадени да опростят създаването, внедряването и управлението на AI агенти. Тези рамки предоставят на разработчиците предварително създадени компоненти, абстракции и инструменти, които улесняват разработването на сложни AI системи.

Тези рамки помагат на разработчиците да се съсредоточат върху уникалните аспекти на своите приложения, като предоставят стандартизирани подходи към общи предизвикателства при разработката на AI агенти. Те повишават мащабируемостта, достъпността и ефективността при изграждането на AI системи.

## Въведение

Този урок ще обхване:

- Какво са рамките за AI агенти и какво позволяват на разработчиците да постигнат?
- Как екипите могат да използват тези рамки за бързо прототипиране, итерация и подобряване на възможностите на агентите си?
- Какви са разликите между рамките и инструментите, създадени от Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> и <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Мога ли да интегрирам директно съществуващите си инструменти от Azure екосистемата или ми трябват независими решения?
- Какво е Microsoft Foundry Agent Service и как това ми помага?

## Цели на обучението

Целите на този урок са да ви помогнат да разберете:

- Ролята на рамките за AI агенти в разработката на AI.
- Как да използвате рамките за AI агенти за изграждане на интелигентни агенти.
- Основните възможности, които позволяват рамките за AI агенти.
- Разликите между Microsoft Agent Framework и Microsoft Foundry Agent Service.

## Какво са рамките за AI агенти и какво позволяват на разработчиците да направят?

Традиционните AI рамки могат да ви помогнат да интегрирате AI в приложенията си и да ги направят по-добри по следните начини:

- **Персонализация**: AI може да анализира поведението и предпочитанията на потребителите, за да предоставя персонализирани препоръки, съдържание и изживявания.
Пример: Услуги за стрийминг като Netflix използват AI, за да предлагат филми и предавания на база историята на гледане, подобрявайки ангажирането и удовлетворението на потребителите.
- **Автоматизация и ефективност**: AI може да автоматизира повтарящи се задачи, оптимизира работните потоци и подобрява оперативната ефективност.
Пример: Приложения за обслужване на клиенти използват чатботове с AI за обработка на често задавани въпроси, намалявайки времето за отговор и освобождавайки човешки агенти за по-сложни случаи.
- **Подобрено потребителско изживяване**: AI може да подобри общото потребителско изживяване чрез интелигентни функции като разпознаване на говор, обработка на естествен език и прогнозен текст.
Пример: Виртуални асистенти като Siri и Google Assistant използват AI, за да разбират и отговарят на гласови команди, улеснявайки взаимодействието с устройствата.

### Звучи чудесно, нали? Защо тогава ни е необходима рамката за AI агенти?

Рамките за AI агенти представляват нещо повече от обикновени AI рамки. Те са създадени да позволят създаването на интелигентни агенти, които могат да взаимодействат с потребители, други агенти и околната среда, за да постигнат конкретни цели. Тези агенти могат да проявяват автономно поведение, да вземат решения и да се адаптират към променящи се условия. Нека разгледаме някои ключови възможности, осигурени от рамките за AI агенти:

- **Сътрудничество и координация на агенти**: Позволява създаването на множество AI агенти, които могат да работят съвместно, да комуникират и координират изпълнението на сложни задачи.
- **Автоматизация и управление на задачи**: Осигурява механизми за автоматизиране на многостъпкови работни потоци, делегиране на задачи и динамично управление на задачи сред агентите.
- **Контекстуално разбиране и адаптация**: Дава на агентите възможност да разбират контекста, да се адаптират към променящи се условия и да вземат решения базирани на информация в реално време.

В обобщение, агентите ви позволяват да правите повече, да повдигнете автоматизацията на следващо ниво, създавайки по-интелигентни системи, които могат да се адаптират и учат от околната среда.

## Как да прототипираме бързо, да итерираме и подобряваме възможностите на агента?

Това е динамична област, но има някои общи неща в повечето рамки за AI агенти, които могат да ви помогнат бързо да прототипирате и итеративно да подобрявате — а именно модулни компоненти, съвместни инструменти и обучение в реално време. Нека разгледаме тези аспекти:

- **Използвайте модулни компоненти**: SDK-тата за AI предлагат предварително създадени компоненти като AI и Memory конектори, извикване на функции с естествен език или чрез плъгини, шаблони за заявки и др.
- **Използвайте съвместни инструменти**: Дизайнирайте агенти с конкретни роли и задачи, които да тестват и усъвършенстват съвместни работни потоци.
- **Учете в реално време**: Внедрете обратни връзки, при които агентите се учат от взаимодействията и динамично коригират поведението си.

### Използване на модулни компоненти

SDK-та като Microsoft Agent Framework предлагат предварително създадени компоненти като AI конектори, дефиниции на инструменти и управление на агенти.

**Как екипите могат да ги използват**: Екипите могат бързо да сглобят тези компоненти, за да създадат функционален прототип без да започват от нулата, позволявайки бързи експерименти и итерации.

**Как работи на практика**: Можете да използвате предварително създаден парсър за извличане на информация от входа на потребителя, модул за памет за съхранение и извличане на данни и генератор на заявки за взаимодействие с потребителите, без да строите тези компоненти от нулата.

**Примерен код**. Нека видим пример за използване на Microsoft Agent Framework с `FoundryChatClient`, за да има моделът отговор на въпроси с извикване на инструменти:

``` python
# Пример на Microsoft Agent Framework на Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Дефинирайте примерна функция на инструмент за резервация на пътуване
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

Това, което можете да видите от този пример, е как можете да използвате предварително създаден парсър за извличане на ключова информация от входа на потребителя, като произход, дестинация и дата на заявка за резервация на полет. Този модулен подход ви позволява да се фокусирате върху високониво логика.

### Използване на съвместни инструменти

Рамки като Microsoft Agent Framework улесняват създаването на множество агенти, които могат да работят съвместно.

**Как екипите могат да ги използват**: Екипите могат да създават агенти с конкретни роли и задачи, като тестват и усъвършенстват съвместни работни потоци и подобряват общата ефективност на системата.

**Как работи на практика**: Можете да създадете екип от агенти, където всеки агент има специализирана функция, като извличане на данни, анализ или вземане на решения. Тези агенти могат да комуникират и споделят информация, за да постигнат обща цел, като отговор на потребителско запитване или изпълнение на задача.

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

# Стартиране на агентите последователно за задача
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

В предния код виждате как можете да създадете задача, включваща множество агенти, които работят заедно за анализ на данни. Всеки агент изпълнява конкретна функция, а задачата се изпълнява чрез координация на агентите за постигане на желания резултат. Създаването на специализирани агенти подобрява ефективността и производителността на задачите.

### Учете в реално време

Разширените рамки предлагат възможности за контекстуално разбиране и адаптация в реално време.

**Как екипите могат да ги използват**: Екипите могат да внедрят обратни връзки, при които агентите се учат от взаимодействия и динамично коригират поведението си, което води до непрекъснато подобрение и усъвършенстване на възможностите.

**Как работи на практика**: Агентите могат да анализират обратна връзка от потребители, данни от околната среда и резултати от задачи, за да актуализират база знания, да коригират алгоритми за вземане на решения и да подобрят изпълнението си с времето. Този итеративен процес на учене позволява агентите да се адаптират към променящи се условия и потребителски предпочитания, повишавайки цялостната ефективност на системата.

## Какви са разликите между Microsoft Agent Framework и Microsoft Foundry Agent Service?

Съществуват много начини за сравнение на тези подходи, но нека погледнем някои ключови разлики по отношение на дизайн, възможности и целеви случаи на използване:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework предоставя опростен SDK за изграждане на AI агенти с помощта на `FoundryChatClient`. Той позволява на разработчиците да създават агенти, които използват Azure OpenAI модели с вградена поддръжка за извикване на инструменти, управление на разговори и корпоративна сигурност чрез Azure идентичност.

**Случаи на използване**: Изграждане на AI агенти за производство с използване на инструменти, многостъпкови работни потоци и корпоративна интеграция.

Ето някои важни основни концепции на Microsoft Agent Framework:

- **Агенти**. Агент се създава чрез `FoundryChatClient` и се конфигурира с име, инструкции и инструменти. Агентът може:
  - **Да обработва потребителски съобщения** и да генерира отговори с помощта на Azure OpenAI модели.
  - **Автоматично да извиква инструменти** в зависимост от контекста на разговора.
  - **Да поддържа състоянието на разговора** в множество взаимодействия.

  Ето откъс от код, показващ как се създава агент:

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

- **Координация на множество агенти**. Можете да създавате множество агенти с различни специализации и да координирате тяхната работа:

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

- **Интеграция с Azure идентичност**. Рамката използва `AzureCliCredential` (или `DefaultAzureCredential`) за сигурна автентикация без ключове, като премахва необходимостта от управление на API ключове.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service е по-нова услуга, представена на Microsoft Ignite 2024. Тя позволява разработка и внедряване на AI агенти с по-гъвкави модели, като директно извикване на отворени LLM модели като Llama 3, Mistral и Cohere.

Microsoft Foundry Agent Service предоставя по-силни механизми за корпоративна сигурност и методи за съхранение на данни, което я прави подходяща за корпоративни приложения.

Тя работи директно с Microsoft Agent Framework за изграждане и внедряване на агенти.

Тази услуга в момента е в публичен преглед и поддържа Python и C# за изграждане на агенти.

С помощта на Python SDK за Microsoft Foundry Agent Service можем да създадем агент с потребителски дефиниран инструмент:

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

### Основни концепции

Microsoft Foundry Agent Service има следните основни концепции:

- **Агент**. Microsoft Foundry Agent Service се интегрира с Microsoft Foundry. В Microsoft Foundry AI агентът действа като „умен“ микросървис, който може да отговаря на въпроси (RAG), да изпълнява действия или изцяло да автоматизира работни потоци. Това се постига чрез съчетаване на мощта на генеративни AI модели с инструменти, позволяващи достъп и взаимодействие с реални източници на данни. Ето пример за агент:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    В този пример агентът се създава с модел `gpt-4.1-mini`, име `my-agent` и инструкции `You are helpful agent`. Агентът е оборудван с инструменти и ресурси за изпълнение на задачи по тълкуване на код.

- **Тема и съобщения**. Темата е друга важна концепция. Тя представлява разговор или взаимодействие между агент и потребител. Темите могат да се използват за проследяване на прогреса на разговора, съхраняване на контекстна информация и управление на състоянието на взаимодействието. Ето пример за тема:

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

    В предишния код се създава тема. След това се изпраща съобщение към темата. Чрез извикване на `create_and_process_run` агентът се подтиква да работи по темата. Накрая съобщенията се извличат и регистрират, за да се види отговорът на агента. Съобщенията показват напредъка на разговора между потребителя и агента. Важно е също да се разбере, че съобщенията могат да са от различни типове като текст, изображение или файл, което означава, че работата на агента е довела до, например, изображение или текстов отговор. Като разработчик можете да използвате тази информация за по-нататъшна обработка или представяне на отговора на потребителя.

- **Интеграция с Microsoft Agent Framework**. Microsoft Foundry Agent Service работи безпроблемно с Microsoft Agent Framework, което означава, че можете да изграждате агенти използвайки `FoundryChatClient` и да ги внедрявате чрез Agent Service в производствени среди.

**Случаи на използване**: Microsoft Foundry Agent Service е предназначена за корпоративни приложения, които изискват сигурно, мащабируемо и гъвкаво внедряване на AI агенти.

## Коя е разликата между тези подходи?
 
Звучи сякаш има припокриване, но има някои ключови разлики по отношение на дизайн, възможности и целеви случаи на използване:
 
- **Microsoft Agent Framework (MAF)**: SDK, готов за производство, за изграждане на AI агенти. Предлага опростен API за създаване на агенти с извикване на инструменти, управление на разговори и интеграция с Azure идентичност.
- **Microsoft Foundry Agent Service**: Платформа и услуга за внедряване в Microsoft Foundry за агенти. Предлага вградена свързаност със услуги като Azure OpenAI, Azure AI Search, Bing Search и изпълнение на код.
 
Още не сте сигурни кого да изберете?

### Примери за използване
 
Нека видим дали можем да ви помогнем, като разгледаме някои често срещани случаи на използване:
 
> Въпрос: Изграждам продукционни AI приложения с агенти и искам да започна бързо
>

>Отговор: Microsoft Agent Framework е чудесен избор. Той предоставя прост, Python-ориентиран API чрез `FoundryChatClient`, който ви позволява да дефинирате агенти с инструменти и инструкции само с няколко реда код.

>Въпрос: Нужно ми е корпоративно внедряване с интеграции в Azure като Search и изпълнение на код
>
> Отговор: Microsoft Foundry Agent Service е най-подходяща. Това е платформа и услуга с вградени възможности за множество модели, Azure AI Search, Bing Search и Azure Functions. Позволява ви лесно да изграждате агенти в Foundry портал и да ги внедрявате мащабируемо.
 
> Въпрос: Все още съм объркан, просто ми дайте един вариант
>
> Отговор: Започнете с Microsoft Agent Framework за изграждане на вашите агенти, след което използвайте Microsoft Foundry Agent Service, когато трябва да ги внедрите и мащабирате в производство. Този подход ви позволява бързо да итерате върху логиката на агента си, като имате ясен път към корпоративно внедряване.
 
Нека обобщим ключовите разлики в таблица:

| Рамка | Фокус | Основни концепции | Случаи на използване |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Опростен агент SDK с извикване на инструменти | Агенти, Инструменти, Azure идентичност | Изграждане на AI агенти, използване на инструменти, многостъпкови работни потоци |
| Microsoft Foundry Agent Service | Гъвкави модели, корпоративна сигурност, генериране на код, извикване на инструменти | Модуларност, Сътрудничество, Оркестрация на процеси | Сигурно, мащабируемо и гъвкаво внедряване на AI агенти |

## Мога ли да интегрирам директно съществуващите си инструменти от Azure екосистемата или ми трябват независими решения?


Отговорът е да, можете да интегрирате съществуващите си инструменти от екосистемата на Azure директно с Microsoft Foundry Agent Service, особено тъй като е създаден да работи безпроблемно с други Azure услуги. Например можете да интегрирате Bing, Azure AI Search и Azure Functions. Също така има дълбока интеграция с Microsoft Foundry.

Microsoft Agent Framework също се интегрира с Azure услуги чрез `FoundryChatClient` и Azure идентичност, позволявайки ви да извиквате Azure услуги директно от вашите агентски инструменти.

## Примерни кодове

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Имаш още въпроси за AI Agent Frameworks?

Присъедини се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да се срещнеш с други учащи, да посетиш консултации и да получиш отговори на въпросите си за AI агенти.

## Референции

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Предишен урок

[Въведение в AI Агенти и случаи на използване на агенти](../01-intro-to-ai-agents/README.md)

## Следващ урок

[Разбиране на агентните дизайнерски модели](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->