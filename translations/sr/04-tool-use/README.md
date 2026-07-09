[![Како дизајнирати добре AI агенте](../../../translated_images/sr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Кликните на слику изнад да бисте погледали видео о овој лекцији)_

# Образац за коришћење алата

Алати су занимљиви јер омогућавају AI агентима да имају шири спектар могућности. Уместо да агент има ограничени скуп радњи које може изводити, додавањем алата, агент сада може изводити широк спектар радњи. У овом поглављу ћемо погледати Образац за коришћење алата, који описује како AI агенти могу користити специфичне алате да би постигли своје циљеве.

## Увод

У овој лекцији желимо да одговоримо на следећа питања:

- Шта је образац за коришћење алата?
- За које случајеве употребе се може применити?
- Који су елементи/грађевински блокови потребни за имплементацију овог образаца?
- Које су посебне разматрања приликом коришћења Обрасца за коришћење алата за изградњу поузданих AI агената?

## Циљеви учења

Након завршетка ове лекције, моћи ћете да:

- Дефинишете Образац за коришћење алата и његову сврху.
- Идентификујете случајеве употребе у којима је овај образац применљив.
- Разумете кључне елементе потребне за имплементацију овог образаца.
- Препознајете разматрања за обезбеђивање поузданости AI агената који користе овај образац.

## Шта је Образац за коришћење алата?

**Образац за коришћење алата** се фокусира на обезбеђивање Large Language Models (LLM) способности да интерагују са спољним алатима како би постигли одређене циљеве. Алати су код који агент може да изврши како би обавио радње. Алат може бити једноставна функција као што је калкулатор, или позив API-ја треће стране као што је проналажење цене акција или временска прогноза. У контексту AI агената, алати су дизајнирани да буду позивани од стране агената као одговор на **функцијске позиве генерисане моделом**.

## За које случајеве употребе се може применити?

AI агенти могу искористити алате за завршетак сложених задатака, преузимање информација или доношење одлука. Образац за коришћење алата често се користи у ситуацијама које захтевају динамичку интеракцију са спољним системима, као што су базе података, веб сервиси или интерпретатори кода. Ова способност је корисна за низ различитих случајева употребе, укључујући:

- **Динамичко преузимање информација:** Агенти могу упитати спољне API-је или базе података да би преузели ажуриране податке (нпр. упит у SQLite базу за анализу података, преузимање цена акција или информација о времену).
- **Извршавање и интерпретација кода:** Агенти могу извршавати код или скрипте за решавање математичких проблема, генерисање извештаја или обављање симулација.
- **Аутоматизација радних токова:** Аутоматизација поновљивих или вишестепених процеса интегрисањем алата као што су планери задатака, услуги за е-пошту или цевоводи за податке.
- **Корисничка подршка:** Агенти могу интераговати са CRM системима, платформама за карте или базама знања како би решили корисничке упите.
- **Генерација и уређивање садржаја:** Агенти могу користити алате као што су провера граматике, резимирање текста или процена безбедности садржаја како би помогли у задацима креирања садржаја.

## Који су елементи/грађевински блокови потребни за имплементацију образаца за коришћење алата?

Ови грађевински блокови омогућавају AI агенту да обавља широк спектар задатака. Погледајмо кључне елементе потребне за имплементацију Образаца за коришћење алата:

- **Схеме функција/алата**: Детаљни описи доступних алата, укључујући назив функције, сврху, потребне параметре и очекиване излазе. Ове шеме омогућавају LLM-у да разуме који су алати доступни и како конструисати важеће захтеве.

- **Логика извршења функције**: Управља када и како се алати позивају на основу намере корисника и контекста разговора. Ово може укључивати модуле за планирање, механизме рутирања или условне токове који динамички одређују коришћење алата.

- **Систем за управљање порукама**: Компоненте које управљају током разговора између уноса корисника, одговора LLM-а, позива алата и излаза алата.

- **Оквир за интеграцију алата**: Инфраструктура која повезује агента са различитим алатима, било да су то једноставне функције или сложени спољни сервиси.

- **Обрада грешака и валидација**: Механизми за руковање неуспесима у извршењу алата, валидацију параметара и управљање неочекиваним одговорима.

- **Управљање стањем**: Праћење контекста разговора, претходних интеракција са алатима и трајних података како би се обезбедила конзистентност током вишекратних интеракција.

Следеће, погледајмо позив функција/алата детаљније.
 
### Позив функције/алата

Позив функције је примарни начин којим омогућавамо Large Language Models (LLM) да интерагују са алатима. Често ћете видети да се „Функција“ и „Алат“ користе наизменично јер су „функције“ (блокови поново употребљивог кода) „алати“ које агенти користе за извршавање задатака. Да би код функције био позван, LLM мора упоредити кориснички захтев са описом функције. За то се шаље шема која садржи описе свих доступних функција LLM-у. LLM затим бира најприкладнију функцију за задатак и враћа њено име и аргументе. Изабрана функција се позива, њен одговор се шаље назад LLM-у, који користи те информације да одговори на захтев корисника.

Да би програмери имплементирали позив функција за агенте, потребно је:

1. LLM модел који подржава позив функција
2. Шема која садржи описе функција
3. Код за сваку описану функцију

За илустрацију, користићемо пример добијања тренутног времена у граду:

1. **Иницијализујте LLM који подржава позив функција:**

    Ни модели не подржавају увек позив функција, па је важно проверити да ли LLM који користите то ради. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> подржава позив функција. Можемо почети иницијализовањем OpenAI клијента према Azure OpenAI **Responses API-ју** (стабилни `/openai/v1/` крајња тачка — није потребна `api_version`).

    ```python
    # Иницијализујте OpenAI клијента за Azure OpenAI (Responses API, v1 крајња тачка)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Креирање шеме функције**:

    Следеће ћемо дефинисати JSON шему која садржи име функције, опис шта функција ради и имена и описе параметара функције.
    Затим ћемо ову шему проследити претходно креираном клијенту, заједно са корисничким захтевом да се нађе време у Сан Франциску. Важно је напоменути да се као резултат враћа **позив алата**, а **не** коначни одговор на питање. Као што је раније поменуто, LLM враћа име функције коју је изабрао за задатак и аргументе који ће јој бити прослеђени.

    ```python
    # Опис функције за модел за читање (одговори АПИ формата алата наравно)
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

    # Први API позив: Затражите од модела да користи функцију
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API враћа позиве алата као function_call ставке у response.output.
    # Додајте их у разговор да би модел имао потпун контекст у следећем кораку.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Код функције потребан за извршење задатка:**

    Сада када је LLM изабрао коју функцију треба покренути, код који спроводи задатак мора бити имплементиран и извршен.
    Можемо имплементирати код за добијање тренутног времена у Python-у. Такође ћемо написати код за вађење имена и аргумената из response_message ради добијања коначног резултата.

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

    # Други позив API-ју: Добијте коначни одговор од модела
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

Позив функција је у срцу већине, ако не и свих, дизајна коришћења алата агената, међутим имплементација од нуле понекад може бити изазовна.
Како смо научили у [Лекцији 2](../../../02-explore-agentic-frameworks), агентски оквири нам пружају већ састављене грађевинске блокове за имплементацију коришћења алата.
 
## Примери коришћења алата са агентским оквирима

Ево неколико примера како можете имплементирати Образац за коришћење алата користећи различите агентске оквире:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> је open-source AI оквир за изградњу AI агената. Он поједностављује процес коришћења позива функција омогућавајући вам да дефинишете алате као Python функције са `@tool` декоратером. Оквир управља комуникацијом напред-назад између модела и вашег кода. Такође пружа приступ унапред направљеним алатима попут Претраге фајлова и Интерпретатора кода преко `FoundryChatClient`.

Следећа дијаграм илуструје процес позива функције са Microsoft Agent Framework:

![function calling](../../../translated_images/sr/functioncalling-diagram.a84006fc287f6014.webp)

У Microsoft Agent Framework алати се definiшу као декорисане функције. Можемо претворити функцију `get_current_time` коју смо раније видели у алат користећи `@tool` декоратер. Оквир ће аутоматски сериализовати функцију и њене параметре, креирајући шему коју ће послати LLM-у.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Креирајте клијента
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Креирајте агента и покрените са алатом
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> је новији агентски оквир дизајниран да омогући програмерима да сигурно граде, имплементирају и скалирају висококвалитетне и прошириве AI агенте без потребе за управљањем основним рачунарским и складишним ресурсима. Посебно је користан за предузећа јер је потпуно управљана услуга са безбедношћу на нивоу предузећа.

У поређењу са развојем директно преко LLM API-ја, Microsoft Foundry Agent Service пружа неке предности, укључујући:

- Аутоматски позив алата – није потребно ручно парсирати позив алата, извршавати га и руковати одговором; све то сада ради сервер.
- Сигурно управљање подацима – уместо да управљате својим стањем разговора, можете се ослонити на тредове који чувају све потребне информације.
- Спремни алати – алати које можете користити за интеракцију са својим изворима података, као што су Bing, Azure AI Search и Azure Functions.

Алати доступни у Microsoft Foundry Agent Service могу се поделити у две категорије:

1. Алатке за знање:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Повезивање кроз Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Претрага фајлова</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Алатке за радњу:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Позив функција</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Интерпретатор кода</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI дефинисани алати</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service нам омогућава коришћење ових алата заједно као `сет алата`. Такође користи `тредове` који прате историју порука из одређеног разговора.

Замислите да сте продајни агент у компанији Contoso. Желите развити конверзацијског агента који може одговарати на питања о вашим продајним подацима.

Следећа слика илуструје како бисте могли користити Microsoft Foundry Agent Service за анализу ваших продајних података:

![Agentic Service In Action](../../../translated_images/sr/agent-service-in-action.34fb465c9a84659e.webp)

За коришћење било којег од ових алата са сервисом можемо креирати клијента и дефинисати алат или сет алата. За практичну имплементацију можемо користити следећи Python код. LLM ће моћи да погледа сет алата и одлучи да ли ће користити кориснички дефинисану функцију `fetch_sales_data_using_sqlite_query` или унапред направљени Интерпретатор кода у зависности од корисничког захтева.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # функција fetch_sales_data_using_sqlite_query која се може наћи у фајлу fetch_sales_data_functions.py.
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

## Која су посебна разматрања приликом коришћења Обрасца за коришћење алата за изградњу поузданих AI агената?

Уобичајена брига код SQL-а који LLM динамички генерише јесте безбедност, нарочито ризик од SQL инјекције или злонамерних акција, као што су брисање или манипулација базом података. Иако су ове бриге валидне, могу се ефикасно ублажити правилном конфигурацијом дозвола приступа бази података. За већину база података то подразумева конфигурисање базе као само за читање. За сервисе база као што су PostgreSQL или Azure SQL, апликацији би требало доделити улогу само за читање (SELECT).

Извођење апликације у безбедном окружењу додатно побољшава заштиту. У предузетничким сценаријима, подаци се обично извлаче и трансформишу из оперативних система у базу података или складиште података само за читање са кориснички пријатељском шемом. Овај приступ осигурава да су подаци безбедни, оптимизовани за перформансе и приступачност, и да апликација има ограничен, само за читање приступ.

## Примери кода

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Имате још питања о Образцу за коришћење алата?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) да се упознате са другим учесницима, присуствујете офис часовима и добијете одговоре на питања о AI агентима.

## Допунски извори

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Радна радионица за Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Радна радионица Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Преглед Microsoft Agent Framework</a>


## Претходна лекција

[Разумевање агенцијских дизајн образаца](../03-agentic-design-patterns/README.md)

## Следећа лекција

[Агенцијски RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->