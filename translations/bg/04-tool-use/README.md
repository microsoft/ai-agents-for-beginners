[![Как да проектираме добри AI агенти](../../../translated_images/bg/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Кликнете върху горната снимка, за да гледате видео на този урок)_

# Дизайнерски модел за използване на инструменти

Инструментите са интересни, защото позволяват на AI агентите да имат по-широк спектър от възможности. Вместо агентът да разполага с ограничен набор от действия, които може да изпълнява, чрез добавяне на инструмент агентът сега може да изпълнява широк спектър от действия. В тази глава ще разгледаме Дизайнерския модел за използване на инструменти, който описва как AI агентите могат да използват специфични инструменти за постигане на своите цели.

## Въведение

В този урок ще се опитаме да отговорим на следните въпроси:

- Какво представлява дизайнерският модел за използване на инструменти?
- За какви случаи на употреба може да се прилага?
- Какви са елементите/строителните блокове, необходими за внедряване на дизайнерския модел?
- Какви са специалните съображения при използване на дизайнерския модел за използване на инструменти за изграждане на надеждни AI агенти?

## Цели на обучението

След завършване на този урок ще можете да:

- Дефинирате дизайнерския модел за използване на инструменти и неговата цел.
- Идентифицирате случаи на употреба, при които дизайнерският модел за използване на инструменти е приложим.
- Разберете ключовите елементи, необходими за внедряване на дизайнерския модел.
- Разпознавате съображения за осигуряване на надеждност при AI агенти, използващи този дизайнерски модел.

## Какво представлява дизайнерският модел за използване на инструменти?

**Дизайнерският модел за използване на инструменти** се фокусира върху предоставянето на възможност на LLM да взаимодействат с външни инструменти за постигане на конкретни цели. Инструментите са код, който може да бъде изпълнен от агент с цел извършване на действия. Инструмент може да бъде проста функция като калкулатор или API повикване към външна услуга, например за проверка на цена на акции или прогнозата за времето. В контекста на AI агентите, инструментите са проектирани да се изпълняват от агенти в отговор на **функционални повиквания, генерирани от модела**.

## За какви случаи на употреба може да се прилага?

AI агентите могат да използват инструменти за изпълнение на сложни задачи, извличане на информация или вземане на решения. Дизайнерският модел за използване на инструменти често се използва в сцени, изискващи динамично взаимодействие с външни системи, като бази данни, уеб услуги или интерпретатори на код. Тази възможност е полезна за множество различни случаи на употреба, включително:

- **Динамично извличане на информация:** Агенти могат да запитват външни API-та или бази данни, за да получат актуални данни (напр. запитване към SQLite база за анализ на данни, получаване на цени на акции или информация за времето).
- **Изпълнение и тълкуване на код:** Агенти могат да изпълняват код или скриптове за решаване на математически задачи, генериране на отчети или провеждане на симулации.
- **Автоматизация на работни потоци:** Автоматизиране на повтарящи се или мултистъпкови работни потоци чрез интегриране на инструменти като планиращи задачи, имейл услуги или данни-пайплайни.
- **Поддръжка на клиенти:** Агенти могат да взаимодействат с CRM системи, платформи за тикети или бази знания за разрешаване на въпроси от потребители.
- **Генериране и редактиране на съдържание:** Агенти могат да използват инструменти като проверка на граматика, обобщаващи текстове или оценка на безопасността на съдържанието за подпомагане на задачи, свързани с създаването на съдържание.

## Какви са елементите/строителните блокове, необходими за внедряване на дизайнерския модел за използване на инструменти?

Тези строителни блокове позволяват на AI агента да извършва широк набор от задачи. Нека разгледаме ключовите елементи, нужни за внедряване на Дизайнерския модел за използване на инструменти:

- **Схеми за функции/инструменти**: Подробни дефиниции на наличните инструменти, включително име на функцията, цел, изисквани параметри и очаквани резултати. Тези схеми позволяват на LLM да разбере кои инструменти са налични и как да съставя валидни заявки.

- **Логика за изпълнение на функции**: Определя кога и как инструментите се извикват на базата на намеренията на потребителя и контекста на разговора. Това може да включва модули за планиране, маршрутизиране или условни потоци, които динамично определят използването на инструменти.

- **Система за управление на съобщения**: Компоненти, които управляват потока на разговор между входовете на потребителя, отговорите на LLM, повикванията към инструменти и техните резултати.

- **Рамка за интеграция на инструменти**: Инфраструктура, която свързва агента с различни инструменти, независимо дали са прости функции или сложни външни услуги.

- **Обработка на грешки и валидация**: Механизми за справяне с провали при изпълнението на инструменти, проверка на параметрите и управление на неочаквани отговори.

- **Управление на състоянието**: Проследява контекста на разговора, предишни взаимодействия с инструменти и постоянни данни, за да осигури последователност в мултистъпковите взаимодействия.

Следва да разгледаме по-подробно функциите/повикванията на функции.

### Повикване на функция/инструмент

Повикването на функция е основният начин, по който позволяваме на Големите езикови модели (LLM) да взаимодействат с инструменти. Често ще срещнете 'Функция' и 'Инструмент' използвани взаимозаменяемо, защото 'функциите' (блокове с многократно използваем код) са 'инструментите', които агентите използват за изпълнение на задачи. За да бъде извикан кодът на дадена функция, LLM трябва да съпостави заявката на потребителя с описанието на функциите. За целта се изпраща схема, съдържаща описанията на всички налични функции към LLM. LLM след това избира най-подходящата функция за задачата и връща нейното име и аргументи. Избраната функция се извиква, нейният отговор се връща обратно към LLM, който използва тази информация, за да отговори на заявката на потребителя.

За да имплементирате повиквания на функции за агенти, ще имате нужда от:

1. Модел LLM, който поддържа повикване на функции
2. Схема, съдържаща описания на функциите
3. Кодът за всяка описана функция

Нека илюстрираме с пример за получаване на текущото време в даден град:

1. **Инициализиране на LLM, който поддържа повикване на функции:**

    Не всички модели поддържат повикване на функции, затова е важно да проверите дали използваният от вас LLM го поддържа. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> поддържа повикване на функции. Можем да започнем с инициализиране на клиента за Azure OpenAI.

    ```python
    # Инициализирайте клиента на Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Създаване на схема за функция:**

    След това ще дефинираме JSON схема, която съдържа името на функцията, описание на това какво прави функцията и имената и описанията на параметрите ѝ.
    След това ще подадем тази схема на предварително създадения клиент, заедно със заявката на потребителя да намери времето в Сан Франциско. Важно е да се отбележи, че се връща **повикване на инструмент**, а **не** окончателен отговор на въпроса. Както беше споменато по-рано, LLM връща името на функцията, която е избрал за задачата, и аргументите, които ще бъдат предадени на нея.

    ```python
    # Описание на функцията за четене от модела
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
  
    # Първоначално съобщение от потребителя
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Първо повикване на API: Попитайте модела да използва функцията
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Обработване на отговора на модела
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

    След като LLM е избрал коя функция трябва да бъде изпълнена, кодът, който изпълнява задачата, трябва да бъде реализиран и изпълнен.
    Можем да напишем кода за получаване на текущото време на Python. Потрябва да напишем и код за извличане на името и аргументите от `response_message`, за да получим крайния резултат.

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
     # Обработка на повиквания на функции
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
  
      # Второ повикване към API: Получаване на окончателния отговор от модела
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

Повикването на функции е в основата на повечето, ако не и на всички дизайнерски модели за използване на инструменти при агенти, но реализирането му от нулата понякога може да бъде предизвикателство.
Както научихме в [Урок 2](../../../02-explore-agentic-frameworks), агентните рамки ни предоставят предварително изградени строителни блокове за внедряване на използване на инструменти.

## Примери за използване на инструменти с агентни рамки

Ето някои примери как можете да приложите Дизайнерския модел за използване на инструменти с различни агентни рамки:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> е отворена AI рамка за разработчици на .NET, Python и Java, работещи с Големи езикови модели (LLM). Тя опростява процеса на използване на повикване на функции чрез автоматично описване на функциите и техните параметри на модела чрез процес, наречен <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">сериализиране</a>. Тя също така управлява двупосочната комуникация между модела и вашия код. Друго предимство на използването на агентна рамка като Semantic Kernel е, че ви позволява да достъпвате предварително изградени инструменти като <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Търсене на файлове</a> и <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Код интерпретатор</a>.

Следната диаграма илюстрира процеса на повикване на функция с Semantic Kernel:

![function calling](../../../translated_images/bg/functioncalling-diagram.a84006fc287f6014.webp)

В Semantic Kernel функциите/инструментите се наричат <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Плъгини</a>. Можем да преобразуваме функцията `get_current_time`, която видяхме по-рано, в плъгин, като я превърнем в клас с функцията вътре. Можем също така да импортираме декоратора `kernel_function`, който приема описанието на функцията. Когато след това създадем kernel с GetCurrentTimePlugin, kernel автоматично ще сериализира функцията и нейните параметри, създавайки схема, която се изпраща към LLM.

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

# Създайте ядрото
kernel = Kernel()

# Създайте приставката
get_current_time_plugin = GetCurrentTimePlugin(location)

# Добавете приставката към ядрото
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> е по-нова агентна рамка, проектирана да даде възможност на разработчиците да изграждат, внедряват и мащабират сигурно висококачествени и разширяеми AI агенти без необходимост от управление на основните изчислителни и хранилищни ресурси. Особено полезна е за корпоративни приложения, тъй като е напълно управляема услуга с корпоративно ниво на сигурност.

В сравнение с разработката директно с LLM API, Azure AI Agent Service предлага няколко предимства, включително:

- Автоматично повикване на инструменти – няма нужда да парсирате повиквания на инструменти, да ги извиквате и да обработвате отговора; всичко това вече се извършва на сървърната страна
- Сигурно управлявани данни – вместо да управлявате собственото състояние на разговора, можете да разчитате на нишки за съхранение на цялата необходима информация
- Готови за употреба инструменти – Инструменти, които можете да използвате за взаимодействие с източниците на данни, като Bing, Azure AI Search и Azure Functions.

Инструментите, налични в Azure AI Agent Service, се разделят на две категории:

1. Инструменти за познание:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">заземяване с търсене Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Търсене на файлове</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Търсене чрез Azure AI</a>

2. Инструменти за действия:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Повикване на функции</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Код интерпретатор</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Инструменти, дефинирани чрез OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ни позволява да използваме тези инструменти заедно като `toolset`. Той също така използва `нишки`, които следят историята на съобщенията от конкретен разговор.

Представете си, че сте търговски агент в компания на име Contoso. Искате да разработите разговорен агент, който може да отговаря на въпроси относно вашите продажбени данни.

Следното изображение илюстрира как бихте могли да използвате Azure AI Agent Service за анализ на вашите продажбени данни:

![Agentic Service In Action](../../../translated_images/bg/agent-service-in-action.34fb465c9a84659e.webp)

За да използваме някой от тези инструменти с услугата, можем да създадем клиент и да дефинираме инструмент или набор от инструменти. За да го направим практически, можем да използваме следния код на Python. LLM ще може да разгледа toolset и да реши дали да използва създадената от потребителя функция `fetch_sales_data_using_sqlite_query` или предварително изградения Код интерпретатор в зависимост от заявката на потребителя.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # функция fetch_sales_data_using_sqlite_query, която може да бъде намерена във файла fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Инициализиране на инструментариум
toolset = ToolSet()

# Инициализиране на агент за извикване на функции с функцията fetch_sales_data_using_sqlite_query и добавянето ѝ към инструментариума
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Инициализиране на инструмента Code Interpreter и добавянето му към инструментариума.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Какви са специалните съображения при използване на дизайнерския модел за използване на инструменти за изграждане на надеждни AI агенти?

Често срещан проблем при динамично генерираните от LLM SQL заявки е сигурността, особено рискът от SQL инжекции или злонамерени действия, като изтриване или манипулиране на базата данни. Въпреки че тези опасения са оправдани, те могат ефективно да се смекчат чрез правилна конфигурация на разрешенията за достъп до базата данни. За повечето бази данни това включва конфигуриране на базата данни като само за четене. За бази данни като PostgreSQL или Azure SQL приложението трябва да бъде назначено с роля само за четене (SELECT).
Работата на приложението в защитена среда допълнително повишава защитата. В бизнес сценарии данните обикновено се извличат и трансформират от оперативни системи в база данни или склад за данни с достъп само за четене и потребителски приятна схема. Този подход гарантира, че данните са защитени, оптимизирани за производителност и достъпност и че приложението има ограничен достъп само за четене.

## Примерни кодове

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Имате ли още въпроси за използването на дизайните за шаблони на инструменти?

Присъединете се към [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), за да се срещнете с други учащи, да посещавате консултации и да получите отговори на въпросите си за AI агентите.

## Допълнителни ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Работилница за Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Работилница Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Уроци за извикване на функции в Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Интерпретатор на код в Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Инструменти на Autogen</a>

## Предишен урок

[Разбиране на агентните дизайни за шаблони](../03-agentic-design-patterns/README.md)

## Следващ урок

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия естествен език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->