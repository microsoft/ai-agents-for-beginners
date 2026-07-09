# Microsoft Agent Framework Workflow తో బహు-ఏజెంట్ అప్లికేషన్లు నిర్మాణం

ఈ పాఠం Microsoft Agent Framework ఉపయోగించి బహు-ఏజెంట్ అప్లికేషన్లు అర్థం చేసుకోవడం మరియు కట్టడం ఎలా అనేది మీకు మార్గదర్శనం చేస్తుంది. మేము బహు-ఏజెంట్ సిస్టమ్స్ యొక్క ప్రాధమిక భావాలపై దృష్టి సారించబోతున్నాము, ఫ్రేమ్‌వర్క్ యొక్క Workflow భాగం యొక్క నిర్మాణాన్ని పరిశీలిస్తాము, మరియు వివిధ workflow నమూనాలకు Python మరియు .NET లో వ్యావహారిక ఉదాహరణలను చూడబోతున్నాము.

## 1\. బహు-ఏజెంట్ సిస్టమ్స్ అర్థం చేసుకోవడం

ఒక AI ఏజెంట్ సాధారణ Large Language Model (LLM) సామర్థ్యాలను మించి పనిచేసే సిస్టమ్. ఇది తన పరిసరాలను గ్రహించి, నిర్ణయాలు తీసుకొని, నిర్దిష్ట లక్ష్యాలను సాధించడానికి చర్యలు తీసుకుంటుంది. బహు-ఏజెంట్ సిస్టమ్ అనగా అనేక ఏజెంట్లు కలిసి పనిచేసి ఒక ఏకైక ఏజెంట్ చే చేయడం కష్టమైన లేదా అసాధ్యమైన సమస్యను పరిష్కరిస్తాయి.

### సాధారణ అప్లికేషన్ సందర్భాలు

  * **సంకీర్ణ సమస్య పరిష్కారం**: ఒక పెద్ద పనిని (ఉదాహరణకు, కంపెనీ విషయంలో ఒక ఈవెంట్ పన్నడం) అనుభవజ్ఞుల ఏజెంట్లు చేత చిన్న ఉపపనులుగా విభజించడం (ఉదా: బడ్జెట్ ఏజెంట్, లాజిస్టిక్స్ ఏజెంట్, మార్కెటింగ్ ఏజెంట్).
  * **వర్చువల్ అసిస్టెంట్లు**: ప్రధాన అసిస్టెంట్ ఏజెంట్ పనులను షెడ్యూలింగ్, పరిశోధన, బుకింగ్ వంటి విభాగాలకు ఇతర అనుభవజ్ఞుల ఏజెంట్లకు అప్పగించడం.
  * **ఆటోమేటెడ్ కంటెంట్ సృష్టి**: ఒక ఏజెంట్ కంటెంట్ డ్రాఫ్ట్ చేయడం, మరొక ఏజెంట్ దాన్ని సమీక్షించడం (ఖచ్చితత్వం, శైలి కోసం), మరియు మూడవ ఏజెంట్ ప్రచురించడం.

### బహు-ఏజెంట్ నమూనాలు

బహు-ఏజెంట్ సిస్టమ్స్ అనేక నమూనాలలో ఏర్పాటు చేయబడవచ్చు, ఇవి వారు ఎలా పరస్పరం సహకరిస్తారో నిర్ణయిస్తాయి:

  * **టీక్రమాత్మక (సీక్వెన్షియల్)**: ఏజెంట్లు ముందుగా నిర్దిష్ట క్రమంలో పని చేస్తాయి, అలా ఒక ఏజెంట్ అవుట్పుట్ తరువాతి ఏజెంట్ ఇన్పుట్ అవుతుంది.
  * **సమాంతర (కన్‌కరెంట్)**: ఏజెంట్లు ఒక పని విభాగాలలో స్వతంత్రంగా సమాంతరంగా పనిచేస్తాయి, మరియు చివర్లో వారి ఫలితాలను సమాహరించవచ్చు.
  * **నీతి ఆధారిత (కండిషనల్)**: వర్క్‌ఫ్లో ఏజెంట్ అవుట్పుట్ ఆధారంగా వివిధ మార్గాలను అనుసరిస్తుంది, ఇది ఒక if-then-else స్టేట్‌మెంట్ లాగా ఉంటుంది.

## 2\. Microsoft Agent Framework Workflow నిర్మాణం

ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క వర్క్‌ఫ్లో వ్యవస్థ అనేది అనేక ఏజెంట్ల మధ్య సమ్లాభక చర్యలు నిర్వహించడానికి రూపొందించిన ఆధునిక సమన్వయం ఇంజిన్. ఇది [Pregel-శైలీ అమలు నమూనా](https://kowshik.github.io/JPregel/pregel_paper.pdf) ఆధారపడిన గ్రాఫ్-ఆధారిత నిర్మాణంపై ఉంటుంది, ఇందులో "సూపర్‌స్టెప్స్" అని పిలవబడే సమకాలీకరించిన దశల్లో ప్రాసెసింగ్ జరుగుతుంది.

### ప్రాథమిక భాగాలు

నిర్మాణం మూడు ప్రధాన భాగాల నుండి ఉంటుంది:

1.  **ఎగ్జిక్యూటర్లు**: ఇవి ప్రాథమిక ప్రాసెసింగ్ యూనిట్లు. మా ఉదాహరణల్లో, `Agent` ఒక ఎగ్జిక్యూటర్ టైపు. ప్రతి ఎగ్జిక్యూటర్ పంపిన సందేశ రకానికి అనుగుణంగా స్వయంచాలకంగా పిలవబడే అనేక సందేశ హ్యాండ్లర్లు కలిగి ఉంటాయి.
2.  **ఎడ్జెస్**: మెసేజిలు ఎగ్జిక్యూటర్ల మధ్య ప్రయాణించే మార్గాన్ని నిర్వచిస్తాయి. ఎడ్జెస్ కు షరతులు ఉండవచ్చు, ఇవి డైనమిక్ రూటింగ్ కి అనుమతిస్తాయి.
3.  **వర్క్‌ఫ్లో**: ఈ భాగం మొత్తం ప్రక్రియను సమన్వయపరుస్తుంది, ఎగ్జిక్యూటర్లు, ఎడ్జెస్ మరియు మొత్తం అమలును నిర్వహిస్తుంది. సందేశాలు సరిగా ప్రాసెస్ అవుతున్నాయో చూసుకోడానికి ఈ వర్క్‌ఫ్లో ఈవెంట్లను స్ట్రీమ్ చేస్తుంది.

*వర్క్‌ఫ్లో వ్యవస్థలో ప్రాథమిక భాగాలను చూపించే ఒక చిహ్నం.*

ఈ నిర్మాణం సీక్వెన్షియల్ చైన్స్, ఫ్యాన్-అవుట్/ఫ్యాన్-ఇన్ సమాంతర ప్రాసెసింగ్, మరియు నీతి ఆధారిత స్విచ్-కేస్ లాజిక్ వంటి ప్రాథమిక నమూనాలకు ఉపయోగించి బలంగా మరియు స్కేలబుల్ అప్లికేషన్లను కట్టడానికి సహకరిస్తుంది.

## 3\. ప్రాక్టికల్ ఉదాహరణలు మరియు కోడ్ విశ్లేషణ

ఇప్పుడు, ఫ్రేమ్‌వర్క్ ఉపయోగించి వివిధ వర్క్‌ఫ్లో నమూనాలను ఎలా అమలు చేయాలో చూద్దాం. ప్రతి ఉదాహరణకు Python మరియు .NET కోడ్‌ను పరిశీలిస్తాము.

### కేసు 1: ప్రాథమిక సీక్వెన్షియల్ వర్క్‌ఫ్లో

ఇది సరళమైన నమూనా, ఒక ఏజెంట్ అవుట్పుట్ నేరుగా మరొకదానికి ఇవ్వబడుతుంది. మన పరిస్థితి లో ఒక హోటల్ `FrontDesk` ఏజెంట్ ప్రయాణ సిఫారసును చేస్తుంది, దానిని తరువాత `Concierge` ఏజెంట్ సమీక్షిస్తుంది.

*ప్రాథమిక FrontDesk -> Concierge వర్క్‌ఫ్లో యొక్క చిహ్నం.*

#### పరిస్థితి నేపథ్యం

ఒక ప్రయాణికుడు పారిస్ లో సిఫారసు కోసం అడుగుతున్నాడు.

1.  సంక్షిప్తత కోసం రూపొందించిన `FrontDesk` ఏజెంట్ లూవర్ మ్యూజియం సందర్శించాలని సిఫారసు చేస్తుంది.
2.  ప్రామాణిక అనుభవాల‌కు ప్రాధాన్యత ఇచ్చే `Concierge` ఏజెంట్ ఈ సిఫారసును స్వీకరించి సమీక్షించి మరింత స్థానిక, తక్కువ టూరిస్టు గల ప్రత్యామ్నాయాన్ని సూచిస్తుంది.

#### Python అమలు విశ్లేషణ

Python ఉదాహరణలో మొదట రెండు ఏజెంట్లను ప్రత్యేక ఉత్తర్వులతో నిర్వచించి సൃഷ్ట్ చేయడం జరుగుతుంది.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# ఏజెంట్ పాత్రలు మరియు సూచనలను నిర్వచించండి
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
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

తరువాత, `WorkflowBuilder` గ్రాఫ్ ను నిర్మించడానికి ఉపయోగిస్తారు. `front_desk_agent` ప్రారంభ పాయింట్ గా సెట్ చేయబడింది, మరియు దాని అవుట్పుట్ ను `reviewer_agent` కి కలిపేందుకు ఒక ఎడ్జ్ సృష్టించబడుతుంది.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

చివరగా, ప్రారంభ యూజర్ ప్రాంప్ట్ తో వర్క్‌ఫ్లో అమలు చేయబడుతుంది.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run వర్క్‌ఫ్లోను అమలు చేస్తుంది; get_outputs() అవుట్పుట్ ఎగ్జిక్యూటర్ యొక్క ఫలితాన్ని అందిస్తుంది.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) అమలు విశ్లేషణ

.NET అమలు చాలా సమానమైన తర్కాన్ని అనుసరిస్తుంది. మొదట ఏజెంట్‌ల పేర్లు మరియు ఉత్తర్వులకు స్థిరాంకులు నిర్వచిస్తారు.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`AzureOpenAIClient` (Responses API) ఉపయోగించి ఏజెంట్లు సృష్టించబడతాయి, ఆపై `WorkflowBuilder` సీక్వెన్షియల్ ఫ్లో నిర్వచిస్తూ `frontDeskAgent` నుండి `reviewerAgent` కి ఎడ్జ్ ను జత చేస్తుంది.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

వర్క్‌ఫ్లో ఆపై యూజర్ సందేశంతో నడపబడుతుంది, ఫలితాలు స్ట్రీమ్ ద్వారా తిరిగి పంపబడతాయి.

### కేసు 2: బహుస్థాయి సీక్వెన్షియల్ వర్క్‌ఫ్లో

ఈ నమూనా ప్రాథమిక క్రమాన్ని విస్తరించి ఎక్కువ ఏజెంట్లను చేరుస్తుంది. ఇది అనేక దశల్లో పరిమార్చు లేదా రూపాంతర చర్యల్లో అవసరమైన ప్రక్రియలకు అనుకూలంగా ఉంటుంది.

#### పరిస్థితి నేపథ్యం

ఒక యూజర్ లివింగ్ రూమ్ ఇమేజ్ ని ఇస్తాడు మరియు ఫర్నిచర్ ధర కోసం అడుగుతాడు.

1.  **సేల్స్-ఏజెంట్**: ఇమేజ్లో ఫర్నిచర్ వస్తువులను గుర్తించి ఒక జాబితాను తయారు చేస్తుంది.
2.  **ప్రైస్-ఏజెంట్**: వస్తువుల జాబితా తీసుకుని బడ్జెట్, మధ్యస్థాయి మరియు ప్రీమియం ఎంపికలతో సవिस्तర ధర వివరాలను అందిస్తుంది.
3.  **కొట్-ఏజెంట్**: ధరల జాబితాను స్వీకరించి Markdown ఫార్మాట్ లో ఒక అధికారిక కనిష్టాన్ని రూపొందిస్తుంది.

*సేల్స్ -> ప్రైస్ -> కొట్ వర్క్‌ఫ్లో యొక్క చిహ్నం.*

#### Python అమలు విశ్లేషణ

మూడు ఏజెంట్లు నిర్వచించబడ్డాయి, ప్రతి ఒక్కటి ప్రత్యేక పాత్రతో. వర్క్‌ఫ్లోను `add_edge` ఉపయోగించి లంకె కట్టబడ్డది: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# మూడు ప్రత్యేక ఏజెంట్లను సృష్టించండి
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# అనుక్రమిక వర్క్‌ఫ్లో ను నిర్మించండి
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ఇన్‌పుట్ ఒక `ChatMessage` గా ఉంటుంది, దీనిలో పాఠ్యం మరియు ఇమేజ్ URI రెండూ ఉంటాయి. ఫ్రేమ్‌వర్క్ ప్రతి ఏజెంట్ అవుట్పుట్ ను తరువాతి ఏజెంట్ కు క్రమంగా పంపుతుంది, చివరి కొటును సృష్టించే వరకు.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# యూజర్ సందేశంలో పాఠ్యము మరియు చిత్రం రెండూ ఉన్నాయి
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

.NET ఉదాహరణ Python వెర్షన్‌ను ప్రతిబింబిస్తుంది. మూడు ఏజెంట్లు (`salesagent`, `priceagent`, `quoteagent`) సృష్టించబడ్డాయి. `WorkflowBuilder` వారిని సీక్వెన్షియల్ గా లింక్ చేస్తుంది.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent priceagent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent quoteagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

యూజర్ సందేశాన్ని ఇమేజ్ డేటాతో (బైట్స్ రూపంలో) మరియు టెక్స్ట్ ప్రాంప్ట్ తో నిర్మిస్తారు. `InProcessExecution.StreamAsync` అనే పద్ధతి వర్క్‌ఫ్లోను మొదలుపెడుతుంది, మరియు చివరి అవుట్పుట్ స్ట్రీమ్ నుండి సేకరిస్తారు.

### కేసు 3: సమాంతర వర్క్‌ఫ్లో

ఈ నమూనా పనులు సమయాన్ని ఆదా చేయడానికి సమాంతరంగా చేయగలిగినప్పుడు ఉపయోగిస్తారు. ఇది అనేక ఏజెంట్లకు "ఫ్యాన్-అవుట్" మరియు ఫలితాలను ఏకదృశ్యంగా సేకరించడం కోసం "ఫ్యాన్-ఇన్" కలిగి ఉంటుంది.

#### పరిస్థితి నేపథ్యం

ఒక యూజర్ సియాటిల్ ప్రయాణాన్ని ప్లాన్ చేయమని అడుగుతున్నాడు.

1.  **డిస్పాచర్ (ఫ్యాన్-అవుట్)**: యూజర్ అభ్యర్ధన రెండు ఏజెంట్లకు ఒకేసారి పంపబడుతుంది.
2.  **రిసెర్చర్-ఏజెంట్**: డిసెంబర్ నెలలో సియాటిల్ ఆకర్షణలు, వాతావరణం మరియు ముఖ్యమైన అంశాలపై పరిశోధన చేస్తుంది.
3.  **ప్లాన్-ఏజెంట్**: స్వతంత్రంగా ఒక రోజువారీ ప్రయాణ విశ్లేషణను తయారు చేస్తుంది.
4.  **ఏగ్రిగేటర్ (ఫ్యాన్-ఇన్)**: రిసెర్చర్ మరియు ప్లానర్ యొక్క అవుట్పుట్లను సేకరించి చివరి ఫలితంగా సమర్పిస్తుంది.

*సమాంతర రిసెర్చర్ మరియు ప్లానర్ వర్క్‌ఫ్లో యొక్క చిహ్నం.*

#### Python అమలు విశ్లేషణ

`ConcurrentBuilder` ఈ నమూనా సృష్టింపును సులభం చేస్తుంది. మీరు పాల్గొనేవారిని జాబితా చేస్తే, బిల్డర్ అవసరమైన ఫ్యాన్-అవుట్ మరియు ఫ్యాన్-ఇన్ లాజిక్ ని స్వయంచాలకంగా సృష్టిస్తుంది.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ఫ్యాన్-అవుట్/ఫ్యాన్-ఇన్ లాజిక్‌ను నిర్వహిస్తుంది
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# వర్క్‌ఫ్లోని నడపండి
events = await workflow.run("Plan a trip to Seattle in December")
```

ఫ్రేమ్‌వర్క్ `research_agent` మరియు `plan_agent` ను సమాంతరంగా అమలు చేస్తుంది, మరియు వారి తుది అవుట్పుట్లను జాబితాగా సేకరిస్తుంది.

#### .NET (C\#) అమలు విశ్లేషణ

.NET లో, ఈ నమూనా మరింత స్పష్టమైన నిర్వచనాన్ని అవసరం చేసుకుంటుంది. ఫ్యాన్-అవుట్ మరియు ఫ్యాన్-ఇన్ లాజిక్ కు అనుగుణంగా మీకు ప్రత్యేక ఎగ్జిక్యూటర్లుగా `ConcurrentStartExecutor` మరియు `ConcurrentAggregationExecutor` సృష్టించాలి.

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

తరువాత `WorkflowBuilder` ఈ కస్టమ్ ఎగ్జిక్యూటర్లను మరియు ఏజెంట్లను ఉపయోగించి గ్రాఫ్ తయారు చేయడానికి `AddFanOutEdge` మరియు `AddFanInEdge` పద్ధతులను ఉపయోగిస్తుంది.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### కేసు 4: నీతి ఆధారిత వర్క్‌ఫ్లో

నీతి ఆధారిత వర్క్‌ఫ్లోలు బ్రాంచింగ్ లాజిక్ ని పరిచయం చేస్తాయి, దీనివల్ల వ్యవస్థ మధ్యంతర ఫలితాల ఆధారంగా వేరే మార్గాలను ముందుకు తీసుకుపోతుంది.

#### పరిస్థితి నేపథ్యం

ఈ వర్క్‌ఫ్లో ఒక సాంకేతిక పాఠ్యాన్ని సృష్టించడం మరియు ప్రచురించడం ను ఆటోమేటిక్ చేస్తుంది.

1.  **ఎవ్యాంజెలిస్ట్-ఏజెంట్**: ఒక ఇచ్చిన రూపకల్పన మరియు URLs ఆధారంగా పాఠ్య డ్రాఫ్ట్ ను రచించును.
2.  **కంటెంట్ రివ్యూ-ఏజెంట్**: డ్రాఫ్ట్ ను సమీక్షిస్తుంది. ఇది పదాల సంఖ్య 200కు పైగా ఉన్నదా అనే దాన్ని తనిఖీ చేస్తుంది.
3.  **నీతి ఆధారిత శాఖ**:
      * **ఆమోదించబడ్డట్లయితే (`Yes`)**: వర్క్‌ఫ్లో `Publisher-Agent` వైపు కొనసాగుతుంది.
      * **నిరాకరించబడ్డట్లయితే (`No`)**: వర్క్‌ఫ్లో ఆగిపోతోంది మరియు తిరస్కరణ కారణాన్ని అవుట్పుట్ చేస్తుంది.
4.  **పబ్లిషర్-ఏజెంట్**: డ్రాఫ్ట్ ఆమోదించబడితే, ఈ ఏజెంట్ కంటెంట్ ను Markdown ఫైల్ గా సురక్షితం చేస్తుంది.

#### Python అమలు విశ్లేషణ

ఈ ఉదాహరణ కన్సిషనల్ లాజిక్ అమలు చేయటానికి ఒక కస్టమ్ ఫంక్షన్ `select_targets` ఉపయోగించబడింది. ఈ ఫంక్షన్ `add_multi_selection_edge_group` కు పాసవైయబడుతుంది మరియు సమీక్షకుడి అవుట్పుట్ నుండి `review_result` ఫీల్డ్ ఆధారంగా వర్క్‌ఫ్లో ని దిశానిర్దేశం చేస్తుంది.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# సమీక్ష ఫలితంపై ఆధారపడి తదుపరి దశను ఈ ఫంక్షన్ నిర్ణయిస్తుంది
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # ఆమోదమైతే, 'save_draft' ఎగ్జిక్యూటర్‌కు వెళ్లండి
        return [save_draft_id]
    else:
        # విభజించబడితే, విఫలతను నివేదించడానికి 'handle_review' ఎగ్జిక్యూటర్‌కు వెళ్లండి
        return [handle_review_id]

# వర్క్‌ఫ్లో బిల్డర్ మార్గనిర్దేశకంగా సెలక్షన్ ఫంక్షన్‌ను వాడుతుంది
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # బహు-ఎంచుకోమయిన ఎడ్జ్ షరతు లాజిక్‌ను అమలు చేస్తుంది
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

JSON అవుట్పుట్ ను ఎజెంట్ల నుండి పార్స్ చేసి దరఖాస్తును గట్టి టైపు అంశాలుగా మార్చే `to_reviewer_result` వంటి కస్టమ్ ఎగ్జిక్యూటర్లను ఉపయోగిస్తారు, ఇవి సెలెక్షన్ ఫంక్షన్ పరిశీలించగలవు.

#### .NET (C\#) అమలు విశ్లేషణ

.NET వెర్షన్ కూడా సారూప్య విధానాన్ని ఉపయోగిస్తుంది, ఒక షరాను తనిఖీ చేసే `Func<object?, bool>` నిర్వచిస్తారు, ఇది `ReviewResult` ఆబ్జెక్ట్ యొక్క `Result` గుణాన్ని చూస్తుంది.

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

`AddEdge` పద్ధతి యొక్క `condition` పారామీటర్ `WorkflowBuilder` కు బ్రాంచ్ మార్గాన్ని సృష్టించడానికి అనుమతిస్తుంది. షరతు `GetCondition(expectedResult: "Yes")` నిజం అయితే వర్క్‌ఫ్లో `publishExecutor` వైపు వెళ్తుంది. లేతగా అయితే, అది `sendReviewerExecutor` వైపు వెళ్తుంది.

## సారాంశం

Microsoft Agent Framework Workflow అనేది సంక్లిష్టమైన బహు-ఏజెంట్ సిస్టమ్స్ ను సమన్వయపరచటానికి బలమైన మరియు అనుకూలమైన పునాది అందిస్తుంది. దీని గ్రాఫ్-ఆధారిత నిర్మాణం మరియు ప్రాథమిక భాగాలను ఉపయోగించి డెవలపర్లు Python మరియు .NET రెండింటిలోనే సొపానపూర్వక వర్క్‌ఫ్లోలను రూపకల్పన చేయవచ్చు మరియు అమలు చేయవచ్చు. మీ అప్లికేషన్ సరళమైన సీక్వెన్షియల్ ప్రాసెసింగ్, సమాంతర అమలయు లేదా డైనమిక్ నీతి ఆధారిత లాజిక్ అవసరం అయినా, ఫ్రేమ్‌వర్క్ శక్తివంతమైన, స్కేలబుల్ మరియు టైప్-సేఫ్ AI ఆధారిత పరిష్కారాలను నిర్మించడానికి అవసరమైన సాధనాలను అందిస్తుంది.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->