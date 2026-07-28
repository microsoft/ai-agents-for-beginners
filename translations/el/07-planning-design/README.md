[![Planning Design Pattern](../../../translated_images/el/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Κάντε κλικ στην εικόνα παραπάνω για να δείτε το βίντεο αυτού του μαθήματος)_

# Σχεδιασμός Σχεδίου

## Εισαγωγή

Αυτό το μάθημα θα καλύψει

* Τον καθορισμό σαφούς συνολικού στόχου και τη διάσπαση μιας πολύπλοκης εργασίας σε διαχειρίσιμες εργασίες.
* Την αξιοποίηση δομημένης εξόδου για πιο αξιόπιστες και μηχανο-αναγνώσιμες απαντήσεις.
* Την εφαρμογή προσέγγισης βασισμένης σε γεγονότα για τη διαχείριση δυναμικών εργασιών και απρόβλεπτων εισόδων.

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα έχετε κατανόηση σχετικά με:

* Την αναγνώριση και τον καθορισμό συνολικού στόχου για έναν AI πράκτορα, διασφαλίζοντας ότι γνωρίζει σαφώς τι πρέπει να επιτευχθεί.
* Τη διάσπαση μιας πολύπλοκης εργασίας σε διαχειρίσιμα υπο-εργασίες και την οργάνωσή τους σε λογική ακολουθία.
* Τον εξοπλισμό των πρακτόρων με τα κατάλληλα εργαλεία (π.χ., εργαλεία αναζήτησης ή ανάλυσης δεδομένων), την απόφαση πότε και πώς χρησιμοποιούνται, και τη διαχείριση απρόβλεπτων καταστάσεων που προκύπτουν.
* Την αξιολόγηση των αποτελεσμάτων των υπο-εργασιών, τη μέτρηση της απόδοσης και την επανάληψη των ενεργειών για τη βελτίωση της τελικής εξόδου.

## Καθορισμός του Συνολικού Στόχου και Διάσπαση μιας Εργασίας

![Defining Goals and Tasks](../../../translated_images/el/defining-goals-tasks.d70439e19e37c47a.webp)

Οι περισσότερες εργασίες στον πραγματικό κόσμο είναι πολύπλοκες για να αντιμετωπιστούν με ένα μόνο βήμα. Ένας AI πράκτορας χρειάζεται έναν συνοπτικό στόχο για να καθοδηγήσει το σχεδιασμό και τις ενέργειές του. Για παράδειγμα, σκεφτείτε τον στόχο:

    "Δημιουργία ένα τριήμερου προγράμματος ταξιδιού."

Αν και είναι απλό να αναφερθεί, χρειάζεται ακόμα βελτίωση. Όσο πιο σαφής είναι ο στόχος, τόσο καλύτερα μπορεί ο πράκτορας (και οποιοιδήποτε ανθρώπινοι συνεργάτες) να εστιάσουν στην επίτευξη του σωστού αποτελέσματος, όπως η δημιουργία ενός ολοκληρωμένου προγράμματος με επιλογές πτήσεων, προτάσεις ξενοδοχείων και προτάσεις δραστηριοτήτων.

### Διάσπαση Εργασιών

Οι μεγάλες ή περίπλοκες εργασίες γίνονται πιο διαχειρίσιμες όταν χωρίζονται σε μικρότερες, στοχευμένες υπο-εργασίες.
Για το παράδειγμα του προγράμματος ταξιδιού, μπορείτε να διασπάσετε τον στόχο σε:

* Κράτηση Πτήσεων
* Κράτηση Ξενοδοχείου
* Ενοικίαση Αυτοκινήτου
* Προσωποποίηση

Κάθε υπο-εργασία μπορεί στη συνέχεια να αντιμετωπιστεί από ειδικούς πράκτορες ή διαδικασίες. Ένας πράκτορας μπορεί να εξειδικεύεται στην αναζήτηση των καλύτερων προσφορών πτήσεων, ένας άλλος να εστιάζει στις κρατήσεις ξενοδοχείων και ούτω καθεξής. Ένας συντονιστής ή “κατώτερος” πράκτορας μπορεί να συγκεντρώσει αυτά τα αποτελέσματα σε ένα ενιαίο και ολοκληρωμένο πρόγραμμα για τον τελικό χρήστη.

Αυτή η αρθρωτή προσέγγιση επιτρέπει επίσης σταδιακές βελτιώσεις. Για παράδειγμα, μπορείτε να προσθέσετε εξειδικευμένους πράκτορες για Προτάσεις Φαγητού ή Τοπικές Προτάσεις Δραστηριοτήτων και να βελτιώσετε το πρόγραμμα με την πάροδο του χρόνου.

### Δομημένη έξοδος

Τα Μεγάλα Μοντέλα Γλώσσας (LLMs) μπορούν να παράγουν δομημένη έξοδο (π.χ. JSON) που είναι πιο εύκολη για τους κατώτερους πράκτορες ή τις υπηρεσίες να διαβάσουν και να επεξεργαστούν. Αυτό είναι ιδιαίτερα χρήσιμο σε περιβάλλον πολλαπλών πρακτόρων, όπου μπορούμε να εκτελέσουμε αυτές τις εργασίες μετά την παραλαβή της εξόδου σχεδιασμού.

Το ακόλουθο απόσπασμα Python δείχνει έναν απλό πράκτορα σχεδιασμού που διασπά έναν στόχο σε υπο-εργασίες και δημιουργεί ένα δομημένο σχέδιο:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Μοντέλο Υπο-Εργασίας Ταξιδιού
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # θέλουμε να αναθέσουμε την εργασία στον πράκτορα

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Ορισμός μηνύματος χρήστη
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

### Πράκτορας Σχεδιασμού με Ορχήστρωση Πολλών Πρακτόρων

Σε αυτό το παράδειγμα, ένας Πράκτορας Ρουτερ Σημασιολογίας λαμβάνει αίτημα χρήστη (π.χ., "Χρειάζομαι ένα σχέδιο ξενοδοχείου για το ταξίδι μου.").

Ο σχεδιαστής στη συνέχεια:

* Λαμβάνει το Σχέδιο Ξενοδοχείου: Ο σχεδιαστής παίρνει το μήνυμα του χρήστη και, βασιζόμενος σε ένα συστημικό prompt (συμπεριλαμβανομένων των διαθέσιμων λεπτομερειών πρακτόρων), δημιουργεί ένα δομημένο σχέδιο ταξιδιού.
* Λίστα Πρακτόρων και Εργαλείων: Το μητρώο πρακτόρων έχει μια λίστα από πράκτορες (π.χ. για πτήσεις, ξενοδοχεία, ενοικιάσεις αυτοκινήτου και δραστηριότητες) μαζί με τις λειτουργίες ή τα εργαλεία που προσφέρουν.
* Δρομολογεί το Σχέδιο στους Αντίστοιχους Πράκτορες: Ανάλογα με τον αριθμό των υπο-εργασιών, ο σχεδιαστής είτε στέλνει το μήνυμα απευθείας σε έναν ειδικό πράκτορα (για σενάρια μιας εργασίας) είτε συντονίζει μέσω ενός διαχειριστή ομαδικής συνομιλίας για τη συνεργασία πολλαπλών πρακτόρων.
* Περιορίζει το Αποτέλεσμα: Τέλος, ο σχεδιαστής συνοψίζει το παραχθέν σχέδιο για σαφήνεια.
Το ακόλουθο δείγμα κώδικα Python παρουσιάζει αυτά τα βήματα:

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

# Μοντέλο Υποεργασίας Ταξιδίου

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # θέλουμε να αναθέσουμε την εργασία στον παράγοντα

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Δημιουργήστε τον πελάτη

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Ορίστε το μήνυμα χρήστη

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

Αυτό που ακολουθεί είναι η έξοδος από τον προηγούμενο κώδικα και μπορείτε στη συνέχεια να χρησιμοποιήσετε αυτή τη δομημένη έξοδο για να δρομολογήσετε στον `assigned_agent` και να συνοψίσετε το σχέδιο ταξιδιού στον τελικό χρήστη.

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

Ένα παράδειγμα σημειωματάριου με το προηγούμενο δείγμα κώδικα είναι διαθέσιμο [εδώ](./code_samples/07-python-agent-framework.ipynb).

### Επαναληπτικός Σχεδιασμός

Ορισμένες εργασίες απαιτούν αλληλεπίδραση ή επανασχεδιασμό, όπου το αποτέλεσμα μιας υπο-εργασίας επηρεάζει την επόμενη. Για παράδειγμα, εάν ο πράκτορας ανακαλύψει απρόβλεπτο μορφότυπο δεδομένων κατά την κράτηση πτήσεων, μπορεί να χρειαστεί να προσαρμόσει την στρατηγική του πριν προχωρήσει στις κρατήσεις ξενοδοχείου.

Επιπλέον, η ανατροφοδότηση του χρήστη (π.χ., ένας άνθρωπος που αποφασίζει ότι προτιμά μια νωρίτερη πτήση) μπορεί να ενεργοποιήσει μερικό επανασχεδιασμό. Αυτή η δυναμική, επαναληπτική προσέγγιση διασφαλίζει ότι η τελική λύση ευθυγραμμίζεται με τους πραγματικούς περιορισμούς και τις μεταβαλλόμενες προτιμήσεις των χρηστών.

π.χ. δείγμα κώδικα

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. όπως και ο προηγούμενος κώδικας και μεταβίβαση στο ιστορικό χρήστη, τρέχον σχέδιο

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
# .. ανασχεδίαση και αποστολή των εργασιών στους αντίστοιχους πράκτορες
```

Για πιο ολοκληρωμένο σχεδιασμό δείτε το Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> για την επίλυση πολύπλοκων εργασιών.

## Περίληψη

Σε αυτό το άρθρο εξετάσαμε ένα παράδειγμα για το πώς μπορούμε να δημιουργήσουμε έναν σχεδιαστή που μπορεί να επιλέξει δυναμικά τους διαθέσιμους πράκτορες που ορίζονται. Το αποτέλεσμα του Σχεδιαστή διασπά τις εργασίες και αναθέτει τους πράκτορες ώστε να μπορούν να εκτελεστούν. Υποτίθεται ότι οι πράκτορες έχουν πρόσβαση στις λειτουργίες/εργαλεία που απαιτούνται για την εκτέλεση της εργασίας. Επιπλέον των πρακτόρων, μπορείτε να συμπεριλάβετε άλλα μοτίβα όπως reflection, summarizer και round robin chat για περαιτέρω προσαρμογή.

## Πρόσθετοι Πόροι

Magnetic One - Ένα γενικός σύστημα πολλαπλών πρακτόρων για την επίλυση πολύπλοκων εργασιών που έχει επιτύχει εντυπωσιακά αποτελέσματα σε πολλαπλά απαιτητικά benchmarks πρακτόρων. Αναφορά: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. Σε αυτή την υλοποίηση ο συντονιστής δημιουργεί ειδικά σχέδια εργασιών και αναθέτει αυτές τις εργασίες στους διαθέσιμους πράκτορες. Εκτός από τον σχεδιασμό, ο συντονιστής χρησιμοποιεί επίσης μηχανισμό παρακολούθησης για την παρακολούθηση της προόδου της εργασίας και επανασχεδιάζει όταν απαιτείται.

### Έχετε Περισσότερες Ερωτήσεις για το Σχεδιαστικό Μοτίβο Planning;

Εγγραφείτε στο [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) για να συναντήσετε άλλους μαθητές, να παρακολουθήσετε ώρες γραφείου και να λάβετε απαντήσεις στα ερωτήματα σας για AI Agents.

## Προηγούμενο Μάθημα

[Κατασκευή Αξιόπιστων Πρακτόρων AI](../06-building-trustworthy-agents/README.md)

## Επόμενο Μάθημα

[Μοτίβο Σχεδιασμού Πολλαπλών Πρακτόρων](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->