<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "033f170be3b54183e2f6b5463371ab69",
  "translation_date": "2025-11-07T09:35:20+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "pl"
}
-->
# 🔍 Eksploracja Agentowych Ram - Podstawowy Agent (.NET)

## 📋 Cele Nauki

Ten notebook bada podstawowe pojęcia Microsoft Agent Framework poprzez implementację prostego agenta w .NET. Nauczysz się kluczowych wzorców agentowych i zrozumiesz, jak działają inteligentni agenci w ekosystemie C# i .NET.

**Czego się dowiesz:**
- 🏗️ **Architektura Agenta**: Zrozumienie podstawowej struktury agentów AI w .NET
- 🛠️ **Integracja Narzędzi**: Jak agenci korzystają z zewnętrznych funkcji, aby rozszerzyć swoje możliwości  
- 💬 **Przepływ Rozmowy**: Zarządzanie rozmowami wieloetapowymi i kontekstem za pomocą zarządzania wątkami
- 🔧 **Wzorce Konfiguracji**: Najlepsze praktyki dotyczące konfiguracji i zarządzania agentami w .NET

## 🎯 Kluczowe Koncepcje

### Zasady Ram Agentowych
- **Autonomia**: Jak agenci podejmują niezależne decyzje, korzystając z abstrakcji AI w .NET
- **Reaktywność**: Reagowanie na zmiany w środowisku i dane wejściowe użytkownika
- **Proaktywność**: Podejmowanie inicjatywy na podstawie celów i kontekstu
- **Zdolność Społeczna**: Interakcja za pomocą języka naturalnego z wątkami rozmów

### Komponenty Techniczne
- **AIAgent**: Orkiestracja agenta i zarządzanie rozmowami (.NET)
- **Funkcje Narzędziowe**: Rozszerzanie możliwości agenta za pomocą metod i atrybutów C#
- **Integracja OpenAI**: Wykorzystanie modeli językowych poprzez standardowe API .NET
- **Zarządzanie Środowiskiem**: Bezpieczna konfiguracja i obsługa poświadczeń za pomocą DotNetEnv

## ⚙️ Wymagania i Konfiguracja

**Wymagane Zależności:**
- .NET 9.0 SDK lub nowszy
- Visual Studio 2022 lub VS Code z rozszerzeniem C#

**Pakiety NuGet:**
- `Microsoft.Extensions.AI` - Podstawowe abstrakcje AI
- `Microsoft.Extensions.AI.OpenAI` - Integracja OpenAI (wersja preview)
- `DotNetEnv` - Zarządzanie zmiennymi środowiskowymi

**Konfiguracja Środowiska (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 🔧 Stos Technologiczny

**Podstawowe Technologie:**
- Microsoft Agent Framework (.NET)
- Integracja z API modeli GitHub
- Wzorce klienta kompatybilne z OpenAI
- Konfiguracja oparta na środowisku z DotNetEnv

**Możliwości Agenta:**
- Rozumienie i generowanie języka naturalnego
- Wywoływanie funkcji i korzystanie z narzędzi za pomocą atrybutów C#
- Odpowiedzi uwzględniające kontekst dzięki wątkom rozmów
- Rozszerzalna architektura z wzorcami wstrzykiwania zależności

## 📚 Porównanie Ram

Ten przykład pokazuje podejście Microsoft Agent Framework w .NET w porównaniu z innymi platformami:

| Funkcja | Ramy Agenta .NET | Odpowiedniki w Pythonie |
|---------|------------------|-------------------------|
| **Bezpieczeństwo Typów** | Silne typowanie w C# | Typowanie dynamiczne |
| **Integracja** | Rodzimy ekosystem .NET | Zróżnicowana kompatybilność |
| **Wydajność** | Wydajność kodu kompilowanego | Wykonanie interpretowane |
| **Gotowość dla Przedsiębiorstw** | Stworzony dla aplikacji produkcyjnych .NET | Zależy od ram |
| **Narzędzia** | Integracja z Visual Studio | Zależne od IDE |

## 🚀 Rozpoczęcie

Postępuj zgodnie z poniższymi krokami, aby zbudować swojego pierwszego podstawowego agenta w .NET i zrozumieć podstawowe koncepcje agentowe!

## 📦 Instalacja i Konfiguracja

Ten przykład jest dostępny jako uruchamialna aplikacja .NET Single File App. Zobacz dołączony plik `02-dotnet-agent-framework.cs` dla pełnej implementacji.

Aby uruchomić ten przykład:

```bash
chmod +x 02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

Lub używając dotnet CLI:

```bash
dotnet run 02-dotnet-agent-framework.cs
```

## 💡 Przegląd Kodowania

Kompletna implementacja obejmuje:

### 1. Zależności Pakietów

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

### 2. Podstawowe Importy

```csharp
using System;
using System.ComponentModel;
using System.ClientModel;
using Microsoft.Extensions.AI;
using Microsoft.Agents.AI;
using OpenAI;
using DotNetEnv;
```

### 3. Konfiguracja Środowiska

```csharp
// Load configuration from .env file
Env.Load("../../../.env");
```

### 4. Definicja Funkcji Narzędziowych

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

### 5. Konfiguracja i Ustawienia Klienta

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

### 6. Konfiguracja Agenta

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

### 7. Inicjalizacja Agenta

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

### 8. Zarządzanie Rozmowami

```csharp
// Create new conversation thread
AgentThread thread = agent.GetNewThread();

// Execute agent: First travel planning request
Console.WriteLine(await agent.RunAsync("Plan me a day trip", thread));

// Execute agent: Follow-up request with context awareness
Console.WriteLine(await agent.RunAsync("I don't like that destination. Plan me another vacation.", thread));
```

## 🎓 Kluczowe Wnioski

1. **Architektura Agenta**: Microsoft Agent Framework oferuje czyste, bezpieczne typowo podejście do budowy agentów AI w .NET
2. **Integracja Narzędzi**: Funkcje oznaczone atrybutami `[Description]` stają się dostępne jako narzędzia dla agenta
3. **Kontekst Rozmowy**: Zarządzanie wątkami umożliwia rozmowy wieloetapowe z pełną świadomością kontekstu
4. **Zarządzanie Konfiguracją**: Zmienne środowiskowe i bezpieczna obsługa poświadczeń zgodnie z najlepszymi praktykami .NET
5. **Kompatybilność z OpenAI**: Integracja z modelami GitHub działa płynnie poprzez kompatybilne API OpenAI

## 🔗 Dodatkowe Zasoby

- [Dokumentacja Microsoft Agent Framework](https://learn.microsoft.com/en-us/dotnet/ai/agents)
- [Marketplace Modeli GitHub](https://github.com/marketplace/models)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai-overview)
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.