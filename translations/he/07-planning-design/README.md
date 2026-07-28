[![תבנית תכנון עיצוב](../../../translated_images/he/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(לחץ על התמונה למעלה כדי לצפות בסרטון של השיעור)_

# תכנון עיצוב

## הקדמה

שיעור זה יעסוק ב

* הגדרת מטרה ברורה כוללת ופירוק משימה מורכבת למשימות ניתנות לניהול.
* שימוש ביציאה מובנית לתגובות אמינות וקריאות למכונה.
* יישום גישה מונחית אירועים לטיפול במשימות דינמיות וקלטים בלתי צפויים.

## מטרות הלמידה

לאחר השלמת שיעור זה, יהיו לך הבנות לגבי:

* זיהוי והגדרת מטרה כוללת לסוכן בינה מלאכותית, תוך הבטחת ידיעתו הברורה מה יש להשיג.
* פירוק משימה מורכבת למשימות משנה ניתנות לניהול וארגון שלהן ברצף לוגי.
* הציידה של סוכנים בכלים הנכונים (לדוגמה, כלי חיפוש או כלי ניתוח נתונים), קבלת החלטות מתי וכיצד להשתמש בהם, וטיפול במצבים בלתי צפויים העולים.
* הערכת תוצאות משימות המשנה, מדידת ביצועים, וחזרה על פעולות לשיפור התוצאה הסופית.

## הגדרת מטרה כוללת ופירוק משימה

![הגדרת מטרות ומשימות](../../../translated_images/he/defining-goals-tasks.d70439e19e37c47a.webp)

רוב המשימות במציאות מורכבות מדי לטיפול בצעד אחד בלבד. סוכן בינה מלאכותית זקוק למטרה מתומצתת כדי להנחות את התכנון והפעולות שלו. לדוגמה, שקול את המטרה:

    "יצירת תוכנית טיול ל-3 ימים."

למרות שמדובר בהצהרה פשוטה, היא עדיין דורשת עיבוד נוסף. ככל שהמטרה תהיה ברורה יותר, הסוכן (וכל משתף פעולה אנושי) יוכל להתמקד טוב יותר בהשגת התוצאה הנכונה, כמו יצירת תוכנית טיול מקיפה עם אפשרויות טיסה, המלצות על מלונות והצעות לפעילויות.

### פירוק משימה

משימות גדולות או מורכבות נעשות ניתנות לניהול יותר כאשר מחלקים אותן למשימות משנה קטנות וממוקדות מטרה.
בדוגמה של תוכנית הטיול, אפשר לפרק את המטרה ל:

* הזמנת טיסה
* הזמנת מלון
* השכרת רכב
* התאמה אישית

כל משימת משנה כזו יכולה להתבצע על ידי סוכנים או תהליכים ייעודיים. סוכן אחד יכול להתמחות בחיפוש העסקאות הטובות ביותר בטיסות, אחר יתמקד בהזמנת מלונות, וכן הלאה. סוכן מתאם או "להלן" יכול להרכיב את התוצאות הללו לתוכנית מסודרת למשתמש הסופי.

גישה מודולרית זו מאפשרת גם שיפורים הדרגתיים. לדוגמה, אפשר להוסיף סוכנים ייחודיים להמלצות אוכל או הצעות לפעילויות מקומיות ולשפר את התוכנית עם הזמן.

### פלט מובנה

מודלים לשוניים גדולים (LLMs) יכולים ליצור פלט מובנה (למשל JSON) שקל יותר עבור סוכנים או שירותים בהמשך לנתח ולמעבד. זה שימושי במיוחד בהקשר מרובה סוכנים, בו ניתן לבצעה את המשימות לאחר קבלת הפלט מתהליך התכנון.

קטע הקוד בפייתון הבא מדגים סוכן תכנון פשוט מפצל מטרה למשימות משנה ומייצר תוכנית מובנית:

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

# מודל משימת משנה לטיול
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # אנו רוצים להקצות את המשימה לסוכן

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

### סוכן תכנון עם אורקסטרציה מרובת סוכנים

בדוגמה זו, סוכן ניתוב סמנטי מקבל בקשת משתמש (למשל, "אני צריך תוכנית למלון בטיול שלי.").

התכנן ואז:

* מקבל את תוכנית המלון: התכנן לוקח את הודעת המשתמש, ובהתבסס על פקודת מערכת (כולל פרטים על סוכנים זמינים), מייצר תוכנית טיול מובנית.
* מפרט סוכנים וכלים שלהם: רישום הסוכנים מכיל רשימה של סוכנים (למשל לטיסות, מלונות, השכרת רכב ופעילויות) יחד עם הפונקציות או הכלים שהם מציעים.
* מנתב את התוכנית לסוכנים המתאימים: בהתאם למספר משימות המשנה, התכנן שולח את ההודעה ישירות לסוכן ייעודי (בסיטואציות של משימה אחת) או מתאם באמצעות מנהל צ'אט קבוצתי לשיתוף פעולה רב-סוכני.
* מסכם את התוצאה: לבסוף, התכנן מסכם את התוכנית שנוצרה לשם בהירות.
דוגמת קוד בפייתון הבאה ממחישה צעדים אלה:

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

# דגם משימה משנית לנסיעה

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

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# צור את הלקוח

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

מה שמגיע לאחר מכן הוא הפלט מהקוד הקודם ואתה יכול להשתמש בפלט המובנה הזה כדי לנווט אל `assigned_agent` ולסכם את תוכנית הטיול למשתמש.

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

מחברת לדוגמה עם קוד הקודם זמינה [כאן](./code_samples/07-python-agent-framework.ipynb).

### תכנון איטרטיבי

חלק מהמשימות דורשות תהליך חזרה או תכנון מחדש, שבו תוצאת משימת משנה אחת משפיעה על הבאה. לדוגמה, אם הסוכן מגלה פורמט נתונים בלתי צפוי בעת הזמנת טיסות, הוא עשוי להזדקק להתאים את האסטרטגיה לפני המשך להזמנת מלונות.

בנוסף, משוב משתמש (למשל, אדם שמחליט שהוא מעדיף טיסה מוקדמת יותר) יכול לגרום לתכנון חלקי מחדש. גישה דינמית ואיטרטיבית זו מבטיחה שהפתרון הסופי מתאים למגבלות מציאותיות ולהעדפות המשתמש שמשתנות.

לדוגמה, קוד

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. אותו דבר כמו הקוד הקודם והעבר את היסטוריית המשתמש, התוכנית הנוכחית

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
# .. לתכנן מחדש ולשלוח את המשימות לסוכנים המתאימים
```

לתכנון מקיף יותר יש לבדוק את Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">פוסט בבלוג</a> לפתרון משימות מורכבות.

## סיכום

במאמר זה הצגנו דוגמה לאופן בו ניתן ליצור מתכנן שבוחר באופן דינמי את הסוכנים הזמינים שהוגדרו. פלט המתכנן מפצל את המשימות ומקצה את הסוכנים כדי שניתן יהיה לבצע אותן. מניחים שלסוכנים יש גישה לפונקציות/כלים הדרושים לביצוע המשימה. בנוסף לסוכנים ניתן להוסיף דפוסים נוספים כמו רפלקציה, מסכם וצ'אט בסבב כדי להתאים את המערכת עוד יותר.

## משאבים נוספים

Magnetic One - מערכת רב-סוכנים כללית לפתרון משימות מורכבות שהשיגה תוצאות מרשימות במספר מבחני ביצוע אתגריים של סוכנים. מקור: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. במימוש זה, האורקסטרטור יוצר תוכניות משימה ספציפיות ומעביר את המשימות לסוכנים הזמינים. בנוסף לתכנון, האורקסטרטור משתמש במנגנון מעקב כדי לפקח על התקדמות המשימה ומבצע תכנון מחדש לפי הצורך.

### יש לך שאלות נוספות לגבי תבנית עיצוב התכנון?

הצטרף ל[Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) כדי להיפגש עם לומדים אחרים, להשתתף בשעות משרד ולקבל מענה על שאלותיך בנוגע לסוכני AI.

## שיעור קודם

[בניית סוכני בינה מלאכותית אמינים](../06-building-trustworthy-agents/README.md)

## שיעור הבא

[תבנית עיצוב רב-סוכנית](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:
מסמך זה תורגם באמצעות שירות תרגום אוטומטי [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להחשיב את המסמך המקורי בשפתו הטבעית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אדם. אנו לא אחראים לכל אי-הבנה או פירוש שגוי הנובע מהשימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->