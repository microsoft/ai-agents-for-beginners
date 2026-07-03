[![Planning Design Pattern](../../../translated_images/bg/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Кликнете върху горното изображение, за да гледате видеото на този урок)_

# Планиране на дизайн

## Въведение

Този урок ще разгледа

* Определяне на ясен обща цел и разделяне на сложна задача на управляеми задачи.
* Използване на структурирани резултати за по-надеждни и машинно-разбираеми отговори.
* Прилагане на подход, управляван от събития, за справяне с динамични задачи и непредвидени входни данни.

## Учебни цели

След завършване на този урок ще имате разбиране за:

* Идентифициране и задаване на обща цел за AI агент, като се гарантира, че той ясно знае какво трябва да се постигне.
* Разлагане на сложна задача на управляеми подзадачи и организирането им в логическа последователност.
* Осигуряване на агентите с правилните инструменти (например търсачки или инструменти за анализ на данни), решаване кога и как да се използват и справяне с непредвидени ситуации, които възникват.
* Оценяване на резултатите от подзадачите, измерване на изпълнението и итерация върху действията за подобряване на крайния резултат.

## Определяне на общата цел и разделяне на задача

![Defining Goals and Tasks](../../../translated_images/bg/defining-goals-tasks.d70439e19e37c47a.webp)

Повечето задачи от реалния свят са твърде сложни, за да се изпълнят на един етап. AI агентът се нуждае от кратка цел, която да насочва планирането и действията му. Например, разгледайте целта:

    "Създаване на тридневен пътуващ маршрут."

Въпреки че изглежда проста, тя все още се нуждае от уточнение. Колкото по-ясна е целта, толкова по-добре агентът (и всеки човек, който си сътрудничи) може да се съсредоточи върху постигането на желания резултат, като например създаване на всеобхватен маршрут с опции за полети, препоръки за хотели и предложения за дейности.

### Разлагане на задача

Големи или сложни задачи стават по-управляеми, когато се разделят на по-малки, целенасочени подзадачи.
В примера с пътуващия маршрут, може да се разложи целта на:

* Резервация на полет
* Резервация на хотел
* Наем на кола
* Персонализация

Всяка подзадача може да бъде изпълнена от специализирани агенти или процеси. Един агент може да е експерт в търсене на най-добрите оферти за полети, друг се фокусира върху резервации на хотели и т.н. Координиращ или „надолу по веригата“ агент може да обедини тези резултати в един цялостен маршрут за крайния потребител.

Този модулен подход също позволява постепенно подобрение. Например, може да добавите специализирани агенти за препоръки за храна или местни активности и с времето да усъвършенствате маршрута.

### Структуриран изход

Големите езикови модели (LLMs) могат да генерират структуриран изход (например JSON), който е по-лесен за парсване и обработване от последващи агенти или услуги. Това е особено полезно в мултиагентски контекст, където можем да изпълним тези задачи след получаване на планиращия изход.

Следният Python код демонстрира прост планиращ агент, който разлага цел на подзадачи и генерира структуриран план:

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
    assigned_agent: AgentEnum  # искаме да зададем задачата на агента

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

### Планиращ агент с мултиагентска оркестрация

В този пример Семантичният маршрутизиращ агент получава потребителско запитване (напр. "Имам нужда от план за хотел за пътуването си.").

Планиращият агент след това:

* Получава плана за хотел: той взема съобщението на потребителя и на базата на системна подсказка (включително налични агенти) генерира структуриран пътуващ план.
* Изброява агентите и техните инструменти: регистърът на агентите съдържа списък с агенти (напр. за полети, хотели, коли под наем и дейности) заедно с функциите или инструментите, които предлагат.
* Пренасочва плана към съответните агенти: в зависимост от броя на подзадачите, планиращият или изпраща съобщението директно на специализиран агент (за еднозадачни сценарии), или координира чрез мениджър на групов чат за мултиагентско сътрудничество.
* Обобщава резултата: накрая планиращият обобщава генерирания план за по-голяма яснота.
Следният Python пример илюстрира тези стъпки:

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

# Модел за Подзадача Пътуване

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

Това, което следва, е изходът от горния код и можете да използвате този структуриран изход, за да го пренасочите към `assigned_agent` и да обобщите пътуващия план за крайния потребител.

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

Примерен бележник с горния код е наличен [тук](07-python-agent-framework.ipynb).

### Итеративно планиране

Някои задачи изискват повторни обсъждания или препланиране, където резултатът от една подзадача влияе на следващата. Например, ако агентът открие неочакван формат на данни по време на резервация на полети, той може да трябва да адаптира стратегията си преди да продължи с резервациите на хотели.

Освен това, обратната връзка от потребителя (например човешко предпочитание за по-ранен полет) може да задейства частично препланиране. Този динамичен, итеративен подход осигурява, че крайното решение е съобразено с реалните ограничения и променящите се предпочитания на потребителя.

напр. примерен код

```python
from agent_framework.azure import AzureAIProjectAgentProvider
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
# .. презапланирай и изпрати задачите на съответните агенти
```

За по-подробно планиране разгледайте Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">блог пост</a> за решаване на сложни задачи.

## Обобщение

В тази статия разгледахме пример как можем да създадем планиращ агент, който динамично избира наличните дефинирани агенти. Изходът на планиращия разгражда задачите и назначава агентите за изпълнение. Предполага се, че агентите имат достъп до функциите/инструментите, необходими за изпълнение на задачата. Освен агентите може да включите и други шаблони като рефлексия, обобщаващ агент и кръгов чат за допълнително персонализиране.

## Допълнителни ресурси

Magentic One - универсална мултиагентска система за решаване на сложни задачи, постигнала впечатляващи резултати в множество предизвикателни мултиагентски тестове. Референция: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. В тази реализация оркестраторът създава специфични планове за задачи и делегира тези задачи на наличните агенти. Освен планиране, оркестраторът прилага и механизъм за проследяване на напредъка и препланира при необходимост.

### Имаш ли още въпроси относно шаблона за планиране?

Присъедини се към [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), за да се срещнеш с други обучаващи се, да участваш в офис часове и да получиш отговори на въпросите си относно AI агентите.

## Предишен урок

[Създаване на надеждни AI агенти](../06-building-trustworthy-agents/README.md)

## Следващ урок

[Шаблон за мултиагентски дизайн](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводачески услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->