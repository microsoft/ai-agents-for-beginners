[![Planning Design Pattern](../../../translated_images/uk/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Натисніть на зображення вище, щоб переглянути відео цього уроку)_

# Планування Дизайну

## Вступ

У цьому уроці буде розглянуто

* Визначення чіткої загальної мети та розбиття складного завдання на керовані підзадачі.
* Використання структурованого виводу для більш надійних та машинозчитуваних відповідей.
* Застосування підходу, що базується на подіях, для обробки динамічних завдань та несподіваних вхідних даних.

## Цілі навчання

Після завершення цього уроку ви матимете розуміння про:

* Визначення та встановлення загальної мети для AI агента, щоб він чітко розумів, що потрібно досягти.
* Розподіл складного завдання на керовані підзадачі та організація їх у логічній послідовності.
* Забезпечення агентів потрібними інструментами (наприклад, інструментами пошуку або аналітики даних), вирішення коли і як їх використовувати, а також обробка несподіваних ситуацій, що виникають.
* Оцінка результатів підзадач, вимірювання ефективності та ітерація дій для покращення кінцевого результату.

## Визначення загальної мети та розбиття завдання

![Defining Goals and Tasks](../../../translated_images/uk/defining-goals-tasks.d70439e19e37c47a.webp)

Більшість завдань у реальному житті занадто складні, щоб виконувати їх за один крок. AI агенту потрібна стисло сформульована ціль для керування плануванням і діями. Наприклад, розглянемо мету:

    "Створити триденний маршрут подорожі."

Хоча це просто сформульовано, все ж потребує уточнення. Чіткість мети дозволяє агенту (та будь-яким співпрацівникам) зосередитися на досягненні правильного результату, наприклад, створенні комплексного маршруту з варіантами рейсів, рекомендаціями готелів та пропозиціями активностей.

### Розбиття завдання

Великі або складні завдання стають більш керованими, коли їх розбивають на менші цілеспрямовані підзадачі.
Для прикладу маршруту подорожі ви можете розбити мету на:

* Бронювання рейсів
* Бронювання готелів
* Оренда автомобіля
* Персоналізація

Кожну підзадачу може виконувати конкретний агент або процес. Один агент може спеціалізуватись на пошуку найкращих пропозицій рейсів, інший — на бронюванні готелів тощо. Координуючий або «низькошаровий» агент потім збирає ці результати в єдиний цілісний маршрут для кінцевого користувача.

Цей модульний підхід також дозволяє впроваджувати поступові вдосконалення. Наприклад, можна додати спеціалізовані агенти для рекомендацій їжі чи місцевих заходів і з часом удосконалювати маршрут.

### Структурований вивід

Великі мовні моделі (LLMs) можуть генерувати структурований вивід (наприклад, JSON), який легше опрацьовувати агентах чи службах на нижчому рівні. Це особливо корисно у контексті багатагентної взаємодії, де можна виконувати ці завдання після отримання плану.

Наступний приклад Python демонструє простий агент планування, який розбиває мету на підзадачі та генерує структурований план:

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

# Модель підзадачі подорожі
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # ми хочемо призначити завдання агенту

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

### Агент планування з багатагентною оркестрацією

У цьому прикладі агент Semantic Router отримує запит користувача (наприклад, "Мені потрібен план готелю для моєї поїздки.").

Планувальник виконує:

* Отримує План Готелю: планувальник бере повідомлення користувача і, ґрунтуючись на системному підказці (включно з деталями доступних агентів), генерує структурований план подорожі.
* Перелічує агентів та їхні інструменти: реєстр агентів містить список агентів (наприклад, для рейсів, готелів, оренди автомобілів та активностей) разом із функціями чи інструментами, які вони пропонують.
* Маршрутизує План до відповідних агентів: залежно від кількості підзадач, планувальник або прямо надсилає повідомлення виділеному агенту (для однотаскових сценаріїв), або координує через менеджера групового чату для багатагентної співпраці.
* Підсумовує результат: зрештою планувальник підсумовує створений план задля ясності.
Наступний код Python ілюструє ці кроки:

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

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Створити клієнта

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

# Вивести вміст відповіді після завантаження у форматі JSON

pprint(json.loads(response_content))
```

Що далі наведене — це вивід попереднього коду, і ви можете використати цей структурований вивід для маршрутизації до `assigned_agent` та підсумування плану подорожі кінцевому користувачу.

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

Приклад ноутбука з попереднім кодом доступний [тут](./code_samples/07-python-agent-framework.ipynb).

### Ітераційне планування

Деякі завдання вимагають повторного обговорення або перепланування, коли результат однієї підзадачі впливає на наступну. Наприклад, якщо агент виявляє несподіваний формат даних під час бронювання рейсів, йому можливо доведеться адаптувати стратегію перед тим, як перейти до бронювання готелів.

Крім того, зворотній зв’язок від користувача (наприклад, людина вирішує, що віддає перевагу більш ранньому рейсу) може спричинити часткове перепланування. Цей динамічний, ітеративний підхід гарантує, що кінцеве рішення узгоджується з реальними обмеженнями та зміною вподобань користувачів.

наприклад код

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. те саме, що і в попередньому коді, і передати історію користувача, поточний план

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
# .. перепланувати і надіслати завдання відповідним агентам
```

Для більш комплексного планування ознайомтесь з Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">публікацією в блозі</a> для розв’язання складних завдань.

## Підсумок

У цій статті ми розглянули приклад створення планувальника, який може динамічно вибирати доступних визначених агентів. Результат роботи планувальника розбиває завдання і призначає агентів, щоб вони могли їх виконувати. Припускається, що агенти мають доступ до функцій/інструментів, необхідних для виконання завдання. Крім агентів, ви можете додати інші патерни, такі як рефлексія, сумаризатор і циклічний чат для подальшої кастомізації.

## Додаткові ресурси

Magentic One - Загальний багатагентний система для розв’язання складних завдань із вражаючими результатами на багатьох складних агентних тестах. Посилання: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. У цій реалізації оркестратор створює планування задач і делегує їх доступним агентам. Крім планування, оркестратор також застосовує механізм відстеження прогресу виконання завдання і переплановує за потреби.

### Є більше питань про патерн планування?

Приєднуйтесь до [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), щоб зустріти інших учасників, відвідати офісні години та отримати відповіді на питання щодо AI агентів.

## Попередній урок

[Створення надійних AI агентів](../06-building-trustworthy-agents/README.md)

## Наступний урок

[Патерн багатогентної взаємодії](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:
Цей документ було перекладено за допомогою сервісу штучного інтелекту для перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->