[![Како дизајнирати добре AI агенте](../../../translated_images/sr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Кликните на слику изнад да бисте погледали видео о овом лекцији)_

# Шаблон дизајна употребе алата

Алати су занимљиви јер омогућавају AI агентима да имају шири спектар функционалности. Уместо да агент има ограничен скуп акција које може извршити, додавањем алата агент сада може обављати широк спектар акција. У овом поглављу ћемо размотрити Шаблон дизајна употребе алата, који описује како AI агенти могу користити специфичне алате за постизање својих циљева.

## Увод

У овој лекцији ћемо покушати да одговоримо на следећа питања:

- Шта је шаблон дизајна употребе алата?
- На које случајеве примене се може применити?
- Који су елементи/грађевни блокови потребни за имплементацију овог шаблона дизајна?
- Које су посебне размотре у вези са употребом шаблона дизајна употребе алата за изградњу поузданих AI агената?

## Циљеви учења

Након завршетка ове лекције, моћи ћете да:

- Дефинишете Шаблон дизајна употребе алата и његову сврху.
- Идентификујете случајеве употребе где је Шаблон дизајна употребе алата применљив.
- Разумете кључне елементе потребне за имплементацију шаблона дизајна.
- Препознате размотре за обезбеђивање поузданости AI агената који користе овај шаблон дизајна.

## Шта је Шаблон дизајна употребе алата?

**Шаблон дизајна употребе алата** фокусира се на давање LLM-овима способности да интерагују са спољним алатима ради постизања специфичних циљева. Алати су код који агент може да изврши да би обавио акције. Алат може бити једноставна функција као што је калкулатор, или позив API-ја треће стране као што је проналажење цене акција или временска прогноза. У контексту AI агената, алати су дизајнирани да се извршавају од стране агената као одговор на **функцијске позиве које генерише модел**.

## На које случајеве примене се може применити?

AI агенти могу користити алате за извршавање сложених задатака, прибављање информација или доношење одлука. Шаблон дизајна употребе алата се често користи у сценаријима који захтевају динамичку интеракцију са спољним системима, као што су базе података, веб сервисе или тумачеве кода. Ова способност је корисна за бројне различите случајеве укључујући:

- **Динамичко прибављање информација:** Агенти могу упитавати спољне API-је или базе података да повуку ажуриране податке (нпр. упит у SQLite базу података за анализу података, прибављање цена акција или информација о времену).
- **Извршавање и тумачење кода:** Агенти могу извршавати код или скрипте да решавају математичке проблеме, генеришу извештаје или обављају симулације.
- **Аутоматизација радних токова:** Аутоматизација понављајућих или вишестепених радних токова интеграцијом алата као што су распореди задатака, услуге е-поште или податочни цевоводи.
- **Корисничка подршка:** Агенти могу интераговати са CRM системима, платформама за тикете или базама знања да решавају корисничке упите.
- **Генерација и уређивање садржаја:** Агенти могу користити алате као што су провера граматике, резимирање текста или процена безбедности садржаја да помогну у задацима креирања садржаја.

## Који су елементи/грађевни блокови потребни за имплементацију шаблона дизајна употребе алата?

Ови грађевни блокови омогућавају AI агенту да изврши широк спектар задатака. Погледајмо кључне елементе потребне за имплементацију Шаблона дизајна употребе алата:

- **Шеме функција/алата**: Детаљни описи доступних алата, укључујући име функције, сврху, потребне параметре и очекиване излазне вредности. Ове шеме омогућавају LLM-у да разуме које алате има на располагању и како да конструише валидне захтеве.

- **Логика извршења функције**: Управља како и када се алати позивају у зависности од намере корисника и контекста разговора. Ово може укључивати модуле планирања, механизме усмеравања или условне токове који динамички одређују употребу алата.

- **Систем руковања порукама**: Компоненте које управљају током разговора између уноса корисника, одговора LLM-а, позива алата и излаза из алата.

- **Фрејмворк за интеграцију алата**: Инфраструктура која повезује агента са различитим алатима, било да су то једноставне функције или сложени спољни сервиси.

- **Руководство грешкама и валидација**: Механизми за руковање неуспесима у извршавању алата, валидацију параметара и управљање неочекиваним одговорима.

- **Управљање стањем**: Праћење контекста разговора, претходних интеракција са алатима и перзистентних података ради обезбеђења конзистентности у вишекратним интеракцијама.

Следеће, погледајмо Позивање функција/алата детаљније.
 
### Позивање функција/алата

Позивање функција је примарни начин да омогућимо Великим Језичким Моделима (LLM) интеракцију са алатима. Често ћете видети да се термини 'функција' и 'алат' користе наизменично јер су 'функције' (блокови поновно употребљивог кода) управо 'алати' које агенти користе за извршавање задатака. Да би се код функције позвао, LLM мора упоредити кориснички захтев са описом функције. За то се шаље шема која садржи описе свих доступних функција LLM-у. Затим LLM одабира најприкладнију функцију за задатак и враћа њено име и аргументе. Изабрана функција се позива, њен одговор се шаље назад LLM-у који користи те информације да одговори на кориснички захтев.

Да би програмери имплементирали позивање функција за агенте, потребно је:

1. Модел LLM који подржава позивање функција
2. Шема која садржи описе функција
3. Код за сваку описану функцију

Користимо пример добијања тренутног времена у граду као илустрацију:

1. **Иницијализујте LLM који подржава позивање функција:**

    Ни сви модели не подржавају позивање функција, па је важно проверити да ли LLM који користите то омогућава. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> подржава позивање функција. Можемо почети иницијализацијом Azure OpenAI клијента.

    ```python
    # Иницијализујте Azure OpenAI клијента
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Креирајте шему функције**:

    Следеће ћемо дефинисати JSON шему која садржи име функције, опис шта функција ради и имена и описе параметара функције.
    Затим ћемо ову шему проследити претходно креираном клијенту, заједно са корисничким захтевом за проналажење времена у Сан Франциску. Важно је напоменути да је **позив алата** оно што се враћа, **а не** коначни одговор на питање. Као што је раније поменуто, LLM враћа име функције коју је изабрао за задатак и аргументе који ће јој бити прослеђени.

    ```python
    # Опис функције коју модел треба да прочита
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Почетна порука корисника
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Први API позив: Затражите од модела да користи функцију
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Обрадите одговор модела
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Код функције који је потребан за извршење задатка:**

    Сада када је LLM изабрао коју функцију треба покренути, потребно је имплементирати и извршити код који обавља задатак.
    Код за добијање тренутног времена можемо имплементирати у Пајтону. Такође ће бити потребно написати код за извлачење имена и аргумената из response_message ради добијања коначног резултата.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Обрада позива функција
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Други позив API-ја: Преузми коначни одговор од модела
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Позивање функција је у срцу већине, ако не и свих, дизајна употребе алата, али је имплементација од нуле понекад изазовна.
Као што смо научили у [Лекцији 2](../../../02-explore-agentic-frameworks), агентски фрејмворкови нам пружају унапред изграђене грађевне блокове за имплементацију употребе алата.
 
## Примери употребе алата са агентским фрејмворковима

Ево неколико примера како можете имплементирати Шаблон дизајна употребе алата користећи различите агентске фрејмворкове:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> је отворени AI фрејмворк за изградњу AI агената. Олакшава процес позивања функција омогућавајући вам да дефинишете алате као Пајтон функције са украсом `@tool`. Фрејмворк управља двосмерном комуникацијом између модела и вашег кода. Поред тога, пружа приступ унапред направљеним алатима као што су Претрага фајлова и Тумач кода преко `AzureAIProjectAgentProvider`.

Следећа дијаграм илуструје процес позивања функција уз Microsoft Agent Framework:

![function calling](../../../translated_images/sr/functioncalling-diagram.a84006fc287f6014.webp)

У Microsoft Agent Framework-у, алати су дефинисани као декорисане функције. Функцију `get_current_time` коју смо раније видели можемо претворити у алат користећи украс `@tool`. Фрејмворк ће аутоматски серијализовати функцију и њене параметре, креирајући шему за слање LLM-у.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Креирај клијента
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Креирај агента и покрени га са алатом
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> је новији агентски фрејмворк који је дизајниран да омогући програмерима да сигурно граде, развијају и скалирају висококвалитетне и прошириве AI агенте без потребе за управљањем подлошком ресурса за обраду и складиштење. Посебно је користан за ентерпрајз апликације пошто је у питању потпуно управљана услуга са ентерпрајз нивоом безбедности.

Упоредо са директним развојем користећи LLM API, Azure AI Agent Service пружа неколико предности, укључујући:

- Аутоматско позивање алата – није потребно парсирати позив алата, извршавати алат и руковати одговором; све то се сада ради на серверској страни
- Сигурно управљани подаци – уместо управљања сопственим стањем разговора, можете се ослонити на нитове који чувају све потребне информације
- Алати спремни за употребу – алати које можете користити за интеракцију са изворима података, као што су Bing, Azure AI Search и Azure Functions.

Алати доступни у Azure AI Agent Service могу бити подељени у две категорије:

1. Алати знања:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Оријентација коришћењем Bing претраге</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Претрага фајлова</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI претрага</a>

2. Активациони алати:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Позивање функција</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Тумач кода</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Алати дефинисани OpenAPI спецификацијом</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure функције</a>

Agent Service нам омогућава да ове алате користимо заједно као `скуп алата` (toolset). Такође користи `нитове` који прате историју порука из одређеног разговора.

Замислите да сте продајни агент у компанији названој Contoso. Желите да развијете конверзацијског агента који може одговарати на питања у вези ваших продајних података.

Следећа слика илуструје како бисте могли користити Azure AI Agent Service за анализу ваших продајних података:

![Agentic Service In Action](../../../translated_images/sr/agent-service-in-action.34fb465c9a84659e.webp)

Да бисте користили било који од ових алата са услугом, можете креирати клијента и дефинисати алат или сет алата. За практичну имплементацију, можемо користити следећи Python код. LLM ће моћи да погледа сет алата и одлучи да ли да користи корисничку функцију `fetch_sales_data_using_sqlite_query` или унапред направљени Тумач кода у зависности од захтева корисника.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # функција fetch_sales_data_using_sqlite_query која се може наћи у датотеци fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Иницијализација сета алата
toolset = ToolSet()

# Иницијализација агента за позивање функција са функцијом fetch_sales_data_using_sqlite_query и додавање у сет алата
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Иницијализација алата Code Interpreter и додавање у сет алата.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Које су посебне размотре при коришћењу Шаблона дизајна употребе алата за изградњу поузданих AI агената?

Честа брига у вези са динамички генерисаним SQL кодом од стране LLM-ова јесте безбедност, посебно ризик од SQL инјекција или злонамерних радњи као што су брисање или манипулација базом података. Иако су ове бриге валидне, могу се ефикасно ублажити правилном конфигурацијом дозвола приступа бази података. За већину база података, то подразумева подешавање базе као само за читање. За базе података као што су PostgreSQL или Azure SQL, апликацији треба доделити улогу само за читање (SELECT).

Покретање апликације у безбедном окружењу даље повећава заштиту. У ентерпрајз сценаријима, подаци се обично извлаче и трансформишу из оперативних система у базу података или складиште података подешено као само за читање са кориснички пријатељском шемом. Овај приступ осигурава да су подаци безбедни, оптимизовани за перформансе и приступачност и да апликација има ограничен приступ само за читање.

## Примери кода

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Имате још питања о Шаблонима дизајна употребе алата?

Придружите се [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) за састанке са другим ученицима, похађање канцеларијских сати и добијање одговора на ваша питања о AI агентима.

## Додатни ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Верска радионица Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer радионица са више агената</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Преглед Microsoft Agent Framework-а</a>

## Претходна лекција

[Разумевање агентских шаблона дизајна](../03-agentic-design-patterns/README.md)

## Следећа лекција
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->