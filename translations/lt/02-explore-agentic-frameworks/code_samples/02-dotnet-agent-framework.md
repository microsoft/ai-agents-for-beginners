<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:41:20+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "lt"
}
-->
# 🔍 Agentinių struktūrų tyrinėjimas - Pagrindinis agentas (.NET)

## 📋 Mokymosi tikslai

Šiame užrašų knygelėje nagrinėjami pagrindiniai Microsoft Agent Framework konceptai per pagrindinio agento įgyvendinimą .NET aplinkoje. Sužinosite pagrindinius agentinius modelius ir suprasite, kaip veikia intelektualūs agentai naudojant C# ir .NET ekosistemą.

**Ką sužinosite:**
- 🏗️ **Agentų architektūra**: Suprasti pagrindinę AI agentų struktūrą .NET aplinkoje
- 🛠️ **Įrankių integracija**: Kaip agentai naudoja išorines funkcijas, kad išplėstų galimybes  
- 💬 **Pokalbių eiga**: Daugkartinių pokalbių ir konteksto valdymas naudojant gijų valdymą
- 🔧 **Konfigūracijos modeliai**: Geriausios praktikos agentų nustatymui ir valdymui .NET aplinkoje

## 🎯 Pagrindinės aptariamos sąvokos

### Agentinio struktūros principai
- **Autonomija**: Kaip agentai priima savarankiškus sprendimus naudojant .NET AI abstrakcijas
- **Reaktyvumas**: Reagavimas į aplinkos pokyčius ir vartotojo įvestis
- **Proaktyvumas**: Iniciatyvos ėmimasis remiantis tikslais ir kontekstu
- **Socialinis gebėjimas**: Sąveika per natūralią kalbą naudojant pokalbių gijas

### Techniniai komponentai
- **AIAgent**: Pagrindinis agento organizavimas ir pokalbių valdymas (.NET)
- **Įrankių funkcijos**: Agentų galimybių plėtra naudojant C# metodus ir atributus
- **OpenAI integracija**: Kalbos modelių naudojimas per standartizuotas .NET API
- **Aplinkos valdymas**: Saugus konfigūravimas ir kredencialų valdymas su DotNetEnv

## ⚙️ Reikalavimai ir nustatymas

**Reikalingos priklausomybės:**
- .NET 9.0 SDK ar naujesnė versija
- Visual Studio 2022 arba VS Code su C# plėtiniu

**NuGet paketai:**
- `Microsoft.Extensions.AI` - Pagrindinės AI abstrakcijos
- `Microsoft.Extensions.AI.OpenAI` - OpenAI integracija (peržiūra)
- `DotNetEnv` - Aplinkos kintamųjų valdymas

**Aplinkos konfigūracija (.env failas):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Technologijų rinkinys

**Pagrindinės technologijos:**
- Microsoft Agent Framework (.NET)
- GitHub Models API integracija
- OpenAI suderinami klientų modeliai
- Konfigūracija pagal aplinką su DotNetEnv

**Agentų galimybės:**
- Natūralios kalbos supratimas ir generavimas
- Funkcijų kvietimas ir įrankių naudojimas su C# atributais
- Atsakymai, atsižvelgiant į kontekstą, naudojant pokalbių gijas
- Išplečiama architektūra su priklausomybių injekcijos modeliais

## 📚 Struktūrų palyginimas

Šis pavyzdys demonstruoja Microsoft Agent Framework požiūrį .NET aplinkoje, palyginti su kitomis platformomis:

| Funkcija | .NET Agent Framework | Python ekvivalentai |
|----------|-----------------------|---------------------|
| **Tipų saugumas** | Stiprus tipavimas su C# | Dinaminis tipavimas |
| **Integracija** | Gimtoji .NET ekosistema | Įvairi suderinamumas |
| **Veikimas** | Kompiliuoto kodo našumas | Interpretuojamas vykdymas |
| **Paruoštumas verslui** | Sukurta gamybos .NET programoms | Priklauso nuo struktūros |
| **Įrankiai** | Visual Studio integracija | Priklauso nuo IDE |

## 🚀 Pradžia

Sekite žemiau pateiktas instrukcijas, kad sukurtumėte savo pirmąjį pagrindinį agentą .NET aplinkoje ir suprastumėte pagrindinius agentinius konceptus!

## 📦 Diegimas ir nustatymas

Šis pavyzdys pateikiamas kaip vykdomas .NET vieno failo programos pavyzdys. Žr. pridedamą `02-dotnet-agent-framework.cs` failą, kuriame pateikiama visa įgyvendinimo versija.

Norėdami paleisti šį pavyzdį:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Arba naudodami dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Kodo apžvalga

Pilnas įgyvendinimas apima:

### 1. Paketų priklausomybės

```csharp
// Core AI abstraction layer for .NET applications
#r "nuget: Microsoft.Extensions.AI, 9.9.1"

// Microsoft Agent Framework OpenAI integration
#r "nuget: Microsoft.Agents.AI.OpenAI, 1.0.0-preview.251001.3"

// Core Microsoft Agent Framework library
#r "nuget: Microsoft.Agents.AI, 1.0.0-preview.251001.3"

// Environment variable management
#r "nuget: DotNetEnv, 3.1.1"
```

### 2. Esminiai importai

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Aplinkos konfigūracija

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Įrankių funkcijų apibrėžimas

```csharp
// Random destination generator tool
[Description("Provides a random vacation destination.")]
static string GetRandomDestination()
{
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
    
    var random = new Random();
    int index = random.Next(destinations.Count);
    return destinations[index];
}
```

### 5. Konfigūracija ir kliento nustatymas

```csharp
// Extract environment variables
var github_endpoint = Environment.GetEnvironmentVariable("GITHUB_ENDPOINT") ?? 
    throw new InvalidOperationException("GITHUB_ENDPOINT is not set.");
var github_model_id = Environment.GetEnvironmentVariable("GITHUB_MODEL_ID") ?? "gpt-4o-mini";
var github_token = Environment.GetEnvironmentVariable("GITHUB_TOKEN") ?? 
    throw new InvalidOperationException("GITHUB_TOKEN is not set.");

// Configure OpenAI client for GitHub Models
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI client
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);
```

### 6. Agentų konfigūracija

```csharp
const string AGENT_NAME = "TravelAgent";

const string AGENT_INSTRUCTIONS = @"You are a helpful AI Agent that can help plan vacations for customers.

Important: When users specify a destination, always plan for that location. Only suggest random destinations when the user hasn't specified a preference.

When the conversation begins, introduce yourself with this message:
""Hello! I'm your TravelAgent assistant. I can help plan vacations and suggest interesting destinations for you. Here are some things you can ask me:
1. Plan a day trip to a specific location
2. Suggest a random vacation destination
3. Find destinations with specific features (beaches, mountains, historical sites, etc.)
4. Plan an alternative trip if you don't like my first suggestion

What kind of trip would you like me to help you plan today?""

Always prioritize user preferences. If they mention a specific destination like ""Bali"" or ""Paris,"" focus your planning on that location rather than suggesting alternatives.
";
```

### 7. Agentų inicializacija

```csharp
// Create AI agent with travel planning capabilities
AIAgent agent = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions)
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create((Func<string>)GetRandomDestination)]
    );
```

### 8. Pokalbių valdymas

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Pagrindinės išvados

1. **Agentų architektūra**: Microsoft Agent Framework suteikia aiškų, tipų saugų požiūrį į AI agentų kūrimą .NET aplinkoje
2. **Įrankių integracija**: Funkcijos, pažymėtos `[Description]` atributais, tampa prieinamais įrankiais agentui
3. **Pokalbių kontekstas**: Gijų valdymas leidžia daugkartinius pokalbius su pilnu konteksto supratimu
4. **Konfigūracijos valdymas**: Aplinkos kintamųjų ir saugaus kredencialų valdymo praktikos atitinka .NET geriausias praktikas
5. **OpenAI suderinamumas**: GitHub Models integracija veikia sklandžiai per OpenAI suderinamas API

## 🔗 Papildomi ištekliai

- [Microsoft Agent Framework dokumentacija](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [GitHub Models Marketplace](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET vieno failo programos](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.