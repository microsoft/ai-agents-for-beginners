[![Истраживање AI оквира за агенте](../../../translated_images/sr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Кликните на горњу слику да бисте погледали видео о овој лекцији)_

# Истражите AI оквире за агенте

AI оквири за агенте су софтверске платформе дизајниране да поједноставе креирање, постављање и управљање AI агентима. Ови оквири обезбеђују програмерима унапред изграђене компоненте, апстракције и алате који убрзавају развој сложених AI система.

Ови оквири помажу програмерима да се фокусирају на јединствене аспекте својих апликација пружајући стандардизоване приступе за уобичајене изазове у развоју AI агената. Они побољшавају скалабилност, приступачност и ефикасност у изградњи AI система.

## Увод

Ова лекција ће обухватити:

- Шта су AI оквири за агенте и шта омогућују програмерима да постигну?
- Како тимови могу да их користе за брзо прототиповање, итерацију и побољшање капацитета свог агента?
- Које су разлике између оквира и алата које су креирали Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> и <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Могу ли да интегришем своје постојеће алате Azure екосистема директно или ми требају самостална решења?
- Шта је Microsoft Foundry Agent Service и како ми помаже?

## Циљеви учења

Циљеви ове лекције су да вам помогну да разумете:

- Улогу AI оквира за агенте у развоју AI.
- Како искористити AI оквире за агенте да бисте изградили интелигентне агенте.
- Кључне могућности које омогућавају AI оквири за агенте.
- Разлике између Microsoft Agent Framework и Microsoft Foundry Agent Service.

## Шта су AI оквири за агенте и шта омогућавају програмерима?

Традиционални AI оквири вам могу помоћи да интегришете AI у своје апликације и учините их бољим на следеће начине:

- **Персонализација**: AI може да анализира понашање и преференције корисника и пружи персонализоване препоруке, садржај и искуства.
Пример: Услуге стриминга попут Netflix користе AI да предложе филмове и емисије на основу историје гледања, повећавајући ангажман и задовољство корисника.
- **Аутоматизација и ефикасност**: AI може да аутоматизује понављајуће задатке, поједностави токове рада и побољша оперативну ефикасност.
Пример: Апликације за корисничку подршку користе AI чатботове за обраду често постављаних упита, смањујући време одговора и ослобађајући људске агенте за сложеније проблеме.
- **Побољшано корисничко искуство**: AI може побољшати укупно искуство корисника пружајући интелигентне функције као што су препознавање гласа, обрада природног језика и предиктивни текст.
Пример: Виртуални асистенти као што су Siri и Google Assistant користе AI за разумевање и одговор на гласовне команде, олакшавајући корисницима интеракцију са уређајима.

### Све то звучи одлично, зашто нам онда треба AI оквир за агенте?

AI оквири за агенте представљају нешто више од обичних AI оквира. Они су дизајнирани да омогуће креирање интелигентних агената који могу да интерагују са корисницима, другим агентима и окружењем како би остварили одређене циљеве. Ови агенти могу показивати аутономно понашање, доносити одлуке и прилагодити се променљивим условима. Погледајмо неке кључне могућности које омогућавају AI оквири за агенте:

- **Сарадња и координација агената**: Омогућавају креирање више AI агената који могу заједно радити, комуницирати и координисати се да реше сложене задатке.
- **Аутоматизација и управљање задацима**: Обезбеђују механизме за аутоматизацију више корака у току рада, делегирање задатака и динамичко управљање задацима између агената.
- **Контекстуално разумевање и прилагођавање**: Опремају агенте способношћу да разумеју контекст, прилагођавају се променљивом окружењу и доносе одлуке засноване на информацијама у реалном времену.

Дакле, у резимеу, агенти вам дозвољавају да урадите више, да подигнете аутоматизацију на виши ниво, да креирате интелигентније системе који се могу прилагодити и учити из свог окружења.

## Како брзо прототиповати, итеративно унапређивати и побољшавати капацитете агента?

Ово је брзо развијајући се простор, али постоје неке ствари заједничке за већину AI оквира за агенте које вам могу помоћи да брзо направите прототип и итерацију, а то су модуларне компоненте, колективни алати и учење у реалном времену. Хајде да их погледамо:

- **Користите модуларне компоненте**: AI SDK-ови нуде унапред изграђене компоненте као што су AI и меморијски конектори, позив функција путем природног језика или додатака кода, шаблони упита и још много тога.
- **Искоришћавајте колективне алате**: Дизајнирајте агенте са специфичним улогама и задацима, омогућавајући им да тестирају и унапређују колаборативне токове рада.
- **Учите у реалном времену**: Имплементирајте петље повратних информација где агенти уче из интеракција и динамички прилагођавају своје понашање.

### Користите модуларне компоненте

SDK-ови као Microsoft Agent Framework нуде унапред изграђене компоненте као што су AI конектори, дефиниције алата и управљање агентима.

**Како тимови могу користити ово**: Тимови могу брзо саставити ове компоненте да направе функционалан прототип без почињања од нуле, што омогућава брзо експериментисање и итерацију.

**Како то функционише у пракси**: Можете користити унапред изграђени парсер за екстракцију информација из корисничког уноса, меморијски модул за чување и проналажење података, као и генератор упита за интеракцију са корисницима, све без потребе да градите ове компоненте од нуле.

**Пример кода**. Погледајмо пример како можете користити Microsoft Agent Framework са `FoundryChatClient` да модел одговара на кориснички унос позивајући алате:

``` python
# Пример Microsoft Agent Framework у Python-у

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Дефиниши пример функције алата за резервацију путовања
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
    # Пример излаза: Ваш лет за Њујорк 1. јануара 2025. је успешно резервисан. Срећан пут! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Оно што из овог примера можете видети је како можете искористити унапред изграђени парсер да извучете кључне информације из корисничког уноса, као што су порекло, одредиште и датум захтева за резервацију лета. Овај модуларни приступ вам дозвољава да се фокусирате на логичку надоградњу.

### Искоришћавајте колективне алате

Оквири као Microsoft Agent Framework олакшавају креирање више агената који могу радити заједно.

**Како тимови могу користити ово**: Тимови могу дизајнирати агенте са специфичним улогама и задацима, омогућавајући им да тестирају и унапреде колаборативне токове рада и побољшају укупну ефикасност система.

**Како то функционише у пракси**: Можете креирати тим агената где сваки агент има специјализовану функцију, као што су дохватање података, анализа или доношење одлука. Ови агенти могу комуницирати и делити информације да би постигли заједнички циљ, као што је одговор на кориснички упит или завршetak задатка.

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

# Агента за преузимање података
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Агента за анализу података
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Покрени агенте секвенцијално на задатку
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

У претходном коду видите како можете креирати задатак у коме више агената ради заједно на анализи података. Сваки агент обавља специфичну функцију, а задатак се извршава координацијом агената како би се постигао жељени резултат. Креирањем посвећених агената са специјализованим улогама, можете побољшати ефикасност и перформансе задатка.

### Учење у реалном времену

Напредни оквири пружају могућности за разумевање контекста и прилагођавање у реалном времену.

**Како тимови могу користити ово**: Тимови могу имплементирати петље повратних информација где агенти уче из интеракција и динамички прилагођавају своје понашање, што води ка континуираном унапређењу и дорађивању капацитета.

**Како то функционише у пракси**: Агенти могу анализирати повратне информације корисника, податке из околине и резултате зададка да ажурирају своју базу знања, прилагођавају алгоритме доношења одлука и побољшавају перформансе током времена. Овај итеративни процес учења омогућава агентима да се прилагоде променљивим условима и преференцијама корисника, повећавајући укупну ефикасност система.

## Које су разлике између Microsoft Agent Framework и Microsoft Foundry Agent Service?

Постоји много начина за поређење ових приступа, али хајде да погледамо неке кључне разлике у погледу њиховог дизајна, могућности и циљних случајева употребе:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework пружа поједностављени SDK за изградњу AI агената користећи `FoundryChatClient`. Омогућава програмерима да креирају агенте који користе Azure OpenAI моделе са уграђеним позивом алата, управљањем разговором и сигурношћу на нивоу предузећа путем Azure идентитета.

**Примене**: Изградња AI агената спремних за производњу са употребом алата, више корака у токовима рада и сценарије интеграције на нивоу предузећа.

Ево неких важних основних концепата Microsoft Agent Framework:

- **Агенти**. Агент се креира преко `FoundryChatClient` и конфигурише са именом, инструкцијама и алатима. Агент може:
  - **Обрадити корисничке поруке** и генерисати одговоре користећи Azure OpenAI моделе.
  - **Аутоматски позивати алате** на основу контекста разговора.
  - **Одржавати стање разговора** кроз више интеракција.

  Ево резјака кода који показује како креирати агента:

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

- **Алате**. Оквир подржава дефинисање алата као Python функција које агент може аутоматски позивати. Алате се региструју приликом креирања агента:

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

- **Координација више агената**. Можете креирати више агената са различитим специјалностима и координисати њихов рад:

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

Microsoft Foundry Agent Service је новији додатак, представљен на Microsoft Ignite 2024. Омогућава развој и постављање AI агената са флексибилнијим моделима, као што је директан позив отворених LLM као што су Llama 3, Mistral и Cohere.

Microsoft Foundry Agent Service пружа јаче механизме безбедности на нивоу предузећа и методе складиштења података, што га чини погодним за предузетничке апликације.

Ради одмах у складу са Microsoft Agent Framework за изградњу и постављање агената.

Ова услуга је тренутно у Јавној претпреми и подржава Python и C# за изградњу агената.

Користећи Microsoft Foundry Agent Service Python SDK, можемо креирати агента са алатом дефинисаним од стране корисника:

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

### Основни концепти

Microsoft Foundry Agent Service има следеће основне концепте:

- **Агент**. Microsoft Foundry Agent Service интегрише се са Microsoft Foundry. У оквиру Microsoft Foundry, AI агент делује као „паметна“ микросервисна јединица која може одговарати на питања (RAG), извршавати акције или у потпуности аутоматизовати токове рада. Постиже то комбинујући снагу генеративних AI модела са алатима који му омогућавају приступ и интеракцију са стварним изворима података. Ево примера агента:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    У овом примеру агент је креиран са моделом `gpt-5-mini`, именом `my-agent` и упутствима `You are helpful agent`. Агент је опремљен алатима и ресурсима за обављање задатака тумачења кода.

- **Нит и поруке**. Нит је још један важан концепт. Представља разговор или интеракцију између агента и корисника. Нити се могу користити за праћење напретка разговора, чување контекстуалних информација и управљање стањем интеракције. Ево примера нити:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Замолите агента да обави рад на нити
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Преузмите и евидентирајте све поруке да бисте видели одговор агента
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    У претходном коду креирана је нит. Након тога је послата порука нити. Позивањем `create_and_process_run`, агента се тражи да изврши рад на нитима. На крају се поруке преузимају и евидентирају како би се видели одговори агента. Поруке указују на напредак разговора између корисника и агента. Такође је важно разумети да поруке могу бити различитих типова као што су текст, слика или датотека, јер је рад агената резултирао, на пример, сликом или текстуалним одговором. Као програмер, затим можете користити те информације за даљу обраду одговора или његову презентацију кориснику.

- **Интеграција са Microsoft Agent Framework**. Microsoft Foundry Agent Service беспрекорно ради са Microsoft Agent Framework-ом, што значи да можете креирати агенте користећи `FoundryChatClient` и постављати их преко Agent Service за производне сценарије.

**Примене**: Microsoft Foundry Agent Service је дизајниран за предузетничке апликације које захтевају сигурно, скалабилно и флексибилно постављање AI агената.

## Која је разлика између ових приступа?
 
Чини се да постоји преклапање, али постоје неке кључне разлике у погледу дизајна, могућности и циљних случајева употребе:
 
- **Microsoft Agent Framework (MAF)**: Производно спреман SDK за изградњу AI агената. Пружа поједностављен API за креирање агената са позивом алата, управљањем разговором и интеграцијом Azure идентитета.
- **Microsoft Foundry Agent Service**: Платформа и услуга за постављање у Microsoft Foundry за агенте. Пружа уграђену повезаност са услугама као што је Azure OpenAI, Azure AI Search, Bing Search и извршавање кода.
 
Још увек нисте сигурни који да одаберете?

### Случајеви употребе
 
Погледајмо ако вам можемо помоћи проласком кроз неке уобичајене случајеве употребе:
 
> П: Изградим производне AI агент апликације и желим да брзо почнем
>

>О: Microsoft Agent Framework је одличан избор. Пружа једноставан, питхонички API преко `FoundryChatClient` који вам омогућава да дефинишете агенте са алатима и упутствима у само неколико линија кода.

>П: Треба ми постављање на нивоу предузећа са Azure интеграцијама као што су Search и извршење кода
>
> О: Microsoft Foundry Agent Service је најбољи избор. То је платформа која пружа уграђене могућности за више модела, Azure AI Search, Bing Search и Azure Functions. Лако је изградити ваше агенте у Foundry порталу и поставити их на скали.
 
> П: Још увек сам збуњен, само ми дајте једну опцију
>
> О: Почните са Microsoft Agent Framework за изградњу агената, а затим користите Microsoft Foundry Agent Service када требате да их поставите и скалирате у производњи. Овај приступ вам омогућава брзу итерацију логике агената уз јасан пут ка постављању на нивоу предузећа.
 
Хајде да резимирамо кључне разлике у табели:

| Оквир | Фокус | Основни концепти | Случајеви употребе |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Пoједностављени SDK за агенте са позивом алата | Агенти, Алате, Azure идентитет | Изградња AI агената, коришћење алата, више корака у токовима рада |
| Microsoft Foundry Agent Service | Флексибилни модели, безбедност на нивоу предузећа, генерисање кода, позив алата | Модуларност, сарадња, оркестрација процеса | Сигурно, скалабилно и флексибилно постављање AI агената |

## Могу ли да интегришем своје постојеће алате Azure екосистема директно или ми требају самостална решења?


Одговор је да, можете интегрисати ваше постојеће Azure алате директно са Microsoft Foundry Agent Service, посебно јер је направљен да беспрекорно ради са другим Azure сервисима. На пример, могли бисте интегрисати Bing, Azure AI Search и Azure Functions. Постоји и дубока интеграција са Microsoft Foundry.

Microsoft Agent Framework такође интегрише Azure сервисе преко `FoundryChatClient` и Azure идентификације, омогућавајући вам да позивате Azure сервисе директно из ваших агентских алата.

## Примери кода

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Имате још питања о AI Agent Frameworks?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) где можете упознати друге учеснике, присуствовати канцеларијским часовима и добити одговоре на ваша питања о AI агентима.

## Референце

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Претходна лекција

[Увод у AI Агенте и употребу агената](../01-intro-to-ai-agents/README.md)

## Следећа лекција

[Разумевање агентских дизајн образаца](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->