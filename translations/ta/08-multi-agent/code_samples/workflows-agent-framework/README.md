<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b39c052ef109db90ad9251183791e2d6",
  "translation_date": "2025-10-11T11:09:09+00:00",
  "source_file": "08-multi-agent/code_samples/workflows-agent-framework/README.md",
  "language_code": "ta"
}
-->
# Microsoft Agent Framework Workflow மூலம் பல முகவர் பயன்பாடுகளை உருவாக்குதல்

இந்த பயிற்சியில், Microsoft Agent Framework-ஐப் பயன்படுத்தி பல முகவர் பயன்பாடுகளை உருவாக்குவதற்கான வழிகாட்டுதலைப் பெறுவீர்கள். பல முகவர் அமைப்புகளின் முக்கிய கருத்துகளைப் புரிந்துகொள்வதுடன், Framework-இன் Workflow கூறின் கட்டமைப்பை ஆராய்ந்து, Python மற்றும் .NET-இல் பல Workflow முறைமைகளுக்கான நடைமுறை உதாரணங்களைப் பார்ப்போம்.

## 1\. பல முகவர் அமைப்புகளைப் புரிந்துகொள்வது

AI Agent என்பது ஒரு Large Language Model (LLM) இன் வழக்கமான திறன்களைத் தாண்டி செயல்படும் ஒரு அமைப்பு. இது தனது சூழலை உணர்ந்து, முடிவுகளை எடுத்து, குறிப்பிட்ட இலக்குகளை அடைய நடவடிக்கைகளை எடுக்க முடியும். பல முகவர் அமைப்பு என்பது பல முகவர்கள் இணைந்து ஒரு பிரச்சினையைத் தீர்க்கும் ஒரு அமைப்பாகும், இது ஒரு முகவரால் தனியாக கையாள முடியாத அல்லது கடினமானதாக இருக்கும்.

### பொதுவான பயன்பாட்டு சூழல்கள்

  * **சிக்கலான பிரச்சினை தீர்வு**: ஒரு பெரிய பணியை (எ.கா., ஒரு நிறுவன அளவிலான நிகழ்வை திட்டமிடுதல்) சிறிய துணை பணிகளாக பிரித்து, சிறப்பு முகவர்களால் (எ.கா., ஒரு பட்ஜெட் முகவர், ஒரு லாஜிஸ்டிக்ஸ் முகவர், ஒரு மார்க்கெட்டிங் முகவர்) கையாளுதல்.
  * **மெய்நிகர் உதவியாளர்கள்**: ஒரு முதன்மை உதவியாளர் முகவர், திட்டமிடல், ஆராய்ச்சி மற்றும் முன்பதிவு போன்ற பணிகளை மற்ற சிறப்பு முகவர்களுக்கு ஒப்படைக்கிறது.
  * **தானியங்கிய உள்ளடக்க உருவாக்கம்**: ஒரு முகவர் உள்ளடக்கத்தை உருவாக்குகிறது, மற்றொரு முகவர் துல்லியம் மற்றும் தொனிக்கான மதிப்பீடு செய்கிறது, மேலும் மூன்றாவது முகவர் அதை வெளியிடுகிறது.

### பல முகவர் முறைமைகள்

பல முகவர் அமைப்புகள் பல முறைமைகளில் ஒழுங்கமைக்கப்படலாம், இது அவற்றின் தொடர்பு முறையை நிர்ணயிக்கிறது:

  * **தொடர்ச்சியானது**: முகவர்கள் முன்கூட்டியே வரையறுக்கப்பட்ட வரிசையில் வேலை செய்கின்றனர், ஒரு முகவரின் வெளியீடு அடுத்ததற்கான உள்ளீடாக மாறுகிறது.
  * **ஒரே நேரத்தில்**: முகவர்கள் ஒரு பணியின் வெவ்வேறு பகுதிகளில் ஒரே நேரத்தில் வேலை செய்கின்றனர், மேலும் அவர்களின் முடிவுகள் இறுதியில் ஒருங்கிணைக்கப்படுகின்றன.
  * **நிபந்தனையுடன்**: Workflow, ஒரு முகவரின் வெளியீட்டின் அடிப்படையில் வெவ்வேறு பாதைகளைப் பின்பற்றுகிறது, இது ஒரு if-then-else அறிக்கையைப் போன்றது.

## 2\. Microsoft Agent Framework Workflow கட்டமைப்பு

Agent Framework-இன் Workflow அமைப்பு என்பது பல முகவர்களுக்கிடையிலான சிக்கலான தொடர்புகளை நிர்வகிக்க வடிவமைக்கப்பட்ட ஒரு மேம்பட்ட ஒருங்கிணைப்பு இயந்திரமாகும். இது [Pregel-பாணி செயல்பாட்டு முறை](https://kowshik.github.io/JPregel/pregel_paper.pdf) அடிப்படையில் கட்டமைக்கப்பட்டுள்ளது, இதில் "supersteps" எனப்படும் ஒத்திசைந்த படிகளில் செயலாக்கம் நடைபெறுகிறது.

### முக்கிய கூறுகள்

இந்த கட்டமைப்பு மூன்று முக்கிய பகுதிகளால் உருவாக்கப்பட்டுள்ளது:

1.  **Executors**: இவை அடிப்படை செயலாக்க அலகுகள். எங்கள் உதாரணங்களில், `Agent` என்பது ஒரு வகை Executor ஆகும். ஒவ்வொரு Executor-க்கும் பல Message Handler-கள் இருக்கலாம், இது பெறப்படும் Message வகையின் அடிப்படையில் தானாகவே அழைக்கப்படும்.
2.  **Edges**: இவை Executor-களுக்கிடையிலான Message-கள் செல்லும் பாதையை வரையறுக்கின்றன. Edges-களுக்கு நிபந்தனைகள் இருக்கலாம், இது Workflow Graph வழியாக தகவலின் மாறுபட்ட வழிமுறையை அனுமதிக்கிறது.
3.  **Workflow**: இந்த கூறு முழு செயல்முறையை ஒருங்கிணைக்கிறது, Executors, Edges மற்றும் செயல்முறையின் ஒட்டுமொத்த ஓட்டத்தை நிர்வகிக்கிறது. இது Message-கள் சரியான வரிசையில் செயலாக்கப்படுவதை உறுதிசெய்கிறது மற்றும் கண்காணிப்புக்கான நிகழ்வுகளை ஸ்ட்ரீம் செய்கிறது.

*Workflow அமைப்பின் முக்கிய கூறுகளை விளக்கும் ஒரு வரைபடம்.*

இந்த அமைப்பு தொடர்ச்சியான சங்கிலிகள், ஒரே நேரத்தில் செயலாக்கத்திற்கான fan-out/fan-in மற்றும் நிபந்தனையுடன் செயல்படும் switch-case logic போன்ற அடிப்படை முறைமைகளைப் பயன்படுத்தி வலுவான மற்றும் அளவிடக்கூடிய பயன்பாடுகளை உருவாக்க அனுமதிக்கிறது.

## 3\. நடைமுறை உதாரணங்கள் மற்றும் குறியீட்டு பகுப்பாய்வு

இப்போது, Framework-ஐப் பயன்படுத்தி வெவ்வேறு Workflow முறைமைகளை எவ்வாறு செயல்படுத்துவது என்பதை ஆராய்வோம். ஒவ்வொரு உதாரணத்திற்கும் Python மற்றும் .NET குறியீட்டைப் பார்ப்போம்.

### வழக்கு 1: அடிப்படை தொடர்ச்சியான Workflow

இது மிக எளிய முறைமையாகும், இதில் ஒரு முகவரின் வெளியீடு நேரடியாக மற்றொரு முகவருக்கு அனுப்பப்படுகிறது. எங்கள் சூழல் ஒரு ஹோட்டல் `FrontDesk` முகவர் ஒரு பயண பரிந்துரையை வழங்குகிறது, அதை `Concierge` முகவர் மதிப்பீடு செய்கிறது.

*FrontDesk -\> Concierge Workflow-இன் அடிப்படை வரைபடம்.*

#### சூழல் பின்னணி

ஒரு பயணி பாரிஸில் ஒரு பரிந்துரையை கேட்கிறார்.

1.  `FrontDesk` முகவர், சுருக்கமாக செயல்படுவதற்காக வடிவமைக்கப்பட்டுள்ளது, Louvre அருங்காட்சியகத்தை பார்வையிட பரிந்துரைக்கிறது.
2.  `Concierge` முகவர், உண்மையான அனுபவங்களை முன்னுரிமை அளிக்கிறான், இந்த பரிந்துரையைப் பெறுகிறது. இது பரிந்துரையை மதிப்பீடு செய்து, ஒரு உள்ளூர், குறைவாக சுற்றுலாப் பயணிகளின் மாற்றத்தை பரிந்துரைக்கிறது.

#### Python செயல்பாட்டு பகுப்பாய்வு

Python உதாரணத்தில், முதலில் இரண்டு முகவர்களை வரையறுத்து உருவாக்குகிறோம், ஒவ்வொன்றும் குறிப்பிட்ட வழிகாட்டுதல்களுடன்.

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

அடுத்ததாக, `WorkflowBuilder` பயன்படுத்தி Graph-ஐ உருவாக்குகிறோம். `front_desk_agent` தொடக்க புள்ளியாக அமைக்கப்படுகிறது, மேலும் அதன் வெளியீட்டை `reviewer_agent`-க்கு இணைக்கும் ஒரு Edge உருவாக்கப்படுகிறது.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

இறுதியாக, Workflow பயனர் கேள்வியுடன் செயல்படுத்தப்படுகிறது.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) செயல்பாட்டு பகுப்பாய்வு

.NET செயல்பாடு மிகவும் ஒத்த தத்துவத்தை பின்பற்றுகிறது. முதலில், முகவர்களின் பெயர்கள் மற்றும் வழிகாட்டுதல்களுக்கான Constants வரையறுக்கப்படுகின்றன.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

முகவர்கள் `OpenAIClient`-ஐப் பயன்படுத்தி உருவாக்கப்படுகின்றன, பின்னர் `WorkflowBuilder` தொடர்ச்சியான ஓட்டத்தை வரையறுக்கிறது, `frontDeskAgent`-இல் இருந்து `reviewerAgent`-க்கு Edge சேர்க்கிறது.

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

Workflow பயனர் Message-யுடன் இயக்கப்படுகிறது, மேலும் முடிவுகள் ஸ்ட்ரீம் மூலம் திரும்ப பெறப்படுகின்றன.

### வழக்கு 2: பல படி தொடர்ச்சியான Workflow

இந்த முறைமையானது அடிப்படை தொடர்ச்சியை மேலும் விரிவாக்குகிறது, மேலும் முகவர்களைச் சேர்க்கிறது. இது பல கட்டங்களின் சீரமைப்பு அல்லது மாற்றம் தேவைப்படும் செயல்முறைகளுக்கு சிறந்தது.

#### சூழல் பின்னணி

ஒரு பயனர் ஒரு வாழும் அறையின் படத்தை வழங்கி, ஒரு பொருட்களின் விலை மதிப்பீட்டை கேட்கிறார்.

1.  **Sales-Agent**: படத்தில் உள்ள பொருட்களை அடையாளம் கண்டு ஒரு பட்டியலை உருவாக்குகிறது.
2.  **Price-Agent**: பொருட்களின் பட்டியலை எடுத்துக்கொண்டு, பட்ஜெட், நடுத்தர மற்றும் பிரீமியம் விருப்பங்களை உள்ளடக்கிய விரிவான விலை விவர breakdown-ஐ வழங்குகிறது.
3.  **Quote-Agent**: விலைப்பட்டியலைப் பெறுகிறது மற்றும் அதை Markdown-இல் ஒரு அதிகாரப்பூர்வ Quote ஆவணமாக வடிவமைக்கிறது.

*Sales -\> Price -\> Quote Workflow-இன் வரைபடம்.*

#### Python செயல்பாட்டு பகுப்பாய்வு

மூன்று முகவர்கள் வரையறுக்கப்படுகின்றன, ஒவ்வொன்றும் ஒரு சிறப்பு பங்கு கொண்டது. Workflow `add_edge` பயன்படுத்தி ஒரு சங்கிலியை உருவாக்குகிறது: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

உள்ளீடு ஒரு `ChatMessage`, இது உரை மற்றும் படத்தின் URI ஆகியவற்றை உள்ளடக்கியது. Framework ஒவ்வொரு முகவரின் வெளியீட்டை அடுத்தவருக்கு அனுப்புவதையும் இறுதியாக Quote உருவாக்கப்படுவதையும் நிர்வகிக்கிறது.

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

#### .NET (C\#) செயல்பாட்டு பகுப்பாய்வு

.NET உதாரணம் Python பதிப்பை பிரதிபலிக்கிறது. மூன்று முகவர்கள் (`salesagent`, `priceagent`, `quoteagent`) உருவாக்கப்படுகின்றன. `WorkflowBuilder` அவற்றை தொடர்ச்சியாக இணைக்கிறது.

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

பயனர் Message, படத்தின் தரவுடன் (bytes ஆக) மற்றும் உரை prompt உடன் உருவாக்கப்படுகிறது. `InProcessExecution.StreamAsync` முறை Workflow-ஐ தொடங்குகிறது, மேலும் இறுதி வெளியீடு ஸ்ட்ரீமில் இருந்து பிடிக்கப்படுகிறது.

### வழக்கு 3: ஒரே நேரத்தில் Workflow

இந்த முறைமையானது பணிகளை ஒரே நேரத்தில் செய்யும்போது நேரத்தைச் சேமிக்க பயன்படுத்தப்படுகிறது. இது பல முகவர்களுக்கு "fan-out" மற்றும் முடிவுகளை ஒருங்கிணைக்க "fan-in" ஆகும்.

#### சூழல் பின்னணி

ஒரு பயனர் சியாட்டிலுக்கு ஒரு பயணத்தை திட்டமிட கேட்கிறார்.

1.  **Dispatcher (Fan-Out)**: பயனர் கோரிக்கை ஒரே நேரத்தில் இரண்டு முகவர்களுக்கு அனுப்பப்படுகிறது.
2.  **Researcher-Agent**: சியாட்டிலில் டிசம்பரில் ஒரு பயணத்திற்கான ஈர்ப்புகள், வானிலை மற்றும் முக்கிய கருத்துகளை ஆராய்கிறது.
3.  **Plan-Agent**: தனித்துவமாக ஒரு விரிவான நாள்-தின பயண திட்டத்தை உருவாக்குகிறது.
4.  **Aggregator (Fan-In)**: ஆராய்ச்சியாளர் மற்றும் திட்டமிடுபவரின் வெளியீடுகள் ஒருங்கிணைக்கப்பட்டு இறுதி முடிவாக வழங்கப்படுகின்றன.

*Concurrent Researcher மற்றும் Planner Workflow-இன் வரைபடம்.*

#### Python செயல்பாட்டு பகுப்பாய்வு

`ConcurrentBuilder` இந்த முறைமையை உருவாக்க எளிமைப்படுத்துகிறது. நீங்கள் பங்கேற்கும் முகவர்களின் பட்டியலை வழங்கினால், Builder தானாகவே தேவையான fan-out மற்றும் fan-in logic-ஐ உருவாக்குகிறது.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework `research_agent` மற்றும் `plan_agent` ஒரே நேரத்தில் செயல்படுவதை உறுதிசெய்கிறது, மேலும் அவர்களின் இறுதி வெளியீடுகள் ஒரு பட்டியலாக ஒருங்கிணைக்கப்படுகின்றன.

#### .NET (C\#) செயல்பாட்டு பகுப்பாய்வு

.NET-இல், இந்த முறைமையானது மேலும் தெளிவான வரையறையை தேவைப்படுகிறது. Custom Executors (`ConcurrentStartExecutor` மற்றும் `ConcurrentAggregationExecutor`) fan-out மற்றும் fan-in logic-ஐ நிர்வகிக்க உருவாக்கப்படுகின்றன.

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

`WorkflowBuilder` பின்னர் `AddFanOutEdge` மற்றும் `AddFanInEdge` பயன்படுத்தி இந்த Custom Executors மற்றும் முகவர்களுடன் Graph-ஐ உருவாக்குகிறது.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### வழக்கு 4: நிபந்தனையுடன் Workflow

நிபந்தனையுடன் Workflow-கள் branching logic-ஐ அறிமுகப்படுத்துகின்றன, இது இடைநிலை முடிவுகளின் அடிப்படையில் வெவ்வேறு பாதைகளை எடுக்க அனுமதிக்கிறது.

#### சூழல் பின்னணி

இந்த Workflow ஒரு தொழில்நுட்ப பயிற்சியை உருவாக்கி வெளியிடுவதைக் தானியங்கமாக்குகிறது.

1.  **Evangelist-Agent**: கொடுக்கப்பட்ட சுருக்கம் மற்றும் URLs அடிப்படையில் பயிற்சியின் ஒரு வரைவை எழுதுகிறது.
2.  **ContentReviewer-Agent**: வரைவை மதிப்பீடு செய்கிறது. இது வார்த்தை எண்ணிக்கை 200 வார்த்தைகளைத் தாண்டுகிறதா என்பதைச் சரிபார்க்கிறது.
3.  **நிபந்தனையுடன் கிளை**:
      * **Approved (`Yes`) என்றால்**: Workflow `Publisher-Agent`-க்கு தொடர்கிறது.
      * **Rejected (`No`) என்றால்**: Workflow நிறுத்தி மறுப்புக்கான காரணத்தை வெளியிடுகிறது.
4.  **Publisher-Agent**: வரைவு அங்கீகரிக்கப்பட்டால், இந்த முகவர் உள்ளடக்கத்தை Markdown கோப்பாக சேமிக்கிறது.

#### Python செயல்பாட்டு பகுப்பாய்வு

இந்த உதாரணம் `select_targets` என்ற Custom Function-ஐ பயன்படுத்தி நிபந்தனையுடன் logic-ஐ செயல்படுத்துகிறது. இந்த Function `add_multi_selection_edge_group`-க்கு அனுப்பப்படுகிறது மற்றும் `review_result` புலத்தின் அடிப்படையில் Workflow-ஐ வழிநடத்துகிறது.

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

`to_reviewer_result` போன்ற Custom Executors, முகவர்களின் JSON வெளியீட்டை Strongly-Typed Objects-ஆக மாற்றி, Selection Function ஆய்வு செய்ய அனுமதிக்கிறது.

#### .NET (C\#) செயல்பாட்டு பகுப்பாய்வு

.NET பதிப்பு ஒரு நிபந்தனை Function-ஐ பயன்படுத்தி இதே அணுகுமுறையை பின்பற்றுகிறது. `Func<object?, bool>` வரையறுக்கப்படுகிறது, இது `ReviewResult` பொருளின் `Result` பண்பைச் சரிபார்க்கிறது.

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

`AddEdge` முறைமையின் `condition` அளவுரு `WorkflowBuilder`-ஐ ஒரு branching பாதையை உருவாக்க அனுமதிக்கிறது. Workflow `publishExecutor`-க்கு Edge-ஐ பின்பற்றும், `GetCondition(expectedResult: "Yes")` உண்மையைத் திருப்பினால். இல்லையெனில், இது `sendReviewerExecutor` பாதையைப் பின்பற்றும்.

## முடிவு

Microsoft Agent Framework Workflow பல முகவர் அமைப்புகளை ஒருங்கிணைக்க வலுவான மற்றும் நெகிழ்வான அடித்தளத்தை வழங்குகிறது. அதன் Graph-அடிப்படையிலான கட்டமைப்பு மற்றும் முக்கிய கூறுகளைப் பயன்படுத்தி, Python மற்றும் .NET-இல் சிக்கலான Workflow-களை வடிவமைத்து செயல்படுத்த முடியும். உங்கள் பயன்பாடு எளிய தொடர்ச்சியான செயலாக்கம், ஒரே நேரத்தில் செயல்பாடு அல்லது dinamic நிபந்தனையுடன் logic தேவைப்படுகிறதா என்பதை பொருத்து, Framework வலுவான, அளவிடக்கூடிய மற்றும் Type-Safe AI-ஆதாரமான தீர்வுகளை உருவாக்க தேவையான கருவிகளை வழங்குகிறது.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.