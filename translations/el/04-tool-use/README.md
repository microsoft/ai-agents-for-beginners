<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T17:31:13+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "el"
}
-->
[![Πώς να Σχεδιάσετε Καλούς Πράκτορες AI](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.el.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Κάντε κλικ στην εικόνα παραπάνω για να δείτε το βίντεο αυτού του μαθήματος)_

# Σχέδιο Χρήσης Εργαλείων

Τα εργαλεία είναι ενδιαφέροντα γιατί επιτρέπουν στους πράκτορες AI να έχουν ένα ευρύτερο φάσμα δυνατοτήτων. Αντί ο πράκτορας να έχει ένα περιορισμένο σύνολο ενεργειών που μπορεί να εκτελέσει, με την προσθήκη ενός εργαλείου, ο πράκτορας μπορεί τώρα να εκτελέσει μια μεγάλη ποικιλία ενεργειών. Σε αυτό το κεφάλαιο, θα εξετάσουμε το Σχέδιο Χρήσης Εργαλείων, το οποίο περιγράφει πώς οι πράκτορες AI μπορούν να χρησιμοποιούν συγκεκριμένα εργαλεία για να επιτύχουν τους στόχους τους.

## Εισαγωγή

Σε αυτό το μάθημα, θα προσπαθήσουμε να απαντήσουμε στις παρακάτω ερωτήσεις:

- Τι είναι το σχέδιο χρήσης εργαλείων;
- Σε ποιες περιπτώσεις χρήσης μπορεί να εφαρμοστεί;
- Ποια είναι τα στοιχεία/δομικά μέρη που χρειάζονται για την υλοποίηση του σχεδίου;
- Ποιες είναι οι ειδικές προϋποθέσεις για τη χρήση του Σχεδίου Χρήσης Εργαλείων για την κατασκευή αξιόπιστων πρακτόρων AI;

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα μπορείτε να:

- Ορίσετε το Σχέδιο Χρήσης Εργαλείων και τον σκοπό του.
- Αναγνωρίσετε περιπτώσεις χρήσης όπου το Σχέδιο Χρήσης Εργαλείων είναι εφαρμόσιμο.
- Κατανοήσετε τα βασικά στοιχεία που χρειάζονται για την υλοποίηση του σχεδίου.
- Αναγνωρίσετε τις προϋποθέσεις για την εξασφάλιση αξιοπιστίας στους πράκτορες AI που χρησιμοποιούν αυτό το σχέδιο.

## Τι είναι το Σχέδιο Χρήσης Εργαλείων;

Το **Σχέδιο Χρήσης Εργαλείων** επικεντρώνεται στο να δώσει στα LLMs τη δυνατότητα να αλληλεπιδρούν με εξωτερικά εργαλεία για να επιτύχουν συγκεκριμένους στόχους. Τα εργαλεία είναι κώδικας που μπορεί να εκτελεστεί από έναν πράκτορα για να πραγματοποιήσει ενέργειες. Ένα εργαλείο μπορεί να είναι μια απλή λειτουργία, όπως ένας υπολογιστής, ή μια κλήση API σε μια υπηρεσία τρίτου μέρους, όπως η αναζήτηση τιμών μετοχών ή η πρόβλεψη καιρού. Στο πλαίσιο των πρακτόρων AI, τα εργαλεία σχεδιάζονται για να εκτελούνται από πράκτορες ως απάντηση σε **κλήσεις λειτουργιών που δημιουργούνται από το μοντέλο**.

## Σε ποιες περιπτώσεις χρήσης μπορεί να εφαρμοστεί;

Οι πράκτορες AI μπορούν να αξιοποιήσουν εργαλεία για να ολοκληρώσουν σύνθετες εργασίες, να ανακτήσουν πληροφορίες ή να λάβουν αποφάσεις. Το σχέδιο χρήσης εργαλείων χρησιμοποιείται συχνά σε σενάρια που απαιτούν δυναμική αλληλεπίδραση με εξωτερικά συστήματα, όπως βάσεις δεδομένων, διαδικτυακές υπηρεσίες ή διερμηνείς κώδικα. Αυτή η δυνατότητα είναι χρήσιμη για διάφορες περιπτώσεις χρήσης, όπως:

- **Δυναμική Ανάκτηση Πληροφοριών:** Οι πράκτορες μπορούν να κάνουν ερωτήματα σε εξωτερικά APIs ή βάσεις δεδομένων για να ανακτήσουν ενημερωμένα δεδομένα (π.χ., ερωτήματα σε βάση δεδομένων SQLite για ανάλυση δεδομένων, αναζήτηση τιμών μετοχών ή πληροφοριών καιρού).
- **Εκτέλεση και Ερμηνεία Κώδικα:** Οι πράκτορες μπορούν να εκτελέσουν κώδικα ή σενάρια για να λύσουν μαθηματικά προβλήματα, να δημιουργήσουν αναφορές ή να πραγματοποιήσουν προσομοιώσεις.
- **Αυτοματοποίηση Ροής Εργασίας:** Αυτοματοποίηση επαναλαμβανόμενων ή πολυβηματικών ροών εργασίας μέσω της ενσωμάτωσης εργαλείων όπως προγραμματιστές εργασιών, υπηρεσίες email ή αγωγοί δεδομένων.
- **Υποστήριξη Πελατών:** Οι πράκτορες μπορούν να αλληλεπιδρούν με συστήματα CRM, πλατφόρμες εισιτηρίων ή βάσεις γνώσεων για να επιλύσουν ερωτήματα χρηστών.
- **Δημιουργία και Επεξεργασία Περιεχομένου:** Οι πράκτορες μπορούν να αξιοποιήσουν εργαλεία όπως ελεγκτές γραμματικής, συνοψιστές κειμένου ή αξιολογητές ασφάλειας περιεχομένου για να βοηθήσουν σε εργασίες δημιουργίας περιεχομένου.

## Ποια είναι τα στοιχεία/δομικά μέρη που χρειάζονται για την υλοποίηση του σχεδίου χρήσης εργαλείων;

Αυτά τα δομικά μέρη επιτρέπουν στον πράκτορα AI να εκτελεί ένα ευρύ φάσμα εργασιών. Ας δούμε τα βασικά στοιχεία που χρειάζονται για την υλοποίηση του Σχεδίου Χρήσης Εργαλείων:

- **Σχήματα Λειτουργιών/Εργαλείων**: Λεπτομερείς ορισμοί των διαθέσιμων εργαλείων, συμπεριλαμβανομένων του ονόματος της λειτουργίας, του σκοπού, των απαιτούμενων παραμέτρων και των αναμενόμενων αποτελεσμάτων. Αυτά τα σχήματα επιτρέπουν στο LLM να κατανοήσει ποια εργαλεία είναι διαθέσιμα και πώς να κατασκευάσει έγκυρα αιτήματα.

- **Λογική Εκτέλεσης Λειτουργιών**: Καθορίζει πώς και πότε καλούνται τα εργαλεία βάσει της πρόθεσης του χρήστη και του πλαισίου της συνομιλίας. Αυτό μπορεί να περιλαμβάνει μονάδες σχεδιασμού, μηχανισμούς δρομολόγησης ή ροές υπό όρους που καθορίζουν τη χρήση εργαλείων δυναμικά.

- **Σύστημα Διαχείρισης Μηνυμάτων**: Συστατικά που διαχειρίζονται τη ροή της συνομιλίας μεταξύ εισόδων χρήστη, απαντήσεων LLM, κλήσεων εργαλείων και εξόδων εργαλείων.

- **Πλαίσιο Ενσωμάτωσης Εργαλείων**: Υποδομή που συνδέει τον πράκτορα με διάφορα εργαλεία, είτε είναι απλές λειτουργίες είτε σύνθετες εξωτερικές υπηρεσίες.

- **Διαχείριση Σφαλμάτων & Επικύρωση**: Μηχανισμοί για τη διαχείριση αποτυχιών στην εκτέλεση εργαλείων, την επικύρωση παραμέτρων και τη διαχείριση απροσδόκητων απαντήσεων.

- **Διαχείριση Κατάστασης**: Παρακολουθεί το πλαίσιο της συνομιλίας, προηγούμενες αλληλεπιδράσεις εργαλείων και επίμονα δεδομένα για να εξασφαλίσει συνέπεια σε πολυγυρισμένες αλληλεπιδράσεις.

Στη συνέχεια, ας δούμε την Κλήση Λειτουργιών/Εργαλείων πιο αναλυτικά.

### Κλήση Λειτουργιών/Εργαλείων

Η κλήση λειτουργιών είναι ο κύριος τρόπος με τον οποίο επιτρέπουμε στα Μεγάλα Γλωσσικά Μοντέλα (LLMs) να αλληλεπιδρούν με εργαλεία. Συχνά θα δείτε τους όρους 'Λειτουργία' και 'Εργαλείο' να χρησιμοποιούνται εναλλακτικά, γιατί οι 'λειτουργίες' (μπλοκ επαναχρησιμοποιήσιμου κώδικα) είναι τα 'εργαλεία' που χρησιμοποιούν οι πράκτορες για να εκτελέσουν εργασίες. Για να εκτελεστεί ο κώδικας μιας λειτουργίας, ένα LLM πρέπει να συγκρίνει το αίτημα του χρήστη με την περιγραφή της λειτουργίας. Για να γίνει αυτό, ένα σχήμα που περιέχει τις περιγραφές όλων των διαθέσιμων λειτουργιών αποστέλλεται στο LLM. Το LLM στη συνέχεια επιλέγει την πιο κατάλληλη λειτουργία για την εργασία και επιστρέφει το όνομά της και τα επιχειρήματα. Η επιλεγμένη λειτουργία εκτελείται, η απάντησή της αποστέλλεται πίσω στο LLM, το οποίο χρησιμοποιεί τις πληροφορίες για να απαντήσει στο αίτημα του χρήστη.

Για να υλοποιήσουν οι προγραμματιστές την κλήση λειτουργιών για πράκτορες, θα χρειαστείτε:

1. Ένα μοντέλο LLM που υποστηρίζει την κλήση λειτουργιών
2. Ένα σχήμα που περιέχει περιγραφές λειτουργιών
3. Τον κώδικα για κάθε περιγραφόμενη λειτουργία

Ας χρησιμοποιήσουμε το παράδειγμα της λήψης της τρέχουσας ώρας σε μια πόλη για να το εικονογραφήσουμε:

1. **Αρχικοποίηση ενός LLM που υποστηρίζει την κλήση λειτουργιών:**

    Δεν υποστηρίζουν όλα τα μοντέλα την κλήση λειτουργιών, οπότε είναι σημαντικό να ελέγξετε ότι το LLM που χρησιμοποιείτε το κάνει.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> υποστηρίζει την κλήση λειτουργιών. Μπορούμε να ξεκινήσουμε με την αρχικοποίηση του πελάτη Azure OpenAI.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Δημιουργία Σχήματος Λειτουργίας**:

    Στη συνέχεια, θα ορίσουμε ένα σχήμα JSON που περιέχει το όνομα της λειτουργίας, την περιγραφή του τι κάνει η λειτουργία, και τα ονόματα και τις περιγραφές των παραμέτρων της λειτουργίας.
    Θα πάρουμε αυτό το σχήμα και θα το περάσουμε στον πελάτη που δημιουργήθηκε προηγουμένως, μαζί με το αίτημα του χρήστη να βρει την ώρα στο Σαν Φρανσίσκο. Αυτό που είναι σημαντικό να σημειωθεί είναι ότι επιστρέφεται μια **κλήση εργαλείου**, **όχι** η τελική απάντηση στην ερώτηση. Όπως αναφέρθηκε νωρίτερα, το LLM επιστρέφει το όνομα της λειτουργίας που επέλεξε για την εργασία και τα επιχειρήματα που θα περάσουν σε αυτήν.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Ο κώδικας της λειτουργίας που απαιτείται για την εκτέλεση της εργασίας:**

    Τώρα που το LLM έχει επιλέξει ποια λειτουργία πρέπει να εκτελεστεί, ο κώδικας που πραγματοποιεί την εργασία πρέπει να υλοποιηθεί και να εκτελεστεί.
    Μπορούμε να υλοποιήσουμε τον κώδικα για να πάρουμε την τρέχουσα ώρα σε Python. Θα χρειαστεί επίσης να γράψουμε τον κώδικα για να εξαγάγουμε το όνομα και τα επιχειρήματα από το response_message για να πάρουμε το τελικό αποτέλεσμα.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

Η Κλήση Λειτουργιών είναι η καρδιά του περισσότερου, αν όχι όλου, σχεδιασμού χρήσης εργαλείων από πράκτορες, ωστόσο η υλοποίησή της από την αρχή μπορεί μερικές φορές να είναι δύσκολη.
Όπως μάθαμε στο [Μάθημα 2](../../../02-explore-agentic-frameworks) τα πλαίσια πρακτόρων μας παρέχουν προκατασκευασμένα δομικά μέρη για την υλοποίηση της χρήσης εργαλείων.

## Παραδείγματα Χρήσης Εργαλείων με Πλαίσια Πρακτόρων

Ακολουθούν μερικά παραδείγματα για το πώς μπορείτε να υλοποιήσετε το Σχέδιο Χρήσης Εργαλείων χρησιμοποιώντας διαφορετικά πλαίσια πρακτόρων:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> είναι ένα ανοιχτού κώδικα AI πλαίσιο για προγραμματιστές .NET, Python και Java που εργάζονται με Μεγάλα Γλωσσικά Μοντέλα (LLMs). Απλοποιεί τη διαδικασία χρήσης κλήσης λειτουργιών περιγράφοντας αυτόματα τις λειτουργίες σας και τις παραμέτρους τους στο μοντέλο μέσω μιας διαδικασίας που ονομάζεται <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialization</a>. Διαχειρίζεται επίσης την επικοινωνία μεταξύ του μοντέλου και του κώδικα σας. Ένα άλλο πλεονέκτημα της χρήσης ενός πλαισίου πρακτόρων όπως το Semantic Kernel είναι ότι σας επιτρέπει να έχετε πρόσβαση σε προκατασκευασμένα εργαλεία όπως <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> και <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Το παρακάτω διάγραμμα απεικονίζει τη διαδικασία κλήσης λειτουργιών με το Semantic Kernel:

![function calling](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.el.png)

Στο Semantic Kernel οι λειτουργίες/εργαλεία ονομάζονται <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Μπορούμε να μετατρέψουμε τη λειτουργία `get_current_time` που είδαμε νωρίτερα σε plugin μετατρέποντάς την σε κλάση με τη λειτουργία μέσα σε αυτήν. Μπορούμε επίσης να εισάγουμε τον διακοσμητή `kernel_function`, ο οποίος λαμβάνει την περιγραφή της λειτουργίας. Όταν στη συνέχεια δημιουργείτε έναν πυρήνα με το GetCurrentTimePlugin, ο πυρήνας θα κάνει αυτόματα serialize τη λειτουργία και τις παραμέτρους της, δημιουργώντας το σχήμα για να το στείλει στο LLM στη διαδικασία.

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

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> είναι ένα νεότερο πλαίσιο πρακτόρων που έχει σχεδιαστεί για να δίνει τη δυνατότητα στους προγραμματιστές να δημιουργούν, να αναπτύσσουν και να κλιμακώνουν υψηλής ποιότητας και επεκτάσιμους πράκτορες AI με ασφάλεια, χωρίς να χρειάζεται να διαχειρίζονται τους υποκείμενους πόρους υπολογισμού και αποθήκευσης. Είναι ιδιαίτερα χρήσιμο για εφαρμογές επιχειρήσεων, καθώς είναι μια πλήρως διαχειριζόμενη υπηρεσία με ασφάλεια επιπέδου επιχείρησης.

Σε σύγκριση με την ανάπτυξη με το LLM API απευθείας, το Azure AI Agent Service παρέχει ορισμένα πλεονεκτήματα, όπως:

- Αυτόματη κλήση εργαλείων – δεν χρειάζεται να αναλύσετε μια κλήση εργαλείου, να καλέσετε το εργαλείο και να διαχειριστείτε την απάντηση· όλα αυτά γίνονται πλέον από την πλευρά του διακομιστή
- Διαχειριζόμενα δεδομένα με ασφάλεια – αντί να διαχειρίζεστε τη δική σας κατάσταση συνομιλίας, μπορείτε να βασιστείτε σε threads για να αποθηκεύσετε όλες τις πληροφορίες που χρειάζεστε
- Εργαλεία έτοιμα προς χρήση – Εργαλεία που μπορείτε να χρησιμοποιήσετε για να αλληλεπιδράσετε με τις πηγές δεδομένων σας, όπως Bing, Azure AI Search και Azure Functions.

Τα εργαλεία που είναι διαθέσιμα στο Azure AI Agent Service μπορούν να χωριστούν σε δύο κατηγορίες:

1. Εργαλεία Γνώσης:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding με Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Εργαλεία Δράσης:
    - <a href="https://learn.microsoft.com/
Η εκτέλεση της εφαρμογής σε ένα ασφαλές περιβάλλον ενισχύει περαιτέρω την προστασία. Σε επιχειρηματικά σενάρια, τα δεδομένα συνήθως εξάγονται και μετασχηματίζονται από λειτουργικά συστήματα σε μια βάση δεδομένων μόνο για ανάγνωση ή σε μια αποθήκη δεδομένων με ένα φιλικό προς τον χρήστη σχήμα. Αυτή η προσέγγιση διασφαλίζει ότι τα δεδομένα είναι ασφαλή, βελτιστοποιημένα για απόδοση και προσβασιμότητα, και ότι η εφαρμογή έχει περιορισμένη, μόνο για ανάγνωση πρόσβαση.

## Δείγματα Κώδικα

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Έχετε Περισσότερες Ερωτήσεις σχετικά με τα Σχέδια Χρήσης Εργαλείων;

Γίνετε μέλος στο [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) για να συναντήσετε άλλους μαθητές, να παρακολουθήσετε ώρες γραφείου και να λάβετε απαντήσεις στις ερωτήσεις σας σχετικά με τους AI Agents.

## Πρόσθετοι Πόροι

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Εργαστήριο Υπηρεσίας Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Εργαστήριο Multi-Agent Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Εκπαιδευτικό Σεμινάριο Κλήσης Λειτουργιών Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Ερμηνευτής Κώδικα Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Εργαλεία Autogen</a>

## Προηγούμενο Μάθημα

[Κατανόηση Σχεδίων Σχεδίασης Πρακτόρων](../03-agentic-design-patterns/README.md)

## Επόμενο Μάθημα

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->