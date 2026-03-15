[![استكشاف أُطر وكلاء الذكاء الاصطناعي](../../../translated_images/ar/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(انقر الصورة أعلاه لمشاهدة فيديو هذا الدرس)_

# استكشاف أُطر وكلاء الذكاء الاصطناعي

أطر وكلاء الذكاء الاصطناعي هي منصات برمجية مصممة لتبسيط إنشاء ونشر وإدارة وكلاء الذكاء الاصطناعي. توفر هذه الأطر للمطورين مكونات جاهزة، وتجريدات، وأدوات تُسرّع تطوير أنظمة الذكاء الاصطناعي المعقدة.

تساعد هذه الأُطر المطورين على التركيز على الجوانب الفريدة لتطبيقاتهم من خلال توفير نهج موحّد للتعامل مع التحديات الشائعة في تطوير وكلاء الذكاء الاصطناعي. إنها تعزز القابلية للتوسع، والوصولية، والكفاءة في بناء أنظمة الذكاء الاصطناعي.

## مقدمة 

ستغطي هذه الدرس:

- ما هي أُطر وكلاء الذكاء الاصطناعي وماذا تسمح للمطورين بتحقيقه؟
- كيف يمكن للفرق استخدام هذه الأُطر لنموذج أولي سريع، وتكرار، وتحسين قدرات الوكيل؟
- ما الفرق بين الأُطر والأدوات التي أنشأتها مايكروسوفت (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">خدمة Azure AI Agent</a> و <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">إطار وكلاء مايكروسوفت</a>)؟
- هل يمكنني دمج أدواتي الحالية في نظام Azure مباشرة، أم أحتاج إلى حلول مستقلة؟
- ما هي خدمة Azure AI Agents وكيف تساعدني؟

## أهداف التعلم

تهدف هذه الدرسة لمساعدتك في فهم:

- دور أُطر وكلاء الذكاء الاصطناعي في تطوير الذكاء الاصطناعي.
- كيفية الاستفادة من أُطر وكلاء الذكاء الاصطناعي لبناء وكلاء أذكياء.
- القدرات الرئيسية التي تتيحها أُطر وكلاء الذكاء الاصطناعي.
- الاختلافات بين إطار وكلاء مايكروسوفت وخدمة Azure AI Agent.

## ما هي أُطر وكلاء الذكاء الاصطناعي وماذا تمكن المطورين من فعله؟

يمكن لأُطر الذكاء الاصطناعي التقليدية مساعدتك في دمج الذكاء الاصطناعي في تطبيقاتك وتحسين هذه التطبيقات بالطرق التالية:

- **التخصيص**: يمكن للذكاء الاصطناعي تحليل سلوك وتفضيلات المستخدم لتقديم توصيات ومحتوى وتجارب مُخصّصة.
مثال: خدمات البث مثل Netflix تستخدم الذكاء الاصطناعي لاقتراح أفلام وبرامج بناءً على سجل المشاهدة، مما يعزز تفاعل المستخدم ورضاه.
- **الأتمتة والكفاءة**: يمكن للذكاء الاصطناعي أتمتة المهام المتكررة، تبسيط سير العمل، وتحسين الكفاءة التشغيلية.
مثال: تطبيقات خدمة العملاء تستخدم روبوتات محادثة مدعومة بالذكاء الاصطناعي للتعامل مع الاستفسارات الشائعة، مما يقلل أوقات الاستجابة ويتيح للوكلاء البشر التعامل مع القضايا الأكثر تعقيدًا.
- **تحسين تجربة المستخدم**: يمكن للذكاء الاصطناعي تحسين تجربة المستخدم العامة من خلال تقديم ميزات ذكية مثل التعرف على الصوت، ومعالجة اللغة الطبيعية، والنص التنبؤي.
مثال: المساعدون الافتراضيون مثل Siri وGoogle Assistant يستخدمون الذكاء الاصطناعي لفهم الأوامر الصوتية والرد عليها، مما يسهل على المستخدمين التفاعل مع أجهزتهم.

### كل ذلك يبدو رائعًا، فلماذا نحتاج إلى إطار وكلاء الذكاء الاصطناعي؟

تمثل أُطر وكلاء الذكاء الاصطناعي شيئًا أكثر من مجرد أُطر الذكاء الاصطناعي التقليدية. فهي مصممة لتمكين إنشاء وكلاء أذكياء يمكنهم التفاعل مع المستخدمين، ووكلاء آخرين، والبيئة لتحقيق أهداف محددة. يمكن لهؤلاء الوكلاء إظهار سلوك ذاتي، اتخاذ قرارات، والتكيف مع الظروف المتغيرة. لنلقِ نظرة على بعض القدرات الرئيسية التي تتيحها أُطر وكلاء الذكاء الاصطناعي:

- **تعاون وتنسيق الوكلاء**: تمكّن من إنشاء عدة وكلاء ذكاء اصطناعي يمكنهم العمل معًا، التواصل، والتنسيق لحل مهام معقدة.
- **أتمتة وإدارة المهام**: توفر آليات لأتمتة سير عمل متعدد الخطوات، تفويض المهام، وإدارة المهام الديناميكية بين الوكلاء.
- **الفهم السياقي والتكيف**: تزود الوكلاء بقدرة فهم السياق، التكيف مع البيئات المتغيرة، واتخاذ قرارات بناءً على معلومات في الوقت الفعلي.

خلاصة القول، تسمح الوكلاء لك بفعل المزيد، والارتقاء بالأتمتة إلى المستوى التالي، وإنشاء أنظمة أكثر ذكاءً يمكنها التكيف والتعلم من بيئتها.

## كيف تنشئ نموذجًا أوليًا بسرعة، وتكرر، وتحسن قدرات الوكيل؟

هذا مجال يتطور بسرعة، لكن هناك بعض الأشياء المشتركة عبر معظم أُطر وكلاء الذكاء الاصطناعي التي يمكن أن تساعدك في إنشاء نموذج أولي سريع وتكراره مثل المكونات المعيارية، أدوات التعاون، والتعلم في الوقت الحقيقي. لنغص في هذه النقاط:

- **استخدم مكونات معيارية**: توفر حزم تطوير البرمجيات مكونات جاهزة مثل موصلات الذكاء الاصطناعي والذاكرة، استدعاء الدوال باستخدام اللغة الطبيعية أو إضافات الكود، قوالب الموجهات، والمزيد.
- **استفد من أدوات التعاون**: صمّم وكلاء بأدوار ومهام محددة، مما يتيح لهم اختبار وتحسين سير العمل التعاوني.
- **تعلم في الوقت الحقيقي**: نفّذ حلقات تغذية راجعة حيث يتعلم الوكلاء من التفاعلات ويُعدِّلون سلوكهم ديناميكيًا.

### استخدم مكونات معيارية

توفر حزم مثل إطار وكلاء مايكروسوفت مكونات جاهزة مثل موصلات الذكاء الاصطناعي، تعريفات الأدوات، وإدارة الوكلاء.

**كيف يمكن للفرق استخدام هذه**: يمكن للفرق تجميع هذه المكونات بسرعة لإنشاء نموذج أولي وظيفي دون البدء من الصفر، مما يتيح تجارب سريعة وتكرارًا متواصلًا.

**كيف تعمل في الممارسة**: يمكنك استخدام محلل مسبق البناء لاستخراج المعلومات من مدخلات المستخدم، ووحدة ذاكرة لتخزين واسترداد البيانات، ومولد موجهات للتفاعل مع المستخدمين، كل ذلك دون الحاجة لبناء هذه المكونات من الصفر.

**مثال على الكود**. لننظر إلى مثال يوضح كيفية استخدام إطار وكلاء مايكروسوفت مع `AzureAIProjectAgentProvider` لجعل النموذج يستجيب لمدخلات المستخدم مع استدعاء الأدوات:

``` python
# مثال على إطار عمل العميل من مايكروسوفت باستخدام بايثون

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# تعريف دالة أداة نموذجية لحجز السفر
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # مثال على الإخراج: تم حجز رحلتك إلى نيويورك في 1 يناير 2025 بنجاح. رحلة آمنة! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

ما يمكنك رؤيته من هذا المثال هو كيف يمكنك الاستفادة من محلل مسبق البناء لاستخراج المعلومات الرئيسية من مدخلات المستخدم، مثل أصل الرحلة، وجهتها، وتاريخ طلب حجز الرحلة. يتيح لك هذا النهج المعياري التركيز على المنطق عالي المستوى.

### استفد من أدوات التعاون

تسهّل أُطر مثل إطار وكلاء مايكروسوفت إنشاء عدة وكلاء يمكنهم العمل معًا.

**كيف يمكن للفرق استخدام هذه**: يمكن للفرق تصميم وكلاء بأدوار ومهام محددة، مما يتيح لهم اختبار وتحسين سير العمل التعاوني وتحسين كفاءة النظام بشكل عام.

**كيف تعمل في الممارسة**: يمكنك إنشاء فريق من الوكلاء حيث يمتلك كل وكيل وظيفة متخصصة، مثل استرداد البيانات، التحليل، أو اتخاذ القرار. يمكن لهؤلاء الوكلاء التواصل ومشاركة المعلومات لتحقيق هدف مشترك، مثل الإجابة على استفسار مستخدم أو إكمال مهمة.

**مثال على الكود (إطار وكلاء مايكروسوفت)**:

```python
# إنشاء عدة وكلاء يعملون معًا باستخدام إطار عمل وكيل مايكروسوفت

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# وكيل استرجاع البيانات
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# وكيل تحليل البيانات
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# تشغيل الوكلاء بالتسلسل على مهمة
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

ما تراه في الكود السابق هو كيف يمكنك إنشاء مهمة تتضمن عدة وكلاء يعملون معًا لتحليل البيانات. يقوم كل وكيل بوظيفة محددة، وتُنفّذ المهمة من خلال تنسيق عمل الوكلاء لتحقيق النتيجة المرجوة. من خلال إنشاء وكلاء مخصصين بأدوار متخصصة، يمكنك تحسين كفاءة وأداء المهام.

### التعلم في الوقت الحقيقي

توفر الأُطر المتقدمة قدرات لفهم السياق في الوقت الحقيقي والتكيف.

**كيف يمكن للفرق استخدام هذه**: يمكن للفرق تنفيذ حلقات تغذية راجعة حيث يتعلم الوكلاء من التفاعلات ويُعدِّلون سلوكهم ديناميكيًا، مما يؤدي إلى تحسين مستمر وصقل للقدرات.

**كيف تعمل في الممارسة**: يمكن للوكلاء تحليل ملاحظات المستخدم، بيانات البيئة، ونتائج المهام لتحديث قاعدة معارفهم، ضبط خوارزميات اتخاذ القرار، وتحسين الأداء بمرور الوقت. تتيح عملية التعلم التكرارية هذه للوكلاء التكيف مع الظروف المتغيرة وتفضيلات المستخدمين، مما يعزز فعالية النظام الشاملة.

## ما الفرق بين إطار وكلاء مايكروسوفت وخدمة Azure AI Agent؟

هناك طرق عديدة لمقارنة هذه الأساليب، لكن لننظر إلى بعض الاختلافات الرئيسية من حيث التصميم، والقدرات، وحالات الاستخدام المستهدفة:

## إطار وكلاء مايكروسوفت (MAF)

يوفر إطار وكلاء مايكروسوفت حزمة SDK مبسّطة لبناء وكلاء الذكاء الاصطناعي باستخدام `AzureAIProjectAgentProvider`. يمكّن المطورين من إنشاء وكلاء يستفيدون من نماذج Azure OpenAI مع استدعاء أدوات مدمج، إدارة المحادثات، وأمان بمستوى المؤسسات عبر هوية Azure.

**حالات الاستخدام**: بناء وكلاء ذكاء اصطناعي جاهزين للإنتاج مع استخدام الأدوات، سير عمل متعدد الخطوات، وسيناريوهات تكامل مؤسسي.

فيما يلي بعض المفاهيم الأساسية الهامة في إطار وكلاء مايكروسوفت:

- **الوكلاء**. يتم إنشاء الوكيل عبر `AzureAIProjectAgentProvider` وتكوينه باسم، تعليمات، وأدوات. يمكن للوكيل:
  - **معالجة رسائل المستخدم** وتوليد الاستجابات باستخدام نماذج Azure OpenAI.
  - **استدعاء الأدوات** تلقائيًا بناءً على سياق المحادثة.
  - **الحفاظ على حالة المحادثة** عبر تفاعلات متعددة.

  فيما يلي مقطع كود يوضح كيفية إنشاء وكيل:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **الأدوات**. يدعم الإطار تعريف الأدوات كدوال Python يمكن للوكيل استدعاؤها تلقائيًا. تُسجَّل الأدوات عند إنشاء الوكيل:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **تنسيق تعدد الوكلاء**. يمكنك إنشاء عدة وكلاء بتخصصات مختلفة وتنسيق عملهم:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **تكامل هوية Azure**. يستخدم الإطار `AzureCliCredential` (أو `DefaultAzureCredential`) للمصادقة الآمنة بدون مفاتيح، مما يلغي الحاجة لإدارة مفاتيح API مباشرةً.

## خدمة Azure AI Agent

خدمة Azure AI Agent هي إضافة أحدث، تم تقديمها في Microsoft Ignite 2024. تتيح تطوير ونشر وكلاء الذكاء الاصطناعي بمرونة أكبر في اختيار النماذج، مثل استدعاء نماذج مفتوحة المصدر مباشرةً مثل Llama 3 وMistral وCohere.

توفر خدمة Azure AI Agent آليات أمان وتخزين بيانات أقوى للمؤسسات، مما يجعلها مناسبة لتطبيقات المؤسسات.

تعمل مباشرةً مع إطار وكلاء مايكروسوفت لبناء ونشر الوكلاء.

هذه الخدمة حاليًا في المعاينة العامة وتدعم Python وC# لبناء الوكلاء.

باستخدام حزمة Python SDK الخاصة بخدمة Azure AI Agent، يمكننا إنشاء وكيل بأداة يعرفها المستخدم:

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
        model="gpt-4o-mini",
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

### مفاهيم أساسية

لخدمة Azure AI Agent المفاهيم الأساسية التالية:

- **الوكيل**. تندمج خدمة Azure AI Agent مع Microsoft Foundry. ضمن AI Foundry، يعمل الوكيل كخدمة مصغرة "ذكية" يمكن استخدامها للإجابة على الأسئلة (RAG)، أداء إجراءات، أو أتمتة سير العمل بالكامل. يحقق ذلك من خلال دمج قوة نماذج التوليد مع أدوات تسمح له بالوصول إلى مصادر البيانات الحقيقية والتفاعل معها. فيما يلي مثال على وكيل:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    في هذا المثال، يُنشأ وكيل بالنموذج `gpt-4o-mini`، وبالاسم `my-agent`، والتعليمات `You are helpful agent`. يتم تجهيز الوكيل بأدوات وموارد لأداء مهام تفسير الكود.

- **الخيط والرسائل**. الخيط مفهوم مهم آخر. يمثل الخيط محادثة أو تفاعلًا بين وكيل ومستخدم. يمكن استخدام الخيوط لتتبع تقدم المحادثة، تخزين معلومات السياق، وإدارة حالة التفاعل. فيما يلي مثال على خيط:

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

    في الكود السابق، تم إنشاء خيط. بعد ذلك، تُرسل رسالة إلى الخيط. من خلال استدعاء `create_and_process_run` يُطلب من الوكيل أداء عمل على الخيط. وأخيرًا، تُسترجع الرسائل وتُسجل لرؤية استجابة الوكيل. تشير الرسائل إلى تقدم المحادثة بين المستخدم والوكيل. من المهم أيضًا فهم أن الرسائل يمكن أن تكون من أنواع مختلفة مثل نص، صورة، أو ملف، أي أن عمل الوكلاء قد ينتج عنه، على سبيل المثال، صورة أو استجابة نصية. كمطور، يمكنك بعد ذلك استخدام هذه المعلومات لمعالجة الاستجابة أكثر أو عرضها على المستخدم.

- **التكامل مع إطار وكلاء مايكروسوفت**. تعمل خدمة Azure AI Agent بسلاسة مع إطار وكلاء مايكروسوفت، مما يعني أنه يمكنك بناء وكلاء باستخدام `AzureAIProjectAgentProvider` ونشرهم عبر خدمة الوكلاء لسيناريوهات الإنتاج.

**حالات الاستخدام**: تم تصميم خدمة Azure AI Agent لتطبيقات المؤسسات التي تتطلب نشر وكلاء ذكاء اصطناعي آمن، قابل للتوسع، ومرن.

## ما الفرق بين هذه النهج؟
 
يبدو أن هناك تداخلًا، لكن توجد بعض الاختلافات الرئيسية من حيث التصميم، والقدرات، وحالات الاستخدام المستهدفة:
 
- **إطار وكلاء مايكروسوفت (MAF)**: هو SDK جاهز للإنتاج لبناء وكلاء الذكاء الاصطناعي. يوفر واجهة برمجة تطبيقات مبسطة لإنشاء وكلاء مع استدعاء الأدوات، إدارة المحادثات، وتكامل هوية Azure.
- **خدمة Azure AI Agent**: هي منصة وخدمة نشر ضمن Azure Foundry للوكلاء. تقدم اتصالًا مدمجًا بخدمات مثل Azure OpenAI، Azure AI Search، Bing Search وتنفيذ الكود.
 
لا تزال غير متأكد أيهما تختار؟

### حالات الاستخدام
 
لنرَ إن كان بإمكاننا مساعدتك من خلال استعراض بعض حالات الاستخدام الشائعة:
 
> Q: أبني تطبيقات وكلاء ذكاء اصطناعي للإنتاج وأريد البدء بسرعة
>

>A: إطار وكلاء مايكروسوفت خيار ممتاز. يوفر واجهة برمجة بسيطة وبأسلوب Python عبر `AzureAIProjectAgentProvider` تتيح لك تعريف وكلاء بأدوات وتعليمات في بضعة أسطر من الكود.

>Q: أحتاج نشرًا بمستوى مؤسسي مع تكاملات Azure مثل Search وتنفيذ الكود
>
> A: خدمة Azure AI Agent هي الأنسب. إنها خدمة منصة توفر قدرات مدمجة لنماذج متعددة، Azure AI Search، Bing Search وAzure Functions. تجعل بناء وكلائك في بوابة Foundry ونشرهم على نطاق واسع أمرًا سهلاً.
 
> Q: ما زلت مرتبكًا، أعطني خيارًا واحدًا فقط
>
> A: ابدأ بإطار وكلاء مايكروسوفت لبناء وكلائك، ثم استخدم خدمة Azure AI Agent عندما تحتاج إلى نشرها وتوسيع نطاقها في الإنتاج. يتيح هذا النهج التكرار السريع على منطق وكيلك مع وجود مسار واضح لنشر مؤسسي.
 
لنلخص الاختلافات الرئيسية في جدول:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| إطار وكلاء مايكروسوفت | حزمة SDK مبسّطة للوكلاء مع استدعاء الأدوات | وكلاء، أدوات، هوية Azure | بناء وكلاء الذكاء الاصطناعي، استخدام الأدوات، سير عمل متعدد الخطوات |
| خدمة Azure AI Agent | نماذج مرنة، أمان مؤسسي، توليد الكود، استدعاء الأدوات | تجزئة، تعاون، تنسيق العمليات | نشر وكلاء الذكاء الاصطناعي الآمن والقابل للتوسع والمرن |

## هل يمكنني دمج أدواتي الحالية في نظام Azure مباشرة، أم أحتاج إلى حلول مستقلة؟
الإجابة هي نعم — يمكنك دمج أدوات منظومة Azure الحالية لديك مباشرةً مع Azure AI Agent Service، خاصةً لأنه بُني للعمل بسلاسة مع خدمات Azure الأخرى. على سبيل المثال، يمكنك دمج Bing وAzure AI Search وAzure Functions. هناك أيضًا تكامل عميق مع Microsoft Foundry.

يعمل Microsoft Agent Framework أيضًا على التكامل مع خدمات Azure عبر `AzureAIProjectAgentProvider` وهوية Azure، مما يتيح لك استدعاء خدمات Azure مباشرةً من أدوات الوكيل الخاصة بك.

## أمثلة الشيفرات

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## هل لديك المزيد من الأسئلة حول أُطر عمل وكلاء الذكاء الاصطناعي؟

انضم إلى [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) للقاء متعلمين آخرين، وحضور ساعات الاستشارة، والحصول على إجابات لأسئلتك حول وكلاء الذكاء الاصطناعي.

## المراجع

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## الدرس السابق

[مقدمة في وكلاء الذكاء الاصطناعي وحالات استخدامهم](../01-intro-to-ai-agents/README.md)

## الدرس التالي

[فهم أنماط التصميم الوكالية](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
إخلاء المسؤولية:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية Co-op Translator (https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. ينبغي اعتبار المستند الأصلي بلغته الأصلية المصدر المرجعي والموثوق. للمعلومات الهامة والحساسة، يُنصح بالاستعانة بترجمة بشرية محترفة. لا نتحمل أي مسؤولية عن أي سوء فهم أو تفسير ينتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->