[![Како дизајнирати добре AI агенте](../../../translated_images/sr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Кликните на слику изнад да бисте погледали видео о овој лекцији)_

# Образац за коришћење алата

Алатке су занимљиве јер омогућавају AI агентима да имају шири спектар способности. Уместо да агент има ограничен скуп радњи које може да изврши, додавањем алата, агент сада може да обавља широк спектар радњи. У овом поглављу ћемо погледати Образац за коришћење алата, који описује како AI агенти могу користити специфичне алате да би постигли своје циљеве.

## Увод

У овој лекцији желимо да одговоримо на следећа питања:

- Шта је образац за коришћење алата?
- За које случајеве употребе се може применити?
- Који су елементи/грађевински блокови потребни за имплементацију образца?
- Које посебне мере треба предузети приликом коришћења Обрасца за коришћење алата за изградњу поузданих AI агената?

## Циљеви учења

Након завршетка ове лекције, моћи ћете да:

- Дефинишете Образац за коришћење алата и његову сврху.
- Идентификујете случајеве употребе где је Образац за коришћење алата применљив.
- Разумете кључне елементе потребне за имплементацију образца.
- Препознате мере за обезбеђење поузданости AI агената који користе овај образац.

## Шта је Образац за коришћење алата?

**Образац за коришћење алата** фокусиран је на то да Large Language Models (LLM) омогући интеракцију са спољним алатима како би постигли специфичне циљеве. Алати су код који агент може извршити да би обавио радње. Алат може бити једноставна функција као што је калкулатор, или позив API-ју треће стране попут претраживања цена акција или временске прогнозе. У контексту AI агената, алати су дизајнирани да буду извршени од стране агената као одговор на **функцијске позиве генерисане моделом**.

## За које случајеве употребе се може применити?

AI агенти могу користити алате за обављање сложених задатака, прикупљање информација или доношење одлука. Образац за коришћење алата се често користи у сценаријима који захтевају динамичку интеракцију са спољним системима као што су базе података, веб сервиси или тумачи кода. Ова способност је корисна за бројне различите случајеве употребе укључујући:

- **Динамичко прикупљање информација:** Агенти могу упитати спољне API-је или базе података ради прикупљања ажурираних података (нпр. упит у SQLite базу података за анализу података, прикупљање цена акција или временских информација).
- **Извршавање и тумачење кода:** Агенти могу извршавати код или скрипте за решавање математичких проблема, генерисање извештаја или извођење симулација.
- **Аутоматизација радних токова:** Аутоматизација понављајућих или вишестепених радних токова интеграцијом алата као што су планирачи задатака, услуге е-поште или податковни цевоводи.
- **Корисничка подршка:** Агенти могу комуницирати са CRM системима, платформама за тикете или базама знања ради решавања корисничких упита.
- **Генерисање и уређивање садржаја:** Агенти могу користити алате као што су провера граматике, резимирање текста или процена безбедности садржаја за помоћ при креирању садржаја.

## Који су елементи/грађевински блокови потребни за имплементацију обрасца коришћења алата?

Ови грађевински блокови омогућавају AI агенту да изврши широк спектар задатака. Погледајмо кључне елементе неопходне за имплементацију Обрасца за коришћење алата:

- **Шеме функција/алата**: Детаљни описи доступних алата, укључујући име функције, сврху, потребне параметре и очекиване излазне вредности. Ове шеме омогућавају LLM-у да разуме које алате има на располагању и како да формира валидне захтеве.

- **Логика извршења функција**: Управља када и како се алати позивају у зависности од корисникове намере и контекста разговора. Ово може обухватати модуле за планирање, механизме усмеравања или условне токове који динамички одређују коришћење алата.

- **Систем за руковање порукама**: Компоненте које управљају током разговора између уноса корисника, одговора LLM-а, позива алата и излаза из алата.

- **Оквир за интеграцију алата**: Инфраструктура која повезује агента са разним алатима, било да су то једноставне функције или комплексне спољне услуге.

- **Обрада грешака и валидација**: Механизми за руковање неуспесима у извршењу алата, валидацију параметара и управљање неочекиваним одговорима.

- **Управљање стањем**: Праћење контекста разговора, претходних интеракција са алатима и постојаних података како би се обезбедила конзистентност кроз више рунда интеракције.

Следеће, погледајмо позив функција/алата детаљније.
 
### Позив функција/алата

Позив функција је примарни начин на који омогућавамо Large Language Models (LLM) да интерагују са алатима. Често ћете видети да се речима 'Функција' и 'Алат' користе наизменично јер су 'функције' (блокови поновно употребљивог кода) 'алати' које агенти користе за извршавање задатака. Да би се код функције позвао, LLM мора упоредити кориснички захтев са описом функције. За то се шаље шема која садржи описе свих доступних функција LLM-у. LLM затим бира најприкладнију функцију за задатак и враћа њено име и аргументе. Изабрана функција се позива, њен одговор се шаље назад LLM-у, који користи те информације да одговори на кориснички захтев.

За програмере који желе да имплементирају позив функција за агенте, потребно је:

1. LLM модел који подржава позив функција
2. Шема која садржи описе функција
3. Код за сваку описану функцију

Пример користећи добијање актуелног времена у неком граду да илуструјемо:

1. **Иницијализујте LLM који подржава позив функција:**

    Ни сви модели не подржавају позив функција, па је важно проверити да ли LLM који користите то ради. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> подржава позив функција. Можемо почети тако што ћемо покренути OpenAI клијента према Azure OpenAI **Responses API-ју** (стабилна `/openai/v1/` рута — није потребно `api_version`). 

    ```python
    # Иницијализујте OpenAI клијента за Azure OpenAI (Responses API, v1 крајња тачка)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Креирајте шему функције**:

    Затим ћемо дефинисати JSON шему која садржи име функције, опис шта функција ради, као и имена и описе параметара функције.
    Ову шему ћемо проследити клијенту креираном раније, заједно са корисничким захтевом да се пронађе време у Сан Франциску. Важно је напоменути да је **позив алата** оно што се враћа, **а не** коначни одговор на питање. Као што је раније поменуто, LLM враћа име изабране функције за задатак и аргументе који ће јој бити прослеђени.

    ```python
    # Опис функције за модел за читање (формат алата за равне одговоре API)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # Почетна порука корисника
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Први позив API-ја: Замолити модел да користи функцију
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API враћа позиве алата као function_call ставке у response.output.
    # Додајте их разговору како би модел имао пун контекст у следећем кораку.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Код функције потребан за извршење задатка:**

    Сада када је LLM изабрао коју функцију је потребно покренути, код који извршава задатак мора бити имплементиран и извршен.
    Можемо имплементирати код за добијање актуелног времена у Python-у. Такође ћемо морати написати код за извлачење имена и аргумената из response_message да бисмо добили коначан резултат.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Врати резултат алата као ставку function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Други позив API-ја: Добијање коначног одговора од модела
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Позив функција је у основи већине, ако не свих дизајна коришћења алата код агената, али имплементација од нуле понекад може бити изазовна.
Као што смо научили у [Лекцији 2](../../../02-explore-agentic-frameworks), агентски оквири нам пружају унапред изграђене грађевинске блокове за имплементацију коришћења алата.
 
## Примери коришћења алата са агентским оквирима

Ево неколико примера како можете имплементирати Образац за коришћење алата користећи различите агентске оквире:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> је отворени AI оквир за прављење AI агената. Он поједностављује процес коришћења позива функција омогућавајући дефинисање алата као Python функција са `@tool` декоратором. Оквир управља комуникацијом између модела и вашег кода. Такође пружа приступ унапред изграђеним алатима као што су File Search и Code Interpreter кроз `FoundryChatClient`.

Следећа дијаграм илуструје процес позива функција у Microsoft Agent Framework:

![function calling](../../../translated_images/sr/functioncalling-diagram.a84006fc287f6014.webp)

У Microsoft Agent Framework-у, алати су дефинисани као декорисане функције. Можемо претворити функцију `get_current_time` коју смо видели раније у алат коришћењем `@tool` декоратора. Оквир аутоматски сериализује функцију и њене параметре, креирајући шему за слање LLM-у.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Креирај клијента
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Креирај агента и покрени са алатом
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> је новији агентски оквир дизајниран да омогући програмерима сигурно креирање, имплементацију и скалирање висококвалитетних и проширивих AI агената без потребе за управљањем основним ресурсима за обраду и складиштење. Посебно је користан за предузећа јер је потпуно управљана услуга са безбедношћу на нивоу предузећа.

У поређењу са развојем директно коришћењем LLM API-ја, Microsoft Foundry Agent Service пружа неке предности, укључујући:

- Аутоматски позив алата – није потребно парсирати позив алата, позивати алат и руковати одговором; све се сада ради на серверу
- Сигурно управљани подаци – уместо да управљате својим стањем разговора, можете се ослонити на thread-ове који чувају све неопходне информације
- Спремни алати – алати које можете користити за интеракцију са вашим изворима података, као што су Bing, Azure AI Search и Azure Functions.

Алатке доступне у Microsoft Foundry Agent Service могу се поделити у две категорије:

1. Алати знања:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Одређивање са Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Претрага фајлова</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Акционе алатке:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Позив функција</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Тумач кода</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Алати дефинисани OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service нам омогућава да користимо ове алате заједно као `комплет алата`. Такође користи `thread` који прате историју порука из одређеног разговора.

Замислите да сте продајни агент у фирми Contoso. Желите да развијете разговорног агента који може одговарати на питања о вашим подацима о продаји.

Следећа слика илуструје како бисте могли користити Microsoft Foundry Agent Service за анализу података о продаји:

![Agentic Service In Action](../../../translated_images/sr/agent-service-in-action.34fb465c9a84659e.webp)

Да бисмо користили било који од ових алата са услугом, можемо креирати клијента и дефинисати алат или комплет алата. За практичну имплементацију можемо користити следећи Python код. LLM ће моћи да погледа комплет алата и одлучи да ли ће користити корисничку функцију `fetch_sales_data_using_sqlite_query` или унапред изграђени Code Interpreter, у зависности од корисничког захтева.

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

# Иницијализација алата за интерпретатор кода и додавање у сет алата.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4.1-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Које су посебне мере за коришћење Образца за коришћење алата у изградњи поузданих AI агената?

Уобичајена забринутост везана за динамички генерисани SQL од стране LLM-а је безбедност, посебно ризик од SQL инјекције или злонамерних радњи као што су брисање или модификација базе података. Иако су ове забринутости валидне, могу се ефикасно ублажити правилном конфигурацијом дозвола приступа бази података. За већину база података то укључује конфигурацију базе као само за читање. За базе као што су PostgreSQL или Azure SQL, апликацији треба доделити улогу само за читање (SELECT).

Покретање апликације у сигурном окружењу додатно појачава заштиту. У пословним сценаријима, подаци се обично извлаче и трансформишу из оперативних система у базу података само за читање или складиште података са кориснички прилагођеном шемом. Овај приступ осигурава да су подаци безбедни, оптимизовани за перформансе и приступачност, као и да апликација има ограничен приступ само за читање.

## Примери кода

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Имате ли још питања о Образцима за коришћење алата?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) да упознате друге ученике, присуствујете канцеларијским сатима и добијете одговоре на ваша питања о AI агентима.

## Додатни ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Радионца Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Радионца Contoso Creative Writer са више агената</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Преглед Microsoft Agent Framework-а</a>


## Тестирање Агента (опционо)

Након што научите како да распоредите агенте у [Lesson 16](../16-deploying-scalable-agents/README.md), можете да извршите брзо тестирање агента `TravelToolAgent` из ове лекције (дали и даље позива своје алате и одговара?) користећи [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Погледајте [`tests/README.md`](../tests/README.md) да бисте сазнали како да га покренете.

## Претходна лекција

[Разумевање агенцких дизајн шема](../03-agentic-design-patterns/README.md)

## Следећа лекција

[Агенцки RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->