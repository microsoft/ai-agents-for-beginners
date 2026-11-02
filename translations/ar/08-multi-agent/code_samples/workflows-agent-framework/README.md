# بناء تطبيقات متعددة الوكلاء باستخدام إطار عمل Microsoft Agent Workflow

سيرشدك هذا الدليل خلال فهم وبناء تطبيقات متعددة الوكلاء باستخدام إطار عمل Microsoft Agent. سوف نستكشف المفاهيم الأساسية لأنظمة الوكلاء المتعددين، نتعمق في هندسة مكون سير العمل للإطار، ونتابع أمثلة عملية في كل من بايثون و .NET لأنماط سير عمل مختلفة.

## 1\. فهم أنظمة الوكلاء المتعددين

الوكيل الذكي هو نظام يتجاوز قدرات نموذج اللغة الكبير العادي (LLM). يمكنه إدراك بيئته، اتخاذ القرارات، واتخاذ الإجراءات لتحقيق أهداف محددة. نظام الوكلاء المتعددين يتضمن عدة من هؤلاء الوكلاء يتعاونون لحل مشكلة ستكون صعبة أو مستحيلة على وكيل واحد التعامل معها بمفرده.

### السيناريوهات التطبيقية الشائعة

  * **حل المشكلات المعقدة**: تقسيم مهمة كبيرة (مثل، تخطيط حدث يشمل الشركة بأكملها) إلى مهام فرعية أصغر يتولاها وكلاء متخصصون (مثلاً، وكيل الميزانية، وكيل اللوجستيات، وكيل التسويق).
  * **المساعدون الافتراضيون**: وكيل مساعد رئيسي يفوض مهام مثل الجدولة، الأبحاث، والحجز إلى وكلاء متخصصين آخرين.
  * **إنشاء المحتوى التلقائي**: سير عمل حيث يقوم وكيل واحد بصياغة المحتوى، وآخر يراجعه من حيث الدقة والنبرة، وثالث ينشره.

### أنماط الوكلاء المتعددين

يمكن تنظيم أنظمة الوكلاء المتعددين في عدة أنماط، تحدد كيف تتفاعل فيما بينها:

  * **تسلسلي**: يعمل الوكلاء بترتيب محدد مسبقًا، مثل خط تجميع. مخرجات وكيل واحد تصبح مدخلات للآخر.
  * **متزامن**: يعمل الوكلاء بالتوازي على أجزاء مختلفة من المهمة، ويتم تجميع نتائجهم في النهاية.
  * **شرطي**: يتبع سير العمل مسارات مختلفة بناءً على مخرجات وكيل، مشابه لعبارة if-then-else.

## 2\. هندسة سير عمل إطار عمل Microsoft Agent

نظام سير العمل في إطار الوكيل هو محرك تنظيم متقدم مصمم لإدارة التفاعلات المعقدة بين عدة وكلاء. تم بناؤه على هندسة قائمة على الرسم البياني تستخدم [نموذج تنفيذ بأسلوب Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf)، حيث تتم المعالجة في خطوات متزامنة تسمى "supersteps".

### المكونات الأساسية

تتألف الهندسة من ثلاثة أجزاء رئيسية:

1.  **المنفذون (Executors)**: هذه هي الوحدات الأساسية للمعالجة. في أمثلتنا، `Agent` هو نوع من المنفذ. يمكن لكل منفذ أن يملك عدة معالجات للرسائل تُستدعى تلقائيًا بناءً على نوع الرسالة المستلمة.
2.  **الحواف (Edges)**: تحدد المسار الذي تسلكه الرسائل بين المنفذين. يمكن أن تحتوي الحواف على شروط تسمح بالتوجيه الديناميكي للمعلومات عبر رسم سير العمل.
3.  **سير العمل (Workflow)**: ينظم هذه العملية بأكملها، يدير المنفذين، الحواف، وتدفق التنفيذ العام. يضمن معالجة الرسائل بالترتيب الصحيح ويبث الأحداث للرصد.

*مخطط يوضح المكونات الأساسية لنظام سير العمل.*

تتيح هذه البنية بناء تطبيقات قوية وقابلة للتوسع باستخدام أنماط أساسية مثل سلاسل متتابعة، ونمط fan-out/fan-in للمعالجة المتوازية، ومنطق switch-case لتدفقات شرطية.

## 3\. أمثلة عملية وتحليل الكود

الآن، دعنا نستعرض كيفية تنفيذ أنماط سير العمل المختلفة باستخدام الإطار. سننظر في الكود الخاص بكلٍ من بايثون و .NET لكل مثال.

### الحالة 1: سير عمل تسلسلي أساسي

هذا هو أبسط نمط، حيث يتم تمرير مخرجات وكيل واحد مباشرة إلى آخر. سيناريو هذا المثال يتضمن وكيل `FrontDesk` في الفندق يقدم توصية سفر، ويتم مراجعتها بواسطة وكيل `Concierge`.

*مخطط سير العمل الأساسي FrontDesk -> Concierge.*

#### خلفية السيناريو

يطلب مسافر توصية في باريس.

1.  وكيل `FrontDesk`، المصمم ليكون مختصرًا، يقترح زيارة متحف اللوفر.
2.  وكيل `Concierge`، الذي يفضل التجارب الأصيلة، يستلم هذا الاقتراح. يراجعه ويقدم ملاحظات، مقترحًا بديلًا محليًا وأقل سياحية.

#### تحليل التنفيذ في بايثون

في مثال بايثون، نعرف وننشئ أولًا الوكيلين، كل منهما بتعليمات محددة.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# تحديد أدوار وتعليمات الوكيل
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# إنشاء نسخ من الوكيل
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

بعد ذلك، يستخدم `WorkflowBuilder` لبناء الرسم البياني. يتم تعيين `front_desk_agent` كنقطة البداية، ويتم إنشاء حافة لربط مخرجاته بالوagent `reviewer_agent`.

```python
# ٠١.برمجية-وكيل-بايثون-إطار-العمل-سير-العمل-نموذج-جي-اتش-الأساسي.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

وأخيرًا، يتم تنفيذ سير العمل باستخدام موجه المستخدم الابتدائي.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# يقوم run بتنفيذ سير العمل؛ تعيد get_outputs() نتيجة منفذ الإخراج.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### تحليل التنفيذ في .NET (C#)

تنفيذ .NET يتبع منطقًا مشابهًا للغاية. أولًا تُعرّف الثوابت لأسماء وتعليمات الوكلاء.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

يتم إنشاء الوكلاء باستخدام `AzureOpenAIClient` (واجهة استجابة Responses API)، ثم يحدد `WorkflowBuilder` التدفق التسلسلي بإضافة حافة من `frontDeskAgent` إلى `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

ثم يتم تشغيل سير العمل برسالة المستخدم، وتُبث النتائج مرة أخرى.

### الحالة 2: سير عمل تسلسلي متعدد الخطوات

هذا النمط يوسع التسلسل الأساسي ليشمل المزيد من الوكلاء. مثالي للعمليات التي تتطلب مراحل متعددة من التحسين أو التحويل.

#### خلفية السيناريو

يقدم المستخدم صورة لغرفة المعيشة ويطلب عرض أسعار للأثاث.

1.  **وكيل المبيعات**: يحدد قطع الأثاث في الصورة وينشئ قائمة.
2.  **وكيل الأسعار**: يأخذ القائمة ويوفر تفصيل للأسعار، يشمل خيارات الميزانية والمتوسطة والفاخرة.
3.  **وكيل العرض**: يستلم القائمة المُسعرّة وينسقها في وثيقة عرض رسمي بصيغة Markdown.

*مخطط سير العمل Sales -> Price -> Quote.*

#### تحليل التنفيذ في بايثون

تم تعريف ثلاثة وكلاء، كل منهم بدور متخصص. تم بناء سير العمل باستخدام `add_edge` لإنشاء سلسلة: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# إنشاء ثلاثة وكلاء متخصصين
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# بناء سير العمل التسلسلي
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

المدخل هو `ChatMessage` يتضمن نصًا ورابط الصورة. يتولى الإطار تمرير مخرجات كل وكيل إلى التالي بالتتابع حتى يتم إنشاء العرض النهائي.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# تحتوي رسالة المستخدم على نص وصورة معًا
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# شغّل سير العمل
events = await workflow.run(message)
```

#### تحليل التنفيذ في .NET (C#)

المثال في .NET يعكس النسخة من بايثون. يتم إنشاء ثلاثة وكلاء (`salesagent`، `priceagent`، `quoteagent`). يربط `WorkflowBuilder` بينهم تسلسليًا.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

يتم إنشاء رسالة المستخدم بكل من بيانات الصورة (كـ bytes) والنص. طريقة `InProcessExecution.RunStreamingAsync` تبدأ سير العمل، ويتم التقاط المخرجات النهائية من التدفق.

### الحالة 3: سير عمل متزامن

يُستخدم هذا النمط عند إمكانية تنفيذ المهام في آنٍ واحد لتوفير الوقت. يتضمن "التوزيع" إلى عدة وكلاء و"التجميع" لنتائجهم.

#### خلفية السيناريو

يطلب مستخدم تخطيط رحلة إلى سياتل.

1.  **الموزع (Fan-Out)**: يتم إرسال طلب المستخدم إلى وكيلين في نفس الوقت.
2.  **وكيل البحث**: يبحث عن المواقع السياحية، الطقس، والنقاط الأساسية لرحلة إلى سياتل في ديسمبر.
3.  **وكيل التخطيط**: ينشئ بشكل مستقل جدول سفر مفصل يومًا بيوم.
4.  **المجمع (Fan-In)**: تُجمع مخرجات كل من الباحث والمخطط وتُعرض معًا كنتيجة نهائية.

*مخطط سير عمل الباحث والمخطط المتزامن.*

#### تحليل التنفيذ في بايثون

يقوم `ConcurrentBuilder` بتبسيط إنشاء هذا النمط. كل ما عليك هو سرد الوكلاء المشاركين، ويقوم البناء تلقائيًا بإنشاء منطق "التوزيع" و"التجميع" اللازم.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# يقوم ConcurrentBuilder بإدارة منطق التفرع والتجميع
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# تشغيل سير العمل
events = await workflow.run("Plan a trip to Seattle in December")
```

يضمن الإطار تنفيذ `research_agent` و `plan_agent` بالتوازي، ويتم جمع مخرجاتهما النهائية في قائمة.

#### تحليل التنفيذ في .NET (C#)

في .NET، يتطلب هذا النمط تعريفًا أكثر وضوحًا. يتم إنشاء منفذين مخصصين (`ConcurrentStartExecutor` و `ConcurrentAggregationExecutor`) للتعامل مع منطق "التوزيع" و"التجميع".

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

ثم يستخدم `WorkflowBuilder` أساليب `AddFanOutEdge` و `AddFanInEdge` لبناء الرسم البياني مع هؤلاء المنفذين المخصصين والوكلاء.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### الحالة 4: سير عمل شرطي

تُدخل سير العمل الشرطي منطق التفرع، مما يسمح للنظام باتخاذ مسارات مختلفة بناءً على نتائج وسطية.

#### خلفية السيناريو

يقوم هذا سير العمل بأتمتة إنشاء ونشر درس تقني.

1.  **وكيل المبشر (Evangelist)**: يكتب مسودة الدرس بناءً على مخطط وروابط معطاة.
2.  **وكيل مراجعة المحتوى**: يراجع المسودة. يتحقق مما إذا كان عدد الكلمات يزيد عن 200 كلمة.
3.  **التفرع الشرطي**:
      * **إذا تم الموافقة (`نعم`)**: يتابع سير العمل إلى وكيل النشر.
      * **إذا تم الرفض (`لا`)**: يتوقف سير العمل ويُخرج سبب الرفض.
4.  **وكيل النشر**: إذا تم الموافقة على المسودة، يحفظ المحتوى في ملف Markdown.

#### تحليل التنفيذ في بايثون

يستخدم هذا المثال وظيفة مخصصة، `select_targets`، لتطبيق المنطق الشرطي. تُمرر هذه الوظيفة إلى `add_multi_selection_edge_group` وتوجه سير العمل بناءً على حقل `review_result` من مخرجات المراجع.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# هذه الدالة تحدد الخطوة التالية بناءً على نتيجة المراجعة
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # إذا تم الموافقة، تابع إلى منفذ 'save_draft'
        return [save_draft_id]
    else:
        # إذا تم الرفض، تابع إلى منفذ 'handle_review' للإبلاغ عن الفشل
        return [handle_review_id]

# يقوم منشئ سير العمل باستخدام دالة الاختيار للتوجيه
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # ينفذ الحافة متعددة الاختيارات المنطق الشرطي
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

تُستخدم منفذات مخصصة مثل `to_reviewer_result` لتحليل الإخراج JSON من الوكلاء وتحويله إلى كائنات ذات نوع قوي يمكن لدالة الاختيار فحصها.

#### تحليل التنفيذ في .NET (C#)

النسخة في .NET تستخدم نهجًا مشابهًا مع دالة شرطية. تُعرف `Func<object?, bool>` لفحص خاصية `Result` لكائن `ReviewResult`.

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

تسمح معلمة `condition` في طريقة `AddEdge` لـ `WorkflowBuilder` بإنشاء مسار تفرعي. يتبع سير العمل الحافة إلى `publishExecutor` فقط إذا كانت حالة `GetCondition(expectedResult: "Yes")` صحيحة. وإلا، يتبع المسار إلى `sendReviewerExecutor`.

## الخلاصة

يوفر سير عمل إطار Microsoft Agent أساسًا قويًا ومرنًا لتنظيم أنظمة متعددة الوكلاء معقدة. بالاستفادة من هندسته القائمة على الرسم البياني ومكوناته الأساسية، يمكن للمطورين تصميم وتنفيذ سير عمل متقدمة في كل من بايثون و .NET. سواء تطلب التطبيق معالجة تسلسلية بسيطة، تنفيذ متوازي، أو منطق شرطي ديناميكي، يوفر الإطار الأدوات لبناء حلول ذكاء اصطناعي قوية، قابلة للتوسع، وآمنة النوع.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->