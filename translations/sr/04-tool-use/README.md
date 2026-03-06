[![Како дизајнирати добре AI агенте](../../../translated_images/sr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Кликните на слику изнад да бисте погледали видео о овој лекцији)_

# Образац Дизајна коришћења алата

Алатке су занимљиве јер омогућавају AI агентима да имају шири спектар могућности. Уместо да агент има ограничен скуп радњи које може да изврши, додавањем алата, агент сада може да изврши велики број радњи. У овом поглављу ћемо погледати Образац Дизајна коришћења алата, који описује како AI агенти могу да користе одређене алате да би постигли своје циљеве.

## Увод

У овој лекцији ћемо покушати да одговоримо на следећа питања:

- Шта је образац дизајна коришћења алата?
- За које случајеве употребе се може применити?
- Који су елементи/компоненте потребни за имплементацију овог образца дизајна?
- Које посебне разматрања треба узети у обзир приликом коришћења Обрасца Дизајна коришћења алата за изградњу поузданих AI агената?

## Циљеви учења

Након завршетка ове лекције, бићете у могућности да:

- Дефинишете Образац Дизајна коришћења алата и његову сврху.
- Идентификујете случајеве употребе у којима је овај образац применљив.
- Разумете кључне елементе потребне за имплементацију овог образца дизајна.
- Препознате аспекте за обезбеђивање поузданости AI агената који користе овај образац дизајна.

## Шта је Образац дизајна коришћења алата?

**Образац дизајна коришћења алата** фокусира се на давање могућности LLM моделима да интерагују са спољним алатима како би постигли одређене циљеве. Алатке су код који агент може извршити да би извео радње. Алат може бити једноставна функција као што је калкулатор, или API позив ка сервису треће стране, као што су проналажење цена акција или временска прогноза. У контексту AI агената, алатке су дизајниране да их агенти извршавају као одговор на **позиве функција генерисане од стране модела**.

## За које случајеве употребе се може применити?

AI агенти могу користити алатке за извршење сложених задатака, преузимање информација или доношење одлука. Образац дизајна коришћења алата често се користи у сценаријима који захтевају динамичку интеракцију са спољним системима, као што су базе података, веб сервиси или интерпретатори кода. Ова могућност је корисна за бројне различите случајеве, укључујући:

- **Динамичко преузимање информација:** Агент може упитати спољне API-јеве или базе података како би преузео ажуриране податке (нпр. упитивање SQLite базе за анализу података, преузимање цена акција или временске прогнозе).
- **Извођење и тумачење кода:** Агент може извршити код или скрипте да реши математичке проблеме, генерише извештаје или спроведе симулације.
- **Аутоматизација радних токова:** Аутоматизација понављајућих или вишестепених радних процеса интеграцијом алатки као што су распореди задаћа, услуге е-поште или канали за податке.
- **Корисничка подршка:** Агент може интераговати са CRM системима, платформама за тикете или базама знања за решавање корисничких упита.
- **Генерација и уређивање садржаја:** Агент може користити алатке као што су провера граматике, резимирање текста или процена безбедности садржаја за помоћ у задацима креирања садржаја.

## Који су елементи/компоненте потребни за имплементацију обрасца коришћења алата?

Ове компоненте омогућавају AI агенту да извршава велики број задатака. Погледајмо основне елементе потребне за имплементацију Обрасца Дизајна коришћења алата:

- **Шеме функција/алатки**: Детаљни описи доступних алатки, укључујући име функције, сврху, потребне параметре и очекиване излазне вредности. Ове шеме омогућавају LLM моделу да разуме које су алатке доступне и како да конструише валидне захтеве.

- **Логика извршења функције**: Управља како и када се алатке позивају на основу намера корисника и контекста разговора. Ово може укључивати модуле за планирање, механизме рутирања или условне токове који динамички одређују коришћење алатки.

- **Систем за руковање порукама**: Компоненте које управљају током разговора између уноса корисника, одговора LLM, позива алата и резултата из алата.

- **Рамка за интеграцију алата**: Инфраструктура која повезује агента са разним алатима, било да су то једноставне функције или комплексне спољне услуге.

- **Обрада грешака и валидација**: Механизми за обраду неуспеха у извршењу алата, валидацију параметара и управљање неочекиваним одговорима.

- **Управљање стањем**: Праћење контекста разговора, претходних интеракција са алатима и трајних података ради обезбеђења конзистентности у више корака интеракције.

Следеће ћемо детаљније погледати позивање функција/алатки.

### Позивање функција/алатки

Позивање функција је главни начин на који омогућавамо Моделима Обогаћеног Језика (LLM) да интерагују са алатима. Често ћете видети да се термини „функција“ и „алат“ користе наизменично јер су „функције“ (блокови поновно употребљивог кода) алатке које агенти користе за обављање задатака. Да би се позвао кôд функције, LLM мора поредити кориснички захтев са описом функција. За то се шаље шема која садржи описе свих доступних функција LLM-у. LLM затим бира најприкладнију функцију за задатак и враћа њено име и аргументе. Изабрана функција се позива, њен одговор се шаље назад LLM-у, који користи те информације да одговори на корисников захтев.

За програмере који желе да имплементирају позивање функција за агенте, потребно је:

1. LLM модел који подржава позивање функција
2. Шема која садржи описе функција
3. Код за сваку описану функцију

Узмимо пример добијања тренутног времена у граду:

1. **Иницијализација LLM који подржава позивање функција:**

    Не подржавају сви модели позивање функција, зато је важно проверити да ли модел који користите подржава ову могућност. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> подржава позивање функција. Можемо почети иницијализацијом Azure OpenAI клијента.

    ```python
    # Иницијализујте Azure OpenAI клијента
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Креирање шеме функције**:

    Следеће ћемо дефинисати JSON шему која садржи име функције, опис шта функција ради, као и имена и описе параметара функције.
    Затим ћемо ову шему проследити клијенту креираном раније, заједно са корисничким захтевом да пронађе време у Сан Франциску. Ваžno је напоменути да је **позив алата** оно што се враћа, **не** коначан одговор на питање. Као што је раније наведено, LLM враћа име одабране функције за задатак и аргументе који ће јој бити прослеђени.

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
  
    # Први позив API-ју: Затражите од модела да користи функцију
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
  
1. **Код функције потребан за извршење задатка:**

    Сада када је LLM изабрао коју функцију треба покренути, код који извршава задатак мора бити имплементиран и покренут.
    Можемо имплементирати код за добијање тренутног времена у Питону. Такође ћемо морати написати код за извлачење имена и аргумената из response_message да бисмо добили коначни резултат.

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
     # Обрадите позиве функција
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
  
      # Други позив API-ју: Добијање коначног одговора од модела
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

Позивање функција је у сржи већине, ако не и свих, образаца коришћења алата агената, али њена имплементација од нуле понекад може бити изазовна.
Као што смо научили у [Лекцији 2](../../../02-explore-agentic-frameworks), агентски оквири нам пружају унапред саграђене компоненте за имплементацију коришћења алата.

## Примери коришћења алата са агентским оквирима

Ево неколико примера како можете имплементирати Образац Дизајна коришћења алата користећи различите агентске оквире:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> је open-source AI оквир за прављење AI агената. Поједностављује процес коришћења позивања функција тако што вам омогућава да дефинишете алатке као Питон функције са `@tool` декоратером. Оквир управља комуникацијом између модела и вашег кода. Такође пружа приступ унапред изграђеним алатима као што су претрага фајлова и интерпретатор кода преко `AzureAIProjectAgentProvider`.

Следећа шема илуструје процес позивања функција у Microsoft Agent Framework-у:

![function calling](../../../translated_images/sr/functioncalling-diagram.a84006fc287f6014.webp)

У Microsoft Agent Framework-у алатке се дефинишу као декорисане функције. Можемо претворити функцију `get_current_time` коју смо раније видели у алат тако што ћемо користити `@tool` декоратер. Оквир ће аутоматски серијализовати функцију и њене параметре, креирајући шему која се шаље LLM-у.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Направите клијента
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Направите агента и покрените са алатом
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> је новији агентски оквир дизајниран да омогући програмерима да сигурно граде, распоређују и скалирају квалитетне и прошириве AI агенте без потребе да управљају основним ресурсима за израчунавање и складиштење. Посебно је користан за корпоративне апликације јер представља потпуно управљану услугу са корпоративним степеном безбедности.

У поређењу са развојем директно помоћу LLM API-ја, Azure AI Agent Service нуди неке предности, укључујући:

- Аутоматско позивање алата – није неопходно парсирати позив алата, извршити алат и обрадити одговор; све се сада обавља на серверу
- Сигурно управљани подаци – уместо да управљате сопственим стањем разговора, можете се ослонити на „threads“ који чувају све потребне информације
- Алати спремни за употребу – Алатке које можете користити за интеракцију са изворима података, као што су Bing, Azure AI Search и Azure Functions.

Алатке доступне у Azure AI Agent Service могу се поделити у две категорије:

1. Алати за знање:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Основна потпора Bing претрагом</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Претрага фајлова</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI претрага</a>

2. Акциони алати:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Позивање функција</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Интерпретатор кода</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI дефинисани алати</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service нам омогућава да ове алатке користимо заједно као `toolset`. Такође користи `threads` који прате историју порука из одређеног разговора.

Замислите да сте продајни агент у компанији Contoso. Желите да развијете разговорног агента који може одговарати на питања у вези са вашим продајним подацима.

Следећа слика илуструје како можете користити Azure AI Agent Service да анализирате своје продајне податке:

![Agentic Service In Action](../../../translated_images/sr/agent-service-in-action.34fb465c9a84659e.webp)

Да бисте користили било који од ових алата са услугом, можете креирати клијента и дефинисати алат или скуп алата. За практичну имплементацију можете користити следећи Python код. LLM ће моћи да гледа на скуп алата и одлучи да ли ће користити кориснички креирану функцију `fetch_sales_data_using_sqlite_query` или унапред направљени интерпретатор кода, у зависности од корисничког захтева.

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

# Иницијализација скупа алата
toolset = ToolSet()

# Иницијализација агента за позивање функција са функцијом fetch_sales_data_using_sqlite_query и додавање у скуп алата
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Иницијализација алата Code Interpreter и додавање у скуп алата.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Која су посебна разматрања за коришћење Обрасца Дизајна коришћења алата за изградњу поузданих AI агената?

Честа брига у вези са динамички генерисаним SQL упитима од стране LLM модела је безбедност, посебно ризик од SQL инјекције или злонамерних акција као што су брисање или нарушавање базе података. Иако су ове бриге оправдане, могу се ефикасно ублажити правилним подешавањем права приступа бази података. За већину база то подразумева конфигурисање базе као само за читање. За базе као што су PostgreSQL или Azure SQL, апликацији треба доделити улогу само за читање (SELECT).

Покретање апликације у сигурном окружењу додатно побољшава заштиту. У корпоративним сценаријима, подаци се обично извлаче и трансформишу из оперативних система у базу података или складиште података само за читање са пријатељском шемом. Овај приступ осигурава да су подаци безбедни, оптимизовани за перформансе и приступачни, а апликација има ограничен приступ само за читање.

## Примери кода

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Имаш више питања о Обрасцима дизајна коришћења алата?

Придружите се [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) да се сретнете са другим ученима, присуствујете сату консултација и добијете одговоре на питања о AI агентима.

## Додатни ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Radionica o Azure AI Agent Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Radionica o Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Pregled Microsoft Agent Framework</a>

## Претходна лекција

[Разумевање агенцијских образаца дизајна](../03-agentic-design-patterns/README.md)

## Следећа лекција
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање одговорности**:  
Овај документ је преведен уз помоћ AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо ка прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења настала коришћењем овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->