# Microsoft Agent Framework Workflow உடன் பன்முக முகவர் பயன்பாடுகளை உருவாக்குதல்

இந்த பயிற்சிப் பகுதி Microsoft Agent Frameworkஐப் பயன்படுத்தி பன்முக முகவர் பயன்பாடுகளைப் புரிந்துகொள்வதிலும் உருவாக்குவதிலும் உங்களைக் வழிநடத்தும். பன்முக முகவர் அமைப்புகளின் அடிப்படைக் கருத்துக்களை ஆராய்ந்து, இந்த அமைப்பின் Workflow பகுதிக்கான கட்டமைப்பை அறிந்து, பைத்தான் மற்றும் .NET ஆகிய இரண்டிலும் பல்வேறு workflow வடிவமைப்புகளுக்கான நடைமுறை எடுத்துக்காட்டுக்களுடன் பயணம் செய்வோம்.

## 1\. பன்முக முகவர் அமைப்புகளைப் புரிதல்

ஒரு AI முகவர் என்பது ஒரு சாதாரண பெரிய மொழி மாதிரி (LLM) திறன்களை மீறிய ஒரு அமைப்பு ஆகும். இது சூழலை உணரக்கூடியது, முடிவுகள் எடுக்கக்கூடியது மற்றும் குறிப்பிட்ட குறிக்கோள்களை அடைவதற்காக செயல்படக்கூடியது. பன்முக முகவர் அமைப்பு என்பது பல முகவர்கள் ஒன்றிணைந்து கூட்டு முயற்சிகளால் ஒரு பிரச்சினையை சரி செய்ய அறிந்து, தனி முகவரால் மட்டுமல்லாமல் கடினமாக இருப்பதை எளிமையாக்கின்றது.

### பொதுவான பயன்பாட்டு காட்சிகள்

  * **சிக்கலான பிரச்சினைகள் தீர்க்கல்**: ஒரு பெரிய பணியை (எ.கா., ஒரு நிறுவன முழுவதும் உள்ள நிகழ்வை திட்டமிடுதல்) சிறிய துணை பணிகளாக பாகுபடுத்தி, குறிப்பிட்ட திறன் வாய்ந்த முகவர்கள் (எ.கா., பட்ஜெட் முகவர், லாஜிஸ்டிக்ஸ் முகவர், சந்தைப்படுத்தல் முகவர்) அதனை கையாள்ந்து தீர்க்கும்.
  * **இயந்திர உதவியாளர்கள்**: ஒரு முதன்மை உதவியாளர் முகவர், அட்டவணை அமைத்தல், ஆய்வு மற்றும் முன்பதிவு போன்ற பணிகளை பிற திறமை வாய்ந்த முகவர்களுக்கு ஒப்படைக்கும்.
  * **தானாக உள்ளடக்கத்தை உருவாக்குதல்**: ஒரு workflowல் ஒருமுகவர் உள்ளடக்கத்தை எழுதுகிறான், மற்றொருவர் சரிபார்க்கிறான், மூன்றாவது வெளியிடுகிறான்.

### பன்முக முகவர் வடிவமைப்புகள்

பன்முக முகவர் அமைப்புகள் பரஸ்பரம் எந்த விதத்தில் செயல்படுகின்றன என்பது கீழ்காணும் வடிவங்களில் ஒருவகை அமைக்கப்படும்:

  * **வரிசைப்படி**: முகவர்கள் முன்கூட்டியே நிர்ணயிக்கப்பட்ட வரிசையில் பணியாற்றுவார்கள். ஒருவரின் பழுது அடுத்தவரின் உள்ளீடாக ஆகும்.
  * **ஒரே சமயம்**: முகவர்கள் ஒரே நேரத்தில் வேறுபட்ட பாகங்களை வேலை செய்கின்றனர், அவர்களின் முடிவுகள் amass செய்து கூற்றாக அமைக்கப்படும்.
  * **நிபந்தனை அடிப்படையிலான**: முகவரின் முடிவின் அடிப்படையில் workflow வேறுபட்ட பாதைகளை பின்பற்றும், if-then-else போன்ற ஆம்சத்தைப் போன்றது.

## 2\. Microsoft Agent Framework Workflow கட்டமைப்பு

Agent Frameworkஇன் workflow அமைப்பு பல முகவர்களுக்கிடையேயான சிக்கலான தொடர்புகளை நிர்வகிக்க வடிவமைக்கப்பட்ட மேம்பட்ட ஒருங்கிணைப்பு இயந்திரமாகும். இது [Pregel-பாணி செயலாக்க மாதிரி](https://kowshik.github.io/JPregel/pregel_paper.pdf) அடிப்படையில் கட்டப்பட்ட ஒருகிராப் கட்டமைப்பில் "supersteps" என அழைக்கப்படும் ஒரே நேரத்தில் முன்னேற்றப்படும் படிகளைப் பயன்படுத்துகிறது.

### முக்கிய கூறுகள்

கட்டமைப்பு மூன்று முக்கிய பகுதிகளாயுள்ளது:

1.  **நிறைவாளர்கள்**: இவை அடிப்படைக் செயலாக்க அலகுகள். எங்கள் எடுத்துக்காட்டுகளில் `Agent` என்பது ஒரு நிறைவாளரின் வகை. ஒவ்வொரு நிறைவாளருக்கும் பல அறிவிப்புகளுக்கு பதில் அளிக்கும் செய்தி கையாள்பவர்கள் உள்ளனர்.
2.  **எட்ஜுகள்**: நிறைவாளர்களுக்கு இடையேயான செய்தித் தொடர்பின் பாதையை நிர்ணயிக்கின்றன. நிறைவுகள் உள்ளடக்கிய வழிகளுக்குச் சிக்கலான வழிசெலுத்தல் அம்சங்களை வழங்குகின்றன.
3.  **Workflow**: முழு சோதனையை ஒருங்கிணைக்கும் பகுதியாக செயல்படுகிறது, நிறைவாளர்கள், எட்ஜுகள் மற்றும் முழுச்செயலின் பராமரிப்பிலும் கவனம் செலுத்துகிறது.

*Workflow அமைப்பின் முக்கிய கூறுகளை விளக்கும் வரைபடம்.*

இந்த கட்டமைப்பு வலுவான பின்தொடர்பு தொடர், சமாலோசம்/முதன்மை வரிசை மற்றும் கட்டுப்பாட்டு நிலைதவிர்க்கும் கூறுகளைப் பயன்படுத்தி வலுவான மற்றும் விரிவாக்கக்கூடிய பயன்பாடுகளை உருவாக்க அனுமதிக்கும்.

## 3\. நடைமுறை எடுத்துக்காட்டுகள் மற்றும் குறியீடு பகுப்பாய்வு

இப்பொழுது இந்த frameworkஐப் பயன்படுத்தி பலவகை workflow வடிவமைப்புகளை நிகழ்த்துவதைக் காணலாம். பைத்தான் மற்றும் .NET இரண்டிலும் குறியீடு காண்போம்.

### வழக்கு 1: அடிப்படை வரிசை Workflow

இது எளிதான வடிவம், ஒரு முகவரின் வெளியீடு ஒன்றுக்கு நேரடியாக அனுப்பப்படுகின்றது. எங்கள் காட்சி ஒன்று ஹோட்டல் `FrontDesk` முகவர் பயண பரிந்துரையை செய்கிறார், அதன் பின்னர் `Concierge` முகவர் அதனை மதிப்பீடு செய்கிறார்.

*அடிப்படை FrontDesk -> Concierge workflow வரைபடம்.*

#### நிலை பின்னணி

ஒரு பயணி பாரீசில் பரிந்துரையை கேட்கிறார்.

1.  குறுகிய வடிவில் உருவாக்கப்பட்ட `FrontDesk` முகவர் லூவரா அருங்காட்சியகம் பார்வையிட பரிந்துரைக்கிறார்.
2.  உண்மையான அனுபவத்தை முன்னிறுத்தும் `Concierge` முகவர் பரிந்துரையை பெறுகிறார். பரிந்துரையை மதிப்பாய்வு செய்து மேலும் நெருங்கிய மற்றும் குறைவான சுற்றுலாத்துறை மூலம் மாற்றை பரிந்துரை செய்கிறார்.

#### பைத்தான் நடைமுறை குறியீடு பகுப்பாய்வு

பைத்தான் எடுத்துக்காட்டில் முதலில் இரண்டு முகவர்களை வரையறுக்கின்றோம், ஒவ்வொன்றிற்குமான குறிப்பிட்ட வழிகாட்டல்களுடன்.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# முகவர் பாத்திரங்களையும் வழிமுறைகளையும் வரையறுக்கவும்
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# முகவர் எடுத்துக்காட்டுக்களை உருவாக்கவும்
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

அதன் பின் `WorkflowBuilder` ஐ பயன்படுத்தி கிராப் கட்டப்படுகிறது. `front_desk_agent` தொடக்கமாக அமைக்கப்பட்டு அதனைப் பின்னர் `reviewer_agent`க்கு இணைக்கும் ஒரு முகவரி உருவாக்கப்படுகிறது.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

இறுதியில் workflow ஆரம்ப பாவனையாளர் கோரிக்கையுடன் இயக்கப்படுகிறது.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run வேலைவாயிலின் செயலை நடத்தியது; get_outputs() வெளியீட்டு செயற்காரரின் முடிவை அளிக்கிறது.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) நடைமுறை குறியீடு பகுப்பாய்வு

.NET நடைமுறைது மிகுந்த ஒத்த வாரிய logicஐ பின்பற்றுகிறது. முதலில் முகவர்களின் பெயர்கள் மற்றும் வழிகாட்டல்கள் முனைப்படுத்தப்படுகின்றன.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

`AzureOpenAIClient` (Responses API) மூலம் முகவர்கள் உருவாக்கப்படுகின்றனர், பின்னர் `WorkflowBuilder` மூலம் `frontDeskAgent` இல் இருந்து `reviewerAgent`க்கு வரிசைப்படி இணைப்பு சேர்க்கப்படுகிறது.

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

workflow பின் பயனாளரின் செய்தியுடன் இயக்கப்பட்டு முடிவுகள் தானாக வரிசைப்படுத்தி வழங்கப்படுகின்றன.

### வழக்கு 2: பலநிலை வரிசை Workflow

இந்த வடிவம் அடிப்படை வரிசையை மேலும் விரிவாக்கி பல முகவர்களை உள்ளடக்கியது. இது பல கட்ட விபராதிகள் அல்லது மாற்றங்கள் தேவைப்படும் செயலாக்கங்களுக்கு மிக உகந்தது.

#### நிலை பின்னணி

ஒரு பயனர் ஒரு வீட்டறை படத்தை வழங்கி அமர்வு பொருட்களின் விலை குறிப்பை கோருகிறார்.

1.  **விற்பனை முகவர்**: படத்தில் உள்ள பொருட்களை அடையாளம் கண்டு பட்டியலை உருவாக்குகிறார்.
2.  **விலை முகவர்**: பொருட்களின் பட்டியலை நிறைவு செய்ய விலை விரிவுரை, பட்ஜெட் முதல் பிரீமியம் வரை வழங்குகிறார்.
3.  **கீழ்க் கட்டளை முகவர்**: விலைப்பட்டியலை பெறுவதற்கு பின் Markdown வடிவிலான அதிகாரப்பூர்வக் குறிப்பிடலாக மாற்றுகிறார்.

* விற்பனை -> விலை -> குறிப்பிடல் workflow வரைபடம்.*

#### பைத்தான் நடைமுறை குறியீடு பகுப்பாய்வு

மூன்று முகவர்கள் ஒவ்வொருவரும் சிறப்பு செயல்பாட்டுடன் வரையறுக்கப்படுகின்றனர். `add_edge` மூலம் தொடர் ஏற்படுத்தி workflow உருவாக்கப்படுகிறது: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# மூன்று சிறப்பு ஏஜெண்ட்களை உருவாக்கவும்
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# வரிசையான வேலைஅழுவை அமைக்கவும்
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

உள்ளீடு ஒரு `ChatMessage` ஆகும், அதில் உரை மற்றும் பட URI இரண்டும் உள்ளது. இதில் ஒவ்வொரு முகவரின் வெளியீடும் அடுத்த முகவருக்கு தரப்படுகிறது இறுதியில் குறிப்பிடல் உருவாக்கும் வரை.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# பயனர் செய்தியில் உரையும் படம் இரண்டும் உள்ளன
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# வேலையினை இயக்குக
events = await workflow.run(message)
```

#### .NET (C\#) நடைமுறை குறியீடு பகுப்பாய்வு

.NET எடுத்துக்காட்டு பைத்தான் பதிப்பைப் போலவே செயல்படுகிறது. மூன்று முகவர்கள் (`salesagent`, `priceagent`, `quoteagent`) உருவாக்கப்படுகின்றனர். `WorkflowBuilder` அவர்கள் வரிசைப்படி இணைக்கப்படுகின்றனர்.

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

பயனாளரின் செய்தி படத் தரவும் உரை வழிகாட்டலும் கொண்டதாக உருவாக்கப்பட்டு, `InProcessExecution.StreamAsync` வழியாக workflow துவக்கப்பட்டுப் அதன் முடிவு ஸ்ட்ரீமாக பெற்றுக்கொள்ளப்படுகிறது.

### வழக்கு 3: ஒரே நேரத்தில் Workflow

இது பணிகளை ஒரே நேரத்தில் செய்து நேரத்தை சேமிக்க பயன்படும். பல முகவர்களுக்கு (fan-out) மற்றும் முடிவுகளைத் திரட்ட (fan-in) செய்கிறது.

#### நிலை பின்னணி

பயனர் சீயாட்டில் பயணத்தை திட்டமிட கேட்கிறார்.

1.  **பங்காளி (Fan-Out)**: பயனரின் கோரிக்கை இரண்டு முகவர்களுக்கு ஒரே நேரத்தில் அனுப்பப்படுகிறது.
2.  **ஆய்வாளர் முகவர்**: சீயாட்டிலில் டிசம்பரில் பார்க்க வேண்டிய இடங்கள், வானிலை மற்றும் மற்ற முக்கிய அம்சங்களை ஆராய்கிறார்.
3.  **திட்டமிடுபவர் முகவர்**: தனித்தன்னாகப் பயண அட்டவணையை தினாந்தரியாக உருவாக்குகிறார்.
4.  **திரட்டிப்பவர் (Fan-In)**: ஆய்வாளர் மற்றும் திட்டக்காரரின் முடிவுகளை ஒன்று சேர்த்து இறுதியான விளைவாக வழங்குகிறார்.

*ஒரே நேரத்தில் ஆய்வாளர் மற்றும் திட்டமிடுபவர் workflow வரைபடம்.*

#### பைத்தான் நடைமுறை குறியீடு பகுப்பாய்வு

`ConcurrentBuilder` இந்த வடிவமைப்பை எளிமையாக்கும். ஐந்து ஆர் பங்கேற்கும் முகவர்களை எழுதுவதுடன், தேவையான fan-out மற்றும் fan-in ளogical களை தானாக உருவாக்குகின்றது.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder ரசிகர் வெளியீடு/அவுட் மூலம் உள்ளீடு தர்கத்தை கையாளும்
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# வேலைபடத்தை செயல்படுத்துக
events = await workflow.run("Plan a trip to Seattle in December")
```

framework `research_agent` மற்றும் `plan_agent` ஒரே நேரத்தில் இயங்குவதை உறுதி செய்கிறது மற்றும் இறுதிப் பலன் ஒரு பட்டியலாக சேகரிக்கப்படுகிறது.

#### .NET (C\#) நடைமுறை குறியீடு பகுப்பாய்வு

.NET இல் இது மிகவும் தெளிவான வரையறைகளோடு வருகிறது. முற்போக்கான நிறைவாளர்கள் (`ConcurrentStartExecutor` மற்றும் `ConcurrentAggregationExecutor`) fan-out மற்றும் fan-in logic களை கையாள உருவாக்கப்படுகின்றன.

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

பின்னர் `WorkflowBuilder` `AddFanOutEdge` மற்றும் `AddFanInEdge` களை பயன்படுத்தி இந்த அமைப்புகளோடு workflow உருவாக்குகிறது.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### வழக்கு 4: நிபந்தனை அடிப்படையிலான Workflow

நிபந்தனை அடிப்படையிலான workflowகள் கிளைப்பட்டு காரணிகளின் முடிவுகளின் அடிப்படையில் வேறுபட்ட பாதைகள் பின்பற்ற அனுமதிக்கின்றன.

#### நிலை பின்னணி

இந்த workflow தொழில்நுட்ப பயிற்சியைத் தானாக உருவாக்கி வெளியிடும்.

1.  **Evangelist-முகவர்**: குறிப்பிட்ட உருபடிகள் மற்றும் URLகளின் அடிப்படையில் பயிற்சிக் கட்டுரைக்கான வரைவோடு எழுதுகிறார்.
2.  **ContentReviewer-முகவர்**: வரையை மதிப்பாய்வு செய்கிறான். உரை பருமன் 200 வார்த்தைகளைத் தாண்டியுள்ளதா என சரிபார்க்கின்றார்.
3.  **நிபந்தனை கிளை**:
      * **அனுமதிக்கப்பட்டால் (`ஆம்`)**: workflow `Publisher-முகவருக்கு` தொடர்கிறது.
      * **நிராகரிக்கப்பட்டால் (`இல்லை`)**: workflow நிறுத்தப்படுகின்றது மற்றும் நிராகரிப்பின் காரணம் வெளியிடப்படுகின்றது.
4.  **Publisher-முகவர்**: வரைவோடு ஏற்றுக்கொள்ளப்பட்டால், இந்த முகவர் உள்ளடக்கத்தை Markdown கோப்பாக சேமிக்கிறார்.

#### பைத்தான் நடைமுறை குறியீடு பகுப்பாய்வு

இந்த எடுத்துக்காட்டில் சுயவிவர செயல்பாட்டான `select_targets` பயன்படுத்தி நிபந்தனை இயங்க வேண்டும். இது `add_multi_selection_edge_group`க்கு வழிநடத்துகிறது மற்றும் `reviewer` வெளியீட்டின் `review_result` புலத்தின் அடிப்படையில் workflow ஐ இயக்குகிறது.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# இந்த செயலி மதிப்பாய்வு முடிவின் அடிப்படையில் அடுத்த நடவடிக்கையை தீர்மானிக்கிறது
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # அனுமதிக்கப்பட்டால், 'save_draft' நிர்வாகி அருகே செல்லவும்
        return [save_draft_id]
    else:
        # மறுத்தால், தோல்வியை அறிக்கையிட 'handle_review' நிர்வாகி அருகே செல்லவும்
        return [handle_review_id]

# வேலைப்பருவ கட்டுமானி வழித்தடமிட தேர்வு செயலியைப் பயன்படுத்துகிறது
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # பன்மைத் தேர்வு எடு நிலைமையான தர்க்கத்தை செயல்படுத்துகிறது
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` போன்ற சுயவிவர நிறைவாளர்கள் JSON வெளியீட்டை பலவகைப்படுத்தி தேர்வு செயல்பாட்டிற்கு காணும் வகையில் மாற்றுகின்றனர்.

#### .NET (C\#) நடைமுறை குறியீடு பகுப்பாய்வு

.NET பதிப்பில் சமமான அணுகுமுறை உள்ளது. `Func<object?, bool>` வடிவில் ஒரு நிபந்தனை செயல்பாட்டு உருவாக்கப்பட்டுள்ளது, இது `ReviewResult` பிராமணத்தின் `Result` மூலம் சரிபார்க்கின்றது.

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

`AddEdge` முறையின் `condition` அளவுருவும் `WorkflowBuilder`க்கு கிளைப்பட்டு பாதையை உருவாக்க அனுமதிக்கிறது. `GetCondition(expectedResult: "Yes")` நிபந்தனை உண்மை என்றால், workflow `publishExecutor`க்கு செல்லும், இல்லையெனில் `sendReviewerExecutor`க்கு செல்லும்.

## முடிவு

Microsoft Agent Framework Workflow நுட்பமான, பல முகவர் அமைப்புகளை ஒருங்கிணைக்கும் வலுவான மற்றும் விரிவான அடிப்படையைக் கொடுக்கிறது. அதன் கிராப் அடிப்படையிலான கட்டமைப்பு மற்றும் முக்கிய கூறுகளை பயன்படுத்தி, டெவலப்பர்கள் பைத்தான் மற்றும் .NET இரண்டிலும் இளம் workflowகளை வடிவமைத்து செயல்படுத்தலாம். எங்கும் உங்கள் பயன்பாடு எளிய வரிசை செயலாக்கம், ஒருமுக செயலாக்கம் அல்லது தநி நிபந்தனை இயங்குதல் ஆர்வமாக இருந்தாலும், இந்த framework வலுவான, விரிவாக்கக்கூடிய மற்றும் வகை பாதுகாப்பான AI இயக்கப்பட்ட தீர்வுகளை உருவாக்க தேவையான கருவிகளை வழங்குகிறது.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->