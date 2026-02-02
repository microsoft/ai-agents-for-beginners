# Microsoft Agent Framework Workflow के साथ मल्टी-एजेंट एप्लिकेशन बनाना

यह ट्यूटोरियल आपको Microsoft Agent Framework का उपयोग करके मल्टी-एजेंट एप्लिकेशन को समझने और बनाने में मदद करेगा। हम मल्टी-एजेंट सिस्टम के मुख्य सिद्धांतों का अध्ययन करेंगे, फ्रेमवर्क के Workflow घटक की वास्तुकला में गहराई से जाएंगे, और Python और .NET में विभिन्न वर्कफ़्लो पैटर्न के व्यावहारिक उदाहरणों को देखेंगे।

## 1\. मल्टी-एजेंट सिस्टम को समझना

AI Agent एक ऐसा सिस्टम है जो एक सामान्य Large Language Model (LLM) की क्षमताओं से आगे बढ़ता है। यह अपने परिवेश को समझ सकता है, निर्णय ले सकता है, और विशिष्ट लक्ष्यों को प्राप्त करने के लिए कार्रवाई कर सकता है। मल्टी-एजेंट सिस्टम में कई एजेंट शामिल होते हैं जो एक साथ काम करते हैं ताकि किसी समस्या को हल किया जा सके, जिसे अकेले एक एजेंट द्वारा संभालना कठिन या असंभव हो।

### सामान्य एप्लिकेशन परिदृश्य

  * **जटिल समस्या समाधान**: एक बड़े कार्य (जैसे, कंपनी-व्यापी इवेंट की योजना बनाना) को छोटे उप-कार्य में विभाजित करना, जिन्हें विशेष एजेंट (जैसे, बजट एजेंट, लॉजिस्टिक्स एजेंट, मार्केटिंग एजेंट) द्वारा संभाला जाता है।
  * **वर्चुअल असिस्टेंट्स**: एक प्राथमिक सहायक एजेंट अन्य विशेष एजेंटों को कार्य सौंपता है, जैसे शेड्यूलिंग, रिसर्च, और बुकिंग।
  * **स्वचालित सामग्री निर्माण**: एक वर्कफ़्लो जिसमें एक एजेंट सामग्री का मसौदा तैयार करता है, दूसरा इसे सटीकता और टोन के लिए समीक्षा करता है, और तीसरा इसे प्रकाशित करता है।

### मल्टी-एजेंट पैटर्न

मल्टी-एजेंट सिस्टम को कई पैटर्न में व्यवस्थित किया जा सकता है, जो उनके इंटरैक्शन को निर्धारित करते हैं:

  * **Sequential**: एजेंट एक पूर्वनिर्धारित क्रम में काम करते हैं, जैसे असेंबली लाइन। एक एजेंट का आउटपुट अगले एजेंट के लिए इनपुट बन जाता है।
  * **Concurrent**: एजेंट एक कार्य के विभिन्न हिस्सों पर समानांतर में काम करते हैं, और उनके परिणाम अंत में एकत्रित किए जाते हैं।
  * **Conditional**: वर्कफ़्लो विभिन्न पथों का अनुसरण करता है, जो एजेंट के आउटपुट पर आधारित होता है, जैसे if-then-else स्टेटमेंट।

## 2\. Microsoft Agent Framework Workflow आर्किटेक्चर

Agent Framework का वर्कफ़्लो सिस्टम एक उन्नत ऑर्केस्ट्रेशन इंजन है, जिसे कई एजेंटों के बीच जटिल इंटरैक्शन को प्रबंधित करने के लिए डिज़ाइन किया गया है। यह एक ग्राफ-आधारित आर्किटेक्चर पर बनाया गया है जो [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf) का उपयोग करता है, जहां प्रोसेसिंग "supersteps" नामक सिंक्रोनाइज़ चरणों में होती है।

### मुख्य घटक

आर्किटेक्चर तीन मुख्य भागों से बना है:

1.  **Executors**: ये मूल प्रोसेसिंग यूनिट हैं। हमारे उदाहरणों में, `Agent` एक प्रकार का एक्सीक्यूटर है। प्रत्येक एक्सीक्यूटर में कई संदेश हैंडलर हो सकते हैं, जो प्राप्त संदेश के प्रकार के आधार पर स्वचालित रूप से सक्रिय होते हैं।
2.  **Edges**: ये परिभाषित करते हैं कि संदेश एक्सीक्यूटर के बीच कैसे यात्रा करते हैं। Edges में शर्तें हो सकती हैं, जो वर्कफ़्लो ग्राफ़ के माध्यम से जानकारी के डायनामिक रूटिंग की अनुमति देती हैं।
3.  **Workflow**: यह घटक पूरे प्रक्रिया का ऑर्केस्ट्रेशन करता है, एक्सीक्यूटर, एजेस, और समग्र निष्पादन प्रवाह का प्रबंधन करता है। यह सुनिश्चित करता है कि संदेश सही क्रम में प्रोसेस किए जाएं और ऑब्ज़र्वेबिलिटी के लिए इवेंट्स को स्ट्रीम करता है।

*वर्कफ़्लो सिस्टम के मुख्य घटकों को दर्शाने वाला एक चित्र।*

यह संरचना बुनियादी पैटर्न जैसे कि sequential chains, fan-out/fan-in (समानांतर प्रोसेसिंग के लिए), और switch-case logic (conditional flows के लिए) का उपयोग करके मजबूत और स्केलेबल एप्लिकेशन बनाने की अनुमति देती है।

## 3\. व्यावहारिक उदाहरण और कोड विश्लेषण

अब, हम फ्रेमवर्क का उपयोग करके विभिन्न वर्कफ़्लो पैटर्न को लागू करने के तरीके का पता लगाएंगे। हम प्रत्येक उदाहरण के लिए Python और .NET कोड देखेंगे।

### केस 1: बेसिक Sequential Workflow

यह सबसे सरल पैटर्न है, जहां एक एजेंट का आउटपुट सीधे दूसरे को पास किया जाता है। हमारा परिदृश्य एक होटल `FrontDesk` एजेंट को शामिल करता है जो यात्रा की सिफारिश करता है, जिसे फिर एक `Concierge` एजेंट द्वारा समीक्षा की जाती है।

*बेसिक FrontDesk -> Concierge वर्कफ़्लो का चित्र।*

#### परिदृश्य पृष्ठभूमि

एक यात्री पेरिस में सिफारिश मांगता है।

1.  `FrontDesk` एजेंट, जो संक्षिप्तता के लिए डिज़ाइन किया गया है, लौवर संग्रहालय का सुझाव देता है।
2.  `Concierge` एजेंट, जो प्रामाणिक अनुभवों को प्राथमिकता देता है, इस सुझाव को प्राप्त करता है। यह सिफारिश की समीक्षा करता है और एक अधिक स्थानीय, कम पर्यटक विकल्प सुझाता है।

#### Python कार्यान्वयन विश्लेषण

Python उदाहरण में, हम पहले दो एजेंटों को परिभाषित और बनाते हैं, प्रत्येक को विशिष्ट निर्देशों के साथ।

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

इसके बाद, `WorkflowBuilder` का उपयोग ग्राफ़ बनाने के लिए किया जाता है। `front_desk_agent` को प्रारंभिक बिंदु के रूप में सेट किया जाता है, और इसका आउटपुट `reviewer_agent` से जोड़ने के लिए एक edge बनाया जाता है।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

अंत में, वर्कफ़्लो को प्रारंभिक उपयोगकर्ता प्रॉम्प्ट के साथ निष्पादित किया जाता है।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) कार्यान्वयन विश्लेषण

.NET कार्यान्वयन बहुत समान तर्क का अनुसरण करता है। पहले, एजेंटों के नाम और निर्देशों के लिए constants परिभाषित किए जाते हैं।

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

एजेंटों को `OpenAIClient` का उपयोग करके बनाया जाता है, और फिर `WorkflowBuilder` sequential flow को परिभाषित करता है, `frontDeskAgent` से `reviewerAgent` तक edge जोड़कर।

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

वर्कफ़्लो को उपयोगकर्ता के संदेश के साथ चलाया जाता है, और परिणामों को स्ट्रीम किया जाता है।

### केस 2: Multi-Step Sequential Workflow

यह पैटर्न बेसिक सीक्वेंस को अधिक एजेंटों को शामिल करने के लिए विस्तारित करता है। यह उन प्रक्रियाओं के लिए आदर्श है जिन्हें कई चरणों में परिष्कृत या रूपांतरित करने की आवश्यकता होती है।

#### परिदृश्य पृष्ठभूमि

एक उपयोगकर्ता एक लिविंग रूम की छवि प्रदान करता है और फर्नीचर कोट का अनुरोध करता है।

1.  **Sales-Agent**: छवि में फर्नीचर आइटम की पहचान करता है और एक सूची बनाता है।
2.  **Price-Agent**: आइटम की सूची लेता है और बजट, मिड-रेंज, और प्रीमियम विकल्पों सहित विस्तृत मूल्य ब्रेकडाउन प्रदान करता है।
3.  **Quote-Agent**: मूल्य सूची प्राप्त करता है और इसे Markdown में एक औपचारिक कोट दस्तावेज़ में प्रारूपित करता है।

*Sales -> Price -> Quote वर्कफ़्लो का चित्र।*

#### Python कार्यान्वयन विश्लेषण

तीन एजेंट परिभाषित किए गए हैं, प्रत्येक एक विशेष भूमिका के साथ। वर्कफ़्लो को `add_edge` का उपयोग करके एक श्रृंखला बनाने के लिए बनाया गया है: `sales_agent` -> `price_agent` -> `quote_agent`।

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

इनपुट एक `ChatMessage` है जिसमें टेक्स्ट और छवि URI दोनों शामिल हैं। फ्रेमवर्क प्रत्येक एजेंट के आउटपुट को अगले एजेंट तक पास करने को संभालता है, जब तक कि अंतिम कोट उत्पन्न न हो जाए।

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

#### .NET (C#) कार्यान्वयन विश्लेषण

.NET उदाहरण Python संस्करण को दर्शाता है। तीन एजेंट (`salesagent`, `priceagent`, `quoteagent`) बनाए जाते हैं। `WorkflowBuilder` उन्हें क्रमिक रूप से जोड़ता है।

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

उपयोगकर्ता का संदेश छवि डेटा (bytes के रूप में) और टेक्स्ट प्रॉम्प्ट दोनों के साथ बनाया जाता है। `InProcessExecution.StreamAsync` विधि वर्कफ़्लो शुरू करती है, और अंतिम आउटपुट स्ट्रीम से कैप्चर किया जाता है।

### केस 3: Concurrent Workflow

यह पैटर्न तब उपयोग किया जाता है जब कार्यों को एक साथ पूरा किया जा सकता है ताकि समय बचाया जा सके। इसमें "fan-out" कई एजेंटों के लिए और "fan-in" परिणामों को एकत्रित करने के लिए शामिल है।

#### परिदृश्य पृष्ठभूमि

एक उपयोगकर्ता सिएटल की यात्रा की योजना बनाने के लिए कहता है।

1.  **Dispatcher (Fan-Out)**: उपयोगकर्ता का अनुरोध एक साथ दो एजेंटों को भेजा जाता है।
2.  **Researcher-Agent**: सिएटल में दिसंबर के लिए आकर्षण, मौसम, और प्रमुख विचारों पर शोध करता है।
3.  **Plan-Agent**: स्वतंत्र रूप से एक विस्तृत दिन-प्रतिदिन यात्रा कार्यक्रम बनाता है।
4.  **Aggregator (Fan-In)**: शोधकर्ता और योजनाकार दोनों के आउटपुट एकत्रित किए जाते हैं और अंतिम परिणाम के रूप में प्रस्तुत किए जाते हैं।

*Concurrent Researcher और Planner वर्कफ़्लो का चित्र।*

#### Python कार्यान्वयन विश्लेषण

`ConcurrentBuilder` इस पैटर्न को बनाने को सरल बनाता है। आप बस भाग लेने वाले एजेंटों को सूचीबद्ध करते हैं, और बिल्डर स्वचालित रूप से आवश्यक fan-out और fan-in लॉजिक बनाता है।

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

फ्रेमवर्क सुनिश्चित करता है कि `research_agent` और `plan_agent` समानांतर में निष्पादित हों, और उनके अंतिम आउटपुट को एक सूची में एकत्रित किया जाए।

#### .NET (C#) कार्यान्वयन विश्लेषण

.NET में, इस पैटर्न को अधिक स्पष्ट परिभाषा की आवश्यकता होती है। कस्टम एक्सीक्यूटर (`ConcurrentStartExecutor` और `ConcurrentAggregationExecutor`) fan-out और fan-in लॉजिक को संभालने के लिए बनाए जाते हैं।

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

`WorkflowBuilder` फिर इन कस्टम एक्सीक्यूटर और एजेंटों के साथ ग्राफ़ बनाने के लिए `AddFanOutEdge` और `AddFanInEdge` का उपयोग करता है।

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### केस 4: Conditional Workflow

Conditional वर्कफ़्लो ब्रांचिंग लॉजिक को पेश करते हैं, जिससे सिस्टम intermediate परिणामों के आधार पर विभिन्न पथों को ले सकता है।

#### परिदृश्य पृष्ठभूमि

यह वर्कफ़्लो एक तकनीकी ट्यूटोरियल के निर्माण और प्रकाशन को स्वचालित करता है।

1.  **Evangelist-Agent**: दिए गए outline और URLs के आधार पर ट्यूटोरियल का मसौदा तैयार करता है।
2.  **ContentReviewer-Agent**: मसौदे की समीक्षा करता है। यह जांचता है कि शब्द संख्या 200 से अधिक है या नहीं।
3.  **Conditional Branch**:
      * **यदि स्वीकृत (`Yes`)**: वर्कफ़्लो `Publisher-Agent` पर आगे बढ़ता है।
      * **यदि अस्वीकृत (`No`)**: वर्कफ़्लो रुक जाता है और अस्वीकृति का कारण आउटपुट करता है।
4.  **Publisher-Agent**: यदि मसौदा स्वीकृत है, तो यह एजेंट सामग्री को Markdown फ़ाइल में सहेजता है।

#### Python कार्यान्वयन विश्लेषण

इस उदाहरण में, एक कस्टम फ़ंक्शन, `select_targets`, का उपयोग conditional लॉजिक को लागू करने के लिए किया जाता है। इस फ़ंक्शन को `add_multi_selection_edge_group` में पास किया जाता है और यह `review_result` फ़ील्ड के आधार पर वर्कफ़्लो को निर्देशित करता है।

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

कस्टम एक्सीक्यूटर जैसे `to_reviewer_result` का उपयोग एजेंटों के JSON आउटपुट को पार्स करने और इसे strongly-typed objects में बदलने के लिए किया जाता है, जिसे चयन फ़ंक्शन निरीक्षण कर सकता है।

#### .NET (C#) कार्यान्वयन विश्लेषण

.NET संस्करण एक समान दृष्टिकोण का उपयोग करता है जिसमें एक condition फ़ंक्शन होता है। एक `Func<object?, bool>` परिभाषित किया जाता है जो `ReviewResult` ऑब्जेक्ट की `Result` प्रॉपर्टी की जांच करता है।

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

`AddEdge` विधि का `condition` पैरामीटर `WorkflowBuilder` को एक ब्रांचिंग पथ बनाने की अनुमति देता है। वर्कफ़्लो केवल तब `publishExecutor` तक जाएगा जब condition `GetCondition(expectedResult: "Yes")` true लौटाएगा। अन्यथा, यह `sendReviewerExecutor` पथ का अनुसरण करेगा।

## निष्कर्ष

Microsoft Agent Framework Workflow जटिल, मल्टी-एजेंट सिस्टम को ऑर्केस्ट्रेट करने के लिए एक मजबूत और लचीला आधार प्रदान करता है। इसकी ग्राफ-आधारित आर्किटेक्चर और मुख्य घटकों का उपयोग करके, डेवलपर्स Python और .NET में परिष्कृत वर्कफ़्लो डिज़ाइन और लागू कर सकते हैं। चाहे आपका एप्लिकेशन सरल sequential प्रोसेसिंग, समानांतर निष्पादन, या डायनामिक conditional लॉजिक की आवश्यकता रखता हो, फ्रेमवर्क शक्तिशाली, स्केलेबल, और type-safe AI-संचालित समाधान बनाने के लिए उपकरण प्रदान करता है।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।