<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:57:13+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "el"
}
-->
# 🎯 Σχεδιασμός & Πρότυπα Σχεδίασης με Μοντέλα GitHub (.NET)

## 📋 Στόχοι Μάθησης

Αυτό το σημειωματάριο παρουσιάζει πρότυπα σχεδιασμού και σχεδιασμού επιπέδου επιχείρησης για τη δημιουργία έξυπνων πρακτόρων χρησιμοποιώντας το Microsoft Agent Framework στο .NET με Μοντέλα GitHub. Θα μάθετε να δημιουργείτε πράκτορες που μπορούν να αναλύουν σύνθετα προβλήματα, να σχεδιάζουν λύσεις πολλών βημάτων και να εκτελούν εξελιγμένες ροές εργασίας με τις δυνατότητες επιχείρησης του .NET.

## ⚙️ Προαπαιτούμενα & Ρύθμιση

**Περιβάλλον Ανάπτυξης:**
- .NET 9.0 SDK ή νεότερο
- Visual Studio 2022 ή VS Code με επέκταση C#
- Πρόσβαση στο API Μοντέλων GitHub

**Απαιτούμενες Εξαρτήσεις:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Ρύθμιση Περιβάλλοντος (αρχείο .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## Εκτέλεση του Κώδικα

Αυτό το μάθημα περιλαμβάνει μια υλοποίηση Εφαρμογής Μονού Αρχείου .NET. Για να το εκτελέσετε:

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

Ή χρησιμοποιήστε την εντολή dotnet run:

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## Υλοποίηση Κώδικα

Η πλήρης υλοποίηση είναι διαθέσιμη στο `07-dotnet-agent-framework.cs`, η οποία δείχνει:

- Φόρτωση ρυθμίσεων περιβάλλοντος με DotNetEnv
- Ρύθμιση του OpenAI client για Μοντέλα GitHub
- Ορισμός δομημένων μοντέλων δεδομένων (Plan και TravelPlan) με σειριοποίηση JSON
- Δημιουργία AI πράκτορα με δομημένη έξοδο χρησιμοποιώντας JSON schema
- Εκτέλεση αιτημάτων σχεδιασμού με απαντήσεις τύπου ασφαλούς

## Βασικές Έννοιες

### Δομημένος Σχεδιασμός με Μοντέλα Τύπου Ασφαλούς

Ο πράκτορας χρησιμοποιεί κλάσεις C# για να ορίσει τη δομή των εξόδων σχεδιασμού:

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

### Οδηγίες Πράκτορα Σχεδιασμού

Ο πράκτορας λειτουργεί ως συντονιστής, αναθέτοντας εργασίες σε εξειδικευμένους υπο-πράκτορες:

- FlightBooking: Για κράτηση πτήσεων και παροχή πληροφοριών πτήσεων
- HotelBooking: Για κράτηση ξενοδοχείων και παροχή πληροφοριών ξενοδοχείων
- CarRental: Για κράτηση αυτοκινήτων και παροχή πληροφοριών ενοικίασης αυτοκινήτων
- ActivitiesBooking: Για κράτηση δραστηριοτήτων και παροχή πληροφοριών δραστηριοτήτων
- DestinationInfo: Για παροχή πληροφοριών σχετικά με προορισμούς
- DefaultAgent: Για διαχείριση γενικών αιτημάτων

## Αναμενόμενη Έξοδος

Όταν εκτελέσετε τον πράκτορα με ένα αίτημα σχεδιασμού ταξιδιού, θα αναλύσει το αίτημα και θα δημιουργήσει ένα δομημένο σχέδιο με κατάλληλες αναθέσεις εργασιών σε εξειδικευμένους πράκτορες, μορφοποιημένο ως JSON που συμμορφώνεται με το schema TravelPlan.

---

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.