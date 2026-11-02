# Εξερεύνηση του Microsoft Agent Framework

![Agent Framework](../../../translated_images/el/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Κατανόηση του Microsoft Agent Framework: Βασικά Χαρακτηριστικά και Αξία  
- Εξερεύνηση των βασικών εννοιών του Microsoft Agent Framework
- Προηγμένα MAF μοτίβα: Ροές εργασιών, Middleware και Μνήμη

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα γνωρίζετε πώς να:

- Δημιουργείτε παραγωγικούς AI Agents χρησιμοποιώντας το Microsoft Agent Framework
- Εφαρμόζετε τα βασικά χαρακτηριστικά του Microsoft Agent Framework στις χρήσεις των πρακτικών περιπτώσεων Agents
- Χρησιμοποιείτε προηγμένα μοτίβα όπως ροές εργασιών, middleware, και παρατηρησιμότητα

## Παραδείγματα Κώδικα 

Παραδείγματα κώδικα για το [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) μπορείτε να βρείτε σε αυτό το αποθετήριο κάτω από τα αρχεία `xx-python-agent-framework` και `xx-dotnet-agent-framework`.

## Κατανόηση του Microsoft Agent Framework

![Framework Intro](../../../translated_images/el/framework-intro.077af16617cf130c.webp)

Το [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) είναι το ενοποιημένο πλαίσιο της Microsoft για τη δημιουργία AI agents. Προσφέρει την ευελιξία να καλύψει τη μεγάλη ποικιλία πρακτικών περιπτώσεων χρήσης agents που παρατηρούνται σε περιβάλλοντα παραγωγής και έρευνας, όπως:

- **Διαδοχικός συντονισμός Agents** σε σενάρια που χρειάζονται ροές εργασιών βήμα-βήμα.
- **Ταυτόχρονος συντονισμός** σε σενάρια όπου οι agents πρέπει να ολοκληρώσουν εργασίες ταυτόχρονα.
- **Συντονισμός ομαδικής συνομιλίας** σε σενάρια όπου οι agents μπορούν να συνεργαστούν σε μία εργασία.
- **Συντονισμός μεταβίβασης** σε σενάρια όπου οι agents παραδίδουν την εργασία ο ένας στον άλλον καθώς ολοκληρώνονται τα υποκαθήκοντα.
- **Μαγνητικός συντονισμός** σε σενάρια όπου ένας διαχειριστής agent δημιουργεί και τροποποιεί λίστα εργασιών και χειρίζεται το συντονισμό των υποagents για την ολοκλήρωση της εργασίας.

Για την παράδοση AI Agents σε παραγωγή, το MAF περιλαμβάνει επίσης χαρακτηριστικά για:

- **Παρατηρησιμότητα** μέσω της χρήσης του OpenTelemetry όπου κάθε ενέργεια του AI Agent, συμπεριλαμβανομένης της κλήσης εργαλείων, των βημάτων συντονισμού, των ροών σκέψης και της παρακολούθησης απόδοσης μέσω των ταμπλό του Microsoft Foundry.
- **Ασφάλεια** με τη φιλοξενία agents εγγενώς στο Microsoft Foundry που περιλαμβάνει ελέγχους ασφαλείας όπως πρόσβαση βασισμένη σε ρόλους, διαχείριση ιδιωτικών δεδομένων και ενσωματωμένη ασφάλεια περιεχομένου.
- **Αντοχή** καθώς τα νήματα agents και οι ροές εργασιών μπορούν να σταματούν, να συνεχίζουν και να ανακτούνται από σφάλματα, επιτρέποντας μεγαλύτερης διάρκειας διαδικασίες.
- **Έλεγχος** καθώς υποστηρίζονται ροές εργασιών που περιλαμβάνουν ανθρώπινη παρέμβαση όπου οι εργασίες σημειώνονται ως απαιτούμενες ανθρώπινη έγκριση.

Το Microsoft Agent Framework εστιάζει επίσης στο να είναι διαλειτουργικό με:

- **Ανεξαρτησία από το cloud** - Οι agents μπορούν να τρέξουν σε containers, στο τοπικό περιβάλλον και σε πολλά διαφορετικά cloud.
- **Ανεξαρτησία από παρόχους** - Οι agents μπορούν να δημιουργηθούν μέσω του προτιμώμενου SDK σας, συμπεριλαμβανομένων Azure OpenAI και OpenAI
- **Ενσωμάτωση Ανοικτών Προτύπων** - Οι agents μπορούν να χρησιμοποιούν πρωτόκολλα όπως Agent-to-Agent(A2A) και Model Context Protocol (MCP) για να ανακαλύπτουν και να χρησιμοποιούν άλλους agents και εργαλεία.
- **Plugins και Συνδέσμοι** - Υπάρχουν σύνδεσμοι με υπηρεσίες δεδομένων και μνήμης όπως Microsoft Fabric, SharePoint, Pinecone και Qdrant.

Ας δούμε πώς αυτά τα χαρακτηριστικά εφαρμόζονται σε μερικές από τις βασικές έννοιες του Microsoft Agent Framework.

## Βασικές Έννοιες του Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/el/agent-components.410a06daf87b4fef.webp)

**Δημιουργία Agents**

Η δημιουργία agent γίνεται ορίζοντας την υπηρεσία συμπερασμού (Πάροχος LLM), ένα
σύνολο οδηγιών για τον AI Agent να ακολουθήσει, και ένα ανατεθειμένο `όνομα`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Το παραπάνω χρησιμοποιεί `Azure OpenAI` αλλά οι agents μπορούν να δημιουργηθούν χρησιμοποιώντας διάφορες υπηρεσίες, συμπεριλαμβανομένου του `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` APIs

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ή [MiniMax](https://platform.minimaxi.com/), που παρέχει API συμβατό με OpenAI με μεγάλα παράθυρα context (έως 204K tokens):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

ή απομακρυσμένους agents χρησιμοποιώντας το πρωτόκολλο A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Εκτέλεση Agents**

Οι agents εκτελούνται χρησιμοποιώντας τις μεθόδους `.run` ή `.run_stream` για είτε μη ροή απάντησης είτε ροή.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Κάθε εκτέλεση agent μπορεί επίσης να έχει επιλογές για να προσαρμόσει παραμέτρους όπως `max_tokens` που χρησιμοποιεί ο agent, `εργαλεία` που ο agent μπορεί να καλέσει, και ακόμη και το `μοντέλο` που χρησιμοποιείται για τον agent.

Αυτό είναι χρήσιμο σε περιπτώσεις όπου απαιτούνται συγκεκριμένα μοντέλα ή εργαλεία για την ολοκλήρωση της εργασίας χρήστη.

**Εργαλεία**

Τα εργαλεία μπορούν να οριστούν τόσο κατά τον ορισμό του agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Όταν δημιουργείτε έναν ChatAgent απευθείας

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

και επίσης κατά την εκτέλεση του agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Εργαλείο που παρέχεται μόνο για αυτήν την εκτέλεση )
```

**Νήματα Agent**

Τα Νήματα Agent χρησιμοποιούνται για τη διαχείριση συνομιλιών πολλαπλών γύρων. Τα νήματα μπορούν να δημιουργηθούν είτε:

- Χρησιμοποιώντας `get_new_thread()` που επιτρέπει στο νήμα να αποθηκευτεί με το χρόνο
- Δημιουργώντας αυτόματα ένα νήμα όταν εκτελείται ένας agent και το νήμα να διαρκεί μόνο κατά την τρέχουσα εκτέλεση.

Για να δημιουργήσετε ένα νήμα, ο κώδικας είναι ως εξής:

```python
# Δημιουργήστε ένα νέο νήμα.
thread = agent.get_new_thread() # Εκτελέστε τον πράκτορα με το νήμα.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Μπορείτε στη συνέχεια να σειριοποιήσετε το νήμα για να αποθηκευτεί για μελλοντική χρήση:

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

**Middleware Agent**

Οι agents αλληλεπιδρούν με εργαλεία και LLMs για να ολοκληρώσουν εργασίες χρηστών. Σε ορισμένα σενάρια, θέλουμε να εκτελέσουμε ή να παρακολουθήσουμε ενδιάμεσες αλληλεπιδράσεις. Το middleware των agents μας επιτρέπει να το κάνουμε αυτό μέσω:

*Middleware Συνάρτησης*

Αυτό το middleware μας επιτρέπει να εκτελέσουμε μια ενέργεια μεταξύ του agent και μιας συνάρτησης/εργαλείου που θα καλέσει. Ένα παράδειγμα χρήσης είναι όταν θέλουμε να κάνουμε καταγραφή κατά την κλήση της συνάρτησης.

Στον παρακάτω κώδικα, το `next` ορίζει αν το επόμενο middleware ή η πραγματική συνάρτηση πρέπει να καλεστεί.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Προεπεξεργασία: Καταγραφή πριν από την εκτέλεση της συνάρτησης
    print(f"[Function] Calling {context.function.name}")

    # Συνέχεια στον επόμενο ενδιάμεσο ή εκτέλεση της συνάρτησης
    await next(context)

    # Μετα-επεξεργασία: Καταγραφή μετά την εκτέλεση της συνάρτησης
    print(f"[Function] {context.function.name} completed")
```

*Middleware Συνομιλίας*

Αυτό το middleware μας επιτρέπει να εκτελέσουμε ή να καταγράψουμε μια ενέργεια μεταξύ του agent και των αιτημάτων προς το LLM.

Περιέχει σημαντικές πληροφορίες όπως τα `μήνυματα` που αποστέλλονται στην υπηρεσία AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Προεπεξεργασία: Καταγραφή πριν την κλήση AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Συνεχίστε στο επόμενο middleware ή υπηρεσία AI
    await next(context)

    # Μεταεπεξεργασία: Καταγραφή μετά την απόκριση AI
    print("[Chat] AI response received")

```

**Μνήμη Agent**

Όπως καλύφθηκε στο μάθημα `Agentic Memory`, η μνήμη είναι σημαντικό στοιχείο για να λειτουργεί ο agent σε διαφορετικά συμφραζόμενα. Το MAF προσφέρει διάφορους τύπους μνημών:

*Μνήμη Εντός Μνήμης*

Αυτή είναι η μνήμη που αποθηκεύεται στα νήματα κατά τη διάρκεια της εκτέλεσης της εφαρμογής.

```python
# Δημιουργήστε ένα νέο νήμα.
thread = agent.get_new_thread() # Εκτελέστε τον πράκτορα με το νήμα.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Επίμονες Μηνύματα*

Αυτή η μνήμη χρησιμοποιείται για τη διατήρηση ιστορικού συνομιλιών μεταξύ διαφορετικών συνεδριών. Ορίζεται με τη χρήση του `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Δημιουργήστε ένα προσαρμοσμένο κατάστημα μηνυμάτων
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Δυναμική Μνήμη*

Αυτή η μνήμη προστίθεται στο συμφραζόμενο πριν από την εκτέλεση των agents. Μπορεί να αποθηκεύεται σε εξωτερικές υπηρεσίες όπως το mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Χρήση του Mem0 για προηγμένες δυνατότητες μνήμης
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

Η παρατηρησιμότητα είναι σημαντική για την κατασκευή αξιόπιστων και συντηρήσιμων συστημάτων agent. Το MAF ενσωματώνεται με το OpenTelemetry για να παρέχει ιχνηλάτηση και μετρητές για καλύτερη παρατηρησιμότητα.

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

### Ροές Εργασιών

Το MAF προσφέρει ροές εργασιών που είναι προκαθορισμένα βήματα για την ολοκλήρωση μιας εργασίας και περιλαμβάνουν AI agents ως συνιστώσες σε αυτά τα βήματα.

Οι ροές εργασιών αποτελούνται από διάφορα στοιχεία που επιτρέπουν καλύτερο έλεγχο ροής. Επιτρέπουν επίσης **πολυ-agent συντονισμό** και **αποθηκεύσεις σημείων ελέγχου** για την αποθήκευση καταστάσεων ροών εργασιών.

Τα βασικά στοιχεία μιας ροής εργασιών είναι:

**Εκτελεστές**

Οι εκτελεστές λαμβάνουν εισερχόμενα μηνύματα, εκτελούν τις ανατεθειμένες εργασίες τους και παράγουν ένα εξερχόμενο μήνυμα. Αυτό μετακινεί τη ροή εργασίας προχωρώντας προς την ολοκλήρωση της μεγαλύτερης εργασίας. Οι εκτελεστές μπορεί να είναι είτε AI agents είτε προσαρμοσμένη λογική.

**Ακμές**

Οι ακμές χρησιμοποιούνται για τον ορισμό της ροής των μηνυμάτων σε μια ροή εργασίας. Αυτές μπορούν να είναι:

*Άμεσες Ακμές* - Απλές συνδέσεις ένα προς ένα μεταξύ εκτελεστών:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Υπό όρους Ακμές* - Ενεργοποιούνται αφού ικανοποιηθεί κάποια συνθήκη. Για παράδειγμα, όταν τα δωμάτια ξενοδοχείων δεν είναι διαθέσιμα, ένας εκτελεστής μπορεί να προτείνει άλλες επιλογές.

*Ακμές διακοπής περιπτώσεων* - Δρομολογούν μηνύματα σε διαφορετικούς εκτελεστές με βάση ορισμένες συνθήκες. Για παράδειγμα, αν ένας πελάτης ταξιδιών έχει προτεραιότητα πρόσβασης, οι εργασίες του θα αντιμετωπιστούν μέσω άλλης ροής εργασίας.

*Ακμές εκπομπής* - Στέλνουν ένα μήνυμα σε πολλαπλούς στόχους.

*Ακμές συλλογής* - Συγκεντρώνουν πολλαπλά μηνύματα από διαφορετικούς εκτελεστές και τα στέλνουν σε έναν στόχο.

**Γεγονότα**

Για να παρέχει καλύτερη παρατηρησιμότητα στις ροές εργασιών, το MAF προσφέρει ενσωματωμένα γεγονότα για την εκτέλεση, όπως:

- `WorkflowStartedEvent`  - Έναρξη εκτέλεσης ροής εργασίας
- `WorkflowOutputEvent` - Η ροή εργασίας παράγει ένα αποτέλεσμα
- `WorkflowErrorEvent` - Η ροή εργασίας αντιμετωπίζει ένα σφάλμα
- `ExecutorInvokeEvent`  - Ο εκτελεστής ξεκινά την επεξεργασία
- `ExecutorCompleteEvent`  -  Ο εκτελεστής ολοκληρώνει την επεξεργασία
- `RequestInfoEvent` - Εκδίδεται ένα αίτημα

## Προηγμένα Μοτίβα MAF

Οι παραπάνω ενότητες καλύπτουν τις βασικές έννοιες του Microsoft Agent Framework. Καθώς δημιουργείτε πιο πολύπλοκους agents, εδώ είναι μερικά προηγμένα μοτίβα που πρέπει να λάβετε υπόψη:

- **Σύνθεση Middleware**: Αλυσίδα πολλαπλών χειριστών middleware (καταγραφή, εξουσιοδότηση, περιορισμός ρυθμού) χρησιμοποιώντας middleware συνάρτησης και συνομιλίας για λεπτομερή έλεγχο της συμπεριφοράς του agent.
- **Αποθήκευση σημείων ελέγχου ροής εργασίας**: Χρησιμοποιήστε γεγονότα ροής εργασιών και σειριοποίηση για την αποθήκευση και επανεκκίνηση μακροχρόνιων διεργασιών agent.
- **Δυναμική Επιλογή Εργαλείου**: Συνδυάστε RAG πάνω σε περιγραφές εργαλείων με την καταχώρηση εργαλείων του MAF για να παρουσιάσετε μόνο σχετικά εργαλεία ανά ερώτημα.
- **Μεταβίβαση μεταξύ πολλαπλών agents**: Χρησιμοποιήστε ακμές ροής εργασίας και διαδρομή υπό όρους για να συντονίσετε μεταβιβάσεις μεταξύ εξειδικευμένων agents.

## Φιλοξενία LangChain / LangGraph Agents στο Microsoft Foundry

Το Microsoft Agent Framework είναι **διαλειτουργικό πλαίσιο** — δεν περιορίζεστε σε agents γραμμένους με MAF. Αν ήδη έχετε έναν agent κατασκευασμένο με **LangChain** ή **LangGraph**, μπορείτε να τον τρέξετε ως **agent φιλοξενούμενο από το Microsoft Foundry** ώστε το Foundry να διαχειρίζεται το runtime, τις συνεδρίες, την κλιμάκωση, την ταυτότητα και τα σημεία πρωτοκόλλου για εσάς, ενώ η λογική του agent σας παραμένει στο LangGraph.

Αυτό γίνεται με το πακέτο `langchain_azure_ai.agents.hosting`, που εκθέτει ένα συνταγμένο γράφο LangGraph πάνω στα ίδια πρωτόκολλα που χρησιμοποιούν οι agents φιλοξενούμενοι από Foundry.

**1. Εγκαταστήστε το hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Το `hosting` extra εγκαθιστά τις βιβλιοθήκες πρωτοκόλλου Foundry: `azure-ai-agentserver-responses` (το συμβατό με OpenAI endpoint `/responses`) και `azure-ai-agentserver-invocations` (το γενικό endpoint `/invocations`).

**2. Επιλέξτε ένα πρωτόκολλο φιλοξενίας:**

| Πρωτόκολλο | Κλάση Υποδοχής | Τελικό Σημείο | Χρήση |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Θέλετε συνομιλία συμβατή με OpenAI, μετάδοση, ιστορικό απαντήσεων και νηματοποίηση συνομιλιών — η συνιστώμενη προεπιλογή για συνομιλιακούς agents. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Χρειάζεστε προσαρμοσμένο σχήμα JSON, ένα webhook-style endpoint ή μη συνομιλιακή επεξεργασία. |

Επειδή το **Responses API είναι το κύριο API για ανάπτυξη στυλ agent στο Foundry**, ξεκινήστε με το `ResponsesHostServer` για τους περισσότερους agents.

**3. Ρυθμίστε μεταβλητές περιβάλλοντος** (`az login` πρώτα ώστε το `DefaultAzureCredential` να μπορεί να εγγραφεί):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Όταν ο agent τρέχει αργότερα ως φιλοξενούμενος agent στο Foundry, η πλατφόρμα εγχέει αυτόματα το `FOUNDRY_PROJECT_ENDPOINT`.

**4. Εκθέστε έναν LangGraph agent μέσω του πρωτοκόλλου Responses:**

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

    # Το ChatOpenAI εδώ στοχεύει στο συμβατό με OpenAI σημείο πρόσβασης (Responses) του έργου Foundry.
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

- **Συνομιλίες**: Οι πελάτες συνεχίζουν μια συνομιλία περνώντας το `previous_response_id` ή ένα ID `conversation`. Αν ο γράφος σας είναι συνταγμένος με έναν LangGraph checkpointer, το Foundry συνδέει την κατάσταση της συνομιλίας με το σημείο ελέγχου (χρησιμοποιήστε έναν ανθεκτικό checkpointer σε παραγωγή· το `MemorySaver` είναι καλό για τοπικές δοκιμές).
- **Ανθρώπινη παρέμβαση**: Αν ο γράφος σας χρησιμοποιεί το LangGraph `interrupt()`, το `ResponsesHostServer` προβάλλει την εκκρεμή διακοπή ως ένα στοιχείο Responses `function_call` / `mcp_approval_request`, και οι πελάτες συνεχίζουν με αντίστοιχη `function_call_output` / `mcp_approval_response`.
- **Ανάπτυξη στο Foundry**: Χρησιμοποιήστε το Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (τοπικό, απαιτεί Docker), μετά `azd provision` και `azd deploy`. Για ανάπτυξη φιλοξενούμενου agent απαιτείται ο ρόλος **Foundry Project Manager**.

Μια εκτελέσιμη έκδοση αυτού του παραδείγματος υπάρχει στο [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Για πλήρη αναλυτική παρουσίαση (πρωτόκολλο Invocations, προσαρμοσμένα σχήματα αιτημάτων και αντιμετώπιση προβλημάτων), δείτε [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Παραδείγματα Κώδικα 

Παραδείγματα κώδικα για το Microsoft Agent Framework μπορείτε να βρείτε σε αυτό το αποθετήριο κάτω από τα αρχεία `xx-python-agent-framework` και `xx-dotnet-agent-framework`.

## Έχετε Περισσότερες Ερωτήσεις για το Microsoft Agent Framework;

Ελάτε στο [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) για να συναντήσετε άλλους μαθητές, να παρακολουθήσετε ώρες γραφείου και να λύσετε τις ερωτήσεις σας για τους AI Agents.
## Προηγούμενο Μάθημα

[Μνήμη για AI Agents](../13-agent-memory/README.md)

## Επόμενο Μάθημα

[Δημιουργία Agents Χρήσης Υπολογιστών (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->