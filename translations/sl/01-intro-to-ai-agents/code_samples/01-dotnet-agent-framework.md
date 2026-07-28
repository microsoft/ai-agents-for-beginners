# 🌍 AI potovalni agent z Microsoft Agent Framework (.NET)

## 📋 Pregled scenarija

Ta primer prikazuje, kako zgraditi inteligentnega agenta za načrtovanje potovanj z uporabo Microsoft Agent Framework za .NET. Agent lahko samodejno ustvari prilagojene dnevne načrte za naključne destinacije po svetu.

### Ključne zmožnosti:

- 🎲 **Naključno izbiranje destinacij**: Uporablja lastno orodje za izbiro počitniških krajev
- 🗺️ **Inteligentno načrtovanje potovanja**: Ustvarja podrobne dnevne itinerarje
- 🔄 **Pretakanje v realnem času**: Podpira tako takojšnje kot pretočne odzive
- 🛠️ **Integracija lastnih orodij**: Prikazuje, kako razširiti zmožnosti agenta

## 🔧 Tehnična arhitektura

### Osnovne tehnologije

- **Microsoft Agent Framework**: Najnovejša .NET implementacija za razvoj AI agentov
- **Azure OpenAI (Responses API)**: Uporablja Azure OpenAI Responses API za inferenco modela
- **Azure Identity**: Varnostno prijavljanje preko `AzureCliCredential` (`az login`)
- **Varnostna konfiguracija**: Upravljanje končnih točk na osnovi okolja

### Ključne komponente

1. **AIAgent**: Glavni orkestrator agenta, ki upravlja tok pogovora
2. **Lastna orodja**: Funkcija `GetRandomDestination()` na voljo agentu
3. **Odjemalec za odzive**: Pogovorni vmesnik, temelječ na Azure OpenAI Responses
4. **Podpora za pretakanje**: Zmožnost generiranja odzivov v realnem času

### Vzorec integracije

```mermaid
graph LR
    A[Zahteva uporabnika] --> B[AI agent]
    B --> C[Azure OpenAI (Responses API)]
    B --> D[Orodje GetRandomDestination]
    C --> E[Potovalni načrt]
    D --> E
```

## 🚀 Začetek

### Predpogoji

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) ali višja različica
- [Azure naročnina](https://azure.microsoft.com/free/) z Azure OpenAI virom in nameščeno modelno rešitev
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — prijava z `az login`

### Zahtevane spremenljivke okolja

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Nato se prijavite, da bo AzureCliCredential lahko pridobil žeton
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Nato se prijavite, da lahko AzureCliCredential pridobi žeton
az login
```

### Primer kode

Za izvedbo primer kode,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Ali z uporabo dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Oglejte si [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) za celotno kodo.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.4.1
#:package Microsoft.Agents.AI.OpenAI@1.1.0
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

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetChatClient(deployment)
    .AsAIAgent(
        instructions: "You are a helpful AI Agent that can help plan vacations for customers at random destinations",
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Execute Agent: Plan a Day Trip
// Run the agent with streaming enabled for real-time response display
// Shows the agent's thinking and response as it generates the content
// Provides better user experience with immediate feedback
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip"))
{
    await Task.Delay(10);
    Console.Write(update);
}
```

## 🎓 Glavne ugotovitve

1. **Arhitektura agenta**: Microsoft Agent Framework ponuja čist, varno tipiziran pristop k gradnji AI agentov v .NET-ju
2. **Integracija orodij**: Funkcije z atributi `[Description]` postanejo na voljo kot orodja za agenta
3. **Upravljanje konfiguracije**: Spremenljivke okolja in varno upravljanje poverilnic sledijo najboljšim praksam .NET
4. **Azure OpenAI Responses API**: Agent uporablja Azure OpenAI Responses API prek SDK Azure.AI.OpenAI

## 🔗 Dodatni viri

- [Dokumentacija Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI v Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->