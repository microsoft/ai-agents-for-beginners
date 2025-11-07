<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:39:40+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "ro"
}
-->
# 🔍 Explorarea Cadrelor Agentice - Agent de Bază (.NET)

## 📋 Obiective de Învățare

Acest notebook explorează conceptele fundamentale ale Microsoft Agent Framework printr-o implementare de bază a unui agent în .NET. Vei învăța modele agentice de bază și vei înțelege cum funcționează agenții inteligenți în profunzime folosind C# și ecosistemul .NET.

**Ce vei descoperi:**
- 🏗️ **Arhitectura Agentului**: Înțelegerea structurii de bază a agenților AI în .NET
- 🛠️ **Integrarea Instrumentelor**: Cum agenții utilizează funcții externe pentru a-și extinde capabilitățile  
- 💬 **Fluxul Conversației**: Gestionarea conversațiilor multi-turn și contextului cu managementul thread-urilor
- 🔧 **Modele de Configurare**: Cele mai bune practici pentru configurarea și gestionarea agenților în .NET

## 🎯 Concepte Cheie Acoperite

### Principiile Cadrelor Agentice
- **Autonomie**: Cum agenții iau decizii independente folosind abstracții AI din .NET
- **Reactivitate**: Răspunsul la schimbările de mediu și la intrările utilizatorului
- **Proactivitate**: Inițiativa bazată pe obiective și context
- **Abilitate Socială**: Interacțiunea prin limbaj natural cu thread-uri de conversație

### Componente Tehnice
- **AIAgent**: Orchestrarea principală a agentului și gestionarea conversațiilor (.NET)
- **Funcții de Instrumente**: Extinderea capabilităților agentului cu metode și atribute C#
- **Integrarea OpenAI**: Utilizarea modelelor de limbaj prin API-uri standardizate .NET
- **Managementul Mediului**: Configurare sigură și gestionarea acreditărilor cu DotNetEnv

## ⚙️ Cerințe Prealabile și Configurare

**Dependențe Necesare:**
- .NET 9.0 SDK sau mai recent
- Visual Studio 2022 sau VS Code cu extensia C#

**Pachete NuGet:**
- `Microsoft.Extensions.AI` - Abstracții AI de bază
- `Microsoft.Extensions.AI.OpenAI` - Integrare OpenAI (previzualizare)
- `DotNetEnv` - Gestionarea variabilelor de mediu

**Configurarea Mediului (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Stiva Tehnică

**Tehnologii de Bază:**
- Microsoft Agent Framework (.NET)
- Integrarea API-urilor GitHub Models
- Modele compatibile OpenAI
- Configurare bazată pe mediu cu DotNetEnv

**Capabilitățile Agentului:**
- Înțelegerea și generarea limbajului natural
- Apelarea funcțiilor și utilizarea instrumentelor cu atribute C#
- Răspunsuri conștiente de context cu thread-uri de conversație
- Arhitectură extensibilă cu modele de injecție de dependențe

## 📚 Comparație între Cadre

Acest exemplu demonstrează abordarea Microsoft Agent Framework în .NET comparativ cu alte platforme:

| Caracteristică | Cadru Agent .NET | Echivalente Python |
|----------------|------------------|--------------------|
| **Siguranța Tipurilor** | Tipizare strictă cu C# | Tipizare dinamică |
| **Integrare** | Ecosistem nativ .NET | Compatibilitate variată |
| **Performanță** | Performanță cod compilat | Execuție interpretată |
| **Pregătit pentru Enterprise** | Construit pentru aplicații .NET de producție | Variază în funcție de cadru |
| **Instrumente** | Integrare Visual Studio | Dependent de IDE |

## 🚀 Începe

Urmează celulele de mai jos pentru a construi primul tău agent de bază în .NET și pentru a înțelege conceptele agentice fundamentale!

## 📦 Instalare și Configurare

Acest exemplu este disponibil ca o aplicație .NET Single File App. Vezi fișierul `02-dotnet-agent-framework.cs` însoțitor pentru implementarea completă.

Pentru a rula acest exemplu:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Sau folosind CLI-ul dotnet:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Prezentare Generală a Codului

Implementarea completă include:

### 1. Dependențe ale Pachetelor

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

### 2. Importuri Esențiale

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Configurarea Mediului

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definirea Funcțiilor de Instrumente

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

### 5. Configurarea și Setarea Clientului

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

### 6. Configurarea Agentului

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

### 7. Inițializarea Agentului

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

### 8. Gestionarea Conversației

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Concluzii Cheie

1. **Arhitectura Agentului**: Microsoft Agent Framework oferă o abordare curată și sigură din punct de vedere al tipurilor pentru construirea agenților AI în .NET
2. **Integrarea Instrumentelor**: Funcțiile decorate cu atribute `[Description]` devin instrumente disponibile pentru agent
3. **Contextul Conversației**: Managementul thread-urilor permite conversații multi-turn cu conștientizare completă a contextului
4. **Managementul Configurării**: Variabilele de mediu și gestionarea sigură a acreditărilor urmează cele mai bune practici .NET
5. **Compatibilitate OpenAI**: Integrarea GitHub Models funcționează perfect prin API-uri compatibile OpenAI

## 🔗 Resurse Suplimentare

- [Documentația Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Piața GitHub Models](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [Aplicații .NET Single File](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.