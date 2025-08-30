<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4a5ccc4ad1dba85fbc2087cf3b986544",
  "translation_date": "2025-08-30T08:54:14+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "sr"
}
-->
[![Как дизајнирати добре AI агенте](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.sr.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Кликните на слику изнад да бисте погледали видео лекцију)_

# Шаблон за коришћење алата

Алатке су занимљиве јер омогућавају AI агентима да имају шири спектар могућности. Уместо да агент има ограничен скуп радњи које може извршити, додавањем алатке агент сада може извршавати широк спектар радњи. У овом поглављу ћемо размотрити шаблон за коришћење алата, који описује како AI агенти могу користити одређене алатке за постизање својих циљева.

## Увод

У овој лекцији настојимо да одговоримо на следећа питања:

- Шта је шаблон за коришћење алата?
- На које случајеве употребе се може применити?
- Који су елементи/градивни блокови потребни за имплементацију шаблона?
- Које су посебне ствари које треба узети у обзир приликом коришћења шаблона за изградњу поузданих AI агената?

## Циљеви учења

Након завршетка ове лекције, бићете у могућности да:

- Дефинишете шаблон за коришћење алата и његову сврху.
- Идентификујете случајеве употребе где је овај шаблон применљив.
- Разумете кључне елементе потребне за имплементацију шаблона.
- Препознате аспекте који осигуравају поузданост AI агената који користе овај шаблон.

## Шта је шаблон за коришћење алата?

**Шаблон за коришћење алата** се фокусира на омогућавање LLM-овима да интерагују са спољним алатима како би постигли одређене циљеве. Алатке су код који агент може извршити ради обављања радњи. Алатка може бити једноставна функција, попут калкулатора, или API позив ка услузи треће стране, као што је претрага цена акција или временска прогноза. У контексту AI агената, алатке су дизајниране да их агенти извршавају као одговор на **функцијске позиве генерисане моделом**.

## На које случајеве употребе се може применити?

AI агенти могу користити алатке за обављање сложених задатака, прикупљање информација или доношење одлука. Шаблон за коришћење алата се често користи у сценаријима који захтевају динамичку интеракцију са спољним системима, као што су базе података, веб услуге или интерпретатори кода. Ова способност је корисна за бројне случајеве употребе, укључујући:

- **Динамичко прикупљање информација:** Агенти могу упућивати упите спољним API-јима или базама података како би добили ажуриране податке (нпр. упит ка SQLite бази за анализу података, добијање цена акција или временских информација).
- **Извршавање и интерпретација кода:** Агенти могу извршавати код или скрипте за решавање математичких проблема, генерисање извештаја или извођење симулација.
- **Аутоматизација радних токова:** Аутоматизација понављајућих или вишестепених радних токова интеграцијом алата као што су планери задатака, услуге е-поште или податковни токови.
- **Корисничка подршка:** Агенти могу комуницирати са CRM системима, платформама за тикете или базама знања ради решавања корисничких упита.
- **Генерисање и уређивање садржаја:** Агенти могу користити алатке као што су провера граматике, сажимање текста или евалуатори безбедности садржаја за помоћ у задацима креирања садржаја.

## Који су елементи/градивни блокови потребни за имплементацију шаблона за коришћење алата?

Ови градивни блокови омогућавају AI агенту да обавља широк спектар задатака. Погледајмо кључне елементе потребне за имплементацију шаблона за коришћење алата:

- **Шеме функција/алата:** Детаљни описи доступних алата, укључујући име функције, сврху, потребне параметре и очекиване излазе. Ове шеме омогућавају LLM-у да разуме који су алати доступни и како да конструише важеће захтеве.
- **Логика извршавања функција:** Управља тиме како и када се алати позивају на основу корисничке намере и контекста разговора. Ово може укључивати модуле за планирање, механизме за рутирање или условне токове који динамички одређују употребу алата.
- **Систем за управљање порукама:** Компоненте које управљају током разговора између корисничких уноса, одговора LLM-а, позива алата и излаза алата.
- **Оквир за интеграцију алата:** Инфраструктура која повезује агента са различитим алатима, било да су то једноставне функције или сложене спољне услуге.
- **Обрада грешака и валидација:** Механизми за руковање неуспесима у извршавању алата, валидацију параметара и управљање неочекиваним одговорима.
- **Управљање стањем:** Праћење контекста разговора, претходних интеракција са алатима и перзистентних података ради осигурања конзистентности током вишеструких интеракција.

Следеће ћемо детаљније размотрити позивање функција/алата.

### Позивање функција/алата

Позивање функција је примарни начин на који омогућавамо великим језичким моделима (LLM-овима) да интерагују са алатима. Често ћете видети да се „функција“ и „алат“ користе наизменично, јер су „функције“ (блокови поновљивог кода) „алати“ које агенти користе за обављање задатака. Да би се код функције позвао, LLM мора упоредити кориснички захтев са описом функције. За то се LLM-у шаље шема која садржи описе свих доступних функција. LLM затим бира најприкладнију функцију за задатак и враћа њено име и аргументе. Изабрана функција се позива, њен одговор се шаље назад LLM-у, који користи информације за одговор на кориснички захтев.

За имплементацију позивања функција за агенте, програмери ће морати:

1. Модел LLM који подржава позивање функција
2. Шему која садржи описе функција
3. Код за сваку описану функцију

Хајде да илуструјемо пример добијања тренутног времена у одређеном граду:

1. **Иницијализација LLM-а који подржава позивање функција:**

    Не подржавају сви модели позивање функција, па је важно проверити да ли LLM који користите то омогућава. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> подржава позивање функција. Можемо започети иницијализацијом Azure OpenAI клијента.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Креирање шеме функције:**

    Затим ћемо дефинисати JSON шему која садржи име функције, опис онога што функција ради, као и имена и описе параметара функције. Ову шему ћемо затим проследити претходно креираном клијенту, заједно са корисничким захтевом за проналажење времена у Сан Франциску. Важно је напоменути да се враћа **позив алата**, а не коначни одговор на питање. Као што је раније поменуто, LLM враћа име функције коју је изабрао за задатак и аргументе који ће јој бити прослеђени.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Код функције потребан за обављање задатка:**

    Сада када је LLM изабрао коју функцију треба покренути, потребно је имплементирати и извршити код који обавља задатак. Можемо имплементирати код за добијање тренутног времена у Python-у. Такође ћемо морати написати код за издвајање имена и аргумената из response_message како бисмо добили коначни резултат.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

Позивање функција је у срцу већине, ако не и свих дизајна агената који користе алате, али имплементација од нуле понекад може бити изазовна. Као што смо научили у [Лекцији 2](../../../02-explore-agentic-frameworks), агентички оквири нам пружају унапред изграђене градивне блокове за имплементацију коришћења алата.

## Примери коришћења алата са агентичким оквирима

Ево неколико примера како можете имплементирати шаблон за коришћење алата користећи различите агентичке оквире:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> је отворени AI оквир за .NET, Python и Java програмере који раде са великим језичким моделима (LLM-овима). Олакшава процес коришћења позивања функција аутоматским описивањем ваших функција и њихових параметара моделу кроз процес назван <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">серијализација</a>. Такође управља комуникацијом између модела и вашег кода. Још једна предност коришћења агентичког оквира као што је Semantic Kernel је та што вам омогућава приступ унапред изграђеним алатима као што су <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> и <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Следећи дијаграм илуструје процес позивања функција са Semantic Kernel-ом:

![function calling](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.sr.png)

У Semantic Kernel-у функције/алати се називају <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Можемо претворити функцију `get_current_time` коју смо видели раније у додатак тако што ћемо је претворити у класу са функцијом унутар ње. Такође можемо увезти декоратор `kernel_function`, који узима опис функције. Када затим креирате језгро са GetCurrentTimePlugin, језгро ће аутоматски серијализовати функцију и њене параметре, креирајући шему за слање LLM-у у том процесу.

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

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> је новији агентички оквир који је дизајниран да омогући програмерима да безбедно граде, распоређују и скалирају висококвалитетне и прошириве AI агенте без потребе за управљањем основним рачунарским и складишним ресурсима. Посебно је користан за предузетничке апликације јер је у потпуности управљана услуга са безбедношћу на нивоу предузећа.

У поређењу са развојем директно са LLM API-јем, Azure AI Agent Service пружа неке предности, укључујући:

- Аутоматско позивање алата – нема потребе за парсирањем позива алата, позивањем алата и руковањем одговором; све ово се сада обавља на серверској страни
- Безбедно управљање подацима – уместо да сами управљате стањем разговора, можете се ослонити на нити за чување свих потребних информација
- Унапред изграђени алати – Алати које можете користити за интеракцију са вашим изворима података, као што су Bing, Azure AI Search и Azure Functions.

Алати доступни у Azure AI Agent Service могу се поделити у две категорије:

1. Алати за знање:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding with Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Алати за акцију:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAI defined tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service нам омогућава да користимо ове алате заједно као `toolset`. Такође користи `threads` које прате историју порука из одређеног разговора.

Замислите да сте продајни агент у компанији Contoso. Желите да развијете конверзацијског агента који може одговарати на питања о вашим продајним подацима.

Следећа слика илуструје како бисте могли користити Azure AI Agent Service за анализу ваших продајних података:

![Agentic Service In Action](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.sr.jpg)

Да бисте користили било који од ових алата са услугом, можемо креирати клијента и дефинисати алат или скуп алата. За практичну имплементацију можемо користити следећи Python код. LLM ће моћи да погледа скуп алата и одлучи да ли ће користити кориснички креирану функцију `fetch_sales_data_using_sqlite_query` или унапред изграђени Code Interpreter у зависности од корисничког захтева.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Које су посебне ствари које треба узети у обзир приликом коришћења шаблона за изградњу поузданих AI агената?

Честа брига у вези са SQL-ом који динамички генеришу LLM-ови је безбедност, посебно ризик од SQL инјекције или злонамерних радњи, као што је брисање или манипулација базом података.
Придружите се [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) да се повежете са другим ученицима, присуствујете консултацијама и добијете одговоре на ваша питања о AI агентима.

## Додатни ресурси

## Претходна лекција

[Разумевање агентичких образаца дизајна](../03-agentic-design-patterns/README.md)

## Наредна лекција

[Агентички RAG](../05-agentic-rag/README.md)

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.