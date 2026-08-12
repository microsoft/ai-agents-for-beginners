# Microsoft Agent Framework Workflow सँग बहु-एजेन्ट अनुप्रयोगहरू बनाउने

यो ट्युटोरियलले Microsoft Agent Framework प्रयोग गरेर बहु-एजेन्ट अनुप्रयोगहरू बुझ्न र बनाउन गाइड गर्नेछ। हामी बहु-एजेन्ट प्रणालीहरूको मूल अवधारणाहरू अन्वेषण गर्नेछौं, फ्रेमवर्कको Workflow कम्पोनेन्टको आर्किटेक्चरमा डुबुल्की मार्नेछौं, र विभिन्न workflow ढाँचाहरूका लागि Python र .NET दुवैमा व्यावहारिक उदाहरणहरू हेर्नेछौं।

## 1\. बहु-एजेन्ट प्रणालीहरू बुझ्न

AI एजेन्ट एक यस्तो प्रणाली हो जुन साधारण ठूलो भाषा मोडेल (LLM) को क्षमताभन्दा बढी हुन्छ। यसले आफ्नो वातावरणलाई बुझ्न, निर्णय लिन, र विशिष्ट लक्ष्यहरू प्राप्त गर्न क्रियाहरू गर्न सक्छ। बहु-एजेन्ट प्रणालीमा यी एजेन्टहरू मध्ये धेरैजना मिलेर एउटा समस्या समाधान गर्छन् जुन एकल एजेन्टले स्वतन्त्र रूपमा गर्न गाह्रो वा असम्भव हुन्छ।

### सामान्य अनुप्रयोग परिदृश्यहरु

  * **जटिल समस्या समाधान**: ठूलो कार्य (जस्तै, कम्पनीव्यापी कार्यक्रम योजना) लाई साना उप-कार्यहरूमा विभाजन गर्नु जसलाई विशेष एजेन्टहरूले सम्हाल्छन् (जस्तै, बजेट एजेन्ट, logistic एजेन्ट, marketing एजेन्ट)।
  * **भर्चुअल सहायकहरू**: एउटा मुख्य सहायक एजेन्टले तालिका मिलाउने, अनुसन्धान गर्ने, र बुकिङ जस्ता कार्यहरू अन्य विशेष एजेन्टहरूलाई सुम्पिन्छ।
  * **स्वचालित सामग्री सिर्जना**: एउटा workflow जहाँ एक एजेन्टले सामग्रीको मस्यौदा तयार गर्छ, अर्कोले यसको शुद्धता र स्वरका लागि समीक्षा गर्छ, र तेस्रोले यो प्रकाशन गर्छ।

### बहु-एजेन्ट ढाँचाहरू

बहु-एजेन्ट प्रणालीहरू विभिन्न ढाँचाहरूमा व्यवस्थित गर्न सकिन्छ, जसले उनीहरूको अन्तरक्रियाको तरिका निर्धारण गर्छ:

  * **क्रमबद्ध (Sequential)**: एजेन्टहरू पूर्वनिर्धारित क्रममा काम गर्छन्, जस्तै असेंबली लाइन। एक एजेन्टको आउटपुट अर्को एजेन्टको इनपुट हुन्छ।
  * **समसामयिक (Concurrent)**: एजेन्टहरूले एउटै कार्यका विभिन्न भागहरूमा समानान्तर काम गर्छन्, र तिनको परिणाम अन्त्यमा सङ्कलन गरिन्छ।
  * **सशर्त (Conditional)**: workflow एक एजेन्टको आउटपुटको आधारमा फरक मार्गहरू पालना गर्छ, if-then-else बयान जस्तै।

## 2\. Microsoft Agent Framework Workflow आर्किटेक्चर

Agent Framework को workflow प्रणाली एक उन्नत समन्वय इन्जिन हो जसले बहु एजेन्टहरूबीच जटिल अन्तरक्रियाहरू व्यवस्थापन गर्न बनाइएको छ। यो एक ग्राफ-आधारित आर्किटेक्चरमा निर्माण गरिएको छ जसले [Pregel-शैलीको कार्यान्वयन मोडेल](https://kowshik.github.io/JPregel/pregel_paper.pdf) प्रयोग गर्छ, जहाँ प्रक्रिया "supersteps" भनिने समक्रमित चरणहरूमा हुन्छ।

### मुख्य कम्पोनेन्टहरू

आर्किटेक्चर मुख्य तीन भागहरू मिलेर बनेको छ:

1.  **Executors**: यी आधारभूत प्रशोधन एकाइहरू हुन्। हाम्रा उदाहरणहरूमा, `Agent` एक प्रकारको executor हो। प्रत्येक executor सँग विभिन्न प्रकारका सन्देशहरू प्राप्त हुँदा स्वतः सक्रिय हुने अनेकौं सन्देश ह्यान्डलरहरू हुन सक्छ।
2.  **Edges**: यी executorहरूबीच सन्देशहरू यात्रा गर्ने मार्ग निर्धारण गर्छन्। Edges सशर्त हुन सक्छन्, जसले workflow ग्राफमा जानकारीको गतिशील राउटिङ अनुमति दिन्छ।
3.  **Workflow**: यो कम्पोनेन्टले सम्पूर्ण प्रक्रिया समन्वय गर्दछ, executorहरू, edges, र कार्यान्वयनको समग्र प्रवाह व्यवस्थापन गर्दछ। यसले सन्देशहरू सही क्रममा प्रशोधन हुन सुनिश्चित गर्दछ र अवलोकनयोग्यताको लागि घटनाहरू स्ट्रिम गर्दछ।

*workflow प्रणालीका मुख्य कम्पोनेन्टहरू देखाउने एक चित्र।*

यो संरचनाले अनुक्रमिक चेनहरू, समानान्तर प्रशोधनको लागि fan-out/fan-in, र सशर्त प्रवाहको लागि switch-case तार्किक जस्ता आधारभूत ढाँचाहरू प्रयोग गरेर बलियो र स्केलेबल अनुप्रयोगहरू बनाउन अनुमति दिन्छ।

## 3\. व्यावहारिक उदाहरणहरू र कोड विश्लेषण

अब, फ्रेमवर्क प्रयोग गरेर विभिन्न workflow ढाँचाहरू कसरी कार्यान्वयन गर्ने हेरौं। हामी प्रत्येक उदाहरणका लागि Python र .NET कोड दुवै हेर्नेछौं।

### केस 1: आधारभूत अनुक्रमिक workflow

यो सबैभन्दा सरल ढाँचा हो, जहाँ एउटा एजेन्टको आउटपुट सिधै अर्को एजेन्टलाई प्रदान गरिन्छ। हाम्रो परिदृश्यमा होटलको `FrontDesk` एजेन्टले यात्रा सिफारिस दिन्छ, जुन `Concierge` एजेन्टले समीक्षा गर्छ।

*आधारभूत FrontDesk -> Concierge workflow को चित्र।*

#### परिदृश्य पृष्ठभूमि

एक यात्रुले पेरिसमा सिफारिस माग्छ।

1.  `FrontDesk` एजेन्टले सहज रूपमा Louvre संग्रहालय भ्रमण गर्न सुझाव दिन्छ।
2.  `Concierge` एजेन्ट, जसले प्रामाणिक अनुभवलाई प्राथमिकता दिन्छ, उक्त सुझाव प्राप्त गर्छ र समीक्षा गरेर स्थानीय, कम पर्यटकिय विकल्प सल्लाह दिन्छ।

#### Python कार्यान्वयन विश्लेषण

Python उदाहरणमा, पहिले दुई एजेन्टहरू परिभाषित र सिर्जना गरिन्छ, प्रत्येकसँग निश्चित निर्देशनहरू छन्।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# एजेन्ट भूमिका र निर्देशनहरू परिभाषित गर्नुहोस्
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# एजेन्ट उदाहरणहरू सिर्जना गर्नुहोस्
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

त्यसपछि, `WorkflowBuilder` प्रयोग गरी ग्राफ निर्माण गरिन्छ। `front_desk_agent` लाई सुरुवाती बिन्दु बनाइन्छ र यसको आउटपुटलाई `reviewer_agent` सँग जोड्न edge बनाइन्छ।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

अन्त्यमा workflow प्रारम्भिक प्रयोगकर्ता प्रॉम्प्टसँग चलाइन्छ।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run ले workflow चलाउँछ; get_outputs() ले output executor को नतिजा फिर्ता गर्छ।
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) कार्यान्वयन विश्लेषण

.NET कार्यान्वयन पनि धेरै मिल्दोजुल्दो तर्क पालना गर्छ। पहिले एजेन्टहरूको नाम र निर्देशनका लागि स्थिरांक निर्धारण गरिन्छ।

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

एजेन्टहरू `AzureOpenAIClient` (Responses API) प्रयोग गरी सिर्जना गरिन्छ, र त्यसपछि `WorkflowBuilder` ले `frontDeskAgent` बाट `reviewerAgent` तर्फ अनुक्रमिक प्रवाह परिभाषित गरी edge थप्छ।

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

त्यसपछि workflow प्रयोगकर्ताको सन्देशसँग चलाइन्छ र परिणामहरू स्ट्रिम गरिन्छ।

### केस 2: बहु-चरण अनुक्रमिक workflow

यो ढाँचाले आधारभूत अनुक्रममा बढी एजेन्टहरू थप्छ। धेरै चरणहरूको परिमार्जन वा रूपान्तरण आवश्यक प्रक्रियाहरूका लागि उपयुक्त हुन्छ।

#### परिदृश्य पृष्ठभूमि

प्रयोगकर्ताले एक लिभिङ रुमको छवि प्रदान गर्दछ र फर्निचरको कोटेशन माग्छ।

1.  **Sales-Agent**: छविमा रहेको फर्निचर वस्तुहरू पहिचान गरी सूची तयार गर्छ।
2.  **Price-Agent**: वस्तुहरूको सूची लिएर विस्तृत मूल्य ब्रेकडाउन प्रदान गर्छ, जसमा बजेट, मध्यम र प्रिमियम विकल्पहरू समावेश छन्।
3.  **Quote-Agent**: मूल्याङ्कन गरिएको सूची प्राप्त गरी यसलाई Markdown मा औपचारिक कोटेसन दस्तावेजमा ढाल्छ।

*Sales -> Price -> Quote workflow को चित्र।*

#### Python कार्यान्वयन विश्लेषण

तीन एजेन्टहरू परिभाषित गरिन्छ, प्रत्येकको विशेषज्ञ भूमिका स्पष्ट हुन्छ। workflow निर्माण गर्दा `add_edge` प्रयोग गरी श्रृंखला बनाईन्छ: `sales_agent` -> `price_agent` -> `quote_agent`।

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# तीनवटा विशेष एजेन्टहरू सिर्जना गर्नुहोस्
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# अनुक्रमिक कार्यप्रवाह निर्माण गर्नुहोस्
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

इनपुट `ChatMessage` हो जसमा टेक्स्ट र छवि URI दुवै हुन्छन्। फ्रेमवर्कले प्रत्येक एजेन्टको आउटपुट अर्को एजेन्टमा श्रृंखलाबद्ध रूपमा पठाउने काम गर्छ जबसम्म अन्तिम कोटेशन उत्पादन हुँदैन।

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# प्रयोगकर्ताको सन्देशमा पाठ र छवि दुवै छन्
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# वर्कफ्लो चलाउनुहोस्
events = await workflow.run(message)
```

#### .NET (C\#) कार्यान्वयन विश्लेषण

.NET उदाहरणले Python संस्करणलाई प्रतिबिम्बित गर्छ। तीन एजेन्ट (`salesagent`, `priceagent`, `quoteagent`) सिर्जना गरिन्छ। `WorkflowBuilder` तिनीहरूलाई अनुक्रमिक रूपमा लिंक गर्छ।

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

प्रयोगकर्ताको सन्देश छवि डेटा (बाइट्सका रूपमा) र पाठ प्रॉम्प्ट दुवै सहित निर्माण गरिएको छ। `InProcessExecution.RunStreamingAsync` विधिले workflow सुरू गर्छ र अन्तिम आउटपुट स्ट्रिमबाट समातिन्छ।

### केस 3: समसामयिक workflow

यस ढाँचाले समय बचतको लागि कार्यहरू एकैपटक गर्न सकिने बेला प्रयोग गरिन्छ। यसमा धेरै एजेन्टहरूमा "fan-out" र परिणामहरू सङ्कलन गर्न "fan-in" समावेश हुन्छ।

#### परिदृश्य पृष्ठभूमि

प्रयोगकर्ताले सियाटल यात्रा योजना बनाउन भन्छ।

1.  **Dispatcher (Fan-Out)**: प्रयोगकर्ताको अनुरोध एकै समयमा दुई एजेन्टहरूलाई पठाइन्छ।
2.  **Researcher-Agent**: डिसेम्बरमा सियाटलको आकर्षणहरू, मौसम, र मुख्य विचारहरू अनुसन्धान गर्छ।
3.  **Plan-Agent**: स्वतन्त्र रूपमा दिन-दिनको विस्तृत यात्रा योजना बनाउँछ।
4.  **Aggregator (Fan-In)**: अनुसन्धानकर्ता र योजनाकार दुवैको आउटपुट सङ्कलन गरी अन्तिम नतिजा प्रस्तुत गर्छ।

*समसामयिक Researcher र Planner workflow को चित्र।*

#### Python कार्यान्वयन विश्लेषण

`ConcurrentBuilder` ले यस ढाँचाको सिर्जना सजिलो बनाउँछ। तपाईंले सहभागी एजेन्टहरूको सूची मात्र दिनु पर्छ, र बिल्डरले आवश्यक fan-out र fan-in तार्किक स्वतः बनाउँछ।

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ले fan-out/fan-in तर्क सम्हाल्छ
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# कार्यप्रवाह चलाउनुहोस्
events = await workflow.run("Plan a trip to Seattle in December")
```

फ्रेमवर्कले `research_agent` र `plan_agent` सँग समानान्तर कार्यान्वयन सुनिश्चित गर्छ र तिनको अन्तिम आउटपुट सूचीमा सङ्कलन गर्छ।

#### .NET (C\#) कार्यान्वयन विश्लेषण

.NET मा, यस ढाँचाले स्पष्ट परिभाषा माग्छ। कस्टम executors (`ConcurrentStartExecutor` र `ConcurrentAggregationExecutor`) fan-out र fan-in तार्किक सम्हाल्न सिर्जना गरिन्छ।

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

`WorkflowBuilder` पछि `AddFanOutEdge` र `AddFanInEdge` प्रयोग गरी यी कस्टम executor र एजेन्टहरू सहित ग्राफ बनाउँछ।

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### केस 4: सशर्त workflow

सशर्त workflows मा शाखागत तार्किक समावेश हुन्छ, जसले प्रणालीलाई मध्यवर्ती परिणामहरूका आधारमा फरक मार्गहरू लिन अनुमति दिन्छ।

#### परिदृश्य पृष्ठभूमि

यो workflow ले प्राविधिक पाठ्यक्रम स्वचालित रूपमा सिर्जना र प्रकाशन गर्छ।

1.  **Evangelist-Agent**: दिइएको रूपरेखा र URLs अनुसार पाठ्यक्रमको मसौदा लेख्छ।
2.  **ContentReviewer-Agent**: मसौदाको समीक्षा गर्छ। यो जाँच्छ कि शब्द संख्या २०० भन्दा बढी छ कि छैन।
3.  **सशर्त शाखा**:
     * **स्वीकृत भएमा (`हो`)**: workflow `Publisher-Agent` तर्फ अगाडि बढ्छ।
     * **अस्वीकृत भएमा (`होइन`)**: workflow रोकिन्छ र अस्वीकृतिको कारण आउटपुट गर्छ।
4.  **Publisher-Agent**: मसौदा स्वीकृत भएमा, यो एजेन्ट सामग्री Markdown फाइलमा सुरक्षित गर्छ।

#### Python कार्यान्वयन विश्लेषण

यस उदाहरणले कस्टम फङ्क्शन `select_targets` प्रयोग गर्छ जुन सशर्त तार्किक कार्यान्वयन गर्छ। यो फङ्क्शन `add_multi_selection_edge_group` लाई दिइन्छ र समीक्षकको आउटपुटको `review_result` क्षेत्रको आधारमा workflow सञ्झालन गर्छ।

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# यो कार्यले समीक्षा नतिजाको आधारमा अर्को कदम निर्धारण गर्दछ
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # स्वीकृत भएमा, 'save_draft' कार्यकर्ता तर्फ अगाडि बढ्नुहोस्
        return [save_draft_id]
    else:
        # अस्वीकृत भएमा, असफलता रिपोर्ट गर्न 'handle_review' कार्यकर्ता तर्फ अगाडि बढ्नुहोस्
        return [handle_review_id]

# वर्कफ्लो निर्माता रुटिङको लागि छनौट कार्य प्रयोग गर्दछ
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # बहु-छनौट एजले सर्तीय तर्क कार्यान्वयन गर्दछ
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

कस्टम executor हरू जस्तै `to_reviewer_result` ले एजेन्टहरूको JSON आउटपुट पार्स गरेर कडा-टाइप गरिएको वस्तुहरूमा परिवर्तन गर्छ, जसलाई चयन फङ्क्शनले निरीक्षण गर्न सक्छ।

#### .NET (C\#) कार्यान्वयन विश्लेषण

.NET संस्करणले पनि यस्तै दृष्टिकोण अपनाउँछ। `Func<object?, bool>` परिभाषित गरी `ReviewResult` वस्तुको `Result` गुण जाँचिन्छ।

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

`AddEdge` विधिको `condition` प्यारामिटरले `WorkflowBuilder` लाई शाखागत मार्ग सिर्जना गर्न अनुमति दिन्छ। workflow `publishExecutor` तर्फको edge मा मात्र जान्छ यदि `GetCondition(expectedResult: "Yes")` ले सत्य फर्काउँछ भने। नभए, यो `sendReviewerExecutor` तर्फको मार्ग अपनाउँछ।

## निष्कर्ष

Microsoft Agent Framework Workflow ले जटिल, बहु-एजेन्ट प्रणालीहरू समन्वय गर्न बलियो र लचकदार आधार प्रदान गर्छ। यसको ग्राफ-आधारित आर्किटेक्चर र मुख्य कम्पोनेन्टहरूलाई उपयोग गरेर, विकासकर्ताहरूले Python र .NET दुवैमा परिष्कृत workflow डिजाइन र कार्यान्वयन गर्न सक्छन्। तपाईंको अनुप्रयोगले सरल अनुक्रमिक प्रक्रिया, समानान्तर कार्यान्वयन, वा गतिशील सशर्त तार्किक आवश्यक परे पनि, फ्रेमवर्कले शक्तिशाली, स्केलेबल, र प्रकार-सुरक्षित AI-शक्तियुक्त समाधानहरू बनाउनका लागि उपकरणहरू प्रदान गर्दछ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सही हुन प्रयास गर्छौं, तर कृपया जानकार हुनुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। मूल दस्तावेज़ यसको मूल भाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा त्रुटिको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->