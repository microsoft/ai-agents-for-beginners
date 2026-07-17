[![استكشاف أُطُر وكلاء الذكاء الاصطناعي](../../../translated_images/ar/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

# استكشاف أُطُر وكلاء الذكاء الاصطناعي

أُطُر وكلاء الذكاء الاصطناعي هي منصات برمجية مصممة لتبسيط إنشاء ونشر وإدارة وكلاء الذكاء الاصطناعي. توفر هذه الأُطُر للمطورين مكونات وأبسطيات وأدوات جاهزة تساعد في تبسيط تطوير أنظمة الذكاء الاصطناعي المعقدة.

تساعد هذه الأُطُر المطورين على التركيز على الجوانب الفريدة لتطبيقاتهم من خلال توفير أساليب موحدة للتحديات الشائعة في تطوير وكلاء الذكاء الاصطناعي. كما تعزز القدرة على التوسع وسهولة الوصول والكفاءة في بناء أنظمة الذكاء الاصطناعي.

## مقدمة

سيغطي هذا الدرس:

- ما هي أُطُر وكلاء الذكاء الاصطناعي وما الذي تمكّن المطورين من تحقيقه؟
- كيف يمكن للفرق استخدام هذه الأُطُر لبناء نماذج أولية بسرعة، وإجراء التكرارات، وتحسين قدرات وكيلهم؟
- ما الفروقات بين الأُطُر والأدوات التي طورتها مايكروسوفت (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">خدمة وكيل مايكروسوفت فاوندرِي</a> و<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">إطار عمل وكيل مايكروسوفت</a>)؟
- هل يمكنني دمج أدوات نظام Azure الموجود لدي مباشرةً، أم أحتاج إلى حلول مستقلة؟
- ما هي خدمة وكيل مايكروسوفت فاوندرِي وكيف تساعدني؟

## أهداف التعلم

أهداف هذا الدرس هي مساعدتك على فهم:

- دور أُطُر وكلاء الذكاء الاصطناعي في تطوير الذكاء الاصطناعي.
- كيفية الاستفادة من أُطُر وكلاء الذكاء الاصطناعي لبناء وكلاء أذكياء.
- القدرات الأساسية التي تمكّنها أُطُر وكلاء الذكاء الاصطناعي.
- الفروقات بين إطار عمل وكيل مايكروسوفت وخدمة وكيل مايكروسوفت فاوندرِي.

## ما هي أُطُر وكلاء الذكاء الاصطناعي وما الذي تمكّن المطورين من القيام به؟

يمكن لأُطُر الذكاء الاصطناعي التقليدية مساعدتك في دمج الذكاء الاصطناعي داخل تطبيقاتك وتحسين هذه التطبيقات بالطرق التالية:

- **التخصيص**: يمكن للذكاء الاصطناعي تحليل سلوك وتفضيلات المستخدم لتقديم توصيات ومحتوى وتجارب مخصصة.
مثال: خدمات البث مثل Netflix تستخدم الذكاء الاصطناعي لاقتراح الأفلام والبرامج بناءً على تاريخ المشاهدة، مما يعزز تفاعل المستخدم ورضاه.
- **الأتمتة والكفاءة**: يمكن للذكاء الاصطناعي أتمتة المهام المتكررة، تبسيط سير العمل، وتحسين الكفاءة التشغيلية.
مثال: تطبيقات خدمة العملاء تستخدم روبوتات الدردشة المدعومة بالذكاء الاصطناعي للتعامل مع الاستفسارات الشائعة، مما يقلل أوقات الاستجابة ويحرر وكلاء البشر للتعامل مع القضايا المعقدة.
- **تحسين تجربة المستخدم**: يمكن للذكاء الاصطناعي تحسين التجربة العامة للمستخدم بتوفير ميزات ذكية مثل التعرف على الصوت، معالجة اللغة الطبيعية، والنص التنبؤي.
مثال: المساعدون الافتراضيون مثل Siri وGoogle Assistant يستخدمون الذكاء الاصطناعي لفهم الأوامر الصوتية والرد عليها، مما يسهل تفاعل المستخدمين مع أجهزتهم.

### كل ذلك يبدو رائعًا، أليس كذلك؟ فلماذا نحتاج إلى إطار وكيل الذكاء الاصطناعي؟

تمثل أُطُر وكلاء الذكاء الاصطناعي شيئًا أكثر من مجرد أُطُر ذكاء اصطناعي عادية. فهي مصممة لتمكين إنشاء وكلاء أذكياء يمكنهم التفاعل مع المستخدمين، وكلاء آخرين، والبيئة لتحقيق أهداف محددة. يمكن لهذه الوكلاء إظهار سلوك مستقل، اتخاذ قرارات، والتكيف مع الظروف المتغيرة. دعونا نلقي نظرة على بعض القدرات الرئيسية التي تمكّنها أُطُر وكلاء الذكاء الاصطناعي:

- **تعاون وتنسيق الوكلاء**: تمكين إنشاء عدة وكلاء ذكاء اصطناعي يمكنهم العمل معًا، التواصل والتنسيق لحل مهام معقدة.
- **أتمتة وإدارة المهام**: توفير آليات لأتمتة سير العمل متعدد الخطوات، توزيع المهام، وإدارة المهام الديناميكية بين الوكلاء.
- **الفهم السياقي والتكيف**: تزويد الوكلاء بالقدرة على فهم السياق، التكيف مع البيئات المتغيرة، واتخاذ قرارات بناءً على المعلومات الآنية.

إذًا في الخلاصة، الوكلاء يسمحون لك بفعل المزيد، رفع مستوى الأتمتة، وإنشاء أنظمة أكثر ذكاءً يمكنها التكيف والتعلم من بيئتها.

## كيف نبني نموذجًا أوليًا بسرعة، نكرر عليه، ونحسن قدرات الوكيل؟

هذه مجال يتطور بسرعة، لكن هناك بعض الأشياء الشائعة عبر معظم أُطُر وكلاء الذكاء الاصطناعي التي تساعدك على بناء نموذج أولي سريعًا وإجراء التكرارات، وهي مكونات الوحدة، الأدوات التعاونية، والتعلم في الوقت الحقيقي. دعونا نستعرضها:

- **استخدام مكونات الوحدة**: تقدم SDKs الذكاء الاصطناعي مكونات جاهزة مثل موصلات الذكاء الاصطناعي والذاكرة، استدعاء وظائف باستخدام اللغة الطبيعية أو الإضافات البرمجية، قوالب الطلب، والمزيد.
- **الاستفادة من الأدوات التعاونية**: تصميم وكلاء بأدوار ومهام محددة، ليتمكنوا من اختبار وصقل سير العمل التعاوني.
- **التعلم في الوقت الحقيقي**: تنفيذ حلقات ملاحظات حيث يتعلم الوكلاء من التفاعلات ويعدلوا سلوكهم بشكل ديناميكي.

### استخدام مكونات الوحدة

توفر SDKs مثل إطار عمل وكيل مايكروسوفت مكونات جاهزة مثل موصلات الذكاء الاصطناعي، تعريفات الأدوات، وإدارة الوكلاء.

**كيف يمكن للفرق استخدام هذه**: يمكن للفرق تجميع هذه المكونات بسرعة لإنشاء نموذج أولي وظيفي دون البدء من الصفر، مما يسمح بالتجريب السريع والتكرار.

**كيف يعمل ذلك عمليًا**: يمكنك استخدام محلل جاهز لاستخراج المعلومات من إدخال المستخدم، وحدة ذاكرة لتخزين واسترجاع البيانات، ومُولّد طلبات للتفاعل مع المستخدمين، كل ذلك دون الحاجة لبناء هذه المكونات من الصفر.

**كود مثال**. دعونا ننظر إلى مثال عن كيفية استخدام إطار عمل وكيل مايكروسوفت مع `FoundryChatClient` لجعل الموديل يستجيب لإدخال المستخدم مع استدعاء الأدوات:

``` python
# مثال على إطار عمل Microsoft Agent بلغة بايثون

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# تعريف دالة أداة نموذجية لحجز السفر
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # مخرجات المثال: تم حجز رحلتك إلى نيويورك في 1 يناير 2025 بنجاح. سفر آمن! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ما تراه من هذا المثال هو كيف يمكنك الاستفادة من محلل جاهز لاستخراج معلومات رئيسية من إدخال المستخدم، مثل الأصل، الوجهة، وتاريخ طلب حجز رحلة طيران. تسمح لك هذه الطريقة المكونة بالتركيز على المنطق العالي المستوى.

### الاستفادة من الأدوات التعاونية

تسهّل أُطُر مثل إطار عمل وكيل مايكروسوفت إنشاء عدة وكلاء يمكنهم العمل معًا.

**كيف يمكن للفرق استخدام هذه**: يمكن للفرق تصميم وكلاء بأدوار ومهام محددة، مما يمكّنهم من اختبار وصقل سير العمل التعاوني وتحسين كفاءة النظام بشكل عام.

**كيف يعمل ذلك عمليًا**: يمكنك إنشاء فريق من الوكلاء، حيث لكل وكيل وظيفة متخصصة مثل استرجاع البيانات، التحليل، أو اتخاذ القرارات. يمكن للوكلاء التواصل ومشاركة المعلومات لتحقيق هدف مشترك، مثل الرد على استفسار المستخدم أو إكمال مهمة.

**كود مثال (إطار عمل وكيل مايكروسوفت)**:

```python
# إنشاء عدة وكلاء يعملون معًا باستخدام إطار عمل Microsoft Agent

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# وكيل استرجاع البيانات
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# وكيل تحليل البيانات
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# تشغيل الوكلاء بالتسلسل على مهمة
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

ما تراه في الكود السابق هو كيفية إنشاء مهمة تشمل عدة وكلاء يعملون معًا لتحليل البيانات. كل وكيل يؤدي وظيفة محددة، وتُنفذ المهمة بتنسيق عمل الوكلاء لتحقيق النتيجة المرجوة. بإنشاء وكلاء مخصصين بأدوار متخصصة، يمكنك تحسين كفاءة وأداء المهمة.

### التعلم في الوقت الحقيقي

توفر الأُطُر المتقدمة قدرات لفهم السياق في الوقت الحقيقي والتكيف معه.

**كيف يمكن للفرق استخدام هذه**: يمكن للفرق تنفيذ حلقات ملاحظات حيث يتعلم الوكلاء من التفاعلات ويعدلون سلوكهم بشكل ديناميكي، مما يؤدي إلى تحسين مستمر وصقل للقدرات.

**كيف يعمل ذلك عمليًا**: يمكن للوكلاء تحليل ملاحظات المستخدم، بيانات البيئة، ونتائج المهام لتحديث قاعدة معرفتهم، تعديل خوارزميات اتخاذ القرار، وتحسين الأداء مع مرور الوقت. تُمكّن هذه العملية التكرارية الوكلاء من التكيف مع الظروف المتغيرة وتفضيلات المستخدم، مما يعزز فعالية النظام بشكل عام.

## ما الفرق بين إطار عمل وكيل مايكروسوفت وخدمة وكيل مايكروسوفت فاوندرِي؟

هناك عدة طرق للمقارنة بين هذه الأُطُر، لكن دعونا نلقي نظرة على بعض الفروقات الرئيسية من حيث التصميم، القدرات، وحالات الاستخدام المستهدفة:

## إطار عمل وكيل مايكروسوفت (MAF)

يوفر إطار عمل وكيل مايكروسوفت SDK مبسط لبناء وكلاء الذكاء الاصطناعي باستخدام `FoundryChatClient`. يمكّن المطورين من إنشاء وكلاء يستخدمون موديلات Azure OpenAI مع استدعاء أدوات مدمج، إدارة المحادثة، وأمان بمستوى المؤسسة من خلال هوية Azure.

**حالات الاستخدام**: بناء وكلاء ذكيين جاهزين للإنتاج مع استخدام الأدوات، سير عمل متعدد الخطوات، وسيناريوهات تكامل المؤسسة.

إليك بعض المفاهيم الأساسية الهامة في إطار عمل وكيل مايكروسوفت:

- **الوكلاء**. يتم إنشاء الوكيل عبر `FoundryChatClient` ويتم تهيئته باسم، تعليمات، وأدوات. يمكن للوكيل:
  - **معالجة رسائل المستخدم** وتوليد الردود باستخدام موديلات Azure OpenAI.
  - **استدعاء الأدوات** تلقائيًا بناءً على سياق المحادثة.
  - **الحفاظ على حالة المحادثة** عبر تفاعلات متعددة.

  إليك مقتطف كود يوضح كيفية إنشاء وكيل:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **الأدوات**. يدعم الإطار تعريف الأدوات كدوال بايثون يمكن للوكيل استدعاؤها تلقائيًا. يتم تسجيل الأدوات عند إنشاء الوكيل:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **تنسيق متعدد الوكلاء**. يمكنك إنشاء عدة وكلاء بتخصصات مختلفة وتنسيق عملهم:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **تكامل هوية Azure**. يستخدم الإطار `AzureCliCredential` (أو `DefaultAzureCredential`) للمصادقة الآمنة بدون مفاتيح، مما يلغي الحاجة لإدارة مفاتيح API مباشرة.

## خدمة وكيل مايكروسوفت فاوندرِي

خدمة وكيل مايكروسوفت فاوندرِي هي إضافة أحدث، تم تقديمها في Microsoft Ignite 2024. تسمح بتطوير ونشر وكلاء ذكاء اصطناعي باستخدام نماذج أكثر مرونة، مثل استدعاء مباشرة لنماذج LLM مفتوحة المصدر مثل Llama 3، Mistral، وCohere.

توفر خدمة وكيل مايكروسوفت فاوندرِي آليات أمان أقوى للمؤسسات وأساليب تخزين بيانات مناسبة، مما يجعلها مثالية للتطبيقات المؤسسية.

تعمل هذه الخدمة بشكل متوافق مع إطار عمل وكيل مايكروسوفت لبناء ونشر الوكلاء.

الخدمة حاليًا في المعاينة العامة وتدعم بايثون وC# لبناء الوكلاء.

باستخدام SDK خدمة وكيل مايكروسوفت فاوندرِي لبايثون، يمكننا إنشاء وكيل بأداة معرفة من المستخدم:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# تعريف وظائف الأداة
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### المفاهيم الأساسية

تحتوي خدمة وكيل مايكروسوفت فاوندرِي على المفاهيم الأساسية التالية:

- **الوكيل**. تتكامل خدمة وكيل مايكروسوفت فاوندرِي مع Microsoft Foundry. داخل مايكروسوفت فاوندرِي، يعمل الوكيل الذكي كـ "خدمة مصغرة" يمكن استخدامها للإجابة على الأسئلة (RAG)، تنفيذ الأفعال، أو أتمتة سير العمل بالكامل. يحقق ذلك من خلال دمج قوة نماذج الذكاء الاصطناعي التوليدية مع أدوات تسمح له بالوصول والتفاعل مع مصادر البيانات الحقيقية. إليك مثال على وكيل:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    في هذا المثال، تم إنشاء وكيل بالموديل `gpt-4.1-mini`، بالاسم `my-agent`، والتعليمات `أنت وكيل مساعد`. تم تجهيز الوكيل بأدوات وموارد لتنفيذ مهام تفسير الكود.

- **الخيط والرسائل**. الخيط هو مفهوم مهم آخر. يمثل محادثة أو تفاعلًا بين الوكيل والمستخدم. يمكن استخدام الخيوط لتتبع تقدم المحادثة، تخزين معلومات السياق، وإدارة حالة التفاعل. إليك مثال على خيط:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # اطلب من الوكيل تنفيذ العمل على الخيط
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # جلب وتسجيل جميع الرسائل لرؤية رد الوكيل
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    في الكود السابق، تم إنشاء خيط. بعدها تم إرسال رسالة للخيط. من خلال استدعاء `create_and_process_run`، يُطلب من الوكيل تنفيذ عمل على الخيط. أخيرًا، يتم جلب الرسائل وتسجيلها لرؤية رد الوكيل. تشير الرسائل إلى تقدم المحادثة بين المستخدم والوكيل. من المهم أيضًا فهم أن الرسائل يمكن أن تكون من أنواع مختلفة مثل نص، صورة، أو ملف، أي أن عمل الوكلاء نتج عنه على سبيل المثال صورة أو رد نصي. كمطور، يمكنك استخدام هذه المعلومات لمزيد من معالجة الرد أو عرضه للمستخدم.

- **التكامل مع إطار عمل وكيل مايكروسوفت**. تعمل خدمة وكيل مايكروسوفت فاوندرِي بسلاسة مع إطار عمل وكيل مايكروسوفت، مما يعني أنه يمكنك بناء الوكلاء باستخدام `FoundryChatClient` ونشرهم عبر خدمة الوكيل لسيناريوهات الإنتاج.

**حالات الاستخدام**: تم تصميم خدمة وكيل مايكروسوفت فاوندرِي لتطبيقات المؤسسات التي تتطلب نشر وكلاء ذكاء اصطناعي آمن وقابل للتوسع ومرن.

## ما الفرق بين هذه الأُطُر؟
 
قد يبدو كأن هناك تداخلًا، لكن توجد بعض الفروقات الرئيسية من حيث التصميم، القدرات، وحالات الاستخدام المستهدفة:
 
- **إطار عمل وكيل مايكروسوفت (MAF)**: هو SDK جاهز للإنتاج لبناء وكلاء الذكاء الاصطناعي. يوفر API مبسط لإنشاء وكلاء مع استدعاء أدوات، إدارة المحادثة، وتكامل هوية Azure.
- **خدمة وكيل مايكروسوفت فاوندرِي**: هي منصة وخدمة نشر في Microsoft Foundry للوكلاء. تقدم اتصالًا مدمجًا مع خدمات مثل Azure OpenAI، Azure AI Search، Bing Search وتنفيذ الكود.
 
ما زلت غير متأكد أي واحد تختار؟

### حالات الاستخدام
 
دعنا نساعدك من خلال طرح بعض حالات الاستخدام الشائعة:
 
> س: أبني تطبيقات وكلاء الذكاء الاصطناعي للإنتاج وأرغب في البدء بسرعة
>

>ج: إطار عمل وكيل مايكروسوفت خيار رائع. يوفر API بسيط بايثوني عبر `FoundryChatClient` يتيح لك تعريف الوكلاء بالأدوات والتعليمات في بضعة أسطر من الكود.

>س: أحتاج نشر بمستوى مؤسسة مع تكاملات Azure مثل البحث وتنفيذ الكود
>
> ج: خدمة وكيل مايكروسوفت فاوندرِي هي الأنسب. إنها خدمة منصة توفر قدرات مدمجة لعدة نماذج، Azure AI Search، Bing Search، وAzure Functions. تجعل من السهل بناء وكلائك في بوابة Foundry ونشرهم على نطاق واسع.
 
> س: ما زلت مرتبكًا، أعطني خيارًا واحدًا فقط
>
> ج: ابدأ بإطار عمل وكيل مايكروسوفت لإنشاء وكلائك، ثم استخدم خدمة وكيل مايكروسوفت فاوندرِي عندما تحتاج إلى نشرهم وتوسيعهم في الإنتاج. تتيح لك هذه الطريقة التكرار السريع على منطق وكيلك مع وجود طريق واضح للنشر المؤسسي.
 
دعنا نلخص الفروقات الرئيسية في جدول:

| الإطار | التركيز | المفاهيم الأساسية | حالات الاستخدام |
| --- | --- | --- | --- |
| إطار عمل وكيل مايكروسوفت | SDK مبسط للوكلاء مع استدعاء الأدوات | الوكلاء، الأدوات، هوية Azure | بناء وكلاء الذكاء الاصطناعي، استخدام الأدوات، سير عمل متعدد الخطوات |
| خدمة وكيل مايكروسوفت فاوندرِي | نماذج مرنة، أمان المؤسسات، توليد الكود، استدعاء الأدوات | التكوينية، التعاون، تنظيم العمليات | نشر آمن، قابل للتوسع، ومرن لوكلاء الذكاء الاصطناعي |

## هل يمكنني دمج أدوات نظام Azure الموجود لدي مباشرةً، أم أحتاج إلى حلول مستقلة؟


الجواب هو نعم، يمكنك دمج أدوات نظام Azure الخاص بك الموجودة مباشرة مع خدمة Microsoft Foundry Agent خاصة، لأنها تم بناؤها للعمل بسلاسة مع خدمات Azure الأخرى. يمكنك على سبيل المثال دمج Bing وAzure AI Search وAzure Functions. هناك أيضًا تكامل عميق مع Microsoft Foundry.

يدمج إطار عمل Microsoft Agent أيضًا مع خدمات Azure من خلال `FoundryChatClient` وهوية Azure، مما يتيح لك استدعاء خدمات Azure مباشرة من أدوات الوكيل الخاصة بك.

## أمثلة على الأكواد

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## هل لديك المزيد من الأسئلة حول أُطُر وكلاء الذكاء الاصطناعي؟

انضم إلى [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) للقاء متعلمين آخرين، وحضور ساعات المكتب، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## مراجع

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">خدمة وكيل Azure</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">إطار عمل Microsoft Agent - ردود Azure OpenAI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">خدمة وكيل Microsoft Foundry</a>

## الدرس السابق

[مقدمة إلى وكلاء الذكاء الاصطناعي وحالات استخدام الوكلاء](../01-intro-to-ai-agents/README.md)

## الدرس التالي

[فهم أنماط تصميم الوكيل](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->