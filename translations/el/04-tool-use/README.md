[![Πώς να Σχεδιάσετε Καλούς Πράκτορες Τεχνητής Νοημοσύνης](../../../translated_images/el/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Κάντε κλικ στην παραπάνω εικόνα για να δείτε το βίντεο αυτού του μαθήματος)_

# Σχεδιαστικό Πρότυπο Χρήσης Εργαλείων

Τα εργαλεία είναι ενδιαφέροντα γιατί επιτρέπουν σε πράκτορες τεχνητής νοημοσύνης να έχουν ευρύτερο φάσμα δυνατοτήτων. Αντί ο πράκτορας να έχει ένα περιορισμένο σύνολο ενεργειών που μπορεί να εκτελέσει, προσθέτοντας ένα εργαλείο, ο πράκτορας μπορεί πλέον να εκτελέσει ένα μεγάλο εύρος ενεργειών. Σε αυτό το κεφάλαιο, θα εξετάσουμε το Σχεδιαστικό Πρότυπο Χρήσης Εργαλείων, που περιγράφει πώς οι πράκτορες ΤΝ μπορούν να χρησιμοποιούν συγκεκριμένα εργαλεία για να επιτύχουν τους στόχους τους.

## Εισαγωγή

Σε αυτό το μάθημα, προσπαθούμε να απαντήσουμε στις ακόλουθες ερωτήσεις:

- Τι είναι το σχεδιαστικό πρότυπο χρήσης εργαλείων;
- Σε ποιες περιπτώσεις χρήσης μπορεί να εφαρμοστεί;
- Ποια είναι τα στοιχεία/οικοδομικά δομικά μπλοκ που χρειάζονται για την υλοποίηση του σχεδιαστικού προτύπου;
- Ποιοι είναι οι ειδικοί παράγοντες που πρέπει να ληφθούν υπόψη για τη χρήση του Σχεδιαστικού Προτύπου Χρήσης Εργαλείων ώστε να κατασκευαστούν αξιόπιστοι πράκτορες ΤΝ;

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα μπορείτε να:

- Ορίσετε το Σχεδιαστικό Πρότυπο Χρήσης Εργαλείων και τον σκοπό του.
- Αναγνωρίσετε τις περιπτώσεις χρήσης όπου το πρότυπο χρήσης εργαλείων είναι εφαρμόσιμο.
- Κατανοήσετε τα βασικά στοιχεία που απαιτούνται για την εφαρμογή του σχεδιαστικού προτύπου.
- Αναγνωρίσετε παράγοντες για τη διασφάλιση αξιοπιστίας σε πράκτορες ΤΝ που χρησιμοποιούν αυτό το σχεδιαστικό πρότυπο.

## Τι είναι το Σχεδιαστικό Πρότυπο Χρήσης Εργαλείων;

Το **Σχεδιαστικό Πρότυπο Χρήσης Εργαλείων** εστιάζει στο να δώσει στα Μεγάλα Μοντέλα Γλώσσας (LLMs) τη δυνατότητα να αλληλεπιδρούν με εξωτερικά εργαλεία για να πετύχουν συγκεκριμένους στόχους. Τα εργαλεία είναι κώδικας που μπορεί να εκτελεστεί από έναν πράκτορα για να αναλάβει ενέργειες. Ένα εργαλείο μπορεί να είναι μια απλή συνάρτηση όπως ένας αριθμομηχανής, ή μια κλήση API σε υπηρεσία τρίτου μέρους όπως αναζήτηση τιμών μετοχών ή πρόβλεψη καιρού. Στο πλαίσιο των πρακτόρων ΤΝ, τα εργαλεία σχεδιάζονται ώστε να εκτελούνται από τους πράκτορες ως απόκριση σε **συναρτησιακές κλήσεις που παράγονται από το μοντέλο**.

## Ποιες είναι οι περιπτώσεις χρήσης στις οποίες μπορεί να εφαρμοστεί;

Οι πράκτορες ΤΝ μπορούν να αξιοποιούν εργαλεία για να ολοκληρώσουν πολύπλοκες εργασίες, να ανακτήσουν πληροφορίες ή να λάβουν αποφάσεις. Το σχεδιαστικό πρότυπο χρήσης εργαλείων χρησιμοποιείται συχνά σε σενάρια που απαιτούν δυναμική αλληλεπίδραση με εξωτερικά συστήματα, όπως βάσεις δεδομένων, διαδικτυακές υπηρεσίες ή ερμηνευτές κώδικα. Αυτή η δυνατότητα είναι χρήσιμη σε πολλαπλές περιπτώσεις χρήσης, μεταξύ άλλων:

- **Δυναμική Ανάκτηση Πληροφοριών:** Οι πράκτορες μπορούν να κάνουν ερωτήματα σε εξωτερικά APIs ή βάσεις δεδομένων για να ανακτήσουν ενημερωμένα δεδομένα (π.χ., ερωτήματα σε βάση δεδομένων SQLite για ανάλυση δεδομένων, λήψη τιμών μετοχών ή πληροφοριών καιρού).
- **Εκτέλεση και Ερμηνεία Κώδικα:** Οι πράκτορες μπορούν να εκτελούν κώδικα ή σενάρια για την επίλυση μαθηματικών προβλημάτων, δημιουργία αναφορών ή εκτέλεση προσομοιώσεων.
- **Αυτοματοποίηση Ροής Εργασίας:** Αυτοματοποιώντας επαναλαμβανόμενες ή πολύ-βηματικές ροές εργασιών ενσωματώνοντας εργαλεία όπως προγραμματιστές εργασιών, υπηρεσίες email ή pipelines δεδομένων.
- **Υποστήριξη Πελατών:** Οι πράκτορες μπορούν να αλληλεπιδρούν με συστήματα CRM, πλατφόρμες διαχείρισης αιτημάτων ή βάσεις γνώσης για την επίλυση ερωτημάτων χρηστών.
- **Δημιουργία και Επεξεργασία Περιεχομένου:** Οι πράκτορες μπορούν να αξιοποιούν εργαλεία όπως ελεγκτές γραμματικής, συνοπτικές περιλήψεις κειμένων ή αξιολογητές ασφάλειας περιεχομένου για να βοηθήσουν με εργασίες δημιουργίας περιεχομένου.

## Ποια είναι τα στοιχεία/δομικά μπλοκ που απαιτούνται για την εφαρμογή του σχεδιαστικού προτύπου χρήσης εργαλείων;

Αυτά τα δομικά στοιχεία επιτρέπουν στον πράκτορα ΤΝ να εκτελεί ένα ευρύ φάσμα εργασιών. Ας δούμε τα βασικά στοιχεία που χρειάζονται για την υλοποίηση του Σχεδιαστικού Προτύπου Χρήσης Εργαλείων:

- **Σχήματα Συναρτήσεων/Εργαλείων:** Λεπτομερείς ορισμοί διαθέσιμων εργαλείων, συμπεριλαμβανομένου του ονόματος της συνάρτησης, του σκοπού, των απαιτούμενων παραμέτρων και των αναμενόμενων αποτελεσμάτων. Αυτά τα σχήματα επιτρέπουν στο LLM να κατανοήσει ποια εργαλεία είναι διαθέσιμα και πώς να δημιουργήσει έγκυρα αιτήματα.

- **Λογική Εκτέλεσης Συνάρτησης:** Καθορίζει πώς και πότε καλούνται τα εργαλεία, βάσει της πρόθεσης του χρήστη και του πλαισίου της συνομιλίας. Αυτό μπορεί να περιλαμβάνει μονάδες προγραμματισμού, μηχανισμούς δρομολόγησης ή ροές με συνθήκες που καθορίζουν δυναμικά τη χρήση εργαλείων.

- **Σύστημα Διαχείρισης Μηνυμάτων:** Στοιχεία που διαχειρίζονται τη ροή της συνομιλίας ανάμεσα στις εισόδους των χρηστών, τις απαντήσεις του LLM, τις κλήσεις εργαλείων και τα αποτελέσματα των εργαλείων.

- **Πλαίσιο Ενσωμάτωσης Εργαλείων:** Υποδομή που συνδέει τον πράκτορα με διάφορα εργαλεία, είτε πρόκειται για απλές συναρτήσεις είτε για πολύπλοκες εξωτερικές υπηρεσίες.

- **Διαχείριση Σφαλμάτων & Επικύρωσης:** Μηχανισμοί για την αντιμετώπιση αποτυχιών στην εκτέλεση εργαλείων, την επικύρωση παραμέτρων και τη διαχείριση μη αναμενόμενων αποκρίσεων.

- **Διαχείριση Κατάστασης:** Παρακολουθεί το πλαίσιο της συνομιλίας, τις προηγούμενες αλληλεπιδράσεις με εργαλεία και τα επίμονα δεδομένα για τη διασφάλιση συνοχής σε αλληλεπιδράσεις πολλαπλών βημάτων.

Ας εξετάσουμε στη συνέχεια τις Κλήσεις Συναρτήσεων/Εργαλείων με περισσότερες λεπτομέρειες.

### Κλήση Συναρτήσεων/Εργαλείων

Η κλήση συναρτήσεων είναι ο βασικός τρόπος που επιτρέπουμε στα Μεγάλα Μοντέλα Γλώσσας (LLMs) να αλληλεπιδρούν με εργαλεία. Συνηθίζεται να χρησιμοποιούνται εναλλακτικά οι όροι 'Συνάρτηση' και 'Εργαλείο', επειδή οι 'συναρτήσεις' (μπλοκ επαναχρησιμοποιήσιμου κώδικα) είναι τα 'εργαλεία' που χρησιμοποιούν οι πράκτορες για να εκτελέσουν εργασίες. Για να κληθεί ο κώδικας μιας συνάρτησης, το LLM πρέπει να συγκρίνει το αίτημα του χρήστη με την περιγραφή των συναρτήσεων. Γι' αυτό αποστέλλεται ένα σχήμα που περιέχει τις περιγραφές όλων των διαθέσιμων συναρτήσεων στο LLM. Το LLM επιλέγει μετά την πιο κατάλληλη συνάρτηση για την εργασία και επιστρέφει το όνομά της και τα επιχειρήματα. Η επιλεγμένη συνάρτηση καλείται, η απόκρισή της αποστέλλεται ξανά στο LLM, το οποίο χρησιμοποιεί τις πληροφορίες για να απαντήσει στο αίτημα του χρήστη.

Για να υλοποιήσουν οι προγραμματιστές την κλήση συναρτήσεων για πράκτορες, θα πρέπει να έχουν:

1. Ένα μοντέλο LLM που υποστηρίζει κλήσεις συναρτήσεων
2. Ένα σχήμα που περιέχει τις περιγραφές συναρτήσεων
3. Τον κώδικα για κάθε περιγραφόμενη συνάρτηση

Ας χρησιμοποιήσουμε το παράδειγμα της λήψης της τρέχουσας ώρας σε μια πόλη για να το απεικονίσουμε:

1. **Αρχικοποίηση ενός LLM που υποστηρίζει κλήσεις συναρτήσεων:**

    Δεν υποστηρίζουν όλα τα μοντέλα κλήσεις συναρτήσεων, οπότε είναι σημαντικό να ελέγξετε αν το μοντέλο που χρησιμοποιείτε έχει αυτήν τη δυνατότητα. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Το Azure OpenAI</a> υποστηρίζει κλήσεις συναρτήσεων. Μπορούμε να ξεκινήσουμε δημιουργώντας τον πελάτη Azure OpenAI.

    ```python
    # Αρχικοποίηση του πελάτη Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Δημιουργία Σχήματος Συνάρτησης:**

    Στη συνέχεια θα ορίσουμε ένα σχήμα JSON που περιέχει το όνομα της συνάρτησης, την περιγραφή του τι κάνει η συνάρτηση, και τα ονόματα και τις περιγραφές των παραμέτρων της συνάρτησης.
    Έπειτα θα περάσουμε αυτό το σχήμα στον πελάτη που δημιουργήσαμε νωρίτερα, μαζί με το αίτημα του χρήστη για την εύρεση της ώρας στο Σαν Φρανσίσκο. Το σημαντικό να σημειωθεί είναι ότι **η κλήση εργαλείου** είναι αυτό που επιστρέφεται, **όχι** η τελική απάντηση στην ερώτηση. Όπως αναφέρθηκε παραπάνω, το LLM επιστρέφει το όνομα της συνάρτησης που επέλεξε για την εργασία, και τα επιχειρήματα που θα της περαστούν.

    ```python
    # Περιγραφή λειτουργίας για το μοντέλο να διαβάσει
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Αρχικό μήνυμα χρήστη
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Πρώτη κλήση API: Ζητήστε από το μοντέλο να χρησιμοποιήσει τη λειτουργία
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Επεξεργασία της απάντησης του μοντέλου
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Ο κώδικας της συνάρτησης που απαιτείται για την εκτέλεση της εργασίας:**

    Τώρα που το LLM έχει επιλέξει ποια συνάρτηση πρέπει να εκτελεστεί, πρέπει να υλοποιηθεί και να εκτελεστεί ο κώδικας που αναλαμβάνει την εργασία.
    Μπορούμε να υλοποιήσουμε τον κώδικα για να πάρουμε την τρέχουσα ώρα σε Python. Θα χρειαστεί επίσης να γράψουμε κώδικα για να εξάγουμε το όνομα και τα επιχειρήματα από την response_message ώστε να πάρουμε το τελικό αποτέλεσμα.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Διαχείριση κλήσεων συναρτήσεων
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Δεύτερη κλήση API: Λάβετε την τελική απάντηση από το μοντέλο
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Η Κλήση Συνάρτησης είναι στον πυρήνα των περισσότερων, αν όχι όλων, σχεδιαστικών προτύπων χρήσης εργαλείων για πράκτορες, ωστόσο η υλοποίησή της από το μηδέν μπορεί μερικές φορές να είναι πρόκληση.
Όπως μάθαμε στο [Μάθημα 2](../../../02-explore-agentic-frameworks), τα agentic frameworks μας παρέχουν προ-κατασκευασμένα δομικά στοιχεία για την υλοποίηση της χρήσης εργαλείων.
 
## Παραδείγματα Χρήσης Εργαλείων με Agentic Frameworks

Εδώ είναι μερικά παραδείγματα για το πώς μπορείτε να υλοποιήσετε το Σχεδιαστικό Πρότυπο Χρήσης Εργαλείων χρησιμοποιώντας διαφορετικά agentic frameworks:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Το Semantic Kernel</a> είναι ένα ανοικτού κώδικα πλαίσιο ΤΝ για προγραμματιστές .NET, Python και Java που δουλεύουν με Μεγάλα Μοντέλα Γλώσσας (LLMs). Απλοποιεί τη διαδικασία χρήσης κλήσεων συναρτήσεων περιγράφοντας αυτόματα τις συναρτήσεις σας και τις παραμέτρους τους στο μοντέλο μέσω μιας διαδικασίας που ονομάζεται <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">σειριοποίηση</a>. Επίσης, διαχειρίζεται την αμφίδρομη επικοινωνία ανάμεσα στο μοντέλο και τον κώδικά σας. Ένα επιπλέον πλεονέκτημα της χρήσης ενός agentic framework όπως το Semantic Kernel, είναι ότι σας επιτρέπει να έχετε πρόσβαση σε προ-κατασκευασμένα εργαλεία όπως το <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Αναζήτηση Αρχείων</a> και τον <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Ερμηνευτή Κώδικα</a>.

Το ακόλουθο διάγραμμα απεικονίζει τη διαδικασία κλήσης συναρτήσεων με το Semantic Kernel:

![function calling](../../../translated_images/el/functioncalling-diagram.a84006fc287f6014.webp)

Στο Semantic Kernel, οι συναρτήσεις/εργαλεία ονομάζονται <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Μπορούμε να μετατρέψουμε τη συνάρτηση `get_current_time` που είδαμε προηγουμένως σε plugin κάνοντάς την κλάση που περιλαμβάνει τη συνάρτηση. Μπορούμε επίσης να εισάγουμε τον διακοσμητή `kernel_function`, ο οποίος λαμβάνει την περιγραφή της συνάρτησης. Όταν στη συνέχεια δημιουργείτε έναν kernel με το GetCurrentTimePlugin, ο kernel θα σειριοποιεί αυτόματα τη συνάρτηση και τις παραμέτρους της, δημιουργώντας το σχήμα που αποστέλλεται στο LLM στη διαδικασία.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Δημιουργήστε τον πυρήνα
kernel = Kernel()

# Δημιουργήστε το πρόσθετο
get_current_time_plugin = GetCurrentTimePlugin(location)

# Προσθέστε το πρόσθετο στον πυρήνα
kernel.add_plugin(get_current_time_plugin)
```
  
### Υπηρεσία Πράκτορα Azure AI

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Η Υπηρεσία Πράκτορα Azure AI</a> είναι ένα νεότερο agentic framework σχεδιασμένο να δίνει τη δυνατότητα στους προγραμματιστές να δημιουργούν, να αναπτύσσουν και να κλιμακώνουν ασφαλώς υψηλής ποιότητας, επεκτάσιμους πράκτορες ΤΝ χωρίς να χρειάζεται να διαχειρίζονται τους υποκείμενους πόρους υπολογισμού και αποθήκευσης. Είναι ιδιαίτερα χρήσιμη για επιχειρηματικές εφαρμογές καθώς είναι μια πλήρως διαχειριζόμενη υπηρεσία με ασφάλεια επιπέδου επιχείρησης.

Σε σύγκριση με την ανάπτυξη χρησιμοποιώντας απευθείας το API του LLM, η Υπηρεσία Πράκτορα Azure AI παρέχει κάποια πλεονεκτήματα, όπως:

- Αυτόματη κλήση εργαλείων – δεν χρειάζεται ο διαχωρισμός της κλήσης εργαλείου, η εκτέλεση του εργαλείου και η διαχείριση της απόκρισης· όλα αυτά γίνονται πλέον στην πλευρά του διακομιστή
- Ασφαλής διαχείριση δεδομένων – αντί να διαχειρίζεστε εσείς την κατάσταση της συνομιλίας, μπορείτε να στηριχθείτε σε "νήματα" (threads) για να αποθηκεύσετε όλες τις απαραίτητες πληροφορίες
- Έτοιμα προς χρήση εργαλεία – Εργαλεία που μπορείτε να χρησιμοποιήσετε για να αλληλεπιδράσετε με τις πηγές δεδομένων σας, όπως Bing, Azure AI Search και Azure Functions.

Τα εργαλεία που είναι διαθέσιμα στην Υπηρεσία Πράκτορα Azure AI μπορούν να χωριστούν σε δύο κατηγορίες:

1. Εργαλεία Γνώσης:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Υποστήριξη με Αναζήτηση Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Αναζήτηση Αρχείων</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Εργαλεία Δράσης:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Κλήση Συνάρτησης</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Ερμηνευτής Κώδικα</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Εργαλεία ορισμένα από OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Η Υπηρεσία Πράκτορα μας επιτρέπει να χρησιμοποιούμε αυτά τα εργαλεία μαζί ως `toolset`. Επίσης, χρησιμοποιεί `threads` που παρακολουθούν το ιστορικό των μηνυμάτων μιας συγκεκριμένης συνομιλίας.

Φανταστείτε ότι είστε πωλητής σε μια εταιρεία που ονομάζεται Contoso. Θέλετε να αναπτύξετε έναν συνομιλιακό πράκτορα που να μπορεί να απαντά σε ερωτήσεις σχετικά με τα δεδομένα πωλήσεών σας.

Η παρακάτω εικόνα απεικονίζει πώς θα μπορούσατε να χρησιμοποιήσετε την Υπηρεσία Πράκτορα Azure AI για να αναλύσετε τα δεδομένα πωλήσεών σας:

![Agentic Service In Action](../../../translated_images/el/agent-service-in-action.34fb465c9a84659e.webp)

Για να χρησιμοποιήσουμε οποιοδήποτε από αυτά τα εργαλεία με την υπηρεσία, μπορούμε να δημιουργήσουμε έναν πελάτη και να ορίσουμε ένα εργαλείο ή σύνολο εργαλείων. Για να το υλοποιήσουμε πρακτικά, μπορούμε να χρησιμοποιήσουμε τον παρακάτω κώδικα Python. Το LLM θα μπορεί να εξετάζει το toolset και να αποφασίζει αν θα χρησιμοποιήσει τη συνάρτηση που δημιούργησε ο χρήστης, `fetch_sales_data_using_sqlite_query`, ή τον προ-κατασκευασμένο Ερμηνευτή Κώδικα ανάλογα με το αίτημα του χρήστη.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # συνάρτηση fetch_sales_data_using_sqlite_query που μπορεί να βρεθεί σε ένα αρχείο fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Αρχικοποίηση σετ εργαλείων
toolset = ToolSet()

# Αρχικοποίηση πράκτορα κλήσης συνάρτησης με τη συνάρτηση fetch_sales_data_using_sqlite_query και προσθήκη στο σετ εργαλείων
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Αρχικοποίηση εργαλείου Ερμηνευτή Κώδικα και προσθήκη του στο σετ εργαλείων.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Ποιοι είναι οι ειδικοί παράγοντες που πρέπει να ληφθούν υπόψη για τη χρήση του Σχεδιαστικού Προτύπου Χρήσης Εργαλείων ώστε να κατασκευαστούν αξιόπιστοι πράκτορες ΤΝ;

Ένας κοινός προβληματισμός με το δυναμικά παραγόμενο SQL από τα LLM είναι η ασφάλεια, ιδίως ο κίνδυνος SQL injection ή κακόβουλων ενεργειών, όπως η διαγραφή ή αλλοίωση της βάσης δεδομένων. Παρόλο που αυτοί οι προβληματισμοί είναι βάσιμοι, μπορούν να αντιμετωπιστούν αποτελεσματικά με την κατάλληλη διαμόρφωση των δικαιωμάτων πρόσβασης στη βάση δεδομένων. Για τις περισσότερες βάσεις δεδομένων, αυτό συνεπάγεται τη ρύθμιση της βάσης σε mode μόνο για ανάγνωση. Για υπηρεσίες βάσεων δεδομένων όπως το PostgreSQL ή το Azure SQL, η εφαρμογή θα πρέπει να ανατίθεται σε ρόλο μόνο για ανάγνωση (SELECT).
Η εκτέλεση της εφαρμογής σε ένα ασφαλές περιβάλλον ενισχύει περαιτέρω την προστασία. Σε επιχειρηματικά σενάρια, τα δεδομένα συνήθως εξάγονται και μετασχηματίζονται από λειτουργικά συστήματα σε μια βάση δεδομένων ή αποθήκη δεδομένων μόνο για ανάγνωση με ένα φιλικό προς τον χρήστη σχήμα. Αυτή η προσέγγιση διασφαλίζει ότι τα δεδομένα είναι ασφαλή, βελτιστοποιημένα για απόδοση και προσβασιμότητα, και ότι η εφαρμογή έχει περιορισμένη πρόσβαση μόνο για ανάγνωση.

## Δείγματα Κωδίκων

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Έχετε Περισσότερες Ερωτήσεις σχετικά με το Σχεδιασμό των Εργαλείων Χρήσης;

Εγγραφείτε στο [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) για να συναντήσετε άλλους μαθητές, να παρακολουθήσετε ώρες υποστήριξης και να λάβετε απαντήσεις στις ερωτήσεις σας για τους Πράκτορες AI.

## Επιπλέον Πόροι

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Εργαστήριο Υπηρεσίας Πρακτόρων Azure AI</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Εργαστήριο Πολυπράκτορα Δημιουργικού Συγγραφέα Contoso</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Εκμάθηση Καλής Χρήσης Κλήσης Συνάρτησης του Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Διερμηνέας Κώδικα του Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Εργαλεία Autogen</a>

## Προηγούμενο Μάθημα

[Κατανόηση των Σχεδιαστικών Προτύπων Πρακτόρων](../03-agentic-design-patterns/README.md)

## Επόμενο Μάθημα

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Το παρόν έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μηχανικής μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις μπορεί να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στην αρχική του γλώσσα θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή παρανοήσεις που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->