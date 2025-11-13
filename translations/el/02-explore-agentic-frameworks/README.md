<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T12:29:59+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "el"
}
-->
[![Εξερεύνηση Πλαισίων Πρακτόρων AI](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.el.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Κάντε κλικ στην εικόνα παραπάνω για να δείτε το βίντεο αυτού του μαθήματος)_

# Εξερεύνηση Πλαισίων Πρακτόρων AI

Τα πλαίσια πρακτόρων AI είναι λογισμικά σχεδιασμένα για να απλοποιούν τη δημιουργία, την ανάπτυξη και τη διαχείριση πρακτόρων AI. Αυτά τα πλαίσια παρέχουν στους προγραμματιστές προκατασκευασμένα στοιχεία, αφαιρέσεις και εργαλεία που διευκολύνουν την ανάπτυξη σύνθετων συστημάτων AI.

Αυτά τα πλαίσια βοηθούν τους προγραμματιστές να επικεντρωθούν στις μοναδικές πτυχές των εφαρμογών τους, παρέχοντας τυποποιημένες προσεγγίσεις στις κοινές προκλήσεις της ανάπτυξης πρακτόρων AI. Ενισχύουν την κλιμακωσιμότητα, την προσβασιμότητα και την αποτελεσματικότητα στην κατασκευή συστημάτων AI.

## Εισαγωγή 

Αυτό το μάθημα θα καλύψει:

- Τι είναι τα Πλαίσια Πρακτόρων AI και τι επιτρέπουν στους προγραμματιστές να επιτύχουν;
- Πώς μπορούν οι ομάδες να τα χρησιμοποιήσουν για να δημιουργήσουν γρήγορα πρωτότυπα, να επαναλάβουν και να βελτιώσουν τις δυνατότητες του πράκτορα τους;
- Ποιες είναι οι διαφορές μεταξύ των πλαισίων και εργαλείων που δημιουργήθηκαν από τη Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, και <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>;
- Μπορώ να ενσωματώσω τα υπάρχοντα εργαλεία του οικοσυστήματος Azure απευθείας ή χρειάζομαι ανεξάρτητες λύσεις;
- Τι είναι η υπηρεσία Azure AI Agents και πώς με βοηθά;

## Στόχοι μάθησης

Οι στόχοι αυτού του μαθήματος είναι να σας βοηθήσουν να κατανοήσετε:

- Τον ρόλο των Πλαισίων Πρακτόρων AI στην ανάπτυξη AI.
- Πώς να αξιοποιήσετε τα Πλαίσια Πρακτόρων AI για να δημιουργήσετε έξυπνους πράκτορες.
- Βασικές δυνατότητες που παρέχονται από τα Πλαίσια Πρακτόρων AI.
- Τις διαφορές μεταξύ AutoGen, Semantic Kernel και Azure AI Agent Service.

## Τι είναι τα Πλαίσια Πρακτόρων AI και τι επιτρέπουν στους προγραμματιστές να κάνουν;

Τα παραδοσιακά Πλαίσια AI μπορούν να σας βοηθήσουν να ενσωματώσετε AI στις εφαρμογές σας και να τις βελτιώσετε με τους εξής τρόπους:

- **Εξατομίκευση**: Το AI μπορεί να αναλύσει τη συμπεριφορά και τις προτιμήσεις των χρηστών για να παρέχει εξατομικευμένες προτάσεις, περιεχόμενο και εμπειρίες.
Παράδειγμα: Υπηρεσίες streaming όπως το Netflix χρησιμοποιούν AI για να προτείνουν ταινίες και σειρές βάσει του ιστορικού προβολών, ενισχύοντας την εμπλοκή και την ικανοποίηση των χρηστών.
- **Αυτοματοποίηση και Αποτελεσματικότητα**: Το AI μπορεί να αυτοματοποιήσει επαναλαμβανόμενες εργασίες, να απλοποιήσει τις ροές εργασίας και να βελτιώσει την επιχειρησιακή αποτελεσματικότητα.
Παράδειγμα: Εφαρμογές εξυπηρέτησης πελατών χρησιμοποιούν chatbots με AI για να χειρίζονται κοινές ερωτήσεις, μειώνοντας τους χρόνους απόκρισης και απελευθερώνοντας ανθρώπινους πράκτορες για πιο σύνθετα θέματα.
- **Βελτιωμένη Εμπειρία Χρήστη**: Το AI μπορεί να βελτιώσει τη συνολική εμπειρία χρήστη παρέχοντας έξυπνες λειτουργίες όπως αναγνώριση φωνής, επεξεργασία φυσικής γλώσσας και προβλεπτικό κείμενο.
Παράδειγμα: Εικονικοί βοηθοί όπως η Siri και το Google Assistant χρησιμοποιούν AI για να κατανοούν και να ανταποκρίνονται σε φωνητικές εντολές, διευκολύνοντας την αλληλεπίδραση των χρηστών με τις συσκευές τους.

### Ακούγεται υπέροχο, σωστά; Τότε γιατί χρειαζόμαστε τα Πλαίσια Πρακτόρων AI;

Τα Πλαίσια Πρακτόρων AI αντιπροσωπεύουν κάτι περισσότερο από απλά Πλαίσια AI. Είναι σχεδιασμένα για να επιτρέπουν τη δημιουργία έξυπνων πρακτόρων που μπορούν να αλληλεπιδρούν με χρήστες, άλλους πράκτορες και το περιβάλλον για να επιτύχουν συγκεκριμένους στόχους. Αυτοί οι πράκτορες μπορούν να επιδεικνύουν αυτόνομη συμπεριφορά, να λαμβάνουν αποφάσεις και να προσαρμόζονται σε μεταβαλλόμενες συνθήκες. Ας δούμε μερικές βασικές δυνατότητες που παρέχονται από τα Πλαίσια Πρακτόρων AI:

- **Συνεργασία και Συντονισμός Πρακτόρων**: Επιτρέπουν τη δημιουργία πολλαπλών πρακτόρων AI που μπορούν να συνεργάζονται, να επικοινωνούν και να συντονίζονται για να λύσουν σύνθετες εργασίες.
- **Αυτοματοποίηση και Διαχείριση Εργασιών**: Παρέχουν μηχανισμούς για την αυτοματοποίηση πολυβηματικών ροών εργασίας, την ανάθεση εργασιών και τη δυναμική διαχείριση εργασιών μεταξύ πρακτόρων.
- **Κατανόηση και Προσαρμογή στο Πλαίσιο**: Εξοπλίζουν τους πράκτορες με την ικανότητα να κατανοούν το πλαίσιο, να προσαρμόζονται σε μεταβαλλόμενα περιβάλλοντα και να λαμβάνουν αποφάσεις βάσει πληροφοριών σε πραγματικό χρόνο.

Συνοπτικά, οι πράκτορες σας επιτρέπουν να κάνετε περισσότερα, να ανεβάσετε την αυτοματοποίηση σε επόμενο επίπεδο, να δημιουργήσετε πιο έξυπνα συστήματα που μπορούν να προσαρμόζονται και να μαθαίνουν από το περιβάλλον τους.

## Πώς να δημιουργήσετε γρήγορα πρωτότυπα, να επαναλάβετε και να βελτιώσετε τις δυνατότητες του πράκτορα;

Αυτός είναι ένας ταχέως εξελισσόμενος τομέας, αλλά υπάρχουν ορισμένα κοινά στοιχεία στα περισσότερα Πλαίσια Πρακτόρων AI που μπορούν να σας βοηθήσουν να δημιουργήσετε γρήγορα πρωτότυπα και να επαναλάβετε, όπως τα αρθρωτά στοιχεία, τα συνεργατικά εργαλεία και η εκμάθηση σε πραγματικό χρόνο. Ας τα εξετάσουμε:

- **Χρησιμοποιήστε Αρθρωτά Στοιχεία**: Τα SDK AI προσφέρουν προκατασκευασμένα στοιχεία όπως συνδέσμους AI και Μνήμης, κλήση λειτουργιών χρησιμοποιώντας φυσική γλώσσα ή πρόσθετα κώδικα, πρότυπα προτροπών και άλλα.
- **Αξιοποιήστε Συνεργατικά Εργαλεία**: Σχεδιάστε πράκτορες με συγκεκριμένους ρόλους και εργασίες, επιτρέποντάς τους να δοκιμάζουν και να βελτιώνουν συνεργατικές ροές εργασίας.
- **Μάθετε σε Πραγματικό Χρόνο**: Εφαρμόστε βρόχους ανατροφοδότησης όπου οι πράκτορες μαθαίνουν από τις αλληλεπιδράσεις και προσαρμόζουν τη συμπεριφορά τους δυναμικά.

### Χρησιμοποιήστε Αρθρωτά Στοιχεία

Τα SDK όπως το Microsoft Semantic Kernel και το LangChain προσφέρουν προκατασκευασμένα στοιχεία όπως συνδέσμους AI, πρότυπα προτροπών και διαχείριση μνήμης.

**Πώς μπορούν οι ομάδες να τα χρησιμοποιήσουν**: Οι ομάδες μπορούν να συναρμολογήσουν γρήγορα αυτά τα στοιχεία για να δημιουργήσουν ένα λειτουργικό πρωτότυπο χωρίς να ξεκινήσουν από το μηδέν, επιτρέποντας γρήγορη πειραματισμό και επανάληψη.

**Πώς λειτουργεί στην πράξη**: Μπορείτε να χρησιμοποιήσετε έναν προκατασκευασμένο αναλυτή για να εξαγάγετε πληροφορίες από την είσοδο του χρήστη, μια μονάδα μνήμης για να αποθηκεύσετε και να ανακτήσετε δεδομένα, και έναν δημιουργό προτροπών για να αλληλεπιδράσετε με τους χρήστες, όλα χωρίς να χρειάζεται να κατασκευάσετε αυτά τα στοιχεία από την αρχή.

**Παράδειγμα κώδικα**. Ας δούμε παραδείγματα για το πώς μπορείτε να χρησιμοποιήσετε έναν προκατασκευασμένο Συνδέσμο AI με το Semantic Kernel Python και .Net που χρησιμοποιεί αυτόματη κλήση λειτουργιών για να απαντήσει το μοντέλο στην είσοδο του χρήστη:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```

Αυτό που βλέπετε από το παράδειγμα είναι πώς μπορείτε να αξιοποιήσετε έναν προκατασκευασμένο αναλυτή για να εξαγάγετε βασικές πληροφορίες από την είσοδο του χρήστη, όπως την προέλευση, τον προορισμό και την ημερομηνία ενός αιτήματος κράτησης πτήσης. Αυτή η αρθρωτή προσέγγιση σας επιτρέπει να επικεντρωθείτε στη λογική υψηλού επιπέδου.

### Αξιοποιήστε Συνεργατικά Εργαλεία

Τα πλαίσια όπως το CrewAI, το Microsoft AutoGen και το Semantic Kernel διευκολύνουν τη δημιουργία πολλαπλών πρακτόρων που μπορούν να συνεργάζονται.

**Πώς μπορούν οι ομάδες να τα χρησιμοποιήσουν**: Οι ομάδες μπορούν να σχεδιάσουν πράκτορες με συγκεκριμένους ρόλους και εργασίες, επιτρέποντάς τους να δοκιμάζουν και να βελτιώνουν συνεργατικές ροές εργασίας και να βελτιώνουν τη συνολική αποτελεσματικότητα του συστήματος.

**Πώς λειτουργεί στην πράξη**: Μπορείτε να δημιουργήσετε μια ομάδα πρακτόρων όπου κάθε πράκτορας έχει εξειδικευμένη λειτουργία, όπως ανάκτηση δεδομένων, ανάλυση ή λήψη αποφάσεων. Αυτοί οι πράκτορες μπορούν να επικοινωνούν και να μοιράζονται πληροφορίες για να επιτύχουν έναν κοινό στόχο, όπως να απαντήσουν σε ένα ερώτημα χρήστη ή να ολοκληρώσουν μια εργασία.

**Παράδειγμα κώδικα (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```

Αυτό που βλέπετε στον προηγούμενο κώδικα είναι πώς μπορείτε να δημιουργήσετε μια εργασία που περιλαμβάνει πολλαπλούς πράκτορες που συνεργάζονται για να αναλύσουν δεδομένα. Κάθε πράκτορας εκτελεί μια συγκεκριμένη λειτουργία, και η εργασία εκτελείται συντονίζοντας τους πράκτορες για να επιτύχουν το επιθυμητό αποτέλεσμα. Δημιουργώντας ειδικούς πράκτορες με εξειδικευμένους ρόλους, μπορείτε να βελτιώσετε την αποτελεσματικότητα και την απόδοση της εργασίας.

### Μάθετε σε Πραγματικό Χρόνο

Τα προηγμένα πλαίσια παρέχουν δυνατότητες για κατανόηση και προσαρμογή στο πλαίσιο σε πραγματικό χρόνο.

**Πώς μπορούν οι ομάδες να τα χρησιμοποιήσουν**: Οι ομάδες μπορούν να εφαρμόσουν βρόχους ανατροφοδότησης όπου οι πράκτορες μαθαίνουν από τις αλληλεπιδράσεις και προσαρμόζουν τη συμπεριφορά τους δυναμικά, οδηγώντας σε συνεχή βελτίωση και αναβάθμιση των δυνατοτήτων.

**Πώς λειτουργεί στην πράξη**: Οι πράκτορες μπορούν να αναλύσουν την ανατροφοδότηση των χρηστών, δεδομένα περιβάλλοντος και αποτελέσματα εργασιών για να ενημερώσουν τη βάση γνώσεων τους, να προσαρμόσουν τους αλγόριθμους λήψης αποφάσεων και να βελτιώσουν την απόδοση με την πάροδο του χρόνου. Αυτή η διαδικασία επαναληπτικής μάθησης επιτρέπει στους πράκτορες να προσαρμόζονται σε μεταβαλλόμενες συνθήκες και προτιμήσεις χρηστών, ενισχύοντας τη συνολική αποτελεσματικότητα του συστήματος.

## Ποιες είναι οι διαφορές μεταξύ των πλαισίων AutoGen, Semantic Kernel και Azure AI Agent Service;

Υπάρχουν πολλοί τρόποι για να συγκρίνετε αυτά τα πλαίσια, αλλά ας δούμε μερικές βασικές διαφορές όσον αφορά τον σχεδιασμό, τις δυνατότητες και τις προτεινόμενες χρήσεις τους:

## AutoGen

Το AutoGen είναι ένα πλαίσιο ανοιχτού κώδικα που αναπτύχθηκε από το AI Frontiers Lab της Microsoft Research. Εστιάζει σε εφαρμογές *agentic* που βασίζονται σε γεγονότα και είναι κατανεμημένες, επιτρέποντας πολλαπλά LLMs και SLMs, εργαλεία και προηγμένα σχέδια πολλαπλών πρακτόρων.

Το AutoGen βασίζεται στην κεντρική ιδέα των πρακτόρων, οι οποίοι είναι αυτόνομες οντότητες που μπορούν να αντιλαμβάνονται το περιβάλλον τους, να λαμβάνουν αποφάσεις και να αναλαμβάνουν δράση για να επιτύχουν συγκεκριμένους στόχους. Οι πράκτορες επικοινωνούν μέσω ασύγχρονων μηνυμάτων, επιτρέποντάς τους να εργάζονται ανεξάρτητα και παράλληλα, ενισχύοντας την κλιμακωσιμότητα και την ανταπόκριση του συστήματος.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Οι πράκτορες βασίζονται στο μοντέλο ηθοποιού</a>. Σύμφωνα με τη Wikipedia, ένας ηθοποιός είναι _το βασικό δομικό στοιχείο του ταυτόχρονου υπολογισμού. Σε απάντηση σε ένα μήνυμα που λαμβάνει, ένας ηθοποιός μπορεί: να λαμβάνει τοπικές αποφάσεις, να δημιουργεί περισσότερους ηθοποιούς, να στέλνει περισσότερα μηνύματα και να καθορίζει πώς να ανταποκριθεί στο επόμενο μήνυμα που λαμβάνει_.

**Προτεινόμενες Χρήσεις**: Αυτοματοποίηση δημιουργίας κώδικα, εργασίες ανάλυσης δεδομένων και δημιουργία προσαρμοσμένων πρακτόρων για λειτουργίες σχεδιασμού και έρευνας.

Ακολουθούν μερικές σημαντικές βασικές έννοιες του AutoGen:

- **Πράκτορες**. Ένας πράκτορας είναι μια οντότητα λογισμικού που:
  - **Επικοινωνεί μέσω μηνυμάτων**, τα οποία μπορεί να είναι συγχρονισμένα ή ασύγχρονα.
  - **Διατηρεί τη δική του κατάσταση**, η οποία μπορεί να τροποποιηθεί από εισερχόμενα μηνύματα.
  - **Εκτελεί ενέργειες** σε απάντηση σε μηνύματα που λαμβάνει ή αλλαγές στην κατάστασή του. Αυτές οι ενέργειες μπορεί να τροποποιήσουν την κατάσταση του πράκτορα και να παράγουν εξωτερικά αποτελέσματα, όπως ενημέρωση αρχείων μηνυμάτων, αποστολή νέων μηνυμάτων, εκτέλεση κώδικα ή πραγματοποίηση κλήσεων API.
    
  Εδώ έχετε ένα σύντομο απόσπασμα κώδικα στο οποίο δημιουργείτε τον δικό σας πράκτορα με δυνατότητες συνομιλίας:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
    
    Στον προηγούμενο κώδικα, δημιουργήθηκε ο `MyAgent` και κληρονομεί από τον `RoutedAgent`. Έχει έναν χειριστή μηνυμάτων που εκτυπώνει το περιεχόμενο του μηνύματος και στη συνέχεια στέλνει μια απάντηση χρησιμοποιώντας τον αντιπρόσωπο `AssistantAgent`. Ιδιαίτερα σημειώστε πώς αναθέτουμε στο `self._delegate` μια παρουσία του `AssistantAgent`, που είναι ένας προκατασκευασμένος πράκτορας που μπορεί να χειριστεί ολοκληρώσεις συνομιλιών.


    Ας ενημερώσουμε το AutoGen για αυτόν τον τύπο πράκτορα και ας ξεκινήσουμε το πρόγραμμα:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Στον προηγούμενο κώδικα, οι πράκτορες καταχωρούνται με το runtime και στη συνέχεια αποστέλλεται ένα μήνυμα στον πράκτορα, με αποτέλεσμα την ακόλουθη έξοδο:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Πολλαπλοί πράκτορες**. Το AutoGen υποστηρίζει τη δημιουργία πολλ
Αυτά τα δεδομένα αποθηκεύονται στη συλλογή μνήμης `SummarizedAzureDocs`. Αυτό είναι ένα πολύ απλοποιημένο παράδειγμα, αλλά μπορείτε να δείτε πώς μπορείτε να αποθηκεύσετε πληροφορίες στη μνήμη για να τις χρησιμοποιήσει το LLM.

Αυτά είναι τα βασικά του πλαισίου Semantic Kernel, τι γίνεται όμως με το Agent Framework;

## Υπηρεσία Azure AI Agent

Η Υπηρεσία Azure AI Agent είναι μια πιο πρόσφατη προσθήκη, που παρουσιάστηκε στο Microsoft Ignite 2024. Επιτρέπει την ανάπτυξη και την υλοποίηση AI agents με πιο ευέλικτα μοντέλα, όπως η άμεση κλήση ανοιχτού κώδικα LLMs όπως Llama 3, Mistral και Cohere.

Η Υπηρεσία Azure AI Agent παρέχει ισχυρούς μηχανισμούς ασφάλειας για επιχειρήσεις και μεθόδους αποθήκευσης δεδομένων, καθιστώντας την κατάλληλη για επιχειρηματικές εφαρμογές.

Λειτουργεί άμεσα με πλαίσια ορχήστρωσης πολλαπλών agents όπως AutoGen και Semantic Kernel.

Αυτή η υπηρεσία βρίσκεται επί του παρόντος σε Δημόσια Προεπισκόπηση και υποστηρίζει Python και C# για τη δημιουργία agents.

Χρησιμοποιώντας το Semantic Kernel Python, μπορούμε να δημιουργήσουμε έναν Azure AI Agent με ένα plugin που ορίζεται από τον χρήστη:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Βασικές έννοιες

Η Υπηρεσία Azure AI Agent περιλαμβάνει τις εξής βασικές έννοιες:

- **Agent**. Η Υπηρεσία Azure AI Agent ενσωματώνεται με το Azure AI Foundry. Στο AI Foundry, ένας AI Agent λειτουργεί ως "έξυπνη" μικροϋπηρεσία που μπορεί να χρησιμοποιηθεί για να απαντά σε ερωτήσεις (RAG), να εκτελεί ενέργειες ή να αυτοματοποιεί πλήρως ροές εργασίας. Το επιτυγχάνει συνδυάζοντας τη δύναμη των γεννητικών μοντέλων AI με εργαλεία που του επιτρέπουν να έχει πρόσβαση και να αλληλεπιδρά με πραγματικές πηγές δεδομένων. Εδώ είναι ένα παράδειγμα agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Σε αυτό το παράδειγμα, δημιουργείται ένας agent με το μοντέλο `gpt-4o-mini`, ένα όνομα `my-agent` και οδηγίες `You are helpful agent`. Ο agent είναι εξοπλισμένος με εργαλεία και πόρους για να εκτελεί εργασίες ερμηνείας κώδικα.

- **Νήμα και μηνύματα**. Το νήμα είναι μια άλλη σημαντική έννοια. Αντιπροσωπεύει μια συνομιλία ή αλληλεπίδραση μεταξύ ενός agent και ενός χρήστη. Τα νήματα μπορούν να χρησιμοποιηθούν για την παρακολούθηση της προόδου μιας συνομιλίας, την αποθήκευση πληροφοριών πλαισίου και τη διαχείριση της κατάστασης της αλληλεπίδρασης. Εδώ είναι ένα παράδειγμα νήματος:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Στον προηγούμενο κώδικα, δημιουργείται ένα νήμα. Στη συνέχεια, αποστέλλεται ένα μήνυμα στο νήμα. Με την κλήση `create_and_process_run`, ζητείται από τον agent να εκτελέσει εργασία στο νήμα. Τέλος, τα μηνύματα ανακτώνται και καταγράφονται για να δούμε την απάντηση του agent. Τα μηνύματα δείχνουν την πρόοδο της συνομιλίας μεταξύ του χρήστη και του agent. Είναι επίσης σημαντικό να κατανοήσουμε ότι τα μηνύματα μπορεί να είναι διαφορετικών τύπων, όπως κείμενο, εικόνα ή αρχείο, δηλαδή η εργασία του agent έχει ως αποτέλεσμα, για παράδειγμα, μια εικόνα ή μια απάντηση κειμένου. Ως προγραμματιστής, μπορείτε στη συνέχεια να χρησιμοποιήσετε αυτές τις πληροφορίες για να επεξεργαστείτε περαιτέρω την απάντηση ή να την παρουσιάσετε στον χρήστη.

- **Ενσωμάτωση με άλλα πλαίσια AI**. Η Υπηρεσία Azure AI Agent μπορεί να αλληλεπιδράσει με άλλα πλαίσια όπως AutoGen και Semantic Kernel, που σημαίνει ότι μπορείτε να δημιουργήσετε μέρος της εφαρμογής σας σε ένα από αυτά τα πλαίσια και, για παράδειγμα, να χρησιμοποιήσετε την Υπηρεσία Agent ως ορχηστρωτή ή να δημιουργήσετε τα πάντα στην Υπηρεσία Agent.

**Περιπτώσεις Χρήσης**: Η Υπηρεσία Azure AI Agent έχει σχεδιαστεί για επιχειρηματικές εφαρμογές που απαιτούν ασφαλή, επεκτάσιμη και ευέλικτη ανάπτυξη AI agents.

## Ποια είναι η διαφορά μεταξύ αυτών των πλαισίων;

Φαίνεται ότι υπάρχει αρκετή επικάλυψη μεταξύ αυτών των πλαισίων, αλλά υπάρχουν κάποιες βασικές διαφορές όσον αφορά τον σχεδιασμό, τις δυνατότητες και τις στοχευμένες περιπτώσεις χρήσης:

- **AutoGen**: Είναι ένα πλαίσιο πειραματισμού που επικεντρώνεται στην πρωτοποριακή έρευνα για συστήματα πολλαπλών agents. Είναι το καλύτερο μέρος για πειραματισμό και πρωτότυπα σύνθετων συστημάτων πολλαπλών agents.
- **Semantic Kernel**: Είναι μια βιβλιοθήκη agent έτοιμη για παραγωγή για τη δημιουργία επιχειρηματικών εφαρμογών με agents. Εστιάζει σε εφαρμογές με βάση γεγονότα, κατανεμημένες εφαρμογές με agents, επιτρέποντας πολλαπλά LLMs και SLMs, εργαλεία και μοτίβα σχεδίασης με έναν ή πολλούς agents.
- **Azure AI Agent Service**: Είναι μια πλατφόρμα και υπηρεσία ανάπτυξης στο Azure Foundry για agents. Προσφέρει συνδεσιμότητα με υπηρεσίες που υποστηρίζονται από το Azure, όπως Azure OpenAI, Azure AI Search, Bing Search και εκτέλεση κώδικα.

Ακόμα δεν είστε σίγουροι ποιο να επιλέξετε;

### Περιπτώσεις Χρήσης

Ας δούμε αν μπορούμε να σας βοηθήσουμε περνώντας από μερικές κοινές περιπτώσεις χρήσης:

> Ε: Πειραματίζομαι, μαθαίνω και δημιουργώ εφαρμογές agents proof-of-concept, και θέλω να μπορώ να δημιουργώ και να πειραματίζομαι γρήγορα
>

> Α: Το AutoGen θα ήταν μια καλή επιλογή για αυτό το σενάριο, καθώς επικεντρώνεται σε εφαρμογές με βάση γεγονότα, κατανεμημένες εφαρμογές με agents και υποστηρίζει προηγμένα μοτίβα σχεδίασης πολλαπλών agents.

> Ε: Τι κάνει το AutoGen καλύτερη επιλογή από το Semantic Kernel και την Υπηρεσία Azure AI Agent για αυτή την περίπτωση χρήσης;
>
> Α: Το AutoGen έχει σχεδιαστεί ειδικά για εφαρμογές με βάση γεγονότα, κατανεμημένες εφαρμογές με agents, καθιστώντας το κατάλληλο για την αυτοματοποίηση εργασιών δημιουργίας κώδικα και ανάλυσης δεδομένων. Παρέχει τα απαραίτητα εργαλεία και δυνατότητες για την αποτελεσματική δημιουργία σύνθετων συστημάτων πολλαπλών agents.

> Ε: Φαίνεται ότι και η Υπηρεσία Azure AI Agent θα μπορούσε να λειτουργήσει εδώ, έχει εργαλεία για δημιουργία κώδικα και άλλα;
>
> Α: Ναι, η Υπηρεσία Azure AI Agent είναι μια πλατφόρμα υπηρεσίας για agents και προσθέτει ενσωματωμένες δυνατότητες για πολλαπλά μοντέλα, Azure AI Search, Bing Search και Azure Functions. Διευκολύνει τη δημιουργία των agents σας στο Foundry Portal και την ανάπτυξή τους σε κλίμακα.

> Ε: Είμαι ακόμα μπερδεμένος, δώστε μου απλά μια επιλογή
>
> Α: Μια εξαιρετική επιλογή είναι να δημιουργήσετε την εφαρμογή σας πρώτα στο Semantic Kernel και στη συνέχεια να χρησιμοποιήσετε την Υπηρεσία Azure AI Agent για να αναπτύξετε τον agent σας. Αυτή η προσέγγιση σας επιτρέπει να διατηρείτε εύκολα τους agents σας ενώ αξιοποιείτε τη δύναμη για τη δημιουργία συστημάτων πολλαπλών agents στο Semantic Kernel. Επιπλέον, το Semantic Kernel έχει έναν συνδετήρα στο AutoGen, καθιστώντας εύκολη τη χρήση και των δύο πλαισίων μαζί.

Ας συνοψίσουμε τις βασικές διαφορές σε έναν πίνακα:

| Πλαίσιο | Εστίαση | Βασικές Έννοιες | Περιπτώσεις Χρήσης |
| --- | --- | --- | --- |
| AutoGen | Εφαρμογές με βάση γεγονότα, κατανεμημένες εφαρμογές με agents | Agents, Personas, Functions, Data | Δημιουργία κώδικα, εργασίες ανάλυσης δεδομένων |
| Semantic Kernel | Κατανόηση και δημιουργία περιεχομένου που μοιάζει με ανθρώπινο | Agents, Modular Components, Συνεργασία | Κατανόηση φυσικής γλώσσας, δημιουργία περιεχομένου |
| Azure AI Agent Service | Ευέλικτα μοντέλα, ασφάλεια για επιχειρήσεις, Δημιουργία κώδικα, Κλήση εργαλείων | Μοναδικότητα, Συνεργασία, Ορχήστρωση διαδικασιών | Ασφαλής, επεκτάσιμη και ευέλικτη ανάπτυξη AI agents |

Ποια είναι η ιδανική περίπτωση χρήσης για καθένα από αυτά τα πλαίσια;

## Μπορώ να ενσωματώσω τα υπάρχοντα εργαλεία του οικοσυστήματος Azure απευθείας ή χρειάζομαι ανεξάρτητες λύσεις;

Η απάντηση είναι ναι, μπορείτε να ενσωματώσετε τα υπάρχοντα εργαλεία του οικοσυστήματος Azure απευθείας με την Υπηρεσία Azure AI Agent, ειδικά επειδή έχει σχεδιαστεί για να λειτουργεί απρόσκοπτα με άλλες υπηρεσίες Azure. Για παράδειγμα, μπορείτε να ενσωματώσετε το Bing, το Azure AI Search και το Azure Functions. Υπάρχει επίσης βαθιά ενσωμάτωση με το Azure AI Foundry.

Για το AutoGen και το Semantic Kernel, μπορείτε επίσης να ενσωματώσετε με τις υπηρεσίες Azure, αλλά μπορεί να χρειαστεί να καλέσετε τις υπηρεσίες Azure από τον κώδικά σας. Ένας άλλος τρόπος ενσωμάτωσης είναι να χρησιμοποιήσετε τα Azure SDKs για να αλληλεπιδράσετε με τις υπηρεσίες Azure από τους agents σας. Επιπλέον, όπως αναφέρθηκε, μπορείτε να χρησιμοποιήσετε την Υπηρεσία Azure AI Agent ως ορχηστρωτή για τους agents που δημιουργήθηκαν στο AutoGen ή το Semantic Kernel, κάτι που θα παρέχει εύκολη πρόσβαση στο οικοσύστημα Azure.

## Δείγματα Κώδικα

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Έχετε περισσότερες ερωτήσεις σχετικά με τα AI Agent Frameworks;

Γίνετε μέλος στο [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) για να συναντήσετε άλλους μαθητές, να παρακολουθήσετε ώρες γραφείου και να λάβετε απαντήσεις στις ερωτήσεις σας για τους AI Agents.

## Αναφορές

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel and AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Using Azure AI Agent Service with AutoGen / Semantic Kernel to build a multi-agent's solution</a>

## Προηγούμενο Μάθημα

[Εισαγωγή στους AI Agents και τις Περιπτώσεις Χρήσης](../01-intro-to-ai-agents/README.md)

## Επόμενο Μάθημα

[Κατανόηση Μοτίβων Σχεδίασης Agents](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->