# Construirea aplicațiilor multi-agent cu Microsoft Agent Framework Workflow

Acest tutorial vă va ghida în înțelegerea și construirea aplicațiilor multi-agent utilizând Microsoft Agent Framework. Vom explora conceptele fundamentale ale sistemelor multi-agent, vom analiza arhitectura componentei Workflow a framework-ului și vom parcurge exemple practice în Python și .NET pentru diferite modele de flux de lucru.

## 1\. Înțelegerea sistemelor multi-agent

Un agent AI este un sistem care depășește capabilitățile unui model lingvistic mare (LLM) standard. Acesta poate percepe mediul înconjurător, poate lua decizii și poate acționa pentru a atinge obiective specifice. Un sistem multi-agent implică mai mulți astfel de agenți care colaborează pentru a rezolva o problemă ce ar fi dificilă sau imposibil de gestionat de un singur agent.

### Scenarii comune de aplicație

  * **Rezolvarea problemelor complexe**: Descompunerea unei sarcini mari (de exemplu, planificarea unui eveniment la nivel de companie) în sub-sarcini mai mici gestionate de agenți specializați (de exemplu, un agent de buget, un agent de logistică, un agent de marketing).
  * **Asistenți virtuali**: Un agent asistent principal care delegă sarcini precum programarea, cercetarea și rezervările către alți agenți specializați.
  * **Crearea automată de conținut**: Un flux de lucru în care un agent redactează conținut, altul îl revizuiește pentru precizie și ton, iar un al treilea îl publică.

### Modele multi-agent

Sistemele multi-agent pot fi organizate în mai multe modele, care determină modul în care interacționează:

  * **Secvențial**: Agenții lucrează într-o ordine predefinită, asemenea unei linii de asamblare. Ieșirea unui agent devine intrarea următorului.
  * **Concurrent**: Agenții lucrează în paralel pe părți diferite ale unei sarcini, iar rezultatele lor sunt agregate la final.
  * **Conditional**: Fluxul de lucru urmează căi diferite în funcție de ieșirea unui agent, similar unei instrucțiuni if-then-else.

## 2\. Arhitectura Microsoft Agent Framework Workflow

Sistemul de workflow din Agent Framework este un motor avansat de orchestrare proiectat să gestioneze interacțiuni complexe între mai mulți agenți. Este construit pe o arhitectură bazată pe grafuri care utilizează un [model de execuție stil Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), unde procesarea are loc în pași sincronizați numiți "supersteps".

### Componentele principale

Arhitectura este compusă din trei părți principale:

1.  **Executori**: Acestea sunt unitățile fundamentale de procesare. În exemplele noastre, un `Agent` este un tip de executor. Fiecare executor poate avea mai mulți handleri de mesaje care sunt invocați automat bazat pe tipul mesajului primit.
2.  **Muchii**: Acestea definesc calea prin care mesajele circulă între executori. Muchiile pot avea condiții, permițând rutarea dinamică a informațiilor prin graful fluxului de lucru.
3.  **Workflow**: Această componentă orchestrează întregul proces, gestionând executorii, muchiile și fluxul general de execuție. Asigură procesarea mesajelor în ordinea corectă și transmite evenimente pentru observabilitate.

*Un diagrame care ilustrează componentele principale ale sistemului de workflow.*

Această structură permite construirea de aplicații robuste și scalabile folosind modele fundamentale precum lanțuri secvențiale, fan-out/fan-in pentru procesare paralelă și logică switch-case pentru fluxuri condiționale.

## 3\. Exemple practice și analiză de cod

Acum să explorăm cum să implementăm diferite modele de workflow folosind framework-ul. Vom analiza cod Python și .NET pentru fiecare exemplu.

### Caz 1: Workflow secvențial de bază

Aceasta este cea mai simplă schemă, unde ieșirea unui agent este transmisă direct către altul. Scenariul nostru implică un agent de recepție la hotel, `FrontDesk`, care face o recomandare de călătorie, care este apoi revizuită de un agent `Concierge`.

*Diagramă a fluxului de lucru FrontDesk -> Concierge.*

#### Contextul scenariului

Un călător cere o recomandare pentru Paris.

1.  Agentul `FrontDesk`, proiectat pentru concizie, sugerează vizitarea Muzeului Louvre.
2.  Agentul `Concierge`, care prioritizează experiențele autentice, primește această sugestie. Revizuiește recomandarea și oferă feedback, sugerând o alternativă mai locală, mai puțin turistică.

#### Analiza implementării în Python

În exemplul Python, definim și creăm mai întâi cei doi agenți, fiecare cu instrucțiuni specifice.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definește rolurile și instrucțiunile agentului
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Creează instanțe de agenți
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Apoi, `WorkflowBuilder` este folosit pentru a construi graful. Agentul `front_desk_agent` este stabilit ca punct de pornire, iar o muchie este creată pentru a conecta ieșirea sa către `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

În final, workflow-ul este executat cu promptul inițial al utilizatorului.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run execută fluxul de lucru; get_outputs() returnează rezultatul executorului de ieșire.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analiza implementării în .NET (C#)

Implementarea .NET urmează o logică foarte similară. Mai întâi, se definesc constante pentru numele și instrucțiunile agenților.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agenții sunt creați folosind un `AzureOpenAIClient` (Responses API), apoi `WorkflowBuilder` definește fluxul secvențial prin adăugarea unei muchii de la `frontDeskAgent` către `reviewerAgent`.

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

Workflow-ul este apoi rulat cu mesajul utilizatorului, iar rezultatele sunt transmise în streaming înapoi.

### Caz 2: Workflow secvențial în mai mulți pași

Acest model extinde secvența de bază pentru a include mai mulți agenți. Este ideal pentru procese care necesită multiple etape de rafinare sau transformare.

#### Contextul scenariului

Un utilizator furnizează o imagine a unei camere de zi și cere o ofertă pentru mobilier.

1.  **Sales-Agent**: Identifică obiectele de mobilier din imagine și creează o listă.
2.  **Price-Agent**: Ia lista de obiecte și oferă o defalcare detaliată de preț, incluzând opțiuni bugetare, medii și premium.
3.  **Quote-Agent**: Primește lista cu prețuri și o formatează într-un document oficial de ofertă în Markdown.

*Diagramă a fluxului Sales -> Price -> Quote.*

#### Analiza implementării în Python

Sunt definiți trei agenți, fiecare cu un rol specializat. Workflow-ul este construit folosind `add_edge` pentru a crea un lanț: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Creează trei agenți specializați
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Construiește fluxul de lucru secvențial
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Intrarea este un `ChatMessage` care include atât text, cât și URI-ul imaginilor. Framework-ul gestionează transmiterea ieșirii fiecărui agent către următorul în secvență până când oferta finală este generată.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Mesajul utilizatorului conține atât text, cât și o imagine
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Rulează fluxul de lucru
events = await workflow.run(message)
```

#### Analiza implementării în .NET (C#)

Exemplul .NET oglindește versiunea Python. Sunt creați trei agenți (`salesagent`, `priceagent`, `quoteagent`). `WorkflowBuilder` îi leagă secvențial.

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

Mesajul utilizatorului este construit cu datele imaginii (ca octeți) și promptul text. Metoda `InProcessExecution.StreamAsync` inițiază workflow-ul, iar rezultatul final este capturat din stream.

### Caz 3: Workflow concurent

Acest model este folosit când sarcinile pot fi executate simultan pentru a economisi timp. Implică un „fan-out” către mai mulți agenți și un „fan-in” pentru a agrega rezultatele.

#### Contextul scenariului

Un utilizator cere să planifice o călătorie la Seattle.

1.  **Dispatcher (Fan-Out)**: Cererea utilizatorului este trimisă simultan către doi agenți.
2.  **Researcher-Agent**: Cercetează atracțiile, vremea și considerentele cheie pentru o călătorie la Seattle în decembrie.
3.  **Plan-Agent**: Creează independent un itinerariu detaliat zi cu zi.
4.  **Aggregator (Fan-In)**: Ieșirile de la cercetător și planificator sunt colectate și prezentate împreună ca rezultat final.

*Diagramă a fluxului concurent Researcher și Planner.*

#### Analiza implementării în Python

`ConcurrentBuilder` simplifică crearea acestui model. Pur și simplu listați agenții participanți, iar builder-ul creează automat logica necesară de fan-out și fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder gestionează logica de fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Rulează fluxul de lucru
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework-ul asigură că `research_agent` și `plan_agent` execută în paralel, iar ieșirile finale sunt colectate într-o listă.

#### Analiza implementării în .NET (C#)

În .NET, acest model necesită o definiție mai explicită. Sunt creați executori personalizați (`ConcurrentStartExecutor` și `ConcurrentAggregationExecutor`) pentru a gestiona logica de fan-out și fan-in.

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

`WorkflowBuilder` utilizează apoi `AddFanOutEdge` și `AddFanInEdge` pentru a construi graful cu acești executori personalizați și agenții.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Caz 4: Workflow condițional

Fluxurile condiționale introduc logică ramificată, permitând sistemului să ia rute diferite pe baza rezultatelor intermediare.

#### Contextul scenariului

Acest workflow automatizează crearea și publicarea unui tutorial tehnic.

1.  **Evangelist-Agent**: Scrie o schiță a tutorialului pe baza unui contur și URL-uri date.
2.  **ContentReviewer-Agent**: Revizuiește schița. Verifică dacă numărul de cuvinte depășește 200.
3.  **Ramură condițională**:
      * **Dacă este aprobat (`Yes`)**: Workflow-ul continuă către `Publisher-Agent`.
      * **Dacă este respins (`No`)**: Workflow-ul se oprește și afișează motivul respingerii.
4.  **Publisher-Agent**: Dacă schița este aprobată, acest agent salvează conținutul într-un fișier Markdown.

#### Analiza implementării în Python

Acest exemplu utilizează o funcție personalizată, `select_targets`, pentru a implementa logica condițională. Funcția este transmisă la `add_multi_selection_edge_group` și direcționează workflow-ul în funcție de câmpul `review_result` din ieșirea reviewer-ului.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Această funcție determină următorul pas pe baza rezultatului revizuirii
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Dacă este aprobat, se trece la executorul 'save_draft'
        return [save_draft_id]
    else:
        # Dacă este respins, se trece la executorul 'handle_review' pentru a raporta eșecul
        return [handle_review_id]

# Constructorul de flux de lucru folosește funcția de selecție pentru rutare
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Muchia de selecție multiplă implementează logica condițională
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Executorii personalizați, precum `to_reviewer_result`, sunt folosiți pentru a parsa ieșirea JSON a agenților și a o converti în obiecte cu tipar puternic pe care funcția de selecție le poate inspecta.

#### Analiza implementării în .NET (C#)

Versiunea .NET folosește o abordare similară cu o funcție de condiție. Se definește un `Func<object?, bool>` pentru a verifica proprietatea `Result` a obiectului `ReviewResult`.

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

Parametrul `condition` al metodei `AddEdge` permite `WorkflowBuilder` să creeze o cale ramificată. Workflow-ul va urma muchia către `publishExecutor` doar dacă condiția `GetCondition(expectedResult: "Yes")` este adevărată. În caz contrar, urmează calea către `sendReviewerExecutor`.

## Concluzie

Microsoft Agent Framework Workflow oferă o fundație robustă și flexibilă pentru orchestrarea sistemelor complexe multi-agent. Prin valorificarea arhitecturii sale bazate pe grafuri și a componentelor de bază, dezvoltatorii pot proiecta și implementa fluxuri de lucru sofisticate în Python și .NET. Indiferent dacă aplicația dumneavoastră necesită procesare secvențială simplă, execuție paralelă sau logică condițională dinamică, framework-ul oferă instrumentele pentru a construi soluții AI puternice, scalabile și sigure din punct de vedere al tipurilor.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->