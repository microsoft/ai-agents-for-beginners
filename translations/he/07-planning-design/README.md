[![תבנית עיצוב לתכנון](../../../translated_images/he/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(לחצו על התמונה למעלה כדי לצפות בסרטון של השיעור הזה)_

# תבנית תכנון

## הקדמה

בשיעור זה נלמד את הנושאים הבאים:

* הגדרת מטרה כללית ברורה והפיכת משימה מורכבת למשימות ניתנות לניהול.
* שימוש בפלט מובנה לקבלת תגובות אמינות יותר וקריאות על ידי מכונה.
* יישום גישה מונעת-אירועים לטיפול במשימות דינמיות וקלטים בלתי צפויים.

## יעדי למידה

בסיום שיעור זה תבין את הדברים הבאים:

* לזהות ולקבוע מטרה כוללת עבור סוכן בינה מלאכותית, ולהבטיח שהוא יודע בצורה ברורה מה יש להשיג.
* לפרק משימה מורכבת לתתי-משימות ניתנות לניהול ולארגן אותן בסדר לוגי.
* לספק לסוכנים את הכלים המתאימים (למשל, כלי חיפוש או כלי ניתוח נתונים), להחליט מתי וכיצד להשתמש בהם, ולנהל מצבים בלתי צפויים שעשויים לצוץ.
* להעריך תוצאות תתי-המשימות, למדוד ביצועים ולחזור על פעולות כדי לשפר את התוצאה הסופית.

## הגדרת המטרה הכוללת ופירוק משימה

![הגדרת מטרות ומשימות](../../../translated_images/he/defining-goals-tasks.d70439e19e37c47a.webp)

רוב המשימות בעולם האמיתי מורכבות מדי כדי להתמודד עמן בצעד אחד. סוכן בינה מלאכותית זקוק למטרה תמציתית כדי להנחות את התכנון והפעולות שלו. לדוגמה, שקלו את המטרה:

    "צור מסלול טיול ל־3 ימים."

אמנם קל לנוסח, אך היא עדיין דורשת דיוק נוסף. ככל שהמטרה ברורה יותר, כך הסוכן (וכל שותפי אנוש) יכולים להתמקד בהשגת התוצאה הנכונה, כגון יצירת מסלול מפורט הכולל אפשרויות טיסות, המלצות למלונות והצעות לפעילויות.

### פירוק המשימה

משימות גדולות או מורכבות נעשות ניתנות לניהול יותר כאשר מפצלים אותן לתת-משימות קטנות וממוקדות מטרה.
למשל עבור דוגמת מסלול הטיול, ניתן לפרק את המטרה ל:

* הזמנת טיסה
* הזמנת מלון
* השכרת רכב
* התאמה אישית

אז ניתן לטפל בכל תת-משימה על ידי סוכנים או תהליכים ייעודיים. סוכן אחד עשוי להתמחות בחיפוש הדילים הטובים ביותר לטיסות, סוכן אחר יתמקד בהזמנות מלון, וכן הלאה. סוכן מתאם או סוכן “downstream” יוכל לאסוף את התוצאות הללו למסלול אחד מלוכד עבור המשתמש הקצה.

גישה מודולרית זו מאפשרת גם שיפורים הדרגתיים. לדוגמה, ניתן להוסיף סוכנים מתמחים להמלצות אוכל או להצעות לפעילויות מקומיות ולשכלל את המסלול עם הזמן.

### פלט מובנה

מודלים לשוניים גדולים (LLMs) יכולים ליצור פלט מובנה (למשל JSON) שקל יותר לסוכנים או לשירותים "downstream" לפרסר ולעבד. זה שימושי במיוחד בהקשר רב-סוכני, שבו ניתן לבצע פעולות על המשימות לאחר קבלת פלט התכנון.

קטע הקוד ב-Python הבא מדגים סוכן תכנון פשוט הפורק מטרה לתתי-משימות ויוצר תוכנית מובנית:

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

# מודל תת-משימה לנסיעה
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # אנו רוצים להקצות את המשימה לסוכן

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# הגדר את הודעת המשתמש
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

### סוכן תכנון עם תזמור רב-סוכני

בדוגמה זו, סוכן ניתוב סמנטי מקבל בקשת משתמש (למשל, "אני צריך תוכנית מלון עבור הטיול שלי.").

לאחר מכן, המתכנן:

* מקבל את תוכנית המלון: המתכנן לוקח את הודעת המשתמש ובאמצעות תבנית מערכת (כולל פרטים על הסוכנים הזמינים), מייצר תוכנית נסיעה מובנית.
* רושם את הסוכנים וכלי העבודה שלהם: רישום הסוכנים מחזיק ברשימת סוכנים (למשל, לטיסות, מלונות, השכרת רכבים ופעילויות) יחד עם הפונקציות או הכלים שהם מציעים.
* מנתב את התוכנית לסוכנים המתאימים: בהתאם למספר תתי-המשימות, המתכנן או שולח את ההודעה ישירות לסוכן ייעודי (בתרחישי משימה יחידה) או מתאם באמצעות מנהל צ'אט קבוצתי לשיתוף פעולה רב-סוכני.
* מסכם את התוצאה: בסופו של דבר, המתכנן מסכם את התוכנית שנוצרה לצורך הבהרה.
דוגמת קוד ה-Python הבאה ממחישה שלבים אלה:

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

# מודל תת-משימה לנסיעות

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # אנחנו רוצים להקצות את המשימה לסוכן

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# צור את הלקוח

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# הגדר את הודעת המשתמש

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

# הדפס את תוכן התגובה לאחר טעינתו כ-JSON

pprint(json.loads(response_content))
```

להלן הפלט מהקוד הקודם, ואפשר להשתמש בפלט המובנה הזה כדי לנתב ל-`assigned_agent` ולסכם את תוכנית הנסיעה עבור המשתמש הקצה.

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

מחברת דוגמה עם דוגמת הקוד הנ״ל זמינה [כאן](07-python-agent-framework.ipynb).

### תכנון איטרטיבי

חלק מהמשימות דורשות תהליך של עשייה חוזרת או תכנון מחדש, שבו תוצאתה של תת-משימה משפיעה על הבאה. לדוגמה, אם הסוכן מגלל פורמט נתונים בלתי צפוי בעת הזמנת טיסות, ייתכן שיהיה צורך להתאים את האסטרטגיה לפני המעבר להזמנות מלון.

בנוסף, משוב משתמש (למשל, אדם שמחליט שהוא מעדיף טיסה מוקדמת יותר) יכול להפעיל תכנון מחלקי מחדש. גישה דינמית ואיטרטיבית זו מבטיחה שהתוצאה הסופית תתיישר עם מגבלות העולם האמיתי והעדפות המשתמש המשתנות.

למשל דוגמת קוד

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. כמו בקוד הקודם והעבר את היסטוריית המשתמש והתוכנית הנוכחית

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
# .. תכנן מחדש ושלח את המשימות לסוכנים המתאימים
```

לתכנון מקיף יותר עיינו ב‑Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">פוסט בבלוג</a> לפתרון משימות מורכבות.

## סיכום

במאמר זה הסתכלנו על דוגמה לאופן שבו ניתן ליצור מתכנן שיכול לבחור בצורה דינמית את הסוכנים הזמינים שהוגדרו. הפלט של המתכנן מפרק את המשימות ומקצה את הסוכנים כך שניתן לבצע אותן. מניחים שלסוכנים יש גישה לפונקציות/כלים הנדרשים לביצוע המשימה. בנוסף לסוכנים, ניתן לכלול דפוסים אחרים כמו רפלקציה, מסכם וצ'אט ברוטציה כדי להתאים אישית עוד יותר.

## משאבים נוספים

Magentic One - מערכת רב-סוכנית כללית לפתרון משימות מורכבות שהשיגה תוצאות מרשימות על מספר מבחני סוכן אתגריים. הפניה: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. ביישום זה המנחה יוצר תכניות ספציפיות למשימות ומפנה משימות אלו לסוכנים הזמינים. בנוסף לתכנון, המנחה גם מפעיל מנגנון מעקב לניטור התקדמות המשימה ומתכנן מחדש לפי הצורך.

### שאלות נוספות לגבי תבנית התכנון?

הצטרפו ל-[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) כדי להיפגש עם לומדים נוספים, להשתתף בשעות קבלה ולקבל תשובות לשאלות על סוכני ה-AI שלכם.

## שיעור קודם

[בניית סוכני בינה מלאכותית אמינים](../06-building-trustworthy-agents/README.md)

## השיעור הבא

[תבנית עיצוב רב-סוכנית](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
הצהרת אחריות:
מסמך זה תורגם בעזרת שירות תרגום מבוסס בינה מלאכותית Co-op Translator (https://github.com/Azure/co-op-translator). אף שאנו שואפים לדיוק, יש לשים לב שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפתו כמקור הסמכות. למידע קריטי מומלץ לתרגום מקצועי שבוצע על ידי מתרגם אנושי. איננו אחראים לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->