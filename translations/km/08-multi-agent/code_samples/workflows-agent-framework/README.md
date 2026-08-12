# ការសាងសង់កម្មវិធីភាគីច្រើនជាមួយ Microsoft Agent Framework Workflow

មេរៀននេះនឹងណែនាំអ្នកឱ្យយល់ដឹង និងបង្កើតកម្មវិធីភាគីច្រើន ប្រើប្រាស់ Microsoft Agent Framework។ យើងនឹងស្វែងយល់ពីគំនិតមូលដ្ឋាននៃប្រព័ន្ធភាគីច្រើន ជ្រាបស្ថាបត្យកម្មនៃធាតុ Workflow របស់ framework និងធ្វើដំណើរកម្មវិធីជាក់ស្តែងក្នុង Python និង .NET សម្រាប់លំនាំ workflow ផ្សេងៗ។

## 1\. ការយល់ដឹងអំពីប្រព័ន្ធភាគីច្រើន

អ្នកតំណាង AI (AI Agent) គឺជាប្រព័ន្ធមួយដែលមានសមត្ថភាពលើសពី Model ភាសាធំទូទៅ (LLM)។ វាអាចចាប់ការយល់ដឹងពីបរិយាកាសរបស់វា សម្រេចចិត្ត និងអនុវត្តន៍សកម្មភាពដើម្បីសម្រេចគោលដៅជាក់លាក់មួយ។ ប្រព័ន្ធភាគីច្រើន ជាប្រព័ន្ធដែលមានភាគីជាច្រើនសហការគ្នាដើម្បីដោះស្រាយបញ្ហាមួយ ដែលលំបាកឬមិនអាចសម្រេចបានដោយភាគីមួយតែប៉ុណ្ណោះ។

### សถานการณ์កម្មវិធីទូទៅ

  * **ដោះស្រាយបញ្ហាស្មុគស្មាញ**៖ ការបែងចែកការងារធំមួយ (ឧ. ការរៀបចំព្រឹត្តការណ៍ក្រុមហ៊ុន) ជាការងារតូចៗ ដែលបានចែកគ្រប់គ្រងដោយភាគីដែលមានជំនាញជាក់លាក់ (ឧ. ភាគីថវិកា ភាគីផលិតកម្ម និងភាគីផ្សព្វផ្សាយ)។
  * **ជំនួយក័ត់សម្រាប់ជំនួយការពិតធ្វើការ**៖ អ្នកជំនួយការចម្បង ដែលចាត់ទុកបំណងដូចការតែងម៉ោង ស្រាវជ្រាវ និងកក់បង្កប់នៅឲ្យភាគីជំនាញផ្សេង។
  * **បង្កើតមាតិកាដោយស្វ័យប្រវត្តិ**៖ លំនាំ workflow ដែលភាគីមួយនិពន្ធមាតិកា ផ្នែកមួយពិនិត្យប្រាកដភាព និងសម្លេង ខណៈដែលភាគីមួយផ្សព្វផ្សាយវា។

### លំនាំការប្រព្រឹត្តិ Multi-Agent

ប្រព័ន្ធភាគីច្រើនអាចត្រូវបានរៀបចំជាលំនាំជាច្រើន ដែលកំណត់ពីរបៀបចាប់លេខធ្វើការរួមគ្នា៖

  * **រៀងតាមលំដាប់**៖ ភាគីធ្វើការតាមលំដាប់បានកំណត់ ដូចបន្ទាត់សមាសធាតុ។ ផលិតផលរបស់ភាគីមួយក្លាយជាពត៌មានបញ្ចូលសម្រាប់ភាគីបន្ទាប់។
  * **ប្រព័ន្ធប្រតិបត្តិការស្រដៀងគ្នា**៖ ភាគីធ្វើការរួមគ្នានៅផ្នែកខុសៗគ្នានៃការងារ ហើយលទ្ធផលរបស់ពួកគេត្រូវបានបញ្ចូលគ្នាក្នុងចុងក្រោយ។
  * **លក្ខខណ្ឌ**៖ Workflow ទៅតាមផ្លូវផ្សេងៗដោយផ្អែកលើលទ្ធផលរបស់ភាគី មុនដូចដូចប្រការហ្នឹងបើ-តែ-ផ្សេង។

## 2\. ស្ថាបត្យកម្ម Microsoft Agent Framework Workflow

ប្រព័ន្ធ workflow របស់ Agent Framework គឺជាម៉ាស៊ីនមេកានិចដំណើរការលំរាំងខ្ពស់ដែលត្រូវបានរចនាឡើងដើម្បីគ្រប់គ្រងអន្តរកម្មស្មុគស្មាញរវាងភាគីជាច្រើន។ វាត្រូវបានកសាងលើស្ថាបត្យកម្មផ្អែកលើក្រាហ្វដែលប្រើ [ម៉ូដែលប្រតិបត្តិការបែប Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf) ដែលដំណើរការបាននៅជាដំណាក់កាលសម្របសម្រួលគ្នាដូចជា "supersteps"។

### ធាតុគន្លឹះ

ស្ថាបត្យកម្មនេះរួមមានផ្នែកសំខាន់ចំនួនបី៖

1.  **អ្នកអនុវត្តការងារ (Executors)**៖ ជាឯកតាបំផុតនៃការប្រតិបត្តិ។ នៅក្នុងឧទាហរណ៍របស់យើង `Agent` គឺជាប្រភេទមួយនៃ executor។ រាល់ executor អាចមានអ្នកដំណើរការសារច្រើនដែលត្រូវបានហៅដោយស្វ័យប្រវត្តិតាមប្រភេទនៃសារ។
2.  **ផ្សារ (Edges)**៖ កំណត់ផ្លូវសារធ្វើដំណើរវិញរវាង executors ។ ផ្សារអាចមានលក្ខខណ្ឌ ដែលអនុញ្ញាតឱ្យផ្លូវពត៌មានប្រែប្រួលបាននៅក្នុងក្រាហ្វ workflow។
3.  **Workflow**៖ ធាតុនេះសម្របសម្រួលដំណើរការទាំងមូល ចាត់ចែង executors ផ្សារ និងហេដ្ឋារចនាសម្ព័ន្ធរបស់ការប្រតិបត្តិការ។ វាធ្វើអោយប្រាកដថាសារត្រូវបានដំណើរការត្រឹមត្រូវ និងចាក់ផ្សាយព្រឹត្តិការណ៍សម្រាប់ការតាមដាន។

*រូបភាពបង្ហាញធាតុគន្លឹះនៃប្រព័ន្ធ workflow ។*

រចនាសម្ព័ន្ធនេះអនុញ្ញាតឱ្យសាងសង់កម្មវិធីដែលមានស្ថេរភាព និងអាចពង្រីកបានដោយប្រើលំនាំមូលដ្ឋានដូចជា ខ្សែរប្រតិបត្តិការរៀងតាមលំដាប់ ការបំបែក និងការបង្រួមសម្រាប់ការប្រតិបត្តិការជាស្រដៀងគ្នា និងតំណភ្ជាប់ប្តូរតាមលក្ខខណ្ឌសម្រាប់ចរន្តលក្ខខណ្ឌ។

## 3\. ឧទាហរណ៍ជាក់ស្តែងនិងវិភាគកូដ

ឥឡូវនេះយើងមកស្រាវជ្រាវពីរបៀបអនុវត្តលំនាំ workflow ផ្សេងៗប្រើ framework។ យើងនឹងមើលកូដទាំង Python និង .NET សម្រាប់នីតិវិធីនីមួយៗ។

### ករណីទី 1: Workflow រៀងតាមលំដាប់មូលដ្ឋាន

នេះគឺជាលំនាំសាមញ្ញបំផុត ដែលផលចេញរបស់ភាគីមួយត្រូវបានផ្ញើជាប់ទៅភាគីមួយទៀត។ ស្ថានការណ៍របស់យើងរួមមានភាគី `FrontDesk` នៃសណ្ឋាគារដែលផ្តល់អនុសាសន៍ធ្វើដំណើរ ហើយបន្ទាប់មកភាគី `Concierge` មកពិនិត្យមើល។

*រូបភាពកម្មវិធី workflow FrontDesk -> Concierge ។*

#### ផ្នែកផ្ទៃខាងក្រោយនៃស្ថានការណ៍

អ្នកដំណើរម្នាក់ស្នើសុំអនុសាសន៍នៅទីក្រុងប៉ារីស។

1.  ភាគី `FrontDesk` ដែលរចនាសម្រាប់ភាពសង្ខេប ផ្តល់អនុសាសន៍ទៅសារមន្ទីរលូវរ។
2.  ភាគី `Concierge` ដែលអនុវត្តភាពពិតប្រាកដ ទទួលអនុសាសន៍នេះ ពិនិត្យ និងផ្តល់មតិយោបល់ ដាក់អនុសាសន៍ជាជម្រើសតំបន់មូលដ្ឋានដែលមានភាពទាក់ទាញយូរទូតិច។

#### វិភាគអនុវត្តPython

ក្នុងឧទាហរណ៍ Python យើងកំណត់ និងបង្កើតភាគីទាំងពីរ ជាមួយនឹងការណែនាំជាក់លាក់។

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# កំណត់តួនាទីនិងការណែនាំបណ្ដាញតំណាង
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# បង្កើតអង្គភាពតំណាង
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

បន្ទាប់មក `WorkflowBuilder` ត្រូវបានប្រើសំរាប់បង្កើតក្រាហ្វ។ `front_desk_agent` ត្រូវបានកំណត់ជាចំណុចចាប់ផ្តើម ហើយផ្លូវត្រូវបង្កើតដើម្បីភ្ជាប់ផលចេញរបស់វាទៅឲ្យ `reviewer_agent`។

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

ចុងក្រោយ workflow ត្រូវបានដំណើរការជាមួយសារ​ចាប់​ផ្តើម​ពីអ្នកប្រើ។

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run កំពុងធ្វើការប្រតិបត្តិវគ្គការងារ; get_outputs() ដំណើរការវិលត្រឡប់លទ្ធផលអ្នកបំពេញ។
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### វិភាគអនុវត្ត .NET (C#)

អនុវត្តន៍ .NET មានលក្ខណៈស្រដៀងគ្នាទាំងមូល។ ជាដំបូង វាកំណត់អថេរចំពោះឈ្មោះភាគី និងការណែនាំ។

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

ភាគីត្រូវបានបង្កើតដោយ `AzureOpenAIClient` (Responds API) ហើយបន្ទាប់មក `WorkflowBuilder` កំណត់លំនាំរៀងតាមលំដាប់ ដោយបន្ថែមផ្លូវពី `frontDeskAgent` ទៅ `reviewerAgent`។

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

Workflow ត្រូវបានបើកដំណើរការជាមួយសាររបស់អ្នកប្រើ ហើយលទ្ធផលត្រូវបានបញ្ចេញតាម stream។

###ករណីទី 2៖ Workflow រៀងតាមលំដាប់ជាច្រើនជំហាន

លំនាំនេះពង្រីកលំដាប់មូលដ្ឋាន ដើម្បីបញ្ចូលភាគីច្រើនជាងមុន។ វាសមស្របសម្រាប់ដំណើរការដែលត្រូវការស្តង់ដារជាច្រើនដំណាក់កាលសម្រាប់កែប្រែ ឬបម្លែងតម្លៃ។

#### ផ្នែកផ្ទៃខាងក្រោយនៃស្ថានការណ៍

អ្នកប្រើប្រាស់ផ្តល់រូបភាពបន្ទប់ទទួលភ្ញៀវ ហើយស្នើសុំតម្លៃគ្រឿងសង្ហារឹម។

1.  **Sales-Agent**៖ កំណត់គ្រឿងសង្ហារឹមក្នុងរូបភាព ហើយបង្កើតបញ្ជី។
2.  **Price-Agent**៖ ទទួលបញ្ជី និងផ្តល់ការបំបែកតម្លៃលម្អិត រួមមានជម្រើសថវិកាប្រាក់ សេរី និងបរិមាណខ្ពស់។
3.  **Quote-Agent**៖ ទទួលបញ្ជីដែលបានបិងចារតម្លៃ ហើយរៀបចំឯកសារជាឯកសារផ្លូវការជារូបមន្ត Markdown។

*រូបភាព workflow Sales -> Price -> Quote ។*

#### វិភាគអនុវត្ត Python

ភាគីចំនួនបីត្រូវបានកំណត់ ជាមួយតួនាទីជាក់លាក់។ Workflow ត្រូវបានបង្កើតដោយប្រើ `add_edge` ដើម្បីបង្កើតខ្សែ `sales_agent` -> `price_agent` -> `quote_agent`។

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# បង្កើតភ្នាក់ងារពិសេសបីនាក់
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# បង្កើតនូវបច្ចេកវិទ្យាការងារតាមលំដាប់លំដោយ
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

បញ្ចូលជាមួយ `ChatMessage` ដែលរួមបញ្ចូលអត្ថបទ និង URI រូបភាព។ Framework គ្រប់គ្រងការផ្ញើរវិញនូវលទ្ធផលរបស់គ្នាទៅភាគីបន្ទាប់តាមលំដាប់រហូតដល់ការបញ្ចប់កំណត់តម្លៃ។

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# សារអ្នកប្រើប្រាស់មានទាំងអត្ថបទ និងរូបភាព
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# ដំណើរការទ្រង់ទ្រាយធ្វើការ
events = await workflow.run(message)
```

#### វិភាគអនុវត្ត .NET (C#)

ឧទាហរណ៍ .NET ស្រដៀងនឹង Python។ ភាគីបី (`salesagent`, `priceagent`, `quoteagent`) ត្រូវបានបង្កើត។ `WorkflowBuilder` តភ្ជាប់តាមលំដាប់។

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

សាររបស់អ្នកប្រើត្រូវបានបង្កើតជាមួយទិន្នន័យរូបភាព (ជា bytes) និងសារ។ វិធីសាស្ត្រ `InProcessExecution.RunStreamingAsync` ចាប់ផ្តើម workflow ហើយលទ្ធផលចុងក្រោយត្រូវបានទាញយកពី stream។

### ករណីទី 3: Workflow ប្រតិបត្តិការស្រដៀងគ្នា

លំនាំនេះត្រូវបានប្រើពេលដែលអាចអនុវត្តការងាររួមគ្នាដើម្បីសន្សំសំចៃពេលវេលា។ វាពាក់ព័ន្ធនឹង fan-out ទៅភាគីច្រើន និង fan-in សម្រាប់ប្រមូលលទ្ធផល។

#### ផ្នែកផ្ទៃខាងក្រោយនៃស្ថានការណ៍

អ្នកប្រើស្នើសុំរៀបចំដំណើរកម្សាន្តទៅ Seattle។

1.  **Dispatcher (Fan-Out)**៖ សំណើរបស់អ្នកប្រើប្រាស់ត្រូវបានបញ្ជូនទៅភាគីពីរដោយស្រដៀងគ្នា។
2.  **Researcher-Agent**៖ ស្រាវជ្រាវទាក់ទងអាតណាក់ស្យុង អាកាសធាតុ និងចំណុចសំខាន់សម្រាប់ដំណើរកម្សាន្តទៅ Seattle ខែធ្នូ។
3.  **Plan-Agent**៖ រៀបចំផែនការដំណើរកម្សាន្តនីតិវិធីថ្ងៃដោយថ្ងៃដោយឡែក។
4.  **Aggregator (Fan-In)**៖ ប្រមូល និងបង្ហាញលទ្ធផលពីអ្នកស្រាវជ្រាវ និងអ្នករៀបចំផែនការជាលទ្ធផលចុងក្រោយ។

*រូបភាព workflow concurrent រវាង Researcher និង Planner ។*

#### វិភាគអនុវត្ត Python

`ConcurrentBuilder` ងាយស្រួលក្នុងការបង្កើតលំនាំនេះ។ អ្នកគ្រាន់តែបញ្ជីភាគីដែលចូលរួម ហើយ builder នឹងបង្កើត logic fan-out និង fan-in ដោយស្វ័យប្រវត្តិ។

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder គ្រប់គ្រងតុល្យភាព fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# បើកដំណើរការជំហានការងារ
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework ធានាថា `research_agent` និង `plan_agent` ប្រតិបត្តិការ đồng thời ហើយលទ្ធផលចុងក្រោយត្រូវបានប្រមូលនៅក្នុងបញ្ជី។

#### វិភាគអនុវត្ត .NET (C#)

ក្នុង .NET លំនាំនេះត្រូវការកំណត់បន្ថែម បញ្ជាក់ executor ផ្ទាល់ខ្លួន (`ConcurrentStartExecutor` និង `ConcurrentAggregationExecutor`) សម្រាប់ fan-out និង fan-in។

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

បន្ទាប់មក `WorkflowBuilder` ប្រើ `AddFanOutEdge` និង `AddFanInEdge` ដើម្បីបង្កើតក្រាហ្វជាមួយ executor ផ្ទាល់ខ្លួន និងភាគី។

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### ករណីទី 4: Workflow លក្ខខណ្ឌ

Workflow លក្ខខណ្ឌបញ្ចូល logic បំបែកផ្លូវ ដែលអនុញ្ញាតឱ្យប្រព័ន្ធទៅតាមផ្លូវផ្សេងដោយផ្អែកលើលទ្ធផលចម្ងល់មួយចំនួន។

#### ផ្នែកផ្ទៃខាងក្រោយនៃស្ថានការណ៍

Workflow នេះស្វ័យប្រវត្តិបង្កើត និងផ្សព្វផ្សាយមេរៀនបច្ចេកទេសមួយ។

1.  **Evangelist-Agent**៖ សរសេរជាអត្រារបស់មេរៀន ដោយផ្អែកលើសេចក្តីសង្ខេបនិង URL។
2.  **ContentReviewer-Agent**៖ ពិនិត្យមើលអត្រារៀបរាប់។ វាសាកល្បងថាចំនួនពាក្យលើសពី 200 ពាក្យឬទេ។
3.  **សំបុត្រលក្ខខណ្ឌ**៖
      * **បើអនុម័ត (`Yes`)**៖ Workflow បន្តទៅភាគី `Publisher-Agent`។
      * **បើបដិសេធ (`No`)**៖ Workflow ផ្អាក និងបង្ហាញហេតុផលបដិសេធ។
4.  **Publisher-Agent**៖ បើអត្រារបស់អត្រារួចហើយ ភាគីនេះរក្សាទុកមាតិកានៅឯកសារ Markdown។

#### វិភាគអនុវត្ត Python

ឧទាហរណ៍នេះប្រើមុខងារផ្ទាល់ខ្លួន `select_targets` ក្នុងការអនុវត្ត logic លក្ខខណ្ឌ។ មុខងារនេះត្រូវបានផ្ញើទៅ `add_multi_selection_edge_group` ហើយណែនាំ workflow ដោយផ្អែកលើផែនទី `review_result` ពីលទ្ធផលអ្នកពិនិត្យ។

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# មុខងារនេះកំណត់ជំហ៊ានបន្ទាប់ដោយផ្អែកលើលទ្ធផលពិនិត្យ
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # ប្រសិនបើបានអនុម័ត ចេញទៅកាន់កម្មវិធី 'save_draft'
        return [save_draft_id]
    else:
        # ប្រសិនបើបានបដិសេធ ចេញទៅកាន់កម្មវិធី 'handle_review' ដើម្បីរាយការណ៍ការបរាជ័យ
        return [handle_review_id]

# អ្នកសាងសង់ចរន្តការងារប្រើមុខងារជ្រើសរើសសម្រាប់បញ្ជូនផ្លូវ
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # គំនុំជម្រើសច្រើនអនុវត្តតុល្យភាពលក្ខខណ្ឌ
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Executor ផ្ទាល់ខ្លួនដូចជា `to_reviewer_result` ត្រូវបានប្រើដើម្បីបកប្រែក្នុងលទ្ធផល JSON ពីភាគី និងបម្លែងទៅជាវត្ថុ typed ដែលមុខងារជ្រើសរើសអាចពិនិត្យបាន។

#### វិភាគអនុវត្ត .NET (C#)

ជំនួស .NET ប្រើរបៀបស្រដៀងគ្នាជាមួយមុខងារលក្ខខណ្ឌ។ កំណត់ `Func<object?, bool>` ដើម្បីពិនិត្យលទ្ធផល `Result` នៃវត្ថុ `ReviewResult`។

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

វិធីសាស្ត្រ `AddEdge` ជាមួយប៉ារ៉ាម៉ែត្រ `condition` អនុញ្ញាតឱ្យ `WorkflowBuilder` បង្កើតផ្លូវបំបែក។ Workflow នឹងបន្តតាម edges ទៅ `publishExecutor` បើលក្ខខណ្ឌ `GetCondition(expectedResult: "Yes")` បង្រឹងភាពមែន។ បើមិនដូច្នោះវានឹងទៅទៅ `sendReviewerExecutor`។

## សេចក្ដីសន្និដ្ឋាន

Microsoft Agent Framework Workflow ផ្តល់មូលដ្ឋានដ៏រឹងមាំ និងបត់បែនសម្រាប់គ្រប់គ្រងប្រព័ន្ធភាគីច្រើនស្មុគស្មាញ។ ដោយប្រើស្ថាបត្យកម្មផ្អែកលើក្រាហ្វនិងធាតុគន្លឹះ វាអនុញ្ញាតឱ្យអ្នកអភិវឌ្ឍន៍រចនា និងអនុវត្ត workflow ដែលស្មុគស្មាញក្នុង Python និង .NET។ មិនថាកម្មវិធីរបស់អ្នកត្រូវការប្រតិបត្តិការរៀងតាមលំដាប់ ឬប្រតិបត្តិការស្រដៀងគ្នា ឬ logic លក្ខខណ្ឌផ្លាស់ប្ដូរ framework នឹងផ្គត់ផ្គង់ឧបករណ៍សម្រាប់បង្កើតដំណោះស្រាយ AI មានប្រសិទ្ធភាព អាចពង្រីកបាន និងមានសុវត្ថិភាពប្រភេទ។ 

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->