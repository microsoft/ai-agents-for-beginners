# Paggawa ng Multi-Agent Applications gamit ang Microsoft Agent Framework Workflow

Ang tutorial na ito ay gagabay sa iyo sa pag-unawa at paggawa ng multi-agent applications gamit ang Microsoft Agent Framework. Tatalakayin natin ang mga pangunahing konsepto ng multi-agent systems, susuriin ang arkitektura ng component na Workflow ng framework, at gagabayan ka sa mga praktikal na halimbawa sa parehong Python at .NET para sa iba't ibang workflow patterns.

## 1\. Pag-unawa sa Multi-Agent Systems

Ang AI Agent ay isang sistema na higit pa sa kakayahan ng isang karaniwang Large Language Model (LLM). Kaya nitong maunawaan ang kanyang kapaligiran, gumawa ng mga desisyon, at gumawa ng mga aksyon para maabot ang tiyak na mga layunin. Ang multi-agent system ay binubuo ng ilang mga ahenteng ito na nagtutulungan upang lutasin ang isang problema na magiging mahirap o imposibleng gawin ng isang ahente lang nang mag-isa.

### Karaniwang mga Scenario ng Aplikasyon

  * **Pagsolusyon ng Komplikadong Problema**: Hatiin ang isang malaking gawain (hal. pagplano ng pang-kumpanyang event) sa mas maliliit na sub-gawain na hawak ng mga espesyalisadong ahente (hal. ahente sa budget, ahente sa logistics, ahente sa marketing).
  * **Virtual Assistants**: Isang pangunahing assistant agent na nagtatalaga ng mga gawain tulad ng pag-schedule, pananaliksik, at booking sa ibang espesyalisadong mga ahente.
  * **Automated Content Creation**: Isang workflow kung saan isang ahente ang gumagawa ng draft ng nilalaman, ang isa ay nire-review ito para sa katumpakan at tono, at ang pangatlo ay nag-publish nito.

### Mga Multi-Agent Patterns

Maaaring istraktura ang mga multi-agent systems sa iba't ibang patterns, na tumutukoy kung paano sila nakikipag-ugnayan:

  * **Sequential**: Ang mga ahente ay nagtatrabaho sa isang takdang pagkakasunod-sunod, parang assembly line. Ang output ng isang ahente ay nagiging input ng susunod.
  * **Concurrent**: Ang mga ahente ay gumagawa ng iba't ibang bahagi ng gawain nang sabay-sabay, at ang mga resulta ay pinagsasama sa dulo.
  * **Conditional**: Ang workflow ay sumusunod sa iba't ibang mga daan batay sa output ng isang ahente, katulad ng if-then-else na pahayag.

## 2\. Arkitektura ng Microsoft Agent Framework Workflow

Ang workflow system ng Agent Framework ay isang advanced na orchestration engine na dinisenyo upang pamahalaan ang komplikadong interaksyon sa pagitan ng iba't ibang mga ahente. Ito ay nakabase sa isang graph-based architecture na gumagamit ng [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), kung saan ang proseso ay nangyayari sa mga sabayang hakbang na tinatawag na "supersteps."

### Pangunahing Mga Komponent

Binubuo ang arkitektura ng tatlong pangunahing bahagi:

1.  **Executors**: Ito ang pangunahing yunit ng pagproseso. Sa aming mga halimbawa, ang `Agent` ay isang uri ng executor. Bawat executor ay maaaring magkaroon ng maraming message handlers na awtomatikong tinatawag depende sa uri ng natanggap na mensahe.
2.  **Edges**: Ito ang tumutukoy sa landas na tinatahak ng mga mensahe sa pagitan ng mga executor. Ang mga edge ay maaaring may kundisyon, na nagpapahintulot ng dynamic na pag-ruta ng impormasyon sa workflow graph.
3.  **Workflow**: Ang component na ito ang nag-oorganisa ng kabuuang proseso, pinamamahalaan ang mga executors, edges, at ang pangkalahatang daloy ng pagsasagawa. Tinitiyak nito na ang mga mensahe ay napoproseso sa tamang pagkakasunod-sunod at nag-stream ng mga event para sa observability.

*Isang diagram na nagpapakita ng mga pangunahing bahagi ng workflow system.*

Ang estrukturang ito ay nagpapahintulot sa pagbuo ng matatag at scalable na mga aplikasyon gamit ang mga pangunahing pattern tulad ng sequential chains, fan-out/fan-in para sa parallel processing, at switch-case logic para sa mga kondisyunal na daloy.

## 3\. Mga Praktikal na Halimbawa at Pagsusuri ng Code

Ngayon, tuklasin natin kung paano ipatupad ang iba't ibang workflow patterns gamit ang framework. Titingnan natin ang parehong Python at .NET na code para sa bawat halimbawa.

### Kaso 1: Basic Sequential Workflow

Ito ang pinakapayak na pattern, kung saan ang output ng isang ahente ay direktang ipinapasa sa isa pa. Ang scenario natin ay may isang hotel na `FrontDesk` agent na nagbibigay ng travel recommendation, na nire-review naman ng isang `Concierge` agent.

*Diagram ng basic FrontDesk -\> Concierge workflow.*

#### Likas na Konteksto ng Scenario

Isang biyahero ang humiling ng rekomendasyon sa Paris.

1.  Ang `FrontDesk` agent, na nilikha para sa pagiging maigsi, ay nagmumungkahi na bisitahin ang Louvre Museum.
2.  Ang `Concierge` agent, na mas pinahahalagahan ang tunay na karanasan, ay tumatanggap ng mungkahing ito. Ini-review nito ang rekomendasyon at nagbibigay ng puna, na nagmumungkahi ng mas lokal at hindi pang-turista na alternatibo.

#### Pagsusuri ng Implementasyon sa Python

Sa halimbawa sa Python, una nating dinefine at nilikha ang dalawang ahente, bawat isa ay may espesipikong mga tagubilin.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Tukuyin ang mga tungkulin at tagubilin ng ahente
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Gumawa ng mga instance ng ahente
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Susunod, ginagamit ang `WorkflowBuilder` upang buuin ang graph. Ang `front_desk_agent` ay itinakda bilang panimulang punto, at gumagawa tayo ng edge upang ikonekta ang kanyang output sa `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Sa wakas, pinapatakbo ang workflow gamit ang initial user prompt.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# Ang run ay nagpapatakbo ng workflow; ang get_outputs() ay nagbabalik ng resulta ng output executor.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Pagsusuri ng Implementasyon sa .NET (C\#)

Ang implementasyon sa .NET ay sumusunod sa halos katulad na lohika. Una, nagde-define ng mga constants para sa mga pangalan at tagubilin ng mga ahente.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Nililikha ang mga ahente gamit ang `AzureOpenAIClient` (Responses API), at pagkatapos ay ginagamit ang `WorkflowBuilder` upang tukuyin ang sequential flow sa pamamagitan ng pagdagdag ng edge mula sa `frontDeskAgent` papunta sa `reviewerAgent`.

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

Pinapagana ang workflow gamit ang mensahe ng gumagamit, at ang mga resulta ay ini-stream pabalik.

### Kaso 2: Multi-Step Sequential Workflow

Pinapalawak ng pattern na ito ang basic sequence upang isama pa ang maraming ahente. Mainam ito para sa mga proseso na nangangailangan ng maraming yugto ng pagpapahusay o pagbabago.

#### Likas na Konteksto ng Scenario

Isang gumagamit ang nagbigay ng larawan ng sala at humiling ng furniture quote.

1.  **Sales-Agent**: Kinikilala ang mga furniture item sa larawan at gumagawa ng listahan.
2.  **Price-Agent**: Kinukuha ang listahan ng mga item at nagbibigay ng detalyadong breakdown ng presyo, kabilang ang mga budget, mid-range, at premium na opsyon.
3.  **Quote-Agent**: Tumatanggap ng priced list at inaayos ito sa isang pormal na dokumento ng quote sa Markdown.

*Diagram ng Sales -\> Price -\> Quote workflow.*

#### Pagsusuri ng Implementasyon sa Python

Tatlong ahente ang dinefine, bawat isa ay may espesyal na tungkulin. Binubuo ang workflow gamit ang `add_edge` upang gumawa ng chain: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Gumawa ng tatlong espesyal na ahente
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Buuhin ang sunud-sunod na workflow
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Ang input ay isang `ChatMessage` na may kasamang teksto at URI ng larawan. Pinangangasiwaan ng framework ang pagpapasa ng output ng bawat ahente papunta sa susunod hanggang sa mabuo ang huling quote.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Naglalaman ang mensahe ng user ng teksto at isang larawan
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Patakbuhin ang workflow
events = await workflow.run(message)
```

#### Pagsusuri ng Implementasyon sa .NET (C\#)

Nakikita sa halimbawa ng .NET ang kaparehong istruktura tulad ng sa Python. Tatlong ahente (`salesagent`, `priceagent`, `quoteagent`) ang nilikha. Ang `WorkflowBuilder` ay nag-uugnay sa kanila nang sequentially.

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

Ang mensahe ng gumagamit ay binubuo ng parehong datos ng larawan (bilang bytes) at teksto na prompt. Ang method na `InProcessExecution.RunStreamingAsync` ang nagpapasimula ng workflow, at ang huling output ay kinukuha mula sa stream.

### Kaso 3: Concurrent Workflow

Ginagamit ang pattern na ito kapag ang mga gawain ay maaaring isagawa nang sabay-sabay upang makatipid sa oras. Kabilang dito ang "fan-out" sa maraming ahente at "fan-in" upang pag-isahin ang mga resulta.

#### Likas na Konteksto ng Scenario

Isang gumagamit ang humiling ng pagplano ng biyahe sa Seattle.

1.  **Dispatcher (Fan-Out)**: Ang kahilingan ng gumagamit ay ipinapadala sa dalawang ahente nang sabay.
2.  **Researcher-Agent**: Nagsasaliksik ng mga atraksyon, panahon, at mga pangunahing konsiderasyon para sa biyahe sa Seattle sa Disyembre.
3.  **Plan-Agent**: Nagbuo nang independyente ng detalyadong araw-araw na itineraryo ng biyahe.
4.  **Aggregator (Fan-In)**: Kinokolekta ang mga output mula sa researcher at planner at ipinapakita nang magkakasama bilang pinal na resulta.

*Diagram ng sabayang Researcher at Planner workflow.*

#### Pagsusuri ng Implementasyon sa Python

Pinadadali ng `ConcurrentBuilder` ang paglikha ng pattern na ito. Ililista mo lang ang mga kalahok na ahente, at ang builder ay awtomatikong gagawa ng kinakailangang fan-out at fan-in na lohika.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# Pinangangasiwaan ng ConcurrentBuilder ang logic ng fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Patakbuhin ang workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Sinisiguro ng framework na ang `research_agent` at `plan_agent` ay magkakasabay na nagpapatupad, at ang kanilang huling output ay kinokolekta sa isang listahan.

#### Pagsusuri ng Implementasyon sa .NET (C\#)

Sa .NET, nangangailangan ang pattern na ito ng mas tahasang depinisyon. Gumagawa ng mga custom executors (`ConcurrentStartExecutor` at `ConcurrentAggregationExecutor`) upang pamahalaan ang fan-out at fan-in na lohika.

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

Ginagamit ng `WorkflowBuilder` ang `AddFanOutEdge` at `AddFanInEdge` upang buuin ang graph kasama ang mga custom executors at mga ahente.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Kaso 4: Conditional Workflow

Nagdadala ang Conditional workflows ng branching logic, na nagpapahintulot sa sistema na pumili ng iba't ibang mga landas base sa mga panandaliang resulta.

#### Likas na Konteksto ng Scenario

Ina-automate ng workflow na ito ang paggawa at paglathala ng isang teknikal na tutorial.

1.  **Evangelist-Agent**: Nagsusulat ng draft ng tutorial base sa isang outline at mga URL.
2.  **ContentReviewer-Agent**: Nirereview ang draft. Sinusuri kung ang bilang ng salita ay lagpas sa 200 salita.
3.  **Conditional Branch**:
      * **Kung Aprubado (`Yes`)**: Ang workflow ay magpapatuloy sa `Publisher-Agent`.
      * **Kung Hindi Aprubado (`No`)**: Hihinto ang workflow at ipapakita ang dahilan ng pagtanggi.
4.  **Publisher-Agent**: Kung aprubado ang draft, ililigtas ng agent na ito ang nilalaman sa isang Markdown na file.

#### Pagsusuri ng Implementasyon sa Python

Gumagamit ang halimbawang ito ng custom function na `select_targets` upang ipatupad ang kondisyunal na lohika. Ang function na ito ay ipinapasa sa `add_multi_selection_edge_group` at ginagabayan ang workflow base sa `review_result` field mula sa output ng reviewer.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Tinutukoy ng function na ito ang susunod na hakbang batay sa resulta ng pagsusuri
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Kung aprubado, magpatuloy sa 'save_draft' executor
        return [save_draft_id]
    else:
        # Kung tinanggihan, magpatuloy sa 'handle_review' executor upang iulat ang pagkabigo
        return [handle_review_id]

# Ginagamit ng workflow builder ang selection function para sa pag-routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Ipinapatupad ng multi-selection edge ang kondisyonal na lohika
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Ginagamit ang mga custom executor tulad ng `to_reviewer_result` upang i-parse ang JSON output mula sa mga ahente at gawing strongly-typed na mga object na maaaring suriin ng selection function.

#### Pagsusuri ng Implementasyon sa .NET (C\#)

Gumagamit ang bersyon sa .NET ng katulad na pamamaraan gamit ang function na kondisyon. Isang `Func<object?, bool>` ang dinefine upang suriin ang `Result` property ng `ReviewResult` object.

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

Pinapayagan ng `condition` parameter ng `AddEdge` method ang `WorkflowBuilder` na gumawa ng branching path. Susundan lang ng workflow ang edge papunta sa `publishExecutor` kung ang kondisyon na `GetCondition(expectedResult: "Yes")` ay totoo. Kung hindi, susundan nito ang landas papunta sa `sendReviewerExecutor`.

## Konklusyon

Nagbibigay ang Microsoft Agent Framework Workflow ng matatag at flexible na pundasyon para sa pag-oorganisa ng komplikado, multi-agent na mga sistema. Sa pamamagitan ng paggamit ng graph-based architecture at mga pangunahing bahagi nito, maaaring magdisenyo at magpatupad ang mga developer ng komplikadong workflows sa parehong Python at .NET. Kung ang iyong aplikasyon ay nangangailangan ng simpleng sequential processing, parallel execution, o dynamic conditional logic, ang framework ay nag-aalok ng mga kasangkapan upang gumawa ng makapangyarihang, scalable, at type-safe na mga solusyong pinapagana ng AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->