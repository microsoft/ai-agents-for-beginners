[![استكشاف أُطُر وكلاء الذكاء الاصطناعي](../../../translated_images/ar/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(انقر على الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

# استكشاف أُطُر وكلاء الذكاء الاصطناعي

أُطُر وكلاء الذكاء الاصطناعي هي منصات برمجية مصممة لتبسيط إنشاء ونشر وإدارة وكلاء الذكاء الاصطناعي. توفر هذه الأُطُر للمطورين مكونات، وتجريدات، وأدوات جاهزة تسهل تطوير أنظمة الذكاء الاصطناعي المعقدة.

تساعد هذه الأُطُر المطورين على التركيز على الجوانب الفريدة لتطبيقاتهم من خلال توفير طرق موحدة للتحديات الشائعة في تطوير وكلاء الذكاء الاصطناعي. كما أنها تعزز القابلية للتوسع، وسهولة الوصول، والكفاءة في بناء أنظمة الذكاء الاصطناعي.

## مقدمة

هذا الدرس سيغطي:

- ما هي أُطُر وكلاء الذكاء الاصطناعي وما الذي تُمكن المطورين من تحقيقه؟
- كيف يمكن للفرق استخدام هذه الأُطُر لعمل نموذج أولي سريع، وتكرار العمل، وتحسين قدرات الوكلاء؟
- ما هي الاختلافات بين الأُطُر والأدوات التي أنشأتها مايكروسوفت (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">خدمة وكيل Microsoft Foundry</a> و<a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">إطار عمل وكيل مايكروسوفت</a>)؟
- هل يمكنني دمج أدوات نظام Azure الحالي مباشرة، أم أحتاج إلى حلول مستقلة؟
- ما هي خدمة وكيل مايكروسوفت فاوندرى وكيف تساعدني؟

## أهداف التعلم

أهداف هذا الدرس هي مساعدتك على فهم:

- دور أُطُر وكلاء الذكاء الاصطناعي في تطوير الذكاء الاصطناعي.
- كيفية الاستفادة من أُطُر وكلاء الذكاء الاصطناعي لبناء وكلاء ذكيين.
- القدرات الرئيسية التي توفرها أُطُر وكلاء الذكاء الاصطناعي.
- الفروقات بين إطار عمل وكيل مايكروسوفت وخدمة وكيل Microsoft Foundry.

## ما هي أُطُر وكلاء الذكاء الاصطناعي وما الذي تمكن المطورين من فعله؟

تساعد أُطُر الذكاء الاصطناعي التقليدية على إدماج الذكاء الاصطناعي في تطبيقاتك وتحسينها بالطرق التالية:

- **التخصيص**: يمكن للذكاء الاصطناعي تحليل سلوك المستخدم وتفضيلاته لتقديم توصيات، ومحتوى، وتجارب مخصصة.
مثال: تستخدم خدمات البث مثل Netflix الذكاء الاصطناعي لاقتراح أفلام وعروض بناءً على سجل المشاهدة، مما يزيد من تفاعل المستخدم ورضاه.
- **الأتمتة والكفاءة**: يمكن للذكاء الاصطناعي أتمتة المهام المتكررة، وتبسيط سير العمل، وتحسين الكفاءة التشغيلية.
مثال: تستخدم تطبيقات خدمة العملاء روبوتات دردشة مدعومة بالذكاء الاصطناعي للتعامل مع الاستفسارات الشائعة، مما يقلل أوقات الاستجابة ويحرر وكلاء البشر للقضايا المعقدة.
- **تعزيز تجربة المستخدم**: يمكن للذكاء الاصطناعي تحسين تجربة المستخدم العامة من خلال تقديم ميزات ذكية مثل التعرف على الصوت، ومعالجة اللغة الطبيعية، والنص التنبؤي.
مثال: تستخدم المساعدات الافتراضية مثل Siri وGoogle Assistant الذكاء الاصطناعي لفهم الأوامر الصوتية والرد عليها، مما يسهل على المستخدمين التفاعل مع أجهزتهم.

### كل هذا يبدو رائعًا، فلماذا نحتاج إلى إطار عمل وكيل الذكاء الاصطناعي؟

أُطُر وكلاء الذكاء الاصطناعي تمثل شيئًا أكثر من مجرد أُطُر ذكاء اصطناعي. فهي مصممة لتمكين إنشاء وكلاء أذكياء يمكنهم التفاعل مع المستخدمين، ووكلاء آخرين، والبيئة لتحقيق أهداف محددة. يمكن أن يظهر هؤلاء الوكلاء سلوكًا مستقلًا، واتخاذ قرارات، والتكيف مع الظروف المتغيرة. لنلقِ نظرة على بعض القدرات الرئيسية التي توفرها أُطُر وكلاء الذكاء الاصطناعي:

- **تعاون وتنسيق الوكلاء**: تمكين إنشاء وكلاء متعددين يمكنهم العمل معًا، والتواصل، والتنسيق لحل مهام معقدة.
- **أتمتة وإدارة المهام**: توفير آليات لأتمتة سير عمل متعدد الخطوات، وتفويض المهام، وإدارة ديناميكية للمهام بين الوكلاء.
- **فهم السياق والتكيف**: تزويد الوكلاء بالقدرة على فهم السياق، والتكيف مع البيئات المتغيرة، واتخاذ القرارات استنادًا إلى المعلومات في الوقت الحقيقي.

إذًا في المجمل، تتيح لك الوكلاء القيام بالمزيد، والارتقاء بالأتمتة إلى المستوى التالي، وإنشاء أنظمة أذكى يمكنها التكيف والتعلم من بيئتها.

## كيفية صنع نموذج أولي سريع، والتكرار، وتحسين قدرات الوكيل؟

هذه الساحة تتطور بسرعة، ولكن هناك بعض الأمور المشتركة بين معظم أُطُر وكلاء الذكاء الاصطناعي التي يمكن أن تساعدك في صنع نموذج أولي سريع والتكرار، وخصوصًا المكونات المعيارية، والأدوات التعاونية، والتعلم في الوقت الحقيقي. لنغص في هذه الأمور:

- **استخدام المكونات المعيارية**: توفر حزم تطوير البرامج مكونات جاهزة مثل موصلات الذكاء الاصطناعي والذاكرة، واستدعاء الوظائف باستخدام اللغة الطبيعية أو الإضافات البرمجية، وقوالب الحث، والمزيد.
- **الاستفادة من الأدوات التعاونية**: تصميم وكلاء بأدوار ومهام محددة، مما يمكنهم من اختبار وتحسين سير العمل التعاوني.
- **التعلم في الوقت الفعلي**: تنفيذ حلقات تغذية راجعة حيث يتعلم الوكلاء من التفاعلات ويضبطون سلوكهم ديناميكيًا.

### استخدام المكونات المعيارية

تقدم حزم تطوير البرامج مثل إطار عمل وكيل مايكروسوفت مكونات جاهزة مثل موصلات الذكاء الاصطناعي، وتعريفات الأدوات، وإدارة الوكلاء.

**كيف يمكن للفرق استخدام هذه**: يمكن للفرق تجميع هذه المكونات بسرعة لإنشاء نموذج أولي وظيفي بدون البدء من الصفر، مما يسمح بالتجربة السريعة والتكرار.

**كيف يعمل ذلك عمليًا**: يمكنك استخدام محلل جاهز لاستخراج المعلومات من مدخلات المستخدم، ووحدة ذاكرة لتخزين واسترجاع البيانات، ومولد حث للتفاعل مع المستخدمين، كل ذلك بدون الحاجة إلى بناء هذه المكونات من الصفر.

**كود مثال**. لننظر إلى مثال يبين كيفية استخدام إطار عمل وكيل مايكروسوفت مع `FoundryChatClient` لجعل النموذج يرد على مدخلات المستخدم مع استدعاء الأدوات:

``` python
# مثال إطار عمل Microsoft Agent باستخدام بايثون

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
    # المخرج المثال: تم حجز رحلتك إلى نيويورك في 1 يناير 2025 بنجاح. رحلة آمنة! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ما تراه من هذا المثال هو كيفية استفادتك من محلل جاهز لاستخراج معلومات رئيسية من مدخلات المستخدم، مثل الأصل، والوجهة، وتاريخ طلب حجز رحلة. هذه الطريقة المعيارية تتيح لك التركيز على المنطق العام.

### الاستفادة من الأدوات التعاونية

تسهل أُطُر مثل إطار عمل وكيل مايكروسوفت إنشاء وكلاء متعددين يمكنهم العمل معًا.

**كيف يمكن للفرق استخدام هذه**: يمكن للفرق تصميم وكلاء بأدوار ومهام محددة، مما يمكنهم من اختبار وتحسين سير العمل التعاوني وتحسين كفاءة النظام بشكل عام.

**كيف يعمل عمليًا**: يمكنك إنشاء فريق من الوكلاء حيث لكل وكيل وظيفة متخصصة، مثل استرجاع البيانات، أو التحليل، أو اتخاذ القرار. يمكن لهؤلاء الوكلاء التواصل وتبادل المعلومات لتحقيق هدف مشترك، مثل الإجابة على استفسار مستخدم أو إتمام مهمة.

**كود مثال (إطار عمل وكيل مايكروسوفت)**:

```python
# إنشاء وكلاء متعددين يعملون معًا باستخدام إطار عمل وكيل مايكروسوفت

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# وكيل استرداد البيانات
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

ما تراه في الكود السابق هو كيف يمكنك إنشاء مهمة تشمل عمل عدة وكلاء معًا لتحليل بيانات. كل وكيل يؤدي وظيفة محددة، ويتم تنفيذ المهمة عبر تنسيق عمل الوكلاء لتحقيق النتيجة المرجوة. من خلال إنشاء وكلاء مخصصين بأدوار متخصصة، يمكنك تحسين كفاءة وأداء المهمة.

### التعلم في الوقت الحقيقي

توفر الأُطُر المتقدمة قدرات لفهم السياق والتكيف في الوقت الفعلي.

**كيف يمكن للفرق استخدام هذه**: يمكن للفرق تنفيذ حلقات تغذية راجعة حيث يتعلم الوكلاء من التفاعلات ويضبطون سلوكهم ديناميكيًا، مما يؤدي إلى تحسين وترقية مستمرة للقدرات.

**كيف يعمل عمليًا**: يمكن للوكلاء تحليل ملاحظات المستخدم، وبيانات البيئة، ونتائج المهام لتحديث قاعدة معرفتهم، وضبط خوارزميات اتخاذ القرار، وتحسين الأداء مع مرور الوقت. هذه العملية التعلمية التكرارية تُمكن الوكلاء من التكيف مع الظروف المتغيرة وتفضيلات المستخدم، مما يعزز فعالية النظام بشكل عام.

## ما هي الاختلافات بين إطار عمل وكيل مايكروسوفت وخدمة وكيل Microsoft Foundry؟

هناك العديد من الطرق لمقارنة هذه النهج، ولكن لننظر إلى بعض الاختلافات الرئيسية من حيث التصميم، والقدرات، والحالات الاستخدام المستهدفة:

## إطار عمل وكيل مايكروسوفت (MAF)

يوفر إطار عمل وكيل مايكروسوفت حزمة تطوير برمجيات مبسطة لبناء وكلاء الذكاء الاصطناعي باستخدام `FoundryChatClient`. يتيح للمطورين إنشاء وكلاء يستفيدون من نماذج Azure OpenAI مع استدعاء الأدوات المدمجة، وإدارة المحادثات، وأمان على مستوى المؤسسات من خلال هوية Azure.

**حالات الاستخدام**: بناء وكلاء ذكاء اصطناعي جاهزين للإنتاج مع استخدام الأدوات، وسير عمل متعدد الخطوات، وسيناريوهات التكامل المؤسسي.

إليك بعض المفاهيم الأساسية الهامة لإطار عمل وكيل مايكروسوفت:

- **الوكلاء**. يتم إنشاء الوكيل عبر `FoundryChatClient` ويتم تكوينه باسم، وتعليمات، وأدوات. يمكن للوكيل:
  - **معالجة رسائل المستخدم** وتوليد الردود باستخدام نماذج Azure OpenAI.
  - **استدعاء الأدوات** تلقائيًا استنادًا إلى سياق المحادثة.
  - **الحفاظ على حالة المحادثة** عبر عدة تفاعلات.

  هذا مقطع كود يوضح كيفية إنشاء وكيل:

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

- **الأدوات**. يدعم الإطار تعريف الأدوات كدوال بايثون يمكن للوكيل استدعاؤها تلقائيًا. تُسجل الأدوات عند إنشاء الوكيل:

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

- **تنسيق الوكلاء المتعددين**. يمكنك إنشاء وكلاء متعددين بتخصصات مختلفة وتنسيق عملهم:

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

- **التكامل مع هوية Azure**. يستخدم الإطار `AzureCliCredential` (أو `DefaultAzureCredential`) للمصادقة الآمنة بدون مفاتيح، مما يلغي الحاجة لإدارة مفاتيح API مباشرة.

## خدمة وكيل Microsoft Foundry

خدمة وكيل Microsoft Foundry هي إضافة أحدث، تم الإعلان عنها في Microsoft Ignite 2024. تتيح تطوير ونشر وكلاء الذكاء الاصطناعي مع نماذج أكثر مرونة، مثل استدعاء مباشرة لنماذج LLM مفتوحة المصدر مثل Llama 3، Mistral، و Cohere.

توفر خدمة وكيل Microsoft Foundry آليات أمان مؤسسية قوية وطرق تخزين بيانات مناسبة للتطبيقات المؤسسية.

تعمل الخدمة بشكل متكامل مع إطار عمل وكيل مايكروسوفت لبناء ونشر الوكلاء.

هذه الخدمة حالياً في مرحلة العرض العام وتدعم بايثون وC# لبناء الوكلاء.

باستخدام حزمة تطوير بايثون لخدمة وكيل Microsoft Foundry، يمكننا إنشاء وكيل بأداة معرفة من قبل المستخدم:

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
        model="gpt-5-mini",
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

تحتوي خدمة وكيل Microsoft Foundry على المفاهيم الأساسية التالية:

- **الوكيل**. تتكامل خدمة وكيل Microsoft Foundry مع Microsoft Foundry. داخل Microsoft Foundry، يعمل وكيل الذكاء الاصطناعي كـ "خدمة مصغرة ذكية" يمكن استخدامها للإجابة على الأسئلة (RAG)، أداء الإجراءات، أو أتمتة سير العمل بالكامل. يتم تحقيق ذلك من خلال دمج قوة نماذج الذكاء الاصطناعي التوليدية مع أدوات تسمح له بالوصول إلى مصادر البيانات الحقيقية والتفاعل معها. إليك مثالاً على وكيل:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    في هذا المثال، يتم إنشاء وكيل باستخدام النموذج `gpt-5-mini`، واسم `my-agent`، وتعليمات `أنت وكيل مساعد`. الوكيل مجهز بالأدوات والموارد لأداء مهام تفسير الكود.

- **الخيط والرسائل**. الخيط هو مفهوم مهم آخر. يمثل محادثة أو تفاعل بين وكيل ومستخدم. يمكن استخدام الخيوط لتعقب تقدم المحادثة، تخزين معلومات السياق، وإدارة حالة التفاعل. إليك مثال على خيط:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # اطلب من الوكيل أداء العمل على الموضوع
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # جلب وتسجيل كل الرسائل لرؤية رد الوكيل
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    في الكود السابق، تم إنشاء خيط. بعد ذلك، يتم إرسال رسالة إلى الخيط. عبر استدعاء `create_and_process_run`، يُطلب من الوكيل أداء عمل على الخيط. أخيرًا، يتم جلب الرسائل وتسجيلها لرؤية رد الوكيل. تشير الرسائل إلى تقدم المحادثة بين المستخدم والوكيل. من المهم أيضًا فهم أن الرسائل يمكن أن تكون من أنواع مختلفة مثل نص، صورة، أو ملف، أي أن عمل الوكلاء قد نتج عنه مثلاً صورة أو رد نصي. كمطور، يمكنك استخدام هذه المعلومات لمزيد من المعالجة أو لعرضها للمستخدم.

- **التكامل مع إطار عمل وكيل مايكروسوفت**. تعمل خدمة وكيل Microsoft Foundry بسلاسة مع إطار عمل وكيل مايكروسوفت، مما يعني أنه يمكنك بناء الوكلاء باستخدام `FoundryChatClient` ونشرهم عبر خدمة الوكيل لسيناريوهات الإنتاج.

**حالات الاستخدام**: تم تصميم خدمة وكيل Microsoft Foundry للتطبيقات المؤسسية التي تتطلب نشر وكلاء ذكاء اصطناعي آمن، وقابل للتوسع، ومرن.

## ما الفرق بين هذه النهج؟
 
قد يبدو أن هناك تداخلًا، لكن هناك بعض الفروقات الرئيسية من حيث التصميم، القدرات، وحالات الاستخدام المستهدفة:
 
- **إطار عمل وكيل مايكروسوفت (MAF)**: هو حزمة تطوير إنتاجية لبناء وكلاء الذكاء الاصطناعي. يوفر واجهة برمجة تطبيقات مبسطة لإنشاء وكلاء مع استدعاء الأدوات، إدارة المحادثات، وتكامل هوية Azure.
- **خدمة وكيل Microsoft Foundry**: هي منصة وخدمة نشر في Microsoft Foundry للوكلاء. توفر اتصالات مدمجة مع خدمات مثل Azure OpenAI، Azure AI Search، Bing Search، وتنفيذ الكود.
 
لا تزال غير متأكد أيهما تختار؟

### حالات الاستخدام
 
دعنا نرى إذا كان بإمكاننا مساعدتك من خلال استعراض بعض حالات الاستخدام الشائعة:
 
> س: أبني تطبيقات وكلاء الذكاء الاصطناعي للإنتاج وأريد البدء بسرعة
>

>ج: إطار عمل وكيل مايكروسوفت خيار ممتاز. يوفر واجهة برمجة تطبيقات سهلة وبايثونية عبر `FoundryChatClient` تتيح لك تعريف الوكلاء بالأدوات والتعليمات في بضعة أسطر من الكود.

>س: أحتاج إلى نشر على مستوى المؤسسات مع تكاملات Azure مثل البحث وتنفيذ الأكواد
>
> ج: خدمة وكيل Microsoft Foundry هي الأنسب. هي خدمة منصة توفر إمكانات مدمجة لنماذج متعددة، Azure AI Search، Bing Search، وAzure Functions. تجعل من السهل بناء وكلائك في بوابة Foundry ونشرهم على نطاق واسع.
 
> س: ما زلت مرتبكًا، فقط امنحني خيارًا واحدًا
>
> ج: ابدأ بإطار عمل وكيل مايكروسوفت لبناء وكلائك، ثم استخدم خدمة وكيل Microsoft Foundry عندما تحتاج إلى نشرهم وتوسيعهم في الإنتاج. هذا الأسلوب يسمح لك بالتكرار السريع في منطق الوكيل مع وجود مسار واضح للنشر المؤسسي.
 
لنلخص الفروقات الرئيسية في جدول:

| الإطار | التركيز | المفاهيم الأساسية | حالات الاستخدام |
| --- | --- | --- | --- |
| إطار عمل وكيل مايكروسوفت | حزمة تطوير وكلاء مبسطة مع استدعاء الأدوات | الوكلاء، الأدوات، هوية Azure | بناء وكلاء AI، استخدام الأدوات، سير العمل متعدد الخطوات |
| خدمة وكيل Microsoft Foundry | نماذج مرنة، أمان المؤسسات، توليد الأكواد، استدعاء الأدوات | التمركزية، التعاون، تنظيم العمليات | نشر وكلاء AI آمن، قابل للتوسع ومرن |

## هل يمكنني دمج أدوات نظام Azure الحالي مباشرة، أم أحتاج إلى حلول مستقلة؟


الجواب هو نعم، يمكنك دمج أدوات بيئة Azure الحالية الخاصة بك مباشرة مع خدمة وكيل Microsoft Foundry خاصةً، حيث تم بناؤها للعمل بسلاسة مع خدمات Azure الأخرى. على سبيل المثال، يمكنك دمج Bing و Azure AI Search و Azure Functions. هناك أيضًا تكامل عميق مع Microsoft Foundry.

إطار عمل وكيل Microsoft يتكامل أيضًا مع خدمات Azure من خلال `FoundryChatClient` وهوية Azure، مما يتيح لك استدعاء خدمات Azure مباشرة من أدوات الوكيل الخاصة بك.

## أمثلة الشيفرات

- بايثون: [إطار عمل الوكيل (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- بايثون: [إطار عمل الوكيل (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [إطار عمل الوكيل](./code_samples/02-dotnet-agent-framework.md)

## هل لديك المزيد من الأسئلة حول أطر عمل الوكلاء الذكية؟

انضم إلى [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) للقاء متعلمين آخرين، وحضور ساعات العمل والإجابة على أسئلتك حول وكلاء الذكاء الاصطناعي.

## المراجع

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">خدمة وكيل Azure</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">إطار عمل وكيل Microsoft - استجابات Azure OpenAI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">خدمة وكيل Microsoft Foundry</a>

## الدرس السابق

[مقدمة في وكلاء الذكاء الاصطناعي وحالات استخدام الوكلاء](../01-intro-to-ai-agents/README.md)

## الدرس التالي

[فهم أنماط تصميم الوكيل](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->