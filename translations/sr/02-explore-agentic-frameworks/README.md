[![Истраживање AI оквира за агенте](../../../translated_images/sr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Кликните на слику изнад да бисте погледали видео о овој лекцији)_

# Истражите AI оквире за агенте

AI оквири за агенте су софтверске платформе дизајниране да поједноставе креирање, имплементацију и управљање AI агентима. Ови оквири пружају програмерима унапред направљене компоненте, апстракције и алате који поједностављују развој сложених AI система.

Ови оквири помажу програмерима да се фокусирају на јединствене аспекте својих апликација пружајући стандардиране приступе за уобичајене изазове у развоју AI агената. Побољшавају скалабилност, приступачност и ефикасност у изградњи AI система.

## Увод

Ова лекција ће обухватити:

- Шта су AI оквири за агенте и шта омогућавају програмерима?
- Како тимови могу користити ове оквире за брзо прототиписање, итерацију и побољшање капацитета свог агента?
- Које су разлике између оквира и алата које креирају Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> и <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Могу ли директно интегрисати своје постојеће алате из Azure екосистема, или ми требају самостална решења?
- Шта је Microsoft Foundry Agent Service и како ми ово помаже?

## Цилјеви учења

Циљ ове лекције је да вам помогне да разумете:

- Улогу AI оквира за агенте у AI развоју.
- Како користити AI оквире за агенте за изградњу интелигентних агената.
- Кључне могућности које омогућавају AI оквири за агенте.
- Разлике између Microsoft Agent Framework и Microsoft Foundry Agent Service.

## Шта су AI оквири за агенте и шта омогућавају програмерима?

Традиционални AI оквири вам могу помоћи да интегришете AI у своје апликације и да их побољшате на следеће начине:

- **Персонализација**: AI може анализирати понашање и преференције корисника да пружи персонализоване препоруке, садржај и искуства.
Пример: Стриминг сервиси попут Netflix-а користе AI да предлагају филмове и емисије на основу историје гледања, повећавајући ангажовање и задовољство корисника.
- **Аутоматизација и ефикасност**: AI може аутоматизовати понављајуће задатке, поједноставити радне токове и побољшати оперативну ефикасност.
Пример: Апликације за корисничку подршку користе AI-ом покренуте чатботове за обраду уобичајених упита, смањујући време одговора и ослобађајући људске агенте за сложеније проблеме.
- **Побољшано корисничко искуство**: AI може побољшати укупно корисничко искуство пружајући интелигентне функције као што су гласовно препознавање, обрада природног језика и предиктивни текст.
Пример: Виртуелни асистенти као што су Siri и Google Assistant користе AI да разумеју и одговарају на гласовне команде, олакшавајући корисницима интеракцију са уређајима.

### Све то звучи одлично, па зашто нам онда треба AI оквир за агенте?

AI оквири за агенте представљају више од обичних AI оквира. Они су дизајнирани да омогуће креирање интелигентних агената који могу да комуницирају са корисницима, другим агентима и окружењем како би постигли специфичне циљеве. Ови агенти могу показивати аутономно понашање, доносити одлуке и прилагођавати се променљивим условима. Погледајмо неке кључне могућности које омогућавају AI оквири за агенте:

- **Сарадња и координација агената**: Омогућавају креирање више AI агената који могу радити заједно, комуницирати и координирати се како би решавали сложене задатке.
- **Аутоматизација и управљање задацима**: Пружају механизме за аутоматизацију вишестепених радних токова, делегирање задатака и динамично управљање задацима међу агентима.
- **Контекстуално разумевање и прилагођавање**: Оспособљавају агенте да разумеју контекст, прилагођавају се променљивим окружењима и доносе одлуке на основу информација у реалном времену.

Дакле, укратко, агенти вам омогућавају да постигнете више, да подигнете аутоматизацију на виши ниво, да креирате интелигентније системе који могу да се прилагођавају и уче из свог окружења.

## Како брзо да прототипирате, итератирате и побољшате капацитете агента?

Ово је динамична област, али постоје неке заједничке ствари у већини AI оквира за агенте које вам могу помоћи у брзом прототипирању и итерацији: модуларне компоненте, сараднички алати и учење у реалном времену. Погледајмо детаљније:

- **Користите модуларне компоненте**: AI SDK-ови нуде унапред направљене компоненте као што су AI и Memory конектори, позив функција користећи природни језик или додатке кода, шаблони за промптове и више.
- **Искористите сарадничке алате**: Дизајнирајте агенте са специфичним улогама и задацима, омогућавајући им да тестирају и усавршавају сарадничке радне токове.
- **Учите у реалном времену**: Имплементирајте повратне петље у којима агенти уче из интеракција и динамички прилагођавају своје понашање.

### Користите модуларне компоненте

SDK-ови као што је Microsoft Agent Framework нуде унапред направљене компоненте као што су AI конектори, дефиниције алата и управљање агентима.

**Како тимови могу ово користити**: Тимови могу брзо саставити ове компоненте како би креирали функционални прототип без потребе да почињу од нуле, омогућавајући брзо експериментисање и итерацију.

**Како ово функционише у пракси**: Можете користити унапред направљени парсер за извлачење информација из корисничког уноса, меморијски модул за складиштење и приступ подацима, и генератор промптова за интеракцију са корисницима, све без потребе да сами градите ове компоненте.

**Пример кода**. Погледајмо пример како можете користити Microsoft Agent Framework са `FoundryChatClient` да модел одговара на унос корисника позивајући алате:

``` python
# Пример Microsoft Agent Framework-а у Пајтону

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Дефиниши функцију алата за резервацију путовања
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
    # Пример излаза: Ваш лет за Њујорк 1. јануара 2025. успешно је резервисан. Срећан пут! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Оно што можете видети из овог примера је како можете искористити унапред направљени парсер да извучете кључне информације из корисничког уноса, као што су порекло, одредиште и датум захтева за резервацију лета. Ова модуларна метода вам омогућава да се фокусирате на општу логику.

### Искористите сарадничке алате

Оквири као што је Microsoft Agent Framework олакшавају креирање више агената који могу радити заједно.

**Како тимови могу ово користити**: Тимови могу дизајнирати агенте са специфичним улогама и задацима, омогућавајући им да тестирају и усавршавају сарадничке радне токове и побољшају укупну ефикасност система.

**Како ово функционише у пракси**: Можете креирати тим агената где сваки агенат има специјализовану функцију, као што је преузимање података, анализа или доношење одлука. Ови агенти могу комуницирати и делити информације како би постигли заједнички циљ, као што је одговор на кориснички упит или извршење задатка.

**Пример кода (Microsoft Agent Framework)**:

```python
# Креирање више агената који раде заједно користећи Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Агенат за преузимање података
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Агенат за анализу података
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Покрени агенте узастопно на задатку
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Оно што видите у претходном коду је како можете креирати задатак који укључује више агената који раде заједно на анализи података. Сваки агенат врши одређену функцију, а задатак се извршава координацијом агената како би се постигао жељени резултат. Креирањем посвећених агената са специјализованим улогама, можете побољшати ефикасност и перформансе задатка.

### Учење у реалном времену

Напредни оквири пружају могућности за разумевање контекста у реалном времену и прилагођавање.

**Како тимови могу ово користити**: Тимови могу имплементирати повратне петље у којима агенти уче из интеракција и динамички прилагођавају своје понашање, што доводи до континуираног побољшања и усавршавања капацитета.

**Како ово функционише у пракси**: Агенти могу анализирати повратне информације корисника, податке из окружења и резултате задатака да ажурирају своју базу знања, прилагоде алгоритме доношења одлука и временом побољшавају перформансе. Овај итеративни процес учења омогућава агентима да се прилагођавају промењивим условима и преференцама корисника, повећавајући укупну ефикасност система.

## Које су разлике између Microsoft Agent Framework и Microsoft Foundry Agent Service?

Постоји много начина да се упореде ови приступи, али погледајмо неке кључне разлике у смислу њиховог дизајна, могућности и циљних сценарија употребе:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework пружа поједностављен SDK за прављење AI агената користећи `FoundryChatClient`. Омогућава програмерима да креирају агенте који користе Azure OpenAI моделе са уграђеним позивима алата, управљањем разговором и безбедношћу на ентерпрајз нивоу преко Azure идентитета.

**Сценарији употребе**: Прављење AI агената спремних за производњу са коришћењем алата, вишестепенским радним токовима и сценаријима интеграције на ентерпрајз нивоу.

Ево неких важних основних концепата Microsoft Agent Framework:

- **Агенти**. Агент се креира преко `FoundryChatClient` и конфигурише са именом, упутствима и алатима. Агент може:
  - **Обрађивати корисничке поруке** и генерисати одговоре користећи Azure OpenAI моделе.
  - **Аутоматски позивати алате** на основу контекста разговора.
  - **Одржавати стање разговора** кроз више интеракција.

  Ево исечка кода који приказује како се креира агент:

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

- **Алати**. Оквир подржава дефинисање алата као Python функција које агент може аутоматски позивати. Алати се региструју при креирању агента:

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

- **Мулти-агентска координација**. Можете креирати више агената са различитим специјализацијама и координисати њихов рад:

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

- **Интеграција Azure идентитета**. Оквир користи `AzureCliCredential` (или `DefaultAzureCredential`) за безбедну, безкључну аутентификацију, елиминишући потребу за директним управљањем API кључевима.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service је новији додатак, представљен на Microsoft Ignite 2024. Омогућава развој и имплементацију AI агената са флексибилнијим моделима, као што је директно коришћење open-source LLM-ова попут Llama 3, Mistral и Cohere.

Microsoft Foundry Agent Service пружа јаче механизме ентерпрајз безбедности и методе складиштења података, што га чини погодним за ентерпрајз апликације.

Ради одмах са Microsoft Agent Framework за изградњу и имплементацију агената.

Ова услуга је тренутно у Јавној Превјеви и подржава Python и C# за изградњу агената.

Коришћењем Microsoft Foundry Agent Service Python SDK можемо креирати агента са кориснички дефинисаним алатом:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Дефинишите функције алата
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

### Основни концепти

Microsoft Foundry Agent Service има следеће основне концепте:

- **Агент**. Microsoft Foundry Agent Service се интегрише са Microsoft Foundry. Унутар Microsoft Foundry, AI агент функционише као „паметна“ микросервиса која може одговарати на питања (RAG), извршавати радње или у целости аутоматизовати радне токове. Ово постиже комбинацијом снаге генеративних AI модела са алатима који му омогућавају приступ и интеракцију са стварним изворима података. Ево примера агента:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    У овом примеру, агент је креиран са моделом `gpt-4o-mini`, именом `my-agent` и упутствима `You are helpful agent`. Агент је опремљен алатима и ресурсима за задатке интерпретације кода.

- **Тема и поруке**. Тема је још један важан концепт. Представља разговор или интеракцију између агента и корисника. Теме се могу користити за праћење напретка разговора, чување контекстуалних информација и управљање стањем интеракције. Ево примера теме:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Затражите од агента да обави рад на нити
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Преузмите и забележите све поруке да бисте видели агентов одговор
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    У претходном коду креирана је тема. Након тога, порука се шаље тој теми. Позивањем `create_and_process_run` тражи се да агент изврши задатак на теми. На крају, поруке се преузимају и евидентирају да би се видео агентски одговор. Поруке показују напредак разговора између корисника и агента. Такође је важно разумети да поруке могу бити различитих типова, као што су текст, слика или датотека, што значи да је агентски рад резултирао, на пример, сликом или текстуалним одговором. Као програмер, затим можете искористити те информације за даљу обраду одговора или његово приказивање кориснику.

- **Интегрише се са Microsoft Agent Framework**. Microsoft Foundry Agent Service ради беспрекорно са Microsoft Agent Framework, што значи да можете градити агенте користећи `FoundryChatClient` и имплементирати их преко Agent Service за производне сценарије.

**Сценарији употребе**: Microsoft Foundry Agent Service је дизајниран за ентерпрајз апликације које захтевају безбедну, скалабилну и флексибилну имплементацију AI агената.

## Која је разлика између ових приступа?
 
Звучи као да постоји преклапање, али постоје кључне разлике у дизајну, функционалности и циљним корисничким случајевима:
 
- **Microsoft Agent Framework (MAF)**: То је SDK спреман за производњу за градњу AI агената. Нуди поједностављен API за креирање агената са позивом алата, управљањем разговорима и интеграцијом Azure идентитета.
- **Microsoft Foundry Agent Service**: Платформа и сервис имплементације у Microsoft Foundry за агенте. Обухвата уграђену конективност према сервисима као што су Azure OpenAI, Azure AI Search, Bing Search и извршавање кода.
 
Још увек нисте сигурни који да изаберете?

### Сценарији употребе
 
Хајде да покушамо да вам помогнемо пролазећи кроз неке најчешће случајеве употребе:
 
> Питање: Правим производне AI апликације агената и желим брзо да започнем.
>

>Одговор: Microsoft Agent Framework је одличан избор. Нуди једноставан, питионичан API преко `FoundryChatClient` који вам омогућава да дефинишете агенте са алатима и упутствима у само неколико линија кода.

>Питање: Треба ми ентерпрајз имплементација са Azure интеграцијама као што су Search и извршавање кода.
>
> Одговор: Microsoft Foundry Agent Service је најбољи избор. То је платформа која пружа уграђене могућности за више модела, Azure AI Search, Bing Search и Azure Functions. Олакшава креирање ваших агената у Foundry порталу и имплементацију на великој скали.
 
> Питање: Још увек сам збуњен, пружите ми само једну опцију.
>
> Одговор: Почните са Microsoft Agent Framework да градите своје агенте, а затим користите Microsoft Foundry Agent Service када треба да их имплементирате и скалирате у производњи. Овај приступ вам омогућава брзо итеративно развијање логике агента уз јасан пут ка ентерпрајз имплементацији.
 
Хајде да сумирамо главне разлике у табели:

| Фрејмворк | Фокус | Основни концепти | Сценарији употребе |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Поједностављени SDK агената са позивима алата | Агенти, Алати, Azure идентитет | Изградња AI агената, коришћење алата, вишестепени радни токови |
| Microsoft Foundry Agent Service | Флексибилни модели, ентерпрајз безбедност, генерисање кода, позив алата | Модуларност, Сарадња, Оркестрација процеса | Безбедна, скалабилна и флексибилна имплементација AI агената |

## Могу ли директно интегрисати своје постојеће Azure екосистем алате, или ми требају самостална решења?


Одговор је да, можете директно интегрисати ваше постојеће алате из Azure екосистема са Microsoft Foundry Agent Service, посебно јер је изграђен да беспрекорно ради са другим Azure услугама. На пример, можете интегрисати Bing, Azure AI Search и Azure Functions. Постоји и дубока интеграција са Microsoft Foundry.

Microsoft Agent Framework се такође интегрише са Azure услугама преко `FoundryChatClient` и Azure идентитета, омогућавајући вам да позивате Azure услуге директно из ваших алата агената.

## Примери кода

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Имате ли још питања о AI Agent Frameworks?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) да упознате друге који уче, учествујете на радним сатима и добијете одговоре на ваша питања о AI агентима.

## Референце

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Претходна лекција

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Следећа лекција

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->