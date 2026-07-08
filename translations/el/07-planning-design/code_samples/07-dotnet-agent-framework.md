# 🎯 Σχεδιασμός & Σχεδιαστικά Πρότυπα με το Azure OpenAI (Responses API) (.NET)

## 📋 Μαθησιακοί Στόχοι

Αυτό το σημειωματάριο παρουσιάζει πρότυπα σχεδιασμού και προγραμματισμού επιπέδου επιχείρησης για τη δημιουργία ευφυών πρακτόρων χρησιμοποιώντας το Microsoft Agent Framework σε .NET με το Azure OpenAI (Responses API). Θα μάθετε πώς να δημιουργείτε πράκτορες που μπορούν να αποσυνθέτουν σύνθετα προβλήματα, να προγραμματίζουν πολύ-βηματικές λύσεις και να εκτελούν εξελιγμένες ροές εργασίας με τις επιχειρησιακές δυνατότητες του .NET.

## ⚙️ Προαπαιτούμενα & Ρύθμιση

**Περιβάλλον Ανάπτυξης:**
- SDK .NET 9.0 ή νεότερο
- Visual Studio 2022 ή VS Code με επέκταση C#
- Συνδρομή Azure με πόρο Azure OpenAI και ανάπτυξη μοντέλου
- Το Azure CLI — σύνδεση με `az login`

**Απαραίτητες Εξαρτήσεις:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Διαμόρφωση Περιβάλλοντος (.env αρχείο):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
```

## Εκτέλεση Κώδικα

Το μάθημα περιλαμβάνει υλοποίηση .NET Single File App. Για να το τρέξετε:

```bash
# Κάντε το αρχείο εκτελέσιμο (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Εκτελέστε την εφαρμογή
./07-dotnet-agent-framework.cs
```

Ή χρησιμοποιήστε την εντολή dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Υλοποίηση Κώδικα

Η πλήρης υλοποίηση είναι διαθέσιμη στο `07-dotnet-agent-framework.cs`, το οποίο παρουσιάζει:

- Φόρτωση διαμόρφωσης περιβάλλοντος με DotNetEnv
- Ρύθμιση του πελάτη Azure OpenAI για το Responses API
- Ορισμό δομημένων μοντέλων δεδομένων (Plan και TravelPlan) με σειριοποίηση JSON
- Δημιουργία πρακτόρα AI με δομημένη έξοδο χρησιμοποιώντας JSON schema
- Εκτέλεση αιτημάτων προγραμματισμού με τύπους ασφαλών απαντήσεων

## Βασικές Έννοιες

### Δομημένος Προγραμματισμός με Τύπους Ασφαλή Μοντέλα

Ο πράκτορας χρησιμοποιεί C# κλάσεις για να ορίσει τη δομή των αποτελεσμάτων προγράμματος:

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### JSON Schema για Δομημένες Εξόδους

Ο πράκτορας διαμορφώνεται ώστε να επιστρέφει απαντήσεις σύμφωνα με το σχήμα TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### Οδηγίες Πράκτορα Προγραμματισμού

Ο πράκτορας λειτουργεί ως συντονιστής, αναθέτοντας εργασίες σε εξειδικευμένους υπο-πράκτορες:

- FlightBooking: Για κράτηση πτήσεων και παροχή πληροφοριών πτήσεων
- HotelBooking: Για κράτηση ξενοδοχείων και παροχή πληροφοριών ξενοδοχείων
- CarRental: Για ενοικίαση αυτοκινήτων και παροχή πληροφοριών ενοικίασης αυτοκινήτων
- ActivitiesBooking: Για κράτηση δραστηριοτήτων και παροχή πληροφοριών δραστηριοτήτων
- DestinationInfo: Για παροχή πληροφοριών σχετικά με προορισμούς
- DefaultAgent: Για αντιμετώπιση γενικών αιτημάτων

## Αναμενόμενη Έξοδος

Όταν εκτελέσετε τον πράκτορα με αίτημα προγραμματισμού ταξιδιού, θα αναλύσει το αίτημα και θα δημιουργήσει ένα δομημένο σχέδιο με κατάλληλες αναθέσεις εργασιών σε εξειδικευμένους πράκτορες, μορφοποιημένο ως JSON που συμμορφώνεται με το σχήμα TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->