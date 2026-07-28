[![Trustworthy AI Agents](../../../translated_images/el/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Κάντε κλικ στην εικόνα παραπάνω για να δείτε το βίντεο αυτού του μαθήματος)_

# Δημιουργία Αξιόπιστων Πρακτόρων AI

## Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Πώς να δημιουργήσετε και να αναπτύξετε ασφαλείς και αποτελεσματικούς Πράκτορες AI
- Σημαντικές παράμετροι ασφαλείας κατά την ανάπτυξη Πρακτόρων AI.
- Πώς να διατηρήσετε το απόρρητο δεδομένων και χρηστών κατά την ανάπτυξη Πρακτόρων AI.

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα γνωρίζετε πώς να:

- Αναγνωρίζετε και μετριάζετε τους κινδύνους κατά τη δημιουργία Πρακτόρων AI.
- Εφαρμόζετε μέτρα ασφαλείας για να διασφαλίσετε τη σωστή διαχείριση δεδομένων και πρόσβασης.
- Δημιουργείτε Πράκτορες AI που διατηρούν το απόρρητο των δεδομένων και παρέχουν ποιοτική εμπειρία χρήστη.

## Ασφάλεια

Ας δούμε πρώτα πώς να δημιουργήσουμε ασφαλείς εφαρμογές οντοτήτων. Ασφάλεια σημαίνει ότι ο πράκτορας AI λειτουργεί όπως έχει σχεδιαστεί. Ως δημιουργοί εφαρμογών οντοτήτων, έχουμε μεθόδους και εργαλεία για να μεγιστοποιήσουμε την ασφάλεια:

### Δημιουργία Πλαισίου Μηνύματος Συστήματος

Αν έχετε δημιουργήσει ποτέ εφαρμογή AI χρησιμοποιώντας Μεγάλα Γλωσσικά Μοντέλα (LLMs), γνωρίζετε τη σημασία του σχεδιασμού ενός ισχυρού system prompt ή μηνύματος συστήματος. Αυτά τα prompts καθορίζουν τους μετακανόνες, τις οδηγίες και τις κατευθυντήριες γραμμές για το πώς το LLM θα αλληλεπιδράσει με τον χρήστη και τα δεδομένα.

Για τους Πράκτορες AI, το σύστημα prompt είναι ακόμη πιο σημαντικό καθώς οι Πράκτορες AI θα χρειαστούν πολύ συγκεκριμένες οδηγίες για να ολοκληρώσουν τα καθήκοντα που έχουμε σχεδιάσει για αυτούς.

Για να δημιουργήσουμε κλιμακούμενα system prompts, μπορούμε να χρησιμοποιήσουμε ένα πλαίσιο μηνύματος συστήματος για την κατασκευή ενός ή περισσότερων πρακτόρων στην εφαρμογή μας:

![Building a System Message Framework](../../../translated_images/el/system-message-framework.3a97368c92d11d68.webp)

#### Βήμα 1: Δημιουργία Μετα-Μηνύματος Συστήματος 

Το μετα-prompt θα χρησιμοποιηθεί από το LLM για να δημιουργήσει τα system prompts για τους πράκτορες που δημιουργούμε. Το σχεδιάζουμε ως πρότυπο ώστε να μπορούμε να δημιουργήσουμε πολλούς πράκτορες αποτελεσματικά, αν χρειαστεί.

Εδώ είναι ένα παράδειγμα μετα-μηνύματος συστήματος που θα δώσουμε στο LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Βήμα 2: Δημιουργία βασικού prompt

Το επόμενο βήμα είναι να δημιουργήσουμε ένα βασικό prompt που να περιγράφει τον Πράκτορα AI. Πρέπει να συμπεριλάβετε τον ρόλο του πράκτορα, τα καθήκοντα που θα ολοκληρώσει, καθώς και άλλες ευθύνες του πράκτορα.

Εδώ είναι ένα παράδειγμα:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Βήμα 3: Παροχή Βασικού Μηνύματος Συστήματος στο LLM

Τώρα μπορούμε να βελτιστοποιήσουμε αυτό το μήνυμα συστήματος παρέχοντας το μετα-μήνυμα συστήματος ως μήνυμα συστήματος μαζί με το βασικό μήνυμα συστήματος.

Αυτό θα παραγάγει ένα μήνυμα συστήματος που είναι καλύτερα σχεδιασμένο για να καθοδηγεί τους Πράκτορες AI:

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

Η αξία αυτού του πλαισίου μηνύματος συστήματος είναι η δυνατότητα κλιμάκωσης της δημιουργίας μηνυμάτων συστήματος από πολλούς πράκτορες με ευκολία, καθώς και η βελτίωση των μηνυμάτων σας με την πάροδο του χρόνου. Είναι σπάνιο να έχετε ένα μήνυμα συστήματος που λειτουργεί τέλεια στην πρώτη προσπάθεια για τη συνολική περίπτωσή σας. Η δυνατότητα μικρών προσαρμογών και βελτιώσεων αλλάζοντας το βασικό μήνυμα συστήματος και εκτελώντας το μέσα από το σύστημα θα σας επιτρέψει να συγκρίνετε και να αξιολογήσετε τα αποτελέσματα.

## Κατανόηση Απειλών

Για να δημιουργήσετε αξιόπιστους Πράκτορες AI, είναι σημαντικό να κατανοήσετε και να μετριάσετε τους κινδύνους και τις απειλές για τον πράκτορά σας AI. Ας δούμε μερικές μόνο από τις διάφορες απειλές προς τους Πράκτορες AI και πώς μπορείτε να σχεδιάσετε και να προετοιμαστείτε καλύτερα για αυτές.

![Understanding Threats](../../../translated_images/el/understanding-threats.89edeada8a97fc0f.webp)

### Καθήκον και Οδηγίες

**Περιγραφή:** Οι επιτιθέμενοι προσπαθούν να αλλάξουν τις οδηγίες ή τους στόχους του Πράκτορα AI μέσω prompt ή χειραγώγησης των εισόδων.

**Μέτρα Μείωσης:** Εκτελέστε ελέγχους επικύρωσης και φίλτρα εισόδου για να ανιχνεύσετε πιθανά επικίνδυνα prompts πριν αυτά επεξεργαστούν από τον Πράκτορα AI. Δεδομένου ότι αυτές οι επιθέσεις συνήθως απαιτούν συχνή αλληλεπίδραση με τον Πράκτορα, ο περιορισμός του αριθμού των γύρων σε μια συνομιλία είναι ένας άλλος τρόπος για να αποτραπούν αυτού του είδους οι επιθέσεις.

### Πρόσβαση σε Κρίσιμα Συστήματα

**Περιγραφή:** Εάν ένας Πράκτορας AI έχει πρόσβαση σε συστήματα και υπηρεσίες που αποθηκεύουν ευαίσθητα δεδομένα, οι επιτιθέμενοι μπορούν να διαβρώσουν την επικοινωνία μεταξύ του πράκτορα και αυτών των υπηρεσιών. Αυτές μπορούν να είναι άμεσες επιθέσεις ή έμμεσες προσπάθειες απόκτησης πληροφοριών για αυτά τα συστήματα μέσω του πράκτορα.

**Μέτρα Μείωσης:** Οι Πράκτορες AI θα πρέπει να έχουν πρόσβαση στα συστήματα μόνο κατά περίπτωση ανάγκης για να αποτραπούν αυτού του είδους οι επιθέσεις. Η επικοινωνία μεταξύ πράκτορα και συστήματος πρέπει επίσης να είναι ασφαλής. Η εφαρμογή αυθεντικοποίησης και ελέγχου πρόσβασης αποτελεί έναν ακόμα τρόπο προστασίας αυτών των πληροφοριών.

### Υπερφόρτωση Πόρων και Υπηρεσιών

**Περιγραφή:** Οι Πράκτορες AI μπορούν να έχουν πρόσβαση σε διάφορα εργαλεία και υπηρεσίες για να ολοκληρώσουν καθήκοντα. Οι επιτιθέμενοι μπορούν να χρησιμοποιήσουν αυτή τη δυνατότητα για να επιτεθούν σε αυτές τις υπηρεσίες στέλνοντας υψηλό όγκο αιτήσεων μέσω του Πράκτορα AI, που μπορεί να οδηγήσει σε αποτυχίες συστήματος ή υψηλό κόστος.

**Μέτρα Μείωσης:** Υλοποιήστε πολιτικές για να περιορίσετε τον αριθμό αιτήσεων που μπορεί να κάνει ένας Πράκτορας AI σε μια υπηρεσία. Ο περιορισμός του αριθμού των γύρων συνομιλίας και αιτήσεων προς τον Πράκτορά σας AI είναι ένας ακόμα τρόπος πρόληψης τέτοιων επιθέσεων.

### Δηλητηρίαση Βάσης Γνώσεων

**Περιγραφή:** Αυτό το είδος επίθεσης δεν στοχεύει άμεσα τον Πράκτορα AI αλλά τη βάση γνώσεων και άλλες υπηρεσίες που χρησιμοποιεί ο Πράκτορας AI. Αυτό μπορεί να περιλαμβάνει τη διαφθορά των δεδομένων ή των πληροφοριών που ο Πράκτορας AI χρησιμοποιεί για την ολοκλήρωση ενός καθήκοντος, οδηγώντας σε προκατειλημμένες ή ανεπιθύμητες απαντήσεις προς τον χρήστη.

**Μέτρα Μείωσης:** Πραγματοποιήστε τακτικούς ελέγχους των δεδομένων που ο Πράκτορας AI χρησιμοποιεί στις ροές εργασίας του. Διασφαλίστε ότι η πρόσβαση σε αυτά τα δεδομένα είναι ασφαλής και ότι αλλάζουν μόνο από αξιόπιστα άτομα για να αποφευχθεί αυτό το είδος επίθεσης.

### Αλυσιδωτά Σφάλματα

**Περιγραφή:** Οι Πράκτορες AI έχουν πρόσβαση σε διάφορα εργαλεία και υπηρεσίες για την ολοκλήρωση καθήκοντων. Λάθη που προκαλούνται από επιτιθέμενους μπορεί να οδηγήσουν σε αποτυχίες άλλων συστημάτων με τα οποία ο Πράκτορας AI είναι συνδεδεμένος, καθιστώντας την επίθεση πιο εκτεταμένη και δυσκολότερη στην αντιμετώπιση.

**Μέτρα Μείωσης:** Μια μέθοδος για την αποφυγή αυτού είναι ο Πράκτορας AI να λειτουργεί σε περιορισμένο περιβάλλον, όπως εκτέλεση εργασιών σε κοντέινερ Docker, για να αποτρέπονται άμεσες επιθέσεις στο σύστημα. Η δημιουργία μηχανισμών εναλλακτικής λύσης και λογικής επανάληψης όταν ορισμένα συστήματα ανταποκρίνονται με σφάλμα είναι ένας άλλος τρόπος πρόληψης μεγαλύτερων αποτυχιών συστήματος.

## Ανθρώπινος στον Κύκλο

Ένας άλλος αποτελεσματικός τρόπος για να δημιουργηθούν αξιόπιστα συστήματα Πρακτόρων AI είναι με τη χρήση Ανθρώπινου στον Κύκλο. Αυτό δημιουργεί μια ροή όπου οι χρήστες μπορούν να παρέχουν ανατροφοδότηση στους Πράκτορες κατά την εκτέλεση. Οι χρήστες ουσιαστικά λειτουργούν ως πράκτορες σε ένα πολυ-πρακτορικό σύστημα παρέχοντας έγκριση ή τερματισμό της διαδικασίας.

![Human in The Loop](../../../translated_images/el/human-in-the-loop.5f0068a678f62f4f.webp)

Εδώ είναι ένα απόσπασμα κώδικα που χρησιμοποιεί το Microsoft Agent Framework για να δείξει πώς υλοποιείται αυτή η ιδέα:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Δημιουργήστε τον πάροχο με έγκριση από άνθρωπο στη διαδικασία
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Δημιουργήστε τον πράκτορα με βήμα έγκρισης από άνθρωπο
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Ο χρήστης μπορεί να ελέγξει και να εγκρίνει την απάντηση
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Συμπέρασμα

Η δημιουργία αξιόπιστων Πρακτόρων AI απαιτεί προσεκτικό σχεδιασμό, ανθεκτικά μέτρα ασφαλείας και συνεχή επανάληψη. Με την υλοποίηση δομημένων συστημάτων μετα-prompting, την κατανόηση πιθανών απειλών και την εφαρμογή στρατηγικών μείωσης, οι προγραμματιστές μπορούν να δημιουργήσουν Πράκτορες AI που είναι ασφαλείς και αποτελεσματικοί. Επιπλέον, η ενσωμάτωση της προσέγγισης ανθρώπου στον κύκλο διασφαλίζει ότι οι Πράκτορες AI παραμένουν ευθυγραμμισμένοι με τις ανάγκες των χρηστών, ενώ ελαχιστοποιούνται οι κίνδυνοι. Καθώς το AI εξελίσσεται, η διατήρηση μιας προληπτικής στάσης σε θέματα ασφάλειας, απορρήτου και ηθικών ζητημάτων θα είναι το κλειδί για την οικοδόμηση εμπιστοσύνης και αξιοπιστίας σε συστήματα με τεχνητή νοημοσύνη.

## Παραδείγματα Κώδικα

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Επίδειξη βήμα προς βήμα του πλαισίου συστήματος μετα-prompt.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Πύλες έγκρισης πριν από ενέργεια, ιεράρχηση κινδύνου και καταγραφή για αξιόπιστους πράκτορες.

### Έχετε Περισσότερες Ερωτήσεις σχετικά με τη Δημιουργία Αξιόπιστων Πρακτόρων AI;

Εγγραφείτε στο [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) για να συναντήσετε άλλους μαθητευόμενους, να παρακολουθήσετε ώρες γραφείου και να λάβετε απαντήσεις στις ερωτήσεις σας για Πράκτορες AI.

## Πρόσθετοι Πόροι

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Επισκόπηση Υπεύθυνης Χρήσης AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Αξιολόγηση γενετικών μοντέλων AI και εφαρμογών AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Μηνύματα συστήματος ασφάλειας</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Πρότυπο Αξιολόγησης Κινδύνου</a>

## Προηγούμενο Μάθημα

[Agentic RAG](../05-agentic-rag/README.md)

## Επόμενο Μάθημα

[Σχέδιο Σχεδιασμού Προγραμματισμού](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->