# بناء تطبيقات متعددة الوكلاء باستخدام إطار عمل Microsoft Agent Workflow

هذا الدليل سيرشدك لفهم وبناء تطبيقات متعددة الوكلاء باستخدام إطار عمل Microsoft Agent. سنستكشف المفاهيم الأساسية لأنظمة الوكلاء المتعددة، ونغوص في بنية مكون Workflow الخاص بالإطار، ونستعرض أمثلة عملية باستخدام Python و .NET لأنماط سير العمل المختلفة.

## 1. فهم أنظمة الوكلاء المتعددة

الوكيل الذكي هو نظام يتجاوز قدرات نموذج اللغة الكبير (LLM) التقليدي. يمكنه إدراك بيئته، واتخاذ القرارات، وتنفيذ الإجراءات لتحقيق أهداف محددة. نظام الوكلاء المتعددة يتضمن عدة وكلاء يتعاونون لحل مشكلة قد تكون صعبة أو مستحيلة على وكيل واحد التعامل معها بمفرده.

### سيناريوهات التطبيقات الشائعة

  * **حل المشكلات المعقدة**: تقسيم مهمة كبيرة (مثل تخطيط حدث على مستوى الشركة) إلى مهام فرعية يتم التعامل معها بواسطة وكلاء متخصصين (مثل وكيل الميزانية، وكيل اللوجستيات، وكيل التسويق).
  * **المساعدات الافتراضية**: وكيل مساعد رئيسي يقوم بتفويض مهام مثل الجدولة، البحث، والحجز إلى وكلاء متخصصين آخرين.
  * **إنشاء المحتوى الآلي**: سير عمل حيث يقوم وكيل بكتابة المحتوى، وآخر بمراجعته للتأكد من دقته ونبرته، وثالث بنشره.

### أنماط الوكلاء المتعددة

يمكن تنظيم أنظمة الوكلاء المتعددة في عدة أنماط تحدد كيفية تفاعلهم:

  * **تتابعي**: يعمل الوكلاء بترتيب محدد مسبقًا، مثل خط التجميع. يصبح ناتج وكيل واحد مدخلًا للوكيل التالي.
  * **متزامن**: يعمل الوكلاء بالتوازي على أجزاء مختلفة من المهمة، ويتم تجميع نتائجهم في النهاية.
  * **شرطي**: يتبع سير العمل مسارات مختلفة بناءً على ناتج وكيل معين، مشابه لبيان if-then-else.

## 2. بنية Workflow في إطار عمل Microsoft Agent

نظام سير العمل في إطار العمل هو محرك تنسيق متقدم مصمم لإدارة التفاعلات المعقدة بين الوكلاء المتعددين. يعتمد على بنية قائمة على الرسوم البيانية تستخدم [نموذج تنفيذ Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf)، حيث تتم المعالجة في خطوات متزامنة تُعرف باسم "supersteps".

### المكونات الأساسية

تتكون البنية من ثلاثة أجزاء رئيسية:

1. **المنفذون**: هم وحدات المعالجة الأساسية. في أمثلتنا، يعتبر `Agent` نوعًا من المنفذين. يمكن لكل منفذ أن يحتوي على عدة معالجات رسائل يتم استدعاؤها تلقائيًا بناءً على نوع الرسالة المستلمة.
2. **الحواف**: تحدد المسار الذي تسلكه الرسائل بين المنفذين. يمكن أن تحتوي الحواف على شروط، مما يسمح بتوجيه ديناميكي للمعلومات عبر الرسم البياني لسير العمل.
3. **سير العمل**: هذا المكون ينظم العملية بأكملها، ويدير المنفذين، والحواف، وتدفق التنفيذ العام. يضمن معالجة الرسائل بالترتيب الصحيح ويبث الأحداث للمراقبة.

*رسم بياني يوضح المكونات الأساسية لنظام سير العمل.*

تتيح هذه البنية إنشاء تطبيقات قوية وقابلة للتوسع باستخدام أنماط أساسية مثل السلاسل التتابعية، التوزيع والتجميع للمعالجة المتوازية، ومنطق التبديل للحالات الشرطية.

## 3. أمثلة عملية وتحليل الكود

الآن، دعونا نستكشف كيفية تنفيذ أنماط سير العمل المختلفة باستخدام الإطار. سنستعرض أمثلة الكود لكل من Python و .NET لكل نمط.

### الحالة 1: سير عمل تتابعي بسيط

هذا هو النمط الأبسط، حيث يتم تمرير ناتج وكيل مباشرة إلى وكيل آخر. السيناريو الخاص بنا يتضمن وكيل `FrontDesk` للفندق الذي يقدم توصية سفر، والتي يتم مراجعتها بعد ذلك بواسطة وكيل `Concierge`.

*رسم بياني لسير العمل الأساسي FrontDesk -> Concierge.*

#### خلفية السيناريو

يسأل مسافر عن توصية في باريس.

1. يقدم وكيل `FrontDesk`، المصمم للإيجاز، اقتراحًا بزيارة متحف اللوفر.
2. يتلقى وكيل `Concierge`، الذي يفضل التجارب الأصيلة، هذا الاقتراح. يقوم بمراجعة التوصية ويقدم ملاحظات، مقترحًا بديلاً أكثر محلية وأقل سياحية.

#### تحليل تنفيذ Python

في مثال Python، نقوم أولاً بتعريف وإنشاء الوكيلين، كل منهما بتعليمات محددة.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

بعد ذلك، يتم استخدام `WorkflowBuilder` لبناء الرسم البياني. يتم تعيين `front_desk_agent` كنقطة البداية، ويتم إنشاء حافة لربط ناتجه بـ `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

أخيرًا، يتم تنفيذ سير العمل مع المطالبة الأولية للمستخدم.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### تحليل تنفيذ .NET (C#)

يتبع تنفيذ .NET منطقًا مشابهًا جدًا. أولاً، يتم تعريف الثوابت لأسماء الوكلاء وتعليماتهم.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

يتم إنشاء الوكلاء باستخدام `OpenAIClient`، ثم يقوم `WorkflowBuilder` بتحديد التدفق التتابعي عن طريق إضافة حافة من `frontDeskAgent` إلى `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

يتم تشغيل سير العمل بعد ذلك مع رسالة المستخدم، ويتم بث النتائج مرة أخرى.

### الحالة 2: سير عمل تتابعي متعدد الخطوات

يمدد هذا النمط التسلسل الأساسي ليشمل المزيد من الوكلاء. إنه مثالي للعمليات التي تتطلب مراحل متعددة من التحسين أو التحويل.

#### خلفية السيناريو

يقدم مستخدم صورة لغرفة معيشة ويطلب عرض أسعار للأثاث.

1. **Sales-Agent**: يحدد عناصر الأثاث في الصورة ويُنشئ قائمة.
2. **Price-Agent**: يأخذ قائمة العناصر ويقدم تفصيلًا للأسعار، بما في ذلك الخيارات الاقتصادية والمتوسطة والفاخرة.
3. **Quote-Agent**: يتلقى القائمة المسعرة ويُنسقها في مستند عرض أسعار رسمي بصيغة Markdown.

*رسم بياني لسير العمل Sales -> Price -> Quote.*

#### تحليل تنفيذ Python

يتم تعريف ثلاثة وكلاء، كل منهم له دور متخصص. يتم بناء سير العمل باستخدام `add_edge` لإنشاء سلسلة: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

المدخل هو `ChatMessage` يتضمن النص ورابط الصورة. يتولى الإطار تمرير ناتج كل وكيل إلى التالي في التسلسل حتى يتم إنشاء عرض الأسعار النهائي.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### تحليل تنفيذ .NET (C#)

يعكس مثال .NET نسخة Python. يتم إنشاء ثلاثة وكلاء (`salesagent`, `priceagent`, `quoteagent`). يقوم `WorkflowBuilder` بربطهم بالتتابع.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

يتم إنشاء رسالة المستخدم مع بيانات الصورة (كبايت) والنص. يتم تشغيل سير العمل باستخدام `InProcessExecution.StreamAsync`، ويتم التقاط الناتج النهائي من البث.

### الحالة 3: سير عمل متزامن

يُستخدم هذا النمط عندما يمكن تنفيذ المهام في نفس الوقت لتوفير الوقت. يتضمن "توزيع" إلى عدة وكلاء و"تجميع" لتجميع النتائج.

#### خلفية السيناريو

يطلب مستخدم تخطيط رحلة إلى سياتل.

1. **Dispatcher (Fan-Out)**: يتم إرسال طلب المستخدم إلى وكيلين في نفس الوقت.
2. **Researcher-Agent**: يبحث عن المعالم السياحية، الطقس، والاعتبارات الرئيسية لرحلة إلى سياتل في ديسمبر.
3. **Plan-Agent**: يُنشئ بشكل مستقل خطة سفر مفصلة يومًا بيوم.
4. **Aggregator (Fan-In)**: يتم جمع نواتج الباحث والمخطط وتقديمها معًا كنتيجة نهائية.

*رسم بياني لسير العمل المتزامن Researcher و Planner.*

#### تحليل تنفيذ Python

يبسط `ConcurrentBuilder` إنشاء هذا النمط. تقوم ببساطة بإدراج الوكلاء المشاركين، ويقوم المنشئ تلقائيًا بإنشاء منطق التوزيع والتجميع اللازم.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

يضمن الإطار أن `research_agent` و `plan_agent` يعملان بالتوازي، ويتم جمع نواتجهما النهائية في قائمة.

#### تحليل تنفيذ .NET (C#)

في .NET، يتطلب هذا النمط تعريفًا أكثر وضوحًا. يتم إنشاء منفذين مخصصين (`ConcurrentStartExecutor` و `ConcurrentAggregationExecutor`) للتعامل مع منطق التوزيع والتجميع.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

ثم يستخدم `WorkflowBuilder` `AddFanOutEdge` و `AddFanInEdge` لبناء الرسم البياني مع هؤلاء المنفذين المخصصين والوكلاء.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### الحالة 4: سير عمل شرطي

تُدخل سير العمل الشرطي منطق التفرع، مما يسمح للنظام باتخاذ مسارات مختلفة بناءً على النتائج الوسيطة.

#### خلفية السيناريو

يقوم هذا سير العمل بأتمتة إنشاء ونشر دليل تقني.

1. **Evangelist-Agent**: يكتب مسودة الدليل بناءً على مخطط وروابط محددة.
2. **ContentReviewer-Agent**: يراجع المسودة. يتحقق مما إذا كان عدد الكلمات يتجاوز 200 كلمة.
3. **فرع شرطي**:
      * **إذا تمت الموافقة (`Yes`)**: يتقدم سير العمل إلى `Publisher-Agent`.
      * **إذا تم الرفض (`No`)**: يتوقف سير العمل ويُخرج سبب الرفض.
4. **Publisher-Agent**: إذا تمت الموافقة على المسودة، يقوم هذا الوكيل بحفظ المحتوى في ملف Markdown.

#### تحليل تنفيذ Python

يستخدم هذا المثال وظيفة مخصصة، `select_targets`، لتنفيذ المنطق الشرطي. يتم تمرير هذه الوظيفة إلى `add_multi_selection_edge_group` لتوجيه سير العمل بناءً على الحقل `review_result` من ناتج المراجع.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

يتم استخدام منفذين مخصصين مثل `to_reviewer_result` لتحليل الناتج JSON من الوكلاء وتحويله إلى كائنات ذات نوع قوي يمكن أن تفحصها وظيفة التحديد.

#### تحليل تنفيذ .NET (C#)

يستخدم إصدار .NET نهجًا مشابهًا مع وظيفة شرطية. يتم تعريف `Func<object?, bool>` للتحقق من خاصية `Result` لكائن `ReviewResult`.

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

يسمح معلمة `condition` في طريقة `AddEdge` لـ `WorkflowBuilder` بإنشاء مسار متفرع. يتبع سير العمل الحافة إلى `publishExecutor` فقط إذا كانت الوظيفة الشرطية `GetCondition(expectedResult: "Yes")` تُرجع true. خلاف ذلك، يتبع المسار إلى `sendReviewerExecutor`.

## الخاتمة

يوفر إطار عمل Microsoft Agent Workflow أساسًا قويًا ومرنًا لتنسيق أنظمة متعددة الوكلاء المعقدة. من خلال الاستفادة من بنيته القائمة على الرسوم البيانية ومكوناته الأساسية، يمكن للمطورين تصميم وتنفيذ سير عمل متقدم في كل من Python و .NET. سواء كان تطبيقك يتطلب معالجة تتابعية بسيطة، تنفيذًا متوازيًا، أو منطقًا شرطيًا ديناميكيًا، يوفر الإطار الأدوات اللازمة لبناء حلول قوية وقابلة للتوسع وآمنة تعتمد على الذكاء الاصطناعي.

---

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.