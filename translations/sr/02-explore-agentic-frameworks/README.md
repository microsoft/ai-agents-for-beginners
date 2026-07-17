[![Истраживање AI оквира за агенте](../../../translated_images/sr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Кликните на слику изнад да бисте гледали видео о овој лекцији)_

# Истражите AI оквире за агенте

AI оквири за агенте су софтверске платформе дизајниране да поједноставе креирање, развој и управљање AI агентима. Ови оквири обезбеђују програмерима унапред изграђене компоненте, апстракције и алате који убрзавају развој сложених AI система.

Ови оквири помажу програмерима да се фокусирају на јединствене аспекте својих апликација пружајући стандардизоване приступе за уобичајене изазове у развоју AI агената. Побољшавају скалабилност, приступачност и ефикасност у изградњи AI система.

## Увод

Ова лекција ће покрити:

- Шта су AI оквири за агенте и шта програмери могу постићи коришћењем истих?
- Како тимови могу да их користе за брзо прављење прототипа, итерацију и побољшање могућности свог агента?
- Које су разлике између оквира и алата креираних од стране Microsoft-а (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> и <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Могу ли директно интегрисати своје постојеће алате из Azure екосистема или ми требају самостална решења?
- Шта је Microsoft Foundry Agent Service и како ми то помаже?

## Циљеви учења

Циљеви ове лекције су да вам помогну да разумете:

- Улогу AI оквира за агенте у развоју AI.
- Како искористити AI оквире за агенте за изградњу интелигентних агената.
- Кључне могућности омогућене AI оквирима за агенте.
- Разлике између Microsoft Agent Framework и Microsoft Foundry Agent Service.

## Шта су AI оквири за агенте и шта програмери могу са њима да ураде?

Традиционални AI оквири могу вам помоћи да интегришете AI у ваше апликације и унапредите их на следеће начине:

- **Персонализација**: AI може анализирати корисничко понашање и преференције како би пружио персонализоване препоруке, садржај и искуства.
Пример: Стриминг сервис као Netflix користи AI да предлаже филмове и серије на основу историје гледања, повећавајући ангажовање и задовољство корисника.
- **Аутоматизација и ефикасност**: AI може аутоматизовати понављајуће задатке, убрзати радне токове и побољшати оперативну ефикасност.
Пример: Апликације за корисничку службу користе AI чат ботове за решавање уобичајених упита, смањујући време одговора и ослобађајући људске агенте за сложеније задатке.
- **Побољшано корисничко искуство**: AI може побољшати укупно корисничко искуство пружајући интелигентне функције као што су препознавање гласа, обрада природног језика и предиктивни текст.
Пример: Виртуални асистенти као што су Siri и Google Assistant користе AI да разумеју и одговарају на гласовне команде, олакшавајући интеракцију корисника са уређајима.

### Све то звучи сјајно, па зашто нам треба AI оквир за агенте?

AI оквири за агенте представљају нешто више од обичних AI оквира. Они су дизајнирани да омогуће креирање интелигентних агената који могу да комуницирају са корисницима, другим агентима и окружењем да би постигли специфичне циљеве. Ови агенти могу показивати аутономно понашање, доносити одлуке и прилагођавати се променљивим условима. Погледајмо неке кључне могућности које омогућују AI оквири за агенте:

- **Сарадња и координација агената**: Омогућавају креирање више AI агената који могу радити заједно, комуницирати и координисати се у решавању сложених задатака.
- **Аутоматизација и управљање задацима**: Обезбеђују механизме за аутоматизацију вишестепених радних токова, делегирање задатака и динамичко управљање задацима међу агентима.
- **Контекстуално разумевање и прилагођавање**: Опремају агенте способношћу разумевања контекста, прилагођавању променљивом окружењу и доношењу одлука на основу информација у реалном времену.

Дакле, у резимеу, агенти вам омогућавају да урадите више, да подигнете аутоматизацију на виши ниво, да креирате интелигентније системе који могу да се прилагођавају и уче из свог окружења.

## Како брзо направити прототип, итерирати и унапредити могућности агента?

Ово је динамично поље, али постоје неке заједничке ствари код већине AI оквира за агенте које могу помоћи да брзо направите прототип и итерирарате, а то су модуларне компоненте, алати за сарадњу и учење у реалном времену. Погледајмо ово детаљније:

- **Користите модуларне компоненте**: AI SDK-ови нуде унапред изграђене компоненте као што су AI и мемори конектори, позивање функција преко природног језика или код додатака, шаблоне упита и друго.
- **Искористите алате за сарадњу**: Дизајнирајте агенте са специфичним улогама и задацима, омогућавајући им да тестирају и унапређују сарадничке радне токове.
- **Учите у реалном времену**: Имплементирајте повратне петље у којима агенти уче из интеракција и динамички прилагођавају своје понашање.

### Користите модуларне компоненте

SDK-ови као што је Microsoft Agent Framework нуде унапред изграђене компоненте као што су AI конектори, дефиниције алата и управљање агентима.

**Како тимови могу да их користе**: Тимови могу брзо саставити ове компоненте како би креирали функционални прототип без почетка од нуле, омогућавајући брзу експериментацију и итерацију.

**Како функционише у пракси**: Можете користити унапред изграђени парсер за извлачење информација из корисничког уноса, меморијски модул за складиштење и пренос података и генератор упита за интеракцију са корисницима, све без потребе да градите ове компоненте од почетка.

**Пример кода**. Погледајмо пример како можете користити Microsoft Agent Framework са `FoundryChatClient` да модел одговара на кориснички унос уз позивање алата:

``` python
# Пример Microsoft Agent Framework Python-а

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Дефинишите пример функције алата за резервацију путовања
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

Оно што можете видети из овог примера је како можете искористити унапред изграђени парсер за извлачење кључних информација из корисничког уноса, као што су порекло, одредиште и датум захтева за резервацију лета. Ова модуларна метода вам омогућава да се фокусирате на логику високог нивоа.

### Искористите алате за сарадњу

Оквири као што је Microsoft Agent Framework олакшавају креирање више агената који могу радити заједно.

**Како тимови могу да их користе**: Тимови могу дизајнирати агенте са специфичним улогама и задацима, омогућавајући им да тестирају и унапређују сарадничке радне токове и побољшају укупну ефикасност система.

**Како функционише у пракси**: Можете креирати тим агената где сваки агент има специјализовану функцију, као што су приступ подацима, анализа или доношење одлука. Ови агенти могу да комуницирају и деле информације да би постигли заједнички циљ, као одговор на кориснички упит или завршетак задатка.

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

# Агенс за преузимање података
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Агенс за анализу података
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

Оно што видите у претходном коду је како можете креирати задатак који укључује сарадњу више агената у анализи података. Сваки агент обавља специфичну функцију, а задатак се извршава координацијом агената ка жељеном резултату. Креирањем посвећених агената са специјализованим улогама, можете побољшати ефикасност и перформансе задатака.

### Учење у реалном времену

Напредни оквири пружају могућности за разумевање контекста и прилагођавање у реалном времену.

**Како тимови могу да их користе**: Тимови могу имплементирати повратне петље у којима агенти уче из интеракција и динамички прилагођавају понашање, што води ка континуираном побољшању и унапређењу могућности.

**Како функционише у пракси**: Агенти могу анализирати кориснички фидбек, податке о окружењу и исходе задатака да ажурирају своју базу знања, прилагођавају алгоритме доношења одлука и побољшавају перформансе током времена. Овај итеративни процес учења омогућава агентима да се прилагођавају променљивим условима и преференцама корисника, повећавајући укупну ефикасност система.

## Које су разлике између Microsoft Agent Framework и Microsoft Foundry Agent Service?

Постоји много начина да се упореде ови приступи, али погледајмо неке кључне разлике у погледу дизајна, могућности и намењених случајева употребе:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework обезбеђује поједностављени SDK за израду AI агената коришћењем `FoundryChatClient`. Омогућава програмерима да креирају агенте који искориштавају Azure OpenAI моделе са уграђеним позивањем алата, управљањем разговором и безбедношћу предузећа преко Azure идентитета.

**Примери употребе**: Израда AI агената спремних за продукцију са коришћењем алата, вишестепеним радним токовима и интеграцијом у предузећа.

Ево неколико важних основних концепата Microsoft Agent Framework:

- **Агенти**. Агент се креира преко `FoundryChatClient` и конфигурише са именом, упутствима и алатима. Агент може:
  - **Обрађивати корисничке поруке** и генерисати одговоре користећи Azure OpenAI моделе.
  - **Аутоматски позивати алате** на основу контекста разговора.
  - **Одржавати стање разговора** кроз више интеракција.

  Ево примера кода који показује како се креира агент:

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

- **Алати**. Оквир подржава дефинисање алата као Python функција које агент може аутоматски позивати. Алати се региструју приликом креирања агента:

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

- **Координација више агената**. Можете креирати више агената са различитим специјализацијама и координисати њихов рад:

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

- **Интеграција Azure идентитета**. Оквир користи `AzureCliCredential` (или `DefaultAzureCredential`) за безбедну, безклјучну аутентификацију, елиминишући потребу за директним управљањем API кључевима.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service је новији додатак, представљен на Microsoft Ignite 2024. Он омогућава развој и постављање AI агената са флексибилнијим моделима, као што је директно позивање open-source LLM модела попут Llama 3, Mistral и Cohere.

Microsoft Foundry Agent Service пружа јаче безбедносне механизме за предузећа као и методе складиштења података, чинећи га погодним за апликације предузећа.

Ради одмах у сарадњи са Microsoft Agent Framework-ом за изградњу и постављање агената.

Овај сервис је тренутно у јавном прегледу и подржава Python и C# за израду агената.

Користећи Microsoft Foundry Agent Service Python SDK можемо креирати агента са алатом дефинисаним од стране корисника:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Дефиниши функције алата
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

### Основни концепти

Microsoft Foundry Agent Service има следеће основне концепте:

- **Агент**. Microsoft Foundry Agent Service се интегрише са Microsoft Foundry. Унутар Microsoft Foundry, AI агент делује као "паметни" микросервис који може одговарати на питања (RAG), извршавати радње или потпуно аутоматизовати радне токове. Ово постиже комбинујући снагу генеративних AI модела са алатима који му омогућавају приступ и интеракцију са стварним изворима података. Ево примера агента:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    У овом примеру, агент је креиран са моделом `gpt-4.1-mini`, именом `my-agent` и инструкцијом `You are helpful agent`. Агент је опремљен алатима и ресурсима за обављање задатака интерпретације кода.

- **Тема и поруке**. Тема је још један важан концепт. Представља разговор или интеракцију између агента и корисника. Теме се могу користити за праћење напретка разговора, чување контекстуалних информација и управљање стањем интеракције. Ево примера теме:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Затражите од агента да изврши посао на тему
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Преузмите и забележите све поруке да бисте видели одговор агента
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    У претходном коду, тема је креирана. Након тога, порука је послата теми. Позивањем `create_and_process_run` агенту се тражи да изврши рад на теми. На крају, поруке се преузимају и бележе ради прегледа одговора агента. Поруке указују на напредак разговора између корисника и агента. Важно је разумети да поруке могу бити различитих типова као што су текст, слика или фајл, што значи да је рад агента могао резултовати, на пример, сликом или текстуалним одговором. Као програмер, можете користити те информације за даљу обраду одговора или његово представљање кориснику.

- **Интеграција са Microsoft Agent Framework-ом**. Microsoft Foundry Agent Service беспрекорно сарађује са Microsoft Agent Framework-ом, што значи да можете градити агенте користећи `FoundryChatClient` и постављати их преко Agent Service за продукционе сценарије.

**Примери употребе**: Microsoft Foundry Agent Service је дизајниран за апликације предузећа које захтевају безбедно, скалабилно и флексибилно постављање AI агената.

## Која је разлика између ових приступа?
 
Заиста изгледа да постоји преклапање, али постоје неке кључне разлике у дизајну, могућностима и намењеним случајевима употребе:
 
- **Microsoft Agent Framework (MAF)**: је SDK спреман за продукцију за креирање AI агената. Обезбеђује поједностављени API за креирање агената са позивима алата, управљањем разговорима и интеграцијом Azure идентитета.
- **Microsoft Foundry Agent Service**: је платформа и сервис за постављање у Microsoft Foundry за агенте. Нуди уграђену повезаност са сервисима као што су Azure OpenAI, Azure AI Search, Bing Search и извршавање кода.
 
Још нисте сигурни који да одаберете?

### Примери употребе
 
Погледајмо да ли можемо помоћи кроз неке честе случајеве употребе:
 
> П: Изграђујем AI агент апликације спремне за продукцију и желим брз старт
>

> О: Microsoft Agent Framework је одличан избор. Обезбеђује једноставан, Python-ски API преко `FoundryChatClient` који вам омогућава да дефинишете агенте са алатима и упутствима у само неколико линија кода.

> П: Потребна ми је ентерпрајс дистрибуција са Azure интеграцијама као Search и извршење кода
>
> О: Microsoft Foundry Agent Service је најбољи избор. То је платформа која нуди уграђене могућности за више модела, Azure AI Search, Bing Search и Azure Functions. Омогућава једноставну израду ваших агената у Foundry порталу и њихово постављање у великом обиму.
 
> П: Још сам збуњен, дајте ми једну опцију
>
> О: Почните са Microsoft Agent Framework за израду ваших агената, а затим користите Microsoft Foundry Agent Service када вам треба постављање и масштабирање у продукцији. Овај приступ вам омогућава брзе итерације на логици агената уз јасан пут ка ентерпрајс дистрибуцији.
 
Резимирајмо кључне разлике у табели:

| Оквир | Фокус | Основни концепти | Примери употребе |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Поједностављени агентски SDK са позивима алата | Агенти, Алати, Azure идентитет | Изградња AI агената, коришћење алата, вишестепени радни токови |
| Microsoft Foundry Agent Service | Флексибилни модели, безбедност предузећа, генерисање кода, позив алата | Модуларност, сарадња, оркестрација процеса | Безбедно, скалабилно и флексибилно постављање AI агената |

## Могу ли директно интегрисати своје постојеће алате из Azure екосистема или ми требају самостална решења?


Одговор је да, можете интегрисати ваше постојеће Azure алате директно са Microsoft Foundry Agent Service, посебно јер је он направљен да беспрекорно ради са другим Azure сервисима. На пример, могли бисте интегрисати Bing, Azure AI Search и Azure Functions. Постоји и дубока интеграција са Microsoft Foundry.

Microsoft Agent Framework такође интегрише са Azure сервисима кроз `FoundryChatClient` и Azure идентитет, омогућавајући вам да позивате Azure сервисе директно из ваших агенских алата.

## Примери кода

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Имате још питања о AI Agent Frameworks?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) да упознате друге ученике, присуствујете office hours и добијете одговоре на ваша питања о AI агентима.

## Референце

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Претходна лекција

[Увод у AI агенте и случајеве употребе агената](../01-intro-to-ai-agents/README.md)

## Следећа лекција

[Разумевање агентних образаца дизајна](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->