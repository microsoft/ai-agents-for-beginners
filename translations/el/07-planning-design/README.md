[![Planning Design Pattern](../../../translated_images/el/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Κάντε κλικ στην παραπάνω εικόνα για να δείτε το βίντεο αυτής της ενότητας)_

# Σχεδιασμός Προγραμματισμού

## Εισαγωγή

Αυτή η ενότητα θα καλύψει

* Τον ορισμό ενός σαφούς συνολικού στόχου και το σπάσιμο μιας πολύπλοκης εργασίας σε διαχειρίσιμες εργασίες.
* Την αξιοποίηση δομημένης εξόδου για πιο αξιόπιστες και μηχανικά αναγνώσιμες απαντήσεις.
* Την εφαρμογή μιας προσέγγισης βασισμένης σε γεγονότα για την αντιμετώπιση δυναμικών εργασιών και απροσδόκητων εισόδων.

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτής της ενότητας, θα έχετε κατανόηση σχετικά με:

* Την αναγνώριση και τον καθορισμό ενός συνολικού στόχου για έναν AI πράκτορα, εξασφαλίζοντας ότι γνωρίζει σαφώς τι πρέπει να επιτευχθεί.
* Τη διάσπαση μιας πολύπλοκης εργασίας σε διαχειρίσιμα υπο-εργασίες και την οργάνωσή τους σε λογική ακολουθία.
* Το εξοπλισμό των πρακτόρων με τα κατάλληλα εργαλεία (π.χ., εργαλεία αναζήτησης ή εργαλεία ανάλυσης δεδομένων), το πότε και πώς χρησιμοποιούνται, και την αντιμετώπιση απροσδόκητων καταστάσεων που προκύπτουν.
* Την αξιολόγηση των αποτελεσμάτων των υπο-εργασιών, τη μέτρηση απόδοσης και την επανάληψη ενεργειών για τη βελτίωση της τελικής εξόδου.

## Ορισμός του Συνολικού Στόχου και Σπάσιμο μίας Εργασίας

![Defining Goals and Tasks](../../../translated_images/el/defining-goals-tasks.d70439e19e37c47a.webp)

Οι περισσότερες εργασίες στον πραγματικό κόσμο είναι πολύπλοκες για να αντιμετωπιστούν με ένα μόνο βήμα. Ένας AI πράκτορας χρειάζεται έναν σαφή και συνοπτικό στόχο για να καθοδηγεί τον σχεδιασμό και τις ενέργειές του. Για παράδειγμα, εξετάστε τον στόχο:

    "Δημιουργία προγράμματος ταξιδιού 3 ημερών."

Αν και είναι απλό να διατυπωθεί, χρειάζεται ακόμη βελτίωση. Όσο πιο σαφής είναι ο στόχος, τόσο καλύτερα μπορεί ο πράκτορας (και οποιοιδήποτε συνεργάτες) να εστιάσουν στην επίτευξη του σωστού αποτελέσματος, όπως η δημιουργία ενός ολοκληρωμένου πλάνου με επιλογές πτήσεων, προτάσεις ξενοδοχείων και προτάσεις δραστηριοτήτων.

### Διάσπαση της Εργασίας

Οι μεγάλες ή περίπλοκες εργασίες γίνονται πιο διαχειρίσιμες όταν χωρίζονται σε μικρότερους, προσανατολισμένους στόχους υπο-εργασίες.  
Στο παράδειγμα του προγράμματος ταξιδιού, μπορείτε να διασπάσετε τον στόχο σε:

* Κράτηση Πτήσεων  
* Κράτηση Ξενοδοχείου  
* Ενοικίαση Αυτοκινήτου  
* Εξατομίκευση

Κάθε υπο-εργασία μπορεί στη συνέχεια να αντιμετωπιστεί από αφιερωμένους πράκτορες ή διαδικασίες. Ένας πράκτορας μπορεί να ειδικεύεται στην αναζήτηση των καλύτερων προσφορών πτήσεων, άλλος επικεντρώνεται στις κρατήσεις ξενοδοχείων κ.ο.κ. Ένας συντονιστής ή “κατώτερος” πράκτορας μπορεί να συνθέσει αυτά τα αποτελέσματα σε ένα συνεκτικό πρόγραμμα για τον τελικό χρήστη.

Αυτή η μονάδα προσέγγισης επιτρέπει επίσης σταδιακές βελτιώσεις. Για παράδειγμα, μπορείτε να προσθέσετε εξειδικευμένους πράκτορες για Προτάσεις Φαγητού ή Τοπικές Δραστηριότητες και να βελτιώσετε το πρόγραμμα με την πάροδο του χρόνου.

### Δομημένη Έξοδος

Τα Μεγάλα Μοντέλα Γλώσσας (LLMs) μπορούν να παράγουν δομημένη έξοδο (π.χ. JSON) που είναι πιο εύκολη στην ανάλυση και επεξεργασία από κατώτερους πράκτορες ή υπηρεσίες. Αυτό είναι ιδιαίτερα χρήσιμο σε περιβάλλον πολλαπλών πρακτόρων, όπου μπορούμε να εκτελέσουμε αυτές τις εργασίες μετά την παραλαβή της εξόδου σχεδιασμού.

Το ακόλουθο απόσπασμα κώδικα Python παρουσιάζει έναν απλό πράκτορα σχεδιασμού που διασπά έναν στόχο σε υπο-εργασίες και δημιουργεί ένα δομημένο πλάνο:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Μοντέλο Υποεργασίας Ταξιδιού
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # θέλουμε να αναθέσουμε την εργασία στον πράκτορα

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Ορίζουμε το μήνυμα χρήστη
system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```
  
### Πράκτορας Σχεδιασμού με Πολλαπλή Ορχήστρωση Πρακτόρων

Σε αυτό το παράδειγμα, ένας Πράκτορας Διαχείρισης Νοημάτων (Semantic Router Agent) λαμβάνει ένα αίτημα χρήστη (π.χ., "Χρειάζομαι πρόγραμμα ξενοδοχείου για το ταξίδι μου.").

Ο σχεδιαστής στη συνέχεια:

* Παραλαμβάνει το Πρόγραμμα Ξενοδοχείου: Ο σχεδιαστής παίρνει το μήνυμα του χρήστη και, βάσει ενός συστημικού προτροπής (που περιλαμβάνει διαθέσιμες πληροφορίες πρακτόρων), δημιουργεί ένα δομημένο πρόγραμμα ταξιδιού.
* Καταγράφει τους Πράκτορες και τα Εργαλεία τους: Το μητρώο πρακτόρων περιέχει λίστα πρακτόρων (π.χ. για πτήση, ξενοδοχείο, ενοικίαση αυτοκινήτου και δραστηριότητες) μαζί με τις λειτουργίες ή τα εργαλεία που προσφέρουν.
* Δρομολογεί το Πρόγραμμα στους Αντίστοιχους Πράκτορες: Ανάλογα με τον αριθμό των υπο-εργασιών, ο σχεδιαστής είτε στέλνει απευθείας το μήνυμα σε αφιερωμένο πράκτορα (για περιπτώσεις μεμονωμένων εργασιών), είτε συντονίζει μέσω ενός διαχειριστή ομαδικής συνομιλίας για συνεργασία πολλαπλών πρακτόρων.
* Συνοψίζει το Αποτέλεσμα: Τέλος, ο σχεδιαστής συνοψίζει το παραγόμενο πρόγραμμα για σαφήνεια.  
Το ακόλουθο δείγμα κώδικα Python απεικονίζει αυτά τα βήματα:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Μοντέλο Υποεργασίας Ταξιδιού

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # θέλουμε να αναθέσουμε την εργασία στον πράκτορα

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Δημιουργήστε τον πελάτη

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Ορίστε το μήνυμα του χρήστη

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# Εκτυπώστε το περιεχόμενο της απόκρισης μετά τη φόρτωσή του ως JSON

pprint(json.loads(response_content))
```
  
Ακολουθεί η έξοδος από τον προηγούμενο κώδικα και μπορείτε να χρησιμοποιήσετε αυτή τη δομημένη έξοδο για δρομολόγηση στον `assigned_agent` και να συνοψίσετε το πρόγραμμα ταξιδιού στον τελικό χρήστη.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```
  
Παράδειγμα σημειωματάριου με το προηγούμενο δείγμα κώδικα είναι διαθέσιμο [εδώ](07-python-agent-framework.ipynb).

### Επαναληπτικός Σχεδιασμός

Ορισμένες εργασίες απαιτούν "πάνω-κάτω" αλληλεπίδραση ή επανασχεδιασμό, όπου το αποτέλεσμα μιας υπο-εργασίας επηρεάζει την επόμενη. Για παράδειγμα, αν ο πράκτορας ανακαλύψει έναν απρόβλεπτο τύπο δεδομένων κατά την κράτηση πτήσεων, μπορεί να χρειαστεί να προσαρμόσει τη στρατηγική του πριν προχωρήσει στις κρατήσεις ξενοδοχείων.

Επιπλέον, τα σχόλια του χρήστη (π.χ. ένας άνθρωπος που αποφασίζει ότι προτιμά μια νωρίτερη πτήση) μπορούν να ενεργοποιήσουν μερικό επανασχεδιασμό. Αυτή η δυναμική, επαναληπτική προσέγγιση εξασφαλίζει ότι η τελική λύση ευθυγραμμίζεται με τους περιορισμούς του πραγματικού κόσμου και τις εξελισσόμενες προτιμήσεις του χρήστη.

π.χ. δείγμα κώδικα

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. το ίδιο με τον προηγούμενο κώδικα και να μεταδώσει το ιστορικό χρήστη, το τρέχον πλάνο

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. να επανασχεδιάσει και να στείλει τις εργασίες στους αντίστοιχους πράκτορες
```
  
Για πιο ολοκληρωμένο σχεδιασμό, δείτε το Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> για επίλυση πολύπλοκων εργασιών.

## Περίληψη

Στο κείμενο αυτό εξετάσαμε ένα παράδειγμα για το πώς μπορούμε να δημιουργήσουμε έναν σχεδιαστή ικανό να επιλέγει δυναμικά τους διαθέσιμους πράκτορες που έχουν οριστεί. Η έξοδος του σχεδιαστή διασπά τις εργασίες και εκχωρεί τους πράκτορες ώστε να εκτελεστούν. Υποτίθεται ότι οι πράκτορες έχουν πρόσβαση σε λειτουργίες/εργαλεία που απαιτούνται για την εκτέλεση της εργασίας. Επιπλέον των πρακτόρων, μπορείτε να συμπεριλάβετε άλλα πρότυπα όπως αναστοχασμό, συνοψιστή και περιστρεφόμενη συνομιλία για περαιτέρω παραμετροποίηση.

## Πρόσθετοι Πόροι

Magentic One - Ένα γενικευμένο σύστημα πολλαπλών πρακτόρων για την επίλυση πολύπλοκων εργασιών που έχει επιτύχει εντυπωσιακά αποτελέσματα σε πολλαπλά απαιτητικά benchmarks πράκτορων. Αναφορά: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Σ’ αυτή την υλοποίηση, ο ορχηστρωτής δημιουργεί συγκεκριμένα πλάνα εργασιών και αναθέτει αυτές τις εργασίες στους διαθέσιμους πράκτορες. Επιπλέον του σχεδιασμού, ο ορχηστρωτής χρησιμοποιεί επίσης μηχανισμό παρακολούθησης για την παρακολούθηση της προόδου της εργασίας και επανασχεδιάζει εάν απαιτείται.

### Έχετε Περισσότερες Ερωτήσεις σχετικά με το Σχεδιαστικό Πρότυπο Προγραμματισμού;

Εγγραφείτε στο [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) για να συναντήσετε άλλους μαθητές, να παρακολουθήσετε ώρες γραφείου και να λάβετε απαντήσεις στις ερωτήσεις σας για τους AI Πράκτορες.

## Προηγούμενη Ενότητα

[Δημιουργώντας Αξιόπιστους AI Πράκτορες](../06-building-trustworthy-agents/README.md)

## Επόμενη Ενότητα

[Πρότυπο Σχεδιασμού Πολλαπλών Πρακτόρων](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις μπορεί να περιέχουν λάθη ή ανακρίβειες. Το αρχικό έγγραφο στη γλώσσα του θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->