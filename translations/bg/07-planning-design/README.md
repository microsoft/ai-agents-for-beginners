[![Planning Design Pattern](../../../translated_images/bg/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Кликнете върху горното изображение, за да гледате видеото на този урок)_

# Planning Design

## Въведение

Този урок ще покрие

* Дефиниране на ясен обща цел и разбиване на сложна задача на управляеми задачи.
* Използване на структурирани резултати за по-надеждни и машинно-читаеми отговори.
* Прилагане на събитийно ориентиран подход за справяне с динамични задачи и неочаквани входове.

## Цели за учене

След завършване на този урок, ще имате разбиране за:

* Идентифициране и задаване на обща цел за AI агент, като се гарантира, че ясно знае какво трябва да бъде постигнато.
* Декомпозиране на сложна задача на управляеми подзадачи и организирането им в логическа последователност.
* Оборудване на агенти с правилните инструменти (например търсачки или инструменти за анализа на данни), решаване кога и как да бъдат използвани, и справяне с неочаквани ситуации, които възникват.
* Оценка на резултатите от подзадачите, измерване на представянето и итерация на действията за подобряване на крайния резултат.

## Дефиниране на общата цел и разбиване на задача

![Defining Goals and Tasks](../../../translated_images/bg/defining-goals-tasks.d70439e19e37c47a.webp)

Повечето реални задачи са твърде сложни, за да се решат с един единствен ход. AI агентът се нуждае от сбита цел, която да насочва планирането и действията му. Например, разгледайте целта:

    "Създай 3-дневен пътешественически план."

Въпреки че е лесно да се заяви, тя все още се нуждае от доуточняване. Колкото по-ясна е целта, толкова по-добре агентът (и всички човешки колеги) могат да се фокусират върху постигането на правилния резултат, като създаване на подробен план с опции за полети, препоръки за хотели и предложения за дейности.

### Декомпозиране на задачата

Големите или сложни задачи стават по-управляеми, когато се разделят на по-малки, целево насочени подзадачи.
За примера с план за пътуване, можете да декомпозирате целта на:

* Резервация на полети
* Резервация на хотел
* Наем на кола
* Персонализация

Всяка подзадача може да бъде решена от отделни агенти или процеси. Един агент може да се специализира в търсене на най-добрите оферти за полети, друг да се фокусира върху резервации на хотели и т.н. Координиращият или „последващ“ агент може да комбинира тези резултати в един цялостен маршрут за крайния потребител.

Този модулен подход позволява също инкрементални подобрения. Например, може да добавите специализирани агенти за препоръки на храна или предложения за местни дейности и да усъвършенствате маршрута с времето.

### Структуриран резултат

Големите езикови модели (LLMs) могат да генерират структуриран изход (напр. JSON), който е по-лесен за обработка и парсване от последващи агенти или услуги. Това е особено полезно в многoагентен контекст, където можем да изпълняваме задачи след получаването на плана от планирания модул.

Следният пример на Python демонстрира прост планиращ агент, който декомпозира целта на подзадачи и създава структуриран план:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Модел за подзадача за пътуване
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # искаме да възложим задачата на агента

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Дефинирайте съобщението на потребителя
system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```

### Планиращ агент с координация на множество агенти

В този пример, Семантичен Роутер Агент получава потребителска заявка (например, "Имам нужда от план за хотел за пътуването си.").

Планиращият модул след това:

* Получава плана за хотел: Планиращият взема съобщението на потребителя и, базирайки се на системно подканяне (включително детайли за наличните агенти), генерира структуриран план за пътуване.
* Изброява агенти и техните инструменти: Регистърът на агенти държи списък с агенти (например за полети, хотели, наем на коли и дейности), заедно с функциите или инструментите, които предлагат.
* Пренасочва плана към съответните агенти: В зависимост от броя на подзадачите, планиращият или изпраща съобщението директно на специализиран агент (за едно- задача сценарии), или координира чрез мениджър на групов чат за многoагентно сътрудничество.
* Обобщава резултата: Накрая, планиращият обобщава генерирания план за яснота.
Следният примерен код на Python илюстрира тези стъпки:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Модел за подвъзлаза на пътуване

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # искаме да възложим задачата на агента

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Създайте клиента

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Определете потребителското съобщение

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# Отпечатайте съдържанието на отговора след зареждането му като JSON

pprint(json.loads(response_content))
```

По-долу е изходът от предходния код и можете след това да използвате този структуриран резултат, за да насочите към `assigned_agent` и да обобщите плана за пътуване за крайния потребител.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

Примерен тетрадка с предходния примерен код е налична [тук](07-python-agent-framework.ipynb).

### Итеративно планиране

Някои задачи изискват двупосочна комуникация или повторно планиране, където резултатът от една подзадача влияе на следващата. Например, ако агентът открие неочакван формат на данни при резервацията на полети, може да се наложи да адаптира своята стратегия, преди да премине към резервации на хотели.

Освен това, обратната връзка от потребителя (например ако човек прецени, че предпочита по-ранен полет) може да задейства частично ново планиране. Този динамичен, итеративен подход гарантира, че крайното решение съответства на реалните ограничения и променящите се предпочитания на потребителите.

примерен код

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. същото като предишния код и предавайте историята на потребителя, текущия план

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. пренасрочете и изпратете задачите до съответните агенти
```

За по-пълноценно планиране, разгледайте Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Блогпост</a> за решаване на сложни задачи.

## Обобщение

В тази статия разгледахме пример за това как можем да създадем планировчик, който динамично избира наличните агенти, които са дефинирани. Изходът на Планировчика декомпозира задачите и назначава агентите, за да могат те да бъдат изпълнени. Предполага се, че агентите имат достъп до функциите/инструментите, необходими за изпълнение на задачата. Освен агенти можете да включите и други модели като рефлексия, обобщител и round robin чат за допълнително персонализиране.

## Допълнителни ресурси

Magentic One - Общ многоагентен система за решаване на сложни задачи и е постигнала впечатляващи резултати по множество предизвикателни агенционни показатели. Референция: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. В тази имплементация оркестраторът създава планове, специфични за задачи, и делегира тези задачи на наличните агенти. Освен планирането, оркестраторът използва и механизъм за проследяване на напредъка на задачата и пре-планира при необходимост.

### Имате още въпроси относно модела за планиране?

Присъединете се към [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), за да се срещнете с други обучаващи се, да посещавате часове за консултации и да получите отговори на въпросите си за AI агенти.

## Предишен урок

[Изграждане на надеждни AI агенти](../06-building-trustworthy-agents/README.md)

## Следващ урок

[Модел за многoагентен дизайн](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия първоначален език трябва да се счита за авторитетен източник. За важна информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да било недоразумения или погрешни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->