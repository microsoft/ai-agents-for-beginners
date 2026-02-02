# माइक्रोसफ्ट एजेन्ट फ्रेमवर्क वर्कफ्लो प्रयोग गरेर बहु-एजेन्ट एप्लिकेसन निर्माण

यो ट्युटोरियलले तपाईंलाई माइक्रोसफ्ट एजेन्ट फ्रेमवर्क प्रयोग गरेर बहु-एजेन्ट एप्लिकेसन निर्माण र बुझ्न मार्गदर्शन गर्नेछ। हामी बहु-एजेन्ट प्रणालीका मुख्य अवधारणाहरू अन्वेषण गर्नेछौं, फ्रेमवर्कको वर्कफ्लो कम्पोनेन्टको आर्किटेक्चरमा गहिरो रूपमा जाँच गर्नेछौं, र विभिन्न वर्कफ्लो ढाँचाहरूका लागि Python र .NET मा व्यावहारिक उदाहरणहरू हेर्नेछौं।

## १\. बहु-एजेन्ट प्रणाली बुझ्दै

एआई एजेन्ट भनेको साधारण ठूलो भाषा मोडेल (LLM) भन्दा पर जान सक्ने प्रणाली हो। यसले आफ्नो वातावरणलाई बुझ्न सक्छ, निर्णय गर्न सक्छ, र विशिष्ट लक्ष्यहरू प्राप्त गर्न कार्य गर्न सक्छ। बहु-एजेन्ट प्रणालीमा धेरै एजेन्टहरू समावेश हुन्छन्, जसले एकल एजेन्टले समाधान गर्न कठिन वा असम्भव हुने समस्या समाधान गर्न सहकार्य गर्छन्।

### सामान्य अनुप्रयोग परिदृश्यहरू

  * **जटिल समस्या समाधान**: ठूलो कार्यलाई (जस्तै, कम्पनी-व्यापी कार्यक्रमको योजना बनाउने) साना उप-कार्यहरूमा विभाजन गर्ने, जसलाई विशेष एजेन्टहरूले ह्यान्डल गर्छन् (जस्तै, बजेट एजेन्ट, लजिस्टिक्स एजेन्ट, मार्केटिङ एजेन्ट)।
  * **भर्चुअल सहायकहरू**: एक प्राथमिक सहायक एजेन्टले तालिका बनाउने, अनुसन्धान गर्ने, र बुकिङ गर्ने जस्ता कार्यहरू अन्य विशेष एजेन्टहरूलाई सुम्पिन्छ।
  * **स्वचालित सामग्री सिर्जना**: एक वर्कफ्लो जहाँ एक एजेन्टले सामग्री तयार गर्छ, अर्कोले यसको शुद्धता र टोनको समीक्षा गर्छ, र तेस्रोले यसलाई प्रकाशित गर्छ।

### बहु-एजेन्ट ढाँचाहरू

बहु-एजेन्ट प्रणालीहरू विभिन्न ढाँचामा व्यवस्थित गर्न सकिन्छ, जसले उनीहरूको अन्तर्क्रिया निर्धारण गर्छ:

  * **क्रमिक**: एजेन्टहरू पूर्वनिर्धारित क्रममा काम गर्छन्, जस्तै असेंबली लाइन। एक एजेन्टको आउटपुट अर्कोको इनपुट बन्छ।
  * **समानान्तर**: एजेन्टहरू कार्यको विभिन्न भागहरूमा समानान्तर रूपमा काम गर्छन्, र अन्त्यमा उनीहरूको नतिजा समग्र रूपमा प्रस्तुत गरिन्छ।
  * **सशर्त**: वर्कफ्लोले एजेन्टको आउटपुटको आधारमा विभिन्न मार्गहरू अनुसरण गर्छ, जस्तै यदि-त-भने-नत्र कथन।

## २\. माइक्रोसफ्ट एजेन्ट फ्रेमवर्क वर्कफ्लो आर्किटेक्चर

एजेन्ट फ्रेमवर्कको वर्कफ्लो प्रणाली एक उन्नत समन्वय इन्जिन हो, जसले बहु-एजेन्टहरू बीचको जटिल अन्तर्क्रियाहरू व्यवस्थापन गर्न डिजाइन गरिएको हो। यो [Pregel-शैली कार्यान्वयन मोडेल](https://kowshik.github.io/JPregel/pregel_paper.pdf) मा आधारित ग्राफ-आधारित आर्किटेक्चरमा निर्माण गरिएको छ, जहाँ "सुपरस्टेप्स" भनिने समकालीन चरणहरूमा प्रशोधन हुन्छ।

### मुख्य कम्पोनेन्टहरू

आर्किटेक्चर तीन मुख्य भागहरूमा विभाजित छ:

1.  **एक्जिक्युटरहरू**: यी आधारभूत प्रशोधन इकाइहरू हुन्। हाम्रो उदाहरणहरूमा, `Agent` एक प्रकारको एक्जिक्युटर हो। प्रत्येक एक्जिक्युटरमा धेरै सन्देश ह्यान्डलरहरू हुन सक्छन्, जुन प्राप्त सन्देशको प्रकारको आधारमा स्वतः सक्रिय हुन्छ।
2.  **एजहरू**: यी एक्जिक्युटरहरू बीच सन्देशहरू जाने मार्ग परिभाषित गर्छन्। एजहरूमा सर्तहरू हुन सक्छन्, जसले वर्कफ्लो ग्राफमार्फत जानकारीको गतिशील रुटिङलाई अनुमति दिन्छ।
3.  **वर्कफ्लो**: यो कम्पोनेन्टले सम्पूर्ण प्रक्रियालाई समन्वय गर्छ, एक्जिक्युटरहरू, एजहरू, र कार्यान्वयनको समग्र प्रवाहलाई व्यवस्थापन गर्छ। यसले सन्देशहरू सही क्रममा प्रशोधन सुनिश्चित गर्छ र अवलोकनयोग्यताका लागि घटनाहरू स्ट्रिम गर्छ।

*वर्कफ्लो प्रणालीका मुख्य कम्पोनेन्टहरूको चित्र।*

यो संरचनाले क्रमिक चेनहरू, समानान्तर प्रशोधनका लागि फ्यान-आउट/फ्यान-इन, र सशर्त प्रवाहका लागि स्विच-केस तर्क जस्ता आधारभूत ढाँचाहरू प्रयोग गरेर बलियो र स्केलेबल एप्लिकेसनहरू निर्माण गर्न अनुमति दिन्छ।

## ३\. व्यावहारिक उदाहरणहरू र कोड विश्लेषण

अब, फ्रेमवर्क प्रयोग गरेर विभिन्न वर्कफ्लो ढाँचाहरू कार्यान्वयन गर्ने तरिका अन्वेषण गरौं। हामी प्रत्येक उदाहरणका लागि Python र .NET कोड हेर्नेछौं।

### केस १: आधारभूत क्रमिक वर्कफ्लो

यो सबैभन्दा सरल ढाँचा हो, जहाँ एक एजेन्टको आउटपुट अर्कोमा सिधै पास गरिन्छ। हाम्रो परिदृश्यमा एक होटल `FrontDesk` एजेन्टले यात्रा सिफारिस गर्छ, जुन `Concierge` एजेन्टले समीक्षा गर्छ।

*आधारभूत FrontDesk -> Concierge वर्कफ्लोको चित्र।*

#### परिदृश्य पृष्ठभूमि

एक यात्रीले पेरिसमा सिफारिस माग्छ।

1.  `FrontDesk` एजेन्ट, संक्षिप्तता प्राथमिकता दिने, लुभ्र संग्रहालय भ्रमण गर्न सिफारिस गर्छ।
2.  `Concierge` एजेन्ट, जसले प्रामाणिक अनुभवलाई प्राथमिकता दिन्छ, यो सिफारिस प्राप्त गर्छ। यसले सिफारिसको समीक्षा गर्छ र एक स्थानीय, कम पर्यटकयुक्त विकल्प सुझाउँछ।

#### Python कार्यान्वयन विश्लेषण

Python उदाहरणमा, हामीले पहिलो दुई एजेन्टहरू परिभाषित र निर्माण गर्छौं, प्रत्येकलाई विशिष्ट निर्देशनसहित।

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

त्यसपछि, `WorkflowBuilder` प्रयोग गरेर ग्राफ निर्माण गरिन्छ। `front_desk_agent` लाई सुरुवात बिन्दु सेट गरिन्छ, र यसको आउटपुटलाई `reviewer_agent` सँग जोड्न एज बनाइन्छ।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

अन्ततः, वर्कफ्लो प्रयोगकर्ता प्रम्प्टको साथ कार्यान्वयन गरिन्छ।

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C#) कार्यान्वयन विश्लेषण

.NET कार्यान्वयनले धेरै समान तर्क अनुसरण गर्छ। पहिलो, एजेन्टहरूको नाम र निर्देशनका लागि स्थिरांकहरू परिभाषित गरिन्छ।

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

एजेन्टहरू `OpenAIClient` प्रयोग गरेर निर्माण गरिन्छ, र त्यसपछि `WorkflowBuilder` ले `frontDeskAgent` बाट `reviewerAgent` सम्म क्रमिक प्रवाह परिभाषित गर्छ।

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

वर्कफ्लो प्रयोगकर्ताको सन्देशको साथ चलाइन्छ, र नतिजाहरू स्ट्रिम गरिन्छ।

### केस २: बहु-चरण क्रमिक वर्कफ्लो

यो ढाँचाले आधारभूत क्रमलाई थप एजेन्टहरू समावेश गर्न विस्तार गर्छ। यो प्रक्रियाहरूका लागि आदर्श हो, जसले धेरै चरणहरूको परिष्कृतता वा रूपान्तरण आवश्यक पर्छ।

#### परिदृश्य पृष्ठभूमि

एक प्रयोगकर्ताले बस्ने कोठाको तस्बिर प्रदान गर्छ र फर्निचरको मूल्यको उद्धरण माग्छ।

1.  **Sales-Agent**: तस्बिरमा फर्निचर वस्तुहरू पहिचान गर्छ र सूची बनाउँछ।
2.  **Price-Agent**: वस्तुहरूको सूची लिन्छ र बजेट, मध्यम-स्तर, र प्रिमियम विकल्पहरू सहित विस्तृत मूल्य ब्रेकडाउन प्रदान गर्छ।
3.  **Quote-Agent**: मूल्य सूची प्राप्त गर्छ र Markdown मा औपचारिक उद्धरण दस्तावेजको रूपमा ढाँचा बनाउँछ।

*Sales -> Price -> Quote वर्कफ्लोको चित्र।*

#### Python कार्यान्वयन विश्लेषण

तीन एजेन्टहरू परिभाषित गरिन्छ, प्रत्येकको विशेष भूमिका छ। वर्कफ्लो `add_edge` प्रयोग गरेर निर्माण गरिन्छ: `sales_agent` -> `price_agent` -> `quote_agent`।

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

इनपुट एक `ChatMessage` हो, जसमा पाठ र तस्बिर URI समावेश छ। फ्रेमवर्कले प्रत्येक एजेन्टको आउटपुटलाई अर्कोमा पास गर्दै अन्तिम उद्धरण उत्पन्न गर्छ।

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

.NET उदाहरणले Python संस्करणलाई प्रतिबिम्बित गर्छ। तीन एजेन्ट (`salesagent`, `priceagent`, `quoteagent`) निर्माण गरिन्छ। `WorkflowBuilder` ले तिनीहरूलाई क्रमिक रूपमा लिंक गर्छ।

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

प्रयोगकर्ताको सन्देश तस्बिर डेटा (बाइट्सको रूपमा) र पाठ प्रम्प्ट सहित निर्माण गरिन्छ। `InProcessExecution.StreamAsync` विधिले वर्कफ्लो सुरु गर्छ, र अन्तिम आउटपुट स्ट्रिमबाट कब्जा गरिन्छ।

### केस ३: समानान्तर वर्कफ्लो

यो ढाँचा तब प्रयोग गरिन्छ जब कार्यहरू एकै समयमा प्रदर्शन गर्न सकिन्छ समय बचत गर्न। यसमा "फ्यान-आउट" धेरै एजेन्टहरूमा र "फ्यान-इन" नतिजाहरू समग्र गर्न समावेश छ।

#### परिदृश्य पृष्ठभूमि

एक प्रयोगकर्ताले सिएटलको यात्रा योजना बनाउन अनुरोध गर्छ।

1.  **Dispatcher (Fan-Out)**: प्रयोगकर्ताको अनुरोध एकै समयमा दुई एजेन्टहरूमा पठाइन्छ।
2.  **Researcher-Agent**: सिएटलको डिसेम्बर भ्रमणका लागि आकर्षणहरू, मौसम, र प्रमुख विचारहरू अनुसन्धान गर्छ।
3.  **Plan-Agent**: स्वतन्त्र रूपमा विस्तृत दिन-प्रतिदिन यात्रा तालिका बनाउँछ।
4.  **Aggregator (Fan-In)**: अनुसन्धानकर्ता र योजनाकारबाट प्राप्त आउटपुटहरू संकलन गरिन्छ र अन्तिम नतिजा रूपमा प्रस्तुत गरिन्छ।

*समानान्तर Researcher र Planner वर्कफ्लोको चित्र।*

#### Python कार्यान्वयन विश्लेषण

`ConcurrentBuilder` ले यो ढाँचा निर्माणलाई सरल बनाउँछ। तपाईंले सहभागी एजेन्टहरूको सूची दिनुहुन्छ, र बिल्डरले आवश्यक फ्यान-आउट र फ्यान-इन तर्क स्वतः बनाउँछ।

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

फ्रेमवर्कले सुनिश्चित गर्छ कि `research_agent` र `plan_agent` समानान्तर रूपमा कार्यान्वयन हुन्छन्, र तिनीहरूको अन्तिम आउटपुट सूचीमा संकलन गरिन्छ।

#### .NET (C#) कार्यान्वयन विश्लेषण

.NET मा, यो ढाँचाले स्पष्ट परिभाषा आवश्यक छ। कस्टम एक्जिक्युटरहरू (`ConcurrentStartExecutor` र `ConcurrentAggregationExecutor`) फ्यान-आउट र फ्यान-इन तर्क ह्यान्डल गर्न निर्माण गरिन्छ।

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

`WorkflowBuilder` ले यी कस्टम एक्जिक्युटरहरू र एजेन्टहरू प्रयोग गरेर ग्राफ निर्माण गर्न `AddFanOutEdge` र `AddFanInEdge` प्रयोग गर्छ।

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### केस ४: सशर्त वर्कफ्लो

सशर्त वर्कफ्लोले शाखा तर्क प्रस्तुत गर्छ, जसले प्रणालीलाई अन्तरिम नतिजाहरूको आधारमा विभिन्न मार्गहरू लिन अनुमति दिन्छ।

#### परिदृश्य पृष्ठभूमि

यो वर्कफ्लोले प्राविधिक ट्युटोरियलको निर्माण र प्रकाशन स्वचालित गर्छ।

1.  **Evangelist-Agent**: दिइएको रूपरेखा र URL हरूको आधारमा ट्युटोरियलको ड्राफ्ट लेख्छ।
2.  **ContentReviewer-Agent**: ड्राफ्टको समीक्षा गर्छ। यसले शब्द गणना २०० भन्दा बढी छ कि छैन जाँच गर्छ।
3.  **सशर्त शाखा**:
      * **यदि स्वीकृत (`Yes`)**: वर्कफ्लो `Publisher-Agent` मा अगाडि बढ्छ।
      * **यदि अस्वीकृत (`No`)**: वर्कफ्लो रोक्छ र अस्वीकृतिको कारण आउटपुट गर्छ।
4.  **Publisher-Agent**: यदि ड्राफ्ट स्वीकृत छ भने, यो एजेन्टले सामग्रीलाई Markdown फाइलमा सुरक्षित गर्छ।

#### Python कार्यान्वयन विश्लेषण

यो उदाहरणले सशर्त तर्क कार्यान्वयन गर्न `select_targets` नामक कस्टम कार्य प्रयोग गर्छ। यो कार्य `add_multi_selection_edge_group` मा पास गरिन्छ र `review_result` क्षेत्रको आधारमा वर्कफ्लो निर्देशित गर्छ।

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

कस्टम एक्जिक्युटरहरू जस्तै `to_reviewer_result` एजेन्टहरूको JSON आउटपुटलाई पार्स गर्न र चयन कार्यले निरीक्षण गर्न सक्ने बलियो-टाइप वस्तुहरूमा रूपान्तरण गर्न प्रयोग गरिन्छ।

#### .NET (C#) कार्यान्वयन विश्लेषण

.NET संस्करणले समान दृष्टिकोण प्रयोग गर्छ। एक `Func<object?, bool>` परिभाषित गरिन्छ, जसले `ReviewResult` वस्तुको `Result` सम्पत्ति जाँच गर्छ।

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

`AddEdge` विधिको `condition` प्यारामिटरले `WorkflowBuilder` लाई शाखा मार्ग निर्माण गर्न अनुमति दिन्छ। वर्कफ्लोले `publishExecutor` मा एज पछ्याउँछ यदि `GetCondition(expectedResult: "Yes")` सत्य फिर्ता गर्छ। अन्यथा, यो `sendReviewerExecutor` मार्ग पछ्याउँछ।

## निष्कर्ष

माइक्रोसफ्ट एजेन्ट फ्रेमवर्क वर्कफ्लोले जटिल, बहु-एजेन्ट प्रणालीहरू समन्वय गर्न बलियो र लचिलो आधार प्रदान गर्छ। यसको ग्राफ-आधारित आर्किटेक्चर र मुख्य कम्पोनेन्टहरू प्रयोग गरेर, विकासकर्ताहरूले Python र .NET मा परिष्कृत वर्कफ्लोहरू डिजाइन र कार्यान्वयन गर्न सक्छन्। तपाईंको एप्लिकेसनलाई सरल क्रमिक प्रशोधन, समानान्तर कार्यान्वयन, वा गतिशील सशर्त तर्क आवश्यक परे पनि, फ्रेमवर्कले शक्तिशाली, स्केलेबल, र टाइप-सेफ एआई-संचालित समाधानहरू निर्माण गर्न उपकरणहरू प्रदान गर्छ।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी यथार्थताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। मूल दस्तावेज़ यसको मातृभाषामा आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।