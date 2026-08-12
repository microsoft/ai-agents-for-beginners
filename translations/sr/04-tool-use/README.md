[![Како дизајнирати добре АИ агенте](../../../translated_images/sr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Кликните на слику изнад да бисте погледали видео о овој лекцији)_

# Образац дизајна коришћења алата

Алати су занимљиви јер омогућавају АИ агентима да имају шири спектар способности. Уместо да агент има ограничен скуп радњи које може извршити, додавањем алата агент сада може извршити широк спектар радњи. У овом поглављу ћемо погледати образац дизајна коришћења алата, који описује како АИ агенти могу користити специфичне алате да би постигли своје циљеве.

## Увод

У овој лекцији покушавамо да одговоримо на следећа питања:

- Шта је образац дизајна коришћења алата?
- За које случајеве употребе се може примењивати?
- Који су елементи/грађевински блокови потребни за имплементацију овог обрасца дизајна?
- Који су посебни аспекти коришћења обрасца дизајна коришћења алата за изградњу поузданих АИ агената?

## Циљеви учења

Након завршетка ове лекције, моћи ћете да:

- Дефинишете образац дизајна коришћења алата и његову сврху.
- Препознате случајеве употребе у којима је образац дизајна коришћења алата применљив.
- Разумете кључне елементе потребне за имплементацију обрасца дизајна.
- Препознате аспекте за обезбеђивање поузданости у АИ агентима који користе овај образац дизајна.

## Шта је образац дизајна коришћења алата?

**Образац дизајна коришћења алата** фокусира се на то да ЛЛМ-овима пружи могућност интеракције са спољашњим алатима ради постизања конкретних циљева. Алати су код који агент може извршити да би обавио одређене радње. Алат може бити једноставна функција као што је калкулатор, или позив API-ја треће стране као што је претрага цене акција или прогноза времена. У контексту АИ агената, алати су дизајнирани да се извршавају од стране агената као одговор на **функцијске позиве генерисане моделом**.

## За које случајеве употребе се може применити?

АИ агенти могу користити алате за извршавање сложених задатака, прибављање информација или доношење одлука. Образац дизајна коришћења алата често се користи у сценаријима који захтевају динамичку интеракцију са спољашњим системима, као што су базе података, веб сервисима или интерпретаторима кода. Ова способност је корисна за низ различитих случајева употребе укључујући:

- **Динамичко прибављање информација:** Агенти могу упитати спољашње API-је или базе података да добију најсвежије податке (нпр. упит SQLite базе ради анализе података, прибављање цена акција или информација о времену).
- **Извршавање и тумачење кода:** Агенти могу извршити код или скрипте да реше математичке проблеме, генеришу извештаје или спроводе симулације.
- **Аутоматизација радног тока:** Аутоматизација поновљених или вишестепених радних процеса интегрисањем алата као што су планери задатака, услуге е-поште или низови обраде података.
- **Корисничка подршка:** Агенти могу интерактивно радити са CRM системима, платформама за тикете или базама знања да решавају корисничке упите.
- **Генерисање и уређивање садржаја:** Агенти могу користити алате као што су провера граматике, резимирање текста или процена безбедности садржаја да помогну у задацима креирања садржаја.

## Који су елементи/грађевински блокови потребни за имплементацију обрасца дизајна коришћења алата?

Ови грађевински блокови омогућавају АИ агенти да извршавају широк спектар задатака. Погледајмо кључне елементе потребне за имплементацију обрасца дизајна коришћења алата:

- **Шеме функција/алата**: Детаљне дефиниције доступних алата, укључујући име функције, сврху, потребне параметре и очекиване излазне вредности. Ове шеме омогућавају ЛЛМ-у да разуме које алате има на располагању и како да конструише важеће захтеве.

- **Логика извршавања функција**: Управља како и када се алати позивају на основу корисничке намере и контекста разговора. Ово може укључивати планерске модуле, механизме усмеравања или условне токове који динамички одређују употребу алата.

- **Систем за руковање порукама**: Компоненте које управљају током разговора између корисничких уноса, одговора ЛЛМ-а, позива алата и резултата алата.

- **Оквир за интеграцију алата**: Инфраструктура која повезује агента са различитим алатима, било да су то једноставне функције или сложени спољашњи сервиси.

- **Обрада грешака и валидација**: Механизми за руковање неуспесима у извршавању алата, валидацију параметара и управљање неочекиваним одговорима.

- **Управљање стањем**: Праћење контекста разговора, претходних интеракција са алатима и упорних података како би се обезбедила доследност током вишеструких корака.

Следеће ћемо детаљније погледати позивање функција/алата.
 
### Позивање функција/алата

Позивање функција је примарни начин на који омогућавамо Великим језичким моделима (ЛЛМ) да интерагују са алатима. Често ћете видети да се „функција“ и „алат“ користе наизменично јер су „функције“ (блокови поновно употребљивог кода) „алати“ које агенти користе за извршавање задатака. Да би се код функције извршио, ЛЛМ мора упоредити кориснички захтев са описом функције. За овај поступак се ЛЛМ-у шаље шема која садржи описе свих расположивих функција. ЛЛМ онда одабира најприкладнију функцију за задатак и враћа њено име и аргументе. Изабрана функција се извршава, њен одговор се шаље назад ЛЛМ-у, који користи те информације да одговори на кориснички захтев.

Да би програмери имплементирали позивање функција за агенте, потребно вам је:

1. ЛЛМ модел који подржава позивање функција
2. Шема која садржи описе функција
3. Код за сваку описану функцију

Да илуструјемо пример добијања тренутног времена у граду:

1. **Иницијализујте ЛЛМ који подржава позивање функција:**

    Ни модели не подржавају сва позивање функција, зато је важно проверити да ли ЛЛМ који користите то ради.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> подржава позивање функција. Можемо почети иницијализовањем OpenAI клијента за Azure OpenAI **Responses API** (стабилни `/openai/v1/` крајњи пут — није потребна `api_version`).

    ```python
    # Иницијализујте OpenAI клијента за Azure OpenAI (Responses API, v1 крајња тачка)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Креирајте шему функције**:

    Следеће ћемо дефинисати JSON шему која садржи име функције, опис шта функција ради, и имена и описе њених параметара.
    Затим ћемо ову шему проследити клијенту који смо раније направили, заједно са корисничким захтевом за добијање времена у Сан Франциску. Важно је напоменути да се као резултат враћа **позив алата**, **а не** коначни одговор на питање. Као што је раније поменуто, ЛЛМ враћа име функције коју је изабрао за задатак и аргументе који ће јој бити прослеђени.

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

    # Први позив API-ју: Замолите модел да користи функцију
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API враћа позиве алата као ставке function_call у response.output.
    # Додајте их у разговор како би модел имао потпун контекст у следећем кораку.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Код функције потребан за извршење задатка:**

    Сада када је ЛЛМ изабрао коју функцију треба покренути, потребно је имплементирати и извршити код који обавља задатак.
    Можемо имплементирати код за добијање тренутног времена у Питону. Такође ћемо морати написати код за извлачење имена и аргумената из response_message да бисмо добили коначан резултат.

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

                # Враћа резултат алата као ставку function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Други позив API-ју: Добија коначни одговор од модела
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

Позивање функција је у срцу већине, ако не и свих решења за коришћење алата код агената, али имплементација од нуле понекад може бити изазовна.
Као што смо научили у [Лекцији 2](../../../02-explore-agentic-frameworks) агенцијски оквири нам пружају унапред направљене грађевинске блокове за имплементацију коришћења алата.
 
## Примери коришћења алата са агенцијским оквирима

Ево неколико примера како можете имплементирати образац дизајна коришћења алата користећи различите агенцијске оквире:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> је отворени АИ оквир за изградњу АИ агената. Поједностављује процес коришћења позивања функција тако што вам омогућава да дефинишете алате као Python функције са `@tool` декоратером. Оквир управља двосмерном комуникацијом између модела и вашег кода. Такође пружа приступ унапред направљеним алатима попут претраге фајлова и интерпретатора кода преко `FoundryChatClient`.

Следећа дијаграм илуструје процес позивања функција са Microsoft Agent Framework:

![function calling](../../../translated_images/sr/functioncalling-diagram.a84006fc287f6014.webp)

У Microsoft Agent Framework-у алати су дефинисани као функције са декоратером. Можемо претворити функцију `get_current_time` коју смо раније видели у алат коришћењем декоратера `@tool`. Оквир ће аутоматски серијализовати функцију и њене параметре, креирајући шему коју ће послати ЛЛМ-у.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> је новији агенцијски оквир дизајниран да омогући програмерима да безбедно праве, распоређују и скалирају квалитетне и прошириве АИ агенте без потребе за управљањем основним рачунарским и складишним ресурсима. Посебно је користан за корпоративне апликације јер је потпуно управљана услуга са безбедношћу корпоративног нивоа.

У поређењу са развојем директно преко ЛЛМ API-ја, Microsoft Foundry Agent Service пружа неке предности, укључујући:

- Аутоматско позивање алата – не морате сами да анализирате позив алата, извршавате алат и руковате одговором; све се то сада ради на серверу
- Безбедно управљање подацима – уместо да управљате сопственим стањем разговора, можете се ослонити на 'threads' који чувају све потребне информације
- Алати спремни за употребу – Алати које можете користити за интеракцију са изворима података, као што су Bing, Azure AI Search и Azure Functions.

Алати доступни у Microsoft Foundry Agent Service могу се поделити у две категорије:

1. Алати за знање:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Поткрепа Bing претрагом</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Претрага фајлова</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Акциони алати:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Позивање функција</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Интерпретатор кода</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Алатке дефинисане OpenAPI стандардом</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service нам омогућава да ове алате користимо заједно као `toolset`. Такође користи `threads` који прате историју порука из одређеног разговора.

Замислите да сте продајни агент у компанији Contoso. Желите да развијете конверзациони агенат који може одговарати на питања о вашим продајним подацима.

Следећа слика илуструје како бисте могли користити Microsoft Foundry Agent Service за анализу ваших продајних података:

![Agentic Service In Action](../../../translated_images/sr/agent-service-in-action.34fb465c9a84659e.webp)

Да бисмо користили било који од ових алата преко сервиса, можемо креирати клијента и дефинисати алат или скуп алата. За практичну имплементацију можемо користити следећи Python код. ЛЛМ ће моћи да погледа тај скуп алата и одлучи да ли ће користити кориснички креирану функцију `fetch_sales_data_using_sqlite_query` или унапред састављени Code Interpreter у зависности од корисничког захтева.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # функција fetch_sales_data_using_sqlite_query која се може пронаћи у фајлу fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Иницијализација сета алата
toolset = ToolSet()

# Иницијализација агента за позивање функција са функцијом fetch_sales_data_using_sqlite_query и додавање исте у сет алата
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Иницијализација алата Code Interpreter и додавање истог у сет алата.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Који су посебни аспекти коришћења обрасца дизајна коришћења алата за изградњу поузданих АИ агената?

Честа брига у вези са динамички генерисаним SQL-ом од стране ЛЛМ-ова је безбедност, нарочито ризик од SQL инјекција или злонамерних радњи, као што су брисање или измена базе података. Иако су ове бриге оправдане, могу се ефикасно смањити правилном конфигурацијом дозвола приступа бази података. За већину база података то подразумева постављање базе у режим само за читање. За сервисе база као што су PostgreSQL или Azure SQL, апликацији би требало доделити улогу само за читање (SELECT).

Покретање апликације у безбедном окружењу додатно побољшава заштиту. У корпоративним сценаријима, подаци се обично извлаче и трансформишу из оперативних система у базу података или складиште за читање са пријатељским шемама. Овај приступ обезбеђује да су подаци сигурни, оптимизовани за перформансе и приступачност, и да апликација има ограничен приступ само за читање.

## Примери кода

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Имате још питања о обрасцима дизајна коришћења алата?

Придружите се [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) да се упознате са другим ученицима, учествујете у радним часовима и добијете одговоре на питања о вашим АИ агентима.

## Додатни ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Радни семинар за Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Radionica Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Преглед Microsoft Agent Framework</a>


## Основно тестирање овог агента (опционо)

Након што научите како да постављате агенте у [Лекцији 16](../16-deploying-scalable-agents/README.md), можете основно тестирати `TravelToolAgent` из ове лекције (да ли и даље позива своје алате и одговара?) помоћу [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Погледајте [`tests/README.md`](../tests/README.md) како да га покренете.

## Претходна лекција

[Разумевање агенцијских дизајн образаца](../03-agentic-design-patterns/README.md)

## Следећа лекција

[Агенцијски RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о одрицању одговорности**:
Овај документ је преведен коришћењем услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->