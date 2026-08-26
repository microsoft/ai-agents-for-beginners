# Εξερευνώντας το Microsoft Agent Framework

![Agent Framework](../../../translated_images/el/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Κατανόηση του Microsoft Agent Framework: Βασικά Χαρακτηριστικά και Αξία  
- Εξερεύνηση των Βασικών Εννοιών του Microsoft Agent Framework
- Προηγμένα Μοντέλα MAF: Ροές Εργασίας, Μεσολαβητές και Μνήμη

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα ξέρετε πώς να:

- Δημιουργείτε Παραγωγικούς Έτοιμους AI Agents χρησιμοποιώντας το Microsoft Agent Framework
- Εφαρμόζετε τα βασικά χαρακτηριστικά του Microsoft Agent Framework στις περιπτώσεις χρήσης του Agent σας
- Χρησιμοποιείτε προηγμένα μοντέλα όπως ροές εργασίας, μεσολαβητές και παρατηρησιμότητα

## Παραδείγματα Κώδικα 

Παραδείγματα κώδικα για το [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) μπορείτε να βρείτε σε αυτό το αποθετήριο στα αρχεία `xx-python-agent-framework` και `xx-dotnet-agent-framework`.

## Κατανόηση του Microsoft Agent Framework

![Framework Intro](../../../translated_images/el/framework-intro.077af16617cf130c.webp)

Το [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) είναι το ενοποιημένο πλαίσιο της Microsoft για τη δημιουργία AI agents. Προσφέρει την ευελιξία να ανταποκριθεί σε πλήθος περιπτώσεων χρήσης agents που συναντώνται τόσο σε παραγωγικά όσο και σε ερευνητικά περιβάλλοντα, όπως:

- **Διαδοχικός συντονισμός** σε σενάρια όπου απαιτούνται βήμα προς βήμα ροές εργασίας.
- **Παράλληλος συντονισμός** σε σενάρια όπου οι agents πρέπει να ολοκληρώσουν εργασίες ταυτόχρονα.
- **Ομαδικός συντονισμός συνομιλίας** σε σενάρια όπου οι agents μπορούν να συνεργαστούν σε μία εργασία.
- **Παράδοση εργασιών** σε σενάρια όπου οι agents παραδίδουν την εργασία ο ένας στον άλλο καθώς ολοκληρώνονται τα υπο-μερίδια.
- **Μαγνητικός συντονισμός** σε σενάρια όπου ένας διαχειριστής agent δημιουργεί και τροποποιεί λίστα εργασιών και χειρίζεται το συντονισμό υποagents για την ολοκλήρωση της εργασίας.

Για την παροχή AI Agents σε παραγωγή, το MAF περιλαμβάνει επίσης χαρακτηριστικά για:

- **Παρατηρησιμότητα** μέσω της χρήσης του OpenTelemetry όπου κάθε ενέργεια του AI Agent, συμπεριλαμβανομένης της κλήσης εργαλείων, των βημάτων ορχήστρωσης, των ροών λογικής και της παρακολούθησης απόδοσης μέσω πινάκων Microsoft Foundry.
- **Ασφάλεια** φιλοξενώντας agents εγγενώς στο Microsoft Foundry που περιλαμβάνει ελέγχους ασφαλείας όπως πρόσβαση βάσει ρόλων, διαχείριση ιδιωτικών δεδομένων και ενσωματωμένη ασφάλεια περιεχομένου.
- **Ανθεκτικότητα** καθώς τα νήματα και οι ροές εργασίας των agents μπορούν να παγώσουν, να συνεχιστούν και να ανακάμψουν από σφάλματα, επιτρέποντας μακροχρόνιες διαδικασίες.
- **Έλεγχος** καθώς υποστηρίζονται ροές εργασίας με ανθρώπινη παρέμβαση όπου οι εργασίες χαρακτηρίζονται ως απαιτούσες ανθρώπινη έγκριση.

Το Microsoft Agent Framework εστιάζει επίσης στην διαλειτουργικότητα μέσω:

- **Παραγωγικού ανεξάρτητου** - Οι agents μπορούν να τρέχουν σε containers, on-prem και σε πολλαπλά διαφορετικά νέφη.
- **Παρέχοντος ανεξάρτητου** - Οι agents μπορούν να δημιουργηθούν μέσω του αγαπημένου σας SDK συμπεριλαμβανομένων των Azure OpenAI και OpenAI
- **Ενσωμάτωσης Ανοιχτών Προτύπων** - Οι agents μπορούν να χρησιμοποιούν πρωτόκολλα όπως Agent-to-Agent (A2A) και Model Context Protocol (MCP) για να ανακαλύπτουν και να χρησιμοποιούν άλλους agents και εργαλεία.
- **Πρόσθετα και Συνδέσμους** - Μπορούν να γίνουν συνδέσεις με υπηρεσίες δεδομένων και μνήμης όπως Microsoft Fabric, SharePoint, Pinecone και Qdrant.

Ας δούμε πώς αυτά τα χαρακτηριστικά εφαρμόζονται σε μερικές από τις βασικές έννοιες του Microsoft Agent Framework.

## Βασικές Έννοιες του Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/el/agent-components.410a06daf87b4fef.webp)

**Δημιουργία Agents**

Η δημιουργία agent γίνεται ορίζοντας την υπηρεσία αναφοράς (Πάροχος LLM), ένα
σύνολο οδηγιών που ο AI Agent πρέπει να ακολουθήσει, και ένα εκχωρημένο `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Το παραπάνω χρησιμοποιεί `Azure OpenAI` αλλά οι agents μπορούν να δημιουργηθούν χρησιμοποιώντας διάφορες υπηρεσίες συμπεριλαμβανομένου του `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

Το OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ή το [MiniMax](https://platform.minimaxi.com/), που παρέχει μια συμβατή με OpenAI API με μεγάλα παράθυρα συμφραζομένων (έως 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ή απομακρυσμένοι agents χρησιμοποιώντας το πρωτόκολλο A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Εκτέλεση Agents**

Οι agents εκτελούνται χρησιμοποιώντας τις μεθόδους `.run` ή `.run_stream` για μη-ροές ή ροές απαντήσεων αντίστοιχα.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Κάθε εκτέλεση agent μπορεί επίσης να έχει επιλογές για παραμετροποίηση όπως τον αριθμό `max_tokens` που χρησιμοποιεί ο agent, τα `tools` που ο agent μπορεί να καλέσει, και ακόμη το ίδιο το `model` που χρησιμοποιείται για τον agent.

Αυτό είναι χρήσιμο σε περιπτώσεις όπου συγκεκριμένα μοντέλα ή εργαλεία απαιτούνται για την ολοκλήρωση μιας εργασίας του χρήστη.

**Εργαλεία**

Τα εργαλεία μπορούν να οριστούν τόσο κατά τον ορισμό του agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Όταν δημιουργείτε απευθείας έναν ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

όσο και κατά την εκτέλεση του agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Εργαλείο που παρέχεται μόνο για αυτήν την εκτέλεση )
```

**Νήματα Agent**

Τα νήματα agent χρησιμοποιούνται για τη διαχείριση συνομιλιών πολλαπλών βημάτων. Τα νήματα μπορούν να δημιουργηθούν είτε με:

- Χρήση του `get_new_thread()` που επιτρέπει την αποθήκευση του νήματος σε βάθος χρόνου
- Δημιουργία αυτόματου νήματος κατά την εκτέλεση ενός agent και το νήμα διαρκεί μόνο κατά τη διάρκεια της τρέχουσας εκτέλεσης.

Για να δημιουργηθεί ένα νήμα, ο κώδικας είναι ως εξής:

```python
# Δημιουργήστε ένα νέο νήμα.
thread = agent.get_new_thread() # Εκτελέστε τον πράκτορα με το νήμα.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Στη συνέχεια μπορείτε να σειριοποιήσετε το νήμα για να αποθηκευτεί για μελλοντική χρήση:

```python
# Δημιουργήστε ένα νέο νήμα.
thread = agent.get_new_thread() 

# Εκτελέστε τον πράκτορα με το νήμα.

response = await agent.run("Hello, how are you?", thread=thread) 

# Σειριοποιήστε το νήμα για αποθήκευση.

serialized_thread = await thread.serialize() 

# Αποσειριοποιήστε την κατάσταση του νήματος μετά τη φόρτωση από την αποθήκευση.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Μεσολαβητής Agent**

Οι agents αλληλεπιδρούν με εργαλεία και LLMs για να ολοκληρώσουν εργασίες χρηστών. Σε ορισμένα σενάρια, θέλουμε να εκτελούμε ή να παρακολουθούμε ενδιάμεσες ενέργειες. Ο μεσολαβητής agent μας επιτρέπει να το κάνουμε αυτό μέσω:

*Λειτουργία Μεσολάβησης*

Αυτός ο μεσολαβητής επιτρέπει την εκτέλεση μιας ενέργειας μεταξύ του agent και μιας λειτουργίας/εργαλείου που θα καλέσει. Ένα παράδειγμα είναι όταν θέλατε να κάνετε καταγραφή της κλήσης της λειτουργίας.

Στον κώδικα παρακάτω, το `next` ορίζει αν πρέπει να κληθεί ο επόμενος μεσολαβητής ή η ίδια η λειτουργία.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Προεπεξεργασία: Καταγραφή πριν την εκτέλεση της λειτουργίας
    print(f"[Function] Calling {context.function.name}")

    # Συνέχεια στο επόμενο middleware ή εκτέλεση λειτουργίας
    await next(context)

    # Μετα-επεξεργασία: Καταγραφή μετά την εκτέλεση της λειτουργίας
    print(f"[Function] {context.function.name} completed")
```

*Μεσολαβητής Συνομιλίας*

Αυτός ο μεσολαβητής μας επιτρέπει να εκτελέσουμε ή να καταγράψουμε μια ενέργεια μεταξύ του agent και των αιτημάτων προς το LLM.

Περιέχει σημαντικές πληροφορίες όπως τα `messages` που αποστέλλονται στην υπηρεσία AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Προεπεξεργασία: Καταγραφή πριν από την κλήση AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Συνέχεια στο επόμενο middleware ή υπηρεσία AI
    await next(context)

    # Μετα-επεξεργασία: Καταγραφή μετά την απόκριση AI
    print("[Chat] AI response received")

```

**Μνήμη Agent**

Όπως καλύφθηκε στο μάθημα `Agentic Memory`, η μνήμη είναι σημαντικός παράγοντας για την λειτουργία του agent σε διαφορετικά πλαίσια. Το MAF προσφέρει διάφορους τύπους μνήμης:

*Μνήμη Προσωρινής Αποθήκευσης (In-Memory Storage)*

Πρόκειται για μνήμη που αποθηκεύεται στα νήματα κατά τη διάρκεια εκτέλεσης της εφαρμογής.

```python
# Δημιουργήστε ένα νέο νήμα.
thread = agent.get_new_thread() # Εκτελέστε τον πράκτορα με το νήμα.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Μηνύματα Διαρκείας (Persistent Messages)*

Αυτή η μνήμη χρησιμοποιείται για την αποθήκευση ιστορικού συνομιλιών μεταξύ διαφορετικών συνεδριών. Ορίζεται με τη χρήση του `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Δημιουργήστε έναν προσαρμοσμένο αποθηκευτικό χώρο μηνυμάτων
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Δυναμική Μνήμη (Dynamic Memory)*

Αυτή η μνήμη προστίθεται στο πλαίσιο πριν την εκτέλεση των agents. Αυτές οι μνήμες μπορούν να αποθηκευτούν σε εξωτερικές υπηρεσίες όπως mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Χρησιμοποιώντας το Mem0 για προχωρημένες δυνατότητες μνήμης
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**Παρατηρησιμότητα Agent**

Η παρατηρησιμότητα είναι σημαντική για την κατασκευή αξιόπιστων και εύκολα συντηρήσιμων agentic συστημάτων. Το MAF ενσωματώνεται με το OpenTelemetry για να παρέχει ιχνηλάτηση και μετρητές για καλύτερη παρατηρησιμότητα.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # κάνε κάτι
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Ροές Εργασίας (Workflows)

Το MAF προσφέρει ροές εργασίας που είναι προ-ορισμένα βήματα για την ολοκλήρωση μιας εργασίας και περιλαμβάνουν AI agents ως συστατικά σε αυτά τα βήματα.

Οι ροές εργασίας αποτελούνται από διάφορα στοιχεία που επιτρέπουν καλύτερο έλεγχο της ροής. Οι ροές εργασίας επίσης επιτρέπουν **πολλαπλό συντονισμό agents** και **checkpointing** για την αποθήκευση καταστάσεων ροής εργασίας.

Τα βασικά στοιχεία μιας ροής εργασίας είναι:

**Εκτελεστές**

Οι εκτελεστές λαμβάνουν τα εισερχόμενα μηνύματα, εκτελούν τις ανατεθειμένες εργασίες και παράγουν ένα εξερχόμενο μήνυμα. Αυτό κινεί τη ροή εργασίας προς την ολοκλήρωση της μεγαλύτερης εργασίας. Οι εκτελεστές μπορούν να είναι AI agents ή προσαρμοσμένη λογική.

**Άκρα (Edges)**

Τα άκρα χρησιμοποιούνται για τον ορισμό της ροής των μηνυμάτων σε μια ροή εργασίας. Αυτά μπορούν να είναι:

*Άμεσα Άκρα* - Απλές συνδέσεις ένα-προς-ένα μεταξύ εκτελεστών:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Υπό όρους Άκρα* - Ενεργοποιούνται αφού ικανοποιηθεί μια συγκεκριμένη συνθήκη. Για παράδειγμα, όταν τα δωμάτια ξενοδοχείων δεν είναι διαθέσιμα, ένας εκτελεστής μπορεί να προτείνει άλλες επιλογές.

*Εναλλακτικά Άκρα (Switch-case Edges)* - Δρομολογούν μηνύματα σε διαφορετικούς εκτελεστές βάσει ορισμένων προϋποθέσεων. Για παράδειγμα, αν ένας πελάτης ταξιδιών έχει προτεραιότητα, οι εργασίες του θα χειριστούν μέσω άλλης ροής εργασίας.

*Φαν-άουτ Άκρα* - Στέλνουν ένα μήνυμα σε πολλαπλούς στόχους.

*Φαν-ιν Άκρα* - Συλλέγουν πολλαπλά μηνύματα από διαφορετικούς εκτελεστές και τα στέλνουν σε έναν στόχο.

**Γεγονότα**

Για την καλύτερη παρατηρησιμότητα των ροών εργασίας, το MAF παρέχει ενσωματωμένα γεγονότα εκτέλεσης όπως:

- `WorkflowStartedEvent`  - Ξεκινά η εκτέλεση ροής εργασίας
- `WorkflowOutputEvent` - Η ροή εργασίας παράγει έξοδο
- `WorkflowErrorEvent` - Η ροή εργασίας συναντά σφάλμα
- `ExecutorInvokeEvent`  - Ο εκτελεστής ξεκινά την επεξεργασία
- `ExecutorCompleteEvent`  -  Ο εκτελεστής ολοκληρώνει την επεξεργασία
- `RequestInfoEvent` - Έχει γίνει αίτημα

## Προηγμένα Μοντέλα MAF

Τα παραπάνω καλύπτουν τις βασικές έννοιες του Microsoft Agent Framework. Καθώς δημιουργείτε πιο σύνθετους agents, δείτε μερικά προηγμένα μοντέλα προς εξέταση:

- **Σύνθεση Μεσολαβητών**: Συνδυάστε πολλούς handlers μεσολαβητή (καταγραφή, έλεγχος ταυτότητας, περιορισμός ρυθμού) χρησιμοποιώντας λειτουργίες και μεσολαβητές συνομιλίας για λεπτομερή έλεγχο της συμπεριφοράς του agent.
- **Checkpointing Ροής Εργασίας**: Χρησιμοποιήστε γεγονότα ροής εργασίας και σειριοποίηση για να αποθηκεύετε και να συνεχίζετε μακροχρόνιες διαδικασίες agent.
- **Δυναμική Επιλογή Εργαλείων**: Συνδυάστε RAG πάνω σε περιγραφές εργαλείων με την καταχώρηση εργαλείων του MAF για να παρουσιάσετε μόνο τα σχετικά εργαλεία ανά ερώτημα.
- **Πολλαπλή Παράδοση Agent**: Χρησιμοποιήστε άκρα ροής εργασίας και υπό όρους δρομολόγηση για τον συντονισμό παραδόσεων μεταξύ εξειδικευμένων agents.

## Φιλοξενώντας LangChain / LangGraph Agents στο Microsoft Foundry

Το Microsoft Agent Framework είναι **διαλειτουργικό** — δεν περιορίζεστε σε agents γραμμένους με MAF. Αν έχετε ήδη ένα agent χτισμένο με **LangChain** ή **LangGraph**, μπορείτε να το εκτελέσετε ως **φιλοξενούμενο agent στο Microsoft Foundry** έτσι ώστε το Foundry να διαχειρίζεται το runtime, τις συνεδρίες, την κλιμάκωση, την ταυτότητα και τα πρωτόκολλα τέλους για εσάς, ενώ η λογική του agent παραμένει στο LangGraph.

Αυτό γίνεται με το πακέτο `langchain_azure_ai.agents.hosting`, που εκθέτει έναν μεταγλωττισμένο γράφο LangGraph πάνω στα ίδια πρωτόκολλα που χρησιμοποιούν οι φιλοξενούμενοι agents του Foundry.

**1. Εγκαταστήστε το πρόσθετο φιλοξενίας (hosting extra):**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Το `hosting` extra εγκαθιστά τις βιβλιοθήκες πρωτοκόλλου Foundry: `azure-ai-agentserver-responses` (το συμβατό με OpenAI endpoint `/responses`) και `azure-ai-agentserver-invocations` (το γενικό endpoint `/invocations`).

**2. Επιλέξτε ένα πρωτόκολλο φιλοξενίας:**

| Πρωτόκολλο | Κλάση Host | Endpoint | Χρησιμοποιείται όταν |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Θέλετε συμβατή με OpenAI συνομιλία, ροή, ιστορικό απαντήσεων και νήματα συνομιλίας — η συνιστώμενη προεπιλογή για συνομιλιακούς agents. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Χρειάζεστε προσαρμοσμένο σχήμα JSON, webhook-style endpoint, ή μη-συνομιλιακή επεξεργασία. |

Επειδή το **Responses API είναι το βασικό API για ανάπτυξη agent-style στο Foundry**, ξεκινήστε με `ResponsesHostServer` για τους περισσότερους agents.

**3. Ρυθμίστε μεταβλητές περιβάλλοντος** (`az login` πρώτα για να μπορεί το `DefaultAzureCredential` να αυθεντικοποιηθεί):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Όταν ο agent εκτελεστεί αργότερα ως φιλοξενούμενος agent στο Foundry, η πλατφόρμα ενσωματώνει αυτόματα το `FOUNDRY_PROJECT_ENDPOINT`.

**4. Εκθέστε έναν agent LangGraph πάνω στο πρωτόκολλο Responses:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # Το ChatOpenAI εδώ στοχεύει στο συμβατό με το OpenAI σημείο τερματισμού (Απαντήσεις) του έργου Foundry.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

Τρέξτε το τοπικά με `python main.py`, στη συνέχεια στείλτε ένα αίτημα Responses στο `http://localhost:8088/responses`.

**Κύριες συμπεριφορές:**

- **Συνομιλίες**: Οι πελάτες συνεχίζουν μια συνομιλία περνώντας `previous_response_id` ή μια `conversation` ID. Αν ο γράφος σας είναι μεταγλωττισμένος με LangGraph checkpointer, το Foundry αντιστοιχεί την κατάσταση συνομιλίας στο checkpoint (χρησιμοποιήστε έναν ανθεκτικό checkpointer στην παραγωγή, το `MemorySaver` είναι επαρκές για τοπικές δοκιμές).
- **Ανθρώπινη παρέμβαση**: Αν ο γράφος σας χρησιμοποιεί το LangGraph `interrupt()`, το `ResponsesHostServer` εμφανίζει το εκκρεμές interrupt ως ένα στοιχείο Responses `function_call` / `mcp_approval_request`, και οι πελάτες συνεχίζουν με ένα αντίστοιχο `function_call_output` / `mcp_approval_response`.
- **Ανάπτυξη στο Foundry**: Χρησιμοποιήστε το Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (τοπικά, απαιτεί Docker), στη συνέχεια `azd provision` και `azd deploy`. Η ανάπτυξη φιλοξενούμενου agent απαιτεί το ρόλο **Foundry Project Manager**.

Μια εκτελέσιμη έκδοση αυτού του παραδείγματος βρίσκεται στο [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Για πλήρη οδηγό (πρωτόκολλο Invocations, προσαρμοσμένα σχήματα αιτημάτων και αντιμετώπιση προβλημάτων), δείτε [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Παραδείγματα Κώδικα 

Παραδείγματα κώδικα για το Microsoft Agent Framework μπορείτε να βρείτε σε αυτό το αποθετήριο στα αρχεία `xx-python-agent-framework` και `xx-dotnet-agent-framework`.

## Έχετε Περισσότερες Ερωτήσεις για το Microsoft Agent Framework;

Εγγραφείτε στο [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) για να συναντήσετε άλλους εκπαιδευόμενους, να συμμετάσχετε σε ώρες γραφείου και να λάβετε απαντήσεις για τις ερωτήσεις σας σχετικά με τους AI Agents.
## Προηγούμενο Μάθημα

[Μνήμη για AI Agents](../13-agent-memory/README.md)

## Επόμενο Μάθημα

[Δημιουργία Agents Χρήσης Υπολογιστών (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->