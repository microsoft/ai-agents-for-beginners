# Microsoft Agent Framework Workflow वापरून मल्टी-एजंट अॅप्लिकेशन्स तयार करणे

ही ट्यूटोरियल तुम्हाला Microsoft Agent Framework वापरून मल्टी-एजंट अॅप्लिकेशन्स समजून घेण्यास आणि तयार करण्यास मार्गदर्शन करेल. आपण मल्टी-एजंट सिस्टीम्सच्या मुख्य संकल्पनांचा अभ्यास करू, फ्रेमवर्कच्या Workflow घटकाच्या आर्किटेक्चरमध्ये डोकावू आणि Python आणि .NET मध्ये विविध वर्कफ्लो पॅटर्नसाठी व्यावहारिक उदाहरणे पाहू.

## 1\. मल्टी-एजंट सिस्टीम्स समजून घेणे

AI Agent हा एक प्रणाली आहे जो मानक Large Language Model (LLM) च्या क्षमतेच्या पलीकडे जातो. तो आपले वातावरण समजतो, निर्णय घेतो आणि विशिष्ट उद्दिष्टे साध्य करण्यासाठी कृती करतो. मल्टी-एजंट सिस्टीममध्ये अनेक एजंट्स एकत्र काम करतात जे एकट्या एजंटसाठी कठीण किंवा अशक्य असलेल्या समस्येचे निराकरण करतात.

### सामान्य अनुप्रयोग परिस्थिती

  * **जटिल समस्या सोडवणे**: मोठ्या कार्याचे (उदा., कंपनी-व्यापी कार्यक्रमाचे नियोजन) छोटे उपकार्यांमध्ये विभाजन करणे, जे विशेष एजंट्सद्वारे हाताळले जाते (उदा., बजेट एजंट, लॉजिस्टिक्स एजंट, मार्केटिंग एजंट).
  * **व्हर्च्युअल सहाय्यक**: एक प्राथमिक सहाय्यक एजंट शेड्यूलिंग, संशोधन आणि बुकिंगसारख्या कार्यांसाठी इतर विशेष एजंट्सना काम सोपवतो.
  * **स्वयंचलित सामग्री निर्मिती**: एक वर्कफ्लो जिथे एक एजंट सामग्री तयार करतो, दुसरा त्याची अचूकता आणि टोनसाठी पुनरावलोकन करतो, आणि तिसरा ती प्रकाशित करतो.

### मल्टी-एजंट पॅटर्न्स

मल्टी-एजंट सिस्टीम्स विविध पॅटर्न्समध्ये आयोजित केल्या जाऊ शकतात, ज्यामुळे त्यांचे परस्परसंवाद ठरतो:

  * **क्रमिक**: एजंट्स पूर्वनिर्धारित क्रमाने काम करतात, जसे असेंब्ली लाइनमध्ये. एका एजंटचे आउटपुट पुढील एजंटसाठी इनपुट बनते.
  * **सहकालिक**: एजंट्स कार्याच्या वेगवेगळ्या भागांवर एकाच वेळी काम करतात आणि त्यांच्या निकालांचा शेवटी एकत्रितपणे उपयोग केला जातो.
  * **शर्तीसंबंधी**: वर्कफ्लो एजंटच्या आउटपुटवर आधारित वेगवेगळ्या मार्गांचे अनुसरण करते, जसे if-then-else विधान.

## 2\. Microsoft Agent Framework Workflow आर्किटेक्चर

Agent Framework चा वर्कफ्लो सिस्टम हा एक प्रगत ऑर्केस्ट्रेशन इंजिन आहे जो अनेक एजंट्समधील जटिल परस्परसंवाद व्यवस्थापित करण्यासाठी डिझाइन केलेला आहे. तो [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf) वर आधारित ग्राफ-आधारित आर्किटेक्चरवर तयार केला आहे, जिथे प्रक्रिया "supersteps" नावाच्या समक्रमित टप्प्यांमध्ये होते.

### मुख्य घटक

आर्किटेक्चर तीन मुख्य भागांमध्ये विभागलेले आहे:

1.  **Executors**: हे मूलभूत प्रक्रिया युनिट्स आहेत. आमच्या उदाहरणांमध्ये, `Agent` हा एक प्रकारचा executor आहे. प्रत्येक executor कडे अनेक संदेश हँडलर्स असतात जे प्राप्त झालेल्या संदेशाच्या प्रकारावर आधारित स्वयंचलितपणे सक्रिय होतात.
2.  **Edges**: हे executors दरम्यान संदेश जाण्याचा मार्ग परिभाषित करतात. Edges कडे अटी असू शकतात, ज्यामुळे वर्कफ्लो ग्राफमधून माहितीचे डायनॅमिक रूटिंग शक्य होते.
3.  **Workflow**: हा घटक संपूर्ण प्रक्रिया ऑर्केस्ट्रेट करतो, executors, edges आणि एकूण कार्यप्रवाह व्यवस्थापित करतो. तो संदेश योग्य क्रमाने प्रक्रिया होण्याची खात्री करतो आणि निरीक्षणासाठी इव्हेंट्स प्रवाहित करतो.

*वर्कफ्लो सिस्टमच्या मुख्य घटकांचे चित्र.*

ही रचना क्रमिक साखळ्या, समांतर प्रक्रियेसाठी fan-out/fan-in, आणि शर्तीसंबंधी प्रवाहासाठी switch-case लॉजिक यासारख्या मूलभूत पॅटर्न्स वापरून मजबूत आणि स्केलेबल अॅप्लिकेशन्स तयार करण्यास अनुमती देते.

## 3\. व्यावहारिक उदाहरणे आणि कोड विश्लेषण

आता, फ्रेमवर्क वापरून विविध वर्कफ्लो पॅटर्न्स कसे अंमलात आणायचे ते पाहू. प्रत्येक उदाहरणासाठी Python आणि .NET कोड पाहू.

### केस 1: मूलभूत क्रमिक वर्कफ्लो

हा सर्वात सोपा पॅटर्न आहे, जिथे एका एजंटचे आउटपुट थेट दुसऱ्याला दिले जाते. आमच्या परिस्थितीत एक हॉटेल `FrontDesk` एजंट प्रवासाची शिफारस करतो, जी नंतर `Concierge` एजंट पुनरावलोकन करतो.

*मूलभूत FrontDesk -> Concierge वर्कफ्लोचे चित्र.*

#### परिस्थिती पार्श्वभूमी

एक प्रवासी पॅरिसमध्ये शिफारस विचारतो.

1.  `FrontDesk` एजंट, जो संक्षिप्ततेसाठी डिझाइन केलेला आहे, Louvre Museum ला भेट देण्याची शिफारस करतो.
2.  `Concierge` एजंट, जो प्रामाणिक अनुभवांना प्राधान्य देतो, ही शिफारस प्राप्त करतो. तो शिफारस पुनरावलोकन करतो आणि अधिक स्थानिक, कमी पर्यटकांसाठी पर्याय सुचवतो.

#### Python अंमलबजावणी विश्लेषण

Python उदाहरणात, आम्ही प्रथम दोन एजंट्स परिभाषित आणि तयार करतो, प्रत्येकाला विशिष्ट सूचना देऊन.

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

यानंतर, `WorkflowBuilder` वापरून ग्राफ तयार केला जातो. `front_desk_agent` प्रारंभ बिंदू म्हणून सेट केला जातो आणि त्याच्या आउटपुटला `reviewer_agent` शी जोडण्यासाठी एक edge तयार केला जातो.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

शेवटी, वर्कफ्लो प्रारंभिक वापरकर्ता प्रॉम्प्टसह चालवला जातो.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) अंमलबजावणी विश्लेषण

.NET अंमलबजावणी खूप समान तर्क अनुसरण करते. प्रथम, एजंट्सच्या नावांसाठी आणि सूचनांसाठी constants परिभाषित केल्या जातात.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

एजंट्स `OpenAIClient` वापरून तयार केले जातात आणि नंतर `WorkflowBuilder` क्रमिक प्रवाह परिभाषित करतो, `frontDeskAgent` पासून `reviewerAgent` पर्यंत edge जोडतो.

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

वर्कफ्लो नंतर वापरकर्त्याच्या संदेशासह चालवला जातो आणि निकाल प्रवाहित केला जातो.

### केस 2: मल्टी-स्टेप क्रमिक वर्कफ्लो

हा पॅटर्न मूलभूत क्रमिकतेला अधिक एजंट्ससह विस्तारित करतो. हे प्रक्रियेसाठी आदर्श आहे ज्याला अनेक टप्प्यांमध्ये सुधारणा किंवा परिवर्तन आवश्यक आहे.

#### परिस्थिती पार्श्वभूमी

एक वापरकर्ता लिव्हिंग रूमचा फोटो देतो आणि फर्निचर कोट विचारतो.

1.  **Sales-Agent**: प्रतिमेतील फर्निचर आयटम्स ओळखतो आणि यादी तयार करतो.
2.  **Price-Agent**: आयटम्सच्या यादीवर आधारित बजेट, मध्यम श्रेणी, आणि प्रीमियम पर्यायांसह तपशीलवार किंमत ब्रेकडाउन प्रदान करतो.
3.  **Quote-Agent**: किंमतीच्या यादीला प्राप्त करतो आणि Markdown मध्ये औपचारिक कोट दस्तऐवज तयार करतो.

*Sales -> Price -> Quote वर्कफ्लोचे चित्र.*

#### Python अंमलबजावणी विश्लेषण

तीन एजंट्स परिभाषित केले जातात, प्रत्येकाला विशेष भूमिका दिली जाते. वर्कफ्लो `add_edge` वापरून साखळी तयार करतो: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

इनपुट एक `ChatMessage` आहे ज्यामध्ये मजकूर आणि प्रतिमेचा URI समाविष्ट आहे. फ्रेमवर्क प्रत्येक एजंटचे आउटपुट पुढील एजंटला पास करते, जोपर्यंत अंतिम कोट तयार होत नाही.

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

#### .NET (C#) अंमलबजावणी विश्लेषण

.NET उदाहरण Python आवृत्तीचे प्रतिबिंबित करते. तीन एजंट्स (`salesagent`, `priceagent`, `quoteagent`) तयार केले जातात. `WorkflowBuilder` त्यांना क्रमिकपणे जोडतो.

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

वापरकर्त्याचा संदेश प्रतिमेचा डेटा (bytes स्वरूपात) आणि मजकूर प्रॉम्प्टसह तयार केला जातो. `InProcessExecution.StreamAsync` पद्धत वर्कफ्लो सुरू करते आणि अंतिम आउटपुट प्रवाहातून कॅप्चर केला जातो.

### केस 3: सहकालिक वर्कफ्लो

हा पॅटर्न वापरला जातो जेव्हा कार्ये एकाच वेळी पूर्ण केली जाऊ शकतात, वेळ वाचवण्यासाठी. यात "fan-out" अनेक एजंट्सकडे आणि "fan-in" निकाल एकत्रित करण्यासाठी समाविष्ट आहे.

#### परिस्थिती पार्श्वभूमी

एक वापरकर्ता सिएटलला प्रवासाचे नियोजन विचारतो.

1.  **Dispatcher (Fan-Out)**: वापरकर्त्याच्या विनंतीला एकाच वेळी दोन एजंट्सकडे पाठवले जाते.
2.  **Researcher-Agent**: सिएटलमध्ये डिसेंबरमध्ये प्रवासासाठी आकर्षणे, हवामान, आणि महत्त्वाच्या गोष्टींचा शोध घेतो.
3.  **Plan-Agent**: स्वतंत्रपणे तपशीलवार दिवस-वार प्रवासाचा कार्यक्रम तयार करतो.
4.  **Aggregator (Fan-In)**: संशोधक आणि नियोजकाचे आउटपुट एकत्रित केले जाते आणि अंतिम निकाल म्हणून सादर केले जाते.

*सहकालिक Researcher आणि Planner वर्कफ्लोचे चित्र.*

#### Python अंमलबजावणी विश्लेषण

`ConcurrentBuilder` हा पॅटर्न तयार करणे सुलभ करतो. तुम्ही सहभागी एजंट्सची यादी देताच, बिल्डर आवश्यक fan-out आणि fan-in लॉजिक स्वयंचलितपणे तयार करतो.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

फ्रेमवर्क सुनिश्चित करते की `research_agent` आणि `plan_agent` समांतरपणे कार्य करतात आणि त्यांचे अंतिम आउटपुट यादीत एकत्रित केले जाते.

#### .NET (C#) अंमलबजावणी विश्लेषण

.NET मध्ये, या पॅटर्नसाठी अधिक स्पष्ट परिभाषा आवश्यक आहे. कस्टम executors (`ConcurrentStartExecutor` आणि `ConcurrentAggregationExecutor`) fan-out आणि fan-in लॉजिक हाताळण्यासाठी तयार केले जातात.

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

`WorkflowBuilder` नंतर `AddFanOutEdge` आणि `AddFanInEdge` वापरून ग्राफ तयार करतो, या कस्टम executors आणि एजंट्ससह.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### केस 4: शर्तीसंबंधी वर्कफ्लो

शर्तीसंबंधी वर्कफ्लो शाखा लॉजिक सादर करतो, ज्यामुळे प्रणालीला मध्यवर्ती निकालांवर आधारित वेगवेगळ्या मार्गांचा अवलंब करता येतो.

#### परिस्थिती पार्श्वभूमी

हा वर्कफ्लो तांत्रिक ट्यूटोरियल तयार करणे आणि प्रकाशित करणे स्वयंचलित करतो.

1.  **Evangelist-Agent**: दिलेल्या रूपरेषा आणि URLs वर आधारित ट्यूटोरियलचा मसुदा तयार करतो.
2.  **ContentReviewer-Agent**: मसुद्याचे पुनरावलोकन करतो. तो तपासतो की शब्दसंख्या 200 शब्दांपेक्षा जास्त आहे का.
3.  **शर्तीसंबंधी शाखा**:
      * **जर मंजूर (`Yes`)**: वर्कफ्लो `Publisher-Agent` कडे पुढे जातो.
      * **जर नाकारले (`No`)**: वर्कफ्लो थांबतो आणि नकाराचे कारण आउटपुट करतो.
4.  **Publisher-Agent**: मसुदा मंजूर झाल्यास, हा एजंट सामग्री Markdown फाइलमध्ये सेव्ह करतो.

#### Python अंमलबजावणी विश्लेषण

या उदाहरणात, `select_targets` नावाचा कस्टम फंक्शन शर्तीसंबंधी लॉजिक अंमलात आणण्यासाठी वापरला जातो. हे फंक्शन `add_multi_selection_edge_group` ला दिले जाते आणि `review_result` क्षेत्रावर आधारित वर्कफ्लो निर्देशित करते.

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

कस्टम executors जसे `to_reviewer_result` एजंट्सच्या JSON आउटपुटचे विश्लेषण करण्यासाठी वापरले जातात आणि त्यांना strongly-typed objects मध्ये रूपांतरित करतात, ज्याचा निवड फंक्शन तपास करू शकतो.

#### .NET (C#) अंमलबजावणी विश्लेषण

.NET आवृत्ती समान दृष्टिकोन वापरते ज्यामध्ये शर्ती फंक्शन आहे. `Func<object?, bool>` परिभाषित केले जाते जे `ReviewResult` ऑब्जेक्टच्या `Result` प्रॉपर्टी तपासते.

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

`AddEdge` पद्धतीचा `condition` पॅरामीटर `WorkflowBuilder` ला शाखा मार्ग तयार करण्यास अनुमती देतो. वर्कफ्लो फक्त `publishExecutor` कडे edge अनुसरण करतो जर `GetCondition(expectedResult: "Yes")` true परत करते. अन्यथा, तो `sendReviewerExecutor` च्या मार्गावर जातो.

## निष्कर्ष

Microsoft Agent Framework Workflow मल्टी-एजंट सिस्टीम्स ऑर्केस्ट्रेट करण्यासाठी एक मजबूत आणि लवचिक पाया प्रदान करते. त्याच्या ग्राफ-आधारित आर्किटेक्चर आणि मुख्य घटकांचा लाभ घेऊन, विकसक जटिल वर्कफ्लो Python आणि .NET मध्ये डिझाइन आणि अंमलात आणू शकतात. तुमच्या अॅप्लिकेशनला साध्या क्रमिक प्रक्रियेसाठी, समांतर अंमलबजावणीसाठी किंवा डायनॅमिक शर्तीसंबंधी लॉजिकसाठी आवश्यकता असो, फ्रेमवर्क शक्तिशाली, स्केलेबल आणि प्रकार-सुरक्षित AI-सक्षम सोल्यूशन्स तयार करण्यासाठी साधने प्रदान करते.

---

**अस्वीकरण**:  
हा दस्तऐवज [Co-op Translator](https://github.com/Azure/co-op-translator) या एआय भाषांतर सेवेचा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर केल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.