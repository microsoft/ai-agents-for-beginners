# Pagbuo ng Multi-Agent Applications gamit ang Microsoft Agent Framework Workflow

Ang tutorial na ito ay gagabay sa iyo sa pag-unawa at pagbuo ng multi-agent applications gamit ang Microsoft Agent Framework. Tatalakayin natin ang mga pangunahing konsepto ng multi-agent systems, susuriin ang arkitektura ng Workflow component ng framework, at gagawa tayo ng mga praktikal na halimbawa sa parehong Python at .NET para sa iba't ibang workflow patterns.

## 1\. Pag-unawa sa Multi-Agent Systems

Ang AI Agent ay isang sistema na lampas sa kakayahan ng isang standard Large Language Model (LLM). Kaya nitong makita ang kapaligiran, gumawa ng mga desisyon, at magsagawa ng aksyon upang maabot ang mga partikular na layunin. Ang multi-agent system naman ay binubuo ng maraming mga agent na nagtutulungan upang lutasin ang isang problema na mahirap o imposible para sa isang agent lang na hawakan nang mag-isa.

### Karaniwang Mga Senaryo ng Aplikasyon

  * **Kompleks na Pagsosolusyon ng Problema**: Paghahati-hati ng malaking gawain (e.g., pagpaplano ng isang pang-kumpanyang kaganapan) sa mas maliliit na sub-task na hinahawakan ng mga espesyalisadong agent (e.g., isang budget agent, isang logistics agent, isang marketing agent).
  * **Virtual Assistants**: Isang pangunahing assistant agent na nag-aatas ng mga gawain tulad ng pag-schedule, pananaliksik, at pag-book sa iba pang espesyalisadong agent.
  * **Automated Content Creation**: Isang workflow kung saan ang isang agent ay nag-bubuo ng draft ng nilalaman, ang isa naman ay nagrereview para sa katumpakan at tono, at ang isa pang naglalathala nito.

### Mga Pattern ng Multi-Agent

Ang mga multi-agent system ay maaaring ayusin sa iba't ibang pattern, na nagtatakda kung paano sila nakikipag-ugnayan:

  * **Sequential**: Ang mga agent ay gumagana sa isang nakatakdang pagkakasunod-sunod, tulad ng assembly line. Ang output ng isang agent ang input ng sumunod.
  * **Concurrent**: Ang mga agent ay gumagana nang sabay-sabay sa iba’t ibang bahagi ng gawain, at pinagsasama ang mga resulta sa dulo.
  * **Conditional**: Ang workflow ay sumusunod sa iba't ibang landas base sa output ng isang agent, tulad ng if-then-else na pahayag.

## 2\. Ang Arkitektura ng Microsoft Agent Framework Workflow

Ang sistema ng workflow ng Agent Framework ay isang advanced na orchestration engine na idinisenyo upang pamahalaan ang komplikadong pakikipag-ugnayan sa pagitan ng maraming agent. Ito ay nakabase sa isang graph-based architecture na gumagamit ng [Pregel-style execution model](https://kowshik.github.io/JPregel/pregel_paper.pdf), kung saan ang pagproseso ay nangyayari sa naka-synchronize na mga hakbang na tinatawag na "supersteps."

### Pangunahing Komponent

Ang arkitektura ay binubuo ng tatlong pangunahing bahagi:

1.  **Executors**: Ito ang mga pangunahing yunit ng pagproseso. Sa ating mga halimbawa, ang isang `Agent` ay uri ng executor. Bawat executor ay maaaring magkaroon ng maraming mga message handler na awtomatikong tinatawag batay sa uri ng mensaheng natanggap.
2.  **Edges**: Ito ang nagtatakda ng landas na dinaanan ng mga mensahe sa pagitan ng mga executor. Ang mga edges ay maaaring may kondisyon, na nagbibigay-daan sa dynamic na pag-route ng impormasyon sa workflow graph.
3.  **Workflow**: Ang komponent na ito ang nag-oorganisa ng buong proseso, pinamamahalaan ang mga executor, edges, at kabuuang daloy ng pag-eexecute. Tinitiyak nito na ang mga mensahe ay naproseso sa tamang pagkakasunod-sunod at nag-stream ng mga kaganapan para sa observability.

*Isang diagram na nagpapakita ng pangunahing mga bahagi ng workflow system.*

Ang istrukturang ito ay nagbibigay-daan para sa pagbuo ng matibay at scalable na mga aplikasyon gamit ang mga pangunahing pattern tulad ng sequential chains, fan-out/fan-in para sa parallel processing, at switch-case logic para sa conditional flows.

## 3\. Mga Praktikal na Halimbawa at Pagsusuri ng Code

Ngayon, susuriin natin kung paano ipatupad ang iba't ibang workflow patterns gamit ang framework. Titignan natin ang parehong Python at .NET na code para sa bawat halimbawa.

### Kaso 1: Pangunahing Sequential Workflow

Ito ang pinakapayak na pattern, kung saan ang output ng isang agent ay direktang ipinapasa sa isa pa. Ang ating senaryo ay may hotel `FrontDesk` agent na nagbibigay ng travel recommendation, na susuriin naman ng `Concierge` agent.

*Diagram ng pangunahing FrontDesk -\> Concierge workflow.*

#### Bakground ng Senaryo

May isang manlalakbay na humihingi ng rekomendasyon sa Paris.

1.  Ang `FrontDesk` agent, na dinisenyo para sa pagiging maigsi, ay nagmumungkahi ng pagbisita sa Louvre Museum.
2.  Ang `Concierge` agent, na inuuna ang authentic na karanasan, ay tumatanggap ng mungkahing ito. Sinusuri nito ang rekomendasyon at nagbibigay ng puna, nagmumungkahi ng isang mas lokal at hindi masyadong turistang alternatibo.

#### Pagsusuri ng Python Implementation

Sa halimbawa ng Python, una nating idinedeklara at ginagawa ang dalawang agent, bawat isa ay may partikular na instructions.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Tukuyin ang mga papel at mga tagubilin ng ahente
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Gumawa ng mga halimbawa ng ahente
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Sunod, ginagamit ang `WorkflowBuilder` upang buuin ang graph. Ang `front_desk_agent` ay itinakda bilang panimulang punto, at isang edge ang ginawa upang ikonekta ang output nito sa `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Sa huli, ang workflow ay pinapatakbo gamit ang panimulang user prompt.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# ang run ay nagpapagana ng workflow; ang get_outputs() ay nagbabalik ng resulta ng output executor.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Pagsusuri ng .NET (C\#) Implementation

Ang .NET implementation ay sumusunod sa halos parehong lohika. Una, dine-define ang mga constants para sa mga pangalan at instructions ng mga agent.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Ginagawa ang mga agent gamit ang `AzureOpenAIClient` (Responses API), at pagkatapos ay ang `WorkflowBuilder` ay nagtatakda ng sequential flow sa pamamagitan ng pagdagdag ng edge mula sa `frontDeskAgent` papunta sa `reviewerAgent`.

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

Ang workflow ay pinapagana gamit ang mensahe ng user, at ang mga resulta ay pinapadaloy pabalik.

### Kaso 2: Multi-Step Sequential Workflow

Pinalalawak ng pattern na ito ang basic sequence para isama ang mas maraming agent. Mainam ito para sa mga proseso na nangangailangan ng maraming yugto ng pagpapaayos o pagbabago.

#### Bakground ng Senaryo

Isang user ang nagbibigay ng larawan ng living room at humihiling ng furniture quote.

1.  **Sales-Agent**: Tinutukoy ang mga furniture item sa larawan at gumagawa ng listahan.
2.  **Price-Agent**: Tumatanggap ng listahan ng items at nagbibigay ng detalyadong breakdown ng presyo, kabilang ang budget, mid-range, at premium na opsyon.
3.  **Quote-Agent**: Tumatanggap ng pinresyuhang listahan at ini-format ito sa isang pormal na dokumento ng quote sa Markdown.

*Diagram ng Sales -\> Price -\> Quote workflow.*

#### Pagsusuri ng Python Implementation

Tatlong agent ang dineklara, bawat isa ay may espesyalisadong tungkulin. Ang workflow ay binuo gamit ang `add_edge` upang gumawa ng chain: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Lumikha ng tatlong espesyal na ahente
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Buuhin ang sunud-sunod na daloy ng trabaho
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Ang input ay isang `ChatMessage` na naglalaman ng teksto at ang image URI. Pinangangasiwaan ng framework ang pagpapasa ng output ng bawat agent papunta sa susunod sa sequence hanggang sa mabuo ang panghuling quote.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Ang mensahe ng gumagamit ay naglalaman ng parehong teksto at larawan
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

#### Pagsusuri ng .NET (C\#) Implementation

Ang halimbawa sa .NET ay kahawig ng bersyon ng Python. Tatlong agent (`salesagent`, `priceagent`, `quoteagent`) ang ginawa. Ang `WorkflowBuilder` ay nag-uugnay sa kanila nang sunud-sunod.

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

Ang mensahe ng user ay binuo gamit ang parehong image data (bilang bytes) at ang text prompt. Ang `InProcessExecution.StreamAsync` na pamamaraan ang nagsisimula ng workflow, at ang panghuling output ay kinukuha mula sa stream.

### Kaso 3: Concurrent Workflow

Ginagamit ang pattern na ito kapag ang mga gawain ay maaaring sabay-sabay gawin para makatipid ng oras. Kabilang dito ang "fan-out" sa maraming agent at "fan-in" para pagsamahin ang mga resulta.

#### Bakground ng Senaryo

Isang user ang humiling na magplano ng biyahe sa Seattle.

1.  **Dispatcher (Fan-Out)**: Ang kahilingan ng user ay ipinapadala sa dalawang agent nang sabay.
2.  **Researcher-Agent**: Nagsasaliksik ng mga atraksyon, panahon, at mahahalagang bagay para sa biyahe sa Seattle sa Disyembre.
3.  **Plan-Agent**: Independiyenteng gumagawa ng detalyadong araw-araw na itineraryo ng paglalakbay.
4.  **Aggregator (Fan-In)**: Pinagsasama ang output mula sa parehong researcher at planner at ipinapakita ito bilang panghuling resulta.

*Diagram ng sabayang Researcher at Planner workflow.*

#### Pagsusuri ng Python Implementation

Pinapadali ng `ConcurrentBuilder` ang paggawa ng pattern na ito. Itinatala mo lang ang mga sangkot na agent, at ang builder ang awtomatikong lumilikha ng kinakailangang fan-out at fan-in na lohika.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# Pinamamahalaan ng ConcurrentBuilder ang fan-out/fan-in na lohika
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Patakbuhin ang workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Tinitiyak ng framework na ang `research_agent` at `plan_agent` ay nagpapatakbo nang sabay, at ang panghuling output nila ay kinokolekta sa isang listahan.

#### Pagsusuri ng .NET (C\#) Implementation

Sa .NET, nangangailangan ang pattern na ito ng mas malinaw na depinisyon. Gumagawa ng custom executors (`ConcurrentStartExecutor` at `ConcurrentAggregationExecutor`) upang hawakan ang fan-out at fan-in na lohika.

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

Ginagamit ng `WorkflowBuilder` ang `AddFanOutEdge` at `AddFanInEdge` upang buuin ang graph gamit ang mga custom executor at mga agent.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Kaso 4: Conditional Workflow

Ang mga conditional workflow ay nagdadala ng panghihiwalay ng daloy, na nagpapahintulot sa sistema na pumili ng iba't ibang landas base sa mga mid-level na resulta.

#### Bakground ng Senaryo

Ang workflow na ito ay nag-automate sa paggawa at paglathala ng isang technical tutorial.

1.  **Evangelist-Agent**: Nagsusulat ng draft ng tutorial base sa ibinigay na balangkas at mga URL.
2.  **ContentReviewer-Agent**: Nire-review ang draft. Sinusuri kung ang bilang ng salita ay higit sa 200.
3.  **Conditional Branch**:
      * **Kung Aprubado (`Yes`)**: Ang workflow ay nagpapatuloy sa `Publisher-Agent`.
      * **Kung Hindi Aprubado (`No`)**: Humihinto ang workflow at inilalabas ang dahilan ng pagtanggi.
4.  **Publisher-Agent**: Kung aprubado ang draft, sine-save ng agent na ito ang nilalaman sa Markdown file.

#### Pagsusuri ng Python Implementation

Gumagamit ang halimbawang ito ng custom na function, `select_targets`, upang ipatupad ang conditional logic. Ipinapasa ang function na ito sa `add_multi_selection_edge_group` at iniaayon ang workflow base sa `review_result` field mula sa output ng reviewer.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Tinutukoy ng function na ito ang susunod na hakbang batay sa resulta ng pagsusuri
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Kung aprubado, magpatuloy sa 'save_draft' na executor
        return [save_draft_id]
    else:
        # Kung tinanggihan, magpatuloy sa 'handle_review' na executor upang iulat ang kabiguan
        return [handle_review_id]

# Ginagamit ng workflow builder ang selection function para sa pag-ruruta
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Ipinalalapat ng multi-selection edge ang kondisyunal na lohika
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Ginagamit ang mga custom executor tulad ng `to_reviewer_result` upang i-parse ang JSON output mula sa mga agent at i-convert ito sa mga strongly-typed na object na kayang suriin ng selection function.

#### Pagsusuri ng .NET (C\#) Implementation

Ang bersyon sa .NET ay gumagamit ng katulad na pamamaraan na may condition function. Isang `Func<object?, bool>` ang dinefine upang suriin ang `Result` property ng `ReviewResult` object.

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

Ang `condition` parameter ng `AddEdge` method ay nagpapahintulot sa `WorkflowBuilder` na gawin ang branching path. Susundin ng workflow ang edge papunta sa `publishExecutor` kung ang kondisyon na `GetCondition(expectedResult: "Yes")` ay totoo. Kung hindi, susundan nito ang landas papunta sa `sendReviewerExecutor`.

## Konklusyon

Ang Microsoft Agent Framework Workflow ay nagbibigay ng matibay at flexible na pundasyon para sa pag-oorganisa ng mga komplikadong multi-agent system. Sa pamamagitan ng pag-gamit ng graph-based architecture at mga pangunahing bahagi nito, makakalikha ang mga developer ng sopistikadong workflows sa parehong Python at .NET. Kung ang iyong aplikasyon ay nangangailangan ng payak na sequential processing, parallel na pag-eexecute, o dynamic na conditional logic, ang framework ay nag-aalok ng mga tools upang makabuo ng malakas, scalable, at type-safe na mga AI-powered na solusyon.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->