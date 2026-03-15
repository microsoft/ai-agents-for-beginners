[![Истраживање оквира за AI агенте](../../../translated_images/sr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Кликните на слику изнад да бисте погледали видео о овој лекцији)_

# Истраживање оквира за AI агенте

AI фрејмворци за агенте су софтверске платформе дизајниране да поједноставе креирање, имплементацију и управљање AI агентима. Ови фрејмворци пружају програмерима унапред изграђене компоненте, апстракције и алате који убрзавају развој сложених AI система.

Ови фрејмворци помажу програмерима да се фокусирају на јединствене аспекте својих апликација пружајући стандардизоване приступе уобичајеним изазовима у развоју AI агената. Они побољшавају скалабилност, приступачност и ефикасност у изградњи AI система.

## Увод

Ова лекција ће обухватити:

- Шта су AI фрејмворци за агенте и шта омогућавају програмерима да постигну?
- Како тимови могу користити ове алате да брзо прототипирају, итеративно унапређују и побољшавају способности свог агента?
- Које су разлике између фрејмворка и алата које је креирао Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> и <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Могу ли директно интегрисати своје постојеће алате из Azure екосистема или ми требају самостална решења?
- Шта је Azure AI Agents service и како ми ово помаже?

## Циљеви учења

Циљеви ове лекције су да вам помогну да разумете:

- Улогу AI фрејмворка за агенте у развоју AI.
- Како да искористите AI фрејмворке за агенте за изградњу интелигентних агената.
- Кључне способности које омогућавају AI фрејмворци за агенте.
- Разлике између Microsoft Agent Framework и Azure AI Agent Service.

## Шта су AI фрејмворци за агенте и шта омогућавају програмерима?

Традиционални AI фрејмворци могу вам помоћи да интегришете AI у своје апликације и учините их бољим на следеће начине:

- **Персонализација**: AI може анализирати понашање и преференције корисника да би пружио персонализоване препоруке, садржај и искуства.
Пример: Стриминг сервиси попут Netflix-а користе AI да предлажу филмове и серије на основу историје гледања, повећавајући ангажовање и задовољство корисника.
- **Аутоматизација и ефикасност**: AI може аутоматизовати понављајуће задатке, поједноставити токове посла и побољшати оперативну ефикасност.
Пример: Апликације за корисничку подршку користе чатботове на бази AI-а за обраду уобичајених упита, смањујући време одговора и ослобађајући људске агенте за сложенија питања.
- **Побољшано корисничко искуство**: AI може побољшати укупно корисничко искуство пружајући интелигентне функције као што су препознавање гласа, обрада природног језика и предиктивни текст.
Пример: Виртуелни асистенти попут Siri и Google Assistant користе AI да разумеју и одговоре на гласовне команде, олакшавајући корисницима интеракцију са уређајима.

### То све звучи одлично, па зашто нам треба AI Agent Framework?

AI фрејмворци за агенте представљају више од обичних AI фрејмворка. Они су дизајнирани да омогуће креирање интелигентних агената који могу да комуницирају са корисницима, другим агентима и окружењем како би постигли специфичне циљеве. Ови агенти могу показивати аутономно понашање, доносити одлуке и прилагођавати се изменљивим условима. Погледајмо неке кључне способности које омогућавају AI фрејмворци за агенте:

- **Сарадња и координација агената**: Омогућава креирање више AI агената који могу заједно да раде, комуницирају и координишу се како би решили сложене задатке.
- **Аутоматизација и управљање задацима**: Пружа механизме за аутоматизацију вишестепених токова рада, делегирање задатака и динамичко управљање задацима међу агентима.
- **Контекстуално разумевање и прилагођавање**: Оспособљава агенте да разумеју контекст, прилагођавају се мењајућим окружењима и доносе одлуке на основу информација у реалном времену.

Дакле, укратко, агенти вам омогућавају да урадите више, да подигнете аутоматизацију на виши ниво, да креирате интелигентније системе који се могу прилагодити и учити из свог окружења.

## Како брзо прототипирати, итеративно побољшавати и унапређивати способности агента?

Ово је брзо-померајући се пејзаж, али постоје неке ствари које су заједничке за већину AI фрејмворка за агенте и које вам могу помоћи да брзо прототипирате и итеративно радите, а то су модуларне компоненте, алати за сарадњу и учење у реалном времену. Хајде да их размотримо:

- **Користите модуларне компоненте**: AI SDK-ови нуде унапред изграђене компоненте као што су AI и Memory конектори, позивање функција користећи природни језик или code plugins, шаблони за промптове и друго.
- **Искористите алате за сарадњу**: Дизајнирајте агенте са специфичним улогама и задацима, омогућавајући им да тестирају и усавршавају сарадничке токове рада.
- **Учите у реалном времену**: Имплементирајте повратне петље у којима агенти уче из интеракција и динамички прилагођавају своје понашање.

### Користите модуларне компоненте

SDK-ови као што је Microsoft Agent Framework нуде унапред изграђене компоненте као што су AI конектори, дефиниције алата и управљање агентима.

**Како тимови могу да их користе**: Тимови могу брзо саставити ове компоненте да би креирали функционални прототип без почетка од нуле, омогућавајући брзо експериментисање и итерације.

**Како то функционише у пракси**: Можете користити унапред изграђени парсер за извлачење информација из уноса корисника, модул за меморију за чување и преузимање података и генератор промпта за интеракцију са корисницима, све без потребе да градите ове компоненте од нуле.

**Пример кода**. Хајде да погледамо пример како можете користити Microsoft Agent Framework са `AzureAIProjectAgentProvider` да би модел реаговао на унос корисника позивањем алата:

``` python
# Пример Microsoft Agent Framework у Пајтону

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Дефинишите пример функције алата за резервацију путовања
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
    # Пример излаза: Ваш лет за Њујорк 1. јануара 2025. успешно је резервисан. Срећно путовање! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Оно што можете видети из овог примера је како можете искористити унапред изграђени парсер за извлачење кључних информација из уноса корисника, као што су полазиште, одредиште и датум захтева за резервацију лета. Овакв приступ омогућава да се фокусирате на логичку, вишу нивоу апликације.

### Искористите алате за сарадњу

Фрејмворци као што је Microsoft Agent Framework олакшавају креирање више агената који могу заједно да раде.

**Како тимови могу да их користе**: Тимови могу дизајнирати агенте са специфичним улогама и задацима, омогућавајући им да тестирају и усавршавају сарадничке токове рада и побољшају укупну ефикасност система.

**Како то функционише у пракси**: Можете креирати тим агената где сваки агент има специјализовану функцију, као што су прикупљање података, анализа или доношење одлука. Ови агенти могу комуницирати и делити информације да би постигли заједнички циљ, као што је одговор на кориснички упит или завршавање задатка.

**Пример кода (Microsoft Agent Framework)**:

```python
# Креирање више агената који заједно раде користећи Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Агенат за преузимање података
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Агенат за анализу података
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Покрени агенте у низу на задатку
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

У претходном коду видите како можете креирати задатак који укључује више агената који заједно анализирају податке. Свaki agent обавља одређену функцију, а задатак се извршава координирањем агената да би се постигao жељени исход. Креирањем посвећених агената са специјализованим улогама можете побољшати ефикасност и перформансе задатака.

### Учење у реалном времену

Напредни фрејмворци пружају могућности за разумевање контекста и прилагођавање у реалном времену.

**Како тимови могу да их користе**: Тимови могу имплементирати повратне петље у којима агенти уче из интеракција и динамички прилагођавају своје понашање, што води константном побољшању и усавршавању способности.

**Како то функционише у пракси**: Агенти могу анализирати повратне информације корисника, податке из окружења и резултате задатака да ажурирају своју базу знања, прилагоде алгоритме доношења одлука и временом побољшају перформансе. Ова итеративна метода учења омогућава агентима да се прилагоде променљивим условима и преференцијама корисника, повећавајући укупну ефикасност система.

## Које су разлике између Microsoft Agent Framework и Azure AI Agent Service?

Постоји много начина да се упореде ови приступи, али погледајмо неке кључне разлике у смислу дизајна, могућности и циљних случајева употребе:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework пружа поједностављен SDK за изградњу AI агената користећи `AzureAIProjectAgentProvider`. Омогућава програмерима да креирају агенте који користе Azure OpenAI моделе са уграђеним позивима алата, управљањем разговором и безбедношћу нивоа предузећа кроз Azure идентитет.

**Случајеви употребе**: Изградња AI агената спремних за продукцију са употребом алата, вишестепеним токовима рада и сценаријима интеграције у предузеће.

Ево неких важних основних концепата Microsoft Agent Framework-а:

- **Agents**. Agent се креира преко `AzureAIProjectAgentProvider` и конфигурише са именом, инструкцијама и алатима. Агент може:
  - **Обрађивати поруке корисника** и генерисати одговоре користећи Azure OpenAI моделе.
  - **Позивати алате** аутоматски на основу контекста конверзације.
  - **Одржавати стање конверзације** кроз више интеракција.

  Ево исечка кода који показује како креирати агента:

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

- **Tools**. Фрејмворк подржава дефинисање алата као Python функција које агент може аутоматски да позове. Алатке се региструју при креирању агента:

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

- **Координација више агената**. Можете креирати више агената са различитим специјализацијама и координисати њихов рад:

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

- **Интеграција Azure иденитета**. Фрејмворк користи `AzureCliCredential` (или `DefaultAzureCredential`) за сигурну, безклјучну аутентикацију, елиминишући потребу за директним управљањем API кључевима.

## Azure AI Agent Service

Azure AI Agent Service је недавнији додатак, представљен на Microsoft Ignite 2024. Омогућава развој и деплој AI агената са флексибилнијим моделима, као што је директно позивање open-source LLM-ова као што су Llama 3, Mistral и Cohere.

Azure AI Agent Service пружа јаче механизме корпоративне безбедности и методе чувања података, што га чини погодним за апликације у предузећима.

Ради одмах са Microsoft Agent Framework-ом за изградњу и деплој агената.

Ова услуга је тренутно у Public Preview и подржава Python и C# за изградњу агената.

Користећи Azure AI Agent Service Python SDK, можемо креирати агента са кориснички дефинисаним алатом:

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

Azure AI Agent Service има следеће основне концепте:

- **Agent**. Azure AI Agent Service се интегрише са Microsoft Foundry. Унутар AI Foundry-а, AI Agent функционише као „паметни“ микросервис који може да одговара на питања (RAG), извршава акције или потпуно аутоматизује токове рада. Ово остварује комбинујући снагу генеративних AI модела са алатима који му омогућавају приступ и интеракцију са реалним изворима података. Ево примера агента:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    У овом примеру, агент је креиран са моделом `gpt-4o-mini`, именом `my-agent` и инструкцијама `You are helpful agent`. Агент је опремљен алатима и ресурсима да извршава задатке тумачења кода.

- **Тред и поруке**. Тред је још један важан концепт. Представља разговор или интеракцију између агента и корисника. Тредови се могу користити за праћење напретка конверзације, чување контекстуалних информација и управљање стањем интеракције. Ево примера треда:

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

    У претходном коду креиран је тред. Након тога, порука је послата у тред. Позивањем `create_and_process_run`, агенту се тражи да изврши посао у оквиру треда. На крају, поруке се преузимају и логују да би се видео агентов одговор. Поруке указују на напредак конверзације између корисника и агента. Такође је важно разумети да поруке могу бити различитих типова као што су текст, слика или фајл, односно да рад агената може резултовати, на пример, сликом или текстуалним одговором. Као програмер, те информације можете користити за даљу обраду одговора или његово представљање кориснику.

- **Интегрише се са Microsoft Agent Framework-ом**. Azure AI Agent Service ради беспрекорно са Microsoft Agent Framework-ом, што значи да можете градити агенте користећи `AzureAIProjectAgentProvider` и распоређивати их кроз Agent Service за продукционе сценарије.

**Случајеви употребе**: Azure AI Agent Service је дизајниран за апликације у предузећима које захтевају сигурно, скалабилно и флексибилно распоређивање AI агената.

## Која је разлика између ових приступа?
 
Изгледа да постоји преклапање, али постоје неке кључне разлике у смислу дизајна, могућности и циљних случајева употребе:
 
- **Microsoft Agent Framework (MAF)**: Је SDK спреман за продукцију за изградњу AI агената. Пружа поједностављен API за креирање агената са позивима алата, управљањем конверзацијом и интеграцијом Azure идентитета.
- **Azure AI Agent Service**: Је платформа и услуга за деплој у Azure Foundry за агенте. Нуди унапред повезаност са сервисима попут Azure OpenAI, Azure AI Search, Bing Search и извршавањем кода.
 
И даље нисте сигурни који да одаберете?

### Случајеви употребе
 
Хајде да видимо да ли вам можемо помоћи проласком кроз неке уобичајене сценарије:
 
> Q: Радим на продукцијским апликацијама AI агената и желим брзо да започнем
>

>A: Microsoft Agent Framework је одличан избор. Пружа једноставан, Python-ичан API преко `AzureAIProjectAgentProvider` који вам омогућава да дефинишете агенте са алатима и инструкцијама у само неколико редова кода.

>Q: Потребно ми је деплојовање на нивоу предузећа са Azure интеграцијама попут Search и извршавања кода
>
> A: Azure AI Agent Service је најприкладнији. То је платформа која пружа уграђене могућности за више модела, Azure AI Search, Bing Search и Azure Functions. Омогућава једноставно креирање агената у Foundry Portalu и њихово распоређивање на скали.
 
> Q: Још увек сам збуњен, дајте ми само једну опцију
>
> A: Почните са Microsoft Agent Framework-ом да изградите своје агенте, а затим користите Azure AI Agent Service када будете требали да их деплојујете и скалирате у продукцији. Овај приступ вам омогућава да брзо итератe над логиком агента, а имате јасан пут до деплоја на нивоу предузећа.
 
Хајде да резимирамо кључне разлике у табели:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Поједностављен SDK за агенте са позивањем алата | Агенти, Алатке, Azure Identity | Изградња AI агената, употреба алата, вишестепени токови рада |
| Azure AI Agent Service | Флексибилни модели, корпоративна безбедност, генерисање кода, позивање алата | Модуларност, Сарадња, Оркестрација процеса | Сигурно, скалабилно и флексибилно распоређивање AI агената |

## Могу ли директно интегрисати своје постојеће Azure екосистем алате или ми требају самостална решења?
Одговор је да — можете интегрисати своје постојеће алате у Azure екосистему директно са Azure AI Agent Service, посебно зато што је он изграђен да беспрекорно сарађује са осталим Azure сервисима. На пример, можете интегрисати Bing, Azure AI Search и Azure Functions. Постоји и дубока интеграција са Microsoft Foundry.

Microsoft Agent Framework се такође интегрише са Azure сервисима преко `AzureAIProjectAgentProvider` и Azure identity, што вам омогућава да позивате Azure сервисе директно из ваших алата агента.

## Примери кода

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Имате ли још питања о оквирима за AI агенте?

Придружите се [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) да бисте се упознали са другим ученицима, присуствовали канцеларијским сатима и добили одговоре на питања о вашим AI агентима.

## Референце

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Претходна лекција

[Увод у AI агенте и случајеве употребе](../01-intro-to-ai-agents/README.md)

## Следећа лекција

[Разумевање агентских образаца дизајна](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Изјава о одрицању одговорности:
Овај документ је преведен помоћу AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да будемо тачни, имајте у виду да аутоматски преводи могу да садрже грешке или нетачности. Изворни документ на оригиналном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Нисмо одговорни за било каква неспоразумевања или погрешна тумачења која произилазе из употребе овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->