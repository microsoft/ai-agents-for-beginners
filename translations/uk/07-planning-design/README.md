[![Патерн планування](../../../translated_images/uk/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Патерн планування

## Вступ

This lesson will cover

* Визначення чіткої загальної мети та розбиття складного завдання на керовані підзавдання.
* Використання структурованого виводу для більш надійних та машинозчитуваних відповідей.
* Застосування подієво-орієнтованого підходу для обробки динамічних завдань та неочікуваних вхідних даних.

## Цілі навчання

After completing this lesson, you will have an understanding about:

* Визначати та встановлювати загальну мету для агента ШІ, забезпечуючи чітке розуміння того, що потрібно досягти.
* Розбивати складне завдання на керовані підзавдання та організовувати їх у логічній послідовності.
* Оснащувати агентів відповідними інструментами (наприклад, інструментами пошуку або аналітики даних), визначати, коли і як їх використовувати, а також обробляти виникаючі непередбачені ситуації.
* Оцінювати результати підзавдань, вимірювати продуктивність і ітерувати дії для покращення кінцевого результату.

## Визначення загальної мети та розбиття завдання

![Визначення цілей і завдань](../../../translated_images/uk/defining-goals-tasks.d70439e19e37c47a.webp)

Більшість реальних завдань занадто складні, щоб вирішувати їх одним кроком. Агенту ШІ потрібна стисло сформульована мета, яка направляє його планування та дії. Наприклад, розглянемо мету:

    "Згенеруйте 3-денний маршрут подорожі."

Хоча її просто сформулювати, її все одно потрібно уточнити. Чим ясніша мета, тим краще агент (та будь-які люди-співпрацівники) можуть зосередитися на досягненні потрібного результату, наприклад на створенні вичерпного маршруту з варіантами перельотів, рекомендаціями готелів та пропозиціями активностей.

### Декомпозиція завдання

Великі або складні завдання стають керованішими, коли їх розбивають на менші, орієнтовані на мету підзавдання.
Для прикладу з маршрутом подорожі ви можете розбити мету на:

* Бронювання рейсів
* Бронювання готелю
* Оренда автомобіля
* Персоналізація

Кожне підзавдання можна виконувати спеціалізованими агентами або процесами. Один агент може спеціалізуватися на пошуку найкращих пропозицій на рейси, інший зосереджується на бронюванні готелів тощо. Координуючий або «downstream» агент потім може скомпілювати ці результати в один цілісний маршрут для кінцевого користувача.

Такий модульний підхід також дозволяє поступово вносити поліпшення. Наприклад, ви можете додати спеціалізованих агентів для рекомендацій щодо їжі або пропозицій місцевих заходів і з часом уточнювати маршрут.

### Структурований вивід

Large Language Models (LLMs) can generate structured output (e.g. JSON) that is easier for downstream agents or services to parse and process. This is especially useful in a multi-agent context, where we can action these tasks after the planning output is received.

The following Python snippet demonstrates a simple planning agent decomposing a goal into subtasks and generating a structured plan:

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

# Модель підзадачі подорожі
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # ми хочемо призначити завдання агенту

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Визначте повідомлення користувача
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

### Агент планування з оркестрацією кількох агентів

In this example, a Semantic Router Agent receives a user request (наприклад, "Мені потрібен план готелю для моєї поїздки.").

The planner then:

* Отримує план готелю: планувальник бере повідомлення користувача і, на основі системного підказу (включаючи інформацію про доступних агентів), генерує структурований план подорожі.
* Перелічує агентів та їх інструменти: реєстр агентів містить список агентів (наприклад, для рейсів, готелів, оренди авто та активностей) разом з функціями або інструментами, які вони пропонують.
* Направляє план відповідним агентам: залежно від кількості підзавдань планувальник або надсилає повідомлення безпосередньо спеціалізованому агенту (для сценаріїв з одним завданням), або координує через менеджера групового чату для спільної роботи кількох агентів.
* Підсумовує результат: нарешті планувальник узагальнює згенерований план для ясності.
The following Python code sample illustrates these steps:

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

# Модель підзадачі подорожі

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # ми хочемо призначити завдання агенту

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Створити клієнта

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Визначити повідомлення користувача

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

# Вивести вміст відповіді після завантаження його у форматі JSON

pprint(json.loads(response_content))
```

What follows is the output from the previous code and you can then use this structured output to route to `assigned_agent` and summarize the travel plan to the end user.

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

An example notebook with the previous code sample is available [here](07-python-agent-framework.ipynb).

### Ітеративне планування

Деякі завдання вимагають обміну інформацією або повторного планування, коли результат одного підзавдання впливає на наступне. Наприклад, якщо агент виявляє неочікуваний формат даних під час бронювання рейсів, йому може знадобитися адаптувати свою стратегію перед переходом до бронювання готелів.

Крім того, відгуки користувача (наприклад, коли людина вирішує, що віддає перевагу більш ранньому рейсу) можуть запустити часткове повторне планування. Такий динамічний, ітеративний підхід гарантує, що кінцеве рішення відповідає реальним обмеженням і змінюваним уподобанням користувача.

наприклад приклад коду

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. те саме, що й у попередньому коді, і передати історію користувача та поточний план

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
# .. перепланувати та надіслати завдання відповідним агентам
```

Для більш комплексного планування перегляньте Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">публікацію в блозі</a> щодо вирішення складних завдань.

## Підсумок

У цій статті ми розглянули приклад того, як можна створити планувальника, який динамічно обирає доступних визначених агентів. Вивід планувальника розбиває завдання і призначає агентів для їх виконання. Припускається, що агенти мають доступ до функцій/інструментів, необхідних для виконання завдання. Окрім агентів ви можете включити інші патерни, такі як рефлексія, підсумовувач і почерговий чат для подальшого налаштування.

## Додаткові ресурси

Magentic One - A Generalist multi-agent system for solving complex tasks and has achieved impressive results on multiple challenging agentic benchmarks. Reference: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. In this implementation the orchestrator creates task specific plans and delegates these tasks to the available agents. In addition to planning the orchestrator also employs a tracking mechanism to monitor the progress of the task and re-plans as required.

### Є ще питання щодо патерну планування?

Приєднуйтесь до [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), щоб зустрітися з іншими учнями, відвідати години консультацій та отримати відповіді на свої питання щодо агентів ШІ.

## Попередній урок

[Побудова надійних агентів ШІ](../06-building-trustworthy-agents/README.md)

## Наступний урок

[Патерн багатоагентної архітектури](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Відмова від відповідальності:
Цей документ було перекладено за допомогою сервісу перекладу на основі штучного інтелекту Co‑op Translator (https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, зверніть увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ у його рідній мові слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний переклад, виконаний людиною. Ми не несемо відповідальності за будь‑які непорозуміння чи хибні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->