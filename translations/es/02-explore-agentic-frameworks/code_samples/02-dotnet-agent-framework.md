<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e23058f87779da210fc0257ee2747c53",
  "translation_date": "2025-11-13T10:53:29+00:00",
  "source_file": "02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.md",
  "language_code": "es"
}
-->
# 🔍 Explorando el Marco de Agentes de Microsoft - Agente Básico (.NET)

## 📋 Objetivos de Aprendizaje

Este ejemplo explora los conceptos fundamentales del Marco de Agentes de Microsoft a través de una implementación básica de un agente en .NET. Aprenderás patrones básicos de agentes y comprenderás cómo funcionan los agentes inteligentes detrás de escena utilizando C# y el ecosistema .NET.

### Lo que Descubrirás

- 🏗️ **Arquitectura de Agentes**: Comprender la estructura básica de los agentes de IA en .NET  
- 🛠️ **Integración de Herramientas**: Cómo los agentes utilizan funciones externas para ampliar capacidades  
- 💬 **Flujo de Conversación**: Gestionar conversaciones de múltiples turnos y contexto con manejo de hilos  
- 🔧 **Patrones de Configuración**: Mejores prácticas para la configuración y gestión de agentes en .NET  

## 🎯 Conceptos Clave Cubiertos

### Principios del Marco de Agentes

- **Autonomía**: Cómo los agentes toman decisiones independientes utilizando abstracciones de IA en .NET  
- **Reactividad**: Responder a cambios en el entorno y entradas del usuario  
- **Proactividad**: Tomar la iniciativa basada en objetivos y contexto  
- **Habilidad Social**: Interactuar mediante lenguaje natural con hilos de conversación  

### Componentes Técnicos

- **AIAgent**: Orquestación central del agente y gestión de conversaciones (.NET)  
- **Funciones de Herramientas**: Ampliar las capacidades del agente con métodos y atributos de C#  
- **Integración con OpenAI**: Aprovechar modelos de lenguaje a través de APIs estandarizadas de .NET  
- **Configuración Segura**: Gestión de claves API basada en el entorno  

## 🔧 Stack Técnico

### Tecnologías Principales

- Marco de Agentes de Microsoft (.NET)  
- Integración con API de Modelos de GitHub  
- Patrones de cliente compatibles con OpenAI  
- Configuración basada en entorno con DotNetEnv  

### Capacidades del Agente

- Comprensión y generación de lenguaje natural  
- Llamadas a funciones y uso de herramientas con atributos de C#  
- Respuestas conscientes del contexto con hilos de conversación  
- Arquitectura extensible con patrones de inyección de dependencias  

## 📚 Comparación de Marcos

Este ejemplo demuestra el enfoque del Marco de Agentes de Microsoft en comparación con otros marcos de agentes:

| Característica | Marco de Agentes de Microsoft | Otros Marcos |
|----------------|-------------------------------|--------------|
| **Integración** | Ecosistema nativo de Microsoft | Compatibilidad variada |
| **Simplicidad** | API limpia e intuitiva | Configuración frecuentemente compleja |
| **Extensibilidad** | Integración fácil de herramientas | Dependiente del marco |
| **Preparado para Empresas** | Diseñado para producción | Varía según el marco |

## 🚀 Comenzando

### Requisitos Previos

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o superior  
- [Token de acceso a la API de Modelos de GitHub](https://docs.github.com/github-models/github-models-at-scale/using-your-own-api-keys-in-github-models)  

### Variables de Entorno Requeridas

```bash
# zsh/bash
export GH_TOKEN=<your_github_token>
export GH_ENDPOINT=https://models.github.ai/inference
export GH_MODEL_ID=openai/gpt-5-mini
```
  
```powershell
# PowerShell
$env:GH_TOKEN = "<your_github_token>"
$env:GH_ENDPOINT = "https://models.github.ai/inference"
$env:GH_MODEL_ID = "openai/gpt-5-mini"
```
  

### Código de Ejemplo

Para ejecutar el ejemplo de código,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```
  
O utilizando la CLI de dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```
  
Consulta [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) para el código completo.

```csharp
#!/usr/bin/dotnet run

#:package Microsoft.Extensions.AI@10.*
#:package Microsoft.Agents.AI.OpenAI@1.*-*

using System.ClientModel;
using System.ComponentModel;

using Microsoft.Agents.AI;
using Microsoft.Extensions.AI;

using OpenAI;

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

// Extract configuration from environment variables
// Retrieve the GitHub Models API endpoint, defaults to https://models.github.ai/inference if not specified
// Retrieve the model ID, defaults to openai/gpt-5-mini if not specified
// Retrieve the GitHub token for authentication, throws exception if not specified
var github_endpoint = Environment.GetEnvironmentVariable("GH_ENDPOINT") ?? "https://models.github.ai/inference";
var github_model_id = Environment.GetEnvironmentVariable("GH_MODEL_ID") ?? "openai/gpt-5-mini";
var github_token = Environment.GetEnvironmentVariable("GH_TOKEN") ?? throw new InvalidOperationException("GH_TOKEN is not set.");

// Configure OpenAI Client Options
// Create configuration options to point to GitHub Models endpoint
// This redirects OpenAI client calls to GitHub's model inference service
var openAIOptions = new OpenAIClientOptions()
{
    Endpoint = new Uri(github_endpoint)
};

// Initialize OpenAI Client with GitHub Models Configuration
// Create OpenAI client using GitHub token for authentication
// Configure it to use GitHub Models endpoint instead of OpenAI directly
var openAIClient = new OpenAIClient(new ApiKeyCredential(github_token), openAIOptions);

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
// Initialize complete agent pipeline: OpenAI client → Chat client → AI agent
// Configure agent with name, detailed instructions, and available tools
// This demonstrates the .NET agent creation pattern with full configuration
AIAgent agent = openAIClient
    .GetChatClient(github_model_id)
    .CreateAIAgent(
        name: AGENT_NAME,
        instructions: AGENT_INSTRUCTIONS,
        tools: [AIFunctionFactory.Create(GetRandomDestination)]
    );

// Create New Conversation Thread for Context Management
// Initialize a new conversation thread to maintain context across multiple interactions
// Threads enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
AgentThread thread = agent.GetNewThread();

// Execute Agent: First Travel Planning Request
// Run the agent with an initial request that will likely trigger the random destination tool
// The agent will analyze the request, use the GetRandomDestination tool, and create an itinerary
// Using the thread parameter maintains conversation context for subsequent interactions
await foreach (var update in agent.RunStreamingAsync("Plan me a day trip", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}

Console.WriteLine();

// Execute Agent: Follow-up Request with Context Awareness
// Demonstrate contextual conversation by referencing the previous response
// The agent remembers the previous destination suggestion and will provide an alternative
// This showcases the power of conversation threads and contextual understanding in .NET agents
await foreach (var update in agent.RunStreamingAsync("I don't like that destination. Plan me another vacation.", thread))
{
    await Task.Delay(10);
    Console.Write(update);
}
```
  

## 🎓 Puntos Clave

1. **Arquitectura de Agentes**: El Marco de Agentes de Microsoft proporciona un enfoque limpio y seguro para construir agentes de IA en .NET  
2. **Integración de Herramientas**: Las funciones decoradas con atributos `[Description]` se convierten en herramientas disponibles para el agente  
3. **Contexto de Conversación**: La gestión de hilos permite conversaciones de múltiples turnos con plena conciencia del contexto  
4. **Gestión de Configuración**: Las variables de entorno y el manejo seguro de credenciales siguen las mejores prácticas de .NET  
5. **Compatibilidad con OpenAI**: La integración con Modelos de GitHub funciona perfectamente a través de APIs compatibles con OpenAI  

## 🔗 Recursos Adicionales

- [Documentación del Marco de Agentes de Microsoft](https://learn.microsoft.com/agent-framework)  
- [Marketplace de Modelos de GitHub](https://github.com/marketplace?type=models)  
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)  
- [.NET Single File Apps](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->