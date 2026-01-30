# Construirea aplicațiilor multi-agent cu Microsoft Agent Framework Workflow

Acest tutorial te va ghida în înțelegerea și construirea aplicațiilor multi-agent folosind Microsoft Agent Framework. Vom explora conceptele de bază ale sistemelor multi-agent, arhitectura componentei Workflow a framework-ului și vom parcurge exemple practice în Python și .NET pentru diferite modele de flux de lucru.

## 1\. Înțelegerea sistemelor multi-agent

Un agent AI este un sistem care depășește capacitățile unui model standard de limbaj extins (LLM). Acesta poate percepe mediul, lua decizii și întreprinde acțiuni pentru a atinge obiective specifice. Un sistem multi-agent implică mai mulți astfel de agenți care colaborează pentru a rezolva o problemă dificilă sau imposibil de gestionat de un singur agent.

### Scenarii comune de aplicație

  * **Rezolvarea problemelor complexe**: Descompunerea unei sarcini mari (de exemplu, organizarea unui eveniment la nivel de companie) în sub-sarcini mai mici gestionate de agenți specializați (de exemplu, un agent de buget, un agent de logistică, un agent de marketing).
  * **Asistenți virtuali**: Un agent principal delegă sarcini precum programarea, cercetarea și rezervările către alți agenți specializați.
  * **Crearea automată de conținut**: Un flux de lucru în care un agent redactează conținut, altul îl verifică pentru acuratețe și ton, iar un al treilea îl publică.

### Modele multi-agent

Sistemele multi-agent pot fi organizate în mai multe modele, care determină modul în care interacționează:

  * **Secvențial**: Agenții lucrează într-o ordine prestabilită, ca pe o linie de asamblare. Rezultatul unui agent devine intrarea pentru următorul.
  * **Concurent**: Agenții lucrează în paralel pe diferite părți ale unei sarcini, iar rezultatele lor sunt agregate la final.
  * **Condițional**: Fluxul de lucru urmează căi diferite în funcție de rezultatul unui agent, similar unei instrucțiuni if-then-else.

## 2\. Arhitectura Workflow din Microsoft Agent Framework

Sistemul de workflow al Agent Framework este un motor avansat de orchestrare conceput pentru a gestiona interacțiuni complexe între mai mulți agenți. Este construit pe o arhitectură bazată pe grafuri care utilizează un [model de execuție în stil Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), unde procesarea are loc în pași sincronizați numiți "supersteps".

### Componente de bază

Arhitectura este compusă din trei părți principale:

1.  **Executori**: Acestea sunt unitățile fundamentale de procesare. În exemplele noastre, un `Agent` este un tip de executor. Fiecare executor poate avea mai mulți handleri de mesaje care sunt invocați automat în funcție de tipul mesajului primit.
2.  **Muchii**: Acestea definesc calea pe care o urmează mesajele între executori. Muchiile pot avea condiții, permițând rutarea dinamică a informațiilor prin graful de workflow.
3.  **Workflow**: Această componentă orchestrează întregul proces, gestionând executorii, muchiile și fluxul general de execuție. Asigură procesarea mesajelor în ordinea corectă și transmite evenimente pentru observabilitate.

*O diagramă care ilustrează componentele de bază ale sistemului de workflow.*

Această structură permite construirea de aplicații robuste și scalabile folosind modele fundamentale precum lanțuri secvențiale, fan-out/fan-in pentru procesare paralelă și logică switch-case pentru fluxuri condiționale.

## 3\. Exemple practice și analiză de cod

Acum, să explorăm cum să implementăm diferite modele de flux de lucru folosind framework-ul. Vom analiza codul atât în Python, cât și în .NET pentru fiecare exemplu.

### Caz 1: Workflow secvențial de bază

Acesta este cel mai simplu model, în care rezultatul unui agent este transmis direct altuia. Scenariul nostru implică un agent `FrontDesk` al hotelului care face o recomandare de călătorie, care este apoi revizuită de un agent `Concierge`.

*Diagramă a workflow-ului de bază FrontDesk -\> Concierge.*

#### Contextul scenariului

Un călător cere o recomandare pentru Paris.

1.  Agentul `FrontDesk`, conceput pentru concizie, sugerează vizitarea Muzeului Luvru.
2.  Agentul `Concierge`, care prioritizează experiențele autentice, primește această sugestie. Acesta revizuiește recomandarea și oferă feedback, sugerând o alternativă mai locală, mai puțin turistică.

#### Analiza implementării în Python

În exemplul Python, definim și creăm mai întâi cei doi agenți, fiecare cu instrucțiuni specifice.

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

Apoi, folosim `WorkflowBuilder` pentru a construi graful. `front_desk_agent` este setat ca punct de pornire, iar o muchie este creată pentru a conecta rezultatul său la `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

În final, workflow-ul este executat cu promptul inițial al utilizatorului.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Analiza implementării în .NET (C#)

Implementarea în .NET urmează o logică foarte similară. Mai întâi, sunt definite constante pentru numele și instrucțiunile agenților.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenții sunt creați folosind un `OpenAIClient`, iar apoi `WorkflowBuilder` definește fluxul secvențial prin adăugarea unei muchii de la `frontDeskAgent` la `reviewerAgent`.

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

Workflow-ul este apoi rulat cu mesajul utilizatorului, iar rezultatele sunt transmise în flux.

### Caz 2: Workflow secvențial multi-pas

Acest model extinde secvența de bază pentru a include mai mulți agenți. Este ideal pentru procese care necesită mai multe etape de rafinare sau transformare.

#### Contextul scenariului

Un utilizator oferă o imagine a unui living și cere o ofertă pentru mobilă.

1.  **Sales-Agent**: Identifică piesele de mobilier din imagine și creează o listă.
2.  **Price-Agent**: Ia lista de articole și oferă o defalcare detaliată a prețurilor, incluzând opțiuni de buget, medii și premium.
3.  **Quote-Agent**: Primește lista cu prețuri și o formatează într-un document formal de ofertă în Markdown.

*Diagramă a workflow-ului Sales -\> Price -\> Quote.*

#### Analiza implementării în Python

Sunt definiți trei agenți, fiecare cu un rol specializat. Workflow-ul este construit folosind `add_edge` pentru a crea un lanț: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Inputul este un `ChatMessage` care include atât text, cât și URI-ul imaginii. Framework-ul gestionează transmiterea rezultatului fiecărui agent către următorul în secvență până când oferta finală este generată.

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

#### Analiza implementării în .NET (C#)

Exemplul .NET oglindește versiunea Python. Sunt creați trei agenți (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` îi leagă secvențial.

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

Mesajul utilizatorului este construit cu datele imaginii (ca bytes) și promptul text. Metoda `InProcessExecution.StreamAsync` inițiază workflow-ul, iar rezultatul final este capturat din flux.

### Caz 3: Workflow concurent

Acest model este utilizat atunci când sarcinile pot fi realizate simultan pentru a economisi timp. Implică un "fan-out" către mai mulți agenți și un "fan-in" pentru agregarea rezultatelor.

#### Contextul scenariului

Un utilizator cere planificarea unei excursii în Seattle.

1.  **Dispatcher (Fan-Out)**: Cererea utilizatorului este trimisă simultan la doi agenți.
2.  **Researcher-Agent**: Cercetează atracții, vremea și considerații cheie pentru o excursie în Seattle în decembrie.
3.  **Plan-Agent**: Creează independent un itinerar detaliat zi cu zi.
4.  **Aggregator (Fan-In)**: Rezultatele de la cercetător și planificator sunt colectate și prezentate împreună ca rezultat final.

*Diagramă a workflow-ului concurent Researcher și Planner.*

#### Analiza implementării în Python

`ConcurrentBuilder` simplifică crearea acestui model. Trebuie doar să listezi agenții participanți, iar builder-ul creează automat logica necesară pentru fan-out și fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework-ul asigură că `research_agent` și `plan_agent` se execută în paralel, iar rezultatele lor finale sunt colectate într-o listă.

#### Analiza implementării în .NET (C#)

În .NET, acest model necesită o definiție mai explicită. Executorii personalizați (`ConcurrentStartExecutor` și `ConcurrentAggregationExecutor`) sunt creați pentru a gestiona logica fan-out și fan-in.

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

`WorkflowBuilder` folosește `AddFanOutEdge` și `AddFanInEdge` pentru a construi graful cu acești executori personalizați și agenții.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Caz 4: Workflow condițional

Workflow-urile condiționale introduc logică de ramificare, permițând sistemului să urmeze căi diferite în funcție de rezultate intermediare.

#### Contextul scenariului

Acest workflow automatizează crearea și publicarea unui tutorial tehnic.

1.  **Evangelist-Agent**: Scrie un draft al tutorialului pe baza unui plan și a unor URL-uri date.
2.  **ContentReviewer-Agent**: Revizuiește draftul. Verifică dacă numărul de cuvinte depășește 200.
3.  **Ramificare condițională**:
      * **Dacă este aprobat (`Yes`)**: Workflow-ul continuă către `Publisher-Agent`.
      * **Dacă este respins (`No`)**: Workflow-ul se oprește și afișează motivul respingerii.
4.  **Publisher-Agent**: Dacă draftul este aprobat, acest agent salvează conținutul într-un fișier Markdown.

#### Analiza implementării în Python

Acest exemplu folosește o funcție personalizată, `select_targets`, pentru a implementa logica condițională. Această funcție este transmisă la `add_multi_selection_edge_group` și direcționează workflow-ul pe baza câmpului `review_result` din rezultatul revizorului.

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

Executorii personalizați precum `to_reviewer_result` sunt utilizați pentru a analiza output-ul JSON de la agenți și a-l converti în obiecte puternic tipizate pe care funcția de selecție le poate inspecta.

#### Analiza implementării în .NET (C#)

Versiunea .NET folosește o abordare similară cu o funcție condițională. Un `Func<object?, bool>` este definit pentru a verifica proprietatea `Result` a obiectului `ReviewResult`.

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

Parametrul `condition` al metodei `AddEdge` permite `WorkflowBuilder` să creeze o cale de ramificare. Workflow-ul va urma muchia către `publishExecutor` doar dacă condiția `GetCondition(expectedResult: "Yes")` returnează true. În caz contrar, urmează calea către `sendReviewerExecutor`.

## Concluzie

Microsoft Agent Framework Workflow oferă o fundație robustă și flexibilă pentru orchestrarea sistemelor complexe multi-agent. Prin valorificarea arhitecturii sale bazate pe grafuri și a componentelor de bază, dezvoltatorii pot proiecta și implementa fluxuri de lucru sofisticate atât în Python, cât și în .NET. Indiferent dacă aplicația ta necesită procesare secvențială simplă, execuție paralelă sau logică condițională dinamică, framework-ul oferă instrumentele necesare pentru a construi soluții AI puternice, scalabile și sigure.

---

**Declinarea responsabilității**:  
Acest document a fost tradus utilizând serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru acuratețe, vă rugăm să aveți în vedere că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea realizată de un profesionist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.