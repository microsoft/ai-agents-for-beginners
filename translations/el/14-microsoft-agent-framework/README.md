# Εξερευνώντας το Microsoft Agent Framework

![Agent Framework](../../../translated_images/el/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Κατανόηση του Microsoft Agent Framework: Κύρια Χαρακτηριστικά και Αξία  
- Εξερεύνηση των Κύριων Εννοιών του Microsoft Agent Framework  
- Προχωρημένα Μοτίβα MAF: Ροές Εργασίας, Μεσαίο Λογισμικό και Μνήμη

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα ξέρετε πώς να:

- Δημιουργείτε Παραγωγικούς Έτοιμους AI Agents χρησιμοποιώντας το Microsoft Agent Framework  
- Εφαρμόζετε τα βασικά χαρακτηριστικά του Microsoft Agent Framework στις περιπτώσεις χρήσης σας με agents  
- Χρησιμοποιείτε προχωρημένα μοτίβα όπως ροές εργασίας, μεσαίο λογισμικό και παρατηρησιμότητα

## Παραδείγματα Κώδικα

Τα παραδείγματα κώδικα για το [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) βρίσκονται σε αυτό το αποθετήριο κάτω από τα αρχεία `xx-python-agent-framework` και `xx-dotnet-agent-framework`.

## Κατανόηση του Microsoft Agent Framework

![Framework Intro](../../../translated_images/el/framework-intro.077af16617cf130c.webp)

Το [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) είναι το ενοποιημένο πλαίσιο της Microsoft για τη δημιουργία AI agents. Παρέχει την ευελιξία να αντιμετωπίζει τη μεγάλη ποικιλία περιπτώσεων χρήσης με agents που συναντώνται σε παραγωγικά και ερευνητικά περιβάλλοντα, όπως:

- **Σειριακή Ορχήστρωση Agent** σε σενάρια όπου απαιτούνται ροές εργασίας βήμα-βήμα.  
- **Παράλληλη ορχήστρωση** σε σενάρια όπου οι agents πρέπει να ολοκληρώσουν εργασίες ταυτόχρονα.  
- **Ορχήστρωση συνομιλίας ομάδας** σε σενάρια όπου οι agents μπορούν να συνεργαστούν σε μία εργασία.  
- **Ορχήστρωση Παράδοσης** σε σενάρια όπου οι agents παραδίδουν την εργασία ο ένας στον άλλον καθώς ολοκληρώνονται οι υποεργασίες.  
- **Μαγνητική Ορχήστρωση** σε σενάρια όπου ένας διαχειριστής agent δημιουργεί και τροποποιεί μια λίστα εργασιών και χειρίζεται το συντονισμό των υποagents για την ολοκλήρωση της εργασίας.

Για την παροχή AI Agents σε Παραγωγή, το MAF περιλαμβάνει επίσης χαρακτηριστικά για:

- **Παρατηρησιμότητα** μέσω της χρήσης του OpenTelemetry όπου κάθε ενέργεια του AI Agent συμπεριλαμβανομένης της κλήσης εργαλείων, βημάτων ορχήστρωσης, ροών συλλογισμού και παρακολούθησης επιδόσεων γίνεται μέσω των πινάκων εργαλείων Microsoft Foundry.  
- **Ασφάλεια** με τη φιλοξενία των agents εγγενώς στο Microsoft Foundry που περιλαμβάνει ελέγχους ασφαλείας όπως πρόσβαση βάσει ρόλων, διαχείριση ιδιωτικών δεδομένων και ενσωματωμένη ασφάλεια περιεχομένου.  
- **Ανθεκτικότητα** καθώς τα νήματα agent και οι ροές εργασίας μπορούν να παύουν, να συνεχίζουν και να ανακάμπτουν από σφάλματα, επιτρέποντας μακρόχρονη εκτέλεση διεργασιών.  
- **Έλεγχος** καθώς υποστηρίζονται ροές εργασίας με ανθρώπινη παρέμβαση όπου οι εργασίες χαρακτηρίζονται ως απαιτούσες ανθρώπινη έγκριση.

Το Microsoft Agent Framework στοχεύει επίσης στην διαλειτουργικότητα μέσω:

- **Ανεξαρτησίας από το Νέφος** - Οι agents μπορούν να τρέχουν σε containers, on-premises και σε διάφορα νέφη.  
- **Ανεξαρτησίας από τον Πάροχο** - Οι agents μπορούν να δημιουργηθούν με το προτιμώμενο SDK σας, συμπεριλαμβανομένων των Azure OpenAI και OpenAI.  
- **Ενσωμάτωσης Ανοικτών Προτύπων** - Οι agents μπορούν να χρησιμοποιήσουν πρωτόκολλα όπως Agent-to-Agent (A2A) και Model Context Protocol (MCP) για να ανακαλύψουν και να χρησιμοποιήσουν άλλους agents και εργαλεία.  
- **Plugins και Connectors** - Μπορούν να γίνουν συνδέσεις σε υπηρεσίες δεδομένων και μνήμης όπως Microsoft Fabric, SharePoint, Pinecone και Qdrant.

Ας δούμε πώς αυτά τα χαρακτηριστικά εφαρμόζονται σε κάποιες από τις βασικές έννοιες του Microsoft Agent Framework.

## Κύριες Έννοιες του Microsoft Agent Framework

### Agents

![Agent Framework](../../../translated_images/el/agent-components.410a06daf87b4fef.webp)

**Δημιουργία Agents**

Η δημιουργία ενός agent γίνεται ορίζοντας την υπηρεσία συμπερασμού (Πάροχος LLM), ένα σύνολο οδηγιών που θα ακολουθεί ο AI Agent, και ένα ανατιθέμενο `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```
  
Το παραπάνω χρησιμοποιεί `Azure OpenAI` αλλά οι agents μπορούν να δημιουργηθούν χρησιμοποιώντας διάφορες υπηρεσίες, συμπεριλαμβανομένου του `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```
  
API OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```
  
```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```
  
ή απομακρυσμένοι agents χρησιμοποιώντας το πρωτόκολλο A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```
  
**Εκτέλεση Agents**

Οι agents εκτελούνται χρησιμοποιώντας τις μεθόδους `.run` ή `.run_stream` για μη-ροή ή ροή απαντήσεων αντίστοιχα.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```
  
```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```
  
Κάθε εκτέλεση agent μπορεί επίσης να έχει επιλογές να προσαρμόσει παραμέτρους όπως `max_tokens` που χρησιμοποιεί ο agent, `tools` που μπορεί να καλέσει ο agent, και ακόμη το ίδιο το `model` που εκτελείται από τον agent.

Αυτό είναι χρήσιμο σε περιπτώσεις όπου απαιτούνται συγκεκριμένα μοντέλα ή εργαλεία για την ολοκλήρωση της εργασίας του χρήστη.

**Εργαλεία**

Τα εργαλεία μπορούν να οριστούν τόσο κατά τον ορισμό του agent:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Όταν δημιουργείτε έναν ChatAgent απευθείας

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```
  
όσο και κατά την εκτέλεση του agent:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Εργαλείο παρέχεται μόνο για αυτήν την εκτέλεση )
```
  
**Νήματα Agent**

Τα Νήματα Agent χρησιμοποιούνται για την αντιμετώπιση συνομιλιών πολλαπλών γύρων. Τα νήματα μπορούν να δημιουργηθούν είτε με:

- Χρήση της `get_new_thread()` που επιτρέπει να αποθηκεύεται το νήμα με την πάροδο του χρόνου  
- Αυτόματη δημιουργία νήματος κατά την εκτέλεση agent και με το νήμα να διαρκεί μόνο κατά τη διάρκεια της τρέχουσας εκτέλεσης.

Ο κώδικας για τη δημιουργία νήματος έχει ως εξής:

```python
# Δημιουργήστε ένα νέο νήμα.
thread = agent.get_new_thread() # Εκτελέστε τον πράκτορα με το νήμα.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```
  
Έπειτα μπορείτε να σειριοποιήσετε το νήμα για να αποθηκευτεί για μελλοντική χρήση:

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
  
**Μεσαίο Λογισμικό Agent**

Οι agents αλληλεπιδρούν με εργαλεία και LLMs για να ολοκληρώσουν εργασίες του χρήστη. Σε ορισμένα σενάρια, θέλουμε να εκτελέσουμε ή να παρακολουθήσουμε ενέργειες μεταξύ αυτών των αλληλεπιδράσεων. Το μεσαίο λογισμικό agent μας επιτρέπει να το κάνουμε αυτό μέσω:

*Μεσαίο Λογισμικό Συναρτήσεων*

Αυτό το μεσαίο λογισμικό μας επιτρέπει να εκτελούμε μια ενέργεια μεταξύ του agent και μιας συνάρτησης ή εργαλείου που θα καλέσει. Παράδειγμα χρήσης είναι η καταγραφή κλήσεων στη συνάρτηση.

Στον παρακάτω κώδικα το `next` καθορίζει αν πρέπει να κληθεί το επόμενο μεσαίο λογισμικό ή η ίδια η συνάρτηση.

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
  
*Μεσαίο Λογισμικό Συνομιλίας*

Αυτό το μεσαίο λογισμικό επιτρέπει να εκτελείται ή να καταγράφεται μια ενέργεια μεταξύ του agent και των αιτημάτων προς το LLM.

Περιέχει σημαντικές πληροφορίες όπως τα `messages` που αποστέλλονται στην AI υπηρεσία.

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

Όπως καλύφθηκε στο μάθημα `Agentic Memory`, η μνήμη είναι ένα σημαντικό στοιχείο που επιτρέπει στον agent να λειτουργεί σε διάφορα πλαίσια. Το MAF προσφέρει διάφορους τύπους μνήμης:

*Μνήμη στην Εφαρμογή (In-Memory Storage)*

Αυτή είναι η μνήμη που αποθηκεύεται σε νήματα κατά την εκτέλεση της εφαρμογής.

```python
# Δημιουργήστε ένα νέο νήμα.
thread = agent.get_new_thread() # Εκτελέστε τον πράκτορα με το νήμα.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```
  
*Επίμονα Μηνύματα*

Αυτή η μνήμη χρησιμοποιείται για την αποθήκευση ιστορικού συνομιλιών ανάμεσα σε διαφορετικές συνεδρίες. Ορίζεται χρησιμοποιώντας το `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Δημιουργήστε μια προσαρμοσμένη αποθήκη μηνυμάτων
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```
  
*Δυναμική Μνήμη*

Αυτή η μνήμη προστίθεται στο πλαίσιο πριν εκτελεστούν οι agents. Μπορεί να αποθηκευτεί σε εξωτερικές υπηρεσίες όπως το mem0:

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

Η παρατηρησιμότητα είναι σημαντική για την κατασκευή αξιόπιστων και διαχειρίσιμων agentic συστημάτων. Το MAF ενσωματώνεται με το OpenTelemetry για την παροχή ιχνηλασίας και μετρητών για καλύτερη παρατηρησιμότητα.

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
  
### Ροές Εργασίας

Το MAF προσφέρει ροές εργασίας που είναι προ-ορισμένα βήματα για την ολοκλήρωση μιας εργασίας και περιλαμβάνουν AI agents ως στοιχεία αυτών των βημάτων.

Οι ροές εργασίας αποτελούνται από διάφορα στοιχεία που επιτρέπουν καλύτερο έλεγχο της ροής. Επίσης επιτρέπουν **πολλαπλή ορχήστρωση agents** και **σημείωση ελέγχου (checkpointing)** για την αποθήκευση καταστάσεων ροής εργασίας.

Τα βασικά στοιχεία μιας ροής εργασίας είναι:

**Εκτελεστές**

Οι εκτελεστές λαμβάνουν εισερχόμενα μηνύματα, εκτελούν τις ανατιθέμενες εργασίες τους και παράγουν ένα εξερχόμενο μήνυμα. Αυτό προωθεί τη ροή εργασίας προς την ολοκλήρωση του μεγαλύτερου έργου. Οι εκτελεστές μπορεί να είναι είτε AI agents είτε προσαρμοσμένη λογική.

**Ακμές**

Οι ακμές χρησιμοποιούνται για να ορίσουν τη ροή μηνυμάτων σε μια ροή εργασίας. Αυτές μπορεί να είναι:

*Άμεσες Ακμές* - Απλές συνδέσεις ένα προς ένα μεταξύ εκτελεστών:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```
  
*Υπό όρους Ακμές* - Ενεργοποιούνται μετά την πλήρωση μιας συγκεκριμένης συνθήκης. Για παράδειγμα, όταν τα δωμάτια ξενοδοχείου δεν είναι διαθέσιμα, ένας εκτελεστής μπορεί να προτείνει άλλες επιλογές.

*Ακμές Διακόπτη-περίπτωσης* - Δρομολογούν μηνύματα σε διαφορετικούς εκτελεστές βάσει ορισμένων συνθηκών. Για παράδειγμα, αν ένας πελάτης ταξιδιού έχει προτεραιότητα πρόσβασης και οι εργασίες του θα χειριστούν μέσω άλλης ροής εργασίας.

*Ακμές πολυδιάσπασης (Fan-out)* - Αποστέλλουν ένα μήνυμα σε πολλαπλούς προορισμούς.

*Ακμές συγχώνευσης (Fan-in)* - Συλλέγουν πολλαπλά μηνύματα από διαφορετικούς εκτελεστές και τα στέλνουν σε έναν προορισμό.

**Γεγονότα**

Για βελτιωμένη παρατηρησιμότητα στη ροή εργασίας, το MAF προσφέρει ενσωματωμένα γεγονότα εκτέλεσης που περιλαμβάνουν:

- `WorkflowStartedEvent`  - Ξεκινά η εκτέλεση ροής εργασίας  
- `WorkflowOutputEvent` - Η ροή εργασίας παράγει έξοδο  
- `WorkflowErrorEvent` - Η ροή εργασίας αντιμετωπίζει σφάλμα  
- `ExecutorInvokeEvent`  - Ο εκτελεστής ξεκινά επεξεργασία  
- `ExecutorCompleteEvent`  -  Ο εκτελεστής ολοκληρώνει επεξεργασία  
- `RequestInfoEvent` - Εκδίδεται ένα αίτημα

## Προχωρημένα Μοτίβα MAF

Τα παραπάνω τμήματα καλύπτουν τις βασικές έννοιες του Microsoft Agent Framework. Καθώς δημιουργείτε πιο σύνθετους agents, εδώ είναι μερικά προχωρημένα μοτίβα προς εξέταση:

- **Σύνθεση Μεσαίου Λογισμικού**: Αλυσίδωση πολλών χειριστών μεσαίου λογισμικού (καταγραφή, αυθεντικοποίηση, περιορισμός ρυθμού) χρησιμοποιώντας λειτουργίες και μεσαίο λογισμικό συνομιλίας για λεπτομερή έλεγχο της συμπεριφοράς agent.  
- **Checkpointing Ροής Εργασίας**: Χρησιμοποιήστε τα γεγονότα ροής εργασίας και σειριοποίηση για αποθήκευση και συνέχιση μακροχρόνιων διεργασιών agent.  
- **Δυναμική Επιλογή Εργαλείων**: Συνδυάστε RAG πάνω σε περιγραφές εργαλείων με την εγγραφή εργαλείων του MAF για να παρουσιάζετε μόνο τα σχετικά εργαλεία ανά ερώτημα.  
- **Πολυ-agent Παράδοση**: Χρησιμοποιήστε τις ακμές ροής εργασίας και τη δρομολόγηση υπό όρους για ορχήστρωση παραδόσεων μεταξύ εξειδικευμένων agents.

## Παραδείγματα Κώδικα

Παραδείγματα κώδικα για το Microsoft Agent Framework βρίσκονται σε αυτό το αποθετήριο κάτω από τα αρχεία `xx-python-agent-framework` και `xx-dotnet-agent-framework`.

## Έχετε Περισσότερες Ερωτήσεις για το Microsoft Agent Framework;

Ενταχθείτε στο [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) για να συναντήσετε άλλους μαθητευόμενους, να παρακολουθήσετε ώρες γραφείου και να λάβετε απαντήσεις στις ερωτήσεις σας για AI Agents.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται η επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε καμία ευθύνη για τυχόν παρανοήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->