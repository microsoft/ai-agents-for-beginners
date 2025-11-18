<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T13:08:01+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "he"
}
-->
[![חקר מסגרות סוכנים של AI](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.he.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(לחצו על התמונה למעלה לצפייה בסרטון של השיעור הזה)_

# חקר מסגרות סוכנים של AI

מסגרות סוכנים של AI הן פלטפורמות תוכנה שנועדו לפשט את יצירתם, פריסתם וניהולם של סוכני AI. מסגרות אלו מספקות למפתחים רכיבים מוכנים מראש, הפשטות וכלים שמייעלים את פיתוחם של מערכות AI מורכבות.

מסגרות אלו עוזרות למפתחים להתמקד בהיבטים הייחודיים של היישומים שלהם על ידי מתן גישות סטנדרטיות לאתגרים נפוצים בפיתוח סוכני AI. הן משפרות את יכולת ההרחבה, הנגישות והיעילות בבניית מערכות AI.

## מבוא

השיעור הזה יעסוק ב:

- מהן מסגרות סוכנים של AI ומה הן מאפשרות למפתחים להשיג?
- כיצד צוותים יכולים להשתמש בהן כדי ליצור אב-טיפוס במהירות, לשפר ולשדרג את יכולות הסוכן שלהם?
- מה ההבדלים בין המסגרות והכלים שנוצרו על ידי Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, ו-<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- האם ניתן לשלב את הכלים הקיימים באקוסיסטם של Azure ישירות, או שיש צורך בפתרונות עצמאיים?
- מהו שירות Azure AI Agents וכיצד הוא עוזר לי?

## מטרות למידה

מטרות השיעור הן לעזור לכם להבין:

- את תפקידן של מסגרות סוכנים של AI בפיתוח AI.
- כיצד לנצל מסגרות סוכנים של AI לבניית סוכנים חכמים.
- יכולות מרכזיות שמאפשרות מסגרות סוכנים של AI.
- ההבדלים בין AutoGen, Semantic Kernel ו-Azure AI Agent Service.

## מהן מסגרות סוכנים של AI ומה הן מאפשרות למפתחים לעשות?

מסגרות AI מסורתיות יכולות לעזור לכם לשלב AI באפליקציות שלכם ולשפר אותן בדרכים הבאות:

- **התאמה אישית**: AI יכול לנתח התנהגות והעדפות משתמשים כדי לספק המלצות, תוכן וחוויות מותאמות אישית.  
דוגמה: שירותי סטרימינג כמו Netflix משתמשים ב-AI כדי להציע סרטים ותוכניות על בסיס היסטוריית הצפייה, מה שמשפר את מעורבות המשתמשים ושביעות רצונם.  
- **אוטומציה ויעילות**: AI יכול לאוטומט משימות חוזרות, לייעל תהליכי עבודה ולשפר את היעילות התפעולית.  
דוגמה: אפליקציות שירות לקוחות משתמשות בצ'אטבוטים מבוססי AI לטיפול בשאלות נפוצות, מה שמפחית את זמני התגובה ומשחרר סוכנים אנושיים לטיפול בבעיות מורכבות יותר.  
- **שיפור חוויית משתמש**: AI יכול לשפר את חוויית המשתמש הכוללת על ידי מתן תכונות חכמות כמו זיהוי קולי, עיבוד שפה טבעית וטקסט חזוי.  
דוגמה: עוזרים וירטואליים כמו Siri ו-Google Assistant משתמשים ב-AI כדי להבין ולהגיב לפקודות קוליות, מה שמקל על המשתמשים לתקשר עם המכשירים שלהם.

### זה נשמע נהדר, נכון? אז למה אנחנו צריכים את מסגרות הסוכנים של AI?

מסגרות סוכנים של AI מייצגות משהו מעבר למסגרות AI רגילות. הן נועדו לאפשר יצירת סוכנים חכמים שיכולים לתקשר עם משתמשים, סוכנים אחרים והסביבה כדי להשיג מטרות ספציפיות. סוכנים אלו יכולים להציג התנהגות אוטונומית, לקבל החלטות ולהתאים את עצמם לתנאים משתנים. בואו נבחן כמה יכולות מרכזיות שמאפשרות מסגרות סוכנים של AI:

- **שיתוף פעולה ותיאום בין סוכנים**: מאפשר יצירת סוכנים מרובים שיכולים לעבוד יחד, לתקשר ולתאם כדי לפתור משימות מורכבות.  
- **אוטומציה וניהול משימות**: מספק מנגנונים לאוטומציה של תהליכי עבודה מרובי שלבים, האצלת משימות וניהול משימות דינמי בין סוכנים.  
- **הבנה והתאמה בהקשר**: מצייד סוכנים ביכולת להבין הקשר, להתאים את עצמם לסביבות משתנות ולקבל החלטות על בסיס מידע בזמן אמת.

לסיכום, סוכנים מאפשרים לכם לעשות יותר, לקחת את האוטומציה לשלב הבא, ליצור מערכות חכמות יותר שיכולות להתאים וללמוד מהסביבה שלהן.

## כיצד ליצור אב-טיפוס במהירות, לשפר ולשדרג את יכולות הסוכן?

זהו תחום שמתפתח במהירות, אך ישנם דברים משותפים לרוב מסגרות הסוכנים של AI שיכולים לעזור לכם ליצור אב-טיפוס ולשדרג במהירות, כמו רכיבים מודולריים, כלים שיתופיים ולמידה בזמן אמת. בואו נצלול לתוך אלו:

- **שימוש ברכיבים מודולריים**: ערכות SDK של AI מציעות רכיבים מוכנים מראש כמו מחברים ל-AI ולזיכרון, קריאה לפונקציות באמצעות שפה טבעית או תוספי קוד, תבניות הנחיה ועוד.  
- **ניצול כלים שיתופיים**: עיצוב סוכנים עם תפקידים ומשימות ספציפיים, המאפשרים להם לבדוק ולשפר תהליכי עבודה שיתופיים.  
- **למידה בזמן אמת**: יישום לולאות משוב שבהן סוכנים לומדים מאינטראקציות ומעדכנים את התנהגותם באופן דינמי.

### שימוש ברכיבים מודולריים

ערכות SDK כמו Microsoft Semantic Kernel ו-LangChain מציעות רכיבים מוכנים מראש כמו מחברי AI, תבניות הנחיה וניהול זיכרון.

**כיצד צוותים יכולים להשתמש בזה**: צוותים יכולים להרכיב במהירות את הרכיבים הללו כדי ליצור אב-טיפוס פונקציונלי מבלי להתחיל מאפס, מה שמאפשר ניסויים ושדרוגים מהירים.

**כיצד זה עובד בפועל**: ניתן להשתמש במנתח מוכן מראש כדי לחלץ מידע מקלט משתמש, מודול זיכרון לאחסון ושליפת נתונים, וגenerator הנחיות כדי לתקשר עם משתמשים, הכל מבלי לבנות את הרכיבים הללו מאפס.

**דוגמת קוד**. בואו נבחן דוגמאות כיצד ניתן להשתמש במחבר AI מוכן מראש עם Semantic Kernel Python ו-.Net שמשתמש בקריאה אוטומטית לפונקציות כדי שהמודל יגיב לקלט משתמש:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```
  
מה שאתם רואים בדוגמה הזו הוא כיצד ניתן לנצל מנתח מוכן מראש כדי לחלץ מידע מרכזי מקלט משתמש, כמו מקור, יעד ותאריך של בקשת הזמנת טיסה. הגישה המודולרית הזו מאפשרת לכם להתמקד בלוגיקה ברמה גבוהה.

### ניצול כלים שיתופיים

מסגרות כמו CrewAI, Microsoft AutoGen ו-Semantic Kernel מאפשרות יצירת סוכנים מרובים שיכולים לעבוד יחד.

**כיצד צוותים יכולים להשתמש בזה**: צוותים יכולים לעצב סוכנים עם תפקידים ומשימות ספציפיים, המאפשרים להם לבדוק ולשפר תהליכי עבודה שיתופיים ולשפר את יעילות המערכת הכוללת.

**כיצד זה עובד בפועל**: ניתן ליצור צוות של סוכנים כאשר לכל סוכן יש פונקציה מיוחדת, כמו שליפת נתונים, ניתוח או קבלת החלטות. סוכנים אלו יכולים לתקשר ולשתף מידע כדי להשיג מטרה משותפת, כמו מענה לשאלת משתמש או השלמת משימה.

**דוגמת קוד (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```
  
מה שאתם רואים בקוד הקודם הוא כיצד ניתן ליצור משימה שכוללת סוכנים מרובים שעובדים יחד לניתוח נתונים. כל סוכן מבצע פונקציה ספציפית, והמשימה מתבצעת על ידי תיאום הסוכנים כדי להשיג את התוצאה הרצויה. על ידי יצירת סוכנים ייעודיים עם תפקידים מיוחדים, ניתן לשפר את יעילות המשימה וביצועיה.

### למידה בזמן אמת

מסגרות מתקדמות מספקות יכולות להבנה והתאמה בהקשר בזמן אמת.

**כיצד צוותים יכולים להשתמש בזה**: צוותים יכולים ליישם לולאות משוב שבהן סוכנים לומדים מאינטראקציות ומעדכנים את התנהגותם באופן דינמי, מה שמוביל לשיפור מתמשך ושדרוג יכולות.

**כיצד זה עובד בפועל**: סוכנים יכולים לנתח משוב משתמשים, נתוני סביבה ותוצאות משימות כדי לעדכן את בסיס הידע שלהם, להתאים אלגוריתמים לקבלת החלטות ולשפר ביצועים לאורך זמן. תהליך הלמידה האיטרטיבי הזה מאפשר לסוכנים להתאים את עצמם לתנאים משתנים ולהעדפות משתמשים, ומשפר את יעילות המערכת הכוללת.

## מה ההבדלים בין המסגרות AutoGen, Semantic Kernel ו-Azure AI Agent Service?

ישנן דרכים רבות להשוות בין המסגרות הללו, אך בואו נבחן כמה הבדלים מרכזיים מבחינת העיצוב, היכולות ומקרי השימוש המיועדים:

## AutoGen

AutoGen היא מסגרת קוד פתוח שפותחה על ידי מעבדת AI Frontiers של Microsoft Research. היא מתמקדת ביישומים מבוססי אירועים, מבוזרים ו*סוכניים*, ומאפשרת שימוש ב-LLMs ו-SLMs מרובים, כלים ותבניות עיצוב מתקדמות של סוכנים מרובים.

AutoGen בנויה סביב הרעיון המרכזי של סוכנים, שהם ישויות אוטונומיות שיכולות לתפוס את סביבתן, לקבל החלטות ולנקוט פעולות כדי להשיג מטרות ספציפיות. סוכנים מתקשרים באמצעות הודעות אסינכרוניות, מה שמאפשר להם לעבוד באופן עצמאי ובמקביל, ומשפר את יכולת ההרחבה והתגובה של המערכת.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">סוכנים מבוססים על מודל השחקן</a>. לפי ויקיפדיה, שחקן הוא _הבלוק הבסיסי של חישוב מקבילי. בתגובה להודעה שהוא מקבל, שחקן יכול: לקבל החלטות מקומיות, ליצור שחקנים נוספים, לשלוח הודעות נוספות ולהחליט כיצד להגיב להודעה הבאה שהוא מקבל_.

**מקרי שימוש**: אוטומציה של יצירת קוד, משימות ניתוח נתונים ובניית סוכנים מותאמים אישית לפונקציות תכנון ומחקר.

הנה כמה מושגים מרכזיים של AutoGen:

- **סוכנים**. סוכן הוא ישות תוכנה ש:
  - **מתקשר באמצעות הודעות**, הודעות אלו יכולות להיות סינכרוניות או אסינכרוניות.  
  - **שומר על מצב משלו**, שניתן לשנות על ידי הודעות נכנסות.  
  - **מבצע פעולות** בתגובה להודעות שהתקבלו או שינויים במצבו. פעולות אלו עשויות לשנות את מצב הסוכן וליצור אפקטים חיצוניים, כמו עדכון יומני הודעות, שליחת הודעות חדשות, ביצוע קוד או ביצוע קריאות API.  

  הנה קטע קוד קצר שבו אתם יוצרים סוכן משלכם עם יכולות צ'אט:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
  
    בקוד הקודם, `MyAgent` נוצר ויורש מ-`RoutedAgent`. יש לו מטפל הודעות שמדפיס את תוכן ההודעה ואז שולח תגובה באמצעות הנציג `AssistantAgent`. שימו לב במיוחד כיצד אנו מקצים ל-`self._delegate` מופע של `AssistantAgent`, שהוא סוכן מוכן מראש שיכול לטפל בהשלמות צ'אט.

    בואו ניידע את AutoGen על סוג הסוכן הזה ונפעיל את התוכנית:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```
  
    בקוד הקודם הסוכנים נרשמים עם זמן הריצה ואז הודעה נשלחת לסוכן, מה שמוביל לפלט הבא:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```
  
- **סוכנים מרובים**. AutoGen תומכת ביצירת סוכנים מרובים שיכולים לעבוד יחד כדי להשיג משימות מורכבות. סוכנים יכולים לתקשר, לשתף מידע ולתאם את פעולותיהם כדי לפתור בעיות בצורה יעילה יותר. כדי ליצור מערכת סוכנים מרובה, ניתן להגדיר סוגים שונים של סוכנים עם פונקציות ותפקידים מיוחדים, כמו שליפת נתונים, ניתוח, קבלת החלטות ואינטראקציה עם משתמשים. בואו נראה כיצד יצירה כזו נראית כדי לקבל תחושה של זה:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```
  
    בקוד הקודם יש לנו `GroupChatManager` שנרשם עם זמן הריצה. מנהל זה אחראי על תיאום האינטראקציות בין סוגים שונים של סוכנים, כמו כותבים, מאיירים, עורכים ומשתמשים.

- **זמן ריצה של סוכן**. המסגרת מספקת סביבת זמן ריצה, המאפשרת תקשורת בין סוכנים, מנהלת את זהויותיהם ומחזורי החיים שלהם, ומבטיחה גבולות אבטחה ופרטיות. המשמעות היא שניתן להפעיל את הסוכנים שלכם בסביבה בטוחה ומבוקרת, מה שמבטיח שהם יוכלו לתקשר בצורה בטוחה ויעילה. ישנם שני זמני ריצה מעניינים:
  - **זמן ריצה עצמאי**. זו בחירה טובה ליישומים בתהליך יחיד שבהם כל הסוכנים מיושמים באותה שפת תכנות ופועלים באותו תהליך. הנה איור של איך זה עובד:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">זמן ריצה עצמאי</a>  
    *סוכנים מתקשרים באמצעות הודעות דרך זמן הריצה, וזמן הריצה מנהל את מחזור החיים של הסוכנים*

  - **זמן ריצה מבוזר**, מתאים ליישומים מרובי תהליכים שבהם סוכנים עשויים להיות מיושמים בשפות תכנות שונות ופועלים על מכונות שונות. הנה איור של איך זה עובד:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">זמן ריצה מבוזר</a>

## Semantic Kernel + מסגרת סוכנים

Semantic Kernel הוא SDK לתזמור AI מוכן לארגונים. הוא כולל מחברי AI וזיכרון, יחד עם מסגרת סוכנים.

בואו נתחיל עם כמה רכיבים מרכזיים:

- **מחברי AI**: זהו ממשק עם שירותי AI חיצוניים ומקורות נתונים לשימוש הן ב-Python והן ב-C#.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  
  
    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```
  
    כאן יש לכם דוגמה פשוטה כיצד ניתן ליצור Kernel ולהוסיף שירות השלמת צ'אט. Semantic Kernel יוצר חיבור לשירות AI חיצוני, במקרה זה, Azure OpenAI Chat Completion.

- **תוספים**: אלו כוללים פונקציות שהאפליקציה יכולה להשתמש בהן. ישנם תוספים מוכנים מראש וגם תוספים מותאמים אישית שניתן ליצור. מושג קשור הוא "פונקציות הנחיה". במקום לספק רמזים בשפה טבעית להפעלת פונקציות, אתם משדרים פונקציות מסוימות למודל. בהתבסס על הקשר הצ'אט הנוכחי, המודל עשוי לבחור לקרוא לאחת מהפונקציות הללו כדי להשלים בקשה או שאילתה. הנה דוגמה:

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```
  
    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```
  
    כאן, תחילה יש לכם תבנית הנחיה `skPrompt` שמשאירה מקום למשתמש להכניס טקסט, `$userInput`. לאחר מכן אתם יוצרים את פונקציית ה-Kernel `SummarizeText` ואז מייבאים אותה ל-Kernel עם שם התוסף `SemanticFunctions`. שימו לב לשם הפונקציה שעוזר ל-Semantic Kernel להבין מה הפונקציה עושה ומתי יש לקרוא לה.

- **פונקציה מקורית**: יש גם פונקציות מקוריות שהמסגרת יכולה לקרוא להן ישירות כדי לבצע את המשימה. הנה דוגמה לפונקציה כזו שמחזירה את התוכן מקובץ:

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```
  
- **זיכרון**: מפשט ומפשט את ניהול ההקשר עבור אפליקציות AI. הרעיון עם זיכרון הוא שזה משהו שה-LLM צריך לדעת עליו. ניתן לאחסן מידע זה בחנות וקטורית שמסתיימת להיות מסד נתונים בזיכרון או מסד נתונים וקטורי או דומה. הנה דוגמה לתרחיש מאוד פשוט שבו *עובדות* מתווספות לזיכרון:

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```
  
העובדות הללו נשמרות לאחר מכן באוסף הזיכרון `SummarizedAzureDocs`. זהו דוגמה מאוד פשוטה, אך ניתן לראות כיצד ניתן לשמור מידע בזיכרון לשימוש של ה-LLM.

אז אלו הם היסודות של מסגרת Semantic Kernel, מה לגבי מסגרת הסוכנים?

## שירות הסוכנים של Azure AI

שירות הסוכנים של Azure AI הוא תוספת חדשה יחסית, שהוצגה בכנס Microsoft Ignite 2024. הוא מאפשר פיתוח ופריסה של סוכני AI עם מודלים גמישים יותר, כמו קריאה ישירה ל-LLMs בקוד פתוח כמו Llama 3, Mistral ו-Cohere.

שירות הסוכנים של Azure AI מספק מנגנוני אבטחה חזקים ושיטות אחסון נתונים, מה שהופך אותו למתאים ליישומים ארגוניים.

השירות עובד באופן מובנה עם מסגרות תזמור רב-סוכנים כמו AutoGen ו-Semantic Kernel.

השירות נמצא כרגע בתצוגה ציבורית ותומך ב-Python וב-C# לבניית סוכנים.

באמצעות Semantic Kernel Python, ניתן ליצור סוכן Azure AI עם תוסף שהוגדר על ידי המשתמש:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### מושגים מרכזיים

שירות הסוכנים של Azure AI כולל את המושגים המרכזיים הבאים:

- **סוכן**. שירות הסוכנים של Azure AI משתלב עם Azure AI Foundry. בתוך AI Foundry, סוכן AI פועל כ"מיקרו-שירות חכם" שניתן להשתמש בו למענה על שאלות (RAG), ביצוע פעולות, או אוטומציה מלאה של תהליכי עבודה. הוא משיג זאת על ידי שילוב הכוח של מודלים גנרטיביים עם כלים שמאפשרים לו לגשת ולהתממשק עם מקורות נתונים בעולם האמיתי. הנה דוגמה לסוכן:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    בדוגמה זו, נוצר סוכן עם המודל `gpt-4o-mini`, שם `my-agent`, והוראות `You are helpful agent`. הסוכן מצויד בכלים ומשאבים לביצוע משימות פרשנות קוד.

- **שרשור והודעות**. השרשור הוא מושג חשוב נוסף. הוא מייצג שיחה או אינטראקציה בין סוכן למשתמש. ניתן להשתמש בשרשורים כדי לעקוב אחר התקדמות השיחה, לשמור מידע הקשרי, ולנהל את מצב האינטראקציה. הנה דוגמה לשרשור:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    בקוד הקודם, נוצר שרשור. לאחר מכן, נשלחת הודעה לשרשור. על ידי קריאה ל-`create_and_process_run`, הסוכן מתבקש לבצע עבודה על השרשור. לבסוף, ההודעות נשלפות ונרשמות כדי לראות את תגובת הסוכן. ההודעות מציינות את התקדמות השיחה בין המשתמש לסוכן. חשוב גם להבין שההודעות יכולות להיות מסוגים שונים כמו טקסט, תמונה או קובץ, כלומר עבודת הסוכן הניבה למשל תמונה או תגובת טקסט. כמפתח, ניתן להשתמש במידע זה כדי לעבד את התגובה או להציג אותה למשתמש.

- **אינטגרציה עם מסגרות AI אחרות**. שירות הסוכנים של Azure AI יכול להתממשק עם מסגרות אחרות כמו AutoGen ו-Semantic Kernel, מה שאומר שניתן לבנות חלק מהאפליקציה באחת מהמסגרות הללו ולמשל להשתמש בשירות הסוכנים כמנהל תזמור, או לבנות הכל בשירות הסוכנים.

**שימושים**: שירות הסוכנים של Azure AI מיועד ליישומים ארגוניים שדורשים פריסה של סוכני AI מאובטחים, ניתנים להרחבה וגמישים.

## מה ההבדל בין המסגרות הללו?

נראה שיש הרבה חפיפה בין המסגרות הללו, אך ישנם כמה הבדלים מרכזיים מבחינת העיצוב, היכולות, והשימושים המיועדים:

- **AutoGen**: מסגרת ניסיונית המתמקדת במחקר מתקדם על מערכות רב-סוכנים. זהו המקום הטוב ביותר להתנסות וליצור אב-טיפוס של מערכות רב-סוכנים מתוחכמות.
- **Semantic Kernel**: ספריית סוכנים מוכנה לייצור לבניית יישומים ארגוניים מבוססי סוכנים. מתמקדת ביישומים מבוססי אירועים, מבוזרים, ומאפשרת עיצוב דפוסי סוכנים יחידים ורב-סוכנים.
- **שירות הסוכנים של Azure AI**: פלטפורמה ושירות פריסה ב-Azure Foundry לסוכנים. מציעה בניית קישוריות לשירותים הנתמכים על ידי Azure כמו Azure OpenAI, Azure AI Search, Bing Search וביצוע קוד.

עדיין לא בטוחים מה לבחור?

### שימושים

בואו נראה אם נוכל לעזור לכם על ידי מעבר על כמה שימושים נפוצים:

> ש: אני מתנסה, לומד ובונה יישומי סוכנים כהוכחת יכולת, ואני רוצה להיות מסוגל לבנות ולהתנסות במהירות
>

>ת: AutoGen תהיה בחירה טובה לתרחיש זה, מכיוון שהיא מתמקדת ביישומים מבוססי אירועים, מבוזרים, ותומכת בדפוסי עיצוב רב-סוכנים מתקדמים.

> ש: מה הופך את AutoGen לבחירה טובה יותר מ-Semantic Kernel ושירות הסוכנים של Azure AI לשימוש זה?
>
> ת: AutoGen תוכננה במיוחד ליישומים מבוססי אירועים, מבוזרים, מה שהופך אותה למתאימה היטב לאוטומציה של משימות יצירת קוד וניתוח נתונים. היא מספקת את הכלים והיכולות הנדרשים לבניית מערכות רב-סוכנים מורכבות ביעילות.

>ש: נשמע שגם שירות הסוכנים של Azure AI יכול לעבוד כאן, יש לו כלים ליצירת קוד ועוד?

>
> ת: כן, שירות הסוכנים של Azure AI הוא שירות פלטפורמה לסוכנים ומוסיף יכולות מובנות למודלים מרובים, Azure AI Search, Bing Search ו-Azure Functions. הוא מקל על בניית הסוכנים בפורטל Foundry ופריסתם בקנה מידה רחב.

> ש: אני עדיין מבולבל, פשוט תנו לי אפשרות אחת
>
> ת: בחירה מצוינת היא לבנות את האפליקציה שלכם תחילה ב-Semantic Kernel ואז להשתמש בשירות הסוכנים של Azure AI כדי לפרוס את הסוכן שלכם. גישה זו מאפשרת לכם לשמר בקלות את הסוכנים שלכם תוך ניצול הכוח לבנות מערכות רב-סוכנים ב-Semantic Kernel. בנוסף, ל-Semantic Kernel יש מחבר ב-AutoGen, מה שמקל על השימוש בשתי המסגרות יחד.

בואו נסכם את ההבדלים המרכזיים בטבלה:

| מסגרת | מיקוד | מושגים מרכזיים | שימושים |
| --- | --- | --- | --- |
| AutoGen | יישומים מבוססי אירועים, מבוזרים | סוכנים, פרסונות, פונקציות, נתונים | יצירת קוד, משימות ניתוח נתונים |
| Semantic Kernel | הבנה ויצירת תוכן דמוי אנושי | סוכנים, רכיבים מודולריים, שיתוף פעולה | הבנת שפה טבעית, יצירת תוכן |
| שירות הסוכנים של Azure AI | מודלים גמישים, אבטחה ארגונית, יצירת קוד, קריאת כלים | מודולריות, שיתוף פעולה, תזמור תהליכים | פריסה של סוכני AI מאובטחים, ניתנים להרחבה וגמישים |

מהו השימוש האידיאלי לכל אחת מהמסגרות הללו?

## האם אני יכול לשלב את הכלים הקיימים שלי באקוסיסטם של Azure ישירות, או שאני צריך פתרונות עצמאיים?

התשובה היא כן, ניתן לשלב את הכלים הקיימים שלכם באקוסיסטם של Azure ישירות עם שירות הסוכנים של Azure AI במיוחד, מכיוון שהוא נבנה לעבוד בצורה חלקה עם שירותי Azure אחרים. לדוגמה, ניתן לשלב Bing, Azure AI Search ו-Azure Functions. יש גם אינטגרציה עמוקה עם Azure AI Foundry.

עבור AutoGen ו-Semantic Kernel, ניתן גם לשלב עם שירותי Azure, אך ייתכן שתצטרכו לקרוא לשירותי Azure מתוך הקוד שלכם. דרך נוספת לשלב היא להשתמש ב-SDKs של Azure כדי להתממשק עם שירותי Azure מתוך הסוכנים שלכם. בנוסף, כמו שהוזכר, ניתן להשתמש בשירות הסוכנים של Azure AI כמנהל תזמור עבור הסוכנים שנבנו ב-AutoGen או Semantic Kernel, מה שיאפשר גישה קלה לאקוסיסטם של Azure.

## דוגמאות קוד

- Python: [מסגרת סוכנים](./code_samples/02-python-agent-framework.ipynb)
- .NET: [מסגרת סוכנים](./code_samples/02-dotnet-agent-framework.md)

## יש לכם עוד שאלות על מסגרות סוכני AI?

הצטרפו ל-[Discord של Azure AI Foundry](https://aka.ms/ai-agents/discord) כדי לפגוש לומדים אחרים, להשתתף בשעות משרד ולקבל תשובות לשאלות שלכם על סוכני AI.

## מקורות

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">שירות הסוכנים של Azure</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel ו-AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">מסגרת סוכנים של Semantic Kernel Python</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">מסגרת סוכנים של Semantic Kernel .Net</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">שירות הסוכנים של Azure AI</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">שימוש בשירות הסוכנים של Azure AI עם AutoGen / Semantic Kernel לבניית פתרון רב-סוכנים</a>

## שיעור קודם

[מבוא לסוכני AI ושימושים](../01-intro-to-ai-agents/README.md)

## שיעור הבא

[הבנת דפוסי עיצוב סוכנים](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום AI [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור סמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי אנושי. איננו אחראים לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->