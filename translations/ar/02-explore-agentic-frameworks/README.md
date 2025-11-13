<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T11:02:05+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ar"
}
-->
[![استكشاف أطر عمل وكلاء الذكاء الاصطناعي](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.ar.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(اضغط على الصورة أعلاه لمشاهدة فيديو الدرس)_

# استكشاف أطر عمل وكلاء الذكاء الاصطناعي

أطر عمل وكلاء الذكاء الاصطناعي هي منصات برمجية مصممة لتبسيط إنشاء ونشر وإدارة وكلاء الذكاء الاصطناعي. توفر هذه الأطر للمطورين مكونات جاهزة، تجريدات، وأدوات تسهل تطوير أنظمة الذكاء الاصطناعي المعقدة.

تساعد هذه الأطر المطورين على التركيز على الجوانب الفريدة لتطبيقاتهم من خلال توفير نهج موحد للتحديات الشائعة في تطوير وكلاء الذكاء الاصطناعي. كما تعزز قابلية التوسع، سهولة الوصول، والكفاءة في بناء أنظمة الذكاء الاصطناعي.

## المقدمة

سيتناول هذا الدرس:

- ما هي أطر عمل وكلاء الذكاء الاصطناعي وما الذي تمكّن المطورين من تحقيقه؟
- كيف يمكن للفرق استخدام هذه الأطر لتصميم نماذج أولية بسرعة، التكرار، وتحسين قدرات الوكيل؟
- ما هي الفروقات بين الأطر والأدوات التي أنشأتها Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>، <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>، و<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>؟
- هل يمكنني دمج أدوات النظام البيئي الحالي لـ Azure مباشرةً، أم أحتاج إلى حلول مستقلة؟
- ما هو Azure AI Agents service وكيف يساعدني؟

## أهداف التعلم

أهداف هذا الدرس هي مساعدتك على فهم:

- دور أطر عمل وكلاء الذكاء الاصطناعي في تطوير الذكاء الاصطناعي.
- كيفية الاستفادة من أطر عمل وكلاء الذكاء الاصطناعي لبناء وكلاء ذكيين.
- القدرات الرئيسية التي توفرها أطر عمل وكلاء الذكاء الاصطناعي.
- الفروقات بين AutoGen، Semantic Kernel، وAzure AI Agent Service.

## ما هي أطر عمل وكلاء الذكاء الاصطناعي وما الذي تمكّن المطورين من القيام به؟

يمكن للأطر التقليدية للذكاء الاصطناعي مساعدتك في دمج الذكاء الاصطناعي في تطبيقاتك وتحسينها بالطرق التالية:

- **التخصيص**: يمكن للذكاء الاصطناعي تحليل سلوك المستخدم وتفضيلاته لتقديم توصيات، محتوى، وتجارب مخصصة.
مثال: تستخدم خدمات البث مثل Netflix الذكاء الاصطناعي لاقتراح الأفلام والعروض بناءً على سجل المشاهدة، مما يعزز تفاعل المستخدم ورضاه.
- **الأتمتة والكفاءة**: يمكن للذكاء الاصطناعي أتمتة المهام المتكررة، تبسيط سير العمل، وتحسين الكفاءة التشغيلية.
مثال: تستخدم تطبيقات خدمة العملاء روبوتات الدردشة المدعومة بالذكاء الاصطناعي للتعامل مع الاستفسارات الشائعة، مما يقلل من أوقات الاستجابة ويتيح للموظفين البشريين التعامل مع القضايا الأكثر تعقيدًا.
- **تحسين تجربة المستخدم**: يمكن للذكاء الاصطناعي تحسين تجربة المستخدم العامة من خلال توفير ميزات ذكية مثل التعرف على الصوت، معالجة اللغة الطبيعية، والنص التنبؤي.
مثال: تستخدم المساعدات الافتراضية مثل Siri وGoogle Assistant الذكاء الاصطناعي لفهم الأوامر الصوتية والرد عليها، مما يسهل على المستخدمين التفاعل مع أجهزتهم.

### يبدو هذا رائعًا، أليس كذلك؟ إذًا لماذا نحتاج إلى أطر عمل وكلاء الذكاء الاصطناعي؟

تمثل أطر عمل وكلاء الذكاء الاصطناعي شيئًا أكثر من مجرد أطر عمل للذكاء الاصطناعي. فهي مصممة لتمكين إنشاء وكلاء ذكيين يمكنهم التفاعل مع المستخدمين، وكلاء آخرين، والبيئة لتحقيق أهداف محددة. يمكن لهؤلاء الوكلاء إظهار سلوك مستقل، اتخاذ قرارات، والتكيف مع الظروف المتغيرة. دعونا نلقي نظرة على بعض القدرات الرئيسية التي توفرها أطر عمل وكلاء الذكاء الاصطناعي:

- **التعاون والتنسيق بين الوكلاء**: تمكين إنشاء وكلاء ذكاء اصطناعي متعددين يمكنهم العمل معًا، التواصل، والتنسيق لحل المهام المعقدة.
- **أتمتة وإدارة المهام**: توفير آليات لأتمتة سير العمل متعدد الخطوات، تفويض المهام، وإدارة المهام الديناميكية بين الوكلاء.
- **الفهم السياقي والتكيف**: تجهيز الوكلاء بالقدرة على فهم السياق، التكيف مع البيئات المتغيرة، واتخاذ قرارات بناءً على المعلومات في الوقت الفعلي.

باختصار، تسمح الوكلاء لك بالقيام بالمزيد، بأخذ الأتمتة إلى المستوى التالي، وإنشاء أنظمة أكثر ذكاءً يمكنها التكيف والتعلم من بيئتها.

## كيفية تصميم نماذج أولية بسرعة، التكرار، وتحسين قدرات الوكيل؟

هذا مجال سريع التغير، ولكن هناك بعض الأمور المشتركة عبر معظم أطر عمل وكلاء الذكاء الاصطناعي التي يمكن أن تساعدك في تصميم نماذج أولية والتكرار بسرعة، وهي المكونات المعيارية، الأدوات التعاونية، والتعلم في الوقت الفعلي. دعونا نتعمق في هذه النقاط:

- **استخدام المكونات المعيارية**: توفر SDKs مكونات جاهزة مثل موصلات الذكاء الاصطناعي والذاكرة، استدعاء الوظائف باستخدام اللغة الطبيعية أو الإضافات البرمجية، قوالب التعليمات، والمزيد.
- **الاستفادة من الأدوات التعاونية**: تصميم وكلاء بأدوار ومهام محددة، مما يمكنهم من اختبار وتحسين سير العمل التعاوني.
- **التعلم في الوقت الفعلي**: تنفيذ حلقات التغذية الراجعة حيث يتعلم الوكلاء من التفاعلات ويعدلون سلوكهم ديناميكيًا.

### استخدام المكونات المعيارية

تقدم SDKs مثل Microsoft Semantic Kernel وLangChain مكونات جاهزة مثل موصلات الذكاء الاصطناعي، قوالب التعليمات، وإدارة الذاكرة.

**كيف يمكن للفرق استخدام هذه المكونات**: يمكن للفرق تجميع هذه المكونات بسرعة لإنشاء نموذج أولي وظيفي دون البدء من الصفر، مما يسمح بالتجربة السريعة والتكرار.

**كيف يعمل ذلك عمليًا**: يمكنك استخدام محلل جاهز لاستخراج المعلومات من إدخال المستخدم، وحدة ذاكرة لتخزين واسترجاع البيانات، ومولد تعليمات للتفاعل مع المستخدمين، كل ذلك دون الحاجة إلى بناء هذه المكونات من الصفر.

**مثال على الكود**. دعونا نلقي نظرة على أمثلة حول كيفية استخدام موصل ذكاء اصطناعي جاهز مع Semantic Kernel Python و.Net الذي يستخدم استدعاء الوظائف التلقائي لجعل النموذج يستجيب لإدخال المستخدم:

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

ما يمكنك رؤيته من هذا المثال هو كيفية الاستفادة من محلل جاهز لاستخراج المعلومات الرئيسية من إدخال المستخدم، مثل الأصل، الوجهة، وتاريخ طلب حجز الرحلة. يتيح هذا النهج المعياري التركيز على المنطق عالي المستوى.

### الاستفادة من الأدوات التعاونية

تسهل أطر العمل مثل CrewAI، Microsoft AutoGen، وSemantic Kernel إنشاء وكلاء متعددين يمكنهم العمل معًا.

**كيف يمكن للفرق استخدام هذه الأدوات**: يمكن للفرق تصميم وكلاء بأدوار ومهام محددة، مما يمكنهم من اختبار وتحسين سير العمل التعاوني وتحسين كفاءة النظام بشكل عام.

**كيف يعمل ذلك عمليًا**: يمكنك إنشاء فريق من الوكلاء حيث يكون لكل وكيل وظيفة متخصصة، مثل استرجاع البيانات، التحليل، أو اتخاذ القرارات. يمكن لهؤلاء الوكلاء التواصل ومشاركة المعلومات لتحقيق هدف مشترك، مثل الإجابة على استفسار المستخدم أو إكمال مهمة.

**مثال على الكود (AutoGen)**:

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

ما تراه في الكود السابق هو كيفية إنشاء مهمة تتضمن وكلاء متعددين يعملون معًا لتحليل البيانات. يقوم كل وكيل بوظيفة محددة، ويتم تنفيذ المهمة من خلال تنسيق الوكلاء لتحقيق النتيجة المرجوة. من خلال إنشاء وكلاء مخصصين بأدوار متخصصة، يمكنك تحسين كفاءة المهمة وأدائها.

### التعلم في الوقت الفعلي

توفر الأطر المتقدمة قدرات لفهم السياق والتكيف في الوقت الفعلي.

**كيف يمكن للفرق استخدام هذه القدرات**: يمكن للفرق تنفيذ حلقات التغذية الراجعة حيث يتعلم الوكلاء من التفاعلات ويعدلون سلوكهم ديناميكيًا، مما يؤدي إلى تحسين مستمر وتطوير القدرات.

**كيف يعمل ذلك عمليًا**: يمكن للوكلاء تحليل ملاحظات المستخدم، بيانات البيئة، ونتائج المهام لتحديث قاعدة معرفتهم، تعديل خوارزميات اتخاذ القرار، وتحسين الأداء بمرور الوقت. يتيح هذا التعلم التكراري للوكلاء التكيف مع الظروف المتغيرة وتفضيلات المستخدم، مما يعزز فعالية النظام بشكل عام.

## ما هي الفروقات بين الأطر AutoGen، Semantic Kernel وAzure AI Agent Service؟

هناك العديد من الطرق لمقارنة هذه الأطر، ولكن دعونا نلقي نظرة على بعض الفروقات الرئيسية من حيث التصميم، القدرات، وحالات الاستخدام المستهدفة:

## AutoGen

AutoGen هو إطار عمل مفتوح المصدر تم تطويره بواسطة مختبر AI Frontiers التابع لـ Microsoft Research. يركز على التطبيقات الموزعة المدفوعة بالأحداث، مما يتيح تصميمات متعددة الوكلاء باستخدام LLMs وSLMs، الأدوات، وأنماط تصميم متقدمة.

AutoGen مبني حول مفهوم الوكلاء، وهم كيانات مستقلة يمكنها إدراك بيئتها، اتخاذ قرارات، واتخاذ إجراءات لتحقيق أهداف محددة. يتواصل الوكلاء من خلال رسائل غير متزامنة، مما يسمح لهم بالعمل بشكل مستقل وبالتوازي، مما يعزز قابلية التوسع واستجابة النظام.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">الوكلاء يعتمدون على نموذج الممثل</a>. وفقًا لويكيبيديا، الممثل هو _الوحدة الأساسية للحساب المتزامن. استجابةً للرسالة التي يتلقاها، يمكن للممثل: اتخاذ قرارات محلية، إنشاء المزيد من الممثلين، إرسال المزيد من الرسائل، وتحديد كيفية الرد على الرسالة التالية التي يتلقاها_.

**حالات الاستخدام**: أتمتة إنشاء الكود، مهام تحليل البيانات، وبناء وكلاء مخصصين لوظائف التخطيط والبحث.

إليك بعض المفاهيم الأساسية لـ AutoGen:

- **الوكلاء**. الوكيل هو كيان برمجي يقوم بـ:
  - **التواصل عبر الرسائل**، يمكن أن تكون هذه الرسائل متزامنة أو غير متزامنة.
  - **الحفاظ على حالته الخاصة**، التي يمكن تعديلها بواسطة الرسائل الواردة.
  - **تنفيذ الإجراءات** استجابةً للرسائل المستلمة أو التغييرات في حالته. قد تؤدي هذه الإجراءات إلى تعديل حالة الوكيل وإحداث تأثيرات خارجية، مثل تحديث سجلات الرسائل، إرسال رسائل جديدة، تنفيذ الكود، أو إجراء مكالمات API.
    
  هنا لديك مقتطف كود قصير لإنشاء وكيل خاص بك بقدرات الدردشة:

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
    
    في الكود السابق، تم إنشاء `MyAgent` ويورث من `RoutedAgent`. لديه معالج رسائل يطبع محتوى الرسالة ثم يرسل استجابة باستخدام المندوب `AssistantAgent`. لاحظ بشكل خاص كيف قمنا بتعيين `self._delegate` إلى مثيل من `AssistantAgent` وهو وكيل جاهز يمكنه التعامل مع إكمالات الدردشة.

    دعونا نخبر AutoGen عن نوع هذا الوكيل ونبدأ البرنامج:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    في الكود السابق، يتم تسجيل الوكلاء مع وقت التشغيل ثم يتم إرسال رسالة إلى الوكيل مما يؤدي إلى الإخراج التالي:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **الوكلاء المتعددون**. يدعم AutoGen إنشاء وكلاء متعددين يمكنهم العمل معًا لتحقيق المهام المعقدة. يمكن للوكلاء التواصل، مشاركة المعلومات، وتنسيق إجراءاتهم لحل المشكلات بكفاءة أكبر. لإنشاء نظام متعدد الوكلاء، يمكنك تعريف أنواع مختلفة من الوكلاء بوظائف وأدوار متخصصة، مثل استرجاع البيانات، التحليل، اتخاذ القرارات، والتفاعل مع المستخدم. دعونا نرى كيف يبدو مثل هذا الإنشاء لنحصل على فكرة عنه:

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

    في الكود السابق، لدينا `GroupChatManager` مسجل مع وقت التشغيل. هذا المدير مسؤول عن تنسيق التفاعلات بين أنواع مختلفة من الوكلاء، مثل الكتاب، الرسامين، المحررين، والمستخدمين.

- **وقت تشغيل الوكيل**. يوفر الإطار بيئة وقت تشغيل، تمكن التواصل بين الوكلاء، إدارة هوياتهم ودورات حياتهم، وفرض حدود الأمان والخصوصية. هذا يعني أنه يمكنك تشغيل وكلائك في بيئة آمنة ومضبوطة، مما يضمن أنهم يمكنهم التفاعل بأمان وكفاءة. هناك نوعان من وقت التشغيل ذو أهمية:
  - **وقت تشغيل مستقل**. هذا خيار جيد للتطبيقات ذات العملية الواحدة حيث يتم تنفيذ جميع الوكلاء بنفس لغة البرمجة ويعملون في نفس العملية. إليك توضيح لكيفية عمله:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">وقت تشغيل مستقل</a>   
    *الوكلاء يتواصلون عبر الرسائل من خلال وقت التشغيل، ووقت التشغيل يدير دورة حياة الوكلاء*

  - **وقت تشغيل الوكلاء الموزع**، مناسب للتطبيقات متعددة العمليات حيث يمكن تنفيذ الوكلاء بلغات برمجة مختلفة ويعملون على أجهزة مختلفة. إليك توضيح لكيفية عمله:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">وقت تشغيل موزع</a>

## Semantic Kernel + إطار عمل الوكلاء

Semantic Kernel هو SDK جاهز للمؤسسات لتنظيم الذكاء الاصطناعي. يتكون من موصلات الذكاء الاصطناعي والذاكرة، إلى جانب إطار عمل الوكلاء.

دعونا نغطي بعض المكونات الأساسية:

- **موصلات الذكاء الاصطناعي**: هذا واجهة مع خدمات الذكاء الاصطناعي الخارجية ومصادر البيانات للاستخدام في كل من Python وC#.

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

    هنا لديك مثال بسيط حول كيفية إنشاء kernel وإضافة خدمة إكمال الدردشة. يقوم Semantic Kernel بإنشاء اتصال مع خدمة ذكاء اصطناعي خارجية، في هذه الحالة، Azure OpenAI Chat Completion.

- **الإضافات**: هذه تغلف الوظائف التي يمكن للتطبيق استخدامها. هناك إضافات جاهزة وأخرى مخصصة يمكنك إنشاؤها. مفهوم ذو صلة هو "وظائف التعليمات". بدلاً من تقديم إشارات لغة طبيعية لاستدعاء الوظائف، تقوم ببث وظائف معينة إلى النموذج. بناءً على سياق الدردشة الحالي، قد يختار النموذج استدعاء إحدى هذه الوظائف لإكمال طلب أو استفسار. إليك مثال:

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

    هنا، لديك أولاً قالب تعليمات `skPrompt` يترك مساحة للمستخدم لإدخال النص، `$userInput`. ثم تقوم بإنشاء وظيفة kernel `SummarizeText` ثم استيرادها إلى kernel باسم الإضافة `SemanticFunctions`. لاحظ اسم الوظيفة الذي يساعد Semantic Kernel على فهم ما تفعله الوظيفة ومتى يجب استدعاؤها.

- **وظيفة أصلية**: هناك أيضًا وظائف أصلية يمكن للإطار استدعاؤها مباشرةً لتنفيذ المهمة. إليك مثال على وظيفة كهذه تسترجع المحتوى من ملف:

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

- **الذاكرة**: تبسط إدارة السياق للتطبيقات الذكية. الفكرة مع الذاكرة هي أن هذا شيء يجب أن يعرفه النموذج. يمكنك تخزين هذه المعلومات في مخزن متجه ينتهي به الأمر إلى أن يكون قاعدة بيانات في الذاكرة أو قاعدة بيانات متجهة أو ما شابه. إليك مثال على سيناريو مبسط جدًا حيث يتم إضافة *حقائق* إلى الذاكرة:

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

يتم تخزين هذه الحقائق بعد ذلك في مجموعة الذاكرة `SummarizedAzureDocs`. هذا مثال مبسط للغاية، ولكن يمكنك أن ترى كيف يمكن تخزين المعلومات في الذاكرة لاستخدامها من قبل LLM.

إذن، هذه هي أساسيات إطار عمل Semantic Kernel، ماذا عن إطار عمل الوكيل؟

## خدمة Azure AI Agent

خدمة Azure AI Agent هي إضافة حديثة تم تقديمها في Microsoft Ignite 2024. تتيح تطوير ونشر وكلاء الذكاء الاصطناعي باستخدام نماذج أكثر مرونة، مثل استدعاء نماذج LLM مفتوحة المصدر مباشرةً مثل Llama 3 وMistral وCohere.

توفر خدمة Azure AI Agent آليات أمان أقوى للمؤسسات وطرق تخزين بيانات، مما يجعلها مناسبة لتطبيقات المؤسسات.

تعمل هذه الخدمة مباشرة مع أطر تنسيق الوكلاء المتعددة مثل AutoGen وSemantic Kernel.

هذه الخدمة حاليًا في العرض العام التجريبي وتدعم Python وC# لبناء الوكلاء.

باستخدام Semantic Kernel Python، يمكننا إنشاء وكيل Azure AI مع مكون إضافي يحدده المستخدم:

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

### المفاهيم الأساسية

تتضمن خدمة Azure AI Agent المفاهيم الأساسية التالية:

- **الوكيل**. تتكامل خدمة Azure AI Agent مع Azure AI Foundry. داخل AI Foundry، يعمل وكيل الذكاء الاصطناعي كخدمة صغيرة "ذكية" يمكن استخدامها للإجابة على الأسئلة (RAG)، أو تنفيذ الإجراءات، أو أتمتة سير العمل بالكامل. يتم تحقيق ذلك من خلال الجمع بين قوة نماذج الذكاء الاصطناعي التوليدية والأدوات التي تتيح لها الوصول إلى مصادر البيانات الواقعية والتفاعل معها. إليك مثال على وكيل:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    في هذا المثال، يتم إنشاء وكيل باستخدام النموذج `gpt-4o-mini`، واسم `my-agent`، وتعليمات `You are helpful agent`. يتم تجهيز الوكيل بأدوات وموارد لتنفيذ مهام تفسير الكود.

- **الخيط والرسائل**. الخيط هو مفهوم مهم آخر. يمثل محادثة أو تفاعل بين الوكيل والمستخدم. يمكن استخدام الخيوط لتتبع تقدم المحادثة، وتخزين معلومات السياق، وإدارة حالة التفاعل. إليك مثال على خيط:

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

    في الكود السابق، يتم إنشاء خيط. بعد ذلك، يتم إرسال رسالة إلى الخيط. من خلال استدعاء `create_and_process_run`، يُطلب من الوكيل تنفيذ العمل على الخيط. أخيرًا، يتم جلب الرسائل وتسجيلها لرؤية استجابة الوكيل. تشير الرسائل إلى تقدم المحادثة بين المستخدم والوكيل. من المهم أيضًا فهم أن الرسائل يمكن أن تكون من أنواع مختلفة مثل النصوص أو الصور أو الملفات، أي أن عمل الوكيل قد أسفر عن صورة أو استجابة نصية على سبيل المثال. كالمطور، يمكنك بعد ذلك استخدام هذه المعلومات لمعالجة الاستجابة بشكل أكبر أو تقديمها للمستخدم.

- **التكامل مع أطر الذكاء الاصطناعي الأخرى**. يمكن لخدمة Azure AI Agent التفاعل مع أطر أخرى مثل AutoGen وSemantic Kernel، مما يعني أنه يمكنك بناء جزء من تطبيقك في أحد هذه الأطر واستخدام خدمة الوكيل كمنسق، أو يمكنك بناء كل شيء في خدمة الوكيل.

**حالات الاستخدام**: تم تصميم خدمة Azure AI Agent لتطبيقات المؤسسات التي تتطلب نشر وكلاء ذكاء اصطناعي آمن وقابل للتوسع ومرن.

## ما الفرق بين هذه الأطر؟

قد يبدو أن هناك الكثير من التداخل بين هذه الأطر، ولكن هناك بعض الاختلافات الرئيسية من حيث التصميم والقدرات وحالات الاستخدام المستهدفة:

- **AutoGen**: هو إطار عمل للتجارب يركز على الأبحاث المتقدمة في أنظمة الوكلاء المتعددة. إنه المكان الأفضل للتجربة والنمذجة الأولية لأنظمة الوكلاء المتعددة المتطورة.
- **Semantic Kernel**: هو مكتبة وكلاء جاهزة للإنتاج لبناء تطبيقات وكلاء للمؤسسات. يركز على التطبيقات الوكيلية الموزعة والموجهة بالأحداث، مما يتيح استخدام LLMs وSLMs متعددة، وأدوات، وأنماط تصميم وكلاء فردية/متعددة.
- **Azure AI Agent Service**: هو منصة وخدمة نشر في Azure Foundry للوكلاء. يوفر بناء الاتصال بالخدمات المدعومة من Azure مثل Azure OpenAI وAzure AI Search وBing Search وتنفيذ الكود.

ما زلت غير متأكد أيهما تختار؟

### حالات الاستخدام

دعنا نحاول مساعدتك من خلال استعراض بعض حالات الاستخدام الشائعة:

> س: أنا أجرب وأتعلم وأبني تطبيقات وكلاء كدليل على المفهوم، وأريد أن أتمكن من البناء والتجربة بسرعة
>

> ج: سيكون AutoGen خيارًا جيدًا لهذا السيناريو، حيث يركز على التطبيقات الوكيلية الموزعة والموجهة بالأحداث ويدعم أنماط تصميم وكلاء متعددة متقدمة.

> س: ما الذي يجعل AutoGen خيارًا أفضل من Semantic Kernel وAzure AI Agent Service لهذا الاستخدام؟
>
> ج: تم تصميم AutoGen خصيصًا للتطبيقات الوكيلية الموزعة والموجهة بالأحداث، مما يجعله مناسبًا لأتمتة مهام توليد الكود وتحليل البيانات. يوفر الأدوات والقدرات اللازمة لبناء أنظمة وكلاء متعددة معقدة بكفاءة.

> س: يبدو أن Azure AI Agent Service يمكن أن يعمل هنا أيضًا، فهو يحتوي على أدوات لتوليد الكود والمزيد؟
>
> ج: نعم، خدمة Azure AI Agent هي منصة للوكلاء وتضيف قدرات مدمجة لنماذج متعددة، وAzure AI Search، وBing Search، وAzure Functions. يجعل ذلك من السهل بناء وكلائك في بوابة Foundry ونشرهم على نطاق واسع.

> س: ما زلت مرتبكًا، فقط أعطني خيارًا واحدًا
>
> ج: خيار رائع هو بناء تطبيقك في Semantic Kernel أولاً ثم استخدام Azure AI Agent Service لنشر وكيلك. يتيح لك هذا النهج الاحتفاظ بوكلائك بسهولة مع الاستفادة من قوة بناء أنظمة وكلاء متعددة في Semantic Kernel. بالإضافة إلى ذلك، يحتوي Semantic Kernel على موصل في AutoGen، مما يجعل من السهل استخدام كلا الإطارين معًا.

دعنا نلخص الاختلافات الرئيسية في جدول:

| الإطار | التركيز | المفاهيم الأساسية | حالات الاستخدام |
| --- | --- | --- | --- |
| AutoGen | التطبيقات الوكيلية الموزعة والموجهة بالأحداث | الوكلاء، الشخصيات، الوظائف، البيانات | توليد الكود، مهام تحليل البيانات |
| Semantic Kernel | فهم وتوليد محتوى يشبه النصوص البشرية | الوكلاء، المكونات المعيارية، التعاون | فهم اللغة الطبيعية، توليد المحتوى |
| Azure AI Agent Service | نماذج مرنة، أمان المؤسسات، توليد الكود، استدعاء الأدوات | التشكيل، التعاون، تنسيق العمليات | نشر وكلاء ذكاء اصطناعي آمن وقابل للتوسع ومرن |

ما هو الاستخدام المثالي لكل من هذه الأطر؟

## هل يمكنني دمج أدوات نظام Azure البيئي الحالية مباشرةً، أم أحتاج إلى حلول مستقلة؟

الإجابة هي نعم، يمكنك دمج أدوات نظام Azure البيئي الحالية مباشرةً مع خدمة Azure AI Agent، خاصةً لأنها تم تصميمها للعمل بسلاسة مع خدمات Azure الأخرى. يمكنك على سبيل المثال دمج Bing وAzure AI Search وAzure Functions. هناك أيضًا تكامل عميق مع Azure AI Foundry.

بالنسبة لـ AutoGen وSemantic Kernel، يمكنك أيضًا دمجها مع خدمات Azure، ولكن قد يتطلب ذلك استدعاء خدمات Azure من الكود الخاص بك. طريقة أخرى للتكامل هي استخدام SDKs الخاصة بـ Azure للتفاعل مع خدمات Azure من وكلائك. بالإضافة إلى ذلك، كما ذكرنا، يمكنك استخدام خدمة Azure AI Agent كمنسق لوكلائك المبنيين في AutoGen أو Semantic Kernel، مما يوفر وصولاً سهلاً إلى نظام Azure البيئي.

## أكواد أمثلة

- Python: [إطار عمل الوكيل](./code_samples/02-python-agent-framework.ipynb)
- .NET: [إطار عمل الوكيل](./code_samples/02-dotnet-agent-framework.md)

## هل لديك المزيد من الأسئلة حول أطر عمل وكلاء الذكاء الاصطناعي؟

انضم إلى [Discord الخاص بـ Azure AI Foundry](https://aka.ms/ai-agents/discord) للتواصل مع متعلمين آخرين، وحضور ساعات العمل، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## المراجع

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">خدمة Azure Agent</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel وAutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">إطار عمل وكيل Semantic Kernel Python</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">إطار عمل وكيل Semantic Kernel .Net</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">خدمة Azure AI Agent</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">استخدام خدمة Azure AI Agent مع AutoGen / Semantic Kernel لبناء حل متعدد الوكلاء</a>

## الدرس السابق

[مقدمة إلى وكلاء الذكاء الاصطناعي وحالات الاستخدام](../01-intro-to-ai-agents/README.md)

## الدرس التالي

[فهم أنماط تصميم الوكلاء](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالترجمة البشرية الاحترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->