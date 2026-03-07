[![Έμπιστοι Πράκτορες Τεχνητής Νοημοσύνης](../../../translated_images/el/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Κάντε κλικ στην εικόνα παραπάνω για να δείτε το βίντεο αυτού του μαθήματος)_

# Δημιουργία Έμπιστων Πρακτόρων Τεχνητής Νοημοσύνης

## Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Πώς να δημιουργήσετε και να αναπτύξετε ασφαλείς και αποτελεσματικούς Πράκτορες Τεχνητής Νοημοσύνης  
- Σημαντικές παραμέτρους ασφαλείας κατά την ανάπτυξη Πρακτόρων Τεχνητής Νοημοσύνης  
- Πώς να διατηρείτε την προστασία των δεδομένων και το απόρρητο των χρηστών κατά την ανάπτυξη Πρακτόρων Τεχνητής Νοημοσύνης

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα γνωρίζετε πώς να:

- Αναγνωρίζετε και να μετριάζετε τους κινδύνους κατά τη δημιουργία Πρακτόρων Τεχνητής Νοημοσύνης  
- Εφαρμόζετε μέτρα ασφαλείας για να διασφαλίσετε σωστή διαχείριση δεδομένων και πρόσβασης  
- Δημιουργείτε Πράκτορες Τεχνητής Νοημοσύνης που διατηρούν το απόρρητο των δεδομένων και προσφέρουν ποιοτική εμπειρία χρήστη

## Ασφάλεια

Ας εξετάσουμε πρώτα την κατασκευή ασφαλών πρακτορικών εφαρμογών. Ασφάλεια σημαίνει ότι ο πράκτορας τεχνητής νοημοσύνης λειτουργεί όπως έχει σχεδιαστεί. Ως δημιουργοί πρακτορικών εφαρμογών, διαθέτουμε μεθόδους και εργαλεία για τη μεγιστοποίηση της ασφάλειας:

### Δημιουργία Πλαισίου Μηνυμάτων Συστήματος

Αν έχετε ποτέ δημιουργήσει εφαρμογή τεχνητής νοημοσύνης χρησιμοποιώντας Μεγάλα Γλωσσικά Μοντέλα (LLMs), γνωρίζετε τη σημασία του σχεδιασμού ενός στιβαρού προτροπέα συστήματος ή μηνύματος συστήματος. Αυτές οι προτροπές καθορίζουν τους κανόνες, τις οδηγίες και τις κατευθύνσεις για το πώς το LLM θα αλληλεπιδρά με τον χρήστη και τα δεδομένα.

Για τους Πράκτορες Τεχνητής Νοημοσύνης, η προτροπή συστήματος είναι ακόμη πιο σημαντική, καθώς οι πράκτορες θα χρειαστούν πολύ συγκεκριμένες οδηγίες για να ολοκληρώσουν τις εργασίες που έχουμε σχεδιάσει για αυτούς.

Για να δημιουργήσουμε κλιμακούμενες προτροπές συστήματος, μπορούμε να χρησιμοποιήσουμε ένα πλαίσιο μηνυμάτων συστήματος για τη δημιουργία ενός ή περισσότερων πρακτόρων στην εφαρμογή μας:

![Δημιουργία Πλαισίου Μηνυμάτων Συστήματος](../../../translated_images/el/system-message-framework.3a97368c92d11d68.webp)

#### Βήμα 1: Δημιουργήστε ένα Μετα-Μήνυμα Συστήματος

Η μετα-προτροπή θα χρησιμοποιηθεί από ένα LLM για να παράγει τις προτροπές συστήματος για τους πράκτορες που δημιουργούμε. Το σχεδιάζουμε ως πρότυπο ώστε να μπορούμε να δημιουργούμε αποτελεσματικά πολλούς πράκτορες αν χρειαστεί.

Εδώ είναι ένα παράδειγμα μετα-μηνύματος συστήματος που θα δίναμε στο LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Βήμα 2: Δημιουργήστε μια βασική προτροπή

Το επόμενο βήμα είναι να δημιουργήσετε μια βασική προτροπή για να περιγράψετε τον Πράκτορα Τεχνητής Νοημοσύνης. Πρέπει να συμπεριλάβετε τον ρόλο του πράκτορα, τις εργασίες που θα ολοκληρώσει και τυχόν άλλες ευθύνες του πράκτορα.

Εδώ είναι ένα παράδειγμα:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Βήμα 3: Παρέχετε το Βασικό Μήνυμα Συστήματος στο LLM

Τώρα μπορούμε να βελτιστοποιήσουμε αυτό το μήνυμα συστήματος παρέχοντας το μετα-μήνυμα συστήματος ως μήνυμα συστήματος μαζί με το βασικό μήνυμα συστήματος.

Αυτό θα δημιουργήσει ένα μήνυμα συστήματος που έχει σχεδιαστεί καλύτερα για να καθοδηγεί τους πράκτορες Τεχνητής Νοημοσύνης μας:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Βήμα 4: Επανάληψη και Βελτίωση

Η αξία αυτού του πλαισίου μηνυμάτων συστήματος είναι να μπορείτε να κλιμακώνετε τη δημιουργία μηνυμάτων συστήματος από πολλούς πράκτορες ευκολότερα καθώς και να βελτιώνετε τα μηνύματα συστήματός σας με την πάροδο του χρόνου. Είναι σπάνιο να έχετε ένα μήνυμα συστήματος που δουλεύει την πρώτη φορά για ολόκληρη την περίπτωση χρήσης σας. Η δυνατότητα να κάνετε μικρές ρυθμίσεις και βελτιώσεις αλλάζοντας το βασικό μήνυμα συστήματος και τρέχοντάς το μέσα από το σύστημα θα σας επιτρέψει να συγκρίνετε και να αξιολογήσετε τα αποτελέσματα.

## Κατανόηση Απειλών

Για να δημιουργήσετε έμπιστους πράκτορες Τεχνητής Νοημοσύνης, είναι σημαντικό να κατανοήσετε και να μετριάσετε τους κινδύνους και τις απειλές προς τον πράκτορά σας. Ας δούμε μόνο μερικές από τις διαφορετικές απειλές προς τους πράκτορες ΤΝ και πώς μπορείτε καλύτερα να τα σχεδιάσετε και να προετοιμαστείτε γι’ αυτές.

![Κατανόηση Απειλών](../../../translated_images/el/understanding-threats.89edeada8a97fc0f.webp)

### Εργασίες και Οδηγίες

**Περιγραφή:** Οι επιτιθέμενοι προσπαθούν να αλλάξουν τις οδηγίες ή τους στόχους του πράκτορα ΤΝ μέσω προτροπής ή χειραγώγησης εισόδων.

**Μείωση:** Εκτελέστε ελέγχους επικύρωσης και φίλτρα εισόδου για να ανιχνεύσετε ενδεχομένως επικίνδυνες προτροπές πριν αυτές επεξεργαστούν από τον Πράκτορα ΤΝ. Δεδομένου ότι αυτές οι επιθέσεις συνήθως απαιτούν συχνή αλληλεπίδραση με τον Πράκτορα, ο περιορισμός του αριθμού των γύρων σε μια συνομιλία είναι ένας άλλος τρόπος για να αποτρέψετε αυτούς τους τύπους επιθέσεων.

### Πρόσβαση σε Κρίσιμα Συστήματα

**Περιγραφή:** Εάν ένας πράκτορας ΤΝ έχει πρόσβαση σε συστήματα και υπηρεσίες που αποθηκεύουν ευαίσθητα δεδομένα, οι επιτιθέμενοι μπορούν να παραβιάσουν την επικοινωνία μεταξύ του πράκτορα και αυτών των υπηρεσιών. Αυτές μπορεί να είναι άμεσες επιθέσεις ή έμμεσες προσπάθειες απόκτησης πληροφοριών για αυτά τα συστήματα μέσω του πράκτορα.

**Μείωση:** Οι πράκτορες ΤΝ θα πρέπει να έχουν πρόσβαση σε συστήματα μόνο όταν είναι απαραίτητο για να αποφευχθούν αυτού του είδους οι επιθέσεις. Η επικοινωνία μεταξύ πράκτορα και συστήματος πρέπει επίσης να είναι ασφαλής. Η εφαρμογή ελέγχου ταυτότητας και διαχείρισης πρόσβασης είναι ένας ακόμα τρόπος προστασίας αυτής της πληροφορίας.

### Υπερφόρτωση Πόρων και Υπηρεσιών

**Περιγραφή:** Οι πράκτορες ΤΝ μπορούν να έχουν πρόσβαση σε διάφορα εργαλεία και υπηρεσίες για την ολοκλήρωση εργασιών. Οι επιτιθέμενοι μπορούν να χρησιμοποιήσουν αυτή τη δυνατότητα για να επιτεθούν σε αυτές τις υπηρεσίες στέλνοντας μεγάλο όγκο αιτήσεων μέσω του πράκτορα ΤΝ, με αποτέλεσμα δυσλειτουργίες συστήματος ή υψηλό κόστος.

**Μείωση:** Εφαρμόστε πολιτικές που περιορίζουν τον αριθμό των αιτήσεων που μπορεί να κάνει ένας πράκτορας ΤΝ σε μια υπηρεσία. Ο περιορισμός των γύρων της συνομιλίας και των αιτήσεων προς τον πράκτορα ΤΝ είναι επίσης ένας τρόπος για την αποφυγή αυτού του είδους των επιθέσεων.

### Δηλητηρίαση Βάσης Γνώσης

**Περιγραφή:** Αυτός ο τύπος επίθεσης δεν στοχεύει άμεσα τον πράκτορα ΤΝ αλλά τη βάση γνώσης και άλλες υπηρεσίες που ο πράκτορας θα χρησιμοποιήσει. Μπορεί να περιλαμβάνει τη διαφθορά των δεδομένων ή πληροφοριών που ο πράκτορας θα χρησιμοποιήσει για να ολοκληρώσει μια εργασία, οδηγώντας σε μεροληπτικές ή ανεπιθύμητες απαντήσεις προς τον χρήστη.

**Μείωση:** Πραγματοποιήστε τακτικούς ελέγχους επικύρωσης των δεδομένων που θα χρησιμοποιεί ο πράκτορας ΤΝ στις ροές εργασιών του. Εξασφαλίστε ότι η πρόσβαση σε αυτά τα δεδομένα είναι ασφαλής και ότι τα δεδομένα αλλάζουν μόνο από αξιόπιστα άτομα για να αποφύγετε αυτού του είδους τη επίθεση.

### Αλυσιδωτά Σφάλματα

**Περιγραφή:** Οι πράκτορες ΤΝ έχουν πρόσβαση σε διάφορα εργαλεία και υπηρεσίες για την ολοκλήρωση εργασιών. Σφάλματα που προκαλούνται από επιτιθέμενους μπορεί να οδηγήσουν σε αποτυχίες άλλων συστημάτων στα οποία ο πράκτορας είναι συνδεδεμένος, καθιστώντας την επίθεση πιο εκτεταμένη και δυσκολότερη στην διάγνωση.

**Μείωση:** Μια μέθοδος για την αποφυγή αυτού είναι να λειτουργεί ο πράκτορας ΤΝ σε περιορισμένο περιβάλλον, όπως εκτέλεση εργασιών σε ένα κοντέινερ Docker, για να αποτραπούν άμεσες επιθέσεις στο σύστημα. Η δημιουργία μηχανισμών εφεδρείας και λογικής επανάληψης όταν συγκεκριμένα συστήματα απαντούν με σφάλμα είναι ένας άλλος τρόπος αποφυγής μεγαλύτερων αποτυχιών συστήματος.

## Ανθρώπινη Παρέμβαση στη Διαδικασία

Ένας ακόμα αποτελεσματικός τρόπος για να δημιουργήσετε συστήματα έμπιστων Πρακτόρων ΤΝ είναι να χρησιμοποιήσετε την προσέγγιση ανθρώπου-στο-βρόχο (Human-in-the-loop). Αυτό δημιουργεί μια ροή όπου οι χρήστες μπορούν να παρέχουν ανατροφοδότηση στους Πράκτορες κατά τη διάρκεια της εκτέλεσης. Οι χρήστες λειτουργούν ουσιαστικά ως πράκτορες σε ένα σύστημα πολλαπλών πρακτόρων, παρέχοντας έγκριση ή τερματισμό της διαδικασίας εκτέλεσης.

![Άνθρωπος στο Βρόχο](../../../translated_images/el/human-in-the-loop.5f0068a678f62f4f.webp)

Εδώ είναι ένα απόσπασμα κώδικα που χρησιμοποιεί το Microsoft Agent Framework για να δείξει πώς εφαρμόζεται αυτή η έννοια:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Δημιουργήστε τον πάροχο με έγκριση από άνθρωπο στη διαδικασία
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Δημιουργήστε τον πράκτορα με βήμα έγκρισης από άνθρωπο
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Ο χρήστης μπορεί να αναθεωρήσει και να εγκρίνει την απάντηση
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Συμπέρασμα

Η δημιουργία έμπιστων Πρακτόρων Τεχνητής Νοημοσύνης απαιτεί προσεκτικό σχεδιασμό, στιβαρά μέτρα ασφαλείας και συνεχή επανάληψη. Εφαρμόζοντας δομημένα συστήματα μετα-προτροπής, κατανοώντας πιθανούς κινδύνους και εφαρμόζοντας στρατηγικές μετριασμού, οι προγραμματιστές μπορούν να δημιουργήσουν πράκτορες που είναι ασφαλείς και αποτελεσματικοί. Επιπλέον, η ενσωμάτωση της προσέγγισης ανθρώπου-στο-βρόχο διασφαλίζει ότι οι πράκτορες παραμένουν ευθυγραμμισμένοι με τις ανάγκες των χρηστών ενώ ελαχιστοποιούν τους κινδύνους. Καθώς η Τεχνητή Νοημοσύνη εξελίσσεται, η διατήρηση μια προληπτικής στάσης σε θέματα ασφάλειας, απορρήτου και ηθικής θα είναι το κλειδί για την καλλιέργεια εμπιστοσύνης και αξιοπιστίας σε συστήματα που βασίζονται στην ΤΝ.

### Έχετε Περισσότερες Ερωτήσεις για τη Δημιουργία Έμπιστων Πρακτόρων Τεχνητής Νοημοσύνης;

Ελάτε στο [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) για να συναντήσετε άλλους εκπαιδευόμενους, να παρακολουθήσετε ώρες γραφείου και να λάβετε απαντήσεις στις ερωτήσεις σας για τους Πράκτορες ΤΝ.

## Πρόσθετοι Πόροι

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Επισκόπηση Υπεύθυνης Χρήσης Τεχνητής Νοημοσύνης</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Αξιολόγηση μοντέλων γενετικής ΤΝ και εφαρμογών ΤΝ</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Μηνύματα συστήματος ασφαλείας</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Πρότυπο Αξιολόγησης Κινδύνου</a>

## Προηγούμενο Μάθημα

[Agentic RAG](../05-agentic-rag/README.md)

## Επόμενο Μάθημα

[Pattern Σχεδιασμού Σχεδιασμού](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση Ευθύνης**:
Αυτό το έγγραφο έχει μεταφραστεί με τη χρήση της υπηρεσίας μηχανικής μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε λάβετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιεσδήποτε παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->