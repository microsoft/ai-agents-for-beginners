# 🌍 Dirbtinio intelekto kelionių agentas su Microsoft Agent Framework (.NET)

## 📋 Scenarijaus apžvalga

Šis pavyzdys demonstruoja, kaip sukurti intelektualų kelionių planavimo agentą, naudojant Microsoft Agent Framework .NET aplinkoje. Agentas gali automatiškai generuoti personalizuotas dienos kelionių maršrutus atsitiktiniams pasaulio taškams.

### Pagrindinės savybės:

- 🎲 **Atsitiktinis kelionės tikslas**: Naudoja pasirinktą įrankį atostogų vietoms pasirinkti
- 🗺️ **Intelektualus kelionės planavimas**: Kuria detalius dienos po dienos maršrutus
- 🔄 **Realaus laiko srautas**: Palaiko tiek momentinius, tiek srautinio perdavimo atsakymus
- 🛠️ **Individualių įrankių integracija**: Demonstruoja, kaip išplėsti agento galimybes

## 🔧 Techninė architektūra

### Pagrindinės technologijos

- **Microsoft Agent Framework**: Naujausia .NET implementacija DI agentų kūrimui
- **Azure OpenAI (Responses API)**: Naudoja Azure OpenAI Responses API modeliui apdoroti
- **Azure Identity**: Saugus prisijungimas per `AzureCliCredential` (`az login`)
- **Saugaus konfigūravimo valdymas**: Aplinkos kintamųjų pagrindu valdoma prieiga prie taškų

### Pagrindinės sudedamosios dalys

1. **AIAgent**: Pagrindinis agentas, valdantis pokalbio eigą
2. **Individualūs įrankiai**: Funkcija `GetRandomDestination()` prieinama agentui
3. **Responses klientas**: Pokalbio sąsaja, pagrįsta Azure OpenAI Responses API
4. **Srautinio perdavimo palaikymas**: Realaus laiko atsakymų generavimo galimybės

### Integracijos modelis

```mermaid
graph LR
    A[Vartotojo užklausa] --> B[DI agentas]
    B --> C[Azure OpenAI (Atsakymų API)]
    B --> D[Įrankis Atsitiktinei Kelionės Vietai Gauti]
    C --> E[Kelionės maršrutas]
    D --> E
```

## 🚀 Pradžia

### Reikalavimai

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) arba naujesnė versija
- [Azure prenumerata](https://azure.microsoft.com/free/) su Azure OpenAI resursu ir modelio paleidimu
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) — prisijunkite su `az login`

### Reikalingi aplinkos kintamieji

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini
# Tada prisijunkite, kad AzureCliCredential galėtų gauti žetoną
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4o-mini"
# Tada prisijunkite, kad AzureCliCredential galėtų gauti žetoną
az login
```

### Pavyzdinis kodas

Norėdami paleisti pavyzdinį kodą,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

Arba naudodami dotnet CLI:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Peržiūrėkite [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) pilną kodą.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@9.*
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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4o-mini";

var azureClient = new AzureOpenAIClient(new Uri(azureEndpoint), new AzureCliCredential());

// Create AI Agent with Travel Planning Capabilities
// Get the Responses client for the specified deployment and create the AI agent
// Configure agent with travel planning instructions and random destination tool
// The agent can now plan trips using the GetRandomDestination function
AIAgent agent = azureClient
    .GetOpenAIResponseClient(deployment)
    .CreateAIAgent(
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

## 🎓 Pagrindinės įžvalgos

1. **Agentų architektūra**: Microsoft Agent Framework suteikia aiškų ir tipams saugų požiūrį DI agentų kūrimui .NET aplinkoje
2. **Įrankių integracija**: Funkcijos, pažymėtos `[Description]` atributais, tampa įrankiais agentui
3. **Konfigūracijos valdymas**: Aplinkos kintamieji ir saugus kredencialų valdymas atitinka .NET gerąsias praktikas
4. **Azure OpenAI Responses API**: Agentas naudoja Azure OpenAI Responses API per Azure.AI.OpenAI SDK

## 🔗 Papildomi ištekliai

- [Microsoft Agent Framework dokumentacija](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [.NET vieno failo programos](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->