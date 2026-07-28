# मायक्रोसॉफ्ट एजंट फ्रेमवर्क वर्कफ्लो वापरून मल्टी-एजंट अ‍ॅप्लिकेशन्स तयार करणे

हा ट्यूटोरियल तुम्हाला मायक्रोसॉफ्ट एजंट फ्रेमवर्क वापरून मल्टी-एजंट अ‍ॅप्लिकेशन्स समजून घेणे आणि तयार करण्यास मार्गदर्शन करेल. आम्ही मल्टी-एजंट सिस्टीमच्या मुख्य संकल्पनांचा अभ्यास करू, फ्रेमवर्कच्या वर्कफ्लो घटकाची आर्किटेक्चर पाहू आणि विविध वर्कफ्लो पॅटर्नसाठी Python आणि .NET मध्ये व्यावहारिक उदाहरणे पाहू.

## 1\. मल्टी-एजंट सिस्टीम समजून घेणे

AI एजंट म्हणजे असा एक सिस्टीम जो सामान्य लार्ज लँग्वेज मॉडेलच्या (LLM) क्षमतांपेक्षा पुढे जातो. तो आपले वातावरण समजून घेऊ शकतो, निर्णय घेऊ शकतो, आणि विशिष्ट उद्दिष्टे साध्य करण्यासाठी कृती करू शकतो. मल्टी-एजंट सिस्टीममध्ये अनेक असे एजंट एकत्र काम करतात ज्यामुळे एखाद्या एका एजंटसाठी एकट्याने हाताळणे कठीण किंवा अशक्य असलेले प्रश्न सोडवले जातात.

### सामान्य अनुप्रयोग परिस्थिती

  * **संकुचित समस्या सोडवणे**: मोठा कार्य (उदा., कंपनीव्यापी कार्यक्रमाचे नियोजन) लहान उप-कार्यांत विभागणे आणि त्या उप-कार्यांवर तज्ञ एजंट (उदा., बजेट एजंट, लॉजिस्टिक्स एजंट, मार्केटिंग एजंट) काम करणे.
  * **वर्चुअल सहाय्यक**: एक मुख्य सहाय्यक एजंट कामांचे (जसे की नियोजन, संशोधन, आणि बुकिंग) इतर तज्ञ एजंटना सोपवणे.
  * **स्वयंचलित सामग्री तयार करणे**: एक वर्कफ्लो ज्यात एक एजंट सामग्री तयार करतो, दुसरा तपासत असतो आणि तिसरा प्रकाशित करतो.

### मल्टी-एजंट पॅटर्न्स

मल्टी-एजंट सिस्टीम वेगवेगळ्या पॅटर्नमध्ये आयोजित केल्या जाऊ शकतात, जे त्यांचं परस्परसंवाद कसा होतो हे ठरवतात:

  * **अनुक्रमिक**: एजंट ठरवलेल्या क्रमाने काम करतात, जसे असेंब्ली लाइनसारखे. एका एजंटचा आउटपुट पुढील एजंटसाठी इनपुट बनतो.
  * **सांघिक**: एजंट समान वेळी वेगवेगळ्या भागांवर काम करतात, आणि शेवटी त्यांचे परिणाम एकत्रित केले जातात.
  * **अटी-आधारित**: एजंटच्या आउटपुटवर आधारित वेगवेगळे मार्ग वर्कफ्लो फॉलो करतो, जसे if-then-else विधानात होते.

## 2\. मायक्रोसॉफ्ट एजंट फ्रेमवर्क वर्कफ्लो आर्किटेक्चर

एजंट फ्रेमवर्कचा वर्कफ्लो सिस्टीम हा एक प्रगत ऑर्केस्ट्रेशन इंजिन आहे ज्याचा उद्देश अनेक एजंटमधील क्लिष्ट परस्परसंवाद व्यवस्थापित करणे आहे. हे एक ग्राफ-आधारित आर्किटेक्चरवर आधारित आहे ज्यामध्ये [Pregel-शैलीचा एक्झिक्युशन मॉडेल](https://kowshik.github.io/JPregel/pregel_paper.pdf) वापरला जातो, जिथे प्रक्रिया "सुपरस्टेप्स" नावाच्या सिंक्रोनाइज़्ड टप्प्यांमध्ये होते.

### मुख्य तत्त्वे

आर्किटेक्चर मध्ये तीन मुख्य भाग असतात:

1.  **एक्झिक्यूटर**: हे मूलभूत प्रक्रिया युनिट असतात. आमच्या उदाहरणांमध्ये, `Agent` हा एक प्रकारचा एक्झिक्यूटर आहे. प्रत्येक एक्झिक्यूटरकडे एकाहून अधिक मेसेज हँडलर्स असू शकतात जे प्राप्त होणाऱ्या मेसेजच्या प्रकारावर आधारित आपोआप invoke होतात.
2.  **एजेस**: हे एक्झिक्यूटरदरम्यान मेसेज जाण्यासाठीचा मार्ग ठरवतात. एजेसवर अटी असू शकतात, ज्यामुळे वर्कफ्लो ग्राफमध्ये माहिती डायनॅमिक पद्धतीने मार्गक्रमण केली जाते.
3.  **वर्कफ्लो**: हा घटक संपूर्ण प्रक्रिया नियंत्रित करतो, एक्झिक्यूटर, एजेस, आणि संपूर्ण एक्झिक्युशन फ्लोचे व्यवस्थापन करतो. यामुळे मेसेजेस योग्य क्रमाने प्रक्रियेत येतात आणि निरीक्षणासाठी इव्हेंट्स प्रवाहित करतो.

*वर्कफ्लो सिस्टीमच्या मुख्य तत्त्वांचे एक चित्रण.*

ही रचना मजबूत आणि स्केलेबल अ‍ॅप्लिकेशन्स तयार करण्यास अनुमती देते जे अनुक्रमित साखळ्या, समानांतर प्रक्रिया करण्यासाठी फॅन-आऊट/फॅन-इन, आणि अटी-आधारित प्रवाहासाठी स्विच-केस लॉजिक सारख्या मूलभूत पॅटर्नवर आधारित असतात.

## 3\. व्यावहारिक उदाहरणे आणि कोड विश्लेषण

आता आपण फ्रेमवर्क वापरून विविध वर्कफ्लो पॅटर्न कसे अंमलात आणता येतात ते पाहूया. आम्ही प्रत्येक उदाहरणासाठी Python आणि .NET कोड दोन्ही तपासू.

### केस 1: बेसिक अनुक्रमिक वर्कफ्लो

हा सोपा पॅटर्न आहे, जिथे एका एजंटचा आउटपुट दुसऱ्या एजंटला थेट दिला जातो. आमच्या परिदृश्यात, एका हॉटेलचा `FrontDesk` एजंट ट्रॅव्हल शिफारस करतो, ज्याचं पुनरावलोकन `Concierge` एजंट करतो.

*मूलभूत FrontDesk -> Concierge वर्कफ्लोचे चित्र.*

#### परिस्थिती संदर्भ

एका प्रवाशाने पॅरिसमध्ये शिफारस मागितली आहे.

1.  `FrontDesk` एजंट, संक्षिप्त स्वरूपासाठी तयार, लूव्र संग्रहालयाला भेट देण्याची सूचना देते.
2.  `Concierge` एजंट, जो प्रामाणिक अनुभवांना प्राधान्य देतो, ही सूचना प्राप्त करतो. तो शिफारस तपासतो आणि अभिप्राय देतो, अधिक स्थानिक आणि कमी पर्यटकांना लोकप्रिय पर्याय सुचवतो.

#### Python अंमलबजावणी विश्लेषण

Python उदाहरणात, प्रथम दोन एजंट्स तयार केले जातात, प्रत्येक विशिष्ट सूचनांसह.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# एजंट भूमिका आणि सूचना परिभाषित करा
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# एजंट उदाहरणे तयार करा
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

नंतर `WorkflowBuilder` ग्राफ तयार करण्यासाठी वापरला जातो. `front_desk_agent` सुरुवातीचा बिंदू ठरतो, आणि त्याचा आउटपुट `reviewer_agent` शी जोडणारा एक एज तयार केला जातो.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

अखेरीस, सुरुवातीचा यूजर प्रॉम्प्ट सह वर्कफ्लो चालवला जातो.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run कार्यप्रवाह चालवते; get_outputs() आउटपुट कार्यान्वयनकर्त्याचा परिणाम परत करतो.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) अंमलबजावणी विश्लेषण

.NET अंमलबजावणी समान लॉजिक वापरते. प्रथम एजंटच्या नावांसाठी आणि सूचनांसाठी constants निर्धारित केले जातात.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

एजंट `AzureOpenAIClient` (Responses API) वापरून तयार केले जातात, आणि नंतर `WorkflowBuilder` अनुक्रमित प्रवाह `frontDeskAgent` पासून `reviewerAgent` पर्यंत एज जोडून तपासतो.

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

वर्कफ्लो यूजरचा मेसेज घेऊन चालवला जातो आणि परिणाम प्रवाहित केले जातात.

### केस 2: मल्टी-स्टेप अनुक्रमिक वर्कफ्लो

हा पॅटर्न मूलभूत साखळीला वाढवतो आणि अधिक एजंट सामील करतो. हा बहु-टप्प्यांत परिष्कृती किंवा रूपांतरण आवश्यक प्रक्रिये साठी योग्य आहे.

#### परिस्थिती संदर्भ

वापरकर्ता एका लिव्हिंग रूमची प्रतिमा प्रदान करतो आणि फर्निचरचा कोट मागतो.

1.  **सेल्स-एजंट**: प्रतिमेतले फर्निचर आयटम ओळखतो आणि यादी तयार करतो.
2.  **प्राइस-एजंट**: आयटमच्या यादीवर आधारित तपशीलवार किंमत पद्धत देतो, ज्यात बजेट, मध्यम श्रेणी आणि प्रीमियम पर्याय असतात.
3.  **कोट-एजंट**: किंमतीसह यादी प्राप्त करतो आणि Markdown मध्ये औपचारिक कोट डॉक्युमेंट तयार करतो.

*सेल्स -> प्राइस -> कोट वर्कफ्लोचे चित्रण.*

#### Python अंमलबजावणी विश्लेषण

तीन एजंट निर्धारीत केले आहेत, प्रत्येकाचे एक तज्ञ कार्य. वर्कफ्लो शेवटच्या कोट तयार होईपर्यंत साखळी तयार करण्यासाठी `add_edge` वापरून बनवलेला आहे: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# तीन खास एजंट तयार करा
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# अनुक्रमिक कार्यप्रवाह तयार करा
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

इनपुट म्हणजे एक `ChatMessage` आहे ज्यात टेक्स्ट आणि प्रतिमेचा URI दोन्ही आहेत. फ्रेमवर्क प्रत्येक एजंटचा आउटपुट पुढील एजंटकडे पास करतो.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# वापरकर्त्याच्या संदेशात मजकूर आणि एक प्रतिमा दोन्ही आहेत
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# कार्यप्रवाह चालवा
events = await workflow.run(message)
```

#### .NET (C\#) अंमलबजावणी विश्लेषण

.NET उदाहरण Python आवृत्ती प्रमाणेच आहे. तीन एजंट (`salesagent`, `priceagent`, `quoteagent`) तयार केले जातात. `WorkflowBuilder` त्यांना अनुक्रमाने जोडतो.

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

वापरकर्त्याचा मेसेज प्रतिमा डेटा (bytes स्वरूपात) आणि टेक्स्ट प्रॉम्प्टसह तयार केला जातो. `InProcessExecution.RunStreamingAsync` वर्कफ्लो सुरू करतो, आणि अंतिम आउटपुट स्ट्रीममधून घेतला जातो.

### केस 3: सांघिक वर्कफ्लो

हा पॅटर्न तेव्हा वापरला जातो जेव्हा कार्ये एकाच वेळी केली जाऊ शकतात ज्यामुळे वेळ वाचतो. यात अनेक एजंटना फॅन-आऊट होते आणि परिणाम एकत्र करणारा फॅन-इन असतो.

#### परिस्थिती संदर्भ

वापरकर्ता सिएटल येथे प्रवासाची योजना करतो.

1.  **डिस्पॅचर (फॅन-आऊट)**: वापरकर्त्याची विनंती दोन एजंटना एकाच वेळी पाठवली जाते.
2.  **रिसर्चर-एजंट**: सिएटलमध्ये डिसेंबरच्या प्रवासासाठी आकर्षणे, हवामान आणि मुख्य विचार संशोधन करतो.
3.  **प्लॅन-एजंट**: स्वतंत्रपणे तपशीलवार दिवसनिहाय प्रवास आराखडा तयार करतो.
4.  **अॅग्रीगेटर (फॅन-इन)**: रिसर्चर आणि प्लॅनरची आउटपुट एकत्र करून अंतिम परिणाम सादर करतो.

*सांघिक रिसर्चर आणि प्लॅनर वर्कफ्लोचे चित्रण.*

#### Python अंमलबजावणी विश्लेषण

`ConcurrentBuilder` या पॅटर्नची निर्मिती सोपी करतो. तुम्ही केवळ सहभागी एजंटची यादी द्याल, आणि बिल्डर आवश्यक फॅन-आऊट आणि फॅन-इन लॉजिक तयार करतो.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder फॅन-आउट/फॅन-इन लॉजिक हाताळतो
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# वर्कफ्लो चालवा
events = await workflow.run("Plan a trip to Seattle in December")
```

फ्रेमवर्क सुनिश्चित करतो की `research_agent` आणि `plan_agent` एकाच वेळी चालतील, आणि त्यांचे अंतिम परिणाम यादीत जमा होतील.

#### .NET (C\#) अंमलबजावणी विश्लेषण

.NET मध्ये हा पॅटर्न अधिक स्पष्ट परिभाषा मागतो. कस्टम एक्झिक्यूटर (`ConcurrentStartExecutor` आणि `ConcurrentAggregationExecutor`) फॅन-आऊट आणि फॅन-इन लॉजिक हाताळण्यासाठी तयार केले जातात.

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

नंतर `WorkflowBuilder` यांचा वापर करून `AddFanOutEdge` आणि `AddFanInEdge` कॉल करून ग्राफ तयार करतो, हे कस्टम एक्झिक्यूटर आणि एजंटसह.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### केस 4: अटी-आधारित वर्कफ्लो

अटी-आधारित वर्कफ्लो शाखा लॉजिक आणतात, ज्यामुळे सिस्टम मधल्या निकालांवर आधारित वेगवेगळे मार्ग घेऊ शकते.

#### परिस्थिती संदर्भ

हा वर्कफ्लो टेक्निकल ट्यूटोरियल तयार करणे आणि प्रकाशित करणे स्वयंचलित करतो.

1.  **ईव्हॅंजलिस्ट-एजंट**: दिलेल्या आराखडा आणि URL वरून ट्यूटोरियलचा मसुदा लिहितो.
2.  **कंटेंटरिव्ह्युअर-एजंट**: मसुदा तपासतो. तो शब्दसंख्या 200 पेक्षा जास्त आहे का ते तपासतो.
3.  **शाखा अटी**:
      * **मंजूर असल्यास (`होय`)**: वर्कफ्लो `Publisher-Agent` कडे पुढे वाढतो.
      * **नाकारल्यास (`नाही`)**: वर्कफ्लो थांबतो आणि नाकारण्याचे कारण देते.
4.  **प्रकाशक-एजंट**: मसुदा मंजूर झाल्यास, हा एजंट सामग्री Markdown फाईलमध्ये जतन करतो.

#### Python अंमलबजावणी विश्लेषण

या उदाहरणात कस्टम फंक्शन `select_targets` वापरून अटी-आधारित लॉजिक अमलात आणले जाते. हे फंक्शन `add_multi_selection_edge_group` ला दिले जाते आणि रिव्ह्युअरच्या आउटपुट मधील `review_result` फील्ड वरून वर्कफ्लो मार्गदर्शन करते.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ही फंक्शन पुनरावलोकन निकालानुसार पुढील पायरी ठरवते
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # मंजूर असल्यास, 'save_draft' कार्यान्वयकाकडे पुढे जा
        return [save_draft_id]
    else:
        # नाकारले असल्यास, अपयश नोंदवण्यासाठी 'handle_review' कार्यान्वयकाकडे पुढे जा
        return [handle_review_id]

# वर्कफ्लो बिल्डर निवड फंक्शनचा वापर राऊटिंगसाठी करतो
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # मल्टी-सेलेक्शन एज अटीचे तर्क लागू करतो
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` सारखे कस्टम एक्झिक्यूटर एजंटमधून JSON आउटपुट पार्स करून स्ट्राँगली टाइप्ड ऑब्जेक्टमध्ये रूपांतर करतात, ज्याचा निवड फंक्शन तपास करू शकते.

#### .NET (C\#) अंमलबजावणी विश्लेषण

.NET आवृत्तीतही याच पद्धतीचा वापर केला जातो. एका `Func<object?, bool>` ला `ReviewResult` ऑब्जेक्टच्या `Result` प्रॉपर्टी तपासण्यासाठी परिभाषित केले जाते.

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

`AddEdge` मेथडचे `condition` पॅरामीटर वर्कफ्लो बिल्डरला शाखा मार्ग तयार करण्यास परवानगी देतो. वर्कफ्लो फक्त `GetCondition(expectedResult: "Yes")` खरे असल्यास `publishExecutor` चा मार्ग घेतो, अन्यथा `sendReviewerExecutor` कडे मार्ग घेतो.

## निष्कर्ष

मायक्रोसॉफ्ट एजंट फ्रेमवर्क वर्कफ्लो एक मजबूत आणि लवचिक पाया पुरवतो क्लिष्ट, मल्टी-एजंट सिस्टीमचे ऑर्केस्ट्रेशन करण्यासाठी. त्याच्या ग्राफ-आधारित आर्किटेक्चर आणि मुख्य तत्त्वांचा उपयोग करून, डेव्हलपर्स Python आणि .NET दोन्हीमध्ये प्रगत वर्कफ्लो डिझाइन आणि अंमलात आणू शकतात. तुमच्या अ‍ॅप्लिकेशनला साधी अनुक्रमिक प्रक्रिया, समानांतर अंमलबजावणी, किंवा डायनॅमिक अटी-आधारित लॉजिक आवश्यक असो, फ्रेमवर्क शक्तिशाली, स्केलेबल, आणि टाइप-सुरक्षित AI-सक्षम सोल्यूशन्स तयार करण्यासाठी साधने पुरवतो.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->