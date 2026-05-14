[![Как да проектираме добри AI агенти](../../../translated_images/bg/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Кликнете върху изображението по-горе, за да гледате видеото на този урок)_

# Проектиране на използване на инструменти

Инструментите са интересни, защото позволяват на AI агентите да имат по-широк спектър от възможности. Вместо агентът да има ограничен набор от действия, които може да изпълнява, чрез добавяне на инструмент, агентът вече може да изпълнява широк спектър от действия. В тази глава ще разгледаме модела за проектиране на използване на инструменти, който описва как AI агентите могат да използват специфични инструменти, за да постигнат целите си.

## Въведение

В този урок ще отговорим на следните въпроси:

- Какво представлява моделът за проектиране на използване на инструменти?
- За кои случаи на употреба може да се приложи?
- Кои са елементите/строителните блокове, необходими за реализиране на модела?
- Какви са специалните съображения при използване на модела за проектиране на използване на инструменти за изграждане на надеждни AI агенти?

## Цели на обучението

След завършване на този урок ще можете да:

- Дефинирате модела за проектиране на използване на инструменти и неговата цел.
- Идентифицирате случаи на употреба, при които моделът е приложим.
- Разберете ключовите елементи, необходими за реализиране на модела.
- Разпознавате съображения за осигуряване на надеждност при AI агенти, използващи този модел.

## Какво представлява моделът за проектиране на използване на инструменти?

**Моделът за проектиране на използване на инструменти** се фокусира върху даването на възможност на големите езикови модели (LLMs) да взаимодействат с външни инструменти за постигане на конкретни цели. Инструментите са код, който може да бъде изпълнен от агент за извършване на действия. Инструмент може да е проста функция като калкулатор или API повикване към услуга на трета страна като проверка на цена на акции или прогнозиране на времето. В контекста на AI агенти, инструментите са проектирани да бъдат изпълнявани от агенти в отговор на **функционални повиквания, генерирани от модела**.

## За кои случаи на употреба може да се приложи?

AI агенти могат да използват инструменти, за да изпълняват сложни задачи, да извличат информация или да вземат решения. Моделът за използване на инструменти често се използва в сценарии, изискващи динамично взаимодействие с външни системи, като бази данни, уеб услуги или интерпретатори на код. Тази възможност е полезна за различни случаи на употреба, включително:

- **Динамично извличане на информация:** Агентите могат да изпращат заявки към външни API-та или бази данни за достъп до актуални данни (напр. заявки към SQLite база данни за анализ на данни, търсене на борсови цени или информация за времето).
- **Изпълнение и интерпретиране на код:** Агентите могат да изпълняват код или скриптове за решаване на математически задачи, генериране на отчети или симулации.
- **Автоматизация на работни потоци:** Автоматизиране на повтарящи се или многостъпкови работни процеси чрез интеграция на инструменти като планировчици на задачи, имейл услуги или данни през канали.
- **Клиентска поддръжка:** Агентите могат да комуникират с CRM системи, платформи за билети или бази знания за разрешаване на потребителски запитвания.
- **Генериране и редактиране на съдържание:** Агентите могат да използват инструменти като проверка на граматика, обобщаване на текст или оценка на безопасността на съдържание, за да подпомагат създаването на съдържание.

## Кои са елементите/строителните блокове, необходими за реализиране на модела за използване на инструменти?

Тези строителни блокове позволяват на AI агента да изпълнява широк набор от задачи. Нека разгледаме ключовите елементи, необходими за реализиране на модела за използване на инструменти:

- **Схеми на функции/инструменти:** Подробни дефиниции на наличните инструменти, включително име на функцията, цел, необходими параметри и очаквани изходи. Тези схеми позволяват на LLM да разбере какви инструменти са налични и как да изгради валидни заявки.

- **Логика за изпълнение на функции:** Управлява как и кога се извикват инструментите въз основа на намерението на потребителя и контекста на разговора. Това може да включва планови модули, механизми за маршрутизация или условни потоци, които динамично определят използването на инструменти.

- **Система за обработка на съобщения:** Компоненти, които управляват потока на разговор между входовете на потребителя, отговорите на LLM, повикванията към инструменти и изходите от инструменти.

- **Рамка за интеграция на инструменти:** Инфраструктура, която свързва агента с различни инструменти – дали те са прости функции или сложни външни услуги.

- **Обработка на грешки и валидиране:** Механизми за справяне с неизпълнения на инструменти, валидиране на параметри и управление на неочаквани отговори.

- **Управление на състоянието:** Следи контекста на разговора, предходните взаимодействия с инструменти и постоянните данни, за да осигури последователност при многократни взаимодействия.

Следва да разгледаме извикването на функции/инструменти по-подробно.

### Извикване на функции/инструменти

Извикването на функции е основният начин, по който позволяваме на големите езикови модели (LLMs) да взаимодействат с инструменти. Често ще срещнете „функция“ и „инструмент“ да се използват взаимозаменяемо, тъй като „функции“ (блокове от преизползваем код) са „инструментите“, които агентите използват за изпълнение на задачи. За да се извика код на функция, LLM трябва да сравни заявката на потребителя с описанието на функциите. За целта към LLM се изпраща схема, съдържаща описанията на всички налични функции. След това LLM избира най-подходящата функция за задачата и връща името и аргументите ѝ. Избраната функция се извиква, отговорът ѝ се изпраща обратно на LLM, който използва тази информация, за да отговори на заявката на потребителя.

За разработчици, желаещи да реализират извикване на функции за агенти, е необходимо:

1. Модел LLM, който поддържа извикване на функции
2. Схема с описания на функциите
3. Код за всяка описана функция

Нека илюстрираме с пример за получаване на текущото време в град:

1. **Иницииране на LLM, който поддържа извикване на функции:**

    Не всички модели поддържат извикване на функции, затова е важно да проверите дали използваният от вас LLM го прави. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> поддържа извикване на функции. Можем да започнем с иницииране на клиента на Azure OpenAI.

    ```python
    # Инициализиране на клиента на Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Създаване на схема на функция:**

    След това ще дефинираме JSON схема, съдържаща името на функцията, описание на това какво прави функцията и имената и описанията на нейните параметри.
    Ще предадем тази схема на клиента, създаден по-рано, заедно със заявката на потребителя да получи време в Сан Франциско. Важно е да се отбележи, че се връща **повикване на инструмент**, а **не** окончателен отговор на въпроса. Както споменахме по-рано, LLM връща името на функцията, която е избрал за задачата, и аргументите, които ще му бъдат подадени.

    ```python
    # Описание на функцията за модела за четене
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
  
    # Първо API повикване: Помолете модела да използва функцията
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
  
1. **Код на функцията, необходим за изпълнение на задачата:**

    След като LLM е избрал коя функция трябва да бъде изпълнена, кодът, който изпълнява задачата, трябва да бъде имплементиран и изпълнен.
    Можем да напишем код на Python за получаване на текущото време. Също така ще трябва да извадим името и аргументите от отговорното съобщение, за да вземем крайния резултат.

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
     # Обработвайте повиквания на функции
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
  
      # Второ API повикване: Получаване на окончателния отговор от модела
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

Извикването на функции е в основата на повечето, ако не и на всички модели за използване на инструменти при агенти, но имплементацията му от нулата може да бъде предизвикателна.
Както научихме в [Урок 2](../../../02-explore-agentic-frameworks), агентните рамки ни предоставят предварително изградени строителни блокове за реализиране на използване на инструменти.

## Примери за използване на инструменти с агентни рамки

Ето някои примери как може да реализирате модела за използване на инструменти чрез различни агентни рамки:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> е отворена AI рамка за изграждане на AI агенти. Тя опростява процеса на използване на извикване на функции, позволявайки да дефинирате инструменти като Python функции с декоратора `@tool`. Рамката управлява двупосочната комуникация между модела и вашия код. Също така предлага достъп до предварително изградени инструменти като Търсене на файлове и Интерпретатор на код чрез `AzureAIProjectAgentProvider`.

Следната диаграма илюстрира процеса на извикване на функции с Microsoft Agent Framework:

![function calling](../../../translated_images/bg/functioncalling-diagram.a84006fc287f6014.webp)

В Microsoft Agent Framework инструментите се дефинират като декорирани функции. Можем да преобразуваме функцията `get_current_time`, която видяхме по-рано, в инструмент, като използваме декоратора `@tool`. Рамката автоматично сериализира функцията и нейните параметри, създавайки схемата за изпращане към LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Създайте клиента
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Създайте агент и го стартирайте с инструмента
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> е по-нова агентна рамка, предназначена да даде възможност на разработчиците да изграждат, внедряват и мащабират висококачествени, разширяеми AI агенти сигурно, без да се налага да управляват основните изчислителни и съхранителни ресурси. Тя е особено полезна за корпоративни приложения, тъй като е напълно управлявана услуга с корпоративно ниво на сигурност.

В сравнение с разработване директно чрез LLM API, Azure AI Agent Service предлага някои предимства, включително:

- Автоматично извикване на инструменти – няма нужда да парсвате повикването на инструмент, да го извиквате и да обработвате отговора; всичко това вече се прави от страна на сървъра
- Сигурно управлявани данни – вместо да управлявате собственото си състояние на разговора, може да разчитате на нишки (threads), в които се съхранява цялата необходима информация
- Готови инструменти – инструменти, с които можете да взаимодействате с източниците на данни, като Bing, Azure AI Search и Azure Functions.

Инструментите налични в Azure AI Agent Service могат да се разделят в две категории:

1. Инструменти за знания:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Интеграция с Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Търсене на файлове</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Инструменти за действия:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Извикване на функции</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Интерпретатор на код</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Инструменти, дефинирани чрез OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Агентната услуга ни позволява да използваме тези инструменти заедно като `набор от инструменти`. Тя също използва `нишки` (threads), които следят историята на съобщенията от конкретен разговор.

Представете си, че сте търговски агент във фирма, наречена Contoso. Искате да разработите разговорен агент, който може да отговаря на въпроси за вашите данни за продажби.

Следващото изображение илюстрира как бихте могли да използвате Azure AI Agent Service за анализиране на данните за продажби:

![Agentic Service In Action](../../../translated_images/bg/agent-service-in-action.34fb465c9a84659e.webp)

За да използваме който и да е от тези инструменти с услугата, можем да създадем клиент и да дефинираме инструмент или набор от инструменти. За практическа реализация можем да използваме следния Python код. LLM ще може да разгледа набора от инструменти и да реши дали да използва потребителската функция `fetch_sales_data_using_sqlite_query` или предварително изградения Интерпретатор на код в зависимост от заявката на потребителя.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # функция fetch_sales_data_using_sqlite_query, която може да бъде намерена във файл fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Инициализиране на набора от инструменти
toolset = ToolSet()

# Инициализиране на агент за извикване на функции с функцията fetch_sales_data_using_sqlite_query и добавянето ѝ към набора от инструменти
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Инициализиране на инструмент Code Interpreter и добавянето му към набора от инструменти.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Какви са специалните съображения при използване на модела за проектиране на използване на инструменти за изграждане на надеждни AI агенти?

Чест проблем при динамично генерирани SQL заявки от LLM е сигурността, особено рискът от SQL инжекция или злонамерени действия, като изтриване или манипулация на базата данни. Докато тези опасения са валидни, те могат да бъдат ефективно смекчени чрез правилно конфигуриране на правата за достъп до базата данни. За повечето бази се конфигурира база данни в режим само за четене. За бази данни като PostgreSQL или Azure SQL приложението трябва да бъде с назначена роля само за четене (SELECT).

Изпълнението в сигурна среда допълнително повишава защитата. В корпоративни сценарии данните обикновено се извличат и трансформират от оперативни системи в база данни или склад за данни в режим само за четене с удобна за потребителя схема. Този подход осигурява, че данните са защитени, оптимизирани по отношение на производителността и достъпността, и че приложението има ограничен достъп само за четене.

## Примери с код

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Имате ли още въпроси за моделите за използване на инструменти?

Присъединете се към [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), за да се свържете с други обучаващи се, да участвате в работни сесии и да получите отговори на въпросите си за AI агенти.

## Допълнителни ресурси

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Работилница за Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Работилница Multi-Agent за Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Преглед на Microsoft Agent Framework</a>

## Предходен урок

[Разбиране на агентните модели за проектиране](../03-agentic-design-patterns/README.md)

## Следващ урок
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->