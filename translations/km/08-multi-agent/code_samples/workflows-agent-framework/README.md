# ការធ្វើកម្មវិធី Multi-Agent ជាមួយ Microsoft Agent Framework Workflow

មេរៀននេះនឹងដឹកនាំអ្នកឲ្យយល់ដឹង និងសាងសង់កម្មវិធី multi-agent ដោយប្រើ Microsoft Agent Framework។ យើងនឹងស្វែងយល់ពីមូលដ្ឋានរបស់ប្រព័ន្ធ multi-agent, ចុះទៅក្នុងរចនាសម្ព័ន្ធនៃទីផ្សារប្រតិបត្ដិ Workflow របស់Framework ហើយដើរតាមឧទាហរណ៍អនុវត្តក្នុងភាសា Python និង .NET សម្រាប់ប្លង់ workflow ផ្សេងៗ។

## 1\. ការយល់ពីប្រព័ន្ធ Multi-Agent

អ្នកប្រើប្រាស់ AI Agent គឺជាប្រព័ន្ធមួយដែលកាត់ផុតពីសមត្ថភាពរបស់គំរូភាសាធំ (LLM) មួយទូទៅ។ វាអាចយល់ពីបរិយាកាសរបស់វា កំណត់នូវការសម្រេចចិត្ត និងអនុវត្តន៍សកម្មភាពដើម្បីសម្រេចបានគោលដៅជាក់លាក់។ ប្រព័ន្ធ multi-agent រួមមានមានអ្នកប្រើប្រាស់ជាច្រើនរួមគ្នាដើម្បីដោះស្រាយបញ្ហាដែលអាចពិបាកឬមិនអាចធ្វើបានដោយភាគីតែមួយ។

### ស្ថានភាពប្រើប្រាស់ទូទៅ

  * **ការដោះស្រាយបញ្ហាស្មុគស្មាញ**: បំបែកកិច្ចការ​ធំព្រមាមួយ (ឧ., ការរៀបចំព្រឹត្តិការណ៍ក្រុមហ៊ុនទាំងមូល) ទៅជាកិច្ចការតូចៗ​ដែលត្រូវបានគ្រប់គ្រងដោយភាគីជំនាញ (ឧ., អ្នកភាគីថវិកា អ្នកភាគីឡូជីស្ទិក អ្នកភាគីទីផ្សារ)។
  * **ជំនួយការសំរាប់មនុស្ស**: អ្នកជំនួយការសំខាន់ម្នាក់ផ្ដាច់កិច្ចការដូចជាការកំណត់ពេលវេលា ការស្រាវជ្រាវ និងការកក់សំបុត្រដល់ភាគីជំនាញផ្សេងទៀត។
  * **ការបង្កើតមាតិកាផ្ទាល់ខ្លួន**: Workflow មួយដែលភាគីមួយសរសេរមាតិកា អ្នកផ្សេងមួយពិនិត្យមើលភាពត្រឹមត្រូវនិងសំឡេង ហើយភាគីទីបីផ្សព្វផ្សាយវា។

### ប្លង់ Multi-Agent

ប្រព័ន្ធ multi-agent អាចរៀបចំក្នុងប្លង់ជាច្រើន ដែលកំណត់របៀបទំនាក់ទំនងរបស់ពួកវា៖

  * **រៀងរាល់ជំហាន**: ភាគីធ្វើការជាកម្មវិធីដែលបានកំណត់ជាមុន ដូចជាសំណុំការងារ។ លទ្ធផលរបស់ភាគីមួយធ្វើជាទិន្នផលនៃភាគីបន្ទាប់។
  * **សម័យស្រប**: ភាគីធ្វើការលើផ្នែកផ្សេងៗនៃកិច្ចការ​ជា​ច្រើនជាយូរអង្វែង ហើយលទ្ធផលរបស់ពួកវាត្រូវបានប្រមូលនៅចុងក្រោយ។
  * **ថាមពលលក្ខខណ្ឌ**: Workflow នេះដើរតាមផ្លូវផ្សេងៗជាផ្អែកលើលទ្ធផលរបស់ភាគី ស្រដៀងនឹងប្រការឥតទំនាក់ទំនង if-then-else។

## 2\. រចនាសម្ព័ន្ធ Microsoft Agent Framework Workflow

ប្រព័ន្ធ workflow របស់ Agent Framework គឺជាម៉ាស៊ីនប្រតិបត្តិការគ្រប់គ្រងដ៏អភិវឌ្ឍន៍សម្រាប់គ្រប់គ្រងអន្តរកម្មស្មុគស្មាញរវាងភាគីជាច្រើន។ វាត្រូវបានសាងសង់លើរចនាសម្ព័ន្ធធ្វើជាចំណុចជាអាគីវីត៊ីដែលប្រើ [ម៉ូដែលប្រតិបត្តិការបែប Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf) ដែលការដំណើរការ​កើតឡើងក្នុងជំហានសាធារណៈ "supersteps"។

### ធាតុមុខងារសំខាន់ៗ

រចនាសម្ព័ន្ធនេះមានផ្នែកមួយចំនួនដូចខាងក្រោម៖

1.  **អ្នកអនុវត្ត (Executors)**: ជាគ្រឿងបន្លាស់មូលដ្ឋាននៃការប្រតិបត្តិការណ៍។ នៅក្នុងឧទាហរណ៍របស់យើង `Agent` គឺជាប្រភេទអ្នកអនុវត្តមួយ។ អ្នកអនុវត្តនិមួយៗអាចមានអ្នកគ្រប់គ្រងសារច្រើនដែលត្រូវបានហៅដោយស្វ័យប្រវត្តិជាសម្រាប់ប្រភេទសារដែលទទួលបាន។
2.  **ដែន (Edges)**: កំណត់ផ្លូវដែលសារទៅរវាងអ្នកអនុវត្ត។ ដែនអាចមានលក្ខខណ្ឌដែលអនុញ្ញាតឲ្យមានការបញ្ជូនព័ត៌មានបានបែប δυναμικόក្នុងក្រាហ្វ workflow។
3.  **Workflow**: ធាតុនេះគ្រប់គ្រងដំណើរការទាំងមូលផងដែរជាមួយអ្នកអនុវត្ត, ដែន, និងលំនាំទូទៅនៃការប្រតិបត្តិ។ វាបញ្ជាក់ថាសារត្រូវបានដំណើរការតាមលំដាប់ត្រឹមត្រូវ និងចាក់បញ្ចាំងព្រឹត្តិការណ៍សម្រាប់ការត្រួតពិនិត្យ។

*រូបតំណាងដែលបង្ហាញធាតុសំខាន់ៗនៃប្រព័ន្ធ workflow។*

រចនាសម្ព័ន្ធនេះអនុញ្ញាតឲ្យសាងសង់កម្មវិធីធន់និងអាចបង្កើនសមត្ថភាពដោយប្រើប្លង់មូលដ្ឋានដូចជាឈញឺស្រប, ការចេញចូល fan-out/fan-in សម្រាប់ការដំណើរការដើម និងបម្លែងទ្រង់ទ្រាយក្នុង switch-case logic សម្រាប់ចរន្តលក្ខខណ្ឌ។

## 3\. ឧទាហរណ៍អនុវត្តជាក់ស្តែង និងវិភាគកូដ

ឥឡូវនេះ យើងនឹងសិក្សាអំពីរបៀបអនុវត្តប្លង់ workflow ផ្សេងៗ ដោយប្រើ framework។ យើងនឹងមើលទៅកូដ Python និង .NET សម្រាប់ឧទាហរណ៍នីមួយៗ។

### ករណីទី 1: Workflow រៀងរាល់ជំហានមូលដ្ឋាន

នេះគឺជាប្លង់សាមញ្ញបំផុត ដែលលទ្ធផលរបស់ភាគីមួយត្រូវបានផ្ទេរមកភាគីមួយផ្សេងទៀតដោយផ្ទាល់។ ភាពស្ថានការណ៍របស់យើងពាក់ព័ន្ធនឹងភាគី `FrontDesk` ក្នុងសណ្ឋាគារដែលផ្ដល់អនុសាសន៍ធ្វើដំណើរ ហើយបន្ទាប់មកត្រូវបានពិនិត្យឡើងវិញដោយភាគី `Concierge`។

*រូបតំណាងនៃ workflow ផ្នែកមូលដ្ឋាន FrontDesk -> Concierge។*

#### ភាពស្ថានការណ៍

អ្នកដំណើរយកអនុសាសន៍នៅទីក្រុងប៉ារីស។

1.  ភាគី `FrontDesk` ដែលរចនាឡើងសម្រាប់អត្ថបទខ្លី បញ្ចូនអនុសាសន៍ទៅកាន់សារមន្ទីរលូវឌ្រ។
2.  ភាគី `Concierge` ដែលផ្ដោតលើបទពិសោធន៍ដើមទទួលអនុសាសន៍នេះ។ វាពិនិត្យអនុសាសន៍និងផ្ដល់មតិយោបល់ ដើម្បីយកជំនួសដោយជម្រើសដែលមានលក្ខណៈជាតំបន់ និងមិនមានអ្នកទេសចរច្រើន។

#### វិភាគអនុវត្ត Python

នៅក្នុងឧទាហរណ៍ Python, យើងដំណើរការកំណត់និងបង្កើតភាគីទាំងពីរ ជាមួយ​នឹង​ប្រតិបត្តិការពិសេស។

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# កំណត់តួនាទីនិងការណែនាំរបស់ភ្នាក់ងារ
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# បង្កើតអាសយដ្ឋានភ្នាក់ងារ
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

បន្ទាប់មក `WorkflowBuilder` ត្រូវបានប្រើសង់ក្រាហ្វនេះ។ `front_desk_agent` ត្រូវបានកំណត់ជា​ចំណុចដំណើរការ ហើយដែនត្រូវបានបង្កើតដើម្បីភ្ជាប់លទ្ធផលរបស់វាទៅកាន់ `reviewer_agent`។

```python
# ០១.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

ចុងក្រោយ workflow ត្រូវបានអនុវត្តជាមួយសំណើផ្ដើមរបស់អ្នកប្រើ។

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run ដំណើរការហ្វ្លូវ័រ; get_outputs() ត្រឡប់លទ្ធផលនៃអ្នកបំពេញការងារ។
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### វិភាគអនុវត្ត .NET (C#)

ការអនុវត្តនៅ .NET តាមដំណើរការដូចគ្នា។ ជាលេខកំណត់ត្រូវបានកំណត់សម្រាប់ឈ្មោះភាគីនិងការណែនាំ។

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

ភាគីត្រូវបានបង្កើតដោយប្រើ `AzureOpenAIClient` (Responses API), ហើយ `WorkflowBuilder` កំណត់លំនាំរៀងរាល់ជំហានដោយបន្ថែមដែនពី `frontDeskAgent` ទៅកាន់ `reviewerAgent`។

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

Workflow បន្ទាប់មកត្រូវបានដំណើរការជាមួយសាររបស់អ្នកប្រើ ហើយលទ្ធផលត្រូវបានចាក់បញ្ចាំងតាមរលត់។

### ករណីទី 2: Workflow រៀងរាល់ជំហានច្រើនជាប់គ្នា

ប្លង់នេះបន្តពីលំនាំមូលដ្ឋាន ដើម្បីបញ្ចូលភាគីច្រើនទៀត។ វាល្អសម្រាប់ដំណើរការដែលត្រូវការជំហានវាយតម្លៃ ឬបម្លែងជាច្រើនជាងមុន។

#### ភាពស្ថានការណ៍

អ្នកប្រើផ្តល់រូបភាពបន្ទប់ទទួលភ្ញៀវ ហើយសុំសម្រង់តម្លៃសម្ភារៈ។

1.  **Sales-Agent**: កំណត់ឈ្មោះសម្ភារៈក្នុងរូបភាព ហើយបង្កើតបញ្ជី។
2.  **Price-Agent**: ទទួលយកបញ្ជី និងផ្ដល់ការបំបែកតម្លៃលម្អិត រួមមានជម្រើសថវិកា មធ្យម និងពិសេស។
3.  **Quote-Agent**: ទទួលបានបញ្ជីតម្លៃនេះ ហើយរៀបចំឯកសារ​សម្រង់តម្លៃជាឯកសារ Markdown។

*រូបតំណាងនៃ workflow Sales -> Price -> Quote។*

#### វិភាគអនុវត្ត Python

មានការ​កំណត់ភាគីបី ហើយលំនាំត្រូវបានបង្កើតដោយប្រើ `add_edge` ដើម្បីបង្កើតខ្សែ: `sales_agent` -> `price_agent` -> `quote_agent`។

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# បង្កើតភ្នាក់ងារប្រភេទពិសេសបីនាក់
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# សង់លំហូរការងារដោយលំដាប់មួយ
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

បញ្ចូល​ជា `ChatMessage` ដែលមានអត្ថបទ និង URI រូបភាព។ Framework គ្រប់គ្រងការផ្ទេរលទ្ធផលរបស់ភាគីមួយ ទៅភាគីបន្ទាប់រហូតដល់បានសម្រង់តម្លៃចុងក្រោយ។

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# សាររបស់អ្នកប្រើមានទាំងអក្សរនិងរូបភាព
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# រត់ដំណើរការ
events = await workflow.run(message)
```

#### វិភាគអនុវត្ត .NET (C#)

ឧទាហរណ៍ .NET ស្រដៀងទៅនឹង Python។ ភាគីបី (`salesagent`, `priceagent`, `quoteagent`) ត្រូវបានបង្កើត។ `WorkflowBuilder` ភ្ជាប់ពួកវាទៅជាលំដាប់។

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

សាររបស់អ្នកប្រើត្រូវបានបង្កើតជាមួយទិន្នន័យរូបភាព (ជា bytes) និងអត្ថបទ។ វិធីសាស្រ្ត `InProcessExecution.StreamAsync` ចាប់ផ្ដើម workflow ហើយស្លឹកចុងក្រោយត្រូវបានចាប់យកពីរលត់។

### ករណីទី 3: Workflow សម័យស្រប

ប្លង់នេះប្រើនៅពេលកិច្ចការអាចធ្វើមួយពេល ដើម្បីប្រមូលពេលវេលា។ វាតែងតែមានការចែកចេញទៅភាគីជាច្រើន (fan-out) និងការប្រមូលលទ្ធផលមកវិញ (fan-in)។

#### ភាពស្ថានការណ៍

អ្នកប្រើស្នើសុំរៀបចំកម្មវិធីដំណើរកំសាន្តទៅ Seattle។

1.  **Dispatcher (Fan-Out)**: សំណើរបស់អ្នកប្រើត្រូវបានផ្ញើទៅភាគីពីរជាមួយគ្នា។
2.  **Researcher-Agent**: ស្រាវជ្រាវពីកន្លែងទេសចរណ៍ អាកាសធាតុ និងចំណាប់អារម្មណ៍សំខាន់ៗ សម្រាប់ដំណើរកំសាន្តSeattle ក្នុងខែធ្នូ។
3.  **Plan-Agent**: បង្កើតផែនការដំណើរកំសាន្តរៀងរាល់ថ្ងៃដោយឯករាជ្យ។
4.  **Aggregator (Fan-In)**: លទ្ធផលពី researcher និង planner ត្រូវបានប្រមូល និងបង្ហាញជារួមជាលទ្ធផលចុងក្រោយ។

*រូបតំណាងនៃការចែកចាយ concurrently របស់ Researcher និង Planner workflow។*

#### វិភាគអនុវត្ត Python

`ConcurrentBuilder` ធ្វើឲ្យការបង្កើតប្លង់នេះ​ងាយស្រួល។ អ្នកគ្រាន់តែបង្ហាញតារាងភាគីចូលរួម ហើយ builder ស្វ័យប្រវត្តិបង្កើត fan-out និង fan-in logic។

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder គ្រប់គ្រងតុល្យភាព fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# ប្រតិបត្តិការ workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework ជាថ្មីធ្វើការដោះស្រាយឲ្យ `research_agent` និង `plan_agent` ប្រតិបត្ដិការលើសម័យស្រប ហើយលទ្ធផលចុងក្រោយត្រូវបានប្រមូលជាតារាង។

#### វិភាគអនុវត្ត .NET (C#)

នៅក្នុង .NET, ប្លង់នេះត្រូវការការបញ្ជាក់ច្បាស់លាស់ជាងមុន។ អ្នកអនុវត្តបុព្វហេតុ (`ConcurrentStartExecutor` និង `ConcurrentAggregationExecutor`) ត្រូវបានបង្កើតសម្រាប់គ្រប់គ្រង fan-out និង fan-in logic។

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

`WorkflowBuilder` បន្ទាប់មកប្រើ `AddFanOutEdge` និង `AddFanInEdge` ដើម្បីបង្កើតក្រាហ្វជាមួយអ្នកអនុវត្តបុព្វហេតុ និងភាគីទាំងនេះ។

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### ករណីទី 4: Workflow លក្ខខណ្ឌ

Workflow លក្ខខណ្ឌបញ្ចូលនូវ​ផ្លូវផ្សេងៗ ការអនុញ្ញាតឲ្យប្រព័ន្ធទៅតាមផ្លូវផ្សេងផ្អែកលើលទ្ធផលពាក់កណ្តាល។

#### ភាពស្ថានការណ៍

Workflow នេះស្វ័យប្រតិបត្តិការ វិញ្ញាសានិងបោះពុម្ពបទបង្រៀនបច្ចេកទេសមួយ។

1.  **Evangelist-Agent**: សរសេរម៉ូដមួយនៃបទបង្រៀន ផ្អែកលើរចនាសម្ព័ន្ធ និងបណ្ដាបែប URL​។
2.  **ContentReviewer-Agent**: ពិនិត្យមើលម៉ូដមួយ។ វាស្ទង់មើល האם מספר המילים מעל 200.
3.  **Conditional Branch**:
      * **ប្រសិនបើអនុម័ត (`Yes`)**: Workflow ដំណើរការទៅកាន់ `Publisher-Agent`។
      * **ប្រសិនបើបដិសេធ (`No`)**: Workflow បញ្ឈប់ និងបង្ហាញមូលហេតុបដិសេធ។
4.  **Publisher-Agent**: ប្រសិនបើម៉ូដត្រូវបានអនុម័ត ភាគីនេះរក្សាទុកមាតិកាទៅឯកសារ Markdown។

#### វិភាគអនុវត្ត Python

ឧទាហរណ៍នេះប្រើមុខងារផ្ទាល់ខ្លួន `select_targets` ដើម្បីអនុវត្ត logic លក្ខខណ្ឌ។ មុខងារនេះត្រូវបានផ្ដល់ទៅ `add_multi_selection_edge_group` ហើយនាំយក workflow ដោយផ្អែកលើវាល `review_result` ពីលទ្ធផលអ្នកពិនិត្យ។

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# មុខងារនេះកំណត់ជំហានបន្ទាប់អាស្រ័យលើលទ្ធផលពិនិត្យ
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # ប្រសិនបើអនុម័ត ចូលទៅកាន់កម្មវិធី 'save_draft'
        return [save_draft_id]
    else:
        # ប្រសិនបើបដិសេធ ចូលទៅកាន់កម្មវិធី 'handle_review' ដើម្បីរាយការណ៍ការបរាជ័យ
        return [handle_review_id]

# អ្នកបង្កើតក្រុមហ៊ុនប្រើមុខងារជ្រើសរើសសម្រាប់ការបញ្ជូន
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # ជម្រើសពហុមុខងារអនុវត្តតម្កើងលក្ខខណ្ឌ
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

អ្នកអនុវត្តបុព្វហេតុដូចជា `to_reviewer_result` ត្រូវបានប្រើក្នុងការ parse លទ្ធផល JSON ពីភាគី និងបំលែងវាទៅជា objects ដ៏មានប្រភេទមាំម៉ាត់ ដែលមុខងារជ្រើសរើសអាចពិនិត្យបាន។

#### វិភាគអនុវត្ត .NET (C#)

កំណែ .NET ប្រើវិធីសាស្រ្តស្រដៀងគ្នាមួយជាមួយមុខងារលក្ខខណ្ឌ។ `Func<object?, bool>` ត្រូវបានកំណត់សម្រាប់ពិនិត្យម្ភៃ `Result` នៃវត្ថុ `ReviewResult` ។

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

ប៉ារ៉ាម៉ែត្រ `condition` នៃវិធីសាស្រ្ត `AddEdge` អនុញ្ញាតឲ្យ `WorkflowBuilder` បង្កើតផ្លូវចែកលំហូរ។ Workflow នឹងតាមដានដែនទៅ `publishExecutor` ប្រសិនបើលក្ខខណ្ឌ `GetCondition(expectedResult: "Yes")` អនុញ្ញាត។ ប្រសិនមិនដូច្នោះ វានឹងបន្តទៅ `sendReviewerExecutor`។

## សរុប

Microsoft Agent Framework Workflow ផ្ដល់មូលដ្ឋានដ៏រឹងមាំ និងបត់បែនសម្រាប់រៀបចំប្រព័ន្ធ multi-agent ស្មុគស្មាញ។ ដោយប្រើប្រាស់រចនាសម្ព័ន្ធក្រាហ្វ និងធាតុមុខងារគ្រប់គ្រាន់ អ្នកអភិវឌ្ឍន៍អាចរចនានិងអនុវត្ត workflows ស្មុគស្មាញជាទូទៅនៅ Python និង .NET។ មិនថាកម្មវិធីរបស់អ្នកត្រូវការមុខងាររៀងរាល់ជំហាន សម័យស្រប ឬ logic លក្ខខណ្ឌ δυναμικό ផ្នែក framework ផ្ដល់ឧបករណ៍ដើម្បីសាងសង់ដំណោះស្រាយ AI មានស្ដង់ដារ ប្រសិទ្ធភាព និងអាចពង្រីកបាន។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->