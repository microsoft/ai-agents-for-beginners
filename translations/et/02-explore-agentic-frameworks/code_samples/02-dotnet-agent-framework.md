# 🔍 Microsoft Agent'i raamistiku uurimine - Põhiline agent (.NET)

## 📋 Õpieesmärgid

See näide uurib Microsoft Agent Frameworki põhikontseptsioone läbi põhilise agendi rakenduse .NET-is. Õpid tuumagentuursete mustrite põhialuseid ja mõistad, kuidas intelligentsed agendid töötavad C# ja .NET ökosüsteemi abil.

### Mida avastad

- 🏗️ **Agendi arhitektuur**: Mõistmine AI agentide põhistruktuurist .NET-is
- 🛠️ **Tööriistade integreerimine**: Kuidas agendid kasutavad väliseid funktsioone võimete laiendamiseks  
- 💬 **Vestluse voog**: Mitme sammuga vestluste ja konteksti haldamine lõimede juhtimise kaudu
- 🔧 **Konfiguratsioonimustrid**: Parimad praktikud agendi seadistamiseks ja haldamiseks .NET-is

## 🎯 Kaetud põhimõisted

### Agendi raamistikupõhimõtted

- **Autonoomia**: Kuidas agendid teevad iseseisvaid otsuseid kasutades .NET AI abstraktsioone
- **Reaktiivsus**: Keskkonna muutustele ja kasutaja sisenditele reageerimine
- **Proaktiivsus**: Initsiatiivide võtmine eesmärkide ja konteksti põhjal
- **Sotsiaalne võimekus**: Loomuliku keele kaudu suhtlemine vestluslõimede kaudu

### Tehnilised komponendid

- **AIAgent**: Tuumagendi korraldus ja vestluste haldamine (.NET)
- **Tööriistafunktsioonid**: Agentide võimete laiendamine C# meetodite ja atribuutide abil
- **Azure OpenAI integreerimine**: Keelemudelite kasutamine Azure OpenAI vastuste API kaudu
- **Turvaline konfiguratsioon**: Keskkonnapõhine lõpp-punktide haldus

## 🔧 Tehniline virn

### Põhitehnoloogiad

- Microsoft Agent Framework (.NET)
- Azure OpenAI (vastuste API) integratsioon
- Azure.AI.OpenAI kliendi mustrid
- Keskkonnapõhine konfiguratsioon DotNetEnv abil

### Agendi võimekused

- Loomuliku keele mõistmine ja genereerimine
- Funktsioonide kutsumine ja tööriistade kasutamine C# atribuutidega
- Kontekstiteadlikud vastused vestlussessioonide abil
- Laiendatav arhitektuur sõltuvuste süstimise mustritega

## 📚 Raamistiku võrdlus

See näide demonstreerib Microsoft Agent Frameworki lähenemist võrreldes teiste agentuursete raamistikega:

| Omadus | Microsoft Agent Framework | Teised raamistikud |
|---------|-------------------------|------------------|
| **Integratsioon** | Looduslik Microsofti ökosüsteem | Mitmekesine ühilduvus |
| **Lihtsus** | Puhas, intuitiivne API | Sageli keeruline seadistus |
| **Laiendatavus** | Lihtne tööriistade integreerimine | Raamistiku-kohane |
| **Ettevõttesisene valmisolek** | Disainitud tootmiseks | Sõltub raamistiku tüübist |

## 🚀 Algus

### Eelnõuded

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) või uuem versioon
- [Azure tellimus](https://azure.microsoft.com/free/) koos Azure OpenAI ressursi ja mudeli juurutusega
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — logi sisse `az login` käsuga

### Vajalikud keskkonnamuutujad

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Seejärel logi sisse, et AzureCliCredential saaks tokeni kätte
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Seejärel logi sisse, et AzureCliCredential saaks tokeni
az login
```

### Näidiskood

Selleks, et käivitada koodinäide,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Või kasutades dotnet CLI-d:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Vaata täielikku koodi failist [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs).

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*
#:package Azure.AI.OpenAI@2.1.0
#:package Azure.Identity@1.13.1

using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using Azure.AI.OpenAI;
using Azure.Identity;

// Tool Function: Random Destination Generator
// This static method will be available to the agent as a callable tool
// The [Description] attribute helps the AI understand when to use this function
// This demonstrates how to create custom tools for AI agents
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
    // List of popular vacation destinations around the world
    // The agent will randomly select from these options
    var destinations = new List<string>
    {
        "Paris, France",
        "Tokyo, Japan",
        "New York City, USA",
        "Sydney, Australia",
        "Rome, Italy",
        "Barcelona, Spain",
        "Cape Town, South Africa",
        "Rio de Janeiro, Brazil",
        "Bangkok, Thailand",
        "Vancouver, Canada"
    };

    // Generate random index and return selected destination
    // Uses System.Random for simple random selection
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}

// Azure OpenAI with the Responses API (stable v1 endpoint). Sign in with `az login`.
var azureEndpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")
    ?? throw new InvalidOperationException("AZURE_OPENAI_ENDPOINT is not set.");
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-5-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Define Agent Identity and Comprehensive Instructions
// Agent name for identification and logging purposes
var AGENT_NAME = "TravelAgent";

// Detailed instructions that define the agent's personality, capabilities, and behavior
// This system prompt shapes how the agent responds and interacts with users
var AGENT_INSTRUCTIONS = """
You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
"Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?"

Always prioritize user preferences. If they mention a specific destination like "Bali" or "Paris," focus your planning on that location rather than suggesting alternatives.
""";

// Create AI Agent with Advanced Travel Planning Capabilities
// Get the Responses client for the deployment and create the AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Session for Context Management.
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentSession session = await agent.CreateSessionAsync();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the session parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", session))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation sessions and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", session))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Peamised järeldused

1. **Agendi arhitektuur**: Microsoft Agent Framework pakub puhast, tüübikindlat lähenemist AI agentide ehitamiseks .NET-is
2. **Tööriistade integreerimine**: Funktsioonid, mis on tähistatud `[Description]` atribuutidega, muutuvad agentidele kättesaadavateks tööriistadeks
3. **Vestluse kontekst**: Sessioonihaldus võimaldab mitme kordusega vestlusi täiskonteksti teadlikkusega
4. **Konfiguratsiooni haldus**: Keskkonnamuutujad ja turvaline volituste käsitlemine järgivad .NET parimaid praktikaid
5. **Azure OpenAI vastuste API**: Agent kasutab Azure OpenAI vastuste API-d läbi Azure.AI.OpenAI SDK

## 🔗 Täiendavad ressursid

- [Microsoft Agent Frameworki dokumentatsioon](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI Microsoft Foundry's](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET üksikfaili äpid](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->