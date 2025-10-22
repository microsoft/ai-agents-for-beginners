<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T14:52:25+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "el"
}
-->
[![Αξιόπιστοι Πράκτορες Τεχνητής Νοημοσύνης](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.el.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Κάντε κλικ στην παραπάνω εικόνα για να παρακολουθήσετε το βίντεο αυτού του μαθήματος)_

# Δημιουργία Αξιόπιστων Πρακτόρων Τεχνητής Νοημοσύνης

## Εισαγωγή

Αυτό το μάθημα θα καλύψει:

- Πώς να δημιουργήσετε και να αναπτύξετε ασφαλείς και αποτελεσματικούς Πράκτορες Τεχνητής Νοημοσύνης.
- Σημαντικές παραμέτρους ασφαλείας κατά την ανάπτυξη Πρακτόρων Τεχνητής Νοημοσύνης.
- Πώς να διατηρήσετε την ιδιωτικότητα δεδομένων και χρηστών κατά την ανάπτυξη Πρακτόρων Τεχνητής Νοημοσύνης.

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα γνωρίζετε πώς να:

- Εντοπίζετε και να μετριάζετε κινδύνους κατά τη δημιουργία Πρακτόρων Τεχνητής Νοημοσύνης.
- Εφαρμόζετε μέτρα ασφαλείας για να διασφαλίσετε ότι τα δεδομένα και η πρόσβαση διαχειρίζονται σωστά.
- Δημιουργείτε Πράκτορες Τεχνητής Νοημοσύνης που διατηρούν την ιδιωτικότητα των δεδομένων και προσφέρουν ποιοτική εμπειρία χρήστη.

## Ασφάλεια

Ας ξεκινήσουμε εξετάζοντας πώς να δημιουργήσουμε ασφαλείς εφαρμογές πρακτόρων. Ασφάλεια σημαίνει ότι ο πράκτορας Τεχνητής Νοημοσύνης λειτουργεί όπως έχει σχεδιαστεί. Ως δημιουργοί εφαρμογών πρακτόρων, έχουμε μεθόδους και εργαλεία για να μεγιστοποιήσουμε την ασφάλεια:

### Δημιουργία Πλαισίου Μηνυμάτων Συστήματος

Αν έχετε δημιουργήσει ποτέ μια εφαρμογή Τεχνητής Νοημοσύνης χρησιμοποιώντας Μεγάλα Γλωσσικά Μοντέλα (LLMs), γνωρίζετε τη σημασία του σχεδιασμού ενός ισχυρού προτροπής συστήματος ή μηνύματος συστήματος. Αυτές οι προτροπές καθορίζουν τους κανόνες, τις οδηγίες και τις κατευθυντήριες γραμμές για το πώς το LLM θα αλληλεπιδρά με τον χρήστη και τα δεδομένα.

Για τους Πράκτορες Τεχνητής Νοημοσύνης, η προτροπή συστήματος είναι ακόμη πιο σημαντική, καθώς οι πράκτορες χρειάζονται εξαιρετικά συγκεκριμένες οδηγίες για να ολοκληρώσουν τις εργασίες που έχουμε σχεδιάσει για αυτούς.

Για να δημιουργήσουμε κλιμακούμενες προτροπές συστήματος, μπορούμε να χρησιμοποιήσουμε ένα πλαίσιο μηνυμάτων συστήματος για τη δημιουργία ενός ή περισσότερων πρακτόρων στην εφαρμογή μας:

![Δημιουργία Πλαισίου Μηνυμάτων Συστήματος](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.el.png)

#### Βήμα 1: Δημιουργία Μετα-Μηνύματος Συστήματος

Το μετα-μήνυμα θα χρησιμοποιηθεί από ένα LLM για να δημιουργήσει τις προτροπές συστήματος για τους πράκτορες που δημιουργούμε. Το σχεδιάζουμε ως πρότυπο ώστε να μπορούμε να δημιουργούμε αποτελεσματικά πολλούς πράκτορες, αν χρειαστεί.

Παρακάτω είναι ένα παράδειγμα μετα-μηνύματος συστήματος που θα δίναμε στο LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Βήμα 2: Δημιουργία Βασικής Προτροπής

Το επόμενο βήμα είναι να δημιουργήσετε μια βασική προτροπή για να περιγράψετε τον Πράκτορα Τεχνητής Νοημοσύνης. Θα πρέπει να περιλαμβάνει τον ρόλο του πράκτορα, τις εργασίες που θα ολοκληρώσει και οποιεσδήποτε άλλες ευθύνες του πράκτορα.

Παρακάτω είναι ένα παράδειγμα:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Βήμα 3: Παροχή Βασικού Μηνύματος Συστήματος στο LLM

Τώρα μπορούμε να βελτιστοποιήσουμε αυτό το μήνυμα συστήματος παρέχοντας το μετα-μήνυμα συστήματος ως μήνυμα συστήματος και το βασικό μήνυμα συστήματος.

Αυτό θα παράγει ένα μήνυμα συστήματος που είναι καλύτερα σχεδιασμένο για την καθοδήγηση των πρακτόρων Τεχνητής Νοημοσύνης:

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

Η αξία αυτού του πλαισίου μηνυμάτων συστήματος είναι να διευκολύνει τη δημιουργία μηνυμάτων συστήματος για πολλούς πράκτορες, καθώς και τη βελτίωση των μηνυμάτων συστήματος με την πάροδο του χρόνου. Είναι σπάνιο να έχετε ένα μήνυμα συστήματος που λειτουργεί τέλεια από την πρώτη φορά για την πλήρη περίπτωση χρήσης σας. Η δυνατότητα να κάνετε μικρές προσαρμογές και βελτιώσεις αλλάζοντας το βασικό μήνυμα συστήματος και εκτελώντας το μέσω του συστήματος θα σας επιτρέψει να συγκρίνετε και να αξιολογήσετε τα αποτελέσματα.

## Κατανόηση Απειλών

Για να δημιουργήσετε αξιόπιστους πράκτορες Τεχνητής Νοημοσύνης, είναι σημαντικό να κατανοήσετε και να μετριάσετε τους κινδύνους και τις απειλές προς τον πράκτορα σας. Ας δούμε μερικές από τις διαφορετικές απειλές προς τους πράκτορες Τεχνητής Νοημοσύνης και πώς μπορείτε να προγραμματίσετε και να προετοιμαστείτε καλύτερα για αυτές.

![Κατανόηση Απειλών](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.el.png)

### Εργασία και Οδηγίες

**Περιγραφή:** Οι επιτιθέμενοι προσπαθούν να αλλάξουν τις οδηγίες ή τους στόχους του πράκτορα Τεχνητής Νοημοσύνης μέσω προτροπών ή χειραγώγησης εισόδων.

**Μετριασμός**: Εκτελέστε ελέγχους επικύρωσης και φίλτρα εισόδου για να ανιχνεύσετε πιθανώς επικίνδυνες προτροπές πριν επεξεργαστούν από τον πράκτορα Τεχνητής Νοημοσύνης. Δεδομένου ότι αυτές οι επιθέσεις συνήθως απαιτούν συχνή αλληλεπίδραση με τον πράκτορα, ο περιορισμός του αριθμού των γύρων σε μια συνομιλία είναι ένας άλλος τρόπος για να αποτρέψετε αυτού του είδους τις επιθέσεις.

### Πρόσβαση σε Κρίσιμα Συστήματα

**Περιγραφή**: Αν ένας πράκτορας Τεχνητής Νοημοσύνης έχει πρόσβαση σε συστήματα και υπηρεσίες που αποθηκεύουν ευαίσθητα δεδομένα, οι επιτιθέμενοι μπορούν να παραβιάσουν την επικοινωνία μεταξύ του πράκτορα και αυτών των υπηρεσιών. Αυτές μπορεί να είναι άμεσες επιθέσεις ή έμμεσες προσπάθειες για την απόκτηση πληροφοριών σχετικά με αυτά τα συστήματα μέσω του πράκτορα.

**Μετριασμός**: Οι πράκτορες Τεχνητής Νοημοσύνης θα πρέπει να έχουν πρόσβαση σε συστήματα μόνο όταν είναι απαραίτητο για να αποτραπούν αυτού του είδους οι επιθέσεις. Η επικοινωνία μεταξύ του πράκτορα και του συστήματος θα πρέπει επίσης να είναι ασφαλής. Η εφαρμογή ελέγχου ταυτότητας και ελέγχου πρόσβασης είναι ένας άλλος τρόπος για την προστασία αυτών των πληροφοριών.

### Υπερφόρτωση Πόρων και Υπηρεσιών

**Περιγραφή:** Οι πράκτορες Τεχνητής Νοημοσύνης μπορούν να έχουν πρόσβαση σε διάφορα εργαλεία και υπηρεσίες για να ολοκληρώσουν εργασίες. Οι επιτιθέμενοι μπορούν να χρησιμοποιήσουν αυτή τη δυνατότητα για να επιτεθούν σε αυτές τις υπηρεσίες στέλνοντας μεγάλο όγκο αιτημάτων μέσω του πράκτορα Τεχνητής Νοημοσύνης, κάτι που μπορεί να οδηγήσει σε αποτυχίες συστημάτων ή υψηλό κόστος.

**Μετριασμός:** Εφαρμόστε πολιτικές για να περιορίσετε τον αριθμό των αιτημάτων που μπορεί να κάνει ένας πράκτορας Τεχνητής Νοημοσύνης σε μια υπηρεσία. Ο περιορισμός του αριθμού των γύρων συνομιλίας και αιτημάτων προς τον πράκτορα Τεχνητής Νοημοσύνης είναι ένας άλλος τρόπος για να αποτρέψετε αυτού του είδους τις επιθέσεις.

### Δηλητηρίαση Βάσης Γνώσεων

**Περιγραφή:** Αυτός ο τύπος επίθεσης δεν στοχεύει άμεσα τον πράκτορα Τεχνητής Νοημοσύνης, αλλά στοχεύει τη βάση γνώσεων και άλλες υπηρεσίες που θα χρησιμοποιήσει ο πράκτορας. Αυτό μπορεί να περιλαμβάνει τη διαφθορά των δεδομένων ή των πληροφοριών που θα χρησιμοποιήσει ο πράκτορας για να ολοκληρώσει μια εργασία, οδηγώντας σε προκατειλημμένες ή ανεπιθύμητες απαντήσεις προς τον χρήστη.

**Μετριασμός:** Εκτελέστε τακτική επαλήθευση των δεδομένων που θα χρησιμοποιεί ο πράκτορας Τεχνητής Νοημοσύνης στις ροές εργασίας του. Διασφαλίστε ότι η πρόσβαση σε αυτά τα δεδομένα είναι ασφαλής και ότι αλλάζει μόνο από αξιόπιστα άτομα για να αποφύγετε αυτού του είδους τις επιθέσεις.

### Αλυσιδωτά Σφάλματα

**Περιγραφή:** Οι πράκτορες Τεχνητής Νοημοσύνης έχουν πρόσβαση σε διάφορα εργαλεία και υπηρεσίες για να ολοκληρώσουν εργασίες. Σφάλματα που προκαλούνται από επιτιθέμενους μπορούν να οδηγήσουν σε αποτυχίες άλλων συστημάτων με τα οποία είναι συνδεδεμένος ο πράκτορας, καθιστώντας την επίθεση πιο εκτεταμένη και δύσκολη στην αντιμετώπιση.

**Μετριασμός**: Ένας τρόπος για να αποφύγετε αυτό είναι να λειτουργεί ο πράκτορας Τεχνητής Νοημοσύνης σε ένα περιορισμένο περιβάλλον, όπως η εκτέλεση εργασιών σε ένα Docker container, για να αποτρέψετε άμεσες επιθέσεις στο σύστημα. Η δημιουργία μηχανισμών εφεδρείας και λογικής επανεκτέλεσης όταν ορισμένα συστήματα ανταποκρίνονται με σφάλμα είναι ένας άλλος τρόπος για να αποτρέψετε μεγαλύτερες αποτυχίες συστημάτων.

## Ανθρώπινη Παρέμβαση

Ένας άλλος αποτελεσματικός τρόπος για να δημιουργήσετε αξιόπιστα συστήματα Πρακτόρων Τεχνητής Νοημοσύνης είναι η χρήση της Ανθρώπινης Παρέμβασης. Αυτό δημιουργεί μια ροή όπου οι χρήστες μπορούν να παρέχουν ανατροφοδότηση στους πράκτορες κατά τη διάρκεια της εκτέλεσης. Οι χρήστες ουσιαστικά λειτουργούν ως πράκτορες σε ένα σύστημα πολλαπλών πρακτόρων, παρέχοντας έγκριση ή τερματισμό της τρέχουσας διαδικασίας.

![Ανθρώπινη Παρέμβαση](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.el.png)

Παρακάτω είναι ένα απόσπασμα κώδικα που χρησιμοποιεί το AutoGen για να δείξει πώς εφαρμόζεται αυτή η ιδέα:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Συμπέρασμα

Η δημιουργία αξιόπιστων πρακτόρων Τεχνητής Νοημοσύνης απαιτεί προσεκτικό σχεδιασμό, ισχυρά μέτρα ασφαλείας και συνεχή βελτίωση. Με την εφαρμογή δομημένων συστημάτων μετα-προτροπών, την κατανόηση πιθανών απειλών και την εφαρμογή στρατηγικών μετριασμού, οι προγραμματιστές μπορούν να δημιουργήσουν πράκτορες Τεχνητής Νοημοσύνης που είναι τόσο ασφαλείς όσο και αποτελεσματικοί. Επιπλέον, η ενσωμάτωση μιας προσέγγισης με ανθρώπινη παρέμβαση διασφαλίζει ότι οι πράκτορες Τεχνητής Νοημοσύνης παραμένουν ευθυγραμμισμένοι με τις ανάγκες των χρηστών, ενώ ελαχιστοποιούνται οι κίνδυνοι. Καθώς η Τεχνητή Νοημοσύνη συνεχίζει να εξελίσσεται, η διατήρηση μιας προληπτικής στάσης σχετικά με την ασφάλεια, την ιδιωτικότητα και τις ηθικές παραμέτρους θα είναι το κλειδί για την ενίσχυση της εμπιστοσύνης και της αξιοπιστίας στα συστήματα που βασίζονται στην Τεχνητή Νοημοσύνη.

### Έχετε περισσότερες ερωτήσεις σχετικά με τη δημιουργία αξιόπιστων Πρακτόρων Τεχνητής Νοημοσύνης;

Γίνετε μέλος στο [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) για να συναντήσετε άλλους μαθητές, να παρακολουθήσετε ώρες γραφείου και να λάβετε απαντήσεις στις ερωτήσεις σας σχετικά με τους Πράκτορες Τεχνητής Νοημοσύνης.

## Πρόσθετοι Πόροι

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Επισκόπηση Υπεύθυνης Τεχνητής Νοημοσύνης</a>  
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Αξιολόγηση μοντέλων γενετικής Τεχνητής Νοημοσύνης και εφαρμογών Τεχνητής Νοημοσύνης</a>  
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Μηνύματα συστήματος ασφαλείας</a>  
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Πρότυπο Αξιολόγησης Κινδύνων</a>  

## Προηγούμενο Μάθημα

[Agentic RAG](../05-agentic-rag/README.md)

## Επόμενο Μάθημα

[Σχεδιαστικό Μοτίβο Προγραμματισμού](../07-planning-design/README.md)

---

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.