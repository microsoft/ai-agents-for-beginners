# 🎯 Σχεδιασμός & Σχέδια Μοτίβων με Azure OpenAI (Responses API) (.NET)

## 📋 Στόχοι Μάθησης

Αυτό το σημειωματάριο παρουσιάζει επιχειρηματικά μοτίβα σχεδιασμού και προγραμματισμού για την κατασκευή ευφυών πρακτόρων χρησιμοποιώντας το Microsoft Agent Framework σε .NET με Azure OpenAI (Responses API). Θα μάθετε να δημιουργείτε πράκτορες που μπορούν να διασπάσουν πολύπλοκα προβλήματα, να σχεδιάσουν πολύ-βηματικές λύσεις και να εκτελέσουν εξελιγμένες ροές εργασίας με τις επιχειρηματικές δυνατότητες του .NET.

## ⚙️ Προαπαιτούμενα & Ρύθμιση

**Περιβάλλον Ανάπτυξης:**
- .NET 9.0 SDK ή νεότερο
- Visual Studio 2022 ή VS Code με επέκταση C#
- Μια συνδρομή Azure με πόρο Azure OpenAI και ανάπτυξη μοντέλου
- Το Azure CLI — συνδεθείτε με `az login`

**Απαραίτητες Εξαρτήσεις:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Διαμόρφωση Περιβάλλοντος (.env αρχείο):**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## Εκτέλεση Κώδικα

Αυτό το μάθημα περιλαμβάνει υλοποίηση .NET Single File App. Για να το εκτελέσετε:

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
- Διαμόρφωση του πελάτη Azure OpenAI και δημιουργία πράκτορα AI με `GetChatClient().AsAIAgent()`
- Ορισμό δομημένων μοντέλων δεδομένων (Plan και TravelPlan) με σειριοποίηση JSON
- Δημιουργία πράκτορα AI με δομημένη έξοδο χρησιμοποιώντας JSON schema
- Εκτέλεση αιτημάτων προγραμματισμού με τύπο-ασφαλείς απαντήσεις

## Κύριες Έννοιες

### Δομημένος Προγραμματισμός με Τύπο-Ασφαλή Μοντέλα

Ο πράκτορας χρησιμοποιεί κλάσεις C# για να ορίσει τη δομή της εξόδου προγραμματισμού:

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

Ο πράκτορας έχει ρυθμιστεί να επιστρέφει απαντήσεις που ταιριάζουν με το schema TravelPlan:

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
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
- CarRental: Για κράτηση αυτοκινήτων και παροχή πληροφοριών ενοικίασης αυτοκινήτων
- ActivitiesBooking: Για κράτηση δραστηριοτήτων και παροχή πληροφοριών δραστηριοτήτων
- DestinationInfo: Για παροχή πληροφοριών σχετικά με προορισμούς
- DefaultAgent: Για τη διαχείριση γενικών αιτημάτων

## Αναμενόμενο Αποτέλεσμα

Όταν εκτελέσετε τον πράκτορα με αίτημα ταξιδιωτικού προγραμματισμού, θα αναλύσει το αίτημα και θα δημιουργήσει ένα δομημένο πλάνο με κατάλληλες αναθέσεις εργασιών σε εξειδικευμένους πράκτορες, μορφοποιημένο ως JSON που συμμορφώνεται με το schema TravelPlan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία μετάφρασης με τεχνητή νοημοσύνη [Co-op Translator](https://github.com/Azure/co-op-translator). Ενώ επιδιώκουμε την ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->