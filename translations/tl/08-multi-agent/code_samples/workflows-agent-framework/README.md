# Paggawa ng Multi-Agent Applications gamit ang Microsoft Agent Framework Workflow

Ang tutorial na ito ay gagabay sa iyo sa pag-unawa at paggawa ng mga multi-agent na aplikasyon gamit ang Microsoft Agent Framework. Tatalakayin natin ang mga pangunahing konsepto ng multi-agent systems, susuriin ang arkitektura ng Workflow component ng framework, at magbibigay ng mga praktikal na halimbawa sa Python at .NET para sa iba't ibang workflow patterns.

## 1\. Pag-unawa sa Multi-Agent Systems

Ang isang AI Agent ay isang sistema na higit pa sa kakayahan ng karaniwang Large Language Model (LLM). Kaya nitong maunawaan ang kapaligiran nito, gumawa ng mga desisyon, at magsagawa ng mga aksyon upang makamit ang mga tiyak na layunin. Ang isang multi-agent system ay binubuo ng maraming agents na nagtutulungan upang lutasin ang isang problema na mahirap o imposibleng gawin ng isang agent lamang.

### Karaniwang Mga Senaryo ng Aplikasyon

  * **Paglutas ng Kumplikadong Problema**: Hinahati ang isang malaking gawain (hal., pagpaplano ng isang event para sa buong kumpanya) sa mas maliliit na sub-tasks na pinangangasiwaan ng mga espesyalistang agents (hal., isang budget agent, logistics agent, marketing agent).
  * **Virtual Assistants**: Isang pangunahing assistant agent na nag-aatas ng mga gawain tulad ng pag-schedule, pananaliksik, at pag-book sa iba pang mga espesyalistang agents.
  * **Automated Content Creation**: Isang workflow kung saan ang isang agent ay gumagawa ng draft ng content, ang isa ay nagre-review para sa katumpakan at tono, at ang pangatlo ay nag-publish nito.

### Mga Pattern ng Multi-Agent

Ang mga multi-agent system ay maaaring isaayos sa iba't ibang pattern na tumutukoy kung paano sila nakikipag-ugnayan:

  * **Sequential**: Ang mga agents ay nagtatrabaho sa isang nakatakdang pagkakasunod, tulad ng isang assembly line. Ang output ng isang agent ay nagiging input para sa susunod.
  * **Concurrent**: Ang mga agents ay nagtatrabaho nang sabay-sabay sa iba't ibang bahagi ng isang gawain, at ang kanilang mga resulta ay pinagsasama sa dulo.
  * **Conditional**: Ang workflow ay sumusunod sa iba't ibang landas batay sa output ng isang agent, katulad ng isang if-then-else na pahayag.

## 2\. Ang Arkitektura ng Microsoft Agent Framework Workflow

Ang workflow system ng Agent Framework ay isang advanced na orchestration engine na idinisenyo upang pamahalaan ang mga kumplikadong interaksyon sa pagitan ng maraming agents. Ito ay nakabatay sa isang graph-based na arkitektura na gumagamit ng isang [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), kung saan ang pagproseso ay nagaganap sa mga synchronized na hakbang na tinatawag na "supersteps."

### Mga Pangunahing Komponent

Ang arkitektura ay binubuo ng tatlong pangunahing bahagi:

1.  **Executors**: Ang mga ito ang pangunahing yunit ng pagproseso. Sa ating mga halimbawa, ang `Agent` ay isang uri ng executor. Ang bawat executor ay maaaring magkaroon ng maraming message handlers na awtomatikong tinatawag batay sa uri ng mensaheng natanggap.
2.  **Edges**: Ang mga ito ang nagtatakda ng landas na tinatahak ng mga mensahe sa pagitan ng mga executor. Ang mga edges ay maaaring magkaroon ng mga kondisyon, na nagpapahintulot sa dynamic na pag-ruta ng impormasyon sa workflow graph.
3.  **Workflow**: Ang komponent na ito ang nag-o-orchestrate ng buong proseso, pinamamahalaan ang mga executor, edges, at ang kabuuang daloy ng pagproseso. Tinitiyak nito na ang mga mensahe ay napoproseso sa tamang pagkakasunod at nag-stream ng mga event para sa observability.

*Isang diagram na nagpapakita ng mga pangunahing komponent ng workflow system.*

Ang estrukturang ito ay nagbibigay-daan sa paggawa ng matibay at scalable na mga aplikasyon gamit ang mga pangunahing pattern tulad ng sequential chains, fan-out/fan-in para sa parallel processing, at switch-case logic para sa conditional flows.

## 3\. Mga Praktikal na Halimbawa at Pagsusuri ng Code

Ngayon, tuklasin natin kung paano ipatupad ang iba't ibang workflow patterns gamit ang framework. Titingnan natin ang parehong Python at .NET code para sa bawat halimbawa.

### Kaso 1: Basic Sequential Workflow

Ito ang pinakasimpleng pattern, kung saan ang output ng isang agent ay direktang ipinapasa sa isa pa. Ang ating senaryo ay may kinalaman sa isang hotel `FrontDesk` agent na nagbibigay ng rekomendasyon sa paglalakbay, na sinusuri naman ng isang `Concierge` agent.

*Diagram ng basic FrontDesk -\> Concierge workflow.*

#### Background ng Senaryo

Isang manlalakbay ang humihingi ng rekomendasyon sa Paris.

1.  Ang `FrontDesk` agent, na idinisenyo para sa pagiging maikli, ay nagmumungkahi ng pagbisita sa Louvre Museum.
2.  Ang `Concierge` agent, na inuuna ang mga authentic na karanasan, ay tumatanggap ng mungkahi. Sinusuri nito ang rekomendasyon at nagbibigay ng feedback, na nagmumungkahi ng mas lokal at hindi gaanong turistang alternatibo.

#### Pagsusuri ng Python Implementation

Sa Python na halimbawa, una nating tinutukoy at ginagawa ang dalawang agents, bawat isa ay may partikular na mga tagubilin.

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

Susunod, ginagamit ang `WorkflowBuilder` upang buuin ang graph. Ang `front_desk_agent` ay itinakda bilang panimulang punto, at isang edge ang nilikha upang ikonekta ang output nito sa `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Sa wakas, ang workflow ay isinasagawa gamit ang paunang user prompt.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Pagsusuri ng .NET (C\#) Implementation

Ang .NET implementation ay sumusunod sa halos parehong lohika. Una, tinutukoy ang mga constants para sa mga pangalan at tagubilin ng agents.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Ang mga agents ay nilikha gamit ang isang `OpenAIClient`, at pagkatapos ay ang `WorkflowBuilder` ay tumutukoy sa sequential flow sa pamamagitan ng pagdaragdag ng edge mula sa `frontDeskAgent` papunta sa `reviewerAgent`.

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

Ang workflow ay pagkatapos ay pinapatakbo gamit ang mensahe ng user, at ang mga resulta ay ini-stream pabalik.

### Kaso 2: Multi-Step Sequential Workflow

Ang pattern na ito ay nagpapalawak sa basic sequence upang isama ang mas maraming agents. Mainam ito para sa mga proseso na nangangailangan ng maraming yugto ng refinement o transformation.

#### Background ng Senaryo

Ang isang user ay nagbibigay ng larawan ng isang living room at humihingi ng furniture quote.

1.  **Sales-Agent**: Tinutukoy ang mga furniture items sa larawan at gumagawa ng listahan.
2.  **Price-Agent**: Kinukuha ang listahan ng mga item at nagbibigay ng detalyadong price breakdown, kabilang ang budget, mid-range, at premium na opsyon.
3.  **Quote-Agent**: Tumatanggap ng priced list at inaayos ito sa isang pormal na quote document sa Markdown.

*Diagram ng Sales -\> Price -\> Quote workflow.*

#### Pagsusuri ng Python Implementation

Tatlong agents ang tinutukoy, bawat isa ay may espesyal na tungkulin. Ang workflow ay binubuo gamit ang `add_edge` upang lumikha ng chain: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Ang input ay isang `ChatMessage` na naglalaman ng parehong text at ang image URI. Ang framework ang bahala sa pagpapasa ng output ng bawat agent sa susunod sa sequence hanggang sa mabuo ang final quote.

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

#### Pagsusuri ng .NET (C\#) Implementation

Ang halimbawa sa .NET ay katulad ng bersyon sa Python. Tatlong agents (`salesagent`, `priceagent`, `quoteagent`) ang nilikha. Ang `WorkflowBuilder` ang nag-uugnay sa kanila nang sunud-sunod.

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

Ang mensahe ng user ay binubuo ng parehong image data (bilang bytes) at ang text prompt. Ang `InProcessExecution.StreamAsync` na pamamaraan ang nagpapasimula ng workflow, at ang final output ay kinukuha mula sa stream.

### Kaso 3: Concurrent Workflow

Ang pattern na ito ay ginagamit kapag ang mga gawain ay maaaring gawin nang sabay-sabay upang makatipid ng oras. Kasama rito ang "fan-out" sa maraming agents at "fan-in" upang pagsama-samahin ang mga resulta.

#### Background ng Senaryo

Isang user ang humihiling na magplano ng biyahe sa Seattle.

1.  **Dispatcher (Fan-Out)**: Ang kahilingan ng user ay ipinapadala sa dalawang agents nang sabay.
2.  **Researcher-Agent**: Nagsasaliksik ng mga atraksyon, panahon, at mahahalagang konsiderasyon para sa biyahe sa Seattle sa Disyembre.
3.  **Plan-Agent**: Independiyenteng gumagawa ng detalyadong day-by-day na travel itinerary.
4.  **Aggregator (Fan-In)**: Ang mga output mula sa researcher at planner ay pinagsasama at ipinapakita bilang final result.

*Diagram ng concurrent Researcher at Planner workflow.*

#### Pagsusuri ng Python Implementation

Ang `ConcurrentBuilder` ay nagpapadali sa paggawa ng pattern na ito. Ililista mo lang ang mga kalahok na agents, at ang builder ang awtomatikong gumagawa ng kinakailangang fan-out at fan-in logic.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Tinitiyak ng framework na ang `research_agent` at `plan_agent` ay sabay na isinasagawa, at ang kanilang final outputs ay pinagsasama sa isang listahan.

#### Pagsusuri ng .NET (C\#) Implementation

Sa .NET, ang pattern na ito ay nangangailangan ng mas malinaw na depinisyon. Ang mga custom executors (`ConcurrentStartExecutor` at `ConcurrentAggregationExecutor`) ay nilikha upang pamahalaan ang fan-out at fan-in logic.

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

Ang `WorkflowBuilder` ay gumagamit ng `AddFanOutEdge` at `AddFanInEdge` upang buuin ang graph gamit ang mga custom executors at ang mga agents.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Kaso 4: Conditional Workflow

Ang mga conditional workflows ay nagpapakilala ng branching logic, na nagpapahintulot sa sistema na kumuha ng iba't ibang landas batay sa intermediate results.

#### Background ng Senaryo

Ang workflow na ito ay awtomatikong gumagawa at nag-publish ng isang technical tutorial.

1.  **Evangelist-Agent**: Gumagawa ng draft ng tutorial batay sa ibinigay na outline at mga URL.
2.  **ContentReviewer-Agent**: Nire-review ang draft. Sinusuri nito kung ang word count ay higit sa 200 na salita.
3.  **Conditional Branch**:
      * **Kung Naaprubahan (`Yes`)**: Ang workflow ay nagpapatuloy sa `Publisher-Agent`.
      * **Kung Tinanggihan (`No`)**: Ang workflow ay humihinto at inilalabas ang dahilan ng pagtanggi.
4.  **Publisher-Agent**: Kung ang draft ay naaprubahan, ang agent na ito ay nagse-save ng content sa isang Markdown file.

#### Pagsusuri ng Python Implementation

Ang halimbawang ito ay gumagamit ng custom na function, `select_targets`, upang ipatupad ang conditional logic. Ang function na ito ay ipinapasa sa `add_multi_selection_edge_group` at nagdidirekta sa workflow batay sa `review_result` field mula sa output ng reviewer.

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

Ang mga custom executors tulad ng `to_reviewer_result` ay ginagamit upang i-parse ang JSON output mula sa mga agents at i-convert ito sa strongly-typed objects na maaaring suriin ng selection function.

#### Pagsusuri ng .NET (C\#) Implementation

Ang bersyon sa .NET ay gumagamit ng katulad na approach gamit ang isang condition function. Ang isang `Func<object?, bool>` ay tinutukoy upang suriin ang `Result` property ng `ReviewResult` object.

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

Ang `AddEdge` method na may `condition` parameter ay nagpapahintulot sa `WorkflowBuilder` na lumikha ng branching path. Ang workflow ay susunod lamang sa edge papunta sa `publishExecutor` kung ang kondisyon na `GetCondition(expectedResult: "Yes")` ay nagbabalik ng true. Kung hindi, susunod ito sa landas papunta sa `sendReviewerExecutor`.

## Konklusyon

Ang Microsoft Agent Framework Workflow ay nagbibigay ng matibay at flexible na pundasyon para sa pag-o-orchestrate ng mga kumplikado at multi-agent na sistema. Sa pamamagitan ng paggamit ng graph-based na arkitektura at mga pangunahing komponent nito, maaaring magdisenyo at magpatupad ang mga developer ng mga sopistikadong workflows sa parehong Python at .NET. Kung ang iyong aplikasyon ay nangangailangan ng simpleng sequential processing, parallel execution, o dynamic conditional logic, ang framework ay nag-aalok ng mga kasangkapan upang makabuo ng makapangyarihan, scalable, at type-safe na AI-powered solutions.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.