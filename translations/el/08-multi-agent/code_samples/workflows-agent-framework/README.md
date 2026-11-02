# Δημιουργία Εφαρμογών Πολλαπλών Πρακτόρων με το Microsoft Agent Framework Workflow

Αυτό το σεμινάριο θα σας καθοδηγήσει στην κατανόηση και δημιουργία εφαρμογών πολλαπλών πρακτόρων χρησιμοποιώντας το Microsoft Agent Framework. Θα εξερευνήσουμε τις βασικές έννοιες των συστημάτων πολλαπλών πρακτόρων, θα εμβαθύνουμε στην αρχιτεκτονική του συστατικού Workflow του πλαισίου και θα περιηγηθούμε σε πρακτικά παραδείγματα σε Python και .NET για διαφορετικά πρότυπα ροής εργασιών.

## 1\. Κατανόηση των Συστημάτων Πολλαπλών Πρακτόρων

Ένας Πράκτορας Τεχνητής Νοημοσύνης είναι ένα σύστημα που υπερβαίνει τις δυνατότητες ενός τυπικού Μεγάλου Μοντέλου Γλώσσας (LLM). Μπορεί να αντιλαμβάνεται το περιβάλλον του, να λαμβάνει αποφάσεις και να εκτελεί ενέργειες για να επιτύχει συγκεκριμένους στόχους. Ένα σύστημα πολλαπλών πρακτόρων περιλαμβάνει αρκετούς από αυτούς τους πράκτορες που συνεργάζονται για να επιλύσουν ένα πρόβλημα που θα ήταν δύσκολο ή αδύνατο να χειριστεί ένας μόνος πράκτορας.

### Συνήθη Σενάρια Εφαρμογών

  * **Πολύπλοκη Επίλυση Προβλημάτων**: Διαχωρισμός ενός μεγάλου έργου (π.χ. οργάνωση εταιρικής εκδήλωσης) σε μικρότερα υπο-έργα που ανατίθενται σε εξειδικευμένους πράκτορες (π.χ. πράκτορας προϋπολογισμού, πράκτορας logistics, πράκτορας marketing).
  * **Εικονικοί Βοηθοί**: Ένας κύριος βοηθός-πράκτορας αναθέτει εργασίες όπως προγραμματισμό, έρευνα και κρατήσεις σε άλλους εξειδικευμένους πράκτορες.
  * **Αυτοματοποιημένη Δημιουργία Περιεχομένου**: Μια ροή εργασίας όπου ένας πράκτορας συντάσσει περιεχόμενο, ένας άλλος το ελέγχει για ακρίβεια και τόνο, και ένας τρίτος το δημοσιεύει.

### Πρότυπα Πολλαπλών Πρακτόρων

Τα συστήματα πολλαπλών πρακτόρων μπορούν να οργανωθούν σε διάφορα πρότυπα, που καθορίζουν τον τρόπο αλληλεπίδρασής τους:

  * **Ακολουθιακό**: Οι πράκτορες εργάζονται με προκαθορισμένη σειρά, σαν γραμμή συναρμολόγησης. Το αποτέλεσμα ενός πράκτορα γίνεται η είσοδος για τον επόμενο.
  * **Ταυτόχρονο**: Οι πράκτορες εργάζονται παράλληλα σε διαφορετικά μέρη μιας εργασίας, και τα αποτελέσματά τους συγκεντρώνονται στο τέλος.
  * **Υπό Συνθήκη**: Η ροή εργασίας ακολουθεί διαφορετικές διαδρομές με βάση την έξοδο ενός πράκτορα, παρόμοια με μια δήλωση if-then-else.

## 2\. Αρχιτεκτονική του Microsoft Agent Framework Workflow

Το σύστημα ροής εργασιών του Agent Framework είναι ένας προηγμένος μηχανισμός ορχήστρωσης σχεδιασμένος για τη διαχείριση σύνθετων αλληλεπιδράσεων μεταξύ πολλαπλών πρακτόρων. Βασίζεται σε μια αρχιτεκτονική βασισμένη σε γράφο που χρησιμοποιεί ένα [εκτελεστικό μοντέλο τύπου Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), όπου η επεξεργασία γίνεται σε συγχρονισμένα βήματα που ονομάζονται «supersteps».

### Κύρια Συστατικά

Η αρχιτεκτονική αποτελείται από τρία βασικά μέρη:

1.  **Εκτελεστές**: Αυτοί είναι οι θεμελιώδεις μονάδες επεξεργασίας. Στα παραδείγματά μας, ένας `Agent` είναι τύπος εκτελεστή. Κάθε εκτελεστής μπορεί να έχει πολλούς χειριστές μηνυμάτων που καλούνται αυτόματα ανάλογα με τον τύπο του λαμβανόμενου μηνύματος.
2.  **Άκρες**: Αυτές ορίζουν τη διαδρομή που ακολουθούν τα μηνύματα μεταξύ των εκτελεστών. Οι άκρες μπορούν να έχουν προϋποθέσεις, επιτρέποντας δυναμική δρομολόγηση της πληροφορίας μέσα στον γράφο ροής εργασίας.
3.  **Ροή Εργασίας**: Αυτό το συστατικό ορχηστρώνει ολόκληρη τη διαδικασία, διαχειρίζεται τους εκτελεστές, τις άκρες και τη συνολική ροή εκτέλεσης. Εξασφαλίζει ότι τα μηνύματα επεξεργάζονται με τη σωστή σειρά και μεταδίδει γεγονότα για την παρατηρησιμότητα.

*Διάγραμμα που απεικονίζει τα κύρια συστατικά του συστήματος ροής εργασίας.*

Αυτή η δομή επιτρέπει τη δημιουργία ανθεκτικών και κλιμακούμενων εφαρμογών χρησιμοποιώντας βασικά πρότυπα όπως ακολουθιακές αλυσίδες, fan-out/fan-in για παράλληλη επεξεργασία και λογική switch-case για υπό συνθήκη ροές.

## 3\. Πρακτικά Παραδείγματα και Ανάλυση Κώδικα

Ας εξερευνήσουμε τώρα πώς να υλοποιήσουμε διαφορετικά πρότυπα ροής εργασίας χρησιμοποιώντας το πλαίσιο. Θα δούμε τόσο κώδικα Python όσο και .NET για κάθε παράδειγμα.

### Περίπτωση 1: Βασική Ακολουθιακή Ροή Εργασίας

Αυτό είναι το απλούστερο πρότυπο, όπου η έξοδος ενός πράκτορα μεταβιβάζεται απευθείας σε άλλον. Το σενάριό μας περιλαμβάνει έναν πράκτορα ξενοδοχείου `FrontDesk` που κάνει μια σύσταση ταξιδιού, η οποία στη συνέχεια εξετάζεται από έναν πράκτορα `Concierge`.

*Διάγραμμα της βασικής ροής εργασίας FrontDesk -> Concierge.*

#### Ιστορικό Σεναρίου

Ένας ταξιδιώτης ζητά μια σύσταση για το Παρίσι.

1.  Ο πράκτορας `FrontDesk`, σχεδιασμένος για συνοπτικότητα, προτείνει την επίσκεψη στο Μουσείο του Λούβρου.
2.  Ο πράκτορας `Concierge`, που προτεραιοποιεί αυθεντικές εμπειρίες, λαμβάνει αυτή την πρόταση. Την εξετάζει και παρέχει σχόλια, προτείνοντας μια πιο τοπική, λιγότερο τουριστική εναλλακτική.

#### Ανάλυση Υλοποίησης Python

Στο παράδειγμα Python, ορίζουμε και δημιουργούμε πρώτα τους δύο πράκτορες, ο καθένας με συγκεκριμένες οδηγίες.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Ορίστε ρόλους και οδηγίες πρακτόρων
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Δημιουργήστε στιγμιότυπα πρακτόρων
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Στη συνέχεια, χρησιμοποιείται ο `WorkflowBuilder` για να κατασκευάσουμε τον γράφο. Ο `front_desk_agent` ορίζεται ως το σημείο εκκίνησης και δημιουργείται μια άκρη που συνδέει την έξοδό του με τον `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Τέλος, εκτελείται η ροή εργασίας με το αρχικό μήνυμα του χρήστη.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# Το run εκτελεί τη ροή εργασίας· το get_outputs() επιστρέφει το αποτέλεσμα του εκτελεστή εξόδου.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Ανάλυση Υλοποίησης .NET (C#)

Η υλοποίηση .NET ακολουθεί πολύ παρόμοια λογική. Πρώτα ορίζονται σταθερές για τα ονόματα και τις οδηγίες των πρακτόρων.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Οι πράκτορες δημιουργούνται χρησιμοποιώντας έναν `AzureOpenAIClient` (API Απαντήσεων), και μετά ο `WorkflowBuilder` ορίζει τη ακολουθιακή ροή προσθέτοντας μια άκρη από τον `frontDeskAgent` προς τον `reviewerAgent`.

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

Η ροή εργασίας εκτελείται με το μήνυμα του χρήστη και τα αποτελέσματα ρέουν πίσω σε πραγματικό χρόνο.

### Περίπτωση 2: Ακολουθιακή Ροή Εργασίας Πολλαπλών Βημάτων

Αυτό το πρότυπο επεκτείνει την βασική ακολουθία για να συμπεριλάβει περισσότερους πράκτορες. Είναι ιδανικό για διαδικασίες που απαιτούν πολλαπλά στάδια βελτίωσης ή μετασχηματισμού.

#### Ιστορικό Σεναρίου

Ένας χρήστης παρέχει μια εικόνα σαλονιού και ζητά μια προσφορά επίπλων.

1.  **Πράκτορας Πωλήσεων**: Αναγνωρίζει τα έπιπλα στην εικόνα και δημιουργεί μια λίστα.
2.  **Πράκτορας Τιμών**: Λαμβάνει τη λίστα αντικειμένων και παρέχει αναλυτική ανάλυση τιμών, συμπεριλαμβανομένων επιλογών προϋπολογισμού, μέσης κατηγορίας και premium.
3.  **Πράκτορας Προσφοράς**: Λαμβάνει τη λίστα με τιμές και την μορφοποιεί σε επίσημο έγγραφο προσφοράς σε Markdown.

*Διάγραμμα της ροής εργασίας Sales -> Price -> Quote.*

#### Ανάλυση Υλοποίησης Python

Ορίζονται τρεις πράκτορες, καθένας με εξειδικευμένο ρόλο. Η ροή εργασίας κατασκευάζεται χρησιμοποιώντας `add_edge` για να δημιουργηθεί μια αλυσίδα: `sales_agent` -> `price_agent` -> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Δημιουργήστε τρεις εξειδικευμένους πράκτορες
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Δημιουργήστε τη διαδοχική ροή εργασίας
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Η είσοδος είναι ένα `ChatMessage` που περιλαμβάνει τόσο κείμενο όσο και το URI της εικόνας. Το πλαίσιο διαχειρίζεται τη μεταφορά της εξόδου κάθε πράκτορα στον επόμενο στη σειρά μέχρι να παραχθεί η τελική προσφορά.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Το μήνυμα του χρήστη περιέχει τόσο κείμενο όσο και μια εικόνα
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Εκτέλεση της ροής εργασίας
events = await workflow.run(message)
```

#### Ανάλυση Υλοποίησης .NET (C#)

Το παράδειγμα .NET αντικατοπτρίζει την έκδοση Python. Δημιουργούνται τρεις πράκτορες (`salesagent`, `priceagent`, `quoteagent`). Ο `WorkflowBuilder` τους συνδέει ακολουθιακά.

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

Το μήνυμα του χρήστη κατασκευάζεται με δεδομένα εικόνας (ως bytes) και το κείμενο προτροπής. Η μέθοδος `InProcessExecution.RunStreamingAsync` ξεκινά τη ροή εργασίας και η τελική έξοδος λαμβάνεται από το ρεύμα.

### Περίπτωση 3: Ταυτόχρονη Ροή Εργασίας

Αυτό το πρότυπο χρησιμοποιείται όταν οι εργασίες μπορούν να εκτελεστούν ταυτόχρονα για εξοικονόμηση χρόνου. Περιλαμβάνει ένα «fan-out» σε πολλούς πράκτορες και «fan-in» για τη συγκέντρωση των αποτελεσμάτων.

#### Ιστορικό Σεναρίου

Ένας χρήστης ζητά να σχεδιάσει ένα ταξίδι στο Σιάτλ.

1.  **Διανομέας (Fan-Out)**: Το αίτημα του χρήστη αποστέλλεται ταυτόχρονα σε δύο πράκτορες.
2.  **Πράκτορας Ερευνών**: Ερευνά αξιοθέατα, καιρό και βασικά ζητήματα για ένα ταξίδι στο Σιάτλ τον Δεκέμβριο.
3.  **Πράκτορας Σχεδιασμού**: Δημιουργεί ανεξάρτητα ένα αναλυτικό ημερήσιο πρόγραμμα ταξιδιού.
4.  **Συγκεντρωτής (Fan-In)**: Συλλέγει και παρουσιάζει τα αποτελέσματα από τον ερευνητή και τον σχεδιαστή ως τελικό αποτέλεσμα.

*Διάγραμμα της ταυτόχρονης ροής ερευνητή και σχεδιαστή.*

#### Ανάλυση Υλοποίησης Python

Ο `ConcurrentBuilder` απλοποιεί τη δημιουργία αυτού του προτύπου. Απλώς παραθέτετε τους συμμετέχοντες πράκτορες, και ο builder δημιουργεί αυτόματα τη λογική fan-out και fan-in.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# Το ConcurrentBuilder χειρίζεται τη λογική fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Εκτέλεση της ροής εργασίας
events = await workflow.run("Plan a trip to Seattle in December")
```

Το πλαίσιο εξασφαλίζει ότι οι `research_agent` και `plan_agent` εκτελούνται παράλληλα, και οι τελικές εξόδους τους συλλέγονται σε λίστα.

#### Ανάλυση Υλοποίησης .NET (C#)

Στο .NET, αυτό το πρότυπο απαιτεί πιο ρητό ορισμό. Δημιουργούνται προσαρμοσμένοι εκτελεστές (`ConcurrentStartExecutor` και `ConcurrentAggregationExecutor`) για τη διαχείριση της λογικής fan-out και fan-in.

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

Ο `WorkflowBuilder` χρησιμοποιεί στη συνέχεια `AddFanOutEdge` και `AddFanInEdge` για να κατασκευάσει τον γράφο με αυτούς τους προσαρμοσμένους εκτελεστές και τους πράκτορες.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Περίπτωση 4: Υπό Συνθήκη Ροή Εργασίας

Οι υπό συνθήκη ροές εργασίας εισάγουν διακλαδώσεις λογικής, επιτρέποντας στο σύστημα να ακολουθήσει διαφορετικές διαδρομές βασισμένες σε ενδιάμεσα αποτελέσματα.

#### Ιστορικό Σεναρίου

Αυτή η ροή εργασίας αυτοματοποιεί τη δημιουργία και δημοσίευση ενός τεχνικού σεμιναρίου.

1.  **Πράκτορας Ευαγγελισμού**: Γράφει ένα προσχέδιο του σεμιναρίου βάσει δομής και URLs.
2.  **Πράκτορας Επανεξέτασης Περιεχομένου**: Επανεξετάζει το προσχέδιο. Ελέγχει αν ο αριθμός λέξεων υπερβαίνει τις 200.
3.  **Υπό Συνθήκη Διακλάδωση**:
      * **Εάν Εγκριθεί (`Ναι`)**: Η ροή συνεχίζει προς τον `Publisher-Agent`.
      * **Εάν Απορριφθεί (`Όχι`)**: Η ροή σταματά και επιστρέφει τον λόγο απόρριψης.
4.  **Πράκτορας Δημοσίευσης**: Εάν το προσχέδιο εγκριθεί, αυτός ο πράκτορας αποθηκεύει το περιεχόμενο σε αρχείο Markdown.

#### Ανάλυση Υλοποίησης Python

Αυτό το παράδειγμα χρησιμοποιεί μια προσαρμοσμένη συνάρτηση, `select_targets`, για να υλοποιήσει τη λογική υπό συνθήκη. Αυτή η συνάρτηση περνά στο `add_multi_selection_edge_group` και κατευθύνει τη ροή βάσει του πεδίου `review_result` της εξόδου του αναθεωρητή.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Αυτή η συνάρτηση καθορίζει το επόμενο βήμα βάσει του αποτελέσματος της αξιολόγησης
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Εάν εγκριθεί, προχωρήστε στον εκτελεστή 'save_draft'
        return [save_draft_id]
    else:
        # Εάν απορριφθεί, προχωρήστε στον εκτελεστή 'handle_review' για να αναφέρετε αποτυχία
        return [handle_review_id]

# Ο κατασκευαστής ροής εργασιών χρησιμοποιεί τη συνάρτηση επιλογής για δρομολόγηση
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Η πολλαπλή επιλογή άκρου υλοποιεί τη συνθηκηκή λογική
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Χρησιμοποιούνται προσαρμοσμένοι εκτελεστές όπως `to_reviewer_result` για να αναλύσουν την έξοδο JSON των πρακτόρων και να τη μετατρέψουν σε αντικείμενα ισχυρού τύπου που μπορεί να εξετάσει η συνάρτηση επιλογής.

#### Ανάλυση Υλοποίησης .NET (C#)

Η έκδοση .NET χρησιμοποιεί παρόμοια προσέγγιση με συνάρτηση συνθήκης. Ορίζεται μια `Func<object?, bool>` για να ελέγχει την ιδιότητα `Result` του αντικειμένου `ReviewResult`.

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

Η παράμετρος `condition` της μεθόδου `AddEdge` επιτρέπει στο `WorkflowBuilder` να δημιουργήσει διακλαδώμενη διαδρομή. Η ροή εργασίας θα ακολουθήσει την άκρη προς τον `publishExecutor` μόνο αν η συνθήκη `GetCondition(expectedResult: "Yes")` επιστρέψει true. Διαφορετικά, θα ακολουθήσει τη διαδρομή προς τον `sendReviewerExecutor`.

## Συμπέρασμα

Το Microsoft Agent Framework Workflow παρέχει μια ισχυρή και ευέλικτη βάση για την ορχήστρωση σύνθετων συστημάτων πολλαπλών πρακτόρων. Εκμεταλλευόμενοι την αρχιτεκτονική βασισμένη σε γράφους και τα κύρια συστατικά, οι προγραμματιστές μπορούν να σχεδιάσουν και να υλοποιήσουν εξελιγμένες ροές εργασιών τόσο σε Python όσο και σε .NET. Είτε η εφαρμογή σας απαιτεί απλή ακολουθιακή επεξεργασία, παράλληλη εκτέλεση ή δυναμική υπό συνθήκη λογική, το πλαίσιο προσφέρει τα εργαλεία για να δημιουργήσετε ισχυρές, κλιμακούμενες και τύπου-ασφαλείς λύσεις με τεχνητή νοημοσύνη.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->