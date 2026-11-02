# 🌍 Agente de Viajes con IA usando Microsoft Agent Framework (.NET)

## 📋 Descripción del Escenario

Este ejemplo demuestra cómo construir un agente inteligente de planificación de viajes usando Microsoft Agent Framework para .NET. El agente puede generar automáticamente itinerarios personalizados de excursiones de un día a destinos aleatorios alrededor del mundo.

### Capacidades Clave:

- 🎲 **Selección Aleatoria de Destinos**: Usa una herramienta personalizada para elegir lugares de vacaciones
- 🗺️ **Planificación Inteligente de Viajes**: Crea itinerarios detallados día a día
- 🔄 **Transmisión en Tiempo Real**: Soporta respuestas inmediatas y por streaming
- 🛠️ **Integración de Herramientas Personalizadas**: Demuestra cómo extender las capacidades del agente

## 🔧 Arquitectura Técnica

### Tecnologías Principales

- **Microsoft Agent Framework**: Implementación más reciente en .NET para desarrollo de agentes IA
- **Azure OpenAI (API de Respuestas)**: Usa la API de respuestas de Azure OpenAI para inferencia del modelo
- **Azure Identity**: Inicio de sesión seguro mediante `AzureCliCredential` (`az login`)
- **Configuración Segura**: Gestión de endpoints basada en el entorno

### Componentes Clave

1. **AIAgent**: El orquestador principal que maneja el flujo de la conversación
2. **Herramientas Personalizadas**: Función `GetRandomDestination()` disponible para el agente
3. **Cliente de Respuestas**: Interfaz de conversación basada en Azure OpenAI Responses
4. **Soporte para Streaming**: Capacidades de generación de respuestas en tiempo real

### Patrón de Integración

```mermaid
graph LR
    A[Solicitud del Usuario] --> B[Agente de IA]
    B --> C[Azure OpenAI (API de Respuestas)]
    B --> D[Herramienta ObtenerDestinoAleatorio]
    C --> E[Itinerario de Viaje]
    D --> E
```

## 🚀 Cómo Empezar

### Requisitos Previos

- [SDK .NET 10](https://dotnet.microsoft.com/download/dotnet/10.0) o superior
- Una [suscripción a Azure](https://azure.microsoft.com/free/) con un recurso Azure OpenAI y un despliegue de modelo
- La [CLI de Azure](https://learn.microsoft.com/cli/azure/install-azure-cli) — iniciar sesión con `az login`

### Variables de Entorno Requeridas

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
export AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
# Luego inicia sesión para que AzureCliCredential pueda obtener un token
az login
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<your-resource>.openai.azure.com"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5-mini"
# Luego inicie sesión para que AzureCliCredential pueda obtener un token
az login
```

### Código de Ejemplo

Para ejecutar el ejemplo de código,

```bash
# zsh/bash
chmod +x ./01-dotnet-agent-framework.cs
./01-dotnet-agent-framework.cs
```

O usando la CLI de dotnet:

```bash
dotnet run ./01-dotnet-agent-framework.cs
```

Ver [`01-dotnet-agent-framework.cs`](../../../../01-intro-to-ai-agents/code_samples/01-dotnet-agent-framework.cs) para el código completo.

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

## 🎓 Puntos Clave

1. **Arquitectura de Agentes**: Microsoft Agent Framework ofrece un enfoque limpio y seguro en tipos para construir agentes IA en .NET
2. **Integración de Herramientas**: Las funciones decoradas con atributos `[Description]` se vuelven herramientas disponibles para el agente
3. **Gestión de Configuración**: Uso de variables de entorno y manejo seguro de credenciales siguiendo las mejores prácticas de .NET
4. **API de Respuestas de Azure OpenAI**: El agente utiliza la API de Respuestas Azure OpenAI a través del SDK Azure.AI.OpenAI

## 🔗 Recursos Adicionales

- [Documentación de Microsoft Agent Framework](https://learn.microsoft.com/agent-framework)
- [Azure OpenAI en Microsoft Foundry](https://learn.microsoft.com/azure/ai-services/openai/)
- [Microsoft.Extensions.AI](https://learn.microsoft.com/dotnet/ai/microsoft-extensions-ai)
- [Aplicaciones de archivo único .NET](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->