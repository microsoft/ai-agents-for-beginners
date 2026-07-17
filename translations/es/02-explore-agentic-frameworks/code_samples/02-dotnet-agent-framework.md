# 🔍 Explorando Microsoft Agent Framework - Agente Básico (.NET)

## 📋 Objetivos de Aprendizaje

Este ejemplo explora los conceptos fundamentales del Microsoft Agent Framework a través de una implementación básica de agente en .NET. Aprenderás patrones agénticos clave y entenderás cómo funcionan los agentes inteligentes internamente usando C# y el ecosistema .NET.

### Lo Que Descubrirás

- 🏗️ **Arquitectura del Agente**: Comprender la estructura básica de los agentes de IA en .NET
- 🛠️ **Integración de Herramientas**: Cómo los agentes usan funciones externas para ampliar capacidades  
- 💬 **Flujo de Conversación**: Gestión de conversaciones de múltiples turnos y contexto con manejo de hilos
- 🔧 **Patrones de Configuración**: Mejores prácticas para la configuración y administración de agentes en .NET

## 🎯 Conceptos Clave Cubiertos

### Principios del Marco Agéntico

- **Autonomía**: Cómo los agentes toman decisiones independientes usando abstracciones de IA en .NET
- **Reactividad**: Responder a cambios ambientales y entradas del usuario
- **Proactividad**: Tomar la iniciativa basada en objetivos y contexto
- **Habilidad Social**: Interactuar a través del lenguaje natural con hilos de conversación

### Componentes Técnicos

- **AIAgent**: Orquestación central del agente y gestión de conversación (.NET)
- **Funciones de Herramientas**: Extender las capacidades del agente con métodos y atributos en C#
- **Integración con Azure OpenAI**: Aprovechar modelos de lenguaje mediante la API Azure OpenAI Responses
- **Configuración Segura**: Gestión de puntos finales basada en el entorno

## 🔧 Pila Técnica

### Tecnologías Principales

- Microsoft Agent Framework (.NET)
- Integración con Azure OpenAI (API Responses)
- Patrones del cliente Azure.AI.OpenAI
- Configuración basada en entorno con DotNetEnv

### Capacidades del Agente

- Comprensión y generación de lenguaje natural
- Llamadas a funciones y uso de herramientas con atributos C#
- Respuestas conscientes del contexto con sesiones de conversación
- Arquitectura extensible con patrones de inyección de dependencias

## 📚 Comparación de Frameworks

Este ejemplo demuestra el enfoque de Microsoft Agent Framework comparado con otros frameworks agénticos:

| Característica | Microsoft Agent Framework | Otros Frameworks |
|---------|-------------------------|------------------|
| **Integración** | Ecosistema nativo de Microsoft | Compatibilidad variada |
| **Simplicidad** | API limpia e intuitiva | Configuración a menudo compleja |
| **Extensibilidad** | Integración fácil de herramientas | Dependiente del framework |
| **Listo para Empresas** | Diseñado para producción | Varía según el framework |

## 🚀 Primeros Pasos

### Requisitos Previos

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o superior
- Una [suscripción a Azure](https://azure.microsoft.com/free/) con un recurso Azure OpenAI y un despliegue de modelo
- La [CLI de Azure](https://learn.microsoft.com/cli/azure/install-azure-cli) — iniciar sesión con `az login`

### Variables de Entorno Requeridas

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Luego inicie sesión para que AzureCliCredential pueda obtener un token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-4.1-mini"
# Luego inicia sesión para que AzureCliCredential pueda obtener un token
az login
```

### Código de Ejemplo

Para ejecutar el ejemplo de código,

```bash
# zsh/bash
chmod +x ./02-dotnet-agent-framework.cs
./02-dotnet-agent-framework.cs
```

O usando la CLI dotnet:

```bash
dotnet run ./02-dotnet-agent-framework.cs
```

Consulta [`02-dotnet-agent-framework.cs`](../../../../02-explore-agentic-frameworks/code_samples/02-dotnet-agent-framework.cs) para el código completo.

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
var deployment = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT") ?? "gpt-4.1-mini";

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

## 🎓 Puntos Clave

1. **Arquitectura del Agente**: Microsoft Agent Framework provee un enfoque limpio y seguro para construir agentes de IA en .NET
2. **Integración de Herramientas**: Las funciones decoradas con atributos `[Description]` se vuelven herramientas disponibles para el agente
3. **Contexto de Conversación**: La gestión de sesiones permite conversaciones de múltiples turnos con plena conciencia del contexto
4. **Gestión de Configuración**: Variables de entorno y manejo seguro de credenciales siguiendo las mejores prácticas de .NET
5. **API Azure OpenAI Responses**: El agente utiliza la API Azure OpenAI Responses mediante el SDK Azure.AI.OpenAI

## 🔗 Recursos Adicionales

- [Documentación Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI en Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Aplicaciones de Archivo Único .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->