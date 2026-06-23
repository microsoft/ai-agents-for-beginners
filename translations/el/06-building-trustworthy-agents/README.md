[![Agents AI Αξιόπιστοι](../../../translated_images/el/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Κάντε κλικ στην εικόνα παραπάνω για να δείτε το βίντεο αυτού του μαθήματος)_

# Δημιουργία Αξιόπιστων Agents AI

## Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Πώς να δημιουργήσετε και να αναπτύξετε ασφαλή και αποτελεσματικά Agents AI
- Σημαντικές παράμετροι ασφάλειας κατά την ανάπτυξη Agents AI.
- Πώς να διατηρήσετε την ιδιωτικότητα των δεδομένων και των χρηστών κατά την ανάπτυξη Agents AI.

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα γνωρίζετε πώς να:

- Αναγνωρίζετε και να μετριάζετε τους κινδύνους κατά τη δημιουργία Agents AI.
- Εφαρμόζετε μέτρα ασφαλείας για να διασφαλίσετε ότι τα δεδομένα και η πρόσβαση διαχειρίζονται σωστά.
- Δημιουργείτε Agents AI που διατηρούν την ιδιωτικότητα των δεδομένων και παρέχουν ποιοτική εμπειρία χρήστη.

## Ασφάλεια

Ας δούμε πρώτα τη δημιουργία ασφαλών εφαρμογών agentic. Ασφάλεια σημαίνει ότι ο agent AI λειτουργεί όπως έχει σχεδιαστεί. Ως κατασκευαστές εφαρμογών agentic, έχουμε μεθόδους και εργαλεία για να μεγιστοποιήσουμε την ασφάλεια:

### Δημιουργία Πλαισίου Μηνύματος Συστήματος

Αν έχετε ποτέ δημιουργήσει μια εφαρμογή AI χρησιμοποιώντας Μεγάλα Μοντέλα Γλώσσας (LLMs), γνωρίζετε τη σημασία του σχεδίου ενός στιβαρού prompt συστήματος ή μηνύματος συστήματος. Αυτά τα prompts καθορίζουν τους μετακανόνες, τις οδηγίες και τις κατευθυντήριες γραμμές για το πώς το LLM θα αλληλεπιδρά με το χρήστη και τα δεδομένα.

Για τους Agents AI, το prompt συστήματος είναι ακόμη πιο σημαντικό καθώς οι Agents AI θα χρειαστούν πολύ συγκεκριμένες οδηγίες για να ολοκληρώσουν τις εργασίες που έχουμε σχεδιάσει γι' αυτούς.

Για να δημιουργήσουμε ευέλικτα prompts συστήματος, μπορούμε να χρησιμοποιήσουμε ένα πλαίσιο μηνύματος συστήματος για να κατασκευάσουμε έναν ή περισσότερους agents στην εφαρμογή μας:

![Δημιουργία Πλαισίου Μηνύματος Συστήματος](../../../translated_images/el/system-message-framework.3a97368c92d11d68.webp)

#### Βήμα 1: Δημιουργία ενός Meta Μηνύματος Συστήματος

Το meta prompt θα χρησιμοποιηθεί από ένα LLM για να δημιουργήσει τα prompts συστήματος για τους agents που δημιουργούμε. Το σχεδιάζουμε ως πρότυπο ώστε να μπορούμε να δημιουργούμε πολλούς agents αποδοτικά, αν χρειαστεί.

Ακολουθεί ένα παράδειγμα meta μηνύματος συστήματος που θα δώσουμε στο LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Βήμα 2: Δημιουργία βασικού prompt

Το επόμενο βήμα είναι να δημιουργήσουμε ένα βασικό prompt που να περιγράφει τον Agent AI. Πρέπει να συμπεριλάβετε τον ρόλο του agent, τις εργασίες που θα ολοκληρώσει, και οποιεσδήποτε άλλες ευθύνες του agent.

Ακολουθεί ένα παράδειγμα:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Βήμα 3: Παροχή βασικού Μηνύματος Συστήματος στο LLM

Τώρα μπορούμε να βελτιστοποιήσουμε αυτό το μήνυμα συστήματος παρέχοντας το meta μήνυμα συστήματος ως το μήνυμα συστήματος μαζί με το βασικό μας μήνυμα συστήματος.

Αυτό θα παράξει ένα μήνυμα συστήματος που είναι καλύτερα σχεδιασμένο για να καθοδηγεί τους Agents AI μας:

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

Η αξία αυτού του πλαισίου μηνύματος συστήματος είναι να μπορεί να κλιμακωθεί η δημιουργία μηνυμάτων συστήματος από πολλαπλούς agents πιο εύκολα καθώς και να βελτιώνετε τα μηνύματά σας με τον χρόνο. Είναι σπάνιο να έχετε ένα μήνυμα συστήματος που να δουλεύει σωστά με την πρώτη φορά για το πλήρες σενάριο χρήσης σας. Η δυνατότητα να κάνετε μικρές αλλαγές και βελτιώσεις αλλάζοντας το βασικό μήνυμα συστήματος και τρέχοντάς το μέσα από το σύστημα θα σας επιτρέψει να συγκρίνετε και να αξιολογήσετε τα αποτελέσματα.

## Κατανόηση Απειλών

Για να δημιουργήσετε αξιόπιστους Agents AI, είναι σημαντικό να κατανοήσετε και να μετριάσετε τους κινδύνους και τις απειλές προς τον Agent AI σας. Ας δούμε μερικές μόνο από τις διαφορετικές απειλές προς τους Agents AI και πώς μπορείτε να προγραμματίσετε και να προετοιμαστείτε καλύτερα για αυτές.

![Κατανόηση Απειλών](../../../translated_images/el/understanding-threats.89edeada8a97fc0f.webp)

### Εργασία και Οδηγία

**Περιγραφή:** Οι επιτιθέμενοι προσπαθούν να αλλάξουν τις οδηγίες ή τους στόχους του Agent AI μέσω prompting ή χειραγώγησης εισόδων.

**Μετριασμός**: Εκτελέστε ελέγχους επικύρωσης και φίλτρα εισόδου για να ανιχνεύσετε πιθανά επικίνδυνα prompts πριν επεξεργαστούν από τον Agent AI. Επειδή αυτές οι επιθέσεις συνήθως απαιτούν συχνή αλληλεπίδραση με τον Agent, ο περιορισμός του αριθμού των γύρων σε μια συνομιλία είναι ένας άλλος τρόπος για να αποτραπούν αυτά τα είδη επιθέσεων.

### Πρόσβαση σε Κρίσιμα Συστήματα

**Περιγραφή:** Αν ένας Agent AI έχει πρόσβαση σε συστήματα και υπηρεσίες που αποθηκεύουν ευαίσθητα δεδομένα, οι επιτιθέμενοι μπορούν να διαβρώσουν την επικοινωνία μεταξύ του agent και αυτών των υπηρεσιών. Αυτές μπορεί να είναι άμεσες επιθέσεις ή έμμεσες προσπάθειες να κερδίσουν πληροφορίες για αυτά τα συστήματα μέσω του agent.

**Μετριασμός:** Οι Agents AI θα πρέπει να έχουν πρόσβαση σε συστήματα μόνο κατά περίπτωση ανάγκης για να αποτραπούν τέτοιου είδους επιθέσεις. Η επικοινωνία μεταξύ του agent και του συστήματος πρέπει επίσης να είναι ασφαλής. Η υλοποίηση πιστοποίησης ταυτότητας και ελέγχου πρόσβασης είναι ένας ακόμα τρόπος για να προστατευτεί αυτή η πληροφορία.

### Υπερφόρτωση Πόρων και Υπηρεσιών

**Περιγραφή:** Οι Agents AI μπορούν να έχουν πρόσβαση σε διάφορα εργαλεία και υπηρεσίες για να ολοκληρώσουν εργασίες. Οι επιτιθέμενοι μπορούν να χρησιμοποιήσουν αυτή την ικανότητα για να επιτεθούν σε αυτές τις υπηρεσίες στέλνοντας μεγάλο όγκο αιτημάτων μέσω του Agent AI, το οποίο μπορεί να οδηγήσει σε αποτυχίες συστήματος ή υψηλό κόστος.

**Μετριασμός:** Υλοποιήστε πολιτικές για να περιορίζετε τον αριθμό των αιτημάτων που μπορεί να κάνει ένας Agent AI σε μια υπηρεσία. Ο περιορισμός των γύρων συνομιλίας και των αιτημάτων προς τον Agent AI σας είναι ένας επιπλέον τρόπος να αποτραπούν αυτές οι επιθέσεις.

### Δηλητηρίαση Βάσης Γνώσεων

**Περιγραφή:** Αυτός ο τύπος επίθεσης δεν στοχεύει άμεσα τον Agent AI αλλά στοχεύει τη βάση γνώσεων και άλλες υπηρεσίες που ο Agent AI θα χρησιμοποιήσει. Αυτό μπορεί να περιλαμβάνει τη διαφθορά των δεδομένων ή πληροφορίας που θα χρησιμοποιήσει ο Agent AI για να ολοκληρώσει μια εργασία, οδηγώντας σε μεροληπτικές ή ανεπιθύμητες απαντήσεις προς τον χρήστη.

**Μετριασμός:** Εκτελέστε τακτικό έλεγχο επαλήθευσης των δεδομένων που θα χρησιμοποιεί ο Agent AI στις ροές εργασιών του. Βεβαιωθείτε ότι η πρόσβαση σε αυτά τα δεδομένα είναι ασφαλής και αλλάζει μόνο από αξιόπιστα άτομα για να αποφύγετε αυτού του τύπου την επίθεση.

### Αλυσιδωτά Σφάλματα

**Περιγραφή:** Οι Agents AI έχουν πρόσβαση σε διάφορα εργαλεία και υπηρεσίες για την ολοκλήρωση εργασιών. Σφάλματα που προκαλούνται από επιτιθέμενους μπορούν να οδηγήσουν σε αποτυχίες άλλων συστημάτων στα οποία ο Agent AI είναι συνδεδεμένος, προκαλώντας την επίθεση να γίνει εκτενέστερη και δυσκολότερη στην αντιμετώπιση.

**Μετριασμός:** Μια μέθοδος για να αποφύγετε αυτό είναι να λειτουργεί ο Agent AI σε περιορισμένο περιβάλλον, όπως εκτέλεση εργασιών μέσα σε ένα Docker container, για να αποτραπούν άμεσες επιθέσεις στο σύστημα. Η δημιουργία μηχανισμών επαναφοράς και λογικής επαναπροσπάθειας όταν ορισμένα συστήματα απαντούν με σφάλμα είναι ένας ακόμα τρόπος να αποτραπούν μεγαλύτερες αποτυχίες συστήματος.

## Ανθρώπινος στην Αλυσίδα (Human-in-the-Loop)

Ένας ακόμη αποτελεσματικός τρόπος να κατασκευάσετε συστήματα αξιόπιστων Agents AI είναι η χρήση του Human-in-the-loop. Αυτό δημιουργεί μια ροή όπου οι χρήστες μπορούν να παρέχουν ανατροφοδότηση στους Agents κατά τη διάρκεια της λειτουργίας. Οι χρήστες ουσιαστικά λειτουργούν ως agents σε ένα σύστημα πολλαπλών agents και παρέχοντας έγκριση ή τερματισμό της τρέχουσας διαδικασίας.

![Άνθρωπος στην Αλυσίδα](../../../translated_images/el/human-in-the-loop.5f0068a678f62f4f.webp)

Ακολουθεί ένα τμήμα κώδικα που χρησιμοποιεί το Microsoft Agent Framework για να δείξει πώς υλοποιείται αυτή η έννοια:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Δημιουργήστε τον πάροχο με έγκριση από άνθρωπο σε διαδικασία
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Δημιουργήστε τον πράκτορα με ένα βήμα έγκρισης από άνθρωπο
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

Η δημιουργία αξιόπιστων Agents AI απαιτεί προσεκτικό σχεδιασμό, στιβαρά μέτρα ασφαλείας και συνεχή επανάληψη. Με την υλοποίηση δομημένων συστημάτων meta prompting, την κατανόηση των δυνητικών απειλών και την εφαρμογή στρατηγικών μετριασμού, οι προγραμματιστές μπορούν να δημιουργήσουν Agents AI που είναι τόσο ασφαλείς όσο και αποτελεσματικοί. Επιπλέον, η ενσωμάτωση της προσέγγισης human-in-the-loop διασφαλίζει ότι οι Agents AI παραμένουν ευθυγραμμισμένοι με τις ανάγκες των χρηστών ενώ μειώνεται ο κίνδυνος. Καθώς η AI συνεχίζει να εξελίσσεται, η διατήρηση μιας προληπτικής στάσης στην ασφάλεια, την ιδιωτικότητα και τις ηθικές παραμέτρους θα είναι το κλειδί για την καλλιέργεια εμπιστοσύνης και αξιοπιστίας σε συστήματα που κινούνται από AI.

## Παραδείγματα Κώδικα

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Επίδειξη βήμα-βήμα του πλαισίου meta-prompt συστήματος μηνυμάτων.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Πύλες έγκρισης προεργασίας, ιεράρχηση κινδύνου και καταγραφή ελέγχου για αξιόπιστους agents.

### Έχετε Περισσότερες Ερωτήσεις για τη Δημιουργία Αξιόπιστων Agents AI;

Ενταχθείτε στο [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) για να συναντήσετε άλλους μαθητές, να παρακολουθήσετε ώρες γραφείου και να λάβετε απαντήσεις στις ερωτήσεις σας για Agents AI.

## Πρόσθετοι Πόροι

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Επισκόπηση Υπεύθυνης AI</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Αξιολόγηση μοντέλων γεννητικής AI και εφαρμογών AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Μηνύματα συστήματος ασφάλειας</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Πρότυπο Αξιολόγησης Κινδύνου</a>

## Προηγούμενο Μάθημα

[Agentic RAG](../05-agentic-rag/README.md)

## Επόμενο Μάθημα

[Σχέδιο Προγραμματισμού](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->