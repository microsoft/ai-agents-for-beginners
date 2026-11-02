# మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ వర్క్‌ఫ్లోతో మల్టీ-ఏజెంట్ అనువర్తనాలను నిర్మించడం

ఈ దశాబ్దం మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ ఉపయోగించి మల్టీ-ఏజెంట్ అనువర్తనాలను అర్థం చేసుకోవడం మరియు తయారు చేయడంలో మీకు మార్గదర్శనం చేస్తుంది. మల్టీ-ఏజెంట్ వ్యవస్థల మూల భావనలను పరిశీలించి, ఫ్రేమ్‌వర్క్ యొక్క వర్క్‌ఫ్లో భాగం ఆర్కిటెక్చర్ లోకి లోతుగా వెల్లడి చేసి, వివిధ వర్క్‌ఫ్లో నమూనాల కోసం Python మరియు .NET లో ప్రాక్టికల్ ఉదాహరణలను చూపిస్తాము.

## 1\. మల్టీ-ఏజెంట్ వ్యవస్థలను అర్థం చేసుకోవడం

AI ఏజెంట్ ఒక సిస్టమ్, ఇది ఒక సాధారణ లార్జ్ లాంగ్వేజ్ మోడల్ (LLM) సామర్థ్యాలను మించిపోయింది. ఇది తన పరిసరాలను గ్రహించి, నిర్ణయాలు తీసుకుని, నిర్దిష్ట లక్ష్యాలను సాధించడానికి చర్యలు చేపడుతుంది. ఒక మల్టీ-ఏజెంట్ వ్యవస్థ అనేది ఈ ఏజెంట్లను కలిపి, ఒక ఏజెంట్ ఒంటరిగా చేయలేని సమస్యను పరిష్కరించడానికి సహకరిస్తుంది.

### సాధారణ అనువర్తన సందర్భాలు

* **సంక్లిష్ట సమస్య పరిష్కారం**: పెద్ద పనిని (ఉదా: సంస్థ మొత్తం ఈవెంట్ ప్లానింగ్) చిన్న ఉప-పనులుగా విభజించి, ప్రత్యేక ఏజెంట్లు (ఉదా: బడ్జెట్ ఏజెంట్, లాజిస్టిక్స్ ఏజెంట్, మార్కెటింగ్ ఏజెంట్) నిర్వహించడం.
* **వర్చువల్ అసిస్టెంట్లు**: ప్రధాన అసిస్టెంట్ ఏజెంట్ షెడ్యూలింగ్, పరిశోధన, బుకింగ్ లాంటి పనులను ఇతర ప్రత్యేక ఏజెంట్లకు డెలిగేట్ చేయడం.
* **ఆటోమేటెడ్ కంటెంట్ సృష్టి**: ఒక ఏజెంట్ కంటెంట్ డ్రాఫ్ట్ చేస్తే, మరొకవాడు దానిని ఖచ్చితత్వం మరియు వాణిగ్యాల కోసం సమీక్షించి, మూడవవాడు దాన్ని ప్రచురిస్తుంది.

### మల్టీ-ఏజెంట్ నమూనాలు

మల్టీ-ఏజెంట్ వ్యవస్థలు అనేక నమూనాలలో ఏర్పాటు చేయవచ్చు, ఇవి వారు ఎలా ఇంటర్‌యాక్ట్ అవుతారో నిర్ణయిస్తాయి:

* **క్రమంగా (Sequential)**: ఏజెంట్లు నిర్దేశించిన క్రమంలో పనిచేస్తారు, అసెంబ్లీ లైన్ లాంటిది. ఒక ఏజెంట్ ఔట్‌పుట్ తరువాతి ఏజెంట్ ఇన్‌పుట్ అవుతుంది.
* **సమకాలీన (Concurrent)**: ఏజెంట్లు ఒకే సమయంలో వివిధ భాగాలలో పని చేస్తారు, వారి ఫలితాలు చివరికి సంగ్రహించబడతాయి.
* **పరిస్థితులపై ఆధారపడి (Conditional)**: ఏజెంట్ ఔట్‌పుట్ ఆధారంగా వర్క్‌ఫ్లో వేర్వేరు మార్గాలు అనుసరిస్తుంది, if-then-else స్టేట్‌మెంట్ లాంటిది.

## 2\. మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ వర్క్‌ఫ్లో ఆర్కిటెక్చర్

ఏజెంట్ ఫ్రేమ్‌వర్క్ వర్క్‌ఫ్లో సిస్టమ్ అనేది బహుళ ఏజెంట్ల మధ్య సంక్లిష్ట ఇంటరాక్షన్లను నిర్వహించడానికి రూపొందించిన ఒక ఆధునిక ఆర్కెస్ట్రేషన్ ఇంజిన్. ఇది ఒక గ్రాఫ్-ఆధారిత ఆర్కిటెక్చర్ పై నిర్మించబడింది, ఇందులో [Pregel-స్టైల్ ఎగ్జిక్యూషన్ మోడల్](https://kowshik.github.io/JPregel/pregel_paper.pdf) ఉపయోగిస్తారు, ఇక్కడ "సూపర్‌స్టెప్స్" అనబడే సమకాలీన దశల్లో ప్రాసెసింగ్ జరుగుతుంది.

### ప్రధాన భాగాలు

ఆర్కిటెక్చర్ మూడు ప్రధాన భాగాలతో కూడి ఉంటుంది:

1.  **ఎగ్జిక్యూటర్లు**: ఇవి ప్రాధమిక ప్రాసెసింగ్ యూనిట్స్. మన ఉదాహరణలో, `Agent` ఒక ఎగ్జిక్యూటర్ రకం. ప్రతి ఎగ్జిక్యూటర్ కు చాల MESSAGE HANDLER లు ఉండవచ్చు, అవి అందిన సందేశం రకాన్ని బట్టి ఆటోమేటిక్ గా పిలవబడతాయి.
2.  **ఎడ్జెస్**: ఎగ్జిక్యూటర్ల మధ్య సందేశాలు ఎలా వెళుతాయో నిర్వచించే మార్గాలు. ఎడ్జెస్ కు షరతులు ఉండవచ్చు, అవి వర్క్‌ఫ్లో గ్రాఫ్ లో సమాచారాన్ని డైనమిక్‌గా మార్గదర్శనం చేస్తాయి.
3.  **వర్క్‌ఫ్లో**: ఇది మొత్తం ప్రక్రియను సమన్వయం చేస్తుంది, ఎగ్జిక్యూటర్లు, ఎడ్జెస్ మరియు ఎగ్జిక్యూషన్ యొక్క మొత్తం ప్రవాహాన్ని నిర్వహిస్తుంది. సందేశాలు సరైన క్రమంలో ప్రాసెస్ అవుతాయని నిర్ధారిస్తుంది మరియు పరిశీలన కోసం ఈవెంట్స్ ప్రసారం చేస్తుంది.

*వర్క్‌ఫ్లో సిస్టమ్ యొక్క ప్రధాన భాగాల‌ను చూపించే ఒక డయాగ్రామ్.*

ఈ నిర్మాణం క్రమశిక్షణచేసిన శ్రేణులు, ఫ్యాన్-అవుట్/ఫ్యాన్-ఇన్ కోసం సమకాలీన ప్రాసెసింగ్, మరియు షవిచ్-కేస్ లాజిక్ వంటి మూల నమూనాలతో హృదయపూర్వక, స్కేలబుల్ అనువర్తనాల నిర్మాణానికి అనుమతిస్తుంది.

## 3\. ప్రాక్టికల్ ఉదాహరణలు మరియు కోడ్ విశ్లేషణ

ఇప్పుడు, ఫ్రేమ్‌వర్క్ ఉపయోగించి వివిధ వర్క్‌ఫ్లో నమూనాలను ఎలా అమలు చేయాలో చూద్దాం. ప్రతి ఉదాహరణ కొరకు Python మరియు .NET కోడ్‌ను పరిశీలిస్తాము.

### కేసు 1: ప్రాథమిక క్రమవారీ వర్క్‌ఫ్లో

ఇది అత్యంత సరళమైన నమూనా, ఒక ఏజెంట్ ఔట్‌పుట్ నేరుగా మరొకటి అందుకునే విధంగా ఉంటుంది. మన సందర్భంలో ఒక హోటల్ `FrontDesk` ఏజెంట్ ట్రావెల్ సిఫారసు చేస్తుంది, దీన్ని `Concierge` ఏజెంట్ సమీక్షిస్తుంది.

*ప్రాథమిక FrontDesk -> Concierge వర్క్‌ఫ్లో యొక్క డయాగ్రామ్.*

#### సందర్భ పరిచయం

ఒక ప్రయాణికుడు పారిస్‌లో సిఫారసు కోరాడు.

1.  సరళమైన `FrontDesk` ఏజెంట్ Louvre మ్యూజియం సందర్శించమని సూచిస్తుంది.
2.  `Concierge` ఏజెంట్, నిజమైన అనుభవాలను ప్రాధాన్యం ఇస్తూ, సూచనను సమీక్షించి మరొక ప్రదేశాన్ని సూచిస్తుంది.

#### Python అమలు విశ్లేషణ

Python ఉదాహరణలో, మొదట రెండు ఏజెంట్లను నిర్వచించి సృష్టిస్తాము, ప్రతి ఏజెంట్‌కు ప్రత్యేక సూచనలు ఉంటాయి.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# ఏజెంట్ పాత్రలు మరియు సూచనలు నిర్వచించండి
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# ఏజెంట్ ఉదాహరణలను సృష్టించండి
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

తరువాత, `WorkflowBuilder` ఉపయోగించి గ్రాఫ్ నిర్మించబడుతుంది. `front_desk_agent` ప్రారంభ పాయింట్ గా సెట్ చేయబడింది, మరియు దాని ఔట్‌పుట్ ను `reviewer_agent` కి కనెక్ట్ చేసే ఎడ్జ్ సృష్టించబడింది.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

చివరగా, మొదటి యూజర్ ప్రాంప్ట్ తో వర్క్‌ఫ్లో నడుపుతారు.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run వర్క్‌ఫ్లోను నడుపుతుంది; get_outputs() అవుట్పుట్ ఎగ్జిక్యూటర్ ఫలితాన్ని తిరిగి ఇస్తుంది.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) అమలు విశ్లేషణ

.NET అమలు చాలా సారూప్యమైన లాజిక్ అనుసరిస్తుంది. మొదట ఏజెంట్ల పేర్లు మరియు సూచనలకు కాన్స్‌టెంట్లు నిర్వచించబడతాయి.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

ఏజెంట్లు `AzureOpenAIClient` (Responses API) ద్వారా సృష్టించబడ్డాయి, మరియు తరువాత `WorkflowBuilder` ద్వారా `frontDeskAgent` నుండి `reviewerAgent`కి క్రమవారీ ప్రవాహాన్ని నిర్వచిస్తూ ఎడ్జ్ జోడించబడింది.

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

వర్క్‌ఫ్లో యూజర్ సందేశంతో నడుస్తుంది, ఫలితాలు స్ట్రీంగా వెనక్కి వస్తాయి.

### కేసు 2: బహుళ-దశ క్రమవారీ వర్క్‌ఫ్లో

ఈ నమూనా ప్రాథమిక క్రమాన్ని పొడగింపజేస్తుంది, మరిన్ని ఏజెంట్లు చేరతారు. ఇక్కడ అనేక దశల సవరణ లేదా మార్పిడి అవసరమైన ప్రాసెస్‌లకు అనుకూలంగా ఉంటుంది.

#### సందర్భ పరిచయం

ఒక యూజర్ లివింగ్ రూమ్ చిత్రం ఇస్తారు, ఫర్నిచర్ కొటేషన్ కోరుతారు.

1.  **సేల్స్-ఏజెంట్**: చిత్రంలోని ఫర్నిచర్ అంశాలను గుర్తించి జాబితా తయారు చేస్తుంది.
2.  **ప్రైస్-ఏజెంట్**: ఆ జాబితా ఆధారంగా బడ్జెట్, మిడ్-రేంజ్, ప్రీమియం ఎంపికల వివరాలతో ధర వివరాలను అందిస్తుంది.
3.  **కోటేషన్-ఏజెంట్**: ధర జాబితాను Markdown లో అధికారిక కోట్ డాక్యుమెంట్ గా రూపకల్పన చేస్తుంది.

*సేల్స్ -> ప్రైస్ -> కోట్ వర్క్‌ఫ్లో డయాగ్రామ్.*

#### Python అమలు విశ్లేషణ

మూడు ఏజెంట్లు నిర్వచించబడ్డాయి, ప్రతి ఒక ప్రత్యేక పాత్రలో. వర్క్‌ఫ్లో `add_edge` ఉపయోగించి క్ర‌మంగా `sales_agent` → `price_agent` → `quote_agent` గా రూపొందించబడింది.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# మూడు ప్రత్యేక ఏజెంట్లను సృష్టించండి
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# వరుస వర్క్‌ఫ్లోని నిర్మించండి
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ఇన్‌పుట్ ఒక `ChatMessage` అయి, ఇది టెక్స్ట్ మరియు చిత్రం URI ని కలిగి ఉంటుంది. ఫ్రేమ్‌వర్క్ ప్రతి ఏజెంట్ ఔట్‌పుట్ ను క్రమంగా తదుపరి ఏజెంట్కు ఇస్తుంది, చివరి కోట్ ఉత్పత్తి అవుతుంది.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# వాడుకరి సందేశం పాఠ్యం మరియు చిత్రం రెండింటినీ కలిగి ఉంది
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# వర్క్‌ఫ్లో నడపండి
events = await workflow.run(message)
```

#### .NET (C\#) అమలు విశ్లేషణ

.NET ఉదాహరణ Python వెర్షన్‌ను అనుసరిస్తుంది. మూడు ఏజెంట్లు (`salesagent`, `priceagent`, `quoteagent`) సృష్టించబడ్డాయి. `WorkflowBuilder` వారిని క్రమంగానూ లింక్ చేస్తుంది.

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

యూజర్ సందేశం చిత్ర డేటాతో (బైట్స్ లాగా) మరియు టెక్స్ట్ ప్రాంప్ట్ తో తయారవుతుంది. `InProcessExecution.RunStreamingAsync` పద్ధతి వర్క్‌ఫ్లో ప్రారంభించి స్ట్రీం నుండి తుది ఔట్‌పుట్‌ను క్యాప్చర్ చేస్తుంది.

### కేసు 3: సమకాలీన వర్క్‌ఫ్లో

ఇది పనులను సమకాలీనంగా నిర్వహించడానికి ఉపయోగించే నమూనా, సమయం ఆదా చేయడానికి. ఇది బహుళ ఏజెంట్ల "ఫ్యాన్-అవుట్" మరియు ఫలితాలను సంగ్రహించే "ఫ్యాన్-ఇన్" ను కలిగి ఉంటుంది.

#### సందర్భ పరిచయం

ఒక యూజర్ సియాటిల్ సవారీ ప్లాన్ చేయమని కోరారు.

1.  **డిస్పాచర్ (ఫ్యాన్-అవుట్)**: యూజర్ అభ్యర్థనను రెండు ఏజెంట్లకు సమానంగా పంపుతుంది.
2.  **రిసర్చర్-ఏజెంట్**: డిసెంబరు లో సియాటిల్ కోసం ఆక్సిటేషన్లు, వాతావరణం మరియు ముఖ్య అంశాలను పరిశోధిస్తుంది.
3.  **ప్లాన్-ఏజెంట్**: స్వతంత్రంగా రోజువారీ అవుట్లైన్ ప్రణాళిక తయారుచేస్తుంది.
4.  **అగ్రిగేటర్ (ఫ్యాన్-ఇన్)**: రెండింటి ఔట్‌పుట్లను కలిపి తుది ఫలితంగా అందిస్తుంది.

*రిసర్చర్ మరియు ప్లానర్ సమకాలీన వర్క్‌ఫ్లో డయాగ్రామ్.*

#### Python అమలు విశ్లేషణ

`ConcurrentBuilder` ఈ నమూనా సృష్టిని సులభతరం చేస్తుంది. మీరు పాల్గొనే ఏజెంట్లను జాబితా చేయాలి, బిల్డర్ ఆటోమేటిక్ గా ఫ్యాన్-అవుట్ మరియు ఫ్యాన్-ఇన్ లాజిక్ తయారు చేస్తుంది.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ఫ్యాన్-ఆషుట్/ఫ్యాన్-ఇన్ లాజిక్‌ని నిర్వహిస్తుంది
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# వర్క్‌ఫ్లోను నడపండి
events = await workflow.run("Plan a trip to Seattle in December")
```

ఫ్రేమ్‌వర్క్ `research_agent` మరియు `plan_agent` మధ్య సమాంతరంగా కొనసాగించటం నిర్ధారిస్తుంది, చివరి ఔట్‌పుట్లు జాబితాగా సంగ్రహించబడతాయి.

#### .NET (C\#) అమలు విశ్లేషణ

.NET లో ఈ నమూనాకు కాస్త స్పష్టమైన నిర్వచనం అవసరం. కస్టమ్ ఎగ్జిక్యూటర్లు (`ConcurrentStartExecutor` మరియు `ConcurrentAggregationExecutor`) ఫ్యాన్-అవుట్ మరియు ఫ్యాన్-ఇన్ లాజిక్ ని నిర్వహించడానికి సృష్టించబడ్డాయి.

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

తరువాత `WorkflowBuilder` ఈ కస్టమ్ ఎగ్జిక్యూటర్లు మరియు ఏజెంట్లతో గ్రాఫ్‌ను `AddFanOutEdge` మరియు `AddFanInEdge` తో నిర్మిస్తుంది.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### కేసు 4: పరిస్థితి ఆధారిత వర్క్‌ఫ్లో

పరిస్థితి ఆధారిత వర్క్‌ఫ్లోలు బ్రాంచింగ్ లాజిక్ ప్రవేశపెట్టడమ్, సిస్టమ్ మధ్యంతర ఫలితాల ఆధారంగా వేర్వేరు మార్గాలను ఎంచుకొనే అనుమతిస్తుంది.

#### సందర్భ పరిచయం

ఈ వర్క్‌ఫ్లో ఒక సాంకేతిక ట్యూటోరియల్ సృష్టి మరియు ప్రచురణను ఆటోమేటిక్ చేస్తుంది.

1.  **ఎవేంజలిస్టు-ఏజెంట్**: ఇవ్వబడిన అవుట్లైన్ మరియు URLs ఆధారంగా ట్యూటోరియల్ డ్రాఫ్ట్ రాస్తుంది.
2.  **కంటెంట్ రివ్యూయర్-ఏజెంట్**: డ్రాఫ్ట్‌ని సమీక్షిస్తుంది, పదాల సంఖ్య 200కు మించితే తనిఖీ చేస్తుంది.
3.  **పరిస్థితి శాఖ**:
* **ఆమోదిస్తే (`Yes`)**: వర్క్‌ఫ్లో `Publisher-Agent` కు ముందుగా ఉంటుంది.
* **న అంగీకరించకపోతే (`No`)**: వర్క్‌ఫ్లో ఆపు, తిరస్కరణ కారణాన్ని చూపిస్తుంది.
4.  **ప్రకాశక-ఏజెంట్**: డ్రాఫ్ట్ ఆమోదిస్తే Markdown ఫైల్లో కంటెంట్‌ను సేవ్ చేస్తుంది.

#### Python అమలు విశ్లేషణ

ఈ ఉదాహరణ ఒక కస్టమ్ ఫంక్షన్ `select_targets` ఉపయోగించి పరిస్థితి లాజిక్ ని అమలు చేస్తుంది. ఈ ఫంక్షన్ `add_multi_selection_edge_group` కు పాస്സ് చేయబడుతుంది మరియు సమీక్షకుడి ఔట్‌పుట్ `review_result` ఫీల్డ్ ఆధారంగా వర్క్‌ఫ్లో నడిపిస్తుంది.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ఈ ఫంక్షన్ సమీక్ష ఫలితాన్ని ఆధారంగా తదుపరి దశను నిర్ణయిస్తుంది
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # ఆమోదిస్తే, 'save_draft' ఎగ్జిక్యూటర్ కు ముందుకు వెళ్ళండి
        return [save_draft_id]
    else:
        # తిరస్కరించబడితే, విఫలమైందని నివేదిక ఇవ్వడానికి 'handle_review' ఎగ్జిక్యూటర్ కు వెళ్ళండి
        return [handle_review_id]

# వర్క్‌ఫ్లో బిల్డర్ మార్గనిర్దేశంకు సెలక్షన్ ఫంక్షన్‌ను ఉపయోగిస్తుంది
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # బహు-ఎంపిక ఎడ్జ్ నిబంధనామయమైన తర్కాన్ని అమలు చేస్తుంది
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

కస్టమ్ ఎగ్జిక్యూటర్లు `to_reviewer_result` వంటి JSON ఔట్‌పుట్‌ను స్ట్రాంగ్-టైప్ ఆబ్జెక్టులుగా మార్చి సెలెక్షన్ ఫంక్షన్ పరిశీలించేందుకు అందుబాటులో ఉంచుతాయి.

#### .NET (C\#) అమలు విశ్లేషణ

.NET వెర్షన్ సమాన విధానాన్ని అనుసరిస్తుంది, ఒక షరతు ఫంక్షన్ ఉపయోగిస్తుంది. `Func<object?, bool>` నిర్వచించబడుతుంది `ReviewResult` ఆబ్జెక్ట్ యొక్క `Result` ప్రాపర్టీని తనిఖీ చేయడానికి.

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

`AddEdge` పద్ధతి యొక్క `condition` పారామీటర్ ద్వారా `WorkflowBuilder` బ్రాంచింగ్ మార్గం సృష్టిస్తుంది. `GetCondition(expectedResult: "Yes")` నిజం అయితే కేవలం `publishExecutor` వైపు హోదా అనుసరిస్తుంది. లేకుంటే `sendReviewerExecutor` కు వెళ్లుతుంది.

## ముగింపు

మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ వర్క్‌ఫ్లో కాంప్లెక్స్, మల్టీ-ఏజెంట్ వ్యవస్థలను సమన్వయం చేసుకోవడానికి ఒక హృదయపూర్వక మరియు సడలనివ్వని ఆధారం అందిస్తుంది. దాని గ్రాఫ్-ఆధారిత ఆర్కిటెక్చర్ మరియు ప్రధాన భాగాలను ఉపయోగించి, డెవలపర్లు Python మరియు .NET రెండింటిలోనూ సాంకేతికంగా సమర్థవంతమైన వర్క్‌ఫ్లోలను డిజైన్ మరియు అమలు చేయగలరు. మీ అనువర్తనానికి తక్కువ క్రమవారీ ప్రాసెసింగ్ కావాలనుకుంటే, సమాంతర నిర్వహణ కావాలనుకుంటే లేదా డైనమిక్ షరతు లాజిక్ అవసరం ఉన్నా, ఈ ఫ్రేమ్‌వర్క్ శక్తివంతమైన, స్కేలబుల్ మరియు టైప్-భద్ర ఆర్టిఫిషియల్ ఇంటెలిజెన్స్ ఆధారిత పరిష్కారాలను నిర్మించడానికి సాధనాలు అందిస్తుంది.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->