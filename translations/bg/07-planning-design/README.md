[![Планиращ дизайн патърн](../../../translated_images/bg/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Кликнете върху изображението по-горе, за да гледате видеото на този урок)_

# Планиращ дизайн

## Въведение

Този урок ще разгледа

* Дефиниране на ясна обща цел и разбиване на сложна задача на управляеми задачи.
* Използване на структурирана изходна информация за по-надеждни и машинно четими отговори.
* Прилагане на подход, базиран на събития, за обработка на динамични задачи и непредвидени входове.

## Учебни цели

След завършване на този урок ще имате разбиране за:

* Идентифициране и задаване на обща цел за AI агент, като се гарантира, че той ясно знае какво трябва да бъде постигнато.
* Декомпозиране на сложна задача на управляеми подзадачи и организирането им в логическа последователност.
* Оборудване на агентите с подходящи инструменти (например инструменти за търсене или за анализ на данни), решаване кога и как да ги използват и справяне с неочаквани ситуации.
* Оценяване на резултатите от подзадачите, измерване на производителността и повтаряне на действията за подобряване на крайния резултат.

## Дефиниране на общата цел и разбиване на задача

![Дефиниране на цели и задачи](../../../translated_images/bg/defining-goals-tasks.d70439e19e37c47a.webp)

Повечето реални задачи са твърде сложни, за да бъдат решени на един етап. AI агентът се нуждае от кратка цел, която да насочва планирането и действията му. Например, разгледайте целта:

    "Създаване на тридневен план за пътуване."

Въпреки че изглежда проста, тя все пак се нуждае от уточнение. Колкото по-ясна е целта, толкова по-добре агентът (и всички човешки сътрудници) може да се фокусират върху постигането на правилния резултат, като създаването на цялостен план с опции за полети, препоръки за хотели и предложения за дейности.

### Декомпозиция на задачи

Големите или сложни задачи стават по-управляеми, когато са разделени на по-малки, ориентирани към целта подзадачи.
За примера с плана за пътуване, можете да разградите целта на:

* Резервация на полети
* Резервация на хотел
* Наем на кола
* Персонализация

Всяка подзадача може да бъде изпълнена от посветени агенти или процеси. Един агент може да се специализира в търсене на най-добрите оферти за полети, друг се фокусира върху резервациите на хотели и т.н. Координиращ или „нисен“ агент след това може да събере тези резултати в един цялостен план за крайния потребител.

Този модулен подход също така позволява постепенно подобрение. Например, може да добавите специализирани агенти за препоръки за храна или предложения за местни дейности и да усъвършенствате плана с времето.

### Структурирана изходна информация

Големите езикови модели (LLMs) могат да генерират структурирана изходна информация (например JSON), която е по-лесна за обработване и парсиране от по-нисходящи агенти или услуги. Това е особено полезно в контекст с много агенти, където можем да изпълним задачите след получаване на плана.

Следният фрагмент на Python демонстрира прост планиращ агент, който декомпозира цел на подзадачи и генерира структуриран план:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.foundry import FoundryChatClient
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

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Определете потребителското съобщение
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

### Планиращ агент с многоагентска оркестрация

В този пример агент Семантичен рутер получава заявка от потребител (например, "Имам нужда от план за хотел за моето пътуване.").

Планиращият агент след това:

* Получава плана за хотели: Планиращият взима съобщението на потребителя и, базирано на системно подсещане (включително налична информация за агенти), генерира структуриран план за пътуване.
* Изброява агенти и техните инструменти: Регистърът на агенти съдържа списък с агенти (например за полети, хотели, коли под наем и дейности) заедно с функциите или инструментите, които те предлагат.
* Насочва плана към съответните агенти: В зависимост от броя на подзадачите, планиращият или изпраща съобщението директно на посветен агент (за еднозадачни сценарии), или координира чрез мениджър на групов чат за многоагентско сътрудничество.
* Обобщава резултата: Накрая планиращият обобщава генерирания план за яснота.
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

# Модел на подзадача за пътуване

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

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Създайте клиента

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Определете съобщението на потребителя

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

По-долу е изходът от предходния код и можете да използвате тази структурирана информация, за да я насочите към `assigned_agent` и да обобщите плана за пътуване за крайния потребител.

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

Примерна тетрадка с предишния примерен код е достъпна [тук](./code_samples/07-python-agent-framework.ipynb).

### Итеративно планиране

Някои задачи изискват обратно и напред или пренасочване на плана, където резултатът на една подзадача влияе на следващата. Например, ако агентът открие неочакван формат на данните при резервацията на полети, може да се наложи да адаптира стратегията си преди да премине към резервацията на хотел.

Освен това, обратната връзка от потребителя (например човек, който реши, че предпочита по-ранен полет) може да задейства частично пренасочване на плана. Този динамичен, итеративен подход гарантира, че крайното решение съответства на реалните ограничения и променящите се предпочитания на потребителя.

например код

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. същото като предишния код и предаване на историята на потребителя, текущия план

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
# .. пренасочване и изпращане на задачите към съответните агенти
```

За по-комплексно планиране разгледайте Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Блогпост</a> за решаване на сложни задачи.

## Обобщение

В тази статия разгледахме пример как да създадем планиращ агент, който динамично избира наличните агенти. Изходът на планиращия агент декомпозира задачите и разпределя агентите, за да може те да бъдат изпълнени. Предполага се, че агентите разполагат с необходимите функции/инструменти за изпълнение на задачата. В допълнение към агентите можете да включите и други патърни като отражение, обобщение и кръгов чат за допълнително персонализиране.

## Допълнителни ресурси

Magnetic One - Общ многоагентски систем за решаване на сложни задачи, който е постигнал впечатляващи резултати на множество предизвикателни агентски бенчмаркове. Референция: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. В тази имплементация оркестраторът създава специфични планове за задачите и ги делегира на наличните агенти. Освен планирането, оркестраторът използва и механизъм за следене на напредъка на задачата и пренасочва плана при необходимост.

### Имате ли повече въпроси относно Планиращия дизайн патърн?

Присъединете се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да се срещнете с други учащи, да посетите офис часове и да получите отговори на въпросите си за AI агенти.

## Предходен урок

[Създаване на надеждни AI агенти](../06-building-trustworthy-agents/README.md)

## Следващ урок

[Многоагентски дизайн патърн](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->