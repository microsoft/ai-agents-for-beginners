[![Как да проектираме добри AI агенти](../../../translated_images/bg/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Кликнете върху изображението по-горе, за да гледате видеото на този урок)_

# Шаблон за използване на инструменти

Инструментите са интересни, защото позволяват на AI агентите да имат по-широк набор от възможности. Вместо агентът да има ограничен набор от действия, които може да изпълнява, чрез добавяне на инструмент агентът може да извършва широк спектър от действия. В тази глава ще разгледаме шаблона за използване на инструменти, който описва как AI агентите могат да използват конкретни инструменти, за да постигнат своите цели.

## Въведение

В този урок ще се опитаме да отговорим на следните въпроси:

- Какво представлява шаблонът за използване на инструменти?
- В какви случаи може да се прилага?
- Какви са елементите/строителните блокове, необходими за реализиране на шаблона?
- Какви са специалните съображения при използване на шаблона за изграждане на надеждни AI агенти?

## Цели на обучението

След завършване на този урок ще можете да:

- Определяте шаблона за използване на инструменти и неговата цел.
- Идентифицирате случаи, в които шаблонът е приложим.
- Разбирате ключовите елементи, необходими за реализиране на шаблона.
- Разпознавате съображения за гарантиране на надеждност при AI агенти, използващи този шаблон.

## Какво представлява шаблонът за използване на инструменти?

**Шаблонът за използване на инструменти** се съсредоточава върху предоставяне на LLM възможността да взаимодействат с външни инструменти за постигане на конкретни цели. Инструментите са код, който може да бъде изпълнен от агент за извършване на действия. Инструмент може да бъде проста функция като калкулатор или API повикване към външна услуга като търсене на борсова цена или прогноза за времето. В контекста на AI агентите инструментите са проектирани да бъдат изпълнявани от агентите в отговор на **функционални повиквания, генерирани от модела**.

## В какви случаи може да се прилага?

AI агентите могат да използват инструменти, за да изпълняват сложни задачи, да извличат информация или да вземат решения. Шаблонът е често използван в сценарии, изискващи динамично взаимодействие с външни системи, като бази данни, уеб услуги или интерпретатори на код. Тази способност е полезна за редица различни случаи, включително:

- **Динамично извличане на информация:** Агентите могат да правят заявки към външни API-та или бази данни за актуални данни (напр. заявки към SQLite база данни за анализ на данни, получаване на борсови цени или информация за времето).
- **Изпълнение и интерпретиране на код:** Агентите могат да изпълняват код или скриптове за решаване на математически задачи, генериране на отчети или симулации.
- **Автоматизация на работни процеси:** Автоматизиране на повтарящи се или многоетапни работни процеси чрез интегриране на инструменти като планировчици на задачи, имейл услуги или потоци за данни.
- **Поддръжка на клиенти:** Агентите могат да взаимодействат с CRM системи, платформи за поддръжка или бази знания за разрешаване на потребителски запитвания.
- **Генериране и редакция на съдържание:** Агентите могат да използват инструменти като проверка на граматика, обобщаване на текст или оценка на безопасността на съдържанието за подпомагане на задачи по създаване на съдържание.

## Какви са елементите/строителните блокове, необходими за реализиране на шаблона за използване на инструменти?

Тези строителни блокове позволяват на AI агента да изпълнява широк спектър от задачи. Нека разгледаме ключовите елементи, необходими за реализиране на шаблона за използване на инструменти:

- **Схеми на функции/инструменти**: Подробни определения на наличните инструменти, включително име на функция, цел, необходими параметри и очаквани резултати. Тези схеми позволяват на LLM да разбере какви инструменти са налични и как да състави валидни заявки.

- **Логика за изпълнение на функции**: Управлява кога и как инструментите се извикват въз основа на намерението на потребителя и контекста на разговора. Това може да включва модул за планиране, маршрутизиране или условни потоци, които динамично определят използването на необходимия инструмент.

- **Система за обработка на съобщения**: Компоненти, които управляват разговорния поток между потребителски входове, отговори от LLM, повикванията към инструменти и резултатите от тях.

- **Рамка за интегриране на инструменти**: Инфраструктура, която свързва агента с различни инструменти, било то прости функции или сложни външни услуги.

- **Обработка на грешки и валидиране**: Механизми за справяне с неуспехи при изпълнение на инструменти, валидиране на параметри и управление на неочаквани отговори.

- **Управление на състоянието**: Следи контекста на разговора, предишните взаимодействия с инструменти и постоянни данни, за да осигури консистентността при многократни взаимодействия.

След това нека разгледаме по-подробно повикванията на функции/инструменти.
 
### Повикване на функция/инструмент

Повикването на функция е основният начин, по който позволяваме на големите езикови модели (LLM) да взаимодействат с инструменти. Често ще видите, че „функция“ и „инструмент“ се използват взаимозаменяемо, тъй като „функциите“ (блокове с преповтарящ се код) са „инструментите“, които агентите използват за изпълнение на задачи. За да бъде извикан кодът на функция, LLM трябва да сравни заявката на потребителя с описанието на функциите. За тази цел се изпраща схема, съдържаща описанията на всички налични функции към LLM. След това LLM избира най-подходящата функция за задачата и връща нейното име и аргументи. Избраната функция се извиква, нейният отговор се изпраща обратно на LLM, който използва информацията, за да отговори на заявката на потребителя.

За разработчиците, които искат да реализират повикване на функции за агенти, ще ви трябват:

1. LLM модел, който поддържа повикване на функции
2. Схема, съдържаща описания на функциите
3. Код за всяка описана функция

Нека използваме пример за получаване на текущото време в град, за да илюстрираме:

1. **Инициализирайте LLM, който поддържа повикване на функции:**

    Не всички модели поддържат повикване на функции, затова е важно да проверите дали използваният от вас LLM го поддържа.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> поддържа повикване на функции. Можем да започнем с иницииране на OpenAI клиент за Azure OpenAI **Responses API** (стабилната `/openai/v1/` крайна точка — не е необходим `api_version`). 

    ```python
    # Инициализиране на OpenAI клиента за Azure OpenAI (Responses API, v1 крайна точка)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Създайте схема на функция:**

    След това ще дефинираме JSON схема, която съдържа името на функцията, описание на това какво прави тя и имената и описанията на параметрите на функцията.
    След това ще предадем тази схема на клиента, създаден по-рано, заедно със заявката на потребителя за намиране на времето в Сан Франциско. Важно е да се отбележи, че се връща **повикване на инструмент**, а не окончателният отговор на въпроса. Както беше споменато по-рано, LLM връща името на функцията, избрана за задачата, и аргументите, които ще ѝ бъдат подадени.

    ```python
    # Описание на функцията за модела (формат на Responses API flat tool)
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
  
    # Първоначално съобщение от потребителя
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Първо повикване на API: Помолете модела да използва функцията
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # API за отговори връща повиквания на инструменти като function_call елементи в response.output.
    # Добавете ги към разговора, за да има моделът пълен контекст на следващия ход.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Кодът на функцията, необходим за изпълнение на задачата:**

    След като LLM е избрал коя функция трябва да бъде изпълнена, кодът, който реализира задачата, трябва да бъде имплементиран и изпълнен.
    Можем да реализираме кода за получаване на текущото време на Python. Също така ще трябва да напишем код, който извлича името и аргументите от response_message, за да получим крайния резултат.

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
    # Обработване на извиквания на функции
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Върнете резултата от инструмента като елемент function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Второ API извикване: Получаване на крайния отговор от модела
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

Повикването на функции е в сърцето на повечето, ако не на всички дизайни за използване на инструменти от агенти, но понякога реализирането му от нулата може да бъде предизвикателно.
Както научихме в [Урок 2](../../../02-explore-agentic-frameworks), агентните рамки ни предоставят предварително изградени строителни блокове за реализация на използване на инструменти.
 
## Примери за използване на инструменти с агентни рамки

Ето някои примери как можете да реализирате шаблона за използване на инструменти с различни агентни рамки:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> е рамка с отворен код за изграждане на AI агенти. Тя опростява процеса на използване на повикване на функции, като ви позволява да дефинирате инструменти като Python функции с декоратора `@tool`. Рамката управлява комуникацията между модела и вашия код. Тя осигурява достъп до предварително изградени инструменти като търсене във файлове и интерпретатор на код чрез `FoundryChatClient`.

Следната диаграма илюстрира процеса на повикване на функция с Microsoft Agent Framework:

![function calling](../../../translated_images/bg/functioncalling-diagram.a84006fc287f6014.webp)

В Microsoft Agent Framework инструментите се дефинират като декорирани функции. Можем да превърнем функцията `get_current_time`, която видяхме по-рано, в инструмент, като използваме декоратора `@tool`. Рамката автоматично ще сериализира функцията и нейните параметри, създавайки схема за изпращане към LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Създайте клиента
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Създайте агент и стартирайте с инструмента
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> е по-нова агентна рамка, проектирана да даде възможност на разработчиците да изграждат, внедряват и мащабират качествени и разширяеми AI агенти сигурно, без да се налага да управляват основните изчислителни и съхранителни ресурси. Тя е особено полезна за корпоративни приложения, тъй като е напълно управлявана услуга с корпоративно ниво на сигурност.

В сравнение с директното разработване с LLM API, Microsoft Foundry Agent Service предлага някои предимства, включително:

- Автоматично повикване на инструменти – няма нужда сами да анализирате повикване на инструмент, да извиквате инструмента и да обработвате отговора; всичко това сега се извършва на сървърната страна
- Сигурно управлявани данни – вместо да управлявате сами състоянието на разговора, можете да разчитате на нишки, които съхраняват цялата необходима информация
- Инструменти на момента – Инструменти, които можете да използвате за взаимодействие с вашите източници на данни, като Bing, Azure AI Search и Azure Functions.

Инструментите, налични в Microsoft Foundry Agent Service, могат да се разделят на две категории:

1. Инструменти за знание:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Свързване с Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Търсене във файлове</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Инструменти за действия:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Повикване на функции</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Интерпретатор на код</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Инструменти, дефинирани с OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service ни позволява да използваме тези инструменти заедно като `toolset`. Също така използва `нишки`, които проследяват историята на съобщенията от даден конкретен разговор.

Представете си, че сте търговски агент в компания, наречена Contoso. Искате да развиете разговорен агент, който може да отговаря на въпроси относно продажбените ви данни.

Следното изображение илюстрира как бихте могли да използвате Microsoft Foundry Agent Service за анализ на вашите продажбени данни:

![Agentic Service In Action](../../../translated_images/bg/agent-service-in-action.34fb465c9a84659e.webp)

За да използваме някой от тези инструменти с услугата, можем да създадем клиент и дефинираме инструмент или набор от инструменти. За да реализираме това практически, можем да използваме следния код на Python. LLM ще може да прегледа набора от инструменти и да реши дали да използва потребителската функция `fetch_sales_data_using_sqlite_query`, или предварително изградения Code Interpreter в зависимост от заявката на потребителя.

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

# Инициализиране на набор от инструменти
toolset = ToolSet()

# Инициализиране на агент за извикване на функция с функцията fetch_sales_data_using_sqlite_query и добавянето ѝ към набора от инструменти
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Инициализиране на инструмент Code Interpreter и добавянето му към набора от инструменти.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Какви са специалните съображения при използване на шаблона за използване на инструменти за изграждане на надеждни AI агенти?

Често срещан проблем при динамично генерирания SQL от LLM е сигурността, особено рискът от SQL инжекции или злонамерени действия, като сриване или манипулация на базата данни. Въпреки че тези опасения са валидни, те могат да бъдат ефективно смекчени чрез правилно конфигуриране на достъпните права до базата данни. За повечето бази данни това означава конфигуриране на базата данни като само за четене. При бази данни като PostgreSQL или Azure SQL, приложението трябва да бъде назначено с роля само за четене (SELECT).

Стартирането на приложението в сигурна среда допълнително повишава защитата. В корпоративни сценарии данните обикновено се извличат и трансформират от оперативни системи в база данни или склад за данни само за четене с потребителски ориентирана схема. Този подход гарантира, че данните са защитени, оптимизирани за производителност и достъпност, и че приложението има ограничен достъп само за четене.

## Примерни кодове

- Python: [Агентна рамка](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Агентна рамка](./code_samples/04-dotnet-agent-framework.md)

## Имате ли още въпроси относно шаблона за използване на инструменти?

Присъединете се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да се срещнете с други учащи, да посещавате часове за въпроси и да получите отговори на въпросите си за AI агенти.

## Допълнителни ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">WorkShop за Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">WorkShop за Contoso Creative Writer с многогласни агенти</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Преглед на Microsoft Agent Framework</a>


## Тест за дим на този агент (по избор)

След като научите как да разгръщате агенти в [Урок 16](../16-deploying-scalable-agents/README.md), можете да направите тест за дим на `TravelToolAgent` от този урок (дали все още използва своите инструменти и отговаря?) с помощта на [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Вижте [`tests/README.md`](../tests/README.md) за информация как да го стартирате.

## Предишен урок

[Разбиране на агентни дизайн модели](../03-agentic-design-patterns/README.md)

## Следващ урок

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->