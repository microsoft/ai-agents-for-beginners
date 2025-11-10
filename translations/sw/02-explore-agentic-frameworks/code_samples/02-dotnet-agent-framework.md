<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:38:40+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "sw"
}
-->
# 🔍 Kuchunguza Mfumo wa Mawakala - Mwakala wa Msingi (.NET)

## 📋 Malengo ya Kujifunza

Notebook hii inachunguza dhana za msingi za Mfumo wa Mawakala wa Microsoft kupitia utekelezaji wa mwakala wa msingi katika .NET. Utajifunza mifumo ya msingi ya kiwakala na kuelewa jinsi mawakala wenye akili hufanya kazi kwa undani kwa kutumia C# na mfumo wa .NET.

**Unachojifunza:**
- 🏗️ **Muundo wa Mwakala**: Kuelewa muundo wa msingi wa mawakala wa AI katika .NET
- 🛠️ **Ujumuishaji wa Zana**: Jinsi mawakala wanavyotumia kazi za nje kupanua uwezo  
- 💬 **Mtiririko wa Mazungumzo**: Kusimamia mazungumzo ya mizunguko mingi na muktadha kwa usimamizi wa nyuzi
- 🔧 **Mifumo ya Usanidi**: Mbinu bora za usanidi na usimamizi wa mawakala katika .NET

## 🎯 Dhana Muhimu Zinazofunikwa

### Kanuni za Mfumo wa Mawakala
- **Uhuru**: Jinsi mawakala wanavyofanya maamuzi huru kwa kutumia dhana za AI za .NET
- **Uchangamfu**: Kujibu mabadiliko ya mazingira na pembejeo za mtumiaji
- **Uchukuaji Hatua**: Kuchukua hatua kulingana na malengo na muktadha
- **Uwezo wa Kijamii**: Kuingiliana kupitia lugha ya asili na nyuzi za mazungumzo

### Vipengele vya Kiufundi
- **AIAgent**: Usimamizi wa msingi wa mwakala na mazungumzo (.NET)
- **Kazi za Zana**: Kupanua uwezo wa mwakala kwa kutumia mbinu na sifa za C#
- **Ujumuishaji wa OpenAI**: Kutumia mifano ya lugha kupitia API za kawaida za .NET
- **Usimamizi wa Mazingira**: Usanidi salama na usimamizi wa hati za DotNetEnv

## ⚙️ Mahitaji na Usanidi

**Vifaa Vinavyohitajika:**
- .NET 9.0 SDK au zaidi
- Visual Studio 2022 au VS Code na kiendelezi cha C#

**Pakiti za NuGet:**
- `Microsoft.Extensions.AI` - Dhana za msingi za AI
- `Microsoft.Extensions.AI.OpenAI` - Ujumuishaji wa OpenAI (hakikisho)
- `DotNetEnv` - Usimamizi wa vigezo vya mazingira

**Usanidi wa Mazingira (faili .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Mfumo wa Kiufundi

**Teknolojia za Msingi:**
- Mfumo wa Mawakala wa Microsoft (.NET)
- Ujumuishaji wa API za GitHub Models
- Mifumo inayolingana na OpenAI
- Usanidi unaotegemea mazingira na DotNetEnv

**Uwezo wa Mwakala:**
- Uelewa wa lugha ya asili na uzalishaji
- Kuita kazi na kutumia zana kwa sifa za C#
- Majibu yanayojali muktadha na nyuzi za mazungumzo
- Muundo unaoweza kupanuliwa na mifumo ya sindikizo la utegemezi

## 📚 Ulinganisho wa Mfumo

Mfano huu unaonyesha mbinu ya Mfumo wa Mawakala wa Microsoft katika .NET ikilinganishwa na majukwaa mengine:

| Kipengele | Mfumo wa Mawakala wa .NET | Sawa za Python |
|-----------|---------------------------|----------------|
| **Usalama wa Aina** | Utypaji thabiti na C# | Utypaji wa nguvu |
| **Ujumuishaji** | Mfumo wa asili wa .NET | Ulinganifu tofauti |
| **Utendaji** | Utendaji wa msimbo uliosimbwa | Utekelezaji wa kutafsiriwa |
| **Uwezo wa Biashara** | Imeundwa kwa programu za uzalishaji za .NET | Inategemea mfumo |
| **Zana** | Ujumuishaji wa Visual Studio | Inategemea IDE |

## 🚀 Kuanza

Fuata seli zilizo hapa chini ili kujenga mwakala wako wa msingi katika .NET na kuelewa dhana za msingi za kiwakala!

## 📦 Usakinishaji na Usanidi

Mfano huu unapatikana kama programu ya faili moja ya .NET inayoweza kuendeshwa. Tazama faili inayosindikiza `02-dotnet-agent-framework.cs` kwa utekelezaji kamili.

Ili kuendesha mfano huu:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Au kwa kutumia dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Ufafanuzi wa Msimbo

Utekelezaji kamili unajumuisha:

### 1. Utegemezi wa Pakiti

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

### 2. Uingizaji Muhimu

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Usanidi wa Mazingira

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Ufafanuzi wa Kazi za Zana

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

### 5. Usanidi na Utekelezaji wa Mteja

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

### 6. Usanidi wa Mwakala

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

### 7. Uanzishaji wa Mwakala

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

### 8. Usimamizi wa Mazungumzo

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Mambo Muhimu ya Kujifunza

1. **Muundo wa Mwakala**: Mfumo wa Mawakala wa Microsoft hutoa mbinu safi, salama kwa aina za kujenga mawakala wa AI katika .NET
2. **Ujumuishaji wa Zana**: Kazi zilizopambwa na sifa za `[Description]` zinakuwa zana zinazopatikana kwa mwakala
3. **Muktadha wa Mazungumzo**: Usimamizi wa nyuzi unaruhusu mazungumzo ya mizunguko mingi yenye ufahamu kamili wa muktadha
4. **Usimamizi wa Usanidi**: Vigezo vya mazingira na usimamizi salama wa hati hufuata mbinu bora za .NET
5. **Ulinganifu wa OpenAI**: Ujumuishaji wa GitHub Models hufanya kazi bila matatizo kupitia API zinazolingana na OpenAI

## 🔗 Rasilimali za Ziada

- [Nyaraka za Mfumo wa Mawakala wa Microsoft](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Soko la GitHub Models](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.