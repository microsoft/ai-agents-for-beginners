# 🛠️ Uso Avanzado de Herramientas con Azure OpenAI (API de Respuestas) (.NET)

## 📋 Objetivos de Aprendizaje

Este cuaderno demuestra patrones de integración de herramientas de nivel empresarial usando el Microsoft Agent Framework en .NET con Azure OpenAI (API de Respuestas). Aprenderás a construir agentes sofisticados con múltiples herramientas especializadas, aprovechando el tipado fuerte de C# y las características empresariales de .NET.

### Capacidades Avanzadas de Herramientas que Dominarás

- 🔧 **Arquitectura Multi-Herramienta**: Construcción de agentes con múltiples capacidades especializadas
- 🎯 **Ejecución de Herramientas con Tipado Seguro**: Aprovechando la validación en tiempo de compilación de C#
- 📊 **Patrones Empresariales de Herramientas**: Diseño de herramientas listas para producción y manejo de errores
- 🔗 **Composición de Herramientas**: Combinando herramientas para flujos de trabajo empresariales complejos

## 🎯 Beneficios de la Arquitectura de Herramientas .NET

### Características Empresariales de las Herramientas

- **Validación en Tiempo de Compilación**: El tipado fuerte asegura la corrección de parámetros de las herramientas
- **Inyección de Dependencias**: Integración con contenedor IoC para gestión de herramientas
- **Patrones Async/Await**: Ejecución de herramientas sin bloqueo con manejo adecuado de recursos
- **Registro Estructurado**: Integración incorporada para monitoreo de ejecución de herramientas

### Patrones Listos para Producción

- **Manejo de Excepciones**: Gestión completa de errores con excepciones tipadas
- **Gestión de Recursos**: Patrones correctos de disposición y gestión de memoria
- **Monitoreo de Rendimiento**: Métricas y contadores de rendimiento integrados
- **Gestión de Configuración**: Configuración con tipado seguro y validación

## 🔧 Arquitectura Técnica

### Componentes Clave de Herramientas .NET

- **Microsoft.Extensions.AI**: Capa unificada de abstracción de herramientas
- **Microsoft.Agents.AI**: Orquestación de herramientas de nivel empresarial
- **Azure OpenAI (API de Respuestas)**: Cliente API de alto rendimiento con agrupamiento de conexiones

### Pipeline de Ejecución de Herramientas

```mermaid
graph LR
    A[Solicitud del Usuario] --> B[Análisis del Agente]
    B --> C[Selección de Herramienta]
    C --> D[Validación de Tipo]
    B --> E[Vinculación de Parámetros]
    E --> F[Ejecución de Herramienta]
    C --> F
    F --> G[Procesamiento de Resultados]
    D --> G
    G --> H[Respuesta]
```

## 🛠️ Categorías y Patrones de Herramientas

### 1. **Herramientas de Procesamiento de Datos**

- **Validación de Entrada**: Tipado fuerte con anotaciones de datos
- **Operaciones de Transformación**: Conversión y formateo de datos con tipado seguro
- **Lógica de Negocio**: Herramientas de cálculo y análisis específicos del dominio
- **Formato de Salida**: Generación estructurada de respuestas

### 2. **Herramientas de Integración** 

- **Conectores API**: Integración de servicios RESTful con HttpClient
- **Herramientas de Base de Datos**: Integración con Entity Framework para acceso a datos
- **Operaciones de Archivos**: Operaciones seguras en el sistema de archivos con validación
- **Servicios Externos**: Patrones de integración con servicios de terceros

### 3. **Herramientas Utilitarias**

- **Procesamiento de Texto**: Utilidades para manipulación y formateo de cadenas
- **Operaciones de Fecha/Hora**: Cálculos de fecha/hora con reconocimiento cultural
- **Herramientas Matemáticas**: Cálculos de precisión y operaciones estadísticas
- **Herramientas de Validación**: Validación de reglas de negocio y verificación de datos

¿Listo para construir agentes de nivel empresarial con potentes herramientas de tipado seguro en .NET? ¡Vamos a diseñar soluciones profesionales! 🏢⚡

## 🚀 Comenzando

### Requisitos Previos

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) o superior
- Una [suscripción de Azure](https://azure.microsoft.com/free/) con un recurso Azure OpenAI y un despliegue de modelo
- La [CLI de Azure](https://learn.microsoft.com/cli/azure/install-azure-cli) — inicia sesión con `az login`

### Variables de Entorno Requeridas

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
# Luego inicia sesión para que AzureCliCredential pueda obtener un token
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
chmod +x ./04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

O usando la CLI dotnet:

```bash
dotnet run ./04-dotnet-agent-framework.cs
```

Consulta [`04-dotnet-agent-framework.cs`](../../../../04-tool-use/code_samples/04-dotnet-agent-framework.cs) para el código completo.

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
await using var session = await agent.CreateSessionAsync();

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