<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b39c052ef109db90ad9251183791e2d6",
  "translation_date": "2025-12-03T16:13:13+00:00",
  "source_file": "08-multi-agent/code_samples/workflows-agent-framework/README.md",
  "language_code": "te"
}
-->
# మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ వర్క్‌ఫ్లోతో మల్టీ-ఏజెంట్ అప్లికేషన్ల నిర్మాణం

ఈ ట్యుటోరియల్ మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ ఉపయోగించి మల్టీ-ఏజెంట్ అప్లికేషన్లను అర్థం చేసుకోవడం మరియు నిర్మించడంలో మీకు మార్గనిర్దేశం చేస్తుంది. మల్టీ-ఏజెంట్ సిస్టమ్స్ యొక్క ప్రధాన భావనలను అన్వేషించి, ఫ్రేమ్‌వర్క్ యొక్క వర్క్‌ఫ్లో భాగం ఆర్కిటెక్చర్‌లో లోతుగా ప్రవేశించి, Python మరియు .NET లో వివిధ వర్క్‌ఫ్లో నమూనాల కోసం ప్రాక్టికల్ ఉదాహరణలను పరిశీలిస్తాము.

## 1\. మల్టీ-ఏజెంట్ సిస్టమ్స్ అర్థం చేసుకోవడం

ఒక AI ఏజెంట్ అనేది సాధారణ లార్జ్ లాంగ్వేజ్ మోడల్ (LLM) సామర్థ్యాలను మించి పనిచేసే వ్యవస్థ. ఇది తన పరిసరాలను గ్రహించగలదు, నిర్ణయాలు తీసుకోగలదు, మరియు నిర్దిష్ట లక్ష్యాలను సాధించడానికి చర్యలు తీసుకోగలదు. మల్టీ-ఏజెంట్ సిస్టమ్ అనేది ఈ ఏజెంట్లలో అనేకమంది కలిసి ఒకే ఏజెంట్ చేయలేని లేదా చేయడం కష్టమైన సమస్యను పరిష్కరించడానికి సహకరించే వ్యవస్థ.

### సాధారణ అప్లికేషన్ సన్నివేశాలు

  * **సంక్లిష్ట సమస్యల పరిష్కారం**: పెద్ద పనిని (ఉదా: కంపెనీ-వ్యాప్తంగా ఈవెంట్ ప్లానింగ్) చిన్న ఉపపనులుగా విభజించడం, ప్రత్యేకత కలిగిన ఏజెంట్లచే నిర్వహించబడుతుంది (ఉదా: బడ్జెట్ ఏజెంట్, లాజిస్టిక్స్ ఏజెంట్, మార్కెటింగ్ ఏజెంట్).
  * **వర్చువల్ అసిస్టెంట్స్**: ఒక ప్రాథమిక అసిస్టెంట్ ఏజెంట్ షెడ్యూలింగ్, రీసెర్చ్, బుకింగ్ వంటి పనులను ఇతర ప్రత్యేకత కలిగిన ఏజెంట్లకు అప్పగిస్తుంది.
  * **ఆటోమేటెడ్ కంటెంట్ క్రియేషన్**: ఒక ఏజెంట్ కంటెంట్‌ను డ్రాఫ్ట్ చేస్తుంది, మరొకటి దానిని ఖచ్చితత్వం మరియు టోన్ కోసం సమీక్షిస్తుంది, మరియు మూడవది దానిని ప్రచురిస్తుంది.

### మల్టీ-ఏజెంట్ నమూనాలు

మల్టీ-ఏజెంట్ సిస్టమ్స్ అనేక నమూనాలలో ఏర్పాటు చేయబడవచ్చు, ఇవి అవి ఎలా పరస్పర చర్యలు చేస్తాయో నిర్ణయిస్తాయి:

  * **సీక్వెన్షియల్**: ఏజెంట్లు ముందుగా నిర్ణయించిన క్రమంలో పనిచేస్తారు, అసెంబ్లీ లైన్ లాగా. ఒక ఏజెంట్ యొక్క అవుట్‌పుట్ తదుపరి ఏజెంట్‌కు ఇన్‌పుట్‌గా మారుతుంది.
  * **కంకరెంట్**: ఏజెంట్లు ఒక పనిలోని వివిధ భాగాలపై సమాంతరంగా పనిచేస్తారు, మరియు వారి ఫలితాలు చివరలో సమీకరించబడతాయి.
  * **కండిషనల్**: వర్క్‌ఫ్లో ఏజెంట్ అవుట్‌పుట్ ఆధారంగా వివిధ మార్గాలను అనుసరిస్తుంది, if-then-else స్టేట్‌మెంట్ లాగా.

## 2\. మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ వర్క్‌ఫ్లో ఆర్కిటెక్చర్

ఏజెంట్ ఫ్రేమ్‌వర్క్ యొక్క వర్క్‌ఫ్లో సిస్టమ్ అనేది అనేక ఏజెంట్ల మధ్య సంక్లిష్ట పరస్పర చర్యలను నిర్వహించడానికి రూపొందించిన అధునాతన ఆర్కెస్ట్రేషన్ ఇంజిన్. ఇది [Pregel-శైలి ఎగ్జిక్యూషన్ మోడల్](https://kowshik.github.io/JPregel/pregel_paper.pdf) పై నిర్మించబడిన గ్రాఫ్-ఆధారిత ఆర్కిటెక్చర్, ఇక్కడ ప్రాసెసింగ్ "సూపర్‌స్టెప్స్" అని పిలువబడే సమకాలీన దశల్లో జరుగుతుంది.

### ప్రధాన భాగాలు

ఆర్కిటెక్చర్ మూడు ప్రధాన భాగాలుగా ఉంటుంది:

1.  **ఎగ్జిక్యూటర్లు**: ఇవి ప్రాథమిక ప్రాసెసింగ్ యూనిట్లు. మా ఉదాహరణలలో, `Agent` అనేది ఒక రకమైన ఎగ్జిక్యూటర్. ప్రతి ఎగ్జిక్యూటర్‌కు అనేక మెసేజ్ హ్యాండ్లర్లు ఉండవచ్చు, ఇవి స్వీకరించిన మెసేజ్ రకంపై ఆధారపడి ఆటోమేటిక్‌గా ఆహ్వానించబడతాయి.
2.  **ఎడ్జ్‌లు**: ఇవి ఎగ్జిక్యూటర్ల మధ్య మెసేజ్‌లు తీసుకునే మార్గాన్ని నిర్వచిస్తాయి. ఎడ్జ్‌లకు షరతులు ఉండవచ్చు, వర్క్‌ఫ్లో గ్రాఫ్ ద్వారా సమాచారాన్ని డైనమిక్‌గా రూట్ చేయడానికి వీలు కల్పిస్తుంది.
3.  **వర్క్‌ఫ్లో**: ఈ భాగం మొత్తం ప్రక్రియను ఆర్కెస్ట్రేట్ చేస్తుంది, ఎగ్జిక్యూటర్లు, ఎడ్జ్‌లు, మరియు మొత్తం ఎగ్జిక్యూషన్ ఫ్లోను నిర్వహిస్తుంది. ఇది మెసేజ్‌లు సరైన క్రమంలో ప్రాసెస్ చేయబడేలా చూసుకుంటుంది మరియు పరిశీలన కోసం ఈవెంట్లను స్ట్రీమ్ చేస్తుంది.

*వర్క్‌ఫ్లో సిస్టమ్ యొక్క ప్రధాన భాగాలను చూపించే ఒక డయాగ్రామ్.*

ఈ నిర్మాణం సీక్వెన్షియల్ చైన్స్, ఫ్యాన్-అవుట్/ఫ్యాన్-ఇన్ వంటి ప్రాథమిక నమూనాలను ఉపయోగించి, మరియు కండిషనల్ ఫ్లోల కోసం స్విచ్-కేస్ లాజిక్ వంటి బలమైన మరియు స్కేలబుల్ అప్లికేషన్లను నిర్మించడానికి అనుమతిస్తుంది.

## 3\. ప్రాక్టికల్ ఉదాహరణలు మరియు కోడ్ విశ్లేషణ

ఇప్పుడు, ఫ్రేమ్‌వర్క్ ఉపయోగించి వివిధ వర్క్‌ఫ్లో నమూనాలను ఎలా అమలు చేయాలో అన్వేషిద్దాం. ప్రతి ఉదాహరణ కోసం Python మరియు .NET కోడ్‌ను పరిశీలిస్తాము.

### కేస్ 1: బేసిక్ సీక్వెన్షియల్ వర్క్‌ఫ్లో

ఇది అత్యంత సరళమైన నమూనా, ఇక్కడ ఒక ఏజెంట్ అవుట్‌పుట్ నేరుగా మరొకదానికి పంపబడుతుంది. మా సన్నివేశం ఒక హోటల్ `FrontDesk` ఏజెంట్‌ను కలిగి ఉంది, ఇది ట్రావెల్ సిఫార్సును చేస్తుంది, దీన్ని `Concierge` ఏజెంట్ సమీక్షిస్తుంది.

*బేసిక్ FrontDesk -\> Concierge వర్క్‌ఫ్లో డయాగ్రామ్.*

#### సన్నివేశం నేపథ్యం

ఒక ప్రయాణికుడు పారిస్‌లో సిఫార్సు కోసం అడుగుతాడు.

1.  `FrontDesk` ఏజెంట్, సంక్షిప్తత కోసం రూపొందించబడింది, లూవ్ర్ మ్యూజియం సందర్శనను సూచిస్తుంది.
2.  `Concierge` ఏజెంట్, ప్రామాణిక అనుభవాలను ప్రాధాన్యత ఇస్తుంది, ఈ సూచనను స్వీకరిస్తుంది. ఇది సిఫార్సును సమీక్షించి, మరింత స్థానిక, తక్కువ పర్యాటక ప్రత్యామ్నాయాన్ని సూచిస్తుంది.

#### Python అమలు విశ్లేషణ

Python ఉదాహరణలో, మేము మొదట రెండు ఏజెంట్లను నిర్వచించి సృష్టిస్తాము, ప్రతి ఒక్కటి ప్రత్యేకమైన సూచనలతో.

```python
# 01.python-ఏజెంట్-ఫ్రేమ్‌వర్క్-వర్క్‌ఫ్లో-ghmodel-బేసిక్.ipynb

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
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

తదుపరి, `WorkflowBuilder` గ్రాఫ్‌ను నిర్మించడానికి ఉపయోగించబడుతుంది. `front_desk_agent` ప్రారంభ బిందువుగా సెట్ చేయబడుతుంది, మరియు దాని అవుట్‌పుట్‌ను `reviewer_agent` కు కనెక్ట్ చేయడానికి ఒక ఎడ్జ్ సృష్టించబడుతుంది.

```python
# 01.python-ఏజెంట్-ఫ్రేమ్‌వర్క్-వర్క్‌ఫ్లో-ghమోడల్-బేసిక్.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

చివరగా, వర్క్‌ఫ్లో ప్రారంభ వినియోగదారు ప్రాంప్ట్‌తో అమలు చేయబడుతుంది.

```python
# 01.python-ఏజెంట్-ఫ్రేమ్‌వర్క్-వర్క్‌ఫ్లో-ghమోడల్-బేసిక్.ipynb

result =''
# run_stream పద్ధతి వర్క్‌ఫ్లోని అమలు చేస్తుంది మరియు ఈవెంట్లను స్ట్రీమ్ చేస్తుంది.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) అమలు విశ్లేషణ

.NET అమలు చాలా సమానమైన లాజిక్‌ను అనుసరిస్తుంది. మొదట, ఏజెంట్ల పేర్లు మరియు సూచనల కోసం కాన్స్టెంట్స్ నిర్వచించబడతాయి.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

ఏజెంట్లు `OpenAIClient` ఉపయోగించి సృష్టించబడతాయి, మరియు తరువాత `WorkflowBuilder` సీక్వెన్షియల్ ఫ్లోను నిర్వచించడానికి `frontDeskAgent` నుండి `reviewerAgent` కు ఒక ఎడ్జ్‌ను జోడిస్తుంది.

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

వర్క్‌ఫ్లో వినియోగదారు సందేశంతో అమలు చేయబడుతుంది, మరియు ఫలితాలు స్ట్రీమ్ చేయబడతాయి.

### కేస్ 2: మల్టీ-స్టెప్ సీక్వెన్షియల్ వర్క్‌ఫ్లో

ఈ నమూనా ప్రాథమిక క్రమాన్ని మరింత ఏజెంట్లను చేర్చడం ద్వారా విస్తరిస్తుంది. ఇది అనేక దశల శుద్ధి లేదా మార్పిడి అవసరమైన ప్రక్రియలకు అనుకూలంగా ఉంటుంది.

#### సన్నివేశం నేపథ్యం

ఒక వినియోగదారు లివింగ్ రూమ్ యొక్క చిత్రాన్ని అందించి, ఫర్నిచర్ కోట్ కోరతాడు.

1.  **సేల్స్-ఏజెంట్**: చిత్రంలోని ఫర్నిచర్ అంశాలను గుర్తించి, జాబితాను సృష్టిస్తుంది.
2.  **ప్రైస్-ఏజెంట్**: అంశాల జాబితాను తీసుకుని, బడ్జెట్, మిడ్-రేంజ్, మరియు ప్రీమియం ఎంపికలతో కూడిన వివరమైన ధర బ్రేక్‌డౌన్‌ను అందిస్తుంది.
3.  **కోట్-ఏజెంట్**: ధర జాబితాను స్వీకరించి, Markdown లో ఫార్మల్ కోట్ డాక్యుమెంట్‌గా ఫార్మాట్ చేస్తుంది.

*సేల్స్ -\> ప్రైస్ -\> కోట్ వర్క్‌ఫ్లో డయాగ్రామ్.*

#### Python అమలు విశ్లేషణ

మూడు ఏజెంట్లు నిర్వచించబడి, ప్రతి ఒక్కటి ప్రత్యేకమైన పాత్రతో ఉంటాయి. వర్క్‌ఫ్లో `add_edge` ఉపయోగించి నిర్మించబడుతుంది, ఇది ఒక చైన్‌ను సృష్టిస్తుంది: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-ఏజెంట్-ఫ్రేమ్‌వర్క్-వర్క్‌ఫ్లో-జిహెచ్‌మోడల్-సీక్వెన్షియల్.ipynb

# మూడు ప్రత్యేకమైన ఏజెంట్లను సృష్టించండి
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# సీక్వెన్షియల్ వర్క్‌ఫ్లోని నిర్మించండి
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

ఇన్‌పుట్ ఒక `ChatMessage`, ఇది టెక్స్ట్ మరియు చిత్రం URI రెండింటినీ కలిగి ఉంటుంది. ఫ్రేమ్‌వర్క్ ప్రతి ఏజెంట్ అవుట్‌పుట్‌ను తదుపరి క్రమంలో పంపుతుంది, చివరికి ఫైనల్ కోట్ ఉత్పత్తి చేయబడే వరకు.

```python
# 02.python-ఏజెంట్-ఫ్రేమ్‌వర్క్-వర్క్‌ఫ్లో-ghmodel-సీక్వెన్షియల్.ipynb

# వినియోగదారు సందేశం టెక్స్ట్ మరియు చిత్రం రెండింటిని కలిగి ఉంది
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# వర్క్‌ఫ్లోను అమలు చేయండి
async for event in workflow.run_stream(message):
    ...
```

#### .NET (C\#) అమలు విశ్లేషణ

.NET ఉదాహరణ Python వెర్షన్‌ను ప్రతిబింబిస్తుంది. మూడు ఏజెంట్లు (`salesagent`, `priceagent`, `quoteagent`) సృష్టించబడతాయి. `WorkflowBuilder` వాటిని సీక్వెన్షియల్‌గా లింక్ చేస్తుంది.

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

వినియోగదారు సందేశం చిత్రం డేటా (బైట్స్‌గా) మరియు టెక్స్ట్ ప్రాంప్ట్ రెండింటితో నిర్మించబడుతుంది. `InProcessExecution.StreamAsync` పద్ధతి వర్క్‌ఫ్లోను ప్రారంభిస్తుంది, మరియు ఫైనల్ అవుట్‌పుట్ స్ట్రీమ్ నుండి క్యాప్చర్ చేయబడుతుంది.

### కేస్ 3: కంకరెంట్ వర్క్‌ఫ్లో

ఈ నమూనా పనులు సమాంతరంగా నిర్వహించబడినప్పుడు సమయాన్ని ఆదా చేయడానికి ఉపయోగించబడుతుంది. ఇది అనేక ఏజెంట్లకు "ఫ్యాన్-అవుట్" మరియు ఫలితాలను సమీకరించడానికి "ఫ్యాన్-ఇన్" ను కలిగి ఉంటుంది.

#### సన్నివేశం నేపథ్యం

ఒక వినియోగదారు సియాటిల్‌కు ట్రిప్ ప్లాన్ చేయమని అడుగుతాడు.

1.  **డిస్పాచర్ (ఫ్యాన్-అవుట్)**: వినియోగదారు అభ్యర్థనను ఒకేసారి రెండు ఏజెంట్లకు పంపుతుంది.
2.  **రిసెర్చర్-ఏజెంట్**: డిసెంబర్‌లో సియాటిల్ ట్రిప్ కోసం ఆకర్షణలు, వాతావరణం, మరియు ముఖ్యమైన అంశాలను పరిశోధిస్తుంది.
3.  **ప్లాన్-ఏజెంట్**: స్వతంత్రంగా ఒక వివరమైన డే-బై-డే ట్రావెల్ ఇటినరరీని సృష్టిస్తుంది.
4.  **అగ్రిగేటర్ (ఫ్యాన్-ఇన్)**: రిసెర్చర్ మరియు ప్లానర్ నుండి అవుట్‌పుట్‌లను సేకరించి, ఫైనల్ ఫలితంగా సమర్పిస్తుంది.

*కంకరెంట్ రిసెర్చర్ మరియు ప్లానర్ వర్క్‌ఫ్లో డయాగ్రామ్.*

#### Python అమలు విశ్లేషణ

`ConcurrentBuilder` ఈ నమూనా సృష్టిని సులభతరం చేస్తుంది. మీరు పాల్గొనే ఏజెంట్లను జాబితా చేయాలి, మరియు బిల్డర్ ఆటోమేటిక్‌గా అవసరమైన ఫ్యాన్-అవుట్ మరియు ఫ్యాన్-ఇన్ లాజిక్‌ను సృష్టిస్తుంది.

```python
# 03.python-ఏజెంట్-ఫ్రేమ్‌వర్క్-వర్క్‌ఫ్లో-ghమోడల్-కాంకరెంట్.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# కాంకరెంట్‌బిల్డర్ ఫ్యాన్-అవుట్/ఫ్యాన్-ఇన్ లాజిక్‌ను నిర్వహిస్తుంది
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# వర్క్‌ఫ్లోను నడపండి
events = await workflow.run("Plan a trip to Seattle in December")
```

ఫ్రేమ్‌వర్క్ `research_agent` మరియు `plan_agent` సమాంతరంగా అమలు చేయడాన్ని నిర్ధారిస్తుంది, మరియు వారి ఫైనల్ అవుట్‌పుట్‌లను జాబితాగా సేకరిస్తుంది.

#### .NET (C\#) అమలు విశ్లేషణ

.NET లో, ఈ నమూనా మరింత స్పష్టమైన నిర్వచనాన్ని అవసరం చేస్తుంది. కస్టమ్ ఎగ్జిక్యూటర్లు (`ConcurrentStartExecutor` మరియు `ConcurrentAggregationExecutor`) ఫ్యాన్-అవుట్ మరియు ఫ్యాన్-ఇన్ లాజిక్‌ను నిర్వహించడానికి సృష్టించబడతాయి.

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

`WorkflowBuilder` ఈ కస్టమ్ ఎగ్జిక్యూటర్లు మరియు ఏజెంట్లతో గ్రాఫ్‌ను నిర్మించడానికి `AddFanOutEdge` మరియు `AddFanInEdge` ను ఉపయోగిస్తుంది.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### కేస్ 4: కండిషనల్ వర్క్‌ఫ్లో

కండిషనల్ వర్క్‌ఫ్లోలు బ్రాంచింగ్ లాజిక్‌ను పరిచయం చేస్తాయి, ఇది మధ్యంతర ఫలితాల ఆధారంగా వివిధ మార్గాలను అనుసరించడానికి వ్యవస్థను అనుమతిస్తుంది.

#### సన్నివేశం నేపథ్యం

ఈ వర్క్‌ఫ్లో ఒక టెక్నికల్ ట్యుటోరియల్ సృష్టి మరియు ప్రచురణను ఆటోమేట్ చేస్తుంది.

1.  **ఎవాంజలిస్ట్-ఏజెంట్**: ఇచ్చిన అవుట్‌లైన్ మరియు URLల ఆధారంగా ట్యుటోరియల్ డ్రాఫ్ట్‌ను రాస్తుంది.
2.  **కంటెంట్ రివ్యూయర్-ఏజెంట్**: డ్రాఫ్ట్‌ను సమీక్షిస్తుంది. ఇది పదాల సంఖ్య 200 పదాలకు పైగా ఉందా అని తనిఖీ చేస్తుంది.
3.  **కండిషనల్ బ్రాంచ్**:
      * **అనుమతించబడితే (`Yes`)**: వర్క్‌ఫ్లో `Publisher-Agent` కు కొనసాగుతుంది.
      * **తిరస్కరించబడితే (`No`)**: వర్క్‌ఫ్లో ఆగిపోతుంది మరియు తిరస్కరణకు కారణాన్ని అవుట్‌పుట్ చేస్తుంది.
4.  **పబ్లిషర్-ఏజెంట్**: డ్రాఫ్ట్ ఆమోదించబడితే, ఈ ఏజెంట్ కంటెంట్‌ను Markdown ఫైల్‌గా సేవ్ చేస్తుంది.

#### Python అమలు విశ్లేషణ

ఈ ఉదాహరణ కండిషనల్ లాజిక్‌ను అమలు చేయడానికి `select_targets` అనే కస్టమ్ ఫంక్షన్‌ను ఉపయోగిస్తుంది. ఈ ఫంక్షన్ `add_multi_selection_edge_group` కు పంపబడుతుంది మరియు `review_result` ఫీల్డ్ ఆధారంగా వర్క్‌ఫ్లోను డైరెక్ట్ చేస్తుంది.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# ఈ ఫంక్షన్ సమీక్ష ఫలితంపై ఆధారపడి తదుపరి దశను నిర్ణయిస్తుంది
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # ఆమోదించబడితే, 'save_draft' ఎగ్జిక్యూటర్‌కు కొనసాగండి
        return [save_draft_id]
    else:
        # తిరస్కరించబడితే, వైఫల్యాన్ని నివేదించడానికి 'handle_review' ఎగ్జిక్యూటర్‌కు కొనసాగండి
        return [handle_review_id]

# వర్క్‌ఫ్లో బిల్డర్ రూటింగ్ కోసం సెలక్షన్ ఫంక్షన్‌ను ఉపయోగిస్తుంది
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # మల్టీ-సెలక్షన్ ఎడ్జ్ షరతు లాజిక్‌ను అమలు చేస్తుంది
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` వంటి కస్టమ్ ఎగ్జిక్యూటర్లు ఏజెంట్ల JSON అవుట్‌పుట్‌ను పార్స్ చేసి, సెలక్షన్ ఫంక్షన్ తనిఖీ చేయగల బలమైన-రకం ఆబ్జెక్టులుగా మార్చడానికి ఉపయోగించబడతాయి.

#### .NET (C\#) అమలు విశ్లేషణ

.NET వెర్షన్ ఒక కండిషన్ ఫంక్షన్‌తో సమానమైన దృక్పథాన్ని ఉపయోగిస్తుంది. `Func<object?, bool>` `ReviewResult` ఆబ్జెక్ట్ యొక్క `Result` ప్రాపర్టీని తనిఖీ చేయడానికి నిర్వచించబడుతుంది.

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

`AddEdge` పద్ధతి యొక్క `condition` పరామితం `WorkflowBuilder` కు బ్రాంచింగ్ మార్గాన్ని సృష్టించడానికి అనుమతిస్తుంది. `GetCondition(expectedResult: "Yes")` నిజం అని తిరిగి ఇస్తే వర్క్‌ఫ్లో `publishExecutor` కు మాత్రమే ఎడ్జ్‌ను అనుసరిస్తుంది. లేనిపక్షంలో, ఇది `sendReviewerExecutor` మార్గాన్ని అనుసరిస్తుంది.

## ముగింపు

మైక్రోసాఫ్ట్ ఏజెంట్ ఫ్రేమ్‌వర్క్ వర్క్‌ఫ్లో సంక్లిష్ట, మల్టీ-ఏజెంట్ సిస్టమ్స్‌ను ఆర్కెస్ట్రేట్ చేయడానికి బలమైన మరియు అనువైన పునాది అందిస్తుంది. దాని గ్రాఫ్-ఆధారిత ఆర్కిటెక్చర్ మరియు ప్రధాన భాగాలను ఉపయోగించడం ద్వారా, డెవలపర్లు Python మరియు .NET లో అధునాతన వర్క్‌ఫ్లోలను రూపొందించి అమలు చేయవచ్చు. మీ అప్లికేషన్‌కు సరళమైన సీక్వెన్షియల్ ప్ర

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**విమర్శ**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించారు. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో తప్పులు లేదా అసమానతలు ఉండవచ్చు. దాని స్వదేశీ భాషలోని అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదాన్ని ఉపయోగించడం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->