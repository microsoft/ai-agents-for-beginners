# Ανάπτυξη Υπηρεσίας Πράκτορα Microsoft Foundry

Σε αυτή την άσκηση, χρησιμοποιείτε τα εργαλεία Microsoft Foundry Agent Service στην [πύλη Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) για να δημιουργήσετε έναν πράκτορα για Κράτηση Πτήσεων. Ο πράκτορας θα μπορεί να αλληλεπιδρά με χρήστες και να παρέχει πληροφορίες σχετικά με πτήσεις.

## Προαπαιτούμενα

Για να ολοκληρώσετε αυτή την άσκηση, χρειάζεστε τα εξής:
1. Έναν λογαριασμό Azure με ενεργή συνδρομή. [Δημιουργήστε λογαριασμό δωρεάν](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
2. Χρειάζεστε δικαιώματα για να δημιουργήσετε ένα Microsoft Foundry hub ή να έχει δημιουργηθεί ένα για εσάς.
    - Αν ο ρόλος σας είναι Συνεργάτης (Contributor) ή Ιδιοκτήτης (Owner), μπορείτε να ακολουθήσετε τα βήματα σε αυτό τον οδηγό.

## Δημιουργία ενός Microsoft Foundry hub

> **Σημείωση:** Το Microsoft Foundry ήταν προηγουμένως γνωστό ως Azure AI Studio.

1. Ακολουθήστε αυτές τις οδηγίες από την [καταχώρηση ιστολογίου Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) για να δημιουργήσετε ένα Microsoft Foundry hub.
2. Όταν δημιουργηθεί το έργο σας, κλείστε τυχόν εμφανιζόμενες συμβουλές και εξετάστε τη σελίδα του έργου στην πύλη Microsoft Foundry, η οποία θα πρέπει να μοιάζει με την ακόλουθη εικόνα:

    ![Microsoft Foundry Project](../../../translated_images/el/azure-ai-foundry.88d0c35298348c2f.webp)

## Ανάπτυξη μοντέλου

1. Στο παράθυρο στα αριστερά για το έργο σας, στην ενότητα **My assets**, επιλέξτε τη σελίδα **Models + endpoints**.
2. Στη σελίδα **Models + endpoints**, στην καρτέλα **Model deployments**, στο μενού **+ Deploy model**, επιλέξτε **Deploy base model**.
3. Αναζητήστε το μοντέλο `gpt-5-mini` στη λίστα, και κατόπιν επιλέξτε και επιβεβαιώστε το.

    > **Σημείωση**: Η μείωση του TPM βοηθά στην αποφυγή υπερβολικής χρήσης του διαθέσιμου ορίου στη συνδρομή που χρησιμοποιείτε.

    ![Model Deployed](../../../translated_images/el/model-deployment.3749c53fb81e18fd.webp)

## Δημιουργία πράκτορα

Τώρα που έχετε αναπτύξει ένα μοντέλο, μπορείτε να δημιουργήσετε έναν πράκτορα. Ένας πράκτορας είναι ένα μοντέλο συνομιλιακής τεχνητής νοημοσύνης που μπορεί να χρησιμοποιηθεί για να αλληλεπιδρά με χρήστες.

1. Στο παράθυρο στα αριστερά για το έργο σας, στην ενότητα **Build & Customize**, επιλέξτε τη σελίδα **Agents**.
2. Κάντε κλικ στο **+ Create agent** για να δημιουργήσετε έναν νέο πράκτορα. Στο πλαίσιο διαλόγου **Agent Setup**:
    - Εισάγετε ένα όνομα για τον πράκτορα, όπως `FlightAgent`.
    - Βεβαιωθείτε ότι έχει επιλεγεί η ανάπτυξη μοντέλου `gpt-5-mini` που δημιουργήσατε προηγουμένως.
    - Ορίστε τις **Οδηγίες** σύμφωνα με το prompt που θέλετε να ακολουθήσει ο πράκτορας. Να ένα παράδειγμα:
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> Για ένα λεπτομερές prompt, μπορείτε να δείτε [αυτό το αποθετήριο](https://github.com/ShivamGoyal03/RoamMind) για περισσότερες πληροφορίες.
    
> Επιπλέον, μπορείτε να προσθέσετε **Knowledge Base** και **Ενέργειες** για να βελτιώσετε τις δυνατότητες του πράκτορα να παρέχει περισσότερες πληροφορίες και να εκτελεί αυτοματοποιημένες εργασίες βάσει αιτημάτων χρηστών. Για αυτή την άσκηση, μπορείτε να παραλείψετε αυτά τα βήματα.
    
![Agent Setup](../../../translated_images/el/agent-setup.9bbb8755bf5df672.webp)

3. Για να δημιουργήσετε έναν νέο πράκτορα πολλαπλής AI, απλώς κάντε κλικ στο **New Agent**. Ο νεοδημιουργημένος πράκτορας θα εμφανιστεί στη σελίδα Agents.


## Δοκιμή του πράκτορα

Μετά τη δημιουργία του πράκτορα, μπορείτε να τον δοκιμάσετε για να δείτε πώς ανταποκρίνεται στα αιτήματα των χρηστών στο περιβάλλον του Microsoft Foundry portal.

1. Στην κορυφή του παραθύρου **Setup** για τον πράκτορά σας, επιλέξτε **Try in playground**.
2. Στο παράθυρο **Playground**, μπορείτε να αλληλεπιδράσετε με τον πράκτορα πληκτρολογώντας ερωτήματα στο παράθυρο συνομιλίας. Για παράδειγμα, μπορείτε να ζητήσετε από τον πράκτορα να αναζητήσει πτήσεις από το Σιάτλ στη Νέα Υόρκη στις 28.

    > **Σημείωση**: Ο πράκτορας ενδέχεται να μην παρέχει ακριβείς απαντήσεις, καθώς δεν χρησιμοποιούνται πραγματικά δεδομένα σε πραγματικό χρόνο σε αυτή την άσκηση. Σκοπός είναι να δοκιμαστεί η ικανότητα του πράκτορα να κατανοεί και να ανταποκρίνεται σε αιτήματα χρηστών βάσει των δοθείσων οδηγιών.

    ![Agent Playground](../../../translated_images/el/agent-playground.dc146586de715010.webp)

3. Μετά τη δοκιμή του πράκτορα, μπορείτε να τον προσαρμόσετε περαιτέρω προσθέτοντας περισσότερες προθέσεις, δεδομένα εκπαίδευσης και ενέργειες για να βελτιώσετε τις δυνατότητές του.

## Καθαρισμός πόρων

Όταν ολοκληρώσετε τη δοκιμή του πράκτορα, μπορείτε να τον διαγράψετε για να αποφύγετε πρόσθετα έξοδα.
1. Ανοίξτε το [Azure portal](https://portal.azure.com) και δείτε τα περιεχόμενα της ομάδας πόρων όπου αναπτύξατε τους πόρους hub που χρησιμοποιήθηκαν σε αυτή την άσκηση.
2. Στη γραμμή εργαλείων, επιλέξτε **Delete resource group**.
3. Εισάγετε το όνομα της ομάδας πόρων και επιβεβαιώστε ότι θέλετε να το διαγράψετε.

## Πόροι

- [Τεκμηρίωση Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Πύλη Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Ξεκινώντας με Microsoft Foundry](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Βασικά στοιχεία των πρακτόρων AI στο Azure](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->