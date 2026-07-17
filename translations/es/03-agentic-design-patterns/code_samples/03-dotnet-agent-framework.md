# 🎨 Patrones de Diseño Agéncico con Azure OpenAI (Responses API) (.NET)

## 📋 Objetivos de Aprendizaje

Este ejemplo demuestra patrones de diseño de nivel empresarial para construir agentes inteligentes usando el Microsoft Agent Framework en .NET con integración de Azure OpenAI (Responses API). Aprenderás patrones profesionales y enfoques arquitectónicos que hacen que los agentes estén listos para producción, sean mantenibles y escalables.

### Patrones de Diseño Empresarial

- 🏭 **Patrón Factory**: Creación estandarizada de agentes con inyección de dependencias
- 🔧 **Patrón Builder**: Configuración y setup fluido del agente
- 🧵 **Patrones Thread-Safe**: Gestión concurrente de conversaciones
- 📋 **Patrón Repository**: Gestión organizada de herramientas y capacidades

## 🎯 Beneficios Arquitectónicos Específicos de .NET

### Funcionalidades Empresariales

- **Tipado Fuerte**: Validación en tiempo de compilación y soporte IntelliSense
- **Inyección de Dependencias**: Integración de contenedor DI incorporado
- **Gestión de Configuración**: Patrones IConfiguration y Options
- **Async/Await**: Soporte de primera clase a programación asíncrona

### Patrones Listos para Producción

- **Integración de Logging**: ILogger y soporte de logging estructurado
- **Health Checks**: Monitorización y diagnóstico incorporados
- **Validación de Configuración**: Tipado fuerte con anotaciones de datos
- **Manejo de Errores**: Gestión estructurada de excepciones

## 🔧 Arquitectura Técnica

### Componentes Core de .NET

- **Microsoft.Extensions.AI**: Abstracciones unificadas de servicio AI
- **Microsoft.Agents.AI**: Framework empresarial de orquestación de agentes
- **Azure OpenAI (Responses API)**: Patrones para clientes API de alto rendimiento
- **Sistema de Configuración**: appsettings.json e integración con el entorno

### Implementación del Patrón de Diseño

```mermaid
graph LR
    A[IServiceCollection] --> B[Constructor de Agente]
    B --> C[Configuración]
    C --> D[Registro de Herramientas]
    D --> E[Agente de IA]
```

## 🏗️ Patrones Empresariales Demostrados

### 1. **Patrones Creacionales**

- **Agent Factory**: Creación centralizada de agentes con configuración consistente
- **Patrón Builder**: API fluida para configuración compleja de agentes
- **Patrón Singleton**: Recursos compartidos y gestión de configuración
- **Inyección de Dependencias**: Acoplamiento débil y facilidad para pruebas

### 2. **Patrones de Comportamiento**

- **Patrón Strategy**: Estrategias intercambiables de ejecución de herramientas
- **Patrón Command**: Operaciones de agente encapsuladas con deshacer/rehacer
- **Patrón Observer**: Gestión del ciclo de vida del agente basada en eventos
- **Patrón Template Method**: Flujos de ejecución estandarizados para agentes

### 3. **Patrones Estructurales**

- **Patrón Adapter**: Capa de integración con Azure OpenAI (Responses API)
- **Patrón Decorator**: Mejora de capacidades del agente
- **Patrón Facade**: Interfaces simplificadas para interacción con agentes
- **Patrón Proxy**: Carga diferida y caché para mejorar rendimiento

## 📚 Principios de Diseño en .NET

### Principios SOLID

- **Responsabilidad Única**: Cada componente tiene un propósito claro
- **Abierto/Cerrado**: Extensible sin modificar
- **Sustitución de Liskov**: Implementaciones de herramientas basadas en interfaces
- **Segregación de Interfaces**: Interfaces enfocadas y cohesivas
- **Inversión de Dependencias**: Depende de abstracciones, no concreciones

### Arquitectura Limpia

- **Capa de Dominio**: Abstracciones centrales de agentes y herramientas
- **Capa de Aplicación**: Orquestación y flujos de agentes
- **Capa de Infraestructura**: Integración con Azure OpenAI (Responses API) y servicios externos
- **Capa de Presentación**: Interacción usuario y formato de respuesta

## 🔒 Consideraciones Empresariales

### Seguridad

- **Gestión de Credenciales**: Manejo seguro de claves API con IConfiguration
- **Validación de Inputs**: Tipado fuerte y validación con anotaciones de datos
- **Saneamiento de Salidas**: Procesamiento y filtrado seguro de respuestas
- **Registro de Auditoría**: Seguimiento completo de operaciones

### Rendimiento

- **Patrones Asíncronos**: Operaciones I/O sin bloqueo
- **Pooling de Conexiones**: Gestión eficiente de clientes HTTP
- **Caching**: Caché de respuestas para mejorar el rendimiento
- **Gestión de Recursos**: Patrones adecuados de liberación y limpieza

### Escalabilidad

- **Seguridad en Hilos**: Soporte para ejecución concurrente de agentes
- **Pooling de Recursos**: Utilización eficiente de recursos
- **Gestión de Carga**: Limitación de tasa y manejo de retropresión
- **Monitorización**: Métricas de rendimiento y health checks

## 🚀 Despliegue en Producción

- **Gestión de Configuración**: Ajustes específicos por entorno
- **Estrategia de Logging**: Registro estructurado con IDs de correlación
- **Manejo de Errores**: Captura global de excepciones con recuperación adecuada
- **Monitorización**: Application insights y contadores de rendimiento
- **Pruebas**: Tests unitarios, integración y patrones de pruebas de carga

¿Listo para construir agentes inteligentes de nivel empresarial con .NET? ¡Vamos a diseñar algo robusto! 🏢✨

## 🚀 Empezando

### Requisitos Previos

- [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) o superior
- Una [suscripción de Azure](https://azure.microsoft.com/free/) con un recurso Azure OpenAI y un despliegue de modelo
- La [CLI de Azure](https://learn.microsoft.com/cli/azure/install-azure-cli) — inicia sesión con `az login`

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
# Luego inicie sesión para que AzureCliCredential pueda obtener un token
az login
```

### Código de Ejemplo

Para ejecutar el ejemplo de código,

```bash
# zsh/bash
chmod +x ./03-dotnet-agent-framework.cs
./03-dotnet-agent-framework.cs
```

O usando la CLI de dotnet:

```bash
dotnet run ./03-dotnet-agent-framework.cs
```

Consulta [`03-dotnet-agent-framework.cs`](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs) para el código completo.

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

// Create New Conversation Session for Context Management
// Initialize a new conversation session to maintain context across multiple interactions
// Sessions enable the agent to remember previous exchanges and maintain conversational state
// This is essential for multi-turn conversations and contextual understanding
var session = await agent.CreateSessionAsync();

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

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->