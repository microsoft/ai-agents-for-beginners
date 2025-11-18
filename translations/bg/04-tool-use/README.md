<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T18:18:55+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "bg"
}
-->
[![Как да проектираме добри AI агенти](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.bg.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Кликнете върху изображението по-горе, за да гледате видеото на този урок)_

# Модел за използване на инструменти

Инструментите са интересни, защото позволяват на AI агентите да имат по-широк набор от възможности. Вместо агентът да има ограничен набор от действия, които може да изпълнява, добавянето на инструмент му позволява да извършва разнообразни действия. В тази глава ще разгледаме модела за използване на инструменти, който описва как AI агентите могат да използват специфични инструменти, за да постигнат целите си.

## Въведение

В този урок ще се опитаме да отговорим на следните въпроси:

- Какво представлява моделът за използване на инструменти?
- За какви случаи на употреба може да се приложи?
- Какви са елементите/основните блокове, необходими за внедряване на модела?
- Какви са специалните съображения при използването на модела за изграждане на надеждни AI агенти?

## Цели на обучението

След завършване на този урок ще можете:

- Да дефинирате модела за използване на инструменти и неговата цел.
- Да идентифицирате случаи на употреба, където моделът е приложим.
- Да разберете ключовите елементи, необходими за внедряване на модела.
- Да разпознаете съображенията за осигуряване на надеждност в AI агентите, използващи този модел.

## Какво представлява моделът за използване на инструменти?

**Моделът за използване на инструменти** се фокусира върху предоставянето на LLMs възможността да взаимодействат с външни инструменти, за да постигнат конкретни цели. Инструментите са код, който може да бъде изпълнен от агент за извършване на действия. Инструментът може да бъде проста функция, като калкулатор, или API заявка към услуга на трета страна, като проверка на цените на акции или прогноза за времето. В контекста на AI агентите, инструментите са проектирани да бъдат изпълнявани от агенти в отговор на **генерирани от модела заявки за функции**.

## За какви случаи на употреба може да се приложи?

AI агентите могат да използват инструменти за изпълнение на сложни задачи, извличане на информация или вземане на решения. Моделът за използване на инструменти често се използва в сценарии, изискващи динамично взаимодействие с външни системи, като бази данни, уеб услуги или интерпретатори на код. Тази способност е полезна за редица различни случаи на употреба, включително:

- **Динамично извличане на информация:** Агенти могат да правят заявки към външни API или бази данни, за да получат актуални данни (например, заявка към SQLite база данни за анализ на данни, извличане на цени на акции или информация за времето).
- **Изпълнение и интерпретация на код:** Агенти могат да изпълняват код или скриптове за решаване на математически проблеми, генериране на отчети или извършване на симулации.
- **Автоматизация на работни процеси:** Автоматизиране на повтарящи се или многоетапни работни процеси чрез интегриране на инструменти като планировчици на задачи, имейл услуги или потоци от данни.
- **Поддръжка на клиенти:** Агенти могат да взаимодействат със CRM системи, платформи за билети или бази знания за разрешаване на потребителски запитвания.
- **Генериране и редактиране на съдържание:** Агенти могат да използват инструменти като проверка на граматика, обобщаване на текст или оценка на безопасността на съдържанието за подпомагане на задачи по създаване на съдържание.

## Какви са елементите/основните блокове, необходими за внедряване на модела за използване на инструменти?

Тези основни блокове позволяват на AI агентите да изпълняват широк набор от задачи. Нека разгледаме ключовите елементи, необходими за внедряване на модела за използване на инструменти:

- **Схеми на функции/инструменти:** Подробни дефиниции на наличните инструменти, включително име на функцията, цел, необходими параметри и очаквани изходи. Тези схеми позволяват на LLM да разбере какви инструменти са налични и как да създаде валидни заявки.
- **Логика за изпълнение на функции:** Управлява как и кога инструментите се извикват въз основа на намерението на потребителя и контекста на разговора. Това може да включва модули за планиране, механизми за маршрутизация или условни потоци, които динамично определят използването на инструменти.
- **Система за управление на съобщения:** Компоненти, които управляват потока на разговор между входовете на потребителя, отговорите на LLM, заявките към инструменти и изходите от тях.
- **Рамка за интеграция на инструменти:** Инфраструктура, която свързва агента с различни инструменти, независимо дали са прости функции или сложни външни услуги.
- **Управление на грешки и валидиране:** Механизми за справяне с неуспехи при изпълнение на инструменти, валидиране на параметри и управление на неочаквани отговори.
- **Управление на състоянието:** Проследява контекста на разговора, предишни взаимодействия с инструменти и постоянни данни, за да осигури последователност при многоетапни взаимодействия.

След това нека разгледаме по-подробно извикването на функции/инструменти.

### Извикване на функции/инструменти

Извикването на функции е основният начин, по който позволяваме на големите езикови модели (LLMs) да взаимодействат с инструменти. Често ще видите, че "функция" и "инструмент" се използват взаимозаменяемо, защото "функциите" (блокове от многократно използваем код) са "инструментите", които агентите използват за изпълнение на задачи. За да бъде извикан кодът на дадена функция, LLM трябва да сравни заявката на потребителя с описанието на функцията. За тази цел схема, съдържаща описанията на всички налични функции, се изпраща на LLM. След това LLM избира най-подходящата функция за задачата и връща нейното име и аргументи. Избраната функция се извиква, нейният отговор се изпраща обратно на LLM, който използва информацията, за да отговори на заявката на потребителя.

За разработчиците, които искат да внедрят извикване на функции за агенти, ще са необходими:

1. LLM модел, който поддържа извикване на функции
2. Схема, съдържаща описания на функции
3. Кодът за всяка описана функция

Нека използваме примера за получаване на текущото време в даден град, за да илюстрираме:

1. **Инициализиране на LLM, който поддържа извикване на функции:**

    Не всички модели поддържат извикване на функции, затова е важно да проверите дали LLM, който използвате, го прави. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> поддържа извикване на функции. Можем да започнем, като инициираме клиента на Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Създаване на схема на функция:**

    След това ще дефинираме JSON схема, която съдържа името на функцията, описание на това какво прави функцията, както и имената и описанията на параметрите на функцията. Ще вземем тази схема и ще я предадем на клиента, създаден по-рано, заедно със заявката на потребителя за намиране на времето в Сан Франциско. Важно е да отбележим, че **заявка към инструмент** е това, което се връща, **а не** крайният отговор на въпроса. Както беше споменато по-рано, LLM връща името на функцията, която е избрал за задачата, и аргументите, които ще бъдат предадени на нея.

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
  
1. **Кодът на функцията, необходим за изпълнение на задачата:**

    Сега, когато LLM е избрал коя функция трябва да бъде изпълнена, кодът, който изпълнява задачата, трябва да бъде внедрен и изпълнен. Можем да внедрим кода за получаване на текущото време на Python. Ще трябва също така да напишем код за извличане на името и аргументите от response_message, за да получим крайния резултат.

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

Извикването на функции е в основата на повечето, ако не всички, дизайни за използване на инструменти от агенти, но внедряването му от нулата понякога може да бъде предизвикателство. Както научихме в [Урок 2](../../../02-explore-agentic-frameworks), агентните рамки ни предоставят предварително изградени основни блокове за внедряване на използване на инструменти.

## Примери за използване на инструменти с агентни рамки

Ето някои примери за това как можете да внедрите модела за използване на инструменти, използвайки различни агентни рамки:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> е отворена рамка за AI за разработчици на .NET, Python и Java, работещи с големи езикови модели (LLMs). Тя опростява процеса на използване на извикване на функции, като автоматично описва вашите функции и техните параметри на модела чрез процес, наречен <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">сериализация</a>. Тя също така управлява комуникацията между модела и вашия код. Друго предимство на използването на агентна рамка като Semantic Kernel е, че ви позволява да получите достъп до предварително изградени инструменти като <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Търсене на файлове</a> и <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Интерпретатор на код</a>.

Следната диаграма илюстрира процеса на извикване на функции със Semantic Kernel:

![извикване на функции](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.bg.png)

В Semantic Kernel функциите/инструментите се наричат <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Можем да преобразуваме функцията `get_current_time`, която видяхме по-рано, в плъгин, като я превърнем в клас с функцията в него. Можем също така да импортираме декоратора `kernel_function`, който приема описанието на функцията. Когато създадете ядро с GetCurrentTimePlugin, ядрото автоматично ще сериализира функцията и нейните параметри, създавайки схемата за изпращане на LLM в процеса.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> е по-нова агентна рамка, която е проектирана да даде възможност на разработчиците да изграждат, внедряват и мащабират висококачествени и разширяеми AI агенти, без да се налага да управляват основните изчислителни и съхранителни ресурси. Тя е особено полезна за корпоративни приложения, тъй като е напълно управлявана услуга с корпоративна степен на сигурност.

В сравнение с разработването директно с LLM API, Azure AI Agent Service предоставя някои предимства, включително:

- Автоматично извикване на инструменти – няма нужда да анализирате заявка към инструмент, да извиквате инструмента и да обработвате отговора; всичко това вече се прави на сървърната страна.
- Сигурно управлявани данни – вместо да управлявате собственото си състояние на разговор, можете да разчитате на нишки, за да съхранявате цялата необходима информация.
- Готови за употреба инструменти – Инструменти, които можете да използвате за взаимодействие с вашите източници на данни, като Bing, Azure AI Search и Azure Functions.

Инструментите, налични в Azure AI Agent Service, могат да бъдат разделени на две категории:

1. Инструменти за знания:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Основа с Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Търсене на файлове</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Инструменти за действия:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Извикване на функции</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Интерпретатор на код</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Инструменти, дефинирани от OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Услугата Agent Service ни позволява да използваме тези инструменти заедно като `toolset`. Тя също така използва `threads`, които следят историята на съобщенията от конкретен разговор.

Представете си, че сте търговски агент в компания, наречена Contoso. Искате да разработите разговорен агент, който може да отговаря на въпроси за вашите данни за продажби.

Следното изображение илюстрира как можете да използвате Azure AI Agent Service за анализ на вашите данни за продажби:

![Agentic Service In Action](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.bg.jpg)

За да използвате някой от тези инструменти с услугата, можем да създадем клиент и да дефинираме инструмент или набор от инструменти. За да го внедрим практически, можем да използваме следния Python код. LLM ще може да разгледа набора от инструменти и да реши дали да използва създадената от потребителя функция `fetch_sales_data_using_sqlite_query` или предварително изградения интерпретатор на код в зависимост от заявката на потребителя.

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

## Какви са специалните съображения при използването на модела за използване на инструменти за изграждане на надеждни AI агенти?

Често срещано притеснение при SQL, динамично генериран от LLMs, е сигурността, особено рискът от SQL инжекция или злонамерени действия, като изтриване или манипулиране на базата данни. Въпреки че тези притеснения са валидни, те могат да бъдат ефективно смекчени чрез правилно конфигуриране на разрешенията за достъп до базата данни. За
Работата на приложението в защитена среда допълнително подобрява защитата. В корпоративни сценарии данните обикновено се извличат и трансформират от оперативни системи в база данни само за четене или склад за данни с удобна за потребителя схема. Този подход гарантира, че данните са защитени, оптимизирани за производителност и достъпност, а приложението има ограничен достъп само за четене.

## Примерни кодове

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Имате още въпроси относно използването на шаблони за дизайн?

Присъединете се към [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), за да се срещнете с други обучаващи се, да участвате в офис часове и да получите отговори на вашите въпроси за AI Agents.

## Допълнителни ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Работилница за Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Работилница за Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Урок за извикване на функции в Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Интерпретатор на код в Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Инструменти Autogen</a>

## Предишен урок

[Разбиране на шаблони за агентен дизайн](../03-agentic-design-patterns/README.md)

## Следващ урок

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия изходен език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->