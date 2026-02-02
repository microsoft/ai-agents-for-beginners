[![Како дизајнирати добре AI агенте](../../../translated_images/sr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Кликните на слику изнад да бисте гледали видео о овој лекцији)_

# Образац дизајна коришћења алата

Алатке су занимљиве зато што омогућавају AI агентима да имају шири спектар способности. Уместо да агент има ограничену листу радњи које може извршити, додавањем алата, агент сада може извршити широк спектар радњи. У овом поглављу ћемо погледати Образац дизајна коришћења алата, који описује како AI агенти могу користити специфичне алате да постигну своје циљеве.

## Увод

У овој лекцији покушавамо да одговоримо на следећа питања:

- Шта је образац дизајна коришћења алата?
- За које случајеве употребе се може применити?
- Који су елементи/градивни блокови потребни за имплементацију овог обрасца дизајна?
- Која су посебна разматрања приликом коришћења Образца дизајна коришћења алата за изградњу поузданих AI агената?

## Циљеви учења

Након завршетка ове лекције, моћи ћете да:

- Дефинишете Образац дизајна коришћења алата и његову сврху.
- Идентификујете случајеве употребе у којима се Образац дизајна коришћења алата може применити.
- Разумете кључне елементе потребне за имплементацију овог обрасца дизајна.
- Препознате разматрања за осигурање поузданости AI агената који користе овај образац дизајна.

## Шта је Образац дизајна коришћења алата?

**Образац дизајна коришћења алата** фокусира се на омогућавање LLM-овима способности да интерагују са спољним алатима како би постигли специфичне циљеве. Алати су код који агент може да изврши како би обавио радње. Алат може бити једноставна функција као што је калкулатор, или позив API-ју треће стране као што је претрага цена акција или прогноза времена. У контексту AI агената, алати су дизајнирани да буду извршени од стране агената као одговор на **функцијске позиве генерисане моделом**.

## За које случајеве употребе се може применити?

AI агенти могу користити алате да заврше сложене задатке, преузму информације или доносе одлуке. Образац дизајна коришћења алата често се користи у сценаријима која захтевају динамичку интеракцију са спољним системима, као што су базе података, веб сервиси или интерпретатори кода. Ова способност је корисна за бројне различите случајеве употребе, укључујући:

- **Динамичко преузимање информација:** Агент може упитати спољне API-је или базе података да преузме актуелне податке (нпр. упит у SQLite базу података за анализу података, преузимање цена акција или информација о времену).
- **Извршавање и тумачење кода:** Агент може извршити код или скрипте за решавање математичких проблема, генерисање извештаја или спровођење симулација.
- **Аутоматизација радних токова:** Аутоматизација понављајућих или мултистепених радних токова интеграцијом алата као што су распоређивачи задатака, услуге е-поште или цевоводи за податке.
- **Корисничка подршка:** Агент може интераговати са CRM системима, платформама за тикете или базама знања да реши корисничке упите.
- **Генерисање и уређивање садржаја:** Агент може користити алате као што су проверивачи граматике, сажимачи текста или процењивачи сигурности садржаја како би помогао у задацима креирања садржаја.

## Који су елементи/градивни блокови потребни за имплементацију обрасца коришћења алата?

Ови градивни блокови омогућавају AI агенту да изврши широк спектар задатака. Погледајмо кључне елементе потребне за имплементацију Образца дизајна коришћења алата:

- **Схеме функција/алата**: Детаљни описи доступних алата, укључујући назив функције, сврху, потребне параметре и очекиване резултате. Ове шеме омогућавају LLM-у да разуме које алате има на располагању и како да конструише валидне захтеве.

- **Логика извршења функција**: Управља како и када се алати позивају на основу корисникове намере и контекста разговора. Ово може укључивати модуле планера, механизме усмеравања или условне токове који динамички одређују употребу алата.

- **Систем руковања порукама**: Компоненте које управљају током разговора између корисничких уноса, одговора LLM-а, позива алата и одговора алата.

- **Инфраструктура интеграције алата**: Инфраструктура која повезује агента са различитим алатима, било да су то једноставне функције или сложени спољни сервиси.

- **Руководство грешкама и валидација**: Механизми за руковање неуспесима у извршењу алата, валидацију параметара и управљање неочекиваним одговорима.

- **Управљање стањем**: Праћење контекста разговора, претходних интеракција са алатима и перзистентних података да се осигура конзистентност током вишеструких кругова интеракције.

Следеће, погледајмо Функцијско/Алатско позивање у детаљнијем приказу.
 
### Функцијско/Алатско позивање

Позивање функција је примарни начин на који омогућавамо Великим језичким моделима (LLM) да интерагују са алатима. Често ћете видети да се термини „Функција“ и „Алат“ користе наизменично зато што су „функције“ (блокови поново употребљивог кода) то што агенти користе као „алате“ за обављање задатака. Да би се код функције извршио, LLM мора упоредити кориснички захтев са описом функције. За то се шаље шема која садржи описе свих доступних функција LLM-у. LLM онда бира најприкладнију функцију за задаци и враћа њено име и аргументе. Изабрана функција се извршава, њен одговор се шаље назад LLM-у који користи информацију да одговори на кориснички захтев.

За развојне програмере који желе да имплементирају позивање функција за агенте потребно је:

1. LLM модел који подржава позивање функција
2. Шема која садржи описе функција
3. Код за сваку описану функцију

Узмимо за пример добијање текућег времена у неком граду да илуструјемо:

1. **Иницијализација LLM-а који подржава позивање функција:**

    Не сви модели подржавају позивање функција, па је важно проверити да LLM који користите то ради.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> подржава позивање функција. Можемо започети иницијализацијом Azure OpenAI клијента.

    ```python
    # Иницијализујте Azure OpenAI клијента
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Креирање шеме функције**:

    Након тога ћемо дефинисати JSON шему која садржи име функције, опис онога што функција ради и имена и описа параметара функције. Затим ћемо ову шему проследити претходно креираном клијенту, заједно са корисничким захтевом да пронађе време у Сан Франциску. Важно је напоменути да се враћа позив алата, **а НЕ** коначан одговор на питање. Као што је раније речено, LLM враћа име функције коју је изабрао за задатак и аргументе који ће јој бити прослеђени.

    ```python
    # Опис функције за читање модела
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
  
    # Први позив API-ја: Замолите модел да користи функцију
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

    Сада када је LLM изабрао коју функцију треба покренути, код који обавља задатак треба имплементирати и извршити. Можемо имплементирати код за добијање текућег времена у Питону. Такође ћемо морати написати код који ће извући име и аргументе из response_message како бисмо добили коначан резултат.

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
  
      # Други API позив: Добити коначни одговор од модела
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

Позивање функција је у сржи већине, ако не и свих образаца коришћења алата код агената, али имплементација од нуле може понекад бити изазовна. Као што смо научили у [Лекција 2](../../../02-explore-agentic-frameworks), агентски оквири нам пружају унапред направљене градивне блокове за имплементацију коришћења алата.
 
## Примери коришћења алата са агентским оквирима

Ево неколико примера како можете имплементирати Образац дизајна коришћења алата користећи различите агентске оквире:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> је open-source AI оквир за .NET, Python и Java развојне програмере који раде са Великим језичким моделима (LLM). Поједностављује процес коришћења позивања функција аутоматски описујући ваше функције и њихове параметре моделу путем процеса званог <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">серијализација</a>. Такође управља комуникацијом напред-назад између модела и вашег кода. Још једна предност коришћења агентског оквира као што је Semantic Kernel је што вам омогућава приступ унапред направљеним алатима као што су <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Претрага фајлова</a> и <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Тумач кода</a>.

Следећа дијаграма илуструје процес позивања функција са Semantic Kernel-ом:

![function calling](../../../translated_images/sr/functioncalling-diagram.a84006fc287f6014.webp)

У Semantic Kernel-у, функције/алати се зову <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">плугинови</a>. Можемо претворити функцију `get_current_time` коју смо видели раније у плагин претварајући је у класу са функцијом у њој. Такође можемо увезти `kernel_function` декоратор који прима опис функције. Када креирате кернел са GetCurrentTimePlugin, кернел ће аутоматски серијализовати функцију и њене параметре, правећи шему коју шаље LLM-у у процесу.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Креирај језгро
kernel = Kernel()

# Креирај додатак
get_current_time_plugin = GetCurrentTimePlugin(location)

# Додај додатак у језгро
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> је новији агентски оквир дизајниран да омогући програмерима да безбедно граде, развијају и скалирају висококвалитетне и прошириве AI агенте без потребе за управљањем основним рачунарским и складишним ресурсима. Посебно је користан за предузетничке апликације јер је то комплетно управљана услуга са корпоративним безбедносним стандардима.

У поређењу са развојем директно са LLM API-јем, Azure AI Agent Service пружа одређене предности, укључујући:

- Аутоматско позивање алата – нема потребе да парсирате позив алата, извршавате алат и управљате одговором; све се сада ради на серверској страни
- Безбедно управљани подаци – уместо да управљате сопственим стањем разговора, можете се ослонити на тредове који чувају све потребне информације
- Алати спремни за употребу – Алати које можете користити за интеракцију са изворима података, као што су Bing, Azure AI Search и Azure Functions.

Алатке доступне у Azure AI Agent Service могу се поделити у две категорије:

1. Алати за знање:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Прецизирање уз Bing претрагу</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Претрага фајлова</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Акциони алати:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Позивање функција</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Тумач кода</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Алатке дефинисане OpenAPI-јем</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service нам омогућава да заједно користимо ове алате као `skup alata`. Такође користи `тредове` који бележе историју порука из одређеног разговора.

Замислите да сте продајни агент у компанији Contoso. Желите да развијете разговорног агента који може да одговара на питања о вашим продајним подацима.

Следећа слика илуструје како бисте могли користити Azure AI Agent Service за анализу ваших продајних података:

![Agentic Service In Action](../../../translated_images/sr/agent-service-in-action.34fb465c9a84659e.webp)

Да бисмо користили било који од ових алата са услугом, можемо креирати клијента и дефинисати алат или скуп алата. Да бисмо ово практично имплементирали, можемо користити следећи Python код. LLM ће моћи да погледа скуп алата и одлучи да ли ће користити кориснички креирану функцију `fetch_sales_data_using_sqlite_query` или унапред направљени Тумач кода у зависности од корисничког захтева.

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

# Иницијализуј алатке
toolset = ToolSet()

# Иницијализуј агент за позивање функција са функцијом fetch_sales_data_using_sqlite_query и додај га у алатке
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Иницијализуј алатку за тумачење кода и додај је у алатке.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Које су посебне разматрања приликом коришћења Образца дизајна коришћења алата за изградњу поузданих AI агената?

Честа брига у вези SQL-а динамички генерисаног од стране LLM-ова је безбедност, посебно ризик од SQL инјекције или злонамерних радњи, као што су брисање или манипулација базом података. Иако су ове бриге оправдане, могу се ефикасно ублажити правилном конфигурацијом приступних права базе података. За већину база података то укључује конфигурацију базе као само за читање. За услуге као што су PostgreSQL или Azure SQL, апликацији треба доделити улогу само за читање (SELECT).
Покретање апликације у безбедном окружењу додатно побољшава заштиту. У предузетничким сценаријима, подаци се обично извлаче и трансформишу из оперативних система у базу података или складиште података само за читање са кориснички пријатном шемом. Овај приступ осигурава да су подаци безбедни, оптимизовани за перформансе и приступачност, и да апликација има ограничен, само за читање приступ.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Imate ли више питања о употреби дизајн образаца алата?

Придружите се [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) да упознате друге ученике, присуствујете канцеларијским сатима и добијете одговоре на своја питања о AI агентима.

## Допунски ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Радна радионица Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Радна радионица Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Туторијал за Semantic Kernel Function Calling</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Претходна лекција

[Разумевање агентских дизајн образаца](../03-agentic-design-patterns/README.md)

## Следећа лекција

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Изјава о ограничењу одговорности**:
Овај документ је преведен коришћењем АИ услуге превођења [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразумевања или погрешна тумачења настала употребом овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->