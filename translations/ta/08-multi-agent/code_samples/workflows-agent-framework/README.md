# Microsoft Agent Framework Workflow உடன் பன்முக முகவர் செயலிகளை உருவாக்குதல்

இந்த பயிற்சிக் குறிப்பானது Microsoft Agent Framework பயன்படுத்தி பன்முக முகவர் செயலிகளை புரிந்து கொண்டு உருவாக்குவதற்கான வழிகாட்டுதலை வழங்கும். நாம் பன்முக முகவர் அமைப்புகளின் முக்கியக் கருத்துக்களை ஆராய்வோம், கட்டமைப்பின் Workflow கூறின் வடிவமைப்பை கவனித்து பார்ப்போம், மற்றும் Python மற்றும் .NET பயன்படுத்தி வெவ்வேறு workflow மாதிரிகளுக்கு நடைமுறை எடுத்துக்காட்டுகளை நடத்தியுக்கொள்வோம்.

## 1\. பன்முக முகவர் அமைப்புகளை புரிந்து கொள்வது

ஒரு AI முகவர் என்பது ஒரு பொதுவான பெரிய மொழி மாதிரி (LLM) திறமைகளை மீறி செயல்படும் ஒரு அமைப்பு. இது தன் சூழலை உணர்ந்து, முடிவுகள் எடுத்து, குறிப்பிட்ட நோக்கங்களை அடைய நடவடிக்கைகளை மேற்கொள்கிறது. ஒரு பன்முக முகவர் அமைப்பு என்பது பல முகவர்கள் ஒருங்கிணைந்து ஒரு பிரச்சினையை தீர்க்க முயலும். இது ஒரு முகவரால் தனாக செய்ய முடியாத அல்லது கடினமான வேலைகளைச் செய்ய உதவுகிறது.

### பொதுவான பயன்பாட்டு காட்சிகள்

  * **சிக்கலான பிரச்சினை தீர்வு**: பெரிய ஒரு பணியை (எ.கா., முழு நிறுவன நிகழ்வை திட்டமிடல்) சிறிய துணை பணிகளாகப் பிரித்து, தனித்தொழில் கொண்ட முகவர்கள் (எ.கா., பட்ஜெட் முகவர், விநியோகம் முகவர், சந்தைப்படுத்தல் முகவர்) கையாளல்.
  * **மெய்நிகர் உதவியாளர்கள்**: முதன்மை உதவியாளர் முகவர் திட்டமிடல், ஆய்வு மற்றும் முன்பதிவு போன்ற பணிகளை பிற தனித்தொழில் கொண்ட முகவர்களுக்கு ஒப்படைக்கும்.
  * **தானாக உள்ளடக்கம் உருவாக்குதல்**: ஒரு முகவர் உள்ளடக்கத்தை வரைவு படுத்தி, மற்றொன்று சராசரி மற்றும் சுருதி பரிசீலனை செய்து, மூன்றாவது முகவர் அதை வெளியிடும் வேலைபாதை.

### பன்முக முகவர் வடிவமைப்புகள்

பன்முக முகவர் அமைப்புகளை பல வடிவங்களில் ஒழுங்குசெய்யலாம், அவை ஒருவரிடம் பரிமாறுவதற்கு விதிகளை வரையறுக்கின்றன:

  * **வரிசைப்படுத்தப்பட்ட**: முகவர்கள் முன்கூட்டியே நிர்ணயிக்கப்பட்ட வரிசையில் வேலை செய்கின்றனர், ஒரு அசம்பிளி வரிசை போல. ஒரு முகவரின் வெளியீடு அடுத்ததுகான உள்ளீடாகிறது.
  * **ஒரே நேரத்தில்**: முகவர்கள் ஒரே நேரத்தில் வேறுபட்ட பணிகளில் செயல்படுகின்றனர், மற்றும் அவற்றின் முடிவுகள் கடையில் சேர்க்கப்படுகின்றன.
  * **நிபந்தனை அடிப்படையிலான**: ஒரு முகவரின் வெளியீட்டை அடிப்படையாகக் கொண்டு workflow வேறுபட்ட பாதைகளில் செல்கிறது. இதை if-then-else கூற்றுப் போலாக்கலாம்.

## 2\. Microsoft Agent Framework Workflow கட்டமைப்பு

Agent Framework-இன் workflow அமைப்பு என்பது பல முகவர்களிடையே சிக்கலான உறவுகளை நிர்வகிப்பதற்கான முன்னேற்றப்பட்ட ஒருங்கிணைப்பு இயந்திரமாகும். இது [Pregel-போன்ற செயலாக்க மாதிரி](https://kowshik.github.io/JPregel/pregel_paper.pdf) அடிப்படையில் உருவாக்கப்பட்டுள்ளது, இதில் செயலாக்கம் ஒருங்கிணைந்த "supersteps" என்ற படிகளாக நடக்கிறது.

### முக்கிய கூறுகள்

கட்டமைப்பு மூன்று முக்கிய பகுதிகளால் துவந்திருகிறது:

1.  **நடத்திகள் (Executors)**: இவை அடிப்படை செயலாக்க அலகுகள். எங்கள் எடுத்துக்காட்டுகளில், ஒரு `Agent` என்பது ஒரு executor வகையினை சேர்ந்தது. ஒவ்வொரு executor-க்கும் பல செய்தி கையாளிகள் இருப்பதற்கு வாய்ப்பு உள்ளது, அவை பெறும் செய்தியின் வகையின் அடிப்படையில் தானாக அழைக்கப்படுகின்றன.
2.  **எட்ஜுகள் (Edges)**: இவை executor-களுக்கு இடையே தகவல் பரிமாற்ற பாதையை குறிப்பிடுகின்றன. இவை நிபந்தனைகளுடன் இருக்கலாம், workflow காட்சி மூலம் தகவலை இயக்கும் வழிமுறைகளை அனுமதிக்கிறது.
3.  **Workflow**: இந்த கூறு முழு செயல்முறையினையும் ஒருங்கிணைக்கும், executor-களை, edge-களை மற்றும் மிகுதி இயக்கத்தை நிர்வகிக்கும். இது செய்திகளின் ஒழுங்கான செயலாக்கம் மற்றும் நிகழ்வுகளுக்கு ஒளிப்படத்தலுக்கான உபகரணங்களையும் உறுதிப்படுத்துகிறது.

*workflow அமைப்பின் முக்கிய கூறுகளை விளக்கும் வரைபடம்.*

இந்த கட்டமைப்பு அடிப்படையாக வரிசைச் சங்கிலிகள், பக்கவாட்டு fan-out/fan-in செயலாக்கம் மற்றும் நிபந்தனை அடிப்படையிலான மாற்றுக் வழிமுறைகள் போன்ற தோற்றங்களைப் பயன்படுத்தி வலுவான மற்றும் அளவிடக்கூடிய செயலிகளை உருவாக்க அனுமதிக்கின்றது.

## 3\. நடைமுறை எடுத்துக்காட்டுகள் மற்றும் குறியீடு பகுப்பு

இப்போது, நாமே framework பயன்படுத்தி வேறுபட்ட workflow மாதிரிகளை எப்படி செயல்படுத்துவது என்று பார்ப்போம். ஒவ்வொரு எடுத்துக்காட்டுக்கும் Python மற்றும் .NET குறியீடையும் பார்ப்போம்.

### எடுத்துக்காட்டு 1: அடிப்படை வரிசைப்படுத்தப்பட்ட Workflow

இது எளிதான மாதிரி, ஒரு முகவரின் வெளியீடு நேரடியாக மற்றொன்றிற்கு அனுப்பப்படும். எங்கள் காட்சியில் ஒரு ஹோட்டல் `FrontDesk` முகவர் ஒரு பயண பரிந்துரையை உருவாக்குகிறார், அது பின்னர் `Concierge` முகவரால் பரிசீலிக்கப்படும்.

*அடிப்படை FrontDesk -> Concierge workflow வரைபடம்.*

#### காட்சியின் பின்னணி

ஒரு பயணி பாரிசில் பரிந்துரை கேட்கிறார்.

1.  சுருக்கமாக உட்படுத்தப்பட்ட `FrontDesk` முகவர் Louvre அருங்காட்சியகத்தைப் பார்வையிட பரிந்துரைக்கிறார்.
2.  உண்மையான அனுபவங்களை முன்னிடும் `Concierge` முகவர் அந்த பரிந்துரையைப் பெறும், பரிந்துரையை பரிசீலித்து, குறைந்த சுற்றுலா இடமான உள்ளூர் மாற்று பரிந்துரையையும் வழங்குகிறார்.

#### Python செயலாக்க பகுப்பு

Python எடுத்துக்காட்டில், முதலில் இரண்டு முகவர்களை வரையறுத்து உருவாக்குகிறோம், ஒவ்வொருவரும் குறிப்பிட்ட அறிவுறுத்தல்களுடன்.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# முகவர் பாத்திரங்களையும் அறிவுறுத்தல்களையும் வரையறு
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# முகவர் நிழல்கள் உருவாக்கவும்
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

அடுத்து, `WorkflowBuilder` பயன்படுத்தி கிராப் கட்டப்படுகிறது. `front_desk_agent` துவக்க புள்ளியாகவும், அதன் வெளியீடை `reviewer_agent`க்கு இணைக்கும் edge உருவாக்கப்படுகிறது.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

இறுதியாக, ஆரம்ப பயனர் கிளியை கொண்டு workflow இயக்கு.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run வேலைप्रவாகத்தை இயக்குகிறது; get_outputs() வெளியீடு இயக்கியின் முடிவை 반환 செய்கிறது.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) செயலாக்க பகுப்பு

.NET செயலாக்கம் மிகவும் ஒத்ததுதான். முதலில் முகவர்களின் பெயர்க்குறிப்புகள் மற்றும் அறிவுறுத்தல்கள் நிர்ணயிக்கப்படுகின்றன.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

முகவர்கள் `AzureOpenAIClient` (Responses API) பயன்படுத்தி உருவாக்கப்படுகின்றனர், பின்னர் `WorkflowBuilder` `frontDeskAgent` முதல் `reviewerAgent` க்கு வரிசைப்படுத்தப்பட்ட edge ஐ உருவாக்குகிறது.

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

பயனரின் செய்தியுடன் workflow இயக்கப்படுகின்றது, முடிவுகள் தொடர்ச்சியாக வழங்கப்படுகின்றன.

### எடுத்துக்காட்டு 2: பல படி வரிசையான Workflow

இந்த மாதிரி அடிப்படை வரிசையை அதிக முகவர்களுக்கு நீட்டிக்கிறது. இது பல சார்ந்த மாற்றங்கள் அல்லது சரிசெய்தல் படிகளை தேவைப்படுத்தும் செயலிகளுக்கு சிறந்தது.

#### காட்சியின் பின்னணி

ஒரு பயனர் ஒரு உறைவுமுனை படத்தை வழங்கி அது தொடர்பான கேள்வி கேட்கிறார்.

1.  **விற்பனை முகவர்**: படத்திலுள்ள கைப்பொருட்களை அடையாளம் கண்டு பட்டியலிடுகிறார்.
2.  **விலை முகவர்**: ஆபரண பட்டியலை சமர்ப்பித்து, பட்ஜெட், நடுத்தர மற்றும் பிரீமியம் விருப்பங்களுடன் விரிவான விலை விபரங்களை வழங்குகிறார்.
3.  **கோட்டை முகவர்**: விலைப்படுத்தப்பட்ட பட்டியலை Markdown வடிவில் ஒரு அதிகாரமான மேற்கோள் ஆவணமாக மாற்றி வழங்குகிறார்.

*விற்பனை -> விலை -> கோட்டை workflow வரைபடம்.*

#### Python செயலாக்க பகுப்பு

மூன்று முகவர்கள் ஒவ்வொருவருக்கும் தனித்தொழில் கொடுக்கப்படுகிறார்கள். workflow `add_edge` வழியாக சங்கிலியாக உருவாகிறது: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# மூன்று சிறப்பு முகவர்கள் உருவாக்கவும்
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# வரிசை வேலைப்பாடை கட்டமைக்கவும்
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

உள்ளீடு ஒரு `ChatMessage`, அதில் உரையும் பட URI-உம் உள்ளது. framework ஒவ்வொரு முகவரின் வெளியீட்டை அடுத்ததுக்கு அனுப்பி நடைமுறை செய்கிறது, இறுதியில் மேற்கோள் உருவாக்கப்படுகிறது.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# பயனர் செய்தியில் உரையும் ஒரு படம் இரண்டும் உள்ளன
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# வேலை தொடரைக் இயக்கவும்
events = await workflow.run(message)
```

#### .NET (C\#) செயலாக்க பகுப்பு

.NET எடுத்துக்காட்டு Python பதிப்புடன் ஒத்திருக்கின்றது. மூன்று முகவர்கள் (`salesagent`, `priceagent`, `quoteagent`) உருவாக்கப்படுகின்றன. `WorkflowBuilder` அவர்கள் வரிசைப்படுத்தப்பட்ட இணைப்பை உருவாக்குகிறது.

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

பயனரின் செய்தி பட தரவு (பைட்களாக) மற்றும் உரை கிளி உடன் உருவாக்கப்படுகிறது. `InProcessExecution.RunStreamingAsync` μέத்தடோடு workflow துவங்கி, இறுதி வெளியீடு தொடரில் பிடிக்கப்படுகிறது.

### எடுத்துக்காட்டு 3: ஒரே நேர Concurrent Workflow

இது பணிகளை ஒரே நேரத்தில் செய்வதற்குரிய மாதிரி. இதில் பல முகவர்களுக்கு "fan-out" செய்து, முடிவுகளை "fan-in" மூலம் ஒன்றிணைக்கும் செயலைச் செய்யும்.

#### காட்சியின் பின்னணி

ஒரு பயனர் சீயாட்டிளுக்கு பயணம் திட்டமிட கேட்கிறார்.

1.  **ஒப்படைப்பாளர் (Fan-Out)**: பயனரின் கோரிக்கையை இரண்டு முகவர்களுக்கு ஒரே நேரத்தில் அனுப்புகிறார்.
2.  **ஆய்வாளர் முகவர்**: சீயாட்டிளின் வசதிகள், வானிலை, முக்கிய கவனங்கள் பற்றி ஆராய்கிறார்.
3.  **திட்டமிடும் முகவர்**: தனிப்பட்ட முறையில் தினசரி பயண திட்டத்தை உருவாக்குகின்றார்.
4.  **இணைப்பாளர் (Fan-In)**: ஆராய்ச்சியாளரும் திட்டமிடுநரும் வழங்கும் முடிவுகளை சேகரித்து, இறுதிப் படையாக வழங்குகிறார்.

*ஒரே நேர ஆராய்ச்சியாளர் மற்றும் திட்டமிடுநர் workflow வரைபடம்.*

#### Python செயலாக்க பகுப்பு

`ConcurrentBuilder` இந்த மாதிரியை எளிமையாக்குகிறது. நீங்கள் பங்கேற்கும் முகவர்களை பட்டியலிடுகிறீர்கள், மற்றும் builder தானாகவே fan-out மற்றும் fan-in வரையறுக்கிறது.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ஈர்க்கல்/பிரிக்கல் தர்க்கத்தை கையாள்கிறது
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# வழிமுறையை இயக்குக
events = await workflow.run("Plan a trip to Seattle in December")
```

framework `research_agent` மற்றும் `plan_agent` ஒரே நேரத்தில் இயங்கவும், முடிவுகளை பட்டியலில் சேகரிக்கும் பணியும் செய்கிறது.

#### .NET (C\#) செயலாக்க பகுப்பு

.NET இல் இந்த மாதிரி சிறிது தெளிவான வரையறையை தேவைப்படுத்துகிறது. தனிப்பட்ட இயக்கிகள் (`ConcurrentStartExecutor` மற்றும் `ConcurrentAggregationExecutor`) fan-out மற்றும் fan-in பணிகளை கையாளக்கூடியவையாக உருவாக்கப்படுகின்றன.

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

பின்னர் `WorkflowBuilder` `AddFanOutEdge` மற்றும் `AddFanInEdge` பயன்படுத்தி இந்த தனிப்பட்ட இயக்கிகள் மற்றும் முகவர்களுடன் கிராப் கட்டுகிறது.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### எடுத்துக்காட்டு 4: நிபந்தனை அடிப்படையிலான Workflow

நிபந்தனை அடிப்படையிலான workflow கள் கிளையின் வழிமுறைகளை அறிமுகப்படுத்துகின்றன, அமைப்பு இடைக்கால முடிவுகளின் அடிப்படையில் வேறுபட்ட பாதைகளை எடுத்துச் செல்ல முடியும்.

#### காட்சியின் பின்னணி

இந்த workflow தொழில்துறை பயிற்சிக் குறிப்பை தானாக உருவாக்கி வெளியிடுகிறது.

1.  **Evangelist-Agent**: கொடுக்கப்பட்ட சுருக்கம் மற்றும் URL அடிப்படையில் பயிற்சிக் குறிப்பின் வரைவை எழுதுகிறார்.
2.  **ContentReviewer-Agent**: வரைவை சரிபார்க்கிறார். வார்த்தை எண்ணிக்கை 200ஐத் தாண்டியுள்ளதா என்பதைப் பார்க்கிறார்.
3.  **நிபந்தனை கிளை**:
      * **சென்றால் (`ஆம்`)**: workflow `Publisher-Agent`க்கு செல்கிறது.
      * **இல்லையெனில் (`இல்லை`)**: workflow நிறுத்தப்படுகிறது மற்றும் நிராகரிப்பு காரணத்தை வெளிப்படுத்துகிறது.
4.  **Publisher-Agent**: வரைவு அனுமதிக்கப்பட்டால், இந்த முகவர் உள்ளடக்கத்தை Markdown கோப்பாக சேமிக்கிறார்.

#### Python செயலாக்க பகுப்பு

இந்த எடுத்துக்காட்டு ஒரு தனிப்பட்ட செயல்பாடு `select_targets` ஐ பயன்படுத்தி நிபந்தனை அச்சொற்களை செயல்படுத்துகிறது. இந்த செயல்பாடு `add_multi_selection_edge_group` க்கு வழங்கப்படுகின்றது மற்றும் பார்வையாளர் வெளியீட்டின் `review_result` புலத்தைப் பயன்படுத்தி workflow ஐ வழிநடத்துகிறது.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# இந்த செயல்பாடு மதிப்பாய்வு முடிவின் அடிப்படையில் அடுத்த படியை தீர்மானிக்கிறது
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # ஒப்புதலானால், 'save_draft' அமல்படுத்துபவருக்கு முன்னேறு
        return [save_draft_id]
    else:
        # மறுக்கப்பட்டால், தோல்வியை அறிக்கையிட 'handle_review' அமல்படுத்துபவருக்கு முன்னேறு
        return [handle_review_id]

# பணிச்சுழற்சி கட்டியாளர் வழிநடத்தும் செயலுக்காக தேர்வு செயல்பாட்டைப் பயன்படுத்துகிறது
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # பல தேர்வு விளிம்பு நிபந்தனை தர்க்கத்தை அமல்படுத்துகிறது
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` போன்ற தனிப்பட்ட இயக்கிகள் முகவர்களின் JSON வெளியீட்டை பாக்ஸிங் செய்து தேர்வு செயல்பாடு பரிசீலிக்க கூடிய வலுவான வகையாக்கப்பட்ட பொருட்களாக மாற்றுகின்றன.

#### .NET (C\#) செயலாக்க பகுப்பு

.NET பதிப்பு நிபந்தனை செயல்பாட்டோடு ஒத்த முறையைப் பயன்படுத்துகிறது. ஒரு `Func<object?, bool>` உருவாக்கப்படுகிறது, இது `ReviewResult` பொருளின் `Result` பண்பை சரிபார்க்கிறது.

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

`AddEdge` செயற்கூறு `condition` அளவுருவின் மூலம் `WorkflowBuilder` கிளை பாதையை உருவாக்குகிறது. workflow `publishExecutor`க்கு செல்லும் வழியை மட்டும் `GetCondition(expectedResult: "Yes")` சப்திக்குச் சராசரி எழுப்பும்போது பின்பற்றும். இல்லையெனில் `sendReviewerExecutor`க்கு செல்லும் பாதையை பின்பற்றும்.

## முடிவு

Microsoft Agent Framework Workflow பல முகவர் அமைப்புகளுக்கு சிக்கலான ஒருங்கிணைப்பில் வலுவான மற்றும் நெகிழ்வான அடித்தளத்தையும் வழங்குகிறது. அதன் கிராப் அடிப்படையிலான கட்டமைப்பும் முக்கிய கூறுகளும், Python மற்றும் .NET இரண்டிலும் மேம்பட்ட workflows வடிவமைக்க மற்றும் செயல்படுத்த உதவுகின்றன. உங்கள் செயலி எளிய வரிசை செயலாக்கத்தையும், ஒரே நேர செயல்பாடுகளையும் அல்லது மாற்று நிபந்தனை நிகழ்வுகளையும் தேவைப்படுத்தினாலும்கூட, இந்த framework சக்திவாய்ந்த, அளவுத் தெளிவிலான மற்றும் வகை பாதுகாப்பான AI மேலாளர் தீர்வுகளை உருவாக்கும் கருவிகளை வழங்குகிறது.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->