# माइक्रोसॉफ्ट एजेंट फ्रेमवर्क वर्कफ़्लो के साथ मल्टी-एजेंट एप्लिकेशन बनाना

यह ट्यूटोरियल आपको माइक्रोसॉफ्ट एजेंट फ्रेमवर्क का उपयोग करके मल्टी-एजेंट एप्लिकेशन को समझने और बनाने के लिए मार्गदर्शन करेगा। हम मल्टी-एजेंट सिस्टम्स की मुख्य अवधारणाओं का अन्वेषण करेंगे, फ्रेमवर्क के वर्कफ़्लो घटक की वास्तुकला में गहराई से उतरेंगे, और विभिन्न वर्कफ़्लो पैटर्न के लिए पायथन और .NET में व्यावहारिक उदाहरणों के माध्यम से चलेंगे।

## 1\. मल्टी-एजेंट सिस्टम्स को समझना

एक एआई एजेंट एक ऐसा सिस्टम है जो एक मानक लार्ज लैंग्वेज मॉडल (LLM) की क्षमताओं से परे जाता है। यह अपने परिवेश को समझ सकता है, निर्णय ले सकता है, और विशिष्ट लक्ष्यों को प्राप्त करने के लिए कार्य कर सकता है। एक मल्टी-एजेंट सिस्टम में कई ऐसे एजेंट आर्टिकों के सहयोग होते हैं जो एक समस्या को हल करने के लिए मिलकर काम करते हैं, जो एक अकेले एजेंट के लिए कठिन या असंभव होगा।

### सामान्य अनुप्रयोग परिदृश्य

  * **जटिल समस्या समाधान**: एक बड़े कार्य (जैसे कंपनी-स्तरीय कार्यक्रम की योजना बनाना) को छोटे उप-कार्य में तोड़ना, जो विशेषज्ञ एजेंट्स द्वारा संभाले जाते हैं (जैसे बजट एजेंट, लॉजिस्टिक्स एजेंट, मार्केटिंग एजेंट)।
  * **वर्चुअल असिस्टेंट्स**: एक मुख्य सहायक एजेंट जो अनुसूची बनाने, शोध करने, और बुकिंग जैसे कार्य अन्य विशेषज्ञ एजेंट्स को सौंपता है।
  * **स्वचालित सामग्री निर्माण**: एक वर्कफ़्लो जहां एक एजेंट सामग्री का मसौदा तैयार करता है, दूसरा सटीकता और टोन की समीक्षा करता है, और तीसरा इसे प्रकाशित करता है।

### मल्टी-एजेंट पैटर्न्स

मल्टी-एजेंट सिस्टम्स को कई पैटर्न में व्यवस्थित किया जा सकता है, जो यह निर्धारित करते हैं कि वे कैसे इंटरैक्ट करते हैं:

  * **क्रमिक (Sequential)**: एजेंट पहले से तय क्रम में कार्य करते हैं, जैसे असेंबली लाइन। एक एजेंट का आउटपुट अगले के लिए इनपुट बनता है।
  * **समानांतर (Concurrent)**: एजेंट एक कार्य के विभिन्न हिस्सों पर समानांतर कार्य करते हैं, और अंत में उनके परिणामों को समेकित किया जाता है।
  * **सशर्त (Conditional)**: वर्कफ़्लो एजेंट के आउटपुट के आधार पर विभिन्न मार्गों का अनुसरण करता है, जैसे एक if-then-else कथन।

## 2\. माइक्रोसॉफ्ट एजेंट फ्रेमवर्क वर्कफ़्लो वास्तुकला

एजेंट फ्रेमवर्क का वर्कफ़्लो सिस्टम एक उन्नत समन्वय इंजन है, जो कई एजेंट्स के बीच जटिल इंटरैक्शन को प्रबंधित करने के लिए डिज़ाइन किया गया है। यह एक ग्राफ-आधारित वास्तुकला पर बना है जो [Pregel-शैली के निष्पादन मॉडल](https://kowshik.github.io/JPregel/pregel_paper.pdf) का उपयोग करता है, जहां प्रक्रिया "सुपरस्टेप्स" नामक समन्वित चरणों में होती है।

### मुख्य घटक

वास्तुकला तीन मुख्य भागों से मिलकर बनी है:

1.  **एग्जीक्यूटर्स**: ये बुनियादी प्रसंस्करण इकाइयां हैं। हमारे उदाहरणों में, एक `Agent` एक प्रकार का एग्जीक्यूटर है। प्रत्येक एग्जीक्यूटर के कई संदेश हैंडलर हो सकते हैं जो प्राप्त संदेश के प्रकार के आधार पर स्वचालित रूप से सक्रिय होते हैं।
2.  **एज**: ये एग्जीक्यूटर्स के बीच संदेशों के मार्ग को परिभाषित करते हैं। एज पर शर्तें हो सकती हैं, जो वर्कफ़्लो ग्राफ में जानकारी के गतिशील मार्ग निर्धारण की अनुमति देती हैं।
3.  **वर्कफ़्लो**: यह घटक संपूर्ण प्रक्रिया को समन्वित करता है, एग्जीक्यूटर्स, एज, और निष्पादन के समग्र प्रवाह का प्रबंधन करता है। यह सुनिश्चित करता है कि संदेश सही क्रम में संसाधित हों और निरीक्षण के लिए घटनाओं को स्ट्रीम करता है।

*वर्कफ़्लो सिस्टम के मुख्य घटकों का आरेख।*

यह संरचना क्रमिक श्रृंखलाओं, समानांतर प्रसंस्करण के लिए फैन-आउट/फैन-इन, और शर्तीय प्रवाह के लिए स्विच-केस लॉजिक जैसे मौलिक पैटर्न का उपयोग करके मजबूत और मापनीय एप्लिकेशन बनाने की अनुमति देती है।

## 3\. व्यावहारिक उदाहरण और कोड विश्लेषण

अब, चलिए देखेंगे कि फ्रेमवर्क का उपयोग करके विभिन्न वर्कफ़्लो पैटर्न कैसे लागू किए जा सकते हैं। हम प्रत्येक उदाहरण के लिए पायथन और .NET दोनों कोड देखेंगे।

### केस 1: बुनियादी क्रमिक वर्कफ़्लो

यह सबसे सरल पैटर्न है, जहां एक एजेंट का आउटपुट सीधे दूसरे को दिया जाता है। हमारे परिदृश्य में एक होटल `FrontDesk` एजेंट है जो यात्रा की सिफारिश करता है, जिसे बाद में `Concierge` एजेंट द्वारा समीक्षा की जाती है।

*बुनियादी FrontDesk -> Concierge वर्कफ़्लो का आरेख।*

#### परिदृश्य पृष्ठभूमि

एक यात्री पेरिस में सिफारिश मांगता है।

1.  `FrontDesk` एजेंट, जो संक्षिप्तता के लिए डिज़ाइन किया गया है, लूवर म्यूज़ियम की यात्रा सुझाता है।
2.  `Concierge` एजेंट, जो प्रामाणिक अनुभवों को प्राथमिकता देता है, इस सुझाव को प्राप्त करता है। यह सिफारिश की समीक्षा करता है और प्रतिक्रिया देता है, एक अधिक स्थानीय, कम पर्यटक विकल्प सुझाता है।

#### पायथन कार्यान्वयन विश्लेषण

पायथन उदाहरण में, हम पहले दो एजेंटों को परिभाषित और बनाते हैं, जिनमें से प्रत्येक के विशिष्ट निर्देश होते हैं।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# एजेंट भूमिकाओं और निर्देशों को परिभाषित करें
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# एजेंट उदाहरण बनाएं
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

इसके बाद, `WorkflowBuilder` का उपयोग ग्राफ बनाने के लिए किया जाता है। `front_desk_agent` को आरंभिक बिंदु के रूप में सेट किया गया है, और इसका आउटपुट `reviewer_agent` से जोड़ने के लिए एक एज बनाया जाता है।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

अंत में, वर्कफ़्लो को प्रारंभिक उपयोगकर्ता संकेत के साथ चलाया जाता है।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run कार्यप्रवाह को निष्पादित करता है; get_outputs() आउटपुट एक्जीक्यूटर का परिणाम लौटाता है।
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) कार्यान्वयन विश्लेषण

.NET कार्यान्वयन भी समान तर्क का पालन करता है। सबसे पहले, एजेंटों के नाम और निर्देशों के लिए स्थिरांक परिभाषित किए जाते हैं।

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

एजेंट `AzureOpenAIClient` (Responses API) का उपयोग करके बनाए जाते हैं, और फिर `WorkflowBuilder` `frontDeskAgent` से `reviewerAgent` तक क्रमिक प्रवाह परिभाषित करता है।

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

फिर, वर्कफ़्लो उपयोगकर्ता के संदेश के साथ चलाया जाता है, और परिणामों को स्ट्रीम किया जाता है।

### केस 2: बहु-चरण क्रमिक वर्कफ़्लो

यह पैटर्न बुनियादी क्रमिकता का विस्तार करता है जिसमें अधिक एजेंट शामिल होते हैं। यह ऐसे प्रक्रियाओं के लिए आदर्श है जिन्हें कई चरणों में सुधार या परिवर्तन की आवश्यकता होती है।

#### परिदृश्य पृष्ठभूमि

एक उपयोगकर्ता एक लिविंग रूम की छवि प्रदान करता है और फर्नीचर के लिए एक उद्धरण मांगता है।

1.  **सेल्स-एजेंट**: छवि में फर्नीचर आइटम्स की पहचान करता है और एक सूची बनाता है।
2.  **प्राइस-एजेंट**: आइटम्स की सूची लेकर विस्तृत मूल्य विवरण प्रदान करता है, जिसमें बजट, मध्य-श्रेणी, और प्रीमियम विकल्प शामिल हैं।
3.  **कोट-एजेंट**: कीमत वाली सूची प्राप्त करता है और इसे Markdown में एक औपचारिक उद्धरण दस्तावेज़ के रूप में प्रारूपित करता है।

*सेल्स -> प्राइस -> कोट वर्कफ़्लो का आरेख।*

#### पायथन कार्यान्वयन विश्लेषण

तीन एजेंट परिभाषित किए जाते हैं, प्रत्येक के पास विशेष भूमिका होती है। वर्कफ़्लो `add_edge` का उपयोग करके एक श्रृंखला बनाता है: `sales_agent` -> `price_agent` -> `quote_agent`।

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# तीन विशिष्ट एजेंट बनाएं
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# अनुक्रमिक वर्कफ़्लो बनाएं
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

इनपुट एक `ChatMessage` है जिसमें पाठ और छवि URI दोनों शामिल हैं। फ्रेमवर्क प्रत्येक एजेंट के आउटपुट को अगले तक श्रृंखला में पास करता है जब तक अंतिम उद्धरण उत्पन्न न हो जाए।

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# उपयोगकर्ता संदेश में दोनों टेक्स्ट और छवि शामिल हैं
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# वर्कफ़्लो चलाएँ
events = await workflow.run(message)
```

#### .NET (C\#) कार्यान्वयन विश्लेषण

.NET उदाहरण पायथन संस्करण की नकल करता है। तीन एजेंट (`salesagent`, `priceagent`, `quoteagent`) बनाए जाते हैं। `WorkflowBuilder` उन्हें क्रम में जोड़ता है।

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

उपयोगकर्ता का संदेश छवि डेटा (बाइट्स के रूप में) और टेक्स्ट प्रॉम्प्ट दोनों के साथ बनाया गया है। `InProcessExecution.RunStreamingAsync` विधि वर्कफ़्लो शुरू करती है, और अंतिम आउटपुट स्ट्रीम से कैप्चर किया जाता है।

### केस 3: समवर्ती (कंकरेन्ट) वर्कफ़्लो

यह पैटर्न तब उपयोग किया जाता है जब कार्यों को एक साथ किया जा सकता है ताकि समय बचाया जा सके। इसमें कई एजेंटों को "फैन-आउट" और परिणामों को एकत्र करने के लिए "फैन-इन" शामिल है।

#### परिदृश्य पृष्ठभूमि

एक उपयोगकर्ता सिएटल यात्रा की योजना बनाने के लिए अनुरोध करता है।

1.  **डिस्पैचर (फैन-आउट)**: उपयोगकर्ता का अनुरोध एक साथ दो एजेंटों को भेजा जाता है।
2.  **रिसर्चर-एजेंट**: सिएटल में दिसंबर में यात्रा के आकर्षण, मौसम, और प्रमुख विचारों की खोज करता है।
3.  **प्लान-एजेंट**: स्वतंत्र रूप से एक दिन-प्रतिदिन यात्रा कार्यक्रम बनाता है।
4.  **एग्रीगेटर (फैन-इन)**: रिसर्चर और प्लानर दोनों के आउटपुट एकत्र कर अंतिम परिणाम के रूप में प्रस्तुत करता है।

*समवर्ती रिसर्चर और प्लानर वर्कफ़्लो का आरेख।*

#### पायथन कार्यान्वयन विश्लेषण

`ConcurrentBuilder` इस पैटर्न के निर्माण को सरल बनाता है। आप बस प्रतिभागी एजेंटों को सूचीबद्ध करते हैं, और बिल्डर स्वचालित रूप से आवश्यक फैन-आउट और फैन-इन लॉजिक बनाता है।

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder फैन-आउट/फैन-इन लॉजिक को संभालता है
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# वर्कफ़्लो चलाएं
events = await workflow.run("Plan a trip to Seattle in December")
```

फ्रेमवर्क सुनिश्चित करता है कि `research_agent` और `plan_agent` समानांतर रूप से निष्पादित हों, और उनके अंतिम आउटपुट एक सूची में संग्रहित होते हैं।

#### .NET (C\#) कार्यान्वयन विश्लेषण

.NET में, इस पैटर्न के लिए अधिक स्पष्ट परिभाषा की आवश्यकता होती है। कस्टम एग्जीक्यूटर्स (`ConcurrentStartExecutor` और `ConcurrentAggregationExecutor`) बनाए जाते हैं जो फैन-आउट और फैन-इन लॉजिक को संभालते हैं।

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

इसके बाद `WorkflowBuilder` इन कस्टम एग्जीक्यूटर्स और एजेंटों के साथ ग्राफ बनाने के लिए `AddFanOutEdge` और `AddFanInEdge` का उपयोग करता है।

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### केस 4: सशर्त (कंडीशनल) वर्कफ़्लो

सशर्त वर्कफ़्लो शाखा लॉजिक प्रस्तुत करते हैं, जिससे सिस्टम मध्यवर्ती परिणामों के आधार पर विभिन्न मार्ग ले सकता है।

#### परिदृश्य पृष्ठभूमि

यह वर्कफ़्लो एक तकनीकी ट्यूटोरियल के निर्माण और प्रकाशन को स्वचालित करता है।

1.  **Evangelist-Agent**: दिए गए आउटलाइन और URLs के आधार पर ट्यूटोरियल का ड्राफ्ट लिखता है।
2.  **ContentReviewer-Agent**: ड्राफ्ट की समीक्षा करता है। यह जांचता है कि शब्द संख्या 200 से अधिक है या नहीं।
3.  **शाखा (Conditional Branch)**:
      * **यदि स्वीकृत (`Yes`)**: वर्कफ़्लो `Publisher-Agent` की ओर बढ़ता है।
      * **यदि अस्वीकृत (`No`)**: वर्कफ़्लो रुक जाता है और अस्वीकृति का कारण आउटपुट करता है।
4.  **Publisher-Agent**: यदि ड्राफ्ट स्वीकृत हो जाता है, तो यह एजेंट सामग्री को Markdown फ़ाइल में सहेजता है।

#### पायथन कार्यान्वयन विश्लेषण

यह उदाहरण कस्टम फ़ंक्शन, `select_targets` का उपयोग करता है जो सशर्त लॉजिक को लागू करता है। यह फ़ंक्शन `add_multi_selection_edge_group` को पास किया जाता है और समीक्षक के आउटपुट के `review_result` फ़ील्ड के आधार पर वर्कफ़्लो को निर्देशित करता है।

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# यह फ़ंक्शन समीक्षा परिणाम के आधार पर अगला कदम निर्धारित करता है
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # यदि अनुमोदित, तो 'save_draft' निष्पादक पर आगे बढ़ें
        return [save_draft_id]
    else:
        # यदि अस्वीकृत, तो विफलता की रिपोर्ट करने के लिए 'handle_review' निष्पादक पर आगे बढ़ें
        return [handle_review_id]

# वर्कफ़्लो बिल्डर रूटिंग के लिए चयन फ़ंक्शन का उपयोग करता है
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # मल्टी-सेलेक्शन एज शर्तीय तर्क को लागू करता है
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

कस्टम एग्जीक्यूटर्स जैसे `to_reviewer_result` JSON आउटपुट को पार्स कर मजबूत-टाइप्ड ऑब्जेक्ट्स में परिवर्तित करते हैं जिन्हें चयन फ़ंक्शन देख सकता है।

#### .NET (C\#) कार्यान्वयन विश्लेषण

.NET संस्करण इसी तरह की विधि का उपयोग करता है जिसमें एक कंडीशन फ़ंक्शन होता है। एक `Func<object?, bool>` परिभाषित होती है जो `ReviewResult` ऑब्जेक्ट के `Result` प्रॉपर्टी की जांच करती है।

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

`AddEdge` मेथड के `condition` पैरामीटर से `WorkflowBuilder` शाखाजनित मार्ग बना सकता है। वर्कफ़्लो केवल तब `publishExecutor` की ओर एज का अनुसरण करेगा जब कंडीशन `GetCondition(expectedResult: "Yes")` सही हो। अन्यथा, यह `sendReviewerExecutor` के पथ का अनुसरण करेगा।

## निष्कर्ष

माइक्रोसॉफ्ट एजेंट फ्रेमवर्क वर्कफ़्लो जटिल, मल्टी-एजेंट सिस्टम्स के समन्वय के लिए एक मजबूत और लचीला आधार प्रदान करता है। इसके ग्राफ-आधारित वास्तुकला और मुख्य घटकों का उपयोग करके, डेवलपर पायथन और .NET दोनों में परिष्कृत वर्कफ़्लो डिजाइन और कार्यान्वित कर सकते हैं। चाहे आपका एप्लिकेशन सरल क्रमिक प्रसंस्करण, समानांतर निष्पादन, या गतिशील सशर्त लॉजिक की आवश्यकता हो, फ्रेमवर्क शक्तिशाली, skalable, और प्रकार-सुरक्षित एआई-संचालित समाधान बनाने के लिए उपकरण प्रदान करता है।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->