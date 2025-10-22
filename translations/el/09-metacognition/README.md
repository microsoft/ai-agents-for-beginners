<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f0deef171fc3a68d5d3d770a8bfb03d",
  "translation_date": "2025-08-29T14:47:04+00:00",
  "source_file": "09-metacognition/README.md",
  "language_code": "el"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-9-thumbnail.38059e8af1a5b71d890c92f576f933c6a307c691339dca7e8ca6ea75a8d857a1.el.png)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Κάντε κλικ στην παραπάνω εικόνα για να παρακολουθήσετε το βίντεο αυτού του μαθήματος)_
# Μεταγνώση στους Πράκτορες Τεχνητής Νοημοσύνης

## Εισαγωγή

Καλώς ήρθατε στο μάθημα για τη μεταγνώση στους πράκτορες τεχνητής νοημοσύνης! Αυτό το κεφάλαιο είναι σχεδιασμένο για αρχάριους που ενδιαφέρονται να μάθουν πώς οι πράκτορες τεχνητής νοημοσύνης μπορούν να σκέφτονται για τις δικές τους διαδικασίες σκέψης. Μέχρι το τέλος αυτού του μαθήματος, θα κατανοείτε βασικές έννοιες και θα είστε εξοπλισμένοι με πρακτικά παραδείγματα για να εφαρμόσετε τη μεταγνώση στο σχεδιασμό πρακτόρων τεχνητής νοημοσύνης.

## Στόχοι Μάθησης

Μετά την ολοκλήρωση αυτού του μαθήματος, θα μπορείτε να:

1. Κατανοήσετε τις επιπτώσεις των βρόχων λογικής στους ορισμούς πρακτόρων.
2. Χρησιμοποιήσετε τεχνικές σχεδιασμού και αξιολόγησης για να βοηθήσετε τους πράκτορες να αυτοδιορθώνονται.
3. Δημιουργήσετε δικούς σας πράκτορες που μπορούν να χειρίζονται κώδικα για την εκτέλεση εργασιών.

## Εισαγωγή στη Μεταγνώση

Η μεταγνώση αναφέρεται στις ανώτερες γνωστικές διαδικασίες που περιλαμβάνουν τη σκέψη για τη δική μας σκέψη. Για τους πράκτορες τεχνητής νοημοσύνης, αυτό σημαίνει την ικανότητα να αξιολογούν και να προσαρμόζουν τις ενέργειές τους με βάση την αυτογνωσία και τις προηγούμενες εμπειρίες. Η μεταγνώση, ή "σκέψη για τη σκέψη," είναι μια σημαντική έννοια στην ανάπτυξη πρακτόρων τεχνητής νοημοσύνης. Περιλαμβάνει την ικανότητα των συστημάτων τεχνητής νοημοσύνης να γνωρίζουν τις δικές τους εσωτερικές διαδικασίες και να μπορούν να παρακολουθούν, να ρυθμίζουν και να προσαρμόζουν τη συμπεριφορά τους ανάλογα. Όπως κάνουμε κι εμείς όταν "διαβάζουμε το δωμάτιο" ή εξετάζουμε ένα πρόβλημα. Αυτή η αυτογνωσία μπορεί να βοηθήσει τα συστήματα τεχνητής νοημοσύνης να λαμβάνουν καλύτερες αποφάσεις, να εντοπίζουν λάθη και να βελτιώνουν την απόδοσή τους με την πάροδο του χρόνου - συνδέοντας ξανά με το τεστ Turing και τη συζήτηση για το αν η τεχνητή νοημοσύνη θα κυριαρχήσει.

Στο πλαίσιο των πρακτόρων τεχνητής νοημοσύνης, η μεταγνώση μπορεί να βοηθήσει στην αντιμετώπιση αρκετών προκλήσεων, όπως:
- Διαφάνεια: Εξασφάλιση ότι τα συστήματα τεχνητής νοημοσύνης μπορούν να εξηγήσουν τη λογική και τις αποφάσεις τους.
- Λογική: Ενίσχυση της ικανότητας των συστημάτων τεχνητής νοημοσύνης να συνθέτουν πληροφορίες και να λαμβάνουν σωστές αποφάσεις.
- Προσαρμογή: Επιτρέποντας στα συστήματα τεχνητής νοημοσύνης να προσαρμόζονται σε νέα περιβάλλοντα και μεταβαλλόμενες συνθήκες.
- Αντίληψη: Βελτίωση της ακρίβειας των συστημάτων τεχνητής νοημοσύνης στην αναγνώριση και ερμηνεία δεδομένων από το περιβάλλον τους.

### Τι είναι η Μεταγνώση;

Η μεταγνώση, ή "σκέψη για τη σκέψη," είναι μια ανώτερη γνωστική διαδικασία που περιλαμβάνει την αυτογνωσία και την αυτορρύθμιση των γνωστικών διαδικασιών. Στον τομέα της τεχνητής νοημοσύνης, η μεταγνώση δίνει τη δυνατότητα στους πράκτορες να αξιολογούν και να προσαρμόζουν τις στρατηγικές και τις ενέργειές τους, οδηγώντας σε βελτιωμένες ικανότητες επίλυσης προβλημάτων και λήψης αποφάσεων. Κατανοώντας τη μεταγνώση, μπορείτε να σχεδιάσετε πράκτορες τεχνητής νοημοσύνης που είναι όχι μόνο πιο έξυπνοι αλλά και πιο προσαρμοστικοί και αποδοτικοί. Σε μια πραγματική μεταγνώση, θα βλέπατε την τεχνητή νοημοσύνη να σκέφτεται ρητά για τη δική της λογική.

Παράδειγμα: «Προτίμησα φθηνότερες πτήσεις επειδή... μπορεί να χάνω απευθείας πτήσεις, οπότε ας το ξαναελέγξω.»
Παρακολουθώντας πώς ή γιατί επέλεξε μια συγκεκριμένη διαδρομή.
- Σημειώνοντας ότι έκανε λάθη επειδή βασίστηκε υπερβολικά στις προτιμήσεις του χρήστη από την προηγούμενη φορά, οπότε τροποποιεί τη στρατηγική λήψης αποφάσεων και όχι μόνο την τελική πρόταση.
- Διαγνώσκοντας μοτίβα όπως, «Όποτε βλέπω τον χρήστη να αναφέρει "πολύ κόσμο," δεν πρέπει μόνο να αφαιρώ ορισμένα αξιοθέατα αλλά και να αναθεωρώ τη μέθοδο επιλογής "κορυφαίων αξιοθέατων" αν πάντα κατατάσσω με βάση τη δημοτικότητα.»

### Σημασία της Μεταγνώσης στους Πράκτορες Τεχνητής Νοημοσύνης

Η μεταγνώση παίζει κρίσιμο ρόλο στο σχεδιασμό πρακτόρων τεχνητής νοημοσύνης για διάφορους λόγους:

![Σημασία της Μεταγνώσης](../../../translated_images/importance-of-metacognition.b381afe9aae352f7734c8628ea3f4b23084634b791c5a120c76a02bb7eeeb7ec.el.png)

- Αυτοαντανάκλαση: Οι πράκτορες μπορούν να αξιολογούν την απόδοσή τους και να εντοπίζουν τομείς για βελτίωση.
- Προσαρμοστικότητα: Οι πράκτορες μπορούν να τροποποιούν τις στρατηγικές τους με βάση προηγούμενες εμπειρίες και μεταβαλλόμενα περιβάλλοντα.
- Διόρθωση Λαθών: Οι πράκτορες μπορούν να εντοπίζουν και να διορθώνουν λάθη αυτόνομα, οδηγώντας σε πιο ακριβή αποτελέσματα.
- Διαχείριση Πόρων: Οι πράκτορες μπορούν να βελτιστοποιούν τη χρήση πόρων, όπως ο χρόνος και η υπολογιστική ισχύς, μέσω σχεδιασμού και αξιολόγησης των ενεργειών τους.

## Συστατικά ενός Πράκτορα Τεχνητής Νοημοσύνης

Πριν εμβαθύνουμε στις μεταγνωστικές διαδικασίες, είναι απαραίτητο να κατανοήσουμε τα βασικά συστατικά ενός πράκτορα τεχνητής νοημοσύνης. Ένας πράκτορας τεχνητής νοημοσύνης συνήθως αποτελείται από:

- Προσωπικότητα: Η προσωπικότητα και τα χαρακτηριστικά του πράκτορα, που καθορίζουν πώς αλληλεπιδρά με τους χρήστες.
- Εργαλεία: Οι δυνατότητες και οι λειτουργίες που μπορεί να εκτελέσει ο πράκτορας.
- Δεξιότητες: Η γνώση και η εξειδίκευση που διαθέτει ο πράκτορας.

Αυτά τα συστατικά συνεργάζονται για να δημιουργήσουν μια "μονάδα εξειδίκευσης" που μπορεί να εκτελεί συγκεκριμένες εργασίες.

**Παράδειγμα**:
Σκεφτείτε έναν ταξιδιωτικό πράκτορα, μια υπηρεσία που όχι μόνο σχεδιάζει τις διακοπές σας αλλά και προσαρμόζει τη διαδρομή της με βάση δεδομένα σε πραγματικό χρόνο και εμπειρίες προηγούμενων πελατών.

### Παράδειγμα: Μεταγνώση σε Υπηρεσία Ταξιδιωτικού Πράκτορα

Φανταστείτε ότι σχεδιάζετε μια υπηρεσία ταξιδιωτικού πράκτορα που υποστηρίζεται από τεχνητή νοημοσύνη. Αυτός ο πράκτορας, "Ταξιδιωτικός Πράκτορας," βοηθά τους χρήστες να σχεδιάσουν τις διακοπές τους. Για να ενσωματώσετε τη μεταγνώση, ο Ταξιδιωτικός Πράκτορας πρέπει να αξιολογεί και να προσαρμόζει τις ενέργειές του με βάση την αυτογνωσία και τις προηγούμενες εμπειρίες. Να πώς μπορεί να παίξει ρόλο η μεταγνώση:

#### Τρέχουσα Εργασία

Η τρέχουσα εργασία είναι να βοηθήσει έναν χρήστη να σχεδιάσει ένα ταξίδι στο Παρίσι.

#### Βήματα για την Ολοκλήρωση της Εργασίας

1. **Συλλογή Προτιμήσεων Χρήστη**: Ρωτήστε τον χρήστη για τις ημερομηνίες ταξιδιού, τον προϋπολογισμό, τα ενδιαφέροντα (π.χ. μουσεία, κουζίνα, ψώνια) και τυχόν συγκεκριμένες απαιτήσεις.
2. **Ανάκτηση Πληροφοριών**: Αναζητήστε επιλογές πτήσεων, καταλυμάτων, αξιοθέατων και εστιατορίων που ταιριάζουν στις προτιμήσεις του χρήστη.
3. **Δημιουργία Προτάσεων**: Παρέχετε ένα εξατομικευμένο δρομολόγιο με λεπτομέρειες πτήσεων, κρατήσεις ξενοδοχείων και προτεινόμενες δραστηριότητες.
4. **Προσαρμογή με Βάση τα Σχόλια**: Ζητήστε από τον χρήστη σχόλια για τις προτάσεις και κάντε τις απαραίτητες προσαρμογές.

#### Απαιτούμενοι Πόροι

- Πρόσβαση σε βάσεις δεδομένων κρατήσεων πτήσεων και ξενοδοχείων.
- Πληροφορίες για αξιοθέατα και εστιατόρια στο Παρίσι.
- Δεδομένα σχολίων χρηστών από προηγούμενες αλληλεπιδράσεις.

#### Εμπειρία και Αυτοαντανάκλαση

Ο Ταξιδιωτικός Πράκτορας χρησιμοποιεί τη μεταγνώση για να αξιολογεί την απόδοσή του και να μαθαίνει από προηγούμενες εμπειρίες. Για παράδειγμα:

1. **Ανάλυση Σχολίων Χρηστών**: Ο Ταξιδιωτικός Πράκτορας εξετάζει τα σχόλια των χρηστών για να καθορίσει ποιες προτάσεις ήταν επιτυχημένες και ποιες όχι. Προσαρμόζει τις μελλοντικές προτάσεις ανάλογα.
2. **Προσαρμοστικότητα**: Αν ένας χρήστης έχει αναφέρει προηγουμένως ότι δεν του αρέσουν τα πολυσύχναστα μέρη, ο Ταξιδιωτικός Πράκτορας θα αποφύγει να προτείνει δημοφιλή τουριστικά σημεία κατά τις ώρες αιχμής στο μέλλον.
3. **Διόρθωση Λαθών**: Αν ο Ταξιδιωτικός Πράκτορας έκανε ένα λάθος σε μια προηγούμενη κράτηση, όπως το να προτείνει ένα ξενοδοχείο που ήταν πλήρες, μαθαίνει να ελέγχει τη διαθεσιμότητα πιο προσεκτικά πριν κάνει προτάσεις.

#### Πρακτικό Παράδειγμα για Προγραμματιστές

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Search for flights, hotels, and attractions based on preferences
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analyze feedback and adjust future recommendations
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Γιατί Έχει Σημασία η Μεταγνώση

- **Αυτοαντανάκλαση**: Οι πράκτορες μπορούν να αναλύουν την απόδοσή τους και να εντοπίζουν τομείς για βελτίωση.
- **Προσαρμοστικότητα**: Οι πράκτορες μπορούν να τροποποιούν στρατηγικές με βάση σχόλια και μεταβαλλόμενες συνθήκες.
- **Διόρθωση Λαθών**: Οι πράκτορες μπορούν να εντοπίζουν και να διορθώνουν λάθη αυτόνομα.
- **Διαχείριση Πόρων**: Οι πράκτορες μπορούν να βελτιστοποιούν τη χρήση πόρων, όπως ο χρόνος και η υπολογιστική ισχύς.

Με την ενσωμάτωση της μεταγνώσης, ο Ταξιδιωτικός Πράκτορας μπορεί να παρέχει πιο εξατομικευμένες και ακριβείς ταξιδιωτικές προτάσεις, βελτιώνοντας τη συνολική εμπειρία του χρήστη.

---

## 2. Σχεδιασμός στους Πράκτορες

Ο σχεδιασμός είναι ένα κρίσιμο στοιχείο της συμπεριφοράς των πρακτόρων τεχνητής νοημοσύνης. Περιλαμβάνει τον καθορισμό των βημάτων που απαιτούνται για την επίτευξη ενός στόχου, λαμβάνοντας υπόψη την τρέχουσα κατάσταση, τους πόρους και τα πιθανά εμπόδια.

### Στοιχεία Σχεδιασμού

- **Τρέχουσα Εργασία**: Ορίστε την εργασία με σαφήνεια.
- **Βήματα για την Ολοκλήρωση της Εργασίας**: Διαχωρίστε την εργασία σε διαχειρίσιμα βήματα.
- **Απαιτούμενοι Πόροι**: Προσδιορίστε τους απαραίτητους πόρους.
- **Εμπειρία**: Χρησιμοποιήστε προηγούμενες εμπειρίες για να ενημερώσετε τον σχεδιασμό.

**Παράδειγμα**:
Ακολουθούν τα βήματα που πρέπει να ακολουθήσει ο Ταξιδιωτικός Πράκτορας για να βοηθήσει έναν χρήστη να σχεδιάσει το ταξίδι του αποτελεσματικά:

### Βήματα για τον Ταξιδιωτικό Πράκτορα

1. **Συλλογή Προτιμήσεων Χρήστη**
   - Ρωτήστε τον χρήστη για λεπτομέρειες σχετικά με τις ημερομηνίες ταξιδιού, τον προϋπολογισμό, τα ενδιαφέροντα και τυχόν συγκεκριμένες απαιτήσεις.
   - Παραδείγματα: "Πότε σκοπεύετε να ταξιδέψετε;" "Ποιο είναι το εύρος του προϋπολογισμού σας;" "Τι δραστηριότητες απολαμβάνετε στις διακοπές σας;"

2. **Ανάκτηση Πληροφοριών**
   - Αναζητήστε σχετικές ταξιδιωτικές επιλογές με βάση τις προτιμήσεις του χρήστη.
   - **Πτήσεις**: Αναζητήστε διαθέσιμες πτήσεις εντός του προϋπολογισμού και των προτιμώμενων ημερομηνιών ταξιδιού.
   - **Καταλύματα**: Βρείτε ξενοδοχεία ή ενοικιαζόμενα ακίνητα που ταιριάζουν στις προτιμήσεις του χρήστη για τοποθεσία, τιμή και ανέσεις.
   - **Αξιοθέατα και Εστιατόρια**: Εντοπίστε δημοφιλή αξιοθέατα, δραστηριότητες και επιλογές φαγητού που ευθυγραμμίζονται με τα ενδιαφέροντα του χρήστη.

3. **Δημιουργία Προτάσεων**
   - Συγκεντρώστε τις ανακτηθείσες πληροφορίες σε ένα εξατομικευμένο δρομολόγιο.
   - Παρέχετε λεπτομέρειες όπως επιλογές πτήσεων, κρατήσεις ξενοδοχείων και προτεινόμενες δραστηριότητες, φροντίζοντας να προσαρμόσετε τις προτάσεις στις προτιμήσεις του χρήστη.

4. **Παρουσίαση Δρομολογίου στον Χρήστη**
   - Μοιραστείτε το προτεινόμενο δρομολόγιο με τον χρήστη για την ανασκόπησή του.
   - Παράδειγμα: "Ακολουθεί ένα προτεινόμενο δρομολόγιο για το ταξίδι σας στο Παρίσι. Περιλαμβάνει λεπτομέρειες πτήσεων, κρατήσεις ξενοδοχείων και μια λίστα με προτεινόμενες δραστηριότητες και εστιατόρια. Πείτε μου τη γνώμη σας!"

5. **Συλλογή Σχολίων**
   - Ζητήστε από τον χρήστη σχόλια για το προτεινόμενο δρομολόγιο.
   - Παραδείγματα: "Σας αρέσουν οι επιλογές πτήσεων;" "Είναι το ξενοδοχείο κατάλληλο για τις ανάγκες σας;" "Υπάρχουν δραστηριότητες που θα θέλατε να προσθέσετε ή να αφαιρέσετε;"

6. **Προσαρμογή με Βάση τα Σχόλια**
   - Τροποποιήστε το δρομολόγιο με βάση τα σχόλια του χρήστη.
   - Κάντε τις απαραίτητες αλλαγές στις προτάσεις πτήσεων, καταλυμάτων και δραστηριοτήτων για να ταιριάζουν καλύτερα στις προτιμήσεις του χρήστη.

7. **Τελική Επιβεβαίωση**

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Example usage
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### Προληπτική Φόρτωση Πλαισίου

Η Προληπτική Φόρτωση Πλαισίου περιλαμβάνει τη φόρτωση σχετικών πληροφοριών ή πλαισίου στο μοντέλο πριν από την επεξεργασία ενός ερωτήματος. Αυτό σημαίνει ότι το μοντέλο έχει πρόσβαση σε αυτές τις πληροφορίες από την αρχή, κάτι που μπορεί να το βοηθήσει να παράγει πιο ενημερωμένες απαντήσεις χωρίς να χρειάζεται να ανακτήσει πρόσθετα δεδομένα κατά τη διαδικασία.

Ακολουθεί ένα απλοποιημένο παράδειγμα για το πώς μπορεί να μοιάζει η προληπτική φόρτωση πλαισίου σε μια εφαρμογή ταξιδιωτικού πράκτορα με Python:

```python
class TravelAgent:
    def __init__(self):
        # Pre-load popular destinations and their information
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Fetch destination information from pre-loaded context
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Example usage
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Επεξήγηση

1. **Αρχικοποίηση (μέθοδος `__init__`)**: Η κλάση `TravelAgent` προφορτώνει ένα λεξικό που περιέχει πληροφορίες για δημοφιλείς προορισμούς όπως το Παρίσι, το Τόκιο, η Νέα Υόρκη και το Σίδνεϊ. Αυτό το λεξικό περιλαμβάνει λεπτομέρειες όπως η χώρα, το νόμισμα, η γλώσσα και τα κύρια αξιοθέατα για κάθε προορισμό.

2. **Ανάκτηση Πληροφοριών (μέθοδος `get_destination_info`)**: Όταν ένας χρήστης ρωτά για έναν συγκεκριμένο προορισμό, η μέθοδος `get_destination_info` ανακτά τις σχετικές πληροφορίες από το προφορτωμένο λεξικό πλαισίου.

Με την προφόρτωση του πλαισίου, η εφαρμογή του ταξιδιωτικού πράκτορα μπορεί να απαντά γρήγορα στα ερωτήματα των χρηστών χωρίς να χρειάζεται να ανακτήσει αυτές τις πληροφορίες από εξωτερική πηγή σε πραγματικό χρόνο. Αυτό καθιστά την εφαρμογή πιο αποτελεσματική και γρήγορη.

### Εκκίνηση Σχεδίου με Στόχο Πριν την Επανάληψη

Η εκκίνηση ενός σχεδίου με στόχο περιλαμβάνει την έναρξη με έναν σαφή στόχο ή επιθυμητό αποτέλεσμα. Ορίζοντας αυτόν τον στόχο εκ των προτέρων, το μοντέλο μπορεί να τον χρησιμοποιήσει ως καθοδηγητική αρχή καθ' όλη τη διάρκεια της επαναληπτικής διαδικασίας. Αυτό βοηθά να διασφαλιστεί ότι κάθε επανάληψη πλησιάζει περισσότερο στην επίτευξη του επιθυμητού αποτελέσματος, καθιστώντας τη διαδικασία πιο αποτελεσματική και εστιασμένη.

Ακολουθεί ένα παράδειγμα για το πώς μπορεί να εκκινήσει ένα ταξιδιωτικό σχέδιο με στόχο πριν την επανάληψη για έναν ταξιδιωτικό πράκτορα με Python:

### Σενάριο

Ένας ταξιδιωτικός πράκτορας θέλει να σχεδιάσει ένα εξατομικευμένο ταξίδι για έναν πελάτη. Ο στόχος είναι να δημιουργηθεί ένα ταξιδιωτικό πρόγραμμα που μεγιστοποιεί την ικανοποίηση του πελάτη βάσει των προτιμήσεων και του προϋπολογισμού του.

### Βήματα

1. Ορισμός των προτιμήσεων και του προϋπολογισμού του πελάτη.
2. Εκκίνηση του αρχικού σχεδίου βάσει αυτών των προτιμήσεων.
3. Επανάληψη για τη βελτίωση του σχεδίου, με στόχο τη μεγιστοποίηση της ικανοποίησης του πελάτη.

#### Κώδικας Python

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Example usage
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### Επεξήγηση Κώδικα

1. **Αρχικοποίηση (μέθοδος `__init__`)**: Η κλάση `TravelAgent` αρχικοποιείται με μια λίστα πιθανών προορισμών, καθένας από τους οποίους έχει χαρακτηριστικά όπως όνομα, κόστος και τύπο δραστηριότητας.

2. **Εκκίνηση Σχεδίου (μέθοδος `bootstrap_plan`)**: Αυτή η μέθοδος δημιουργεί ένα αρχικό ταξιδιωτικό σχέδιο βάσει των προτιμήσεων και του προϋπολογισμού του πελάτη. Εξετάζει τη λίστα των προορισμών και τους προσθέτει στο σχέδιο αν ταιριάζουν στις προτιμήσεις του πελάτη και είναι εντός του προϋπολογισμού.

3. **Ταίριασμα Προτιμήσεων (μέθοδος `match_preferences`)**: Αυτή η μέθοδος ελέγχει αν ένας προορισμός ταιριάζει στις προτιμήσεις του πελάτη.

4. **Επανάληψη Σχεδίου (μέθοδος `iterate_plan`)**: Αυτή η μέθοδος βελτιώνει το αρχικό σχέδιο προσπαθώντας να αντικαταστήσει κάθε προορισμό στο σχέδιο με μια καλύτερη επιλογή, λαμβάνοντας υπόψη τις προτιμήσεις και τους περιορισμούς του προϋπολογισμού του πελάτη.

5. **Υπολογισμός Κόστους (μέθοδος `calculate_cost`)**: Αυτή η μέθοδος υπολογίζει το συνολικό κόστος του τρέχοντος σχεδίου, συμπεριλαμβανομένου ενός πιθανού νέου προορισμού.

#### Παράδειγμα Χρήσης

- **Αρχικό Σχέδιο**: Ο ταξιδιωτικός πράκτορας δημιουργεί ένα αρχικό σχέδιο βάσει των προτιμήσεων του πελάτη για αξιοθέατα και έναν προϋπολογισμό $2000.
- **Βελτιωμένο Σχέδιο**: Ο ταξιδιωτικός πράκτορας επαναλαμβάνει το σχέδιο, βελτιστοποιώντας το για τις προτιμήσεις και τον προϋπολογισμό του πελάτη.

Με την εκκίνηση του σχεδίου με έναν σαφή στόχο (π.χ. τη μεγιστοποίηση της ικανοποίησης του πελάτη) και την επανάληψη για τη βελτίωση του σχεδίου, ο ταξιδιωτικός πράκτορας μπορεί να δημιουργήσει ένα εξατομικευμένο και βελτιστοποιημένο ταξιδιωτικό πρόγραμμα για τον πελάτη. Αυτή η προσέγγιση διασφαλίζει ότι το ταξιδιωτικό σχέδιο ευθυγραμμίζεται με τις προτιμήσεις και τον προϋπολογισμό του πελάτη από την αρχή και βελτιώνεται με κάθε επανάληψη.

### Αξιοποίηση LLM για Επανακατάταξη και Βαθμολόγηση

Τα Μεγάλα Γλωσσικά Μοντέλα (LLMs) μπορούν να χρησιμοποιηθούν για επανακατάταξη και βαθμολόγηση, αξιολογώντας τη συνάφεια και την ποιότητα των ανακτημένων εγγράφων ή των παραγόμενων απαντήσεων. Ακολουθεί πώς λειτουργεί:

**Ανάκτηση**: Το αρχικό βήμα ανάκτησης φέρνει ένα σύνολο υποψήφιων εγγράφων ή απαντήσεων βάσει του ερωτήματος.

**Επανακατάταξη**: Το LLM αξιολογεί αυτούς τους υποψήφιους και τους επανακατατάσσει βάσει της συνάφειας και της ποιότητάς τους. Αυτό το βήμα διασφαλίζει ότι οι πιο σχετικές και υψηλής ποιότητας πληροφορίες παρουσιάζονται πρώτες.

**Βαθμολόγηση**: Το LLM αποδίδει βαθμολογίες σε κάθε υποψήφιο, αντικατοπτρίζοντας τη συνάφεια και την ποιότητά τους. Αυτό βοηθά στην επιλογή της καλύτερης απάντησης ή εγγράφου για τον χρήστη.

Με την αξιοποίηση των LLM για επανακατάταξη και βαθμολόγηση, το σύστημα μπορεί να παρέχει πιο ακριβείς και σχετικές πληροφορίες, βελτιώνοντας τη συνολική εμπειρία του χρήστη.

Ακολουθεί ένα παράδειγμα για το πώς ένας ταξιδιωτικός πράκτορας μπορεί να χρησιμοποιήσει ένα Μεγάλο Γλωσσικό Μοντέλο (LLM) για επανακατάταξη και βαθμολόγηση ταξιδιωτικών προορισμών βάσει των προτιμήσεων του χρήστη με Python:

#### Σενάριο - Ταξίδι βάσει Προτιμήσεων

Ένας ταξιδιωτικός πράκτορας θέλει να προτείνει τους καλύτερους ταξιδιωτικούς προορισμούς σε έναν πελάτη βάσει των προτιμήσεών του. Το LLM θα βοηθήσει στην επανακατάταξη και βαθμολόγηση των προορισμών για να διασφαλίσει ότι παρουσιάζονται οι πιο σχετικές επιλογές.

#### Βήματα:

1. Συλλογή προτιμήσεων χρήστη.
2. Ανάκτηση μιας λίστας πιθανών ταξιδιωτικών προορισμών.
3. Χρήση του LLM για επανακατάταξη και βαθμολόγηση των προορισμών βάσει των προτιμήσεων του χρήστη.

Ακολουθεί πώς μπορείτε να ενημερώσετε το προηγούμενο παράδειγμα για να χρησιμοποιήσετε τις Υπηρεσίες Azure OpenAI:

#### Απαιτήσεις

1. Χρειάζεστε μια συνδρομή Azure.
2. Δημιουργήστε έναν πόρο Azure OpenAI και αποκτήστε το κλειδί API σας.

#### Παράδειγμα Κώδικα Python

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Generate a prompt for the Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Define headers and payload for the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Call the Azure OpenAI API to get the re-ranked and scored destinations
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Extract and return the recommendations
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Example usage
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### Επεξήγηση Κώδικα - Σύστημα Προτιμήσεων

1. **Αρχικοποίηση**: Η κλάση `TravelAgent` αρχικοποιείται με μια λίστα πιθανών ταξιδιωτικών προορισμών, καθένας από τους οποίους έχει χαρακτηριστικά όπως όνομα και περιγραφή.

2. **Λήψη Προτάσεων (μέθοδος `get_recommendations`)**: Αυτή η μέθοδος δημιουργεί ένα prompt για την υπηρεσία Azure OpenAI βάσει των προτιμήσεων του χρήστη και κάνει ένα HTTP POST αίτημα στο API του Azure OpenAI για να λάβει επανακαταταγμένους και βαθμολογημένους προορισμούς.

3. **Δημιουργία Prompt (μέθοδος `generate_prompt`)**: Αυτή η μέθοδος κατασκευάζει ένα prompt για το Azure OpenAI, συμπεριλαμβανομένων των προτιμήσεων του χρήστη και της λίστας των προορισμών. Το prompt καθοδηγεί το μοντέλο να επανακατατάξει και να βαθμολογήσει τους προορισμούς βάσει των παρεχόμενων προτιμήσεων.

4. **Κλήση API**: Η βιβλιοθήκη `requests` χρησιμοποιείται για να κάνει ένα HTTP POST αίτημα στο endpoint του Azure OpenAI API. Η απάντηση περιέχει τους επανακαταταγμένους και βαθμολογημένους προορισμούς.

5. **Παράδειγμα Χρήσης**: Ο ταξιδιωτικός πράκτορας συλλέγει τις προτιμήσεις του χρήστη (π.χ. ενδιαφέρον για αξιοθέατα και ποικιλόμορφο πολιτισμό) και χρησιμοποιεί την υπηρεσία Azure OpenAI για να λάβει επανακαταταγμένες και βαθμολογημένες προτάσεις για ταξιδιωτικούς προορισμούς.

Φροντίστε να αντικαταστήσετε το `your_azure_openai_api_key` με το πραγματικό κλειδί API του Azure OpenAI και το `https://your-endpoint.com/...` με το πραγματικό URL του endpoint της ανάπτυξης του Azure OpenAI.

Με την αξιοποίηση του LLM για επανακατάταξη και βαθμολόγηση, ο ταξιδιωτικός πράκτορας μπορεί να παρέχει πιο εξατομικευμένες και σχετικές ταξιδιωτικές προτάσεις στους πελάτες, βελτιώνοντας τη συνολική εμπειρία τους.
#### Πρακτικό Παράδειγμα: Αναζήτηση με Πρόθεση στον Ταξιδιωτικό Πράκτορα

Ας πάρουμε τον Ταξιδιωτικό Πράκτορα ως παράδειγμα για να δούμε πώς μπορεί να υλοποιηθεί η αναζήτηση με πρόθεση.

1. **Συλλογή Προτιμήσεων Χρήστη**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Κατανόηση της Πρόθεσης του Χρήστη**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Επίγνωση Πλαισίου**

   ```python
   def analyze_context(query, user_history):
       # Combine current query with user history to understand context
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Αναζήτηση και Εξατομίκευση Αποτελεσμάτων**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Example search logic for informational intent
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Example search logic for navigational intent
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Example search logic for transactional intent
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Example personalization logic
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Return top 10 personalized results
   ```

5. **Παραδείγματα Χρήσης**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Δημιουργία Κώδικα ως Εργαλείο

Οι πράκτορες δημιουργίας κώδικα χρησιμοποιούν μοντέλα AI για να γράψουν και να εκτελέσουν κώδικα, επιλύοντας σύνθετα προβλήματα και αυτοματοποιώντας εργασίες.

### Πράκτορες Δημιουργίας Κώδικα

Οι πράκτορες δημιουργίας κώδικα χρησιμοποιούν γενετικά μοντέλα AI για να γράψουν και να εκτελέσουν κώδικα. Αυτοί οι πράκτορες μπορούν να επιλύσουν σύνθετα προβλήματα, να αυτοματοποιήσουν εργασίες και να παρέχουν πολύτιμες πληροφορίες δημιουργώντας και εκτελώντας κώδικα σε διάφορες γλώσσες προγραμματισμού.

#### Πρακτικές Εφαρμογές

1. **Αυτοματοποιημένη Δημιουργία Κώδικα**: Δημιουργία αποσπασμάτων κώδικα για συγκεκριμένες εργασίες, όπως ανάλυση δεδομένων, web scraping ή μηχανική μάθηση.
2. **SQL ως RAG**: Χρήση ερωτημάτων SQL για ανάκτηση και επεξεργασία δεδομένων από βάσεις δεδομένων.
3. **Επίλυση Προβλημάτων**: Δημιουργία και εκτέλεση κώδικα για την επίλυση συγκεκριμένων προβλημάτων, όπως η βελτιστοποίηση αλγορίθμων ή η ανάλυση δεδομένων.

#### Παράδειγμα: Πράκτορας Δημιουργίας Κώδικα για Ανάλυση Δεδομένων

Φανταστείτε ότι σχεδιάζετε έναν πράκτορα δημιουργίας κώδικα. Δείτε πώς μπορεί να λειτουργήσει:

1. **Εργασία**: Ανάλυση ενός συνόλου δεδομένων για την αναγνώριση τάσεων και μοτίβων.
2. **Βήματα**:
   - Φόρτωση του συνόλου δεδομένων σε ένα εργαλείο ανάλυσης δεδομένων.
   - Δημιουργία ερωτημάτων SQL για φιλτράρισμα και συγκέντρωση δεδομένων.
   - Εκτέλεση των ερωτημάτων και ανάκτηση των αποτελεσμάτων.
   - Χρήση των αποτελεσμάτων για τη δημιουργία οπτικοποιήσεων και πληροφοριών.
3. **Απαιτούμενοι Πόροι**: Πρόσβαση στο σύνολο δεδομένων, εργαλεία ανάλυσης δεδομένων και δυνατότητες SQL.
4. **Εμπειρία**: Χρήση προηγούμενων αποτελεσμάτων ανάλυσης για τη βελτίωση της ακρίβειας και της συνάφειας μελλοντικών αναλύσεων.

### Παράδειγμα: Πράκτορας Δημιουργίας Κώδικα για Ταξιδιωτικό Πράκτορα

Σε αυτό το παράδειγμα, θα σχεδιάσουμε έναν πράκτορα δημιουργίας κώδικα, τον Ταξιδιωτικό Πράκτορα, για να βοηθήσει τους χρήστες στον προγραμματισμό ταξιδιών δημιουργώντας και εκτελώντας κώδικα. Αυτός ο πράκτορας μπορεί να χειριστεί εργασίες όπως η αναζήτηση ταξιδιωτικών επιλογών, το φιλτράρισμα αποτελεσμάτων και η σύνταξη ενός προγράμματος ταξιδιού χρησιμοποιώντας γενετική AI.

#### Επισκόπηση του Πράκτορα Δημιουργίας Κώδικα

1. **Συλλογή Προτιμήσεων Χρήστη**: Συλλέγει δεδομένα χρήστη όπως προορισμό, ημερομηνίες ταξιδιού, προϋπολογισμό και ενδιαφέροντα.
2. **Δημιουργία Κώδικα για Ανάκτηση Δεδομένων**: Δημιουργεί αποσπάσματα κώδικα για την ανάκτηση δεδομένων σχετικά με πτήσεις, ξενοδοχεία και αξιοθέατα.
3. **Εκτέλεση Δημιουργημένου Κώδικα**: Εκτελεί τον δημιουργημένο κώδικα για την ανάκτηση πληροφοριών σε πραγματικό χρόνο.
4. **Δημιουργία Προγράμματος Ταξιδιού**: Συνθέτει τα δεδομένα που ανακτήθηκαν σε ένα εξατομικευμένο σχέδιο ταξιδιού.
5. **Προσαρμογή με Βάση την Ανατροφοδότηση**: Λαμβάνει ανατροφοδότηση από τον χρήστη και αναδημιουργεί κώδικα εάν χρειάζεται για να βελτιώσει τα αποτελέσματα.

#### Βήμα-Βήμα Υλοποίηση

1. **Συλλογή Προτιμήσεων Χρήστη**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Δημιουργία Κώδικα για Ανάκτηση Δεδομένων**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Example: Generate code to search for flights based on user preferences
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Example: Generate code to search for hotels
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Εκτέλεση Δημιουργημένου Κώδικα**

   ```python
   def execute_code(code):
       # Execute the generated code using exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Δημιουργία Προγράμματος Ταξιδιού**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Προσαρμογή με Βάση την Ανατροφοδότηση**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Adjust preferences based on user feedback
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Regenerate and execute code with updated preferences
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Αξιοποίηση της Επίγνωσης Περιβάλλοντος και της Λογικής

Η κατανόηση του σχήματος του πίνακα μπορεί να βελτιώσει τη διαδικασία δημιουργίας ερωτημάτων μέσω της αξιοποίησης της επίγνωσης περιβάλλοντος και της λογικής.

Δείτε ένα παράδειγμα για το πώς μπορεί να γίνει αυτό:

1. **Κατανόηση του Σχήματος**: Το σύστημα θα κατανοήσει το σχήμα του πίνακα και θα χρησιμοποιήσει αυτές τις πληροφορίες για να στηρίξει τη δημιουργία ερωτημάτων.
2. **Προσαρμογή με Βάση την Ανατροφοδότηση**: Το σύστημα θα προσαρμόσει τις προτιμήσεις του χρήστη με βάση την ανατροφοδότηση και θα σκεφτεί ποια πεδία στο σχήμα πρέπει να ενημερωθούν.
3. **Δημιουργία και Εκτέλεση Ερωτημάτων**: Το σύστημα θα δημιουργήσει και θα εκτελέσει ερωτήματα για την ανάκτηση ενημερωμένων δεδομένων πτήσεων και ξενοδοχείων με βάση τις νέες προτιμήσεις.

Ακολουθεί ένα ενημερωμένο παράδειγμα κώδικα Python που ενσωματώνει αυτές τις έννοιες:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Adjust preferences based on user feedback
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Reasoning based on schema to adjust other related preferences
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Custom logic to adjust preferences based on schema and feedback
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Generate code to fetch flight data based on updated preferences
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Generate code to fetch hotel data based on updated preferences
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Simulate execution of code and return mock data
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Generate itinerary based on flights, hotels, and attractions
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Example schema
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Example usage
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Regenerate and execute code with updated preferences
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Επεξήγηση - Κράτηση με Βάση την Ανατροφοδότηση

1. **Επίγνωση Σχήματος**: Το λεξικό `schema` ορίζει πώς πρέπει να προσαρμοστούν οι προτιμήσεις με βάση την ανατροφοδότηση. Περιλαμβάνει πεδία όπως `favorites` και `avoid`, με αντίστοιχες προσαρμογές.
2. **Προσαρμογή Προτιμήσεων (μέθοδος `adjust_based_on_feedback`)**: Αυτή η μέθοδος προσαρμόζει τις προτιμήσεις με βάση την ανατροφοδότηση του χρήστη και το σχήμα.
3. **Προσαρμογές με Βάση το Περιβάλλον (μέθοδος `adjust_based_on_environment`)**: Αυτή η μέθοδος προσαρμόζει τις προσαρμογές με βάση το σχήμα και την ανατροφοδότηση.
4. **Δημιουργία και Εκτέλεση Ερωτημάτων**: Το σύστημα δημιουργεί κώδικα για την ανάκτηση ενημερωμένων δεδομένων πτήσεων και ξενοδοχείων με βάση τις προσαρμοσμένες προτιμήσεις και προσομοιώνει την εκτέλεση αυτών των ερωτημάτων.
5. **Δημιουργία Προγράμματος Ταξιδιού**: Το σύστημα δημιουργεί ένα ενημερωμένο πρόγραμμα ταξιδιού με βάση τα νέα δεδομένα πτήσεων, ξενοδοχείων και αξιοθέατων.

Με την αξιοποίηση της επίγνωσης περιβάλλοντος και της λογικής με βάση το σχήμα, το σύστημα μπορεί να δημιουργήσει πιο ακριβή και σχετικά ερωτήματα, οδηγώντας σε καλύτερες ταξιδιωτικές προτάσεις και μια πιο εξατομικευμένη εμπειρία χρήστη.

### Χρήση SQL ως Τεχνική RAG (Ανάκτηση-Ενισχυμένη Γενετική)

Η SQL (Δομημένη Γλώσσα Ερωτημάτων) είναι ένα ισχυρό εργαλείο για την αλληλεπίδραση με βάσεις δεδομένων. Όταν χρησιμοποιείται ως μέρος μιας προσέγγισης RAG (Ανάκτηση-Ενισχυμένη Γενετική), η SQL μπορεί να ανακτήσει σχετικά δεδομένα από βάσεις δεδομένων για να ενημερώσει και να δημιουργήσει απαντήσεις ή ενέργειες σε πράκτορες AI. Ας εξερευνήσουμε πώς η SQL μπορεί να χρησιμοποιηθεί ως τεχνική RAG στο πλαίσιο του Ταξιδιωτικού Πράκτορα.

#### Βασικές Έννοιες

1. **Αλληλεπίδραση με Βάσεις Δεδομένων**:
   - Η SQL χρησιμοποιείται για την εκτέλεση ερωτημάτων σε βάσεις δεδομένων, την ανάκτηση σχετικών πληροφοριών και την επεξεργασία δεδομένων.
   - Παράδειγμα: Ανάκτηση λεπτομερειών πτήσεων, πληροφοριών ξενοδοχείων και αξιοθέατων από μια βάση δεδομένων ταξιδιών.

2. **Ενσωμάτωση με RAG**:
   - Τα ερωτήματα SQL δημιουργούνται με βάση την είσοδο και τις προτιμήσεις του χρήστη.
   - Τα δεδομένα που ανακτώνται χρησιμοποιούνται για τη δημιουργία εξατομικευμένων προτάσεων ή ενεργειών.

3. **Δυναμική Δημιουργία Ερωτημάτων**:
   - Ο πράκτορας AI δημιουργεί δυναμικά ερωτήματα SQL με βάση το πλαίσιο και τις ανάγκες του χρήστη.
   - Παράδειγμα: Προσαρμογή ερωτημάτων SQL για φιλτράρισμα αποτελεσμάτων με βάση τον προϋπολογισμό, τις ημερομηνίες και τα ενδιαφέροντα.

#### Εφαρμογές

- **Αυτοματοποιημένη Δημιουργία Κώδικα**: Δημιουργία αποσπασμάτων κώδικα για συγκεκριμένες εργασίες.
- **SQL ως RAG**: Χρήση ερωτημάτων SQL για επεξεργασία δεδομένων.
- **Επίλυση Προβλημάτων**: Δημιουργία και εκτέλεση κώδικα για την επίλυση προβλημάτων.

**Παράδειγμα**:
Ένας πράκτορας ανάλυσης δεδομένων:

1. **Εργασία**: Ανάλυση ενός συνόλου δεδομένων για την εύρεση τάσεων.
2. **Βήματα**:
   - Φόρτωση του συνόλου δεδομένων.
   - Δημιουργία ερωτημάτων SQL για φιλτράρισμα δεδομένων.
   - Εκτέλεση ερωτημάτων και ανάκτηση αποτελεσμάτων.
   - Δημιουργία οπτικοποιήσεων και πληροφοριών.
3. **Πόροι**: Πρόσβαση στο σύνολο δεδομένων, δυνατότητες SQL.
4. **Εμπειρία**: Χρήση προηγούμενων αποτελεσμάτων για τη βελτίωση μελλοντικών αναλύσεων.

#### Πρακτικό Παράδειγμα: Χρήση SQL στον Ταξιδιωτικό Πράκτορα

1. **Συλλογή Προτιμήσεων Χρήστη**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Δημιουργία Ερωτημάτων SQL**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Εκτέλεση Ερωτημάτων SQL**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Δημιουργία Προτάσεων**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Παράδειγμα Ερωτημάτων SQL

1. **Ερώτημα Πτήσης**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Ερώτημα Ξενοδοχείου**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Ερώτημα Αξιοθέατων**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Με την αξιοποίηση της SQL ως μέρος της προσέγγισης RAG, οι πράκτορες AI όπως ο Ταξιδιωτικός Πράκτορας μπορούν να ανακτούν δυναμικά και να χρησιμοποιούν σχετικά δεδομένα για να παρέχουν ακριβείς και εξατομικευμένες προτάσεις.

### Παράδειγμα Μεταγνώσης

Για να δείξουμε μια υλοποίηση μεταγνώσης, ας δημιουργήσουμε έναν απλό πράκτορα που *αναλογίζεται τη διαδικασία λήψης αποφάσεων* ενώ επιλύει ένα πρόβλημα. Σε αυτό το παράδειγμα, θα δημιουργήσουμε ένα σύστημα όπου ένας πράκτορας προσπαθεί να βελτιστοποιήσει την επιλογή ξενοδοχείου, αλλά στη συνέχεια αξιολογεί τη δική του λογική και προσαρμόζει τη στρατηγική του όταν κάνει λάθη ή υποβέλτιστες επιλογές.

Θα το προσομοιώσουμε χρησιμοποιώντας ένα βασικό παράδειγμα όπου ο πράκτορας επιλέγει ξενοδοχεία με βάση έναν συνδυασμό τιμής και ποιότητας, αλλά θα "αναλογιστεί" τις αποφάσεις του και θα προσαρμοστεί ανάλογα.

#### Πώς αυτό δείχνει μεταγνώση:

1. **Αρχική Απόφαση**: Ο πράκτορας θα επιλέξει το φθηνότερο ξενοδοχείο, χωρίς να κατανοεί την επίδραση της ποιότητας.
2. **Αναλογισμός και Αξιολόγηση**: Μετά την αρχική επιλογή, ο πράκτορας θα ελέγξει αν το ξενοδοχείο είναι "κακή" επιλογή χρησιμοποιώντας την ανατροφοδότηση του χρήστη. Αν διαπιστώσει ότι η ποιότητα του ξενοδοχείου ήταν πολύ χαμηλή, θα αναλογιστεί τη λογική του.
3. **Προσαρμογή Στρατηγικής**: Ο πράκτορας προσαρμόζει τη στρατηγική του με βάση τον αναλογισμό και μεταβαίνει από το "φθηνότερο" στο "υψηλότερης ποιότητας", βελτιώνοντας έτσι τη διαδικασία λήψης αποφάσεων στις μελλοντικές επαναλήψεις.

Ακολουθεί ένα παράδειγμα:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Stores the hotels chosen previously
        self.corrected_choices = []  # Stores the corrected choices
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Available strategies

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Let's assume we have some user feedback that tells us whether the last choice was good or not
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Adjust strategy if the previous choice was unsatisfactory
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Simulate a list of hotels (price and quality)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Create an agent
agent = HotelRecommendationAgent()

# Step 1: The agent recommends a hotel using the "cheapest" strategy
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Step 2: The agent reflects on the choice and adjusts strategy if necessary
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Step 3: The agent recommends again, this time using the adjusted strategy
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Ικανότητες Μεταγνώσης Πράκτορα

Το κλειδί εδώ είναι η ικανότητα του πράκτορα να:
- Αξιολογεί τις προηγούμενες επιλογές και τη διαδικασία λήψης αποφάσεων.
- Προσαρμόζει τη στρατηγική του με βάση αυτόν τον αναλογισμό, δηλαδή τη μεταγνώση σε δράση.

Αυτό είναι μια απλή μορφή μεταγνώσης όπου το σύστημα είναι ικανό να προσαρμόζει τη διαδικασία λογικής του με βάση εσωτερική ανατροφοδότηση.

### Συμπέρασμα

Η μεταγνώση είναι ένα ισχυρό εργαλείο που μπορεί να βελτιώσει σημαντικά τις δυνατότητες των πρακτόρων AI. Με την ενσωμάτωση μεταγνωστικών διαδικασιών, μπορείτε να σχεδιάσετε πράκτορες που είναι πιο έξυπνοι, προσαρμοστικοί και αποτελεσματικοί. Χρησιμοποιήστε τους πρόσθετους πόρους για να εξερευνήσετε περαιτέρω τον συναρπαστικό κόσμο της μεταγνώσης στους πράκτορες AI.

### Έχετε Περισσότερες Ερωτήσεις για το Σχεδιαστικό Πρότυπο Μεταγνώσης;

Εγγραφείτε στο [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) για να συναντήσετε άλλους μαθητές, να παρακολουθήσετε ώρες γραφείου και να λάβετε απαντήσεις στις ερωτήσεις σας για τους Πράκτορες AI.

## Προηγούμενο Μάθημα

[Σχεδιαστικό Πρότυπο Πολλαπλών Πρακτόρων](../08-multi-agent/README.md)

## Επόμενο Μάθημα

[Πράκτορες AI σε Παραγωγή](../10-ai-agents-production/README.md)

---

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.